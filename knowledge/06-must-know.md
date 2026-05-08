# Must-know tahák

Tenhle soubor je minimum, které chceš umět napsat z hlavy. Není to náhrada za topic stránky; je to rychlý seznam odpovědních koster s nejlepším ROI.

## A0: první priorita

### [[knowledge/topics/mpi-reduce-bcast|MPI Reduce/Bcast]]

**Kdy poznat:** každý proces má `value`, `rank`, `numprocs` a zadání chce globální součet, minimum, maximum, průměr nebo filtr podle globální hodnoty.

**Kostra odpovědi:**

1. Přes `MPI_Reduce` spočítat globální hodnotu na rootu.
2. Pokud ji potřebují všechny procesy, poslat ji přes `MPI_Bcast`.
3. Lokálně spočítat kandidát.
4. Kandidáty znovu agregovat přes `MPI_Reduce`.
5. Uvést stromovou složitost `O(log p)`.

**Pozor:** `Bcast` není potřeba, když výsledek vyhodnocuje a tiskne jen root. U průměru pozor na integer division, u `max % min` na `min == 0`.

### [[knowledge/topics/pram-tipovacka|PRAM tipovačka]]

**Kdy poznat:** první otázka s EREW/CREW/common CRCW a výběrem času/ceny pro AND/OR/XOR/NAND, min/max, monotónnost, nuly nebo počet.

**Kostra odpovědi:**

- Nezávislá operace nad každým prvkem: čas `O(1)` při `n` procesorech.
- Redukce typu AND/OR/min/max na EREW/CREW: typicky strom `O(log n)`.
- Common CRCW pomůže jen tam, kde více procesorů zapisuje stejnou hodnotu.
- Cena = čas krát počet procesorů; u stromu s `n` procesory typicky `O(n log n)`, u optimalizované redukce s ubíráním procesorů `O(n)`.

**Pozor:** nemíchat čas a cenu. U CRCW vždy říct, jaký typ kolize zápisu je povolený.

### [[knowledge/topics/broadcast-fifo-kauzalita|Broadcast/FIFO/kauzalita]]

**Kdy poznat:** zadání chce FIFO broadcast, causal broadcast, kauzální relaci, porušení FIFO/kauzality/atomicity nebo synchronizovatelnost.

**Kostra odpovědi:**

- FIFO: zprávy od stejného odesílatele se doručují ve stejném pořadí, v jakém byly vyslány.
- Kauzalita: pokud `m1 -> m2`, každý proces musí doručit `m1` před `m2`.
- `->` vznikne lokálním pořadím událostí, send/receive vazbou a tranzitivitou.
- Causal broadcast se typicky hlídá vektorovými hodinami nebo závislostmi ve zprávě.
- Atomic broadcast řeší shodné pořadí doručení u všech procesů.

**Pozor:** FIFO neřeší pořadí zpráv od různých odesílatelů. Kauzalita je silnější než FIFO pro závislé události, ale nerovná se total order.

## A1: druhá priorita

### [[knowledge/topics/razeni-prefix|Řazení, prescan, prefix]]

**Kdy poznat:** Pipeline Merge Sort, Enumeration Sort, Prescan, Odd-even transposition/merge, simulace po konkrétním počtu kroků.

**Kostra odpovědi:**

- U simulací vždy kreslit tabulku kroků a procesorů.
- Enumeration Sort: pro každý prvek spočítat rank podle počtu menších prvků; duplicitám dát stabilní pravidlo.
- Prescan: upsweep spočítá součty segmentů, downsweep rozdistribuuje prefixy.
- Pipeline Merge Sort: hodnoty jdou potrubím, procesy lokálně porovnávají a posílají dál podle pravidla.

**Pozor:** nejčastější chyba je posun o jeden krok nebo nejasné pravidlo pro duplicity.

### [[knowledge/topics/euler-tour-suffix-sums|Euler tour + suffix sums]]

**Kdy poznat:** strom, orientované hrany dopředu/zpět, `Etour`, `SuffixS`, `preorder(v)`, `level(v)`, počet potomků.

