# Razeni a vyhledavani

Oficialni slidy extrahovane z PDF. Text je automaticky vytazeny pres `pdftotext -layout`; u obrazkovych nebo diagramovych stran kontroluj originalni PDF.

## Metadata

| Pole | Hodnota |
|---|---|
| Zdroj | [[raw/2526_Razeni_vyhledavani_v7.pdf]] |
| Soubor | `2526_Razeni_vyhledavani_v7.pdf` |
| Stran | 61 |
| PDF title | Prezentace aplikace PowerPoint |
| Creator | Microsoft® PowerPoint® LTSC |
| Page size | 960 x 540 pts |

## Pouziti

- Pouzivej jako oficialni oporu pro definice, algoritmy, terminologii a slozitosti.
- Pokud je strana zalozena hlavne na obrazku, cituj stranu a zkontroluj originalni PDF.
- Pro exam historii porad preferuj `knowledge/exams/**/term-*.md`; slidy slouzi jako vykladovy zdroj.

## Text po stranach

### Strana 1

```text
ANALÝZA ALGORITMŮ
                                                                     p(n) = {1, c, log n, n, n log n, n2, nr, rn}




■   Počet procesorů                                             sekvenční     konstantní rozumný            nerozumný
                                                                alg.          alg.
     – (p) potřebných k řešení úlohy                                                     počet CPU          počet CPU
         v závislosti na velikosti instance n
■   Čas řešení potřebný k řešení úlohy v jednotkách (krocích)            t(n)
■   Cena paralelního řešení: c(n) = p(n) . t(n)
     – Algoritmus s optimální cenou: c(n)optim = tseq(n) čas pro úlohu při sekvenčním výpočtu
■   Zrychlení x Efektivnost
     – zrychlení tseq(n) / t(n)
     – Efektivnost tseq(n) / c(n) - beru v úvahu i počet procesorů
          ■    <1   neoptimální (přidá se režie)
          ■    =1   optimální
          ■    >1   ?
```

### Strana 2

```text
VYHLEDÁVACÍ
 ALGORITMY
```

### Strana 3

```text
Vyhledávání
■   Vstup: sekvence X = {x1, x2, ..., xn} a prvek x
■   Úlohou je nalézt x = xk a jeho pozici k
■   Optimální sekvenční algorimus má složitost …

    a) Pokud X není uspořádáno –

          t(n)=O(n) c(n)=O(n)
          (prohledání až všech n prvků)

    b) Pokud X je uspořádáno – binární vyhledávání
          t(n)=O(log n)        c(n)=O(log n)
          (prohledání až log n prvků)
```

### Strana 4

```text
Vyhledávání v neseřazené posloupnosti

  •Algorithm
      Looks for an element in unsorted sequence
   procedura SEARCH(S, x, k) { sequence, element, result}
  •1. for
      model
          i =with PRAM
               1 to     (Nin
                     N do  processors)
                              parallel
         read x
     endfor
  2. for i = 1 to N do in parallel
         Si = {s(i-1).(n/N)+1, s(i-1).(n/N)+2, ..., si.(n/N)}
         SEQUENTIAL SEARCH (Si, x, ki)
            - paralell Search calls SEQUENTAL Search
  endfor
  3. for i = 1 to N do in parallel
         if ki > 0 then k = ki endif
     endfor
```

### Strana 5

```text
Analýza

■ EREW
   – 1. krok = O(log n)        2. krok = O(n/N)          3.krok = O(log N)
   – t(n) = O(log N + n/N)              c(n) = O(N.log N + n)
   – Ve fázi 1. musí každý uzel znát hledaný prvek
■ CREW
   – 1. step = O(1)             2. step = O(n/N)          3.step= O(log N)
   – t(n) = O(log N + n/N)               c(n) = O(N.log N + n)
■ CRCW
   – 1. steo = O(1)             2. step = O(n/N)           3.step = O(1)
   – t(n) = O(n/N)                       c(n) = O(n) což je optimální
```

### Strana 6

```text
N-ární vyhledávání na CREW
•   Vyhledává v seřazené posloupnosti
■ Princip algritmu:
         •   Při použití binárního vyhledávání bychom mohli rozlišit, ve které polovině se prvek
             nachází (s využitím jednoho procesoru).
         •   S N procesory můžeme provést N+1 vyhledávání. V jednom kroku můžeme zjistit, v
             které části se prvek nachází
         •   Pokud se liší ukazatel u dvou následujících prozkoumaných prvků (vlevo, vpravo),
             upraví se rozsah vyhledávání
•   g je nejmenší číslo takové, že 𝑛 ≤ 𝑁 + 1 𝑔 − 1
■ Potřebujeme udělat g = [ log(n+1)/log(N+1) ] kroků
```

### Strana 7

```text
N-ární CREW vyhledávání, příklad 1
■ S={1, 4, 6, 9, 10, 11, 13, 14, 15, 18, 20, 23, 32, 45, 51}, |S|=15, hledáme 45
■ Počet procesorů N=3 … tedy g=2 jelikož 15 ≤ 3 + 1 2 − 1


                                𝑗𝑖 = 𝑞 − 1 + 𝑖 𝑁 + 1 𝑔−1

       1    4    6       9      10   11   13      14      15   18   20      23          32     45     51

      q=1            J1=4                      j2=8                      J3=12                       r=15
                     c1=right                  c2=right                  c3=right


       1    4    6       9      10   11   13      14      15   18   20      23          32     45     51

                                                                             j1=13           j2=14   j3=15
                                                                             c1=right        k=r12   c3=left


                                                                                    q=13             r=15
```

