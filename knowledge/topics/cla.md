# Carry-look-ahead adder

## Zkouškový pattern

Zadání typicky dá dvě dekadická čísla a chce ukázat paralelní sčítání přes Carry-look-ahead. Nejde jen o výsledek součtu; body jsou za `generate/propagate/stop`, prefixový výpočet přenosů a krátké vysvětlení hloubky `O(log n)`.

## Pojmy

Pro bitovou pozici `i`:

- generate: `g_i = a_i & b_i`
- propagate: `p_i = a_i xor b_i` nebo podle přednášky `a_i | b_i`
- carry: `c_{i+1} = g_i | (p_i & c_i)`
- sum: `s_i = p_i xor c_i` při XOR definici propagate.

Někdy se v materiálech používá trojice propagate/stop/generate. Držet se definice ze zadání/přednášky.

## Minimální odpověď

- Převést čísla do binární podoby se stejnou šířkou.
- Pro každý bit určit stav `g/p/s` nebo dvojici `g/p` podle zadání.
- Přenosy počítat prefixově, ne sekvenčním ripple-carry průchodem.
- Na konci dopočítat sum bity a uvést paralelní hloubku `O(log n)`.

## Postup u příkladu

1. Přepsat čísla do binární soustavy na stejný počet bitů.
2. Pro každý bit spočítat `g` a `p` nebo `p/s/g`.
3. Prefixovým výpočtem spočítat carry do každé pozice.
4. Dopočítat součet.
5. Uvést paralelní hloubku `O(log n)`.

## Vyřešené příklady z termínů

### CLA: `90 + 139`

Zdroj: [[knowledge/exams/2018-2019/term-1-radny-a]]

Zadání: algoritmem Carry-look-ahead Parallel Binary Adder provést součet `90 + 139` a názorně demonstrovat kroky.

Řešení:

- Nepiš jen `229`; ukaž binární vstupy a tabulku bitových stavů.
- Pro každý bit rozhodni, zda generuje carry (`g`), propaguje carry (`p`), nebo carry zastaví (`s`).
- Prefix operátor nad stavy určí carry do vyšších bitů.
- Součet získáš XORem vstupních bitů s příslušným carry.

### CLA: `77 + 125`

Zdroj: [[knowledge/exams/2018-2019/term-1-radny-b]]

Zadání: CLA sčítačka, popsat vše potřebné.

Řešení:

- Tento typ je stejný jako výše, ale je dobrý na procvičení směru bitů.
- Největší riziko je počítat prefix zleva doprava podle zápisu čísla místo od nejnižšího bitu k vyšším bitům.
- V odpovědi explicitně napiš, který bit bereš jako `i=0`.

### CLA: `39 + 110` a `120 + 99`

Zdroje: [[knowledge/exams/2020-2021/term-1-radny-zkratka]], [[knowledge/exams/2022-2023/term-2-prvni-opravny]]

Zadání: spočítat konkrétní součet pomocí CLA.

Řešení:

- U obou zadání stačí stejná šablona: převod, `g/p/s`, prefix carry, výsledné bity.
- Pokud zadání neříká definici `p`, drž se přednáškové konvence pro daný zápis; nemíchej XOR-propagate a OR-propagate v jednom řešení.

## Kde se to objevuje

- [[knowledge/exams/2018-2019/term-1-radny-a]]
- [[knowledge/exams/2018-2019/term-1-radny-b]]
- [[knowledge/exams/2018-2019/term-1-radny-c]]
- [[knowledge/exams/2020-2021/term-1-radny-zkratka]]
- [[knowledge/exams/2022-2023/term-2-prvni-opravny]]
- [[knowledge/exams/2023-2024/term-0-pretermin]]

## Chyby

- Míchat dvě definice propagate.
- Počítat bity v opačném směru.
- Zapomenout vstupní carry `c_0`.
