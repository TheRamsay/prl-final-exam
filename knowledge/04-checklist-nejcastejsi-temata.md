# Checklist nejčastějších témat

Praktický checklist pro opakování. Každý blok má tři úrovně: **minimum** pro rychlé body, **standard** pro běžnou zkouškovou variantu a **jistota** pro méně příjemné obměny.

## A0: udělat bez vyjednávání

### [[topics/mpi-reduce-bcast|MPI Reduce/Bcast]]

**Evidence:** `common_latest` ~35, starší četnosti 25x, 28 odkazů v termínových souborech.

- [ ] Minimum: umím napsat `Reduce SUM/MIN/MAX` na root.
- [ ] Minimum: vím, kdy je potřeba `Bcast` a kdy stačí výsledek na rootu.
- [ ] Standard: umím spočítat průměr a potom vybrat hodnoty podle podmínky `value > avg`.
- [ ] Standard: umím `max % min == 0`, počet max/min, součet max/min.
- [ ] Standard: umím normalizaci hodnot na rozsah `0..1` nebo `1..5`.
- [ ] Jistota: umím druhé minimum/maximum přes redukci dvojice.
- [ ] Jistota: umím vysvětlit čas `O(log p)` pro stromové `Reduce/Bcast`.

Typické termíny: [[exams/2025-2026/term-0-pretermin-a]], [[exams/2024-2025/term-0-pretermin]], [[exams/2023-2024/term-1-radny-b]], [[exams/2022-2023/term-1-radny-c]], [[exams/2021-2022/term-3-druhy-opravny]], [[exams/2019-2020/term-2-prvni-opravny]].

### [[topics/pram-tipovacka|PRAM tipovačka]]

**Evidence:** `common_latest` ~27, starší četnosti 25x, 30 odkazů v termínových souborech.

- [ ] Minimum: znám rozdíl EREW, CREW, common CRCW.
- [ ] Minimum: u každé odpovědi uvádím čas `t(n)` i cenu `c(n)`.
- [ ] Standard: umím AND/OR přes stromovou redukci i common zápis.
- [ ] Standard: umím XOR/NAND, monotónnost, stejné prvky, počet nul/sudých.
- [ ] Standard: umím min/max a součet jako redukční úlohy.
- [ ] Jistota: rozliším časovou složitost a cenu při `n` procesorech.
- [ ] Jistota: poznám, kdy common CRCW nejde použít kvůli různým zapisovaným hodnotám.

Typické termíny: [[exams/2025-2026/term-0-pretermin-a]], [[exams/2024-2025/term-0-pretermin]], [[exams/2023-2024/term-1-radny-c]], [[exams/2022-2023/term-0-pretermin]], [[exams/2021-2022/term-2-prvni-opravny-b]], [[exams/2018-2019/term-1-radny-c]].

### [[topics/broadcast-fifo-kauzalita|Broadcast/FIFO/kauzalita]]

**Evidence:** `common_latest` ~26, starší četnosti 10x plus 6x async->sync/koruna, 16 odkazů v termínových souborech.

- [ ] Minimum: umím definovat FIFO broadcast a kauzální broadcast.
- [ ] Minimum: umím napsat relaci kauzality `->`.
- [ ] Standard: umím poznat porušení FIFO, kauzality a atomicity z diagramu.
- [ ] Standard: umím popsat ABCAST / total order broadcast.
- [ ] Standard: umím princip synchronizovatelnosti a koruny.
- [ ] Jistota: umím stručně popsat převod asynchronního systému na synchronní, pokud je synchronizovatelný.

Typické termíny: [[exams/2025-2026/term-0-pretermin-a]], [[exams/2024-2025/term-0-pretermin]], [[exams/2023-2024/term-2-prvni-opravny]], [[exams/2022-2023/term-0-pretermin]], [[exams/2021-2022/term-2-prvni-opravny-a]], [[exams/2020-2021/term-3-druhy-opravny]].

## A1: vysoká návratnost po A0

### [[topics/razeni-prefix|Řazení, prescan, prefix]]

**Evidence:** `common_latest` ~25, starší četnosti 5x Pipeline Merge Sort, 4x Prescan, 4x Enumeration Sort, 3x Odd-even, 20 odkazů v termínových souborech.

