# Četnosti témat

Zdroj: `raw/common_latest.md` a `raw/common_16-22.md`.

## Aktualizovaný odhad

| Téma | Odhad četnosti | Typické varianty |
|---|---:|---|
| [[knowledge/topics/mpi-reduce-bcast|MPI Reduce/Bcast]] | ~35 | průměr, min/max, počet prvků, normalizace, součet podle podmínky, druhé min/max |
| [[knowledge/topics/pram-tipovacka|PRAM tipovačka]] | ~27 | EREW/CREW/common CRCW, AND/OR/XOR/NAND, max/min, monotónnost, nuly/sudá |
| [[knowledge/topics/broadcast-fifo-kauzalita|Broadcast/FIFO/kauzalita]] | ~26 | FIFO broadcast, kauzální relace, porušení FIFO/kauzality/atomicity, koruna |
| [[knowledge/topics/architektury|Architektury]] | ~26 | VLIW, zřetězení/MISD, dataflow, SIMD/MIMD, Xeon Phi, PRAM, sítě |
| [[knowledge/topics/razeni-prefix|Řazení/prefix]] | ~25 | Pipeline Merge Sort, Enumeration Sort, Prescan, Odd-even |
| [[knowledge/topics/synchronizace-monitory-semafory|Monitory/semafory]] | ~17 | wait/signal, monitor ze semaforů, readers-writers, producer-consumer |
| [[knowledge/topics/distribuovane-algoritmy|Distribuované algoritmy]] | ~16 | Marzullo, Maekawa, Suzuki, Dijkstra, Hirschberg-Sinclair |
| [[knowledge/topics/euler-tour-suffix-sums|Euler tour + suffix sums]] | ~15 | preorder, level/depth, následovníci, Etour |
| [[knowledge/topics/distribuovane-algoritmy|Random mating/list ranking/terminace]] | ~15 | random mating do 4 kroků, reconstruction, 4-counter termination |
| [[knowledge/topics/pi-kalkul|Pi-kalkul]] | ~14 | 3 až 4 možné redukce, koncové výrazy |
| [[knowledge/topics/cla|CLA]] | ~14 | propagate/stop/generate, carries přes scan |
| [[knowledge/topics/occam|OCCAM]] | ~13 | kanály, pole kanálů, queue/buffer, alternace |
| [[knowledge/topics/mutual-exclusion|Test-and-set/Peterson]] | ~8 | aktivní čekání, bounded TAS, starvation |
| [[knowledge/topics/parallel-splitting-select|Parallel splitting/SELECT]] | ~6 | pivot, L/E/G, k-tý prvek |
| [[knowledge/topics/linda-ada|Linda/ADA]] | ~6 | linked list, reverse/delete/search |

## Starší četnosti 2016-2022

- 25x MPI
- 25x PRAM tipsport
- 12x Etour/suffixsum
- 10x Broadcast FIFO/kauzalita/atomičnost
- 9x OCCAM
- 9x Carry-look-ahead
- 6x synchronizace asynchronního systému, koruna
- 6x Pi-kalkul
- 6x Monitor/wait/signal
- 5x Test-and-set
- 5x Pipeline Merge Sort
- 4x Random mating
- 4x Linda
- 4x Prescan
- 4x zřetězené procesy/MISD
- 4x Enumeration sort
- 4x VLIW

## Kontrola proti sjednoceným termínům

Po sjednocení archivu má [[knowledge/exams/00-index|archiv termínů]] 30 samostatných termínových souborů. Následující čísla nejsou náhrada ručních četností výše; jsou to počty odkazů na topic poznámky v aktuální knowledge bázi. Slouží jako sanity check, že ROI plán odpovídá i tomu, co je skutečně prolinkované v termínech.

| Téma | Odkazy v termínech |
|---|---:|
| [[knowledge/topics/pram-tipovacka|PRAM tipovačka]] | 57 |
| [[knowledge/topics/mpi-reduce-bcast|MPI Reduce/Bcast]] | 53 |
| [[knowledge/topics/distribuovane-algoritmy|Distribuované algoritmy]] | 53 |
| [[knowledge/topics/razeni-prefix|Řazení/prefix]] | 38 |
| [[knowledge/topics/architektury|Architektury]] | 36 |
| [[knowledge/topics/broadcast-fifo-kauzalita|Broadcast/FIFO/kauzalita]] | 35 |
| [[knowledge/topics/euler-tour-suffix-sums|Euler tour + suffix sums]] | 30 |
| [[knowledge/topics/pi-kalkul|Pi-kalkul]] | 26 |
| [[knowledge/topics/synchronizace-monitory-semafory|Monitory/semafory]] | 24 |
| [[knowledge/topics/occam|OCCAM]] | 19 |
| [[knowledge/topics/cla|CLA]] | 14 |
| [[knowledge/topics/mutual-exclusion|Test-and-set/Peterson]] | 12 |
| [[knowledge/topics/linda-ada|Linda/ADA]] | 10 |
| [[knowledge/topics/parallel-splitting-select|Parallel splitting/SELECT]] | 8 |

## Praktický závěr

- **Nejlepší ROI:** MPI, PRAM, Broadcast.
- **Nejlepší druhá vlna:** Řazení/prefix, Euler tour, synchronizace, architektury.
- **Bodově užitečné doplnění:** Pi-kalkul, CLA, OCCAM, distribuované algoritmy.
- **Až po základu:** mutual exclusion, parallel splitting/SELECT, Linda/ADA.
