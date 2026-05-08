# 2021/2022 - řádný termín - varianta C

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2021/2022 |
| Termínový label | řádný termín |
| Typ | řádný termín |
| Varianta | C |
| Forma | přepsaný obrázek z Discordu |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc doplňuje raw` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2021-2022]] |
| Primární zdroj zadání | raw screenshot; student doc rozšiřuje řešení |

## Student doc reference

- [[knowledge/sources/student-doc/2021-2022-extract]] obsahuje odpovídající řádný termín C s dílčími řešeními.
- Destilace: [[knowledge/exams/2021-2022/student-doc-digest]]

## Původní zdroje

- Obrázek: [[raw/term_1_2021_c_img.webp]]
- Kopie obrázku ve vaultu: ![[knowledge/assets/term_1_2021_c_img.webp]]

## Tématické odkazy

- [[knowledge/topics/pram-tipovacka|PRAM / Tipsport]]
- [[knowledge/topics/architektury|Xeon Phi]]
- [[knowledge/topics/euler-tour-suffix-sums|Etour + suffixsum]]
- [[knowledge/topics/synchronizace-monitory-semafory|Monitor]]
- [[knowledge/topics/broadcast-fifo-kauzalita|Asynchronní/synchronní signály]]
- [[knowledge/topics/razeni-prefix|Prescan]]
- [[knowledge/topics/occam|OCCAM]]
- [[knowledge/topics/mpi-reduce-bcast|MPI]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Téma | Signál v zadání |
|---:|---|---|
| 1 | [[knowledge/topics/pram-tipovacka]] | PRAM / Tipsport |
| 2 | [[knowledge/topics/architektury]] | Xeon Phi |
| 3 | [[knowledge/topics/euler-tour-suffix-sums]] | Etour + suffixsum |
| 4 | [[knowledge/topics/synchronizace-monitory-semafory]] | Monitor |
| 5 | [[knowledge/topics/broadcast-fifo-kauzalita]] | Asynchronní/synchronní signály |
| 6 | [[knowledge/topics/razeni-prefix]] | Prescan |
| 7 | [[knowledge/topics/occam]] | OCCAM |
| 8 | [[knowledge/topics/mpi-reduce-bcast]] | MPI |

## Jednotné zadání

1. Tipsport extra liga.
2. Xeon.
3. Je dán `etour` a `suffixsum`; zjistit, kolik je následujících vrcholů, popsat princip a určit časovou náročnost.
4. Monitor.
5. Jsou asynchronní signály a určit, zda jdou přeuspořádat tak, aby šly volat synchronně.
6. Prescan.
7. OCCAM: mám kanály `1-10` a může přijít `adr` nebo `in`; když do `adr` přijde `1-10`, nastavím aktivní index na to číslo, jinak na `0`; když do `in` něco přijde, vložím to na aktivní channel.
8. MPI: počet prvků stejných jako max a stejných jako min v logaritmickém čase.

## Rozdíly / doplnění ze student_doc

- Viz sekce `Stav verifikace` a `Student doc reference`; detailní roční porovnání je v [[knowledge/exams/_verification/raw-vs-student-doc]].

## Poznámky k nejistotám

- Přepis je z krátké Discord zprávy; nejde o plné zadání.
