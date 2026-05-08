# 2025/2026 - řádný termín - cvičná predikce A

## Metadata

| Pole | Hodnota |
|---|---|
| Typ | cvičné zadání |
| Cíl | predikce pro řádný termín 2025/2026 |
| Doporučený limit | 120-150 minut |
| Body | 70 |
| Jistota | vysoká strukturou, střední konkrétními variantami |

## Témata

- [[knowledge/topics/pram-tipovacka|PRAM tipovačka]]
- [[knowledge/topics/architektury|VLIW]]
- [[knowledge/topics/synchronizace-monitory-semafory|Čtenáři/písaři]]
- [[knowledge/topics/euler-tour-suffix-sums|Euler tour a preorder]]
- [[knowledge/topics/distribuovane-algoritmy|Ricart-Agrawala]]
- [[knowledge/topics/razeni-prefix|Enumeration Sort]]
- [[knowledge/topics/pi-kalkul|Pi-kalkul]]
- [[knowledge/topics/mpi-reduce-bcast|MPI Reduce/Bcast]]

## Proč tahle varianta

Tohle je nejpravděpodobnější řádný-termínový tvar: PRAM první, MPI poslední, uprostřed architektura, synchronizace, Euler, distribuovaný algoritmus, řazení a formální jazyk. Je blízká řádným termínům [[knowledge/exams/2023-2024/term-1-radny-b]] a [[knowledge/exams/2023-2024/term-1-radny-c]], ale bere v úvahu i témata z [[knowledge/exams/2025-2026/term-0-pretermin-a]].

## Zadání

1. **PRAM tipovačka, 6 b.** Pro modely EREW PRAM, CREW PRAM a common CRCW PRAM určete časovou složitost `t(n)` a cenu `c(n)` optimálního algoritmu pro:
   - zjištění, zda posloupnost `n` bitů obsahuje alespoň jednu jedničku;
   - zjištění, zda jsou všechny prvky posloupnosti stejné;
   - výpočet XOR všech prvků posloupnosti.

2. **VLIW, 9 b.** Popište architekturu VLIW procesoru. Vysvětlete, jak se plánuje paralelismus instrukcí, jaké vznikají konflikty a jak se jim předchází. Připojte jednoduchý nákres dlouhého instrukčního slova a funkčních jednotek.

3. **Čtenáři/písaři, 9 b.** Navrhněte řešení problému čtenářů a písařů pomocí obecných semaforů tak, aby čtenáři měli přednost. Uveďte inicializaci semaforů, sdílené proměnné a pseudokód pro čtenáře i písaře. Neřešte hladovění písařů.

4. **Euler tour + suffix sums, 9 b.** Máte výsledek Eulerova průchodu stromem `Etour` a pro každou orientovanou hranu umíte zjistit, zda je dopředná. Popište algoritmus pro výpočet preorder čísla `preorder(v)` pro každý vrchol. Uveďte ohodnocení hran, použití prefix/suffix sum a časovou složitost.

5. **Ricart-Agrawala, 10 b.** Čtyři procesy `P1..P4` žádají o vstup do kritické sekce. Proces `P4` žádá v čase 6, proces `P2` v čase 7. Zpráva má latenci 3 takty, kritická sekce trvá 1 takt. Priority při shodném Lamportově čase jsou `P1 > P2 > P3 > P4`. Nakreslete komunikaci request/reply, doplňte Lamportovy časy událostí a určete pořadí vstupu do kritické sekce.

6. **Enumeration Sort, 9 b.** Uvažujte zapojení čtyř procesorů `P1..P4` s registry `X, Y, C, Z`. Vstupní posloupnost `7, 2, 7, 5, 1, 4` je zpracovávaná zprava. Procesory řadí vzestupně a duplicity řeší stabilně podle pořadí vstupu. Zapište obsah registrů po 6. kroku a stručně popište význam registru `C`.

7. **Pi-kalkul, 9 b.** Pro zadaný proces najděte alespoň 4 různé možné redukce do stavu, kde už nelze dále redukovat. U každé redukce uveďte komunikační pár, provedenou substituci a výsledný výraz. Pokud v některém stavu platí pozorování, zapište jej.

```text
(a(x).x<d>.0 + b(y).c<y>.0)
|
(a<c>.0 + c(z).z<e>.0)
|
(new k)(c(k).k<f>.0 | k(u).0)
```

8. **MPI, 10 b.** Každý proces má hodnotu `value`, svůj `rank` a počet procesů `numprocs`. K dispozici jsou zjednodušené funkce `MPI_Reduce(send, recv, operace, root)` a `MPI_Bcast(adresa, root)`. Napište algoritmus v C++/MPI s logaritmickou komunikační složitostí, který na procesu 0 vypíše součet všech prvků větších než průměr všech hodnot.

## Kontrola po dopsání

- PRAM: [[knowledge/topics/pram-tipovacka]]
- VLIW: [[knowledge/topics/architektury#VLIW]]
- Čtenáři/písaři: [[knowledge/topics/synchronizace-monitory-semafory]]
- Euler preorder: [[knowledge/topics/euler-tour-suffix-sums]]
- Ricart-Agrawala: [[knowledge/topics/distribuovane-algoritmy]]
- Enumeration Sort: [[knowledge/visuals/enumeration-sort-ranks]]
- Pi-kalkul: [[knowledge/topics/pi-kalkul]]
- MPI: [[knowledge/topics/mpi-reduce-bcast]]
