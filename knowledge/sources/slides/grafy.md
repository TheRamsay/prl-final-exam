# Grafove algoritmy

Automaticky extrahovany text z OpenDocument prezentace.

| Pole | Hodnota |
|---|---|
| Zdroj | [[raw/2526_Grafy_v1.odp]] |
| Soubor | `2526_Grafy_v1.odp` |
| Pocet slidu | 65 |

### Strana 1

```text
ALGORITMY NAD GRAFY
```

### Strana 2

```text
LITERATURA
Reif, J: Synthesis of Parallel Algorithms, Morgan Kaufmann, 1993, ISBN:155860135X, kapitola 2
Reif, J: Synthesis of Parallel Algorithms, Morgan Kaufmann, 1993, ISBN:155860135X, kapitola 3
Hirvonen, J:Distributed Algorithms 2020,Aalto University, Finland,https://jukkasuomela.fi/da2020/
```

### Strana 3

```text
Práce se seznamy
Algoritmy pracují nad vázaným seznamem
Každý prvek drží hodnotuvi(nebo označení uzlu) a ukazatel na následijíSucc[i]
Pole následníkůsucc
Succ
3
5
3
6
4
1
Index
1
2
3
4
5
6
Následníkem uzlu 2 je uzel 5
```

### Strana 4

```text
Určení předchůdců na základě následníků
Je třeba zvlášť ošetřit první a poslední prvek seznamu
Algorithm 1:
fori = 1tondo in parallel
Pred[Succ[i]] = i
Algorithm2:
fori = 1 to ndo inparallel
Pred[i]=nil
ifi<>Succ[i]then
Pred[Succ[i]] = i;
t(n)=O(1)p(n)=nc(n)=O(n) Vše od EREW výše (!)
```

### Strana 5

```text
Úloha: ohodnocení seznamu (List Ranking)
Převod seznamu na pole
Uzly jsou seřazeny podle vzdálenosti k poslednímu uzlu v seznamu
Sekvenční řešení má tříduO(n)
Paralelní řešení – zdvojování cesty (path doubling)
Algorithm
Input: array Succ[1..n]
Output: array Rank[1..n]
fori=1tondo in parallel
ifSucc[i]=i thenRank[i] = 0
elseRank[i] = 1
fork = 1tolog ndo
Rank[i] = Rank[i] + Rank[Succ[i]]
Succ[i] = Succ[Succ[i]]
end for
Rank posledního je 0
Absorbce vzdálenosti následníka a jeho přeskočení
```

### Strana 6

```text
List Ranking – Příklad
SuccRank
index1 2 3 4 5 61 2 3 4 5 6
initially3 5 3 6 4 11 1 0 1 1 1
step13 4 3 1 6 31 2 0 2 2 2
step23 1 3 3 3 31 4 0 3 4 2
step33 3 3 3 3 31 5 0 3 4 2
2
5
4
6
1
3
1
0
EREW
t(n)=O(log n)
p(n)=n
c(n)=O(n*log n)
Není optimální
1
2
5
4
6
1
3
4
3
2
0
1
2
5
4
6
1
3
5
4
3
2
0
```

### Strana 7

```text
Úloha: Suma suffixů, paralelní
Nepočítáme vzdálenost, ale součet hodnot od aktuálního ke koncovému uzlu
Na vstupu máme kromě seznamu i hodnoty uzlů a operátor, který má být použit
Algorithm
Input:arrayV = [vn-1, ... v1,0]
fori = 1tondo inparallel
ifSucc[i] = ithenLast =vi
Val[i] = 0/* nebo neutrální prvek operace*/
elseVal[i] =vi
fork = 1tolog ndo
Val[i] = Val[i]Val[Succ[i]]
Succ[i] =Succ[Succ[i]]
end for
ifLast<> 0thenVal[i] = Val[i]Last
end for
Zabrání vícečetnému přičítání hodnoty posledního prvku procesy, které jej dosáhnou
dříve než polog nkrocích. Hodnotu přičteme všem až zde.
```

