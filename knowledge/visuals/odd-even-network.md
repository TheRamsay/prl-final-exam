# Odd-even: compare-exchange síť

Zdrojový topic: [[knowledge/topics/razeni-prefix]]

## Odd-even transposition sort

Střídají se sudé a liché vrstvy sousedních compare-exchange operací.

```mermaid
flowchart TB
  S0["start: a0 a1 a2 a3 a4 a5"] --> S1["krok 1: CE(0,1), CE(2,3), CE(4,5)"]
  S1 --> S2["krok 2: CE(1,2), CE(3,4)"]
  S2 --> S3["krok 3: CE(0,1), CE(2,3), CE(4,5)"]
  S3 --> S4["krok 4: CE(1,2), CE(3,4)"]
  S4 --> S5["opakuj n kroků"]
```

Tabulkově:

| Krok | Aktivní compare-exchange bloky |
|---:|---|
| 1 | `(0,1)`, `(2,3)`, `(4,5)` |
| 2 | `(1,2)`, `(3,4)` |
| 3 | `(0,1)`, `(2,3)`, `(4,5)` |
| 4 | `(1,2)`, `(3,4)` |

## Odd-even merge sort pro 4 vstupy

Pro malou síť je nejpraktičtější kreslit vrstvy CE bloků.

```mermaid
flowchart LR
  A0["a0"] --> C01["CE(0,1)"]
  A1["a1"] --> C01
  A2["a2"] --> C23["CE(2,3)"]
  A3["a3"] --> C23
  C01 --> C02["CE(0,2)"]
  C23 --> C02
  C01 --> C13["CE(1,3)"]
  C23 --> C13
  C02 --> C12["CE(1,2)"]
  C13 --> C12
  C12 --> OUT["seřazený výstup"]
```

Stejná síť jako vrstvy:

| Vrstva | CE bloky |
|---:|---|
| 1 | `(0,1)`, `(2,3)` |
| 2 | `(0,2)`, `(1,3)` |
| 3 | `(1,2)` |

## Mini příklad transposition sortu

Vstup:

```text
[4, 1, 3, 2]
```

| Krok | Operace | Stav |
|---:|---|---|
| 0 | start | `[4, 1, 3, 2]` |
| 1 | `(0,1)`, `(2,3)` | `[1, 4, 2, 3]` |
| 2 | `(1,2)` | `[1, 2, 4, 3]` |
| 3 | `(0,1)`, `(2,3)` | `[1, 2, 3, 4]` |
| 4 | `(1,2)` | `[1, 2, 3, 4]` |

## Zkoušková odpověď

1. Uveď, které CE bloky běží paralelně v jedné vrstvě.
2. Nezaměň transposition sort a odd-even merge sort.
3. U sítě kresli vrstvy; u simulace kresli stavy po krocích.

## Časté chyby

- Spustit v jedné vrstvě CE bloky, které sdílejí stejný vodič.
- Prohlásit, že transposition sort končí vždy po dvou krocích.
- U merge sítě zapomenout poslední porovnání středních vodičů.
