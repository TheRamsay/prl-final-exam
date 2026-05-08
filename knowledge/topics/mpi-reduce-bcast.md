# MPI: Reduce a Bcast

## Co umět

- V každém procesu je typicky `rank`, `numproc`, `value`.
- `Reduce` umí agregovat na root: `SUM`, `MIN`, `MAX`, případně vlastní dvojice.
- `Bcast` pošle výsledek z root všem.
- Když výsledek tiskne každý proces, root agreguje, broadcastne a každý si spočítá lokální výraz.
- Když tiskne jen root, broadcast často není nutný, pokud root má vše potřebné.

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

## Složitost

- Stromová implementace `Reduce` a `Bcast`: `O(log p)` komunikačních kroků.
- Sekvenční lokální práce obvykle `O(1)`.

## Chyby

- Zapomenutý `Bcast` průměru/min/max, když hodnotu potřebují i neroot procesy.
- Integer division u průměru.
- Nejasné, zda se druhé minimum počítá jako druhá různá hodnota nebo druhý prvek včetně duplicit.
- Dělení nulou u `max % min`.