### Strana 8

```text
Suffix Sum – Příklad
2
5
4
6
1
3
2
1
3
1
2->0
2
5
4
6
1
3
4
3
4
0
2
5
4
6
1
3
7
6
4
0
3
SuccSuffix sum
index1 2 3 4 5 61 2 3 4 5 6
initially3 5 3 6 4 13 3 0 2 1 1
step13 4 3 1 6 33 4 0 3 3 4
step23 1 3 3 3 33 7 0 6 7 4
step33 3 3 3 3 33 10 0 6 7 4
Step43 3 3 3 3 35 12 2 8 9 6
2
5
4
6
1
3
7
6
4
0
2
5
4
6
1
3
12
9
8
6
2
3
5
EREW
t(n)=O(log n)
p(n)=n
c(n)=O(n*log n)
Initially
Step 1
Step 2
Step 3
Step 4
```

### Strana 9

```text
List Ranking, Algoritmus 2
Motivace, algoritmus není optimální
Pracují všechny procesy, v každém kroce polovina již nadále zbytečně
Pokud by přestaly pracovat – kteří? (procesy neznají svoji pozici v seznmu)
=>Uspat všechny na sudých pozicích, ale kteří jsou sudí?
```

### Strana 10

```text
Randomizovaný algoritmus – Random Mate
Uzlům se náhodně přidělí hodnotaM(Male) neboF(Female)
Uspaný uzel je takový, který máhodnotu M a jeho předchůdce hodnotu F
Vzdálenost mezi dvěma neuspanými uzly je nejvíc 2 (tj nenásledují dva uspané uzly po sobě)
Pro rekonstrukci a určení pozice každého z uzlů, je třeba si poznačit čas uspání
M
F
M
F
M
F
M
F
M
F
M
```

### Strana 11

```text
Algoritmus Random Mate, 1. fáze
procedureRandomMate
fori = 1tondo inparallel
ifi =tailthenrank[i]=0
elserank[i] = 1
active[i] =True/pokudTrue- procesor pracuje,False- procesor je uspaný */
endfor
t = 1/*globalvariable*/
whilesucc[head] <>taildo inparallel//ije rankprocesu
ifactive[i]andsucc[i] <>tailthen
sex[i] =Random(M, F)
ifsex[i] = Fandsex[succ[i]] = Mthen
time[succ[i]] = t
active[succ[i]] =False
rank[i] = rank[i] + rank[succ[i]]
succ[i] =succ[succ[i]]
endif
t = t + 1
endif
endwhile
/* endofjumpingphase*/
Postupné uspávání a přeskakování procesů, na konci první proces ukazuje na poslední
a zná vzdálenost k němu.
Jak snadno a rychle
Poznáme, že uzel je
posledním v seznamu?
```

### Strana 12

```text
Random Mate, příklad, 1. fáze
1
F
M
F
M
F
M
0
t=1
F
M
F
M
F
2
1
0
2
t=1
t=2
t=1
t=2
t=1
M
F
1
0
3
4
2
t=1
t=2
t=3
t=1
t=2
t=1
t=4
1
0
4
2
t=1
t=2
t=3
t=1
t=2
t=1
F
M
1
0
4
2
7
8
F
Přeskočen,
ale …
```

### Strana 13

```text
Algoritmus Random Mate, 2. fáze
/* reconstuction phase */
whilet > 0do in parallel //i je rank procesu
iftime[i] = tandsucc[i] <> tailthen
rank[i] = rank[i] + rank[succ[i]]
end if
t = t - 1
end while
end
Rekonstrukční fáze
Podle označení uspání uzlů jsou v obráceném pořadí uzly oživovány
Oživený proces spočte svůj rank jako součet ranku před uspáním a ranku následníka
```

### Strana 14

