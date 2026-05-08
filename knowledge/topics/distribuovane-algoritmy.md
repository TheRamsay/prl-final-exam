# Distribuované algoritmy

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

