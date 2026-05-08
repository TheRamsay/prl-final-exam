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
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2019-2020]] |
| Primární zdroj zadání | student doc |

## Student doc reference

- Extract: [[knowledge/sources/student-doc/2019-2020-extract]]
- Roční digest: [[knowledge/exams/2019-2020/student-doc-digest]]

## Původní zdroje

- Raw dokument: [[raw/student_doc]]
- Očištěný zdroj: [[knowledge/sources/student-doc/clean]]

## Tématické odkazy

- [[knowledge/topics/pram-tipovacka|PRAM]]
- [[knowledge/topics/architektury|Zřetězené procesory]]
- [[knowledge/topics/synchronizace-monitory-semafory|Producent-konzument]]
- [[knowledge/topics/euler-tour-suffix-sums|Euler + suffix sum]]
- [[knowledge/topics/broadcast-fifo-kauzalita|Broadcast]]
- [[knowledge/topics/razeni-prefix|Prescan]]
- [[knowledge/topics/linda-ada|Linda]]
- [[knowledge/topics/mpi-reduce-bcast|MPI]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Téma | Signál v zadání |
|---:|---|---|
| 1 | [[knowledge/topics/pram-tipovacka|PRAM]] | PRAM |
| 2 | [[knowledge/topics/architektury|Zřetězené procesory]] | Zřetězené procesory |
| 3 | [[knowledge/topics/synchronizace-monitory-semafory|Producent-konzument]] | Producent-konzument |
| 4 | [[knowledge/topics/euler-tour-suffix-sums|Euler + suffix sum]] | Euler + suffix sum |
| 5 | [[knowledge/topics/broadcast-fifo-kauzalita|Broadcast]] | Broadcast |
| 6 | [[knowledge/topics/razeni-prefix|Prescan]] | Prescan |
| 7 | [[knowledge/topics/linda-ada|Linda]] | Linda |
| 8 | [[knowledge/topics/mpi-reduce-bcast|MPI]] | MPI |

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

