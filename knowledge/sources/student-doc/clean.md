 **PRL**  
Príprava na semestrálnu skúšku 2022/2023  
*\[*     **fuck** *\] – Parkovanie pre kurzory*

*Dopĺňajte zadania a riešenia, prosím.*	  
*Prosím, pridávajte aj doplňujúce odkazy na prednášky (číslo prednášky a strana) alebo zdroje z internetu.ak*   
***Pokud je zadání nedostatečné, zkuste doplnit nějaký obdobný příklad \- pokud máte, na kterém je možné demonstrovat postup řešení prosím :)*** 

Prosím, ak niekto vie napísať nejaké zhrnutie, v ktorých prednáškach sa na čo zamerať, budeme veľmi vďační.

**Prosím ľudí, ktorí neplánujú nič upravovať, aby sa prepli do režimu ZOBRAZENIE\! Google dokument má obmedzený počet editorov. Dovoľte aj ostatným vypĺňať dokument. ĎAKUJEM**

\---------------------------------------------------------------------------------------------------------------------------------------------  
**Dôležité informácie o semestrálnej skúške povedané na prednáške:**

Riadny termín:  
**15.05.2023 12:00-13:50 \- učebňa D105**

1\. opravný termín:  
**29.05.2023 13:00-14:50 \- učebňa D105**

2\. opravný termín:  
**05.06.2023 16:00-17:50 \- učebňa D105**

\---------------------------------------------------------------------------------------------------------------------------------------------  
Materiály:  
[https://mega.nz/file/qooiUIAS\#vKYHmPturiT51YMfU3ElB1XbRi87xQl6bJ4snFhW4lA](https://mega.nz/file/qooiUIAS#vKYHmPturiT51YMfU3ElB1XbRi87xQl6bJ4snFhW4lA) \- študentské poznámky

[https://uloz.to/file/aV4YioMFCCMi/prl-zip](https://uloz.to/file/aV4YioMFCCMi/prl-zip) \- skúšky 2018/2019 a staršie

[https://docs.google.com/document/d/18PI10fxMBaaUFgexU52Kk\_WHQrSrq5VgpGcA9IKfcvY/edit\#heading=h.n9jxqj3bxsdm](https://docs.google.com/document/d/18PI10fxMBaaUFgexU52Kk_WHQrSrq5VgpGcA9IKfcvY/edit#heading=h.n9jxqj3bxsdm) \- vypracovane 2018/19 az 2016/17 \+ teoria  
\---------------------------------------------------------------------------------------------------------------------------------------------

 **Semestrálna skúška 2024/2025 \- Predtermin**  
**Př. 1**  
Tipsport crcw \- NOT, OR, či array obsahuje čísla väčšie než 0\.  
Pri OR sa pýtal na cenu, pri NOT a čísla\>0 na časovú zložitosť.  
**Př. 2**  
Ako sa uplatní zreťazenie v aritmetických operáciách, nakresliť príklad.  
**Př. 3**  
Čo je koruna, príklad komunikácie kde koruna je a kde nie  
**Př. 4**  
Parallel splitting, ukázať na príklade  
**Př. 5**  
Euler tour \- adjacency list, tabuľka, nakresliť graf, vypísať etour  
**Př. 6**  
Sequential enumeration sort, 6 krok  
**Př. 7**  
OCCAM, byte channels \- data, ctrl, out\[5\].  
Data odoslať na out kanál špecifikovaný dátom z ctrl kanálu.  
**Př. 8**  
MPI, normalizácia čísel do intervalu \<0, 1\>

#  **Semestrálna skúška 2023/2024 \- Predtermin**

**Př. 1**  
Tipsport crcw \- XOR, NAND, AND

**Př. 2**  
PRAM model \- opisat ho, nakreslit obrazok

**Př. 3**  
Kauzalni broadcast \+ relace kauzality

**Př. 4**  
Euler pro počet následovníků \+ popis

**Př. 5**  
CLA

**Př. 6**  
Meakawův algoritmus \- opisat kvorum a na obrazku znazornit zalomenu verziu kvor pre 12 procesov. takto ukazte zistenie kvor pre 2 procesy

**Př. 7**  
OCCAM \- implementujte proceduru IDK, ktora na vstupe dostava channely pre input, clk, a outputy OUT\_LEFT a OUT\_RIGHT. Ked dostane na inpute cislo, da ho do vnutornej nekonecnej queue. Ked dostane na clk lubovolnu vec, tak outputne na OUTL alebo OUTR prvy prvok queue. ukazatel na prvy prvok sa potom posunie, treba to robit rucne. tento clk vzdy outputuje striedavo (ako v PMS uplne prvy proces)

**Př. 8**  
MPI \- mate k dispozicii reduce, broadcast, rank procesu, a pocet vsetkych prvkov. kazdy proces ma premennu value, v ktorej ma nejaku hodnotu. napiste kod, v ktorom si kazdy proces vypocita value \- (priemer vsetkych hodnot), a vysledok da na output vo formate `rank: vysledok`

#  **Semestrálna skúška 2023/2024 \- RADNY skupina B**

**Př. 1**  
PRAM "tipovacka" (6b)  
a) časova složitost: XOR pro EREW, CREW, common CRCW  
b) časova složitost: počet sudych čísel pro EREW, CREW, common CRCW  
c) cena: NAND  pro EREW, CREW, common CRCW

**Př. 2**  
Popište architekturu procesů s velkým kódovým slovem (VLIW). Popište možné konflikty a způsob jejich předcházení, resp. řeešní. Ilustrujte patřičnými obárázky. (Vlevo okynko nadepsane "princip, konflikty", vpravo nadepsane  "obrazky") (9b)

**Př. 3**  
Pro problém čtenáři písaři uveďte kódy, kterými lze řešit pomocí obecného semaforu tak, aby nedocházelo ke konfliktům ani úváznutí. Řešením má být varianta, kdy čtenáři mají přednost. Neřešte případné hladovění písařů. Z algoritmu by měl být zřejmý princip vzájemného vyloučení při vstupu do kritické sekce. (9b)

**Př. 4**  
Demonstrujte operace nad stromem s použitím funkce sumy sufixů SuffixsS(hrany, ohodnocení). Pokud máte výsledek Eulerova průchodu stromem ve struktuře Etour, pokud jste schopni provést podmíněný příkaz "if e je dopredna then" podle toho, zdali je hrana je či není dopředná, jak lze spočíst pořadí vrcholů (pro zobrazení preor(v)-\>N) při průchodu pre-order? Uveďte algoritmus, krátký slovní popis pincipu a časovou složitost celého výpočtu. (Zvlast misto na alg, zvlast misto na popis, zvlast mistecko pro casovou slozitost. (9b)

**Př. 5**  
Randezvouz smth smth novy priklad \- viz obrazek. (10b)  
[obrazek: image1]  
[obrazek: image2]  
\-1  
[obrazek: image3]  
\+1  
**Př. 6**  
Vyplnit vysledek po 6 krocich enumeration sortu zapojeny v řadě (viz dalsi obrazek). (9b)

**Př. 7**  
PI kalkul cca: (new v) (a(v).a(v).0 | b'z. ... .0 \+ b(x). ... .0  )| b(x). ... .0 | b'f.c'a.0) Najit alespon 4 ruzne redukce aby uz neslo dale redukovat. (9b)

**Př. 8**  
MPI: vypsat soucet prvku vetsich nez prumer, dispozici broadcast a reduce. (9b)

# 

# 

#  **Semestrálna skúška 2023/2024 \- RADNY skupina A**

**Př. 1**  
PRAM Tipsport (OR, je posloupnost monotonni?, je v poli cisel nula?)

**Př. 2**  
Popsat princip zřetězených procesorů

**Př. 3**  
Popsat monitor (včetně signal a wait) \+ nákres

**Př. 4**  
K dispozici funkce na výpočet sumy sufixu a příkaz "if e je dopredna then do..." \- popsat algoritmus pro výpočet úrovně vrcholu (pseudokód \+ slovní popis \+ časová složitost)

**Př. 5**  
Rendezvous kktina, nový příklad

**Př. 6**  
Pipeline Merge Sort \- stav po 10 krocích

**Př. 7**  
Pi kalkul

**Př. 8**  
MPI \- proces má v proměnné value svoji hodnotu, pomocí Reduce a Bcast (definice funkcí byly v zadání) implementovat následující: chceme vytisknout součet lichých hodnot \* součet sudých hodnot

#  **Semestrálna skúška 2023/2024 \- RADNY skupina B**

**Př. 1**  
PRAM "tipovacka" (6b)  
a) časova složitost: XOR pro EREW, CREW, common CRCW  
b) časova složitost: počet sudych čísel pro EREW, CREW, common CRCW  
c) cena: NAND  pro EREW, CREW, common CRCW

**Př. 2**  
Popiště architekturu procesů s velkým kódovým slovem (VLIW). Popiště možné konflikty a způsob jejich předcházení, resp. řeešní. Ilustrujte patřičnými obárázky. (Vlevo okynko nadepsane "princip, konflikty", vpravo nadepsane  "obrazky") (9b)

**Př. 3**  
Pro problém čtenáři písaři uvěďtě kódy, kterými lze řešit pomocí obecného semaforu tak, aby nedocházelo ke konfliktům ani úváznutí. Řešením má být varianta, kdy čtenáři mají přednost. Neřešte případné hladovění písařů. Z algoritmu by měl být zřejmý princip vzájemného vyloučení při vstupu do kritické sekce. (9b)

**Př. 4**  
Demonstrujte operace nad stromem s použitím funkce sumy sufixů SuffixsS(hrany, ohodnocení). Pokud máte výsledek Eulerova průchodu stromem ve struktuře Etour, pokud jste schopni provést podmíněný příkaz "if e je dopredna then" podle toho, zdali je hrana je či není dopředná, jak lze spočíst pořadí vrcholů (pro zobrazení preor(v)-\>N) při průchodu pre-order? Uveďte algoritmus, krátký slovní popis pincipu a časovou složitost celého výpočtu. (Zvlast misto na alg, zvlast misto na popis, zvlast mistecko pro casovou slozitost. (9b)

**Př. 5**  
Randezvouz smth smth novy priklad \- viz obrazek. (10b)  
[obrazek: image1]  
[obrazek: image2]

**Př. 6**  
Vyplnit vysledek po 6 krocich enumeration sortu zapojeny v řadě (viz dalsi obrazek). (9b)  
[obrazek: image4]

**Př. 7**  
PI kalkul cca: (new v) (a(v).a(v).0 | b'z. ... .0 \+ b(x). ... .0  )| b(x). ... .0 | b'f.c'a.0) Najit alespon 4 ruzne redukce aby uz neslo dale redukovat. (9b)

**Př. 8**  
MPI: vypsat soucet prvku vetsich nez prumer, dispozici broadcast a reduce. (9b)

# 

#  **Semestrálna skúška 2023/2024 \- 1\. opravny**

**Př. 1**  
6b: PRAM (EREW, CREW, COMMON CRCW): cena zoradit sekvenciu, cena XOR, casova zlozitost AND

**Př. 2**  
9b: a) FIFO broadcast send, recv algoritmus,  b) definovat relaciu kauzality

