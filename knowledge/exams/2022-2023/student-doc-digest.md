# 2022/2023 - student doc digest

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2022/2023 |
| Zdroj | studentský dokument |
| Stav | první destilace |
| Auditovatelný extract | [[knowledge/sources/student-doc/2022-2023-extract]] |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | mix `student_doc doplňuje raw` a `student_doc only` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2022-2023]] |

## Původní zdroje

- Raw dokument: [[raw/student_doc]]
- Očištěný zdroj: [[knowledge/sources/student-doc/clean]]
- Extract roku: [[knowledge/sources/student-doc/2022-2023-extract]]

## Přehled termínů

### Term 0 - předtermín

Samostatný soubor: [[knowledge/exams/2022-2023/term-0-pretermin]]

1. [[knowledge/topics/pram-tipovacka|PRAM sportka]] - tipování složitosti.
   - Poznámka ze zdroje: hledání prvku v unikátní posloupnosti má cenu `n`; u EREW je potřeba řešit distribuci hledané hodnoty, CREW zvládá čtení konstantně.
   - U počtu prvků větších než `x` zdroj upozorňuje, že samotné nalezení indexu nestačí; počet prvků typicky vyžaduje redukci/součet.
2. [[knowledge/topics/broadcast-fifo-kauzalita|FIFO broadcast a relace kauzality]] - napsat kód FIFO broadcastu a popsat relaci kauzality.
3. [[knowledge/topics/pi-kalkul|Pi-kalkul]].
4. [[knowledge/topics/euler-tour-suffix-sums|Euler]].
5. [[knowledge/topics/architektury|Redukční počítač]].
6. [[knowledge/topics/broadcast-fifo-kauzalita|Synchronizovatelnost procesů]].
7. [[knowledge/topics/mutual-exclusion|Aktivní čekání: test-and-set a swap]].
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - zjistit `max % min == 0`.

### Term 1 - řádný termín - skupina A

1. [[knowledge/topics/pram-tipovacka|PRAM Sportka]].
2. [[knowledge/topics/architektury|Propojovací síť]] - co to je, nevýhody, nakreslit.
3. [[knowledge/topics/euler-tour-suffix-sums|Výpočet levelu vrcholu]] se složitostí.
4. [[knowledge/topics/synchronizace-monitory-semafory|Monitor]] - hlavně `wait()` a `signal()` + obrázek.
5. [[knowledge/topics/pi-kalkul|Pi-kalkul]] s pluskem a privátní proměnnou.
   - Zdroj obsahuje pokus o řešení a odkazy na nástroje `stargazer` a `rug-picalc`.
   - Pozor: řešení je ve zdroji označené jako nejisté.
6. [[knowledge/topics/razeni-prefix|Pipeline Merge Sort]].
7. Hirschberg-Sinclair - určení master uzlu.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - zjistit, která půlka pole má větší počet záporných hodnot.

### Term 1 - řádný termín - skupina B

Samostatný soubor: [[knowledge/exams/2022-2023/term-1-radny-b]]

1. [[knowledge/topics/pram-tipovacka|PRAM Synotip]].
2. [[knowledge/topics/architektury|Xeon Phi]].
3. [[knowledge/topics/mutual-exclusion|Bounded test-and-set]].
4. [[knowledge/topics/razeni-prefix|Enumeration Sort]].
5. [[knowledge/topics/pi-kalkul|Pi-kalkul]].
6. [[knowledge/topics/distribuovane-algoritmy|Marzullův algoritmus]].
7. [[knowledge/topics/distribuovane-algoritmy|Kvórum]].
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - spočítat poměr lichých a sudých v posloupnosti.

### Term 1 - řádný termín - skupina C

Samostatný soubor: [[knowledge/exams/2022-2023/term-1-radny-c]]

1. [[knowledge/topics/pram-tipovacka|PRAM Sportka]].
2. Pět úrovní granularity paralelismu.
3. [[knowledge/topics/euler-tour-suffix-sums|Euler]].
4. [[knowledge/topics/synchronizace-monitory-semafory|Semafory + monitor ze semaforů]].
5. [[knowledge/topics/pi-kalkul|Pi-kalkul]] s pluskem a privátní proměnnou.
6. [[knowledge/topics/distribuovane-algoritmy|Random mating]] - několik kroků podle obrázku.
7. Algoritmus čtyř čítačů.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - převést čísla z intervalu `1-5` na interval `0-1`, netřeba vypisovat.

### Term 2 - 1. opravný termín

1. [[knowledge/topics/pram-tipovacka|Tipování složitosti]].
2. [[knowledge/topics/razeni-prefix|Odd-even transposition sort]] - algoritmus, analýza, cena.
3. [[knowledge/topics/parallel-splitting-select|Paralelní SELECT]] - princip a příklad.
4. [[knowledge/topics/distribuovane-algoritmy|Marzullův algoritmus]] - princip a aplikace na intervaly z obrázku.
5. [[knowledge/topics/pi-kalkul|Pi-kalkul]] - najít 3 možné redukce.
6. [[knowledge/topics/cla|CLA]] - příklad `120 + 99`.
7. [[knowledge/topics/distribuovane-algoritmy|Čtyři čítači]] - detekce ukončení; uvést příklad, kdy k detekci dojde a kdy nedojde.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - zjistit, která část sekvence je menší/větší/stejně velká jako průměr.

### Term 3 - 2. opravný termín

Samostatný soubor: [[knowledge/exams/2022-2023/term-3-druhy-opravny]]

1. [[knowledge/topics/pram-tipovacka|PRAM tipování]].
2. [[knowledge/topics/broadcast-fifo-kauzalita|Kauzální odesílání/přijímání zprávy a relace kauzality]].
3. [[knowledge/topics/pram-tipovacka|PRAM architektura]] - popsat a nakreslit.
4. [[knowledge/topics/linda-ada|ADA]] - popsat a uvést konkrétní příkazy.
5. [[knowledge/topics/pi-kalkul|Pi-kalkul]] - 3 redukce.
6. [[knowledge/topics/razeni-prefix|Upsweep/down-sweep]] příklad.
7. [[knowledge/topics/distribuovane-algoritmy|Čtyři čítače]], za 10 bodů.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - v logaritmickém čase zjistit, zda má posloupnost 3 a více různých hodnot.

## Největší přínos oproti raw `term_*.md`

- Přidává 2022/2023 předtermín, řádný termín skupiny A/B/C a 2. opravný termín.
- U některých příkladů obsahuje náznaky řešení nebo varování, že řešení ve zdroji je nejisté.
- Potvrzuje opakování vzoru: PRAM + komunikace/synchronizace + Euler/prefix/sort + jazyk/pi-kalkul + MPI.
