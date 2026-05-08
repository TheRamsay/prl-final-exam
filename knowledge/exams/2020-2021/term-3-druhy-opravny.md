# 2020/2021 - 2. opravný termín

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2020/2021 |
| Termínový label | 2. opravný termín |
| Typ | 2. opravný termín |
| Varianta | nezadaná |
| Forma | krátká studentská poznámka |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc doplňuje raw` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2020-2021]] |
| Primární zdroj zadání | raw poznámka; student doc potvrzuje a přidává řešení |

## Student doc reference

- [[knowledge/sources/student-doc/2020-2021-extract]] obsahuje odpovídající 2. opravný termín s dílčími řešeními.
- Destilace: [[knowledge/exams/2020-2021/student-doc-digest]]

## Původní zdroje

- Textový zdroj: [[raw/term_3_2020]]

## Tématické odkazy

- [[knowledge/topics/pram-tipovacka|PRAM]]
- [[knowledge/topics/architektury|VLIW]]
- [[knowledge/topics/synchronizace-monitory-semafory|Monitor a semafory]]
- [[knowledge/topics/synchronizace-monitory-semafory|Pět filozofů]]
- [[knowledge/topics/broadcast-fifo-kauzalita|FIFO/broadcast]]
- [[knowledge/topics/distribuovane-algoritmy|Random mating]]
- [[knowledge/topics/occam|OCCAM]]
- [[knowledge/topics/mpi-reduce-bcast|MPI]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Téma | Signál v zadání |
|---:|---|---|
| 1 | [[knowledge/topics/pram-tipovacka|PRAM]] | PRAM |
| 2 | [[knowledge/topics/architektury|VLIW]] | VLIW |
| 3 | [[knowledge/topics/synchronizace-monitory-semafory|Monitor a semafory]] | Monitor a semafory |
| 4 | [[knowledge/topics/synchronizace-monitory-semafory|Pět filozofů]] | Pět filozofů |
| 5 | [[knowledge/topics/broadcast-fifo-kauzalita|FIFO/broadcast]] | FIFO/broadcast |
| 6 | [[knowledge/topics/distribuovane-algoritmy|Random mating]] | Random mating |
| 7 | [[knowledge/topics/occam|OCCAM]] | OCCAM |
| 8 | [[knowledge/topics/mpi-reduce-bcast|MPI]] | MPI |

## Jednotné zadání

1. PRAM tipovačka.
2. VLIW a jak se řeší konflikty.
3. Monitor: popis a obrázek.
4. Problém pěti filozofů: kód se semafory a popis, řešení musí být deadlock-proof.
5. Něco s FIFO a broadcastem, tabulka.
6. Random mating.
7. OCCAM: procedura `AVG` se třemi kanály typu `BYTE`: `DATA`, `CHNH`, `CHNL`. Procedura bere čísla z `DATA`, počítá dlouhodobý průměr a podle toho, zda je číslo větší nebo menší než průměr, ho pošle na příslušný kanál.
8. MPI: spočítat součet hodnot menších než maximum nebo větších než minimum.

## Rozdíly / doplnění ze student_doc

- Viz sekce `Stav verifikace` a `Student doc reference`; detailní roční porovnání je v [[knowledge/exams/_verification/raw-vs-student-doc]].

## Poznámky k nejistotám

- Zdroj je jen stručný seznam témat.
