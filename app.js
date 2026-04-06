const state = {
  questions: Array.isArray(window.STAT_QUESTIONS) ? window.STAT_QUESTIONS : [],
  filtered: [],
  index: 0,
  progress: {},
  revealAll: false,
  responses: {},
  randomOrder: [],
  auth: {
    user: null,
    loading: true,
    error: "",
    syncTone: "",
    syncText: "Checking session…"
  },
  records: emptyRecords()
};

const elements = {
  authOverlay: document.getElementById("auth-overlay"),
  loginForm: document.getElementById("login-form"),
  loginUsername: document.getElementById("login-username"),
  loginPassword: document.getElementById("login-password"),
  loginButton: document.getElementById("login-button"),
  loginError: document.getElementById("login-error"),
  totalCount: document.getElementById("total-count"),
  masteredCount: document.getElementById("mastered-count"),
  reviewCount: document.getElementById("review-count"),
  attemptCount: document.getElementById("attempt-count"),
  accuracyCount: document.getElementById("accuracy-count"),
  accountName: document.getElementById("account-name"),
  accountNote: document.getElementById("account-note"),
  logoutButton: document.getElementById("logout-button"),
  syncStatus: document.getElementById("sync-status"),
  answeredParts: document.getElementById("answered-parts"),
  recentRecords: document.getElementById("recent-records"),
  modeSelect: document.getElementById("mode-select"),
  jumpInput: document.getElementById("jump-input"),
  jumpButton: document.getElementById("jump-button"),
  searchInput: document.getElementById("search-input"),
  randomButton: document.getElementById("random-button"),
  resetProgressButton: document.getElementById("reset-progress-button"),
  questionList: document.getElementById("question-list"),
  currentBadge: document.getElementById("current-badge"),
  currentTitle: document.getElementById("current-title"),
  progressText: document.getElementById("progress-text"),
  progressFill: document.getElementById("progress-fill"),
  questionContent: document.getElementById("question-content"),
  prevButton: document.getElementById("prev-button"),
  nextButton: document.getElementById("next-button"),
  revealButton: document.getElementById("reveal-button"),
  markMasteredButton: document.getElementById("mark-mastered-button"),
  markReviewButton: document.getElementById("mark-review-button"),
  clearStatusButton: document.getElementById("clear-status-button")
};

function emptyRecords() {
  return {
    totalAttempts: 0,
    correctAttempts: 0,
    accuracy: 0,
    totalReveals: 0,
    answeredParts: 0,
    recent: []
  };
}

function cloneData(value) {
  return JSON.parse(JSON.stringify(value));
}

function normalizeKeys(keys) {
  return [...keys].sort().join("|");
}

function truncate(value, maxLength) {
  return value.length > maxLength ? `${value.slice(0, maxLength - 1)}…` : value;
}

function shuffle(array) {
  const copy = [...array];
  for (let index = copy.length - 1; index > 0; index -= 1) {
    const swapIndex = Math.floor(Math.random() * (index + 1));
    [copy[index], copy[swapIndex]] = [copy[swapIndex], copy[index]];
  }
  return copy;
}

function rebuildRandomOrder() {
  state.randomOrder = shuffle(state.questions.map((question) => question.id));
}

function setSyncStatus(text, tone = "") {
  state.auth.syncText = text;
  state.auth.syncTone = tone;
}

function clearUserState() {
  state.progress = {};
  state.responses = {};
  state.records = emptyRecords();
  state.revealAll = false;
}

function currentQuestion() {
  return state.filtered[state.index] || null;
}

function questionStatus(id) {
  return state.progress[id] || "none";
}

function findQuestion(questionId) {
  return state.questions.find((question) => question.id === questionId) || null;
}

function findPart(questionId, partId) {
  const question = findQuestion(questionId);
  return question?.parts.find((part) => part.id === partId) || null;
}

function partHasInteractiveChoice(part) {
  return part.choices.length > 0 && part.answerKeys.length > 0;
}

function isMultiSelect(part) {
  return part.answerKeys.length > 1;
}

function responseState(questionId, partId) {
  if (!state.responses[questionId]) {
    state.responses[questionId] = {};
  }
  if (!state.responses[questionId][partId]) {
    state.responses[questionId][partId] = {
      selectedKeys: [],
      checked: false,
      revealed: false
    };
  }
  return state.responses[questionId][partId];
}

