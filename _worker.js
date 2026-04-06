const SESSION_COOKIE = "spl_session";
const SESSION_TTL_SECONDS = 60 * 60 * 24 * 30;
const JSON_HEADERS = {
  "content-type": "application/json; charset=UTF-8",
  "cache-control": "no-store"
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname.startsWith("/api/")) {
      return handleApi(request, env, url);
    }

    return env.ASSETS.fetch(request);
  }
};

async function handleApi(request, env, url) {
  if (request.method === "OPTIONS") {
    return new Response(null, { status: 204 });
  }

  try {
    if (url.pathname === "/api/login" && request.method === "POST") {
      return login(request, env);
    }

    if (url.pathname === "/api/logout" && request.method === "POST") {
      return logout(request, env);
    }

    if (url.pathname === "/api/state" && request.method === "GET") {
      const session = await requireSession(request, env);
      return jsonResponse(await buildUserState(env, session));
    }

    if (url.pathname === "/api/question-status" && request.method === "POST") {
      const session = await requireSession(request, env);
      return updateQuestionStatus(request, env, session);
    }

    if (url.pathname === "/api/part-state" && request.method === "POST") {
      const session = await requireSession(request, env);
      return updatePartState(request, env, session);
    }

    if (url.pathname === "/api/reset-progress" && request.method === "POST") {
      const session = await requireSession(request, env);
      return resetProgress(env, session);
    }

    return jsonResponse({ error: "Not found." }, 404);
  } catch (error) {
    if (error instanceof UnauthorizedError) {
      return jsonResponse({ error: error.message }, 401, {
        "set-cookie": clearSessionCookie()
      });
    }

    return jsonResponse(
      { error: error instanceof Error ? error.message : "Unexpected server error." },
      500
    );
  }
}

class UnauthorizedError extends Error {}

function jsonResponse(payload, status = 200, extraHeaders = {}) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: {
      ...JSON_HEADERS,
      ...extraHeaders
    }
  });
}

async function parseJson(request) {
  try {
    return await request.json();
  } catch {
    throw new Error("Invalid JSON payload.");
  }
}

function readCookie(request, name) {
  const cookieHeader = request.headers.get("cookie") || "";
  const cookies = cookieHeader.split(";").map((part) => part.trim());
  for (const cookie of cookies) {
    const [key, ...rest] = cookie.split("=");
    if (key === name) {
      return decodeURIComponent(rest.join("="));
    }
  }
  return null;
}

function sessionCookie(token) {
  return [
    `${SESSION_COOKIE}=${encodeURIComponent(token)}`,
    "Path=/",
    "HttpOnly",
    "Secure",
    "SameSite=Lax",
    `Max-Age=${SESSION_TTL_SECONDS}`
  ].join("; ");
}

function clearSessionCookie() {
  return [
    `${SESSION_COOKIE}=`,
    "Path=/",
    "HttpOnly",
    "Secure",
    "SameSite=Lax",
    "Max-Age=0"
  ].join("; ");
}

function getAuthDirectory(env) {
  if (!env.AUTH_USERS_JSON) {
    throw new Error("AUTH_USERS_JSON secret is missing.");
  }

  let parsed;
  try {
    parsed = JSON.parse(env.AUTH_USERS_JSON);
  } catch {
    throw new Error("AUTH_USERS_JSON is not valid JSON.");
  }

  if (!parsed || typeof parsed !== "object") {
    throw new Error("AUTH_USERS_JSON must be a JSON object.");
  }

  return parsed;
}

function resolveUserRecord(env, usernameInput) {
  const directory = getAuthDirectory(env);
  const wanted = String(usernameInput || "").trim().toLowerCase();
  const match = Object.entries(directory).find(([name]) => name.toLowerCase() === wanted);
  if (!match) return null;

  const [username, value] = match;
  if (typeof value === "string") {
    return {
      username,
      displayName: username,
      password: value
    };
  }

  if (value && typeof value === "object") {
    return {
      username,
      displayName: value.displayName || username,
      password: value.password || ""
    };
  }

  return null;
}

async function cleanupExpiredSessions(env) {
  await env.DB.prepare("DELETE FROM sessions WHERE expires_at <= ?")
    .bind(nowIso())
    .run();
}