```text
Random Mate, příklad, 2. fáze
t=1
t=2
t=3
t=1
t=2
t=1
t=4
1
0
4
2
8
t=1
t=2
t=3
t=1
t=2
t=1
1
0
4
2
8
t=1
t=2
t=1
t=2
t=1
1
0
4+1=5
2
t=1
1
0
5
2+1=3
8
1
0
5
3
6
2
7
4
1+5=6
```

### Strana 15

```text
Random Mate, analýza
Pro velkénje velmi malá pravděpodobnost, že počet kol algoritmu bude větší než c.log n
t(n) =O(log n)
Cena
c(n) = n.log n cožnení optimální
Cena (množství práce)
c(n) = n + 3/4n + (3/4)2n + ... = O(n)cožjeoptimální
```

### Strana 16

```text
Optimal List Ranking
Požadavek: pevný počet stále pracujících procesorů (procesor nelenoší, pokud uzel, který reprezentuje, uspán)
Simulace algoritmu Random Mate pomocín/log nprocesorů, každý procesor vykonává prácilog nprocesorů
Každý procesor má zásobník prvků o velikostilog n
Každý procesor na vrcholu zásobníku se pokoušívyplést, pokud jeMa ukazuje na něj uzel s přiřazenýmF
Pokud je vrchol zásobníku přeskočen, procesor se zabývá dalším prvkem na zásobníku
F
M
F
M
F
M
F
M
```

### Strana 17

```text
Vypletení uzlu
Přeskočení uzlu
succ
Vypletení uzlu
pred
```

### Strana 18

```text
AlgoritmusOptimal List Ranking
```

### Strana 19

```text
Optimal List Ranking, příklad,jen 1. fáze
Lineární seznam o devíti listech
9
5
1
6
7
3
2
8
4
Pole následníků:
1
2
3
4
5
6
7
8
9
6
8
nil
9
1
7
3
4
5
1
F
2
F
3
F
nil
M
nil
M
4
F
5
F
6
F
7
F
8
F
9
F
```

### Strana 20

```text
Optimal List Ranking, příklad
Lineární seznam o devíti listech
9
5
1
6
7
2
8
4
Pole následníků:
1
2
3
4
5
6
7
8
9
6
8
nil
9
1
7
3
4
5
1
F
2
F
3
F
4
M
5
F
6
F
7
M
8
F
9
F
Náhodně zvoleno F/M pro
Top prvky v zásobnících (1,4,7)
Přeskočeny budou uzly4a7
3
nil
M
nil
```

### Strana 21

```text
Optimal List Ranking, příklad
Lineární seznam o devíti listech
9
5
1
6
7
3
2
8
4
Pole následníků:
1
2
3
4
5
6
7
8
9
6
8
nil
9
1
7
3
4
5
1
F
2
F
3
F
4
M
5
M
6
F
7
M
8
M
9
F
Náhodně zvoleno F/M pro
Top prvky v zásobnících (1,5,8)
Přeskočeny budou uzly5a8
(ne 1)!
3
nil
M
nil
```

### Strana 22

```text
Optimal List Ranking, příklad
Lineární seznam o devíti listech
9
5
1
6
7
3
2
8
4
Pole následníků:
1
2
3
4
5
6
7
8
9
6
8
nil
9
1
7
3
4
5
1
M
2
F
3
F
4
M
5
M
6
F
7
M
8
M
9
F
Náhodně zvoleno F/M pro
Top prvky v zásobnících (1,6,9)
Přeskočeny bude uzel1
3
nil
M
nil
```

### Strana 23

```text
Optimal List Ranking, příklad
Lineární seznam o devíti listech
9
5
1
6
7
3
2
8
4
Pole následníků:
1
2
3
4
5
6
7
8
9
6
8
nil
9
1
7
3
4
5
1
M
2
F
3
F
4
M
5
M
6
M
7
M
8
M
9
M
Náhodně zvoleno F/M pro
Top prvky v zásobnících (2,6,9)
Přeskočen bud uzel9
nil
M
nil
```

### Strana 24

