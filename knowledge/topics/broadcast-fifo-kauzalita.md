# Broadcast, FIFO, kauzalita, ABCAST

## Pojmy

- FIFO broadcast: zprávy od stejného odesílatele jsou každému příjemci doručeny ve stejném pořadí, v jakém byly odeslány.
- Kauzální broadcast: pokud `m1 -> m2` v relaci happened-before, všichni doručí `m1` před `m2`.
- Atomic broadcast/ABCAST: všichni správní příjemci doručí zprávy ve stejném globálním pořadí.
- Synchronizovatelnost: asynchronní průběh lze reprezentovat synchronním, pokud splňuje podmínky dané komunikační strukturou, často se zkouší přes "korunu".

## FIFO broadcast algoritmus

Typická šablona:

- Každý proces drží pořadové číslo zpráv od každého odesílatele.
- Odesílatel inkrementuje vlastní sekvenční číslo a posílá `(sender, seq, payload)`.
- Příjemce doručí zprávu od `sender` jen pokud `seq == next[sender]`.
- Jinak ji odloží do bufferu.

## Kauzalita

Relace `->`:

1. Události ve stejném procesu jsou uspořádané lokálním pořadím.
2. Odeslání zprávy předchází jejímu přijetí.
3. Relace je tranzitivní.

## Jak řešit diagramy

1. Vypsat pro každý proces lokální pořadí událostí.
2. Doplnit hrany send -> receive.
3. Udělat tranzitivní uzávěr jen v nutném rozsahu.
4. Hledat porušení:
   - FIFO: stejný odesílatel, jeden příjemce, obrácené doručení.
   - Kauzalita: doručení následku před příčinou.
   - Atomicita: dva procesy doručí stejné zprávy v jiném pořadí.

## Chyby

- Zaměnit přijetí zprávy s doručením aplikaci.
- Posuzovat FIFO mezi různými odesílateli.
- Přehlédnout tranzitivitu kauzality.

