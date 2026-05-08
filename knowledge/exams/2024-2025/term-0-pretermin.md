# 2024/2025 - předtermín

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2024/2025 |
| Termínový label | předtermín |
| Typ | předtermín |
| Varianta | nezadaná |
| Forma | student doc |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc only` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2024-2025]] |
| Primární zdroj zadání | student doc |

## Student doc reference

- Extract: [[knowledge/sources/student-doc/2024-2025-extract]]
- Roční digest: [[knowledge/exams/2024-2025/student-doc-digest]]

## Původní zdroje

- Raw dokument: [[raw/student_doc]]
- Očištěný zdroj: [[knowledge/sources/student-doc/clean]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Signál v zadání | Topic |
|---:|---|---|
| 1 | PRAM Tipsport | [[knowledge/topics/pram-tipovacka]] |
| 2 | Zřetězení | [[knowledge/topics/architektury]] |
| 3 | Koruna a synchronizovatelnost | [[knowledge/topics/broadcast-fifo-kauzalita]] |
| 4 | Parallel splitting | [[knowledge/topics/parallel-splitting-select]] |
| 5 | Euler tour | [[knowledge/topics/euler-tour-suffix-sums]] |
| 6 | Enumeration Sort | [[knowledge/topics/razeni-prefix]] |
| 7 | OCCAM | [[knowledge/topics/occam]] |
| 8 | MPI | [[knowledge/topics/mpi-reduce-bcast]] |

## Jednotné zadání

1. Tipsport CRCW - NOT, OR, zda array obsahuje čísla větší než 0.
   - U OR se ptal na cenu.
   - U NOT a `čísla > 0` se ptal na časovou složitost.
2. Jak se uplatní zřetězení v aritmetických operacích, nakreslit příklad.
3. Co je koruna, příklad komunikace, kde koruna je a kde není.
4. Parallel splitting, ukázat na příkladu.
5. Euler tour - adjacency list, tabulka, nakreslit graf, vypsat `Etour`.
6. Sequential Enumeration Sort, 6. krok.
7. OCCAM, byte channels `data`, `ctrl`, `out[5]`; data odeslat na výstupní kanál specifikovaný hodnotou z `ctrl`.
8. MPI, normalizace čísel do intervalu `<0, 1>`.

## Rozdíly / doplnění ze student_doc

- Termín je jen ve studentském dokumentu; nemáme odpovídající `raw/term*.md`.

## Poznámky k nejistotám

- Zdroj je stručný studentský seznam, ne originální zadání.

