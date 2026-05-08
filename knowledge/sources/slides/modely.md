# Modely distribuovanych systemu

Oficialni slidy extrahovane z PDF. Text je automaticky vytazeny pres `pdftotext -layout`; u obrazkovych nebo diagramovych stran kontroluj originalni PDF.

## Metadata

| Pole | Hodnota |
|---|---|
| Zdroj | [[raw/PRL2526_MODELY.pdf]] |
| Soubor | `PRL2526_MODELY.pdf` |
| Stran | 37 |
| PDF title | Modely a jazyky pro distribuovanÉ systémy |
| Creator | Microsoft® PowerPoint® LTSC |
| Page size | 960 x 540 pts |

## Pouziti

- Pouzivej jako oficialni oporu pro definice, algoritmy, terminologii a slozitosti.
- Pokud je strana zalozena hlavne na obrazku, cituj stranu a zkontroluj originalni PDF.
- Pro exam historii porad preferuj `knowledge/exams/**/term-*.md`; slidy slouzi jako vykladovy zdroj.

## Text po stranach

### Strana 1

```text
MODELY KOMUNIKUJÍCÍCH
            PROCESŮ
              CSP, π – kalkul, OCCAM
```

### Strana 2

```text
CSP – Communicating Sequential
Processes
■ Communicating Sequential Processes (CSP) je formální jazyk pro modelování
  paralelních systémů komunikujících předáváním zpráv.
■ C. A. R. HOARE 1978
■ Výchozí pro další systémy, jako jsou napríkad π-kalkul nebo OCCAM
```

### Strana 3

```text
OCCAM

■ Původně založen na Hoareho CSP, později inspirován a rozšířen o prvky z PI-kalkulu
  (OCCAM PI)
■ Navržen tak, aby měl formální sémantikou vhodnou pro automatickou transformaci
  programu
■ Transformace programů zapsaných v OCCAMu přímo na hardware (transputery, SW-
  HW codesign)
■ Řada jazyků má k dispozici OCCAM – like rozšíření pro paralelní procesy, včetně JAVA
```

### Strana 4

```text
OCCAM, základní primitiva
■   Occam primitivum je proces a je jednoho z následujících pěti druhů:
         Přiřazení            x := y + 2
         Vstup                keyboard ? char
         Výstup               screen ! char
         Skip                 SKIP – NOP, které se ukončí
         Stop                 STOP –- NOP, které se nikdy neukončí
■   Kanály poskytují možnost komunikace mezi procesy, nebufferovanou point-to-point synchronní
    komunikaci
■   Kanály mají definovaný typ zpráv, které přenášejí




                                       Channel c
                            c!x                           c?y
```

### Strana 5

```text
Sekvenční procesy
■ SEQ executes sub-processes sequentially
         SEQ
                   keyboard ? char –- read char from keyboard
                   screen ! char -- write char to screen
Můžeme replikovat sekvence
         SEQ i = 0 FOR array.size
                   stream ! data.array[i]
… je stejné jako
         SEQ
                   stream ! data.array[0]
                   stream ! data.array[1]
                   ...
```

### Strana 6

```text
Kompozice paralelních procesů
■ PAR spustí vykonávání paralelních procesů
        PAR
                keyboard(kbd.to.ed)
                editor(kbd.to.ed,ed.to.screen)
                screen(ed.to.screen)




                                  ed.to.screen   secreen


                       editor

                                  kbd.to.ed      keyboard
```

### Strana 7

```text
PAR pro paralelní vykonávání procesů
■ Příklad: Square pipe
                WHILE next <> EOF
                      SEQ
                            x := next
                            PAR
                                  in ? next
                                  out ! x * x
■ Omezení přístupu paralelních procesů k datům
   – Variables modified in one arm of PAR cannot be read or written in other parts
     of PAR, e.g., PAR -- this PAR is invalid
                SEQ
                         mice := 42 -- assigns to mice
                         c ! 42
                         c ? mice -- assigns to mice
```

### Strana 8

```text
Replikovaný PAR
■ Replikovaný PAR může být použit pro vytvoření pole paralelních procesů
        PAR
                    farmer()
                    PAR i = 0 FOR 4 -- count must be constant
                          worker(i)


                                                             Pole komunikačních kanálů propojuje
                                           farmer()
                                                             dělníky s matrem, v kódu nejsou uvažováni




                               worker(1)              worker(2)                worker(3)
        worker(0)
```

### Strana 9

```text
Vyrovnávací paměť (Buffer)


 IN        OUT
                      WHILE TRUE
                         BYTE b:
                         SEQ
                             in ? b
                             out ! b
```

### Strana 10

```text
Dvojitý Buffer

                       CHAN OF BYTE ch:
                       PAR
                           WHILE TRUE
 IN        CH    OUT          BYTE b:
                              SEQ
                                  in ? b
                                  ch ! b
                           WHILE TRUE
                              BYTE b:
                              SEQ
                                  ch ? b
                                  out ! b
```

### Strana 11

```text
Dvojitý Buffer
                       WHILE TRUE
                          left ? packet
                          out ! Packet
                          right ?   packet
    LEFT                  out ! packet
                 OUT
    RIGHT


                       WHILE TRUE
                          PAR
                              left ? packet
                                  out ! Packet
                              right ? packet
                                  out ! packet
```

