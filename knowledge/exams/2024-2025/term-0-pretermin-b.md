# 2024/2025 - předtermín - varianta B

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2024/2025 |
| Termínový label | předtermín |
| Typ | předtermín |
| Varianta | B |
| Forma | text |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `discord only` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2024-2025]] |
| Primární zdroj zadání | raw text |

## Student doc reference

- Nenalezeno ve studentském dokumentu.
- Existující studentský předtermín [[knowledge/exams/2024-2025/term-0-pretermin]] má jiné body, proto je tento přepis veden samostatně.

## Původní zdroje

- Textový zdroj: [[raw/term_0_2024_b]]
- JSON export: [[raw/discord/2025/621775635722928128.json]]
- Audit nálezu: [[raw/discord-analysis/exam-leak-audit-2026-05-09]]

## Discord reference

| Role | Message ID | Čas | Autor |
|---|---|---|---|
| hlavní přepis | `1371213632301568040` | `2025-05-11T19:53:25.858+00:00` | `michal3441` |
| kontext varianty | `1371440040315584532` | `2025-05-12T10:53:05.735+00:00` | `dalicon` |
| kontext varianty | `1371444998431572020` | `2025-05-12T11:12:47.842+00:00` | `orangesyrek` |

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u Discord rekonstrukce je mapování orientační.

| Otázka | Signál v zadání | Topic |
|---:|---|---|
| 1 | EREW/CREW tipovačka | [[knowledge/topics/pram-tipovacka]] |
| 2 | Zřetězené procesory a konflikty | [[knowledge/topics/architektury]] |
| 3 | Random mating | [[knowledge/topics/distribuovane-algoritmy]] |
| 4 | Select / k-tý prvek | [[knowledge/topics/parallel-splitting-select]] |
| 5 | Pipeline Merge Sort | [[knowledge/topics/razeni-prefix]] |
| 6 | OCCAM cyklus s datovými linkami | [[knowledge/topics/occam]] |
| 7 | MPI rozdíl průměrů levé a pravé části | [[knowledge/topics/mpi-reduce-bcast]] |
| 8 | Kauzální všesměrové vysílání | [[knowledge/topics/broadcast-fifo-kauzalita]] |

## Jednotné zadání

1. EREW/CREW tipovačka: vybrat složitost algoritmu.
2. Definovat, jak fungují zřetězené procesory a jaké konflikty mohou nastat.
3. Random mating: navrhnout pseudonáhodné generování M/F tokenů tak, aby algoritmus skončil po 4 iteracích.
4. Select pro výběr k-tého prvku: popsat a ukázat na příkladu.
5. Pipeline Merge Sort: stav po 11 krocích.
6. OCCAM: cyklus `(0,3)` se čtyřmi datovými linkami, signály začátku/ukončení komunikace nebo kruhovým přenosem indexu, potvrzením o poslání zprávy a přeposláním dat.
7. MPI: výpočet rozdílu aritmetických průměrů levé a pravé části pole s 32 prvky.
8. Popsat a vysvětlit kauzální všesměrové vysílání.

## Rozdíly / doplnění ze student_doc

- Není ve student docu; zdroj je rekonstrukce z Discord zprávy po předtermínu.
- Studentský dokument obsahuje jiný předtermínový přepis, pravděpodobně jinou variantu.

## Poznámky k nejistotám

- Zdroj není oficiální PDF/fotka zadání.
- Označení `varianta B` je odvozené z okolního Discord kontextu, ne přímo z hlavní zprávy.
- OCCAM bod je ve zdroji zapsaný velmi volně.
