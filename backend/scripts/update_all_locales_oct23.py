# -*- coding: utf-8 -*-
import re
import os

DATA = {
    "en": {
        "football": {
            "tagline": "Thursday Night Football final: Bears edge Patriots 30-24 at Soldier Field. Chicago moves to 5-2.",
            "liveNow": "TNF Final: Bears 30, Patriots 24. Williams 308 pass yds, 2 TD; Santos 58-yd FG. Bears 5-2, Patriots 4-3. 49ers 6-0.",
            "pulse": "TNF FINAL: BEARS 30, PATRIOTS 24",
            "keywords": "NFL Week 7, Bears, Patriots, Caleb Williams, Drake Maye, Cairo Santos, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Almaty Friday: Tsitsipas beats Duckworth in straight sets to reach semifinals.",
            "liveNow": "Almaty QF: Tsitsipas d. Duckworth 6-3, 6-4. Bublik d. Khachanov 4-6, 7-6, 7-6. Medvedev d. Atmane 6-4, 6-4. Basilashvili d. Mannarino 6-3, 6-1.",
            "pulse": "ALMATY: TSITSIPAS AND BUBLIK REACH SEMIFINALS",
            "keywords": "ATP, Almaty, Tsitsipas, Duckworth, Bublik, Khachanov, Medvedev, Basilashvili"
        },
        "f1": {
            "tagline": "Friday practice underway at COTA: Antonelli and Russell begin US Grand Prix running.",
            "liveNow": "Austin Friday: Practice 1 and 2 at COTA. Race Sunday 25 October at 15:00 local. Antonelli 340, Russell 238 (gap 102). Mercedes 578.",
            "pulse": "AUSTIN PRACTICE UNDERWAY: ANTONELLI LEADS BY 102",
            "keywords": "Formula 1, United States GP, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "Matchweek 8 opens tonight with Ipswich v Forest. City lead table by three on 21.",
            "liveNow": "MW8 Friday 20:00 UK: Ipswich v Forest at Portman Road. City 21 (7-0-0), Arsenal 18, Brighton 16. Chelsea v Spurs Saturday.",
            "pulse": "PREMIER LEAGUE: MW8 OPENS TONIGHT AT IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Ipswich, Forest, MW8"
        },
        "basketball": {
            "tagline": "WNBA Finals Game 4: Dream chase first franchise crown with 2-1 series lead in Atlanta.",
            "liveNow": "Game 4 at State Farm Arena: Dream lead 2-1 after 97-71 blowout. Reese historic 3rd Finals double-double. Valkyries face elimination.",
            "pulse": "WNBA FINALS: DREAM CHASE TITLE IN GAME 4",
            "keywords": "WNBA Finals, Game 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Round 2 at Port Royal: Blanchet holds lead after opening 9-under 62 with two eagles.",
            "liveNow": "Butterfield Bermuda Round 2: Chandler Blanchet leads after 62 (-9). Conners, Kohles, Walker at 63 (-7). Port Royal Golf Course, par 71.",
            "pulse": "PORT ROYAL ROUND 2: BLANCHET PACES FIELD",
            "keywords": "PGA Tour, Bermuda, Port Royal, Blanchet, Conners, Kohles, Round 2, Butterfield"
        },
        "home": {
            "tonight": "Friday desk",
            "tonightBlurb": "Thursday Night Football final: Bears edge Patriots 30-24 at Soldier Field. Tsitsipas and Bublik advance to Almaty semifinals. Dream chase WNBA title in Game 4.",
            "plTitle": "Premier League: Matchweek 8 kicks off tonight as Ipswich host Forest",
            "plBlurb": "Action starts at Portman Road before Saturday's London derby between Chelsea and Spurs. City lead table on 21 (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "Next race: United States GP in Austin",
            "f1Blurb": "Friday practice underway at COTA. Race Sunday 25 October at 15:00 local. Antonelli holds 102-point lead over teammate Russell."
        },
        "pg": {
            "pinFinal": "Almaty Friday: Tsitsipas d. Duckworth 6-3, 6-4. Bublik d. Khachanov 4-6, 7-6(5), 7-6(5). Medvedev d. Atmane 6-4, 6-4. Basilashvili d. Mannarino 6-3, 6-1.",
            "week1Closed": "NFL Week 7 TNF final: Bears edge Patriots 30-24 at Soldier Field",
            "week1Sub": "Williams 308 pass yds, 2 TD; Burden 130 rec yds, 1 TD; Santos 58-yd FG. Bears 5-2, Patriots 4-3. 49ers stand 6-0.",
            "countdownTnf": "TNF Final: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs and Vikings 5-0. Bills 5-1.",
            "barsPoints": "Bars show the gap to the leader. Antonelli has 340, 102 ahead of Russell on 238. Friday practice underway in Austin.",
            "tableAfterMonday": "Premier League: City lead table on 21 points (7-0-0). Arsenal 18, Brighton 16. MW8 opens tonight at Ipswich.",
            "pinClub": "Select a club. City are 7-0-0 on 21. Arsenal 18, Brighton 16. Spurs beat Coventry 3-1. MW8 opens Friday at Portman Road.",
            "plFootnote": "Matchweek 8 opens Friday: Ipswich v Forest; Saturday: Chelsea v Spurs, Villa v City. Monday final: Tottenham 3, Coventry 1.",
            "majorsDone": "Butterfield Bermuda Round 2 underway. Chandler Blanchet leads after opening 9-under 62 with two eagles. Conners, Kohles trail at 63.",
            "wnbaFirstRound": "WNBA Finals Game 4: Dream lead series 2-1 after 97-71 rout. Angel Reese historic 3rd double-double (21 pts, 12 reb). Game 4 in Atlanta.",
            "bracketFootnote": "Game 1: Valkyries 68, Dream 64. Game 2: Dream 79, Valkyries 65. Game 3: Dream 97, Valkyries 71. Dream lead series 2-1. Game 4 at State Farm Arena."
        }
    },
    "fr": {
        "football": {
            "tagline": "Final TNF : les Bears dominent les Patriots 30-24 a Soldier Field. Chicago passe a 5-2.",
            "liveNow": "Final TNF : Bears 30, Patriots 24. Williams 308 yds a la passe, 2 TD ; Santos FG de 58 yds. Bears 5-2, Patriots 4-3. 49ers 6-0.",
            "pulse": "FINAL TNF : BEARS 30, PATRIOTS 24",
            "keywords": "NFL semaine 7, Bears, Patriots, Caleb Williams, Drake Maye, Cairo Santos, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Almaty vendredi : Tsitsipas ecarte Duckworth en deux sets et file en demies.",
            "liveNow": "Almaty quarts : Tsitsipas bat Duckworth 6-3, 6-4. Bublik bat Khachanov 4-6, 7-6, 7-6. Medvedev bat Atmane 6-4, 6-4. Basilashvili bat Mannarino 6-3, 6-1.",
            "pulse": "ALMATY : TSITSIPAS ET BUBLIK EN DEMI-FINALES",
            "keywords": "ATP, Almaty, Tsitsipas, Duckworth, Bublik, Khachanov, Medvedev, Basilashvili"
        },
        "f1": {
            "tagline": "Essais du vendredi lances au COTA : Antonelli et Russell en piste a Austin.",
            "liveNow": "Austin vendredi : essais libres 1 et 2 au COTA. Course dimanche 25 octobre a 15:00 locale. Antonelli 340, Russell 238 (ecart 102). Mercedes 578.",
            "pulse": "ESSAIS D'AUSTIN EN COURS : ANTONELLI MENE DE 102 POINTS",
            "keywords": "Formule 1, GP des Etats-Unis, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "La 8e journee s'ouvre ce soir : Ipswich recoit Forest. City en tete avec 21 points.",
            "liveNow": "8e journee vendredi 20h00 UK : Ipswich - Forest a Portman Road. City 21 (7-0-0), Arsenal 18, Brighton 16. Chelsea - Spurs samedi.",
            "pulse": "PREMIER LEAGUE : 8E JOURNEE CE SOIR A IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Ipswich, Forest, 8e journee"
        },
        "basketball": {
            "tagline": "Finales WNBA match 4 : le Dream vise son premier titre en menant 2-1 a Atlanta.",
            "liveNow": "Match 4 a la State Farm Arena : Dream en tete 2-1 apres le succes 97-71. 3e double-double historique de Reese. Valkyries dos au mur.",
            "pulse": "FINALES WNBA : LE DREAM EN QUETE DU TITRE AU MATCH 4",
            "keywords": "WNBA Finales, match 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "2e tour a Port Royal : Blanchet en tete apres son 62 (-9) inaugural ponctue de deux eagles.",
            "liveNow": "Butterfield Bermuda 2e tour : Chandler Blanchet mene apres son 62 (-9). Conners, Kohles, Walker a 63 (-7). Port Royal Golf Course, par 71.",
            "pulse": "PORT ROYAL 2E TOUR : BLANCHET EN TETE DU CHAMP",
            "keywords": "PGA Tour, Bermudes, Port Royal, Blanchet, Conners, Kohles, 2e tour, Butterfield"
        },
        "home": {
            "tonight": "Bureau du vendredi",
            "tonightBlurb": "Final TNF : les Bears battent les Patriots 30-24 a Soldier Field. Tsitsipas et Bublik rejoignent le dernier carre a Almaty. Le Dream a une victoire du sacre WNBA.",
            "plTitle": "Premier League : la 8e journee debute ce soir avec Ipswich contre Forest",
            "plBlurb": "Coup d'envoi a Portman Road avant le derby londonien Chelsea - Spurs samedi. City domine le classement avec 21 points (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "Prochaine course : GP des Etats-Unis a Austin",
            "f1Blurb": "Essais du vendredi en cours au COTA. Course dimanche 25 octobre a 15:00 locale. Antonelli possede 102 points d'avance sur Russell."
        },
        "pg": {
            "pinFinal": "Almaty vendredi : Tsitsipas bat Duckworth 6-3, 6-4. Bublik bat Khachanov 4-6, 7-6(5), 7-6(5). Medvedev bat Atmane 6-4, 6-4. Basilashvili bat Mannarino 6-3, 6-1.",
            "week1Closed": "NFL semaine 7 TNF termine : les Bears dominent les Patriots 30-24 a Soldier Field",
            "week1Sub": "Williams 308 yds a la passe, 2 TD ; Burden 130 yds a la reception ; Santos FG de 58 yds. Bears 5-2, Patriots 4-3. 49ers a 6-0.",
            "countdownTnf": "Final TNF : Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs et Vikings 5-0. Bills 5-1.",
            "barsPoints": "Les barres indiquent l'ecart avec le leader. Antonelli compte 340, 102 points devant Russell a 238. Essais du vendredi en cours a Austin.",
            "tableAfterMonday": "Premier League : City mene avec 21 points (7-0-0). Arsenal 18, Brighton 16. La 8e journee debute ce soir a Ipswich.",
            "pinClub": "Selectionnez un club. City est a 7-0-0 avec 21 pts. Arsenal 18, Brighton 16. Les Spurs ont battu Coventry 3-1. 8e journee vendredi a Portman Road.",
            "plFootnote": "8e journee vendredi : Ipswich - Forest ; samedi : Chelsea - Spurs, Villa - City. Lundi final : Tottenham 3, Coventry 1.",
            "majorsDone": "Butterfield Bermuda 2e tour en cours. Chandler Blanchet mene apres son 62 (-9) avec deux eagles. Conners et Kohles a 63.",
            "wnbaFirstRound": "Finales WNBA match 4 : le Dream mene 2-1 apres son carton 97-71. 3e double-double record d'Angel Reese (21 pts, 12 reb). Match 4 a Atlanta.",
            "bracketFootnote": "Match 1 : Valkyries 68, Dream 64. Match 2 : Dream 79, Valkyries 65. Match 3 : Dream 97, Valkyries 71. Le Dream mene 2-1. Match 4 a la State Farm Arena."
        }
    },
    "es": {
        "football": {
            "tagline": "Final de TNF: los Bears superan 30-24 a los Patriots en Soldier Field. Chicago sube a 5-2.",
            "liveNow": "Final TNF: Bears 30, Patriots 24. Williams 308 yds pase, 2 TD; Santos gol de campo 58 yds. Bears 5-2, Patriots 4-3. 49ers 6-0.",
            "pulse": "FINAL TNF: BEARS 30, PATRIOTS 24",
            "keywords": "NFL Semana 7, Bears, Patriots, Caleb Williams, Drake Maye, Cairo Santos, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Almaty viernes: Tsitsipas vence a Duckworth en sets corridos y avanza a semifinales.",
            "liveNow": "Almaty cuartos: Tsitsipas a Duckworth 6-3, 6-4. Bublik a Khachanov 4-6, 7-6, 7-6. Medvedev a Atmane 6-4, 6-4. Basilashvili a Mannarino 6-3, 6-1.",
            "pulse": "ALMATY: TSITSIPAS Y BUBLIK CLASIFICAN A SEMIFINALES",
            "keywords": "ATP, Almaty, Tsitsipas, Duckworth, Bublik, Khachanov, Medvedev, Basilashvili"
        },
        "f1": {
            "tagline": "Practicas del viernes en marcha en COTA: Antonelli y Russell abren accion en Austin.",
            "liveNow": "Austin viernes: practicas 1 y 2 en COTA. Carrera domingo 25 octubre a las 15:00 local. Antonelli 340, Russell 238 (ventaja 102). Mercedes 578.",
            "pulse": "PRACTICAS DE AUSTIN EN MARCHA: ANTONELLI LIDERA POR 102",
            "keywords": "Formula 1, GP de Estados Unidos, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "La jornada 8 inicia esta noche con Ipswich vs Forest. City lidera la tabla con 21.",
            "liveNow": "Jornada 8 viernes 20:00 UK: Ipswich vs Forest en Portman Road. City 21 (7-0-0), Arsenal 18, Brighton 16. Chelsea vs Spurs sabado.",
            "pulse": "PREMIER LEAGUE: JORNADA 8 ARRANCA ESTA NOCHE EN IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Ipswich, Forest, Jornada 8"
        },
        "basketball": {
            "tagline": "Finales WNBA Juego 4: Dream busca su primera corona liderando 2-1 la serie en Atlanta.",
            "liveNow": "Juego 4 en State Farm Arena: Dream lidera 2-1 tras victoria 97-71. Historico 3er doble-doble de Reese. Valkyries al borde.",
            "pulse": "FINALES WNBA: DREAM BUSCA EL TITULO EN JUEGO 4",
            "keywords": "WNBA Finales, Juego 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Ronda 2 en Port Royal: Blanchet lidera tras abrir con un 62 (-9) con dos eagles.",
            "liveNow": "Butterfield Bermuda Ronda 2: Chandler Blanchet lidera tras 62 (-9). Conners, Kohles, Walker en 63 (-7). Port Royal Golf Course, par 71.",
            "pulse": "PORT ROYAL RONDA 2: BLANCHET LIDERA EL TABLERO",
            "keywords": "PGA Tour, Bermudas, Port Royal, Blanchet, Conners, Kohles, Ronda 2, Butterfield"
        },
        "home": {
            "tonight": "Mesa del viernes",
            "tonightBlurb": "Final TNF: Bears superan a Patriots 30-24 en Soldier Field. Tsitsipas y Bublik avanzan a semifinales en Almaty. Dream a un triunfo del titulo WNBA.",
            "plTitle": "Premier League: la jornada 8 comienza esta noche con Ipswich recibiendo a Forest",
            "plBlurb": "Accion en Portman Road antes del derby londinense Chelsea vs Spurs el sabado. City lidera con 21 puntos (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "Proxima carrera: GP de Estados Unidos en Austin",
            "f1Blurb": "Practicas de viernes en marcha en COTA. Carrera domingo 25 octubre a las 15:00 local. Antonelli aventaja a Russell por 102 puntos."
        },
        "pg": {
            "pinFinal": "Almaty viernes: Tsitsipas a Duckworth 6-3, 6-4. Bublik a Khachanov 4-6, 7-6(5), 7-6(5). Medvedev a Atmane 6-4, 6-4. Basilashvili a Mannarino 6-3, 6-1.",
            "week1Closed": "NFL Semana 7 final TNF: Bears superan 30-24 a los Patriots en Soldier Field",
            "week1Sub": "Williams 308 yds pase, 2 TD; Burden 130 yds recepcion; Santos FG de 58 yds. Bears 5-2, Patriots 4-3. 49ers estan 6-0.",
            "countdownTnf": "Final TNF: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs y Vikings 5-0. Bills 5-1.",
            "barsPoints": "Las barras muestran la ventaja con el lider. Antonelli suma 340, 102 mas que Russell con 238. Practicas de viernes en Austin.",
            "tableAfterMonday": "Premier League: City lidera con 21 puntos (7-0-0). Arsenal 18, Brighton 16. La jornada 8 arranca esta noche en Ipswich.",
            "pinClub": "Seleccione un club. City tiene 7-0-0 con 21 pts. Arsenal 18, Brighton 16. Spurs vencio a Coventry 3-1. Jornada 8 el viernes en Portman Road.",
            "plFootnote": "Jornada 8 viernes: Ipswich vs Forest; sabado: Chelsea vs Spurs, Villa vs City. Lunes final: Tottenham 3, Coventry 1.",
            "majorsDone": "Butterfield Bermuda Ronda 2 en marcha. Chandler Blanchet lidera tras abrir con 62 (-9) y dos eagles. Conners y Kohles en 63.",
            "wnbaFirstRound": "Finales WNBA Juego 4: Dream lidera 2-1 tras aplastar 97-71. Historico 3er doble-doble de Angel Reese (21 pts, 12 reb). Juego 4 en Atlanta.",
            "bracketFootnote": "Juego 1: Valkyries 68, Dream 64. Juego 2: Dream 79, Valkyries 65. Juego 3: Dream 97, Valkyries 71. Dream lidera 2-1. Juego 4 en State Farm Arena."
        }
    },
    "de": {
        "football": {
            "tagline": "TNF-Endstand: Bears bezwingen Patriots mit 30-24 im Soldier Field. Chicago klettert auf 5-2.",
            "liveNow": "TNF-Endstand: Bears 30, Patriots 24. Williams 308 Pass-Yards, 2 TD; Santos 58-Yard-FG. Bears 5-2, Patriots 4-3. 49ers 6-0.",
            "pulse": "TNF-ENDSTAND: BEARS 30, PATRIOTS 24",
            "keywords": "NFL Woche 7, Bears, Patriots, Caleb Williams, Drake Maye, Cairo Santos, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Almaty am Freitag: Tsitsipas schlaegt Duckworth glatt in zwei Saetzen und steht im Halbfinale.",
            "liveNow": "Almaty Viertelfinale: Tsitsipas d. Duckworth 6-3, 6-4. Bublik d. Khachanov 4-6, 7-6, 7-6. Medvedev d. Atmane 6-4, 6-4. Basilashvili d. Mannarino 6-3, 6-1.",
            "pulse": "ALMATY: TSITSIPAS UND BUBLIK ERREICHEN HALBFINALE",
            "keywords": "ATP, Almaty, Tsitsipas, Duckworth, Bublik, Khachanov, Medvedev, Basilashvili"
        },
        "f1": {
            "tagline": "Freitagstraining am COTA laeuft: Antonelli und Russell starten US-Grand-Prix-Wochenende.",
            "liveNow": "Austin Freitag: 1. und 2. Freies Training am COTA. Rennen Sonntag 25. Oktober um 15:00 Ortszeit. Antonelli 340, Russell 238 (Abstand 102). Mercedes 578.",
            "pulse": "AUSTIN TRAINING LAEUFT: ANTONELLI FUEHRT MIT 102 PUNKTEN",
            "keywords": "Formel 1, GP USA, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "Spieltag 8 eroeffnet heute: Ipswich empfaengt Forest. Man City fuehrt Tabelle mit 21 Punkten an.",
            "liveNow": "8. Spieltag Freitag 20:00 UK: Ipswich gegen Forest an der Portman Road. City 21 (7-0-0), Arsenal 18, Brighton 16. Chelsea gegen Spurs Samstag.",
            "pulse": "PREMIER LEAGUE: 8. SPIELTAG STARTET HEUTE IN IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Ipswich, Forest, 8. Spieltag"
        },
        "basketball": {
            "tagline": "WNBA-Finals Spiel 4: Dream greifen in Atlanta mit 2-1-Fuehrung nach erstem Franchise-Titel.",
            "liveNow": "Spiel 4 in der State Farm Arena: Dream fuehren 2-1 nach 97-71-Erfolg. Historisches 3. Final-Double-Double von Reese. Valkyries unter Druck.",
            "pulse": "WNBA-FINALS: DREAM WOLLEN TITEL IN SPIEL 4",
            "keywords": "WNBA Finals, Spiel 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Runde 2 in Port Royal: Blanchet fuehrt nach ueberragender 62 (-9) mit zwei Eagles.",
            "liveNow": "Butterfield Bermuda 2. Runde: Chandler Blanchet fuehrt nach 62 (-9). Conners, Kohles, Walker bei 63 (-7). Port Royal Golf Course, Par 71.",
            "pulse": "PORT ROYAL 2. RUNDE: BLANCHET FUEHRT DAS FELD AN",
            "keywords": "PGA Tour, Bermuda, Port Royal, Blanchet, Conners, Kohles, 2. Runde, Butterfield"
        },
        "home": {
            "tonight": "Freitags-Desk",
            "tonightBlurb": "TNF-Finale: Bears schlagen Patriots 30-24 im Soldier Field. Tsitsipas und Bublik stehen im Almaty-Halbfinale. Dream greifen nach WNBA-Krone.",
            "plTitle": "Premier League: 8. Spieltag beginnt heute mit Ipswich gegen Forest",
            "plBlurb": "Auftakt an der Portman Road vor dem Londoner Derby Chelsea gegen Spurs am Samstag. City fuehrt mit 21 Punkten (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "Naechstes Rennen: Großer Preis der USA in Austin",
            "f1Blurb": "Freitagstraining am COTA laeuft. Rennen Sonntag 25. Oktober um 15:00 Ortszeit. Antonelli hat 102 Punkte Vorsprung auf Russell."
        },
        "pg": {
            "pinFinal": "Almaty Freitag: Tsitsipas d. Duckworth 6-3, 6-4. Bublik d. Khachanov 4-6, 7-6(5), 7-6(5). Medvedev d. Atmane 6-4, 6-4. Basilashvili d. Mannarino 6-3, 6-1.",
            "week1Closed": "NFL Woche 7 TNF-Endstand: Bears schlagen Patriots 30-24 im Soldier Field",
            "week1Sub": "Williams 308 Pass-Yards, 2 TD; Burden 130 Rec-Yards; Santos 58-Yard-FG. Bears 5-2, Patriots 4-3. 49ers stehen 6-0.",
            "countdownTnf": "TNF-Endstand: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs und Vikings 5-0. Bills 5-1.",
            "barsPoints": "Balken zeigen Abstand zum Führenden. Antonelli hat 340, 102 vor Russell mit 238. Freitagstraining in Austin laeuft.",
            "tableAfterMonday": "Premier League: City fuehrt mit 21 Punkten (7-0-0). Arsenal 18, Brighton 16. 8. Spieltag startet heute in Ipswich.",
            "pinClub": "Klub waehlen. City hat 7-0-0 mit 21 Pkt. Arsenal 18, Brighton 16. Spurs schlugen Coventry 3-1. 8. Spieltag Freitag in Ipswich.",
            "plFootnote": "8. Spieltag Freitag: Ipswich - Forest; Samstag: Chelsea - Spurs, Villa - City. Montag final: Tottenham 3, Coventry 1.",
            "majorsDone": "Butterfield Bermuda Runde 2 laeuft. Chandler Blanchet fuehrt nach 62 (-9) mit zwei Eagles. Conners und Kohles bei 63.",
            "wnbaFirstRound": "WNBA Finals Spiel 4: Dream fuehren 2-1 nach 97-71-Erfolg. Angel Reese historisches 3. Double-Double (21 Pkt, 12 Reb). Spiel 4 in Atlanta.",
            "bracketFootnote": "Spiel 1: Valkyries 68, Dream 64. Spiel 2: Dream 79, Valkyries 65. Spiel 3: Dream 97, Valkyries 71. Dream fuehren 2-1. Spiel 4 in der State Farm Arena."
        }
    },
    "it": {
        "football": {
            "tagline": "Finale TNF: i Bears superano i Patriots 30-24 al Soldier Field. Chicago sale a 5-2.",
            "liveNow": "Finale TNF: Bears 30, Patriots 24. Williams 308 yds su lancio, 2 TD; Santos FG da 58 yds. Bears 5-2, Patriots 4-3. 49ers 6-0.",
            "pulse": "FINALE TNF: BEARS 30, PATRIOTS 24",
            "keywords": "NFL Week 7, Bears, Patriots, Caleb Williams, Drake Maye, Cairo Santos, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Almaty venerdi: Tsitsipas batte Duckworth in due set e vola in semifinale.",
            "liveNow": "Almaty quarti: Tsitsipas b. Duckworth 6-3, 6-4. Bublik b. Khachanov 4-6, 7-6, 7-6. Medvedev b. Atmane 6-4, 6-4. Basilashvili b. Mannarino 6-3, 6-1.",
            "pulse": "ALMATY: TSITSIPAS E BUBLIK IN SEMIFINALE",
            "keywords": "ATP, Almaty, Tsitsipas, Duckworth, Bublik, Khachanov, Medvedev, Basilashvili"
        },
        "f1": {
            "tagline": "Prove del venerdi al via al COTA: Antonelli e Russell aprono il weekend di Austin.",
            "liveNow": "Austin venerdi: prove libere 1 e 2 al COTA. Gara domenica 25 ottobre alle 15:00 locali. Antonelli 340, Russell 238 (gap 102). Mercedes 578.",
            "pulse": "PROVE DI AUSTIN AL VIA: ANTONELLI GUIDA CON +102 PUNTI",
            "keywords": "Formula 1, GP Stati Uniti, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "L'8a giornata si apre stasera: l'Ipswich ospita il Forest. City in vetta a quota 21.",
            "liveNow": "8a giornata venerdi 20:00 UK: Ipswich v Forest a Portman Road. City 21 (7-0-0), Arsenal 18, Brighton 16. Chelsea v Spurs sabato.",
            "pulse": "PREMIER LEAGUE: L'8A GIORNATA COMINCIA STASERA A IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Ipswich, Forest, 8a giornata"
        },
        "basketball": {
            "tagline": "Finals WNBA Gara 4: il Dream insegue il primo titolo con la serie sul 2-1 ad Atlanta.",
            "liveNow": "Gara 4 alla State Farm Arena: Dream avanti 2-1 dopo il 97-71. Terza doppia doppia storica di Reese. Valkyries spalle al muro.",
            "pulse": "FINALS WNBA: IL DREAM PUNTA AL TITOLO IN GARA 4",
            "keywords": "WNBA Finals, Gara 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Secondo giro a Port Royal: Blanchet al comando dopo il 62 (-9) inaugurale con due eagle.",
            "liveNow": "Butterfield Bermuda 2° giro: Chandler Blanchet guida dopo il 62 (-9). Conners, Kohles, Walker a 63 (-7). Port Royal Golf Course, par 71.",
            "pulse": "PORT ROYAL 2° GIRO: BLANCHET GUIDA LA CLASSIFICA",
            "keywords": "PGA Tour, Bermuda, Port Royal, Blanchet, Conners, Kohles, 2° giro, Butterfield"
        },
        "home": {
            "tonight": "Desk di venerdi",
            "tonightBlurb": "Finale TNF: i Bears battono i Patriots 30-24 al Soldier Field. Tsitsipas e Bublik in semifinale ad Almaty. Dream a una vittoria dal titolo WNBA.",
            "plTitle": "Premier League: l'8a giornata scatta stasera con Ipswich contro Forest",
            "plBlurb": "Si gioca a Portman Road prima del derby londinese Chelsea contro Spurs di sabato. City primo a quota 21 (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "Prossima gara: GP degli Stati Uniti ad Austin",
            "f1Blurb": "Prove libere del venerdi in corso al COTA. Gara domenica 25 ottobre alle 15:00 locali. Antonelli ha 102 punti di vantaggio su Russell."
        },
        "pg": {
            "pinFinal": "Almaty venerdi: Tsitsipas b. Duckworth 6-3, 6-4. Bublik b. Khachanov 4-6, 7-6(5), 7-6(5). Medvedev b. Atmane 6-4, 6-4. Basilashvili b. Mannarino 6-3, 6-1.",
            "week1Closed": "NFL Week 7 finale TNF: i Bears piegano i Patriots 30-24 al Soldier Field",
            "week1Sub": "Williams 308 yds lancio, 2 TD; Burden 130 yds ricezione; Santos FG da 58 yds. Bears 5-2, Patriots 4-3. 49ers imbattuti a 6-0.",
            "countdownTnf": "Finale TNF: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs e Vikings 5-0. Bills 5-1.",
            "barsPoints": "Le barre indicano il distacco dal leader. Antonelli ha 340 punti, 102 su Russell (238). Prove del venerdi in corso ad Austin.",
            "tableAfterMonday": "Premier League: City in vetta a 21 punti (7-0-0). Arsenal 18, Brighton 16. L'8a giornata si apre stasera a Ipswich.",
            "pinClub": "Seleziona un club. City a 7-0-0 con 21 punti. Arsenal 18, Brighton 16. Gli Spurs hanno battuto il Coventry 3-1. 8a giornata venerdi a Portman Road.",
            "plFootnote": "8a giornata venerdi: Ipswich v Forest; sabato: Chelsea v Spurs, Villa v City. Lunedi finale: Tottenham 3, Coventry 1.",
            "majorsDone": "Butterfield Bermuda 2° giro in corso. Chandler Blanchet in testa dopo il 62 (-9) con due eagle. Conners e Kohles a quota 63.",
            "wnbaFirstRound": "Finals WNBA Gara 4: Dream avanti 2-1 dopo il travolgente 97-71. 3a doppia doppia record di Angel Reese (21 pts, 12 reb). Gara 4 ad Atlanta.",
            "bracketFootnote": "Gara 1: Valkyries 68, Dream 64. Gara 2: Dream 79, Valkyries 65. Gara 3: Dream 97, Valkyries 71. Dream avanti 2-1. Gara 4 alla State Farm Arena."
        }
    },
    "pl": {
        "football": {
            "tagline": "Koniec meczu TNF: Bears pokonali Patriots 30-24 na Soldier Field. Chicago poprawia bilans na 5-2.",
            "liveNow": "Koniec TNF: Bears 30, Patriots 24. Williams 308 jardow gora, 2 TD; Santos 58-jardowy FG. Bears 5-2, Patriots 4-3. 49ers 6-0.",
            "pulse": "KONIEC TNF: BEARS 30, PATRIOTS 24",
            "keywords": "NFL Tydzien 7, Bears, Patriots, Caleb Williams, Drake Maye, Cairo Santos, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Almaty w piatek: Tsitsipas pewnie pokonuje Duckwortha w dwoch setach i wchodzi do polfinalu.",
            "liveNow": "Almaty cwiercfinaly: Tsitsipas d. Duckworth 6-3, 6-4. Bublik d. Khachanov 4-6, 7-6, 7-6. Medvedev d. Atmane 6-4, 6-4. Basilashvili d. Mannarino 6-3, 6-1.",
            "pulse": "ALMATY: TSITSIPAS I BUBLIK W POLFINALE",
            "keywords": "ATP, Almaty, Tsitsipas, Duckworth, Bublik, Khachanov, Medvedev, Basilashvili"
        },
        "f1": {
            "tagline": "Piatkowe treningi na COTA rozpoczeta: Antonelli i Russell otwieraja weekend w Austin.",
            "liveNow": "Austin piatek: 1. i 2. trening na COTA. Wyscig w niedziele 25 pazdziernika o 15:00 czasu lokalnego. Antonelli 340, Russell 238 (102 pkt straty). Mercedes 578.",
            "pulse": "TRENINGI W AUSTIN ROZPOCZETE: ANTONELLI PROWADZI O 102 PKT",
            "keywords": "Formula 1, GP USA, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "8. kolejka rusza dzis wieczorem: Ipswich podejmuje Forest. City prowadzi w tabeli z 21 punktami.",
            "liveNow": "8. kolejka piatek 20:00 UK: Ipswich v Forest na Portman Road. City 21 (7-0-0), Arsenal 18, Brighton 16. Chelsea v Spurs w sobote.",
            "pulse": "PREMIER LEAGUE: 8. KOLEJKA STARTUJE DZIS W IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Ipswich, Forest, 8. kolejka"
        },
        "basketball": {
            "tagline": "Finaly WNBA mecz 4: Dream stoja przed szansa na tytul, prowadzac w serii 2-1 w Atlancie.",
            "liveNow": "Mecz 4 w State Farm Arena: Dream prowadza 2-1 po wygranej 97-71. Historyczne 3. double-double Reese. Valkyries graja o przetrwanie.",
            "pulse": "FINALY WNBA: DREAM GRAJA O MISTRZOSTWO W MECZU 4",
            "keywords": "WNBA Finaly, mecz 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "2. runda w Port Royal: Blanchet na czele po wysmienitym 62 (-9) z dwoma eagle'ami.",
            "liveNow": "Butterfield Bermuda 2. runda: Chandler Blanchet prowadzi po 62 (-9). Conners, Kohles, Walker na 63 (-7). Port Royal Golf Course, par 71.",
            "pulse": "PORT ROYAL 2. RUNDA: BLANCHET LIDEREM TURNIEJU",
            "keywords": "PGA Tour, Bermudy, Port Royal, Blanchet, Conners, Kohles, 2. runda, Butterfield"
        },
        "home": {
            "tonight": "Pulpit piatkowy",
            "tonightBlurb": "Final TNF: Bears wygrali z Patriots 30-24 na Soldier Field. Tsitsipas i Bublik w polfinale w Almatach. Dream o krok od tytulu WNBA.",
            "plTitle": "Premier League: 8. kolejka rozpoczyna sie dzis wieczorem meczem Ipswich z Forest",
            "plBlurb": "Poczatek na Portman Road przed sobotnimi derbami Londynu pomiedzy Chelsea a Spurs. City liderem z 21 punktami (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "Nastepny wyscig: GP Stanow Zjednoczonych w Austin",
            "f1Blurb": "Piatkowe treningi na COTA w toku. Wyscig w niedziele 25 pazdziernika o 15:00 czasu lokalnego. Antonelli ma 102 punkty przewagi nad Russellem."
        },
        "pg": {
            "pinFinal": "Almaty piatek: Tsitsipas d. Duckworth 6-3, 6-4. Bublik d. Khachanov 4-6, 7-6(5), 7-6(5). Medvedev d. Atmane 6-4, 6-4. Basilashvili d. Mannarino 6-3, 6-1.",
            "week1Closed": "NFL Tydzien 7 koniec TNF: Bears pokonali Patriots 30-24 na Soldier Field",
            "week1Sub": "Williams 308 jardow gora, 2 TD; Burden 130 jardow odbioru; Santos 58-jardowy FG. Bears 5-2, Patriots 4-3. 49ers na 6-0.",
            "countdownTnf": "Koniec TNF: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs i Vikings 5-0. Bills 5-1.",
            "barsPoints": "Paski pokazuja strate do lidera. Antonelli ma 340, 102 przed Russellem (238). Piatkowe treningi w Austin w toku.",
            "tableAfterMonday": "Premier League: City prowadzi z 21 punktami (7-0-0). Arsenal 18, Brighton 16. 8. kolejka rusza dzis w Ipswich.",
            "pinClub": "Wybierz klub. City ma 7-0-0 i 21 pkt. Arsenal 18, Brighton 16. Spurs pokonali Coventry 3-1. 8. kolejka w piatek na Portman Road.",
            "plFootnote": "8. kolejka piatek: Ipswich v Forest; sobota: Chelsea v Spurs, Villa v City. Poniedzialek final: Tottenham 3, Coventry 1.",
            "majorsDone": "Butterfield Bermuda 2. runda w toku. Chandler Blanchet prowadzi po otwarciu 62 (-9) z dwoma eagle'ami. Conners i Kohles maja 63.",
            "wnbaFirstRound": "Finaly WNBA mecz 4: Dream prowadza 2-1 po pogromie 97-71. 3. rekordowe double-double Angel Reese (21 pkt, 12 zb). Mecz 4 w Atlancie.",
            "bracketFootnote": "Mecz 1: Valkyries 68, Dream 64. Mecz 2: Dream 79, Valkyries 65. Mecz 3: Dream 97, Valkyries 71. Dream prowadza 2-1. Mecz 4 w State Farm Arena."
        }
    },
    "zh": {
        "football": {
            "tagline": "周四夜赛战报：熊队在军人球场30-24险胜爱国者，战绩提升至5胜2负。",
            "liveNow": "TNF完赛：熊队 30，爱国者 24。威廉姆斯传球308码2达阵；桑托斯命中58码任意球。熊队5-2，爱国者4-3。49人6-0。",
            "pulse": "TNF战报：熊队 30，爱国者 24",
            "keywords": "NFL第7周, 熊队, 爱国者, 凯莱布·威廉姆斯, 梅耶, 桑托斯, 军人球场, TNF"
        },
        "tennis": {
            "tagline": "阿拉木图周五：西西帕斯直落两盘击败达克沃斯，强势晋级半决赛。",
            "liveNow": "阿拉木图八强战：西西帕斯 6-3、6-4 达克沃斯；布勃利克 4-6、7-6、7-6 哈恰诺夫；梅德韦杰夫 6-4、6-4 阿特马纳；巴西拉什维利 6-3、6-1 马纳里诺。",
            "pulse": "阿拉木图：西西帕斯与布勃利克会师半决赛",
            "keywords": "ATP, 阿拉木图, 西西帕斯, 达克沃斯, 布勃利克, 哈恰诺夫, 梅德韦杰夫, 巴西拉什维利"
        },
        "f1": {
            "tagline": "美洲赛道周五练习赛开打：安东内利与拉塞尔开启美国站征程。",
            "liveNow": "奥斯汀周五：美洲赛道一练和二练进行中。正赛周日10月25日当地时间15:00开跑。安东内利340分，拉塞尔238分（分差102）。梅赛德斯578分。",
            "pulse": "奥斯汀练习赛打响：安东内利领先102分",
            "keywords": "一级方程式, 美国大奖赛, 奥斯汀, COTA, 安东内利, 拉塞尔, 梅赛德斯, 法拉利"
        },
        "soccer": {
            "tagline": "英超第8轮今晚打响：伊普斯维奇迎战森林。曼城21分强势领跑积分榜。",
            "liveNow": "第8轮周五英国时间20:00：伊普斯维奇在波特曼路球场迎战森林。曼城21分（7胜0平0负），阿森纳18分，布莱顿16分。切尔西对热刺周六开战。",
            "pulse": "英超联赛：第8轮今晚在伊普斯维奇揭幕",
            "keywords": "英超, 曼城, 阿森纳, 热刺, 切尔西, 伊普斯维奇, 森林, 第8轮"
        },
        "basketball": {
            "tagline": "WNBA总决赛第4战：梦想大比分2-1领先，在亚特兰大冲击队史首座总冠军奖杯。",
            "liveNow": "州立农业球馆第4战：梦想97-71大胜后2-1领先。里斯创纪录连续三场总决赛两双。女武神面临生死战。",
            "pulse": "WNBA总决赛：梦想第4战全力冲冠",
            "keywords": "WNBA总决赛, 第4战, 梦想, 女武神, 里斯, 霍华德, 州立农业球馆, 2-1"
        },
        "golf": {
            "tagline": "皇家港次轮较量：布兰切特首轮狂轰62杆（-9）射下双鹰，牢牢占据榜首。",
            "liveNow": "百慕大锦标赛次轮：钱德勒·布兰切特以62杆（-9）领跑。康纳斯、科尔斯以63杆（-7）紧追。皇家港高尔夫球场，标准杆71杆。",
            "pulse": "皇家港次轮打响：布兰切特全场领跑",
            "keywords": "美巡赛, 百慕大, 皇家港, 布兰切特, 康纳斯, 科尔斯, 次轮, 百慕大锦标赛"
        },
        "home": {
            "tonight": "周五快讯",
            "tonightBlurb": "周四夜赛完结：熊队在军人球场30-24力克爱国者。西西帕斯与布勃利克挺进阿拉木图半决赛。梦想距WNBA总冠军仅差一胜。",
            "plTitle": "英超联赛：第8轮今晚拉开帷幕，伊普斯维奇主场迎战森林",
            "plBlurb": "比赛在波特曼路球场打响，周六迎来切尔西对热刺的伦敦德比。曼城积21分（7战全胜）傲视群雄，阿森纳18分，布莱顿16分。",
            "f1Title": "下一站：奥斯汀美国大奖赛",
            "f1Blurb": "美洲赛道周五自由练习赛展开。正赛于10月25日周日当地时间15:00打响。安东内利在车手积分榜上领先拉塞尔102分。"
        },
        "pg": {
            "pinFinal": "阿拉木图周五：西西帕斯 6-3、6-4 达克沃斯；布勃利克 4-6、7-6(5)、7-6(5) 哈恰诺夫；梅德韦杰夫 6-4、6-4 阿特马纳；巴西拉什维利 6-3、6-1 马纳里诺。",
            "week1Closed": "NFL第7周TNF完赛：熊队在军人球场30-24战胜爱国者",
            "week1Sub": "威廉姆斯传球308码2达阵；伯登接球130码；桑托斯命中58码任意球。熊队5-2，爱国者4-3。49人保持6-0完好战绩。",
            "countdownTnf": "TNF完赛：熊队 30，爱国者 24。熊队5-2。49人6-0。酋长与维京人5-0。比尔5-1。",
            "barsPoints": "柱状图显示与领跑者的分差。安东内利积340分，领先拉塞尔（238分）达102分。奥斯汀周五练习赛进行中。",
            "tableAfterMonday": "英超联赛：曼城积21分（7战全胜）高居榜首。阿森纳18分，布莱顿16分。第8轮今晚在伊普斯维奇揭幕。",
            "pinClub": "选择俱乐部。曼城7战全胜积21分。阿森纳18分，布莱顿16分。热刺3-1击败考文垂。第8轮周五在波特曼路展开。",
            "plFootnote": "第8轮周五：伊普斯维奇对森林；周六：切尔西对热刺，维拉对曼城。周一完赛：热刺 3，考文垂 1。",
            "majorsDone": "百慕大锦标赛次轮进行中。布兰切特首轮射下双鹰交出62杆（-9）领跑。康纳斯与科尔斯以63杆紧咬。",
            "wnbaFirstRound": "WNBA总决赛第4战：梦想97-71大胜后大比分2-1领先。安吉尔·里斯创纪录连续三场总决赛砍下两双（21分12板）。第4战亚特兰大打响。",
            "bracketFootnote": "第1战：女武神 68，梦想 64。第2战：梦想 79，女武神 65。第3战：梦想 97，女武神 71。梦想大比分2-1领先。第4战在州立农业球馆举行。"
        }
    },
    "ja": {
        "football": {
            "tagline": "TNF試合結果：ベアーズがソルジャー・フィールドでペイトリオッツを30-24で下し5勝2敗に。",
            "liveNow": "TNF終了：ベアーズ 30、ペイトリオッツ 24。ウィリアムズ308パスヤード・2TD、サントス58ydのFG。ベアーズ5-2、ペイトリオッツ4-3。49ersは6-0。",
            "pulse": "TNF終了：ベアーズ 30、ペイトリオッツ 24",
            "keywords": "NFL第7週, ベアーズ, ペイトリオッツ, ケイレブ・ウィリアムズ, メイエ, サントス, ソルジャー・フィールド, TNF"
        },
        "tennis": {
            "tagline": "アルマティ金曜：チチパスがダックワースをストレートで破り準決勝へ進出。",
            "liveNow": "アルマティ準々決勝：チチパス 6-3, 6-4 ダックワース。ブブリク 4-6, 7-6, 7-6 ハチャノフ。メドベージェフ 6-4, 6-4 アトマネ。バシラシビリ 6-3, 6-1 マナリノ。",
            "pulse": "アルマティ：チチパスとブブリクが準決勝進出",
            "keywords": "ATP, アルマティ, チチパス, ダックワース, ブブリク, ハチャノフ, メドベージェフ, バシラシビリ"
        },
        "f1": {
            "tagline": "COTAで金曜フリー走行開始：アントネッリとラッセルがアメリカGP週末を始動。",
            "liveNow": "オースティン金曜：COTAでFP1とFP2実施中。決勝は10月25日日曜現地15:00。アントネッリ340点、ラッセル238点（差102点）。メルセデス578点。",
            "pulse": "オースティン練習走行開始：アントネッリが102点リード",
            "keywords": "F1, アメリカGP, オースティン, COTA, アントネッリ, ラッセル, メルセデス, フェラーリ"
        },
        "soccer": {
            "tagline": "第8節が今夜開幕：イプスウィッチがフォレストを迎撃。マンチェスター・Cが勝点21で首位。",
            "liveNow": "第8節金曜20:00英国時間：ポートマン・ロードでイプスウィッチ対フォレスト。首位シティ21点（7勝0敗）、アーセナル18点、ブライトン16点。土曜にチェルシー対スパーズ。",
            "pulse": "プレミアリーグ：第8節が今夜イプスウィッチで開幕",
            "keywords": "プレミアリーグ, シティ, アーセナル, スパーズ, チェルシー, イプスウィッチ, フォレスト, 第8節"
        },
        "basketball": {
            "tagline": "WNBAファイナル第4戦：ドリームが2勝1敗で球団史上初優勝を目指しアトランタで激突。",
            "liveNow": "ステートファーム・アリーナで第4戦：ドリームが97-71圧勝で王手。リーズが3試合連続ダブルダブルの歴史的快挙。ヴァルキリーズは背水の陣。",
            "pulse": "WNBAファイナル：ドリームが第4戦で王座へ挑む",
            "keywords": "WNBAファイナル, 第4戦, ドリーム, ヴァルキリーズ, リーズ, ハワード, ステートファーム・アリーナ, 2-1"
        },
        "golf": {
            "tagline": "ポートロイヤル第2ラウンド：ブランシェットが初日2イーグル・62（-9）で単独首位キープ。",
            "liveNow": "バミューダ選手権第2R：チャンドラー・ブランシェットが62（-9）で首位。コナーズ、コールズらが63（-7）で追走。ポートロイヤル・ゴルフコース（パー71）。",
            "pulse": "ポートロイヤル第2R：ブランシェットが首位独走",
            "keywords": "PGAツアー, バミューダ, ポートロイヤル, ブランシェット, コナーズ, コールズ, 第2R, バミューダ選手権"
        },
        "home": {
            "tonight": "金曜デスク",
            "tonightBlurb": "TNF終了：ベアーズが30-24でペイトリオッツに競り勝つ。チチパスとブブリクがアルマティ準決勝へ。ドリームがWNBA初優勝に王手。",
            "plTitle": "プレミアリーグ：第8節が今夜イプスウィッチ対フォレストでキックオフ",
            "plBlurb": "ポートマン・ロードでの一戦から開幕し土曜にはチェルシー対スパーズのロンドンダービー。シティが7戦全勝21点で首位、アーセナル18点、ブライトン16点。",
            "f1Title": "次戦：オースティンのアメリカGP",
            "f1Blurb": "COTAで金曜フリー走行が進行中。決勝は10月25日日曜現地15:00。アントネッリがラッセルに102点リード。"
        },
        "pg": {
            "pinFinal": "アルマティ金曜：チチパス 6-3, 6-4 ダックワース。ブブリク 4-6, 7-6(5), 7-6(5) ハチャノフ。メドベージェフ 6-4, 6-4 アトマネ。バシラシビリ 6-3, 6-1 マナリノ。",
            "week1Closed": "NFL第7週TNF終了：ベアーズがソルジャー・フィールドでペイトリオッツを30-24で撃破",
            "week1Sub": "ウィリアムズ308ydパス・2TD、バーデン130ydレシーブ、サントス58ydのFG。ベアーズ5-2、ペイトリオッツ4-3。49ersは6勝0敗を維持。",
            "countdownTnf": "TNF終了：ベアーズ 30、ペイトリオッツ 24。ベアーズ5-2。49ers 6-0。チーフスとバイキングス5-0。ビルズ5-1。",
            "barsPoints": "バーは首位との差を示します。アントネッリが340点で首位、ラッセル（238点）に102点差。オースティンで金曜走行中。",
            "tableAfterMonday": "プレミアリーグ：シティが7戦全勝の21点で首位。アーセナル18点、ブライトン16点。第8節が今夜イプスウィッチで開幕。",
            "pinClub": "クラブを選択。シティは7戦全勝21点。アーセナル18点、ブライトン16点。スパーズはコベントリーに3-1で勝利。第8節金曜にポートマン・ロードで開催。",
            "plFootnote": "第8節金曜：イプスウィッチ対フォレスト。土曜：チェルシー対スパーズ、ヴィラ対シティ。月曜終了：トッテナム 3、コベントリー 1。",
            "majorsDone": "バミューダ選手権第2Rが進行中。ブランシェットが初日2イーグルの62（-9）でリード。コナーズ、コールズが63で追う。",
            "wnbaFirstRound": "WNBAファイナル第4戦：ドリームが97-71の大勝で2勝1敗。エンジェル・リーズが3戦連続ダブルダブル（21点12R）の快挙。第4戦アトランタ。",
            "bracketFootnote": "第1戦：ヴァルキリーズ 68、ドリーム 64。第2戦：ドリーム 79、ヴァルキリーズ 65。第3戦：ドリーム 97、ヴァルキリーズ 71。ドリームが2勝1敗で王手。第4戦はステートファーム・アリーナ。"
        }
    },
    "ko": {
        "football": {
            "tagline": "TNF 경기 결과: 베어스가 솔저 필드에서 패트리어츠를 30-24로 꺾고 5승 2패 기록.",
            "liveNow": "TNF 종료: 베어스 30, 패트리어츠 24. 윌리엄스 패스 308야드 2TD, 산토스 58야드 FG. 베어스 5-2, 패트리어츠 4-3. 49ers 6-0 유지.",
            "pulse": "TNF 종료: 베어스 30, 패트리어츠 24",
            "keywords": "NFL 7주차, 베어스, 패트리어츠, 케イレ브 윌리엄스, 메이예, 산토스, 솔저 필드, TNF"
        },
        "tennis": {
            "tagline": "알마티 금요일: 치치파스가 더크워스를 무실세트로 제압하고 4강에 안착.",
            "liveNow": "알마티 8강전: 치치파스 6-3, 6-4 더크워스. 부블리크 4-6, 7-6, 7-6 하차노프. 메드베데프 6-4, 6-4 아트만. 바실라시빌리 6-3, 6-1 마나리노.",
            "pulse": "알마티: 치치파스와 부블리크 4강 진출",
            "keywords": "ATP, 알마티, 치치파스, 더크워스, 부블리크, 하차노프, 메드베데프, 바실라시빌리"
        },
        "f1": {
            "tagline": "COTA 금요 연습 주행 시작: 안토넬리와 러셀이 미국 GP 일정에 돌입.",
            "liveNow": "오스틴 금요일: COTA에서 연습 주행 1, 2세션 진행 중. 결승 일요일 10월 25일 현지 15:00. 안토넬리 340점, 러셀 238점 (102점 차). 메르세데스 578점.",
            "pulse": "오스틴 연습 주행 돌입: 안토넬리 102점 차 리드",
            "keywords": "F1, 미국 GP, 오스틴, COTA, 안토넬리, 러셀, 메르세데스, 페라리"
        },
        "soccer": {
            "tagline": "8라운드 오늘 밤 개막: 입스위치가 포레스트와 격돌. 맨시티 승점 21점으로 선두 순항.",
            "liveNow": "8라운드 금요일 20:00 UK: 포트먼 로드에서 입스위치 대 포레스트. 맨시티 21점 (7전 전승), 아스널 18점, 브라이턴 16점. 토요일 첼시 대 토트넘.",
            "pulse": "프리미어리그: 8라운드 오늘 밤 입스위치에서 개막",
            "keywords": "프리미어리그, 맨시티, 아스널, 토트넘, 첼시, 입스위치, 포레스트, 8라운드"
        },
        "basketball": {
            "tagline": "WNBA 파이널 4차전: 드림이 시리즈 2-1로 앞서며 아틀란타에서 창단 첫 우승 정조준.",
            "liveNow": "스테이트 팜 아레나 4차전: 드림 97-71 대승으로 2-1 리드. 리스 역사상 최초 3경기 연속 파이널 더블더블. 발키리스 벼랑 끝.",
            "pulse": "WNBA 파이널: 드림, 4차전에서 우승 확정 도전",
            "keywords": "WNBA 파이널, 4차전, 드림, 발키리스, 리스, 하워드, 스테이트 팜 아레나, 2-1"
        },
        "golf": {
            "tagline": "포트 로열 2라운드: 블랑셰가 1라운드 이글 2방 포함 62타(-9)로 단독 선두 질주.",
            "liveNow": "버뮤다 챔피언십 2라운드: 챈들러 블랑셰 62타(-9)로 선두. 코너스, 콜스 등 63타(-7)로 추격 중. 포트 로열 골프 코스, 파 71.",
            "pulse": "포트 로열 2R: 블랑셰 단독 선두 질주",
            "keywords": "PGA 투어, 버뮤다, 포트 로열, 블랑셰, 코너스, 콜스, 2라운드, 버뮤다 챔피언십"
        },
        "home": {
            "tonight": "금요일 데스크",
            "tonightBlurb": "TNF 종료: 베어스가 솔저 필드에서 패트리어츠에 30-24 승리. 치치파스와 부블리크 알마티 4강 진출. 드림, WNBA 우승까지 1승 남김.",
            "plTitle": "프리미어리그: 8라운드가 오늘 밤 입스위치 대 포레스트로 킥오프",
            "plBlurb": "포트먼 로드 경기 이후 토요일 첼시 대 토트넘 런던 더비 예정. 맨시티 7전 전승 승점 21점으로 선두, 아스널 18점, 브라이턴 16점.",
            "f1Title": "다음 경기: 오스틴 미국 그랑프리",
            "f1Blurb": "COTA 금요 연습 주행 진행 중. 결승 10월 25일 일요일 현지 15:00. 안토넬리가 팀 동료 러셀에 102점 차 앞섬."
        },
        "pg": {
            "pinFinal": "알마티 금요일: 치치파스 6-3, 6-4 더크워스. 부블리크 4-6, 7-6(5), 7-6(5) 하차노프. 메드베데프 6-4, 6-4 아트만. 바실라시빌리 6-3, 6-1 마나리노.",
            "week1Closed": "NFL 7주차 TNF 종료: 베어스가 솔저 필드에서 패트리어츠를 30-24로 제압",
            "week1Sub": "윌리엄스 패스 308야드 2TD, 버든 130야드 리시빙, 산토스 58야드 FG. 베어스 5-2, 패트리어츠 4-3. 49ers 6승 무패.",
            "countdownTnf": "TNF 종료: 베어스 30, 패트리어츠 24. 베어스 5-2. 49ers 6-0. 치프스와 바이킹스 5-0. 빌스 5-1.",
            "barsPoints": "막대는 선두와의 격차를 보여줍니다. 안토넬리 340점, 러셀(238점)에 102점 차 선두. 오스틴 금요 연습 주행 중.",
            "tableAfterMonday": "프리미어리그: 맨시티 7전 전승 승점 21점으로 선두. 아스널 18점, 브라이턴 16점. 8라운드 오늘 밤 입스위치에서 개막.",
            "pinClub": "클럽을 선택하세요. 맨시티 7전 전승 21점. 아스널 18점, 브라이턴 16점. 스퍼스는 코번트리를 3-1로 격파. 8라운드 금요일 포트먼 로드.",
            "plFootnote": "8라운드 금요일: 입스위치 v 포레스트. 토요일: 첼시 v 스퍼스, 빌라 v 시티. 월요일 종료: 토트넘 3, 코번트리 1.",
            "majorsDone": "버뮤다 챔피언십 2라운드 진행 중. 챈들러 블랑셰가 1R 이글 2개와 62타(-9)로 선두. 코너스와 콜스가 63타로 추격.",
            "wnbaFirstRound": "WNBA 파이널 4차전: 드림 97-71 대승으로 2-1 리드. 앤젤 리스 역사상 최초 3경기 연속 더블더블 (21점 12리바운드). 4차전 아틀란타.",
            "bracketFootnote": "1차전: 발키리스 68, 드림 64. 2차전: 드림 79, Valkyries 65. 3차전: 드림 97, 발키리스 71. 드림이 2-1 리드. 4차전은 스테이트 팜 아레나."
        }
    },
    "ar": {
        "football": {
            "tagline": "نهائي الخميس الكروي: البيرز يهزمون الباتريوتس 30-24 في سولجر فيلد. شيكاغو تصعد الى 5-2.",
            "liveNow": "نهائي TNF: بيرز 30، باتريوتس 24. ويليامز 308 ياردة تمرير و2 هبوط؛ سانتوس هدف ميداني من 58 ياردة. بيرز 5-2، باتريوتس 4-3. 49ers في الصدارة بـ6-0.",
            "pulse": "نهائي TNF: بيرز 30، باتريوتس 24",
            "keywords": "NFL الاسبوع 7, بيرز, باتريوتس, ويليامز, ماي, سانتوس, سولجر فيلد, TNF"
        },
        "tennis": {
            "tagline": "الماتي الجمعة: تسيتسيباس يتخطى داكوورث بمجموعتين نظيفتين ويبلغ نصف النهائي.",
            "liveNow": "الماتي ربع النهائي: تسيتسيباس يهزم داكوورث 6-3 و6-4. بوبليك يهزم خاتشانوف 4-6 و7-6 و7-6. ميدفيديف يهزم اتمان 6-4 و6-4. باسيلاشفيلي يهزم مانارينو 6-3 و6-1.",
            "pulse": "الماتي: تسيتسيباس وبوبليك يبلغان نصف النهائي",
            "keywords": "ATP, الماتي, تسيتسيباس, داكوورث, بوبليك, خاتشانوف, ميدفيديف, باسيلاشفيلي"
        },
        "f1": {
            "tagline": "تجارب الجمعة تنطلق في حلبة الامريكتين: انتونيللي وراسل يفتتحان عطلة اسبوع اوستن.",
            "liveNow": "اوستن الجمعة: التجارب الحرة 1 و2 في COTA. السباق الاحد 25 اكتوبر الساعة 15:00 محليا. انتونيللي 340، راسل 238 (الفارق 102). مرسيدس 578.",
            "pulse": "تجارب اوستن تبدا: انتونيللي يتصدر بفارق 102 نقطة",
            "keywords": "فورمولا 1, جائزة امريكا الكبرى, اوستن, COTA, انتونيللي, راسل, مرسيدس, فيراري"
        },
        "soccer": {
            "tagline": "الجولة 8 تنطلق الليلة: ايبسويتش يستضيف فورست. سيتي يتصدر الترتيب بـ21 نقطة.",
            "liveNow": "الجولة 8 الجمعة 20:00 بتوقيت بريطانيا: ايبسويتش ضد فورست في بورتمان رود. سيتي 21 (7-0-0)، ارسنال 18، برايتون 16. تشيلسي ضد توتنهام السبت.",
            "pulse": "الدوري الانجليزي: الجولة 8 تبدا الليلة في ايبسويتش",
            "keywords": "الدوري الانجليزي, سيتي, ارسنال, سبيرز, تشيلسي, ايبسويتش, فورست, الجولة 8"
        },
        "basketball": {
            "tagline": "نهائيات WNBA المباراة 4: دريم يتقدم 2-1 ويبحث عن حسم لقبه الاول في اتلانتا.",
            "liveNow": "المباراة 4 في ستيت فارم ارينا: دريم يتقدم 2-1 بعد الفوز 97-71. ريس تحقق ثالث ثنائية مزدوجة تاريخية. فالكيريز امام فرصة اخيرة.",
            "pulse": "نهائيات WNBA: دريم يسعى لحسم اللقب في المباراة 4",
            "keywords": "نهائيات WNBA, المباراة 4, دريم, فالكيريز, ريس, هوارد, ستيت فارم ارينا, 2-1"
        },
        "golf": {
            "tagline": "الجولة 2 في بورت رويال: بلانشيت يتصدر بعد افتتاحية تاريخية بـ62 ضربة (-9) مع نسريْن.",
            "liveNow": "بطولة برمودا الجولة 2: تشاندلر بلانشيت يتصدر بعد 62 (-9). كونرز وكولز عند 63 (-7). ملعب بورت رويال، معدل 71 ضربة.",
            "pulse": "بورت رويال الجولة 2: بلانشيت يقود المنافسين",
            "keywords": "جولة PGA, برمودا, بورت رويال, بلانشيت, كونرز, كولز, الجولة 2, برمودا"
        },
        "home": {
            "tonight": "مكتب الجمعة",
            "tonightBlurb": "نهائي TNF: بيرز يتغلبون على باتريوتس 30-24 في سولجر فيلد. تسيتسيباس وبوبليك يبلغان نصف النهائي في الماتي. دريم على بعد فوز واحد من لقب WNBA.",
            "plTitle": "الدوري الانجليزي: الجولة 8 تبدا الليلة بمواجهة ايبسويتش ونوتنغهام فورست",
            "plBlurb": "المنافسات تنطلق في بورتمان رود قبل ديربي لندن السبت بين تشيلسي وتوتنهام. سيتي يتصدر بـ21 نقطة (7 انتصارات)، ارسنال 18، برايتون 16.",
            "f1Title": "السباق المقبل: جائزة امريكا الكبرى في اوستن",
            "f1Blurb": "تجارب الجمعة الحرة جارية في حلبة الامريكتين. السباق الاحد 25 اكتوبر الساعة 15:00 محليا. انتونيللي يتقدم على زميله راسل بـ102 نقطة."
        },
        "pg": {
            "pinFinal": "الماتي الجمعة: تسيتسيباس يهزم داكوورث 6-3 و6-4. بوبليك يهزم خاتشانوف 4-6 و7-6(5) و7-6(5). ميدفيديف يهزم اتمان 6-4 و6-4. باسيلاشفيلي يهزم مانارينو 6-3 و6-1.",
            "week1Closed": "NFL الاسبوع 7 نهائي TNF: بيرز يهزمون باتريوتس 30-24 في سولجر فيلد",
            "week1Sub": "ويليامز 308 ياردة تمرير و2 TD؛ بيردن 130 ياردة استقبال؛ سانتوس هدف ميداني من 58 ياردة. بيرز 5-2، باتريوتس 4-3. 49ers على 6-0.",
            "countdownTnf": "نهائي TNF: بيرز 30، باتريوتس 24. بيرز 5-2. 49ers في الصدارة 6-0. تشيفز وفايكنغز 5-0. بيلز 5-1.",
            "barsPoints": "الاعمدة توضح الفارق مع المتصدر. انتونيللي يملك 340 نقطة متقدما بـ102 على راسل (238). تجارب الجمعة جارية في اوستن.",
            "tableAfterMonday": "الدوري الانجليزي: سيتي يتصدر الترتيب بـ21 نقطة (7-0-0). ارسنال 18، برايتون 16. الجولة 8 تفتتح الليلة في ايبسويتش.",
            "pinClub": "اختر ناديا. سيتي يملك 21 نقطة من 7 انتصارات. ارسنال 18، برايتون 16. سبيرز هزم كوفنتري 3-1. الجولة 8 الجمعة في بورتمان رود.",
            "plFootnote": "الجولة 8 الجمعة: ايبسويتش ضد فورست؛ السبت: تشيلسي ضد سبيرز، فيلا ضد سيتي. نتيجة الاثنين: توتنهام 3، كوفنتري 1.",
            "majorsDone": "بطولة برمودا الجولة 2 جارية. تشاندلر بلانشيت يتصدر بعد افتتاحية 62 (-9) مع نسريْن. كونرز وكولز يتخلفان عند 63.",
            "wnbaFirstRound": "نهائيات WNBA المباراة 4: دريم يتقدم 2-1 بعد اكتساح 97-71. انجيل ريس تسجل ثالث ثنائية مزدوجة تاريخية (21 نقطة و12 متابعة). المباراة 4 في اتلانتا.",
            "bracketFootnote": "المباراة 1: فالكيريز 68، دريم 64. المباراة 2: دريم 79، فالكيريز 65. المباراة 3: دريم 97، فالكيريز 71. دريم يتقدم 2-1. المباراة 4 في ستيت فارم ارينا."
        }
    }
}

# Strict validation
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
    for sport_name, fields in [("football", data["football"]), ("tennis", data["tennis"]), ("f1", data["f1"]), ("soccer", data["soccer"]), ("basketball", data["basketball"]), ("golf", data["golf"])]:
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

print("All locale updates completed successfully!")
