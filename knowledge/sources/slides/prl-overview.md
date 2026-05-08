# PRL prehled predmetu a paralelni modely

Oficialni slidy extrahovane z PDF. Text je automaticky vytazeny pres `pdftotext -layout`; u obrazkovych nebo diagramovych stran kontroluj originalni PDF.

## Metadata

| Pole | Hodnota |
|---|---|
| Zdroj | [[raw/2526_PRL.pdf]] |
| Soubor | `2526_PRL.pdf` |
| Stran | 98 |
| PDF title | PowerPoint Presentation |
| Creator | Microsoft® PowerPoint® LTSC |
| Page size | 720 x 540 pts |

## Pouziti

- Pouzivej jako oficialni oporu pro definice, algoritmy, terminologii a slozitosti.
- Pokud je strana zalozena hlavne na obrazku, cituj stranu a zkontroluj originalni PDF.
- Pro exam historii porad preferuj `knowledge/exams/**/term-*.md`; slidy slouzi jako vykladovy zdroj.

## Text po stranach

### Strana 1

```text
  PARALELNÍ
ARCHITEKTURY
  František Zbořil ml., Petr Hanáček
               – 2024
```

### Strana 2

```text
Paralelizace úlohy

■ Sekvenční vykonání úlohy – jedním procesorem jedny data.
■ Pokud lze úloha rozdělit na podúlohy, které lze vykonávat
  paralelně, může být úloha splněna v kratším čase
■ Pokud jeden dělník vykoná práci v čase 𝑇𝑠𝑒𝑘𝑣𝑒𝑛č𝑛í, pak N
                                       𝑇
  dělníků vykoná tu samou práci v čase 𝑠𝑒𝑘𝑣𝑒𝑛č𝑛í
                                            𝑁

■ Práce (úloha) však nemusí být plně rozdělitelná
  (paralelizovatelná) mezi všechny dostupné dělníky
    – Inicializace úlohy – sekvenční část
```

### Strana 3

```text
Zrychlení

Zrychlení výpočtu při paralelizaci úlohy
            𝑇𝑛𝑒𝑝𝑎𝑟𝑎𝑙𝑒𝑙𝑖𝑧𝑜𝑣𝑎𝑛á ú𝑙𝑜ℎ𝑎
       𝑆=
             𝑇𝑝𝑎𝑟𝑎𝑙𝑒𝑙𝑖𝑧𝑜𝑣𝑎𝑛á ú𝑙𝑜ℎ𝑎

Pokud část úlohy 𝑃 paralelizovatelnou po N podúlohách označíme jako
𝛼𝑃, 𝛼 ∈< 0,1 >, a zbývající část je vykonána sekvenčně
Amdahlův zákon                        𝛼 = 0.8; 0.9; 0.92; 0.95
                   1
      𝑆 𝑁 =            𝛼
                1−𝛼 +𝑁
```

### Strana 4

```text
Paralelní architektury

■ Von Neumanovské architektury
   – Flynova klasifikace
■ Ne Vone Neumanovské architektury
   – Dataflow (řízené tokem dat)
   – Redukční počítače
   – Neuronové sítě
   – Atd.
```

### Strana 5

```text
Flynova klasifikace

(Single / Multiple, Instruction / Data)
■ SISD - Jedna instrukce pracuje s jedním datovým prvkem
■ SIMD - Jedna instrukce pracuje s více datovými prvky
   – Vektorové procesory
   – MSIMD
■ MISD - Více instrukcí pracuje s jedním datovým prvkem
■ MIMD - Více instrukcí pracuje s více datovými prvky
   – Vícevláknové procesory
   – Viceprocesorové systémy
          ■   Distribuované systémy
```

### Strana 6

```text
 Flynova klasifikace

+                  +    A+B
            A+B    *
A B               A B   A*B



                   +
+           A+B         A+B
                   *
A B         C+D   A B   C*D
C D               C D
```

### Strana 7

```text
 Paralelní architektury
                            Paralelní architektury

       von Neumann               Data Flow            Redukční
SISD   MISD MIMD        SIMD

                     Zřetězené                vektorové procesory
     Zřetězené
VLIW procesory       MIMD                     asociativní procesory
                                              zřetězené SIMD
                   Ostatní MIMD               MSIMD
                 MIMD


Se společnou     S propojovací        S pevnou
 sběrnicí             sítí            sítí
```

### Strana 8

```text
      NE-VON
NEUMANOVSKÉ
ARCHITEKTURY
         DATAFLOW
         REDUKČNÍ
```

### Strana 9

```text
  DATAFLOW
ARCHITEKTURY
```

### Strana 10

```text
Dataflow architektura
■ není von Neumannovská architektura (nemá program a PC)
■ provádí interpretaci grafu toku dat



             Program



           Dataflow graf



        Interpretace grafu
```

### Strana 11

```text
Graf toku řízení
Uzel grafu
                X
                                  Z=X+Y
                             +

                   Y

Provedení uzlu (firing)
   2
                                                9
               +                           +

   7      Příchod dvou událostí      Nová událost
```

### Strana 12

```text
Typy uzlů
         1 3

     +    >    T   F   T   F   BARIERA




    +     >    T   F   T   F   BARIERA
```

### Strana 13

```text
Příklad
         x
                        -
                                          z
                                     +
         y              x


Uložení grafu toku dat v paměti aktivit


   x
                       sub
                         x     PB
                         y     PB             add
                                               a
                                               b
                       mult
                         x    PB
   y                     y    PB
```

### Strana 14

```text
Dataflow procesor, statický
                   Operation Unit



                  Instruction Queue


 Update Unit                                  Fetch Unit


                    Activity Store


                                      Read / Write
Message passing
                                      Read
```

