# 2023/2024 - 2. opravný termín

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2023/2024 |
| Termínový label | 2. opravný termín |
| Typ | 2. opravný termín |
| Varianta | nezadaná |
| Forma | text |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `discord only` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2023-2024]] |
| Primární zdroj zadání | raw text |

## Student doc reference

- Nenalezeno ve studentském dokumentu.

## Původní zdroje

- Textový zdroj: [[raw/term_3_2023]]
- JSON export: [[raw/discord/2024/621775635722928128.json]]
- Kontextová analýza: [[raw/discord-analysis/broadcast-fifo-kauzalita]]

## Discord reference

| Role | Message ID | Čas | Autor |
|---|---|---|---|
| hlavní přepis | `1247167970506051594` | `2024-06-03T12:40:15.429+00:00` | `yamauu` |
| potvrzení PRAM | `1247179584214925343` | `2024-06-03T13:26:24.353+00:00` | `martet` |
| potvrzení Linda | `1247179624803467283` | `2024-06-03T13:26:34.030+00:00` | `martet` |

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u Discord rekonstrukce je mapování orientační.

| Otázka | Signál v zadání | Topic |
|---:|---|---|
| 1 | PRAM sázka | [[knowledge/topics/pram-tipovacka]] |
| 2 | Parallel splitting | [[knowledge/topics/parallel-splitting-select]] |
| 3 | Suffix sum na stromě | [[knowledge/topics/euler-tour-suffix-sums]] |
| 4 | ADA select/accept a synchronizace | [[knowledge/topics/linda-ada]] |
| 5 | Broadcast: FIFO, kauzalita, atomicita | [[knowledge/topics/broadcast-fifo-kauzalita]] |
| 6 | Random mating | [[knowledge/topics/distribuovane-algoritmy]] |
| 7 | Linda reverse listu | [[knowledge/topics/linda-ada]] |
| 8 | MPI odečíst průměr | [[knowledge/topics/mpi-reduce-bcast]] |

## Jednotné zadání

1. PRAM sázka:
   - cena výpočtu absolutních hodnot posloupnosti kladných čísel;
   - časová složitost OR;
   - cena zjištění, jestli je posloupnost Fibonacciho sekvence.
2. Parallel splitting.
3. Suffix sum na stromě: algoritmus a popsat postup.
4. ADA: k čemu se používá `select` a `accept`, co se používá na synchronizaci.
5. Broadcast: FIFO, kauzalita a atomicita na diagramu.
6. Random mating.
7. Linda: reverse listu daného jako čtveřice `(jmeno_seznamu, ID, hodnota, next_ID)`, první prvek jako dvojice `(jmeno_seznamu, ID)`.
8. MPI: odečíst od každého prvku průměr všech prvků.

## Rozdíly / doplnění ze student_doc

- Není ve student docu; zdroj je rekonstrukce z Discord zprávy po termínu.

## Poznámky k nejistotám

- Zdroj není oficiální PDF/fotka zadání.
- Otázka 5 zmiňuje diagram, ale diagram není dostupný.
- Podoba PRAM podotázky "Fibonacciho sekvence" je převzatá z Discordu; raw přepis ponechává původní pravopisnou variantu `fibonnaciho`.
- PRAM a Linda body byly krátce poté potvrzeny další Discord zprávou.