```text
Optimal List Ranking, příklad
Lineární seznam o devíti listech
9
5
1
6
7
3
2
8
4
Pole následníků:
1
2
3
4
5
6
7
8
9
6
8
nil
9
1
7
3
4
5
1
M
2
M
3
F
4
M
5
M
6
M
7
M
8
M
9
M
Náhodně zvoleno F/M pro
Top prvky v zásobnících (2,6)
Přeskočen nebude žádný uzel
nil
M
nil
```

### Strana 25

```text
Optimal List Ranking, příklad
Lineární seznam o devíti listech
9
5
1
6
7
3
2
8
4
Pole následníků:
1
2
3
4
5
6
7
8
9
6
8
nil
9
1
7
3
4
5
1
M
2
F
3
F
4
M
5
M
6
M
7
M
8
M
9
M
Náhodně zvoleno F/M pro
Top prvky v zásobnících (2,6)
Přeskočen bud uzel6
nil
M
nil
```

### Strana 26

```text
Optimal List Ranking, příklad
Lineární seznam o devíti listech
9
5
1
6
7
3
2
8
4
Pole následníků:
1
2
3
4
5
6
7
8
9
6
8
nil
9
1
7
3
4
5
1
M
2
M
3
F
4
M
5
M
6
M
7
M
8
M
9
M
Náhodně zvoleno F/M pro
Top prvky v zásobnících (2)
Kdy bud přeskočen uzel2?
nil
M
nil
```

### Strana 27

```text
PARALELNÍ ALGORITMY NAD STROMy
```

### Strana 28

```text
PrůchodEuler tour
Obecný průchod binárním stromem
Její speciální případy jsou průchodypreorder(NLR),postorder(LRN)ainorder (LNR)
+
*
-
2
5
1
3
2
L
N
R
*
```

### Strana 29

```text
Euler tour
T= (V,E)-daný strom
T’= (V,E’)-orientovaný graf získaný z T tak, že každá hrana (u, v) je nahrazena dvěma orientovanými hranami <u, v> a <v, u>
T’ je Elerovský graf – obsahuje orientovanou kružnici, která prochází každou hranou právě jednou
1
2
3
4
5
6
```

### Strana 30

```text
Euler tour, paralelní algoritmus
Eulerova kružniceje reprezentována funkcí následníkaEtourkterá každé hraně e ∈E’ přiřazuje hranuEtour(e) ∈E’ která následuje hranu e
Reprezentace –seznam sousednosti(adjacency list)
Vrchol1
2
3
4
Pokud e = (u, v) je hrana e, pakR= (v, u) je reverzní hrana
1
3
4
2
e1
e4
e2
e5
e6
e3
```

### Strana 31

```text
Vytvoření Eulerovy cesty, algoritmus
constructing Euler tour
Input: adjacency list of T
Output: Array Etour with 2n-2 entries
Etour(e) is a edge followinge
fori = 1to2n-2do in parallel//i je rank procesu
{ei= (u, v) }
ifnext(eR) <> nil thenEtour(e) = next(eR)
elseEtour(e) = AdjList(v){první prvek ze seznamu sousednosti uzluv }
endif
endfor
```

### Strana 32

```text
Příklad
Algoritmus nepoužívá kořen stromu
Pokud použijeme kořen, pak cesta prochází stromem průchodem „depth-first search“
1
3
4
2
e1
e4
e2
e5
e6
e3
4
```

### Strana 33

```text
Euler Tour, Příklad2
1
2
5
4
e1
e3
e4
e6
e11
e2
3
6
e12
7
e5
e10
e9
e7
e8
e1
e2
e9
e10
v1
e4
e3
v4
e6
e5
v5
e7
e8
v6
e12
e11
v7
e8
e7
e11
e12
e10
e9
v3
e3
e4
e2
e1
e5
e6
v2
e1
e2
e3
e4
e5
e6
e7
e8
e9
e10
e11
e12
e2
e1
e4
e3
e6
e5
e8
e7
e10
e9
e12
e11
nill
e9
nill
e5
e7
e2
nill
e10
v2
V4
v7
v5
v3
v1
v6
e3
e4
e8
e6
e11
e1
e12
eR
next(eR)
e=(u,v)
AdjList(v)
Fisrt(AdjList(v))
```