### Strana 15

```text
Jazyky pro Dataflow

■ Hlavní požadavek – single assignment rule
   – Proměnná se může vyskytovat na levé straně přiřazení
      pouze jedenkrát (v oblasti kódu, kde je používána)
■ Příklad jazyků
   – VAL, Id, LUCID
■ Dataflow program je přeložen na dataflow graf, což je
  orientovaný graf s pojmenovánými uzly, které reprezentují
  instrukce, a hranami, reprezentujícími závislosti mezi
  instrukcemi
    – (obdobný grafu závislostí, používaným v překladačích)
```

### Strana 16

```text
  Příklad v jazyce VAL
function Stats(x,y,z: real             x             y           z
          returns real,real);
  let                                                            +
    Mean := (x + y + z)/3;
                                  ^2       ^2       ^2
    StDev := SQRT((x**2 + y**2
                      + z**2)/3                                  +         3
                                                +
                   - Mean**2);
   in                                  +                             /
    Mean, StDev                                     3
  endlet                                                                 Mean
endfun                                      /               ^2

                                                     *

                                                     √

                                                    StDev
```

### Strana 17

```text
   Příklad v jazyce ID, faktoriál
                                                      n
Program počítá faktoriál n! čísla n
( initial j <- n; k <- 1
   while j > 1 do
     new j <- j - 1;
     new k <- k * j;                                  F       T
   return k )
                                                          1       1

                                      1       *           >       -

                                          T       F




                                              n!
```

### Strana 18

```text
Implementace podmíněných
výrazů

                   P
       T   F


                       f           g   P
   f           g



                           T   F
```

### Strana 19

```text
  Implementace cyklů
L: Inicializace, nový kontext cyklu
D: Inkrementace proměnné cyklu                    L
D-1: proměnná cyklu na 1
L-1: nastavení původního kontextu                               P
                                              T       F

                                      D
                                                          D-1
                                          f

                                                          L-1
```

### Strana 20

```text
■ Požadavek
    –   <opcode, operand, target>
■ Výsledek
    –   <result, target>
■ Zdroj paralelismu - větší počet operačních jednotek, které
  pracují paralelně
■ Problém - vyskytnou-li se na jedné hraně grafu dvě události,
  může dojít ke změně jejich pořadí → potvrzení

                                               Počet operandů
                      opcode        counter    (nebo PB pro každý
                            operand 1          operand)
                            operand 2
                             target
                           acknowledge
```

### Strana 21

```text
                         *           ack

2                   3          2
     *         ni              3
                               nj
                         acknowledge
                         acknowledge
    sqrt       nl

                        sqrt        counter
           z

                               z
                               ni
```

### Strana 22

```text
Dynamický Dataflow
(Manchester architecture, 1985)
■ Každá iterace smyčky nebo vyvolání podprogramu by měla být
  možná paralelně (jako samostatný podgraf)
■ Jeho replikace je jen ‚konceptuální‘
■ Každá značka má
   – adresu instrukce, pro kterou jsou data určena
   – kontextové informace
■ Každá hrana je soubor (bag) který může obsahovat libovolné
  množství značek s různými tagy
■ Operaci je možné vykonat, pokud má na vstupech všechna
  potřebná data (s identickými tag-y)
```

### Strana 23

```text
Dataflow procesor, dynamický
                                          Program memory


                                     Matched
                                     tokens
                                     sets
     Data tokens
                   Matching Unit
                                                Fetch Unit


 Token Queue


                   Processing Unit
    Data tokens                            Enabled instructions


                          Opcode
                     Literal / constant
                      Destination s1
                             …
                      Destination sn
```

### Strana 24

```text
    Dynamic Dataflow Architectures
( následující tři slidy od Onur Mutlu, Computer Architecture: Dataflow (Part I)
■
■   Allocate instruction templates, i.e., a frame, dynamically to
    support each loop iteration and procedure call
    ❑   termination detection needed to deallocate frames

■   The code can be shared if we separate the code and the
    operand storage



               a token                   <fp, ip, port, data>

                               frame              instruction
                               pointer              pointer
```

### Strana 25

```text
A Frame in Dynamic Dataflow
1   +     1     3L, 4L       Program                                             b
                                                     a
2   *     2     3R, 4R
3    -    3        5L
                                                 1                       2
                                                         +                   *7
4   +     4        5R
5   *     5        out                                   x                       y
                               <fp, ip, p , v>

                                                     3       -           4   +
1
2
3    L         7                                                 5   *
4
                              Frame
5
    Need to provide storage for only one operand/operator
```

### Strana 26

```text
Monsoon Processor (ISCA 1990)
op r d1,d2          Instruction
              ip       Fetch
Code


             fp+r    Operand
                                    Token
                      Fetch
Frames                              Queue


                        ALU



                      Form
                      Token



                          Network       Network
```

### Strana 27

```text
REDUKČNÍ
POČÍTAČE
```

### Strana 28

```text
Redukční počítač

■   Funkcionální programování / založené na redukci výrazů
■   Redukce, nahrazení části výrazu jeho hodnotou
■   Příklad
       𝑥∗𝑦+ 𝑥−𝑦
V jazyce LISP
      (+ (* x y) (- x y))
Pro redukční počítač se rozdělí do sekvencí (vymezenou < … > )
     +< ∗< 𝑥 𝑦 > − < 𝑥 𝑦 > >
Pro vstupní hodnoty / argumenty x=3, y=2
       +< ∗< 3 2 > − < 3 2 > >
       +< 6 1 >
        7
```

### Strana 29

```text
Redukční architektura,
stromová
T uzly: procesory a komunikace   1, rozdělení L-uzlů na redukční pole
                                 2, provedení redukce
L uzly: paměti                   3, posuv v paměti L-uzlů
```

