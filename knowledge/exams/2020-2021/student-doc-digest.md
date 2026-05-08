# 2020/2021 - student doc digest

## Metadata

| Pole | Hodnota |
|---|---|
| Akademický rok | 2020/2021 |
| Zdroj | studentský dokument |
| Stav | první destilace |
| Auditovatelný extract | [[knowledge/sources/student-doc/2020-2021-extract]] |

## Stav verifikace

| Pole | Hodnota |
|---|---|
| Verifikační status | `student_doc doplňuje raw` |
| Kontrolní matice | [[knowledge/exams/_verification/raw-vs-student-doc#2020-2021]] |

## Původní zdroje

- Raw dokument: [[raw/student_doc]]
- Očištěný zdroj: [[knowledge/sources/student-doc/clean]]
- Extract roku: [[knowledge/sources/student-doc/2020-2021-extract]]

## Přehled termínů

### Term 1 - řádný termín

1. [[knowledge/topics/pram-tipovacka|PRAM složitosti]] - cena XOR, časová složitost OR, cena součtu/maxima/minima.
   - Zdroj uvádí jako pravděpodobné: XOR čas `log n`; součet/max/min cena `n log n`.
2. [[knowledge/topics/mutual-exclusion|Test-and-set]] - aktivní čekání, atomická instrukce nad `lock`.
3. [[knowledge/topics/broadcast-fifo-kauzalita|Kauzalita]].
4. [[knowledge/topics/euler-tour-suffix-sums|Eulerův tah / suffix]].
5. [[knowledge/topics/distribuovane-algoritmy|Ricart-Agrawala]] - optimalizace Lamportova algoritmu.
6. Euler strom/graf.
7. [[knowledge/topics/cla|Carry-look-ahead]] - spočítat `39 + 110`.
   - Zdroj rozepisuje binární převod, vektor `s/p/g`, prefixový operátor a výsledný součet.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - součet hodnot větších než průměr.
   - Zdroj obsahuje standardní šablonu: `Reduce SUM`, `Bcast avg`, lokální filtr, `Reduce SUM`.

### Term 2 - 1. opravný termín

1. [[knowledge/topics/pram-tipovacka|PRAM složitosti]].
2. [[knowledge/topics/pram-tipovacka|PRAM architektura]] - popis a obrázek.
3. [[knowledge/topics/pi-kalkul|Pi-kalkul]] - redukce a pozorování.
4. Random mating - příklad.
5. [[knowledge/topics/distribuovane-algoritmy|Suzuki]] - princip a obrázek se 4 uzly.
6. [[knowledge/topics/synchronizace-monitory-semafory|Monitor]] - `wait`, `signal`, obrázek.
7. [[knowledge/topics/linda-ada|Linda]] - reverz seznamu.
   - Zdroj obsahuje pseudokód s `rd`, `in`, `out` a upozornění na přepsání původní hlavy.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - součet čísel větších než průměr.

### Term 3 - 2. opravný termín

1. [[knowledge/topics/pram-tipovacka|PRAM tipovačka]].
2. [[knowledge/topics/architektury|VLIW]] + řešení konfliktů.
3. [[knowledge/topics/synchronizace-monitory-semafory|Monitor]] - popis + obrázek.
4. [[knowledge/topics/synchronizace-monitory-semafory|Problém pěti filozofů]] - kód se semafory, deadlock-proof.
   - Zdroj používá semafor `E.count = 4`, aby narušil cyklické čekání, a semafory pro vidličky.
5. [[knowledge/topics/broadcast-fifo-kauzalita|FIFO/broadcast]] podle tabulky.
6. Random mating.
7. [[knowledge/topics/occam|OCCAM]] - procedura `AVG(DATA, CHNH, CHNL)` počítá dlouhodobý průměr a posílá hodnoty podle porovnání s průměrem.
8. [[knowledge/topics/mpi-reduce-bcast|MPI]] - součet hodnot menších než maximum nebo větších než minimum.
   - Zdroj: `Reduce MAX`, `Bcast max`, lokální filtr, `Reduce SUM`.

## Využitelné řešicí poznámky

- Rok 2020/2021 dobře doplňuje hotové šablony pro MPI, CLA, monitor, Linda a filozofy.
- Některé PRAM odpovědi jsou ve zdroji označené jako nejisté; nepřebírat bez kontroly.