**Př. 3**  
9b: testandset riesenie kritickej sekcie \- kod plus popis

**Př. 4**  
9b: algoritmus 4 citacov princip fungovania plus nakreslit 2 obrazky, v jednom sa detekovalo ukoncenie a v druhom nie

**Př. 5**  
10b: RA synchronizácia vstupov do CS, 4 procesy, synchronny cas, plus pocitanie logickeho casu jednotlivych udalosti, sprava ma latency 3 takty, kriticka sekcia trva 1 takt, na vstupe a vystupe nastanu 2 abstraktne udalosti, priority procesov: 1 ma najvacsiu prioritu, v case 6 taktov zaziada proces 4, v case 7 taktov zaziada o CS proces 3, naznacit komunikaciu sipkami, napisat ku kazdej udalosti logicky cas (podla Lamporta), vypisat aj logicky cas kazdeho procesu po poslednej vykonanej udalosti

**Př. 6**  
9b: random mating (8 uzlov, vyberat F/M pseudonahodne tak, aby sa jumping phase skoncil do 4 iteracii, nezabudnut aj reconstruction phase)

**Př. 7**  
9b: pi kalkul (vypisat tie 3 vyrazy, na ktore to mozno redukovat)

**Př. 8**  
9b: MPI najst druhy najmensi prvok v log. case, mozno pouzit len MPI\_Bcast, MPI\_Reduce

# 

#  **Semestrálna skúška 2022/2023 \- předtermín**

**Př. 1**  
Tipování složitosti PRAM sportka

### **Řešení:**

[obrazek: image5]  
\* **hledání prvku v unikátní posloupnosti** \- cena *n* \- protože mám n procesů, každý porovná jeden prvek pole s hledaným, a ten který najde, tak ho je schopný uložit do paměti. Tím že ty prvky jsou unikátní, tak by to mělo být možné udělat i na EREW (distribuce hledaného prvku ale bude v *log n* čase), CREW v čase *const*.

\* re: počet prvků větších než x \- myslím, že čas by měl být taky *log n* i pro CRCW, protože v čase *const* jsem schopný najít index hledaného prvku, ale nemyslím, že jde sečíst kolik takových prvků je, bez ohledu na počet procesů \+1

Co si o tom myslíte? 

**Př. 2**  
Napsat kód FIFO broadcastu a popsat relaci kauzality

### **Řešení:**

[obrazek: image6]  
[obrazek: image7]

**Př. 3**  
Pi kalkul  
**Řešení:**

**Př. 4**  
Euler

### **Řešení:**

,

**Př. 5**  
Redukční počítač  
Řešení:  
[obrazek: image8]  
**Př. 6**  
Otázka zda lze synchronizovat procesy

### **Řešení:**

**Př. 7**  
Implementace aktivním čekáním test\&set a swap

### **Řešení:**

[obrazek: image9] 

**Př. 8**  
MPI max % min \== 0  
**Řešení:**

# 

# **Semestrálna skúška 2022/2023 \- riadny termín \- skupina A**

**Př. 1**  
Pram Sportka

### **Řešení:**

**Př. 2**  
Co je to propojovací sit, nevýhody a nakreslit

### **Řešení:**

**Př. 3**  
Algo pro výpočet levelu vrcholu za slozitost  
**Řešení:**

**Př. 4**  
Monitor, hlavne popsat wait() a signal() \+ obrazek

### **Řešení:**

**Př. 5**  
Pi kalkul mega nanic(s pluskem a taky privátní proměnnou)  
*ac.0 \+ za.cf.0 | z(c).c(e).P1 \+ a(x).xd.P2 | ⱴz(az.z(b).τ.0)*

### **Řešení:**

Riešenie by mohlo byť niečo takéto? (nedávam 100% za to že je to za full body)  
*[obrazek: image10]*  
1,4,5 už nejde ďalej redukovať. *τ* je pravdepodobne možné v hociktorom kroku odmazať, podľa toho čo som vypozoroval z online nástrojov.

Užitočné linky:

### [**https://github.com/bordaigorl/stargazer**](https://github.com/bordaigorl/stargazer) **\- iba pekný vizualizér procesov v pi-kalkulu**