### Strana 12

```text
Alternace
■ ALT combines a number of processes only one of which is executed
■ Každý proces má strážce:
   – vstup input on channel
   – čeká na časovač
   – Čeká na splnění boolovské podmínky
      ALT
              left ? packet -- guard input statement
                       out ! packet
              right ? packet –- guard input statement
                       out ! packet
                                                     LEFT
                                                                       OUT
                                                     RIGHT       ALT
```

### Strana 13

```text
Alternace
ALT
           strazce1
                 proces1
…                                        WHILE TRUE
           strazcen                         ALT
                 proces                         left ? packet
                                                    out ! packet
                                                right ? packet
Strážci mohou čekat na                              out ! packet
1, vstup
         in ? data
2, platnost boolovské podmínky & vstup
         not.empty & in ? data
2, platnost boolovské podmínky & SKIP    LEFT
                                                           OUT
         not.empty & SKIP                          ALT
                                         RIGHT
```

### Strana 14

```text
OCCAM – deklarace procedur
-- other parts to program
        PROC buff(CHAN OF BYTE in, out)
                 WHILE TRUE
                            BYTE x:
                            SEQ
                                      in ? x
                                      out ! x :
-- end of buff
        CHAN OF BYTE comms, buffer.in, buffer.out:
                 PAR
                            buff(buffer.in, comms)
                            buff(comms, buffer.out)
```

### Strana 15

```text
Π-KALKUL
```

### Strana 16

```text
π - kalkul

■ Formální nástroj pro modelování paralelních a mobilních procesů
■ Jazyk + axiomy + redukční pravidla
■ Syntax:
   – Předpona  je v jednom z následujících tvarů 𝜋 = ҧ𝑥𝑦 𝑥 𝑧       𝜏 | [x=y]
   – Proces je pak zapsán jako
                      𝑃 ∷= 𝑀 𝑃 𝑃′ 𝜗𝑧𝑃 ! 𝑃
                      𝑀 ∶≔ 𝟎 𝜋. 𝑃 𝑀 + 𝑀′
```

### Strana 17

```text
π – kalkul, procesy

0           -   prázdný (ukončený) proces
𝜋. 𝑃        –   předpona
 𝑥=𝑦 𝑃      -   test
𝑃 + 𝑃′      -   nedeterministický výběr
𝑃 | 𝑃′      -   paralelní kompozice
(𝜗𝑧)𝑃       -   omezení jména
!𝑃          -   replikace
```

### Strana 18

```text
Strukturální kongruence
                                         𝑀+𝟎 ≡ 𝑀
 V relaci strukturální kongruence jsou
 procesy, které jsou stejné,             M1 + M2 ≡ M2 + M1
 pouze jinak zapsané.                    M1 + (M2 + M3 ) ≡ (M1 +M2 + M3 )
 V π–kalkulu je strukturální             𝑃|𝟎 ≡ 𝑃
 kongruence nejmenší kongruencí, která
 splňuje axiomy =>                       𝑃1 |𝑃2 ≡ 𝑃2 |𝑃1
                                         (𝑃1 𝑃2 𝑃3 ≡ 𝑃1 (𝑃2 |𝑃3 )
                                         ! 𝑃 ≡ 𝑃|! 𝑃
                                           ϑa 𝟎 ≡ 𝟎
                                           𝜗𝑎 𝜗𝑏 𝑃 ≡ 𝜗𝑏 𝜗𝑎 𝑃
                                          x = x π. P ≡ π. P
                                         P1 | 𝜗𝑎 𝑃2 ≡ 𝜗𝑎 (P1 |𝑃2 )
                                                         𝑝𝑜𝑘𝑢𝑑 𝑎 ∈ 𝑓𝑛(𝑃1 )
```

### Strana 19

```text
π – kalkul, redukční pravidla
Je možné přejmenovávat volná jména v procesu, nebo

(COMM)                      ҧ
                           𝑥𝑧.𝑃 𝑥 𝑦 .𝑄→ 𝑃 𝑄 𝑦/𝑧


                                       (aplikuje substituci na všechna volná jména v Q)

                             𝑃→𝑄
(R-PAR)                    𝑃 𝑅→𝑄 𝑅

                               𝑃→𝑄
(R-RES)                     𝜗𝑥 𝑃→(𝜗𝑥)𝑄

                           𝑃≡𝑃′→𝑄≡𝑄′
(R-STRUCT)
                             𝑃→𝑄′


(RESTRUCT)
                           𝜏.𝑃+𝑀→𝑃
                              𝑃→𝑄
(MATCH)                     [𝑥=𝑥]𝑃→𝑄
```

### Strana 20

