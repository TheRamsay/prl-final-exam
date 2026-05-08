# ROI plán učení

Tenhle plán je optimalizovaný na zisk bodů, ne na úplné pokrytí předmětu. Vychází ze zdrojů `raw/common_latest.md`, `raw/common_16-22.md` a z 30 sjednocených souborů v [[exams/00-index|archivu termínů]].

## Jak číst priority

- **A0**: naučit jako první. Téma se opakuje skoro pořád nebo tvoří rychle získatelné body.
- **A1**: vysoká návratnost. Často bodově silné, ale vyžaduje přesnější postup.
- **B**: pravidelně padá, ale až po zvládnutí A0/A1.
- **C**: doplněk pro lepší pokrytí variant.

## A0: nejrychlejší body

| Téma | ROI | Proč první | Minimální cíl |
|---|---:|---|---|
| [MPI Reduce/Bcast](topics/mpi-reduce-bcast.md) | velmi vysoké | V `common_latest` ~35 výskytů; v termínových souborech 28 odkazů. Typicky poslední úloha za 9-10 bodů. | Umět napsat šablonu `Reduce`, `Bcast`, průměr, min/max, filtr podle podmínky. |
| [PRAM tipovačka](topics/pram-tipovacka.md) | velmi vysoké | V `common_latest` ~27 výskytů; v termínových souborech 30 odkazů. Často první příklad a dá se řešit rychle. | Umět EREW/CREW/common CRCW pro AND/OR/XOR/NAND, monotónnost, počet, min/max. |
| [Broadcast/FIFO/kauzalita](topics/broadcast-fifo-kauzalita.md) | vysoké | V `common_latest` ~26 výskytů; v termínových souborech 16 odkazů. Padá jako teorie, pseudokód i diagram. | Umět FIFO broadcast, kauzální relaci, ABCAST/atomicitu, synchronizovatelnost a korunu. |

## A1: velké opakující se bloky

| Téma | ROI | Proč | Minimální cíl |
|---|---:|---|---|
| [Řazení, prescan, prefix](topics/razeni-prefix.md) | vysoké | V `common_latest` ~25 výskytů; v termínových souborech 20 odkazů. Často konkrétní simulace po N krocích. | Umět Pipeline Merge Sort, Enumeration Sort, Prescan, Odd-even transposition/merge. |
| [Euler tour + suffix sums](topics/euler-tour-suffix-sums.md) | vysoké | V `common_latest` ~15 výskytů; v termínových souborech 16 odkazů. Otázky se hodně recyklují. | Umět `preorder(v)`, `level(v)`, počet potomků, převod hrany -> vrcholy, složitost. |
| [Monitory a semafory](topics/synchronizace-monitory-semafory.md) | vysoké | V `common_latest` ~17 výskytů; v termínových souborech 12 odkazů. Časté kreslení/pseudokód. | Umět `wait/signal`, monitor, semafor `P/V`, readers-writers, producer-consumer. |
| [Architektury](topics/architektury.md) | střední až vysoké | V `common_latest` ~26 výskytů; v termínových souborech 10 odkazů. Široké téma, často teoretické body. | Umět VLIW, zřetězení/MISD, Dataflow, SIMD/MIMD, Xeon Phi, PRAM model, sítě. |

## B: pravidelná druhá vlna

| Téma | ROI | Minimální cíl |
|---|---:|---|
| [Distribuované algoritmy](topics/distribuovane-algoritmy.md) | střední | Marzullo, Maekawa, Suzuki, Ricart-Agrawala, Dijkstra, Hirschberg-Sinclair, volba lídra. |
| [Pi-kalkul](topics/pi-kalkul.md) | střední | Redukce výrazů, 3-4 možné koncové redukce, pozorování. |
| [Carry-look-ahead adder](topics/cla.md) | střední | `propagate/generate/stop`, výpočet carry pomocí scan, sečtení dvojice čísel. |
| [OCCAM](topics/occam.md) | střední | Kanály, pole kanálů, buffer/queue, alternace, jednoduchý proces. |
| Random mating / list ranking / terminace | střední | Simulace random mating, list ranking, 4 čítače terminace. |

## C: doplnit po základu

| Téma | ROI | Minimální cíl |
|---|---:|---|
| [Test-and-set, swap, Peterson](topics/mutual-exclusion.md) | nižší, ale opakuje se | Aktivní čekání, bounded TAS, starvation, Peterson. |
| [Parallel splitting / SELECT](topics/parallel-splitting-select.md) | nižší | Rozdělení podle pivotu `L/E/G`, výběr k-tého prvku. |
| [Linda / ADA](topics/linda-ada.md) | nižší | Základní operace nad n-ticí/listem, reverse/delete/search. |

## Doporučené pořadí

1. **První průchod: A0.** MPI, PRAM, Broadcast. Cíl je umět okamžitě napsat kostru odpovědi bez přemýšlení.
2. **Druhý průchod: A1.** Řazení/prescan, Euler tour, synchronizace, architektury. Cíl je umět postup a typické chyby.
3. **Třetí průchod: B.** Distribuované algoritmy, Pi-kalkul, CLA, OCCAM, random/list/terminace.
4. **Poslední průchod: termíny.** Otevřít [[exams/00-index|minulé termíny]] a u každé otázky si nahlas říct, do kterého tématu patří a jaká je šablona řešení.

## Co nedělat první

- Nezačínat okrajovými jazyky a jednorázovými příklady, dokud neumíš MPI/PRAM/Broadcast.
- Neučit se architektury jako dlouhý text bez kresby a bez 3-4 vět, které by šly napsat do zkoušky.
- Nesimulovat řazení “od oka”; u těchto úloh je lepší trénovat tabulku kroků.

## Rychlý denní plán

| Blok | Čas | Obsah | Výstup |
|---|---:|---|---|
| 1 | 60-90 min | MPI + PRAM | 5 hotových minišablon |
| 2 | 60-90 min | Broadcast + synchronizace | definice + 2 pseudokódy |
| 3 | 90 min | Řazení/prescan + Euler | 2 ručně odsimulované příklady |
| 4 | 60 min | Architektury + distribuované algoritmy | krátké odpovědi na papír |
| 5 | 60 min | Pi-kalkul + CLA + OCCAM | po jednom typickém řešení |

## Navazující checklist

- [[04-checklist-nejcastejsi-temata|Checklist nejčastějších témat]]
- [[02-cetnosti-temat|Četnosti témat]]
- [[exams/00-index|Minulé termíny]]
