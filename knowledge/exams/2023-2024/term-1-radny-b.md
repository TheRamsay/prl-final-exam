# 2023/2024 - řádný termín - varianta B

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2023/2024 |
| Termínový label | řádný termín |
| Typ | řádný termín |
| Varianta | B |
| Forma | text |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc doplňuje raw` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2023-2024]] |
| Primární zdroj zadání | raw text; student doc potvrzuje duplicitu skupiny B |

## Student doc reference

- [[knowledge/sources/student-doc/2023-2024-extract]] obsahuje skupinu B dvakrát a potvrzuje pořadí příkladů.
- Porovnávací digest: [[knowledge/exams/2023-2024/student-doc-digest]]

## Původní zdroje

- Textový zdroj: [[raw/term_1_2023_b]]
- Obrázek k Enumeration Sortu: [[raw/term_1_2023_a_img2.webp]]
- Kopie obrázku ve vaultu: ![[knowledge/assets/term_1_2023_a_img2.webp]]

## Tématické odkazy

- [[knowledge/topics/pram-tipovacka|PRAM tipovačka]]
- [[knowledge/topics/architektury|VLIW]]
- [[knowledge/topics/synchronizace-monitory-semafory|Čtenáři/písaři]]
- [[knowledge/topics/euler-tour-suffix-sums|Euler tour a preorder]]
- [[knowledge/topics/distribuovane-algoritmy|Rendezvous]]
- [[knowledge/topics/razeni-prefix|Enumeration Sort]]
- [[knowledge/topics/pi-kalkul|Pi-kalkul]]
- [[knowledge/topics/mpi-reduce-bcast|MPI]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Téma | Signál v zadání |
|---:|---|---|
| 1 | [[knowledge/topics/pram-tipovacka|PRAM tipovačka]] | PRAM tipovačka |
| 2 | [[knowledge/topics/architektury|VLIW]] | VLIW |
| 3 | [[knowledge/topics/synchronizace-monitory-semafory|Čtenáři/písaři]] | Čtenáři/písaři |
| 4 | [[knowledge/topics/euler-tour-suffix-sums|Euler tour a preorder]] | Euler tour a preorder |
| 5 | [[knowledge/topics/distribuovane-algoritmy|Rendezvous]] | Rendezvous |
| 6 | [[knowledge/topics/razeni-prefix|Enumeration Sort]] | Enumeration Sort |
| 7 | [[knowledge/topics/pi-kalkul|Pi-kalkul]] | Pi-kalkul |
| 8 | [[knowledge/topics/mpi-reduce-bcast|MPI]] | MPI |

## Jednotné zadání

1. PRAM tipovačka, 6 b:
   - časová složitost XOR pro EREW, CREW, common CRCW;
   - časová složitost počtu sudých čísel pro EREW, CREW, common CRCW;
   - cena NAND pro EREW, CREW, common CRCW.
2. VLIW, 9 b: popsat architekturu procesorů s velkým kódovým slovem, možné konflikty a způsoby předcházení nebo řešení; ilustrovat obrázky.
3. Čtenáři/písaři, 9 b: uvést kódy s obecným semaforem tak, aby nedocházelo ke konfliktům ani uváznutí. Varianta s předností čtenářů; neřešit hladovění písařů.
4. Euler tour + suffix sums, 9 b: pro `Etour` a informaci, zda je hrana dopředná, spočítat pořadí vrcholů `preor(v) -> N` při preorder průchodu. Uvést algoritmus, slovní popis principu a časovou složitost.
5. Rendezvous, 10 b: nový příklad podle obrázku.
6. Enumeration Sort, 9 b: vyplnit výsledek po 6 krocích zapojení v řadě.
   - Přepis obrázku: Uvažujte algoritmus Enumeration Sort s topologií uvedenou na obrázku. Pro vstupní posloupnost uvedenou v zadání, zpracovávanou zprava, zapište obsah jednotlivých registrů po 6. kroku. Procesory řadí tak, aby v prvním procesoru bylo uloženo nejmenší číslo. Obrázek má čtyři procesory `P1` až `P4`; každý proces má registry `X`, `Y`, `C`, `Z`; vstup vede shora do všech procesů a data postupují zleva doprava mezi procesory.
7. Pi-kalkul, 9 b: najít alespoň 4 různé redukce do stavu, kde už nelze dále redukovat.
8. MPI, 9 b: vypsat součet prvků větších než průměr, k dispozici `broadcast` a `reduce`.

## Rozdíly / doplnění ze student_doc

- Viz sekce `Stav verifikace` a `Student doc reference`; detailní roční porovnání je v [[knowledge/exams/_verification/raw-vs-student-doc]].

## Poznámky k nejistotám

- Obrázek k Enumeration Sortu je v raw pojmenovaný `term_1_2023_a_img2.webp`, ale obsahově patří k příkladu 6 varianty B. Vstupní posloupnost v horní části obrázku není spolehlivě čitelná.
