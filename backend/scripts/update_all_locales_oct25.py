# -*- coding: utf-8 -*-
import re
import os

DATA = {
    "en": {
        "f1": {
            "tagline": "United States GP race day at COTA: Antonelli starts on pole as Ferrari and Verstappen chase.",
            "liveNow": "Austin Sunday 15:00 local: 56 laps at COTA. Antonelli on pole (1:34.035) ahead of Verstappen (+0.179s). Antonelli leads championship by 102.",
            "pulse": "RACE DAY: ANTONELLI LEADS FROM POLE IN TEXAS",
            "keywords": "Formula 1, United States GP, Austin, COTA, Antonelli, Verstappen, Leclerc, Race Day"
        },
        "tennis": {
            "tagline": "Almaty final: Medvedev rallies past Basilashvili 6-7, 6-1, 6-3 to defend his title.",
            "liveNow": "Almaty Final: Medvedev d. Basilashvili 6-7(6), 6-1, 6-3 in 1h 53m. 25th career title and first career title defense for Medvedev.",
            "pulse": "ALMATY FINAL: MEDVEDEV DEFENDS TITLE IN THREE SETS",
            "keywords": "ATP, Almaty, Medvedev, Basilashvili, final, title defense, 25th title"
        },
        "football": {
            "tagline": "NFL Week 7 Sunday: Unbeaten Chiefs, 49ers and Vikings put perfect marks on the line.",
            "liveNow": "Sunday Week 7: 49ers (6-0) at Falcons, Colts at Vikings (5-0), Chiefs (5-0) at Seahawks (SNF). Bears sit 5-2 after TNF win.",
            "pulse": "NFL WEEK 7: UNBEATEN TRIO TESTED SUNDAY",
            "keywords": "NFL Week 7, Chiefs, 49ers, Vikings, Bears, Sunday slate, SNF"
        },
        "soccer": {
            "tagline": "Premier League shocks: Spurs stun Chelsea 2-0; Villa topple City 2-1 as Arsenal go level top.",
            "liveNow": "MW8: Spurs 2, Chelsea 0; Villa 2, City 1; Arsenal 2, Everton 0. City and Arsenal tied on 21 pts (7-0-1). Sunday: Liverpool 2, Brighton 0.",
            "pulse": "PREMIER LEAGUE: SPURS AND VILLA DELIVER SATURDAY SHOCKS",
            "keywords": "Premier League, Spurs, Chelsea, Villa, City, Arsenal, MW8"
        },
        "basketball": {
            "tagline": "WNBA Finals Game 4: Valkyries stifle Dream 67-62 to level series 2-2 and force Game 5.",
            "liveNow": "Game 4 Final: Valkyries 67, Dream 62. Williams 17 pts, Stokes defense halts Reese streak. Series tied 2-2 heading to San Francisco.",
            "pulse": "WNBA FINALS: VALKYRIES FORCE GAME 5 IN SAN FRANCISCO",
            "keywords": "WNBA Finals, Game 4, Valkyries, Dream, Williams, Reese, Game 5, 2-2"
        },
        "golf": {
            "tagline": "Bermuda final round: Power and Smotherman share 54-hole lead; Blanchet and Hirata in chase.",
            "liveNow": "Butterfield Bermuda Final Round: Power and Smotherman co-lead after 54 holes. Blanchet and Hirata chase at Port Royal, par 71.",
            "pulse": "PORT ROYAL FINAL ROUND: POWER AND SMOTHERMAN CO-LEAD",
            "keywords": "PGA Tour, Bermuda, Port Royal, Power, Smotherman, Blanchet, Hirata, Final Round"
        },
        "home": {
            "tonight": "Sunday desk",
            "tonightBlurb": "Antonelli starts on pole at COTA. Medvedev defends Almaty Open crown. Spurs and Villa rock the Premier League. Valkyries force Game 5.",
            "plTitle": "Premier League: Spurs stun Chelsea 2-0 and Villa shock City 2-1 as Arsenal go level top",
            "plBlurb": "Tottenham won at Stamford Bridge for first time since 2018. City suffered their first league loss (21 pts), joining Arsenal at the summit.",
            "f1Title": "United States GP: Race day at COTA",
            "f1Blurb": "Kimi Antonelli starts from pole position (1:34.035) with Max Verstappen alongside. Lights out Sunday at 15:00 local."
        },
        "pg": {
            "pinFinal": "Almaty Final: Medvedev d. Basilashvili 6-7(6), 6-1, 6-3 in 1h 53m. 25th career title and first career title defense for Medvedev.",
            "week1Closed": "NFL Week 7 TNF final: Bears edge Patriots 30-24 at Soldier Field",
            "week1Sub": "Williams 308 pass yds, 2 TD; Burden 130 rec yds; Santos 58-yd FG. Bears 5-2, Patriots 4-3. 49ers stand 6-0.",
            "countdownTnf": "TNF Final: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs and Vikings 5-0. Bills 5-1.",
            "barsPoints": "Bars show the gap to the leader. Antonelli has 340, 102 ahead of Russell on 238. Antonelli starts on pole at COTA.",
            "tableAfterMonday": "Premier League: City and Arsenal tied on 21 points (7-0-1). Villa beat City 2-1; Spurs beat Chelsea 2-0.",
            "pinClub": "Select a club. City and Arsenal are 7-0-1 on 21. Chelsea 13, Villa 11, Spurs 9. Tottenham beat Chelsea 2-0 at the Bridge.",
            "plFootnote": "Saturday: Spurs 2, Chelsea 0; Villa 2, City 1; Arsenal 2, Everton 0. Sunday: Liverpool 2, Brighton 0; Bournemouth 3, Man Utd 0.",
            "majorsDone": "Butterfield Bermuda Final Round underway. Seamus Power and Austin Smotherman co-lead after 54 holes (-14). Blanchet, Hirata trail by 1.",
            "wnbaFirstRound": "WNBA Finals Game 4: Valkyries stun Dream 67-62 to level series 2-2. Gabby Williams 17 pts; Reese held to 8 pts. Game 5 in San Francisco.",
            "bracketFootnote": "Game 1: Valkyries 68, Dream 64. Game 2: Dream 79, Valkyries 65. Game 3: Dream 97, Valkyries 71. Game 4: Valkyries 67, Dream 62. Series tied 2-2."
        }
    },
    "fr": {
        "f1": {
            "tagline": "GP des Etats-Unis jour de course au COTA : Antonelli en pole devant Verstappen et les Ferrari.",
            "liveNow": "Austin dimanche 15h00 locale : 56 tours au COTA. Antonelli en pole (1:34.035) devant Verstappen (+0.179s). Antonelli mene de 102 points.",
            "pulse": "JOUR DE COURSE : ANTONELLI EN POLE AU TEXAS",
            "keywords": "Formule 1, GP des Etats-Unis, Austin, COTA, Antonelli, Verstappen, Leclerc, jour de course"
        },
        "tennis": {
            "tagline": "Finale d'Almaty : Medvedev renverse Basilashvili 6-7, 6-1, 6-3 et conserve son titre.",
            "liveNow": "Finale Almaty : Medvedev bat Basilashvili 6-7(6), 6-1, 6-3 en 1h53. 25e titre en carriere et premier titre conserve pour Medvedev.",
            "pulse": "FINALE ALMATY : MEDVEDEV CONSERVE SON TITRE EN TROIS MANCHES",
            "keywords": "ATP, Almaty, Medvedev, Basilashvili, finale, titre conserve, 25e titre"
        },
        "football": {
            "tagline": "NFL semaine 7 dimanche : Chiefs, 49ers et Vikings invaincus mettent leur serie en jeu.",
            "liveNow": "Dimanche semaine 7 : 49ers (6-0) chez les Falcons, Colts chez les Vikings (5-0), Chiefs (5-0) chez les Seahawks (SNF). Bears a 5-2.",
            "pulse": "NFL SEMAINE 7 : LE TRIO D'INVAINCUS AU DEFI DU DIMANCHE",
            "keywords": "NFL semaine 7, Chiefs, 49ers, Vikings, Bears, affiches de dimanche, SNF"
        },
        "soccer": {
            "tagline": "Secousses en Premier League : les Spurs surprennent Chelsea 2-0, Villa bat City 2-1, Arsenal co-leader.",
            "liveNow": "8e journee : Spurs 2, Chelsea 0 ; Villa 2, City 1 ; Arsenal 2, Everton 0. City et Arsenal en tete a 21 pts (7-0-1).",
            "pulse": "PREMIER LEAGUE : LES SPURS ET VILLA FRAPPENT UN GRAND COUP",
            "keywords": "Premier League, Spurs, Chelsea, Villa, City, Arsenal, 8e journee"
        },
        "basketball": {
            "tagline": "Finales WNBA match 4 : les Valkyries domptent le Dream 67-62, egalisent a 2-2 et arrachent le match 5.",
            "liveNow": "Match 4 final : Valkyries 67, Dream 62. Williams 17 pts, la defense neutralise Reese. Egalite 2-2, match 5 a San Francisco.",
            "pulse": "FINALES WNBA : LES VALKYRIES ARRACHENT UN MATCH 5 DECISIF",
            "keywords": "WNBA Finales, match 4, Valkyries, Dream, Williams, Reese, match 5, 2-2"
        },
        "golf": {
            "tagline": "Dernier tour aux Bermudes : Power et Smotherman co-leaders apres 54 trous, Blanchet et Hirata a l'affut.",
            "liveNow": "Butterfield Bermuda tour final : Power et Smotherman co-leaders a -14. Blanchet et Hirata a un coup a Port Royal, par 71.",
            "pulse": "PORT ROYAL TOUR FINAL : POWER ET SMOTHERMAN CO-LEADERS",
            "keywords": "PGA Tour, Bermudes, Port Royal, Power, Smotherman, Blanchet, Hirata, tour final"
        },
        "home": {
            "tonight": "Bureau du dimanche",
            "tonightBlurb": "Antonelli en pole au COTA. Medvedev conserve sa couronne a Almaty. Les Spurs et Villa secouent la Premier League. Les Valkyries forcent un match 5.",
            "plTitle": "Premier League : les Spurs surprennent Chelsea 2-0, Villa fait tomber City 2-1",
            "plBlurb": "Tottenham s'impose a Stamford Bridge pour la premiere fois depuis 2018. City battu (21 pts), Arsenal revient a hauteur en tete.",
            "f1Title": "GP des Etats-Unis : jour de course au COTA",
            "f1Blurb": "Kimi Antonelli s'elance en pole position (1:34.035) aux cotes de Max Verstappen. Depart dimanche a 15h00 locale."
        },
        "pg": {
            "pinFinal": "Finale Almaty : Medvedev bat Basilashvili 6-7(6), 6-1, 6-3 en 1h53. 25e titre et premier sacre conserve de sa carriere.",
            "week1Closed": "NFL semaine 7 TNF termine : les Bears dominent les Patriots 30-24 a Soldier Field",
            "week1Sub": "Williams 308 yds a la passe, 2 TD ; Burden 130 yds a la reception ; Santos FG de 58 yds. Bears 5-2, Patriots 4-3. 49ers a 6-0.",
            "countdownTnf": "Final TNF : Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs et Vikings 5-0. Bills 5-1.",
            "barsPoints": "Les barres indiquent l'ecart avec le leader. Antonelli compte 340 points, 102 devant Russell a 238. Antonelli part en pole a Austin.",
            "tableAfterMonday": "Premier League : City et Arsenal a egalite en tete a 21 points (7-0-1). Villa bat City 2-1 ; Spurs battent Chelsea 2-0.",
            "pinClub": "Selectionnez un club. City et Arsenal a 7-0-1 avec 21 pts. Chelsea 13, Villa 11, Spurs 9. Les Spurs s'imposent au Bridge 2-0.",
            "plFootnote": "Samedi : Spurs 2, Chelsea 0 ; Villa 2, City 1 ; Arsenal 2, Everton 0. Dimanche : Liverpool 2, Brighton 0 ; Bournemouth 3, Man Utd 0.",
            "majorsDone": "Butterfield Bermuda tour final en cours. Seamus Power et Austin Smotherman co-leaders apres 54 trous (-14). Blanchet et Hirata a 1 coup.",
            "wnbaFirstRound": "Finales WNBA match 4 : les Valkyries dominent le Dream 67-62 et egalisent a 2-2. Gabby Williams 17 pts. Match 5 a San Francisco.",
            "bracketFootnote": "Match 1 : Valkyries 68, Dream 64. Match 2 : Dream 79, Valkyries 65. Match 3 : Dream 97, Valkyries 71. Match 4 : Valkyries 67, Dream 62. Egalite 2-2."
        }
    },
    "es": {
        "f1": {
            "tagline": "Dia de carrera del GP de Estados Unidos en COTA: Antonelli arranca en pole con Verstappen al acecho.",
            "liveNow": "Austin domingo 15:00 local: 56 vueltas en COTA. Antonelli en pole (1:34.035) por delante de Verstappen (+0.179s). Ventaja de 102 puntos.",
            "pulse": "DIA DE CARRERA: ANTONELLI PARTE DESDE LA POLE EN TEXAS",
            "keywords": "Formula 1, GP de Estados Unidos, Austin, COTA, Antonelli, Verstappen, Leclerc, dia de carrera"
        },
        "tennis": {
            "tagline": "Final de Almaty: Medvedev remonta ante Basilashvili 6-7, 6-1, 6-3 y defiende su corona.",
            "liveNow": "Final Almaty: Medvedev a Basilashvili 6-7(6), 6-1, 6-3 en 1h 53m. 25° titulo en su carrera y primera defensa exitosa.",
            "pulse": "FINAL ALMATY: MEDVEDEV DEFIENDE SU TITULO EN TRES SETS",
            "keywords": "ATP, Almaty, Medvedev, Basilashvili, final, defensa de titulo, 25° titulo"
        },
        "football": {
            "tagline": "NFL Semana 7 domingo: Invictos Chiefs, 49ers y Vikings arriesgan su marcha perfecta.",
            "liveNow": "Domingo Semana 7: 49ers (6-0) en Falcons, Colts en Vikings (5-0), Chiefs (5-0) en Seahawks (SNF). Bears 5-2.",
            "pulse": "NFL SEMANA 7: EL TRIO DE INVICTOS A PRUEBA EL DOMINGO",
            "keywords": "NFL Semana 7, Chiefs, 49ers, Vikings, Bears, cartelera de domingo, SNF"
        },
        "soccer": {
            "tagline": "Sorpresas en Premier League: Spurs frenan 2-0 a Chelsea, Villa tumba 2-1 a City y Arsenal iguala la cima.",
            "liveNow": "Jornada 8: Spurs 2, Chelsea 0; Villa 2, City 1; Arsenal 2, Everton 0. City y Arsenal empatados en 21 pts (7-0-1).",
            "pulse": "PREMIER LEAGUE: SPURS Y VILLA PROTAGONIZAN GRANDES SORPRESAS",
            "keywords": "Premier League, Spurs, Chelsea, Villa, City, Arsenal, Jornada 8"
        },
        "basketball": {
            "tagline": "Finales WNBA Juego 4: Valkyries superan 67-62 a Dream, empatan la serie 2-2 y fuerzan el Juego 5.",
            "liveNow": "Juego 4 Final: Valkyries 67, Dream 62. Williams 17 pts, defensa frena a Reese. Serie igualada 2-2 rumbo a San Francisco.",
            "pulse": "FINALES WNBA: VALKYRIES FUERZAN EL QUINTO JUEGO EN SAN FRANCISCO",
            "keywords": "WNBA Finales, Juego 4, Valkyries, Dream, Williams, Reese, Juego 5, 2-2"
        },
        "golf": {
            "tagline": "Ronda final en Bermudas: Power y Smotherman comparten el liderato tras 54 hoyos; Blanchet e Hirata al acecho.",
            "liveNow": "Butterfield Bermuda Ronda Final: Power y Smotherman co-lideran con -14. Blanchet e Hirata a un golpe en Port Royal, par 71.",
            "pulse": "PORT ROYAL RONDA FINAL: POWER Y SMOTHERMAN CO-LIDERES",
            "keywords": "PGA Tour, Bermudas, Port Royal, Power, Smotherman, Blanchet, Hirata, Ronda Final"
        },
        "home": {
            "tonight": "Mesa del domingo",
            "tonightBlurb": "Antonelli arranca en pole en COTA. Medvedev retiene su corona en Almaty. Spurs y Villa sacuden la Premier League. Valkyries fuerzan el Juego 5.",
            "plTitle": "Premier League: Spurs sorprenden 2-0 a Chelsea y Villa tumba 2-1 al City",
            "plBlurb": "Tottenham gana en Stamford Bridge por primera vez desde 2018. City sufre su primer tropiezo (21 pts), igualado con Arsenal.",
            "f1Title": "GP de Estados Unidos: dia de carrera en COTA",
            "f1Blurb": "Kimi Antonelli parte desde la pole position (1:34.035) junto a Max Verstappen. Luces fuera el domingo a las 15:00 local."
        },
        "pg": {
            "pinFinal": "Final Almaty: Medvedev a Basilashvili 6-7(6), 6-1, 6-3 en 1h 53m. 25° titulo y primera defensa de titulo en su carrera.",
            "week1Closed": "NFL Semana 7 final TNF: Bears superan 30-24 a los Patriots en Soldier Field",
            "week1Sub": "Williams 308 yds pase, 2 TD; Burden 130 yds recepcion; Santos FG de 58 yds. Bears 5-2, Patriots 4-3. 49ers estan 6-0.",
            "countdownTnf": "Final TNF: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs y Vikings 5-0. Bills 5-1.",
            "barsPoints": "Las barras muestran la ventaja con el lider. Antonelli suma 340, 102 mas que Russell (238). Antonelli parte en pole en Austin.",
            "tableAfterMonday": "Premier League: City y Arsenal empatados en 21 puntos (7-0-1). Villa vencio a City 2-1; Spurs a Chelsea 2-0.",
            "pinClub": "Seleccione un club. City y Arsenal con 7-0-1 y 21 pts. Chelsea 13, Villa 11, Spurs 9. Spurs ganaron 2-0 en Stamford Bridge.",
            "plFootnote": "Sabado: Spurs 2, Chelsea 0; Villa 2, City 1; Arsenal 2, Everton 0. Domingo: Liverpool 2, Brighton 0; Bournemouth 3, Man Utd 0.",
            "majorsDone": "Butterfield Bermuda Ronda Final en marcha. Seamus Power y Austin Smotherman co-lideran tras 54 hoyos (-14). Blanchet e Hirata a 1.",
            "wnbaFirstRound": "Finales WNBA Juego 4: Valkyries vencen 67-62 a Dream y empatan la serie 2-2. Gabby Williams 17 pts. Juego 5 en San Francisco.",
            "bracketFootnote": "Juego 1: Valkyries 68, Dream 64. Juego 2: Dream 79, Valkyries 65. Juego 3: Dream 97, Valkyries 71. Juego 4: Valkyries 67, Dream 62. Serie 2-2."
        }
    },
    "de": {
        "f1": {
            "tagline": "GP der USA Renntag am COTA: Antonelli startet von der Pole, Verstappen und Ferrari jagen ihn.",
            "liveNow": "Austin Sonntag 15:00 Ortszeit: 56 Runden am COTA. Antonelli auf Pole (1:34.035) vor Verstappen (+0.179s). Antonelli fuehrt mit 102 Punkten.",
            "pulse": "RENNTAG: ANTONELLI STARTET VON DER POLE IN TEXAS",
            "keywords": "Formel 1, GP USA, Austin, COTA, Antonelli, Verstappen, Leclerc, Renntag"
        },
        "tennis": {
            "tagline": "Almaty-Finale: Medvedev dreht Match gegen Basilashvili 6-7, 6-1, 6-3 und verteidigt Titel.",
            "liveNow": "Almaty Finale: Medvedev d. Basilashvili 6-7(6), 6-1, 6-3 in 1h 53m. 25. Karrieretitel und erste erfolgreiche Titelverteidigung.",
            "pulse": "ALMATY FINALE: MEDVEDEV VERTEIDIGT TITEL IN DREI SAETZEN",
            "keywords": "ATP, Almaty, Medvedev, Basilashvili, Finale, Titelverteidigung, 25. Titel"
        },
        "football": {
            "tagline": "NFL Woche 7 Sonntag: Ungeschlagene Chiefs, 49ers und Vikings setzen makellose Bilanzen aufs Spiel.",
            "liveNow": "Sonntag Woche 7: 49ers (6-0) bei Falcons, Colts bei Vikings (5-0), Chiefs (5-0) bei Seahawks (SNF). Bears 5-2.",
            "pulse": "NFL WOCHE 7: UNGESCHLAGENES TRIO AM SONNTAG GEFORDERT",
            "keywords": "NFL Woche 7, Chiefs, 49ers, Vikings, Bears, Sonntagsspiele, SNF"
        },
        "soccer": {
            "tagline": "Premier-League-Beben: Spurs ueberraschen Chelsea 2-0, Villa schlaegt City 2-1, Arsenal zieht gleich.",
            "liveNow": "8. Spieltag: Spurs 2, Chelsea 0; Villa 2, City 1; Arsenal 2, Everton 0. City und Arsenal punktgleich vorn mit 21 (7-0-1).",
            "pulse": "PREMIER LEAGUE: SPURS UND VILLA SORGEN FUER SAMSTAGS-SENSATIONEN",
            "keywords": "Premier League, Spurs, Chelsea, Villa, City, Arsenal, 8. Spieltag"
        },
        "basketball": {
            "tagline": "WNBA-Finals Spiel 4: Valkyries ringen Dream 67-62 nieder, stellen auf 2-2 und erzwingen Spiel 5.",
            "liveNow": "Spiel 4 Endstand: Valkyries 67, Dream 62. Williams 17 Pkt, Abwehr stoppt Reese. Serie 2-2, Showdown in San Francisco.",
            "pulse": "WNBA-FINALS: VALKYRIES ERZWINGEN ENTSCHEIDENDES SPIEL 5",
            "keywords": "WNBA Finals, Spiel 4, Valkyries, Dream, Williams, Reese, Spiel 5, 2-2"
        },
        "golf": {
            "tagline": "Finalrunde auf Bermuda: Power und Smotherman teilen 54-Loch-Fuehrung, Blanchet und Hirata lauern.",
            "liveNow": "Butterfield Bermuda Finalrunde: Power und Smotherman gleichauf bei -14. Blanchet und Hirata einen Schlag zurueck in Port Royal.",
            "pulse": "PORT ROYAL FINALRUNDE: POWER UND SMOTHERMAN AN DER SPITZE",
            "keywords": "PGA Tour, Bermuda, Port Royal, Power, Smotherman, Blanchet, Hirata, Finalrunde"
        },
        "home": {
            "tonight": "Sonntags-Desk",
            "tonightBlurb": "Antonelli auf Pole am COTA. Medvedev verteidigt Almaty-Titel. Spurs und Villa schocken Premier League. Valkyries erzwingen Spiel 5.",
            "plTitle": "Premier League: Spurs schlagen Chelsea 2-0, Villa bezwingt City 2-1",
            "plBlurb": "Tottenham gewinnt erstmals seit 2018 an der Stamford Bridge. City kassiert erste Niederlage (21 Pkt), Arsenal schliesst auf.",
            "f1Title": "Grosser Preis der USA: Renntag am COTA",
            "f1Blurb": "Kimi Antonelli startet von der Pole Position (1:34.035) neben Max Verstappen. Rennstart am Sonntag um 15:00 Ortszeit."
        },
        "pg": {
            "pinFinal": "Almaty Finale: Medvedev d. Basilashvili 6-7(6), 6-1, 6-3 in 1h 53m. 25. Karrieretitel und erste erfolgreiche Titelverteidigung.",
            "week1Closed": "NFL Woche 7 TNF-Endstand: Bears schlagen Patriots 30-24 im Soldier Field",
            "week1Sub": "Williams 308 Pass-Yards, 2 TD; Burden 130 Rec-Yards; Santos 58-Yard-FG. Bears 5-2, Patriots 4-3. 49ers stehen 6-0.",
            "countdownTnf": "TNF-Endstand: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs und Vikings 5-0. Bills 5-1.",
            "barsPoints": "Balken zeigen Abstand zum Fuehrenden. Antonelli hat 340, 102 vor Russell (238). Antonelli startet von der Pole in Austin.",
            "tableAfterMonday": "Premier League: City und Arsenal punktgleich an der Spitze mit 21 Punkten (7-0-1). Villa schlaegt City 2-1; Spurs siegen bei Chelsea 2-0.",
            "pinClub": "Klub waehlen. City und Arsenal 7-0-1 mit 21 Pkt. Chelsea 13, Villa 11, Spurs 9. Spurs siegen 2-0 an der Bridge.",
            "plFootnote": "Samstag: Spurs 2, Chelsea 0; Villa 2, City 1; Arsenal 2, Everton 0. Sonntag: Liverpool 2, Brighton 0; Bournemouth 3, Man Utd 0.",
            "majorsDone": "Butterfield Bermuda Finalrunde laeuft. Seamus Power und Austin Smotherman fuehren nach 54 Loch (-14). Blanchet und Hirata 1 Schlag zurueck.",
            "wnbaFirstRound": "WNBA Finals Spiel 4: Valkyries schlagen Dream 67-62 und stellen auf 2-2. Gabby Williams 17 Pkt. Spiel 5 in San Francisco.",
            "bracketFootnote": "Spiel 1: Valkyries 68, Dream 64. Spiel 2: Dream 79, Valkyries 65. Spiel 3: Dream 97, Valkyries 71. Spiel 4: Valkyries 67, Dream 62. Stand 2-2."
        }
    },
    "it": {
        "f1": {
            "tagline": "GP degli Stati Uniti giorno di gara al COTA: Antonelli scatta in pole, Verstappen e Ferrari all'inseguimento.",
            "liveNow": "Austin domenica 15:00 locali: 56 giri al COTA. Antonelli in pole (1:34.035) davanti a Verstappen (+0.179s). Vantaggio di 102 punti.",
            "pulse": "GIORNO DI GARA: ANTONELLI PARTE IN POLE IN TEXAS",
            "keywords": "Formula 1, GP Stati Uniti, Austin, COTA, Antonelli, Verstappen, Leclerc, gara"
        },
        "tennis": {
            "tagline": "Finale Almaty: Medvedev rimonta Basilashvili 6-7, 6-1, 6-3 e difende il titolo.",
            "liveNow": "Finale Almaty: Medvedev b. Basilashvili 6-7(6), 6-1, 6-3 in 1h 53m. 25° titolo in carriera e prima difesa vincente.",
            "pulse": "FINALE ALMATY: MEDVEDEV DIFENDE IL TITOLO IN TRE SET",
            "keywords": "ATP, Almaty, Medvedev, Basilashvili, finale, titolo difeso, 25° titolo"
        },
        "football": {
            "tagline": "NFL Week 7 domenica: Chiefs, 49ers e Vikings imbattuti mettono in palio il percorso netto.",
            "liveNow": "Domenica Week 7: 49ers (6-0) ad Atlanta, Colts a Minnesota (5-0), Chiefs (5-0) a Seattle (SNF). Bears a 5-2.",
            "pulse": "NFL WEEK 7: IL TRIO DI IMBATTUTI ALLA PROVA DELLA DOMENICA",
            "keywords": "NFL Week 7, Chiefs, 49ers, Vikings, Bears, partite domenica, SNF"
        },
        "soccer": {
            "tagline": "Colpi di scena in Premier League: Spurs battono Chelsea 2-0, Villa supera City 2-1, Arsenal aggancia la vetta.",
            "liveNow": "8a giornata: Spurs 2, Chelsea 0; Villa 2, City 1; Arsenal 2, Everton 0. City e Arsenal appaiati a quota 21 (7-0-1).",
            "pulse": "PREMIER LEAGUE: SPURS E VILLA FIRMANO LE IMPRESE DEL SABATO",
            "keywords": "Premier League, Spurs, Chelsea, Villa, City, Arsenal, 8a giornata"
        },
        "basketball": {
            "tagline": "Finals WNBA Gara 4: le Valkyries superano il Dream 67-62, pareggiano la serie 2-2 e forzano Gara 5.",
            "liveNow": "Finale Gara 4: Valkyries 67, Dream 62. Williams 17 punti, difesa argina Reese. Serie sul 2-2, decisiva a San Francisco.",
            "pulse": "FINALS WNBA: LE VALKYRIES TRASCINANO LA SERIE A GARA 5",
            "keywords": "WNBA Finals, Gara 4, Valkyries, Dream, Williams, Reese, Gara 5, 2-2"
        },
        "golf": {
            "tagline": "Giro finale alle Bermuda: Power e Smotherman in vetta dopo 54 buche, Blanchet e Hirata a ridosso.",
            "liveNow": "Butterfield Bermuda giro finale: Power e Smotherman co-leader a -14. Blanchet e Hirata a un colpo a Port Royal, par 71.",
            "pulse": "PORT ROYAL GIRO FINALE: POWER E SMOTHERMAN AL COMANDO",
            "keywords": "PGA Tour, Bermuda, Port Royal, Power, Smotherman, Blanchet, Hirata, giro finale"
        },
        "home": {
            "tonight": "Desk di domenica",
            "tonightBlurb": "Antonelli in pole al COTA. Medvedev difende il trono ad Almaty. Spurs e Villa scuotono la Premier League. Le Valkyries portano le Finals a Gara 5.",
            "plTitle": "Premier League: gli Spurs piegano il Chelsea 2-0, il Villa abbatte il City 2-1",
            "plBlurb": "Tottenham corsaro a Stamford Bridge per la prima volta dal 2018. City sconfitto (21 pt), l'Arsenal aggancia la prima posizione.",
            "f1Title": "GP degli Stati Uniti: giorno di gara al COTA",
            "f1Blurb": "Kimi Antonelli scatta dalla pole position (1:34.035) affiancato da Max Verstappen. Semaforo verde domenica alle 15:00 locali."
        },
        "pg": {
            "pinFinal": "Finale Almaty: Medvedev b. Basilashvili 6-7(6), 6-1, 6-3 in 1h 53m. 25° titolo e prima difesa di un trofeo in carriera.",
            "week1Closed": "NFL Week 7 finale TNF: i Bears piegano i Patriots 30-24 al Soldier Field",
            "week1Sub": "Williams 308 yds lancio, 2 TD; Burden 130 yds ricezione; Santos FG da 58 yds. Bears 5-2, Patriots 4-3. 49ers imbattuti a 6-0.",
            "countdownTnf": "Finale TNF: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs e Vikings 5-0. Bills 5-1.",
            "barsPoints": "Le barre indicano il distacco dal leader. Antonelli ha 340 punti, 102 su Russell (238). Antonelli scatta in pole ad Austin.",
            "tableAfterMonday": "Premier League: City e Arsenal appaiati in vetta con 21 punti (7-0-1). Villa batte City 2-1; Spurs battono Chelsea 2-0.",
            "pinClub": "Seleziona un club. City e Arsenal a 7-0-1 con 21 punti. Chelsea 13, Villa 11, Spurs 9. Vittoria Spurs 2-0 a Stamford Bridge.",
            "plFootnote": "Sabato: Spurs 2, Chelsea 0; Villa 2, City 1; Arsenal 2, Everton 0. Domenica: Liverpool 2, Brighton 0; Bournemouth 3, Man Utd 0.",
            "majorsDone": "Butterfield Bermuda giro finale in corso. Seamus Power e Austin Smotherman co-leader dopo 54 buche (-14). Blanchet e Hirata a -1.",
            "wnbaFirstRound": "Finals WNBA Gara 4: Valkyries battono Dream 67-62 e impattano la serie sul 2-2. Gabby Williams 17 punti. Gara 5 a San Francisco.",
            "bracketFootnote": "Gara 1: Valkyries 68, Dream 64. Gara 2: Dream 79, Valkyries 65. Gara 3: Dream 97, Valkyries 71. Gara 4: Valkyries 67, Dream 62. Parita 2-2."
        }
    },
    "pl": {
        "f1": {
            "tagline": "Niedzielny wyscig o GP USA na COTA: Antonelli rusza z pole position, Verstappen i Ferrari w poscigu.",
            "liveNow": "Austin niedziela 15:00 czasu lokalnego: 56 okrazen na COTA. Antonelli na pole (1:34.035) przed Verstappenem (+0.179s). 102 pkt przewagi.",
            "pulse": "DZIEN WYSCIGU: ANTONELLI STARTUJE Z POLE POSITION W TEKSASIE",
            "keywords": "Formula 1, GP USA, Austin, COTA, Antonelli, Verstappen, Leclerc, dzien wyscigu"
        },
        "tennis": {
            "tagline": "Final w Almatach: Medvedev odwraca losy meczu z Basilashvilim 6-7, 6-1, 6-3 i broni tytulu.",
            "liveNow": "Final Almaty: Medvedev d. Basilashvili 6-7(6), 6-1, 6-3 w 1h 53m. 25. tytul w karierze i pierwsza udana obrona tytulu.",
            "pulse": "FINAL ALMATY: MEDVEDEV OBRONIL TYTUL W TRZECH SETACH",
            "keywords": "ATP, Almaty, Medvedev, Basilashvili, final, obrona tytulu, 25. tytul"
        },
        "football": {
            "tagline": "NFL Tydzien 7 niedziela: Niepokonani Chiefs, 49ers i Vikings stawiaja na szali bezbledny bilans.",
            "liveNow": "Niedziela Tydzien 7: 49ers (6-0) w Falcons, Colts w Vikings (5-0), Chiefs (5-0) w Seahawks (SNF). Bears 5-2.",
            "pulse": "NFL TYDZIEN 7: NIEPOKONANE TRIO SPRAWDZONE W NIEDZIELE",
            "keywords": "NFL Tydzien 7, Chiefs, 49ers, Vikings, Bears, niedzielne mecze, SNF"
        },
        "soccer": {
            "tagline": "Szok w Premier League: Spurs ograli Chelsea 2-0, Villa pokonala City 2-1, Arsenal dogonil lidera.",
            "liveNow": "8. kolejka: Spurs 2, Chelsea 0; Villa 2, City 1; Arsenal 2, Everton 0. City i Arsenal na czele z 21 pkt (7-0-1).",
            "pulse": "PREMIER LEAGUE: SPURS I VILLA SPRAWIAJA SENSACJE W SOBOTE",
            "keywords": "Premier League, Spurs, Chelsea, Villa, City, Arsenal, 8. kolejka"
        },
        "basketball": {
            "tagline": "Finaly WNBA mecz 4: Valkyries pokonaly Dream 67-62, wyrownaly stan serii na 2-2 i wymusily mecz 5.",
            "liveNow": "Koniec meczu 4: Valkyries 67, Dream 62. Williams 17 pkt, defensywa zatrzymala Reese. Remis 2-2, mecz 5 w San Francisco.",
            "pulse": "FINALY WNBA: VALKYRIES WYMUSILY DECYDUJACY MECZ 5",
            "keywords": "WNBA Finaly, mecz 4, Valkyries, Dream, Williams, Reese, mecz 5, 2-2"
        },
        "golf": {
            "tagline": "Finalowa runda na Bermudach: Power i Smotherman liderami po 54 dolkach, Blanchet i Hirata w poscigu.",
            "liveNow": "Butterfield Bermuda runda finalowa: Power i Smotherman na czele z -14. Blanchet i Hirata jeden dol za nimi w Port Royal.",
            "pulse": "PORT ROYAL RUNDA FINALOWA: POWER I SMOTHERMAN NA CZELE",
            "keywords": "PGA Tour, Bermudy, Port Royal, Power, Smotherman, Blanchet, Hirata, runda finalowa"
        },
        "home": {
            "tonight": "Pulpit niedzielny",
            "tonightBlurb": "Antonelli na pole position na COTA. Medvedev obronil tytul w Almatach. Spurs i Villa zaszokowali Premier League. Valkyries wymusily mecz 5.",
            "plTitle": "Premier League: Spurs pokonali Chelsea 2-0, Villa ograla Manchester City 2-1",
            "plBlurb": "Tottenham wygrywa na Stamford Bridge pierwszy raz od 2018 roku. City ponosi pierwsza porazke (21 pkt), Arsenal zrownal sie na szczycie.",
            "f1Title": "GP Stanow Zjednoczonych: dzien wyscigu na COTA",
            "f1Blurb": "Kimi Antonelli startuje z pole position (1:34.035) obok Maxa Verstappena. Start w niedziele o 15:00 czasu lokalnego."
        },
        "pg": {
            "pinFinal": "Final Almaty: Medvedev d. Basilashvili 6-7(6), 6-1, 6-3 w 1h 53m. 25. tytul i pierwsza udana obrona tytulu w karierze.",
            "week1Closed": "NFL Tydzien 7 koniec TNF: Bears pokonali Patriots 30-24 na Soldier Field",
            "week1Sub": "Williams 308 jardow gora, 2 TD; Burden 130 jardow odbioru; Santos 58-jardowy FG. Bears 5-2, Patriots 4-3. 49ers na 6-0.",
            "countdownTnf": "Koniec TNF: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs i Vikings 5-0. Bills 5-1.",
            "barsPoints": "Paski pokazuja strate do lidera. Antonelli ma 340, 102 przed Russellem (238). Antonelli startuje z pole w Austin.",
            "tableAfterMonday": "Premier League: City i Arsenal na czele z 21 punktami (7-0-1). Villa pokonala City 2-1; Spurs wygrali z Chelsea 2-0.",
            "pinClub": "Wybierz klub. City i Arsenal maja 7-0-1 i 21 pkt. Chelsea 13, Villa 11, Spurs 9. Wygrana Spurs 2-0 na Stamford Bridge.",
            "plFootnote": "Sobota: Spurs 2, Chelsea 0; Villa 2, City 1; Arsenal 2, Everton 0. Niedziela: Liverpool 2, Brighton 0; Bournemouth 3, Man Utd 0.",
            "majorsDone": "Butterfield Bermuda runda finalowa w toku. Seamus Power i Austin Smotherman prowadza po 54 dolkach (-14). Blanchet i Hirata 1 uderzenie za nimi.",
            "wnbaFirstRound": "Finaly WNBA mecz 4: Valkyries wygraly z Dream 67-62 i wyrownaly stan serii na 2-2. Gabby Williams 17 pkt. Mecz 5 w San Francisco.",
            "bracketFootnote": "Mecz 1: Valkyries 68, Dream 64. Mecz 2: Dream 79, Valkyries 65. Mecz 3: Dream 97, Valkyries 71. Mecz 4: Valkyries 67, Dream 62. Remis 2-2."
        }
    },
    "zh": {
        "f1": {
            "tagline": "美洲赛道周日正赛打响：安东内利杆位发车，维斯塔潘与法拉利全力追击。",
            "liveNow": "奥斯汀周日当地时间15:00：美洲赛道56圈正赛开跑。安东内利斩获杆位（1:34.035）领先维斯塔潘（+0.179秒）。安东内利总分领先102分。",
            "pulse": "正赛日：安东内利德州杆位领跑",
            "keywords": "一级方程式, 美国大奖赛, 奥斯汀, COTA, 安东内利, 维斯塔潘, 勒克莱尔, 正赛日"
        },
        "tennis": {
            "tagline": "阿拉木图决赛：梅德韦杰夫6-7、6-1、6-3逆转巴西拉什维利成功卫冕。",
            "liveNow": "阿拉木图男单决赛：梅德韦杰夫用时1小时53分钟以6-7(6)、6-1、6-3击败巴西拉什维利。收获生涯第25座冠军并首度实现巡回赛卫冕。",
            "pulse": "阿拉木图决赛：梅德韦杰夫三盘逆转成功卫冕",
            "keywords": "ATP, 阿拉木图, 梅德韦杰夫, 巴西拉什维利, 决赛, 卫冕, 第25冠"
        },
        "football": {
            "tagline": "NFL第7周超级周日：保持全胜的酋长、49人与维京人全力捍卫不败金身。",
            "liveNow": "第7周周日焦点：49人（6-0）客战猎鹰，维京人（5-0）主场迎战小马，酋长（5-0）周日夜赛做客海鹰。熊队5-2。",
            "pulse": "NFL第7周：不败三强周日经受考验",
            "keywords": "NFL第7周, 酋长, 49人, 维京人, 熊队, 周日焦点, SNF"
        },
        "soccer": {
            "tagline": "英超冷门迭爆：热刺2-0客破切尔西，维拉2-1击落曼城，阿森纳积分追平榜首。",
            "liveNow": "第8轮：热刺2-0切尔西；维拉2-1曼城；阿森纳2-0埃弗顿。曼城与阿森纳同积21分（7胜0平1负）领跑。",
            "pulse": "英超联赛：热刺与维拉联袂制造周六大冷",
            "keywords": "英超, 热刺, 切尔西, 维拉, 曼城, 阿森纳, 第8轮"
        },
        "basketball": {
            "tagline": "WNBA总决赛第4战：女武神67-62客胜梦想，大比分扳成2-2平拖入抢五大战。",
            "liveNow": "第4战战报：女武神 67，梦想 62。威廉姆斯17分，全队严防终结里斯两双纪录。系列赛2-2平移师旧金山。",
            "pulse": "WNBA总决赛：女武神顽强拖入旧金山抢五生死战",
            "keywords": "WNBA总决赛, 第4战, 女武神, 梦想, 威廉姆斯, 里斯, 第5战, 2-2"
        },
        "golf": {
            "tagline": "百慕大锦标赛决赛轮：鲍尔与斯莫瑟曼前54洞并列领跑，布兰切特与平田宪圣紧追。",
            "liveNow": "百慕大锦标赛决赛轮：鲍尔与斯莫瑟曼同以-14杆并列领先。布兰切特和平田宪圣落后1杆紧随其后。皇家港标准杆71杆。",
            "pulse": "皇家港决赛轮：鲍尔与斯莫瑟曼并列榜首争冠",
            "keywords": "美巡赛, 百慕大, 皇家港, 鲍尔, 斯莫瑟曼, 布兰切特, 平田宪圣, 决赛轮"
        },
        "home": {
            "tonight": "周日快讯",
            "tonightBlurb": "安东内利在美洲赛道杆位发车。梅德韦杰夫卫冕阿拉木图冠军。热刺与维拉震撼英超。女武神将WNBA总决赛拖入抢五。",
            "plTitle": "英超联赛：热刺2-0客胜切尔西，维拉2-1终结曼城连胜",
            "plBlurb": "热刺自2018年以来首度攻克斯坦福桥。曼城遭遇赛季首败（21分），阿森纳积分追平领跑。",
            "f1Title": "美国大奖赛：美洲赛道正赛日打响",
            "f1Blurb": "基米·安东内利凭借1:34.035圈速夺得杆位，与维斯塔潘头排起跑。正赛周日当地时间15:00开战。"
        },
        "pg": {
            "pinFinal": "阿拉木图决赛：梅德韦杰夫 6-7(6)、6-1、6-3 逆转巴西拉什维利。收获生涯第25座冠军并首度卫冕成功。",
            "week1Closed": "NFL第7周TNF完赛：熊队在军人球场30-24战胜爱国者",
            "week1Sub": "威廉姆斯传球308码2达阵；伯登接球130码；桑托斯命中58码任意球。熊队5-2，爱国者4-3。49人保持6-0完好战绩。",
            "countdownTnf": "TNF完赛：熊队 30，爱国者 24。熊队5-2。49人6-0。酋长与维京人5-0。比尔5-1。",
            "barsPoints": "柱状图显示与领跑者的分差。安东内利积340分，领先拉塞尔（238分）达102分。安东内利奥斯汀杆位起跑。",
            "tableAfterMonday": "英超联赛：曼城与阿森纳同积21分（7胜0平1负）并列榜首。维拉2-1击败曼城；热刺2-0客破切尔西。",
            "pinClub": "选择俱乐部。曼城与阿森纳同为7胜0平1负积21分。切尔西13分，维拉11分，热刺9分。热刺在斯坦福桥2-0获胜。",
            "plFootnote": "周六：热刺 2-0 切尔西；维拉 2-1 曼城；阿森纳 2-0 埃弗顿。周日：利物浦 2-0 布莱顿；伯恩茅斯 3-0 曼联。",
            "majorsDone": "百慕大锦标赛决赛轮进行中。鲍尔与斯莫瑟曼前54洞同以-14杆领跑。布兰切特与平田宪圣仅落后1杆。",
            "wnbaFirstRound": "WNBA总决赛第4战：女武神67-62力克梦想将大比分扳成2-2平。威廉姆斯17分。第5战移师旧金山。",
            "bracketFootnote": "第1战：女武神 68，梦想 64。第2战：梦想 79，女武神 65。第3战：梦想 97，女武神 71。第4战：女武神 67，梦想 62。系列赛2-2平。"
        }
    },
    "ja": {
        "f1": {
            "tagline": "COTAでアメリカGP決勝レース開催：アントネッリがポール発進、フェルスタッペンとフェラーリが追走。",
            "liveNow": "オースティン日曜現地15:00：COTAで56周の決勝。アントネッリがポール（1:34.035）、フェルスタッペン2番手（+0.179秒）。102点リード。",
            "pulse": "決勝レース：アントネッリがテキサスでポールから発進",
            "keywords": "F1, アメリカGP, オースティン, COTA, アントネッリ, フェルスタッペン, ルクレール, 決勝"
        },
        "tennis": {
            "tagline": "アルマティ決勝：メドベージェフがバシラシビリに6-7, 6-1, 6-3で逆転勝ち、初タイトル防衛達成。",
            "liveNow": "アルマティ決勝：メドベージェフが1時間53分でバシラシビリを6-7(6), 6-1, 6-3で撃破。通算25個目のタイトル獲得かつキャリア初の防衛成功。",
            "pulse": "アルマティ決勝：メドベージェフが3セット逆転でタイトル防衛",
            "keywords": "ATP, アルマティ, メドベージェフ, バシラシビリ, 決勝, タイトル防衛, 通算25勝"
        },
        "football": {
            "tagline": "NFL第7週日曜：全勝のチーフス、49ers、バイキングスが無敗記録をかけて激突。",
            "liveNow": "日曜第7週：49ers（6-0）対ファルコンズ、バイキングス（5-0）対コルツ、チーフス（5-0）対シーホークス（SNF）。ベアーズ5-2。",
            "pulse": "NFL第7週：無敗の3チームが日曜の試練へ",
            "keywords": "NFL第7週, チーフス, 49ers, バイキングス, ベアーズ, 日曜ゲーム, SNF"
        },
        "soccer": {
            "tagline": "プレミアリーグ波乱：スパーズがチェルシーを2-0撃破、ヴィラがシティに2-1勝利、アーセナルが首位並走。",
            "liveNow": "第8節：スパーズ 2-0 チェルシー、ヴィラ 2-1 シティ、アーセナル 2-0 エヴァートン。シティとアーセナルが勝点21（7勝0分1敗）で首位並走。",
            "pulse": "プレミアリーグ：スパーズとヴィラが土曜に大番狂わせ",
            "keywords": "プレミアリーグ, スパーズ, チェルシー, ヴィラ, シティ, アーセナル, 第8節"
        },
        "basketball": {
            "tagline": "WNBAファイナル第4戦：ヴァルキリーズがドリームを67-62で破り2勝2敗のタイ、最終第5戦へ。",
            "liveNow": "第4戦終了：ヴァルキリーズ 67、ドリーム 62。ウィリアムズ17得点、守備でリーズを封じる。2勝2敗で決着はサンフランシスコへ。",
            "pulse": "WNBAファイナル：ヴァルキリーズが逆王手で最終第5戦へ",
            "keywords": "WNBAファイナル, 第4戦, ヴァルキリーズ, ドリーム, ウィリアムズ, リーズ, 第5戦, 2-2"
        },
        "golf": {
            "tagline": "バミューダ最終ラウンド：パワーとスモザーマンが54ホール終了時点で首位タイ、ブランシェット追走。",
            "liveNow": "バミューダ選手権最終R：パワーとスモザーマンが通算-14で首位。ブランシェットと平田憲聖が1打差で追う。ポートロイヤル（パー71）。",
            "pulse": "ポートロイヤル最終R：パワーとスモザーマンが首位タイ",
            "keywords": "PGAツアー, バミューダ, ポートロイヤル, パワー, スモザーマン, ブランシェット, 平田憲聖, 最終R"
        },
        "home": {
            "tonight": "日曜デスク",
            "tonightBlurb": "アントネッリがCOTAでポール発進。メドベージェフがアルマティで連覇。スパーズとヴィラがプレミアで大波乱。ヴァルキリーズが第5戦へ持ち込む。",
            "plTitle": "プレミアリーグ：スパーズがチェルシーを2-0撃破、ヴィラがシティに土をつける",
            "plBlurb": "トッテナムが2018年以来となるスタンフォード・ブリッジでの勝利。シティが初黒星（21点）でアーセナルと首位タイに並ぶ。",
            "f1Title": "アメリカGP：COTAで決勝レース開幕",
            "f1Blurb": "キミ・アントネッリが1:34.035でポールポジションを獲得、フェルスタッペンとフロントローからスタート。日曜現地15:00決勝。"
        },
        "pg": {
            "pinFinal": "アルマティ決勝：メドベージェフ 6-7(6), 6-1, 6-3 バシラシビリ。通算25個目のタイトル獲得でキャリア初のタイトル防衛。",
            "week1Closed": "NFL第7週TNF終了：ベアーズがソルジャー・フィールドでペイトリオッツを30-24で撃破",
            "week1Sub": "ウィリアムズ308ydパス・2TD、バーデン130ydレシーブ、サントス58ydのFG。ベアーズ5-2、ペイトリオッツ4-3。49ersは6勝0敗を維持。",
            "countdownTnf": "TNF終了：ベアーズ 30、ペイトリオッツ 24。ベアーズ5-2。49ers 6-0。チーフスとバイキングス5-0。ビルズ5-1。",
            "barsPoints": "バーは首位との差を示します。アントネッリが340点で首位、ラッセル（238点）に102点差。アントネッリがオースティンでポール発進。",
            "tableAfterMonday": "プレミアリーグ：シティとアーセナルが勝点21（7勝0分1敗）で首位並走。ヴィラがシティを2-1、スパーズがチェルシーを2-0で撃破。",
            "pinClub": "クラブを選択。シティとアーセナルは7勝0分1敗で21点。チェルシー13点、ヴィラ11点、スパーズ9点。スパーズが敵地で2-0勝利。",
            "plFootnote": "土曜：スパーズ 2-0 チェルシー、ヴィラ 2-1 シティ、アーセナル 2-0 エヴァートン。日曜：リヴァプール 2-0 ブライトン、ボーンマス 3-0 マンU。",
            "majorsDone": "バミューダ選手権最終Rが進行中。パワーとスモザーマンが54ホール終了時点で-14の首位タイ。ブランシェットと平田が1打差追走。",
            "wnbaFirstRound": "WNBAファイナル第4戦：ヴァルキリーズが67-62でドリームを下し2勝2敗のタイに。ウィリアムズ17点。第5戦はサンフランシスコ。",
            "bracketFootnote": "第1戦：ヴァルキリーズ 68、ドリーム 64。第2戦：ドリーム 79、ヴァルキリーズ 65。第3戦：ドリーム 97、ヴァルキリーズ 71。第4戦：ヴァルキリーズ 67、ドリーム 62。2勝2敗タイ。"
        }
    },
    "ko": {
        "f1": {
            "tagline": "미국 GP COTA 결승 레이스 데이: 안토넬리 폴포지션 출발, 베르스타펜과 페라리 추격전.",
            "liveNow": "오스틴 일요일 현지 15:00: COTA 56랩 결승. 안토넬리 폴(1:34.035), 베르스타펜 2위(+0.179초). 안토넬리 102점 차 리드.",
            "pulse": "레이스 데이: 안토넬리 텍사스에서 폴포지션 출발",
            "keywords": "F1, 미국 GP, 오스틴, COTA, 안토넬리, 베르스타펜, 르클레르, 레이스 데이"
        },
        "tennis": {
            "tagline": "알마티 결승: 메드베데프가 바실라시빌리에 6-7, 6-1, 6-3 역전승 거두고 타이틀 방어 성공.",
            "liveNow": "알마티 결승: 메드베데프 1시간 53분 접전 끝에 바실라시빌리를 6-7(6), 6-1, 6-3으로 격파. 통산 25번째 타이틀이자 생애 첫 타이틀 방어.",
            "pulse": "알마티 결승: 메드베데프 3세트 역전승으로 타이틀 방어",
            "keywords": "ATP, 알마티, 메드베데프, 바실라시빌리, 결승, 타이틀 방어, 25번째 우승"
        },
        "football": {
            "tagline": "NFL 7주차 일요일: 무패 질주 중인 치프스, 49ers, 바이킹스가 완벽한 성적표 수성에 나선다.",
            "liveNow": "일요일 7주차: 49ers(6-0) 대 팔콘스, 바이킹스(5-0) 대 콜츠, 치프스(5-0) 대 시호크스(SNF). 베어스 5-2.",
            "pulse": "NFL 7주차: 무패 3총사 일요일 시험대 돌입",
            "keywords": "NFL 7주차, 치프스, 49ers, 바이킹스, 베어스, 일요일 일정, SNF"
        },
        "soccer": {
            "tagline": "프리미어리그 지각변동: 토트넘이 첼시를 2-0 제압, 빌라가 맨시티를 2-1로 격침하며 아스널과 공동 선두.",
            "liveNow": "8라운드: 토트넘 2, 첼시 0; 빌라 2, 맨시티 1; 아스널 2, 에버턴 0. 맨시티와 아스널 승점 21점(7승 0무 1패) 공동 1위.",
            "pulse": "프리미어리그: 토트넘과 빌라 토요일 대이변 연출",
            "keywords": "프리미어리그, 토트넘, 첼시, 빌라, 맨시티, 아스널, 8라운드"
        },
        "basketball": {
            "tagline": "WNBA 파이널 4차전: 발키리스가 드림을 67-62로 꺾고 시리즈 2-2 균형, 5차전 강제 돌입.",
            "liveNow": "4차전 최종: 발키리스 67, 드림 62. 윌리엄스 17점, 질식 수비로 리스 봉쇄. 시리즈 2-2 원점, 샌프란시스코 5차전.",
            "pulse": "WNBA 파이널: 발키리스 승부 원점으로 돌리며 5차전 진입",
            "keywords": "WNBA 파이널, 4차전, 발키리스, 드림, 윌리엄스, 리스, 5차전, 2-2"
        },
        "golf": {
            "tagline": "버뮤다 최종 라운드: 파워와 스모더먼이 54홀 공동 선두 질주, 블랑셰와 히라타 맹추격.",
            "liveNow": "버뮤다 챔피언십 최종R: 파워와 스모더먼 14언더파 공동 선두. 블랑셰와 히라타 1타 차 추격. 포트 로열 파71.",
            "pulse": "포트 로열 최종 라운드: 파워와 스모더먼 공동 선두",
            "keywords": "PGA 투어, 버뮤다, 포트 로열, 파워, 스모더먼, 블랑셰, 히라타, 최종 라운드"
        },
        "home": {
            "tonight": "일요일 데스크",
            "tonightBlurb": "안토넬리 COTA 폴포지션 출발. 메드베데프 알마티 타이틀 방어 성공. 토트넘과 빌라 프리미어리그 대이변. 발키리스 WNBA 5차전 성사.",
            "plTitle": "프리미어리그: 토트넘 첼시 2-0 격파, 빌라 맨시티 2-1 제압",
            "plBlurb": "토트넘 2018년 이후 첫 스탬퍼드 브리지 승리. 맨시티 시즌 첫 패배(21점), 아스널과 승점 동률 선두.",
            "f1Title": "미국 GP: COTA 결승 레이스 개막",
            "f1Blurb": "키미 안토넬리가 1:34.035로 폴포지션을 획득하며 베르스타펜과 나란히 출발합니다. 일요일 현지 15:00 결승."
        },
        "pg": {
            "pinFinal": "알마티 결승: 메드베데프 6-7(6), 6-1, 6-3 바실라시빌리. 통산 25번째 타이틀이자 생애 첫 타이틀 방어 달성.",
            "week1Closed": "NFL 7주차 TNF 종료: 베어스가 솔저 필드에서 패트리어츠를 30-24로 제압",
            "week1Sub": "윌리엄스 308야드 패스 2TD, 버든 130야드 리시빙, 산토스 58야드 FG. 베어스 5-2, 패트리어츠 4-3. 49ers 6승 0패 유지.",
            "countdownTnf": "TNF 종료: 베어스 30, 패트리어츠 24. 베어스 5-2. 49ers 6-0. 치프스와 바이킹스 5-0. 빌스 5-1.",
            "barsPoints": "막대는 선두와의 격차를 보여줍니다. 안토넬리가 340점, 러셀(238점)에 102점 앞서 있습니다. 안토넬리 오스틴 폴 출발.",
            "tableAfterMonday": "프리미어리그: 맨시티와 아스널 승점 21점(7승 0무 1패) 공동 선두. 빌라가 맨시티를 2-1, 토트넘이 첼시를 2-0으로 제압.",
            "pinClub": "클럽을 선택하세요. 맨시티와 아스널 7승 0무 1패 21점. 첼시 13점, 빌라 11점, 토트넘 9점. 토트넘 브리지에서 2-0 승리.",
            "plFootnote": "토요일: 토트넘 2-0 첼시, 빌라 2-1 맨시티, 아스널 2-0 에버턴. 일요일: 리버풀 2-0 브라이턴, 본머스 3-0 맨유.",
            "majorsDone": "버뮤다 챔피언십 최종 라운드 진행 중. 시머스 파워와 오스틴 스모더먼 54홀 14언더파 공동 선두. 블랑셰, 히라타 1타 차.",
            "wnbaFirstRound": "WNBA 파이널 4차전: 발키리스가 드림을 67-62로 꺾고 시리즈 2-2 원점. 개비 윌리엄스 17점. 5차전 샌프란시스코.",
            "bracketFootnote": "1차전: 발키리스 68, 드림 64. 2차전: 드림 79, 발키리스 65. 3차전: 드림 97, 발키리스 71. 4차전: 발키리스 67, 드림 62. 2승 2패 동률."
        }
    },
    "ar": {
        "f1": {
            "tagline": "يوم سباق جائزة امريكا الكبرى في حلبة الامريكيتين: انتونيلي ينطلق من القطب وفيرستابن وفيراري يلاحقان.",
            "liveNow": "اوستن الاحد 15:00 محليا: 56 لفة في حلبة الامريكيتين. انتونيلي اولا (1:34.035) امام فيرستابن (+0.179 ثانية). فارق 102 نقطة.",
            "pulse": "يوم السباق: انتونيلي يقود شبكة الانطلاق في تكساس",
            "keywords": "فورمولا 1, جائزة امريكا الكبرى, اوستن, حلبة الامريكيتين, انتونيلي, فيرستابن, لوكلير, يوم السباق"
        },
        "tennis": {
            "tagline": "نهائي الماتي: ميدفيديف يقلب الطاولة على باسيلاشفيلي 6-7 و6-1 و6-3 ويدافع عن لقبه بنجاح.",
            "liveNow": "نهائي الماتي: ميدفيديف يهزم باسيلاشفيلي 6-7(6) و6-1 و6-3 في ساعة و53 دقيقة. اللقب 25 في مسيرته واول دفاع ناجح عن لقب.",
            "pulse": "نهائي الماتي: ميدفيديف يدافع عن لقبه في ثلاث مجموعات",
            "keywords": "ATP, الماتي, ميدفيديف, باسيلاشفيلي, نهائي, دفاع عن اللقب, اللقب 25"
        },
        "football": {
            "tagline": "NFL الاسبوع 7 الاحد: تشيفس و49رز وفايكنغز بلا هزيمة يضعون سجلهم المثالي على المحك.",
            "liveNow": "مباريات الاحد: 49رز (6-0) ضد فالكونز، فايكنغز (5-0) ضد كولتس، تشيفس (5-0) ضد سيهوكس (SNF). بيرز 5-2.",
            "pulse": "NFL الاسبوع 7: اختبار حاسم للثلاثي الذي لا يقهر",
            "keywords": "NFL الاسبوع 7, تشيفس, 49رز, فايكنغز, بيرز, مباريات الاحد, SNF"
        },
        "soccer": {
            "tagline": "مفاجآت الدوري الانجليزي: توتنهام يصدم تشيلسي 2-0، وفيلا يسقط سيتي 2-1 وارسنال يتقاسم الصدارة.",
            "liveNow": "الجولة 8: توتنهام 2، تشيلسي 0؛ فيلا 2، سيتي 1؛ ارسنال 2، ايفرتون 0. سيتي وارسنال في الصدارة بـ21 نقطة (7-0-1).",
            "pulse": "الدوري الانجليزي: توتنهام وفيلا يفجران مفاجآت السبت الكبرى",
            "keywords": "الدوري الانجليزي, توتنهام, تشيلسي, فيلا, سيتي, ارسنال, الجولة 8"
        },
        "basketball": {
            "tagline": "نهائيات WNBA المباراة 4: فالكيريز يسقط دريم 67-62 ويعادل السلسلة 2-2 لفرض مباراة خامسة فاصلة.",
            "liveNow": "المباراة 4: فالكيريز 67، دريم 62. ويليامز 17 نقطة والدفاع يوقف سلسلة ريس. التعادل 2-2 ومباراة الحسم في سان فرانسيسكو.",
            "pulse": "نهائيات WNBA: فالكيريز يفرض مباراة خامسة حاسمة في سان فرانسيسكو",
            "keywords": "نهائيات WNBA, المباراة 4, فالكيريز, دريم, ويليامز, ريس, المباراة 5, 2-2"
        },
        "golf": {
            "tagline": "الجولة الختامية في برمودا: باور وسموذرمن في صدارة 54 حفرة، وبلانشيت وهيراتا يطاردان.",
            "liveNow": "بطولة برمودا الجولة الختامية: باور وسموذرمن في صدارة مشتركة بـ-14. بلانشيت وهيراتا بفارق ضربة في بورت رويال معدل 71.",
            "pulse": "بورت رويال الجولة الختامية: باور وسموذرمن في الصدارة",
            "keywords": "جولة PGA, برمودا, بورت رويال, باور, سموذرمن, بلانشيت, هيراتا, الجولة الختامية"
        },
        "home": {
            "tonight": "مكتب الاحد",
            "tonightBlurb": "انتونيلي ينطلق من القطب في تكساس. ميدفيديف يدافع عن لقبه في الماتي. توتنهام وفيلا يهزان الدوري الانجليزي. فالكيريز يفرض مباراة فاصلة في WNBA.",
            "plTitle": "الدوري الانجليزي: توتنهام يسقط تشيلسي 2-0 وفيلا يصعق مانشستر سيتي 2-1",
            "plBlurb": "توتنهام يفوز في ستامفورد بريدج لاول مرة منذ 2018. سيتي يتجرع خسارته الاولى (21 نقطة) وارسنال يتساوى معه بالقمة.",
            "f1Title": "جائزة امريكا الكبرى: يوم السباق في حلبة الامريكيتين",
            "f1Blurb": "كيمي انتونيلي ينطلق من المركز الاول (1:34.035) الى جانب ماكس فيرستابن. الانطلاق الاحد الساعة 15:00 محليا."
        },
        "pg": {
            "pinFinal": "نهائي الماتي: ميدفيديف يهزم باسيلاشفيلي 6-7(6) و6-1 و6-3 في ساعة و53 دقيقة. اللقب 25 واول دفاع ناجح عن لقب في مسيرته.",
            "week1Closed": "NFL الاسبوع 7 نهاية TNF: بيرز يهزم باتريوتس 30-24 في سولجر فيلد",
            "week1Sub": "ويليامز 308 ياردات تمرير و2 TD؛ بيردن 130 ياردة استقبال؛ سانتوس هدف ميداني من 58 ياردة. بيرز 5-2، باتريوتس 4-3. 49رز 6-0.",
            "countdownTnf": "نهاية TNF: بيرز 30، باتريوتس 24. بيرز 5-2. 49رز 6-0. تشيفس وفايكنغز 5-0. بيلز 5-1.",
            "barsPoints": "الاعمدة توضح الفارق مع المتصدر. انتونيلي يملك 340 نقطة، متقدما بـ102 على راسل (238). انتونيلي ينطلق من القطب في اوستن.",
            "tableAfterMonday": "الدوري الانجليزي: سيتي وارسنال يتشاركان الصدارة بـ21 نقطة (7-0-1). فيلا اسقط سيتي 2-1؛ وتوتنهام هزم تشيلسي 2-0.",
            "pinClub": "اختر ناديا. سيتي وارسنال 7-0-1 برصيد 21 نقطة. تشيلسي 13، فيلا 11، توتنهام 9. توتنهام فاز 2-0 في الستامفورد.",
            "plFootnote": "السبت: توتنهام 2-0 تشيلسي؛ فيلا 2-1 سيتي؛ ارسنال 2-0 ايفرتون. الاحد: ليفربول 2-0 برايتون؛ بورنموث 3-0 مان يونايتد.",
            "majorsDone": "بطولة برمودا الجولة الختامية جارية. سيموس باور واوستن سموذرمن في صدارة 54 حفرة (-14). بلانشيت وهيراتا بفارق ضربة واحدة.",
            "wnbaFirstRound": "نهائيات WNBA المباراة 4: فالكيريز يهزم دريم 67-62 ويعادل السلسلة 2-2. غابي ويليامز 17 نقطة. المباراة 5 في سان فرانسيسكو.",
            "bracketFootnote": "المباراة 1: فالكيريز 68، دريم 64. المباراة 2: دريم 79، فالكيريز 65. المباراة 3: دريم 97، فالكيريز 71. المباراة 4: فالكيريز 67، دريم 62. التعادل 2-2."
        }
    }
}

# Strict validation against em-dashes and double-hyphens
for lang, sections in DATA.items():
    for sec_name, sec_dict in sections.items():
        for k, v in sec_dict.items():
            if "—" in v:
                raise ValueError(f"Em-dash found in {lang}.{sec_name}.{k}: {v}")
            if "--" in v:
                raise ValueError(f"Double-hyphen found in {lang}.{sec_name}.{k}: {v}")

print("Validation passed: No em-dashes or double-hyphens found in DATA dictionary.")

# 1. Update frontend/src/i18n/playground.ts
pg_file = "frontend/src/i18n/playground.ts"
with open(pg_file, "r", encoding="utf-8") as f:
    pg_content = f.read()

for lang in ["en", "fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
    pg_data = DATA[lang]["pg"]
    pattern = rf'(["\']?{lang}["\']?:\s*\{{)([\s\S]*?)(^\s*\}},?)'
    match = re.search(pattern, pg_content, re.MULTILINE)
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

print("All locale updates for 25 Oct 2026 completed successfully!")