```text
π – kalkul, komunikace
■ Synchronní přes pojmenovaný komunikační kanál

                                       𝑥 𝑦 . 𝑃| ҧ
                                               𝑥𝑎. 𝑃′


Tj. Procesy komunikují přes komunikační kanál kanál x
                                         𝑥𝑎. 𝑃′ → 𝑃[𝑦/𝑎] 𝑃′
                                   𝑥 𝑦 .𝑃 ҧ


■ Jiný příklad ukazuje mobilitu komunikujících kanálů:


                 𝑥𝑏. 𝟎 𝑥 𝑦 . ത
                  ҧ          𝑦𝑎. 𝟎 𝑏 𝑤 . 𝑃|𝑐 𝑧 . 𝑃′ →
                    ത 𝟎 𝑏 𝑤 . 𝑃|𝑐 𝑧 . 𝑃′ ≡
                 𝟎 𝑏𝑎.
                 ത 𝟎 𝑏 𝑤 . 𝑃 𝑐 𝑧 . 𝑃′ →
                 𝑏𝑎.
                 𝟎|𝑃 𝑤/𝑎 |𝑐 𝑧 . 𝑃′ ≡ 𝑃 𝑤/𝑎 |𝑐 𝑧 . 𝑃′
```

### Strana 21

```text
π – kalkul, omezené komunikační
kanály
■ Omezení se používá pro soukromé – skryté kanály nějaké skupiny procesů
■ Na rozdíl od CSP, kde omezení nemohlo být rozšířeno, v π – kalkulu mohou procesy v
  dosahu omezení poslat jméno skrytého kanálu vnějšímu procesu a rozšířit tak o něj
  toto omezení … (Scope Extrusion)
                       ഥ 𝑺 𝑹 |𝑏 𝑐 . ҧ𝑐𝑑. 𝑃 → ϑa 𝑺 𝑹|ഥ
                    ϑa 𝒃𝒂.                          𝒂𝒅. 𝑷

               ഥ 𝑺
               𝒃𝒂.       R   𝑏 𝑐 . ҧ𝑐𝑑. 𝑃       𝑺       R   ഥ
                                                            𝒂𝒅. 𝑷


                     a                              a
                         b                              b
```

### Strana 22

```text
π – kalkul, sématika se štítkovanými
přechody
■ Provedení akce znázorňujeme štítkovanou přechodovou relací →α kde α je akce
■ α může být:
                 𝑥𝑦                  vstupní akce
                 𝑥𝑦
                  ҧ                  otevřená výstupní akce
                 𝑥ҧ 𝑧                výstupní akce s omezeným jménem ‘z’
                 𝜏                   tichá akce
Příklad:
                                            ҧ𝑠𝑎. ҧ𝑠𝑏. 𝟎 → ҧ𝑠𝑎 ҧ𝑠𝑏. 𝟎
                                          𝑎 𝑦 . 𝑄 →𝑎𝑧 𝑄[𝑦/𝑧]
■ Tiché akce 𝜏 nejsou pozorovatelné (například i komunikace v rámci procesu,
  nedeterministický výběr apod.)
Příklad:
                                                    𝑣𝑢. 𝟎 →𝜏 ҧ𝑠𝑏. 0 𝑧 𝑦 . 𝟎 𝑠 𝑢 . ത
                     ҧ𝑠𝑎. ҧ𝑠𝑏. 𝟎 𝑧 𝑦 . 𝟎 𝑠 𝑣 . 𝑠 𝑢 . ҧ                            𝑎𝑢. 𝟎
```

### Strana 23

```text
Simulace
Relace simulace S, procesy P a Q
Silná simulace                                 Slabá simulace
                                                                    τ
                                               Pokud 𝑃 𝑺 𝑄 a 𝑃 → 𝑃′ pak existuje 𝑄′
                     𝑎                                       τ∗
Pokud 𝑃 𝑺 𝑄 a 𝑃 → 𝑃′ pak existuje 𝑄′            takové, že 𝑄 → 𝑄′ a 𝑃′ 𝑺 𝑄′
                 𝑎                                                  𝑎
 takové, že 𝑄 → 𝑄′ a 𝑃′ 𝑺 𝑄′                   Pokud 𝑃 𝑺 𝑄 a 𝑃 → 𝑃′ pak existuje 𝑄′
                                                             τ∗𝑎τ∗
                                                takové, že 𝑄       𝑄′ a 𝑃′ 𝑺 𝑄′


                                       𝑃           𝑆       Q            𝑃       𝑆     Q
     𝑃           𝑆       Q
                                           τ                   τ∗           a             τ∗ a τ∗
         a                   a


                                       𝑃′         𝑆        Q′           𝑃′      𝑆     Q′
     𝑃′          𝑆       Q′
```

### Strana 24

```text
Bisimulace, bisimilarita
Bisimulace je relace taková, že procesy se mohou simulovat navzájem
Bisimilarita je relace mezi dvěma procesy, pro které existuje (alespoň jedna) relace
simulace, je sjednocením všech bisimulací

                                Bisimulace
                                S1={(1,A),(2,B),(3,C),(4,B),(5,C),(A,1),(B,2),(C,3),(B,4),(C,5)}
     1                          S2={(1,C),(2,B),(3,C),(4,B),(5,C),(C,1),(B,2),(C,3),(B,4),(C,5)}
         a
                                S3={(2,B),(3,C),(4,B),(5,C),(B,2),(C,3),(B,4),(C,5)}
     2                          S4={(3,A),(4,B),(5,C),(A,3),(B,4),(C,5)}
         b
                                S5={(3,C),(4,B),(5,C),(3,C),(B,4),(C,5)}
     3            A             S6={(4,B),(5,A),(5,C),(B,4),(A,5),(C,5)}
         a            a
     4       a    B       a     Bisimilarita
         b            b         R={(1,A),(1,C),(2,B),(3,A),(3,C),(4,B),(5,A),(5,C),
     5            C                  (A,1),(C,1),(B,2),(A,3),(C,3),(B,4),(A,5),(C,5)}
```

