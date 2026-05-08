# 2021/2022 - 1. opravný termín - varianta B

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2021/2022 |
| Termínový label | 1. opravný termín |
| Typ | 1. opravný termín |
| Varianta | B |
| Forma | student doc |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc only` |
| Kontrolní matice | [[exams/_verification/raw-vs-student-doc#2021-2022]] |
| Primární zdroj zadání | student doc |

## Student doc reference

- Extract: [[sources/student-doc/2021-2022-extract]]
- Roční digest: [[student-doc-digest]]

## Původní zdroje

- Raw dokument: [raw/student_doc.md](../../../raw/student_doc.md)
- Očištěný zdroj: [[sources/student-doc/clean]]

## Tématické odkazy

- [[topics/pram-tipovacka|Common CRCW AND]]
- Xeon Phi
- [[topics/razeni-prefix|Odd-even merge sort]]
- [[topics/distribuovane-algoritmy|Marzullo]]
- [[topics/broadcast-fifo-kauzalita|Async -> sync]]
- [[topics/razeni-prefix|Enumeration Sort]]
- [[topics/occam|OCCAM]]
- [[topics/mpi-reduce-bcast|MPI]]

## Jednotné zadání

1. Udělat AND pro common CRCW. Popsat princip + příklad.
2. Xeon Phi: popsat + obrázek.
3. Odd-even merge sort + nakreslit síť 4x4 pomocí CE porovnávaček.
4. Marzullův algoritmus.
5. Async -> sync: zda se dá synchronizovat, jak se to detekuje a které zprávy tomu brání.
6. Enumeration Sort.
7. OCCAM: procedura s polem kanálů `OUT[10]`, kanály `IN` a `ALT`; `ALT` zapíná/vypíná alternování, `IN` se posílá na aktuální kanál.
8. MPI: každý proces má prvek; zjistit, zda sudé procesory mají sudé prvky a liché procesory liché prvky.

## Rozdíly / doplnění ze student_doc

- Termín je jen ve studentském dokumentu.
- Student doc obsahuje částečná řešení k Odd-even merge, Marzullo, OCCAM a MPI.

## Poznámky k nejistotám

- U Xeon Phi je ve zdroji poznámka, že pravděpodobně chtěli architekturní obrázek se skalární/vektorovou jednotkou/cache.

