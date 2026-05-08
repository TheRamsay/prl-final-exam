# Četnosti témat

Zdroj: `raw/common_latest.txt` a `raw/common_16-22.txt`.

## Aktualizovaný odhad

| Téma | Odhad četnosti | Typické varianty |
|---|---:|---|
| [MPI Reduce/Bcast](topics/mpi-reduce-bcast.md) | ~35 | průměr, min/max, počet prvků, normalizace, součet podle podmínky, druhé min/max |
| [PRAM tipovačka](topics/pram-tipovacka.md) | ~27 | EREW/CREW/common CRCW, AND/OR/XOR/NAND, max/min, monotónnost, nuly/sudá |
| [Broadcast/FIFO/kauzalita](topics/broadcast-fifo-kauzalita.md) | ~26 | FIFO broadcast, kauzální relace, porušení FIFO/kauzality/atomicity, koruna |
| [Architektury](topics/architektury.md) | ~26 | VLIW, zřetězení/MISD, dataflow, SIMD/MIMD, Xeon Phi, PRAM, sítě |
| [Řazení/prefix](topics/razeni-prefix.md) | ~25 | Pipeline Merge Sort, Enumeration Sort, Prescan, Odd-even |
| [Monitory/semafory](topics/synchronizace-monitory-semafory.md) | ~17 | wait/signal, monitor ze semaforů, readers-writers, producer-consumer |
| [Distribuované algoritmy](topics/distribuovane-algoritmy.md) | ~16 | Marzullo, Maekawa, Suzuki, Dijkstra, Hirschberg-Sinclair |
| [Euler tour + suffix sums](topics/euler-tour-suffix-sums.md) | ~15 | preorder, level/depth, následovníci, Etour |
| Random mating/list ranking/terminace | ~15 | random mating do 4 kroků, reconstruction, 4-counter termination |
| [Pi-kalkul](topics/pi-kalkul.md) | ~14 | 3 až 4 možné redukce, koncové výrazy |
| [CLA](topics/cla.md) | ~14 | propagate/stop/generate, carries přes scan |
| [OCCAM](topics/occam.md) | ~13 | kanály, pole kanálů, queue/buffer, alternace |
| [Test-and-set/Peterson](topics/mutual-exclusion.md) | ~8 | aktivní čekání, bounded TAS, starvation |
| [Parallel splitting/SELECT](topics/parallel-splitting-select.md) | ~6 | pivot, L/E/G, k-tý prvek |
| [Linda/ADA](topics/linda-ada.md) | ~6 | linked list, reverse/delete/search |

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

Po sjednocení archivu má [[exams/00-index|archiv termínů]] 30 samostatných termínových souborů. Následující čísla nejsou náhrada ručních četností výše; jsou to počty odkazů na topic poznámky v aktuální knowledge bázi. Slouží jako sanity check, že ROI plán odpovídá i tomu, co je skutečně prolinkované v termínech.

| Téma | Odkazy v termínech |
|---|---:|
| [PRAM tipovačka](topics/pram-tipovacka.md) | 30 |
| [MPI Reduce/Bcast](topics/mpi-reduce-bcast.md) | 28 |
| [Řazení/prefix](topics/razeni-prefix.md) | 20 |
| [Euler tour + suffix sums](topics/euler-tour-suffix-sums.md) | 16 |
| [Broadcast/FIFO/kauzalita](topics/broadcast-fifo-kauzalita.md) | 16 |
| [Pi-kalkul](topics/pi-kalkul.md) | 14 |
| [Monitory/semafory](topics/synchronizace-monitory-semafory.md) | 12 |
| [Distribuované algoritmy](topics/distribuovane-algoritmy.md) | 11 |
| [OCCAM](topics/occam.md) | 10 |
| [Architektury](topics/architektury.md) | 10 |
| [Test-and-set/Peterson](topics/mutual-exclusion.md) | 7 |
| [CLA](topics/cla.md) | 7 |
| [Linda/ADA](topics/linda-ada.md) | 5 |
| [Parallel splitting/SELECT](topics/parallel-splitting-select.md) | 4 |

## Praktický závěr

- **Nejlepší ROI:** MPI, PRAM, Broadcast.
- **Nejlepší druhá vlna:** Řazení/prefix, Euler tour, synchronizace, architektury.
- **Bodově užitečné doplnění:** Pi-kalkul, CLA, OCCAM, distribuované algoritmy.
- **Až po základu:** mutual exclusion, parallel splitting/SELECT, Linda/ADA.
