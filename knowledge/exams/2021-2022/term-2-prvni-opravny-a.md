# 2021/2022 - 1. opravný termín - varianta A

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2021/2022 |
| Termínový label | 1. opravný termín |
| Typ | 1. opravný termín |
| Varianta | A |
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

## Tématické odkazy

- [[knowledge/topics/pram-tipovacka|CRCW AND]]
- [[knowledge/topics/architektury|MIMD / Xeon Phi]]
- [[knowledge/topics/euler-tour-suffix-sums|Euler path + suffixsum]]
- [[knowledge/topics/razeni-prefix|Pipeline sort]]
- [[knowledge/topics/broadcast-fifo-kauzalita|Async -> sync a kauzalita]]
- [[knowledge/topics/distribuovane-algoritmy|FIFO algoritmy]]
- [[knowledge/topics/occam|OCCAM]]
- [[knowledge/topics/mpi-reduce-bcast|MPI]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Téma | Signál v zadání |
|---:|---|---|
| 1 | [[knowledge/topics/pram-tipovacka]] | CRCW AND |
| 2 | [[knowledge/topics/architektury]] | MIMD / Xeon Phi |
| 3 | [[knowledge/topics/euler-tour-suffix-sums]] | Euler path + suffixsum |
| 4 | [[knowledge/topics/razeni-prefix]] | Pipeline sort |
| 5 | [[knowledge/topics/broadcast-fifo-kauzalita]] | Async -> sync a kauzalita |
| 6 | [[knowledge/topics/distribuovane-algoritmy]] | FIFO algoritmy |
| 7 | [[knowledge/topics/occam]] | OCCAM |
| 8 | [[knowledge/topics/mpi-reduce-bcast]] | MPI |

## Jednotné zadání

1. Popsat algoritmus na CRCW pro AND a uvést příklad.
2. Kde využít MIMD, popsat + obrázek.
3. Suffixsum pro Euler path: výpočet úrovně vrcholu.
4. Jak budou vypadat procesory ve 12. kroku při Pipeline Sort.
5. Async -> sync: zda se dá převést; pokud ano, jak; pokud ne, proč; popsat relaci kauzality.
6. FIFO algoritmy.
7. OCCAM: kanály `ls`, `gt`, `in`, vstup `BYTE th`, buffer velikosti `SIZE`; podle podmínek ukládat do pole nebo posílat na `ls/gt`.
8. MPI: zjistit, zda suma prvků v první polovině je menší než suma prvků ve druhé polovině; vypsat ano/ne.

## Rozdíly / doplnění ze student_doc

- Termín je jen ve studentském dokumentu.
- Student doc přidává částečná řešení k CRCW AND, suffixsum, async -> sync a MPI.

## Poznámky k nejistotám

- FIFO algoritmy jsou ve zdroji odhadované jako Lamport/Ricart-Agrawala.
