# PRAM

Oficialni slidy extrahovane z PDF. Text je automaticky vytazeny pres `pdftotext -layout`; u obrazkovych nebo diagramovych stran kontroluj originalni PDF.

## Metadata

| Pole | Hodnota |
|---|---|
| Zdroj | [[raw/PDA06_PRAM_MNG.pdf]] |
| Soubor | `PDA06_PRAM_MNG.pdf` |
| Stran | 106 |
| Page size | 595.276 x 841.89 pts (A4) |

## Pouziti

- Pouzivej jako oficialni oporu pro definice, algoritmy, terminologii a slozitosti.
- Pokud je strana zalozena hlavne na obrazku, cituj stranu a zkontroluj originalni PDF.
- Pro exam historii porad preferuj `knowledge/exams/**/term-*.md`; slidy slouzi jako vykladovy zdroj.

## Text po stranach

### Strana 1

```text
                  PRL06 - MNG
                    Model 2019




                      Paralelní
              a distribuované
                      algoritmy
Část 6             PRAM, Suma prefixů



 Post 19/20
                   Souhrnné materiály

  Petr Hanáček
                                 Ver 0.1
                                  PDA0x0 Slide 5
```

### Strana 2

```text
Paralelní a distribuované algoritmy
                                        Paralelní a distribuované algoritmy
                                                                                  Upd 2005, Upd 2007
                                                                                  Upd 2008/9, Post 2009/10
                                                                                  Post 2010/11
                                                                                  Post 19 MNGprep
                                                                                  Koro version



                                  PDA 6
                            PRAM, Suma prefixů
                                                                      .




                PRL                                                                                  1




                                                                                                         6
                                                         Učebnice
            •     [Reif] Reif, J: Synthesis of Parallel Algorithms, Morgan
                  Kaufmann, 1993, ISBN:155860135X
            •     Kapitoly:
                      – 20 The Complexity of Computation on the Parallel Random Access Machine
                          » Zajímavé jsou pro nás strany 2-6
                      – 1 Prefix Sums and Their Applications
                          » Zajímavé jsou pro nás strany 2-13, 17-20, 23-24




                PRL                                                                                  2




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je                          1
                      zakázáno.
```

### Strana 3

```text
Paralelní a distribuované algoritmy
                                                   Model
                  Model je rozhraní,
                  které odděluje
                  aplikaci (high-level)
                                                                  Aplikace
                  od architektury (low
                  level)
                                                                               Poskytuje
                                                                               operace


                                                                         MODEL


                                                                Požaduje
                                                                implementaci

                                                                   Architektura
                PRL                                                                         3




                                                   PRAM
            •     Parallel Random Access Machine
                       Synchronní model paralelního výpočtu,
                        procesory komunikují sdílenou pamětí
                                                                             MOV 1,4
                       Skládá se z p procesorů RAM
                                                                             ADD 3,2
                                                                             CMPJ 1, 4, 8
                 Procesor
                         Aditivní (logické) operace                         PROCESOR
                         [Multiplikativní operace]
                         Podmíněné skoky na základě porovnání
                         [Adresování]
                                                                     1
                 Paměť (sada registrů)                                    REGISTRY
                       Neomezený počet                              n
                       [Neomezená délka slova] - není příliš                   RAM
                        vhodná, už se nepoužívá


                PRL                                                                         4




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je             2
                      zakázáno.
```

### Strana 4

```text
Paralelní a distribuované algoritmy
                                                      PRAM
                 Je to alternativní model k paralelnímu Turingovu
                  stroji
            •     Všechny RAMy jsou řízeny jedním společným
                  programem
                                     Společné
                                     řízení




                          LM1      RAM1         LM2    RAM2              LMn      RAMn




                                                      Společná
                                                      paměť
                PRL                                                                               5




            •     Definice
                      – PRAM je synchronní model paralelního výpočtu, ve kterém procesory
                        komunikují sdílenou pamětí. Skládá se z p procesorů P1...Pn, jež jsou
                        RAM.
                      – Výpočet probíhá po krocích synchronně. Krok:
                           čtení sdílené paměti
                           lokální operace
                           zápis do sdílené paměti
                      – Procesory mohou během kroku provádět různé operace a mohou
                        používat svůj index (unikátní číslo procesoru).
            •     Teorém
                      – Každý problém, řešitelné PRAMem s p procesory v t krocích je také
                        řešitelné p’p procesory v O(t p/p’) krocích.
            •     Důkaz
                      – Původních p procesorů je rozděleno do p’ skupin o velikosti max p/p’.
                        Každý z p’ procesorů simulujícího stroje se stará o jednu skupinu. Pro
                        simulaci jednoho kroku původního stroje každý z p’ procesorů simuluje
                        čtecí fázi procesorů své skupiny, pak lokální fázi a na konec zápisovou
                        fázi.
                PRL                                                                               6




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je                   3
                      zakázáno.
```

### Strana 5

```text
Paralelní a distribuované algoritmy
                       Omezení přístupu ke sdílené paměti
                 Je dovoleno současné čtení ?
                 Je dovoleno současné zapisování ?
            •     Čtyři různé architektury přístupu k paměti
                          »   EREW - exclusive read, exclusive write
                          »   ERCW - exclusive read, concurrent write - nemá opodstatnění, nepoužívá se
                          »   CREW - concurrent read, exclusive write
                          »   CRCW - concurrent read, concurrent write - splňují pouze některé architektury, technicky
                              obtížněji realizovatelný

            •     U architektury CRCW je třeba specifikovat řešení
                  zápisových konfliktů:
                           COMMON - všechny zapisované hodnoty musí být shodné
                           ARBITRARY - zapisované hodnoty mohou být různé, zapíše se libovolná z nich
                           PRIORITY - procesory mají pevné priority, zapíše se hodnota, zapisovaná procesorem s
                            nejvyšší prioritou
                      – Relace A  B - algoritmus, který běží na architektuře B, běží beze změn i
                        na A. ( A je stejně tolerantní nebo tolerantnější k zápisovým konfliktům)
            •     Pak platí:
                      – PRIORITY  ARBITRARY  COMMON  CREW PRAM  EREW PRAM

                PRL                                                                                                  7




                                        DALŠÍ ALGORITMY




                PRL                                                                                                  8




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je                                      4
                      zakázáno.
```

### Strana 6

```text
Paralelní a distribuované algoritmy
                                              Broadcast
                   Hodnota, uložená v paměti, má být rozšířena mezi N
                    procesory
                       pro CREW a CRCW PRAM je triviální řešení v konstantním čase
                       pro EREW je třeba simulovat současné čtení
            •       Funkce
                      – P1 přečte D a zpřístupní jej P2.
                      – P1 a P2 jej zpřístupní paralelně P3 a P4.
                      – P1, P2, P3 a P4 jej zpřístupní paralelně P5, P6, P7 a P8..
                      – …
            Algoritmus
            D - hodnota, která se má rozšířit mezi N procesory
            A[1..N] - pole ve sdílené paměti o délce N
            procedure BROADCAST(D, N, A)
            (1) A[1] = D;
            (2) for i = 0 to (log N-1) do
                   for j = 2i+1 to 2i+2-1 do in parallel
                           A[j] = A[j-2i]
                   endfor
               endfor
                PRL                                                                            9




                x                       x          L                     L                 L
                              L
                              x                    x                     x                 x
                x     P1               x    P2                                  x    P5
                                                   x                     x                 x
                                                            x    P3      x                 x
                                                                                x    P6
                                                                         x                 x
                                                            x    P4
                                                                                           x
                                                                                x    P7
                                                                                           x
                                                                                           x
                                                                                x    P8
                                                                                           x


                      (a)                   (b)                 (c)                  (d)


            Analýza
                      SEQ                              t(n) = O(n)
                      EREW                             t(n) = O(log n)
                      CREW, CRCW                       t(n) = O(c)
                PRL                                                                        10




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je                5
                      zakázáno.
```

### Strana 7

```text
Paralelní a distribuované algoritmy
                                           Suma prefixů
                 All-prefix-sums, allsums, scan
                 Jeden ze základních kamenů stavby paralelních
                  algoritmů
            •     Definice
                      – Suma prefixů je operace, jejímž vstupem je binární asociativní operátor
                          a uspořádaná posloupnost prvků
                         [a0, a1, ..., an-1]
                      a která vrací posloupnost
                         [a0, (a0  a1), ..., (a0  a1  ...  an-1)]


            •     Např. jestliže je operátor  sčítání a vstupní posloupnost
                        [3 1 7 0 4 1 6 3]
            •     pak výsledek sumy prefixů je
                        [3 4 11 11 15 16 22 25].

                PRL                                                                               11




                                            Suma prefixů
            •     Některá použití:
                       Vyhodnocování polynomů
                       Sčítání binárních čísel v hardware
                       Lexikální porovnávání řetězců
                       Lexikální analýza
                       Implementace radix-sortu, quick-sortu
                       Rušení označených prvků v poli
                       Vyhledávání regulárních výrazů (grep)
                       Implementace některých stromových operací
                       Označování komponent ve dvourozměrných obrázcích
                 Některé jiné názvy
                       V knihovně MPI: MPI_scan
                       V programu MATLAB: y=cumsum(x)

                PRL                                                                               12




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je                    6
                      zakázáno.
```

### Strana 8

```text
Paralelní a distribuované algoritmy
                 Lze použít jakýkoli asociativní operátor +

                                   Asociativita:
                                   (a +b)+c = a+ (b +c)


                 Sum (+)                                    Konkatenace

                Product (*)                                 Vstup: Řetězce
                                      AND “”
                   Max                 OR “”
                   Min                                      MatMul
                                         XOR
                Vstup: čísla                                Vstup: Matice
                                     Vstup: Bity
                                     (Boolean)
            PRL                                                                   13




                                  Sekvenční řešení
            Sekvenční algoritmus
            procedure allsums (Out, In)
            i=0
            sum = In[0]
            while i<length do
                   i = i+1
                   sum = sum + In[i]
                   Out[i] = sum
            endwhile


            •    Časová složitost je t(n) = O(n)




            PRL                                                                   14




Petr Hanáček     Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je        7
                  zakázáno.
```

### Strana 9

```text
Paralelní a distribuované algoritmy
                               Scan, prescan, reduce
            •   Definice                                Inclusive scan
                  – Operace scan je suma prefixů
            •   Definice                                Exclusive scan
                  – Operace prescan má jako vstup binární asociativní operátor ,
                    neutrální prvek I a vektor
                    [a0, ..., an-1] a vrací vektor
                    [I, a0, (a0  a1), ..., (a0  a1  ...  an-2)]
            •   Definice
                  – Operace reduce má stejný vstup jak scan a vrací hodnotu a0  a1
                     ...  an-1

                                          SCAN, ALLSUMS
                I, a0, a0 + a1, ........, a0 + a1 + ... + an-2, a0 + a1 + ... + an-1
                                 PRESCAN                           REDUCE
            PRL                                                                        15




                      Paralelní suma prefixů - Reduce
               Reduce
                   Reduce může být spočtena pomocí stromu procesorů, za
                    předpokladu, že  je asociativní (nemusí být komutativní)


            Algoritmus
            for j = 0 to log n - 1 do
              for i = 0 to n - 1 step 2j+1 do in parallel
                a[i+2j+1-1] = a[i + 2j -1] + a[i + 2j+1 - 1]
              end for
            end for




            PRL                                                                        16




Petr Hanáček     Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je             8
                  zakázáno.
```

### Strana 10

```text
Paralelní a distribuované algoritmy




                PRL                                                                     17




                                               Reduce
            •     Diskuse
                      – strom má výšku log n, pro každý pár prvků je nutný 1 procesor
                      – t(n) = O(log n)                  c(n) = O(n.log n)
                      – p(n) = n/2                             což není optimální
            •     máme-li méně procesorů N<n, každý procesor
                  provede sekvenční reduce pro svůj kousek
                  posloupnosti o délce n/N a výsledky se zpracují
                  pomocí reduce




            PRL                                                                         18




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je          9
                      zakázáno.
```

### Strana 11

```text
Paralelní a distribuované algoritmy
                                             +-reduce pro n > p
            •     Algoritmus
                            for each processor i do in parallel
                                  sum[i] = a[(n/N).i]
                                  for j = 1 to n/N do
                                           sum[i] = sum[i] + a[(n/N).i + j]
                            result = +-reduce(sum)

            •




                  Pak
                      – t(n) = n/N + log N = O(n/N + log N)
                      – je-li log N < n/N, pak
                            t(n) = O(n/N) a
                            c(n) = O(n/N).N = O(n)          což je optimální

                PRL                                                                                             19




                                              Prescan a scan
                 Uvedeme prescan, scan se získá posunem doleva, přidáním reduce
            •     Algoritmus
                   – (i) UpSweep algoritmus totožný s reduce, ale každý uzel si pamatuje
                      mezisoučet
                   – (ii) DownSweep
                          » kořenu se přiřadí neutrální prvek I
                          » nyní se provádí log n kroků (každá úroveň jednou), počínaje kořenem, směrem k listům a
                            v každém kroku procesory v té úrovni pracují paralelně:
                          » uzel dá svému P synovi svoji hodnotu  hodnotu L-syna a L-synovi dá svoji hodnotu




                                                           +prescan
                                                           na stromu



                                                                                4     11



                PRL                                                                                             20




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je                                  10
                      zakázáno.
```

### Strana 12

```text
Paralelní a distribuované algoritmy
                          +-prescan na architektuře PRAM
            Procedure down-sweep (a)
            a[n-1] = 0
            for d = (log n) - 1 downto 0 do
              for i = 0 to n-1 step 2d+1 do in parallel
                t = a[i + 2d - 1]
                a[i + 2d - 1] = a[i + 2d+1 - 1]       //left child = parent
                a[i + 2d+1 - 1] = t + a[i + 2d+1 - 1]//right child = parent+right
              end for
            end for




                PRL                                                                              21




            •     Teorém: po dokončení downsweep obsahuje každý uzel
                  sumu hodnot všech listů, jež ho předcházejí
            •     Důkaz indukcí:
                       kořen nepředcházejí žádné listy, takže jeho správná hodnota je neutrální
                        prvek
                       L-syn je předcházen týmiž uzly, jako samotný uzel (A), za předpokladu,
                        že otec má správnou hodnotu, stačí ji předat L-synovi

                                                                            0



                 pravý syn je předcházen                                                   V
                  listy A, B, proto jeho hodnota
                  je hodnota otce  hodnota                                          L[V]       R[V]
                  levého syna
                                                                  A              B
                PRL                                                                              22




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je                    11
                      zakázáno.
```

### Strana 13

```text
Paralelní a distribuované algoritmy

            •     Analýza
            •     Složitost je stejná, jako u reduce
            •     Zlepšení ceny:
                      – t(n) = O(n/N)
                      – c(n) = O(n), za předpokladu, že log N < n/N        což je
                        optimální




            PRL                                                                       23




                                 Suma prefixů na mřížce
            •     Zpracuje n prvků v √n krocích




                PRL                                                                   24




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je        12
                      zakázáno.
```

### Strana 14

```text
Paralelní a distribuované algoritmy
                              Suma prefixů na hyperkostce
            •     Zpracuje n prvků v log n krocích




                PRL                                                                   25




                                       Suma prefixů na AVX




                PRL                                                                   26
                      Credits: https://www.wikiwand.com/en/Prefix_sum




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je        13
                      zakázáno.
```

### Strana 15

```text
Paralelní a distribuované algoritmy
                                        Packing problem
            •     Máme k vstupních položek, rozmístěných v poli o n
                  pozicích, k<n
            •     Cílem je vytvořit výstupní
                  pole, kde položky zaujímají
                  prvních k pozic
            •     Algoritmus
                      – Spočteme pole binárních příznaků, 1-položka existuje, 0-neexistuje
                      – Spočteme +-scan tohoto pole
                      – Přesuneme položky na správné pozice




                PRL                                                                          27




                                  Packing problem – AVX
            •     Instrukce
            •     VCOMPRESSPS ymm1/m256{k1}{z}, ymm2




                PRL                                                                          28




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je               14
                      zakázáno.
```

### Strana 16

```text
Paralelní a distribuované algoritmy
                                        Viditelnost
            •   Problém
                  – Je dána matice terénu ve formě matice nadmořských výšek a
                    pozorovací bod X(místo pozorovatele), zjistěte, které body podél
                    paprsku vycházejícího z místa X jsou viditelné
            •   Řešení
                  – Bod je viditelný, pokud žádný bod mezi pozorovatelem a jím
                    nemá větší vertikální úhel.
                  – (i) vytvoří se vektor výšek bodů podél pozorovacího paprsku
                  – (ii) vektor výšek se přepočítá na vektor úhlů
                  – (iii) pomocí max_prescan se spočte vektor maximálních úhlů
                    pro zjištění viditelnosti bodu stačí určit jeho úhel a porovnat s
                    maximem.
            •   Analýza
                  – t(n) = O(n/N + log N) na EREW PRAM

            PRL                                                                         29




            procedure LINE_OF_SIGHT
            for each index i do in parallel
                   angle[i] = arctan ((alt[i] - alt[0])/i)
            max_prev_angle = max_prescan(angle)
            for each index i do in parallel
                   if (angle[i] > max_prev_angle[i]) then result[i] = visible
                           else result[i] = unvisible endif
            endfor
             PRL                                                             30




Petr Hanáček     Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je              15
                  zakázáno.
```

### Strana 17

```text
Paralelní a distribuované algoritmy
                 Carry Look Ahead Parallel Binary Adder
            •     Vstup: Dvě n-bitová binární čísla X = xn-1..x0 a
                  Y = yn-1..y0
            •     Cíl: Spočítat Z = zn-1..z0 = X + Y pomocí log n kroků
            •     Musíme předvypočítat všechny bity přenosu cn-1..c0
                  abychom mohli přímo spočítat zi = xi + yi + ci I=0..n-1
                                                                             x0 y0 c0/cin
                       xn-1   yn-1                            x1   y1
                                            ci-1




                                                   ...
                                                                                c1
                                                         c2
            Cout/cn
                                     si-1                               s1            s0
                PRL                                                                         31




                 Carry Look Ahead Parallel Binary Adder
            •     Algoritmus:
                      – Spočteme pole D = dn-1…d0 kde di {propagate, stop, generate}
                      – for i=0 to n-1 do in parallel
                         if (xi=1) and (yi=1) then di = g
                         else if (xi=0) and (yi=0) then di = s
                         else di = p
                        endfor
                      – Spočteme -scan pole D a tím dostaneme všechny bity přenosu
                        v logaritmickém čase




                PRL                                                                         32




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je              16
                      zakázáno.
```

### Strana 18

```text
Paralelní a distribuované algoritmy
                             Funkce  (někdy značená ¢)
            •     p = p’ and p’’
            •     g = g’’ or (g’ and p’’)
            •     Přenos je generován pokud:
                      – Levý blok generuje
                      – Pravý blok generuje a levý propaguje




                PRL                                                                    33




                                          Radix sort
            •     Bitový radix sort (radix = 2)
                      – V každém kroku se bere v úvahu 1 bit klíče a pomocí operace
                        split se prvky s nulovým bitem přemístí na začátek řazeného pole
                        řazených čísel a s jedničkovým bitem na konec




            procedure SPLIT_RADIX_SORT(A, number_of_bits)
            for i = 0 to (number_of_bits - 1) do
                   A = split(A, A<i>)

                PRL                                                                    34




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je         17
                      zakázáno.
```

### Strana 19

```text
Paralelní a distribuované algoritmy
                                 Radix sort - Operace split
            •     Jak udělat split? - sekvenční složitost je O(n)
            •     Idea
                      – pro každý prvek určíme správnou pozici a v konstantním čase
                        přemístíme (EREW)
            •     Postup
                           pro prvky s nulovým bitem se jejich pozice získá provedením  - prescan na
                            invertované pole bitů
                           pro prvky s jedničkovým bitem provedu  scan na reverzované pole bitů (tj.
                            od konce) a výsledek se odečte od n.

                 Analýza
                       split má stejnou složitost jako scan
                 Radix sort:
                         t(n) = O(n/N + log N).O(log n) = O(n/N.log n + log n . log N)

            PRL                                                                                          35




                                              Operace split
            procedure split(A, Flags)
               I-down = +-prescan(not(Flags))
               I-up = n - +-scan(reverse-order(Flags))
               for i=0 to n-1 do in parallel
                     if (Flags[i]) Index[i] = I-up[i]
                     else Index[i] = I-down[i] endif
               endfor
               result = permute (A, Index)




                                                                              7     7             8



                PRL                                                                                      36




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je                           18
                      zakázáno.
```

### Strana 20

```text
Paralelní a distribuované algoritmy
                                            Segmentovaný scan
            •     Definice
                   – Segmentovaná suma prefixů je operace, jejímž vstupem je
                      binární asociativní operátor , uspořádaná posloupnost prvků
                      [a0, a1, ..., an-1]
                      uspořádaná posloupnost příznaků
                      [f0, f1, ..., fn-1]
                   a která vrací posloupnost
                      [s0, s1, ..., sn-1]
                   kde v posloupnosti s jsou sumy prefixů přes jednotlivé segmenty,
                      kde hranice segmentu je dána hodnotou 1 v poli příznaků f
            •     Příklad :
                   – a                           = [5 1 3 4 3 9 2 6]
                   – f                           = [1 0 1 0 0 0 1 0]
                   – Segmented +_SCAN            = [5 6 3 7 10 19 2 8]
                   – segmented max_SCAN = [5 5 3 4 4 9 2 6]

                PRL                                                                                               37




                                                          Quicksort
            •     Jeden z prvků se vybere jako pivot (medián, náhodně, první), prvky
                  se rozdělí do 3 skupin (menší, rovné, větší než pivot) a pro každou
                  skupinu se rekurzivně volá quicksort
            •     Použije se segmentovaný scan a každá skupina bude ve svém
                  vlastním segmentu
            •     Algoritmus
                      – (1) zkontroluj, zda už prvky nejsou seřazené. Každý procesor se podívá, zda
                        předchozí procesor má menší, nebo stejnou hodnotu. S výsledky se provede and-
                        reduce
                      – (2) v každém segmentu najdi pivot a předej jej ostatním procesorům v segmentu.
                        Vybírá-li se jako pivot 1. prvek, lze použít segmented-copy-scan, kde binární
                        operátor copy vrací 1. ze svých 2 parametrů:
                                   a  copy(a, b)
                          » To má za následek rozšíření pivota v celém segmentu (lze také pivota vybírat jinak)
                      – (3) v každém segmentu porovnej prvky s pivotem a rozděl segment na 3 části (=,
                        <, >). Po rozdělení se použije modifikovaný split z radix-sortu.
                      – (4) v rámci každého segmentu vlož dodatečné příznaky, které rozdělí segment na
                        3 segmenty. Každý procesor se podívá na předchozí prvek a pozná, zda je na
                        začátku segmentu.
                      – (5) jdi na krok (1)


                PRL                                                                                               38




Petr Hanáček         Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je                                    19
                      zakázáno.
```

