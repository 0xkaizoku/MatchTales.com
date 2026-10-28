# -*- coding: utf-8 -*-
import re
import os

DATA = {
    "en": {
        "soccer": {
            "tagline": "Carabao Cup shock: League Two Fleetwood Town stun Arsenal 5-3 on penalties after 1-1 draw.",
            "liveNow": "Fourth Round drama: Fleetwood Town eliminate Arsenal 5-3 on penalties. Wednesday ties: Man City vs Brighton, Liverpool vs Chelsea.",
            "pulse": "LEAGUE CUP SHOCK: FLEETWOOD TOWN STUN ARSENAL IN SHOOTOUT",
            "keywords": "Carabao Cup, Fleetwood Town, Arsenal, penalty shootout, Fourth Round, shock upset"
        },
        "basketball": {
            "tagline": "Valkyries grab 3-2 Finals lead as NBA season explodes with Wembanyama 29-point show.",
            "liveNow": "WNBA Finals Game 5: Valkyries 64, Dream 55. NBA Opening: Spurs 130, Kings 103 (Wemby 9 dunks); Celtics 125, Nets 124 (Tatum 40 pts).",
            "pulse": "HOOPS EXPLOSION: VALKYRIES SEIZE 3-2 LEAD AS NBA TIPOFS",
            "keywords": "WNBA Finals, Game 5, Valkyries, Dream, NBA opening night, Wembanyama, Tatum, Spurs"
        },
        "football": {
            "tagline": "Cowboys crush Eagles 38-21 on MNF: Prescott throws 3 TDs; Packers host Panthers on Thursday night.",
            "liveNow": "MNF Final: Cowboys 38, Eagles 21 behind Prescott masterclass. Vikings (6-0) stand as lone unbeaten. TNF: Panthers at Packers.",
            "pulse": "MNF STATEMENT: COWBOYS ROUT EAGLES 38-21 IN PHILADELPHIA",
            "keywords": "NFL Week 7, MNF, Cowboys, Eagles, Prescott, Week 8, Packers, Panthers, TNF"
        },
        "tennis": {
            "tagline": "Vienna drama: Alcaraz downs Khachanov in straight sets while Zverev survives 13-11 tiebreak marathon.",
            "liveNow": "Vienna R1: Alcaraz def. Khachanov 6-4, 7-6 (5). Zverev outlasts Landaluce 7-5, 3-6, 7-6 (13-11) saving match points.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ AND ZVEREV SURVIVE VIENNA OPENERS",
            "keywords": "ATP, Vienna, Erste Bank Open, Alcaraz, Khachanov, Zverev, Landaluce, tiebreak"
        },
        "f1": {
            "tagline": "Mexico City GP countdown: Antonelli needs ninth place at Hermanos Rodriguez to seal maiden title.",
            "liveNow": "Championship equation: Antonelli (365 pts) leads Russell by 123. P9 on Sunday guarantees title. Antonelli confirms car #12 for 2027.",
            "pulse": "MEXICO CITY GP: ANTONELLI ON BRINK OF HISTORIC WORLD TITLE",
            "keywords": "Formula 1, Mexico City GP, Antonelli, Russell, World Champion, Hermanos Rodriguez, Mercedes"
        },
        "golf": {
            "tagline": "VidantaWorld Mexico Open tee-off: Smotherman brings Bermuda momentum to $6M FedExCup Fall test.",
            "liveNow": "Mexico Open Preview: Field gathers at VidantaVallarta. Smotherman seeks back-to-back wins after 3rd playoff hole triumph in Bermuda.",
            "pulse": "FEDEXCUP FALL: VIDANTAWORLD MEXICO OPEN TEEING OFF",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Power, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Wednesday desk",
            "tonightBlurb": "Fleetwood Town stun Arsenal on penalties in Carabao Cup. Valkyries grab 3-2 Finals lead. Cowboys route Eagles on MNF.",
            "plTitle": "Carabao Cup miracle: League Two Fleetwood Town knock out Arsenal on penalties",
            "plBlurb": "David Harrington saves Bukayo Saka penalty as fourth-tier minnows hold Arsenal 1-1 and win 5-3 in shootout at Highbury.",
            "f1Title": "Mexico City GP: Antonelli stands on brink of maiden world title",
            "f1Blurb": "With a 123-point lead, Kimi Antonelli needs only a ninth-place finish in Mexico to become the youngest champion in F1 history."
        },
        "pg": {
            "pinFinal": "Carabao Cup Final (pen 5-3): Fleetwood Town 1, Arsenal 1. League Two underdogs eliminate Arsenal in sensational shootout.",
            "week1Closed": "NFL Week 7 MNF final: Cowboys rout Eagles 38-21 at Lincoln Financial Field",
            "week1Sub": "Prescott throws 3 TDs and Lamb posts 116 yards. Vikings (6-0) stand as lone unbeaten. Thursday night: Panthers at Packers.",
            "countdownTnf": "TNF Thursday: Panthers (3-4) at Packers (5-2). Cowboys topple Eagles 38-21 on MNF. Vikings stand 6-0.",
            "barsPoints": "Bars show the gap to the leader. Antonelli has 365, 123 ahead of Russell on 242. P9 in Mexico clinches title.",
            "tableAfterMonday": "Premier League: City and Arsenal tied on 21 (7-0-1). Liverpool 15, Chelsea 13, Bournemouth 13. Fleetwood stun Arsenal in cup.",
            "pinClub": "Select a club. City and Arsenal top table on 21. Fleetwood Town eliminate Arsenal 5-3 on penalties in Carabao Cup.",
            "plFootnote": "Tuesday cup: Fleetwood Town 1-1 Arsenal (5-3 pens); Bradford 2-0 Peterborough. Wednesday: Man City vs Brighton, Liverpool vs Chelsea.",
            "majorsDone": "VidantaWorld Mexico Open tee-off: Smotherman headlines $6M FedExCup Fall event after 3rd-playoff-hole Bermuda victory.",
            "wnbaFirstRound": "WNBA Finals Game 5 final: Valkyries defeat Dream 64-55 behind stifling defense to seize 3-2 championship lead.",
            "bracketFootnote": "Game 1: Valkyries 68-64. Game 2: Dream 79-65. Game 3: Dream 97-71. Game 4: Valkyries 67-62. Game 5: Valkyries 64-55. Series 3-2 GSV."
        }
    },
    "fr": {
        "soccer": {
            "tagline": "Exploit en Carabao Cup : Fleetwood Town (D4) elimine Arsenal aux tirs au but (5-3) apres un nul 1-1.",
            "liveNow": "Drame au 4e tour : Fleetwood Town sort Arsenal aux tirs au but (5-3). Mercredi : Man City contre Brighton, Liverpool contre Chelsea.",
            "pulse": "SEISME EN COUPE : FLEETWOOD TOWN SORT ARSENAL AUX TIRS AU BUT",
            "keywords": "Carabao Cup, Fleetwood Town, Arsenal, tirs au but, 4e tour, exploit historique"
        },
        "basketball": {
            "tagline": "Les Valkyries menent 3-2 en Finales tandis que la NBA demarre avec le festival Wembanyama.",
            "liveNow": "Finales WNBA match 5 : Valkyries 64, Dream 55. Reprise NBA : Spurs 130, Kings 103 (Wemby 9 dunks) ; Celtics 125, Nets 124 (Tatum 40 pts).",
            "pulse": "EXPLOSION BASKET : LES VALKYRIES MENENT 3-2, LA NBA S'ENFLAMME",
            "keywords": "Finales WNBA, match 5, Valkyries, Dream, reprise NBA, Wembanyama, Tatum, Spurs"
        },
        "football": {
            "tagline": "Les Cowboys ecrasent les Eagles 38-21 au MNF : Prescott lance 3 TD ; les Packers recoivent Carolina jeudi.",
            "liveNow": "MNF final : Cowboys 38, Eagles 21 grace au recital de Prescott. Vikings (6-0) seuls invaincus. TNF : Panthers chez les Packers.",
            "pulse": "DEMONSTRATION AU MNF : DALLAS SURCLASSE PHILADELPHIE 38-21",
            "keywords": "NFL semaine 7, MNF, Cowboys, Eagles, Prescott, semaine 8, Packers, Panthers, TNF"
        },
        "tennis": {
            "tagline": "Tension a Vienne : Alcaraz domine Khachanov en deux sets, Zverev survit a un tiebreak marathon 13-11.",
            "liveNow": "Vienne 1er tour : Alcaraz bat Khachanov 6-4, 7-6 (5). Zverev domine Landaluce 7-5, 3-6, 7-6 (13-11) en sauvant des balles de match.",
            "pulse": "ERSTE BANK OPEN : ALCARAZ ET ZVEREV PASSENT LE PIEGE VIENNOIS",
            "keywords": "ATP, Vienne, Erste Bank Open, Alcaraz, Khachanov, Zverev, Landaluce, tiebreak"
        },
        "f1": {
            "tagline": "Compte a rebours au Mexique : Antonelli vise une 9e place pour sceller son premier titre mondial.",
            "liveNow": "Scenario du titre : Antonelli (365 pts) compte 123 pts d'avance sur Russell. Une 9e place dimanche garantit la couronne.",
            "pulse": "GP DU MEXIQUE : ANTONELLI AUX PORTES D'UN TITRE HISTORIQUE",
            "keywords": "Formule 1, GP du Mexique, Antonelli, Russell, champion du monde, Hermanos Rodriguez, Mercedes"
        },
        "golf": {
            "tagline": "Coup d'envoi du VidantaWorld Mexico Open : Smotherman surfe sur son exploit des Bermudes.",
            "liveNow": "Presentation Mexique : Le circuit s'installe a VidantaVallarta. Smotherman vise le double apres son triomphe en playoff aux Bermudes.",
            "pulse": "FEDEXCUP FALL : LE VIDANTAWORLD MEXICO OPEN PREND LE DEPART",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Power, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Desk du mercredi",
            "tonightBlurb": "Fleetwood Town sort Arsenal en Carabao Cup. Les Valkyries menent 3-2 en Finales. Les Cowboys ecrasent les Eagles au MNF.",
            "plTitle": "Miracle en Coupe : Fleetwood Town (D4) elimine Arsenal aux tirs au but",
            "plBlurb": "David Harrington devie le tir de Bukayo Saka et Fleetwood (D4) s'impose 5-3 aux tirs au but apres un nul 1-1 a Highbury.",
            "f1Title": "GP du Mexique : Antonelli a un pas du sacre mondial",
            "f1Blurb": "Avec 123 points d'avance, Kimi Antonelli n'a besoin que d'une neuvieme place a Mexico pour devenir le plus jeune champion de l'histoire."
        },
        "pg": {
            "pinFinal": "Coupe de la Ligue (tab 5-3) : Fleetwood Town 1, Arsenal 1. Le club de D4 elimine Arsenal au terme d'une seance epique.",
            "week1Closed": "NFL Semaine 7 MNF final : Les Cowboys surclassent les Eagles 38-21 au Lincoln Financial Field",
            "week1Sub": "Prescott lance 3 TD et Lamb capte 116 yards. Vikings (6-0) seuls invaincus. Jeudi soir : Panthers chez les Packers.",
            "countdownTnf": "TNF Jeudi : Panthers (3-4) chez les Packers (5-2). Dallas domine Philadelphie 38-21 au MNF. Vikings a 6-0.",
            "barsPoints": "L'ecart avec le leader : Antonelli a 365 pts, 123 d'avance sur Russell (242). La 9e place au Mexique scelle le titre.",
            "tableAfterMonday": "Premier League : City et Arsenal a 21 pts (7-0-1). Liverpool 15, Chelsea 13. Exploit retentissant de Fleetwood en coupe.",
            "pinClub": "Selectionnez un club. City et Arsenal co-leaders a 21 pts. Fleetwood Town sort Arsenal aux tirs au but.",
            "plFootnote": "Mardi en coupe : Fleetwood Town 1-1 Arsenal (5-3 tab) ; Bradford 2-0 Peterborough. Mercredi : Man City vs Brighton, Liverpool vs Chelsea.",
            "majorsDone": "Coup d'envoi du Mexico Open : Smotherman en vedette a VidantaVallarta apres sa victoire au 3e trou de playoff aux Bermudes.",
            "wnbaFirstRound": "Finales WNBA match 5 final : Les Valkyries battent le Dream 64-55 grace a leur verrou defensif et menent 3-2.",
            "bracketFootnote": "Match 1 : Valkyries 68-64. Match 2 : Dream 79-65. Match 3 : Dream 97-71. Match 4 : Valkyries 67-62. Match 5 : Valkyries 64-55. Serie 3-2 GSV."
        }
    },
    "es": {
        "soccer": {
            "tagline": "Campanada en la Copa de la Liga: Fleetwood Town de cuarta division elimina a Arsenal en penaltis (5-3).",
            "liveNow": "Drama en cuarta ronda: Fleetwood Town despide a Arsenal 5-3 en penaltis tras 1-1. Miercoles: City vs Brighton, Liverpool vs Chelsea.",
            "pulse": "BOMBAZO EN INGLATERRA: FLEETWOOD TOWN ELIMINA A ARSENAL EN PENALTIS",
            "keywords": "Carabao Cup, Fleetwood Town, Arsenal, tanda de penaltis, cuarta ronda, sorpresa historica"
        },
        "basketball": {
            "tagline": "Valkyries toman ventaja 3-2 en las Finales mientras la NBA arranca con recital de Wembanyama.",
            "liveNow": "Finales WNBA Partido 5: Valkyries 64, Dream 55. Debut NBA: Spurs 130, Kings 103 (Wemby 9 mates); Celtics 125, Nets 124 (Tatum 40 pts).",
            "pulse": "FIESTA DEL BASKET: VALKYRIES MANDAN 3-2 Y LA NBA DESPEGA",
            "keywords": "Finales WNBA, Partido 5, Valkyries, Dream, debut NBA, Wembanyama, Tatum, Spurs"
        },
        "football": {
            "tagline": "Cowboys arrollan a Eagles 38-21 en el MNF: Prescott lanza 3 TD; Packers reciben a Panthers el jueves.",
            "liveNow": "MNF Final: Cowboys 38, Eagles 21 con recital de Prescott. Vikings (6-0) unico invicto. TNF: Panthers en Lambeau Field.",
            "pulse": "GOLPE EN EL MNF: DALLAS VENCE CON CONTUNDENCIA A EAGLES 38-21",
            "keywords": "NFL semana 7, MNF, Cowboys, Eagles, Prescott, semana 8, Packers, Panthers, TNF"
        },
        "tennis": {
            "tagline": "Emocion en Viena: Alcaraz supera a Khachanov en dos mangas y Zverev sobrevive a un tiebreak de 13-11.",
            "liveNow": "Viena R1: Alcaraz vence a Khachanov 6-4, 7-6 (5). Zverev tumba a Landaluce 7-5, 3-6, 7-6 (13-11) salvando bolas de partido.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ Y ZVEREV AVANZAN CON DRAMA EN VIENA",
            "keywords": "ATP, Viena, Erste Bank Open, Alcaraz, Khachanov, Zverev, Landaluce, tiebreak"
        },
        "f1": {
            "tagline": "Cuenta atras en Mexico: Antonelli necesita el noveno puesto en el Hermanos Rodriguez para sellar el titulo.",
            "liveNow": "Ecuacion del campeonato: Antonelli (365 pts) aventaja a Russell en 123. P9 el domingo asegura el titulo mundial 2026.",
            "pulse": "GP DE MEXICO: ANTONELLI ROZA EL TITULO MUNDIAL MAS JOVEN DE LA HISTORIA",
            "keywords": "Formula 1, GP de Mexico, Antonelli, Russell, campeon mundial, Hermanos Rodriguez, Mercedes"
        },
        "golf": {
            "tagline": "Arranque del VidantaWorld Mexico Open: Smotherman traslada a Vallarta la inercia ganadora de Bermudas.",
            "liveNow": "Previa Mexico Open: El circuito llega a VidantaVallarta. Smotherman busca el doblete tras vencer en playoff en Bermudas.",
            "pulse": "FEDEXCUP FALL: ARRANCA EL VIDANTAWORLD MEXICO OPEN EN VALLARTA",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Power, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Mesa del miercoles",
            "tonightBlurb": "Fleetwood Town elimina a Arsenal en penaltis. Valkyries toman ventaja 3-2 en Finales. Cowboys arrollan a Eagles en el MNF.",
            "plTitle": "Milagro en la Copa: Fleetwood Town de cuarta division echa a Arsenal en penaltis",
            "plBlurb": "David Harrington detiene el penalti de Bukayo Saka y Fleetwood empata 1-1 antes de ganar 5-3 desde los once metros en Highbury.",
            "f1Title": "GP de Mexico: Antonelli a las puertas de la gloria mundial",
            "f1Blurb": "Con 123 puntos de ventaja, Kimi Antonelli solo necesita terminar noveno en Mexico para proclamarse el campeon mas joven de la F1."
        },
        "pg": {
            "pinFinal": "Copa de la Liga (pen 5-3): Fleetwood Town 1, Arsenal 1. Heroica tanda de penaltis clasifica al conjunto modesto de League Two.",
            "week1Closed": "NFL Semana 7 MNF final: Cowboys superan con claridad a Eagles 38-21 en Filadelfia",
            "week1Sub": "Prescott lanza 3 TD y Lamb acumula 116 yardas. Vikings (6-0) quedan como unico invicto. Jueves noche: Panthers en Green Bay.",
            "countdownTnf": "TNF Jueves: Panthers (3-4) en casa de Packers (5-2). Victoria contundente de Dallas 38-21 en Filadelfia. Vikings 6-0.",
            "barsPoints": "Diferencia con el lider: Antonelli suma 365, 123 sobre Russell (242). El noveno puesto en Mexico le da el titulo.",
            "tableAfterMonday": "Premier League: City y Arsenal empatados en 21 (7-0-1). Liverpool 15, Chelsea 13. Golpe historico de Fleetwood en copa.",
            "pinClub": "Selecciona un club. City y Arsenal comparten liderato con 21. Fleetwood elimina a Arsenal en la Carabao Cup.",
            "plFootnote": "Martes de copa: Fleetwood Town 1-1 Arsenal (5-3 pen); Bradford 2-0 Peterborough. Miercoles: Man City vs Brighton, Liverpool vs Chelsea.",
            "majorsDone": "Arranque del Mexico Open: Smotherman encabeza la cita de 6 millones en Vidanta tras ganar en playoff en Bermudas.",
            "wnbaFirstRound": "Finales WNBA Partido 5 final: Valkyries vencen 64-55 a Dream con ferrea defensa y toman ventaja de 3-2.",
            "bracketFootnote": "Partido 1: Valkyries 68-64. Partido 2: Dream 79-65. Partido 3: Dream 97-71. Partido 4: Valkyries 67-62. Partido 5: Valkyries 64-55. Serie 3-2 GSV."
        }
    },
    "de": {
        "soccer": {
            "tagline": "Ligapokal-Sensation: Viertligist Fleetwood Town wirft Arsenal mit 5:3 im Elfmeterschießen raus.",
            "liveNow": "Drama im Achtelfinale: Fleetwood Town schlaegt Arsenal 5:3 i.E. nach 1:1. Mittwoch: Man City gegen Brighton, Liverpool gegen Chelsea.",
            "pulse": "POKAL-SENSATION: FLEETWOOD TOWN FEUERT ARSENAL IM ELFMETERSCHIESSEN RAUS",
            "keywords": "Carabao Cup, Fleetwood Town, Arsenal, Elfmeterschießen, Achtelfinale, Sensation"
        },
        "basketball": {
            "tagline": "Valkyries gehen mit 3:2 in Fuehrung, waehrend die NBA mit Wembanyama-Gala eroeffnet.",
            "liveNow": "WNBA Finals Spiel 5: Valkyries 64, Dream 55. NBA-Auftakt: Spurs 130, Kings 103 (Wemby 9 Dunks); Celtics 125, Nets 124 (Tatum 40 Pkt).",
            "pulse": "BASKETBALL-FEUERWERK: VALKYRIES FUEHREN 3:2, NBA STARTET MIT WEMBY-SHOW",
            "keywords": "WNBA Finals, Spiel 5, Valkyries, Dream, NBA-Saisonstart, Wembanyama, Tatum, Spurs"
        },
        "football": {
            "tagline": "Cowboys fegen Eagles mit 38:21 im MNF vom Feld: Prescott wirft 3 TDs; Packers empfangen Panthers.",
            "liveNow": "MNF Final: Cowboys 38, Eagles 21 dank Prescott-Gala. Vikings (6-0) bleiben einziges ungeschlagenes Team. TNF: Panthers bei Packers.",
            "pulse": "MNF-STATEMENT: COWBOYS ZERLEGEN EAGLES MIT 38:21 IN PHILADELPHIA",
            "keywords": "NFL Woche 7, MNF, Cowboys, Eagles, Prescott, Woche 8, Packers, Panthers, TNF"
        },
        "tennis": {
            "tagline": "Wiener Krimi: Alcaraz bezwingt Khachanov in zwei Saetzen, Zverev uebersteht 13:11-Tiebreak-Marathon.",
            "liveNow": "Wien R1: Alcaraz schlaegt Khachanov 6:4, 7:6 (5). Zverev siegt nach Abwehr von Matchbaellen 7:5, 3:6, 7:6 (13:11) gegen Landaluce.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ UND ZVEREV ZIEHEN MIT DRAMA INS ACHTELFINALE",
            "keywords": "ATP, Wien, Erste Bank Open, Alcaraz, Khachanov, Zverev, Landaluce, Tiebreak"
        },
        "f1": {
            "tagline": "Countdown in Mexiko: Antonelli genuegt Platz neun im Autodromo Hermanos Rodriguez zum WM-Titel.",
            "liveNow": "WM-Entscheidung: Antonelli (365 Pkt) fuehrt mit 123 Zaehlern vor Russell. Platz neun am Sonntag sichert den Titel vorzeitig.",
            "pulse": "GP VON MEXIKO: ANTONELLI VOR HISTORISCHER KROENUNG ZUM WELTMEISTER",
            "keywords": "Formel 1, GP von Mexiko, Antonelli, Russell, Weltmeister, Hermanos Rodriguez, Mercedes"
        },
        "golf": {
            "tagline": "Auftakt zur VidantaWorld Mexico Open: Smotherman bringt Bermuda-Schwung mit nach Vallarta.",
            "liveNow": "Vorschau Mexiko: PGA Tour gastiert in VidantaVallarta. Smotherman peilt zweiten Sieg in Folge nach Bermuda-Playoff-Triumph an.",
            "pulse": "FEDEXCUP FALL: VIDANTAWORLD MEXICO OPEN STARTET IN VALLARTA",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Power, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Mittwochs-Desk",
            "tonightBlurb": "Fleetwood Town wirft Arsenal im Elfmeterschießen raus. Valkyries fuehren 3:2. Cowboys siegen im MNF.",
            "plTitle": "Pokal-Wunder: Viertligist Fleetwood Town schlaegt Arsenal im Elfmeterschießen",
            "plBlurb": "David Harrington pariert Elfmeter von Bukayo Saka; Fleetwood trotzt Arsenal ein 1:1 ab und siegt 5:3 i.E. im Highbury Stadium.",
            "f1Title": "GP von Mexiko: Antonelli greift nach dem WM-Titel",
            "f1Blurb": "Mit 123 Punkten Vorsprung reicht Kimi Antonelli in Mexiko Rang neun, um juengster Formel-1-Weltmeister aller Zeiten zu werden."
        },
        "pg": {
            "pinFinal": "Ligapokal (5:3 i.E.): Fleetwood Town 1, Arsenal 1. Viertligist wirft Arsenal in dramatischer Elfmeter-Entscheidung raus.",
            "week1Closed": "NFL Woche 7 MNF final: Cowboys dominieren Eagles 38:21 im Lincoln Financial Field",
            "week1Sub": "Prescott wirft 3 TDs und Lamb verbucht 116 Yards. Vikings (6-0) bleiben ungeschlagen. Donnerstagabend: Panthers bei Packers.",
            "countdownTnf": "TNF Donnerstag: Panthers (3-4) bei Packers (5-2). Cowboys demuetigen Eagles 38:21 im MNF. Vikings stehen 6-0.",
            "barsPoints": "Abstand zum Spitzenreiter: Antonelli 365, 123 vor Russell (242). Platz neun in Mexiko reicht zum Titel.",
            "tableAfterMonday": "Premier League: City und Arsenal gleichauf bei 21 (7-0-1). Liverpool 15, Chelsea 13. Fleetwood schockt Arsenal im Pokal.",
            "pinClub": "Waehlen Sie einen Klub. City und Arsenal fuehren mit 21 Punkten. Fleetwood eliminiert Arsenal im Ligapokal.",
            "plFootnote": "Dienstag im Pokal: Fleetwood Town 1:1 Arsenal (5:3 i.E.); Bradford 2:0 Peterborough. Mittwoch: Man City vs Brighton, Liverpool vs Chelsea.",
            "majorsDone": "Start der Mexico Open: Smotherman fuehrt das 6-Mio-Feld in Vidanta nach seinem Playoff-Erfolg auf Bermuda an.",
            "wnbaFirstRound": "WNBA Finals Spiel 5: Valkyries besiegen Dream 64:55 mit Defensiv-Bollwerk und fuehren 3:2.",
            "bracketFootnote": "Spiel 1: Valkyries 68-64. Spiel 2: Dream 79-65. Spiel 3: Dream 97-71. Spiel 4: Valkyries 67-62. Spiel 5: Valkyries 64-55. Serie 3-2 GSV."
        }
    },
    "it": {
        "soccer": {
            "tagline": "Clamoroso in Carabao Cup: il Fleetwood Town (D4) elimina l'Arsenal ai rigori (5-3) dopo l'1-1.",
            "liveNow": "Quarto turno shock: il Fleetwood Town estromette l'Arsenal ai rigori per 5-3. Mercoledi: Man City-Brighton e Liverpool-Chelsea.",
            "pulse": "SHOCK IN COPPA DI LEGA: IL FLEETWOOD TOWN ELIMINA L'ARSENAL AI RIGORI",
            "keywords": "Carabao Cup, Fleetwood Town, Arsenal, calci di rigore, quarto turno, impresa storica"
        },
        "basketball": {
            "tagline": "Valkyries sul 3-2 nelle Finals mentre l'NBA si accende con lo show da 29 punti di Wembanyama.",
            "liveNow": "Finals WNBA Gara 5: Valkyries 64, Dream 55. Opening NBA: Spurs 130, Kings 103 (Wemby 9 schiacciate); Celtics 125, Nets 124 (Tatum 40 pts).",
            "pulse": "ESPLOSIONE BASKET: VALKYRIES AVANTI 3-2, L'NBA RIPARTE COL BOTTO",
            "keywords": "Finals WNBA, Gara 5, Valkyries, Dream, debutto NBA, Wembanyama, Tatum, Spurs"
        },
        "football": {
            "tagline": "I Cowboys travolgono gli Eagles 38-21 al MNF: Prescott lancia 3 TD; i Packers ospitano Carolina giovedi.",
            "liveNow": "MNF finale: Cowboys 38, Eagles 21 con una prova magistrale di Prescott. Vikings (6-0) soli imbattuti. TNF: Panthers a Green Bay.",
            "pulse": "MNF PERENTORIO: DALLAS ASSEDIATA E VINCITRICE SUGLI EAGLES PER 38-21",
            "keywords": "NFL settimana 7, MNF, Cowboys, Eagles, Prescott, settimana 8, Packers, Panthers, TNF"
        },
        "tennis": {
            "tagline": "Emozioni a Vienna: Alcaraz piega Khachanov in due set, Zverev vince un tiebreak maratona per 13-11.",
            "liveNow": "Vienna R1: Alcaraz batte Khachanov 6-4, 7-6 (5). Zverev supera Landaluce 7-5, 3-6, 7-6 (13-11) annullando match point.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ E ZVEREV AVANZANO AL SECONDO TURNO A VIENNA",
            "keywords": "ATP, Vienna, Erste Bank Open, Alcaraz, Khachanov, Zverev, Landaluce, tiebreak"
        },
        "f1": {
            "tagline": "Verso il GP del Messico: ad Antonelli basta il nono posto all'Hermanos Rodriguez per il Mondiale.",
            "liveNow": "Corsa al titolo: Antonelli (365 pts) ha 123 punti su Russell. Un nono posto domenica assegna la corona piloti 2026.",
            "pulse": "GP DEL MESSICO: ANTONELLI A UN PASSO DAL TITOLO IRIDATO PIU GIOVANE",
            "keywords": "Formula 1, GP del Messico, Antonelli, Russell, campione del mondo, Hermanos Rodriguez, Mercedes"
        },
        "golf": {
            "tagline": "Via al VidantaWorld Mexico Open: Smotherman porta a Vallarta l'entusiasmo della vittoria a Bermuda.",
            "liveNow": "Presentazione Messico: Il tour fa tappa a VidantaVallarta. Smotherman cerca il bis dopo il playoff trionfale a Bermuda.",
            "pulse": "FEDEXCUP FALL: AL VIA IL VIDANTAWORLD MEXICO OPEN A VALLARTA",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Power, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Desk di mercoledi",
            "tonightBlurb": "Il Fleetwood Town elimina l'Arsenal ai rigori. Le Valkyries conducono 3-2 nelle Finals. I Cowboys battono gli Eagles al MNF.",
            "plTitle": "Miracolo in coppa: il Fleetwood Town (D4) elimina l'Arsenal ai calci di rigore",
            "plBlurb": "David Harrington neutralizza il rigore di Bukayo Saka e il Fleetwood pareggia 1-1 prima di imporsi 5-3 dal dischetto ad Highbury.",
            "f1Title": "GP del Messico: Antonelli alle soglie dell'iride",
            "f1Blurb": "Con 123 lunghezze di vantaggio, a Kimi Antonelli basta il nono posto in Messico per laurearsi campione del mondo piu giovane di sempre."
        },
        "pg": {
            "pinFinal": "Coppa di Lega (5-3 d.c.r.): Fleetwood Town 1, Arsenal 1. Gli sfavoriti di quarta divisione estromettono i Gunners.",
            "week1Closed": "NFL Settimana 7 MNF finale: I Cowboys superano con autorita gli Eagles 38-21 a Philadelphia",
            "week1Sub": "Prescott lancia 3 TD e Lamb firma 116 yard. Vikings (6-0) unici imbattuti. Giovedi notte: Panthers a Green Bay.",
            "countdownTnf": "TNF Giovedi: Panthers (3-4) sul campo dei Packers (5-2). Dallas travolge Philadelphia 38-21 al MNF. Vikings 6-0.",
            "barsPoints": "Distacco dal leader: Antonelli 365, 123 punti sopra Russell (242). Il nono posto in Messico vale il titolo.",
            "tableAfterMonday": "Premier League: City e Arsenal appaiate a quota 21 (7-0-1). Liverpool 15, Chelsea 13. Fleetwood clamoroso in coppa.",
            "pinClub": "Seleziona un club. City e Arsenal guidano con 21 punti. Il Fleetwood Town elimina l'Arsenal in Carabao Cup.",
            "plFootnote": "Martedi in coppa: Fleetwood Town 1-1 Arsenal (5-3 d.c.r.); Bradford 2-0 Peterborough. Mercoledi: Man City-Brighton, Liverpool-Chelsea.",
            "majorsDone": "Inizia il Mexico Open: Smotherman guida il field da 6 milioni a Vidanta dopo il trionfo al playoff alle Bermuda.",
            "wnbaFirstRound": "Finals WNBA Gara 5 finale: Valkyries battono Dream 64-55 con una grande difesa e salgono 3-2.",
            "bracketFootnote": "Gara 1: Valkyries 68-64. Gara 2: Dream 79-65. Gara 3: Dream 97-71. Gara 4: Valkyries 67-62. Gara 5: Valkyries 64-55. Serie 3-2 GSV."
        }
    },
    "pl": {
        "soccer": {
            "tagline": "Sensacja w Pucharze Ligi: Czwartoligowe Fleetwood Town eliminuje Arsenal w rzutach karnych (5:3).",
            "liveNow": "Dramat w 4. rundzie: Fleetwood Town pokonuje Arsenal 5:3 w karnych po remisie 1:1. Sroda: Man City z Brighton, Liverpool z Chelsea.",
            "pulse": "SENSACJA W ANGLII: FLEETWOOD TOWN WYRZUCA ARSENAL PO KARNYCH",
            "keywords": "Carabao Cup, Fleetwood Town, Arsenal, rzuty karne, 4. runda, sensacja pucharu"
        },
        "basketball": {
            "tagline": "Valkyries prowadza 3-2 w Finalach, podczas gdy NBA startuje z fajerwerkami Wembanyamy.",
            "liveNow": "Finaly WNBA mecz 5: Valkyries 64, Dream 55. Start NBA: Spurs 130, Kings 103 (Wemby 9 wsadow); Celtics 125, Nets 124 (Tatum 40 pkt).",
            "pulse": "KOSZYKARSKI SZAŁ: VALKYRIES NA PROWADZENIU 3-2, NBA ROZPOCZETA",
            "keywords": "Finaly WNBA, mecz 5, Valkyries, Dream, start NBA, Wembanyama, Tatum, Spurs"
        },
        "football": {
            "tagline": "Cowboys gromia Eagles 38:21 w MNF: Prescott rzuca 3 TD; Packers podejmuja Panthers w czwartek.",
            "liveNow": "MNF final: Cowboys 38, Eagles 21 po koncercie Prescotta. Vikings (6-0) jedyna niepokonana ekipa. TNF: Panthers w Green Bay.",
            "pulse": "POKAZ SILY W MNF: DALLAS ROZBIJA EAGLES 38:21 W FILADELFII",
            "keywords": "NFL tydzien 7, MNF, Cowboys, Eagles, Prescott, tydzien 8, Packers, Panthers, TNF"
        },
        "tennis": {
            "tagline": "Emocje w Wiedniu: Alcaraz ogrywa Chaczanowa w dwoch setach, Zverev wygrywa tiebreak 13:11.",
            "liveNow": "Wieden R1: Alcaraz pokonuje Chaczanowa 6:4, 7:6 (5). Zverev wygrywa z Landaluce 7:5, 3:6, 7:6 (13:11) po obronie pilek meczowych.",
            "pulse": "ERSTE BANK OPEN: ALCARAZ I ZVEREV GRAJA DALEJ PO WIELKICH EMOCJACH",
            "keywords": "ATP, Wieden, Erste Bank Open, Alcaraz, Chaczanow, Zverev, Landaluce, tiebreak"
        },
        "f1": {
            "tagline": "Odliczanie w Meksyku: Antonelli potrzebuje dziewiatego miejsca na Hermanos Rodriguez do tytulu.",
            "liveNow": "Uklad w mistrzostwach: Antonelli (365 pkt) ma 123 pkt przewagi nad Russellem. 9. miejsce w niedziele przypieczetuje tytul.",
            "pulse": "GP MEKSYKU: ANTONELLI NA PROGU NAJMLODSZEGO MISTRZOSTWA SWIATA",
            "keywords": "Formula 1, GP Meksyku, Antonelli, Russell, mistrz swiata, Hermanos Rodriguez, Mercedes"
        },
        "golf": {
            "tagline": "Start VidantaWorld Mexico Open: Smotherman przenosi forme z Bermudow na pole w Vallarcie.",
            "liveNow": "Zapowiedz Meksyku: Tour zjezdza do VidantaVallarta. Smotherman poluje na kolejny triumf po dogrywce na Bermudach.",
            "pulse": "FEDEXCUP FALL: VIDANTAWORLD MEXICO OPEN RUSZA W MEKSYKU",
            "keywords": "PGA Tour, VidantaWorld Mexico Open, Smotherman, Power, VidantaVallarta, FedExCup Fall"
        },
        "home": {
            "tonight": "Srodowe biuro",
            "tonightBlurb": "Fleetwood Town wyrzuca Arsenal po karnych. Valkyries prowadza 3-2 w Finalach. Cowboys gromia Eagles w MNF.",
            "plTitle": "Cud w pucharze: Czwartoligowe Fleetwood Town eliminuje Arsenal w karnych",
            "plBlurb": "David Harrington broni karny Bukayo Saki, a Fleetwood remisuje 1:1 i wygrywa 5:3 w serii jedenastek na Highbury.",
            "f1Title": "GP Meksyku: Antonelli o krok od mistrzostwa swiata",
            "f1Blurb": "Z przewaga 123 punktow Kimi Antonelli potrzebuje zaledwie 9. lokaty w Meksyku, by zostac najmlodszym mistrzem w dziejach F1."
        },
        "pg": {
            "pinFinal": "Puchar Ligi (karne 5:3): Fleetwood Town 1, Arsenal 1. Sensacyjny awans czwartoligowca po rzutach karnych.",
            "week1Closed": "NFL Tydzien 7 MNF final: Cowboys bezdyskusyjnie lepsi od Eagles 38:21 w Filadelfii",
            "week1Sub": "Prescott rzuca 3 TD, a Lamb notuje 116 jardow. Vikings (6-0) jedynym zespolem bez porazki. Czwartek: Panthers u Packers.",
            "countdownTnf": "TNF Czwartek: Panthers (3-4) na terenie Packers (5-2). Dallas dominuje w Filadelfii 38:21. Vikings 6-0.",
            "barsPoints": "Roznica do lidera: Antonelli 365, 123 przed Russellem (242). Dziewiate miejsce w Meksyku daje tytul.",
            "tableAfterMonday": "Premier League: City i Arsenal na czele z 21 pkt (7-0-1). Liverpool 15, Chelsea 13. Szokujace odpadniecie Arsenalu w pucharze.",
            "pinClub": "Wybierz klub. City i Arsenal lideruja z 21 punktami. Fleetwood Town wyrzuca Arsenal z Carabao Cup.",
            "plFootnote": "Wtorek w pucharze: Fleetwood Town 1:1 Arsenal (5:3 karne); Bradford 2:0 Peterborough. Sroda: Man City z Brighton, Liverpool z Chelsea.",
            "majorsDone": "Poczatek Mexico Open: Smotherman na czele turnieju z pula 6 mln dol. po zwycieskiej dogrywce na Bermudach.",
            "wnbaFirstRound": "Finaly WNBA mecz 5 final: Valkyries wygrywaja z Dream 64:55 dzieki zelaznej obronie i obejmuja prowadzenie 3-2.",
            "bracketFootnote": "Mecz 1: Valkyries 68-64. Mecz 2: Dream 79-65. Mecz 3: Dream 97-71. Mecz 4: Valkyries 67-62. Mecz 5: Valkyries 64-55. Seria 3-2 GSV."
        }
    },
    "zh": {
        "soccer": {
            "tagline": "联赛杯惊天冷门：英乙弱旅弗利特伍德点球大战5-3爆冷淘汰阿森纳。",
            "liveNow": "第四轮大戏：弗利特伍德点球5-3淘汰阿森纳。周三战况：曼城对阵布莱顿，利物浦对阵切尔西。",
            "pulse": "联赛杯惊天巨震：英乙弗利特伍德点球绝杀阿森纳",
            "keywords": "联赛杯, 弗利特伍德, 阿森纳, 点球大战, 第四轮, 惊天大冷"
        },
        "basketball": {
            "tagline": "女武神总决赛3-2夺赛点，NBA揭幕战文班亚马29分9扣篮引爆联盟。",
            "liveNow": "WNBA总决赛G5：女武神64-55击败梦想。NBA揭幕战：马刺130-103大胜国王（文班9扣篮），凯尔特人125-124险胜篮网（塔图姆40分）。",
            "pulse": "篮球风暴：女武神总决赛3-2领先，NBA揭幕战文班亚马震撼全场",
            "keywords": "WNBA总决赛, 第五战, 女武神, 梦想, NBA揭幕战, 文班亚马, 塔图姆, 马刺"
        },
        "football": {
            "tagline": "牛仔周一夜赛38-21大胜老鹰：普雷斯科特3达阵，包装工周四迎战黑豹。",
            "liveNow": "MNF战报：牛仔38-21客场击溃老鹰。维京人（6-0）成为联盟唯一不败之师。周四夜赛：黑豹客战包装工。",
            "pulse": "周一夜赛统治力：达拉斯牛仔38-21客场掀翻费城老鹰",
            "keywords": "NFL第七周, MNF, 牛仔, 老鹰, 普雷斯科特, 第八周, 包装工, 黑豹, TNF"
        },
        "tennis": {
            "tagline": "维也纳惊魂：阿尔卡拉斯直落两盘击败哈恰诺夫，兹维列夫抢七13-11史诗险胜。",
            "liveNow": "维也纳首轮：阿尔卡拉斯6-4、7-6(5)力克哈恰诺夫。兹维列夫挽救赛点7-5、3-6、7-6(13-11)险胜兰达鲁塞。",
            "pulse": "维也纳公开赛：阿尔卡拉斯与兹维列夫涉险晋级十六强",
            "keywords": "ATP, 维也纳公开赛, 阿尔卡拉斯, 哈恰诺夫, 兹维列夫, 兰达鲁塞, 抢七"
        },
        "f1": {
            "tagline": "墨西哥城大奖赛倒计时：安东内利在罗德里格斯赛道只需第九名即可提前加冕世界冠军。",
            "liveNow": "争冠局势：安东内利（365分）领先拉塞尔123分。周日正赛获得第九名即可锁定总冠军，安东内利确认2027年保留12号车号。",
            "pulse": "墨西哥大奖赛：安东内利即将加冕F1史上最年轻世界冠军",
            "keywords": "一级方程式, 墨西哥大奖赛, 安东内利, 拉塞尔, 世界冠军, 罗德里格斯赛道, 梅赛德斯"
        },
        "golf": {
            "tagline": "墨西哥公开赛挥杆：斯莫瑟曼携百慕大夺冠之势冲击600万美元秋季赛。",
            "liveNow": "墨西哥前瞻：美巡赛齐聚维丹塔瓦亚塔。斯莫瑟曼在百慕大加洞赛夺冠后力争连冠。",
            "pulse": "联邦快递杯秋季赛：维丹塔世界墨西哥公开赛正式开杆",
            "keywords": "美巡赛, 墨西哥公开赛, 斯莫瑟曼, 鲍尔, 维丹塔瓦亚塔, 联邦快递杯秋季赛"
        },
        "home": {
            "tonight": "周三战报",
            "tonightBlurb": "弗利特伍德点球淘汰阿森纳爆大冷。女武神总决赛3-2夺赛点。牛仔周一夜赛客场大胜老鹰。",
            "plTitle": "联赛杯奇迹：英乙弗利特伍德点球大战淘汰夺冠热门阿森纳",
            "plBlurb": "哈灵顿扑出萨卡点球，英乙黑马1-1战平阿森纳并在点球大战中5-3获胜，创造建队118年历史纪录。",
            "f1Title": "墨西哥大奖赛：安东内利距首座世界冠军奖杯仅一步之遥",
            "f1Blurb": "手握123分领先优势，安东内利在墨西哥城只需取得第九名即可成为F1史上最年轻的年度车手总冠军。"
        },
        "pg": {
            "pinFinal": "联赛杯决战（点球5-3）：弗利特伍德1-1阿森纳。英乙弱旅通过惊心动魄的点球大战爆冷淘汰阿森纳。",
            "week1Closed": "NFL第七周MNF赛果：达拉斯牛仔在林肯金融球场38-21轻取费城老鹰",
            "week1Sub": "普雷斯科特送出3记达阵，兰姆接球破百。维京人（6-0）继续独享不败金身。周四夜赛：黑豹客战包装工。",
            "countdownTnf": "周四夜赛前瞻：黑豹（3-4）挑战包装工（5-2）。牛仔周一38-21客场大胜老鹰。维京人6胜0负独走。",
            "barsPoints": "积分差距：安东内利积365分领先拉塞尔123分。墨西哥正赛进入前九即刻夺冠。",
            "tableAfterMonday": "英超积分榜：曼城与阿森纳同积21分（7胜1负）。利物浦15分，切尔西13分。联赛杯阿森纳爆冷出局。",
            "pinClub": "选择俱乐部查看。曼城与阿森纳并列榜首积21分。弗利特伍德在联赛杯点球淘汰阿森纳。",
            "plFootnote": "周二杯赛：弗利特伍德1-1阿森纳（点球5-3）；布拉德福德2-0彼得伯勒。周三焦点：曼城对布莱顿，利物浦对切尔西。",
            "majorsDone": "墨西哥公开赛启幕：斯莫瑟曼在百慕大第三个加洞夺冠后领衔出战维丹塔600万美元赛事。",
            "wnbaFirstRound": "WNBA总决赛G5终局：女武神依靠末节窒息防守64-55击败梦想，大比分3-2手握赛点。",
            "bracketFootnote": "G1：女武神68-64。G2：梦想79-65。G3：梦想97-71。G4：女武神67-62。G5：女武神64-55。大比分女武神3-2梦想。"
        }
    },
    "ja": {
        "soccer": {
            "tagline": "カラバオ杯の大波乱：4部フリートウッド・タウンがPK戦5-3でアーセナルを撃破。",
            "liveNow": "4回戦の激震：フリートウッドが1-1からのPK戦5-3でアーセナルを下す。水曜：マンチェスターC対ブライトン、リヴァプール対チェルシー。",
            "pulse": "リーグ杯の奇跡：4部フリートウッドがPK戦でアーセナルを沈める",
            "keywords": "カラバオ杯, フリートウッド, アーセナル, PK戦, 4回戦, 歴史的大波乱"
        },
        "basketball": {
            "tagline": "ヴァルキリーズがファイナル3-2で王手、NBA開幕戦でウェンバンヤマが29得点9ダンク。",
            "liveNow": "WNBAファイナル第5戦：ヴァルキリーズ 64-55 ドリーム。NBA開幕戦：スパーズ 130-103 キングス（ウェンビー9ダンク）、セルティックス 125-124 ネッツ（テイタム40得点）。",
            "pulse": "バスケ熱狂：ヴァルキリーズが3-2で王手、NBA開幕でウェンバンヤマ爆発",
            "keywords": "WNBAファイナル, 第5戦, ヴァルキリーズ, ドリーム, NBA開幕戦, ウェンバンヤマ, テイタム, スパーズ"
        },
        "football": {
            "tagline": "カウボーイズがMNFでイーグルスを38-21で圧倒：プレスコット3TD、木曜TNFはパッカーズ対パンサーズ。",
            "liveNow": "MNF試合結果：プレスコットの圧巻采配でカウボーイズが38-21で快勝。バイキングス（6-0）が唯一の全勝。木曜TNF：パンサーズ対パッカーズ。",
            "pulse": "MNF快勝劇：ダラスがフィラデルフィアの地でイーグルスを38-21で撃破",
            "keywords": "NFL第7週, MNF, カウボーイズ, イーグルス, プレスコット, 第8週, パッカーズ, パンサーズ, TNF"
        },
        "tennis": {
            "tagline": "ウィーン激闘：アルカラスがハチャノフにストレート勝ち、ズベレフは13-11のマラソンタイブレークを制す。",
            "liveNow": "ウィーン1回戦：アルカラスがハチャノフを6-4、7-6(5)で下す。ズベレフはマッチポイントをしのぎ7-5、3-6、7-6(13-11)でランダルーチェに逆転勝ち。",
            "pulse": "エルステ・バンク・オープン：アルカラスとズベレフが劇的勝利で16強入り",
            "keywords": "ATP, ウィーン, エルステ・バンク・オープン, アルカラス, ハチャノフ, ズベレフ, ランダルーチェ, タイブレーク"
        },
        "f1": {
            "tagline": "メキシコGP開幕迫る：アントネッリはエルマノス・ロドリゲスで9位以上なら初戴冠。",
            "liveNow": "タイトル争い：アントネッリ（365点）がラッセルに123点リード。日曜の決勝で9位以上に入れば史上最年少王者が確定。2027年もカーナンバー12継続を表明。",
            "pulse": "メキシコGP：アントネッリが史上最年少F1王者戴冠へ王手",
            "keywords": "フォーミュラ1, メキシコGP, アントネッリ, ラッセル, ワールドチャンピオン, エルマノス・ロドリゲス, メルセデス"
        },
        "golf": {
            "tagline": "ヴィダンタ・ワールド・メキシコ・オープン開幕：スモザーマンがバミューダの勢いで賞金600万ドル大会へ挑む。",
            "liveNow": "メキシコ展望：PGAツアーがヴィダンタ・バジャルタに集結。バミューダでの激闘プレーオフを制したスモザーマンが連勝を狙う。",
            "pulse": "フェデックスカップ・フォール：メキシコ・オープンが開幕",
            "keywords": "PGAツアー, メキシコ・オープン, スモザーマン, パワー, ヴィダンタ・バジャルタ, フェデックスカップ・フォール"
        },
        "home": {
            "tonight": "水曜デスク",
            "tonightBlurb": "フリートウッドがPK戦でアーセナルを撃破。ヴァルキリーズがファイナル3-2で王手。カウボーイズがイーグルスに完勝。",
            "plTitle": "カップ戦の奇跡：4部フリートウッド・タウンがPK戦でアーセナルを下す大波乱",
            "plBlurb": "ハリントンがサカのPKを阻止し、1-1の引き分けからPK戦5-3でフリートウッドがクラブ創設118年の歴史的勝利。",
            "f1Title": "メキシコGP：アントネッリが史上最年少王座獲得へ秒読み",
            "f1Blurb": "123点の大差をつけているキミ・アントネッリは、メキシコで9位以上に入れば史上最年少F1王者に輝く。"
        },
        "pg": {
            "pinFinal": "カラバオ杯決着（PK5-3）：フリートウッド 1-1 アーセナル。4部の大番狂わせでアーセナルが敗退。",
            "week1Closed": "NFL第7週MNF試合終了：カウボーイズがリンカーン・フィナンシャル・フィールドでイーグルスを38-21で撃破",
            "week1Sub": "プレスコット3TD、ラム116ヤード。バイキングス（6-0）が唯一無敗。木曜夜：パンサーズ対パッカーズ。",
            "countdownTnf": "木曜TNF展望：パンサーズ（3-4）が敵地でパッカーズ（5-2）と対戦。ダラスがMNFで38-21快勝。バイキングス6勝0敗。",
            "barsPoints": "首位との差：アントネッリ365点、ラッセル（242点）に123点差。メキシコで9位以上なら王座確定。",
            "tableAfterMonday": "プレミア順位表：シティとアーセナルが21点で首位タイ（7勝1敗）。リヴァプール15点、チェルシー13点。カップ戦でアーセナル敗退。",
            "pinClub": "クラブを選択。シティとアーセナルが21点で首位並走。フリートウッドがリーグ杯でアーセナルをPKで撃破。",
            "plFootnote": "火曜カップ戦：フリートウッド 1-1 アーセナル（PK5-3）、ブラッドフォード 2-0 ピーターバラ。水曜：マンチェスターC対ブライトン、リヴァプール対チェルシー。",
            "majorsDone": "メキシコ・オープン開幕：バミューダで3ホールのプレーオフを制したスモザーマンが賞金600万ドル大会を牽引。",
            "wnbaFirstRound": "WNBAファイナル第5戦結果：鉄壁の守備でヴァルキリーズがドリームを64-55で下し、3-2で優勝へ王手。",
            "bracketFootnote": "第1戦：ヴァルキリーズ 68-64。第2戦：ドリーム 79-65。第3戦：ドリーム 97-71。第4戦：ヴァルキリーズ 67-62。第5戦：ヴァルキリーズ 64-55。通算3-2でGSVリード。"
        }
    },
    "ko": {
        "soccer": {
            "tagline": "카라바오컵 대이변: 4부 리그 플리트우드 타운이 승부차기 5-3으로 아스널을 격파.",
            "liveNow": "4라운드 격돌: 플리트우드가 1-1 무승부 후 승부차기 5-3으로 아스널 탈락시킴. 수요일: 맨시티 대 브라이턴, 리버풀 대 첼시.",
            "pulse": "리그컵 대이변: 4부 플리트우드가 승부차기 끝에 아스널 제압",
            "keywords": "카라바오컵, 플리트우드 타운, 아스널, 승부차기, 4라운드, 대이변"
        },
        "basketball": {
            "tagline": "발키리스 파이널 3-2 리드, NBA 개막전에서 웸반야마 29득점 9덩크 폭발.",
            "liveNow": "WNBA 파이널 5차전: 발키리스 64-55 드림. NBA 개막전: 스퍼스 130-103 킹스(웸비 9덩크), 셀틱스 125-124 네츠(테이텀 40득점).",
            "pulse": "농구 열풍: 발키리스 파이널 3-2 우세, NBA 개막 웸반야마 대폭발",
            "keywords": "WNBA 파이널, 5차전, 발키리스, 드림, NBA 개막전, 웸반야마, 테이텀, 스퍼스"
        },
        "football": {
            "tagline": "카우보이스 MNF서 이글스 38-21 완파: 프레스콧 3TD, 목요일 TNF는 패커스 대 팬서스.",
            "liveNow": "MNF 최종: 프레스콧의 맹활약 속에 카우보이스가 38-21로 승리. 바이킹스(6-0) 단독 무패. TNF: 팬서스 대 패커스.",
            "pulse": "MNF 완승: 댈러스 카우보이스, 필라델피아에서 이글스 38-21 격파",
            "keywords": "NFL 7주차, MNF, 카우보이스, 이글스, 프레스콧, 8주차, 패커스, 팬서스, TNF"
        },
        "tennis": {
            "tagline": "빈 오픈 격전: 알카라스 하차노프에 완승, 츠베레프는 13-11 타이ブレーク 끝 대역전승.",
            "liveNow": "빈 1회전: 알카라스가 하차노프를 6-4, 7-6(5)으로 제압. 츠베레프는 매치포인트를 극복하고 7-5, 3-6, 7-6(13-11)로 린다루세 꺾어.",
            "pulse": "에르스테 방크 오픈: 알카라스와 츠베레프, 명승부 끝 16강 진출",
            "keywords": "ATP, 빈 오픈, 에르스테 방크 오픈, 알카라스, 하차노프, 츠베레프, 린다루세, 타이브레이크"
        },
        "f1": {
            "tagline": "멕시코시티 GP 카운트다운: 안토넬리 에르마노스 로드리게스서 9위만 해도 조기 챔피언 확정.",
            "liveNow": "타이틀 방정식: 안토넬리(365점)가 러셀에 123점 앞서. 일요일 결선 9위 이상이면 사상 최연소 월드 챔피언 등극. 2027년 12번 유지 발표.",
            "pulse": "멕시코 GP: 안토넬리, F1 역대 최연소 월드 챔피언 등극 초읽기",
            "keywords": "포뮬러 1, 멕시코 GP, 안토넬리, 러셀, 월드 챔피언, 에르마노스 로드리게스, 메르세데스"
        },
        "golf": {
            "tagline": "비단타월드 멕시코 오픈 개막: 스머더먼 버뮤다 우승 기세 몰아 600만 달러 대회 출격.",
            "liveNow": "멕시코 프리뷰: PGA 투어가 비단타바야르타에 집결. 버뮤다 연장 접전 끝 우승한 스머더먼이 2연승 도전.",
            "pulse": "페덱스컵 폴: 비단타월드 멕시코 오픈 공식 티오프",
            "keywords": "PGA 투어, 멕시코 오픈, 스머더먼, 파워, 비단타바야르타, 페덱스컵 폴"
        },
        "home": {
            "tonight": "수요일 데스크",
            "tonightBlurb": "플리트우드가 승부차기로 아스널 제압. 발키리스 파이널 3-2 리드. 카우보이스 MNF서 이글스 완파.",
            "plTitle": "리그컵 기적: 4부 플리트우드 타운이 아스널을 승부차기로 탈락시키는 대이변",
            "plBlurb": "해링턴 골키퍼가 사카의 킥을 막아내며 1-1 무승부 끝에 플리트우드가 5-3 승부차기 승리로 118년 구단 역사상 첫 8강 진출.",
            "f1Title": "멕시코 GP: 안토넬리 사상 최연소 챔피언 등극 눈앞",
            "f1Blurb": "123점 리드를 지닌 키미 안토넬리는 멕시코시티에서 9위 안에만 들면 F1 역사상 최연소 월드 챔피언에 오른다."
        },
        "pg": {
            "pinFinal": "카라바오컵 결과(승부차기 5-3): 플리트우드 1-1 아스널. 4부 리그의 기적적인 승부차기 승리로 아스널 탈락.",
            "week1Closed": "NFL 7주차 MNF 결과: 카우보이스가 링컨 파이낸셜 필드에서 이글스를 38-21로 격파",
            "week1Sub": "프레스콧 3TD, 램 116야드. 바이킹스(6-0) 단독 무패 질주. 목요일 밤: 팬서스 대 패커스.",
            "countdownTnf": "목요일 TNF 프리뷰: 팬서스(3-4)가 패커스(5-2) 원정에 나섭니다. 카우보이스가 MNF서 38-21 완승. 바이킹스 6승 무패.",
            "barsPoints": "선두와의 격차: 안토넬리 365점, 러셀(242점)에 123점 앞서. 멕시코에서 9위면 타이틀 확정.",
            "tableAfterMonday": "프리미어리그 순위: 맨시티와 아스널이 승점 21점으로 공동 선두(7승 1패). 리버풀 15점, 첼시 13점. 아스널 컵대회 탈락.",
            "pinClub": "클럽을 선택하세요. 맨시티와 아스널 승점 21로 공동 선두. 플리트우드가 카라바오컵에서 아스널을 꺾음.",
            "plFootnote": "화요일 컵대회: 플리트우드 1-1 아스널(승부차기 5-3), 브래드퍼드 2-0 피터버러. 수요일: 맨시티 대 브라이턴, 리버풀 대 첼시.",
            "majorsDone": "멕시코 오픈 개막: 버뮤다 연장전서 우승한 스머더먼이 비단타 600만 달러 대회 출전.",
            "wnbaFirstRound": "WNBA 파이널 5차전 최종: 질식 수비 앞세운 발키리스가 드림을 64-55로 꺾고 3-2로 앞서.",
            "bracketFootnote": "1차전: 발키리스 68-64. 2차전: 드림 79-65. 3차전: 드림 97-71. 4차전: 발키리스 67-62. 5차전: 발키리스 64-55. 골든스테이트 3-2 우세."
        }
    },
    "ar": {
        "soccer": {
            "tagline": "مفاجأة مدوية في كأس الرابطة: فليتوود تاون من الدرجة الرابعة يقصي أرسنال بركلات الترجيح 5-3 بعد التعادل 1-1.",
            "liveNow": "إثارة الدور الرابع: فليتوود يقصي أرسنال بركلات الترجيح 5-3. مباريات الأربعاء: مانشستر سيتي ضد برايتون، ليفربول ضد تشيلسي.",
            "pulse": "زلزال في كأس الرابطة: فليتوود يقهر أرسنال بركلات الترجيح",
            "keywords": "كأس الرابطة, فليتوود تاون, أرسنال, ركلات الترجيح, الدور الرابع, مفاجأة تاريخية"
        },
        "basketball": {
            "tagline": "فالكيريز يتقدمون 3-2 في النهائي، وموسم الرابطة الوطنية ينطلق بإبداع ويمبانياما و29 نقطة.",
            "liveNow": "نهائي السيدات المباراة 5: فالكيريز 64، دريم 55. افتتاح الرجال: سبيرز 130، كينغز 103 (ويمبي 9 دنك)؛ سيلتكس 125، نتس 124 (تاتوم 40 نقطة).",
            "pulse": "إثارة السلة: فالكيريز على بعد خطوة من اللقب وضربة بداية نارية للرجال",
            "keywords": "نهائي السيدات, المباراة 5, فالكيريز, دريم, افتتاح السلة, ويمبانياما, تاتوم, سبيرز"
        },
        "football": {
            "tagline": "كاوبويز يسحقون إيغلز 38-21 في ليلة الاثنين: بريسكوت يرمي 3 تمريرات حاسمة، وباكرز يستضيفون بانثرز الخميس.",
            "liveNow": "نهائي ليلة الاثنين: كاوبويز 38، إيغلز 21 بعزف منفرد من بريسكوت. فايكنغز (6-0) بلا هزيمة. ليلة الخميس: بانثرز ضد باكرز.",
            "pulse": "عرض القوة في ليلة الاثنين: دالاس يكتسح فيلادلفيا 38-21",
            "keywords": "دوري كرة القدم الأمريكية, الأسبوع 7, كاوبويز, إيغلز, بريسكوت, الأسبوع 8, باكرز, بانثرز"
        },
        "tennis": {
            "tagline": "إثارة فيينا: ألكاراز يجتاز خاتشانوف بمجموعتين نظيفتين، وزفيريف ينجو في شوط كسر التعادل 13-11.",
            "liveNow": "فيينا الدور الأول: ألكاراز يهزم خاتشانوف 6-4 و7-6(5). زفيريف يتجاوز لاندالوس 7-5 و3-6 و7-6(13-11) بعد إنقاذ كرات حاسمة.",
            "pulse": "بطولة فيينا: ألكاراز وزفيريف يعبران عقبة الدور الأول بصعوبة",
            "keywords": "تنس, فيينا, ألكاراز, خاتشانوف, زفيريف, لاندالوس, كسر التعادل"
        },
        "f1": {
            "tagline": "العد التنازلي لجائزة المكسيك: أنتونيللي بحاجة للمركز التاسع في هيرمانوس رودريغيز لحسم اللقب العالمي.",
            "liveNow": "معادلة البطولة: أنتونيللي (365 نقطة) يتقدم بفارق 123 نقطة على راسل. المركز التاسع يوم الأحد يضمن له التتويج التاريخي.",
            "pulse": "جائزة المكسيك: أنتونيللي على أبواب التتويج كأصغر بطل في تاريخ الفورمولا 1",
            "keywords": "فورمولا 1, جائزة المكسيك, أنتونيللي, راسل, بطل العالم, هيرمانوس رودريغيز, مرسيدس"
        },
        "golf": {
            "tagline": "انطلاق بطولة المكسيك المفتوحة: سموذر مان يدخل المنافسات بزخم تتويجه الدرامي في برمودا.",
            "liveNow": "نظرة على بطولة المكسيك: نجوم الجولف يجتمعون في فيدانتا فايارتا. سموذر مان يطمح لتحقيق لقبه الثاني تواليا بجوائز 6 ملايين دولار.",
            "pulse": "جولة الخريف: انطلاق بطولة فيدانتا وورلد المكسيك المفتوحة",
            "keywords": "جولة بي جي إيه, بطولة المكسيك المفتوحة, سموذر مان, باور, فيدانتا فايارتا, جولة الخريف"
        },
        "home": {
            "tonight": "مكتب الأربعاء",
            "tonightBlurb": "فليتوود تاون يقصي أرسنال بركلات الترجيح. فالكيريز يتقدمون 3-2 في النهائي. كاوبويز يسحقون إيغلز في ليلة الاثنين.",
            "plTitle": "معجزة كأس الرابطة: فليتوود تاون من الدرجة الرابعة يقصي أرسنال بركلات الترجيح",
            "plBlurb": "ديفيد هارينغتون يتصدى لركلة بوكايو ساكا ليفوز فليتوود بركلات الترجيح 5-3 بعد التعادل 1-1 في ملعب هايبوري.",
            "f1Title": "جائزة المكسيك: أنتونيللي على عتبة اللقب العالمي",
            "f1Blurb": "بفارق 123 نقطة، يحتاج كيمي أنتونيللي فقط إلى المركز التاسع في المكسيك ليصبح أصغر بطل عالمي في تاريخ فورمولا 1."
        },
        "pg": {
            "pinFinal": "كأس الرابطة (ترجيح 5-3): فليتوود تاون 1، أرسنال 1. فريق الدرجة الرابعة يقصي أرسنال في ملحمة ركلات الجزاء.",
            "week1Closed": "نهائي ليلة الاثنين: كاوبويز يهزمون إيغلز 38-21 في ملعب لينكون فاينانشال فيلد",
            "week1Sub": "بريسكوت يمرر 3 لمسات هبوط ولامب يسجل 116 ياردة. فايكنغز (6-0) الفريق الوحيد بدون هزيمة. ليلة الخميس: بانثرز ضد باكرز.",
            "countdownTnf": "ليلة الخميس: بانثرز (3-4) في ضيافة باكرز (5-2). دالاس يسحق فيلادلفيا 38-21. فايكنغز يتصدر بسجل 6-0.",
            "barsPoints": "الفارق مع المتصدر: أنتونيللي 365 نقطة، بفارق 123 أمام راسل (242). المركز التاسع في المكسيك يحسم اللقب.",
            "tableAfterMonday": "ترتيب الدوري الإنجليزي: سيتي وأرسنال في الصدارة بـ 21 نقطة (7 انتصارات وهزيمة). ليفربول 15، تشيلسي 13. خروج صادم لأرسنال من الكأس.",
            "pinClub": "اختر ناديا. سيتي وأرسنال يتقاسمان الصدارة بـ 21 نقطة. فليتوود يقصي أرسنال من كأس الرابطة.",
            "plFootnote": "مباريات الكأس يوم الثلاثاء: فليتوود 1-1 أرسنال (5-3 ترجيح)؛ برادفورد 2-0 بيتربورو. الأربعاء: مان سيتي ضد برايتون، ليفربول ضد تشيلسي.",
            "majorsDone": "انطلاق بطولة المكسيك المفتوحة: سموذر مان يتصدر المنافسة بجوائز 6 ملايين دولار بعد فوزه الدرامي في برمودا.",
            "wnbaFirstRound": "نهائي السيدات المباراة 5: فالكيريز يهزمون دريم 64-55 بفضل دفاع حديدي ويتقدمون 3-2 في السلسلة.",
            "bracketFootnote": "المباراة 1: فالكيريز 68-64. المباراة 2: دريم 79-65. المباراة 3: دريم 97-71. المباراة 4: فالكيريز 67-62. المباراة 5: فالكيريز 64-55. النتيجة 3-2 لصالح فالكيريز."
        }
    }
}

# Validation: ensure no em-dash and no double-hyphen in any translation
for lang, sections in DATA.items():
    for sec_name, sec_dict in sections.items():
        for k, text in sec_dict.items():
            assert "—" not in text, f"Em-dash found in {lang}.{sec_name}.{k}: {text}"
            assert "--" not in text, f"Double-hyphen found in {lang}.{sec_name}.{k}: {text}"

print("Validation passed: No em-dashes or double-hyphens found in DATA dictionary.")

# 1. Update frontend/src/i18n/playground.ts
pg_file = "frontend/src/i18n/playground.ts"
with open(pg_file, "r", encoding="utf-8") as f:
    pg_content = f.read()

for lang in DATA:
    pg_data = DATA[lang]["pg"]
    pattern = rf'("{lang}":\s*\{{)([\s\S]*?)(^\s*\}},?)'
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

print("All locale updates for 28 Oct 2026 completed successfully!")