### Strana 30

```text
    Redukční architektura,
    stromová




+    <   (   *   <   3   2   (   -   <   3   2
```

### Strana 31

```text
Redukční architektura,
stromová




+    <   6               1




7
```

### Strana 32

```text
Redukční počítače ALICE

■ Založen na rekurzivně vyčíslitelných funkcích
■ Funkce jsou zapsány pravidly
   – Pravidla jsou prvního řádu a mohou zahrnovat rekurzi
Příklad, připojení prvku do seznamu
       Append(x, nil) ← x::nil
       Append(x, e::L) ← e:: Append(x, L)
Příklad, výpočet faktoriálu (pro n>0)
       Factorial(n) ←         FactB(0, n)
       FactB(i, i) ← i
       FactB(i, i+1) ← i+1
       FactB(i, j) ← FactB(i, mid) * FactB(mid, j)
              kde mid= (i+j) div 2
```

### Strana 33

```text
    Výpočet faktoriálu rozkladem
                                                            Factorial(5)
R1 Factorial(n) ← FactB(0, n)
R2 FactB(i, i) ← i
R3 FactB(i, i+1) ← i+1
R4 FactB(i, j) ← FactB(i, mid) * FactB(mid, j)                 FactB(0,5)


Factorial(5)         Factorial(5)                                  *
                                                      FactB(0,2)       FactB(2,5)


FactB(0,5)           FactB(0,5)                            *                *

                                         FactB(0,1) FactB(1,2)   FactB(2,3) FactB(3,5)

               FactB(0,2)   FactB(2,5)
```

### Strana 34

```text
     Výpočet faktoriálu rozkladem
                                                                           Factorial(5)
R1 Factorial(n) ← FactB(0, n)
R2 FactB(i, i) ← i
R3 FactB(i, i+1) ← i+1
R4 FactB(i, j) ← FactB(i, mid) * FactB(mid, j)
                                                                               FactB(0,5)
Factorial(5)       Factorial(5)                Factorial(5)
                                                                                    *
                                                                     FactB(0,2)         FactB(2,5)
FactB(0,5)            FactB(0,5)                  FactB(0,5)
                                                                           *                 *
    120                   *                           *
                                                                                                 FactB(3,5)
             FactB(0,2)       FactB(2,5)   FactB(0,2) FactB(2,5)

                                                                       1        2        3           *
                  2              60           2                *

                                                                   FactB(3,5)       FactB(3,4)       FactB(4,5)


                                                          3           20                     4           5
```

### Strana 35

```text
Redukční počítače, ALICE

■ Funkce je realizována pakety

                   ARGUMENTY                  POČET     SEZNAM
ID   FUNKCE                       STATUS
                    HODNOTA                 REFERENCI   SIGNÁLů

■ Funkce je redukovatelná, pokud má k dispozici všechny
  argumenty
■ Pokud nemá, musí čekat, dokud neobdrží signály, že jsou již k
  dispozici (v počtu referencí)
■ Pokud je redukovaná, je k dispozici výsledná hodnota –
  signály všem, kteří ji čekají (v seznam signálů)
```

### Strana 36

```text
    Redukční počítače, ALICE
R1 Factorial(n) ← FactB(0, n)
R2 FactB(i, i) ← i
R3 FactB(i, i+1) ← i+1                                                         n:R3
R4 FactB(i, j) ← FactB(i, mid) * FactB(mid, j)
                                                                               p:R3
                                                          l:R4                 q:R3
                i:R1                 i:R4                m:R4                    r:R4
i   Factorial      j   i   FactB       k j   i    *         l m      i     *        l m

j   Integer        5   k   Integer      0    l   FactB     [0] [2]   l     *        n p

                       j   Integer      5    m   FactB    [2] [5]    m     *        q r

                                                                     n   FactB     [0] [1]

                                                                     p   FactB     [1] [2]

                                                                     q   FactB     [2] [3]

                                                                     r   FactB     [3] [5]
```

### Strana 37

```text
Redukční počítače, ALICE
Čekání na operandy
i      *        l m      2   =   i      *       l m   1   =

l    FactB     [0] [2]   0   i   l   Integral    2    0   i

m    FactB     [2] [5]   0   i   m   Integral   60    0   i


i      *        l m      2   =   i      *       l m   0   =

l   Integral     2       0   i   l   Integral    2    0   i

m   FactB      [2] [5]   0   i   m   Integral   60    0   i



                                 i   Integer    120   0   =
```

### Strana 38

```text
   VON NEUMANOVSKÉ
       ARCHITEKTURY
VLIW, VEKTOROVÉ, ZŘETĚZENÉ
MIMD, PROPOJOVACÍ SÍTĚ
```

### Strana 39

```text
Von Neumannovská
architektura
                     CPU – Central Processing Unit
     MEMORY          ■ Řídící jednotka: řídí
                       fungování procesoru,
                       obsahuje PC a IR,
       CPU             obstarává signály
 CONTROL UNIT    R   ■ ALU – Aritmeticko logická
                 E     jednotka, provádí operace
                       profesoru.
                 G
     ALU         S   ■ Registry – akumulátor,
                       dále například datové či
                       adresové registry, registr
                       příznaků…
   I/O DEVICES       ■ Sběrnice – adresová,
                       datová, řídící
```

### Strana 40

```text
ZŘETĚZENÉ
PROCESORY
```

### Strana 41

```text
Zřetězené procesory

■ Lineárně propojené procesory
■ Řešení úloh s proudovým charakterem
■ Data procházejí postupně jednotlivými procesory
■ Aritmetické zřetězení / Zřetězení instrukcí




        P1         P2         P3                    Pn
```

