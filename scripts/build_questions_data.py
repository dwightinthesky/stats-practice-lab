from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "questions_compiled.md"
OUTPUT = ROOT / "questions.js"

SECTION_RE = re.compile(r"^##\s+(\d+)\.\s+(.*)$", re.M)
HEADING_RE = re.compile(r"^\*\*(.*?)\*\*(.*)$")
OPTION_RE = re.compile(r"^(?:•\s*)?([A-Z])\.\s+(.*)$")

PROMPT_SECTION_HEADINGS = (
    "Choices",
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
    "Model Form",
)

ANSWER_SECTION_HEADINGS = (
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
    "Fit Interpretation",
    "Correct Graph",
    "Observed Counts",
    "Expected Counts",
    "Note",
)

IGNORE_HEADINGS = ("Question Type",)


def clean_text(value: str) -> str:
    value = value.replace("**", "").replace("`", "")
    value = re.sub(r"\s+", " ", value).strip()
    if value.startswith("- "):
        value = f"• {value[2:].strip()}"
    return value


def append_line(target: list[str], value: str) -> None:
    value = clean_text(value)
    if not value:
        if target and target[-1] != "":
            target.append("")
        return
    target.append(value)


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


def parse_option_keys(text: str) -> list[str]:
    normalized = text.replace("`", "").strip()
    if re.fullmatch(r"[A-Z](?:\s*,\s*[A-Z])*", normalized):
        return [item.strip() for item in normalized.split(",")]
    return []


def make_part(index: int, label: str = "Question") -> dict[str, object]:
    return {
        "id": f"part-{index}",
        "label": label,
        "prompt": [],
        "choices": [],
        "answerKeys": [],
        "answerDetails": [],
        "explanation": [],
    }


def compact_lines(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    for line in lines:
        if line == "" and (not cleaned or cleaned[-1] == ""):
            continue
        cleaned.append(line)
    while cleaned and cleaned[0] == "":
        cleaned.pop(0)
    while cleaned and cleaned[-1] == "":
        cleaned.pop()
    return cleaned


def parse_question(body: str) -> tuple[list[str], list[dict[str, object]]]:
    intro: list[str] = []
    parts: list[dict[str, object]] = []
    current_part: dict[str, object] | None = None
    mode = "intro"

    def ensure_part(label: str = "Question") -> dict[str, object]:
        nonlocal current_part
        if current_part is None:
            current_part = make_part(len(parts) + 1, label)
            parts.append(current_part)
        return current_part

    for raw_line in body.splitlines():
        stripped = raw_line.strip()

        if not stripped:
            if mode == "intro":
                append_line(intro, "")
            elif current_part is not None:
                target = (
                    current_part["choices"]
                    if mode == "choices"
                    else current_part["explanation"]
                    if mode == "explanation"
                    else current_part["answerDetails"]
                    if mode == "answer"
                    else current_part["prompt"]
                )
                append_line(target, "")
            continue

        heading_match = HEADING_RE.match(stripped)
        if heading_match:
            heading = heading_match.group(1).strip()
            tail = heading_match.group(2).strip()
            normalized = heading.rstrip(":").strip()

            if normalized.startswith(IGNORE_HEADINGS):
                mode = "intro"
                continue

            if normalized.startswith("Part"):
                current_part = make_part(len(parts) + 1, clean_text(normalized))
                parts.append(current_part)
                mode = "prompt"
                if tail:
                    append_line(current_part["prompt"], tail)
                continue

            if normalized == "Explanation":
                part = ensure_part()
                mode = "explanation"
                if tail:
                    append_line(part["explanation"], tail)
                continue

            if normalized == "Choices":
                ensure_part()
                mode = "choices"
                continue

            if normalized.startswith(ANSWER_SECTION_HEADINGS):
                part = ensure_part()
                mode = "answer"
                cleaned_tail = clean_text(tail) if tail else ""
                answer_keys = parse_option_keys(cleaned_tail) if cleaned_tail else []

                if answer_keys:
                    part["answerKeys"] = answer_keys
                    answer_line = (
                        f"Correct answers: {', '.join(answer_keys)}"
                        if len(answer_keys) > 1
                        else f"Correct answer: {answer_keys[0]}"
                    )
                    append_line(part["answerDetails"], answer_line)
                else:
                    heading_line = clean_text(f"{normalized}: {cleaned_tail}" if cleaned_tail else normalized)
                    append_line(part["answerDetails"], heading_line)
                continue

            if normalized.startswith(PROMPT_SECTION_HEADINGS):
                target = ensure_part()["prompt"] if current_part is not None else intro
                mode = "prompt"
                heading_line = clean_text(f"{normalized}: {tail}" if tail else normalized)
                append_line(target, heading_line)
                continue

            target = ensure_part()["prompt"] if current_part is not None else intro
            mode = "prompt"
            heading_line = clean_text(f"{normalized}: {tail}" if tail else normalized)
            append_line(target, heading_line)
            continue

        if mode == "choices":
            part = ensure_part()
            cleaned = clean_text(stripped)
            option_match = OPTION_RE.match(cleaned)
            if option_match:
                part["choices"].append(
                    {
                        "key": option_match.group(1),
                        "text": option_match.group(2).strip(),
                    }
                )
            else:
                append_line(part["prompt"], cleaned)
            continue

        cleaned = clean_text(stripped)
        option_match = OPTION_RE.match(cleaned)
        if option_match and mode not in {"answer", "explanation"}:
            part = ensure_part()
            part["choices"].append(
                {
                    "key": option_match.group(1),
                    "text": option_match.group(2).strip(),
                }
            )
            mode = "choices"
            continue

        if mode == "answer":
            append_line(ensure_part()["answerDetails"], stripped)
            continue

        if mode == "explanation":
            append_line(ensure_part()["explanation"], stripped)
            continue

        if current_part is None:
            append_line(intro, stripped)
        else:
            append_line(current_part["prompt"], stripped)

    intro = compact_lines(intro)
    finalized_parts: list[dict[str, object]] = []

    if not parts:
        parts = [make_part(1)]

    for part in parts:
        part["prompt"] = compact_lines(part["prompt"])
        part["answerDetails"] = compact_lines(part["answerDetails"])
        part["explanation"] = compact_lines(part["explanation"])
        finalized_parts.append(part)

    if not intro:
        intro = ["Solve the item below, then check the explanation."]

    return intro, finalized_parts


def build_questions() -> list[dict[str, object]]:
    text = SOURCE.read_text(encoding="utf-8")
    sections = parse_sections(text)
    questions = []

    for qid in sorted(sections):
        title, body = sections[qid]
        intro, parts = parse_question(body)
        questions.append(
            {
                "id": qid,
                "title": title.replace("`", ""),
                "intro": intro,
                "parts": parts,
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