### Strana 25

```text
π – kalkul, kontext, kongruence
■ Kontext zapisujeme s uvedením místa [.] na místo 0 procesu, který není degenerující
  (první na některé pozici nedeterministického výběru)
■ Proces P, který má být proveden v kontextu C pak C[P]
■ Procesy jsou v relaci kongruence, pokud jsou v této relaci pro libovolný kontext

                                   𝐶0 : 𝜗𝑧 . ! 𝑧 𝑤 . ഥ 𝑤𝑎. 𝟎)
                             𝐶1 : 𝑥 𝑧 . ! (𝜗𝑤)(𝑧 𝑤 . . + 𝑦 𝑣 . 𝟎)


■ Aplikací procesu
                  𝐶0 ! ҧ𝑧𝑏. 𝟎 = 𝜗𝑧 (! ҧ
                                     𝑧𝑏. 𝟎 | ! 𝑧 𝑤 . ഥ
                                                     𝑤𝑎. 𝟎 )
                  𝐶1 ! ҧ𝑧𝑏. 𝟎 = 𝑥 𝑧 . ! (𝜗𝑤) 𝑧 𝑤 . ! ҧ𝑧𝑏. 𝟎 + 𝑦 𝑣 . 𝟎


■ Kongruence je relace S, kde P, Q ∈ 𝑆 ⇒ (𝐶 𝑃 , 𝐶[𝑄]) ∈ 𝑆 pro jakýkoliv kontext C
```

### Strana 26

```text
π – kalkul, kongruence
■ ‚Nesmí být degenerující‘ – příklad
                 P1 = τ. 𝐴. 𝟎 P2 = 𝐴. 𝟎 (kongruence)
                    . + P3 : τ. A + P3 vs. A + P3
■ Kongruence je ekvivalence, která platí pro aplikaci jakékoliv substituce
Například procesy
                           ത
                 P1 = a(a)|𝑏𝑏       a                   ത + 𝑏𝑏.
                                             P2 = a a . 𝑏𝑏  ത 𝑎(𝑎)
        nejsou kongruencí, protože pro 𝑥 𝑎 . | ҧ𝑥𝑏 a substituci σ = {[𝑏/𝑎]}
                             ത a
                 P1 σ = 𝑏 𝑏 |𝑏𝑏                           ത + 𝑏𝑏.
                                             P2 σ = 𝑏 𝑏 . 𝑏𝑏  ത 𝑏 𝑏
Kongruencí jsou procesy
                           ത
                 P1 = a(a)|𝑏𝑏       a                   ത + 𝑏𝑏.
                                             P2 = a a . 𝑏𝑏  ത 𝑎 𝑎 + 𝑎=𝑏 τ
```

### Strana 27

```text
π – kalkul, pozorování
■   Pozorování se vztahují ke komunikačním kanálů, které nejsou soukromé pro nějakou skupinu
    procesů
■   Zápis 𝑷 ↓ 𝒙 – process P má jméno x jako vstup
■   Zápis 𝑷 ↓ 𝒙
              ഥ - process P má jméno x jako výstup
■   Procesy jsou pozorovatelem neroznatelné, pokud mají stejné chování na výstupech
■   Příklad:
                                   ҧ 𝟎 𝑧 𝑦 .𝟎 𝑞 𝑣 .𝑡 𝑢 . ҧ
                    P = ϑ𝑧 ( ҧ𝑠𝑎. 𝑡𝑏.                   𝑣𝑢. 𝟎|𝜏. 𝑤 𝑧 . 𝟎)


P ↓ 𝑎 ??? – ne, je subjekt komunikace, ne komunikační kanál (vstup / výstup)
P ↓ 𝑠ҧ ??? – ano, agent může poslat jméno po kanálu s
P ↓ 𝑡ҧ ??? – ne, agent nyní nemůže posílat jméno po kanálu t
P ↓ 𝑞 ??? – ano, agent může přijmout jméno po kanálu q
P ↓ 𝑡 ??? – ne, agent nyní nemůže přijímat jméno po kanálu t
P ↓ 𝑧 ??? - ne, jméno z je privátní procesu a není pozorovatelné z vnějšku
P ↓ 𝑤 ??? – ne, agent nyní nemůže použít w, ale platí P ⇓ 𝑤, viz dále
```

### Strana 28

