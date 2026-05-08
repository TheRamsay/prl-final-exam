# 2019/2020 - řádný termín - varianta A

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2019/2020 |
| Termínový label | řádný termín |
| Typ | řádný termín |
| Varianta | A |
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

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Signál v zadání | Topic |
|---:|---|---|
| 1 | PRAM | [[knowledge/topics/pram-tipovacka]] |
| 2 | VLIW | [[knowledge/topics/architektury]] |
| 3 | Monitor | [[knowledge/topics/synchronizace-monitory-semafory]] |
| 4 | Broadcast | [[knowledge/topics/broadcast-fifo-kauzalita]] |
| 5 | OCCAM | [[knowledge/topics/occam]] |
| 6 | Etour + suffix | [[knowledge/topics/euler-tour-suffix-sums]] |
| 7 | Random mating | [[knowledge/topics/distribuovane-algoritmy]] |
| 8 | MPI | [[knowledge/topics/mpi-reduce-bcast]] |

## Jednotné zadání

1. PRAM tipovačka se třemi částmi: časová složitost EREW pro jeden algoritmus, cena CREW pro jiný algoritmus, časová složitost common CRCW pro další algoritmus.
2. VLIW - popsat, obrázek.
3. Monitor - popsat, hlavně `signal` a `wait`, obrázek.
4. Broadcasty - pro dva obrázky určit FIFO, kauzalitu, atomičnost; jednu vlastnost opravit a překreslit.
5. OCCAM - popsat, primitiva, obrázek.
6. Stromy - algoritmus pro preorder, když máme funkci suffix a cesty uložené ve struktuře `Etour`; popsat a uvést složitost.
7. Random mating - použít na příkladu tak, aby skončil ve 4 krocích.
8. MPI - počet prvků, jejichž hodnota je větší než průměrná.

## Rozdíly / doplnění ze student_doc

- Termín je jen ve studentském dokumentu.
- Student doc obsahuje MPI řešení přes globální průměr a redukci počtu větších prvků.

## Poznámky k nejistotám

- Některé PRAM části jsou v textu neúplné nebo špatně čitelné.
