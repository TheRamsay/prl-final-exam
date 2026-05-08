# Linda, ADA a ostatní jazyky

## Linda

Linda pracuje s tuple space.

Typické operace:

- `out(tuple)`: vložení n-tice.
- `in(pattern)`: vyzvednutí odpovídající n-tice, blokuje.
- `rd(pattern)`: přečtení odpovídající n-tice bez odebrání.
- `eval(...)`: spuštění procesu / vyhodnocení.

Typické úlohy:

- operace nad spojovým seznamem;
- reverse/delete/search;
- koordinace procesů přes n-tice.

## ADA

Zkouškově spíš okrajové. Držet se pojmů:

- task;
- entry;
- rendezvous;
- accept.

## Chyby

- Zaměnit `rd` a `in`.
- Zapomenout, že `in` je destruktivní.
- U rendezvous neuvažovat blokování obou stran do spárování.

