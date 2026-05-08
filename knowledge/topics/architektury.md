# Architektury

## Zkouškový pattern

Téma se ptá na krátký popis a nákres principu: VLIW, pipeline/zřetězení, SIMD/MIMD, dataflow, Xeon Phi nebo PRAM model. Body jsou hlavně za správnou terminologii, výhody/nevýhody a typické konflikty.

## VLIW

Very Long Instruction Word spojuje několik nezávislých operací do jednoho širokého instrukčního slova. Paralelismus plánuje převážně překladač, hardware pak spouští operace na více funkčních jednotkách.

Co uvést:

- dlouhé instrukční slovo obsahuje sloty pro různé jednotky;
- statické plánování;
- závislosti dat, strukturální konflikty a řídicí konflikty;
- řešení: plánování, vkládání NOP, predikace, rozbalení smyček, kontrola závislostí.

Minimální odpověď: VLIW přesouvá plánování paralelismu do překladače; široká instrukce obsahuje více operací pro různé funkční jednotky.

## Zřetězené procesory / pipeline

- Výpočet se rozdělí do fází.
- Po naplnění pipeline se v každém taktu dokončuje jeden výsledek.
- Latence jednoho prvku může být větší, propustnost po naplnění je vysoká.
- Rizika: datové hazardy, strukturální hazardy, větvení.

Minimální odpověď: pipeline zvyšuje propustnost, ne nutně latenci jednoho prvku; po naplnění může dokončovat jeden výsledek za takt.

## SIMD/MIMD

- SIMD: jedna instrukce nad více daty, vhodné pro vektory/matice.
- MIMD: více procesorů provádí různé instrukce nad různými daty.

Co dodat:

- SIMD má jednoduché řízení a dobré využití pro pravidelná data.
- MIMD je obecnější, ale složitější na synchronizaci a komunikaci.
- UMA/NUMA se týká přístupu ke sdílené paměti.

## Dataflow

- Instrukce se spustí, jakmile má dostupné operandy.
- Řízení je dáno tokem dat, ne centrálním programovým čítačem.
- Dobré pro vysvětlení implicitního paralelismu.

## PRAM jako architektura/model

- Sdílená paměť, synchronní kroky, procesory přistupují k buňkám podle omezení EREW/CREW/CRCW.
- Je to hlavně abstraktní výpočetní model, ne realistická hardwarová architektura.

## Xeon Phi a vektorové procesory

Xeon Phi se v zadáních objevuje jako kombinace MIMD a SIMD:

- mnoho jader běží MIMD stylem;
- každé jádro má široké vektorové jednotky, typicky zmiňované jako 512bitové registry;
- tématem jsou cache, paměťová hierarchie a vektorová část jádra;
- vhodné je nakreslit jádra, vektorové jednotky a sdílenou/privátní cache podle zadání.

U vektorových procesorů zdůrazni, že jedna vektorová instrukce pracuje nad více prvky vektoru. Výhoda je vysoká propustnost pro pravidelná data, nevýhoda horší využití u nepravidelných větvení a závislostí.

## Propojovací síť

Propojovací síť určuje, jak spolu komunikují procesory, paměti nebo uzly paralelního systému.

Co uvést:

- topologie: sběrnice, křížový přepínač, mřížka, hypercube, strom;
- parametry: průměr, stupeň uzlu, šířka pásma, bisection bandwidth;
- výhody/nevýhody: cena, latence, škálovatelnost, bottleneck.

## Redukční počítač a granularita

Redukční počítač spouští výpočet jako přepis/redukci výrazů, ne jako klasickou sekvenci instrukcí řízenou programovým čítačem. U odpovědi pomáhá propojit to s dataflow myšlenkou: výpočet se aktivuje dostupností podvýrazů.

Granularita paralelismu popisuje velikost práce mezi synchronizacemi nebo komunikací:

- jemná granularita: hodně malých paralelních úloh, větší režie;
- hrubá granularita: méně větších úloh, menší režie, ale horší vyvážení.

## Mini-drill

1. Jaký je rozdíl mezi latencí a propustností v pipeline?
2. Co u VLIW řeší překladač?
3. Kdy je SIMD vhodnější než MIMD?
4. Proč je PRAM spíš model než reálná architektura?

## Vyřešené příklady z termínů

### VLIW

Zdroj: [[knowledge/exams/2023-2024/student-doc-digest]]

Zadání: popsat VLIW.

Řešení:

- VLIW používá dlouhé instrukční slovo se sloty pro několik funkčních jednotek.
- Paralelismus plánuje hlavně překladač, ne dynamický hardware.
- Překladač musí řešit datové závislosti, strukturální konflikty a větvení.
- Typické techniky: vkládání NOP, rozbalení smyček, plánování instrukcí, predikace.
- Výhoda je jednodušší hardware, nevýhoda horší kompatibilita/plánování pro různé implementace.