### Strana 8

_Bez extrahovatelneho textu._

### Strana 9

```text
N-ární CREW vyhledávání, příklad 2
■ S={1, 4, 6, 9, 10, 11, 13, 14, 15, 18, 20, 23, 32, 45, 51}, |S|=15, hledáme 21
■ Počet procesorů N=2 … tedy g=3 jelikož 15<=(2+1)^3 -1

       1    4    6    9   10   11   13   14      15      18     20     23      32   45    51


      q=1                                     j1=9                                        r=15     j1=18
                                              c1=right                                             c1=left

       1    4    6    9   10   11   13   14      15      18     20     23      32   45    51       r=15


                                                         q=10        j2=12               j2=15
                                                                     c2=left             c2=left

       1    4    6    9   10   11   13   14      15      18     20     23      32   45    51       r=15

                                                         q=10 r=11

                                                         j2=10    j2=11
                                                         c2=right c2=right
```

### Strana 10

```text
Vyhledávání, analýza

Potřebujeme CREW PRAM
     – t(n) = O(log(n+1)/log(N+1)) = O(logN+1(n+1))
     – c(n) = O(N.logN+1(n+1)) což není optimální
```

### Strana 11

```text
Vyhledávání na stromě

■ Topologie – Binární strom s 2n-1 procesory
■ Algoritmus
   – 1. Kořen stromu načte hledanou hodnotu a předá ji synům, a ty
      dále až k listovým uzlům
   – 2. Listy obsahují prvek nebo prvky, ve kterých se snaží hodnotu
      vyhledat, výsledkem je 0 or 1.
   – 3. Všechny tyto výsledky jsou předány kořenu
      - každý nelistový uzel spočte logický součet hodnot potomků a
      přepošle výsledek výš
      Kořen obdrží 0 – nenalezeno, 1- nalezeno
```

### Strana 12

```text
Tree Search, příklad
```

### Strana 13

```text
Tree Search, analýza

  Krok (1) má složitost O(log n),
  krok (2) má konstantní složitost,
  krok (3) složitost O(log n).

  t(n) = O(log n)           p(n) = 2.n-1

  c(n) = t(n).p(n) = O(n.log n)            což není optimální
```

### Strana 14

```text
Parallel splitting (Paralelní rozdělení)
• Úloha:
      Vstup: Sekvence čísel S a číslo m
      Výstup: Tři sekvence L, E a G takové, že
              L = {𝑠𝑖 𝜖 𝑆: 𝑠𝑖 < 𝑚}
              E = {𝑠𝑖 𝜖 𝑆: 𝑠𝑖 = 𝑚}
              G = {𝑠𝑖 𝜖 𝑆: 𝑠𝑖 > 𝑚}
• Složitost sekvenčního algoritmu je O(n)
• Paralelní řešení – máme N procesorů, které rozdělí sekvenci S na
  podsekvence Si délky n/N
```

### Strana 15

```text
 Parallel splitting, Algoritmus
(i) m zasláno všem z N procesorů (BROADCAST)
(ii) Každý processor Pi rozdělí posloupnost Si na posloupnosit Li, Ei, Gi
(iii) Všechny sekvence Li jsou spojeny do L
       ai = |Li|
       Pro všechna i, 1 < i < N se spočte suma:

       xi = σ𝑖𝑗=1 𝑎𝑗 aj       a x0 = 0

(iv) Každý procesor zapíše svou sekvenci Li paralelně id indexu z i-1+1
 Obdobně pro sekvence Ei a Gi, indexy jsou počítány od konce předešlých,
 tedy k yi se přičte x|N| a k zi se přičte y|N|
                                                                P1      P2     P3
                                                              L1=3    L2=2   L3=4


                                                          a   3 2 4

                                                          z   0 3 5



                                                                       3     5
```

### Strana 16

```text
    Parallel splitting, Příklad
■   Vstup: 13, 1, 12, 14, 3, 6, 8, 10, 2, 15, 7, 11, 4, 5, 9, číslo m = 8
■   Počet procesorů N=3
■   Rozdělíme na 3 posloupnosti o 5 prvcích a hledáme medián |Si|=5
    13, 1, 12, 14, 3                      6, 8, 10, 2, 15                   7, 11, 4, 5, 9
    L1={1, 3}                              L2={2, 6}                        L3={4, 5, 7}
    E1={}                                  E2={8}                           E3={}
    G1={12, 13, 14}                        G2={10, 15}                      G3={9, 11}
    a1=|L1|=2 a2=|L2|=2 a3=|L3|=3
            x0 = 0 x1 = σi=1..1 𝑎𝑖 = 2, x2 = σi=1..2 𝑎𝑖 = 4 x3 = σi=1..3 𝑎𝑖 = 7
    b1=|E1|=0 b2=|E2|=1 b3=|E3|=0
            y0 = x3 = 7 y1 = σi=1..1 𝑏𝑖 + 𝑥3 = 7 y2 = σi=1..2 b𝑖 + 𝑥3 = 8 𝑦3 = σi=1..3 𝑏𝑖 + 𝑥3 = 8
    c1=|G1|=3 c2=|G2|=2 c3=|G3|=2
            z0 = 𝑦3 = 8 z1 = σi=1..1 ci + 𝑦3 = 11 z2 = σi=1..2 ci + 𝑦3 = 13 z3 = σi=1..3 𝑐𝑖 + 𝑦3 = 15
```

### Strana 17