### Strana 21

```text
Paralelní a distribuované algoritmy

            klíč      6,4     9,2     3,4     1,6     8,7     4,1     9,2     3,4
            flags     1       0       0       0       0       0       0       0
            Pivots    6,4     6,4     6,4     6,4     6,4     6,4     6,4     6,4
            F         ==      >       <       <       >       <       >       <
            split     3,4     1,6     4,1     3,4     6,4     9,2     8,7     9,2
            flags     1       0       0       0       1       1       0       0
            pivots    3,4     3,4     3,4     3,4     6,4     9,2     9,2     9,2


            •   Analýza
                  – Každá iterace má konstantní počet operací scan
                  – Při vhodné volbě pivotů skončí algoritmus po O(log n) krocích,
                    takže složitost je:
                  – t(n) = O(n/N + log N).O(log n) = O(n/N.log n + log N. log n)
                  – c(n) = O(n.log N + N. log n. log N)
                            pro dostatečně malé N optimální
            PRL                                                                      39




                                    KONEC


            PRL                                                                      40




Petr Hanáček     Umístění tohoto dokumentu na jakýkoli (i neveřejný) server je           20
                  zakázáno.
```

### Strana 22

```text
             21

  The Complexity of
 Computation on the
Parallel Random Access
        Machine
          Faith E. Fich

    Department of Computer Science
         University of Toronto
        10 King's College Road
           Toronto, Ontario
          CANADA M5S 1A4




                  1
```

### Strana 23

```text
2     Chapter 21.   The Complexity of Computation on the PRAM

This chapter discusses the Parallel Random Access Machine (PRAM), various
parameters of this model, under what circumstances these parameters aect
its computational power, and how they do so. It also surveys techniques that
have been used to obtain lower bounds for specic problems on PRAMs.


                              21.1
                        The PRAM Model
      The PRAM is a synchronous model of parallel computation in which
processors communicate via a shared memory. It consists of m shared memory
cells M1  : : : Mm and p processors P1 : : : Pp . Each processor is a random
access machine (RAM) with a private local memory. During every step of a
computation, a processor may read from one shared memory cell, perform a
local operation, and write to one shared memory cell. Dierent processors
may execute dierent operations during a step and may make reference to
their own index. Reads, local operations, and writes are viewed as occurring
during three separate phases. This simplies analysis and only changes the
running time of an algorithm by a constant factor.
      An input x consists of n values x1  : : : xn. At the beginning of the
computation, these values are located in shared memory cells M1  : : : Mn ,
respectively, provided n  m. If there are n  m output values, they appear
                                             0


in the rst n shared memory cells at the end of the computation When
              0


the number of shared memory cells is too small, the input values can be
distributed approximately equally among the processors. Another possibility
is to have a separate, read-only memory containing the input values VW85,
LY89, FLRY89]. In this case, each processor is also allowed to read from one
of the n read-only memory cells during each computation step.
      EXERCISE 21.1
      Explain why it doesn't matter whether the input is initially located in
      the shared memory, the processors' local memories, or a separate read-
      only memory, provided the amount of shared memory is large enough to
      contain the input (i.e. m  n).
      If the amount of shared memory m is small, then where the input is
located is more important. For example, determining whether the input con-
tains two consecutive variables with value 1 requires (n=m) steps when the
input is distributed among the processors' local memories (Exercise 21.43).
```

### Strana 24

```text
                                                  21.1 The PRAM Model       3
However, when the input is in a separate read-only memory, this computation
can be done signicantly faster (Exercise 21.9).
       Limiting the amount of shared memory in a PRAM corresponds to re-
stricting the amount of information that can be communicated between pro-
cessors in one step. For example, a set of processors connected to one another
by a single bus may be viewed as a PRAM with one shared memory cell.
     THEOREM 21.1
     Any problem that can be solved by a PRAM using p processors in t steps
     can also be solved using p  p processors in O(tp=p ) steps.
                                0                            0



     PROOF
     The original p processors are partitioned into p groups of size at most
                                                         0


     dp=p e. Each of the p processors in the simulating machine is associated
          0                 0


     with one of these groups. To simulate one step of the original computa-
     tion, each of the p processors sequentially simulates the read and local
                        0


     computation phases performed by all the processors in its group and
     then sequentially simulates their write phases.
     EXERCISE 21.2
      ACF90] Give an example of a problem that can be solved in one step on
     a PRAM with p processors, but requires 2dp=p e ; 1 steps on a PRAM
                                                     0


     with p processors for 1  p < p.
              0                     0




     EXERCISE 21.3
     Prove that any problem that can be solved by a PRAM using m shared
     memory cells and p processors in t steps can also be solved using m  m
                                                                        0


     shared memory cells and maxfp m g processors in O(tm=m ) steps.
                                         0                        0




     EXERCISE 21.4
      Goo89] A forking PRAM is a PRAM in which a new processor is created
     when an existing processor executes a fork operation. In addition to
     creating the new processor, this operation species the task that the
     new processor is to perform (starting at the next time step). Initially
     there is one processor.
     Prove that if a forking PRAM algorithm uses t steps and p processors,
     then this algorithm can be implemented on a PRAM using O(t logp)
     steps and O(p= logp) processors. Explain explicitly how work is allo-
     cated to the PRAM processors.
```

### Strana 25

```text
4     Chapter 21.   The Complexity of Computation on the PRAM

       One consequence of Theorem 21.1 is that the processor-time product
p  t of any algorithm solving a problem is at least a constant factor times
the sequential time complexity of the problem. Thus, a lower bound on the
sequential time complexity gives a lower bound on the number of processors
needed for a PRAM to solve the problem in a given amount of time, as well
as a lower bound on the amount of time needed for a PRAM to solve the
problem using a given number of processors.
       A PRAM algorithm is optimal if it is not possible to simultaneously
improve both the time and the number of processors by more than a constant
factor. If a PRAM algorithm solves a problem in t steps using p processors,
where p  t is within a constant factor of the sequential time complexity of
the problem, then it is called ecient KRS90]. All ecient algorithms are
optimal, but not all optimal algorithms are ecient. For many problems, it
is interesting and important to nd the fastest possible ecient algorithm.
       Some people call a parallel algorithm optimal if its processor-time prod-
uct is within a constant factor of the running time of the fastest known se-
quential algorithm solving the same problem. Unless there is a matching
sequential lower bound for the problem, diculties may arise with this def-
inition. Specically, if a faster sequential algorithm is found, suddenly, the
parallel algorithm is no longer optimal. Furthermore, this denition of opti-
mality may preclude calling an algorithm optimal even when it is provably
impossible to simultaneously improve both the time and the number of pro-
cessors. For example, PARITY has linear sequential time complexity, but an
exponential number of processors are required by any PRAM that computes
it in constant time (Theorem 21.33).
       The PRAM is a natural generalization of the unit cost RAM CR73,
AHU74], a commonly used model of sequential computation. Numerous par-
allel algorithms have been designed for the PRAM because it is a simple,
precise model in which parallel algorithms can be expressed using a high level
language. The PRAM often corresponds to the programmer's view of par-
allel computation, ignoring lower level architectural details such as memory
organization, routing, memory contention, and synchronization. In essence,
PRAM programmers do not have to be concerned with how communication
is accomplished, but only what is to be communicated where. PRAMs can be
simulated by more realistic models MV84, UW87, Ran87, AHMP87, HP89]
and some real parallel computers Sch80, Smi90]. Thus, programs written for
the PRAM can be compiled into programs for these machines. Although some
of the assumptions (such as constant time access to shared memory) are not
```

### Strana 26

```text
                             21.2 Restrictions on Access to Shared Memory     5
generally valid, the performance of algorithms on the PRAM can be a good
predictor of their relative performance on real machines, especially as prob-
lem sizes get large. Furthermore, because the PRAM is a powerful model, the
lower bounds obtained for it are automatically applicable to a wide variety of
less powerful, more realistic machines.


                           21.2
        Restrictions on Access to Shared Memory
      An important parameter of the PRAM model is the extent to which
concurrent access to shared memory cells is allowed. If at most one processor
can read from a single memory cell at a particular step and at most one pro-
cessor can write to a single memory cell at a particular step, then the PRAM
is called exclusive read exclusive write (EREW) LPV81]. In a concurrent
read exclusive write (CREW) PRAM FW78], any number of processors can
simultaneously read from the same memory cell, but at most one processor
can write to each memory cell at a given step. Many algorithms designed for
CREW and EREW PRAMs avoid write conicts by having each processor
own one cell to which all its writes are performed. These restricted models
are called the concurrent-read owner-write (CROW) PRAM DR86] and the
exclusive-read owner-write (EROW) PRAM FW90], respectively.
      When concurrent writes are allowed, it is necessary to specify how con-
icts are resolved. Three of the most frequently used concurrent read concur-
rent write (CRCW) PRAMs are considered here. A number of others are dis-
cussed in the literature. (For example, see FRW88a, GR90, EG88, HR90].)
The COMMON model Kuc82] requires that all processors simultaneously
writing to the same memory cell write a common value. On the ARBITRARY
model Vis83], an arbitrary one of the values written to a memory cell at a
given step will appear in the cell. Any algorithm for this model must work
regardless of which value is chosen (say, by an adversary) to resolve each write
conict that arises. In the PRIORITY model Gol82], processors are assigned
xed, distinct priorities. The processor of highest priority among those that
simultaneously write to a memory cell succeeds. Without loss of generality,
we assume that lower indexed processors have higher priority.
      Any algorithm that runs on ARBITRARY will run unchanged on PRI-
ORITY. Thus PRIORITY is at least as powerful as ARBITRARY. Similarly,
ARBITRARY is at least as powerful as COMMON, COMMON is at least as
```

### Strana 27

```text
6      Chapter 21.    The Complexity of Computation on the PRAM

powerful as the CREW PRAM, and the CREW PRAM is at least as powerful
as the EREW PRAM. Diagrammatically,
PRIORITY  ARBITRARY  COMMON  CREW PRAM  EREW PRAM:
      It is important to understand the relationships between these models.
Specically, are some of these models strictly more powerful than others?
Can additional resources compensate for restricted access to shared memory?
Tradeos can help a computer architect choose among a number of design
alternatives or help a programmer compare algorithms written on dierent
models. A step by step simulation of a more powerful model by a less powerful
model is particularly useful because it allows the straightforward transforma-
tion of algorithms designed for the former into algorithms that can run on the
latter.
TABLE 21.1
Relationships Between PRAM Models
The fourth column contains bounds on the amount of time for the simulating
model using the indicated number of processors to simulate one step of the
original model with p processors. For the last three rows, the input is initially
distributed among the processors' local memories and both the original and
simulating models have m shared memory cells.
  Original         Simulating        Number of          Amount of          Reference
  Model            Model             Processors         Time
    PRIORITY         EREW PRAM                                                Thm 21.2
    ARBITRARY        CREW PRAM
                                        p                (log p)            Thm 21.3
    COMMON                                                                    Thm 21.23
    PRIORITY                                                                Thm 21.7
    ARBITRARY
                     COMMON              kp         k(log log
                                                            log p
                                                               p;log p)       Ex 21.13
                                                                    
    PRIORITY         ARBITRARY           kp           O log(
                                                           log log p
                                                              k +1))          Ex 21.14
    CREW PRAM        EREW PRAM          1            p
                                                     ( log p= log log p)      Ex 21.39
    PRIORITY         EREW PRAM                                                Ex 21.7
    ARBITRARY        CREW PRAM
                                      p+m    2
                                                          (p=m)
                                                                              Ex 21.44
    COMMON
    PRIORITY         COMMON              p                (log(p=m))          Thm 21.42
    ARBITRARY
    PRIORITY         ARBITRARY           p                (log(p=m))          Ex 21.41

   Table 21.1 summarizes some of the known relationships between the
PRAM models discussed above. The remainder of this section discusses these
```

### Strana 28

```text
                            21.2 Restrictions on Access to Shared Memory     7
and related results and the conditions under which they apply. Some of the
lower bounds are presented in Section 4.
     The rst simulation is quite simple. Moreover, it contains ideas that are
used in other simulations in this section.
     THEOREM 21.2 FRW88a]
     One step of PRIORITY with p processors and m shared memory cells
     can be simulated by an EREW PRAM in O(logp) steps with p processors
     and mp shared memory cells.
     PROOF
     Each PRIORITY processor is simulated by a corresponding EREW
     PRAM processor. For each original shared memory cell in PRIOR-
     ITY, the EREW PRAM will have p shared memory cells. One of these
     will contain the same sequence of values as the original cell. The other
     p ; 1 cells are assumed to be initialized to 0 and will be used to resolve
     conicting accesses to the cell.
     To simulate the write phase, each processor must know whether it is the
     leftmost processor (i.e. the processor of lowest index) wishing to write
     into some cell and, if so, it can perform the write. This leads to the
     denition of the following problem.
          LEFTMOST WRITERS
          Each processor Pi has a value in the range f0 : : : mg in its
          local memory, denoting the shared memory cell that Pi wants
          to access. The value 0 indicates that Pi does not want to
          access any cell. Each processor Pi must determine whether it
          is the leftmost processor among those with the same nonzero
          value.
     One way to solve this problem is to solve m simultaneous instances of
     the following problem, one for each of the original shared memory cells.
          LEFTMOST PRISONER
          Each processor has a bit, known only to itself, which is 1 if
          the processor wants to access the given memory cell. Each
          processor with value 1 must determine whether it is the left-
          most processor with value 1. Only processors with value 1 can
          participate in the computation.
```

### Strana 29

```text
8    Chapter 21.   The Complexity of Computation on the PRAM

    The name of this problem comes from imagining the processors to be
    prisoners who cooperate with one another to determine the lowest num-
    bered occupied prison cell. Note that all m instances can be solved
    simultaneously because every processor participates in at most one com-
    putation.
    The additional p ; 1 memory cells associated with each original memory
    cell are used to solve its LEFTMOST PRISONER problem. They are
    viewed as representing the internal nodes of a binary tree with p leaves
    (one corresponding to each processor) and depth dlog2 pe.
    All processors with value 1 are considered to be initially located at the
    corresponding leaves of the tree. The internal nodes of the tree are
    processed one level at a time, starting from the bottom. Each processor
    located at the right child of a node in the current level reads the value
    stored at the left child. When this value is 0, there is no processor located
    at the node's left child. In this case, the processor proceeds to the node
    and writes the value 1 there. Simultaneously, each processor located at
    the left child of a node in the current level proceeds to the node and
    writes the value 1 there. The processor that reaches the root of the tree
    is the leftmost processor that wants to access the given shared memory
    cell. Hence, it can perform the write to the cell. (An example appears
    in Figure 21.1.) Finally, processors retrace their steps back down the
    tree, erasing the values they have written at the nodes.
    To simulate the read phase, it is sucient to choose one processor to read
    each desired memory cell and distribute its contents to all interested pro-
    cessors. This can also be accomplished by performing the LEFTMOST
    PRISONER algorithm and having the processor that reaches the root
    read the given shared memory cell. As the processors go back down the
    tree, this value is written at each internal node that a processor reaches
    and is then erased. A processor waiting at a node can read the value
    from its parent at the appropriate time.
     A simplied version of this algorithm can be performed on COMMON
without using more shared memory than the original machine.
     EXERCISE 21.5
      FRW88a] Prove that one step of PRIORITY with p processors and m
     shared memory cells can be simulated by COMMON in O(logp) steps
     with p processors and m shared memory cells.
```

### Strana 30

```text
                             21.2 Restrictions on Access to Shared Memory     9


                                           0P
                                             PP
                             
                                                PP
                             0                          0
                        
                        0
                                Q
                                  Q
                                    0
                                                 
                                                 0
                                                           Q
                                                             Q
                                                               k
                                                               1 P7
                   0k A0k 0k A1kP 1k P AA0k
                    
                                           4     5


                                           0P
                                             PP
                             
                                                PP
                             0                          0
                        
                        0
                                Q
                                  Q
                                    1 P4
                                                 
                                                  
                                                 1 P5
                                                            Q
                                                             Q
                                                               k
                                                               1 P7
                   0k AA0k 0k AA1k 1k AA0k
                                           0P
                                             PP
                             
                                                PP
                             1 P4                       1 P5
                        
                        0
                                Q
                                  Q
                                    1
                                                 
                                                 1
                                                           Q
                                                             Q
                                                               k
                                                               1 P7
                   0k AA0k 0k AA1k 1k AA0k
                                            P4
                                           1P
                                             PP
                             
                                                PP
                             1                          1 P5
                        
                        0
                                Q
                                  Q
                                    1
                                                 
                                                 1
                                                           Q
                                                             Q
                                                               k
                                                               1 P7
                   0k AA0k 0k AA1k 1k AA0k
FIGURE 21.1
An example illustrating the processors going up the tree in the LEFTMOST PRIS-
ONER algorithm in the proof of Theorem 21.2. Here processors P4, P5, and P7
want to access the shared memory cell and processors P1 , P2 , P3 and P6 do not.
```

### Strana 31

```text
10     Chapter 21.   The Complexity of Computation on the PRAM

      The following simulation is more complicated than the simulation in
Theorem 21.2, but uses fewer shared memory cells. When m 2 (p), Exercise
21.3 and Theorem 21.1 can be applied to this result to show that no additional
processors or shared memory cells are needed for simulating PRIORITY by
an EREW PRAM in O(log p) steps.
     THEOREM 21.3         Eck79, Vis83, NS81]
     One step of PRIORITY with p processors and m shared memory cells
     can be simulated by an EREW PRAM in O(log p) steps with p processors
     and m + p shared memory cells.
     PROOF
     As in the proof of Theorem 21.2, each original shared memory cell has
     a corresponding shared memory cell in the EREW PRAM and the local
     operations of each original processor are performed by a corresponding
     processor in the EREW PRAM. An auxiliary array A of size p is also
     used.
     At a given read or write phase in the PRIORITY algorithm, if processor
     Pi wants to access cell Mj , it writes the pair (j i) to memory cell Ai . If
     Pi doesn't want to access any shared memory cell, it writes (0 i) to Ai .
     Notice that each of the indices 1 : : : p occurs as the second component
     of exactly one element of A. For example, if P1 wants to access cell M2 ,
     P2 wants to access cell M4, P3 wants to access cell M2 , P4 wants to
     access cell M1 , P5 wants to access cell M4, P6 wants to access cell M2 ,
     and P7 does not want to access any cell, the array A would have the
     following contents.
           (2,1) (4,2) (2,3) (1,4) (4,5) (2,6) (0,7)
     The array A is then sorted into lexicographic order. This takes O(log p)
     steps on an EREW PRAM with p processors. (See Chapter 12.)
           (0,7) (1,4) (2,1) (2,3) (2,6) (4,2) (4,5)
     Next, each processor Pi appends a bit to the contents of cell Ai . This
     bit is 0 when the rst component of Ai is either 0 or the same as the
     rst component of Ai 1  otherwise this bit is 1. Observe that processor
                           ;

     Pi is the highest priority processor wishing to access cell Mj if the triple
     (j i 1) appears in the array A.
            (0,7,0) (1,4,1) (2,1,1) (2,3,0) (2,6,0) (4,2,1) (4,5,0)
```

### Strana 32

```text
                            21.2 Restrictions on Access to Shared Memory       11
     In the example, P4 is the highest priority processor that wants to access
     M1 , P1 is the highest priority processor that wants to access M2 , and
     P2 is the highest priority processor that wants to access M4.
     From this point, it is easy to nish the simulation of a write phase. First,
     each processor Pk reads the triple (j i b) in Ak and writes this triple
     into Ai . Then processor Pi reads the triple (j i b) from Ai . If the bit b
     has value 1, then Pi is the highest priority processor that wants to write
     to Mj , so it can perform its write.
          (2,1,1) (4,2,1) (2,3,0) (1,4,1) (4,5,0) (2,6,0) (0,7,0)
     In this case, P1 writes to cell M2 , P2 writes to cell M4 , and P4 writes to
     cell M1 .
     Once the appropriate bit has been appended to the contents of each cell
     of A, a read phase can be simulated as follows. Each processor Pk reads
     the triple (j i b) in Ak . If the bit b has value 1, then Pk reads shared
     memory cell Mj and overwrites the third component of Ak with the value
     vj it read. These values are then duplicated as appropriate. Specically,
     for l = dlog2 pe : : : 1, processor Pk overwrites the third component of
     Ak+2l;1 with the third component of Ak , provided they have the same
     rst components. Here are the successive contents of the array in the
     example.
           (0,7,0) (1,4,v1) (2,1,v2) (2,3,0) (2,6,0) (4,2,v4) (4,5,0)
          (0,7,0) (1,4,v1) (2,1,v2) (2,3,v2) (2,6,0) (4,2,v4) (4,5,v4)
          (0,7,0) (1,4,v1) (2,1,v2) (2,3,v2) (2,6,v2) (4,2,v4) (4,5,v4)
     Finally, each processor Pk reads the triple (j i b) in Ak and writes it
     into Ai .
          (2,1,v2) (4,2,v4) (2,3,v2) (1,4,v1) (4,5,v4) (2,6,v2) (0,7,0)
     Now processor Pi can read the value it needs from Ai.
     Concurrent write PRAMs with p processors cannot, in general, be sim-
ulated by exclusive write PRAMs without an (log p) factor increase in time,
even with an innite number of processors and shared memory cells. This is
because the OR of n Boolean variables can be computed in one step on COM-
MON with n processors and one shared memory cell, but requires (log n)
```

### Strana 33

```text
12     Chapter 21.   The Complexity of Computation on the PRAM

steps on a CREW PRAM with an innite number of processors and shared
memory cells. (See Theorem 21.23.)
     EXERCISE 21.6
     Prove that the OR of n Boolean variables can be computed in O(logn)
     steps on an EROW PRAM with n= log2 n processors and n= log2 n shared
     memory cells.
      When the amount of shared memory m is small, signicantly more time
is needed to compute the OR of n input bits on a CREW PRAM, even with
an innite number of processors. If the input bits are initially located in
the processors' local memories, then (n=m) steps are required (see Exercise
21.44),
   p whereas,
           if they are located in a separate read-only shared memory,
 n=m steps are required Bea87, VW85].
     EXERCISE 21.7
     Prove that one step of PRIORITY with p processors and m shared
     memory cells can be simulated by an EREW PRAM in O(p=m) steps
     with p + m2 processors and m shared memory cells.
     EXERCISE 21.8
      VW85] Prove that the OR of n Boolean variables
                                                  plocated in a separate
                                                                  
     read-only shared memory can be computed in O n=m + log m steps
     on an EREW PRAM with O(pnm) processors and m shared memory
     cells.
     EXERCISE 21.9
     Suppose the input consists of n bitsp located in a separate read-only
     shared memory.p Prove that, in O( n=m + log m) steps, an EREW
     PRAM with O( nm) processors and m shared memory cells can deter-
     mine whether the input contains two consecutive variables with value 1.
     Prove that this problem can be solved in O(1) steps on COMMON with
     n processors and 1 shared memory cell.
     Both COMMON and ARBITRARY can simulate PRIORITY with only
a constant factor increase in time, by increasing the number of processors and
the amount of shared memory.
     THEOREM 21.4         Kuc82]
```