### Strana 42

```text
Zřetězené procesory,
aritmetické zřetězení
Sčítání reálných čísel
             X= sx * mx*2ex       Y= sy * my*2ey

                    Exp. comparation


                     Mantisa shifting


                           Addition


                         Normalization

                                   Z=X+Y
```

### Strana 43

```text
            10^3, 10^2                      0,9504, 0,82

                                    REGS

    Compare
   exponents
                    3-2=1
                            1
     REGS
                    3
Choose exponent
                            2    Align Mantisas       0.082

                                     REGS

                                                      0.9504 +
                            3   ADD/SUB Manisa        0,082 =
                                                      1,0324
    REGS                             REGS


Adjust exponent
                    4
                            4   Normaliza results     0,10324


    REGS                             REGS
```

### Strana 44

```text
RISC, pětifázové zpracování
  IF    ID    EX    MEM    WB


IF: Načtení instrukce
ID: Dekódování instrukce
     – Specifické pro RISC,
     – Určení operandů, načítání z lok. paměti / registrů,
         adresy cílů skoků
EX: Vykonání instrukce
MEM: Alokace dat v paměti, pokud je třeba
     – jednocyklové instrukce -> pouze posílají výsledky dále
     – dvoucyklové instrukce (R1 [adresa]) načítají data z
         paměti
WB: Zápis do lok. paměti / registrů, další např. řídící akce
```

### Strana 45

```text
Pipeline
Zřetězené procesory, RISC



     IF     ID    EX   MEM   WB

            IF    ID    EX   MEM   WB

                  IF    ID   EX    MEM   WB

                        IF   ID    EX    MEM   WB

                             IF    ID    EX    MEM   WB
```

### Strana 46

```text
Zřetězené procesory,
problémy
■ Strukturální hazardy
   – Instrukce v zřetězené lince požadují stejný prostředek
       (přístup do paměti)
■ Datové hazardy
   – Výsledek předchozí instrukce v zřetězené lince je
      očekáván jinou – následující instrukcí
■ Řídící hazardy
   – Podmíněné skoky
```

### Strana 47

```text
Strukturální hazardy
Současný přístup ke zdroji (paměti, sběrnici) na různých stupních
zřetězení
       IF     ID    EX    MEM     WB

              IF     ID     EX    MEM     WB

                     IF     ID     EX    MEM   WB

                            IF     ID     EX   MEM   WB

                                    IF    ID   EX    MEM   WB


Řešení: pozdržení vykonávání
        oddělení instrukční a datové paměti
```

### Strana 48

```text
Datové hazardy, typy
                                                     5ti fázové zřetězení?
■   RAW (Read after Write)
     ADD R1, T1, T2
     SUB T3, R1, T4
      write SUB musí být zapsáno až po zapsání ADD
■   WAR (Write after Read)
     ADD T1, R1, T2
     SUB R1, T3, T4
      write SUB musí být zapsáno až po načtení ADD
■   WAW (Write after Write)
     ADD R1, T1, T2
     SUB R1, T3, T4
      write SUB musí být načteno až po zapsání ADD
```

### Strana 49

```text
    Datové hazardy, řešení
Přeposíláním
ADD R3, R6, R5        IF     ID     EX    MEM     WB

SUB R4, R3, R5               IF     ID     EX    MEM     WB

OR R6, R3, R7                        IF     ID     EX    MEM     WB

AND R8, R3, R9                              IF     ID     EX    MEM     WB

XOR R10, R3, R11                                   IF     ID     EX    MEM     WB

Pozastavením (stall)
    Snižuje propustnost linky
Překladačem
    Překladač zamění provádění instrukcí tak, aby data byla k dispozici včas
    Překladač vloží instrukci nop, snižuje propustnost linky
```

### Strana 50

```text
Řídící hazardy
                             [pc]      IF   ID    EX    MEM   WB
■ Pokud se zpracovává
  podmíněný skok,            [pc+04]         IF   ID     EX   MEM   WB

  následné instrukce
  nemají být vykonány        [pc+08]               IF    ID   EX    MEM    WB


■ Vyprázdnění (flush)        [pc+0c]                     IF    ID   EX     MEM   WB


      [pc]: beq t1,t2,30 …   [pc+20]                           IF    ID    EX    MEM   WB




                             [pc]      IF   ID    EX    MEM   WB


                             [pc+04]        IF    ID
                                                                          FLUSH
                             [pc+08]              IF


                             [pc+34]                     IF   ID    EX    MEM    WB
```

### Strana 51

```text
Řídící hazardy, řešení

■ Odložení vykonání následujících instrukcí (stall)
■ Předvídání, dynamické předvídání
   – Vytváření a uchovávání záznamů o provedení –
      neprovedení skoku pří vykonání instrukce
■ Zaměněním pořadí instrukcí
   – Instrukce následně vykonané neovlivní provádění
     programu
```

### Strana 52

```text
Zřetězené procesory
TRANSPUTER T9000
  Instruction
     Fetch



  Instruction
  Groupping
                                                       2x
           1            2       3       4              5
  Workspace
  Workspace     Workspace
                Non-Local   Main     ALU/    Write /
   Cache
    Cache        Cache
                 Adress     Cache    FPU      Jump



  Local         Calculate Read      ALU     Jump or write
  variables     address non-local operations
                          variables
```

### Strana 53

