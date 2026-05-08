# 2023/2024 - řádný termín - varianta A

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2023/2024 |
| Termínový label | řádný termín |
| Typ | řádný termín |
| Varianta | A |
| Forma | text + obrázky |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `shoda` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2023-2024]] |
| Primární zdroj zadání | raw text + raw obrázek |

## Student doc reference

- [[knowledge/sources/student-doc/2023-2024-extract]] potvrzuje text varianty A.
- Porovnávací digest: [[knowledge/exams/2023-2024/student-doc-digest]]

## Původní zdroje

- Textový zdroj: [[raw/term_1_2023_a]]
- Obrázek: [[raw/term_1_2023_a_img1.webp]]
- Kopie obrázku ve vaultu: ![[knowledge/assets/term_1_2023_a_img1.webp]]

## Tématické odkazy

- [[knowledge/topics/pram-tipovacka|PRAM tipovačka]]
- [[knowledge/topics/architektury|Zřetězené procesory]]
- [[knowledge/topics/synchronizace-monitory-semafory|Monitor]]
- [[knowledge/topics/euler-tour-suffix-sums|Suffix sums a level(v)]]
- [[knowledge/topics/distribuovane-algoritmy|Bagrodia/Bagródia Rendezvous algoritmus]]
- [[knowledge/topics/razeni-prefix|Pipeline Merge Sort]]
- [[knowledge/topics/pi-kalkul|Pi-kalkul]]
- [[knowledge/topics/mpi-reduce-bcast|MPI]]

## Mapování na témata

Pořadí odpovídá pořadí bodů v jednotném zadání; u zkrácených zadání je mapování orientační.

| Otázka | Téma | Signál v zadání |
|---:|---|---|
| 1 | [[knowledge/topics/pram-tipovacka]] | PRAM tipovačka |
| 2 | [[knowledge/topics/architektury]] | Zřetězené procesory |
| 3 | [[knowledge/topics/synchronizace-monitory-semafory]] | Monitor |
| 4 | [[knowledge/topics/euler-tour-suffix-sums]] | Suffix sums a level(v) |
| 5 | [[knowledge/topics/distribuovane-algoritmy]] | Bagrodia/Bagródia Rendezvous algoritmus |
| 6 | [[knowledge/topics/razeni-prefix]] | Pipeline Merge Sort |
| 7 | [[knowledge/topics/pi-kalkul]] | Pi-kalkul |
| 8 | [[knowledge/topics/mpi-reduce-bcast]] | MPI |

## Jednotné zadání

1. PRAM Tipsport: OR, zda je posloupnost monotónní, zda je v poli čísel nula.
2. Popsat princip zřetězených procesorů.
3. Popsat monitor včetně `signal`, `wait` a nákresu.
4. K dispozici je funkce na výpočet sumy suffixu a příkaz `if e je dopredna then do ...`; popsat algoritmus pro výpočet úrovně vrcholu, pseudokód, slovní popis a časovou složitost.
5. Demonstrujte Bagrodiův algoritmus pro Rendezvous procesů. Na začátku drží procesy tokeny podle obrázku vlevo. Proces je vyznačen obdélníkem s mizející výplní, protože procesy jsou v kontextu, dokud neučiní komunikaci. Všechny procesy při vstupu do kontextu mají zájem komunikovat se všemi ostatními. Volí procesy podle umístění tokenů ve frontě; na obrázku je čelo fronty tokenů vlevo. Pokud proces obdrží nový token, zařadí jej do fronty. Doba zaslání zprávy je jedna časová jednotka. Pokud proces chce zaslat zprávu po vstupu do kontextu, zašle ji okamžitě. Proces, který odpovídá na přijatou zprávu nebo hledá nového partnera, odpoví se zpožděním jedné časové jednotky. Pokud se proces ve stejný okamžik chystá odeslat zprávu a zároveň zprávu přijímá, nejprve zprávu odešle a pak zpracuje přijatou zprávu. Priority procesů jsou vzestupně `P1 > P2 > ... > P5` a partnery procesy volí podle umístění tokenů ve frontě. Pokud procesy naváží komunikaci, opustí kontext a už se do něj nevrací. Uveďte, které procesy budou komunikovat a jak budou procesy držet tokeny po ukončení komunikace.
   - Přepis počátečních tokenů podle obrázku:
     - `P1`: `1,4`, `1,5`, `1,2`
     - `P2`: `2,3`
     - `P3`: `1,3`, `3,5`
     - `P4`: `3,4`, `2,4`
     - `P5`: `2,5`, `4,5`
6. Pipeline Merge Sort - stav po 10 krocích.
7. Pi-kalkul.
8. MPI - proces má v proměnné `value` svoji hodnotu. Pomocí `Reduce` a `Bcast` implementovat výpočet: vytisknout `sum(liché hodnoty) * sum(sudé hodnoty)`.

## Rozdíly / doplnění ze student_doc

- Viz sekce `Stav verifikace` a `Student doc reference`; detailní roční porovnání je v [[knowledge/exams/_verification/raw-vs-student-doc]].

## Poznámky k nejistotám

- Obrázek k příkladu 5 je částečně perspektivně zkreslený; přesné časové diagramy je vhodné kontrolovat proti raw obrázku.
