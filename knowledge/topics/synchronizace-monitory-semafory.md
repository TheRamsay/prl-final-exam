# Monitory, semafory, čtenáři/písaři

## Semafor

Operace:

```text
P(S):
  if S > 0: S = S - 1
  else blokuj proces ve frontě S

V(S):
  if fronta S není prázdná: probuď jeden proces
  else S = S + 1
```

`P` a `V` musí být atomické.

## Monitor

Monitor zapouzdřuje sdílený stav a procedury. V monitoru je v jednom okamžiku aktivní nejvýše jeden proces. Podmínkové proměnné mají operace:

- `wait(c)`: proces se zablokuje na podmínce a uvolní monitor.
- `signal(c)`: probudí jeden proces čekající na podmínce.

## Čtenáři/písaři s předností čtenářů

Typická idea:

```text
semaphore mutex = 1
semaphore wrt = 1
int readcount = 0

reader:
  P(mutex)
  readcount++
  if readcount == 1: P(wrt)
  V(mutex)
  read()
  P(mutex)
  readcount--
  if readcount == 0: V(wrt)
  V(mutex)

writer:
  P(wrt)
  write()
  V(wrt)
```

## Producent-konzument

Standardní semafory:

- `empty = N`
- `full = 0`
- `mutex = 1`

Producent: `P(empty), P(mutex), insert, V(mutex), V(full)`.
Konzument: `P(full), P(mutex), remove, V(mutex), V(empty)`.

## Chyby

- `wait` v monitoru musí uvolnit monitor.
- `signal` není totéž co semaforové `V`.
- U readers-writers s předností čtenářů může hladovět písař; pokud zadání říká neřešit hladovění, je to v pořádku.

