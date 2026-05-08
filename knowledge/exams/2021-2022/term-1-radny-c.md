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
| Kontrolní matice | [[exams/_verification/raw-vs-student-doc#2021-2022]] |
| Primární zdroj zadání | raw screenshot; student doc rozšiřuje řešení |

## Student doc reference

- [[sources/student-doc/2021-2022-extract]] obsahuje odpovídající řádný termín C s dílčími řešeními.
- Destilace: [[student-doc-digest]]

## Původní zdroje

- Obrázek: [raw/term_1_2021_c_img.webp](../../../raw/term_1_2021_c_img.webp)
- Kopie obrázku ve vaultu: ![[term_1_2021_c_img.webp]]

## Tématické odkazy

- [[topics/pram-tipovacka|PRAM / Tipsport]]
- Xeon Phi
- [[topics/euler-tour-suffix-sums|Etour + suffixsum]]
- [[topics/synchronizace-monitory-semafory|Monitor]]
- [[topics/broadcast-fifo-kauzalita|Asynchronní/synchronní signály]]
- [[topics/razeni-prefix|Prescan]]
- [[topics/occam|OCCAM]]
- [[topics/mpi-reduce-bcast|MPI]]

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

- Viz sekce `Stav verifikace` a `Student doc reference`; detailní roční porovnání je v [[exams/_verification/raw-vs-student-doc]].

## Poznámky k nejistotám

- Přepis je z krátké Discord zprávy; nejde o plné zadání.
