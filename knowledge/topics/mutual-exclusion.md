# Test-and-set, swap, Peterson

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

## Chyby

- Tvrdit bounded waiting u jednoduchého TAS bez fronty.
- Zapomenout atomickou povahu TAS/swap.
- U Petersona prohodit `turn` tak, že oba čekají špatně.

