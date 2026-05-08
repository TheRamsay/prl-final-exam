# Predikční matice: řádný termín 2025/2026

Predikce vychází z [[knowledge/exams/00-index|archivu termínů]], hlavně z nových bloků `Mapování na témata`. Čísla níže počítají výskyty tematických řádků v termínových souborech, ne ručně odhadované četnosti z `raw/common_*`.

## Datový základ

- Řádné termíny v archivu: 15 variant.
- Předtermíny v archivu: 5 souborů, z toho [[knowledge/exams/2025-2026/term-0-pretermin-b|2025/2026 předtermín B]] je jen krátký fragment.
- Pro predikci řádného termínu má větší váhu řádný-termínový slot pattern než přesné opakování předtermínu 2025/2026.

## Rychlý závěr

Nejpravděpodobnější tvar řádného termínu 2025/2026:

| Slot | Nejpravděpodobnější téma | Alternativy |
|---:|---|---|
| 1 | [[knowledge/topics/pram-tipovacka|PRAM tipovačka]] | PRAM model / architektura jen vzácně |
| 2 | [[knowledge/topics/architektury|Architektury]] | test-and-set / mutual exclusion |
| 3 | [[knowledge/topics/synchronizace-monitory-semafory|Monitory/semafory]] | Euler, řazení, parallel splitting |
| 4 | [[knowledge/topics/euler-tour-suffix-sums|Euler tour + suffix sums]] | distribuované algoritmy, řazení |
| 5 | [[knowledge/topics/pi-kalkul|Pi-kalkul]] nebo [[knowledge/topics/distribuovane-algoritmy|distribuované algoritmy]] | broadcast/kauzalita |
| 6 | [[knowledge/topics/razeni-prefix|Řazení/prefix]] | Euler, distribuované algoritmy |
| 7 | [[knowledge/topics/cla|CLA]] / [[knowledge/topics/pi-kalkul|Pi-kalkul]] / [[knowledge/topics/occam|OCCAM]] | distribuované algoritmy |
| 8 | [[knowledge/topics/mpi-reduce-bcast|MPI Reduce/Bcast]] | téměř fixní slot |

## Predikční matice

| Téma | Řádné výskyty | Typický slot v řádném | Bylo v předtermínu 2025/26 | Predikce pro řádný 2025/26 | Doporučený trénink |
|---|---:|---|---|---|---|
| [[knowledge/topics/pram-tipovacka|PRAM tipovačka]] | 16 | Q1 | ano, A | **téměř jisté** | AND/OR/XOR/NAND, nuly, monotónnost, cena vs čas |
| [[knowledge/topics/mpi-reduce-bcast|MPI Reduce/Bcast]] | 15 | Q8 | ano, A | **téměř jisté** | průměr, min/max, filtr podle průměru/min/max, `max % min` |
| [[knowledge/topics/architektury|Architektury]] | 13 | Q2 | ne | **velmi vysoké** | VLIW, dataflow/redukční počítač, zřetězení/MISD, PRAM model |
| [[knowledge/topics/euler-tour-suffix-sums|Euler tour + suffix sums]] | 12 | Q4/Q6 | ano, A | **vysoké** | `preorder(v)`, `level(v)`, počet následovníků/potomků |
| [[knowledge/topics/razeni-prefix|Řazení/prefix]] | 11 | Q6 | ano, A+B | **vysoké** | Prescan, Odd-even, Pipeline Merge Sort, Enumeration Sort |
| [[knowledge/topics/distribuovane-algoritmy|Distribuované algoritmy]] | 13 | Q4/Q5/Q6/Q7 | ano, A+B | **střední až vysoké** | Maekawa, Ricart-Agrawala, Suzuki, Marzullo, Random mating, volba lídra |
| [[knowledge/topics/synchronizace-monitory-semafory|Monitory/semafory]] | 8 | Q3/Q4 | ano, A | **střední až vysoké** | monitor `wait/signal`, readers-writers, producer-consumer, pět filozofů |
| [[knowledge/topics/pi-kalkul|Pi-kalkul]] | 9 | Q5/Q7 | ne | **střední až vysoké** | 3-4 redukce, substituce, pozorování, rozsah vázaných jmen |
| [[knowledge/topics/broadcast-fifo-kauzalita|Broadcast/FIFO/kauzalita]] | 6 | Q5/Q6, méně stabilní | ano, A+B | **střední** | FIFO vs kauzalita vs atomicita, ABCAST, synchronizovatelnost, koruna |
| [[knowledge/topics/cla|CLA]] | 4 | Q7 | ne | **střední** | generate/propagate/stop, scan přes carry, 2 příklady sčítání |
| [[knowledge/topics/occam|OCCAM]] | 4 | Q7 | ano, A | **nižší až střední** | kanály, `SEQ/PAR/ALT`, buffer/fronta, jednoduchý filtr |
| [[knowledge/topics/mutual-exclusion|Mutual exclusion]] | 5 | Q2/Q3/Q7 | ne | **nižší doplněk** | test-and-set, swap, bounded waiting, Peterson |
| [[knowledge/topics/parallel-splitting-select|Parallel splitting / SELECT]] | 2 | Q3 | ne | **nižší doplněk** | pivot, `L/E/G`, výběr k-tého prvku |
| [[knowledge/topics/linda-ada|Linda / ADA]] | 1 | Q7 | ne | **nízké** | Linda operace, list reverse/delete/search |

