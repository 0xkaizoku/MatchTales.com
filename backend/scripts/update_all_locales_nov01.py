# -*- coding: utf-8 -*-
"""
Update playground.ts, messages.ts, and all messages-*.ts files for 1 November 2026.
"""
import re
import os

DATA = {
    "en": {
        "f1": {
            "tagline": "Mexico City GP: Kimi Antonelli finishes P2 behind Leclerc to become youngest F1 World Champion in history.",
            "liveNow": "Final at Hermanos Rodriguez: Charles Leclerc wins Mexico GP; Kimi Antonelli (Mercedes) finishes P2 to mathematically clinch the 2026 World Championship.",
            "pulse": "2026 F1 WORLD CHAMPION: KIMI ANTONELLI MAKES MOTORSPORT HISTORY IN MEXICO",
            "keywords": "Formula 1, Mexico City GP, Antonelli, World Champion, Leclerc, Mercedes, Autodromo Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open: Raul Pereda shoots 66 to become first Mexican PGA Tour winner on home soil.",
            "liveNow": "Final at VidantaVallarta: Raul Pereda (-17, 267) birdies 15 and 17 to edge Austin Smotherman (-15, 269) by two shots for historic maiden victory.",
            "pulse": "PGA TOUR MEXICO OPEN: RAUL PEREDA CLAIMS HISTORIC HOME TRIUMPH AT -17",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Raul Pereda, Austin Smotherman, VidantaVallarta, champion"
        },
        "football": {
            "tagline": "NFL Week 8: Undefeated Vikings stifle Colts 24-17 to advance to 7-0 behind Sam Darnold and Justin Jefferson.",
            "liveNow": "Final in Minneapolis: Vikings 24, Colts 17. Darnold 274 yds, 2 TD to Jefferson (128 rec yds). Minnesota stands as NFL's only 7-0 team.",
            "pulse": "NFL WEEK 8: MINNESOTA VIKINGS REMAIN PERFECT AT 7-0 AFTER HOLDING OFF COLTS",
            "keywords": "NFL Week 8, Minnesota Vikings, Indianapolis Colts, Sam Darnold, Justin Jefferson, undefeated"
        },
        "tennis": {
            "tagline": "Erste Bank Open Final: Carlos Alcaraz sweeps Lorenzo Musetti 6-3, 6-4 to lift Vienna ATP 500 crown.",
            "liveNow": "Vienna Championship: Alcaraz def. Musetti 6-3, 6-4 in 84 minutes. Alcaraz wins 6th title of 2026 without dropping a single set all week.",
            "pulse": "ERSTE BANK OPEN: CARLOS ALCARAZ SWEEPS LORENZO MUSETTI TO CAPTURE VIENNA TITLE",
            "keywords": "ATP, Vienna, Erste Bank Open, Alcaraz, Musetti, champion, Wiener Stadthalle"
        },
        "basketball": {
            "tagline": "NBA Sunday: Shai Gilgeous-Alexander pours in 36 points as defending champion Thunder edge Clippers 116-109.",
            "liveNow": "Final in Inglewood: Thunder 116, Clippers 109. Gilgeous-Alexander 36 pts, 9 ast; Holmgren 18 pts, 4 blk. Oklahoma City improves to 4-0.",
            "pulse": "NBA SUNDAY: SHAI GILGEOUS-ALEXANDER LEADS UNBEATEN THUNDER PAST CLIPPERS",
            "keywords": "NBA, Thunder, Clippers, Gilgeous-Alexander, Holmgren, Kawhi Leonard, Intuit Dome"
        },
        "soccer": {
            "tagline": "Premier League MW9: Cole Palmer strikes winner as Chelsea edge Newcastle 2-1; City lead table on 24 points.",
            "liveNow": "Premier League Sunday: Chelsea 2-1 Newcastle (Jackson 18', Palmer 47'; Isak 32'). Chelsea climb to 16 pts. Man City lead league with 24 pts.",
            "pulse": "PREMIER LEAGUE MW9: COLE PALMER STRIKES AS CHELSEA DOWN NEWCASTLE 2-1",
            "keywords": "Premier League, Chelsea, Newcastle, Cole Palmer, Nicolas Jackson, Stamford Bridge"
        },
        "home": {
            "tonight": "Sunday desk",
            "tonightBlurb": "Antonelli crowned youngest F1 champion in history. Pereda wins Mexico Open in historic home triumph. Vikings remain 7-0.",
            "plTitle": "Formula 1: Kimi Antonelli becomes youngest World Champion in history",
            "plBlurb": "Mercedes prodigy finishes P2 behind Charles Leclerc in Mexico City GP to clinch the 2026 World Drivers' Championship at 20 years old.",
            "f1Title": "PGA Tour: Raul Pereda claims emotional maiden title at VidantaWorld Mexico Open",
            "f1Blurb": "Local hero shoots final-round 66 to finish at 17-under, becoming the first Mexican golfer to win the national open on the PGA Tour."
        },
        "pg": {
            "pinFinal": "Mexico City GP: Leclerc wins, Antonelli finishes P2 to clinch 2026 World Championship.",
            "week1Closed": "NFL Week 8 Sunday: Vikings 24, Colts 17 to stay perfect at 7-0. Packers beat Panthers 27-17 on TNF.",
            "week1Sub": "Darnold 2 TDs to Jefferson. Vikings (7-0) stand as the only undefeated team in the NFL.",
            "countdownTnf": "Week 8 Final: Undefeated Vikings (7-0) handle Colts 24-17. Packers (6-2) roll past Panthers.",
            "barsPoints": "Antonelli clinches title with 383 pts, leading Russell (252) by 131 points with 3 rounds left.",
            "tableAfterMonday": "Premier League Matchweek 9: City lead with 24 pts, Arsenal 22, Liverpool and Chelsea 16.",
            "pinClub": "Select a club. City lead on 24, Arsenal 22, Liverpool and Chelsea on 16.",
            "plFootnote": "PL MW9: Chelsea 2-1 Newcastle, Arsenal 2-2 Liverpool, Man City 1-0 Southampton.",
            "majorsDone": "VidantaWorld Mexico Open Final: Raul Pereda (-17, 267) wins historic maiden title by two shots."
        }
    },
    "fr": {
        "f1": {
            "tagline": "GP du Mexique : Kimi Antonelli termine 2e et devient le plus jeune champion du monde de F1 de l'histoire.",
            "liveNow": "Course a Mexico : Charles Leclerc gagne le GP ; Kimi Antonelli (Mercedes) finit 2e et s'assure mathematiquement le titre mondial 2026.",
            "pulse": "CHAMPION DU MONDE F1 2026 : KIMI ANTONELLI ENTRE DANS LA LEGENDE A MEXICO",
            "keywords": "Formule 1, GP du Mexique, Antonelli, champion du monde, Leclerc, Mercedes"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open : Raul Pereda signe un 66 et devient le premier Mexicain vainqueur a domicile.",
            "liveNow": "Finale a VidantaVallarta : Raul Pereda (-17, 267) devance Austin Smotherman (-15, 269) de deux coups pour un sacre historique.",
            "pulse": "PGA TOUR MEXICO OPEN : TRIOMPHE HISTORIQUE DU MEXICAIN RAUL PEREDA A -17",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Raul Pereda, Smotherman, VidantaVallarta"
        },
        "football": {
            "tagline": "NFL Semaine 8 : Les Vikings toujours parfaits (7-0) apres leur victoire 24-17 sur les Colts.",
            "liveNow": "Score final a Minneapolis : Vikings 24, Colts 17. Darnold 274 yds, 2 TD pour Jefferson (128 yds). Minnesota reste la seule equipe a 7-0.",
            "pulse": "NFL SEMAINE 8 : LES MINNESOTA VIKINGS IMBATTABLES A 7-0 APRES LEUR SUCCES SUR LES COLTS",
            "keywords": "NFL Semaine 8, Minnesota Vikings, Indianapolis Colts, Darnold, Jefferson, invaincus"
        },
        "tennis": {
            "tagline": "Tournoi de Vienne finale : Carlos Alcaraz ecarte Lorenzo Musetti 6-3, 6-4 et s'offre la couronne.",
            "liveNow": "Finale a Vienne : Alcaraz bat Musetti 6-3, 6-4 en 84 minutes. Alcaraz s'adjuge son 6e titre de l'annee sans ceder le moindre set.",
            "pulse": "TOURNOI DE VIENNE : CARLOS ALCARAZ S'OFFRE LE TITRE SANS PERDRE UN SEUL SET",
            "keywords": "ATP, Vienne, Erste Bank Open, Alcaraz, Musetti, champion"
        },
        "basketball": {
            "tagline": "NBA dimanche : Shai Gilgeous-Alexander compile 36 points et le Thunder bat les Clippers 116-109.",
            "liveNow": "Fin de match a Los Angeles : Thunder 116, Clippers 109. Gilgeous-Alexander 36 pts, 9 passes ; Holmgren 18 pts, 4 contres. OKC a 4-0.",
            "pulse": "NBA DIMANCHE : SHAI GILGEOUS-ALEXANDER GUIDE LE THUNDER INVAINCU FACE AUX CLIPPERS",
            "keywords": "NBA, Thunder, Clippers, Gilgeous-Alexander, Holmgren, Intuit Dome"
        },
        "soccer": {
            "tagline": "Premier League J9 : Cole Palmer offre la victoire a Chelsea 2-1 contre Newcastle ; City toujours leader.",
            "liveNow": "Premier League dimanche : Chelsea 2-1 Newcastle (Jackson 18', Palmer 47' ; Isak 32'). Chelsea monte a 16 pts. Man City premier avec 24 pts.",
            "pulse": "PREMIER LEAGUE J9 : COLE PALMER FAIT PLIER NEWCASTLE ET LANCE CHELSEA (2-1)",
            "keywords": "Premier League, Chelsea, Newcastle, Cole Palmer, Stamford Bridge"
        },
        "home": {
            "tonight": "Desk du dimanche",
            "tonightBlurb": "Antonelli plus jeune champion F1 de l'histoire. Pereda gagne l'Open du Mexique. Les Vikings toujours parfaits a 7-0.",
            "plTitle": "Formule 1 : Kimi Antonelli devient le plus jeune champion du monde de l'histoire",
            "plBlurb": "Le prodige de Mercedes termine 2e derriere Charles Leclerc a Mexico et s'adjuge le titre mondial 2026 a seulement 20 ans.",
            "f1Title": "PGA Tour : Raul Pereda triomphe avec emotion au VidantaWorld Mexico Open",
            "f1Blurb": "Le Mexicain rend une carte finale de 66 a -17 pour devenir le premier golfeur local victorieux de l'Open national sur le PGA Tour."
        },
        "pg": {
            "pinFinal": "GP du Mexique : Leclerc s'impose, Antonelli finit 2e et s'assure le titre mondial 2026.",
            "week1Closed": "NFL Semaine 8 dimanche : Vikings 24, Colts 17 pour rester parfaits a 7-0. Packers 27, Panthers 17 jeudi.",
            "week1Sub": "Darnold 2 TD pour Jefferson. Les Vikings (7-0) sont la seule franchise invaincue de la NFL.",
            "countdownTnf": "Bilan Semaine 8 : Les Vikings invaincus (7-0) battent les Colts 24-17. Les Packers (6-2) enchainent.",
            "barsPoints": "Antonelli champion avec 383 pts, 131 d'avance sur Russell (252) a 3 courses du terme.",
            "tableAfterMonday": "Premier League 9e journee : City mene avec 24 pts, Arsenal 22, Liverpool et Chelsea 16.",
            "pinClub": "Choisissez un club. City est premier avec 24 pts, Arsenal 22, Liverpool et Chelsea 16.",
            "plFootnote": "PL J9 : Chelsea 2-1 Newcastle, Arsenal 2-2 Liverpool, Man City 1-0 Southampton.",
            "majorsDone": "VidantaWorld Mexico Open : Raul Pereda (-17, 267) signe un exploit historique et gagne de deux coups."
        }
    },
    "es": {
        "f1": {
            "tagline": "GP de Mexico: Kimi Antonelli finaliza 2° tras Leclerc y se corona como el campeon mas joven de la historia de la F1.",
            "liveNow": "Final en Mexico: Charles Leclerc gana el Gran Premio; Kimi Antonelli (Mercedes) asegura matematicamente el Mundial 2026 con su 2° puesto.",
            "pulse": "CAMPEON DEL MUNDO F1 2026: KIMI ANTONELLI HACE HISTORIA EN LA CIUDAD DE MEXICO",
            "keywords": "Formula 1, GP de Mexico, Antonelli, campeon del mundo, Leclerc, Mercedes"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open: Raul Pereda firma un 66 y se convierte en el primer mexicano campeon en casa.",
            "liveNow": "Final en VidantaVallarta: Raul Pereda (-17, 267) bate por dos golpes a Austin Smotherman (-15, 269) para una victoria historica.",
            "pulse": "PGA TOUR MEXICO OPEN: RAUL PEREDA LOGRA UN TRIUNFO HISTORICO EN CASA CON -17",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Raul Pereda, Smotherman, VidantaVallarta"
        },
        "football": {
            "tagline": "NFL Semana 8: Los invictos Vikings vencen 24-17 a los Colts y avanzan a 7-0 liderados por Darnold y Jefferson.",
            "liveNow": "Final en Minneapolis: Vikings 24, Colts 17. Darnold 274 yds, 2 TD para Jefferson (128 yds). Minnesota es el unico 7-0 de la liga.",
            "pulse": "NFL SEMANA 8: MINNESOTA VIKINGS SIGUEN PERFECTOS TRAS DERROTAR A COLTS (7-0)",
            "keywords": "NFL Semana 8, Minnesota Vikings, Indianapolis Colts, Darnold, Jefferson, invictos"
        },
        "tennis": {
            "tagline": "ATP Viena final: Carlos Alcaraz supera 6-3, 6-4 a Lorenzo Musetti y levanta la corona austriaca.",
            "liveNow": "Final de Viena: Alcaraz vence a Musetti 6-3, 6-4 en 84 minutos. Sexto titulo de 2026 sin ceder un solo set en el torneo.",
            "pulse": "ATP VIENA: CARLOS ALCARAZ DOBLEGA A LORENZO MUSETTI Y CONQUISTA EL TITULO",
            "keywords": "ATP, Viena, Erste Bank Open, Alcaraz, Musetti, campeon"
        },
        "basketball": {
            "tagline": "NBA domingo: Shai Gilgeous-Alexander anota 36 puntos y el campeon Thunder supera 116-109 a Clippers.",
            "liveNow": "Final en Los Angeles: Thunder 116, Clippers 109. Gilgeous-Alexander 36 pts, 9 ast; Holmgren 18 pts, 4 tap. OKC se pone 4-0.",
            "pulse": "NBA DOMINGO: SHAI GILGEOUS-ALEXANDER GUIA AL INVICTO THUNDER ANTE CLIPPERS",
            "keywords": "NBA, Thunder, Clippers, Gilgeous-Alexander, Holmgren, Intuit Dome"
        },
        "soccer": {
            "tagline": "Premier League J9: Cole Palmer firma el gol del triunfo en el 2-1 del Chelsea al Newcastle; City lider con 24.",
            "liveNow": "Premier League domingo: Chelsea 2-1 Newcastle (Jackson 18', Palmer 47'; Isak 32'). Chelsea suma 16 pts. Man City manda con 24 pts.",
            "pulse": "PREMIER LEAGUE J9: COLE PALMER DECIDE EL TRIUNFO DEL CHELSEA SOBRE NEWCASTLE (2-1)",
            "keywords": "Premier League, Chelsea, Newcastle, Cole Palmer, Stamford Bridge"
        },
        "home": {
            "tonight": "Edicion del domingo",
            "tonightBlurb": "Antonelli el campeon mas joven de la F1. Pereda campeon historico del Mexico Open. Los Vikings siguen 7-0.",
            "plTitle": "Formula 1: Kimi Antonelli se convierte en el campeon del mundo mas joven de la historia",
            "plBlurb": "El italiano de Mercedes finaliza segundo tras Charles Leclerc en Mexico para cerrar el campeonato mundial 2026 con 20 anos.",
            "f1Title": "PGA Tour: Raul Pereda emociona a Mexico al coronarse en VidantaWorld",
            "f1Blurb": "El veracruzano firma 66 golpes para acabar con -17 y ser el primer mexicano que gana el torneo nacional en el PGA Tour."
        },
        "pg": {
            "pinFinal": "GP de Mexico: Victoria de Leclerc, Antonelli termina 2° y se corona campeon mundial de F1 2026.",
            "week1Closed": "NFL Semana 8 domingo: Vikings 24, Colts 17 para seguir 7-0. Packers ganaron 27-17 a Panthers el jueves.",
            "week1Sub": "Darnold 2 TD a Jefferson. Los Vikings (7-0) son el unico equipo invicto en toda la NFL.",
            "countdownTnf": "Semana 8 final: Vikings (7-0) derrotan 24-17 a Colts. Packers (6-2) ganaron en TNF.",
            "barsPoints": "Antonelli asegura el titulo con 383 pts, aventajando en 131 puntos a Russell a falta de 3 carreras.",
            "tableAfterMonday": "Premier League jornada 9: City lider con 24 pts, Arsenal 22, Liverpool y Chelsea 16.",
            "pinClub": "Elige un club. City manda con 24, Arsenal 22, Liverpool y Chelsea empatan en 16.",
            "plFootnote": "PL J9: Chelsea 2-1 Newcastle, Arsenal 2-2 Liverpool, Man City 1-0 Southampton.",
            "majorsDone": "VidantaWorld Mexico Open: Raul Pereda (-17, 267) gana con dos golpes de ventaja en historica victoria."
        }
    },
    "de": {
        "f1": {
            "tagline": "Formel 1 Mexiko GP: Kimi Antonelli wird Zweiter hinter Leclerc und ist juengster Weltmeister aller Zeiten.",
            "liveNow": "Rennen in Mexiko: Charles Leclerc siegt; Kimi Antonelli (Mercedes) sichert sich auf P2 rechnerisch den WM-Titel 2026.",
            "pulse": "FORMEL 1 WELTMEISTER 2026: KIMI ANTONELLI SCHREIBT GESCHICHTE IN MEXIKO",
            "keywords": "Formel 1, Mexiko GP, Antonelli, Weltmeister, Leclerc, Mercedes"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open: Raul Pereda triumphiert mit 66er-Runde als erster mexikanischer Heimsieger.",
            "liveNow": "Finale in VidantaVallarta: Raul Pereda (-17, 267) siegt mit zwei Schlaegen Vorsprung vor Austin Smotherman (-15, 269).",
            "pulse": "PGA TOUR MEXICO OPEN: RAUL PEREDA TRIUMPHERT MIT -17 IN DER HEIMAT",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Raul Pereda, Smotherman, VidantaVallarta"
        },
        "football": {
            "tagline": "NFL Woche 8: Ungeschlagene Vikings bezwingen Colts 24:17 und stehen dank Darnold bei 7:0.",
            "liveNow": "Endstand in Minneapolis: Vikings 24, Colts 17. Darnold 274 Yds, 2 TD auf Jefferson (128 Yds). Minnesota bleibt bei 7:0.",
            "pulse": "NFL WOCHE 8: MINNESOTA VIKINGS BLEIBEN NACH SIEG GEGEN COLTS PERFEKT BEI 7:0",
            "keywords": "NFL Woche 8, Minnesota Vikings, Indianapolis Colts, Darnold, Jefferson, ungeschlagen"
        },
        "tennis": {
            "tagline": "Erste Bank Open Finale: Carlos Alcaraz besiegt Lorenzo Musetti 6:3, 6:4 und holt den Wiener Titel.",
            "liveNow": "Wien Finale: Alcaraz schl. Musetti 6:3, 6:4 in 84 Minuten. Sechster Titel 2026 ohne Satzverlust im Turnier.",
            "pulse": "ERSTE BANK OPEN: CARLOS ALCARAZ GEWINNT DEN TITEL IN WIEN OHNE SATZVERLUST",
            "keywords": "ATP, Wien, Erste Bank Open, Alcaraz, Musetti, Champion"
        },
        "basketball": {
            "tagline": "NBA Sonntag: Shai Gilgeous-Alexander erzielt 36 Punkte beim 116:109 des Meisters Thunder gegen die Clippers.",
            "liveNow": "Endstand in Inglewood: Thunder 116, Clippers 109. Gilgeous-Alexander 36 Pkt, 9 Ass; Holmgren 18 Pkt. OKC bei 4:0.",
            "pulse": "NBA SONNTAG: SHAI GILGEOUS-ALEXANDER FUEHRT UNGESCHLAGENE THUNDER ZUM SIEG",
            "keywords": "NBA, Thunder, Clippers, Gilgeous-Alexander, Holmgren, Intuit Dome"
        },
        "soccer": {
            "tagline": "Premier League 9. Spieltag: Cole Palmer schiesst Chelsea zum 2:1 ueber Newcastle; City Tabellenfuehrer mit 24.",
            "liveNow": "Premier League Sonntag: Chelsea 2:1 Newcastle (Jackson 18., Palmer 47.; Isak 32.). Chelsea bei 16 Pkt. City fuehrt mit 24.",
            "pulse": "PREMIER LEAGUE: COLE PALMER SCHLIESST CHELSEA ZUM 2:1-ERFOLG UEBER NEWCASTLE",
            "keywords": "Premier League, Chelsea, Newcastle, Cole Palmer, Stamford Bridge"
        },
        "home": {
            "tonight": "Sonntagsausgabe",
            "tonightBlurb": "Antonelli juengster F1-Weltmeister aller Zeiten. Pereda siegt bei Mexico Open. Vikings stehen bei 7:0.",
            "plTitle": "Formel 1: Kimi Antonelli kroent sich zum juengsten Weltmeister der Geschichte",
            "plBlurb": "Mercedes-Star wird in Mexiko Zweiter hinter Charles Leclerc und sichert sich mit 20 Jahren den WM-Titel 2026.",
            "f1Title": "PGA Tour: Raul Pereda feiert emotionalen Heimsieg bei den Mexico Open",
            "f1Blurb": "Der Mexikaner spielt eine 66er-Schlussrunde fuer ein Gesamtergebnis von -17 und triumphiert vor heimischer Kulisse."
        },
        "pg": {
            "pinFinal": "Mexiko GP: Leclerc siegt, Antonelli auf P2 rechnerisch Weltmeister 2026.",
            "week1Closed": "NFL Woche 8 Sonntag: Vikings 24, Colts 17 fuer makellose 7:0-Bilanz. Packers schlugen Panthers 27:17.",
            "week1Sub": "Darnold 2 TDs auf Jefferson. Die Vikings (7:0) bleiben das einzige ungeschlagene NFL-Team.",
            "countdownTnf": "Woche 8 Rueckblick: Ungeschlagene Vikings (7:0) siegen 24:17. Packers stehen bei 6:2.",
            "barsPoints": "Antonelli holt Titel mit 383 Pkt, 131 Punkte vor Russell bei noch 3 ausstehenden Rennen.",
            "tableAfterMonday": "Premier League 9. Spieltag: City fuehrt mit 24 Pkt, Arsenal 22, Liverpool und Chelsea 16.",
            "pinClub": "Klub waehlen. City hat 24 Punkte, Arsenal 22, Liverpool und Chelsea jeweils 16.",
            "plFootnote": "PL 9. Spieltag: Chelsea 2:1 Newcastle, Arsenal 2:2 Liverpool, Man City 1:0 Southampton.",
            "majorsDone": "VidantaWorld Mexico Open Finale: Raul Pereda (-17, 267) gewinnt sensationell mit 2 Schlaegen Vorsprung."
        }
    },
    "it": {
        "f1": {
            "tagline": "GP Messico: Kimi Antonelli e 2° dietro a Leclerc e diventa il piu giovane campione del mondo di F1.",
            "liveNow": "Gara a Citta del Messico: Charles Leclerc vince il GP; Kimi Antonelli (Mercedes) chiude 2° ed e campione del mondo 2026.",
            "pulse": "CAMPIONE DEL MONDO F1 2026: KIMI ANTONELLI NELLA STORIA A CITTA DEL MESSICO",
            "keywords": "Formula 1, GP Messico, Antonelli, campione del mondo, Leclerc, Mercedes"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open: Raul Pereda gira in 66 e diventa il primo messicano a trionfare in casa.",
            "liveNow": "Finale a VidantaVallarta: Raul Pereda (-17, 267) batte di due colpi Austin Smotherman (-15, 269) per una vittoria da favola.",
            "pulse": "PGA TOUR MEXICO OPEN: RAUL PEREDA FIRMA IL TRIONFO IN CASA A -17",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Raul Pereda, Smotherman, VidantaVallarta"
        },
        "football": {
            "tagline": "NFL Week 8: I Vikings restano imbattuti sul 7-0 superando 24-17 i Colts con Darnold e Jefferson.",
            "liveNow": "Finale a Minneapolis: Vikings 24, Colts 17. Darnold 274 yd, 2 TD per Jefferson (128 yd). Minnesota sola sul 7-0.",
            "pulse": "NFL WEEK 8: MINNESOTA VIKINGS PERFETTI SUL 7-0 DOPO IL SUCCESSO SUI COLTS",
            "keywords": "NFL Week 8, Minnesota Vikings, Indianapolis Colts, Darnold, Jefferson, imbattuti"
        },
        "tennis": {
            "tagline": "Erste Bank Open finale: Carlos Alcaraz piega Lorenzo Musetti 6-3, 6-4 e conquista il titolo a Vienna.",
            "liveNow": "Finale a Vienna: Alcaraz batte Musetti 6-3, 6-4 in 84 minuti. Sesto trofeo del 2026 senza perdere alcun set in settimana.",
            "pulse": "ERSTE BANK OPEN: CARLOS ALCARAZ SUPERA LORENZO MUSETTI E FA SUO IL TITOLO A VIENNA",
            "keywords": "ATP, Vienna, Erste Bank Open, Alcaraz, Musetti, campione"
        },
        "basketball": {
            "tagline": "NBA domenica: Shai Gilgeous-Alexander ne mette 36 e il Thunder campione piega i Clippers 116-109.",
            "liveNow": "Finale a Los Angeles: Thunder 116, Clippers 109. Gilgeous-Alexander 36 pt, 9 ast; Holmgren 18 pt. OKC a 4-0.",
            "pulse": "NBA DOMENICA: SHAI GILGEOUS-ALEXANDER GUIDA IL THUNDER IMBATTUTO SUI CLIPPERS",
            "keywords": "NBA, Thunder, Clippers, Gilgeous-Alexander, Holmgren, Intuit Dome"
        },
        "soccer": {
            "tagline": "Premier League 9ª giornata: Cole Palmer decide Chelsea-Newcastle 2-1; Manchester City primo a 24 punti.",
            "liveNow": "Premier League domenica: Chelsea 2-1 Newcastle (Jackson 18', Palmer 47'; Isak 32'). Chelsea a 16 pt. City in testa a 24.",
            "pulse": "PREMIER LEAGUE: IL CHELSEA VOLA CON COLE PALMER, NEWCASTLE BATTUTO 2-1",
            "keywords": "Premier League, Chelsea, Newcastle, Cole Palmer, Stamford Bridge"
        },
        "home": {
            "tonight": "Edizione della domenica",
            "tonightBlurb": "Antonelli piu giovane campione F1 della storia. Pereda trionfa al Mexico Open. Vikings imbattuti sul 7-0.",
            "plTitle": "Formula 1: Kimi Antonelli e il piu giovane campione del mondo della storia",
            "plBlurb": "Il talento della Mercedes chiude 2° dietro a Charles Leclerc in Messico e vince il titolo mondiale 2026 a soli 20 anni.",
            "f1Title": "PGA Tour: Raul Pereda fa sognare il Messico vincendo il Mexico Open",
            "f1Blurb": "Giro finale da 66 colpi per chiudere a -17: e il primo messicano a trionfare nell'Open nazionale nel PGA Tour."
        },
        "pg": {
            "pinFinal": "GP Messico: Vince Leclerc, Antonelli 2° si laurea campione del mondo 2026.",
            "week1Closed": "NFL Week 8 domenica: Vikings 24, Colts 17 per restare imbattuti sul 7-0. Packers vincenti giovedi.",
            "week1Sub": "Darnold 2 TD per Jefferson. I Vikings (7-0) sono l'unica squadra ancora imbattuta in NFL.",
            "countdownTnf": "Week 8 bilancio: Vikings perfetti a 7-0 dopo il 24-17 sui Colts. Packers salgono a 6-2.",
            "barsPoints": "Antonelli campione a 383 pt, 131 lunghezze su Russell a tre GP dal termine della stagione.",
            "tableAfterMonday": "Premier League 9ª giornata: City in testa a 24 pt, Arsenal 22, Liverpool e Chelsea 16.",
            "pinClub": "Scegli un club. City primo a 24 punti, Arsenal 22, Liverpool e Chelsea appaiate a 16.",
            "plFootnote": "PL 9ª giornata: Chelsea 2-1 Newcastle, Arsenal 2-2 Liverpool, Man City 1-0 Southampton.",
            "majorsDone": "VidantaWorld Mexico Open Finale: Raul Pereda (-17, 267) trionfa di due colpi tra gli applausi."
        }
    },
    "pl": {
        "f1": {
            "tagline": "GP Meksyku: Kimi Antonelli zajmuje 2. miejsce za Leclerkiem i zostaje najmlodszym mistrzem swiata F1.",
            "liveNow": "Wyscig w Meksyku: Charles Leclerc wygrywa; Kimi Antonelli (Mercedes) konczy na P2 i pieczetuje tytul mistrza swiata 2026.",
            "pulse": "MISTRZ SWIATA F1 2026: KIMI ANTONELLI PRZECHODZI DO HISTORII W MEKSYKU",
            "keywords": "Formula 1, GP Meksyku, Antonelli, mistrz swiata, Leclerc, Mercedes"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open: Raul Pereda uzyskuje 66 i jako pierwszy Meksykanin wygrywa u siebie.",
            "liveNow": "Final w VidantaVallarta: Raul Pereda (-17, 267) wyprzedza Austina Smothermana (-15, 269) o dwa uderzenia w historycznym triumfie.",
            "pulse": "PGA TOUR MEXICO OPEN: RAUL PEREDA ODNOSI HISTORYCZNY SUKCES W DOMU Z WYNIKIEM -17",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Raul Pereda, Smotherman, VidantaVallarta"
        },
        "football": {
            "tagline": "NFL Tydzien 8: Niepokonani Vikings pokonuja Colts 24:17 i maja bilans 7-0 dzieki akcjom Darnolda i Jeffersona.",
            "liveNow": "Koniec w Minneapolis: Vikings 24, Colts 17. Darnold 274 jardy, 2 TD do Jeffersona (128 jardow). Minnesota samotnym liderem 7-0.",
            "pulse": "NFL TYDZIEN 8: MINNESOTA VIKINGS POZOSTAJA PERFEKCYJNI NA CZELE Z BILANSEM 7-0",
            "keywords": "NFL Tydzien 8, Minnesota Vikings, Indianapolis Colts, Darnold, Jefferson, niepokonani"
        },
        "tennis": {
            "tagline": "Erste Bank Open final: Carlos Alcaraz pokonuje Lorenzo Musettiego 6:3, 6:4 i wznosi puchar w Wiedniu.",
            "liveNow": "Final w Wiedniu: Alcaraz wygrywa z Musettim 6:3, 6:4 w 84 minuty. Szosty tytul w 2026 roku bez straty chocby seta.",
            "pulse": "ERSTE BANK OPEN: CARLOS ALCARAZ POKONUJE LORENZO MUSETTIEGO I ZDOBYWA TYTUL W WIEDNIU",
            "keywords": "ATP, Wieden, Erste Bank Open, Alcaraz, Musetti, mistrz"
        },
        "basketball": {
            "tagline": "NBA niedziela: Shai Gilgeous-Alexander rzuca 36 punktow, a mistrzowie Thunder wygrywaja z Clippers 116:109.",
            "liveNow": "Koniec w Inglewood: Thunder 116, Clippers 109. Gilgeous-Alexander 36 pkt, 9 as; Holmgren 18 pkt, 4 blk. OKC ma 4-0.",
            "pulse": "NBA NIEDZIELA: SHAI GILGEOUS-ALEXANDER PROWADZI NIEPOKONANYCH THUNDER DO WYGRANEJ",
            "keywords": "NBA, Thunder, Clippers, Gilgeous-Alexander, Holmgren, Intuit Dome"
        },
        "soccer": {
            "tagline": "Premier League 9. kolejka: Cole Palmer daje Chelsea zwyciestwo 2:1 nad Newcastle; City na czele z 24 pkt.",
            "liveNow": "Premier League niedziela: Chelsea 2:1 Newcastle (Jackson 18', Palmer 47'; Isak 32'). Chelsea ma 16 pkt. Man City prowadzi z 24 pkt.",
            "pulse": "PREMIER LEAGUE: BLYSK COLE'A PALMERA ZAPEWNIA CHELSEA TRIUMF 2:1 NAD NEWCASTLE",
            "keywords": "Premier League, Chelsea, Newcastle, Cole Palmer, Stamford Bridge"
        },
        "home": {
            "tonight": "Wydanie niedzielne",
            "tonightBlurb": "Antonelli najmlodszym mistrzem F1 w historii. Pereda triumfuje w Mexico Open. Vikings bez porazki (7-0).",
            "plTitle": "Formula 1: Kimi Antonelli najmlodszym mistrzem swiata w dziejach",
            "plBlurb": "Mlodzieniec Mercedesa zajmuje 2. miejsce za Charlesem Leclerkiem w Meksyku i zdobywa tytul majac zaledwie 20 lat.",
            "f1Title": "PGA Tour: Raul Pereda zachwyca Meksyk wielkim zwyciestwem w VidantaWorld",
            "f1Blurb": "Wynik 66 w rundzie finalowej i lacznie -17 daje mu historyczne pierwsze zwyciestwo reprezentanta gospodarzy w PGA Tour."
        },
        "pg": {
            "pinFinal": "GP Meksyku: Wygrana Leclerca, Antonelli na P2 przypieczetowal tytul mistrza swiata 2026.",
            "week1Closed": "NFL Tydzien 8 niedziela: Vikings 24, Colts 17, bilans 7-0. Packers pokonali Panthers w czwartek.",
            "week1Sub": "Darnold 2 TD do Jeffersona. Vikings (7-0) pozostaja jedyna niepokonana ekipa w lidze.",
            "countdownTnf": "Tydzien 8 podsumowanie: Niepokonani Vikings (7-0) ograli Colts 24:17. Packers maja 6-2.",
            "barsPoints": "Antonelli mistrzem z 383 pkt, przewaga 131 pkt nad Russellem na 3 wyscigi przed koncem.",
            "tableAfterMonday": "Premier League 9. kolejka: City na czele z 24 pkt, Arsenal 22, Liverpool i Chelsea po 16.",
            "pinClub": "Wybierz klub. City prowadzi z 24 pkt, Arsenal ma 22, Liverpool i Chelsea po 16.",
            "plFootnote": "PL 9. kolejka: Chelsea 2:1 Newcastle, Arsenal 2:2 Liverpool, Man City 1:0 Southampton.",
            "majorsDone": "VidantaWorld Mexico Open Final: Raul Pereda (-17, 267) zwycieza z przewaga dwoch uderzen."
        }
    },
    "zh": {
        "f1": {
            "tagline": "F1墨西哥大奖赛：安东内利屈居亚军仍提前封王，加冕F1历史上最年轻世界冠军。",
            "liveNow": "墨西哥城正赛终场：勒克莱尔夺冠；安东内利（梅赛德斯）获亚军，提前三站锁定2026年度世界车手总冠军。",
            "pulse": "2026F1世界冠军：基米·安东内利在墨西哥城书写赛车历史新纪录",
            "keywords": "F1, 墨西哥大奖赛, 安东内利, 世界冠军, 勒克莱尔, 梅赛德斯"
        },
        "golf": {
            "tagline": "美巡赛墨西哥公开赛：本土球手佩雷达决赛轮狂飙66杆逆转夺冠，创造历史。",
            "liveNow": "巴亚尔塔港决赛：佩雷达总成绩-17杆（267杆）以两杆优势击败斯莫瑟曼（-15，269）斩获本土历史首冠。",
            "pulse": "美巡赛墨西哥公开赛：本土英雄佩雷达-17杆夺冠引爆全场狂欢",
            "keywords": "美巡赛, 墨西哥公开赛, 佩雷达, 斯莫瑟曼, 巴亚尔塔"
        },
        "football": {
            "tagline": "NFL常规赛第8周：维京人24-17力克小马，开季7战全胜独占联盟榜首。",
            "liveNow": "明尼阿波利斯终场：维京人24-17小马。达诺德274码2达阵连线杰弗森（128码）。明尼苏达以7胜0负保持不败。",
            "pulse": "NFL第8周：明尼苏达维京人击溃小马豪取7连胜领跑全联盟",
            "keywords": "NFL第8周, 维京人, 小马, 达诺德, 杰弗森, 不败战绩"
        },
        "tennis": {
            "tagline": "维也纳ATP500决赛：阿尔卡拉斯6-3、6-4完胜穆塞蒂加冕，整周一盘未丢夺今年第6冠。",
            "liveNow": "维也纳争冠战：阿尔卡拉斯耗时84分钟以6-3、6-4战胜穆塞蒂夺冠，保持整周一盘未失的完美状态捧杯。",
            "pulse": "维也纳ATP500：阿尔卡拉斯直落两盘击败穆塞蒂捧起冠军奖杯",
            "keywords": "ATP, 维也纳, 阿尔卡拉斯, 穆塞蒂, 冠军"
        },
        "basketball": {
            "tagline": "NBA周日焦点战：亚历山大独揽36分9助攻，卫冕冠军雷霆116-109力克快船豪取4连胜。",
            "liveNow": "洛杉矶终场：雷霆116-109快船。亚历山大36分9助攻；霍姆格伦18分4帽。俄克拉荷马城4胜0负领跑西部。",
            "pulse": "NBA周日：亚历山大轰下36分带领不败雷霆力克快船",
            "keywords": "NBA, 雷霆, 快船, 亚历山大, 霍姆格伦, 直觉穹顶"
        },
        "soccer": {
            "tagline": "英超第9轮：帕尔默下半场开局建功，切尔西主场2-1力克纽卡；曼城24分领跑。",
            "liveNow": "英超周日战况：切尔西2-1纽卡斯尔联（杰克逊18'，帕尔默47'；伊萨克32'）。切尔西积16分，曼城积24分居首。",
            "pulse": "英超第9轮：帕尔默制胜球助切尔西2-1拿下纽卡斯尔联",
            "keywords": "英超, 切尔西, 纽卡斯尔联, 帕尔默, 斯坦福桥"
        },
        "home": {
            "tonight": "周日速递",
            "tonightBlurb": "安东内利加冕F1最年轻世界冠军。佩雷达美巡赛本土夺冠创历史。维京人7连胜独步联盟。",
            "plTitle": "F1赛车：安东内利成为历史上最年轻的F1世界总冠军",
            "plBlurb": "梅奔新星在墨西哥城站紧随勒克莱尔收获亚军，年仅20岁便提前锁定2026年度车手世界总冠军。",
            "f1Title": "美巡赛：劳尔·佩雷达在墨西哥公开赛书写本土神话",
            "f1Blurb": "29岁本土名将决赛轮交出66杆总成绩-17杆夺冠，成为美巡赛历史上首位本土问鼎公开赛的墨西哥球员。"
        },
        "pg": {
            "pinFinal": "F1墨西哥大奖赛：勒克莱尔夺冠，安东内利收获亚军提前锁定2026年度世界冠军。",
            "week1Closed": "NFL第8周周日战：维京人24-17胜小马保持7-0全胜。包装工周四27-17胜黑豹。",
            "week1Sub": "达诺德两次连线杰弗森达阵。维京人（7-0）是全联盟唯一未尝败绩的队伍。",
            "countdownTnf": "第8周收官：无败维京人（7-0）24-17拿下小马。包装工战绩升至6-2。",
            "barsPoints": "安东内利积383分提前加冕，在还剩3站比赛时领先拉塞尔（252分）多达131分。",
            "tableAfterMonday": "英超第9轮积分榜：曼城24分领跑，阿森纳22分，利物浦与切尔西同积16分。",
            "pinClub": "选择俱乐部。曼城24分，阿森纳22分，利物浦与切尔西同为16分。",
            "plFootnote": "英超第9轮：切尔西2-1纽卡，阿森纳2-2利物浦，曼城1-0南安普顿。",
            "majorsDone": "墨西哥公开赛决赛轮：佩雷达总成绩-17杆（267杆）两杆优势夺得历史首冠。"
        }
    },
    "ja": {
        "f1": {
            "tagline": "F1メキシコGP：アントネッリが2位に入り、F1史上最年少ワールドチャンピオンに決定。",
            "liveNow": "メキシコシティ決勝：ルクレール優勝；アントネッリ（メルセデス）が2位でフィニッシュし2026年年間王者を確定。",
            "pulse": "2026 F1世界王者：キミ・アントネッリがメキシコでモータースポーツの歴史を塗り替える",
            "keywords": "F1, メキシコGP, アントネッリ, ワールドチャンピオン, ルクレール, メルセデス"
        },
        "golf": {
            "tagline": "メキシコ・オープン：ペレダが66をマークし地元メキシコ勢初のPGAツアー制覇を達成。",
            "liveNow": "ヴィダンタ・バジャルタ最終日：ラウル・ペレダ（-17、267）がスモーザーマン（-15、269）を2打差で破り初優勝。",
            "pulse": "PGAツアー メキシコ・オープン：ラウル・ペレダが通算17アンダーで歴史的ホーム優勝",
            "keywords": "PGAツアー, メキシコ・オープン, ラウル・ペレダ, スモーザーマン, バジャルタ"
        },
        "football": {
            "tagline": "NFL第8週：無敗バイキングスがコルツを24-17で下し、ダーノルドとジェファーソンの活躍で7連勝。",
            "liveNow": "ミネアポリス公式戦：バイキングス 24-17 コルツ。ダーノルド 274ヤード、2TD。バイキングスがリーグ唯一の7勝0敗。",
            "pulse": "NFL第8週：ミネソタ・バイキングスがコルツを破り開幕7連勝無敗を死守",
            "keywords": "NFL第8週, バイキングス, コルツ, ダーノルド, ジェファーソン, 無敗"
        },
        "tennis": {
            "tagline": "エルステ・バンク・オープン決勝：アルカラスがムゼッティを6-3、6-4で破りウィーン制覇。",
            "liveNow": "ウィーン決勝：アルカラスがムゼッティを6-3、6-4（84分）で下す。大会全試合ストレート勝ちで今季6勝目。",
            "pulse": "エルステ・バンク・オープン：アルカラスがムゼッティを下しウィーンタイトル獲得",
            "keywords": "ATP, ウィーン, アルカラス, ムゼッティ, 優勝"
        },
        "basketball": {
            "tagline": "NBA日曜：SGAが36得点をマークし、王者サンダーがクリッパーズを116-109で破り開幕4連勝。",
            "liveNow": "イングルウッド終局：サンダー 116-109 クリッパーズ。ギルジャス・アレクサンダー 36得点9アシスト。サンダーが4勝0敗。",
            "pulse": "NBA日曜：シェイ・ギルジャス・アレクサンダーが無敗サンダーを勝利へ牽引",
            "keywords": "NBA, サンダー, クリッパーズ, ギルジャス・アレクサンダー, インテュイット・ドーム"
        },
        "soccer": {
            "tagline": "プレミアリーグ第9節：コール・パーマーの決勝点でチェルシーがニューカッスルに2-1勝利；マンCが首位。",
            "liveNow": "プレミアリーグ日曜：チェルシー 2-1 ニューカッスル（ジャクソン 18'、パーマー 47'；イサク 32'）。チェルシー勝ち点16。",
            "pulse": "プレミアリーグ第9節：コール・パーマーが輝きチェルシーがニューカッスルを2-1撃破",
            "keywords": "プレミアリーグ, チェルシー, ニューカッスル, パーマー, スタンフォード・ブリッジ"
        },
        "home": {
            "tonight": "日曜版デスク",
            "tonightBlurb": "アントネッリがF1史上最年少王者に戴冠。ペレダがメキシコ・オープンで歴史的快挙。バイキングスが開幕7連勝。",
            "plTitle": "F1：キミ・アントネッリが史上最年少のワールドチャンピオンに輝く",
            "plBlurb": "メルセデスの至宝がメキシコGPでルクレールに続く2位に入り、弱冠20歳で2026年ドライバーズ世界選手権を獲得。",
            "f1Title": "PGAツアー：ラウル・ペレダがヴィダンタで感動の自国オープントロフィーを掲げる",
            "f1Blurb": "最終日に66をマークし通算17アンダーで逆転優勝。PGAツアーのメキシコ・オープンで自国選手初の戴冠を達成。"
        },
        "pg": {
            "pinFinal": "メキシコGP：ルクレール優勝、2位のアントネッリが2026年年間ワールドチャンピオン確定。",
            "week1Closed": "NFL第8週日曜：バイキングスが24-17でコルツを下し7勝0敗。パッカーズは木曜勝利。",
            "week1Sub": "ダーノルドからジェファーソンへ2本のTDパス。バイキングスが唯一の無敗チーム。",
            "countdownTnf": "第8週総括：無敗のバイキングス（7-0）がコルツを撃破。パッカーズは6勝2敗。",
            "barsPoints": "アントネッリが383ポイントで戴冠。ラッセル（252）に残り3戦で131点差をつけ確定。",
            "tableAfterMonday": "プレミアリーグ順位表：マンCが勝ち点24で首位、アーセナル22点、リヴァプールとチェルシー16点。",
            "pinClub": "クラブを選択。マンCが24点で首位、アーセナル22点、リヴァプールとチェルシーが16点。",
            "plFootnote": "PL第9節：チェルシー 2-1 ニューカッスル、アーセナル 2-2 リヴァプール、マンC 1-0 サウサンプトン。",
            "majorsDone": "メキシコ・オープン最終日：ペレダ（-17、267）が2打差で歴史的ツアー初優勝。"
        }
    },
    "ko": {
        "f1": {
            "tagline": "F1 멕시코 GP: 키미 안토넬리 2위 완주로 역대 최연소 F1 월드 챔피언 등극.",
            "liveNow": "멕시코시티 결선: 샤를 르클레르 우승; 키미 안토넬리(메르세데스) 2위로 2026년 세계 챔피언 확정.",
            "pulse": "2026 F1 월드 챔피언: 키미 안토넬리 멕시코서 모터스포츠 역사 새로 쓰다",
            "keywords": "F1, 멕시코 GP, 안토넬리, 월드 챔피언, 르클레르, 메르세데스"
        },
        "golf": {
            "tagline": "멕시코 오픈: 라울 페레다 최종일 66타 대역전승, 멕시코인 최초 홈 우승 달성.",
            "liveNow": "바야르타 최종 라운드: 라울 페레다(-17, 267)가 오스틴 스모더먼(-15, 269)을 2타 차로 제치고 역사적 첫 승.",
            "pulse": "PGA 투어 멕시코 오픈: 라울 페레다 자국서 17언더파 역사적 우승 트로피",
            "keywords": "PGA 투어, 멕시코 오픈, 라울 페레다, 스모더먼, 바야르타"
        },
        "football": {
            "tagline": "NFL 8주차: 무패 바이킹스, 콜츠 24-17 꺾고 다놀드와 제퍼슨 활약 앞세워 개막 7연승 질주.",
            "liveNow": "미네아폴리스 경기 결과: 바이킹스 24-17 콜츠. 다놀드 274야드 2TD(제퍼슨 128야드). 미네소타 단독 7-0 무패.",
            "pulse": "NFL 8주차: 미네소타 바이킹스 콜츠 꺾고 7승 무패 단독 선두 행진",
            "keywords": "NFL 8주차, 미네소타 바이킹스, 콜츠, 다놀드, 제퍼슨, 무패"
        },
        "tennis": {
            "tagline": "빈 오픈 결승: 카를로스 알카라스, 무세티 6-3 6-4 완파하고 무실세트 우승 달성.",
            "liveNow": "빈 오픈 결승: 알카라스 무세티를 6-3, 6-4(84분)로 제압. 대회 내내 무실세트로 시즌 6번째 타이틀 획득.",
            "pulse": "빈 오픈 테니스: 알카라스 무세티 꺾고 무실세트 퍼펙트 우승",
            "keywords": "ATP, 빈 오픈, 알카라스, 무세티, 우승"
        },
        "basketball": {
            "tagline": "NBA 일요일: SGA 36점 폭발, 디펜딩 챔피언 썬더 클리퍼스 116-109 꺾고 개막 4연승.",
            "liveNow": "잉글우드 경기 결과: 썬더 116-109 클리퍼스. 길저스-알렉산더 36점 9어시스트. 오클라호마시티 4승 0패 질주.",
            "pulse": "NBA 일요일: 샤이 길저스-알렉산더 36점 앞세워 무패 썬더 클리퍼스 격파",
            "keywords": "NBA, 썬더, 클리퍼스, 길저스-알렉산더, 인튜이트 돔"
        },
        "soccer": {
            "tagline": "프리미어리그 9R: 콜 파머 결승골 작렬, 첼시 뉴캐슬 2-1 제압; 맨시티 승점 24점 선두.",
            "liveNow": "프리미어리그 일요일: 첼시 2-1 뉴캐슬 (잭슨 18', 파머 47'; 이삭 32'). 첼시 승점 16점. 맨시티 승점 24점 1위.",
            "pulse": "프리미어리그 9R: 콜 파머 결승골로 첼시 뉴캐슬 2-1 격파",
            "keywords": "프리미어리그, 첼시, 뉴캐슬, 콜 파머, 스탬퍼드 브리지"
        },
        "home": {
            "tonight": "일요일 데스크",
            "tonightBlurb": "안토넬리 최연소 F1 챔피언 등극. 페레다 멕시코 오픈 홈 첫 우승. 바이킹스 7연승 무패 질주.",
            "plTitle": "F1 레이싱: 키미 안토넬리 역대 최연소 월드 챔피언 등극",
            "plBlurb": "메르세데스 신예가 멕시코 GP서 르클레르에 이어 2위를 차지하며 20세 나이로 2026 세계 챔피언을 확정지었습니다.",
            "f1Title": "PGA 투어: 라울 페레다 멕시코 오픈서 감격의 첫 승 달성",
            "f1Blurb": "최종 라운드 66타로 합계 17언더파를 작성하며 PGA 투어 멕시코 오픈 사상 최초로 자국 선수가 우승을 거머쥐었습니다."
        },
        "pg": {
            "pinFinal": "멕시코 GP: 르클레르 우승, 2위 안토넬리가 2026 F1 월드 챔피언 확정.",
            "week1Closed": "NFL 8주차 일요일: 바이킹스 24-17 콜츠 꺾고 7연승. 패커스는 목요일 승리.",
            "week1Sub": "다놀드 2TD 패스 제퍼슨 연결. 바이킹스(7-0)가 NFL 유일의 무패 팀.",
            "countdownTnf": "8주차 결산: 무패 바이킹스(7-0) 콜츠 제압. 패커스는 6승 2패.",
            "barsPoints": "안토넬리 383점으로 챔피언 등극. 3경기 남겨두고 러셀(252)에 131점 차 리드.",
            "tableAfterMonday": "프리미어리그 9R 순위표: 맨시티 승점 24점 1위, 아스널 22점, 리버풀과 첼시 16점.",
            "pinClub": "클럽 선택. 맨시티 승점 24점, 아스널 22점, 리버풀과 첼시 각 16점.",
            "plFootnote": "PL 9R: 첼시 2-1 뉴캐슬, 아스널 2-2 리버풀, 맨시티 1-0 사우샘프턴.",
            "majorsDone": "멕시코 오픈 최종일: 페레다(-17, 267) 2타 차 역사적 첫 우승 달성."
        }
    },
    "ar": {
        "f1": {
            "tagline": "جائزة المكسيك الكبرى: كيمي أنتونيللي ينهي السباق ثانيا خلف لوكلير ويصبح أصغر بطل عالم في تاريخ الفورمولا 1.",
            "liveNow": "سباق المكسيك: شارل لوكلير يفوز؛ كيمي أنتونيللي (مرسيدس) يحرز المركز الثاني ويحسم لقب بطولة العالم 2026 رسميا.",
            "pulse": "بطل العالم 2026: كيمي أنتونيللي يصنع التاريخ في المكسيك ويصبح الأصغر تتويجا",
            "keywords": "فورمولا 1, جائزة المكسيك الكبرى, أنتونيللي, بطل العالم, لوكلير, مرسيدس"
        },
        "golf": {
            "tagline": "بطولة المكسيك المفتوحة: راؤول بيريدا يسجل 66 ضربة ويصبح أول مكسيكي يتوج باللقب على أرضه.",
            "liveNow": "نهائي فيدانتا فايارتا: راؤول بيريدا (-17، 267) يتفوق بضربتين على أوستن سموذر مان (-15، 269) في انتصار تاريخي.",
            "pulse": "جولة بي جي إيه: راؤول بيريدا يحقق فوزا تاريخيا في بطولة المكسيك المفتوحة بـ -17",
            "keywords": "جولف, بطولة المكسيك المفتوحة, راؤول بيريدا, سموذر مان, فيدانتا فايارتا"
        },
        "football": {
            "tagline": "دوري NFL الأسبوع 8: فايكنغز يواصل انطلاقته الخالية من الهزائم (7-0) بعد الفوز 24-17 على كولتس.",
            "liveNow": "النهائي في مينيابوليس: فايكنغز 24، كولتس 17. دارنولد 274 ياردة وتمريرتا هبوط لجيفرسون. مينيسوتا الوحيد بسجل 7-0.",
            "pulse": "دوري NFL: مينيسوتا فايكنغز يحافظ على علامته الكاملة (7-0) بعد إسقاط كولتس",
            "keywords": "دوري NFL, مينيسوتا فايكنغز, كولتس, دارنولد, جيفرسون, دون هزيمة"
        },
        "tennis": {
            "tagline": "بطولة فيينا للتنس النهائي: كارلوس ألكاراز يهزم لورينزو موسيتي 6-3 و6-4 ويتوج باللقب.",
            "liveNow": "نهائي فيينا: ألكاراز يهزم موسيتي 6-3 و6-4 في 84 دقيقة. لقبه السادس في 2026 دون خسارة أي مجموعة طوال الأسبوع.",
            "pulse": "بطولة فيينا المفتوحة: كارلوس ألكاراز يتفوق على موسيتي ويحصد الكأس",
            "keywords": "تنس, فيينا, ألكاراز, موسيتي, بطل"
        },
        "basketball": {
            "tagline": "دوري السلة الأمريكي الأحد: شاي غيلجيوس-ألكسندر يسجل 36 نقطة وثاندر البطل يهزم كليبرز 116-109.",
            "liveNow": "النهائي في لوس أنجلوس: ثاندر 116، كليبرز 109. غيلجيوس-ألكسندر 36 نقطة و9 تمريرات. أوكلاهوما سيتي يرتفع إلى 4-0.",
            "pulse": "دوري السلة الأمريكي: شاي غيلجيوس-ألكسندر يقود ثاندر حامل اللقب للفوز على كليبرز",
            "keywords": "دوري السلة الأمريكي, ثاندر, كليبرز, غيلجيوس-ألكسندر, إنتويت دوم"
        },
        "soccer": {
            "tagline": "الدوري الإنجليزي الجولة 9: كول بالمر يسجل هدف الفوز لتشيلسي 2-1 أمام نيوكاسل؛ وسيتي يتصدر بـ 24 نقطة.",
            "liveNow": "الدوري الإنجليزي الأحد: تشيلسي 2-1 نيوكاسل (جاكسون 18'، بالمر 47'؛ إيساك 32'). تشيلسي يبلغ 16 نقطة وسيتي يتصدر بـ 24.",
            "pulse": "الدوري الإنجليزي: كول بالمر يحسم مواجهة تشيلسي أمام نيوكاسل يونايتد (2-1)",
            "keywords": "الدوري الإنجليزي, تشيلسي, نيوكاسل, كول بالمر, ستامفورد بريدج"
        },
        "home": {
            "tonight": "موجز الأحد",
            "tonightBlurb": "أنتونيللي أصغر بطل عالم في تاريخ الفورمولا 1. بيريدا يحقق إنجازا تاريخيا في بطولة المكسيك. فايكنغز يبلغ 7-0.",
            "plTitle": "فورمولا 1: كيمي أنتونيللي يصبح أصغر بطل عالم في تاريخ الرياضة",
            "plBlurb": "سائق مرسيدس الإيطالي ينهي سباق المكسيك في المركز الثاني خلف لوكلير ويحسم لقب بطولة العالم 2026 بعمر 20 عاما.",
            "f1Title": "جولة بي جي إيه: راؤول بيريدا يحقق لقبا أسطوريا في بطولة المكسيك المفتوحة",
            "f1Blurb": "البطل المكسيكي يسجل 66 ضربة في الجولة الختامية لينهي المنافسات بـ 17 تحت المعدل ويتوج بلقب تاريخي على أرضه."
        },
        "pg": {
            "pinFinal": "جائزة المكسيك: لوكلير يفوز وأنتونيللي ينهي ثانيا ليضمن لقب بطولة العالم 2026 رسميا.",
            "week1Closed": "دوري NFL الأحد: فايكنغز 24، كولتس 17 ليواصل سجله المثالي 7-0. باكرز فاز يوم الخميس.",
            "week1Sub": "دارنولد يمرر هبوطين لجيفرسون. فايكنغز (7-0) هو الفريق الوحيد دون هزيمة في الدوري.",
            "countdownTnf": "حصاد الأسبوع 8: فايكنغز المثالي (7-0) يهزم كولتس 24-17. باكرز بسجل 6-2.",
            "barsPoints": "أنتونيللي يتوج باللقب بـ 383 نقطة بفارق 131 نقطة عن راسل قبل 3 جولات من النهاية.",
            "tableAfterMonday": "ترتيب الدوري الإنجليزي الجولة 9: سيتي في الصدارة بـ 24 نقطة، أرسنال 22، ليفربول وتشيلسي 16.",
            "pinClub": "اختر ناديا. سيتي يتصدر بـ 24، أرسنال 22، ليفربول وتشيلسي بـ 16 نقطة.",
            "plFootnote": "الدوري الإنجليزي: تشيلسي 2-1 نيوكاسل، أرسنال 2-2 ليفربول، مان سيتي 1-0 ساوثهامبتون.",
            "majorsDone": "نهائي بطولة المكسيك للجولف: بيريدا (-17، 267) يتوج باللقب التاريخي بفارق ضربتين."
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

print("All locale updates for 1 Nov 2026 completed successfully!")
