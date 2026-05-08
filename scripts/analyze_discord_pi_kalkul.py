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

PI_RE = re.compile(r"pi.?kalkul|pi calculus|pi-calculus|pikalkul", re.IGNORECASE)
REDUCTION_RE = re.compile(r"reduk|pozorovan|plus v pi|alfa reduk|prednost pred \|", re.IGNORECASE)
EXAM_RE = re.compile(r"predtermin|p[řr]edterm[ií]n|riadny|radny|opravn|skupina|zkou[sš]k|sk[uú][sš]ka", re.IGNORECASE)
RESOURCE_RE = re.compile(r"youtube|wis\.fit|slajd|predn[aá][sš]k|video|guide|doc", re.IGNORECASE)


def load_exports() -> list[tuple[str, dict]]:
    exports = []
    for year_dir in sorted(INPUT_DIR.iterdir()):
        path = year_dir / CHANNEL_FILE_NAME
        if path.exists():
            exports.append((year_dir.name, json.loads(path.read_text())))
    return exports


def one_line(text: str, limit: int = 320) -> str:
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
    yearly_reduction_counts = []
    all_hits = []
    exam_hits = []
    reduction_hits = []
    resource_hits = []
    author_counts = Counter()

    for year, export in exports:
        year_hits = []
        year_reduction_hits = []
        for message in export["messages"]:
            content = message.get("content") or ""
            if not PI_RE.search(content):
                continue

            record = {
                "year": year,
                "timestamp": message["timestamp"],
                "author": message["author"]["name"],
                "content": one_line(content),
            }
            year_hits.append(record)
            all_hits.append(record)
            author_counts[record["author"]] += 1

            if EXAM_RE.search(content):
                exam_hits.append(record)
            if REDUCTION_RE.search(content):
                reduction_hits.append(record)
                year_reduction_hits.append(record)
            if RESOURCE_RE.search(content):
                resource_hits.append(record)

        yearly_counts.append((year, len(year_hits)))
        yearly_reduction_counts.append((year, len(year_reduction_hits)))

    summary_lines = [
        "# Pi-kalkul from Discord",
        "",
        "Focused side analysis of pi-kalkul references in the Discord export.",
        "",
        "## Counts by year",
        "",
        "| Year | Pi-kalkul messages | Reduction/notation messages |",
        "| --- | ---: | ---: |",
    ]
    for (year, count), (_, reduction_count) in zip(yearly_counts, yearly_reduction_counts):
        summary_lines.append(f"| {year} | {count} | {reduction_count} |")

    summary_lines.extend(
        [
            "",
            "## Observations",
            "",
            f"- Total pi-kalkul mentions: {len(all_hits)}",
            f"- Messages specifically about reductions/notation: {len(reduction_hits)}",
            f"- Messages that look like exam reconstructions: {len(exam_hits)}",
            f"- Messages that point to learning resources: {len(resource_hits)}",
            f"- Most active authors on this topic: {', '.join(f'{name} ({count})' for name, count in author_counts.most_common(8))}",
            "",
            "## What the Discord adds",
            "",
            "- Pi-kalkul is discussed as a recurring exam topic, not a fringe one.",
            "- The highest-value Discord content is not general chat, but concrete exam reconstructions and questions about reductions, observations, `+`, and operator precedence.",
            "- Students repeatedly struggle with the same points: how reduction works, what `pozorování` means, what `+` means, and how many distinct reduction branches are needed.",
            "",
            "## Exam-like messages",
            "",
        ]
    )
    for record in exam_hits[:25]:
        summary_lines.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )

    summary_lines.extend(["", "## Reduction/notation messages", ""])
    for record in reduction_hits[:25]:
        summary_lines.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )

    summary_lines.extend(["", "## Resource messages", ""])
    for record in resource_hits[:20]:
        summary_lines.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )

    write_text(OUTPUT_DIR / "pi-kalkul.md", "\n".join(summary_lines) + "\n")

    hits_lines = ["year\ttimestamp\tauthor\tkind\tcontent"]
    for record in all_hits:
        kind = []
        if EXAM_RE.search(record["content"]):
            kind.append("exam")
        if REDUCTION_RE.search(record["content"]):
            kind.append("reduction")
        if RESOURCE_RE.search(record["content"]):
            kind.append("resource")
        if not kind:
            kind.append("general")
        hits_lines.append(
            "\t".join(
                [
                    record["year"],
                    record["timestamp"],
                    record["author"],
                    ",".join(kind),
                    record["content"].replace("\t", " "),
                ]
            )
        )
    write_text(OUTPUT_DIR / "pi-kalkul.tsv", "\n".join(hits_lines) + "\n")


if __name__ == "__main__":
    main()
