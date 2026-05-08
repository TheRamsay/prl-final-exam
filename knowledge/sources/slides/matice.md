# Matice a paralelni nasobeni

Oficialni slidy extrahovane z PDF. Text je automaticky vytazeny pres `pdftotext -layout`; u obrazkovych nebo diagramovych stran kontroluj originalni PDF.

## Metadata

| Pole | Hodnota |
|---|---|
| Zdroj | [[raw/2425_Matice.pdf]] |
| Soubor | `2425_Matice.pdf` |
| Stran | 23 |
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
 ALGORITMY PRO
MATICE A VEKTORY
```

### Strana 2

```text
Literatura k této přednášce
■ Akl, kapitola 7
■ https://research.iaun.ac.ir/pd/saeed-nasri/pdfs/UploadFile_9325.pdf
```

### Strana 3

```text
Transpozice matice
 ■ Čtvercová matice n x n s prvky ai j
 ■ Čtvercová matice n x n s prvky aj i
 ■ Sekvenční řešení:
          procedure TRANSPOSE(A)
            for i=2 to n do
               for j=1 to i-1 do
                    aij   aji
               endfor
            endfor


 ■ Složitost je 𝑡 𝑛 = 𝑂(𝑛2 )
```

### Strana 4

```text
Transpozice matice, mřížková topologie
■ Topologie, mřížková n x n pro čtvercovou matici n x n
■ Každý procesor má 3 registry
   – A - obsahuje aij, aji po ukončení
   – B - hodnoty od pravého (horního) souseda
   – C - hodnoty od levého (dolního) souseda
```

### Strana 5

```text
    Transpozice matice, mřížková topologie
 A=5        A=6        A=7       A=8
B=6,2,1    B=7,3,1    B=8,4,1    B=     Step 1:
C=1,1,2      C=         C=       C=     do steps 1.1 and 1.2 in parallel
                                        (1.1)
                                         for i = 2 to n do in parallel
  A=1        A=2       A=3       A=4      for j = 1 to i - 1 do in parallel
  B=       B=3,3,2    B=4,4,2    B=        C(i - 1, j) ← (aij, j, i)
C=11,1,3   C=12,2,3     C=       C=
                                        end for
                                        end for
                                        (1.2)
 A=11       A=12       A=13      A=14
                                         for i = 1 to n - 1 do in parallel
  B=         B=       B=14,4,3    B=
C=9,1,4    C=10,2,4   C=0,3,4     C=      for j = i + 1 to n do in parallel
                                           B(i, j - 1) ← (aij, j, i)
                                          end for
  A=9       A=10        A=0      A=15    end for.
  B=         B=         B=        B=
  C=         C=         C=        C=
                                               (hodnota, cilovy_x, cilovy_y)
```

### Strana 6

```text
    Transpozice matice, mřížková topologie
  A=5       A=1        A=7        A=8      Paralelně 2.1, 2.2, 2.3
B=7,3,1    B=8,4,1    B=8,4,1     B=
C=11,1,3   C=1,1,2      C=        C=       2.1
                                           Pokud obdrží hodnoty zprava, posílají
                                           dál
 A=6         A=2       A=12       A=4      Pokud obdrží hodnotu zleva, a jsou
B=6,2,1    B=4,4,2    B=4,4,2     B=       cílové, uloží, jinak posílají dál
C=9,1,4    C=10,2,4   C=12,2,3    C=
                                           2.2
                                           Pokud diagonální obdrží zdola,
 A=11        A=3       A=13       A=0      posílají vpravo
  B=       B=3,3,2    B=14,4,3     B=      Pokud diagonální obdrží zprava,
C=9,1,4    C=10,2,4   C=0,3,4    C=0,3,4   posílají dolů

                                           2.3
  A=9       A=10       A=14      A=15      Pokud obdrží hodnoty zdola, posílají
  B=         B=       B=14,4,3    B=       dál
  C=         C=         C=        C=       Pokud obdrží hodnotu shora, a jsou
                                           cílové, uloží, jinak posílají dál