### Strana 34

```text
                           21.2 Restrictions on Access to Shared Memory       13

     One step of PRIORITY with p processors and m shared
                                                    ;   memory cells
                                                     p
     can be simulated by COMMON in O(1) steps with 2 processors and
     m + p shared memory cells.
     PROOF
     Processors P1 : : : Pp are responsible for simulating the original proces-
     sors. Simulation of the read and compute phases is trivial, since the two
     models do not dier in this respect. To simulate the write phase, each
     processor Pi writes the index of the location to which it wishes to write
     into the auxiliary shared memory cell Ai . As in the proof of Theorem
     21.3, the value 0 denotes the fact that Pi does not wish to write during
     this step. For example, the array A might contain the following values.
                             2 4 2 1 4 2 0
                 ;
     Each of the p2 processors then reads a dierent pair of memory cells in
     the array. If Ai and Aj contain the same value and i < j, the processor
     that read these two cells writes 0 into Aj . This results in the following
     array.
                             2 4 0 1 0 0 0
     Finally, for 1  i  p, memory cell Ai is read by processor Pi . If
     Ai contains a nonzero value j, then processor Pi is the lowest indexed
     processor that wants to write to location Mj and, thus, it can perform
     the write.
     The number of processors used to achieve a constant time simulation
can be reduced if more shared memory is available.
     EXERCISE 21.10
      FRW88a] Prove that one step of PRIORITY with p processors and m
     shared memory cells can be simulated by COMMON in O(1=") steps
     with minfp + mp"  p1+"g processors and mp"=2 shared memory cells, for
     any " 2 O(1).
     EXERCISE 21.11
      Cha91] A semi-oblivious PRAM algorithm is a PRAM algorithm such
     that, for each processor and at each step of the computation, there is
     at most one shared memory cell to which it writes. However, whether a
```

### Strana 35

```text
14    Chapter 21.    The Complexity of Computation on the PRAM

     particular processor decides to write at a particular step may depend on
     the state it is in (and hence on the values of the input). Prove that any
     step of a semi-oblivious PRIORITY algorithm that uses p processors
     and m shared memory cells can be simulated in constant time by a
     semi-oblivious COMMON algorithm using p processors and m+p shared
     memory cells.

     THEOREM 21.5         CDHR88]
     One step of PRIORITY with p processors and m shared memory cells
     can be simulated by COMMON in O(1) steps with p log2 p processors and
     mp + p shared memory cells.
     PROOF
     As in the proof of Theorem 21.2, for each shared memory cell Mj , the
     LEFTMOST PRISONER problem is solved using a binary tree with p
     leaves. However, instead of having processors proceed up the tree one
     level at a time, the bit values at all the internal nodes are determined
     simultaneously.
     For every original processor Pi, there are log2 p processors in the simu-
     lating machine. If processor Pi wants to write to memory cell Mj , these
     processors simultaneously write the value 1 to each ancestor of the ith
     leaf that has the ith leaf in its left subtree.
     Note that, after this step, an internal node has value 1 if and only if
     there is a leaf in its left subtree corresponding to an original processor
     that wants to write to Mj . Thus, processor Pi is the leftmost processor
     that wants to write to memory cell Mj if and only if every ancestor of
     the ith leaf that has the ith leaf in its right subtree contains the value 0.
     This can be determined in constant time by computing the OR of these
     values using one additional memory cell associated with processor Pi.
     Consider the example in Figure 21.2. Since P3 is in its parent's and
     great grandparent's left subtree and in its grandparent's right subtree,
     the OR that is computed has value 0. However, P4 is in its parent's and
     grandparent's right subtrees and P5 is in its great grandparent's right
     subtree, so the ORs that are computed for both these processors have
     value 1.
```

### Strana 36

```text
                             21.2 Restrictions on Access to Shared Memory       15

                                          1P
                                            PP
                             
                                               PP
                             0                      1
                        
                        0
                                Q
                                  Q
                                     1
                                               
                                               1
                                                       Q
                                                         Q
                                                          0k
                   0k A0k 1kP A1kP 1kP AA0k
                    
                                      3   4    5



FIGURE 21.2
The result of the rst step of the LEFTMOST PRISONER algorithm in the proof
of Theorem 21.5. In this example, p = 7 and processors P3 , P4, and P5 wish to
write to the shared memory cell.

     Even without increasing the number of processors, it is still possible to
simulate PRIORITY faster on COMMON than on the EREW PRAM.
     THEOREM 21.6           FRW88b]
     One step of PRIORITY with p processors and m shared memory cells
     can be simulated by COMMON in O(log p=loglogp) steps with p proces-
     sors and O(mp) shared memory cells.
     PROOF
     Here the LEFTMOST PRISONER problem is solved using a completely
     dierent approach. For p = 2, the problem can be solved in one write
     phase and one read phase using one shared memory cell that is initialized
     to 0. Specically, if P1 has value 1, it writes 1 into the cell. In this case,
     it is the leftmost processor with value 1. If P2 has value 1, it reads the
     cell. It is the leftmost processor with value 1 if and only if it reads the
     value 0.
     Given an algorithm that solves the problem for p = t! in t ; 1 write
     and read phases using mt 1 shared memory cells, we can construct an
                                 ;

     algorithm that solves the problem for p = (t + 1)! in t write and read
     phases using mt = (t + 1)mt 1 + 1 shared memory cells, as follows. The
                                      ;

     problem is divided into t + 1 subproblems of size t!. Group 1 consists
     of the rst t! processors, group 2 consists of the next t! processors, etc.
     Each subproblem is solved independently, using mt 1 shared memory
                                                              ;
```

### Strana 37

```text
16     Chapter 21.    The Complexity of Computation on the PRAM

     cells and t ; 1 of the write and read phases. One shared memory cell
     is used for the groups to interact with one another, so that the group
     containing the leftmost processor with value 1 can be determined. This
     cell initially contains the value 0. In the ith write phase, all processors
     (with value 1) in group i write 1 to the cell and in the next read phase
     all processors (with value 1) in group i + 1 read the cell. Notice that
     after the ith write phase, the cell contains the value 0 if and only if
     no processors in the rst i groups have the value 1. Thus if there are
     any processors with value 1 in group i + 1, they will learn whether their
     group contains the leftmost processor with value 1.
     The number of shared memory cells used to solve each leftmost prisoner
     problem satises the recurrence
                         m1 = 1
                         mt = (t + 1)mt 1 + 1 for t > 1:
                                            ;



     This implies mt 2 O((t + 1)!) = O(p). Therefore the total number of
     shared memory cells used in the simulation is O(mp).
     The ideas in the proofs of the two preceding theorems can be combined
to get increasingly faster simulations of PRIORITY by COMMON as the
number of processors in the simulating machine increases.
     EXERCISE 21.12
      Ragb, Bop89] Prove that one step of PRIORITY with p processors
     and m shared memory cells can be simulated by COMMON in t steps
     with kp processors, for 1  k  log2 p, provided t log2 t 2 O( logk p ) i.e.
     t 2 O( k(log loglogpp log k) ). How many shared memory cells do you use?
                     ;



      A matching ( k(log loglogpp log k) ) lower bound for solving the LEFTMOST
                              ;

PRISONER problem on COMMON has been achieved Ragb]. This does not
imply that the simulation of PRIORITY by COMMON in Exercise 21.12 is
optimal it only implies that a better simulation cannot be achieved by this
approach. However, the algorithm is known to be optimal for simulating
either PRIORITY or ARBITRARY with suciently large amounts of shared
memory. Consider the following problem.
      ELEMENT DISTINCTNESS
      Given n input values x1  : : : xn in the range f1 : : : rg, determine
      if they are pairwise distinct (i.e. xi 6= xj for i 6= j).
```

### Strana 38

```text
                              21.2 Restrictions on Access to Shared Memory     17
ELEMENT DISTINCTNESS is easy to solve on ARBITRARY (and, hence,
PRIORITY), given sucient shared memory.
      EXERCISE 21.13
      Prove that ELEMENT DISTINCTNESS can be solved in O(1) steps on
      ARBITRARY using n processors and r shared memory cells.
An algorithm for solving ELEMENT DISTINCTNESS on COMMON can be
obtained by simulating the algorithm in Exercise 21.13. using the simulation
in Exercise 21.12. If the size, r, of the input domain is suciently large, then
the resulting algorithm is optimal.
     THEOREM 21.7 Bop89, Edm91]
     COMMON with kn processors and an in nite amount of shared memory
                        log n
     requires ( k(log log;n log k) ) steps to solve ELEMENT DISTINCTNESS,
     provided the size of the input domain is suciently large.

      This result implies that, for r suciently large, COMMON with kn pro-
                                                       log n
cessors and innite shared memory requires ( k(log log   n log k) ) times as many
                                                          ;

steps to solve ELEMENT DISTINCTNESS as PRIORITY or ARBITRARY
with n processors and r shared memory cells. Thus, the simulation men-
tioned in Exercise 21.12 is optimal whenever the machine being simulated
has a suciently large shared memory. However, when the amount of shared
memory m is smaller (for example, only exponential in the number of proces-
sors), the optimality of this simulation is unknown. The diculty with using
ELEMENT DISTINCTNESS to separate COMMON from ARBITRARY and
PRIORITY in this case is that, if the domain size r is small, there are not
good lower bounds known for ELEMENT DISTINCTNESS on COMMON
and, if r is large, there are not good upper bounds known for ELEMENT
DISTINCTNESS on ARBITRARY or PRIORITY.
      ARBITRARY can simulate PRIORITY substantially faster than COM-
MON can.
     THEOREM 21.8        CDHR88]
     One step of PRIORITY with p processors and m shared memory cells
     can be simulated by ARBITRARY in O(loglog p) steps using p proces-
     sors and m(p ; 1) shared memory cells.
     PROOF
```

### Strana 39

```text
18     Chapter 21.    The Complexity of Computation on the PRAM

     This algorithm also works by solving thep  LEFTMOST PRISONER prob-
     lem. The processors are divided into p contiguous groups of size pp.
     Each group chooses a representative processor with value 1, if there is
     one. This is done as follows, using one cell for each group. The cell is
     initialized to 0. Then all processors that are in the group and have value
     1 attempt to write their indices into the cell. The processor whose index
     appears in the cell is chosen to be the representative for the group. All
     processors (with value 1) in the group can then read the cell to nd out
     which processor is the representative.
     For example, if there are nine processors, of which P5, P6, P7, and P9
     have value 1, then the memory cells associated with the three groups
     f1 2 3g, f4 5 6g, and f7 8 9g could contain the values 0, 6, and 7,
     respectively.
     Determining the leftmost p   group that contains a processor with value
     1 is a subproblem of size p that is solved recursively by the chosen
     representatives. Those processors (with value 1) that were not chosen as
     representatives are used to recursively determine the leftmost processors
     with p value 1 in their groups. Each of these subproblems has size less
     than p.
     The total time to solve a LEFTMOST       PRISONER problem of size p sat-
     ises the recurrence t(p) = t(pp)+O(1). This implies t(p) 2 O(loglog p).
     It can also be shown inductively that at most p ; 1 memory cells are
     used to solve a LEFTMOST PRISONER problem of size p.
      EXERCISE 21.14
       Ragb] Prove that one step of PRIORITY with p processors and m
                                                                       log log p
      shared memory cells can be simulated by ARBITRARY in O( log(         k+1) )
      steps with kp processors, for 1  k  log2 p. How many shared memory
      cells do you use?
      In particular, the result in Exercise 21.14 implies that one step of PRI-
ORITY with p processors can be simulated by ARBITRARY in O(1=") steps
using O(p(log p)") processors, for 0 < "  1.
                                               log log p
      There is a matching lower bound of ( log(   k+1) ) steps on ARBITRARY
for solving a generalized version of the LEFTMOST PRISONER problem in
which each input bit is known to a group of k processors Ragb]. It is open
whether a better simulation of PRIORITY by ARBITRARY can be achieved
in some other way.
```

### Strana 40

```text
                    21.3 Relationships Between PRAMs and Other Models        19
       When the amount of shared memory is small and the input is initially
distributed among the processors' local memories, o(log p) time simulations of
CRCW PRAMs with stronger write conict resolution mechanisms by CRCW
PRAMs with weaker ones are not possible without increasing the number of
processors or shared memory cells. Specically, (log(p=m)) steps are re-
quired to simulate either one step of ARBITRARY by COMMON or one step
of PRIORITY by ARBITRARY, using the same number of processors and
the same number of shared memory cells. (See Exercise 21.42 and Theorem
21.41.) If m 2 O(p1 ") for some constant " > 0, this implies that (log p)
                     ;


steps are required.
       It is more dicult to obtain lower bounds when the input is located
in a separate read-only shared memory. In this case, (log log(p=m)) steps
are known to be required to simulate ARBITRARY with p processors and m
shared memory cells by COMMON with p processors and m shared memory
cells and (log(p=m)= loglog(p=m)) steps are known to be required to simulate
PRIORITY with p processors and m shared memory cells by ARBITRARY
with m shared memory cells and any number of processors FLRY89]. In
contrast, PRIORITY and ARBITRARY require the same amount of time
to compute any symmetric Boolean function using one shared memory cell
 LY86, LY87].

                        21.3
  Relationships Between PRAMs and Other Models
      The PRAM is closely related to other models of computation. This
section considers relationships between PRAMs and four theoretical models:
Boolean circuits, unbounded fan-in Boolean circuits, Turing machines, and
decision trees. These relationships are important for obtaining a better un-
derstanding of parallel computation and because good upper and lower bounds
on PRAMs can often be obtained from corresponding bounds on these models.
      A Boolean circuit is a directed acyclic graph whose nodes are either
inputs, which have fan-in 0, or gates, which have fan-in at most 2. The inputs
are labelled by distinct variables. Each gate is labelled by a Boolean function
whose arity is equal to the fan-in of the gate. Some nodes are also designated
as outputs. The depth of a Boolean circuit is the length of the longest directed
path from an input to an output and its size is the number of gates it contains.
      A CROW PRAM can easily simulate a Boolean circuit using one pro-
cessor for each gate. The processor reads the values at the nodes with edges
```

### Strana 41

```text
20     Chapter 21.   The Complexity of Computation on the PRAM

directed into the gate as they become available, performs the gate computa-
tion, and writes the result in its shared memory cell. If the fan-out of every
node in the circuit is bounded by a constant, then the simulation can be done
using only exclusive reads. However, any Boolean circuit can be converted
to a Boolean circuit with nodes of fan-out at most 2 and only constant fac-
tor increases in size and depth HKP]. Therefore concurrent reads are not
necessary.
      THEOREM 21.9
      Any Boolean circuit of depth d and size s can be can be simulated by an
      EROW PRAM in O(d) steps using s processors and s shared memory
     cells.
      An unbounded fan-in Boolean circuit is a directed acyclic graph com-
posed of input nodes with fan-in 0, NOT gates with fan-in 1, and unbounded
fan-in AND and OR gates. Its depth is the length of the longest directed path
from an input to an output and its size is the number of edges in the graph.
Since COMMON can compute the AND or OR of n bits in one step using n
processors and one shared memory cell, it can easily simulate any unbounded
fan-in Boolean circuit.
     THEOREM 21.10          SV84]
     Any unbounded fan-in Boolean circuit of depth d and size s can be sim-
     ulated by COMMON in d steps using s processors and s shared memory
     cells.
      Any Boolean function f : f0 1gn ! f0 1g can be expressed by a formula
of size O(n2n) in disjunctive or conjunctive normal form and thus can be
computed by COMMON in two steps using exponentially many processors
and cells. More generally, COMMON can use table look-up to compute any
function f : f0 1gn ! R with Boolean inputs in two steps with n2n processors
and 2n shared memory cells. The idea is to allocate n processors to each
of the 2n possible inputs. Each group checks if it corresponds to the true
input by reading the input and performing an AND. One processor from the
unique group whose AND is 1 writes the answer. Thus it is impossible to get
nontrivial lower bounds on time for CRCW PRAMs without restricting the
number of processors or shared memory cells.
      EXERCISE 21.15
```

### Strana 42

```text
                    21.3 Relationships Between PRAMs and Other Models       21
      CSV84] Prove that any Boolean function computed by a Boolean circuit
     of depth O(log log n) can be computed by an unbounded fan-in circuit
     of depth two and nO(1) size.
      The complexity classes NCk and ACk consist of those Boolean functions
that can be computed in O((log n)k ) depth and nO(1) size by Boolean circuits
and unbounded fan-in Boolean circuits, respectively. Theorem 21.9 implies
that any problem in NCk can be solved by an EROW PRAM in O((logn)k )
steps using nO(1) processors. Similarly, by Theorem 21.10, any problem in
ACk can be solved by COMMON in O((log n)k ) steps using nO(1) processors.
It follows from Exercise 21.15 that any problem in NCk can be computed
by an unbounded fan-in circuit of depth O((log n)k = log log n) and size nO(1).
Combined with Theorem 21.10, this result shows that any problem in NCk
can be solved by COMMON in O((log n)k = loglog n) steps using nO(1) proces-
sors and nO(1) memory cells. Thus the upper bound on the time for solving
problems in NCk can be improved by allowing concurrent writes.
      The word size of a PRAM is the maximum number of bits that can be
contained in each cell of shared memory. Note that Theorems 21.9 and 21.10
and the corollaries mentioned above remain valid even with the restriction
that the word size is 1.
      Next, we consider some sequential complexity classes. Specically, let
DLOG denote the class of problems that can be solved by deterministic Tur-
ing machines using logarithmic space. Let NLOG be the analogous class for
nondeterministic Turing machines. Theorems 21.11 and 21.12 will show that
all problems in the classes DLOG and NLOG can be solved in logarithmic
time by the EROW PRAM and COMMON, respectively, using a polynomial
number of processors.
      The con guration graph of a Turing machine on a given input has one
node for each possible combination of state, head positions, work tape con-
tents, and time. Directed edges correspond to transitions. Note that the
conguration graph is acyclic. Furthermore, since a Turing machine has a
constant size alphabet, every node has constant fan-in and fan-out.
      If a Turing machine uses O(log n) space, then it uses nO(1) time and
its conguration graph has nO(1) nodes. Moreover, the conguration graph
can easily be constructed by an EROW PRAM in O(log n) steps using nO(1)
processors. Each node in the conguration graph of a deterministic Turing
machine has fan-out at most one. In this case, parallel tree contraction (see
Chapter 2) can be used to determine whether there is a path from the initial
```

### Strana 43

```text
22     Chapter 21.   The Complexity of Computation on the PRAM

conguration to an accepting conguration.
     THEOREM 21.11         FW78, KR90]
     Any problem in DLOG can be solved by an EROW PRAM in O(logn)
     steps using nO(1) processors.

      For nondeterministic Turing machines, it suces to compute the tran-
sitive closure of the conguration graph. This can be done by an unbounded
fan-in Boolean circuit with O(logn) depth and nO(1) size Bor77] and, hence,
from Theorem 21.10, by COMMON in O(log n) steps using nO(1) processors.

     THEOREM 21.12
     Any problem in NLOG can be solved by COMMON in O(log n) steps
     using nO(1) processors.
       For any problem in NP, a superlogarithmic lower bound on the EREW
PRAM with a polynomial number of processors would imply that DLOG is
strictly contained in NP. Similarly, !(log n=log log n) lower bounds on COM-
MON with a polynomial number of processors for problems in NP would imply
that NC1 is strictly contained in NP. Since it is currently unknown whether
the inclusions NC1  DLOG  NP are strict, such lower bounds could be
dicult to obtain.
       Unbounded fan-in Boolean circuits can also simulate PRAMs. A re-
stricted instruction set PRAM is a PRAM in which only addition, subtraction,
comparison, bitwise Boolean operations, read, write, and indirect addressing
are allowed. Multiplication and division of small numbers can also be permit-
ted without changing the results.
     THEOREM 21.13         SV84]
     A restricted instruction set PRAM with inputs of word size  using t
     steps and p processors can be simulated by an unbounded fan-in circuit
     of depth O(t) and size (pt)O(1).
In particular, any Boolean function that can be computed by a restricted in-
struction set PRAM in O((log n)k ) steps using nO(1) processors is in ACk .
If COMMON(t) denotes those Boolean functions that can be computed by a
```

### Strana 44

```text
                   21.3 Relationships Between PRAMs and Other Models          23
restricted instruction set COMMON PRAM in O(t) steps using nO(1) proces-
sors, then
       AC0                     NC1               DLOG  NLOG 
        k                        \          
  COMMON(1)            COMMON logloglogn n

       AC1                       NCk                              ACk
         k                              \                              k
                                             (log n)k
 COMMON(log n)                  COMMON       log log n           COMMON((log n)k ):
Note that by Theorem 21.4, these relationships are also valid when COMMON
is replaced by ARBITRARY or PRIORITY.
      PRAMs that allow a limited number of other instructions such as ar-
bitrary multiplication, division, and shifts have also been studied Tra88,
TLR88].
      An easy counting argument Ruz] shows that almost all Boolean func-
tions require exponential size unbounded fan-in circuits. Combining this re-
sult with Theorem 21.13 gives an analogous result for restricted instruction
set PRAMs.

     COROLLARY 21.14
     Almost all Boolean functions require an exponential number of processors
     to be computed by a restricted instruction set PRAM in polynomial time.
     Lower bounds for specic functions on unbounded fan-in Boolean circuits
can be translated into lower bounds on restricted instruction set PRAMs. For
example, consider the following lower bound for PARITY.
     THEOREM 21.15
      Has87] Any unbounded fan-in circuit of depth k that computes PARITY
     has size 2 (n         ).
                   1=(k;1)



In particular, any unbounded fan-in circuit with nO(1) size computing the
PARITY of n input bits (i.e. x1    xn) has depth (log n= loglog n).
Together with Theorem 21.13, this implies that any restricted instruction
set PRAM with nO(1) processors requires (log n= log log n) time to compute
```

### Strana 45