```text
π – kalkul, ‘barbed’ simulace, bisimulace
Centrem zájmu v oblasti procesních algeber je podobnost procesů
Jeden proces může simulovat jiný proces (relace simulace), založena na pozorováních -> barbed
simulace
Silná ‘barbed’ bisimulace ->
Procesy P a Q jsou v relaci silné bisimulace S(𝑃, 𝑄) pokud
         𝑃 ↓ 𝑥 implikuje Q ↓ 𝑥
         𝑃 →𝜏 𝑃′ implikuje 𝑄 →𝜏 𝑄′pro nějaké 𝑄 ′ a S(𝑃′ , 𝑄 ′ )
         𝑄 ↓ 𝑥 implikuje 𝑃 ↓ 𝑥
         𝑄 →𝜏 𝑄′implikuje 𝑃 →𝜏 𝑃′pro nějaké 𝑄 ′ a S(𝑃′ , 𝑄 ′ )
Slabá ‘barbed’ bisimulace -> tiché akce nejsou pozorovatelné, proto použijeme relaci pro
pozorovatelné akce ⇒𝛼
Jednou nebo více tichými akcemi přejde proces do stavu dle relace.
                                          ⇒ ≝ (→𝜏 )∗
Pak pro akci 𝛼
                                            ⇒𝛼 ≝ ⇒→𝛼 ⇒
Zápis 𝑷 ⇓ 𝒙 značí, že proces P může tichými akcemi přejít ⇒ do stavu, kde 𝑷 ↓ 𝒙
```

### Strana 29

```text
π – kalkul, silná simulace, příklad
Pozor! Mohou být procesy P a Q v relaci silné bisimulace?
                                    𝑃 = 𝜏. (𝑎 𝑥 𝑏(𝑦) + 𝑎 𝑥 𝑐(𝑧))
                                    𝑄 = 𝜏. 𝑎 𝑥 𝑏(𝑦) + 𝜏. 𝑎 𝑥 𝑐(𝑧)
Může Q simulovat krok?
         𝑃 →𝜏 𝑃 ′
         𝜏. (𝑎 𝑥 𝑏(𝑦) + 𝑐 𝑥 𝑐(𝑧)) →𝜏 𝑎 𝑥 𝑏(𝑦) + 𝑎 𝑥 𝑐(𝑧)
Nemůže, protože
          𝑄 →𝜏 𝑄 ′
         buď         1, 𝜏. 𝑎 𝑥 𝑏(𝑦) + 𝜏. 𝑎 𝑥 𝑐(𝑧) →𝜏 𝑎 𝑥 𝑏(𝑦)
         nebo        2, 𝜏. 𝑎 𝑥 𝑏(𝑦) + 𝜏. 𝑎 𝑥 𝑐(𝑧) →𝜏 𝑎 𝑥 𝑐(𝑧)
Pak v případě 1 𝑃′ →𝑎(𝑥) 𝑃′′ = 𝑐(𝑧) nemůže 𝑄′ →𝑎(𝑥) 𝑄′′ = 𝑏 𝑦 ,
                     protože ¬(𝑃′′ ↓ 𝑐 → 𝑄′′ ↓ 𝑐) a ¬(𝑄′′ ↓ 𝑏 → 𝑃′′ ↓ 𝑏)
V případě 2 𝑃′ →𝑎(𝑥) 𝑃′′ = 𝑏(𝑦) nemůže 𝑄′ →𝑎(𝑥) 𝑄′′ = 𝑐 𝑧
                     protože ¬(𝑃′′ ↓ 𝑏 → 𝑄′′ ↓ 𝑏) a ¬(𝑄′′ ↓ 𝑐 → 𝑃′′ ↓ 𝑐)
```

### Strana 30

```text
π – kalkul, ‘late’ / ’early’ simulace
■   ‘pozdní’ late či ‘včasná’ early simulace, založená na štítkovaných přechodech
■   Liší se v tom, jak jsou chápány vstupní akce a to se týká převážně procesů s nedeterministickým
    výběrem.
■   Pro obě late/early simulace S:
                   α
         Pokud 𝑃 → 𝑃′ , akce není vstupní α ≠ 𝑥 𝑦 a vázané jméno v α není volné v P nebo Q
                                                  α
         (𝑏𝑛(α) ∉ 𝑓𝑛(𝑃, 𝑄)), pak pro nějaké 𝑄′, 𝑄 → 𝑄′ jsou tyto procesy v relaci late nebo early
         simulace 𝑃′ 𝑆 𝑄′
    Vstupní akce pro late simulaci
                  𝑥(𝑦)                                                α
         Pokud 𝑃      𝑃′ , y ∉ 𝑓𝑛(𝑃, 𝑄), pak pro nějaký proces 𝑄′ , 𝑄 → 𝑄′ a pro jakékoliv jméno w
         jsou tyto procesy v relaci late simulace 𝑃′ [𝑤/𝑦] 𝑆 𝑄′ [𝑤/𝑦]
    Vstupní akce pro early simulaci
                  𝑥(𝑦)                                                                 α
         Pokud 𝑃       𝑃′ , y ∉ 𝑓𝑛(𝑃, 𝑄), pak pro všecha jména w existuje nějaké 𝑄′ , 𝑄 → 𝑄′ a
         tyto procesy jsou v relaci early simulace 𝑃′ [𝑤/𝑦] 𝑆 𝑄′ [𝑤/𝑦]
```

### Strana 31