function shouldShowFeedback(part, response) {
  if (state.revealAll) return true;
  if (partHasInteractiveChoice(part) && response.checked) return true;
  if (!partHasInteractiveChoice(part) && response.revealed) return true;
  return false;
}

function questionSearchText(question) {
  const partText = question.parts.flatMap((part) => [
    part.label,
    ...part.prompt,
    ...part.choices.map((choice) => choice.text),
    ...part.answerDetails,
    ...part.explanation
  ]);
  return `${question.id} ${question.title} ${question.intro.join(" ")} ${partText.join(" ")}`.toLowerCase();
}

function applyFilters() {
  const mode = elements.modeSelect.value;
  const search = elements.searchInput.value.trim().toLowerCase();

  let questions = [...state.questions];

  if (mode === "review") {
    questions = questions.filter((question) => questionStatus(question.id) === "review");
  } else if (mode === "mastered") {
    questions = questions.filter((question) => questionStatus(question.id) === "mastered");
  } else if (mode === "random") {
    const order = new Map(state.randomOrder.map((id, idx) => [id, idx]));
    questions.sort((left, right) => (order.get(left.id) ?? 0) - (order.get(right.id) ?? 0));
  }

  if (search) {
    questions = questions.filter((question) => questionSearchText(question).includes(search));
  }

  state.filtered = questions;
  if (state.index >= state.filtered.length) {
    state.index = 0;
  }
}

function formatAccuracy(value) {
  return `${Math.round((value || 0) * 100)}%`;
}

function formatTimestamp(value) {
  if (!value) return "";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return new Intl.DateTimeFormat(undefined, {
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit"
  }).format(date);
}

function describeRecord(record) {
  const question = findQuestion(record.questionId);
  const part = question?.parts.find((candidate) => candidate.id === record.partId);
  return {
    title: question ? `Q${question.id} · ${truncate(question.title, 34)}` : `Q${record.questionId}`,
    part: part ? part.label : record.partId
  };
}

function renderAuth() {
  const signedIn = Boolean(state.auth.user);
  elements.authOverlay.classList.toggle("hidden", signedIn);
  elements.loginButton.disabled = state.auth.loading;
  elements.loginUsername.disabled = state.auth.loading;
  elements.loginPassword.disabled = state.auth.loading;

  if (state.auth.error) {
    elements.loginError.hidden = false;
    elements.loginError.textContent = state.auth.error;
  } else {
    elements.loginError.hidden = true;
    elements.loginError.textContent = "";
  }

  elements.syncStatus.textContent = state.auth.syncText;
  elements.syncStatus.className = `sync-pill${state.auth.syncTone ? ` ${state.auth.syncTone}` : ""}`;

  if (signedIn) {
    elements.accountName.textContent = state.auth.user.displayName;
    elements.accountNote.textContent = "Your mastery markers and answer history are syncing automatically.";
    elements.logoutButton.disabled = false;
  } else {
    elements.accountName.textContent = "Not signed in";
    elements.accountNote.textContent = "Sign in to save question status and answer records.";
    elements.logoutButton.disabled = true;
  }
}

function renderStats() {
  const statuses = Object.values(state.progress);
  elements.totalCount.textContent = String(state.questions.length);
  elements.masteredCount.textContent = String(statuses.filter((value) => value === "mastered").length);
  elements.reviewCount.textContent = String(statuses.filter((value) => value === "review").length);
  elements.attemptCount.textContent = String(state.records.totalAttempts || 0);
  elements.accuracyCount.textContent = formatAccuracy(state.records.accuracy);
}

function renderQuestionList() {
  elements.questionList.innerHTML = "";

  state.filtered.forEach((question, idx) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `question-list-item${idx === state.index ? " active" : ""}`;
    button.addEventListener("click", () => {
      state.index = idx;
      state.revealAll = false;
      render();
    });

    const badge = document.createElement("span");
    badge.textContent = `#${question.id}`;

    const text = document.createElement("div");
    const title = document.createElement("div");
    title.textContent = truncate(question.title, 64);
    const meta = document.createElement("small");
    meta.textContent = `${question.parts.length} part${question.parts.length === 1 ? "" : "s"}`;
    text.append(title, meta);

    const statusDot = document.createElement("span");
    statusDot.className = `question-list-status ${questionStatus(question.id)}`;

    button.append(badge, text, statusDot);
    elements.questionList.appendChild(button);
  });
}

