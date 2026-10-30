# -*- coding: utf-8 -*-
"""
Update playground.ts, messages.ts, and all messages-*.ts files for 31 October 2026.
"""
import re
import os

DATA = {
    "en": {
        "soccer": {
            "tagline": "Premier League MW9: Arsenal and Liverpool battle to 2-2 draw at Emirates; Man City take sole top spot.",
            "liveNow": "Premier League MW9: Arsenal 2-2 Liverpool (Saka 9', Merino 43'; Van Dijk 18', Salah 81'). City 1-0 Southampton. City 23 pts, Arsenal 22, Liverpool 16.",
            "pulse": "PREMIER LEAGUE MW9: ARSENAL AND LIVERPOOL SHARE SPOILS IN 2-2 EMIRATES EPIC",
            "keywords": "Premier League, Arsenal, Liverpool, Emirates Stadium, Saka, Salah, Merino, Van Dijk, Man City"
        },
        "basketball": {
            "tagline": "NBA Saturday: Victor Wembanyama puts up 31 points and 6 blocks as Spurs tame Suns 118-106 in Phoenix.",
            "liveNow": "Final at Footprint Center: Spurs 118, Suns 106. Wembanyama 31 pts, 14 reb, 6 blk; Chris Paul 12 ast; Durant 28 pts. Spurs 3-1.",
            "pulse": "NBA SATURDAY: VICTOR WEMBANYAMA POSTS 31 POINTS AND 6 BLOCKS IN PHOENIX",
            "keywords": "NBA, Spurs, Suns, Wembanyama, Chris Paul, Kevin Durant, Phoenix, Footprint Center"
        },
        "football": {
            "tagline": "College Football Week 10: Georgia pulls away from Florida 34-20 in Jacksonville Cocktail Party to stay 8-0.",
            "liveNow": "Final in Jacksonville: Georgia 34, Florida 20. Beck 285 yds, 3 TD; Etienne 112 yds, 1 TD. Sunday: 6-0 Vikings face Colts.",
            "pulse": "COLLEGE FOOTBALL: GEORGIA OVERPOWERS FLORIDA 34-20 TO PRESERVE 8-0 RECORD",
            "keywords": "College Football, Georgia Bulldogs, Florida Gators, Carson Beck, Trevor Etienne, Jacksonville, SEC"
        },
        "tennis": {
            "tagline": "Erste Bank Open semi-finals: Carlos Alcaraz outduels Alexander Zverev 6-4, 7-6 to book ticket to Vienna final.",
            "liveNow": "Vienna ATP 500 SF: Alcaraz def. Zverev 6-4, 7-6 (5) with 34 winners. Alcaraz reaches 9th final of 2026 without dropping a set.",
            "pulse": "ERSTE BANK OPEN: CARLOS ALCARAZ SUBDUES ALEXANDER ZVEREV TO REACH VIENNA FINAL",
            "keywords": "ATP, Vienna, Erste Bank Open, Alcaraz, Zverev, semi-final, Wiener Stadthalle"
        },
        "f1": {
            "tagline": "Mexico City GP Qualifying: Kimi Antonelli captures dramatic pole position ahead of Leclerc and Verstappen.",
            "liveNow": "Qualifying at Hermanos Rodriguez: Antonelli (1:16.892) takes pole from Leclerc (+0.076s) and Verstappen (+0.142s). P9 on Sunday seals title.",
            "pulse": "MEXICO CITY GP QUALIFYING: KIMI ANTONELLI STORMS TO POLE POSITION ON BRINK OF TITLE",
            "keywords": "Formula 1, Mexico City GP, Antonelli, pole position, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open round 3: Austin Smotherman clings to 54-hole lead at 13-under; Raul Pereda chases at 12-under.",
            "liveNow": "Moving day at VidantaVallarta: Smotherman -13 (66-65-69=200) holds 1-shot lead over Mexico's Raul Pereda (-12, 201) and Rai (-11).",
            "pulse": "PGA TOUR MEXICO OPEN: SMOTHERMAN HOLDS 54-HOLE LEAD AT -13; PEREDA CHARGES TO -12",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, 54-hole lead"
        },
        "home": {
            "tonight": "Saturday desk",
            "tonightBlurb": "Arsenal and Liverpool battle to 2-2 thriller. Antonelli takes Mexico GP pole. Alcaraz beats Zverev to reach Vienna final.",
            "plTitle": "Premier League MW9: Arsenal and Liverpool battle to 2-2 draw in North London epic",
            "plBlurb": "Saka and Merino goals answered by Van Dijk and 81st-minute Salah equalizer; City take top spot after 1-0 win over Southampton.",
            "f1Title": "Mexico City GP: Kimi Antonelli captures pole position on title threshold",
            "f1Blurb": "Mercedes prodigy clocks 1:16.892 at 2,285 meters to edge Leclerc by 0.076s; needs only P9 on Sunday to become world champion."
        },
        "pg": {
            "pinFinal": "Premier League MW9: Arsenal 2-2 Liverpool at Emirates; City edge Southampton 1-0 to lead on 23 points.",
            "week1Closed": "College Football Week 10: Georgia 34, Florida 20. NFL Week 8 TNF: Packers 27, Panthers 17.",
            "week1Sub": "Carson Beck throws 3 TDs and Etienne rushes for 112 yds. Sunday: 6-0 Vikings put undefeated record on line.",
            "countdownTnf": "NFL Week 8 Sunday preview: 6-0 Vikings face Colts. Packers (6-2) handle Panthers 27-17 on TNF.",
            "barsPoints": "Bars show the gap to the leader. Antonelli starts from pole in Mexico with 365 pts; P9 on Sunday clinches world title.",
            "tableAfterMonday": "Premier League Matchweek 9: City take sole top spot with 23 pts (7-2-0) following Arsenal 2-2 Liverpool thriller.",
            "pinClub": "Select a club. City lead on 23, Arsenal follow on 22, Liverpool on 16. Fleetwood Town host Newcastle in Carabao QF.",
            "plFootnote": "PL MW9: Arsenal 2-2 Liverpool, Man City 1-0 Southampton. Carabao QF: Fleetwood vs Newcastle, Man City vs Brentford.",
            "majorsDone": "VidantaWorld Mexico Open Round 3: Smotherman leads at 13-under 200; local hero Pereda trails by one at 12-under 201."
        }
    },
    "fr": {
        "soccer": {
            "tagline": "Premier League J9 : Arsenal et Liverpool se neutralisent 2-2 a l'Emirates ; Man City seul leader.",
            "liveNow": "Premier League J9 : Arsenal 2-2 Liverpool (Saka 9', Merino 43' ; Van Dijk 18', Salah 81'). City 1-0 Southampton. City 23 pts, Arsenal 22, Liverpool 16.",
            "pulse": "PREMIER LEAGUE J9 : ARSENAL ET LIVERPOOL SE NEUTRALISENT DANS UN CHOC 2-2 A L'EMIRATES",
            "keywords": "Premier League, Arsenal, Liverpool, Emirates Stadium, Saka, Salah, Merino, Van Dijk, Man City"
        },
        "basketball": {
            "tagline": "NBA samedi : Victor Wembanyama eclabousse Phoenix de son talent avec 31 points et 6 contres (118-106).",
            "liveNow": "Score final a Phoenix : Spurs 118, Suns 106. Wembanyama 31 pts, 14 reb, 6 blk ; Chris Paul 12 passes ; Durant 28 pts. Spurs 3-1.",
            "pulse": "NBA SAMEDI : VICTOR WEMBANYAMA MONUMENTAL AVEC 31 POINTS ET 6 CONTRES A PHOENIX",
            "keywords": "NBA, Spurs, Suns, Wembanyama, Chris Paul, Kevin Durant, Phoenix, Footprint Center"
        },
        "football": {
            "tagline": "College Football Semaine 10 : Georgia surclasse Florida 34-20 a Jacksonville et reste invaincu (8-0).",
            "liveNow": "Fin de match a Jacksonville : Georgia 34, Florida 20. Beck 285 yds, 3 TD ; Etienne 112 yds, 1 TD. Dimanche : Vikings (6-0).",
            "pulse": "COLLEGE FOOTBALL : GEORGIA MATTE FLORIDA 34-20 ET PRESERVE SON BILAN PARFAIT (8-0)",
            "keywords": "College Football, Georgia Bulldogs, Florida Gators, Carson Beck, Trevor Etienne, Jacksonville, SEC"
        },
        "tennis": {
            "tagline": "Tournoi de Vienne demi-finales : Carlos Alcaraz surclasse Alexander Zverev 6-4, 7-6 et file en finale.",
            "liveNow": "Vienne ATP 500 DF : Alcaraz bat Zverev 6-4, 7-6 (5) avec 34 coups gagnants. Neuvieme finale de 2026 sans perdre un set.",
            "pulse": "TOURNOI DE VIENNE : CARLOS ALCARAZ DOMINE ALEXANDER ZVEREV POUR REJOINDRE LA FINALE",
            "keywords": "ATP, Vienne, Erste Bank Open, Alcaraz, Zverev, demi-finale, Wiener Stadthalle"
        },
        "f1": {
            "tagline": "GP du Mexique qualifications : Kimi Antonelli s'adjuge la pole position devant Leclerc et Verstappen.",
            "liveNow": "Qualifications a Mexico : Antonelli (1:16.892) en pole devant Leclerc (+0.076s) et Verstappen (+0.142s). P9 dimanche suffit.",
            "pulse": "GP DU MEXIQUE QUALIFICATIONS : KIMI ANTONELLI PREND LA POLE ET ROZE LE TITRE MONDIAL",
            "keywords": "Formule 1, GP du Mexique, Antonelli, pole position, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R3 : Austin Smotherman mene a -13 ; le Mexicain Raul Pereda a un coup (-12).",
            "liveNow": "Troisieme tour a VidantaVallarta : Smotherman -13 (66-65-69=200) mene d'un coup sur Raul Pereda (-12, 201) et Rai (-11).",
            "pulse": "PGA TOUR MEXICO OPEN : SMOTHERMAN EN TETE A -13 ; PEREDA POUSSE A -12 AVANT LA FINALE",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, 54 trous"
        },
        "home": {
            "tonight": "Desk du samedi",
            "tonightBlurb": "Arsenal et Liverpool font match nul 2-2. Antonelli en pole au Mexique. Alcaraz domine Zverev pour rejoindre la finale a Vienne.",
            "plTitle": "Premier League J9 : Arsenal et Liverpool se partagent les points 2-2 dans un sommet haletant",
            "plBlurb": "Saka et Merino ont repondu a Van Dijk et Salah ; Manchester City prend les commandes apres sa victoire 1-0 sur Southampton.",
            "f1Title": "GP du Mexique : Kimi Antonelli s'offre la pole position aux portes du sacre",
            "f1Blurb": "Le prodige Mercedes boucle son tour en 1:16.892 a 2 285 m et devance Leclerc ; P9 dimanche suffira pour etre sacre champion."
        },
        "pg": {
            "pinFinal": "Premier League J9 : Arsenal 2-2 Liverpool a l'Emirates ; Man City bat Southampton 1-0 et prend la tete avec 23 pts.",
            "week1Closed": "College Football S10 : Georgia 34, Florida 20. NFL Semaine 8 TNF : Packers 27, Panthers 17.",
            "week1Sub": "Carson Beck lance 3 TD et Etienne court pour 112 yds. Dimanche : les Vikings (6-0) defendent leur invincibilite.",
            "countdownTnf": "NFL Semaine 8 apercu dimanche : Vikings (6-0) face aux Colts. Les Packers (6-2) ont battu les Panthers 27-17.",
            "barsPoints": "Les barres montrent l'ecart. Antonelli part en pole avec 365 pts ; la 9e place dimanche lui offre le titre mondial.",
            "tableAfterMonday": "Premier League 9e journee : Manchester City seul leader avec 23 pts apres le nul 2-2 entre Arsenal et Liverpool.",
            "pinClub": "Choisissez un club. City mene avec 23 pts, Arsenal 22, Liverpool 16. Fleetwood accueille Newcastle en quarts.",
            "plFootnote": "PL J9 : Arsenal 2-2 Liverpool, Man City 1-0 Southampton. Quarts Carabao : Fleetwood vs Newcastle, Man City vs Brentford.",
            "majorsDone": "VidantaWorld Mexico Open R3 : Smotherman mene a -13 (200) ; le heros local Pereda est en embuscade a -12 (201)."
        }
    },
    "es": {
        "soccer": {
            "tagline": "Premier League J9: Arsenal y Liverpool empatan 2-2 en el Emirates; el Manchester City asume el liderato en solitario.",
            "liveNow": "Premier League J9: Arsenal 2-2 Liverpool (Saka 9', Merino 43'; Van Dijk 18', Salah 81'). City 1-0 Southampton. City 23 pts, Arsenal 22, Liverpool 16.",
            "pulse": "PREMIER LEAGUE J9: ARSENAL Y LIVERPOOL REPARTEN PUNTOS EN UN DUELO APASIONANTE EN EL EMIRATES",
            "keywords": "Premier League, Arsenal, Liverpool, Emirates Stadium, Saka, Salah, Merino, Van Dijk, Man City"
        },
        "basketball": {
            "tagline": "NBA sabado: Victor Wembanyama brilla con 31 puntos y 6 tapones en el triunfo de Spurs ante Suns 118-106.",
            "liveNow": "Final en Phoenix: Spurs 118, Suns 106. Wembanyama 31 pts, 14 reb, 6 blk; Chris Paul 12 ast; Durant 28 pts. Spurs 3-1.",
            "pulse": "NBA SABADO: VICTOR WEMBANYAMA IMPONE SU LEY CON 31 PUNTOS Y 6 TAPONES EN PHOENIX",
            "keywords": "NBA, Spurs, Suns, Wembanyama, Chris Paul, Kevin Durant, Phoenix, Footprint Center"
        },
        "football": {
            "tagline": "College Football Semana 10: Georgia derrota 34-20 a Florida en el Cocktail Party de Jacksonville y sigue 8-0.",
            "liveNow": "Final en Jacksonville: Georgia 34, Florida 20. Beck 285 yds, 3 TD; Etienne 112 yds, 1 TD. Domingo: Vikings (6-0).",
            "pulse": "COLLEGE FOOTBALL: GEORGIA DOBLEGA A FLORIDA 34-20 Y SE MANTIENE INVICTA (8-0)",
            "keywords": "College Football, Georgia Bulldogs, Florida Gators, Carson Beck, Trevor Etienne, Jacksonville, SEC"
        },
        "tennis": {
            "tagline": "ATP Viena semifinales: Carlos Alcaraz tumba a Alexander Zverev 6-4, 7-6 y clasifica a la gran final.",
            "liveNow": "Viena ATP 500 SF: Alcaraz vence a Zverev 6-4, 7-6 (5) con 34 tiros ganadores. Novena final de 2026 sin ceder sets.",
            "pulse": "ATP VIENA: CARLOS ALCARAZ SUPERA A ALEXANDER ZVEREV Y SE METE EN LA FINAL",
            "keywords": "ATP, Viena, Erste Bank Open, Alcaraz, Zverev, semifinal, Wiener Stadthalle"
        },
        "f1": {
            "tagline": "Clasificacion GP de Mexico: Kimi Antonelli logra una pole sensacional por delante de Leclerc y Verstappen.",
            "liveNow": "Clasificacion en Mexico: Antonelli (1:16.892) se lleva la pole ante Leclerc (+0.076s) y Verstappen (+0.142s). P9 el domingo da el titulo.",
            "pulse": "GP DE MEXICO CLASIFICACION: KIMI ANTONELLI VUELA A LA POLE Y ROZA LA CORONA MUNDIAL",
            "keywords": "Formula 1, GP de Mexico, Antonelli, pole position, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R3: Austin Smotherman lidera con -13; el mexicano Raul Pereda acecha a un golpe (-12).",
            "liveNow": "Tercera ronda en VidantaVallarta: Smotherman -13 (66-65-69=200) aventaja por uno a Raul Pereda (-12, 201) y Rai (-11).",
            "pulse": "PGA TOUR MEXICO OPEN: SMOTHERMAN MANDA CON -13; EL HEROE LOCAL PEREDA APRIETA A -12",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, 54 hoyos"
        },
        "home": {
            "tonight": "Edicion del sabado",
            "tonightBlurb": "Arsenal y Liverpool firman tablas 2-2. Antonelli logra la pole en Mexico. Alcaraz bate a Zverev para meterse en la final de Viena.",
            "plTitle": "Premier League J9: Arsenal y Liverpool empatan 2-2 en una batalla memorable en el Emirates",
            "plBlurb": "Goles de Saka y Merino contestados por Van Dijk y Salah; el City es nuevo lider solitario tras ganar 1-0 al Southampton.",
            "f1Title": "GP de Mexico: Kimi Antonelli se aduena de la pole y roza la gloria mundial",
            "f1Blurb": "El joven talento de Mercedes marca 1:16.892 en la altitud y supera a Leclerc; solo necesita un P9 el domingo para coronarse campeon."
        },
        "pg": {
            "pinFinal": "Premier League J9: Arsenal 2-2 Liverpool en el Emirates; City vence 1-0 a Southampton y lidera con 23 puntos.",
            "week1Closed": "College Football S10: Georgia 34, Florida 20. NFL Semana 8 TNF: Packers 27, Panthers 17.",
            "week1Sub": "Carson Beck lanza 3 TD y Etienne corre para 112 yds. Domingo: los invictos Vikings (6-0) reciben a los Colts.",
            "countdownTnf": "NFL Semana 8 previa domingo: Vikings (6-0) juegan ante Colts. Packers (6-2) superaron 27-17 a Panthers en TNF.",
            "barsPoints": "Las barras muestran la ventaja. Antonelli sale en pole con 365 pts; el 9° puesto el domingo le da el campeonato mundial.",
            "tableAfterMonday": "Premier League jornada 9: City lider solitario con 23 pts tras el 2-2 entre Arsenal y Liverpool.",
            "pinClub": "Elige un club. City lidera con 23, Arsenal 22, Liverpool 16. Fleetwood recibe a Newcastle en cuartos.",
            "plFootnote": "PL J9: Arsenal 2-2 Liverpool, Man City 1-0 Southampton. Cuartos Carabao: Fleetwood vs Newcastle, Man City vs Brentford.",
            "majorsDone": "VidantaWorld Mexico Open R3: Smotherman comanda con -13 (200); Raul Pereda a solo un golpe con -12 (201)."
        }
    },
    "de": {
        "soccer": {
            "tagline": "Premier League 9. Spieltag: Arsenal und Liverpool trennen sich 2:2; Man City erobert alleinige Tabellenfuehrung.",
            "liveNow": "Premier League: Arsenal 2:2 Liverpool (Saka 9., Merino 43.; Van Dijk 18., Salah 81.). City 1:0 Southampton. City 23 Pkt, Arsenal 22, Liverpool 16.",
            "pulse": "PREMIER LEAGUE 9. SPIELTAG: ARSENAL UND LIVERPOOL TEILEN SICH DIE PUNKTE BEIM 2:2 IM EMIRATES",
            "keywords": "Premier League, Arsenal, Liverpool, Emirates Stadium, Saka, Salah, Merino, Van Dijk, Man City"
        },
        "basketball": {
            "tagline": "NBA Samstag: Victor Wembanyama glaenzt mit 31 Punkten und 6 Blocks beim 118:106 der Spurs in Phoenix.",
            "liveNow": "Endstand in Phoenix: Spurs 118, Suns 106. Wembanyama 31 Pkt, 14 Reb, 6 Blk; Chris Paul 12 Ass; Durant 28 Pkt. Spurs 3-1.",
            "pulse": "NBA SAMSTAG: VICTOR WEMBANYAMA UEBERRAGT MIT 31 PUNKTEN UND 6 BLOCKS IN PHOENIX",
            "keywords": "NBA, Spurs, Suns, Wembanyama, Chris Paul, Kevin Durant, Phoenix, Footprint Center"
        },
        "football": {
            "tagline": "College Football Woche 10: Georgia schlaegt Florida 34:20 in Jacksonville und bleibt mit 8:0 unbesiegt.",
            "liveNow": "Endstand in Jacksonville: Georgia 34, Florida 20. Beck 285 Yds, 3 TD; Etienne 112 Yds, 1 TD. Sonntag: Vikings (6-0).",
            "pulse": "COLLEGE FOOTBALL: GEORGIA BEZWINGT FLORIDA 34:20 BEI DER COCKTAIL PARTY",
            "keywords": "College Football, Georgia Bulldogs, Florida Gators, Carson Beck, Trevor Etienne, Jacksonville, SEC"
        },
        "tennis": {
            "tagline": "Erste Bank Open Halbfinale: Carlos Alcaraz bezwingt Alexander Zverev 6:4, 7:6 und steht im Wiener Finale.",
            "liveNow": "Wien ATP 500 HF: Alcaraz schl. Zverev 6:4, 7:6 (5) mit 34 Winnern. Neuntes Saisonfinale 2026 ohne Satzverlust.",
            "pulse": "ERSTE BANK OPEN: CARLOS ALCARAZ SCHLAEGT ALEXANDER ZVEREV UND ZIEHT INS FINALE EIN",
            "keywords": "ATP, Wien, Erste Bank Open, Alcaraz, Zverev, Halbfinale, Wiener Stadthalle"
        },
        "f1": {
            "tagline": "Formel 1 Mexiko Qualifying: Kimi Antonelli sichert sich packende Pole Position vor Leclerc und Verstappen.",
            "liveNow": "Qualifying in Mexiko: Antonelli (1:16,892) holt Pole vor Leclerc (+0,076s) und Verstappen (+0,142s). P9 am Sonntag reicht zum WM-Titel.",
            "pulse": "MEXIKO GP QUALIFYING: KIMI ANTONELLI STUERMT ZUR POLE POSITION VOR LECLERC",
            "keywords": "Formel 1, Mexiko GP, Antonelli, Pole Position, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R3: Austin Smotherman behauptet Fuehrung bei -13; Lokalmatador Pereda folgt bei -12.",
            "liveNow": "3. Runde in VidantaVallarta: Smotherman -13 (66-65-69=200) liegt einen Schlag vor Mexikos Raul Pereda (-12, 201) und Rai (-11).",
            "pulse": "PGA TOUR MEXICO OPEN: SMOTHERMAN FUEHRT BEI -13; PEREDA BEGEISTERT BEI -12",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, 54 Loecher"
        },
        "home": {
            "tonight": "Samstagsausgabe",
            "tonightBlurb": "Arsenal und Liverpool trennen sich 2:2. Antonelli sichert sich Pole in Mexiko. Alcaraz bezwingt Zverev fuer das Finale in Wien.",
            "plTitle": "Premier League 9. Spieltag: Arsenal und Liverpool mit 2:2-Remis im mitreissenden Spitzenspiel",
            "plBlurb": "Saka und Merino trafen fuer Arsenal, van Dijk und Salah glichen aus; City fuehrt nach 1:0 ueber Southampton die Tabelle an.",
            "f1Title": "Mexiko GP: Kimi Antonelli faehrt auf Pole Position vor dem grossen WM-Showdown",
            "f1Blurb": "Mercedes-Star setzt 1:16,892 Min. in der Hoehenluft und distanziert Leclerc; P9 am Sonntag genuegt zur Weltmeisterschaft."
        },
        "pg": {
            "pinFinal": "Premier League 9. Spieltag: Arsenal 2:2 Liverpool; City schlaegt Southampton 1:0 und fuehrt mit 23 Punkten.",
            "week1Closed": "College Football W10: Georgia 34, Florida 20. NFL Woche 8 TNF: Packers 27, Panthers 17.",
            "week1Sub": "Carson Beck wirft 3 TDs und Etienne erlaeuft 112 Yds. Sonntag: Ungeschlagene Vikings (6-0) fordern Colts.",
            "countdownTnf": "NFL Woche 8 Sonntag-Ausblick: Vikings (6-0) gegen Colts. Packers (6-2) schlugen Panthers 27:17 am Donnerstag.",
            "barsPoints": "Balken zeigen Abstand. Antonelli startet von Pole mit 365 Pkt; Rang 9 am Sonntag sichert die Weltmeisterschaft.",
            "tableAfterMonday": "Premier League 9. Spieltag: City mit 23 Pkt alleiniger Spitzenreiter nach dem 2:2 zwischen Arsenal und Liverpool.",
            "pinClub": "Klub waehlen. City fuehrt mit 23, Arsenal 22, Liverpool 16. Fleetwood empfaengt Newcastle im Pokal.",
            "plFootnote": "PL 9. Spieltag: Arsenal 2:2 Liverpool, City 1:0 Southampton. Carabao Cup: Fleetwood vs Newcastle, City vs Brentford.",
            "majorsDone": "VidantaWorld Mexico Open R3: Smotherman fuehrt mit -13 (200); Lokalmatador Pereda liegt bei -12 (201)."
        }
    },
    "it": {
        "soccer": {
            "tagline": "Premier League 9ª giornata: Arsenal e Liverpool pareggiano 2-2; Manchester City solo al comando.",
            "liveNow": "Premier League: Arsenal 2-2 Liverpool (Saka 9', Merino 43'; Van Dijk 18', Salah 81'). City 1-0 Southampton. City 23 pt, Arsenal 22, Liverpool 16.",
            "pulse": "PREMIER LEAGUE: ARSENAL E LIVERPOOL SPETTACOLO ED EQUILIBRIO, FINISCE 2-2 ALL'EMIRATES",
            "keywords": "Premier League, Arsenal, Liverpool, Emirates Stadium, Saka, Salah, Merino, Van Dijk, Man City"
        },
        "basketball": {
            "tagline": "NBA sabato: Victor Wembanyama dominante con 31 punti e 6 stoppate nel successo Spurs a Phoenix (118-106).",
            "liveNow": "Finale a Phoenix: Spurs 118, Suns 106. Wembanyama 31 pt, 14 rim, 6 st; Chris Paul 12 ast; Durant 28 pt. Spurs 3-1.",
            "pulse": "NBA SABATO: VICTOR WEMBANYAMA SHOW CON 31 PUNTI E 6 STOPPATE A PHOENIX",
            "keywords": "NBA, Spurs, Suns, Wembanyama, Chris Paul, Kevin Durant, Phoenix, Footprint Center"
        },
        "football": {
            "tagline": "College Football Week 10: Georgia supera Florida 34-20 nel grande classico di Jacksonville e sale a 8-0.",
            "liveNow": "Finale a Jacksonville: Georgia 34, Florida 20. Beck 285 yd, 3 TD; Etienne 112 yd, 1 TD. Domenica: Vikings (6-0).",
            "pulse": "COLLEGE FOOTBALL: GEORGIA PIEGA FLORIDA 34-20 E RESTA IMBATTUTA A QUOTA 8-0",
            "keywords": "College Football, Georgia Bulldogs, Florida Gators, Carson Beck, Trevor Etienne, Jacksonville, SEC"
        },
        "tennis": {
            "tagline": "Erste Bank Open semifinali: Carlos Alcaraz batte Alexander Zverev 6-4, 7-6 e vola in finale a Vienna.",
            "liveNow": "Vienna ATP 500 SF: Alcaraz b. Zverev 6-4, 7-6 (5) con 34 vincenti. Nona finale del 2026 senza perdere un set.",
            "pulse": "ERSTE BANK OPEN: CARLOS ALCARAZ BATTE ALEXANDER ZVEREV E VOLA IN FINALE A VIENNA",
            "keywords": "ATP, Vienna, Erste Bank Open, Alcaraz, Zverev, semifinale, Wiener Stadthalle"
        },
        "f1": {
            "tagline": "Qualifiche GP Messico: Kimi Antonelli centra una splendida pole position davanti a Leclerc e Verstappen.",
            "liveNow": "Qualifiche in Messico: Antonelli (1:16.892) in pole su Leclerc (+0.076s) e Verstappen (+0.142s). Domenica basta il 9° posto.",
            "pulse": "GP MESSICO QUALIFICHE: KIMI ANTONELLI VOLA IN POLE POSITION A UN PASSO DAL TITOLO",
            "keywords": "Formula 1, GP Messico, Antonelli, pole position, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R3: Austin Smotherman guida a -13; il messicano Raul Pereda insegue a -12.",
            "liveNow": "Terzo giro a VidantaVallarta: Smotherman -13 (66-65-69=200) ha un colpo di vantaggio su Raul Pereda (-12, 201) e Rai (-11).",
            "pulse": "PGA TOUR MEXICO OPEN: SMOTHERMAN IN VETTA A -13; PEREDA ACCENDE IL PUBBLICO A -12",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, 54 buche"
        },
        "home": {
            "tonight": "Edizione del sabato",
            "tonightBlurb": "Arsenal e Liverpool pareggiano 2-2. Antonelli in pole in Messico. Alcaraz batte Zverev e conquista la finale a Vienna.",
            "plTitle": "Premier League 9ª giornata: Arsenal e Liverpool spettacolo puro, finisce 2-2 all'Emirates",
            "plBlurb": "I gol di Saka e Merino replicati da Van Dijk e Salah all'81'; il City vola in vetta solitaria dopo l'1-0 al Southampton.",
            "f1Title": "GP del Messico: Kimi Antonelli conquista la pole position verso il titolo iridato",
            "f1Blurb": "Il talento della Mercedes gira in 1:16.892 in quota battendo Leclerc; domenica basta un 9° posto per diventare campione del mondo."
        },
        "pg": {
            "pinFinal": "Premier League: Arsenal 2-2 Liverpool; City batte Southampton 1-0 ed e capolista solitaria con 23 punti.",
            "week1Closed": "College Football W10: Georgia 34, Florida 20. NFL Settimana 8 TNF: Packers 27, Panthers 17.",
            "week1Sub": "Carson Beck lancia 3 TD ed Etienne corre per 112 yd. Domenica: i Vikings imbattuti (6-0) affrontano i Colts.",
            "countdownTnf": "NFL Settimana 8 preview domenica: Vikings (6-0) contro Colts. Packers (6-2) hanno battuto i Panthers 27-17.",
            "barsPoints": "I grafici mostrano il distacco. Antonelli scatta in pole con 365 pt; il 9° posto domenica gli vale il mondiale.",
            "tableAfterMonday": "Premier League 9ª giornata: City solo al comando con 23 punti dopo il 2-2 tra Arsenal e Liverpool.",
            "pinClub": "Scegli un club. City in testa a 23, Arsenal 22, Liverpool 16. Fleetwood ospita Newcastle nei quarti.",
            "plFootnote": "PL 9ª giornata: Arsenal 2-2 Liverpool, Man City 1-0 Southampton. Coppa: Fleetwood vs Newcastle, Man City vs Brentford.",
            "majorsDone": "VidantaWorld Mexico Open R3: Smotherman guida con -13 (200); l'eroe di casa Pereda e a -12 (201)."
        }
    },
    "pl": {
        "soccer": {
            "tagline": "Premier League 9. kolejka: Arsenal i Liverpool zremisowaly 2:2; Manchester City samodzielnym liderem.",
            "liveNow": "Premier League: Arsenal 2:2 Liverpool (Saka 9', Merino 43'; Van Dijk 18', Salah 81'). City 1:0 Southampton. City 23 pkt, Arsenal 22, Liverpool 16.",
            "pulse": "PREMIER LEAGUE 9. KOLEJKA: ARSENAL I LIVERPOOL DZIELA SIE PUNKTAMI PO MECZU 2:2 NA EMIRATES",
            "keywords": "Premier League, Arsenal, Liverpool, Emirates Stadium, Saka, Salah, Merino, Van Dijk, Man City"
        },
        "basketball": {
            "tagline": "NBA sobota: Victor Wembanyama zachwyca 31 punktami i 6 blokami w wygranym 118:106 meczu Spurs z Suns.",
            "liveNow": "Koniec w Phoenix: Spurs 118, Suns 106. Wembanyama 31 pkt, 14 zb, 6 blk; Chris Paul 12 as; Durant 28 pkt. Spurs 3-1.",
            "pulse": "NBA SOBOTA: VICTOR WEMBANYAMA DOMINUJE Z 31 PUNKTAMI I 6 BLOKAMI W PHOENIX",
            "keywords": "NBA, Spurs, Suns, Wembanyama, Chris Paul, Kevin Durant, Phoenix, Footprint Center"
        },
        "football": {
            "tagline": "College Football Tydzien 10: Georgia wygrywa z Florida 34:20 w Jacksonville i zachowuje bilans 8-0.",
            "liveNow": "Koniec w Jacksonville: Georgia 34, Florida 20. Beck 285 jardow, 3 TD; Etienne 112 jardow, 1 TD. Niedziela: Vikings (6-0).",
            "pulse": "COLLEGE FOOTBALL: GEORGIA POKONUJE FLORIDE 34:20 I UTRZYMUJE STATUS NIEPOKONANEJ (8-0)",
            "keywords": "College Football, Georgia Bulldogs, Florida Gators, Carson Beck, Trevor Etienne, Jacksonville, SEC"
        },
        "tennis": {
            "tagline": "Erste Bank Open polfinaly: Carlos Alcaraz pokonuje Alexandra Zvereva 6:4, 7:6 i wchodzi do finalu w Wiedniu.",
            "liveNow": "Wieden ATP 500 PF: Alcaraz pok. Zvereva 6:4, 7:6 (5) z 34 uderzeniami konczacymi. Dziewiaty final w 2026 roku.",
            "pulse": "ERSTE BANK OPEN: CARLOS ALCARAZ POKONUJE ALEXANDRA ZVEREVA I MELDUJE SIE W FINALE",
            "keywords": "ATP, Wieden, Erste Bank Open, Alcaraz, Zverev, polfinal, Wiener Stadthalle"
        },
        "f1": {
            "tagline": "Kwalifikacje GP Meksyku: Kimi Antonelli zdobywa pole position przed Leclerkiem i Verstappenem.",
            "liveNow": "Kwalifikacje w Meksyku: Antonelli (1:16.892) na pole position przed Leclerkiem (+0,076 s) i Verstappenem (+0,142 s).",
            "pulse": "KWALIFIKACJE GP MEKSYKU: KIMI ANTONELLI ZDOBYWA POLE POSITION I BLISKO MISTRZOSTWA",
            "keywords": "Formula 1, GP Meksyku, Antonelli, pole position, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R3: Austin Smotherman prowadzi z -13; meksykanski bohater Raul Pereda traci punkt (-12).",
            "liveNow": "Runda 3 w VidantaVallarta: Smotherman -13 (66-65-69=200) uderzenie przed Paulem Pereda (-12, 201) i Raiem (-11).",
            "pulse": "PGA TOUR MEXICO OPEN: SMOTHERMAN NA CZELE Z -13; PEREDA ZACHWYCA KIBICOW Z -12",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, 54 dolki"
        },
        "home": {
            "tonight": "Sobotnie wydanie",
            "tonightBlurb": "Arsenal i Liverpool na remis 2:2. Antonelli z pole position w Meksyku. Alcaraz pokonuje Zvereva i zagra w finale w Wiedniu.",
            "plTitle": "Premier League 9. kolejka: Arsenal i Liverpool zremisowaly 2:2 w elektryzujacym hicie",
            "plBlurb": "Gole Saki i Merino wyrownane przez Van Dijka i Salaha w 81. minucie; Man City liderem po 1:0 z Southampton.",
            "f1Title": "GP Meksyku: Kimi Antonelli zdobywa pole position i jest o krok od mistrzostwa swiata",
            "f1Blurb": "Mlodzieniec Mercedesa uzyskal 1:16.892 na duzej wysokosci; 9. miejsce w niedziele wystarczy do tytulu mistrza swiata."
        },
        "pg": {
            "pinFinal": "Premier League 9. kolejka: Arsenal 2:2 Liverpool; City pokonuje Southampton 1:0 i prowadzi z 23 punktami.",
            "week1Closed": "College Football T10: Georgia 34, Florida 20. NFL Tydzien 8 TNF: Packers 27, Panthers 17.",
            "week1Sub": "Carson Beck rzucil 3 TD, a Etienne wybiegal 112 jardow. Niedziela: niepokonani Vikings (6-0) podejma Colts.",
            "countdownTnf": "NFL Tydzien 8 zapowiedz niedzieli: Vikings (6-0) graja z Colts. Packers (6-2) pokonali Panthers 27:17 w TNF.",
            "barsPoints": "Wykresy pokazuja przewage. Antonelli rusza z pole position z 365 pkt; 9. miejsce w niedziele daje tytul.",
            "tableAfterMonday": "Premier League 9. kolejka: City samodzielnym liderem z 23 pkt po remisie 2:2 pomiedzy Arsenalem a Liverpoolem.",
            "pinClub": "Wybierz klub. City na czele z 23 pkt, Arsenal 22, Liverpool 16. Fleetwood podejmie Newcastle w cwiercfinale.",
            "plFootnote": "PL 9. kolejka: Arsenal 2:2 Liverpool, Man City 1:0 Southampton. Carabao: Fleetwood vs Newcastle, Man City vs Brentford.",
            "majorsDone": "VidantaWorld Mexico Open R3: Smotherman prowadzi z -13 (200); miejscowy bohater Pereda ma -12 (201)."
        }
    },
    "zh": {
        "soccer": {
            "tagline": "英超第9轮焦点战：阿森纳2-2战平利物浦；曼城1-0胜南安普顿独占榜首。",
            "liveNow": "英超第9轮：阿森纳2-2利物浦（萨卡9'，梅里诺43'；范戴克18'，萨拉赫81'）。曼城1-0南安普顿。曼城23分，阿森纳22分，利物浦16分。",
            "pulse": "英超第9轮：阿森纳利物浦酋长球场2-2战平，强强对话精彩绝伦",
            "keywords": "英超, 阿森纳, 利物浦, 酋长球场, 萨卡, 萨拉赫, 梅里诺, 范戴克, 曼城"
        },
        "basketball": {
            "tagline": "NBA周六焦点战：文班亚马爆砍31分14板6帽统治攻防，马刺客场118-106力克太阳。",
            "liveNow": "菲尼克斯终场：马刺118-106太阳。文班亚马31分14板6帽3断；保罗12助攻0失误；杜兰特28分。马刺3胜1负。",
            "pulse": "NBA周六：文班亚马31分14篮板6盖帽攻防一体带队客场击退太阳",
            "keywords": "NBA, 马刺, 太阳, 文班亚马, 保罗, 杜兰特, 菲尼克斯"
        },
        "football": {
            "tagline": "NCAA橄榄球第10周：佐治亚下半场逆转佛罗里达34-20保持8胜0负不败纪录。",
            "liveNow": "杰克逊维尔终场：佐治亚34-20佛罗里达。贝克285码3达阵；埃蒂安112码1达阵。周日：6胜0负维京人出战。",
            "pulse": "大学橄榄球：佐治亚34-20力克佛罗里达豪取八连胜",
            "keywords": "大学橄榄球, 佐治亚斗牛犬, 佛罗里达短吻鳄, 贝克, 埃蒂安, SEC"
        },
        "tennis": {
            "tagline": "维也纳ATP500半决赛：阿尔卡拉斯6-4、7-6力克兹维列夫晋级争冠战。",
            "liveNow": "维也纳站半决赛：阿尔卡拉斯6-4、7-6(5)胜兹维列夫，狂轰34个制胜分，一盘未失晋级今年第9个决赛。",
            "pulse": "维也纳ATP500：阿尔卡拉斯击败兹维列夫挺进男单决赛",
            "keywords": "ATP, 维也纳, 阿尔卡拉斯, 兹维列夫, 半决赛"
        },
        "f1": {
            "tagline": "F1墨西哥大奖赛排位赛：安东内利跑出1分16秒892力夺杆位，加冕世界冠军在即。",
            "liveNow": "墨西哥城排位赛：安东内利（1:16.892）击败勒克莱尔（+0.076秒）和维斯塔潘（+0.142秒）夺杆位。周日前九即夺冠。",
            "pulse": "F1墨西哥大奖赛排位赛：超新星安东内利力压勒克莱尔勇夺杆位",
            "keywords": "F1, 墨西哥大奖赛, 安东内利, 杆位, 勒克莱尔, 维斯塔潘"
        },
        "golf": {
            "tagline": "美巡赛墨西哥公开赛第三轮：斯莫瑟曼-13杆保住榜首；本土名将佩雷达67杆落后一杆紧追。",
            "liveNow": "巴亚尔塔港移动日：斯莫瑟曼-13（66-65-69=200）领先墨西哥名将佩雷达（-12，201）一杆，拉伊-11名列第三。",
            "pulse": "美巡赛墨西哥公开赛：斯莫瑟曼-13杆领跑，本土英雄佩雷达-12杆紧追",
            "keywords": "美巡赛, 墨西哥公开赛, 斯莫瑟曼, 佩雷达, 拉伊, 移动日"
        },
        "home": {
            "tonight": "周六速递",
            "tonightBlurb": "阿森纳与利物浦2-2战平。安东内利墨西哥夺杆位。阿尔卡拉斯击溃兹维列夫进维也纳决赛。",
            "plTitle": "英超第9轮：阿森纳2-2利物浦，强强对话平分秋色",
            "plBlurb": "萨卡梅里诺建功，范戴克与萨拉赫进球扳平；曼城1-0小胜南安普顿独占榜首。",
            "f1Title": "F1墨西哥站：安东内利夺杆位，加冕总冠军近在咫尺",
            "f1Blurb": "梅奔新星在海拔2285米跑出1分16秒892险胜勒克莱尔；周日只需第9名即可提前加冕年度总冠军。"
        },
        "pg": {
            "pinFinal": "英超第9轮：阿森纳2-2利物浦；曼城1-0胜南安普顿积23分独占榜首。",
            "week1Closed": "NCAA橄榄球第10周：佐治亚34-20佛罗里达。NFL第8周TNF：包装工27-17黑豹。",
            "week1Sub": "贝克送出3次达阵，埃蒂安冲球112码。周日：6胜0负维京人迎战小马迎考验。",
            "countdownTnf": "NFL周日前瞻：6胜0负维京人对阵小马。包装工TNF以27-17拿下黑豹战绩升至6-2。",
            "barsPoints": "积分榜差距图。安东内利365分杆位发车；周日正赛进入前九即可确保世界冠军。",
            "tableAfterMonday": "英超积分榜：阿森纳利物浦2-2战平后，曼城积23分独自领跑英超积分榜。",
            "pinClub": "选择俱乐部。曼城23分，阿森纳22分，利物浦16分。弗利特伍德联赛杯抽中纽卡。",
            "plFootnote": "英超第9轮：阿森纳2-2利物浦，曼城1-0南安普顿。联赛杯八强：弗利特伍德对纽卡，曼城对小蜜蜂。",
            "majorsDone": "墨西哥公开赛第三轮：斯莫瑟曼-13（200）领先；本土英雄佩雷达-12（201）一杆之差逼近。"
        }
    },
    "ja": {
        "soccer": {
            "tagline": "プレミアリーグ第9節：アーセナルとリヴァプールがエミレーツで激闘2-2；マンCが単独首位浮上。",
            "liveNow": "プレミアリーグ第9節：アーセナル 2-2 リヴァプール（サカ 9'、メリーノ 43'；ファン・ダイク 18'、サラー 81'）。マンC 1-0 サウサンプトン。マンC 23点、アーセナル 22点、リヴァプール 16点。",
            "pulse": "プレミアリーグ第9節：アーセナルとリヴァプールが意地をぶつけ合い2-2のドロー",
            "keywords": "プレミアリーグ, アーセナル, リヴァプール, エミレーツ, サカ, サラー, マンC"
        },
        "basketball": {
            "tagline": "NBA土曜：ウェンバンヤマが31得点14リバウンド6ブロックと大爆発、スパーズがサンズを118-106で撃破。",
            "liveNow": "フェニックス公式戦：スパーズ 118-106 サンズ。ウェンバンヤマ 31得点14リバウンド6ブロック；ポール 12アシスト0失策；デュラント 28得点。スパーズ 3勝1敗。",
            "pulse": "NBA土曜：ウェンバンヤマが31得点6ブロックの猛攻で敵地フェニックスを制圧",
            "keywords": "NBA, スパーズ, サンズ, ウェンバンヤマ, クリス・ポール, デュラント"
        },
        "football": {
            "tagline": "カレッジフットボール第10週：全米2位ジョージア大が後半逆転でフロリダ大を34-20で下し開幕8連勝。",
            "liveNow": "ジャクソンビル決戦：ジョージア大 34-20 フロリダ大。ベック 285ヤード 3TD；エティエンヌ 112ヤード 1TD。日曜は無敗バイキングス（6-0）。",
            "pulse": "カレッジフットボール：ジョージア大が宿敵フロリダ大を34-20で撃破し無敗キープ",
            "keywords": "カレッジフットボール, ジョージア大, フロリダ大, ベック, エティエンヌ, SEC"
        },
        "tennis": {
            "tagline": "エルステ・バンク・オープン準決勝：アルカラスがズベレフを6-4、7-6で下しウィーン決勝進出。",
            "liveNow": "ウィーンATP500準決勝：アルカラスが34本のウィナーを放ちズベレフに6-4、7-6(5)で勝利。セットを失わず今季9度目の決勝へ。",
            "pulse": "エルステ・バンク・オープン：アルカラスがズベレフとの大激戦を制しウィーン決勝へ",
            "keywords": "ATP, ウィーン, アルカラス, ズベレフ, 準決勝"
        },
        "f1": {
            "tagline": "F1メキシコGP予選：アントネッリが1分16秒892で激戦を制しポールポジション獲得。",
            "liveNow": "メキシコシティ予選：アントネッリ（1分16秒892）がルクレール（+0.076秒）とフェルスタッペン（+0.142秒）を抑えPP。日曜9位以上で年間王者。",
            "pulse": "F1メキシコGP予選：キミ・アントネッリが圧巻のタイムでポールポジション獲得",
            "keywords": "F1, メキシコGP, アントネッリ, ポールポジション, ルクレール, フェルスタッペン"
        },
        "golf": {
            "tagline": "メキシコ・オープン第3日：スモーザーマンが通算13アンダーで首位死守；地元ペレダが1打差追走。",
            "liveNow": "ヴィダンタ・バジャルタ第3ラウンド：スモーザーマン -13（66-65-69=200）が地元ペレダ（-12、201）を1打差でリード。",
            "pulse": "PGAツアー メキシコ・オープン：スモーザーマンが13アンダー首位、地元ペレダが12アンダー猛追",
            "keywords": "PGAツアー, メキシコ・オープン, スモーザーマン, ペレダ, ライ, 第3日"
        },
        "home": {
            "tonight": "土曜版デスク",
            "tonightBlurb": "アーセナルとリヴァプールが2-2激闘。アントネッリがメキシコでPP獲得。アルカラスがズベレフ破りウィーン決勝へ。",
            "plTitle": "プレミアリーグ第9節：アーセナルとリヴァプールが2-2で引き分け、名勝負を演じる",
            "plBlurb": "サカとメリーノの得点にファン・ダイクとサラーが応酬；サウサンプトンを下したマンチェスター・Cが単独首位へ。",
            "f1Title": "F1メキシコGP：キミ・アントネッリが予選ポール獲得、王座戴冠へ前進",
            "f1Blurb": "メルセデスの若き天才が標高2285mで最速タイムを記録；日曜決勝で9位以内に入れば年間チャンピオン確定。"
        },
        "pg": {
            "pinFinal": "プレミアリーグ第9節：アーセナル 2-2 リヴァプール；マンCが1-0でサウサンプトンを下し勝ち点23で首位浮上。",
            "week1Closed": "カレッジフットボール第10週：ジョージア大 34-20 フロリダ大。NFL TNF：パッカーズ 27-17 パンサーズ。",
            "week1Sub": "カーソン・ベックが3TDパス、エティエンヌが112ヤード。日曜は無敗バイキングス（6-0）が登場。",
            "countdownTnf": "NFL日曜プレビュー：6勝0敗のバイキングスがコルツと対戦。パッカーズは木曜に27-17で快勝。",
            "barsPoints": "ポイント差グラフ。アントネッリが365点でポール発進；日曜決勝で9位以内ならタイトル獲得。",
            "tableAfterMonday": "プレミアリーグ順位表：アーセナル対リヴァプールの2-2ドローにより、マンCが勝ち点23で単独首位。",
            "pinClub": "クラブを選択。マンCが23点、アーセナル22点、リヴァプール16点。フリートウッドは杯準々決勝でニューカッスル戦。",
            "plFootnote": "PL第9節：アーセナル 2-2 リヴァプール、マンC 1-0 サウサンプトン。杯8強：フリートウッド対ニューカッスル。",
            "majorsDone": "メキシコ・オープン第3日：スモーザーマンが通算-13（200）で首位；地元ペレダが1打差の-12（201）で追走。"
        }
    },
    "ko": {
        "soccer": {
            "tagline": "프리미어리그 9R: 아스널과 리버풀 2-2 명승부 무승부; 맨시티 단독 선두 도약.",
            "liveNow": "프리미어리그 9R: 아스널 2-2 리버풀 (사카 9', 메리노 43'; 반다이크 18', 살라 81'). 맨시티 1-0 사우샘프턴. 맨시티 23점, 아스널 22점, 리버풀 16점.",
            "pulse": "프리미어리그 9R: 아스널과 리버풀 에미레이츠서 2-2 무승부 명승부 연출",
            "keywords": "프리미어리그, 아스널, 리버풀, 에미레이츠, 사카, 살라, 맨시티"
        },
        "basketball": {
            "tagline": "NBA 토요일: 웸반야마 31점 14리바운드 6블록 폭발, 스퍼스 피닉스 118-106 격파.",
            "liveNow": "피닉스 경기 결과: 스퍼스 118, 선즈 106. 웸반야마 31점 14리바운드 6블록; 크리스 폴 12어시스트; 듀란트 28점. 스퍼스 3승 1패.",
            "pulse": "NBA 토요일: 빅터 웸반야마 31점 14리바운드 6블록 괴물 활약으로 피닉스 격파",
            "keywords": "NBA, 스퍼스, 선즈, 웸반야마, 크리스 폴, 케빈 듀란트"
        },
        "football": {
            "tagline": "대학 미식축구 10주차: 전미 2위 조지아대, 잭슨빌서 플로리다대 34-20 꺾고 8연승 질주.",
            "liveNow": "잭슨빌 경기 결과: 조지아대 34, 플로리다대 20. 벡 285야드 3TD; 에티엔 112야드 1TD. 일요일: 바이킹스(6-0).",
            "pulse": "대학 미식축구: 조지아대, 플로리다대 34-20 완파하고 무패 행진 지속",
            "keywords": "대학 미식축구, 조지아대, 플로리다대, 카슨 벡, 트레버 에티엔, SEC"
        },
        "tennis": {
            "tagline": "빈 오픈 4강: 알카라스, 즈베레프 6-4 7-6 제압하고 결승 진출.",
            "liveNow": "빈 ATP 500 준결승: 알카라스, 34개 위너 폭발하며 즈베레프에 6-4, 7-6(5) 승리. 무실세트로 시즌 9번째 결승행.",
            "pulse": "빈 오픈 테니스: 카를로스 알카라스, 즈베레프 꺾고 빈 결승행 확정",
            "keywords": "ATP, 빈 오픈, 알카라스, 즈베레프, 준결승"
        },
        "f1": {
            "tagline": "F1 멕시코 GP 예선: 키미 안토넬리 1분16초892로 폴포지션 획득, 월드 챔피언 눈앞.",
            "liveNow": "멕시코시티 예선: 안토넬리(1:16.892) 르클레르(+0.076초)와 페르스타펜(+0.142초) 제치고 1위. 일요일 본선 9위 이상이면 우승.",
            "pulse": "F1 멕시코 GP 예선: 키미 안토넬리 드라마틱한 폴포지션으로 챔피언 등극 초읽기",
            "keywords": "F1, 멕시코 GP, 안토넬리, 폴포지션, 르클레르, 페르스타펜"
        },
        "golf": {
            "tagline": "멕시코 오픈 3R: 스모더먼 13언더파 단독 선두; 홈스타 페레다 12언더파 1타 차 맹추격.",
            "liveNow": "바야르타 3라운드: 스모더먼 -13(66-65-69=200)이 멕시코 라울 페레다(-12, 201)에 1타 앞선 단독 선두.",
            "pulse": "PGA 투어 멕시코 오픈: 스모더먼 13언더파 선두, 홈팬 열광시킨 페레다 12언더파 추격",
            "keywords": "PGA 투어, 멕시코 오픈, 스모더먼, 페레다, 라이, 3라운드"
        },
        "home": {
            "tonight": "토요일 데스크",
            "tonightBlurb": "아스널과 리버풀 2-2 무승부. 안토넬리 멕시코 폴포지션 획득. 알카라스 즈베레프 꺾고 빈 결승 진출.",
            "plTitle": "프리미어리그 9R: 아스널과 리버풀, 2-2 명승부 끝 승점 1점씩 분할",
            "plBlurb": "사카와 메리노 득점에 반다이크와 살라의 81분 동점골로 응수; 맨시티 사우샘프턴전 1-0 승리로 단독 선두.",
            "f1Title": "F1 멕시코 GP: 키미 안토넬리 폴포지션 차지하며 세계 챔피언 등극 직전",
            "f1Blurb": "메르세데스 신예가 2285m 고도에서 1분16초892 기록; 일요일 본선 9위 이상만 기록하면 F1 최연소 챔피언 등극."
        },
        "pg": {
            "pinFinal": "프리미어리그 9R: 아스널 2-2 리버풀; 맨시티 사우샘프턴 1-0 꺾고 승점 23점 단독 1위.",
            "week1Closed": "대학 미식축구 10주차: 조지아대 34, 플로리다대 20. NFL 8주차 TNF: 패커스 27, 팬서스 17.",
            "week1Sub": "카슨 벡 3TD 및 에티엔 112야드 러싱. 일요일: 6승 0패 무패 행진 바이킹스 출격.",
            "countdownTnf": "NFL 일요일 프리뷰: 6승 0패 바이킹스 대 콜츠. 패커스는 목요일 밤 팬서스를 27-17로 격파.",
            "barsPoints": "점수 차이 차트. 안토넬리 365점으로 폴포지션 출발; 일요일 9위 이상이면 세계 챔피언 확정.",
            "tableAfterMonday": "프리미어리그 순위표: 아스널-리버풀 2-2 무승부 이후 맨시티가 승점 23점으로 단독 선두 질주.",
            "pinClub": "클럽 선택. 맨시티 23점, 아스널 22점, 리버풀 16점. 플리트우드는 카라바오컵 8강서 뉴캐슬과 격돌.",
            "plFootnote": "PL 9R: 아스널 2-2 리버풀, 맨시티 1-0 사우샘프턴. 리그컵: 플리트우드 vs 뉴캐슬, 맨시티 vs 브렌트퍼드.",
            "majorsDone": "멕시코 오픈 3R: 스모더먼 -13(200) 선두; 홈 팬들의 영웅 페레다가 -12(201)로 1타 차 추격."
        }
    },
    "ar": {
        "soccer": {
            "tagline": "الدوري الإنجليزي الجولة 9: أرسنال وليفربول يتعادلان 2-2 في قمة ملعب الإمارات؛ وسيتي ينفرد بالصدارة.",
            "liveNow": "الدوري الإنجليزي: أرسنال 2-2 ليفربول (ساكا 9'، ميرينو 43'؛ فان دايك 18'، صلاح 81'). سيتي 1-0 ساوثهامبتون. سيتي 23 نقطة، أرسنال 22، ليفربول 16.",
            "pulse": "الدوري الإنجليزي الجولة 9: أرسنال وليفربول يقتسمان النقاط في قمة نارية انتهت 2-2",
            "keywords": "الدوري الإنجليزي, أرسنال, ليفربول, ملعب الإمارات, ساكا, صلاح, ميرينو, فان دايك, مانشستر سيتي"
        },
        "basketball": {
            "tagline": "دوري السلة الأمريكي السبت: فيكتور ويمبانياما يبدع بـ 31 نقطة و6 تصديات وسبيرز يهزم صنز 118-106.",
            "liveNow": "النتيجة النهائية في فينيكس: سبيرز 118، صنز 106. ويمبانياما 31 نقطة و14 متابعة و6 تصديات؛ بول 12 تمريرة؛ دورانت 28 نقطة. سبيرز 3-1.",
            "pulse": "دوري السلة الأمريكي السبت: ويمبانياما يتألق بـ 31 نقطة و6 تصديات ويقود سبيرز للفوز في فينيكس",
            "keywords": "دوري السلة الأمريكي, سبيرز, صنز, ويمبانياما, كريس بول, كيفن دورانت"
        },
        "football": {
            "tagline": "كرة القدم الأمريكية الجامعية الأسبوع 10: جورجيا تتفوق على فلوريدا 34-20 في جاكسونفيل وتبلغ 8-0.",
            "liveNow": "النهائي في جاكسونفيل: جورجيا 34، فلوريدا 20. بيك 285 ياردة و3 تمريرات هبوط؛ إيتيين 112 ياردة وهبوط. الأحد: فايكنغز (6-0).",
            "pulse": "كرة القدم الأمريكية الجامعية: جورجيا تهزم فلوريدا 34-20 وتحافظ على سجلها المثالي",
            "keywords": "كرة القدم الجامعية, جورجيا, فلوريدا, كارسون بيك, تريفور إيتيين, جاكسونفيل"
        },
        "tennis": {
            "tagline": "بطولة فيينا للتنس نصف النهائي: كارلوس ألكاراز يهزم ألكسندر زفيريف 6-4 و7-6 ويبلغ النهائي.",
            "liveNow": "نصف نهائي فيينا: ألكاراز يهزم زفيريف 6-4 و7-6 (5) مع 34 ضربة قاضية. النهائي التاسع في 2026 دون خسارة أي مجموعة.",
            "pulse": "بطولة فيينا المفتوحة: ألكاراز يتفوق على زفيريف ويتأهل للمباراة النهائية",
            "keywords": "تنس, فيينا, ألكاراز, زفيريف, نصف النهائي"
        },
        "f1": {
            "tagline": "تجارب جائزة المكسيك الكبرى: كيمي أنتونيللي يخطف مركز الانطلاق الأول متقدما على لوكلير وفرستابن.",
            "liveNow": "تأهيل المكسيك: أنتونيللي (1:16.892) في الصدارة أمام لوكلير (+0.076 ث) وفرستابن (+0.142 ث). المركز التاسع الأحد يحسم اللقب.",
            "pulse": "جائزة المكسيك الكبرى: أنتونيللي ينطلق أولا ويقترب خطوة حاسمة من لقب بطولة العالم",
            "keywords": "فورمولا 1, جائزة المكسيك الكبرى, أنتونيللي, مركز الانطلاق الأول, لوكلير, فرستابن"
        },
        "golf": {
            "tagline": "بطولة المكسيك المفتوحة الجولة 3: أوستن سموذر مان يتصدر بـ 13 تحت المعدل وبيريدا يطارده بـ -12.",
            "liveNow": "الجولة 3 في فيدانتا فايارتا: سموذر مان -13 (66-65-69=200) متقدما بضربة على راؤول بيريدا (-12، 201) وراي (-11).",
            "pulse": "جولة بي جي إيه: سموذر مان يحافظ على الصدارة بـ -13 وبيريدا يشعل حماس الجماهير بـ -12",
            "keywords": "جولف, بطولة المكسيك المفتوحة, سموذر مان, بيريدا, راي, الجولة الثالثة"
        },
        "home": {
            "tonight": "موجز السبت",
            "tonightBlurb": "أرسنال وليفربول يتعادلان 2-2. أنتونيللي ينطلق أولا في المكسيك. ألكاراز يهزم زفيريف ليبلغ نهائي فيينا.",
            "plTitle": "الدوري الإنجليزي الجولة 9: أرسنال وليفربول يتعادلان 2-2 في قمة مثيرة بملعب الإمارات",
            "plBlurb": "هدفا ساكا وميرينو قابلهما هدفا فان دايك وصلاح في الدقيقة 81؛ وسيتي ينفرد بالصدارة بعد فوزه 1-0 على ساوثهامبتون.",
            "f1Title": "جائزة المكسيك الكبرى: كيمي أنتونيللي يحصد مركز الانطلاق الأول ويقترب من التتويج",
            "f1Blurb": "سائق مرسيدس يسجل 1:16.892 على ارتفاع 2285 مترا متفوقا على لوكلير؛ ويكفيه المركز التاسع يوم الأحد ليصبح أصغر بطل عالم."
        },
        "pg": {
            "pinFinal": "الدوري الإنجليزي: أرسنال 2-2 ليفربول في الإمارات؛ سيتي يهزم ساوثهامبتون 1-0 ويتصدر بـ 23 نقطة.",
            "week1Closed": "كرة القدم الجامعية الأسبوع 10: جورجيا 34، فلوريدا 20. دوري NFL الأسبوع 8: باكرز 27، بانثرز 17.",
            "week1Sub": "كارسون بيك يسجل 3 تمريرات هبوط وإيتيين يركض لمسافة 112 ياردة. الأحد: فايكنغز (6-0).",
            "countdownTnf": "دوري NFL نظرة على مباريات الأحد: فايكنغز (6-0) ضد كولتس. باكرز فاز 27-17 على بانثرز يوم الخميس.",
            "barsPoints": "الأشرطة توضح الفارق. أنتونيللي ينطلق أولا ولديه 365 نقطة؛ المركز التاسع الأحد يمنحه اللقب رسميا.",
            "tableAfterMonday": "ترتيب الدوري الإنجليزي الممتاز: سيتي ينفرد بالصدارة بـ 23 نقطة بعد تعادل أرسنال وليفربول 2-2.",
            "pinClub": "اختر ناديا. سيتي يتصدر بـ 23، أرسنال 22، ليفربول 16. فليتوود يستضيف نيوكاسل في ربع النهائي.",
            "plFootnote": "الدوري الإنجليزي: أرسنال 2-2 ليفربول، مان سيتي 1-0 ساوثهامبتون. كأس الرابطة: فليتوود ضد نيوكاسل.",
            "majorsDone": "بطولة المكسيك المفتوحة الجولة 3: سموذر مان يتصدر بـ 13 تحت المعدل (200)؛ وبيريدا يطارده بـ -12 (201)."
        }
    }
}

