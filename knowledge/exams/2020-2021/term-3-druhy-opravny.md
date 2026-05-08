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

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Signál v zadání | Topic |
|---:|---|---|
| 1 | PRAM | [[knowledge/topics/pram-tipovacka]] |
| 2 | VLIW | [[knowledge/topics/architektury]] |
| 3 | Monitor a semafory | [[knowledge/topics/synchronizace-monitory-semafory]] |
| 4 | Pět filozofů | [[knowledge/topics/synchronizace-monitory-semafory]] |
| 5 | FIFO/broadcast | [[knowledge/topics/broadcast-fifo-kauzalita]] |
| 6 | Random mating | [[knowledge/topics/distribuovane-algoritmy]] |
| 7 | OCCAM | [[knowledge/topics/occam]] |
| 8 | MPI | [[knowledge/topics/mpi-reduce-bcast]] |

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
