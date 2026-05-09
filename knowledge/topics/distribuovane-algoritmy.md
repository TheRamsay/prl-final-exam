# Distribuované algoritmy

## Zkouškový pattern

Tahle stránka je catch-all pro distribuované algoritmy mimo broadcast/ABCAST. V zadání se střídají mutual exclusion algoritmy, synchronizace vstupu do kritické sekce, detekce ukončení, volba lídra, časová synchronizace a menší simulační algoritmy jako Random mating nebo Rendezvous.

## Oficiální slidy

- [[knowledge/sources/slides/distribuovana-synchronizace#Strana 10|Distribuovaná synchronizace, str. 10]] až [[knowledge/sources/slides/distribuovana-synchronizace#Strana 13|str. 13]] - Marzulloův algoritmus.
- [[knowledge/sources/slides/distribuovana-synchronizace#Strana 30|Distribuovaná synchronizace, str. 30]] až [[knowledge/sources/slides/distribuovana-synchronizace#Strana 39|str. 39]] - Lamport a Ricart-Agrawala pro distribuované vzájemné vyloučení.
- [[knowledge/sources/slides/distribuovana-synchronizace#Strana 47|Distribuovaná synchronizace, str. 47]] až [[knowledge/sources/slides/distribuovana-synchronizace#Strana 52|str. 52]] - Maekawa.
- [[knowledge/sources/slides/distribuovana-synchronizace#Strana 84|Distribuovaná synchronizace, str. 84]] až [[knowledge/sources/slides/distribuovana-synchronizace#Strana 94|str. 94]] - Suzuki-Kasami; diagramové kroky kontroluj v [[raw/PRL2526_DISTSYNCH.pdf]].
- [[knowledge/sources/slides/komunikace#Strana 38|Komunikace, str. 38]] až [[knowledge/sources/slides/komunikace#Strana 41|str. 41]] - Bagrodia/rendezvous tokeny a příklady.
- [[knowledge/sources/slides/grafy#Strana 10|Grafy, str. 10]] až [[knowledge/sources/slides/grafy#Strana 15|str. 15]] - Random Mate / Random mating, obě fáze a analýza.
- [[knowledge/sources/slides/grafy#Strana 16|Grafy, str. 16]] až [[knowledge/sources/slides/grafy#Strana 26|str. 26]] - Optimal List Ranking přes Random Mate simulaci.
- [[knowledge/sources/slides/distribuovana-synchronizace#Strana 129|Distribuovaná synchronizace, str. 129]] až [[knowledge/sources/slides/distribuovana-synchronizace#Strana 135|str. 135]] - volba lídra a detektor Ω.

## Maekawa

Vzájemné vyloučení přes kvóra:

- Každý proces má množinu procesů, od kterých žádá povolení.
- Každá dvě kvóra se protínají.
- Proces vstoupí do kritické sekce po získání všech odpovědí ze svého kvóra.

U kreslení pro 12 procesů se často používá zalomená konstrukce kvór. Důležité je ukázat průnik kvór, ne jen nakreslit tabulku.

## Ricart-Agrawala

- Proces při žádosti rozešle request s Lamportovým timestampem.
- Vstoupí do CS po obdržení reply od všech ostatních.
- Při konfliktu rozhoduje menší timestamp, pak priorita/id.
- Po opuštění CS odešle odložené odpovědi.

## Suzuki-Kasami

- Token-based mutual exclusion.
- Do CS může vstoupit vlastník tokenu.
- Requesty se šíří broadcastem; token drží frontu čekatelů a vektor posledních požadavků.

## Marzullo

Algoritmus hledá interval s maximálním překryvem intervalů časových odhadů.

Postup:

1. Z každého intervalu udělat začátek `+1` a konec `-1`.
2. Seřadit body.
3. Procházet zleva doprava a počítat aktivní intervaly.
4. Vybrat úsek s maximálním počtem překryvů.

## Dijkstra termination detection

Zkouší se jako princip detekce ukončení v distribuovaném výpočtu. V odpovědi oddělit:

- lokální pasivitu procesu;
- zprávy v kanálech;
- globální podmínku ukončení.

## Volba lídra a detektory

U voleb lídra drž dvě roviny:

- pravidlo, podle kterého se vybírá lídr;
- okamžiky, kdy porucha nebo obnova spustí novou epochu.

U novějšího zadání s perfektním detektorem lídra se lídrem stává živý proces s nejvyšší prioritou a epochy se vypisují chronologicky.

## Rendezvous / Bagrodia

Zadání z roku 2023/2024 používá tokeny a fronty partnerů:

- proces drží frontu tokenů potenciálních partnerů;
- při vstupu do kontextu chce komunikovat;
- při přijetí nového tokenu jej zařadí do fronty;
- pokud se dvojice domluví na komunikaci, opustí kontext.

Při simulaci hlídej pořadí událostí ve stejném čase: pokud zadání říká, že proces nejdřív odesílá a až potom zpracuje příjem, musíš to respektovat.

## Random mating

Opakovaný simulační úkol:

1. V jumping phase se uzly pseudonáhodně párují jako `F/M`.
2. Cílem je zvolit kroky tak, aby fáze skončila do zadaného počtu iterací, často do 4.
3. Reconstruction phase obnoví nebo popíše výslednou strukturu.

Bez obrázku nelze dopočítat konkrétní páry, ale šablona odpovědi je vždy: vypsat iterace, ukázat změny hran/párů a nezapomenout reconstruction phase.

## Čtyři čtenáři / čtyři čítače

Ve zdrojích se objevuje jako krátké zadání k detekci ukončení, někdy zapsané jako "čtyři čtenáři" a jindy jako "čtyři čítače". Ber to jako úlohu na globální stav:

- ukázat běh, kde lokální podmínky vedou k detekci ukončení;
- ukázat běh, kde zprávy nebo stav v kanálu detekci brání;
- oddělit lokální pasivitu od globálního ukončení.

## Vyřešené příklady z termínů

### Maekawa a zalomená kvóra

Zdroj: [[knowledge/exams/2023-2024/term-0-pretermin]]

Zadání: Maekawův algoritmus, kvóra pro 12 procesů a určení kvór pro 2 procesy.

Řešení:

- Nakresli kvóra tak, aby se každá dvě protínala.
- Proces vstoupí do kritické sekce po získání všech povolení ze svého kvóra.
- Důkaz není v kompletním výčtu procesů, ale v průniku kvór.

### Ricart-Agrawala s Lamportovými hodinami

Zdroj: [[knowledge/exams/2023-2024/term-2-prvni-opravny]]

Zadání: 4 procesy žádají o kritickou sekci v synchronním čase, zpráva má latenci 3 takty, kritická sekce trvá 1 takt; zakreslit komunikaci a logické časy.

Řešení:

- Každý request nese Lamportův timestamp.
- Při konfliktu rozhoduje menší timestamp, poté priorita/id podle zadání.
- Reply se odkládá, pokud má lokální proces přednost.
- Po každé události aktualizuj Lamportovy hodiny: lokální událost `+1`, příjem `max(local, received)+1`.

### Marzullo

Zdroj: [[knowledge/exams/2022-2023/term-2-prvni-opravny]]

Zadání: Marzullův algoritmus.

Řešení:

- Přepiš intervaly na začátky a konce.
- Seřaď body a sweepem počítej počet aktivních intervalů.
- Výsledkem je interval s maximálním překryvem.

### Random mating

Zdroj: [[knowledge/exams/2023-2024/term-2-prvni-opravny]]

Zadání: 8 uzlů, vybírat `F/M` pseudonáhodně tak, aby jumping phase skončila do 4 iterací; nezapomenout reconstruction phase.

Řešení:

- V tabulce napiš iterace jumping phase.
- U každého uzlu uveď aktuální partnerství nebo směr skoku.
- Po skončení první fáze dopiš reconstruction phase; to je častý bodový únik.

### Volba lídra po výpadcích

Zdroj: [[knowledge/exams/2025-2026/term-0-pretermin-a]]

Zadání: perfektní detektor lídra pro 4 procesy, výpadky a obnovy v taktech 1-14, vypsat epochy.

Řešení:

- V každém taktu vezmi jen živé procesy.
- Lídrem je živý proces s nejvyšší prioritou.
- Nová epocha vzniká při změně lídra; zapisuj `(rank lídra, pořadové číslo jeho vlády)`.

## Kde se to objevuje

Podle sjednocených termínových souborů v archivu:

- [[knowledge/exams/2025-2026/term-0-pretermin-b]]
- [[knowledge/exams/2025-2026/term-0-pretermin-a]]
- [[knowledge/exams/2024-2025/term-2-prvni-opravny]]
- [[knowledge/exams/2024-2025/term-0-pretermin-b]]
- [[knowledge/exams/2023-2024/term-3-druhy-opravny]]
- [[knowledge/exams/2023-2024/term-2-prvni-opravny]]
- [[knowledge/exams/2023-2024/term-1-radny-c]]
- [[knowledge/exams/2023-2024/term-1-radny-b]]
- [[knowledge/exams/2023-2024/term-1-radny-a]]
- [[knowledge/exams/2023-2024/term-0-pretermin]]
- [[knowledge/exams/2022-2023/term-3-druhy-opravny]]
- [[knowledge/exams/2022-2023/term-2-prvni-opravny]]
- [[knowledge/exams/2022-2023/term-1-radny-c]]
- [[knowledge/exams/2022-2023/term-1-radny-b]]
- [[knowledge/exams/2021-2022/term-3-druhy-opravny]]
- [[knowledge/exams/2021-2022/term-2-prvni-opravny-b]]
- [[knowledge/exams/2021-2022/term-2-prvni-opravny-a]]
- [[knowledge/exams/2020-2021/term-3-druhy-opravny]]
- [[knowledge/exams/2020-2021/term-2-prvni-opravny]]
- [[knowledge/exams/2020-2021/term-1-radny-zkratka]]
- [[knowledge/exams/2019-2020/term-2-prvni-opravny]]
- [[knowledge/exams/2019-2020/term-1-radny-a]]
- [[knowledge/exams/2018-2019/term-1-radny-c]]
- [[knowledge/exams/2018-2019/term-1-radny-b]]
- [[knowledge/exams/2018-2019/term-1-radny-a]]