function renderLines(container, lines, extraClass = "") {
  lines.forEach((line) => {
    const paragraph = document.createElement("p");
    if (line.endsWith(":") && !line.startsWith("•")) {
      paragraph.className = "section-heading";
    }
    if (line.startsWith("•")) {
      paragraph.classList.add("bullet");
    }
    if (extraClass) {
      paragraph.classList.add(extraClass);
    }
    paragraph.textContent = line;
    container.appendChild(paragraph);
  });
}

function dedupeLines(lines) {
  const compact = [];
  for (const line of lines) {
    if (!line) {
      if (compact.length && compact[compact.length - 1] !== "") {
        compact.push("");
      }
      continue;
    }
    if (compact[compact.length - 1] === line) {
      continue;
    }
    compact.push(line);
  }
  while (compact[0] === "") compact.shift();
  while (compact[compact.length - 1] === "") compact.pop();
  return compact;
}

function renderFeedback(part, response) {
  const feedback = document.createElement("div");
  let tone = "neutral";
  let badge = "Worked answer";

  if (partHasInteractiveChoice(part)) {
    const correct = normalizeKeys(response.selectedKeys) === normalizeKeys(part.answerKeys);
    if (response.checked) {
      tone = correct ? "correct" : "incorrect";
      badge = correct ? "Correct" : "Not quite";
    } else if (state.revealAll) {
      badge = "Answer reveal";
    }
  }

  feedback.className = `feedback-panel ${tone}`;

  const badgeNode = document.createElement("div");
  badgeNode.className = `feedback-badge ${tone}`;
  badgeNode.textContent = badge;
  feedback.appendChild(badgeNode);

  const lines = [];
  if (part.answerKeys.length) {
    lines.push(
      part.answerKeys.length > 1
        ? `Correct answers: ${part.answerKeys.join(", ")}`
        : `Correct answer: ${part.answerKeys[0]}`
    );
  }
  lines.push(...part.answerDetails);
  lines.push(...part.explanation);

  const content = document.createElement("div");
  content.className = "feedback-content";
  renderLines(content, dedupeLines(lines), "feedback-line");
  feedback.appendChild(content);

  return feedback;
}

function renderChoiceButtons(question, part, response) {
  const wrapper = document.createElement("div");
  wrapper.className = "choice-grid";

  part.choices.forEach((choice) => {
    const button = document.createElement("button");
    button.type = "button";

    const selected = response.selectedKeys.includes(choice.key);
    const showFeedback = shouldShowFeedback(part, response);
    const correct = part.answerKeys.includes(choice.key);
    const wrongPick = response.checked && selected && !correct;

    button.className = "choice-button";
    if (selected) button.classList.add("selected");
    if (showFeedback && correct) button.classList.add("correct");
    if (showFeedback && wrongPick) button.classList.add("incorrect");

    if (isMultiSelect(part)) {
      button.addEventListener("click", () => toggleMultiChoice(question.id, part.id, choice.key));
    } else {
      button.addEventListener("click", () => {
        void setSingleChoice(question.id, part.id, choice.key);
      });
    }

    const key = document.createElement("span");
    key.className = "choice-key";
    key.textContent = choice.key;

    const text = document.createElement("span");
    text.className = "choice-text";
    text.textContent = choice.text;

    button.append(key, text);
    wrapper.appendChild(button);
  });

  return wrapper;
}

