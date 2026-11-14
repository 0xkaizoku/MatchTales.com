#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update playground.ts, messages.ts, and all messages-*.ts across all 10 locales for 14 November 2026."""
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

DATA = {
    "en": {
        "common": {
            "todayDesk": "Saturday desk: Commanders 24-21 Giants (Diggs 32-yd at 0:57). Spurs 123-85 Warriors (Castle 32). Stockholm final today Fritz vs Tirante. Dubai R2: McIlroy and Hatton 139.",
            "todayNfl": "TNF Final: Commanders 24, Giants 21. Daniels 3 TD, Diggs winner, Douglas INT. WSH 3-5-1, NYG 5-3-1. No Saturday NFL game. Sunday Munich: Patriots vs Lions, 9:30 a.m. ET FOX.",
            "todayTnf": "NFL Week 10 TNF Final: Commanders 24-21 Giants at MetLife. Saturday dark. Next: Patriots vs Lions, Munich, Sunday 9:30 a.m. ET FOX."
        },
        "football": {
            "tagline": "TNF Final: Diggs 32-yard TD with 0:57 left lifts Commanders 24-21 over Giants. No Saturday NFL game.",
            "liveNow": "FINAL Thu: Commanders 24, Giants 21 (Daniels 3 TD, Diggs winner, Douglas INT). WSH 3-5-1, NYG 5-3-1. Sunday Munich: Patriots vs Lions, 9:30 a.m. ET FOX.",
            "pulse": "NFL TNF FINAL: COMMANDERS 24-21 GIANTS ON DIGGS TD AT 0:57; SATURDAY DARK, SUNDAY MUNICH",
            "keywords": "NFL Week 10, Thursday Night Football, Commanders, Giants, Jayden Daniels, Stefon Diggs"
        },
        "basketball": {
            "tagline": "Spurs 123-85 Warriors for an 11th straight win; Castle 32. Thursday: Cunningham 52 in 2OT.",
            "liveNow": "Fri: Spurs 123, Warriors 85 (Castle 32, Wemby 12/12/6). Thu: Pistons 144-140 2OT Wizards (Cunningham 52). Tonight: 5 NBA games upcoming.",
            "pulse": "NBA: SPURS 11TH STRAIGHT 123-85, CASTLE 32; CUNNINGHAM 52 IN DOUBLE OT THURSDAY",
            "keywords": "NBA, San Antonio Spurs, Golden State Warriors, Stephon Castle, Victor Wembanyama, Cade Cunningham"
        },
        "soccer": {
            "tagline": "Kane penalty wins England 2-1 on cap 126; Arsenal hold Barcelona 1-1 at Camp Nou. Sunday: Spain vs England.",
            "liveNow": "Thu Finals: England 2-1 Croatia (Rogers 24, Kane 64 pen); Italy 3-1 France; Czechia 0-2 Spain; Barcelona 1-1 Arsenal. Sunday 19:45 GMT: Spain vs England, Madrid.",
            "pulse": "ENGLAND 2-1 CROATIA AND BARCELONA 1-1 ARSENAL; SUNDAY SPAIN VS ENGLAND IN MADRID",
            "keywords": "UWCL, Barcelona, Arsenal, Nations League, Harry Kane, England, Croatia, Spain"
        },
        "tennis": {
            "tagline": "Stockholm Final Today: Fritz vs Tirante after a 6-4, 6-2 SF. Turin opens Sunday with Zverev vs Jodar.",
            "liveNow": "Today Final: Fritz vs Tirante (upcoming). Fri SF: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). QF: Fritz walkover Rune. Turin Sunday.",
            "pulse": "STOCKHOLM FINAL TODAY FRITZ VS TIRANTE; TURIN OPENS SUNDAY ZVEREV VS JODAR",
            "keywords": "Stockholm Open, Taylor Fritz, Thiago Agustin Tirante, Nitto ATP Finals, Turin, Alexander Zverev"
        },
        "f1": {
            "tagline": "Five days to Round 21 Las Vegas: 33 points still split Verstappen to Norris. No Strip race yet.",
            "liveNow": "Drivers P2 race unchanged: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Round 21: 19-21 Nov.",
            "pulse": "FIVE DAYS TO VEGAS: VERSTAPPEN TO NORRIS STILL 33 PTS BEHIND CHAMPION ANTONELLI",
            "keywords": "Formula 1, Round 21, Las Vegas GP, Max Verstappen, Lando Norris, Kimi Antonelli, Mercedes"
        },
        "golf": {
            "tagline": "Dubai R2 complete: McIlroy and Hatton share 139 (-5). Round 3 Saturday unpublished as final.",
            "liveNow": "R2 AP: T1 McIlroy 69-70=139, Hatton 70-69=139; T3 Luiten 140, Reitan 140; Chacarra 143 (T11). R3 in progress, not posted as final.",
            "pulse": "DUBAI R2: MCILROY AND HATTON SHARE 139; LUITEN 140; R3 NOT PUBLISHED AS FINAL",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Tyrrell Hatton, Joost Luiten, Eugenio Chacarra"
        },
        "home": {
            "tonight": "Saturday desk",
            "tonightBlurb": "Commanders beat Giants 24-21 on Diggs' 32-yard score with 57 seconds left. Spurs rolled Warriors 123-85 (Castle 32). Stockholm final today is Fritz vs Tirante. Dubai R2: McIlroy and Hatton share 139. Sunday: Spain vs England in Madrid; Patriots vs Lions in Munich unpublished.",
            "plTitle": "England 2-1 Croatia and Barcelona 1-1 Arsenal; Sunday Spain vs England in Madrid",
            "plBlurb": "Arsenal still lead the PL on 27 (Brighton 22, Man City 21, Liverpool 18). Thursday: Kane penalty on cap 126; Maanum and Hansen share UWCL spoils 1-1. Sunday 19:45 GMT: Spain vs England, Metropolitano.",
            "f1Title": "Five days to Round 21 Las Vegas: 33 points still split Verstappen (279) to Norris (246)",
            "f1Blurb": "Mercedes (652) and Antonelli (390) remain champions entering the 6.201 km Strip (19-21 Nov), with Ferrari (510), Red Bull (415) and McLaren (398). No race result."
        },
        "pg": {
            "pinFinal": "Stockholm Final Today: Fritz vs Tirante. Fri SF: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). Turin Sunday: Zverev vs Jodar.",
            "week1Closed": "NFL Week 10 TNF: Commanders 24, Giants 21 at MetLife (Diggs 32-yd TD at 0:57).",
            "week1Sub": "Daniels 23/33, 249 yds, 3 TD; Douglas INT. WSH 3-5-1, NYG 5-3-1. Saturday dark. Sunday Munich: Patriots vs Lions 9:30 a.m. ET FOX.",
            "countdownTnf": "TNF FINAL: Commanders 24-21 Giants. Saturday 14 Nov has no NFL game. Next: Patriots vs Lions, Munich, Sunday 9:30 a.m. ET FOX.",
            "gridAfterMadrid": "Drivers & Constructors Entering Round 21 · Las Vegas Strip (19-21 Nov)",
            "barsPoints": "Antonelli (390) & Mercedes (652) Champions; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Premier League Break (MW10): Arsenal lead 27 pts, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Select a club. Arsenal lead on 27, Brighton 22, Man City 21, Liverpool 18, Chelsea and Everton 16.",
            "plFootnote": "Thu: Barcelona 1-1 Arsenal (Maanum 22, Hansen 59); England 2-1 Croatia (Kane 64 pen, cap 126). Sunday: Spain vs England 19:45 GMT.",
            "majorsDone": "Dubai R2 Complete (AP): McIlroy & Hatton -5 (139), Luiten & Reitan -4 (140), Chacarra -1 (143, T11). R3 Saturday unpublished."
        }
    },
    "fr": {
        "common": {
            "todayDesk": "Bureau du samedi : Commanders 24-21 Giants (Diggs a 0:57). Spurs 123-85 Warriors (Castle 32). Finale de Stockholm aujourd'hui Fritz vs Tirante. Dubai T2 : McIlroy et Hatton 139.",
            "todayNfl": "TNF termine : Commanders 24, Giants 21. Daniels 3 TD, Diggs vainqueur, Douglas INT. WSH 3-5-1, NYG 5-3-1. Pas de match NFL samedi. Dimanche Munich : Patriots vs Lions, 9h30 ET FOX.",
            "todayTnf": "NFL Semaine 10 TNF : Commanders 24-21 Giants au MetLife. Samedi vide. Suivant : Patriots vs Lions a Munich, dimanche 9h30 ET FOX."
        },
        "football": {
            "tagline": "TNF : Diggs inscrit un TD de 32 yards a 0:57 et les Commanders battent les Giants 24-21. Pas de NFL samedi.",
            "liveNow": "FINAL jeudi : Commanders 24, Giants 21 (Daniels 3 TD, Diggs, Douglas INT). WSH 3-5-1, NYG 5-3-1. Dimanche Munich : Patriots vs Lions, 9h30 ET FOX.",
            "pulse": "NFL TNF : COMMANDERS 24-21 GIANTS SUR TD DE DIGGS A 0:57 ; SAMEDI VIDE, DIMANCHE MUNICH",
            "keywords": "NFL Semaine 10, Commanders, Giants, Jayden Daniels, Stefon Diggs, TNF"
        },
        "basketball": {
            "tagline": "Spurs 123-85 Warriors pour une 11e victoire d'affilee ; Castle 32. Jeudi : Cunningham 52 en 2OT.",
            "liveNow": "Ven : Spurs 123, Warriors 85 (Castle 32, Wemby 12/12/6). Jeu : Pistons 144-140 2OT Wizards (Cunningham 52). Ce soir : 5 matchs NBA a venir.",
            "pulse": "NBA : 11e SUCCES D'AFFILEE DES SPURS 123-85, CASTLE 32 ; CUNNINGHAM 52 JEUDI EN 2OT",
            "keywords": "NBA, Spurs, Warriors, Stephon Castle, Wembanyama, Cade Cunningham"
        },
        "soccer": {
            "tagline": "Penalty de Kane : Angleterre 2-1 pour sa 126e selection ; Arsenal tient Barcelone 1-1. Dimanche : Espagne vs Angleterre.",
            "liveNow": "Jeudi : Angleterre 2-1 Croatie (Rogers 24, Kane 64 pen) ; Italie 3-1 France ; Tchequie 0-2 Espagne ; Barcelone 1-1 Arsenal. Dimanche 19h45 GMT : Espagne-Angleterre a Madrid.",
            "pulse": "ANGLETERRE 2-1 CROATIE ET BARCELONE 1-1 ARSENAL ; DIMANCHE ESPAGNE VS ANGLETERRE A MADRID",
            "keywords": "UWCL, Barcelone, Arsenal, Ligue des nations, Harry Kane, Angleterre, Croatie, Espagne"
        },
        "tennis": {
            "tagline": "Finale de Stockholm aujourd'hui : Fritz vs Tirante apres 6-4, 6-2 en demie. Turin ouvre dimanche avec Zverev vs Jodar.",
            "liveNow": "Finale aujourd'hui : Fritz vs Tirante (a venir). Ven SF : Fritz bat Musetti 6-4, 6-2 ; Tirante bat Tabilo 7-5, 7-6 (1). QF : Fritz walkover Rune. Turin dimanche.",
            "pulse": "FINALE DE STOCKHOLM AUJOURD'HUI FRITZ VS TIRANTE ; TURIN OUVRE DIMANCHE ZVEREV VS JODAR",
            "keywords": "Stockholm Open, Taylor Fritz, Thiago Agustin Tirante, Nitto ATP Finals, Turin, Zverev"
        },
        "f1": {
            "tagline": "J-5 avant la manche 21 a Las Vegas : 33 points separent encore Verstappen de Norris. Pas de course sur le Strip.",
            "liveNow": "Course a P2 inchangee : Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390 ; Mercedes 652). Manche 21 : 19-21 nov.",
            "pulse": "J-5 AVANT LAS VEGAS : VERSTAPPEN A NORRIS TOUJOURS 33 PTS DERRIERE ANTONELLI",
            "keywords": "Formule 1, Manche 21, Las Vegas GP, Verstappen, Norris, Antonelli, Mercedes"
        },
        "golf": {
            "tagline": "Dubai T2 terminee : McIlroy et Hatton partagent 139 (-5). T3 samedi non publiee comme finale.",
            "liveNow": "T2 AP : T1 McIlroy 69-70=139, Hatton 70-69=139 ; T3 Luiten 140, Reitan 140 ; Chacarra 143 (T11). T3 en cours, non publiee.",
            "pulse": "DUBAI T2 : MCILROY ET HATTON A 139 ; LUITEN 140 ; T3 NON PUBLIEE COMME FINALE",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Tyrrell Hatton, Joost Luiten, Eugenio Chacarra"
        },
        "home": {
            "tonight": "Bureau du samedi",
            "tonightBlurb": "Les Commanders battent les Giants 24-21 sur un TD de 32 yards de Diggs a 57 secondes de la fin. Les Spurs ecrasent les Warriors 123-85 (Castle 32). Finale de Stockholm aujourd'hui : Fritz vs Tirante. Dubai T2 : McIlroy et Hatton a 139. Dimanche : Espagne-Angleterre a Madrid ; Patriots-Lions a Munich non publie.",
            "plTitle": "Angleterre 2-1 Croatie et Barcelone 1-1 Arsenal ; dimanche Espagne vs Angleterre a Madrid",
            "plBlurb": "Arsenal mene toujours en PL avec 27 pts (Brighton 22, Man City 21, Liverpool 18). Jeudi : penalty de Kane pour sa 126e cape ; Maanum et Hansen se partagent l'UWCL 1-1. Dimanche 19h45 GMT : Espagne-Angleterre.",
            "f1Title": "J-5 avant Las Vegas (manche 21) : 33 points separent encore Verstappen (279) de Norris (246)",
            "f1Blurb": "Mercedes (652) et Antonelli (390) restent champions avant les 6,201 km du Strip (19-21 nov) devant Ferrari (510), Red Bull (415) et McLaren (398). Pas de resultat de course."
        },
        "pg": {
            "pinFinal": "Finale Stockholm aujourd'hui : Fritz vs Tirante. Ven SF : Fritz bat Musetti 6-4, 6-2 ; Tirante bat Tabilo 7-5, 7-6 (1). Turin dimanche : Zverev vs Jodar.",
            "week1Closed": "NFL Semaine 10 TNF : Commanders 24, Giants 21 au MetLife (TD de 32 yards de Diggs a 0:57).",
            "week1Sub": "Daniels 23/33, 249 yds, 3 TD ; Douglas INT. WSH 3-5-1, NYG 5-3-1. Samedi vide. Dimanche Munich : Patriots vs Lions 9h30 ET FOX.",
            "countdownTnf": "TNF TERMINE : Commanders 24-21 Giants. Pas de match NFL samedi 14 nov. Suivant : Patriots vs Lions a Munich, dimanche 9h30 ET FOX.",
            "gridAfterMadrid": "Pilotes et Constructeurs avant la manche 21 · Las Vegas Strip (19-21 nov)",
            "barsPoints": "Antonelli (390) et Mercedes (652) champions ; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Treve Premier League (J10) : Arsenal 27 pts, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Choisissez un club. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea et Everton 16.",
            "plFootnote": "Jeu : Barcelone 1-1 Arsenal (Maanum 22, Hansen 59) ; Angleterre 2-1 Croatie (Kane 64 pen, 126e cape). Dimanche : Espagne-Angleterre 19h45 GMT.",
            "majorsDone": "Dubai T2 (AP) : McIlroy et Hatton -5 (139), Luiten et Reitan -4 (140), Chacarra -1 (143, T11). T3 samedi non publiee."
        }
    },
    "es": {
        "common": {
            "todayDesk": "Sabado: Commanders 24-21 Giants (Diggs a 0:57). Spurs 123-85 Warriors (Castle 32). Final de Estocolmo hoy Fritz vs Tirante. Dubai R2: McIlroy y Hatton 139.",
            "todayNfl": "TNF final: Commanders 24, Giants 21. Daniels 3 TD, Diggs ganador, Douglas INT. WSH 3-5-1, NYG 5-3-1. Sin NFL el sabado. Domingo Munich: Patriots vs Lions, 9:30 ET FOX.",
            "todayTnf": "NFL Semana 10 TNF: Commanders 24-21 Giants en MetLife. Sabado sin partido. Siguiente: Patriots vs Lions en Munich, domingo 9:30 ET FOX."
        },
        "football": {
            "tagline": "TNF: Diggs anota de 32 yardas a falta de 0:57 y Commanders vencen 24-21 a Giants. Sin NFL el sabado.",
            "liveNow": "FINAL jue: Commanders 24, Giants 21 (Daniels 3 TD, Diggs, Douglas INT). WSH 3-5-1, NYG 5-3-1. Domingo Munich: Patriots vs Lions, 9:30 ET FOX.",
            "pulse": "NFL TNF: COMMANDERS 24-21 GIANTS CON TD DE DIGGS A 0:57; SABADO SIN PARTIDO, DOMINGO MUNICH",
            "keywords": "NFL Semana 10, Commanders, Giants, Jayden Daniels, Stefon Diggs, TNF"
        },
        "basketball": {
            "tagline": "Spurs 123-85 Warriors, undécima seguida; Castle 32. Jueves: Cunningham 52 en 2OT.",
            "liveNow": "Vie: Spurs 123, Warriors 85 (Castle 32, Wemby 12/12/6). Jue: Pistons 144-140 2OT Wizards (Cunningham 52). Hoy: 5 partidos NBA por jugar.",
            "pulse": "NBA: SPURS 11 SEGUIDAS 123-85, CASTLE 32; CUNNINGHAM 52 EL JUEVES EN DOBLE PRORROGA",
            "keywords": "NBA, Spurs, Warriors, Stephon Castle, Wembanyama, Cade Cunningham"
        },
        "soccer": {
            "tagline": "Penalty de Kane: Inglaterra 2-1 en su cap 126; Arsenal empata 1-1 en el Camp Nou. Domingo: Espana vs Inglaterra.",
            "liveNow": "Jueves: Inglaterra 2-1 Croacia (Rogers 24, Kane 64 pen); Italia 3-1 Francia; Chequia 0-2 Espana; Barcelona 1-1 Arsenal. Domingo 19:45 GMT: Espana-Inglaterra en Madrid.",
            "pulse": "INGLATERRA 2-1 CROACIA Y BARCELONA 1-1 ARSENAL; DOMINGO ESPANA VS INGLATERRA EN MADRID",
            "keywords": "UWCL, Barcelona, Arsenal, Liga de Naciones, Harry Kane, Inglaterra, Croacia, Espana"
        },
        "tennis": {
            "tagline": "Final de Estocolmo hoy: Fritz vs Tirante tras 6-4, 6-2 en SF. Turin abre el domingo con Zverev vs Jodar.",
            "liveNow": "Final hoy: Fritz vs Tirante (pendiente). Vie SF: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). CF: Fritz walkover Rune. Turin domingo.",
            "pulse": "FINAL DE ESTOCOLMO HOY FRITZ VS TIRANTE; TURIN ABRE EL DOMINGO ZVEREV VS JODAR",
            "keywords": "Estocolmo, Taylor Fritz, Thiago Agustin Tirante, Nitto ATP Finals, Turin, Zverev"
        },
        "f1": {
            "tagline": "Cinco dias para la ronda 21 en Las Vegas: 33 puntos siguen separando a Verstappen de Norris. Sin carrera en el Strip.",
            "liveNow": "Pelea por P2 igual: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Ronda 21: 19-21 nov.",
            "pulse": "CINCO DIAS PARA LAS VEGAS: VERSTAPPEN A NORRIS SIGUEN A 33 PTS DEL CAMPEON ANTONELLI",
            "keywords": "Formula 1, Ronda 21, Las Vegas GP, Verstappen, Norris, Antonelli, Mercedes"
        },
        "golf": {
            "tagline": "Dubai R2 cerrada: McIlroy y Hatton comparten 139 (-5). R3 del sabado no se publica como final.",
            "liveNow": "R2 AP: T1 McIlroy 69-70=139, Hatton 70-69=139; T3 Luiten 140, Reitan 140; Chacarra 143 (T11). R3 en juego, no publicada.",
            "pulse": "DUBAI R2: MCILROY Y HATTON COMPARTEN 139; LUITEN 140; R3 NO PUBLICADA COMO FINAL",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Tyrrell Hatton, Joost Luiten, Eugenio Chacarra"
        },
        "home": {
            "tonight": "Sabado al dia",
            "tonightBlurb": "Commanders ganan 24-21 a Giants con TD de 32 yardas de Diggs a 57 segundos. Spurs golean 123-85 a Warriors (Castle 32). Final de Estocolmo hoy: Fritz vs Tirante. Dubai R2: McIlroy y Hatton a 139. Domingo: Espana-Inglaterra en Madrid; Patriots-Lions en Munich sin publicar.",
            "plTitle": "Inglaterra 2-1 Croacia y Barcelona 1-1 Arsenal; domingo Espana vs Inglaterra en Madrid",
            "plBlurb": "Arsenal sigue lider en Premier con 27 (Brighton 22, Man City 21, Liverpool 18). Jueves: penalty de Kane en el cap 126; Maanum y Hansen empatan 1-1 en UWCL. Domingo 19:45 GMT: Espana-Inglaterra.",
            "f1Title": "Cinco dias para Las Vegas (ronda 21): 33 puntos entre Verstappen (279) y Norris (246)",
            "f1Blurb": "Mercedes (652) y Antonelli (390) siguen campeones hacia el circuito de 6,201 km (19-21 nov) con Ferrari (510), Red Bull (415) y McLaren (398). Sin resultado de carrera."
        },
        "pg": {
            "pinFinal": "Final Estocolmo hoy: Fritz vs Tirante. Vie SF: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). Turin domingo: Zverev vs Jodar.",
            "week1Closed": "NFL Semana 10 TNF: Commanders 24, Giants 21 en MetLife (TD de 32 yardas de Diggs a 0:57).",
            "week1Sub": "Daniels 23/33, 249 yds, 3 TD; Douglas INT. WSH 3-5-1, NYG 5-3-1. Sabado sin NFL. Domingo Munich: Patriots vs Lions 9:30 ET FOX.",
            "countdownTnf": "TNF FINAL: Commanders 24-21 Giants. El sabado 14 nov no hay NFL. Siguiente: Patriots vs Lions en Munich, domingo 9:30 ET FOX.",
            "gridAfterMadrid": "Pilotos y Constructores hacia Ronda 21 · Las Vegas Strip (19-21 nov)",
            "barsPoints": "Antonelli (390) y Mercedes (652) campeones; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Pausa Premier League (J10): Arsenal 27 pts, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Elige un club. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea y Everton 16.",
            "plFootnote": "Jue: Barcelona 1-1 Arsenal (Maanum 22, Hansen 59); Inglaterra 2-1 Croacia (Kane 64 pen, cap 126). Domingo: Espana-Inglaterra 19:45 GMT.",
            "majorsDone": "Dubai R2 (AP): McIlroy y Hatton -5 (139), Luiten y Reitan -4 (140), Chacarra -1 (143, T11). R3 sabado no publicada."
        }
    },
    "de": {
        "common": {
            "todayDesk": "Samstag: Commanders 24:21 Giants (Diggs bei 0:57). Spurs 123:85 Warriors (Castle 32). Stockholm-Finale heute Fritz vs. Tirante. Dubai R2: McIlroy und Hatton 139.",
            "todayNfl": "TNF-Finale: Commanders 24, Giants 21. Daniels 3 TD, Diggs Siegtor, Douglas INT. WSH 3-5-1, NYG 5-3-1. Samstag kein NFL-Spiel. Sonntag Muenchen: Patriots vs. Lions, 9:30 ET FOX.",
            "todayTnf": "NFL Woche 10 TNF: Commanders 24:21 Giants im MetLife. Samstag spielfrei. Naechstes: Patriots vs. Lions in Muenchen, Sonntag 9:30 ET FOX."
        },
        "football": {
            "tagline": "TNF: Diggs trifft aus 32 Yards bei 0:57, Commanders schlagen Giants 24:21. Samstag kein NFL-Spiel.",
            "liveNow": "FINAL Do: Commanders 24, Giants 21 (Daniels 3 TD, Diggs, Douglas INT). WSH 3-5-1, NYG 5-3-1. Sonntag Muenchen: Patriots vs. Lions, 9:30 ET FOX.",
            "pulse": "NFL TNF: COMMANDERS 24:21 GIANTS DURCH DIGGS-TD BEI 0:57; SAMSTAG FREI, SONNTAG MUENCHEN",
            "keywords": "NFL Woche 10, Commanders, Giants, Jayden Daniels, Stefon Diggs, TNF"
        },
        "basketball": {
            "tagline": "Spurs 123:85 Warriors zum 11. Sieg in Serie; Castle 32. Donnerstag: Cunningham 52 in 2OT.",
            "liveNow": "Fr: Spurs 123, Warriors 85 (Castle 32, Wemby 12/12/6). Do: Pistons 144:140 2OT Wizards (Cunningham 52). Heute: 5 NBA-Spiele bevorstehend.",
            "pulse": "NBA: SPURS 11. SIEG IN SERIE 123:85, CASTLE 32; CUNNINGHAM 52 AM DONNERSTAG IN 2OT",
            "keywords": "NBA, Spurs, Warriors, Stephon Castle, Wembanyama, Cade Cunningham"
        },
        "soccer": {
            "tagline": "Kane-Elfmeter: England 2:1 bei Cap 126; Arsenal haelt Barcelona 1:1. Sonntag: Spanien vs. England.",
            "liveNow": "Donnerstag: England 2:1 Kroatien (Rogers 24, Kane 64 Elfm.); Italien 3:1 Frankreich; Tschechien 0:2 Spanien; Barcelona 1:1 Arsenal. Sonntag 19:45 GMT: Spanien-England in Madrid.",
            "pulse": "ENGLAND 2:1 KROATIEN UND BARCELONA 1:1 ARSENAL; SONNTAG SPANIEN VS. ENGLAND IN MADRID",
            "keywords": "UWCL, Barcelona, Arsenal, Nations League, Harry Kane, England, Kroatien, Spanien"
        },
        "tennis": {
            "tagline": "Stockholm-Finale heute: Fritz vs. Tirante nach 6:4, 6:2 im HF. Turin startet Sonntag mit Zverev vs. Jodar.",
            "liveNow": "Finale heute: Fritz vs. Tirante (ausstehend). Fr HF: Fritz d Musetti 6:4, 6:2; Tirante d Tabilo 7:5, 7:6 (1). VF: Fritz walkover Rune. Turin Sonntag.",
            "pulse": "STOCKHOLM-FINALE HEUTE FRITZ VS. TIRANTE; TURIN STARTET SONNTAG ZVEREV VS. JODAR",
            "keywords": "Stockholm Open, Taylor Fritz, Thiago Agustin Tirante, Nitto ATP Finals, Turin, Zverev"
        },
        "f1": {
            "tagline": "Noch fuenf Tage bis Runde 21 in Las Vegas: 33 Punkte trennen weiter Verstappen und Norris. Kein Strip-Rennen.",
            "liveNow": "P2-Duell unveraendert: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Runde 21: 19.-21. Nov.",
            "pulse": "FUENF TAGE BIS LAS VEGAS: VERSTAPPEN BIS NORRIS WEITER 33 PUNKTE HINTER ANTONELLI",
            "keywords": "Formel 1, Runde 21, Las Vegas GP, Verstappen, Norris, Antonelli, Mercedes"
        },
        "golf": {
            "tagline": "Dubai R2 komplett: McIlroy und Hatton teilen 139 (-5). R3 am Samstag nicht als Finale veroeffentlicht.",
            "liveNow": "R2 AP: T1 McIlroy 69-70=139, Hatton 70-69=139; T3 Luiten 140, Reitan 140; Chacarra 143 (T11). R3 laeuft, nicht als Finale.",
            "pulse": "DUBAI R2: MCILROY UND HATTON TEILEN 139; LUITEN 140; R3 NICHT ALS FINALE VEROFFENTLICHT",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Tyrrell Hatton, Joost Luiten, Eugenio Chacarra"
        },
        "home": {
            "tonight": "Samstag im Fokus",
            "tonightBlurb": "Commanders schlagen Giants 24:21 durch Diggs' 32-Yards-TD bei 57 Sekunden. Spurs deklassieren Warriors 123:85 (Castle 32). Stockholm-Finale heute: Fritz vs. Tirante. Dubai R2: McIlroy und Hatton 139. Sonntag: Spanien-England in Madrid; Patriots-Lions in Muenchen unveröffentlicht.",
            "plTitle": "England 2:1 Kroatien und Barcelona 1:1 Arsenal; Sonntag Spanien vs. England in Madrid",
            "plBlurb": "Arsenal fuehrt die PL weiter an (27 vor Brighton 22, Man City 21, Liverpool 18). Donnerstag: Kane-Elfmeter bei Cap 126; Maanum und Hansen teilen UWCL 1:1. Sonntag 19:45 GMT: Spanien-England.",
            "f1Title": "Fuenf Tage bis Las Vegas (Runde 21): 33 Punkte zwischen Verstappen (279) und Norris (246)",
            "f1Blurb": "Mercedes (652) und Antonelli (390) bleiben Weltmeister vor dem 6,201-km-Strip (19.-21. Nov) vor Ferrari (510), Red Bull (415) und McLaren (398). Kein Rennergebnis."
        },
        "pg": {
            "pinFinal": "Stockholm-Finale heute: Fritz vs. Tirante. Fr HF: Fritz d Musetti 6:4, 6:2; Tirante d Tabilo 7:5, 7:6 (1). Turin Sonntag: Zverev vs. Jodar.",
            "week1Closed": "NFL Woche 10 TNF: Commanders 24, Giants 21 im MetLife (Diggs 32-Yards-TD bei 0:57).",
            "week1Sub": "Daniels 23/33, 249 Yds, 3 TD; Douglas INT. WSH 3-5-1, NYG 5-3-1. Samstag frei. Sonntag Muenchen: Patriots vs. Lions 9:30 ET FOX.",
            "countdownTnf": "TNF-FINALE: Commanders 24:21 Giants. Samstag, 14. Nov., kein NFL-Spiel. Naechstes: Patriots vs. Lions in Muenchen, Sonntag 9:30 ET FOX.",
            "gridAfterMadrid": "Fahrer & Konstrukteure vor Runde 21 · Las Vegas Strip (19.-21. Nov)",
            "barsPoints": "Antonelli (390) & Mercedes (652) Champions; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "PL-Pause (Spieltag 10): Arsenal 27 Pkt., Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Klub waehlen. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea und Everton 16.",
            "plFootnote": "Do: Barcelona 1:1 Arsenal (Maanum 22, Hansen 59); England 2:1 Kroatien (Kane 64 Elfm., Cap 126). Sonntag: Spanien-England 19:45 GMT.",
            "majorsDone": "Dubai R2 (AP): McIlroy & Hatton -5 (139), Luiten & Reitan -4 (140), Chacarra -1 (143, T11). R3 Samstag unveröffentlicht."
        }
    },
    "it": {
        "common": {
            "todayDesk": "Sabato: Commanders 24-21 Giants (Diggs a 0:57). Spurs 123-85 Warriors (Castle 32). Finale di Stoccolma oggi Fritz vs Tirante. Dubai R2: McIlroy e Hatton 139.",
            "todayNfl": "TNF chiuso: Commanders 24, Giants 21. Daniels 3 TD, Diggs decisivo, Douglas INT. WSH 3-5-1, NYG 5-3-1. Niente NFL sabato. Domenica Monaco: Patriots vs Lions, 9:30 ET FOX.",
            "todayTnf": "NFL Week 10 TNF: Commanders 24-21 Giants al MetLife. Sabato vuoto. Prossimo: Patriots vs Lions a Monaco, domenica 9:30 ET FOX."
        },
        "football": {
            "tagline": "TNF: Diggs segna da 32 yard a 0:57 e i Commanders battono i Giants 24-21. Niente NFL sabato.",
            "liveNow": "FINAL gio: Commanders 24, Giants 21 (Daniels 3 TD, Diggs, Douglas INT). WSH 3-5-1, NYG 5-3-1. Domenica Monaco: Patriots vs Lions, 9:30 ET FOX.",
            "pulse": "NFL TNF: COMMANDERS 24-21 GIANTS CON TD DI DIGGS A 0:57; SABATO VUOTO, DOMENICA MONACO",
            "keywords": "NFL Week 10, Commanders, Giants, Jayden Daniels, Stefon Diggs, TNF"
        },
        "basketball": {
            "tagline": "Spurs 123-85 Warriors, undicesima di fila; Castle 32. Giovedi: Cunningham 52 in 2OT.",
            "liveNow": "Ven: Spurs 123, Warriors 85 (Castle 32, Wemby 12/12/6). Gio: Pistons 144-140 2OT Wizards (Cunningham 52). Stasera: 5 gare NBA in programma.",
            "pulse": "NBA: SPURS 11 DI FILA 123-85, CASTLE 32; CUNNINGHAM 52 GIOVEDI IN DOPPIO OT",
            "keywords": "NBA, Spurs, Warriors, Stephon Castle, Wembanyama, Cade Cunningham"
        },
        "soccer": {
            "tagline": "Rigore di Kane: Inghilterra 2-1 alla 126a presenza; l'Arsenal ferma il Barcellona 1-1. Domenica: Spagna vs Inghilterra.",
            "liveNow": "Giovedi: Inghilterra 2-1 Croazia (Rogers 24, Kane 64 rig.); Italia 3-1 Francia; Cechia 0-2 Spagna; Barcellona 1-1 Arsenal. Domenica 19:45 GMT: Spagna-Inghilterra a Madrid.",
            "pulse": "INGHILTERRA 2-1 CROAZIA E BARCELLONA 1-1 ARSENAL; DOMENICA SPAGNA VS INGHILTERRA A MADRID",
            "keywords": "UWCL, Barcellona, Arsenal, Nations League, Harry Kane, Inghilterra, Croazia, Spagna"
        },
        "tennis": {
            "tagline": "Finale di Stoccolma oggi: Fritz vs Tirante dopo 6-4, 6-2 in SF. Torino apre domenica con Zverev vs Jodar.",
            "liveNow": "Finale oggi: Fritz vs Tirante (in programma). Ven SF: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). QF: Fritz walkover Rune. Torino domenica.",
            "pulse": "FINALE DI STOCCOLMA OGGI FRITZ VS TIRANTE; TORINO APRE DOMENICA ZVEREV VS JODAR",
            "keywords": "Stoccolma, Taylor Fritz, Thiago Agustin Tirante, Nitto ATP Finals, Torino, Zverev"
        },
        "f1": {
            "tagline": "Cinque giorni alla Round 21 di Las Vegas: 33 punti dividono ancora Verstappen e Norris. Nessuna gara sullo Strip.",
            "liveNow": "Corsa a P2 invariata: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Round 21: 19-21 nov.",
            "pulse": "CINQUE GIORNI A LAS VEGAS: VERSTAPPEN-NORRIS ANCORA A 33 PTS DAL CAMPIONE ANTONELLI",
            "keywords": "Formula 1, Round 21, Las Vegas GP, Verstappen, Norris, Antonelli, Mercedes"
        },
        "golf": {
            "tagline": "Dubai R2 chiuso: McIlroy e Hatton condividono 139 (-5). R3 di sabato non pubblicata come finale.",
            "liveNow": "R2 AP: T1 McIlroy 69-70=139, Hatton 70-69=139; T3 Luiten 140, Reitan 140; Chacarra 143 (T11). R3 in corso, non pubblicata.",
            "pulse": "DUBAI R2: MCILROY E HATTON A 139; LUITEN 140; R3 NON PUBBLICATA COME FINALE",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Tyrrell Hatton, Joost Luiten, Eugenio Chacarra"
        },
        "home": {
            "tonight": "Sabato in evidenza",
            "tonightBlurb": "I Commanders battono i Giants 24-21 con TD da 32 yard di Diggs a 57 secondi. Gli Spurs travolgono i Warriors 123-85 (Castle 32). Finale di Stoccolma oggi: Fritz vs Tirante. Dubai R2: McIlroy e Hatton a 139. Domenica: Spagna-Inghilterra a Madrid; Patriots-Lions a Monaco non pubblicati.",
            "plTitle": "Inghilterra 2-1 Croazia e Barcellona 1-1 Arsenal; domenica Spagna vs Inghilterra a Madrid",
            "plBlurb": "L'Arsenal guida ancora la PL a 27 (Brighton 22, Man City 21, Liverpool 18). Giovedi: rigore di Kane alla 126a; Maanum e Hansen 1-1 in UWCL. Domenica 19:45 GMT: Spagna-Inghilterra.",
            "f1Title": "Cinque giorni a Las Vegas (Round 21): 33 punti tra Verstappen (279) e Norris (246)",
            "f1Blurb": "Mercedes (652) e Antonelli (390) restano campioni verso i 6,201 km dello Strip (19-21 nov) davanti a Ferrari (510), Red Bull (415) e McLaren (398). Nessun risultato di gara."
        },
        "pg": {
            "pinFinal": "Finale Stoccolma oggi: Fritz vs Tirante. Ven SF: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). Torino domenica: Zverev vs Jodar.",
            "week1Closed": "NFL Week 10 TNF: Commanders 24, Giants 21 al MetLife (TD da 32 yard di Diggs a 0:57).",
            "week1Sub": "Daniels 23/33, 249 yds, 3 TD; Douglas INT. WSH 3-5-1, NYG 5-3-1. Sabato vuoto. Domenica Monaco: Patriots vs Lions 9:30 ET FOX.",
            "countdownTnf": "TNF CHIUSO: Commanders 24-21 Giants. Sabato 14 nov senza NFL. Prossimo: Patriots vs Lions a Monaco, domenica 9:30 ET FOX.",
            "gridAfterMadrid": "Piloti e Costruttori verso Round 21 · Las Vegas Strip (19-21 nov)",
            "barsPoints": "Antonelli (390) e Mercedes (652) campioni; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Pausa Premier League (J10): Arsenal 27 pts, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Scegli un club. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea ed Everton 16.",
            "plFootnote": "Gio: Barcellona 1-1 Arsenal (Maanum 22, Hansen 59); Inghilterra 2-1 Croazia (Kane 64 rig., 126a). Domenica: Spagna-Inghilterra 19:45 GMT.",
            "majorsDone": "Dubai R2 (AP): McIlroy e Hatton -5 (139), Luiten e Reitan -4 (140), Chacarra -1 (143, T11). R3 sabato non pubblicata."
        }
    },
    "pl": {
        "common": {
            "todayDesk": "Sobota: Commanders 24:21 Giants (Diggs przy 0:57). Spurs 123:85 Warriors (Castle 32). Final w Sztokholmie dzis Fritz vs Tirante. Dubaj R2: McIlroy i Hatton 139.",
            "todayNfl": "TNF zakonczony: Commanders 24, Giants 21. Daniels 3 TD, Diggs, Douglas INT. WSH 3-5-1, NYG 5-3-1. W sobote bez NFL. Niedziela Monachium: Patriots vs Lions, 9:30 ET FOX.",
            "todayTnf": "NFL 10. tydzien TNF: Commanders 24:21 Giants na MetLife. Sobota wolna. Nastepnie: Patriots vs Lions w Monachium, niedziela 9:30 ET FOX."
        },
        "football": {
            "tagline": "TNF: Diggs z 32 jardow przy 0:57, Commanders 24:21 Giants. W sobote bez NFL.",
            "liveNow": "FINAL czw: Commanders 24, Giants 21 (Daniels 3 TD, Diggs, Douglas INT). WSH 3-5-1, NYG 5-3-1. Niedziela Monachium: Patriots vs Lions, 9:30 ET FOX.",
            "pulse": "NFL TNF: COMMANDERS 24:21 GIANTS PO TD DIGGSA PRZY 0:57; SOBOTA WOLNA, NIEDZIELA MONACHIUM",
            "keywords": "NFL tydzien 10, Commanders, Giants, Jayden Daniels, Stefon Diggs, TNF"
        },
        "basketball": {
            "tagline": "Spurs 123:85 Warriors, 11. zwyciestwo z rzedu; Castle 32. Czwartek: Cunningham 52 w 2OT.",
            "liveNow": "Pt: Spurs 123, Warriors 85 (Castle 32, Wemby 12/12/6). Czw: Pistons 144:140 2OT Wizards (Cunningham 52). Dzis: 5 meczow NBA do rozegrania.",
            "pulse": "NBA: SPURS 11. Z RZEDU 123:85, CASTLE 32; CUNNINGHAM 52 W CZWARTEK W PODWOJNEJ DOGRYWCE",
            "keywords": "NBA, Spurs, Warriors, Stephon Castle, Wembanyama, Cade Cunningham"
        },
        "soccer": {
            "tagline": "Karny Kane'a: Anglia 2:1 przy 126. wystepie; Arsenal 1:1 z Barcelona. Niedziela: Hiszpania vs Anglia.",
            "liveNow": "Czwartek: Anglia 2:1 Chorwacja (Rogers 24, Kane 64 karny); Wlochy 3:1 Francja; Czechy 0:2 Hiszpania; Barcelona 1:1 Arsenal. Niedziela 19:45 GMT: Hiszpania-Anglia w Madrycie.",
            "pulse": "ANGLIA 2:1 CHORWACJA I BARCELONA 1:1 ARSENAL; NIEDZIELA HISZPANIA VS ANGLIA W MADRYCIE",
            "keywords": "UWCL, Barcelona, Arsenal, Liga Narodow, Harry Kane, Anglia, Chorwacja, Hiszpania"
        },
        "tennis": {
            "tagline": "Final w Sztokholmie dzis: Fritz vs Tirante po 6:4, 6:2 w SF. Turyn startuje w niedziele: Zverev vs Jodar.",
            "liveNow": "Final dzis: Fritz vs Tirante (przed nami). Pt SF: Fritz d Musetti 6:4, 6:2; Tirante d Tabilo 7:5, 7:6 (1). QF: Fritz walkower Rune. Turyn niedziela.",
            "pulse": "FINAL W SZTOKHOLMIE DZIS FRITZ VS TIRANTE; TURYN W NIEDZIELE ZVEREV VS JODAR",
            "keywords": "Sztokholm, Taylor Fritz, Thiago Agustin Tirante, Nitto ATP Finals, Turyn, Zverev"
        },
        "f1": {
            "tagline": "Piec dni do rundy 21 w Las Vegas: 33 punkty nadal dziela Verstappena i Norrisa. Bez wyscigu na Strip.",
            "liveNow": "Walka o P2 bez zmian: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Runda 21: 19-21 lis.",
            "pulse": "PIEC DNI DO LAS VEGAS: VERSTAPPEN DO NORRISA NADAL 33 PKT ZA MISTRZEM ANTONELLIM",
            "keywords": "Formula 1, runda 21, Las Vegas GP, Verstappen, Norris, Antonelli, Mercedes"
        },
        "golf": {
            "tagline": "Dubaj R2 zakonczona: McIlroy i Hatton dziela 139 (-5). R3 w sobote nie publikowana jako final.",
            "liveNow": "R2 AP: T1 McIlroy 69-70=139, Hatton 70-69=139; T3 Luiten 140, Reitan 140; Chacarra 143 (T11). R3 w toku, nie publikowana.",
            "pulse": "DUBAJ R2: MCILROY I HATTON DZIELA 139; LUITEN 140; R3 NIE PUBLIKOWANA JAKO FINAL",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Tyrrell Hatton, Joost Luiten, Eugenio Chacarra"
        },
        "home": {
            "tonight": "Sobotni pulpit",
            "tonightBlurb": "Commanders wygrywaja 24:21 z Giants po TD Diggsa z 32 jardow przy 57 sekundach. Spurs rozbijaja Warriors 123:85 (Castle 32). Final w Sztokholmie dzis: Fritz vs Tirante. Dubaj R2: McIlroy i Hatton 139. Niedziela: Hiszpania-Anglia w Madrycie; Patriots-Lions w Monachium niepublikowane.",
            "plTitle": "Anglia 2:1 Chorwacja i Barcelona 1:1 Arsenal; niedziela Hiszpania vs Anglia w Madrycie",
            "plBlurb": "Arsenal nadal prowadzi w PL z 27 pkt (Brighton 22, Man City 21, Liverpool 18). Czwartek: karny Kane'a przy 126. wystepie; Maanum i Hansen 1:1 w UWCL. Niedziela 19:45 GMT: Hiszpania-Anglia.",
            "f1Title": "Piec dni do Las Vegas (runda 21): 33 punkty miedzy Verstappenem (279) a Norrisem (246)",
            "f1Blurb": "Mercedes (652) i Antonelli (390) pozostaja mistrzami przed torem 6,201 km (19-21 lis) przed Ferrari (510), Red Bullem (415) i McLarenem (398). Bez wyniku wyscigu."
        },
        "pg": {
            "pinFinal": "Final Sztokholm dzis: Fritz vs Tirante. Pt SF: Fritz d Musetti 6:4, 6:2; Tirante d Tabilo 7:5, 7:6 (1). Turyn niedziela: Zverev vs Jodar.",
            "week1Closed": "NFL 10. tydzien TNF: Commanders 24, Giants 21 na MetLife (TD Diggsa z 32 jardow przy 0:57).",
            "week1Sub": "Daniels 23/33, 249 yds, 3 TD; Douglas INT. WSH 3-5-1, NYG 5-3-1. Sobota wolna. Niedziela Monachium: Patriots vs Lions 9:30 ET FOX.",
            "countdownTnf": "TNF ZAKONCZONY: Commanders 24:21 Giants. Sobota 14 lis bez NFL. Nastepnie: Patriots vs Lions w Monachium, niedziela 9:30 ET FOX.",
            "gridAfterMadrid": "Kierowcy i konstruktorzy przed runda 21 · Las Vegas Strip (19-21 lis)",
            "barsPoints": "Antonelli (390) i Mercedes (652) mistrzowie; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Przerwa Premier League (K10): Arsenal 27 pkt, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Wybierz klub. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea i Everton 16.",
            "plFootnote": "Czw: Barcelona 1:1 Arsenal (Maanum 22, Hansen 59); Anglia 2:1 Chorwacja (Kane 64 karny, 126. wystep). Niedziela: Hiszpania-Anglia 19:45 GMT.",
            "majorsDone": "Dubaj R2 (AP): McIlroy i Hatton -5 (139), Luiten i Reitan -4 (140), Chacarra -1 (143, T11). R3 sobota niepublikowana."
        }
    },
    "zh": {
        "common": {
            "todayDesk": "周六要闻：指挥官24-21胜巨人（迪格斯0:57达阵）。马刺123-85勇士（卡斯尔32分）。斯德哥尔摩决赛今日弗里茨对蒂兰特。迪拜第二轮麦克罗伊与哈顿139杆并列。",
            "todayNfl": "TNF完场：指挥官24，巨人21。丹尼尔斯3次达阵，迪格斯制胜，道格拉斯抄截。华盛顿3-5-1，纽约5-3-1。周六无NFL。周日慕尼黑：爱国者对雄狮，美东9:30 FOX。",
            "todayTnf": "NFL第10周TNF：指挥官24-21巨人。周六轮空。下一场：周日慕尼黑爱国者对雄狮，美东9:30 FOX。"
        },
        "football": {
            "tagline": "TNF：迪格斯在剩余0:57时32码达阵，指挥官24-21击败巨人。周六无NFL。",
            "liveNow": "周四完场：指挥官24，巨人21（丹尼尔斯3达阵，迪格斯制胜，道格拉斯抄截）。华盛顿3-5-1，纽约5-3-1。周日慕尼黑：爱国者对雄狮，美东9:30 FOX。",
            "pulse": "NFL TNF：指挥官24-21巨人，迪格斯0:57达阵；周六轮空，周日慕尼黑开球",
            "keywords": "NFL第10周, 指挥官, 巨人, 丹尼尔斯, 迪格斯, TNF"
        },
        "basketball": {
            "tagline": "马刺123-85勇士拿下11连胜，卡斯尔32分。周四：坎宁安52分两加时。",
            "liveNow": "周五：马刺123，勇士85（卡斯尔32分，文班12/12/6）。周四：活塞144-140两加时奇才（坎宁安52分）。今晚5场NBA待赛。",
            "pulse": "NBA：马刺11连胜123-85，卡斯尔32分；周四坎宁安52分两加时",
            "keywords": "NBA, 马刺, 勇士, 卡斯尔, 文班亚马, 坎宁安"
        },
        "soccer": {
            "tagline": "凯恩点球第126场为英格兰2-1取胜；阿森纳女足诺坎普1-1巴萨。周日：西班牙对英格兰。",
            "liveNow": "周四完场：英格兰2-1克罗地亚（罗杰斯24，凯恩64点球）；意大利3-1法国；捷克0-2西班牙；巴萨1-1阿森纳。周日19:45 GMT：马德里西班牙对英格兰。",
            "pulse": "英格兰2-1克罗地亚、巴萨1-1阿森纳；周日马德里西班牙对英格兰",
            "keywords": "女足欧冠, 巴塞罗那, 阿森纳, 欧国联, 哈里凯恩, 英格兰, 克罗地亚, 西班牙"
        },
        "tennis": {
            "tagline": "斯德哥尔摩决赛今日：弗里茨对蒂兰特（半决赛6-4、6-2）。都灵周日揭幕兹维列夫对霍达尔。",
            "liveNow": "今日决赛：弗里茨对蒂兰特（未赛）。周五半决赛：弗里茨6-4、6-2穆塞蒂；蒂兰特7-5、7-6(1)塔比洛。四分之一：弗里茨轮空鲁内。都灵周日开赛。",
            "pulse": "斯德哥尔摩决赛今日弗里茨对蒂兰特；都灵周日揭幕兹维列夫对霍达尔",
            "keywords": "斯德哥尔摩公开赛, 弗里茨, 蒂兰特, ATP年终总决赛, 都灵, 兹维列夫"
        },
        "f1": {
            "tagline": "距拉斯维加斯第21站还剩五天：维斯塔潘到诺里斯仍差33分。大道赛道尚未开跑。",
            "liveNow": "第二名争夺未变：维斯塔潘279，拉塞尔262，汉密尔顿261，勒克莱尔249，诺里斯246（安东内利390；梅赛德斯652）。第21站：11月19-21日。",
            "pulse": "拉斯维加斯倒计时五天：维斯塔潘至诺里斯仍落后冠军安东内利33分",
            "keywords": "F1, 第21站, 拉斯维加斯大奖赛, 维斯塔潘, 诺里斯, 安东内利, 梅赛德斯"
        },
        "golf": {
            "tagline": "迪拜第二轮收杆：麦克罗伊与哈顿并列139杆（-5）。周六第三轮不作为完场发布。",
            "liveNow": "第二轮美联社：并列第一麦克罗伊69-70=139、哈顿70-69=139；并列第三吕腾140、雷坦140；查卡拉143（并列11）。第三轮进行中未完场。",
            "pulse": "迪拜第二轮：麦克罗伊与哈顿并列139；吕腾140；第三轮不作为完场",
            "keywords": "高尔夫, 迪拜DP世界巡回赛锦标赛, 麦克罗伊, 哈顿, 吕腾, 查卡拉"
        },
        "home": {
            "tonight": "周六要闻",
            "tonightBlurb": "指挥官靠迪格斯剩余57秒32码达阵24-21击败巨人。马刺123-85横扫勇士（卡斯尔32分）。斯德哥尔摩决赛今日弗里茨对蒂兰特。迪拜第二轮麦克罗伊与哈顿并列139杆。周日：马德里西班牙对英格兰；慕尼黑爱国者对雄狮不发布比分。",
            "plTitle": "英格兰2-1克罗地亚、巴萨1-1阿森纳；周日马德里西班牙对英格兰",
            "plBlurb": "阿森纳仍以27分领跑英超（布莱顿22、曼城21、利物浦18）。周四：凯恩第126场点球；马努姆与汉森女足欧冠1-1。周日19:45 GMT：西班牙对英格兰。",
            "f1Title": "拉斯维加斯第21站倒计时五天：维斯塔潘（279分）至诺里斯（246分）仍差33分",
            "f1Blurb": "梅赛德斯（652分）与安东内利（390分）仍为双冠王，即将登陆6.201公里大道赛道（11月19-21日），法拉利510、红牛415、迈凯伦398。尚无比赛成绩。"
        },
        "pg": {
            "pinFinal": "斯德哥尔摩决赛今日：弗里茨对蒂兰特。周五半决赛：弗里茨6-4、6-2穆塞蒂；蒂兰特7-5、7-6(1)塔比洛。都灵周日：兹维列夫对霍达尔。",
            "week1Closed": "NFL第10周TNF：指挥官24，巨人21（迪格斯0:57时32码达阵）。",
            "week1Sub": "丹尼尔斯23/33、249码、3达阵；道格拉斯抄截。华盛顿3-5-1，纽约5-3-1。周六轮空。周日慕尼黑：爱国者对雄狮美东9:30 FOX。",
            "countdownTnf": "TNF完场：指挥官24-21巨人。11月14日周六无NFL。下一场：周日慕尼黑爱国者对雄狮，美东9:30 FOX。",
            "gridAfterMadrid": "车手与车队积分进入第21站 · 拉斯维加斯大道（11月19-21日）",
            "barsPoints": "安东内利（390）与梅赛德斯（652）已封王；维斯塔潘279，拉塞尔262，汉密尔顿261，勒克莱尔249，诺里斯246。",
            "tableAfterMonday": "英超国际比赛日休战（第10轮后）：阿森纳27分，布莱顿22，曼城21，利物浦18，切尔西16。",
            "pinClub": "选择俱乐部。阿森纳27分，布莱顿22，曼城21，利物浦18，切尔西与埃弗顿16。",
            "plFootnote": "周四：巴萨1-1阿森纳（马努姆22，汉森59）；英格兰2-1克罗地亚（凯恩64点球，第126场）。周日：西班牙对英格兰19:45 GMT。",
            "majorsDone": "迪拜第二轮（美联社）：麦克罗伊与哈顿-5（139），吕腾与雷坦-4（140），查卡拉-1（143，并列11）。周六第三轮未完场。"
        }
    },
    "ja": {
        "common": {
            "todayDesk": "土曜デスク：コマンダース24-21ジャイアンツ（ディッグス0:57）。スパーズ123-85ウォリアーズ（キャッスル32点）。ストックホルム決勝は本日フリッツ対ティランテ。ドバイ2日目はマキロイとハットンが139。",
            "todayNfl": "TNF終了：コマンダース24、ジャイアンツ21。ダニエルズ3TD、ディッグス決勝、ダグラスINT。WSH 3-5-1、NYG 5-3-1。土曜はNFLなし。日曜ミュンヘン：ペイトリオッツ対ライオンズ、ET 9:30 FOX。",
            "todayTnf": "NFL第10週TNF：コマンダース24-21ジャイアンツ。土曜は試合なし。次戦：日曜ミュンヘンでペイトリオッツ対ライオンズ、ET 9:30 FOX。"
        },
        "football": {
            "tagline": "TNF：残り0:57でディッグスが32ヤードTD、コマンダースがジャイアンツに24-21。土曜はNFLなし。",
            "liveNow": "木曜終了：コマンダース24、ジャイアンツ21（ダニエルズ3TD、ディッグス、ダグラスINT）。WSH 3-5-1、NYG 5-3-1。日曜ミュンヘン：ペイトリオッツ対ライオンズ、ET 9:30 FOX。",
            "pulse": "NFL TNF：コマンダース24-21ジャイアンツ、ディッグス0:57のTD；土曜休み、日曜ミュンヘン",
            "keywords": "NFL第10週, コマンダース, ジャイアンツ, ジェイデン・ダニエルズ, ステフォン・ディッグス"
        },
        "basketball": {
            "tagline": "スパーズ123-85ウォリアーズで11連勝、キャッスル32点。木曜はカニンガム52点の2OT。",
            "liveNow": "金曜：スパーズ123、ウォリアーズ85（キャッスル32、ウェンビー12/12/6）。木曜：ピストンズ144-140 2OTウィザーズ（カニンガム52）。今夜NBA5試合は未開催。",
            "pulse": "NBA：スパーズ11連勝123-85、キャッスル32点；木曜カニンガム52点のダブルOT",
            "keywords": "NBA, スパーズ, ウォリアーズ, ステフォン・キャッスル, ウェンバンヤマ, カニンガム"
        },
        "soccer": {
            "tagline": "ケインが126キャップ目のPKでイングランド2-1；アーセナルはカンプ・ノウで1-1。日曜はスペイン対イングランド。",
            "liveNow": "木曜：イングランド2-1クロアチア（ロジャース24、ケイン64 PK）；イタリア3-1フランス；チェコ0-2スペイン；バルセロナ1-1アーセナル。日曜19:45 GMT：マドリードでスペイン対イングランド。",
            "pulse": "イングランド2-1クロアチア、バルセロナ1-1アーセナル；日曜マドリードでスペイン対イングランド",
            "keywords": "UWCL, バルセロナ, アーセナル, ネーションズリーグ, ハリー・ケイン, イングランド, クロアチア"
        },
        "tennis": {
            "tagline": "ストックホルム決勝は本日フリッツ対ティランテ（SFは6-4, 6-2）。トリノは日曜にズベレフ対ホダールで開幕。",
            "liveNow": "本日決勝：フリッツ対ティランテ（未開催）。金曜SF：フリッツがムセッティに6-4, 6-2；ティランテがタビロに7-5, 7-6(1)。QFはルーン棄権。トリノは日曜。",
            "pulse": "ストックホルム決勝は本日フリッツ対ティランテ；トリノは日曜ズベレフ対ホダールで開幕",
            "keywords": "ストックホルム・オープン, テイラー・フリッツ, ティランテ, Nitto ATPファイナルズ, トリノ"
        },
        "f1": {
            "tagline": "ラスベガス第21戦まであと5日：フェルスタッペンからノリスまでなお33点差。ストリップ未開催。",
            "liveNow": "2位争いは不変：フェルスタッペン279、ラッセル262、ハミルトン261、ルクレール249、ノリス246（アントネッリ390；メルセデス652）。第21戦は11月19-21日。",
            "pulse": "ラスベガスまで5日：フェルスタッペンからノリスは王者アントネッリの33点差のまま",
            "keywords": "F1, 第21戦, ラスベガスGP, フェルスタッペン, ノリス, アントネッリ, メルセデス"
        },
        "golf": {
            "tagline": "ドバイ2日目終了：マキロイとハットンが139（-5）で首位タイ。土曜3日目は最終結果として未掲載。",
            "liveNow": "R2 AP：T1 マキロイ69-70=139、ハットン70-69=139；T3 ルイテン140、レイタン140；チャカラ143（T11）。R3進行中、最終扱いせず。",
            "pulse": "ドバイ2日目：マキロイとハットンが139；ルイテン140；3日目は最終として非掲載",
            "keywords": "ゴルフ, DPワールドツアー選手権, ローリー・マキロイ, ティレル・ハットン, ルイテン"
        },
        "home": {
            "tonight": "土曜デスク",
            "tonightBlurb": "コマンダースが残り57秒のディッグス32ヤードTDでジャイアンツに24-21。スパーズはキャッスル32点でウォリアーズを123-85。ストックホルム決勝は本日フリッツ対ティランテ。ドバイ2日目はマキロイとハットンが139。日曜はマドリードでスペイン対イングランド、ミュンヘンのNFLは未掲載。",
            "plTitle": "イングランド2-1クロアチア、バルセロナ1-1アーセナル；日曜マドリードでスペイン対イングランド",
            "plBlurb": "アーセナルはPL首位27点（ブライトン22、マンC21、リバプール18）。木曜：ケイン126キャップ目のPK；マーヌムとハンセンがUWCL1-1。日曜19:45 GMT：スペイン対イングランド。",
            "f1Title": "ラスベガス第21戦まで5日：フェルスタッペン（279）からノリス（246）まで33点差",
            "f1Blurb": "メルセデス（652）とアントネッリ（390）は王者のまま6.201kmストリップ（11月19-21日）へ。フェラーリ510、レッドブル415、マクラーレン398。レース結果なし。"
        },
        "pg": {
            "pinFinal": "ストックホルム決勝本日：フリッツ対ティランテ。金曜SF：フリッツ 6-4, 6-2 ムセッティ；ティランテ 7-5, 7-6(1) タビロ。トリノ日曜：ズベレフ対ホダール。",
            "week1Closed": "NFL第10週TNF：コマンダース24、ジャイアンツ21（ディッグス0:57の32ヤードTD）。",
            "week1Sub": "ダニエルズ23/33、249yds、3TD；ダグラスINT。WSH 3-5-1、NYG 5-3-1。土曜休み。日曜ミュンヘン：ペイトリオッツ対ライオンズ ET 9:30 FOX。",
            "countdownTnf": "TNF終了：コマンダース24-21ジャイアンツ。11月14日土曜はNFLなし。次戦：日曜ミュンヘンでペイトリオッツ対ライオンズ、ET 9:30 FOX。",
            "gridAfterMadrid": "ドライバー＆コンストラクター 第21戦へ · ラスベガス・ストリップ（11月19-21日）",
            "barsPoints": "アントネッリ（390）とメルセデス（652）が王者；フェルスタッペン279、ラッセル262、ハミルトン261、ルクレール249、ノリス246。",
            "tableAfterMonday": "プレミア休戦（第10節後）：アーセナル27、ブライトン22、マンC21、リバプール18、チェルシー16。",
            "pinClub": "クラブを選択。アーセナル27、ブライトン22、マンC21、リバプール18、チェルシーとエバートン16。",
            "plFootnote": "木曜：バルセロナ1-1アーセナル（マーヌム22、ハンセン59）；イングランド2-1クロアチア（ケイン64 PK、126キャップ）。日曜：スペイン対イングランド 19:45 GMT。",
            "majorsDone": "ドバイ2日目（AP）：マキロイ＆ハットン -5（139）、ルイテン＆レイタン -4（140）、チャカラ -1（143、T11）。土曜R3は未掲載。"
        }
    },
    "ko": {
        "common": {
            "todayDesk": "토요일 데스크: 커맨더스 24-21 자이언츠(디그스 0:57). 스퍼스 123-85 워리어스(캐슬 32점). 스톡홀름 결승은 오늘 프리츠 vs 티란테. 두바이 2R 매킬로이·해튼 139타.",
            "todayNfl": "TNF 종료: 커맨더스 24, 자이언츠 21. 대니얼스 3TD, 디그스 결승, 더글러스 INT. WSH 3-5-1, NYG 5-3-1. 토요일 NFL 없음. 일요일 뮌헨: 패트리어츠 vs 라이온스, ET 9:30 FOX.",
            "todayTnf": "NFL 10주차 TNF: 커맨더스 24-21 자이언츠. 토요일 휴장. 다음: 일요일 뮌헨 패트리어츠 vs 라이온스, ET 9:30 FOX."
        },
        "football": {
            "tagline": "TNF: 디그스가 0:57에 32야드 TD, 커맨더스가 자이언츠를 24-21로 제압. 토요일 NFL 없음.",
            "liveNow": "목요일 종료: 커맨더스 24, 자이언츠 21(대니얼스 3TD, 디그스, 더글러스 INT). WSH 3-5-1, NYG 5-3-1. 일요일 뮌헨: 패트리어츠 vs 라이온스, ET 9:30 FOX.",
            "pulse": "NFL TNF: 커맨더스 24-21 자이언츠, 디그스 0:57 TD; 토요일 휴장, 일요일 뮌헨",
            "keywords": "NFL 10주차, 커맨더스, 자이언츠, 제이든 대니얼스, 스테폰 디그스"
        },
        "basketball": {
            "tagline": "스퍼스 123-85 워리어스로 11연승, 캐슬 32점. 목요일 커닝햄 52점 2OT.",
            "liveNow": "금요일: 스퍼스 123, 워리어스 85(캐슬 32, 웸비 12/12/6). 목요일: 피스톤스 144-140 2OT 위저즈(커닝햄 52). 오늘 밤 NBA 5경기 예정.",
            "pulse": "NBA: 스퍼스 11연승 123-85, 캐슬 32점; 목요일 커닝햄 52점 더블OT",
            "keywords": "NBA, 스퍼스, 워리어스, 스테폰 캐슬, 웸반야마, 케이드 커닝햄"
        },
        "soccer": {
            "tagline": "케인이 126번째 출전 PK로 잉글랜드 2-1; 아스널이 캄프 누에서 1-1. 일요일 스페인 vs 잉글랜드.",
            "liveNow": "목요일: 잉글랜드 2-1 크로아티아(로저스 24, 케인 64 PK); 이탈리아 3-1 프랑스; 체코 0-2 스페인; 바르셀로나 1-1 아스널. 일요일 19:45 GMT 마드리드 스페인-잉글랜드.",
            "pulse": "잉글랜드 2-1 크로아티아, 바르셀로나 1-1 아스널; 일요일 마드리드 스페인 vs 잉글랜드",
            "keywords": "UWCL, 바르셀로나, 아스널, 네이션스리그, 해리 케인, 잉글랜드, 크로아티아"
        },
        "tennis": {
            "tagline": "스톡홀름 결승 오늘: 프리츠 vs 티란테(SF 6-4, 6-2). 토리노는 일요일 츠베레프 vs 호다르로 개막.",
            "liveNow": "오늘 결승: 프리츠 vs 티란테(예정). 금 SF: 프리츠 d 무세티 6-4, 6-2; 티란테 d 타빌로 7-5, 7-6(1). QF: 프리츠 기권승 루네. 토리노 일요일.",
            "pulse": "스톡홀름 결승 오늘 프리츠 vs 티란테; 토리노 일요일 츠베레프 vs 호다르 개막",
            "keywords": "스톡홀름 오픈, 테일러 프리츠, 티란테, 니토 ATP 파이널스, 토리노"
        },
        "f1": {
            "tagline": "라스베이거스 21라운드까지 5일: 베르스타펜부터 노리스까지 여전히 33점 차. 스트립 경기는 아직 없음.",
            "liveNow": "2위 싸움 변동 없음: 베르스타펜 279, 러셀 262, 해밀턴 261, 르클레르 249, 노리스 246(안토넬리 390; 메르세데스 652). 21라운드 11월 19-21일.",
            "pulse": "라스베이거스 D-5: 베르스타펜부터 노리스까지 챔피언 안토넬리와 33점 차 유지",
            "keywords": "F1, 21라운드, 라스베이거스 GP, 베르스타펜, 노리스, 안토넬리, 메르세데스"
        },
        "golf": {
            "tagline": "두바이 2R 종료: 매킬로이와 해튼이 139타(-5) 공동 선두. 토요일 3R는 최종으로 미게시.",
            "liveNow": "2R AP: T1 매킬로이 69-70=139, 해튼 70-69=139; T3 라위텐 140, 레이탄 140; 차카라 143(T11). 3R 진행 중, 최종 아님.",
            "pulse": "두바이 2R: 매킬로이·해튼 139 공동; 라위텐 140; 3R는 최종으로 미게시",
            "keywords": "골프, DP 월드 투어 챔피언십, 로리 매킬로이, 타렐 해튼, 요스트 라위텐"
        },
        "home": {
            "tonight": "토요일 데스크",
            "tonightBlurb": "커맨더스가 57초 남기고 디그스 32야드 TD로 자이언츠를 24-21로 꺾었습니다. 스퍼스는 캐슬 32점으로 워리어스를 123-85. 스톡홀름 결승은 오늘 프리츠 vs 티란테. 두바이 2R는 매킬로이·해튼 139. 일요일 마드리드 스페인-잉글랜드, 뮌헨 NFL은 미게시.",
            "plTitle": "잉글랜드 2-1 크로아티아, 바르셀로나 1-1 아스널; 일요일 마드리드 스페인 vs 잉글랜드",
            "plBlurb": "아스널이 PL 선두 27점(브라이턴 22, 맨시티 21, 리버풀 18). 목요일: 케인 126번째 출전 PK; 마누움·한센 UWCL 1-1. 일요일 19:45 GMT 스페인-잉글랜드.",
            "f1Title": "라스베이거스 21라운드 D-5: 베르스타펜(279)부터 노리스(246)까지 33점 차",
            "f1Blurb": "메르세데스(652)와 안토넬리(390)는 챔피언 자격으로 6.201km 스트립(11월 19-21일)에 진입합니다. 페라리 510, 레드불 415, 맥라렌 398. 경기 결과 없음."
        },
        "pg": {
            "pinFinal": "스톡홀름 결승 오늘: 프리츠 vs 티란테. 금 SF: 프리츠 d 무세티 6-4, 6-2; 티란테 d 타빌로 7-5, 7-6(1). 토리노 일요일: 츠베레프 vs 호다르.",
            "week1Closed": "NFL 10주차 TNF: 커맨더스 24, 자이언츠 21(디그스 0:57 32야드 TD).",
            "week1Sub": "대니얼스 23/33, 249yds, 3TD; 더글러스 INT. WSH 3-5-1, NYG 5-3-1. 토요일 휴장. 일요일 뮌헨: 패트리어츠 vs 라이온스 ET 9:30 FOX.",
            "countdownTnf": "TNF 종료: 커맨더스 24-21 자이언츠. 11월 14일 토요일 NFL 없음. 다음: 일요일 뮌헨 패트리어츠 vs 라이온스, ET 9:30 FOX.",
            "gridAfterMadrid": "드라이버·컨스트럭터 21라운드 진입 · 라스베이거스 스트립 (11월 19-21일)",
            "barsPoints": "안토넬리(390)와 메르세데스(652) 챔피언; 베르스타펜 279, 러셀 262, 해밀턴 261, 르클레르 249, 노리스 246.",
            "tableAfterMonday": "프리미어리그 휴식(10라운드 후): 아스널 27점, 브라이턴 22, 맨시티 21, 리버풀 18, 첼시 16.",
            "pinClub": "클럽을 선택하세요. 아스널 27, 브라이턴 22, 맨시티 21, 리버풀 18, 첼시와 에버턴 16.",
            "plFootnote": "목: 바르셀로나 1-1 아스널(마누움 22, 한센 59); 잉글랜드 2-1 크로아티아(케인 64 PK, 126캡). 일: 스페인-잉글랜드 19:45 GMT.",
            "majorsDone": "두바이 2R(AP): 매킬로이·해튼 -5(139), 라위텐·레이탄 -4(140), 차카라 -1(143, T11). 토요일 3R 미게시."
        }
    },
    "ar": {
        "common": {
            "todayDesk": "نشرة السبت: كوماندرز 24-21 جاينتس (ديغز عند 0:57). سبرز 123-85 ووريورز (كاسل 32). نهائي ستوكهولم اليوم فريتز ضد تيرانت. دبي الجولة 2: ماكلروي وهاتون 139.",
            "todayNfl": "نهاية TNF: كوماندرز 24، جاينتس 21. دانيالز 3 TD، ديغز الحاسم، دوغلاس اعتراض. واشنطن 3-5-1، نيويورك 5-3-1. لا NFL يوم السبت. الأحد ميونخ: باتريوتس ضد ليونز، 9:30 ET FOX.",
            "todayTnf": "الأسبوع 10 TNF: كوماندرز 24-21 جاينتس في ميتلايف. السبت بلا مباراة. التالي: باتريوتس ضد ليونز في ميونخ الأحد 9:30 ET FOX."
        },
        "football": {
            "tagline": "TNF: ديغز يسجل من 32 ياردة عند 0:57 وكوماندرز يغلبون جاينتس 24-21. لا NFL يوم السبت.",
            "liveNow": "نهائي الخميس: كوماندرز 24، جاينتس 21 (دانيالز 3 TD، ديغز، دوغلاس اعتراض). واشنطن 3-5-1، نيويورك 5-3-1. الأحد ميونخ: باتريوتس ضد ليونز، 9:30 ET FOX.",
            "pulse": "NFL TNF: كوماندرز 24-21 جاينتس بهدف ديغز عند 0:57؛ السبت بلا مباريات والأحد ميونخ",
            "keywords": "NFL الأسبوع 10, كوماندرز, جاينتس, جايادن دانيالز, ستيفون ديغز"
        },
        "basketball": {
            "tagline": "سبرز 123-85 ووريورز للفوز الحادي عشر تواليا؛ كاسل 32. الخميس: كانينغهام 52 في وقتين إضافيين.",
            "liveNow": "الجمعة: سبرز 123، ووريورز 85 (كاسل 32، ويمبي 12/12/6). الخميس: بيستونز 144-140 وقتان إضافيان ويزاردز (كانينغهام 52). الليلة 5 مباريات NBA قادمة.",
            "pulse": "NBA: سبرز فوز 11 تواليا 123-85، كاسل 32؛ كانينغهام 52 الخميس في وقتين إضافيين",
            "keywords": "NBA, سبرز, ووريورز, ستيفون كاسل, ويمبانياما, كيد كانينغهام"
        },
        "soccer": {
            "tagline": "ركلة كين الجزائية في ظهوره 126 تمنح إنجلترا 2-1؛ أرسنال يتعادل 1-1 في كامب نو. الأحد: إسبانيا ضد إنجلترا.",
            "liveNow": "الخميس: إنجلترا 2-1 كرواتيا (روجرز 24، كين 64 جزاء)؛ إيطاليا 3-1 فرنسا؛ التشيك 0-2 إسبانيا؛ برشلونة 1-1 أرسنال. الأحد 19:45 GMT: إسبانيا ضد إنجلترا في مدريد.",
            "pulse": "إنجلترا 2-1 كرواتيا وبرشلونة 1-1 أرسنال؛ الأحد إسبانيا ضد إنجلترا في مدريد",
            "keywords": "دوري أبطال السيدات, برشلونة, أرسنال, دوري الأمم, هاري كين, إنجلترا, كرواتيا"
        },
        "tennis": {
            "tagline": "نهائي ستوكهولم اليوم: فريتز ضد تيرانت بعد 6-4 و6-2 في نصف النهائي. تورينو تفتح الأحد بزفيريف ضد خودار.",
            "liveNow": "النهائي اليوم: فريتز ضد تيرانت (قادم). الجمعة نصف النهائي: فريتز يتفوق على موسيتي 6-4، 6-2؛ تيرانت على تابيلو 7-5، 7-6 (1). ربع النهائي: فريتز بدون لعب أمام رون. تورينو الأحد.",
            "pulse": "نهائي ستوكهولم اليوم فريتز ضد تيرانت؛ تورينو تفتح الأحد زفيريف ضد خودار",
            "keywords": "ستوكهولم, تايلور فريتز, تياغو أغوستين تيرانت, نهائيات ATP, تورينو"
        },
        "f1": {
            "tagline": "خمسة أيام على الجولة 21 في لاس فيغاس: 33 نقطة ما زالت تفصل فيرستابن عن نوريس. لا سباق على الستريب بعد.",
            "liveNow": "سباق المركز الثاني دون تغيير: فيرستابن 279، راسل 262، هاميلتون 261، لوكلير 249، نوريس 246 (أنطونيلي 390؛ مرسيدس 652). الجولة 21: 19-21 نوفمبر.",
            "pulse": "خمسة أيام على لاس فيغاس: فيرستابن حتى نوريس ما زالوا على بعد 33 نقطة من أنطونيلي",
            "keywords": "فورمولا 1, الجولة 21, جائزة لاس فيغاس, فيرستابن, نوريس, أنطونيلي, مرسيدس"
        },
        "golf": {
            "tagline": "دبي الجولة 2 مكتملة: ماكلروي وهاتون يقتسمان 139 (-5). الجولة 3 السبت غير منشورة كنهاية.",
            "liveNow": "الجولة 2 AP: الأول ماكلروي 69-70=139 وهاتون 70-69=139؛ الثالث لويتن 140 وريتان 140؛ تشاكارا 143 (ح11). الجولة 3 جارية وغير نهائية.",
            "pulse": "دبي الجولة 2: ماكلروي وهاتون يقتسمان 139؛ لويتن 140؛ الجولة 3 غير منشورة كنهاية",
            "keywords": "غولف, بطولة جولة DP العالمية, روري ماكلروي, تيريل هاتون, جوست لويتن"
        },
        "home": {
            "tonight": "نشرة السبت",
            "tonightBlurb": "كوماندرز يغلبون جاينتس 24-21 بهدف ديغز من 32 ياردة قبل 57 ثانية. سبرز يسحقون ووريورز 123-85 (كاسل 32). نهائي ستوكهولم اليوم فريتز ضد تيرانت. دبي الجولة 2: ماكلروي وهاتون 139. الأحد: إسبانيا ضد إنجلترا في مدريد؛ باتريوتس ضد ليونز في ميونخ غير منشور.",
            "plTitle": "إنجلترا 2-1 كرواتيا وبرشلونة 1-1 أرسنال؛ الأحد إسبانيا ضد إنجلترا في مدريد",
            "plBlurb": "أرسنال ما زال يتصدر البريميرليغ بـ27 نقطة (برايتون 22، مان سيتي 21، ليفربول 18). الخميس: جزاء كين في ظهوره 126؛ مانوم وهانسن 1-1 في دوري السيدات. الأحد 19:45 GMT: إسبانيا ضد إنجلترا.",
            "f1Title": "خمسة أيام على لاس فيغاس (الجولة 21): 33 نقطة بين فيرستابن (279) ونوريس (246)",
            "f1Blurb": "مرسيدس (652) وأنطونيلي (390) يبقيان بطلين قبل حلبة 6.201 كلم (19-21 نوفمبر) أمام فيراري (510) وريد بول (415) ومكلارين (398). لا نتيجة سباق."
        },
        "pg": {
            "pinFinal": "نهائي ستوكهولم اليوم: فريتز ضد تيرانت. الجمعة نصف النهائي: فريتز يتفوق على موسيتي 6-4، 6-2؛ تيرانت على تابيلو 7-5، 7-6 (1). تورينو الأحد: زفيريف ضد خودار.",
            "week1Closed": "NFL الأسبوع 10 TNF: كوماندرز 24، جاينتس 21 في ميتلايف (ديغز 32 ياردة عند 0:57).",
            "week1Sub": "دانيالز 23/33، 249 ياردة، 3 TD؛ دوغلاس اعتراض. واشنطن 3-5-1، نيويورك 5-3-1. السبت بلا NFL. الأحد ميونخ: باتريوتس ضد ليونز 9:30 ET FOX.",
            "countdownTnf": "نهاية TNF: كوماندرز 24-21 جاينتس. السبت 14 نوفمبر بلا NFL. التالي: باتريوتس ضد ليونز في ميونخ الأحد 9:30 ET FOX.",
            "gridAfterMadrid": "السائقون والصانعون قبل الجولة 21 · لاس فيغاس ستريب (19-21 نوفمبر)",
            "barsPoints": "أنطونيلي (390) ومرسيدس (652) أبطال؛ فيرستابن 279، راسل 262، هاميلتون 261، لوكلير 249، نوريس 246.",
            "tableAfterMonday": "استراحة البريميرليغ (الجولة 10): أرسنال 27، برايتون 22، مان سيتي 21، ليفربول 18، تشيلسي 16.",
            "pinClub": "اختر ناديا. أرسنال 27، برايتون 22، مان سيتي 21، ليفربول 18، تشيلسي وإيفرتون 16.",
            "plFootnote": "الخميس: برشلونة 1-1 أرسنال (مانوم 22، هانسن 59)؛ إنجلترا 2-1 كرواتيا (كين 64 جزاء، الظهور 126). الأحد: إسبانيا ضد إنجلترا 19:45 GMT.",
            "majorsDone": "دبي الجولة 2 (AP): ماكلروي وهاتون -5 (139)، لويتن وريتان -4 (140)، تشاكارا -1 (143، ح11). الجولة 3 السبت غير منشورة."
        }
    },
}


