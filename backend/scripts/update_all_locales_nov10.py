#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update playground.ts, messages.ts, and all messages-*.ts files for 10 November 2026."""
import re
import os

DATA = {
    "en": {
        "football": {
            "tagline": "NFL Week 9 MNF: James Cook rushes for 107 yards as Bills stifle Vikings 23-6 in Minneapolis.",
            "liveNow": "Final at U.S. Bank Stadium: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds, 1 TD. Buffalo hands Minnesota (7-1) its first defeat.",
            "pulse": "NFL WEEK 9 MNF: BUFFALO BILLS STIFLE VIKINGS 23-6 TO HAND MINNESOTA FIRST DEFEAT",
            "keywords": "NFL Week 9, Buffalo Bills, Minnesota Vikings, James Cook, Josh Allen, Sam Darnold, MNF"
        },
        "basketball": {
            "tagline": "NBA: Stephen Curry scores 25 points and passes DeRozan for 16th all-time as Warriors demolish Pelicans 138-87.",
            "liveNow": "Final at Chase Center: Warriors 138, Pelicans 87. Curry 25 pts (passes DeRozan); Podziemski 25 pts; Lendeborg 23 pts. Golden State wins 8th straight.",
            "pulse": "NBA: STEPHEN CURRY HITS ALL-TIME MILESTONE AS WARRIORS DEMOLISH PELICANS 138-87",
            "keywords": "NBA, Warriors, Pelicans, Stephen Curry, Brandin Podziemski, milestone"
        },
        "soccer": {
            "tagline": "Premier League MW10: Martin Odegaard winner against Hull sends Arsenal six points clear atop the table.",
            "liveNow": "Final at Emirates: Arsenal 1-0 Hull City (Odegaard 72'). Arsenal move to 27 points from 10 matches after City fall 3-1 at Forest.",
            "pulse": "PREMIER LEAGUE MW10: MARTIN ODEGAARD 72ND-MINUTE STRIKE FIRES ARSENAL SIX POINTS CLEAR",
            "keywords": "Premier League, Arsenal, Hull City, Martin Odegaard, Emirates Stadium, MW10"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters Final: Carlos Alcaraz battles past Ben Shelton 7-6(5), 7-5 to capture maiden Bercy crown.",
            "liveNow": "Paris Masters Final: Alcaraz def. Shelton 7-6(5), 7-5. Alcaraz saves key break points and captures his 9th ATP Masters 1000 title.",
            "pulse": "ROLEX PARIS MASTERS FINAL: CARLOS ALCARAZ DOWNS BEN SHELTON IN STRAIGHT SETS FOR 9TH MASTERS CROWN",
            "keywords": "ATP, Rolex Paris Masters, Carlos Alcaraz, Ben Shelton, Accor Arena, Final"
        },
        "f1": {
            "tagline": "Sao Paulo GP: Lando Norris wins chaotic Interlagos race as Mercedes officially clinches 2026 Constructors title.",
            "liveNow": "Interlagos Race Final: Norris P1 (McLaren), Verstappen P2 (from 21st), Hadjar P3. Russell P4 and Antonelli P5 seal title for Mercedes.",
            "pulse": "F1 SAO PAULO GP: LANDO NORRIS WINS DRAMATIC WET RACE AS MERCEDES CLINCHES CONSTRUCTORS TITLE",
            "keywords": "Formula 1, Sao Paulo GP, Interlagos, Lando Norris, Max Verstappen, Mercedes"
        },
        "golf": {
            "tagline": "WWT Championship: 19-year-old Blades Brown edges Ben James in playoff for historic maiden PGA Tour victory.",
            "liveNow": "Final Round at Diamante: Blades Brown (-24) def. Ben James (-24) on 2nd playoff hole to become youngest PGA Tour winner in 95 years.",
            "pulse": "PGA TOUR CABO: BLADES BROWN EDGES BEN JAMES IN PLAYOFF TO WIN HISTORIC WWT CHAMPIONSHIP",
            "keywords": "PGA Tour, WWT Championship, Blades Brown, Ben James, El Cardonal, Diamante, Los Cabos"
        },
        "home": {
            "tonight": "Tuesday desk",
            "tonightBlurb": "Alcaraz downs Shelton for first Paris Masters title. Norris wins chaotic Interlagos race as Mercedes clinches title. Bills stifle Vikings on MNF. Brown wins Cabo playoff at 19. Curry milestone in Warriors rout. Arsenal six clear.",
            "plTitle": "Premier League MW10: Martin Odegaard winner against Hull fires Arsenal six points clear",
            "plBlurb": "Gunners grind out 1-0 win at Emirates Stadium as Man City fall 3-1 at Forest and Chelsea lose at Sunderland.",
            "f1Title": "Sao Paulo GP: Lando Norris wins wet Interlagos race as Mercedes clinches Constructors title",
            "f1Blurb": "Norris wins by 14.6s from pole; Verstappen charges from 21st to 2nd; Mercedes seals crown on 652 points."
        },
        "pg": {
            "pinFinal": "NFL Week 9 MNF: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds, 1 TD. Buffalo hands Minnesota first loss.",
            "week1Closed": "NFL Week 9 MNF: Bills beat Vikings 23-6 as James Cook rushes for 107 yards and a touchdown.",
            "week1Sub": "James Cook 107 yards and a score; Allen 235 yards. Bills hand Vikings (7-1) their first defeat.",
            "countdownTnf": "Week 9 MNF Final: Bills 23, Vikings 6. Buffalo improves to 7-2 in dominant road win.",
            "barsPoints": "Mercedes clinches 2026 Constructors title with 652 pts; Norris wins Interlagos thriller from Verstappen.",
            "tableAfterMonday": "Premier League Matchweek 10: Arsenal lead with 27 pts, Man City 21, Brighton 19, Liverpool 18, Chelsea 16.",
            "pinClub": "Select a club. Arsenal lead on 27, Man City 21, Brighton 19, Liverpool 18, Chelsea and Everton 16.",
            "plFootnote": "PL MW10: Arsenal 1-0 Hull, Forest 3-1 Man City, Palace 1-3 Liverpool, Sunderland 1-0 Chelsea, Leeds 1-0 Spurs.",
            "majorsDone": "PGA Tour: 19-year-old Blades Brown edges Ben James in playoff to win historic WWT Championship in Cabo."
        }
    },
    "fr": {
        "football": {
            "tagline": "NFL Semaine 9 MNF : James Cook court pour 107 yards et les Bills etouffent les Vikings 23-6 a Minneapolis.",
            "liveNow": "Fin de match au U.S. Bank Stadium : Bills 23, Vikings 6. Cook 107 yds, 1 TD ; Allen 235 yds, 1 TD. Buffalo inflige a Minnesota (7-1) son premier revers.",
            "pulse": "NFL SEMAINE 9 MNF : BUFFALO ETOUFFE LES VIKINGS 23-6 ET LEUR INFLIGE LEUR PREMIERE DEFAITE",
            "keywords": "NFL Semaine 9, Buffalo Bills, Minnesota Vikings, James Cook, Josh Allen, Sam Darnold"
        },
        "basketball": {
            "tagline": "NBA : Stephen Curry marque 25 points et depasse DeRozan au 16e rang historique dans le carton des Warriors 138-87.",
            "liveNow": "Fin de match au Chase Center : Warriors 138, Pelicans 87. Curry 25 pts ; Podziemski 25 pts ; Lendeborg 23 pts. Golden State signe son 8e succes de suite.",
            "pulse": "NBA : CURRY DEPASSE DEROZAN AU 16E RANG HISTORIQUE, LES WARRIORS ECRASENT LES PELICANS 138-87",
            "keywords": "NBA, Warriors, Pelicans, Stephen Curry, Brandin Podziemski, record"
        },
        "soccer": {
            "tagline": "Premier League J10 : Le but de Martin Odegaard contre Hull donne six points d'avance a Arsenal en tete.",
            "liveNow": "Fin de match a l'Emirates : Arsenal 1-0 Hull City (Odegaard 72'). Arsenal passe a 27 points en 10 matches apres la defaite de City 3-1 a Forest.",
            "pulse": "PREMIER LEAGUE J10 : MARTIN ODEGAARD PERMET A ARSENAL DE PRENDRE SIX POINTS D'AVANCE",
            "keywords": "Premier League, Arsenal, Hull City, Martin Odegaard, Emirates Stadium"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters Finale : Carlos Alcaraz bat Ben Shelton 7-6(5), 7-5 pour son premier trophee a Bercy.",
            "liveNow": "Paris Masters Finale : Alcaraz bat Shelton 7-6(5), 7-5. Alcaraz s'adjuge son 9e titre en ATP Masters 1000.",
            "pulse": "ROLEX PARIS MASTERS FINALE : CARLOS ALCARAZ S'OFFRE BEN SHELTON EN DEUX SETS POUR UN 9E MASTERS",
            "keywords": "ATP, Rolex Paris Masters, Carlos Alcaraz, Ben Shelton, Accor Arena"
        },
        "f1": {
            "tagline": "GP de Sao Paulo : Lando Norris gagne sous la pluie a Interlagos, Mercedes scelle le titre constructeurs 2026.",
            "liveNow": "Course a Interlagos : Norris 1er (McLaren), Verstappen 2e (parti 21e), Hadjar 3e. Russell 4e et Antonelli 5e sacrent Mercedes.",
            "pulse": "F1 GP DE SAO PAULO : LANDO NORRIS S'IMPOSE SOUS LA PLUIE, MERCEDES CHAMPION DES CONSTRUCTEURS",
            "keywords": "Formule 1, GP de Sao Paulo, Interlagos, Lando Norris, Max Verstappen, Mercedes"
        },
        "golf": {
            "tagline": "WWT Championship : Blades Brown, 19 ans, bat Ben James en playoff et signe un sacre historique.",
            "liveNow": "Dernier tour a Diamante : Blades Brown (-24) bat Ben James (-24) au 2e trou de barrage, plus jeune vainqueur depuis 95 ans.",
            "pulse": "PGA TOUR CABO : BLADES BROWN BAT BEN JAMES EN BARRAGE ET S'IMPOSE AU WWT CHAMPIONSHIP",
            "keywords": "PGA Tour, WWT Championship, Blades Brown, Ben James, El Cardonal, Diamante"
        },
        "home": {
            "tonight": "Bureau du mardi",
            "tonightBlurb": "Alcaraz bat Shelton pour son premier Paris Masters. Norris s'impose a Interlagos, Mercedes sacre. Les Bills etouffent les Vikings. Brown triomphe en playoff a 19 ans. Curry historique. Arsenal a +6.",
            "plTitle": "Premier League J10 : Martin Odegaard donne la victoire a Arsenal face a Hull",
            "plBlurb": "Les Gunners gagnent 1-0 a l'Emirates tandis que City chute 3-1 a Forest et Chelsea perd a Sunderland.",
            "f1Title": "GP de Sao Paulo : Lando Norris gagne sous la pluie, Mercedes valide le titre",
            "f1Blurb": "Norris s'impose avec 14,6s d'avance ; Verstappen remonte de 21e a 2e ; Mercedes sacre a 652 points."
        },
        "pg": {
            "pinFinal": "NFL Semaine 9 MNF : Bills 23, Vikings 6. Cook 107 yds, 1 TD ; Allen 235 yds. Buffalo inflige a Minnesota sa 1ere defaite.",
            "week1Closed": "NFL Semaine 9 MNF : Les Bills battent les Vikings 23-6 avec 107 yards au sol de James Cook.",
            "week1Sub": "James Cook 107 yards et 1 TD ; Allen 235 yards. Les Bills font tomber les Vikings (7-1).",
            "countdownTnf": "Bilan Semaine 9 MNF : Bills 23, Vikings 6. Buffalo monte a 7-2 apres un grand match a l'exterieur.",
            "barsPoints": "Mercedes valide le titre des constructeurs 2026 avec 652 pts ; Norris gagne a Interlagos devant Verstappen.",
            "tableAfterMonday": "Premier League J10 : Arsenal en tete avec 27 pts, City 21, Brighton 19, Liverpool 18, Chelsea 16.",
            "pinClub": "Choisissez un club. Arsenal en tete a 27, City 21, Brighton 19, Liverpool 18, Chelsea et Everton 16.",
            "plFootnote": "PL J10 : Arsenal 1-0 Hull, Forest 3-1 City, Palace 1-3 Liverpool, Sunderland 1-0 Chelsea, Leeds 1-0 Spurs.",
            "majorsDone": "PGA Tour : Blades Brown (19 ans) bat Ben James en playoff et remporte le WWT Championship a Cabo."
        }
    },
    "es": {
        "football": {
            "tagline": "NFL Semana 9 MNF: James Cook corre para 107 yardas y los Bills frenan 23-6 a los Vikings en Minneapolis.",
            "liveNow": "Final en U.S. Bank Stadium: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds, 1 TD. Buffalo propina a Minnesota (7-1) su primera derrota.",
            "pulse": "NFL SEMANA 9 MNF: BUFFALO FRENA A LOS VIKINGS 23-6 Y LES QUITA EL INVICTO",
            "keywords": "NFL Semana 9, Buffalo Bills, Minnesota Vikings, James Cook, Josh Allen, Sam Darnold"
        },
        "basketball": {
            "tagline": "NBA: Stephen Curry anota 25 puntos y supera a DeRozan en la lista historica en el 138-87 de Warriors ante Pelicans.",
            "liveNow": "Final en Chase Center: Warriors 138, Pelicans 87. Curry 25 pts; Podziemski 25; Lendeborg 23. Golden State logra su 8ª victoria consecutiva.",
            "pulse": "NBA: CURRY SUPERA A DEROZAN EN EL 16º PUESTO HISTORICO, WARRIORS AROLLAN A PELICANS 138-87",
            "keywords": "NBA, Warriors, Pelicans, Stephen Curry, Brandin Podziemski"
        },
        "soccer": {
            "tagline": "Premier League J10: El golazo de Martin Odegaard ante Hull dispara al Arsenal a seis puntos de ventaja.",
            "liveNow": "Final en el Emirates: Arsenal 1-0 Hull City (Odegaard 72'). Arsenal suma 27 puntos en 10 jornadas tras la caida del City 3-1 en Forest.",
            "pulse": "PREMIER LEAGUE J10: MARTIN ODEGAARD LIDERA EL TRIUNFO DE ARSENAL PARA DISPARAR LA VENTAJA A 6 PUNTOS",
            "keywords": "Premier League, Arsenal, Hull City, Martin Odegaard, Emirates Stadium"
        },
        "tennis": {
            "tagline": "Final Rolex Paris Masters: Carlos Alcaraz supera a Ben Shelton 7-6(5), 7-5 y conquista su primera corona en Bercy.",
            "liveNow": "Final Paris Masters: Alcaraz vence a Shelton 7-6(5), 7-5. Alcaraz asegura su 9º trofeo de categoria ATP Masters 1000.",
            "pulse": "FINAL ROLEX PARIS MASTERS: CARLOS ALCARAZ VENCE A BEN SHELTON EN DOS SETS POR SU 9º MASTERS",
            "keywords": "ATP, Rolex Paris Masters, Carlos Alcaraz, Ben Shelton, Accor Arena"
        },
        "f1": {
            "tagline": "GP de Sao Paulo: Lando Norris reina bajo el agua en Interlagos y Mercedes corona el Mundial de Constructores.",
            "liveNow": "Carrera en Interlagos: Norris 1º (McLaren), Verstappen 2º (salio 21º), Hadjar 3º. Russell 4º y Antonelli 5º coronan a Mercedes.",
            "pulse": "F1 GP DE SAO PAULO: LANDO NORRIS GANA EN LLUVIA, MERCEDES PROCLAMADO CAMPEON DE CONSTRUCTORES",
            "keywords": "Formula 1, GP de Sao Paulo, Interlagos, Lando Norris, Max Verstappen, Mercedes"
        },
        "golf": {
            "tagline": "WWT Championship: Blades Brown, de 19 anos, vence a Ben James en el playoff en un triunfo historico.",
            "liveNow": "Ronda final en Diamante: Blades Brown (-24) bate a Ben James (-24) en el 2º hoyo de desempate, ganador mas joven en 95 anos.",
            "pulse": "PGA TOUR CABO: BLADES BROWN VENCE A BEN JAMES EN EL DESEMPATE DEL WWT CHAMPIONSHIP",
            "keywords": "PGA Tour, WWT Championship, Blades Brown, Ben James, El Cardonal, Diamante"
        },
        "home": {
            "tonight": "Mesa del martes",
            "tonightBlurb": "Alcaraz vence a Shelton por su primer Paris Masters. Norris gana en Interlagos, Mercedes campeon. Los Bills frenan a Vikings. Brown gana con 19 anos en playoff. Curry historico. Arsenal a +6.",
            "plTitle": "Premier League J10: Martin Odegaard da la victoria al Arsenal ante el Hull",
            "plBlurb": "Los Gunners vencen 1-0 en el Emirates mientras el City cae 3-1 ante Forest y el Chelsea tropieza en Sunderland.",
            "f1Title": "GP de Sao Paulo: Lando Norris gana bajo el agua, Mercedes asegura el titulo",
            "f1Blurb": "Norris gana con 14.6s de renta; Verstappen remonta de 21º a 2º; Mercedes corona el titulo con 652 puntos."
        },
        "pg": {
            "pinFinal": "NFL Semana 9 MNF: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds. Buffalo quita el invicto a Minnesota.",
            "week1Closed": "NFL Semana 9 MNF: Los Bills superan 23-6 a los Vikings con 107 yardas terrestres de James Cook.",
            "week1Sub": "James Cook 107 yardas y 1 TD; Allen 235 yardas. Los Bills derriban a los Vikings (7-1).",
            "countdownTnf": "Resumen Semana 9 MNF: Bills 23, Vikings 6. Buffalo se coloca 7-2 tras gran victoria a domicilio.",
            "barsPoints": "Mercedes asegura el titulo de constructores con 652 pts; Norris gana en Interlagos ante Verstappen.",
            "tableAfterMonday": "Premier League J10: Arsenal lider con 27 pts, City 21, Brighton 19, Liverpool 18, Chelsea 16.",
            "pinClub": "Elija un club. Arsenal lider con 27, City 21, Brighton 19, Liverpool 18, Chelsea y Everton 16.",
            "plFootnote": "PL J10: Arsenal 1-0 Hull, Forest 3-1 City, Palace 1-3 Liverpool, Sunderland 1-0 Chelsea, Leeds 1-0 Spurs.",
            "majorsDone": "PGA Tour: Blades Brown (19 anos) bate a Ben James en el desempate y se lleva el WWT Championship en Cabo."
        }
    },
    "de": {
        "football": {
            "tagline": "NFL Woche 9 MNF: James Cook erlaeuft 107 Yards beim 23:6-Erfolg der Bills gegen die Vikings in Minneapolis.",
            "liveNow": "Endstand im U.S. Bank Stadium: Bills 23, Vikings 6. Cook 107 Yds, 1 TD; Allen 235 Yds. Buffalo fuegt Minnesota (7-1) erste Niederlage zu.",
            "pulse": "NFL WOCHE 9 MNF: BUFFALO BREMST DIE VIKINGS MIT 23:6 AUS UND BEENDET DEREN SIEGESSERIE",
            "keywords": "NFL Woche 9, Buffalo Bills, Minnesota Vikings, James Cook, Josh Allen, Sam Darnold"
        },
        "basketball": {
            "tagline": "NBA: Stephen Curry erzielt 25 Punkte, ueberholt DeRozan auf Rang 16 und Warriors siegen 138:87 gegen Pelicans.",
            "liveNow": "Endstand im Chase Center: Warriors 138, Pelicans 87. Curry 25 Pkt; Podziemski 25 Pkt; Lendeborg 23 Pkt. Achter Sieg in Serie fuer Golden State.",
            "pulse": "NBA: CURRY STEIGT AUF PLATZ 16 DER EWIGEN BESTENLISTE, WARRIORS FEGEN PELICANS MIT 138:87 WEG",
            "keywords": "NBA, Warriors, Pelicans, Stephen Curry, Brandin Podziemski"
        },
        "soccer": {
            "tagline": "Premier League 10. Spieltag: Martin Odegaard schiesst Arsenal gegen Hull zu sechs Punkten Vorsprung.",
            "liveNow": "Endstand im Emirates: Arsenal 1-0 Hull City (Odegaard 72'). Arsenal zieht auf 27 Punkte davon, da City 1:3 bei Forest patzt.",
            "pulse": "PREMIER LEAGUE 10. SPIELTAG: MARTIN ODEGAARD BRINGT ARSENAL SECHS PUNKTE IN FUEHRUNG",
            "keywords": "Premier League, Arsenal, Hull City, Martin Odegaard, Emirates Stadium"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters Finale: Carlos Alcaraz bezwingt Ben Shelton 7:6(5), 7:5 fuer ersten Bercy-Titel.",
            "liveNow": "Paris Masters Finale: Alcaraz besiegt Shelton 7:6(5), 7:5. Alcaraz sichert sich seinen 9. ATP-Masters-1000-Titel.",
            "pulse": "ROLEX PARIS MASTERS FINALE: CARLOS ALCARAZ SCHLAEGT BEN SHELTON IN ZWEI SAETZEN ZUR 9. MASTERS-KROENE",
            "keywords": "ATP, Rolex Paris Masters, Carlos Alcaraz, Ben Shelton, Accor Arena"
        },
        "f1": {
            "tagline": "Sao Paulo GP: Lando Norris triumphiert im Regen von Interlagos, Mercedes sichert Konstrukteurstitel 2026.",
            "liveNow": "Rennen in Interlagos: Norris P1 (McLaren), Verstappen P2 (von P21), Hadjar P3. Russell P4 und Antonelli P5 machen Mercedes zum Weltmeister.",
            "pulse": "F1 SAO PAULO GP: LANDO NORRIS SIEGT IM REGEN, MERCEDES GEWINNT KONSTRUKTEURS-WELTMEISTERSCHAFT",
            "keywords": "Formel 1, Sao Paulo GP, Interlagos, Lando Norris, Max Verstappen, Mercedes"
        },
        "golf": {
            "tagline": "WWT Championship: 19-jaehriger Blades Brown schlaegt Ben James im Playoff zu historischem Premierensieg.",
            "liveNow": "Finalrunde in Diamante: Blades Brown (-24) schlaegt Ben James (-24) am 2. Extraloch, juengster Sieger seit 95 Jahren.",
            "pulse": "PGA TOUR CABO: BLADES BROWN BEZWINGT BEN JAMES IM STECHEN DER WWT CHAMPIONSHIP",
            "keywords": "PGA Tour, WWT Championship, Blades Brown, Ben James, El Cardonal, Diamante"
        },
        "home": {
            "tonight": "Dienstags-Desk",
            "tonightBlurb": "Alcaraz schlaegt Shelton fuer ersten Paris-Titel. Norris siegt in Interlagos, Mercedes ist Meister. Bills stoppen Vikings. Brown gewinnt Playoff mit 19 Jahren. Curry-Meilenstein. Arsenal +6.",
            "plTitle": "Premier League 10. Spieltag: Martin Odegaard fuehrt Arsenal zum Heimsieg",
            "plBlurb": "Gunners siegen 1:0 im Emirates, waehrend City 1:3 bei Forest verliert und Chelsea in Sunderland patzt.",
            "f1Title": "Sao Paulo GP: Lando Norris siegt im Regen, Mercedes kroent sich zum Champion",
            "f1Blurb": "Norris siegt mit 14,6s Vorsprung; Verstappen faehrt von 21 auf 2; Mercedes Weltmeister mit 652 Punkten."
        },
        "pg": {
            "pinFinal": "NFL Woche 9 MNF: Bills 23, Vikings 6. Cook 107 Yds, 1 TD; Allen 235 Yds. Buffalo beendet Minnesotas Serie.",
            "week1Closed": "NFL Woche 9 MNF: Die Bills schlagen die Vikings 23:6 mit 107 Rushing Yards von James Cook.",
            "week1Sub": "James Cook 107 Yards und 1 TD; Allen 235 Yards. Bills besiegen Vikings (7-1).",
            "countdownTnf": "Woche 9 MNF Endstand: Bills 23, Vikings 6. Buffalo steht nach Auswaertssieg bei 7-2.",
            "barsPoints": "Mercedes sichert Konstrukteurs-WM mit 652 Punkten; Norris gewinnt Interlagos-Krimi vor Verstappen.",
            "tableAfterMonday": "Premier League 10. Spieltag: Arsenal fuehrt mit 27 Punkten vor Man City (21), Brighton (19), Liverpool (18).",
            "pinClub": "Waehlen Sie einen Club. Arsenal fuehrt mit 27, City 21, Brighton 19, Liverpool 18, Chelsea und Everton 16.",
            "plFootnote": "PL 10. Spieltag: Arsenal 1-0 Hull, Forest 3-1 City, Palace 1-3 Liverpool, Sunderland 1-0 Chelsea, Leeds 1-0 Spurs.",
            "majorsDone": "PGA Tour: Blades Brown (19 Jahre) bezwingt Ben James im Playoff und siegt bei der WWT Championship in Cabo."
        }
    },
    "it": {
        "football": {
            "tagline": "NFL Week 9 MNF: James Cook corre per 107 yard e i Bills soffocano i Vikings 23-6 a Minneapolis.",
            "liveNow": "Finale allo U.S. Bank Stadium: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds. Buffalo infligge a Minnesota (7-1) il primo ko.",
            "pulse": "NFL WEEK 9 MNF: BUFFALO BATTE I VIKINGS 23-6 E TOGLIE L'IMBATTIBILITA A MINNESOTA",
            "keywords": "NFL Week 9, Buffalo Bills, Minnesota Vikings, James Cook, Josh Allen, Sam Darnold"
        },
        "basketball": {
            "tagline": "NBA: Stephen Curry segna 25 punti e scavalca DeRozan al 16° posto storico nel 138-87 dei Warriors sui Pelicans.",
            "liveNow": "Finale al Chase Center: Warriors 138, Pelicans 87. Curry 25 pt; Podziemski 25 pt; Lendeborg 23 pt. 8° successo di fila per Golden State.",
            "pulse": "NBA: CURRY SALE AL 16° POSTO MARCATORI DI SEMPRE, I WARRIORS DEMOLISCONO I PELICANS 138-87",
            "keywords": "NBA, Warriors, Pelicans, Stephen Curry, Brandin Podziemski"
        },
        "soccer": {
            "tagline": "Premier League 10ª giornata: La perla di Martin Odegaard regala all'Arsenal sei punti di vantaggio in vetta.",
            "liveNow": "Finale all'Emirates: Arsenal 1-0 Hull City (Odegaard 72'). Arsenal a 27 punti in 10 giornate dopo il ko del City per 3-1 a Forest.",
            "pulse": "PREMIER LEAGUE 10ª GIORNATA: MARTIN ODEGAARD LANCIA L'ARSENAL A SEI PUNTI DI DISTACCO",
            "keywords": "Premier League, Arsenal, Hull City, Martin Odegaard, Emirates Stadium"
        },
        "tennis": {
            "tagline": "Rolex Paris Masters Finale: Carlos Alcaraz supera Ben Shelton 7-6(5), 7-5 e conquista la prima corona a Bercy.",
            "liveNow": "Finale Paris Masters: Alcaraz batte Shelton 7-6(5), 7-5. Lo spagnolo alza il suo 9° titolo Masters 1000 in carriera.",
            "pulse": "ROLEX PARIS MASTERS FINALE: CARLOS ALCARAZ PIEGA BEN SHELTON IN DUE SET E CONQUISTA IL 9° MASTERS",
            "keywords": "ATP, Rolex Paris Masters, Carlos Alcaraz, Ben Shelton, Accor Arena"
        },
        "f1": {
            "tagline": "GP San Paolo: Lando Norris vince sul bagnato a Interlagos, la Mercedes vince il titolo Costruttori 2026.",
            "liveNow": "Gara a Interlagos: Norris 1° (McLaren), Verstappen 2° (partito 21°), Hadjar 3°. Russell 4° e Antonelli 5° regalano il titolo a Mercedes.",
            "pulse": "F1 GP SAN PAOLO: LANDO NORRIS VINCE SUL BAGNATO, MERCEDES CAMPIONE DEL MONDO COSTRUTTORI",
            "keywords": "Formula 1, GP San Paolo, Interlagos, Lando Norris, Max Verstappen, Mercedes"
        },
        "golf": {
            "tagline": "WWT Championship: Il 19enne Blades Brown supera Ben James al playoff in uno storico trionfo.",
            "liveNow": "Giro finale a Diamante: Blades Brown (-24) batte Ben James (-24) alla 2ª buca di spareggio, vincitore piu giovane in 95 anni.",
            "pulse": "PGA TOUR CABO: BLADES BROWN SUPERA BEN JAMES ALLO SPAREGGIO DEL WWT CHAMPIONSHIP",
            "keywords": "PGA Tour, WWT Championship, Blades Brown, Ben James, El Cardonal, Diamante"
        },
        "home": {
            "tonight": "Desk del martedi",
            "tonightBlurb": "Alcaraz batte Shelton per il primo Paris Masters. Norris vince a Interlagos, Mercedes iridata. I Bills fermano i Vikings. Brown vince lo spareggio a 19 anni. Curry record. Arsenal a +6.",
            "plTitle": "Premier League 10ª giornata: Martin Odegaard firma l'1-0 dell'Arsenal sull'Hull",
            "plBlurb": "I Gunners vincono 1-0 all'Emirates mentre il City crolla 3-1 a Nottingham e il Chelsea scivola a Sunderland.",
            "f1Title": "GP San Paolo: Lando Norris vince sul bagnato, Mercedes campione costruttori",
            "f1Blurb": "Norris vince con 14,6s di margine; Verstappen sale da 21° a 2°; Mercedes vince il titolo con 652 punti."
        },
        "pg": {
            "pinFinal": "NFL Week 9 MNF: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds. Buffalo infligge il 1° ko a Minnesota.",
            "week1Closed": "NFL Week 9 MNF: I Bills superano i Vikings 23-6 con 107 yard su corsa di James Cook.",
            "week1Sub": "James Cook 107 yard e 1 TD; Allen 235 yard. I Bills battono i Vikings (7-1).",
            "countdownTnf": "Week 9 MNF Finale: Bills 23, Vikings 6. Buffalo sale a 7-2 dopo il successo esterno.",
            "barsPoints": "Mercedes vince il titolo Costruttori con 652 pt; Norris vince a Interlagos davanti a Verstappen.",
            "tableAfterMonday": "Premier League 10ª giornata: Arsenal in vetta con 27 pt, City 21, Brighton 19, Liverpool 18, Chelsea 16.",
            "pinClub": "Scegli un club. Arsenal in vetta a 27, City 21, Brighton 19, Liverpool 18, Chelsea ed Everton 16.",
            "plFootnote": "PL 10ª giornata: Arsenal 1-0 Hull, Forest 3-1 City, Palace 1-3 Liverpool, Sunderland 1-0 Chelsea, Leeds 1-0 Spurs.",
            "majorsDone": "PGA Tour: Blades Brown (19 anni) batte Ben James allo spareggio e vince il WWT Championship a Cabo."
        }
    },
    "pl": {
        "football": {
            "tagline": "NFL tydzien 9 MNF: James Cook zdobywa 107 jardow biegiem, a Bills dławia Vikings 23-6 w Minneapolis.",
            "liveNow": "Koniec na U.S. Bank Stadium: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds. Buffalo zadaje Minnesocie (7-1) pierwsza porazke.",
            "pulse": "NFL TYDZIEN 9 MNF: BUFFALO POKONUJE VIKINGS 23-6 I ODBIERA IM MIANO NIEPOKONANYCH",
            "keywords": "NFL tydzien 9, Buffalo Bills, Minnesota Vikings, James Cook, Josh Allen, Sam Darnold"
        },
        "basketball": {
            "tagline": "NBA: Stephen Curry rzuca 25 punktow i wyprzedza DeRozana na 16. miejscu wszech czasow w pogromie Pelicans 138-87.",
            "liveNow": "Koniec w Chase Center: Warriors 138, Pelicans 87. Curry 25 pkt; Podziemski 25 pkt; Lendeborg 23 pkt. 8. wygrana z rzedu Golden State.",
            "pulse": "NBA: CURRY AWANSUJE NA 16. MIEJSCE W HISTORII, WARRIORS ROZBIJAJA PELICANS 138-87",
            "keywords": "NBA, Warriors, Pelicans, Stephen Curry, Brandin Podziemski"
        },
        "soccer": {
            "tagline": "Premier League 10. kolejka: Zwycieski gol Martina Odegaarda daje Arsenalowi szesc punktow przewagi.",
            "liveNow": "Koniec na Emirates: Arsenal 1-0 Hull City (Odegaard 72'). Arsenal ma 27 punktow po 10 meczach po porazce City 1-3 w Forest.",
            "pulse": "PREMIER LEAGUE 10. KOLEJKA: MARTIN ODEGAARD DAJE ARSENALOWI SZESC PUNKTOW PRZEWAGI",
            "keywords": "Premier League, Arsenal, Hull City, Martin Odegaard, Emirates Stadium"
        },
        "tennis": {
            "tagline": "Final Rolex Paris Masters: Carlos Alcaraz pokonuje Bena Sheltona 7-6(5), 7-5 i zdobywa puchar w Bercy.",
            "liveNow": "Final Paris Masters: Alcaraz wygrywa z Sheltonem 7-6(5), 7-5. Alcaraz siega po swoj 9. puchar rangi Masters 1000.",
            "pulse": "FINAL ROLEX PARIS MASTERS: CARLOS ALCARAZ POKONUJE BENA SHELTONA W DWOCH SETACH PO 9. TYTUL MASTERS",
            "keywords": "ATP, Rolex Paris Masters, Carlos Alcaraz, Ben Shelton, Accor Arena"
        },
        "f1": {
            "tagline": "GP Sao Paulo: Lando Norris wygrywa w deszczu na Interlagos, Mercedes mistrzem konstruktorow 2026.",
            "liveNow": "Wyscig na Interlagos: Norris 1. (McLaren), Verstappen 2. (startowal z 21.), Hadjar 3. Russell 4. i Antonelli 5. daja tytul Mercedesowi.",
            "pulse": "F1 GP SAO PAULO: LANDO NORRIS WYGRYWA W DESZCZU, MERCEDES MISTRZEM SWIATA KONSTRUKTOROW",
            "keywords": "Formula 1, GP Sao Paulo, Interlagos, Lando Norris, Max Verstappen, Mercedes"
        },
        "golf": {
            "tagline": "WWT Championship: 19-letni Blades Brown pokonuje Bena Jamesa w dogrywce i przechodzi do historii.",
            "liveNow": "Runda finalowa w Diamante: Blades Brown (-24) pokonuje Bena Jamesa (-24) na 2. dolku dogrywki, najmlodszy mistrz od 95 lat.",
            "pulse": "PGA TOUR CABO: BLADES BROWN POKONUJE BENA JAMESA W DOGRYWCE WWT CHAMPIONSHIP",
            "keywords": "PGA Tour, WWT Championship, Blades Brown, Ben James, El Cardonal, Diamante"
        },
        "home": {
            "tonight": "Biurko wtorkowe",
            "tonightBlurb": "Alcaraz pokonuje Sheltona i wygrywa w Paryzu. Norris triumfuje na Interlagos, Mercedes mistrzem. Bills zatrzymuja Vikings. 19-letni Brown wygrywa w dogrywce. Rekord Curry'ego. Arsenal +6.",
            "plTitle": "Premier League 10. kolejka: Martin Odegaard daje wygrana Arsenalowi",
            "plBlurb": "Kanonierzy wygrywaja 1-0 na Emirates, a City ulega 1-3 w Forest i Chelsea przegrywa w Sunderlandzie.",
            "f1Title": "GP Sao Paulo: Lando Norris wygrywa w deszczu, Mercedes przypieczetowal tytul",
            "f1Blurb": "Norris wygrywa z przewaga 14,6 s; Verstappen awansuje z 21. na 2.; Mercedes mistrzem z 652 punktami."
        },
        "pg": {
            "pinFinal": "NFL Tydzien 9 MNF: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds. Buffalo odbiera Vikings miano niepokonanych.",
            "week1Closed": "NFL Tydzien 9 MNF: Bills pokonuja Vikings 23-6 dzieki 107 jardom biegowym Jamesa Cooka.",
            "week1Sub": "James Cook 107 jardow i 1 TD; Allen 235 jardow. Bills wygrywaja z Vikings (7-1).",
            "countdownTnf": "Tydzien 9 MNF Wynik: Bills 23, Vikings 6. Buffalo poprawia bilans do 7-2 po wyjazdowej wygranej.",
            "barsPoints": "Mercedes przypieczetowal mistrzostwo konstruktorow z 652 pkt; Norris wygrywa na Interlagos przed Verstappenem.",
            "tableAfterMonday": "Premier League 10. kolejka: Arsenal liderem z 27 pkt przed City (21), Brighton (19), Liverpoolem (18).",
            "pinClub": "Wybierz klub. Arsenal prowadzi z 27, City 21, Brighton 19, Liverpool 18, Chelsea i Everton 16.",
            "plFootnote": "PL 10. kolejka: Arsenal 1-0 Hull, Forest 3-1 City, Palace 1-3 Liverpool, Sunderland 1-0 Chelsea, Leeds 1-0 Spurs.",
            "majorsDone": "PGA Tour: Blades Brown (19 lat) pokonuje Bena Jamesa w dogrywce i wygrywa WWT Championship w Cabo."
        }
    },
    "zh": {
        "football": {
            "tagline": "NFL第9周周一夜赛：库克冲球107码比尔防守组发威，客场23-6力克维京人破其不败金身。",
            "liveNow": "明尼阿波利斯完场：比尔23，维京人6。库克107码1达阵；阿伦235码1达阵。布法罗送维京人（7胜1负）赛季首败。",
            "pulse": "NFL第9周周一夜赛：布法罗比尔23-6力克明尼苏达维京人送对手赛季首败",
            "keywords": "NFL第9周, 布法罗比尔, 明尼苏达维京人, 詹姆斯·库克, 乔希·阿伦, 萨姆·达诺德"
        },
        "basketball": {
            "tagline": "NBA常规赛：库里总得分超越德罗赞升至历史第16位，勇士138-87狂胜鹈鹕豪取八连胜。",
            "liveNow": "大通中心完场：勇士138，鹈鹕87。库里25分（升至历史第16）；波杰姆斯基25分；伦德博格23分。勇士8连胜。",
            "pulse": "NBA：库里总得分里程碑升至历史第16位，金州勇士138-87血洗新奥尔良鹈鹕",
            "keywords": "NBA, 勇士, 鹈鹕, 斯蒂芬·库里, 布兰丁·波杰姆斯基"
        },
        "soccer": {
            "tagline": "英超第10轮：厄德高兜射破门阿森纳1-0赫尔城，在积分榜上豪取6分领先优势。",
            "liveNow": "酋长球场完场：阿森纳1-0赫尔城（厄德高72分）。曼城1-3客负森林后，阿森纳10战积27分扩大领先优势。",
            "pulse": "英超第10轮：厄德高第72分钟绝杀，阿森纳1-0赫尔城建立6分领跑优势",
            "keywords": "英超, 阿森纳, 赫尔城, 厄德高, 酋长球场"
        },
        "tennis": {
            "tagline": "巴黎大师赛决赛：阿尔卡拉斯7-6(5)、7-5力克谢尔顿，首度加冕贝西兼斩获大师赛第9冠。",
            "liveNow": "巴黎大师赛决赛：阿尔卡拉斯7-6(5)、7-5战胜谢尔顿。阿尔卡拉斯斩获个人第9座大师赛奖杯锁定年终第一。",
            "pulse": "巴黎大师赛决赛：阿尔卡拉斯直落两盘击败谢尔顿，首夺贝西冠军加冕大师赛第9冠",
            "keywords": "ATP, 劳力士巴黎大师赛, 阿尔卡拉斯, 谢尔顿, 贝尔西体育馆"
        },
        "f1": {
            "tagline": "F1圣保罗大奖赛：诺里斯雨战杆位夺冠，梅赛德斯车队提前锁定2026年度车队总冠军。",
            "liveNow": "英特拉格斯正赛完场：诺里斯第1（迈凯伦），维斯塔潘第2（第21位发车），哈贾尔第3。拉塞尔第4安东内利第5锁定梅奔车队冠军。",
            "pulse": "F1圣保罗站：诺里斯雨地大胜，维斯塔潘连超19车获亚军，梅赛德斯加冕车队冠军",
            "keywords": "F1, 圣保罗大奖赛, 英特拉格斯, 诺里斯, 维斯塔潘, 梅赛德斯"
        },
        "golf": {
            "tagline": "全球科技锦标赛：19岁小将布雷兹·布朗加洞赛绝杀本·詹姆斯，创95年来最年轻美巡冠军纪录。",
            "liveNow": "卡多纳尔决赛轮：布雷兹·布朗（-24）在第二加洞击败本·詹姆斯（-24），成为95年以来最年轻美巡赛冠军。",
            "pulse": "美巡赛卡波站：19岁布雷兹·布朗加洞击败本·詹姆斯夺得全球科技锦标赛冠军",
            "keywords": "美巡赛, 全球科技锦标赛, 布雷兹·布朗, 本·詹姆斯, 洛斯卡波斯"
        },
        "home": {
            "tonight": "周二聚焦",
            "tonightBlurb": "阿尔卡拉斯击败谢尔顿首夺巴黎大师赛。诺里斯雨战登顶，梅奔锁定车队冠军。比尔周一夜赛破维京人金身。19岁布朗加洞创美巡纪录。库里里程碑。阿森纳6分领跑。",
            "plTitle": "英超第10轮：厄德高建功助阿森纳小胜赫尔城",
            "plBlurb": "枪手酋长球场1-0苦战告捷，曼城1-3爆冷不敌森林，切尔西在桑德兰告负。",
            "f1Title": "圣保罗大奖赛：诺里斯雨战折桂，梅赛德斯加冕车队总冠军",
            "f1Blurb": "诺里斯14.6秒大胜；维斯塔潘第21位追至亚军；梅赛德斯积652分锁定冠军。"
        },
        "pg": {
            "pinFinal": "NFL第9周周一夜赛：比尔23-6维京人。库克107码1达阵，阿伦235码。布法罗终结明尼苏达不败金身。",
            "week1Closed": "NFL第9周MNF：比尔23-6力克维京人，詹姆斯·库克全场推进107码并斩获达阵。",
            "week1Sub": "詹姆斯·库克107码加达阵；阿伦235码。比尔送维京人（7-1）首败。",
            "countdownTnf": "第9周MNF完场：比尔23-6客场大胜维京人，战绩提升至7胜2负。",
            "barsPoints": "梅赛德斯以652分加冕车队总冠军；诺里斯力压维斯塔潘夺得英特拉格斯雨战胜利。",
            "tableAfterMonday": "英超第10轮：阿森纳27分领跑，曼城21分，布莱顿19分，利物浦18分，切尔西16分。",
            "pinClub": "选择俱乐部。阿森纳27分领跑，曼城21分，布莱顿19分，利物浦18分，切尔西与埃弗顿16分。",
            "plFootnote": "英超第10轮：阿森纳1-0赫尔城，森林3-1曼城，水晶宫1-3利物浦，桑德兰1-0切尔西，利兹1-0热刺。",
            "majorsDone": "美巡赛：19岁小将布雷兹·布朗加洞绝杀本·詹姆斯，夺得卡波站WWT锦标赛冠军。"
        }
    },
    "ja": {
        "football": {
            "tagline": "NFL第9週MNF：クックが107ヤード走、ビルズがミネアポリスでバイキングスを23-6で圧倒。",
            "liveNow": "U.S.バンク・スタジアム試合終了：ビルズ 23、バイキングス 6。クック107ヤード1TD、アレン235ヤード。ミネソタ（7勝1敗）に今季初黒星。",
            "pulse": "NFL第9週MNF：バッファロー・ビルズがバイキングスを23-6で圧倒し無敗を止める",
            "keywords": "NFL第9週, バッファロー・ビルズ, ミネソタ・バイキングス, ジェームズ・クック, ジョシュ・アレン"
        },
        "basketball": {
            "tagline": "NBA：ステフィン・カリーが歴代得点16位に浮上、ウォリアーズがペリカンズを138-87で破砕し8連勝。",
            "liveNow": "チェイス・センター試合終了：ウォリアーズ 138、ペリカンズ 87。カリー25点（デローザン超え）、ポジェムスキー25点。怒涛の8連勝。",
            "pulse": "NBA：カリーが歴代得点16位に到達、ゴールデンステイトがペリカンズを138-87で圧倒",
            "keywords": "NBA, ウォリアーズ, ペリカンズ, ステフィン・カリー, ブランディン・ポジェムスキー"
        },
        "soccer": {
            "tagline": "プレミアリーグ第10節：ウーデゴール決勝弾でアーセナルがハルに1-0勝利、首位リードを6差に拡大。",
            "liveNow": "エミレーツ試合終了：アーセナル 1-0 ハル・シティ（ウーデゴール 72分）。シティがフォレストに1-3で敗れ、アーセナル勝ち点27へ。",
            "pulse": "プレミアリーグ第10節：ウーデゴールの72分ミドル炸裂、アーセナルが勝ち点差を6に広げる",
            "keywords": "プレミアリーグ, アーセナル, ハル・シティ, マルティン・ウーデゴール"
        },
        "tennis": {
            "tagline": "ロレックス・パリ・マスターズ決勝：アルカラスがシェルトンを7-6(5)、7-5で破り大会初制覇。",
            "liveNow": "パリ・マスターズ決勝：アルカラスがシェルトンを7-6(5)、7-5で撃破。通算9度目のマスターズ1000制覇を果たす。",
            "pulse": "パリ・マスターズ決勝：アルカラスがストレートでシェルトンを下し9度目のマスターズ戴冠",
            "keywords": "ATP, ロレックス・パリ・マスターズ, カルロス・アルカラス, ベン・シェルトン"
        },
        "f1": {
            "tagline": "F1サンパウロGP：雨のインテルラゴスでノリスが優勝、メルセデスが2026年コンストラクターズ王座獲得。",
            "liveNow": "インテルラゴス決勝終了：ノリス1位（マクラーレン）、フェルスタッペン2位（21番手発進）、ハジャル3位。メルセデスがタイトル確定。",
            "pulse": "F1サンパウロGP：雨の激戦をノリスが制覇、メルセデスがコンストラクターズ王座を自力確定",
            "keywords": "F1, サンパウロGP, インテルラゴス, ランド・ノリス, マックス・フェルスタッペン"
        },
        "golf": {
            "tagline": "WWT選手権：19歳のブレイズ・ブラウンがPOでベン・ジェームズを下し95年ぶりの最年少PGAツアー優勝。",
            "liveNow": "ディアマンテ最終日終了：ブレイズ・ブラウン（-24）がプレーオフ2ホール目でベン・ジェームズを下し歴史的初優勝。",
            "pulse": "PGAツアー・カボ：19歳のブレイズ・ブラウンがPOを制しWWT選手権で米ツアー最年少優勝",
            "keywords": "PGAツアー, WWT選手権, ブレイズ・ブラウン, ベン・ジェームズ, ロスカボス"
        },
        "home": {
            "tonight": "火曜デスク",
            "tonightBlurb": "アルカラスがシェルトンを破りパリ初V。ノリスが雨のブラジル制覇、メルセデス王者。ビルズがバイキングス撃破。19歳ブラウンがPO制覇。カリー歴代16位。アーセナル6差独走。",
            "plTitle": "プレミアリーグ第10節：ウーデゴール弾でアーセナル辛勝",
            "plBlurb": "ガナーズが1-0で勝利する一方、マンチェスター・Cは1-3で敗戦、チェルシーも黒星。",
            "f1Title": "サンパウロGP：ノリスが雨中独走、メルセデスが王座確定",
            "f1Blurb": "ノリスが14.6秒差で勝利。フェルスタッペンが21番手から猛追2位。メルセデス652点で王者。"
        },
        "pg": {
            "pinFinal": "NFL第9週MNF：ビルズ 23、バイキングス 6。クック107ヤード1TD。バッファローが無敗のミネソタを粉砕。",
            "week1Closed": "NFL第9週MNF：ビルズがクックの107ヤード走でバイキングスを23-6で撃破。",
            "week1Sub": "ジェームズ・クック107ヤードと1TD、アレン235ヤード。バイキングス（7勝1敗）に初黒星。",
            "countdownTnf": "第9週MNF試合終了：ビルズ 23、バイキングス 6。バッファローが敵地で完勝し7勝2敗。",
            "barsPoints": "メルセデスが652点でチーム王座確定。ノリスがインテルラゴスの激戦を制覇。",
            "tableAfterMonday": "プレミアリーグ第10節：アーセナルが勝ち点27で首位独走、マン・C21点、ブライトン19点、リヴァプール18点。",
            "pinClub": "クラブを選択。アーセナル首位27点、マン・C21点、ブライトン19点、リヴァプール18点、チェルシーとエヴァートン16点。",
            "plFootnote": "PL第10節：アーセナル 1-0 ハル、フォレスト 3-1 マン・C、パレス 1-3 リヴァプール、サンダーランド 1-0 チェルシー、リーズ 1-0 トッテナム。",
            "majorsDone": "PGAツアー：19歳のブレイズ・ブラウンがPOでベン・ジェームズを破りWWT選手権初優勝。"
        }
    },
    "ko": {
        "football": {
            "tagline": "NFL 9주차 MNF: 제임스 쿡 107야드 질주, 빌스가 미니애폴리스에서 바이킹스를 23-6으로 제압.",
            "liveNow": "U.S. 뱅크 스타디움 종료: 빌스 23, 바이킹스 6. 쿡 107야드 1TD, 앨런 235야드. 미네소타(7승 1패) 시즌 첫 패.",
            "pulse": "NFL 9주차 MNF: 버펄로 빌스가 미네소타 바이킹스를 23-6으로 누르고 무패 행진을 저지",
            "keywords": "NFL 9주차, 버펄로 빌스, 미네소타 바이킹스, 제임스 쿡, 조시 앨런"
        },
        "basketball": {
            "tagline": "NBA: 스테픈 커리 25점 폭발로 역대 득점 16위 등극, 워리어스 펠리컨스 138-87 대파 8연승.",
            "liveNow": "체이스 센터 종료: 워리어스 138, 펠리컨스 87. 커리 25점(드로잔 추월), 포지엠스키 25점, 렌데보그 23점. 8연승 질주.",
            "pulse": "NBA: 커리 역대 득점 16위 등극, 골든스테이트 워리어스 펠리컨스에 138-87 대승",
            "keywords": "NBA, 워리어스, 펠리컨스, 스테픈 커리, 브랜딘 포지엠스키"
        },
        "soccer": {
            "tagline": "프리미어리그 10R: 외데고르 환상 결승골 아스널, 헐시티 1-0 꺾고 6점 차 선두 질주.",
            "liveNow": "에미레이츠 종료: 아스널 1-0 헐시티 (외데고르 72'). 맨시티가 포레스트에 1-3 패배하며 아스널 승점 27점 선두 질주.",
            "pulse": "프리미어리그 10R: 마르틴 외데고르 72분 결승골, 아스널 6점 차 독주 체제 구축",
            "keywords": "프리미어리그, 아스널, 헐시티, 마르틴 외데고르, 에미레이츠"
        },
        "tennis": {
            "tagline": "롤렉스 파리 마스터스 결승: 카를로스 알카라스, 벤 셸턴 7-6(5), 7-5 꺾고 베르시 첫 우승.",
            "liveNow": "파리 마스터스 결승: 알카라스가 셸턴을 7-6(5), 7-5로 꺾고 통산 9번째 마스터스 1000 우승 달성.",
            "pulse": "파리 마스터스 결승: 알카라스, 셸턴 꺾고 생애 첫 베르시 정상 및 마스터스 9승 달성",
            "keywords": "ATP, 롤렉스 파리 마스터스, 카를로스 알카라스, 벤 셸턴"
        },
        "f1": {
            "tagline": "F1 상파울루 GP: 빗속의 인터라고스에서 랜도 노리스 우승, 메르세데스 컨스트럭터 챔피언 확정.",
            "liveNow": "인터라고스 레이스 종료: 노리스 1위(맥라렌), 베르스타펜 2위(21그리드 출발), 하자르 3위. 메르세데스 우승 확정.",
            "pulse": "F1 상파울루 GP: 랜도 노리스 우중전 완벽 제패, 메르세데스 컨스트럭터 챔피언 등극",
            "keywords": "F1, 상파울루 GP, 인터라고스, 랜도 노리스, 막스 베르스타펜"
        },
        "golf": {
            "tagline": "WWT 챔피언십: 19세 블레이즈 브라운, 연장 접전 끝 벤 제임스 꺾고 95년 만의 PGA 투어 최연소 우승.",
            "liveNow": "디아만테 최종 라운드 종료: 블레이즈 브라운(-24)이 2차 연장에서 벤 제임스 제치고 역사적 첫 우승.",
            "pulse": "PGA 투어 카보: 블레이즈 브라운 연장 끝 벤 제임스 제치고 WWT 챔피언십 우승",
            "keywords": "PGA 투어, WWT 챔피언십, 블레이즈 브라운, 벤 제임스, 로스카보스"
        },
        "home": {
            "tonight": "화요일 데스크",
            "tonightBlurb": "알카라스 파리 첫 우승. 노리스 빗속 브라질 제패, 메르세데스 챔피언. 빌스 바이킹스 격파. 19세 브라운 연장 우승. 커리 득점 16위. 아스널 6점 차 선두.",
            "plTitle": "프리미어리그 10R: 외데고르 골로 아스널 승리",
            "plBlurb": "아스널 1-0 승리, 맨시티는 포레스트에 1-3 완패, 첼시도 선덜랜드에 무릎.",
            "f1Title": "상파울루 GP: 노리스 우중전 우승, 메르세데스 왕좌 복귀",
            "f1Blurb": "노리스 14.6초 차 우승; 베르스타펜 21위에서 2위 질주; 메르세데스 652점 챔피언."
        },
        "pg": {
            "pinFinal": "NFL 9주차 MNF: 빌스 23, 바이킹스 6. 쿡 107야드 1TD. 버펄로가 무패 미네소타를 격파.",
            "week1Closed": "NFL 9주차 MNF: 빌스가 쿡의 107야드 활약으로 바이킹스를 23-6으로 제압.",
            "week1Sub": "제임스 쿡 107야드와 1TD, 앨런 235야드. 바이킹스(7-1)에 시즌 첫 패배.",
            "countdownTnf": "9주차 MNF 경기 종료: 빌스 23, 바이킹스 6. 버펄로 원정 완승으로 7승 2패.",
            "barsPoints": "메르세데스 652점으로 팀 챔피언 확정; 노리스가 인터라고스 명승부 우승.",
            "tableAfterMonday": "프리미어리그 10R: 아스널 승점 27점 선두, 맨시티 21점, 브라이턴 19점, 리버풀 18점.",
            "pinClub": "클럽을 선택하세요. 아스널 선두 27점, 맨시티 21점, 브라이턴 19점, 리버풀 18점, 첼시와 에버턴 16점.",
            "plFootnote": "PL 10R: 아스널 1-0 헐시티, 포레스트 3-1 맨시티, 팰리스 1-3 리버풀, 선덜랜드 1-0 첼시, 리즈 1-0 토트넘.",
            "majorsDone": "PGA 투어: 19세 블레이즈 브라운 연장 끝 벤 제임스 꺾고 카보 WWT 챔피언십 우승."
        }
    },
    "ar": {
        "football": {
            "tagline": "الدوري الامريكي الاسبوع 9 MNF: جيمس كوك يركض لمسافة 107 ياردات وبيلز يخنق فايكنغز 23-6 في منيابوليس.",
            "liveNow": "نهاية المباراة في ملعب يو اس بنك: بيلز 23، فايكنغز 6. كوك 107 ياردات ولمسة؛ الن 235 ياردة. بافلو يلحق بمينيسوتا (7-1) اول خسارة.",
            "pulse": "الدوري الامريكي الاسبوع 9 MNF: بافلو بيلز يخنق مينيسوتا 23-6 ويلحق به اولى هزائم الموسم",
            "keywords": "الدوري الامريكي الاسبوع 9, بافلو بيلز, مينيسوتا فايكنغز, جيمس كوك, جوش الن"
        },
        "basketball": {
            "tagline": "دوري السلة: ستيفن كاري يسجل 25 نقطة ويصعد للمركز 16 تاريخيا وواريورز يسحق بيلوكانز 138-87.",
            "liveNow": "نهاية المباراة في تشيس سنتر: واريورز 138، بيلوكانز 87. كاري 25 نقطة؛ بودزيمسكي 25؛ لينديبورغ 23. الفوز الثامن تواليا لغولدن ستيت.",
            "pulse": "دوري السلة: كاري يصعد للمركز 16 في تاريخ الهدافين، غولدن ستيت يسحق نيو اورليانز 138-87",
            "keywords": "دوري السلة, واريورز, بيلوكانز, ستيفن كاري, براندين بودزيمسكي"
        },
        "soccer": {
            "tagline": "الدوري الانجليزي الجولة 10: هدف مارتن اوديغارد يقود ارسنال لتوسيع الفارق في الصدارة الى ست نقاط.",
            "liveNow": "نهاية المباراة في الامارات: ارسنال 1-0 هال سيتي (اوديغارد 72). ارسنال يرفع رصيده الى 27 نقطة بعد خسارة سيتي 1-3 في فورست.",
            "pulse": "الدوري الانجليزي الجولة 10: اوديغارد يسجل في الدقيقة 72 وارسنال يبتعد بفارق 6 نقاط",
            "keywords": "الدوري الانجليزي, ارسنال, هال سيتي, مارتن اوديغارد, ملعب الامارات"
        },
        "tennis": {
            "tagline": "نهائي باريس بيرسي: كارلوس الكاراز يتفوق على بين شيلتون 7-6(5) و7-5 ليحرز لقبه الاول في البطولة.",
            "liveNow": "نهائي باريس: الكاراز يهزم شيلتون 7-6(5) و7-5. الاسباني يحرز لقبه التاسع في بطولات الماسترز 1000.",
            "pulse": "نهائي باريس بيرسي: كارلوس الكاراز يقهر بين شيلتون بمجموعتين دون رد ويحقق تاسع القابه الكبرى",
            "keywords": "تنس, باريس ماسترز, كارلوس الكاراز, بين شيلتون, صالة اكور"
        },
        "f1": {
            "tagline": "جائزة ساو باولو الكبرى: لاندو نوريس يفوز بسباق انترلاغوس الممطر ومرسيدس تحسم بطولة الصانعين.",
            "liveNow": "سباق انترلاغوس: نوريس اول (مكلارين)، فيرستابن ثان (انطلق 21)، هاجار ثالث. راسل رابع وانتونيلي خامس يحسمان اللقب لمرسيدس.",
            "pulse": "فورمولا 1 ساو باولو: لاندو نوريس يفوز بالسباق الممطر ومرسيدس بطلة للعالم في الصانعين",
            "keywords": "فورمولا 1, جائزة ساو باولو, انترلاغوس, لاندو نوريس, ماكس فيرستابن"
        },
        "golf": {
            "tagline": "بطولة WWT: الشاب بليدز براون (19 عاما) يهزم بن جيمس في التمايز ليحقق فوزا تاريخيا.",
            "liveNow": "الجولة الاخيرة في ديامانتي: بليدز براون (-24) يهزم بن جيمس (-24) في الحفرة الاضافية الثانية، اصغر بطل منذ 95 عاما.",
            "pulse": "PGA تور كابو: بليدز براون يهزم بن جيمس في جولة التمايز ليتوج ببطولة WWT",
            "keywords": "PGA تور, بطولة WWT, بليدز براون, بن جيمس, لوس كابوس"
        },
        "home": {
            "tonight": "مكتب الثلاثاء",
            "tonightBlurb": "الكاراز يهزم شيلتون ويتوج في باريس. نوريس يفوز في انترلاغوس ومرسيدس بطلة. بيلز يسقط فايكنغز. براون (19 عاما) بطل الغولف بالتمايز. انجاز كاري. ارسنال +6.",
            "plTitle": "الدوري الانجليزي الجولة 10: اوديغارد يقود ارسنال للفوز على هال",
            "plBlurb": "الغانرز يفوزون 1-0 في الامارات بينما سقط سيتي 1-3 في فورست وخسر تشيلسي في سندرلاند.",
            "f1Title": "جائزة ساو باولو: نوريس يفوز تحت المطر، مرسيدس تحسم لقب الصانعين",
            "f1Blurb": "نوريس يفوز بفارق 14.6 ثانية؛ فيرستابن يصعد من المركز 21 للثاني؛ مرسيدس بطلة بـ652 نقطة."
        },
        "pg": {
            "pinFinal": "الدوري الامريكي الاسبوع 9 MNF: بيلز 23، فايكنغز 6. كوك 107 ياردات ولمسة. بافلو يلحق اول خسارة بمينيسوتا.",
            "week1Closed": "الدوري الامريكي الاسبوع 9 MNF: بيلز يهزم فايكنغز 23-6 مع 107 ياردات ركضا لجيمس كوك.",
            "week1Sub": "جيمس كوك 107 ياردات ولمسة؛ الن 235 ياردة. بيلز يسقط فايكنغز (7-1).",
            "countdownTnf": "الاسبوع 9 MNF النتيجة النهائية: بيلز 23، فايكنغز 6. بافلو يصعد الى 7-2 بفوز خارجي كبير.",
            "barsPoints": "مرسيدس تحسم بطولة الصانعين بـ652 نقطة؛ نوريس يفوز في انترلاغوس امام فيرستابن.",
            "tableAfterMonday": "البريميرليغ الجولة 10: ارسنال في الصدارة بـ27 نقطة، سيتي 21، برايتون 19، ليفربول 18، تشيلسي 16.",
            "pinClub": "اختر ناديا. ارسنال في الصدارة بـ27، سيتي 21، برايتون 19، ليفربول 18، تشيلسي وايفرتون 16.",
            "plFootnote": "الجولة 10: ارسنال 1-0 هال، فورست 3-1 سيتي، بالاس 1-3 ليفربول، سندرلاند 1-0 تشيلسي، ليدز 1-0 توتنهام.",
            "majorsDone": "PGA تور: بليدز براون (19 عاما) يهزم بن جيمس في التمايز ويتوج ببطولة WWT في كابو."
        }
    }
}

# Verify no em-dashes
for lang, sections in DATA.items():
    for sec_name, sec_dict in sections.items():
        for k, text in sec_dict.items():
            if "—" in text or "--" in text:
                raise ValueError(f"Found em-dash or double-hyphen in {lang}.{sec_name}.{k}: {text}")

print("Validation passed: 0 em-dashes across all locale dictionaries.")

# Update playground.ts
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

# Update messages.ts and messages-*.ts
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

print("All locale updates for 10 Nov 2026 completed successfully!")

