# 2023/2024 - 1. opravný termín

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2023/2024 |
| Termínový label | 1. opravný termín |
| Typ | 1. opravný termín |
| Varianta | nezadaná |
| Forma | text |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `shoda` |
| Kontrolní matice | [[exams/_verification/raw-vs-student-doc#2023-2024]] |
| Primární zdroj zadání | raw text |

## Student doc reference

- [[sources/student-doc/2023-2024-extract]] potvrzuje pořadí i témata 1. opravného termínu.
- Porovnávací digest: [[student-doc-digest]]

## Původní zdroje

- Textový zdroj: [raw/term_2_2023.txt](../../../raw/term_2_2023.txt)

## Tématické odkazy

- [[topics/pram-tipovacka|PRAM tipovačka]]
- [[topics/broadcast-fifo-kauzalita|FIFO broadcast a kauzalita]]
- [[topics/mutual-exclusion|Test-and-set]]
- Čtyři čtenáři / detekce ukončení
- Ricart-Agrawala / Lamportovy hodiny
- Random mating
- [[topics/pi-kalkul|Pi-kalkul]]
- [[topics/mpi-reduce-bcast|MPI]]

## Jednotné zadání

1. PRAM, 6 b: pro EREW, CREW, common CRCW určit cenu seřazení sekvence, cenu XOR a časovou složitost AND.
2. FIFO broadcast, 9 b: algoritmus `send` a `recv`; definovat relaci kauzality.
3. Test-and-set, 9 b: řešení kritické sekce, kód a popis.
4. Algoritmus čtyř čtenářů, 9 b: princip fungování a nakreslit 2 obrázky, v jednom se detekovalo ukončení a ve druhém ne.
5. Ricart-Agrawala, 10 b: synchronizace vstupů do CS pro 4 procesy, synchronní čas, počítání logického času událostí. Zpráva má latenci 3 takty, kritická sekce trvá 1 takt, na vstupu a výstupu nastanou 2 abstraktní události, priority procesů: 1 má největší prioritu, v čase 6 žádá proces 4, v čase 7 žádá proces 3. Naznačit komunikaci šipkami, napsat logický čas každé události a logický čas každého procesu po poslední události.
6. Random mating, 9 b: 8 uzlů, vybírat F/M pseudonáhodně tak, aby jumping phase skončila do 4 iterací; nezapomenout reconstruction phase.
7. Pi-kalkul, 9 b: vypsat 3 výrazy, na které lze redukovat.
8. MPI, 9 b: najít druhý nejmenší prvek v logaritmickém čase, lze použít jen `MPI_Bcast` a `MPI_Reduce`.

## Rozdíly / doplnění ze student_doc

- Viz sekce `Stav verifikace` a `Student doc reference`; detailní roční porovnání je v [[exams/_verification/raw-vs-student-doc]].

## Poznámky k nejistotám

- Zdroj je studentský přepis opravného termínu 2024.