### Strana 34

```text
Zavedení kořene
Pro operace nad stromem musíme být schopni pro každý vrchol v určit jeho rodičeparent(v)
Proto musíme definovat kořen stromu, kterým bude vrcholr
Zkonstruujeme Eulerovu cestu a přiřadíme pro hranuevedoucí do kořener
Etour(e) = e
Jinými slovy přeřízneme Eulerovu cestu ve vrcholur
```

### Strana 35

```text
Úkol: Spočíst pozici každé hrany
Algoritmus– Eulerova cesta s pozicemi
Vstup: binární strom (adjacency list)
Výstup: pole Etour, pole Posn, kde Posn(e) je pozice hranyev Eulerově cestě
1.Spočteme se pole EtourO(c)
2.Přiřadíme Etour(e) = e pro hranuevedoucí do kořeneO(1)
3.Rank =ListRanking(Etour)O(log n)
4.Spočteme paralelně posn(e) = 2n-2-Rank(e)O(1)
1
3
4
2
e1
e4
e2
e5
e6
e3
root
```

### Strana 36

```text
Úkol: Nalezení rodičů
Vstup:Eulerova cesta a speciální vrcholroot
Výstup:Pro každý vrcholv≠root,je jeho rodičem vrcholparent(v)
Hrana- dopřednáposn(e) <posn(eR)
- zpětnáposn(e) >posn(eR)
Pokud (u,v) je dopředná hrana, pakuje rodičemvve stromu
Uzelvje listem, pokud neexistuje dopředná (v,w)
Algorithm
for each edge e = (u, v) do in parallel
if posn(e) < posn(eR) then
parent(v):= u;
endif
parent(root) := nil;
endfor
```

### Strana 37

```text
Obecný výpočet ve stromu
Pro mnoho algoritmů nad stromemTje postup:
Vytvoříme Eulerovu cestu
Vytvoříme pole hodnot
Spočteme nad ním sumu suffixů(List Ranking)
Provedeme korekci
Můžeme tak např. spočíst:
Pořadípostordervrcholu
Pořadípreordervrcholu
Pořadíinordervrcholu
Počet následníkůvrcholu
Úroveňvrcholu
```

### Strana 38

```text
Úkol: Přiřazení pořadí preorder vrcholům
Pořadípreordervrcholu ve stromě je 1+počet dopředných hran, kterými jsme prošli po cestě k vrcholu
(Preorder –navštiv nejdřívrodiče,pak obapotomky)
Root
1
2
3
4
1
3
4
2
e1
e4
e2
e5
e6
e3
```

### Strana 39

```text
Příklad
Algorithm
1) for eachedo in parallel
if e is forward edge then weight = 1
else weight = 0
endif
2) weight = SuffixSums(Etour, Weight)
3) for eachedo in parallel
if e=(u, v) is forward edge then
preorder(v) = n - weight(e) + 1
endif
preorder(root) = 1
e1 e2 e3 e4 e5 e6
Result
Suffix Sums
1
3
4
2
e1
e4
e2
e5
e6
e3
1 3 6 2 4 5 pořadí v EC
```

### Strana 40

```text
Úkol: Počet následníků vrcholuv
Počet dopředných hran v podstromu, který má kořen ve vrcholuv+ 1 (aby byl započítán i vrchol)
Počet dopředných hran v segmentu Eulerovy cesty, počínajícím i končícím vev
Algorithm- number of descendants
1) for eachedo in parallel
if e is forward edge then weight = 1
else weight = 0
endif
2) weight = SuffixSums(Etour, Weight)
3) for eachedo in parallel
if e=(u, v) is forward edge then
desc(v) = weight(u, v) - weight(v, u)
endif
desc(root) = n
```

