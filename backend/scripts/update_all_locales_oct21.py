import re

DATA = {
    "en": {
        "football": {
            "tagline": "Thursday kickoff: Patriots visit the Bears at Soldier Field. 49ers remain 6-0.",
            "liveNow": "TNF Thursday 8:15 p.m. ET: Patriots (4-2) at Bears (4-2), Prime Video, Chicago -3. Monday final: 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF TOMORROW: PATRIOTS AT BEARS (4-2)",
            "keywords": "NFL Week 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field"
        },
        "tennis": {
            "tagline": "Almaty Wednesday: Tsitsipas edges Kovacevic in three. Khachanov cruises past Sakamoto.",
            "liveNow": "Almaty: Tsitsipas d. Kovacevic 7-6(9), 3-6, 6-3. Khachanov d. Sakamoto 6-2, 6-4. Duckworth d. Darderi 7-5, 7-6(7). Lyon: Moutet d. Humbert.",
            "pulse": "ALMATY: TSITSIPAS AND KHACHANOV REACH ROUND TWO",
            "keywords": "ATP, Almaty, Tsitsipas, Kovacevic, Khachanov, Duckworth, Lyon, Moutet"
        },
        "f1": {
            "tagline": "United States GP: two days to Friday practice. Antonelli leads Russell by 102.",
            "liveNow": "No running on 21 October. COTA weekend 23-25 October, race Sunday 25 October at 15:00 local. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN IN TWO DAYS: ANTONELLI LEADS BY 102",
            "keywords": "Formula 1, United States GP, Austin, COTA, Antonelli, Russell, Mercedes"
        },
        "soccer": {
            "tagline": "Spurs digest 3-1 win ahead of Chelsea trip. City lead table by three on 21.",
            "liveNow": "Standings: City 21, Arsenal 18, Brighton 16. Spurs 16th on 6, Coventry 17th on 6. MW8 opens Friday; Chelsea v Spurs Saturday.",
            "pulse": "PREMIER LEAGUE: CITY LEAD AS DERBY WEEKEND NEARS",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Maddison, MW8"
        },
        "basketball": {
            "tagline": "WNBA Finals Game 3 tonight: Valkyries at Dream. The series is tied 1-1.",
            "liveNow": "Game 3 Wednesday 8:00 p.m. ET, State Farm Arena, USA/Peacock/CNBC. No score. Game 2: Dream 79, Valkyries 65. Series 1-1.",
            "pulse": "WNBA FINALS GAME 3 TONIGHT: SERIES TIED 1-1",
            "keywords": "WNBA Finals, Game 3, Dream, Valkyries, Reese, State Farm Arena, 1-1"
        },
        "golf": {
            "tagline": "Wednesday Pro-Am wraps in Bermuda. Port Royal opens Thursday for Round 1.",
            "liveNow": "Pro-Am completed Wednesday. Field of 120, purse $6 million, par 71. Adam Schenk defends. Round 1 Thursday, Golf Channel 1-4 p.m. ET.",
            "pulse": "PORT ROYAL OPENS THURSDAY: PRO-AM COMPLETE",
            "keywords": "PGA Tour, Bermuda, Port Royal, Adam Schenk, Pro-Am, Brennan"
        },
        "home": {
            "tonight": "Wednesday desk",
            "tonightBlurb": "WNBA Finals Game 3 tonight in Atlanta, series 1-1. Tsitsipas and Khachanov win in Almaty. Patriots visit Bears on Thursday.",
            "plTitle": "Premier League: City hold three-point lead as Spurs prepare for Chelsea",
            "plBlurb": "Spurs 16th on 6 after beating Coventry 3-1. City lead table on 21, Arsenal 18, Brighton 16. Matchweek 8 begins Friday.",
            "f1Title": "Next race: United States GP in Austin",
            "f1Blurb": "Paddock setup in Austin. COTA weekend 23-25 October, race Sunday 25 October at 15:00 local. Antonelli leads by 102."
        },
        "pg": {
            "pinFinal": "Almaty Wednesday: Tsitsipas edges Kovacevic 7-6(9), 3-6, 6-3. Khachanov d. Sakamoto 6-2, 6-4. Shanghai stands: Davidovich Fokina d. Jodar.",
            "week1Closed": "NFL Week 7 kickoff: Patriots at Bears on Thursday night",
            "week1Sub": "Patriots visit Bears at Soldier Field, 8:15 p.m. ET, Prime Video, Chicago -3. 49ers stand 6-0. Chiefs and Vikings 5-0.",
            "countdownTnf": "TNF Thursday: Patriots at Bears. Monday final: 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Bars show the gap to the leader. Antonelli has 340, 102 ahead of Russell on 238. Two days to Friday practice in Austin.",
            "tableAfterMonday": "Premier League: City lead table on 21 points. Arsenal 18, Brighton 16. Spurs 16th on 6 after 3-1 win.",
            "pinClub": "Select a club. City are 7-0-0 on 21. Arsenal 18, Brighton 16. Spurs beat Coventry 3-1. MW8 opens Friday.",
            "plFootnote": "Monday final: Tottenham 3, Coventry 1. Matchweek 8 opens Friday: Ipswich v Forest; Saturday: Chelsea v Spurs, Villa v City.",
            "majorsDone": "Wednesday Pro-Am wraps. Butterfield Bermuda opens Thursday at Port Royal, field of 120, Adam Schenk defends. Brennan won Baycurrent at 16 under.",
            "wnbaFirstRound": "WNBA Finals Game 3 tonight: Valkyries at Dream, series tied 1-1. Tip 8:00 p.m. ET, State Farm Arena. No score.",
            "bracketFootnote": "Game 1: Valkyries 68, Dream 64. Game 2: Dream 79, Valkyries 65. Game 3 tonight, Wednesday 21 October, 8:00 p.m. ET, USA/Peacock/CNBC. Series tied 1-1."
        }
    },
    "fr": {
        "football": {
            "tagline": "Coup d'envoi jeudi : les Patriots rendent visite aux Bears. Les 49ers restent a 6-0.",
            "liveNow": "TNF jeudi 20 h 15 ET : Patriots (4-2) chez les Bears (4-2), Prime Video, Chicago -3. Finale de lundi : 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF DEMAIN : PATRIOTS CHEZ LES BEARS (4-2)",
            "keywords": "NFL semaine 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field"
        },
        "tennis": {
            "tagline": "Mercredi a Almaty : Tsitsipas ecarte Kovacevic en trois sets. Khachanov domine Sakamoto.",
            "liveNow": "Almaty : Tsitsipas bat Kovacevic 7-6(9), 3-6, 6-3. Khachanov bat Sakamoto 6-2, 6-4. Duckworth bat Darderi 7-5, 7-6(7). Lyon : Moutet bat Humbert.",
            "pulse": "ALMATY : TSITSIPAS ET KHACHANOV AU DEUXIEME TOUR",
            "keywords": "ATP, Almaty, Tsitsipas, Kovacevic, Khachanov, Duckworth, Lyon, Moutet"
        },
        "f1": {
            "tagline": "GP des Etats-Unis : deux jours avant les essais libres. Antonelli devance Russell de 102 points.",
            "liveNow": "Pas de roulage le 21 octobre. Week-end a COTA du 23 au 25 octobre, course dimanche 25 octobre a 15:00 locale. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN DANS DEUX JOURS : ANTONELLI MENE DE 102",
            "keywords": "Formule 1, GP des Etats-Unis, Austin, COTA, Antonelli, Russell, Mercedes"
        },
        "soccer": {
            "tagline": "Les Spurs savourent avant Chelsea. City mene avec trois longueurs d'avance a 21.",
            "liveNow": "Classement : City 21, Arsenal 18, Brighton 16. Spurs 16es a 6, Coventry 17es a 6. 8e journee des vendredi ; Chelsea - Spurs samedi.",
            "pulse": "PREMIER LEAGUE : CITY MENE AVANT LE DERBY",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Maddison, 8e journee"
        },
        "basketball": {
            "tagline": "Finales WNBA match 3 ce soir : les Valkyries chez le Dream. Serie a 1-1.",
            "liveNow": "Match 3 mercredi 20 h 00 ET, State Farm Arena, USA/Peacock/CNBC. Pas de score. Match 2 : Dream 79, Valkyries 65. Serie 1-1.",
            "pulse": "FINALES WNBA MATCH 3 CE SOIR : SERIE A 1-1",
            "keywords": "WNBA Finales, match 3, Dream, Valkyries, Reese, State Farm Arena, 1-1"
        },
        "golf": {
            "tagline": "Fin du Pro-Am aux Bermudes. Port Royal ouvre jeudi pour le premier tour.",
            "liveNow": "Pro-Am termine mercredi. Champ de 120, dotation 6 millions, par 71. Adam Schenk defend son titre. Premier tour jeudi, Golf Channel 13 h a 16 h ET.",
            "pulse": "PORT ROYAL OUVRE JEUDI : PRO-AM TERMINE",
            "keywords": "PGA Tour, Bermudes, Port Royal, Adam Schenk, Pro-Am, Brennan"
        },
        "home": {
            "tonight": "Bureau du mercredi",
            "tonightBlurb": "Match 3 des Finales WNBA ce soir a Atlanta (1-1). Tsitsipas et Khachanov gagnent a Almaty. Les Patriots visitent les Bears jeudi.",
            "plTitle": "Premier League : City garde trois points d'avance alors que les Spurs preparent Chelsea",
            "plBlurb": "Spurs 16es a 6 points apres leur 3-1 contre Coventry. City mene a 21, Arsenal 18, Brighton 16. 8e journee vendredi.",
            "f1Title": "Prochaine course : GP des Etats-Unis a Austin",
            "f1Blurb": "Installation des garages a Austin. COTA du 23 au 25 octobre, course dimanche 25 octobre a 15:00 locale. Antonelli mene de 102."
        },
        "pg": {
            "pinFinal": "Mercredi a Almaty : Tsitsipas bat Kovacevic 7-6(9), 3-6, 6-3. Khachanov bat Sakamoto 6-2, 6-4. Shanghai tient : Davidovich Fokina bat Jodar.",
            "week1Closed": "NFL coup d'envoi semaine 7 : Patriots chez les Bears jeudi soir",
            "week1Sub": "Patriots chez les Bears au Soldier Field, 20 h 15 ET, Prime Video, Chicago -3. 49ers a 6-0. Chiefs et Vikings a 5-0.",
            "countdownTnf": "TNF jeudi : Patriots chez les Bears. Finale lundi : 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Les barres montrent l'ecart. Antonelli a 340, 102 devant Russell (238). Deux jours avant les essais a Austin.",
            "tableAfterMonday": "Premier League : City mene avec 21 points. Arsenal 18, Brighton 16. Spurs 16es a 6 apres leur victoire 3-1.",
            "pinClub": "Choisir un club. City est a 7-0-0 et 21 points. Arsenal 18, Brighton 16. Les Spurs battent Coventry 3-1. 8e journee vendredi.",
            "plFootnote": "Finale lundi : Tottenham 3, Coventry 1. La 8e journee commence vendredi : Ipswich contre Forest ; samedi : Chelsea contre Spurs.",
            "majorsDone": "Pro-Am termine mercredi. Butterfield Bermuda commence jeudi a Port Royal, champ de 120, Adam Schenk defend. Brennan a gagne le Baycurrent a -16.",
            "wnbaFirstRound": "Match 3 des Finales WNBA ce soir : Valkyries chez le Dream, serie a 1-1. Coup d'envoi 20 h 00 ET, State Farm Arena.",
            "bracketFootnote": "Match 1 : Valkyries 68, Dream 64. Match 2 : Dream 79, Valkyries 65. Match 3 ce soir mercredi 21 octobre, 20 h 00 ET, USA/Peacock/CNBC. Serie 1-1."
        }
    },
    "es": {
        "football": {
            "tagline": "Cigüeña el jueves: los Patriots visitan a los Bears. Los 49ers siguen 6-0.",
            "liveNow": "TNF jueves 8:15 p.m. ET: Patriots (4-2) en Bears (4-2), Prime Video, Chicago -3. Final del lunes: 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF MANANA: PATRIOTS EN BEARS (4-2)",
            "keywords": "NFL semana 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field"
        },
        "tennis": {
            "tagline": "Almaty miercoles: Tsitsipas supera a Kovacevic en tres. Khachanov resuelve ante Sakamoto.",
            "liveNow": "Almaty: Tsitsipas a Kovacevic 7-6(9), 3-6, 6-3. Khachanov a Sakamoto 6-2, 6-4. Duckworth a Darderi 7-5, 7-6(7). Lyon: Moutet a Humbert.",
            "pulse": "ALMATY: TSITSIPAS Y KHACHANOV A SEGUNDA RONDA",
            "keywords": "ATP, Almaty, Tsitsipas, Kovacevic, Khachanov, Duckworth, Lyon, Moutet"
        },
        "f1": {
            "tagline": "GP de Estados Unidos: a dos dias de los libres del viernes. Antonelli aventaja a Russell en 102.",
            "liveNow": "No se rueda el 21 de octubre. Fin de semana en COTA, 23-25 de octubre, carrera domingo 25 a las 15:00 local. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN EN DOS DIAS: ANTONELLI LLEVA 102",
            "keywords": "Formula 1, GP de Estados Unidos, Austin, COTA, Antonelli, Russell, Mercedes"
        },
        "soccer": {
            "tagline": "El Spurs asimila el 3-1 antes de ir a Chelsea. El City lidera por tres con 21.",
            "liveNow": "Posiciones: City 21, Arsenal 18, Brighton 16. Spurs 16o con 6, Coventry 17o con 6. Fecha 8 abre el viernes; Chelsea v Spurs el sabado.",
            "pulse": "PREMIER LEAGUE: CITY MANDA ANTE EL DERBI",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Maddison, Fecha 8"
        },
        "basketball": {
            "tagline": "Finales WNBA Juego 3 esta noche: Valkyries en Dream. La serie esta 1-1.",
            "liveNow": "Juego 3 miercoles 8:00 p.m. ET, State Farm Arena, USA/Peacock/CNBC. Sin marcador. Juego 2: Dream 79, Valkyries 65. Serie 1-1.",
            "pulse": "FINALES WNBA JUEGO 3 HOY: SERIE 1-1",
            "keywords": "WNBA Finales, Juego 3, Dream, Valkyries, Reese, State Farm Arena, 1-1"
        },
        "golf": {
            "tagline": "Finaliza el Pro-Am en Bermudas. Port Royal abre el jueves la primera ronda.",
            "liveNow": "Pro-Am concluido el miercoles. Campo de 120, bolsa de 6 millones, par 71. Adam Schenk defiende. Ronda 1 el jueves, Golf Channel 1-4 p.m. ET.",
            "pulse": "PORT ROYAL ABRE EL JUEVES: PRO-AM LISTO",
            "keywords": "PGA Tour, Bermudas, Port Royal, Adam Schenk, Pro-Am, Brennan"
        },
        "home": {
            "tonight": "Mesa del miercoles",
            "tonightBlurb": "Juego 3 de las Finales WNBA esta noche en Atlanta (1-1). Tsitsipas y Khachanov ganan en Almaty. Patriots en Bears el jueves.",
            "plTitle": "Premier League: el City mantiene tres de ventaja mientras Spurs prepara Chelsea",
            "plBlurb": "Spurs 16o con 6 puntos tras vencer 3-1 a Coventry. City lidera con 21, Arsenal 18, Brighton 16. La fecha 8 empieza el viernes.",
            "f1Title": "Proxima carrera: GP de Estados Unidos en Austin",
            "f1Blurb": "Montaje de boxes en Austin. COTA del 23 al 25 de octubre, carrera el domingo 25 a las 15:00 local. Antonelli lidera por 102."
        },
        "pg": {
            "pinFinal": "Miercoles en Almaty: Tsitsipas a Kovacevic 7-6(9), 3-6, 6-3. Khachanov a Sakamoto 6-2, 6-4. Shangai sigue: Davidovich Fokina a Jodar.",
            "week1Closed": "Arranque semana 7 NFL: Patriots en Bears el jueves por la noche",
            "week1Sub": "Patriots en Bears en Soldier Field, 8:15 p.m. ET, Prime Video, Chicago -3. 49ers con 6-0. Chiefs y Vikings con 5-0.",
            "countdownTnf": "TNF jueves: Patriots en Bears. Final lunes: 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Las barras muestran la ventaja. Antonelli suma 340, 102 sobre Russell (238). A dos dias de las practicas en Austin.",
            "tableAfterMonday": "Premier League: City manda con 21 puntos. Arsenal 18, Brighton 16. Spurs 16o con 6 tras el 3-1.",
            "pinClub": "Elige club. City marcha 7-0-0 con 21. Arsenal 18, Brighton 16. Spurs vencio a Coventry 3-1. Fecha 8 arranca el viernes.",
            "plFootnote": "Final lunes: Tottenham 3, Coventry 1. La jornada 8 abre el viernes: Ipswich v Forest; sabado: Chelsea v Spurs.",
            "majorsDone": "Pro-Am cerrado el miercoles. Butterfield Bermuda abre el jueves en Port Royal, campo de 120, Adam Schenk defiende. Brennan gano Baycurrent con -16.",
            "wnbaFirstRound": "Juego 3 de las Finales WNBA esta noche: Valkyries en Dream, serie 1-1. Salto 8:00 p.m. ET, State Farm Arena.",
            "bracketFootnote": "Juego 1: Valkyries 68, Dream 64. Juego 2: Dream 79, Valkyries 65. Juego 3 esta noche miercoles 21 de octubre, 8:00 p.m. ET, USA/Peacock/CNBC. Serie 1-1."
        }
    },
    "de": {
        "football": {
            "tagline": "Donnerstag Kickoff: Patriots gastieren bei den Bears im Soldier Field. 49ers bleiben 6-0.",
            "liveNow": "TNF Donnerstag 20:15 ET: Patriots (4-2) bei den Bears (4-2), Prime Video, Chicago -3. Montag: 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF MORGEN: PATRIOTS BEI DEN BEARS (4-2)",
            "keywords": "NFL Woche 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field"
        },
        "tennis": {
            "tagline": "Almaty Mittwoch: Tsitsipas ringt Kovacevic in drei Saetzen nieder. Khachanov schlaegt Sakamoto.",
            "liveNow": "Almaty: Tsitsipas d. Kovacevic 7-6(9), 3-6, 6-3. Khachanov d. Sakamoto 6-2, 6-4. Duckworth d. Darderi 7-5, 7-6(7). Lyon: Moutet d. Humbert.",
            "pulse": "ALMATY: TSITSIPAS UND KHACHANOV IM ACHTELFINALE",
            "keywords": "ATP, Almaty, Tsitsipas, Kovacevic, Khachanov, Duckworth, Lyon, Moutet"
        },
        "f1": {
            "tagline": "GP der USA: Zwei Tage bis zum Freitagstraining. Antonelli fuehrt vor Russell mit 102 Punkten.",
            "liveNow": "Kein Fahrbetrieb am 21. Oktober. COTA-Wochenende 23.-25. Oktober, Rennen Sonntag 25. Oktober um 15:00 Ortszeit. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN IN ZWEI TAGEN: ANTONELLI FUEHRT MIT 102",
            "keywords": "Formel 1, GP der USA, Austin, COTA, Antonelli, Russell, Mercedes"
        },
        "soccer": {
            "tagline": "Spurs verarbeiten 3-1 vor Chelsea-Duell. City fuehrt Tabelle mit drei Punkten Vorsprung an.",
            "liveNow": "Tabelle: City 21, Arsenal 18, Brighton 16. Spurs 16. mit 6, Coventry 17. mit 6. Spieltag 8 startet Freitag; Chelsea v Spurs Samstag.",
            "pulse": "PREMIER LEAGUE: CITY VORN VOR DEM DERBY",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Maddison, Spieltag 8"
        },
        "basketball": {
            "tagline": "WNBA-Finals Spiel 3 heute Abend: Valkyries beim Dream. Serie steht 1-1.",
            "liveNow": "Spiel 3 Mittwoch 20:00 ET, State Farm Arena, USA/Peacock/CNBC. Noch kein Score. Spiel 2: Dream 79, Valkyries 65. Serie 1-1.",
            "pulse": "WNBA-FINALS SPIEL 3 HEUTE: SERIE 1-1",
            "keywords": "WNBA Finals, Spiel 3, Dream, Valkyries, Reese, State Farm Arena, 1-1"
        },
        "golf": {
            "tagline": "Mittwochs-Pro-Am auf Bermuda beendet. Port Royal oeffnet Donnerstag fuer Runde 1.",
            "liveNow": "Pro-Am am Mittwoch abgeschlossen. Feld von 120, 6 Mio. Dollar Preisgeld, Par 71. Adam Schenk verteidigt. Runde 1 Donnerstag, Golf Channel 13-16 Uhr ET.",
            "pulse": "PORT ROYAL OEFFNET DONNERSTAG: PRO-AM DURCH",
            "keywords": "PGA Tour, Bermuda, Port Royal, Adam Schenk, Pro-Am, Brennan"
        },
        "home": {
            "tonight": "Mittwochs-Pult",
            "tonightBlurb": "WNBA-Finals Spiel 3 heute Abend in Atlanta (1-1). Tsitsipas und Khachanov siegen in Almaty. Patriots bei den Bears am Donnerstag.",
            "plTitle": "Premier League: City haelt Drei-Punkte-Vorsprung vor Tottenham-Trip nach Chelsea",
            "plBlurb": "Spurs 16. mit 6 Punkten nach 3-1 gegen Coventry. City fuehrt mit 21, Arsenal 18, Brighton 16. Spieltag 8 beginnt am Freitag.",
            "f1Title": "Naechstes Rennen: GP der USA in Austin",
            "f1Blurb": "Paddock-Aufbau in Austin. COTA-Wochenende 23.-25. Oktober, Rennen Sonntag 25. Oktober um 15:00 Ortszeit. Antonelli vorn mit 102."
        },
        "pg": {
            "pinFinal": "Mittwoch in Almaty: Tsitsipas d. Kovacevic 7-6(9), 3-6, 6-3. Khachanov d. Sakamoto 6-2, 6-4. Shanghai bleibt: Davidovich Fokina d. Jodar.",
            "week1Closed": "NFL Woche 7 Auftakt: Patriots bei den Bears am Donnerstagabend",
            "week1Sub": "Patriots bei den Bears im Soldier Field, 20:15 ET, Prime Video, Chicago -3. 49ers stehen 6-0. Chiefs und Vikings 5-0.",
            "countdownTnf": "TNF Donnerstag: Patriots bei den Bears. Montag Endstand: 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Balken zeigen Rueckstand. Antonelli hat 340, 102 vor Russell (238). Noch zwei Tage bis zum Training in Austin.",
            "tableAfterMonday": "Premier League: City fuehrt mit 21 Punkten. Arsenal 18, Brighton 16. Spurs 16. mit 6 nach dem 3-1.",
            "pinClub": "Club waehlen. City steht 7-0-0 bei 21 Punkten. Arsenal 18, Brighton 16. Spurs schlugen Coventry 3-1. Spieltag 8 startet Freitag.",
            "plFootnote": "Montag Endstand: Tottenham 3, Coventry 1. Spieltag 8 startet Freitag: Ipswich v Forest; Samstag: Chelsea v Spurs.",
            "majorsDone": "Mittwochs-Pro-Am beendet. Butterfield Bermuda startet Donnerstag in Port Royal, Feld von 120, Adam Schenk verteidigt. Brennan siegte mit -16.",
            "wnbaFirstRound": "WNBA-Finals Spiel 3 heute Abend: Valkyries beim Dream, Serie 1-1. Tip-off 20:00 ET, State Farm Arena.",
            "bracketFootnote": "Spiel 1: Valkyries 68, Dream 64. Spiel 2: Dream 79, Valkyries 65. Spiel 3 heute Mittwoch 21. Oktober, 20:00 ET, USA/Peacock/CNBC. Serie 1-1."
        }
    },
    "it": {
        "football": {
            "tagline": "Calcio d'inizio giovedi: i Patriots fanno visita ai Bears. I 49ers restano 6-0.",
            "liveNow": "TNF giovedi 20:15 ET: Patriots (4-2) dai Bears (4-2), Prime Video, Chicago -3. Finale lunedi: 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF DOMANI: PATRIOTS DAI BEARS (4-2)",
            "keywords": "NFL Week 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field"
        },
        "tennis": {
            "tagline": "Almaty mercoledi: Tsitsipas supera Kovacevic in tre set. Khachanov batte Sakamoto.",
            "liveNow": "Almaty: Tsitsipas batte Kovacevic 7-6(9), 3-6, 6-3. Khachanov batte Sakamoto 6-2, 6-4. Duckworth batte Darderi 7-5, 7-6(7). Lione: Moutet batte Humbert.",
            "pulse": "ALMATY: TSITSIPAS E KHACHANOV AGLI OTTAVI",
            "keywords": "ATP, Almaty, Tsitsipas, Kovacevic, Khachanov, Duckworth, Lione, Moutet"
        },
        "f1": {
            "tagline": "GP degli Stati Uniti: due giorni alle libere del venerdi. Antonelli precede Russell di 102.",
            "liveNow": "Nessuna sessione il 21 ottobre. Weekend COTA 23-25 ottobre, gara domenica 25 alle 15:00 locali. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN TRA DUE GIORNI: ANTONELLI A +102",
            "keywords": "Formula 1, GP Stati Uniti, Austin, COTA, Antonelli, Russell, Mercedes"
        },
        "soccer": {
            "tagline": "Gli Spurs metabolizzano il 3-1 prima del Chelsea. Il City guida con tre punti a quota 21.",
            "liveNow": "Classifica: City 21, Arsenal 18, Brighton 16. Spurs 16i con 6, Coventry 17i con 6. Week 8 al via venerdi; Chelsea v Spurs sabato.",
            "pulse": "PREMIER LEAGUE: CITY IN TESTA VERSO IL DERBY",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Maddison, Week 8"
        },
        "basketball": {
            "tagline": "Finali WNBA Gara 3 stasera: Valkyries in casa del Dream. Serie sull'1-1.",
            "liveNow": "Gara 3 mercoledi 20:00 ET, State Farm Arena, USA/Peacock/CNBC. Nessun punteggio. Gara 2: Dream 79, Valkyries 65. Serie 1-1.",
            "pulse": "FINALI WNBA GARA 3 STASERA: SERIE 1-1",
            "keywords": "WNBA Finali, Gara 3, Dream, Valkyries, Reese, State Farm Arena, 1-1"
        },
        "golf": {
            "tagline": "Chiuso il Pro-Am alle Bermuda. Port Royal apre giovedi per il primo giro.",
            "liveNow": "Pro-Am completato mercoledi. Campo da 120, montepremi 6 milioni, par 71. Adam Schenk difende il titolo. Giro 1 giovedi, Golf Channel 13-16 ET.",
            "pulse": "PORT ROYAL APRE GIOVEDI: PRO-AM CHIUSO",
            "keywords": "PGA Tour, Bermuda, Port Royal, Adam Schenk, Pro-Am, Brennan"
        },
        "home": {
            "tonight": "Banco del mercoledi",
            "tonightBlurb": "Finali WNBA Gara 3 stasera ad Atlanta (1-1). Tsitsipas e Khachanov vincono ad Almaty. I Patriots visitano i Bears giovedi.",
            "plTitle": "Premier League: City a +3 mentre gli Spurs preparano la sfida al Chelsea",
            "plBlurb": "Spurs 16i a 6 punti dopo il 3-1 al Coventry. City in testa a 21, Arsenal 18, Brighton 16. La giornata 8 inizia venerdi.",
            "f1Title": "Prossima gara: GP degli Stati Uniti ad Austin",
            "f1Blurb": "Allestimento box ad Austin. Weekend COTA 23-25 ottobre, gara domenica 25 alle 15:00 locali. Antonelli guida con 102 di vantaggio."
        },
        "pg": {
            "pinFinal": "Mercoledi ad Almaty: Tsitsipas batte Kovacevic 7-6(9), 3-6, 6-3. Khachanov batte Sakamoto 6-2, 6-4. Shanghai resta: Davidovich Fokina batte Jodar.",
            "week1Closed": "Kickoff Week 7 NFL: Patriots dai Bears giovedi notte",
            "week1Sub": "Patriots dai Bears al Soldier Field, 20:15 ET, Prime Video, Chicago -3. 49ers sul 6-0. Chiefs e Vikings a 5-0.",
            "countdownTnf": "TNF giovedi: Patriots dai Bears. Finale lunedi: 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Le barre indicano il distacco. Antonelli a 340, 102 davanti a Russell (238). Due giorni al via delle libere ad Austin.",
            "tableAfterMonday": "Premier League: City primo con 21 punti. Arsenal 18, Brighton 16. Spurs 16i con 6 punti dopo il 3-1.",
            "pinClub": "Scegli un club. City 7-0-0 a 21 punti. Arsenal 18, Brighton 16. Gli Spurs battono il Coventry 3-1. Week 8 al via venerdi.",
            "plFootnote": "Finale lunedi: Tottenham 3, Coventry 1. La giornata 8 apre venerdi: Ipswich v Forest; sabato: Chelsea v Spurs.",
            "majorsDone": "Pro-Am chiuso mercoledi. Butterfield Bermuda al via giovedi a Port Royal, campo da 120, Adam Schenk difende. Brennan ha vinto a -16.",
            "wnbaFirstRound": "Finali WNBA Gara 3 stasera: Valkyries dal Dream, serie sull'1-1. Palla a due 20:00 ET, State Farm Arena.",
            "bracketFootnote": "Gara 1: Valkyries 68, Dream 64. Gara 2: Dream 79, Valkyries 65. Gara 3 stasera mercoledi 21 ottobre, 20:00 ET, USA/Peacock/CNBC. Serie 1-1."
        }
    },
    "pl": {
        "football": {
            "tagline": "Czwartkowy kickoff: Patriots odwiedzaja Bears na Soldier Field. 49ers maja 6-0.",
            "liveNow": "TNF czwartek 20:15 ET: Patriots (4-2) u Bears (4-2), Prime Video, Chicago -3. Poniedzialek: 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF JUTRO: PATRIOTS U BEARS (4-2)",
            "keywords": "NFL Tydzien 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field"
        },
        "tennis": {
            "tagline": "Almaty sroda: Tsitsipas pokonuje Kovacevicia w trzech setach. Khachanov ogrywa Sakamoto.",
            "liveNow": "Almaty: Tsitsipas pok. Kovacevicia 7-6(9), 3-6, 6-3. Khachanov pok. Sakamoto 6-2, 6-4. Duckworth pok. Darderiego 7-5, 7-6(7). Lyon: Moutet pok. Humberta.",
            "pulse": "ALMATY: TSITSIPAS I KHACHANOV W DRUGIEJ RUNDZIE",
            "keywords": "ATP, Almaty, Tsitsipas, Kovacevic, Khachanov, Duckworth, Lyon, Moutet"
        },
        "f1": {
            "tagline": "GP USA: dwa dni do piatkowych treningow. Antonelli prowadzi przed Russellem o 102 punkty.",
            "liveNow": "Brak jazd 21 pazdziernika. Weekend na COTA 23-25 pazdziernika, wyscig w niedziele 25 pazdziernika o 15:00. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN ZA DWA DNI: ANTONELLI PROWADZI O 102",
            "keywords": "Formula 1, GP USA, Austin, COTA, Antonelli, Russell, Mercedes"
        },
        "soccer": {
            "tagline": "Spurs ciesza sie z 3-1 przed wyjazdem na Chelsea. City prowadza z trzema punktami przewagi.",
            "liveNow": "Tabela: City 21, Arsenal 18, Brighton 16. Spurs 16. z 6 pkt, Coventry 17. z 6 pkt. Kolejka 8 rusza w piatek; Chelsea v Spurs w sobote.",
            "pulse": "PREMIER LEAGUE: CITY NA CZELE PRZED DERBAMI",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Maddison, Kolejka 8"
        },
        "basketball": {
            "tagline": "Finaly WNBA mecz 3 dzis wieczorem: Valkyries u Dream. Stan serii 1-1.",
            "liveNow": "Mecz 3 sroda 20:00 ET, State Farm Arena, USA/Peacock/CNBC. Brak wyniku. Mecz 2: Dream 79, Valkyries 65. Seria 1-1.",
            "pulse": "FINALY WNBA MECZ 3 DZIS: SERIA 1-1",
            "keywords": "WNBA Finaly, mecz 3, Dream, Valkyries, Reese, State Farm Arena, 1-1"
        },
        "golf": {
            "tagline": "Srodowy Pro-Am na Bermudach zakonczony. Port Royal otwiera 1. runde w czwartek.",
            "liveNow": "Pro-Am ukonczony w srode. Stawka 120 graczy, pula 6 mln dol., par 71. Adam Schenk broni tytulu. Runda 1 czwartek, Golf Channel 13-16 ET.",
            "pulse": "PORT ROYAL RUSZA W CZWARTEK: PRO-AM ZAMKNIETY",
            "keywords": "PGA Tour, Bermudy, Port Royal, Adam Schenk, Pro-Am, Brennan"
        },
        "home": {
            "tonight": "Biurko srodowe",
            "tonightBlurb": "Finaly WNBA mecz 3 dzis w Atlancie (1-1). Tsitsipas i Khachanov wygrywaja w Almatach. Patriots u Bears w czwartek.",
            "plTitle": "Premier League: City z trzema punktami przewagi, Spurs szykuja sie na Chelsea",
            "plBlurb": "Spurs 16. z 6 punktami po wygranej 3-1 z Coventry. City prowadza z 21, Arsenal 18, Brighton 16. Kolejka 8 od piatku.",
            "f1Title": "Nastepny wyscig: GP USA w Austin",
            "f1Blurb": "Przygotowania w padoku w Austin. Weekend COTA 23-25 pazdziernika, wyscig w niedziele o 15:00. Antonelli ma 102 pkt przewagi."
        },
        "pg": {
            "pinFinal": "Sroda w Almatach: Tsitsipas pok. Kovacevicia 7-6(9), 3-6, 6-3. Khachanov pok. Sakamoto 6-2, 6-4. Szanghaj trwa: Davidovich Fokina pok. Jodara.",
            "week1Closed": "Inauguracja 7. tygodnia NFL: Patriots u Bears w czwartek wieczorem",
            "week1Sub": "Patriots u Bears na Soldier Field, 20:15 ET, Prime Video, Chicago -3. 49ers maja 6-0. Chiefs i Vikings 5-0.",
            "countdownTnf": "TNF czwartek: Patriots u Bears. Poniedzialek: 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Slupki pokazuja strate. Antonelli ma 340, 102 przed Russellem (238). Dwa dni do treningow w Austin.",
            "tableAfterMonday": "Premier League: City prowadza z 21 punktami. Arsenal 18, Brighton 16. Spurs 16. z 6 pkt po wygranej 3-1.",
            "pinClub": "Wybierz klub. City maja 7-0-0 i 21 pkt. Arsenal 18, Brighton 16. Spurs pokonali Coventry 3-1. Kolejka 8 startuje w piatek.",
            "plFootnote": "Wynik poniedzialku: Tottenham 3, Coventry 1. Kolejka 8 otwiera sie w piatek: Ipswich v Forest; sobota: Chelsea v Spurs.",
            "majorsDone": "Pro-Am zamkniety w srode. Butterfield Bermuda rusza w czwartek w Port Royal, 120 graczy, broni Adam Schenk. Brennan wygral z -16.",
            "wnbaFirstRound": "Mecz 3 finalow WNBA dzis wieczorem: Valkyries u Dream, seria 1-1. Poczatek 20:00 ET, State Farm Arena.",
            "bracketFootnote": "Mecz 1: Valkyries 68, Dream 64. Mecz 2: Dream 79, Valkyries 65. Mecz 3 dzis sroda 21 pazdziernika, 20:00 ET, USA/Peacock/CNBC. Seria 1-1."
        }
    },
    "zh": {
        "football": {
            "tagline": "周四开踢：爱国者客战士兵球场的熊。49人维持6胜0负。",
            "liveNow": "TNF周四美东晚8:15：爱国者(4-2)对熊(4-2)，Prime Video，芝加哥让3分。周一终场：49人23-17指挥官(49人6-0)。",
            "pulse": "TNF明日打响：爱国者客战熊(4-2)",
            "keywords": "NFL第7周, 爱国者, 熊, 49人, 指挥官, 酋长, 士兵球场"
        },
        "tennis": {
            "tagline": "阿拉木图周三：西西帕斯激战三盘险胜科瓦切维奇。哈恰诺夫完胜坂本怜。",
            "liveNow": "阿拉木图：西西帕斯胜科瓦切维奇 7-6(9), 3-6, 6-3。哈恰诺夫胜坂本怜 6-2, 6-4。达克沃斯胜达尔德里 7-5, 7-6(7)。里昂：穆泰胜安贝尔。",
            "pulse": "阿拉木图：西西帕斯与哈恰诺夫挺进16强",
            "keywords": "ATP, 阿拉木图, 西西帕斯, 科瓦切维奇, 哈恰诺夫, 达克沃斯, 里昂, 穆泰"
        },
        "f1": {
            "tagline": "美国大奖赛：距离周五练习赛还有两天。安东内利领先拉塞尔102分。",
            "liveNow": "10月21日无赛道计时。美洲赛道周末10月23-25日，正赛周日当地时间15:00。安东内利340，拉塞尔238。梅赛德斯578。",
            "pulse": "奥斯汀进入倒计时两天：安东内利领跑102分",
            "keywords": "F1, 美国大奖赛, 奥斯汀, COTA, 安东内利, 拉塞尔, 梅赛德斯"
        },
        "soccer": {
            "tagline": "热刺迎战切尔西前收获首胜。曼城积21分保有3分优势领跑。",
            "liveNow": "积分榜：曼城21分，阿森纳18分，布莱顿16分。热刺第16积6分，考文垂第17积6分。第8轮周五开打；周六切尔西对热刺。",
            "pulse": "英超：德比周末临近 曼城领跑积分榜",
            "keywords": "英超, 曼城, 阿森纳, 热刺, 切尔西, 考文垂, 麦迪逊, 第8轮"
        },
        "basketball": {
            "tagline": "今晚WNBA总决赛第3战：女武神客场战梦想。总比分1-1战平。",
            "liveNow": "第3战周三美东晚8:00，州立农业球馆，USA/Peacock/CNBC。尚未开赛。第2战：梦想79-65女武神。系列赛1-1。",
            "pulse": "今晚WNBA总决赛第3战：战成1-1平",
            "keywords": "WNBA总决赛, 第3战, 梦想, 女武神, 里斯, 州立农业球馆, 1-1"
        },
        "golf": {
            "tagline": "百慕大周三配对赛落幕。皇家港球场周四打响首轮较量。",
            "liveNow": "周三配对赛结束。120名球员，总奖金600万美元，标准杆71杆。亚当·申克卫冕。首轮周四高尔夫频道美东下午1-4点直播。",
            "pulse": "皇家港周四开杆：配对赛顺利收官",
            "keywords": "美巡赛, 百慕大, 皇家港, 亚当申克, 配对赛, 布伦南"
        },
        "home": {
            "tonight": "周三工作台",
            "tonightBlurb": "WNBA总决赛第3战今晚在亚特兰大打响（1-1）。西西帕斯与哈恰诺夫在阿拉木图取胜。周四爱国者挑战熊。",
            "plTitle": "英超：曼城手握3分领跑 热刺全力备战切尔西",
            "plBlurb": "热刺3-1击败考文垂积6分升至第16。曼城21分领跑，阿森纳18分，布莱顿16分。第8轮周五开战。",
            "f1Title": "下一站比赛：奥斯汀美国大奖赛",
            "f1Blurb": "奥斯汀围场搭建中。美洲赛道周末10月23-25日，正赛周日当地15:00。安东内利领先102分。"
        },
        "pg": {
            "pinFinal": "阿拉木图周三：西西帕斯胜科瓦切维奇 7-6(9), 3-6, 6-3。哈恰诺夫胜坂本怜 6-2, 6-4。上海站依然：达维多维奇胜霍达尔。",
            "week1Closed": "NFL第7周开幕：周四夜赛爱国者客战熊",
            "week1Sub": "士兵球场爱国者对熊，美东晚8:15，Prime Video，芝加哥让3分。49人保持6-0。酋长与维京人5-0。",
            "countdownTnf": "TNF周四：爱国者对熊。周一终场：49人23-17指挥官(49人6-0)。酋长22-6，比尔33-30。",
            "barsPoints": "条形图显示与领头羊的分差。安东内利积340分领先拉塞尔（238分）102分。奥斯汀周五练习赛进入两天倒计时。",
            "tableAfterMonday": "英超积分榜：曼城21分领跑。阿森纳18分，布莱顿16分。热刺3-1获胜后积6分位列第16。",
            "pinClub": "选择俱乐部。曼城7战全胜积21分。阿森纳18分，布莱顿16分。热刺3-1击败考文垂。第8轮周五开打。",
            "plFootnote": "周一终场：托特纳姆3-1考文垂。第8轮周五打响：伊普斯维奇对森林；周六：切尔西对热刺。",
            "majorsDone": "配对赛周三结束。百慕大锦标赛周四在皇家港开打，120名球员，亚当·申克卫冕。布伦南低于标准杆16杆夺冠记录保持。",
            "wnbaFirstRound": "WNBA总决赛第3战今晚：女武神客场对梦想，系列赛1-1。美东晚8:00州立农业球馆开赛。",
            "bracketFootnote": "第1战：女武神68-64梦想。第2战：梦想79-65女武神。第3战今晚10月21日周三美东晚8:00，USA/Peacock/CNBC。系列赛1-1。"
        }
    },
    "ja": {
        "football": {
            "tagline": "木曜キックオフ：ペイトリオッツがソルジャー・フィールドのベアーズを訪問。49ersは6勝0敗を維持。",
            "liveNow": "TNF木曜東部午後8時15分：ペイトリオッツ(4-2)対ベアーズ(4-2)、Prime Video、シカゴ3点リード。月曜最終：49ers 23-17 コマンダーズ(49ers 6-0)。",
            "pulse": "TNF明日開幕：ペイトリオッツ対ベアーズ(4-2)",
            "keywords": "NFL第7週, ペイトリオッツ, ベアーズ, 49ers, コマンダーズ, チーフス, ソルジャーフィールド"
        },
        "tennis": {
            "tagline": "水曜アルマティ：チチパスが3セットでコバチェビッチを下す。ハチャノフは坂本怜に快勝。",
            "liveNow": "アルマティ：チチパス勝コバチェビッチ 7-6(9), 3-6, 6-3。ハチャノフ勝坂本怜 6-2, 6-4。ダックワース勝ダルデリ 7-5, 7-6(7)。リヨン：ミュテ勝アンベール。",
            "pulse": "アルマティ：チチパスとハチャノフが2回戦へ",
            "keywords": "ATP, アルマティ, チチパス, コバチェビッチ, ハチャノフ, ダックワース, リヨン, ミュテ"
        },
        "f1": {
            "tagline": "アメリカGP：金曜フリー走行まであと2日。アントネッリがラッセルに102点リード。",
            "liveNow": "10月21日は走行なし。COTA週末は10月23-25日、決勝は日曜現地15:00。アントネッリ340、ラッセル238。メルセデス578。",
            "pulse": "オースティンまで2日：アントネッリが102点リード",
            "keywords": "F1, アメリカGP, オースティン, COTA, アントネッリ, ラッセル, メルセデス"
        },
        "soccer": {
            "tagline": "トッテナムが初勝利で一息、チェルシー戦へ。マンチェスター・Cは勝ち点3差で首位。",
            "liveNow": "順位：シティ21、アーセナル18、ブライトン16。スパーズ16位(6点)、コベントリー17位(6点)。第8節は金曜開幕、土曜にチェルシー対スパーズ。",
            "pulse": "プレミアリーグ：ダービー前、シティが首位快走",
            "keywords": "プレミアリーグ, シティ, アーセナル, スパーズ, チェルシー, コベントリー, マディソン, 第8節"
        },
        "basketball": {
            "tagline": "今夜WNBAファイナル第3戦：ヴァルキリーズ対ドリーム。1勝1敗の対決。",
            "liveNow": "第3戦水曜東部午後8時、ステートファーム・アリーナ、USA/Peacock/CNBC。スコアなし。第2戦：ドリーム 79-65 ヴァルキリーズ。シリーズ1-1。",
            "pulse": "WNBAファイナル第3戦今夜：1勝1敗",
            "keywords": "WNBAファイナル, 第3戦, ドリーム, ヴァルキリーズ, リース, ステートファームアリーナ, 1-1"
        },
        "golf": {
            "tagline": "バミューダで水曜プロアマ終了。ポートロイヤルが木曜に第1ラウンド開幕。",
            "liveNow": "プロアマ水曜終了。120名、賞金総額600万ドル、パー71。アダム・シェンク連覇挑戦。第1R木曜、ゴルフチャンネル東部13-16時生中継。",
            "pulse": "ポートロイヤル木曜開幕：プロアマ終了",
            "keywords": "PGAツアー, バミューダ, ポートロイヤル, アダムシェンク, プロアマ, ブレナン"
        },
        "home": {
            "tonight": "水曜デスク",
            "tonightBlurb": "今夜アトランタでWNBAファイナル第3戦（1-1）。チチパスとハチャノフがアルマティで勝利。木曜にペイトリオッツ対ベアーズ。",
            "plTitle": "プレミアリーグ：マンチェスター・Cが勝ち点3差で首位、スパーズはチェルシー戦へ",
            "plBlurb": "スパーズはコベントリーに3-1で勝ち勝ち点6の16位。シティ21点、アーセナル18点、ブライトン16点。第8節は金曜開幕。",
            "f1Title": "次戦：オースティンでのアメリカGP",
            "f1Blurb": "オースティンでパドック設営中。COTA週末は10月23-25日、決勝は日曜現地15:00。アントネッリが102点リード。"
        },
        "pg": {
            "pinFinal": "水曜アルマティ：チチパス勝コバチェビッチ 7-6(9), 3-6, 6-3。ハチャノフ勝坂本 6-2, 6-4。上海：ダビドビッチ勝ホダル。",
            "week1Closed": "NFL第7週キックオフ：木曜夜にペイトリオッツ対ベアーズ",
            "week1Sub": "ソルジャー・フィールドでペイトリオッツ対ベアーズ、東部午後8時15分、Prime Video、シカゴ3点優勢。49ersは6勝0敗。チーフスとバイキングスは5勝0敗。",
            "countdownTnf": "TNF木曜：ペイトリオッツ対ベアーズ。月曜最終：49ers 23-17 コマンダーズ(49ers 6-0)。チーフス22-6、ビルズ33-30。",
            "barsPoints": "バーは首位との差を表示。アントネッリ340点でラッセル（238点）に102点リード。オースティン走行開始まであと2日。",
            "tableAfterMonday": "プレミアリーグ：マンチェスター・Cが勝ち点21で首位。アーセナル18、ブライトン16。スパーズは3-1で勝ち点6の16位。",
            "pinClub": "クラブを選択。シティは7戦全勝の21点。アーセナル18、ブライトン16。スパーズはコベントリーを3-1で下す。第8節は金曜開幕。",
            "plFootnote": "月曜最終：トッテナム 3-1 コベントリー。第8節は金曜開幕：イプスウィッチ対フォレスト、土曜にチェルシー対スパーズ。",
            "majorsDone": "水曜プロアマ終了。バターフィールド・バミューダは木曜ポートロイヤルで開幕、120名、アダム・シェンク連覇挑戦。ブレナンが16アンダーで勝利。",
            "wnbaFirstRound": "WNBAファイナル第3戦今夜：ヴァルキリーズ対ドリーム、シリーズ1-1。東部午後8時、ステートファーム・アリーナ。",
            "bracketFootnote": "第1戦：ヴァルキリーズ 68-64 ドリーム。第2戦：ドリーム 79-65 ヴァルキリーズ。第3戦は今夜10月21日水曜東部午後8時、USA/Peacock/CNBC。シリーズ1-1。"
        }
    },
    "ko": {
        "football": {
            "tagline": "목요일 킥오프: 패트리어츠가 솔저 필드의 베어스를 방문. 49ers는 6승 0패 유지.",
            "liveNow": "TNF 목요일 동부 저녁 8:15: 패트리어츠(4-2) 대 베어스(4-2), Prime Video, 시카고 3점 우세. 월요일 최종: 49ers 23-17 커맨더스(49ers 6-0).",
            "pulse": "TNF 내일 개막: 패트리어츠 대 베어스(4-2)",
            "keywords": "NFL 7주차, 패트리어츠, 베어스, 49ers, 커맨더스, 치프스, 솔저필드"
        },
        "tennis": {
            "tagline": "알마티 수요일: 치치파스가 코바체비치와 3세트 접전 끝 승리. 하차노프는 사카모토 제압.",
            "liveNow": "알마티: 치치파스 승 코바체비치 7-6(9), 3-6, 6-3. 하차노프 승 사카모토 6-2, 6-4. 덕워스 승 다르데리 7-5, 7-6(7). 리옹: 무테 승 움베르.",
            "pulse": "알마티: 치치파스와 하차노프 16강 진출",
            "keywords": "ATP, 알마티, 치치파스, 코바체비치, 하차노프, 덕워스, 리옹, 무테"
        },
        "f1": {
            "tagline": "미국 GP: 금요일 연습 주행까지 이틀. 안토넬리가 러셀에 102점 차 리드.",
            "liveNow": "10월 21일 주행 없음. COTA 주말 10월 23-25일, 결승 일요일 현지 15:00. 안토넬리 340, 러셀 238. 메르세데스 578.",
            "pulse": "오스틴까지 이틀: 안토넬리 102점 차 리드",
            "keywords": "F1, 미국 GP, 오스틴, COTA, 안토넬리, 러셀, 메르세데스"
        },
        "soccer": {
            "tagline": "토트넘, 첼시 원정 전 3-1 첫 승 만끽. 맨시티 승점 3점 차 선두.",
            "liveNow": "순위: 맨시티 21, 아스널 18, 브라이턴 16. 토트넘 16위(6점), 코번트리 17위(6점). 8라운드 금요일 개막, 토요일 첼시 대 토트넘.",
            "pulse": "프리미어리그: 더비 앞두고 맨시티 선두",
            "keywords": "프리미어리그, 맨시티, 아스널, 토트넘, 첼시, 코번트리, 매디슨, 8라운드"
        },
        "basketball": {
            "tagline": "오늘 밤 WNBA 파이널 3차전: 발키리스 대 드림. 1승 1패 팽팽.",
            "liveNow": "3차전 수요일 동부 저녁 8:00, 스테이트팜 아레나, USA/Peacock/CNBC. 스코어 없음. 2차전: 드림 79-65 발키리스. 시리즈 1-1.",
            "pulse": "오늘 밤 WNBA 파이널 3차전: 1승 1패",
            "keywords": "WNBA 파이널, 3차전, 드림, 발키리스, 리스, 스테이트팜 아레나, 1-1"
        },
        "golf": {
            "tagline": "버뮤다 수요일 프로암 종료. 포트 로열 목요일 1라운드 개막.",
            "liveNow": "프로암 수요일 완료. 120명 출전, 총상금 600만 달러, 파71. 애덤 솅크 2연패 도전. 1R 목요일, 골프 채널 동부 13-16시 생중계.",
            "pulse": "포트 로열 목요일 개막: 프로암 종료",
            "keywords": "PGA 투어, 버뮤다, 포트 로열, 애덤 솅크, 프로암, 브레넌"
        },
        "home": {
            "tonight": "수요일 데스크",
            "tonightBlurb": "오늘 밤 애틀랜타에서 WNBA 파이널 3차전(1-1). 치치파스와 하차노프가 알마티에서 승리. 목요일 패트리어츠 대 베어스.",
            "plTitle": "프리미어리그: 맨시티 승점 3점 차 선두, 토트넘은 첼시전 대비",
            "plBlurb": "토트넘은 코번트리전 3-1 승리로 승점 6점 16위. 맨시티 21점, 아스널 18점, 브라이턴 16점. 8라운드는 금요일 개막.",
            "f1Title": "다음 경기: 오스틴 미국 GP",
            "f1Blurb": "오스틴 패덕 세팅 중. COTA 주말 10월 23-25일, 결승 일요일 현지 15:00. 안토넬리가 102점 차 리드."
        },
        "pg": {
            "pinFinal": "수요일 알마티: 치치파스 승 코바체비치 7-6(9), 3-6, 6-3. 하차노프 승 사카모토 6-2, 6-4. 상하이: 다비도비치 승 호다르.",
            "week1Closed": "NFL 7주차 개막: 목요일 밤 패트리어츠 대 베어스",
            "week1Sub": "솔저 필드에서 패트리어츠 대 베어스, 동부 저녁 8시 15분, Prime Video, 시카고 3점 우세. 49ers 6승 0패. 치프스와 바이킹스 5승 무패.",
            "countdownTnf": "TNF 목요일: 패트리어츠 대 베어스. 월요일 최종: 49ers 23-17 커맨더스(49ers 6-0). 치프스 22-6, 빌스 33-30.",
            "barsPoints": "막대는 선두와의 격차 표시. 안토넬리 340점으로 러셀(238점)에 102점 차 리드. 오스틴 주행까지 이틀.",
            "tableAfterMonday": "프리미어리그: 맨시티 승점 21점으로 선두. 아스널 18점, 브라이턴 16점. 토트넘 3-1 승리 후 16위(6점).",
            "pinClub": "클럽 선택. 맨시티는 7승 0무 0패 21점. 아스널 18, 브라이턴 16. 토트넘은 코번트리를 3-1로 꺾음. 8라운드 금요일 시작.",
            "plFootnote": "월요일 최종: 토트넘 3, 코번트리 1. 8라운드는 금요일 개막: 입스위치 대 포리스트, 토요일 첼시 대 토트넘.",
            "majorsDone": "수요일 프로암 종료. 버터필드 버뮤다는 목요일 포트 로열 개막, 120명, 애덤 솅크 타이틀 방어. 브레넌 16언더파 우승 유지.",
            "wnbaFirstRound": "WNBA 파이널 3차전 오늘 밤: 발키리스 대 드림, 시리즈 1-1. 동부 저녁 8시 스테이트팜 아레나.",
            "bracketFootnote": "1차전: 발키리스 68, 드림 64. 2차전: 드림 79, 발키리스 65. 3차전 오늘 10월 21일 수요일 동부 저녁 8시, USA/Peacock/CNBC. 시리즈 1-1."
        }
    },
    "ar": {
        "football": {
            "tagline": "ضربة البداية الخميس: باتريوتس يحل ضيفا على بيرز في سولجر فيلد. 49ers يستمر 6-0.",
            "liveNow": "TNF الخميس 8:15 مساء بتوقيت الشرق: باتريوتس (4-2) عند بيرز (4-2)، برايم فيديو، شيكاغو -3. نهاية الاثنين: 49ers 23، كوماندرز 17 (49ers 6-0).",
            "pulse": "TNF غدا: باتريوتس عند بيرز (4-2)",
            "keywords": "NFL الاسبوع 7, باتريوتس, بيرز, 49ers, كوماندرز, تشيفس, سولجر فيلد"
        },
        "tennis": {
            "tagline": "الماتي الاربعاء: تسيتسيباس يتفوق على كوفاسيفيتش في ثلاث مجموعات. وخاتشانوف يتجاوز ساكاموتو.",
            "liveNow": "الماتي: تسيتسيباس فاز على كوفاسيفيتش 7-6(9) و3-6 و6-3. خاتشانوف على ساكاموتو 6-2 و6-4. داكوورث على دارديري 7-5 و7-6(7). ليون: موتيه على هومبير.",
            "pulse": "الماتي: تسيتسيباس وخاتشانوف الى الدور الثاني",
            "keywords": "ATP, الماتي, تسيتسيباس, كوفاسيفيتش, خاتشانوف, داكوورث, ليون, موتيه"
        },
        "f1": {
            "tagline": "جائزة الولايات المتحدة: يومان على تجارب الجمعة. انتونيللي يتقدم بـ102 نقطة على راسل.",
            "liveNow": "لا تجارب في 21 اكتوبر. عطلة اوستن 23-25 اكتوبر، السباق الاحد 25 اكتوبر الساعة 15:00 بالتوقيت المحلي. انتونيللي 340، راسل 238. مرسيدس 578.",
            "pulse": "اوستن بعد يومين: انتونيللي يتقدم بـ102",
            "keywords": "فورمولا 1, جائزة الولايات المتحدة, اوستن, COTA, انتونيللي, راسل, مرسيدس"
        },
        "soccer": {
            "tagline": "توتنهام يستمتع بفوزه 3-1 قبل مواجهة تشيلسي. سيتي يتصدر بفارق 3 نقاط برصيد 21.",
            "liveNow": "الترتيب: سيتي 21، ارسنال 18، برايتون 16. توتنهام 16 برصيد 6، كوفنتري 17 برصيد 6. الجولة 8 تفتح الجمعة؛ تشيلسي ضد توتنهام السبت.",
            "pulse": "البريميرليج: سيتي في الصدارة مع اقتراب الديربي",
            "keywords": "البريميرليج, سيتي, ارسنال, توتنهام, تشيلسي, كوفنتري, ماديسون, الجولة 8"
        },
        "basketball": {
            "tagline": "المباراة 3 من نهائيات WNBA الليلة: فالكيريز عند دريم. السلسلة متعادلة 1-1.",
            "liveNow": "المباراة 3 الاربعاء 8:00 مساء بتوقيت الشرق، ستيت فارم ارينا، USA/Peacock/CNBC. بلا نتيجة. المباراة 2: دريم 79، فالكيريز 65. السلسلة 1-1.",
            "pulse": "المباراة 3 من نهائيات WNBA الليلة: 1-1",
            "keywords": "نهائيات WNBA, المباراة 3, دريم, فالكيريز, ريس, ستيت فارم ارينا, 1-1"
        },
        "golf": {
            "tagline": "اختتام منافسات برو-ام الاربعاء في برمودا. بورت رويال يفتتح الجولة 1 الخميس.",
            "liveNow": "اكتملت برو-ام الاربعاء. 120 لاعبا، جوائز 6 ملايين، معدل 71. ادم شينك يدافع. الجولة 1 الخميس، غولف تشانل 1-4 مساء بتوقيت الشرق.",
            "pulse": "بورت رويال يفتح الخميس: برو-ام اكتملت",
            "keywords": "PGA Tour, برمودا, بورت رويال, ادم شينك, برو-ام, برينان"
        },
        "home": {
            "tonight": "مكتب الاربعاء",
            "tonightBlurb": "المباراة 3 من نهائيات WNBA الليلة في اتلانتا (1-1). تسيتسيباس وخاتشانوف يفوزان في الماتي. باتريوتس عند بيرز الخميس.",
            "plTitle": "البريميرليج: سيتي يحافظ على فارق ثلاث نقاط وتوتنهام يستعد لتشيلسي",
            "plBlurb": "توتنهام 16 برصيد 6 نقاط بعد هزيمة كوفنتري 3-1. سيتي يتصدر بـ21، ارسنال 18، برايتون 16. الجولة 8 تبدا الجمعة.",
            "f1Title": "السباق التالي: جائزة الولايات المتحدة في اوستن",
            "f1Blurb": "تجهيز البادوك في اوستن. عطلة COTA بين 23-25 اكتوبر، السباق الاحد الساعة 15:00 محليا. انتونيللي يتصدر بفارق 102."
        },
        "pg": {
            "pinFinal": "اربعاء الماتي: تسيتسيباس على كوفاسيفيتش 7-6(9) و3-6 و6-3. خاتشانوف على ساكاموتو 6-2 و6-4. شنغهاي تبقى: دافيدوفيتش فوكينا على خودار.",
            "week1Closed": "انطلاق الاسبوع 7 في NFL: باتريوتس عند بيرز ليلة الخميس",
            "week1Sub": "باتريوتس عند بيرز في سولجر فيلد، 8:15 مساء بتوقيت الشرق، برايم فيديو، شيكاغو -3. 49ers عند 6-0. تشيفس وفايكنغز 5-0.",
            "countdownTnf": "TNF الخميس: باتريوتس عند بيرز. نهاية الاثنين: 49ers 23، كوماندرز 17 (49ers 6-0). تشيفس 22-6، بيلز 33-30.",
            "barsPoints": "الاعمدة تظهر الفارق عن المتصدر. انتونيللي يملك 340، بزيادة 102 على راسل (238). يومان على تجارب اوستن.",
            "tableAfterMonday": "البريميرليج: سيتي يتصدر برصيد 21 نقطة. ارسنال 18، برايتون 16. توتنهام 16 برصيد 6 نقاط بعد الفوز 3-1.",
            "pinClub": "اختر ناديا. سيتي 7-0-0 برصيد 21 نقطة. ارسنال 18، برايتون 16. توتنهام فاز على كوفنتري 3-1. الجولة 8 تنطلق الجمعة.",
            "plFootnote": "نهاية الاثنين: توتنهام 3، كوفنتري 1. الجولة 8 تفتح الجمعة: ابسويتش ضد فورست؛ السبت: تشيلسي ضد توتنهام.",
            "majorsDone": "اختتام برو-ام الاربعاء. بطولة برمودا تفتح الخميس في بورت رويال، 120 لاعبا، ادم شينك يدافع. برينان فاز بـ16 تحت المعدل.",
            "wnbaFirstRound": "نهائيات WNBA المباراة 3 الليلة: فالكيريز عند دريم، السلسلة 1-1. البداية 8:00 مساء بتوقيت الشرق، ستيت فارم ارينا.",
            "bracketFootnote": "المباراة 1: فالكيريز 68، دريم 64. المباراة 2: دريم 79، فالكيريز 65. المباراة 3 الليلة الاربعاء 21 اكتوبر، 8:00 مساء بتوقيت الشرق، USA/Peacock/CNBC. السلسلة 1-1."
        }
    }
}

