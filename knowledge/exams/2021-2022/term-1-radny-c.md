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

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Signál v zadání | Topic |
|---:|---|---|
| 1 | PRAM / Tipsport | [[knowledge/topics/pram-tipovacka]] |
| 2 | Xeon Phi | [[knowledge/topics/architektury]] |
| 3 | Etour + suffixsum | [[knowledge/topics/euler-tour-suffix-sums]] |
| 4 | Monitor | [[knowledge/topics/synchronizace-monitory-semafory]] |
| 5 | Asynchronní/synchronní signály | [[knowledge/topics/broadcast-fifo-kauzalita]] |
| 6 | Prescan | [[knowledge/topics/razeni-prefix]] |
| 7 | OCCAM | [[knowledge/topics/occam]] |
| 8 | MPI | [[knowledge/topics/mpi-reduce-bcast]] |

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
