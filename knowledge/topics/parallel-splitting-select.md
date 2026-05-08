# Parallel splitting a SELECT

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

## Chyby

- Špatně přepočítat `k` při pokračování v `G`.
- Ignorovat duplicity pivotu.
- Neuvést, že samotné stabilní rozdělení se typicky dělá přes prefixy.

