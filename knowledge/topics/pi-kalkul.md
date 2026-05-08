# Pi-kalkul

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

## Chyby

- Redukovat přes jiný kanál jen proto, že proměnná má podobné jméno.
- Zapomenout, že volba `+` po výběru větve zahodí druhou větev.
- Neudělat substituci ve zbytku procesu.

