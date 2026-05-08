# 2018/2019 - řádný termín - varianta C

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2018/2019 |
| Termínový label | řádný termín |
| Typ | řádný termín |
| Varianta | C |
| Forma | student doc |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc only` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2018-2019]] |
| Primární zdroj zadání | student doc |

## Student doc reference

- Extract: [[knowledge/sources/student-doc/2018-2019-extract]]
- Roční digest: [[knowledge/exams/2018-2019/student-doc-digest]]

## Původní zdroje

- Raw dokument: [[raw/student_doc]]
- Očištěný zdroj: [[knowledge/sources/student-doc/clean]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Signál v zadání | Topic |
|---:|---|---|
| 1 | PRAM | [[knowledge/topics/pram-tipovacka]] |
| 2 | Zřetězené procesory | [[knowledge/topics/architektury]] |
| 3 | Odd-even merge | [[knowledge/topics/razeni-prefix]] |
| 4 | Marzullo | [[knowledge/topics/distribuovane-algoritmy]] |
| 5 | Pi-kalkul | [[knowledge/topics/pi-kalkul]] |
| 6 | Prescan | [[knowledge/topics/razeni-prefix]] |
| 7 | CLA | [[knowledge/topics/cla]] |
| 8 | MPI | [[knowledge/topics/mpi-reduce-bcast]] |

## Jednotné zadání

1. PRAM otázky:
   - Časová složitost operace XOR.
   - Cena kontroly, zda je posloupnost monotónní.
   - Časová složitost součtu absolutních hodnot prvků posloupnosti.
2. Popsat architekturu zřetězených procesorů + nákres.
3. Popsat odd-even merge + nakreslit obecnou schéma a síť 4x4 pomocí CE bloků.
4. Popsat Marzullův algoritmus; součástí byl i příklad podobný přednáškám.
5. Pi-kalkul - redukovat výraz a napsat pozorování.
6. Prescan - zapsat výsledek po prvním kroku a po skončení up-sweep, potom po prvním kroku a po skončení down-sweep.
7. CLA sčítačka: `77 + 125`.
8. MPI - počet prvků, které jsou beze zbytku dělitelné prvním prvkem; k dispozici jen `MPI_Bcast` a `MPI_Reduce`, požadovaná logaritmická časová složitost.

## Rozdíly / doplnění ze student_doc

- Termín je jen ve studentském dokumentu.
- Student doc obsahuje doplňkové poznámky k prescanu a CLA.

## Poznámky k nejistotám

- Prescan řešení ve zdroji obsahuje komentář, že v ukázce může být chyba.