function renderPart(question, part) {
  const response = responseState(question.id, part.id);
  const card = document.createElement("section");
  card.className = "part-card";

  const label = document.createElement("div");
  label.className = "part-label";
  label.textContent =
    part.label === "Question" && question.parts.length === 1 ? "Main item" : part.label;
  card.appendChild(label);

  if (part.prompt.length) {
    const prompt = document.createElement("div");
    prompt.className = "part-prompt";
    renderLines(prompt, part.prompt);
    card.appendChild(prompt);
  }

  if (part.choices.length) {
    const hint = document.createElement("p");
    hint.className = "part-hint";
    hint.textContent = isMultiSelect(part)
      ? "Select all that apply, then check your selection."
      : "Choose one option to get immediate feedback.";
    card.appendChild(hint);

    card.appendChild(renderChoiceButtons(question, part, response));

    if (isMultiSelect(part)) {
      const toolbar = document.createElement("div");
      toolbar.className = "part-toolbar";

      const checkButton = document.createElement("button");
      checkButton.type = "button";
      checkButton.className = "mini-button primary";
      checkButton.textContent = "Check Selection";
      checkButton.disabled = response.selectedKeys.length === 0;
      checkButton.addEventListener("click", () => {
        void checkMultiChoice(question.id, part.id);
      });
      toolbar.appendChild(checkButton);
      card.appendChild(toolbar);
    }
  } else if (!shouldShowFeedback(part, response) && (part.answerDetails.length || part.explanation.length)) {
    const toolbar = document.createElement("div");
    toolbar.className = "part-toolbar";
    const revealButton = document.createElement("button");
    revealButton.type = "button";
    revealButton.className = "mini-button";
    revealButton.textContent = "Show Worked Answer";
    revealButton.addEventListener("click", () => {
      void revealWorkedAnswer(question.id, part.id);
    });
    toolbar.appendChild(revealButton);
    card.appendChild(toolbar);
  }

  if (shouldShowFeedback(part, response)) {
    card.appendChild(renderFeedback(part, response));
  }

  return card;
}

function renderQuestion() {
  const question = currentQuestion();
  if (!question) {
    elements.currentBadge.textContent = "No questions";
    elements.currentTitle.textContent = "Nothing matches this filter yet.";
    elements.progressText.textContent = "0 / 0";
    elements.progressFill.style.width = "0%";
    elements.questionContent.innerHTML = "<p>Try switching the mode or clearing the search.</p>";
    return;
  }

  elements.currentBadge.textContent = `Question ${question.id}`;
  elements.currentTitle.textContent = question.title;
  elements.progressText.textContent = `${state.index + 1} / ${state.filtered.length}`;
  elements.progressFill.style.width = `${((state.index + 1) / state.filtered.length) * 100}%`;
  elements.revealButton.textContent = state.revealAll ? "Hide All Explanations" : "Reveal All Explanations";

  elements.questionContent.innerHTML = "";

  const intro = document.createElement("div");
  intro.className = "question-intro";
  renderLines(intro, question.intro);
  elements.questionContent.appendChild(intro);

  const parts = document.createElement("div");
  parts.className = "part-stack";
  question.parts.forEach((part) => parts.appendChild(renderPart(question, part)));
  elements.questionContent.appendChild(parts);
}

function renderRecords() {
  elements.answeredParts.textContent = `${state.records.answeredParts || 0} answered`;
  elements.recentRecords.innerHTML = "";

  if (!state.auth.user) {
    const empty = document.createElement("p");
    empty.className = "empty-records";
    empty.textContent = "Sign in to load your activity history.";
    elements.recentRecords.appendChild(empty);
    return;
  }

  if (!state.records.recent.length) {
    const empty = document.createElement("p");
    empty.className = "empty-records";
    empty.textContent = "No saved answer history yet. Your checked answers and reveals will show up here.";
    elements.recentRecords.appendChild(empty);
    return;
  }

  state.records.recent.forEach((record) => {
    const item = document.createElement("article");
    item.className = "record-item";

    const description = describeRecord(record);
    const top = document.createElement("div");
    top.className = "record-topline";

    const title = document.createElement("strong");
    title.textContent = description.title;

    const badge = document.createElement("span");
    let badgeLabel = "Viewed";
    let badgeTone = "revealed";
    if (record.checked) {
      badgeLabel = record.isCorrect ? "Correct" : "Incorrect";
      badgeTone = record.isCorrect ? "correct" : "incorrect";
    }
    badge.className = `record-badge ${badgeTone}`;
    badge.textContent = badgeLabel;

    top.append(title, badge);

    const meta = document.createElement("p");
    meta.className = "record-meta";
    meta.textContent = `${description.part} · ${record.selectedKeys?.length ? `Answer ${record.selectedKeys.join(", ")}` : "Worked answer reveal"}`;

    const time = document.createElement("p");
    time.className = "record-timestamp";
    time.textContent = formatTimestamp(record.createdAt);

    item.append(top, meta, time);
    elements.recentRecords.appendChild(item);
  });
}

function render() {
  applyFilters();
  renderAuth();
  renderStats();
  renderQuestionList();
  renderRecords();
  renderQuestion();
}

