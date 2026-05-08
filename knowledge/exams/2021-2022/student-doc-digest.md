# 2021/2022 - student doc digest

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2021/2022 |
| Zdroj | studentský dokument |
| Stav | první destilace |
| Auditovatelný extract | [[sources/student-doc/2021-2022-extract]] |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | mix `student_doc doplňuje raw` a `student_doc only` |
| Kontrolní matice | [[exams/_verification/raw-vs-student-doc#2021-2022]] |

## Původní zdroje

- Raw dokument: [raw/student_doc.md](../../../raw/student_doc.md)
- Očištěný zdroj: [[sources/student-doc/clean]]
- Extract roku: [[sources/student-doc/2021-2022-extract]]

## Přehled termínů

### Term 1 - řádný termín - skupina A

1. [[topics/pram-tipovacka|PRAM tipovačka]].
2. [[topics/mutual-exclusion|Test-and-set]].
   - Řešení ve zdroji zdůrazňuje atomickou instrukci, sdílený `lock`, busy waiting a odemčení po opuštění KS.
3. [[topics/euler-tour-suffix-sums|Etour + suffix sum]] - určit úroveň uzlu ve stromu.
4. [[topics/razeni-prefix|Pipeline Merge Sort]].
   - Zdroj připomíná `p(n)=log n + 1`, procesor `Pi` spojuje dvě seřazené posloupnosti délky `2^(i-2)`, čas `O(n)`, cena `O(n log n)`.
5. [[topics/architektury|Zřetězené procesory / MISD]].
6. [[topics/broadcast-fifo-kauzalita|Asynchronní komunikace na synchronní]] - rozhodnout, zda je převod možný.
7. [[topics/occam|OCCAM]] - buffer, overflow nebo hodnota `0`, výstup na `high/low` podle thresholdu.
8. [[topics/mpi-reduce-bcast|MPI]] - zřejmě `sum % max == 0` nebo `sum % min == 0`, stačí 2x `Reduce`.

### Term 1 - řádný termín - skupina B

1. [[topics/pram-tipovacka|PRAM tipsport]].
2. [[topics/architektury|Vektorové procesory SIMD]] - výhody, nevýhody, obrázek UMA/NUMA.
3. [[topics/parallel-splitting-select|Paralelní SELECT k-tého prvku]].
   - Zdroj uvádí EREW PRAM, sdílené pole, `t(n)=O(n/N)` pro omezený počet procesorů, cena `O(n)`.
4. [[topics/mutual-exclusion|Petersonův algoritmus]] - princip a pseudokód.
5. Synchronizace.
6. [[topics/razeni-prefix|Enumeration Sort]] - napsat registry `X, Y, C, Z` po skončení algoritmu.
7. [[topics/occam|OCCAM]] - pole 10 kanálů, vstupy `adr`, `in`; hodnoty z `in` posílat na aktuální kanál, `adr` posouvá index modulo 10.
8. [[topics/mpi-reduce-bcast|MPI]] - pokud `max % min == 0`, vypsat `Ano`, jinak `Ne`.

### Term 1 - řádný termín - skupina C

1. [[topics/pram-tipovacka|PRAM tipsport extraliga]].
2. Xeon Phi - kombinace SIMD + MIMD.
3. [[topics/euler-tour-suffix-sums|Etour + suffixsum]] - zjistit počet následujících vrcholů ve stromě, princip a časová náročnost.
   - Zdroj uvádí kroky: spočítání `Etour`, inicializace `weight`, suffix sums `O(log n)`, korekce výsledku.
4. [[topics/synchronizace-monitory-semafory|Monitor]] - popis, `wait`, `signal`, obrázek.
5. [[topics/broadcast-fifo-kauzalita|Asynchronní signály -> synchronní provedení]].
   - Zdroj: hledat korunu; pokud koruna existuje, systém nelze provést synchronně.
6. [[topics/razeni-prefix|Prescan]] - zapsat jako pole, vědět, které pozice se přepisují.
7. [[topics/occam|OCCAM]] - kanály `1-10`, vstupy `adr` a `in`; `adr` nastaví aktivní index, `in` posílá na aktivní kanál.
8. [[topics/mpi-reduce-bcast|MPI]] - počet prvků rovných maximu a počet prvků rovných minimu v logaritmickém čase.

### Term 2 - 1. opravný - skupina A

Samostatný soubor: [[term-2-prvni-opravny-a]]

1. [[topics/pram-tipovacka|CRCW AND]] - popsat algoritmus a uvést příklad.
2. [[topics/architektury|MIMD / Xeon Phi]] - kde využít, popis a obrázek.
3. [[topics/euler-tour-suffix-sums|Suffixsum pro Euler path]] - výpočet úrovně vrcholu.
   - Váhy: dopředná hrana `-1`, zpětná `+1`, suffix sum, korekce přes dopředné hrany.
4. [[topics/razeni-prefix|Pipeline sort]] - stav procesorů ve 12. kroku.
5. [[topics/broadcast-fifo-kauzalita|Async -> sync, koruna, kauzalita]].
   - Zdroj uvádí příklad koruny velikosti 4 a definici kauzální relace.
6. FIFO algoritmy - ve zdroji zmíněn Lamport a Ricart-Agrawala.
7. [[topics/occam|OCCAM]] - kanály `ls`, `gt`, `in`, vstupní `BYTE th`, buffer velikosti `SIZE`, poslat podle `x <= th` nebo `x > th`.
8. [[topics/mpi-reduce-bcast|MPI]] - zjistit, zda suma prvků v první polovině je menší než suma ve druhé.

### Term 2 - 1. opravný - skupina B

Samostatný soubor: [[term-2-prvni-opravny-b]]

1. [[topics/pram-tipovacka|Common CRCW AND]] - princip a příklad.
2. Xeon Phi - kombinace SIMD/MIMD, 512bitové vektorové registry.
3. [[topics/razeni-prefix|Odd-even merge sort]] - popis + síť 4x4 z CE prvků.
4. [[topics/distribuovane-algoritmy|Marzullův algoritmus]].
5. [[topics/broadcast-fifo-kauzalita|Async -> sync]] - detekce koruny a zprávy, které brání synchronizaci.
6. [[topics/razeni-prefix|Enumeration Sort]].
7. [[topics/occam|OCCAM]] - `OUT[10]`, `IN`, `ALT`; `ALT` zapíná/vypíná alternování mezi kanály.
8. [[topics/mpi-reduce-bcast|MPI]] - sudé procesory mají sudé prvky a liché procesory liché prvky.

### Term 3 - 2. opravný termín

Samostatný soubor: [[term-3-druhy-opravny]]

1. [[topics/pram-tipovacka|PRAM tipovačka]].
2. [[topics/architektury|Dataflow architektura]] - popsat + obrázek.
3. [[topics/synchronizace-monitory-semafory|Semafor]] - popsat operace `P` a `V`.
4. [[topics/broadcast-fifo-kauzalita|FIFO broadcast]] - přijímání, odesílání a algoritmy.
5. Async -> sync příklad.
6. Random mating - skončit první fázi do 4 kroků.
7. [[topics/linda-ada|Linda]] - vyhledávání v lineárním seznamu.
8. [[topics/mpi-reduce-bcast|MPI]] - najít druhé maximum, pozor na záporné hodnoty.

## Využitelné řešicí poznámky

- Test-and-set, Peterson, monitor, Marzullo, suffix sums a několik MPI šablon jsou ve zdroji částečně vypracované.
- U OCCAM úloh jsou zadání cennější než řešení; řešení jsou často jen nástřely.
- U async -> sync se opakuje motiv koruny, tj. důležité pro [[topics/broadcast-fifo-kauzalita]].
