# 2018/2019 - řádný termín - varianta A

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2018/2019 |
| Termínový label | řádný termín |
| Typ | řádný termín |
| Varianta | A |
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

## Tématické odkazy

- [[knowledge/topics/pram-tipovacka|PRAM]]
- [[knowledge/topics/architektury|Granularita paralelismu]]
- [[knowledge/topics/razeni-prefix|Odd-even transposition sort]]
- [[knowledge/topics/distribuovane-algoritmy|Maekawa]]
- [[knowledge/topics/pi-kalkul|Pi-kalkul]]
- [[knowledge/topics/euler-tour-suffix-sums|Eulerův tah]]
- [[knowledge/topics/cla|CLA]]
- [[knowledge/topics/mpi-reduce-bcast|MPI]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Téma | Signál v zadání |
|---:|---|---|
| 1 | [[knowledge/topics/pram-tipovacka|PRAM]] | PRAM |
| 2 | [[knowledge/topics/architektury|Granularita paralelismu]] | Granularita paralelismu |
| 3 | [[knowledge/topics/razeni-prefix|Odd-even transposition sort]] | Odd-even transposition sort |
| 4 | [[knowledge/topics/distribuovane-algoritmy|Maekawa]] | Maekawa |
| 5 | [[knowledge/topics/pi-kalkul|Pi-kalkul]] | Pi-kalkul |
| 6 | [[knowledge/topics/euler-tour-suffix-sums|Eulerův tah]] | Eulerův tah |
| 7 | [[knowledge/topics/cla|CLA]] | CLA |
| 8 | [[knowledge/topics/mpi-reduce-bcast|MPI]] | MPI |

## Jednotné zadání

1. PRAM otázky, 6 b:
   - Cena optimálního algoritmu pro AND prvků `1/0` pro EREW, CREW, common CRCW.
   - Cena optimálního algoritmu pro zjištění, zda se v posloupnosti nachází alespoň dva rozdílné prvky.
   - Časová složitost optimálního algoritmu pro průměrnou hodnotu posloupnosti.
2. Granularity paralelismu, 9 b: uvést úrovně a stručně je popsat z hlediska paralelizace.
3. Odd-even transposition sort, 9 b: uvést algoritmicky a odvodit cenu.
4. Maekawův algoritmus, 9 b: k čemu slouží kvóra, co musí splňovat, jak se určují; ilustrovat obrázkem.
5. Pi-kalkul, 9 b: redukovat všemi možnými způsoby a uvést pozorování.
6. Eulerův tah, 9 b: pro zadaný graf `G=(V,E)` s vrcholy `v1..v6` a hranami `e1..e14` demonstrovat paralelní výpočet Eulerova tahu.
7. Carry-look-ahead parallel binary adder, 9 b: provést součet `90 + 139` a demonstrovat kroky.
8. MPI, 10 b: paralelní C++/MPI algoritmus s logaritmickou časovou složitostí pro součet čísel posloupnosti, která jsou větší než její průměr.

## Rozdíly / doplnění ze student_doc

- Termín je jen ve studentském dokumentu.
- Skupina A je ve zdroji přepsaná nejdoslovněji.

## Poznámky k nejistotám

- Některá řešení pod zadáním obsahují studentskou diskusi a nemusí být plně ověřená.
