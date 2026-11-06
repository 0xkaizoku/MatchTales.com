#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update playground.ts, messages.ts, and all messages-*.ts files for 6 November 2026."""
import re
import os

DATA = {
    "en": {
        "football": {
            "tagline": "NFL Week 9 TNF: Jaguars thrash depleted Ravens 33-10 behind Lawrence, four Little field goals.",
            "liveNow": "Final in Baltimore: Jaguars 33, Ravens 10. Lawrence 242 yds, 50-yd TD; Little 4 FGs; Fagnano 2 INT. Jaguars 6-2, Ravens 4-5.",
            "pulse": "NFL WEEK 9 TNF: JACKSONVILLE JAGUARS THRASH RAVENS 33-10; JAGUARS 6-2, RAVENS 4-5",
            "keywords": "NFL Week 9, Jacksonville Jaguars, Baltimore Ravens, Trevor Lawrence, Cam Little, Joe Fagnano, TNF"
        },
        "basketball": {
            "tagline": "NBA: Wembanyama posts 52 points, 24 rebounds, 8 blocks as Spurs edge Mavericks 112-111.",
            "liveNow": "Final in San Antonio: Spurs 112, Mavericks 111. Wembanyama 52-24-8; winning FT 24.2s. Spurs 6-2. Cavs are 4-4.",
            "pulse": "NBA: WEMBANYAMA 52-24-8 AS SPURS EDGE MAVERICKS 112-111 FOR SIXTH STRAIGHT",
            "keywords": "NBA, Spurs, Mavericks, Wembanyama, Irving, Harper, Frost Bank Center"
        },
        "soccer": {
            "tagline": "UCL MD4: Haaland winner as Manchester City edge RB Leipzig 3-2. Arsenal lead Premier League on 24 points.",
            "liveNow": "Final in Leipzig: RB Leipzig 2-3 Manchester City (Lukeba OG 37, Baku 49, Fernandez 58, Nusa 61, Haaland 78). City 3-1, 7th in UCL.",
            "pulse": "UCL MD4: HAALAND 78TH-MINUTE WINNER LIFTS CITY PAST LEIPZIG 3-2; ARSENAL LEAD PL ON 24",
            "keywords": "Champions League, Manchester City, RB Leipzig, Haaland, Arsenal, Premier League"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters QF: Ben Shelton beats Tommy Paul 6-4, 4-6, 6-3 to reach first Bercy semi-final.",
            "liveNow": "Paris Masters QF: Shelton def. Paul 6-4, 4-6, 6-3 in 1h46m, 19 aces. Tiafoe qualifies for Turin; Paul is out.",
            "pulse": "ROLEX PARIS MASTERS: BEN SHELTON BEATS TOMMY PAUL TO REACH FIRST BERCY SEMI-FINAL",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Tommy Paul, Accor Arena, ATP Finals"
        },
        "f1": {
            "tagline": "São Paulo GP FP1: Lando Norris leads Kimi Antonelli and Max Verstappen at Interlagos.",
            "liveNow": "FP1: Norris 1:11.717, Antonelli +0.082s, Verstappen +0.236s. No Sprint. Mercedes 630, Ferrari 504 after Mexico.",
            "pulse": "F1 INTERLAGOS FP1: NORRIS LEADS ANTONELLI; NO SPRINT; MERCEDES 630, FERRARI 504",
            "keywords": "Formula 1, São Paulo GP, Interlagos, Norris, Antonelli, Verstappen, Mercedes, Ferrari"
        },
        "golf": {
            "tagline": "WWT Championship Round 1: Chris Kirk fires bogey-free 63 to lead by one at El Cardonal.",
            "liveNow": "R1 complete: Kirk 63 leads Dunlap and Blair 64. Purse $6 million. Round 2 in progress, unpublished as final.",
            "pulse": "PGA TOUR CABO R1: CHRIS KIRK 63 LEADS WWT CHAMPIONSHIP; FEDEXCUP FALL CARDS ON THE LINE",
            "keywords": "PGA Tour, WWT Championship, Chris Kirk, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Friday desk",
            "tonightBlurb": "Jaguars thrash Ravens 33-10 on TNF. Wembanyama 52-24-8 as Spurs edge Mavs. Haaland winner in Leipzig. Shelton into Paris SF. Norris leads Interlagos FP1. Kirk 63 in Cabo.",
            "plTitle": "NFL Week 9 TNF: Jaguars thrash depleted Ravens 33-10 behind Lawrence",
            "plBlurb": "Trevor Lawrence throws for 242 yards and a 50-yard touchdown as Jacksonville forces three turnovers. Jaguars 6-2, Ravens 4-5.",
            "f1Title": "NBA: Wembanyama posts 52 points, 24 rebounds, 8 blocks as Spurs edge Mavericks 112-111",
            "f1Blurb": "First 50-20-5 block night since McAdoo in 1974. Winning free throw with 24.2 seconds left. Spurs 6-2. Cavs are 4-4."
        },
        "pg": {
            "pinFinal": "NFL Week 9 TNF: Jaguars 33, Ravens 10. Lawrence 242 yds, Little 4 FGs, Fagnano 2 INT.",
            "week1Closed": "NFL Week 9 TNF: Jaguars beat Ravens 33-10 to improve to 6-2. Ravens 4-5.",
            "week1Sub": "Lawrence 50-yd TD to Washington. Little 4 FGs. Steelers still 6-2 in AFC North.",
            "countdownTnf": "Week 9 TNF final: Jaguars 33, Ravens 10. Next: JAX at TEN Nov 15.",
            "barsPoints": "Mercedes lead Constructors with 630 pts, 126 ahead of Ferrari (504). No Sprint in São Paulo.",
            "tableAfterMonday": "Premier League after MW9: Arsenal 24, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "pinClub": "Select a club. Arsenal lead on 24, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "plFootnote": "PL MW9: Arsenal 1-0 Liverpool, Brighton 1-0 City, Chelsea 2-0 Man Utd, Everton 1-0 Newcastle. Next: Everton vs Coventry Fri 20:00 GMT.",
            "majorsDone": "PGA Tour: Chris Kirk 63 leads WWT Championship R1 at El Cardonal; Dunlap and Blair 64. Purse $6 million."
        }
    },
    "fr": {
        "football": {
            "tagline": "NFL Semaine 9 TNF : Les Jaguars ecrasent les Ravens 33-10, Lawrence et quatre field goals de Little.",
            "liveNow": "Score final a Baltimore : Jaguars 33, Ravens 10. Lawrence 242 yds, TD de 50 yds ; Little 4 FG ; Fagnano 2 INT. Jaguars 6-2, Ravens 4-5.",
            "pulse": "NFL SEMAINE 9 TNF : LES JACKSONVILLE JAGUARS ECRASENT LES RAVENS 33-10 ; JAGUARS 6-2, RAVENS 4-5",
            "keywords": "NFL Semaine 9, Jacksonville Jaguars, Baltimore Ravens, Trevor Lawrence, Cam Little, Joe Fagnano"
        },
        "basketball": {
            "tagline": "NBA : Wembanyama compile 52 points, 24 rebonds et 8 contres, les Spurs battent les Mavericks 112-111.",
            "liveNow": "Fin de match a San Antonio : Spurs 112, Mavericks 111. Wembanyama 52-24-8 ; lancer franc a 24,2s. Spurs 6-2. Cavs a 4-4.",
            "pulse": "NBA : WEMBANYAMA 52-24-8, LES SPURS BATTENT LES MAVERICKS 112-111 POUR UN SIXIEME SUCCES D'AFFILEE",
            "keywords": "NBA, Spurs, Mavericks, Wembanyama, Irving, Harper"
        },
        "soccer": {
            "tagline": "Ligue des champions J4 : Haaland offre le succes a Manchester City 3-2 a Leipzig. Arsenal mene la Premier League a 24 pts.",
            "liveNow": "Fin de match a Leipzig : RB Leipzig 2-3 Manchester City (Lukeba CSC 37, Baku 49, Fernandez 58, Nusa 61, Haaland 78). City 3-1, 7e.",
            "pulse": "C1 J4 : HAALAND A LA 78E OFFRE LE 3-2 A CITY CONTRE LEIPZIG ; ARSENAL MENE LA PL A 24 PTS",
            "keywords": "Ligue des champions, Manchester City, RB Leipzig, Haaland, Arsenal, Premier League"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters QF : Ben Shelton bat Tommy Paul 6-4, 4-6, 6-3 et rejoint sa premiere demi a Bercy.",
            "liveNow": "Paris Masters QF : Shelton bat Paul 6-4, 4-6, 6-3 en 1h46, 19 aces. Tiafoe qualifie pour Turin ; Paul elimine.",
            "pulse": "ROLEX PARIS MASTERS : BEN SHELTON BATTIT TOMMY PAUL ET REJOINT SA PREMIERE DEMI A BERCY",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Tommy Paul, Accor Arena"
        },
        "f1": {
            "tagline": "GP de São Paulo EL1 : Lando Norris devance Kimi Antonelli et Max Verstappen a Interlagos.",
            "liveNow": "EL1 : Norris 1:11.717, Antonelli +0,082s, Verstappen +0,236s. Pas de Sprint. Mercedes 630, Ferrari 504 apres Mexico.",
            "pulse": "F1 INTERLAGOS EL1 : NORRIS DEVANT ANTONELLI ; PAS DE SPRINT ; MERCEDES 630, FERRARI 504",
            "keywords": "Formule 1, GP de São Paulo, Interlagos, Norris, Antonelli, Verstappen"
        },
        "golf": {
            "tagline": "WWT Championship 1er tour : Chris Kirk signe un 63 sans bogey et mene d'un coup a El Cardonal.",
            "liveNow": "T1 termine : Kirk 63 devant Dunlap et Blair 64. Bourse 6 millions de dollars. 2e tour en cours, non publie.",
            "pulse": "PGA TOUR CABO T1 : CHRIS KIRK 63 EN TETE DU WWT CHAMPIONSHIP ; CARTES FEDEXCUP FALL EN JEU",
            "keywords": "PGA Tour, WWT Championship, Chris Kirk, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Desk du vendredi",
            "tonightBlurb": "Les Jaguars ecrasent les Ravens 33-10. Wembanyama 52-24-8. Haaland vainqueur a Leipzig. Shelton en demi a Paris. Norris en tete des EL1. Kirk 63 a Cabo.",
            "plTitle": "NFL Semaine 9 TNF : Les Jaguars ecrasent les Ravens 33-10 portes par Lawrence",
            "plBlurb": "Trevor Lawrence lance pour 242 yards et un TD de 50 yards. Jacksonville provoque trois turnovers. Jaguars 6-2, Ravens 4-5.",
            "f1Title": "NBA : Wembanyama compile 52 points, 24 rebonds, 8 contres, les Spurs battent Dallas 112-111",
            "f1Blurb": "Premier 50-20-5 contres depuis McAdoo en 1974. Lancer franc a 24,2s. Spurs 6-2. Cavs a 4-4."
        },
        "pg": {
            "pinFinal": "NFL Semaine 9 TNF : Jaguars 33, Ravens 10. Lawrence 242 yds, Little 4 FG, Fagnano 2 INT.",
            "week1Closed": "NFL Semaine 9 TNF : Les Jaguars battent les Ravens 33-10 et passent a 6-2. Ravens 4-5.",
            "week1Sub": "Lawrence TD de 50 yds pour Washington. Little 4 FG. Les Steelers restent 6-2 en AFC Nord.",
            "countdownTnf": "TNF Semaine 9 : Jaguars 33, Ravens 10. Suite : JAX a TEN le 15 novembre.",
            "barsPoints": "Mercedes mene chez les constructeurs avec 630 pts, 126 d'avance sur Ferrari (504). Pas de Sprint a São Paulo.",
            "tableAfterMonday": "Premier League apres la J9 : Arsenal 24, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "pinClub": "Choisissez un club. Arsenal mene a 24 pts, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "plFootnote": "PL J9 : Arsenal 1-0 Liverpool, Brighton 1-0 City, Chelsea 2-0 Man Utd, Everton 1-0 Newcastle. Suite : Everton-Coventry ven. 20h GMT.",
            "majorsDone": "PGA Tour : Chris Kirk 63 en tete du WWT Championship T1 a El Cardonal ; Dunlap et Blair 64. Bourse 6 M$."
        }
    },
    "es": {
        "football": {
            "tagline": "NFL Semana 9 TNF: Los Jaguars golean 33-10 a los Ravens con Lawrence y cuatro goles de campo de Little.",
            "liveNow": "Final en Baltimore: Jaguars 33, Ravens 10. Lawrence 242 yardas, TD de 50; Little 4 FG; Fagnano 2 INT. Jaguars 6-2, Ravens 4-5.",
            "pulse": "NFL SEMANA 9 TNF: JACKSONVILLE JAGUARS GOLEAN 33-10 A RAVENS; JAGUARS 6-2, RAVENS 4-5",
            "keywords": "NFL Semana 9, Jacksonville Jaguars, Baltimore Ravens, Trevor Lawrence, Cam Little, Joe Fagnano"
        },
        "basketball": {
            "tagline": "NBA: Wembanyama anota 52 puntos, 24 rebotes y 8 tapones y los Spurs ganan 112-111 a Dallas.",
            "liveNow": "Final en San Antonio: Spurs 112, Mavericks 111. Wembanyama 52-24-8; tiro libre a 24,2s. Spurs 6-2. Cavs 4-4.",
            "pulse": "NBA: WEMBANYAMA 52-24-8 Y LOS SPURS GANAN 112-111 A MAVERICKS, SEXTA SEGUIDA",
            "keywords": "NBA, Spurs, Mavericks, Wembanyama, Irving, Harper"
        },
        "soccer": {
            "tagline": "UCL J4: Haaland da el 3-2 al Manchester City en Leipzig. Arsenal lidera la Premier con 24 puntos.",
            "liveNow": "Final en Leipzig: RB Leipzig 2-3 Manchester City (Lukeba PP 37, Baku 49, Fernandez 58, Nusa 61, Haaland 78). City 3-1, 7o.",
            "pulse": "UCL J4: HAALAND EN EL 78 DA EL 3-2 AL CITY EN LEIPZIG; ARSENAL LIDER DE LA PREMIER CON 24",
            "keywords": "Champions, Manchester City, RB Leipzig, Haaland, Arsenal, Premier League"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters CF: Ben Shelton vence a Tommy Paul 6-4, 4-6, 6-3 y alcanza su primera semifinal en Bercy.",
            "liveNow": "Paris Masters CF: Shelton gana 6-4, 4-6, 6-3 en 1h46, 19 aces. Tiafoe se clasifica para Turin; Paul fuera.",
            "pulse": "ROLEX PARIS MASTERS: BEN SHELTON VENCE A TOMMY PAUL Y JUEGA SU PRIMERA SEMIFINAL EN BERCY",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Tommy Paul, Accor Arena"
        },
        "f1": {
            "tagline": "GP de São Paulo EL1: Lando Norris lidera a Kimi Antonelli y Max Verstappen en Interlagos.",
            "liveNow": "EL1: Norris 1:11.717, Antonelli +0.082s, Verstappen +0.236s. Sin Sprint. Mercedes 630, Ferrari 504 tras Mexico.",
            "pulse": "F1 INTERLAGOS EL1: NORRIS LIDER; SIN SPRINT; MERCEDES 630, FERRARI 504",
            "keywords": "Formula 1, GP de São Paulo, Interlagos, Norris, Antonelli, Verstappen"
        },
        "golf": {
            "tagline": "WWT Championship R1: Chris Kirk firma un 63 sin bogeys y lidera de un golpe en El Cardonal.",
            "liveNow": "R1 cerrado: Kirk 63 lidera a Dunlap y Blair 64. Bote de 6 millones. R2 en juego, no publicado como final.",
            "pulse": "PGA TOUR CABO R1: CHRIS KIRK 63 LIDER DEL WWT CHAMPIONSHIP; TARJETAS FEDEXCUP FALL EN JUEGO",
            "keywords": "PGA Tour, WWT Championship, Chris Kirk, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Desk del viernes",
            "tonightBlurb": "Jaguars golean 33-10 a Ravens. Wembanyama 52-24-8. Haaland gana en Leipzig. Shelton a semifinales en Paris. Norris manda en EL1. Kirk 63 en Cabo.",
            "plTitle": "NFL Semana 9 TNF: Los Jaguars golean 33-10 a los Ravens con Lawrence",
            "plBlurb": "Trevor Lawrence lanza para 242 yardas y un TD de 50. Jacksonville fuerza tres perdidas. Jaguars 6-2, Ravens 4-5.",
            "f1Title": "NBA: Wembanyama 52 puntos, 24 rebotes y 8 tapones, Spurs 112-111 a Dallas",
            "f1Blurb": "Primer 50-20-5 tapones desde McAdoo en 1974. Tiro libre a 24,2s. Spurs 6-2. Cavs 4-4."
        },
        "pg": {
            "pinFinal": "NFL Semana 9 TNF: Jaguars 33, Ravens 10. Lawrence 242 yd, Little 4 FG, Fagnano 2 INT.",
            "week1Closed": "NFL Semana 9 TNF: Jaguars vencen 33-10 a Ravens y suben a 6-2. Ravens 4-5.",
            "week1Sub": "Lawrence TD de 50 a Washington. Little 4 FG. Steelers siguen 6-2 en AFC Norte.",
            "countdownTnf": "TNF Semana 9: Jaguars 33, Ravens 10. Siguiente: JAX en TEN el 15 de noviembre.",
            "barsPoints": "Mercedes lidera constructores con 630 pts, 126 sobre Ferrari (504). Sin Sprint en São Paulo.",
            "tableAfterMonday": "Premier League tras la J9: Arsenal 24, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "pinClub": "Elige un club. Arsenal lidera con 24, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "plFootnote": "PL J9: Arsenal 1-0 Liverpool, Brighton 1-0 City, Chelsea 2-0 Man Utd, Everton 1-0 Newcastle. Siguiente: Everton-Coventry vie 20:00 GMT.",
            "majorsDone": "PGA Tour: Chris Kirk 63 lidera el WWT Championship R1 en El Cardonal; Dunlap y Blair 64. Bote 6 M$."
        }
    },
    "de": {
        "football": {
            "tagline": "NFL Woche 9 TNF: Jaguars demontieren die Ravens 33:10, Lawrence und vier Field Goals von Little.",
            "liveNow": "Ende in Baltimore: Jaguars 33, Ravens 10. Lawrence 242 Yards, 50-Yard-TD; Little 4 FG; Fagnano 2 INT. Jaguars 6-2, Ravens 4-5.",
            "pulse": "NFL WOCHE 9 TNF: JACKSONVILLE JAGUARS DEMONTIEREN RAVENS 33:10; JAGUARS 6-2, RAVENS 4-5",
            "keywords": "NFL Woche 9, Jacksonville Jaguars, Baltimore Ravens, Trevor Lawrence, Cam Little, Joe Fagnano"
        },
        "basketball": {
            "tagline": "NBA: Wembanyama mit 52 Punkten, 24 Rebounds, 8 Blocks, Spurs schlagen Mavericks 112:111.",
            "liveNow": "Ende in San Antonio: Spurs 112, Mavericks 111. Wembanyama 52-24-8; Freiwurf bei 24,2s. Spurs 6-2. Cavs 4-4.",
            "pulse": "NBA: WEMBANYAMA 52-24-8, SPURS SCHLAGEN MAVERICKS 112:111 ZUM SECHSTEN SIEG IN FOLGE",
            "keywords": "NBA, Spurs, Mavericks, Wembanyama, Irving, Harper"
        },
        "soccer": {
            "tagline": "CL MD4: Haaland entscheidet 3:2 fuer Manchester City in Leipzig. Arsenal fuehrt die Premier League mit 24 Punkten.",
            "liveNow": "Ende in Leipzig: RB Leipzig 2:3 Manchester City (Lukeba ET 37, Baku 49, Fernandez 58, Nusa 61, Haaland 78). City 3-1, Rang 7.",
            "pulse": "CL MD4: HAALAND IN DER 78. MINUTE ENTSCHEIDET 3:2 IN LEIPZIG; ARSENAL FUEHRT PL MIT 24",
            "keywords": "Champions League, Manchester City, RB Leipzig, Haaland, Arsenal, Premier League"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters VF: Ben Shelton schlaegt Tommy Paul 6:4, 4:6, 6:3 und erreicht sein erstes Halbfinale in Bercy.",
            "liveNow": "Paris Masters VF: Shelton siegt 6:4, 4:6, 6:3 in 1:46h, 19 Asse. Tiafoe ist in Turin dabei; Paul ausgeschieden.",
            "pulse": "ROLEX PARIS MASTERS: BEN SHELTON SCHLAEGT TOMMY PAUL UND STEHT IM ERSTEN BERCY-HALBFINALE",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Tommy Paul, Accor Arena"
        },
        "f1": {
            "tagline": "Sao-Paulo-GP FP1: Lando Norris vor Kimi Antonelli und Max Verstappen in Interlagos.",
            "liveNow": "FP1: Norris 1:11.717, Antonelli +0,082s, Verstappen +0,236s. Kein Sprint. Mercedes 630, Ferrari 504 nach Mexiko.",
            "pulse": "F1 INTERLAGOS FP1: NORRIS VOR ANTONELLI; KEIN SPRINT; MERCEDES 630, FERRARI 504",
            "keywords": "Formel 1, Sao-Paulo-GP, Interlagos, Norris, Antonelli, Verstappen"
        },
        "golf": {
            "tagline": "WWT Championship Runde 1: Chris Kirk spielt ein bogeyfreies 63 und fuehrt um einen Schlag in El Cardonal.",
            "liveNow": "R1 fertig: Kirk 63 vor Dunlap und Blair 64. Preisgeld 6 Millionen Dollar. Runde 2 laeuft, nicht als Finalstand.",
            "pulse": "PGA TOUR CABO R1: CHRIS KIRK 63 FUEHRT WWT CHAMPIONSHIP; FEDEXCUP-FALL-KARTEN AUF DER LINIE",
            "keywords": "PGA Tour, WWT Championship, Chris Kirk, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Freitag-Desk",
            "tonightBlurb": "Jaguars demontieren Ravens 33:10. Wembanyama 52-24-8. Haaland siegt in Leipzig. Shelton im Paris-HF. Norris fuehrt FP1. Kirk 63 in Cabo.",
            "plTitle": "NFL Woche 9 TNF: Jaguars demontieren Ravens 33:10 mit Lawrence",
            "plBlurb": "Trevor Lawrence wirft 242 Yards und einen 50-Yard-TD. Jacksonville erzwingt drei Ballverluste. Jaguars 6-2, Ravens 4-5.",
            "f1Title": "NBA: Wembanyama 52 Punkte, 24 Rebounds, 8 Blocks, Spurs 112:111 gegen Dallas",
            "f1Blurb": "Erstes 50-20-5-Blocks-Spiel seit McAdoo 1974. Freiwurf bei 24,2s. Spurs 6-2. Cavs 4-4."
        },
        "pg": {
            "pinFinal": "NFL Woche 9 TNF: Jaguars 33, Ravens 10. Lawrence 242 Yards, Little 4 FG, Fagnano 2 INT.",
            "week1Closed": "NFL Woche 9 TNF: Jaguars schlagen Ravens 33:10 und stehen 6-2. Ravens 4-5.",
            "week1Sub": "Lawrence 50-Yard-TD an Washington. Little 4 FG. Steelers weiter 6-2 in der AFC North.",
            "countdownTnf": "TNF Woche 9: Jaguars 33, Ravens 10. Weiter: JAX in TEN am 15. November.",
            "barsPoints": "Mercedes fuehrt die Konstrukteurs-WM mit 630 Punkten, 126 vor Ferrari (504). Kein Sprint in Sao Paulo.",
            "tableAfterMonday": "Premier League nach MW9: Arsenal 24, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "pinClub": "Club waehlen. Arsenal fuehrt mit 24, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "plFootnote": "PL MW9: Arsenal 1:0 Liverpool, Brighton 1:0 City, Chelsea 2:0 Man Utd, Everton 1:0 Newcastle. Weiter: Everton gegen Coventry Fr 20:00 GMT.",
            "majorsDone": "PGA Tour: Chris Kirk 63 fuehrt WWT Championship R1 in El Cardonal; Dunlap und Blair 64. Preisgeld 6 Mio. Dollar."
        }
    },
    "it": {
        "football": {
            "tagline": "NFL Week 9 TNF: i Jaguars travolgono i Ravens 33-10 con Lawrence e quattro field goal di Little.",
            "liveNow": "Finale a Baltimore: Jaguars 33, Ravens 10. Lawrence 242 yard, TD da 50; Little 4 FG; Fagnano 2 INT. Jaguars 6-2, Ravens 4-5.",
            "pulse": "NFL WEEK 9 TNF: JACKSONVILLE JAGUARS TRAVOLGONO I RAVENS 33-10; JAGUARS 6-2, RAVENS 4-5",
            "keywords": "NFL Week 9, Jacksonville Jaguars, Baltimore Ravens, Trevor Lawrence, Cam Little, Joe Fagnano"
        },
        "basketball": {
            "tagline": "NBA: Wembanyama 52 punti, 24 rimbalzi, 8 stoppate, gli Spurs battono i Mavericks 112-111.",
            "liveNow": "Finale a San Antonio: Spurs 112, Mavericks 111. Wembanyama 52-24-8; libero a 24,2s. Spurs 6-2. Cavs 4-4.",
            "pulse": "NBA: WEMBANYAMA 52-24-8, GLI SPURS BATTERONO I MAVERICKS 112-111, SESTA DI FILA",
            "keywords": "NBA, Spurs, Mavericks, Wembanyama, Irving, Harper"
        },
        "soccer": {
            "tagline": "UCL GS4: Haaland decide 3-2 per il Manchester City a Lipsia. Arsenal in testa alla Premier con 24 punti.",
            "liveNow": "Finale a Lipsia: RB Lipsia 2-3 Manchester City (Lukeba aut. 37, Baku 49, Fernandez 58, Nusa 61, Haaland 78). City 3-1, 7i.",
            "pulse": "UCL GS4: HAALAND AL 78' REGALA IL 3-2 AL CITY A LIPSIA; ARSENAL PRIMO IN PREMIER CON 24",
            "keywords": "Champions, Manchester City, RB Lipsia, Haaland, Arsenal, Premier League"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters QF: Ben Shelton batte Tommy Paul 6-4, 4-6, 6-3 e vola in semifinale a Bercy per la prima volta.",
            "liveNow": "Paris Masters QF: Shelton vince 6-4, 4-6, 6-3 in 1h46, 19 ace. Tiafoe qualificato a Torino; Paul fuori.",
            "pulse": "ROLEX PARIS MASTERS: BEN SHELTON BATTE TOMMY PAUL E RAGGIUNGE LA PRIMA SEMIFINALE A BERCY",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Tommy Paul, Accor Arena"
        },
        "f1": {
            "tagline": "GP di São Paulo PL1: Lando Norris precede Kimi Antonelli e Max Verstappen a Interlagos.",
            "liveNow": "PL1: Norris 1:11.717, Antonelli +0.082s, Verstappen +0.236s. Niente Sprint. Mercedes 630, Ferrari 504 dopo Città del Messico.",
            "pulse": "F1 INTERLAGOS PL1: NORRIS DAVANTI AD ANTONELLI; NIENTE SPRINT; MERCEDES 630, FERRARI 504",
            "keywords": "Formula 1, GP di São Paulo, Interlagos, Norris, Antonelli, Verstappen"
        },
        "golf": {
            "tagline": "WWT Championship 1o giro: Chris Kirk chiude 63 senza bogey e guida di un colpo a El Cardonal.",
            "liveNow": "R1 chiuso: Kirk 63 davanti a Dunlap e Blair 64. Montepremi 6 milioni. R2 in corso, non pubblicato come finale.",
            "pulse": "PGA TOUR CABO R1: CHRIS KIRK 63 IN TESTA AL WWT CHAMPIONSHIP; CARD FEDEXCUP FALL IN PALIO",
            "keywords": "PGA Tour, WWT Championship, Chris Kirk, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Desk del venerdi",
            "tonightBlurb": "Jaguars travolgono i Ravens 33-10. Wembanyama 52-24-8. Haaland vince a Lipsia. Shelton in semifinale a Parigi. Norris in testa in PL1. Kirk 63 a Cabo.",
            "plTitle": "NFL Week 9 TNF: i Jaguars travolgono i Ravens 33-10 con Lawrence",
            "plBlurb": "Trevor Lawrence lancia per 242 yard e un TD da 50. Jacksonville forza tre palloni persi. Jaguars 6-2, Ravens 4-5.",
            "f1Title": "NBA: Wembanyama 52 punti, 24 rimbalzi, 8 stoppate, Spurs 112-111 su Dallas",
            "f1Blurb": "Primo 50-20-5 stoppate da McAdoo nel 1974. Libero a 24,2s. Spurs 6-2. Cavs 4-4."
        },
        "pg": {
            "pinFinal": "NFL Week 9 TNF: Jaguars 33, Ravens 10. Lawrence 242 yard, Little 4 FG, Fagnano 2 INT.",
            "week1Closed": "NFL Week 9 TNF: i Jaguars battono i Ravens 33-10 e salgono a 6-2. Ravens 4-5.",
            "week1Sub": "Lawrence TD da 50 a Washington. Little 4 FG. Steelers ancora 6-2 in AFC North.",
            "countdownTnf": "TNF Week 9: Jaguars 33, Ravens 10. Prossimo: JAX a TEN il 15 novembre.",
            "barsPoints": "Mercedes guida i Costruttori con 630 punti, 126 su Ferrari (504). Niente Sprint a São Paulo.",
            "tableAfterMonday": "Premier League dopo la 9a: Arsenal 24, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "pinClub": "Scegli un club. Arsenal primo a 24, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "plFootnote": "PL 9a: Arsenal 1-0 Liverpool, Brighton 1-0 City, Chelsea 2-0 Man Utd, Everton 1-0 Newcastle. Prossimo: Everton-Coventry ven 20:00 GMT.",
            "majorsDone": "PGA Tour: Chris Kirk 63 guida il WWT Championship R1 a El Cardonal; Dunlap e Blair 64. Montepremi 6 milioni."
        }
    },
    "pl": {
        "football": {
            "tagline": "NFL tydzien 9 TNF: Jaguars rozbijaja Ravens 33:10, Lawrence i cztery field goale Little'a.",
            "liveNow": "Koniec w Baltimore: Jaguars 33, Ravens 10. Lawrence 242 jardy, TD z 50; Little 4 FG; Fagnano 2 INT. Jaguars 6-2, Ravens 4-5.",
            "pulse": "NFL TYDZIEN 9 TNF: JACKSONVILLE JAGUARS ROZBIJAJA RAVENS 33:10; JAGUARS 6-2, RAVENS 4-5",
            "keywords": "NFL tydzien 9, Jacksonville Jaguars, Baltimore Ravens, Trevor Lawrence, Cam Little, Joe Fagnano"
        },
        "basketball": {
            "tagline": "NBA: Wembanyama 52 punkty, 24 zbiorki, 8 blokow, Spurs wygrywaja z Mavericks 112:111.",
            "liveNow": "Koniec w San Antonio: Spurs 112, Mavericks 111. Wembanyama 52-24-8; rzut wolny przy 24,2s. Spurs 6-2. Cavs 4-4.",
            "pulse": "NBA: WEMBANYAMA 52-24-8, SPURS WYGRYWAJA 112:111 Z MAVERICKS, SZOSTA Z RZEDU",
            "keywords": "NBA, Spurs, Mavericks, Wembanyama, Irving, Harper"
        },
        "soccer": {
            "tagline": "LM kolejka 4: Haaland daje City wygrana 3:2 w Lipsku. Arsenal liderem Premier League z 24 punktami.",
            "liveNow": "Koniec w Lipsku: RB Lipsk 2:3 Manchester City (Lukeba sam. 37, Baku 49, Fernandez 58, Nusa 61, Haaland 78). City 3-1, 7. miejsce.",
            "pulse": "LM KOLEJKA 4: HAALAND W 78. MINUCIE DAJE CITY 3:2 W LIPSKU; ARSENAL LIDEREM PL Z 24",
            "keywords": "Liga Mistrzow, Manchester City, RB Lipsk, Haaland, Arsenal, Premier League"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters CF: Ben Shelton pokonuje Tommy'ego Paula 6:4, 4:6, 6:3 i gra pierwszy polfinal w Bercy.",
            "liveNow": "Paris Masters CF: Shelton wygrywa 6:4, 4:6, 6:3 w 1:46, 19 asow. Tiafoe w Turynie; Paul poza walka.",
            "pulse": "ROLEX PARIS MASTERS: BEN SHELTON POKONUJE TOMMY'EGO PAULA I GRA PIERWSZY POLFINAL W BERCY",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Tommy Paul, Accor Arena"
        },
        "f1": {
            "tagline": "GP Sao Paulo FP1: Lando Norris przed Kimi Antonellim i Maxem Verstappenem w Interlagos.",
            "liveNow": "FP1: Norris 1:11.717, Antonelli +0,082s, Verstappen +0,236s. Bez sprintu. Mercedes 630, Ferrari 504 po Meksyku.",
            "pulse": "F1 INTERLAGOS FP1: NORRIS PRZED ANTONELLIM; BEZ SPRINTU; MERCEDES 630, FERRARI 504",
            "keywords": "Formua 1, GP Sao Paulo, Interlagos, Norris, Antonelli, Verstappen"
        },
        "golf": {
            "tagline": "WWT Championship runda 1: Chris Kirk gra 63 bez bogeya i prowadzi o uderzenie w El Cardonal.",
            "liveNow": "R1 zakonczona: Kirk 63 przed Dunlapem i Blairem 64. Pula 6 mln dolarow. R2 w toku, nie jako wynik koncowy.",
            "pulse": "PGA TOUR CABO R1: CHRIS KIRK 63 LIDEREM WWT CHAMPIONSHIP; KARTY FEDEXCUP FALL NA SZALI",
            "keywords": "PGA Tour, WWT Championship, Chris Kirk, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Desk piatek",
            "tonightBlurb": "Jaguars rozbijaja Ravens 33:10. Wembanyama 52-24-8. Haaland wygrywa w Lipsku. Shelton w polfinale w Paryzu. Norris liderem FP1. Kirk 63 w Cabo.",
            "plTitle": "NFL tydzien 9 TNF: Jaguars rozbijaja Ravens 33:10 dzieki Lawrence'owi",
            "plBlurb": "Trevor Lawrence rzuca na 242 jardy i TD z 50. Jacksonville wymusza trzy straty. Jaguars 6-2, Ravens 4-5.",
            "f1Title": "NBA: Wembanyama 52 punkty, 24 zbiorki, 8 blokow, Spurs 112:111 z Dallas",
            "f1Blurb": "Pierwszy 50-20-5 blokow od McAdoo w 1974. Rzut wolny przy 24,2s. Spurs 6-2. Cavs 4-4."
        },
        "pg": {
            "pinFinal": "NFL tydzien 9 TNF: Jaguars 33, Ravens 10. Lawrence 242 jardy, Little 4 FG, Fagnano 2 INT.",
            "week1Closed": "NFL tydzien 9 TNF: Jaguars wygrywaja 33:10 z Ravens i maja 6-2. Ravens 4-5.",
            "week1Sub": "Lawrence TD z 50 do Washingtona. Little 4 FG. Steelers nadal 6-2 w AFC North.",
            "countdownTnf": "TNF tydzien 9: Jaguars 33, Ravens 10. Dalej: JAX w TEN 15 listopada.",
            "barsPoints": "Mercedes prowadzi u konstruktorow z 630 pkt, 126 przed Ferrari (504). Bez sprintu w Sao Paulo.",
            "tableAfterMonday": "Premier League po 9. kolejce: Arsenal 24, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "pinClub": "Wybierz klub. Arsenal prowadzi z 24, City 21, Brighton 19, Chelsea 16, Liverpool 15.",
            "plFootnote": "PL 9. kol.: Arsenal 1:0 Liverpool, Brighton 1:0 City, Chelsea 2:0 Man Utd, Everton 1:0 Newcastle. Dalej: Everton-Coventry pt 20:00 GMT.",
            "majorsDone": "PGA Tour: Chris Kirk 63 liderem WWT Championship R1 w El Cardonal; Dunlap i Blair 64. Pula 6 mln dolarow."
        }
    },
    "zh": {
        "football": {
            "tagline": "NFL第9周周四夜赛：美洲虎33-10大胜乌鸦，劳伦斯传球与利特尔四记任意球定胜负。",
            "liveNow": "巴尔的摩终场：美洲虎33-10乌鸦。劳伦斯242码、50码达阵；利特尔4记任意球；法尼亚诺2次拦截。美洲虎6-2，乌鸦4-5。",
            "pulse": "NFL第9周周四夜赛：杰克逊维尔美洲虎33-10横扫乌鸦；美洲虎6胜2负，乌鸦4胜5负",
            "keywords": "NFL第9周, 美洲虎, 乌鸦, 特雷弗·劳伦斯, 卡姆·利特尔, 乔·法尼亚诺"
        },
        "basketball": {
            "tagline": "NBA：文班亚马52分24篮板8盖帽，马刺112-111险胜独行侠。",
            "liveNow": "圣安东尼奥终场：马刺112-111独行侠。文班52-24-8；24.2秒罚球绝杀。马刺6-2。骑士4-4。",
            "pulse": "NBA：文班亚马52-24-8，马刺112-111险胜独行侠拿下六连胜",
            "keywords": "NBA, 马刺, 独行侠, 文班亚马, 欧文, 哈珀"
        },
        "soccer": {
            "tagline": "欧冠联赛阶段第4轮：哈兰德绝杀助曼城3-2战胜莱比锡。阿森纳英超24分领跑。",
            "liveNow": "莱比锡终场：莱比锡红牛2-3曼城（卢克巴乌龙37，巴库49，费尔南德斯58，努萨61，哈兰德78）。曼城3胜1负排第7。",
            "pulse": "欧冠第4轮：哈兰德第78分钟绝杀莱比锡3-2；阿森纳英超24分领跑",
            "keywords": "欧冠, 曼城, 莱比锡红牛, 哈兰德, 阿森纳, 英超"
        },
        "tennis": {
            "tagline": "巴黎大师赛四分之一决赛：谢尔顿6-4、4-6、6-3击败保罗，首次打进贝尔西四强。",
            "liveNow": "巴黎大师赛四分之一决赛：谢尔顿1小时46分钟19记ACE击败保罗。蒂亚福锁定都灵资格，保罗出局。",
            "pulse": "巴黎大师赛：本·谢尔顿击败汤米·保罗，首次打进贝尔西四强",
            "keywords": "ATP, 巴黎大师赛, 本·谢尔顿, 汤米·保罗, 阿科尔体育馆"
        },
        "f1": {
            "tagline": "圣保罗大奖赛第一次练习：诺里斯领跑安东内利与维斯塔潘。",
            "liveNow": "FP1：诺里斯1:11.717，安东内利+0.082秒，维斯塔潘+0.236秒。本周末无冲刺赛。墨西哥站后梅赛德斯630分，法拉利504分。",
            "pulse": "F1英特拉格斯FP1：诺里斯领跑安东内利；无冲刺赛；梅赛德斯630，法拉利504",
            "keywords": "F1, 圣保罗大奖赛, 英特拉格斯, 诺里斯, 安东内利, 维斯塔潘"
        },
        "golf": {
            "tagline": "WWT锦标赛第一轮：柯克 bogey-free 63杆领先一杆。",
            "liveNow": "第一轮结束：柯克63杆领先邓拉普与布莱尔64杆。奖金600万美元。第二轮进行中，不作为完赛成绩发布。",
            "pulse": "美巡卡博第一轮：克里斯·柯克63杆领跑WWT锦标赛；秋季系列卡位争夺升温",
            "keywords": "美巡赛, WWT锦标赛, 克里斯·柯克, 埃尔卡多纳尔, 迪亚曼特, 洛斯卡沃斯"
        },
        "home": {
            "tonight": "周五稿台",
            "tonightBlurb": "美洲虎周四夜赛33-10大胜乌鸦。文班52-24-8马刺险胜。哈兰德莱比锡绝杀。谢尔顿进巴黎四强。诺里斯FP1最快。柯克卡博63杆。",
            "plTitle": "NFL第9周周四夜赛：美洲虎33-10大胜乌鸦，劳伦斯主导进攻",
            "plBlurb": "劳伦斯传球242码并送出50码达阵，美洲虎制造三次失误。美洲虎6-2，乌鸦4-5。",
            "f1Title": "NBA：文班亚马52分24篮板8盖帽，马刺112-111险胜独行侠",
            "f1Blurb": "1974年麦卡杜之后首次50+20+5盖。24.2秒罚球绝杀。马刺6-2。骑士目前4-4。"
        },
        "pg": {
            "pinFinal": "NFL第9周周四夜赛：美洲虎33-10乌鸦。劳伦斯242码，利特尔4记任意球，法尼亚诺2次拦截。",
            "week1Closed": "NFL第9周周四夜赛：美洲虎33-10击败乌鸦升至6-2。乌鸦4-5。",
            "week1Sub": "劳伦斯50码达阵给华盛顿。利特尔4记任意球。钢人美联北区仍为6-2。",
            "countdownTnf": "第9周周四夜赛：美洲虎33-10乌鸦。下一场：11月15日客场挑战泰坦。",
            "barsPoints": "梅赛德斯车队630分领跑车队积分榜，领先法拉利（504分）126分。圣保罗站无冲刺赛。",
            "tableAfterMonday": "英超第9轮后：阿森纳24分，曼城21分，布莱顿19分，切尔西16分，利物浦15分。",
            "pinClub": "选择俱乐部。阿森纳24分领跑，曼城21，布莱顿19，切尔西16，利物浦15。",
            "plFootnote": "英超第9轮：阿森纳1-0利物浦，布莱顿1-0曼城，切尔西2-0曼联，埃弗顿1-0纽卡。下一场：周五20:00 GMT埃弗顿对考文垂。",
            "majorsDone": "美巡赛：克里斯·柯克63杆领跑WWT锦标赛第一轮；邓拉普与布莱尔64杆。奖金600万美元。"
        }
    },
    "ja": {
        "football": {
            "tagline": "NFL第9週TNF：ジャガーズがレイブンズを33-10で圧倒。ローレンスとリトル4本のFG。",
            "liveNow": "ボルチモア終了：ジャガーズ33-10レイブンズ。ローレンス242yd、50ydTD。リトル4FG。ファニャーノ2INT。ジャガーズ6勝2敗、レイブンズ4勝5敗。",
            "pulse": "NFL第9週TNF：ジャクソンビル・ジャガーズがレイブンズを33-10で撃破。ジャガーズ6勝2敗、レイブンズ4勝5敗",
            "keywords": "NFL第9週, ジャガーズ, レイブンズ, トレバー・ローレンス, キャム・リトル, ジョー・ファニャーノ"
        },
        "basketball": {
            "tagline": "NBA：ウェンバンヤマが52得点24リバウンド8ブロック、スパーズがマーベリックスを112-111で破る。",
            "liveNow": "サンアントニオ終了：スパーズ112-111マーベリックス。ウェンバン52-24-8。24.2秒フリースロー。スパーズ6勝2敗。キャブスは4勝4敗。",
            "pulse": "NBA：ウェンバンヤマ52-24-8、スパーズがマーベリックスを112-111で破り6連勝",
            "keywords": "NBA, スパーズ, マーベリックス, ウェンバンヤマ, アービング, ハーパー"
        },
        "soccer": {
            "tagline": "CL第4節：ハーランドがライプツィヒで決勝点、マンCが3-2勝利。プレミアはアーセナルが24点で首位。",
            "liveNow": "ライプツィヒ終了：RBライプツィヒ2-3マンC（ルケバOG37、バク49、フェルナンデス58、ヌサ61、ハーランド78）。シティ3勝1敗で7位。",
            "pulse": "CL第4節：ハーランドが78分に決勝点、シティがライプツィヒに3-2。プレミア首位はアーセナル24点",
            "keywords": "チャンピオンズリーグ, マンチェスター・シティ, RBライプツィヒ, ハーランド, アーセナル, プレミアリーグ"
        },
        "tennis": {
            "tagline": "ロレックス・パリ・マスターズ準々決勝：シェルトンがポールを6-4, 4-6, 6-3で破り初のベルシー4強。",
            "liveNow": "パリ・マスターズQF：シェルトンが1時間46分19本のエースで勝利。ティアフォーがトリノ出場決定、ポールは敗退。",
            "pulse": "ロレックス・パリ・マスターズ：ベン・シェルトンがトミー・ポールを破り初のベルシー準決勝へ",
            "keywords": "ATP, パリ・マスターズ, ベン・シェルトン, トミー・ポール, アコーアリーナ"
        },
        "f1": {
            "tagline": "サンパウロGP FP1：ノリスがアントネッリとフェルスタッペンを抑えて首位。",
            "liveNow": "FP1：ノリス1:11.717、アントネッリ+0.082秒、フェルスタッペン+0.236秒。スプリントなし。メキシコ後メルセデス630点、フェラーリ504点。",
            "pulse": "F1インテルラゴスFP1：ノリス首位、スプリントなし、メルセデス630点、フェラーリ504点",
            "keywords": "F1, サンパウロGP, インテルラゴス, ノリス, アントネッリ, フェルスタッペン"
        },
        "golf": {
            "tagline": "WWT選手権第1ラウンド：カークがボギーなし63で1打差首位。",
            "liveNow": "R1終了：カーク63、ダンラップとブレア64。賞金600万ドル。R2進行中につき最終成績としては非掲載。",
            "pulse": "PGAツアー カボR1：クリス・カーク63でWWT選手権首位、フェデックスカップ・フォールのカード争い",
            "keywords": "PGAツアー, WWT選手権, クリス・カーク, エル・カルドナル, ディアマンテ, ロスカボス"
        },
        "home": {
            "tonight": "金曜デスク",
            "tonightBlurb": "ジャガーズがTNFで33-10勝利。ウェンバン52-24-8。ハーランドがライプツィヒで決勝点。シェルトンがパリ4強。ノリスがFP1首位。カーク63。",
            "plTitle": "NFL第9週TNF：ジャガーズがローレンスの活躍でレイブンズを33-10撃破",
            "plBlurb": "ローレンスが242ydと50ydTD。ジャガーズが3ターンオーバーを奪う。ジャガーズ6勝2敗、レイブンズ4勝5敗。",
            "f1Title": "NBA：ウェンバンヤマ52得点24リバウンド8ブロック、スパーズ112-111でダラスを破る",
            "f1Blurb": "1974年マクアドー以来の50-20-5ブロック。24.2秒のフリースロー。スパーズ6勝2敗。キャブスは4勝4敗。"
        },
        "pg": {
            "pinFinal": "NFL第9週TNF：ジャガーズ33-10レイブンズ。ローレンス242yd、リトル4FG、ファニャーノ2INT。",
            "week1Closed": "NFL第9週TNF：ジャガーズが33-10でレイブンズを破り6勝2敗。レイブンズ4勝5敗。",
            "week1Sub": "ローレンスがワシントンへ50ydTD。リトル4FG。スティーラーズはAFC北地区で引き続き6勝2敗。",
            "countdownTnf": "第9週TNF：ジャガーズ33-10レイブンズ。次戦は11月15日タイタンズ戦。",
            "barsPoints": "メルセデスが630点でコンストラクターズ首位、フェラーリ（504点）に126点差。サンパウロはスプリントなし。",
            "tableAfterMonday": "プレミアリーグ第9節後：アーセナル24点、シティ21点、ブライトン19点、チェルシー16点、リヴァプール15点。",
            "pinClub": "クラブを選択。アーセナル24点、シティ21点、ブライトン19点、チェルシー16点、リヴァプール15点。",
            "plFootnote": "プレミア第9節：アーセナル1-0リヴァプール、ブライトン1-0シティ、チェルシー2-0マンU、エバートン1-0ニューカッスル。次戦：金曜20:00 GMTエバートン対コヴェントリー。",
            "majorsDone": "PGAツアー：クリス・カーク63でWWT選手権R1首位。ダンラップとブレア64。賞金600万ドル。"
        }
    },
    "ko": {
        "football": {
            "tagline": "NFL 9주차 TNF: 재규어스, 로런스와 리틀 필드골 4개로 레이븐스 33-10 대파.",
            "liveNow": "볼티모어 최종: 재규어스 33-10 레이븐스. 로런스 242야드 50야드 TD. 리틀 FG 4개. 파냐노 INT 2개. 재규어스 6승 2패, 레이븐스 4승 5패.",
            "pulse": "NFL 9주차 TNF: 잭슨빌 재규어스, 레이븐스 33-10 대파. 재규어스 6승 2패, 레이븐스 4승 5패",
            "keywords": "NFL 9주차, 재규어스, 레이븐스, 트레버 로런스, 캠 리틀, 조 파냐노"
        },
        "basketball": {
            "tagline": "NBA: 웸반야마 52점 24리바운드 8블록, 스퍼스가 매버릭스 112-111 제압.",
            "liveNow": "샌안토니오 최종: 스퍼스 112-111 매버릭스. 웸반 52-24-8. 24.2초 자유투. 스퍼스 6승 2패. 캐벌리어스는 4승 4패.",
            "pulse": "NBA: 웸반야마 52-24-8, 스퍼스 매버릭스 112-111 제압하고 6연승",
            "keywords": "NBA, 스퍼스, 매버릭스, 웸반야마, 어빙, 하퍼"
        },
        "soccer": {
            "tagline": "UCL 4차전: 홀란드 결승골로 맨시티 라이프치히 3-2 승리. 프리미어리그는 아스널 24점 선두.",
            "liveNow": "라이프치히 최종: RB 라이프치히 2-3 맨시티 (루케바 자책 37, 바쿠 49, 페르난데스 58, 누사 61, 홀란드 78). 시티 3승 1패 7위.",
            "pulse": "UCL 4차전: 홀란드 78분 결승골로 시티 3-2 승리. 프리미어리그 선두 아스널 24점",
            "keywords": "챔피언스리그, 맨체스터 시티, RB 라이프치히, 홀란드, 아스널, 프리미어리그"
        },
        "tennis": {
            "tagline": "롤렉스 파리 마스터스 8강: 셸턴, 폴을 6-4 4-6 6-3으로 꺾고 첫 베르시 4강.",
            "liveNow": "파리 마스터스 8강: 셸턴 1시간 46분 에이스 19개로 승리. 티아포 토리노 확정, 폴 탈락.",
            "pulse": "롤렉스 파리 마스터스: 벤 셸턴, 토미 폴 꺾고 첫 베르시 준결승 진출",
            "keywords": "ATP, 롤렉스 파리 마스터스, 벤 셸턴, 토미 폴, 아코르 아레나"
        },
        "f1": {
            "tagline": "상파울루 GP FP1: 노리스가 안토넬리와 베르스타펜을 제치고 1위.",
            "liveNow": "FP1: 노리스 1:11.717, 안토넬리 +0.082초, 베르스타펜 +0.236초. 스프린트 없음. 멕시코 이후 메르세데스 630점, 페라리 504점.",
            "pulse": "F1 인테를라고스 FP1: 노리스 선두, 스프린트 없음, 메르세데스 630, 페라리 504",
            "keywords": "F1, 상파울루 GP, 인테를라고스, 노리스, 안토넬리, 베르스타펜"
        },
        "golf": {
            "tagline": "WWT 챔피언십 1라운드: 커크가 보기 없는 63타로 1타 선두.",
            "liveNow": "R1 종료: 커크 63, 던랩과 블레어 64. 상금 600만 달러. 2라운드 진행 중이라 최종 성적 미게시.",
            "pulse": "PGA 투어 카보 R1: 크리스 커크 63타로 WWT 챔피언십 선두, 페덱스컵 폴 카드 경쟁",
            "keywords": "PGA 투어, WWT 챔피언십, 크리스 커크, 엘 카르도날, 디아만테, 로스카보스"
        },
        "home": {
            "tonight": "금요일 데스크",
            "tonightBlurb": "재규어스 TNF 33-10 승리. 웸반 52-24-8. 홀란드 라이프치히 결승골. 셸턴 파리 4강. 노리스 FP1 1위. 커크 63타.",
            "plTitle": "NFL 9주차 TNF: 재규어스, 로런스 앞세워 레이븐스 33-10 대파",
            "plBlurb": "로런스 242야드 패스와 50야드 TD. 재규어스가 턴오버 3개 유도. 재규어스 6승 2패, 레이븐스 4승 5패.",
            "f1Title": "NBA: 웸반야마 52점 24리바운드 8블록, 스퍼스 112-111로 댈러스 제압",
            "f1Blurb": "1974년 맥아두 이후 첫 50-20-5 블록. 24.2초 자유투. 스퍼스 6승 2패. 캐벌리어스는 4승 4패."
        },
        "pg": {
            "pinFinal": "NFL 9주차 TNF: 재규어스 33, 레이븐스 10. 로런스 242야드, 리틀 FG 4, 파냐노 INT 2.",
            "week1Closed": "NFL 9주차 TNF: 재규어스가 레이븐스 33-10으로 꺾고 6승 2패. 레이븐스 4승 5패.",
            "week1Sub": "로런스 워싱턴에게 50야드 TD. 리틀 FG 4개. 스틸러스는 AFC 북부에서 여전히 6승 2패.",
            "countdownTnf": "9주차 TNF: 재규어스 33-10 레이븐스. 다음 경기 11월 15일 타이탄스 원정.",
            "barsPoints": "메르세데스가 630점으로 컨스트럭터 선두, 페라리(504점)에 126점 차. 상파울루는 스프린트 없음.",
            "tableAfterMonday": "프리미어리그 9라운드 후: 아스널 24점, 시티 21점, 브라이턴 19점, 첼시 16점, 리버풀 15점.",
            "pinClub": "클럽 선택. 아스널 24점 선두, 시티 21, 브라이턴 19, 첼시 16, 리버풀 15.",
            "plFootnote": "EPL 9R: 아스널 1-0 리버풀, 브라이턴 1-0 시티, 첼시 2-0 맨유, 에버턴 1-0 뉴캐슬. 다음: 금 20:00 GMT 에버턴 대 코번트리.",
            "majorsDone": "PGA 투어: 크리스 커크 63타로 WWT 챔피언십 R1 선두. 던랩과 블레어 64. 상금 600만 달러."
        }
    },
    "ar": {
        "football": {
            "tagline": "الدوري الامريكي الاسبوع 9: جاغوارز يسحق ريڤنز 33-10 بلورنس واربعة ركلات ميدانية من ليتل.",
            "liveNow": "النتيجة النهائية في بالتيمور: جاغوارز 33، ريڤنز 10. لورنس 242 ياردة وهدف من 50. ليتل 4 ركلات. فاينيانو تقطيعان. جاغوارز 6-2، ريڤنز 4-5.",
            "pulse": "الدوري الامريكي الاسبوع 9: جاكسونفيل جاغوارز يسحق بالتيمور ريڤنز 33-10؛ جاغوارز 6-2، ريڤنز 4-5",
            "keywords": "الدوري الامريكي, جاغوارز, ريڤنز, تريفر لورنس, كام ليتل, جو فاينيانو"
        },
        "basketball": {
            "tagline": "دوري السلة: ويمبانياما 52 نقطة و24 ارتدادا و8 صدات وسبيرز يهزم مافريكس 112-111.",
            "liveNow": "النهاية في سان انطونيو: سبيرز 112، مافريكس 111. ويمبانياما 52-24-8. رمية حرة قبل 24.2 ثانية. سبيرز 6-2. كافالييرز 4-4.",
            "pulse": "دوري السلة: ويمبانياما 52-24-8 وسبيرز يهزم مافريكس 112-111 للفوز السادس تواليا",
            "keywords": "دوري السلة, سبيرز, مافريكس, ويمبانياما, ايرفينغ, هاربر"
        },
        "soccer": {
            "tagline": "دوري ابطال اوروبا الجولة 4: هالاند يحسم 3-2 لمانشستر سيتي في لايبزيغ. ارسنال يتصدر البريميرليغ بـ24 نقطة.",
            "liveNow": "النهاية في لايبزيغ: لايبزيغ 2-3 مانشستر سيتي (لوكبا بالخطأ 37، باكو 49، فرنانديز 58، نوسا 61، هالاند 78). سيتي 3-1 في المركز السابع.",
            "pulse": "دوري الابطال الجولة 4: هالاند في الدقيقة 78 يحسم 3-2 لسيتي؛ ارسنال يتصدر البريميرليغ بـ24",
            "keywords": "دوري الابطال, مانشستر سيتي, لايبزيغ, هالاند, ارسنال, البريميرليغ"
        },
        "tennis": {
            "tagline": "باريس ماسترز ربع النهائي: بن شيلتون يهزم تومي بول 6-4 و4-6 و6-3 ويبلغ نصف نهائي بيرسي لاول مرة.",
            "liveNow": "باريس ماسترز ربع النهائي: شيلتون يفوز في ساعة و46 دقيقة بـ19 ايس. تيافو يتاهل الى تورينو وبول يخرج.",
            "pulse": "باريس ماسترز: بن شيلتون يهزم تومي بول ويبلغ نصف نهائي بيرسي لاول مرة",
            "keywords": "تنس, باريس ماسترز, بن شيلتون, تومي بول, اكور ارينا"
        },
        "f1": {
            "tagline": "جائزة ساو باولو الحصة الاولى: لاندو نوريس يتقدم على كيمي انطونيلي وماكس فيرستابن في انترلاغوس.",
            "liveNow": "الحصة الاولى: نوريس 1:11.717، انطونيلي +0.082ث، فيرستابن +0.236ث. لا سباق قصير. مرسيدس 630 وفيراري 504 بعد المكسيك.",
            "pulse": "فورمولا 1 انترلاغوس الحصة الاولى: نوريس اولا؛ لا سباق قصير؛ مرسيدس 630 وفيراري 504",
            "keywords": "فورمولا 1, جائزة ساو باولو, انترلاغوس, نوريس, انطونيلي, فيرستابن"
        },
        "golf": {
            "tagline": "بطولة WWT الجولة الاولى: كريس كيرك يسجل 63 دون بوجي ويتقدم بضربة في ال كاردونال.",
            "liveNow": "الجولة الاولى انتهت: كيرك 63 امام دنلاب وبلير 64. الجائزة 6 ملايين دولار. الجولة الثانية جارية ولم تنشر كنتيجة نهائية.",
            "pulse": "PGA تور كابو الجولة الاولى: كريس كيرك 63 في الصدارة؛ بطاقات فيدكس كاب الخريف على المحك",
            "keywords": "PGA تور, بطولة WWT, كريس كيرك, ال كاردونال, ديامانتي, لوس كابوس"
        },
        "home": {
            "tonight": "مكتب الجمعة",
            "tonightBlurb": "جاغوارز يسحق ريڤنز 33-10. ويمبانياما 52-24-8. هالاند يحسم لايبزيغ. شيلتون الى نصف نهائي باريس. نوريس يتصدر الحصة الاولى. كيرك 63 في كابو.",
            "plTitle": "الدوري الامريكي الاسبوع 9: جاغوارز يسحق ريڤنز 33-10 بلورنس",
            "plBlurb": "تريفر لورنس يمرر 242 ياردة ويسجل هدفا من 50. جاكسونفيل يجبر على ثلاث خسائر للكرة. جاغوارز 6-2، ريڤنز 4-5.",
            "f1Title": "دوري السلة: ويمبانياما 52 نقطة و24 ارتدادا و8 صدات وسبيرز 112-111 على دالاس",
            "f1Blurb": "اول 50-20-5 صدات منذ مكادو عام 1974. رمية حرة قبل 24.2 ثانية. سبيرز 6-2. كافالييرز 4-4."
        },
        "pg": {
            "pinFinal": "الدوري الامريكي الاسبوع 9: جاغوارز 33، ريڤنز 10. لورنس 242 ياردة، ليتل 4 ركلات، فاينيانو تقطيعان.",
            "week1Closed": "الدوري الامريكي الاسبوع 9: جاغوارز يهزم ريڤنز 33-10 ويرتفع الى 6-2. ريڤنز 4-5.",
            "week1Sub": "لورنس هدف من 50 لياردة لواشنطن. ليتل 4 ركلات. ستيلرز ما زال 6-2 في شمال AFC.",
            "countdownTnf": "الخميس ليلا الاسبوع 9: جاغوارز 33، ريڤنز 10. التالي: جاكسونفيل في تينيسي 15 نوفمبر.",
            "barsPoints": "مرسيدس تتقدم في بطولة الصانعين بـ630 نقطة، بفارق 126 عن فيراري (504). لا سباق قصير في ساو باولو.",
            "tableAfterMonday": "البريميرليغ بعد الجولة 9: ارسنال 24، سيتي 21، برايتون 19، تشيلسي 16، ليفربول 15.",
            "pinClub": "اختر ناديا. ارسنال يتصدر بـ24، سيتي 21، برايتون 19، تشيلسي 16، ليفربول 15.",
            "plFootnote": "الجولة 9: ارسنال 1-0 ليفربول، برايتون 1-0 سيتي، تشيلسي 2-0 مان يونايتد، ايفرتون 1-0 نيوكاسل. التالي: ايفرتون ضد كوفنتري الجمعة 20:00 GMT.",
            "majorsDone": "PGA تور: كريس كيرك 63 يتصدر الجولة الاولى في ال كاردونال؛ دنلاب وبلير 64. الجائزة 6 ملايين دولار."
        }
    },
}