- [ ] Minimum: rozliším Pipeline Merge Sort, Enumeration Sort, Prescan a Odd-even.
- [ ] Standard: umím tabulkově simulovat stav po `N` krocích.
- [ ] Standard: u Enumeration Sort umím duplicity přes tie-break indexem.
- [ ] Standard: u Prescanu rozliším up-sweep, down-sweep, inclusive/exclusive scan.
- [ ] Jistota: umím napsat čas a práci pro typický paralelní scan/sort variantu.

Typické termíny: [[exams/2025-2026/term-0-pretermin-a]], [[exams/2024-2025/term-0-pretermin]], [[exams/2023-2024/term-1-radny-b]], [[exams/2022-2023/term-3-druhy-opravny]], [[exams/2021-2022/term-1-radny-a]], [[exams/2018-2019/term-1-radny-c]].

### [[topics/euler-tour-suffix-sums|Euler tour + suffix sums]]

**Evidence:** `common_latest` ~15, starší četnosti 12x, 16 odkazů v termínových souborech.

- [ ] Minimum: umím z neorientované hrany udělat dvě orientované hrany.
- [ ] Minimum: vím, co je Etour a následník hrany.
- [ ] Standard: umím `level(v)` přes `+1/-1` a suffix/prefix sum.
- [ ] Standard: umím `preorder(v)` přes první vstup do vrcholu.
- [ ] Standard: umím počet potomků/následovníků jako variantu nad Etour.
- [ ] Jistota: umím převést výsledek z hran zpět na hodnoty vrcholů a uvést složitost.

Typické termíny: [[exams/2025-2026/term-0-pretermin-a]], [[exams/2024-2025/term-0-pretermin]], [[exams/2023-2024/term-1-radny-a]], [[exams/2022-2023/term-1-radny-c]], [[exams/2021-2022/term-2-prvni-opravny-a]], [[exams/2018-2019/term-1-radny-a]].

### [[topics/synchronizace-monitory-semafory|Monitory, semafory, readers-writers]]

**Evidence:** `common_latest` ~17, starší četnosti 6x monitor/wait/signal plus 2x producer-consumer, 12 odkazů v termínových souborech.

- [ ] Minimum: umím vysvětlit monitor, `wait`, `signal`.
- [ ] Minimum: umím základní semaforové operace `P` a `V`.
- [ ] Standard: umím readers-writers s prioritou čtenářů nebo bez uváznutí.
- [ ] Standard: umím producer-consumer pseudokód.
- [ ] Jistota: umím monitor implementovaný semafory a popsat, kde vzniká deadlock/starvation.

Typické termíny: [[exams/2025-2026/term-0-pretermin-a]], [[exams/2023-2024/term-1-radny-b]], [[exams/2022-2023/term-1-radny-b]], [[exams/2021-2022/term-1-radny-b]], [[exams/2020-2021/term-2-prvni-opravny]], [[exams/2019-2020/term-1-radny-a]].

### [[topics/architektury|Architektury]]

**Evidence:** `common_latest` ~26, starší četnosti VLIW 4x, zřetězení/MISD 4x, Xeon Phi 3x, DataFlow 2x, PRAM architektura 2x, 10 odkazů v termínových souborech.

- [ ] Minimum: umím VLIW a konflikty v instrukčním slově.
- [ ] Minimum: umím zřetězené procesory/pipeline a základní výhody.
- [ ] Standard: umím SIMD/MIMD, UMA/NUMA, Xeon Phi.
- [ ] Standard: umím Dataflow architekturu.
- [ ] Standard: umím PRAM model a propojovací síť.
- [ ] Jistota: ke každé architektuře mám 3 věty + jednoduchý nákres.

Typické termíny: [[exams/2023-2024/term-1-radny-a]], [[exams/2023-2024/term-1-radny-b]], [[exams/2022-2023/term-1-radny-b]], [[exams/2021-2022/term-2-prvni-opravny-a]], [[exams/2021-2022/term-3-druhy-opravny]], [[exams/2019-2020/term-1-radny-a]].

## B: přidat pro jistotu

### [[topics/distribuovane-algoritmy|Distribuované algoritmy]]

