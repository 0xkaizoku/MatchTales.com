# -*- coding: utf-8 -*-
"""
Update playground.ts, messages.ts, and all messages-*.ts files for 2 November 2026.
"""
import re
import os

DATA = {
    "en": {
        "football": {
            "tagline": "NFL Week 8 MNF: Steelers overpower Giants 26-18 behind Calvin Austin's two touchdowns and ferocious pass rush.",
            "liveNow": "Final in Pittsburgh: Steelers 26, Giants 18. Austin 2 TD (73-yd punt ret, 29-yd rec); Wilson 278 yds; Watt 2 sacks. Steelers improve to 6-2.",
            "pulse": "NFL WEEK 8 MNF: PITTSBURGH STEELERS TOP GIANTS 26-18 TO LEAD AFC NORTH AT 6-2",
            "keywords": "NFL Week 8, Pittsburgh Steelers, New York Giants, Calvin Austin, Russell Wilson, T.J. Watt, MNF"
        },
        "basketball": {
            "tagline": "NBA Thriller: Donovan Mitchell sinks baseline jumper with 0.3 seconds left as Cavaliers edge Bucks 114-113.",
            "liveNow": "Final in Milwaukee: Cavaliers 114, Bucks 113. Mitchell 30 pts (game-winner 0.3s) answers Lillard's 41 pts (10 threes). Cleveland moves to 7-0.",
            "pulse": "NBA THRILLER: DONOVAN MITCHELL HITS GAME-WINNER AS CAVALIERS STAY UNBEATEN (7-0)",
            "keywords": "NBA, Cavaliers, Bucks, Donovan Mitchell, Damian Lillard, Giannis Antetokounmpo, buzzer-beater"
        },
        "soccer": {
            "tagline": "Premier League MW9: Harry Wilson scores sensational stoppage-time brace as Fulham stun Brentford 2-1.",
            "liveNow": "Final at Craven Cottage: Fulham 2-1 Brentford (Wilson 90+2', 90+7'; Janelt 24'). Fulham climb to 8 points after dramatic derby comeback.",
            "pulse": "PREMIER LEAGUE MW9: HARRY WILSON 97TH-MINUTE HEADER CAPS MIRACLE FULHAM COMEBACK",
            "keywords": "Premier League, Fulham, Brentford, Harry Wilson, Craven Cottage, West London derby"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters: Stefanos Tsitsipas rallies past Roberto Carballes Baena 4-6, 6-3, 6-3 in Bercy opener.",
            "liveNow": "Paris Masters R64: Tsitsipas def. Carballes Baena 4-6, 6-3, 6-3 in 2h07m. Tsitsipas fires 37 winners and 11 aces to keep ATP Finals bid alive.",
            "pulse": "ROLEX PARIS MASTERS: STEFANOS TSITSIPAS BATTLES BACK TO WIN THREE-SET BERCY OPENER",
            "keywords": "ATP, Rolex Paris Masters, Tsitsipas, Carballes Baena, Accor Arena, Bercy, ATP Finals"
        },
        "f1": {
            "tagline": "São Paulo GP Preview: Fresh off Antonelli's coronation, F1 heads to Interlagos for high-stakes Constructors' showdown.",
            "liveNow": "Next up: Grande Prêmio de São Paulo (6-8 Nov). Mercedes (607 pts) lead Ferrari (474 pts) by 133 points heading into Interlagos Sprint weekend.",
            "pulse": "F1 INTERLAGOS PREVIEW: MERCEDES AND FERRARI CLASH IN SAO PAULO SPRINT SHOWDOWN",
            "keywords": "Formula 1, São Paulo GP, Interlagos, Antonelli, Ferrari, Mercedes, Constructors Championship"
        },
        "golf": {
            "tagline": "WWT Championship Preview: Following Pereda's historic triumph, PGA Tour arrives in Cabo with FedExCup cards on the line.",
            "liveNow": "Next up at El Cardonal at Diamante (5-8 Nov). Raul Pereda vaults into world top 50; Smotherman and Rai chase redemption in Los Cabos.",
            "pulse": "PGA TOUR CABO PREVIEW: PLAYERS CHASE TOP 125 STATUS AT TIGER WOODS-DESIGNED DIAMANTE",
            "keywords": "PGA Tour, WWT Championship, Los Cabos, El Cardonal, Diamante, Raul Pereda, Smotherman"
        },
        "home": {
            "tonight": "Monday desk",
            "tonightBlurb": "Steelers top Giants on MNF to lead AFC North. Mitchell hits buzzer-beater as Cavaliers stay 7-0. Wilson stoppage-time brace lifts Fulham.",
            "plTitle": "NFL Week 8 MNF: Steelers overpower Giants 26-18 behind Calvin Austin",
            "plBlurb": "Calvin Austin III scores on 73-yard punt return and 29-yard catch as T.J. Watt and Pittsburgh defense seal sole possession of first place in AFC North.",
            "f1Title": "NBA Thriller: Donovan Mitchell hits game-winner with 0.3s left as Cavaliers edge Bucks 114-113",
            "f1Blurb": "Mitchell scores 30 points and hits baseline dagger to answer Damian Lillard's 41 points and preserve Cleveland's flawless 7-0 start."
        },
        "pg": {
            "pinFinal": "NFL Week 8 MNF: Steelers 26, Giants 18. Austin 2 TDs, Wilson 278 yds, Watt 2 sacks.",
            "week1Closed": "NFL Week 8 MNF: Steelers beat Giants 26-18 to improve to 6-2 atop AFC North.",
            "week1Sub": "Calvin Austin 73-yd punt return and 29-yd rec TD. Steelers (6-2) take AFC North lead.",
            "countdownTnf": "Week 8 Final: Steelers 26, Giants 18 on MNF. Undefeated Vikings stand 7-0.",
            "barsPoints": "Mercedes leads Constructors with 607 pts, ahead of Ferrari (474) by 133 pts heading to Interlagos.",
            "tableAfterMonday": "Premier League Matchweek 9: City lead with 24 pts, Arsenal 22, Liverpool and Chelsea 16, Fulham 8.",
            "pinClub": "Select a club. City lead on 24, Arsenal 22, Liverpool and Chelsea 16, Brentford 11, Fulham 8.",
            "plFootnote": "PL MW9: Fulham 2-1 Brentford, Chelsea 2-1 Newcastle, Arsenal 2-2 Liverpool, Man City 1-0 Southampton.",
            "majorsDone": "PGA Tour: Raul Pereda (-17, 267) wins historic Mexico Open; Tour heads to Cabo for WWT Championship."
        }
    },
    "fr": {
        "football": {
            "tagline": "NFL Semaine 8 MNF : Les Steelers dominent les Giants 26-18 grace a Calvin Austin et une defense impenetrable.",
            "liveNow": "Score final a Pittsburgh : Steelers 26, Giants 18. Austin 2 TD (retour de punt de 73 yds, passe de 29 yds) ; Wilson 278 yds. Pittsburgh a 6-2.",
            "pulse": "NFL SEMAINE 8 MNF : LES PITTSBURGH STEELERS S'IMPOSENT 26-18 ET PRENNENT LA TETE DE L'AFC NORD",
            "keywords": "NFL Semaine 8, Pittsburgh Steelers, New York Giants, Calvin Austin, Russell Wilson, T.J. Watt"
        },
        "basketball": {
            "tagline": "NBA thriller : Donovan Mitchell reussit le tir de la gagne a 0,3 seconde du terme, les Cavaliers battent les Bucks 114-113.",
            "liveNow": "Fin de match a Milwaukee : Cavaliers 114, Bucks 113. Mitchell 30 pts (panier decisif a 0,3s) repond aux 41 pts de Lillard. Cleveland a 7-0.",
            "pulse": "NBA THRILLER : DONOVAN MITCHELL CRUCIFIE LES BUCKS ET GARDE CLEVELAND INVAINCU A 7-0",
            "keywords": "NBA, Cavaliers, Bucks, Donovan Mitchell, Damian Lillard, Giannis Antetokounmpo"
        },
        "soccer": {
            "tagline": "Premier League J9 : Harry Wilson signe un double magique dans le temps additionnel, Fulham renverse Brentford 2-1.",
            "liveNow": "Fin de match a Craven Cottage : Fulham 2-1 Brentford (Wilson 90+2', 90+7' ; Janelt 24'). Fulham remonte a 8 points.",
            "pulse": "PREMIER LEAGUE J9 : LE DOUBLÉ MIRACULEUX D'HARRY WILSON DANS LES ARRETS DE JEU FAIT GAGNER FULHAM",
            "keywords": "Premier League, Fulham, Brentford, Harry Wilson, Craven Cottage"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters : Stefanos Tsitsipas renverse Roberto Carballes Baena 4-6, 6-3, 6-3 pour son entree a Bercy.",
            "liveNow": "Paris Masters premier tour : Tsitsipas bat Carballes Baena 4-6, 6-3, 6-3 en 2h07. 37 winners et 11 aces pour le Grec.",
            "pulse": "ROLEX PARIS MASTERS : STEFANOS TSITSIPAS S'EN SORT EN TROIS MANCHES A BERCY",
            "keywords": "ATP, Rolex Paris Masters, Tsitsipas, Carballes Baena, Accor Arena"
        },
        "f1": {
            "tagline": "Presentation GP de São Paulo : Apres le sacre d'Antonelli, la F1 file a Interlagos pour la bataille des constructeurs.",
            "liveNow": "Prochain rendez-vous : Grande Premio de São Paulo (6-8 nov). Mercedes (607 pts) devance Ferrari (474 pts) de 133 points avant le Sprint.",
            "pulse": "F1 INTERLAGOS : MERCEDES ET FERRARI SE DISPUTENT LE MONDIAL DES CONSTRUCTEURS AU BRESIL",
            "keywords": "Formule 1, GP de São Paulo, Interlagos, Antonelli, Ferrari, Mercedes"
        },
        "golf": {
            "tagline": "Presentation WWT Championship : Apres l'exploit de Pereda, le PGA Tour arrive a Los Cabos pour la course aux cartes.",
            "liveNow": "Prochaine etape a El Cardonal at Diamante (5-8 nov). Pereda dans le top 50 mondial ; Smotherman et Rai en quete de rachat.",
            "pulse": "PGA TOUR CABO : LES GOLFEURS A L'ASSAUT D'EL CARDONAL DESSINÉ PAR TIGER WOODS",
            "keywords": "PGA Tour, WWT Championship, Los Cabos, El Cardonal, Diamante, Pereda"
        },
        "home": {
            "tonight": "Desk du lundi",
            "tonightBlurb": "Les Steelers battent les Giants et dominent l'AFC Nord. Mitchell crucifie les Bucks sur le gong (7-0). Doublé inoui de Wilson a Fulham.",
            "plTitle": "NFL Semaine 8 MNF : Les Steelers ecrasent les Giants 26-18 portes par Calvin Austin",
            "plBlurb": "Calvin Austin III marque sur retour de punt de 73 yds et reception de 29 yds tandis que la defense de Pittsburgh prend la tete de sa division.",
            "f1Title": "NBA thriller : Donovan Mitchell reussit le panier de la victoire a 0,3s du buzzer (114-113)",
            "f1Blurb": "Mitchell compile 30 points et convertit le shoot de la gagne pour repondre aux 41 points de Lillard et porter Cleveland a 7-0."
        },
        "pg": {
            "pinFinal": "NFL Semaine 8 MNF : Steelers 26, Giants 18. Austin 2 TD, Wilson 278 yds, Watt 2 sacks.",
            "week1Closed": "NFL Semaine 8 MNF : Les Steelers battent les Giants 26-18 et menent l'AFC Nord a 6-2.",
            "week1Sub": "Austin marque deux TD decisifs. Les Steelers (6-2) s'emparent des commandes de leur division.",
            "countdownTnf": "Bilan Semaine 8 : Les Steelers gagnent 26-18 lundi. Les Vikings toujours parfaits a 7-0.",
            "barsPoints": "Mercedes mene chez les constructeurs avec 607 pts, 133 d'avance sur Ferrari (474) avant le Bresil.",
            "tableAfterMonday": "Premier League J9 : Man City premier avec 24 pts, Arsenal 22, Liverpool et Chelsea 16, Fulham 8.",
            "pinClub": "Choisissez un club. City mene a 24 pts, Arsenal 22, Liverpool et Chelsea 16, Fulham 8.",
            "plFootnote": "PL J9 : Fulham 2-1 Brentford, Chelsea 2-1 Newcastle, Arsenal 2-2 Liverpool, Man City 1-0 Southampton.",
            "majorsDone": "PGA Tour : Raul Pereda vainqueur historique au Mexique ; direction Los Cabos pour le WWT Championship."
        }
    },
    "es": {
        "football": {
            "tagline": "NFL Semana 8 MNF: Los Steelers superan 26-18 a los Giants con doblete de Calvin Austin y una defensa intratable.",
            "liveNow": "Final en Pittsburgh: Steelers 26, Giants 18. Austin 2 TD (retorno de 73 yds, pase de 29 yds); Wilson 278 yds; Watt 2 sacks. Pittsburgh con 6-2.",
            "pulse": "NFL SEMANA 8 MNF: PITTSBURGH STEELERS VENCEN A GIANTS Y MANDAN EN LA AFC NORTE CON 6-2",
            "keywords": "NFL Semana 8, Pittsburgh Steelers, New York Giants, Calvin Austin, Russell Wilson, T.J. Watt"
        },
        "basketball": {
            "tagline": "NBA Thriller: Donovan Mitchell anota la canasta ganadora a 0.3 segundos del final y Cavaliers superan 114-113 a Bucks.",
            "liveNow": "Final en Milwaukee: Cavaliers 114, Bucks 113. Mitchell 30 pts (game-winner a 0.3s) frena los 41 pts de Lillard. Cleveland se pone 7-0.",
            "pulse": "NBA THRILLER: DONOVAN MITCHELL DECIDE SOBRE LA BOCINA Y CLEVELAND SIGUE INVICTO CON 7-0",
            "keywords": "NBA, Cavaliers, Bucks, Donovan Mitchell, Damian Lillard, Giannis Antetokounmpo"
        },
        "soccer": {
            "tagline": "Premier League J9: Harry Wilson anota un doblete en el anadido y el Fulham remonta 2-1 al Brentford.",
            "liveNow": "Final en Craven Cottage: Fulham 2-1 Brentford (Wilson 90+2', 90+7'; Janelt 24'). Fulham alcanza 8 puntos tras epica remontada.",
            "pulse": "PREMIER LEAGUE J9: HARRY WILSON FIRMA UN DOBLETE HEROICO EN EL DESCUENTO PARA EL FULHAM",
            "keywords": "Premier League, Fulham, Brentford, Harry Wilson, Craven Cottage"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters: Stefanos Tsitsipas remonta a Roberto Carballes Baena 4-6, 6-3, 6-3 en su debut en Bercy.",
            "liveNow": "Paris Masters primera ronda: Tsitsipas bate a Carballes Baena 4-6, 6-3, 6-3 en 2h07m. 37 golpes ganadores del griego.",
            "pulse": "ROLEX PARIS MASTERS: STEFANOS TSITSIPAS REMONTA EN TRES SETS EN SU ESTRENO EN PARIS",
            "keywords": "ATP, Rolex Paris Masters, Tsitsipas, Carballes Baena, Accor Arena"
        },
        "f1": {
            "tagline": "Previa GP de São Paulo: Tras la coronacion de Antonelli, la F1 viaja a Interlagos para el asalto al mundial de constructores.",
            "liveNow": "Proxima cita: Grande Premio de São Paulo (6-8 nov). Mercedes (607 pts) aventaja a Ferrari (474 pts) en 133 puntos antes del Sprint.",
            "pulse": "F1 INTERLAGOS PREVIA: MERCEDES Y FERRARI COLISIONAN EN EL SPRINT DE SAO PAULO",
            "keywords": "Formula 1, GP de São Paulo, Interlagos, Antonelli, Ferrari, Mercedes"
        },
        "golf": {
            "tagline": "Previa WWT Championship: Tras la gloria de Pereda, el PGA Tour llega a Cabo con las tarjetas en juego.",
            "liveNow": "Proxima cita en El Cardonal at Diamante (5-8 nov). Pereda sube al top 50 mundial; Smotherman y Rai buscan revancha en Los Cabos.",
            "pulse": "PGA TOUR CABO: DUELO DECISIVO POR EL TOP 125 EN EL CAMPO DISENADO POR TIGER WOODS",
            "keywords": "PGA Tour, WWT Championship, Los Cabos, El Cardonal, Diamante, Pereda"
        },
        "home": {
            "tonight": "Edicion del lunes",
            "tonightBlurb": "Steelers vencen a Giants y mandan en la AFC Norte. Mitchell anota sobre la bocina (7-0). Remontada increible de Wilson con Fulham.",
            "plTitle": "NFL Semana 8 MNF: Steelers superan 26-18 a Giants liderados por Calvin Austin",
            "plBlurb": "Calvin Austin III anota en retorno de 73 yardas y recepcion de 29 yardas mientras T.J. Watt asegura el liderato acerero de la AFC Norte.",
            "f1Title": "NBA Thriller: Donovan Mitchell sella el triunfo a 0.3 segundos del final (114-113)",
            "f1Blurb": "Mitchell anota 30 puntos y la canasta de la victoria para neutralizar los 41 puntos de Lillard y mantener invicto a Cleveland con 7-0."
        },
        "pg": {
            "pinFinal": "NFL Semana 8 MNF: Steelers 26, Giants 18. Austin 2 TD, Wilson 278 yds, Watt 2 sacks.",
            "week1Closed": "NFL Semana 8 MNF: Steelers ganan 26-18 a Giants y lideran la AFC Norte con marca de 6-2.",
            "week1Sub": "Austin dos touchdowns claves. Los Steelers (6-2) toman el liderato solitario de division.",
            "countdownTnf": "Semana 8 final: Steelers 26-18 Giants en MNF. Vikings siguen perfectos con 7-0.",
            "barsPoints": "Mercedes manda en constructores con 607 pts, 133 por delante de Ferrari (474) rumbo a Interlagos.",
            "tableAfterMonday": "Premier League jornada 9: City lider con 24 pts, Arsenal 22, Liverpool y Chelsea 16, Fulham 8.",
            "pinClub": "Elige un club. City manda con 24, Arsenal 22, Liverpool y Chelsea 16, Fulham suma 8.",
            "plFootnote": "PL J9: Fulham 2-1 Brentford, Chelsea 2-1 Newcastle, Arsenal 2-2 Liverpool, Man City 1-0 Southampton.",
            "majorsDone": "PGA Tour: Raul Pereda campeon historico del Mexico Open; el tour se traslada a Cabo para el WWT Championship."
        }
    },
    "de": {
        "football": {
            "tagline": "NFL Woche 8 MNF: Steelers schlagen Giants 26:18 dank Calvin Austins Gala und dominanter Defense.",
            "liveNow": "Endstand in Pittsburgh: Steelers 26, Giants 18. Austin 2 TD (73-yd Punt-Return, 29-yd Pass); Wilson 278 Yds; Watt 2 Sacks. Steelers bei 6-2.",
            "pulse": "NFL WOCHE 8 MNF: PITTSBURGH STEELERS SCHLAGEN GIANTS 26:18 UND FUEHREN AFC NORTH AN",
            "keywords": "NFL Woche 8, Pittsburgh Steelers, New York Giants, Calvin Austin, Russell Wilson, T.J. Watt"
        },
        "basketball": {
            "tagline": "NBA Thriller: Donovan Mitchell trifft 0,3 Sekunden vor Schluss, Cavaliers schlagen Bucks 114:113.",
            "liveNow": "Endstand in Milwaukee: Cavaliers 114, Bucks 113. Mitchell 30 Pkt (Siegwurf 0,3s) kontert Lillards 41 Pkt. Cleveland bleibt bei 7-0.",
            "pulse": "NBA THRILLER: DONOVAN MITCHELL TRIFFT MIT DEM BUZZER ZUM SIEBENTEN CAVALIERS-SIEG (7-0)",
            "keywords": "NBA, Cavaliers, Bucks, Donovan Mitchell, Damian Lillard, Giannis Antetokounmpo"
        },
        "soccer": {
            "tagline": "Premier League 9. Spieltag: Harry Wilson trifft doppelt in der Nachspielzeit, Fulham dreht Derby gegen Brentford zum 2:1.",
            "liveNow": "Endstand im Craven Cottage: Fulham 2-1 Brentford (Wilson 90+2', 90+7'; Janelt 24'). Fulham klettert auf 8 Punkte.",
            "pulse": "PREMIER LEAGUE 9. SPIELTAG: HARRY WILSON SCHOCKT BRENTFORD MIT SPÄTEM DOPPELPACK",
            "keywords": "Premier League, Fulham, Brentford, Harry Wilson, Craven Cottage"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters: Stefanos Tsitsipas kaempft Roberto Carballes Baena 4:6, 6:3, 6:3 zum Auftakt nieder.",
            "liveNow": "Paris Masters 1. Runde: Tsitsipas siegt 4:6, 6:3, 6:3 in 2h07m. 37 Winner und 11 Asse fuer den Griechen.",
            "pulse": "ROLEX PARIS MASTERS: STEFANOS TSITSIPAS DREHT DREISATZKRIMI IN DER ACCOR ARENA",
            "keywords": "ATP, Rolex Paris Masters, Tsitsipas, Carballes Baena, Accor Arena"
        },
        "f1": {
            "tagline": "São Paulo GP Vorschau: Nach Antonellis Titel rast die Formel 1 zum Konstrukteurs-Showdown nach Interlagos.",
            "liveNow": "Naechstes Rennen: Grande Premio de São Paulo (6.-8. Nov). Mercedes (607 Pkt) fuehrt vor Ferrari (474 Pkt) vor dem Sprint.",
            "pulse": "F1 INTERLAGOS VORSCHAU: MERCEDES UND FERRARI KÄMPFEN IN SAO PAULO UM DEN TEAM-TITEL",
            "keywords": "Formel 1, São Paulo GP, Interlagos, Antonelli, Ferrari, Mercedes"
        },
        "golf": {
            "tagline": "WWT Championship Vorschau: Nach Peredas historischem Triumph reist die PGA Tour nach Cabo.",
            "liveNow": "Naechste Station: El Cardonal at Diamante (5.-8. Nov). Pereda in den Top 50; Smotherman und Rai starten Aufholjagd.",
            "pulse": "PGA TOUR CABO VORSCHAU: KAMPF UM DIE TOP-125-KARTEN AUF TIGER WOODS' KURS",
            "keywords": "PGA Tour, WWT Championship, Los Cabos, El Cardonal, Diamante, Pereda"
        },
        "home": {
            "tonight": "Montags-Desk",
            "tonightBlurb": "Steelers schlagen Giants im MNF und fuehren AFC North an. Mitchell trifft mit dem Buzzer (7-0). Wilson schiesst Fulham zum Derbysieg.",
            "plTitle": "NFL Woche 8 MNF: Steelers besiegen Giants 26:18 dank Doppelpack von Calvin Austin",
            "plBlurb": "Calvin Austin III ueberragt mit 73-Yard-Return und 29-Yard-Touchdown; T.J. Watt sichert Pittsburgh Platz eins in der AFC North.",
            "f1Title": "NBA Thriller: Donovan Mitchell trifft 0,3 Sekunden vor Ende zum 114:113 der Cavaliers",
            "f1Blurb": "Mitchell erzielt 30 Punkte und den Game-Winner gegen Lillards 41 Punkte und haelt Cleveland ungeschlagen bei 7-0."
        },
        "pg": {
            "pinFinal": "NFL Woche 8 MNF: Steelers 26, Giants 18. Austin 2 TD, Wilson 278 Yds, Watt 2 Sacks.",
            "week1Closed": "NFL Woche 8 MNF: Steelers bezwingen Giants 26:18 und fuehren AFC North mit 6-2 an.",
            "week1Sub": "Austin mit zwei Touchdowns. Die Steelers (6-2) erobern die alleinige Divisionsfuehrung.",
            "countdownTnf": "Woche 8 Endstand: Steelers siegen 26:18 am MNF. Vikings bleiben ungeschlagen bei 7-0.",
            "barsPoints": "Mercedes fuehrt Konstrukteurs-WM mit 607 Pkt vor Ferrari (474 Pkt) vor dem Brasilien-GP an.",
            "tableAfterMonday": "Premier League Tabelle J9: City fuehrt mit 24 Pkt, Arsenal 22, Liverpool und Chelsea 16, Fulham 8.",
            "pinClub": "Waehle einen Klub. City hat 24, Arsenal 22, Liverpool und Chelsea 16, Fulham steht bei 8.",
            "plFootnote": "PL J9: Fulham 2-1 Brentford, Chelsea 2-1 Newcastle, Arsenal 2-2 Liverpool, Man City 1-0 Southampton.",
            "majorsDone": "PGA Tour: Raul Pereda siegt historisch in Mexiko; Tour zieht weiter nach Cabo zur WWT Championship."
        }
    },
    "it": {
        "football": {
            "tagline": "NFL Week 8 MNF: Gli Steelers battono i Giants 26-18 con due magie di Calvin Austin e una difesa insuperabile.",
            "liveNow": "Finale a Pittsburgh: Steelers 26, Giants 18. Austin 2 TD (ritorno di punt da 73 yds, ricezione da 29 yds); Wilson 278 yds; Watt 2 sack. Pittsburgh a 6-2.",
            "pulse": "NFL WEEK 8 MNF: PITTSBURGH STEELERS SUPERANO I GIANTS 26-18 E VOLANO IN TESTA ALL'AFC NORTH",
            "keywords": "NFL Week 8, Pittsburgh Steelers, New York Giants, Calvin Austin, Russell Wilson, T.J. Watt"
        },
        "basketball": {
            "tagline": "NBA Thriller: Donovan Mitchell gela i Bucks a 0.3 secondi dalla fine, Cavaliers vittoriosi 114-113.",
            "liveNow": "Finale a Milwaukee: Cavaliers 114, Bucks 113. Mitchell 30 pts (canestro vincente a 0.3s) piega i 41 punti di Lillard. Cleveland vola a 7-0.",
            "pulse": "NBA THRILLER: DONOVAN MITCHELL SEGNA SULLA SIRENA E I CAVALIERS RESTANO IMBATTUTI (7-0)",
            "keywords": "NBA, Cavaliers, Bucks, Donovan Mitchell, Damian Lillard, Giannis Antetokounmpo"
        },
        "soccer": {
            "tagline": "Premier League 9ª giornata: Favola Harry Wilson nel recupero, doppietta e vittoria 2-1 del Fulham sul Brentford.",
            "liveNow": "Finale a Craven Cottage: Fulham 2-1 Brentford (Wilson 90+2', 90+7'; Janelt 24'). Il Fulham sale a 8 punti.",
            "pulse": "PREMIER LEAGUE 9ª GIORNATA: HARRY WILSON RIBALTA IL DERBY NEL RECUPERO PER IL FULHAM",
            "keywords": "Premier League, Fulham, Brentford, Harry Wilson, Craven Cottage"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters: Stefanos Tsitsipas piega Roberto Carballes Baena 4-6, 6-3, 6-3 al debutto a Bercy.",
            "liveNow": "Paris Masters primo turno: Tsitsipas batte Carballes Baena 4-6, 6-3, 6-3 in 2h07m. 37 vincenti per il greco.",
            "pulse": "ROLEX PARIS MASTERS: STEFANOS TSITSIPAS RIMONTA IN TRE SET E PASSA IL TURNO A PARIGI",
            "keywords": "ATP, Rolex Paris Masters, Tsitsipas, Carballes Baena, Accor Arena"
        },
        "f1": {
            "tagline": "Presentazione GP San Paolo: Dopo il titolo di Antonelli, la F1 approda a Interlagos per il duello costruttori.",
            "liveNow": "Prossimo evento: Grande Premio de São Paulo (6-8 nov). Mercedes (607 pts) precede Ferrari (474 pts) di 133 punti prima della Sprint.",
            "pulse": "F1 INTERLAGOS PRESENTAZIONE: MERCEDES E FERRARI SI CONTENDONO IL TITOLO A SAN PAOLO",
            "keywords": "Formula 1, GP San Paolo, Interlagos, Antonelli, Ferrari, Mercedes"
        },
        "golf": {
            "tagline": "Presentazione WWT Championship: Dopo l'impresa di Pereda, il PGA Tour sbarca a Los Cabos.",
            "liveNow": "Prossimo torneo a El Cardonal at Diamante (5-8 nov). Pereda nei primi 50 al mondo; Smotherman cerca il riscatto.",
            "pulse": "PGA TOUR CABO: CORSA AL TOP 125 SUL PERCORSO DISEGNATO DA TIGER WOODS",
            "keywords": "PGA Tour, WWT Championship, Los Cabos, El Cardonal, Diamante, Pereda"
        },
        "home": {
            "tonight": "Desk del lunedi",
            "tonightBlurb": "Steelers vincono il MNF e guidano l'AFC North. Mitchell canestro vincente sulla sirena (7-0). Doppietta prodigio di Wilson per il Fulham.",
            "plTitle": "NFL Week 8 MNF: Gli Steelers superano i Giants 26-18 guidati da Calvin Austin",
            "plBlurb": "Calvin Austin III protagonista con due touchdown mentre T.J. Watt e la difesa di Pittsburgh conquistano il primato solitario di divisione.",
            "f1Title": "NBA Thriller: Donovan Mitchell insacca a 0.3s dalla sirena, Cavaliers battono Bucks 114-113",
            "f1Blurb": "Mitchell firma 30 punti e il tiro decisivo rispondendo ai 41 punti di Lillard e regalando a Cleveland il settimo successo consecutivo."
        },
        "pg": {
            "pinFinal": "NFL Week 8 MNF: Steelers 26, Giants 18. Austin 2 TD, Wilson 278 yds, Watt 2 sack.",
            "week1Closed": "NFL Week 8 MNF: Steelers battono Giants 26-18 e guidano l'AFC North sul 6-2.",
            "week1Sub": "Austin protagonista con due touchdown. Gli Steelers (6-2) si issano al comando della divisione.",
            "countdownTnf": "Week 8 Finale: Steelers 26-18 Giants al MNF. Vikings restano perfetti a 7-0.",
            "barsPoints": "Mercedes guida la classifica costruttori con 607 punti, 133 davanti alla Ferrari (474) verso Interlagos.",
            "tableAfterMonday": "Classifica Premier League 9ª giornata: City prima con 24 pts, Arsenal 22, Liverpool e Chelsea 16, Fulham 8.",
            "pinClub": "Seleziona un club. City in vetta a 24, Arsenal 22, Liverpool e Chelsea 16, Fulham a 8.",
            "plFootnote": "PL 9ª g.: Fulham 2-1 Brentford, Chelsea 2-1 Newcastle, Arsenal 2-2 Liverpool, Man City 1-0 Southampton.",
            "majorsDone": "PGA Tour: Raul Pereda vince il Mexico Open; il circuito si sposta a Los Cabos per il WWT Championship."
        }
    },
    "pl": {
        "football": {
            "tagline": "NFL Tydzien 8 MNF: Steelers pokonuja Giants 26:18 dzieki dwoch przylozeniom Calvina Austina i zelaznej obronie.",
            "liveNow": "Koniec w Pittsburghu: Steelers 26, Giants 18. Austin 2 TD (73 yds punt return, 29 yds chwyt); Wilson 278 yds; Watt 2 sacki. Steelers maja 6-2.",
            "pulse": "NFL TYDZIEN 8 MNF: PITTSBURGH STEELERS OGRAJA GIANTS 26:18 I LIDERUJA W AFC NORTH (6-2)",
            "keywords": "NFL Tydzien 8, Pittsburgh Steelers, New York Giants, Calvin Austin, Russell Wilson, T.J. Watt"
        },
        "basketball": {
            "tagline": "NBA dreszczowiec: Donovan Mitchell trafia na 0,3 sekundy przed koncem, Cavaliers wygrywaja z Bucks 114:113.",
            "liveNow": "Koniec w Milwaukee: Cavaliers 114, Bucks 113. Mitchell 30 pkt (rzut meczowy 0,3s) odpowiada na 41 pkt Lillarda. Cleveland ma 7-0.",
            "pulse": "NBA DRESZCZOWIEC: DONOVAN MITCHELL TRAFIA Z SYRENA, CAVALIERS WCIĄŻ NIEPOKONANI (7-0)",
            "keywords": "NBA, Cavaliers, Bucks, Donovan Mitchell, Damian Lillard, Giannis Antetokounmpo"
        },
        "soccer": {
            "tagline": "Premier League 9. kolejka: Magiczny dublet Harry'ego Wilsona w doliczonym czasie gry, Fulham wygrywa 2:1 z Brentfordem.",
            "liveNow": "Koniec na Craven Cottage: Fulham 2-1 Brentford (Wilson 90+2', 90+7'; Janelt 24'). Fulham zdobywa 8 punktow po niesamowitym powrocie.",
            "pulse": "PREMIER LEAGUE 9. KOLEJKA: DWA GOLE WILSONA W KONCOWCE DAJA FULHAM DERBOWE ZWYCIESTWO",
            "keywords": "Premier League, Fulham, Brentford, Harry Wilson, Craven Cottage"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters: Stefanos Tsitsipas odrabia straty i wygrywa z Roberto Carballesem Baena 4:6, 6:3, 6:3 w Paryzu.",
            "liveNow": "Paris Masters 1. runda: Tsitsipas pokonuje Carballesa Baene 4:6, 6:3, 6:3 w 2h07m. 37 winnerow greckiego tenisisty.",
            "pulse": "ROLEX PARIS MASTERS: STEFANOS TSITSIPAS WYGRYWA TRZYSETOWY MECZ OTWARCIA W BERCY",
            "keywords": "ATP, Rolex Paris Masters, Tsitsipas, Carballes Baena, Accor Arena"
        },
        "f1": {
            "tagline": "Zapowiedz GP Sao Paulo: Po mistrzostwie Antonellego F1 przenosi sie na Interlagos na walke o tytul konstruktorow.",
            "liveNow": "Kolejny wyscig: Grande Premio de São Paulo (6-8 listopada). Mercedes (607 pkt) prowadzi przed Ferrari (474 pkt) o 133 punkty przed sprintem.",
            "pulse": "F1 INTERLAGOS ZAPOWIEDZ: MERCEDES I FERRARI WALCZA O MISTRZOSTWO W BRAZYLII",
            "keywords": "Formula 1, GP Sao Paulo, Interlagos, Antonelli, Ferrari, Mercedes"
        },
        "golf": {
            "tagline": "Zapowiedz WWT Championship: Po triumfie Peredy cykl PGA Tour dociera do Cabo w walce o karty na 2027.",
            "liveNow": "Kolejny turniej w El Cardonal at Diamante (5-8 listopada). Pereda w czolowej 50; Smotherman i Rai szukaja rewanzu.",
            "pulse": "PGA TOUR CABO: BÓJ O MIEJSCA W TOP 125 NA POLU ZAPROJEKTOWANYM PRZEZ TIGERA WOODSA",
            "keywords": "PGA Tour, WWT Championship, Los Cabos, El Cardonal, Diamante, Pereda"
        },
        "home": {
            "tonight": "Poniedzialkowy raport",
            "tonightBlurb": "Steelers pokonuja Giants w MNF i prowadza w dywizji. Mitchell trafia rzut meczowy (7-0). Niewiarygodny dublet Wilsona dla Fulham.",
            "plTitle": "NFL Tydzien 8 MNF: Steelers pokonuja Giants 26:18 po show Calvina Austina",
            "plBlurb": "Calvin Austin III zdobywa 2 przylozenia, a T.J. Watt i defensywa Pittsburgha daja druzynie samodzielne prowadzenie w AFC North.",
            "f1Title": "NBA dreszczowiec: Donovan Mitchell trafia na 0,3s przed syrena, Cavaliers gora 114:113",
            "f1Blurb": "Mitchell notuje 30 punktow i decydujacy rzut przeciwko 41 punktom Lillarda, utrzymujac bilans 7-0 dla Cleveland."
        },
        "pg": {
            "pinFinal": "NFL Tydzien 8 MNF: Steelers 26, Giants 18. Austin 2 TD, Wilson 278 yds, Watt 2 sacki.",
            "week1Closed": "NFL Tydzien 8 MNF: Steelers wygrywaja z Giants 26:18 i lideruja AFC North z bilansem 6-2.",
            "week1Sub": "Austin dwa kluczowe przylozenia. Steelers (6-2) obejmuja samodzielne prowadzenie.",
            "countdownTnf": "Podsumowanie Tygodnia 8: Steelers 26-18 Giants w MNF. Vikings wciaz bez porazki na 7-0.",
            "barsPoints": "Mercedes prowadzi wsrod konstruktorow z 607 pkt, o 133 punkty przed Ferrari (474) przed Interlagos.",
            "tableAfterMonday": "Tabela Premier League 9. kolejka: City na czele z 24 pkt, Arsenal 22, Liverpool i Chelsea 16, Fulham 8.",
            "pinClub": "Wybierz klub. City prowadzi z 24 pkt, Arsenal 22, Liverpool i Chelsea 16, Fulham ma 8.",
            "plFootnote": "PL 9. kol.: Fulham 2-1 Brentford, Chelsea 2-1 Newcastle, Arsenal 2-2 Liverpool, Man City 1-0 Southampton.",
            "majorsDone": "PGA Tour: Historyczny sukces Raula Peredy w Meksyku; kolejny przystanek to WWT Championship w Cabo."
        }
    },
    "zh": {
        "football": {
            "tagline": "NFL第8周周一夜赛：奥斯汀独中两元防线筑墙，钢人26-18击溃巨人领跑美北。",
            "liveNow": "匹兹堡终场：钢人26-18巨人。奥斯汀2达阵（73码弃踢回攻+29码接球）；威尔逊278码；瓦特2擒杀。钢人战绩升至6胜2负。",
            "pulse": "NFL第8周周一夜赛：匹兹堡钢人26-18力克巨人，以6胜2负独占美联北区第一",
            "keywords": "NFL第8周, 匹兹堡钢人, 纽约巨人, 卡尔文·奥斯汀, 威尔逊, 瓦特, 周一夜赛"
        },
        "basketball": {
            "tagline": "NBA焦点战：米切尔终场前0.3秒中投绝杀，骑士114-113险胜雄鹿豪取开季7连胜。",
            "liveNow": "密尔沃基终场：骑士114-113雄鹿。米切尔30分（0.3秒绝杀）对轰利拉德41分（10记三分）。克利夫兰开季7胜0负保持全胜。",
            "pulse": "NBA焦点战：米切尔极限绝杀助骑士险胜雄鹿，开季7连胜领跑全联盟",
            "keywords": "NBA, 骑士, 雄鹿, 多诺万·米切尔, 利拉德, 字母哥, 绝杀"
        },
        "soccer": {
            "tagline": "英超第9轮：威尔逊补时梅开二度演绝地逆转，富勒姆2-1绝杀布伦特福德德比称雄。",
            "liveNow": "克拉文农场终场：富勒姆2-1布伦特福德（威尔逊90+2'、90+7'；雅内尔特24'）。富勒姆上演惊天大逆转积分升至8分。",
            "pulse": "英超第9轮：哈里·威尔逊伤停补时连进两球，富勒姆2-1逆转绝杀布伦特福德",
            "keywords": "英超, 富勒姆, 布伦特福德, 哈里·威尔逊, 克拉文农场, 西伦敦德比"
        },
        "tennis": {
            "tagline": "劳力士巴黎大师赛：西西帕斯4-6、6-3、6-3逆转卡巴列斯，首战告捷保留总决赛希望。",
            "liveNow": "巴黎大师赛首轮：西西帕斯2小时7分钟激战逆转卡巴列斯。希腊名将轰出37记制胜分与11记ACE球挺进32强。",
            "pulse": "劳力士巴黎大师赛：西西帕斯贝尔西揭幕战三盘逆转，强势晋级32强",
            "keywords": "ATP, 劳力士巴黎大师赛, 西西帕斯, 卡巴列斯, 贝尔西体育馆"
        },
        "f1": {
            "tagline": "F1圣保罗大奖赛前瞻：安东内利加冕后F1移师英特拉格斯，梅赛德斯与法拉利打响车队冠军决战。",
            "liveNow": "下一站：圣保罗大奖赛（11月6-8日）。在冲刺赛周末前，梅赛德斯（607分）领先法拉利（474分）133分锁定车队卫冕关键战。",
            "pulse": "F1巴西站前瞻：英特拉格斯迎来冲刺赛决战，梅赛德斯与法拉利上演车队争霸",
            "keywords": "一级方程式, 圣保罗大奖赛, 英特拉格斯, 安东内利, 法拉利, 梅赛德斯"
        },
        "golf": {
            "tagline": "美巡赛WWT锦标赛前瞻：佩雷达历史性夺冠余威尚存，美巡转战卡博打响保卡生死战。",
            "liveNow": "下一站洛斯卡波斯卡多纳尔球场（11月5-8日）。佩雷达跃升世界前50；斯莫瑟曼与阿龙·莱力争反弹。",
            "pulse": "美巡赛卡博前瞻：群雄逐鹿老虎·伍兹设计球场，争夺秋季赛前125名参赛全卡",
            "keywords": "美巡赛, WWT锦标赛, 洛斯卡波斯, 卡多纳尔, 迪亚曼特, 佩雷达"
        },
        "home": {
            "tonight": "周一特别报道",
            "tonightBlurb": "钢人周一夜赛击溃巨人领跑美北。米切尔0.3秒中投绝杀（7-0）。威尔逊补时双响助富勒姆德比逆转。",
            "plTitle": "NFL第8周周一夜赛：钢人26-18击溃巨人，奥斯汀双达阵建功",
            "plBlurb": "奥斯汀上演73码弃踢回攻与29码接球达阵，瓦特携匹兹堡防线助球队以6胜2负独占美联北区榜首。",
            "f1Title": "NBA焦点战：米切尔终场前0.3秒中投绝杀，骑士114-113力克雄鹿",
            "f1Blurb": "米切尔轰下30分命中后仰压哨绝杀，硬撼利拉德41分与10记三分，率领克利夫兰开季7连胜保持不败。"
        },
        "pg": {
            "pinFinal": "NFL第8周MNF：钢人26-18巨人。奥斯汀2达阵，威尔逊278码，瓦特2擒杀。",
            "week1Closed": "NFL第8周MNF：钢人26-18力克巨人，以6胜2负领跑美联北区。",
            "week1Sub": "奥斯汀独中两元。钢人队（6-2）巩固美北第一宝座。",
            "countdownTnf": "第8周收官：钢人周一夜赛26-18胜巨人。维京人7-0独孤求败。",
            "barsPoints": "梅赛德斯车队以607分领跑车队榜，领先法拉利（474分）达133分进军英特拉格斯。",
            "tableAfterMonday": "英超第9轮积分榜：曼城24分领跑，阿森纳22分，利物浦与切尔西同积16分，富勒姆8分。",
            "pinClub": "选择俱乐部。曼城24分居首，阿森纳22，利物浦与切尔西16，富勒姆积分升至8分。",
            "plFootnote": "英超第9轮：富勒姆2-1布伦特福德，切尔西2-1纽卡，阿森纳2-2利物浦，曼城1-0南安普顿。",
            "majorsDone": "美巡赛：佩雷达本土历史性问鼎墨西哥赛；美巡移师卡博打响WWT锦标赛。"
        }
    },
    "ja": {
        "football": {
            "tagline": "NFL第8週MNF：スティーラーズがオースティンの2TDと強固な守備でジャイアンツを26-18で破り地区首位浮上。",
            "liveNow": "ピッツバーグ終結：スティーラーズ 26-18 ジャイアンツ。オースティン2TD（73ydパントリターン、29ydパス捕球）。通算6勝2敗。",
            "pulse": "NFL第8週MNF：ピッツバーグ・スティーラーズがジャイアンツを26-18で下しAFC北地区単独首位へ",
            "keywords": "NFL第8週, スティーラーズ, ジャイアンツ, カルビン・オースティン, ウィルソン, ワット"
        },
        "basketball": {
            "tagline": "NBA激闘：ミッチェルが残り0.3秒で劇的決勝ジャンパー、無敗キャバリアーズがバックスを114-113で破る。",
            "liveNow": "ミルウォーキー終結：キャバリアーズ 114-113 バックス。ミッチェル30点（決勝弾0.3秒）がリラードの41点に応戦。開幕7勝0敗。",
            "pulse": "NBA激闘：ドノバン・ミッチェルが残り0.3秒で決勝ブザービーター、キャブズ開幕7連勝",
            "keywords": "NBA, キャバリアーズ, バックス, ミッチェル, リラード, アデトクンボ, ブザービーター"
        },
        "soccer": {
            "tagline": "プレミアリーグ第9節：ハリー・ウィルソンが劇的AT2発！フラムがブレントフォードに2-1逆転勝利。",
            "liveNow": "クレイヴン・コテージ終結：フラム 2-1 ブレントフォード（ウィルソン 90+2', 90+7'；ヤネルト 24'）。フラムが勝ち点8に到達。",
            "pulse": "プレミアリーグ第9節：途中出場のハリー・ウィルソンがATに2得点を奪いフラムが奇跡の逆転劇",
            "keywords": "プレミアリーグ, フラム, ブレントフォード, ハリー・ウィルソン, ロンドンダービー"
        },
        "tennis": {
            "tagline": "ロレックス・パリ・マスターズ：チチパスがカルバレス・バエナに4-6, 6-3, 6-3で逆転勝利し初戦突破。",
            "liveNow": "パリ・マスターズ1回戦：チチパスが2時間7分の激闘の末4-6, 6-3, 6-3で勝利。ウィナー37本でトリノへの望みを繋ぐ。",
            "pulse": "ロレックス・パリ・マスターズ：チチパスがアコー・アリーナで逆転勝利を飾り初戦突破",
            "keywords": "ATP, パリ・マスターズ, チチパス, カルバレス・バエナ, アコー・アリーナ"
        },
        "f1": {
            "tagline": "F1サンパウロGPプレビュー：アントネッリ戴冠の興奮冷めやらぬ中、名門インテルラゴスで熱きコンストラクターズ決戦。",
            "liveNow": "次戦：サンパウロGP（11月6〜8日）。スプリント開催のインテルラゴスを前にメルセデス（607点）がフェラーリ（474点）を133点リード。",
            "pulse": "F1インテルラゴスプレビュー：メルセデスとフェラーリがブラジルの地でチーム王座を懸け激突",
            "keywords": "F1, サンパウロGP, インテルラゴス, アントネッリ, フェラーリ, メルセデス"
        },
        "golf": {
            "tagline": "PGAツアー WWT選手権プレビュー：ペレダの歴史的快挙に沸くメキシコ、カボでシード権争奪戦が開幕。",
            "liveNow": "次戦エル・カルドナル・アット・ディアマンテ（11月5〜8日）。ペレダが世界50位入り；スモザーマンがリベンジを誓う。",
            "pulse": "PGAツアー カボプレビュー：タイガー・ウッズ設計コースでフォールシリーズ上位125位争いが激化",
            "keywords": "PGAツアー, WWT選手権, ロスカボス, エル・カルドナル, ディアマンテ, ペレダ"
        },
        "home": {
            "tonight": "月曜デスク",
            "tonightBlurb": "スティーラーズがMNFでジャイアンツを破り地区首位。ミッチェル0.3秒決勝弾でキャブズ7連勝。ウィルソンAT2発でフラム勝利。",
            "plTitle": "NFL第8週MNF：スティーラーズがオースティンの活躍でジャイアンツを26-18で撃破",
            "plBlurb": "カルビン・オースティンが73ydパントリターンTDと29ydレシーブTDを決め、T.J.ワット率いる守備陣がAFC北地区首位を堅持。",
            "f1Title": "NBA激闘：ドノバン・ミッチェルが残り0.3秒で決勝シュートを沈めキャブズが勝利",
            "f1Blurb": "ミッチェルが30得点と圧巻の勝負強さを発揮し、リラードの41得点を退けてクリーブランドの無傷7連勝を守る。"
        },
        "pg": {
            "pinFinal": "NFL第8週MNF：スティーラーズ 26-18 ジャイアンツ。オースティン2TD、ウィルソン278yd、ワット2サック。",
            "week1Closed": "NFL第8週MNF：スティーラーズが26-18でジャイアンツを倒し6勝2敗でAFC北地区首位。",
            "week1Sub": "オースティンが2つの劇的TD。スティーラーズ（6勝2敗）が地区首位に立つ。",
            "countdownTnf": "第8週終了：スティーラーズがMNFで26-18勝利。無敗バイキングスは7勝0敗をキープ。",
            "barsPoints": "メルセデスが607点でコンストラクターズ首位、フェラーリ（474点）に133点差をつけブラジルへ。",
            "tableAfterMonday": "プレミアリーグ第9節順位表：首位シティ24点、アーセナル22点、リヴァプールとチェルシー16点、フラム8点。",
            "pinClub": "クラブを選択。シティ24点、アーセナル22点、リヴァプールとチェルシー16点、フラム8点。",
            "plFootnote": "プレミア第9節：フラム 2-1 ブレントフォード、チェルシー 2-1 ニューカッスル、アーセナル 2-2 リヴァプール。",
            "majorsDone": "PGAツアー：ペレダがメキシコで母国初優勝の快挙；次戦はカボでのWWT選手権へ。"
        }
    },
    "ko": {
        "football": {
            "tagline": "NFL 8주차 MNF: 스틸러스, 캘빈 오스틴의 2TD와 철벽 수비 앞세워 자이언츠 26-18 격파하고 AFC 북부 선두.",
            "liveNow": "피츠버그 최종: 스틸러스 26-18 자이언츠. 오스틴 2TD (73yd 펀트 리턴, 29yd 리시빙); 윌슨 278yds; 와트 2색. 6승 2패.",
            "pulse": "NFL 8주차 MNF: 피츠버그 스틸러스, 자이언츠 26-18로 꺾고 AFC 북부 단독 1위 질주",
            "keywords": "NFL 8주차, 피츠버그 스틸러스, 뉴욕 자이언츠, 캘빈 오스틴, 러셀 윌슨, T.J. 와트"
        },
        "basketball": {
            "tagline": "NBA 명승부: 도노반 미첼 0.3초 남기고 위닝샷 작렬, 무패 캐벌리어스 벅스 114-113 제압.",
            "liveNow": "밀워키 최종: 캐벌리어스 114-113 벅스. 미첼 30점 (0.3초 위닝샷)으로 릴라드의 41점(3점 10방) 제압. 클리블랜드 개막 7연승.",
            "pulse": "NBA 명승부: 도노반 미첼의 종료 0.3초 전 버저비터로 캐벌리어스 개막 7연승 무패 질주",
            "keywords": "NBA, 캐벌리어스, 벅스, 도노반 미첼, 데미안 릴라드, 쿤보, 버저비터"
        },
        "soccer": {
            "tagline": "프리미어리그 9R: 해리 윌슨 추가시간 멀티골 기적, 풀럼 브렌트퍼드 2-1 대역전승.",
            "liveNow": "크레이븐 코티지 최종: 풀럼 2-1 브렌트퍼드 (윌슨 90+2', 90+7'; 야넬트 24'). 풀럼 서런던 더비 역전승으로 승점 8점.",
            "pulse": "프리미어리그 9R: 교체 투입된 해리 윌슨 추가시간 멀티골 폭발로 풀럼 기적의 역전승",
            "keywords": "프리미어리그, 풀럼, 브렌트퍼드, 해리 윌슨, 크레이븐 코티지, 런던 더비"
        },
        "tennis": {
            "tagline": "롤렉스 파리 마스터스: 치치파스, 카르바예스 바에나에 4-6, 6-3, 6-3 역전승 거두고 베르시 2회전 진출.",
            "liveNow": "파리 마스터스 1회전: 치치파스 2시간 7분 접전 끝에 역전승. 위너 37개 꽂으며 파이널스 진출 경쟁 지속.",
            "pulse": "롤렉스 파리 마스터스: 스테파노스 치치파스 3세트 접전 끝에 역전승으로 32강 안착",
            "keywords": "ATP, 롤렉스 파리 마스터스, 치치파스, 카르바예스 바에나, 아코르 아레나"
        },
        "f1": {
            "tagline": "F1 상파울루 GP 프리뷰: 안토넬리 대관식 뒤이어 인테를라고스서 메르세데스 대 페라리 컨스트럭터 혈전.",
            "liveNow": "다음 일정: 상파울루 그랑프리 (11월 6-8일). 스프린트 앞두고 메르세데스(607점)가 페라리(474점)에 133점 앞서.",
            "pulse": "F1 인테를라고스 프리뷰: 메르세데스와 페라리가 브라질 스프린트서 팀 타이틀 격돌",
            "keywords": "포뮬러 1, 상파울루 GP, 인테를라고스, 안토넬리, 페라리, 메르세데스"
        },
        "golf": {
            "tagline": "PGA 투어 WWT 챔피언십 프리뷰: 페레다의 역사적 우승 열기 속 카보서 펼쳐지는 시드권 쟁탈전.",
            "liveNow": "다음 대회: 엘 카르도날 앳 디아만테 (11월 5-8일). 페레다 세계 50위권 진입; 스모더먼과 라이의 설욕전.",
            "pulse": "PGA 투어 카보 프리뷰: 타이거 우즈 설계 코스서 펼쳐지는 가을 시리즈 톱125 사수 혈전",
            "keywords": "PGA 투어, WWT 챔피언십, 로스카보스, 엘 카르도날, 디아만테, 페레다"
        },
        "home": {
            "tonight": "월요일 데스크",
            "tonightBlurb": "스틸러스 자이언츠 꺾고 AFC 북부 선두. 미첼 0.3초 위닝샷 캐벌리어스 7연승. 윌슨 추가시간 멀티골 풀럼 승리.",
            "plTitle": "NFL 8주차 MNF: 스틸러스, 캘빈 오스틴의 맹활약 앞세워 자이언츠 26-18 격파",
            "plBlurb": "오스틴이 73야드 펀트 리턴 및 29야드 패스를 터치다운으로 연결하고 T.J. 와트가 자이언츠를 묶어 지구 선두 수성.",
            "f1Title": "NBA 명승부: 도노반 미첼 종료 0.3초 전 버저비터로 벅스 제압 (114-113)",
            "f1Blurb": "미첼이 30점과 결승 점퍼를 꽂아 릴라드의 41점을 무너뜨리고 클리블랜드의 7연승 무패 행진을 견인했습니다."
        },
        "pg": {
            "pinFinal": "NFL 8주차 MNF: 스틸러스 26, 자이언츠 18. 오스틴 2 TD, 윌슨 278 yds, 와트 2 sacks.",
            "week1Closed": "NFL 8주차 MNF: 스틸러스, 자이언츠 26-18로 잡고 6승 2패로 AFC 북부 선두 질주.",
            "week1Sub": "오스틴 2개 터치다운 작렬. 스틸러스(6-2) 지구 단독 1위 등극.",
            "countdownTnf": "8주차 최종: 스틸러스 MNF서 26-18 승리. 무패 바이킹스는 7승 0패 유지.",
            "barsPoints": "메르세데스가 607점으로 컨스트럭터 선두, 페라리(474점)에 133점 앞서며 브라질로 향합니다.",
            "tableAfterMonday": "프리미어리그 9R 순위: 맨시티 24점 선두, 아스널 22점, 리버풀과 첼시 16점, 풀럼 8점.",
            "pinClub": "클럽 선택. 맨시티 24점, 아스널 22점, 리버풀과 첼시 16점, 풀럼 승점 8점 도약.",
            "plFootnote": "EPL 9R: 풀럼 2-1 브렌트퍼드, 첼시 2-1 뉴캐슬, 아스널 2-2 리버풀, 맨시티 1-0 사우샘프턴.",
            "majorsDone": "PGA 투어: 라울 페레다 멕시코 오픈서 역사적 우승; 투어는 카보 WWT 챔피언십으로 이동."
        }
    },
    "ar": {
        "football": {
            "tagline": "دوري NFL الأسبوع 8: ستيلرز يتفوق على جاينتس 26-18 بفضل ثنائية كالفين أوستن ودفاع حديدي.",
            "liveNow": "النتيجة النهائية في بيتسبرغ: ستيلرز 26، جاينتس 18. أوستن يسجل هبوطين؛ ويلسون 278 ياردة؛ وات يسقط الخصم مرتين. بيتسبرغ بسجل 6-2.",
            "pulse": "دوري NFL الأسبوع 8: بيتسبرغ ستيلرز يهزم جاينتس 26-18 وينفرد بصدارة مجموعته بسجل 6-2",
            "keywords": "دوري كرة القدم الأمريكية, ستيلرز, جاينتس, كالفين أوستن, راسل ويلسون, تي جيه وات"
        },
        "basketball": {
            "tagline": "دوري السلة الأمريكي: دونوفان ميتشل يسجل سلة الفوز القاتلة قبل 0.3 ثانية وكافالييرز يهزم باكس 114-113.",
            "liveNow": "النتيجة النهائية في ميلووكي: كافالييرز 114، باكس 113. ميتشل 30 نقطة (سلة الحسم قبل 0.3ث) يبطل 41 نقطة لليلارد. كليفلاند بـ 7 انتصارات دون هزيمة.",
            "pulse": "دوري السلة الأمريكي: ميتشل يسجل في الثانية الأخيرة ليقود كافالييرز لفوز مثير ويواصل السجل المثالي (7-0)",
            "keywords": "دوري السلة الأمريكي, كافالييرز, باكس, دونوفان ميتشل, داميان ليلارد, يانيس"
        },
        "soccer": {
            "tagline": "الدوري الإنجليزي الجولة 9: هاري ويلسون يقلب الطاولة بثنائية قاتلة في الوقت الضائع وفولهام يهزم برينتفورد 2-1.",
            "liveNow": "نهاية دربي لندن: فولهام 2-1 برينتفورد (ويلسون 90+2'، 90+7'؛ يانيلت 24'). فولهام يرفع رصيده إلى 8 نقاط بعد ريمونتادا مذهلة.",
            "pulse": "الدوري الإنجليزي الممتاز: ثنائية إعجازية من هاري ويلسون تمنح فولهام الفوز في الوقت بدل الضائع",
            "keywords": "الدوري الإنجليزي, فولهام, برينتفورد, هاري ويلسون, كرافن كوتيج, دربي لندن"
        },
        "tennis": {
            "tagline": "بطولة باريس للماسترز: ستيفانوس تسيتسيباس يقلب تأخره ويهزم كارباييس باينا 4-6 و6-3 و6-3 في الدور الأول.",
            "liveNow": "باريس للماسترز الدور الأول: تسيتسيباس يفوز 4-6 و6-3 و6-3 في ساعتين و7 دقائق. 37 ضربة قاضية لليوناني.",
            "pulse": "بطولة باريس للماسترز: تسيتسيباس يعوض خسارة المجموعة الأولى ويتأهل للدور الثاني في قاعة بيرسي",
            "keywords": "تنس, بطولة باريس للماسترز, تسيتسيباس, كارباييس باينا, أكور أرينا"
        },
        "f1": {
            "tagline": "تقديم جائزة ساو باولو: بعد تتويج أنتونيللي، الفورمولا 1 تنتقل إلى إنترلاغوس لحسم بطولة الصانعين.",
            "liveNow": "السباق القادم: جائزة ساو باولو الكبرى (6-8 نوفمبر). مرسيدس (607 نقاط) تتقدم بفارق 133 نقطة أمام فيراري (474 نقطة).",
            "pulse": "فورمولا 1 تقديم إنترلاغوس: مواجهة نارية بين مرسيدس وفيراري في سباق السرعة بالبرازيل",
            "keywords": "فورمولا 1, جائزة ساو باولو, إنترلاغوس, أنتونيللي, فيراري, مرسيدس"
        },
        "golf": {
            "tagline": "تقديم بطولة دابليو دابليو تي: بعد إنجاز بيريدا التاريخي، الجولة تنتقل إلى كابو لحسم بطاقات الموسم.",
            "liveNow": "المحطة القادمة في ملعب إل كاردونال (5-8 نوفمبر). بيريدا في أفضل 50 عالميا؛ وسموذر مان يسعى للتعويض.",
            "pulse": "جولة الجولف الأمريكية: صراع شرس للبقاء ضمن أفضل 125 لاعبا على ملعب تايغر وودز",
            "keywords": "جولة الجولف الأمريكية, بطولة دابليو دابليو تي, لوس كابوس, إل كاردونال, ديامانتي, بيريدا"
        },
        "home": {
            "tonight": "موجز الإثنين",
            "tonightBlurb": "ستيلرز يهزم جاينتس وينفرد بصدارة مجموعته. ميتشل يسجل سلة الحسم بالثانية الأخيرة (7-0). ويلسون يصنع المعجزة لفولهام.",
            "plTitle": "دوري NFL الأسبوع 8: ستيلرز يتفوق على جاينتس 26-18 بتألق كالفين أوستن",
            "plBlurb": "أوستن يسجل هبوطين تاريخيين وتي جيه وات يقود دفاع بيتسبرغ لحسم صدارة المجموعة برصيد 6 انتصارات وهزيمتين.",
            "f1Title": "دوري السلة الأمريكي: دونوفان ميتشل يخطف سلة الفوز قبل 0.3 ثانية (114-113)",
            "f1Blurb": "ميتشل يسجل 30 نقطة وسلة الفوز القاتلة في اللحظة الأخيرة ليرد على 41 نقطة من ليلارد ويحافظ على سجل كليفلاند المثالي 7-0."
        },
        "pg": {
            "pinFinal": "دوري NFL الأسبوع 8: ستيلرز 26، جاينتس 18. أوستن هبوطين، ويلسون 278 ياردة، وات إسقاطين.",
            "week1Closed": "دوري NFL الأسبوع 8: ستيلرز يهزم جاينتس 26-18 ويتقدم بسجل 6-2 في صدارة مجموعته.",
            "week1Sub": "أوستن يسجل هبوطين حاسمين. ستيلرز (6-2) ينفرد بالصدارة.",
            "countdownTnf": "حصاد الأسبوع 8: ستيلرز يفوز 26-18 يوم الإثنين. فايكنغز المثالي يستمر بسجل 7-0.",
            "barsPoints": "مرسيدس تتصدر بطولة الصانعين بـ 607 نقاط، متقدمة بـ 133 نقطة على فيراري (474) نحو إنترلاغوس.",
            "tableAfterMonday": "ترتيب الدوري الإنجليزي الجولة 9: سيتي 24 نقطة، أرسنال 22، ليفربول وتشيلسي 16، فولهام 8.",
            "pinClub": "اختر ناديا. سيتي يتصدر بـ 24، أرسنال 22، ليفربول وتشيلسي 16، فولهام يبلغ 8 نقاط.",
            "plFootnote": "الدوري الإنجليزي: فولهام 2-1 برينتفورد، تشيلسي 2-1 نيوكاسل، أرسنال 2-2 ليفربول، مان سيتي 1-0 ساوثهامبتون.",
            "majorsDone": "جولة بي جي إيه: فوز تاريخي لراؤول بيريدا في المكسيك؛ والجولة تتجه إلى كابو لبطولة WWT."
        }
    }
}

# 1. Update frontend/src/i18n/playground.ts
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

# Helper to update messages
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

# 2. Update frontend/src/i18n/messages.ts (en and fr)
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

# 3. Update all messages-*.ts
for lang in ["es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
    lang_file = os.path.join(os.path.dirname(__file__), f"../../frontend/src/i18n/messages-{lang}.ts")
    with open(lang_file, "r", encoding="utf-8") as f:
        l_content = f.read()
    l_content = update_messages_dict(l_content, lang)
    with open(lang_file, "w", encoding="utf-8") as f:
        f.write(l_content)
    print(f"Updated {lang_file}")

print("All locale updates for 2 Nov 2026 completed successfully!")

