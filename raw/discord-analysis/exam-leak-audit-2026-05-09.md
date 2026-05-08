# Discord exam leak audit 2026-05-09

## Scope

Audit všech `raw/discord/*/621775635722928128.json` exportů se zaměřením na celé nebo skoro celé seznamy zadání. Cíl: najít termíny, které nejsou v `knowledge/exams/**/term-*.md`, a odlišit je od duplicit, predikcí a běžné diskuze.

## Metoda

- Kandidáti: zprávy s více očíslovanými body, slovy `předtermín`, `řádný`, `opravný`, `skupina`, `zadání`, `zkouška`, nebo vysokou hustotou PRL témat.
- Kontrola proti archivu: `knowledge/exams/**/term-*.md`, roční `00-index.md`, `knowledge/exams/_verification/raw-vs-student-doc.md`, raw termy `raw/term_*.md`.
- Rokování: kalendářní květen/červen zprávy odpovídá akademickému roku `YYYY-1/YYYY`. Např. zprávy z května 2025 jsou akademický rok 2024/2025.

## Shrnutí

| Stav | Počet | Poznámka |
|---|---:|---|
| Doplněno do archivu | 2 | Oba nálezy jsou z akademického roku 2024/2025. |
| Potenciální konflikt s existujícím zápisem | 1 | 2022/2023 řádný B, otázka 6. |
| Pokryté / duplicity | více | 2020/2021, 2021/2022, 2022/2023 opravné, 2023/2024, 2025/2026 předtermín. |
| Nezkoušková nebo mimo rozsah | 1 hlavní | `Polsemka` z 2020; není normalizovaná jako finální zkouškový termín. |

## Doplněno do archivu

### 2024/2025 - předtermín, další varianta nebo konfliktní předtermínový přepis

Zdrojová zpráva:

- Message ID `1371213632301568040`, `2025-05-11T19:53:25.858+00:00`, `michal3441`, `raw/discord/2025/621775635722928128.json`
- Text začíná `Toto inac bolo na predtermine`.

Normalizované soubory:

- [[raw/term_0_2024_b]]
- [[knowledge/exams/2024-2025/term-0-pretermin-b]]

Přepis témat:

1. EREW/CREW tipovačka.
2. Zřetězené procesory a konflikty.
3. Random mating, volba M/F tokenů tak, aby skončil do 4 iterací.
4. Select pro výběr k-tého prvku.
5. Pipeline Merge Sort po 11 krocích.
6. OCCAM cyklus s datovými linkami a potvrzováním/posíláním dat.
7. MPI: rozdíl aritmetických průměrů levé a pravé části pole s 32 prvky.
8. Kauzální všesměrové vysílání.

Ověření proti archivu:

- V `knowledge/exams/2024-2025/term-0-pretermin.md` už předtermín existuje, ale má jiné body: PRAM NOT/OR/>0, zřetězení, koruna, parallel splitting, Euler, Enumeration Sort, OCCAM `data/ctrl/out[5]`, MPI normalizace.
- Zprávy `1371440040315584532` (`2025-05-12T10:53:05.735+00:00`, `dalicon`) a `1371444998431572020` (`2025-05-12T11:12:47.842+00:00`, `orangesyrek`) zmiňují rozdíl v zadání a skupinu B, takže nejde spolehlivě sloučit do jediného existujícího předtermínu.

Závěr: vysoká pravděpodobnost, že pro 2024/2025 předtermín máme jen jednu variantu a Discord zachycuje druhou variantu nebo konfliktní přepis.

### 2024/2025 - pravděpodobně 1. opravný termín

Zdrojové zprávy:

- Message ID `1377277331391123546`, `2025-05-28T13:28:24.379+00:00`, `maxersk`
- Message ID `1377277568310313013`, `2025-05-28T13:29:20.865+00:00`, `maxersk`
- Message ID `1377278331656863776`, `2025-05-28T13:32:22.861+00:00`, `omegapatyk`, editováno `2025-05-28T13:34:04.718+00:00`
- Message ID `1377278632397115503`, `2025-05-28T13:33:34.563+00:00`, `maxersk`
- Message ID `1377286239593562254`, `2025-05-28T14:03:48.260+00:00`, `matej6396`

Normalizované soubory:

- [[raw/term_2_2024]]
- [[knowledge/exams/2024-2025/term-2-prvni-opravny]]

Přepis témat:

1. PRAM tipovačka; další zpráva zmiňuje AND a součty.
2. FIFO broadcast + relace kauzality; další zpráva doplňuje, že šlo o napsání algoritmů.
3. Čtyři čítače.
4. Čtenáři/písaři.
5. `Balgoriuv alg` / pravděpodobně Barodingův algoritmus nebo podobný distribuovaný algoritmus.
6. Prescan / upsweep-downsweep v poli.
7. OCCAM.
8. MPI: podle doplňujících zpráv určit, jestli je průměr blíž k minimu nebo maximu; jedna zpráva formuluje “které číslo posloupnosti je blíže k min a které k max”.

Ověření proti archivu:

- Před normalizací obsahoval `knowledge/exams/2024-2025/00-index.md` jen předtermín a digest.
- Před normalizací v repo nebyl žádný `term-1-radny*`, `term-2-prvni-opravny*` ani raw `term_*_2024.md` pro akademický rok 2024/2025.
- Kontext: zpráva `1376539456651133039` (`2025-05-26T12:36:21.332+00:00`, `eniacx64`) se ptá na registraci na první opravný; zpráva `1376849229963591761` (`2025-05-27T09:07:17.045+00:00`, `marosnip`) se ptá, co bylo na řádném termínu; 2025-05-28 po poledni přichází seznam zadání. Nejpravděpodobnější label je tedy `1. opravný termín`, ale samotná zpráva ho explicitně nepojmenovává.

Závěr: vysoká pravděpodobnost chybějícího termínu, ale label `1. opravný termín` je odvozený z kontextu.

## Potenciální konflikt, ne nový termín

### 2022/2023 - řádný termín B, otázka 6

Zdrojová zpráva:

- `2023-05-15T11:14:37.051+00:00`, `rebel_svk`

Discord přepis pro skupinu B:

1. PRAM Synotip.
2. Xeon.
3. Bounded test-and-set.
4. Enumeration Sort.
5. Pi-kalkul.
6. `Nejaký stromovy algoritmus suffix či čo`.
7. Kvórum.
8. MPI poměr lichých a sudých.

Archiv:

- `knowledge/exams/2022-2023/term-1-radny-b.md` má otázku 6 jako Marzullův algoritmus a otázku 7 jako Kvórum.
- `knowledge/exams/2022-2023/student-doc-digest.md` odpovídá archivní verzi.

Závěr: nejde o nový termín, ale je tu slabý konflikt mezi Discord zprávou a student_doc. Vzhledem k formulaci `či čo` a tomu, že student_doc i digest jsou konzistentní, ponechat jako nízkou důvěru.

## Pokryté kandidáty

| Discord datum | Kandidát | Stav v archivu |
|---|---|---|
| 2020-06-08 | `Test` po `Polsemka`, témata PRAM/zřetězení/producent-konzument/Euler/Broadcast/Prescan/Linda/MPI | Odpovídá `knowledge/exams/2019-2020/term-1-radny-b.md`. |
| 2021-05-10 | PRAM/test-and-set/kauzalita/Euler/RA/CLA/MPI | Odpovídá `knowledge/exams/2020-2021/term-1-radny-zkratka.md`. |
| 2021-05-25 | “min rok 1. opravny” PRAM/Xeon/Odd-even/Marzullo/CLA/semafor/LINDA/MPI | Odpovídá `knowledge/exams/2019-2020/term-2-prvni-opravny.md`. |
| 2021-05-26 | 1. opravný PRAM architektura/Pi/Random/Suzuki/Monitor/Linda/MPI | Odpovídá `knowledge/exams/2020-2021/term-2-prvni-opravny.md`. |
| 2021-06-09 | PRAM/VLIW/Monitor/filozofové/FIFO/Random/OCCAM/MPI | Odpovídá `knowledge/exams/2020-2021/term-3-druhy-opravny.md`. |
| 2022-05-16 | Skupina B a C 2021/2022 | Pokryto v `knowledge/exams/2021-2022/term-1-radny-b.md` a `term-1-radny-c.md`. |
| 2023-05-03 | 2022/2023 předtermín | Pokryto v `knowledge/exams/2022-2023/term-0-pretermin.md`. |
| 2023-05-15 | 2022/2023 řádné varianty | Pokryto v `knowledge/exams/2022-2023/term-1-radny-*.md`, s výše uvedenou nízkodůvěrovou poznámkou pro B. |
| 2023-05-29 | 2022/2023 1. opravný | Pokryto v `knowledge/exams/2022-2023/term-2-prvni-opravny.md`. |
| 2023-06-05 | 2022/2023 2. opravný | Pokryto v `knowledge/exams/2022-2023/term-3-druhy-opravny.md`. |
| 2024-04-24 až 2024-06-03 | 2023/2024 předtermín, řádné A/B/C, 1. opravný, 2. opravný | Pokryto v `knowledge/exams/2023-2024/term-*.md`, včetně nově přidaného `term-3-druhy-opravny`. |
| 2026-05-06 | 2025/2026 předtermín A/B | Pokryto v `knowledge/exams/2025-2026/term-0-pretermin-a.md` a částečně v `term-0-pretermin-b.md`; Discord potvrzuje B body 2, 3 a 6. |

## Mimo hlavní exam archiv

### 2020-06-08 `Polsemka`

Zdrojová zpráva `2020-06-08T16:58:12.17+00:00` obsahuje i sekci `Polsemka`:

1. Úplné propojení, topologie 6 uzlů, diagram, konektivita, bisekce.
2. Které dvojice algoritmů jsou optimální: Pipeline Merge, Odd-even transposition, Odd-even merge.
3. PRAM: sdílené/lokální paměti.
4. Popis redukčních počítačů.

Tohle není v `knowledge/exams` jako finální zkouškový termín. Pokud chceme archivovat i půlsemestrální testy/semestrálky, je to samostatná kategorie.

## Doporučený další krok

1. Zvážit, jestli existující [[knowledge/exams/2024-2025/term-0-pretermin]] přeznačit na variantu A nebo ho nechat jako studentský neoznačený předtermín.
2. Volitelně založit sekci pro `Polsemka` mimo `knowledge/exams`, pokud chceme sledovat i průběžné písemky.
