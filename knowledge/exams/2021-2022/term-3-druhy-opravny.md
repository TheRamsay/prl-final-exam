# 2021/2022 - 2. opravný termín

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2021/2022 |
| Termínový label | 2. opravný termín |
| Typ | 2. opravný termín |
| Varianta | nezadaná |
| Forma | student doc |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc only` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2021-2022]] |
| Primární zdroj zadání | student doc |

## Student doc reference

- Extract: [[knowledge/sources/student-doc/2021-2022-extract]]
- Roční digest: [[knowledge/exams/2021-2022/student-doc-digest]]

## Původní zdroje

- Raw dokument: [[raw/student_doc]]
- Očištěný zdroj: [[knowledge/sources/student-doc/clean]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Signál v zadání | Topic |
|---:|---|---|
| 1 | PRAM | [[knowledge/topics/pram-tipovacka]] |
| 2 | Dataflow | [[knowledge/topics/architektury]] |
| 3 | Semafor | [[knowledge/topics/synchronizace-monitory-semafory]] |
| 4 | FIFO broadcast | [[knowledge/topics/broadcast-fifo-kauzalita]] |
| 5 | Async -> sync | [[knowledge/topics/broadcast-fifo-kauzalita]] |
| 6 | Random mating | [[knowledge/topics/distribuovane-algoritmy]] |
| 7 | Linda | [[knowledge/topics/linda-ada]] |
| 8 | MPI | [[knowledge/topics/mpi-reduce-bcast]] |

## Jednotné zadání

1. PRAM tipovačka.
2. Popsat Dataflow architekturu + obrázek.
3. Semafor - popsat operace `P` a `V`.
4. FIFO broadcast - jak probíhá přijímání a odesílání a algoritmy.
5. Příklad na async -> sync.
6. Random mating, skončit první fázi do 4 kroků.
7. Linda - vyhledávání v lineárním seznamu.
8. MPI: najít druhé maximum; pozor, hodnoty mohou být záporné.

## Rozdíly / doplnění ze student_doc

- Termín je jen ve studentském dokumentu.
- Student doc obsahuje konkrétní Linda pseudokód pro vyhledávání.

## Poznámky k nejistotám

- MPI řešení není ve zdroji doplněné.