def validate_no_dashes():
    for lang, sections in DATA.items():
        for sec, fields in sections.items():
            for k, val in fields.items():
                s = re.sub(r"https?://\S+", "", val)
                if "\u2014" in s or "--" in s:
                    raise ValueError(f"Disallowed dash in {lang}.{sec}.{k}: {val}")
    print("Validation passed: 0 em-dashes or double-hyphens across all 10 locales.")


def update_section_fields(block, fields, context_label):
    for k, text in fields.items():
        escaped = json.dumps(text, ensure_ascii=False)[1:-1]
        field_pattern = rf'(\b{re.escape(k)}:\s*)"([^"\\]*(?:\\.[^"\\]*)*)"'
        new_block, n = re.subn(field_pattern, lambda m: m.group(1) + f'"{escaped}"', block, count=1)
        if n != 1:
            raise RuntimeError(f"Failed replacing double-quoted field {k} in {context_label} (matches={n})")
        block = new_block
    return block


def update_pg_fields(block, fields, context_label):
    for k, text in fields.items():
        escaped = json.dumps(text, ensure_ascii=False)[1:-1]
        field_pattern = rf'("{re.escape(k)}":\s*)"([^"\\]*(?:\\.[^"\\]*)*)"'
        new_block, n = re.subn(field_pattern, lambda m: m.group(1) + f'"{escaped}"', block, count=1)
        if n != 1:
            raise RuntimeError(f"Failed replacing pg field {k} in {context_label} (matches={n})")
        block = new_block
    return block