```text
24     Chapter 21.   The Complexity of Computation on the PRAM

PARITY. Since PARITY 2 NC1, it follows that this lower bound is tight to
within a constant factor.
      Lower bounds for computing specic problems, such as integer addition,
have also been directly obtained on restricted instruction set CRCW PRAMs
 MR84]. These proofs and the lower bounds obtained using Theorem 21.13
depend in an essential way on the restricted instruction set.
      In contrast, an abstract or ideal PRAM, places no restriction on the
instruction set. At each step, a processor can compute any function of its
local information. Furthermore, shared memory cells are allowed to contain
arbitrarily large values. Although this model is unrealistic, lower bounds in
this model have great generality since they do not depend on any assumptions
about the instruction set. These lower bounds are actually lower bounds on
the amount of communication, as opposed to the amount of computation, nec-
essary to solve a problem. They give insight into the nature of communication
between processors and may point out where bottlenecks in communication
arise. Abstract PRAMs also approximate the situation where communication
to and from shared memory is much more expensive than local operations,
for example, where each processor is located on a separate chip and access to
shared memory is through a combining network.
      Not surprisingly, abstract PRAMs can be much more powerful than
restricted instruction set PRAMs.

     THEOREM 21.16
     Any function of n variables can be computed by an abstract EROW
     PRAM in O(log n) steps using n= log2 n processors and n=2 log2 n shared
     memory cells.

     PROOF
     Each processor begins by reading log2 n input values and combining
     them into one large value. The information known by processors are
     combined in a binary-tree-like fashion. In each round, the remaining
     processors are grouped into pairs. In each pair, one processor commu-
     nicates the information it knows about the input to the other processor
     and then leaves the computation. After dlog2 ne rounds, one processor
     knows all n input values. Then this processor computes the answer in a
     single additional step.
```

### Strana 46

```text
                   21.3 Relationships Between PRAMs and Other Models        25
In particular, superlogarithmic lower bounds for time cannot be obtained on
an abstract PRAM without severely restricting the numbers of processors or
shared memory cells.
     EXERCISE 21.16
      Bea87, Bea88] Prove that any function f : f0 1gn ! R can be computed
     by abstract COMMON in log2 n ; log2 log2 (p=n) + O(1) steps using
     p  2n processors and p= log2(p=n) shared memory cells.
     Processors in an abstract PRAM can read and write arbitrarily large
values. However, to handle large input and output values, unbounded fan-in
Boolean circuits need large numbers of gates. Except for this technicality,
unbounded fan-in Boolean circuits can simulate abstract PRAMs.
     THEOREM 21.17         LY89]
     If an (abstract CRCW) PRAM computes a Boolean function in t steps
     using p processors, then the function can be computed
                                                      t+O(1)
                                                               by an unbounded
     fan-in Boolean circuit of depth O(t) and size p 2       .
     This result was proved using Kolmogorov complexity. Specically, given
a PRAM, the number of bits needed to describe the states of processors and
the addresses and contents of accessed shared memory cells does not grow too
quickly with time. In constant depth, an unbounded fan-in Boolean circuit
can compute these descriptions (rather than the actual states, addresses, and
contents) at any given step from the descriptions at the previous step.

     COROLLARY 21.18         BH89, Bea87]
     Almost all Boolean functions of n variables require log2 n ; log2 log2 p +
     (1) steps to be computed by an (abstract CRCW) PRAM with p pro-
     cessors.
      Together, theorems
                   p      21.15 and 21.17 imply that a PRAM with nO(1) pro-
cessors requires ( log n) steps to compute the PARITY of n bits. Although
this lower bound is not tight, the proof is much easier than the direct proof
of Theorem 21.33.
      Limiting the word size can signicantly aect the amount of time re-
quired to solve certain problems. Dierent organizations of memory, such as
a small number of shared memory cells with large word size or a large number
```

### Strana 47

```text
26     Chapter 21.    The Complexity of Computation on the PRAM

with small word size, can be better for dierent problems Bel88, Bel91]. For
reasonable bounds on the word size, improved versions of Theorem 21.17 and
Corollary 21.18 can be obtained.
      THEOREM 21.19           Bel88, Bel91]
      If an (abstract CRCW) PRAM with word size  computes a Boolean
      function using t steps and p processors, then the function can be com-
      puted by an unbounded fan-in circuit of depth O(t) and size pO(1) 2O(t) .



      COROLLARY 21.20
      Almost all Boolean functions of n variables require n log p steps to be
                                                                 ;


      computed by an (abstract CRCW) PRAM with word size  using p pro-
      cessors.

      From Theorems 21.15 and 21.19, it alsoOfollows    that an (abstract CRCW)
                    O
PRAM with (log n) word size and n
                      (1)                (log n) (1)
                                                     processors requires (log n= log log n)
steps to compute the PARITY of n input bits. Since PARITY is in NC1 , this
lower bound on time is tight to within a constant factor.
      The decision tree is a widely used model for obtaining sequential lower
bounds. An algorithm consists of a tree in which every internal node is labelled
by an input variable and every leaf is labelled by a possible answer. An internal
node has one child corresponding to each possible value of the input variable
that labels it. The execution of a decision tree algorithm begins at its root.
When an internal node is visited, the value of the input variable labelling the
node determines the appropriate child to visit next. The output is the label
of the leaf that is reached. The decision tree complexity of a problem is the
minimum depth of any decision tree that solves the problem (expressed as
a function of the number of input variables). Like the abstract PRAM, the
decision tree ignores the computation used to solve a problem. Rather, it
focuses attention on how much of the input must be examined to determine
the answer. There is a very close correspondence between the decision tree
model and the CROW PRAM.
      THEOREM 21.21           Raga]
```

### Strana 48

```text
               21.3 Relationships Between PRAMs and Other Models                        27
Any function that can be computed by a CROW PRAM in t steps can
be computed by a decision tree of height 2t .
PROOF
Consider any CROW PRAM that computes a function in t steps using
p processors. For 1  i  p and 1  t  t, let S(i t ) denote an ordered
                                               0                        0


pair consisting of the state of processor Pi and the contents of its corre-
sponding memory cell Mi immediately after step t . We will inductively
                                                                   0


dene decision trees T(i t ) that compute S(i t ). The desired decision
                              0                                0


tree can then be obtained from T (1 t) if the ordered pair labelling each
leaf is replaced by its second component.
Let qi be the initial state of processor Pi. If Mi initially contains the ith
input value, then T (i 0) is a tree of height 1. Its root is labelled xi and
there is a leaf labelled (qi v) for each possible value v of xi . Otherwise,
Mi initially contains the value 0 and T (i 0) consists of a single node
labelled (qi  0).
The decision tree T (i t + 1) is created by modifying the decision tree
                         0


T(i t ). Each leaf labelled (q v) in T(i t ) indicates that processor Pi
      0                                                0


is in state q and memory cell Mi contains v at the end of step t on                 0


those inputs that lead to the leaf. Suppose that, in this state, Pi reads
memory cell Mi0 during step t + 1. Then each leaf of T(i t ) labelled
                                       0                                        0


(q v) is replaced by the decision tree T (i  t ) and the labels of the leaves
                                                   0       0


are changed appropriately. Specically, the label (q  v ) of a leaf in this
                                                                        0   0


subtree is changed to (q  v ) if Pi goes into state q and writes the value
                         00       00                               00


v as a result of reading the value v from Mi0 .
 00                                        0



It is easy to verify that the height of T(i t ) is at most 2t0 .
                                                           0




THEOREM 21.22
 Raga] If a function can be computed by a decision tree of height h, then
it can be computed by a CROW PRAM in 1 + dlog2 he steps.
PROOF
Consider any decision tree of height h. Associate one CROW PRAM
processor with each node in the decision tree. Let processor P1 be associ-
ated with the root. To begin the computation, each processor associated
with an internal node reads the value of the input variable labelling its
```

### Strana 49

```text
28     Chapter 21.    The Complexity of Computation on the PRAM

     node and writes a pointer to the processor associated with the child cor-
     responding to that value. Then, using pointer jumping, the path in the
     decision tree from the root to a leaf can be determined in dlog2 he more
     steps.
      From Theorem 21.21, a lower bound of h on a decision tree implies
a lower bound of dlog2 he on a CROW PRAM. Thus the logarithm of the
decision tree complexity of a problem almost exactly characterizes the time it
takes to solve the problem on a CROW PRAM.
      EXERCISE 21.17
       Sni] Prove that a CROW PRAM requires dlog2 ne steps to compute the
      OR of n input bits, even if it is known that all possible inputs contain
      at most one bit with value 1.
     EXERCISE 21.18
      FR90] Prove that a CROW PRAM requires dlog2 (n;1)e steps to reverse
     the direction of the links in a singly linked list of length n.


                              21.4
                     Lower Bound Techniques
       Many of the lower bound proofs created specically for (abstract) PRAMs
look at how processors and memory cells accumulate knowledge about the
input as computation proceeds and what kinds of knowledge can be accumu-
lated. They also nd ways of measuring that knowledge and then showing
that it cannot increase too quickly.
       One of the facts that makes proving PRAM lower bounds dicult is
that processors can communicate information by deciding not to write to a
particular shared memory cell. This is nicely illustrated by the following
example in which x1 _ x2 _ x3 _ x4 _ x5 is computed in 2 steps on an EREW
PRAM. Note that, by Exercise 21.17, a CROW PRAM requires 3 steps for
this computation.
       Initially, memory cells M1  M2  M3 M4, and M5 contain the input bits
x1  x2 x3 x4, and x5 , respectively. During step 1,
       processor P1 reads M2 and, if x2 = 1, writes 1 into M1 ,
       processor P3 reads M4 and, if x4 = 1, writes 1 into M3 , and
       processor P5 reads M5 ,
```

### Strana 50

```text
                                               21.4 Lower Bound Techniques     29
resulting in the following memory contents.
            x1 _ x2 x2             x3 _ x4 x4               x5
      At step 2, processor P5 reads M3. If x5 _ (x3 _ x4) = 1, then P5 writes 1
into M1 . At this point, memory cell M1 contains the value x1 _ x2 _ x3 _ x4 _ x5,
as desired. Note that processor P5 communicates the fact that x3 _ x4 _ x5 = 0
by not writing into memory cell M1 .
      This idea can be generalized to show that the OR of n bits can be
computed almost 1.4 times faster on an EREW PRAM than on a CROW
PRAM. The tth Fibonacci number, Ft , is dened by the recurrence
                         F0 = 0
                         F1 = 1 and
                         Ft = Ft 1 + Ft 2 for t  2
                                  p                         p
                                    ;       ;


and satises the inequalities ((1+ 5)=2)t 2 < Ft  ((1+ 5)=2)t 1 for t > 0.
                                           ;                         ;




      EXERCISE 21.19
       CDR86] Prove that an EREW PRAM can compute the OR of n input
      bits using n processors and shared memory cells in t steps, provided
      F2t+1  n.
      In the example above, there is at most one processor that writes into a
particular memory cell at a particular time step on any input. This is not the
case for all EREW and CREW PRAM algorithms. Depending on the input,
dierent processors may write into a particular cell at a given step. However,
the conditions under which the dierent processors perform these writes are
mutually exclusive. The fact that none of these conditions are satised by
the input is conveyed when no write occurs. Under some circumstances, this
could be a lot of information. For example, if the input is known to contain at
most one bit with value 1, then the OR of the input bits can be computed in
one step on an EREW PRAM. This is accomplished by having each processor
read an input bit and, if it reads the value 1, write 1 to memory cell M1.
In contrast, from Exercise 21.17, a CROW PRAM requires dlog2 ne steps to
perform this computation.

       21.4.1 Sensitivity, Block Sensitivity, and Degree
      The algorithm in Exercise 21.19 is optimal. More generally, it is possible
to characterize, to within a small constant factor, the time needed to compute
total n-ary functions on a CREW PRAM in terms of certain simple properties.
```

### Strana 51

```text
30     Chapter 21.       The Complexity of Computation on the PRAM

      A function f with domain D  D1    Dn and range R is sensitive
to the set of coordinates S  f1 : : : ng on input x 2 D if there exists an input
y 2 D such that f(x) 6= f(y) and xj = yj for all j 62 S. The sensitivity or
critical complexity of f is
                   max
                   x D
                     2
                        #fijf is sensitive to fig on input xg.
For example, the OR of n Boolean variables has sensitivity n (consider the
all 0 input) as does their PARITY (consider any input). The function that
computes the MAXIMUM of any n input values also has sensitivity n.
      The sensitivity of a function can be used to obtain a lower bound on the
amount of time necessary to compute it on a CREW PRAM. This is done by
showing that the number of coordinates aecting the state of a processor or
the contents of a memory cell cannot grow too quickly as the computation
proceeds. Formally, coordinate i aects processor P (or memory cell M)
on input x 2 D1    Dn at time t if the state of P (or contents of M)
immediately after step t is dierent on the inputs x and y, for some input
y 2 D1    Dn that is the same as x except in coordinate i. Since the
maximum number of coordinates that aect memory cell M1 at the end of
the computation must be at least the sensitivity of the function f, this leads
to a lower bound on time.
     THEOREM 21.23            CDR86]
     A CREW PRAM requires at least logb(sensitivity(f))
                                                    p steps to compute
     a function f : D1    Dn ! R, where b = (5 + 21)=2.
     PROOF
     Let s(t) and c(t) denote the maximum number of coordinates aecting
     any processor or shared memory cell, respectively, on any input at time
     t. Then
                              s(0) = 0 and c(0) = 1:
     Suppose processor P reads from memory cell M on input x during step
     t. Then any coordinate i aecting P on input x at time t either aects
     P on input x at time t ; 1 or aects M on input x at time t ; 1. To see
     this, consider any input y that diers from x only in coordinate i and
     causes P to have a dierent state immediately after step t. If, on input
     y, P is in the same state at time t ; 1 as it is on x, then it reads from
     cell M during step t. Furthermore, if it nds the same value there, then
```

### Strana 52

```text
                                       21.4 Lower Bound Techniques       31
processor P is in the same state immediately after step t on both these
inputs, a contradiction. Thus
                        s(t)  s(t ; 1) + c(t ; 1):
Now consider any shared memory cell M on any input x. There are two
cases to consider. If some processor P writes to M on input x during
step t, then any coordinate aecting M on input x at time t also aects
P on input x at time t. There are at most s(t) such coordinates.
Otherwise no processor writes to M on input x during step t. Let i be
any coordinate that aects M on input x at time t. If i does not aect
M on input x at time t ; 1, there must be an input y(i) that diers from
x only in coordinate i and a processor P (i) that writes to M on input
y(i) during step t.
Let j be any other coordinate that aects M on input x at time t.
If P (i) 6= P (j ), then either coordinate j aects P (i) on input y(i) or
coordinate i aects P (j ) on input y(j ) at time t. Otherwise, during step
t, processors P (i) and P (j ) would both write to M on input z, where
                               8 (i)
                               >
                               < yi if k = i
                         zk = > yj(j ) if k = j
                               : xk otherwise.
Suppose there are exactly v coordinates that aect M on input x at
time t, but not at time t ; 1. Consider a graph whose vertices are these
v coordinates. In this graph there is an edge from i to j if and only if
P (i) 6= P (j ) and coordinate j aects P (i) on input y(i) at time t. Since
no processor is aected by more than s(t) coordinates at time t on a
given input, this graph contains at most v  s(t) edges.
For any processor P, at most s(t) of the v coordinates i are such that
P = P (i) . This is because these coordinates all aect P on input x at
time t. Thus there are at least v  (v ; s(t)) ordered pairs (i j) such
that P (i) 6= P (j ). At least half of these must be edges in the graph.
Hence v  s(t)  v  (v ; s(t))=2, which implies that v  3s(t). Since M
is aected by at most c(t ; 1) + v coordinates at time t,
                           c(t)  c(t ; 1) + 3s(t):
From the solution of the resulting recurrence, it follows that s(t) c(t) <
bt so at least logb(sensitivity(f)) steps are required to compute f.
```

### Strana 53

```text
32     Chapter 21.   The Complexity of Computation on the PRAM

     EXERCISE 21.20
     CDR86] Show that the OR of n input bits can be computed in k +
     O(log k) steps on a CREW PRAM if the input is known to contain at
     most k bits with value 1.
     EXERCISE 21.21
     Where does the proof of Theorem 21.23 break down for computing the
     OR of n input bits, when the input is known to contain at most one bit
     with value 1?
     EXERCISE 21.22
     Prove that a CREW PRAM requires (minfk logng) steps to compute
     the OR of n input bits, when the input is known to contain at most k
     bits with value 1.
      EXERCISE 21.23                                          p
       Bea87] Prove that no coordinate aects more than (2+ 3)t processors
      or memory cells after t steps of an EREW PRAM computing a Boolean
      function.
      The function f depends on coordinate i if f is sensitive to fig on some
input x 2 D1    Dn . In other words, there are two inputs x and y,
diering only on coordinate i, such that f(x) 6= f(y).
     THEOREM 21.24 Sim82]
     Every function f : f0 1gn ! f0 1g that depends on k of its coordinates
     has sensitivity (logk).

     COROLLARY 21.25           Sim82]
     A CREW PRAM requires (log log k) steps to compute any function
     f : f0 1gn ! f0 1g that depends on k of its coordinates.
     EXERCISE 21.24
     Consider the Boolean addressing function f : f0 1gn ! f0 1g dened
     by
                       f(x1  : : : xr  y0  : : : y2r 1 ) = yj 
                P r
                                                ;


     where j = i=1 xi2r i and n = r + 2r . It uses the binary number
                           ;


     formed by concatenating the rst r bits as an index to select one of the
```

### Strana 54

```text
                                            21.4 Lower Bound Techniques       33
       remaining bits. Prove that this Boolean function has sensitivity r + 1
       and depends on all n of its coordinates. How quickly can you compute
       this function on a CREW PRAM?
       EXERCISE 21.25
       Show that the addressing function f : f0 : : : n ; 1g f0 1gn ! f0 1g
       dened by
                               f(i y0  : : : yn 1) = yi
                                              ;



       can be computed by a PRAM in constant time using only one processor.
       Explain the dierence between this result and Exercise 21.24.
     A very useful generalization of sensitivity is block sensitivity Nis89]. For
any function f with domain D  D1    Dn , it is dened to be
 max
 x D
   2
     maxfkjf is sensitive to k disjoint subsets of coordinates on input xg.
Clearly, the sensitivity of a function f is bounded above by its block sensi-
tivity. However, there are functions whose sensitivity is less than their block
sensitivity. (See Exercises 21.26 and 21.27.) It is an open question whether
the sensitivity of a function is always at least some polynomial of its block
sensitivity or whether it can be exponentially smaller.
       EXERCISE 21.26
        Nis89, WZ88] Consider the Boolean function of n variables that has
       value 1 when exactly bn=2c or bn=2c + 1 of the input bits have value
       1. What is the sensitivity, the block sensitivity, and the decision tree
       complexity of this function?
       EXERCISE 21.27
        Rub] Exhibit a Boolean function of n variables with sensitivity O(pn)
       and block sensitivity (n).
The lower bound in Theorem 21.23 can be extended to block sensitivity.
       THEOREM 21.26         Nis89]
       A CREW PRAM requires at least logb (block sensitivity(f))
                                                              p steps to
       compute a function f : D1    Dn ! R, where b = (5 + 21)=2.
       PROOF
```

### Strana 55

```text
34     Chapter 21.     The Complexity of Computation on the PRAM

     Suppose the block sensitivity of f is k and, on input x, f is sensitive to
     the disjoint sets of coordinates S1  : : : Sk . For j = 1 : : : k, let y(j ) 2
     D1    Dn be an input such that f(y(j ) ) 6= f(x) and yi(j ) = xi for all
     i 62 Sj . Given (z1  : : : zk ) 2 f0 1gk, dene g(z1  : : : zk ) to be the value
     of the function f on the input w = (w1 : : : wn), constructed as follows.
     If zj = 1, then make w agree with y(j ) on all coordinates in the set Sj .
     If zj = 0, then make w agree with x on all coordinates in the set Sj . On
     those coordinates not in any of the sets S1  : : : Sk , also make w agree
     with x. In other words,
                                 ( (j)
                          wi =      yi     if i 2 Sj and zj = 1
                                    xi     otherwise.
     The function g : f0 1gk ! R has sensitivity k and can be computed by
     a CREW PRAM at least as quickly as the function f. It follows that
     any CREW PRAM requires at least logb (k) steps to compute f.
      A set of coordinates C is a certi cate for a function f on an input x
if f(x) = f(y) for every input y that agrees with x on all coordinates in C.
In other words, knowing the values xi for all i 2 C determines the value of
f(x). For example, a set of coordinates corresponding to the variables in a
minterm or maxterm of a Boolean function is a certicate. The certi cate
complexity or nondeterministic decision tree complexity of a function f with
domain D  D1    Dn is
              max
              x D
                2
                  minf#C jC is a certicate for f on input xg.
The block sensitivity, certicate complexity, and decision tree complexity of
a function f : D1    Dn ! R are always closely related.
     EXERCISE 21.28
     Prove that, for any function f : D1    Dn ! R, block sensitivity(f)
      certi cate complexity(f)  decision tree complexity(f).
     THEOREM 21.27 Nis89]
     For any function f : D1    Dn ! R, certi cate complexity(f ) 
     (block sensitivity(f))2 .
     PROOF
```

### Strana 56

```text
                                        21.4 Lower Bound Techniques         35
Suppose the block sensitivity of f is k. For any input x, let B be a
maximal collection of disjoint sets of coordinates such that each S 2 B
is a minimal set of coordinates to which f is sensitive on input x. Note
that jBj  k. Let C = fS jS 2 Bg be the coordinates that occur in the
sets in B.
Then C is a certicate for f on input x. To see why, suppose there
was an input y that agreed with x on all coordinates in C such that
f(x) 6= f(y). Let C be the set of coordinates on which y diers from
                      0


x. Then f is sensitive to C on input x. Let C be a minimal subset
                              0                      00


of C to which f is sensitive on input x. Since C and C are disjoint,
      0                                                            00


C is disjoint from each S 2 B. But then B fC g is a collection of
 00                                                           00


disjoint minimal sets of coordinates to which f is sensitive on input x,
contradicting the maximality of B.
To complete the proof, it suces to show that jS j  k for each S 2 B,
because this implies that jC j  k2 . Consider any S 2 B and let y be
an input that agrees with x on all coordinates not in S and such that
f(x) 6= f(y). Then, by the minimality of S, for each i 2 S, fig is a set
of coordinates to which f is sensitive of input y. Clearly ffigji 2 S g is a
disjoint collection of sets. Since the block sensitivity of f is k, it follows
that jS j  k.


THEOREM 21.28 BI87, HH86, Tar88]
For any function f : D1    Dn ! R, decision tree complexity(f )
 (certi cate complexity(f))2 .
PROOF
First note that if f(x) 6= f(y), then every certicate C for f on input
x intersects every certicate C for f on input y. Otherwise, it would
                                  0


be possible to construct an input z consistent with x at all coordinates
in C and consistent with y at all coordinates in C , which would imply
                                                          0


that f(x) = f(z) = f(y).
Suppose 0  l  k and, for some r 2 R, every input x 2 f 1 (r) has a    ;


certicate of size at most k and every input y 62 f 1 (r) has a certicate of
                                                    ;


size at most l. We prove by induction that decision tree complexity(f) 
kl.
```

