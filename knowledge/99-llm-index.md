# LLM index

Tahle stránka je navigační mapa pro rychlé vyhledávání a odpovídání nad bází.

## Základní pravidlo

Odpovídej primárně z vaultu. Externí zdroje používej až když ve vaultu chybí potřebný kontext nebo když uživatel výslovně chce ověření mimo repozitář.

Priorita zdrojů:

1. `knowledge/topics/*.md` pro destilované znalosti, postupy a odpovědní šablony.
2. `knowledge/exams/**/term-*.md` pro konkrétní historická zadání.
3. `knowledge/exams/_verification/raw-vs-student-doc.md` pro jistotu, rozpory a původ zdroje.
4. `knowledge/sources/slides/*.md` pro oficiální výklad, definice, algoritmy, diagramové stránky a složitosti.
5. `raw/*.md`, `raw/*.webp`, `raw/*.pdf` a `raw/*.odp` pro původní materiál.
6. `knowledge/sources/student-doc/` pro rozsekaný studentský dokument.

## Nejrychlejší vstupy

- [[knowledge/00-rozcestnik|Lidský rozcestník]]
- [[knowledge/01-roi-plan|ROI plán učení]]
- [[knowledge/06-must-know|Must-know tahák]]
- [[knowledge/07-predikce-radny-2025-2026|Predikce řádného termínu 2025/2026]]
- [[knowledge/08-pretermin-vs-radny|Předtermín vs řádný termín]]
- [[knowledge/02-cetnosti-temat|Četnosti témat]]
- [[knowledge/04-checklist-nejcastejsi-temata|Checklist nejčastějších témat]]
- [[knowledge/topics/00-index|Topic index]]
- [[knowledge/visuals/00-index|Vizualizace]]
- [[knowledge/practice/00-index|Cvičné testy]]
- [[knowledge/sources/slides/00-index|Oficiální slidy]]
- [[knowledge/05-vyhledavani|Vyhledávání]]
- [[knowledge/exams/00-index|Archiv minulých termínů]]
- [[knowledge/exams/_verification/raw-vs-student-doc|Raw vs student doc]]

## Odpovědní postup

1. Najdi topic poznámku v `knowledge/topics/`.
2. Najdi aspoň jeden historický výskyt v `knowledge/exams/**/term-*.md`.
3. Pokud jde o přesnost zadání, otevři verifikační matici a případně raw zdroj uvedený v termínovém souboru.
4. V odpovědi cituj explicitní vault odkazy ve formátu wikilinku, například `[[knowledge/topics/mpi-reduce-bcast]]` nebo `[[raw/term_1_2022_a]]`.
5. Když je zdroj nejistý, pojmenuj stav: `shoda`, `raw only`, `student_doc only`, nebo `student_doc doplňuje raw`.

## Recepty podle dotazu

- "Vysvětli téma": začni topic poznámkou, přidej minimální odpověď a typické chyby.
- "Co se učit první": použij [[knowledge/01-roi-plan]] a [[knowledge/06-must-know]].
- "Co čekat u řádného termínu": použij [[knowledge/07-predikce-radny-2025-2026]] a [[knowledge/08-pretermin-vs-radny]].
- "Kdy se to objevilo": hledej odkazy na topic v `knowledge/exams/`.
- "Je to jisté / odkud to je": použij [[knowledge/exams/_verification/raw-vs-student-doc]].
- "Co říkají oficiální materiály": začni sekcí `Oficiální slidy` v topic poznámce; pokud nestačí, použij [[knowledge/sources/slides/00-index]] a konkrétní slide extrakt.
- "Chci drill": použij [[knowledge/practice/00-index]] a mini-drilly v topic poznámkách.

## Topic poznámky

- [[knowledge/topics/mpi-reduce-bcast|MPI Reduce/Bcast]]
- [[knowledge/topics/pram-tipovacka|PRAM tipovačka]]
- [[knowledge/topics/broadcast-fifo-kauzalita|Broadcast, FIFO, kauzalita, ABCAST]]
- [[knowledge/topics/razeni-prefix|Řazení, prescan, prefix/suffix]]
- [[knowledge/topics/euler-tour-suffix-sums|Euler tour a suffix sums]]
- [[knowledge/topics/synchronizace-monitory-semafory|Monitory a semafory]]
- [[knowledge/topics/architektury|Architektury]]
- [[knowledge/topics/distribuovane-algoritmy|Distribuované algoritmy]]
- [[knowledge/topics/pi-kalkul|Pi-kalkul]]
- [[knowledge/topics/cla|Carry-look-ahead adder]]
- [[knowledge/topics/occam|OCCAM]]
- [[knowledge/topics/mutual-exclusion|Mutual exclusion]]
- [[knowledge/topics/parallel-splitting-select|Parallel splitting / SELECT]]
- [[knowledge/topics/linda-ada|Linda / ADA]]

## Užitečné dotazy pro agenta

```sh
rg -n "PRAM|CRCW|EREW" knowledge raw
rg -n "MPI|Reduce|Bcast" knowledge/exams knowledge/topics
rg -n "\\[\\[knowledge/topics/pram-tipovacka" knowledge/exams
rg -n "\\[\\[knowledge/topics/mpi-reduce-bcast" knowledge/exams
rg -n "Termínový label|Jednotné zadání|Mapování na témata" knowledge/exams
rg -n "Verifikační status|raw only|student_doc only|student_doc doplňuje raw|shoda" knowledge/exams knowledge/exams/_verification
```

## Kde co leží

- `knowledge/topics/`: destilované znalosti a šablony odpovědí.
- `knowledge/06-must-know.md`: nejkratší opakovací tahák s odpovědními kostrami pro témata s nejlepším ROI.
- `knowledge/07-predikce-radny-2025-2026.md`: predikční matice pro řádný termín 2025/2026.
- `knowledge/08-pretermin-vs-radny.md`: podpůrná analýza rozdílů mezi předtermíny a řádnými termíny.
- `knowledge/practice/`: predikční cvičné testy sestavené podle historie zadání.
- `knowledge/sources/slides/`: automaticky extrahované oficiální slidy po stránkách.
- `knowledge/05-vyhledavani.md`: poznámka k webovému full-text search.
- `knowledge/exams/<rok>/`: sjednocené minulé termíny po akademických letech.
- `knowledge/exams/_verification/`: audit shody mezi raw termíny a student docem.
- `knowledge/sources/student-doc/`: rozsekaný studentský dokument podle let.
- `raw/`: původní zdroje, včetně webp obrázků.

## Odpovědní politika

- Pro učení používej nejdřív topic poznámky a ROI plán.
- Pro ověření teorie používej oficiální slidy, ale u diagramových stran vždy kontroluj raw PDF.
- Pro dotazy typu “kdy se to objevilo” používej archiv termínů.
- Pro dotazy typu “je to jisté” používej verifikační matici.
- Když odpovídáš z více zdrojů, uveď konkrétní soubory a preferuj jeden topic + jeden minulý termín.
- Když uživatel chce zkouškovou odpověď, piš krátce: definice, algoritmus/postup, složitost nebo vlastnost, typická past.
- Když jsou zdroje v rozporu, nevyhlašuj vítěze bez raw kontroly.
- Neodkazuj na `*.txt`; raw texty jsou převedené na `*.md`.