[https://github.com/bhaaksema/rug-picalc](https://github.com/bhaaksema/rug-picalc) \- nástroj pomocou ktorého som sa snažil príklad vypočítať, zo všetkých iných skúšaných mu chýba najmenej konštrukcií (pre príklad vyššie, nie je tam možné len tak zapísať P1 alebo P2)  
[https://fse.studenttheses.ub.rug.nl/25451/1/bCS\_2021\_HaaksemaB.pdf](https://fse.studenttheses.ub.rug.nl/25451/1/bCS_2021_HaaksemaB.pdf) \- vpodstate manuál k nástroju, najdôležitejšie strany 8-9  
*search 'a{0} \< 'c{0} \> . nil \+ 'z{0} \< 'a{0} \> . 'c{0} \< 'f{0} \> . nil | 'z{0}('c) . 'c{0}('e) . 'p{0}('l) . nil \+ 'a{0}('x) . 'x{0} \< 'd{0} \> . 'p{0}('w) . nil | \['z\] 'a{0} \< 'z{0} \> . 'z{0}('b) . tau . nil \=\>+ X:Term .* \- prepísané zadanie pre použitie v nástroji spomenutom vyššie

myslim v 4\. by nemalo byt pozorovatelne z, pretoze z je obmedzene meno, podobne aj v 3\. by mali byt len 2 pozorovania?  
este neviem kam v kroku 5 zmyzlo P2?  
[obrazek: image11]

**Př. 6**  
Pipeline merge sort

### **Řešení:**

**Př. 7**  
Hirschberg-Sinclair, určení master uzlu

### **Řešení:**

**Př. 8**  
MPI zjistit, která půlka pole má větší počet záporných hodnot

### **Řešení:**

# **Semestrálna skúška 2022/2023 \- riadny termín \- skupina B**

**Př. 1**  
Pram synotip

### **Řešení:**

**Př. 2**  
Xeon Phi

### **Řešení:**

**Př. 3**  
Bounded test and set

### **Řešení:**

**Př. 4**  
Enumeration sort

### **Řešení:**

**Př. 5**  
Pi kalkul

### **Řešení:**

**Př. 6**  
Marzullov algoritmus

### **Řešení:**

**Př. 7**  
Kvorum

### **Řešení:**

**Př. 8**  
MPI spočítať pomer lichych a sudych v postupnosti

### **Řešení:**

# 

# **Semestrálna skúška 2022/2023 \- riadny termín \- skupina C**

(opravte prosím nepresné zadania :)  
**Př. 1**  
Pram Sportka

### **Řešení:**

**Př. 2**  
5 úrovní granularity paralelizmu

### **Řešení:**

**Př. 3**  
niečo s Eulerom  
**Řešení:**

**Př. 4**  
Zapísať štruktúru semaforov \+ zostrojiť Monitor za pomoci semaforov

### **Řešení:**

**Př. 5**  
Pi kalkul mega nanic(s pluskem a taky privátní proměnnou)

### **Řešení:**

**Př. 6**  
Random mating, bol obrázok a malo sa previesť niekoľko krokov algoritmu

### **Řešení:**

**Př. 7**  
Algoritmus 4 čítačov

### **Řešení:**

**Př. 8**  
MPI \- previesť čísla z intervalu 1-5 na interval 0-1, netrebalo vypisovať

# **Řešení:**  **Semestrálna skúška 2022/2023 \- 1\. opravný termín**

**Př. 1**  
Tipování složitosti

### **Řešení:**

**Př. 2**  
Napísať algoritmicky Odd-even transposition sort \+ analýza \+ cena

### **Řešení:**

**Př. 3**  
Vysvetliť princíp paralelného selectu \+ príklad  
**Řešení:**

**Př. 4**  
Vysvetliť princíp Marzullovho algoritmu \+ z obrázka, kde boli intervaly, aplikovať daný algoritmus

### **Řešení:**

**Př. 5**  
Pi kalkul \- nájsť 3 možné redukcie

### **Řešení:**

**Př. 6**  
CLA príklad, 120 \+ 99

### **Řešení:**

**Př. 7**  
4 čítači \- detekcia ukončenia  
Napísať príklad, kedy dôjde k detekcii ukončenia a príklad, kedy nedôjde k detekcii ukončenia

### **Řešení:**

[obrazek: image12]  
[obrazek: image13]

**Př. 8**  
MPI, zistiť ktorá časť sekvencie je menšia/väčšia/rovnako veľká ako priemer  
**Řešení:**

# **Semestrálna skúška 2022/2023 \- 2\. opravný termín**

## **Př. 1**

PRAM tipování

### **Řešení:**

## **Př. 2**

Odesílání a přijímání zprávy kauzálně \+ definice relace kauzality

### **Řešení:**

## **Př. 3**

PRAM architektura popsat a nakreslit

### **Řešení:**

## **Př. 4**

ADA popsat \+ konkrétní příkazy

### **Řešení:**

## **Př. 5**

Pi calcul, 3 redukce

### **Řešení:**

## **Př. 6**

Upsweep downsweep příklad

### **Řešení:**

## **Př. 7**

4 čítače (za 10b btw)

### **Řešení:**

## **Př. 8**

MPI v log čase zjistit, zda má posloupnost 3 a více různých hodnot 

### **Řešení:**

# **Semestrálna skúška 2021/2022 \- riadny termín \- skupina A**

## **Př. 1**

Pram tipovačka, nepamätám sa presne na zadanie,  
 proste sa nauč toto

### **Řešení:**

**[obrazek: image14]**

## **Př. 2**

Test and set

### **Řešení:**

- inštrukcia, ktorá niečo otestuje a výsledkom je hodnota 0/1 na nejakej adrese v pamäti  
- je to atomická inštrukcia, teda otestuje a rovno nastaví hodnotu na 1  
- riešenie pre dva procesy:  
- proces chce vstúpiť do kritickej sekcie  
1. procesy zdieľajú hodnotu lock, ktorá je na začiatku 0 (odomknuté)  
2. ak na testandset narazil prvý proces:  
- test vráti z lock 0 (je odomknutý)  
- set nastaví lock \= 1  
- vstúpi do kritickej sekcie  
3. lock je potom atomicky zamknutý a proces je v kritickej sekcii  
4. ak chce pristúpiť do kritickej sekcie ďalší proces:  
- test vráti z lock 1 (je zamknutý)  
- set nastaví lock \= 1  
- čaká v smyčke while na uvolnenie zámku  
5. ak prvý proces opustí kritickú sekciu, nastaví lock \= 0 (odomkne zámok)  
6. druhý proces môže vstúpiť do kritickej sekcie

## **Př. 3**

etour a suffixsum \- určení úrovně uzlu ve stromu

### **Řešení:**

[obrazek: image15]

## **Př. 4 а**

Pipeline merge sort (neviem ci priklad ci teoria tak tu hodim teoriu \+ nejaky priklad

### **Řešení:**

* linearne pole procesorov p(n) \= log n \+ 1  
* cisla nie su ulozene v procesoroch ale postupne do nich vstupuju  
* kazdy procesor spaja 2 zoradene postupnosti dlzky 2^(i-2)  
  [obrazek: image16]

**Analyza:**

* procesor Pi zacne ked ma na jednom vstupe postupnost dlzky 2^(i-2) a na druhom 1, teda zacne 2^(i-2)+1 cyklov po procesore Pi-1  
* n \+ 2^r \+ r \-1 \= 2n \+ log n \-1 cyklov \= t(n) \= O(n)  
* c(n) \= O(n)\*O(log n \+1) \= O(n\*log n)  \-\> je optimalny

**Priklad:**  
**[obrazek: image17]** 

## **Př. 5** 

Zretazene processory MISD

### **Řešení:**

* lineárne prepojené procesory  
* riešenie úloh s prúdovým charakterom  
* data prechádzajú postupne jednotlivými procesormi  
* [obrazek: image18] 

## **Př. 6**

Asynchronna komunikacia na synchronnu ci je mozne

### **Řešení:**

Skupina C pr. 5

## **Př. 7**

OCCAM priklad ale netusim aky, bol som C \- Neco s polem jako “buffer” (jak se v OCCAM kurva delaji pole?) kam ti chodi prvky z jednoho channelu a v ten moment co ti ten buffer zacina pretykat nebo kdyz ti prijde 0 tak mas vzit prvek ktery je v tom poli nejdyl a ten poslat na “high” output channel pokud je to cislo vetsi nez nejaky threshhold nebo na “low” output channel kdyz mensi nebo rovno (takze jsi dostal 3 channely a jedno cislo \- ten threshhold \- na vstup te procedury ci jak se to vola) 

### **Řešení:x**

## **Př. 8** 

MPI priklad ale netusim aky, bol som C \- Neco EZ kde stacilo jen zavolat 2x reduce \- tusim ze kazdy procesor u z mel nejakou svoji hodnotu (stejne tak rank i size jsi mel v nejakych promennych uz predem) a mel jsi vypsat jestli je suma tech hodnot delitelna maximem (nebo minimem?) tech hodnot? (reduce i broadcast meli zjednodusene argumenty v zadani jeste k tomu)

### **Řešení:**

int max,sum;  
MPI\_REDUCE(val,max,MPI\_INT,MPI\_MAX,0); //root proces dostane max pres reduce  
MPI\_REDUCE(val,sum,MPI\_INT,MPI\_SUM,0); //root proces dostane sum pres reduce

if (rank \== 0) {  
    if (sum % max \== 0\) std::cout \<\< "Je delitelno bez zbytku" \<\< std::endl;  
    else std::cout \<\< "Neni lol" \<\< std::endl;  
}

# 

# **Semestrálna skúška 2021/2022 \- riadny termín \- skupina B**

## **Př. 1** 

PRAM tipsport

### **Řešení:**

pozri skupinu A Pr.1

## **Př. 2**

Vektorové procesory SIMD \+ obrázek 

### **Řešení:**

* jediný program counter (PC)  
* dokážu zrýchliť niektoré výpočty za cenu pomerne málo procesorov  
* **Výhody:**  
  * jednoduchší než MIMD  
  * menšie nároky na pamäť  
  * jeden inšt. tok a synchronizácia zjednodušuje programy  
  * odpadá réžia so zložitou synchron. medzi procesmi, ktorá je u MIMD  
  * rýchlejšia komunikácia medzi procesormi než u MIMD


* **Nevýhody:**  
  * Nie všetky problémy sú dátovo paralelizovateľné  
  * pokles výkonnosti u programov s veľa podmienenými skokmi  
  * nie sú vhodné pri malom počte procesorov  
  * vyžadujú nie úplne bežné procesory

 **[obrazek: image19][obrazek: image20]**  
**UMA (uniform memory access)			NUMA (non uniform mem. acc.)**

## **Př. 3**

Paralelní select K-teho prvku z posloupnosti S. Princip \+ demonstrace (neviem kde najst demo)

### **Řešení:**

* hlada k-ty najmensi prvok v postupnosti S  
* EREW PRAM s N procesormi  
* pouziva zdielane pole M o N prvkoch  
* časová zložitosť je optimálna, teda koľkokrát zvýšime počet procesorov, toľkokrát sa algoritmus zrýchli  
* t(n) \= O(n/N) pre n\>4, N \< n / log n  
* p(n) \= N  
* c(n) \= O(n)  \-\> je optimalnyS

## **Př. 4** 

Peterson algoritmus \+ pseudokód

### **Řešení:**

- rieši mutual exclusion  
- každý proces sa dostane na rad do kritickej sekcie  
- ak proces chce vstupiť do krit. sekcie, nastaví svoj flag a musí počkať kým príde na rad  
- P1 navštívi kritickú sekciu aspoň po jednej návšteve P0 (už keď je P0 chytený vo while cykle), nemôže sa teda stať že P1 bude stále predbiehať P0 alebo naopak, zabráni sa tým hladoveniu

**Pseudokód:**

1. zapichne svoju vlajočku a dá prednosť druhému  
2. pokiaľ má oponent zapichnutú vlajku a turn je jeho, tak sa čaká  
3. ak bojojú o kritickú sekciu:  
   1. obaja majú zapichnutú vlajku  
   2. obaja si dajú navzájom prednosť  
   3. ale turn má len jeden z nich (buď i alebo j)  
4. ten, ktorý má turn vstúpi do krit. sekcie  
5. po skončení si vezme vlajku  
6. ten čo čakal už nepozerá na turn, do krit. sekcie sa dostane pretože oponent si zobral vlajku

shared var flag: array \[0..1\] of boolean; 	//flagy žádosti o vstup do kritické sekce  
 turn: 0..1; 					// označení aktuálního kola  
   
 repeat  
   flag\[i\] := true;                      		// Proces žádá o krit. sekci  
   turn := j;                           		// Proces nastaví kolo na druhý proces  
   while (flag\[j\] and turn=j) do skip;      // Čeká kym je kolo druhého procesu a žádá o krit. sekci  
   **\<critical section\>**  
   flag\[i\] := false;                     	// Po dokončení krit. sekce proces stáhne žádost o krit sekci  
   \<remainder section\>  
 until false;

## **Př. 5** 

Synchronizácia (novinka tento rok)

### **Řešení:**

## **Př. 6**

Enumeration sort napísať X,Y,C,Z po skončení algo aka bol priklad aky neviem ale tu je nejaký na ukážku

### **Řešení:**

* lineárne pole n procesorov  
* majú spoločnú zbernicu, ktorá je schopná preniesť v každom kroku 1 hodnotu  
* cena nie je optimálna O(n) \= n^2  
* **Priklad:**

[obrazek: image21][obrazek: image22]

## **Př. 7** 

OCCAM shit  
Jestli si matně vybavuju tak na OCCAM tam bylo něco ve smyslu, že mám proceduru co má na vstupu array 10 channelů a vstupy adr a in, všechno BYTE. Když na vstup adr příjde něco, tak inkrementuju channel modulo 10\. Když přijde na in něco tak to pošlu na aktuálně nastavený channel. 

z toho co je napisane a kodu by som povedal ze je to to iste co 2021/22 1\. opravny skup B pr 7 

### **Řešení:**

PROC name(\[10\] CHAN OF BYTE channels, CHAN OF BYTE adr,in)  
   outAdr := 0  
   WHILE TRUE  
     ALT  
        adr ? x  
           	outAdr := outAdr \+ 1  
            IF  
                outAdr \> 9  
                    outAdr := 0  
        	    TRUE  
                    SKIP   
        in ? y  
           	channels\[outAdr\] \! y

## **Př. 8** 

MPI: Pokud max % min \== 0, pak vypiš “Ano”, jinak vypiš “Ne”.  
	

### **Řešení:**

Volani Reduce je mozna spatne, v te otazce byla hlavicka definovana, tak se to akorat trochu upravi  
int rank,val; //bylo zadano, ze kazdy procesor ma svuj rank a hodnotu  
⁹  
int max,min;  
MPI\_REDUCE(val,max,MPI\_INT,MPI\_MAX,0); //root proces dostane max pres reduce  
MPI\_REDUCE(val,min,MPI\_INT,MPI\_MIN,0); //root proces dosatne min pres reduce

if (rank \== 0) {  
    if (max % min \== 0\) std::cout \<\< "Min a max jsou delitelne bezezbytku" \<\< std::endl;  
    else std::cout \<\< "Min a max nejsou delitelne bezezbytku" \<\< std::endl;  
}

# 

# **Semestrálna skúška 2021/2022 \- riadny termín \- skupina C**

## **Př. 1** 

PRAM tipsport extraliga

### **Řešení:**

skupina A Pr. 1

## **Př. 2**

XEON popisat \+ obrazok (nie, nerobim si srandu, vazne to tam dal \-\_-) WTF \+54

### **Řešení:**

* kombinácia SIMD \+ MIMD

[obrazek: image23]

## **Př. 3**

Mám etour a suffixsum, zistiť koľko je nasledujúcich vrcholov v strome \+ popísať princíp \+ určiť časovú náročnosť 

### **Řešení:[obrazek: image24]**  

analýza 

1. spočítanie Etour O(c)  
2. inicializácia wieght O(c)  
3. výpočet suffixSums O(log n)  
4. korekcia výsledku O(c)li

t(n)=O(log n)  
c(n)=závisi od implementácie suffixSums

## **Př. 4** 

Monitor popísať (aj wait a signal) \+ obrázok

### **Řešení:**

* je to high-level jazyková konštrukcia, ktorá poskytuje rovnakú funkcionalitu ako semafory, ale je jednoduchší na použitie  
* môže byť implementovaný pomocou semaforov  
* **je to softvérový modul ktorý obsahuje:**  
  * jednu alebo viac procedúr  
  * inicializačnú sekvenciu  
  * lokálne premenné  
* **charakteristiky:**   
  * lokálne premenné sú prístupné len procedúram monitoru  
  * proces vstúpi do monitoru tým že zavolá jednu z jeho procedúr  
  * len 1 proces môže byť v monitore v jednom čase  
  * pre každú podmienkovú premennú obsahuje vnútornú frontu  
  * naviac má jednu urgentnú frontu  
* monitor nám zaručuje vzájomné vylúčenie (mutual exclusion) a nepotrebujeme ho pritom naprogramovať ručne, čiže naše zdieľané dáta sú chránené ak ich umiestnime do monitoru  
* **Condition variablesm**  
  * sú prístupné len  z monitoru  
  * môže sa k ním pristúpiť len z týchto 2 funkcí:  
    * **wait(a)** \- blokuje vykonanie volajúceho procesu na podmienke a  
      	\- proces môže pokračovať len ak iný proces zavolá signal(a)  
    * **signal(a) \-** vzbudí pokračovanie vykonávania nejakého procesu, ktorý čaká na podmienku a

[obrazek: image25]  
[obrazek: image26]

## **Př. 5**

asynchronní signály a určit zda jdou předkládat tak aby šly volat synchrone  
vypadlo to nějak takto cca  
[obrazek: image27]

### **Řešení:**

Musíme zjistit, zda v asynchronním systému existuje koruna. Pokud koruna neexistuje, je systém proveditelný synchronně. Pro každý proces si vypíšeme všechny události, které jsou v relaci kauzality: \-e\>. A pak se v nich snažíme najít cyklus aka korunu.

1\.      Proces \= (1,4)

2\.      Proces \= (2,3)

3\.      Proces \= (3,5)

[obrazek: image28]4\.      Proces \= (4,1)

5\.      Proces \= (5,6)

6\.      Proces \= (2,6)

 

Koruna v tam je velikosti 2: (1,4) \-\> (4,1) \=\> systém nelze provést synchronně.

## **Př. 6** 

Príklad na prescan, zoradiť 16 čísel (ukážkový príklad z minulého roku na pochopenie princípu)

### **Řešení:**

**prvky : 5, 1, 6, 10, 3, 8, 2, 4**   
**[obrazek: image29]**  
**pozn.: bylo to potřeba zapsat jako pole tj vědět které číslo v tom poli se má přepsat**

## **Př. 7**

OCCAM mám ebo in, keď mi do adr príde 1-10 tak nastavím aktívny index na to číslo ináč 0, keď do in niečo príde tak to vložím na aktívny channel   

### **Řešení:**

## **Př. 8** 

MPI počet prvkov rovnakých ako max a rovnakých ako min v log čase

### **Řešení:**

**[obrazek: image30]**

# 

# 

#  **Semestrálna skúška 2021/2022 \- 1\. opravný \- skupina A**

## **Př. 1** 

 popísať Algo na CRCW pre AND a uviesť príklad

### **Řešení:**

Tým, že každý z procesorov má pridelenú hodnotu a jedná sa o operáciu AND, stačí aby každý procesor skontroloval, či je jeho hodnota 0 a ak áno, poslal správu hlavnému procesoru (resp. zapísal hodnotu 0 do jeho pamäte). Výsledkom je potom hodnota hlavného procesoru.  
[obrazek: image31]  
niečo také asi, všetky procesory sa naraz pozrú na svoju hodnotu, proc P3 má hodnotu 0 teda pošle správu hlavnému procesoru P1 a teda celý AND je FALSE

## **Př. 2** 

kde by sme využili MIMD, popísať \+ obrázok

### **Řešení:**

Xeon phi I guess ako kombinácia SIMD a MIMD  
[obrazek: image23]

MIMD: Multiple Instruction Multiple Data

- zreťazené MIMD  
- ostatné MIMD \- so spoločnou zbernicou, s prepojovacou sieťou, so pevnou sieťou  
- multiprocesory \- tesné viazanie typicky cez zdieľanú pamäť  
- multicomputery \- voľnejšie viazanie typicky cez predávanie správ

## **Př. 3** 

suffixsum pre euler path výpočet úrovne vrcholu

### **Řešení:**

- úroveň vrcholu je najkratšia vzdialenosť medzi koreňom a vrcholom  
- daná rozdielom počtu spätných a dopredných hrán na zvyšku Eulerovej cesty od vrcholu  
  algo:  
1. inicializácia poľa váh: dopredná \= \-1, spätná \= \+1  
2. suffix sum na poľom váh  
3. korekcia: cez  všetky dopredné hrany sa spočíta úroveň vrcholu v

		váha hrany \+1   
level(v) \= weight(e) \+ 1, e \= (u,v)  
[obrazek: image32]

## **Př. 4** 

ako budú vyzerať procesory v 12\. Kroku pri pipeline sort

### **Řešení:**

nepamätám si zadanie ale bolo tam tuším, že 8 čísel a 4 procesory   
pozri si nejaký príklad nech vieš ako sa to robí napr. riadny termín 2021/22, skupina A pr. 4

## **Př. 5** 

async \-\> sync či sa dá, ak ano tak ako, kde to vidime atď. ak nie preco a popisat relaciu kauzality  
[obrazek: image33]

### **Řešení:**

nie je to možné, vzniká tam koruna o veľkosti 4 medzi prvými 4\. procesmi  
proces 1 : (S1, R4)  
proces 2: (S2, R3)  
proces 3: (S3, R1)  
proces 4: (S4, R2)  
koruna: (S1, R4) \-\> (S4, R2) \-\> (S2, R3) \-\> (S3, R1)

relácia kauzality \-\>

- hovoríme, že a kauzálne predchádza b keď jeden proces vykonal tieto udalosti v tomto poradí a \-\> b   
- broadcast vysielanie a doručenie je v relácii kauzality: send(msg) \-\> deliver(msg)  
- relácia je tranzitívna 

## **Př. 6** 

FIFO algoritmy

### **Řešení:**

niesom si úplne istý ale asi chcel tieto dva ?

* Lampartov alg.  
  * procesy se snaží shodnout na tom, ktorý z nich získa kritickú sekciu  
  * založené na FIFO doručovaní správ  
  * udržuje lokálnu prioritnú frontu správ, v ktorej priority sú úplne usporiadané podľa predávaných časových razítok    
* Ricart \- Agrawala alg.  
  * vylepšenie Lampartova alg., vyžaduje len 2(n-1) správ (Lampart 3(n-1) )  
  * zlučuje správy, odpovede a uvoľnenia dohromady  
  * synchronizačné oneskorenie je opäť len 1 zaslaná správa  
    

## **Př. 7**

OCCAM chanelly ls,gt,in potom BYTE th ako vstup, vytvorit pole o veľkosti SIZE malo byť že \[0..SIZE-1\] po in prijať x ak má buffer (pole) miesto a x \!= 0 tak to uloží do poľa ak miesto nieje alebo x \== 0 AND x \<= th potom ls \! x a ak x \== 0 AND x \> th potom gt \! x

### **Řešení:**

## **Př. 8**

MPI nájsť či suma prvkov v 1\. Polovici je Broadcastmenšia ako suma prvkov v 2\. Vypísať áno alebo nie

### **Řešení:**

[obrazek: image34]  
Alebo   
[obrazek: image35]

# **Semestrálna skúška 2021/2022 \- 1\. opravný \- skupina B**

## **Př. 1** 

Udělat AND pro common CRCW. Popsat princip \+ příklad

### **Řešení:**

2021/22 1.opr skupina A pr. 1

## **Př. 2** 

Xeon Phi Popsat \+ obrázek (dostal jsem 8b za ten architekturní se skalar, vect jednotkou, cache,... takže chtěl asi ten)

### **Řešení:**

kombinácia SIMD a MIMD  
32 512-bitových vektorových registrov  
[obrazek: image23]

## **Př. 3** 

Odd Even merge sort \+ ještě nakreslit tu síť 4x4 s použitím CE porovnávaček

### **Řešení:**

* princíp je spájanie dvoch zoradených postupností  
* špeciálna sieť procesorov, základný stavebný kameň je procesorový element CE \= sieť 1x1  
* každý procesor má 2 výstupné a 2 vstupné kanály  
* každý procesor porovná hodnoty na svojich vstupoch a menší dá na výstup L(Low) a väčší na výstup H (High)

[obrazek: image36]  
[obrazek: image37]

## **Př. 4** 

Marzullův alg 

### **Řešení:**

* NTP (Network Time Protocol) používa Marzullov alg. na stanovenie času líšiacich sa odpovedí časových serverov  
* pre množinu intervalov, hľadáme najmenší interval s najväčším počtom prienikov  
  Alg:  
1. zoraď intervaly podľa offsetov začiatkov a koncov intervalov. Počiatočné okamžiky označ ci \=1 a koncové ci \= \-1  
2. best \= 0, count \= 0  
3. urob sumu prefixov, teda postupne pre každý offset i od najnižšej hodnoty po najväčšiu urob count \+= ci

   if count \> best then best \= count 

[obrazek: image38]	

## **Př. 5** 

async \-\> sync či sa dá, ak ano tak ako, kde to vidime atď. ak nie preco a popisat relaciu kauzality. Dá se synchronizovat? Pokud ano uvést jak. Pokud ne, uvést jak se to dá detekovat, co se tam nachází a které konkrétní zprávy tomu zabraňují  
[obrazek: image39]

### **Řešení:**

2021/22 1.opr skupina A, pr. 5

## **Př. 6** 

Enumeration Sort (predpokladam ze pole a chcel priklad nie algo)

### **Řešení:**

* lineárne pole n procesorov so spoločnou zbernicou, v jednom kroku prenesie max 1 hodnotu  
* procesory majú 4 registre:  
  * Xi \- prvok xi, dostane sa do procesoru cez zbernicu  
  * Yi \- postupne prvky x1..xn, presuvaju sa lineárnym prepojením procesorov  
  * Zi \- zoradený prvok xi (finálna utriedená postupnosť)  
  * Ci \- počet prvkov menších ako xi

neviem ake boli hodnoty, pre ukážku si pozri 2021/22 riadny skupina B pr 6 alebo som nasiel toto  
**[obrazek: image40]**

## **Př. 7**

V tom OCCAM bylo něco jako máte proceduru něco, která má jako parametry \[0..9\] kanálů CHN, a vstupy IN, ALT typu INT. Na IN přichází hodnoty a jsou posílány na právě aktivní kanál (začíná se 0). Pokud  na ALT přijde 1, zapne se alterace a po každém odeslání IN se posuň na další kanál, tj. (active \+1) % 10\. Pokud přijde na ALT 0, tak vypni alteraci a vše se odesílá na aktuální kanál.

Procedúra s tromi parametrami \- pole kanálov OUT\[10\] a kanály IN a ALT. Na IN a ALT sú prijímané hodnoty 0/1. Hodnota prijatá na ALT zapína/vypína alternovanie medzi OUT kanálmi. Hodnota na IN je poslaná na aktuálny kanál OUT a podľa toho či je zapnutá alternacia je inkrementovany index kanálu OUT (modulo počet kanálov).

### **Řešení:**

[obrazek: image41]

## **Př. 8**

MPI, každej procesor měl prvek a zjistit jestli sudý procesory mají sudy prvky a lichý mají lichý prvky

### **Řešení:**

Dá sa aj s MPI\_AND namiesto MPI\_SUM  
[obrazek: image42]

# **Semestrálna skúška 2021/2022 \- 2\. opravný**

## **Př. 1**

PRAM tipovačka

### **Řešení:**

## **Př. 2**

Popísať Dataflow architektúru \+ obrázok

### **Řešení:**

## **Př. 3**

Semafor \- popísať P a V operácie

### **Řešení:**

## **Př. 4**

FIFO broadcast \- ako prebieha prijímanie a odosielanie a algoritmy

### **Řešení:**

[obrazek: image43]

## **Př. 5**

Príklad na async \-\> sync

### **Řešení:**

## **Př. 6**

Príklad na random mating, skončiť prvú fázu do 4 krokov

### **Řešení:**

## **Př. 7**

LINDA \- vyhľadávanie v lineárnom zozname

### **Řešení:**

ze slajdu: (Name, Unique\_identifier, Next, Val)

TID id, next;  
int to\_find;

rd("list", "head", ?id)  
while(id \!= NULL){  
 rd("list", id, ?next, ?val);  
 if to\_find \== val  
  return True  
 id \= next  
}

## **Př. 8**

MPI nájsť druhé maximum (pozor, hodnoty môžu byť aj záporné)

### **Řešení:**

 

# **Semestrálna skúška 2020/2021 \- riadny termín**

## **Př. 1** 

cena XOR

- casova zlozitost OR  
- cena suctu? maxima a minima

### **Řešení:**

\[podle toho jak to bylo v minulych letech, **overte mi prosim**\]

* cas XOR  
  * EREW                  log n   
  * CREW                  log n  
  * Common CRCW  log n  
* cena sum  
  * EREW		     n\*log n  
  * CREW                  n\*log n  
  * Common CRCW  n\*log n  
* cena max/min  
  * EREW		     n\*log n  
  * CREW                  n\*log n  
  * Common CRCW  n\*log n

\+2

## **Př. 2**

Operace testAndSet  
\[asi jde o semafor?\]  
\[Nope. Semafory jsou uz reseni vzajemneho vylouceni **bez aktivniho cekani**. Tady jde o zpusob, kdy ve while proces, ktery ceka na kritickou sekci, testuje testAndSet(\&lock) porad dokola, viz prezentace Vzajemne vylouceni\]

### **Řešení:**

- inštrukcia, ktorá niečo otestuje a výsledkom je hodnota 0/1 na nejakej adrese v pamäti  
- je to atomická inštrukcia, teda otestuje a rovno nastaví hodnotu na 1  
- riešenie pre dva procesy:  
- proces chce vstúpiť do kritickej sekcie  
7. procesy zdieľajú hodnotu lock, ktorá je na začiatku 0 (odomknuté)  
8. ak na testandset narazil prvý proces:  
- test vráti z lock 0 (je odomknutý)  
- set nastaví lock \= 1  
- vstúpi do kritickej sekcie  
9. lock je potom atomicky zamknutý a proces je v kritickej sekcii  
10. ak chce pristúpiť do kritickej sekcie ďalší proces:  
- test vráti z lock 1 (je zamknutý)  
- set nastaví lock \= 1  
- čaká v smyčke while na uvolnenie zámku  
11. ak prvý proces opustí kritickú sekciu, nastaví lock \= 0 (odomkne zámok)  
12. druhý proces môže vstúpiť do kritickej sekcie

## **Př. 3** 

kauzalita

### **Řešení:**

**[obrazek: image44]**

## **Př. 4**

Euler tah \-suffix?

### **Řešení:**

## **Př. 5**

R-A

### **Řešení:**

Algoritmus Ricart-Agrawala  
– Jedná se o optimalizaci Lamportova algoritmu

## **Př. 6**

Euler strom/graf?

### **Řešení:**

## **Př. 7**

Carry look ahead add \- spocitat 39 a 110  
r

### **Řešení:**

1. Prevest do bin  
   1. 39:   00100111  
   2. 110: 01101110  
2. Spočítať pole di pomoci a. b. kde di \\in {**p**ropagate, **g**enerate, **s**top}  
   1. if xi \== 1 and yi \== 1 \-\> di \= g // nevadi co prislo zhora, vzdu bude carry  
   2. if xi \== 0 and yi \== 0 \-\> di \= s // nevadi co prislo zhora, nikdy nebude carry  
   3. else di \= p // carry zavisi na tom, co prijde zhora

   Pro nas priklad

x : 0 0 1 0 0 1 1 1 	  
	y : 0 1 1 0 1 1 1 0  
	d : s p g s p g g p // initialni vector

3. Pocitam co bude v dalsim kroku, aktulani di \<tecka v kolecku\> di-1  (pro prvni hodntu di-1 \= s \- neutralni prvek)  
   osa X: to bylo pred tim (di-1)  
   osa Y: co je v init vectoru (di)  
   [obrazek: image45]

x : 0 0 1 0 0 1 1 1 	  
	y : 0 1 1 0 1 1 1 0  
	d : s p g s p g g p  
d’: s g g s g g g s  s

4. Pocitame carry bit \- pokud je s/p \-\> nasledujici carry bit ja 0, jinak 1

x : 0 0 1 0 0 1 1 1 	  
	y : 0 1 1 0 1 1 1 0  
	d : s p g s p g g p  
d’: s g g s g g g s  s  
c : 1 1 0 1 1 1 0 0

5. Delam summu xi \+ yi \+ ci

x : 0 0 1 0 0 1 1 1 	  
	y : 0 1 1 0 1 1 1 0  
	d : s p g s p g g p  
d’: s g g s g g g s  s  
c : 1 1 0 1 1 1 0 0  
z : 1 0 0 1 0 1 0 1  \== 149

Overte me prosim vas  
\+2

## **Př. 8**

naprogramovat s log zlozitostou sucet hodnot vacsich nez priemer

### **Řešení:**

   MPI\_Init(&argc, &argv); 

   int rank,size,sum;

   MPI\_Comm\_rank(MPI\_COMM\_WORLD, &rank);  
   MPI\_Comm\_size(MPI\_COMM\_WORLD, &size);  
   int buf\=(rank\*1234)%33; //"random" data 

   MPI\_Reduce(&buf,&sum,1,MPI\_INT,MPI\_SUM,0,MPI\_COMM\_WORLD);

   double avg;  
   if (rank \== 0) avg \= (double)sum / (double)size;  
   MPI\_Bcast(&avg,1,MPI\_DOUBLE,0,MPI\_COMM\_WORLD);

   buf \= (buf \> avg) ? buf : 0;  
    
   int sum;//jiz definovany vyse  
   MPI\_Reduce(&buf,&sum,1,MPI\_INT,MPI\_SUM,0,MPI\_COMM\_WORLD);  
   if (rank \== 0) std::cout \<\< sum \<\< std::endl;

   MPI\_Finalize();

# **Semestrálna skúška 2020/2021 \- 1\. opravný termín**

## **Př. 1**

PRAM složitosti,

### **Řešení:**

## **Př. 2**

PRAM architektura (popis+obrazek) ,

### **Řešení:**

## **Př. 3**

Pi kalkul (redukce+pozorování), 

### **Řešení:**

## **Př. 4**

Random mating(příklad), 

### **Řešení:**

## **Př. 5**

Suzuki (princip+obrazek 4 uzly), 

### **Řešení:**

## **Př. 6**

Monitor(popsat wait/signal, obrázek),

### **Řešení:**

* je to high-level jazyková konštrukcia, ktorá poskytuje rovnakú funkcionalitu ako semafory, ale je jednoduchší na použitie  
* môže byť implementovaný pomocou semaforov  
* **je to softvérový modul ktorý obsahuje:**  
  * jednu alebo viac procedúr  
  * inicializačnú sekvenciu  
  * lokálne premenné  
* **charakteristiky:**   
  * lokálne premenné sú prístupné len procedúram monitoru  
  * proces vstúpi do monitoru tým že zavolá jednu z jeho procedúr  
  * len 1 proces môže byť v monitore v jednom čase  
  * pre každú podmienkovú premennú obsahuje vnútornú frontu  
  * naviac má jednu urgentnú frontu  
* monitor nám zaručuje vzájomné vylúčenie (mutual exclusion) a nepotrebujeme ho pritom naprogramovať ručne, čiže naše zdieľané dáta sú chránené ak ich umiestnime do monitoru  
* **Condition variables**  
  * sú prístupné len  z monitoru  
  * môže sa k ním pristúpiť len z týchto 2 funkcí:  
    * **wait(a)** \- blokuje vykonanie volajúceho procesu na podmienke a  
      	\- proces môže pokračovať len ak iný proces zavolá signal(a)  
    * **signal(a) \-** vzbudí pokračovanie vykonávania nejakého procesu, ktorý čaká na podmienku a

[obrazek: image25]  
[obrazek: image26]

## **Př. 7**

Linda ( reverz seznamu)

### **Řešení:**

TID id, prev, next;  
int val;

rd("list", "head", ?id);  
in("list", id, ?next, ?val);  
out("list", id, NULL, val);  
prev \= id;  
id \= next;

while(id \!= NULL) {  
 in("list", id, ?next, ?val);  
 out("list", id, prev, val);

 prev \= id;  
 id \= next;  
}  
out("list", "head", prev);

— netreba sa este zbavit original headu?  
— cize pred poslednym riadkom:  
— in(“list”, “head”, ?id);

## **Př. 8**

MPI ( součet čísel větších jak průměr)

# 

### **Řešení:**

# **Semestrálna skúška 2020/2021 \- 2\. opravný termín**

## **Př. 1**

PRAM tipovačka

### **Řešení:**

## **Př. 2**

VLIW \+ ako sa riešia konflikty

### **Řešení:**

## **Př. 3**

Monitor \- popis \+ obrázok

### **Řešení:**

* je to high-level jazyková konštrukcia, ktorá poskytuje rovnakú funkcionalitu ako semafory, ale je jednoduchší na použitie  
* môže byť implementovaný pomocou semaforov  
* **je to softvérový modul ktorý obsahuje:**  
  * jednu alebo viac procedúr  
  * inicializačnú sekvenciu  
  * lokálne premenné  
* **charakteristiky:**   
  * lokálne premenné sú prístupné len procedúram monitoru  
  * proces vstúpi do monitoru tým že zavolá jednu z jeho procedúr  
  * len 1 proces môže byť v monitore v jednom čase  
  * pre každú podmienkovú premennú obsahuje vnútornú frontu  
  * naviac má jednu urgentnú frontu  
* monitor nám zaručuje vzájomné vylúčenie (mutual exclusion) a nepotrebujeme ho pritom naprogramovať ručne, čiže naše zdieľané dáta sú chránené ak ich umiestnime do monitoru  
* **Condition variables**  
  * sú prístupné len  z monitoru  
  * môže sa k ním pristúpiť len z týchto 2 funkcí:  
    * **wait(a)** \- blokuje vykonanie volajúceho procesu na podmienke a  
      	\- proces môže pokračovať len ak iný proces zavolá signal(a)  
    * **signal(a) \-** vzbudí pokračovanie vykonávania nejakého procesu, ktorý čaká na podmienku a

[obrazek: image25]  
[obrazek: image26]

## **Př. 4**

Problém 5 filozofov \- kód so semaformi \+ popis ako to funguje (plus musel byt deadlock proof ten kód)

### **Řešení:**

Jde o úlohu, kde 5 filosofů/procesů v náhodných chvílích buď přemýšlí, žádají o vidličku nebo jedí. Pokud chce filosof jíst, musí získat 2 sdílené zdroje/vidličky, kdy jedna je od něj vlevo a druhá vpravo. Zároveň jsou vidličky ale sdílené se sousedními filosofy. Řešení, kde je ošetřena možnost uváznutí:

semaphore E;  
fork \= array\[0..4\] of semaphore;

initialize:  
E.count \= 4; //porusime cyklickou ozavislost (viz Coffmanovy podminky), nechame jist pouze 4 z 5 filosofu  
	for i=0..4 {fork\[i\] \= 1;} //jen jeden proces muze danou vidlicku v jednu chvili vlastnit  
filosof:  
	repeat  
	think;  
	P(E);  
	P(fork\[i\]); //leva vidlicka \- kdo to v tom nevidi, necht si nakresli stul s 5 procesy okolo a 5 vidlicek  
		    //nutne si indexy nakreslit proti smeru hodinovych rucicek a kazda leva vidlicka bude mit  
    //dany index procesu  
	P(fork\[i+1 mod 5\]); //prava vidlicka  
	eat;  
	V(fork\[i+1 mod 5\]);  
	V(fork\[i\]);  
	V(E);  
	forever

## **Př. 5**

Nieco s FIFO a broadcastom, nejaká random tabuľka, v živote som to nevidel

### **Řešení:**

## **Př. 6**

Random mating (pravdepodobne 1:1 recycle z 1\. opravného)

### **Řešení:**

## **Př. 7**

OCCAM \- naprogramovanie procedúry AVG, ktorá má tri kanály typu BYTE a to DATA, CHNH, CHNL. Procedúra berie čísla z kanálu DATA, počíta z nich dlhodobý priemer, a podľa toho či číslo, ktoré prišlo je väčšie alebo menšie ako priemer tak ho pošle príslušnému kanálu. (nepísal však ktorému tak som predpokladal, že CHNH je pre väčšie čísla a ten druhý je pre menšie alebo rovné (ale tá rovnosť nebola explicitne zmienená)).

### **Řešení:**

Pomocí různých jiných řešení jsem se to pokusil splácat, ale netuším jestli to je dobře, tak je na vás jestli tomu chcete věřit, možná by nad SEQ mělo být WHILE TRUE, idk:

PROC avg(CHAN OF BYTE DATA, CHNH, CHNL)  
    INT counter := 0  
    INT sum := 0  
    INT value :  
    INT avg :  
    SEQ  
        counter := counter \+ 1  
        DATA ? value

        sum := sum \+ value  
        avg := sum/counter  
        IF  
            value \<= avg  
                CHNL \! value  
            value \> avg  
                CHNH \! value

Já bych udělal paralelní sekci pro výpočet meanu a pro výstup, což by taky znamenalo, že aktuální hodnota by se nepočítala do dlouhodobého průměru při rozhodování, na který výstup se hodnota pošle. Možná to i dává větší smysl, říct, zda je hodnota větší nebo menší než dosavadní průměr a až potom upravit ten průměr.z

## **Př. 8**

MPI \- "spočítať sumu menších čísiel v postupnosti ako je jej minimum" \<-- potom sa na upozornenie opravil a povedal, že si máme zvoliť menších ako maximum alebo väčších ako minimum

### **Řešení:**

   MPI\_Init(&argc, &argv); 

   int rank,size,sum;

   MPI\_Comm\_rank(MPI\_COMM\_WORLD, &rank);  
   MPI\_Comm\_size(MPI\_COMM\_WORLD, &size);  
   int buf\=(rank\*1234)%33; //"random" data   
   int max; 

   MPI\_Reduce(&buf,&max,1,MPI\_INT,MPI\_MAX,0,MPI\_COMM\_WORLD); // root process receives max \-\> this value need to be sent to all other processes

   MPI\_Bcast(\&max, 1, MPI\_INT, 0, MPI\_COMM\_WORLD);

   int val \= buf \< max ? buf : 0 ;  
   int sum;  
   MPI\_Reduce(&val,&sum,1,MPI\_INT,MPI\_SUM,0,MPI\_COMM\_WORLD);  
   if (rank \== 0) std::cout \<\< sum \<\< std::endl;

   MPI\_Finalize();

# 

Myslím, že **MPI\_Reduce** a **MPI\_Bcast** mohou být nahrazeny **MPI\_Allreduce**.  
Ale v zadani je uvedeno (ne tady, ale v originalnim) ze muzeme pouzit jenom cMPI\_Reduce a MPI\_Bcast 

# **Semestrálna skúška 2019/2020 \- riadny termín \- skupina A**

## **Př. 1** 

PRAM tipovačka, měla tři části:

urči asymptotickou časovou složitost EREW nějakého algoritmu  
urči cenu CREW nějakého (jiného) algoritmu  
učit asymptotickou časovou složitost common CRCW nějakého (jiného) algoritmu

### **Řešení:**

**Casova zlozitost sucinu prvkov postupnosti**

- EREW PRAM			log n

**Cena OR postupnosti**

- CREW PRAM 			n\*log n

**Casova zlozitost unsorted**   
**ch**

- CRCW PRAM			n/N

## **Př. 2**

VLIW \- popsat, obrázek

### **Řešení:**

[obrazek: image46]  
	  
[obrazek: image47]

## 

## **Př. 3** 

Monitor \- popsat, hlavně signal a wait, obrázek

### **Řešení:**

[obrazek: image48]  
[obrazek: image49]  
[obrazek: image26]

## **Př. 4**

Broadcasty \- dva obrázky jako ze slajdů, měli jsme určit jestli splňují FIFO, kauzalitu, atomičnost a jednu vlastnost si vybrat, opravit a nakreslit vedle znovu

### **Řešení:**

PS co je kauzalita  
[obrazek: image50]

## **Př. 5**

OCCAM \- popsat, primitiva, obrázek

### **Řešení:**

[obrazek: image51]  
Primitiva  
[obrazek: image52]

## **Př. 6**

Stromy \- to jsem úplně nepochopil co přesně mám dělat, ale asi napsat algoritmus pro preorder, když máme funkci suffix a cesty uloženy ve struktuře Etour \+ popsat a složitost

### **Řešení:**

[obrazek: image53]

## **Př. 7**

Random mating \- použít na příkladu, aby skončil ve 4 krocích

### **Řešení:**

[obrazek: image54]Richa  
kdyztak me opravte, ale pohlavi F a M volim nahodne (spici procesor uz nemeni pohlavi). Jakmile narazim na sekvenci F-\>M, tak F procesor zmeni svou hodnotu na val\[i\] \+ val\[succ\[i\]\] a naslednika uspim, poznacim si poradi, ve kterem jsem ho uspal.   
Pokracuju, dokud prvni prvek neukazuje na posledni a potom prichazi na radu rekonstrukci faze, kdy probouzim procesory v opacnem poradi a jestli neukazuji na konec listu, tak provedu korekci val\[i\] \= val\[i\] \+ val\[succ\[i\]\]. Abychom splnili pozadovany pocet kroku, musime zvolit F a M spravne xD

## **Př. 8**

MPI \- počet prvků, jejichž hodnota byla větší než průměrná

### **Řešení:**

   MPI\_Init(&argc, &argv); 

   int rank,size,sum;  
   MPI\_Comm\_rank(MPI\_COMM\_WORLD, &rank);  
   MPI\_Comm\_size(MPI\_COMM\_WORLD, &size);  
   int buf\=(rank\*1234)%33; //"random" data 

   MPI\_Reduce(&buf,&sum,1,MPI\_INT,MPI\_SUM,0,MPI\_COMM\_WORLD);

   double avg;  
   if (rank \== 0) avg \= (double)sum / (double)size;  
   MPI\_Bcast(&avg,1,MPI\_DOUBLE,0,MPI\_COMM\_WORLD);

   bool largerThanAvg \= buf \> avg;  
   buf \= largerThanAvg ? 1 : 0;  
    
   int cnt;  
   MPI\_Reduce(&buf,&cnt,1,MPI\_INT,MPI\_SUM,0,MPI\_COMM\_WORLD);  
   if (rank \== 0) std::cout \<\< cnt \<\< std::endl;      
   MPI\_Finalize();

ANO: 0x  
NE: 0x

# **Semestrálna skúška 2019/2020 \- riadny termín \- skupina B**

## **Př. 1** 

I cena alg ktory zoradi,  
II cena ktory zisti ci je nejaky zhodny,  
III casova zlozitost algoritmu ktory spocita AND?

### **Řešení:**

## **Př. 2**

Zretazene procesory

### **Řešení:**

## **Př. 3** 

Kod producent konzument

### **Řešení:**

## **Př. 4**

euler suffix sum

### **Řešení:**

## **Př. 5**

Broadcast

### **Řešení:**

## **Př. 6**

Prescan (upsweep, downsweep)

### **Řešení:**

## **Př. 7**

Linda \- zadefinovat synchronizaciu alebo vylucenie

### **Řešení:**

## **Př. 8**

MPI (reduce, broadcast) c++ \- 16 prvkov zistit ci su aspon 2 rozne \- logaritmicka casova zložitosť

### **Řešení:**

   MPI\_Init(&argc, &argv); 

   int rank,size,max,min;  
   bool hasTwoDiffValues;

   MPI\_Comm\_rank(MPI\_COMM\_WORLD, &rank);  
   MPI\_Comm\_size(MPI\_COMM\_WORLD, &size);   
   int buf\=(rank\*1234)%33; //"random" data 

   MPI\_Reduce(&buf,&max,1,MPI\_INT,MPI\_MAX,0,MPI\_COMM\_WORLD);  
   MPI\_Reduce(&buf,&min,1,MPI\_INT,MPI\_MIN,0,MPI\_COMM\_WORLD);  
    
   if (rank \== 0) {  
       hasTwoDiffValues \= max \!= min;  
       std::cout \<\< hasTwoDiffValues \<\< std::endl;s  
   }

   MPI\_Finalize();

# **Semestrálna skúška 2019/2020 \- 1\. opravný termín**

## **Př. 1** 

PRAM ako na každom termíne

### **Řešení:**

## **Př. 2**

Xeon Phi \- architektúra

### **Řešení:**

Kombinace SIMD a MIMD  
[obrazek: image23]

## **Př. 3** 

Odd-even merge sort \- popis algoritmu, sieť 4x4

### **Řešení:**

## **Př. 4**

Marzullo algoritmus \- popis algoritmu, ukázať na príklade

### **Řešení:**

[obrazek: image55]

## **Př. 5**

CLA \- podrobný postup ako sa sčítajú 2 čísla

### **Řešení:**

## **Př. 6**

Obyčajný semafór \- príkazy, princíp

### **Řešení:**

[obrazek: image56]  
[obrazek: image57]

* Synchronizačný nástroj poskytovaný OS, ktorý nevyžaduje aktívne čakanie (busy waiting)  
* semafor S je premenná typu Int ku ktorej (okrem inicializácie) sa môže pristupovať len cez 2 atomické a vzájomne exkluzívne operácie P(S) a V(S)  
* aby sa predišlo aktívnemu čakaniu \- ak musí proces čakať, je uložený do fronty blokovaných procesov čakajúcich na rovnakú akciu  
* v skutočnosti je teda semafor štruktúra, obsahujúca celočíselnú premennú a FIFO frontu blokovaných procesov  
  [obrazek: image58]  
  [obrazek: image59]  
- S.count musí byť inicializované na nezápornú hodnotu  
- Ked je **S.count \>= 0** tak udáva počet procesov, ktoré môžu použiť P(S) bez toho aby boli zablokované  
- Ked je **S.count \< 0** tak udáva počet procesov ktoré čakajú na semafor  
- telá funkcií P(S) a V(S) sú kritické sekcie \- 2 procesy nemôžu byť súčasne v oboch

## **Př. 7**

LINDA

### **Řešení:**

[obrazek: image60]   
[obrazek: image61]

## **Př. 8**

MPI \- priemer čísel väčších ako priemer všetkých

### **Řešení:**

   MPI\_Init(&argc, &argv); 

   int rank,size,sum;

   MPI\_Comm\_rank(MPI\_COMM\_WORLD, &rank);  
   MPI\_Comm\_size(MPI\_COMM\_WORLD, &size);  
   int buf\=(rank\*1234)%33; //"random" data 

   MPI\_Reduce(&buf,&sum,1,MPI\_INT,MPI\_SUM,0,MPI\_COMM\_WORLD);

   double avg;  
   if (rank \== 0) avg \= (double)sum / (double)size;  
   MPI\_Bcast(&avg,1,MPI\_DOUBLE,0,MPI\_COMM\_WORLD);

   bool largerThanAvg \= buf \> avg;  
   int cntBuf;  
   buf \= largerThanAvg ? buf : 0;  
   cntBuf \= largerThanAvg ? 1 : 0;

   int cntSum;  
   MPI\_Reduce(&cntBuf,&cntSum,1,MPI\_INT,MPI\_SUM,0,MPI\_COMM\_WORLD);  
   MPI\_Reduce(&buf,&sum,1,MPI\_INT,MPI\_SUM,0,MPI\_COMM\_WORLD);

   if (rank \== 0) {  
       avg \= double(sum) / double(cntSum);  
       std::cout \<\< avg \<\< std::endl;  
   }  
   MPI\_Finalize();

Pre 2018/19 a staršie pozri druhý doc, link na 1\. strane v materiáloch

# **Semestrálna skúška 2018/2019 \- riadny termín \- skupina A**

*Zadanie je prepísané doslovne 1:1*

## **Př. 1 (6b)**

Odpověď na příklady 1-3 musí být provedena zakroužkováním správné volby v tomto zadání (odpovědi na přiloženém papíře nebudou hodnoceny). Možnosti odpovědí pro příklady 1 až 3 jsou následující:  
a) konstantní  
b) logaritmická  
c) n.log n  
d) lineární  
e) kvadratická  
f) polynomiální

