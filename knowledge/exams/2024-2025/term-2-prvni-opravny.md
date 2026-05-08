# 2024/2025 - 1. opravný termín

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2024/2025 |
| Termínový label | 1. opravný termín |
| Typ | 1. opravný termín |
| Varianta | nezadaná |
| Forma | text |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `discord only` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2024-2025]] |
| Primární zdroj zadání | raw text |

## Student doc reference

- Nenalezeno ve studentském dokumentu.

## Původní zdroje

- Textový zdroj: [[raw/term_2_2024]]
- JSON export: [[raw/discord/2025/621775635722928128.json]]
- Audit nálezu: [[raw/discord-analysis/exam-leak-audit-2026-05-09]]

## Discord reference

| Role | Message ID | Čas | Autor |
|---|---|---|---|
| kontext termínu | `1376539456651133039` | `2025-05-26T12:36:21.332+00:00` | `eniacx64` |
| kontext termínu | `1376849229963591761` | `2025-05-27T09:07:17.045+00:00` | `marosnip` |
| dílčí přepis | `1377277331391123546` | `2025-05-28T13:28:24.379+00:00` | `maxersk` |
| dílčí přepis | `1377277568310313013` | `2025-05-28T13:29:20.865+00:00` | `maxersk` |
| hlavní přepis | `1377278331656863776` | `2025-05-28T13:32:22.861+00:00` | `omegapatyk` |
| doplnění FIFO | `1377278632397115503` | `2025-05-28T13:33:34.563+00:00` | `maxersk` |
| doplnění MPI | `1377286239593562254` | `2025-05-28T14:03:48.260+00:00` | `matej6396` |

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u Discord rekonstrukce je mapování orientační.

| Otázka | Signál v zadání | Topic |
|---:|---|---|
| 1 | PRAM tipovačka | [[knowledge/topics/pram-tipovacka]] |
| 2 | FIFO broadcast + relace kauzality | [[knowledge/topics/broadcast-fifo-kauzalita]] |
| 3 | Čtyři čítače | [[knowledge/topics/distribuovane-algoritmy]] |
| 4 | Čtenáři/písaři | [[knowledge/topics/synchronizace-monitory-semafory]] |
| 5 | Balgoriův algoritmus | [[knowledge/topics/distribuovane-algoritmy]] |
| 6 | Prescan / upsweep-downsweep v poli | [[knowledge/topics/razeni-prefix]] |
| 7 | OCCAM | [[knowledge/topics/occam]] |
| 8 | MPI průměr vůči min/max | [[knowledge/topics/mpi-reduce-bcast]] |

## Jednotné zadání

1. PRAM tipovačka; ve zdroji dodatečně zmíněné AND a součty.
2. FIFO broadcast + relace kauzality; podle doplňující zprávy napsat algoritmy.
3. Čtyři čítače.
4. Čtenáři/písaři: více čtenářů a jeden zapisovač, udržet prioritu čtenářů.
5. Balgoriův algoritmus.
6. Prescan / upsweep-downsweep v poli.
7. OCCAM.
8. MPI: určit, jestli je průměr blíže k minimu nebo maximu; jedna zpráva zmiňuje i čísla posloupnosti, která jsou blíže k minimu a maximu.

## Rozdíly / doplnění ze student_doc

- Není ve student docu; zdroj je rekonstrukce z Discord zpráv po termínu.

## Poznámky k nejistotám

- Zdroj není oficiální PDF/fotka zadání.
- Label `1. opravný termín` je odvozený z okolního Discord kontextu.
- Bod 5 je ve zdroji zapsaný jako `Balgoriuv alg`; ponechávám věcně opatrně jako `Balgoriův algoritmus`.
- MPI bod má dvě blízké formulace z různých zpráv.