```text
Parallel splitting, Příklad
 L1={1, 3}                          L2={2, 6}                   L3={4, 5, 7}
 E1={}                              E2={8}                      E3={}
 G1={12, 13, 14}                    G2={10, 15}                 G3={9, 11}
      𝒙𝟎 = 𝟎       𝒙𝟏 = 𝟐 𝒙𝟐 = 𝟒            x3 = 7
      𝒚𝟎 = 𝟕       𝒚𝟏 = 𝟕 𝒚𝟐 = 𝟖            𝑦3 = 8
      𝒛𝟎 = 𝟖       𝒛𝟏 = 𝟏𝟏 𝒛𝟐 = 𝟏𝟑          z3 = 15

               1        2       4


               1    3   2   6   4   5


               1    3   2   6   4   5   7    8    12


               1    3   2   6   4   5   7    8    12 13    10         9


               1    3   2   6   4   5   7    8    12 13 14 10 15      9   11
```

### Strana 18

```text
Parallel splitting, Analýza
■ Analýza
   – (i) Krok (i) trvá O(log N)
   – (ii) Rozdělení optimálním sekvenčním algoritmem má složitost O(n/N)
   – (iii) Hodnoty x, y a z se dají spočítat sumou prefixů (ukážeme později) v O(log N)
   – (iv) Následné spojení má složitost O(n/N)


■ Časová složitost je    t(n) = O(log N + n/N) = O(n/N) pro dostatečně malé N
■ Cena je                c(n) = O(n/N).N = O(n)    což je optimální
```

### Strana 19

```text
Nalezení k-tého nejmenšího prvku, sekvenční řešení

      procedure SEQUENTIAL_SELECT(S, k)
      (1) if |S| < Q then sort S and count down
             else divide S into |S|/Q sequences Si of length Q
      (2) // Sort every sequence Si and find its median M[i]
           for i=1 to |S|/Q do
             M[i] = SEQUENTIAL_SELECT(Si, |Si|/2)
           end for
      (3) // Find “median of medians” m
          m = SEQUENTIAL_SELECT(M, |M|/2)
      (4)    L = {𝑠𝑖 𝜖 𝑆: 𝑠𝑖 < 𝑚}
             E = {𝑠𝑖 𝜖 𝑆: 𝑠𝑖 = 𝑚}
             G = {𝑠𝑖 𝜖 𝑆: 𝑠𝑖 > 𝑚}
      (5) if |L| > k then SEQUENTIAL_SELECT(L,k) // element must be in L
          else if |L| + |E| > k then return m    // element must be in E
          else SEQUENTIAL_SELECT(G, k-|L|-|E|)   // element must be in G



■ Pokud k=|S|/2 jedná se o medián
■ t(n)=O(n)
```

### Strana 20

```text
    Nalezení k-tého nejmenšího prvku, paralelní řešení

      procedure PARALLEL SELECT(S, k)
      (1) if |S| < 4 then find imediatly the k-th element
          else divide S into N subsequences Si of length n/N and every
                sequence Si assert to a processor Pi
      (2) for i=1 to N do in parallel
             M[i] = SEQ.SELECT(Si, |Si|/2)
           end for
      (3) m = PARALL.SELECT(M, |M|/2)   with the lowest number
                                                       of processors
      (4) PALALLEL SPLITTING(S, m)
                 L = {𝑠𝑖 𝜖 𝑆: 𝑠𝑖 < 𝑚}
                 E = {𝑠𝑖 𝜖 𝑆: 𝑠𝑖 = 𝑚}
                 G = {𝑠𝑖 𝜖 𝑆: 𝑠𝑖 > 𝑚}
      (5) if |L| > k then PAR.SELECT(L,k)
             else if |L| + |E| > k then return m
                     else PAR.SELECT(G, k-|L|-|E|)

■    Pokud k=|S|/2 jedná se o medián
■    t(n)=O(n)
```

### Strana 21

```text
Příklad
■ Vstup: 13, 1, 12, 14, 3, 6, 8, 10, 2, 15, 7, 11, 4, 5, 9
■ Počet procesorů N=4
■ Rozdělíme na 3 posloupnosti o 5 prvcích a hledáme medián |Si|=15, |Si| / 2 = 7
    13, 1, 12, 14,3          6, 8, 10,2,15            7, 11, 4, 5, 9
       M[1]=12                  M[2]=8                    M[3]=7
    12, 6, 7, 5 -> sekvenčně M=7
Použijeme Parallel Splitting

            1   3   2   6   4   5   7   13 12 14   8   10 15 11 9

   |L|= 6 |M|=1 |G|= 8
              //.pokud bychom hledali 8. prvek, pokračujeme hledáním prvního v G
```

### Strana 22

```text
Časová složitost podrobněji

■ Při volbě pivotů a rozdělení, hledáme v posloupnosti s asi 70% uzlů
                                                               7         7 2
■ Celková práce přes rekurze se dá odhadnout řadou n +              n+       n…
                                                               10        10

        To je geometrická řada s kvocientem 𝛾 = 0.7
                                    𝑛      𝑛      𝑛
        Její součet je σ∞     𝑖
                        𝑖=1 𝑛𝛾 =       =       =     ≈ 0.33𝑛
                                   1−𝛾   1−0.7   0.3

        Tedy třída časové složitosti je je O(𝑛)
```

### Strana 23

```text
ALGORITMY ŘAZENÍ
```

### Strana 24

