# Discord analysis scratchpad

This is a side analysis generated from `raw/discord/<year>/621775635722928128.json`.
It does not modify the knowledge base.

## High-level

- Years covered: 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026
- Total messages: 28465
- Bot messages: 78 (0.27%)
- Attachments: 1390
- Embeds: 288
- Reactions: 5892
- Pinned messages: 26
- Link-bearing messages: 365

## Strong signals

- Peak month by volume: `2022-05` with `6911` messages.
- Peak day by volume: `2022-05-15` with `1263` messages.
- Most active author overall: `monnte` with `1451` messages.

## Topic counts

- `MPI`: 822 mentions across 643 messages.
- `PRAM`: 469 mentions across 344 messages.
- `Euler/suffix`: 414 mentions across 342 messages.
- `Pi-kalkul`: 297 mentions across 290 messages.
- `Distributed`: 245 mentions across 206 messages.
- `Broadcast/FIFO/kauzalita`: 236 mentions across 181 messages.
- `Monitory/semafory`: 230 mentions across 175 messages.
- `OCCAM`: 220 mentions across 192 messages.
- `Random/list`: 185 mentions across 166 messages.
- `CLA`: 56 mentions across 55 messages.
- `Mutual exclusion`: 45 mentions across 43 messages.

## Topic examples

### PRAM

- `2020` `2020-04-17T04:52:04.04+00:00` `the_mozes`: > Tu časovou složitost máme popisovat podle naší implementace, nebo podle přednášek (materiálů)? Ze zpětné vazby minulého projektu mi to není úplně jasné. @Tasemal já když sem mu to u 1. popsal jako to bylo v přednáškách tak mi řekl že je to správně a dal mi za to body. třeba ...
- `2020` `2020-04-17T19:28:57.117+00:00` `xgoldpal`: @Mozes ono ideálně by to neměl být binární, ale N-ární strom, přičemž každý CPU by zpracoval N hodnot lokálně a pak by odeslal výsledek otci, který by ho přijal od N synů, tak zpracoval lokálně a poslal dál, takže by to mělo smysl, kdyby lokální cena byla vyšší než overhead, t...
- `2020` `2020-04-19T16:48:47.544+00:00` `lukashino`: Vysla vam cena O((n^2)/N + (n *log N) ) ?

### MPI

- `2020` `2020-04-17T19:25:48.068+00:00` `xgoldpal`: > btw jak se vám to scaluje? já když to pustim na jednom procesoru tak je to podstatně rychlejší než když začnu přidávat další a čím víc jich přidám, tím je to pomalejší (měření sem dělal až po 64 hodnot, všude stejný příběh) @Mozes zatím jsem neměřil, ale není divu, jsou to m...
- `2020` `2020-04-17T21:00:01.972+00:00` `burned2854`: Já osobně to právě kvůli tomu měřil na login uzlu (snad nebudou stížnosti 😄 ), ale Mim mi psal, že prý se dá při té alokci nastavit parametr `mpiprocs` a nějaké dodatečné info je na https://docs.it4i.cz/software/mpi/running_openmpi, ale osobně jsem to pak už nezkoušel, takže n...
- `2020` `2020-04-19T14:58:30.941+00:00` `xgoldpal`: taky vám to tak (MPI) na merlinovi extrémně zpomalilo nebo jenom nějaké moje speciální úpravy? 😄

### OCCAM

- `2020` `2020-04-17T20:57:22.26+00:00` `khub`: Podelil by se nekdo o navod, jak to na salomonu poustet? Kdyz pouziju stejny prikaz jako v AVS na vstup do queue, tak se asi nedostanu na uzel co ma 28 jader?
- `2020` `2020-04-17T21:08:34.875+00:00` `wildbitangent`: > Podelil by se nekdo o navod, jak to na salomonu poustet? Kdyz pouziju stejny prikaz jako v AVS na vstup do queue, tak se asi nedostanu na uzel co ma 28 jader? @Khub $ qsub -q qexp -l select=1:ncpus=24:mpiprocs=24:ompthreads=1 -I Pokial chces viac uzlov, tak selecet=N (az 8) ...
- `2020` `2020-05-26T15:39:47.814+00:00` `betsst`: @Crash https://discordapp.com/channels/461541385204400138/621775635722928128/675695483548729354

### Random/list

- `2020` `2020-04-17T21:08:34.875+00:00` `wildbitangent`: > Podelil by se nekdo o navod, jak to na salomonu poustet? Kdyz pouziju stejny prikaz jako v AVS na vstup do queue, tak se asi nedostanu na uzel co ma 28 jader? @Khub $ qsub -q qexp -l select=1:ncpus=24:mpiprocs=24:ompthreads=1 -I Pokial chces viac uzlov, tak selecet=N (az 8) ...
- `2020` `2020-05-30T18:57:51.432+00:00` `rozmaryn6921`: mate nekdo prosim doreseny priklad na pipeline merge sort na strane 12 v PDA0304? stale mi to nevychazi tak zda by nekdo sem nehodil info jak na to
- `2020` `2020-06-04T12:07:50.688+00:00` `berkelos`: Zdravím, rozumí někdo tomu algoritmu podle kterého se provedl tento pipeline merge sort? Na netu jsem našel nějaké způsoby, ale ani jeden neseděl pro příklad ve slajdech.

