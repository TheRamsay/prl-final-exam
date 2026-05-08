# OCCAM

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

## Chyby

- Zapomenout, že komunikace je synchronní rendezvous.
- Ztratit vnitřní stav queue/průměru mezi iteracemi.
- Číst z kanálu, který v dané větvi nemusí být připravený, bez `ALT`.