# 1. Update frontend/src/i18n/playground.ts
pg_file = os.path.join(os.path.dirname(__file__), "../../frontend/src/i18n/playground.ts")
with open(pg_file, "r", encoding="utf-8") as f:
    pg_content = f.read()

for lang in ["en", "fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
    pg_data = DATA[lang]["pg"]
    pattern = rf'("{lang}":\s*\{{)([\s\S]*?)(\n  \}},|\n  \}})'
    match = re.search(pattern, pg_content)
    if match:
        block = match.group(2)
        for k, text in pg_data.items():
            field_pattern = rf'("{k}":\s*)"(.*?)"'
            clean_text = text.replace('"', '\\"')
            block = re.sub(field_pattern, rf'\1"{clean_text}"', block)
        pg_content = pg_content[:match.start(2)] + block + pg_content[match.end(2):]
    else:
        print(f"Warning: lang block for {lang} not matched in playground.ts")

with open(pg_file, "w", encoding="utf-8") as f:
    f.write(pg_content)
print("Updated frontend/src/i18n/playground.ts")

# Helper to update messages
def update_messages_dict(content, lang, prefix=""):
    data = DATA[lang]
    # update sports
    for sport_name in ["football", "tennis", "f1", "soccer", "basketball", "golf"]:
        fields = data[sport_name]
        idx = content.find(f"{sport_name}: {{", prefix) if prefix else content.find(f"{sport_name}: {{")
        if idx != -1:
            end_idx = content.find("},", idx)
            sport_block = content[idx:end_idx]
            for k, text in fields.items():
                clean_text = text.replace('"', '\\"')
                field_pattern = rf'({k}:\s*)"(.*?)"'
                sport_block = re.sub(field_pattern, rf'\1"{clean_text}"', sport_block)
            content = content[:idx] + sport_block + content[end_idx:]
    # update home
    home_idx = content.find("home: {", prefix) if prefix else content.find("home: {")
    if home_idx != -1:
        end_idx = content.find("},\n};", home_idx)
        if end_idx == -1:
            end_idx = content.find("},\n  footer:", home_idx)
        if end_idx == -1:
            end_idx = content.find("},\n}", home_idx)
        home_block = content[home_idx:end_idx]
        for k, text in data["home"].items():
            clean_text = text.replace('"', '\\"')
            field_pattern = rf'({k}:\s*)"(.*?)"'
            home_block = re.sub(field_pattern, rf'\1"{clean_text}"', home_block)
        content = content[:home_idx] + home_block + content[end_idx:]
    return content

# 2. Update frontend/src/i18n/messages.ts (en and fr)
msg_file = os.path.join(os.path.dirname(__file__), "../../frontend/src/i18n/messages.ts")
with open(msg_file, "r", encoding="utf-8") as f:
    msg_content = f.read()

fr_pos = msg_content.find("export const fr: Messages = {")
en_part = msg_content[:fr_pos]
fr_part = msg_content[fr_pos:]

en_part = update_messages_dict(en_part, "en")
fr_part = update_messages_dict(fr_part, "fr")

msg_content = en_part + fr_part
with open(msg_file, "w", encoding="utf-8") as f:
    f.write(msg_content)
print("Updated frontend/src/i18n/messages.ts")

# 3. Update all messages-*.ts
for lang in ["es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
    lang_file = os.path.join(os.path.dirname(__file__), f"../../frontend/src/i18n/messages-{lang}.ts")
    with open(lang_file, "r", encoding="utf-8") as f:
        l_content = f.read()
    l_content = update_messages_dict(l_content, lang)
    with open(lang_file, "w", encoding="utf-8") as f:
        f.write(l_content)
    print(f"Updated {lang_file}")

print("All locale updates for 31 Oct 2026 completed successfully!")
