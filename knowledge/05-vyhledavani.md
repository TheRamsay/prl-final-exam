# Vyhledávání

Web používá Quartz full-text search přes FlexSearch. Vyhledávání je zapnuté v layoutu a indexuje text stránek přes `ContentIndex`.

## Jak hledat na webu

- Klikni na `Hledat` v levém panelu.
- Klávesová zkratka: `Ctrl+K` nebo `Cmd+K`.
- Hledání prochází názvy, obsah i tagy.
- Výsledky ukazují výřez textu s nalezeným výrazem.
- Tag search: `Ctrl+Shift+K` / `Cmd+Shift+K`, nebo dotaz začít znakem `#`.

## Dobré dotazy

```text
Ricart Agrawala
FIFO broadcast
koruna synchronizovatelnost
MPI průměr
Enumeration Sort
OCCAM CTRL OUT
CLA 120 99
Random mating
```

## Co je zapojené

- Search UI: `.quartz/quartz.layout.ts` používá `Component.Search()`.
- Full-text index: `.quartz/quartz.config.ts` používá `Plugin.ContentIndex()`.
- Index na webu: `static/contentIndex.json`.

## Poznámka

Quartz indexuje text stránek, ne URL odkazy. Když chceš hledat konkrétní raw soubor, je lepší použít lokálně `rg` v repozitáři.
