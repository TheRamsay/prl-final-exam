# Monitory, semafory, čtenáři/písaři

## Zkouškový pattern

Zadání často chce krátkou definici `P/V`, monitoru, `wait/signal`, nebo klasický pseudokód pro readers-writers či producer-consumer. U monitoru se hodně kontroluje, jestli `wait` uvolní monitor.

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

Minimální odpověď: semafor je sdílený čítač s atomickými operacemi `P` a `V`; používá se k vyloučení nebo počítání dostupných zdrojů.

## Monitor

Monitor zapouzdřuje sdílený stav a procedury. V monitoru je v jednom okamžiku aktivní nejvýše jeden proces. Podmínkové proměnné mají operace:

- `wait(c)`: proces se zablokuje na podmínce a uvolní monitor.
- `signal(c)`: probudí jeden proces čekající na podmínce.

Minimální odpověď: monitor dává vzájemné vyloučení automaticky; podmínkové proměnné řeší čekání na stav uvnitř monitoru.

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

## Monitor ze semaforů

Když se ptají obecně, stačí popsat princip:

- binární semafor chrání vstup do monitoru;
- čekání na podmínce musí uvolnit monitor;
- `signal` přesune/probudí čekající proces podle zvolené sémantiky;
- je potřeba ošetřit frontu čekajících procesů.

## Mini-drill

1. Proč musí být `P` a `V` atomické?
2. Co přesně udělá `wait(c)` v monitoru?
3. Proč readers-writers s předností čtenářů může vyhladovět písaře?
4. Jaké tři semafory stačí pro producer-consumer s bufferem velikosti `N`?

## Vyřešené příklady z termínů

### Monitor, `wait`, `signal`

Zdroj: [[knowledge/exams/2025-2026/term-0-pretermin-a]]

Zadání: vysvětlit princip monitoru, zejména instrukce `signal` a `wait`, ilustrovat obrázkem.

Řešení:

- Monitor zapouzdřuje sdílený stav a procedury.
- V monitoru je v jednom okamžiku aktivní nejvýše jeden proces.
- `wait(c)` zablokuje proces na podmínkové proměnné `c` a uvolní monitor.
- `signal(c)` probudí jeden proces čekající na `c`, pokud nějaký existuje.
- Obrázek stačí kreslit jako monitor s frontou vstupu a frontami podmínkových proměnných.

### Čtenáři/písaři s předností čtenářů

Zdroj: [[knowledge/exams/2023-2024/term-1-radny-b]]

Zadání: řešit readers-writers se semafory a předností čtenářů.

Řešení:

- `mutex` chrání proměnnou `readcount`.
- `wrt` blokuje písaře i první/poslední čtenářskou změnu.
- První čtenář zamkne `wrt`, poslední čtenář ho odemkne.
- Písař jen `P(wrt), write, V(wrt)`.
- Nevýhoda: při trvalém příchodu čtenářů může písař hladovět.

### Producer-consumer

Zdroj: [[knowledge/exams/2019-2020/student-doc-digest]]

Zadání: klasický producent-konzument.

Řešení:

- `empty = N` počítá volná místa.
- `full = 0` počítá obsazená místa.
- `mutex = 1` chrání samotný buffer.
- Producent: `P(empty), P(mutex), insert, V(mutex), V(full)`.
- Konzument: `P(full), P(mutex), remove, V(mutex), V(empty)`.

## Kde se to objevuje

Podle sjednocených termínových souborů v archivu:

- [[knowledge/exams/2025-2026/term-0-pretermin-a]]
- [[knowledge/exams/2023-2024/term-1-radny-c]]
- [[knowledge/exams/2023-2024/term-1-radny-b]]
- [[knowledge/exams/2023-2024/term-1-radny-a]]
- [[knowledge/exams/2022-2023/term-1-radny-c]]
- [[knowledge/exams/2021-2022/term-3-druhy-opravny]]
- [[knowledge/exams/2021-2022/term-1-radny-c]]
- [[knowledge/exams/2021-2022/term-1-radny-b]]
- [[knowledge/exams/2020-2021/term-3-druhy-opravny]]
- [[knowledge/exams/2020-2021/term-2-prvni-opravny]]
- [[knowledge/exams/2019-2020/term-2-prvni-opravny]]
- [[knowledge/exams/2019-2020/term-1-radny-b]]
- [[knowledge/exams/2019-2020/term-1-radny-a]]

## Chyby

- `wait` v monitoru musí uvolnit monitor.
- `signal` není totéž co semaforové `V`.
- U readers-writers s předností čtenářů může hladovět písař; pokud zadání říká neřešit hladovění, je to v pořádku.
- U producer-consumer nezaměnit pořadí `empty/full`.
