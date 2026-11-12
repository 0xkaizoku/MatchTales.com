#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update playground.ts, messages.ts, and all messages-*.ts across all 10 locales for 12 November 2026."""
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

DATA = {
    "en": {
        "common": {
            "todayDesk": "Thursday desk: Barcelona host Arsenal at Camp Nou & England face Croatia at Wembley. TNF tonight: Commanders (Daniels cleared) at Giants. Dubai R1: Luiten 67, McIlroy 69.",
            "todayNfl": "TNF Tonight (8:15 p.m. ET, Prime Video): Commanders (2-5-1, Daniels cleared, C Patrick OUT) at Giants (5-2-1, McCarthy active). MNF: Bills 23-6 Vikings.",
            "todayTnf": "NFL Week 10 Tonight: Commanders (2-5-1, Daniels cleared, C Patrick & TE Yankoff OUT) at Giants (5-2-1, Vintage White Out), 8:15 p.m. ET after Week 5's 27-27 tie."
        },
        "football": {
            "tagline": "TNF Tonight (8:15 p.m. ET, Prime Video): Both Jayden Daniels & J.J. McCarthy cleared for Giants White Out vs Commanders.",
            "liveNow": "Tonight 8:15 p.m. ET: Commanders (2-5-1, C Patrick & TE Yankoff OUT, Daniels cleared) at Giants (5-2-1, McCarthy/Nabers/Skattebo active). MNF Final: Bills 23, Vikings 6.",
            "pulse": "NFL TNF TONIGHT: JAYDEN DANIELS & J.J. MCCARTHY CLEARED FOR METLIFE WHITE OUT REMATCH",
            "keywords": "NFL Week 10, Thursday Night Football, New York Giants, Washington Commanders, Jayden Daniels, J.J. McCarthy"
        },
        "basketball": {
            "tagline": "NBA: Harden's 32 leads Cavaliers past Knicks 115-107; Rockets beat Warriors 115-108 as Curry exits Q1 injured.",
            "liveNow": "Wed Finals: Cavaliers 115, Knicks 107 (Harden 32, Brunson 27); Rockets 115, Warriors 108 (Curry Q1 inj., Sengun 19); Celtics 98, Raptors 93 (-22 rally). Tonight: 4 NBA games.",
            "pulse": "NBA: HARDEN DROPS 32 AT MSG, WARRIORS LOSE CURRY EARLY AT HOUSTON & CELTICS RALLY FROM 22",
            "keywords": "NBA, Cavaliers, Knicks, James Harden, Rockets, Warriors, Stephen Curry, Celtics"
        },
        "soccer": {
            "tagline": "UWCL & Nations League Tonight: Barcelona host Arsenal at Camp Nou; England face Croatia at Wembley after OL Lyonnes crushed Juventus 6-0.",
            "liveNow": "Tonight: Barcelona vs Arsenal (18:45 CET Camp Nou); England vs Croatia (19:45 UK), Italy vs France, Czechia vs Spain (20:45 CET). Wed UWCL: Juventus 0-6 OL Lyonnes.",
            "pulse": "TONIGHT: BARCELONA VS ARSENAL AT CAMP NOU & ENGLAND VS CROATIA AFTER LYON 6-0 AT JUVENTUS",
            "keywords": "UWCL, Barcelona, Arsenal, Spotify Camp Nou, England, Croatia, Nations League, OL Lyonnes"
        },
        "tennis": {
            "tagline": "Turin Draw Set: Zverev anchors McEnroe Group & Alcaraz leads Lendl Group; Fritz faces Rune today in Stockholm QF.",
            "liveNow": "Turin: McEnroe = Zverev (1), Shelton (3), Fils (6), Jodar (8); Lendl = Alcaraz (2), Medvedev (4), Cobolli (5), Tiafoe (7). Stockholm Today: Fritz vs Rune QF.",
            "pulse": "NITTO ATP FINALS DRAW SET: ALCARAZ & ZVEREV SPLIT IN TURIN AS FRITZ MEETS RUNE IN STOCKHOLM",
            "keywords": "Nitto ATP Finals, Turin Draw, Carlos Alcaraz, Alexander Zverev, Stockholm Open, Taylor Fritz, Holger Rune"
        },
        "f1": {
            "tagline": "One Week to Round 21 in Las Vegas: Five F1 drivers packed inside 33 points behind Champion Antonelli.",
            "liveNow": "Drivers P2 Race: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli Champion 390; Mercedes 652). Round 21: Las Vegas (19-21 Nov).",
            "pulse": "ROUND 21 VEGAS COUNTDOWN: VERSTAPPEN TO NORRIS SEPARATED BY 33 PTS BEHIND ANTONELLI",
            "keywords": "Formula 1, Round 21, Las Vegas GP, Max Verstappen, Lando Norris, Kimi Antonelli, Mercedes, Ferrari"
        },
        "golf": {
            "tagline": "Dubai R1 Complete: Joost Luiten fires 67 (-5) to lead Jacob Skov Olesen (68) & Rory McIlroy (69, T3).",
            "liveNow": "Dubai R1: 1. Joost Luiten -5 (67); 2. Jacob Skov Olesen -4 (68); T3. Rory McIlroy -3 (69), Perez, De Leo, Schott, Laporta; T28. Eugenio Chacarra E (72).",
            "pulse": "DUBAI R1: LUITEN LEADS ON 67 (-5) WHILE MCILROY OPENS 69 TO GAIN THREE ON CHACARRA",
            "keywords": "Golf, DP World Tour Championship, Joost Luiten, Rory McIlroy, Jacob Skov Olesen, Eugenio Chacarra"
        },
        "home": {
            "tonight": "Thursday desk",
            "tonightBlurb": "Barcelona host Arsenal at Camp Nou alongside England vs Croatia at Wembley after OL Lyonnes crushed Juventus 6-0. Tonight's TNF pairs cleared QBs Jayden Daniels and J.J. McCarthy at MetLife. Luiten leads Dubai with 67 as McIlroy shoots 69; Turin Finals groups drawn; Cavs and Rockets won Wednesday.",
            "plTitle": "Camp Nou Tonight & Nations League: Barcelona vs Arsenal & England vs Croatia after Lyon's 6-0 rout",
            "plBlurb": "Arsenal retain a five-point PL lead (27 to Brighton 22, Man City 21). Tonight: Barcelona vs Arsenal (18:45 CET) & England vs Croatia (19:45 UK), Italy vs France, Czechia vs Spain.",
            "f1Title": "Round 21 Las Vegas Countdown: 33 points split Verstappen (279) to Norris (246) behind Antonelli",
            "f1Blurb": "Mercedes (652) and Antonelli (390) hold both 2026 titles entering Round 21 on the 6.201 km Strip (19-21 Nov), with Ferrari (510), Red Bull (415) and McLaren (398) behind."
        },
        "pg": {
            "pinFinal": "Turin Groups Set: McEnroe (Zverev, Shelton, Fils, Jodar) | Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Stockholm QF Today: Fritz vs Rune.",
            "week1Closed": "NFL Week 9 MNF: Bills (7-1) smother Vikings (6-2) 23-6 in Minneapolis.",
            "week1Sub": "Cook 107 yds, 1 TD; Allen 234 yds to Latu; Wentz 2 INTs. Tonight: Commanders at Giants (both QBs cleared).",
            "countdownTnf": "TONIGHT Week 10 TNF (8:15 p.m. ET, Prime Video): Commanders (Daniels cleared, C Patrick OUT) at Giants (McCarthy active).",
            "gridAfterMadrid": "Drivers & Constructors Entering Round 21 · Las Vegas Strip (19-21 Nov)",
            "barsPoints": "Antonelli (390) & Mercedes (652) Champions; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Premier League Break (MW10): Arsenal lead 27 pts, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Select a club. Arsenal lead on 27, Brighton 22, Man City 21, Liverpool 18, Chelsea and Everton 16.",
            "plFootnote": "Wed UWCL: Juventus 0-6 OL Lyonnes (Katoto 2); OH Leuven 1-1 HB Koge. Tonight: Barcelona vs Arsenal & England vs Croatia.",
            "majorsDone": "Dubai R1 Complete: Joost Luiten -5 (67), Jacob Skov Olesen -4 (68), Rory McIlroy -3 (69, T3), Eugenio Chacarra E (72, T28)."
        }
    },
    "fr": {
        "common": {
            "todayDesk": "Bureau du jeudi : Barcelone recoit Arsenal au Camp Nou et l'Angleterre affronte la Croatie a Wembley. TNF ce soir : Commanders chez les Giants. Dubai T1 : Luiten 67, McIlroy 69.",
            "todayNfl": "TNF ce soir (20h15 ET, Prime Video) : Commanders (2-5-1, Daniels apte, C Patrick forfait) chez les Giants (5-2-1, McCarthy apte). MNF : Bills 23-6 Vikings.",
            "todayTnf": "NFL Semaine 10 ce soir : Commanders (2-5-1, Daniels apte, Patrick & Yankoff forfaits) chez les Giants (5-2-1, White Out) a 20h15 ET apres le 27-27."
        },
        "football": {
            "tagline": "TNF ce soir (20h15 ET) : Jayden Daniels et J.J. McCarthy tous deux aptes pour le White Out Giants-Commanders.",
            "liveNow": "Ce soir 20h15 ET : Commanders (Daniels apte, C Patrick forfait) chez Giants (McCarthy/Nabers/Skattebo actifs). MNF : Bills 23, Vikings 6.",
            "pulse": "NFL TNF CE SOIR : JAYDEN DANIELS ET J.J. MCCARTHY APTES POUR LE WHITE OUT AU METLIFE STADIUM",
            "keywords": "NFL Semaine 10, Giants, Commanders, Jayden Daniels, J.J. McCarthy, Prime Video"
        },
        "basketball": {
            "tagline": "NBA : Harden marque 32 pts au MSG, Cleveland bat les Knicks 115-107 ; Houston domine les Warriors 115-108 (Curry blesse).",
            "liveNow": "Mercredi : Cavaliers 115-107 Knicks (Harden 32, Brunson 27) ; Rockets 115-108 Warriors (Curry blesse Q1, Sengun 19) ; Celtics 98-93 Raptors. Ce soir : 4 matchs.",
            "pulse": "NBA : HARDEN INSCRIT 32 PTS AU MSG, CURRY SORT BLESSE A HOUSTON ET BOSTON RENVERSE TORONTO",
            "keywords": "NBA, Cavaliers, Knicks, James Harden, Rockets, Warriors, Stephen Curry, Celtics"
        },
        "soccer": {
            "tagline": "UWCL & Ligue des nations ce soir : Barcelone-Arsenal au Camp Nou et Angleterre-Croatie a Wembley apres le 6-0 d'OL Lyonnes a Turin.",
            "liveNow": "Ce soir : Barcelone-Arsenal (18h45 CET) ; Angleterre-Croatie (19h45 UK), Italie-France, Tchequie-Espagne (20h45 CET). Mercredi : Juventus 0-6 OL Lyonnes.",
            "pulse": "CE SOIR : BARCELONE VS ARSENAL AU CAMP NOU ET ANGLETERRE VS CROATIE APRES LE 6-0 LYONNAIS",
            "keywords": "UWCL, Barcelone, Arsenal, Camp Nou, Angleterre, Croatie, Ligue des nations, OL Lyonnes"
        },
        "tennis": {
            "tagline": "Tirage de Turin : Zverev dans le groupe McEnroe, Alcaraz dans le groupe Lendl ; Fritz affronte Rune aujourd'hui a Stockholm.",
            "liveNow": "Turin : McEnroe (Zverev, Shelton, Fils, Jodar) ; Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Stockholm aujourd'hui : quart Fritz vs Rune.",
            "pulse": "NITTO ATP FINALS TIRAGE : ALCARAZ ET ZVEREV SEPARES A TURIN AVANT FRITZ VS RUNE A STOCKHOLM",
            "keywords": "Nitto ATP Finals, Turin, Alcaraz, Zverev, Stockholm Open, Fritz, Rune"
        },
        "f1": {
            "tagline": "J-7 avant la manche 21 a Las Vegas : cinq pilotes F1 groupes en 33 points derriere le champion Antonelli.",
            "liveNow": "Course a P2 : Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390 ; Mercedes 652). Manche 21 : Las Vegas (19-21 nov).",
            "pulse": "MANCHE 21 LAS VEGAS : VERSTAPPEN A NORRIS GROUPES EN 33 PTS DERRIERE ANTONELLI",
            "keywords": "Formule 1, Manche 21, Las Vegas GP, Verstappen, Norris, Antonelli, Mercedes"
        },
        "golf": {
            "tagline": "Dubai T1 : Joost Luiten signe 67 (-5) devant Jacob Skov Olesen (68) et Rory McIlroy (69, T3).",
            "liveNow": "Dubai T1 : 1. Joost Luiten -5 (67) ; 2. Jacob Skov Olesen -4 (68) ; T3. Rory McIlroy -3 (69), Perez, De Leo, Schott, Laporta ; T28. Chacarra E (72).",
            "pulse": "DUBAI T1 : LUITEN EN TETE EN 67 (-5), MCILROY (69) PREND TROIS COUPS A CHACARRA",
            "keywords": "Golf, DP World Tour Championship, Joost Luiten, Rory McIlroy, Eugenio Chacarra"
        },
        "home": {
            "tonight": "Bureau du jeudi",
            "tonightBlurb": "Barcelone recoit Arsenal au Camp Nou en meme temps qu'Angleterre-Croatie a Wembley apres le 6-0 d'OL Lyonnes chez la Juventus. Ce soir TNF oppose Jayden Daniels a J.J. McCarthy. Luiten (67) devance McIlroy (69) a Dubai ; tirage de Turin fixe.",
            "plTitle": "Camp Nou ce soir & Ligue des nations : Barcelone-Arsenal et Angleterre-Croatie apres le 6-0 de Lyon",
            "plBlurb": "Arsenal mene en PL (27 pts devant Brighton 22 et City 21). Ce soir : Barcelone-Arsenal (18h45) et Angleterre-Croatie (19h45 UK), Italie-France.",
            "f1Title": "Compte a rebours Las Vegas (Manche 21) : 33 points entre Verstappen (279) et Norris (246)",
            "f1Blurb": "Mercedes (652) et Antonelli (390) deja titrés avant les 6,201 km de Las Vegas (19-21 nov) devant Ferrari (510), Red Bull (415) et McLaren (398)."
        },
        "pg": {
            "pinFinal": "Groupes Turin : McEnroe (Zverev, Shelton, Fils, Jodar) | Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Stockholm QF : Fritz vs Rune.",
            "week1Closed": "NFL Semaine 9 MNF : les Bills (7-1) dominent les Vikings (6-2) 23-6 a Minneapolis.",
            "week1Sub": "Cook 107 yds, 1 TD ; Allen 234 yds vers Latu ; Wentz 2 INT. Ce soir : Commanders chez les Giants (les deux QB aptes).",
            "countdownTnf": "CE SOIR Semaine 10 TNF (20h15 ET) : Commanders (Daniels apte, C Patrick forfait) chez les Giants (McCarthy actif).",
            "gridAfterMadrid": "Pilotes et Constructeurs avant la manche 21 · Las Vegas Strip (19-21 nov)",
            "barsPoints": "Antonelli (390) & Mercedes (652) champions ; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Treve Premier League (J10) : Arsenal 27 pts, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Choisissez un club. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea et Everton 16.",
            "plFootnote": "Mercredi UWCL : Juventus 0-6 OL Lyonnes (Katoto 2) ; OH Leuven 1-1 HB Koge. Ce soir : Barcelone-Arsenal et Angleterre-Croatie.",
            "majorsDone": "Dubai T1 : Joost Luiten -5 (67), Jacob Skov Olesen -4 (68), Rory McIlroy -3 (69, T3), Eugenio Chacarra E (72, T28)."
        }
    },
    "es": {
        "common": {
            "todayDesk": "Edicion del jueves: Barcelona recibe al Arsenal en el Camp Nou e Inglaterra choca con Croacia en Wembley. TNF hoy: Commanders ante Giants. Dubai R1: Luiten 67, McIlroy 69.",
            "todayNfl": "TNF esta noche (20:15 ET, Prime Video): Commanders (2-5-1, Daniels apto, C Patrick baja) en Giants (5-2-1, McCarthy listo). MNF: Bills 23-6 Vikings.",
            "todayTnf": "NFL Semana 10 hoy: Commanders (Daniels apto, Patrick y Yankoff baja) en Giants (5-2-1, White Out), 20:15 ET tras el 27-27 de Semana 5."
        },
        "football": {
            "tagline": "TNF esta noche (20:15 ET): Jayden Daniels y J.J. McCarthy listos para el duelo Giants-Commanders en MetLife.",
            "liveNow": "Esta noche 20:15 ET: Commanders (Daniels apto, C Patrick baja) en Giants (McCarthy/Nabers/Skattebo listos). MNF: Bills 23, Vikings 6.",
            "pulse": "NFL TNF HOY: DANIELS Y MCCARTHY CON LUZ VERDE PARA EL WHITE OUT EN METLIFE STADIUM",
            "keywords": "NFL Semana 10, Giants, Commanders, Jayden Daniels, J.J. McCarthy, TNF"
        },
        "basketball": {
            "tagline": "NBA: Harden anota 32 puntos en el MSG con Cleveland ante Knicks (115-107); Rockets vencen 115-108 tras lesion de Curry.",
            "liveNow": "Finales mie: Cavaliers 115-107 Knicks (Harden 32, Brunson 27); Rockets 115-108 Warriors (Curry lesion Q1, Sengun 19); Celtics 98-93 Raptors. Hoy: 4 partidos.",
            "pulse": "NBA: HARDEN ANOTA 32 EN EL MSG, CURRY SE LESIONA EN HOUSTON Y BOSTON REMONTA 22 PUNTOS",
            "keywords": "NBA, Cavaliers, Knicks, James Harden, Rockets, Warriors, Stephen Curry, Celtics"
        },
        "soccer": {
            "tagline": "UWCL y Liga de Naciones hoy: Barcelona-Arsenal en el Camp Nou e Inglaterra-Croacia en Wembley tras el 6-0 de OL Lyonnes a la Juventus.",
            "liveNow": "Esta noche: Barcelona-Arsenal (18:45 CET); Inglaterra-Croacia (19:45 UK), Italia-Francia, Chequia-Espana (20:45 CET). Mie: Juventus 0-6 OL Lyonnes.",
            "pulse": "HOY: BARCELONA VS ARSENAL EN EL CAMP NOU E INGLATERRA VS CROACIA TRAS EL 0-6 DE LYON",
            "keywords": "UWCL, Barcelona, Arsenal, Camp Nou, Inglaterra, Croacia, Liga de Naciones, OL Lyonnes"
        },
        "tennis": {
            "tagline": "Sorteo de Turin definido: Zverev lidera el Grupo McEnroe y Alcaraz el Lendl; hoy Fritz contra Rune en Estocolmo.",
            "liveNow": "Turin: McEnroe (Zverev, Shelton, Fils, Jodar); Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Estocolmo hoy: cuartos Fritz vs Rune.",
            "pulse": "SORTEO NITTO ATP FINALS: ALCARAZ Y ZVEREV SEPARADOS EN TURIN ANTES DE FRITZ-RUNE",
            "keywords": "Nitto ATP Finals, Turin, Carlos Alcaraz, Alexander Zverev, Estocolmo, Taylor Fritz, Holger Rune"
        },
        "f1": {
            "tagline": "A una semana de la ronda 21 en Las Vegas: cinco pilotos separados por 33 puntos tras el campeon Antonelli.",
            "liveNow": "Lucha por P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Ronda 21: Las Vegas (19-21 nov).",
            "pulse": "CUENTA REGRESIVA RONDA 21 LAS VEGAS: 33 PUNTOS ENTRE VERSTAPPEN Y NORRIS TRAS ANTONELLI",
            "keywords": "Formula 1, Ronda 21, Las Vegas GP, Verstappen, Norris, Antonelli, Mercedes"
        },
        "golf": {
            "tagline": "Dubai R1 completa: Joost Luiten firma 67 (-5) ante Jacob Skov Olesen (68) y Rory McIlroy (69, T3).",
            "liveNow": "Dubai R1: 1. Joost Luiten -5 (67); 2. Jacob Skov Olesen -4 (68); T3. Rory McIlroy -3 (69), Perez, De Leo, Schott, Laporta; T28. Chacarra E (72).",
            "pulse": "DUBAI R1: LUITEN MANDA CON 67 (-5) Y MCILROY (69) RECORTA TRES GOLPES A CHACARRA",
            "keywords": "Golf, DP World Tour Championship, Joost Luiten, Rory McIlroy, Eugenio Chacarra"
        },
        "home": {
            "tonight": "Jueves al dia",
            "tonightBlurb": "El Barcelona recibe al Arsenal en el Camp Nou junto al Inglaterra-Croacia tras el 6-0 del OL Lyonnes en Biella. Esta noche TNF mide a Jayden Daniels y J.J. McCarthy. Luiten (67) lidera ante McIlroy (69) en Dubai; cuadros listos en Turin.",
            "plTitle": "Camp Nou hoy y Liga de Naciones: Barcelona-Arsenal e Inglaterra-Croacia tras el 6-0 del Lyon",
            "plBlurb": "El Arsenal mantiene 27 pts en Premier (Brighton 22, Man City 21). Hoy: Barcelona-Arsenal (18:45 CET) e Inglaterra-Croacia, Italia-Francia, Chequia-Espana.",
            "f1Title": "Rumbo a Ronda 21 en Las Vegas: 33 puntos entre Verstappen (279) y Norris (246)",
            "f1Blurb": "Mercedes (652) y Antonelli (390) ya son campeones hacia el circuito de 6,201 km (19-21 nov) con Ferrari (510), Red Bull (415) y McLaren (398)."
        },
        "pg": {
            "pinFinal": "Grupos Turin: McEnroe (Zverev, Shelton, Fils, Jodar) | Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Estocolmo CF hoy: Fritz vs Rune.",
            "week1Closed": "NFL Semana 9 MNF: Bills (7-1) frenan 23-6 a los Vikings (6-2) en Minneapolis.",
            "week1Sub": "Cook 107 yds, 1 TD; Allen 234 yds a Latu; Wentz 2 INT. Hoy: Commanders en Giants (ambos QB aptos).",
            "countdownTnf": "ESTA NOCHE Semana 10 TNF (20:15 ET): Commanders (Daniels apto, C Patrick baja) en Giants (McCarthy activo).",
            "gridAfterMadrid": "Pilotos y Constructores hacia Ronda 21 · Las Vegas Strip (19-21 nov)",
            "barsPoints": "Antonelli (390) y Mercedes (652) campeones; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Pausa Premier League (J10): Arsenal 27 pts, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Elige un club. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea y Everton 16.",
            "plFootnote": "Mie UWCL: Juventus 0-6 OL Lyonnes (Katoto 2); OH Leuven 1-1 HB Koge. Hoy: Barcelona-Arsenal e Inglaterra-Croacia.",
            "majorsDone": "Dubai R1 final: Joost Luiten -5 (67), Jacob Skov Olesen -4 (68), Rory McIlroy -3 (69, T3), Eugenio Chacarra E (72, T28)."
        }
    },
    "de": {
        "common": {
            "todayDesk": "Donnerstag-Ueberblick: Barcelona empfaengt Arsenal im Camp Nou, England trifft in Wembley auf Kroatien. TNF heute: Commanders bei Giants. Dubai R1: Luiten 67, McIlroy 69.",
            "todayNfl": "TNF heute Nacht (20:15 ET, Prime Video): Commanders (2-5-1, Daniels fit, C Patrick aus) bei Giants (5-2-1, McCarthy einsatzbereit). MNF: Bills 23:6 Vikings.",
            "todayTnf": "NFL Woche 10 heute Nacht: Commanders (Daniels fit, Patrick & Yankoff aus) bei den Giants (5-2-1, White Out) um 20:15 ET nach dem 27:27."
        },
        "football": {
            "tagline": "TNF heute Nacht (20:15 ET): Jayden Daniels & J.J. McCarthy beide einsatzbereit fuer Giants gegen Commanders.",
            "liveNow": "Heute 20:15 ET: Commanders (Daniels fit, C Patrick raus) bei Giants (McCarthy/Nabers/Skattebo dabei). MNF: Bills 23, Vikings 6.",
            "pulse": "NFL TNF HEUTE NACHT: DANIELS UND MCCARTHY FIT FUER DAS WHITE OUT IM METLIFE STADIUM",
            "keywords": "NFL Woche 10, Giants, Commanders, Jayden Daniels, J.J. McCarthy, TNF"
        },
        "basketball": {
            "tagline": "NBA: Harden mit 32 Punkten im MSG beim Cavs-Sieg in New York (115:107); Rockets schlagen Warriors 115:108 (Curry frueh verletzt).",
            "liveNow": "Mittwoch: Cavaliers 115:107 Knicks (Harden 32, Brunson 27); Rockets 115:108 Warriors (Curry Q1 verletzt, Sengun 19); Celtics 98:93 Raptors. Heute: 4 Spiele.",
            "pulse": "NBA: HARDEN ERZIELT 32 IM MSG, CURRY SCHEIDET IN HOUSTON VERLETZT AUS, CELTICS HOLEN -22 AUF",
            "keywords": "NBA, Cavaliers, Knicks, James Harden, Rockets, Warriors, Stephen Curry, Celtics"
        },
        "soccer": {
            "tagline": "UWCL & Nations League heute: Barcelona gegen Arsenal im Camp Nou und England gegen Kroatien nach OL Lyonnes' 6:0 in Biella.",
            "liveNow": "Heute Abend: Barcelona vs. Arsenal (18:45 MEZ); England vs. Kroatien (19:45 UK), Italien vs. Frankreich, Tschechien vs. Spanien (20:45 MEZ). Mi: Juventus 0:6 OL Lyonnes.",
            "pulse": "HEUTE ABEND: BARCELONA VS. ARSENAL IM CAMP NOU & ENGLAND VS. KROATIEN NACH LYONS 6:0",
            "keywords": "UWCL, Barcelona, Arsenal, Camp Nou, England, Kroatien, Nations League, OL Lyonnes"
        },
        "tennis": {
            "tagline": "Turin-Auslosung steht: Zverev fuehrt McEnroe-Gruppe an, Alcaraz die Lendl-Gruppe; Fritz gegen Rune heute in Stockholm.",
            "liveNow": "Turin: McEnroe (Zverev, Shelton, Fils, Jodar); Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Stockholm heute: VF Fritz vs. Rune.",
            "pulse": "NITTO ATP FINALS AUSLOSUNG: ALCARAZ & ZVEREV GETRENNT IN TURIN VOR FRITZ VS. RUNE",
            "keywords": "Nitto ATP Finals, Turin, Carlos Alcaraz, Alexander Zverev, Stockholm, Taylor Fritz, Holger Rune"
        },
        "f1": {
            "tagline": "Noch eine Woche bis Runde 21 in Las Vegas: fuenf F1-Stars innerhalb von 33 Punkten hinter Champion Antonelli.",
            "liveNow": "P2-Duell: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Runde 21: Las Vegas (19.-21. Nov).",
            "pulse": "RUNDE 21 LAS VEGAS COUNTDOWN: VERSTAPPEN BIS NORRIS IN 33 PUNKTEN HINTER ANTONELLI",
            "keywords": "Formel 1, Runde 21, Las Vegas GP, Verstappen, Norris, Antonelli, Mercedes"
        },
        "golf": {
            "tagline": "Dubai R1 beendet: Joost Luiten fuehrt mit 67 (-5) vor Jacob Skov Olesen (68) und Rory McIlroy (69, T3).",
            "liveNow": "Dubai R1: 1. Joost Luiten -5 (67); 2. Jacob Skov Olesen -4 (68); T3. Rory McIlroy -3 (69), Schott, Perez, De Leo, Laporta; T28. Chacarra E (72).",
            "pulse": "DUBAI R1: LUITEN FUEHRT MIT 67 (-5), MCILROY (69) NIMMT CHACARRA DREI SCHLAEGE AB",
            "keywords": "Golf, DP World Tour Championship, Joost Luiten, Rory McIlroy, Freddy Schott, Eugenio Chacarra"
        },
        "home": {
            "tonight": "Donnerstag im Fokus",
            "tonightBlurb": "Barcelona empfaengt Arsenal im Camp Nou parallel zu England gegen Kroatien nach OL Lyonnes' 6:0 gegen Juventus. Heute Nacht TNF zwischen Jayden Daniels und J.J. McCarthy. Luiten (67) fuehrt in Dubai vor McIlroy (69); Turin-Gruppen gelost.",
            "plTitle": "Camp Nou heute & Nations League: Barcelona vs. Arsenal und England vs. Kroatien nach Lyons 6:0",
            "plBlurb": "Arsenal fuehrt die PL weiter an (27 Pkt. vor Brighton 22, Man City 21). Heute: Barcelona vs. Arsenal & England vs. Kroatien, Italien vs. Frankreich.",
            "f1Title": "Countdown zu Runde 21 in Las Vegas: 33 Punkte trennen Verstappen (279) bis Norris (246)",
            "f1Blurb": "Mercedes (652) und Antonelli (390) reisen als Weltmeister zum 6,201-km-Strip (19.-21. Nov) vor Ferrari (510), Red Bull (415) und McLaren (398)."
        },
        "pg": {
            "pinFinal": "Turin-Gruppen: McEnroe (Zverev, Shelton, Fils, Jodar) | Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Stockholm VF: Fritz vs. Rune.",
            "week1Closed": "NFL Woche 9 MNF: Bills (7-1) bezwingen Vikings (6-2) 23:6 in Minneapolis.",
            "week1Sub": "Cook 107 Yds, 1 TD; Allen 234 Yds auf Latu; Wentz 2 INTs. Heute Nacht: Commanders bei Giants (beide QBs fit).",
            "countdownTnf": "HEUTE NACHT Woche 10 TNF (20:15 ET): Commanders (Daniels fit, C Patrick aus) bei Giants (McCarthy aktiv).",
            "gridAfterMadrid": "Fahrer & Konstrukteure vor Runde 21 · Las Vegas Strip (19.-21. Nov)",
            "barsPoints": "Antonelli (390) & Mercedes (652) Champions; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "PL-Pause (Spieltag 10): Arsenal 27 Pkt., Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Klub waehlen. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea und Everton 16.",
            "plFootnote": "Mi UWCL: Juventus 0:6 OL Lyonnes (Katoto 2); OH Leuven 1:1 HB Koge. Heute: Barcelona vs. Arsenal & England vs. Kroatien.",
            "majorsDone": "Dubai R1: Joost Luiten -5 (67), Jacob Skov Olesen -4 (68), Rory McIlroy -3 (69, T3), Eugenio Chacarra E (72, T28)."
        }
    },
    "it": {
        "common": {
            "todayDesk": "Edizione del giovedi: Barcellona-Arsenal al Camp Nou e Inghilterra-Croazia a Wembley. TNF stanotte: Commanders dai Giants. Dubai R1: Luiten 67, McIlroy 69.",
            "todayNfl": "TNF stanotte (20:15 ET, Prime Video): Commanders (2-5-1, Daniels abile, C Patrick fuori) dai Giants (5-2-1, McCarthy attivo). MNF: Bills 23-6 Vikings.",
            "todayTnf": "NFL Week 10 stanotte: Commanders (Daniels abile, Patrick e Yankoff out) dai Giants (5-2-1, White Out), 20:15 ET dopo il 27-27."
        },
        "football": {
            "tagline": "TNF stanotte (20:15 ET): Jayden Daniels e J.J. McCarthy entrambi abili per il White Out Giants-Commanders.",
            "liveNow": "Stanotte 20:15 ET: Commanders (Daniels abile, C Patrick out) dai Giants (McCarthy/Nabers/Skattebo pronti). MNF: Bills 23, Vikings 6.",
            "pulse": "NFL TNF STANOTTE: DANIELS E MCCARTHY ABILI PER IL WHITE OUT AL METLIFE STADIUM",
            "keywords": "NFL Week 10, Giants, Commanders, Jayden Daniels, J.J. McCarthy, TNF"
        },
        "basketball": {
            "tagline": "NBA: Harden ne segna 32 al MSG nel colpo Cavs sui Knicks (115-107); Houston batte i Warriors 115-108 (Curry ko nel Q1).",
            "liveNow": "Mercoledi: Cavaliers 115-107 Knicks (Harden 32, Brunson 27); Rockets 115-108 Warriors (Curry infortunio Q1, Sengun 19); Celtics 98-93 Raptors. Stanotte: 4 gare.",
            "pulse": "NBA: HARDEN 32 AL MSG, INFORTUNIO PER CURRY A HOUSTON E RIMONTA CELTICS DA -22",
            "keywords": "NBA, Cavaliers, Knicks, James Harden, Rockets, Warriors, Stephen Curry, Celtics"
        },
        "soccer": {
            "tagline": "UWCL e Nations League stasera: Barcellona-Arsenal al Camp Nou, Italia-Francia a San Siro e Inghilterra-Croazia dopo il 6-0 OL Lyonnes alla Juventus.",
            "liveNow": "Stasera: Barcellona-Arsenal (18:45 CET); Italia-Francia & Repubblica Ceca-Spagna (20:45 CET), Inghilterra-Croazia (19:45 UK). Mer: Juventus 0-6 OL Lyonnes.",
            "pulse": "STASERA: BARCELLONA-ARSENAL AL CAMP NOU E ITALIA-FRANCIA DOPO IL 6-0 DEL LIONE A BIELLA",
            "keywords": "UWCL, Barcellona, Arsenal, Camp Nou, Italia, Francia, Inghilterra, OL Lyonnes"
        },
        "tennis": {
            "tagline": "Sorteggio Torino deciso: Zverev nel gruppo McEnroe, Alcaraz nel Lendl con Cobolli; oggi Fritz-Rune a Stoccolma.",
            "liveNow": "Torino: McEnroe (Zverev, Shelton, Fils, Jodar); Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Stoccolma oggi: quarto Fritz vs Rune.",
            "pulse": "SORTEGGIO NITTO ATP FINALS: ALCARAZ E COBOLLI NEL LENDL, ZVEREV NEL MCENROE; FRITZ-RUNE OGGI",
            "keywords": "Nitto ATP Finals, Torino, Alcaraz, Zverev, Flavio Cobolli, Stoccolma, Fritz, Rune"
        },
        "f1": {
            "tagline": "Meno sette al Round 21 di Las Vegas: cinque piloti in 33 punti alle spalle del campione Antonelli.",
            "liveNow": "Corsa al P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Round 21: Las Vegas (19-21 nov).",
            "pulse": "ROUND 21 LAS VEGAS: CINQUE PILOTI IN 33 PUNTI DIETRO AL CAMPIONE ANTONELLI",
            "keywords": "Formula 1, Round 21, Las Vegas GP, Verstappen, Norris, Antonelli, Ferrari"
        },
        "golf": {
            "tagline": "Dubai R1 concluso: Joost Luiten comanda in 67 (-5) su Jacob Skov Olesen (68); De Leo, Laporta e McIlroy terzi (-3).",
            "liveNow": "Dubai R1: 1. Joost Luiten -5 (67); 2. Jacob Skov Olesen -4 (68); T3. Rory McIlroy -3 (69), De Leo, Laporta, Perez, Schott; T28. Chacarra E (72).",
            "pulse": "DUBAI R1: LUITEN GUIDA CON 67 (-5), DE LEO E LAPORTA A -3 CON MCILROY DAVANTI A CHACARRA",
            "keywords": "Golf, DP World Tour Championship, Joost Luiten, Rory McIlroy, Gregorio De Leo, Francesco Laporta"
        },
        "home": {
            "tonight": "Giovedi in diretta",
            "tonightBlurb": "Barcellona-Arsenal al Camp Nou insieme a Italia-Francia e Inghilterra-Croazia dopo il 6-0 subito dalla Juventus contro OL Lyonnes. Stanotte TNF tra Jayden Daniels e J.J. McCarthy. Luiten (67) guida a Dubai davanti a McIlroy, De Leo e Laporta (-3); sorteggiati i gironi di Torino.",
            "plTitle": "Camp Nou e Nations League stasera: Barcellona-Arsenal, Italia-Francia e Inghilterra-Croazia",
            "plBlurb": "Arsenal sempre in vetta in PL a 27 punti (Brighton 22, Man City 21). Stasera Barcellona-Arsenal (18:45) e Nations League MD5.",
            "f1Title": "Verso il Round 21 di Las Vegas: 33 punti da Verstappen (279) a Norris (246)",
            "f1Blurb": "Mercedes (652) e Antonelli (390) gia campioni prima dei 6,201 km di Las Vegas (19-21 nov) davanti a Ferrari (510), Red Bull (415) e McLaren (398)."
        },
        "pg": {
            "pinFinal": "Gironi Torino: McEnroe (Zverev, Shelton, Fils, Jodar) | Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Stoccolma QF oggi: Fritz vs Rune.",
            "week1Closed": "NFL Week 9 MNF: i Bills (7-1) bloccano i Vikings (6-2) 23-6 a Minneapolis.",
            "week1Sub": "Cook 107 yds, 1 TD; Allen 234 yds a Latu; Wentz 2 INT. Stanotte: Commanders dai Giants (entrambi i QB abili).",
            "countdownTnf": "STANOTTE Week 10 TNF (20:15 ET): Commanders (Daniels abile, C Patrick fuori) dai Giants (McCarthy attivo).",
            "gridAfterMadrid": "Piloti e Costruttori verso il Round 21 · Las Vegas Strip (19-21 nov)",
            "barsPoints": "Antonelli (390) e Mercedes (652) campioni; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Sosta Premier League (G10): Arsenal 27 pt, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Seleziona un club. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea ed Everton 16.",
            "plFootnote": "Mer UWCL: Juventus 0-6 OL Lyonnes (Katoto 2); OH Leuven 1-1 HB Koge. Stasera: Barcellona-Arsenal e Italia-Francia.",
            "majorsDone": "Dubai R1: Joost Luiten -5 (67), Jacob Skov Olesen -4 (68), Rory McIlroy, De Leo & Laporta -3, Chacarra E (72)."
        }
    },
    "pl": {
        "common": {
            "todayDesk": "Czwartek: Barcelona podejmuje Arsenal na Camp Nou, a Anglia gra z Chorwacja na Wembley. TNF dzis w nocy: Commanders u Giants. Dubaj R1: Luiten 67, McIlroy 69.",
            "todayNfl": "TNF dzis w nocy (20:15 ET, Prime Video): Commanders (2-5-1, Daniels zdrowy, C Patrick poza gra) u Giants (5-2-1, McCarthy gotowy). MNF: Bills 23:6 Vikings.",
            "todayTnf": "NFL 10. tydzien dzis: Commanders (Daniels gotowy, Patrick i Yankoff poza gra) u Giants (5-2-1, White Out) o 20:15 ET po remisie 27:27."
        },
        "football": {
            "tagline": "TNF dzis w nocy (20:15 ET): Jayden Daniels i J.J. McCarthy obaj gotowi na starcie Giants z Commanders.",
            "liveNow": "Dzis 20:15 ET: Commanders (Daniels zdrowy, C Patrick out) u Giants (McCarthy/Nabers/Skattebo gotowi). MNF: Bills 23, Vikings 6.",
            "pulse": "NFL TNF DZIS W NOCY: JAYDEN DANIELS I J.J. MCCARTHY GOTOWI NA WHITE OUT NA METLIFE",
            "keywords": "NFL 10. tydzien, Giants, Commanders, Jayden Daniels, J.J. McCarthy, TNF"
        },
        "basketball": {
            "tagline": "NBA: Harden rzuca 32 pkt w MSG dla Cavaliers przeciwko Knicks (115:107); Rockets pokonuja Warriors 115:108 po urazie Curry'ego.",
            "liveNow": "Sroda: Cavaliers 115:107 Knicks (Harden 32, Brunson 27); Rockets 115:108 Warriors (uraz Curry'ego Q1, Sengun 19); Celtics 98:93 Raptors. Dzis: 4 mecze.",
            "pulse": "NBA: 32 PUNKTY HARDENA W MSG, KONTUZJA CURRY'EGO W HOUSTON I POWROT CELTICS Z -22",
            "keywords": "NBA, Cavaliers, Knicks, James Harden, Rockets, Warriors, Stephen Curry, Celtics"
        },
        "soccer": {
            "tagline": "UWCL i Liga Narodow dzis: Barcelona-Arsenal na Camp Nou i Anglia-Chorwacja na Wembley po zwyciestwie OL Lyonnes 6:0 nad Juventusem.",
            "liveNow": "Dzis wieczorem: Barcelona-Arsenal (18:45 CET); Anglia-Chorwacja (19:45 UK), Wlochy-Francja, Czechy-Hiszpania (20:45 CET). Sroda: Juventus 0:6 OL Lyonnes.",
            "pulse": "DZIS WIECZOR: BARCELONA VS ARSENAL NA CAMP NOU I ANGLIA VS CHORWACJA PO 6:0 LYONU",
            "keywords": "UWCL, Barcelona, Arsenal, Camp Nou, Anglia, Chorwacja, Liga Narodow, OL Lyonnes"
        },
        "tennis": {
            "tagline": "Losowanie w Turynie: Zverev na czele grupy McEnroe, Alcaraz prowadzi w Lendl; dzis Fritz kontra Rune w Sztokholmie.",
            "liveNow": "Turyn: McEnroe (Zverev, Shelton, Fils, Jodar); Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Sztokholm dzis: cwiercfinal Fritz vs Rune.",
            "pulse": "LOSOWANIE NITTO ATP FINALS: ALCARAZ I ZVEREV ROZDZIELENI W TURYNIE PRZED FRITZ-RUNE",
            "keywords": "Nitto ATP Finals, Turyn, Alcaraz, Zverev, Stockholm Open, Fritz, Rune"
        },
        "f1": {
            "tagline": "Tydzien do 21. rundy w Las Vegas: piec gwiazd F1 w 33 punktach za mistrzem Antonellim.",
            "liveNow": "Walka o P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Runda 21: Las Vegas (19-21 lis).",
            "pulse": "TYDZIEN DO 21. RUNDY W LAS VEGAS: VERSTAPPEN DO NORRISA W 33 PKT ZA ANTONELLIM",
            "keywords": "Formula 1, Runda 21, Las Vegas GP, Verstappen, Norris, Antonelli, Mercedes"
        },
        "golf": {
            "tagline": "Dubaj R1: Joost Luiten prowadzi z wynikiem 67 (-5) przed Jacobem Skov Olesenem (68) i Rorym McIlroyem (69, T3).",
            "liveNow": "Dubaj R1: 1. Joost Luiten -5 (67); 2. Jacob Skov Olesen -4 (68); T3. Rory McIlroy -3 (69), Perez, De Leo, Schott, Laporta; T28. Chacarra E (72).",
            "pulse": "DUBAJ R1: LUITEN PROWADZI PO 67 (-5), MCILROY (69) ODRABIA TRZY UDERZENIA DO CHACARRY",
            "keywords": "Golf, DP World Tour Championship, Joost Luiten, Rory McIlroy, Eugenio Chacarra"
        },
        "home": {
            "tonight": "Czwartek w sporcie",
            "tonightBlurb": "Barcelona podejmuje Arsenal na Camp Nou rownolegle z Anglia-Chorwacja po triumfie OL Lyonnes 6:0 nad Juventusem. Dzis w nocy TNF z udzialem Jaydena Danielsa i J.J. McCarthy'ego. Luiten (67) przed McIlroyem (69) w Dubaju; grupy w Turynie rozlosowane.",
            "plTitle": "Camp Nou dzis i Liga Narodow: Barcelona-Arsenal oraz Anglia-Chorwacja po 6:0 Lyonu",
            "plBlurb": "Arsenal utrzymuje 27 pkt na czele PL (Brighton 22, Man City 21). Dzis: Barcelona-Arsenal (18:45) i Anglia-Chorwacja, Wlochy-Francja.",
            "f1Title": "Odliczanie do 21. rundy w Las Vegas: 33 punkty od Verstappena (279) do Norrisa (246)",
            "f1Blurb": "Mercedes (652) i Antonelli (390) sa juz mistrzami przed torem Strip o dlugosci 6,201 km (19-21 lis) przed Ferrari (510), Red Bullem (415) i McLarenem (398)."
        },
        "pg": {
            "pinFinal": "Grupy Turyn: McEnroe (Zverev, Shelton, Fils, Jodar) | Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Sztokholm 1/4: Fritz vs Rune.",
            "week1Closed": "NFL Tydzien 9 MNF: Bills (7-1) zatrzymuja Vikings (6-2) 23:6 w Minneapolis.",
            "week1Sub": "Cook 107 yds, 1 TD; Allen 234 yds do Latu; Wentz 2 INT. Dzis w nocy: Commanders u Giants (obaj QB gotowi).",
            "countdownTnf": "DZIS W NOCY Tydzien 10 TNF (20:15 ET): Commanders (Daniels zdrowy, C Patrick out) u Giants (McCarthy gotowy).",
            "gridAfterMadrid": "Kierowcy i Konstruktorzy przed 21. runda · Las Vegas Strip (19-21 lis)",
            "barsPoints": "Antonelli (390) i Mercedes (652) mistrzami; Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246.",
            "tableAfterMonday": "Przerwa Premier League (K10): Arsenal 27 pkt, Brighton 22, Man City 21, Liverpool 18, Chelsea 16.",
            "pinClub": "Wybierz klub. Arsenal 27, Brighton 22, Man City 21, Liverpool 18, Chelsea i Everton 16.",
            "plFootnote": "Sroda UWCL: Juventus 0:6 OL Lyonnes (Katoto 2); OH Leuven 1:1 HB Koge. Dzis: Barcelona-Arsenal i Anglia-Chorwacja.",
            "majorsDone": "Dubaj R1: Joost Luiten -5 (67), Jacob Skov Olesen -4 (68), Rory McIlroy -3 (69, T3), Eugenio Chacarra E (72, T28)."
        }
    },
    "zh": {
        "common": {
            "todayDesk": "周四要闻：巴萨女足诺坎普迎战阿森纳，欧国联英格兰温布利战克罗地亚。今晚TNF：丹尼尔斯与麦卡锡齐复出。迪拜首轮吕腾67杆、麦克罗伊69杆。",
            "todayNfl": "今晚TNF（20:15 ET，Prime Video）：指挥官（2-5-1，丹尼尔斯无碍，中锋帕特里克缺阵）客战巨人（5-2-1，麦卡锡出战）。MNF比尔23-6维京人。",
            "todayTnf": "NFL第10周周四夜赛今夜打响：指挥官（丹尼尔斯复出、帕特里克与扬科夫休战）客战巨人（5-2-1，复古全白战袍），继第5周27-27后再战。"
        },
        "football": {
            "tagline": "今晚TNF（20:15 ET）：杰登·丹尼尔斯与J.J.麦卡锡双双无伤病限制出战巨人主场全白夜赛。",
            "liveNow": "今晚20:15 ET：指挥官（丹尼尔斯可出战、中锋帕特里克缺阵）客战巨人（麦卡锡/纳伯斯/斯卡特博均全勤）。MNF比尔23-6胜维京人。",
            "pulse": "NFL今晚周四夜赛：丹尼尔斯与麦卡锡双双获准登场，巨人与指挥官重演27平续集",
            "keywords": "NFL第10周, 巨人, 指挥官, 杰登·丹尼尔斯, J.J.麦卡锡, 周四夜赛"
        },
        "basketball": {
            "tagline": "NBA：哈登在麦迪逊狂砍32分助骑士115-107力克尼克斯；火箭115-108击败勇士，库里首节伤退。",
            "liveNow": "周三赛果：骑士115-107尼克斯（哈登32分，布伦森27）；火箭115-108勇士（库里Q1伤退，申京19）；凯尔特人98-93猛龙（22分逆转）。今晚4场。",
            "pulse": "NBA：哈登32分攻克麦迪逊，库里首节伤退勇士负火箭，凯尔特人22分大逆转",
            "keywords": "NBA, 骑士, 尼克斯, 詹姆斯·哈登, 火箭, 勇士, 斯蒂芬·库里, 凯尔特人"
        },
        "soccer": {
            "tagline": "今晚欧冠女足与欧国联双线焦点：巴萨诺坎普迎战阿森纳，英格兰温布利对阵克罗地亚；里昂女足前夜6-0大胜尤文。",
            "liveNow": "今晚赛程：巴萨vs阿森纳（18:45 CET）；英格兰vs克罗地亚（19:45 UK），意大利vs法国，捷克vs西班牙（20:45 CET）。周三：尤文0-6里昂。",
            "pulse": "今晚焦点：巴萨诺坎普对决阿森纳，英格兰战克罗地亚，前夜里昂6-0横扫尤文",
            "keywords": "欧冠女足, 巴塞罗那, 阿森纳, 诺坎普, 英格兰, 克罗地亚, 欧国联, 里昂"
        },
        "tennis": {
            "tagline": "都灵年终总决赛抽签揭晓：兹维列夫与阿尔卡拉斯分镇两组；斯德哥尔摩八强弗里茨今日对阵鲁内。",
            "liveNow": "都灵分组：麦肯罗组（兹维列夫、谢尔顿、菲斯、霍达尔）；伦德尔组（阿尔卡拉斯、梅德韦杰夫、科博利、蒂亚福）。斯德哥尔摩今日：弗里茨vs鲁内。",
            "pulse": "ATP年终总决赛分组确定：阿尔卡拉斯兹维列夫分领两区，斯德哥尔摩弗里茨今日战鲁内",
            "keywords": "ATP年终总决赛, 都灵抽签, 阿尔卡拉斯, 兹维列夫, 斯德哥尔摩, 弗里茨, 鲁内"
        },
        "f1": {
            "tagline": "距离第21站拉斯维加斯倒计时一周：冠军安东内利身后的五虎之争仅差33分。",
            "liveNow": "亚军争夺：维斯塔潘279、拉塞尔262、汉密尔顿261、勒克莱尔249、诺里斯246（安东内利390、梅赛德斯652）。第21站：拉斯维加斯（11月19-21日）。",
            "pulse": "第21站拉斯维加斯倒计时：维斯塔潘至诺里斯仅差33分",
            "keywords": "F1, 第21站, 拉斯维加斯站, 维斯塔潘, 诺里斯, 安东内利, 梅赛德斯"
        },
        "golf": {
            "tagline": "迪拜首轮结束：约斯特·吕腾67杆（-5）领先雅各布·斯科夫·奥莱森（68杆）与罗里·麦克罗伊（69杆并列第三）。",
            "liveNow": "迪拜首轮：1.吕腾-5（67）；2.奥莱森-4（68）；T3.麦克罗伊-3（69）、佩雷斯、德莱奥、肖特、拉波尔塔；T28.查卡拉E（72）。",
            "pulse": "迪拜首轮：吕腾67杆领跑，麦克罗伊69杆抢先查卡拉三杆",
            "keywords": "高尔夫, DP世界巡回锦标赛, 约斯特·吕腾, 罗里·麦克罗伊, 欧亨尼奥·查卡拉"
        },
        "home": {
            "tonight": "周四赛事看板",
            "tonightBlurb": "巴萨女足诺坎普迎战阿森纳并与英格兰战克罗地亚同晚开球，前夜里昂6-0大胜尤文。今晚TNF丹尼尔斯与麦卡锡双双复出。迪拜首轮吕腾67杆领跑，麦克罗伊69杆；都灵总决赛分组及周三NBA赛果全汇总。",
            "plTitle": "今夜诺坎普与欧国联：巴萨对决阿森纳，英格兰战克罗地亚，前夜里昂6-0大胜尤文",
            "plBlurb": "阿森纳以27分领跑英超（布莱顿22、曼城21）。今晚关注巴萨vs阿森纳（18:45）及英格兰vs克罗地亚、意大利vs法国。",
            "f1Title": "F1第21站拉斯维加斯倒计时：维斯塔潘（279）至诺里斯（246）差33分",
            "f1Blurb": "梅赛德斯（652分）与安东内利（390分）提前夺冠前往6.201公里拉斯维加斯大道赛道（11月19-21日），法拉利510、红牛415紧追。"
        },
        "pg": {
            "pinFinal": "都灵分组：麦肯罗组（兹维列夫、谢尔顿、菲斯、霍达尔）| 伦德尔组（阿尔卡拉斯、梅德韦杰夫、科博利、蒂亚福）。斯德哥尔摩八强：弗里茨vs鲁内。",
            "week1Closed": "NFL第9周MNF：比尔（7-1）客场23-6压制维京人（6-2）。",
            "week1Sub": "库克107码1达阵；阿伦234码连线拉图；温茨2次抄截。今晚TNF：指挥官客战巨人。",
            "countdownTnf": "今晚第10周TNF（20:15 ET）：指挥官（丹尼尔斯出战、帕特里克缺阵）客战巨人（麦卡锡上场）。",
            "gridAfterMadrid": "第21站前车手与车队榜 · 拉斯维加斯大道赛道（11月19-21日）",
            "barsPoints": "安东内利（390）与梅赛德斯（652）夺冠；维斯塔潘279、拉塞尔262、汉密尔顿261、勒克莱尔249、诺里斯246。",
            "tableAfterMonday": "英超国际比赛日（第10轮）：阿森纳27分、布莱顿22、曼城21、利物浦18、切尔西16。",
            "pinClub": "选择球队。阿森纳27分领跑，布莱顿22，曼城21，利物浦18，切尔西与埃弗顿16。",
            "plFootnote": "周三欧冠女足：尤文0-6里昂（卡托托两球）；鲁汶1-1克厄。今晚：巴萨vs阿森纳、英格兰vs克罗地亚。",
            "majorsDone": "迪拜首轮结束：吕腾-5（67），奥莱森-4（68），麦克罗伊-3（69并列第三），查卡拉E（72并列第28）。"
        }
    },
    "ja": {
        "common": {
            "todayDesk": "木曜デスク：バルセロナ対アーセナルがカンプ・ノウで実現、イングランドはクロアチア戦へ。今夜TNFはダニエルズとマッカーシーが出場可。ドバイ初日ルイテン67、マキロイ69。",
            "todayNfl": "今夜TNF（20:15 ET、Prime Video）：コマンダース（ダニエルズ復帰、Cパトリック欠場）対ジャイアンツ（マッカーシー先発）。MNFはビルズ23-6勝利。",
            "todayTnf": "NFL第10週今夜：コマンダース（ダニエルズ出場可、パトリック＆ヤンコフ欠場）対ジャイアンツ（5勝2敗1分）、第5週27-27の再戦。"
        },
        "football": {
            "tagline": "今夜TNF（20:15 ET）：ジェイデン・ダニエルズとJ.J.マッカーシーが揃って出場可能、メッツライフのホワイトアウト決戦。",
            "liveNow": "今夜20:15 ET：コマンダース（ダニエルズ復帰、Cパトリック欠場）対ジャイアンツ（マッカーシー/ネイバーズ/スカッテボ出場）。MNF：ビルズ23-6バイキングス。",
            "pulse": "NFL TNF今夜：ダニエルズ＆マッカーシーが揃って出陣、ジャイアンツ対コマンダース第5週引き分けの再戦",
            "keywords": "NFL第10週, ジャイアンツ, コマンダース, ジェイデン・ダニエルズ, J.J.マッカーシー"
        },
        "basketball": {
            "tagline": "NBA：ハーデン32得点でキャブズがニックスに115-107勝利；ロケッツはカリー負傷のウォリアーズを115-108撃破。",
            "liveNow": "水曜結果：キャバリアーズ115-107ニックス（ハーデン32、ブランソン27）；ロケッツ115-108ウォリアーズ（カリーQ1負傷、シェングン19）；セルティックス98-93ラプターズ。今夜4試合。",
            "pulse": "NBA：ハーデンがMSGで32得点、カリー負傷交代のウォリアーズにロケッツ勝利、セルティックス22点差逆転",
            "keywords": "NBA, キャバリアーズ, ニックス, ハーデン, ロケッツ, ウォリアーズ, ステフィン・カリー"
        },
        "soccer": {
            "tagline": "今夜UWCL＆ネーションズリーグ：バルセロナ対アーセナル（カンプ・ノウ）とイングランド対クロアチア、前夜はリヨンがユベントスに6-0大勝。",
            "liveNow": "今夜：バルセロナ対アーセナル（18:45 CET）；イングランド対クロアチア（19:45 UK）、イタリア対フランス、チェコ対スペイン（20:45 CET）。水曜：ユベントス0-6リヨン。",
            "pulse": "今夜決戦：カンプ・ノウでバルサ対アーセナル＆ウェンブリーでイングランド対クロアチア、リヨンは6-0大勝",
            "keywords": "UWCL, バルセロナ, アーセナル, カンプ・ノウ, イングランド, クロアチア, ネーションズリーグ, リヨン"
        },
        "tennis": {
            "tagline": "トリノ最終戦の組み合わせ決定：ズベレフがマッケンロー組、アルカラスがレンドル組へ；ストックホルム準々決勝フリッツ対ルネ本日。",
            "liveNow": "トリノ：マッケンロー組（ズベレフ、シェルトン、フィス、ホダール）；レンドル組（アルカラス、メドベージェフ、コボッリ、ティアフォー）。本日ストックホルムQF：フリッツ対ルネ。",
            "pulse": "NITTO ATPファイナルズ組分け決定：アルカラス＆ズベレフが別組、本日ストックホルムでフリッツ対ルネ",
            "keywords": "Nitto ATPファイナルズ, トリノ抽選, アルカラス, ズベレフ, ストックホルム, フリッツ, ルネ"
        },
        "f1": {
            "tagline": "第21戦ラスベガスGPまであと1週間：王者アントネッリの背後で5選手が33点差に密集。",
            "liveNow": "2位争い：フェルスタッペン279、ラッセル262、ハミルトン261、ルクレール249、ノリス246（アントネッリ390、メルセデス652）。第21戦：ラスベガス（11/19-21）。",
            "pulse": "第21戦ラスベガスまで1週間：フェルスタッペンからノリスまで33点差の大接戦",
            "keywords": "F1, 第21戦, ラスベガスGP, フェルスタッペン, ノリス, アントネッリ, メルセデス"
        },
        "golf": {
            "tagline": "ドバイ初日終了：ヨースト・ルイテンが67（-5）で単独首位、オレセン68、マキロイ69で3位タイ。",
            "liveNow": "ドバイ1R：1.ルイテン -5 (67)；2.オレセン -4 (68)；3位T.マキロイ -3 (69)、ペレス、デ・レオ、ショット、ラポルタ；28位T.チャカラ E (72)。",
            "pulse": "ドバイ初日：ルイテンが67（-5）で首位、マキロイは69でチャカラに3打差先勝",
            "keywords": "ゴルフ, DPワールドツアー選手権, ルイテン, ローリー・マキロイ, チャカラ"
        },
        "home": {
            "tonight": "木曜デスク",
            "tonightBlurb": "カンプ・ノウでバルサ対アーセナル、ウェンブリーでイングランド対クロアチアが今夜開催（前夜はリヨンがユベントスに6-0）。今夜TNFはダニエルズ対マッカーシー。ドバイ初日はルイテン67、マキロイ69。トリノ組分けも確定。",
            "plTitle": "今夜カンプ・ノウ＆ネーションズリーグ：バルサ対アーセナルとイングランド対クロアチア",
            "plBlurb": "PL首位アーセナルは勝ち点27（ブライトン22、シティ21）。今夜バルセロナ対アーセナル（18:45）ほか欧州ネーションズリーグ第5節。",
            "f1Title": "第21戦ラスベガスGP直前：フェルスタッペン（279）からノリス（246）まで33点差",
            "f1Blurb": "王者メルセデス（652）＆アントネッリ（390）に続き、全長6.201kmストリップ決戦（11/19-21）へフェラーリ510、レッドブル415、マクラーレン398。"
        },
        "pg": {
            "pinFinal": "トリノ組分け：マッケンロー（ズベレフ、シェルトン、フィス、ホダール）| レンドル（アルカラス、メドベージェフ、コボッリ、ティアフォー）。本日QF：フリッツ対ルネ。",
            "week1Closed": "NFL第9週MNF：ビルズ（7勝1敗）が敵地でバイキングス（6勝2敗）を23-6で撃破。",
            "week1Sub": "クック107yd・1TD、アレン234yd、ウェンツ2INT。今夜TNF：コマンダース対ジャイアンツ（両QB出場可）。",
            "countdownTnf": "今夜第10週TNF（20:15 ET）：コマンダース（ダニエルズ復帰、パトリック欠場）対ジャイアンツ（マッカーシー先発）。",
            "gridAfterMadrid": "第21戦ラスベガス直前順位 · ラスベガス・ストリップ（11/19-21）",
            "barsPoints": "アントネッリ（390）＆メルセデス（652）王座；フェルスタッペン279、ラッセル262、ハミルトン261、ルクレール249、ノリス246。",
            "tableAfterMonday": "プレミアリーグ（第10節）：アーセナル27、ブライトン22、マンC21、リバプール18、チェルシー16。",
            "pinClub": "クラブを選択。アーセナル27、ブライトン22、マンC21、リバプール18、チェルシー＆エバートン16。",
            "plFootnote": "水曜UWCL：ユベントス0-6リヨン（カトト2点）；ルーヴェン1-1キューゲ。今夜：バルサ対アーセナル、イングランド対クロアチア。",
            "majorsDone": "ドバイ1R終了：ルイテン -5 (67)、オレセン -4 (68)、マキロイ -3 (69・3位T)、チャカラ E (72・28位T)。"
        }
    },
    "ko": {
        "common": {
            "todayDesk": "목요일 데스크: 캄프 누 바르셀로나-아스널 및 웸블리 잉글랜드-크로아티아 오늘 밤 개최. TNF 대니얼스·맥카시 출전 준비 완료. 두바이 1R 라위텐 67타, 매킬로이 69타.",
            "todayNfl": "오늘 밤 TNF(20:15 ET, 프라임 비디오): 커맨더스(2-5-1, 대니얼스 정상, C 패트릭 결장) @ 자이언츠(5-2-1, 맥카시 선발). MNF 빌스 23-6 승.",
            "todayTnf": "NFL 10주차 오늘 밤: 커맨더스(대니얼스 출전, 패트릭·얀코프 아웃) @ 자이언츠(5-2-1, 화이트 아웃), 5주차 27-27 이후 재대결."
        },
        "football": {
            "tagline": "오늘 밤 TNF(20:15 ET): 제이든 대니얼스와 J.J. 맥카시 모두 부상 표기 해제, 메트라이프 화이트 아웃 대결.",
            "liveNow": "오늘 밤 20:15 ET: 커맨더스(대니얼스 출전, C 패트릭 결장) @ 자이언츠(맥카시/네이버스/스카테보 출전). MNF: 빌스 23-6 바이킹스.",
            "pulse": "NFL TNF 오늘 밤: 대니얼스·맥카시 나란히 출전 청신호, 5주차 27-27 연장 무승부 리턴매치",
            "keywords": "NFL 10주차, 자이언츠, 커맨더스, 제이든 대니얼스, J.J. 맥카시, TNF"
        },
        "basketball": {
            "tagline": "NBA: 하든 MSG서 32득점하며 캐벌리어스 115-107 승리 견인; 로케츠는 커리 부상 이른 이탈 속 워리어스 115-108 제압.",
            "liveNow": "수요일 결과: 캐벌리어스 115-107 닉스(하든 32, 브런슨 27); 로케츠 115-108 워리어스(커리 1Q 부상, 센군 19); 셀틱스 98-93 랩터스(-22 역전). 오늘 밤 4경기.",
            "pulse": "NBA: 하든 32점으로 MSG 접수, 커리 조기 부상 속 로케츠 승리, 보스턴 22점 차 대역전",
            "keywords": "NBA, 캐벌리어스, 닉스, 제임스 하든, 로케츠, 워리어스, 스테판 커리, 셀틱스"
        },
        "soccer": {
            "tagline": "오늘 밤 UWCL·네이션스리그 빅매치: 캄프 누 바르셀로나-아스널 및 잉글랜드-크로아티아, 전날 리옹은 유벤투스 6-0 완파.",
            "liveNow": "오늘 밤: 바르셀로나 vs 아스널(18:45 CET); 잉글랜드 vs 크로아티아(19:45 UK), 이탈리아 vs 프랑스, 체코 vs 스페인(20:45 CET). 수요일: 유벤투스 0-6 리옹.",
            "pulse": "오늘 밤 빅매치: 캄프 누 바르셀로나-아스널 & 잉글랜드-크로아티아, 전날 리옹 유벤투스 6-0 완파",
            "keywords": "UWCL, 바르셀로나, 아스널, 캄프 누, 잉글랜드, 크로아티아, 네이션스리그, 리옹"
        },
        "tennis": {
            "tagline": "토리노 파이널스 조 편성 완료: 즈베레프 매켄로 조·알카라스 렌들 조; 오늘 스톡홀름 8강 프리츠 vs 루네.",
            "liveNow": "토리노: 매켄로(즈베레프, 셸턴, 피스, 호다르); 렌들(알카라스, 메드베데프, 코볼리, 티아포). 오늘 스톡홀름 8강: 프리츠 vs 루네.",
            "pulse": "니토 ATP 파이널스 조 추첨 완료: 알카라스-즈베레프 분리, 오늘 스톡홀름 프리츠 vs 루네",
            "keywords": "니토 ATP 파이널스, 토리노, 알카라스, 즈베레프, 스톡홀름, 프리츠, 루네"
        },
        "f1": {
            "tagline": "라스베이거스 21라운드 D-7: 챔피언 안토넬리 뒤 5명이 33점 차 초박빙 순위 경쟁.",
            "liveNow": "2위 싸움: 베르스타펜 279, 러셀 262, 해밀턴 261, 르클레르 249, 노리스 246(안토넬리 390, 메르세데스 652). 21라운드: 라스베이거스(11/19-21).",
            "pulse": "21라운드 라스베이거스 카운트다운: 베르스타펜부터 노리스까지 단 33점 차",
            "keywords": "포뮬러 1, 21라운드, 라스베이거스 GP, 베르스타펜, 노리스, 안토넬리, 메르세데스"
        },
        "golf": {
            "tagline": "두바이 1R 종료: 요스트 라위텐 67타(-5) 단독 선두, 야코브 올레센 68타, 로리 매킬로이 69타 공동 3위.",
            "liveNow": "두바이 1R: 1.라위텐 -5(67); 2.올레센 -4(68); T3.매킬로이 -3(69), 페레스, 데 레오, 쇼트, 라포르타; T28.차카라 E(72).",
            "pulse": "두바이 1R: 라위텐 67타(-5) 선두, 매킬로이 69타로 차카라에 3타 우위",
            "keywords": "골프, DP 월드투어 챔피언십, 요스트 라위텐, 로리 매킬로이, 에우헤니오 차카라"
        },
        "home": {
            "tonight": "목요일 주요 경기",
            "tonightBlurb": "전날 리옹이 유벤투스를 6-0으로 꺾은 데 이어 오늘 밤 캄프 누 바르셀로나-아스널과 잉글랜드-크로아티아가 열립니다. TNF에서는 대니얼스와 맥카시가 맞붙고, 두바이 1R은 라위텐(67타)과 매킬로이(69타)가 치고 나갔습니다.",
            "plTitle": "오늘 밤 캄프 누 & 네이션스리그: 바르셀로나-아스널과 잉글랜드-크로아티아 격돌",
            "plBlurb": "프리미어리그 1위 아스널(27점)이 브라이턴(22)·맨시티(21)에 앞선 가운데 오늘 밤 UWCL 바르셀로나-아스널 및 네이션스리그 5차전 개최.",
            "f1Title": "F1 21라운드 라스베이거스 D-7: 베르스타펜(279)부터 노리스(246)까지 33점 차",
            "f1Blurb": "메르세데스(652)와 안토넬리(390)의 우승 확정 뒤 6.201km 스트립 서킷(11/19-21)에서 페라리(510)·레드불(415)·맥라렌(398) 격돌."
        },
        "pg": {
            "pinFinal": "토리노 조 편성: 매켄로(즈베레프, 셸턴, 피스, 호다르) | 렌들(알카라스, 메드베데프, 코볼리, 티아포). 오늘 스톡홀름 8강: 프리츠 vs 루네.",
            "week1Closed": "NFL 9주차 MNF: 빌스(7-1)가 미니애폴리스에서 바이킹스(6-2)를 23-6 제압.",
            "week1Sub": "쿡 107야드 1TD, 앨런 234야드, 웬츠 2INT. 오늘 밤 TNF: 커맨더스 @ 자이언츠.",
            "countdownTnf": "오늘 밤 10주차 TNF(20:15 ET): 커맨더스(대니얼스 출전, 패트릭 아웃) @ 자이언츠(맥카시 선발).",
            "gridAfterMadrid": "21라운드 전 드라이버·컨스트럭터즈 순위 · 라스베이거스 스트립(11/19-21)",
            "barsPoints": "안토넬리(390)·메르세데스(652) 챔피언; 베르스타펜 279, 러셀 262, 해밀턴 261, 르클레르 249, 노리스 246.",
            "tableAfterMonday": "프리미어리그 휴식기(10R): 아스널 27점, 브라이턴 22, 맨시티 21, 리버풀 18, 첼시 16.",
            "pinClub": "클럽 선택. 아스널 27, 브라이턴 22, 맨시티 21, 리버풀 18, 첼시·에버턴 16.",
            "plFootnote": "수요일 UWCL: 유벤투스 0-6 리옹(카토토 2골), 뢰번 1-1 코게. 오늘 밤: 바르셀로나-아스널 및 잉글랜드-크로아티아.",
            "majorsDone": "두바이 1R: 요스트 라위텐 -5(67), 야코브 올레센 -4(68), 로리 매킬로이 -3(69 공동 3위), 차카라 E(72)."
        }
    },
    "ar": {
        "common": {
            "todayDesk": "نشرة الخميس: قمة برشلونة وأرسنال في كامب نو وإنجلترا أمام كرواتيا في ويمبلي. الليلة TNF بين دانيالز وماكارثي. دبي ج1: لويتن 67، مكلروي 69.",
            "todayNfl": "الليلة TNF (8:15 م ET، Prime Video): كوماندرز (2-5-1، دانيالز جاهز، باتريك غائب) عند جاينتس (5-2-1، ماكارثي أساسي). بيلز 23-6 فايكنغز.",
            "todayTnf": "الأسبوع 10 الليلة: كوماندرز (دانيالز جاهز، باتريك ويانكوف خارج القائمة) عند جاينتس (5-2-1، وايت أوت) بعد تعادل 27-27."
        },
        "football": {
            "tagline": "الليلة TNF (8:15 م ET): جايدن دانيالز وجي جي ماكارثي جاهزان لمواجهة جاينتس وكوماندرز في ميتلايف.",
            "liveNow": "الليلة 8:15 م ET: كوماندرز (دانيالز جاهز، باتريك غائب) عند جاينتس (ماكارثي ونابرز وسكاتيبو جاهزون). MNF: بيلز 23، فايكنغز 6.",
            "pulse": "NFL الليلة: جاهزية دانيالز وماكارثي تعيد إشعال قمة ميتلايف البيضاء بعد تعادل 27-27",
            "keywords": "NFL الأسبوع 10, جاينتس, كوماندرز, جايدن دانيالز, جي جي ماكارثي"
        },
        "basketball": {
            "tagline": "NBA: هاردن يسجل 32 نقطة في نيويورك ويقود كافالييرز 115-107؛ روكتس يهزم ووريورز 115-108 بعد إصابة كوري المبكرة.",
            "liveNow": "نتائج الأربعاء: كافالييرز 115-107 نيكس (هاردن 32، برونسون 27)؛ روكتس 115-108 ووريورز (خروج كوري بالربع الأول، سينغون 19)؛ سيلتيكس 98-93 رابتورز. الليلة: 4 مباريات.",
            "pulse": "NBA: هاردن يبدع بـ32 نقطة في نيويورك، ووريورز يفقد كوري في هيوستن، وسيلتيكس يعود من -22",
            "keywords": "NBA, كافالييرز, نيكس, جيمس هاردن, روكتس, ووريورز, ستيفن كوري, سيلتيكس"
        },
        "soccer": {
            "tagline": "الليلة بدوري الأبطال ودوري الأمم: برشلونة يستضيف أرسنال في كامب نو وإنجلترا تلاقي كرواتيا بعد سداسية ليون في يوفنتوس.",
            "liveNow": "الليلة: برشلونة ضد أرسنال (18:45 CET)؛ إنجلترا ضد كرواتيا (19:45 UK)، إيطاليا ضد فرنسا والتشيك ضد إسبانيا (20:45 CET). الأربعاء: يوفنتوس 0-6 أولمبيك ليون.",
            "pulse": "قمة الليلة: برشلونة وأرسنال في كامب نو وإنجلترا ضد كرواتيا عقب سداسية ليون في يوفنتوس",
            "keywords": "دوري أبطال أوروبا للسيدات, برشلونة, أرسنال, كامب نو, إنجلترا, كرواتيا, ليون"
        },
        "tennis": {
            "tagline": "قرعة نهائيات تورينو: زفيريف على رأس ماكنرو وألكاراز على رأس ليندل؛ اليوم فريتز ضد رونه في ربع نهائي ستوكهولم.",
            "liveNow": "تورينو: ماكنرو (زفيريف، شيلتون، فيلس، جودار)؛ ليندل (ألكاراز، ميدفيديف، كوبولي، تيافو). ستوكهولم اليوم: فريتز ضد رونه.",
            "pulse": "قرعة نهائيات ATP في تورينو: فصل ألكاراز وزفيريف قبل مواجهة فريتز ورونه اليوم في ستوكهولم",
            "keywords": "نهائيات ATP, قرعة تورينو, ألكاراز, زفيريف, ستوكهولم, فريتز, رونه"
        },
        "f1": {
            "tagline": "أسبوع واحد على الجولة 21 في لاس فيغاس: خمسة سائقين في 33 نقطة خلف البطل أنطونيلي.",
            "liveNow": "سباق الوصافة: فيرستابن 279، راسل 262، هاميلتون 261، لوكلير 249، نوريس 246 (أنطونيلي 390؛ مرسيدس 652). الجولة 21: لاس فيغاس (19-21 نوفمبر).",
            "pulse": "العد التنازلي للجولة 21 في لاس فيغاس: 33 نقطة تفصل فيرستابن عن نوريس خلف أنطونيلي",
            "keywords": "فورمولا 1, الجولة 21, لاس فيغاس, فيرستابن, نوريس, أنطونيلي, مرسيدس"
        },
        "golf": {
            "tagline": "دبي الجولة الأولى: يوست لويتن يتصدر بـ67 ضربة (-5) أمام ياكوب سكوف أوليسن (68) وروري مكلروي (69).",
            "liveNow": "دبي ج1: 1. يوست لويتن -5 (67)؛ 2. أوليسن -4 (68)؛ T3. مكلروي -3 (69)، بيريز، دي ليو، شوت، لابورتا؛ T28. تشاكارا E (72).",
            "pulse": "دبي الجولة الأولى: لويتن في الصدارة بـ67 ضربة ومكلروي يتفوق على تشاكارا بثلاث ضربات",
            "keywords": "غولف, بطولة جولة دي بي ورلد, يوست لويتن, روري مكلروي, يوجينيو تشاكارا"
        },
        "home": {
            "tonight": "أحداث الخميس",
            "tonightBlurb": "برشلونة يستضيف أرسنال في كامب نو وإنجلترا تلاقي كرواتيا بعد فوز ليون 6-0 على يوفنتوس. الليلة مواجهة دانيالز وماكارثي في NFL، ولويتن (67) يتصدر دبي أمام مكلروي (69) مع تحديد مجموعات تورينو.",
            "plTitle": "كامب نو ودوري الأمم الليلة: برشلونة ضد أرسنال وإنجلترا ضد كرواتيا بعد سداسية ليون",
            "plBlurb": "أرسنال يحافظ على صدارة البريميرليغ (27 مقابل برايتون 22 وسيتي 21). الليلة: برشلونة ضد أرسنال (18:45) وقمتا إنجلترا وكرواتيا وإيطاليا وفرنسا.",
            "f1Title": "العد التنازلي للجولة 21 في لاس فيغاس: 33 نقطة من فيرستابن (279) إلى نوريس (246)",
            "f1Blurb": "مرسيدس (652) وأنطونيلي (390) بطلان قبل حلبة 6.201 كلم (19-21 نوفمبر)، وفيراري (510) وريد بول (415) ومكلارين (398) في المطاردة."
        },
        "pg": {
            "pinFinal": "مجموعات تورينو: ماكنرو (زفيريف، شيلتون، فيلس، جودار) | ليندل (ألكاراز، ميدفيديف، كوبولي، تيافو). ستوكهولم اليوم: فريتز ضد رونه.",
            "week1Closed": "NFL الأسبوع 9 MNF: بيلز (7-1) يهزم فايكنغز (6-2) 23-6 في مينيابوليس.",
            "week1Sub": "كوك 107 ياردات وTD؛ ألن 234 ياردة؛ وينتز اعتراضان. الليلة TNF: كوماندرز عند جاينتس.",
            "countdownTnf": "الليلة الأسبوع 10 TNF (8:15 م ET): كوماندرز (دانيالز جاهز، باتريك غائب) عند جاينتس (ماكارثي جاهز).",
            "gridAfterMadrid": "الترتيب قبل الجولة 21 · لاس فيغاس ستريب (19-21 نوفمبر)",
            "barsPoints": "أنطونيلي (390) ومرسيدس (652) بطلان؛ فيرستابن 279، راسل 262، هاميلتون 261، لوكلير 249، نوريس 246.",
            "tableAfterMonday": "توقف البريميرليغ (الجولة 10): أرسنال 27، برايتون 22، مان سيتي 21، ليفربول 18، تشيلسي 16.",
            "pinClub": "اختر ناديا. أرسنال 27، برايتون 22، سيتي 21، ليفربول 18، تشيلسي وإيفرتون 16.",
            "plFootnote": "الأربعاء UWCL: يوفنتوس 0-6 أولمبيك ليون (كاتوتو 2)؛ لوفين 1-1 كوغه. الليلة: برشلونة ضد أرسنال وإنجلترا ضد كرواتيا.",
            "majorsDone": "دبي ج1: لويتن -5 (67)، أوليسن -4 (68)، مكلروي -3 (69، الثالث مكرر)، تشاكارا E (72)."
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
    c_close = re.search(r"\r?\n  \},", content[c_idx:])
    assert c_close is not None, f"common end not found in {lang}"
    c_end = c_idx + c_close.start()
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
    h_close = re.search(r"\r?\n  \}(?:,)?", content[h_idx:])
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
        pattern = rf'("{lang}":\s*\{{)([\s\S]*?)(\r?\n  \}},|\r?\n  \}})'
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

    print("All 10-locale UI updates for 12 Nov 2026 completed successfully!")

