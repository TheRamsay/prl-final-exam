# Řazení, prescan, prefix/suffix

## Zkouškový pattern

Většina úloh chce ruční simulaci po zadaném počtu kroků nebo zapsání mezistavů algoritmu. Nestačí znát název algoritmu; je potřeba umět kreslit tabulku kroků.

## Vizualizace a drill stránky

- [[knowledge/visuals/prescan-upsweep-downsweep|Prescan: up-sweep a down-sweep]]
- [[knowledge/visuals/enumeration-sort-ranks|Enumeration Sort: ranky a duplicity]]
- [[knowledge/visuals/pipeline-merge-sort|Pipeline Merge Sort: procesory a tabulka taktů]]
- [[knowledge/visuals/odd-even-network|Odd-even: compare-exchange síť]]

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

## Vyřešené příklady z termínů

### Prescan: mezistavy up-sweep/down-sweep

Zdroj: [[knowledge/exams/2023-2024/term-1-radny-c]]

Zadání: pro posloupnost `3, 15, 2, 8, 12, 10, 3, 2, 12, 11, 17, 5, 19, 2, 5, 1` doplnit stav po prvním a posledním kroku up-sweep i down-sweep.

Řešení pro exclusive scan:

- Po 1. kroku up-sweep:
  `3, 18, 2, 10, 12, 22, 3, 5, 12, 23, 17, 22, 19, 21, 5, 6`
- Po posledním kroku up-sweep:
  `3, 18, 2, 28, 12, 22, 3, 55, 12, 23, 17, 45, 19, 21, 5, 127`
- Před down-sweep se kořen nastaví na `0`.
- Po 1. kroku down-sweep:
  `3, 18, 2, 28, 12, 22, 3, 0, 12, 23, 17, 45, 19, 21, 5, 55`
- Výsledek exclusive scan:
  `0, 3, 18, 20, 28, 40, 50, 53, 55, 67, 78, 95, 100, 119, 121, 126`

### Enumeration Sort s duplicitami

Zdroj: pattern z [[knowledge/exams/2023-2024/term-1-radny-b]]

Zadání: doplnit registry po několika krocích Enumeration Sortu; obrázek v raw je hůř čitelný, ale princip ranku je stabilní.

Řešení pro ukázkový vstup `4, 2, 4, 1`:

```text
rank[0] = count(<4)=2 + count(==4 vlevo)=0 => 2
rank[1] = count(<2)=1 + count(==2 vlevo)=0 => 1
rank[2] = count(<4)=2 + count(==4 vlevo)=1 => 3
rank[3] = count(<1)=0 + count(==1 vlevo)=0 => 0
```

Výstup je `1, 2, 4, 4`. Tie-break podle indexu zabrání kolizi dvou čtyřek.

### Pipeline Merge Sort

Zdroj: [[knowledge/exams/2025-2026/term-0-pretermin-a]]

Zadání: pro vstup `5, 2, 9, 4, 3, 6, 8, 7` zpracovávaný zprava zapsat stav po 10. kroku.

Řešení postupem:

1. Nekresli finálně seřazené pole; kresli tabulku taktů.
2. V každém taktu vlož další hodnotu zprava a u každého procesoru proveď právě jeden povolený compare/forward krok.
3. Menší hodnota jde z dvojice jako první.
4. Po 10. kroku opiš obsahy vstupů/výstupů procesů z tabulky.

Bez přesné tabulky kroků je odpověď neauditovatelná; u této úlohy je rozhodující mechanická simulace.

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