# Verify no em-dash or double-hyphen in any translation string
for lang, sections in DATA.items():
    for sec, keys in sections.items():
        for k, v in keys.items():
            assert "—" not in v, f"Em-dash in {lang}.{sec}.{k}: {v}"
            assert "--" not in v, f"Double-hyphen in {lang}.{sec}.{k}: {v}"

print("All translations verified! No em-dashes or double-hyphens.")

# 1. Update frontend/src/i18n/playground.ts
pg_file = "frontend/src/i18n/playground.ts"
with open(pg_file, "r", encoding="utf-8") as f:
    pg_content = f.read()

for lang, val in DATA.items():
    pg_vals = val["pg"]
    # We want to replace the fields in PLAYGROUND[lang]
    # Find block for lang
    pattern = rf'("{lang}":\s*\{{)(.*?)(\n  \}})'
    match = re.search(pattern, pg_content, re.DOTALL)
    if match:
        block = match.group(2)
        for k, text in pg_vals.items():
            # replace `"k": "..."`
            field_pattern = rf'("{k}":\s*)"(.*?)"'
            clean_text = text.replace('"', '\\"')
            block = re.sub(field_pattern, rf'\1"{clean_text}"', block)
        pg_content = pg_content[:match.start(2)] + block + pg_content[match.end(2):]
    else:
        print(f"Warning: lang block for {lang} not matched in playground.ts")

with open(pg_file, "w", encoding="utf-8") as f:
    f.write(pg_content)
print("Updated frontend/src/i18n/playground.ts")

# 2. Update frontend/src/i18n/messages.ts (en and fr)
msg_file = "frontend/src/i18n/messages.ts"
with open(msg_file, "r", encoding="utf-8") as f:
    msg_content = f.read()

def update_messages_dict(content, lang, prefix=""):
    data = DATA[lang]
    # update sports
    for sport_name, fields in [("football", data["football"]), ("tennis", data["tennis"]), ("f1", data["f1"]), ("soccer", data["soccer"]), ("basketball", data["basketball"]), ("golf", data["golf"])]:
        # find sport block
        for k, text in fields.items():
            # pattern within sport_name
            clean_text = text.replace('"', '\\"')
            # We look for tagline/liveNow/pulse/keywords under sport_name
            # Search after sport_name
            idx = content.find(f"{sport_name}: {{", prefix) if prefix else content.find(f"{sport_name}: {{")
            if idx != -1:
                end_idx = content.find("},", idx)
                sport_block = content[idx:end_idx]
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

# In messages.ts, first block is en, second is fr
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

print("All locale updates completed!")
