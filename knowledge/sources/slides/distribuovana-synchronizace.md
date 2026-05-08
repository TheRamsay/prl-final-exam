# Distribuovana synchronizace

Oficialni slidy extrahovane z PDF. Text je automaticky vytazeny pres `pdftotext -layout`; u obrazkovych nebo diagramovych stran kontroluj originalni PDF.

## Metadata

| Pole | Hodnota |
|---|---|
| Zdroj | [[raw/PRL2526_DISTSYNCH.pdf]] |
| Soubor | `PRL2526_DISTSYNCH.pdf` |
| Stran | 194 |
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
  KONSENSUS V
DISTRIBUOVANÝCH
   SYSTÉMECH
   František Zbořil ml., Petr Hanáček
              GTs – 2026
```

### Strana 2

```text
Synchronizace

■ Synchronizace zaručuje (částečné) uspořádání mezi událostmi
■ Pokud máme systémy se sdílenou pamětí, pak můžeme použít
  nám již známé mechanismy, jako jsou semafory nebo monitory
■ Pokud máme sdílený prostředek v distribuovaných systémech,
  jako například nástěnku, synchronizaci také již dokážeme
  realizovat, například pomocí systému LINDA
■ Ale pokud chceme zajistit synchronizaci pouze předáváním zpráv,
  potom se budeme zabývat
   1. Synchronizací globálním (reálným) časem
   2. Synchronizací řízenou master uzlem
   3. Synchronizací založenou na shodě mezi procesy
```

### Strana 3

```text
Synchronizace v distribuovaných
systémech, úvodní poznámky
■ Požadavky:
        ■   kauzalita: uspořádání v reálném čase ~ uspořádání dle
            logických hodin nebo časových razítek (”korektní chování z
            pohledu uživatele”)
        ■   všechny procesy uspořádávají události v tom samém
            pořadí
    – Pokud bychom měli, jakože nemáme, přesné hodiny ve
      všech uzlech, pak bychom byli schopni požadavky splnit.
      Dokážeme je ale splnit i bez nich
    – Vždy se totiž nemůžeme spolehnout na skutečný čas a
      někdy i nemusíme znát centrální řídící uzel
```

### Strana 4

```text
 SYNCHRONIZACE
     FYZICKÝM A
LOGICKÝM ČASEM
           FYZICKÝ ČAS
                   NTP
```

### Strana 5

```text
Synchronizace fyzického
času, Berkley algoritmus
■ Předpokládá se, že komunikace dotaz - odpověď (návratový
  čas) je dostatečně krátká
■ Hlavní uzel si vyžádá od všech hodnotu posunu vůči svému
  aktuálnímu času
■ Následně vypočte průměrnou hodnotu posunu a z té posuny
  pro jednotlivé uzly


      03:14                  03:06
-13    -16    +5        +5     +8    -13
03:01 02:58 03:19      03:01 02:58 03:19
```

### Strana 6

```text
Network Time Protocol (NTP)

■ Synchronizace v síti na různých úrovních (stratech)
■ Komunikace přes UDP
■ Universal Coordinated Time (UCT)
■ Různé módy synchronizace
   – Multicast – opakované vysílání aktuálního času v rámci
      skupiny. Vhodné pro malé sítě s vysokou rychlostí
      přenosu dat
   – Klientský přístup – volání procedury na serveru klientem,
      použitelné v případech, kdy není možný multicast
   – Párový přístup – synchronizováno s velkou přesností
```

### Strana 7

```text
UTC




      Strata 1 (Time Servers)




                 Strata 2




                  Strata 3
```

### Strana 8

```text
NTP – trvání komunikace a
zpoždění
                                Ti-2      Ti-1




                         Ti-3                    Ti

■   Zpoždění se spočte jako
       di=Ti-2-Ti-3+Ti-Ti-1
■   Posunutí (offset) je
       oi=1/2(Ti-2-Ti-3+Ti-1-Ti)
■   Obojí je spočteno pro všechny kontaktované NTP servery
■   Filtrování (Marzullo-ův algoritmus)
```

### Strana 9

```text
NTP – trvání komunikace a
zpoždění, příklad
         124                 152   161




         161        183                  204



■ Skutečný offset je 37, zpoždění jedné zprávy je 6
      di=Ti-2-Ti-3+Ti-Ti-1
      di=152-183+204-161=-31+43=12
      oi=1/2(Ti-2-Ti-3+Ti-1-Ti)
      oi =1/2(152-183+161-204)=1/2(-31-43)=1/2(-74)=-37
```

### Strana 10

```text
Marzullo-ův algoritmus

■ Pro množinu intervalů hledáme nejmenší interval, který spadá
  do největšího možného počtu intervalů z této množiny.
■ tj. pokud by takové intervaly existovaly pro n intervalů a pro
  n+1 intervalů žádný průnik již nebylo možné nalézt, vezme se
  ten nejmenší z nich.

               a2        c2   b2

                    r2
```

### Strana 11

```text
Marzullo-ův algoritmus

■ Každý interval <a,b>, resp. <c-r,c+r> reprezentují dvě dvojice
      (a,1), (b,-1) resp. (c-r,1), (c+r,-11)


1. Seřaď intervaly podle offsetů počátků a konců intervalů.
   Počáteční okamžiky označte ci=1, koncové ci=-1
2. Best = 0, Count = 0
3. Postupně pro každý offset i od nejnižší hodnoty po nejvyšší
             Count += ci
             Pokud Count > Best pak Best = Count, c = ci
```

### Strana 12

_Bez extrahovatelneho textu._

### Strana 13

```text
 1     3      2   3    4      3   4 3   2    0
   2                                     1
[1,1] [3,3]           [4,6]                      [4,6]
  [2,2]
```

### Strana 14

```text
VOLBA HLAVNÍHO
          UZLU
```

### Strana 15

```text
Volba hlavního (master) uzlu,
algoritmus Chang a Roberts
■ Procesy jsou korektní po celou dobu (pro tuto a ostatní
  metody, než se přejde k nekorektním procesům)
   – Jejich chování definované a je správně, nikdy neselžou –
      nepřestanou fungovat ani na přechodnou dobu
■ Procesy jsou propojeny v kruhové topologii a každý má
  přiděleno unikátní číslo UID
■ Algoritmus hledá maximální hodnotu ze všech hodnot těchto
  uzlů
■ Zprávy jsou posílány po směru hodinových ručiček
```

### Strana 16

```text
Volba master uzlu, Chang and
Roberts, algoritmus
■   Procesy se shodnou na procesu, který má největší UID takto:
      – Uzel zahájí komunikaci, označí se za účastníka a pošle zprávu se svým
          UID následujícímu
      – Pokud uzel přeposílá zprávu, označí se za účastníka
      – Každý uzel po obdržení zprávy
          ■   Pokud UID ve zprávě je větší než UID tohoto uzlu, je zpráva přeposlána dále
              tak jak je
          ■   Pokud je číslo ve zprávě menší než má uzel UID, potom
               –    Pokud již je účastník, zahodí zprávu
               –    Pokud není účastník, nahradí hodnotu původní za svoje UID a
                    přepošle zprávu dále
          ■   Pokud je číslo ve zprávě stejné jako má uzel UID, potom tento uzel volbu
              vyhrál. Potom zahájí druhou část algoritmu
     –   Vítěz volby se odznačí jako účastník a pošle svoje číslo dále
     –   Každý, kdo obdrží zprávu a je stále účastníkem, si číslo poznačí,
         odznačí se jako účastník a pošle zprávu dále.
     –   Pokud zprávu obdrží vítěz volby, zprávu zahodí
```

### Strana 17

```text
                    2                                       2 2                            2                                 2
          3                     4             3                      4           3                 4               3                 4
                                                                                                       4
              5             1                      5             1                   5         1                       5         1
                                                                                                                             4

           3 2                                5 2 3                                      2 5                               2
       3                    4             3                       4              3                 4               3                 4
      5                                                                                                                                  5
              5         1                         5           1                      5         1                       5         1


                    2                                   2                                  2                           5 2
                                                                                                             [5]
      3                     4             3                      4           3                     4               3                 4
                                                                            5
           5            1                     5              1                       5         1                       5         1
                    5
              [5]                                 [5]                                [5]                               [5]

[5]
                    2 5             [5]
                                                        2            [5]   [5]
                                                                                           2           [5]   [5]
                                                                                                                             2           [5]
      3                     4             3                      4               3                 4               3                 4
                                                                     5
          5             1                     5              1                       5         1 [5]                   5         1 [5]
                                                                                           5
```

### Strana 18

```text
Volba master uzlu, Chang and
Roberts, analýza algoritmu
■ Nejlepší případ – hlasování zahájí pouze uzel s nejvyšším UID.
  Pak proběhne 2n zpráv