### Strana 41

```text
1
2
5
4
e1
e3
e4
e6
e11
e2
3
6
e12
7
e5
e10
e9
e7
e8
1
2
5
4
1[6]
1[5]
0[4]
0[2]
1[1]
0[2]
3
6
0[0]
7
1[4]
0[0]
1[2]
1[3]
0[2]
e1
e2
e3
e4
e5
e6
e7
e8
e9
e10
e11
e12
6
2
5
4
2
3
2
0
1
0
SuffixSum
v1
v2
v3
v4
v5
v6
v7
7
4
2
1
2
1
n=7
```

### Strana 42

```text
Úkol: Výpočet úrovně vrcholu
Počet hran na cestě (nikoli Eulerově) z vrcholu v do kořene
Rozdíl počtu zpětných a dopředných hran na zbytku Eulerovy cesty od vrcholu v do konce
Algorithm: - level of vertex
1) for eachedo in parallel
ifeis forward edge then weight(e) =-1
else weight(e) = +1
end if
end for
2) weight = SuffixSums(Etour, weight)
3) for eachedo in parallel
if e = (u, v) is forward edge then level(v) = weight(e) + 1
endif
endfor
level(root) = 0
```

### Strana 43

```text
1
2
5
4
e1
e3
e4
e6
e11
e2
3
6
e12
7
e5
e10
e9
e7
e8
1
2
5
4
-1[0]
-1[1]
1[0]
-1[1]
1[-1]
3
6
1[0]
7
-1[1]
1[-1]
-1[0]
-1[2]
1[1]
e1
e2
e3
e4
e5
e6
e7
e8
e9
e10
e11
e12
0
-1
1
0
1
0
2
1
0
-1
1
0
SuffixSum
v1
v2
v3
v4
v5
v6
v7
0
1
2
3
root=v1
```

### Strana 44

```text
Analýza předchozích algoritmů
0) Spočtení EtourO(c)
1) Inicializace weightO(c)
2) Výpočet SuffixSumsO(log n)
3) Korekce výsledkuO(c)
t(n) =O(log n)
c(n) – závisí na implementaci SuffixSums
```

### Strana 45

```text
Úkol:Pořadí listů
1) for eachedo in parallel
if e is forward edge to a leaf then weight = 1
else weight = 0
endif
2) weight = SuffixSums(Etour, Weight)
3) for eachedo in parallel
leafs=weight((root, w))
if e=(u, v) is forward edge
and v is leaf
then
leaf(v) = leafs - weight(u, v) + 1
endif
preorder(root) = 1
e1 e2 e3 e4 e5 e6
1
3
4
2
e1
e4
e2
e5
e6
e3
0
1
0
Weight
2
1
2
1
0
SfxSum
Leaf(v2)=1; leaf(v4)=2
```

### Strana 46

```text
KONTRAKCE STROMů
```

### Strana 47

```text
Kontrakce stromu / Tree Contraction
Některé operace nad stromem se nedají provést efektivně pouze pomocí Eulerovy cesty
Například paralelní vyhodnocení aritmetického výrazu uloženého v binárním stromu
```

### Strana 48

```text
Chain (řetěz)
Posloupnost uzlů prvního stupně až po uzel, který má jednoho nebo dva vnuky
Nejdelšířetězve stromu
```

### Strana 49

```text
Kontrakce stromu
Contraction:Rake+Compress
RAKE– redukce listů k rodičovskému uzlu
Počet operací Rake když
strom je lineárním
seznamem?
```

### Strana 50

```text
Kontrakce stromu
Contraction:Rake+Compress
Compress– redukce sudých prvků řetězu na liché
```

### Strana 51

```text
Kontrakce stromu
Contraction:Rake+Compress
RAKE– redukce listů k rodičovskému uzlu
RAKE
COMPRESS
RAKE
COMPRESS
RAKE
```

### Strana 52

