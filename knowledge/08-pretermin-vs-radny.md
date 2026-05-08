# Předtermín vs řádný termín

Tenhle soubor je podpůrná analýza pro [[knowledge/07-predikce-radny-2025-2026|predikci řádného termínu 2025/2026]]. Cíl není dokazovat přesné pravděpodobnosti, ale odlišit stabilní řádný-termínový pattern od předtermínového šumu.

## Vstupní vzorek

| Typ | Počet souborů | Poznámka |
|---|---:|---|
| řádný termín | 15 | většinou plné varianty A/B/C |
| předtermín | 5 | zahrnuje fragment [[knowledge/exams/2025-2026/term-0-pretermin-b]] |
| opravné termíny | mimo tuhle analýzu | pro aktuální cíl méně důležité |

## Stabilita slotů v řádných termínech

| Slot | Nejčastější řádný pattern | Síla signálu |
|---:|---|---|
| Q1 | [[knowledge/topics/pram-tipovacka]] | velmi silná: 15/15 řádných variant |
| Q2 | [[knowledge/topics/architektury]] | silná: 11/15 |
| Q3 | [[knowledge/topics/synchronizace-monitory-semafory]] | střední: 5/15, další jsou Euler/řazení/splitting |
| Q4 | [[knowledge/topics/euler-tour-suffix-sums]] | silná: 6/15, často se střídá s distribuovanými algoritmy |
| Q5 | [[knowledge/topics/pi-kalkul]] nebo [[knowledge/topics/distribuovane-algoritmy]] | střední: 5/15 vs 4/15 |
| Q6 | [[knowledge/topics/razeni-prefix]] | silná: 7/15 |
| Q7 | [[knowledge/topics/cla]], [[knowledge/topics/pi-kalkul]], [[knowledge/topics/occam]], distribuované algoritmy | slabší: proměnlivý doplňkový slot |
| Q8 | [[knowledge/topics/mpi-reduce-bcast]] | velmi silná: 14/15 jako Q8, 15/15 celkově |

## Předtermínový pattern

Předtermíny drží jen dvě velmi stabilní věci:

- Q1 často [[knowledge/topics/pram-tipovacka|PRAM]].
- Q8 bývá [[knowledge/topics/mpi-reduce-bcast|MPI]], pokud je předtermín plný.

Zbytek je méně pravidelný než u řádných termínů:

| Slot | Předtermínově časté | Praktický závěr |
|---:|---|---|
| Q2 | broadcast/architektury/distribuované | nebrat jako fixní slot |
| Q3 | broadcast, synchronizace, řazení | vyšší šum než u řádného termínu |
| Q4 | Euler | podobné řádným, ale vzorek je malý |
| Q5 | architektury/CLA/Euler/distribuované | bez jasné dominance |
| Q6 | řazení nebo broadcast/distribuované | řazení se opakuje, ale varianty se mění |
| Q7 | často OCCAM | tohle je rozdíl proti řádným, kde je Q7 proměnlivější |

## Co z toho plyne pro řádný 2025/2026

Předtermín 2025/2026 už pokryl:

- [[knowledge/topics/pram-tipovacka|PRAM]]
- [[knowledge/topics/broadcast-fifo-kauzalita|Broadcast/FIFO/kauzalita]]
- [[knowledge/topics/synchronizace-monitory-semafory|Monitor]]
- [[knowledge/topics/euler-tour-suffix-sums|Euler level]]
- [[knowledge/topics/distribuovane-algoritmy|volba lídra / detekce ukončení]]
- [[knowledge/topics/razeni-prefix|Pipeline Merge Sort / Enumeration Sort]]
- [[knowledge/topics/occam|OCCAM]]
- [[knowledge/topics/mpi-reduce-bcast|MPI]]

To neznamená, že tato témata v řádném nebudou. U PRAM a MPI by takový závěr byl špatný, protože jsou strukturálně stabilní. Rozumnější čtení je:

- **PRAM/MPI ignorovat nejde**, i když už byly.
- **Architektury jsou po předtermínu podezřele volné**, hlavně protože řádný Q2 historicky často patří architekturám.
- **Pi-kalkul a CLA jsou dobré kandidáty na návrat**, protože v předtermínu 2025/2026 nebyly a v řádných termínech se vrací.
- **Řazení/prefix čekat, ale jinou variantu než předtermín**, tedy spíš Prescan nebo Odd-even.
- **Distribuované algoritmy čekat, ale jiný algoritmus než leader/termination**, tedy Maekawa, Ricart-Agrawala, Suzuki, Marzullo nebo Random mating.

## Řádný termín není jen těžší předtermín

Historicky řádné termíny působí šablonovitěji:

1. začátek PRAM,
2. brzy architektura,
3. uprostřed synchronizace/Euler/distribuované,
4. jedna simulační úloha z řazení/prefixu,
5. jeden formální/jazykový nebo aritmetický doplněk,
6. konec MPI.

Předtermín je užitečný jako signál aktuálních preferencí, ale pro řádný 2025/2026 je lepší učit podle řádného slot patternu.

## Doporučený závěr

Pro řádný 2025/2026 má největší smysl trénovat:

1. [[knowledge/topics/pram-tipovacka|PRAM]] a [[knowledge/topics/mpi-reduce-bcast|MPI]] jako fixní body.
2. [[knowledge/topics/architektury|Architektury]] jako nejsilnější téma, které v předtermínu 2025/2026 chybělo.
3. [[knowledge/topics/euler-tour-suffix-sums|Euler]] a [[knowledge/topics/razeni-prefix|řazení/prefix]] přes jiné varianty než v předtermínu.
4. [[knowledge/topics/pi-kalkul|Pi-kalkul]] a [[knowledge/topics/cla|CLA]] jako návratové kandidáty.
5. [[knowledge/topics/distribuovane-algoritmy|Distribuované algoritmy]] šířeji, ne jen volbu lídra.