```

### Strana 7

```text
   Transpozice matice, mřížková topologie
 A=5        A=1       A=7        A=8      Paralelně 2.1, 2.2, 2.3
B=8,4,1   B=8,4,1    B=8,4,1     B=
C=9,1,4   C=11,1,3     C=        C=       2.1
                                          Pokud obdrží hodnoty zprava, posílají
                                          dál
 A=6        A=2       A=12       A=4      Pokud obdrží hodnotu zleva, a jsou
B=7,3,1   B=4,4,2    B=4,4,2     B=       cílové, uloží, jinak posílají dál
C=9,1,4   C=10,2,4   C=10,2,4    C=
                                          2.2
                                          Pokud diagonální obdrží zdola,
 A=11       A=3       A=13       A=0      posílají vpravo
  B=      B=4,4,2    B=14,4,3     B=      Pokud diagonální obdrží zprava,
C=9,1,4   C=10,2,4   C=0,3,4    C=0,3,4   posílají dolů

                                          2.3
 A=9       A=10       A=14      A=15      Pokud obdrží hodnoty zdola, posílají
 B=         B=       B=14,4,3    B=       dál
 C=         C=         C=        C=       Pokud obdrží hodnotu shora, a jsou
                                          cílové, uloží, jinak posílají dál
```

### Strana 8

```text
    Transpozice matice, mřížková topologii
 A=5              A=1          A=11        A=8       Paralelně 2.1, 2.2, 2.3
B=8,4,1          B=8,4,1      B=8,4,1      B=
C=9,1,4          C= 9,1,4    C= 11,1,3     C=        2.1
                                                     Pokud obdrží hodnoty zprava, posílají
                                                     dál
 A=6               A=2        A=12        A=10       Pokud obdrží hodnotu zleva, a jsou
B= 8,4,1         B=4,4,2     B=4,4,2        B=       cílové, uloží, jinak posílají dál
C=9,1,4          C=10,2,4    C=10,2,4    C= 10,2,4
                                                     2.2
                                                     Pokud diagonální obdrží zdola,
 A=7               A=3        A=13         A=0       posílají vpravo
B= 7,3,1         B=4,4,2     B=14,4,3       B=       Pokud diagonální obdrží zprava,
C=9,1,4          C=10,2,4    C=0,3,4      C=0,3,4    posílají dolů

                                                     2.3
 A=9              A=4         A=14         A=15      Pokud obdrží hodnoty zdola, posílají
 B=              B= 4,4,2    B=14,4,3       B=       dál
 C=                C=          C=           C=       Pokud obdrží hodnotu shora, a jsou
                                                     cílové, uloží, jinak posílají dál
    + další dva kroky TODO
```

### Strana 9

```text
Transpozice matice, mřížková topologie,
analýza
■ Počet procesorů 𝑝(𝑛) = 𝑂(𝑛2 )
■ Časová složitost, k přesunutí je třeba 2 ∗ (𝑛 − 1) kroků t n = 𝑂(𝑛)
■ Cena c n = 𝑂(𝑛3 )              což není optimální
```

### Strana 10

```text
Transpozice matice, Perfect Shuffle
■ Topologie
   – Uzly propojené jako Perfect Sfuffle (dokonalý přesun)
   – Funguje pro matice 𝑛 × 𝑛 kde 𝑛 = 2𝑞 pro nějaké přirozené číslo 𝑞
                       2
    –   Celkem tedy 2𝑞 = 22𝑞 uzlů
    –   Pro indexování uzlů je třeba 2𝑞 bitů
■ Uzel
   – Může přeposlat hodnotu na uzel s indexem levě bitově posunutým
        ■   (např. 0101 -> 1010, 1100 -> 1001 apod.)
■ Princip
   – Po log 𝑛 tedy 𝑞 přesunech každé z hodnot matice je matice transponovaná
```

### Strana 11

```text
    Transpozice matice, Perfect Shuffle
                                                                          [2,3]
Uzel matice [𝑖, 𝑗] je indexován jako 2𝑞 𝑖 − 1 + 𝑗 − 1



