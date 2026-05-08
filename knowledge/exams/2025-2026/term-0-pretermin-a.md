# 2025/2026 - předtermín - varianta A

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2025/2026 |
| Termínový label | předtermín |
| Typ | předtermín |
| Varianta | A |
| Datum v zadání | 6.5.2026 |
| Forma | text + přepsané obrázky |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `raw only` |
| Kontrolní matice | [[exams/_verification/raw-vs-student-doc#2025-2026]] |
| Primární zdroj zadání | raw text + raw obrázky |

## Student doc reference

- Odpovídající sekce ve studentském dokumentu zatím nenalezena.

## Původní zdroje

- Textový zdroj: [[raw/term_0_2026_a]]
- Obrázky: [[raw/term_0_2026_img1.webp]], [[raw/term_0_2026_img2.webp]], [[raw/term_0_2026_img3.webp]], [[raw/term_0_2026_img4.webp]]
- Kopie obrázků ve vaultu: ![[knowledge/assets/term_0_2026_img1.webp]] ![[knowledge/assets/term_0_2026_img2.webp]] ![[knowledge/assets/term_0_2026_img3.webp]] ![[knowledge/assets/term_0_2026_img4.webp]]

## Tématické odkazy

- [[topics/pram-tipovacka|PRAM tipovačka]]
- [[topics/broadcast-fifo-kauzalita|Kauzální broadcast a relace kauzality]]
- [[topics/synchronizace-monitory-semafory|Monitor, wait, signal]]
- [[topics/euler-tour-suffix-sums|Euler tour, suffix sums, level(v)]]
- Distribuovaná volba lídra po výpadcích
- [[topics/razeni-prefix|Pipeline Merge Sort]]
- [[topics/occam|OCCAM]]
- [[topics/mpi-reduce-bcast|MPI Reduce/Bcast]]

## Jednotné zadání

1. **PRAM tipovačka, 6 b.** Odpovědi pro příklady I-III se vybírají z možností: a) konstantní, b) logaritmická, c) `n log n`, d) lineární, e) kvadratická, f) polynomiální.
   - I. Mějme výpočetní model PRAM s `N` procesory. Jaká bude cena optimálního algoritmu, který spočte OR prvků `1/0` v posloupnosti `n` prvků (`n = N`) pro EREW PRAM, CREW PRAM a common CRCW PRAM?
   - II. Mějme výpočetní model PRAM s `N` procesory. Jaká bude časová složitost optimálního algoritmu, který spočte negaci NOT prvků `1/0` v posloupnosti `n` prvků (`n = N`) pro EREW PRAM, CREW PRAM a common CRCW PRAM?
   - III. Mějme výpočetní model PRAM s `N` procesory. Jaká bude časová složitost optimálního algoritmu, který zjistí, zda posloupnost `n` prvků (`n = N`) obsahuje pouze nuly, pro EREW PRAM, CREW PRAM a common CRCW PRAM?
2. **Kauzální všesměrové vysílání, 9 b.** Popište, jak je vysílána a přijímána zpráva při kauzálním všesměrovém vysílání. Dále uveďte, jak je definována relace kauzality.
3. **Monitor, 9 b.** Vysvětlete princip synchronizačního nástroje Monitor, zejména instrukce `signal` a `wait`. Ilustrujte obrázkem.
4. **Euler tour + suffix sums, 9 b.** Demonstrujte operaci nad stromem s použitím funkce sumy suffixů `SuffixS(hrany, ohodnocení)`. Pokud máte výsledek Eulerova průchodu stromem ve struktuře `Etour` a umíte provést podmíněný příkaz `if e je dopredna then ...` podle toho, zda hrana `e` je dopředná, jak lze spočítat úroveň vrcholů pro zobrazení `level(v) -> N`? Uveďte algoritmus, krátký slovní popis principu a časovou složitost celého výpočtu.
5. **Detektor lídra, 9 b.** Perfektní detektor lídra hlídá čtyři procesy v taktech 1-14. K selhání či obnově dochází na začátku taktu, detektor změnu zpracuje a určí nového lídra do konce téhož taktu. Koncem taktu začíná nová epocha definovaná jako `(rank lídra, pořadové číslo jeho vlády)`. Lídrem je vždy živý proces s nejvyšší prioritou, kde Rank 1 je nejvyšší a Rank 4 nejnižší. Podle přiloženého grafu identifikujte a chronologicky vypište všechny epochy.
   - Přepis grafu dostupnosti:
     - `P1`: živý v intervalech přibližně `1-3`, `5-8`, `10-12`.
     - `P2`: živý v intervalech přibližně `1-2`, `11-14`.
     - `P3`: živý v intervalech přibližně `1-6`, `7-12`.
     - `P4`: živý v intervalech přibližně `1-4`, `5-14`.
6. **Pipeline Merge Sort, 9 b.** Uvažujte řadicí algoritmus Pipeline Merge Sort. Pro vstupní posloupnost `5, 2, 9, 4, 3, 6, 8, 7`, která je zpracovávána zprava, zapište hodnoty na vstupech/výstupech procesů po 10. kroku. Hodnota `7` je na začátku kroku 1 na vstupu `P1` a první krok ji přepošle na patřičné místo. Procesy řadí hodnoty tak, že ze dvou vybírají menší jako první.
7. **OCCAM, 9 b.** Definujte nekonečnou proceduru `SMOOTH_VAL`, která čte z kanálu `DATA` hodnoty typu `INT`. Procedura počítá aritmetický průměr z právě přijaté hodnoty a hodnoty předchozí; pro první přijaté číslo se jako předchozí použije defaultní hodnota 0. Výsledek se odesílá na kanál `AVG`. Pokud vypočítaný průměr překročí prahovou hodnotu čtenou z kanálu `LIMIT` (výchozí limit je 100), procedura odešle příznak `TRUE` na výstupní kanál `WARN`.
8. **MPI, 10 b.** Naprogramujte v C++/MPI algoritmus s logaritmickou časovou složitostí, který určí, zda je maximum v posloupnosti přirozených čísel beze zbytku dělitelné minimem této posloupnosti.
   - Vstup: každý procesor má svou hodnotu v proměnné `value`, celkový počet procesorů v `numprocs` a svůj rank v `rank`.
   - Funkce: k dispozici jsou zjednodušené `MPI_Bcast(adresa, root)` a `MPI_Reduce(send, recv, operace, root)`.
   - Výstup: výsledek `ANO/NE` vypíše pouze proces s rankem 0.

## Rozdíly / doplnění ze student_doc

- Viz sekce `Stav verifikace` a `Student doc reference`; detailní roční porovnání je v [[exams/_verification/raw-vs-student-doc]].

## Poznámky k nejistotám

- Původní krátký textový soubor obsahoval jen zkrácený seznam; zde je doplněn přesnější přepis ze čtyř obrázků.
- Intervaly v grafu u příkladu 5 jsou přepsané vizuálně; před řešením je vhodné zkontrolovat proti obrázku.