### Strana 57

```text
36     Chapter 21.   The Complexity of Computation on the PRAM

     If jRj = 1, then f is a constant function and decision tree complexity(f) =
     0  kl. Therefore, assume jRj > 1.
     If f has no input in its domain with value r, consider the function f that
                                                                          0


     is identical to f except that it does not contain r in its codomain. Since
     every input has a certicate of size at most l, decision tree complexity(f) =
     decision tree complexity(f )  l2  kl.
                                0



     Otherwise, choose an input in f 1 (r) and construct a decision tree T
                                       ;


     whose rst k levels are labelled by the variables in a length k certicate
     for f on that input. For each node v at depth k, consider the restriction
     fv of f to the subdomain in which these k variables have the values
     specied by the path to v. Since every input x 2 f 1 (r) has a certicate
                                                         ;


     of size at most k and every input y 62 f 1 (r) has a certicate of size
                                                ;


     at most l that contains at least one of these k variables, every input
     x 2 fv 1 (r) has a certicate of size at most k and every input y 62 fv 1 (r)
      0    ;                                                         0    ;


     has a certicate of size at most l ; 1. Thus fv has a decision tree of height
     at most k(l ;1). This tree is rooted at node v of T. The resulting decision
     tree T computes f and has height at most k + k(l ; 1) = kl.

      EXERCISE 21.29
       BSVW86] Prove that, for any monotone Boolean function f, sensitivity(f)
      = certi cate complexity(f).
      Both log(block sensitivity(f)) and log(decision tree complexity(f)) char-
acterize the time to compute a function f : D1    Dn ! R on a CREW
PRAM to within a small constant factor. This follows from Theorems 21.27
and 21.28, the fact that logb (block sensitivity(f)) is a lower bound on the
time for a CREW PRAM to compute f (Theorem 21.26), and the fact that
1 + dlog2(decision tree complexity(f))e is an upper bound on the time for a
CROW PRAM and, hence, a CREW PRAM to compute f (Theorem 21.22).
Moreover, given a CREW PRAM algorithm computing such a function, it
is possible to construct a CROW PRAM algorithm to compute the function
to within a constant factor as fast. However, the new algorithm is not nec-
essarily a step by step simulation of the original algorithm and it might use
exponentially more processors. It is an open question whether such a large
blowup in the number of processors is necessary.
      For many of these results, it is essential that the domain of the function
f is complete, i.e. if there are n inputs, then the domain of f can be expressed
as the direct product of n sets of values. In other words, the value of any
```

### Strana 58

```text
                                                    21.4 Lower Bound Techniques           37
input variable is not constrained by the values of other input variables. The
results are not necessarily true when the domain of f is not complete.
      For example, the OR of n bits when it is known that at most one bit is
1 can be computed in one step on a CREW PRAM, but the sensitivity of this
function is n and it requires log2 n steps on a CROW PRAM. (See Exercises
21.20 and 21.17.) Similarly, reversing a singly linked list or a disjoint collection
of circular singly linked lists of length n has decision tree complexity n ; 1
(Exercise 21.18), although this can be done in one step on a CREW PRAM
 FR90]. In contrast, when reverse pointers are also present, the situation is
quite dierent.
      THEOREM 21.29              FR90]
      A CROW PRAM can compute any function of a disjoint collection of
      circular doubly linked lists to within a constant factor as fast as a CREW
      PRAM.

      Additional work needs to be done to understand what problems can be
solved more quickly by a CREW PRAM than by a CROW PRAM.
      Lower bounds that exactly match the upper bounds for certain Boolean
functions have been obtained by considering yet another property. For any
Boolean function f : f0 1gn ! f0 1g, there is a unique multilinear polynomial
                                             X               Y
                              Pf (x) =                  aI         xi
                                         I f1:::ng        i2I
with integer coecients that represents f in the sense that Pf (x) = f(x)
whenever x 2 f0 1gn. Moreover, the coecients aI have absolute value at
most 2n 1 Smo87]. For example, if f(x1  : : : xn) = x1 ^    ^ xn, then
          ;


Pf (x1  : : : xn) = x1    xn and if f(x1  : : : xn) = x1_  _xn, then Pf (x1  : : : xn) =
1 ; (1 ; x1)    (1 ; xn). The degree of the Boolean function f is dened to
be the degree of the polynomial Pf .
      EXERCISE 21.30
       DKR90] Prove the following facts about the degrees of Boolean func-
      tions.
          1. degree(f) = degree(f).
          2. degree(f ^ g)  degree(f) + degree(g).
          3. degree(f _ g)  degree(f) + degree(g).
```

### Strana 59

```text
38     Chapter 21.   The Complexity of Computation on the PRAM

       4. If f ^ g  0, then degree(f _ g)  maxfdegree(f), degree(g)g.
      Since the OR of n bits has degree n, the following result shows that the
algorithm in Exercise 21.19 is the fastest possible on a CREW PRAM.
     THEOREM 21.30          DKR90]
     If a CREW PRAM computes a Boolean function f : f0 1gn ! f0 1g in
     t steps, then F2t+1  degree(f).
     PROOF
     Without loss of generality, we make the following two assumptions.
     First, a processor's state is merely (an encoding of) the sequence of
     values it has read at each step (so a processor never forgets informa-
     tion). Second, whenever a processor writes, it identies itself and its
     current state (i.e. it communicates everything it knows).
     For each processor, partition the set of inputs f0 1gn so that inputs are
     in the same block if and only if they cause the processor to be in the
     same state immediately after step t. Let s(t) denote the maximum de-
     gree of the characteristic function of any block of one of these partitions.
     Similarly, let c(t) denote the maximum degree of the characteristic func-
     tion of any block of the partition of f0 1gn induced by a shared memory
     cell's contents immediately after step t. Then, as in the proof of Theorem
     21.23,
                      s(0) = 0
                      c(0) = 1 and
                      s(t)  s(t ; 1) + c(t ; 1) for t > 0:
     Now consider the characteristic function of any block of the partition
     induced by the contents of a shared memory cell M, immediately after
     step t. If, in state q, processor Pi writes into M during step t, then the
     characteristic function giq : f0 1gn ! f0 1g of the set of inputs that
     cause Pi to be in state q at time t is also the characteristic function of
     the set of inputs for which M contains the value (i q) immediately after
     step t. This function has degree at most s(t), by denition.
     Suppose, instead, that no processors write to M during step t and M
     contains the value v immediately after step t. Let g be the characteris-
     tic function identifying those inputs for which M contains the value v
```

### Strana 60

```text
                                                 21.4 Lower Bound Techniques          39
     immediately after step t ; 1. Then the characteristic function g of the      0


     corresponding block of the partition induced by M's contents at time t
     can be expressed as                 _
                                 g = g ^ giq 
                                        0


                                                iq
     where the OR is taken over all values of i and q such that, in state q,
     processor Pi writes to M during step t. Since concurrent writes to M
     cannot occur, at most one of the functions giq has
                                                      0 value 11 for a given
                                                                     _
     input. From Exercise 21.30, it follows that degree @ giq A  s(t). By
                                                                     iq
     denition, degree(g)  c(t ; 1). Thus degree(g )  c(t ; 1) + s(t) and,
                                                             0


     hence,
                         c(t)  c(t ; 1) + s(t) for t > 0:
     It is easy to prove by induction that s(t)  F2t and c(t)  F2t+1 for
     all t  0. The theorem then follows from the fact that degree(f) is
     bounded above by the maximum degree of the characteristic functions
     of the blocks of the partition induced by M1 's contents at the end of the
     computation.

     EXERCISE 21.31
     DKR90] Let n = k2 and consider the function
            f(x1  : : : xn) = (x1 ^    ^ xk ) _    _ (xn k+1 ^    ^ xn):
                                                                 ;



     Prove that the certicate complexity of f is k and its degree is n. What
     is its decision tree complexity?
     EXERCISE 21.32
     Prove that the degree of any Boolean function is always bounded above
     by its decision tree complexity.
     THEOREM 21.31             Sze89]
     The block sensitivity of any Boolean function is bounded above by the
     square of its degree.
For special classes of Boolean functions, better results can be shown.
```

### Strana 61

```text
40     Chapter 21.   The Complexity of Computation on the PRAM

     EXERCISE 21.33
     DKR90] Prove that the sensitivity of a monotone Boolean function is
     bounded above by its degree.
     THEOREM 21.32          DKR90]
     Any nonconstant, symmetric, Boolean function of n variables has degree
     larger than n=2.

      The time taken by a randomized CREW PRAM to compute a Boolean
function is also related to the function's block sensitivity and degree Nis89,
DKR90]. These results imply that a randomized CREW PRAM cannot com-
pute a Boolean function more than a constant factor faster than a determin-
istic CROW PRAM.

       21.4.2 Simplifying the Algorithmic Structure by
                        Restricting the Input
      A variety of lower bounds for the PRAM have been obtained as follows.
Given an algorithm to solve a problem, nd a restricted problem, either on
a smaller number of input variables or a smaller input domain, on which the
algorithm behaves in a considerably simpler manner. Then lower bounds are
proved directly for this class of simpler algorithms.
      It is useful to consider the partitions of the set of inputs into blocks
that are indistinguishable to a processor or a memory cell during the rst t
steps of the computation. As time increases, these partitions become more
complicated. The proofs of the next results use the technique of random
restrictions to show that these partitions do not become suciently complex
too quickly. Essentially, after each step of the computation, the values of
relatively few randomly chosen bits are xed. This leaves only a slightly
smaller instance of the problem. It can be shown that the resulting partitions
of the set of inputs are likely to remain quite simple in structure.
      THEOREM 21.33 BH89]
      If PRIORITY     computes the PARITY of n input bits in t steps, then it
      uses 2 (n1=t) processors and 2 ((n=t!)1=t) shared memory cells.


     COROLLARY 21.34          BH89]
```

### Strana 62

```text
                                             21.4 Lower Bound Techniques       41
     PRIORITY with n0(1) processors or shared memory cells requires (log n= loglog n)
     steps to compute the PARITY of n input bits.

     THEOREM 21.35 BH89]
     For all t 2 31 log n=log log n ; !(log n=(log logn)2 ), there is a Boolean
     function of n variables that can be computed by COMMON in t steps
     using n processors and memory cells, but cannot be computed by PRI-
     ORITY in t ; 1 steps using n0(1) processors or using nO(1) memory
     cells.

Thus, even one extra time step can be more useful than increasing the number
of processors or shared memory cells by a polynomial factor or using a more
powerful write resolution rule.
      An early example of this approach was applied to the following problem
 Sni85].
     SEARCH AN ORDERED LIST
     Given x1 : : : xn y 2 f1 : : : rg such that x1  x2  : : :  xn ,
     determine that either y < x1 or xn  y or nd the index i such
     that xi  y < xi+1 .
Using (p + 1)-ary search, a CREW PRAM with p processors can solve this
problem in time O(log n= log(p + 1)). A nontrivial lower bound can be ob-
tained on an EREW PRAM, even for the restricted version of the problem
in which x1 : : : xn y 2 f0 1g, by bounding the number of variables aecting
processors and memory cells as a function of time. This lower bound remains
valid even if concurrent writes are allowed.
      EXERCISE 21.34
       Sni85] Prove that an EREW PRAM with p processors requires (log n;
      logp) steps to SEARCH AN ORDERED LIST of length n.
     EXERCISE 21.35
      Sni85] Prove that an EREW PRAM can SEARCH AN ORDERED
     LIST of length n in O(log n ; log p) steps using p processors, provided
     p copies of y are given as part of the input.
     EXERCISE 21.36
```

### Strana 63

```text
42     Chapter 21.    The Complexity of Computation on the PRAM

      Sni85] Prove that an EREW
                            p     PRAM can SEARCH AN ORDERED
     LIST of length n in O( log n) steps using n processors and memory
     cells.
      Even with an arbitrarily large number of processors, the upper bound
in Exercise 21.36 cannot be improved. This is a consequence of the limited
ability of the EREW PRAM to access the input variable y.
     THEOREM 21.36           Sni85]
                                     p
     An EREW PRAM requires ( log n) steps to SEARCH AN ORDERED
     list of length n, provided the domain size, r, is suciently large.

      The idea of the proof is to show that any algorithm has a simple structure
for a large subset of the inputs. Then a lower bound is obtained assuming
this simple structure.
      Two inputs x x 2 Dn are order equivalent if, for all i j 2 f1 : : : ng,
                      0




                          xi < xj if and only if xi < xj :
                                                  0     0




A function f : Dn ! R depends only on the relative values of its variables if
f(x) = f(x ) for all order equivalent inputs x x 2 Dn . The address functions
           0                                       0


of a PRAM algorithm are the functions of the input that describe where in
shared memory each processor reads from and writes to at each step in the
computation. A PRAM algorithm depends only on the relative values of its
variables if its address functions depend only on the relative values of their
variables.

     LEMMA 21.37
     Consider any EREW PRAM algorithm to SEARCH AN ORDERED
     LIST. If the domain size r is suciently large (as a function of the
     number of processors, memory cells, and time steps), then there is a
     large subset S  f1 : : : rg such that the EREW PRAM algorithm de-
     pends only on the relative values of its variables when restricted to inputs
     x1 : : : xn y 2 S .
This lemma can be proved by applying the following result from Ramsey
theory to each of the address functions.
```

### Strana 64

```text
                                            21.4 Lower Bound Techniques     43
     THEOREM 21.38 GRS80]
     Given a function f : Dn ! R, where jDj is suciently large in terms
     of n, jRj, and s, there is a subset S  D, with jS j  s, such that f jS n
     depends only on the relative values of its variables.
Finally, any EREW PRAM algorithm to SEARCH AN ORDERED LIST that
depends only on the relative values of its variables can be shown to require
( log n) steps, using arguments similar to those needed for Exercise 21.34
 Sni85].
      Furthermore, if the EREW PRAM algorithm stores at most a con-
stant number of input values in each shared memory cell, then it requires
  (log n= loglog n) steps to SEARCH AN ORDERED LIST. If, in addition,
each processor only stores a constant number of input values in its local mem-
ory, (log n) steps are necessary.
      These results demonstrate that concurrent read can be more powerful
than exclusive read (because a CREW PRAM with n processors can SEARCH
AN ORDERED LIST of n numbers in O(1) steps), although not necessarily
for problems with complete domains. However, the lower bounds in Exercise
21.34 and Theorem 21.36 also apply to any problem that has SEARCH AN
ORDERED LIST as a special case. Unfortunately, the natural extension to a
complete domain, the problem of searching an unordered list, is also dicult
for a CREW PRAM.
      EXERCISE 21.37
      Prove that a CREW PRAM requires (log n) time to search an un-
      ordered list x1  : : : xn for an element y.
      It is possible to construct a problem with complete domain that has
SEARCH AN ORDERED LIST as a special case and can be computed sub-
stantially more quickly by a CREW PRAM than by an EREW PRAM GNR89].
A comparison tree is a binary decision tree in which each internal node is la-
belled by a comparison between two input variables instead of by a single input
variable. The two children of an internal node correspond to the outcomes <
and  of the comparison. As in a decision tree, computation begins at the
root and the output is the label of the leaf that is reached. Consider the fol-
lowing comparison tree with n internal nodes and depth dlog2 ne, an example
of which is illustrated in Figure 21.3. At the ith internal node (encountered in
an inorder traversal), the input variables y and xi are compared. The leaves
are labelled sequentially from left to right with the numbers 0 1 : : : n. The
```

### Strana 65

```text
44      Chapter 21.          The Complexity of Computation on the PRAM

problem is to determine the output of this comparison tree, given the input
x1  : : : xn y 2 f1 : : : rg. When the input variables x1 : : : xn are restricted
to be in sorted order, this problem is equivalent to SEARCH AN ORDERED
LIST.
                                               y : x4
                                      <                    

                    y : x2                                             y : x6
           <                                                  <                 
       y : x1                     y : x3                 y : x5                  y : x7
  <                         <                     <                      <             
   0            1             2            3         4             5         6            7

FIGURE 21.3
The comparison tree problem, for n = 7.

       EXERCISE 21.38
        GNR89] Prove that on a CREW PRAM, the comparison problem can be
       solved in O(log log n) steps, using n processors, and requires (log log n)
       steps, regardless of the number of processors.
       EXERCISE 21.39
       Prove that an exclusive
                        p      read PRAM with an innite number of proces-
       sors requires ( logp= loglog p) steps to simulate a general step of a
       concurrent read PRAM with p processors, when the input domain size
       is suciently large.
      EXERCISE 21.40
       GNR89] Construct a function with domain f0 1gn and range f0 1g
      that can be solved in O(loglog n) steps on a CREW PRAM using n
      processors, but requires (log n ; log p) steps to be computed by an
      EREW PRAM with p processors.
      Lower bounds for a number of other problems have been obtained us-
ing the Ramsey theory technique. The ELEMENT DISTINCTNESS problem
```

### Strana 66

```text
                                           21.4 Lower Bound Techniques     45
was studied by Fich, Meyer auf der Heide, and Wigderson FMW87]. They
showed that COMMON with n processors and an innite amount of shared
memory requires (log log logn) steps to solve this problem for a domain
of size 2 (n log n) . Ragde, Steiger, Szemeredi,
                                        p        and Wigderson RSSW88] im-
proved the lower bound on time to ( log n) and Boppana Bop89] improved
it further to (log n= loglog n), matching the upper bound. (See Theorem
21.7 and Exercise 21.13.) Both results require substantially larger domains.
Recently, Edmonds Edm91] was able to obtain an (log n= log log n) lower
bound using a domain only doubly exponential in n. Boppana Bop89] and
Edmonds Edm91] also proved that PRIORITY with n processors requires
(log n= loglog n) steps to solve ELEMENT DISTINCTNESS on these do-
mains, when the amount of shared memory does not increase as a function
of the domain size r. On PRIORITY with n processors (or even n(logn)O(1)
processors) and innite memory, Fich, Meyer auf der Heide, and Wigder-
son MW87] showed that nding the MAXIMUM of n elements requires
(log logn) steps (matching Shiloach and Vishkin's upper bound SV81]) and
Meyer auf der Heide pand Wigderson MW87] showed that SORTING a list of
length n requires ( log n) steps. Schieber and Vishkin SV90] used similar
ideas to obtain a tight (log log n) lower bound on the number of steps needed
by PRIORITY with n(log n)0(1) processors and innite memory to merge two
sorted lists of length n or nd the nearest neighbour of each vertex in an
n-vertex convex polygon.
      A serious limitation of these lower bounds, and one that is inherent in
the use of Ramsey theory, is that they are only applicable when the size of
the problem domain is very large. For example, provided the domain size
r 2 O(m), ARBITRARY can solve ELEMENT DISTINCTNESS in O(1)
steps using n processors and m shared memory cells. (See Exercise 21.13.)
Berkman and Vishkin BV89] showed that two sorted lists of length n con-
taining numbers in the range f1 : : : rg can be merged on a CREW PRAM
in O(loglog logr) steps using n= loglog log r processors.
     EXERCISE 21.41
      FRW88a, EG88] Prove that the MAXIMUM of n elements with values
     in the range f1 : : : nO(1)g can be found on COMMON using n proces-
     sors and memory cells and O(1) time.
     At present, it is unknown whether an EREW PRAM can compute every
Boolean function as quickly as a CREW PRAM can. However, the following
Boolean function require substantially more time to compute on an EROW
```

### Strana 67

```text
46     Chapter 21.    The Complexity of Computation on the PRAM

PRAM than on a CROW PRAM FW90].
      BOOLEAN DECISION TREE EVALUATION
      Given the values of 2m Boolean variables x0 : : : x2m 1 and (the
                                                                    ;

      binary encoding of) a complete decision tree of height h, in which
      each internal node is labelled by one of these 2m variables and the
      leaves are alternately labelled 0 and 1, determine the label of the
      leaf that is reached. The size of the input is n = 2m + m(2h ; 1).
      For example, when m = 2 and h = 3, the rst four bits of the input
111000100111100110 represent the values x0 = 1, x1 = 1, x2 = 1, and x3 = 0.
The remaining bits represent the indices of the labels of the interior nodes
of the decision tree illustrated in Figure 21.4, when these nodes are arranged
according to the inorder traversal of the tree.
                                         x3


                      x2                                   x1

             x0                 x1                x2                    x2

        0         1        0         1        0        1        0            1

FIGURE 21.4
The Boolean decision tree of height 3 represented by the encoding 00100111100110.


     THEOREM 21.39             FW90]
     For an appropriate choice of h and m, a CROW PRAM can solve the
     BOOLEAN DECISION TREE EVALUATION problem in O(log logn)
     steps, but anyp (probabilistic) EROW PRAM that computes it requires
     (expected) ( log n) steps.

      From Theorem 21.22, it follows that a CROW PRAM can solve the
BOOLEAN DECISION TREE EVALUATION problem in time O(log m +
log h). To prove the lower bound, it is sucient to consider the behaviour of
```

### Strana 68

```text
                                             21.4 Lower Bound Techniques        47

an EROW PRAM algorithm on a randomly chosen input from f0 1gn. After
each step of the EROW PRAM computation, a longer initial segment of the
root to leaf path is revealed. It is very unlikely that any processor knows both
the value of a variable that has not been revealed and (any bit of) the label of
a node in the subtree rooted at the end of this initial segment. In particular,
for suciently short computations, if a processor knows anything about which
variable labels the parent of the leaf that is reached, then it is unlikely to know
anything about the value of that variable. It is conjectured that an EREW
PRAM requires (logn) (1) steps to solve the BOOLEAN DECISION TREE
EVALUATION problem, for appropriate h and m.

                         21.4.3 Small Memory
      There are certain techniques that are particularly useful for proving
lower bounds on a PRAM with a small amount of shared memory. When a
PRAM has only one shared memory cell, we may assume that all processors
read the shared memory cell at every step of the computation. The sequence of
contents of the m shared memory cells is called the history of the computation.
Then a processor's knowledge can be expressed as a function of the history
and any input values initially located in its local memory. A lower bound
of (t=m) steps on a PRAM using m shared memory cells can be obtained
from a lower bound of t steps on a PRAM using one shared memory cell by
applying the result of Exercise 21.3.
      The following information theoretic lower bound is obtained by consid-
ering the partition of the set of all possible inputs into blocks that cause the
shared memory to have exactly the same history up to a given point in time.
Since two processors may not attempt to write dierent values in the same
memory cell at the same time, it must be possible to infer some \mutual
exclusion" information from the history. This mutual exclusion information
takes time to set up and is not reusable, so the partition cannot become too
ne too quickly.
      THEOREM 21.40 FRW88a]
      (Probabilistic) COMMON with n processors and m shared memory cells
      that computes a surjective function f : f0 1gn ! R requires (expected
      time) ((log jRj)=m) steps for some input.

     EXERCISE 21.42
```