- [ ] Marzullo: intervaly, průniky, nejlepší počet překryvů.
- [ ] Maekawa: kvóra, průnik každých dvou kvór.
- [ ] Suzuki: token, žádosti, fronta.
- [ ] Ricart-Agrawala: timestampy a odpovědi.
- [ ] Dijkstra/Hirschberg-Sinclair/volba lídra: základní princip a složitost.

Typické termíny: [[exams/2025-2026/term-0-pretermin-a]], [[exams/2023-2024/term-1-radny-c]], [[exams/2022-2023/term-1-radny-b]], [[exams/2021-2022/term-3-druhy-opravny]], [[exams/2020-2021/term-2-prvni-opravny]], [[exams/2018-2019/term-1-radny-b]].

### [[topics/pi-kalkul|Pi-kalkul]]

- [ ] Umím najít synchronizující vstup/výstup.
- [ ] Umím provést substituci.
- [ ] Umím zapsat 3-4 různé možné redukce.
- [ ] Umím říct, kdy už výraz nejde redukovat.
- [ ] Umím vypsat pozorování typu `downarrow x`.

Typické termíny: [[exams/2023-2024/term-1-radny-a]], [[exams/2023-2024/term-1-radny-b]], [[exams/2023-2024/term-1-radny-c]], [[exams/2022-2023/term-0-pretermin]], [[exams/2020-2021/term-1-radny-zkratka]], [[exams/2018-2019/term-1-radny-b]].

### [[topics/cla|Carry-look-ahead]]

- [ ] Znám význam `generate`, `propagate`, `stop`.
- [ ] Umím převést dvojici binárních čísel na stavy bitů.
- [ ] Umím provést scan pro carry.
- [ ] Umím dopočítat výsledný součet.

Typické termíny: [[exams/2022-2023/term-1-radny-a-zkratka]], [[exams/2021-2022/term-1-radny-b]], [[exams/2020-2021/term-1-radny-zkratka]], [[exams/2019-2020/term-1-radny-b]], [[exams/2018-2019/term-1-radny-a]].

### [[topics/occam|OCCAM]]

- [ ] Znám `CHAN`, `PAR`, `SEQ`, `ALT`.
- [ ] Umím číst z kanálu a zapisovat do kanálu.
- [ ] Umím pole kanálů a routování na výstup podle hodnoty.
- [ ] Umím buffer/queue s podmíněným příjmem/výdejem.
- [ ] Umím nekonečný proces se stavem.

Typické termíny: [[exams/2025-2026/term-0-pretermin-a]], [[exams/2024-2025/term-0-pretermin]], [[exams/2021-2022/term-2-prvni-opravny-a]], [[exams/2021-2022/term-2-prvni-opravny-b]], [[exams/2019-2020/term-1-radny-a]].

## C: když zbyde čas

### [[topics/mutual-exclusion|Test-and-set, swap, Peterson]]

- [ ] Umím aktivní čekání přes test-and-set.
- [ ] Umím bounded waiting variantu.
- [ ] Umím Petersonův algoritmus pro dva procesy.
- [ ] Umím popsat starvation a deadlock.

### [[topics/parallel-splitting-select|Parallel splitting / SELECT]]

- [ ] Umím rozdělit prvky podle pivotu na `L/E/G`.
- [ ] Umím rozhodnout, ve které části leží k-tý prvek.
- [ ] Umím napsat základní rekurzivní krok.

### [[topics/linda-ada|Linda / ADA]]

- [ ] Znám základní Linda operace nad tuple space.
- [ ] Umím linked-list search/delete/reverse styl úlohy.
- [ ] Znám základní ADA komunikaci podle zadání.

## Závěrečný drill

- [ ] Otevřít [[exams/00-index|archiv termínů]].
- [ ] Projít poslední tři roky: [[exams/2025-2026/00-index]], [[exams/2024-2025/00-index]], [[exams/2023-2024/00-index]].
- [ ] U každé otázky napsat do 10 sekund téma a šablonu řešení.
- [ ] Označit si slabiny v tomhle checklistu.
- [ ] Před zkouškou znovu projet jen nezaškrtnuté body z A0 a A1.