### Zřetězené procesory

Zdroj: [[knowledge/exams/2024-2025/term-0-pretermin]]

Zadání: vysvětlit zřetězení v aritmetických operacích a nakreslit příklad.

Řešení:

- Aritmetická operace se rozdělí na fáze, například načtení operandů, dílčí výpočet, normalizace, zápis.
- Každá fáze běží v jiné části pipeline.
- Po naplnění pipeline se v každém taktu může dokončit jeden výsledek.
- Latence jednoho výsledku je počet fází, ale propustnost je po naplnění až jeden výsledek za takt.
- Do obrázku nakresli řadu fází a několik instrukcí posunutých o jeden takt.

### Dataflow architektura

Zdroj: [[knowledge/exams/2021-2022/student-doc-digest]]

Zadání: popsat dataflow architekturu.

Řešení:

- Instrukce není spouštěna programovým čítačem, ale dostupností operandů.
- Výpočet lze kreslit jako graf závislostí.
- Uzel se aktivuje, když jsou dostupné všechny vstupní tokeny.
- Výhoda: přirozeně odhaluje paralelismus.
- Nevýhoda: složitá správa tokenů, paměti a pořadí efektů.

### Xeon Phi

Zdroj: [[knowledge/exams/2021-2022/term-2-prvni-opravny-b]]

Zadání: Xeon Phi, popsat a nakreslit obrázek.

Řešení:

- Popiš ho jako mnohojádrovou architekturu se SIMD vektorovými jednotkami.
- Uveď kombinaci MIMD na úrovni jader a SIMD uvnitř jádra.
- Do obrázku dej jádra, vektorovou jednotku/cache a propojení s pamětí.

### Propojovací síť

Zdroj: [[knowledge/exams/2023-2024/term-1-radny-c]]

Zadání: k čemu se používá propojovací síť.

Řešení:

- Propojuje procesory mezi sebou nebo procesory s pamětí.
- Hodnotí se latence, propustnost, cena a škálovatelnost.
- Nakresli alespoň jednu topologii a řekni její bottleneck.

### Redukční počítač

Zdroj: [[knowledge/exams/2022-2023/term-0-pretermin]]

Zadání: Redukční počítač.

Řešení:

- Výpočet chápej jako postupnou redukci výrazů.
- Paralelismus vzniká tam, kde lze nezávisle redukovat podvýrazy.
- Dobrá odpověď odliší redukční/dataflow princip od klasického von Neumannova řízení.

## Kde se to objevuje

Podle sjednocených termínových souborů v archivu:

- [[knowledge/exams/2024-2025/term-0-pretermin]]
- [[knowledge/exams/2024-2025/term-0-pretermin-b]]
- [[knowledge/exams/2023-2024/term-1-radny-c]]
- [[knowledge/exams/2023-2024/term-1-radny-b]]
- [[knowledge/exams/2023-2024/term-1-radny-a]]
- [[knowledge/exams/2023-2024/term-0-pretermin]]
- [[knowledge/exams/2022-2023/term-1-radny-c]]
- [[knowledge/exams/2022-2023/term-1-radny-b]]
- [[knowledge/exams/2022-2023/term-1-radny-a-zkratka]]
- [[knowledge/exams/2022-2023/term-0-pretermin]]
- [[knowledge/exams/2021-2022/term-3-druhy-opravny]]
- [[knowledge/exams/2021-2022/term-2-prvni-opravny-b]]
- [[knowledge/exams/2021-2022/term-2-prvni-opravny-a]]
- [[knowledge/exams/2021-2022/term-1-radny-c]]
- [[knowledge/exams/2021-2022/term-1-radny-b]]
- [[knowledge/exams/2021-2022/term-1-radny-a]]
- [[knowledge/exams/2020-2021/term-3-druhy-opravny]]
- [[knowledge/exams/2020-2021/term-2-prvni-opravny]]
- [[knowledge/exams/2019-2020/term-2-prvni-opravny]]
- [[knowledge/exams/2019-2020/term-1-radny-b]]
- [[knowledge/exams/2019-2020/term-1-radny-a]]
- [[knowledge/exams/2018-2019/term-1-radny-c]]
- [[knowledge/exams/2018-2019/term-1-radny-a]]

## Chyby

- U pipeline tvrdit, že zrychlí latenci jednoho prvku; hlavní zisk je propustnost.
- U VLIW zapomenout na statické plánování překladačem.
- Zaměnit SIMD a MIMD jen podle počtu procesorů, ne podle toku instrukcí.