```text
Kontrakce stromu, redukce výrazu
Každý list obsahuje operand a každý nelistový uzel obsahuje operátor, jako je například+,*
Cílem je spočíst hodnotu výrazu v kořeni
Technikatree contractionje systematický způsob jak zmenšovat strom až do velikosti jednoho vrcholu
Opakovaně aplikujeme
Spojení listu s jeho rodičem
nebo
Spojení vrcholu stupně 2 s jeho rodičem
```

### Strana 53

```text
OperaceSHUNT
T= (V,E)je binární strom a pro každý vrcholvjep(v)jeho rodič
sib(v)je synemp(v)(tedy sourozencemv)
Bereme v úvahu pouze binární stromy
OperaceSHUNTpro listový vrcholutakový, žep(u) ≠ rprovede následující:
Odstraníu ap(u)ze stromuT
Připojí podstromsib(u) top(p(u))
```

### Strana 54

```text
SHUNT pro strom s výrazy
Po hranách jsou funkce ve tvarua*X+b, kde X je hodnota potomka
Inicializovány jako funkce identity 1*X+0
ʘ
X
5
fL(X)
fR(Y)=CR
f(fL(X) ʘ fR(Y))
X
f‘(fʘ(Z))
fR(Y)= a*5+ b
fL(X)= c*X + d
f(Z)= e*Z + i
f‘(Z)=e*((c*X+d)ʘ(a*5+b)) + i
```

### Strana 55

```text
SHUNTpro strom s výrazy
Po hranáchse propagují funkce ve tvaru a*X+b, kde X je hodnota potomka
Inicializovány jako funkce identity 1*X+0
X
5
fL(X)
fR(5)
X
f‘(Z)
f(val(v))
fR(Y)=1*5+ 0
fL(X)= 1*X + 0
f(Z)= 1*Z + 0
f‘(Z) =1*((1*X+0)+(1*5+0)) +0
f‘(Z) =1*X+ 5
v
fR(Y) = 1*Y + 0
fL(X) = 1*X + 0
f(Z) = 1*Z + 0
f‘(Z) = 1*((1*X+0)*(1*5+0)) + 0
f‘(Z) = 5*X+0
Pokudjesčítání
Pokud jenásobení
```

### Strana 56

```text
Operace SHUNT
V algoritmutree contractionaplikujeme operaceSHUNTopakovaně, abychom pokaždé zmenšili velikost stromu
Pro maximální rychlost ji chceme aplikovat na co nejvíce listů paralelně
Ale nelze aplikovat operaci RAKE na vrcholy, jejichž rodiče ve stromu sousedí
Například nelze provést paralelně operaci RAKE na vrcholy1a8
Musíme aplikovatoperaci SHUNT na nesousedící uzly
```

### Strana 57

```text
Kontrakce s operacíSHUNT
Uložíme všechnlistůdo poleA
Aoddobsahuje prvky poleAs lichými indexy
Aevenobsahuje prvky poleAse sudými indexy
PoleAoddaAevenvytvoříme v časeO(1)za cenuO(n)
fori:=1 to log(n+1)do
1.Apply the rake operation in parallel to all the elements
of Aoddthat are left children
2.Apply the rake operation in parallel to the rest
of the elements in Aodd
3.A := Aeven
endfor
```

### Strana 58

```text
Kontrakce stromuoperací SHUNT
A = (2,4,6)
```

### Strana 59

```text
Vlastnosti algoritmu
Když je operace SHUNT aplikována paralelně na několik listů, rodiče těchto listů nejsou sousedi
Provádíme SHUNT na každého druhého levého syna, pak na každého druhého pravého syna atd.
Počet listů se po každé iteraci cyklu zmenší na polovinu
Liché listy jsou „shrabány“
Proto je strom zcela zredukován v časeO(log n)
```

### Strana 60

