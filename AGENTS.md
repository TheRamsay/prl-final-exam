# Agent Guide

This repository is a PRL final exam knowledge base. Prefer answering from the Markdown vault before using external sources.

## Start Here

- Human entrypoint: `knowledge/00-rozcestnik.md`
- LLM entrypoint: `knowledge/99-llm-index.md`
- ROI study plan: `knowledge/01-roi-plan.md`
- Topic frequency summary: `knowledge/02-cetnosti-temat.md`
- Exam archive index: `knowledge/exams/00-index.md`
- Raw source archive: `raw/`

## Source Priority

1. `knowledge/topics/*.md` for distilled knowledge and answer templates.
2. `knowledge/exams/**/term-*.md` for normalized past exam questions.
3. `knowledge/exams/_verification/raw-vs-student-doc.md` for source agreement and uncertainty.
4. `raw/*.md` and `raw/*.webp` for original material.
5. `knowledge/sources/student-doc/**` for extracted student-document context.

## Search Patterns

Use `rg` first.

```sh
rg -n "PRAM|CRCW|EREW" knowledge raw
rg -n "Termínový label|Jednotné zadání|Tématické odkazy" knowledge/exams
rg -n "\\[\\[knowledge/topics/pram-tipovacka" knowledge/exams
rg -n "Verifikační status|student_doc|raw only|shoda" knowledge/exams/_verification
```

## Answering Rules

- When answering exam-study questions, cite the relevant topic note and at least one past exam file when possible.
- When there is disagreement or uncertainty, check `knowledge/exams/_verification/raw-vs-student-doc.md` and mention it.
- Do not treat `raw/student_doc.md` as fully normalized; use the extracted files under `knowledge/sources/student-doc/` when possible.
- Keep Obsidian/Quartz links explicit: use `[[knowledge/...]]` or `[[raw/...]]`, not bare relative wikilinks.
- Preserve Czech terminology used in the vault: `předtermín`, `řádný termín`, `1. opravný termín`, `2. opravný termín`.
