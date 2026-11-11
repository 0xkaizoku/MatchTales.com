#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update playground.ts, messages.ts, and all messages-*.ts across all 10 locales for 11 November 2026."""
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

DATA = {
    "en": {
        "common": {
            "todayDesk": "Wednesday desk: Paul George scores 36 in Celtics 123-101 rout at Philly. Bayern edge PSG 2-1 before Juventus-Lyon tonight. Musetti & Rune win in Stockholm.",
            "todayNfl": "Week 10 TNF (Thu 8:15 p.m. ET): Commanders (2-5-1) at Giants (5-2-1, McCarthy starts). MNF Final: Bills (7-1) 23, Vikings (6-2) 6 (Cook 107 yds, Wentz 2 INTs).",
            "todayTnf": "NFL Week 10 Thursday: Commanders (2-5-1) at Giants (5-2-1, Vintage White Out), 8:15 p.m. ET on Prime Video. Week 5 meeting finished 27-27 OT."
        },
        "football": {
            "tagline": "NFL Week 10 TNF Tomorrow: Giants (5-2-1) and J.J. McCarthy host Commanders after Week 5 27-27 tie.",
            "liveNow": "Thursday 8:15 p.m. ET (MetLife White Out): Commanders (2-5-1) at Giants (5-2-1). MNF Final: Bills (7-1) 23, Vikings (6-2) 6 (Cook 107 yds, 1 TD).",
            "pulse": "NFL WEEK 10 TNF: GIANTS (5-2-1) HOST COMMANDERS TOMORROW AFTER WEEK 5 27-27 DEADLOCK",
            "keywords": "NFL Week 10, Thursday Night Football, New York Giants, Washington Commanders, J.J. McCarthy, Bills, Vikings"
        },
        "basketball": {
            "tagline": "NBA: Paul George pours in 36 points in Philly return as Celtics rout 76ers 123-101 to seize East No. 1.",
            "liveNow": "Final in Philly: Celtics 123, 76ers 101 (George 36 pts, 6-11 3PT; Tatum 21; Maxey 24, Brown 13). Tonight ESPN: CLE at NYK (7 p.m. ET), GSW at HOU (9:30 p.m. ET).",
            "pulse": "NBA: PAUL GEORGE DROPS 36 IN PHILLY RETURN AS CELTICS TAKE EAST NO. 1 BEFORE TONIGHT ON ESPN",
            "keywords": "NBA, Celtics, 76ers, Paul George, Jayson Tatum, Cavaliers, Knicks, Warriors, Rockets"
        },
        "soccer": {
            "tagline": "UWCL MD4: Bayern win 2-1 at PSG and Real Madrid crush Paris FC 3-0 before Juventus host OL Lyonnes tonight.",
            "liveNow": "Tuesday Finals: PSG 1-2 Bayern (Buhl 40'); Real Madrid 3-0 Paris FC; Hacken 0-0 Chelsea. Tonight: Juventus vs OL Lyonnes (20:00 UTC). Thu: Barcelona vs Arsenal.",
            "pulse": "UWCL MD4: BAYERN EDGE PSG 2-1, JUVENTUS HOST LYON TONIGHT BEFORE BARCELONA VS ARSENAL",
            "keywords": "UWCL, Bayern Munich, PSG, Juventus, OL Lyonnes, Barcelona, Arsenal, Premier League"
        },
        "tennis": {
            "tagline": "Stockholm Open: Musetti 6-1, 6-4 & Rune advance smoothly on eve of Thursday Nitto ATP Finals draw.",
            "liveNow": "Stockholm R16/R32: Musetti def. Samuel 6-1, 6-4; Rune def. Bergs 6-3, 6-4; Humbert def. Vallejo 6-4, 6-3. Turin 8-man draw: Thu 12:00 CET.",
            "pulse": "ATP STOCKHOLM & TURIN DRAW: MUSETTI AND RUNE ADVANCE BEFORE THURSDAY NITTO ATP FINALS DRAW",
            "keywords": "ATP, Stockholm Open, Lorenzo Musetti, Holger Rune, Nitto ATP Finals, Turin"
        },
        "f1": {
            "tagline": "F1 Standings Entering Las Vegas: 33 points cover Verstappen (279) through Norris (246) behind Antonelli.",
            "liveNow": "Drivers P2 Race: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli Champion 390; Mercedes 652). Next: Las Vegas (19-21 Nov).",
            "pulse": "F1 ENTERING LAS VEGAS: FIVE STARS SEPARATED BY 33 POINTS IN BATTLE BEHIND ANTONELLI",
            "keywords": "Formula 1, Las Vegas GP, Max Verstappen, Lando Norris, Kimi Antonelli, Mercedes, Ferrari"
        },
        "golf": {
            "tagline": "DP World Tour Championship: Rory McIlroy and Race leader Eugenio Chacarra pair up Thursday in Dubai.",
            "liveNow": "Dubai R1 Tomorrow (12:40 GST): Chacarra (4,243.79 pts) leads McIlroy (3,709.86) by 533.93 pts for $3M prize. Cabo Final: Blades Brown (-23) wins playoff at 19.",
            "pulse": "DUBAI FINALE: LEADER EUGENIO CHACARRA AND RORY MCILROY TEE OFF TOGETHER THURSDAY",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Eugenio Chacarra, Race to Dubai, Blades Brown"
        },
        "home": {
            "tonight": "Wednesday desk",
            "tonightBlurb": "Paul George scores 36 in Celtics 123-101 rout at Philly before CLE-NYK & GSW-HOU on ESPN. Bayern win 2-1 at PSG before Juventus-Lyon tonight. Giants host Commanders Thu TNF. McIlroy pairs with Chacarra in Dubai. Musetti wins in Stockholm.",
            "plTitle": "UWCL MD4 & PL Break: Bayern beat PSG 2-1 tonight's lead-in; Arsenal lead Brighton by five",
            "plBlurb": "Arsenal enter the break on 27 pts ahead of Brighton (22) and Man City (21). Tonight UWCL: Juventus vs OL Lyonnes (20:00 UTC); Thu: Barcelona vs Arsenal.",
            "f1Title": "Sao Paulo GP & Vegas Chase: 33 points split Verstappen (279) to Norris (246) behind Antonelli",
            "f1Blurb": "Norris won wet Interlagos in 1:35:23.504 as Mercedes sealed Constructors (652). Five drivers chase P2 entering Las Vegas (Ferrari 510, Red Bull 415, McLaren 398)."
        },
        "pg": {
            "pinFinal": "Stockholm Open: Musetti def. Samuel 6-1, 6-4; Rune def. Bergs 6-3, 6-4; Humbert def. Vallejo 6-4, 6-3. Turin Finals draw Thu 12:00 CET.",
            "week1Closed": "NFL Week 9 MNF: Bills (7-1) smother Vikings (6-2) 23-6 in Minneapolis.",
            "week1Sub": "Cook 31 car, 107 yds, 5-yd TD; Allen 234 yds to Latu; Wentz 8-25, 2 INTs. Next: Commanders at Giants Thu TNF.",
            "countdownTnf": "Week 10 TNF Tomorrow (8:15 p.m. ET, Prime Video): Commanders (2-5-1) at Giants (5-2-1).",
            "gridAfterMadrid": "Post-Sao Paulo Drivers & Constructors · Next: Las Vegas Strip (19-21 Nov)",
            "barsPoints": "Antonelli (390) & Mercedes (652) Champions; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Premier League Break (MW10): Arsenal lead 27 pts, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Select a club. Arsenal lead on 27, Brighton 22, Man City 21, Liverpool 18, Chelsea and Everton 16.",
            "plFootnote": "UWCL MD4: PSG 1-2 Bayern, Real Madrid 3-0 Paris FC, Hacken 0-0 Chelsea. Tonight: Juventus vs OL Lyonnes (20:00 UTC).",
            "majorsDone": "DP World Tour Championship (Dubai Thu 12:40 GST): Chacarra (4,243.79) & McIlroy (3,709.86) in final R1 group."
        }
    },
    "fr": {
        "common": {
            "todayDesk": "Bureau du mercredi : Paul George inscrit 36 points, Boston ecarte Philly 123-101. Le Bayern bat le PSG 2-1 avant Juventus-OL Lyonnes ce soir. Musetti et Rune gagnent a Stockholm.",
            "todayNfl": "Semaine 10 TNF (jeudi 20h15 ET) : Commanders (2-5-1) chez les Giants (5-2-1, McCarthy titulaire). MNF : Bills (7-1) 23, Vikings (6-2) 6.",
            "todayTnf": "NFL Semaine 10 jeudi : Commanders (2-5-1) chez les Giants (5-2-1, White Out), 20h15 ET sur Prime Video apres le 27-27 de la Semaine 5."
        },
        "football": {
            "tagline": "NFL Semaine 10 TNF demain : les Giants (5-2-1) et J.J. McCarthy recoivent Washington apres le nul 27-27.",
            "liveNow": "Jeudi 20h15 ET (MetLife White Out) : Commanders (2-5-1) chez Giants (5-2-1). MNF : Bills (7-1) 23, Vikings (6-2) 6 (Cook 107 yds).",
            "pulse": "NFL SEMAINE 10 TNF : LES GIANTS (5-2-1) RECOIVENT LES COMMANDERS DEMAIN APRES LE 27-27",
            "keywords": "NFL Semaine 10, Giants, Commanders, J.J. McCarthy, Bills, Vikings"
        },
        "basketball": {
            "tagline": "NBA : Paul George marque 36 points a Philadelphie, les Celtics dominent les 76ers 123-101 et passent 1ers a l'Est.",
            "liveNow": "Score final : Celtics 123, 76ers 101 (George 36 pts ; Tatum 21 ; Maxey 24). Ce soir sur ESPN : CLE a NYK (19h ET), GSW a HOU (21h30 ET).",
            "pulse": "NBA : PAUL GEORGE INSCRIT 36 POINTS A PHILLY, BOSTON PREND LA TETE DE L'EST AVANT ESPN CE SOIR",
            "keywords": "NBA, Celtics, 76ers, Paul George, Jayson Tatum, Knicks, Warriors"
        },
        "soccer": {
            "tagline": "UWCL J4 : le Bayern gagne 2-1 au PSG et le Real domine Paris FC 3-0 avant Juventus-OL Lyonnes ce soir.",
            "liveNow": "Mardi : PSG 1-2 Bayern (Buhl 40') ; Real 3-0 Paris FC ; Hacken 0-0 Chelsea. Ce soir : Juventus-OL Lyonnes (20h00 UTC). Jeudi : Barcelone-Arsenal.",
            "pulse": "UWCL J4 : LE BAYERN BAT LE PSG 2-1, JUVENTUS RECOIT LYON CE SOIR AVANT BARCELONE-ARSENAL",
            "keywords": "UWCL, Bayern Munich, PSG, Juventus, OL Lyonnes, Barcelone, Arsenal, Premier League"
        },
        "tennis": {
            "tagline": "Open de Stockholm : Musetti (6-1, 6-4) et Rune avancent sans trembler avant le tirage de Turin jeudi.",
            "liveNow": "Stockholm : Musetti bat Samuel 6-1, 6-4 ; Rune bat Bergs 6-3, 6-4 ; Humbert bat Vallejo 6-4, 6-3. Tirage ATP Finals jeudi 12h00 CET.",
            "pulse": "ATP STOCKHOLM & TURIN : MUSETTI ET RUNE BRILLENT AVANT LE TIRAGE DES ATP FINALS JEUDI",
            "keywords": "ATP, Stockholm, Lorenzo Musetti, Holger Rune, Nitto ATP Finals, Turin"
        },
        "f1": {
            "tagline": "F1 avant Las Vegas : 33 points separent Verstappen (279) et Norris (246) derriere le champion Antonelli.",
            "liveNow": "Classement : Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli champion 390 ; Mercedes 652). Prochain GP : Las Vegas.",
            "pulse": "F1 AVANT LAS VEGAS : CINQ PILOTES EN 33 POINTS POUR LA DEUXIEME PLACE",
            "keywords": "Formule 1, GP de Las Vegas, Max Verstappen, Lando Norris, Mercedes, Ferrari"
        },
        "golf": {
            "tagline": "DP World Tour Championship : Rory McIlroy et le leader Eugenio Chacarra jouent ensemble jeudi a Dubai.",
            "liveNow": "Dubai Tour 1 demain (12h40 GST) : Chacarra (4 243,79 pts) mene devant McIlroy (3 709,86) pour 3 M$. Cabo : Blades Brown (-23) gagne a 19 ans.",
            "pulse": "FINALE DE DUBAI : EUGENIO CHACARRA ET RORY MCILROY PARTENT ENSEMBLE JEUDI",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Eugenio Chacarra, Dubai, Blades Brown"
        },
        "home": {
            "tonight": "Bureau du mercredi",
            "tonightBlurb": "Paul George inscrit 36 points face aux 76ers (123-101) avant CLE-NYK et GSW-HOU sur ESPN. Le Bayern bat le PSG 2-1 avant Juventus-Lyon ce soir. Giants-Commanders jeudi. McIlroy face a Chacarra a Dubai.",
            "plTitle": "UWCL J4 & Treve PL : le Bayern gagne au PSG, Arsenal compte cinq points d'avance sur Brighton",
            "plBlurb": "Arsenal mene avec 27 pts devant Brighton (22) et Man City (21). Ce soir en UWCL : Juventus-OL Lyonnes (20h00 UTC) ; jeudi : Barcelone-Arsenal.",
            "f1Title": "Bilan Interlagos & Vegas : 33 points entre Verstappen (279) et Norris (246)",
            "f1Blurb": "Norris a gagne au Bresil en 1:35:23.504 et Mercedes est champion (652). Ferrari (510), Red Bull (415) et McLaren (398) se suivent vers Las Vegas."
        },
        "pg": {
            "pinFinal": "Open de Stockholm : Musetti bat Samuel 6-1, 6-4 ; Rune bat Bergs 6-3, 6-4. Tirage Turin jeudi 12h00 CET.",
            "week1Closed": "NFL Semaine 9 MNF : les Bills (7-1) etouffent les Vikings (6-2) 23-6 a Minneapolis.",
            "week1Sub": "Cook 107 yds, 1 TD ; Allen 234 yds vers Latu ; Wentz 8/25, 2 INT. A suivre : Commanders chez Giants jeudi TNF.",
            "countdownTnf": "Semaine 10 TNF demain (20h15 ET, Prime Video) : Commanders (2-5-1) chez Giants (5-2-1).",
            "gridAfterMadrid": "Classements apres Sao Paulo · Prochain : Las Vegas Strip (19-21 nov)",
            "barsPoints": "Antonelli (390) et Mercedes (652) champions ; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Premier League (treve J10) : Arsenal 27 pts, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Choisissez un club. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea et Everton 16.",
            "plFootnote": "UWCL J4 : PSG 1-2 Bayern, Real 3-0 Paris FC, Hacken 0-0 Chelsea. Ce soir : Juventus-OL Lyonnes (20h00 UTC).",
            "majorsDone": "DP World Tour Championship (Dubai jeudi 12h40 GST) : Chacarra (4 243,79) et McIlroy (3 709,86) associes au 1er tour."
        }
    },
    "es": {
        "common": {
            "todayDesk": "Mesa del miercoles: Paul George anota 36 puntos en la victoria de Celtics 123-101 en Filadelfia. Bayern vence 2-1 al PSG antes de Juventus-Lyon hoy. Musetti y Rune ganan en Estocolmo.",
            "todayNfl": "Semana 10 TNF (jueves 8:15 p.m. ET): Commanders (2-5-1) en Giants (5-2-1, McCarthy titular). MNF: Bills (7-1) 23, Vikings (6-2) 6.",
            "todayTnf": "NFL Semana 10 jueves: Commanders (2-5-1) en Giants (5-2-1, White Out), 8:15 p.m. ET por Prime Video tras el empate 27-27."
        },
        "football": {
            "tagline": "NFL Semana 10 TNF manana: Giants (5-2-1) y J.J. McCarthy reciben a Commanders tras el 27-27 de la Semana 5.",
            "liveNow": "Jueves 8:15 p.m. ET (MetLife White Out): Commanders (2-5-1) en Giants (5-2-1). MNF: Bills (7-1) 23, Vikings (6-2) 6 (Cook 107 yds).",
            "pulse": "NFL SEMANA 10 TNF: GIANTS (5-2-1) RECIBEN A COMMANDERS MANANA TRAS EL EMPATE 27-27",
            "keywords": "NFL Semana 10, Giants, Commanders, J.J. McCarthy, Bills, Vikings"
        },
        "basketball": {
            "tagline": "NBA: Paul George brilla con 36 puntos en Filadelfia y los Celtics vencen 123-101 a 76ers por el liderato del Este.",
            "liveNow": "Final en Filadelfia: Celtics 123, 76ers 101 (George 36 pts; Tatum 21; Maxey 24). Hoy en ESPN: CLE en NYK (7 p.m. ET), GSW en HOU (9:30 p.m. ET).",
            "pulse": "NBA: PAUL GEORGE ANOTA 36 EN SU REGRESO A PHILLY Y BOSTON SUBE AL LIDERATO DEL ESTE",
            "keywords": "NBA, Celtics, 76ers, Paul George, Jayson Tatum, Cavaliers, Knicks"
        },
        "soccer": {
            "tagline": "UWCL J4: el Bayern gana 2-1 al PSG y el Real Madrid vence 3-0 al Paris FC antes de Juventus-Lyon hoy.",
            "liveNow": "Martes: PSG 1-2 Bayern (Buhl 40'); Real Madrid 3-0 Paris FC; Hacken 0-0 Chelsea. Hoy: Juventus-OL Lyonnes (20:00 UTC). Jueves: Barcelona-Arsenal.",
            "pulse": "UWCL J4: BAYERN VENCE AL PSG 2-1, JUVENTUS RECIBE AL LYON HOY ANTES DE BARCELONA VS ARSENAL",
            "keywords": "UWCL, Bayern Munich, PSG, Juventus, OL Lyonnes, Barcelona, Arsenal"
        },
        "tennis": {
            "tagline": "ATP Estocolmo: Musetti (6-1, 6-4) y Rune avanzan con firmeza antes del sorteo de Turin el jueves.",
            "liveNow": "Estocolmo: Musetti a Samuel 6-1, 6-4; Rune a Bergs 6-3, 6-4; Humbert a Vallejo 6-4, 6-3. Sorteo Nitto ATP Finals jueves 12:00 CET.",
            "pulse": "ATP ESTOCOLMO Y TURIN: MUSETTI Y RUNE AVANZAN EN LA VISPERA DEL SORTEO FINAL",
            "keywords": "ATP, Estocolmo, Lorenzo Musetti, Holger Rune, Nitto ATP Finals, Turin"
        },
        "f1": {
            "tagline": "F1 rumbo a Las Vegas: solo 33 puntos separan a Verstappen (279) de Norris (246) tras el campeon Antonelli.",
            "liveNow": "Pilotos: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli campeon 390; Mercedes 652). Proxima: Las Vegas.",
            "pulse": "F1 RUMBO A LAS VEGAS: CINCO PILOTOS EN 33 PUNTOS EN LA LUCHA POR EL SUBCAMPEONATO",
            "keywords": "Formula 1, GP de Las Vegas, Max Verstappen, Lando Norris, Mercedes, Ferrari"
        },
        "golf": {
            "tagline": "DP World Tour Championship: Rory McIlroy y el lider Eugenio Chacarra salen juntos el jueves en Dubai.",
            "liveNow": "Dubai R1 manana (12:40 GST): Chacarra (4.243,79 pts) aventaja en 533,93 a McIlroy (3.709,86). Cabo: Blades Brown (-23) campeon con 19 anos.",
            "pulse": "FINAL DE DUBAI: EUGENIO CHACARRA Y RORY MCILROY COMPARTEN PARTIDO ESTELAR EL JUEVES",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Eugenio Chacarra, Dubai, Blades Brown"
        },
        "home": {
            "tonight": "Mesa del miercoles",
            "tonightBlurb": "Paul George anota 36 en la victoria de Celtics 123-101 antes de CLE-NYK y GSW-HOU en ESPN. Bayern gana 2-1 en Paris previo a Juventus-Lyon. Giants reciben a Commanders el jueves. McIlroy con Chacarra en Dubai.",
            "plTitle": "UWCL J4 y Paron Premier: Bayern asalta Paris; Arsenal lidera con cinco puntos sobre Brighton",
            "plBlurb": "Arsenal manda con 27 pts sobre Brighton (22) y Man City (21). Hoy UWCL: Juventus-OL Lyonnes (20:00 UTC); jueves: Barcelona-Arsenal.",
            "f1Title": "Sao Paulo y Las Vegas: 33 puntos entre Verstappen (279) y Norris (246) tras Antonelli",
            "f1Blurb": "Norris gano en Interlagos en 1:35:23.504 y Mercedes aseguro Constructores (652). Ferrari suma 510, Red Bull 415 y McLaren 398."
        },
        "pg": {
            "pinFinal": "Estocolmo: Musetti a Samuel 6-1, 6-4; Rune a Bergs 6-3, 6-4; Humbert a Vallejo 6-4, 6-3. Sorteo de Turin el jueves.",
            "week1Closed": "NFL Semana 9 MNF: Bills (7-1) frenan a Vikings (6-2) 23-6 en Minneapolis.",
            "week1Sub": "Cook 107 yds, 1 TD; Allen 234 yds con Latu; Wentz 2 INTs. Proximo: Commanders en Giants jueves TNF.",
            "countdownTnf": "Semana 10 TNF manana (8:15 p.m. ET, Prime Video): Commanders (2-5-1) en Giants (5-2-1).",
            "gridAfterMadrid": "Clasificacion tras Sao Paulo · Siguiente: Las Vegas Strip (19-21 nov)",
            "barsPoints": "Antonelli (390) y Mercedes (652) campeones; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Premier League (J10): Arsenal lider 27 pts, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Elige club. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea y Everton 16.",
            "plFootnote": "UWCL J4: PSG 1-2 Bayern, Real Madrid 3-0 Paris FC, Hacken 0-0 Chelsea. Hoy: Juventus vs OL Lyonnes (20:00 UTC).",
            "majorsDone": "DP World Tour Championship (Dubai jueves 12:40 GST): Chacarra (4.243,79) y McIlroy (3.709,86) juntos en R1."
        }
    },
    "de": {
        "common": {
            "todayDesk": "Mittwoch-Desk: Paul George erzielt 36 Punkte bei Bostons 123:101 in Philadelphia. Bayern siegt 2:1 bei PSG vor Juventus-Lyon heute Abend. Musetti und Rune weiter.",
            "todayNfl": "Woche 10 TNF (Do 20:15 ET): Commanders (2-5-1) bei den Giants (5-2-1, McCarthy spielt). MNF: Bills (7-1) schlagen Vikings (6-2) 23:6.",
            "todayTnf": "NFL Woche 10 Donnerstag: Commanders (2-5-1) bei Giants (5-2-1, White Out), 20:15 ET bei Prime Video nach dem 27:27-Remis."
        },
        "football": {
            "tagline": "NFL Woche 10 TNF morgen: Giants (5-2-1) mit J.J. McCarthy empfangen Commanders nach dem 27:27.",
            "liveNow": "Donnerstag 20:15 ET (MetLife White Out): Commanders (2-5-1) bei Giants (5-2-1). MNF: Bills (7-1) 23, Vikings (6-2) 6.",
            "pulse": "NFL WOCHE 10 TNF: GIANTS (5-2-1) EMPFANGEN MORGEN COMMANDERS NACH DEM 27:27-KRIMI",
            "keywords": "NFL Woche 10, Giants, Commanders, J.J. McCarthy, Bills, Vikings"
        },
        "basketball": {
            "tagline": "NBA: Paul George trifft fuer 36 Punkte in Philadelphia, Celtics schlagen 76ers 123:101 fuer Platz 1 im Osten.",
            "liveNow": "Endstand Philly: Celtics 123, 76ers 101 (George 36; Tatum 21; Maxey 24). Heute ESPN: CLE bei NYK, GSW bei HOU.",
            "pulse": "NBA: PAUL GEORGE TRIFFT 36 IN PHILLY, BOSTON UEBERNIMMT OST-SPITZE VOR ESPN HEUTE NACHT",
            "keywords": "NBA, Celtics, 76ers, Paul George, Jayson Tatum, Knicks, Warriors"
        },
        "soccer": {
            "tagline": "UWCL 4. Spieltag: Bayern siegt 2:1 bei PSG und Real Madrid 3:0 gegen Paris FC vor Juventus-Lyon heute.",
            "liveNow": "Dienstag: PSG 1:2 Bayern (Buhl 40.'); Real 3:0 Paris FC; Hacken 0:0 Chelsea. Heute: Juventus-OL Lyonnes (20:00 UTC). Do: Barcelona-Arsenal.",
            "pulse": "UWCL 4. SPIELTAG: BAYERN SIEGT IN PARIS, JUVENTUS HEUTE GEGEN LYON VOR BARCELONA-ARSENAL",
            "keywords": "UWCL, FC Bayern, PSG, Juventus, OL Lyonnes, Barcelona, Arsenal, Premier League"
        },
        "tennis": {
            "tagline": "ATP Stockholm: Musetti (6:1, 6:4) und Rune siegen souveraen einen Tag vor der Turin-Auslosung.",
            "liveNow": "Stockholm: Musetti schlaegt Samuel 6:1, 6:4; Rune schlaegt Bergs 6:3, 6:4; Humbert weiter. ATP-Finals-Auslosung Do 12:00 MEZ.",
            "pulse": "ATP STOCKHOLM & TURIN: MUSETTI UND RUNE WEITER VOR DONNERSTAGS-AUSLOSUNG",
            "keywords": "ATP, Stockholm, Lorenzo Musetti, Holger Rune, Nitto ATP Finals, Turin"
        },
        "f1": {
            "tagline": "Formel 1 vor Las Vegas: 33 Punkte zwischen Verstappen (279) und Norris (246) hinter Champion Antonelli.",
            "liveNow": "Fahrer-WM: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Naechstes Rennen: Las Vegas.",
            "pulse": "FORMEL 1 VOR LAS VEGAS: FUENF STARS INNERHALB VON 33 PUNKTEN HINTER ANTONELLI",
            "keywords": "Formel 1, Las Vegas GP, Max Verstappen, Lando Norris, Mercedes, Ferrari"
        },
        "golf": {
            "tagline": "DP World Tour Championship: Rory McIlroy und Spitzenreiter Eugenio Chacarra spielen Donnerstag gemeinsam in Dubai.",
            "liveNow": "Dubai R1 morgen (12:40 GST): Chacarra (4.243,79 Pkt) vor McIlroy (3.709,86 Pkt) im Kampf um 3 Mio. Dollar. Cabo: Blades Brown (-23) siegt im Stechen.",
            "pulse": "FINALE IN DUBAI: SPITZENREITER CHACARRA UND RORY MCILROY AM DONNERSTAG IM TOP-FLIGHT",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Eugenio Chacarra, Dubai, Blades Brown"
        },
        "home": {
            "tonight": "Mittwoch-Desk",
            "tonightBlurb": "Paul George erzielt 36 Punkte bei Bostons 123:101 vor CLE-NYK und GSW-HOU auf ESPN. Bayern schlaegt PSG 2:1 vor Juventus-Lyon heute. Giants gegen Commanders am Donnerstag. McIlroy startet in Dubai mit Chacarra.",
            "plTitle": "UWCL & PL-Pause: Bayern siegt 2:1 in Paris; Arsenal fuenf Punkte vor Brighton",
            "plBlurb": "Arsenal fuehrt mit 27 Punkten vor Brighton (22) und Man City (21). Heute UWCL: Juventus gegen OL Lyonnes (20:00 UTC); Do: Barcelona-Arsenal.",
            "f1Title": "Sao Paulo & Las Vegas: 33 Punkte trennen Verstappen (279) bis Norris (246)",
            "f1Blurb": "Norris gewann in 1:35:23,504 und Mercedes ist Konstrukteurs-Weltmeister (652). Dahinter: Ferrari 510, Red Bull 415, McLaren 398."
        },
        "pg": {
            "pinFinal": "ATP Stockholm: Musetti schlaegt Samuel 6:1, 6:4; Rune bezwingt Bergs 6:3, 6:4. Turin-Auslosung Do 12:00 MEZ.",
            "week1Closed": "NFL Woche 9 MNF: Bills (7-1) bezwingen Vikings (6-2) in Minneapolis 23:6.",
            "week1Sub": "Cook 107 Yards, 1 TD; Allen 234 Yds zu Latu; Wentz 2 INTs. Naechstes Spiel: Commanders bei Giants (Do TNF).",
            "countdownTnf": "Woche 10 TNF morgen (20:15 ET, Prime Video): Commanders (2-5-1) bei den Giants (5-2-1).",
            "gridAfterMadrid": "WM-Stand nach Sao Paulo · Naechstes Rennen: Las Vegas (19.-21. Nov)",
            "barsPoints": "Antonelli (390) & Mercedes (652) Weltmeister; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Premier League (Pause nach Spieltag 10): Arsenal 27 Pkt, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Klub waehlen. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea und Everton 16.",
            "plFootnote": "UWCL 4. Spieltag: PSG 1:2 Bayern, Real Madrid 3:0 Paris FC, Hacken 0:0 Chelsea. Heute: Juventus vs OL Lyonnes.",
            "majorsDone": "DP World Tour Championship (Dubai Do 12:40 GST): Chacarra (4.243,79) & McIlroy (3.709,86) in Runde 1 gemeinsam."
        }
    },
    "it": {
        "common": {
            "todayDesk": "Scrivania di mercoledi: Paul George segna 36 punti nel 123-101 dei Celtics a Philly. Bayern batte PSG 2-1 prima di Juventus-Lione stasera. Musetti e Rune vincono a Stoccolma.",
            "todayNfl": "Week 10 TNF (gio 20:15 ET): Commanders (2-5-1) dai Giants (5-2-1, gioca McCarthy). MNF: Bills (7-1) 23, Vikings (6-2) 6.",
            "todayTnf": "NFL Week 10 giovedi: Commanders (2-5-1) in casa dei Giants (5-2-1, White Out), 20:15 ET su Prime Video dopo il 27-27."
        },
        "football": {
            "tagline": "NFL Week 10 TNF domani: Giants (5-2-1) con J.J. McCarthy ospitano i Commanders dopo il 27-27.",
            "liveNow": "Giovedi 20:15 ET (MetLife White Out): Commanders (2-5-1) vs Giants (5-2-1). MNF: Bills (7-1) 23, Vikings (6-2) 6.",
            "pulse": "NFL WEEK 10 TNF: I GIANTS (5-2-1) SFIDANO I COMMANDERS DOMANI DOPO IL 27-27",
            "keywords": "NFL Week 10, Giants, Commanders, J.J. McCarthy, Bills, Vikings"
        },
        "basketball": {
            "tagline": "NBA: Paul George firma 36 punti nel ritorno a Philadelphia, Celtics 123-101 sui 76ers e primi a Est.",
            "liveNow": "Finale a Philly: Celtics 123, 76ers 101 (George 36 pt; Tatum 21; Maxey 24). Stasera su ESPN: CLE-NYK, GSW-HOU.",
            "pulse": "NBA: PAUL GEORGE DA 36 PUNTI A PHILLY, BOSTON PRIMA A EST ASPETTANDO ESPN STASERA",
            "keywords": "NBA, Celtics, 76ers, Paul George, Jayson Tatum, Knicks, Warriors"
        },
        "soccer": {
            "tagline": "UWCL 4a giornata: Bayern passa 2-1 a Parigi e Real Madrid batte Paris FC 3-0 prima di Juventus-OL Lyonnes stasera.",
            "liveNow": "Martedi: PSG 1-2 Bayern (Buhl 40'); Real 3-0 Paris FC; Hacken 0-0 Chelsea. Stasera: Juventus-OL Lyonnes (20:00 UTC). Gio: Barcellona-Arsenal.",
            "pulse": "UWCL 4A GIORNATA: BAYERN VINCE A PARIGI, STASERA JUVENTUS-LIONE PRIMA DI BARCELLONA-ARSENAL",
            "keywords": "UWCL, Bayern Monaco, PSG, Juventus, OL Lyonnes, Barcellona, Arsenal"
        },
        "tennis": {
            "tagline": "ATP Stoccolma: Musetti (6-1, 6-4) e Rune avanzano netti alla vigilia del sorteggio ATP Finals di Torino.",
            "liveNow": "Stoccolma: Musetti b. Samuel 6-1, 6-4; Rune b. Bergs 6-3, 6-4; Humbert b. Vallejo 6-4, 6-3. Sorteggio Torino gio 12:00 CET.",
            "pulse": "ATP STOCCOLMA & TORINO: MUSETTI E RUNE AVANTI PRIMA DEL SORTEGGIO DI GIOVEDI",
            "keywords": "ATP, Stoccolma, Lorenzo Musetti, Holger Rune, Nitto ATP Finals, Torino"
        },
        "f1": {
            "tagline": "F1 verso Las Vegas: 33 punti tra Verstappen (279) e Norris (246) alle spalle del campione Antonelli.",
            "liveNow": "Piloti: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli campione 390; Mercedes 652). Prossima: Las Vegas.",
            "pulse": "F1 VERSO LAS VEGAS: CINQUE PILOTI IN 33 PUNTI DIETRO AL CAMPIONE ANTONELLI",
            "keywords": "Formula 1, GP Las Vegas, Max Verstappen, Lando Norris, Mercedes, Ferrari"
        },
        "golf": {
            "tagline": "DP World Tour Championship: Rory McIlroy e il leader Eugenio Chacarra partono insieme giovedi a Dubai.",
            "liveNow": "Dubai R1 domani (12:40 GST): Chacarra (4.243,79 pt) guida su McIlroy (3.709,86). Cabo: Blades Brown (-23) vince ai playoff a 19 anni.",
            "pulse": "FINALE DI DUBAI: CHACARRA E RORY MCILROY NELL'ULTIMO FLIGHT DEL GIOVEDI",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Eugenio Chacarra, Dubai, Blades Brown"
        },
        "home": {
            "tonight": "Scrivania di mercoledi",
            "tonightBlurb": "Paul George segna 36 punti nel 123-101 di Boston prima di CLE-NYK e GSW-HOU su ESPN. Bayern espugna Parigi 2-1 prima di Juventus-Lione stasera. Giovedi TNF Giants-Commanders. McIlroy e Chacarra insieme a Dubai.",
            "plTitle": "UWCL & Sosta Premier: Bayern batte PSG 2-1, Arsenal guida a +5 sul Brighton",
            "plBlurb": "Arsenal davanti a quota 27 su Brighton (22) e Man City (21). Stasera in UWCL: Juventus-OL Lyonnes (20:00 UTC); giovedi: Barcellona-Arsenal.",
            "f1Title": "Interlagos & Las Vegas: cinque stelle in 33 punti da Verstappen (279) a Norris (246)",
            "f1Blurb": "Norris vince in 1:35:23.504 e Mercedes trionfa nei Costruttori (652). Ferrari a 510, Red Bull 415 e McLaren 398 verso il Nevada."
        },
        "pg": {
            "pinFinal": "Stoccolma: Musetti b. Samuel 6-1, 6-4; Rune b. Bergs 6-3, 6-4. Giovedi 12:00 CET il sorteggio di Torino.",
            "week1Closed": "NFL Week 9 MNF: i Bills (7-1) bloccano i Vikings (6-2) 23-6 a Minneapolis.",
            "week1Sub": "Cook 107 yard e 1 TD; Allen 234 yd a Latu; Wentz 2 INT. Prossima: Commanders dai Giants gio TNF.",
            "countdownTnf": "Week 10 TNF domani (20:15 ET, Prime Video): Commanders (2-5-1) dai Giants (5-2-1).",
            "gridAfterMadrid": "Classifiche post San Paolo · Prossima: Las Vegas Strip (19-21 nov)",
            "barsPoints": "Antonelli (390) e Mercedes (652) campioni; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Premier League (10a): Arsenal 27 pt, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Scegli club. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea ed Everton 16.",
            "plFootnote": "UWCL 4a: PSG 1-2 Bayern, Real 3-0 Paris FC, Hacken 0-0 Chelsea. Stasera: Juventus vs OL Lyonnes (20:00 UTC).",
            "majorsDone": "DP World Tour Championship (Dubai gio 12:40 GST): Chacarra (4.243,79) e McIlroy (3.709,86) nel gruppo finale R1."
        }
    },
    "pl": {
        "common": {
            "todayDesk": "Srodowe biurko: Paul George rzuca 36 punktow dla Celtics w wygranej 123-101 z 76ers. Bayern ogrywa PSG 2-1 przed wieczornym Juventus-Lyon. Musetti i Rune wygrywaja w Sztokholmie.",
            "todayNfl": "Tydzien 10 TNF (czw 20:15 ET): Commanders (2-5-1) u Giants (5-2-1, startuje McCarthy). MNF: Bills (7-1) 23, Vikings (6-2) 6.",
            "todayTnf": "NFL tydzien 10 czwartek: Commanders (2-5-1) u Giants (5-2-1, White Out), 20:15 ET w Prime Video po remisie 27-27."
        },
        "football": {
            "tagline": "NFL tydzien 10 TNF jutro: Giants (5-2-1) z J.J. McCarthym podejmuja Commanders po remisie 27-27.",
            "liveNow": "Czwartek 20:15 ET (MetLife White Out): Commanders (2-5-1) u Giants (5-2-1). MNF: Bills (7-1) 23, Vikings (6-2) 6.",
            "pulse": "NFL TYDZIEN 10 TNF: GIANTS (5-2-1) KONTRA COMMANDERS JUTRO PO REMISIE 27-27",
            "keywords": "NFL tydzien 10, Giants, Commanders, J.J. McCarthy, Bills, Vikings"
        },
        "basketball": {
            "tagline": "NBA: Paul George zdobywa 36 punktow po powrocie do Filadelfii, Celtics gromia 76ers 123-101 i sa pierwsi na Wschodzie.",
            "liveNow": "Wynik koncowy: Celtics 123, 76ers 101 (George 36 pkt; Tatum 21; Maxey 24). Dzis w ESPN: CLE-NYK, GSW-HOU.",
            "pulse": "NBA: PAUL GEORGE RZUCA 36 PKT W PHILLY, CELTICS LIDEREM WSCHODU PRZED MECZAMI W ESPN",
            "keywords": "NBA, Celtics, 76ers, Paul George, Jayson Tatum, Knicks, Warriors"
        },
        "soccer": {
            "tagline": "UWCL 4. kolejka: Bayern wygrywa 2-1 z PSG, Real gromi Paris FC 3-0 przed srodowym meczem Juventus - OL Lyonnes.",
            "liveNow": "Wtorek: PSG 1-2 Bayern (Buhl 40'); Real 3-0 Paris FC; Hacken 0-0 Chelsea. Dzis: Juventus-OL Lyonnes (20:00 UTC). Czw: Barcelona-Arsenal.",
            "pulse": "UWCL 4. KOLEJKA: BAYERN OGRYWA PSG 2-1, DZIS JUVENTUS KONTRA LYON PRZED HITEM BARCELONA-ARSENAL",
            "keywords": "UWCL, Bayern Monachium, PSG, Juventus, OL Lyonnes, Barcelona, Arsenal"
        },
        "tennis": {
            "tagline": "ATP Sztokholm: Musetti (6-1, 6-4) i Rune pewnie awansuja w przeddzien losowania Nitto ATP Finals w Turynie.",
            "liveNow": "Sztokholm: Musetti - Samuel 6-1, 6-4; Rune - Bergs 6-3, 6-4; Humbert - Vallejo 6-4, 6-3. Losowanie Turyn czw 12:00 CET.",
            "pulse": "ATP SZTOKHOLM I TURYN: MUSETTI I RUNE PEWNIE DALEJ PRZED CZWARTKOWYM LOSOWANIEM",
            "keywords": "ATP, Sztokholm, Lorenzo Musetti, Holger Rune, Nitto ATP Finals, Turyn"
        },
        "f1": {
            "tagline": "F1 przed Las Vegas: pieciu kierowcow w 33 punktach za mistrzem Kimi Antonellim.",
            "liveNow": "Kierowcy: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Kolejna runda: Las Vegas.",
            "pulse": "F1 PRZED LAS VEGAS: PIEC GWIAZD W 33 PUNKTACH W WALCE ZA ANTONELLIM",
            "keywords": "Formula 1, Las Vegas GP, Max Verstappen, Lando Norris, Mercedes, Ferrari"
        },
        "golf": {
            "tagline": "DP World Tour Championship: Rory McIlroy i lider Eugenio Chacarra zagraja razem w czwartek w Dubaju.",
            "liveNow": "Dubaj R1 jutro (12:40 GST): Chacarra (4243,79 pkt) wyprzedza McIlroya (3709,86) w grze o 3 mln $. Cabo: 19-letni Blades Brown (-23) wygrywa play-off.",
            "pulse": "FINAL W DUBAJU: CHACARRA I RORY MCILROY RAZEM NA STARCIE W CZWARTEK",
            "keywords": "Golf, DP World Tour Championship, Rory McIlroy, Eugenio Chacarra, Dubaj, Blades Brown"
        },
        "home": {
            "tonight": "Srodowe biurko",
            "tonightBlurb": "Paul George rzuca 36 punktow dla Celtics w wygranej 123-101 przed CLE-NYK i GSW-HOU w ESPN. Bayern wygrywa 2-1 w Paryzu przed Juventus-Lyon. Giants kontra Commanders w czwartek. McIlroy z Chacarra w Dubaju.",
            "plTitle": "UWCL i Przerwa w Premier League: Bayern wygrywa w Paryzu, Arsenal 5 pkt przed Brighton",
            "plBlurb": "Arsenal liderem z 27 pkt przed Brighton (22) i Man City (21). Dzis w UWCL: Juventus-OL Lyonnes (20:00 UTC); czwartek: Barcelona-Arsenal.",
            "f1Title": "Sao Paulo i Las Vegas: 33 punkty dziela Verstappena (279) i Norrisa (246)",
            "f1Blurb": "Norris wygral w 1:35:23.504, a Mercedes zdobyl tytul konstruktorow (652). Ferrari ma 510, Red Bull 415, McLaren 398."
        },
        "pg": {
            "pinFinal": "Sztokholm: Musetti - Samuel 6-1, 6-4; Rune - Bergs 6-3, 6-4. Losowanie Turyn w czwartek o 12:00 CET.",
            "week1Closed": "NFL tydzien 9 MNF: Bills (7-1) pokonuja Vikings (6-2) 23-6 w Minneapolis.",
            "week1Sub": "Cook 107 jardow, 1 TD; Allen 234 jardy do Latu; Wentz 2 INT. Dalej: Commanders u Giants czw TNF.",
            "countdownTnf": "Tydzien 10 TNF jutro (20:15 ET, Prime Video): Commanders (2-5-1) u Giants (5-2-1).",
            "gridAfterMadrid": "Tabela po Sao Paulo · Nastepny wyscig: Las Vegas (19-21 lis)",
            "barsPoints": "Antonelli (390) i Mercedes (652) mistrzami; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Premier League (10. kolejka): Arsenal 27 pkt, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Wybierz klub. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea i Everton 16.",
            "plFootnote": "UWCL 4. kolejka: PSG 1-2 Bayern, Real 3-0 Paris FC, Hacken 0-0 Chelsea. Dzis: Juventus vs OL Lyonnes.",
            "majorsDone": "DP World Tour Championship (Dubaj czw 12:40 GST): Chacarra (4243,79) i McIlroy (3709,86) razem w 1. rundzie."
        }
    },
    "zh": {
        "common": {
            "todayDesk": "周三编辑台：保罗·乔治重返费城砍36分，凯尔特人123-101大胜76人。拜仁客胜大巴黎2-1，今晚尤文迎战里昂。穆塞蒂与鲁内斯德哥尔摩告捷。",
            "todayNfl": "第10周周四夜赛（周四8:15 PM ET）：指挥官（2-5-1）做客巨人（5-2-1，麦卡锡预计首发）。周一夜赛：比尔（7-1）23-6维京人（6-2）。",
            "todayTnf": "NFL第10周周四夜赛：指挥官对阵巨人（白色主题战），Prime Video晚8:15 ET直播，两队第5周曾加时27-27打平。"
        },
        "football": {
            "tagline": "NFL第10周周四夜赛明晨：巨人（5-2-1）与麦卡锡在27-27平局五周后主场再战指挥官。",
            "liveNow": "周四8:15 PM ET：指挥官（2-5-1）客战巨人（5-2-1）。周一夜赛：比尔（7-1）23-6胜维京人（6-2）（库克107码）。",
            "pulse": "NFL第10周TNF：巨人（5-2-1）明晚白色主题夜再战指挥官",
            "keywords": "NFL第10周, 巨人, 指挥官, J.J.麦卡锡, 比尔, 维京人"
        },
        "basketball": {
            "tagline": "NBA：保罗·乔治重返费城狂砍36分，凯尔特人123-101大胜76人升至东部第一。",
            "liveNow": "终场比分：凯尔特人123-101胜76人（乔治36分6记三分；塔图姆21；马克西24）。今晚ESPN直播骑士战尼克斯、勇士战火箭。",
            "pulse": "NBA：保罗·乔治回费城轰36分助绿军登顶东部，今晚ESPN双赛来袭",
            "keywords": "NBA, 凯尔特人, 76人, 保罗·乔治, 塔图姆, 尼克斯, 勇士"
        },
        "soccer": {
            "tagline": "女足欧冠第4轮：拜仁2-1客胜大巴黎、皇马3-0胜巴黎FC，今晚尤文战里昂、周四巴萨对阵阿森纳。",
            "liveNow": "周二战果：大巴黎1-2拜仁（布尔40'）；皇马3-0巴黎FC；赫根0-0切尔西。今晚尤文vs里昂（20:00 UTC），周四巴萨vs阿森纳。",
            "pulse": "女足欧冠：拜仁力克大巴黎，今夜尤文迎战里昂、明日诺坎普焦点战",
            "keywords": "女足欧冠, 拜仁慕尼黑, 巴黎圣日耳曼, 尤文图斯, 里昂, 巴萨, 阿森纳"
        },
        "tennis": {
            "tagline": "ATP斯德哥尔摩：穆塞蒂（6-1, 6-4）携鲁内稳健晋级，周四正午都灵将揭晓年终分组抽签。",
            "liveNow": "斯德哥尔摩：穆塞蒂6-1, 6-4胜萨缪尔；鲁内6-3, 6-4胜贝尔格斯；安贝尔晋级。周四12:00 CET都灵ATP年终抽签。",
            "pulse": "ATP斯德哥尔摩与年终抽签：穆塞蒂、鲁内赢球蓄力，周四都灵揭晓分组",
            "keywords": "ATP, 斯德哥尔摩, 穆塞蒂, 鲁内, ATP年终总决赛, 都灵"
        },
        "f1": {
            "tagline": "F1迈向拉斯维加斯：总冠军安东内利身后，维斯塔潘至诺里斯5人仅差33分。",
            "liveNow": "车手榜：维斯塔潘279，拉塞尔262，汉密尔顿261，勒克莱尔249，诺里斯246（安东内利390；梅赛德斯652）。下站：拉斯维加斯。",
            "pulse": "F1拉斯维加斯前瞻：安东内利加冕后五大车手紧咬33分差距",
            "keywords": "F1, 拉斯维加斯大奖赛, 维斯塔潘, 诺里斯, 梅赛德斯, 法拉利"
        },
        "golf": {
            "tagline": "DP世界巡回锦标赛：麦克罗伊周四迪拜首轮同组榜首查卡拉正面交锋。",
            "liveNow": "迪拜首轮明晨打响（12:40 GST）：查卡拉（4,243.79分）领先麦克罗伊（3,709.86分）争夺300万大奖。卡波：19岁布朗-23延长夺冠。",
            "pulse": "迪拜收官战：查卡拉与麦克罗伊周四最后一组携手出发",
            "keywords": "高尔夫, DP世界巡回锦标赛, 麦克罗伊, 查卡拉, 迪拜, 布莱兹·布朗"
        },
        "home": {
            "tonight": "周三编辑台",
            "tonightBlurb": "保罗·乔治砍36分助凯尔特人123-101大胜，今晚ESPN连播骑士尼克斯、勇士火箭。拜仁2-1胜巴黎后今晚尤文战里昂。巨人周四迎战指挥官。麦克罗伊迪拜同组查卡拉。",
            "plTitle": "女足欧冠与英超休赛期：拜仁2-1擒大巴黎，阿森纳领先布莱顿5分居首",
            "plBlurb": "阿森纳27分领跑布莱顿（22）与曼城（21）。今晚女足欧冠尤文战里昂，周四巴萨主场迎战阿森纳。",
            "f1Title": "桑巴之后赴赌城：维斯塔潘（279）到诺里斯（246）五强分差仅33分",
            "f1Blurb": "诺里斯1:35:23.504称雄雨战，梅赛德斯652分锁定车队冠军；法拉利510、红牛415、迈凯伦398奔赴拉斯维加斯。"
        },
        "pg": {
            "pinFinal": "斯德哥尔摩：穆塞蒂6-1, 6-4胜萨缪尔；鲁内6-3, 6-4胜贝尔格斯。周四12:00 CET都灵年终抽签。",
            "week1Closed": "NFL第9周MNF：比尔（7-1）客场23-6锁死维京人（6-2）。",
            "week1Sub": "库克107码1达阵；阿伦传234码连线拉图；温茨2次抄截。下战：周四夜赛指挥官战巨人。",
            "countdownTnf": "第10周TNF明晚（8:15 PM ET，Prime Video）：指挥官（2-5-1）对阵巨人（5-2-1）。",
            "gridAfterMadrid": "圣保罗后车手与车队积分 · 下站：拉斯维加斯（11月19-21日）",
            "barsPoints": "安东内利（390）与梅赛德斯（652）已夺冠；维斯塔潘279、拉塞尔262、汉密尔顿261、勒克莱尔249、诺里斯246。",
            "tableAfterMonday": "英超第10轮间歇期：阿森纳27分领跑，布莱顿22，曼城21，利物浦18，切尔西16。",
            "pinClub": "选择球队。阿森纳27、布莱顿22、曼城21、利物浦18、切尔西与埃弗顿16。",
            "plFootnote": "女足欧冠第4轮：大巴黎1-2拜仁，皇马3-0巴黎FC，赫根0-0切尔西。今晚尤文vs里昂。",
            "majorsDone": "DP世界巡回锦标赛（周四12:40 GST）：查卡拉（4,243.79）与麦克罗伊（3,709.86）首轮同组。"
        }
    },
    "ja": {
        "common": {
            "todayDesk": "水曜デスク：ポール・ジョージが古巣で36得点、セルティックス123-101快勝。バイエルンがPSGに2-1勝利、今夜ユヴェントス対リヨン。ムゼッティとルーネも勝利。",
            "todayNfl": "第10週TNF（木曜20:15 ET）：コマンダーズ（2-5-1）対ジャイアンツ（5-2-1、マッカーシー先発へ）。MNF：ビルズ（7-1）23-6バイキングス（6-2）。",
            "todayTnf": "NFL第10週木曜：コマンダーズ対ジャイアンツ（ホワイトアウト、Prime Video 20:15 ET）。第5週は延長27-27。"
        },
        "football": {
            "tagline": "NFL第10週TNF明日：地区首位ジャイアンツ（5-2-1）が第5週27-27の再戦へ。",
            "liveNow": "木曜20:15 ET：コマンダーズ（2-5-1）対ジャイアンツ（5-2-1）。MNF：ビルズ（7-1）23-6バイキングス（6-2）。",
            "pulse": "NFL第10週TNF：ジャイアンツ（5-2-1）が明日コマンダーズと再戦",
            "keywords": "NFL第10週, ジャイアンツ, コマンダーズ, マッカーシー, ビルズ, バイキングス"
        },
        "basketball": {
            "tagline": "NBA：ポール・ジョージが古巣フィラデルフィアで36得点、セルティックスが123-101で東首位浮上。",
            "liveNow": "試合終了：セルティックス123-101 76ers（ジョージ36点；テイタム21；マクシー24）。今夜ESPN：CLE対NYK、GSW対HOU。",
            "pulse": "NBA：ジョージ36得点でボストン首位浮上、今夜ESPNで注目2連戦",
            "keywords": "NBA, セルティックス, 76ers, ポール・ジョージ, テイタム, ニックス, ウォリアーズ"
        },
        "soccer": {
            "tagline": "UWCL第4節：バイエルンがPSGを2-1で下しレアルは3-0快勝、今夜ユヴェントス対リヨンへ。",
            "liveNow": "火曜結果：PSG 1-2 バイエルン（ビュール40分）；レアル3-0パリFC；ヘッケン0-0チェルシー。今夜ユヴェントス対リヨン。",
            "pulse": "UWCL第4節：バイエルン敵地で勝利、今夜ユヴェントス対リヨン、明日バルサ対アーセナル",
            "keywords": "UWCL, バイエルン, PSG, ユヴェントス, リヨン, バルセロナ, アーセナル"
        },
        "tennis": {
            "tagline": "ATPストックホルム：ムゼッティ（6-1, 6-4）とルーネが快勝、木曜のトリノ抽選会へ。",
            "liveNow": "ストックホルム：ムゼッティ 6-1, 6-4 サミュエル；ルーネ 6-3, 6-4 ベルグス。木曜12:00 CETにNitto ATPファイナルズ抽選。",
            "pulse": "ATPストックホルム＆トリノ抽選：ムゼッティとルーネ快勝、木曜正午に組合せ決定",
            "keywords": "ATP, ストックホルム, ムゼッティ, ルーネ, ATPファイナルズ, トリノ"
        },
        "f1": {
            "tagline": "F1ラスベガス展望：王者アントネッリの下、フェルスタッペン（279）からノリス（246）まで33点差。",
            "liveNow": "順位：フェルスタッペン279、ラッセル262、ハミルトン261、ルクレール249、ノリス246（アントネッリ390；メルセデス652）。次戦ベガス。",
            "pulse": "F1ラスベガス前哨戦：5人が33点差にひしめく大混戦の2位争い",
            "keywords": "F1, ラスベガスGP, フェルスタッペン, ノリス, メルセデス, フェラーリ"
        },
        "golf": {
            "tagline": "DPワールドツアー選手権：マキロイと首位チャカラが木曜ドバイ第1Rで同組対決。",
            "liveNow": "ドバイ第1R明日（12:40 GST）：チャカラ（4,243.79pt）がマキロイ（3,709.86）を533.93ptリード。カボ：19歳ブラウン（-23）優勝。",
            "pulse": "ドバイ最終戦：チャカラとマキロイが木曜第1R最終組で激突",
            "keywords": "ゴルフ, DPワールドツアー選手権, マキロイ, チャカラ, ドバイ, ブレイズ・ブラウン"
        },
        "home": {
            "tonight": "水曜デスク",
            "tonightBlurb": "ジョージ36得点でセルティックス123-101快勝、今夜ESPNはCLE対NYK・GSW対HOU。バイエルンがPSGを下し今夜ユヴェントス対リヨン。明日TNFジャイアンツ戦。ドバイでマキロイ対チャカラ。",
            "plTitle": "UWCL＆プレミア中断期間：バイエルンがパリ撃破、アーセナルはブライトンに5差首位",
            "plBlurb": "アーセナルが勝ち点27で首位、2位ブライトン（22）、3位マンC（21）。今夜UWCLユヴェントス対OLリヨンヌ、木曜バルサ対アーセナル。",
            "f1Title": "ブラジル後＆ラスベガス：フェルスタッペン（279）からノリス（246）まで33点差",
            "f1Blurb": "ノリスが1:35:23.504で優勝、メルセデスが652点で王座確定。フェラーリ510、レッドブル415、マクラーレン398。"
        },
        "pg": {
            "pinFinal": "ストックホルム：ムゼッティ 6-1, 6-4 サミュエル；ルーネ 6-3, 6-4 ベルグス。木曜トリノ抽選会。",
            "week1Closed": "NFL第9週MNF：ビルズ（7-1）がバイキングス（6-2）を23-6で完封撃破。",
            "week1Sub": "クック107yd 1TD、アレン234yd ラトゥへTD、ウェンツ2INT。次戦は木曜TNFジャイアンツ戦。",
            "countdownTnf": "第10週TNF明日（20:15 ET、Prime Video）：コマンダーズ（2-5-1）対ジャイアンツ（5-2-1）。",
            "gridAfterMadrid": "サンパウロ後のポイント順位 · 次戦：ラスベガス（11/19-21）",
            "barsPoints": "アントネッリ（390）＆メルセデス（652）王者確定。フェルスタッペン279、ラッセル262、ハミルトン261、ルクレール249、ノリス246。",
            "tableAfterMonday": "プレミア第10節：アーセナル27、ブライトン22、マンC21、リヴァプール18、チェルシー16。",
            "pinClub": "クラブを選択。アーセナル27、ブライトン22、マンC21、リヴァプール18、チェルシー＆エヴァートン16。",
            "plFootnote": "UWCL第4節：PSG 1-2 バイエルン、レアル3-0パリFC、ヘッケン0-0チェルシー。今夜ユヴェントス対リヨン。",
            "majorsDone": "DPワールドツアー選手権（木曜12:40 GST）：チャカラ（4,243.79）とマキロイ（3,709.86）が第1R同組。"
        }
    },
    "ko": {
        "common": {
            "todayDesk": "수요일 데스크: 폴 조지 친정 원정 36점 폭발, 보스턴 123-101 완승. 바이에른 파리 2-1 승 이어 오늘 유벤투스-리옹전. 무세티·루네 스톡홀름 승리.",
            "todayNfl": "10주차 TNF(목 20:15 ET): 커맨더스(2-5-1) vs 자이언츠(5-2-1, 맥카시 선발 유력). MNF: 빌스(7-1) 23-6 바이킹스(6-2).",
            "todayTnf": "NFL 10주차 목요 경기: 커맨더스 vs 자이언츠(화이트아웃), Prime Video 8:15 PM ET 중계. 5주차 맞대결 27-27 무승부."
        },
        "football": {
            "tagline": "NFL 10주차 TNF 내일: 1위 자이언츠(5-2-1)와 맥카시, 27-27 무승부 설욕전 출격.",
            "liveNow": "목요일 20:15 ET: 커맨더스(2-5-1) @ 자이언츠(5-2-1). MNF: 빌스(7-1) 23-6 바이킹스(6-2).",
            "pulse": "NFL 10주차 TNF: 자이언츠(5-2-1), 내일 커맨더스와 27-27 무승부 리턴매치",
            "keywords": "NFL 10주차, 자이언츠, 커맨더스, J.J. 맥카시, 빌스, 바이킹스"
        },
        "basketball": {
            "tagline": "NBA: 폴 조지 필라델피아 원정 36점 폭발, 보스턴 76ers 123-101 대파하며 동부 1위.",
            "liveNow": "최종: 보스턴 123-101 필라델피아(조지 36점; 테이텀 21; 맥시 24). 오늘 ESPN: 클리블랜드-뉴욕, 골든스테이트-휴스턴.",
            "pulse": "NBA: 폴 조지 36점 원정 폭격 보스턴 동부 1위 등극… 오늘 밤 ESPN 더블헤더",
            "keywords": "NBA, 셀틱스, 76ers, 폴 조지, 제이슨 테이텀, 닉스, 워리어스"
        },
        "soccer": {
            "tagline": "UWCL 4차전: 바이에른 PSG 2-1 제압·레알 3-0 완승… 오늘 유벤투스 vs OL 리옹.",
            "liveNow": "화요일 결과: PSG 1-2 바이에른(뷜 40분); 레알 3-0 파리FC; 해켄 0-0 첼시. 오늘 유벤투스-리옹; 목 바르셀로나-아스널.",
            "pulse": "UWCL 4차전: 바이에른 원정 승, 오늘 밤 유벤투스-리옹 이어 목요일 캄프 누 빅매치",
            "keywords": "UWCL, 바이에른 뮌헨, PSG, 유벤투스, 리옹, 바르셀로나, 아스널"
        },
        "tennis": {
            "tagline": "ATP 스톡홀름: 무세티(6-1, 6-4)·루네 순항, 목요일 토리노 ATP 파이널스 조 추첨 임박.",
            "liveNow": "스톡홀름: 무세티 2-0 새뮤얼(6-1, 6-4); 루네 2-0 베르흐스(6-3, 6-4). 목 12:00 CET 토리노 조 추첨.",
            "pulse": "ATP 스톡홀름 & 토리노 추첨: 무세티·루네 완승 뒤 목요일 파이널스 조 추첨",
            "keywords": "ATP, 스톡홀름, 무세티, 루네, 니토 ATP 파이널스, 토리노"
        },
        "f1": {
            "tagline": "F1 라스베이거스 전선: 챔피언 안토넬리 뒤 2위~6위 5명 단 33점 차.",
            "liveNow": "순위: 베르스타펀 279, 러셀 262, 해밀턴 261, 르클레르 249, 노리스 246(안토넬리 390; 메르세데스 652). 다음: 라스베이거스.",
            "pulse": "F1 라스베이거스 전망: 다섯 명의 스타가 33점 차로 2위 쟁탈전",
            "keywords": "포뮬러 1, 라스베이거스 GP, 베르스타펀, 노리스, 메르세데스, 페라리"
        },
        "golf": {
            "tagline": "DP 월드투어 챔피언십: 맥길로이, 선두 차카라와 목요일 두바이 1라운드 동반 플레이.",
            "liveNow": "두바이 내일 12:40 GST: 차카라(4,243.79점)가 맥길로이(3,709.86)에 533.93점 차 선두. 카보: 블레이즈 브라운(-23) 우승.",
            "pulse": "두바이 최종전: 선두 차카라와 로리 맥길로이 목요일 마지막 조 동반 출격",
            "keywords": "골프, DP 월드투어 챔피언십, 로리 맥길로이, 에우헤니오 차카라, 두바이"
        },
        "home": {
            "tonight": "수요일 데스크",
            "tonightBlurb": "폴 조지 36점으로 보스턴 123-101 대승(오늘 ESPN CLE-NYK, GSW-HOU). 바이에른 파리 2-1 승리 뒤 오늘 유벤투스-리옹전. 자이언츠 내일 TNF 출격. 맥길로이 두바이서 차카라와 격돌.",
            "plTitle": "UWCL & PL 휴식기: 바이에른 파리 원정 승, 아스널 브라이튼에 승점 5점 앞선 선두",
            "plBlurb": "아스널 승점 27, 브라이튼 22, 맨시티 21. 오늘 UWCL 유벤투스 vs 리옹(20:00 UTC); 목요일 바르셀로나 vs 아스널.",
            "f1Title": "상파울루 이후 라스베이거스: 베르스타펀(279)~노리스(246) 단 33점 차",
            "f1Blurb": "노리스가 1:35:23.504 우승, 메르세데스 컨스트럭터스 제패(652). 페라리 510, 레드불 415, 맥라렌 398."
        },
        "pg": {
            "pinFinal": "스톡홀름: 무세티 6-1, 6-4 새뮤얼; 루네 6-3, 6-4 베르흐스. 목요일 토리노 파이널스 추첨.",
            "week1Closed": "NFL 9주차 MNF: 빌스(7-1), 미니애폴리스서 바이킹스(6-2) 23-6 제압.",
            "week1Sub": "쿡 107야드 1TD; 앨런 234야드 라투 TD; 웬츠 2INT. 다음: 목요일 TNF 자이언츠전.",
            "countdownTnf": "10주차 TNF 내일(8:15 PM ET, Prime Video): 커맨더스(2-5-1) @ 자이언츠(5-2-1).",
            "gridAfterMadrid": "상파울루 이후 포인트 · 다음: 라스베이거스(11/19-21)",
            "barsPoints": "안토넬리(390)·메르세데스(652) 우승 확정; 베르스타펀 279, 러셀 262, 해밀턴 261, 르클레르 249, 노리스 246.",
            "tableAfterMonday": "프리미어리그 10R 휴식기: 아스널 27, 브라이튼 22, 맨시티 21, 리버풀 18, 첼시 16.",
            "pinClub": "구단 선택. 아스널 27, 브라이튼 22, 맨시티 21, 리버풀 18, 첼시·에버튼 16.",
            "plFootnote": "UWCL 4차전: PSG 1-2 바이에른, 레알 3-0 파리FC, 해켄 0-0 첼시. 오늘 유벤투스 vs 리옹.",
            "majorsDone": "DP 월드투어 챔피언십(두바이 목 12:40 GST): 차카라(4,243.79)와 맥길로이(3,709.86) 1R 동반 라운드."
        }
    },
    "ar": {
        "common": {
            "todayDesk": "مكتب الاربعاء: بول جورج يسجل 36 نقطة في اكتساح سلتيكس 123-101. بايرن يهزم باريس 2-1 قبل يوفنتوس وليون الليلة. موسيتي وروني يتاهلان في ستوكهولم.",
            "todayNfl": "الاسبوع 10 الخميس ليلا: كوماندرز (2-5-1) ضد جاينتس (5-2-1، مكارثي مرشح اساسي). الاثنين السابق: بيلز (7-1) 23-6 فايكنغز (6-2).",
            "todayTnf": "NFL الخميس: كوماندرز ضد جاينتس بقمصان بيضاء، الساعة 8:15 مساء بالتوقيت الشرقي على برايم فيديو بعد تعادل 27-27."
        },
        "football": {
            "tagline": "NFL الاسبوع 10 الخميس غدا: جاينتس (5-2-1) ومكارثي يستضيفان كوماندرز بعد تعادل 27-27.",
            "liveNow": "الخميس 8:15 م ET: كوماندرز (2-5-1) عند جاينتس (5-2-1). نتيجة الاثنين: بيلز (7-1) 23، فايكنغز (6-2) 6.",
            "pulse": "NFL الاسبوع 10: جاينتس (5-2-1) يستضيف كوماندرز غدا في موقعة الثار",
            "keywords": "NFL الاسبوع 10، جاينتس، كوماندرز، مكارثي، بيلز، فايكنغز"
        },
        "basketball": {
            "tagline": "NBA: بول جورج يتالق بـ36 نقطة في فيلادلفيا ويقود سلتيكس للفوز 123-101 واعتلاء قمة الشرق.",
            "liveNow": "النهاية: سلتيكس 123، سيكسرز 101 (جورج 36؛ تيتوم 21؛ ماكسي 24). الليلة على ESPN: كليفلاند-نيكس وواريورز-روكتس.",
            "pulse": "NBA: بول جورج يسجل 36 نقطة ضد فيلادلفيا وسلتيكس يتصدر الشرق قبل سهرة ESPN",
            "keywords": "NBA، سلتيكس، سيكسرز، بول جورج، جايسون تيتوم، نيكس، واريورز"
        },
        "soccer": {
            "tagline": "دوري ابطال اوروبا للسيدات الجولة 4: بايرن يهزم باريس 2-1 وريال مدريد 3-0 قبل يوفنتوس وليون الليلة.",
            "liveNow": "الثلاثاء: باريس 1-2 بايرن؛ ريال مدريد 3-0 باريس اف سي؛ هاكن 0-0 تشيلسي. الليلة: يوفنتوس ضد ليون (20:00 UTC).",
            "pulse": "دوري الابطال للسيدات: بايرن يفوز في باريس والليلة يوفنتوس يستضيف ليون قبل برشلونة وارسنال",
            "keywords": "دوري ابطال اوروبا للسيدات، بايرن ميونخ، باريس، يوفنتوس، ليون، برشلونة، ارسنال"
        },
        "tennis": {
            "tagline": "ستوكهولم المفتوحة: موسيتي (6-1، 6-4) وروني يتاهلان بثبات عشية قرعة نهائيات تورينو يوم الخميس.",
            "liveNow": "ستوكهولم: موسيتي على صامويل 6-1، 6-4؛ روني على بيرغز 6-3، 6-4. قرعة نهائيات ATP تورينو الخميس 12:00 CET.",
            "pulse": "تنس ستوكهولم وقرعة تورينو: موسيتي وروني يتاهلان قبل قرعة الخميس",
            "keywords": "تنس، ستوكهولم، لورينزو موسيتي، هولغر روني، نهائيات ATP، تورينو"
        },
        "f1": {
            "tagline": "فورمولا 1 قبل لاس فيغاس: 33 نقطة تفصل فيرستابن (279) عن نوريس (246) خلف البطل انتونيلي.",
            "liveNow": "السائقون: فيرستابن 279، راسل 262، هاميلتون 261، لوكلير 249، نوريس 246 (انتونيلي 390؛ مرسيدس 652). القادم: لاس فيغاس.",
            "pulse": "فورمولا 1 قبل لاس فيغاس: خمسة نجوم ضمن 33 نقطة على الوصافة",
            "keywords": "فورمولا 1، جائزة لاس فيغاس، فيرستابن، نوريس، مرسيدس، فيراري"
        },
        "golf": {
            "tagline": "بطولة جولة دي بي ورلد دبي: ماكلروي يبدأ الخميس بصحبة المتصدر اوجينيو تشاكارا.",
            "liveNow": "دبي غدا (12:40 GST): تشاكارا (4243.79 نقطة) يتقدم على ماكلروي (3709.86) بفارق 533.93. كابو: براون (-23) بطلا.",
            "pulse": "نهائي دبي: تشاكارا وروري ماكلروي في المجموعة الاخيرة للجولة الاولى الخميس",
            "keywords": "غولف، دي بي ورلد دبي، روري ماكلروي، اوجينيو تشاكارا، بليدز براون"
        },
        "home": {
            "tonight": "مكتب الاربعاء",
            "tonightBlurb": "بول جورج يسجل 36 نقطة في فوز بوسطن 123-101 قبل مواجهتي ESPN الليلة. بايرن يهزم باريس 2-1 ويوفنتوس يلاقي ليون. جاينتس امام كوماندرز غدا. ماكلروي وتشاكارا معا في دبي.",
            "plTitle": "دوري الابطال للسيدات والبريميرليغ: بايرن يعبر باريس وارسنال يتصدر بفارق 5 نقاط عن برايتون",
            "plBlurb": "ارسنال يتصدر بـ27 نقطة امام برايتون (22) وسيتي (21). الليلة يوفنتوس ضد ليون؛ غدا برشلونة امام ارسنال.",
            "f1Title": "ساو باولو ولاس فيغاس: 33 نقطة تفصل فيرستابن (279) عن نوريس (246) خلف انتونيلي",
            "f1Blurb": "نوريس توج بزمن 1:35:23.504 ومرسيدس حسمت الصانعين بـ652 نقطة، خلفها فيراري 510 وريد بول 415 ومكلارين 398."
        },
        "pg": {
            "pinFinal": "ستوكهولم: موسيتي يهزم صامويل 6-1، 6-4؛ روني يتغلب على بيرغز 6-3، 6-4. قرعة تورينو الخميس 12:00 CET.",
            "week1Closed": "NFL الاسبوع 9 MNF: بيلز (7-1) يخنق فايكنغز (6-2) 23-6 في مينيابوليس.",
            "week1Sub": "كوك 107 ياردات وTD؛ الن 234 ياردة الى لاتو؛ وينتز اعتراضان. التالي: الخميس امام جاينتس.",
            "countdownTnf": "الاسبوع 10 الخميس غدا (8:15 م ET، Prime Video): كوماندرز (2-5-1) عند جاينتس (5-2-1).",
            "gridAfterMadrid": "الترتيب بعد ساو باولو · التالي: لاس فيغاس (19-21 نوفمبر)",
            "barsPoints": "انتونيلي (390) ومرسيدس (652) بطلان؛ فيرستابن 279، راسل 262، هاميلتون 261، لوكلير 249، نوريس 246.",
            "tableAfterMonday": "البريميرليغ (الجولة 10): ارسنال 27، برايتون 22، سيتي 21، ليفربول 18، تشيلسي 16.",
            "pinClub": "اختر ناديا. ارسنال 27، برايتون 22، سيتي 21، ليفربول 18، تشيلسي وايفرتون 16.",
            "plFootnote": "UWCL الجولة 4: باريس 1-2 بايرن، ريال 3-0 باريس اف سي، هاكن 0-0 تشيلسي. الليلة يوفنتوس ضد ليون.",
            "majorsDone": "بطولة جولة دي بي ورلد دبي (الخميس 12:40 GST): تشاكارا (4243.79) وماكلروي (3709.86) معا في الجولة الاولى."
        }
    }
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

    # Update common.todayDesk / todayNfl / todayTnf
    c_idx = content.find("common: {")
    assert c_idx != -1, f"common: {{ not found in {lang}"
    c_end = content.find("},\n", c_idx)
    assert c_end != -1, f"common end not found in {lang}"
    c_block = update_section_fields(content[c_idx:c_end], data["common"], f"{lang}.common")
    content = content[:c_idx] + c_block + content[c_end:]

    # Update sports.{sport}
    for sport_name in ["football", "tennis", "f1", "soccer", "basketball", "golf"]:
        s_idx = content.find(f"    {sport_name}: {{")
        if s_idx == -1:
            s_idx = content.find(f"{sport_name}: {{")
        assert s_idx != -1, f"sport {sport_name} not found in {lang}"
        s_end = content.find("},", s_idx)
        assert s_end != -1, f"sport {sport_name} end not found in {lang}"
        s_block = update_section_fields(content[s_idx:s_end], data[sport_name], f"{lang}.sports.{sport_name}")
        content = content[:s_idx] + s_block + content[s_end:]

    # Update home.*
    h_idx = content.find("  home: {")
    assert h_idx != -1, f"home: {{ not found in {lang}"
    h_end = content.find("},\n", h_idx)
    # note: home contains strings, first '  },' on its own line closes home block
    h_close = re.search(r"\n  \}(?:,)?", content[h_idx:])
    assert h_close is not None, f"home end not found in {lang}"
    h_end = h_idx + h_close.start()
    h_block = update_section_fields(content[h_idx:h_end], data["home"], f"{lang}.home")
    content = content[:h_idx] + h_block + content[h_end:]

    return content


if __name__ == "__main__":
    validate_no_dashes()

    # 1. playground.ts
    pg_file = os.path.join(ROOT, "frontend/src/i18n/playground.ts")
    with open(pg_file, "r", encoding="utf-8") as f:
        pg_content = f.read()

    for lang in ["en", "fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        pattern = rf'("{lang}":\s*\{{)([\s\S]*?)(\n  \}},|\n  \}})'
        match = re.search(pattern, pg_content)
        assert match is not None, f"lang block for {lang} not matched in playground.ts"
        new_block = update_pg_fields(match.group(2), DATA[lang]["pg"], f"playground.{lang}")
        pg_content = pg_content[:match.start(2)] + new_block + pg_content[match.end(2):]

    with open(pg_file, "w", encoding="utf-8") as f:
        f.write(pg_content)
    print("Updated frontend/src/i18n/playground.ts")

    # 2. messages.ts (en + fr)
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

    # 3. messages-*.ts (es, de, it, pl, zh, ja, ko, ar)
    for lang in ["es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        lang_file = os.path.join(ROOT, f"frontend/src/i18n/messages-{lang}.ts")
        with open(lang_file, "r", encoding="utf-8") as f:
            l_content = f.read()
        l_content = update_messages_dict(l_content, lang)
        with open(lang_file, "w", encoding="utf-8") as f:
            f.write(l_content)
        print(f"Updated {lang_file}")

    print("All 10-locale UI updates for 11 Nov 2026 completed successfully!")