### Distributed

- `2020` `2020-04-19T15:13:57.993+00:00` `maszko`: ak pouzivate broadcast na rozoslanie, davate ho do komunikacneho protokolu?
- `2020` `2020-04-19T16:51:48.112+00:00` `lukashino`: ale podla fora by si mohol aj Allgather prip Broadcast
- `2020` `2020-06-04T15:32:43.986+00:00` `lgtm`: Suzuki, Pi kalkul, a take

### Pi-kalkul

- `2020` `2020-06-01T06:42:34.058+00:00` `.qbasty`: Neví někdo kde (ve které přednášce) se nachází Pi-kalkul? Nikde jsem to neviděl ale bylo to minulý rok na semestrálce.
- `2020` `2020-06-04T15:32:43.986+00:00` `lgtm`: Suzuki, Pi kalkul, a take
- `2020` `2020-06-04T15:33:08.96+00:00` `brum_barnum`: A teraz je pi kalkul niekde? (V nových)

### Euler/suffix

- `2020` `2020-06-05T15:05:00.241+00:00` `mitches_`: ale ten Euler mě dost štve sakra 😄
- `2020` `2020-06-06T17:08:11.186+00:00` `burned2854`: Tohle není ranking algoritmus, takže nepočítáme vzdálenost od konce, ale opravdu počítáme sumu suffixu. Tím pádem musíme nastavit ten poslední prvek na neutrální hodnotu pro danou operaci, protože jinak by se v tom cyklu neustále ta hodnota přičítala a dostal by jsi špatný výs...
- `2020` `2020-06-08T12:01:14.6+00:00` `brum_barnum`: Semestralka: pram, Occam, mpi počet čísel vetsi než priemer, random mating, Euler tour preorder, monitor

### Monitory/semafory

- `2020` `2020-06-07T19:34:04.004+00:00` `xgoldpal`: náhodou někdo vysvětlení k tomu monitoru? 😄 Nechápu moc tu urgentní queue. Na slide (i dle obrázku) to vypadá tak, že se z nějakého důvodu ukladá do urgent queue volající té signal procedury, ze záznamu říkal, že se tam umístňují procesy, které byli předtím v condition queue a...
- `2020` `2020-06-08T12:01:14.6+00:00` `brum_barnum`: Semestralka: pram, Occam, mpi počet čísel vetsi než priemer, random mating, Euler tour preorder, monitor
- `2021` `2021-04-20T19:55:42.354+00:00` `kateriska`: @Dajvid wait kdy jsi se narodil? :VUTrtzW:

### Mutual exclusion

- `2021` `2021-04-26T13:52:00.238+00:00` `mira9566`: "typek" je program a "objektivny duvod" je deadlock.
- `2021` `2021-04-27T20:30:54.136+00:00` `francze`: :monkahmm: ty procesory jen čtou, je tam i tak lock na ten soubor aby to "časově" případně vadilo? 🤔
- `2021` `2021-04-29T12:55:52.226+00:00` `tomas238`: ja tam mam neaky steady clock

### CLA

- `2021` `2021-05-09T19:46:00.423+00:00` `tomas238`: ako mu pri tej CLA vyslo s ako neutralny prvok? :HAhaaVUT:
- `2021` `2021-05-09T19:50:13.53+00:00` `ishanka`: nejvic me na te CLA sere
- `2021` `2021-05-10T15:28:09.392+00:00` `betsst`: 1.- cena XOR -casova zlozitost OR - cena suctu? maxima a minima 2. test &set 3. kauzalita 4. Euler tah -suffix? 5. R-A 6. Euler strom/graf? 7. Carry look ahead add - spocitat 39 a 110 8. naprogramovat s logickou zlozitostou sucet hodnot nez vacsich nez priemer? ----- ak si nie...

### Broadcast/FIFO/kauzalita

- `2021` `2021-05-10T15:28:09.392+00:00` `betsst`: 1.- cena XOR -casova zlozitost OR - cena suctu? maxima a minima 2. test &set 3. kauzalita 4. Euler tah -suffix? 5. R-A 6. Euler strom/graf? 7. Carry look ahead add - spocitat 39 a 110 8. naprogramovat s logickou zlozitostou sucet hodnot nez vacsich nez priemer? ----- ak si nie...
- `2021` `2021-05-10T16:46:28.124+00:00` `ishanka`: ale tak rip A, mozna jeste kapne B, kdyz zavre oci u kauzality :VUTrtzW:
- `2021` `2021-05-24T21:43:59.111+00:00` `chichin`: linda, occam, suzuki, meakow, marzul,broadcast abcast, takove ty sipecky co ani uz nevim k cemu to bylo...
