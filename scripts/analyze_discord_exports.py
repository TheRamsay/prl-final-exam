#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INPUT_DIR = ROOT / "raw" / "discord"
OUTPUT_DIR = ROOT / "raw" / "discord-analysis"
CHANNEL_FILE_NAME = "621775635722928128.json"

TOPIC_PATTERNS = {
    "MPI": r"\bmpi\b|reduce|bcast|broadcast|priemer|average|maximum|minimum|druh[yý] nejmen",
    "PRAM": r"\bpram\b|tipsport|crcw|erew|crew|casov[áa] slozitost|cena\b",
    "Broadcast/FIFO/kauzalita": r"fifo|kauzal|abcast|koruna|atomic broadcast|happened-before",
    "Euler/suffix": r"\beuler\b|suffix|etour|preor|pre-order|n[aá]sledovn",
    "Monitory/semafory": r"monitor|semafor|wait\b|signal\b|cten[aá]r|p[ií]sa[rř]|readers|writers",
    "Mutual exclusion": r"test.?and.?set|critical section|kritick[áa] sekce|lock\b|vz[aá]jemn[eé] vylou",
    "OCCAM": r"\boccam\b|channel|queue|fronta|clk|out_left|out_right|altern",
    "Pi-kalkul": r"pi.?kalkul|redukce|pi calculus|pi-calculus",
    "CLA": r"\bcla\b|carry.?look.?ahead",
    "Distributed": r"ricart|lamport|maekawa|suzuki|token|quorum|kvor|broadcast",
    "Random/list": r"random mating|enumeration sort|pipeline merge sort|splitting|select|odd-even-transposition",
}

EXAM_SIGNAL_RE = re.compile(
    r"predtermin|p[řr]edterm[ií]n|riadny|radny|opravn|skupina|term[ií]n|zkou[sš]k|sk[uú][sš]ka",
    re.IGNORECASE,
)
URL_RE = re.compile(r"https?://", re.IGNORECASE)


