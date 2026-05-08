# 2019/2020 - student doc digest

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2019/2020 |
| Zdroj | studentský dokument |
| Stav | první destilace |
| Auditovatelný extract | [[knowledge/sources/student-doc/2019-2020-extract]] |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc only` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2019-2020]] |

## Původní zdroje

- Raw dokument: [[raw/student_doc]]
- Očištěný zdroj: [[knowledge/sources/student-doc/clean]]
- Extract roku: [[knowledge/sources/student-doc/2019-2020-extract]]

## Přehled termínů

### Term 1 - řádný termín - skupina A

Samostatný soubor: [[knowledge/exams/2019-2020/term-1-radny-a]]

1. [[knowledge/topics/pram-tipovacka|PRAM tipovačka]] - tři části: čas EREW, cena CREW, čas common CRCW.
   - Zdroj uvádí příklady: součin prvků `O(log n)`, OR cena `n log n`, nejasné `unsorted`.
2. [[knowledge/topics/architektury|VLIW]] - popis a obrázek.
3. [[knowledge/topics/synchronizace-monitory-semafory|Monitor]] - `signal`, `wait`, obrázek.
4. [[knowledge/topics/broadcast-fifo-kauzalita|Broadcasty]] - určit FIFO, kauzalitu, atomičnost; jednu vlastnost opravit a překreslit.
5. [[knowledge/topics/occam|OCCAM]] - popis, primitiva, obrázek.
6. [[knowledge/topics/euler-tour-suffix-sums|Stromy / preorder přes Etour + suffix]] - algoritmus, popis, složitost.
7. [[knowledge/topics/distribuovane-algoritmy|Random mating]] - demonstrovat na příkladu do 4 kroků.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - počet prvků větších než průměr.

### Term 1 - řádný termín - skupina B

Samostatný soubor: [[knowledge/exams/2019-2020/term-1-radny-b]]

1. [[knowledge/topics/pram-tipovacka|PRAM]] - cena algoritmu řazení, cena zjištění shodných prvků, čas AND.
2. [[knowledge/topics/architektury|Zřetězené procesory]].
3. [[knowledge/topics/synchronizace-monitory-semafory|Producent-konzument]] - kód.
4. [[knowledge/topics/euler-tour-suffix-sums|Euler + suffix sum]].
5. [[knowledge/topics/broadcast-fifo-kauzalita|Broadcast]].
6. [[knowledge/topics/razeni-prefix|Prescan]] - up-sweep, down-sweep.
7. [[knowledge/topics/linda-ada|Linda]] - synchronizace nebo vyloučení.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - pro 16 prvků zjistit, zda existují alespoň 2 různé hodnoty.
   - Zdroj řeší přes `Reduce MAX`, `Reduce MIN`, root porovná `max != min`.

### Term 2 - 1. opravný termín

Samostatný soubor: [[knowledge/exams/2019-2020/term-2-prvni-opravny]]

1. [[knowledge/topics/pram-tipovacka|PRAM jako na každém termínu]].
2. [[knowledge/topics/architektury|Xeon Phi]] architektura - kombinace SIMD a MIMD.
3. [[knowledge/topics/razeni-prefix|Odd-even merge sort]] - popis algoritmu, síť 4x4.
4. [[knowledge/topics/distribuovane-algoritmy|Marzullo]] - popis a příklad.
5. [[knowledge/topics/cla|CLA]] - podrobný postup sčítání dvou čísel.
6. [[knowledge/topics/synchronizace-monitory-semafory|Semafor]] - operace, princip.
   - Zdroj uvádí `P(S)`, `V(S)`, blokování ve FIFO frontě, význam `S.count`.
7. [[knowledge/topics/linda-ada|Linda]].
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - průměr čísel větších než průměr všech.
   - Šablona: spočítat globální průměr, filtrovat větší prvky, redukovat jejich součet i počet, root vydělí.

## Využitelné řešicí poznámky

- Rok 2019/2020 rozšiřuje hlavně broadcast vlastnosti, OCCAM primitiva, [[knowledge/topics/distribuovane-algoritmy|Random mating]] a MPI varianty.
- Některá PRAM zadání jsou ve zdroji neúplná; digest drží jen to, co je čitelné.
