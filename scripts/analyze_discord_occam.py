#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INPUT_DIR = ROOT / "raw" / "discord"
OUTPUT_DIR = ROOT / "raw" / "discord-analysis"
CHANNEL_FILE_NAME = "621775635722928128.json"

TOPIC_RE = re.compile(
    r"\boccam\b|\bocam\b|\bavg\b|\bchnh\b|\bchnl\b|out_left|out_right|\balt\b|\bseq\b|\bpar\b|\bskip\b|\bstop\b",
    re.IGNORECASE,
)
EXAM_RE = re.compile(r"predtermin|p[řr]edterm[ií]n|riadny|radny|opravn|skupina|zkou[sš]k|sk[uú][sš]ka", re.IGNORECASE)
RESOURCE_RE = re.compile(r"pdf|wiki|dokumentov|guide|zaznam|video|syntax", re.IGNORECASE)
SCORING_RE = re.compile(
    r"free body|free|worth|sta[cč][ií]|bod[ií]k|bodov|fullku|fullka|hrotit nebude|princip|kostr|syntaxi .*resit nebude|uzna|dal jej|polku z toho",
    re.IGNORECASE,
)
SYNTAX_RE = re.compile(r"\balt\b|\bseq\b|\bpar\b|\?|\!|skip|stop|proc|while", re.IGNORECASE)


def load_exports() -> list[tuple[str, dict]]:
    exports = []
    for year_dir in sorted(INPUT_DIR.iterdir()):
        path = year_dir / CHANNEL_FILE_NAME
        if path.exists():
            exports.append((year_dir.name, json.loads(path.read_text())))
    return exports


def one_line(text: str, limit: int = 360) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def main() -> None:
    exports = load_exports()
    yearly_counts = []
    all_hits = []
    exam_hits = []
    scoring_hits = []
    syntax_hits = []
    resource_hits = []
    author_counts = Counter()

    for year, export in exports:
        year_total = 0
        for message in export["messages"]:
            content = message.get("content") or ""
            if not TOPIC_RE.search(content):
                continue

            record = {
                "year": year,
                "timestamp": message["timestamp"],
                "author": message["author"]["name"],
                "content": one_line(content),
            }
            all_hits.append(record)
            year_total += 1
            author_counts[record["author"]] += 1

            if EXAM_RE.search(content):
                exam_hits.append(record)
            if SCORING_RE.search(content):
                scoring_hits.append(record)
            if SYNTAX_RE.search(content):
                syntax_hits.append(record)
            if RESOURCE_RE.search(content):
                resource_hits.append(record)

        yearly_counts.append((year, year_total))

    summary = [
        "# OCCAM from Discord",
        "",
        "Focused side analysis of OCCAM references in the Discord export.",
        "",
        "## Counts by year",
        "",
        "| Year | Topic messages |",
        "| --- | ---: |",
    ]
    for year, count in yearly_counts:
        summary.append(f"| {year} | {count} |")

    summary.extend(
        [
            "",
            "## Observations",
            "",
            f"- Total OCCAM-related messages: {len(all_hits)}",
            f"- Messages that look like exam reconstructions: {len(exam_hits)}",
            f"- Messages that talk about scoring / how hard to grade: {len(scoring_hits)}",
            f"- Messages that focus on syntax / minimal constructs: {len(syntax_hits)}",
            f"- Messages that point to resources: {len(resource_hits)}",
            f"- Most active authors on this topic: {', '.join(f'{name} ({count})' for name, count in author_counts.most_common(8))}",
            "",
            "## What Discord suggests",
            "",
            "- OCCAM is usually treated as a code-pattern question: channels, persistent internal state, and a small set of control constructs.",
            "- Several messages suggest students expect partial credit from showing the right skeleton and principle, even with imperfect syntax.",
            "- Repeated minimal syntax set in chat: `SEQ`, `PAR`, `ALT`, `?`, `!`, plus state variables and an infinite loop.",
            "- Typical recurring tasks match the knowledge base: queue/buffer, active output selection, alternating outputs, and average/threshold routing.",
            "",
            "## Scoring / grading signals",
            "",
        ]
    )
    for record in scoring_hits[:25]:
        summary.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )

    summary.extend(["", "## Exam-like messages", ""])
    for record in exam_hits[:25]:
        summary.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )

    summary.extend(["", "## Syntax / control hints", ""])
    for record in syntax_hits[:25]:
        summary.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )

    summary.extend(["", "## Resource hints", ""])
    for record in resource_hits[:20]:
        summary.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )

    write_text(OUTPUT_DIR / "occam.md", "\n".join(summary) + "\n")

    tsv = ["year\ttimestamp\tauthor\tkind\tcontent"]
    for record in all_hits:
        kinds = []
        content = record["content"]
        if EXAM_RE.search(content):
            kinds.append("exam")
        if SCORING_RE.search(content):
            kinds.append("scoring")
        if SYNTAX_RE.search(content):
            kinds.append("syntax")
        if RESOURCE_RE.search(content):
            kinds.append("resource")
        if not kinds:
            kinds.append("general")
        tsv.append(
            "\t".join(
                [
                    record["year"],
                    record["timestamp"],
                    record["author"],
                    ",".join(kinds),
                    content.replace("\t", " "),
                ]
            )
        )
    write_text(OUTPUT_DIR / "occam.tsv", "\n".join(tsv) + "\n")


if __name__ == "__main__":
    main()