```text
Paralelní řadící algoritmy
■ Porovnávací algoritmy
   – Odd – Even Transposition Sort
■ Výčtové řadící algoritmy
   – Na mřížce
   – Na lineárním poli
■ Algoritmy slučováním
   – Odd – Even Merge Sort
   – Pipeline Merge Sort
   – Merge – Splitting Sort
■ Algoritmy založené na výběru minima
   – Minimum Extraction Sort
■ Algoritmus rozdělením
   – Bucket Sort
   – Median Finding and Splitting (+ nalezení Mediánu)
```

### Strana 25

```text
Odd – Even Transposition Sort
■ Topologie:
       lineární pole n procesorů p(n) = n
■ Princip:
       na počátku každý procesor pi obsahuje jednu z řazených hodnot yi
       v prvním kroku se každý lichý procesor pi spojí se svým sousedem pi+1 a
       porovnají své hodnoty, platí-li yi >yi+1, procesory vymění své hodnoty
       v druhém kroku se každý sudý procesor ... to samé
       po n krocích (maximálně) jsou hodnoty seřazeny
■ Algoritmus
          Algoritmus:
          for k = 1 to n/2 do
            for i = 1, 3, ..., 2.(n/2)-1 do in parallel
              if yi > yi+1 then yi <-> yi+1 endif
            endfor
            for i = 2, 4, ..., 2.((n-1)/2) do in parallel
              if yi > yi+1 then yi <-> yi+1 endif
            endfor
          endfor
```

### Strana 26

```text
Odd – Even Transposition Sort, příklad

   4     3    1     2      1. krok, liší


   3    4     1     2      1. krok, sudí


   3    1     4     2      2. krok, liší



   1    3     2     4      2. krok, sudí



   1    2     3     4
```

### Strana 27

```text
Odd – Even Transposition Sort, Analýza
• každý z kroků (1) a (2)                7   6   5   4   3   2   1
  provádí jedno porovnání a
                                     1   6   7   4   5   2 3     1
  dva přenosy - konstantní čas
■ Složitost: t(n) = O(n)             2   6   4   7   2   5 1     3
                                     3
■ Cena: c(n) = t(n) . p(n) = O(n)    4
  . n = O(n2) což není optimální     5
■ Algoritmus má časovou              6
                                     7   1
  složitost t(n) = O(n), což je to
  nejlepší, čeho lze při lineární
  topologii dosáhnout.c
```

### Strana 28

```text
Enumeration Sort (Mřížka)
■ Topologie:
      dvojrozměrné pole n x n procesorů, vertikálně i horizontálně propojeny do
      stromové struktury
■ Uzel
        může uložit dva prvky do svých registrů A a B
        může porovnat A a B a uložit výsledek do registru RANK
        pomocí stromového propojení může zadat obsah kteréhokoli registru jinému procesoru
        může přičítat k registru RANK v RANK bude 1, nebo 0
■ Princip:
       správná pozice každého prvku ve výstupní seřazené posloupnosti je dána
       počtem prvků, které jsou menší než tento prvek
```

### Strana 29

```text
Komunikace na stromě (připomenutí)

      [1,1]      [1,2]    [1,3]   [1,4]       [1,5]   [1,6]   [1,7]




                         [1,4]            Pro n uzlů výška stromu log n
              [1,2]
                                          Přenesení hodnoty mezi libovolnými dvěma
                         [1,5]
                                          uzly nanejvýš v 2*(log n - 1) krocích
  [1,1]
                         [1,6]
              [1,3]
                         [1,7]
```

### Strana 30

```text
Enumeration Sort (Mřížka), Algoritmus
1) každý prvek je porovnán se všemi ostatními pomocí jedné řady procesorů
2) správná pozice prvku je RANK(xi) = 1 + počet menších prvků
3) každý prvek je zadán na správné místo
    1) for i=1 to n do in parallel
             1.1) každý procesor P(i, j) v řadě i získá xi a xj
                      (i, j = 1...n) a uloží je do A(i, j) a B(i, j)
                      prvky se roznáší do procesorů
             1.2) if B(i, j) < A(i, j) then RANK(i, j) = 1
                                               else RANK(i, j) = 0
              endif
       endfor
    2) for i = 1 to n do in parallel
             2.1) obsah registrů RANK všech procesorů v řadě i je sečten a
              uložen do RANK(i, 1)
             2.2) P(i, 1) spočte RANK(xi) jako RANK(i,1) += 1
       endfor
    3) for i=1 to n do in parallel
             if RANK(i, 1)=j then xi je přesunuto z A(i, j) do A(j, 1)
             endif
       endfor
```

### Strana 31

```text
Enumeration Sort (Mřížka), 1. fáze
          9
          9   8   3   5   6

          8


          3


          5


          6
```

### Strana 32

```text
Enumeration Sort (Mřížka), 1. fáze
 9   9   9            9   9   9      9   9
 9   8   3   5   6    9   8   3      5   6

 8   8   8            8   8   8      8   8
 9   8   3   5   6    9   8   3      5   6

 3   3   3            3   3   3      3   3
 9   8   3   5   6    9   8   3      5   6

 5   5   5            5   5   5      5   5
                      9   8   3      5   6

 6   6   6            6   6   6      6   6
                      9   8   3      5   6
```

### Strana 33

```text
Enumeration Sort (Mřížka), 2. fáze
                              if B(i, j) < A(i, j)
                               then
9     9     9     9     9        RANK(i, j) = 1
  0     1     1     1     1     else
9     8     3     5     6
                                 RANK(i, j) = 0

8     8     8     8     8      for k = ((log n) - 1) downto 1 do
  0     0     1     1     1     for j = 2k-1 to 2k-1 do in parallel
9     8     3     5     6
                                      RANK(i,j) += RANK(i,2j)+ RANK(i,2j+1)
                                endfor
3     3     3     3     3      endfor
  0     0     0     0     0
9     8     3     5     6

5     5     5     5     5
  0     0     1     0     0
9     8     3     5     6

6     6     6     6     6
  0     0     1     1     0
9     8     3     5     6
```

