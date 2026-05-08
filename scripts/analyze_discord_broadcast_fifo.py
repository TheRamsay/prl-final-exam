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
    r"\bbroadcast\b|\bfifo\b|kauzal|causal|abcast|atomicit|atomic broadcast|koruna|happened-before|relac[ei] kauzality",
    re.IGNORECASE,
)
EXAM_RE = re.compile(r"predtermin|p[řr]edterm[ií]n|riadny|radny|opravn|skupina|zkou[sš]k|sk[uú][sš]ka", re.IGNORECASE)
ALGO_RE = re.compile(r"send|recv|algoritmus|vys[ií]l|prij[ií]m|doru[cč]|buffer|tabu[lľ]k|diagram", re.IGNORECASE)
PAIN_RE = re.compile(
    r"nechap|nech[aá]pu|wtf|v zivote som to nevidel|nesrozumiteln|co chcel autor|jak.*atomic|3 podm[ií]nky|sipecky|tabu[lľ]ka|rip",
    re.IGNORECASE,
)
PROPERTY_RE = re.compile(r"fifo|kauzal|atomicit|abcast|3 podm[ií]nky|vlastnost", re.IGNORECASE)


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
    exam_hits = []
    algo_hits = []
    pain_hits = []
    property_hits = []
    all_hits = []
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
            if ALGO_RE.search(content):
                algo_hits.append(record)
            if PAIN_RE.search(content):
                pain_hits.append(record)
            if PROPERTY_RE.search(content):
                property_hits.append(record)

        yearly_counts.append((year, year_total))

    summary_lines = [
        "# Broadcast/FIFO/kauzalita from Discord",
        "",
        "Focused side analysis of broadcast/FIFO/kauzalita references in the Discord export.",
        "",
        "## Counts by year",
        "",
        "| Year | Topic messages |",
        "| --- | ---: |",
    ]
    for year, count in yearly_counts:
        summary_lines.append(f"| {year} | {count} |")

    summary_lines.extend(
        [
            "",
            "## Observations",
            "",
            f"- Total topic mentions: {len(all_hits)}",
            f"- Messages that look like exam reconstructions: {len(exam_hits)}",
            f"- Messages that talk about send/recv/algorithms/diagrams: {len(algo_hits)}",
            f"- Messages that look like confusion or pain points: {len(pain_hits)}",
            f"- Messages explicitly talking about properties (`FIFO`, `kauzalita`, `atomicita`): {len(property_hits)}",
            f"- Most active authors on this topic: {', '.join(f'{name} ({count})' for name, count in author_counts.most_common(8))}",
            "",
            "## What Discord focuses on",
            "",
            "- Exact exam forms: either `send/recv` algorithm, or a diagram/table where you classify FIFO/kauzalita/atomicita.",
            "- Repeated confusion about the distinction between FIFO, causality, and atomicity.",
            "- Repeated complaints about `random tabulka`, `šipečky`, and unclear broadcast diagrams.",
            "- Some confusion in chat mixes MPI broadcast with the distributed-systems broadcast topic, so raw Discord needs filtering.",
            "",
            "## Exam-like messages",
            "",
        ]
    )
    for record in exam_hits[:30]:
        summary_lines.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )

    summary_lines.extend(["", "## Algorithm/diagram messages", ""])
    for record in algo_hits[:30]:
        summary_lines.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )

    summary_lines.extend(["", "## Pain points", ""])
    for record in pain_hits[:25]:
        summary_lines.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )

    write_text(OUTPUT_DIR / "broadcast-fifo-kauzalita.md", "\n".join(summary_lines) + "\n")

    hits_lines = ["year\ttimestamp\tauthor\tkind\tcontent"]
    for record in all_hits:
        kind = []
        content = record["content"]
        if EXAM_RE.search(content):
            kind.append("exam")
        if ALGO_RE.search(content):
            kind.append("algo")
        if PROPERTY_RE.search(content):
            kind.append("property")
        if PAIN_RE.search(content):
            kind.append("pain")
        if not kind:
            kind.append("general")
        hits_lines.append(
            "\t".join(
                [
                    record["year"],
                    record["timestamp"],
                    record["author"],
                    ",".join(kind),
                    content.replace("\t", " "),
                ]
            )
        )
    write_text(OUTPUT_DIR / "broadcast-fifo-kauzalita.tsv", "\n".join(hits_lines) + "\n")


if __name__ == "__main__":
    main()
