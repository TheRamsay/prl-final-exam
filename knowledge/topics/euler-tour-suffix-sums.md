# Euler tour a suffix sums

## Zkouškový pattern

Zadání dá strom, adjacency list nebo tabulku hran a chce `Etour`, `level(v)`, `preorder(v)` nebo počet následovníků. V odpovědi musí být vidět převod ze stromu na orientované hrany a použití prefix/suffix sum.

## Základní princip

Strom se převede na orientované hrany v Eulerově průchodu. Nad hranami se nastaví ohodnocení a použije se prefix/suffix suma. Podle volby ohodnocení z výsledku dostaneme vlastnosti vrcholů.

## Typické výstupy

- `preorder(v) -> N`
- `level(v) -> N`
- počet následovníků/potomků
- hloubka vrcholu
- Etour tabulka

## Minimální odpověď

1. Každou neorientovanou hranu nahradím dvěma orientovanými hranami.
2. Pro každou orientovanou hranu určím následníka v Euler tour.
3. Nastavím váhy podle požadované veličiny.
4. Spočítám prefix/suffix sum.
5. Převedu hodnoty z hran zpět na vrcholy.
6. Uvedu složitost.

## Šablona odpovědi

1. Vytvořit dvojice orientovaných hran pro každou neorientovanou hranu stromu.
2. Sestavit Euler tour přes následníky hran.
3. Každé hraně přiřadit váhu podle cíle:
   - pro level/depth typicky `+1` na dopředné hraně a `-1` na zpětné;
   - pro preorder označit první vstup do vrcholu;
   - pro počet následovníků pracovat s velikostí podstromu.
4. Spočítat suffix/prefix sum.
5. Z hodnot hran odvodit hodnoty vrcholů.
6. Uvést složitost: typicky `O(log n)` paralelně po sestavení struktur, práce `O(n)`.

## Volba vah

| Cíl | Typická váha |
|---|---|
| `level(v)` / hloubka | `+1` na dopředné hraně, `-1` na zpětné |
| `preorder(v)` | označit první vstup do vrcholu |
| počet potomků | spočítat rozsah podstromu v Eulerově průchodu |
| Etour tabulka | vypsat následníky orientovaných hran |

## Mini-drill

1. Proč má strom s `n` vrcholy `2(n-1)` orientovaných hran v Etour?
2. Jak poznáš dopřednou a zpětnou hranu?
3. Kdy použiješ prefix a kdy suffix sum?
4. Jak převedeš hranovou hodnotu zpět na `level(v)`?

## Kde se to objevuje

- [[knowledge/exams/2025-2026/term-0-pretermin-a]]
- [[knowledge/exams/2024-2025/term-0-pretermin]]
- [[knowledge/exams/2023-2024/student-doc-digest]]
- [[knowledge/exams/2022-2023/student-doc-digest]]
- [[knowledge/exams/2021-2022/student-doc-digest]]
- [[knowledge/exams/2019-2020/student-doc-digest]]

## Chyby

- Neříct, jak poznám dopřednou a zpětnou hranu.
- Zaměnit pořadí hran v Etour.
- Vynechat převod z hranových hodnot na hodnoty vrcholů.
- Uvést jen výsledek bez popisu vah.
