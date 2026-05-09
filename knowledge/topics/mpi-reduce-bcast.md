# MPI: Reduce a Bcast

## Zkouškový pattern

Každý proces má lokální hodnotu `value` a má se spočítat globální vlastnost v logaritmickém čase pomocí `MPI_Reduce` a případně `MPI_Bcast`. Často se řeší průměr, minimum, maximum, počet prvků splňujících podmínku nebo kombinace sudé/liché části.

## Oficiální slidy

- [[knowledge/sources/slides/mpi#Strana 8|MPI, str. 8]] až [[knowledge/sources/slides/mpi#Strana 14|str. 14]] - inicializace, `MPI_COMM_WORLD`, rank a size.
- [[knowledge/sources/slides/mpi#Strana 24|MPI, str. 24]] - kolektivní komunikace, `MPI_Bcast` a `MPI_Reduce`.
- [[knowledge/sources/slides/mpi#Strana 25|MPI, str. 25]] - standardní redukční operace (`MPI_SUM`, `MPI_MAX`, `MPI_MIN`, ...).
- [[knowledge/sources/slides/mpi#Strana 26|MPI, str. 26]] až [[knowledge/sources/slides/mpi#Strana 29|str. 29]] - příklady reduce pro sumu, maximum a dvě části vstupu.
- [[knowledge/sources/slides/mpi#Strana 44|MPI, str. 44]] až [[knowledge/sources/slides/mpi#Strana 45|str. 45]] - příklad s `MPI_Bcast`.

## Co umět

- V každém procesu je typicky `rank`, `numproc`, `value`.
- `Reduce` agreguje na root: `SUM`, `MIN`, `MAX`, případně vlastní dvojice.
- `Bcast` pošle výsledek z root všem.
- Když výsledek tiskne každý proces, root agreguje, broadcastne a každý si spočítá lokální výraz.
- Když tiskne jen root, broadcast často není nutný.

## Minimální odpověď

1. Urči, které globální hodnoty potřebuješ: `sum`, `avg`, `min`, `max`, počet.
2. Spočítej je přes `MPI_Reduce`.
3. Pokud je potřebují i neroot procesy, pošli je přes `MPI_Bcast`.
4. Lokálně nastav `candidate`.
5. Kandidáty agreguj druhým `MPI_Reduce`.
6. Uveď `O(log p)` komunikačních kroků pro stromovou implementaci.

## Šablona pro průměr

```c
sum = 0;
MPI_Reduce(&value, &sum, 1, MPI_INT, MPI_SUM, root, MPI_COMM_WORLD);
if (rank == root) avg = (double)sum / numproc;
MPI_Bcast(&avg, 1, MPI_DOUBLE, root, MPI_COMM_WORLD);
```

Potom lokálně:

```c
out = value - avg;
printf("%d: %f\n", rank, out);
```

## Typické varianty

- Součet prvků větších než průměr:
  1. `Reduce SUM` pro součet všech hodnot.
  2. `Bcast avg`.
  3. Lokální `candidate = value > avg ? value : 0`.
  4. `Reduce SUM` kandidátů.

- Je maximum dělitelné minimem:
  1. `Reduce MAX`.
  2. `Reduce MIN`.
  3. Root vyhodnotí `max % min == 0`, pozor na `min == 0`.

- Součet prvků rovných minimu nebo maximu:
  1. `Reduce MIN`, `Reduce MAX`.
  2. `Bcast min`, `Bcast max`.
  3. Kandidát podle podmínky.
  4. `Reduce SUM`.

- Druhé minimum:
  - Nejčistší je redukovat dvojici `(min1, min2)`.
  - Lokální stav: `min1 = value`, `min2 = INF`.
  - Kombinace dvou stavů vezme dvě nejmenší různé hodnoty ze čtyř kandidátů.

## Rozhodovací pravidlo

| Zadání | Potřebuje `Bcast`? |
|---|---|
| Root má jen vypsat globální výsledek | většinou ne |
| Každý proces má vypsat výraz závislý na globální hodnotě | ano |
| Potřebuji vybrat lokální kandidáty podle globálního průměru/min/max | ano |
| Dvě nezávislé globální hodnoty, vyhodnocuje root | ne, stačí dva `Reduce` |

## Složitost

- Stromová implementace `Reduce` a `Bcast`: `O(log p)` komunikačních kroků.
- Sekvenční lokální práce obvykle `O(1)`.

## Mini-drill

1. Napiš postup pro součet hodnot větších než průměr.
2. Kdy je potřeba broadcastovat průměr?
3. Jak bys řešil `max % min == 0` a na co si dát pozor?
4. Jak reprezentovat stav pro druhé minimum?

## Vyřešené příklady z termínů

### `max % min == 0`

Zdroj: [[knowledge/exams/2025-2026/term-0-pretermin-a]]

Zadání: v logaritmickém čase určit, zda je maximum v posloupnosti přirozených čísel beze zbytku dělitelné minimem.

Řešení:

```c
int root = 0;
int mn, mx;
MPI_Reduce(&value, &mn, 1, MPI_INT, MPI_MIN, root, MPI_COMM_WORLD);
MPI_Reduce(&value, &mx, 1, MPI_INT, MPI_MAX, root, MPI_COMM_WORLD);

if (rank == root) {
  bool ok = (mn != 0) && (mx % mn == 0);
  printf("%s\n", ok ? "Ano" : "Ne");
}
```

Není potřeba `Bcast`, pokud výsledek tiskne jen root. Komunikační složitost je `O(log p)`.

### `value - average(values)`

Zdroj: [[knowledge/exams/2023-2024/term-0-pretermin]]

Zadání: každý proces má vypsat `rank: value - average(values)`.

Řešení:

```c
int root = 0;
int sum = 0;
double avg = 0.0;
MPI_Reduce(&value, &sum, 1, MPI_INT, MPI_SUM, root, MPI_COMM_WORLD);
if (rank == root) avg = (double)sum / numproc;
MPI_Bcast(&avg, 1, MPI_DOUBLE, root, MPI_COMM_WORLD);

double out = value - avg;
printf("%d: %f\n", rank, out);
```

`Bcast` je nutný, protože průměr potřebují všechny procesy.

### Součet prvků větších než průměr

Zdroj: [[knowledge/exams/2023-2024/term-1-radny-b]]

Řešení:

1. `Reduce SUM` spočítá globální součet.
2. Root spočítá `avg`.
3. `Bcast avg`.
4. Každý proces nastaví `candidate = value > avg ? value : 0`.
5. `Reduce SUM` nad `candidate`.

Výsledek tiskne root. Celkově několik kolektivních operací, každá `O(log p)`.

## Kde se to objevuje

Podle sjednocených termínových souborů v archivu:

- [[knowledge/exams/2025-2026/term-0-pretermin-a]]
- [[knowledge/exams/2024-2025/term-0-pretermin]]
- [[knowledge/exams/2024-2025/term-2-prvni-opravny]]
- [[knowledge/exams/2024-2025/term-0-pretermin-b]]
- [[knowledge/exams/2023-2024/term-3-druhy-opravny]]
- [[knowledge/exams/2023-2024/term-2-prvni-opravny]]
- [[knowledge/exams/2023-2024/term-1-radny-c]]
- [[knowledge/exams/2023-2024/term-1-radny-b]]
- [[knowledge/exams/2023-2024/term-1-radny-a]]
- [[knowledge/exams/2023-2024/term-0-pretermin]]
- [[knowledge/exams/2022-2023/term-3-druhy-opravny]]
- [[knowledge/exams/2022-2023/term-2-prvni-opravny]]
- [[knowledge/exams/2022-2023/term-1-radny-c]]
- [[knowledge/exams/2022-2023/term-1-radny-b]]
- [[knowledge/exams/2022-2023/term-1-radny-a-zkratka]]
- [[knowledge/exams/2022-2023/term-0-pretermin]]
- [[knowledge/exams/2021-2022/term-3-druhy-opravny]]
- [[knowledge/exams/2021-2022/term-2-prvni-opravny-b]]
- [[knowledge/exams/2021-2022/term-2-prvni-opravny-a]]
- [[knowledge/exams/2021-2022/term-1-radny-c]]
- [[knowledge/exams/2021-2022/term-1-radny-b]]
- [[knowledge/exams/2021-2022/term-1-radny-a]]
- [[knowledge/exams/2020-2021/term-3-druhy-opravny]]
- [[knowledge/exams/2020-2021/term-2-prvni-opravny]]
- [[knowledge/exams/2020-2021/term-1-radny-zkratka]]
- [[knowledge/exams/2019-2020/term-2-prvni-opravny]]
- [[knowledge/exams/2019-2020/term-1-radny-b]]
- [[knowledge/exams/2019-2020/term-1-radny-a]]
- [[knowledge/exams/2018-2019/term-1-radny-c]]
- [[knowledge/exams/2018-2019/term-1-radny-b]]
- [[knowledge/exams/2018-2019/term-1-radny-a]]

## Chyby

- Zapomenutý `Bcast` průměru/min/max, když hodnotu potřebují i neroot procesy.
- Integer division u průměru.
- Nejasné, zda se druhé minimum počítá jako druhá různá hodnota nebo druhý prvek včetně duplicit.
- Dělení nulou u `max % min`.