### Strana 69

```text
48     Chapter 21.   The Complexity of Computation on the PRAM

       FRW88a] Prove that COMMON with p processors and m shared mem-
      ory cells requires (log(p=m)) steps to simulate one step of ARBI-
      TRARY or PRIORITY with p processors and m memory cells.
      Adversary arguments are also useful for proving lower bounds with small
amounts of shared memory. As the computation proceeds, the adversary xes
the history by xing the values of some of the input variables and, in the case
of ARBITRARY, the outcomes of write conicts. Unless the computation is
suciently long, this information is insucient to determine the answer.
     THEOREM 21.41          FRW88a]
     ARBITRARY with p processors and m shared memory cells requires
     (log(p=m)) steps to simulate one step of PRIORITY with p processors
     and m memory cells.
     PROOF
     It suces to prove the lower bound for the following restricted version
     of the LEFTMOST WRITERS problem. The p processors are divided
     into m groups of approximately equal size and, for i 2 f1 : : : mg, each
     processor in group i must have value 0 or i. Consider any ARBITRARY
     algorithm that solves this problem.
     A processor whose value has not yet been xed by the adversary is said
     to be free. The adversary xes the values of certain processors after each
     step of the computation in a way that allows any free processor to be
     the leftmost writer in its group. This is accomplished by never xing
     the value of a processor to anything but 0 if there is a free processor of
     lower index within the same group. As long as there is at least one free
     processor, the algorithm cannot have terminated.
     Initially, the rightmost processor in each group has its value xed to the
     index of the group. The values of the other processors are free. Once the
     history for the rst t steps has been xed, the action of each processor
     at step t + 1 can be viewed as a function of its value. Based on these
     actions, the adversary xes the contents of each of the m shared memory
     cells at step t + 1, as follows.
     If possible, the adversary xes the contents of a cell by choosing the
     value written at step t + 1 by a processor whose value has already been
     xed. Otherwise, if there is a free processor that writes to the cell at step
     t + 1 when its value is 0, the adversary xes the value of that processor
```

### Strana 70

```text
                                       21.4 Lower Bound Techniques        49
to 0 and xes the contents of the cell by choosing the value written by
that processor.
The remaining unxed cells are only written to by free processors when
their values are nonzero. If possible, the adversary xes the contents of
such a cell by choosing the value written by a processor among the right
half of the free processors in some group. The value of the processor is
set to the index of its group to ensure that the write takes place. The
value of every free processor of higher index within the same group is
xed to 0.
Note that each time the contents of a cell is xed in one of these ways,
the number of possible answers decreases by at most a factor of 2.
Finally, the left half of the free processors in each group have their values
xed to 0, ensuring that no processors write to the remaining unxed
cells. The adversary xes the contents of those cells to be the same as
at step t. This decreases the number of possible answers by a factor of
2m .
Initially, there are ((n=m)m ) possible answers. This is because any
processor in group i can be the leftmost writer to cell i. At each step,
the total number of possible answers decreases by a factor of at most
22m . Thus any algorithm must perform (log(n=m)) steps to determine
the answer in the worst case.

EXERCISE 21.43
 FLRY89] Prove that PRIORITY with an innite number of proces-
sors and m shared memory cells requires (n=m) steps to determine
whether the input x1  : : : xn contains two consecutive variables with
value 1, assuming that the input is initially located in the processors'
local memories.
EXERCISE 21.44
Prove that a CREW PRAM with an innite number of processors and
m shared memory cells requires (n=m) steps to compute the OR of n
input bits that are initially located in the processors' local memories.


                      21.4.4 Reductions
```

### Strana 71

```text
50      Chapter 21.     The Complexity of Computation on the PRAM

        The most frequently used lower bound technique is to nd a problem
for a which a good lower bound is known and reduce it to the problem of
interest. Specically, let f be a problem with n input variables and let g be
a problem with n input variables. Suppose a PRAM can map each instance
                   0


(x1  : : : xn) of f to an instance (y1  : : : yn0 ) of g in t steps and can map the
answer g(y1  : : : yn0 ) to the answer f(x1  : : : xn) in t steps. If the PRAM
                                                             0


requires at least T steps to solve f, then it requires at least T ; t ; t steps0


to solve g. To get a nontrivial lower bound for g, it is important that the
time t + t used to perform the reduction is signicantly less than the lower
           0


bound T for f. For example, the problem of merging two sorted lists of length
n can be reduced in constant time to the problem of triangulating a mono-
tone polygon with (n) vertices by an EREW PRAM using O(n) processors
 BSV88]. Since the former problem requires (loglog n) steps on PRIOR-
ITY with n(log n)O(1) processors (see Section 21.21), it follows that this lower
bound also applies to the latter problem. More generally, if merging two sorted
lists of length n can be reduced to a problem with O(n) inputs on PRIOR-
ITY using o(log log n) steps and n(log n)O(1) processors, then that problem
requires (loglog n) steps on PRIORITY with n(logn)O(1) processors.
        Sometimes it is possible to express each component of g's input as a
function of at most one component of f's input and each component of f's
answer as a function of at most one component of g's answer. Then f can
be reduced to g by a CREW PRAM in constant time using one processor
for each component of g's input and one processor for each component of f's
answer. This type of reduction is called a projection.
        THEOREM 21.42
        The PARITY of n bits can be reduced via a projection to LIST RANK-
        ING in a list of length 3n + 1.
      PROOF
      Consider an instance (x1 : : : xn) of the PARITY problem. Create an
      instance of LIST RANKING with nodes 1 : : : 2n + 1 arranged in order
      starting at 1. If xi = 0, then node 2n + i + 1 is placed between nodes
      n + i and n + i + 1 and if xi = 1, then it is placed between nodes i and
      i + 1. In particular, the distance from node n + 1 to the end of the list
      is the number of input variables with value 1 plus twice the number of
      input variables with value 0. Hence, the least signicant bit of the rank
      of node n + 1 is the PARITY of x1 : : : xn.
```

### Strana 72

```text
                                            21.4 Lower Bound Techniques       51
      From Theorems 21.23 and 21.33, it follows that LIST RANKING re-
quires (log n) steps on a CREW PRAM using any number of processors
and (log n= loglog n) steps on PRIORITY using a polynomial number of
processors.
      EXERCISE 21.45
       FSS84] Prove that there is a projection mapping the PARITY of n bits
      to the MULTIPLICATION of two n bit numbers.
Many other examples of projections appear in SV85] and CSV84].
      An analogue of Turing reducibility is also useful for proving lower bounds.
Let f be a problem with n inputs and let fgig be a family of problems where
gi has i inputs. Suppose there is a PRAM that can solve f using t time steps
and p processors, given access to an oracle that solves any instance of gi for
i  s(n). If the PRAM can solve gi using t (i) time steps and p (i) proces-
                                                 0                  0


sors, then it can solve f using at most t  t (s(n)) time steps and p  p (s(n))
                                             0                            0


processors. Furthermore, if no input to an oracle computation is a function of
an output of another oracle computation, then the PRAM can solve f using
only t + t (s(n)) time steps.
         0


      A special case of such a reduction is one that can be performed by a
constant depth, polynomial size unbounded fan-in Boolean circuit with gates
that compute any bit of the output of a problem in fgig. This reduction
can also be performed by COMMON (and, hence, PRIORITY) in constant
time using a polynomial number of processors. (See Theorem 21.10.) Con-
stant depth, polynomial size reductions from determining the PARITY of
n bits to ADDING, SORTING, and determining the MAJORITY of O(n)
bits and computing the TRANSITIVE CLOSURE of an n + 2 node graph
 FSS84, CSV84] imply (log n= loglog n) lower bounds for these problems on
PRIORITY with n0(1) processors. Other examples of constant depth, poly-
nomial size reductions appear in FSS84, CSV84, ACG+ 88].
      EXERCISE 21.46
       CSV84] Prove that SORTING n n-bit integers is reducible to determin-
      ing (the bits of) the binary representation of the sum of n bits and vice
      versa.

                          Acknowledgements
I am grateful to Je Edmonds, David Neto, Naomi Nishimura, Prabhakar
Ragde, and Jeannine St. Jacques for carefully reading various drafts of this
```

### Strana 73

```text
52    Chapter 21.   The Complexity of Computation on the PRAM

chapter and making valuable comments. Preparation of this chapter was sup-
ported by the Natural Sciences and Engineering Research Council of Canada
(grant A9176) and the Information Technology Research Centre of Ontario.
```

### Strana 74

```text
Bibliography
ACF90]    S. Akl, M. Cosnard, and A. Ferreira. Data-movement-intensive
          problems: Two folk theorems in parallel computation revisited.
          Technical Report 90-18, Ecole Normale Sup#erieure de Lyon, June
          1990.
ACG+ 88] A. Aggarwal, B. Chazelle, L. Guibas, C. O'Dunlaing, and C. Yap.
         Parallel computational geometry. Algorithmica, 3:293{327, 1988.
AHMP87] H. Alt, T. Hagerup, K. Mehlhorn, and F. Preparata. Deterministic
        simulation of idealized parallel computers on more realistic ones.
        SIAM Journal on Computing, 16(5):808{835, October 1987.
AHU74] A. Aho, J. Hopcroft, and J. Ullman. The Design and Analysis of
       Computer Algorithms. Addison-Wesley, 1974.
Bea87]    P. Beame. Lower Bounds in Parallel Machine Computation. PhD
          thesis, University of Toronto, 1987. Department of Computer
          Science Tech. Report 198/87.
Bea88]    P. Beame. Limits on the power of concurrent-write parallel ma-
          chines. Information and Computation, 76(1):13{28, 1988.
Bel88]    S. Bellantoni. Parallel RAMs with bounded memory wordsize.
          Master's thesis, University of Toronto, 1988.
Bel91]    S. Bellantoni. Parallel RAMs with bounded memory wordsize.
          Information and Computation, 91(2):259{273, April 1991.
BH89]     P. Beame and J. Hastad. Optimal bounds for decision problems
          on the CRCW PRAM. Journal of the ACM, 36(3):643{670, 1989.
                                   53
```

### Strana 75

```text
54      Chapter 21. The Complexity of Computation on the PRAM

BI87]   M. Blum and R. Impagliazzo. Generic oracles and oracle classes.
        In FOCS, pages 118{126, 1987.
Bop89] R. Boppana. Optimal separations between concurrent-write par-
        allel machines. In STOC, pages 320{326, 1989.
Bor77] A. Borodin. On relating time and space to size and depth. SIAM
        Journal on Computing, 6(4):733{744, December 1977.
BSV88] O. Berkman, B. Schieber, and U. Vishkin. Some doubly loga-
        rithmic optimal parallel algorithms based on nding all nearest
        smaller values. Technical Report UMIACS-TR-88-79, submitted
        to J.Algorithms, University of Maryland, 1988.
BSVW86] S. Bublitz, U. Sch&urfeld, B. Voigt, and I. Wegener. Properties
        of complexity measures for PRAMs and WRAMs. Theoretical
        Computer Science, 48:53{73, 1986.
BV89] O. Berkman and U. Vishkin. Recursive *-tree parallel data struc-
        ture. In FOCS, pages 196{202, 1989.
CDHR88] B. Chelbus, K. Diks, T. Hagerup, and T. Radzik. Ecient sim-
        ulations between CRCW PRAMs. In 13th MFCS, Lecture Notes
        in Computer Science 324, pages 230{239. Springer-Verlag, 1988.
CDR86] S. Cook, C. Dwork, and R. Reischuk. Upper and lower bounds
        for parallel random access machines without simultaneous writes.
        SIAM Journal on Computing, 15:87{97, 1986.
Cha91] S. Chaudhuri. Tight bounds for the chaining problem. In Proceed-
        ings of the Symposium on Parallel Algorithms and Architectures,
        pages 62{70, 1991.
CR73] S. Cook and R. Reckow. Time bounded random access machines.
        Journal of Computer and System Sciences, 7(4):354{375, 1973.
CSV84] A. Chandra, L. Stockmeyer, and U. Vishkin. Constant depth
        reducibility. SIAM Journal on Computing, 13:423{439, 1984.
DKR90] M. Dietzfelbinger, M. Kutylowski, and R. Reischuk. Exact time
        bounds for computing boolean functions on PRAMs without si-
        multaneous writes. In Proceedings of the Symposium on Parallel
        Algorithms and Architectures, pages 125{137, July 1990.
```

### Strana 76

```text
                                         21.4 Lower Bound Techniques     55
DR86]     P. Dymond and W.L. Ruzzo. Parallel RAMs with owned global
          memory and deterministic context-free language recognition. In
          ICALP, pages 95{104, July 1986.
Eck79]    D. Eckstein. Simultaneous memory access. Technical Report TR-
          79-6, Iowa State University, 1979.
Edm91]    J.A. Edmonds. Lower bounds with smaller domain size on concur-
          rent write parallel machines. In Structures in Complexity Theory,
          pages 322{333, July 1991.
EG88]     D. Eppstein and Z. Galil. Parallel algorithmic techniques for com-
          binatorial computing. Ann. Rev. Comput. Sci., 3:233{283, 1988.
FLRY89] F. Fich, M. Li, P. Ragde, and Y. Yesha. Lower bounds for parallel
        random access machines with read only memory. Information and
        Computation, 83(2):234{244, November 1989.
FMW87] F. Fich, F. Meyer auf der Heide, and A. Wigderson. Lower bounds
       for parallel random access machines with unbounded shared mem-
       ory. In F. Preparata, editor, Advances in Computing Research,
       volume 4, pages 1{15. JAI Press Inc., 1987.
FR90]     F. Fich and V. Ramachandran. Lower bounds for parallel compu-
          tation on linked structures. In Proceedings of the Symposium on
          Parallel Algorithms and Architectures, July 1990.
FRW88a] F. Fich, P. Ragde, and A. Wigderson. Relations between
        concurrent-write models of parallel computation. SIAM Journal
        on Computing, 17:606{627, 1988. A preliminary version appeared
        in the Proceedings of the Third ACM Symposium on Principles
        of Distributed Computing, 1984, pages 179-189.
FRW88b] F. Fich, P. Ragde, and A. Wigderson. Simulations among between
        concurrent-write PRAMs. Algorithmica, 3:43{51, 1988.
FSS84]    M. Furst, J.B. Saxe, and M. Sipser. Parity, circuits, and the
          polynomial-time hierarchy. Math. Sys. Th., 17:13{27, 1984.
FW78]     S. Fortune and J. Wyllie. Parallelism in random access machines.
          In STOC, pages 114{118, 1978.
```

### Strana 77

```text
56    Chapter 21. The Complexity of Computation on the PRAM

FW90]  F. Fich and A. Wigderson. Towards understanding exclusive read.
       SIAM Journal on Computing, 19(4):718{727, August 1990.
GNR89] E. Gafni, J. Naor, and P. Ragde. On separating the EREW and
       CROW models. Theoretical Computer Science, 68(3):343{346,
       1989.
Gol82] L. Goldschlager. A unied approach to models of synchronous
       parallel machines. Journal of the ACM, 29:1073{1086, 1982.
Goo89] M. Goodrich. Intersecting line segments in parallel with an
       output-sensitive number of processors. In Proceedings of the Sym-
       posium on Parallel Algorithms and Architectures, pages 127{137,
       June 1989.
GR90] V. Grolmusz and P. Ragde. Incomparability in parallel computa-
       tion. Discrete Applied Mathematics, 29(1):63{78, November 1990.
GRS80] R.L. Graham, B.L. Rothschild, and J.H. Spencer. Ramsey Theory.
       John Wiley, New York, 1980.
Has87] J. Hastad. Computational Limitations for Small Depth Circuits.
       MIT Press, Cambridge, Mass., 1987.
HH86] J. Hartmanis and L. Hemachandra. Complexity classes without
       machines: On complete sets for UP. In ICALP, pages 123{135,
       July 1986.
HKP]   J. Hoover, M. Klawe, and N. Pippenger. Bounding Fan-Out in
       Logical Networks. Journal of the ACM, 31(1):13{18, 1984.
HP89] S. Hornick and F. Preparata. Deterministic P-RAM simulation
       with constant redundancy. In Proceedings of the Symposium on
       Parallel Algorithms and Architectures, pages 103{109, June 1989.
HR90] T. Hagerup and T. Radzik. Every robust CRCW PRAM can
       eciently simulate a PRIORITY PRAM. In Proceedings of the
       Symposium on Parallel Algorithms and Architectures, pages 117{
       124, 1990.
KR90] R. Karp and V. Ramachandran. A survey of parallel algorithms for
       shared-memory machines. In Handbook of Theoretical Computer
       Science, volume A. MIT Press, 1990.
```

### Strana 78

```text
                                        21.4 Lower Bound Techniques     57
KRS90]   C. Kruskal, L. Rudolph, and M. Snir. A complexity theory of e-
         cient parallel algorithms. Theoretical Computer Science, 71(1):95{
         132, 1990.
Kuc82]   L. Kucera. Parallel computation and conicts in memory access.
         Information Processing Letters, 14(2):93{96, 1982.
LPV81]   G. Lev, N. Pippenger, and L.G. Valiant. A fast parallel algorithm
         for routing in permutation networks. IEEE Trans. Comput., C-
         30:93{100, 1981.
LY86]    M. Li and Y. Yesha. New lower bounds for parallel computation.
         In STOC, pages 177{187, 1986.
LY87]    M. Li and Y. Yesha. The probabilistic and deterministic parallel
         complexity of symmetric functions. In ICALP, pages 326{335,
         1987.
LY89]    M. Li and Y. Yesha. New lower bounds for parallel computation.
         Journal of the ACM, 36(3):671{680, 1989.
MR84]    F. Meyer auf der Heide and R. Reischuk. Limits to speed up par-
         allel machines by large hardware and unbounded communication.
         In FOCS, volume 25, pages 56{64, 1984.
MV84]    K. Mehlhorn and U. Vishkin. Randomized and deterministic sim-
         ulation of prams by parallel machines with restricted granularity
         of parallel memories. Acta Informatica, 21:339{374, 1984.
MW87]    F. Meyer auf der Heide and A. Wigderson. The complexity of par-
         allel sorting. SIAM Journal on Computing, 16(1):100{107, Febru-
         ary 1987.
Nis89]   N. Nisan. CREW PRAMS and decision trees. In STOC, pages
         327{335, 1989.
NS81]    D. Nassimi and S. Sahni. Data broadcasting in SIMD computers.
         IEEE Trans. Comput., C-30:101{107, 1981.
NS92]    N. Nisan and M. Szegedy. On the degree of boolean functions as
         real polynomials. In STOC, 1992.
```

### Strana 79

```text
58       Chapter 21. The Complexity of Computation on the PRAM

PY91]        I. Parberry and P. Yan. Improved upper and lower time bounds
             for parallel random access machines without simultaneous writes.
             SIAM Journal on Computing, 20:88{99, 1991.
Raga]        P. Ragde. unpublished manuscript.
Ragb]        P. Ragde. Processor-time tradeos in PRAM simulations. Journal
             of Computer and System Sciences, 44, 1992.
Ran87]       A. Ranade. How to emulate shared memory. In FOCS, pages
             185{194, 1987.
RSSW88] P. Ragde, W. Steiger, E. Szemeredi, and A. Wigderson. The
        parallel complexity of element distinctness is !((log n)1=2). SIAM
        J. Dis. Math., 1:399{410, 1988.
Rub]         D. Rubinstein. personal communication.
Ruz]         W.L. Ruzzo. personal communication, cited in BH89, Bea87].
Sch80]       J. T. Schwartz. Ultracomputers. ACM Trans. Programming Lang.
             Systems, 2:484{521, 1980.
Sim82]       H. Simon. A tight !(log logn) bound on the time for parallel
             RAM's to compute nondegenerate boolean functions. Information
             and Control, 55:102{107, 1982.
Smi90]       Burton Smith. The tera computer system. In Proceedings of
             the ACM International Conference on Supercomputing, pages 1{7,
             1990.
Smo87]       R. Smolensky. Algebraic methods in the theory of lower bounds
             for boolean circuit complexity. In STOC, pages 77{82, 1987.
Sni]         M. Snir. private communication.
Sni85]       M. Snir. On parallel searching. SIAM Journal on Computing,
             14(3):688{708, August 1985.
SV81]        Y. Shiloach and U. Vishkin. Finding the maximum, merging, and
             sorting in a parallel computation model. J. Algorithms, 2:88{102,
             1981.
```

### Strana 80

```text
                                        21.4 Lower Bound Techniques      59
SV84]    L. Stockmeyer and U. Vishkin. Simulation of parallel random
         access machines by circuits. SIAM Journal on Computing, 13:404{
         422, 1984.
SV85]    S. Skyum and L. Valiant. A complexity theory based on boolean
         algebra. Journal of the ACM, 32:484{502, 1985.
SV90]    B. Schieber and U. Vishkin. Finding all nearest neighbors for
         convex polygons in parallel: A new lower bound technique and a
         matching algorithm. Discrete Applied Mathematics, 29(1):97{112,
         November 1990.
Sze89]   G. Szegedy. Algebraic Methods in Lower Bounds for Computa-
         tional Models with Limited Communication. PhD thesis, Univer-
         sity of Chicago, 1989.
Tar88]   G. Tardos. Query complexity, or why is it dicult to separate
         npa \ co ; npa from pa by a random oracle a?, 1988. manuscript.
TLR88]   J. Trahan, M.C. Loui, and V. Ramachandran. Multiplication,
         division, and shift instruction in parallel random access machines.
         In Proc. 22nd Conf. Inf. Sci. Syst., pages 126{130, 1988.
Tra88]   J. Trahan. Instruction Sets for Parallel Random Access Machines.
         PhD thesis, University of Illinois, Urbana-Champaign, 1988.
UW87]    E. Upfal and A. Wigderson. How to share memory in a distributed
         system. Journal of the ACM, 34:116{127, 1987.
Vis83]   U. Vishkin. Implementation of simultaneous memory access in
         models that forbid it. J. Alg., 4:45{50, 1983.
VW85]    U. Vishkin and A. Wigderson. Trade-os between depth and
         width in parallel computation. SIAM Journal on Computing,
         14:303{314, 1985. FOCS 1983, pages 146-153.
WZ88]    I. Wegener and L. Z#adori. A note on the relations between crit-
         ical and sensitive complexity. Technical Report 256, Universit&at
         Dortmund, 1988.
```