### Strana 34

```text
Enumeration Sort (Mřížka), 2. fáze
Po sečtení druhé úrovně stromu               Po sečtení první úrovně a kořenu


   9        9         9          9     9         9         9        9           9     9
     0        3         1          1     1         4         3        1           1     1
   9        8         3          5     6         9         8        3           5     6

   8        8         8          8     8         8         8        8           8     8
     0        2         1          1     1         3         2        1           1     1
   9        8         3          5     6         9         8        3           5     6

   3        3         3          3     3         3         3        3           3     3
     0        0         0          0     0         0         0        0           0     0
   9        8         3          5     6         9         8        3           5     6

   5        5         5          5     5         5         5        5           5     5
     0        0         1          0     0         1         0        1           0     0
   9        8         3          5     6         9         8        3           5     6

   6        6         6          6     6         6         6        6           6     6
     0        1         1          1     0         2         1        1           1     0
   9        8         3          5     6         9         8        3           5     6
```

### Strana 35

```text
Enumeration Sort (Mřížka), 3. fáze
V každém řádku se přesune hodnota registru A v prvním sloupci do sloupce stejného řádku daného
Hodnotou registru C. Tedy v prvním řádku se hodnota 9 do 5 . sloupce. Stejně tak i pro ostatní řádky.
(v nejvíce log n – 1 krocích).

  9                                                                                             9
      4                                                     5


  8                                                                                   8
      3                                                     4


  3                                                     3
      0                                                     1


  5                                                               5
      1                                                     2


  6                                                                         6
      2                                                     3
```

### Strana 36

```text
Enumeration Sort (Mřížka), 3. fáze
V každém řádku se přesune hodnoty z aktuálního registru, kam byla hodnota přesunuta, vertikálně
Na pozici diagonály v nejvíce 2*(log n – 1) krocích, následně pak všechny přesune do prvního sloupce.
v nejvíce log n – 1 krocích

  3                                                     3
      5                                                     5


            5                                           5
      4                                                     4


                      6                                 6
      1                                                     1


                               8                        8
      2                                                     2


                                         9              9
      2                                                     3
```

### Strana 37

```text
Enumeration Sort (Mřížka), analýza
■ Analýza
   – t(n) = O(log n)            p(n) = n2
   – c(n) = O(n2. log n)        což není optimální


■ Diskuse
   • Algoritmus je extrémně rychlý O(log n), což znamená zrychlení O(n) krát oproti
       optimálnímu sekvenčnímu algoritmu.
   • Žádný paralelní alg. pro rozumný výpočetní model není rychlejší, bez ohledu na
       počet procesorů
   • Spotřebovává mnoho procesorů - n2 je na hranici přijatelnosti
   • Vstupní posloupnost nesmí obsahovat stejné prvky (navrhněte úpravu)
```

### Strana 38

```text
Enumeration Sort (Lineární)
■ Topologie:
      Lineární propojení n uzlů pro řazení posloupnosti délky n
■ Uzel
        může uložit dva prvky do svých registrů X a Y, RANK (označíme C) a výstupní registr Z
        může porovnat A a B a uložit výsledek do registru RANK
■ Princip:
       Hodnoty vstupují do registru X postupně po sběrnici
       Hodnoty se přesouvají po registrech Y přes lineární propojení
       Hodnoty jsou umisťovány do registru Zci po sběrnici
       Každý uzel porovnává hodnoty X a Y, pokud jsou k dispozici, a případně
       inkrementuje C
       Pokud již byl porovnán každý pár, hodnota z Xi je přesunuta do příslušného Zci
```

### Strana 39

```text
  Enumeration Sort (Lineární), Algoritmus
                                                                             Sběrnice


                         IN       C           C          C             C                OUT
                                  X           X          X             X
                                  Y           Y          Y             Y
                                  Z           Z          Z             Z


                                                                Lineární spojení

Algoritmus:
     1) všechny registry C se nastaví na hodnotu 1
     2) následující činnosti se opakují 2n krát 1 <= k <= 2n
           pokud vstup není vyčerpán, vstupní prvek xi se vloží do Xi (sběrnicí) a do Y1 (lineárním spojením) a
           obsah všech registrů Y se posune doprava
           každý procesor s neprázdnými registry X a Y je porovná, a je-li X > Y inkrementuje C
           je-li k > n (t.j. po vyčerpání vstupu) procesor Pk-n pošle sběrnicí obsah svého registru X procesoru PCk-n,
           který jej uloží do svého registru Z
     3) v následujících n cyklech procesory posouvají obsah svých registrů doprava a procesor Pn produkuje
     seřazenou posloupnost
```

### Strana 40

```text
      1   1   1   1   3   2
897               7   9   8
                  8   8   8
                  7       9



      1   1   1   1   3   2
 89   7           7   9   8
      7           8   8   9
                  7   8   9




      1   1   1   1   3   2
  8   7   9       7   9   8   9
      9   7       8   8   8
                  7   7   8



      1   2   1   1   3   2
      7   9   8   7   9   8   8 9
      8   9   7   8   8   8
                  7   7   7



      1   2   2   1   3   2
      7   9   8   7   9   8   7 8 9
      8   8   9   8   8   8
      7           7   7   7
```

### Strana 41