function applySnapshot(payload) {
  state.auth.user = payload.user || null;
  state.progress = payload.progress || {};
  state.responses = payload.responses || {};
  state.records = payload.records || emptyRecords();
}

async function apiFetch(path, options = {}) {
  const config = {
    method: options.method || "GET",
    headers: {
      Accept: "application/json"
    },
    credentials: "same-origin"
  };

  if (options.body !== undefined) {
    config.headers["Content-Type"] = "application/json";
    config.body = JSON.stringify(options.body);
  }

  const response = await fetch(path, config);
  let data = {};
  try {
    data = await response.json();
  } catch {
    data = {};
  }

  if (response.status === 401 && options.authenticated !== false) {
    state.auth.user = null;
    clearUserState();
    setSyncStatus("Session expired. Sign in again.", "error");
    render();
    throw new Error("Please sign in again.");
  }

  if (!response.ok) {
    throw new Error(data.error || "Request failed.");
  }

  return data;
}

async function loadSession() {
  state.auth.loading = true;
  state.auth.error = "";
  setSyncStatus("Checking session…");
  render();

  try {
    const response = await fetch("/api/state", {
      method: "GET",
      headers: { Accept: "application/json" },
      credentials: "same-origin"
    });

    if (response.status === 401) {
      state.auth.user = null;
      clearUserState();
      setSyncStatus("Sign in to sync progress.");
      return;
    }

    const data = await response.json();
    applySnapshot(data);
    setSyncStatus("Progress synced", "success");
  } catch {
    state.auth.user = null;
    clearUserState();
    setSyncStatus("Could not reach sync service.", "error");
  } finally {
    state.auth.loading = false;
    render();
  }
}

async function handleLogin(event) {
  event.preventDefault();
  state.auth.loading = true;
  state.auth.error = "";
  setSyncStatus("Signing in…");
  renderAuth();

  try {
    const data = await apiFetch("/api/login", {
      method: "POST",
      authenticated: false,
      body: {
        username: elements.loginUsername.value.trim(),
        password: elements.loginPassword.value
      }
    });

    elements.loginForm.reset();
    applySnapshot(data);
    setSyncStatus("Signed in and synced", "success");
  } catch (error) {
    state.auth.error = error.message;
    setSyncStatus("Sign-in failed", "error");
  } finally {
    state.auth.loading = false;
    render();
  }
}

async function handleLogout() {
  state.auth.loading = true;
  setSyncStatus("Signing out…");
  renderAuth();

  try {
    await apiFetch("/api/logout", { method: "POST" });
  } catch {
    // If logout fails remotely, we still clear the UI to avoid a stuck session.
  } finally {
    state.auth.loading = false;
    state.auth.user = null;
    state.auth.error = "";
    clearUserState();
    setSyncStatus("Signed out");
    render();
  }
}

function jumpToQuestion() {
  const targetId = Number(elements.jumpInput.value);
  if (!targetId) return;
  const targetIndex = state.filtered.findIndex((question) => question.id === targetId);
  if (targetIndex >= 0) {
    state.index = targetIndex;
    state.revealAll = false;
    render();
  }
}

function moveBy(delta) {
  if (!state.filtered.length) return;
  state.index = (state.index + delta + state.filtered.length) % state.filtered.length;
  state.revealAll = false;
  render();
}

async function syncQuestionStatus(questionId, status) {
  const previous = cloneData(state.progress);

  if (status === "none") {
    delete state.progress[questionId];
  } else {
    state.progress[questionId] = status;
  }

  setSyncStatus("Saving status…");
  render();

  try {
    await apiFetch("/api/question-status", {
      method: "POST",
      body: { questionId, status }
    });
    setSyncStatus("Status saved", "success");
    render();
  } catch (error) {
    state.progress = previous;
    setSyncStatus(error.message, "error");
    render();
  }
}

function setQuestionStatus(status) {
  const question = currentQuestion();
  if (!question || !state.auth.user) return;
  void syncQuestionStatus(question.id, status);
}

