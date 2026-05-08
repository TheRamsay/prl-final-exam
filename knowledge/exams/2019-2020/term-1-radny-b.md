# 2019/2020 - řádný termín - varianta B

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2019/2020 |
| Termínový label | řádný termín |
| Typ | řádný termín |
| Varianta | B |
| Forma | student doc |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc only` |
| Kontrolní matice | [[exams/_verification/raw-vs-student-doc#2019-2020]] |
| Primární zdroj zadání | student doc |

## Student doc reference

- Extract: [[sources/student-doc/2019-2020-extract]]
- Roční digest: [[student-doc-digest]]

## Původní zdroje

- Raw dokument: [raw/student_doc.md](../../../raw/student_doc.md)
- Očištěný zdroj: [[sources/student-doc/clean]]

## Tématické odkazy

- [[topics/pram-tipovacka|PRAM]]
- [[topics/architektury|Zřetězené procesory]]
- [[topics/synchronizace-monitory-semafory|Producent-konzument]]
- [[topics/euler-tour-suffix-sums|Euler + suffix sum]]
- [[topics/broadcast-fifo-kauzalita|Broadcast]]
- [[topics/razeni-prefix|Prescan]]
- [[topics/linda-ada|Linda]]
- [[topics/mpi-reduce-bcast|MPI]]

## Jednotné zadání

1. PRAM: cena algoritmu, který seřadí; cena algoritmu, který zjistí, zda je nějaký prvek shodný; časová složitost algoritmu, který spočítá AND.
2. Zřetězené procesory.
3. Kód producent-konzument.
4. Euler suffix sum.
5. Broadcast.
6. Prescan: up-sweep, down-sweep.
7. Linda - zadefinovat synchronizaci nebo vyloučení.
8. MPI v C++: pro 16 prvků zjistit, zda jsou alespoň 2 různé; požadovaná logaritmická časová složitost.

## Rozdíly / doplnění ze student_doc

- Termín je jen ve studentském dokumentu.
- Student doc obsahuje MPI řešení přes `Reduce MAX`, `Reduce MIN`, root porovná `max != min`.

## Poznámky k nejistotám

- Většina příkladů je jen stručně vypsaná bez plného zadání.

