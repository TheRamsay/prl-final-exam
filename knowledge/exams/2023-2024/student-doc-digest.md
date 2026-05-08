# 2023/2024 - student doc digest

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2023/2024 |
| Zdroj | studentský dokument |
| Stav | porovnávací digest |
| Auditovatelný extract | [[sources/student-doc/2023-2024-extract]] |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | porovnávací zdroj pro raw termíny |
| Kontrolní matice | [[exams/_verification/raw-vs-student-doc#2023-2024]] |

## Původní zdroje

- Raw dokument: [raw/student_doc.md](../../../raw/student_doc.md)
- Očištěný zdroj: [[sources/student-doc/clean]]
- Extract roku: [[sources/student-doc/2023-2024-extract]]

## Přehled

Tento blok se výrazně překrývá s ručně sesbíranými soubory v `raw/term_0_2023.txt`, `raw/term_1_2023_*.txt` a `raw/term_2_2023.txt`. Nezakládal jsem podle něj nové primární termíny; slouží jako kontrolní zdroj a doplňuje placeholdery obrázků v původním studentském dokumentu.

## Sekce ve student doc

### Term 0 - předtermín

Odpovídá [[exams/2023-2024/term-0-pretermin]].

1. [[topics/pram-tipovacka|Tipsport CRCW]] - XOR, NAND, AND.
2. [[topics/pram-tipovacka|PRAM model]] - popsat a nakreslit.
3. [[topics/broadcast-fifo-kauzalita|Kauzální broadcast + relace kauzality]].
4. [[topics/euler-tour-suffix-sums|Euler pro počet následovníků]] + popis.
5. [[topics/cla|CLA]].
6. [[topics/distribuovane-algoritmy|Maekawa]] - kvórum, zalomená kvóra pro 12 procesů.
7. [[topics/occam|OCCAM]] - queue, `input`, `clk`, `OUT_LEFT`, `OUT_RIGHT`.
8. [[topics/mpi-reduce-bcast|MPI]] - `value - average(values)`.

### Term 1 - řádný A/B

Odpovídá [[exams/2023-2024/term-1-radny-a]] a [[exams/2023-2024/term-1-radny-b]]. Student doc obsahuje skupinu B dvakrát, jednou s placeholdery `[obrazek: image1]` až `[obrazek: image4]`.

Opakující se skupina B:

1. PRAM: XOR čas, počet sudých čas, NAND cena.
2. [[topics/architektury|VLIW]].
3. [[topics/synchronizace-monitory-semafory|Čtenáři/písaři]] se semafory, přednost čtenářů.
4. [[topics/euler-tour-suffix-sums|Euler + suffix sums]] pro `preor(v) -> N`.
5. Rendezvous podle obrázku.
6. [[topics/razeni-prefix|Enumeration Sort]] po 6 krocích.
7. [[topics/pi-kalkul|Pi-kalkul]] - alespoň 4 koncové redukce.
8. [[topics/mpi-reduce-bcast|MPI]] - součet prvků větších než průměr.

Skupina A:

1. PRAM Tipsport: OR, monotónnost, nula v poli.
2. [[topics/architektury|Zřetězené procesory]].
3. [[topics/synchronizace-monitory-semafory|Monitor]].
4. [[topics/euler-tour-suffix-sums|Suffix sums pro level(v)]].
5. Rendezvous.
6. [[topics/razeni-prefix|Pipeline Merge Sort]] po 10 krocích.
7. [[topics/pi-kalkul|Pi-kalkul]].
8. [[topics/mpi-reduce-bcast|MPI]] - součet lichých krát součet sudých.

### Term 2 - 1. opravný

Odpovídá [[exams/2023-2024/term-2-prvni-opravny]].

1. PRAM: cena řazení, cena XOR, čas AND.
2. FIFO broadcast `send/recv`, relace kauzality.
3. Test-and-set pro KS.
4. Algoritmus čtyř čítačů.
5. Ricart-Agrawala + Lamportovy časy.
6. Random mating.
7. Pi-kalkul.
8. MPI: druhý nejmenší prvek.

## Poznámky

- Primární strukturované soubory pro 2023/2024 už existují; tento digest je hlavně kontrolní a odkazový.
- Obrázky ze student doc nejsou v `clean.md` extrahované jako soubory, jen jako placeholdery.