**Kostra odpovědi:**

- Nahradit každou hranu dvojicí orientovaných hran.
- Sestavit Euler tour jako seznam hran.
- Dopředným a zpětným hranám přiřadit váhy podle cílové funkce.
- Přes prefix/suffix sums spočítat hodnotu pro hrany a převést ji na vrcholy.
- Složitost typicky `O(log n)` čas při paralelním scan/prescan.

**Pozor:** u `level(v)` se typicky dopředná hrana počítá jako `+1`, zpětná jako `-1`, ale záleží na použitém prefixu/suffixu a na tom, na které hraně hodnotu čteš.

### [[knowledge/topics/synchronizace-monitory-semafory|Monitory a semafory]]

**Kdy poznat:** `wait`, `signal`, monitor, semafor, readers-writers, producer-consumer.

**Kostra odpovědi:**

- Monitor zapouzdřuje sdílená data a procedury; uvnitř monitoru je aktivní nejvýše jeden proces.
- `wait(c)` uvolní monitor a uspává proces na podmínce `c`.
- `signal(c)` probudí jeden proces čekající na `c`.
- Semafor má atomické operace `P/down/wait` a `V/up/signal`.
- Při pseudokódu vždy ukázat, kdo chrání kritickou sekci a kde se mění čítače/stav.

**Pozor:** u monitoru nezapomenout, že `wait` uvolňuje monitor. U semaforu nezamknout cestu, kde se dá skončit bez `V`.

### [[knowledge/topics/architektury|Architektury]]

**Kdy poznat:** VLIW, zřetězené procesory, MISD, SIMD/MIMD, dataflow, Xeon Phi, PRAM, propojovací sítě.

**Kostra odpovědi:**

- Definovat princip jednou větou.
- Nakreslit tok instrukcí/dat nebo pipeline.
- Uvést, co se paralelizuje.
- Uvést výhodu a limitaci.

**Pozor:** u MISD/zřetězeného zpracování rozlišit více jednotek nad jedním proudem dat vs více datových proudů.

## B: pravidelné doplňky

### [[knowledge/topics/distribuovane-algoritmy|Distribuované algoritmy]]

Umět aspoň rozpoznat: Marzullo pro intervaly hodin, Maekawa/Suzuki/Ricart-Agrawala pro vzájemné vyloučení, Dijkstra/Hirschberg-Sinclair pro volbu v kruhu, volbu lídra podle priorit a epoch.

### [[knowledge/topics/pi-kalkul|Pi-kalkul]]

U redukce hledat komplementární vstup/výstup na stejném kanálu, provést substituci jména a vypsat možné koncové výrazy. Pozor na rozsah vázaných jmen.

### [[knowledge/topics/cla|Carry-look-ahead adder]]

Pro každý bit určit `g` generate, `p` propagate, `s` stop. Carry se počítá prefixově z těchto stavů; pak se vypočte součet bitů s příslušným carry.

### [[knowledge/topics/occam|OCCAM]]

Kanály jsou synchronní komunikace. U procesu ukázat `SEQ`, `PAR`, čtení `?`, zápis `!`, pole kanálů a případně `ALT`. Nekonečný filtr/buffer se píše jako cyklus nad čtením a zapisováním.

## Jak to použít

1. Projdi A0 a zkus každé téma vysvětlit do 90 sekund.
2. Otevři [[knowledge/exams/00-index|minulé termíny]] a u každé otázky si najdi její mapování na téma.
3. Když nevíš detail, jdi přes odkaz do topicu a vrať se zpět do termínu.
4. Na konci si dej jeden [[knowledge/practice/00-index|cvičný test]] bez koukání.

## Navazující stránky

- [[knowledge/01-roi-plan|ROI plán učení]]
- [[knowledge/04-checklist-nejcastejsi-temata|Checklist nejčastějších témat]]
- [[knowledge/topics/00-index|Topic index]]
- [[knowledge/exams/00-index|Minulé termíny]]
