# Řazení, prescan, prefix/suffix

## Pipeline Merge Sort

Typická zkoušková úloha chce stav po `N` krocích. Důležité je držet přesnou simulaci:

1. Procesory jsou zapojené do pipeline.
2. Každý proces drží lokální fronty/buffery podle fáze merge.
3. V každém kroku se posune nejvýše jedna relevantní hodnota podle pravidel algoritmu.
4. Neztratit stabilitu a pořadí proudů.

## Enumeration Sort

Pro každý prvek spočítat, kolik prvků je menších, případně menších nebo stejných s tie-breakem podle indexu. Výsledná pozice prvku je jeho rank.

Šablona:

```text
rank[i] = počet j takových, že A[j] < A[i]
          + počet j < i takových, že A[j] == A[i]
B[rank[i]] = A[i]
```

## Prescan / prefix sum

Pro pole velikosti mocniny dvou:

- Up-sweep: buduje redukční strom, v kořeni je celkový součet.
- Down-sweep: kořen se nastaví na neutrální prvek, hodnoty se propagují dolů a vznikne exclusive scan.

U zkoušky často chtějí stavy po prvním a posledním kroku obou fází.

## Odd-even transposition sort

- Střídají se fáze porovnání dvojic `(0,1),(2,3),...` a `(1,2),(3,4),...`.
- Po `n` fázích je seřazeno.
- Paralelní čas `O(n)`, práce `O(n^2)`.

## Chyby

- Zaměnit inclusive a exclusive prescan.
- U Enumeration Sort nezvládnout duplicity.
- U PMS simulovat více posunů v jednom taktu, než dovoluje zadání.

