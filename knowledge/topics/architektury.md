# Architektury

## VLIW

Very Long Instruction Word spojuje několik nezávislých operací do jednoho širokého instrukčního slova. Paralelismus plánuje převážně překladač, hardware pak spouští operace na více funkčních jednotkách.

Co uvést:

- dlouhé instrukční slovo obsahuje sloty pro různé jednotky;
- statické plánování;
- závislosti dat, strukturální konflikty a řídicí konflikty;
- řešení: plánování, vkládání NOP, predikace, rozbalení smyček, kontrola závislostí.

## Zřetězené procesory / pipeline

- Výpočet se rozdělí do fází.
- Po naplnění pipeline se v každém taktu dokončuje jeden výsledek.
- Latence jednoho prvku může být větší, propustnost po naplnění je vysoká.
- Rizika: datové hazardy, strukturální hazardy, větvení.

## SIMD/MIMD

- SIMD: jedna instrukce nad více daty, vhodné pro vektory/matice.
- MIMD: více procesorů provádí různé instrukce nad různými daty.

## Dataflow

- Instrukce se spustí, jakmile má dostupné operandy.
- Řízení je dáno tokem dat, ne centrálním programovým čítačem.
- Dobré pro vysvětlení implicitního paralelismu.

## PRAM jako architektura/model

- Sdílená paměť, synchronní kroky, procesory přistupují k buňkám podle omezení EREW/CREW/CRCW.
- Je to hlavně abstraktní výpočetní model, ne realistická hardwarová architektura.