### Strana 81

```text
               1

     Prefix Sums
and Their Applications
       Guy E. Blelloch
     School of Computer Science
     Carnegie Mellon University
     Pittsburgh, PA 15213-3890




                35
```

### Strana 82

```text
36     Chapter 1.        Prefix Sums and Their Applications


                                         1.1
                                    Introduction
      Experienced algorithm designers rely heavily on a set of building blocks
and on the tools needed to put the blocks together into an algorithm. The
understanding of these basic blocks and tools is therefore critical to the un-
derstanding of algorithms. Many of the blocks and tools needed for parallel
algorithms extend from sequential algorithms, such as dynamic-programming
and divide-and-conquer, but others are new.
      This chapter introduces one of the simplest and most useful building
blocks for parallel algorithms: the all-prefix-sums operation. The chapter de-
fines the operation, shows how to implement it on a PRAM and illustrates
many applications of the operation. In addition to being a useful building
block, the all-prefix-sums operation is a good example of a computation that
seems inherently sequential, but for which there is an efficient parallel algo-
rithm. The operation is defined as follows:
     DEFINITION
     The all-prefix-sums operation takes a binary associative operator ⊕, and
     an ordered set of n elements

                                          [a0 , a1 , ..., an−1 ],

     and returns the ordered set

                          [a0 , (a0 ⊕ a1 ), ..., (a0 ⊕ a1 ⊕ ... ⊕ an−1 )].


For example, if ⊕ is addition, then the all-prefix-sums operation on the ordered
set

                          [3    1     7      0     4     1     6         3],

would return

                    [3      4    11       11     14      16         22     25].

     The uses of the all-prefix-sums operation are extensive. Here is a list of
some of them:

      1. To lexically compare strings of characters. For example, to deter-
         mine that "strategy" should appear before "stratification" in
         a dictionary (see Problem 2).
```

### Strana 83

```text
                                                        1.1 Introduction    37


      2. To add multi precision numbers. These are numbers that cannot
         be represented in a single machine word (see Problem 3).
      3. To evaluate polynomials (see Problem 6).
      4. To solve recurrences. For example, to solve the recurrences
         xi = ai xi−1 + bi xi−2 and xi = ai + bi /xi−1 (see Section 1.4).
      5. To implement radix sort (see Section 1.3).
      6. To implement quicksort (see Section 1).
      7. To solve tridiagonal linear systems (see Problem 12).
      8. To delete marked elements from an array (see Section 1.3).
      9. To dynamically allocate processors (see Section 1.6).
     10. To perform lexical analysis. For example, to parse a program into
         tokens.
     11. To search for regular expressions. For example, to implement the
         UNIX grep program.
     12. To implement some tree operations. For example, to find the depth
         of every vertex in a tree (see Chapter 3).
     13. To label components in two dimensional images.


       In fact, all-prefix-sums operations using addition, minimum and max-
imum are so useful in practice that they have been included as primitive
instructions in some machines. Researchers have also suggested that a sub-
class of the all-prefix-sums operation be added to the PRAM model as a “unit
time” primitive because of their efficient hardware implementation.
       Before describing the implementation we must consider how the def-
inition of the all-prefix-sums operation relates to the PRAM model. The
definition states that the operation takes an ordered set, but does not specify
how the ordered set is laid out in memory. One way to lay out the elements
is in contiguous locations of a vector (a one dimensional array). Another way
is to use a linked-list with pointers from each element to the next. It turns
out that both forms of the operation have uses. In the examples listed above,
the component labeling and some of the tree operations require the linked-list
version, while the other examples can use the vector version.
       Sequentially, both versions are easy to compute (see Figure 1.1). The
vector version steps down the vector, adding each element into a sum and
writing the sum back, while the linked-list version follows the pointers while
keeping the running sum and writing it back. The algorithms in Figure 1.1 for
both versions are inherently sequential: to calculate a value at any step, the
result of the previous step is needed. The algorithms therefore require O(n)
time. To execute the all-prefix-sums operation in parallel, the algorithms must
```

### Strana 84

```text
38      Chapter 1.    Prefix Sums and Their Applications


     proc all-prefix-sums(Out, In)         proc all-prefix-sums(Out, In)
       i ← 0                                 i ← 0
       sum ← In[0]                           sum ← In[0].value
       Out[0] ← sum                          Out[0] ← sum
       while (i < length)                    while (In[i].pointer 6= EOL)
         i ← i + 1                             i ← In[i].pointer
         sum ← sum + In[i]                     sum ← sum + In[i].value
         Out[i] ← sum                          Out[i] ← sum

              Vector Version                                 List Version


FIGURE 1.1
Sequential algorithms for calculating the all-prefix-sums operation with oper-
ator + on a vector and on a linked-list. In the list version, each element of In
consists of two fields: a value (.value), and a pointer to the next position in
the list (.pointer). EOL means the end-of-list pointer.


be changed significantly.
     The remainder of this chapter is concerned with the vector all-prefix-
sums operation. We will henceforth use the term scan for this operation.1

       DEFINITION
       The scan operation is a vector all-prefix-sums operation.

Chapters 2, 3 and 4 discuss uses of the linked-list all-prefix-sums operation
and derive an optimal deterministic algorithm for the problem on the PRAM.
      Sometimes it is useful for each element of the result vector to contain
the sum of all the previous elements, but not the element itself. We call such
an operation, a prescan.

       DEFINITION
       The prescan operation takes a binary associative operator ⊕ with identity
       I, and a vector of n elements

                                   [a0 , a1 , ..., an−1 ],
1 The term scan comes from the computer language APL.
```

### Strana 85

```text
                                                           1.2 Implementation   39


     and returns the vector

                    [I, a0 , (a0 ⊕ a1 ), ..., (a0 ⊕ a1 ⊕ ... ⊕ an−2 )].

A prescan can be generated from a scan by shifting the vector right by one and
inserting the identity. Similarly, the scan can be generated from the prescan
by shifting left, and inserting at the end the sum of the last element of the
prescan and the last element of the original vector.



                                1.2
                           Implementation
      This section describes an algorithm for calculating the scan operation in
parallel. For p processors and a vector of length n on an EREW PRAM, the
algorithm has a time complexity of O(n/p + lg p). The algorithm is simple
and well suited for direct implementation in hardware. Chapter 4 shows
how the time of the scan operation with certain operators can be reduced to
O(n/p + lg p/ lg lg p) on a CREW PRAM.
      Before describing the scan operation, we consider a simpler problem,
that of generating only the final element of the scan. We call this the reduce
operation.
     DEFINITION
     The reduce operation takes a binary associative operator ⊕ with identity
     i, and an ordered set [a0 , a1 , ..., an−1 ] of n elements, and returns the
     value a0 ⊕ a1 ⊕ ... ⊕ an−1 .

Again we consider only the case where the ordered set is kept in a vector.
A balanced binary tree can be used to implement the reduce operation by
laying the tree over the values, and using ⊕ to sum pairs at each vertex (see
Figure 1.2a). The correctness of the result relies on ⊕ being associative. The
operator, however, does not need to be commutative since the order of the
operands is maintained. On an EREW PRAM, each level of the tree can be
executed in parallel, so the implementation can step from the leaves to the
root of the tree (see Figure 1.2b); we call this an up-sweep. Since the tree is
of depth ⌈lg n⌉, and one processor is needed for every pair of elements, the
algorithm requires O(lg n) time and n/2 processors.
      If we assume a fixed number of processors p, with n > p, then each
processor can sum an n/p section of the vector to generate a processor sum; the
```

### Strana 86

```text
40     Chapter 1.      Prefix Sums and Their Applications




                       (a) Executing a +-reduce on a tree.


            for d from 0 to (lg n) − 1
              in parallel for i from 0 to n − 1 by 2d+1
                a[i + 2d+1 − 1] ← a[i + 2d − 1] + a[i + 2d+1 − 1]

        Step                          Vector in Memory
        0        [ 3        1     7       0     4      1     6       3 ]

        1        [3         4     7      7      4      5     6       9 ]
        2        [3         4     7      11     4      5     6      14 ]
        3        [3         4     7      11     4      5     6      25 ]

                     (b) Executing a +-reduce on a PRAM.


FIGURE 1.2
An example of the reduce operation when ⊕ is integer addition. The boxes
in (b) show the locations that are modified on each step. The length of the
vector is n and must be a power of two. The final result will reside in a[n − 1].


tree technique can then be used to reduce the processor sums (see Figure 1.3).
The time taken to generate the processor sums is ⌈n/p⌉, so the total time
required on an EREW PRAM is:

                    TR (n, p) = ⌈n/p⌉ + ⌈lg p⌉ = O(n/p + lg p).             (1.1)

When n/p ≥ lg p the complexity is O(n/p). This time is an optimal speedup
over the sequential algorithm given in Figure 1.1.
      We now return to the scan operation. We actually show how to imple-
```

### Strana 87

```text
                                                        1.2 Implementation    41


                     in parallel for each processor i
                       sum[i] ← a[(n/p)i]
                       for j from 1 to n/p
                         sum[i] ← sum[i] + a[(n/p)i + j]
                     result ← +-reduce(sum)


          [ |4  7 1}
               {z          0
                           | {z 5 2}      6
                                          | {z 4 8}        1| {z9 5} ]
           processor 0     processor 1    processor 2      processor 3

            Processor Sums        =       [12      7      18      15]
            Total Sum             =       52


FIGURE 1.3
The +-reduce operation with more elements than processors. We assume that
n/p is an integer.


ment the prescan operation; the scan is then determined by shifting the result
and putting the sum at the end. If we look at the tree generated by the reduce
operation, it contains many partial sums over regions of the vector. It turns
out that these partial sums can be used to generate all the prefix sums. This
requires executing another sweep of the tree with one step per level, but this
time starting at the root and going to the leaves (a down-sweep). Initially,
the identity element is inserted at the root of the tree. On each step, each
vertex at the current level passes to its left child its own value, and it passes
to its right child, ⊕ applied to the value from the left child from the up-sweep
and its own value (see Figure 1.4a).
       Let us consider why the down-sweep works. We say that vertex x pre-
cedes vertex y if x appears before y in the preorder traversal of the tree (depth
first, from left to right).

     THEOREM 1.1
     After a complete down-sweep, each vertex of the tree contains the sum
     of all the leaf values that precede it.
     PROOF

     The proof is inductive from the root: we show that if a parent has the
     correct sum, both children must have the correct sum. The root has no
     elements preceding it, so its value is correctly the identity element.
```

### Strana 88

```text
42        Chapter 1.    Prefix Sums and Their Applications




                        (a) Executing a +-prescan on a tree.

      procedure down-sweep(A)
        a[n − 1] ← 0                               % Set the identity
        for d from (lg n) − 1 downto 0
          in parallel for i from 0 to n − 1 by 2d+1
             t ← a[i + 2d − 1]                     % Save in temporary
             a[i + 2d − 1] ← a[i + 2d+1 − 1]       % Set left child
             a[i + 2d+1 − 1] ← t + a[i + 2d+1 − 1] % Set right child

               Step                       Vector in Memory
               0         [ 3    1     7      0       4       1    6      3 ]

     up        1         [3     4     7      7       4       5    6     9 ]
               2         [3     4     7      11      4       5    6    14 ]
               3         [3     4     7      11      4       5    6    25 ]

     clear     4         [3     4     7      11      4       5    6      0 ]

     down      5         [3     4     7      0      4        5    6    11 ]
               6         [3     0     7      4      4        11   6    16 ]
               7         [ 0    3     4      11     11       15   16   22 ]

                       (b) Executing a +-prescan on a PRAM.



FIGURE 1.4
A parallel prescan on a tree using integer addition as the associative operator
⊕, and 0 as the identity.
```

### Strana 89

```text
                                                       1.2 Implementation      43




FIGURE 1.5
Illustration for Theorem 1.1.


     Consider Figure 1.5. The left child of any vertex has exactly the same
     leaves preceding it as the vertex itself (the leaves in region A in the
     figure). This is because the preorder traversal always visits the left child
     of a vertex immediately after the vertex. By the induction hypothesis,
     the parent has the correct sum, so it need only copy this sum to the left
     child.
     The right child of any vertex has two sets of leaves preceding it, the leaves
     preceding the parent (region A), and the leaves at or below the left child
     (region B). Therefore, by adding the parent’s down-sweep value, which is
     correct by the induction hypothesis, and the left-child’s up-sweep value,
     the right-child will contain the sum of all the leaves preceding it.

      Since the leaf values that precede any leaf are the values to the left of
it in the scan order, the values at the leaves are the results of a left-to-right
prescan. To implement the prescan on an EREW PRAM, the partial sums
at each vertex must be kept during the up-sweep so they can be used during
the down-sweep. We must therefore be careful not to overwrite them. In fact,
this was the motivation for putting the sums on the right during the reduce
in Figure 1.2b. Figure 1.4b shows the PRAM code for the down-sweep. Each
step can execute in parallel, so the running time is 2 ⌈lg n⌉.
      If we assume a fixed number of processors p, with n > p, we can use
a similar method to that in the reduce operation to generate an optimal
```

### Strana 90

```text
44     Chapter 1.      Prefix Sums and Their Applications



          [ |4  7 1}
               {z            0| {z5 2}           6| {z4 8}          1| {z9 5} ]
           processor 0       processor 1         processor 2        processor 3

                 Sum            =          [12        7        18        15]
                 +-prescan      =          [0        12        19        37]

       [0
        |   4{z 11}      12
                         |     12
                               {z    17}     19
                                             |     25
                                                   {z    29}         37
                                                                     |     38
                                                                           {z    47}]
        processor 0        processor 1         processor 2             processor 3



FIGURE 1.6
A +-prescan with more elements than processors.


algorithm. Each processor first sums an n/p section of the vector to generate
a processor sum, the tree technique is then used to prescan the processor
sums. The results of the prescan of the processor sums are used as an offset
for each processor to prescan within its n/p section (see Figure 1.6). The time
complexity of the algorithm is:

                   TS (n, p) = 2(⌈n/p⌉ + ⌈lg p⌉) = O(n/p + lg n)                        (1.2)

which is the same order as the reduce operation and is also an optimal speedup
over the sequential version when n/p ≥ lg p.
      This section described how to implement the scan (prescan) operation.
The rest of the chapter discusses its applications.



                                 1.3
                    Line-of-Sight and Radix-Sort
      As an example of the use of a scan operation, consider a simple line-of-
sight problem. The line-of-sight problem is: given a terrain map in the form of
a grid of altitudes and an observation point X on the grid, find which points
are visible along a ray originating at the observation point (see Figure 1.7).
      A point on a ray is visible if and only if no other point between it and the
observation point has a greater vertical angle. To find if any previous point has
a greater angle, the altitude of each point along the ray is placed in a vector
(the altitude vector). These altitudes are then converted to angles and placed
```

### Strana 91

```text
                                         1.3 Line-of-Sight and Radix-Sort    45


 procedure line-of-sight(altitude)
   in parallel for each index i
     angle[i] ← arctan(scale × (altitude[i] - altitude[0])/ i)
   max-previous-angle ← max-prescan(angle)
   in parallel for each index i
     if (angle[i] > max-previous-angle[i])
         result[i] ← "visible"
     else
         result[i] ← not "visible"




FIGURE 1.7
The line-of-sight algorithm for a single ray. The X marks the observation
point. The visible points are shaded. A point on the ray is visible if no
previous point has a greater angle.


in the angle vector (see Figure 1.7). A prescan using the operator maximum
(max-prescan) is then executed on the angle vector, which returns to each point
the maximum previous angle. To test for visibility each point only needs to
compare its angle to the result of the max-prescan. This can be generalized to
finding all visible points on the grid. For n points on a ray, the complexity of
the algorithm is the complexity of the scan, TS (n, p) = O(n/p + lg n) on an
EREW PRAM.
      We now consider another example, a radix sort algorithm. The algorithm
loops over the bits of the keys, starting at the lowest bit, executing a split
```

### Strana 92

```text
46       Chapter 1.   Prefix Sums and Their Applications


               procedure split-radix-sort(A, number-of-bits)
                 for i from 0 to (number-of-bits − 1)
                    A ← split(A, Ahii)

     A                       =     [5    7     3    1      4   2   7     2]
     Ah0i                    =     [1    1     1    1      0   0   1     0]
     A ← split(A, Ah0i)      =     [4    2     2    5      7   3   1     7]
     Ah1i                    =     [0    1     1    0      1   1   0     1]
     A ← split(A, Ah1i)      =     [4    5     1    2      2   7   3     7]
     Ah2i                    =     [1    1     0    0      0   1   0     1]
     A ← split(A, Ah2i)      =     [1    2     2    3      4   5   7     7]


FIGURE 1.8
An example of the split radix sort on a vector containing three bit values. The
Ahni notation signifies extracting the nth bit of each element of the vector A.
The split operation packs elements with a 0 flag to the bottom and with a 1
flag to the top.


operation on each iteration (assume all keys have the same number of bits).
The split operation packs the keys with a 0 in the corresponding bit to the
bottom of a vector, and packs the keys with a 1 in the bit to the top of
the same vector. It maintains the order within both groups. The sort works
because each split operation sorts the keys with respect to the current bit
(0 down, 1 up) and maintains the sorted order of all the lower bits since we
iterate from the bottom bit up. Figure 1.8 shows an example of the sort.
      We now consider how the split operation can be implemented using a
scan. The basic idea is to determine a new index for each element and then
permute the elements to these new indices using an exclusive write. To de-
termine the new indices for elements with a 0 in the bit, we invert the flags
and execute a prescan with integer addition. To determine the new indices of
elements with a 1 in the bit, we execute a +-scan in reverse order (starting at
the top of the vector) and subtract the results from the length of the vector
n. Figure 1.9 shows an example of the split operation along with code to
implement it.
      Since the split operation just requires two scan operations, a few steps
of exclusive memory accesses, and a few parallel arithmetic operations, it has
the same asymptotic complexity as the scan: O(n/p + lg p) on an EREW
```

### Strana 93

```text
                                                          1.4 Recurrence Equations         47


                  procedure split(A, Flags)
                    I-down ← +-prescan(not(Flags))
                    I-up    ← n - +-scan(reverse-order(Flags))
                    in parallel for each index i
                      if (Flags[i])
                         Index[i] ← I-up[i]
                      else
                         Index[i] ← I-down[i]
                    result ← permute(A, Index)

     A                          =     [5       7      3       1   4    2    7        2]
     Flags                      =     [1       1      1       1   0    0    1        0]
     I-down                     =     [0       0      0       0   0    1    2        2 ]
     I-up                       =     [ 3      4      5       6   6    6    7        7]
     Index                      =     [3       4      5       6   0    1    7        2]
     permute(A, Index)          =     [4       2      2       5   7    3    1        7]


FIGURE 1.9
The split operation packs the elements with a 0 in the corresponding flag
position to the bottom of a vector, and packs the elements with a 1 to the
top of the same vector. The permute writes each element of A to the index
specified by the corresponding position in Index.


PRAM.2 If we assume that n keys are each O(lg n) bits long, then the overall
algorithm runs in time:
                     n                  n
                  O(( + lg p) lg n) = O( lg n + lg n lg p).
                     p                  p



                                    1.4
                            Recurrence Equations
      This section shows how various recurrence equations can be solved using
the scan operation. A recurrence is a set of equations of the form

                   xi   = fi (xi−1 , xi−2 , · · · , xi−m ),       m≤i<n               (1.3)
2 On an CREW PRAM we can use the scan described in Chapter 4 to get a time of O(n/p +

lg p/ lg lg p).
```

### Strana 94

```text
48      Chapter 1.      Prefix Sums and Their Applications


along with a set of initial values x0 , · · · , xm−1 .
     The scan operation is the special case of a recurrence of the form
                               
                                 a0                 i=0
                     xi =                                               (1.4)
                                 xi−1 ⊕ ai          0 < i < n,

where ⊕ is any binary associative operator. This section shows how to reduce
a more general class of recurrences to equation (1.4), and therefore how to
use the scan algorithm discussed in Section 1.2 to solve these recurrences in
parallel.

                      1.4.1      First-Order Recurrences
      We initially consider first-order recurrences of the following form
                          
                              b0                   i=0
                  xi =                                                    (1.5)
                              (xi−1 ⊗ ai ) ⊕ bi    0 < i < n,

where the ai ’s and bi ’s are sets of n arbitrary constants (not necessarily scalars)
and ⊕ and ⊗ are arbitrary binary operators that satisfy three restrictions:
      1. ⊕ is associative (i.e. (a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)).
      2. ⊗ is semiassociative (i.e. there exists a binary associative operator
         ⊙ such that (a ⊗ b) ⊗ c = a ⊗ (b ⊙ c)).
      3. ⊗ distributes over ⊕ (i.e. a ⊗ (b ⊕ c) = (a ⊗ b) ⊕ (a ⊗ c)).

The operator ⊙ is called the companion operator of ⊗. If ⊗ is fully associative,
then ⊙ and ⊗ are equivalent.
      We now show how (1.5) can be reduced to (1.4). Consider the set of
pairs
                                 ci = [ai , bi ]                           (1.6)
and define a new binary operator • as follows:

                      ci • cj ≡ [ci,a ⊙ cj,a , (ci,b ⊗ cj,a ) ⊕ cj,b ]                (1.7)

where ci,a and ci,b are the first and second elements of ci , respectively.
      Given the conditions on the operators ⊕ and ⊗, the operator • is asso-
ciative as we show below:

 (ci • cj ) • ck
          =    [ci,a ⊙ cj,a , (ci,b ⊗ cj,a ) ⊕ cj,b ] • ck
          =    [(ci,a ⊙ cj,a ) ⊙ ck,a , (((ci,b ⊗ cj,a ) ⊕ cj,b ) ⊗ ck,a ) ⊕ ck,b ]
```

### Strana 95

