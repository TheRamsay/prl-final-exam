# 2025/2026 - řádný termín - cvičná predikce C

## Metadata

| Pole | Hodnota |
|---|---|
| Typ | cvičné zadání |
| Cíl | těžší predikce pro řádný termín 2025/2026 |
| Doporučený limit | 150 minut |
| Body | 70 |
| Jistota | nižší konkrétně, vysoká pro pokrytí rizikových témat |

## Témata

- [[knowledge/topics/pram-tipovacka|PRAM tipovačka]]
- [[knowledge/topics/architektury|Dataflow / redukční počítač]]
- [[knowledge/topics/mutual-exclusion|Bounded test-and-set]]
- [[knowledge/topics/euler-tour-suffix-sums|Euler tour a počet potomků]]
- [[knowledge/topics/distribuovane-algoritmy|Random mating]]
- [[knowledge/topics/razeni-prefix|Pipeline Merge Sort]]
- [[knowledge/topics/cla|Carry-look-ahead]]
- [[knowledge/topics/mpi-reduce-bcast|MPI Reduce/Bcast]]

## Proč tahle varianta

Tohle je horší, ale pořád realistická varianta: místo Pi-kalkulu/OCCAM dává CLA, místo běžné synchronizace aktivní čekání a místo Maekawy/Ricarta simulační Random mating. Hodí se po zvládnutí variant A a B.

## Zadání

1. **PRAM tipovačka, 6 b.** Pro EREW, CREW a common CRCW určete čas a cenu optimálního algoritmu pro:
   - výpočet NAND všech prvků bitové posloupnosti;
   - zjištění, zda je posloupnost monotónně neklesající;
   - spočítání počtu sudých prvků v posloupnosti `n` čísel.

2. **Dataflow a redukční počítač, 9 b.** Popište princip dataflow architektury a redukčního počítače. Vysvětlete, kdy se může výpočet spustit, jak se reprezentují závislosti a jaký je rozdíl proti klasickému řízení programovým čítačem. Připojte jednoduchý graf výrazu `(a+b)*(c+d)`.

3. **Bounded test-and-set, 9 b.** Vysvětlete atomickou instrukci test-and-set a napište základní řešení kritické sekce. Poté vysvětlete, proč základní řešení nemusí splňovat bounded waiting, a navrhněte úpravu s čekacími příznaky pro `n` procesů.

4. **Euler tour + počet potomků, 9 b.** Popište, jak pomocí Euler tour a prefix/suffix sum spočítat počet potomků každého vrcholu zakořeněného stromu. Vysvětlete, jak poznáte první vstup a poslední opuštění vrcholu a jak z hodnot odvodíte velikost podstromu.

5. **Random mating, 10 b.** Máte 8 uzlů v seznamu `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8`. Demonstrujte jumping phase algoritmu Random mating tak, aby skončila nejpozději do 4 iterací. Pro každou iteraci zapište zvolené značky `F/M`, provedené skoky a stav seznamu. Nezapomeňte popsat reconstruction phase.

6. **Pipeline Merge Sort, 9 b.** Uvažujte Pipeline Merge Sort pro vstup

```text
6, 1, 8, 3, 7, 2, 5, 4
```

zpracovávaný zprava. Hodnota `4` je na začátku kroku 1 na vstupu `P1`. Procesy vždy posílají menší hodnotu jako první. Zapište hodnoty na vstupech/výstupech procesů po 10. kroku a stručně popište, jak jste simulovali bufferování.

7. **Carry-look-ahead, 9 b.** Algoritmem Carry-look-ahead Parallel Binary Adder proveďte součet `86 + 173`. Ukažte binární zápis, pro každý bit určete `generate/propagate/stop`, prefixový výpočet carry a výsledný součet. Uveďte paralelní hloubku.

8. **MPI, 10 b.** Každý proces má hodnotu `value`. Pomocí `MPI_Reduce` a `MPI_Bcast` napište algoritmus, který normalizuje hodnoty do intervalu `<0, 1>` podle vzorce `(value - min) / (max - min)` a každému procesu uloží výsledek do proměnné `normalized`. Pokud jsou všechny hodnoty stejné, nastavte `normalized = 0`.

## Kontrola po dopsání

- Dataflow/redukční počítač: [[knowledge/topics/architektury]]
- TAS: [[knowledge/topics/mutual-exclusion]]
- Random mating: [[knowledge/topics/distribuovane-algoritmy]]
- Pipeline Merge Sort: [[knowledge/visuals/pipeline-merge-sort]]
- CLA: [[knowledge/topics/cla]]
- MPI normalizace: [[knowledge/topics/mpi-reduce-bcast]]