1. mějme výpočetní model PRAM s N procesory. Jaká bude **cena** optimálního algoritmu, který spočte **AND prvků 1/0** v posloupnosti n prvků (pro n=N) v případě:  
   1. EREW PRAM    
   2. CREW PRAM  
   3. common CRCW PRAM  
2. mějme výpočetní model PRAM s N procesory. Jaká bude **cena** optimálního algoritmu, který zjistí, zdali se v posloupnosti n prvků (pro n=N) **nachází alespoň dva rozdílné** (tedy že není posloupností stejných prvků) v případě:   
   1. EREW PRAM  
   2. CREW PRAM  
   3. common CRCW PRAM  
3. mějme výpočetní model PRAM s N procesory. Jaká bude **časová složitost** optimálního algoritmu, který spočte **průměrnou hodnotu** posloupnosti n prvků (pro n=N) v případě:  
   1. EREW PRAM   
   2. CREW PRAM  
   3. common CRCW PRAM

### 

### **Řešení:**

1. AND  
   1. c) n log n  
   2. c) n log n  
   3. d) linearni  
2. nachází alespoň dva rozdílné  
   1. c) n log n  
   2. c) n log n  
   3. d) linearni  
3. Prumer  
   1. b) logaritmická  
   2. b) logaritmická  
   3. b) logaritmická

