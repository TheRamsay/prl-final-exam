# 2025/2026 - řádný termín - cvičná predikce B

## Metadata

| Pole | Hodnota |
|---|---|
| Typ | cvičné zadání |
| Cíl | predikce pro řádný termín 2025/2026 |
| Doporučený limit | 120-150 minut |
| Body | 70 |
| Jistota | střední, zaměřeno na témata z předtermínu a oprav |

## Témata

- [[knowledge/topics/pram-tipovacka|PRAM tipovačka]]
- [[knowledge/topics/architektury|Propojovací síť / Xeon Phi]]
- [[knowledge/topics/broadcast-fifo-kauzalita|FIFO broadcast a kauzalita]]
- [[knowledge/topics/euler-tour-suffix-sums|Euler tour a level(v)]]
- [[knowledge/topics/distribuovane-algoritmy|Čtyři čtenáři / detekce ukončení]]
- [[knowledge/topics/razeni-prefix|Prescan]]
- [[knowledge/topics/occam|OCCAM]]
- [[knowledge/topics/mpi-reduce-bcast|MPI Reduce/Bcast]]

## Proč tahle varianta

Tahle sada pokrývá témata, která se objevila v předtermínu 2025/2026, ale převádí je do řádného-termínového rozsahu osmi úloh. Je vhodná jako kontrola proti tomu, co by mohli recyklovat v jiné formulaci: FIFO/kauzalita, čtyři čtenáři, prescan, OCCAM a MPI.

## Zadání

1. **PRAM tipovačka, 6 b.** Pro EREW, CREW a common CRCW určete odpovědi z možností `O(1)`, `O(log n)`, `O(n)`, `O(n log n)`, `O(n^2)`, polynomiální:
   - čas pro negaci všech bitů v poli délky `n`;
   - cenu algoritmu, který zjistí, zda pole obsahuje pouze nuly;
   - cenu algoritmu, který spočítá maximum z `n` čísel.

2. **Propojovací síť a Xeon Phi, 9 b.** Vysvětlete, k čemu slouží propojovací síť v paralelním systému. Popište alespoň dvě topologie a jejich výhody/nevýhody. Na závěr stručně vysvětlete, proč se Xeon Phi dá chápat jako kombinace MIMD a SIMD.

3. **FIFO broadcast, 9 b.** Napište algoritmus `send` a `recv` pro FIFO broadcast. Uveďte, jak se používají sekvenční čísla a buffer. Poté definujte relaci kauzality `->` a vysvětlete, proč FIFO samo o sobě nezaručuje kauzální broadcast.

4. **Euler tour + level(v), 9 b.** Pro strom s hranami `1-2`, `1-3`, `2-4`, `2-5`, `3-6`, `6-7` sestavte orientované hrany pro Euler tour. Popište, jak pomocí ohodnocení dopředných a zpětných hran a suffix sums spočítáte úroveň `level(v)` každého vrcholu. Uveďte časovou složitost.

5. **Detekce ukončení, 10 b.** Popište princip algoritmu čtyř čtenářů / čtyř čítačů pro detekci ukončení distribuovaného výpočtu. Uveďte jeden příklad běhu, kde je ukončení detekováno, a jeden příklad, kde lokální pasivita nestačí kvůli zprávě v kanálu.

6. **Prescan, 9 b.** Pro posloupnost

```text
4, 1, 9, 2, 8, 3, 7, 5
```

proveďte exclusive prescan pomocí up-sweep/down-sweep. Zapište stav pole po prvním kroku up-sweep, po dokončení up-sweep, po prvním kroku down-sweep a výsledné pole.

7. **OCCAM, 9 b.** Definujte nekonečnou proceduru `ROUTER`, která má vstupní kanály `DATA` a `CTRL` typu `BYTE` a pole výstupních kanálů `OUT[5]`. Procedura drží aktivní index výstupu, na začátku `0`. Pokud přijde hodnota na `CTRL` v rozsahu `0..4`, nastaví aktivní index. Pokud přijde hodnota na `DATA`, odešle ji na aktuální výstupní kanál. Uvažujte, že oba vstupní kanály mohou být připravené nezávisle.

8. **MPI, 10 b.** Každý proces má přirozené číslo `value`. Napište algoritmus pomocí `MPI_Reduce` a `MPI_Bcast`, který na procesu 0 vypíše `ANO`, pokud je součet všech sudých hodnot dělitelný počtem hodnot rovných globálnímu maximu; jinak vypíše `NE`. Ošetřete dělení nulou.

## Kontrola po dopsání

- FIFO buffer: [[knowledge/visuals/fifo-broadcast-buffer]]
- Kauzalita: [[knowledge/visuals/causal-broadcast-happened-before]]
- Prescan: [[knowledge/visuals/prescan-upsweep-downsweep]]
- OCCAM: [[knowledge/topics/occam]]
- MPI: [[knowledge/topics/mpi-reduce-bcast]]
