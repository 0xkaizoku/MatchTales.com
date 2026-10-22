# -*- coding: utf-8 -*-
import re
import os

DATA = {
    "en": {
        "football": {
            "tagline": "Thursday kickoff: Patriots visit the Bears at Soldier Field. 49ers remain 6-0.",
            "liveNow": "TNF Thursday 8:15 p.m. ET: Patriots (4-2) at Bears (4-2), Prime Video, Chicago -3. Monday: 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF TONIGHT: PATRIOTS AT BEARS (4-2)",
            "keywords": "NFL Week 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Almaty Thursday: Tsitsipas closes Kukushkin farewell. Mannarino upsets Rublev.",
            "liveNow": "Almaty R16: Tsitsipas d. Kukushkin 6-1, 6-2. Mannarino d. Rublev 6-4, 3-6, 6-3. Duckworth d. Darderi 7-5, 7-6(9).",
            "pulse": "ALMATY: TSITSIPAS AND MANNARINO ADVANCE TO QF",
            "keywords": "ATP, Almaty, Tsitsipas, Kukushkin, Mannarino, Rublev, Duckworth, Darderi"
        },
        "f1": {
            "tagline": "Austin Thursday media day: one day to Friday practice. Antonelli leads Russell by 102.",
            "liveNow": "Paddock media day at COTA. Weekend 23-25 October, race Sunday 25 October at 15:00 local. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN MEDIA DAY: ONE DAY TO PRACTICE",
            "keywords": "Formula 1, United States GP, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "Matchweek 8 opens Friday with Ipswich v Forest. City lead table by three on 21.",
            "liveNow": "Standings: City 21, Arsenal 18, Brighton 16. Spurs 16th on 6, Coventry 17th on 6. MW8 opens Friday; Chelsea v Spurs Saturday.",
            "pulse": "PREMIER LEAGUE: MW8 OPENS FRIDAY AT IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Ipswich, Forest, MW8"
        },
        "basketball": {
            "tagline": "WNBA Finals Game 3: Dream crush Valkyries 97-71 to take 2-1 series lead.",
            "liveNow": "Final Wednesday: Dream 97, Valkyries 71. Angel Reese 21 pts, 12 reb, 3 stl. Game 4 Friday 8:00 p.m. ET, State Farm Arena.",
            "pulse": "WNBA FINALS: DREAM LEAD 2-1 AFTER 97-71 ROUT",
            "keywords": "WNBA Finals, Game 3, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Round 1 begins at Port Royal. Butterfield Bermuda field of 120 tees off.",
            "liveNow": "Round 1 Thursday: Port Royal Golf Course, Southampton. Field of 120, purse $6M, par 71. Defending champion Adam Schenk.",
            "pulse": "PORT ROYAL ROUND 1 UNDERWAY: 120 IN FIELD",
            "keywords": "PGA Tour, Bermuda, Port Royal, Adam Schenk, Round 1, Butterfield"
        },
        "home": {
            "tonight": "Thursday desk",
            "tonightBlurb": "Thursday Night Football: Patriots at Bears tonight at Soldier Field. Dream lead Finals 2-1 after 97-71 rout. Tsitsipas and Mannarino reach Almaty quarters.",
            "plTitle": "Premier League: City hold three-point lead as MW8 opens Friday",
            "plBlurb": "Spurs 16th on 6 after beating Coventry 3-1. City lead table on 21, Arsenal 18, Brighton 16. Ipswich host Forest on Friday; Chelsea meet Spurs on Saturday.",
            "f1Title": "Next race: United States GP in Austin",
            "f1Blurb": "Thursday media day in Austin. COTA weekend 23-25 October, race Sunday 25 October at 15:00 local. Antonelli leads Russell by 102."
        },
        "pg": {
            "pinFinal": "Almaty Thursday: Tsitsipas d. Kukushkin 6-1, 6-2. Mannarino d. Rublev 6-4, 3-6, 6-3. Duckworth d. Darderi 7-5, 7-6(9).",
            "week1Closed": "NFL Week 7 kickoff: Patriots at Bears on Thursday night",
            "week1Sub": "Patriots visit Bears at Soldier Field, 8:15 p.m. ET, Prime Video, Chicago -3. 49ers stand 6-0. Chiefs and Vikings 5-0.",
            "countdownTnf": "TNF Tonight: Patriots at Bears. Monday final: 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Bars show the gap to the leader. Antonelli has 340, 102 ahead of Russell on 238. One day to Friday practice in Austin.",
            "tableAfterMonday": "Premier League: City lead table on 21 points. Arsenal 18, Brighton 16. Spurs 16th on 6 after 3-1 win. MW8 opens Friday.",
            "pinClub": "Select a club. City are 7-0-0 on 21. Arsenal 18, Brighton 16. Spurs beat Coventry 3-1. MW8 opens Friday at Portman Road.",
            "plFootnote": "Monday final: Tottenham 3, Coventry 1. Matchweek 8 opens Friday: Ipswich v Forest; Saturday: Chelsea v Spurs, Villa v City.",
            "majorsDone": "Butterfield Bermuda opens Thursday at Port Royal, field of 120, Adam Schenk defends. Brennan won Baycurrent at 16 under.",
            "wnbaFirstRound": "WNBA Finals Game 3 final: Dream crush Valkyries 97-71, take 2-1 series lead. Reese 21 pts, 12 reb. Game 4 Friday in Atlanta.",
            "bracketFootnote": "Game 1: Valkyries 68, Dream 64. Game 2: Dream 79, Valkyries 65. Game 3: Dream 97, Valkyries 71. Dream lead series 2-1. Game 4 Friday 23 October, 8:00 p.m. ET, State Farm Arena."
        }
    },
    "fr": {
        "football": {
            "tagline": "Coup d'envoi jeudi : les Patriots rendent visite aux Bears. Les 49ers restent a 6-0.",
            "liveNow": "TNF jeudi 20 h 15 ET : Patriots (4-2) chez les Bears (4-2), Prime Video, Chicago -3. Lundi : 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF CE SOIR : PATRIOTS CHEZ LES BEARS (4-2)",
            "keywords": "NFL semaine 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Jeudi a Almaty : Tsitsipas clot les adieux de Koukouchkine. Mannarino surprend Rublev.",
            "liveNow": "Almaty 8es : Tsitsipas bat Koukouchkine 6-1, 6-2. Mannarino bat Rublev 6-4, 3-6, 6-3. Duckworth bat Darderi 7-5, 7-6(9).",
            "pulse": "ALMATY : TSITSIPAS ET MANNARINO EN QUARTS",
            "keywords": "ATP, Almaty, Tsitsipas, Kukushkin, Mannarino, Rublev, Duckworth, Darderi"
        },
        "f1": {
            "tagline": "Journee media jeudi a Austin : a un jour des essais libres. Antonelli devance Russell de 102 points.",
            "liveNow": "Paddock a COTA jeudi. Week-end du 23 au 25 octobre, course dimanche 25 octobre a 15:00 locale. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN JOURNEE MEDIA : A UN JOUR DES ESSAIS",
            "keywords": "Formule 1, GP des Etats-Unis, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "La 8e journee s'ouvre vendredi avec Ipswich contre Forest. City mene de trois points a 21.",
            "liveNow": "Classement : City 21, Arsenal 18, Brighton 16. Spurs 16es a 6, Coventry 17es a 6. 8e journee vendredi ; Chelsea - Spurs samedi.",
            "pulse": "PREMIER LEAGUE : 8E JOURNEE DES VENDREDI A IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Ipswich, Forest, 8e journee"
        },
        "basketball": {
            "tagline": "Finales WNBA match 3 : le Dream ecrase les Valkyries 97-71 et mene 2-1.",
            "liveNow": "Final mercredi : Dream 97, Valkyries 71. Angel Reese 21 pts, 12 reb, 3 int. Match 4 vendredi 20 h 00 ET, State Farm Arena.",
            "pulse": "FINALES WNBA : LE DREAM MENE 2-1 APRES UN SUCCES 97-71",
            "keywords": "WNBA Finales, match 3, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Le 1er tour debute a Port Royal. Champ de 120 joueurs aux Bermudes.",
            "liveNow": "1er tour jeudi : Port Royal Golf Course, Southampton. 120 joueurs, dotation 6 M$, par 71. Adam Schenk defend son titre.",
            "pulse": "PORT ROYAL PREMIER TOUR EN COURS : 120 JOUEURS",
            "keywords": "PGA Tour, Bermudes, Port Royal, Adam Schenk, 1er tour, Butterfield"
        },
        "home": {
            "tonight": "Bureau du jeudi",
            "tonightBlurb": "Thursday Night Football : Patriots chez les Bears ce soir. Le Dream mene 2-1 apres un succes 97-71. Tsitsipas et Mannarino en quarts a Almaty.",
            "plTitle": "Premier League : City compte trois points d'avance avant la 8e journee vendredi",
            "plBlurb": "Spurs 16es a 6 points apres leur succes 3-1 contre Coventry. City en tete a 21, Arsenal 18, Brighton 16. Ipswich recoit Forest vendredi ; Chelsea affronte les Spurs samedi.",
            "f1Title": "Prochaine course : GP des Etats-Unis a Austin",
            "f1Blurb": "Journee des medias a Austin. Week-end COTA du 23 au 25 octobre, course dimanche 25 octobre a 15:00 locale. Antonelli devance Russell de 102 points."
        },
        "pg": {
            "pinFinal": "Almaty jeudi : Tsitsipas bat Koukouchkine 6-1, 6-2. Mannarino bat Rublev 6-4, 3-6, 6-3. Duckworth bat Darderi 7-5, 7-6(9).",
            "week1Closed": "NFL semaine 7 coup d'envoi : Patriots chez les Bears jeudi soir",
            "week1Sub": "Patriots chez les Bears a Soldier Field, 20 h 15 ET, Prime Video, Chicago -3. Les 49ers restent a 6-0. Chiefs et Vikings a 5-0.",
            "countdownTnf": "TNF ce soir : Patriots chez les Bears. Lundi : 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Les barres indiquent l'ecart avec le leader. Antonelli compte 340, 102 points devant Russell a 238. A un jour des essais libres a Austin.",
            "tableAfterMonday": "Premier League : City mene avec 21 points. Arsenal 18, Brighton 16. Spurs 16es a 6 apres leur victoire 3-1. 8e journee des vendredi.",
            "pinClub": "Selectionnez un club. City est a 7-0-0 a 21. Arsenal 18, Brighton 16. Les Spurs ont battu Coventry 3-1. 8e journee vendredi a Portman Road.",
            "plFootnote": "Lundi : Tottenham 3, Coventry 1. La 8e journee s'ouvre vendredi : Ipswich - Forest ; samedi : Chelsea - Spurs, Villa - City.",
            "majorsDone": "Le Butterfield Bermuda ouvre jeudi a Port Royal, champ de 120, Adam Schenk defend son titre. Brennan a gagne le Baycurrent a 16 sous le par.",
            "wnbaFirstRound": "Finales WNBA match 3 termine : le Dream bat les Valkyries 97-71 et mene 2-1. Reese 21 pts, 12 reb. Match 4 vendredi a Atlanta.",
            "bracketFootnote": "Match 1 : Valkyries 68, Dream 64. Match 2 : Dream 79, Valkyries 65. Match 3 : Dream 97, Valkyries 71. Le Dream mene 2-1. Match 4 vendredi 23 octobre, 20 h 00 ET, State Farm Arena."
        }
    },
    "es": {
        "football": {
            "tagline": "Inicio del jueves: los Patriots visitan a los Bears en Soldier Field. 49ers siguen 6-0.",
            "liveNow": "TNF jueves 20:15 ET: Patriots (4-2) en Bears (4-2), Prime Video, Chicago -3. Lunes: 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF ESTA NOCHE: PATRIOTS EN BEARS (4-2)",
            "keywords": "NFL Semana 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Almaty jueves: Tsitsipas cierra la despedida de Kukushkin. Mannarino sorprende a Rublev.",
            "liveNow": "Almaty R16: Tsitsipas a Kukushkin 6-1, 6-2. Mannarino a Rublev 6-4, 3-6, 6-3. Duckworth a Darderi 7-5, 7-6(9).",
            "pulse": "ALMATY: TSITSIPAS Y MANNARINO A CUARTOS",
            "keywords": "ATP, Almaty, Tsitsipas, Kukushkin, Mannarino, Rublev, Duckworth, Darderi"
        },
        "f1": {
            "tagline": "Austin jueves dia de medios: a un dia de las practicas. Antonelli lidera sobre Russell por 102.",
            "liveNow": "Paddock en COTA jueves. Fin de semana 23-25 octubre, carrera domingo 25 octubre a las 15:00 local. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN DIA DE MEDIOS: A UN DIA DE LAS PRACTICAS",
            "keywords": "Formula 1, GP de Estados Unidos, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "La jornada 8 arranca el viernes con Ipswich vs Forest. City lidera por tres con 21.",
            "liveNow": "Clasificacion: City 21, Arsenal 18, Brighton 16. Spurs 16º con 6, Coventry 17º con 6. Jornada 8 el viernes; Chelsea vs Spurs sabado.",
            "pulse": "PREMIER LEAGUE: JORNADA 8 ARRANCA EL VIERNES EN IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Ipswich, Forest, Jornada 8"
        },
        "basketball": {
            "tagline": "Finales WNBA Partido 3: Dream arrolla a Valkyries 97-71 y lidera 2-1.",
            "liveNow": "Final miercoles: Dream 97, Valkyries 71. Angel Reese 21 pts, 12 reb, 3 rob. Partido 4 viernes 20:00 ET, State Farm Arena.",
            "pulse": "FINALES WNBA: DREAM LIDERA 2-1 TRAS TRIUNFO 97-71",
            "keywords": "WNBA Finales, Partido 3, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Comienza la ronda 1 en Port Royal. Campo de 120 golfistas en Bermudas.",
            "liveNow": "Ronda 1 jueves: Port Royal Golf Course, Southampton. 120 jugadores, bolsa de 6M$, par 71. Adam Schenk defiende el titulo.",
            "pulse": "PORT ROYAL RONDA 1 EN CURSO: 120 EN CAMPO",
            "keywords": "PGA Tour, Bermudas, Port Royal, Adam Schenk, Ronda 1, Butterfield"
        },
        "home": {
            "tonight": "Mesa del jueves",
            "tonightBlurb": "Thursday Night Football: Patriots en Bears esta noche. Dream lidera Finales 2-1 tras victoria 97-71. Tsitsipas y Mannarino avanzan en Almaty.",
            "plTitle": "Premier League: City sostiene tres puntos de ventaja al abrir la jornada 8 el viernes",
            "plBlurb": "Spurs 16º con 6 puntos tras vencer 3-1 a Coventry. City lidera con 21, Arsenal 18, Brighton 16. Ipswich recibe a Forest el viernes; Chelsea choca con Spurs el sabado.",
            "f1Title": "Proxima carrera: GP de Estados Unidos en Austin",
            "f1Blurb": "Dia de medios en Austin. Fin de semana en COTA 23-25 octubre, carrera domingo 25 octubre a las 15:00 local. Antonelli aventaja a Russell por 102."
        },
        "pg": {
            "pinFinal": "Almaty jueves: Tsitsipas a Kukushkin 6-1, 6-2. Mannarino a Rublev 6-4, 3-6, 6-3. Duckworth a Darderi 7-5, 7-6(9).",
            "week1Closed": "NFL Semana 7 kickoff: Patriots en Bears el jueves por la noche",
            "week1Sub": "Patriots visitan a Bears en Soldier Field, 20:15 ET, Prime Video, Chicago -3. 49ers siguen 6-0. Chiefs y Vikings 5-0.",
            "countdownTnf": "TNF esta noche: Patriots en Bears. Lunes: 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Barras muestran la diferencia con el lider. Antonelli suma 340, 102 sobre Russell con 238. A un dia de las practicas en Austin.",
            "tableAfterMonday": "Premier League: City encabeza con 21 puntos. Arsenal 18, Brighton 16. Spurs 16º con 6 tras victoria 3-1. Jornada 8 arranca el viernes.",
            "pinClub": "Elige un club. City marcha 7-0-0 con 21. Arsenal 18, Brighton 16. Spurs batio a Coventry 3-1. Jornada 8 arranca viernes en Portman Road.",
            "plFootnote": "Final del lunes: Tottenham 3, Coventry 1. Jornada 8 abre viernes: Ipswich vs Forest; sabado: Chelsea vs Spurs, Villa vs City.",
            "majorsDone": "Butterfield Bermuda arranca jueves en Port Royal, 120 competidores, Adam Schenk defiende. Brennan gano Baycurrent con 16 bajo par.",
            "wnbaFirstRound": "Finales WNBA Partido 3 final: Dream aplasta a Valkyries 97-71, ventaja 2-1. Reese 21 pts, 12 reb. Partido 4 viernes en Atlanta.",
            "bracketFootnote": "Partido 1: Valkyries 68, Dream 64. Partido 2: Dream 79, Valkyries 65. Partido 3: Dream 97, Valkyries 71. Dream lidera 2-1. Partido 4 viernes 23 de octubre, 20:00 ET, State Farm Arena."
        }
    },
    "de": {
        "football": {
            "tagline": "Donnerstag-Kickoff: Patriots gastieren bei den Bears im Soldier Field. 49ers bleiben 6-0.",
            "liveNow": "TNF Donnerstag 20:15 ET: Patriots (4-2) bei Bears (4-2), Prime Video, Chicago -3. Montag: 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF HEUTE NACHT: PATRIOTS BEI BEARS (4-2)",
            "keywords": "NFL Woche 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Almaty Donnerstag: Tsitsipas beendet Kukushkins Abschied. Mannarino ueberrascht Rublev.",
            "liveNow": "Almaty Achtelfinale: Tsitsipas d. Kukushkin 6-1, 6-2. Mannarino d. Rublev 6-4, 3-6, 6-3. Duckworth d. Darderi 7-5, 7-6(9).",
            "pulse": "ALMATY: TSITSIPAS UND MANNARINO ERREICHEN VIERTELFINALE",
            "keywords": "ATP, Almaty, Tsitsipas, Kukushkin, Mannarino, Rublev, Duckworth, Darderi"
        },
        "f1": {
            "tagline": "Austin Donnerstag Medientag: Ein Tag bis zum Freitagstraining. Antonelli fuehrt vor Russell mit 102.",
            "liveNow": "Paddock-Medientag am COTA. Wochenende 23.-25. Oktober, Rennen Sonntag 25. Oktober um 15:00 Uhr Ortszeit. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN MEDIENTAG: NOCH EIN TAG BIS ZUM TRAINING",
            "keywords": "Formel 1, Grosser Preis der USA, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "Spieltag 8 startet am Freitag mit Ipswich gegen Forest. City fuehrt Tabelle mit 21 Punkten an.",
            "liveNow": "Tabelle: City 21, Arsenal 18, Brighton 16. Spurs 16. mit 6, Coventry 17. mit 6. Spieltag 8 oeffnet Freitag; Chelsea gegen Spurs Samstag.",
            "pulse": "PREMIER LEAGUE: SPIELTAG 8 BEGINNT FREITAG IN IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Ipswich, Forest, Spieltag 8"
        },
        "basketball": {
            "tagline": "WNBA Finals Spiel 3: Dream deklassieren Valkyries 97-71 und fuehren 2-1 in der Serie.",
            "liveNow": "Endstand Mittwoch: Dream 97, Valkyries 71. Angel Reese 21 Pkt, 12 Reb, 3 Stl. Spiel 4 Freitag 20:00 ET, State Farm Arena.",
            "pulse": "WNBA FINALS: DREAM FUEHREN 2-1 NACH 97-71 KANTERSIEG",
            "keywords": "WNBA Finals, Spiel 3, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Runde 1 beginnt in Port Royal. Butterfield Bermuda Feld von 120 teet auf.",
            "liveNow": "Runde 1 Donnerstag: Port Royal Golf Course, Southampton. 120 Starter, 6 Mio. Dollar Preisgeld, Par 71. Adam Schenk Titelverteidiger.",
            "pulse": "PORT ROYAL RUNDE 1 LAEUFT: 120 IM FELD",
            "keywords": "PGA Tour, Bermuda, Port Royal, Adam Schenk, Runde 1, Butterfield"
        },
        "home": {
            "tonight": "Donnerstag Desk",
            "tonightBlurb": "Thursday Night Football: Patriots bei den Bears heute im Soldier Field. Dream fuehren in den Finals 2-1 nach 97-71. Tsitsipas und Mannarino im Almaty-Viertelfinale.",
            "plTitle": "Premier League: City haelt Drei-Punkte-Vorsprung vor Spieltag 8 am Freitag",
            "plBlurb": "Spurs 16. mit 6 Punkten nach 3-1 gegen Coventry. City fuehrt mit 21, Arsenal 18, Brighton 16. Ipswich empfaengt Forest am Freitag; Chelsea trifft Samstag auf Spurs.",
            "f1Title": "Naechstes Rennen: Grosser Preis der USA in Austin",
            "f1Blurb": "Medientag in Austin. COTA-Wochenende 23.-25. Oktober, Rennen Sonntag 25. Oktober um 15:00 Uhr Ortszeit. Antonelli hat 102 Punkte Vorsprung auf Russell."
        },
        "pg": {
            "pinFinal": "Almaty Donnerstag: Tsitsipas d. Kukushkin 6-1, 6-2. Mannarino d. Rublev 6-4, 3-6, 6-3. Duckworth d. Darderi 7-5, 7-6(9).",
            "week1Closed": "NFL Woche 7 Kickoff: Patriots bei den Bears am Donnerstagabend",
            "week1Sub": "Patriots gastieren bei Bears im Soldier Field, 20:15 ET, Prime Video, Chicago -3. 49ers stehen 6-0. Chiefs und Vikings 5-0.",
            "countdownTnf": "TNF heute Nacht: Patriots bei Bears. Montag: 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Balken zeigen den Rueckstand zur Spitze. Antonelli hat 340, 102 Punkte vor Russell mit 238. Ein Tag bis zum Freitagstraining in Austin.",
            "tableAfterMonday": "Premier League: City fuehrt mit 21 Punkten. Arsenal 18, Brighton 16. Spurs 16. mit 6 nach 3-1 Sieg. Spieltag 8 beginnt Freitag.",
            "pinClub": "Klub waehlen. City steht 7-0-0 bei 21. Arsenal 18, Brighton 16. Spurs schlugen Coventry 3-1. Spieltag 8 oeffnet Freitag an der Portman Road.",
            "plFootnote": "Montag: Tottenham 3, Coventry 1. Spieltag 8 oeffnet Freitag: Ipswich gegen Forest; Samstag: Chelsea gegen Spurs, Villa gegen City.",
            "majorsDone": "Butterfield Bermuda beginnt Donnerstag in Port Royal, Feld von 120, Adam Schenk verteidigt Titel. Brennan gewann Baycurrent mit 16 unter Par.",
            "wnbaFirstRound": "WNBA Finals Spiel 3 Endstand: Dream schlagen Valkyries 97-71, fuehren 2-1. Reese 21 Pkt, 12 Reb. Spiel 4 Freitag in Atlanta.",
            "bracketFootnote": "Spiel 1: Valkyries 68, Dream 64. Spiel 2: Dream 79, Valkyries 65. Spiel 3: Dream 97, Valkyries 71. Dream fuehren 2-1. Spiel 4 Freitag 23. Oktober, 20:00 ET, State Farm Arena."
        }
    },
    "it": {
        "football": {
            "tagline": "Calcio d'inizio giovedi: i Patriots visitano i Bears al Soldier Field. 49ers sempre sul 6-0.",
            "liveNow": "TNF giovedi 20:15 ET: Patriots (4-2) a Chicago con i Bears (4-2), Prime Video, Chicago -3. Lunedi: 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF STASERA: PATRIOTS DAI BEARS (4-2)",
            "keywords": "NFL Settimana 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Almaty giovedi: Tsitsipas chiude l'addio di Kukushkin. Mannarino sorprende Rublev.",
            "liveNow": "Almaty ottavi: Tsitsipas b. Kukushkin 6-1, 6-2. Mannarino b. Rublev 6-4, 3-6, 6-3. Duckworth b. Darderi 7-5, 7-6(9).",
            "pulse": "ALMATY: TSITSIPAS E MANNARINO VOLANO AI QUARTI",
            "keywords": "ATP, Almaty, Tsitsipas, Kukushkin, Mannarino, Rublev, Duckworth, Darderi"
        },
        "f1": {
            "tagline": "Giovedi media ad Austin: a un giorno dalle prove libere. Antonelli precede Russell di 102.",
            "liveNow": "Paddock a COTA giovedi. Weekend 23-25 ottobre, gara domenica 25 ottobre alle 15:00 locali. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN MEDIA DAY: A UN GIORNO DALLE LIBERE",
            "keywords": "Formula 1, GP Stati Uniti, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "La giornata 8 parte venerdi con Ipswich contro Forest. City in vetta a quota 21.",
            "liveNow": "Classifica: City 21, Arsenal 18, Brighton 16. Spurs 16esimi a 6, Coventry 17esimi a 6. 8a giornata venerdi; Chelsea v Spurs sabato.",
            "pulse": "PREMIER LEAGUE: 8A GIORNATA DA VENERDI A IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Ipswich, Forest, 8a giornata"
        },
        "basketball": {
            "tagline": "Finali WNBA Gara 3: Dream travolgono le Valkyries 97-71 e salgono 2-1 nella serie.",
            "liveNow": "Finale mercoledi: Dream 97, Valkyries 71. Angel Reese 21 pt, 12 rim, 3 rec. Gara 4 venerdi 20:00 ET, State Farm Arena.",
            "pulse": "FINALI WNBA: DREAM AVANTI 2-1 DOPO IL 97-71",
            "keywords": "WNBA Finali, Gara 3, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Giro 1 al via a Port Royal. Campo di 120 giocatori alle Bermuda.",
            "liveNow": "Giro 1 giovedi: Port Royal Golf Course, Southampton. 120 giocatori, montepremi 6M$, par 71. Adam Schenk difende il titolo.",
            "pulse": "PORT ROYAL GIRO 1 IN CORSO: 120 IN GARA",
            "keywords": "PGA Tour, Bermuda, Port Royal, Adam Schenk, Giro 1, Butterfield"
        },
        "home": {
            "tonight": "Banco del giovedi",
            "tonightBlurb": "Thursday Night Football: Patriots dai Bears stasera al Soldier Field. Dream avanti 2-1 nelle Finali dopo il 97-71. Tsitsipas e Mannarino ai quarti ad Almaty.",
            "plTitle": "Premier League: il City conserva tre punti di vantaggio prima della 8a giornata venerdi",
            "plBlurb": "Spurs 16esimi a 6 punti dopo aver battuto Coventry 3-1. City primo a 21, Arsenal 18, Brighton 16. Ipswich ospita Forest venerdi; Chelsea contro Spurs sabato.",
            "f1Title": "Prossima gara: GP degli Stati Uniti ad Austin",
            "f1Blurb": "Giovedi dedicato ai media ad Austin. Weekend a COTA 23-25 ottobre, gara domenica 25 ottobre alle 15:00 locali. Antonelli ha 102 punti su Russell."
        },
        "pg": {
            "pinFinal": "Almaty giovedi: Tsitsipas b. Kukushkin 6-1, 6-2. Mannarino b. Rublev 6-4, 3-6, 6-3. Duckworth b. Darderi 7-5, 7-6(9).",
            "week1Closed": "NFL Settimana 7 kickoff: Patriots dai Bears giovedi sera",
            "week1Sub": "Patriots dai Bears a Soldier Field, 20:15 ET, Prime Video, Chicago -3. 49ers sempre a 6-0. Chiefs e Vikings a 5-0.",
            "countdownTnf": "TNF stasera: Patriots dai Bears. Lunedi: 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Le barre mostrano il distacco dal leader. Antonelli ha 340 punti, 102 su Russell a 238. A un giorno dalle prove libere di Austin.",
            "tableAfterMonday": "Premier League: City primo a 21 punti. Arsenal 18, Brighton 16. Spurs 16esimi a 6 dopo il 3-1. 8a giornata venerdi.",
            "pinClub": "Seleziona un club. City e 7-0-0 a 21. Arsenal 18, Brighton 16. Gli Spurs hanno battuto Coventry 3-1. 8a giornata da venerdi a Portman Road.",
            "plFootnote": "Lunedi: Tottenham 3, Coventry 1. La giornata 8 comincia venerdi: Ipswich contro Forest; sabato: Chelsea contro Spurs, Villa contro City.",
            "majorsDone": "Butterfield Bermuda inizia giovedi a Port Royal, campo di 120, Adam Schenk difende il titolo. Brennan ha vinto il Baycurrent a 16 sotto il par.",
            "wnbaFirstRound": "Finali WNBA Gara 3 finale: Dream abbattono Valkyries 97-71, avanti 2-1. Reese 21 pt, 12 rim. Gara 4 venerdi ad Atlanta.",
            "bracketFootnote": "Gara 1: Valkyries 68, Dream 64. Gara 2: Dream 79, Valkyries 65. Gara 3: Dream 97, Valkyries 71. Dream avanti 2-1. Gara 4 venerdi 23 ottobre, 20:00 ET, State Farm Arena."
        }
    },
    "pl": {
        "football": {
            "tagline": "Czwartkowy kickoff: Patriots odwiedzaja Bears na Soldier Field. 49ers pozostaja 6-0.",
            "liveNow": "TNF czwartek 20:15 ET: Patriots (4-2) u Bears (4-2), Prime Video, Chicago -3. Poniedzialek: 49ers 23, Commanders 17 (49ers 6-0).",
            "pulse": "TNF DZIS W NOCY: PATRIOTS U BEARS (4-2)",
            "keywords": "NFL Tydzien 7, Patriots, Bears, 49ers, Commanders, Chiefs, Soldier Field, TNF"
        },
        "tennis": {
            "tagline": "Almaty czwartek: Tsitsipas konczy pozegnanie Kukuszkina. Mannarino pokonuje Rublowa.",
            "liveNow": "Almaty 1/8 finalu: Tsitsipas pokonal Kukuszkina 6-1, 6-2. Mannarino pokonal Rublowa 6-4, 3-6, 6-3. Duckworth pokonal Darderiego 7-5, 7-6(9).",
            "pulse": "ALMATY: TSITSIPAS I MANNARINO W CWIERCFINALE",
            "keywords": "ATP, Almaty, Tsitsipas, Kukushkin, Mannarino, Rublev, Duckworth, Darderi"
        },
        "f1": {
            "tagline": "Czwartek medialny w Austin: jeden dzien do piatkowych treningow. Antonelli wyprzedza Russella o 102.",
            "liveNow": "Padok w COTA w czwartek. Weekend 23-25 pazdziernika, wyscig niedziela 25 pazdziernika o 15:00 czasu lokalnego. Antonelli 340, Russell 238. Mercedes 578.",
            "pulse": "AUSTIN DZIEN MEDIALNY: JEDEN DZIEN DO TRENINGOW",
            "keywords": "Formula 1, GP USA, Austin, COTA, Antonelli, Russell, Mercedes, Ferrari"
        },
        "soccer": {
            "tagline": "Kolejka 8 rusza w piatek meczem Ipswich z Forest. City prowadzi z 21 punktami.",
            "liveNow": "Tabela: City 21, Arsenal 18, Brighton 16. Spurs 16. miejsce z 6 pkt, Coventry 17. z 6 pkt. Kolejka 8 w piatek; Chelsea - Spurs w sobote.",
            "pulse": "PREMIER LEAGUE: KOLEJKA 8 RUSZA W PIATEK W IPSWICH",
            "keywords": "Premier League, City, Arsenal, Spurs, Chelsea, Coventry, Ipswich, Forest, Kolejka 8"
        },
        "basketball": {
            "tagline": "Finaly WNBA mecz 3: Dream rozbily Valkyries 97-71 i prowadza 2-1 w serii.",
            "liveNow": "Koniec w srode: Dream 97, Valkyries 71. Angel Reese 21 pkt, 12 zb, 3 prz. Mecz 4 w piatek 20:00 ET, State Farm Arena.",
            "pulse": "FINALY WNBA: DREAM PROWADZA 2-1 PO POGROMIE 97-71",
            "keywords": "WNBA Finaly, Mecz 3, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Runda 1 rusza w Port Royal. 120 golfistow na Bermudach.",
            "liveNow": "Runda 1 czwartek: Port Royal Golf Course, Southampton. 120 graczy, pula 6 mln USD, par 71. Adam Schenk broni tytulu.",
            "pulse": "PORT ROYAL RUNDA 1 W TOKU: 120 ZAWODNIKOW",
            "keywords": "PGA Tour, Bermudy, Port Royal, Adam Schenk, Runda 1, Butterfield"
        },
        "home": {
            "tonight": "Czwartkowe biurko",
            "tonightBlurb": "Thursday Night Football: Patriots u Bears dzis na Soldier Field. Dream prowadza 2-1 po pogromie 97-71. Tsitsipas i Mannarino w cwiercfinale w Almaty.",
            "plTitle": "Premier League: City utrzymuje trzy punkty przewagi przed kolejka 8 w piatek",
            "plBlurb": "Spurs 16. z 6 pkt po wygranej 3-1 z Coventry. City liderem z 21 pkt, Arsenal 18, Brighton 16. Ipswich podejmuje Forest w piatek; Chelsea gra ze Spurs w sobote.",
            "f1Title": "Nastepny wyscig: GP USA w Austin",
            "f1Blurb": "Dzien medialny w Austin. Weekend w COTA 23-25 pazdziernika, wyscig niedziela 25 pazdziernika o 15:00. Antonelli ma 102 pkt przewagi nad Russellem."
        },
        "pg": {
            "pinFinal": "Almaty czwartek: Tsitsipas pokonal Kukuszkina 6-1, 6-2. Mannarino pokonal Rublowa 6-4, 3-6, 6-3. Duckworth pokonal Darderiego 7-5, 7-6(9).",
            "week1Closed": "NFL Tydzien 7 kickoff: Patriots u Bears w czwartkowy wieczor",
            "week1Sub": "Patriots u Bears na Soldier Field, 20:15 ET, Prime Video, Chicago -3. 49ers maja 6-0. Chiefs i Vikings 5-0.",
            "countdownTnf": "TNF dzis w nocy: Patriots u Bears. Poniedzialek: 49ers 23, Commanders 17 (49ers 6-0). Chiefs 22-6, Bills 33-30.",
            "barsPoints": "Paski pokazuja strate do lidera. Antonelli ma 340, 102 pkt przed Russellem z 238. Jeden dzien do piatkowych treningow w Austin.",
            "tableAfterMonday": "Premier League: City prowadzi z 21 punktami. Arsenal 18, Brighton 16. Spurs 16. z 6 pkt po wygranej 3-1. Kolejka 8 od piatku.",
            "pinClub": "Wybierz klub. City ma 7-0-0 i 21 pkt. Arsenal 18, Brighton 16. Spurs pokonali Coventry 3-1. Kolejka 8 rusza w piatek na Portman Road.",
            "plFootnote": "Poniedzialek: Tottenham 3, Coventry 1. Kolejka 8 startuje w piatek: Ipswich - Forest; sobota: Chelsea - Spurs, Villa - City.",
            "majorsDone": "Butterfield Bermuda rusza w czwartek w Port Royal, 120 graczy, Adam Schenk broni tytulu. Brennan wygral Baycurrent z wynikiem 16 ponizej par.",
            "wnbaFirstRound": "Finaly WNBA mecz 3: Dream rozbily Valkyries 97-71, prowadza 2-1. Reese 21 pkt, 12 zb. Mecz 4 w piatek w Atlancie.",
            "bracketFootnote": "Mecz 1: Valkyries 68, Dream 64. Mecz 2: Dream 79, Valkyries 65. Mecz 3: Dream 97, Valkyries 71. Dream prowadza 2-1. Mecz 4 w piatek 23 pazdziernika, 20:00 ET, State Farm Arena."
        }
    },
    "zh": {
        "football": {
            "tagline": "周四开球：新英格兰爱国者作客士兵球场挑战熊队。49人保持6胜0负。",
            "liveNow": "TNF周四美东20:15：爱国者(4-2)作客熊队(4-2)，Prime Video，芝加哥让3分。周一：49人23-17指挥官(49人6-0)。",
            "pulse": "今晚周四夜赛：爱国者作客挑战熊队(4-2)",
            "keywords": "NFL第7周, 爱国者, 熊队, 49人, 指挥官, 酋长, 士兵球场, TNF"
        },
        "tennis": {
            "tagline": "阿拉木图周四：西西帕斯送别库库什金。马纳里诺爆冷击败卢布列夫。",
            "liveNow": "阿拉木图16强：西西帕斯 6-1, 6-2 库库什金；马纳里诺 6-4, 3-6, 6-3 卢布列夫；达克沃斯 7-5, 7-6(9) 达尔德里。",
            "pulse": "阿拉木图：西西帕斯与马纳里诺晋级八强",
            "keywords": "ATP, 阿拉木图, 西西帕斯, 库库什金, 马纳里诺, 卢布列夫, 达克沃斯, 达尔德里"
        },
        "f1": {
            "tagline": "奥斯汀周四媒体日：距离周五一练仅剩一天。安东内利领先拉塞尔102分。",
            "liveNow": "COTA围场媒体日。10月23至25日周末，正赛周日10月25日当地时间15:00。安东内利340分，拉塞尔238分。梅赛德斯578分。",
            "pulse": "奥斯汀媒体日：距离练习赛仅剩一天",
            "keywords": "一级方程式, 美国大奖赛, 奥斯汀, COTA, 安东内利, 拉塞尔, 梅赛德斯, 法拉利"
        },
        "soccer": {
            "tagline": "英超第8轮周五由伊普斯维奇对阵诺丁汉森林打响。曼城21分领跑。",
            "liveNow": "积分榜：曼城21，阿森纳18，布莱顿16。热刺第16积6分，考文垂第17积6分。第8轮周五开打；切尔西对热刺周六进行。",
            "pulse": "英超联赛：第8轮周五在伊普斯维奇开打",
            "keywords": "英超, 曼城, 阿森纳, 热刺, 切尔西, 考文垂, 伊普斯维奇, 森林, 第8轮"
        },
        "basketball": {
            "tagline": "WNBA总决赛G3：梦想队97-71大胜女武神，系列赛2-1领先。",
            "liveNow": "周三完场：梦想队 97-71 女武神。安吉尔·里斯21分12篮板3抢断。G4周五美东20:00，州立农业球馆。",
            "pulse": "WNBA总决赛：梦想队大胜97-71取得2-1领先",
            "keywords": "WNBA总决赛, G3, 梦想队, 女武神, 里斯, 霍华德, 州立农业球馆, 2-1"
        },
        "golf": {
            "tagline": "皇家港首轮开打。百慕大锦标赛120名球员登场。",
            "liveNow": "周四首轮：南安普敦皇家港高尔夫球场。120人参赛，总奖金600万美元，标准杆71杆。亚当·申克卫冕。",
            "pulse": "皇家港首轮进行中：120名选手角逐",
            "keywords": "美巡赛, 百慕大, 皇家港, 亚当申克, 首轮, 巴特菲尔德"
        },
        "home": {
            "tonight": "周四编辑台",
            "tonightBlurb": "今晚周四夜赛：爱国者作客挑战熊队。梦想队97-71大胜女武神取得总决赛2-1领先。西西帕斯与马纳里诺晋级阿拉木图八强。",
            "plTitle": "英超联赛：曼城握有3分领跑优势，第8轮周五打响",
            "plBlurb": "热刺3-1击败考文垂后位列第16积6分。曼城21分领跑，阿森纳18分，布莱顿16分。伊普斯维奇周五迎战森林；切尔西周六对阵热刺。",
            "f1Title": "下一站：奥斯汀美国大奖赛",
            "f1Blurb": "奥斯汀周四媒体日。COTA赛道周末10月23至25日，正赛周日10月25日当地时间15:00。安东内利领先拉塞尔102分。"
        },
        "pg": {
            "pinFinal": "阿拉木图周四：西西帕斯 6-1, 6-2 库库什金；马纳里诺 6-4, 3-6, 6-3 卢布列夫；达克沃斯 7-5, 7-6(9) 达尔德里。",
            "week1Closed": "NFL第7周开踢：爱国者周四夜赛作客熊队",
            "week1Sub": "爱国者作客士兵球场挑战熊队，美东20:15，Prime Video，芝加哥让3分。49人6-0。酋长与维京人5-0。",
            "countdownTnf": "今晚TNF：爱国者挑战熊队。周一完场：49人23-17指挥官(49人6-0)。酋长22-6，水牛城33-30。",
            "barsPoints": "柱状图显示与领跑者的差距。安东内利340分，领先238分的拉塞尔102分。距离奥斯汀练习赛还有一天。",
            "tableAfterMonday": "英超：曼城积21分位居榜首。阿森纳18分，布莱顿16分。热刺3-1取胜后积6分排第16。第8轮周五开打。",
            "pinClub": "选择俱乐部。曼城7胜0平积21分。阿森纳18分，布莱顿16分。热刺3-1击败考文垂。第8轮周五在波特曼路球场开战。",
            "plFootnote": "周一赛果：热刺 3-1 考文垂。第8轮周五揭幕：伊普斯维奇对森林；周六：切尔西对热刺，维拉对曼城。",
            "majorsDone": "百慕大锦标赛周四在皇家港开打，120人阵容，亚当·申克卫冕。布伦南以低于标准杆16杆斩获湾流锦标赛冠军。",
            "wnbaFirstRound": "WNBA总决赛G3完场：梦想队97-71大胜女武神取得2-1领先。里斯21分12篮板。G4周五在亚特兰大进行。",
            "bracketFootnote": "G1：女武神 68-64 梦想队。G2：梦想队 79-65 女武神。G3：梦想队 97-71 女武神。梦想队2-1领先。G4周五10月23日美东20:00，州立农业球馆。"
        }
    },
    "ja": {
        "football": {
            "tagline": "木曜キックオフ：ソルジャー・フィールドでペイトリオッツがベアーズと対戦。49ersは6勝0敗を維持。",
            "liveNow": "TNF木曜20:15 ET：ペイトリオッツ(4-2)対ベアーズ(4-2)、Prime Video、シカゴ-3。月曜：49ers 23、コマンダーズ 17 (49ers 6-0)。",
            "pulse": "今夜TNF：ペイトリオッツ対ベアーズ (4-2)",
            "keywords": "NFL第7週, ペイトリオッツ, ベアーズ, 49ers, コマンダーズ, チーフス, ソルジャー・フィールド, TNF"
        },
        "tennis": {
            "tagline": "アルマトイ木曜：チチパスがククシュキンの引退試合を制す。マナリノがルブレフを破る波乱。",
            "liveNow": "アルマトイ16強：チチパス 6-1, 6-2 ククシュキン。マナリノ 6-4, 3-6, 6-3 ルブレフ。ダックワース 7-5, 7-6(9) ダルデリ。",
            "pulse": "アルマトイ：チチパスとマナリノが準々決勝進出",
            "keywords": "ATP, アルマトイ, チチパス, ククシュキン, マナリノ, ルブレフ, ダックワース, ダルデリ"
        },
        "f1": {
            "tagline": "オースティン木曜メディアデー：金曜フリー走行まであと1日。アントネッリがラッセルを102点リード。",
            "liveNow": "COTAパドックメディアデー。10月23-25日週末、決勝日曜10月25日現地15:00。アントネッリ340点、ラッセル238点。メルセデス578点。",
            "pulse": "オースティン メディアデー：走行開始まであと1日",
            "keywords": "F1, アメリカGP, オースティン, COTA, アントネッリ, ラッセル, メルセデス, フェラーリ"
        },
        "soccer": {
            "tagline": "プレミア第8節は金曜のイプスウィッチ対フォレストで開幕。シティが勝点21で首位堅持。",
            "liveNow": "順位表：シティ21、アーセナル18、ブライトン16。スパーズ勝点6で16位、コベントリー勝点6で17位。第8節金曜開幕、土曜にチェルシー対スパーズ。",
            "pulse": "プレミアリーグ：第8節が金曜イプスウィッチで開幕",
            "keywords": "プレミアリーグ, シティ, アーセナル, スパーズ, チェルシー, コベントリー, イプスウィッチ, フォレスト, 第8節"
        },
        "basketball": {
            "tagline": "WNBAファイナル第3戦：ドリームが97-71でヴァルキリーズを圧倒し2勝1敗とリード。",
            "liveNow": "水曜結果：ドリーム 97, ヴァルキリーズ 71。エンジェル・リース21得点12リバウンド3スティール。第4戦金曜20:00 ET、ステートファーム・アリーナ。",
            "pulse": "WNBAファイナル：ドリームが97-71の大勝で2勝1敗とリード",
            "keywords": "WNBAファイナル, 第3戦, ドリーム, ヴァルキリーズ, リース, ハワード, ステートファーム・アリーナ, 2-1"
        },
        "golf": {
            "tagline": "ポートロイヤルで第1ラウンド開幕。バミューダ選手権120選手が出場。",
            "liveNow": "第1ラウンド木曜：ポートロイヤル・ゴルフコース。120名出場、賞金600万ドル、パー71。アダム・シェンクが連覇に挑む。",
            "pulse": "ポートロイヤル第1R進行中：120選手がティオフ",
            "keywords": "PGAツアー, バミューダ, ポートロイヤル, アダム・シェンク, 第1ラウンド, バターフィールド"
        },
        "home": {
            "tonight": "木曜デスク",
            "tonightBlurb": "今夜TNF：ペイトリオッツが敵地ソルジャー・フィールドでベアーズと対戦。ドリームが97-71の大勝でファイナル2勝1敗。チチパスとマナリノがアルマトイ8強進出。",
            "plTitle": "プレミアリーグ：金曜開幕の第8節を前にシティが3点差で首位",
            "plBlurb": "スパーズはコベントリーに3-1で勝ち勝点6で16位。シティ21、アーセナル18、ブライトン16。金曜にイプスウィッチ対フォレスト、土曜にチェルシー対スパーズ。",
            "f1Title": "次戦：オースティンでのアメリカGP",
            "f1Blurb": "オースティンでの木曜メディアデー。COTA週末10月23-25日、決勝日曜10月25日現地15:00。アントネッリがラッセルに102点リード。"
        },
        "pg": {
            "pinFinal": "アルマトイ木曜：チチパス 6-1, 6-2 ククシュキン。マナリノ 6-4, 3-6, 6-3 ルブレフ。ダックワース 7-5, 7-6(9) ダルデリ。",
            "week1Closed": "NFL第7週キックオフ：木曜夜にペイトリオッツ対ベアーズ",
            "week1Sub": "ペイトリオッツがソルジャー・フィールドでベアーズと激突、20:15 ET、Prime Video、シカゴ-3。49ersは6-0。チーフスとバイキングスは5-0。",
            "countdownTnf": "今夜TNF：ペイトリオッツ対ベアーズ。月曜：49ers 23, コマンダーズ 17 (49ers 6-0)。チーフス 22-6、ビルズ 33-30。",
            "barsPoints": "バーは首位との差を示します。アントネッリは340点で238点のラッセルを102点リード。オースティンの走行まであと1日。",
            "tableAfterMonday": "プレミアリーグ：シティが勝点21で首位。アーセナル18、ブライトン16。スパーズは3-1勝利で勝点6の16位。第8節金曜開幕。",
            "pinClub": "クラブを選択。シティは7勝0敗で21点。アーセナル18、ブライトン16。スパーズはコベントリーに3-1で勝利。第8節は金曜ポートマン・ロードで開幕。",
            "plFootnote": "月曜結果：トッテナム 3, コベントリー 1。第8節金曜開幕：イプスウィッチ対フォレスト、土曜：チェルシー対スパーズ、ヴィラ対シティ。",
            "majorsDone": "バターフィールド・バミューダ選手権が木曜ポートロイヤルで開幕、120選手、アダム・シェンク連覇へ。ブレナンが16アンダーでベイカレント制覇。",
            "wnbaFirstRound": "WNBAファイナル第3戦結果：ドリームが97-71でヴァルキリーズを圧倒、2勝1敗リード。リース21得点12リバウンド。第4戦金曜アトランタ。",
            "bracketFootnote": "第1戦：ヴァルキリーズ 68, ドリーム 64。第2戦：ドリーム 79, ヴァルキリーズ 65。第3戦：ドリーム 97, ヴァルキリーズ 71。ドリーム2勝1敗。第4戦金曜10月23日20:00 ET、ステートファーム・アリーナ。"
        }
    },
    "ko": {
        "football": {
            "tagline": "목요일 킥오프: 솔저 필드에서 패트리어츠와 베어스 격돌. 49ers는 6승 0패 유지.",
            "liveNow": "TNF 목요일 20:15 ET: 패트리어츠(4-2) at 베어스(4-2), Prime Video, 시카고 -3. 월요일: 49ers 23, 커맨더스 17 (49ers 6-0).",
            "pulse": "오늘 밤 TNF: 패트리어츠 AT 베어스 (4-2)",
            "keywords": "NFL 7주차, 패트리어츠, 베어스, 49ers, 커맨더스, 치프스, 솔저 필드, TNF"
        },
        "tennis": {
            "tagline": "알마티 목요일: 치치파스, 쿠쿠슈킨 고별전 제압. 마나리노, 루블료프 꺾는 이변.",
            "liveNow": "알마티 16강: 치치파스 승 6-1, 6-2 쿠쿠슈킨. 마나리노 승 6-4, 3-6, 6-3 루블료프. 더크워스 승 7-5, 7-6(9) 다르데리.",
            "pulse": "알마티: 치치파스와 마나리노 8강 진출",
            "keywords": "ATP, 알마티, 치치파스, 쿠쿠슈킨, 마나리노, 루블료프, 더크워스, 다르데리"
        },
        "f1": {
            "tagline": "오스틴 목요일 미디어데이: 금요일 연습 주행까지 하루. 안토넬리, 러셀에 102점 차 리드.",
            "liveNow": "COTA 패덕 미디어데이. 10월 23-25일 주말, 결선 일요일 10월 25일 현지 15:00. 안토넬리 340, 러셀 238. 메르세데스 578.",
            "pulse": "오스틴 미디어데이: 연습 주행까지 하루",
            "keywords": "F1, 미국 GP, 오스틴, COTA, 안토넬리, 러셀, 메르세데스, 페라리"
        },
        "soccer": {
            "tagline": "프리미어리그 8라운드 금요일 입스위치 대 포레스트로 개막. 맨시티 승점 21로 3점 차 선두.",
            "liveNow": "순위표: 맨시티 21, 아스널 18, 브라이튼 16. 토트넘 6점으로 16위, 코번트리 6점으로 17위. 8R 금요일 개막, 토요일 첼시 대 토트넘.",
            "pulse": "프리미어리그: 8라운드 금요일 입스위치에서 개막",
            "keywords": "프리미어리그, 맨시티, 아스널, 토트넘, 첼시, 코번트리, 입스위치, 포레스트, 8R"
        },
        "basketball": {
            "tagline": "WNBA 파이널 3차전: 드림, 발키리스 97-71로 대파하고 시리즈 2-1 리드.",
            "liveNow": "수요일 최종: 드림 97, 발키리스 71. 엔젤 리스 21득점 12리바운드 3스틸. 4차전 금요일 20:00 ET, 스테이트팜 아레나.",
            "pulse": "WNBA 파이널: 드림, 97-71 대승으로 시리즈 2-1 리드",
            "keywords": "WNBA 파이널, 3차전, 드림, 발키리스, 리스, 하워드, 스테이트팜 아레나, 2-1"
        },
        "golf": {
            "tagline": "포트 로열에서 1라운드 개막. 버뮤다 챔피언십 120명 출전.",
            "liveNow": "1라운드 목요일: 포트 로열 골프코스. 120명 출전, 총상금 600만 달러, 파 71. 디펜딩 챔피언 애덤 솅크.",
            "pulse": "포트 로열 1라운드 진행 중: 120명 티오프",
            "keywords": "PGA 투어, 버뮤다, 포트 로열, 애덤 솅크, 1라운드, 버터필드"
        },
        "home": {
            "tonight": "목요일 데스크",
            "tonightBlurb": "오늘 밤 목요일 나이트 풋볼: 패트리어츠 솔저 필드에서 베어스와 격돌. 드림, 97-71 대승으로 파이널 2-1 리드. 치치파스와 마나리노 알마티 8강 안착.",
            "plTitle": "프리미어리그: 금요일 8R 개막 앞두고 맨시티 3점 차 선두 질주",
            "plBlurb": "토트넘은 코번트리전 3-1 승리로 승점 6점 16위. 맨시티 21점 선두, 아스널 18점, 브라이튼 16점. 금요일 입스위치 대 포레스트, 토요일 첼시 대 토트넘.",
            "f1Title": "다음 레이스: 오스틴 미국 그랑프리",
            "f1Blurb": "오스틴 목요일 미디어데이. COTA 주말 10월 23-25일, 결선 일요일 10월 25일 현지 15:00. 안토넬리 러셀에 102점 차 리드."
        },
        "pg": {
            "pinFinal": "알마티 목요일: 치치파스 승 6-1, 6-2 쿠쿠슈킨. 마나리노 승 6-4, 3-6, 6-3 루블료프. 더크워스 승 7-5, 7-6(9) 다르데리.",
            "week1Closed": "NFL 7주차 킥오프: 목요일 밤 패트리어츠 at 베어스",
            "week1Sub": "패트리어츠 솔저 필드에서 베어스 상대, 20:15 ET, Prime Video, 시카고 -3. 49ers 6승 0패. 치프스와 바이킹스 5승 0패.",
            "countdownTnf": "오늘 밤 TNF: 패트리어츠 at 베어스. 월요일 결과: 49ers 23, 커맨더스 17 (49ers 6-0). 치프스 22-6, 빌스 33-30.",
            "barsPoints": "막대는 선두와의 격차를 보여줍니다. 안토넬리 340점, 238점의 러셀에 102점 앞섬. 오스틴 연습 주행까지 하루.",
            "tableAfterMonday": "프리미어리그: 맨시티 승점 21점으로 선두. 아스널 18점, 브라이튼 16점. 토트넘 3-1 승리로 6점 16위. 8R 금요일 개막.",
            "pinClub": "클럽 선택. 맨시티 7승 0패 21점. 아스널 18점, 브라이튼 16점. 토트넘 코번트리 3-1 제압. 8R 포트먼 로드에서 금요일 개막.",
            "plFootnote": "월요일 결과: 토트넘 3, 코번트리 1. 8R 금요일 개막: 입스위치 대 포레스트; 토요일: 첼시 대 토트넘, 빌라 대 맨시티.",
            "majorsDone": "버터필드 버뮤다 목요일 포트 로열 개막, 120명 출전, 애덤 솅크 타이틀 방어. 브레넌 16언더파로 베이커런트 우승.",
            "wnbaFirstRound": "WNBA 파이널 3차전 최종: 드림 발키리스 97-71 격파, 시리즈 2-1 리드. 리스 21득점 12리바운드. 4차전 금요일 애틀랜타.",
            "bracketFootnote": "1차전: 발키리스 68, 드림 64. 2차전: 드림 79, 발키리스 65. 3차전: 드림 97, 발키리스 71. 드림 2-1 리드. 4차전 금요일 10월 23일 20:00 ET, 스테이트팜 아레나."
        }
    },
    "ar": {
        "football": {
            "tagline": "انطلاق الخميس: باتريوتس يحل ضيفا على بيرز في سولجر فيلد. سان فرانسيسكو يحافظ على 6-0.",
            "liveNow": "TNF الخميس 20:15 بتوقيت شرق أمريكا: باتريوتس (4-2) لدى بيرز (4-2)، برايم فيديو، شيكاغو -3. الاثنين: 49ers 23، كوماندرز 17 (49ers 6-0).",
            "pulse": "TNF الليلة: باتريوتس يواجه بيرز (4-2)",
            "keywords": "NFL الأسبوع 7, باتريوتس, بيرز, 49ers, كوماندرز, تشيفس, سولجر فيلد, TNF"
        },
        "tennis": {
            "tagline": "ألماتي الخميس: تسيتسيباس ينهي مسيرة كوكوشكين الوداعية. مانارينو يفاجئ روبليف.",
            "liveNow": "ألماتي ثمن النهائي: تسيتسيباس يهزم كوكوشكين 6-1, 6-2. مانارينو يهزم روبليف 6-4, 3-6, 6-3. داكورث يهزم دارديري 7-5, 7-6(9).",
            "pulse": "ألماتي: تسيتسيباس ومانارينو إلى ربع النهائي",
            "keywords": "ATP, ألماتي, تسيتسيباس, كوكوشكين, مانارينو, روبليف, داكورث, دارديري"
        },
        "f1": {
            "tagline": "يوم الإعلام الخميس في أوستن: يوم واحد على انطلاق التجارب الحرة. أنتونيللي يتقدم بـ 102 نقطة.",
            "liveNow": "يوم الإعلام في حلبة كوتا. عطلة نهاية الأسبوع 23-25 أكتوبر، السباق الأحد 25 أكتوبر الساعة 15:00 بالتوقيت المحلي. أنتونيللي 340، راسل 238. مرسيدس 578.",
            "pulse": "أوستن يوم الإعلام: يوم واحد على التجارب الحرة",
            "keywords": "فورمولا 1, جائزة أمريكا الكبرى, أوستن, كوتا, أنتونيللي, راسل, مرسيدس, فيراري"
        },
        "soccer": {
            "tagline": "الجولة 8 تنطلق الجمعة بلقاء إيبسويتش ونوتنغهام فورست. سيتي يتصدر بـ 21 نقطة.",
            "liveNow": "الترتيب: سيتي 21، أرسنال 18، برايتون 16. توتنهام بالمركز 16 برصيد 6، كوفنتري 17 برصيد 6. الجولة 8 تنطلق الجمعة؛ تشيلسي ضد توتنهام السبت.",
            "pulse": "الدوري الإنجليزي: الجولة 8 تنطلق الجمعة في إيبسويتش",
            "keywords": "الدوري الإنجليزي, سيتي, أرسنال, توتنهام, تشيلسي, كوفنتري, إيبسويتش, فورست, الجولة 8"
        },
        "basketball": {
            "tagline": "نهائي WNBA المباراة 3: دريم يسحق فالكيريز 97-71 ويتقدم 2-1 في السلسلة.",
            "liveNow": "النتيجة النهائية الأربعاء: دريم 97، فالكيريز 71. أنجيل ريس 21 نقطة و12 متابعة و3 سرقات. المباراة 4 الجمعة 20:00 ET، ستيت فارم أرينا.",
            "pulse": "نهائي WNBA: دريم يتقدم 2-1 بعد فوز كاسح 97-71",
            "keywords": "نهائي WNBA, المباراة 3, دريم, فالكيريز, ريس, هاوارد, ستيت فارم أرينا, 2-1"
        },
        "golf": {
            "tagline": "انطلاق الجولة الأولى في بورت رويال. 120 لاعبا في برمودا.",
            "liveNow": "الجولة الأولى الخميس: ملعب بورت رويال، ساوثهامبتون. 120 لاعبا، جوائز 6 ملايين دولار، بار 71. آدم شينك يدافع عن اللقب.",
            "pulse": "بورت رويال الجولة الأولى جارية: 120 في الميدان",
            "keywords": "جولة PGA, برمودا, بورت رويال, آدم شينك, الجولة الأولى, بترفيلد"
        },
        "home": {
            "tonight": "مكتب الخميس",
            "tonightBlurb": "Thursday Night Football: باتريوتس يواجه بيرز الليلة في سولجر فيلد. دريم يتقدم 2-1 بعد الفوز 97-71. تسيتسيباس ومانارينو في ربع نهائي ألماتي.",
            "plTitle": "الدوري الإنجليزي: سيتي يتقدم بفارق 3 نقاط قبل انطلاق الجولة 8 الجمعة",
            "plBlurb": "توتنهام في المركز 16 بـ 6 نقاط بعد فوزه 3-1 على كوفنتري. سيتي في الصدارة بـ 21 نقطة، أرسنال 18، برايتون 16. إيبسويتش يستضيف فورست الجمعة؛ تشيلسي يلتقي توتنهام السبت.",
            "f1Title": "السباق القادم: جائزة الولايات المتحدة الكبرى في أوستن",
            "f1Blurb": "يوم الإعلام في أوستن. عطلة نهاية الأسبوع 23-25 أكتوبر، السباق الأحد 25 أكتوبر الساعة 15:00 بالتوقيت المحلي. أنتونيللي يتقدم على راسل بفارق 102 نقطة."
        },
        "pg": {
            "pinFinal": "ألماتي الخميس: تسيتسيباس يهزم كوكوشكين 6-1, 6-2. مانارينو يهزم روبليف 6-4, 3-6, 6-3. داكورث يهزم دارديري 7-5, 7-6(9).",
            "week1Closed": "انطلاق الأسبوع 7 من NFL: باتريوتس لدى بيرز ليلة الخميس",
            "week1Sub": "باتريوتس يحل ضيفا على بيرز في سولجر فيلد، 20:15 ET، برايم فيديو، شيكاغو -3. 49ers في الصدارة 6-0. تشيفس وفايكنغز 5-0.",
            "countdownTnf": "TNF الليلة: باتريوتس لدى بيرز. نتيجة الاثنين: 49ers 23، كوماندرز 17 (49ers 6-0). تشيفس 22-6، بيلز 33-30.",
            "barsPoints": "الأشرطة توضح الفارق مع المتصدر. أنتونيللي لديه 340 نقطة، متقدما بـ 102 نقطة على راسل (238). يوم واحد على تجارب أوستن الحرة.",
            "tableAfterMonday": "الدوري الإنجليزي: سيتي يتصدر بـ 21 نقطة. أرسنال 18، برايتون 16. توتنهام بالمركز 16 برصيد 6 نقاط بعد فوز 3-1. الجولة 8 تنطلق الجمعة.",
            "pinClub": "اختر ناديا. سيتي 7-0-0 برصيد 21 نقطة. أرسنال 18، برايتون 16. توتنهام فاز 3-1 على كوفنتري. الجولة 8 تنطلق الجمعة في بورتمان رود.",
            "plFootnote": "نتيجة الاثنين: توتنهام 3، كوفنتري 1. الجولة 8 تفتتح الجمعة: إيبسويتش ضد فورست؛ السبت: تشيلسي ضد توتنهام، فيلا ضد سيتي.",
            "majorsDone": "بطولة بترفيلد برمودا تنطلق الخميس في بورت رويال، 120 لاعبا، آدم شينك يدافع عن اللقب. برينان فاز بلقب باي كرنت بـ 16 تحت المعدل.",
            "wnbaFirstRound": "نهائي WNBA المباراة 3: دريم يسحق فالكيريز 97-71 ويتقدم 2-1. ريس 21 نقطة و12 متابعة. المباراة 4 الجمعة في أتلانتا.",
            "bracketFootnote": "المباراة 1: فالكيريز 68، دريم 64. المباراة 2: دريم 79، فالكيريز 65. المباراة 3: دريم 97، فالكيريز 71. دريم يتقدم 2-1. المباراة 4 الجمعة 23 أكتوبر، 20:00 ET، ستيت فارم أرينا."
        }
    }
}

# Verify no em-dash or double-hyphen in DATA
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