```text
    Zřetězené procesory
a[i+1]=b[j+15]+c[k+7]        INSTRUKCE

 ldl j            1          Integer registry        stnl n (store non local)
 ldl b            1                                   word´[Areg @ n] ← Breg
 wsub             2          Areg, Breg, Creg         Areg´ ← Creg
 ldnl 15          2,3
--------------------------   Instrukce                wsub (word subscript)
 ldl k            1                                    Areg´ ← Areg +word[Breg]
 ldl c            1          ldl n (load local)        Breg´ ← Creg
 wsub             2            Areg´ ← word[Wptr @ n] Creg´ ← undefined
 ldnl 7           2,3          Breg´ ← Areg
 add              4            Creg´ ← Breg           add
--------------------------                             Areg´ ← Breg + Areg
 ldl i            1          ldnl n (load non local)   Breg´ ← Creg
 ldl a            1            Areg´ ← word[Areg @ n] Creg´ ← undefined
 wsub             2
 stnl 1           2,5
```

### Strana 54

```text
VLIW
```

### Strana 55

```text
  VLIW - Very Long Instruction
  Word
■ jediný tok řízení, který řídí všechny procesory
■ každá instrukce - samostatné pole s operačním kódem pro všechny
  procesory
   – jediný PC, který prochází program
   – instrukce jsou prováděny sekvenčně
   – instrukce také určují, jak probíhá komunikace mezi procesory.
      Jsou v nich uloženy informace o odesílateli, příjemci a velikosti
      dat. Tyto informace s ohledem na časování generuje kompilátor


               MEM OP     ALU OP     ALU OP         BR Op
```

### Strana 56

```text
VLIW (Very Long Instruction
Word)
■ Překladač organizuje nezávislé instrukce do jednoho
  dlouhého instrukčního slova
   – Zvyšuje nárok na překladač, ale snižuje ‚složitost‘ HW
■ Například ELI-512 (512 bitů)




                             Nejlepší: Pracují všechny procesory
                             Nejhorší: Pracuje jeden procesor
```

### Strana 57

```text
VLIW - Very Long Instruction Word
                                               MEM OP          PAMĚŤ




NAČTENÍ INSTRUKCE
                    DEKÓDOVÁNÍ
                                               ALU OP




                                                BR Op


                                 IF   ID       EX   MEM   WB
                                               EX
                                               EX

                                          IF   ID   EX    MEM    WB
                                                    EX
                                      …
```

### Strana 58

```text
    TRACE 7/300
                             Instrukční tok (256 bitů)




BRANICHING   INTEGER   INTEGER     MEMORY       MEMORY   FLOAT     FLOAT




                           INT REGS                         FLOAT REGS




                        MEMORY SUBSYSTEM
```

### Strana 59

```text
     Překlad pro VLIW
C=(2A+3B)*2I               GRAF ZÁVISLOSTÍ                                  DLOUHÉ INSTRUKCE
Q=(C+A+B)-4(I+J)
  [1] LD A                            [2]         [6]
                                                                BRA   IN0    IN1    ME0    ME1    FL0     FL1
                         [1]                            [10]
  [2] LD B                                                                          LD A   LD B
  [3] t1=A*2
  [4] t2=B*3       [3]         [13]         [4]   [7]   [11]                        LD I   LD J
  [5] t3=t1+t2
  [6] LD I
  [7] t4=2*I       [5]                                   [12]                                      2*A    3*B
  [8] C=t4*t3                                                         2*I     I+J                 t1+t2   A+B
  [9] ST C                                  [8]
                                                                      4*t5                        t4*t3 C+t7
  [10] LD J
  [11] t5= I+J      [14]                    [9]                                     ST C          t8-t6
  [12] t6= 4+t5
                                                                                    ST Q
  [13] t7=A+B
                                        [15]
  [14] t8=C+t7
  [15] Q=t8-t6
                                        [16]
  [16] ST Q
```

### Strana 60

```text
VLIW - Vlastnosti
■   Výhody
      – Jednoduchý hardware
      – Dobře škálovatelné
■   • Nevýhody
      – Podmíněné skoky (když jedna instrukce provede skok, ostatní instrukce
               mají problém)
      – Problém toku dat (instrukce zpracovávané v jednom kroku nemohou
               navzájem používat své výsledky)
          ■   Některé závislosti nejsou staticky rozpoznatelné v době překladu (např.
              aliasing ukazatelů, oddělený překlad, dynamické sestavování) =>
              překladač musí být konzervativní a výsledná výkonnost je nižší než při
              schopnosti rozpoznat všechny závislosti
          ■   Některé latence nejsou odhadnutelné v době překladu (např. latence
              instrukcí LOAD a STORE kvůli případnému Hit nebo Miss v cache)
          ■   některé VLIW používají softwarově řízenou lokální paměť místo datové
              cache; jinde překladač předpokládá 100% Hit-Rate
     –   Velikost programu - synchronizační NOPy jsou u VLIW navíc
     –   VLIW nejsou softwarově zpětně kompatibilní jako superskalární
         procesory (i když existují cesty, jak toho dosáhnout)
```

### Strana 61

```text
    VLIW vs superskalární procesory
■   Statické superskalární procesory (Static, In-Order     VLIW
    Superscalar)
     – Zpracovávají více instrukcí paralelně ale v
          programovém pořadí
     – Typická šířka 3-4 instrukce
     – Paralelní provádění může zahájit pouze
          limitovaná kombinace typů instrukcí
          („párovatelné instrukce“)
■   VLIW procesory
     – Instrukce obsahuje více paralelních operací       SUPERSCALAR
     – Konflikty detekuje a řeší překladač (téměř
         výlučně)                                        DISPATCHER
     – Šířka instrukcí typicky 6-10 paralelních
         operací
■   Dynamické superskalární procesory (Dynamic, Out-
    Of-Order Superscalar)
     – Zpracovává více instrukcí paralelně i mimo
          programové pořadí
     – Dnes typicky podporuje spekulativní provádění
          instrukcí za skokem a někdy i spekulativní
          provádění Load/Store instrukcí
```