```text
                                                          1.4 Recurrence Equations      49


           = [ci,a ⊙ (cj,a ⊙ ck,a ), ((ci,b ⊗ cj,a ) ⊗ ck,a ) ⊕ ((cj,b ⊗ ck,a ) ⊕ ck,b )]
           = [ci,a ⊙ (cj,a ⊙ ck,a ), (ci,b ⊗ (cj,a ⊙ ck,a )) ⊕ ((cj,b ⊗ ck,a ) ⊕ ck,b )]
           = ci • [cj,a ⊙ ck,a , (cj,b ⊗ ck,a ) ⊕ ck,b ]
           = ci • (cj • ck )

        We now define the ordered set si = [yi , xi ], where the yi obey the recur-
rence
                                       
                                            a0           i=0
                           yi      =                                                  (1.8)
                                            yi−1 ⊙ ai    0 < i < n,

and the xi are from (1.5). Using (1.5), (1.6) and (1.8) we obtain:

          s0      =   [y0 , x0 ]
                  =   [a0 , b0 ]
                  =   c0
           si     =   [yi , xi ]                                      0<i<n
                  =   [yi−1 ⊙ ai , (xi−1 ⊗ ai ) ⊕ bi ]
                  =   [yi−1 ⊙ ci,a , (xi−1 ⊗ ci,a ) ⊕ ci,b ]
                  =   [yi−1 , xi−1 ] • ci
                  =   si−1 • ci .

Since • is associative, we have reduced (1.5) to (1.4). The results xi are just
the second values of si (the si,b ). This allows us to use the scan algorithm of
Section 1.2 with operator • to solve any recurrence of the form (1.5) on an
EREW PRAM in time:

                (T⊙ + T⊗ + T⊕ )TS (n, p) = 2(T⊙ + T⊗ + T⊕ )(n/p + lg p)               (1.9)

where T⊙ , T⊗ and T⊕ are the times taken by ⊙, ⊗ and ⊕ (• makes one call to
each). If all that is needed is the final value xn−1 , then we can use a reduce
instead of scan with the operator •, and the running time is:

          (T⊙ + T⊗ + T⊕ )TR (n, p) = (T⊙ + T⊗ + T⊕ )(n/p + lg p)                     (1.10)

which is asymptotically a factor of 2 faster than (1.9).
      Applications of first-order linear recurrences include the simulation of
various time-varying linear systems, the backsubstitution phase of tridiagonal
linear-systems solvers, and the evaluation of polynomials.
```

### Strana 96

```text
50      Chapter 1.     Prefix Sums and Their Applications


                     1.4.2        Higher Order Recurrences
      We now consider the more general order m recurrences of the form:
             (
               bi                                           0≤i<m
       xi =                                                           (1.11)
               (xi−1 ⊗ ai,1 ) ⊕ · · · ⊕ (xi−m ⊗ ai,m ) ⊕ bi m ≤ i < n

 where ⊕ and ⊗ are binary operators with the same three restrictions as
in (1.5): ⊕ is associative, ⊗ is semiassociative, and ⊗ distributes over ⊕.
      To convert this equation into the form (1.5), we define the following
vector of variables:

                             si    = [ xi   · · · xi−m+1 ].                     (1.12)

Using (1.11) we can write (1.12) as:
                                                              
                                   ai,1       1    0   ··· 0
                                 .                         .. 
                                 ..          0     1        . 
                                                              
                                 .           ..       ..      
si = [ xi−1 · · · xi−m ] ⊗(v)   ..           .          . 0  ⊕(v) [ bi 0 · · · 0 ]
                                 .                            
                                 .                            
                                 .         0      ··· 0 1 
                                       ai,m 0      ··· 0 0

     = (si−1 ⊗(v) Ai ) ⊕(v) Bi                                                  (1.13)

 where ⊗(v) is vector-matrix multiply and ⊕(v) is vector addition. If we use
matrix-matrix multiply as the companion operator of ⊗(v) , then (1.13) is in
the form (1.5). The time taken for solving equations of the form (1.11) on an
EREW PRAM is therefore:

 (Tm⊗m (m)+Tv⊗m (m)+Tv⊕v (m))TS (n, p) = O((n/p+lg p)Tm⊗m (m)) (1.14)

where Tm⊗m (m) is the time taken by an m ⊗ m matrix multiply. The sequen-
tial complexity for solving the equations is O(nm), so the parallel complexity
is optimal in n when n/p ≥ lg p, but is not optimal in m—the parallel algo-
rithm performs a factor of O(TM⊗M (m)/m) more work than the sequential
algorithm.
      Applications of the recurrence (1.11) include solving recurrences of the
form xi = ai + bi /xi−1 (see problem 10), and generating the first n Fibonacci
numbers x0 = x1 = 1, xi = xi−1 + xi−2 (see problem 11).
```

### Strana 97

```text
                                                                1.5 Segmented Scans         51


   a                           =      [5       1     3      4       3     9    2       6]
   f                           =      [1       0     1      0       0     0    1       0]
   segmented +-scan            =      [5       6     3      7      10    19    2       8]
   segmented max-scan          =      [5       5     3      4       4     9    2       6]


FIGURE 1.10
The segmented scan operations restart at the beginning of each segment. The
vector f contains flags that mark the beginning of the segments.


                                  1.5
                            Segmented Scans

This section shows how the vector operated on by a scan can be broken into
segments with flags so that the scan starts again at each segment boundary
(see Figure 1.10). Each of these scans takes two vectors of values: a data vector
and a flag vector. The segmented scan operations present a convenient way
to execute a scan independently over many sets of values. The next section
shows how the segmented scans can be used to execute a parallel quicksort,
by keeping each recursive call in a separate segment, and using a segmented
+-scan to execute a split within each segment.
      The segmented scans satisfy the recurrence:
                       
                         a0
                                                                i=0
            xi   =            ai                   fi = 1                             (1.15)
                                                                 0<i<n
                              (xi−1 ⊕ ai )         fi = 0

where ⊕ is the original associative scan operator. If ⊕ has an identity I⊕ ,
then (1.15) can be written as:
                              
                                  a0                        i=0
                  xi    =                                                             (1.16)
                                  (xi−1 ×s fi ) ⊕ ai        0<i<n

where ×s is defined as:
                                           
                                               I⊕    f =1
                            x ×s f    =                                               (1.17)
                                               x     f = 0.

This is in the form (1.5) and ×s is semiassociative with logical or as the
companion operator (see Problem 9). Since we have reduced (1.15) to the
```

### Strana 98

```text
52      Chapter 1.      Prefix Sums and Their Applications


form (1.5), we can use the technique described in Section 1 to execute the
segmented scans in time

                            (Tor + T×s + T⊕ )TS (n, p) .                         (1.18)

     This time complexity is only a small constant factor greater than the
unsegmented version since or and ×s are trivial operators.

                         1.5.1    Example: Quicksort
       To illustrate the use of segmented scans, we consider a parallel version
of quicksort. Similar to the standard sequential version, the parallel version
picks one of the keys as a pivot value, splits the keys into three sets—keys
lesser, equal and greater than the pivot—and recurses on each set.3 The
parallel algorithm has an expected time complexity of O(TS (n, p) lg n) =
O( np lg n + lg2 n).
       The basic intuition of the parallel version is to keep each subset in its
own segment, and to pick pivot values and split the keys independently within
each segment. Figure 1.11 shows pseudocode for the parallel quicksort and
gives an example. The steps of the sort are outlined as follows:
       1. Check if the keys are sorted and exit the routine if they are.
          Each processor checks to see if the previous processor has a lesser
          or equal value. We execute a reduce with logical and to check if all
          the elements are in order.
       2. Within each segment, pick a pivot and distribute it to the other
          elements.
          If we pick the first element as a pivot, we can use a segmented scan
          with the binary operator copy, which returns the first of its two
          arguments:
                                     a ← copy(a, b) .
          This has the effect of copying the first element of each segment
          across the segment. The algorithm could also pick a random ele-
          ment within each segment (see Problem 15).
       3. Within each segment, compare each element with the pivot and
          split based on the result of the comparison.
          For the split, we can use a version of the split operation described in
          Section 1.3 which splits into three sets instead of two, and which is
3 We do not need to recursively sort the keys equal to the pivot,   but the algorithm as
described below does.
```

### Strana 99

```text
                                                    1.5 Segmented Scans      53


    procedure quicksort(keys)
      seg-flags[0] ← 1
      while not-sorted(keys)
        pivots    ← seg-copy(keys, seg-flags)
        f         ← pivots <=> keys
        keys      ← seg-split(keys, f, seg-flags)
        seg-flags ← new-seg-flags(keys, pivots, seg-flags)

  Key                     =    [6.4   9.2   3.4   1.6   8.7   4.1   9.2   3.4]
  Seg-Flags               =    [1      0     0     0     0     0     0      0]
  Pivots                  =    [6.4   6.4   6.4   6.4   6.4   6.4   6.4   6.4]
  F                       =    [=     >     <     <     >     <     >      <]
  Key ← split(Key, F)     =    [3.4   1.6   4.1   3.4   6.4   9.2   8.7   9.2]
  Seg-Flags               =    [1      0     0     0     1     1     0      0]
  Pivots                  =    [3.4   3.4   3.4   3.4   6.4   9.2   9.2   9.2]
  F                       =    [=     <     >     =     =     =     <      =]
  Key ← split(Key, F)     =    [1.6   3.4   3.4   4.1   6.4   8.7   9.2   9.2]
  Seg-Flags               =    [1      1     0     1     1     1     1      0]


FIGURE 1.11
An example of parallel quicksort. On each step, within each segment, we dis-
tribute the pivot, test whether each element is equal-to, less-than or greater-
than the pivot, split into three groups, and generate a new set of segment
flags. The operation <=> returns one of three values depending on whether
the first argument is less than, equal to or greater than the second.


         segmented. To implement such a segmented split, we can use a seg-
         mented version of the +-scan operation to generate indices relative
         to the beginning of each segment, and we can use a segmented copy-
         scan to copy the offset of the beginning of each segment across the
         segment. We then add the offset to the segment indices to generate
         the location to which we permute each element.
      4. Within each segment, insert additional segment flags to separate
         the split values.
         Knowing the pivot value, each element can determine if it is at the
         beginning of the segment by looking at the previous element.
      5. Return to step 1.
```

### Strana 100

```text
54     Chapter 1.   Prefix Sums and Their Applications


Each iteration of this sort requires a constant number of calls to the scans
and to the primitives of the PRAM. If we select pivots randomly within each
segment, quicksort is expected to complete in O(lg n) iterations, and therefore
has an expected running time of O(lg n · TS (n, p)).
     The technique of recursively breaking segments into subsegments and
operating independently within each segment can be used for many other
divide-and-conquer algorithms, such as mergesort.



                                1.6
                       Allocating Processors

      Consider the following problem: given a set of processors, each contain-
ing an integer, allocate that integer number of new processors to each initial
processor. Such allocation is necessary in the parallel line-drawing routine
described in Section 1. In this line-drawing routine, each processor calcu-
lates the number of pixels in the line and dynamically allocates a processor
for each pixel. Allocating new elements is also useful for the branching part
of many branch-and-bound algorithms. Consider, for example, a brute force
chess-playing algorithm that executes a fixed-depth search of possible moves
to determine the best next move. We can test or search the moves in parallel
by placing each possible move in a separate processor. Since the algorithm
dynamically decides how many next moves to generate (depending on the
position), we need to dynamically allocate new processing elements.
      More formally, given a length l vector A with integer elements ai , allo-
cation is the task of creating a new vector B of length

                                       l−1
                                       X
                                  L=         ai                         (1.19)
                                       i=0

with ai elements of B assigned to each position i of A. By assigned to, we
mean that there must be some method for distributing a value at position i of
a vector to the ai elements which are assigned to that position. Since there is
a one-to-one correspondence between elements of a vector and processors, the
original vector requires l processors and the new vector requires L processors.
Typically, an algorithm does not operate on the two vectors at the same time,
so that we can use the same processors for both.
      Allocation can be implemented by assigning a contiguous segment of
elements to each position i of A. To allocate segments we execute a +-prescan
```

### Strana 101

```text
                                                            1.6 Allocating Processors             55


            V                                        [v1    =              v2      v3 ]
            A                                        [4     =              1        3]
            Hpointers ← +-prescan(A)                 [0     =              4        5]
                                                    
                                                  
                                                
                                              
                                                                           ?         ?
  Segment-flag                      =      [1      0      0       0      1       1        0     0]
  distribute(V, Hpointers)          =      [v1     v1     v1      v1     v2      v3       v3   v3 ]
  index(Hpointers)                  =      [0      1      2       3      0       0        1     2]



FIGURE 1.12
An example of processor allocation. The vector A specifies how many new
elements each position needs. We can allocate a segment to each position by
applying a +-prescan to A and using the result as pointers to the beginning
of each segment. We can then distribute the values of V to the new elements
with a permute to the beginning of the segment and a segmented copy-scan
across the segment.


on the vector A that returns a pointer to the start of each segment (see Fig-
ure 1.12). We can then generate the appropriate segment flags by writing a
flag to the index specified by the pointer. To distribute values from each posi-
tion i to its segment, we write the values to the beginning of the segments and
use a segmented copy-scan operation to copy the values across the segment.
Allocation and distribution each require one call to a scan and therefore have
complexity TS (l, p) and TS (L, p) respectively.
      Once a segment has been allocated for each initial element, it is often
necessary to generate indices within each segment. We call this the index
operation, and it can be implemented with a segmented +-prescan.

                     1.6.1        Example: Line Drawing
      As an example of how allocation is used, consider line drawing. The
line-drawing problem is: given a set of pairs of points

            h(x0 , y0 ) : (x̂0 , ŷ0 )i, . . . , h(xn−1 , yn−1 ) : (x̂n−1 , ŷn−1 )i ,

generate all the locations of pixels that lie between on of the pairs of points.
Figure 1.13 illustrates an example. The routine we discuss returns a vector of
```

### Strana 102

```text
56      Chapter 1.    Prefix Sums and Their Applications




  procedure line-draw(x, y)
     in parallel for each line i
         % determine the length of the line
         length[i] ← max(|p2 [i].x − p1 [i].x|, |p2 [i].y − p1 [i].y|)

          % determine the x and y increments
          ∆[i].x ← (p2 [i].x − p1 [i].x) / length[i]
          ∆[i].y ← (p2 [i].y − p1 [i].y) / length[i]

      % distribute values and generate index
      p′1 ← distribute(p1, lengths)
      ∆′ ← distribute(∆, lengths)
      index ← index(lengths)

      in parallel for each pixel j
          % determine the final position
          result[j].x ← p′1 [j].x + round(index[j] × ∆′ [j].x)
          result[j].y ← p′1 [j].y + round(index[j] × ∆′ [j].y)




FIGURE 1.13
The pixels generated by a line drawing routine. In this example the endpoints
are h(11, 2) : (23, 14)i, h(2, 13) : (13, 8)i, and h(16, 4) : (31, 4)i. The algorithm
allocates 12, 11 and 16 pixels respectively for the three lines.
```

### Strana 103

```text
                                                                    1.7 Exercises   57


(x, y) pairs that specify the position of each pixel along every line. If a pixel
appears in more than one line, it will appear more than once in the vector.
The routine generates the same set of pixels as generated by the simple digital
differential analyzer sequential technique.
       The basic idea of the routine is for each line to allocate a processor
for each pixel in the line, and then for each allocated pixel to determine, in
parallel, its final position in the grid. Figure 1.13 shows the code. To allocate
a processor for each pixel, each line must first determine the number of pixels
in the line. This number can be calculated by taking the maximum of the x
and y differences of the line’s endpoints. Each line now allocates a segment of
processors for its pixels, and distributes one endpoint along with the per-pixel
x and y increments across the segment. We now have one processor for each
pixel and one segment for each line. We can view the position of a processor
in its segment as the position of a pixel in its line. Based on the endpoint the
slope and the position in the line (determined with a index operation), each
pixel can determine its final (x, y) location in the grid.
       This routine has the same complexity as a scan TS (m, p), where m is
the total number of pixels. To actually place the points on a grid, rather than
just generating their position, we would need to permute a flag to a position
based on the location of the point. In general, this will require the simplest
form of concurrent-write (one of the values gets written), since a pixel might
appear in more than one line.


                                    1.7
                                  Exercises
1.1    Modify the algorithm in Figure 1.4 to execute a scan instead of a prescan.
1.2    Use the scan operation to compare two strings of length n in O(n/p + lg p)
       time on an EREW PRAM.
1.3    Given two vectors of bits that represent nonnegative integers, show how a
       prescan can be used to add the two numbers (return a vector of bits that
       represents the sum of the two numbers).
1.4    Trace the steps of the split-radix sort on the vector
                     [2     11      4      5     9      6      15       3].
1.5    Show that subtraction is semiassociative and find its companion operator.
1.6    Write a recurrence equation of the form (1.5) that evaluates a polynomial

                          y = b1 xn−1 + b2 xn−2 + · · · + bn−1 x + bn
```

### Strana 104

```text
58     Chapter 1.       Prefix Sums and Their Applications


       for a given x.

1.7    Show that if ⊗ has an inverse, the recurrence of the form (1.5) can be solved
       with some local operations (not involving communication among processors)
       and two scan operations (using ⊗ and ⊕ as the operators).
1.8    Prove that vector-matrix multiply is semiassociative.

1.9    Prove that the operator ×s defined in (1.17) is semiassociative.
1.10   Show how the recurrence x(i) = a(i) + b(i)/x(i − 1), where + is numeric
       addition and / is division, can be converted into the form (1.11) with two
       terms (m = 2).
1.11   Use a scan to generate the first n Fibonacci numbers.

1.12   Show how to solve a tridiagonal linear-system using the recurrences in Sec-
       tion 1.4. Is the algorithm asymptotically optimal?

1.13   In the language Common Lisp, the % character means that what follows the
       character up to the end of the line is a comment. Use the scan operation to
       mark all the comment characters (everything between a % and an end-of-
       line).
1.14   Trace the steps of the parallel quicksort on the vector
                  [27       11     51    5     49     36         15   23].
1.15   Describe how quicksort is changed so that it selects a random element within
       each segment for a pivot.

1.16   Design an algorithm that given the radius and number of sides on a regular
       polygon, determines all the pixels that outline the polygon.




                           Notes and References

      The all-prefix-sums operation has been around for centuries as the recur-
rence xi = ai + xi−1 . A parallel circuit to execute the scan operation was first
suggested by Ofman (1963) for the addition of binary numbers. A parallel
implementation of scans on a perfect shuffle network was later suggested by
Stone (1971) for polynomial evaluation. The optimal algorithm discussed in
Section 1.2 is a slight variation of algorithms suggested by Kogge and Stone
(1973) and by Stone (1975) in the context of recurrence equations.
      Ladner and Fischer (1980) first showed an efficient general-purpose cir-
cuit for implementing the scan operation. Brent and Kung (1980), in the
```

### Strana 105

```text
                                                             1.7 Bibliography      59


context of binary addition, first showed an efficient VLSI layout for a scan
circuit. More recent work on implementing scan operations in parallel include
the work of Fich (1983) and of Lakshmivarahan, Yang and Dhall (1987), which
give improvements over the circuit of Ladner and Fischer, and of Lubachevsky
and Greenberg (1987), which demonstrates the implementation of the scan
operation on asynchronous machines. Blelloch (1987) suggested that certain
scan operations be included in the PRAM model as primitives and shows how
this affects the complexity of various algorithms. Work on the linked-list-
based all-prefix-sums operation is considered and referenced in Chapters 2, 3
and 4.
      The line-of-sight and radix-sort algorithms are discussed by Blelloch
(1988, 1990). The parallel solution of recurrence problems was first discussed
by Karp, Miller and Winograd (1967), and parallel algorithms to solve them
are given by Kogge and Stone (1973), Stone (1973, 1975) and Chen and Kuck
(1975). Hyafil and Kung (1977) show that the complexity (1.10) is a lower
bound.
      Schwartz (1980) and, independently, Mago (1979) first suggested the
segmented versions of the scans. Blelloch (1990) suggested many uses of
these scans including the quicksort algorithm and the line-drawing algorithm
presented in Sections 1 and 1.
      I would like to thank Siddhartha Chatterjee, Jonathan Hardwick and
Jay Sipelstein for reading over drafts of this chapter.



                                 Bibliography


Blelloch, G.E., Scans as Primitive Parallel Operations. IEEE Transactions on Com-
      puters, C-38(11):1526–1538, November 1989.
Blelloch, G.E., Vector Models for Data-Parallel Computing. MIT Press, Cambridge,
      MA, 1990.
Blelloch, G.E., and Little, J.J., Parallel Solutions to Geometric Problems on the Scan
      Model of Computation. In Proceedings International Conference on Parallel
      Processing, pages Vol 3: 218–222, August 1988.
Brent, R.P., and Kung, H.T., The Chip Complexity of Binary Arithmetic. In Pro-
      ceedings ACM Symposium on Theory of Computing, pages 190–200, 1980.
Chen, S., and Kuck, D.J., Time and Parallel Processor Bounds for Linear Recurrence
      Systems. IEEE Transactions on Computers, C-24(7), July 1975.
Fich, F.E., New Bounds for Parallel Prefix Circuits. In Proceedings ACM Symposium
      on Theory of Computing, pages 100–109, April 1983.
```

### Strana 106

```text
60      Chapter 1.    Prefix Sums and Their Applications


Hyafil, L., and Kung, H.T., The Complexity of Parallel Evaluation of Linear Recur-
      rences. Journal of the Association for Computing Machinery, 24(3):513–521,
      July 1977.
Karp, R.H., Miller, R.E., and Winograd S., The Organization of Computations for
      Uniform Recurrence Equations. Journal of the Association for Computing
      Machinery, 14:563–590, 1967.
Kogge, P.M., and Stone, H.S., A Parallel Algorithm for the Efficient Solution of a
      General Class of Recurrence Equations. IEEE Transactions on Computers,
      C-22(8):786–793, August 1973.
Ladner, R.E., and Fischer, M.J., Parallel Prefix Computation. Journal of the Asso-
      ciation for Computing Machinery, 27(4):831–838, October 1980.
Lakshmivarahan, S., Yang, C.M., and Dhall, S.K., Optimal Parallel Prefix Circuits
      with (size + depth) = 2n−n and ⌈log n⌉ ≤ depth ≤ ⌈2 log n⌉−3. In Proceedings
      International Conference on Parallel Processing, pages 58–65, August 1987.
Lubachevsky, B.D., and Greenberg, A.G., Simple, Efficient Asynchronous Parallel
      Prefix Algorithms. In Proceedings International Conference on Parallel Pro-
      cessing, pages 66–69, August 1987.
Mago, G.A., A network of computers to execute reduction languages. International
      Journal of Computer and Information Sciences, 1979.
Ofman, Y., On the Algorithmic Complexity of Discrete Functions. Soviet Physics
      Doklady, 7(7):589–591, January 1963.
Schwartz, J.T., Ultracomputers. ACM Transactions on Programming Languages
      and Systems, 2(4):484–521, October 1980.
Stone, H.S., Parallel Processsing with the Perfect Shuffle. IEEE Transactions on
      Computers, C-20(2):153–161, 1971.
Stone, H.S., An Efficient Parallel Algorithm for the Solution of a Tridiagonal Linear
      System of Equations. Journal of the Association for Computing Machinery,
      20(1):27–38, January 1973.
Stone, H.S., Parallel Tridiagonal Equation Solvers. ACM Transactions on Mathe-
      matical Software, 1(4):289–307, December 1975.
```
