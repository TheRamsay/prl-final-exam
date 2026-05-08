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

## Mini-drill

1. Jaký je rozdíl mezi latencí a propustností v pipeline?
2. Co u VLIW řeší překladač?
3. Kdy je SIMD vhodnější než MIMD?
4. Proč je PRAM spíš model než reálná architektura?

## Kde se to objevuje

- [[knowledge/exams/2024-2025/term-0-pretermin]]
- [[knowledge/exams/2023-2024/student-doc-digest]]
- [[knowledge/exams/2021-2022/student-doc-digest]]
- [[knowledge/exams/2020-2021/student-doc-digest]]
- [[knowledge/exams/2019-2020/student-doc-digest]]
- [[knowledge/exams/2018-2019/student-doc-digest]]

## Chyby

- U pipeline tvrdit, že zrychlí latenci jednoho prvku; hlavní zisk je propustnost.
- U VLIW zapomenout na statické plánování překladačem.
- Zaměnit SIMD a MIMD jen podle počtu procesorů, ne podle toku instrukcí.