### Strana 62

```text
  SIMD
VEKTOROVÉ PROCESORY
```

### Strana 63

```text
SIMD

■ Vektorové procesory (ale nejen ony, array computers)
■ Obsahuje instrukce pro práci s poli – vektory dat
■ 1976: Cray-1 Superpočítač (Seymour Cray)
■ Použití dříve u GPU, dnes již běžná součást architektur
```

### Strana 64

```text
Vector / array computers
■ Array computers (mřížkové počítače)
   – Obsahuje jednotky (processing elements) zvládajíci ALU, a
       Floating point + registry
   – Pracují paralelně a synchronizovaně
■ Vector computers (vektorové počítače)
   – Jednotky jsou jednodušší, specializované
   – Pracuji zřetězeně (deep pipelining, pipelined SIMD).

PE1    PE1     PE1      PE1         MEM      ADD     MUL     BR
LD0    LD1     LD2     LD3          LD0
ADD0   ADD1    ADD2    ADD3         LD1      ADD0
MUL0   MUL1    MUL2    MUL3         LD2      ADD1    MUL0
…      …       …       …            LD3      ADD2    MUL1
                                             ADD3    MUL2
                                                     MUL3
```

### Strana 65

```text
     Vektorový procesor (VMIPS)

                    MAIN MEMORY
                                            FP ADD/SUB

                     VECTOR
                      LD/ST                  FP MULT


                                              FP DIV


                                             INTEGER


                                             LOGICAL

                       Vektorové registry
Skalární registry
```

### Strana 66

```text
Vektorový procesor (VMIPS)
ADDVV.D V0,V1,V2
MULVV.D V3,V4,V5   Instrukční sada
DIVVS.D V6,V7,F1


           V0
           V1                        FP ADD/SUB
           V2
           V3                         FP MULT
           V4
           V5
           V6                          FP DIV
           v7


            F0                        LOGICAL
            F1
            F2
                                      INTEGER
            F3
```

### Strana 67

```text
  Příklad: výpočet Y = a * X + Y
Sekvenční                                  Vektorové
LD F0, a                                   LD F0, a ; load scalar a
ADDI R4, Rx, #512 ; last address to load   LV V1, Rx ; load vector X
Loop:                                      MULVS.d V2, F0, V1 ; vector-scalar
LD F2, 0(Rx) ; load X(i)
                                                                  ; multiply
MULTD F2, F0, F2 ; a * X(i)
                                           LV V3, Ry ; load vector Y
LD F4, 0 (Ry) ; load Y(i)
                                           ADDVV.d V4, V2, V3 ; add
ADDD F4, F2, F4 ; a x X(i) + Y(i)
                                           SV Ry, V4 ; store the result
SD F4, 0 (Ry) ; store into Y(i)
ADDI Rx, Rx, #8 ; increment index to X
ADDI Ry, Ry, #8 ; increment index to Y
SUB R20, R4, Rx ; compute bound
BNZ R20, Loop ; check if done
```

### Strana 68

```text
 Načítání vektoru, Stride
C=A x B                   A                     B
             0   1    2   3   4   5     0

                                        6

                                        12

                                        18

                                        24

                                        30




 C[0]=A[0]*B[0]+A[1]*B[6]+A[2]*B[12] + … A[5]*B[30]
 C[0]=A[0]*B[0]+A[0+1]*B[0+6]+A[1+1]*B[6+6] + … A[4+1]*B[24+6]


  LV V1, 0(Ra)
  LVWS V2, 0(Rb), 6
  MULVV V3, V1, V2
```

### Strana 69

```text
SIMD – Vektorový procesor

UMA –Uniform Memory Access


Datová sběrnice
                          ŘÍDÍCÍ
                        JEDNOTKA
                                          Řídící sběrnice


                  P      P                     P

                        Propojovací síť

                  M      M                     M
```

### Strana 70

```text
SIMD – Vektorový procesor

NUMA – Non-Uniform Memory Access


Datová sběrnice
                          ŘÍDÍCÍ
                        JEDNOTKA
                                           Řídící sběrnice


                  P      P                      P

                  M      M                      M


                         Propojovací síť
```

### Strana 71

```text
MSIMD – Multiple SIMD

               CU1      CU2                    CUn

                      Propojovací řídící síť


               PM1      PM2                    PMn


                     Propojovací datová síť




■ Dělení procesorů na nezávislé skupiny
■ Dynamické alokování procesorů
```

### Strana 72

```text
Výhody / nevýhody SIMD
Výhody
■   Jednodušší než MIMD
■   Menší nároky na paměť
■   Jeden instrukční tok a synchronizace zjednodušuje programy
■   Odpadá režie se složitou synchronizací mezi procesy, která je u MIMD
■   Rychlejší komunikace mezi procesory než u MIMD
     – Menší latence
     – Menší režie na struktury komunikačních paketů, směrování atd.
Nevýhody
■ Ne všechny problémy jsou datově paralelizovatelné
■ Pokles výkonnosti u programů s mnoha podmíněnými skoky
■ Nejsou vhodné při malém počtu procesorů (neexistuje něco jako
  „starter kit“)
■ Vyžadují ne úplně běžné procesory
```

### Strana 73

```text
Granularita paralelismu
■ uvnitř instrukcí - INTRA INSTRUCTION
    –   nejjemnější paralelismus
                                                                   Načtení op. kódu
■ mezi instrukcemi INTER INSTRUCTION
    –   některé instrukce se provádějí paralelně, ale není to
        vidět na úrovni programovacího jazyka
                                                                PC++                  ALU
    –   zřetězení u RISC
    –   více jednotek (T10000)
■ mezi příkazy
    –   vektorové počítače
    –   specializované koprocesory (FPU)
■ mezi bloky procesu (vlákna, thready)
    –    parbegin
    –      thread1;
    –      thread2;
    –    parend                                                    F o rk
■ mezi procesy
    –   zpravidla nemají sdílenou paměť
    –   mohou být odděleně kompilovány
```

