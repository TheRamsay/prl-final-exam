# Broadcast, FIFO, kauzalita, ABCAST

## Zkouškový pattern

Zadání bývá jedna ze tří forem: napsat algoritmus FIFO broadcastu, rozhodnout vlastnosti v diagramu, nebo vysvětlit synchronizovatelnost přes korunu. Hodnotí se hlavně přesné rozlišení FIFO, kauzality a atomicity.

## Pojmy

- FIFO broadcast: zprávy od stejného odesílatele jsou každému příjemci doručeny ve stejném pořadí, v jakém byly odeslány.
- Kauzální broadcast: pokud `m1 -> m2` v relaci happened-before, všichni doručí `m1` před `m2`.
- Atomic broadcast/ABCAST: všichni správní příjemci doručí zprávy ve stejném globálním pořadí.
- Synchronizovatelnost: asynchronní průběh lze reprezentovat synchronním, pokud splňuje podmínky dané komunikační strukturou, často se zkouší přes "korunu".

## Minimální odpověď

- FIFO řeší pořadí zpráv **od stejného odesílatele**.
- Kauzalita řeší happened-before, tedy lokální pořadí, send/receive a tranzitivitu.
- Atomicita řeší stejné globální pořadí doručení u všech procesů.
- Porušení hledej až na úrovni doručení aplikaci, ne pouhého přijetí do bufferu.

## FIFO broadcast algoritmus

Typická šablona:

- Každý proces drží pořadové číslo zpráv od každého odesílatele.
- Odesílatel inkrementuje vlastní sekvenční číslo a posílá `(sender, seq, payload)`.
- Příjemce doručí zprávu od `sender` jen pokud `seq == next[sender]`.
- Jinak ji odloží do bufferu.
- Po doručení zprávy zkontroluje buffer, jestli se neuvolnily další zprávy.

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

## Koruna / synchronizovatelnost

U úloh async -> sync hledej cyklickou závislost mezi zprávami a procesy, která brání tomu, aby šel průběh rozřezat na synchronní kola. Typická odpověď:

1. označit problematické zprávy;
2. ukázat lokální pořadí na procesech;
3. vysvětlit, proč vzniká koruna;
4. navrhnout odstranění nebo změnu pořadí zpráv, pokud zadání chce opravu.

## Mini-drill

1. Může FIFO porušit dvojice zpráv od různých odesílatelů?
2. Jaké tři typy hran tvoří happened-before?
3. Jak poznáš porušení atomic broadcastu?
4. Proč bufferované přijetí není totéž co doručení?

## Kde se to objevuje

- [[knowledge/exams/2025-2026/term-0-pretermin-a]]
- [[knowledge/exams/2025-2026/term-0-pretermin-b]]
- [[knowledge/exams/2024-2025/term-0-pretermin]]
- [[knowledge/exams/2023-2024/student-doc-digest]]
- [[knowledge/exams/2022-2023/student-doc-digest]]
- [[knowledge/exams/2021-2022/student-doc-digest]]

## Chyby

- Zaměnit přijetí zprávy s doručením aplikaci.
- Posuzovat FIFO mezi různými odesílateli.
- Přehlédnout tranzitivitu kauzality.
- U atomicity kontrolovat jen jeden proces místo porovnání pořadí mezi procesy.
