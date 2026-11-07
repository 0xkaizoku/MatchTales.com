#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update playground.ts, messages.ts, and all messages-*.ts files for 7 November 2026."""
import re
import os

DATA = {
    "en": {
        "football": {
            "tagline": "NFL Week 9 Madrid: Bengals visit Falcons at Bernabeu on Sunday, 9:30 a.m. ET. Saturday has no NFL game.",
            "liveNow": "UPCOMING Sunday in Madrid: Bengals (5-2) at Falcons (3-5), 9:30 a.m. ET, NFL Network. Last final: Jaguars 33, Ravens 10. No Saturday game.",
            "pulse": "NFL WEEK 9 MADRID: BENGALS AT FALCONS SUNDAY 9:30 A.M. ET; LAST FINAL JAGUARS 33-10",
            "keywords": "NFL Week 9, Cincinnati Bengals, Atlanta Falcons, Madrid, Bernabeu, Joe Burrow, Bijan Robinson"
        },
        "basketball": {
            "tagline": "NBA: Luka Doncic scores 53 as Lakers rally past Trail Blazers 124-118.",
            "liveNow": "Final in Los Angeles: Lakers 124, Trail Blazers 118. Doncic 53; Reaves 25. Spurs 7-2. Cavs are 5-4.",
            "pulse": "NBA: DONCIC 53 AS LAKERS BEAT TRAIL BLAZERS 124-118; SPURS 7-2, CAVS 5-4",
            "keywords": "NBA, Lakers, Trail Blazers, Doncic, Reaves, NBA Cup"
        },
        "soccer": {
            "tagline": "Premier League MW10: Noah Okafor winner as Leeds beat Tottenham 1-0. Arsenal still 24 from 9.",
            "liveNow": "Final at Elland Road: Leeds 1-0 Tottenham (Okafor 79). Friday: Everton 3-1 Coventry. Arsenal vs Hull unpublished.",
            "pulse": "PREMIER LEAGUE MW10: OKAFOR 79TH-MINUTE WINNER LIFTS LEEDS PAST TOTTENHAM 1-0",
            "keywords": "Premier League, Leeds, Tottenham, Okafor, Everton, Coventry"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters SF: Ben Shelton beats Luca Van Assche 5-7, 6-3, 6-4 to reach the final.",
            "liveNow": "Paris Masters SF: Shelton def. Van Assche 5-7, 6-3, 6-4. First American finalist since Sock 2017. Alcaraz vs Ruud unpublished.",
            "pulse": "ROLEX PARIS MASTERS: BEN SHELTON BEATS VAN ASSCHE TO REACH THE BERCY FINAL",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Luca Van Assche, Accor Arena"
        },
        "f1": {
            "tagline": "Sao Paulo GP FP3: Max Verstappen leads Kimi Antonelli by 0.025s at Interlagos.",
            "liveNow": "FP3: Verstappen 1:11.622, Antonelli +0.025s, Norris +0.131s. Qualifying unpublished. Mercedes 630, Ferrari 504.",
            "pulse": "F1 INTERLAGOS FP3: VERSTAPPEN LEADS ANTONELLI BY 0.025S; QUALIFYING UNPUBLISHED",
            "keywords": "Formula 1, Sao Paulo GP, Interlagos, Verstappen, Antonelli, Norris"
        },
        "golf": {
            "tagline": "WWT Championship Round 2: Ben James shoots 64 to lead at 15 under at El Cardonal.",
            "liveNow": "R2 complete: James 129 (-15) leads Malnati 130. Kirk 135. Cut 139. Round 3 unpublished as final.",
            "pulse": "PGA TOUR CABO R2: BEN JAMES 129 LEADS WWT CHAMPIONSHIP; ROUND 3 UNPUBLISHED",
            "keywords": "PGA Tour, WWT Championship, Ben James, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Saturday desk",
            "tonightBlurb": "Doncic scores 53 as Lakers beat Blazers. Leeds 1-0 Tottenham. Shelton into Paris final. Verstappen leads Interlagos FP3. James 129 in Cabo. Bengals-Falcons Madrid Sunday.",
            "plTitle": "NBA: Luka Doncic scores 53 as Lakers rally past Trail Blazers 124-118",
            "plBlurb": "Eleventh career 50-point game. Reaves 25. Spurs 7-2. Cavs are 5-4.",
            "f1Title": "Premier League MW10: Noah Okafor winner as Leeds beat Tottenham 1-0",
            "f1Blurb": "Okafor 79th-minute finish, 97 seconds after coming on. Friday: Everton 3-1 Coventry. Arsenal vs Hull unpublished."
        },
        "pg": {
            "pinFinal": "NFL Week 9 Madrid upcoming: Bengals at Falcons Sunday 9:30 a.m. ET. Last final: Jaguars 33, Ravens 10.",
            "week1Closed": "NFL Week 9: Saturday has no game. Last final TNF Jaguars 33-10. Sunday Madrid unpublished as a score.",
            "week1Sub": "Bengals 5-2, Falcons 3-5 at Bernabeu. Steelers 6-2 on a Week 9 bye.",
            "countdownTnf": "Week 9 TNF still stands: Jaguars 33, Ravens 10. Next: CIN at ATL Madrid Nov 8.",
            "barsPoints": "Mercedes lead Constructors with 630 pts, 126 ahead of Ferrari (504). FP3: Verstappen 1:11.622. Qualifying unpublished.",
            "tableAfterMonday": "Premier League after finished MW10 boards: Arsenal 24 from 9, City 21, Brighton 19, Chelsea 16, Everton 16 from 10, Leeds 14 from 10.",
            "pinClub": "Select a club. Arsenal 24 from 9, City 21, Everton 16 from 10, Leeds 14 from 10. Hull unpublished.",
            "plFootnote": "MW10 finished: Leeds 1-0 Tottenham (Okafor 79), Everton 3-1 Coventry. Arsenal vs Hull unpublished.",
            "majorsDone": "PGA Tour: Ben James 129 (-15) leads WWT Championship after R2; Malnati 130. Round 3 unpublished."
        }
    },
    "fr": {
        "football": {
            "tagline": "NFL Semaine 9 Madrid : les Bengals jouent les Falcons au Bernabeu dimanche a 9h30 ET. Pas de match samedi.",
            "liveNow": "A venir dimanche a Madrid : Bengals (5-2) contre Falcons (3-5), 9h30 ET, NFL Network. Dernier score : Jaguars 33, Ravens 10.",
            "pulse": "NFL SEMAINE 9 MADRID : BENGALS-FALCONS DIMANCHE 9H30 ET ; DERNIER SCORE JAGUARS 33-10",
            "keywords": "NFL Semaine 9, Cincinnati Bengals, Atlanta Falcons, Madrid, Bernabeu, Joe Burrow"
        },
        "basketball": {
            "tagline": "NBA : Luka Doncic inscrit 53 points, les Lakers battent les Trail Blazers 124-118.",
            "liveNow": "Fin de match a Los Angeles : Lakers 124, Trail Blazers 118. Doncic 53 ; Reaves 25. Spurs 7-2. Cavs a 5-4.",
            "pulse": "NBA : DONCIC 53, LES LAKERS BATTENT LES TRAIL BLAZERS 124-118 ; SPURS 7-2, CAVS 5-4",
            "keywords": "NBA, Lakers, Trail Blazers, Doncic, Reaves"
        },
        "soccer": {
            "tagline": "Premier League J10 : Noah Okafor offre le 1-0 a Leeds contre Tottenham. Arsenal toujours a 24 en 9.",
            "liveNow": "Fin de match a Elland Road : Leeds 1-0 Tottenham (Okafor 79). Vendredi : Everton 3-1 Coventry. Arsenal-Hull non publie.",
            "pulse": "PREMIER LEAGUE J10 : OKAFOR A LA 79E OFFRE LE 1-0 A LEEDS CONTRE TOTTENHAM",
            "keywords": "Premier League, Leeds, Tottenham, Okafor, Everton, Coventry"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters DF : Ben Shelton bat Luca Van Assche 5-7, 6-3, 6-4 et rejoint la finale.",
            "liveNow": "Paris Masters DF : Shelton bat Van Assche 5-7, 6-3, 6-4. Premier Americain en finale depuis Sock 2017. Alcaraz-Ruud non publie.",
            "pulse": "ROLEX PARIS MASTERS : BEN SHELTON BAT VAN ASSCHE ET REJOINT LA FINALE A BERCY",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Luca Van Assche, Accor Arena"
        },
        "f1": {
            "tagline": "GP de Sao Paulo EL3 : Max Verstappen devance Kimi Antonelli de 0,025 s a Interlagos.",
            "liveNow": "EL3 : Verstappen 1:11.622, Antonelli +0,025 s, Norris +0,131 s. Qualifications non publiees. Mercedes 630, Ferrari 504.",
            "pulse": "F1 INTERLAGOS EL3 : VERSTAPPEN DEVANT ANTONELLI DE 0,025 S ; QUALIFS NON PUBLIEES",
            "keywords": "Formule 1, GP de Sao Paulo, Interlagos, Verstappen, Antonelli, Norris"
        },
        "golf": {
            "tagline": "WWT Championship 2e tour : Ben James signe un 64 et mene a 15 sous le par a El Cardonal.",
            "liveNow": "T2 termine : James 129 (-15) devant Malnati 130. Kirk 135. Cut 139. 3e tour non publie.",
            "pulse": "PGA TOUR CABO T2 : BEN JAMES 129 EN TETE DU WWT CHAMPIONSHIP ; 3E TOUR NON PUBLIE",
            "keywords": "PGA Tour, WWT Championship, Ben James, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Desk du samedi",
            "tonightBlurb": "Doncic 53 points, les Lakers battent Portland. Leeds 1-0 Tottenham. Shelton en finale a Paris. Verstappen en tete des EL3. James 129 a Cabo. Bengals-Falcons dimanche a Madrid.",
            "plTitle": "NBA : Luka Doncic inscrit 53 points, les Lakers battent les Trail Blazers 124-118",
            "plBlurb": "Onzieme match a 50 points. Reaves 25. Spurs 7-2. Cavs a 5-4.",
            "f1Title": "Premier League J10 : Noah Okafor offre le 1-0 a Leeds contre Tottenham",
            "f1Blurb": "Okafor a la 79e, 97 secondes apres son entree. Vendredi : Everton 3-1 Coventry. Arsenal-Hull non publie."
        },
        "pg": {
            "pinFinal": "NFL Semaine 9 Madrid a venir : Bengals-Falcons dimanche 9h30 ET. Dernier score : Jaguars 33, Ravens 10.",
            "week1Closed": "NFL Semaine 9 : pas de match samedi. Dernier score TNF Jaguars 33-10. Madrid dimanche sans score.",
            "week1Sub": "Bengals 5-2, Falcons 3-5 au Bernabeu. Steelers 6-2 au repos en semaine 9.",
            "countdownTnf": "TNF Semaine 9 toujours valable : Jaguars 33, Ravens 10. Suite : CIN a ATL Madrid le 8 novembre.",
            "barsPoints": "Mercedes mene chez les constructeurs avec 630 pts, 126 d'avance sur Ferrari (504). EL3 : Verstappen 1:11.622. Qualifs non publiees.",
            "tableAfterMonday": "Premier League apres les matches termines de la J10 : Arsenal 24 en 9, City 21, Brighton 19, Chelsea 16, Everton 16 en 10, Leeds 14 en 10.",
            "pinClub": "Choisissez un club. Arsenal 24 en 9, City 21, Everton 16 en 10, Leeds 14 en 10. Hull non publie.",
            "plFootnote": "J10 terminee : Leeds 1-0 Tottenham (Okafor 79), Everton 3-1 Coventry. Arsenal-Hull non publie.",
            "majorsDone": "PGA Tour : Ben James 129 (-15) en tete du WWT Championship apres le T2 ; Malnati 130. 3e tour non publie."
        }
    },
    "es": {
        "football": {
            "tagline": "NFL Semana 9 Madrid: los Bengals visitan a los Falcons en el Bernabeu el domingo a las 9:30 ET. No hay partido el sabado.",
            "liveNow": "Domingo en Madrid: Bengals (5-2) contra Falcons (3-5), 9:30 ET, NFL Network. Ultimo final: Jaguars 33, Ravens 10. Sin partido el sabado.",
            "pulse": "NFL SEMANA 9 MADRID: BENGALS-FALCONS DOMINGO 9:30 ET; ULTIMO FINAL JAGUARS 33-10",
            "keywords": "NFL Semana 9, Cincinnati Bengals, Atlanta Falcons, Madrid, Bernabeu, Joe Burrow"
        },
        "basketball": {
            "tagline": "NBA: Luka Doncic anota 53 y los Lakers ganan 124-118 a los Trail Blazers.",
            "liveNow": "Final en Los Angeles: Lakers 124, Trail Blazers 118. Doncic 53; Reaves 25. Spurs 7-2. Cavs 5-4.",
            "pulse": "NBA: DONCIC 53 Y LOS LAKERS GANAN 124-118 A TRAIL BLAZERS; SPURS 7-2, CAVS 5-4",
            "keywords": "NBA, Lakers, Trail Blazers, Doncic, Reaves"
        },
        "soccer": {
            "tagline": "Premier League J10: gol de Noah Okafor y Leeds gana 1-0 a Tottenham. Arsenal sigue con 24 en 9.",
            "liveNow": "Final en Elland Road: Leeds 1-0 Tottenham (Okafor 79). Viernes: Everton 3-1 Coventry. Arsenal-Hull no publicado.",
            "pulse": "PREMIER LEAGUE J10: OKAFOR EN EL 79 DA EL 1-0 AL LEEDS ANTE TOTTENHAM",
            "keywords": "Premier League, Leeds, Tottenham, Okafor, Everton, Coventry"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters SF: Ben Shelton vence a Luca Van Assche 5-7, 6-3, 6-4 y alcanza la final.",
            "liveNow": "Paris Masters SF: Shelton gana 5-7, 6-3, 6-4. Primer estadounidense en la final desde Sock 2017. Alcaraz-Ruud no publicado.",
            "pulse": "ROLEX PARIS MASTERS: BEN SHELTON VENCE A VAN ASSCHE Y JUEGA LA FINAL EN BERCY",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Luca Van Assche, Accor Arena"
        },
        "f1": {
            "tagline": "GP de Sao Paulo EL3: Max Verstappen lidera a Kimi Antonelli por 0.025s en Interlagos.",
            "liveNow": "EL3: Verstappen 1:11.622, Antonelli +0.025s, Norris +0.131s. Clasificacion no publicada. Mercedes 630, Ferrari 504.",
            "pulse": "F1 INTERLAGOS EL3: VERSTAPPEN LIDER POR 0.025S; CLASIFICACION NO PUBLICADA",
            "keywords": "Formula 1, GP de Sao Paulo, Interlagos, Verstappen, Antonelli, Norris"
        },
        "golf": {
            "tagline": "WWT Championship 2a ronda: Ben James firma 64 y lidera a 15 bajo en El Cardonal.",
            "liveNow": "R2 cerrada: James 129 (-15) delante de Malnati 130. Kirk 135. Corte 139. 3a ronda no publicada.",
            "pulse": "PGA TOUR CABO R2: BEN JAMES 129 LIDERA EL WWT CHAMPIONSHIP; 3A RONDA NO PUBLICADA",
            "keywords": "PGA Tour, WWT Championship, Ben James, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Desk del sabado",
            "tonightBlurb": "Doncic 53, los Lakers ganan a Portland. Leeds 1-0 Tottenham. Shelton a la final de Paris. Verstappen lidera la EL3. James 129 en Cabo. Bengals-Falcons el domingo en Madrid.",
            "plTitle": "NBA: Luka Doncic anota 53 y los Lakers ganan 124-118 a los Trail Blazers",
            "plBlurb": "Undecimo partido de 50 puntos. Reaves 25. Spurs 7-2. Cavs 5-4.",
            "f1Title": "Premier League J10: gol de Noah Okafor y Leeds gana 1-0 a Tottenham",
            "f1Blurb": "Okafor en el 79, 97 segundos despues de entrar. Viernes: Everton 3-1 Coventry. Arsenal-Hull no publicado."
        },
        "pg": {
            "pinFinal": "NFL Semana 9 Madrid por jugar: Bengals-Falcons domingo 9:30 ET. Ultimo final: Jaguars 33, Ravens 10.",
            "week1Closed": "NFL Semana 9: no hay partido el sabado. Ultimo final TNF Jaguars 33-10. Madrid domingo sin marcador.",
            "week1Sub": "Bengals 5-2, Falcons 3-5 en el Bernabeu. Steelers 6-2, bye en la semana 9.",
            "countdownTnf": "TNF Semana 9 sigue en pie: Jaguars 33, Ravens 10. Siguiente: CIN en ATL Madrid el 8 de noviembre.",
            "barsPoints": "Mercedes lidera constructores con 630 pts, 126 sobre Ferrari (504). EL3: Verstappen 1:11.622. Clasificacion no publicada.",
            "tableAfterMonday": "Premier League tras los partidos cerrados de la J10: Arsenal 24 en 9, City 21, Brighton 19, Chelsea 16, Everton 16 en 10, Leeds 14 en 10.",
            "pinClub": "Elige un club. Arsenal 24 en 9, City 21, Everton 16 en 10, Leeds 14 en 10. Hull no publicado.",
            "plFootnote": "J10 cerrada: Leeds 1-0 Tottenham (Okafor 79), Everton 3-1 Coventry. Arsenal-Hull no publicado.",
            "majorsDone": "PGA Tour: Ben James 129 (-15) lidera el WWT Championship tras la R2; Malnati 130. 3a ronda no publicada."
        }
    },
    "de": {
        "football": {
            "tagline": "NFL Woche 9 Madrid: Bengals gegen Falcons am Sonntag 9:30 ET im Bernabeu. Samstag kein NFL-Spiel.",
            "liveNow": "Sonntag in Madrid: Bengals (5-2) gegen Falcons (3-5), 9:30 ET, NFL Network. Letztes Ergebnis: Jaguars 33, Ravens 10. Kein Samstagsspiel.",
            "pulse": "NFL WOCHE 9 MADRID: BENGALS-FALCONS SONNTAG 9:30 ET; LETZTES ERGEBNIS JAGUARS 33-10",
            "keywords": "NFL Woche 9, Cincinnati Bengals, Atlanta Falcons, Madrid, Bernabeu, Joe Burrow"
        },
        "basketball": {
            "tagline": "NBA: Luka Doncic erzielt 53 Punkte, Lakers schlagen Trail Blazers 124:118.",
            "liveNow": "Ende in Los Angeles: Lakers 124, Trail Blazers 118. Doncic 53; Reaves 25. Spurs 7-2. Cavs 5-4.",
            "pulse": "NBA: DONCIC 53, LAKERS SCHLAGEN TRAIL BLAZERS 124:118; SPURS 7-2, CAVS 5-4",
            "keywords": "NBA, Lakers, Trail Blazers, Doncic, Reaves"
        },
        "soccer": {
            "tagline": "Premier League ST10: Noah Okafor trifft, Leeds schlaegt Tottenham 1:0. Arsenal weiter 24 aus 9.",
            "liveNow": "Ende in Elland Road: Leeds 1:0 Tottenham (Okafor 79). Freitag: Everton 3:1 Coventry. Arsenal gegen Hull unveroeffentlicht.",
            "pulse": "PREMIER LEAGUE ST10: OKAFOR IN DER 79. TRIFFT ZUM 1:0 FUER LEEDS GEGEN TOTTENHAM",
            "keywords": "Premier League, Leeds, Tottenham, Okafor, Everton, Coventry"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters HF: Ben Shelton schlaegt Luca Van Assche 5:7, 6:3, 6:4 und steht im Finale.",
            "liveNow": "Paris Masters HF: Shelton gewinnt 5:7, 6:3, 6:4. Erster US-Finalist seit Sock 2017. Alcaraz gegen Ruud unveroeffentlicht.",
            "pulse": "ROLEX PARIS MASTERS: BEN SHELTON SCHLAEGT VAN ASSCHE UND STEHT IM BERCY-FINALE",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Luca Van Assche, Accor Arena"
        },
        "f1": {
            "tagline": "Sao-Paulo-GP FP3: Max Verstappen fuehrt Kimi Antonelli um 0,025s an in Interlagos.",
            "liveNow": "FP3: Verstappen 1:11.622, Antonelli +0,025s, Norris +0,131s. Qualifying unveroeffentlicht. Mercedes 630, Ferrari 504.",
            "pulse": "F1 INTERLAGOS FP3: VERSTAPPEN FUEHRT UM 0,025S; QUALIFYING UNVEROEFFENTLICHT",
            "keywords": "Formel 1, Sao-Paulo-GP, Interlagos, Verstappen, Antonelli, Norris"
        },
        "golf": {
            "tagline": "WWT Championship Runde 2: Ben James spielt 64 und fuehrt mit 15 unter in El Cardonal.",
            "liveNow": "R2 komplett: James 129 (-15) vor Malnati 130. Kirk 135. Cut 139. Runde 3 unveroeffentlicht.",
            "pulse": "PGA TOUR CABO R2: BEN JAMES 129 FUEHRT WWT CHAMPIONSHIP; RUNDE 3 UNVEROEFFENTLICHT",
            "keywords": "PGA Tour, WWT Championship, Ben James, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Samstags-Desk",
            "tonightBlurb": "Doncic 53, Lakers schlagen Portland. Leeds 1:0 Tottenham. Shelton im Paris-Finale. Verstappen fuehrt FP3. James 129 in Cabo. Bengals-Falcons sonntags in Madrid.",
            "plTitle": "NBA: Luka Doncic erzielt 53 Punkte, Lakers schlagen Trail Blazers 124:118",
            "plBlurb": "Elftes 50-Punkte-Spiel. Reaves 25. Spurs 7-2. Cavs 5-4.",
            "f1Title": "Premier League ST10: Noah Okafor trifft, Leeds schlaegt Tottenham 1:0",
            "f1Blurb": "Okafor in der 79., 97 Sekunden nach der Einwechslung. Freitag: Everton 3:1 Coventry. Arsenal gegen Hull unveroeffentlicht."
        },
        "pg": {
            "pinFinal": "NFL Woche 9 Madrid steht aus: Bengals-Falcons Sonntag 9:30 ET. Letztes Ergebnis: Jaguars 33, Ravens 10.",
            "week1Closed": "NFL Woche 9: Samstag kein Spiel. Letztes Ergebnis TNF Jaguars 33-10. Madrid Sonntag ohne Spielstand.",
            "week1Sub": "Bengals 5-2, Falcons 3-5 im Bernabeu. Steelers 6-2, Bye in Woche 9.",
            "countdownTnf": "TNF Woche 9 gilt weiter: Jaguars 33, Ravens 10. Weiter: CIN in ATL Madrid am 8. November.",
            "barsPoints": "Mercedes fuehrt bei den Konstrukteuren mit 630 Pkt, 126 vor Ferrari (504). FP3: Verstappen 1:11.622. Qualifying unveroeffentlicht.",
            "tableAfterMonday": "Premier League nach beendeten ST10-Spielen: Arsenal 24 aus 9, City 21, Brighton 19, Chelsea 16, Everton 16 aus 10, Leeds 14 aus 10.",
            "pinClub": "Club waehlen. Arsenal 24 aus 9, City 21, Everton 16 aus 10, Leeds 14 aus 10. Hull unveroeffentlicht.",
            "plFootnote": "ST10 beendet: Leeds 1:0 Tottenham (Okafor 79), Everton 3:1 Coventry. Arsenal gegen Hull unveroeffentlicht.",
            "majorsDone": "PGA Tour: Ben James 129 (-15) fuehrt WWT Championship nach R2; Malnati 130. Runde 3 unveroeffentlicht."
        }
    },
    "it": {
        "football": {
            "tagline": "NFL Week 9 Madrid: i Bengals affrontano i Falcons al Bernabeu domenica alle 9:30 ET. Nessuna partita sabato.",
            "liveNow": "Domenica a Madrid: Bengals (5-2) contro Falcons (3-5), 9:30 ET, NFL Network. Ultimo risultato: Jaguars 33, Ravens 10. Niente sabato.",
            "pulse": "NFL WEEK 9 MADRID: BENGALS-FALCONS DOMENICA 9:30 ET; ULTIMO RISULTATO JAGUARS 33-10",
            "keywords": "NFL Week 9, Cincinnati Bengals, Atlanta Falcons, Madrid, Bernabeu, Joe Burrow"
        },
        "basketball": {
            "tagline": "NBA: Luka Doncic segna 53, i Lakers battono i Trail Blazers 124-118.",
            "liveNow": "Fine a Los Angeles: Lakers 124, Trail Blazers 118. Doncic 53; Reaves 25. Spurs 7-2. Cavs 5-4.",
            "pulse": "NBA: DONCIC 53, I LAKERS BATTONO I TRAIL BLAZERS 124-118; SPURS 7-2, CAVS 5-4",
            "keywords": "NBA, Lakers, Trail Blazers, Doncic, Reaves"
        },
        "soccer": {
            "tagline": "Premier League 10a: gol di Noah Okafor, Leeds batte il Tottenham 1-0. Arsenal ancora 24 in 9.",
            "liveNow": "Fine a Elland Road: Leeds 1-0 Tottenham (Okafor 79). Venerdi: Everton 3-1 Coventry. Arsenal-Hull non pubblicato.",
            "pulse": "PREMIER LEAGUE 10A: OKAFOR AL 79' REGALA L'1-0 AL LEEDS SUL TOTTENHAM",
            "keywords": "Premier League, Leeds, Tottenham, Okafor, Everton, Coventry"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters SF: Ben Shelton batte Luca Van Assche 5-7, 6-3, 6-4 e vola in finale.",
            "liveNow": "Paris Masters SF: Shelton vince 5-7, 6-3, 6-4. Primo americano in finale da Sock 2017. Alcaraz-Ruud non pubblicato.",
            "pulse": "ROLEX PARIS MASTERS: BEN SHELTON BATTE VAN ASSCHE E GIOCA LA FINALE A BERCY",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Luca Van Assche, Accor Arena"
        },
        "f1": {
            "tagline": "GP di Sao Paulo PL3: Max Verstappen precede Kimi Antonelli di 0.025s a Interlagos.",
            "liveNow": "PL3: Verstappen 1:11.622, Antonelli +0.025s, Norris +0.131s. Qualifiche non pubblicate. Mercedes 630, Ferrari 504.",
            "pulse": "F1 INTERLAGOS PL3: VERSTAPPEN PRIMO DI 0.025S; QUALIFICHE NON PUBBLICATE",
            "keywords": "Formula 1, GP di Sao Paulo, Interlagos, Verstappen, Antonelli, Norris"
        },
        "golf": {
            "tagline": "WWT Championship 2o giro: Ben James firma 64 e guida a 15 sotto a El Cardonal.",
            "liveNow": "2o giro chiuso: James 129 (-15) davanti a Malnati 130. Kirk 135. Taglio 139. 3o giro non pubblicato.",
            "pulse": "PGA TOUR CABO 2O GIRO: BEN JAMES 129 IN TESTA AL WWT CHAMPIONSHIP; 3O GIRO NON PUBBLICATO",
            "keywords": "PGA Tour, WWT Championship, Ben James, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Desk del sabato",
            "tonightBlurb": "Doncic 53, i Lakers battono Portland. Leeds 1-0 Tottenham. Shelton in finale a Parigi. Verstappen guida le PL3. James 129 a Cabo. Bengals-Falcons domenica a Madrid.",
            "plTitle": "NBA: Luka Doncic segna 53, i Lakers battono i Trail Blazers 124-118",
            "plBlurb": "Undicesima gara da 50 punti. Reaves 25. Spurs 7-2. Cavs 5-4.",
            "f1Title": "Premier League 10a: gol di Noah Okafor, Leeds batte il Tottenham 1-0",
            "f1Blurb": "Okafor al 79', 97 secondi dopo l'ingresso. Venerdi: Everton 3-1 Coventry. Arsenal-Hull non pubblicato."
        },
        "pg": {
            "pinFinal": "NFL Week 9 Madrid in programma: Bengals-Falcons domenica 9:30 ET. Ultimo risultato: Jaguars 33, Ravens 10.",
            "week1Closed": "NFL Week 9: nessuna partita sabato. Ultimo risultato TNF Jaguars 33-10. Madrid domenica senza punteggio.",
            "week1Sub": "Bengals 5-2, Falcons 3-5 al Bernabeu. Steelers 6-2, bye nella settimana 9.",
            "countdownTnf": "TNF Week 9 resta valido: Jaguars 33, Ravens 10. Segue: CIN ad ATL Madrid l'8 novembre.",
            "barsPoints": "Mercedes guida i costruttori con 630 pts, 126 su Ferrari (504). PL3: Verstappen 1:11.622. Qualifiche non pubblicate.",
            "tableAfterMonday": "Premier League dopo le gare chiuse della 10a: Arsenal 24 in 9, City 21, Brighton 19, Chelsea 16, Everton 16 in 10, Leeds 14 in 10.",
            "pinClub": "Scegli un club. Arsenal 24 in 9, City 21, Everton 16 in 10, Leeds 14 in 10. Hull non pubblicato.",
            "plFootnote": "10a chiusa: Leeds 1-0 Tottenham (Okafor 79), Everton 3-1 Coventry. Arsenal-Hull non pubblicato.",
            "majorsDone": "PGA Tour: Ben James 129 (-15) guida il WWT Championship dopo il 2o giro; Malnati 130. 3o giro non pubblicato."
        }
    },
    "pl": {
        "football": {
            "tagline": "NFL tydzien 9 Madryt: Bengals graja z Falcons na Bernabeu w niedziele o 9:30 ET. W sobote nie ma meczu.",
            "liveNow": "Niedziela w Madrycie: Bengals (5-2) przeciwko Falcons (3-5), 9:30 ET, NFL Network. Ostatni wynik: Jaguars 33, Ravens 10. Bez soboty.",
            "pulse": "NFL TYDZIEN 9 MADRYT: BENGALS-FALCONS NIEDZIELA 9:30 ET; OSTATNI WYNIK JAGUARS 33-10",
            "keywords": "NFL tydzien 9, Cincinnati Bengals, Atlanta Falcons, Madryt, Bernabeu, Joe Burrow"
        },
        "basketball": {
            "tagline": "NBA: Luka Doncic zdobywa 53 punkty, Lakers wygrywaja z Trail Blazers 124:118.",
            "liveNow": "Koniec w Los Angeles: Lakers 124, Trail Blazers 118. Doncic 53; Reaves 25. Spurs 7-2. Cavs 5-4.",
            "pulse": "NBA: DONCIC 53, LAKERS WYGRYWAJA 124:118 Z TRAIL BLAZERS; SPURS 7-2, CAVS 5-4",
            "keywords": "NBA, Lakers, Trail Blazers, Doncic, Reaves"
        },
        "soccer": {
            "tagline": "Premier League kol. 10: gol Noaha Okafora, Leeds wygrywa z Tottenhamem 1:0. Arsenal nadal 24 z 9.",
            "liveNow": "Koniec na Elland Road: Leeds 1:0 Tottenham (Okafor 79). Piatek: Everton 3:1 Coventry. Arsenal-Hull nieopublikowany.",
            "pulse": "PREMIER LEAGUE KOL. 10: OKAFOR W 79. MINUCIE DAJE LEEDS 1:0 Z TOTTENHAMEM",
            "keywords": "Premier League, Leeds, Tottenham, Okafor, Everton, Coventry"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters PF: Ben Shelton pokonuje Luce Van Assche 5:7, 6:3, 6:4 i gra w finale.",
            "liveNow": "Paris Masters PF: Shelton wygrywa 5:7, 6:3, 6:4. Pierwszy Amerykanin w finale od Socka 2017. Alcaraz-Ruud nieopublikowany.",
            "pulse": "ROLEX PARIS MASTERS: BEN SHELTON POKONUJE VAN ASSCHE I GRA W FINALE W BERCY",
            "keywords": "ATP, Rolex Paris Masters, Ben Shelton, Luca Van Assche, Accor Arena"
        },
        "f1": {
            "tagline": "GP Sao Paulo T3: Max Verstappen wyprzedza Kimiego Antonellego o 0,025 s na Interlagos.",
            "liveNow": "T3: Verstappen 1:11.622, Antonelli +0,025 s, Norris +0,131 s. Kwalifikacje nieopublikowane. Mercedes 630, Ferrari 504.",
            "pulse": "F1 INTERLAGOS T3: VERSTAPPEN PIERWSZY O 0,025 S; KWALIFIKACJE NIEOPUBLIKOWANE",
            "keywords": "Formula 1, GP Sao Paulo, Interlagos, Verstappen, Antonelli, Norris"
        },
        "golf": {
            "tagline": "WWT Championship 2. runda: Ben James gra 64 i prowadzi na 15 pod parem na El Cardonal.",
            "liveNow": "R2 zakonczona: James 129 (-15) przed Malnatim 130. Kirk 135. Cut 139. 3. runda nieopublikowana.",
            "pulse": "PGA TOUR CABO R2: BEN JAMES 129 PROWADZI WWT CHAMPIONSHIP; 3. RUNDA NIEOPUBLIKOWANA",
            "keywords": "PGA Tour, WWT Championship, Ben James, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Sobotni desk",
            "tonightBlurb": "Doncic 53, Lakers wygrywaja z Portland. Leeds 1:0 Tottenham. Shelton w finale w Paryzu. Verstappen prowadzi T3. James 129 w Cabo. Bengals-Falcons w niedziele w Madrycie.",
            "plTitle": "NBA: Luka Doncic zdobywa 53 punkty, Lakers wygrywaja z Trail Blazers 124:118",
            "plBlurb": "11. mecz z 50 punktami. Reaves 25. Spurs 7-2. Cavs 5-4.",
            "f1Title": "Premier League kol. 10: gol Noaha Okafora, Leeds wygrywa z Tottenhamem 1:0",
            "f1Blurb": "Okafor w 79. minucie, 97 sekund po wejściu. Piatek: Everton 3:1 Coventry. Arsenal-Hull nieopublikowany."
        },
        "pg": {
            "pinFinal": "NFL tydzien 9 Madryt do zagrania: Bengals-Falcons niedziela 9:30 ET. Ostatni wynik: Jaguars 33, Ravens 10.",
            "week1Closed": "NFL tydzien 9: w sobote nie ma meczu. Ostatni wynik TNF Jaguars 33-10. Madryt w niedziele bez wyniku.",
            "week1Sub": "Bengals 5-2, Falcons 3-5 na Bernabeu. Steelers 6-2, pauza w 9. tygodniu.",
            "countdownTnf": "TNF tydzien 9 nadal wazny: Jaguars 33, Ravens 10. Dalej: CIN w ATL Madryt 8 listopada.",
            "barsPoints": "Mercedes prowadzi u konstruktorow z 630 pkt, 126 przed Ferrari (504). T3: Verstappen 1:11.622. Kwalifikacje nieopublikowane.",
            "tableAfterMonday": "Premier League po zakonczonych meczach 10. kolejki: Arsenal 24 z 9, City 21, Brighton 19, Chelsea 16, Everton 16 z 10, Leeds 14 z 10.",
            "pinClub": "Wybierz klub. Arsenal 24 z 9, City 21, Everton 16 z 10, Leeds 14 z 10. Hull nieopublikowany.",
            "plFootnote": "Kol. 10 zakonczona: Leeds 1:0 Tottenham (Okafor 79), Everton 3:1 Coventry. Arsenal-Hull nieopublikowany.",
            "majorsDone": "PGA Tour: Ben James 129 (-15) prowadzi WWT Championship po R2; Malnati 130. 3. runda nieopublikowana."
        }
    },
    "zh": {
        "football": {
            "tagline": "NFL第9周马德里：猛虎周日美东9:30在伯纳乌对阵猎鹰。周六无NFL比赛。",
            "liveNow": "周日马德里待赛：猛虎（5胜2负）对猎鹰（3胜5负），美东9:30，NFL Network。最近完场：美洲虎33-10乌鸦。周六无赛。",
            "pulse": "NFL第9周马德里：猛虎周日对猎鹰；最近完场美洲虎33-10",
            "keywords": "NFL第9周, 辛辛那提猛虎, 亚特兰大猎鹰, 马德里, 伯纳乌, 乔·伯罗"
        },
        "basketball": {
            "tagline": "NBA：东契奇砍下53分，湖人124-118逆转开拓者。",
            "liveNow": "洛杉矶完场：湖人124，开拓者118。东契奇53分；里夫斯25分。马刺7胜2负。骑士5胜4负。",
            "pulse": "NBA：东契奇53分湖人124-118胜开拓者；马刺7-2，骑士5-4",
            "keywords": "NBA, 湖人, 开拓者, 东契奇, 里夫斯"
        },
        "soccer": {
            "tagline": "英超第10轮：奥卡福尔绝杀，利兹联1-0击败热刺。阿森纳9场仍24分。",
            "liveNow": "埃兰路完场：利兹1-0热刺（奥卡福尔79）。周五：埃弗顿3-1考文垂。阿森纳对赫尔暂不发布。",
            "pulse": "英超第10轮：奥卡福尔第79分钟绝杀助利兹1-0热刺",
            "keywords": "英超, 利兹联, 热刺, 奥卡福尔, 埃弗顿, 考文垂"
        },
        "tennis": {
            "tagline": "巴黎大师赛半决赛：谢尔顿5-7、6-3、6-4击败范阿舍晋级决赛。",
            "liveNow": "巴黎大师赛半决赛：谢尔顿5-7、6-3、6-4。自2017年索克后首位美国决赛选手。阿尔卡拉斯对鲁德暂不发布。",
            "pulse": "巴黎大师赛：谢尔顿击败范阿舍晋级贝尔西决赛",
            "keywords": "ATP, 巴黎大师赛, 本·谢尔顿, 卢卡·范阿舍, 阿科尔体育馆"
        },
        "f1": {
            "tagline": "圣保罗大奖赛第三次练习：维斯塔潘领先安东内利0.025秒。",
            "liveNow": "第三次练习：维斯塔潘1:11.622，安东内利+0.025秒，诺里斯+0.131秒。排位赛暂不发布。梅赛德斯630，法拉利504。",
            "pulse": "F1英特拉格斯第三次练习：维斯塔潘领先0.025秒；排位赛暂不发布",
            "keywords": "一级方程式, 圣保罗大奖赛, 英特拉格斯, 维斯塔潘, 安东内利, 诺里斯"
        },
        "golf": {
            "tagline": "WWT锦标赛第二轮：本·詹姆斯64杆以15杆优势领先埃尔卡多纳尔。",
            "liveNow": "第二轮结束：詹姆斯129（-15）领先马尔纳蒂130。柯克135。晋级线139。第三轮暂不发布。",
            "pulse": "PGA巡回赛卡沃第二轮：詹姆斯129领跑WWT；第三轮暂不发布",
            "keywords": "PGA巡回赛, WWT锦标赛, 本·詹姆斯, 埃尔卡多纳尔, 迪亚曼特, 洛斯卡沃斯"
        },
        "home": {
            "tonight": "周六台",
            "tonightBlurb": "东契奇53分湖人胜开拓者。利兹1-0热刺。谢尔顿进巴黎决赛。维斯塔潘领第三次练习。詹姆斯129卡沃。猛虎周日马德里对猎鹰。",
            "plTitle": "NBA：东契奇砍下53分，湖人124-118逆转开拓者",
            "plBlurb": "生涯第11次50+。里夫斯25分。马刺7胜2负。骑士5胜4负。",
            "f1Title": "英超第10轮：奥卡福尔绝杀，利兹联1-0击败热刺",
            "f1Blurb": "奥卡福尔第79分钟、上场97秒破门。周五：埃弗顿3-1考文垂。阿森纳对赫尔暂不发布。"
        },
        "pg": {
            "pinFinal": "NFL第9周马德里待赛：猛虎周日美东9:30对猎鹰。最近完场：美洲虎33-10乌鸦。",
            "week1Closed": "NFL第9周：周六无赛。周四夜赛美洲虎33-10仍为最近完场。周日马德里暂无比分。",
            "week1Sub": "猛虎5胜2负，猎鹰3胜5负，伯纳乌。钢人6胜2负，第9周轮空。",
            "countdownTnf": "第9周周四夜赛仍成立：美洲虎33-10乌鸦。下一场：11月8日马德里猛虎对猎鹰。",
            "barsPoints": "梅赛德斯车队积分630，领先法拉利126分（504）。第三次练习：维斯塔潘1:11.622。排位赛暂不发布。",
            "tableAfterMonday": "英超已完赛第10轮：阿森纳9场24分，曼城21，布莱顿19，切尔西16，埃弗顿10场16，利兹10场14。",
            "pinClub": "选择俱乐部。阿森纳9场24分，曼城21，埃弗顿10场16，利兹10场14。赫尔暂不发布。",
            "plFootnote": "第10轮已完赛：利兹1-0热刺（奥卡福尔79），埃弗顿3-1考文垂。阿森纳对赫尔暂不发布。",
            "majorsDone": "PGA巡回赛：本·詹姆斯第二轮后129（-15）领跑WWT；马尔纳蒂130。第三轮暂不发布。"
        }
    },
    "ja": {
        "football": {
            "tagline": "NFL第9週マドリード：ベンガルズが日曜午前9時30分ETにベルナベウでファルコンズと対戦。土曜に試合なし。",
            "liveNow": "日曜マドリード予定：ベンガルズ（5勝2敗）対ファルコンズ（3勝5敗）、東部9時30分、NFLネットワーク。直近確定：ジャガーズ33-10レイブンズ。土曜なし。",
            "pulse": "NFL第9週マドリード：日曜ベンガルズ対ファルコンズ；直近確定ジャガーズ33-10",
            "keywords": "NFL第9週, シンシナティ・ベンガルズ, アトランタ・ファルコンズ, マドリード, ベルナベウ, ジョー・バロウ"
        },
        "basketball": {
            "tagline": "NBA：ルカ・ドンチッチが53得点、レイカーズがトレイルブレイザーズに124-118。",
            "liveNow": "ロサンゼルス終了：レイカーズ124、トレイルブレイザーズ118。ドンチッチ53；リーブス25。スパーズ7勝2敗。キャブス5勝4敗。",
            "pulse": "NBA：ドンチッチ53得点でレイカーズ124-118；スパーズ7-2、キャブス5-4",
            "keywords": "NBA, レイカーズ, トレイルブレイザーズ, ドンチッチ, リーブス"
        },
        "soccer": {
            "tagline": "プレミアリーグ第10節：オカフォが決勝点、リーズがトッテナムに1-0。アーセナルは9試合24のまま。",
            "liveNow": "エランド・ロード終了：リーズ1-0トッテナム（オカフォ79分）。金曜：エバートン3-1コヴェントリー。アーセナル対ハルは未掲載。",
            "pulse": "プレミアリーグ第10節：オカフォ79分の決勝点でリーズがトッテナムに1-0",
            "keywords": "プレミアリーグ, リーズ, トッテナム, オカフォ, エバートン, コヴェントリー"
        },
        "tennis": {
            "tagline": "パリ・マスターズ準決勝：シェルトンがバンアッシェに5-7、6-3、6-4で勝ち決勝へ。",
            "liveNow": "パリ・マスターズ準決勝：シェルトン5-7、6-3、6-4。2017年ソック以来の米国人決勝進出。アルカラス対ルードは未掲載。",
            "pulse": "パリ・マスターズ：シェルトンがバンアッシェを破りベルシー決勝へ",
            "keywords": "ATP, パリ・マスターズ, ベン・シェルトン, ルカ・バンアッシェ, アコール・アリーナ"
        },
        "f1": {
            "tagline": "サンパウロGP FP3：フェルスタッペンがアントネッリに0.025秒差で首位。",
            "liveNow": "FP3：フェルスタッペン1:11.622、アントネッリ+0.025秒、ノリス+0.131秒。予選未掲載。メルセデス630、フェラーリ504。",
            "pulse": "F1インテルラゴスFP3：フェルスタッペンが0.025秒差；予選未掲載",
            "keywords": "F1, サンパウロGP, インテルラゴス, フェルスタッペン, アントネッリ, ノリス"
        },
        "golf": {
            "tagline": "WWT選手権第2ラウンド：ベン・ジェームズが64を出し15アンダーで首位。",
            "liveNow": "R2終了：ジェームズ129（-15）がマルナティ130をリード。カーク135。カット139。第3ラウンド未掲載。",
            "pulse": "PGAツアーカボR2：ベン・ジェームズ129がWWT首位；第3ラウンド未掲載",
            "keywords": "PGAツアー, WWT選手権, ベン・ジェームズ, エル・カルドナル, ディアマンテ, ロスカボス"
        },
        "home": {
            "tonight": "土曜デスク",
            "tonightBlurb": "ドンチッチ53得点でレイカーズ勝利。リーズ1-0トッテナム。シェルトンがパリ決勝へ。フェルスタッペンがFP3首位。ジェームズ129。日曜マドリードはベンガルズ対ファルコンズ。",
            "plTitle": "NBA：ルカ・ドンチッチが53得点、レイカーズがトレイルブレイザーズに124-118",
            "plBlurb": "キャリア11度目の50得点。リーブス25。スパーズ7勝2敗。キャブス5勝4敗。",
            "f1Title": "プレミアリーグ第10節：オカフォが決勝点、リーズがトッテナムに1-0",
            "f1Blurb": "オカフォ79分、投入97秒。金曜：エバートン3-1コヴェントリー。アーセナル対ハルは未掲載。"
        },
        "pg": {
            "pinFinal": "NFL第9週マドリード予定：日曜9時30分ETベンガルズ対ファルコンズ。直近確定：ジャガーズ33、レイブンズ10。",
            "week1Closed": "NFL第9週：土曜に試合なし。TNFジャガーズ33-10が直近確定。日曜マドリードはスコアなし。",
            "week1Sub": "ベンガルズ5勝2敗、ファルコンズ3勝5敗、ベルナベウ。スティーラーズ6勝2敗、第9週バイ。",
            "countdownTnf": "第9週TNFは有効：ジャガーズ33-10レイブンズ。次は11月8日マドリードCIN対ATL。",
            "barsPoints": "メルセデスがコンストラクター630点、フェラーリ（504）に126差。FP3：フェルスタッペン1:11.622。予選未掲載。",
            "tableAfterMonday": "終了した第10節：アーセナル9試合24、シティ21、ブライトン19、チェルシー16、エバートン10試合16、リーズ10試合14。",
            "pinClub": "クラブを選ぶ。アーセナル9試合24、シティ21、エバートン10試合16、リーズ10試合14。ハル未掲載。",
            "plFootnote": "第10節終了分：リーズ1-0トッテナム（オカフォ79）、エバートン3-1コヴェントリー。アーセナル対ハル未掲載。",
            "majorsDone": "PGAツアー：ベン・ジェームズR2後129（-15）がWWT首位；マルナティ130。第3ラウンド未掲載。"
        }
    },
    "ko": {
        "football": {
            "tagline": "NFL 9주차 마드리드: 벵걸스가 일요일 동부 9시 30분 베르나베우에서 팰컨스와 대결. 토요일 경기 없음.",
            "liveNow": "일요일 마드리드 예정: 벵걸스(5승 2패) 대 팰컨스(3승 5패), 동부 9시 30분, NFL 네트워크. 최근 확정: 재규어스 33-10 레이븐스. 토요일 없음.",
            "pulse": "NFL 9주차 마드리드: 일요일 벵걸스 대 팰컨스; 최근 확정 재규어스 33-10",
            "keywords": "NFL 9주차, 신시내티 벵걸스, 애틀랜타 팰컨스, 마드리드, 베르나베우, 조 버로"
        },
        "basketball": {
            "tagline": "NBA: 루카 돈치치 53점, 레이커스가 트레일 블레이저스 124-118 제압.",
            "liveNow": "로스앤젤레스 종료: 레이커스 124, 트레일 블레이저스 118. 돈치치 53; 리브스 25. 스퍼스 7승 2패. 캐브스 5승 4패.",
            "pulse": "NBA: 돈치치 53점 레이커스 124-118; 스퍼스 7-2, 캐브스 5-4",
            "keywords": "NBA, 레이커스, 트레일 블레이저스, 돈치치, 리브스"
        },
        "soccer": {
            "tagline": "프리미어리그 10라운드: 오카포르 결승골, 리즈가 토트넘에 1-0. 아스널은 9경기 24점 유지.",
            "liveNow": "엘랜드 로드 종료: 리즈 1-0 토트넘(오카포르 79). 금요일: 에버턴 3-1 코번트리. 아스널 대 헐 미공개.",
            "pulse": "프리미어리그 10라운드: 오카포르 79분 결승골로 리즈 1-0 토트넘",
            "keywords": "프리미어리그, 리즈, 토트넘, 오카포르, 에버턴, 코번트리"
        },
        "tennis": {
            "tagline": "파리 마스터스 준결승: 셸턴, 반 아슈에 5-7 6-3 6-4 승리하고 결승 진출.",
            "liveNow": "파리 마스터스 준결승: 셸턴 5-7 6-3 6-4. 2017 속 이후 첫 미국 결승. 알카라스 대 루드 미공개.",
            "pulse": "파리 마스터스: 셸턴이 반 아슈를 꺾고 베르시 결승 진출",
            "keywords": "ATP, 파리 마스터스, 벤 셸턴, 루카 반 아슈, 아코르 아레나"
        },
        "f1": {
            "tagline": "상파울루 GP FP3: 베르스타펜이 안토넬리를 0.025초 차로 선두.",
            "liveNow": "FP3: 베르스타펜 1:11.622, 안토넬리 +0.025초, 노리스 +0.131초. 예선 미공개. 메르세데스 630, 페라리 504.",
            "pulse": "F1 인테를라고스 FP3: 베르스타펜 0.025초 선두; 예선 미공개",
            "keywords": "포뮬러 1, 상파울루 GP, 인테를라고스, 베르스타펜, 안토넬리, 노리스"
        },
        "golf": {
            "tagline": "WWT 챔피언십 2라운드: 벤 제임스가 64타로 15언더 선두.",
            "liveNow": "R2 종료: 제임스 129(-15)가 말나티 130 선두. 커크 135. 컷 139. 3라운드 미공개.",
            "pulse": "PGA 투어 카보 R2: 벤 제임스 129 WWT 선두; 3라운드 미공개",
            "keywords": "PGA 투어, WWT 챔피언십, 벤 제임스, 엘 카르도날, 디아만테, 로스카보스"
        },
        "home": {
            "tonight": "토요일 데스크",
            "tonightBlurb": "돈치치 53점 레이커스 승리. 리즈 1-0 토트넘. 셸턴 파리 결승. 베르스타펜 FP3 선두. 제임스 129 카보. 일요일 마드리드 벵걸스-팰컨스.",
            "plTitle": "NBA: 루카 돈치치 53점, 레이커스가 트레일 블레이저스 124-118 제압",
            "plBlurb": "커리어 11번째 50점. 리브스 25. 스퍼스 7승 2패. 캐브스 5승 4패.",
            "f1Title": "프리미어리그 10라운드: 오카포르 결승골, 리즈가 토트넘에 1-0",
            "f1Blurb": "오카포르 79분, 투입 97초. 금요일: 에버턴 3-1 코번트리. 아스널 대 헐 미공개."
        },
        "pg": {
            "pinFinal": "NFL 9주차 마드리드 예정: 일요일 동부 9시 30분 벵걸스 대 팰컨스. 최근 확정: 재규어스 33, 레이븐스 10.",
            "week1Closed": "NFL 9주차: 토요일 경기 없음. TNF 재규어스 33-10이 최근 확정. 일요일 마드리드는 점수 없음.",
            "week1Sub": "벵걸스 5승 2패, 팰컨스 3승 5패, 베르나베우. 스틸러스 6승 2패, 9주차 바이.",
            "countdownTnf": "9주차 TNF 유효: 재규어스 33-10 레이븐스. 다음은 11월 8일 마드리드 CIN 대 ATL.",
            "barsPoints": "메르세데스가 컨스트럭터 630점, 페라리(504)에 126점 차. FP3: 베르스타펜 1:11.622. 예선 미공개.",
            "tableAfterMonday": "끝난 10라운드: 아스널 9경기 24, 시티 21, 브라이턴 19, 첼시 16, 에버턴 10경기 16, 리즈 10경기 14.",
            "pinClub": "클럽을 고르세요. 아스널 9경기 24, 시티 21, 에버턴 10경기 16, 리즈 10경기 14. 헐 미공개.",
            "plFootnote": "10라운드 종료분: 리즈 1-0 토트넘(오카포르 79), 에버턴 3-1 코번트리. 아스널 대 헐 미공개.",
            "majorsDone": "PGA 투어: 벤 제임스 R2 후 129(-15) WWT 선두; 말나티 130. 3라운드 미공개."
        }
    },
    "ar": {
        "football": {
            "tagline": "الدوري الامريكي الاسبوع 9 مدريد: بنغالز يلاقي فالكونز في البرنابيو الاحد الساعة 9:30 بتوقيت شرق امريكا. لا مباراة السبت.",
            "liveNow": "الاحد في مدريد: بنغالز (5-2) ضد فالكونز (3-5)، 9:30 صباحا، NFL Network. اخر نتيجة: جاغوارز 33، ريڤنز 10. لا سبت.",
            "pulse": "الدوري الامريكي الاسبوع 9 مدريد: بنغالز ضد فالكونز الاحد؛ اخر نتيجة جاغوارز 33-10",
            "keywords": "الدوري الامريكي, بنغالز, فالكونز, مدريد, برنابيو, جو بارو"
        },
        "basketball": {
            "tagline": "دوري السلة: لوكا دونتشيتش يسجل 53 ويقود ليكرز لفوز 124-118 على تريل بليزرز.",
            "liveNow": "النهاية في لوس انجلوس: ليكرز 124، تريل بليزرز 118. دونتشيتش 53؛ ريفز 25. سبيرز 7-2. كافز 5-4.",
            "pulse": "دوري السلة: دونتشيتش 53 وليكرز 124-118 على بليزرز؛ سبيرز 7-2 وكافز 5-4",
            "keywords": "دوري السلة, ليكرز, تريل بليزرز, دونتشيتش, ريفز"
        },
        "soccer": {
            "tagline": "الدوري الانجليزي الجولة 10: هدف نوح اوكافور يمنح ليدز الفوز 1-0 على توتنهام. ارسنال ما زال 24 من 9.",
            "liveNow": "النهاية في ايلاند رود: ليدز 1-0 توتنهام (اوكافور 79). الجمعة: ايفرتون 3-1 كوفنتري. ارسنال ضد هال غير منشور.",
            "pulse": "الدوري الانجليزي الجولة 10: اوكافور في الدقيقة 79 يحسم 1-0 لليدز على توتنهام",
            "keywords": "الدوري الانجليزي, ليدز, توتنهام, اوكافور, ايفرتون, كوفنتري"
        },
        "tennis": {
            "tagline": "باريس ماسترز نصف النهائي: بن شيلتون يهزم لوكا فان آش 5-7 و6-3 و6-4 ويبلغ النهائي.",
            "liveNow": "باريس ماسترز نصف النهائي: شيلتون 5-7 و6-3 و6-4. اول اميركي في النهائي منذ سوك 2017. الكاراز ضد رود غير منشور.",
            "pulse": "باريس ماسترز: بن شيلتون يهزم فان آش ويبلغ نهائي بيرسي",
            "keywords": "تنس, باريس ماسترز, بن شيلتون, لوكا فان آش, اكور ارينا"
        },
        "f1": {
            "tagline": "جائزة ساو باولو الحصة الثالثة: ماكس فيرستابن يتقدم على كيمي انطونيلي بـ0.025 ثانية في انترلاغوس.",
            "liveNow": "الحصة الثالثة: فيرستابن 1:11.622، انطونيلي +0.025ث، نوريس +0.131ث. التصفيات غير منشورة. مرسيدس 630 وفيراري 504.",
            "pulse": "فورمولا 1 انترلاغوس الحصة الثالثة: فيرستابن بفارق 0.025ث؛ التصفيات غير منشورة",
            "keywords": "فورمولا 1, جائزة ساو باولو, انترلاغوس, فيرستابن, انطونيلي, نوريس"
        },
        "golf": {
            "tagline": "بطولة WWT الجولة الثانية: بن جيمس يسجل 64 ويتقدم بـ15 تحت في ال كاردونال.",
            "liveNow": "الجولة الثانية انتهت: جيمس 129 (-15) امام مالناتي 130. كيرك 135. القطع 139. الجولة الثالثة غير منشورة.",
            "pulse": "PGA تور كابو الجولة الثانية: بن جيمس 129 في الصدارة؛ الجولة الثالثة غير منشورة",
            "keywords": "PGA تور, بطولة WWT, بن جيمس, ال كاردونال, ديامانتي, لوس كابوس"
        },
        "home": {
            "tonight": "مكتب السبت",
            "tonightBlurb": "دونتشيتش 53 وليكرز يفوز. ليدز 1-0 توتنهام. شيلتون الى نهائي باريس. فيرستابن يتصدر الحصة الثالثة. جيمس 129 في كابو. بنغالز-فالكونز الاحد في مدريد.",
            "plTitle": "دوري السلة: لوكا دونتشيتش يسجل 53 ويقود ليكرز لفوز 124-118 على تريل بليزرز",
            "plBlurb": "المباراة الحادية عشرة بـ50 نقطة. ريفز 25. سبيرز 7-2. كافز 5-4.",
            "f1Title": "الدوري الانجليزي الجولة 10: هدف نوح اوكافور يمنح ليدز الفوز 1-0 على توتنهام",
            "f1Blurb": "اوكافور في الدقيقة 79 بعد 97 ثانية من دخوله. الجمعة: ايفرتون 3-1 كوفنتري. ارسنال ضد هال غير منشور."
        },
        "pg": {
            "pinFinal": "الدوري الامريكي الاسبوع 9 مدريد قادم: بنغالز-فالكونز الاحد 9:30. اخر نتيجة: جاغوارز 33، ريڤنز 10.",
            "week1Closed": "الدوري الامريكي الاسبوع 9: لا مباراة السبت. اخر نتيجة الخميس جاغوارز 33-10. مدريد الاحد بلا نتيجة.",
            "week1Sub": "بنغالز 5-2، فالكونز 3-5 في البرنابيو. ستيلرز 6-2 في راحة الاسبوع 9.",
            "countdownTnf": "خميس الاسبوع 9 ما زال قائما: جاغوارز 33، ريڤنز 10. التالي: سينسيناتي في اتلانتا مدريد 8 نوفمبر.",
            "barsPoints": "مرسيدس تتقدم في بطولة الصانعين بـ630 نقطة، بفارق 126 عن فيراري (504). الحصة الثالثة: فيرستابن 1:11.622. التصفيات غير منشورة.",
            "tableAfterMonday": "البريميرليغ بعد مباريات الجولة 10 المكتملة: ارسنال 24 من 9، سيتي 21، برايتون 19، تشيلسي 16، ايفرتون 16 من 10، ليدز 14 من 10.",
            "pinClub": "اختر ناديا. ارسنال 24 من 9، سيتي 21، ايفرتون 16 من 10، ليدز 14 من 10. هال غير منشور.",
            "plFootnote": "الجولة 10 المكتملة: ليدز 1-0 توتنهام (اوكافور 79)، ايفرتون 3-1 كوفنتري. ارسنال ضد هال غير منشور.",
            "majorsDone": "PGA تور: بن جيمس 129 (-15) يتصدر بطولة WWT بعد الجولة الثانية؛ مالناتي 130. الجولة الثالثة غير منشورة."
        }
    },
}

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

print("All locale updates for 7 Nov 2026 completed successfully!")
