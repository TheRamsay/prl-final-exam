# Pi-kalkul

## Zkouškový pattern

Zadání dá jeden výraz v pi-kalkulu a chce několik možných redukcí nebo koncových výrazů. Často se hodnotí i pozorování typu `↓x`. Důležité je vypsat různé větve nedeterminismu, ne jen jednu náhodnou redukci.

## Oficiální slidy

- [[knowledge/sources/slides/modely#Strana 16|Modely, str. 16]] až [[knowledge/sources/slides/modely#Strana 18|str. 18]] - úvod do π-kalkulu, procesy a strukturální ekvivalence.
- [[knowledge/sources/slides/modely#Strana 19|Modely, str. 19]] až [[knowledge/sources/slides/modely#Strana 21|str. 21]] - redukční pravidla, komunikace a omezené kanály.
- [[knowledge/sources/slides/modely#Strana 25|Modely, str. 25]] až [[knowledge/sources/slides/modely#Strana 27|str. 27]] - pozorování, barbed simulace a bisimulace.
- [[knowledge/sources/slides/modely#Strana 31|Modely, str. 31]] až [[knowledge/sources/slides/modely#Strana 37|str. 37]] - příklady redukcí a bufferu.

## Syntaxe, která se objevuje

- `a(x).P`: přijmi hodnotu na kanálu `a`, ulož do `x`, pokračuj jako `P`.
- `a'b.P` nebo `ā⟨b⟩.P`: pošli `b` po kanálu `a`, pokračuj jako `P`.
- `P | Q`: paralelní kompozice.
- `P + Q`: volba.
- `0`: konec.
- `(new x) P`: omezení jména `x`.

## Jak řešit redukce

1. Najít kompatibilní dvojici send/receive na stejném kanálu.
2. Pro každou možnou volbu udělat substituci přijaté hodnoty.
3. Pokračovat, dokud nejde redukovat.
4. Vypsat různé koncové výrazy.

## Co se obvykle hodnotí

- Správné párování kanálů.
- Korektní substituce.
- Rozlišení alternativ v `+`.
- Uvedení 3 až 4 různých možných výsledků, pokud existují.

## Vyřešené příklady z termínů

### Redukovat všemi možnými způsoby

Zdroj: [[knowledge/exams/2018-2019/term-1-radny-a]]

Zadání: paralelní procesy redukovat všemi možnými způsoby a v každé fázi uvést pozorování.

Řešení:

- Nejprve najdi všechny dvojice `output/input` na stejném kanálu.
- Každá možná komunikace je samostatná větev řešení.
- Po výběru větve u `+` druhá větev mizí.
- Pozorování zapisuj podle toho, které výstupní akce jsou v daném stavu viditelné.

### Najít 4 koncové redukce

Zdroj: [[knowledge/exams/2023-2024/term-1-radny-b]]

Zadání: najít alespoň 4 různé redukce do stavu, kde už nelze dále redukovat.

Řešení:

- Cílem není maximálně zkrátit zápis, ale ukázat různé dosažitelné koncové stavy.
- Po každé komunikaci proveď substituci ve zbytku procesu.
- Pokud jsou v procesu privátní jména, hlídej scope; nesmíš omylem spárovat jméno mimo jeho omezení.

### Najít 3 možné redukce

Zdroj: [[knowledge/exams/2022-2023/term-2-prvni-opravny]]

Zadání: najít 3 možné redukce.

Řešení:

- Stačí tři korektní větve, ale každá musí být opravdu dosažitelná z původního procesu.
- U každé větve napiš komunikační pár, substituci a výsledný výraz po redukci.

## Kde se to objevuje

Podle sjednocených termínových souborů v archivu:

- [[knowledge/exams/2023-2024/term-2-prvni-opravny]]
- [[knowledge/exams/2023-2024/term-1-radny-c]]
- [[knowledge/exams/2023-2024/term-1-radny-b]]
- [[knowledge/exams/2023-2024/term-1-radny-a]]
- [[knowledge/exams/2022-2023/term-3-druhy-opravny]]
- [[knowledge/exams/2022-2023/term-2-prvni-opravny]]
- [[knowledge/exams/2022-2023/term-1-radny-c]]
- [[knowledge/exams/2022-2023/term-1-radny-b]]
- [[knowledge/exams/2022-2023/term-1-radny-a-zkratka]]
- [[knowledge/exams/2022-2023/term-0-pretermin]]
- [[knowledge/exams/2020-2021/term-2-prvni-opravny]]
- [[knowledge/exams/2018-2019/term-1-radny-c]]
- [[knowledge/exams/2018-2019/term-1-radny-b]]
- [[knowledge/exams/2018-2019/term-1-radny-a]]

## Chyby

- Redukovat přes jiný kanál jen proto, že proměnná má podobné jméno.
- Zapomenout, že volba `+` po výběru větve zahodí druhou větev.
- Neudělat substituci ve zbytku procesu.
