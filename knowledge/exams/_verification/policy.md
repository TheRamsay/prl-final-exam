# Pravidla verifikace

## Cíl

Verifikace má oddělit původní raw zadání od doplňků ze studentského dokumentu. Nic v `raw/` nepřepisujeme a nic ze studentského dokumentu automaticky nepovyšujeme nad raw zdroj.

## Statusy

| Status | Význam |
|---|---|
| `shoda` | Raw a student doc popisují stejný termín a stejné pořadí příkladů. |
| `student_doc doplňuje raw` | Raw existuje, student doc ho potvrzuje nebo rozšiřuje o řešení/detail. |
| `raw only` | Máme raw zdroj, ale ve student docu není odpovídající sekce. |
| `student_doc only` | Termín je jen ve studentském dokumentu. |
| `rozpor` | Zdroje se liší věcně, pořadím nebo variantou. |
| `neověřeno` | Není jasné, jestli jde o stejný termín/variantu. |

## Pravidla zápisu

- Primární zadání v termínových souborech vychází z raw zdrojů, pokud existují.
- Student doc se zapisuje do sekce `Student doc reference` a `Rozdíly / doplnění ze student_doc`.
- Pokud student doc pouze opakuje raw, uvést `shoda`.
- Pokud student doc přidává řešení nebo upřesnění, uvést `student_doc doplňuje raw`.
- Pokud je část nečitelná nebo nejistá, explicitně to zapsat do `Poznámky k nejistotám`.
- Obrázkové přepisy zatím nehrotíme nad rámec už existujících přepisů.

