from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "questions_compiled.md"
OUTPUT = ROOT / "questions.js"

SECTION_RE = re.compile(r"^##\s+(\d+)\.\s+(.*)$", re.M)

PROMPT_HEADINGS = (
    "Choices",
    "Part",
    "Data",
    "Technology Output",
    "Stem-and-Leaf Display",
    "Observed Table",
    "Data Table",
    "Regression Results",
    "From the Printout",
    "Given",
    "Totals",
    "About the two populations",
    "About the two samples",
    "Probabilities from the Histogram",
)

ANSWER_HEADINGS = (
    "Correct Answer",
    "Correct Answers",
    "Correct Fill-ins",
    "Interpretation Choice",
    "Correct Interpretation",
    "Fill-in Conclusion",
    "Hypotheses",
    "Expected Weekly Price",
    "Yearly Budget",
    "Re-created Data Set",
    "Conclusion",
    "Expected Cell Counts",
    "Chi-Squared Indicator",
    "Cramer's V Coefficient",
    "Test Statistic",
    "p-value",
    "Note",
)

SKIP_HEADINGS = ("Question Type", "Explanation")


def clean_line(value: str) -> str:
    value = value.replace("**", "").replace("`", "")
    value = re.sub(r"\s+", " ", value).strip()
    if value.startswith("- "):
        value = f"• {value[2:].strip()}"
    return value


def parse_sections(text: str) -> dict[int, tuple[str, str]]:
    matches = list(SECTION_RE.finditer(text))
    sections: dict[int, tuple[str, str]] = {}
    for index, match in enumerate(matches):
        qid = int(match.group(1))
        title = match.group(2).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[qid] = (title, text[start:end].strip())
    return sections


def extract_lines(body: str, mode: str) -> list[str]:
    lines: list[str] = []
    capture_answer_block = False
    skip_prompt_block = False

    for raw in body.splitlines():
        stripped = raw.strip()
        if not stripped:
            if (mode == "answer" and capture_answer_block) or (mode == "prompt" and not skip_prompt_block):
                if lines and lines[-1] != "":
                    lines.append("")
            continue
        heading_match = re.match(r"^\*\*(.*?)\*\*(.*)$", stripped)
        if heading_match:
            heading = heading_match.group(1).strip()
            tail = heading_match.group(2).strip()
            normalized = heading.rstrip(":").strip()

            if normalized.startswith(SKIP_HEADINGS):
                capture_answer_block = False
                skip_prompt_block = False
                continue

            if mode == "prompt":
                if normalized.startswith(ANSWER_HEADINGS):
                    skip_prompt_block = True
                    capture_answer_block = False
                    continue
                if normalized.startswith(PROMPT_HEADINGS):
                    skip_prompt_block = False
                    text_line = clean_line(heading + (" " + tail if tail else ""))
                    if lines and lines[-1] != "":
                        lines.append("")
                    lines.append(text_line)
                    continue
                skip_prompt_block = False
                capture_answer_block = False
                continue

            if mode == "answer":
                if normalized.startswith(ANSWER_HEADINGS):
                    capture_answer_block = True
                    text_line = clean_line(heading + (" " + tail if tail else ""))
                    if lines and lines[-1] != "":
                        lines.append("")
                    lines.append(text_line)
                    continue
                capture_answer_block = False
                continue

        if mode == "prompt":
            if skip_prompt_block:
                continue
            text_line = clean_line(stripped)
            if text_line:
                lines.append(text_line)
        elif mode == "answer" and capture_answer_block:
            text_line = clean_line(stripped)
            if text_line:
                lines.append(text_line)

    while lines and lines[0] == "":
        lines.pop(0)
    while lines and lines[-1] == "":
        lines.pop()

    compact: list[str] = []
    for line in lines:
        if line == "" and compact and compact[-1] == "":
            continue
        compact.append(line)
    return compact


def build_questions() -> list[dict[str, object]]:
    text = SOURCE.read_text(encoding="utf-8")
    sections = parse_sections(text)
    questions = []
    for qid in sorted(sections):
        title, body = sections[qid]
        questions.append(
            {
                "id": qid,
                "title": title.replace("`", ""),
                "prompt": extract_lines(body, "prompt")
                or ["Work from the title first, then reveal the answer when you are ready."],
                "answer": extract_lines(body, "answer")
                or ["Answer details were not structured in the source notes for this item."],
            }
        )
    return questions


def main() -> None:
    questions = build_questions()
    payload = "window.STAT_QUESTIONS = " + json.dumps(questions, ensure_ascii=False, indent=2) + ";\n"
    OUTPUT.write_text(payload, encoding="utf-8")
    print(f"Built {len(questions)} questions -> {OUTPUT}")


if __name__ == "__main__":
    main()
