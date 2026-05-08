# 2022/2023 - předtermín

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2022/2023 |
| Termínový label | předtermín |
| Typ | předtermín |
| Varianta | nezadaná |
| Forma | student doc |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc only` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2022-2023]] |
| Primární zdroj zadání | student doc |

## Student doc reference

- Extract: [[knowledge/sources/student-doc/2022-2023-extract]]
- Roční digest: [[knowledge/exams/2022-2023/student-doc-digest]]

## Původní zdroje

- Raw dokument: [[raw/student_doc]]
- Očištěný zdroj: [[knowledge/sources/student-doc/clean]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Signál v zadání | Topic |
|---:|---|---|
| 1 | PRAM sportka | [[knowledge/topics/pram-tipovacka]] |
| 2 | FIFO broadcast a kauzalita | [[knowledge/topics/broadcast-fifo-kauzalita]] |
| 3 | Pi-kalkul | [[knowledge/topics/pi-kalkul]] |
| 4 | Euler | [[knowledge/topics/euler-tour-suffix-sums]] |
| 5 | Redukční počítač | [[knowledge/topics/architektury]] |
| 6 | Synchronizovatelnost | [[knowledge/topics/broadcast-fifo-kauzalita]] |
| 7 | Test-and-set a swap | [[knowledge/topics/mutual-exclusion]] |
| 8 | MPI | [[knowledge/topics/mpi-reduce-bcast]] |

## Jednotné zadání

1. Tipování složitosti PRAM sportka.
2. Napsat kód FIFO broadcastu a popsat relaci kauzality.
3. Pi-kalkul.
4. Euler.
5. Redukční počítač.
6. Otázka, zda lze synchronizovat procesy.
7. Implementace aktivním čekáním `test&set` a `swap`.
8. MPI: `max % min == 0`.

## Rozdíly / doplnění ze student_doc

- Termín je jen ve studentském dokumentu; nemáme odpovídající `raw/term*.md`.
- Student doc obsahuje několik placeholderů obrázků a náznak řešení k PRAM.

## Poznámky k nejistotám

- Některá řešení ve zdroji jsou diskusní a nejsou potvrzená.