async function persistPartState(questionId, partId, previousState) {
  const part = findPart(questionId, partId);
  const response = responseState(questionId, partId);
  const payload = {
    questionId,
    partId,
    selectedKeys: response.selectedKeys,
    checked: Boolean(response.checked),
    revealed: Boolean(response.revealed),
    isCorrect:
      part && partHasInteractiveChoice(part) && response.checked
        ? normalizeKeys(response.selectedKeys) === normalizeKeys(part.answerKeys)
        : null
  };

  setSyncStatus("Saving answer…");
  renderQuestion();

  try {
    const data = await apiFetch("/api/part-state", {
      method: "POST",
      body: payload
    });

    if (data.records) {
      state.records = data.records;
    }
    setSyncStatus("Answer saved", "success");
    render();
  } catch (error) {
    state.responses[questionId][partId] = previousState;
    setSyncStatus(error.message, "error");
    render();
  }
}

async function setSingleChoice(questionId, partId, key) {
  if (!state.auth.user) return;
  const previous = cloneData(responseState(questionId, partId));
  const response = responseState(questionId, partId);
  response.selectedKeys = [key];
  response.checked = true;
  response.revealed = false;
  renderQuestion();
  await persistPartState(questionId, partId, previous);
}

function toggleMultiChoice(questionId, partId, key) {
  const response = responseState(questionId, partId);
  const next = new Set(response.selectedKeys);
  if (next.has(key)) {
    next.delete(key);
  } else {
    next.add(key);
  }
  response.selectedKeys = [...next].sort();
  response.checked = false;
  renderQuestion();
}

async function checkMultiChoice(questionId, partId) {
  if (!state.auth.user) return;
  const previous = cloneData(responseState(questionId, partId));
  const response = responseState(questionId, partId);
  response.checked = true;
  response.revealed = false;
  renderQuestion();
  await persistPartState(questionId, partId, previous);
}

async function revealWorkedAnswer(questionId, partId) {
  if (!state.auth.user) return;
  const previous = cloneData(responseState(questionId, partId));
  const response = responseState(questionId, partId);
  response.revealed = true;
  renderQuestion();
  await persistPartState(questionId, partId, previous);
}

async function resetProgress() {
  if (!state.auth.user) return;
  const confirmed = window.confirm("Reset all mastered and review markers for this user?");
  if (!confirmed) return;

  const previous = cloneData(state.progress);
  state.progress = {};
  setSyncStatus("Resetting progress…");
  render();

  try {
    await apiFetch("/api/reset-progress", { method: "POST" });
    setSyncStatus("Progress reset", "success");
    render();
  } catch (error) {
    state.progress = previous;
    setSyncStatus(error.message, "error");
    render();
  }
}

elements.loginForm.addEventListener("submit", handleLogin);
elements.logoutButton.addEventListener("click", () => {
  void handleLogout();
});

elements.modeSelect.addEventListener("change", () => {
  if (elements.modeSelect.value === "random") {
    rebuildRandomOrder();
  }
  state.index = 0;
  state.revealAll = false;
  render();
});

elements.searchInput.addEventListener("input", () => {
  state.index = 0;
  render();
});

elements.jumpButton.addEventListener("click", jumpToQuestion);
elements.jumpInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") jumpToQuestion();
});

elements.randomButton.addEventListener("click", () => {
  if (!state.filtered.length) return;
  state.index = Math.floor(Math.random() * state.filtered.length);
  state.revealAll = false;
  render();
});

elements.resetProgressButton.addEventListener("click", () => {
  void resetProgress();
});

elements.prevButton.addEventListener("click", () => moveBy(-1));
elements.nextButton.addEventListener("click", () => moveBy(1));
elements.revealButton.addEventListener("click", () => {
  state.revealAll = !state.revealAll;
  renderQuestion();
});

elements.markMasteredButton.addEventListener("click", () => setQuestionStatus("mastered"));
elements.markReviewButton.addEventListener("click", () => setQuestionStatus("review"));
elements.clearStatusButton.addEventListener("click", () => setQuestionStatus("none"));

document.addEventListener("keydown", (event) => {
  const tag = document.activeElement?.tagName?.toLowerCase();
  if (tag === "input" || tag === "select" || tag === "textarea") return;
  if (!state.auth.user) return;

  if (event.key === "ArrowLeft") moveBy(-1);
  if (event.key === "ArrowRight") moveBy(1);
  if (event.key.toLowerCase() === "r") {
    state.revealAll = !state.revealAll;
    renderQuestion();
  }
  if (event.key.toLowerCase() === "m") setQuestionStatus("mastered");
  if (event.key.toLowerCase() === "l") setQuestionStatus("review");
});

rebuildRandomOrder();
render();
void loadSession();