procedure SHUFFLE TRANSPOSE (A)                         2𝑞 𝑖 − 1 + 𝑗 − 1 = 22 ∗ 1 + 2
for i = 1 to q do                                       = 6 = 𝟎𝟏𝟏𝟎
        for k = 1 to 22𝑞 − 2 do in parallel
                 𝑷𝑘 ,sends the element of A it currently holds to 𝑷2𝑘𝑚𝑜𝑑(22𝑞−1)
        end for
                                                                                  Levý shift
end for
```

### Strana 12

```text
        Transpozice matice, Perfect shuffle, příklad
       Matice 𝟒𝒙𝟒 neboli 22 𝑥22 , q=2
         2𝑞 𝑖 − 1 + 𝑗 − 1 → 2𝑞 𝑗 − 1 + 𝑖 − 1                         (1,2)                                  (2,4)
       Pro 1,2 → [2,1], tedy                                 (2,1)
        22 1 − 1 + 2 − 1 → 22 2 − 1 + 1 − 1
                  1 → 4, 0001 → 0010
       Pro 2,4 → [4,2], tedy                                                                        (4,2)
        22 2 − 1 + 4 − 1 → 22 4 − 1 + 2 − 1
                 7 → 13, (0111 → 1101)                            0001         0100           0111             1101



0000      0001   0010   0011   0100   0101   0110   0111   1000      1001    1010     1011   1100     1101      1110       1111




0000      0001   0010   0011   0100   0101   0110   0111   1000      1001    1010     1011   1100     1101          1110   1111
```

### Strana 13

```text
Transpozice matice, Perfect shuffle

■ Při přenosu nedochází ke konfliktům -> každý odesilatel je unikátní a tedy i příjemce
  po levém shiftu je unikátní
■ Počet procesorů 𝑝(𝑛) = 𝑂(𝑛2 )
■ Časová složitost, k přesunutí je třeba log n kroků t n = 𝑂(log 𝑛)
■ Cena c n = 𝑂(log 𝑛 ∗ 𝑛3 )               což není optimální
```

### Strana 14

```text
 Transpozice matice, sdílená paměť

 ■ I pro EREW lze provést transpozici v konstantním čase
 ■ Potom cena je 𝑐 = 𝑂(𝑛2 )

procedure EREW TRANSPOSE
for i = 2 to n do in parallel
       for j = 1 to i - 1 do in parallel
              aij ++ aji
       end for
end for
```

### Strana 15

```text
Násobení matic
■ Součin matic A (m x n) a B (n x k) je matice C (m x k) kde:

   𝑐𝑖𝑗 = σ𝑛𝑠=1 𝑎𝑖𝑠 ∗ 𝑏𝑠𝑗          1 ≤ 𝑖 ≤ 𝑚, 1 ≤ 𝑗 ≤ 𝑘

     Složitost je O (n3)
     Složitost optimálního algoritmu není známa, je O(nx), kde 2<x<3
     Žádný algoritmus nemá lepší složitost než O(n2)
    procedure MATRIX MULT(A, B, C)
    for i=1 to m do
      for j=1 to k do
        cij = 0
        for s=1 to n do
             cij=cij + (ais * bsj)
        endfor
      endfor
    endfor
```

### Strana 16

```text
Násobení matic – sdílená paměť
Nerealistická varianta
                         procedure MATRIX MULT(A, B, C)
                         for i=1 to m do in parallel
                           for j=1 to k do in parallel
                             cij = 0
                             for s=1 to n do in parallel
                                   cij=cij + (ais * bsj)
                             endfor
                           endfor
                         endfor
Realistická varianta

                         procedure MATRIX MULT(A, B, C)
                         for i=1 to m do in parallel
                           for j=1 to k do in parallel
                             cij = 0
                             for s=1 to n do
                                   cij=cij + (ais * bsj)
                             endfor
                           endfor
                         endfor