```text
π – kalkul, ‘late’/’early’ simulace, příklad
Uvažujme dva procesy
        P= x(y).τ.0 + x(y).O
        Q= P + x(y).[x=y].τ.0
Jsou tyto procesy v relaci late bisimulace?
         Nejsou, při late bisimulaci nedokáže proces P simulovat krok x(y) v případě, že
         proces Q vybere x(y).[x=y].τ.0 podproces. Příjem jména x za vstupní y způsobí
         jiné chování (provedení τ) než příjem jiného jména za y (způsobí zablokování
         procesu, tedy 0). Tedy P nedokáže jedním z možných podprocesů x(y).τ.0 či
         x(y).O nedokáže simulovat všechna možná přijímaná jména.
Jsou tyto procey v relace early bisimulace?
         Jsou, v tomto případě je potřeba, aby pro každé jméno přijímané přes x(y)
         existoval podproces, který ‘odpovídá’ podprocesu druhého procesu. Tedy pokud
         by pro přijímané jméno proces Q (nedeterministicky) zvolil podproces s
         testem, tak P může reagovat na základě jména, jestli odpovídající jeho
         podproces je τ.0 (v případě, že přijímané jméno je x a test tedy projde), nebo 0
```

### Strana 32

```text
π – kalkul, příklady

                            ത
■ Forwarder FW a, 𝑏 = 𝑎 𝑧 . 𝑏𝑧

        𝑎𝑥 FW a, 𝑏 = ത
        ത                     ത → 𝑏𝑥
                     𝑎𝑥 𝑎 𝑧 . 𝑏𝑧  ത

        𝑎𝑥 𝜗𝑏 FW a, 𝑏 FW 𝑏, 𝑐
        ത                           =ത           ത 𝑏 𝑧 . ҧ𝑐𝑧 →
                                     𝑎𝑥 𝜗𝑏 𝑎 𝑧 . 𝑏𝑧
                                    ത 𝑏 𝑧 . ҧ𝑐𝑧 → ҧ𝑐𝑥
                                 𝜗𝑏 𝑏𝑥
                                ത ҧ𝑐𝑑)
■ Duplikátor D 𝑎, 𝑏, 𝑐 = 𝑎 𝑑 . (𝑏𝑑|

        𝑎𝑥|D 𝑎, 𝑏, 𝑐 = ത
        ത                        ത ҧ𝑐𝑑) → 𝑏𝑥|
                       𝑎𝑥|𝑎 𝑑 . (𝑏𝑑|      ത ҧ𝑐𝑥
■ Generátor nového jména 𝑁𝑁 𝑎 = 𝑎 𝑥 . 𝜗𝑏 ҧ𝑥𝑏

       ҧ𝑖o 𝑁𝑁 𝑖 = ҧ𝑖𝑜 𝑖 𝑜 . 𝜗𝑏 ҧ𝑜𝑏 → 𝜗𝑏 ( ҧ𝑜𝑏)
```

### Strana 33