### Strana 74

```text
INTERAKCE V
PARALELNÍCH
 SYSTÉMECH
 Petr Hanáček, František Zbořil ml.
             – 2024
```

### Strana 75

```text
Komunikace
■ přenáší data
   – „Předávání informací mezi procesy (procesory, vlákny, ...)“
■ Prostředky pro komunikaci
   – Sdílená paměť
         ■   skutečná x simulovaná
         ■   boj o sběrnici, cache, lokalita odkazů (busy waiting !)
         ■   řešení konfliktů při zápisu
         ■   obtížně použitelná pro synchronizaci
     –   Zasílání zpráv
         ■   kanály
              – synchronní x asynchronní (kapacita)
              – jednosměrný x obousměrný (ACK)
         ■   volání vzdálených procedur (RPC)
         ■   všesměrové vysílání (broadcasting)
              – úmyslné posílání zpráv všem
              – vysílání každému procesu
              – záplava - na jednu zprávu odpoví procesy jinou b.
                  zprávou
```

### Strana 76

```text
Synchronizace
■ nepřenáší se data
    –   „Zajištění požadovaných časových vztahů mezi událostmi“
■ Prostředky
        ■   zasílání zpráv (nejlépe synchronní)
        ■   randevous (RPC - remote procedure call)
        ■   semafor
        ■   monitor
        ■   bariéra

■   Typické synchronizační úlohy
    –   soupeření
        ■   vzájemné vyloučení
        ■   čtenáři x písaři
    –   kooperace
        ■   dohoda
        ■   producent - konzument

■ Synchronizace v distribuovaných systémech
   – Logický čas
   – Časová razítka / tokeny
```

### Strana 77

```text
             Sdílená paměť a předávání
             zpráv u MIMD
                                 ■ Multitasking                Předávání zpráv           Sdílená
             P                       – 1 cpu
                                     – přepínání kontextu
             M
                                     – virtuální procesory     simulováno SW            Ano
                                 ■ sdílená paměť
CPU1                      CPU1
                                     – Cache
              M
                                     – těsně vázané
                                     – boj o sběrnici          simulováno SW, HW        Ano
                                 ■ virtuální sdílená paměť
CPU                       CPU        – all cache               simulováno SW, HW        simul. HW
M                         M
                                     – spojení caches komunikačními kanály
                                     – navenek se tváří jako společný (jediný) adresový prostor
                                 ■ předávání zpráv
          Propojení
                                                               Ano                     simul. SW
                                     – volně vázaná architektura
    CPU           CPU
                                     – počítačové sítě
      M               M              – propojeny pouze procesory
```

### Strana 78

```text
Vlastnosti sdílené paměti /
předávání zpráv
■ Sdílená paměť
   – všechny procesy mají přístup do společného
       paměťového prostoru
   – řešení současného přístupu k jedné buňce paměti
        ■   Exclusive-read, Exclusive-Write (EREW)
        ■   Concurrent-Read, Exclusive-Write (CREW)
        ■   Exclusive-Read, Concurrent-Write (ERCW)
        ■   Concurrent-Read, Concurrent-Write (CRCW)
■ Předávání zpráv
   – každý procesor má svůj adresový prostor
   – procesory mají vlastní paměť - komunikace pomocí zpráv
```

### Strana 79

```text
Propojovací sítě
■ Použití propojovacích sítí
   – Propojit procesory se sdílenou pamětí
   – Propojit procesory navzájem
■ Typy propojovacích médií
   – Statické
   – Dynamické
   – Sdílené (sběrnice)
   – Přepínané
■ Vlastnosti propojovací sítě ovlivňují vhodnost jednotlivých typů
  algoritmů a ovlivňují efektivnost toku dat
```

### Strana 80

```text
Statické sítě
■ Všechny uzly jsou procesory
■ Kanály jsou spojnice mezi uzly (procesory)
■ Používají se pro architektury bez sdílené paměti
■ Vlastnosti
   – Průměr (Diameter): Délka nejdelší z nejkratších cest mezi
       všemi dvojicemi uzlů
   – Šířka bisekce (Bisection width): Minimální počet hran, které
       spojují dvě přibližně stejně velké poloviny sítě
   – Konektivita (Arc connectivity): Minimální počet hran, které
       je nutné odstranit pro rozdělení sítě na více částí, také
       stupeň uzlu
   – Velikost (Network size): Počet uzlů v síti
   – Cena (Cost): Počet hran v síti
```

### Strana 81

```text
■ Úplné propojení             ■ Hvězda
   –   Diametr = 1               –   Diametr = 2
   –   Konektivita = p-1         –   Konektivita = 1
   –   Šířka bisekce = p2/4      –   Šířka bisekce = (p-1)/2
```

### Strana 82

```text
k-ární n-rozměrná kostka
               Kartézký součin n lineárních
               polí s k uzly
               Počet uzlů k^n
               Například: Hyperkostka,
               kružnice, torus,...


              2 1   2 2   2 3       2 4
```

### Strana 83

```text
 n-rozměná kostka (k=2)


2 1   2 2   2 3          2 4   Populární v starších počítačích s
                               předáváním zpráv
                               (intel iPSC, NCUBE)




■ Počet uzlů |N| = 2n
■ Diametr = n
■ Konektivita = n
■ Šířka bisekce = 2n-1
```

### Strana 84