ANO: 1x  
NE: 0x (V 2\. nemalo by to byť hľadanie maxima a minima a potom porovnanie? Čiže v odpovedi common CRCW PRAM by malo byť 2 \* (n \* log(n)) \= n log n  
–tady není nutné hledat max/min, stačí když:

1) každý procesor si vezme jednu hodnotu O(1)  
2) např. procesor s rank \== 0 umístí svoji hodnotu do sdílené paměti O(1)  
3) každý procesor si tu hodnotu natáhne a porovná se svojí O(1)  
4) pokud nějaký procesor má různé hodnoty, tak tu informaci někam zapíše a jelikož těchto procesorů může být víc tak u CREW by to byl problém, ale tady to bude v O(1)

–takže cena \= n)

## **Př. 2 (9b)**

Uveďte, na jakých úrovních lze spatřovat **granularity paralelismu**. jednotlivé úrovně stručně popište z hlediska paralelizace.

### **Řešení:** 

\[prednaska PDA0102\_Arch\_MNG stranka 21 slajd 40\]

* Uvnitr instrukci  
  * Nejjemnejsi paralelismus  
  * Programator nema nad tim kontrolu a nejsou viditelne pro programatora  
  * Pri vykonaní inst-ci nektere akce se provadeji paralelne  
* Mezi instrukci  
  * Nektere inst-ci se provadeji paralelne, ale neni to videt na urovni prog jazyka  
  * Typicke zretezeni u RISC  