```text
     π – kalkul, přepínání stanic
𝐶𝑎𝑟 𝑡𝑎𝑙𝑘 = 𝑡𝑎𝑙𝑘 < 𝑑𝑎𝑡𝑎 >. 𝐶𝑎𝑟(𝑡𝑎𝑙𝑘)
𝑆𝑡𝑎𝑡𝑖𝑜𝑛𝐴 𝑡𝑎𝑙𝑘, 𝑠𝑤 = 𝑡𝑎𝑙𝑘 𝑥 . 𝑃𝑟𝑜𝑐𝑒𝑠𝑠 𝑥 . 𝑆𝑡𝑎𝑡𝑖𝑜𝑛𝐴 𝑡𝑎𝑙𝑘, 𝑠𝑤 + 𝑠𝑤 < 𝑡𝑎𝑙𝑘 >. 𝟎
𝑆𝑡𝑎𝑡𝑖𝑜𝑛𝐵 𝑠𝑤 = 𝑠𝑤 𝑡 . 𝐵𝑎𝑠𝑒𝑆𝑡𝑎𝑡𝑖𝑜𝑛(𝑡)
𝐵𝑎𝑠𝑒𝑆𝑡𝑎𝑡𝑖𝑜𝑛 𝑡 = 𝑡 𝑥 . 𝑃𝑟𝑜𝑐𝑒𝑠𝑠 𝑥 . 𝐵𝑎𝑠𝑒𝑆𝑡𝑎𝑡𝑖𝑜𝑛(𝑡)

𝑪𝒂𝒓 𝒕𝒂𝒍𝒌 |𝑺𝒕𝒂𝒕𝒊𝒐𝒏𝑨 𝒕𝒂𝒍𝒌, 𝒔𝒘 |𝑺𝒕𝒂𝒕𝒊𝒐𝒏𝑩(𝒔𝒘)
𝑡𝑎𝑙𝑘 < 𝑎ℎ𝑜𝑗 >. 𝐶𝑎𝑟(𝑡𝑎𝑙𝑘) | 𝑡𝑎𝑙𝑘 𝑥 . 𝑃𝑟𝑜𝑐𝑒𝑠𝑠 𝑥 . 𝑆𝑡𝑎𝑡𝑖𝑜𝑛𝐴 𝑡𝑎𝑙𝑘, 𝑠𝑤 + 𝑠𝑤 < 𝑡𝑎𝑙𝑘 >. 𝟎|𝑆𝑡𝑎𝑡𝑖𝑜𝑛𝐵(𝑠𝑤)
𝐶𝑎𝑟(𝑡𝑎𝑙𝑘) | 𝑃𝑟𝑜𝑐𝑒𝑠𝑠 𝑎ℎ𝑜𝑗 . 𝑆𝑡𝑎𝑡𝑖𝑜𝑛𝐴 𝑡𝑎𝑙𝑘, 𝑠𝑤 |𝑆𝑡𝑎𝑡𝑖𝑜𝑛𝐵(𝑠𝑤)
𝑡𝑎𝑙𝑘 < 𝑝𝑟𝑙 >. 𝐶𝑎𝑟(𝑡𝑎𝑙𝑘)| 𝑆𝑡𝑎𝑡𝑖𝑜𝑛𝐴 𝑡𝑎𝑙𝑘, 𝑠𝑤 |𝑆𝑡𝑎𝑡𝑖𝑜𝑛𝐵(𝑠𝑤)
𝑡𝑎𝑙𝑘 < 𝑝𝑟𝑙 >. 𝐶𝑎𝑟(𝑡𝑎𝑙𝑘) | 𝑡𝑎𝑙𝑘 𝑥 . 𝑃𝑟𝑜𝑐𝑒𝑠𝑠 𝑥 . 𝑆𝑡𝑎𝑡𝑖𝑜𝑛𝐴 𝑡𝑎𝑙𝑘, 𝑠𝑤 + 𝑠𝑤 < 𝑡𝑎𝑙𝑘 >. 𝟎 |𝑆𝑡𝑎𝑡𝑖𝑜𝑛𝐵(𝑠𝑤)
𝑡𝑎𝑙𝑘 < 𝑝𝑟𝑙 >. 𝐶𝑎𝑟(𝑡𝑎𝑙𝑘) | 𝑠𝑤 < 𝑡𝑎𝑙𝑘 >. 𝟎 | 𝑠𝑤 𝑡 . 𝐵𝑎𝑠𝑒𝑆𝑡𝑎𝑡𝑖𝑜𝑛(𝑡)
𝑡𝑎𝑙𝑘 < 𝑝𝑟𝑙 >. 𝐶𝑎𝑟(𝑡𝑎𝑙𝑘) |𝐵𝑎𝑠𝑒𝑆𝑡𝑎𝑡𝑖𝑜𝑛(𝑡𝑎𝑙𝑘)
𝑡𝑎𝑙𝑘 < 𝑝𝑟𝑙 >. 𝐶𝑎𝑟(𝑡𝑎𝑙𝑘) |𝑡𝑎𝑙𝑘 𝑥 . 𝑃𝑟𝑜𝑐𝑒𝑠𝑠 𝑥 . 𝐵𝑎𝑠𝑒𝑆𝑡𝑎𝑡𝑖𝑜𝑛(𝑡𝑎𝑙𝑘)
```

### Strana 34

```text
π – kalkul, příklad, neomezený buffer

Definujeme procesy modelující neomezený buffer
𝑩 i, 𝑜 = 𝑖 𝑥 . 𝑪(𝑥, 𝑖, 𝑜)
𝑪 𝑥, 𝑖, 𝑜 = ҧ𝑜𝑥. 𝑩 𝑖, 𝑜 + 𝑖 𝑦 . (𝑪 𝑦, 𝑖, 𝑜 ~𝑪 𝑥, 𝑖, 𝑜 )
𝑪 y, i, o ~𝑪(x, i, o) = 𝜗𝑚 (𝑪 𝑦, 𝑖, 𝑚 |𝑪 𝑥, 𝑚, 𝑜 )


Prozkoumáme chování procesu
ҧ𝑖𝑎. ҧ𝑖𝑏. 𝑜 𝑥 . 𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 | 𝑩 i, 𝑜
```

### Strana 35

```text
π – kalkul, příklad, neomezený buffer
                                                               𝑩 i, 𝑜 = 𝑖 𝑥 . 𝑪(𝑥, 𝑖, 𝑜)
                                                               𝑪 𝑥, 𝑖, 𝑜 = ҧ𝑜𝑥. 𝐵 𝑖, 𝑜 + 𝑖 𝑦 . (𝑪 𝑦, 𝑖, 𝑜 ~𝑪 𝑥, 𝑖, 𝑜 )
                                                               𝑪 y, i, o ~𝑪(x, i, o) = 𝜗𝑚 (𝑪 𝑦, 𝑖, 𝑚 |𝑪 𝑥, 𝑚, 𝑜 )


ҧ𝑖𝑎. ҧ𝑖𝑏. 𝑜 𝑥 . 𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 | 𝑩 i, 𝑜 =

ҧ𝑖𝑎. ҧ𝑖𝑏. 𝑜 𝑥 . 𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 | 𝑖 𝑥 . 𝑪(𝑥, 𝑖, 𝑜) →
ҧ𝑖𝑏. 𝑜 𝑥 . 𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 | 𝑪 𝑎, 𝑖, 𝑜 =

ҧ𝑖𝑏. 𝑜 𝑥 . 𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 | ҧ𝑜𝑎. 𝑩 𝑖, 𝑜 + 𝑖 𝑦 . (𝑪 𝑦, 𝑖, 𝑜 ~𝑪 𝑎, 𝑖, 𝑜 ) →
𝑜 𝑥 . 𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 | (𝑪 𝑏, 𝑖, 𝑜 ~𝑪 𝑎, 𝑖, 𝑜 ) =
𝑜 𝑥 . 𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 | 𝜗𝑚 (𝑪 𝑏, 𝑖, 𝑚 |𝑪 𝑎, 𝑚, 𝑜 ) =
𝑜 𝑥 . 𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 |
   𝜗𝑚 ഥ
      𝑚𝑏. 𝑩 𝑖, 𝑚 + 𝑖 𝑦 . 𝑪 𝑦, 𝑖, 𝑚 ~𝑪 𝑏, 𝑖, 𝑚            ҧ𝑜𝑎. 𝑩 𝑚, 𝑜 + 𝑚 𝑦 . 𝑪 𝑦, 𝑚, 𝑜 ~𝑪 𝑎, 𝑚, 𝑜
```

