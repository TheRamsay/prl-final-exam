# Broadcast/FIFO/kauzalita from Discord

Focused side analysis of broadcast/FIFO/kauzalita references in the Discord export.

## Counts by year

| Year | Topic messages |
| --- | ---: |
| 2019 | 0 |
| 2020 | 5 |
| 2021 | 25 |
| 2022 | 84 |
| 2023 | 58 |
| 2024 | 57 |
| 2025 | 5 |
| 2026 | 5 |

## Observations

- Total topic mentions: 239
- Messages that look like exam reconstructions: 8
- Messages that talk about send/recv/algorithms/diagrams: 45
- Messages that look like confusion or pain points: 13
- Messages explicitly talking about properties (`FIFO`, `kauzalita`, `atomicita`): 136
- Most active authors on this topic: monnte (16), rys8515 (10), no.body.the.sad.slider.boy (9), safarmirek (8), kristyna4270 (7), duristomas67 (7), jany26 (7), maybe_coffee (6)

## What Discord focuses on

- Exact exam forms: either `send/recv` algorithm, or a diagram/table where you classify FIFO/kauzalita/atomicita.
- Repeated confusion about the distinction between FIFO, causality, and atomicity.
- Repeated complaints about `random tabulka`, `šipečky`, and unclear broadcast diagrams.
- Some confusion in chat mixes MPI broadcast with the distributed-systems broadcast topic, so raw Discord needs filtering.

## Exam-like messages