```

### Strana 17

```text
     Násobení matic ne mřížce                                                             b13
                                                                                    b12   b23
                                                                              b11   b22   b33   n
    Mřížka n x k procesorů                                                    b21   b32   b43
    Prvky matic A a B se přivádějí do procesorů 1. řádku a 1 sloupce          b31   b42   b53
                                                                              b41   b52
    Každý procesor P(i,j) obsahuje prvek cij
                                                                              b51               k

                                                        a11 a12 a13 a14 a15

                                     k
              n                                      a21 a22 a23 a24 a25
                                b11 B12 b13                                                     m
     a11 a12 a12 A14 a15
                                b21 b22 b23       a31 a32 a33 a34 a35
     a21 A22 a22 a24 a25
m                           n   b31 b32 b33
     a31 A32 a32 A34 a35                      a41 a42 a43 a44 a45
                                b41 b42 b43
     a41 a42 a42 a44 a45
                                b51 b52 b54
                                                                        m            k
```

### Strana 18

```text
   Násobení matic ne mřížce
   Algoritmus
   procedure MESH MULT(A, B, C)
   for i=1 to m do in parallel
     for j=1 to k do in parallel
       cij = 0
       while P(i,j) receives inputs a,b do
            cij = cij + (a * b)
            if i<m then send b to P(i+1, j)
            if j<k then send a to P(i, j+1)
       endwhile
     endfor
   endfor

Analýza
Prvky am1 a b1k potřebují m+k+n-2 kroků, aby se dostaly k poslednímu procesoru P(m, k)
t(n) = O(n)    p(n) = O(n2) c(n) = O(n3) … což není optimální
```

### Strana 19

```text
Násobení matice vektorem
■ Součin matice A (m x n) a vektoru U (n) je vektor V (m) kde:
■ 𝑣𝑖 = σ𝑛𝑙=1 𝑎𝑗𝑖 ∗ 𝑢𝑖 1 ≤ 𝑖 ≤ 𝑛
■ Časová složitost optimálního sekvenčního algoritmu je 𝒕 𝑛 = 𝑶(𝑚 ∗ 𝑛)
   – Je třeba pracovat s každým prvkem matice
```

### Strana 20

```text
Paralelní násobení matice vektorem
■ Lineární pole m procesorů, každý obsahuje jeden prvek vi


  P1    V1               a11 a12 a13 a14

  P2    V2           a21 a22 a23 a24

  P3
        V3        a31 a32 a33 a34


             u1
             u2
             u3
             u4
```

### Strana 21

```text
Paralelní násobení matice vektorem,
algoritmus a analýza
    procedure LINEAR MV MULT
    for i=1 to m do in parallel
      vi = 0
      while Pi receives inputs a and u do
        vi = vi + (a * u)
        if i>1 then send u to Pi-1
      endwhile
    endfor
Analýza
     – t(n) = m+n-1 = t(n)=O(n) p(n)=O(n)
     – c(n)=O(n2)       → což je optimální
```

### Strana 22

```text
Paralelní násobení matice                                     v1
                                                              v2
vektorem, stromová struktura                                  v3


•   Čas m+n-1 předchozího algoritmu je
    možno zlepšit na m-1+log n při
    zdvojnásobení počtu procesorů
•   Architektura má n listových
    procesorů P1...Pn a n-1 nelistových
    procesorů
■ Listové procesory násobí, nelistové
  sčítají                                      u1        u2        u3             u4
                                          P1        P2                  P3   P4


                                           a11       a12       a13                a14
                                           a21       a22       a23                a24
                                           a31       a32       a33                a34
```

### Strana 23

```text
    Paralelní násobení matice                                           v1
                                                                        v2
    vektorem, stromová struktura                                        v3
Algoritmus
procedure TREE MV MULT(A, U V)
do steps 1 and 2 in parallel
(1) for i=1 to n do in parallel
      for j=1 to m do
          send ui*dij to parent
      endfor
   endfor
(2) for i=n+1 to 2n-1 do in parallel
      while Pi receives two inputs do
          compute the sum
             if i<2n-1 then send result to parent        u1        u2        u3             u4
                 else write result                  P1        P2                  P3   P4
                 endif
       endwhile
   endfor                                            a11       a12       a13                a14
■   Analýza                                          a21       a22       a23                a24
     –    t(n)=m-1+ log n = O(m)                     a31       a32       a33                a34
     –    c(n)=O(m*n)          → což je optimální
```
