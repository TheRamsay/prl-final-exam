# Carry-look-ahead adder

## Pojmy

Pro bitovou pozici `i`:

- generate: `g_i = a_i & b_i`
- propagate: `p_i = a_i xor b_i` nebo podle přednášky `a_i | b_i`
- carry: `c_{i+1} = g_i | (p_i & c_i)`
- sum: `s_i = p_i xor c_i` při XOR definici propagate.

Někdy se v materiálech používá trojice propagate/stop/generate. Držet se definice ze zadání/přednášky.

## Postup u příkladu

1. Přepsat čísla do binární soustavy na stejný počet bitů.
2. Pro každý bit spočítat `g` a `p` nebo `p/s/g`.
3. Prefixovým výpočtem spočítat carry do každé pozice.
4. Dopočítat součet.
5. Uvést paralelní hloubku `O(log n)`.

## Chyby

- Míchat dvě definice propagate.
- Počítat bity v opačném směru.
- Zapomenout vstupní carry `c_0`.

