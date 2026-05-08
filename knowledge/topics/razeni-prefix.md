# Řazení, prescan, prefix/suffix

## Zkouškový pattern

Většina úloh chce ruční simulaci po zadaném počtu kroků nebo zapsání mezistavů algoritmu. Nestačí znát název algoritmu; je potřeba umět kreslit tabulku kroků.

## Pipeline Merge Sort

Typická zkoušková úloha chce stav po `N` krocích. Důležité je držet přesnou simulaci:

1. Procesory jsou zapojené do pipeline.
2. Každý proces drží lokální fronty/buffery podle fáze merge.
3. V každém kroku se posune nejvýše jedna relevantní hodnota podle pravidel algoritmu.
4. Neztratit stabilitu a pořadí proudů.

Minimální odpověď: popsat pipeline, pravidlo posunu, ukázat tabulku taktů a uvést výsledný stav po požadovaném kroku.

## Enumeration Sort

Pro každý prvek spočítat, kolik prvků je menších, případně menších nebo stejných s tie-breakem podle indexu. Výsledná pozice prvku je jeho rank.

```text
rank[i] = počet j takových, že A[j] < A[i]
          + počet j < i takových, že A[j] == A[i]
B[rank[i]] = A[i]
```

U duplicit je tie-break podle indexu zásadní; bez něj dva prvky mohou chtít stejnou pozici.

## Prescan / prefix sum

Pro pole velikosti mocniny dvou:

- Up-sweep: buduje redukční strom, v kořeni je celkový součet.
- Down-sweep: kořen se nastaví na neutrální prvek, hodnoty se propagují dolů a vznikne exclusive scan.

U zkoušky často chtějí stavy po prvním a posledním kroku obou fází.

Rozlišuj:

- **exclusive scan**: na pozici `i` je součet prvků před `i`;
- **inclusive scan**: na pozici `i` je součet prvků do `i` včetně.

## Odd-even transposition sort

- Střídají se fáze porovnání dvojic `(0,1),(2,3),...` a `(1,2),(3,4),...`.
- Po `n` fázích je seřazeno.
- Paralelní čas `O(n)`, práce `O(n^2)`.

## Odd-even merge sort

- Jde o třídicí síť z compare-exchange bloků.
- Typická zkouška chce schéma nebo síť pro malý rozměr, často `4x4`.
- U odpovědi stačí princip rekurzivního merge lichých a sudých pozic a výsledné compare-exchange vrstvy.

## Mini-drill

1. Jak vyřeší Enumeration Sort duplicity?
2. Jaký je rozdíl mezi inclusive a exclusive prescan?
3. Co se má zapsat po prvním kroku up-sweep?
4. Proč u Pipeline Merge Sortu nestačí seřadit vstup “od oka”?

## Kde se to objevuje

- [[knowledge/exams/2025-2026/term-0-pretermin-a]]
- [[knowledge/exams/2025-2026/term-0-pretermin-b]]
- [[knowledge/exams/2024-2025/term-0-pretermin]]
- [[knowledge/exams/2023-2024/student-doc-digest]]
- [[knowledge/exams/2022-2023/student-doc-digest]]
- [[knowledge/exams/2018-2019/student-doc-digest]]

## Chyby

- Zaměnit inclusive a exclusive prescan.
- U Enumeration Sort nezvládnout duplicity.
- U Pipeline Merge Sortu simulovat více posunů v jednom taktu, než dovoluje zadání.
- U sorting networks zapomenout, že compare-exchange bloky ve stejné vrstvě běží paralelně.