```text
Enumeration Sort (Lineární), Analýza
■   Analýza
     – Bod 1) je v konstantním čase
     – bod 2) trvá 2n cyklů,
     – bod 3) trvá n cyklů
     –         t(n) = O(n)
     –         c(n) = t(n).p(n) = O(n).n = O(n2), což není optimální
■   Poznámky
     – .výpočet složitosti platí pouze za předpokladu, že přenos hodnoty
       sběrnicí trvá konstantní dobu bez ohledu na fyzickou vzdálenost
       procesorů
     – .algoritmus není schopen řadit vstup obsahující stejné hodnoty
       (Navrhněte modifikaci)
```

### Strana 42

```text
Minimum Extraction sort
■ Topologie
         Stromová topologie
■ Uzly
         Listové uzly obsahují řázenou posloupnost, do nelistových je vybírána hodnota z
         potomkovských (umí porovnávat tyto hodnoty), kořenový uzel posílá hodnoty na
         výstup
■ Princip
         každý nelistový procesor porovná hodnoty svých dvou synů a menší z nich pošle svému
         otci po (log n) + 1 krocích se minimální prvek dostane do kořenového procesoru
         každým dalším krokem se získá další nejmenší prvek
```

### Strana 43

```text
Minimum Extraction sort, Algoritmus

   1) for all leafs do in parallel
            processor reads one element
       end for
   2) for i=1 to 2n+(log n)-1 do
         for all nonleafs do in parallel
           if root and nonempty       then output number
           else if nonempty then nothing
                else {i.e. empty nonleaf}                          Zde je třeba
                  if children empty then nothing                   pozorně synchronizovat
                  else
                     if one child empty then get number from child
                     else {no child empty}
                               get smaller number from childs
                     endif
                  endif
                endif
           endif
         endfor
      endfor
```

### Strana 44

```text
Minimum Extraction sort, Příklad


                                                    7           5           3       1


8       7       6   5   4       3       2   1   8           6           4       2



                                                                    1


            5                       1                   5                                       5                   2

    7                       3                       7           6           3       2       7           6       3

8               6       4               2       8                       4               8                   4

                                                                                                    1
```

### Strana 45

```text
Minimum Extraction sort, Analýza

■ Jelikož strom má (log n)+1 úrovní, první prvek se získá po (log n)+1 krocích.
  Kořenový procesor potřebuje jeden krok na porovnání a jeden na uložení výsledku
  do paměti. Každý ze zbylých n-1 prvků spotřebuje 2 kroky.
   – t(n) = 2.n + (log n) - 1 = O(n)
   – p(n) = 2.n - 1
   – c(n) = t(n).p(n) = O(n2) což není optimální
```

### Strana 46

```text
Bucket Sort
•   Topologie
           řazení stromem procesorů s m listovými procesory n = 2m (tedy m=log n)
           strom obsahuje 2m - 1 procesorů, takže p(n) = (2. log n) - 1
•   Uzly
           každý listový procesor obsahuje n/m řazených prvků a umí je seřadit
           optimálním sekvenčním algoritmem
•   Princip
           každý nelistový procesor umí spojit dvě seřazené posloupnosti optimálním
           sekvenčním algoritmem
```

### Strana 47

```text
Bucket Sort, Algoritmus
  Řazené prvky se rovnoměrně rozdělí mezi listové procesory
  Každý list seřadí svou posloupnost
     for j = 1 to log m do
               for all processors at level (log m)-j do in parallel
                       procesor spojí posloupnosti svých synů
               endfor
              endfor
  Kořenový procesor uloží výslednou posloupnost do paměti
```

### Strana 48

```text
Bucket Sort, příklad

                                                    2 4 5 10 12 13 14 15   1 3 6 7 8 9 11 16



 5 2 10 14    13 4 15 12    1 8 11 9    6 16 7 3



                                                       1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16




  2 5 10 14    4 12 13 15    1 8 9 11    3 6 7 16
```

### Strana 49

```text
Bucket Sort, Analýza
1.Každý listový procesor čte 𝑛Τlog 𝑛 prvků, takže složitost je 𝑂(𝑛Τlog 𝑛)
2.Při použití optimálního algoritmu
                  𝑂(𝑟 ∗ log 𝑟) = 𝑂((𝑛Τlog 𝑛) ∗ log( 𝑛Τlog 𝑛)) = 𝑂(𝑛)
3.Při j-té iteraci každý procesor na úrovni i = (log m) - j spojí dvě
posloupnosti o délce 2𝑛𝑖 . Při použití merge každá j-tá iterace zabere 𝑘𝑛
                                                                       2𝑖
kroků, kde k je konstantní. Krok 3 tedy trvá
                      𝑘𝑛
         σ(log
          𝑖=1
               𝑚)−1
                         = 𝑂(𝑛)
                      2𝑖


4.Třída výpisu výsledné posloupnosti na výstup je je O(n)
Celkově tedy
        t(n) = O(n)               p(n) = O(log n)
        c(n) = O(n.log n)                  což je optimální
```

### Strana 50

```text
Odd – Even Merge Sort
■ Algoritmus založený na slučování
■ Topologie
   – Speciální topologie pro slučování. Jednotka CE uspořádá dvě hodnoty na
      vstupech na výstup
   – Spojováním jednotek do bloků dokáže uspořádat dvě uspořádané vstupní
      posloupnosti v jednu
         Síť 1x1                           Síť 2x2

                                     a1        L d1                 c1
                                     a2        H d2
    a           L     min(a, b)
                                                             L
    b      CE         max(a, b)
                                                                    c2
                H                                  l1        H      c3
                                     b1        L
                                     b2            l2
                                               H                    c4
```