■ Nejhorší případ – uzel s maximálním indexem je první za
  iniciátorem hlasování a každý uzel zahájí hlasování před
  odesláním první zprávy některým z uzlů
    – V nejhorším případě se musí přeposlat 3(n-1) zpráv pro
        jeden uzel
    – Celkově je ale možné pracovat až s O(n2) zprávami
                                                    (n*(n-1)/2)+n
         ■   Uzly od největšího po nejmenší (ve směru
                     posílání zpráv                             5
         ■   Každý uzel inicializuje volbu              1               4
         ■   Pak v první fázi 1+2+3+4+5=15 zpráv
                                                            2       3
```

### Strana 19

```text
 Volba master uzlu,
 Hirschberg-Sinclair
■   Počet zpráv i časová složitost O(n*log n)

Všechny uzly začínají výpočet zároveň, zašlou ELECTION(UID,0,1) pravému i levému
sousedovi

Po přijetí ELECTION(UID r, d) procesem i s UIDi
        if     UID < UIDi then zahoď zprávu
        elseif UID = UIDi then zašli levémi sousedovi ELECTED(UID)
        elseif d < 2r zašli ELECTION(UID, r. d+1) po směru zprávy (‘pošli dál’)
        elseif d >= 2r zašli REPLY(UID, r) směrem, odkud přišla zprávu (‘odpověz’)

Pří přijetí zprávy REPLY(UID, r)
         if       UID ≠ UIDi then zašli REPLY(UID, r) po směru zprávy
         elseif uzel obdržel REPLY(UID, r) z obou směrů,
                 then pošli ELECTION(UID r+1, d) po obou směrech

Po přijetí zprávy ELECTED(UID)
        if      UID ≠ UIDi then poznač si UID a přepošli zprávu ELECTED(UID) po
směru zprávy
```

### Strana 20

```text
   Volba master uzlu,
   Hirschberg-Sinclair
Příklad 1
                    1                   1                           1
                8       5           8       5               8               5

            4               2   4               2       4                       2

                6       7           6       7               6               7
                    3                   3                           3

Příklad 2
                    1                   1                       1
                8       2           8       2           8               2

            7               3   7               3   7                       3

                6       4           6       4           6               4
                    5                   5                       5
```

### Strana 21

```text
Volba master uzlu,
Hirschberg-Sinclair
■ V jednom běhu usne minimálně polovina uzlů, maximálně až
  na jeden všichni
■ Jediný z uzlů zůstane zaručeně po log2n bězích
■ V posledním z běhů bude zasláno 4n zpráv
   – V příkladech na předchozím slidu chybí poslední běh
   – A také informování ostatních uzlů o výsledku volby
■ Proto je zaručeno, že třída počtů zpráv je O(n*logn)
```

### Strana 22

```text
 SYNCHRONIZACE
LOGICKÉHO ČASU
 LAMPORTOVY HODINY, LAMPORTŮV A RA ALGORITMUS
                        MEAKAWŮV ALGORITMUS
                       RAYMONDůV ALGORITMUS
               CHANG A ROBERTSŮV ALGORITMUS
```

### Strana 23

```text
Požadavky na vzájemné
vyloučení
•   Vzájemné vyloučení (Mutual exclusion) – v kritické sekci smí
    být v jednom okamžiku nejvýše jeden proces.
•   Konzistence uspořádání (Ordering consistency) – systém
    musí zachovat definované pořadí konkurenčních požadavků.
•   Bez uváznutí (Deadlock freedom) – systém se nesmí dostat
    do stavu, kdy žádný proces nemůže pokračovat.
•   Bez vyhladovění (Starvation freedom) – každý proces žádající
    o vstup musí být nakonec obsloužen.
•   Férovost (Fairness) – procesy mají získávat přístup ke kritické
    sekci spravedlivým způsobem.
```

### Strana 24

```text
Mechanismy vzájemného vyloučení
v distribuovaných systémech

■ Obecně existují dva druhy mechanismů (algoritmů) pro
  zajištění vzájemného vyloučení
■ Algoritmy založené na časových razítcích
   – Lamportův algoritmus dist. vzájemného vyloučeni
   – Ricard-Agrawala-ův algoritmus
   – Meakawův algoritmus
■ Algoritmy založený na tokenech
   – Suzuki-Kasami vysílací algoritmus
   – Raymondův stromový algoritmus
```

### Strana 25

```text
Lamportovy hodiny

■ Nepotřebuje fyzický čas v distribuovaných systémech
■ Absence globálních hodin, synchronizovaných hodin, nebo
  master uzlu
■ Relace Happened-before (stalo se před tím) / kauzalita


R(e1,e2) iff   e1 předchází e2 v rámci jednoho procesu
               e1 je send(p2,m,ix) v procesu p1 a e2 je
                           receive(p1,m,ix) v procesu p2
                R(e1,e3) a R(e3,e2) // tranzitivita
```

### Strana 26

```text
Synchronizace s
Lamportovýmí hodinami
■ Lamportovy logické hodiny
   – Každý proces i má jedny logické hodiny Ci
   – Log. hodiny před každou událostí e zvyšují čítač
     (monotónně, tj. např o 1)
   – C(e) zobrazuje pro každou událost odpovídající logický
     čas
   – Požadujeme, aby
                  a►b => C(a)<C(b)
```

### Strana 27

```text
Implementace logických
hodin



■ Spolu se zprávou se posílá i časové razítko dle logického času
  vysílacího procesu
■ Při přijetí zprávy rec(m,p,tp) příjemce i nastaví/aktualizuje
  svůj logický čas Ci:=max(Ci+1, tp+1)
```

### Strana 28

```text
Implementace logických
hodin
        1       2       3   4       5   6       7




            1       2           3           4       7

■ Spolu se zprávou se posílá i časové razítko dle logického času
  vysílacího procesu
■ Při přijetí zprávy rec(m,p,tp) příjemce i nastaví/aktualizuje
  svůj logický čas Ci:=max(Ci+1, tp+1)
```

### Strana 29

```text
Poznámky k logickým
hodinám
■ “Happens-before” je nereflexivní relace částečného
  uspořádání
■ Abychom dosáhli úplného uspořádání je třeba dodat další
  informaci, zde lze použít ID procesů, pak procesy s nižším
  číslem ‘mají přednost’ a jejich události, pro které nemůžeme
  uspořádání původně určit, předcházejí událostem procesů s
  vyšším číslem.
■ Nerozlišujeme zvýšení logického času na základě toho, jestli k
  němu došlo vnitřní událostí, nebo na základě komunikace
```

### Strana 30

```text
Lamportův algoritmus

■ Procesy hledají shodu navzájem na tom, který z nich získá
  kritickou sekci
■ Založeno na FIFO doručování zpráv
■ Udržuje lokální prioritní frontu zpráv ve které priority jsou
  úplně uspořádány podle předávaných časových razítek
```

### Strana 31

```text
Lamportův algoritmus
(požadavek)
                 Časová razítka jsou úplně uspořádána diký číslu procesu
       [(2,1)]



 [(1,2)]
```

### Strana 32

```text
Lamportův algoritmus
(odpověď)
       [(2,1)]         [(1,2),(2,1)]



 [(1,2)]

           [(1,2),(2,1)]




             [(1,2)]   [(1,2),(2,1)]
```

### Strana 33

```text
Lamportův algoritmus
(kritická sekce)
       [(2,1)]         [(1,2),(2,1)]



 [(1,2)]

           [(1,2),(2,1)]




             [(1,2)]   [(1,2),(2,1)]
```

### Strana 34

```text
Lamportův algoritmus
(uvolnění kritické sekce)
       [(2,1)]         [(1,2),(2,1)]   [(2,1)]



 [(1,2)]

           [(1,2),(2,1)]




             [(1,2)]   [(1,2),(2,1)]        [(2,1)]
```

### Strana 35

```text
Algoritmus Ricart-Agrawala

■ Lamportův algoritmus vyžaduje 3(n-1) zpráv
   – (n-1) požadavků
   – (n-1) odpovědí
   – (n-1) uvolnění
■ Algoritmus Ricart-Agrawala
   – Jedná se o optimalizaci Lamportova algoritmu
        ■   Slučuje dohromady zprávy odpovědi a uvolnění
    – Celkem se tak posílá pouze 2(n-1) zpráv
    – Synchronizační zpoždění je opět jedna zaslaná zpráva
```

### Strana 36

```text
Algoritmus Ricart-Agrawala
(požadavek)
       [(2,1)]



 [(1,2)]
```

### Strana 37

```text
Algoritmus Ricart-Agrawala
(odpověď)
       [(2,1)]        [(1,2),(2,1)]


                            ack
 [(1,2)]

           [(1,2),(2,1)]
                                  ack
                           ack
```

### Strana 38

```text
Ricart-Agrawala algoritmus
(kritická sekce)
                                        Odpověď je pozdržena procesem P2
       [(2,1)]        [(1,2),(2,1)]


                            ack
 [(1,2)]

           [(1,2),(2,1)]
                                  ack
                           ack
```

### Strana 39

```text
Ricart-Agrawala algoritmus
(uvolnění kritické sekce)
       [(2,1)]        [(1,2),(2,1)]     [(2,1)]


                            ack
                                        ack
 [(1,2)]

           [(1,2),(2,1)]
                                  ack
                           ack
```

### Strana 40

```text
Maekawův algoritmus

■ Povolení je třeba jen od podmnožiny procesů
■ Každý proces 1<=i<=N si udržuje seznam procesů Ri tak, že
   – Každé dva procesy sdílí nějaký proces, tedy Ri∩Rj≠{}
   – Každý proces i je v Ri
    – Velikost těchto množin je K, K= 2 ∗ 𝑁 + 1
    – Každý proces je přítomen celkem K-krát v seznamech
      všech procesů
```

### Strana 41

```text
Maekawův algoritmus,
vytvoření kvór
■   Biliardová metoda pro vytváření kvór
■   Hrajeme šťouch vždy v tom samém směru, například směrem dopravo a nahoru
■   Přímý x zalomený šťouch (zamezí té samé posloupnosti pro všechny čísla na trase
    šťouchu před odrazem).
```

### Strana 42

```text
Billiard pro 2*24+1=7^2

     1         2         3              1         2         3
4         5         6         7    4         5         6         7
     8         9         10             8         9         10
11        12        13        14   11        12        13        14

     15        16        17             15        16        17

18        19        20        21   18        19        20        21

     22        23        24             22        23        24
```

### Strana 43

```text
Zalomený billiard pro 24 uzlů
• V místě odpovídajícímu číslu procesu, pro který hledáme kvórum, zalomíme
  na opačnou stranu.
• Zalomíme zpět tak, aby cílové pole bylo stejné jako v nezalomeném případě.


     1         2         3                 1         2         3
4         5         6         7       4         5         6         7

     8         9         10                8         9         10

11        12        13        14      11        12        13        14

     15        16        17                15        16        17

18        19        20        21      18        19        20        21

     22        23        24                22        23        24
```

### Strana 44

```text
Zalomený billiard pro 24 uzlů
• V místě odpovídajícímu číslu procesu, pro který hledáme kvórum, zalomíme
  na opačnou stranu.
• Zalomíme zpět tak, aby cílové pole bylo stejné jako v nezalomeném případě.


     1         2         3                  1         2         3

4         5         6         7        4         5         6         7

     8         9         10                 8         9         10

11        12        13        14       11        12        13        14
     15        16        17                 15        16        17
18        19        20        21       18        19        20        21

     22        23        24                 22        23        24
```

### Strana 45

```text
Maekawaův algoritmus,
základní verze
■   Žádající proces
     – Pokud chce proces i vstoupit do kritické sekce ve stavu svých
         logických hodin ts, pošle request(ts,i) všem procesům z Ri
     – Pokud obdrží grant(j) od všech j z Ri, vstoupí do kritické sekce
     – Po opuštění kritické sekce pošle release(i) všem z Ri
■   Žádaný proces. Pokud proces i obdrží request(ts,j) od nějakého procesu
    j, pak
       – pokud nevydal žádný aktuální grant jinému procesu, pošle grant(i)
           procesu j
       – pokud již vydal grant jinému procesu, pošel failed(i) a zařadí jej do
           fronty
       – Pokud obdrží zprávu release(j), pak odstraní proces j ze své fronty
           a pošle grant(k) případnému aktuálně prvnímu procesu ve frontě.
```

### Strana 46

```text
Maekawaův algoritmus,
základní verze
■ Výhoda - posílá k 𝑁 − 1 zpráv kde k je mezi 3 a 6 (minimálně
  request, grant, release, // request, fail, grant, release, //
  request, inquiry, yield, grant, release, grant – ve verzi bez
  uváznutí)
■ Problém – může nastat uváznutí
```

### Strana 47

```text
Maekawaův algoritmus,
uváznutí
■ Uváznutí pro procesy P0 – P6 v základní verzi,
■ Vytvoříme si quora R0-R6 (např billiardovou metodou)


R0={0,1,2}, R1={1,3,5}, R2={2,4,5}, R3={0,3,4}, R4={1,4,6},
R5={0,5,6}, R6={2,3,6}


■ 0,1,2 chtějí do KS – co obdrží od svých Ri?
   – 0 <- od 0 a 2 dostane grant, od 1 ne (garantuje sebe)
   – 1 <- od 1 a 3 dostane grant, od 5 ne (garantuje dvojku)
   – 2 <- od 4 a 5 dostane grant, od 2 ne (garantovala nulu)
Příklad:
      grant 0->0, grant 1->1, grant 3->1, failed 1->0, grant 2->0,
      failed 2->2, grant 4->2, grant 5->2, failed 5->1
```

### Strana 48

```text
Maekawaův algoritmus

■   Žádající proces
     – Pokud chce proces i vstoupit do kritické sekce ve stavu svých logických
          hodin ts, pošle request(ts,i) všem procesům z Ri
     – Pokud obdrží grant(j) od všech j z Ri, vstoupí do kritické sekce
     – Po opuštění kritické sekce pošle release(i) všem z Ri
■   Žádaný proces. Pokud proces i obdrží request(ts,j) od nějakého procesu j, pak
     – pokud nevydal žádný aktuální grant jinému procesu, pošle grant(i)
         procesu j
     – pokud vydal grant procesu s vyšší prioritou, pošle failed(i) procesu j a
         zařadí si tento proces do fronty
     – jinak
           ■   optá se procesu k, kterému dal grant zprávou inquire(i)
           ■   pokud obdrží zprávu yield(k), pak dá grant(i) a proces k si uloží do fronty
```

### Strana 49

```text
Maekawaův algoritmus

■ Spolupracující proces
   – Proces i, který dostane zprávu inquire(j) od procesu j
      pošle zpět zprávu yield(i), pokud dostal na svoji žádost
      fail(k) od nějakého procesu ze svého Ri, nebo poslal
      dříve někomu jinému yeld(i) a neobdržel od něj grant(i)
      zpět
   – Pokud proces i obdrží zprávu release(j), pak odstraní j ze
      své fronty a pošle grant(k) případnému aktuálně
      prvnímu procesu ve frontě.
```

### Strana 50

```text
Maekawaův algoritmus,
uváznutí vyřešeno
R0={0,1,2}, R1={1,3,5}, R2={2,4,5}, R3={0,3,4}, R4={1,4,6}, R5={0,5,6}, R6={2,3,6}
R0 > R1 > R2 …
      grant 0 -> 0, grant 1 -> 1, grant 3 -> 1,
      ?? grant(1 -> 0): // vydal grant 1, R1<R0
                  inquire 1
      grant 2 -> 0
      failed 2->2 // vydal grant R0, R0>R2
      grant 4-> 2
      grant 5 -> 2
      ?? grant 5 -> 1: inquire 2      // vydal grant R2, R2 < R1
                  yeld(2) -> 1, grant 5->1
                  proces 1 je v kritické sekci
      release 1->5, release 1->1 release 3->1
      grant(1->0)
                  proces 0 je v kritické sekci
      release 0 -> 0, release 0 -> 1, release 0 -> 2
      grant 5 -> 2 // před tím yeld, je ve ftontě
                  proces 2 je v kritické sekci
```

### Strana 51

```text
Raymondův algoritmus

■ Myšlenka
   – Jedna virtuální značka/token reprezentuje v systému
      poukázku na kritickou sekci.
   – Proces může vstoupit do kritické sekce, pokud obdrží
      token
   – Důkaz o vzájemném vyloučení procesu je triviální (token
      může držet jen jeden proces a ten jej předává, pokud
      není v kritické sekci)
```

### Strana 52

```text
Raymondův algoritmus,
inicializace      Holder=self
                  Active=false
                              1         Request_Q=()
                                        Asked=false
Holder= ?                                              Holder= ?
Active=false                                           Active=false
Request_Q=()                                           Request_Q=()
Asked=false                                            Asked=false
               2                               3




         4           5              6                     7

Holder= ?      Holder= ?          Holder= ?            Holder= ?
Active=false   Active=false       Active=false         Active=false
Request_Q=()   Request_Q=()       Request_Q=()         Request_Q=()
Asked=false    Asked=false        Asked=false          Asked=false
```

### Strana 53

```text
Raymondův algoritmus,
inicializace      Holder=self
                  Active=false
                              1         Request_Q=()
                                        Asked=false
Holder= 1                                              Holder= 1
Active=false                                           Active=false
Request_Q=()                                           Request_Q=()
Asked=false                                            Asked=false
               2                               3




         4           5              6                     7

Holder= ?      Holder= ?          Holder= ?            Holder= ?
Active=false   Active=false       Active=false         Active=false
Request_Q=()   Request_Q=()       Request_Q=()         Request_Q=()
Asked=false    Asked=false        Asked=false          Asked=false
```

### Strana 54

```text
Raymondův algoritmus,
inicializace      Holder=self
                  Active=false
                              1         Request_Q=()
                                        Asked=false
Holder= 1                                              Holder= 1
Active=false                                           Active=false
Request_Q=()                                           Request_Q=()
Asked=false                                            Asked=false
               2                               3




         4           5              6                     7

Holder= 2      Holder= 2          Holder= 3            Holder= 3
Active=false   Active=false       Active=false         Active=false
Request_Q=()   Request_Q=()       Request_Q=()         Request_Q=()
Asked=false    Asked=false        Asked=false          Asked=false
```

### Strana 55

```text
Raymondův algoritmus

■ Proces je povinen předat token žádajícímu procesu, pokud jej
  drží, pokud jej právě nepoužívá a pokud takový požadavek je
  (včetně sebe, pak pouze zahájí používání kritické sekce)
  ASSIGN-PRIVILEGE:
  if HOLDER = self and not USING and REQUEST-Q # empty
      then
        HOLDER := dequeue (REQUEST-Q)
        ASKED := false
        if HOLDER = self
            then
               USING := true (initiate entry into critical section)
            else
               send PRIVILEGE to HOLDER
```

### Strana 56

```text
Raymondův algoritmus

■ Agent, pokud chce přístup do kritické sekce, vloží hodnotu
  ‘self’ do Request_q
■ Agent odešle požadavek, pokud je žádán procesem (včetně
  sebe) o token, a nemá poznačeno, že si již ve směru ‘Holder’
  zažádal
   MAKE- REQUEST:
   if HOLDER # self and REQUEST-Q # empty and not ASKED
       then
         send REQUEST to HOLDER
         ASKED := true
```

### Strana 57

```text
Raymondův algoritmus
                                        Holder=self
                                        Active=true
                              1         Request_Q=()
                                        Asked=false
Holder=1                                               Holder=1
Active=false                                           Active=false
Request_Q=()                                           Request_Q=()
Asked=false                                            Asked=false
               2                               3




         4           5              6                     7

Holder=2       Holder=2           Holder=3             Holder=3
Active=false   Active=false       Active=false         Active=false
Request_Q=()   Request_Q=()       Request_Q=()         Request_Q=()
Asked=false    Asked=false        Asked=false          Asked=false
```

### Strana 58

```text
Raymondův algoritmus
                                      Holder=self
                                      Active=false
                            1         Request_Q=()
                                      Asked=false
Holder=1                                             Holder=1
Active=false                                         Active=false
Request_Q=()                                         Request_Q=()
Asked=false                                          Asked=false
               2                             3




         4           5            6                     7

Holder=2       Holder=2         Holder=3             Holder=3
Active=false   Active=false     Active=false         Active=false
Request_Q=()   Request_Q=(self) Request_Q=()         Request_Q=()
Asked=false    Asked= false     Asked=false          Asked=false
```

### Strana 59

```text
Raymondův algoritmus
                                       Holder=self
                                       Active=false
                               1       Request_Q=()
                                       Asked=false
Holder=1                                              Holder=1
Active=false                                          Active=false
Request_Q=()                                          Request_Q=()
Asked=false                                           Asked=false
               2                              3

                         Req


         4           5             6                     7

Holder=2       Holder=2         Holder=3              Holder=3
Active=false   Active=false     Active=false          Active=false
Request_Q=()   Request_Q=(self) Request_Q=()          Request_Q=()
Asked=false    Asked= true      Asked=false           Asked=false
```

### Strana 60

```text
Raymondův algoritmus
                                       Holder=self
                                       Active=false
                             1         Request_Q=()
                                       Asked=false
Holder=1                                              Holder=1
Active=false                                          Active=false
Request_Q=(5)                                         Request_Q=()
Asked=false                                           Asked=false
                2                             3




         4            5            6                     7

Holder=2        Holder=2         Holder=3             Holder=3
Active=false    Active=false     Active=false         Active=false
Request_Q=()    Request_Q=(self) Request_Q=()         Request_Q=(self)
Asked=false     Asked= true      Asked=false          Asked=false
```

### Strana 61

```text
Raymondův algoritmus
                                       Holder=self
                                       Active=false
                             1         Request_Q=()
                                       Asked=false
Holder=1                                              Holder=1
                Req
Active=false                                          Active=false
Request_Q=(5)                                         Request_Q=()
Asked=true                                            Asked=false
                2                             3
                                                             Req



         4            5            6                     7

Holder=2        Holder=2         Holder=3             Holder=3
Active=false    Active=false     Active=false         Active=false
Request_Q=()    Request_Q=(self) Request_Q=()         Request_Q=(self)
Asked=false     Asked= true      Asked=false          Asked=true
```

### Strana 62

```text
Raymondův algoritmus
                                       Holder=self
                                       Active=false
                             1         Request_Q=(2)
                                       Asked=false
Holder=1                                            Holder=1
Active=false                                        Active=false
Request_Q=(5)                                       Request_Q=(7)
Asked=true                                          Asked=false
                2                              3




         4            5            6                   7

Holder=2        Holder=2         Holder=3           Holder=3
Active=false    Active=false     Active=false       Active=false
Request_Q=()    Request_Q=(self) Request_Q=()       Request_Q=(self)
Asked=false     Asked= true      Asked=false        Asked=true
```

### Strana 63

```text
Raymondův algoritmus
                                          Holder=2
                                          Active=false
                                1         Request_Q=()
                                          Asked=false
Holder=1        Privilege                                Holder=1
Active=false                                   Req       Active=false
Request_Q=(5)                                            Request_Q=(7)
Asked=true                                               Asked=true
                  2                              3




         4                  5         6                     7

Holder=2           Holder=2         Holder=3             Holder=3
Active=false       Active=false     Active=false         Active=false
Request_Q=()       Request_Q=(self) Request_Q=()         Request_Q=(self)
Asked=false        Asked= true      Asked=false          Asked=true
```

### Strana 64

```text
Raymondův algoritmus
                                       Holder=2
                                       Active=false
                             1         Request_Q=(3)
                                       Asked=false
Holder=self                                         Holder=1
Active=false                                        Active=false
Request_Q=(5)                                       Request_Q=(7)
Asked=true                                          Asked=true
                2                              3




         4            5            6                   7

Holder=2        Holder=2         Holder=3           Holder=3
Active=false    Active=false     Active=false       Active=false
Request_Q=()    Request_Q=(self) Request_Q=()       Request_Q=(self)
Asked=false     Asked= true      Asked=false        Asked=true
```

### Strana 65

```text
Raymondův algoritmus
                                         Holder=2
                                         Active=false
                                 1       Request_Q=(3)
                                         Asked=true
Holder=5           Req                                Holder=1
Active=false                                          Active=false
Request_Q=()                                          Request_Q=(7)
Asked=false                                           Asked=true
               2                                 3
                         Privilege



         4               5           6                   7

Holder=2       Holder=2         Holder=3              Holder=3
Active=false   Active=false     Active=false          Active=false
Request_Q=()   Request_Q=(self) Request_Q=()          Request_Q=(self)
Asked=false    Asked= true      Asked=false           Asked=true
```

### Strana 66

```text
Raymondův algoritmus
                                       Holder=2
                                       Active=false
                             1         Request_Q=(3)
                                       Asked=true
Holder=5                                            Holder=1
Active=false                                        Active=false
Request_Q=(1)                                       Request_Q=(7)
Asked=false                                         Asked=true
                2                              3




         4            5            6                   7

Holder=2        Holder=self      Holder=3           Holder=3
Active=false    Active=false     Active=false       Active=false
Request_Q=()    Request_Q=(self) Request_Q=()       Request_Q=(self)
Asked=false     Asked= true      Asked=false        Asked=true
```

### Strana 67

```text
Raymondův algoritmus
                                         Holder=2
                                         Active=false
                               1         Request_Q=(3)
                                         Asked=true
Holder=5                                              Holder=1
Active=false                                          Active=false
Request_Q=(1)                                         Request_Q=(7)
Asked=true                                            Asked=true
                2                                3
                      Req



         4            5              6                   7

Holder=2        Holder=self        Holder=3           Holder=3
Active=false    Active=true        Active=false       Active=false
Request_Q=()    Request_Q=()       Request_Q=()       Request_Q=(self)
Asked=false     Asked= false       Asked=false        Asked=true
```

### Strana 68

```text
Raymondův algoritmus
                                          Holder=2
                                          Active=false
                                1         Request_Q=(3)
                                          Asked=true
Holder=5                                               Holder=1
Active=false                                           Active=false
Request_Q=(1)                                          Request_Q=(7)
Asked=true                                             Asked=true
                2                                 3




         4            5               6                   7

Holder=2        Holder=self         Holder=3           Holder=3
Active=false    Active=true         Active=false       Active=false
Request_Q=()    Request_Q=(2)       Request_Q=()       Request_Q=(self)
Asked=false     Asked= false        Asked=false        Asked=true
```

### Strana 69

```text
Raymondův algoritmus,
zhodnocení
■ Vlastnosti
   – (+) Nezpůsobuje vyhladovění
   – (+) Nezpůsobuje uváznutí
   – (+) Fault tolerance
   – (-) Přerušení jednoho komunikačního kanálů může
       odpojit i všechny procesy (konektivita = 1)
```

### Strana 70

```text
Analýza Raymondova
algoritmu
■ Počet zaslaných zpráv – třída složitosti O(lg N)
■ Průměrné synchronizační zpoždění je lg N/2
■ Přenosnost se snižuje při zahlcení sítě zprávami
■ Může použít greedy strategii - možnost hladovění
```

### Strana 71

```text
Suzuki – Kasami vysílací
algoritmus
■   Token obsahuje frontu procesů a pole čítačů LN[i], v tomto poli je
    uvedeno, kolikrát byl token kterému procesu přidělen
■   Každý uzel i také udržuje pole čítačů Ri[i] pro každý proces, což značí, že
    na každém procesu je uloženo, kolikrát který proces o token žádal
■   Uzel vyžadující vstup do kritické sekce, tedy uzel i, se snaží získat token.
    Zvýší svůj čítač ve svém poli a rozešle zprávu všem ostatním
■   Každý proces si upraví čítač u daného procesu (po obdržení zprávy) na
    výšší číslo ze svého aktuálního čítače a čítače ve zprávě – pro vyřešení
    případných zpožděných zpráv.
■   Proces, který má volný token, nebo ho právě uvolnil, zkontroluje svoje
    čítače, a všechny čítače, které mají o jedna větší číslo a nejsou ve frontě
    tokenu do této fronty umístí. Následně pošle token prvnímu procesu z
    fronty a ten z fronty odstraní
```

### Strana 72

```text
  Suzuki – Kasami vysílací
  algoritmus
                                              V systému je pět plně propojených
                  [0,0,0,0,0]
                          [0,0,0,0,0]
                                              procesů. Proces 1 drží token.
                     1

[0,0,0,0,0]                     [0,0,0,0,0]
    2                               5




              3            4
         [0,0,0,0,0] [0,0,0,0,0]
```

### Strana 73

```text
  Suzuki – Kasami vysílací
  algoritmus
                                                       Proces 3 zažádá o token, protože
                    [0,0,0,0,0]
                                 [0,0,0,0,0]
                                                       chce vstoupit do kritické sekce
                         1

[0,0,0,0,0]                              [0,0,0,0,0]
                (3,1)
    2                                       5
                             (3,1)
        (3,1)

                        (3,1)
                3                    4
            [0,0,1,0,0] [0,0,0,0,0]
```

### Strana 74

```text
  Suzuki – Kasami vysílací
  algoritmus
                                                 Procesy 1,2 a 5 zprávu zpracují.
                  [0,0,1,0,0]
                                                 Proces jedna drží token,
                     1                           nepotřebuje jej a jelikož je třetí
                                                 proces jediným, jehož hodnota v
[0,0,1,0,0]                        [0,0,1,0,0]   čítači je větší, než hodnota v čítači
    2                                 5          tokenu, zašle jej tomuto procesu
                     [0,0,0,0,0]



                    (3,1)
              3             4
         [0,0,1,0,0] [0,0,0,0,0]
```

### Strana 75

```text
  Suzuki – Kasami vysílací
  algoritmus
                                                 Proces 3 se nachází v kritické
                     [0,0,1,0,0]
                                                 sekci. Proces 4 také zpracoval
                         1                       zprávu a upravil si patřičně svůj
             (2,1)                               čítač. V ten samý okamžik žádá o
[0,0,1,0,0]                        [0,0,1,0,0]   token proces 2. Vyšle všem zprávu,
                     (2,1)
    2                                 5          že žádá poprvé a je odložen,
                                                 čekajíc na token.
    (2,1)            (2,1)

              [0,0,0,0,0]

                 3            4
            [0,0,1,0,0] [0,0,1,0,0]
```

### Strana 76

```text
  Suzuki – Kasami vysílací
  algoritmus
                                                                   Všechny procesy až na pátý si
                      [0,1,1,0,0]
                                                                   zpracují žádost od druhého
                              1                                    procesu, upraví své čítače a jelikož
                                             (5,1)                 proces 3 dokončil svoji činnost v
[0,1,1,0,0]          (5,1)
                                     (4,1)           [0,0,1,0,0]   kritické sekci, posílá token
    2                  (2,1)                            5          jedinému procesu, o kterém ví, že
                                                                   jeho počet žádostí je vyšší, než je v
                  (4,1)        (5,1)
              [0,0,1,0,0]
                                              (5,1)                tokenu uložený jeho počet přidělení
                                                       (4,1)
                                                                   tomuto procesu. Zároveň ale žádají
                                                                   procesy 4 a 5 o token. Procesu 5
                 3           (4,1)
                                             4                     stále nedorazila první žádost od
         [0,1,1,0,0] [0,1,1,0,0]                                   procesu 2.
```

### Strana 77

```text
    Suzuki – Kasami vysílací
    algoritmus
                                                    Proces 2 si užívá kritické sekce,
                      [0,1,1,1,1]
                                                    procesy 4 a 5 čekají na token a
                              1                     zpráva uzlu pět od uzlu nebyla
                                                    stále doručena, přestože již žádající
 [0,1,1,1,1]                          [0,0,1,1,1]   uzel token má!
                      (2,1)
       2                                 5
[0,0,1,0,0]



                  3               4
              [0,1,1,1,1] [0,1,1,1,1]
```

### Strana 78

```text
  Suzuki – Kasami vysílací
  algoritmus
                                                   Stále máme jednu starou bloudící
                       [0,1,1,1,1]
                                                   zprávu v systému. Proces dva
                            1                      dokončil svoji činnost v kritické
                                                   sekci a zjistil, že hned dva uzly
[0,1,1,1,1]                          [0,0,1,1,1]   čekají na token, protože v čítači
                    (2,1)
    2                                   5          vidí, že mají vyšší počet žádostí,
                                                   než je počet přidělení v záznamech
                                                   tokenu. Vybere jeden, například
   [0,1,1,0,0], [p5|                               čtvrtý, tomu pošle token a pátý
                                                   proces umístí do frontu tokenu.
                3               4
          [0,1,1,1,1] [0,1,1,1,1]
```

### Strana 79

```text
  Suzuki – Kasami vysílací
  algoritmus
                                                            Proces 4 je v kritické sekci a
                         [0,1,1,1,1]
                                                            proces 2 znovu žádá o vstup do
                 (2,2)
                             1                              této sekce. Pošle patřičné zprávy.

[0,1,1,1,1]                             [0,0,1,1,1]
                         (2,2)
    2                    (2,1)              5

                            (2,2)
        (2,2)


                     3              4   [0,1,1,0,0], [p5|
                [0,1,1,1,1] [0,1,1,1,1]
```

### Strana 80

```text
  Suzuki – Kasami vysílací
  algoritmus
                                                Ty jsou zpracovány všemi procesy, i
                  [0,2,1,1,1]
                                                pátým, kterému nedošla první
                      1                         žádost od dvojky. Proces 4 opustil
                                                kritickou sekci a posílá dále token
[0,2,1,1,1]                     [0,2,1,1,1]     procesu uloženému na čele frontu
    2             (2,1)            5            procesů tokenu. Stejně by v tomto
                                                případě zjistil, že pětka čeká na
                                                token na základě čítače, ale díky
                                                frontě by věděla o žádosti pětky, i
                                  [0,1,1,1,0]
                                                kdyby od ní nebyla zde žádost ještě
              3            4                    zpracována.
         [0,2,1,1,1] [0,2,1,1,1]
```

### Strana 81

```text
  Suzuki – Kasami vysílací
  algoritmus
                                                     Proces 5 obdrží token a vstupuje
                  [0,2,1,1,1]
                                                     do kritické sekce. Také konečně
                     1                               dorazila první zpráva od procesu 2.
                                                     Ta ale neupraví čítač, protože ten je
[0,2,1,1,1]                     [0,2,1,1,1]          Již pro proces 2 u procesu 5
    2                              5                 nastaven na aktuální hodnotu 2.
                                                     Pokud by v době, kdy proces 2
                                       [0,1,1,1,0]
                                                     žádal poprvé byl token na uzlu 5,
                                                     pak by nebyl kvůli zdržení zprávy
                                                     odeslán.
              3            4
         [0,2,1,1,1] [0,2,1,1,1]
```

### Strana 82

```text
Analýza

■ Počet zpráv pro jeden vstup do kritické sekce 𝑂(𝑁)
■ Zaručeno vzájemné vyloučení a bez možnosti uváznutí a
  vyhladovění
■ Díky frontě požadavků garantována férovost
```

### Strana 83

```text
DETEKCE UKONČENÍ
```

### Strana 84

```text
Detekce ukončení běhu v
distribuovaném systému
■ V systému se nachází n procesů, které komunikují
  předáváním zpráv
■ Pokud neuvedeme jinak, předpokládáme plné propojení
  procesů komunikačními kanály
■ Procesy komunikují s různou dobou zpoždění v přenášení
  zpráv.
■ Detekce ukončení musí být schopna nalézt stav, ve kterém již
  není žádná zpráva přenášena nějakým kanálem a nikdy v
  budoucnu pro tento běh ani nebude (stabilní vlastnost).
```

### Strana 85

```text
Atomický model
komunikujících procesů
■ Komunikace je zahájena jedním procesem
■ Pokud proces obdrží zprávu, může odeslat atomicky zprávy
  ostatním procesům
■ Pokud v systému není žádná zpráva, je běh systému ukončen
```

### Strana 86

```text
Algoritmus čtyř čítačů

■ Myšlenka je založena na kauzalitě odesílané a přijímané
  zprávy
■ Pokud v nějakém čase t1 obdrží pozorovatel od všech procesů
  počet přijatých zpráv a poté se dotáže na počet odeslaných
  zpráv => pokud se v odpovědi v čase t2 tyto počty rovnají,
  musely v okamžiku ukončení odpovědi na první dotaz být
  obdrženy všechny odeslané zprávy
   – Pokud by v čase t1 nějaká dříve odeslaná zpráva ještě
       nebyla doručena, musí být zahrnuta v oznámených
       odeslaných zprávách v čase t2
```

### Strana 87

```text
Algoritmus čtyř čítačů

Při přijetí zprávy
          recvi=recvi+1
          sendi=sendi+x (x je počet zpráv odeslaných od
          přijetí poslední zprávy doposud)
Při odeslání zprávy


Detekce ukončení
       loop
              dotaz všem procesům na počet přijetí a
                    odeslání zpráv
              po obdržení všech odpovědí
              R2 = suma všech avizovaných přijatých zpráv
              S2 = suma všech avizovaných odeslaných zpráv
              pokud R1 = S2, došlo v řezu k přijetí všech
              odeslaných zpráv (detekce ukončení), jinak
               R1 = R2 , S2 = S1
```

### Strana 88

```text
Algoritmus čtyř čítačů

 p1
 p2
 p3

pozorovatel
                                 t1      t2                             t3
V čase t1 pozorovatel zjistí (minimálně kolik) S1 a R1
V čase t3 pozorovatel zjistí (minimálně kolik) S2 a R2
S2 jistě zahrnuje zprávy odeslané před t2
R1 jistě nezahrnuje zprávy přijaté po t2
Pokud R1 = S2, pak v čase t2 byly všechny komunikační kanály prázdné (všech
R1 = S2 zpráv bylo přijato před t2 a muselo být i odesláno před ---t2) → detekce
ukončení před časem t2 dle předpokladů

R* >= R1 = S2 >= S*, tedy R* >= S*, ale podle kauzality R*=S* v čase t 2
R* a S* je skutečný počet přijatých a odeslaných zpráv před časem t 2
```

### Strana 89

```text
Algoritmus čtyř čítačů, příklad
p1    t1                                t2

p2
p3                                                                  R1=3, S1=3
                                                                    R2=5, S2=5


               (0,0)   (1,1) (2,2)            (2,1)   (1,2) (2,2)
pozorovatel
p1              t1                      t2

p2
p3                                                                  R1=5, S1=5
                                                                    R2=5, S2=5


                       (2,1)    (1,2) (2,2)   (2,1)   (1,2) (2,2)
 pozorovatel
```

### Strana 90

```text
Řez procesů (obecně)
■ Pro každou událost e v řezu C je každá událost f, která
  kauzálně předchází události e také v řezu C



     p1
     p2
     p3

     p4
```

### Strana 91

```text
Detekce ukončení, vektor
■ Pro n procesů p1, p2 … pnmáme token s vektorem [m1,m2 … mn]
■ Token se postupně předává po jednotlivých procesech
■ Pokud process obdrží token, pak rj je počet zpráv, které obdržel
  od procesu i od posledního držení tokenu a si počet zpráv, které
  od té doby procesu i odeslal
■ Ve vektoru sníží hodnotu u procesu, od kterých přijal zprávy o ri a
  u sebe zvýší hodnotu o si
```

### Strana 92

```text
     Vektorový algoritmus, příklad

                                                                                                t1=(0,0,1,0,0,0)
p1     t1                            t7                               t13
                                                                                                t2=(0,0,1,0,0,0)
                                                                                                t3=(0,1,0,0,0,1)
p2          t2                            t8                                t14
                                                                                                t4=(0,1,0,0,0,1)
                                                                                                t5=(0,1,0,0,0,1)
p3               t3                            t9                                 t15           t6=(1,1,0,1,0,0)
                                                                                                t7=(1,1,0,1,0,0)
p4                    t4                            t10                             t16
                                                                                                t8=(1,0,0,1,1,0)
                                                                                                t9=(1,0,0,1,1,1)
p5                         t5                             t11                             t17
                                                                                                t10=(1,1,0,0,1,1)
                                                                                                t11=(1,1,0,0,1,1)
p6                              t6                              t12                             t12=(1,1,0,0,1,0)
                                                                                                t13=(0,1,0,0,1,0)
                                                                                                t14=(0,0,0,0,1,0)
                                                                                                t15=(0,0,0,0,1,0)
                                                                                                t16=(0,0,0,0,1,0)
                                                                                                t17=(0,0,0,0,0,0)
```

### Strana 93

```text
     Vektorový algoritmus, příklad
                                                                Řez
                                                                                                t1=(0,0,1,0,0,0)
p1     t1                            t7                               t13
                                                                                                t2=(0,0,1,0,0,0)
                                                                                                t3=(0,1,0,0,0,1)
p2          t2                            t8                                t14
                                                                                                t4=(0,1,0,0,0,1)
                                                                                                t5=(0,1,0,0,0,1)
p3               t3                            t9                                 t15           t6=(1,1,0,1,0,0)
                                                                                                t7=(1,1,0,1,0,0)
p4                    t4                            t10                             t16
                                                                                                t8=(1,0,0,1,1,0)
                                                                                                t9=(1,0,0,1,1,1)
p5                         t5                             t11                             t17
                                                                                                t10=(1,1,0,0,1,1)
                                                                                                t11=(1,1,0,0,1,1)
p6                              t6                              t12                             t12=(1,1,0,0,1,0)
                                                                                                t13=(0,1,0,0,1,0)
                                                                                                t14=(0,0,0,0,1,0)
                                                                                                t15=(0,0,0,0,1,0)
                                                                                                t16=(0,0,0,0,1,0)
                                                                                                t17=(0,0,0,0,0,0)
```

### Strana 94

```text
Detekce ukončení,
diseminační procesy
■ Komunikace je zahájena jedním procesem
■ Ostatní procesy začínají v klidovém stavu
■ Pokud proces obdrží zprávu, může
   – provádět (tichou činnost)
   – odesílat zprávy ostatním procesům
   – přejít do klidového stavu
■ Pokud v systému není žádná zpráva a všechny procesy jsou v
  klidovém stavu, je běh systému ukončen
```

### Strana 95

```text
Použítí kostry grafu
komunikace, pseudokód
Při přijetí zprávy receive(pi,pj,m) procesem pi od
procesu pj
     stavi =aktivni
     if(predeki=null) then
           predeki=pj
     else
           send(pi,pj,ACK)
Při přechodu do nečinnosti
     stavi=pasivni
     if(deficit=0)
           send(pi,predek,ACK)
           predek=null
Při odeslání zprávy send(pi,pj,m)
     deficit++
Při přijetí zprávy receive(pj,pi,ACK)
     deficit--
     if(deficit=0)&(stav=pasivni)
           send(pi,predek,ACK)
           predek=null
```

### Strana 96

```text
        α                           α                            α                       α

    1   2     3         1           2       3            1       2       3       1       2     3
                                                         ACK

                    5           3            6       5       3           6   5                 6



        α                               α                    α                             α
                            ACK             ACK

    1   2     3             1           2        3           2                             2
                                                                                     ACK
ACK           ACK
                                                         3           5               3             5
5             6


                                        α                      α             α                 α
        α                                                    ACK


        2                               2                      2                         UKONČENÍ
            ACK
              5
```

### Strana 97

```text
NEKOREKTNÍ
   PROCESY
```

### Strana 98

```text
 Asynchronní / Synchronní
 distribuovaný systém
Asynchronní systém (Model reálného světa)
• V systému neexistuje žádná pevná horní mez Δ pro doručení zprávy.
  Zpráva může dorazit za milisekundu, za hodinu …
• Standardní model pro internet, cloudy a většinu distribuovaných aplikací –
  síť je nepředvídatelná.
• Zprávy se mohou předbíhat (zpráva B odeslaná po zprávě A může dorazit
  dříve), mohou se ztratit nebo být duplikovány
Synchronní systém
• Definuje existenci horní meze Δ (latence). To znamená, že máme
  matematickou jistotu, že zpráva vždy dorazí do určitého času.
• Klíčový předpoklad pro řešitelnost konsenzu. V reálném světě
  (asynchronní systémy) tento předpoklad neplatí, proto jej simulujeme
  pomocí Failure Detectorů
Částečně synchronní systém
• Na počátku asynchronní systém se po čase se systém ustálí do
   synchronního stavu
```

### Strana 99

```text
Abstrakce a Modely Selhání
Abstrakce chování procesu (Co se s ním stane?)
•   Crash & Stop (Havárie a zastavení): Proces přestane fungovat a nikdy se neobnoví.
•   Crash & Recovery (Havárie a obnova): Proces selže, ale po čase se obnoví a pokračuje.
    Musí mít přístup k perzistentní pamětii k obnově stavu.
•   Byzantine (Byzantské selhání): Libovolné chování. Proces může odesílat špatná data,
    lhát nebo se chovat škodlivě. Nejtěžší model na řešení.
Abstrakce observace systému (Jak selhání vidíme?)
•   Fail-Silent: Při selhání proces prostě zmlkne. Ostatní procesy to nemohou spolehlivě
    odlišit od pomalé sítě bez použití timeoutů (často vede k nutnosti eventual consistency
    modelů).
•   Fail-Stop (vyžaduje Perfect Failure Detector): Selhání je okamžitě a spolehlivě
    detekováno všemi ostatními. Ostatní procesy vědí, že daný proces selhal a už se
    nevrátí.
•   Fail-Noisy: Ostatní procesy jsou informovány o selhání (např. obdrží signál nebo vyprší
    spolehlivý timeout), ale detekce může mít zpoždění nebo být dočasně nepřesná
    (falešná pozitiva, je podezírán se selhání proces, který se jen opozdil).
```

### Strana 100

```text
Detekce selhání, požadavky
■ Pro model crash-stop abstrakci a synchronní distribuovaný
  systém máme perfektní detektor selhání
■ Vlastnosti
        ■   Silná úplnost (Strong completeness): Eventuálně (dříve
            nebo později) je každý selhaný proces permantně
            detekován
        ■   Silná přesnost (Strong accuracy): pokud je proces
            detekován jako selhaný, tak selhal
■ Pro model crash-stop a částečně synchronní distribuovaný
  systém máme eventuálně perfektní detektor selhání
        ■   Silná úplnost
        ■   Eventuálně silná přesnost (Eventual strong accuracy):
            Eventuálně žádný korektní proces není podezřívaný jako
            selhaný
```

### Strana 101

```text
Detekce selhání, perfektní detektor
selhání P
                                                Proces neposlal
upon event <P,Init> do                          HeartbeatReply a ani
      active:=П;                                není mezi dříve
      detected:=0;
                                                detekovanými
      start_timer();
                                                Signalizujeme, že daný
upon event (Timeout) do
      forall 𝑝 ∈ Π                              proces (asi) selhal
       if(𝑝 ∉ 𝑎𝑙𝑖𝑣𝑒) ∧ (𝑝 ∉ 𝑑𝑒𝑡𝑒𝑐𝑡𝑒𝑑) then      (v systému může být
              𝑑𝑒𝑡𝑒𝑐𝑡𝑒𝑑= 𝑑𝑒𝑡𝑒𝑐𝑡𝑒𝑑 ∪ p ;          obsluha této události)
              trigger<P,Crash|p>;
       trigger<send|p,[HeartbeatRequest]>;      Každému, i domněle
      alive:=0;                                 selhanému procesu
      start_timer();                            pošleme žádost o
                                                heartbeat
upon event <deliver, q,[HeartbeatRequest]> do
      trigger <send | q,[HearbeatReply]>        Začneme novou
                                                etapu, žádný proces
upon event <deliver | p,[ HeartbeatReply]> do   není považován teď za
      𝑎𝑐𝑡𝑖𝑣𝑒:= active ∪ p
                                                živý
```

### Strana 102

```text
Detekce selhání, nakonec
perfektní detektor selhání
■ Procesy, které se odmlčí, nakonec obnoví svoji činnost
■ Po ukončení čekání jsou procesy považovány buď za živé,
  pokud odpověděly, nebo podezřelé – generuje událost
  < ◊𝑃, 𝑆𝑢𝑠𝑝𝑒𝑐𝑡| 𝑝 >
■ Pokud nějaký podezřelý proces se ozve později
   – je odstraněn z množiny podezřelých
   – zvětší se interval čekání (pravděpodobně nebyl
      dostatečný)
   – generuje se událost < ◊𝑃, 𝑅𝑒𝑠𝑡𝑜𝑟𝑒| 𝑝 >
```

### Strana 103

```text
Detekce selhání, nakonec
perfektní detektor selhání
  upon event <◊P,Init> do
          active:=П; suspected:=0;
          delay:=Δ;
          start_timer(delay);

  upon event (Timeout) do
          if(𝑎𝑙𝑖𝑣𝑒 ∩ 𝑠𝑢𝑠𝑝𝑒𝑐𝑡𝑒𝑑 ≠ 0) then
                    delay:=delay+ Δ;
          forall 𝑝 ∈ Π
                    if(𝑝 ∉ 𝑎𝑙𝑖𝑣𝑒) ∧ (𝑝 ∉ 𝑠𝑢𝑠𝑝𝑒𝑐𝑡𝑒𝑑) then
                              suspected= suspected ∪ p ;
                              trigger< ◊P, Suspect|p>;
                    else if(𝑝 ∈ 𝑎𝑙𝑣𝑒) ∧ (𝑝 ∈ 𝑠𝑢𝑠𝑝𝑒𝑐𝑡𝑒𝑑) then
                              suspected= suspected − p ;
                              trigger< ◊P, Restore|p>;
                    trigger<send|p,[HeartbeatRequest]>;
          alive:=0;
          start_timer(delay);

  upon event <deliver, q,[ HeartbeatRequest]> do
          trigger <Send, q,[HearbearReply]>

  upon event <deliver, p,[ HeartbeatReply]> do
          𝑎𝑐𝑡𝑖𝑣𝑒:= active ∪ p
```

### Strana 104

```text
Detekce selhání, nakonec
perfektní detektor selhání
     Δ
                             P1
                             P2
                             P3
                             P4




                         Detektor
  TIMEOUT
  active={p2,p4}
  suspected={p1,p3}
```

### Strana 105

```text
Detekce selhání, nakonec
perfektní detektor selhání
    Δ
                             P1
                             P2
                             P3
                             P4




                         Detektor
    active={p1}
    suspected={p1,p3}
```

### Strana 106

```text
Detekce selhání, eventuálně
perfektní detektor selhání
    Δ      Δ
                                   P1
                                   P2
                                   P3
                                   P4




                                 Detektor
        active={p2,p4,p1}
        suspected={p1,p3}
        (𝑎𝑙𝑣𝑒 ∩ 𝑠𝑢𝑠𝑝𝑒𝑐𝑡𝑒𝑑 ≠ 0)
```

### Strana 107

```text
Detekce selhání, eventuálně
perfektní detektor selhání
    Δ   Δ   2Δ
                                  P1
                                  P2
                                  P3
                                  P4




                                Detektor
            active={p2,p4,p1}
            suspected={p3}
```

### Strana 108

```text
Detekce selhání, eventuálně
perfektní detektor selhání
    Δ   Δ   2Δ    2Δ
                                 P1
                                 P2
                                 P3
                                 P4




                              Detektor
                 active={p1,p2,p3,p4}
                 suspected={p3}
                 (𝑎𝑙𝑣𝑒 ∩ 𝑠𝑢𝑠𝑝𝑒𝑐𝑡𝑒𝑑 ≠ 0)
                 … příště 3Δ
```

### Strana 109

```text
Volba lídra - v Monarchickém systému
/ Eventual Leader Detector Ω
■ Lze použít i pro crash-recovery abstrakce procesů
■ Udržuje množinu podezřelých procesů, které v daném
  čase neodpověděli a na základě této množiny volí lídra
■ Vládne (a je mu důvěřováno) živý process (Monarcha),
  resp. process nepodezíraný z neživosti, s největší prioritou

upon event <Ω,Init> do
       suspected:=0
       leader:=0
upon event <◊P, Suspect|p> do
       suspected := suspected ∪ p
upon event <◊P, Restore|p > do
       suspected := suspected \ p
upon leader ≠ maxrank(Π \ suspected) do
       leader := maxrank(Π \ suspected)
       trigger< Ω , Trust | leader>;
```

### Strana 110

```text
Nakonec perfektní detektor
selhání Ω
■   Předpokládá se, že existuje aspoň jeden proces, který nikdy neselže, nebo někdy
    selhává, ale po čase a zotavení již nikdy neselže
■   Tento proces je vybrán algoritmem, který si počítá epochy, ve kterých byl aktivní
      –    Při inicializaci se epocha nastaví na 1 (a uloži se, aby byla dostupná při zotavení
           se procesu)
      –    Při obnovení po pádu procesu se epocha inkrementuje o jedna
upon event <Ω,Init> do
        epoch := 0; sotre(epoch); candidates :=0;
        trigger< Ω, Recovery>
// událost Recovery nastává i při zotavení
upon event <Ω,Recovery> do
        leader:=maxrank(Π);
        trigger< Ω, Trust | Leader>
        delay:= Δ;
        retrieve(epoch); epoch:=epoch+1; store(epoch);
        forall p ∈ Π trigger< Send | p,[HEARTBEAT, epoch] >;
        candidates:=0;
        start_timer(delay);
```

### Strana 111

```text
Nakonec perfektní detektor
selhání Ω
■   V každém cyklu je procesem za lídra označen proces, který má odpověděl
    v nastaveném intervalu, a má nejmenší počet epoch (selhal nejméněkrát).
    Pokud je více takových, volí se podle ranku (provede select)
■   Pokud se lídr změnil od minulého kola je nový lídr avizován událostí
       < Ω , Trust | leader> a je zvýšen delay o hodnotu Δ
upon event <Timeout> do
        newleader:=select(candidates);
        if newleader≠leader then
                delay:=delay+ Δ;
                leader:=newleader;
                trigger< Ω, Trust | Leader>
        forall p ∈ Π trigger< Send | p,[HEARTBEAT, epoch] >;
        candidates:=0;
                start_timer(delay);

upon event <Deliver, q, [HEARTBEAT, ep] > do
        if (s,e) ∈ candidates & s=q & e<ep then
                   candidates:=(candidates – (q,e)) U (q,ep)
```

### Strana 112

```text
     Volba lídra pro částečně synchronní
     distribuovaný systém, příklad
𝑃1

𝑃2

𝑃3

𝑃4

     t1      t2           t3           t4 t5                      t6

(t1,t2): candidates= ((P1,0), (P2,0), (P3,0), (P4.0)) / ((P1,0), (P3,0), (P4.0)) /((P1,0), (P2,1), (P3,0), (P4.0))
(t2,t3): candidates= ((P2,1), (P3,0), (P4.0)) / ((P3,0), (P4.0))
(t3,t4): candidates= ((P4.0)) / ((P2,2), (P4.0)) / ((P2,2), (P3,1), (P4.0))
(t4,t5): candidates= ((P2,2), (P3,1))
(t5,t6): candidates= ((P1,1), (P2,2), (P3,1)) / ((P1,1), (P3,1)) / ((P1,1), (P3,1), (P4,1)) /
                                             ((P1,1), (P2,3), (P3,1), (P4,1)) / ((P1,1), (P2,3), (P4,1))
(t6,t+): candidates= ((P2,3), (P4,1)) / ((P2,3), (P3,2), (P4,1)) / ((P1,2), (P2,3), (P3,2), (P4,1)) /
                                             ((P1,2), (P3,2), (P4,1)) / ((P1,2), (P2,4), (P3,2), (P4,1))
```

### Strana 113

```text
Volba lídra pro asynchronní
distribuovaný systém, vlastnosti
■ Vlastnosti
   – Nakonec přesnost (Eventual Accuracy): Po nějakém čase
       každý proces věří nějakému korektnímu procesu jako
       lídrovi
   – Nakonec shoda (Eventual Agreement): Po nějakém čase
       žádné dva procesy nevěří různým procesům jako lídrům


Systém nakonec konverguje k jedinému, permanentně korektnímu lídrovi
(bez ohledu na počáteční stav nebo přechodné chyby)

Abstrakce zotavení: Algoritmus umožňuje procesům po restartu (po pádu)
integrovat se zpět do rozhodování, aniž by byla narušena integrita lídra
```

### Strana 114

```text
Distribuovaný konsensus

■   Procesy navrhují volbu / hodnotu a kolektivně se shodnou na
    nějakém návrhu
■   Operace pro konsensus
     –   Návrh (Proposal), každý proces může vznést návrh a ten rozešle všem
         ostatním procesům
     –   Rozhodnutí (Decision), proces se rozhodl pro návrh na základě všeobecné
         shody – všechny procesy se musí shodnout na stejném návrhu

■   Vyžaduje synchronní systém, nebo částečně synchronní systém
     –   Omezené zpoždění zpráv, je garantované zpoždění do nějakého limitu Δ
     –   Omezený čas zpracování události procesem
     –   Algoritmy pracují v kolech
```

### Strana 115

```text
Distribuovaný konsensus

■ Základní požadavky
    –   Ukončení (Termination) Každý korektní proces se nakonec pro
        nějakou hodnotu rozhodne.
    –   Platnost (Validity) Pokud se proces rozhodne pro hodnotu ‚V‘, pak ‚V‘
        musela být navržena některým z procesů.
    –   Integrita (Integrity) Žádný proces se nerozhodne více než jednou.
    –   Shoda (Agreement) Žádné dva korektní procesy se nerozhodnou pro
        odlišné hodnoty.
    –   Uniformní shoda (Uniform Agreement): Žádné dva procesy se
        nerozhodnou pro odlišné hodnoty
■ Poslední vlastnost odlišuje regulérní konsensus od uniformního
  konsensu – v druhém případě je vyžadována, v prvním ne
```

### Strana 116

```text
Distribuovaný konsensus

■   Pro asynchronní systém neexistuje algoritmus pro zaručení konsensu
■   FLP Věta (Ficher, Lynche, Paterson, 1985)
       „V čistě asynchronním systému nelze dosáhnout konsensu (shody)
       deterministickým algoritmem, pokud může dojít k selhání byť jen
       jednoho jediného procesu.“
       Protože nedokážeme rozlišit mezi tím, jestli proces selhal, nebo je
       jen extrémně pomalý
■   Pokud máme algoritmus pro distribuovaný konsensus, dokážeme na
    něj převést ostatní úlohy (volba leadera, detekce chyb …)
       Jedná se o nejtěžší problém v distribuovaných systémech
```

### Strana 117

```text
Regulérní konsensus,
záplavový algoritmus
■   Algoritmus pracuje v kolech, ve kterých procesy sdílejí návrhy, které
    podaly, nebo o nich dostali zprávu od ostatních
■   Předpokládá crash-stop model selhání, selhání lze detekovat
■   Používá Best Effort všesměrové vysílání a Perfect Failure Detector →
    jeho použití zaručí shodu i pro Best Effort, jednodušší, než použít
    Reliable Broadcast
       Přenáší menší počet zpráv při jednom vysílání
       Nepřeposílá zprávy
       I neodeslané zprávy představují režii
■   Zaručuje platnost, shodu, integiritu, ukončení
```

### Strana 118

```text
Regulérní konsensus,
záplavový algoritmus
Princip:
■    Procesy si uchovávají
           seznam procesů, od kterých obdrželi zprávu v přechozím kole
           seznam procesů, od kterých obdrželi zprávu v přechozím kole
           seznam návrhů, i kterých se doslechly v aktuálním kole
■    Proces v každém kole vysílá zprávu se všemi mu známými návrhy
■    Kolo skončí pro proces v okamžiku, když obdrží zprávu od všech ostatních korektních
     procesů – nekorektní co selhaly jsou detekovány
■    Po skončení kola proces rozhodne pro nejmenší (největší) z jemu známých návrhů,
     pokud obdržel informace o návrzích od stejného počřu procesů jako v minulém kole
```

### Strana 119

```text
Regulérní konsensus, záplavový
algoritmus
Algoritmus si udržuje seznam procesů, které selhaly, dále číslo kola, zvolený návrh, pokud učinil
rozhodnutí, seznam procesů, od kterých v daném kole obdržel návrhy a všechny návrhy, které v daném
kole zaznamenal

upon event <c, init> do    // c – regulerní záplavový konsensus
   correct:=П; round:=1 decision:=nill;
   recievedFrom:=[]; proposals:=[]

Perfektní detektor v synchronním systému dokáže detekovat, že proces p nepracuje správně a pokud byl
učiněn návrh tímto procesem, vysílá tento návrh společně se všemi mu doposud známými návrhy dál
(možně jen v prvním kole

upon event <crash,p> do                         // detekováno selhání procesu p
   correct:=correct-{p};
upon event <propose,c, v> do
   proposals[1]:=proposals U {v}
     trigger<beb, broadcast | [Proposal, 1, proposals[1]]);

Pokud je mu doručen seznam návrhů od procesu proces, obojí si pro aktuální kolo zaznamená

upon event <deliver(process, [Proposal, round, ps])> do
      receivedfrom[round]:=receivedfrom[round] U {process}
      proposals[round]:=proposals[round] U ps
```

### Strana 120

```text
    Regulérní konsensus, záplavový algoritmus

■   Pokud proces obdrží v kole k odpovědi od stejné množiny procesů, jako v kole
    předchozím, má informace o všech navržených ‚aktivních‘ hodnotách
     –    Žádný proces, který postoupil do kola k neví o jiném návrhu
■   Pokud proces nebyl doposud schopen sám rozhodnout na základě shod návrhů z
    aktuálního a předchozího kola, ale jiný korektní proces již rozhodl, následuje takové
    rozhodnutí

when correct ⊆ receivedfrom[round] ∧ decision = nill
   if receivedfrom[round]=receivedfrom[round − 1]
       decision := min(proposals[round]);
        trigger<beb, broadcast([DECIDED,decision])
         trigger<c, decide(decision)>
   else round := round +1;
       trigger<beb,broadcast([PROPOSAL,round,proposals
                                               [round − 1]])
upon event deliver(p, [DECIDED,v]) do
   if p ∈ correct ∧ decision = nill then
        decision := v
        trigger<beb, broadcast([DECIDED,decision])>
       trigger<c, decide(decision)>

           Předpokládáme perfektní detektor selhání, nemůže být    Není zaručena atomicita! Decide může
           označen za korektní proces, který u tohoto broadcastu   nastat i když broadcast selže
           selal
```

### Strana 121

```text
              a         b           c        d                        a         b       c           d
             1         2            3       4                  1234           1234     1234             1234


              a         b           c        d                        a         b       c           d
 RecFrm[0] []         []        []          []          RecFrm[1] [abcd]      [abcd]   [abcd]   [abcd]
 RecFrm[1]:[abcd]     [abcd]    [abcd]      [abcd]      RecFrm[2]:[abd]       [abd]    -        [abd]
 Correct: [abcd]      [abcd]    [abcd]      [abcd]      Correct: [abd]        [abd]    -        [abd]
 proposals:[1234]     [1234]    [1234]      [1234]      proposals:[1234]      [1234]   -        [1234]


                                                                          a     b       c       d
                  a        b            c    d
                       1234                                  Decide(1)                              1234
           1234                                  1234

                                                                          a     b       c       d
                  a        b            c    d
 RecFrm[2] [abd]      [abd]     -           [abd]         Decide         1      -       -       1
 RecFrm[3]:[abd]      -         -           [ad]
 Correct: [abd]       -         -           [ad]
 proposals:[1234]     -         -           [1234]


a doručí od b dříve než detekuje jeho selhání ->          d obdrží informaci, že a rozhodl a rozhodnutí
učini rozhodnutí                                          následuje
(abc byly v minulém kole korektní a všichni znají
jejich návrhy [1234])
```

### Strana 122

```text
Analýza

■ Algoritmus skončí po f+1 kolech kde f je počet selhání
■ Počet přenesených zpráv každé kolo 𝑂(𝑁 2 ), stejný je i počet
  Decided zpráv
■ Počet kol nejvýše 𝑁 → celkem zpráv 𝑂(𝑁 3 )
■ Je zaručena integrita, platnost (zřejmé z algoritmu), shoda,
  ukončení
```

### Strana 123

```text
Analýza, korektnost

■ Shoda (Agreement): Všechny korektní procesy rozhodnou stejně.
      V jednom kole nemohou dva procesy rozhodnout odlišně
      Pokud rozhodují po obdržení stejného počtu zpráv, rozhodují
      stejně
      Pokud obdrží Decision, buď jej obdrželi všechny korektní, nebo
      některé korektní obdrží méně zpráv a nemohou rozhodnout
      Jak rozhodl první korektní, rozhodnou všechny korektní v
      následujícím kole
■ Ukončení (Termination): Nové kolo pokračuje, když alespoň jeden
  proces selže, nejpozději po f kolech nemůže již žádný selhat
```

### Strana 124

```text
   Analýza, uniformní shoda ?

                                   a         b         c            d             e
■ Není zaručena uniformní          5        4          3            2            1
  shoda
                                   a         b         c            d             e
■ Pokud proces udělá        5432            5432       5432             54321
  rozhodnutí a nešíří jej
  (selže před odesláním),          a         b         c            d
  toto rozhodnutí je        5432           5432            54321

  ‚zapomenuto‘                     a         b         c
                                                                                2x po sobě od
                                                                                abcd, decision(1)
                                                                                Rozeslání ale selže
■ Ostatní procesy mohou     5432           5432        Decision 1
                                                       CRASH
  udělat rozhodnutí jiné           a         b
                             Decision 2   Decision 2
```

### Strana 125

```text
Záplavový algoritmus,
uniformní shoda
■   Procesy rozhodnou až v N-tém kole
■   Udržují procesy, od kterých slyšeli návrh jen pro aktuální kolo
■   Udržují globální, napříč koly, seznam doslechnutých návrhů
→ V N-tém kole mají všechny korektní (přeživši) procesy stejnou
     množinu doslechnutých návrhů
       (pokud by proces věděl o návrhu o kterých jiný proces neví,
       musely by jej šířit v každém kole nekorektní procesy →
                                          těch je ale méně než N)
→ Rozhodnou jen oni a rozhodnou stejně (uniformní shoda)
```

### Strana 126

```text
Hierarchický konsensus
■   Algoritmus s 𝑂 𝑁 2 zprávami
■   Používá Best Effort všesměrové vysílání a Perfect Failure Detector
    pro crash-stop model procesů
■   Zaručuje platnost, shodu, integritu, ukončení
■   V následující verzi nezaručuje uniformní shodu
■   Princip:
       Pracuje v kolech, proces učiní rozhodnutí v kole, které odpovídá
       jeho ranku
       Rozhoduje se podle své aktuální hodnoty props a vysílá ji všem
       ostatním procesům
       Na počátku nastaví svůj návrh do své lokální proměnné props
       Pokud proces obdrží hodnotu od procesu s vyšší prioritou, než má
       on sám, ale s nižší než je hodnota procesu, od kterého akceptoval
       propavlue, uloží si ji a poznačí si i tento proces
```

### Strana 127

```text
    Hierarchický konsensus,
    algoritmus / implementace
■   Algoritmus si udržuje seznam procesů, které selhaly, dále číslo kola, aktuálně zvolený
      návrh a jeho navrhovatele, příznak, zdali od procesu s daným rankem již návrh
      obdržel a příznak, zdali již návrh vysílal.
■   Detekuje procesy které selhaly
■   V případě podání počátečního návrhu, tento šíří jako návrh v rámci prvního kola


upon event <c,init> do // c – hierarchický konsensus
      detected:={}; round:=1; proposal:=null; proposer:=0;
      delivered={}; broadcast:=false

upon event <crash|p> do // detekováno selhání procesu p
       detected:=detected U {rank(p)}

upon event <c,propose|v> do
       proposal:=v;
```

### Strana 128

```text
 Hierarchický konsensus,
 algoritmus
Proces rozhodne, pokud aktuální kolo odpovídá jeho ranku
upon round=rank(self) ∧ proposal≠nill ∧ broadcast=false do
          broadcast=true
          trigger<beb, Broadcast|[DECIDED, proposal]>
          trigger<c,Decide|proposal>

Index kola každý proces zvýší, pokud pro od procesu s rankem round obdrží zprávu o jeho rozhodnutí, nebo
detekuje jeho selhání
upon round ∈ detected ∨ delivered[round]=true do
       round=round+1


Po obdržení zprávy od procesu p si zprávu uloží jako aktuální kadidátní rozhodnutí, včetně informace o
doručení od daného procesu, pokud rank odesilatele je menší než jeho, ale větší než rank procesu aktuálně
uloženého kadndidátního rozhodnutí
upon event <beb, Deliver| p,[DECIDED,v])>
         if rank(p)<rank(self) ∧ rank(p)>proposer then
                   proposal=v, proposer=p
         delivered(rank(p)):=true
```

### Strana 129

```text
P1 P2 P3 p4 P5                         P6
                                               ■ Žádný proces nerozhodne a nevysílá
                                           2     dříve, než obdrží zprávu nebo
                                                 detekuje selhání všech procesů s
                     2           P4:             nižším rankem.
                                   2

                                 P2:
                                               ■ Nezáleží na pořadí, v jakém proces
                2
                                 CRASH           obdrží v rámci jednoho kola zprávy od
                                                 procesů s nižším rankem nebo
          3
                                 P5              detekuje jejich selhání → vždy
                                      2
                                                 rozhodně stejně
                                 P1:
     8                           CRASH         ■ Všechny korektní procesy rozhodnou
                                                 s hodnotou, kterou rozhodl korektní
                                 P3:
 2                                     3
                                                 proces s nějnižším rankem
                                               ■ Není zaručena uniformní shoda
     Adaptuje nejprve hodnotu 3 od procesu P3,   (druhý proces rozhodl pro hodnotu 8)
     pak hodnotu 2 od procesu 5. Hodnou 2 od
     procesuP4 ignoruje
```

### Strana 130

```text
2   8   2   2   2   2   2   2


2   8   2   2   2   2   2   2


2   8   2   2   2   2   2   2


2   8   2   2   2   2   2   2   ■   Žádný proces nerozhodne a nevysílá dříve,
                                    než obdrží zprávu nebo detekuje selhání
                                    všech procesů s nižším rankem.
2   8   2   2   2   2   2   2
                                ■   Nezáleží na pořadí, v jakém proces obdrží
2   8   2   2   2   2   2   2
                                    v rámci jednoho kola zprávy od procesů s
                                    nižším rankem nebo detekuje jejich
                                    selhání → vždy rozhodně stejně
2   8   2   8   8   1   8   2
                                ■   Všechny korektní procesy rozhodnou s
                                    hodnotou, kterou rozhodl korektní proces s
2   8   2   5   6   1   4   2       nějnižším rankem
                                ■   Není zaručena uniformní shoda (druhý
2   8   3   5   6   1   4   7
                                    proces rozhodl pro hodnotu 8)
```

### Strana 131

```text
2   8   2   2   2   2   2   2


2   8   2   2   2   2   2   2


2   8   2   2   2   2   2   2


2   8   2   2   2   2   2   2   ■   Žádný proces nerozhodne a nevysílá
                                    dříve, než obdrží zprávu nebo detekuje
                                    selhání všech procesů s nižším rankem.
2   8   2   2   2   2   2   2
                                ■   Nezáleží na pořadí, v jakém proces
                                    obdrží v rámci jednoho kola zprávy od
2   8   2   2   2   2   2   2
                                    procesů s nižším rankem nebo detekuje
                                    jejich selhání → vždy rozhodně stejně
2   8   2   8   8   1   8   3
                                ■   Všechny korektní procesy rozhodnou s
                                    hodnotou, kterou rozhodl korektní
2   8   2   5   6   1   4   3       proces s nějnižším rankem
                                ■   Není zaručena uniformní shoda (druhý
2   8   3   5   6   1   4   7       proces rozhodl pro hodnotu 8)
```

### Strana 132

```text
Hierarchický konsensus,
Analýza
■ Je zaručena platnost, shoda a integrita
■ Ukončení vyplývá z vlastnosti silné úplnosti perfektního
  detektoru (odhalí selhání procesu)
■ Není zaručena uniformní shoda
■ Ukončení je garantováno po N kolech, v každém se přenese
  O(N) zpráv
■ Počet vysílaných zpráv je 𝑂(𝑁 2 )
```

### Strana 133

```text
    Uniformní Hierarchický
    konsensus
■   S použitím spolehlivého broadcastu zajistíme uniformní shodu
■   Spolehlivý broadcast je složitější a zahrnuje více zpráv, použijeme jen v okamžiku,
    kdy je jisté, že všechny uzly ví o návrhu, leadera jehož rank odpovídá aktuálnímu
    kolu
■   Princip:
       Leader, odešle návrh a neuloží dokud nedostane ‘ack’ od ostatních (nebo
       nedetekuje jejich pád)
       Pokud má všechna potvrzení, ukládá a spolehlivým broadcastem posílá
       informaci o doruční
       Účastnící pokud obdrží návrh od lídera, přijmou jej za aktuální a pošlou ‘ack’
       Pokud účastníci obdrží informaci o doručení od lídera, informaci doručí
       Pokud účastníci detekují pád lídera, přechází do dalšího kola
```

### Strana 134

```text
Uniformní hierarchický                                                                        2        8       2
                                                                                                               2
                                                                                                                           5


konsensus, příklady
                                                                                          2       2        2

                                                                                              2        2       2           2
                                                                                                      CRASH          ack
                                          Procesy na výzvu odpoví ‘ack’ až                            ack
        2        8            2       5
                                          na jeden, který selhal. Ten je detekován        2            2       2         2
    2                         2
            2        2                    a vzápětí proces 1 odešle spolehlivým
                                          broadcastem rozhodnutí, všechny
        2        2            2       2
                                          korektní procesy jej doručí a rozhodnou.
            CRASH
                ack               ack                                                     2            2       2         2
                                             Procesy na výzvu odpoví ‘ack’ až                                        2
        2        2        2           2      na jeden, který selhal. Ten je detekován
                                             a vzápětí proces 1 zkusí odeslat                                  2         2
Dcd 2                         Dcd 2
                      Dcd 2                  spolehlivým broadcastem rozhodnutí, ale                           ack

        2        2        2           2      Selže. Rozhodnutí nedoručil žádný korektní                        2           2
                                             proces, detekují selhání procesu 1 a
                                                                                                                     Dcd 2
                                             pokračuje proces 3
                                                                                                               2           2
```

### Strana 135

```text
Epocha lídra
■   Epocha je v distribuovaném systému definována jako časový úsek od okamžiku
    volby lídra po jeho sesazení
■   Epocha definována unikátní dvojicí: (𝑡𝑠, 𝑙𝑒𝑎𝑑𝑒𝑟𝐼𝐷)
      – ts – Časové razítko epochy, Zajišťuje monotonii a pořadí.
       ■ Vyšší ts vždy „přebíjí“ nižší (logická hodiny/čítač).
      – LeaderID (leaderID): Identifikátor – rank lídra této epochy, zajišťuje autoritu.

■   Společně tyto parametry vytvářejí jednoznačný kontext, který procesům říká:
       "Věřím tomuto lídrovi v této konkrétní fázi vývoje systému.„

■   Vznik nové epochy nastává, když detektor Ω nahlásí nového důvěryhodného lídra
■   Akceptace (Validační pravidlo): Proces přijme novou epochu (𝑡𝑠, 𝑙𝑒𝑎𝑑𝑒𝑟𝐼𝐷) pouze
    tehdy, pokud je 𝑡𝑠 vyšší než jeho lastts (předchozí časové razítko)
■   Tímto se automaticky „degraduje“ starý lídr – jeho zprávy už systém neakceptuje,
    protože mají nižší 𝑡𝑠.
```

### Strana 136

```text
Střídání epoch lídra: Epoch
change
■ Modul ec (epoch change) signalizuje započetí nové epochy
  událostí
                   < 𝑒𝑐, 𝑆𝑡𝑎𝑟𝑡𝐸𝑝𝑜𝑐ℎ|𝑡𝑠, 𝑙𝑖𝑑 >
■ Garantuje následující vlastnosti
   – Monotonie: pokud
                   ′     ′
                           korektní′ proces začne epochu (𝑡𝑠, 𝑙id)
      a později (𝑡𝑠 , 𝑙𝑖𝑑 ) pak 𝑡𝑠 > 𝑡𝑠
   – Konzistence: pokud jeden korektní proces započne
      epochu (𝑡𝑠, 𝑙id) a jiný (𝑡𝑠′, 𝑙𝑖𝑑′) a pokud 𝑡𝑠 = 𝑡𝑠′ pak
      𝑙𝑖𝑑 = 𝑙id′
   – Nakonec leader: od určitého okamžiku všechny korektní
      procesy započaly stejnou epochu s korektním leaderem
      a další epochu nezahájí
```

### Strana 137

```text
Střídání epoch lídra: Epoch
change, algoritmus
■  Inicializuje aktuálního leadera, časové razítko aktuální epochy a
   vlastní časové razitko, které bude případně používat při nárokování si
   vlády
upon event <ec,init> do
       trusted:=l0, lastts=0; ts=rank(self)
■  Detektor leadera Ω detekuje nového leadera a procesy si jej poznačí.
   Pokud je leaderem on, uchází se o převzetí vlády zasláním zprávy s
   časovým razítkem o N procesu větším než posledně (tak má každý
   proces unikátní sekvenci časových razítek)
upon event <Ω,trust|p> do
      trusted:=p
      if p=self then
             ts:=ts+N
             trigger<beb, Broadcast|[NEWEPOCH, ts]>
```

### Strana 138

```text
Střídání epoch lídra: Epoch
change, algoritmus
■   Proces akceptuje nárok odesilatele na vládu, pokud dle jeho
    informací je odesilatel aktuálním lídrem a časové razítko ve zprávě je
    větší než posledně mu známé. Jinak odmítne
upon event <beb, Deliver | led, [NEWEPOCH, newts]> do
   if trusted:=led & newts>lastts then
      lastts:=newts;
      trigger <ec, StartEpoch | newts, led>
   else
      trigger <pl, Send | led, [NACK] > // NACK – not ack
■   Pokud je proces odmítnut (buď ještě nezná nového leadera, nebo jej
    nezná odesilatel odmítnutí) a stále věří, že leaderem je on, je
    tvrdohlavý a požadavek opakuje se zvýšeným časovým razítkem
upon event <pl, Deliver | p, [NACK] > do
    if trusted:=led then
      ts:=ts+N
      trigger<beb, Broadcast|[NEWEPOCH, ts]>
```

### Strana 139

```text
Střídání epoch lídra: Epoch
change, analýza
■ Leader doručí svůj nárok všem procesům (platnost Best Effort
  Broadcast)
■ Pokud nedoručí, selhal a leaderem se stane jiný proces
■ Dříve nebo později, pokud neselže, doručí nárok s nějvětším
  časovým razítkem
■ Monotonie a konzistence plyne z algoritmu
■ Vlastnost nakonec silná přesnost detektoru a volby lídra Ω
  zaručuje, že nakonec bude zvolen lídr, který je lídrem
  permanentně
```

### Strana 140

```text
Střídání epoch lídra: Epoch
change, příklad
P1
          NEWEPOCH, 2     NEWEPOCH, 6
P2
           StartEpoch, P2,2
                       NACK
P3
                              StartEpoch, P2,6
P4
                 StartEpoch, P2,2


 Ω   TRUST P2                                        TRUST P3


                                                 P3 a P4 doposud
                                                 Neselhali, P3 má
                                                 Vyšší prioritu
```

### Strana 141

```text
Konsensus v asynchronním
systému
■ Přestože platí FLP, existuje algoritmus, díky kterému může
  dojít ke konsensu … ale(!)
■ Platí v něm jen safety podmínky, platnost, integrita a shoda
■ Neplatí liveness podmínka ukončení
   – Nezaručuje, že někdy shody bude dosaženo
```

### Strana 142

```text
PAXOS

■ Obecný princip
   – Algoritmus využívá kvórum (nadpoloviční většinu)
      procesů a unikátní čísla návrhů.
   – Navrhovatel (proposer) předkládá vybrané majoritě
      návrh obsahující hodnotu a unikátní číslo návrhu.
   – Akceptoři (acceptors) návrh přijmou nebo odmítnou na
      základě porovnání čísla návrhu s těmi, která již dříve
      zaznamenali.
   – Pokud je hodnota potvrzena majoritou, stává se
      neměnným konsenzem a všechny budoucí návrhy musí
      tuto hodnotu respektovat.
        ■   N/2+1 proces zapsal stejný návrh
```

### Strana 143

```text
PAXOS, Algoritmus
           Fáze přípravy
■   Navrhovatel (Proposer) připravuje půdu:
    – Zvolí si unikátní číslo návrhu (vyšší než jakékoliv doposud
       použité).
    – Odešle zprávu PREPARE(číslo) na majoritu (quorum) procesů.
■   Akceptoři (Acceptors) reagují:
    – Ignorují: Pokud už slíbili účast jinému návrhu s vyšším
       číslem.
    – Slibují (Promise): Pokud je číslo návrhu dostatečně vysoké,
       odpoví: „Slibuji, že nebudu akceptovat žádný nižší návrh.“
    – Posílají info: Pokud už dříve nějakou hodnotu „odsouhlasili“,
       přiloží ji k odpovědi (aby Navrhovatel věděl, co musí
       respektovat).
```

### Strana 144

```text
PAXOS, Algoritmus
           Fáze přijetí
■   Navrhovatel konsoliduje:
     – Pokud obdržel sliby od majority, může konečně poslat svůj
       návrh.
     – Pokud mu akceptoři v první fázi poslali zprávy, že už mají
       uloženou nějakou předchozí hodnotu, navrhovatel musí tuto
       hodnotu převzít (místo té své původní). Tím se zajišťuje, že se
       konsenzus nepřepíše něčím starším.
     – Odešle zprávu ACCEPT(číslo, hodnota) všem akceptorům.
■   Akceptoři rozhodují:
     – Přijmou: Pokud mezitím nepřišel jiný navrhovatel s vyšším
       číslem, akceptor hodnotu „uloží“ (zapíše do svého logu) a
       potvrdí to navrhovateli.
     – Odmítnou: Pokud mezitím slíbili účast někomu jinému (kdo má
       vyšší číslo návrhu), tento ACCEPT prostě zahodí.
```

### Strana 145

```text
             PREPARE(1)                                                    PREPARE(2)
 -      -        -     -      -      -      -      -      A     A     A     A     A      A     A     A
[-]    [-]      [-]   [-]    [-]    [-]    [-]    [-]    [1]   [1]   [1]   [1]   [1]    [1]   [1]   [1]




        RESPONSE(-)                                                        RESPONSE(A)
 -      -       -      -      -      -      -      -      A     A     A     A     A      A     A     A
[1]    [1]     [1]    [1]    [1]    [1]    [1]    [1]    [2]   [2]   [2]   [2]   [2]    [2]   [2]   [2]




             ACCEPT(A,1)                                                     ACCEPT(A,2)

 -      -        -     -      -      -      -      -      A     A     A     A     A      A     A     A
[1]    [1]      [1]   [1]    [1]    [1]    [1]    [1]    [2]   [2]   [2]   [2]   [2]    [2]   [2]   [2]


  A      A       A      A      A      A      A      A     A     A     A     A     A      A     A     A
 [1]    [1]     [1]    [1]    [1]    [1]    [1]    [1]   [2]   [2]   [1]   [2]   [2]    [2]   [2]   [2]
                      WRITE(A)                                             WRITE(A)
```

### Strana 146

```text
               PREPARE(1)                                                       PREPARE(2)
 -        -        -     -      -      -      -      -      A      A      A      -       -       -     -        -
[-]      [-]      [-]   [-]    [-]    [-]    [-]    [-]    [1]    [1]    [1]    [2]     [2]     [2]   [2]      [2]




          RESPONSE(-)                                                           RESPONSE(-)
 -       -        -      -      -      -      -      -      A      A      A      -               -     -        -
[1]     [1]      [1]    [1]    [1]    [1]    [1]    [1]    [1]    [1]    [1]    [2]     [2]     [2]   [2]      [2]




               ACCEPT(A,1)                                                             ACCEPT(B,2)

 -        -       -      -      -      -      -      -      A      A      A      -              -      -        -
[1]      [1]     [1]    [1]    [1]    [1]    [1]    [1]    [1]    [1]    [1]    [2]    [2]     [2]    [2]      [2]


  A       A        A      -      -      -      -      -      A      A      A      B      B       B        B      B
 [1]     [1]      [1]    [1]    [1]    [1]    [1]    [1]    [1]    [1]    [1]    [2]    [2]     [2]      [2]    [2]
       WRITE(A)                                                                               WRITE(B)
```

### Strana 147

```text
              PREPARE(1)                                              ACCEPT(A,1)
  -      -        -      -      -      -      -      -     -     -        -     -     -     -        -       -
 [-]    [-]      [-]    [-]    [-]    [-]    [-]    [-]   [2]   [2]      [2]   [2]   [2]   [1]      [1]     [1]


                                                           -     -       -      -     -     A       A        A
                                                          [2]   [2]     [2]    [2]   [2]   [1]     [1]      [1]
         RESPONSE(-)
                                                                                                 WRITE(A)
 -      -        -      -      -      -      -      -
[1]    [1]      [1]    [1]    [1]    [1]    [1]    [1]


                                                                      ACCEPT(B,2)

              PREPARE(2)                                   -     -       -      -     -     -        -       -
                                                          [2]   [2]     [2]    [2]   [2]   [1]      [1]     [1]
  -      -        -      -      -      -      -      -
 [1]    [1]      [1]    [1]    [1]    [1]    [1]    [1]
                                                           B     B       B      B     B     A       A        A
                                                          [2]   [2]     [2]    [2]   [2]   [1]     [1]      [1]
                                                                      WRITE(B)
             RESPONSE(-)

 -      -        -      -      -      -      -      -
[2]    [2]      [2]    [2]    [2]    [1]    [1]    [1]
```

### Strana 148

```text
  PAXOS, Algoritmus, důkaz shody
Majorita M nakonec uloží stejnou hodnotu se stejným číslem návrhu
Je možné, aby v systému byla později uložena hodnota s vyšším číslem návrhu
a jinou hodnotou, než je hodnota konsensu?
  B     B     B     B     B     A     C     A
 [2]   [2]   [2]   [2]   [2]   [1]   [4]   [1]

K uložení (C,4) musel navrhovatel získat majoritu procesů. Z principu majority
musel jeden z procesů z M dát příslib k návrhu s časovým razítkem 4
Předpokládejme, že je to první hypotetické uložení jiné hodnoty než B s číslem
návrhu větším než 2
Tento proces již musel uložit (B,2)
  pokud by dal souhlas k PROPOSE(4) dřív, nemohl by (B,2) uložit
  pokud jej dal později, musel připojit hodnotu B
     ta může mít vyšší číslo návrhu, konkrétně 3, pokud v rámci jiného návrhu
     akceptoval návrh a uložil (ale musí jí byt B, jinak by neplatil předpoklad)
  jiný proces nemohl přislíbit s připojenou jinou hodnotou a s vyšším číslem
  návrhu než je 2, protože se jedná o první uložení jiné hodnoty s časovým razítkem
  vyšším než 2
Nemůže totiž dojit k prvnímu uložení hodnoty mimo konsensus
```

### Strana 149

```text
 PAXOS,                             -     -
                                               PREPARE(1)
                                                   -     -     -
                                                                    PREPARE(2)

                                                                       -     -      -

 LIVELOCK                          [-]   [-]      [-]   [-]   [-]     [-]   [-]    [-]




                                                                    RESPONSE(2)
■ Pokus je mnoho                               RESPONSE(1)
  navrhovatelů, kteří chtělí        -     -       -      -     -      -      -     -
                                   [1]   [1]            [2]   [2]    [2]          [2]
  svůj návrh prosadit, může                      [1]                        [2]

  dojít k livelock (uváznutí v
  neustálé aktivitě)
                                                                    ACCEPT(A,2)
■ Navrhovatelé podávají                        PREPARE(3)
  návrhy se zvyšujícími se čísly    -     -        -     -     -       -     -      -
  návrhu, a nikdy nevznikne        [1]   [1]      [1]   [2]   [2]     [2]   [2]    [2]

  majorita pro jeden návrh
■ Řešení? -> využít lídra
                                               RESPONSE(3)            PREPARE(6)

                                    -     -        -     -     -       -     A      A
                                   [3]   [3]      [3]   [3]   [3]     [3]   [2]    [2]
```

### Strana 150

```text
Paxos s Eventually Leader-em

■ Princip: Delegování právomoci na jednoho navrhovatele
   – Všichni účastníci věří, že existuje Leader díky Ω (epocha
       lídra)
   – Ostatní Proposeři "čekají" (nebo se stáhnou), pokud
       detekují aktivního Leadera.
   – Konflikty zmizí, protože návrhy podává pouze jeden proces.

■ Shoda, Integrita, Platnost: Stále platí – i když Leader Detector
  selže (např. v jednu chvíli máme dva leadery), Paxos je díky své
  podstatě stále bezpečný (safety neztrácíme).
■ Ukončení: Obnovena v momentě, kdy Detector stabilizuje na
  jednom správném Leaderovi
```

### Strana 151

```text
BYZANTSKÉ
  PROCESY
     FZjr 2019 - 2024
```

### Strana 152

```text
Byzantské procesy

■ Nesprávné ukončení procesu nemá žádná pravidla a chování
  procesu není nijak vymezené
■ Proces dokonce může, pokud je ukončen napadením,
  předstírat korektní chování, přitom poskytovat nepravdivé
  informace
■ Detekce uvedené v předchozích částech jsou nepoužitelné
```

### Strana 153

```text
Problém Byzantských
generálů – příběh
■ Vojsko Byzantské říše složené z několika armád dobývá město.
■ Každý generál velí své armádě a komunikuje s ostatními generály
  pomocí seržantů.
■ Generálové nebo seržanti mohou být agenty nepřítele a jejich
  záměr jde proti zájmům Byzantských. Nepřátelský agent - generál
  může vydávat falešné zprávy, aby věrní generálové nedosáhli
  konsensu,
■ Útok na město se blíží a všechny armády musí zaútočit ve stejný
  okamžik, jinak je téměř jistá porážka útočících vojsk s velkými
  ztrátami
■ Věrní generálové se musí dohodnout na době útoku a to
  navzdory možným nepřátelským agentům ve svých řadách.
```

### Strana 154

```text
Problém Byzantských
generálů
■ Dohody nelze dosáhnout, pokud byzantských procesů je jedna
  třetina nebo více.
■ Důkaz: Ukážeme pro tři procesy, kde je jeden generál a dva
  seržanti, že v případě jednoho zkorumpovaného člena nejde
  dosáhnout dohody
■ Pokud general není loajální, pak pro způsobení ztrát vydá
  odlešné rozkazy oboum seržantům …
■ Požadujeme:
   – IC1: Všichni věrní seržanti vykonají ten samý příkaz
   – IC2: Pokud příkaz vydal věrný generál, vykonají jej takto
      všichni věrní seržanti
```

### Strana 155

```text
Problém Byzantských
generálů
                              útok



                                     řekl ústup

                               ?


  útok                ústup                útok                útok



         řekl ústup                               řekl ústup
```

### Strana 156

```text
Pro n účastníků a m zrádců

■ n Albánských generálů a z toho m zrádců
■ Pokud n<=3*m problém nemá řešení
■ Spor
   – Dobrá, umíme vyřešit problém pro n=3*m Albánských
       generálů …
   – … pak bychom ale měli být schopni řešit i problém tří
       Byzantských generálů s jedním zrádcem!
   – Protože bychom redukovali Albánce po skupinách na
       Byzanťany, zlé do skupiny jedné, zbylé do ostatních dvou
       skupin a výstupem skupin by byla zjištěná shoda.
```

### Strana 157

```text
Algoritmus pro řešení Problému
Byzantských generálů
■   Algoritmus OM přijímá parametr m
■   Algoritmu OM(0)
      1. Generál posílá jeho hodnotu každému ze seržantů
      2. Každý seržant použije tuto hodnotu, pokud je mu doručena, pokud ne,
           použije defaultní hodnotu (například RETREAT)
■   Algoritmu OM(m), pro m>0
      1. Generál posílá jeho hodnotu každému ze seržantů
      2. Pokud seržant i obdrží hodnotu, označíme ji vi, pokud žádnou
           neobdrží, pracuje s defaultní hodnotou. Posléze provede algoritmus
           OM(m-1), ve kterém nahradí na pozici generála původního generála a
           zašle tuto hodnotu všem ostatním seržantům
      3. Pro všechny i a pro každého j seržant platí, že seržant i obdrží zprávu
           vj po ukončení kroku 2 (výsledek OM(m-1) pro tohoto seržanta), nebo
           Defaultní hodotu, Pak je jím zvolenou hodnotou (na této úrovni
           rekurze) hodnota majority(v1 … vn-1)
```

### Strana 158

```text
Generál věrný, OM(0)
■ Pokud jsou všichni věrní, není co řešit a OM(0) funguje pro IC1 a
  IC2
■ Algoritmus OM(0) funguje vždy, když je generál věrný, tj. pro
  libovolný počet zrádců mezi seržanty
■ Pravidlo IC2 je splněno tím, že věrní seržanti splní generálův
  rozkaz




                        a                     a
                                a        a




             a              a             a             x
```

### Strana 159

```text
Generál věrný, OM(m)
■ Budeme potřebovat, aby fungoval i algoritmus OM(m), m>0
■ Pro případ věrného generála je větší m komplikací, ale bez toho
  to pro obecný případ i možných něvěrných hlavních generálů
  nepůjde
tedy …
■ Každý seržant je generálem pro skupinu bez původního generála
  a nechá řešit ostatní problém s tím, že mu tito sdělí své
  rozhodnutí
■ Z těchto rozhodnutí zvolí majoritu a tuto příjme jako své
  rozhodnutí.
```

### Strana 160

```text
OM(1), generál věrný
■   Pokud byl původní generál věrný, obdrží všichni seržanti stejnou
    hodnotu, a proto v případě vyjednávání ve skupině bez původního
    generála dojde ke shodě mezi věrnými seržanty, pokud jich je více než
    zrádců.
■   První seržant navrhne hodnotu, ostatní věrní hodnotu přijmou a první
    seržant jakmile zjistí, že nadpoloviční většina ostatních seržantů hodnotu
    přijala, příjme ji také (dle principu majority)
■   Všichni ostatní věrní seržanti si stejným způsobem ověří svoji hodnotu

              a




             a               a               a                x


     majority(a,a,a,x)
```

### Strana 161

```text
OM(1), generál věrný
■ V případě dvou zrádců z celkového počtu pěti vojáků (i s
  původním generálem) již algoritmus OM(1) nefunguje správně
■ Zrádci mou poslat jinou hodnotu rozhodnutí pokud hledání
  shody vyhlásí věrný první seržant a jinou pokud druhý seržant
  hledá shodu na rozkazu.


            b




            ?           b            a            a


    majority(a,a,b,b)
```

### Strana 162

```text
OM(2), generál věrný
■ V případě dalšího kola vyjednávání o hodnotách, kdy zbylí tři
  seržanti neodpoví ihned, ale utvoří další podskupinky bez
  původních generálů a radí se navzájem.
■ Tedy věrní hodnotu nepotvrdí ihned, ale v tomto případě dojde ke
  zmatení, protože v o jednoho věrného menších podskupinkách
  získá zrádce navrch a zmate zbývající věrné!


            a




            a             a             a             x


    majority(a,a,a,x)
```

### Strana 163

```text
OM(3), generál věrný
■    V případě dalšího kola vyjednávání o hodnotách, kdy zbylí tři seržanti
     neodpoví ihned, ale utvoří další podskupinky bez původních generálů a
     radí se navzájem.
■    Tedy věrní hodnotu nepotvrdí ihned, ale v tomto případě ještě nedojde ke
     zmatení, protože v o-jednoho věrného menších podskupinkách získá
     zrádce trochu navrch, ale stále dva loajální určí správce

              a                      a            a




                                         a              x
              ?              a

    majority(a,a,?,?) majority(a,a,x)

                             Zjistí stejným způsobem pro L3 a zrádného L4
```

### Strana 164

```text
OM(m), generál věrný

■   Algoritmus OM(m) splňuje podmínku IC2, a tím i podmínku IC1, v
    případě, když hlavní, původní rozkaz vydávající generál je věrný, pokud
    platí


                  CELKOVÝ_POČET_VOJÁKů > 2*POČET_ZRÁDCů + m


■   V našem případě bylo pět vojáků, jeden zrádce, a fungovalo nám i
    OM(2), protože 5>2*1+2
■   OM(3) by již nefungovalo, neplatí 5>2*1+3,
■   Stejně tak nefungovalo již OM(1) pro dva zrádce. Neplatí totiž 5>2*2+1
```

### Strana 165

```text
OM(1), generál zrádný
■   Skupina seržantů si dokáže poradit se zrádným generálem, pokud jdou
    alespoň tři a všichni jsou věrní a to algoritmem OM(1).
■   Poradí se, předají si hodnoty, které jim generál zaslal a shodnou se na
    majoritě, protože jako věrní nelžou a každý řekne po pravdě obdrženou
    hodnotu
■   Je splněna podmínka IC1 a IC2 neřešíme, ta je jen pro případ věrného
    generála




                           a                        d
                                   b           c




              c                c                c                c
                                majority(a,b,c,d)
```

### Strana 166

```text
OM(1), generál zrádný (+1)
■    V případě dvou zrádných vojáků z pěti by algoritmus nefungoval ani v případě
     věrného generála. Pro šest vojáků a dva zrádce ano.
■    Fungoval by algoritmus OM(1) pro zrádného generála, jednoho ze seržantů a
     čtyř věrných?
■    Nefungoval: při vyjednávání o generálově rozkazu zrádný seržant zmaří shodu
     věrných podstrčením různých údajně obdržených hodnot.




                        a                           d             e
                                 b         c




                   d                            d             c
                                     a
    majority(a,b,c,d,?): např majority(a,a,b,c,d)≠ majority(a,b,c,c,d)
```

### Strana 167

```text
OM(2), generál zrádný (+1)
■   Pokud by se ale poradili o jedna menší skupiny o každé zprávě. Tyto skupiny
    vyvolá každý věrný seržant
■   Pokud se bude diskutovat o zprávě od věrného seržanta, bude v podskupině
    přítomen i zrádce, ale převaha věrných se shodne na zprávě věrného tak, jak
    ji poslal.
■   Pokud se bude diskutovat o zprávě zrádce, budou jednat jen věrní seržanti a
    ti pokaždé předloží jimi obdrženou zprávu od zrádce a každý vektor zpráv v
    této skupině vyhodnotí stejně. Každý iniciuje jednání o zprávě, kterou dostali
    od zrádce a vyhodnotí (4 x majority(a,c,d,d))

                              majority(a,c,d,d)



                      d                               d               c
                                           a

■   Každý iniciuje jednání o zprávě, co dostali od zrádce (4 x majority(a,c,d,d))
    Čímž si věc ujasní a shodnou se na zprávě od zrádce, v tomto případě na d
■   Nyní již mohou tuto hodnotu každý použít v původním OM(1) z minulého
    slajdu a loajální se shodnou na stejné akci -> Platí IC1
```

### Strana 168

```text
Problém Byzantských generálů.
Řešení pro m zrádců
■ Algoritmus OM(m) řeší problém Byzantských generálů,
  pokud je maximálně m zrádců a celkem je více než 3*m
  vojáků
■ Víme, že pro případ věrného generála dokáže algoritmus
  OM(m) zajistit obě podmínky IC1 a IC2, pokud počet vojáků je
  větší než dvojnásobek zrádců plus m, což platí, protože
  zrádců je m, stejné číslo je argumentem tohoto algoritmu, a
  vojáků je předpokládáno více než 3*m, což je ‘přesně
  potřeba’
```

### Strana 169

```text
Problém Byzantských generálů.
Řešení pro m zrádců
■   Algoritmus OM(m) řeší problém Byzantských generálů, pokud je
    maximálně m zrádců a celkem je více než 3*m vojáků
■   Důkaz indukcí funkčnosti OM(m) pro případ zrádného generála a 3*m-1
    seržantů
■   OM(0) platí pro situaci bez zrádce triviálně
■   Indukcí, pokud OM(m-1) splňuje IC1 a IC2, pak lze dokázat splnění těchto
    podmínek i OM(m)
■   Pokud je generál zrádný, pak v diskusi o jeho rozkazech OM(m-1) z druhého
    kroku algoritmu je více než (3*m-1) vojáků a zrádců je m-1. Musí platit, že je
    vojáků > 3* zrádců, tedy 3*m-1 > 3*(m-1), což platí
■   Provedením OM(m-1) každí dva věrní seržanti se shodnou na stejné hodnotě
    vj.
* pozn.: jelikož generál je zrádce, je v OM(m-1) o jednoho méně zrádců, a tedy
buď již generál zrádce není, a OM(m-1) funguje, nebo je opět generál zrádce a v
následně použítém OM(m-2) je o zrádce méně. Pokud jsou pokaždé generálové
zrádci, dostaneme se po m ‘zanořeních’ do OM(0), kde již žádný zrádce nezbývá.
```

### Strana 170

_Bez extrahovatelneho textu._

### Strana 171

```text
OM(0) funguje – tj. všichni poctivci si uloží došlou hodnotu, pak IC1 i IC2




OM(0) funguje (!)




OM(0) nefunguje – poctivci si uloží hodnotu od zrádce a každý může mít jinou
```

### Strana 172

```text
              a
                                   OM(1) funguje taky, i když se nám to trochu zkomplikuje

    a         a


         Všichni sice od poctivce obdrží tu samou informaci, OM(0) by problém řešila, ale zkusíme, jestli je toto
         robustní pro jedno kolo porady
        [a]             [a]          [x]
        []              [a]          [x]
a       []        a     []           [x]    Co nakonec tvrdí zrádce je jedno, důležité je, aby oba poctivci zvolili
                                            stejnou hodnotu, a tu zvolí, protože nakonec u obou ve vektoru hodnot
a                 a            a     a      bude původní hodnota od poctivého generála dvakrát, od zrádce nějaká
[a]      [x]      [a]    [x]   [a]    [a]
                                            hodnota jednou, a mediánem bude ona původní hodnota od poctivého
[a]      []       [a]    [x]   [a]    [a]   maršála
[]       [x]      []     [x]   [x]    [x]
```

### Strana 173

```text
                        Pokud oním zrádcem je maršál, MP(0) nefunguje, ale co porada?

a   b         c


Radí se vždy ti samí poctivci, akorát pokaždé hledá ‘pravdu’ jiný z nich. Ale vektor výsledků
Bude vždy stejný a každý zvolí tu samou střední hodnotu

                  [a]          [a]          [a]
                  []           [b]          [b]
        a         []
                         b     []
                                      c     [c]



        b         c      a     c      a     b
        [a]       [a]    [a]   [a]    [a]   [a]
        [b]       []     [b]   [b]    [b]   [b]
        []        [c]    []    [c]    [c]   [c]
```

### Strana 174

```text
Při první poradě má každý poctivý generál (zahajovatel první porady) správnou hodnotu
od věrného maršála, jeden ze seržantů také, a druhý seržant je zrádce
Druhá porada probíhá mezi oběma seržanty, u zrádce by to byla jen předstíraná snaha, ale
poctivý seržant je manipulován zrádcem a … může zvolit jinou hodnotu než poctivý
generál zadal -> viz úvodní příklad
TEDY MP(2) nefunguje pro tři poctivce a jednoho zrádce!!!
Protože pro systém s n zrádci funguje max. OP(n), pokud je poctivců vic než n
```

### Strana 175

```text
                                f
                                          Každý provede OM(1) pro data od maršála. Tedy vyloučí jej z rozpravy a zeptá
      a
          b   c     d     e               se ostatních, jakou informaci dostali
                                          Jelikož je to OM(1), tak pro každou odpověď vyvolají diskuzi opět




[-]   []      []    []    []        []     [-]   []    []    []    []    []    [-]   []    []    []          []
                                                                                                       []
[]    [b]     []    []    []        []     []    [b]   []    []    []    []    []    [b]   []    []          []
                                                                                                       []
[]    []      [c]   []    []        []     []    []    [c]   []    []    []    []    []    [c]   []          []
                                                                                                       []
[]    []      []    [d]   []        []     []    []    []    [d]   []    []    [-]   [d]   [d]   [d]         [d]
                                                                                                       [d]
[]    []      []    []    [e]       []     [-]   [e]   [e]   [e]   [e]   [e]   [-]   [e]   [e]   [e]         [e]
                                                                                                       [e]
[-]   [f]     [f]   [f]   [f]       [f]    [-]   [f]   [f]   [f]   [f]   [f]   [-]   [f]   [f]   [f]         [f]
                                                                                                       [f]




                                                                                                                         c   d   d   c   d
[-]   []      []    []    []        []     [-]   []    []    []    []    []          [a]         [d]
                                                                               [-]         [d]         [a]   [a]
[]    [b]     []    []    []        []     []    [b]   [b]   [b]   [b]   [b]         [b]         [b]
                                                                               []          [b]         [b]   [b]
[]    [c]     [c]   [c]   [c]       [c]    []    [c]   [c]   [c]   [c]   [c]         [c]         [c]
                                                                               []          [c]         [c]   [c]
[-]   [d]     [d]   [d]   [d]       [d]    [-]   [d]   [d]   [d]   [d]   [d]   [-]   [d]   [d]   [d]   [d]   [d]
                                                                                                                   MED
[-]   [e]     [e]   [e]   [e]       [e]    [-]   [e]   [e]   [e]   [e]   [e]         [e]         [e]
                                                                               [-]         [e]         [e]   [e]
[-]   [f]     [f]   [f]   [f]       [f]    [-]   [f]   [f]   [f]   [f]   [f]         [f]         [f]
                                                                               [-]         [f]         [f]   [f]
```

### Strana 176

```text
      c     d     d     c     d     Nyní budou šestkrát debatovat o každé z šesti hodnot. Každá debata obsahuje
[-]   [a]   [d]   [d]   [a]   [d]   jedno rozeslání od generála a vyhodnocení. Zkusme debatu u prvních dvou
[-]   [b]   [b]   [b]   [b]   [b]   hodnotách, té od zrádce, a potom od prvního věrného zleva
[-]   [c]   [c]   [c]   [c]   [c]
[-]   [d]   [d]   [d]   [d]   [d]
[-]   [e]   [e]   [e]   [e]   [e]   V debatě o hodnotě zrádce tohoto vynechají a provedou …
[-]   [f]   [f]   [f]   [f]   [f]




      [a]   []    []    []    []          [a]    []    []    []    []          [a]   []    []    []    []
      []    [d]   []    []    []          []     [d]   []    []    []          []    [d]   []    []    []
      []    []    [d]   []    []          []     []    [d]   []    []          [d]   [d]   [d]   [d]   [d]
      []    []    []    [a]   []          [a]    [a]   [a]   [a]   [a]         [a]   [a]   [a]   [a]   [a]
      [d]   [d]   [d]   [d]   [d]         [d]    [d]   [d]   [d]   [d]         [d]   [d]   [d]   [d]   [d]




                                                                               d     d     d     d     d
      [a]   []    []    []    []           [a]   [a]   [a]   [a]   [a]
      [d]   [d]   [d]   [d]   [d]          [d]   [d]   [d]   [d]   [d]   MED
      [d]   [d]   [d]   [d]   [d]          [d]   [d]   [d]   [d]   [d]
      [a]   [a]   [a]   [a]   [a]          [a]   [a]   [a]   [a]   [a]
      [d]   [d]   [d]   [d]   [d]          [d]   [d]   [d]   [d]   [d]
```

### Strana 177

```text
      d     d     d     d     d      O hodnotě prvního (a zrádného) mají jisto, ale musí se shodnout pro jistotu
[-]   [d]   [d]   [d]   [d]    [d]   i na hodnotách ostatních. Uvedeme shodu pro druhého, nyní loajálního, seržanta
[-]   [b]   [b]   [b]   [b]    [b]   a obdobně pak bude probíhat shoda na ostatních hodnotách
[-]   [c]   [c]   [c]   [c]    [c]
[-]   [d]   [d]   [d]   [d]    [d]
[-]   [e]   [e]   [e]   [e]    [e]
[-]   [f]   [f]   [f]   [f]    [f]




      [x]   []    []    []    []           [x]   []    []    []    []          [x]   []    []    []    []
      []    [b]   []    []    []           []    [b]   []    []    []          []    [b]   []    []    []
      []    []    [b]   []    []           []    []    [b]   []    []          [x]   [b]   [b]   [b]   [b]
      []    []    []    [b]   []           [x]   [b]   [b]   [b]   [b]         [x]   [b]   [b]   [b]   [b]
      [x]   [b]   [b]   [b]   [b]          [x]   [b]   [b]   [b]   [b]         [x]   [b]   [b]   [b]   [b]




                                                                               b     b     b     b     b
      [x]   []    []    []    []           [x]   [a]   [a]   [d]   [d]
      [x]   [b]   [b]   [b]   [b]          [x]   [b]   [b]   [b]   [b]   MED
      [x]   [b]   [b]   [b]   [b]          [x]   [b]   [b]   [b]   [b]
      [x]   [b]   [b]   [b]   [b]          [x]   [b]   [b]   [b]   [b]
      [x]   [b]   [b]   [b]   [b]          [x]   [b]   [b]   [b]   [b]
```

### Strana 178

```text
      c           d     c     d     Zpět ale k příkladu, kde se jedná o shodě na informaci od prvního seržanta –
[-]   [a]   [d]   [d]   [a]   [d]   zrádce. Pokud by zrádní měli být vedle maršála i dva seržanti, pak …
[-]   [b]   [b]   [b]   [b]   [b]   Musí se šestkrát dosáhnout shody na 25ti hodnotách ve skupinách po čtyřech
[-]   [c]   [c]   [c]   [c]   [c]
[-]   [d]   [d]   [d]   [d]   [d]    6*5*4 jednání o shodách, každé jednání mezi čtyřmi agenty
[-]   [e]   [e]   [e]   [e]   [e]   Navíc tento systém (tři zrádci ze sedmi) nebude fungovat v případ věrného
[-]   [f]   [f]   [f]   [f]   [f]
                                    maršála! Pro tři zrádce musí být minimálně sedm poctivců.




      [a]   []    []    []    []          [a]    []     []    []    []          [a]   []    []    []    []
      []    [x]   []    []    []          []     [x]    []    []    []          []    [x]   []    []    []
      []    []    [d]   []    []          []     []     [d]   []    []          [d]   [x]   [d]   [d]   [d]
      []    []    []    [a]   []          [a]    [x]    [a]   [a]   [a]         [a]   [x]   [a]   [a]   [a]
      [d]   [x]   [d]   [d]   [d]         [d]    [x]    [d]   [d]   [d]         [d]   [x]   [d]   [d]   [d]




                                                                                a           a     d     d
      [a]   []    []    []    []           [a]    [x]   [a]   [a]   [a]
      [a]   [x]   [a]   [d]   [d]          [a]    [x]   [a]   [d]   [d]   MED
      [d]   [x]   [d]   [d]   [d]          [d]    [x]   [d]   [d]   [d]
      [a]   [x]   [a]   [a]   [a]          [a]    [x]   [a]   [a]   [a]
      [d]   [x]   [d]   [d]   [d]          [d]    [x]   [d]   [d]   [d]
```

### Strana 179

```text
OM(2) PRO GENERÁLA P, CELKEM 7P A 3Z
                                                     Shoda korektních na zprávě?

                      7xP 3xZ                        Pro P↓ potřebujeme většinu
                           P
                      6xP 3xZ                 O(1)   Pro Z↓ potřebujeme všechny
                  P             Z

        5xP 3xZ                     6xP 2xZ   O(2)
```

### Strana 180

```text
OM(2) PRO GENERÁLA Z, CELKEM 7P A 3Z

                      7xP 3xZ
                           Z
                      7xP 2xZ                 O(1)
                  P             Z

        6xP 2xZ                     7xP 1xZ   O(2)
```

### Strana 181

```text
OM(4) PRO GENERÁLA P, CELKEM 7P A 3Z

                                   7xP 3xZ
                                        P
                                   6xP 3xZ                               O(1)
                           P                    Z

                 5xP 3xZ                            5xP 2xZ              O(2)
             P                 Z               P              Z

                                                           5xP 1xZ       O(3)
          4xP 3xZ       5xP 2xZ              5xP 2xZ
     P              Z   P           Z    P             Z    P        Z
                                                                         O(4)
    3xP 3xZ 4xP 2xZ 4xP 2xZ 5xP 1xZ 4xP 2xZ 5xP 1xZ 4xP 1xZ 5xP 0xZ
```

### Strana 182

```text
OM(4) PRO GENERÁLA Z, CELKEM 7P A 3Z

                                      7xP 3xZ
                                           Z
                                      7xP 2xZ                               O(1)
                             P                      Z

                  6xP 2xZ                               7xP 1xZ             O(2)
              P                  Z                P               Z

                                                              7xP 0xZ       O(3)
            5xP 2xZ         6xP 1xZ             6xP 1xZ
       P              Z     P          Z    P             Z       P
                                                                            O(4)
    4xP 2xZ 5xP 1xZ       5xP 1xZ 6xP 0xZ 5xP 1xZ       6xP 0xZ   6xP 0xZ
```

### Strana 183

```text
OM(3) PRO GENERÁLA P, CELKEM 7P A 3Z

                              7xP 3xZ
                                   P
                              6xP 3xZ                          O(1)
                      P                    Z

            5xP 3xZ                            5xP 2xZ         O(2)
        P                 Z               P              Z

                                                     5xP 1xZ   O(3)
      4xP 3xZ     5xP 2xZ               5xP 2xZ
```

### Strana 184

```text
OM(3) PRO GENERÁLA Z, CELKEM 7P A 3Z

                              7xP 3xZ
                                   Z
                              7xP 2xZ                          O(1)
                      P                    Z

            6xP 2xZ                            7xP 1xZ         O(2)
        P                 Z               P              Z

                                                     7xP 0xZ   O(3)
      5xP 2xZ     6xP 1xZ               6xP 1xZ
```

### Strana 185

```text
Rotating Byzantine Leader
Detection
■   Požadavky:
      –    Nakonec úspěch (Eventual succession): pokud více než f korektních procesů
           ztratí důvěru v leadera, nový leader dostane důvěru korektních procesů
      –    Odolnost proti puči (Putsch resistence): novému / jinému než stávajícímu leaderu
           korektní proces uvěří jen když si aspoň jeden proces stěžuje na stávajícího lídra
      –    Nakonec shoda (Eventual agreement): procesy budou po nějakém čase (pro
           koordinaci) věřit stejnému leaderu
Princip:
■   Procesy si mohou ‚stěžovat‘ na chování leadera z vlastní zkušenosti
■   Pokud je korektnímu zřejmé , že si stěžuje aspoň jeden korektní, ke
    stížnosti se připojí
■   Pokud si stěžuje více než polovina korektních procesů, vymění leadera
```

### Strana 186

```text
     Rotating Byzantine Leader
     Detection, algoritmus
• Algoritmus pracuje s koly kdy číslo kola určuje rank potenciálního lídra. Udržuje
  seznam procesů. které si na aktuálního lídra stěžovali a příznak, zdali si tento
  proces také na lídra stěžoval
• Pokud sezná, že lídr se chová nekorektně, zašle stížnost všem procesům


 upon event <bld, init> do
      round:=1; complainist:=[]; complained:=False;
      trigger <bld, Trust | LEADER(round)>

 upon event <bld, complain | p> such that p=leader(round)
                                 & complained=False
      complaint:=True;
      trigger <al, Send | q, COMPLAINT ,round] to all processes
```

### Strana 187

```text
     Rotating Byzantine Leader
     Detection, algoritmus
Zpracovává se událost, že přišla informace o stížnosti na aktuálního lídra a od tohoto procesu
stížnost ještě nemáme poznačenou → poznačíme si
upon event <al, Deliver | p, COMPLAINT, round]>
      such that r=round and complainist[p]=nill do
             complainist[p]=COMPLAINT
             if (#complainist)>f &
                          complained=FALSE then
                   complained=TRUE
                  trigger <al, Send | q, COMPLAINT, round]> to all processes
             else (#complainist)>2f then
                   round:=round+1; complainist:=[]
                   complained:=false;
                   trigger <bld, Trust | LEADER(round)>



                                                      Důvěru v nového lídra daného rankem
   Pokud je stěžovatelů více než                      round+1 získáme, pokud si na
   nekorektních a proces si ještě                     původního stěžovala napoloviční
   nestěžoval, připojí se (aspoň jeden                většína korektních
   korektní si stěžuje → s lídrem něco je)
```

### Strana 188

```text
Princip ‚lavinového‘ šíření stížností
                        Stežuje si korektní proces 3

                        Nekorektní proces 5 posílá stížnost jen
                        dvěma korektním 4 a 7

                        Stežuje si korektní proces 10


                        Stežuje si korektní proces 1


                        Korektní 4 a 7 mají >f stížností, připojují se

                        Stěžuje si nadpoloviční většina korektních,
                        všechny korektní se připojují ke stížnosti →
                        nakonec dojde k >2f stížnostem →
                                                      změna leadera
```

### Strana 189

```text
Rotating Byzantine Leader
Detection, princip
■ Protože se vyžaduje, aby přišla stížnost alespoň od f+1 procesů,
  nekorektní procesy samy nemohou vyprovokovat změnu lídra
■ Pokud obdržel 2f+1 stížností, je jisté, že si stěžuje alespoň f+1
  korektních
   – Tedy každý korektní obdržel jistě f+1 stížností
   – Zamezím případu, kdy všichni Byzanští pošlou stížnost
       procesu A, ostatním ne
   – Jeden korektní detekuje selhání a také posílá stížnost, pak
       proces A má f+1 stížností a ostatní 1
   – Jen pokud se podaří lavinově stížnost propagovat pro
       nadpoloviční většinu, je možné lídra změnit – proces A
       bude mít 3f+1 stížností, ostatní 2f+1 → změní lídra všichni
```

### Strana 190

```text
    Byzantské kvorum

■   Pokud z N procesů je f nekorektních, byzantských
                                             𝑁+𝑓
     byzantské kvorum je skupina více než        procesů
                                              2
■   Pak dvě quora obsahují alespoň jeden společný korektní proces
       Korektních procesů je 𝑁 − 𝑓
                                 𝑁+𝑓      𝑁−𝑓
       v kvoru je korektních >       −𝑓 =     (více než polovina)
                                  2        2
… a tedy dvě kvora musí mít alespoň jeden společný korektní proces
                                                   𝑁+𝑓
■   Princip: Protože quora o velikosti větší než       se vždy překrývají v
                                                    2
    korektním procesu, pokud jedno quorum potvrzuje hodnotu v,
    nemůže existovat jiné quorum potvrzující odlišnou hodnotu v′.
■   Důvod:
    Korektní procesy neposílají konfliktní informace.
```

### Strana 191

```text
Byzantský konzistentní
broadcast
■   Požadavky:
     –    Platnost (Validity)
     –    Bez zdvojení (No Duplication)
     –    Integrita (Integrity)
     –    Konzistence (Consistency): Pokud dva korektní procesy doručí zprávy 𝑚 a 𝑚′
          pak 𝑚 = 𝑚′

        (na rozdíl od shody (Agreement), podmínkou není, aby zprávu přijaly
        všechny korektní procesy)
Princip:
1. Vysilatel vysílá zprávu a procesy avizují (zasílají echo) její obdržení
    ostatním
2. Pokud proces obdrží byzantské quorum se stejnou zprávou, uloží tuto
    zprávu
```

### Strana 192

```text
    Authenticated Echo
    Broadcast, algoritmus
                                           upon event <bcb, init,bcb> do
Udržuje příznak, zda již na obdrženou
                                              sentecho:=False; delivered:=False; echos:=[ _ ]
zprávu odpověděl, jaké echa obdržel a
zdali již na základě ech doručil hodnotu
                                           upon event <bcb, b’cast | m> do
                                                  send([SEND, m]) to all processes
Broadcast rozesílá zprávu všem ostatním
                                           upon event <al, deliver | [SEND, m]> do
Při doručení zprávy rozesílá echo všem            from sender s and sendecho=False
ostatním                                          sentecho=True
                                                  trigger <Send | m> to all processes
Po obdržení echa si toto zaznamená
                                           upon event <al, deliver | [p, Echo, m]> do
                                                  if echos[p]=nill then echos[p]:=m
Pokud pro nějakou zprávu m dostal
byzantské quorum ech, zprávu di doručí                             𝑁+𝑓
                                           when #({echos[p]=m])>       and delivered=False
                                                                    2
                                                  delivered:=True; deliver(bcb, m)
```

### Strana 193

```text
      Authenticated Echo
      Broadcast, příklad
Pro 8 procesů, z nichž tři jsou nekorektní
                                      8+3     A   X   A   A   X   A   A       B     B      X         B
/ Byzantské, je byzantské kvórum >
                                       2
tedy 8
Byzanstský proces rozeslal zprávu a snaží
                                              A   A   A   A   A   A   A       B     B      A         B
se zmást korektní procesy (pěti poslal A,
třem B).
Proces může uložit pouze A, a to jen pokud                                8 × 𝐴 -> deliver(bcm, A)
Všechny Byzanstké pošlou echo(A). Jinou
                                              A   X   A   A   X   A   A        B     B     X         B
hodnotu (třeba B) není možné korektnímu
procesu k uložení vnutit

Všimněte si, že …                             A   B   A   A   B   A   A       B     B      B     B
 Pokud více než polovina korektních procesů
 neobdrží stejnou hodnotu, nelze kvorum
 vytvořit                                                                 5×𝐴,6×𝐵
```

### Strana 194

```text
Authenticated Echo
Broadcast, korektnost
■ Korektnost pro 𝑁 > 3𝑓
■ Konzistence vyplývá z toho, že každé dvě quora mají alespoň
  jeden společný korektní proces
    –   Pro korektnost může být libovolný poměr korektních a
        nekorektních procesů
■ Platnost ovšem vyžaduje více než dvoutřetinový počet korektních
   – Pokud by korektní proces vysílal a třetina nebo více
       nekorektních by neposlala echo, korektní procesy, kterých
                       𝑁+𝑓
       je tak méně než 2 by neuložily

■   Analýza (počet zpráv) 𝑂(𝑁 2 )
```