async function requireSession(request, env) {
  await cleanupExpiredSessions(env);

  const token = readCookie(request, SESSION_COOKIE);
  if (!token) {
    throw new UnauthorizedError("Please sign in.");
  }

  const row = await env.DB.prepare(
    "SELECT session_id, username, display_name, expires_at FROM sessions WHERE session_id = ?"
  )
    .bind(token)
    .first();

  if (!row) {
    throw new UnauthorizedError("Please sign in.");
  }

  if (row.expires_at <= nowIso()) {
    await env.DB.prepare("DELETE FROM sessions WHERE session_id = ?").bind(token).run();
    throw new UnauthorizedError("Session expired.");
  }

  await env.DB.prepare("UPDATE sessions SET updated_at = ? WHERE session_id = ?")
    .bind(nowIso(), token)
    .run();

  return {
    token,
    username: row.username,
    displayName: row.display_name
  };
}

function nowIso() {
  return new Date().toISOString();
}

function plusDays(days) {
  return new Date(Date.now() + days * 24 * 60 * 60 * 1000).toISOString();
}

async function login(request, env) {
  const body = await parseJson(request);
  const usernameInput = String(body.username || "").trim();
  const passwordInput = String(body.password || "");

  if (!usernameInput || !passwordInput) {
    return jsonResponse({ error: "Username and password are required." }, 400);
  }

  const user = resolveUserRecord(env, usernameInput);
  if (!user || user.password !== passwordInput) {
    return jsonResponse({ error: "Incorrect username or password." }, 401);
  }

  await cleanupExpiredSessions(env);

  const sessionId = crypto.randomUUID();
  await env.DB.prepare(
    `INSERT INTO sessions (session_id, username, display_name, expires_at, created_at, updated_at)
     VALUES (?, ?, ?, ?, ?, ?)`
  )
    .bind(sessionId, user.username, user.displayName, plusDays(30), nowIso(), nowIso())
    .run();

  const payload = await buildUserState(env, user);
  return jsonResponse(payload, 200, {
    "set-cookie": sessionCookie(sessionId)
  });
}

async function logout(request, env) {
  const token = readCookie(request, SESSION_COOKIE);
  if (token) {
    await env.DB.prepare("DELETE FROM sessions WHERE session_id = ?").bind(token).run();
  }

  return jsonResponse({ ok: true }, 200, {
    "set-cookie": clearSessionCookie()
  });
}

async function updateQuestionStatus(request, env, session) {
  const body = await parseJson(request);
  const questionId = Number(body.questionId);
  const status = String(body.status || "none");

  if (!Number.isInteger(questionId) || questionId <= 0) {
    return jsonResponse({ error: "A valid questionId is required." }, 400);
  }

  if (!["mastered", "review", "none"].includes(status)) {
    return jsonResponse({ error: "Invalid status." }, 400);
  }

  if (status === "none") {
    await env.DB.prepare("DELETE FROM question_progress WHERE username = ? AND question_id = ?")
      .bind(session.username, questionId)
      .run();
  } else {
    await env.DB.prepare(
      `INSERT INTO question_progress (username, question_id, status, updated_at)
       VALUES (?, ?, ?, ?)
       ON CONFLICT(username, question_id) DO UPDATE SET
         status = excluded.status,
         updated_at = excluded.updated_at`
    )
      .bind(session.username, questionId, status, nowIso())
      .run();
  }

  return jsonResponse({ ok: true });
}

async function updatePartState(request, env, session) {
  const body = await parseJson(request);
  const questionId = Number(body.questionId);
  const partId = String(body.partId || "").trim();
  const selectedKeys = Array.isArray(body.selectedKeys)
    ? body.selectedKeys.map((key) => String(key))
    : [];
  const checked = Boolean(body.checked);
  const revealed = Boolean(body.revealed);
  const isCorrect =
    body.isCorrect === null || body.isCorrect === undefined ? null : Boolean(body.isCorrect);

  if (!Number.isInteger(questionId) || questionId <= 0) {
    return jsonResponse({ error: "A valid questionId is required." }, 400);
  }

  if (!partId) {
    return jsonResponse({ error: "A valid partId is required." }, 400);
  }

  await env.DB.prepare(
    `INSERT INTO part_state (
        username,
        question_id,
        part_id,
        selected_keys,
        checked,
        revealed,
        is_correct,
        updated_at
      )
      VALUES (?, ?, ?, ?, ?, ?, ?, ?)
      ON CONFLICT(username, question_id, part_id) DO UPDATE SET
        selected_keys = excluded.selected_keys,
        checked = excluded.checked,
        revealed = excluded.revealed,
        is_correct = excluded.is_correct,
        updated_at = excluded.updated_at`
  )
    .bind(
      session.username,
      questionId,
      partId,
      JSON.stringify(selectedKeys),
      checked ? 1 : 0,
      revealed ? 1 : 0,
      isCorrect === null ? null : isCorrect ? 1 : 0,
      nowIso()
    )
    .run();

  const records = await buildRecords(env, session.username);
  return jsonResponse({ ok: true, records });
}