### Strana 36

```text
π – kalkul, příklad, neomezený buffer
                                               𝑩 i, 𝑜 = 𝑖 𝑥 . 𝑪(𝑥, 𝑖, 𝑜)
                                               𝑪 𝑥, 𝑖, 𝑜 = ҧ𝑜𝑥. 𝐵 𝑖, 𝑜 + 𝑖 𝑦 . (𝑪 𝑦, 𝑖, 𝑜 ~𝑪 𝑥, 𝑖, 𝑜 )
                                               𝑪 y, i, o ~𝑪(x, i, o) = 𝜗𝑚 (𝑪 𝑦, 𝑖, 𝑚 |𝑪 𝑥, 𝑚, 𝑜 )



𝑜 𝑥 . 𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 |
   𝜗𝑚 ഥ
      𝑚𝑏. 𝑩 𝑖, 𝑚 + 𝑖 𝑦 . 𝑪 𝑦, 𝑖, 𝑚 ~𝑪 𝑏, 𝑖, 𝑚      ҧ𝑜𝑎. 𝑩 𝑚, 𝑜 +
      𝑚 𝑦 . 𝑪 𝑦, 𝑚, 𝑜 ~𝑪 𝑎, 𝑚, 𝑜    →
𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 | 𝜗𝑚 ഥ
                    𝑚𝑏. 𝑩 𝑖, 𝑚 + 𝑖 𝑦 . 𝑪 𝑦, 𝑖, 𝑚 ~𝑪 𝑏, 𝑖, 𝑚      𝑩 𝑚, 𝑜 =
𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 | 𝜗𝑚 ഥ
                    𝑚𝑏. 𝑩 𝑖, 𝑚 + 𝑖 𝑦 . 𝑪 𝑦, 𝑖, 𝑚 ~𝑪 𝑏, 𝑖, 𝑚      𝑚 𝑥 . 𝑪 𝑥, 𝑚, 𝑜 →
𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 | 𝜗𝑚 𝑩 𝑖, 𝑚 𝑪 𝑏, 𝑚, 𝑜 =

𝑜 𝑦 . ҧ𝑖𝑐. 𝑜 𝑧 | 𝜗𝑚 𝑖 𝑥 . 𝑪(𝑥, 𝑖, 𝑚) ҧ𝑜𝑏. 𝑩 𝑚, 𝑜 + 𝑖 𝑦 . (𝑪 𝑦, 𝑚, 𝑜 ~𝑪 𝑏, 𝑚, 𝑜 ) →
ҧ𝑖𝑐. 𝑜 𝑧 | 𝜗𝑚 𝑖 𝑥 . 𝑪(𝑥, 𝑖, 𝑜) 𝑩 𝑚, 𝑜 )
```

### Strana 37

```text
π – kalkul, příklad, neomezený buffer
                                              𝑩 i, 𝑜 = 𝑖 𝑥 . 𝑪(𝑥, 𝑖, 𝑜)
                                              𝑪 𝑥, 𝑖, 𝑜 = ҧ𝑜𝑥. 𝐵 𝑖, 𝑜 + 𝑖 𝑦 . (𝑪 𝑦, 𝑖, 𝑜 ~𝑪 𝑥, 𝑖, 𝑜 )
                                              𝑪 y, i, o ~𝑪(x, i, o) = 𝜗𝑚 (𝑪 𝑦, 𝑖, 𝑚 |𝑪 𝑥, 𝑚, 𝑜 )




ҧ𝑖𝑐. 𝑜 𝑧 | 𝜗𝑚 𝑖 𝑥 . 𝑪(𝑥, 𝑖, 𝑜) 𝑩 𝑚, 𝑜 ) →
𝑜 𝑧 𝜗𝑚 𝑪 𝑐, 𝑖, 𝑜 𝑩 𝑚, 𝑜 =

𝑜 𝑧   𝜗𝑚 ҧ𝑜𝑐. 𝑩 𝑖, 𝑜 + 𝑖 𝑦 . (𝑪 𝑦, 𝑖, 𝑜 ~𝑪 𝑐, 𝑖, 𝑜 ) 𝑩 𝑚, 𝑜    → 𝑶| 𝜗𝑚 (𝑩(𝑖, 𝑜)|𝑩 𝑚, 𝑜 )
```