## Co je po předtermínu 2025/2026 nejzajímavější

Témata, která v předtermínu 2025/2026 nebyla a v řádných termínech se drží:

1. [[knowledge/topics/architektury|Architektury]] - hlavně Q2; v řádných termínech nejsilnější netriviální slot.
2. [[knowledge/topics/pi-kalkul|Pi-kalkul]] - častý ve střední části, v předtermínu 2025/2026 nebyl.
3. [[knowledge/topics/cla|CLA]] - není extrémně časté, ale historicky se vrací jako Q7.
4. [[knowledge/topics/mutual-exclusion|Mutual exclusion]] - doplněk, pokud místo monitorů přijde aktivní čekání.

Témata, která v předtermínu byla, ale i tak je nejde vynechat:

- [[knowledge/topics/pram-tipovacka|PRAM]] a [[knowledge/topics/mpi-reduce-bcast|MPI]]: strukturálně skoro povinné.
- [[knowledge/topics/razeni-prefix|Řazení/prefix]]: v předtermínu padly Pipeline Merge Sort a Enumeration Sort, ale řádný termín může otočit na Prescan/Odd-even.
- [[knowledge/topics/euler-tour-suffix-sums|Euler]]: předtermín měl `level(v)`, řádný může chtít `preorder(v)` nebo počet potomků.
- [[knowledge/topics/distribuovane-algoritmy|Distribuované algoritmy]]: předtermín měl volbu lídra/detekci ukončení, řádný může jít do Maekawa/Ricart/Suzuki/Marzullo.

## Doporučená příprava podle ROI

### Musí být automatické

- PRAM: umět odlišit čas a cenu, EREW/CREW/common CRCW.
- MPI: umět z hlavy napsat `Reduce`, volit kdy je potřeba `Bcast`, a vyřešit průměr/min/max.
- Architektury: mít 4 krátké odpovědi s nákresem: VLIW, dataflow/redukční počítač, zřetězení/MISD, PRAM model.

### Nejlepší druhá vlna

- Euler: naučit tři šablony `level`, `preorder`, počet potomků/následovníků.
- Řazení/prefix: procvičit tabulkovou simulaci, hlavně Prescan a Odd-even jako protiváhu k předtermínu.
- Synchronizace: monitor + readers-writers + pět filozofů.

### Diferenciační body

- Pi-kalkul a CLA, protože nebyly v předtermínu 2025/2026.
- Distribuované algoritmy jiného typu než předtermín: Maekawa, Ricart-Agrawala, Suzuki, Marzullo.

## Nejpravděpodobnější tréninková sada

Tahle sada je praktický výběr, ne nové zadání:

1. PRAM: OR/XOR/NAND + cena vs čas.
2. Architektura: VLIW nebo dataflow/redukční počítač.
3. Synchronizace: readers-writers nebo pět filozofů.
4. Euler: `preorder(v)` nebo počet potomků přes suffix/prefix sums.
5. Distribuovaný algoritmus: Ricart-Agrawala nebo Maekawa.
6. Řazení: Prescan nebo Odd-even merge/transposition.
7. Pi-kalkul nebo CLA.
8. MPI: součet prvků nad průměrem / druhé minimum / `max % min`.

## Odkazy

- [[knowledge/08-pretermin-vs-radny|Předtermín vs řádný termín]]
- [[knowledge/practice/00-index|Cvičné testy]]
- [[knowledge/06-must-know|Must-know tahák]]
- [[knowledge/02-cetnosti-temat|Četnosti témat]]
