# Parallel splitting a SELECT

## Zkouškový pattern

Zadání chce buď popsat paralelní rozdělení podle pivotu, nebo ukázat princip paralelního SELECTu na malém příkladu. Body jsou za správnou práci s částmi `L/E/G`, duplicitami pivotu a přepočtem `k`.

## Parallel splitting

Zadaný pivot rozdělí posloupnost do tří částí:

- `L`: prvky menší než pivot;
- `E`: prvky rovné pivotu;
- `G`: prvky větší než pivot.

Paralelně se pro každý prvek spočítá predikát a pozice ve výsledné části pomocí prefix sum.

## SELECT

Cílem je najít k-tý nejmenší prvek.

Šablona:

1. Vybrat pivot.
2. Rozdělit na `L/E/G`.
3. Pokud `k <= |L|`, pokračovat v `L`.
4. Pokud `|L| < k <= |L| + |E|`, pivot je výsledek.
5. Jinak pokračovat v `G` s `k = k - |L| - |E|`.

## Vyřešené příklady z termínů

### Parallel splitting s malým příkladem

Zdroj: [[knowledge/exams/2018-2019/term-1-radny-b]]

Zadání: popsat Parallel splitting a uvést menší příklad.

Řešení:

- Vyber pivot a pro každý prvek paralelně určete, zda patří do `L`, `E`, nebo `G`.
- Prefix sum nad predikáty určí pozici prvku v příslušné části.
- Výsledek zapisuj jako tři souvislé bloky `L | E | G`.

### Paralelní SELECT

Zdroj: [[knowledge/exams/2022-2023/term-2-prvni-opravny]]

Zadání: vysvětlit princip paralelního SELECTu a ukázat příklad.

Řešení:

- Po rozdělení podle pivotu porovnej `k` s `|L|` a `|L| + |E|`.
- Pokud výsledek leží v `G`, nezapomeň přepočítat `k`.
- Duplicity pivotu řeš přes blok `E`; pokud `k` padne do `E`, výsledkem je pivot.

### Parallel splitting v novějším předtermínu

Zdroj: [[knowledge/exams/2024-2025/term-0-pretermin]]

Zadání: Parallel splitting, ukázat na příkladu.

Řešení:

- Stačí malý vstup, pivot, tři predikátové řádky a výsledné pozice.
- Při vysvětlování zmiň, že stabilní rozdělení typicky používá prefixy.

## Kde se to objevuje

Podle sjednocených termínových souborů v archivu:

- [[knowledge/exams/2024-2025/term-0-pretermin]]
- [[knowledge/exams/2024-2025/term-0-pretermin-b]]
- [[knowledge/exams/2023-2024/term-3-druhy-opravny]]
- [[knowledge/exams/2022-2023/term-2-prvni-opravny]]
- [[knowledge/exams/2021-2022/term-1-radny-b]]
- [[knowledge/exams/2018-2019/term-1-radny-b]]

## Chyby

- Špatně přepočítat `k` při pokračování v `G`.
- Ignorovat duplicity pivotu.
- Neuvést, že samotné stabilní rozdělení se typicky dělá přes prefixy.
