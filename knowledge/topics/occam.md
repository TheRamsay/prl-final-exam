# OCCAM

## Zkouškový pattern

Zadání většinou chce napsat nekonečnou proceduru s kanály, vnitřním stavem a větvením podle vstupu. Typicky se opakuje buffer/fronta, výběr výstupního kanálu, střídání výstupů nebo výpočet průměru.

## Oficiální slidy

- [[knowledge/sources/slides/modely#Strana 3|Modely, str. 3]] až [[knowledge/sources/slides/modely#Strana 6|str. 6]] - OCCAM, procesy a komunikační kanály.
- [[knowledge/sources/slides/modely#Strana 7|Modely, str. 7]] až [[knowledge/sources/slides/modely#Strana 9|str. 9]] - `SEQ`, `PAR`, replikovaný `PAR`.
- [[knowledge/sources/slides/modely#Strana 12|Modely, str. 12]] až [[knowledge/sources/slides/modely#Strana 14|str. 14]] - `ALT`, stráže a příklady.
- [[knowledge/sources/slides/modely#Strana 15|Modely, str. 15]] - deklarace procedur.

## Co umět

- Kanály a komunikaci přes `?` a `!`.
- Sekvenční `SEQ` a paralelní `PAR`.
- Alternativu `ALT`.
- Pole kanálů.
- Nekonečnou smyčku procesu.

## Typická šablona

```occam
PROC worker(CHAN OF BYTE data, ctrl, out)
  BYTE x:
  WHILE TRUE
    SEQ
      data ? x
      out ! x
:
```

Skutečná syntaxe se může lišit podle přednášek, ale zkouška často hodnotí hlavně princip komunikace, uchování stavu a správné čekání na kanálech.

## Typické úlohy

- Přesměrovat data na výstupní kanál podle hodnoty z control kanálu.
- Udržovat vnitřní queue a na clock posílat další prvek.
- Střídat výstupy vlevo/vpravo.
- Počítat průměr a podle něj směrovat hodnoty.
- Hlásit `WARN`, když hodnota překročí limit.

## Vyřešené příklady z termínů

### Fronta a střídání výstupů

Zdroj: [[knowledge/exams/2023-2024/term-0-pretermin]]

Zadání: procedura s kanály `input`, `clk`, `OUT_LEFT`, `OUT_RIGHT`; hodnoty z `input` ukládat do vnitřní fronty a při `clk` posílat první prvek střídavě doleva a doprava.

Řešení:

- Udržuj frontu a index prvního prvku.
- `input ? x` pouze vloží hodnotu do fronty.
- `clk ? any` vybere první prvek, pošle ho na aktuální výstup a přepne směr.
- Prázdnou frontu je potřeba ošetřit; buď `clk` ignorovat, nebo čekat podle přesné interpretace zadání.

### Směrování podle `ctrl`

Zdroj: [[knowledge/exams/2024-2025/term-0-pretermin]]

Zadání: byte channels `data`, `ctrl`, `out[5]`; data odeslat na výstupní kanál určený hodnotou z `ctrl`.

Řešení:

- Drž aktuální výstupní index.
- Po přijetí hodnoty z `ctrl` aktualizuj index, pokud je v rozsahu.
- Po přijetí hodnoty z `data` pošli hodnotu na `out[index]`.
- Pokud mohou přijít oba typy událostí, použij `ALT` nebo jasně popiš nedeterministické čekání na připravený kanál.

### Průměr a výstupy podle porovnání

Zdroj: [[knowledge/exams/2020-2021/term-3-druhy-opravny]]

Zadání: procedura `AVG` se třemi kanály typu `BYTE`: `DATA`, `CHNH`, `CHNL`; počítá dlouhodobý průměr a posílá hodnoty podle porovnání s průměrem.

Řešení:

- Drž součet a počet přijatých hodnot nebo aktualizovaný průměr.
- Po `DATA ? x` aktualizuj stav.
- Podle porovnání `x` s průměrem pošli `x` na vyšší nebo nižší kanál.

## Kde se to objevuje

Podle sjednocených termínových souborů v archivu:

- [[knowledge/exams/2025-2026/term-0-pretermin-a]]
- [[knowledge/exams/2024-2025/term-0-pretermin]]
- [[knowledge/exams/2024-2025/term-2-prvni-opravny]]
- [[knowledge/exams/2024-2025/term-0-pretermin-b]]
- [[knowledge/exams/2023-2024/term-0-pretermin]]
- [[knowledge/exams/2021-2022/term-2-prvni-opravny-b]]
- [[knowledge/exams/2021-2022/term-2-prvni-opravny-a]]
- [[knowledge/exams/2021-2022/term-1-radny-c]]
- [[knowledge/exams/2021-2022/term-1-radny-b]]
- [[knowledge/exams/2021-2022/term-1-radny-a]]
- [[knowledge/exams/2020-2021/term-3-druhy-opravny]]
- [[knowledge/exams/2019-2020/term-1-radny-a]]

## Chyby

- Zapomenout, že komunikace je synchronní rendezvous.
- Ztratit vnitřní stav queue/průměru mezi iteracemi.
- Číst z kanálu, který v dané větvi nemusí být připravený, bez `ALT`.
