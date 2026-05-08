# 2023/2024 - řádný termín - varianta C

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2023/2024 |
| Termínový label | řádný termín |
| Typ | řádný termín |
| Varianta | C |
| Forma | text + obrázek |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `raw only` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2023-2024]] |
| Primární zdroj zadání | raw text + raw obrázek |

## Student doc reference

- Odpovídající skupina C nebyla v horním bloku studentského dokumentu nalezena.
- Porovnávací digest: [[knowledge/exams/2023-2024/student-doc-digest]]

## Původní zdroje

- Textový zdroj: [[raw/term_1_2023_c]]
- Obrázek: [[raw/term_1_2023_c_img1.webp]]
- Kopie obrázku ve vaultu: ![[knowledge/assets/term_1_2023_c_img1.webp]]

## Tématické odkazy

- [[knowledge/topics/pram-tipovacka|PRAM tipovačka]]
- [[knowledge/topics/architektury|Propojovací síť]]
- [[knowledge/topics/synchronizace-monitory-semafory|Semafor P/V]]
- [[knowledge/topics/euler-tour-suffix-sums|Eulerova cesta]]
- [[knowledge/topics/distribuovane-algoritmy|Barodingův algoritmus]]
- [[knowledge/topics/razeni-prefix|Prescan]]
- [[knowledge/topics/pi-kalkul|Pi-kalkul]]
- [[knowledge/topics/mpi-reduce-bcast|MPI]]

## Jednotné zadání

1. PRAM Tipsport, 6 b: na výběr `const`, `log(n)`, `n`, `n*log(n)`, `n^2`, polynomiální. Pro EREW, CREW a CRCW určit:
   - `t(n)` pro AND v posloupnosti;
   - `c(n)` pro zjištění, zda posloupnost obsahuje jen stejné prvky;
   - `c(n)` pro součet posloupnosti.
2. K čemu se používá propojovací síť, 9 b.
3. Popsat funkci semaforu a napsat algoritmus pro základní funkce `P` a `V`, 9 b.
4. Eulerova cesta na grafu podle obrázku, 9 b.
   - Přepis viditelné části grafu: vrcholy `v1` až `v7`; orientované hrany označené přibližně `e1` až `e12`; viditelné dvojice zahrnují `v1 <-> v2` (`e1/e2`), `v1 <-> v3` (`e3/e4`), `v1 <-> v4` (`e5/e8`), `v4 <-> v5` (`e6/e7`), `v1 <-> v6` (`e9/e12`), `v6 <-> v7` (`e10/e11`).
5. Barodingův algoritmus, 10 b.
6. Prescan v poli, 9 b: pro posloupnost `3, 15, 2, 8, 12, 10, 3, 2, 12, 11, 17, 5, 19, 2, 5, 1` doplnit stav po prvním a posledním kroku up-sweep i down-sweep.
7. Pi-kalkul, 9 b: napsat alespoň 4 výsledné redukce pro zadaný výraz.
8. MPI, 9 b: v logaritmické složitosti udělat algoritmus pro součet prvků posloupnosti, které jsou buď maximum nebo minimum dané posloupnosti. K dispozici jsou `rank`, `numproc`, `value`, `MPI_Bcast(adresa_hodnoty, root)` a `MPI_Reduce(adresa_send, adresa_recv, operace, root)`.

## Rozdíly / doplnění ze student_doc

- Viz sekce `Stav verifikace` a `Student doc reference`; detailní roční porovnání je v [[knowledge/exams/_verification/raw-vs-student-doc]].

## Poznámky k nejistotám

- Hrany v grafu jsou přepsané vizuálně z ručního náčrtu; pro přesné řešení kontrolovat obrázek.