* Mezi prikazy  
  * Vektorove pocitace  
  * Specializovane koprocesory (FPU)  
  * Programátor ma nad tim urcitou kontrolu  
* Mezi bloky procesu (vlakna, thready)  
  * predpoklada se ze mame sdileny adresovy prostor a vytvoreni noveho vlaklna skoro zadarmo  
  * Programator muze to ovlivnovat  
* Mezi procesy  
  * zpravidla nemaji sdilenou pamet  
  * Muzou byt kompilovane oddelene

## **Př. 3 (9b)**

Uveďte algoritmicky **Odd-Even transposition sort** a odvoďte jeho **cenu**.

### **Řešení:**

**[obrazek: image62]**  
**[obrazek: image63]**

## **Př. 4 (9b)**

Uveďte, k čemu u **Meakawova algoritmu** slouží **kvóra**, co musí splňovat a jak se určují pro nějakou množinu procesů. Názorně ilustrujte obrázkem

\<i v prednaskach algos je uplne na picu vysvetlen, takze nvm\>

### **Řešení:**

Kvórum, definice, účel: podmnožina procesů o velikosti alespoň odmocniny celkového počtu procesů. Každé 2 kvóra musí mít alespoń jeden společný proces

Kvórum, alg. nalezení: pro n procesorů, kde n \= a^2 | a ∈ ℕ, jinak nějaké matematické metody.. ale asi by se pro menší počet procesorů dalo určit nějak iterativně na zkoušce  
 [obrazek: image64]  