def update_messages_dict(content, lang):
    data = DATA[lang]

    c_idx = content.find("common: {")
    assert c_idx != -1, f"common: {{ not found in {lang}"
    c_close = re.search(r"\r?\n  \},", content[c_idx:])
    assert c_close is not None, f"common end not found in {lang}"
    c_end = c_idx + c_close.start()
    c_block = update_section_fields(content[c_idx:c_end], data["common"], f"{lang}.common")
    content = content[:c_idx] + c_block + content[c_end:]

    for sport_name in ["football", "tennis", "f1", "soccer", "basketball", "golf"]:
        s_idx = content.find(f"    {sport_name}: {{")
        if s_idx == -1:
            s_idx = content.find(f"{sport_name}: {{")
        assert s_idx != -1, f"sport {sport_name} not found in {lang}"
        s_end = content.find("},", s_idx)
        assert s_end != -1, f"sport {sport_name} end not found in {lang}"
        s_block = update_section_fields(content[s_idx:s_end], data[sport_name], f"{lang}.sports.{sport_name}")
        content = content[:s_idx] + s_block + content[s_end:]

    h_idx = content.find("  home: {")
    assert h_idx != -1, f"home: {{ not found in {lang}"
    h_close = re.search(r"\r?\n  \}(?:,)?", content[h_idx:])
    assert h_close is not None, f"home end not found in {lang}"
    h_end = h_idx + h_close.start()
    h_block = update_section_fields(content[h_idx:h_end], data["home"], f"{lang}.home")
    content = content[:h_idx] + h_block + content[h_end:]

    return content


