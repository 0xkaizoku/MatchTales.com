# -*- coding: utf-8 -*-
import re
import os

DATA = {
    "en": {
        "soccer": {
            "tagline": "Carabao Cup round 4: Man City edge Brighton 2-1 and Liverpool down Chelsea 2-0 to book quarter-final spots.",
            "liveNow": "Quarter-final draw today: Man City and Liverpool advance alongside Fleetwood Town. Premier League returns Saturday.",
            "pulse": "CARABAO CUP QUARTER-FINAL DRAW: GIANTS JOIN FLEETWOOD TOWN IN HAT",
            "keywords": "Carabao Cup, Man City, Liverpool, Fleetwood Town, quarter-final draw, Haaland, Gakpo"
        },
        "basketball": {
            "tagline": "WNBA Finals Game 6 tonight: Valkyries (3-2) seek historic maiden title as Thunder open NBA defense with win.",
            "liveNow": "WNBA Finals Game 6 tonight in Atlanta: Valkyries lead 3-2. NBA: Thunder 122, Nuggets 108 (SGA 34 pts); Spurs 130, Kings 103 (Wemby 29 pts).",
            "pulse": "WNBA FINALS GAME 6: VALKYRIES ON BRINK OF CHAMPIONSHIP DESTINY",
            "keywords": "WNBA Finals, Game 6, Valkyries, Dream, Angel Reese, NBA opening week, SGA, Thunder"
        },
        "football": {
            "tagline": "NFL Week 8 kickoff tonight: Packers host Panthers at Lambeau Field as NFC North race intensifies.",
            "liveNow": "TNF tonight: Panthers (3-4) at Packers (5-2) on Prime Video. Minnesota Vikings (6-0) stand as lone unbeaten team.",
            "pulse": "THURSDAY NIGHT FOOTBALL: PACKERS HOST PANTHERS UNDER LAMBEAU LIGHTS",
            "keywords": "NFL Week 8, TNF, Packers, Panthers, Jordan Love, Bryce Young, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Vienna Round of 16: Alcaraz sweeps Berrettini 6-3, 6-4 while Zverev downs Giron to reach quarter-finals.",
            "liveNow": "Erste Bank Open R16: Alcaraz def. Berrettini 6-3, 6-4 (28 winners, 0 break points faced). Zverev def. Giron 6-2, 7-5 into Friday quarters.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ AND ZVEREV CRUISE INTO VIENNA QUARTER-FINALS",
            "keywords": "ATP, Vienna, Erste Bank Open, Alcaraz, Berrettini, Zverev, Giron, quarter-finals"
        },
        "f1": {
            "tagline": "Mexico City GP media day: Antonelli confirms car #12 for 2027 needing only P9 on Sunday to seal title.",
            "liveNow": "Press day at Hermanos Rodriguez: Antonelli (365 pts) confirms car #12. Ninth-place finish in Mexico guarantees 2026 World Championship.",
            "pulse": "MEXICO CITY GP: ANTONELLI CONFIRMS NUMBER 12 ON BRINK OF CROWN",
            "keywords": "Formula 1, Mexico City GP, Antonelli, car 12, Russell, World Champion, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open round 1: Raul Pereda leads with 65 as Bermuda winner Smotherman opens with 66.",
            "liveNow": "VidantaVallarta Round 1: Raul Pereda (-6, 65) leads by one over Austin Smotherman (-5, 66) and Aaron Rai (-5, 66). Grillo at -4.",
            "pulse": "PGA TOUR MEXICO OPEN: PEREDA LEADS AS SMOTHERMAN FIRES 66",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Pereda, Smotherman, Rai, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Thursday desk",
            "tonightBlurb": "WNBA Finals Game 6 in Atlanta. Packers host Panthers on TNF. Man City and Liverpool advance in Carabao Cup.",
            "plTitle": "Carabao Cup round 4: Man City and Liverpool book quarter-final spots",
            "plBlurb": "City edge Brighton 2-1 and Liverpool down Chelsea 2-0 to join fourth-tier Cinderella Fleetwood Town in the last eight.",
            "f1Title": "Mexico City GP: Antonelli confirms car 12 on brink of historic coronation",
            "f1Blurb": "Facing media in Mexico City, Kimi Antonelli needs just ninth place on Sunday to become Formula 1's youngest world champion."
        },
        "pg": {
            "pinFinal": "Carabao Cup round 4: Man City edge Brighton 2-1 and Liverpool defeat Chelsea 2-0 to join Fleetwood Town in quarter-finals.",
            "week1Closed": "NFL Week 8 TNF: Packers host Panthers at Lambeau Field under prime-time lights",
            "week1Sub": "Jordan Love (14 TD) leads 5-2 Green Bay against Bryce Young and 3-4 Carolina. Vikings (6-0) stand as lone unbeaten.",
            "countdownTnf": "TNF tonight: Panthers (3-4) at Packers (5-2). Jordan Love tests Carolina pass defense. Vikings stand 6-0.",
            "barsPoints": "Bars show the gap to the leader. Antonelli has 365, 123 ahead of Russell on 242. P9 in Mexico clinches maiden title.",
            "tableAfterMonday": "Premier League: City and Arsenal tied on 21 (7-0-1). Liverpool 15, Chelsea 13. Carabao Cup: Man City and Liverpool advance.",
            "pinClub": "Select a club. City and Arsenal lead table on 21. Man City, Liverpool, and Fleetwood Town reach Carabao Cup quarter-finals.",
            "plFootnote": "Wednesday cup: Man City 2-1 Brighton, Liverpool 2-0 Chelsea. Tuesday: Fleetwood Town 1-1 Arsenal (5-3 pens). Quarter-final draw today.",
            "majorsDone": "VidantaWorld Mexico Open round 1: Raul Pereda fires 65 to lead; Bermuda winner Smotherman opens with 5-under 66.",
            "wnbaFirstRound": "WNBA Finals Game 6 tonight: Valkyries (3-2) can clinch historic inaugural title at Dream in Atlanta.",
            "bracketFootnote": "Game 1: Valkyries 68-64. Game 2: Dream 79-65. Game 3: Dream 97-71. Game 4: Valkyries 67-62. Game 5: Valkyries 64-55. Game 6 tonight in Atlanta."
        }
    },
    "fr": {
        "soccer": {
            "tagline": "Carabao Cup 4e tour : Man City ecarte Brighton 2-1 et Liverpool domine Chelsea 2-0 pour rallier les quarts.",
            "liveNow": "Tirage au sort aujourd'hui : Man City et Liverpool rejoignent Fleetwood Town. La Premier League reprend samedi.",
            "pulse": "TIRAGE COUPE DE LA LIGUE : LES CADORS REJOIGNENT FLEETWOOD TOWN",
            "keywords": "Carabao Cup, Man City, Liverpool, Fleetwood Town, tirage quarts, Haaland, Gakpo"
        },
        "basketball": {
            "tagline": "Finales WNBA match 6 ce soir : Les Valkyries (3-2) visent le titre ; le Thunder reussit sa reprise NBA.",
            "liveNow": "Match 6 ce soir a Atlanta : Golden State mene 3-2. NBA : Thunder 122, Nuggets 108 (SGA 34 pts) ; Spurs 130, Kings 103 (Wemby 29 pts).",
            "pulse": "FINALES WNBA MATCH 6 : LES VALKYRIES AUX PORTES DE L'HISTOIRE",
            "keywords": "Finales WNBA, match 6, Valkyries, Dream, Angel Reese, reprise NBA, SGA, Thunder"
        },
        "football": {
            "tagline": "Coup d'envoi Semaine 8 NFL : Les Packers accueillent Carolina a Lambeau Field sous tension en NFC Nord.",
            "liveNow": "TNF ce soir : Panthers (3-4) chez les Packers (5-2) sur Prime Video. Minnesota Vikings (6-0) restent seuls invaincus.",
            "pulse": "THURSDAY NIGHT FOOTBALL : LES PACKERS RECOIVENT LES PANTHERS A LAMBEAU",
            "keywords": "NFL semaine 8, TNF, Packers, Panthers, Jordan Love, Bryce Young, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Vienne 8es de finale : Alcaraz ecarte Berrettini 6-3, 6-4, Zverev domine Giron pour aller en quarts.",
            "liveNow": "Erste Bank Open 8es : Alcaraz bat Berrettini 6-3, 6-4 (28 coups gagnants, 0 balle de break concedee). Zverev domine Giron 6-2, 7-5.",
            "pulse": "ERSTE BANK OPEN : ALCARAZ ET ZVEREV EN QUARTS DE FINALE A VIENNE",
            "keywords": "ATP, Vienne, Erste Bank Open, Alcaraz, Berrettini, Zverev, Giron, quarts de finale"
        },
        "f1": {
            "tagline": "GP du Mexique journee presse : Antonelli confirme le numero 12 pour 2027, la 9e place suffira dimanche.",
            "liveNow": "Presse a Mexico : Antonelli (365 pts) conserve le #12. Une 9e place dimanche garantit le titre mondial 2026.",
            "pulse": "GP DU MEXIQUE : ANTONELLI CONFIRME LE 12 AVANT SA COURONNE",
            "keywords": "Formule 1, GP du Mexique, Antonelli, numero 12, Russell, champion du monde, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open T1 : Raul Pereda brille avec un 65, Smotherman ouvre avec un solide 66.",
            "liveNow": "VidantaVallarta 1er tour : Raul Pereda (-6, 65) mene d'un coup devant Austin Smotherman (-5, 66) et Aaron Rai (-5, 66).",
            "pulse": "PGA TOUR MEXICO OPEN : PEREDA EN TETE, SMOTHERMAN SIGNE UN 66",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Pereda, Smotherman, Rai, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Bureau du jeudi",
            "tonightBlurb": "Finales WNBA match 6 a Atlanta. Les Packers recoivent Carolina au TNF. Man City et Liverpool filent en quarts de coupe.",
            "plTitle": "Carabao Cup 4e tour : Man City et Liverpool valident leur billet pour les quarts",
            "plBlurb": "City domine Brighton 2-1 et Liverpool ecarte Chelsea 2-0 pour rejoindre le club feerique de Fleetwood Town en quarts.",
            "f1Title": "GP du Mexique : Antonelli confirme le numero 12 a l'aube d'un sacre historique",
            "f1Blurb": "Devant la presse a Mexico, Kimi Antonelli n'a besoin que d'une 9e place dimanche pour devenir le plus jeune champion du monde."
        },
        "pg": {
            "pinFinal": "Coupe de la Ligue 4e tour : Man City bat Brighton 2-1 et Liverpool sort Chelsea 2-0 pour rejoindre Fleetwood Town.",
            "week1Closed": "NFL Semaine 8 TNF : Les Packers recoivent les Panthers a Lambeau Field sous les projecteurs",
            "week1Sub": "Jordan Love (14 TD) mene Green Bay (5-2) face a Bryce Young et Carolina (3-4). Vikings (6-0) seuls invaincus.",
            "countdownTnf": "TNF ce soir : Panthers (3-4) chez les Packers (5-2). Jordan Love teste la defense des Panthers. Vikings a 6-0.",
            "barsPoints": "L'ecart avec le leader : Antonelli a 365 pts, 123 d'avance sur Russell (242). La 9e place au Mexique scelle le titre.",
            "tableAfterMonday": "Premier League : City et Arsenal a 21 pts (7-0-1). Liverpool 15, Chelsea 13. Coupe : City et Liverpool qualifies.",
            "pinClub": "Selectionnez un club. City et Arsenal en tete a 21. Man City, Liverpool et Fleetwood Town en quarts de coupe.",
            "plFootnote": "Mercredi : Man City 2-1 Brighton, Liverpool 2-0 Chelsea. Mardi : Fleetwood Town 1-1 Arsenal (tab 5-3). Tirage au sort aujourd'hui.",
            "majorsDone": "VidantaWorld Mexico Open T1 : Raul Pereda en tete a 65 ; Austin Smotherman en embuscade a 5 sous le par (66).",
            "wnbaFirstRound": "Finales WNBA match 6 ce soir : Les Valkyries (3-2) peuvent s'offrir un titre historique a Atlanta.",
            "bracketFootnote": "Match 1: Valkyries 68-64. Match 2: Dream 79-65. Match 3: Dream 97-71. Match 4: Valkyries 67-62. Match 5: Valkyries 64-55. Match 6 ce soir a Atlanta."
        }
    },
    "es": {
        "soccer": {
            "tagline": "Copa de la Liga ronda 4: Man City bate 2-1 a Brighton y Liverpool supera 2-0 a Chelsea para sellar cuartos.",
            "liveNow": "Sorteo de cuartos hoy: Man City y Liverpool avanzan junto al sorprendente Fleetwood Town. Premier League vuelve el sabado.",
            "pulse": "SORTEO COPA DE LA LIGA: LOS GIGANTES SE UNEN A FLEETWOOD TOWN",
            "keywords": "Carabao Cup, Man City, Liverpool, Fleetwood Town, sorteo cuartos, Haaland, Gakpo"
        },
        "basketball": {
            "tagline": "Partido 6 Finales WNBA hoy: Valkyries (3-2) buscan la gloria; Thunder arranca defensa de titulo NBA con triunfo.",
            "liveNow": "Partido 6 hoy en Atlanta: Valkyries lideran 3-2. NBA: Thunder 122, Nuggets 108 (SGA 34 pts); Spurs 130, Kings 103 (Wemby 29 pts).",
            "pulse": "FINALES WNBA PARTIDO 6: VALKYRIES A UN PASO DEL ANILLO HISTORICO",
            "keywords": "WNBA Finals, Partido 6, Valkyries, Dream, Angel Reese, apertura NBA, SGA, Thunder"
        },
        "football": {
            "tagline": "Semana 8 de la NFL arranca hoy: Packers reciben a Panthers en Lambeau Field en duelo clave de NFC Norte.",
            "liveNow": "TNF hoy: Panthers (3-4) en casa de Packers (5-2) en Prime Video. Minnesota Vikings (6-0) siguen invictos.",
            "pulse": "THURSDAY NIGHT FOOTBALL: PACKERS RECIBEN A PANTHERS EN LAMBEAU FIELD",
            "keywords": "NFL Semana 8, TNF, Packers, Panthers, Jordan Love, Bryce Young, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Viena octavos: Alcaraz arrolla a Berrettini 6-3, 6-4 y Zverev doblega a Giron para acceder a cuartos de final.",
            "liveNow": "Erste Bank Open R16: Alcaraz vence a Berrettini 6-3, 6-4 (28 golpes ganadores, 0 bolas de break cedidas). Zverev a cuartos.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ Y ZVEREV ACCEDEN A CUARTOS EN VIENA",
            "keywords": "ATP, Viena, Erste Bank Open, Alcaraz, Berrettini, Zverev, Giron, cuartos de final"
        },
        "f1": {
            "tagline": "GP de Mexico dia de medios: Antonelli confirma dorsal 12 para 2027 a un paso de coronarse con P9 el domingo.",
            "liveNow": "Rueda de prensa en Mexico: Antonelli (365 pts) mantendra el #12. Un noveno puesto en carrera garantiza el campeonato mundial.",
            "pulse": "GP DE MEXICO: ANTONELLI CONFIRMA EL 12 ANTES DE SU CORONACION",
            "keywords": "Formula 1, GP de Mexico, Antonelli, dorsal 12, Russell, campeon del mundo, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R1: Raul Pereda deleita con 65 y Smotherman brilla con 66 golpes.",
            "liveNow": "VidantaVallarta Ronda 1: Raul Pereda (-6, 65) lidera por un golpe sobre Austin Smotherman (-5, 66) y Aaron Rai (-5, 66).",
            "pulse": "PGA TOUR MEXICO OPEN: PEREDA LIDERA Y SMOTHERMAN FIRMA UN 66",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Pereda, Smotherman, Rai, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Mesa del jueves",
            "tonightBlurb": "Finales WNBA Partido 6 en Atlanta. Packers reciben a Panthers en TNF. Man City y Liverpool avanzan en Carabao Cup.",
            "plTitle": "Copa de la Liga ronda 4: Man City y Liverpool sellan sus boletos a cuartos",
            "plBlurb": "City vence a Brighton 2-1 y Liverpool supera 2-0 a Chelsea para acompanar al modesto Fleetwood Town en cuartos de final.",
            "f1Title": "GP de Mexico: Antonelli confirma el numero 12 al borde de una coronacion historica",
            "f1Blurb": "Ante la prensa en Mexico, Kimi Antonelli solo necesita un noveno lugar el domingo para ser el campeon mundial mas joven."
        },
        "pg": {
            "pinFinal": "Copa de la Liga ronda 4: Man City derrota 2-1 a Brighton y Liverpool supera 2-0 a Chelsea rumbo a cuartos de final.",
            "week1Closed": "NFL Semana 8 TNF: Packers reciben a Panthers bajo los focos de Lambeau Field",
            "week1Sub": "Jordan Love (14 TD) lidera a Green Bay (5-2) frente a Bryce Young y Carolina (3-4). Vikings (6-0) unicos invictos.",
            "countdownTnf": "TNF hoy: Panthers (3-4) en Packers (5-2). Jordan Love desafia a la secundaria de Carolina. Vikings con 6-0.",
            "barsPoints": "Barras muestran distancia al lider. Antonelli suma 365, 123 mas que Russell (242). P9 en Mexico asegura el titulo.",
            "tableAfterMonday": "Premier League: City y Arsenal empatados en 21 (7-0-1). Liverpool 15, Chelsea 13. Copa: City y Liverpool en cuartos.",
            "pinClub": "Selecciona un club. City y Arsenal mandan con 21. Man City, Liverpool y Fleetwood Town en cuartos de copa.",
            "plFootnote": "Miercoles copa: Man City 2-1 Brighton, Liverpool 2-0 Chelsea. Martes: Fleetwood Town 1-1 Arsenal (pen 5-3). Sorteo de cuartos hoy.",
            "majorsDone": "VidantaWorld Mexico Open R1: Raul Pereda lidera con 65; Austin Smotherman acecha a un golpe tras abrir con 66.",
            "wnbaFirstRound": "Partido 6 Finales WNBA hoy: Valkyries (3-2) pueden sellar su historico primer titulo en casa de Atlanta.",
            "bracketFootnote": "Partido 1: Valkyries 68-64. Partido 2: Dream 79-65. Partido 3: Dream 97-71. Partido 4: Valkyries 67-62. Partido 5: Valkyries 64-55. Partido 6 hoy en Atlanta."
        }
    },
    "de": {
        "soccer": {
            "tagline": "Carabao Cup Achtelfinale: Man City schlaegt Brighton 2:1, Liverpool bezwingt Chelsea 2:0 auf dem Weg ins Viertelfinale.",
            "liveNow": "Viertelfinal-Auslosung heute: Man City und Liverpool folgen Sensationsteam Fleetwood Town. Premier League am Samstag.",
            "pulse": "LIGAPOKAL-AUSLOSUNG: SCHWERGEWICHTE FOLGEN FLEETWOOD TOWN IN DEN TOPF",
            "keywords": "Carabao Cup, Man City, Liverpool, Fleetwood Town, Auslosung Viertelfinale, Haaland, Gakpo"
        },
        "basketball": {
            "tagline": "WNBA Finals Spiel 6 heute: Valkyries (3:2) greifen nach historischem Titel; Thunder starten NBA-Saison mit Sieg.",
            "liveNow": "Spiel 6 heute in Atlanta: Golden State fuehrt 3:2. NBA: Thunder 122, Nuggets 108 (SGA 34 Pkt); Spurs 130, Kings 103 (Wemby 29 Pkt).",
            "pulse": "WNBA FINALS SPIEL 6: VALKYRIES VOR HISTORISCHER PREMIEREN-KROENUNG",
            "keywords": "WNBA Finals, Spiel 6, Valkyries, Dream, Angel Reese, NBA-Saisonstart, SGA, Thunder"
        },
        "football": {
            "tagline": "NFL Woche 8 startet heute: Packers empfangen Panthers im Lambeau Field im brisanten NFC-Duell.",
            "liveNow": "TNF heute Nacht: Panthers (3-4) bei den Packers (5-2) auf Prime Video. Minnesota Vikings (6-0) bleiben ungeschlagen.",
            "pulse": "THURSDAY NIGHT FOOTBALL: PACKERS EMPFANGEN PANTHERS IM LAMBEAU FIELD",
            "keywords": "NFL Woche 8, TNF, Packers, Panthers, Jordan Love, Bryce Young, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Wien Achtelfinale: Alcaraz schlaegt Berrettini 6:3, 6:4, Zverev bezwingt Giron und zieht ins Viertelfinale ein.",
            "liveNow": "Erste Bank Open AF: Alcaraz besiegt Berrettini 6:3, 6:4 (28 Winner, kein Breakball zugelassen). Zverev schlaegt Giron 6:2, 7:5.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ UND ZVEREV ZIEHEN SOUVERAEN INS VIERTELFINALE EIN",
            "keywords": "ATP, Wien, Erste Bank Open, Alcaraz, Berrettini, Zverev, Giron, Viertelfinale"
        },
        "f1": {
            "tagline": "GP Mexiko Medientag: Antonelli bestaetigt Startnummer 12 fuer 2027 vor moeglicher WM-Kroenung am Sonntag.",
            "liveNow": "Pressekonferenz in Mexiko: Antonelli (365 Pkt) bleibt bei #12. Platz 9 am Sonntag reicht zum juengsten WM-Titel aller Zeiten.",
            "pulse": "GP MEXIKO: ANTONELLI BESTAETIGT NUMMER 12 VOR HISTORISCHEM TITEL",
            "keywords": "Formel 1, GP Mexiko, Antonelli, Nummer 12, Russell, Weltmeister, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R1: Raul Pereda begeistert mit 65, Smotherman glaenzt mit 66 Schlaegen.",
            "liveNow": "VidantaVallarta Runde 1: Raul Pereda (-6, 65) fuehrt mit einem Schlag vor Austin Smotherman (-5, 66) und Aaron Rai (-5, 66).",
            "pulse": "PGA TOUR MEXICO OPEN: PEREDA FUEHRT, SMOTHERMAN SCHLAEGT EINE 66",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Pereda, Smotherman, Rai, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Donnerstags-Redaktion",
            "tonightBlurb": "WNBA Finals Spiel 6 in Atlanta. Packers fordern Panthers im TNF. Man City und Liverpool erreichen Pokal-Viertelfinale.",
            "plTitle": "Carabao Cup Achtelfinale: Man City und Liverpool buchen Viertelfinal-Tickets",
            "plBlurb": "City bezwingt Brighton 2:1 und Liverpool schlaegt Chelsea 2:0; beide folgen Viertligist Fleetwood Town in die Runde der letzten Acht.",
            "f1Title": "GP Mexiko: Antonelli bestaetigt Startnummer 12 kurz vor historischer WM-Kroenung",
            "f1Blurb": "Vor den Medien in Mexiko-Stadt benoetigt Kimi Antonelli am Sonntag lediglich Rang neun, um juengster Formel-1-Weltmeister zu werden."
        },
        "pg": {
            "pinFinal": "Ligapokal Achtelfinale: Man City besiegt Brighton 2:1 und Liverpool wirft Chelsea 2:0 aus dem Wettbewerb.",
            "week1Closed": "NFL Woche 8 TNF: Packers empfangen Panthers im frostigen Lambeau Field unter Flutlicht",
            "week1Sub": "Jordan Love (14 TD) fuehrt Green Bay (5-2) gegen Bryce Young und Carolina (3-4). Vikings (6-0) allein unbesiegt.",
            "countdownTnf": "TNF heute: Panthers (3-4) bei Packers (5-2). Jordan Love fordert Carolinas Defensive. Vikings stehen bei 6-0.",
            "barsPoints": "Balken zeigen Abstand zum Führenden. Antonelli hat 365 Pkt, 123 vor Russell (242). P9 in Mexiko genuegt zum Titel.",
            "tableAfterMonday": "Premier League: City und Arsenal punktgleich auf 21 (7-0-1). Liverpool 15, Chelsea 13. Pokal: City und Liverpool weiter.",
            "pinClub": "Waehlen Sie einen Klub. City und Arsenal fuehren mit 21. City, Liverpool und Fleetwood Town im Viertelfinale.",
            "plFootnote": "Mittwoch Pokal: Man City 2:1 Brighton, Liverpool 2:0 Chelsea. Dienstag: Fleetwood Town 1:1 Arsenal (5:3 i.E.). Auslosung heute.",
            "majorsDone": "VidantaWorld Mexico Open R1: Raul Pereda fuehrt nach einer 65; Austin Smotherman lauert mit 66 Schlaegen dicht dahinter.",
            "wnbaFirstRound": "WNBA Finals Spiel 6 heute: Valkyries (3:2) koennen in Atlanta sensationell den ersten Meistertitel holen.",
            "bracketFootnote": "Spiel 1: Valkyries 68:64. Spiel 2: Dream 79:65. Spiel 3: Dream 97:71. Spiel 4: Valkyries 67:62. Spiel 5: Valkyries 64:55. Spiel 6 heute in Atlanta."
        }
    },
    "it": {
        "soccer": {
            "tagline": "Carabao Cup ottavi: Man City piega Brighton 2-1 e Liverpool batte Chelsea 2-0 staccando il pass per i quarti.",
            "liveNow": "Sorteggio quarti oggi: Man City e Liverpool avanzano con il Fleetwood Town. Premier League torna sabato.",
            "pulse": "SORTEGGIO COPPA DI LEGA: LE GRANDI RAGGIUNGONO IL FLEETWOOD TOWN",
            "keywords": "Carabao Cup, Man City, Liverpool, Fleetwood Town, sorteggio quarti, Haaland, Gakpo"
        },
        "basketball": {
            "tagline": "Finali WNBA Gara 6 stasera: Valkyries (3-2) per la storia; Thunder aprono la stagione NBA con un successo.",
            "liveNow": "Gara 6 stasera ad Atlanta: Valkyries avanti 3-2. NBA: Thunder 122, Nuggets 108 (SGA 34 pts); Spurs 130, Kings 103 (Wemby 29 pts).",
            "pulse": "FINALI WNBA GARA 6: VALKYRIES A UN PASSO DAL SOGNO MONDIALE",
            "keywords": "WNBA Finals, Gara 6, Valkyries, Dream, Angel Reese, ripresa NBA, SGA, Thunder"
        },
        "football": {
            "tagline": "NFL Week 8 al via stasera: I Packers ospitano i Panthers al Lambeau Field con la corsa NFC Nord accesa.",
            "liveNow": "TNF stasera: Panthers (3-4) al Lambeau Field contro i Packers (5-2). Minnesota Vikings (6-0) unici imbattuti.",
            "pulse": "THURSDAY NIGHT FOOTBALL: I PACKERS OSPITANO I PANTHERS A LAMBEAU",
            "keywords": "NFL Week 8, TNF, Packers, Panthers, Jordan Love, Bryce Young, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Vienna ottavi: Alcaraz liquida Berrettini 6-3, 6-4 e Zverev batte Giron conquistando i quarti.",
            "liveNow": "Erste Bank Open R16: Alcaraz batte Berrettini 6-3, 6-4 (28 vincenti, 0 palle break concesse). Zverev supera Giron 6-2, 7-5.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ E ZVEREV VOLANO AI QUARTI A VIENNA",
            "keywords": "ATP, Vienna, Erste Bank Open, Alcaraz, Berrettini, Zverev, Giron, quarti di finale"
        },
        "f1": {
            "tagline": "GP Messico media day: Antonelli conferma il numero 12 per il 2027 a un passo dal titolo con la P9 domenica.",
            "liveNow": "Conferenza a Citta del Messico: Antonelli (365 pts) terra il #12. Un nono posto domenica basta per il Mondiale 2026.",
            "pulse": "GP MESSICO: ANTONELLI CONFERMA IL NUMERO 12 ALL'ALBA DEL TITOLO",
            "keywords": "Formula 1, GP Messico, Antonelli, numero 12, Russell, campione del mondo, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R1: Raul Pereda guida con un 65, Smotherman subito brillante con 66.",
            "liveNow": "VidantaVallarta Giro 1: Raul Pereda (-6, 65) guida di un colpo su Austin Smotherman (-5, 66) e Aaron Rai (-5, 66).",
            "pulse": "PGA TOUR MEXICO OPEN: PEREDA IN TESTA, SMOTHERMAN FIRMA UN 66",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Pereda, Smotherman, Rai, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Desk di giovedi",
            "tonightBlurb": "Finali WNBA Gara 6 ad Atlanta. I Packers sfidano i Panthers al TNF. Man City e Liverpool volano ai quarti di coppa.",
            "plTitle": "Carabao Cup ottavi: Man City e Liverpool approdano ai quarti di finale",
            "plBlurb": "City supera Brighton 2-1 e Liverpool batte Chelsea 2-0; entrambe raggiungono la favola Fleetwood Town tra le migliori otto.",
            "f1Title": "GP Messico: Antonelli conferma il numero 12 prima della storica incoronazione",
            "f1Blurb": "Davanti ai media in Messico, Kimi Antonelli ha bisogno solo del nono posto domenica per essere il piu giovane iridato."
        },
        "pg": {
            "pinFinal": "Coppa di Lega ottavi: Man City batte Brighton 2-1 e Liverpool supera Chelsea 2-0 unendosi a Fleetwood Town nei quarti.",
            "week1Closed": "NFL Settimana 8 TNF: I Packers ospitano i Panthers al freddo del Lambeau Field in prima serata",
            "week1Sub": "Jordan Love (14 TD) guida Green Bay (5-2) contro Bryce Young e Carolina (3-4). Vikings (6-0) imbattuti.",
            "countdownTnf": "TNF stasera: Panthers (3-4) a Green Bay (5-2). Jordan Love mette alla prova la retroguardia ospite. Vikings a 6-0.",
            "barsPoints": "Distanza dalla vetta: Antonelli ha 365 pts, 123 su Russell (242). Il 9° posto in Messico assicura il primo titolo.",
            "tableAfterMonday": "Premier League: City e Arsenal appaiate a 21 (7-0-1). Liverpool 15, Chelsea 13. Coppa: City e Liverpool ai quarti.",
            "pinClub": "Scegli un club. City e Arsenal prime con 21. Man City, Liverpool e Fleetwood Town ai quarti di coppa.",
            "plFootnote": "Mercoledi coppa: Man City 2-1 Brighton, Liverpool 2-0 Chelsea. Martedi: Fleetwood Town 1-1 Arsenal (5-3 dcr). Sorteggio oggi.",
            "majorsDone": "VidantaWorld Mexico Open R1: Raul Pereda guida con un ottimo 65; Austin Smotherman subito a ruota con 66 colpi.",
            "wnbaFirstRound": "Finali WNBA Gara 6 stasera: Valkyries (3-2) possono festeggiare lo storico primo titolo sul parquet di Atlanta.",
            "bracketFootnote": "Gara 1: Valkyries 68-64. Gara 2: Dream 79-65. Gara 3: Dream 97-71. Gara 4: Valkyries 67-62. Gara 5: Valkyries 64-55. Gara 6 stasera ad Atlanta."
        }
    },
    "pl": {
        "soccer": {
            "tagline": "Puchar Ligi runda 4: Man City pokonuje Brighton 2:1, Liverpool ogrywa Chelsea 2:0 i melduje sie w cwiercfinale.",
            "liveNow": "Losowanie cwiercfinalow dzis: Man City i Liverpool dolaczaja do Fleetwood Town. Premier League wraca w sobote.",
            "pulse": "LOSOWANIE PUCHARU LIGI: GIGANCI DOLACZAJA DO FLEETWOOD TOWN",
            "keywords": "Carabao Cup, Man City, Liverpool, Fleetwood Town, losowanie cwiercfinalu, Haaland, Gakpo"
        },
        "basketball": {
            "tagline": "Mecz 6 Finalow WNBA dzis: Valkyries (3-2) graja o historyczny tytul; Thunder otwieraja sezon NBA wygrana.",
            "liveNow": "Mecz 6 dzis w Atlancie: Valkyries prowadza 3-2. NBA: Thunder 122, Nuggets 108 (SGA 34 pkt); Spurs 130, Kings 103 (Wemby 29 pkt).",
            "pulse": "FINALY WNBA MECZ 6: VALKYRIES O KROK OD HISTORYCZNEGO MISTRZOSTWA",
            "keywords": "WNBA Finals, mecz 6, Valkyries, Dream, Angel Reese, start NBA, SGA, Thunder"
        },
        "football": {
            "tagline": "NFL Tydzien 8 startuje dzis: Packers podejmuja Panthers na Lambeau Field w waznym starciu NFC.",
            "liveNow": "TNF dzis w nocy: Panthers (3-4) na Lambeau Field u Packers (5-2). Minnesota Vikings (6-0) jedyna niepokonana druzyna.",
            "pulse": "THURSDAY NIGHT FOOTBALL: PACKERS PODEJMUJA PANTHERS NA LAMBEAU FIELD",
            "keywords": "NFL Tydzien 8, TNF, Packers, Panthers, Jordan Love, Bryce Young, Lambeau Field, Vikings"
        },
        "tennis": {
            "tagline": "Wieden 1/8 finalu: Alcaraz pewnie pokonuje Berrettiniego 6:3, 6:4, Zverev wygrywa z Gironem i wchodzi do cwiercfinalu.",
            "liveNow": "Erste Bank Open 1/8: Alcaraz def. Berrettini 6:3, 6:4 (28 winnerow, zero break pointow rywala). Zverev wygrywa 6:2, 7:5.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ I ZVEREV PEWNIE AWANSUJA DO CWIERCFINALU",
            "keywords": "ATP, Wieden, Erste Bank Open, Alcaraz, Berrettini, Zverev, Giron, cwiercfinal"
        },
        "f1": {
            "tagline": "GP Meksyku dzien medialny: Antonelli potwierdza numer 12 na sezon 2027 przed niedzielna szansa na tytul.",
            "liveNow": "Konferencja w Meksyku: Antonelli (365 pkt) zatrzymuje #12. Dziewiate miejsce w niedziele gwarantuje tytul mistrza swiata 2026.",
            "pulse": "GP MEKSYKU: ANTONELLI POTWIERDZA NUMER 12 PRZED KORONACJA",
            "keywords": "Formula 1, GP Meksyku, Antonelli, numer 12, Russell, mistrz swiata, Hermanos Rodriguez"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open R1: Raul Pereda prowadzi z wynikiem 65, Smotherman otwiera runda 66.",
            "liveNow": "VidantaVallarta Runda 1: Raul Pereda (-6, 65) prowadzi o uderzenie przed Austinem Smothermanem (-5, 66) i Aaronem Rai (-5, 66).",
            "pulse": "PGA TOUR MEXICO OPEN: PEREDA NA CZELE, SMOTHERMAN UZYSKUJE 66",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Pereda, Smotherman, Rai, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Wydanie czwartkowe",
            "tonightBlurb": "Mecz 6 Finalow WNBA w Atlancie. Packers podejmuja Panthers w TNF. Man City i Liverpool w cwiercfinale Pucharu Ligi.",
            "plTitle": "Puchar Ligi runda 4: Man City i Liverpool melduja sie w cwiercfinale",
            "plBlurb": "City wygrywa z Brighton 2:1, a Liverpool pokonuje Chelsea 2:0; obie ekipy dolaczaja do czwartoligowego Fleetwood Town w 1/4 finalu.",
            "f1Title": "GP Meksyku: Antonelli potwierdza numer 12 na krawedzi historycznego triumfu",
            "f1Blurb": "Podczas czwartkowych spotkan z mediami Kimi Antonelli podkresla, ze wystarczy mu 9. lokata w niedziele, by zostac mistrzem."
        },
        "pg": {
            "pinFinal": "Puchar Ligi runda 4: Man City pokonuje Brighton 2:1, a Liverpool odprawia Chelsea 2:0 na drodze do cwiercfinalu.",
            "week1Closed": "NFL Tydzien 8 TNF: Packers podejmuja Panthers na Lambeau Field w blasku reflektorow",
            "week1Sub": "Jordan Love (14 TD) prowadzi Green Bay (5-2) przeciwko Bryce'owi Youngowi i Carolinie (3-4). Vikings (6-0) niepokonani.",
            "countdownTnf": "TNF dzis: Panthers (3-4) u Packers (5-2). Jordan Love sprawdza defensywe Caroliny. Vikings maja bilans 6-0.",
            "barsPoints": "Wykres pokazuje strate do lidera. Antonelli ma 365 pkt, o 123 wiecej niz Russell (242). P9 w Meksyku daje tytul.",
            "tableAfterMonday": "Premier League: City i Arsenal na czele z 21 pkt (7-0-1). Liverpool 15, Chelsea 13. Puchar: City i Liverpool w cwiercfinale.",
            "pinClub": "Wybierz klub. City i Arsenal lideruja z 21 pkt. Man City, Liverpool i Fleetwood Town w cwiercfinale pucharu.",
            "plFootnote": "Sroda puchar: Man City 2:1 Brighton, Liverpool 2:0 Chelsea. Wtorek: Fleetwood 1:1 Arsenal (karne 5:3). Losowanie dzis.",
            "majorsDone": "VidantaWorld Mexico Open R1: Raul Pereda liderem po 65; triumfator z Bermudow Austin Smotherman o krok za nim z 66.",
            "wnbaFirstRound": "Mecz 6 Finalow WNBA dzis: Valkyries (3-2) staja przed szansa zdobycia debiutanckiego tytulu w Atlancie.",
            "bracketFootnote": "Mecz 1: Valkyries 68:64. Mecz 2: Dream 79:65. Mecz 3: Dream 97:71. Mecz 4: Valkyries 67:62. Mecz 5: Valkyries 64:55. Mecz 6 dzis w Atlancie."
        }
    },
    "zh": {
        "soccer": {
            "tagline": "联赛杯第4轮：曼城2-1力克布莱顿，利物浦2-0完胜切尔西携手晋级八强。",
            "liveNow": "四分之一决赛抽签今日揭晓：曼城与利物浦携手弗利特伍德进八强。英超联赛周六战火重燃。",
            "pulse": "联赛杯八强抽签：英超双雄与弗利特伍德进入候选池",
            "keywords": "联赛杯, 曼城, 利物浦, 弗利特伍德, 八强抽签, 哈兰德, 加克波"
        },
        "basketball": {
            "tagline": "WNBA总决赛G6今晚打响：女武神（3-2）客战梦想争冠；雷霆揭幕战力克掘金开启卫冕之旅。",
            "liveNow": "总决赛G6今晚亚特兰大开战：女武神总比分3-2领先。NBA：雷霆122-108掘金（亚历山大34分）；马刺130-103国王。",
            "pulse": "WNBA总决赛G6：金州女武神距历史性夺冠仅差最后一步",
            "keywords": "WNBA总决赛, G6, 女武神, 梦想, 里斯, NBA揭幕战, 亚历山大, 雷霆"
        },
        "football": {
            "tagline": "NFL第8周周四夜赛开幕：包装工坐镇兰博球场迎战黑豹，国联北区竞争白热化。",
            "liveNow": "周四夜赛今晚开打：黑豹（3-4）客场挑战包装工（5-2）。明尼苏达维京人（6-0）高居联盟唯一全胜。",
            "pulse": "周四夜赛：绿湾包装工坐镇兰博球场迎击卡罗来纳黑豹",
            "keywords": "NFL第8周, TNF, 包装工, 黑豹, 爱芙, 布莱斯杨, 兰博球场, 维京人"
        },
        "tennis": {
            "tagline": "维也纳站16强：阿尔卡拉斯6-3、6-4横扫贝雷蒂尼，兹维列夫击败吉隆携手挺进八强。",
            "liveNow": "维也纳公开赛八分之一决赛：阿尔卡拉斯2-0完胜贝雷蒂尼（28记制胜分，未送破发点）。兹维列夫晋级周五八强。",
            "pulse": "维也纳公开赛：阿尔卡拉斯与兹维列夫强势挺进八强",
            "keywords": "ATP, 维也纳, 公开赛, 阿尔卡拉斯, 贝雷蒂尼, 兹维列夫, 吉隆, 八强"
        },
        "f1": {
            "tagline": "墨西哥站媒体日：安东内利确认2027年保留12号车号，周日拿到第9名即可加冕世界冠军。",
            "liveNow": "罗德里格斯赛道媒体日：安东内利（365分）确认保留12号。周日正赛获得第九名即可确保2026世界冠军。",
            "pulse": "墨西哥大奖赛：安东内利确认保留12号迎接世界冠军点",
            "keywords": "F1, 墨西哥站, 安东内利, 12号车号, 拉塞尔, 世界冠军, 罗德里格斯赛道"
        },
        "golf": {
            "tagline": "墨西哥公开赛首轮：本土球星佩雷达轰65杆独占鳌头，斯莫瑟曼交66杆紧随其后。",
            "liveNow": "巴亚尔塔港首轮战罢：佩雷达（-6，65杆）领跑，百慕大冠军斯莫瑟曼（-5，66杆）与阿隆赖并列第二。",
            "pulse": "美巡赛墨西哥公开赛：佩雷达领跑，斯莫瑟曼交出66杆",
            "keywords": "美巡赛, 墨西哥公开赛, 佩雷达, 斯莫瑟曼, 阿隆赖, 巴亚尔塔港, 秋季赛"
        },
        "home": {
            "tonight": "周四体育前线",
            "tonightBlurb": "WNBA总决赛G6客战亚特兰大。包装工周四夜赛迎击黑豹。曼城利物浦双双闯入联赛杯八强。",
            "plTitle": "联赛杯第4轮：曼城与利物浦携手挺进八强",
            "plBlurb": "曼城2-1险胜布莱顿，利物浦2-0轻取切尔西，与第四级别黑马弗利特伍德一同晋级联赛杯四分之一决赛。",
            "f1Title": "墨西哥大奖赛：安东内利确认保留12号迎接加冕时刻",
            "f1Blurb": "在墨西哥城接受全球媒体采访时，安东内利表示只需在周日正赛中取得第九名即可成为历史最年轻世界冠军。"
        },
        "pg": {
            "pinFinal": "联赛杯第4轮：曼城2-1布莱顿，利物浦2-0击溃切尔西，携手英乙弗利特伍德晋级八强。",
            "week1Closed": "NFL第8周TNF：包装工在兰博球场的灯光与寒风中迎战黑豹",
            "week1Sub": "爱芙（14次达阵）率领5胜2负的绿湾迎击布莱斯杨的黑豹。维京人（6-0）独享不败战绩。",
            "countdownTnf": "今晚周四夜赛：黑豹（3-4）客场挑战包装工（5-2）。爱芙考验黑豹二道防线。维京人保持6-0。",
            "barsPoints": "积分柱状图显示与领跑者的差距。安东内利365分，领先拉塞尔123分。墨西哥站第9即可锁定头衔。",
            "tableAfterMonday": "英超积分榜：曼城与阿森纳同积21分（7胜0平1负）。利物浦15，切尔西13。联赛杯：曼城利物浦双双晋级。",
            "pinClub": "选择俱乐部查看数据。曼城阿森纳积21分领跑。曼城、利物浦与弗利特伍德闯入联赛杯八强。",
            "plFootnote": "周三联赛杯：曼城2-1布莱顿，利物浦2-0切尔西。周二：弗利特伍德1-1阿森纳（点球5-3）。八强抽签今日举行。",
            "majorsDone": "墨西哥公开赛第1轮：佩雷达打出65杆独占首位；百慕大锦标赛冠军斯莫瑟曼交出66杆仅落后一杆。",
            "wnbaFirstRound": "WNBA总决赛G6今晚开打：手握3-2领先的女武神有望在亚特兰大客场夺得历史首冠。",
            "bracketFootnote": "G1: 女武神 68-64。G2: 梦想 79-65。G3: 梦想 97-71。G4: 女武神 67-62。G5: 女武神 64-55。G6 今晚亚特兰大开打。"
        }
    },
    "ja": {
        "soccer": {
            "tagline": "カラバオ杯4回戦：マンチェスターCがブライトンに2-1、リヴァプールがチェルシーに2-0で勝利し8強入り。",
            "liveNow": "本日準々決勝抽選会：マンCとリヴァプールがフリートウッド・タウンと共に8強進出。プレミアリーグは土曜再開。",
            "pulse": "カラバオ杯8強抽選会：強豪2クラブがフリートウッドと共にドローへ",
            "keywords": "カラバオ杯, マンC, リヴァプール, フリートウッド, 8強抽選, ハーランド, ガクポ"
        },
        "basketball": {
            "tagline": "WNBAファイナル第6戦今夜：ヴァルキリーズ（3勝2敗）が初制覇に挑む；NBA開幕戦でサンダーがナゲッツ破る。",
            "liveNow": "今夜アトランタで第6戦：ヴァルキリーズが王手。NBA：サンダー 122-108 ナゲッツ（SGA 34点）；スパーズ 130-103 キングス。",
            "pulse": "WNBAファイナル第6戦：ヴァルキリーズが歴史的初優勝へカウントダウン",
            "keywords": "WNBAファイナル, 第6戦, ヴァルキリーズ, ドリーム, エンジェル・リース, NBA開幕週, SGA, サンダー"
        },
        "football": {
            "tagline": "NFL第8週今夜開幕：パッカーズがランボー・フィールドにパンサーズを迎え撃つ注目のNFC対決。",
            "liveNow": "TNF今夜：パンサーズ（3勝4敗）がパッカーズ（5勝2敗）と対戦。ミネソタ・バイキングス（6勝0敗）が唯一無敗を維持。",
            "pulse": "サーズデーナイトフットボール：パッカーズがランボーでパンサーズを迎え撃つ",
            "keywords": "NFL第8週, TNF, パッカーズ, パンサーズ, ジョーダン・ラヴ, ブライス・ヤング, ランボー・フィールド, バイキングス"
        },
        "tennis": {
            "tagline": "ウィーン16強：アルカラスがベレッティーニを6-3、6-4で破り、ズベレフもギロン下し8強進出。",
            "liveNow": "エルステ・バンク・オープン16強：アルカラスがベレッティーニをストレート破る（ウィナー28本、被BPゼロ）。ズベレフも8強。",
            "pulse": "エルステ・バンク・オープン：アルカラスとズベレフがウィーン8強へ進出",
            "keywords": "ATP, ウィーン, エルステ・バンク・オープン, アルカラス, ベレッティーニ, ズベレフ, ギロン, 準々決勝"
        },
        "f1": {
            "tagline": "F1メキシコGP木曜会見：アントネッリが2027年もカーナンバー12継続を明言、日曜9位で戴冠決定。",
            "liveNow": "メキシコ公式会見：アントネッリ（365点）が12番維持を発表。日曜の決勝で9位以上に入れば2026年世界王者に決定。",
            "pulse": "メキシコGP：アントネッリが戴冠目前で12番継続を発表",
            "keywords": "F1, メキシコGP, アントネッリ, ゼッケン12, ラッセル, 世界王者, ロドリゲス・サーキット"
        },
        "golf": {
            "tagline": "ヴィダンタワールド・メキシコオープン初日：地元ペレダが65で単独首位発進、好調スモザーマンが66で追走。",
            "liveNow": "ヴィダンタ・ヴァジャルタ第1ラウンド：ラウル・ペレダ（-6、65）が首位、スモザーマン（-5、66）とライが2位タイ。",
            "pulse": "PGAツアー・メキシコオープン：ペレダが単独首位、スモザーマンが66発進",
            "keywords": "PGAツアー, メキシコオープン, ペレダ, スモザーマン, ライ, ヴィダンタ・ヴァジャルタ, フォールシリーズ"
        },
        "home": {
            "tonight": "木曜デスク",
            "tonightBlurb": "WNBAファイナル第6戦がアトランタで開催。パッカーズがTNFでパンサーズを迎撃。マンCとリヴァプールがリーグ杯8強進出。",
            "plTitle": "カラバオ杯4回戦：マンチェスター・Cとリヴァプールが8強入り",
            "plBlurb": "マンチェスター・Cがブライトンを2-1、リヴァプールがチェルシーを2-0で下し、4部フリートウッドと共に準々決勝へ駒を進めた。",
            "f1Title": "メキシコGP：アントネッリが戴冠目前でカーナンバー12継続を明言",
            "f1Blurb": "メキシコでの公式会見で、キミ・アントネッリは日曜に9位以上に入ればF1史上最年少世界王者になると語った。"
        },
        "pg": {
            "pinFinal": "カラバオ杯4回戦：マンチェスターCがブライトンに2-1、リヴァプールがチェルシーに2-0で勝利し8強進出。",
            "week1Closed": "NFL第8週TNF：凍てつくランボー・フィールドのカクテル光線の下でパッカーズがパンサーズを迎え撃つ",
            "week1Sub": "ジョーダン・ラヴ（14TD）率いるグリーンベイ（5勝2敗）がブライス・ヤングのパンサーズと激突。バイキングス（6勝0敗）が唯一無敗。",
            "countdownTnf": "今夜TNF：パンサーズ（3勝4敗）対パッカーズ（5勝2敗）。ラヴが敵守備陣をテスト。バイキングスは6戦全勝。",
            "barsPoints": "首位との差を示すバー。アントネッリは365点でラッセル（242点）に123点差。メキシコでP9獲得なら即戴冠。",
            "tableAfterMonday": "プレミアリーグ：マンCとアーセナルが勝ち点21で並ぶ（7勝1敗）。リヴァプール15、チェルシー13。カップ戦：マンCとリヴァプールが8強へ。",
            "pinClub": "クラブを選択。マンCとアーセナルが勝ち点21で首位タイ。マンC、リヴァプール、フリートウッドが準々決勝進出。",
            "plFootnote": "水曜カップ戦：マンC 2-1 ブライトン、リヴァプール 2-0 チェルシー。火曜：フリートウッド 1-1 アーセナル（PK 5-3）。抽選会は本日開催。",
            "majorsDone": "ヴィダンタワールド・メキシコオープン初日：ラウル・ペレダが65で単独首位；バミューダ覇者スモザーマンが66で1打差追走。",
            "wnbaFirstRound": "WNBAファイナル第6戦今夜：3勝2敗と王手をかけたヴァルキリーズが敵地アトランタで初年度戴冠へ挑戦。",
            "bracketFootnote": "第1戦: ヴァルキリーズ 68-64。第2戦: ドリーム 79-65。第3戦: ドリーム 97-71。第4戦: ヴァルキリーズ 67-62。第5戦: ヴァルキリーズ 64-55。第6戦 今夜アトランタ。"
        }
    },
    "ko": {
        "soccer": {
            "tagline": "카라바오컵 16강: 맨시티 2-1 브라이턴, 리버풀 2-0 첼시 제압하고 8강 진출 확정.",
            "liveNow": "8강 대진 추첨 오늘 진행: 맨시티와 리버풀이 4부 플리트우드와 함께 8강 합류. 프리미어리그는 토요일 재개.",
            "pulse": "카라바오컵 8강 대진 추첨: 강호들이 플리트우드와 함께 추첨함에 합류",
            "keywords": "카라바오컵, 맨시티, 리버풀, 플리트우드, 8강 추첨, 홀란, 각포"
        },
        "basketball": {
            "tagline": "WNBA 파이널 6차전 오늘 밤: 발키리스(3-2) 창단 첫 우승 도전; 썬더는 NBA 개막전 승리로 산뜻한 출발.",
            "liveNow": "파이널 6차전 오늘 밤 애틀랜타서 격돌: 발키리스 3-2 리드. NBA: 썬더 122-108 너게츠(SGA 34점); 스퍼스 130-103 킹스.",
            "pulse": "WNBA 파이널 6차전: 골든스테이트 발키리스 역사적 우승까지 단 1승",
            "keywords": "WNBA 파이널, 6차전, 발키리스, 드림, 엔젤 리스, NBA 개막주간, SGA, 썬더"
        },
        "football": {
            "tagline": "NFL 8주차 오늘 밤 킥오프: 패커스가 램보 필드서 팬서스 맞아 NFC 북부 추격전 가속.",
            "liveNow": "오늘 밤 TNF: 팬서스(3승 4패) 원정서 패커스(5승 2패)와 대결. 미네소타 바이킹스(6승 무패) 유일 무패 행진.",
            "pulse": "서스데이 나이트 풋볼: 패커스, 램보 필드 조명 아래 팬서스와 격돌",
            "keywords": "NFL 8주차, TNF, 패커스, 팬서스, 조던 러브, 브라이스 영, 램보 필드, 바이킹스"
        },
        "tennis": {
            "tagline": "빈 16강: 알카라스 베레티니 6-3, 6-4 완파, 츠베레프 기론 꺾고 나란히 8강 진출.",
            "liveNow": "에르스테 방크 오픈 16강: 알카라스 2-0 베레티니(위너 28개, 브레이크 허용 0개). 츠베레프 2-0 기론으로 금요일 8강 진출.",
            "pulse": "에르스테 방크 오픈: 알카라스와 츠베레프 빈 8강 순항",
            "keywords": "ATP, 빈, 에르스테 방크 오픈, 알카라스, 베레티니, 츠베레프, 기론, 8강"
        },
        "f1": {
            "tagline": "F1 멕시코 GP 미디어 데이: 안토넬리 2027년에도 12번 유지 선언, 일요일 9위면 챔피언 확정.",
            "liveNow": "멕시코시티 기자회견: 안토넬리(365점) 12번 유지 발표. 일요일 결선 9위 달성 시 2026 월드 챔피언 확정.",
            "pulse": "멕시코 GP: 안토넬리 챔피언 등극 앞두고 등번호 12번 유지 발표",
            "keywords": "F1, 멕시코 GP, 안토넬리, 등번호 12번, 러셀, 월드 챔피언, 로드리게스 서킷"
        },
        "golf": {
            "tagline": "비단타월드 멕시코 오픈 1R: 홈스타 라울 페레다 65타 선두, 스모더맨 66타로 맹추격.",
            "liveNow": "비단타 바야르타 1라운드: 라울 페레다(-6, 65타) 선두, 오스틴 스모더맨(-5, 66타)과 에런 라이 공동 2위.",
            "pulse": "PGA 투어 멕시코 오픈: 페레다 선두 질주, 스모더맨 66타 작성",
            "keywords": "PGA 투어, 멕시코 오픈, 페레다, 스모더맨, 라이, 비단타 바야르타, 페덱스컵 가을"
        },
        "home": {
            "tonight": "목요일 데스크",
            "tonightBlurb": "WNBA 파이널 6차전 애틀랜타서 개최. 패커스 TNF서 팬서스 격돌. 맨시티와 리버풀 리그컵 8강 안착.",
            "plTitle": "카라바오컵 16강: 맨체스터 시티와 리버풀 나란히 8강 진출",
            "plBlurb": "맨시티가 브라이턴을 2-1로 제압하고 리버풀이 첼시를 2-0으로 꺾으며 4부 돌풍의 플리트우드와 함께 8강에 올랐다.",
            "f1Title": "멕시코 GP: 안토넬리 대관식 앞두고 12번 고수 선언",
            "f1Blurb": "멕시코 현지 미디어 데이서 키미 안토넬리는 일요일 결선 9위만 기록해도 역대 최연소 F1 월드 챔피언에 오른다고 밝혔다."
        },
        "pg": {
            "pinFinal": "카라바오컵 16강: 맨시티가 브라이턴을 2-1로, 리버풀이 첼시를 2-0으로 꺾고 8강에 진출했다.",
            "week1Closed": "NFL 8주차 TNF: 패커스가 램보 필드의 차가운 밤 조명 아래 팬서스를 맞이한다",
            "week1Sub": "조던 러브(14 TD)의 그린베이(5승 2패)가 브라이스 영의 캐롤라이나(3승 4패)와 맞대결. 바이킹스(6-0) 단독 무패.",
            "countdownTnf": "오늘 밤 TNF: 팬서스(3-4) 대 패커스(5-2). 조던 러브가 캐롤라이나 수비를 공략한다. 바이킹스 6전 전승.",
            "barsPoints": "선두와의 격차를 보여주는 막대. 안토넬리는 365점으로 러셀(242점)에 123점 앞서 있다. 멕시코 9위면 타이틀 확정.",
            "tableAfterMonday": "프리미어리그: 맨시티와 아스널 승점 21로 공동 선두(7승 1패). 리버풀 15, 첼시 13. 리그컵: 맨시티와 리버풀 8강 진출.",
            "pinClub": "클럽을 선택하세요. 맨시티와 아스널 승점 21로 공동 1위. 맨시티, 리버풀, 플리트우드가 리그컵 8강에 합류.",
            "plFootnote": "수요일 리그컵: 맨시티 2-1 브라이턴, 리버풀 2-0 첼시. 화요일: 플리트우드 1-1 아스널(승부차기 5-3). 대진 추첨 오늘 진행.",
            "majorsDone": "비단타월드 멕시코 오픈 1R: 라울 페레다가 65타로 선두; 버뮤다 챔피언 스모더맨이 66타로 1타 차 추격.",
            "wnbaFirstRound": "WNBA 파이널 6차전 오늘 밤: 3승 2패로 앞선 발키리스가 애틀랜타 원정서 창단 첫해 우승 확정에 도전한다.",
            "bracketFootnote": "1차전: 발키리스 68-64. 2차전: 드림 79-65. 3차전: 드림 97-71. 4차전: 발키리스 67-62. 5차전: 발키리스 64-55. 6차전 오늘 밤 애틀랜타."
        }
    },
    "ar": {
        "soccer": {
            "tagline": "كأس الرابطة دور الـ 16: مانشستر سيتي يتفوق على برايتون 2-1 وليفربول يهزم تشيلسي 2-0 ليعبرا إلى ربع النهائي.",
            "liveNow": "قرعة ربع النهائي اليوم: مانشستر سيتي وليفربول يعبران برفقة فليتوود تاون. عودة الدوري الإنجليزي الممتاز يوم السبت.",
            "pulse": "قرعة ربع نهائي كأس الرابطة: عمالقة إنجلترا ينضمون إلى فليتوود تاون",
            "keywords": "كأس الرابطة, مانشستر سيتي, ليفربول, فليتوود تاون, قرعة ربع النهائي, هالاند, خاكبو"
        },
        "basketball": {
            "tagline": "نهائي WNBA المباراة 6 الليلة: فالكيريز (3-2) يطارد لقبا تاريخيا؛ وثاندر يفتتح حملة الدفاع عن لقبه في NBA بفوز ثمين.",
            "liveNow": "المباراة 6 الليلة في أتلانتا: فالكيريز متقدم 3-2. دوري NBA: ثاندر 122-108 ناغتس (غيلجيوس-ألكسندر 34 نقطة)؛ سبيرز 130-103 كينغز.",
            "pulse": "نهائي دوري السلة النسائي WNBA المباراة 6: فالكيريز على بعد خطوة من المجد التاريخي",
            "keywords": "نهائي WNBA, المباراة 6, فالكيريز, دريم, أنجيل ريس, انطلاق NBA, ألكسندر, ثاندر"
        },
        "football": {
            "tagline": "انطلاق الأسبوع 8 من دوري كرة القدم الأمريكية الليلة: باكرز يستضيف بانثرز في لامبو فيلد مع اشتعال المنافسة.",
            "liveNow": "مباراة ليلة الخميس الليلة: بانثرز (3-4) في ضيافة باكرز (5-2) على برايم فيديو. مينيسوتا فايكنغز (6-0) الفريق الوحيد بدون هزيمة.",
            "pulse": "مباراة ليلة الخميس: غرين باي باكرز يستضيف كارولاينا بانثرز في لامبو فيلد",
            "keywords": "دوري NFL الأسبوع 8, TNF, باكرز, بانثرز, جوردان لوف, برايس يونغ, لامبو فيلد, فايكنغز"
        },
        "tennis": {
            "tagline": "بطولة فيينا ثمن النهائي: ألكاراز يكتسح بيريتيني 6-3 و6-4 وزفيريف يتجاوز غيرون ليبلغا ربع النهائي.",
            "liveNow": "بطولة بنك إيرستيه ثمن النهائي: ألكاراز يهزم بيريتيني 6-3 و6-4 (28 ضربة قاضية وبدون أي نقطة كسر). وزفيريف يتأهل لربع نهائي الجمعة.",
            "pulse": "بطولة بنك إيرستيه المفتوحة: ألكاراز وزفيريف يبلغان ربع النهائي في فيينا",
            "keywords": "تنس, فيينا, بنك إيرستيه المفتوحة, ألكاراز, بيريتيني, زفيريف, غيرون, ربع النهائي"
        },
        "f1": {
            "tagline": "جائزة المكسيك الكبرى اليوم الإعلامي: أنتونيللي يؤكد بقاء الرقم 12 لعام 2027 ويكفيه المركز 9 يوم الأحد للتتويج.",
            "liveNow": "يوم الإعلام في حلبة هيرمانوس رودريغيز: أنتونيللي (365 نقطة) يحتفظ بالرقم 12. المركز التاسع يوم الأحد يضمن له اللقب العالمي.",
            "pulse": "جائزة المكسيك الكبرى: أنتونيللي يؤكد احتفاظه بالرقم 12 قبل التتويج التاريخي",
            "keywords": "فورمولا 1, جائزة المكسيك, أنتونيللي, الرقم 12, راسل, بطل العالم, حلبة هيرمانوس رودريغيز"
        },
        "golf": {
            "tagline": "بطولة فيدانتا وورلد المكسيك المفتوحة الجولة 1: راؤول بيريدا يتصدر بـ 65 ضربة وسموذر مان يتألق بـ 66 ضربة.",
            "liveNow": "فيدانتا فايارتا الجولة 1: راؤول بيريدا (-6، 65) يتصدر بفارق ضربة واحدة أمام أوستن سموذر مان (-5، 66) وآرون راي (-5، 66).",
            "pulse": "جولة بي جي إيه بطولة المكسيك المفتوحة: بيريدا يتصدر وسموذر مان يسجل 66 ضربة",
            "keywords": "جولة بي جي إيه, بطولة المكسيك المفتوحة, بيريدا, سموذر مان, راي, فيدانتا فايارتا, كأس فيديكس"
        },
        "home": {
            "tonight": "مكتب الخميس",
            "tonightBlurb": "المباراة 6 في نهائي WNBA في أتلانتا. باكرز يستضيف بانثرز في مباراة ليلة الخميس. مانشستر سيتي وليفربول يبلغان ربع نهائي الكأس.",
            "plTitle": "كأس الرابطة دور الـ 16: مانشستر سيتي وليفربول يحجزان بطاقتي ربع النهائي",
            "plBlurb": "سيتي يتخطى برايتون 2-1 وليفربول يهزم تشيلسي 2-0 ليلحقا بفريق الدرجة الرابعة فليتوود تاون في الدور ربع النهائي.",
            "f1Title": "جائزة المكسيك الكبرى: أنتونيللي يؤكد الرقم 12 على أعتاب التتويج التاريخي",
            "f1Blurb": "خلال حديثه للإعلام في المكسيك، يحتاج كيمي أنتونيللي إلى المركز التاسع فقط يوم الأحد ليصبح أصغر بطل عالم في تاريخ فورمولا 1."
        },
        "pg": {
            "pinFinal": "كأس الرابطة دور الـ 16: مانشستر سيتي يهزم برايتون 2-1 وليفربول يتفوق على تشيلسي 2-0 ليبلغا ربع النهائي.",
            "week1Closed": "دوري كرة القدم الأمريكية الأسبوع 8: باكرز يستضيف بانثرز في ملعب لامبو فيلد تحت الأضواء الكاشفة",
            "week1Sub": "جوردان لوف (14 تمريرة حاسمة) يقود غرين باي (5-2) أمام برايس يونغ وكارولاينا (3-4). فايكنغز (6-0) دون هزيمة.",
            "countdownTnf": "مباراة ليلة الخميس اليوم: بانثرز (3-4) في ضيافة باكرز (5-2). لوف يختبر دفاع كارولاينا. فايكنغز بسجل 6-0.",
            "barsPoints": "الأشرطة توضح الفارق عن المتصدر. أنتونيللي لديه 365 نقطة بفارق 123 عن راسل (242). المركز التاسع في المكسيك يحسم اللقب.",
            "tableAfterMonday": "الدوري الإنجليزي: سيتي وأرسنال في الصدارة بـ 21 نقطة (7-0-1). ليفربول 15، تشيلسي 13. الكأس: تأهل سيتي وليفربول.",
            "pinClub": "اختر ناديا. سيتي وأرسنال يتصدران بـ 21 نقطة. مانشستر سيتي وليفربول وفليتوود تاون في ربع نهائي الكأس.",
            "plFootnote": "مباريات الأربعاء: سيتي 2-1 برايتون، ليفربول 2-0 تشيلسي. الثلاثاء: فليتوود 1-1 أرسنال (ترجيح 5-3). القرعة اليوم.",
            "majorsDone": "بطولة المكسيك المفتوحة الجولة 1: راؤول بيريدا يتصدر بعد تسجيل 65 ضربة؛ وبطل برمودا سموذر مان يطارده بـ 66 ضربة.",
            "wnbaFirstRound": "نهائي دوري WNBA المباراة 6 الليلة: فالكيريز (3-2) بإمكانه حسم لقبه التاريخي الأول في صالة أتلانتا.",
            "bracketFootnote": "م 1: فالكيريز 68-64. م 2: دريم 79-65. م 3: دريم 97-71. م 4: فالكيريز 67-62. م 5: فالكيريز 64-55. المباراة 6 الليلة في أتلانتا."
        }
    }
}

# 1. Update frontend/src/i18n/playground.ts
pg_file = "frontend/src/i18n/playground.ts"
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
    # update sports
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

print("All locale updates for 29 Oct 2026 completed successfully!")