Obr:

## **Př. 5 (9b)**

Paralelní **procesy zapsané níže v jazyce Π kalkulu redukujte všemi možnými způsoby**. V každé fázi redukce včetně původního zápisu uveďte, pokud existují, **jaká pozorování platí** (např. ↓x, ↓neg(z) atd.)[obrazek: image65]

### **Řešení:**

### **[obrazek: image66]**

*src: [https://discord.com/channels/461541385204400138/621775635722928128/840993532240068608](https://discord.com/channels/461541385204400138/621775635722928128/840993532240068608)*  
pár drobností \- ak je samotná 0 v procese, nepíše sa  
na konci v zadaní je P’ (P s čiarkou), pričom tá čiarka sa od oranžového riadku stratila, pozor na to  
nestratili sa tam niekde \< a \>? viem, že sme neprišli na to, ako sa s nimi pracuje, ale minimálne zapísané by byť mali, nie?  
v zelenom výsledku je neg(a) (c), pričom c by nemalo byť v zátvorke

## **Př. 6 (9b)**

Pro graf G=(V, E), V \= {v1, v2, v3, v4, v5, v6} a E \= {e1, …, e14},  
e1 \= (v3, v6), 		e2 \= (v6, v3),  
e3 \= (v5, v3), 		e4 \= (v3, v5),  
e5 \= (v1, v2), 		e6 \= (v2, v1),  
e7 \= (v3, v4), 		e8 \= (v4, v3),  
e9 \= (v1, v3), 		e10 \= (v3, v1),  
e11 \= (v4, v5), 	e12 \= (v5, v4),  
e13 \= (v4, v6), 	e14 \= (v6, v4),  
demonstrujte názorně paralelní výpočet Eulerova tahu.

### **Řešení:**

### [obrazek: image67]

[obrazek: image68]

## **Př. 7 (9b)**

Algoritmem **Carry Look Ahead Parallel Binary Adder** proveďte **součet čísel 90 a 139**. Názorně demonstrujte jednotlivé kroky. Musí být jasné, jak celý proces sčítání probíhá.

### **Řešení:**

[obrazek: image69]

## **Př. 8 (10b)**

**Naprogramujte paralelní** algoritmus v jazyce **C++** s pomocí knihovni **MPI**, který bude mít **logaritmickou časovou složitost** a který provede **součet čísel posloupnosti, která jsou větší než její průměr**. K dispozici máte knihovní funkcie v podobě:   
**MPI\_Bcast (adresa\_hodnoty, root)**  
**MPI\_Reduce (adresa\_send, adresa\_recv, operace, root)**.  
Každý proces má hodnotu prvku posloupnosti na pozici svého ranku uloženou v proměnné value. Také má uložen celkový počet procesorů v proměnné numprocs a svůj rank v proměnné rank. Výsledek je vypsán na obrazovku.

### **Řešení:**

   MPI\_Init(&argc, &argv); 

   int rank,size,sum;  
   MPI\_Comm\_rank(MPI\_COMM\_WORLD, &rank);  
   MPI\_Comm\_size(MPI\_COMM\_WORLD, &size);  
   int buf\=(rank\*1234)%33; //"random" data 

   MPI\_Reduce(&buf,&sum,1,MPI\_INT,MPI\_SUM,0,MPI\_COMM\_WORLD);

   double avg;  
   if (rank \== 0) avg \= (double)sum / (double)size;  
   MPI\_Bcast(&avg,1,MPI\_DOUBLE,0,MPI\_COMM\_WORLD);

   buf \= buf \> avg ? buf : 0;  
    
   int cnt;  
   MPI\_Reduce(&buf,&cnt,1,MPI\_INT,MPI\_SUM,0,MPI\_COMM\_WORLD);  
   if (rank \== 0) std::cout \<\< cnt \<\< std::endl;      
   MPI\_Finalize();

# **Semestrálna skúška 2018/2019 \- riadny termín \- skupina B**

## **Př. 1** 

PRAM otazky

Cena OR postupnosti  
Cena reverzacie postupnosti    
Casova zlozitost sucinu prvkov postupnosti

### **Řešení:**

**Cena OR postupnosti**

- EREW PRAM 			n\*log n  
- CREW PRAM			n\*log n  
- common CRCW PRAM	n

**Cena reverzacie postupnosti**

- EREW PRAM 			???  
- CREW PRAM			???  
- common CRCW PRAM	???

**Casova zlozitost sucinu prvkov postupnosti**

- EREW PRAM 			log n (cena *n log n*, pozor, na co se ptají)  
- CREW PRAM			log n  
- common CRCW PRAM	log n

Reverse neni to stajne co serazeni? \-\> stejna cena jako u serazeni by bylo

### **Řešení:**

**PRAM \- Parallel Random Access Machine**

## **Př. 2**

Popisat architekturu PRAM \+ obrazok

* synchrónny model paralelneho vypoctu, procesory komunikujú zdielanou pamatou  
* skladá sa z p procesorov RAM

* **Pamäť (sada registrov):**  
  * neobmedzený počet

* Je to alternetívny model k paralelnému Turingovmu stroju  
* Všetky RAMy sú riadené jedným spoločným programom  
  [obrazek: image70]  
* **Definicia :**   
  * PRAM je synchrónny model paralelného výpočtu, v ktorom procesory komunikujú zdieľanou pamäťou. Skladá sa z p procesorov P1...Pn, ktoré sú typu RAM.  
  * Výpočet prebieha po krokoch synchrónne:   1\. čítanie zdieľanej pamäte

    2\. lokálny zápis

    3\. zápis do zdieľanej pamäte 

**Obmedzenie prístupu k zdieľanej pameti**

* 4 rôzne architektúry prístupu pamäti:  
  * EREW \- exclusive read, exclusive write  
  * ERCW \- exclusive read, concurrent write \- nepoužíva sa  
  * CREW \- concurrent read, exclusive write  
  * CRCW \- concurrent read, concurrent write \- spĺňajú len niektoré architektury

## **Př. 3** 

Popisat Paralell splitting \+ uviest mensi priklad

### **Řešení:**

**\-mam trosku problem pochopit o co tu ide, z prednasky mi to nie je jasne, ma sa rozdelit nezoradena postupnost a skoncit rozdelena nezoradeno? napr. 3,5,1,9,2,10**  
**rozdelime podla m=5 na L \= 3,1,2; E \= 5 a G \= 9,10? akeby sme mali 3 procesory tak kazdy si vezme 2 cisla, urobi si LEG a potom ich spoji do kopy hej?**

* jeho ulohou je rozdelit postupnost S podla cisla m na 3 casti:  
  * L \= {si € S: si \< m}  
  * E \= {si € S: si \= m}  
  * G \= {si € S: si \> m}  
- Po tom co se vytvoří se vypočítá, kam mají procesory ukládat své výsledné posloupnosti (suma prefixů), aby mohly ukládat současně a nemusely čekat, než budou uloženy všechny předchozí hodnoty.

* u sekvencneho algoritmu mame zlozitost O(n)

[obrazek: image71][obrazek: image72]

## **Př. 4**

Popisat princip Suzuki algoritmus. Nakreslit obrazok na priklad: Mame styri procesory (uzly), jeden, ktory nema token, ziada o KS. (Tri mensie obrazky)

### **Řešení:**

\-token aj procesy obsahuju vektor, pri tokene to označuje kolkokrát bol token ktorému procesu prideleny, pri procese to označuje koľkokrát zažiadal o token  
\-ak chce proces vstúpiť do KS, odošle ostatńym procesom správu s číslom, ktoré udáva koľkikrát o KS žiada. Procesy si hodnotu upravia ak je nižšia než ta čo prišla, následne proces ktorý ma token odošle danému procesu token, daný proces ak obdrží token zvýši hodnotu v jeho čítači  
\- ak žiadaju o token viaceré procesy, tak je odoslaný tomu ktorý je prvý vo fronte, podľa nejakého kritéria  
**[obrazek: image73][obrazek: image74]**

## **Př. 5**

Pi kalkul \- redukovat vyraz a napisat pozorovania

### **Řešení:**

## **Př. 6**

Random mating demonstrovat na 8 prvkoch, tak aby algo skoncil v 4 krokoch. Obe faze.

### **Řešení:**

## **Př. 7**

CLA scitacka. 77 \+ 125\. Popisat vsetko potrebne.

### **Řešení:**

**[obrazek: image75][obrazek: image76]**  
**ako sa ziska ten posledny riadok Z??? xi \+ yi \+ ci (mod 2\) je to \**binarni\** scitani, tim padem zadny (mod 2\) \<= lol, student MITu**  
**Ako sa prosim vypočítal ten riadok C a ten riadok s kruzkom nad nim?**  
**To je suma prefixů daného operátoru ˚ pro CLA, nosič {p, g, s}, p neutrální prvek, s a g levě agresivní. Symbol g generuje 1 ve vyšším bitu, s generuje 0 ve vyšším bitu, p propaguje současný bit výše.**

## **Př. 8**

MPI \- Zistit pocet prvkov, ktore su maximami alebo minimami.

### **Řešení:**

**[obrazek: image77]**

# **Semestrálna skúška 2018/2019 \- riadny termín \- skupina C**

## **Př. 1** 

PRAM otazky  
pro kazdou otazku byly 3 podotazky jak je to u EREW, CREW a common CRCW  
1a) časová zložitosť operácie XOR  
1b) cena kontroly či daná postupnosť je monotónna  
1c) časová zložitosť súčtu absolútnych hodnôt prvkov postupnosti