async function resetProgress(env, session) {
  await env.DB.prepare("DELETE FROM question_progress WHERE username = ?")
    .bind(session.username)
    .run();

  return jsonResponse({ ok: true });
}

async function buildUserState(env, session) {
  const progressPromise = env.DB.prepare(
    "SELECT question_id, status FROM question_progress WHERE username = ?"
  )
    .bind(session.username)
    .all();

  const responsesPromise = env.DB.prepare(
    `SELECT question_id, part_id, selected_keys, checked, revealed
     FROM part_state
     WHERE username = ?`
  )
    .bind(session.username)
    .all();

  const [progressResult, responsesResult, records] = await Promise.all([
    progressPromise,
    responsesPromise,
    buildRecords(env, session.username)
  ]);

  const progress = {};
  for (const row of progressResult.results || []) {
    progress[row.question_id] = row.status;
  }

  const responses = {};
  for (const row of responsesResult.results || []) {
    if (!responses[row.question_id]) {
      responses[row.question_id] = {};
    }
    responses[row.question_id][row.part_id] = {
      selectedKeys: safeJsonArray(row.selected_keys),
      checked: Boolean(row.checked),
      revealed: Boolean(row.revealed)
    };
  }

  return {
    user: {
      username: session.username,
      displayName: session.displayName
    },
    progress,
    responses,
    records
  };
}

function safeJsonArray(value) {
  try {
    const parsed = JSON.parse(value || "[]");
    return Array.isArray(parsed) ? parsed.map((item) => String(item)) : [];
  } catch {
    return [];
  }
}

async function buildRecords(env, username) {
  const summaryResult = await env.DB.prepare(
    `SELECT
       COALESCE(SUM(CASE WHEN checked = 1 THEN 1 ELSE 0 END), 0) AS total_attempts,
       COALESCE(SUM(CASE WHEN checked = 1 AND is_correct = 1 THEN 1 ELSE 0 END), 0) AS correct_attempts,
       COALESCE(SUM(CASE WHEN revealed = 1 THEN 1 ELSE 0 END), 0) AS total_reveals
     FROM part_state
     WHERE username = ?`
  )
    .bind(username)
    .first();

  const answeredResult = await env.DB.prepare(
    `SELECT COUNT(*) AS answered_parts
     FROM part_state
     WHERE username = ? AND (checked = 1 OR revealed = 1)`
  )
    .bind(username)
    .first();

  const recentResult = await env.DB.prepare(
    `SELECT
       question_id,
       part_id,
       selected_keys,
       checked,
       revealed,
       is_correct,
       updated_at
     FROM part_state
     WHERE username = ?
     AND (checked = 1 OR revealed = 1)
     ORDER BY updated_at DESC
     LIMIT 12`
  )
    .bind(username)
    .all();

  const totalAttempts = Number(summaryResult?.total_attempts || 0);
  const correctAttempts = Number(summaryResult?.correct_attempts || 0);
  const totalReveals = Number(summaryResult?.total_reveals || 0);
  const answeredParts = Number(answeredResult?.answered_parts || 0);

  return {
    totalAttempts,
    correctAttempts,
    accuracy: totalAttempts ? correctAttempts / totalAttempts : 0,
    totalReveals,
    answeredParts,
    recent: (recentResult.results || []).map((row) => ({
      questionId: row.question_id,
      partId: row.part_id,
      selectedKeys: safeJsonArray(row.selected_keys),
      checked: Boolean(row.checked),
      revealed: Boolean(row.revealed),
      isCorrect: row.is_correct === null ? null : Boolean(row.is_correct),
      createdAt: row.updated_at
    }))
  };
}
