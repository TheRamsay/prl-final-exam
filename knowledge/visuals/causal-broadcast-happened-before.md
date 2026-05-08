# Kauzalita: happened-before

Zdrojový topic: [[knowledge/topics/broadcast-fifo-kauzalita]]

## Co si pamatovat

- Kauzální broadcast hlídá relaci `->`, ne jen pořadí jednoho odesílatele.
- `m1 -> m2` znamená: každý proces, který doručí obě zprávy, musí doručit `m1` před `m2`.
- Kauzalita vzniká lokálním pořadím událostí, hranami `send -> receive` a tranzitivitou.

## Typický kauzální řetěz

```mermaid
sequenceDiagram
  participant P1
  participant P2
  participant P3
  P1->>P2: m1
  Note over P2: receive m1
  P2->>P3: m2
  Note over P3: m1 -> m2, takže m2 čeká na m1
  P1->>P3: m1
  P3->>P3: deliver m1
  P3->>P3: deliver m2
```

## Proč `m2` čeká

```mermaid
flowchart LR
  A["P1 send m1"] --> B["P2 receive m1"]
  B --> C["P2 send m2"]
  A -. "m1 je kauzální předchůdce" .-> C
  C --> D["P3 receive m2"]
  E["P3 receive m1"] --> F["P3 deliver m1"]
  D --> G{"má P3 doručené všechny předchůdce m2?"}
  F --> G
  G -->|ano| H["P3 deliver m2"]
  G -->|ne| I["buffer m2"]
```

## Happened-before checklist

| Zdroj relace | Co zapsat do diagramu | Typický příklad |
|---|---|---|
| Lokální pořadí | události na jednom procesu jdou shora dolů | `send a -> receive b` na `P2` |
| Komunikační hrana | odeslání zprávy předchází přijetí | `send(m) -> recv(m)` |
| Tranzitivita | spoj předchozí závislosti | `a -> b` a `b -> c`, tedy `a -> c` |

## Zkoušková odpověď

1. Definuj `->` přes lokální pořadí, `send -> receive` a tranzitivitu.
2. U broadcastu řekni, že zpráva nese kauzální historii, typicky vektorové hodiny.
3. Příjemce doručí zprávu až po doručení všech jejích kauzálních předchůdců.
4. Porušení kauzality je doručení následku před příčinou.

## Časté chyby

- Kontrolovat jen přímé hrany a zapomenout tranzitivitu.
- Zaměnit kauzalitu s FIFO; FIFO je jen pořadí jednoho odesílatele.
- Posuzovat `recv` místo `deliver`.

## Termínové zdroje

- [[knowledge/exams/2025-2026/term-0-pretermin-a]]
- [[knowledge/exams/2023-2024/term-0-pretermin]]
- [[knowledge/exams/2022-2023/term-3-druhy-opravny]]
