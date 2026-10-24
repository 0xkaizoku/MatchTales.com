# -*- coding: utf-8 -*-
import re
import os

DATA = {
    "en": {
        "football": {
            "tagline": "NFL Week 7 Sunday eve: Bears sit 5-2 after TNF win. Unbeaten Chiefs, 49ers and Vikings ready for Sunday.",
            "liveNow": "TNF Final: Bears 30, Patriots 24. Sunday slate: Chiefs at Seahawks (SNF), 49ers at Falcons, Colts at Vikings.",
            "pulse": "NFL WEEK 7: SUNDAY SLATE AHEAD",
            "keywords": "NFL Week 7, Bears, Patriots, Chiefs, 49ers, Vikings, Caleb Williams, Sunday slate"
        },
        "tennis": {
            "tagline": "Almaty Saturday: Basilashvili stuns Tsitsipas in three sets. Medvedev advances as Bublik retires.",
            "liveNow": "Almaty SF: Basilashvili d. Tsitsipas 6-4, 6-7(5), 6-3. Medvedev d. Bublik 6-3, ret. Sunday final: Medvedev v Basilashvili.",
            "pulse": "ALMATY SF: BASILASHVILI AND MEDVEDEV REACH FINAL",
            "keywords": "ATP, Almaty, Basilashvili, Tsitsipas, Medvedev, Bublik, semifinals, final"
        },
        "f1": {
            "tagline": "Austin Saturday qualifying: Leclerc paced Friday practice; Antonelli defends 102-point lead.",
            "liveNow": "COTA Saturday: FP3 and Qualifying at 16:00 local. Leclerc led FP1 and FP2; Antonelli +0.042s. Race Sunday 15:00.",
            "pulse": "AUSTIN SATURDAY: QUALIFYING AT COTA",
            "keywords": "Formula 1, United States GP, Austin, COTA, Leclerc, Antonelli, Russell, Qualifying"
        },
        "soccer": {
            "tagline": "London derby Saturday: Chelsea host Tottenham at Stamford Bridge. Friday final: Ipswich 1, Forest 1.",
            "liveNow": "MW8 Saturday 17:30 UK: Chelsea v Tottenham at Stamford Bridge. Friday: Ipswich 1, Forest 1. City lead on 21 (7-0-0).",
            "pulse": "DERBY DAY: CHELSEA HOST TOTTENHAM AT THE BRIDGE",
            "keywords": "Premier League, Chelsea, Tottenham, London derby, Stamford Bridge, Ipswich, Forest, MW8"
        },
        "basketball": {
            "tagline": "WNBA Finals Game 4 today: Dream lead series 2-1 and chase first championship in Atlanta.",
            "liveNow": "Game 4 at State Farm Arena: Dream lead 2-1 after 97-71 blowout. Reese historic 3rd Finals double-double. Valkyries fight for Game 5.",
            "pulse": "WNBA FINALS GAME 4: DREAM CHASE HISTORIC CROWN",
            "keywords": "WNBA Finals, Game 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Bermuda Round 3: Blanchet and Hirata share 36-hole lead at 13 under (129) at Port Royal.",
            "liveNow": "Butterfield Bermuda Round 3: Blanchet (62-67) and Hirata (65-64) tied at -13. Conners in chase. Port Royal, par 71.",
            "pulse": "PORT ROYAL ROUND 3: BLANCHET AND HIRATA TIED AT -13",
            "keywords": "PGA Tour, Bermuda, Port Royal, Blanchet, Hirata, Conners, Round 3, Butterfield"
        },
        "home": {
            "tonight": "Saturday desk",
            "tonightBlurb": "Chelsea host Tottenham at Stamford Bridge. Basilashvili and Medvedev reach Almaty final. Dream chase WNBA title in Game 4.",
            "plTitle": "Premier League: Chelsea host Tottenham at Stamford Bridge in London derby",
            "plBlurb": "Action shifts to London after Friday's 1-1 draw between Ipswich and Forest. City lead on 21 (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "United States GP: Saturday qualifying at COTA",
            "f1Blurb": "Leclerc topped Friday practice in Austin with Antonelli just 0.042s behind. Qualifying Saturday at 16:00 local time; Antonelli defends 102-point lead."
        },
        "pg": {
            "pinFinal": "Almaty SF: Basilashvili d. Tsitsipas 6-4, 6-7(5), 6-3. Medvedev d. Bublik 6-3, ret. Sunday final: Medvedev v Basilashvili.",
            "week1Closed": "NFL Week 7 TNF final: Bears edge Patriots 30-24 at Soldier Field",
            "week1Sub": "Williams 308 pass yds, 2 TD; Burden 130 rec yds; Santos 58-yd FG. Bears 5-2, Patriots 4-3. 49ers stand 6-0.",
            "countdownTnf": "TNF Final: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs and Vikings 5-0. Bills 5-1.",
            "barsPoints": "Bars show the gap to the leader. Antonelli has 340, 102 ahead of Russell on 238. Qualifying Saturday at COTA.",
            "tableAfterMonday": "Premier League: City lead table on 21 points (7-0-0). Arsenal 18, Brighton 16. Friday: Ipswich 1, Forest 1. Chelsea v Spurs Saturday.",
            "pinClub": "Select a club. City are 7-0-0 on 21. Arsenal 18, Brighton 16. Friday: Ipswich 1, Forest 1. Chelsea v Spurs Saturday.",
            "plFootnote": "Friday final: Ipswich 1, Forest 1. Saturday: Chelsea v Spurs, Villa v City, Brighton v Wolves. Sunday: Arsenal v Palace.",
            "majorsDone": "Butterfield Bermuda Round 3 underway. Blanchet (62-67) and Hirata (65-64) share lead at 13-under 129. Conners in chase.",
            "wnbaFirstRound": "WNBA Finals Game 4: Dream lead series 2-1 after 97-71 rout. Angel Reese historic 3rd double-double (21 pts, 12 reb). Game 4 in Atlanta.",
            "bracketFootnote": "Game 1: Valkyries 68, Dream 64. Game 2: Dream 79, Valkyries 65. Game 3: Dream 97, Valkyries 71. Dream lead series 2-1. Game 4 at State Farm Arena."
        }
    },
    "fr": {
        "football": {
            "tagline": "NFL semaine 7 veille de dimanche : les Bears a 5-2 apres leur succes au TNF. Chiefs, 49ers et Vikings prets pour dimanche.",
            "liveNow": "Final TNF : Bears 30, Patriots 24. Affiches de dimanche : Chiefs chez les Seahawks, 49ers chez les Falcons, Colts chez les Vikings.",
            "pulse": "NFL SEMAINE 7 : PLACE AU DIMANCHE",
            "keywords": "NFL semaine 7, Bears, Patriots, Chiefs, 49ers, Vikings, Caleb Williams, affiches de dimanche"
        },
        "tennis": {
            "tagline": "Almaty samedi : Basilashvili cree l'exploit contre Tsitsipas en trois sets. Medvedev passe sur abandon de Bublik.",
            "liveNow": "Almaty demies : Basilashvili bat Tsitsipas 6-4, 6-7(5), 6-3. Medvedev bat Bublik 6-3, ab. Finale dimanche : Medvedev contre Basilashvili.",
            "pulse": "ALMATY DEMIES : BASILASHVILI ET MEDVEDEV EN FINALE",
            "keywords": "ATP, Almaty, Basilashvili, Tsitsipas, Medvedev, Bublik, demi-finales, finale"
        },
        "f1": {
            "tagline": "Qualifications samedi a Austin : Leclerc en tete vendredi ; Antonelli defend 102 points d'avance.",
            "liveNow": "COTA samedi : EL3 et qualifications a 16:00 locale. Leclerc a domine les EL1 et EL2 ; Antonelli a 0.042s. Course dimanche a 15:00.",
            "pulse": "AUSTIN SAMEDI : QUALIFICATIONS AU COTA",
            "keywords": "Formule 1, GP des Etats-Unis, Austin, COTA, Leclerc, Antonelli, Russell, qualifications"
        },
        "soccer": {
            "tagline": "Derby londonien ce samedi : Chelsea recoit Tottenham a Stamford Bridge. Vendredi : Ipswich 1, Forest 1.",
            "liveNow": "8e journee samedi 17h30 UK : Chelsea - Tottenham a Stamford Bridge. Vendredi : Ipswich 1, Forest 1. City en tete a 21 (7-0-0).",
            "pulse": "JOUR DE DERBY : CHELSEA ACCUEILLE TOTTENHAM A STAMFORD BRIDGE",
            "keywords": "Premier League, Chelsea, Tottenham, derby de Londres, Stamford Bridge, Ipswich, Forest, 8e journee"
        },
        "basketball": {
            "tagline": "Finales WNBA match 4 aujourd'hui : le Dream mene 2-1 et vise son premier titre a Atlanta.",
            "liveNow": "Match 4 a la State Farm Arena : Dream mene 2-1 apres le succes 97-71. 3e double-double record de Reese. Valkyries pour forcer un match 5.",
            "pulse": "FINALES WNBA MATCH 4 : LE DREAM VISE UN SACRE HISTORIQUE",
            "keywords": "WNBA Finales, match 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Bermudes 3e tour : Blanchet et Hirata co-leaders apres 36 trous a 13 sous le par (129) a Port Royal.",
            "liveNow": "Butterfield Bermuda 3e tour : Blanchet (62-67) et Hirata (65-64) a egalite a -13. Conners en embuscade. Port Royal, par 71.",
            "pulse": "PORT ROYAL 3E TOUR : BLANCHET ET HIRATA A EGALITE A -13",
            "keywords": "PGA Tour, Bermudes, Port Royal, Blanchet, Hirata, Conners, 3e tour, Butterfield"
        },
        "home": {
            "tonight": "Bureau du samedi",
            "tonightBlurb": "Chelsea recoit Tottenham a Stamford Bridge. Basilashvili et Medvedev se qualifient pour la finale a Almaty. Le Dream vise le titre WNBA au match 4.",
            "plTitle": "Premier League : Chelsea recoit Tottenham a Stamford Bridge pour le derby de Londres",
            "plBlurb": "L'action passe a Londres apres le match nul 1-1 vendredi entre Ipswich et Forest. City est en tete avec 21 points (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "GP des Etats-Unis : qualifications samedi au COTA",
            "f1Blurb": "Leclerc a mene les essais vendredi a Austin avec Antonelli a seulement 0.042s. Qualifications samedi a 16:00 locale ; Antonelli defend 102 points d'avance."
        },
        "pg": {
            "pinFinal": "Almaty demies : Basilashvili bat Tsitsipas 6-4, 6-7(5), 6-3. Medvedev bat Bublik 6-3, ab. Finale dimanche : Medvedev contre Basilashvili.",
            "week1Closed": "NFL semaine 7 TNF termine : les Bears dominent les Patriots 30-24 a Soldier Field",
            "week1Sub": "Williams 308 yds a la passe, 2 TD ; Burden 130 yds a la reception ; Santos FG de 58 yds. Bears 5-2, Patriots 4-3. 49ers a 6-0.",
            "countdownTnf": "Final TNF : Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs et Vikings 5-0. Bills 5-1.",
            "barsPoints": "Les barres indiquent l'ecart avec le leader. Antonelli compte 340 points, 102 devant Russell a 238. Qualifications samedi au COTA.",
            "tableAfterMonday": "Premier League : City mene avec 21 points (7-0-0). Arsenal 18, Brighton 16. Vendredi : Ipswich 1, Forest 1. Chelsea - Spurs samedi.",
            "pinClub": "Selectionnez un club. City est a 7-0-0 avec 21 pts. Arsenal 18, Brighton 16. Vendredi : Ipswich 1, Forest 1. Chelsea - Spurs samedi.",
            "plFootnote": "Vendredi final : Ipswich 1, Forest 1. Samedi : Chelsea - Spurs, Villa - City, Brighton - Wolves. Dimanche : Arsenal - Palace.",
            "majorsDone": "Butterfield Bermuda 3e tour en cours. Blanchet (62-67) et Hirata (65-64) co-leaders a 13 sous le par (129). Conners en chasse.",
            "wnbaFirstRound": "Finales WNBA match 4 : le Dream mene 2-1 apres son carton 97-71. 3e double-double record d'Angel Reese (21 pts, 12 reb). Match 4 a Atlanta.",
            "bracketFootnote": "Match 1 : Valkyries 68, Dream 64. Match 2 : Dream 79, Valkyries 65. Match 3 : Dream 97, Valkyries 71. Le Dream mene 2-1. Match 4 a la State Farm Arena."
        }
    },
    "es": {
        "football": {
            "tagline": "NFL Semana 7 vispera de domingo: Bears con marca de 5-2 tras triunfo en TNF. Invictos Chiefs, 49ers y Vikings listos para el domingo.",
            "liveNow": "Final TNF: Bears 30, Patriots 24. Cartelera dominical: Chiefs en Seahawks (SNF), 49ers en Falcons, Colts en Vikings.",
            "pulse": "NFL SEMANA 7: CARTELERA DOMINICAL EN PUERTA",
            "keywords": "NFL Semana 7, Bears, Patriots, Chiefs, 49ers, Vikings, Caleb Williams, cartelera de domingo"
        },
        "tennis": {
            "tagline": "Almaty sabado: Basilashvili sorprende a Tsitsipas en tres sets. Medvedev avanza por retiro de Bublik.",
            "liveNow": "Almaty semifinales: Basilashvili a Tsitsipas 6-4, 6-7(5), 6-3. Medvedev a Bublik 6-3, ret. Final domingo: Medvedev vs Basilashvili.",
            "pulse": "ALMATY SEMIFINALES: BASILASHVILI Y MEDVEDEV A LA FINAL",
            "keywords": "ATP, Almaty, Basilashvili, Tsitsipas, Medvedev, Bublik, semifinales, final"
        },
        "f1": {
            "tagline": "Clasificacion de sabado en Austin: Leclerc marco el ritmo el viernes; Antonelli defiende 102 puntos de ventaja.",
            "liveNow": "COTA sabado: Libres 3 y clasificacion a las 16:00 local. Leclerc lidero Libres 1 y 2; Antonelli a 0.042s. Carrera domingo 15:00.",
            "pulse": "AUSTIN SABADO: CLASIFICACION EN COTA",
            "keywords": "Formula 1, GP de Estados Unidos, Austin, COTA, Leclerc, Antonelli, Russell, clasificacion"
        },
        "soccer": {
            "tagline": "Derbi londinense este sabado: Chelsea recibe a Tottenham en Stamford Bridge. Viernes: Ipswich 1, Forest 1.",
            "liveNow": "Jornada 8 sabado 17:30 UK: Chelsea vs Tottenham en Stamford Bridge. Viernes: Ipswich 1, Forest 1. City lidera con 21 (7-0-0).",
            "pulse": "DIA DE DERBI: CHELSEA RECIBE A TOTTENHAM EN EL BRIDGE",
            "keywords": "Premier League, Chelsea, Tottenham, derbi de Londres, Stamford Bridge, Ipswich, Forest, Jornada 8"
        },
        "basketball": {
            "tagline": "Finales WNBA Juego 4 hoy: Dream lidera 2-1 la serie y busca su primer campeonato en Atlanta.",
            "liveNow": "Juego 4 en State Farm Arena: Dream lidera 2-1 tras triunfo 97-71. Historico 3er doble-doble de Reese. Valkyries luchan por forzar el Juego 5.",
            "pulse": "FINALES WNBA JUEGO 4: DREAM BUSCA LA CORONA HISTORICA",
            "keywords": "WNBA Finales, Juego 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Bermudas Ronda 3: Blanchet y Hirata comparten el liderato tras 36 hoyos con 13 bajo par (129) en Port Royal.",
            "liveNow": "Butterfield Bermuda Ronda 3: Blanchet (62-67) e Hirata (65-64) empatados en -13. Conners a la caza. Port Royal, par 71.",
            "pulse": "PORT ROYAL RONDA 3: BLANCHET E HIRATA EMPATADOS EN -13",
            "keywords": "PGA Tour, Bermudas, Port Royal, Blanchet, Hirata, Conners, Ronda 3, Butterfield"
        },
        "home": {
            "tonight": "Mesa del sabado",
            "tonightBlurb": "Chelsea recibe a Tottenham en Stamford Bridge. Basilashvili y Medvedev alcanzan la final en Almaty. Dream busca coronarse en el Juego 4 de la WNBA.",
            "plTitle": "Premier League: Chelsea recibe a Tottenham en Stamford Bridge en el derbi de Londres",
            "plBlurb": "La accion se traslada a Londres tras el empate 1-1 del viernes entre Ipswich y Forest. City lidera con 21 puntos (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "GP de Estados Unidos: clasificacion de sabado en COTA",
            "f1Blurb": "Leclerc domino las practicas del viernes en Austin con Antonelli a solo 0.042s. Clasificacion el sabado a las 16:00 local; Antonelli defiende 102 puntos de ventaja."
        },
        "pg": {
            "pinFinal": "Almaty semifinales: Basilashvili a Tsitsipas 6-4, 6-7(5), 6-3. Medvedev a Bublik 6-3, ret. Final domingo: Medvedev vs Basilashvili.",
            "week1Closed": "NFL Semana 7 final TNF: Bears superan 30-24 a los Patriots en Soldier Field",
            "week1Sub": "Williams 308 yds pase, 2 TD; Burden 130 yds recepcion; Santos FG de 58 yds. Bears 5-2, Patriots 4-3. 49ers estan 6-0.",
            "countdownTnf": "Final TNF: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs y Vikings 5-0. Bills 5-1.",
            "barsPoints": "Las barras muestran la ventaja con el lider. Antonelli suma 340, 102 mas que Russell con 238. Clasificacion de sabado en COTA.",
            "tableAfterMonday": "Premier League: City lidera con 21 puntos (7-0-0). Arsenal 18, Brighton 16. Viernes: Ipswich 1, Forest 1. Chelsea vs Spurs sabado.",
            "pinClub": "Seleccione un club. City tiene 7-0-0 con 21 pts. Arsenal 18, Brighton 16. Viernes: Ipswich 1, Forest 1. Chelsea vs Spurs sabado.",
            "plFootnote": "Viernes final: Ipswich 1, Forest 1. Sabado: Chelsea vs Spurs, Villa vs City, Brighton vs Wolves. Domingo: Arsenal vs Palace.",
            "majorsDone": "Butterfield Bermuda Ronda 3 en marcha. Blanchet (62-67) e Hirata (65-64) comparten la cima con -13 (129). Conners a la caza.",
            "wnbaFirstRound": "Finales WNBA Juego 4: Dream lidera 2-1 tras aplastar 97-71. Historico 3er doble-doble de Angel Reese (21 pts, 12 reb). Juego 4 en Atlanta.",
            "bracketFootnote": "Juego 1: Valkyries 68, Dream 64. Juego 2: Dream 79, Valkyries 65. Juego 3: Dream 97, Valkyries 71. Dream lidera 2-1. Juego 4 en State Farm Arena."
        }
    },
    "de": {
        "football": {
            "tagline": "NFL Woche 7 vor dem Sonntag: Bears stehen 5-2 nach TNF-Sieg. Ungeschlagene Chiefs, 49ers und Vikings bereit.",
            "liveNow": "TNF-Endstand: Bears 30, Patriots 24. Sonntag-Spiele: Chiefs bei Seahawks (SNF), 49ers bei Falcons, Colts bei Vikings.",
            "pulse": "NFL WOCHE 7: SONNTAGSSPIELE STEHEN BEVOR",
            "keywords": "NFL Woche 7, Bears, Patriots, Chiefs, 49ers, Vikings, Caleb Williams, Sonntagsspiele"
        },
        "tennis": {
            "tagline": "Almaty am Samstag: Basilashvili ueberrascht Tsitsipas in drei Saetzen. Medvedev siegt nach Aufgabe von Bublik.",
            "liveNow": "Almaty Halbfinale: Basilashvili d. Tsitsipas 6-4, 6-7(5), 6-3. Medvedev d. Bublik 6-3, Aufg. Finale Sonntag: Medvedev gegen Basilashvili.",
            "pulse": "ALMATY HALBFINALE: BASILASHVILI UND MEDVEDEV ERREICHEN FINALE",
            "keywords": "ATP, Almaty, Basilashvili, Tsitsipas, Medvedev, Bublik, Halbfinale, Finale"
        },
        "f1": {
            "tagline": "Qualifying am Samstag in Austin: Leclerc dominierte Freitag; Antonelli verteidigt 102 Punkte Vorsprung.",
            "liveNow": "COTA Samstag: 3. Freies Training und Qualifying um 16:00 Ortszeit. Leclerc fuehrte FP1 und FP2 an; Antonelli +0.042s. Rennen Sonntag 15:00.",
            "pulse": "AUSTIN SAMSTAG: QUALIFYING AM COTA",
            "keywords": "Formel 1, GP USA, Austin, COTA, Leclerc, Antonelli, Russell, Qualifying"
        },
        "soccer": {
            "tagline": "London-Derby am Samstag: Chelsea empfaengt Tottenham an der Stamford Bridge. Freitag: Ipswich 1, Forest 1.",
            "liveNow": "8. Spieltag Samstag 17:30 UK: Chelsea gegen Tottenham an der Stamford Bridge. Freitag: Ipswich 1, Forest 1. City fuehrt mit 21 (7-0-0).",
            "pulse": "DERBY-TAG: CHELSEA EMPFAENGT TOTTENHAM AN DER BRIDGE",
            "keywords": "Premier League, Chelsea, Tottenham, London Derby, Stamford Bridge, Ipswich, Forest, 8. Spieltag"
        },
        "basketball": {
            "tagline": "WNBA-Finals Spiel 4 heute: Dream fuehren 2-1 und wollen in Atlanta ersten Titel der Franchise-Geschichte.",
            "liveNow": "Spiel 4 in der State Farm Arena: Dream fuehren 2-1 nach 97-71-Gala. Historisches 3. Final-Double-Double von Reese. Valkyries kaempfen um Spiel 5.",
            "pulse": "WNBA-FINALS SPIEL 4: DREAM GREIFEN NACH HISTORISCHER KRONE",
            "keywords": "WNBA Finals, Spiel 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Bermuda Runde 3: Blanchet und Hirata teilen 36-Loch-Fuehrung bei 13 unter Par (129) in Port Royal.",
            "liveNow": "Butterfield Bermuda 3. Runde: Blanchet (62-67) und Hirata (65-64) gleichauf bei -13. Conners in Verfolgung. Port Royal, Par 71.",
            "pulse": "PORT ROYAL 3. RUNDE: BLANCHET UND HIRATA BEI -13 GLEICHAUF",
            "keywords": "PGA Tour, Bermuda, Port Royal, Blanchet, Hirata, Conners, 3. Runde, Butterfield"
        },
        "home": {
            "tonight": "Samstags-Desk",
            "tonightBlurb": "Chelsea empfaengt Tottenham an der Stamford Bridge. Basilashvili und Medvedev erreichen Almaty-Finale. Dream greifen in Spiel 4 nach WNBA-Krone.",
            "plTitle": "Premier League: Chelsea empfaengt Tottenham an der Stamford Bridge zum London-Derby",
            "plBlurb": "Nach dem 1-1 am Freitag zwischen Ipswich und Forest blickt alles nach London. City fuehrt mit 21 Punkten (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "Großer Preis der USA: Qualifying am Samstag am COTA",
            "f1Blurb": "Leclerc fuehrte das Training am Freitag in Austin an, Antonelli nur 0.042s dahinter. Qualifying am Samstag um 16:00 Ortszeit; Antonelli verteidigt 102 Punkte Vorsprung."
        },
        "pg": {
            "pinFinal": "Almaty Halbfinale: Basilashvili d. Tsitsipas 6-4, 6-7(5), 6-3. Medvedev d. Bublik 6-3, Aufg. Finale Sonntag: Medvedev gegen Basilashvili.",
            "week1Closed": "NFL Woche 7 TNF-Endstand: Bears schlagen Patriots 30-24 im Soldier Field",
            "week1Sub": "Williams 308 Pass-Yards, 2 TD; Burden 130 Rec-Yards; Santos 58-Yard-FG. Bears 5-2, Patriots 4-3. 49ers stehen 6-0.",
            "countdownTnf": "TNF-Endstand: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs und Vikings 5-0. Bills 5-1.",
            "barsPoints": "Balken zeigen Abstand zum Führenden. Antonelli hat 340, 102 vor Russell mit 238. Qualifying am Samstag am COTA.",
            "tableAfterMonday": "Premier League: City fuehrt mit 21 Punkten (7-0-0). Arsenal 18, Brighton 16. Freitag: Ipswich 1, Forest 1. Chelsea gegen Spurs Samstag.",
            "pinClub": "Klub waehlen. City hat 7-0-0 mit 21 Pkt. Arsenal 18, Brighton 16. Freitag: Ipswich 1, Forest 1. Chelsea gegen Spurs Samstag.",
            "plFootnote": "Freitag final: Ipswich 1, Forest 1. Samstag: Chelsea - Spurs, Villa - City, Brighton - Wolves. Sonntag: Arsenal - Palace.",
            "majorsDone": "Butterfield Bermuda Runde 3 laeuft. Blanchet (62-67) und Hirata (65-64) fuehren gemeinsam bei 13 unter Par (129). Conners lauert.",
            "wnbaFirstRound": "WNBA Finals Spiel 4: Dream fuehren 2-1 nach 97-71-Erfolg. Angel Reese historisches 3. Double-Double (21 Pkt, 12 Reb). Spiel 4 in Atlanta.",
            "bracketFootnote": "Spiel 1: Valkyries 68, Dream 64. Spiel 2: Dream 79, Valkyries 65. Spiel 3: Dream 97, Valkyries 71. Dream fuehren 2-1. Spiel 4 in der State Farm Arena."
        }
    },
    "it": {
        "football": {
            "tagline": "NFL Week 7 vigilia di domenica: Bears sul 5-2 dopo la vittoria al TNF. Gli imbattuti Chiefs, 49ers e Vikings pronti per domenica.",
            "liveNow": "Finale TNF: Bears 30, Patriots 24. Gare di domenica: Chiefs a Seahawks (SNF), 49ers ad Atlanta, Colts a Minnesota.",
            "pulse": "NFL WEEK 7: ATTESA PER IL PROGRAMMA DELLA DOMENICA",
            "keywords": "NFL Week 7, Bears, Patriots, Chiefs, 49ers, Vikings, Caleb Williams, programma domenica"
        },
        "tennis": {
            "tagline": "Almaty sabato: Basilashvili batte a sorpresa Tsitsipas in tre set. Medvedev vola in finale dopo il ritiro di Bublik.",
            "liveNow": "Almaty semifinali: Basilashvili b. Tsitsipas 6-4, 6-7(5), 6-3. Medvedev b. Bublik 6-3, rit. Finale domenica: Medvedev v Basilashvili.",
            "pulse": "ALMATY SEMIFINALI: BASILASHVILI E MEDVEDEV IN FINALE",
            "keywords": "ATP, Almaty, Basilashvili, Tsitsipas, Medvedev, Bublik, semifinali, finale"
        },
        "f1": {
            "tagline": "Qualifiche di sabato ad Austin: Leclerc il piu veloce venerdi; Antonelli difende 102 punti di vantaggio.",
            "liveNow": "COTA sabato: FP3 e qualifiche alle 16:00 locali. Leclerc primo in FP1 e FP2; Antonelli a +0.042s. Gara domenica alle 15:00.",
            "pulse": "AUSTIN SABATO: QUALIFICHE AL COTA",
            "keywords": "Formula 1, GP Stati Uniti, Austin, COTA, Leclerc, Antonelli, Russell, qualifiche"
        },
        "soccer": {
            "tagline": "Derby di Londra sabato: il Chelsea ospita il Tottenham a Stamford Bridge. Venerdi: Ipswich 1, Forest 1.",
            "liveNow": "8a giornata sabato 17:30 UK: Chelsea v Tottenham a Stamford Bridge. Venerdi: Ipswich 1, Forest 1. City in vetta a 21 (7-0-0).",
            "pulse": "GIORNO DI DERBY: CHELSEA CONTRO TOTTENHAM A STAMFORD BRIDGE",
            "keywords": "Premier League, Chelsea, Tottenham, derby di Londra, Stamford Bridge, Ipswich, Forest, 8a giornata"
        },
        "basketball": {
            "tagline": "Finals WNBA Gara 4 oggi: il Dream guida 2-1 e insegue il primo titolo della storia ad Atlanta.",
            "liveNow": "Gara 4 alla State Farm Arena: Dream avanti 2-1 dopo il netto 97-71. Terza doppia doppia storica di Reese. Valkyries a caccia di Gara 5.",
            "pulse": "FINALS WNBA GARA 4: IL DREAM INSEGUE IL TITOLO STORICO",
            "keywords": "WNBA Finals, Gara 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Bermuda 3° giro: Blanchet e Hirata co-leader dopo 36 buche con 13 colpi sotto il par (129) a Port Royal.",
            "liveNow": "Butterfield Bermuda 3° giro: Blanchet (62-67) e Hirata (65-64) appaiati a -13. Conners insegue. Port Royal, par 71.",
            "pulse": "PORT ROYAL 3° GIRO: BLANCHET E HIRATA IN VETTA A -13",
            "keywords": "PGA Tour, Bermuda, Port Royal, Blanchet, Hirata, Conners, 3° giro, Butterfield"
        },
        "home": {
            "tonight": "Desk di sabato",
            "tonightBlurb": "Il Chelsea ospita il Tottenham a Stamford Bridge. Basilashvili e Medvedev approdano in finale ad Almaty. Dream a caccia del titolo WNBA in Gara 4.",
            "plTitle": "Premier League: Chelsea contro Tottenham a Stamford Bridge per il derby di Londra",
            "plBlurb": "L'attenzione si sposta a Londra dopo l'1-1 di venerdi tra Ipswich e Forest. City primo a quota 21 (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "GP degli Stati Uniti: qualifiche di sabato al COTA",
            "f1Blurb": "Leclerc il piu veloce nelle libere del venerdi ad Austin con Antonelli a soli 0.042s. Qualifiche sabato alle 16:00 locali; Antonelli difende 102 punti di vantaggio."
        },
        "pg": {
            "pinFinal": "Almaty semifinali: Basilashvili b. Tsitsipas 6-4, 6-7(5), 6-3. Medvedev b. Bublik 6-3, rit. Finale domenica: Medvedev v Basilashvili.",
            "week1Closed": "NFL Week 7 finale TNF: i Bears piegano i Patriots 30-24 al Soldier Field",
            "week1Sub": "Williams 308 yds lancio, 2 TD; Burden 130 yds ricezione; Santos FG da 58 yds. Bears 5-2, Patriots 4-3. 49ers imbattuti a 6-0.",
            "countdownTnf": "Finale TNF: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs e Vikings 5-0. Bills 5-1.",
            "barsPoints": "Le barre indicano il distacco dal leader. Antonelli ha 340 punti, 102 su Russell (238). Qualifiche di sabato al COTA.",
            "tableAfterMonday": "Premier League: City in vetta a 21 punti (7-0-0). Arsenal 18, Brighton 16. Venerdi: Ipswich 1, Forest 1. Chelsea v Spurs sabato.",
            "pinClub": "Seleziona un club. City a 7-0-0 con 21 punti. Arsenal 18, Brighton 16. Venerdi: Ipswich 1, Forest 1. Chelsea v Spurs sabato.",
            "plFootnote": "Venerdi finale: Ipswich 1, Forest 1. Sabato: Chelsea v Spurs, Villa v City, Brighton v Wolves. Domenica: Arsenal v Palace.",
            "majorsDone": "Butterfield Bermuda 3° giro in corso. Blanchet (62-67) e Hirata (65-64) guidano appaiati a -13 (129). Conners insegue.",
            "wnbaFirstRound": "Finals WNBA Gara 4: Dream avanti 2-1 dopo il travolgente 97-71. 3a doppia doppia record di Angel Reese (21 pts, 12 reb). Gara 4 ad Atlanta.",
            "bracketFootnote": "Gara 1: Valkyries 68, Dream 64. Gara 2: Dream 79, Valkyries 65. Gara 3: Dream 97, Valkyries 71. Dream avanti 2-1. Gara 4 alla State Farm Arena."
        }
    },
    "pl": {
        "football": {
            "tagline": "NFL Tydzien 7 przed niedziela: Bears maja bilans 5-2 po triumfie w TNF. Niepokonani Chiefs, 49ers i Vikings gotowi na niedziele.",
            "liveNow": "Koniec TNF: Bears 30, Patriots 24. Niedzielne mecze: Chiefs w Seahawks (SNF), 49ers w Falcons, Colts w Vikings.",
            "pulse": "NFL TYDZIEN 7: EMOCJE NIEDZIELNE TUZ-TUZ",
            "keywords": "NFL Tydzien 7, Bears, Patriots, Chiefs, 49ers, Vikings, Caleb Williams, niedzielne mecze"
        },
        "tennis": {
            "tagline": "Almaty w sobote: Basilashvili sensacyjnie ogral Tsitsipasa w trzech setach. Medvedev awansuje po kreczu Bublika.",
            "liveNow": "Almaty polfinaly: Basilashvili d. Tsitsipas 6-4, 6-7(5), 6-3. Medvedev d. Bublik 6-3, krecz. Niedzielny final: Medvedev v Basilashvili.",
            "pulse": "ALMATY POLFINALY: BASILASHVILI I MEDVEDEV W FINALE",
            "keywords": "ATP, Almaty, Basilashvili, Tsitsipas, Medvedev, Bublik, polfinaly, final"
        },
        "f1": {
            "tagline": "Sobotnie kwalifikacje w Austin: Leclerc najszybszy w piatek; Antonelli broni 102 punktow przewagi.",
            "liveNow": "COTA sobota: 3. trening i kwalifikacje o 16:00 czasu lokalnego. Leclerc wygral 1. i 2. trening; Antonelli +0.042s. Wyscig w niedziele o 15:00.",
            "pulse": "AUSTIN SOBOTA: KWALIFIKACJE NA COTA",
            "keywords": "Formula 1, GP USA, Austin, COTA, Leclerc, Antonelli, Russell, kwalifikacje"
        },
        "soccer": {
            "tagline": "Sobotnie derby Londynu: Chelsea podejmuje Tottenham na Stamford Bridge. W piatek: Ipswich 1, Forest 1.",
            "liveNow": "8. kolejka sobota 17:30 UK: Chelsea v Tottenham na Stamford Bridge. Piatek: Ipswich 1, Forest 1. City liderem z 21 (7-0-0).",
            "pulse": "DZIEN DERBOW: CHELSEA PODEJMUJE TOTTENHAM NA STAMFORD BRIDGE",
            "keywords": "Premier League, Chelsea, Tottenham, derby Londynu, Stamford Bridge, Ipswich, Forest, 8. kolejka"
        },
        "basketball": {
            "tagline": "Finaly WNBA mecz 4 dzis: Dream prowadza 2-1 i walcza o pierwszy tytul w historii w Atlancie.",
            "liveNow": "Mecz 4 w State Farm Arena: Dream prowadza 2-1 po wygranej 97-71. Rekordowe 3. double-double Reese. Valkyries walcza o mecz 5.",
            "pulse": "FINALY WNBA MECZ 4: DREAM WALCZA O HISTORYCZNE MISTRZOSTWO",
            "keywords": "WNBA Finaly, mecz 4, Dream, Valkyries, Reese, Howard, State Farm Arena, 2-1"
        },
        "golf": {
            "tagline": "Bermudy 3. runda: Blanchet i Hirata prowadza po 36 dolkach z wynikiem 13 ponizej par (129) w Port Royal.",
            "liveNow": "Butterfield Bermuda 3. runda: Blanchet (62-67) i Hirata (65-64) na wspolnym prowadzeniu z -13. Conners w poscigu. Port Royal, par 71.",
            "pulse": "PORT ROYAL 3. RUNDA: BLANCHET I HIRATA PROWADZA Z -13",
            "keywords": "PGA Tour, Bermudy, Port Royal, Blanchet, Hirata, Conners, 3. runda, Butterfield"
        },
        "home": {
            "tonight": "Pulpit sobotni",
            "tonightBlurb": "Chelsea podejmuje Tottenham na Stamford Bridge. Basilashvili i Medvedev melduja sie w finale w Almatach. Dream graja o tytul WNBA w meczu 4.",
            "plTitle": "Premier League: Chelsea podejmuje Tottenham na Stamford Bridge w derbach Londynu",
            "plBlurb": "Emocje przenosza sie do Londynu po piatkowym remisie 1-1 pomiedzy Ipswich a Forest. City liderem z 21 punktami (7-0-0), Arsenal 18, Brighton 16.",
            "f1Title": "GP Stanow Zjednoczonych: sobotnie kwalifikacje na COTA",
            "f1Blurb": "Leclerc byl najszybszy w piatkowych treningach w Austin, Antonelli tylko 0.042s za nim. Kwalifikacje w sobote o 16:00 czasu lokalnego; Antonelli broni 102 pkt przewagi."
        },
        "pg": {
            "pinFinal": "Almaty polfinaly: Basilashvili d. Tsitsipas 6-4, 6-7(5), 6-3. Medvedev d. Bublik 6-3, krecz. Niedzielny final: Medvedev v Basilashvili.",
            "week1Closed": "NFL Tydzien 7 koniec TNF: Bears pokonali Patriots 30-24 na Soldier Field",
            "week1Sub": "Williams 308 jardow gora, 2 TD; Burden 130 jardow odbioru; Santos 58-jardowy FG. Bears 5-2, Patriots 4-3. 49ers na 6-0.",
            "countdownTnf": "Koniec TNF: Bears 30, Patriots 24. Bears 5-2. 49ers 6-0. Chiefs i Vikings 5-0. Bills 5-1.",
            "barsPoints": "Paski pokazuja strate do lidera. Antonelli ma 340, 102 przed Russellem (238). Sobotnie kwalifikacje na COTA.",
            "tableAfterMonday": "Premier League: City prowadzi z 21 punktami (7-0-0). Arsenal 18, Brighton 16. Piatek: Ipswich 1, Forest 1. Chelsea v Spurs w sobote.",
            "pinClub": "Wybierz klub. City ma 7-0-0 i 21 pkt. Arsenal 18, Brighton 16. Piatek: Ipswich 1, Forest 1. Chelsea v Spurs w sobote.",
            "plFootnote": "Piatek final: Ipswich 1, Forest 1. Sobota: Chelsea v Spurs, Villa v City, Brighton v Wolves. Niedziela: Arsenal v Palace.",
            "majorsDone": "Butterfield Bermuda 3. runda w toku. Blanchet (62-67) i Hirata (65-64) na prowadzeniu z wynikiem -13 (129). Conners w poscigu.",
            "wnbaFirstRound": "Finaly WNBA mecz 4: Dream prowadza 2-1 po pogromie 97-71. 3. rekordowe double-double Angel Reese (21 pkt, 12 zb). Mecz 4 w Atlancie.",
            "bracketFootnote": "Mecz 1: Valkyries 68, Dream 64. Mecz 2: Dream 79, Valkyries 65. Mecz 3: Dream 97, Valkyries 71. Dream prowadza 2-1. Mecz 4 w State Farm Arena."
        }
    },
    "zh": {
        "football": {
            "tagline": "NFL第7周超级周日前瞻：熊队击沉爱国者收获5胜2负。不败之师酋长、49人与维京人周日悉数登场。",
            "liveNow": "TNF战报：熊队 30，爱国者 24。周日焦点：酋长客战海鹰，49人客战猎鹰，小马客战维京人。",
            "pulse": "NFL第7周：超级周日大战在即",
            "keywords": "NFL第7周, 熊队, 爱国者, 酋长, 49人, 维京人, 凯莱布·威廉姆斯, 周日焦点战"
        },
        "tennis": {
            "tagline": "阿拉木图周六：巴西拉什维利三盘力克西西帕斯爆冷进决赛。布勃利克伤退保送梅德韦杰夫。",
            "liveNow": "阿拉木图半决赛：巴西拉什维利 6-4、6-7(5)、6-3 西西帕斯；梅德韦杰夫 6-3（对手退赛）布勃利克。周日决赛：梅德韦杰夫对阵巴西拉什维利。",
            "pulse": "阿拉木图半决赛：巴西拉什维利与梅德韦杰夫会师决赛",
            "keywords": "ATP, 阿拉木图, 巴西拉什维利, 西西帕斯, 梅德韦杰夫, 布勃利克, 半决赛, 决赛"
        },
        "f1": {
            "tagline": "奥斯汀周六排位赛：勒克莱尔领跑周五练习赛；安东内利手握102分领先优势。",
            "liveNow": "美洲赛道周六：三练与排位赛当地时间16:00打响。勒克莱尔一练二练登顶；安东内利落后0.042秒。正赛周日15:00。",
            "pulse": "奥斯汀周六：美洲赛道排位赛开战",
            "keywords": "一级方程式, 美国大奖赛, 奥斯汀, COTA, 勒克莱尔, 安东内利, 拉塞尔, 排位赛"
        },
        "soccer": {
            "tagline": "周六伦敦德比战：切尔西在斯坦福桥迎战热刺。周五战报：伊普斯维奇 1-1 森林。",
            "liveNow": "第8轮周六英国时间17:30：切尔西在斯坦福桥迎战热刺。周五赛果：伊普斯维奇 1-1 森林。曼城21分（7战全胜）领跑。",
            "pulse": "德比日：切尔西坐镇斯坦福桥迎战热刺",
            "keywords": "英超, 切尔西, 热刺, 伦敦德比, 斯坦福桥, 伊普斯维奇, 森林, 第8轮"
        },
        "basketball": {
            "tagline": "WNBA总决赛第4战今日打响：梦想大比分2-1领先，在亚特兰大冲击队史首冠。",
            "liveNow": "州立农业球馆第4战：梦想97-71大胜后2-1领先。里斯创纪录连续三场总决赛两双。女武神背水一战争取拖入第5战。",
            "pulse": "WNBA总决赛第4战：梦想全力冲击历史首冠",
            "keywords": "WNBA总决赛, 第4战, 梦想, 女武神, 里斯, 霍华德, 州立农业球馆, 2-1"
        },
        "golf": {
            "tagline": "百慕大锦标赛第三轮：布兰切特与平田宪圣前36洞同以低于标准杆13杆（129杆）领跑皇家港。",
            "liveNow": "百慕大锦标赛第3轮：布兰切特（62-67）与平田宪圣（65-64）同以-13杆并列榜首。康纳斯紧追。皇家港标准杆71杆。",
            "pulse": "皇家港第3轮：布兰切特与平田宪圣并列榜首",
            "keywords": "美巡赛, 百慕大, 皇家港, 布兰切特, 平田宪圣, 康纳斯, 第3轮, 百慕大锦标赛"
        },
        "home": {
            "tonight": "周六快讯",
            "tonightBlurb": "切尔西在斯坦福桥迎战热刺。巴西拉什维利与梅德韦杰夫会师阿拉木图决赛。梦想冲击WNBA总冠军第4战。",
            "plTitle": "英超联赛：切尔西坐镇斯坦福桥球场迎战热刺上演伦敦德比",
            "plBlurb": "在周五伊普斯维奇1-1战平森林之后焦点转向伦敦。曼城积21分（7战全胜）傲视群雄，阿森纳18分，布莱顿16分。",
            "f1Title": "美国大奖赛：美洲赛道周六排位赛",
            "f1Blurb": "勒克莱尔领跑奥斯汀周五练习赛，安东内利仅落后0.042秒。排位赛于周六当地时间16:00打响；安东内利手握102分榜首优势。"
        },
        "pg": {
            "pinFinal": "阿拉木图半决赛：巴西拉什维利 6-4、6-7(5)、6-3 西西帕斯；梅德韦杰夫 6-3（对手退赛）布勃利克。周日决赛：梅德韦杰夫对阵巴西拉什维利。",
            "week1Closed": "NFL第7周TNF完赛：熊队在军人球场30-24战胜爱国者",
            "week1Sub": "威廉姆斯传球308码2达阵；伯登接球130码；桑托斯命中58码任意球。熊队5-2，爱国者4-3。49人保持6-0完好战绩。",
            "countdownTnf": "TNF完赛：熊队 30，爱国者 24。熊队5-2。49人6-0。酋长与维京人5-0。比尔5-1。",
            "barsPoints": "柱状图显示与领跑者的分差。安东内利积340分，领先拉塞尔（238分）达102分。周六排位赛美洲赛道展开。",
            "tableAfterMonday": "英超联赛：曼城积21分（7战全胜）高居榜首。阿森纳18分，布莱顿16分。周五：伊普斯维奇 1-1 森林。切尔西对热刺周六开战。",
            "pinClub": "选择俱乐部。曼城7战全胜积21分。阿森纳18分，布莱顿16分。周五：伊普斯维奇 1-1 森林。切尔西对热刺周六开战。",
            "plFootnote": "周五赛果：伊普斯维奇 1-1 森林。周六：切尔西对热刺，维拉对曼城，布莱顿对狼队。周日：阿森纳对水晶宫。",
            "majorsDone": "百慕大锦标赛第3轮进行中。布兰切特（62-67）与平田宪圣（65-64）同以-13杆（129杆）并列领跑。康纳斯紧随其后。",
            "wnbaFirstRound": "WNBA总决赛第4战：梦想97-71大胜后大比分2-1领先。安吉尔·里斯创纪录连续三场总决赛砍下两双（21分12板）。第4战亚特兰大打响。",
            "bracketFootnote": "第1战：女武神 68，梦想 64。第2战：梦想 79，女武神 65。第3战：梦想 97，女武神 71。梦想大比分2-1领先。第4战在州立农业球馆举行。"
        }
    },
    "ja": {
        "football": {
            "tagline": "NFL第7週日曜前夜：TNF勝利のベアーズが5勝2敗。無敗のチーフス、49ers、バイキングスが日曜の激突へ。",
            "liveNow": "TNF終了：ベアーズ 30、ペイトリオッツ 24。日曜カード：チーフス対シーホークス、49ers対ファルコンズ、コルツ対バイキングス。",
            "pulse": "NFL第7週：白熱の日曜ゲームへ突入",
            "keywords": "NFL第7週, ベアーズ, ペイトリオッツ, チーフス, 49ers, バイキングス, ケイレブ・ウィリアムズ, 日曜ゲーム"
        },
        "tennis": {
            "tagline": "アルマティ土曜：バシラシビリがチチパスを3セットで破る大金星。メドベージェフはブブリクの途中棄権で決勝へ。",
            "liveNow": "アルマティ準決勝：バシラシビリ 6-4, 6-7(5), 6-3 チチパス。メドベージェフ 6-3（棄権）ブブリク。日曜決勝：メドベージェフ対バシラシビリ。",
            "pulse": "アルマティ準決勝：バシラシビリとメドベージェフが決勝進出",
            "keywords": "ATP, アルマティ, バシラシビリ, チチパス, メドベージェフ, ブブリク, 準決勝, 決勝"
        },
        "f1": {
            "tagline": "オースティン土曜予選：ルクレールが金曜トップタイム。アントネッリは102点リードを守る。",
            "liveNow": "COTA土曜：FP3と予選（現地16:00開始）。ルクレールがFP1とFP2で首位、アントネッリ差0.042秒。決勝は日曜15:00。",
            "pulse": "オースティン土曜：COTAで公式予選",
            "keywords": "F1, アメリカGP, オースティン, COTA, ルクレール, アントネッリ, ラッセル, 予選"
        },
        "soccer": {
            "tagline": "土曜のロンドンダービー：チェルシーがスタンフォード・ブリッジでトッテナムを迎撃。金曜結果：イプスウィッチ 1-1 フォレスト。",
            "liveNow": "第8節土曜17:30英国時間：チェルシー対トッテナム（スタンフォード・ブリッジ）。金曜：イプスウィッチ 1-1 フォレスト。シティが勝点21（7勝0敗）で首位。",
            "pulse": "ダービーデー：チェルシーがスタンフォード・ブリッジでスパーズと激突",
            "keywords": "プレミアリーグ, チェルシー, トッテナム, ロンドンダービー, スタンフォード・ブリッジ, イプスウィッチ, フォレスト, 第8節"
        },
        "basketball": {
            "tagline": "本日WNBAファイナル第4戦：ドリームが2勝1敗で王手、アトランタで球団史上初優勝を狙う。",
            "liveNow": "ステートファーム・アリーナで第4戦：ドリームが97-71圧勝で2勝1敗。リーズが歴史的3戦連続ダブルダブル。ヴァルキリーズは第5戦へ望みをつなぐ戦い。",
            "pulse": "WNBAファイナル第4戦：ドリームが歴史的初制覇へ挑む",
            "keywords": "WNBAファイナル, 第4戦, ドリーム, ヴァルキリーズ, リーズ, ハワード, ステートファーム・アリーナ, 2-1"
        },
        "golf": {
            "tagline": "バミューダ第3ラウンド：ブランシェットと平田憲聖が36ホール終了時点で通算13アンダー（129）の首位タイ。",
            "liveNow": "バミューダ選手権第3R：ブランシェット（62-67）と平田憲聖（65-64）が通算-13で首位並走。コナーズが追走。ポートロイヤル（パー71）。",
            "pulse": "ポートロイヤル第3R：ブランシェットと平田憲聖が-13で首位タイ",
            "keywords": "PGAツアー, バミューダ, ポートロイヤル, ブランシェット, 平田憲聖, コナーズ, 第3R, バミューダ選手権"
        },
        "home": {
            "tonight": "土曜デスク",
            "tonightBlurb": "チェルシーがスタンフォード・ブリッジでトッテナムを迎撃。バシラシビリとメドベージェフがアルマティ決勝へ。ドリームが第4戦で王手。",
            "plTitle": "プレミアリーグ：チェルシー対トッテナムのロンドンダービーがスタンフォード・ブリッジで開催",
            "plBlurb": "金曜のイプスウィッチ対フォレスト（1-1）に続き舞台はロンドンへ。シティが7戦全勝21点で首位、アーセナル18点、ブライトン16点。",
            "f1Title": "アメリカGP：COTAで土曜公式予選",
            "f1Blurb": "オースティン金曜フリー走行はルクレールがトップ、アントネッリがわずか0.042秒差。公式予選は土曜現地16:00開始。アントネッリが102点リードを守る。"
        },
        "pg": {
            "pinFinal": "アルマティ準決勝：バシラシビリ 6-4, 6-7(5), 6-3 チチパス。メドベージェフ 6-3（棄権）ブブリク。日曜決勝：メドベージェフ対バシラシビリ。",
            "week1Closed": "NFL第7週TNF終了：ベアーズがソルジャー・フィールドでペイトリオッツを30-24で撃破",
            "week1Sub": "ウィリアムズ308ydパス・2TD、バーデン130ydレシーブ、サントス58ydのFG。ベアーズ5-2、ペイトリオッツ4-3。49ersは6勝0敗を維持。",
            "countdownTnf": "TNF終了：ベアーズ 30、ペイトリオッツ 24。ベアーズ5-2。49ers 6-0。チーフスとバイキングス5-0。ビルズ5-1。",
            "barsPoints": "バーは首位との差を示します。アントネッリが340点で首位、ラッセル（238点）に102点差。土曜はCOTAで公式予選。",
            "tableAfterMonday": "プレミアリーグ：シティが7戦全勝の21点で首位。アーセナル18点、ブライトン16点。金曜：イプスウィッチ 1-1 フォレスト。土曜にチェルシー対スパーズ。",
            "pinClub": "クラブを選択。シティは7戦全勝21点。アーセナル18点、ブライトン16点。金曜：イプスウィッチ 1-1 フォレスト。土曜にチェルシー対スパーズ。",
            "plFootnote": "金曜結果：イプスウィッチ 1-1 フォレスト。土曜：チェルシー対スパーズ、ヴィラ対シティ、ブライトン対ウルブズ。日曜：アーセナル対パレス。",
            "majorsDone": "バミューダ選手権第3Rが進行中。ブランシェット（62-67）と平田憲聖（65-64）が通算13アンダー（129）で首位並走。コナーズ追走。",
            "wnbaFirstRound": "WNBAファイナル第4戦：ドリームが97-71の大勝で2勝1敗。エンジェル・リーズが3戦連続ダブルダブル（21点12R）の快挙。第4戦アトランタ。",
            "bracketFootnote": "第1戦：ヴァルキリーズ 68、ドリーム 64。第2戦：ドリーム 79、ヴァルキリーズ 65。第3戦：ドリーム 97、ヴァルキリーズ 71。ドリームが2勝1敗で王手。第4戦はステートファーム・アリーナ。"
        }
    },
    "ko": {
        "football": {
            "tagline": "NFL 7주차 슈퍼 선데이 전야: TNF 승리 거둔 베어스 5승 2패. 무패 치프스, 49ers, 바이킹스 일요일 출격 대기.",
            "liveNow": "TNF 종료: 베어스 30, 패트리어츠 24. 일요일 주요 일정: 치프스 대 시애틀, 49ers 대 애틀랜타, 콜츠 대 미네소타.",
            "pulse": "NFL 7주차: 슈퍼 선데이 대격돌 임박",
            "keywords": "NFL 7주차, 베어스, 패트리어츠, 치프스, 49ers, 바이킹스, 케イレ브 윌리엄스, 일요일 일정"
        },
        "tennis": {
            "tagline": "알마티 토요일: 바실라시빌리가 3세트 접전 끝에 치치파스를 꺾는 이변 연출. 메드베데프는 부블리크 기권으로 결승행.",
            "liveNow": "알마티 준결승: 바실라시빌리 6-4, 6-7(5), 6-3 치치파스. 메드베데프 6-3(기권승) 부블리크. 일요일 결승: 메드베데프 대 바실라시빌리.",
            "pulse": "알마티 준결승: 바실라시빌리와 메드베데프 결승 진출",
            "keywords": "ATP, 알마티, 바실라시빌리, 치치파스, 메드베데프, 부블리크, 준결승, 결승"
        },
        "f1": {
            "tagline": "오스틴 토요일 예선: 르클레르 금요일 연습 주행 선두, 안토넬리 102점 차 리드 수성.",
            "liveNow": "COTA 토요일: 3차 연습 및 예선 현지 16:00 진행. 르클레르 FP1과 FP2 선두, 안토넬리 +0.042초. 결승 일요일 15:00.",
            "pulse": "오스틴 토요일: COTA 공식 예선",
            "keywords": "F1, 미국 GP, 오스틴, COTA, 르클레르, 안토넬리, 러셀, 예선"
        },
        "soccer": {
            "tagline": "토요일 런던 더비: 첼시가 스탬퍼드 브리지에서 토트넘과 격돌. 금요일 결과: 입스위치 1-1 노팅엄 포레스트.",
            "liveNow": "8라운드 토요일 17:30 영국시간: 스탬퍼드 브리지에서 첼시 대 토트넘. 금요일: 입스위치 1-1 포레스트. 맨시티 21점(7승 0패) 선두.",
            "pulse": "더비 데이: 첼시 스탬퍼드 브리지에서 토트넘과 격돌",
            "keywords": "프리미어리그, 첼시, 토트넘, 런던 더비, 스탬퍼드 브리지, 입스위치, 포레스트, 8라운드"
        },
        "basketball": {
            "tagline": "WNBA 파이널 4차전 오늘 개막: 드림이 2승 1패로 앞선 가운데 애틀랜타에서 창단 첫 우승 도전.",
            "liveNow": "스테이트 팜 아레나 4차전: 드림이 97-71 대승으로 2-1 리드. 리스 사상 첫 3경기 연속 파이널 더블더블. 발키리스 5차전 향한 배수의 진.",
            "pulse": "WNBA 파이널 4차전: 드림 창단 첫 우승 도전",
            "keywords": "WNBA 파이널, 4차전, 드림, 발키리스, 리스, 하워드, 스테이트 팜 아레나, 2-1"
        },
        "golf": {
            "tagline": "버뮤다 3라운드: 블랑셰와 히라타 켄세이가 36홀 합계 13언더파(129타)로 포트 로열 공동 선두 질주.",
            "liveNow": "버뮤다 챔피언십 3R: 블랑셰(62-67)와 히라타(65-64) 13언더파 공동 선두. 코너스 추격. 포트 로열 파71.",
            "pulse": "포트 로열 3라운드: 블랑셰와 히라타 13언더파 공동 선두",
            "keywords": "PGA 투어, 버뮤다, 포트 로열, 블랑셰, 히라타 켄세이, 코너스, 3라운드, 버뮤다 챔피언십"
        },
        "home": {
            "tonight": "토요일 데스크",
            "tonightBlurb": "첼시가 스탬퍼드 브리지에서 토트넘과 런던 더비 격돌. 바실라시빌리와 메드베데프 알마티 결승 진출. 드림 WNBA 4차전 첫 우승 도전.",
            "plTitle": "프리미어리그: 첼시 스탬퍼드 브리지에서 토트넘과 런던 더비 격돌",
            "plBlurb": "금요일 입스위치와 포레스트의 1-1 무승부에 이어 런던으로 시선 집중. 맨시티가 7전 전승 21점으로 선두, 아스널 18점, 브라이턴 16점.",
            "f1Title": "미국 GP: COTA 토요일 공식 예선",
            "f1Blurb": "르클레르가 오스틴 금요일 연습 선두, 안토넬리 0.042초 차 추격. 예선은 토요일 현지 16:00 시작, 안토넬리 102점 차 리드 수성."
        },
        "pg": {
            "pinFinal": "알마티 준결승: 바실라시빌리 6-4, 6-7(5), 6-3 치치파스. 메드베데프 6-3(기권승) 부블리크. 일요일 결승: 메드베데프 대 바실라시빌리.",
            "week1Closed": "NFL 7주차 TNF 종료: 베어스가 솔저 필드에서 패트리어츠를 30-24로 제압",
            "week1Sub": "윌리엄스 308야드 패스 2TD, 버든 130야드 리시빙, 산토스 58야드 FG. 베어스 5-2, 패트리어츠 4-3. 49ers 6승 0패 유지.",
            "countdownTnf": "TNF 종료: 베어스 30, 패트리어츠 24. 베어스 5-2. 49ers 6-0. 치프스와 바이킹스 5-0. 빌스 5-1.",
            "barsPoints": "막대는 선두와의 격차를 보여줍니다. 안토넬리가 340점, 러셀(238점)에 102점 앞서 있습니다. 토요일 COTA 예선 진행.",
            "tableAfterMonday": "프리미어리그: 맨시티 21점(7전 전승) 선두 질주. 아스널 18점, 브라이턴 16점. 금요일: 입스위치 1-1 포레스트. 토요일 첼시 대 토트넘.",
            "pinClub": "클럽을 선택하세요. 맨시티는 7승 0패 21점. 아스널 18점, 브라이턴 16점. 금요일: 입스위치 1-1 포레스트. 토요일 첼시 대 토트넘.",
            "plFootnote": "금요일 결과: 입스위치 1-1 포레스트. 토요일: 첼시 대 토트넘, 빌라 대 맨시티, 브라이턴 대 울버햄프턴. 일요일: 아스널 대 팰리스.",
            "majorsDone": "버뮤다 챔피언십 3라운드 진행 중. 블랑셰(62-67)와 히라타 켄세이(65-64) 13언더파 129타 공동 선두. 코너스 추격.",
            "wnbaFirstRound": "WNBA 파이널 4차전: 드림이 97-71 대승으로 2승 1패 리드. 엔젤 리스 3경기 연속 더블더블(21점 12리바운드) 대기록. 4차전 애틀랜타.",
            "bracketFootnote": "1차전: 발키리스 68, 드림 64. 2차전: 드림 79, 발키리스 65. 3차전: 드림 97, 발키리스 71. 드림이 2승 1패로 리드. 4차전 스테이트 팜 아레나."
        }
    },
    "ar": {
        "football": {
            "tagline": "NFL الاسبوع 7 عشية الاحد: بيرز 5-2 بعد فوز TNF. وتشيفس و49رز وفايكنغز بلا هزيمة يتاهبون للاحد.",
            "liveNow": "نهائي TNF: بيرز 30، باتريوتس 24. مواجهات الاحد: تشيفس في ضيافة سيهوكس، 49رز ضد فالكونز، كولتس ضد فايكنغز.",
            "pulse": "NFL الاسبوع 7: مباريات الاحد المرتقبة",
            "keywords": "NFL الاسبوع 7, بيرز, باتريوتس, تشيفس, 49رز, فايكنغز, كاليب ويليامز, مباريات الاحد"
        },
        "tennis": {
            "tagline": "الماتي السبت: باسيلاشفيلي يفجر مفاجأة ويهزم تسيتسيباس في ثلاث مجموعات. وميدفيديف يتاهل بانسحاب بوبليك.",
            "liveNow": "الماتي نصف النهائي: باسيلاشفيلي يهزم تسيتسيباس 6-4 و6-7(5) و6-3. ميدفيديف يهزم بوبليك 6-3 (انسحاب). نهائي الاحد: ميدفيديف ضد باسيلاشفيلي.",
            "pulse": "نصف نهائي الماتي: باسيلاشفيلي وميدفيديف الى النهائي",
            "keywords": "ATP, الماتي, باسيلاشفيلي, تسيتسيباس, ميدفيديف, بوبليك, نصف النهائي, النهائي"
        },
        "f1": {
            "tagline": "تجارب اوستن التاهيلية السبت: لوكلير تصدر تجارب الجمعة؛ وانتونيلي يدافع عن صدارة بفارق 102 نقطة.",
            "liveNow": "حلبة الامريكيتين السبت: التجارب الحرة 3 والتاهيلية الساعة 16:00 محليا. لوكلير تصدر التجارب 1 و2؛ انتونيلي بفارق 0.042 ثانية. السباق الاحد 15:00.",
            "pulse": "اوستن السبت: التجارب التاهيلية في حلبة الامريكيتين",
            "keywords": "فورمولا 1, جائزة امريكا الكبرى, اوستن, حلبة الامريكيتين, لوكلير, انتونيلي, راسل, تجارب تاهيلية"
        },
        "soccer": {
            "tagline": "ديربي لندن السبت: تشيلسي يستضيف توتنهام في ستامفورد بريدج. نتيجة الجمعة: ايبسويتش 1، فورست 1.",
            "liveNow": "الجولة 8 السبت 17:30 بتوقيت بريطانيا: تشيلسي ضد توتنهام في ستامفورد بريدج. الجمعة: ايبسويتش 1، فورست 1. سيتي يتصدر بـ21 نقطة (7-0-0).",
            "pulse": "يوم الديربي: تشيلسي يستضيف توتنهام في ستامفورد بريدج",
            "keywords": "الدوري الانجليزي, تشيلسي, توتنهام, ديربي لندن, ستامفورد بريدج, ايبسويتش, فورست, الجولة 8"
        },
        "basketball": {
            "tagline": "نهائيات WNBA المباراة 4 اليوم: دريم يتقدم 2-1 في السلسلة ويسعى لحسم اول لقب في تاريخه باتلانتا.",
            "liveNow": "المباراة 4 في ستيت فارم ارينا: دريم يتقدم 2-1 بعد فوزه 97-71. ريس وثالث ثنائية مزدوجة تاريخية. فالكيريز يقاتل لفرض مباراة خامسة.",
            "pulse": "نهائيات WNBA المباراة 4: دريم يسعى لحسم التتويج التاريخي",
            "keywords": "نهائيات WNBA, المباراة 4, دريم, فالكيريز, ريس, هوارد, ستيت فارم ارينا, 2-1"
        },
        "golf": {
            "tagline": "برمودا الجولة 3: بلانشيت وهيراتا يتقاسمان صدارة 36 حفرة بـ13 ضربة تحت المعدل (129) في بورت رويال.",
            "liveNow": "بطولة برمودا الجولة 3: بلانشيت (62-67) وهيراتا (65-64) في صدارة مشتركة بـ-13 ضربة. كونرز يلاحق. ملعب بورت رويال معدل 71.",
            "pulse": "بورت رويال الجولة 3: بلانشيت وهيراتا في صدارة مشتركة بـ-13",
            "keywords": "جولة PGA, برمودا, بورت رويال, بلانشيت, هيراتا, كونرز, الجولة 3, بطولة برمودا"
        },
        "home": {
            "tonight": "مكتب السبت",
            "tonightBlurb": "تشيلسي يستضيف توتنهام في ستامفورد بريدج. باسيلاشفيلي وميدفيديف الى نهائي الماتي. دريم يسعى لحسم لقب WNBA في المباراة 4.",
            "plTitle": "الدوري الانجليزي: تشيلسي يستضيف توتنهام في ديربي لندن بستامفورد بريدج",
            "plBlurb": "تتجه الانظار الى لندن بعد تعادل ايبسويتش وفورست 1-1 الجمعة. سيتي يتصدر بـ21 نقطة (7-0-0)، ارسنال 18، برايتون 16.",
            "f1Title": "جائزة امريكا الكبرى: التجارب التاهيلية السبت في حلبة الامريكيتين",
            "f1Blurb": "لوكلير تصدر تجارب الجمعة في اوستن بفارق 0.042 ثانية عن انتونيلي. التاهيل السبت الساعة 16:00 محليا؛ انتونيلي يدافع عن فارق 102 نقطة."
        },
        "pg": {
            "pinFinal": "الماتي نصف النهائي: باسيلاشفيلي يهزم تسيتسيباس 6-4 و6-7(5) و6-3. ميدفيديف يهزم بوبليك 6-3 (انسحاب). نهائي الاحد: ميدفيديف ضد باسيلاشفيلي.",
            "week1Closed": "NFL الاسبوع 7 نهاية TNF: بيرز يهزم باتريوتس 30-24 في سولجر فيلد",
            "week1Sub": "ويليامز 308 ياردات تمرير و2 TD؛ بيردن 130 ياردة استقبال؛ سانتوس هدف ميداني من 58 ياردة. بيرز 5-2، باتريوتس 4-3. 49رز 6-0.",
            "countdownTnf": "نهاية TNF: بيرز 30، باتريوتس 24. بيرز 5-2. 49رز 6-0. تشيفس وفايكنغز 5-0. بيلز 5-1.",
            "barsPoints": "الاعمدة توضح الفارق مع المتصدر. انتونيلي يملك 340 نقطة، متقدما بـ102 على راسل (238). التجارب التاهيلية السبت في اوستن.",
            "tableAfterMonday": "الدوري الانجليزي: سيتي يتصدر بـ21 نقطة (7-0-0). ارسنال 18، برايتون 16. الجمعة: ايبسويتش 1، فورست 1. تشيلسي ضد توتنهام السبت.",
            "pinClub": "اختر ناديا. سيتي 7-0-0 برصيد 21 نقطة. ارسنال 18، برايتون 16. الجمعة: ايبسويتش 1، فورست 1. تشيلسي ضد توتنهام السبت.",
            "plFootnote": "الجمعة نهائي: ايبسويتش 1، فورست 1. السبت: تشيلسي ضد توتنهام، فيلا ضد سيتي، برايتون ضد وولفز. الاحد: ارسنال ضد بالاس.",
            "majorsDone": "بطولة برمودا الجولة 3 جارية. بلانشيت (62-67) وهيراتا (65-64) يتقاسمان الصدارة بـ-13 (129 ضربة). كونرز يلاحق.",
            "wnbaFirstRound": "نهائيات WNBA المباراة 4: دريم يتقدم 2-1 بعد فوزه 97-71. انجيل ريس وثالث ثنائية مزدوجة تاريخية (21 نقطة و12 متابعة). المباراة 4 باتلانتا.",
            "bracketFootnote": "المباراة 1: فالكيريز 68، دريم 64. المباراة 2: دريم 79، فالكيريز 65. المباراة 3: دريم 97، فالكيريز 71. دريم يتقدم 2-1. المباراة 4 في ستيت فارم ارينا."
        }
    }
}

# Strict validation against em-dashes and double-hyphens
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

print("All locale updates for 24 Oct 2026 completed successfully!")
