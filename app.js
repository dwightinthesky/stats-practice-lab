const STORAGE_KEY = "stats-practice-lab-progress";

const state = {
  questions: Array.isArray(window.STAT_QUESTIONS) ? window.STAT_QUESTIONS : [],
  filtered: [],
  index: 0,
  progress: loadProgress(),
  revealAll: false,
  responses: {},
  randomOrder: []
};

const elements = {
  totalCount: document.getElementById("total-count"),
  masteredCount: document.getElementById("mastered-count"),
  reviewCount: document.getElementById("review-count"),
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

function loadProgress() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
  } catch {
    return {};
  }
}

function saveProgress() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.progress));
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

function questionStatus(id) {
  return state.progress[id] || "none";
}

function setQuestionStatus(status) {
  const question = currentQuestion();
  if (!question) return;
  if (status === "none") {
    delete state.progress[question.id];
  } else {
    state.progress[question.id] = status;
  }
  saveProgress();
  render();
}

function currentQuestion() {
  return state.filtered[state.index] || null;
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

function renderStats() {
  const statuses = Object.values(state.progress);
  elements.totalCount.textContent = String(state.questions.length);
  elements.masteredCount.textContent = String(statuses.filter((value) => value === "mastered").length);
  elements.reviewCount.textContent = String(statuses.filter((value) => value === "review").length);
}

function truncate(value, maxLength) {
  return value.length > maxLength ? `${value.slice(0, maxLength - 1)}…` : value;
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

function setSingleChoice(questionId, partId, key) {
  const response = responseState(questionId, partId);
  response.selectedKeys = [key];
  response.checked = true;
  renderQuestion();
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
  renderQuestion();
}

function checkMultiChoice(questionId, partId) {
  const response = responseState(questionId, partId);
  response.checked = true;
  renderQuestion();
}

function revealWorkedAnswer(questionId, partId) {
  const response = responseState(questionId, partId);
  response.revealed = true;
  renderQuestion();
}

function normalizeKeys(keys) {
  return [...keys].sort().join("|");
}

function partHasInteractiveChoice(part) {
  return part.choices.length > 0 && part.answerKeys.length > 0;
}

function isMultiSelect(part) {
  return part.answerKeys.length > 1;
}

function shouldShowFeedback(part, response) {
  if (state.revealAll) return true;
  if (partHasInteractiveChoice(part) && response.checked) return true;
  if (!partHasInteractiveChoice(part) && response.revealed) return true;
  return false;
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
      button.addEventListener("click", () => setSingleChoice(question.id, part.id, choice.key));
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
    if (isMultiSelect(part)) {
      const hint = document.createElement("p");
      hint.className = "part-hint";
      hint.textContent = "Select all that apply, then check your selection.";
      card.appendChild(hint);
    } else {
      const hint = document.createElement("p");
      hint.className = "part-hint";
      hint.textContent = "Choose one option to get immediate feedback.";
      card.appendChild(hint);
    }

    card.appendChild(renderChoiceButtons(question, part, response));

    if (isMultiSelect(part)) {
      const toolbar = document.createElement("div");
      toolbar.className = "part-toolbar";

      const checkButton = document.createElement("button");
      checkButton.type = "button";
      checkButton.className = "mini-button primary";
      checkButton.textContent = "Check Selection";
      checkButton.disabled = response.selectedKeys.length === 0;
      checkButton.addEventListener("click", () => checkMultiChoice(question.id, part.id));
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
    revealButton.addEventListener("click", () => revealWorkedAnswer(question.id, part.id));
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

function render() {
  applyFilters();
  renderStats();
  renderQuestionList();
  renderQuestion();
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
  const confirmed = window.confirm("Reset all mastered / review markers?");
  if (!confirmed) return;
  state.progress = {};
  saveProgress();
  render();
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