```text
k-árni n-rozměná kostka (mřížka)




■ Počet uzlů |N| = kn
■ Diametr = n(k-1)
■ Konektivita = 2n
■ Šířka bisekce = kn-1
```

### Strana 85

```text
k-árni n-rozměná kostka (torus)




  n=1 jednosměrný    n=2, jednosměrný     n=3, obousměrný

JEDNOSMĚRNÝ                      OBOUSMĚRNÝ
■ Počet uzlů |N| = kn           ■ Počet uzlů |N| = kn
■ Diametr = n(k-1)              ■ Diametr = n[k/2]
■ Konektivita = 2n              ■ Konektivita = 4n
■ Šířka bisekce = kn-1          ■ Šířka bisekce = 2kn-1
```

### Strana 86

```text
Ring, Chordal ring
■ Ring o k uzlech je k-ární 1rozměrný Torus
■ Chordal ring (ring + propojení uzlů ve vzdálenosti ‚l‘, případně
  ve vzdálenostech z množiny 𝐿 = 𝑙1 , 𝑙2 … 𝑙𝑘
```

### Strana 87

```text
d-arní strom
               Strom, kde žádný uzel nemá
               více než d potomků
               Obvykle binární (d=2)


               ■ Diametr = 2h (pro hloubku
                 stromu h)
               p pro jakýkoliv strom
               2*(logd p) pro vyvážené stromy
               ■ Konektivita = 1
               ■ Šířka bisekce = 1
```

### Strana 88

```text
Dynamické sítě

■   Prvky jsou buď procesory, paměťové buňky, nebo přepínače
■   Často se používají pro implementaci architektur se sdílenou pamětí
■   Sběrnice, křížové přepínače (crossbar), dynamické sítě, fat tree
■   Příklad: sběrnice (bus)
     – Cena ϴ(p), propustnost ϴ(1)
■   Příklad: křížový přepínač (crossbar)
     – Cena Ω(p2), propustnost O(p), neblokující
     – Diameter = 1, Konektivita = 1, Bisekce = p
■   Neblokující
     – Lze spojit vždy libovolné dva uzly, které jsou k dispozici
■   Přenastavitelné
     – Lze změnit trasu propojení pro vyřešení konfliktu
■   Blokující
     – Nelze současně propojit libovolné dva uzly
```

### Strana 89

```text
Křížový přepínač
Příklad: křížový přepínač (crossbar)
     Cena Ω(p2), propustnost O(p), neblokující
     Diameter = 1, Konektivita = 1, Bisekce = p
Pro p>m některé procesory nemají možnost přistupovat k
paměti
```

### Strana 90

```text
Fat tree
■ Řeší problém větší zátěž komunikací blíže ke kořenu stromu
■ Dynamická volba kanálu pro komunikaci
```

### Strana 91

```text
Shuffle and Exchange
Exchange – inverze posledního bitu      Shuffle – levý shift
0    000 -> 001         0         0     0   000 -> 000         0             0
1    001 -> 000         1         1     1   001 -> 010         1             1
2    010 -> 011         2         2     2   010 -> 100         2             2
3    011 -> 010         3         3     3   011 -> 110         3             3
4    100 -> 101         4         4     4   100 -> 001         4             4
5    101 -> 100         5         5     5   101 -> 011         5             5
6    110 -> 111         6         6     6   110 -> 101         6             6
7    111 -> 110         7         7     7   111 -> 111         7             7



        000       001       010   011         100    101            110     111




    Exchange dle bitů cílového uzlu
    Příklad: cílový 110 z uzlu 010
       EXCHANGE (pro 110) 010 -> 011, SHUFFLE 011                  -> 110
       EXCHANGE (pro 110) 110 -> 111, SHUFFLE 111                  -> 111
       EXCHANGE (pro 110) 111 -> 110
```

### Strana 92

```text
Přepínače
■ Data přechází přes přepínače, ne přes uzly (např.
  hyperkostka)
■ Přepínač … přeposílá vstup na jeden nebo více výstupů
■ Realizace, fyzický, multiplexor / demultiplexor
■ Buffer v případě konfliktů
■ Možné směrovací mechanismy
```

### Strana 93

```text
Multistage indirect networks
■   Many such networks: Omega, Butterfly, Benes, ...
     – Connect p processors to p memory banks with Q(p lg p) switches
     – Q(lg p) stages of Q(p) switches each
■   Blocking network
     – Even if processors address distinct memory banks (permutation
          routing), can still have contention for switching elements
■   Omega network (p = 8)

         P                  Switches               M
```

### Strana 94

```text
Síť Omega, konflikty
                           000
                           001
                           010
 ->101                     011
                           100
                     101   101
                           110
         101   101         111


                           000
                           001
                           010
 ->101                     011
                           100
 ->100                     101
                           110
                           111
```

### Strana 95

```text
 Sběrnice
 ■ Obvykle pro sdílený prostředek (paměť)
 ■ Cena ϴ(p), propustnost ϴ(1), diametr=1
 ■ Obtížná škálovatelnost                 Data bus
                                                               Adress bus

            M
            E
            M
                       P1          P2          P3         P4
 ■ Zvýšení propustnosti – lokálni cash


           M        CACHE 1     CACHE 2     CACHE 3    CACHE 4
           E
           M
                      P1          P2          P3         P4

p procesorů, přístup k datům v paměti / cache tcycle
Každý proces načítá k dat, 50% dat v cache
0.5 * tcycle * k + 0.5 * tcycle * kp -> 0.5 * tcycle * kp pro velké p
```

### Strana 96

```text
Cache, koherence
```

### Strana 97

```text
Cache, koherence
```

### Strana 98

```text
Cache, koherence
```