if __name__ == "__main__":
    validate_no_dashes()

    pg_file = os.path.join(ROOT, "frontend/src/i18n/playground.ts")
    with open(pg_file, "r", encoding="utf-8") as f:
        pg_content = f.read()

    for lang in ["en", "fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        pattern = rf'("{lang}":\s*\{{)([\s\S]*?)(\r?\n  \}},|\r?\n  \}})'
        match = re.search(pattern, pg_content)
        assert match is not None, f"lang block for {lang} not matched in playground.ts"
        new_block = update_pg_fields(match.group(2), DATA[lang]["pg"], f"playground.{lang}")
        pg_content = pg_content[:match.start(2)] + new_block + pg_content[match.end(2):]

    with open(pg_file, "w", encoding="utf-8") as f:
        f.write(pg_content)
    print("Updated frontend/src/i18n/playground.ts")

    msg_file = os.path.join(ROOT, "frontend/src/i18n/messages.ts")
    with open(msg_file, "r", encoding="utf-8") as f:
        msg_content = f.read()

    fr_pos = msg_content.find("export const fr: Messages = {")
    assert fr_pos != -1
    en_part = update_messages_dict(msg_content[:fr_pos], "en")
    fr_part = update_messages_dict(msg_content[fr_pos:], "fr")
    with open(msg_file, "w", encoding="utf-8") as f:
        f.write(en_part + fr_part)
    print("Updated frontend/src/i18n/messages.ts")

    for lang in ["es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        lang_file = os.path.join(ROOT, f"frontend/src/i18n/messages-{lang}.ts")
        with open(lang_file, "r", encoding="utf-8") as f:
            l_content = f.read()
        l_content = update_messages_dict(l_content, lang)
        with open(lang_file, "w", encoding="utf-8") as f:
            f.write(l_content)
        print(f"Updated {lang_file}")

    print("All 10-locale UI updates for 14 Nov 2026 completed successfully!")
