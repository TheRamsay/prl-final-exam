# PRAM tipovačka

## Zkouškový pattern

Úloha obvykle chce odhadnout čas, cenu a počet procesorů pro několik jednoduchých výpočtů nad polem. Často se ptá na rozdíl mezi EREW, CREW, CRCW a common CRCW.

## Modely

- EREW: exclusive read, exclusive write.
- CREW: concurrent read, exclusive write.
- CRCW: concurrent read, concurrent write.
- Common CRCW: souběžný zápis povolen jen při zápisu stejné hodnoty.

## Minimální odpověď

U každé podúlohy napiš:

1. použitý model;
2. čas `t(n)`;
3. počet procesorů `p(n)`;
4. cenu `c(n) = p(n) * t(n)`;
5. jednu větu, proč je čtení/zápis v daném modelu povolené.

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
4. Vyjádřit čas, počet procesorů a cenu.

## Typické mini-odpovědi

- **Existuje prvek s vlastností P?** Inicializuj odpověď na `false`; každý proces s nalezenou vlastností zapíše `true`. V common CRCW všichni zapisují stejnou hodnotu, takže `O(1)` při `n` procesorech.
- **AND přes všechny prvky.** Buď common CRCW zápisem `false` při porušení vlastnosti, nebo stromová redukce v `O(log n)`.
- **XOR/parita.** Nejde vyřešit pouhým common zápisem, protože výsledky nejsou monotónní; použij stromovou redukci.
- **Maximum/minimum.** Bez speciálního conflict resolution bezpečně stromová redukce `O(log n)` s `O(n)` procesory.
- **Monotónnost.** Paralelně porovnej sousední dvojice a potom agreguj AND.

## Mini-drill

1. Jaký je rozdíl mezi CRCW a common CRCW?
2. Proč OR existence jde v common CRCW v `O(1)`, ale XOR ne?
3. Jak spočítáš cenu stromové redukce s `n` procesory a časem `O(log n)`?
4. Kde u monotónnosti vzniká problém v EREW?

## Vyřešené příklady z termínů

### OR prvků `1/0`

Zdroj: [[knowledge/exams/2025-2026/term-0-pretermin-a]]

Zadání: určit cenu optimálního algoritmu pro OR nad `n` prvky při `N = n` procesorech.

Řešení:

- EREW: stromová redukce, čas `O(log n)`, procesory `O(n)`, cena `O(n log n)`.
- CREW: souběžné čtení nepomůže zásadně u redukce do jedné hodnoty, typicky `O(log n)` čas a cena `O(n log n)`.
- Common CRCW: každý proces s hodnotou `1` zapíše do sdílené odpovědi `1`; zapisovaná hodnota je stejná, čas `O(1)`, procesory `O(n)`, cena `O(n)`.

### NOT všech prvků

Zdroj: [[knowledge/exams/2025-2026/term-0-pretermin-a]]

Zadání: spočítat negaci všech prvků `1/0` v posloupnosti.

Řešení:

- Každý proces zpracuje jeden prvek: `B[i] = !A[i]`.
- V EREW, CREW i CRCW nevzniká konflikt, protože proces `i` čte `A[i]` a zapisuje `B[i]`.
- Čas `O(1)`, procesory `O(n)`, cena `O(n)`.

### XOR / parita

Zdroj: [[knowledge/exams/2023-2024/term-1-radny-b]]

Zadání: určit časovou složitost XOR pro EREW, CREW a common CRCW.

Řešení:

- XOR není monotónní existence vlastnosti, takže common zápis stejné hodnoty nestačí.
- Bez silnějšího conflict resolution použij stromovou redukci XOR.
- Typická odpověď pro všechny tři modely: čas `O(log n)`; při `O(n)` procesorech cena `O(n log n)`.

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

## Na co si dát pozor

- Common CRCW neznamená libovolný conflict resolution. Zapisující procesy musí zapisovat stejnou hodnotu.
- U ceny je potřeba počítat procesory, nejen čas.
- U EREW nesmí více procesorů ve stejném kroku číst stejnou buňku.
- U CREW je souběžné čtení povolené, zápis ne.