### Strana 51

```text
    Odd – Even Merge Sort, obecné bloky
■ K sestavení obecného bloku n x n potřebujeme
   – Dva bloky n/2 x n/2
   – N-1 CE bloků
■ Liché prvky {a1, a3, ..}{b1, b3, ...} jsou spojeny sítí n/2 x n/2 do sekvence
  {d1, d2, d3, ...} a podobně sudé prvky do sekvence {e1, e2,...}

                                  a1                    d1                        c1
Finální sekvence {c1, c2, ...}    a2                    d2
       c1 = d1                    a3
                                  a4                    d3                        c2
       …
       c2j = min (dj+1, ej)                                                       c3
                                  ai-1
       c2ij1 = max (dj+1, ej)
                                  ai
       …                          b1                                              c4
                                                        e1
       c2n = en                   b2
                                                                                  c5
                                 bi-1                   e2
                                  bi
```

### Strana 52

```text
Odd – Even Merge Sort,
                   ověření funkčnosti
a1
a2       Prvek di je i tý prvek z n prvků ve výsledné posloupnosti první
a3       řadičky. Tedy existuje
a4       i-1 menších lichých prvků v celkové posloupnosti a n-i větších
      d3 lichých prvků v posloupnosti. Jelikož každý lichý prvek má sudého
a5
a6
         ‚sourozence‘, který v této řadičce nebyl obsloužen, je 2*(i-1)
         menších prvků celkem a 2*(n-i) větších prvků celkem a tedy prvek
a7
         di musí být buď na pozici 2*(i-1) nebo 2*(i-1)+1
a8

b1
          d3 může být
b2
          a1 s d1=b1 a d2=b3
b3        pak jej předchází b1,b2,b3 a možná i b4 (4. nebo 5.)
b4        a3 s předchůdci a1 a b1
b5        pak jej předchází a1,a2,b1 a možná i b2 (4. nebo 5.)
A6        a5 s d1=a1 a d2=a3
a7        pak jej předchází a1,a2,a3 a a4 (4.)
a8
          … obdobně může být i b1, b3 a b5
```

### Strana 53

```text
Odd – Even Merge Sort, struktura
■   Řadíme po fázích
         dvojice vstupů v uspořádanou posloupnost délky 2 (CE)
         dvojice uspořádaných dvojic v uspořádanou čtveřici (Síť 2x2)
         … dvojice uspořádaných 2𝑛−1 -tic na uspořádanou 2𝑛 tici

             CE
                        2x2
             CE
                                     4x4
             CE
                        2x2
             CE
                                                     8x8
             CE
                        2x2
             CE
                                     4x4
             CE
                        2x2
             CE
```

### Strana 54

```text
Odd – Even Merge Sort, analýza
■ Počet CE jednotek roste v řadě 1, 3, 9, 25 …
■ Obecně ni=2*(ni-1)+2(i-2)-1 ( resp p(2n) = 2p(n)+(n-1) = 1+n*log n )
    n1=1, n2=2+1=3, n3=2*3+3=9, n4=2*9+7=25, n5=2*25+15=65
■ Řadíme posloupnost o délce n=2m
   – 1.fáze potřebuje 2m-1 CE
   – 2.fáze potřebuje 2m-2 sítí 2x2 po 3 procesorech                 1+16*log216
   – 3.fáze 2m-3 sítí 4x4 po 9 procesorech
   – 4.fáze 2m-4 sítí po 25 procesorech
   –          atd.
   – Suma je O(n* log2n)                  // fází je log n
■ Časová složitost (počet kroků v jednotlivých fázích ke řada 1,2,3 … log n)
   –            t(n) = O(m2) = O(log2n)     // součet řady
■ Cena
   –              c(n) = O(n*log4 n)         // což není optimální
```

### Strana 55

```text
Pipeline Merge Sort
■ Topologie
       Lineárně propojené uzly
■ Funkčnost uzlů
       Má dvě vstupní fronty a jednu výstupní. Spojí dvě seřazené posloupnosti délky n v
       jednu seřazenou posloupnost délky 2n
■ Princip
       Postupně slučuje seřazené posloupnosti délky 2𝑖 do seřazené posloupnosti délky
       2𝑖+1 pro i= 0 … log 𝑛 kde n je délka vstupní posloupnosti
                                      1            2               4
                  8                                                                   8
                          P1              P2           P3              P4

                                                                                   r = log n = 3
                                     Spojuje posloupnost délky
                                     jedna do posloup. délky dvě

                               Označení front :
                          q 2(i-1)                                          q 2i
                                                  Pi
                      q 2(i-1)+1                                            q 2i+1
```

### Strana 56