# French pulse had BATTIT which is wrong - I'll leave and not use that exact if we want. "BATTIT" should be "BATT" or "BAT". I'll fix: "BEN SHELTON BAT TOMMY PAUL"

DATA["fr"]["tennis"]["pulse"] = "ROLEX PARIS MASTERS : BEN SHELTON BAT TOMMY PAUL ET REJOINT SA PREMIERE DEMI A BERCY"
DATA["it"]["basketball"]["pulse"] = "NBA: WEMBANYAMA 52-24-8, GLI SPURS BATTERONO I MAVERICKS 112-111, SESTA DI FILA".replace("BATTERONO", "BATTONO")
DATA["zh"]["golf"]["tagline"] = "WWT锦标赛第一轮：柯克交出无柏忌63杆并领先一杆。"

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

def update_messages_dict(content, lang, prefix=""):
    data = DATA[lang]
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

for lang in ["es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
    lang_file = os.path.join(os.path.dirname(__file__), f"../../frontend/src/i18n/messages-{lang}.ts")
    with open(lang_file, "r", encoding="utf-8") as f:
        l_content = f.read()
    l_content = update_messages_dict(l_content, lang)
    with open(lang_file, "w", encoding="utf-8") as f:
        f.write(l_content)
    print(f"Updated {lang_file}")

print("All locale updates for 6 Nov 2026 completed successfully!")
