# PRAM tipovačka

## Modely

- EREW: exclusive read, exclusive write.
- CREW: concurrent read, exclusive write.
- CRCW: concurrent read, concurrent write.
- Common CRCW: souběžný zápis povolen jen při zápisu stejné hodnoty.

## Co u odpovědi uvádět

- Čas `t(n)`.
- Cena `c(n) = p(n) * t(n)`.
- Použitý počet procesorů.
- Jestli využívám stromovou redukci, paralelní porovnávání, nebo common write.

## Rychlá mapa typických úloh

| Úloha | Intuice |
|---|---|
| OR/AND existence vlastnosti | CRCW často `O(1)` common zápisem stejné hodnoty, EREW/CREW obvykle redukce `O(log n)` |
| XOR/parita | nelze jen common write, typicky stromová redukce |
| max/min | paralelní redukce nebo turnaj |
| počet prvků | transformace na 0/1 a suma |
| monotónnost | paralelně zkontrolovat sousedy, pak AND přes výsledky |
| všechna čísla stejná | porovnat s jedním prvkem nebo sousedy, podle modelu čtení |

## Šablona řešení

1. Převést zadání na elementární predikáty nad prvky nebo dvojicemi.
2. Spočítat lokální predikát paralelně.
3. Agregovat přes OR/AND/sumu/max.
4. Vyjádřit čas a cenu.

## Na co si dát pozor

- Common CRCW neznamená libovolný conflict resolution. Zapisující procesy musí zapisovat stejnou hodnotu.
- U ceny je potřeba počítat procesory, nejen čas.
- U EREW nesmí více procesorů ve stejném kroku číst stejnou buňku.
- U CREW je souběžné čtení povolené, zápis ne.