def load_exports() -> list[tuple[str, dict]]:
    exports = []
    for year_dir in sorted(INPUT_DIR.iterdir()):
        path = year_dir / CHANNEL_FILE_NAME
        if path.exists():
            exports.append((year_dir.name, json.loads(path.read_text())))
    return exports


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def trim_text(text: str, limit: int = 280) -> str:
    text = normalize_text(text)
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def main() -> None:
    exports = load_exports()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    compiled_topics = {name: re.compile(pattern, re.IGNORECASE) for name, pattern in TOPIC_PATTERNS.items()}

    total_messages = 0
    total_bots = 0
    total_attachments = 0
    total_embeds = 0
    total_reactions = 0
    total_pins = 0
    total_link_messages = 0

    yearly_rows = []
    top_authors_global: Counter[str] = Counter()
    top_days: Counter[str] = Counter()
    top_months: Counter[str] = Counter()
    topic_mentions: Counter[str] = Counter()
    topic_messages: Counter[str] = Counter()
    pinned_records: list[dict] = []
    exam_signal_records: list[dict] = []
    attachment_authors: Counter[str] = Counter()
    topic_examples: dict[str, list[dict]] = defaultdict(list)

    for year, export in exports:
        messages = export["messages"]
        authors_year = Counter()
        year_topic_messages: Counter[str] = Counter()
        with_attachments = 0
        with_links = 0
        with_pins = 0

        for message in messages:
            total_messages += 1
            author = message["author"]["name"]
            authors_year[author] += 1
            top_authors_global[author] += 1

            if message["author"].get("isBot"):
                total_bots += 1

            ts = message["timestamp"]
            day = ts[:10]
            month = ts[:7]
            top_days[day] += 1
            top_months[month] += 1

            content = message.get("content") or ""
            content_one_line = trim_text(content)

            attachments = message.get("attachments") or []
            embeds = message.get("embeds") or []
            reactions = message.get("reactions") or []
            is_pinned = bool(message.get("isPinned"))

            if attachments:
                with_attachments += 1
                total_attachments += len(attachments)
                attachment_authors[author] += 1
            if embeds:
                total_embeds += len(embeds)
            if reactions:
                total_reactions += len(reactions)
            if is_pinned:
                with_pins += 1
                total_pins += 1
                pinned_records.append(
                    {
                        "year": year,
                        "timestamp": ts,
                        "author": author,
                        "content": content_one_line,
                    }
                )
            if URL_RE.search(content):
                with_links += 1
                total_link_messages += 1

            if EXAM_SIGNAL_RE.search(content) and len(content.strip()) >= 80:
                exam_signal_records.append(
                    {
                        "year": year,
                        "timestamp": ts,
                        "author": author,
                        "content": content_one_line,
                    }
                )

            for topic_name, regex in compiled_topics.items():
                hits = regex.findall(content)
                if not hits:
                    continue
                topic_mentions[topic_name] += len(hits)
                topic_messages[topic_name] += 1
                year_topic_messages[topic_name] += 1
                if len(topic_examples[topic_name]) < 5 and content_one_line:
                    topic_examples[topic_name].append(
                        {
                            "year": year,
                            "timestamp": ts,
                            "author": author,
                            "content": content_one_line,
                        }
                    )

        date_after = export["dateRange"]["after"][:10]
        date_before = export["dateRange"]["before"][:10]
        top_three_topics = ", ".join(
            f"{name} ({count})" for name, count in year_topic_messages.most_common(3)
        )
        top_three_authors = ", ".join(
            f"{name} ({count})" for name, count in authors_year.most_common(3)
        )
        yearly_rows.append(
            {
                "year": year,
                "messages": len(messages),
                "date_after": date_after,
                "date_before": date_before,
                "attachments_messages": with_attachments,
                "link_messages": with_links,
                "pinned_messages": with_pins,
                "top_authors": top_three_authors,
                "top_topics": top_three_topics,
            }
        )

    yearly_lines = [
        "year\tmessages\tdate_after\tdate_before\tattachments_messages\tlink_messages\tpinned_messages\ttop_authors\ttop_topics"
    ]
    for row in yearly_rows:
        yearly_lines.append(
            "\t".join(
                [
                    row["year"],
                    str(row["messages"]),
                    row["date_after"],
                    row["date_before"],
                    str(row["attachments_messages"]),
                    str(row["link_messages"]),
                    str(row["pinned_messages"]),
                    row["top_authors"],
                    row["top_topics"],
                ]
            )
        )
    write_text(OUTPUT_DIR / "yearly_summary.tsv", "\n".join(yearly_lines) + "\n")

    topic_lines = ["topic\tmentions\tmessages"]
    for topic_name, mention_count in topic_mentions.most_common():
        topic_lines.append(f"{topic_name}\t{mention_count}\t{topic_messages[topic_name]}")
    write_text(OUTPUT_DIR / "topic_counts.tsv", "\n".join(topic_lines) + "\n")

    month_lines = ["month\tmessages"]
    for month, count in sorted(top_months.items()):
        month_lines.append(f"{month}\t{count}")
    write_text(OUTPUT_DIR / "monthly_counts.tsv", "\n".join(month_lines) + "\n")

    day_lines = ["day\tmessages"]
    for day, count in top_days.most_common(30):
        day_lines.append(f"{day}\t{count}")
    write_text(OUTPUT_DIR / "top_days.tsv", "\n".join(day_lines) + "\n")

    pinned_md = ["# Pinned Discord messages", ""]
    for record in pinned_records:
        pinned_md.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )
    write_text(OUTPUT_DIR / "pinned_messages.md", "\n".join(pinned_md) + "\n")

    exam_signal_records.sort(key=lambda item: (item["year"], item["timestamp"]))
    exam_md = ["# Exam-signal messages", ""]
    for record in exam_signal_records[:120]:
        exam_md.append(
            f"- `{record['year']}` `{record['timestamp']}` `{record['author']}`: {record['content']}"
        )
    write_text(OUTPUT_DIR / "exam_signal_messages.md", "\n".join(exam_md) + "\n")

    overview = {
        "generatedAt": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "years": [year for year, _ in exports],
        "messageCount": total_messages,
        "botMessageCount": total_bots,
        "attachmentCount": total_attachments,
        "embedCount": total_embeds,
        "reactionCount": total_reactions,
        "pinnedMessageCount": total_pins,
        "linkMessageCount": total_link_messages,
        "topAuthors": top_authors_global.most_common(15),
        "topAttachmentAuthors": attachment_authors.most_common(10),
        "topDays": top_days.most_common(15),
        "topicCounts": [[name, topic_mentions[name], topic_messages[name]] for name in topic_mentions],
    }
    write_text(OUTPUT_DIR / "overview.json", json.dumps(overview, ensure_ascii=False, indent=2) + "\n")

    summary_md = [
        "# Discord analysis scratchpad",
        "",
        "This is a side analysis generated from `raw/discord/<year>/621775635722928128.json`.",
        "It does not modify the knowledge base.",
        "",
        "## High-level",
        "",
        f"- Years covered: {', '.join(overview['years'])}",
        f"- Total messages: {total_messages}",
        f"- Bot messages: {total_bots} ({(100 * total_bots / total_messages):.2f}%)",
        f"- Attachments: {total_attachments}",
        f"- Embeds: {total_embeds}",
        f"- Reactions: {total_reactions}",
        f"- Pinned messages: {total_pins}",
        f"- Link-bearing messages: {total_link_messages}",
        "",
        "## Strong signals",
        "",
        f"- Peak month by volume: `{top_months.most_common(1)[0][0]}` with `{top_months.most_common(1)[0][1]}` messages.",
        f"- Peak day by volume: `{top_days.most_common(1)[0][0]}` with `{top_days.most_common(1)[0][1]}` messages.",
        f"- Most active author overall: `{top_authors_global.most_common(1)[0][0]}` with `{top_authors_global.most_common(1)[0][1]}` messages.",
        "",
        "## Topic counts",
        "",
    ]
    for topic_name, mention_count in topic_mentions.most_common():
        summary_md.append(
            f"- `{topic_name}`: {mention_count} mentions across {topic_messages[topic_name]} messages."
        )

    summary_md.extend(["", "## Topic examples", ""])
    for topic_name, examples in topic_examples.items():
        summary_md.append(f"### {topic_name}")
        summary_md.append("")
        for example in examples[:3]:
            summary_md.append(
                f"- `{example['year']}` `{example['timestamp']}` `{example['author']}`: {example['content']}"
            )
        summary_md.append("")

    write_text(OUTPUT_DIR / "summary.md", "\n".join(summary_md))


if __name__ == "__main__":
    main()
