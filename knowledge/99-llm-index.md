# LLM index

Tahle stránka je navigační mapa pro rychlé vyhledávání a odpovídání nad bází.

## Nejrychlejší vstupy

- [[knowledge/00-rozcestnik|Lidský rozcestník]]
- [[knowledge/01-roi-plan|ROI plán učení]]
- [[knowledge/02-cetnosti-temat|Četnosti témat]]
- [[knowledge/04-checklist-nejcastejsi-temata|Checklist nejčastějších témat]]
- [[knowledge/topics/00-index|Topic index]]
- [[knowledge/visuals/00-index|Vizualizace]]
- [[knowledge/practice/00-index|Cvičné testy]]
- [[knowledge/exams/00-index|Archiv minulých termínů]]
- [[knowledge/exams/_verification/raw-vs-student-doc|Raw vs student doc]]

## Jak hledat odpověď

1. Najdi téma v `knowledge/topics/`.
2. Najdi výskyty tématu v minulých termínech přes odkazy na topic poznámku.
3. Zkontroluj verifikační matici, jestli je zdroj `shoda`, `raw only`, `student_doc only`, nebo `student_doc doplňuje raw`.
4. Pokud je potřeba přesné zadání, otevři raw zdroj z termínového souboru.

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
rg -n "Termínový label|Jednotné zadání|Tématické odkazy" knowledge/exams
rg -n "Verifikační status|raw only|student_doc only|shoda" knowledge/exams
```

## Kde co leží

- `knowledge/topics/`: destilované znalosti a šablony odpovědí.
- `knowledge/practice/`: predikční cvičné testy sestavené podle historie zadání.
- `knowledge/exams/<rok>/`: sjednocené minulé termíny po akademických letech.
- `knowledge/exams/_verification/`: audit shody mezi raw termíny a student docem.
- `knowledge/sources/student-doc/`: rozsekaný studentský dokument podle let.
- `raw/`: původní zdroje, včetně webp obrázků.

## Odpovědní politika

- Pro učení používej nejdřív topic poznámky a ROI plán.
- Pro dotazy typu “kdy se to objevilo” používej archiv termínů.
- Pro dotazy typu “je to jisté” používej verifikační matici.
- Když odpovídáš z více zdrojů, uveď konkrétní soubory.
- Neodkazuj na `*.txt`; raw texty jsou převedené na `*.md`.
