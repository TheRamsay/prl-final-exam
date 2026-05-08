# 2018/2019 - student doc digest

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2018/2019 |
| Zdroj | studentský dokument |
| Stav | první destilace |
| Auditovatelný extract | [[knowledge/sources/student-doc/2018-2019-extract]] |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc only` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2018-2019]] |

## Původní zdroje

- Raw dokument: [[raw/student_doc]]
- Očištěný zdroj: [[knowledge/sources/student-doc/clean]]
- Extract roku: [[knowledge/sources/student-doc/2018-2019-extract]]

## Přehled termínů

### Term 1 - řádný termín - skupina A

Samostatný soubor: [[knowledge/exams/2018-2019/term-1-radny-a]]

1. [[knowledge/topics/pram-tipovacka|PRAM otázky, 6 b]].
   - Cena AND pro EREW/CREW/common CRCW.
   - Cena zjištění, zda se nachází alespoň dva rozdílné prvky.
   - Časová složitost výpočtu průměrné hodnoty.
2. Granularity paralelismu, 9 b.
   - Uvnitř instrukcí, mezi instrukcemi, mezi příkazy, mezi bloky procesů/vlákny, mezi procesy.
3. [[knowledge/topics/razeni-prefix|Odd-even transposition sort]] - algoritmus a cena.
4. [[knowledge/topics/distribuovane-algoritmy|Maekawa]] - kvóra, požadavky a určení pro množinu procesů.
5. [[knowledge/topics/pi-kalkul|Pi-kalkul]] - redukovat všemi možnými způsoby a uvést pozorování.
6. [[knowledge/topics/euler-tour-suffix-sums|Eulerův tah]] - pro konkrétní graf s vrcholy `v1..v6` a hranami `e1..e14` demonstrovat paralelní výpočet Eulerova tahu.
7. [[knowledge/topics/cla|CLA]] - součet `90 + 139`.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - součet čísel větších než průměr, k dispozici zjednodušené `MPI_Bcast` a `MPI_Reduce`.

### Term 1 - řádný termín - skupina B

Samostatný soubor: [[knowledge/exams/2018-2019/term-1-radny-b]]

1. [[knowledge/topics/pram-tipovacka|PRAM otázky]] - cena OR, cena reverzace posloupnosti, časová složitost součinu prvků.
2. [[knowledge/topics/pram-tipovacka|PRAM architektura]] - popis a obrázek.
   - Zdroj uvádí synchronní model, sdílenou paměť, procesory RAM a varianty EREW/CREW/CRCW.
3. [[knowledge/topics/parallel-splitting-select|Parallel splitting]] - popis a menší příklad rozdělení do `L/E/G`.
4. [[knowledge/topics/distribuovane-algoritmy|Suzuki]] - princip tokenového algoritmu, příklad se 4 procesory.
5. [[knowledge/topics/pi-kalkul|Pi-kalkul]] - redukce a pozorování.
6. [[knowledge/topics/distribuovane-algoritmy|Random mating]] - demonstrovat na 8 prvcích, obě fáze, skončit do 4 kroků.
7. [[knowledge/topics/cla|CLA]] - `77 + 125`.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - počet prvků, které jsou maximy nebo minimy.

### Term 1 - řádný termín - skupina C

Samostatný soubor: [[knowledge/exams/2018-2019/term-1-radny-c]]

1. [[knowledge/topics/pram-tipovacka|PRAM otázky]].
   - Časová složitost XOR.
   - Cena kontroly monotónnosti.
   - Časová složitost součtu absolutních hodnot.
2. [[knowledge/topics/architektury|Zřetězené procesory]] - popis a nákres.
3. [[knowledge/topics/razeni-prefix|Odd-even merge]] - obecná schéma a síť 4x4 pomocí CE bloků.
4. [[knowledge/topics/distribuovane-algoritmy|Marzullo]] - popis a příklad.
5. [[knowledge/topics/pi-kalkul|Pi-kalkul]] - redukce a pozorování.
6. [[knowledge/topics/razeni-prefix|Prescan]] - výsledek po prvním kroku a po skončení up-sweep, potom po prvním kroku a po skončení down-sweep.
7. [[knowledge/topics/cla|CLA]] - `77 + 125`.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - počet prvků beze zbytku dělitelných prvním prvkem, jen `MPI_Bcast` a `MPI_Reduce`, logaritmická časová složitost.

### Term 2 - 1. opravný termín

Samostatný soubor: [[knowledge/exams/2018-2019/term-2-prvni-opravny]]

Zdroj odkazuje na druhý dokument mimo aktuální raw materiály. V tomto vaultu je zatím jen odkaz a žádná detailní destilace.

## Využitelné řešicí poznámky

- Rok 2018/2019 má nejvíc doslovných zadání, hlavně skupina A.
- Silné doplnění pro Maekawu, Suzuki, parallel splitting, granularity paralelismu, PRAM architekturu a detailní MPI formulace.
