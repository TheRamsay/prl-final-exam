# Linda, ADA a ostatní jazyky

## Zkouškový pattern

Linda se objevuje jako práce s tuple space nad jednoduchou datovou strukturou, často seznamem. ADA se objevuje spíš jako krátká teorie: task, entry, rendezvous a `accept`.

## Oficiální slidy

- [[knowledge/sources/slides/komunikace#Strana 42|Komunikace, str. 42]] až [[knowledge/sources/slides/komunikace#Strana 46|str. 46]] - ADA, rendezvous, `accept`, `select` a bounded buffer.
- [[knowledge/sources/slides/komunikace#Strana 49|Komunikace, str. 49]] až [[knowledge/sources/slides/komunikace#Strana 52|str. 52]] - Linda tuple space a operace `out`, `in`, `rd`, `eval`.
- [[knowledge/sources/slides/komunikace#Strana 53|Komunikace, str. 53]] až [[knowledge/sources/slides/komunikace#Strana 55|str. 55]] - synchronizační primitiva, kanály a příklad se seznamem v Lindě.

## Linda

Linda pracuje s tuple space.

Typické operace:

- `out(tuple)`: vložení n-tice.
- `in(pattern)`: vyzvednutí odpovídající n-tice, blokuje.
- `rd(pattern)`: přečtení odpovídající n-tice bez odebrání.
- `eval(...)`: spuštění procesu / vyhodnocení.

Typické úlohy:

- operace nad spojovým seznamem;
- reverse/delete/search;
- koordinace procesů přes n-tice.

## ADA

Zkouškově spíš okrajové. Držet se pojmů:

- task;
- entry;
- rendezvous;
- accept.

## Vyřešené příklady z termínů

### Linda: reverz seznamu

Zdroj: [[knowledge/exams/2020-2021/student-doc-digest]]

Zadání: Linda, reverz seznamu.

Řešení:

- Uzel seznamu reprezentuj n-ticí, například `(node, id, value, next)`.
- `rd` použij pro čtení bez odebrání, `in` pro destruktivní změnu vazby.
- Reverz typicky přepíše odkazy `next`; hlídej, aby současně neběžely dvě destruktivní změny stejné n-tice.

### Linda: vyhledávání v lineárním seznamu

Zdroj: [[knowledge/exams/2021-2022/term-3-druhy-opravny]]

Zadání: Linda, vyhledávání v lineárním seznamu.

Řešení:

- Proces iteruje přes n-tice uzlů podle odkazu `next`.
- Pro čisté hledání používej `rd`, aby se seznam nerozbil.
- `in` použij až u operací typu delete nebo update.

### ADA: popsat a uvést příkazy

Zdroj: [[knowledge/exams/2022-2023/term-3-druhy-opravny]]

Zadání: ADA, popsat a uvést konkrétní příkazy.

Řešení:

- Základ je `task`, `entry`, volání entry a `accept`.
- Rendezvous znamená, že volající i přijímající task se synchronizují na komunikačním bodě.
- Uveď, že `accept` může obsahovat tělo obsluhy požadavku.

## Kde se to objevuje

Podle sjednocených termínových souborů v archivu:

- [[knowledge/exams/2023-2024/term-3-druhy-opravny]]
- [[knowledge/exams/2022-2023/term-3-druhy-opravny]]
- [[knowledge/exams/2021-2022/term-3-druhy-opravny]]
- [[knowledge/exams/2020-2021/term-2-prvni-opravny]]
- [[knowledge/exams/2019-2020/term-2-prvni-opravny]]
- [[knowledge/exams/2019-2020/term-1-radny-b]]

## Chyby

- Zaměnit `rd` a `in`.
- Zapomenout, že `in` je destruktivní.
- U rendezvous neuvažovat blokování obou stran do spárování.
