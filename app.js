const STORAGE_KEY = "stats-practice-lab-progress";

const state = {
  questions: Array.isArray(window.STAT_QUESTIONS) ? window.STAT_QUESTIONS : [],
  filtered: [],
  index: 0,
  progress: loadProgress(),
  answerVisible: false
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
  answerPanel: document.getElementById("answer-panel"),
  answerContent: document.getElementById("answer-content"),
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

function applyFilters() {
  const mode = elements.modeSelect.value;
  const search = elements.searchInput.value.trim().toLowerCase();

  let questions = [...state.questions];

  if (mode === "random") {
    questions = [...questions].sort(() => Math.random() - 0.5);
  } else if (mode === "review") {
    questions = questions.filter((question) => questionStatus(question.id) === "review");
  } else if (mode === "mastered") {
    questions = questions.filter((question) => questionStatus(question.id) === "mastered");
  }

  if (search) {
    questions = questions.filter((question) => {
      const haystack = `${question.id} ${question.title} ${question.prompt.join(" ")}`.toLowerCase();
      return haystack.includes(search);
    });
  }

  state.filtered = questions;
  if (state.index >= state.filtered.length) {
    state.index = 0;
  }
}

function renderStats() {
  const statuses = Object.values(state.progress);
  const mastered = statuses.filter((value) => value === "mastered").length;
  const review = statuses.filter((value) => value === "review").length;
  elements.totalCount.textContent = String(state.questions.length);
  elements.masteredCount.textContent = String(mastered);
  elements.reviewCount.textContent = String(review);
}

function renderQuestionList() {
  elements.questionList.innerHTML = "";

  state.filtered.forEach((question, idx) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `question-list-item${idx === state.index ? " active" : ""}`;
    button.addEventListener("click", () => {
      state.index = idx;
      state.answerVisible = false;
      render();
    });

    const badge = document.createElement("span");
    badge.textContent = `#${question.id}`;

    const text = document.createElement("div");
    const title = document.createElement("div");
    title.textContent = truncate(question.title, 68);
    const meta = document.createElement("small");
    meta.textContent = `${question.prompt.length} lines`;
    text.append(title, meta);

    const statusDot = document.createElement("span");
    statusDot.className = `question-list-status ${questionStatus(question.id)}`;

    button.append(badge, text, statusDot);
    elements.questionList.appendChild(button);
  });
}

function truncate(value, maxLength) {
  return value.length > maxLength ? `${value.slice(0, maxLength - 1)}…` : value;
}

function renderLines(container, lines) {
  container.innerHTML = "";
  lines.forEach((line) => {
    const paragraph = document.createElement("p");
    if (line.endsWith(":") && !line.startsWith("•")) {
      paragraph.className = "section-heading";
    }
    if (line.startsWith("•")) {
      paragraph.classList.add("bullet");
    }
    paragraph.textContent = line;
    container.appendChild(paragraph);
  });
}

function renderQuestion() {
  const question = currentQuestion();
  if (!question) {
    elements.currentBadge.textContent = "No questions";
    elements.currentTitle.textContent = "Nothing matches this filter yet.";
    elements.progressText.textContent = "0 / 0";
    elements.progressFill.style.width = "0%";
    elements.questionContent.innerHTML = "<p>Try switching the mode or clearing the search.</p>";
    elements.answerPanel.classList.add("hidden");
    return;
  }

  elements.currentBadge.textContent = `Question ${question.id}`;
  elements.currentTitle.textContent = question.title;
  elements.progressText.textContent = `${state.index + 1} / ${state.filtered.length}`;
  elements.progressFill.style.width = `${((state.index + 1) / state.filtered.length) * 100}%`;
  renderLines(elements.questionContent, question.prompt);

  if (state.answerVisible) {
    elements.answerPanel.classList.remove("hidden");
    renderLines(elements.answerContent, question.answer.length ? question.answer : ["No structured answer was parsed."]);
    elements.revealButton.textContent = "Hide Answer";
  } else {
    elements.answerPanel.classList.add("hidden");
    elements.revealButton.textContent = "Reveal Answer";
  }
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
    state.answerVisible = false;
    render();
  }
}

function moveBy(delta) {
  if (!state.filtered.length) return;
  state.index = (state.index + delta + state.filtered.length) % state.filtered.length;
  state.answerVisible = false;
  render();
}

elements.modeSelect.addEventListener("change", () => {
  state.index = 0;
  state.answerVisible = false;
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
  state.answerVisible = false;
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
  state.answerVisible = !state.answerVisible;
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
    state.answerVisible = !state.answerVisible;
    renderQuestion();
  }
  if (event.key.toLowerCase() === "m") setQuestionStatus("mastered");
  if (event.key.toLowerCase() === "l") setQuestionStatus("review");
});

render();