```text
Barvení lineárního seznamu
Barvení třemi barvami {1,2,3}
Počáteční ohodnocení -> unikátní čísloc(u)pro každý uzelu
Lokální maxima (levý a pravý soused
c(ul) < c(u) > c(ur)
c(u) <-min({1,2,3}-{c(ul), c(ur)})
12
33
15
20
27
37
42
13
12
1
15
20
27
37
1
13
2
1
15
20
27
2
1
2
1
15
20
1
2
1
2
1
15
2
1
2
1
2
1
3
2
1
2
1
2
>
<
>
<
>
<
>
<
>
<
>
<
>
```

### Strana 61

```text
Barvení lineárního seznamu
Extrémní případ je pro monotónně uspořádané hodnoty uzlů seznamu
10
9
8
7
6
5
4
3
1
9
8
7
6
5
4
3
1
2
1
7
6
5
4
3
1
2
1
2
6
5
4
3
1
2
1
2
1
5
4
3
1
2
1
2
1
2
4
3
>
<
>
<
>
<
>
<
```

### Strana 62

```text
Barvení redukcí řádu
V nejhorším případě počet iterací O(n)
Rychlejší algoritmus
Redukuje uzlu označené identifikátorynabarev …
c0(u) a c1(u) jsou barvy
c0(u) = 2*i(u)+b(u)kde
i(u) je pozice bitu, kde se c0(u) a c1(u) liší
b(u) je hodnota bitu na této pozici
Pozn: Poslední prvek má fiktivního následníka s jinou barvou než on sám (např+1)
12
33
15
20
27
37
42
13
12
33
001100
100001
2*0+0= 0(0000)
33
15
100001
001111
2*1+0=2 (0010)
15
20
001111
010100
2*0+1= 1(0001)
20
27
010100
011011
2*0+0= 0(0000)
27
37
011011
100101
2*1+1= 3(0011)
37
42
100101
010101
2*5+0= 10 (1010)
42
13
010101
001101
2*4+0= 8(1000)
13
14
001101
001110
2*4+1=1 (0001)
```

### Strana 63

```text
Barvení redukcí řádu
Barvy jsou unikátní, protože v seznamu se nachází unikátní čísla (na začátku), nebo dvě sousední čísla jsou rozdílná
i(u) =i(v) =i: We know thatb(u)is bit numberiofc0(u), andb(v)is bit numberiofc1(u). By the definition ofi(u), we alsoknow that these bits differ. Henceb(u)̸=b(v)andc(u)̸=c(v).
i(u)̸=i(v): No matter how we chooseb(u)∈ {0,1}andb(v)∈{0, 1}, we havec(u)̸=c(v).
0
2
1
0
3
10
8
1
0
2
0000
0010
2*1+0=2 (010)
2
1
0010
0001
2*1+1=3 (011)
1
0
0001
0000
2*0+1= 1(001)
0
3
0000
0011
2*0+0= 0(000)
3
10
0011
1010
2*0+1=1 (001)
10
8
1010
1000
2*1+1=3 (011)
8
1
1000
0001
2*0+0=0 (000)
1
2
0001
0010
2*0+1=1 (001)
```

### Strana 64

```text
Barvení redukcí řádu
Pro 4 barvy
Nelze redukovat na méně než 4 barvy
Pokud máme 6 nebo míň barev, redukujeme na tři algoritmem ↑
Počet iterací dán jako
2
3
1
0
1
3
0
1
0
2
010
011
2*0+0=0 (010)
2
1
011
001
2*1+1=3 (011)
1
0
001
000
2*0+1= 1(001)
0
3
000
001
2*0+0= 0(000)
3
10
001
011
2*1+0=2 (001)
10
8
011
000
2*0+1=1 (011)
8
1
000
001
2*0+0=0 (000)
1
2
001
010
2*0+1=1 (001)
```

### Strana 65

```text
Barvení redukcí řádu
0
3
1
0
2
1
0
1
>
<
0
2
1
0
2
1
0
1
Nakonec použijeme algoritmus pro barvení třemi barvami …
```