- `2021` `2021-06-09T11:23:55.195+00:00` `nitram147`: 1.) PRAM tipovačka 2.) VLIW + ako sa riešia konflikty 3.) Monitor - popis + obrázok 4.) Problém 5 filozofov - kód so semaformi + popis ako to funguje (plus musel byt deadlock proof ten kód) 5.) Nieco s FIFO a broadcastom, nejaká random tabuľka, v živote som to nevidel 6.) Random mating (pravdepodobne 1:1 recycle z 1. opravného) 7.) OCCAM - naprogramovanie...
- `2023` `2023-05-14T10:12:21.215+00:00` `di3go_cz`: Výskyt otázek ze těch dvou docs (2022/2023 předtermín - 2016/2017): ```25x MPI 25x PRAM tipsport 12x Etour, suffixsum -> (preorder / následující vrcholy / cesta …) 10x něco s Broadcast FIFO / kauzalita / atomičnost (kód, graf nebo teorie) 9x OCCAM (popsat, primitiva, příklad) 9x Carry look ahead příklad 6x Monžnost převést asynchronní systém na synchronní...
- `2023` `2023-06-05T16:16:33.19+00:00` `wulferion`: 2. Opravný: ``` 1. PRAM tipování 2. Odesílání a přijímání zprávy kauzálně + definice relace kauzality 3. PRAM architektura popsat a nakreslit 4. ADA popsat + konkrétní příkazy 5. Pi calcul, 3 redukce 6. Upsweep downsweep příklad 7. 4 čítače (za 10b btw) 8. MPI v log čase zjistit, zda má posloupnost 3 a více různých hodnot ```
- `2024` `2024-04-24T14:06:45.323+00:00` `headclass`: PREDTERMIN 2023/24 1. Tipsport crcw - XOR, NAND, AND 2. PRAM model - opisat ho, nakreslit obrazok 3. Kauzalni broadcast + relace kauzality 4. Euler pro počet následovníků + popis 5. CLA 6. Meakawův algoritmus - opisat kvorum a na obrazku znazornit zalomenu verziu kvor pre 12 procesov. takto ukazte zistenie kvor pre 2 procesy 7. OCCAM - implementujte proce...
- `2024` `2024-05-13T15:24:18.353+00:00` `fadofado`: 2023/24 - Řádný - Skupina B 1.) PRAM "tipovacka" (6b) a) časova složitost: **XOR** pro EREW, CREW, common CRCW b) časova složitost: **počet sudych čísel** pro EREW, CREW, common CRCW c) cena: **NAND** pro EREW, CREW, common CRCW 2.) Popiště architekturu procesů s velkým kódovým slovem (**VLIW**). Popiště možné konflikty a způsob jejich předcházení, resp. ...
- `2024` `2024-05-27T13:39:17.712+00:00` `jany26`: 1. opravny 2024 1) 6b: PRAM (EREW, CREW, COMMON CRCW): cena zoradit sekvenciu, cena XOR, casova zlozitost AND 2) 9b: a) FIFO broadcast send, recv algoritmus, b) definovat relaciu kauzality, 3) 9b: testandset riesenie kritickej sekcie - kod plus popis, 4) 9b: algoritmus 4 citacov princip fungovania plus nakreslit 2 obrazky, v jednom sa detekovalo ukoncenie...
- `2024` `2024-06-03T12:40:15.429+00:00` `yamauu`: 2. opravny 2024 1. PRAM sazka 1) cena vypoctu absolutnich hodnot posloupnosti kladnych cisel (:OMEGALUL:) 2) casova slozitost OR 3) cena zjisteni, jestli je posloupnost fibonnaciho sekvence 2. parallel splitting 3. Suffix sum na strome algoritmus + popsat postup 4. Ada - naco sa pouziva select a accept a co sa pouziva na synchronizaciu 5. Broadcast: FIFO,...
- `2025` `2025-05-11T19:53:25.858+00:00` `michal3441`: Toto inac bolo na predtermine 1. EREW/CREW tipovacka, kde musis vybrat zlozitost algoritmu 2. definovat ako funguju zretazene procesory a ake konflikty mozu nastat 3. Random mating alg, mas navrhnut ako sa budu pseudonahodne generovat tie male a female tokeny tak, aby skoncil po 4 iteraciach 4. Select sort na vyber k-teho prvku (opisat a ukazat hocijaky p...

## Algorithm/diagram messages

- `2020` `2020-06-08T16:58:12.17+00:00` `betsst`: **Polsemka** 1. Uplne prepojenie topologia 6 uzlov - diagram, konektivita, bisekcia 2. Ktore z uvedený dvojic algoritmov su optimalne (pipeline merge, od even transposition a odd even merge sort myslim) 3. PRAM - ma/nema zdielane/lokalne pamati 4. Popis redukcnych pc **Test** 1. I cena alg ktory zoradi, II cena ktory zisti ci je nejaky zhodny, III casova ...
- `2021` `2021-06-09T11:23:55.195+00:00` `nitram147`: 1.) PRAM tipovačka 2.) VLIW + ako sa riešia konflikty 3.) Monitor - popis + obrázok 4.) Problém 5 filozofov - kód so semaformi + popis ako to funguje (plus musel byt deadlock proof ten kód) 5.) Nieco s FIFO a broadcastom, nejaká random tabuľka, v živote som to nevidel 6.) Random mating (pravdepodobne 1:1 recycle z 1. opravného) 7.) OCCAM - naprogramovanie...
- `2022` `2022-04-28T17:27:39.839+00:00` `rys8515`: send recv, broadcast, gather, allgather
- `2022` `2022-05-13T07:48:51.455+00:00` `janosamek`: Odpoveď od Zbořila na ten deliver (ak by niekoho zaujímalo): deliver je doručení, totiž ona zpráva nemusí být doručena v okamžiku, kdy se objeví 'na železe', na aplik.úrovni si systém sám rozhodne,kdy zprávu doručí, aby zajistil FIFO nebo kauzalitu. Doručení na železo / uzel je receive
- `2022` `2022-05-14T21:53:56.359+00:00` `kristyna4270`: ale máš tam FIFO doručování zpráv, takže tam nemůžou mít stejná časová razítka či?
- `2022` `2022-05-15T08:40:29.572+00:00` `kristyna4270`: atomicita spočívá v tom, že: - všechny procesy přijmou všechny zprávy ve stejném pořadí - ale ne v tom samém, jak byly vysílány (ve fyzickém čase) - ale v nějakém pořadí, které zachovají všechny procesy ⇒ tj. agreement mezi procesy
- `2022` `2022-05-16T00:47:02.722+00:00` `rys8515`: spravis si vsetky mozne pary (send(msg_i), recv(msg_j)), kde send(msg_i) ->e recv(msg_j) -- je kauzalne pred -- a ked v nich je cyklus tak je tam koruna a nejde to spravit synchronne
- `2022` `2022-05-16T06:52:07.316+00:00` `lada_42`: @Lori tady máš příklad. Tady ta zpráva přišla tomu procesu a až potom na ni reagoval - kauzalita splněna. Pokud by ale to modry kolečko předchazelo tomu doručeni, tak je kauzalita porušena
- `2022` `2022-05-16T07:14:12.395+00:00` `rys8515`: FIFO = P1 posle spravu m1 a potom spravu m2, najskor sa musi vsetkym dorucit m1 a az potom m2
- `2022` `2022-05-16T07:15:01.458+00:00` `rys8515`: kauzalita = P1 posiela vsetkym spravu m1, procesor P2 prijme m1 a posiela vsetkym spravu m2, najskor sa musi vsetkym dorucit sprava m1 a az potom m2
- `2022` `2022-05-16T08:36:37.887+00:00` `dj_boeing`: jaky je teda rozdil mezi FIFO, kauzalnim a atomickym vysilanim? nejak to v tom nevidim
- `2022` `2022-05-26T11:28:45.312+00:00` `sebasuuu`: v docu je napisane ze "Pro každý proces si vypíšeme všechny send(m_i) -> receive(m_j), které jsou v relaci kauzality: -e>." ale 6. proces ma najprv receive 2 a potom send 6, nemalo by to teda byt 6. proces = (6,2) ?
- `2022` `2022-05-27T11:10:54.169+00:00` `sebasuuu`: A: - popísať Algo na CRCW pre AND a uviesť príklad - kde by sme využili MIMD, popísať + obrázok - suffixsum pre euler path výpočet úrovne vrcholu - MPI nájsť či suma prvkov v 1. Polovici je menšia ako suma prvkov v 2. Vypísať áno alebo nie - ako budú vyzerať procesory v 12. Kroku pri pipeline sort - async -> či sa dá tak ako, kde to vidime atď. - OCCAM ch...
- `2022` `2022-06-07T14:58:11.412+00:00` `sebasuuu`: - PRAM tipovačka - data flow architektúra popísať + obrázok - semafor popísať P a V operácie - FIFO broadcast ako prebieha prijímanie a odosielanie a algoritmy - async na Sync príklad - random mating príklad, skončiť prvú fázu do 4 krokov - LINDA vyhľadávanie v lineárnom zozname - MPI nájsť druhé maximum, pozor hodnoty môžu byť aj záporné
- `2023` `2023-05-13T11:57:44.205+00:00` `duristomas67`: zlava do prava ti ide ako keby čas a tie vodorovne čiary su procesy. Pre každý send (zelene koliečko) si vypíšeš relácie kauzality, teda všetky receive čo nasleduju po nom teda pre m1 (proces 1) by to bolo (send1, recieve2), (send1, recieve 3), potom pre proces 2 by to bolo (send2, receive1), (send2, receive3) a pre trojku (send3, receive2), (send3, recei...
- `2023` `2023-05-13T12:02:28.118+00:00` `duristomas67`: aby si videl aj niečo kde nie je koruna tak napríklad toto z prednášky ked vypíšeš rovnako tie kauzality tak máš (s1,r2), (s1,r3), (s2,r3) (po send3 napríklad už ide len receive3 čo ignoruješ, vypisuješ len tieto či idu ako keby medzi procesmi a nie len v rámci 1 lebo to je logické že bude vždy po sende) no a tu korunu nikdy nenájdeš - cyklus
- `2023` `2023-05-13T12:32:35.213+00:00` `jak3_117`: Well, nwm jestli to dobre, ale podle me to jde delat jednoduse. U synchronizovane komunikace musi byt, ze time(send) == time(recieve). Takze ty kauzalni zavislosti se daji urcit tak, ze zanedbavas barvicky a jdes pouze postupne po lifeline kazdeho procesu zleva doprava. Zajima te teda jenom, ke ktere zprave dana tecka patri. Z toho urcis, ty zavislosti me...
- `2023` `2023-05-13T12:49:56.951+00:00` `jak3_117`: Vlevo mas originalni asynchroni komunikaci, vpravo vyslednou po synchronizaci. Proste u synchroni odeslani i doruceni probihaji ve stejny okamzik. Takze je muzes pri urcovani tech kauzalnich zavislosti vzajemne zamenovat diky tomu.
- `2023` `2023-05-13T13:34:52.798+00:00` `diskordsux`: podle těchto slajdů to chápu tak, že atomičnost znamená, že je ten broadcast reliable (což se asi u těchto úloh předpokládá automaticky) a v úplným pořadí, tzn. když procesy _p_ a _q_ doručí zprávy _m_ a _n_, tak když třeba _p_ je doručí v pořadí _m_ -> _n_, pak je doručí v tomto pořadí i _q_
- `2023` `2023-05-13T17:00:11.93+00:00` `monnte`: send(m1) -> recive(m2) send(m2) -> recive(m1) nastane a to je jedno kolko sprav medzi tým bude že sa takto cyklom dostaneš spet k m1 tak to je koruna
- `2023` `2023-05-14T10:12:21.215+00:00` `di3go_cz`: Výskyt otázek ze těch dvou docs (2022/2023 předtermín - 2016/2017): ```25x MPI 25x PRAM tipsport 12x Etour, suffixsum -> (preorder / následující vrcholy / cesta …) 10x něco s Broadcast FIFO / kauzalita / atomičnost (kód, graf nebo teorie) 9x OCCAM (popsat, primitiva, příklad) 9x Carry look ahead příklad 6x Monžnost převést asynchronní systém na synchronní...
- `2023` `2023-05-14T13:29:55.732+00:00` `adda00`: - algoritmy, stromy, randommating (obě fáze), broadcasty(jak funguje semafor, jak funguje monitor, ), busy waiting (test and set, peterson) - problemy paralelsimu, jak bychom resili prodcent konzument nebo 5 filozofu pomoci (), ocaml(posilat na in, na out), linda je popis primit, nebo jak byl ten seznam - nutkani tam dat redukci pcalcluc(co se muze zreduk...
- `2023` `2023-05-14T17:57:34.772+00:00` `petak5`: Spojis si uzly send s uzlami receive v ramci jedneho procesoru (jedna horizontalna ciara) a ked tam je kruznica (koruna?) tak nemozes to prerobit na synchronne
- `2023` `2023-05-15T06:55:43.533+00:00` `veverica`: > In summary, causality captures the order of events based on their causal relationships, ensuring a consistent global order of events in the system. FIFO ordering, on the other hand, specifically ensures that the temporal order of messages sent by the same sender is preserved.
- `2023` `2023-05-15T06:56:10.737+00:00` `veverica`: podla tohto je fifo merane pre toho isteho sendera
- `2024` `2024-04-24T00:22:42.013+00:00` `paetrik`: Dle mě by to mělo být takto ``` send(1) -> recv(4) send(2) -> recv(3) send(2) -> recv(6) send(3) -> recv(5) send(4) -> recv(1) send(5) -> recv(6) ``` a koruna tam tedy velikosti 2: `send(1)->recv(4),send(4)->recv(1)` Ale nejsem si jistý, zda to je správně :monkahmm:
- `2024` `2024-04-24T07:14:43.179+00:00` `enhaut`: Na riadku sú procesy, s_i sú odosielania, r_i sú príjmy, i sú označenie správ a doprava po čiara h plynie čas. Tak ideš po jednotlivých riadkoch a pozrieš sa, či máš nejaký send pred recv (kauzalne mu predchádza), ak áno tak to je ta dvojica (send časovo skôr, receive časovo neskôr). Aspoň tak som to pochopil a vychádza to
- `2024` `2024-04-24T07:26:30.913+00:00` `paetrik`: Já tu relaci kauzality chápu tak, že si položím otázku: Když na odešlu nějaké zprávy (např. m1) tak jakou zprávu díky ní můžu přijmout (nepočítám tu stejnou zprávu)? Zde to je zpráva m2. Přesněji: odešlu m1 -> můžu pak odeslat m2 -> odešlu m2 -> druhý proces přijal zprávu m2 na základě toto, že jsem odeslal zprávu m1, tedy `send(m1)` je kauzální na `recv(...
- `2024` `2024-04-24T09:56:42.089+00:00` `paetrik`: Tuto komunikaci bys mohl lehce simulovat synchronní. Relace kauzality tam jsou jenom: `send(m1) -> recv(m2)` a `send(m2) -> recv(m3)` a `send(m3)` už neřeší, protože na tom nezáleží příjem žádné zprávy. Bych teda alespoň řekl já :monkahmm:
- `2024` `2024-04-24T14:06:45.323+00:00` `headclass`: PREDTERMIN 2023/24 1. Tipsport crcw - XOR, NAND, AND 2. PRAM model - opisat ho, nakreslit obrazok 3. Kauzalni broadcast + relace kauzality 4. Euler pro počet následovníků + popis 5. CLA 6. Meakawův algoritmus - opisat kvorum a na obrazku znazornit zalomenu verziu kvor pre 12 procesov. takto ukazte zistenie kvor pre 2 procesy 7. OCCAM - implementujte proce...

## Pain points

- `2020` `2020-04-19T16:51:48.112+00:00` `lukashino`: ale podla fora by si mohol aj Allgather prip Broadcast
- `2021` `2021-05-09T14:42:16.707+00:00` `matt_3651`: Nevie niekto co chcel autor povedat tymto obrazkom pre broadcast? :peepoThink:
- `2021` `2021-05-10T16:46:28.124+00:00` `ishanka`: ale tak rip A, mozna jeste kapne B, kdyz zavre oci u kauzality :VUTrtzW:
- `2021` `2021-05-24T21:43:59.111+00:00` `chichin`: linda, occam, suzuki, meakow, marzul,broadcast abcast, takove ty sipecky co ani uz nevim k cemu to bylo...
- `2021` `2021-06-09T11:23:55.195+00:00` `nitram147`: 1.) PRAM tipovačka 2.) VLIW + ako sa riešia konflikty 3.) Monitor - popis + obrázok 4.) Problém 5 filozofov - kód so semaformi + popis ako to funguje (plus musel byt deadlock proof ten kód) 5.) Nieco s FIFO a broadcastom, nejaká random tabuľka, v živote som to nevidel 6.) Random mating (pravdepodobne 1:1 recycle z 1. opravného) 7.) OCCAM - naprogramovanie...
- `2021` `2021-06-09T19:02:38.666+00:00` `nitram147`: uprimne som cakal aj broadcast ale pozeral som tu prednasku na dvakrat a RIP
- `2022` `2022-05-14T16:24:47.553+00:00` `afos`: keď pri broadcaste chce FIFO, bude chcieť len nejaký stručný popis, že čo to je, alebo bude chcieť ten totálne wtf kód?
- `2022` `2022-05-16T08:36:37.887+00:00` `dj_boeing`: jaky je teda rozdil mezi FIFO, kauzalnim a atomickym vysilanim? nejak to v tom nevidim
- `2022` `2022-05-27T07:41:22.541+00:00` `beeblebr0x`: m1 -> m2 m2 -> m1 tak rip -> koruna -> nejdze previest na synchro
- `2023` `2023-05-14T12:50:47.59+00:00` `stupidboisbb`: ale z tohoto slajdu mi pripadne ze FIFO==kauzalita
- `2024` `2024-04-24T09:50:33.611+00:00` `penpem`: stale nechapem co je koruna
- `2024` `2024-06-03T11:30:08.66+00:00` `yamauu`: a fifo, kauzalita a atomicnost na nesrozumitelnym diagramu
- `2024` `2024-06-03T12:40:15.429+00:00` `yamauu`: 2. opravny 2024 1. PRAM sazka 1) cena vypoctu absolutnich hodnot posloupnosti kladnych cisel (:OMEGALUL:) 2) casova slozitost OR 3) cena zjisteni, jestli je posloupnost fibonnaciho sekvence 2. parallel splitting 3. Suffix sum na strome algoritmus + popsat postup 4. Ada - naco sa pouziva select a accept a co sa pouziva na synchronizaciu 5. Broadcast: FIFO,...
