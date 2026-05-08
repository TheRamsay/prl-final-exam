# Euler tour a suffix sums

## Základní princip

Strom se převede na orientované hrany v Eulerově průchodu. Nad hranami se nastaví ohodnocení a použije se prefix/suffix suma. Podle volby ohodnocení z výsledku dostaneme vlastnosti vrcholů.

## Typické výstupy

- `preorder(v) -> N`
- `level(v) -> N`
- počet následovníků/potomků
- hloubka vrcholu
- Etour tabulka

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

## Chyby

- Neříct, jak poznám dopřednou a zpětnou hranu.
- Zaměnit pořadí hran v Etour.
- Vynechat převod z hranových hodnot na hodnoty vrcholů.

