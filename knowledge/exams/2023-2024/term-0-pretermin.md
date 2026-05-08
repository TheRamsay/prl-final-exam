# 2023/2024 - předtermín

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2023/2024 |
| Termínový label | předtermín |
| Typ | předtermín |
| Varianta | nezadaná |
| Forma | text |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `shoda` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2023-2024]] |
| Primární zdroj zadání | raw text |

## Student doc reference

- [[knowledge/sources/student-doc/2023-2024-extract]] potvrzuje pořadí i témata předtermínu.
- Porovnávací digest: [[knowledge/exams/2023-2024/student-doc-digest]]

## Původní zdroje

- Textový zdroj: [[raw/term_0_2023]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Signál v zadání | Topic |
|---:|---|---|
| 1 | PRAM tipovačka | [[knowledge/topics/pram-tipovacka]] |
| 2 | PRAM model | [[knowledge/topics/architektury]] |
| 3 | Kauzální broadcast | [[knowledge/topics/broadcast-fifo-kauzalita]] |
| 4 | Euler tour | [[knowledge/topics/euler-tour-suffix-sums]] |
| 5 | CLA | [[knowledge/topics/cla]] |
| 6 | Maekawa | [[knowledge/topics/distribuovane-algoritmy]] |
| 7 | OCCAM | [[knowledge/topics/occam]] |
| 8 | MPI | [[knowledge/topics/mpi-reduce-bcast]] |

## Jednotné zadání

1. Tipsport CRCW - XOR, NAND, AND.
2. PRAM model - popsat a nakreslit obrázek.
3. Kauzální broadcast a relace kauzality.
4. Euler pro počet následovníků a popis.
5. CLA.
6. Maekawův algoritmus - popsat kvórum a na obrázku znázornit zalomenou verzi kvór pro 12 procesů; ukázat zjištění kvór pro 2 procesy.
7. OCCAM - implementovat proceduru s kanály `input`, `clk`, `OUT_LEFT`, `OUT_RIGHT`. Když přijde číslo na `input`, vloží se do vnitřní nekonečné fronty. Když přijde libovolná hodnota na `clk`, pošle se první prvek fronty střídavě na `OUT_LEFT` nebo `OUT_RIGHT` a ukazatel se posune ručně.
8. MPI - k dispozici je `reduce`, `broadcast`, rank procesu a počet prvků. Každý proces má proměnnou `value`. Napsat kód, ve kterém si každý proces vypočítá `value - average(values)` a výsledek vypíše ve formátu `rank: vysledek`.

## Rozdíly / doplnění ze student_doc

- Viz sekce `Stav verifikace` a `Student doc reference`; detailní roční porovnání je v [[knowledge/exams/_verification/raw-vs-student-doc]].

## Poznámky k nejistotám

- Zdroj je studentský textový přepis, ne originální sken.