```text
                     . .         . . .        . . . .                                             . .        . 2 3        4 6 7 8
1 5 3 2 8 7 4 6 P1          P2           P3             P4 . . . . . . . .   . . . . . . . . P1         P2           P3             P4 . . . . . . . .
                     . .         . . .        . . . .                                             . .        . . 1        . . . 5
                     . .6        . . .        . . . .                                             . .        . . 2        . 4 6 7
. 1 5 3 2 8 7 4 P1          P2           P3             P4 . . . . . . . .   . . . . . . . . P1         P2           P3             P4 8 . . . . . . .
                     . .         . . .        . . . .                                             . .        . . 1        . . 3 5
                     . .6        . . .        . . . .                                             . .        . . .        . . 4 6
. . 1 5 3 2 8 7 P1          P2           P3             P4 . . . . . . . .   . . . . . . . . P1         P2           P3             P4 7 8 . . . . . .
                     . 4         . . .        . . . .                                             . .        . . 1        . 2 3 5
                     . 7         . . 6        . . . .                                             . .        . . .        . . . 4
. . . 1 5 3 2 8 P1          P2           P3             P4 . . . . . . . .   . . . . . . . . P1         P2           P3             P4 6 7 8 . . . . .
                     . 4         . . .        . . . .                                             . .        . . .        1 2 3 5
                     . 7         . 4 6        . . . .                                             . .        . . .        . . . 4
. . . . 1 5 3 2 P1          P2           P3             P4 . . . . . . . .   . . . . . . . . P1         P2           P3             P4 5 6 7 8 . . . .
                     . 8         . . .        . . . .                                             . .        . . .        . 1 2 3
                     2 7         . 4 6        . . . .                                             . .        . . .        . . . .
. . . . . 1 5 3 P1          P2           P3             P4 . . . . . . . .   . . . . . . . . P1         P2           P3             P4 4 5 6 7 8 . . .
                     . .         . . 8        . . . .                                             . .        . . .        . 1 2 3
                     . 2         . 4 6        . . . 8                                             . .        . . .        . . . .
. . . . . . 1 5 P1          P2           P3             P4 . . . . . . . .   . . . . . . . . P1         P2           P3             P4 3 4 5 6 7 8 . .
                     . 3         . . 7        . . . .                                             . .        . . .        . . 1 2
                     5 2         3 4 6        . . 7 8                                             . .        . . .        . . . .
. . . . . . . 1 P1          P2           P3             P4 . . . . . . . .   . . . . . . . . P1         P2           P3             P4 2 3 4 5 6 7 8 .
                     . .         . . .        . . . .                                             . .        . . .        . . . 1
                     . 5         2 3 4        . 6 7 8                                             . .        . . .        . . . .
. . . . . . . . P1          P2           P3             P4 . . . . . . . .   . . . . . . . . P1         P2           P3             P4 1 2 3 4 5 6 7 8
                     . 1         . . .        . . . .                                             . .        . . .        . . . .
                     . .         . 2 3        4 6 7 8                                             . .        . 2 3        4 6 7 8
. . . . . . . . P1          P2           P3             P4 . . . . . . . .   . . . . . . . . P1         P2           P3             P4 . . . . . . . .
                     . 1         . . 5        . . . .                                             . 1        . . 5        . . . .
```

### Strana 57

```text
Pipeline Merge Sort, Analýza
■ Procesor Pi začne, když má na jednom vstupu posloupnost délky 2i-2 a na druhém 1,
  tedy začne 2i-2+1 cyklů po procesoru Pi-1.
■ Pi tedy začne v cyklu
        1 + σ𝑖−2  𝑗
             𝑗=0(2 +1) = 2
                          𝑖−1
                              + 𝑖 − 1 (tj. v 3., 6., 11. …)
    a skončí v cyklu
         𝑛 − 1 + 2𝑖−1 + 𝑖 − 1
■ Algoritmus skončí za:
   – n + 2r + r - 1 = 2n + log n - 1 cyklů, t(n) = O(n)       // r je log n
   – c(n) = t(n).p(n) = O(n).(log n + 1) = O(n.log n)         což je optimální
```

### Strana 58

```text
Median Finding and Splitting

• stejná architektura jako Bucket Sort
  - strom procesorů s m listy, n = 2m , m=log n
  - procesor na úrovni i zpracovává n/2i prvků
  - každý list umí optimální sekvenční sort
• nový požadavek
  každý nelistový procesor umí nalézt medián v optimálním čase
  (např. algoritmus Select s O(n) složitostí)
```

### Strana 59

```text
Median Finding and Splitting,
Algoritmus
   1.Kořen načte řazenou sekvenci S
   2.for i=0 to (log m) - 1 do
          for all processors at level i do in parallel
          2.1) Nalezni ve své sekvenci medián M (sekvenčně)
          2.2) Pro každý prvek x této sekvence
                 if x < M then pošli x levému synovi
                        else pošli x pravému synovi
                 endif
          endfor
   endor
   3.for all leaf processors do
          3.1) seřaď svou sekvenci sekvenčním algoritmem
          3.2) ulož ji do výstupní vyrovnávací paměti
   endfor
```

### Strana 60

```text
Median Finding and Splitting, Příklad
    1.                                    2.
            2 5 7 1 8 4 6 3                               M=4



                                                2 1 4 3               5 7 8 6




    3.                                    4.



          M=2                 M=6


    2 1         4 3   5 6           7 8   1 2       3 4         5 6        7 8
```

### Strana 61

```text
Median Finding and Splitting, Analýza
1.První krok má složitost O(n)
2.Procesor na i-té úrovni hledá medián v posloupnosti délky n/2i , což mu při
optimálním algoritmu trvá O(n/2i). Rozdělení posloupnosti trvá rovněž O(n/2i),
tedy celkem krok 2:
                           𝑛
                σ(log
                 𝑖=1
                      𝑚)−1
                           𝑖 = 𝑂(𝑛)
                           2

3.každý procesor řadí posloupnost délky n/log n což mu trvá
    𝑛                                                𝑛
𝑂(     ∗ log( 𝑛Τ( log 𝑛))) a výstup uloží v čase 𝑂(     ), takže složitost kroku 3 je
  𝑙𝑜𝑔𝑛                                             𝑙𝑜𝑔𝑛
O(n)

       t(n) = O(n)               p(n) = O(log n)
       c(n) = O(n.log n)            což je optimální
```
