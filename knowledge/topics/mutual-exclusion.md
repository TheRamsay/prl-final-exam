# Test-and-set, swap, Peterson

## Zkouškový pattern

Téma se ptá na aktivní čekání a atomické instrukce pro kritickou sekci. Často stačí napsat pseudokód, vysvětlit atomickou operaci a říct, které vlastnosti algoritmus má nebo nemá.

## Test-and-set

Atomická instrukce:

```text
test_and_set(lock):
  old = lock
  lock = true
  return old
```

Použití:

```text
while test_and_set(lock):
  skip
critical_section()
lock = false
```

## Peterson pro 2 procesy

```text
flag[i] = true
turn = j
while flag[j] && turn == j:
  skip
critical_section()
flag[i] = false
```

## Co uvádět

- Vzájemné vyloučení.
- Progress.
- Bounded waiting, pokud algoritmus zajišťuje.
- Aktivní čekání a jeho nevýhody.

## Vyřešené příklady z termínů

### Test-and-set

Zdroj: [[knowledge/exams/2020-2021/term-1-radny-zkratka]]

Zadání: Test-and-set.

Řešení:

- Definuj atomickou instrukci, která vrátí starou hodnotu zámku a nastaví zámek na obsazeno.
- Pseudokód kritické sekce je `while test_and_set(lock): skip`.
- Po kritické sekci se zámek uvolní `lock = false`.
- Uveď nevýhodu: aktivní čekání a bez další fronty žádná férovost.

### Aktivní čekání: test-and-set a swap

Zdroj: [[knowledge/exams/2022-2023/term-1-radny-a-zkratka]]

Zadání: aktivní čekání, test-and-set a swap.

Řešení:

- U obou instrukcí zdůrazni atomickou povahu.
- `swap` pracuje přes lokální proměnnou procesu a sdílený zámek.
- Obě varianty řeší mutual exclusion, ale základní podoba může hladovět.

### Bounded test-and-set

Zdroj: [[knowledge/exams/2022-2023/term-1-radny-b]]

Zadání: Bounded test-and-set.

Řešení:

- Nestačí obyčejný TAS; je potřeba přidat mechanismus pořadí čekatelů.
- V odpovědi explicitně odliš mutual exclusion od bounded waiting.
- Typicky se používá pole čekajících procesů nebo předávání povolení dalšímu čekateli.

## Kde se to objevuje

- [[knowledge/exams/2020-2021/term-1-radny-zkratka]]
- [[knowledge/exams/2021-2022/term-1-radny-a]]
- [[knowledge/exams/2022-2023/term-1-radny-a-zkratka]]
- [[knowledge/exams/2022-2023/term-1-radny-b]]
- [[knowledge/exams/2023-2024/term-2-prvni-opravny]]

## Chyby

- Tvrdit bounded waiting u jednoduchého TAS bez fronty.
- Zapomenout atomickou povahu TAS/swap.
- U Petersona prohodit `turn` tak, že oba čekají špatně.