### **Řešení:**

**1a) časová zložitosť operácie XOR**

- EREW PRAM 			log n  
- CREW PRAM			log n  
- common CRCW PRAM	log n

**1b) cena neceho**  
**1c)časová zložitosť súčtu absolútnych hodnôt prvkov postupnosti**

- EREW PRAM 			log n  
- CREW PRAM			log n  
- common CRCW PRAM	log n

*tymto si niesom ista, je to len z mojej hlavy, riesime len sucet hodnot, lebo absolutnu hodnotu si urobi kazdy procesor sam za konstantny cas*

## **Př. 2**

Popsat architekturu zretezenych procesoru \+ nakres

### **Řešení:**

* lineárne prepojené procesory  
* riešenie úloh s prúdovým charakterom  
* data prechádzajú postupne jednotlivými procesormi  
  [obrazek: image78]  
- v prednaskach je aj tento obrazok, nejde vsak o zretazenie instrukcii a nie procesorov? ved zretazene instrukcie sa daju vykonavat na 1 procesore nie?  
  [obrazek: image79]

## **Př. 3** 

Popsat odd-even merge \+ nakresliť chceli všeobecnú schému a sieť 4x4 pomocou CE blokov

### **Řešení:**

* každý procesor má 2 výstupné a 2 vstupné kanály  
* každý procesor porovná hodnoty na svojich vstupoch a menší dá na výstup L(Low) a väčší na výstup H (High)

[obrazek: image36]  
[obrazek: image80]

## **Př. 4**

Popsat Marzullo algoritmus, okrem popísania bol aj príklad podobný prednáškam

### **Řešení:**

\- NTP používa marzullov alg. na stanovenie času z líšiacich sa odpovedí časových serverov

[obrazek: image81][obrazek: image82]

## **Př. 5**

Pi kalkul \- redukovat vyraz a napisat pozorovania

### **Řešení:**

## **Př. 6**

zadané nejaké prvky, spraviť prescan \- napísať výsledok po prvom kroku a po skončení upsweep, potom výsledok po prvom kroku a po skončení downsweep (za predpokladu že na začiatku downsweepu bol vložený už neutrálny prvok na poslednú pozíciu)

### **Řešení:**

1. UpSweep \- každému uzlu sa priradí súčet jeho synov  
2. DownSweep :  a) koreňu sa priradí neutrálny prvok

   b) ďalej dá každý uzol:

   \-- svoju pravému synovi: svoju hodnotu ⊕ hodnotu Laveho syna

   \-- svojmu lavemu synovi: svoju hodnotu

   \- krok b) sa prevedie postupne pre každú úroveň (teda log n krat) a robí sa paralelne v každej úrovni

[obrazek: image83]  
[obrazek: image84]  
**Príklad na preskúšanie:**  
**prvky : 5, 1, 6, 10, 3, 8, 2, 4**   
Riesenie:d  
**[obrazek: image85]**  
**Imo je v UpSweep chyba a měl by končit číslem 39 (Reduce všech čísel s operací plus-\> 22+17) \+1 DownSweep mi vyšel stejně \+1**

## **Př. 7**

CLA scitacka. 77 \+ 125\. Popisat vsetko potrebne.

### **Řešení:**

## **SPř. 8**

MPI \- pocet prvku, ktere jsou bezezbytku delitelne prvnim prvkem, k dispozici pouze mpi\_bcast a mpi\_reduce, požadovali logaritmickú časovú zložitosť	

### **Řešení:**

odstrihol si  ze:   
int prvok0 \= value;	//inak to spadne,lebo budeme porovnavat nedef.  
**[obrazek: image86]**

# **Semestrálna skúška 2018/2019 \- 1\. opravný termín**

### 

pre 1\. op a starsie roky check druhy doc:  
[https://docs.google.com/document/d/18PI10fxMBaaUFgexU52Kk\_WHQrSrq5VgpGcA9IKfcvY/edit\#heading=h.swp6u0hxje7b](https://docs.google.com/document/d/18PI10fxMBaaUFgexU52Kk_WHQrSrq5VgpGcA9IKfcvY/edit#heading=h.swp6u0hxje7b)






















































































