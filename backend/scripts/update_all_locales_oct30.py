# -*- coding: utf-8 -*-
import re
import os

DATA = {
    "en": {
        "soccer": {
            "tagline": "Carabao Cup quarter-finals set: Fleetwood Town draw Newcastle at Highbury; Arsenal host Liverpool in MW9.",
            "liveNow": "Carabao Cup draw: Fleetwood vs Newcastle, Man City vs Brentford, Palace vs Liverpool. Saturday: Arsenal vs Liverpool at Emirates.",
            "pulse": "CARABAO CUP DRAW: FLEETWOOD TOWN HANDED GLAMOUR NEWCASTLE CLASH",
            "keywords": "Carabao Cup, quarter-final draw, Fleetwood Town, Newcastle, Arsenal, Liverpool, Emirates"
        },
        "basketball": {
            "tagline": "WNBA Champions: Expansion Valkyries edge Dream 76-71 in Game 6 to complete historic inaugural title run.",
            "liveNow": "WNBA Finals Game 6 Final: Valkyries 76, Dream 71 (GSV wins 4-2). Finals MVP Gabby Williams 21 pts, Thornton clutch three.",
            "pulse": "EXPANSION IMMORTALITY: VALKYRIES WIN 2026 WNBA CHAMPIONSHIP",
            "keywords": "WNBA Finals, Game 6, Champions, Valkyries, Gabby Williams, Angel Reese, Dream, title"
        },
        "football": {
            "tagline": "Packers roll past Panthers 27-17 on TNF: Jordan Love throws 2 TDs to lift Green Bay to 6-2.",
            "liveNow": "TNF Final: Packers 27, Panthers 17 at Lambeau Field. Jacobs 94 yds, Gary 2 sacks. Sunday: 6-0 Vikings defend unbeaten record.",
            "pulse": "TNF RECAP: PACKERS SUBDUE PANTHERS 27-17 IN FREEZING GREEN BAY",
            "keywords": "NFL Week 8, TNF, Packers, Panthers, Jordan Love, Josh Jacobs, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Vienna Quarter-finals: Alcaraz sweeps Draper 6-4, 6-4 to set up blockbuster Saturday semi-final against Zverev.",
            "liveNow": "Erste Bank Open QF: Alcaraz def. Draper 6-4, 6-4 (29 winners). Zverev def. Rublev 7-6 (4), 6-4. Semi-final Saturday: Alcaraz vs Zverev.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ AND ZVEREV SET UP BLOCKBUSTER SEMI-FINAL",
            "keywords": "ATP, Vienna, Erste Bank Open, Alcaraz, Draper, Zverev, Rublev, semi-finals"
        },
        "f1": {
            "tagline": "Mexico City GP Friday Practice: Antonelli sets blistering 1:17.342 pace in FP2 on title threshold.",
            "liveNow": "FP2 in Mexico: Antonelli 1:17.342 (P1), Leclerc +0.112 (P2), Verstappen +0.148 (P3). P9 on Sunday guarantees World Championship.",
            "pulse": "MEXICO CITY GP: ANTONELLI PACES FP2 AT ALTITUDE ON TITLE THRESHOLD",
            "keywords": "Formula 1, Mexico City GP, Antonelli, FP2, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open round 2: Smotherman fires 65 to lead at 11-under; Pereda and Rai pursue at 9-under.",
            "liveNow": "Round 2 at VidantaVallarta: Smotherman -11 (66-65, 131) leads by two over Pereda (-9) and Rai (-9). 36-hole cut falls at -1.",
            "pulse": "PGA TOUR MEXICO OPEN: SMOTHERMAN SURGES INTO 36-HOLE LEAD AT -11",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, 36-hole lead"
        },
        "home": {
            "tonight": "Friday desk",
            "tonightBlurb": "Valkyries crowned WNBA champions in Game 6 thriller. Packers beat Panthers 27-17 on TNF. Antonelli paces Mexico FP2.",
            "plTitle": "Carabao Cup draw: Fourth-tier Fleetwood Town draw Newcastle in dream home tie",
            "plBlurb": "Minnows host Magpies at Highbury; Man City draw Brentford and Liverpool face Crystal Palace ahead of Saturday Emirates showdown.",
            "f1Title": "Mexico City GP: Antonelli sets fastest practice time on title threshold",
            "f1Blurb": "Mercedes phenom clocks 1:17.342 in FP2 at 2,285 meters; needs only a ninth-place finish on Sunday to become world champion."
        },
        "pg": {
            "pinFinal": "Carabao Cup quarter-final draw: Fleetwood Town host Newcastle at Highbury; Man City face Brentford, Palace host Liverpool.",
            "week1Closed": "NFL Week 8 TNF final: Packers overpower Panthers 27-17 at Lambeau Field",
            "week1Sub": "Jordan Love throws 2 TDs and Jacobs rushes for 94 yds to reach 6-2. Sunday: 6-0 Vikings put undefeated streak on the line.",
            "countdownTnf": "Week 8 Sunday preview: 6-0 Vikings defend perfect record. Packers (6-2) handle Panthers 27-17 on TNF.",
            "barsPoints": "Bars show the gap to the leader. Antonelli has 365, 123 ahead of Russell on 242. P9 in Mexico clinches maiden title.",
            "tableAfterMonday": "Premier League Matchweek 9: Arsenal and City tied on 21 (7-0-1). Blockbuster Arsenal vs Liverpool on Saturday.",
            "pinClub": "Select a club. City and Arsenal lead on 21. Fleetwood Town draw Newcastle in Carabao Cup quarter-finals.",
            "plFootnote": "Carabao Cup QF draw: Fleetwood vs Newcastle, Man City vs Brentford, Palace vs Liverpool, Spurs vs Southampton. PL MW9 this weekend.",
            "majorsDone": "VidantaWorld Mexico Open Round 2: Smotherman leads at 11-under 131; Pereda and Rai chase at 9-under.",
            "wnbaFirstRound": "WNBA Finals Game 6 final: Valkyries defeat Dream 76-71 to capture historic maiden championship in inaugural year.",
            "bracketFootnote": "Game 1: Valkyries 68-64. Game 2: Dream 79-65. Game 3: Dream 97-71. Game 4: Valkyries 67-62. Game 5: Valkyries 64-55. Game 6: Valkyries 76-71 (GSV wins 4-2)."
        }
    },
    "fr": {
        "soccer": {
            "tagline": "Quarts de finale de Coupe de la Ligue : Fleetwood Town herite de Newcastle ; Arsenal affronte Liverpool en PL.",
            "liveNow": "Tirage Carabao Cup : Fleetwood contre Newcastle, Man City contre Brentford. Samedi : choc Arsenal contre Liverpool a l'Emirates.",
            "pulse": "TIRAGE COUPE DE LA LIGUE : FLEETWOOD TOWN DEFIERA NEWCASTLE A HIGHBURY",
            "keywords": "Carabao Cup, tirage quarts, Fleetwood Town, Newcastle, Arsenal, Liverpool, Emirates"
        },
        "basketball": {
            "tagline": "Les Valkyries championnes WNBA : Victoire 76-71 sur le Dream lors du match 6 pour un exploit inaugural historique.",
            "liveNow": "Finales WNBA match 6 final : Valkyries 76, Dream 71 (titre 4-2). Gabby Williams MVP des Finales (21 pts), tir decisif de Thornton.",
            "pulse": "LEGENDE INAUGURALE : LES VALKYRIES SACREES CHAMPIONNES WNBA 2026",
            "keywords": "Finales WNBA, match 6, championnes, Valkyries, Gabby Williams, Angel Reese, Dream, sacre"
        },
        "football": {
            "tagline": "Les Packers dominent Carolina 27-17 au TNF : Jordan Love lance 2 TD et porte Green Bay a 6-2.",
            "liveNow": "TNF final : Packers 27, Panthers 17 a Lambeau Field. Jacobs 94 yards, Gary 2 sacks. Dimanche : les Vikings (6-0) sous pression.",
            "pulse": "TNF FINAL : GREEN BAY DOMINE CAROLINA 27-17 SOUS LE FROID DE LAMBEAU",
            "keywords": "NFL semaine 8, TNF, Packers, Panthers, Jordan Love, Josh Jacobs, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Vienne quarts de finale : Alcaraz domine Draper 6-4, 6-4 et s'offre une demi-finale royale face a Zverev.",
            "liveNow": "Erste Bank Open quarts : Alcaraz bat Draper 6-4, 6-4 (29 coups gagnants). Zverev bat Rublev 7-6, 6-4. Choc Alcaraz contre Zverev samedi.",
            "pulse": "ERSTE BANK OPEN : ALCARAZ ET ZVEREV EN DEMI-FINALE ROYALE A VIENNE",
            "keywords": "ATP, Vienne, Erste Bank Open, Alcaraz, Draper, Zverev, Rublev, demi-finales"
        },
        "f1": {
            "tagline": "GP du Mexique essais libres : Antonelli survole les EL2 en 1:17.342 aux portes de la couronne mondiale.",
            "liveNow": "EL2 a Mexico : Antonelli 1:17.342 (P1), Leclerc +0,112 (P2), Verstappen +0,148 (P3). P9 dimanche assure le titre mondial.",
            "pulse": "GP DU MEXIQUE : ANTONELLI LE PLUS RAPIDE EN EL2 EN HAUTE ALTITUDE",
            "keywords": "Formule 1, GP du Mexique, Antonelli, EL2, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open T2 : Smotherman brille avec un 65 et mene a -11 ; Pereda et Rai a deux coups.",
            "liveNow": "2e tour a VidantaVallarta : Smotherman -11 (66-65, 131) mene de deux coups sur Pereda (-9) et Rai (-9). Cut a -1.",
            "pulse": "PGA TOUR MEXICO OPEN : SMOTHERMAN PREND LA TETE A -11 APRES 36 TROUS",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, 36 trous"
        },
        "home": {
            "tonight": "Bureau du vendredi",
            "tonightBlurb": "Les Valkyries sacrees championnes WNBA lors du match 6. Les Packers battent Carolina 27-17 au TNF. Antonelli en tete des EL2 a Mexico.",
            "plTitle": "Tirage Coupe de la Ligue : Fleetwood Town defiera Newcastle a domicile",
            "plBlurb": "Le club de D4 accueillera les Magpies a Highbury ; Man City tire Brentford et Liverpool ira a Crystal Palace avant le choc de samedi.",
            "f1Title": "GP du Mexique : Antonelli signe le meilleur temps des essais a l'approche du titre",
            "f1Blurb": "Le prodige italien tourne en 1:17.342 lors des EL2 a 2 285 m d'altitude ; une 9e place dimanche suffit pour etre sacre champion."
        },
        "pg": {
            "pinFinal": "Tirage quarts Coupe de la Ligue : Fleetwood Town accueille Newcastle a Highbury ; Man City defie Brentford, Liverpool a Selhurst Park.",
            "week1Closed": "NFL Semaine 8 TNF final : Les Packers dominent les Panthers 27-17 a Lambeau Field",
            "week1Sub": "Jordan Love lance 2 TD et Jacobs gagne 94 yards pour atteindre 6-2. Dimanche : les Vikings (6-0) defendent leur invincibilite.",
            "countdownTnf": "Apercu dimanche Semaine 8 : Vikings (6-0) invaincus. Les Packers (6-2) ecartent les Panthers 27-17 au TNF.",
            "barsPoints": "L'ecart avec le leader : Antonelli a 365 pts, 123 d'avance sur Russell (242). La 9e place au Mexique scelle le titre.",
            "tableAfterMonday": "Premier League 9e journee : Arsenal et City a 21 pts (7-0-1). Sommet Arsenal contre Liverpool ce samedi.",
            "pinClub": "Selectionnez un club. City et Arsenal en tete a 21. Fleetwood Town herite de Newcastle en quarts de coupe.",
            "plFootnote": "Tirage Carabao Cup : Fleetwood contre Newcastle, Man City contre Brentford, Palace contre Liverpool, Spurs contre Southampton.",
            "majorsDone": "VidantaWorld Mexico Open T2 : Smotherman en tete a -11 (131) ; Pereda et Rai en embuscade a -9.",
            "wnbaFirstRound": "Finales WNBA match 6 final : Les Valkyries battent le Dream 76-71 et decrochent un titre historique des leur premiere saison.",
            "bracketFootnote": "Match 1: Valkyries 68-64. Match 2: Dream 79-65. Match 3: Dream 97-71. Match 4: Valkyries 67-62. Match 5: Valkyries 64-55. Match 6: Valkyries 76-71 (GSV gagne 4-2)."
        }
    },
    "es": {
        "soccer": {
            "tagline": "Cuartos de Copa de la Liga definidos: Fleetwood Town recibe a Newcastle en Highbury; Arsenal recibe a Liverpool en Premier.",
            "liveNow": "Sorteo Carabao Cup: Fleetwood vs Newcastle, Man City vs Brentford, Palace vs Liverpool. Sabado: Arsenal vs Liverpool en el Emirates.",
            "pulse": "SORTEO COPA DE LA LIGA: EL MODESTO FLEETWOOD TOWN SE MEDIRA AL NEWCASTLE",
            "keywords": "Carabao Cup, sorteo cuartos, Fleetwood Town, Newcastle, Arsenal, Liverpool, Emirates"
        },
        "basketball": {
            "tagline": "Campeonas WNBA: Las Valkyries baten 76-71 al Dream en el Partido 6 y logran el titulo en su primer ano.",
            "liveNow": "Finales WNBA Partido 6 Final: Valkyries 76, Dream 71 (serie 4-2). Gabby Williams MVP de las Finales con 21 pts; triple salvador de Thornton.",
            "pulse": "GLORIA DE EXPANSION: VALKYRIES CONQUISTAN EL CAMPEONATO WNBA 2026",
            "keywords": "WNBA Finals, Partido 6, campeonas, Valkyries, Gabby Williams, Angel Reese, Dream, titulo"
        },
        "football": {
            "tagline": "Packers superan 27-17 a Panthers en TNF: Jordan Love lanza 2 TD y situa a Green Bay con 6-2.",
            "liveNow": "TNF Final: Packers 27, Panthers 17 en Lambeau Field. Jacobs 94 yardas, Gary 2 capturas. Domingo: Vikings (6-0) defienden el invicto.",
            "pulse": "TNF CRONICA: GREEN BAY IMPONE SU LEY ANTE CAROLINA 27-17 EN LAMBEAU",
            "keywords": "NFL Semana 8, TNF, Packers, Panthers, Jordan Love, Josh Jacobs, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Viena cuartos de final: Alcaraz supera 6-4, 6-4 a Draper y se cita en semifinales con Zverev.",
            "liveNow": "Erste Bank Open QF: Alcaraz bate a Draper 6-4, 6-4 (29 golpes ganadores). Zverev vence a Rublev 7-6, 6-4. Semifinal sabado: Alcaraz vs Zverev.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ Y ZVEREV PROTAGONIZARAN UNA GRAN SEMIFINAL",
            "keywords": "ATP, Viena, Erste Bank Open, Alcaraz, Draper, Zverev, Rublev, semifinales"
        },
        "f1": {
            "tagline": "GP de Mexico entrenamientos: Antonelli vuela en los Libres 2 con 1:17.342 a las puertas del campeonato.",
            "liveNow": "Libres 2 en Mexico: Antonelli 1:17.342 (P1), Leclerc +0.112 (P2), Verstappen +0.148 (P3). P9 el domingo asegura el titulo mundial.",
            "pulse": "GP DE MEXICO: ANTONELLI LIDERA LOS LIBRES 2 ANTE SU CORONACION",
            "keywords": "Formula 1, GP de Mexico, Antonelli, Libres 2, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R2: Smotherman firma 65 impactos para liderar con -11; Pereda y Rai le siguen con -9.",
            "liveNow": "Ronda 2 en VidantaVallarta: Smotherman -11 (66-65, 131) aventaja en dos golpes a Pereda (-9) y Rai (-9). Corte en -1.",
            "pulse": "PGA TOUR MEXICO OPEN: SMOTHERMAN TOMA EL MANDO CON 11 BAJO PAR",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, liderato 36 hoyos"
        },
        "home": {
            "tonight": "Mesa del viernes",
            "tonightBlurb": "Valkyries se coronan campeonas de la WNBA en el Partido 6. Packers vencen 27-17 a Panthers en TNF. Antonelli lidera libres en Mexico.",
            "plTitle": "Sorteo Copa de la Liga: El modesto Fleetwood Town recibe al Newcastle en casa",
            "plBlurb": "El club de cuarta division acoge al Newcastle en Highbury; Man City emparejado con Brentford y Liverpool visita al Palace.",
            "f1Title": "GP de Mexico: Antonelli marca el ritmo mas veloz camino del titulo mundial",
            "f1Blurb": "El joven italiano para el crono en 1:17.342 a 2.285 metros; un noveno puesto el domingo le corona como campeon del mundo."
        },
        "pg": {
            "pinFinal": "Sorteo cuartos Copa de la Liga: Fleetwood Town recibe a Newcastle en Highbury; Man City ante Brentford, Liverpool visita al Palace.",
            "week1Closed": "NFL Semana 8 TNF final: Packers vencen 27-17 a Panthers bajo los focos de Lambeau Field",
            "week1Sub": "Jordan Love lanza 2 TD y Jacobs corre para 94 yds para colocar a Green Bay 6-2. Domingo: Vikings defienden marca de 6-0.",
            "countdownTnf": "Previo domingo Semana 8: Vikings (6-0) defienden el invicto. Packers (6-2) derrotan 27-17 a Panthers en TNF.",
            "barsPoints": "Barras muestran distancia al lider. Antonelli suma 365, 123 mas que Russell (242). P9 en Mexico asegura el titulo.",
            "tableAfterMonday": "Premier League Jornada 9: Arsenal y City empatados con 21 pts (7-0-1). Bloque estelar Arsenal vs Liverpool el sabado.",
            "pinClub": "Selecciona un club. City y Arsenal mandan con 21. Fleetwood Town jugara ante Newcastle en cuartos de copa.",
            "plFootnote": "Sorteo Carabao Cup: Fleetwood vs Newcastle, Man City vs Brentford, Palace vs Liverpool, Spurs vs Southampton.",
            "majorsDone": "VidantaWorld Mexico Open R2: Smotherman lidera con 11 bajo par (131); Pereda y Rai acechan con 9 bajo par.",
            "wnbaFirstRound": "Finales WNBA Partido 6 final: Valkyries derrotan 76-71 a Dream y ganan un campeonato historico en su temporada debut.",
            "bracketFootnote": "Partido 1: Valkyries 68-64. Partido 2: Dream 79-65. Partido 3: Dream 97-71. Partido 4: Valkyries 67-62. Partido 5: Valkyries 64-55. Partido 6: Valkyries 76-71 (GSV gana 4-2)."
        }
    },
    "de": {
        "soccer": {
            "tagline": "Carabao Cup Viertelfinale fix: Fleetwood Town empfaengt Newcastle; Arsenal fordert Liverpool in der Premier League.",
            "liveNow": "Ligapokal-Auslosung: Fleetwood vs Newcastle, Man City vs Brentford, Palace vs Liverpool. Samstag: Topspiel Arsenal vs Liverpool.",
            "pulse": "LIGAPOKAL-AUSLOSUNG: TRAUMLOS FLEETWOOD TOWN EMPFAENGT NEWCASTLE",
            "keywords": "Carabao Cup, Auslosung Viertelfinale, Fleetwood Town, Newcastle, Arsenal, Liverpool, Emirates"
        },
        "basketball": {
            "tagline": "WNBA Champions: Neuling Valkyries ringt Dream mit 76:71 nieder und vollendet historisches Premieren-Wunder.",
            "liveNow": "WNBA Finals Spiel 6 Endstand: Valkyries 76, Dream 71 (Serie 4:2). Finals-MVP Gabby Williams mit 21 Pkt; Thornton trifft entscheidenden Dreier.",
            "pulse": "PREMIEREN-SENSATION: VALKYRIES SIND WNBA CHAMPIONS 2026",
            "keywords": "WNBA Finals, Spiel 6, Meister, Valkyries, Gabby Williams, Angel Reese, Dream, Titel"
        },
        "football": {
            "tagline": "Packers bezwingen Panthers im TNF mit 27:17: Jordan Love wirft 2 TDs und fuehrt Green Bay auf 6:2.",
            "liveNow": "TNF Endstand: Packers 27, Panthers 17 im Lambeau Field. Jacobs 94 Yards, Gary 2 Sacks. Sonntag: ungeschlagene Vikings (6:0) im Einsatz.",
            "pulse": "TNF REKORD: PACKERS BEZWINGEN PANTHERS 27:17 IM FROSTIGEN GREEN BAY",
            "keywords": "NFL Woche 8, TNF, Packers, Panthers, Jordan Love, Josh Jacobs, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Wien Viertelfinale: Alcaraz schlaegt Draper 6:4, 6:4 und zieht ins Halbfinal-Duell gegen Zverev ein.",
            "liveNow": "Erste Bank Open VF: Alcaraz besiegt Draper 6:4, 6:4 (29 Winner). Zverev schlaegt Rublev 7:6, 6:4. Halbfinale am Samstag: Alcaraz vs Zverev.",
            "pulse": "ERSTE BANK OPEN: TRAUM-HALBFINALE ZWISCHEN ALCARAZ UND ZVEREV PERFEKT",
            "keywords": "ATP, Wien, Erste Bank Open, Alcaraz, Draper, Zverev, Rublev, Halbfinale"
        },
        "f1": {
            "tagline": "GP Mexiko Training: Antonelli setzt mit 1:17.342 die Bestzeit in FP2 vor moeglicher WM-Kroenung.",
            "liveNow": "FP2 in Mexiko: Antonelli 1:17.342 (P1), Leclerc +0.112 (P2), Verstappen +0.148 (P3). P9 am Sonntag garantiert den Weltmeistertitel.",
            "pulse": "GP MEXIKO: ANTONELLI DOMINIERT FP2 AUF 2.285 METERN HOEHE",
            "keywords": "Formel 1, GP Mexiko, Antonelli, FP2, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R2: Smotherman fuehrt nach einer 65 mit -11; Pereda und Rai bei 9 unter Par.",
            "liveNow": "Runde 2 in VidantaVallarta: Smotherman -11 (66-65, 131) liegt zwei Schlaege vor Pereda (-9) und Rai (-9). Cut bei -1.",
            "pulse": "PGA TOUR MEXICO OPEN: SMOTHERMAN UEBERNIMMT MIT 11 UNTER PAR DIE SPITZE",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, Halbzeitfuehrung"
        },
        "home": {
            "tonight": "Freitags-Redaktion",
            "tonightBlurb": "Valkyries holen die WNBA-Kroene in Spiel 6. Packers schlagen Panthers 27:17 im TNF. Antonelli Schnellster im Mexiko-Training.",
            "plTitle": "Ligapokal-Auslosung: Viertligist Fleetwood Town zieht Traumlos Newcastle",
            "plBlurb": "Außenseiter empfaengt Newcastle im Highbury Stadium; Man City trifft auf Brentford und Liverpool reist zu Crystal Palace.",
            "f1Title": "GP Mexiko: Antonelli faehrt Bestzeit vor dem grossen Titeltag",
            "f1Blurb": "Der Mercedes-Pilot dreht auf 2.285 Metern Hoehe die schnellste Runde in FP2; Platz neun am Sonntag genuegt zum WM-Titel."
        },
        "pg": {
            "pinFinal": "Carabao Cup Viertelfinale: Fleetwood Town empfaengt Newcastle; Man City gegen Brentford, Liverpool gastiert bei Palace.",
            "week1Closed": "NFL Woche 8 TNF Endstand: Packers schlagen Panthers mit 27:17 im Lambeau Field",
            "week1Sub": "Jordan Love wirft 2 TDs und Jacobs laeuft fuer 94 Yards zum 6:2-Erfolg. Sonntag: ungeschlagene Vikings (6:0) gefordert.",
            "countdownTnf": "NFL Sonntag Vorschau: Vikings (6:0) verteidigen weisse Weste. Packers (6:2) siegen 27:17 gegen Panthers im TNF.",
            "barsPoints": "Balken zeigen Abstand zum Führenden. Antonelli hat 365 Pkt, 123 vor Russell (242). P9 in Mexiko genuegt zum Titel.",
            "tableAfterMonday": "Premier League 9. Spieltag: Arsenal und City punktgleich bei 21 (7-0-1). Top-Duell Arsenal vs Liverpool am Samstag.",
            "pinClub": "Waehlen Sie einen Klub. City und Arsenal fuehren mit 21. Fleetwood Town trifft im Pokal auf Newcastle.",
            "plFootnote": "Ligapokal Viertelfinale: Fleetwood vs Newcastle, Man City vs Brentford, Palace vs Liverpool, Spurs vs Southampton.",
            "majorsDone": "VidantaWorld Mexico Open R2: Smotherman fuehrt mit 11 unter Par (131); Pereda und Rai lauern bei -9.",
            "wnbaFirstRound": "WNBA Finals Spiel 6 Endstand: Valkyries schlagen Dream 76:71 und gewinnen sensationell die Meisterschaft im Premierenjahr.",
            "bracketFootnote": "Spiel 1: Valkyries 68:64. Spiel 2: Dream 79:65. Spiel 3: Dream 97:71. Spiel 4: Valkyries 67:62. Spiel 5: Valkyries 64:55. Spiel 6: Valkyries 76:71 (GSV gewinnt 4:2)."
        }
    },
    "it": {
        "soccer": {
            "tagline": "Quarti di Carabao Cup definiti: Il Fleetwood Town pesca il Newcastle a Highbury; Arsenal-Liverpool sabato.",
            "liveNow": "Sorteggio Coppa di Lega: Fleetwood vs Newcastle, Man City vs Brentford, Palace vs Liverpool. Sabato: Arsenal vs Liverpool all'Emirates.",
            "pulse": "COPPA DI LEGA: IL FAVOLOSO FLEETWOOD TOWN PESCA IL NEWCASTLE A HIGHBURY",
            "keywords": "Carabao Cup, sorteggio quarti, Fleetwood Town, Newcastle, Arsenal, Liverpool, Emirates"
        },
        "basketball": {
            "tagline": "Valkyries campionesse WNBA: Battute le Dream 76-71 in Gara 6 completando un miracolo sportivo al debutto.",
            "liveNow": "Finali WNBA Gara 6 Finale: Valkyries 76, Dream 71 (serie 4-2). Gabby Williams MVP delle Finali (21 punti), tripla decisiva di Thornton.",
            "pulse": "IMPRESA DA LEGGENDA: LE VALKYRIES VINCONO IL TITOLO WNBA 2026",
            "keywords": "WNBA Finals, Gara 6, campionesse, Valkyries, Gabby Williams, Angel Reese, Dream, titolo"
        },
        "football": {
            "tagline": "I Packers superano i Panthers 27-17 nel TNF: Jordan Love lancia 2 TD portando Green Bay sul 6-2.",
            "liveNow": "TNF Finale: Packers 27, Panthers 17 a Lambeau Field. Jacobs 94 yard, Gary 2 sack. Domenica: Vikings (6-0) imbattuti.",
            "pulse": "TNF REPORT: GREEN BAY PIEGA CAROLINA 27-17 NELLA NOTTE DI LAMBEAU",
            "keywords": "NFL Week 8, TNF, Packers, Panthers, Jordan Love, Josh Jacobs, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Vienna quarti di finale: Alcaraz batte Draper 6-4, 6-4 e vola in semifinale contro Alexander Zverev.",
            "liveNow": "Erste Bank Open QF: Alcaraz supera Draper 6-4, 6-4 (29 vincenti). Zverev piega Rublev 7-6, 6-4. Sabato semifinale Alcaraz vs Zverev.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ E ZVEREV REGALANO UNA SEMIFINALE STELLARE",
            "keywords": "ATP, Vienna, Erste Bank Open, Alcaraz, Draper, Zverev, Rublev, semifinali"
        },
        "f1": {
            "tagline": "GP Messico prove libere: Antonelli vola nelle FP2 in 1:17.342 a un passo dall'iride mondiale.",
            "liveNow": "FP2 a Citta del Messico: Antonelli 1:17.342 (P1), Leclerc +0.112 (P2), Verstappen +0.148 (P3). P9 domenica basta per il titolo.",
            "pulse": "GP MESSICO: ANTONELLI DETTA IL PASSO NELLE FP2 IN QUOTA VERSO IL TITOLO",
            "keywords": "Formula 1, GP Messico, Antonelli, FP2, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R2: Smotherman gira in 65 e guida a -11; Pereda e Rai inseguono a quota -9.",
            "liveNow": "Giro 2 a VidantaVallarta: Smotherman -11 (66-65, 131) avanti di due colpi su Pereda (-9) e Rai (-9). Taglio a -1.",
            "pulse": "PGA TOUR MEXICO OPEN: SMOTHERMAN IN VETTA DA SOLO A QUOTA 11 SOTTO IL PAR",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, comando 36 buche"
        },
        "home": {
            "tonight": "Desk di venerdi",
            "tonightBlurb": "Le Valkyries trionfano in Gara 6 e vincono il titolo WNBA. I Packers superano i Panthers 27-17 nel TNF. Antonelli domina le FP2 in Messico.",
            "plTitle": "Sorteggio Coppa di Lega: Il favoloso Fleetwood Town ospitera il Newcastle",
            "plBlurb": "La matricola di quarta serie affrontera i Magpies a Highbury; Man City pesca il Brentford e Liverpool sul campo del Crystal Palace.",
            "f1Title": "GP Messico: Antonelli svetta nelle prove libere alla vigilia della coronazione",
            "f1Blurb": "Il talento italiano ferma il cronometro a 1:17.342 nelle FP2 a 2.285 metri; nono posto sufficiente domenica per laurearsi campione.",
        },
        "pg": {
            "pinFinal": "Sorteggio quarti Carabao Cup: Fleetwood Town ospita il Newcastle a Highbury; Man City vs Brentford, Palace contro Liverpool.",
            "week1Closed": "NFL Week 8 TNF finale: I Packers superano i Panthers per 27-17 al Lambeau Field",
            "week1Sub": "Jordan Love lancia 2 TD e Jacobs corre per 94 yard portando Green Bay sul 6-2. Domenica: Vikings a quota 6-0.",
            "countdownTnf": "Presentazione domenica Week 8: Vikings (6-0) imbattuti. I Packers (6-2) battono i Panthers 27-17 nel TNF.",
            "barsPoints": "Distanza dalla vetta: Antonelli ha 365 pts, 123 su Russell (242). Il 9° posto in Messico assicura il primo titolo.",
            "tableAfterMonday": "Premier League 9a giornata: Arsenal e City appaiate a 21 (7-0-1). Sabato grande sfida Arsenal vs Liverpool.",
            "pinClub": "Scegli un club. City e Arsenal prime con 21. Fleetwood Town affrontera il Newcastle nei quarti di coppa.",
            "plFootnote": "Carabao Cup quarti: Fleetwood vs Newcastle, Man City vs Brentford, Palace vs Liverpool, Spurs vs Southampton.",
            "majorsDone": "VidantaWorld Mexico Open R2: Smotherman guida a -11 (131); Pereda e Rai inseguono a -9.",
            "wnbaFirstRound": "Finali WNBA Gara 6 finale: Le Valkyries battono le Dream 76-71 e conquistano uno storico titolo al primo anno.",
            "bracketFootnote": "Gara 1: Valkyries 68-64. Gara 2: Dream 79-65. Gara 3: Dream 97-71. Gara 4: Valkyries 67-62. Gara 5: Valkyries 64-55. Gara 6: Valkyries 76-71 (GSV vince 4-2)."
        }
    },
    "pl": {
        "soccer": {
            "tagline": "Pary cwiercfinalowe Pucharu Ligi: Fleetwood Town podejmie Newcastle na Highbury; hit Arsenal vs Liverpool w sobote.",
            "liveNow": "Losowanie Carabao Cup: Fleetwood vs Newcastle, Man City vs Brentford, Palace vs Liverpool. W sobote Arsenal kontra Liverpool.",
            "pulse": "LOSOWANIE PUCHARU LIGI: FLEETWOOD TOWN ZAGRA Z NEWCASTLE NA HIGHBURY",
            "keywords": "Carabao Cup, losowanie cwiercfinalu, Fleetwood Town, Newcastle, Arsenal, Liverpool, Emirates"
        },
        "basketball": {
            "tagline": "Mistrzynie WNBA: Debiutujace Valkyries pokonuja Dream 76:71 w meczu 6 i siegaja po puchar w pierwszym roku istnienia.",
            "liveNow": "Finaly WNBA mecz 6 wynik: Valkyries 76, Dream 71 (seria 4-2). Gabby Williams MVP Finalow z 21 pkt; decydujaca trojka Thornton.",
            "pulse": "HISTORYCZNY SUKCES DEBIUTANTA: VALKYRIES MISTRZYNIAMI WNBA 2026",
            "keywords": "WNBA Finals, mecz 6, mistrzynie, Valkyries, Gabby Williams, Angel Reese, Dream, puchar"
        },
        "football": {
            "tagline": "Packers pokonuja Panthers 27:17 w TNF: Jordan Love rzuca 2 TD i prowadzi Green Bay do bilansu 6-2.",
            "liveNow": "TNF wynik: Packers 27, Panthers 17 na Lambeau Field. Jacobs 94 jardy, Gary 2 sacki. W niedziele niepokonani Vikings (6-0).",
            "pulse": "TNF PODSUMOWANIE: GREEN BAY WYGRYWA Z CAROLINA 27:17 W ZIMNYM LAMBEAU",
            "keywords": "NFL Tydzien 8, TNF, Packers, Panthers, Jordan Love, Josh Jacobs, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Wieden cwiercfinaly: Alcaraz pewnie pokonuje Drapera 6:4, 6:4 i w sobote zagra w polfinale ze Zverevem.",
            "liveNow": "Erste Bank Open QF: Alcaraz def. Draper 6:4, 6:4 (29 winnerow). Zverev pokonuje Rublowa 7:6, 6:4. Hitowy polfinal Alcaraz vs Zverev w sobote.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ I ZVEREV W WIELKIM POLFINALE W WIEDNIU",
            "keywords": "ATP, Wieden, Erste Bank Open, Alcaraz, Draper, Zverev, Rublow, polfinal"
        },
        "f1": {
            "tagline": "GP Meksyku treningi: Antonelli uzyskuje czas 1:17.342 w FP2 i zbliza sie do tytulu mistrza swiata.",
            "liveNow": "FP2 w Meksyku: Antonelli 1:17.342 (P1), Leclerc +0.112 (P2), Verstappen +0.148 (P3). P9 w niedziele da mu mistrzostwo.",
            "pulse": "GP MEKSYKU: ANTONELLI NAJSZYBSZY W FP2 NA WYSOKOSCI PRZED SZANSA NA TYTUL",
            "keywords": "Formula 1, GP Meksyku, Antonelli, FP2, Leclerc, Verstappen, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R2: Smotherman z wynikiem 65 na czele z -11; Pereda i Rai traca dwa uderzenia.",
            "liveNow": "Runda 2 w VidantaVallarta: Smotherman -11 (66-65, 131) prowadzi przed Pereda (-9) i Rai (-9). Cut ustalony na -1.",
            "pulse": "PGA TOUR MEXICO OPEN: SMOTHERMAN SAMODZIELNYM LIDEREM PO 36 DOLKACH (-11)",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Pereda, Rai, VidantaVallarta, lider 36 dolkow"
        },
        "home": {
            "tonight": "Wydanie piatkowe",
            "tonightBlurb": "Valkyries mistrzyniami WNBA po triumfie w meczu 6. Packers wygrywaja z Panthers 27:17 w TNF. Antonelli najszybszy w treningu w Meksyku.",
            "plTitle": "Losowanie Pucharu Ligi: Czwartoligowe Fleetwood Town podejmie Newcastle United",
            "plBlurb": "Kopciuszek zagra u siebie z Newcastle na Highbury; Man City podejmie Brentford, a Liverpool zmierzy sie z Crystal Palace.",
            "f1Title": "GP Meksyku: Antonelli najszybszy w treningu przed niedzielna szansa na tytul",
            "f1Blurb": "Wloski kierowca uzyskal wynik 1:17.342 na wysokosci 2285 metrow; dziewiate miejsce w niedziele da mu upragnione mistrzostwo."
        },
        "pg": {
            "pinFinal": "Carabao Cup cwiercfinal: Fleetwood Town podejmie Newcastle na Highbury; Man City vs Brentford, Palace zagra z Liverpoolem.",
            "week1Closed": "NFL Tydzien 8 TNF final: Packers pokonuja Panthers 27:17 na Lambeau Field",
            "week1Sub": "Jordan Love rzuca 2 TD, a Jacobs notuje 94 jardy biegiem na wage bilansu 6-2. W niedziele niepokonani Vikings (6-0).",
            "countdownTnf": "Zapowiedz niedzieli Tygodnia 8: Vikings (6-0) bronia niepokonanej serii. Packers (6-2) pewnie ogrywaja Panthers 27:17 w TNF.",
            "barsPoints": "Wykres pokazuje strate do lidera. Antonelli ma 365 pkt, o 123 wiecej niz Russell (242). P9 w Meksyku daje tytul.",
            "tableAfterMonday": "Premier League 9. kolejka: Arsenal i City na czele z 21 pkt (7-0-1). Hitowe starcie Arsenal vs Liverpool w sobote.",
            "pinClub": "Wybierz klub. City i Arsenal lideruja z 21 pkt. Fleetwood Town wylosowalo Newcastle w cwiercfinale pucharu.",
            "plFootnote": "Puchar Ligi 1/4: Fleetwood vs Newcastle, Man City vs Brentford, Palace vs Liverpool, Spurs vs Southampton.",
            "majorsDone": "VidantaWorld Mexico Open R2: Smotherman prowadzi z -11 (131); Pereda i Rai gonia z wynikiem -9.",
            "wnbaFirstRound": "Finaly WNBA mecz 6 final: Valkyries wygrywaja 76:71 z Dream i zdobywaja historyczne mistrzostwo w debiutanckim sezonie.",
            "bracketFootnote": "Mecz 1: Valkyries 68:64. Mecz 2: Dream 79:65. Mecz 3: Dream 97:71. Mecz 4: Valkyries 67:62. Mecz 5: Valkyries 64:55. Mecz 6: Valkyries 76:71 (GSV wygrywa 4-2)."
        }
    },
    "zh": {
        "soccer": {
            "tagline": "联赛杯八强对阵出炉：第四级别黑马弗利特伍德主场迎战纽卡斯尔联；英超阿森纳迎战利物浦。",
            "liveNow": "联赛杯抽签：弗利特伍德对纽卡，曼城对布伦特福德，利物浦客战水晶宫。周六英超焦点：阿森纳对利物浦。",
            "pulse": "联赛杯八强抽签：英乙黑马弗利特伍德坐镇主场硬碰纽卡斯尔联",
            "keywords": "联赛杯, 八强抽签, 弗利特伍德, 纽卡斯尔联, 阿森纳, 利物浦, 酋长球场"
        },
        "basketball": {
            "tagline": "WNBA总冠军诞生：新军金州女武神G6以76-71力克梦想，总比分4-2创造建队首年夺冠神迹。",
            "liveNow": "WNBA总决赛G6终局：女武神76-71击溃梦想（总比分4-2夺冠）。总决赛MVP威廉姆斯21分，桑顿命中制胜三分。",
            "pulse": "新军历史神迹：金州女武神夺得2026年WNBA总冠军",
            "keywords": "WNBA总决赛, G6, 总冠军, 女武神, 威廉姆斯, 里斯, 梦想, 夺冠"
        },
        "football": {
            "tagline": "周四夜赛包装工27-17轻取黑豹：乔丹·爱芙两度传球达阵，绿湾战绩改写为6胜2负。",
            "liveNow": "周四夜赛终局：包装工主场27-17黑豹。雅各布斯冲球94码，加里斩获2次擒杀。周日不败维京人（6-0）出战。",
            "pulse": "周四夜赛综述：包装工兰博球场27-17战胜黑豹挺进6胜",
            "keywords": "NFL第8周, TNF, 包装工, 黑豹, 乔丹爱芙, 雅各布斯, 兰博球场, 维京人"
        },
        "tennis": {
            "tagline": "维也纳站八强战：阿尔卡拉斯6-4、6-4轻取德雷珀，周六半决赛火拼头号种子兹维列夫。",
            "liveNow": "维也纳公开赛QF：阿尔卡拉斯直落两盘击退德雷珀（轰出29记制胜分）。兹维列夫击败卢布列夫。周六半决赛强强对话。",
            "pulse": "维也纳公开赛：阿尔卡拉斯与兹维列夫会师男单半决赛焦点战",
            "keywords": "ATP, 维也纳, 维也纳公开赛, 阿尔卡拉斯, 德雷珀, 兹维列夫, 卢布列夫, 半决赛"
        },
        "f1": {
            "tagline": "F1墨西哥站周五练习赛：安东内利二练飙出1分17秒342高居榜首，世界冠军近在咫尺。",
            "liveNow": "墨西哥城二练：安东内利1:17.342（P1），勒克莱尔+0.112（P2），维斯塔潘+0.148（P3）。周日正赛保住P9即封王。",
            "pulse": "F1墨西哥大奖赛：安东内利二练拔得头筹步入冠军加冕点",
            "keywords": "F1, 墨西哥站, 安东内利, 二练, 勒克莱尔, 维斯塔潘, 罗德里格斯赛道"
        },
        "golf": {
            "tagline": "墨西哥公开赛第二轮：斯莫瑟曼轰65杆总成绩-11领跑；佩雷达与赖以-9杆紧随其后。",
            "liveNow": "巴亚尔塔港次轮：斯莫瑟曼-11（66-65，131）领先佩雷达（-9）和赖（-9）两杆。36洞晋级线定在-1杆。",
            "pulse": "美巡赛墨西哥公开赛：斯莫瑟曼次轮交出65杆以低于标准杆11杆独占鳌头",
            "keywords": "美巡赛, 墨西哥公开赛, 斯莫瑟曼, 佩雷达, 赖, 巴亚尔塔港, 36洞领先"
        },
        "home": {
            "tonight": "周五体育前线",
            "tonightBlurb": "金州女武神在G6决战中加冕WNBA总冠军。包装工周四夜赛27-17战胜黑豹。安东内利领跑墨西哥站二练。",
            "plTitle": "联赛杯八强抽签：第四级别弗利特伍德主场迎战纽卡斯尔联",
            "plBlurb": "海滨弱旅坐镇主场迎击喜鹊；曼城抽中布伦特福德，利物浦做客水晶宫，周六酋长球场阿森纳硬碰红军。",
            "f1Title": "F1墨西哥大奖赛：安东内利二练刷出最快圈速迎加冕时刻",
            "f1Blurb": "梅赛德斯天才车手在海拔2285米跑出1分17秒342；周日正赛获得第九名即可成为历史最年轻世界冠军。"
        },
        "pg": {
            "pinFinal": "联赛杯八强对阵：弗利特伍德主场战纽卡；曼城对布伦特福德，水晶宫迎战利物浦，热刺碰南安普顿。",
            "week1Closed": "NFL第8周周四夜赛终局：包装工在兰博球场27-17战胜黑豹",
            "week1Sub": "乔丹·爱芙传出2次达阵，雅各布斯冲球94码，绿湾战绩升至6胜2负。周日维京人（6-0）出战捍卫不败身。",
            "countdownTnf": "第8周周日展望：6胜0负维京人迎战强敌。包装工（6-2）周四夜赛27-17拿下黑豹。",
            "barsPoints": "积分柱状图显示与领跑者的差距。安东内利365分，领先拉塞尔123分。墨西哥站第9即可锁定头衔。",
            "tableAfterMonday": "英超积分榜第9轮：阿森纳与曼城同积21分（7胜0平1负）。周六酋长球场阿森纳对阵利物浦超级对决。",
            "pinClub": "选择俱乐部查看数据。曼城阿森纳积21分领跑。弗利特伍德联赛杯抽中纽卡斯尔联。",
            "plFootnote": "联赛杯八强：弗利特伍德对纽卡，曼城对布伦特福德，水晶宫对利物浦，热刺对南安普顿。英超第9轮周末打响。",
            "majorsDone": "墨西哥公开赛第2轮：斯莫瑟曼以低于标准杆11杆（131）领跑；佩雷达与赖以-9杆紧随其后。",
            "wnbaFirstRound": "WNBA总决赛G6终局：金州女武神76-71击退梦想，建队首年奇迹般夺得队史首座总冠军奖杯。",
            "bracketFootnote": "G1: 女武神 68-64。G2: 梦想 79-65。G3: 梦想 97-71。G4: 女武神 67-62。G5: 女武神 64-55。G6: 女武神 76-71（女武神4-2夺冠）。"
        }
    },
    "ja": {
        "soccer": {
            "tagline": "カラバオ杯8強対戦決定：4部フリートウッドが本拠地でニューカッスルと激突；プレミアは首位攻防戦へ。",
            "liveNow": "カラバオ杯抽選：フリートウッド対ニューカッスル、マンC対ブレントフォード。土曜プレミア：アーセナル対リヴァプール。",
            "pulse": "カラバオ杯8強決定：快進撃のフリートウッドが本拠地にニューカッスルを迎撃",
            "keywords": "カラバオ杯, 8強抽選, フリートウッド, ニューカッスル, アーセナル, リヴァプール, エミレーツ"
        },
        "basketball": {
            "tagline": "WNBA年間王者誕生：ヴァルキリーズが第6戦を76-71で制し、創設初年度での歴史的完全制覇を達成。",
            "liveNow": "WNBAファイナル第6戦試合終了：ヴァルキリーズ 76-71 ドリーム（4勝2敗で初優勝）。ギャビー・ウィリアムズが21得点でMVP。",
            "pulse": "創設初年度の完全優勝：ゴールデンステイト・ヴァルキリーズがWNBA制覇",
            "keywords": "WNBAファイナル, 第6戦, 優勝, ヴァルキリーズ, ギャビー・ウィリアムズ, エンジェル・リース, ドリーム"
        },
        "football": {
            "tagline": "パッカーズがパンサーズを27-17で退ける：ジョーダン・ラヴが2TDパスを決めグリーンベイが6勝2敗へ。",
            "liveNow": "TNF試合終了：ランボーでパッカーズが27-17勝利。ジェイコブズが94ヤード獲得、守備陣4サック。日曜日は無敗バイキングス登場。",
            "pulse": "TNF総括：グリーンベイがランボー・フィールドでパンサーズに快勝",
            "keywords": "NFL第8週, TNF, パッカーズ, パンサーズ, ジョーダン・ラヴ, ジェイコブズ, ランボー, バイキングス"
        },
        "tennis": {
            "tagline": "ウィーン準々決勝：アルカラスがドレイパーを6-4、6-4で一蹴し、土曜の準決勝でズベレフと激突へ。",
            "liveNow": "エルステ・バンク・オープンQF：アルカラスがドレイパーをストレート撃破（ウィナー29本）。ズベレフも8強突破。土曜準決勝で激突。",
            "pulse": "エルステ・バンク・オープン：アルカラスとズベレフが準決勝で頂上決戦へ",
            "keywords": "ATP, ウィーン, エルステ・バンク・オープン, アルカラス, ドレイパー, ズベレフ, ルブレフ, 準決勝"
        },
        "f1": {
            "tagline": "F1メキシコGP金曜走行：アントネッリがFP2で1分17秒342のトップタイム、世界タイトルへ視界良好。",
            "liveNow": "メキシコFP2：アントネッリ 1:17.342（P1）、ルクレール +0.112（P2）、フェルスタッペン +0.148（P3）。日曜9位でタイトル獲得。",
            "pulse": "F1メキシコGP：アントネッリが標高2285mの高地FP2で堂々首位発進",
            "keywords": "F1, メキシコGP, アントネッリ, FP2, ルクレール, フェルスタッペン, ロドリゲス・サーキット"
        },
        "golf": {
            "tagline": "メキシコオープン2日目：スモザーマンがノーボギーの65をマークし通算11アンダーで単独首位浮上。",
            "liveNow": "ヴィダンタ・ヴァジャルタ第2R：スモザーマン -11（66-65、131）が首位。地元ペレダ（-9）とライ（-9）が追走。予選カットは-1。",
            "pulse": "PGAツアー・メキシコオープン：スモザーマンが通算11アンダーで単独首位へ浮上",
            "keywords": "PGAツアー, メキシコオープン, スモザーマン, ペレダ, ライ, ヴィダンタ・ヴァジャルタ, 36ホール首位"
        },
        "home": {
            "tonight": "金曜デスク",
            "tonightBlurb": "ヴァルキリーズが第6戦を制してWNBA王者に輝く。パッカーズがTNFで27-17勝利。アントネッリがメキシコFP2で最速タイム。",
            "plTitle": "カラバオ杯抽選結果：4部フリートウッドが本拠地でニューカッスルを迎え撃つ",
            "plBlurb": "快進撃の下位クラブが名門を本拠地に迎える；マンCはブレントフォードと激突、土曜はアーセナル対リヴァプールの頂上決戦。",
            "f1Title": "F1メキシコGP：アントネッリが戴冠目前で金曜練習走行トップタイム",
            "f1Blurb": "メルセデスの新星が標高2285mの高地で1分17秒342を記録；日曜決勝で9位以上に入れば史上最年少王者に決定。"
        },
        "pg": {
            "pinFinal": "カラバオ杯準々決勝：フリートウッドが本拠地でニューカッスルと激突；マンC対ブレントフォード、パレス対リヴァプール。",
            "week1Closed": "NFL第8週TNF試合終了：パッカーズがランボー・フィールドでパンサーズを27-17で撃破",
            "week1Sub": "ジョーダン・ラヴが2TDパスを決め、ジェイコブズが94ヤード獲得で6勝2敗。日曜日は6戦全勝バイキングスが登場。",
            "countdownTnf": "第8週日曜展望：6勝0敗バイキングスが無敗死守へ。パッカーズ（6勝2敗）はTNFでパンサーズに快勝。",
            "barsPoints": "首位との差を示すバー。アントネッリは365点でラッセル（242点）に123点差。メキシコでP9獲得なら即戴冠。",
            "tableAfterMonday": "プレミアリーグ第9節：アーセナルとマンCが勝ち点21で首位タイ。土曜日にエミレーツでアーセナル対リヴァプール。",
            "pinClub": "クラブを選択。マンCとアーセナルが勝ち点21で首位タイ。フリートウッドがニューカッスルと対戦へ。",
            "plFootnote": "カラバオ杯準々決勝：フリートウッド対ニューカッスル、マンC対ブレントフォード、パレス対リヴァプール、トッテナム対サウサンプトン。",
            "majorsDone": "ヴィダンタワールド・メキシコオープン第2R：スモザーマンが通算11アンダー（131）で首位；ペレダとライが9アンダー追走。",
            "wnbaFirstRound": "WNBAファイナル第6戦試合終了：ヴァルキリーズがドリームを76-71で破り、参入初年度での歴史的完全優勝を達成。",
            "bracketFootnote": "第1戦: ヴァルキリーズ 68-64。第2戦: ドリーム 79-65。第3戦: ドリーム 97-71。第4戦: ヴァルキリーズ 67-62。第5戦: ヴァルキリーズ 64-55。第6戦: ヴァルキリーズ 76-71（ヴァルキリーズ4勝2敗で制覇）。"
        }
    },
    "ko": {
        "soccer": {
            "tagline": "카라바오컵 8강 대진 완성: 4부 플리트우드 타운, 안방서 뉴캐슬 영접; 프리미어리그는 아스널 대 리버풀 격돌.",
            "liveNow": "카라바오컵 8강: 플리트우드 대 뉴캐슬, 맨시티 대 브렌트퍼드, 팰리스 대 리버풀. 토요일: 아스널 대 리버풀 빅매치.",
            "pulse": "카라바오컵 8강 대진: 플리트우드 타운 안방에서 뉴캐슬과 꿈의 격돌",
            "keywords": "카라바오컵, 8강 대진, 플리트우드, 뉴캐슬, 아스널, 리버풀, 에미레이츠"
        },
        "basketball": {
            "tagline": "WNBA 챔피언 등극: 골든스테이트 발키리스, 6차전서 드림 76-71 꺾고 창단 첫해 역사적 우승 완성.",
            "liveNow": "WNBA 파이널 6차전 경기 종료: 발키리스 76, 드림 71 (시리즈 4-2 우승). 개비 윌리엄스 파이널 MVP(21점), 손튼 쐐기 3점포.",
            "pulse": "창단 첫해 기적의 챔피언: 골든스테이트 발키리스 2026 WNBA 우승",
            "keywords": "WNBA 파이널, 6차전, 챔피언, 발키리스, 개비 윌리엄스, 엔젤 리스, 드림, 우승"
        },
        "football": {
            "tagline": "패커스, TNF서 팬서스 27-17 제압: 조던 러브 터치다운 2개 작렬하며 그린베이 6승 2패 질주.",
            "liveNow": "TNF 최종 결과: 램보 필드서 패커스 27, 팬서스 17. 제이콥스 94야드, 게리 2색. 일요일: 6전 전승 바이킹스 출격.",
            "pulse": "TNF 경기 결과: 그린베이 패커스, 램보 필드서 캐롤라이나 27-17 제압",
            "keywords": "NFL 8주차, TNF, 패커스, 팬서스, 조던 러브, 조슈아 제이콥스, 램보 필드, 바이킹스"
        },
        "tennis": {
            "tagline": "빈 8강: 알카라스, 드레이퍼 6-4, 6-4 완파하고 토요일 준결승서 츠베레프와 맞대결.",
            "liveNow": "에르스테 방크 오픈 8강: 알카라스 2-0 드레이퍼(위너 29개). 츠베레프 2-0 루블료프 제압. 토요일 준결승 알카라스 대 츠베레프.",
            "pulse": "에르스테 방크 오픈: 알카라스와 츠베레프 준결승 맞대결 성사",
            "keywords": "ATP, 빈, 에르스테 방크 오픈, 알카라스, 드레이퍼, 츠베레프, 루블료프, 준결승"
        },
        "f1": {
            "tagline": "F1 멕시코 GP 연습주행: 안토넬리, FP2서 1분 17초 342로 1위 찍으며 챔피언 등극 초읽기.",
            "liveNow": "멕시코 FP2 결과: 안토넬리 1:17.342(1위), 르클레르 +0.112(2위), 베르스타펜 +0.148(3위). 일요일 결선 9위면 타이틀 확정.",
            "pulse": "F1 멕시코 GP: 키미 안토넬리 고지대 FP2서 1위 질주하며 타이틀 눈앞",
            "keywords": "F1, 멕시코 GP, 안토넬리, FP2, 르클레르, 베르스타펜, 로드리게스 서킷"
        },
        "golf": {
            "tagline": "멕시코 오픈 2R: 스모더맨 65타 몰아치며 11언더파 선두; 페레다와 라이가 9언더파로 추격.",
            "liveNow": "비단타 바야르타 2라운드: 스모더맨 -11(66-65, 131) 2타 차 선두, 페레다(-9)와 라이(-9) 공동 2위. 컷 -1.",
            "pulse": "PGA 투어 멕시코 오픈: 스모더맨 보기 없이 11언더파 36홀 단독 선두 질주",
            "keywords": "PGA 투어, 멕시코 오픈, 스모더맨, 페레다, 라이, 비단타 바야르타, 36홀 단독 선두"
        },
        "home": {
            "tonight": "금요일 데스크",
            "tonightBlurb": "발키리스가 파이널 6차전서 승리하며 WNBA 챔피언에 올랐다. 패커스는 TNF서 팬서스를 27-17로 격파. 안토넬리 멕시코 연습주행 1위.",
            "plTitle": "카라바오컵 8강 추첨 결과: 4부 플리트우드 타운, 안방서 뉴캐슬과 격돌",
            "plBlurb": "4부 리그 돌풍의 팀 홈에서 뉴캐슬 영접; 맨시티는 브렌트퍼드 상대, 리버풀은 팰리스 원정 앞두고 주말 아스널전 준비.",
            "f1Title": "F1 멕시코 GP: 안토넬리, 챔피언 등극 앞두고 금요일 연습주행 1위",
            "f1Blurb": "메르세데스 신성이 해발 2285m 고지대서 1분 17초 342 기록; 일요일 결선 9위만 달성해도 역대 최연소 월드 챔피언 확정."
        },
        "pg": {
            "pinFinal": "카라바오컵 8강 대진: 플리트우드 타운 안방서 뉴캐슬 맞이; 맨시티 대 브렌트퍼드, 팰리스 대 리버풀.",
            "week1Closed": "NFL 8주차 TNF 최종: 패커스가 램보 필드서 팬서스를 27-17로 제압",
            "week1Sub": "조던 러브 2개 TD 패스, 제이콥스 94야드 러싱으로 그린베이 6승 2패 달성. 일요일 6승 무패 바이킹스 출격.",
            "countdownTnf": "8주차 일요일 전망: 6승 무패 바이킹스 무패 행진 도전. 패커스(6승 2패)는 TNF서 팬서스를 27-17로 완파.",
            "barsPoints": "선두와의 격차를 보여주는 막대. 안토넬리는 365점으로 러셀(242점)에 123점 앞서 있다. 멕시코 9위면 타이틀 확정.",
            "tableAfterMonday": "프리미어리그 9라운드: 아스널과 맨시티 승점 21로 공동 1위. 토요일 에미레이츠 스타디움서 아스널 대 리버풀 격돌.",
            "pinClub": "클럽을 선택하세요. 맨시티와 아스널 승점 21로 선두. 플리트우드 타운은 리그컵 8강서 뉴캐슬과 맞대결.",
            "plFootnote": "카라바오컵 8강 대진: 플리트우드 대 뉴캐슬, 맨시티 대 브렌트퍼드, 팰리스 대 리버풀, 토트넘 대 사우샘프턴.",
            "majorsDone": "비단타월드 멕시코 오픈 2R: 스모더맨이 11언더파 131타로 선두; 페레다와 라이가 9언더파로 추격.",
            "wnbaFirstRound": "WNBA 파이널 6차전 최종: 발키리스가 드림을 76-71로 꺾고 창단 첫 시즌에 역사적인 챔피언 트로피를 차지했다.",
            "bracketFootnote": "1차전: 발키리스 68-64. 2차전: 드림 79-65. 3차전: 드림 97-71. 4차전: 발키리스 67-62. 5차전: 발키리스 64-55. 6차전: 발키리스 76-71 (발키리스 4승 2패 우승)."
        }
    },
    "ar": {
        "soccer": {
            "tagline": "اكتمال قرعة ربع نهائي كأس الرابطة: فليتوود تاون يستضيف نيوكاسل في هايبوري؛ وقمة نارية بين أرسنال وليفربول السبت.",
            "liveNow": "قرعة كأس الرابطة: فليتوود ضد نيوكاسل، مان سيتي ضد برينتفورد، بالاس ضد ليفربول. السبت: قمة أرسنال وليفربول في الدوري.",
            "pulse": "قرعة ربع نهائي كأس الرابطة: فليتوود تاون يحصل على مواجهة تاريخية أمام نيوكاسل",
            "keywords": "كأس الرابطة, قرعة ربع النهائي, فليتوود تاون, نيوكاسل, أرسنال, ليفربول, ملعب الإمارات"
        },
        "basketball": {
            "tagline": "بطلات دوري WNBA: غولدن ستيت فالكيريز يتغلب على دريم 76-71 في المباراة 6 ويحقق لقبا إعجازيا في أول مواسمه.",
            "liveNow": "نهائي WNBA المباراة 6 النهائي: فالكيريز 76، دريم 71 (السلسلة 4-2). غابي ويليامز أفضل لاعبة في النهائي بـ 21 نقطة، وثلاثية قاتلة لثورنتون.",
            "pulse": "إنجاز رياضي تاريخي: غولدن ستيت فالكيريز بطلا لدوري WNBA 2026 في عامه الأول",
            "keywords": "نهائي WNBA, المباراة 6, بطلات, فالكيريز, غابي ويليامز, أنجيل ريس, دريم, تتويج"
        },
        "football": {
            "tagline": "باكرز يتغلب على بانثرز 27-17 في مباراة الخميس: جوردان لوف يمرر كرتي هبوط ليرفع رصيد غرين باي إلى 6-2.",
            "liveNow": "مباراة ليلة الخميس النهائي: باكرز 27، بانثرز 17 في لامبو فيلد. جاكوبس 94 ياردة، وغاري يحقق إسقاطين. الأحد: فايكنغز (6-0) دون هزيمة.",
            "pulse": "مباراة ليلة الخميس: غرين باي يحكم قبضته ويهزم كارولاينا 27-17 في ويسكونسن",
            "keywords": "دوري NFL الأسبوع 8, TNF, باكرز, بانثرز, جوردان لوف, جوش جاكوبس, لامبو فيلد, فايكنغز"
        },
        "tennis": {
            "tagline": "بطولة فيينا ربع النهائي: ألكاراز يكتسح دريبر 6-4 و6-4 ويتأهل لقمة نصف النهائي يوم السبت أمام زفيريف.",
            "liveNow": "بطولة بنك إيرستيه ربع النهائي: ألكاراز يهزم دريبر 6-4 و6-4 (29 ضربة قاضية). زفيريف يتجاوز روبليف 7-6 و6-4. نصف نهائي السبت: ألكاراز ضد زفيريف.",
            "pulse": "بطولة بنك إيرستيه المفتوحة: ألكاراز وزفيريف في نصف نهائي مرتقب وناري في فيينا",
            "keywords": "تنس, فيينا, بنك إيرستيه المفتوحة, ألكاراز, دريبر, زفيريف, روبليف, نصف النهائي"
        },
        "f1": {
            "tagline": "جائزة المكسيك الكبرى التجارب الحرة: أنتونيللي يسجل الزمن الأسرع 1:17.342 في حصة التجارب الثانية نحو اللقب.",
            "liveNow": "التجارب الثانية في المكسيك: أنتونيللي 1:17.342 (المركز 1)، لوكلير +0.112 (المركز 2)، فيرستابن +0.148 (المركز 3). المركز 9 الأحد يحسم اللقب.",
            "pulse": "جائزة المكسيك الكبرى: أنتونيللي يتصدر التجارب الحرة الثانية على ارتفاع شاهق",
            "keywords": "فورمولا 1, جائزة المكسيك, أنتونيللي, التجارب 2, لوكلير, فيرستابن, حلبة هيرمانوس رودريغيز"
        },
        "golf": {
            "tagline": "بطولة فيدانتا وورلد المكسيك المفتوحة الجولة 2: سموذر مان يسجل 65 لينفرد بالصدارة بـ 11 تحت المعدل؛ وبيريدا وراي يلاحقانه.",
            "liveNow": "الجولة 2 في فيدانتا فايارتا: سموذر مان -11 (66-65، 131) يتصدر بفارق ضربتين عن بيريدا (-9) وراي (-9). معدل التأهل عند -1.",
            "pulse": "جولة بي جي إيه بطولة المكسيك المفتوحة: سموذر مان ينفرد بالصدارة بمجموع 11 تحت المعدل",
            "keywords": "جولة بي جي إيه, بطولة المكسيك المفتوحة, سموذر مان, بيريدا, راي, فيدانتا فايارتا, صدارة 36 حفرة"
        },
        "home": {
            "tonight": "مكتب الجمعة",
            "tonightBlurb": "تتويج تاريخي لفالكيريز بلقب WNBA في المباراة 6. باكرز يهزم بانثرز 27-17 في مباراة ليلة الخميس. أنتونيللي يتصدر تجارب المكسيك.",
            "plTitle": "قرعة كأس الرابطة: فليتوود تاون يحظى بمواجهة الحلم أمام نيوكاسل يونايتد",
            "plBlurb": "فريق الدرجة الرابعة يستضيف نيوكاسل في هايبوري؛ مان سيتي يلتقي برينتفورد وليفربول يواجه كريستال بالاس قبل قمة السبت.",
            "f1Title": "جائزة المكسيك الكبرى: أنتونيللي يسجل الزمن الأسرع في التجارب تمهيدا للتتويج",
            "f1Blurb": "سائق مرسيدس الإيطالي يسجل 1:17.342 على ارتفاع 2285 مترا؛ ويكفيه المركز التاسع يوم الأحد ليصبح أصغر بطل عالم."
        },
        "pg": {
            "pinFinal": "قرعة ربع نهائي كأس الرابطة: فليتوود تاون يستضيف نيوكاسل في هايبوري؛ وسيتي يواجه برينتفورد، وليفربول يلعب ضد بالاس.",
            "week1Closed": "دوري كرة القدم الأمريكية الأسبوع 8: باكرز يتفوق على بانثرز 27-17 في ملعب لامبو فيلد",
            "week1Sub": "جوردان لوف يسجل تمريرتي هبوط وجاكوبس يركض لمسافة 94 ياردة ليصل باكرز إلى 6-2. الأحد: فايكنغز بسجل 6-0.",
            "countdownTnf": "نظرة على مباريات الأحد: فايكنغز (6-0) يدافع عن سجله الخالي من الهزائم. باكرز (6-2) يتغلب على بانثرز 27-17 في مباراة الخميس.",
            "barsPoints": "الأشرطة توضح الفارق عن المتصدر. أنتونيللي لديه 365 نقطة بفارق 123 عن راسل (242). المركز التاسع في المكسيك يحسم اللقب.",
            "tableAfterMonday": "الدوري الإنجليزي الممتاز الجولة 9: أرسنال وسيتي في الصدارة بـ 21 نقطة (7-0-1). قمة أرسنال وليفربول يوم السبت.",
            "pinClub": "اختر ناديا. سيتي وأرسنال في الصدارة بـ 21 نقطة. فليتوود تاون يواجه نيوكاسل في ربع نهائي كأس الرابطة.",
            "plFootnote": "قرعة ربع نهائي كأس الرابطة: فليتوود ضد نيوكاسل، مان سيتي ضد برينتفورد، بالاس ضد ليفربول، توتنهام ضد ساوثهامبتون.",
            "majorsDone": "بطولة المكسيك المفتوحة الجولة 2: سموذر مان يتصدر بـ 11 ضربة تحت المعدل (131)؛ وبيريدا وراي يطاردانه بـ -9.",
            "wnbaFirstRound": "نهائي دوري WNBA المباراة 6 النهائي: فالكيريز يهزم دريم 76-71 ويتوج باللقب التاريخي الأول في عامه التأسيسي.",
            "bracketFootnote": "م 1: فالكيريز 68-64. م 2: دريم 79-65. م 3: دريم 97-71. م 4: فالكيريز 67-62. م 5: فالكيريز 64-55. م 6: فالكيريز 76-71 (فوز فالكيريز 4-2)."
        }
    }
}

# 1. Update frontend/src/i18n/playground.ts
pg_file = "frontend/src/i18n/playground.ts"
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
msg_file = "frontend/src/i18n/messages.ts"
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
    lang_file = f"frontend/src/i18n/messages-{lang}.ts"
    with open(lang_file, "r", encoding="utf-8") as f:
        l_content = f.read()
    l_content = update_messages_dict(l_content, lang)
    with open(lang_file, "w", encoding="utf-8") as f:
        f.write(l_content)
    print(f"Updated {lang_file}")

print("All locale updates for 30 Oct 2026 completed successfully!")
