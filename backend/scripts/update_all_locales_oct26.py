# -*- coding: utf-8 -*-
import re
import os

DATA = {
    "en": {
        "f1": {
            "tagline": "World Champion Antonelli: Italian teenager wins United States GP from pole to seal 2026 title.",
            "liveNow": "Austin GP Final: Antonelli wins ahead of Leclerc and Verstappen. Russell P8 clinches title for Antonelli with 123-point lead.",
            "pulse": "WORLD CHAMPION: ANTONELLI SEALS 2026 TITLE AT COTA",
            "keywords": "Formula 1, United States GP, Austin, COTA, Antonelli, World Champion, Verstappen, Leclerc"
        },
        "basketball": {
            "tagline": "WNBA Finals Game 5 tonight: Valkyries and Dream clash at Chase Center in winner-take-all decider.",
            "liveNow": "Tonight 20:00 ET / 17:00 PT: Game 5 in San Francisco. Series tied 2-2 after Valkyries 67-62 road stunner in Game 4.",
            "pulse": "WNBA FINALS DECIDER: GAME 5 TONIGHT IN SAN FRANCISCO",
            "keywords": "WNBA Finals, Game 5, Valkyries, Dream, Williams, Reese, Chase Center, decider"
        },
        "football": {
            "tagline": "NFL Week 7 Sunday shocks: Seahawks topple Chiefs 20-3, Falcons beat 49ers 29-20; Vikings stand alone at 6-0.",
            "liveNow": "Sunday finals: Seahawks 20, Chiefs 3; Falcons 29, 49ers 20; Vikings 16, Colts 10. Tonight: Cowboys (2-4) at Eagles (2-4) on MNF.",
            "pulse": "UPSET SUNDAY: VIKINGS LONE UNBEATEN AS CHIEFS AND 49ERS FALL",
            "keywords": "NFL Week 7, Chiefs, 49ers, Vikings, Seahawks, Falcons, Cowboys, Eagles, MNF"
        },
        "soccer": {
            "tagline": "Premier League MW8 wrap: Bournemouth stun Man United 3-0 at Old Trafford; Liverpool top Brighton 2-0.",
            "liveNow": "MW8 Sunday: Bournemouth 3, Man United 0; Liverpool 2, Brighton 0; Newcastle 2, Palace 0. Man City and Arsenal top table on 21 pts.",
            "pulse": "PREMIER LEAGUE: BOURNEMOUTH ROUT MAN UNITED AT OLD TRAFFORD",
            "keywords": "Premier League, Bournemouth, Man United, Liverpool, Arsenal, Man City, MW8"
        },
        "golf": {
            "tagline": "Bermuda playoff thriller: Austin Smotherman outlasts Seamus Power on third extra hole for second victory in a month.",
            "liveNow": "Bermuda Final: Smotherman pars 16th on 3rd playoff hole to defeat Power after 54-hole tie at 16 under. Conners T3 at -14.",
            "pulse": "PORT ROYAL PLAYOFF: SMOTHERMAN CLAIMS BERMUDA TITLE",
            "keywords": "PGA Tour, Bermuda, Port Royal, Smotherman, Power, Playoff, Champion"
        },
        "tennis": {
            "tagline": "ATP 500 swing opens in Vienna and Basel: Alcaraz meets Khachanov while Almaty champion Medvedev enters draw.",
            "liveNow": "Monday Round 1: Erste Bank Open in Vienna and Swiss Indoors in Basel underway. Alcaraz, Zverev and Medvedev headline.",
            "pulse": "INDOOR SWING: VIENNA AND BASEL LAUNCH ATP 500 WEEK",
            "keywords": "ATP, Vienna, Basel, Alcaraz, Khachanov, Medvedev, Zverev, Erste Bank Open"
        },
        "home": {
            "tonight": "Monday desk",
            "tonightBlurb": "Antonelli crowned World Champion at COTA. WNBA Finals Game 5 decider in San Francisco. Chiefs and 49ers fall on upset Sunday.",
            "plTitle": "Premier League: Bournemouth stun Man United 3-0 at Old Trafford as MW8 concludes",
            "plBlurb": "Cherries take historic 3-0 victory at Old Trafford. Liverpool top Brighton 2-0 to climb third behind joint-leaders City and Arsenal.",
            "f1Title": "United States GP: Antonelli crowned World Champion",
            "f1Blurb": "Kimi Antonelli wins from pole at COTA. With Russell in eighth, the 20-year-old Italian mathematically seals the 2026 Drivers' World Championship."
        },
        "pg": {
            "pinFinal": "Austin GP Final: Antonelli wins ahead of Leclerc and Verstappen. Russell P8 clinches 2026 World Championship for Antonelli.",
            "week1Closed": "NFL Week 7 SNF final: Seahawks stun Chiefs 20-3 at Lumen Field",
            "week1Sub": "Seattle defense holds Mahomes without a TD. Falcons beat 49ers 29-20. Vikings (6-0) stand as lone unbeaten. Tonight: Cowboys at Eagles.",
            "countdownTnf": "MNF Tonight: Cowboys (2-4) at Eagles (2-4). Chiefs and 49ers handed first losses on Sunday. Vikings stand 6-0.",
            "barsPoints": "Bars show the gap to the leader. Antonelli has 365, 123 ahead of Russell on 242. Antonelli crowned 2026 World Champion.",
            "tableAfterMonday": "Premier League: City and Arsenal tied on 21 (7-0-1). Liverpool 15, Chelsea 13, Bournemouth 13. United down on 10.",
            "pinClub": "Select a club. City and Arsenal are 7-0-1 on 21. Liverpool 15, Bournemouth 13. Bournemouth won 3-0 at Old Trafford.",
            "plFootnote": "Sunday: Bournemouth 3, Man United 0; Liverpool 2, Brighton 0; Newcastle 2, Palace 0. Saturday: Spurs 2, Chelsea 0; Villa 2, City 1.",
            "majorsDone": "Butterfield Bermuda Final: Austin Smotherman defeated Seamus Power on the 3rd playoff hole at Port Royal to win the championship.",
            "wnbaFirstRound": "WNBA Finals Game 5 tonight: Valkyries host Dream at Chase Center with series tied 2-2. Winner takes the WNBA crown.",
            "bracketFootnote": "Game 1: Valkyries 68-64. Game 2: Dream 79-65. Game 3: Dream 97-71. Game 4: Valkyries 67-62. Game 5 tonight in San Francisco."
        }
    },
    "fr": {
        "f1": {
            "tagline": "Antonelli champion du monde : le prodige italien s'impose depuis la pole au COTA et scelle le titre 2026.",
            "liveNow": "GP d'Austin final : Antonelli s'impose devant Leclerc et Verstappen. Russell P8 permet le sacre d'Antonelli avec 123 points d'avance.",
            "pulse": "CHAMPION DU MONDE : ANTONELLI SACRE AU COTA EN 2026",
            "keywords": "Formule 1, GP des Etats-Unis, Austin, COTA, Antonelli, champion du monde, Verstappen, Leclerc"
        },
        "basketball": {
            "tagline": "Finales WNBA match 5 ce soir : les Valkyries et le Dream s'affrontent au Chase Center dans le choc decisif.",
            "liveNow": "Ce soir a San Francisco : match 5 couperet. Egalite 2-2 apres le triomphe 67-62 des Valkyries a Atlanta lors du match 4.",
            "pulse": "FINALES WNBA : MATCH 5 DECISIF CE SOIR A SAN FRANCISCO",
            "keywords": "WNBA Finales, match 5, Valkyries, Dream, Williams, Reese, Chase Center, match decisif"
        },
        "football": {
            "tagline": "Dimanche de surprises en NFL : les Seahawks domptent les Chiefs 20-3, les 49ers battus par Atlanta, Minnesota seul invaincu a 6-0.",
            "liveNow": "Finales dimanche : Seahawks 20, Chiefs 3 ; Falcons 29, 49ers 20 ; Vikings 16, Colts 10. Ce soir : Cowboys chez les Eagles au MNF.",
            "pulse": "DIMANCHE FOU : LES VIKINGS SEULS INVAINCUS, LES CHIEFS ET 49ERS CHUTENT",
            "keywords": "NFL semaine 7, Chiefs, 49ers, Vikings, Seahawks, Falcons, Cowboys, Eagles, MNF"
        },
        "soccer": {
            "tagline": "Bilan de la 8e journee : Bournemouth humilie Manchester United 3-0 a Old Trafford, Liverpool bat Brighton 2-0.",
            "liveNow": "Dimanche : Bournemouth 3, Man United 0 ; Liverpool 2, Brighton 0 ; Newcastle 2, Palace 0. City et Arsenal en tete a 21 pts.",
            "pulse": "PREMIER LEAGUE : BOURNEMOUTH CORRIGE MANCHESTER UNITED A OLD TRAFFORD",
            "keywords": "Premier League, Bournemouth, Man United, Liverpool, Arsenal, Man City, 8e journee"
        },
        "golf": {
            "tagline": "Suspense aux Bermudes : Austin Smotherman bat Seamus Power au 3e trou de playoff et s'offre un deuxieme succes en un mois.",
            "liveNow": "Bermudes final : Smotherman rentre le par au 16 apres une egalite a 54 trous (-16) face a Power. Conners T3 a -14.",
            "pulse": "PLAYOFF A PORT ROYAL : SMOTHERMAN SACRE AUX BERMUDES",
            "keywords": "PGA Tour, Bermudes, Port Royal, Smotherman, Power, playoff, champion"
        },
        "tennis": {
            "tagline": "La tournee indoor ATP 500 s'ouvre a Vienne et Bâle : Alcaraz defie Khachanov, Medvedev en lice.",
            "liveNow": "Lundi 1er tour : coup d'envoi a Vienne et Bâle. Alcaraz, Zverev et le champion d'Almaty Medvedev sur les courts.",
            "pulse": "CIRCUIT INDOOR : VIENNE ET BÂLE LANCENT LA SEMAINE ATP 500",
            "keywords": "ATP, Vienne, Bâle, Alcaraz, Khachanov, Medvedev, Zverev, Erste Bank Open"
        },
        "home": {
            "tonight": "Desk du lundi",
            "tonightBlurb": "Antonelli couronne champion du monde au COTA. Match 5 decisif des finales WNBA a San Francisco. Chute des invaincus en NFL.",
            "plTitle": "Premier League : Bournemouth surprend Manchester United 3-0 a Old Trafford",
            "plBlurb": "Succes retentissant de Bournemouth a Old Trafford. Liverpool domine Brighton 2-0 et s'installe a la 3e place derriere City et Arsenal.",
            "f1Title": "GP des Etats-Unis : Antonelli champion du monde",
            "f1Blurb": "Victoire depuis la pole pour Kimi Antonelli au COTA. Avec Russell huitieme, l'Italien scelle mathematiquement le titre mondial 2026."
        },
        "pg": {
            "pinFinal": "GP d'Austin final : Antonelli s'impose devant Leclerc et Verstappen. Russell P8 offre le titre mondial a Antonelli.",
            "week1Closed": "NFL SNF final : les Seahawks corrigent les Chiefs 20-3 a Lumen Field",
            "week1Sub": "La defense de Seattle prive Mahomes de touchdown. Falcons 29, 49ers 20. Vikings seuls a 6-0. Ce soir : Cowboys a Philadelphie.",
            "countdownTnf": "MNF ce soir : Cowboys (2-4) chez les Eagles (2-4). Chiefs et 49ers ont perdu dimanche. Les Vikings restent a 6-0.",
            "barsPoints": "L'ecart avec le leader. Antonelli compte 365 pts, 123 d'avance sur Russell (242). Antonelli est champion du monde.",
            "tableAfterMonday": "Premier League : City et Arsenal en tete a 21 (7-0-1). Liverpool 15, Chelsea et Bournemouth 13. United a 10.",
            "pinClub": "Choisissez un club. City et Arsenal ont 21 pts. Liverpool 15, Bournemouth 13. Bournemouth a gagne 3-0 a Old Trafford.",
            "plFootnote": "Dimanche : Bournemouth 3, Man United 0 ; Liverpool 2, Brighton 0. Samedi : Spurs 2, Chelsea 0 ; Villa 2, City 1.",
            "majorsDone": "Bermudes final : Austin Smotherman a battu Seamus Power au 3e trou de barrage pour enlever le trophee.",
            "wnbaFirstRound": "Finales WNBA match 5 ce soir : les Valkyries recoivent le Dream a Chase Center a 2-2. Le titre au bout du suspense.",
            "bracketFootnote": "Match 1 : Valkyries 68-64. Match 2 : Dream 79-65. Match 3 : Dream 97-71. Match 4 : Valkyries 67-62. Match 5 ce soir."
        }
    },
    "es": {
        "f1": {
            "tagline": "Antonelli campeon del mundo: el prodigio italiano gana el GP de Estados Unidos desde la pole y asegura el titulo 2026.",
            "liveNow": "Final en Austin: Antonelli vence ante Leclerc y Verstappen. Russell P8 sella la corona para Antonelli con 123 puntos de ventaja.",
            "pulse": "CAMPEON DEL MUNDO: ANTONELLI SE CORONA EN EL COTA",
            "keywords": "Formula 1, GP de Estados Unidos, Austin, COTA, Antonelli, campeon del mundo, Verstappen, Leclerc"
        },
        "basketball": {
            "tagline": "Juego 5 de las Finales WNBA esta noche: Valkyries y Dream chocan en el Chase Center por la gloria definitiva.",
            "liveNow": "Esta noche en San Francisco: quinto juego definitivo. Serie empatada 2-2 tras el triunfo 67-62 de Valkyries en el Juego 4.",
            "pulse": "DECISION DE LAS FINALES WNBA: JUEGO 5 ESTA NOCHE EN SAN FRANCISCO",
            "keywords": "Finales WNBA, Juego 5, Valkyries, Dream, Williams, Reese, Chase Center, juego definitivo"
        },
        "football": {
            "tagline": "Domingo de sorpresas en la NFL: Seahawks doblegan 20-3 a Chiefs, Falcons baten a 49ers y Vikings quedan solos e invictos con 6-0.",
            "liveNow": "Resultados domingo: Seahawks 20, Chiefs 3; Falcons 29, 49ers 20; Vikings 16, Colts 10. Esta noche: Cowboys en Philadelphia en el MNF.",
            "pulse": "DOMINGO DE SORPRESAS: VIKINGS SOLOS E INVICTOS AL CAER CHIEFS Y 49ERS",
            "keywords": "NFL Semana 7, Chiefs, 49ers, Vikings, Seahawks, Falcons, Cowboys, Eagles, MNF"
        },
        "soccer": {
            "tagline": "Cierre de la jornada 8: Bournemouth golea 3-0 al Manchester United en Old Trafford y Liverpool supera 2-0 a Brighton.",
            "liveNow": "Domingo: Bournemouth 3, Man United 0; Liverpool 2, Brighton 0; Newcastle 2, Palace 0. Man City y Arsenal lideran con 21 pts.",
            "pulse": "PREMIER LEAGUE: BOURNEMOUTH APLASTA AL MAN UNITED EN OLD TRAFFORD",
            "keywords": "Premier League, Bournemouth, Man United, Liverpool, Arsenal, Man City, jornada 8"
        },
        "golf": {
            "tagline": "Dramatico desempate en Bermudas: Austin Smotherman vence a Seamus Power en el tercer hoyo extra para su segundo triunfo en un mes.",
            "liveNow": "Final Bermudas: Smotherman hace par en el 16 para batir a Power tras igualar a 16 bajo par en 54 hoyos. Conners T3 con -14.",
            "pulse": "DESEMPATE EN PORT ROYAL: SMOTHERMAN CAMPEON EN BERMUDAS",
            "keywords": "PGA Tour, Bermudas, Port Royal, Smotherman, Power, desempate, campeon"
        },
        "tennis": {
            "tagline": "Arranca la gira bajo techo ATP 500 en Viena y Basilea: Alcaraz ante Khachanov y Medvedev listo para competir.",
            "liveNow": "Lunes primera ronda: Erste Bank Open de Viena y Swiss Indoors de Basilea en marcha con Alcaraz, Zverev y Medvedev.",
            "pulse": "GIRA INDOOR: VIENA Y BASILEA ABREN LA SEMANA ATP 500",
            "keywords": "ATP, Viena, Basilea, Alcaraz, Khachanov, Medvedev, Zverev, Erste Bank Open"
        },
        "home": {
            "tonight": "Mesa del lunes",
            "tonightBlurb": "Antonelli consagrado campeon mundial en COTA. Quinto partido definitivo de las Finales WNBA. Caida de invictos en la NFL.",
            "plTitle": "Premier League: Bournemouth golea 3-0 a Manchester United en Old Trafford",
            "plBlurb": "Campanada historica de Bournemouth en Old Trafford. Liverpool vence 2-0 a Brighton y sube al tercer puesto tras City y Arsenal.",
            "f1Title": "GP de Estados Unidos: Antonelli campeon del mundo",
            "f1Blurb": "Victoria de punta a punta para Kimi Antonelli en COTA. Con Russell octavo, el italiano sella matematicamente el titulo mundial 2026."
        },
        "pg": {
            "pinFinal": "Final Austin: Antonelli gana ante Leclerc y Verstappen. Russell P8 asegura el campeonato mundial para Antonelli.",
            "week1Closed": "NFL SNF final: Seahawks sorprenden 20-3 a Chiefs en Lumen Field",
            "week1Sub": "Defensa de Seattle frena a Mahomes sin anotacion. Falcons 29, 49ers 20. Vikings quedan 6-0. Esta noche: Cowboys en Eagles.",
            "countdownTnf": "MNF esta noche: Cowboys (2-4) ante Eagles (2-4). Chiefs y 49ers cayeron el domingo. Vikings marchan 6-0.",
            "barsPoints": "Diferencia con el lider. Antonelli suma 365 pts, 123 mas que Russell (242). Antonelli es campeon mundial de F1.",
            "tableAfterMonday": "Premier League: City y Arsenal empatados en 21 (7-0-1). Liverpool 15, Chelsea y Bournemouth 13. United con 10.",
            "pinClub": "Elija un club. City y Arsenal lideran con 21. Liverpool 15, Bournemouth 13. Bournemouth vencio 3-0 en Old Trafford.",
            "plFootnote": "Domingo: Bournemouth 3, Man United 0; Liverpool 2, Brighton 0. Sabado: Spurs 2, Chelsea 0; Villa 2, City 1.",
            "majorsDone": "Bermudas final: Austin Smotherman vencio a Seamus Power en el tercer hoyo de playoff para alzar el trofeo.",
            "wnbaFirstRound": "Finales WNBA Juego 5 esta noche: Valkyries reciben a Dream en el Chase Center con serie 2-2 por el anillo.",
            "bracketFootnote": "Juego 1: Valkyries 68-64. Juego 2: Dream 79-65. Juego 3: Dream 97-71. Juego 4: Valkyries 67-62. Juego 5 esta noche."
        }
    },
    "de": {
        "f1": {
            "tagline": "Weltmeister Antonelli: Italienisches Ausnahmetalent gewinnt US-GP von der Pole und macht WM-Titel 2026 perfekt.",
            "liveNow": "Austin GP Finale: Antonelli siegt vor Leclerc und Verstappen. Russell auf P8 besiegelt Antonellis Titelgewinn mit 123 Punkten Vorsprung.",
            "pulse": "WELTMEISTER: ANTONELLI CROWNT SICH IN AUSTIN ZUM CHAMPION",
            "keywords": "Formel 1, US GP, Austin, COTA, Antonelli, Weltmeister, Verstappen, Leclerc"
        },
        "basketball": {
            "tagline": "WNBA Finals Spiel 5 heute Nacht: Valkyries und Dream kaempfen im Chase Center um die Meisterschaftskrone.",
            "liveNow": "Heute Nacht in San Francisco: Alles-oder-Nichts in Spiel 5. Stand 2-2 nach dem 67-62-Auswaertscoup der Valkyries in Spiel 4.",
            "pulse": "FINALS SHOWDOWN: ENTSCHEIDENDES SPIEL 5 IN SAN FRANCISCO",
            "keywords": "WNBA Finals, Spiel 5, Valkyries, Dream, Williams, Reese, Chase Center, Titelkampf"
        },
        "football": {
            "tagline": "NFL Woche 7 Sonntag der Sensationen: Seahawks entzaubern Chiefs 20-3, Falcons schlagen 49ers, Vikings nun allein ungeschlagen bei 6-0.",
            "liveNow": "Sonntags-Finals: Seahawks 20, Chiefs 3; Falcons 29, 49ers 20; Vikings 16, Colts 10. Heute Nacht: Cowboys bei den Eagles im MNF.",
            "pulse": "SENSATIONSSONNTAG: VIKINGS ALLEIN UNBESIEGT NACH NIEDERLAGEN DER CHIEFS UND 49ERS",
            "keywords": "NFL Woche 7, Chiefs, 49ers, Vikings, Seahawks, Falcons, Cowboys, Eagles, MNF"
        },
        "soccer": {
            "tagline": "Premier League 8. Spieltag Abschluss: Bournemouth schockt Manchester United mit 3-0 im Old Trafford, Liverpool 2-0 gegen Brighton.",
            "liveNow": "Sonntag: Bournemouth 3, Man United 0; Liverpool 2, Brighton 0; Newcastle 2, Palace 0. Man City und Arsenal vorn mit 21 Punkten.",
            "pulse": "PREMIER LEAGUE: BOURNEMOUTH DEMUETIGT MAN UNITED IM OLD TRAFFORD",
            "keywords": "Premier League, Bournemouth, Man United, Liverpool, Arsenal, Man City, 8. Spieltag"
        },
        "golf": {
            "tagline": "Bermuda Stechen-Krimi: Austin Smotherman bezwingt Seamus Power am dritten Extraloch zum zweiten Toursieg innerhalb eines Monats.",
            "liveNow": "Bermuda Finale: Smotherman locht zum Par auf der 16 nach 54-Loch-Gleichstand bei 16 unter Par gegen Power. Conners T3 bei -14.",
            "pulse": "PORT ROYAL PLAYOFF: SMOTHERMAN HOLT BERMUDA-TITEL",
            "keywords": "PGA Tour, Bermuda, Port Royal, Smotherman, Power, Playoff, Sieger"
        },
        "tennis": {
            "tagline": "ATP 500 Hallenserie startet in Wien und Basel: Alcaraz trifft auf Khachanov, Almaty-Champion Medvedev im Feld.",
            "liveNow": "Montag Runde 1: Erste Bank Open in Wien und Swiss Indoors in Basel gestartet. Alcaraz, Zverev und Medvedev im Fokus.",
            "pulse": "HALLENSAISON: WIEN UND BASEL EROEFFNEN DIE ATP-500-WOCHE",
            "keywords": "ATP, Wien, Basel, Alcaraz, Khachanov, Medvedev, Zverev, Erste Bank Open"
        },
        "home": {
            "tonight": "Montags-Desk",
            "tonightBlurb": "Antonelli in Austin zum Weltmeister gekroent. Entscheidendes Spiel 5 der WNBA Finals. Ungeschlagene Favoriten stuerzen in der NFL.",
            "plTitle": "Premier League: Bournemouth fegt Manchester United 3-0 im Old Trafford vom Platz",
            "plBlurb": "Bournemouth feiert historischen Auswaertssieg. Liverpool klettert durch 2-0 gegen Brighton auf Rang 3 hinter City und Arsenal.",
            "f1Title": "US Grand Prix: Antonelli ist Formel-1-Weltmeister",
            "f1Blurb": "Kimi Antonelli siegt von der Pole in Austin. Mit Rang 8 fuer Teamkollege Russell sichert sich der Italiener vorzeitig die Krone 2026."
        },
        "pg": {
            "pinFinal": "Austin GP Finale: Antonelli siegt vor Leclerc und Verstappen. Russell P8 sichert Antonelli vorzeitig den WM-Titel.",
            "week1Closed": "NFL SNF Finale: Seahawks fertigen Chiefs mit 20-3 im Lumen Field ab",
            "week1Sub": "Seattle haelt Mahomes ohne Touchdown. Falcons schlagen 49ers 29-20. Vikings stehen bei 6-0. Heute: Cowboys in Philadelphia.",
            "countdownTnf": "MNF heute Nacht: Cowboys (2-4) bei den Eagles (2-4). Chiefs und 49ers verloren am Sonntag. Vikings stehen 6-0.",
            "barsPoints": "Abstand zum Spitzenreiter: Antonelli fuehrt mit 365 Punkten, 123 vor Russell (242). Antonelli ist Formel-1-Weltmeister.",
            "tableAfterMonday": "Premier League: City und Arsenal punktgleich mit 21 (7-0-1). Liverpool 15, Chelsea 13, Bournemouth 13. United bei 10.",
            "pinClub": "Klub waehlen. City und Arsenal haben 21 Punkte. Liverpool 15, Bournemouth 13. Bournemouth siegte 3-0 im Old Trafford.",
            "plFootnote": "Sonntag: Bournemouth 3, Man United 0; Liverpool 2, Brighton 0. Samstag: Spurs 2, Chelsea 0; Villa 2, City 1.",
            "majorsDone": "Bermuda Finale: Austin Smotherman besiegte Seamus Power am dritten Extraloch im Stechen zum Turniersieg.",
            "wnbaFirstRound": "WNBA Finals Spiel 5 heute: Valkyries empfangen Dream im Chase Center bei 2-2 im Showdown um den Titel.",
            "bracketFootnote": "Spiel 1: Valkyries 68-64. Spiel 2: Dream 79-65. Spiel 3: Dream 97-71. Spiel 4: Valkyries 67-62. Spiel 5 heute Nacht."
        }
    },
    "it": {
        "f1": {
            "tagline": "Antonelli campione del mondo: il talento italiano vince il GP degli Stati Uniti dalla pole e fa suo il titolo 2026.",
            "liveNow": "Finale Austin: Antonelli trionfa davanti a Leclerc e Verstappen. Russell P8 regala la certezza iridata con 123 punti di margine.",
            "pulse": "CAMPIONE DEL MONDO: ANTONELLI CHIUDE IL MONDIALE AD AUSTIN",
            "keywords": "Formula 1, GP Stati Uniti, Austin, COTA, Antonelli, campione del mondo, Verstappen, Leclerc"
        },
        "basketball": {
            "tagline": "WNBA Finals Gara 5 stanotte: Valkyries e Dream al Chase Center per la sfida decisiva che assegna l'anello.",
            "liveNow": "Stanotte a San Francisco: Gara 5 decisiva. Serie sul 2-2 dopo l'incredibile 67-62 esterno delle Valkyries in Gara 4.",
            "pulse": "VERDETTO WNBA FINALS: GARA 5 STANOTTE A SAN FRANCISCO",
            "keywords": "WNBA Finals, Gara 5, Valkyries, Dream, Williams, Reese, Chase Center, titolo"
        },
        "football": {
            "tagline": "Domenica di scossoni in NFL: i Seahawks domano i Chiefs 20-3, Falcons battono i 49ers, Vikings unici imbattuti a 6-0.",
            "liveNow": "Finali domenica: Seahawks 20, Chiefs 3; Falcons 29, 49ers 20; Vikings 16, Colts 10. Stanotte: Cowboys a Philadelphia nel MNF.",
            "pulse": "DOMENICA PAZZA: VIKINGS SOLI A 6-0 DOPO I KO DI CHIEFS E 49ERS",
            "keywords": "NFL Week 7, Chiefs, 49ers, Vikings, Seahawks, Falcons, Cowboys, Eagles, MNF"
        },
        "soccer": {
            "tagline": "Chiusura 8a giornata: il Bournemouth travolge il Manchester United 3-0 a Old Trafford, Liverpool batte Brighton 2-0.",
            "liveNow": "Domenica: Bournemouth 3, Man United 0; Liverpool 2, Brighton 0; Newcastle 2, Palace 0. City e Arsenal in testa a 21 punti.",
            "pulse": "PREMIER LEAGUE: IL BOURNEMOUTH ESPUGNA OLD TRAFFORD PER 3-0",
            "keywords": "Premier League, Bournemouth, Man United, Liverpool, Arsenal, Man City, 8a giornata"
        },
        "golf": {
            "tagline": "Playoff mozzafiato a Bermuda: Austin Smotherman batte Seamus Power alla terza buca di spareggio e fa bis in un mese.",
            "liveNow": "Bermuda finale: Smotherman firma il par alla 16 nello spareggio dopo il -16 sulle 54 buche con Power. Conners T3 a -14.",
            "pulse": "SPAREGGIO A PORT ROYAL: SMOTHERMAN TRIONFA A BERMUDA",
            "keywords": "PGA Tour, Bermuda, Port Royal, Smotherman, Power, spareggio, vincitore"
        },
        "tennis": {
            "tagline": "Al via i tornei ATP 500 indoor a Vienna e Basilea: Alcaraz sfida Khachanov, c'e il campione di Almaty Medvedev.",
            "liveNow": "Lunedi 1° turno: scattano Vienna e Basilea. Alcaraz, Zverev e Medvedev guidano il tabellone austriaco.",
            "pulse": "STAGIONE INDOOR: VIENNA E BASILEA ACCENDONO LA SETTIMANA ATP 500",
            "keywords": "ATP, Vienna, Basilea, Alcaraz, Khachanov, Medvedev, Zverev, Erste Bank Open"
        },
        "home": {
            "tonight": "Desk di lunedi",
            "tonightBlurb": "Antonelli iridato al COTA. Gara 5 decisiva delle WNBA Finals a San Francisco. Crollano le imbattute in NFL.",
            "plTitle": "Premier League: il Bournemouth sbanca Old Trafford per 3-0",
            "plBlurb": "Impresa clamorosa del Bournemouth a Manchester. Il Liverpool supera 2-0 il Brighton e sale al 3° posto dietro City e Arsenal.",
            "f1Title": "GP degli Stati Uniti: Antonelli campione del mondo",
            "f1Blurb": "Kimi Antonelli vince dalla pole a Austin. Con l'ottavo posto di Russell il ventenne italiano chiude i conti per il titolo 2026."
        },
        "pg": {
            "pinFinal": "Finale Austin: Antonelli vince davanti a Leclerc e Verstappen. Russell P8 incorona Antonelli campione del mondo.",
            "week1Closed": "NFL SNF finale: i Seahawks travolgono i Chiefs 20-3 a Lumen Field",
            "week1Sub": "Seattle ferma Mahomes senza mete. Falcons battono 49ers 29-20. Vikings volano a 6-0. Stanotte: Cowboys a Philadelphia.",
            "countdownTnf": "MNF stanotte: Cowboys (2-4) contro Eagles (2-4). Chiefs e 49ers sconfitti domenica. I Vikings restano a 6-0.",
            "barsPoints": "Distacco dal leader: Antonelli a 365 punti, 123 davanti a Russell (242). Antonelli e campione del mondo.",
            "tableAfterMonday": "Premier League: City e Arsenal appaiate a 21 (7-0-1). Liverpool 15, Chelsea e Bournemouth 13. United a quota 10.",
            "pinClub": "Seleziona un club. City e Arsenal guidano a 21. Liverpool 15, Bournemouth 13. Bournemouth ha vinto 3-0 a Old Trafford.",
            "plFootnote": "Domenica: Bournemouth 3, Man United 0; Liverpool 2, Brighton 0. Sabato: Spurs 2, Chelsea 0; Villa 2, City 1.",
            "majorsDone": "Bermuda finale: Austin Smotherman supera Seamus Power alla 3a buca di spareggio e vince il torneo.",
            "wnbaFirstRound": "WNBA Finals Gara 5 stanotte: Valkyries e Dream al Chase Center sul 2-2 per l'anello piu ambito.",
            "bracketFootnote": "Gara 1: Valkyries 68-64. Gara 2: Dream 79-65. Gara 3: Dream 97-71. Gara 4: Valkyries 67-62. Gara 5 stanotte."
        }
    },
    "pl": {
        "f1": {
            "tagline": "Mistrz Swiata Antonelli: Wloski nastolatek wygrywa GP Stanow Zjednoczonych z pole position i pieczetuje tytul 2026.",
            "liveNow": "Final Austin: Antonelli triumfuje przed Leclerkiem i Verstappenem. Russell P8 zapewnia Antonellemu mistrzostwo ze 123 pkt przewagi.",
            "pulse": "MISTRZ SWIATA: ANTONELLI ZDOBYWA TYTUL W TEKSASIE",
            "keywords": "Formula 1, GP USA, Austin, COTA, Antonelli, mistrz swiata, Verstappen, Leclerc"
        },
        "basketball": {
            "tagline": "Mecz numer 5 Finalow WNBA dzis w nocy: Valkyries i Dream w Chase Center walcza o decydujace mistrzostwo.",
            "liveNow": "Dzis w nocy w San Francisco: mecz o wszystko. Stan serii 2-2 po wyjazdowej wygranej Valkyries 67-62 w meczu numer 4.",
            "pulse": "FINALOWY ROZSTRZYGNIECIE WNBA: MECZ 5 DZIS W SAN FRANCISCO",
            "keywords": "Finaly WNBA, Mecz 5, Valkyries, Dream, Williams, Reese, Chase Center, mecz o mistrzostwo"
        },
        "football": {
            "tagline": "Sensacje niedzieli 7. tygodnia NFL: Seahawks uciszaja Chiefs 20-3, Falcons bija 49ers, Vikings jedynymi niepokonanymi z 6-0.",
            "liveNow": "Finaly niedzieli: Seahawks 20, Chiefs 3; Falcons 29, 49ers 20; Vikings 16, Colts 10. Dzis w nocy: Cowboys u Eagles w MNF.",
            "pulse": "NIEDZIELA SENSACJI: VIKINGS SAMI NA CZELE PO PORAZKACH CHIEFS I 49ERS",
            "keywords": "NFL Tydzien 7, Chiefs, 49ers, Vikings, Seahawks, Falcons, Cowboys, Eagles, MNF"
        },
        "soccer": {
            "tagline": "Koncowka 8. kolejki Premier League: Bournemouth rozbija Manchester United 3-0 na Old Trafford, Liverpool wygrywa 2-0.",
            "liveNow": "Niedziela: Bournemouth 3, Man United 0; Liverpool 2, Brighton 0; Newcastle 2, Palace 0. Man City i Arsenal na czele z 21 pkt.",
            "pulse": "PREMIER LEAGUE: BOURNEMOUTH UPURZA MAN UNITED NA OLD TRAFFORD",
            "keywords": "Premier League, Bournemouth, Man United, Liverpool, Arsenal, Man City, 8. kolejka"
        },
        "golf": {
            "tagline": "Dramatyczna dogrywka na Bermudach: Austin Smotherman pokonuje Seamusa Powera na trzecim dolku i wygrywa drugi turniej w miesiacu.",
            "liveNow": "Bermudy final: Smotherman z par na 16. dolku dogrywki bije Powera po remisie na -16 po 54 dolkach. Conners T3 z -14.",
            "pulse": "DOGRYWKA W PORT ROYAL: SMOTHERMAN MISTRZEM NA BERMUDACH",
            "keywords": "PGA Tour, Bermudy, Port Royal, Smotherman, Power, dogrywka, mistrz"
        },
        "tennis": {
            "tagline": "Ruszaja turnieje halowe ATP 500 w Wiedniu i Bazylei: Alcaraz gra z Chaczanowem, mistrz z Almaty Medwiediew w stawce.",
            "liveNow": "Poniedzialek 1. runda: start w Wiedniu i Bazylei. Alcaraz, Zverev oraz Medwiediew gwiazdami turnieju.",
            "pulse": "SEZON HALOWY: WIEDEN I BAZYLEA OTWIERAJA TYDZIEN ATP 500",
            "keywords": "ATP, Wieden, Bazylea, Alcaraz, Khachanov, Medvedev, Zverev, Erste Bank Open"
        },
        "home": {
            "tonight": "Poniedzialkowe biurko",
            "tonightBlurb": "Antonelli mistrzem swiata F1 w Austin. Decydujacy mecz numer 5 Finalow WNBA. Porazki niepokonanych w NFL.",
            "plTitle": "Premier League: Bournemouth gromi Manchester United 3-0 na Old Trafford",
            "plBlurb": "Bournemouth sprawia wielka sensacje w Manchesterze. Liverpool pokonuje Brighton 2-0 i wskakuje na podium za City i Arsenal.",
            "f1Title": "Grand Prix USA: Antonelli mistrzem swiata",
            "f1Blurb": "Kimi Antonelli wygrywa z pole position w Austin. Przy 8. miejscu Russella Wloch przypieczetowal tytul mistrzowski w sezonie 2026."
        },
        "pg": {
            "pinFinal": "Final Austin: Antonelli wygrywa przed Leclerkiem i Verstappenem. Russell P8 daje Antonellemu tytul mistrza.",
            "week1Closed": "NFL SNF final: Seahawks demoluja Chiefs 20-3 na Lumen Field",
            "week1Sub": "Defensywa Seattle nie pozwala Mahomesowi na przylozenie. Falcons 29, 49ers 20. Vikings z 6-0. Dzis: Cowboys u Eagles.",
            "countdownTnf": "MNF dzis w nocy: Cowboys (2-4) graja z Eagles (2-4). Chiefs i 49ers polegli w niedziele. Vikings maja bilans 6-0.",
            "barsPoints": "Przewaga nad rywalami: Antonelli ma 365 pkt, o 123 wiecej niz Russell (242). Antonelli jest mistrzem swiata.",
            "tableAfterMonday": "Premier League: City i Arsenal na czele z 21 (7-0-1). Liverpool 15, Chelsea i Bournemouth 13. United z 10 pkt.",
            "pinClub": "Wybierz klub. City i Arsenal maja po 21 pkt. Liverpool 15, Bournemouth 13. Bournemouth wygralo 3-0 na Old Trafford.",
            "plFootnote": "Niedziela: Bournemouth 3, Man United 0; Liverpool 2, Brighton 0. Sobota: Spurs 2, Chelsea 0; Villa 2, City 1.",
            "majorsDone": "Bermudy final: Austin Smotherman pokonal Seamusa Powera na 3. dolku dogrywki i zgarnal trofeum.",
            "wnbaFirstRound": "Finaly WNBA mecz 5 dzis: Valkyries podejmuja Dream w Chase Center przy stanie 2-2 w walce o tytul.",
            "bracketFootnote": "Mecz 1: Valkyries 68-64. Mecz 2: Dream 79-65. Mecz 3: Dream 97-71. Mecz 4: Valkyries 67-62. Mecz 5 dzis w nocy."
        }
    },
    "zh": {
        "f1": {
            "tagline": "安东内利加冕F1世界冠军：意大利超级新星从杆位起步夺得美洲赛道分站冠军并锁定2026总冠军。",
            "liveNow": "奥斯汀正赛收官：安东内利力压勒克莱尔与维斯塔潘夺冠。拉塞尔位列第8助安东内利领先123分提前登顶世界之巅。",
            "pulse": "世界冠军诞生：安东内利在COTA正式加冕2026年车手总冠军",
            "keywords": "一级方程式, 美国大奖赛, 奥斯汀, COTA, 安东内利, 世界冠军, 维斯塔潘, 勒克莱尔"
        },
        "basketball": {
            "tagline": "WNBA总决赛抢五大战今晚打响：女武神与梦想齐聚旧金山大通中心决出总冠军归属。",
            "liveNow": "今晚旧金山决战：总比分2-2平，女武神第4战客场67-62取胜后回归主场力争创历史夺冠。",
            "pulse": "WNBA总冠军决战：抢五生死战今晚大通中心开战",
            "keywords": "WNBA总决赛, 抢五, 女武神, 梦想, 威廉姆斯, 里斯, 大通中心, 总冠军"
        },
        "football": {
            "tagline": "NFL第7周超级冷门周日：海鹰20-3掀翻酋长，猎鹰29-20击败49人，维京人6胜0负成全联盟唯一不败之师。",
            "liveNow": "周日比赛：海鹰20-3酋长，猎鹰29-20力破49人，维京人16-10小马。今晚周一夜赛：牛仔客战老鹰。",
            "pulse": "冷门周日狂澜：酋长与49人吞首败，维京人6战全胜独占鳌头",
            "keywords": "NFL第7周, 酋长, 49人, 维京人, 海鹰, 猎鹰, 牛仔, 老鹰, MNF"
        },
        "soccer": {
            "tagline": "英超第8轮战罢：伯恩茅斯客场3-0完胜曼联震动梦剧场，利物浦2-0轻取布莱顿攀至第三。",
            "liveNow": "第8轮周日赛果：伯恩茅斯3-0曼联，利物浦2-0布莱顿，纽卡2-0水晶宫。曼城阿森纳同积21分并列领跑。",
            "pulse": "英超冷门夜：伯恩茅斯老特拉福德客场3-0横扫曼联",
            "keywords": "英超, 伯恩茅斯, 曼联, 利物浦, 阿森纳, 曼城, 第8轮"
        },
        "golf": {
            "tagline": "百慕大锦标赛延长赛绝杀：斯莫瑟曼在第3个加洞险胜鲍尔，一个月内斩获个人美巡赛第二冠。",
            "liveNow": "百慕大决赛：斯莫瑟曼在54洞与鲍尔同为-16后，于第16洞加洞保帕成功夺冠。科纳斯位列T3（-14）。",
            "pulse": "皇家港加洞决胜：斯莫瑟曼夺得百慕大锦标赛冠军",
            "keywords": "美巡赛, 百慕大, 皇家港, 斯莫瑟曼, 鲍尔, 加洞赛, 冠军"
        },
        "tennis": {
            "tagline": "ATP 500室内赛季维也纳与巴塞尔启幕：阿尔卡拉斯首战对决哈恰诺夫，阿拉木图冠军梅德韦杰夫在列。",
            "liveNow": "周一第1轮：维也纳与巴塞尔两项ATP 500大战开打，阿尔卡拉斯、兹维列夫与梅德韦杰夫领衔出战。",
            "pulse": "室内赛季狂欢：维也纳与巴塞尔联袂拉开ATP 500大幕",
            "keywords": "ATP, 维也纳, 巴塞尔, 阿尔卡拉斯, 哈恰诺夫, 梅德韦杰夫, 兹维列夫, 室内赛"
        },
        "home": {
            "tonight": "周一总览",
            "tonightBlurb": "安东内利在COTA加冕F1世界总冠军。WNBA总决赛抢五生死决战。NFL豪强不败金身在周日纷纷告破。",
            "plTitle": "英超赛况：伯恩茅斯客场3-0大胜曼联，梦剧场沦陷",
            "plBlurb": "伯恩茅斯打出队史客场经典战役。利物浦2-0战胜布莱顿升至第三，紧咬同积21分的曼城与阿森纳。",
            "f1Title": "F1美国大奖赛：安东内利加冕世界冠军",
            "f1Blurb": "安东内利杆位起跑统治奥斯汀。队友拉塞尔仅排第八，20岁意大利新星提前锁定2026年车手总冠军。"
        },
        "pg": {
            "pinFinal": "奥斯汀正赛：安东内利力克勒克莱尔与维斯塔潘夺冠，拉塞尔第八助安东内利提前锁定年度总冠军。",
            "week1Closed": "NFL周日夜赛：海鹰在流明球场20-3痛击酋长",
            "week1Sub": "西雅图防守让马霍姆斯未获达阵。猎鹰29-20胜49人。维京人6胜0负独占鳌头。今晚：牛仔客战老鹰。",
            "countdownTnf": "今晚周一夜赛：牛仔（2-4）客战老鹰（2-4）。酋长与49人周日遭遇首败。维京人6战全胜。",
            "barsPoints": "积分榜差距展示：安东内利积365分领先拉塞尔（242分）多达123分，安东内利加冕2026总冠军。",
            "tableAfterMonday": "英超积分榜：曼城与阿森纳同积21分（7胜1负）。利物浦15分，切尔西与伯恩茅斯13分，曼联10分。",
            "pinClub": "选择球队。曼城与阿森纳积21分。利物浦15分，伯恩茅斯13分，伯恩茅斯老特拉福德3-0完胜曼联。",
            "plFootnote": "周日：伯恩茅斯3-0曼联，利物浦2-0布莱顿。周六：热刺2-0切尔西，维拉2-1曼城。",
            "majorsDone": "百慕大锦标赛：斯莫瑟曼在第3个加洞险胜鲍尔，成功捧得锦标赛冠军奖杯。",
            "wnbaFirstRound": "WNBA总决赛抢五大战今晚打响：女武神与梦想在大通中心2-2决战，胜者捧得总冠军金杯。",
            "bracketFootnote": "G1：女武神68-64。G2：梦想79-65。G3：梦想97-71。G4：女武神67-62。G5今晚旧金山开战。"
        }
    },
    "ja": {
        "f1": {
            "tagline": "アントネッリがF1世界王者に君臨：イタリアの神童がアメリカGPでポール・トゥ・ウィンを飾り2026年タイトルを戴冠。",
            "liveNow": "オースティン決勝：アントネッリがルクレールとフェルスタッペンを抑え優勝。ラッセル8位でアントネッリが123点差で年間王者を確定。",
            "pulse": "世界王者誕生：アントネッリがCOTAで2026年ドライバーズ選手権を制覇",
            "keywords": "フォーミュラ1, アメリカGP, オースティン, COTA, アントネッリ, 世界王者, フェルスタッペン, ルクレール"
        },
        "basketball": {
            "tagline": "WNBAファイナル運命の第5戦は今夜：バルキリーズとドリームがチェイス・センターで頂点を懸けて激突。",
            "liveNow": "今夜サンフランシスコで最終決戦：対戦成績2勝2敗。第4戦を67-62で奪い返したバルキリーズが本拠地で初戴冠へ挑む。",
            "pulse": "WNBAファイナル最終決戦：運命の第5戦が今夜サンフランシスコで開幕",
            "keywords": "WNBAファイナル, 第5戦, バルキリーズ, ドリーム, ウィリアムズ, リース, チェイス・センター, 頂上決戦"
        },
        "football": {
            "tagline": "NFL第7週波乱のサンデー：シーホークスがチーフスを20-3で圧倒、ファルコンズが49ers撃破、バイキングスが6勝0敗で唯一無敗に。",
            "liveNow": "日曜結果：シーホークス20-3チーフス、ファルコンズ29-20の49ers、バイキングス16-10コルツ。今夜：カウボーイズ対イーグルス（MNF）。",
            "pulse": "大波乱サンデー：チーフスと49ersが初黒星、バイキングスが単独全勝をキープ",
            "keywords": "NFL第7週, チーフス, 49ers, バイキングス, シーホークス, ファルコンズ, カウボーイズ, イーグルス, MNF"
        },
        "soccer": {
            "tagline": "プレミアリーグ第8節総括：ボーンマスがオールド・トラッフォードでマンUを3-0粉砕、リヴァプールは2-0で3位浮上。",
            "liveNow": "第8節日曜：ボーンマス3-0マンチェスター・U、リヴァプール2-0ブライトン、ニューカッスル2-0パレス。シティとアーセナルが勝点21首位タイ。",
            "pulse": "プレミアリーグ：ボーンマスが敵地オールド・トラッフォードで歴史的3-0完勝",
            "keywords": "プレミアリーグ, ボーンマス, マンチェスター・ユナイテッド, リヴァプール, アーセナル, マンチェスター・C, 第8節"
        },
        "golf": {
            "tagline": "バミューダ選手権プレーオフ激闘：オースティン・スモーザーマンが3ホール目にパワーを下し今月ツアー2勝目。",
            "liveNow": "バミューダ決勝：54ホール通算16アンダーで並んだパワーとのプレーオフ、16番でのパーセーブでスモーザーマンが優勝。コナーズT3（-14）。",
            "pulse": "ポートロイヤル死闘：スモーザーマンがプレーオフを制しバミューダ戴冠",
            "keywords": "PGAツアー, バミューダ, ポートロイヤル, スモーザーマン, パワー, プレーオフ, 優勝"
        },
        "tennis": {
            "tagline": "ATP 500室内シーズンがウィーンとバーゼルで開幕：アルカラスがハチャノフと対決、アルマトイ王者メドベージェフも参戦。",
            "liveNow": "月曜1回戦：エルステ・バンク・オープンとスイス・インドアがスタート。アルカラス、ズベレフ、メドベージェフが熱戦へ。",
            "pulse": "インドア開幕：ウィーンとバーゼルでATP 500ウィークが開幕",
            "keywords": "ATP, ウィーン, バーゼル, アルカラス, ハチャノフ, メドベージェフ, ズベレフ, エルステ・バンク・オープン"
        },
        "home": {
            "tonight": "月曜デスク",
            "tonightBlurb": "アントネッリがCOTAでF1世界王者に輝く。WNBAファイナルは運命の第5戦へ。NFLでは無敗勢が日曜に相次いで陥落。",
            "plTitle": "プレミアリーグ：ボーンマスがオールド・トラッフォードでマンUに3-0完勝",
            "plBlurb": "ボーンマスが歴史的圧勝。リヴァプールがブライトンを2-0で下し、首位タイのシティとアーセナルを追走する3位へ浮上。",
            "f1Title": "F1アメリカGP：アントネッリが世界王者を戴冠",
            "f1Blurb": "キミ・アントネッリがオースティンでポール・トゥ・ウィン。ラッセルが8位に終わり、20歳のイタリア人が2026年王者を確定。"
        },
        "pg": {
            "pinFinal": "オースティン決勝：アントネッリがルクレールとフェルスタッペンを抑え優勝。ラッセル8位でアントネッリ戴冠。",
            "week1Closed": "NFL SNF決勝：シーホークスがルーメン・フィールドでチーフスを20-3で撃破",
            "week1Sub": "シアトル守備陣がマホームズを無TDに封じる。ファルコンズ29-20の49ers。バイキングス6-0。今夜：カウボーイズ対イーグルス。",
            "countdownTnf": "今夜MNF：カウボーイズ（2-4）対イーグルス（2-4）。チーフスと49ersは日曜に初敗戦。バイキングスは6-0全勝。",
            "barsPoints": "首位との差：アントネッリが365点、ラッセル（242点）に123点差をつけて2026年F1世界王者を確定。",
            "tableAfterMonday": "プレミアリーグ順位：シティとアーセナルが21点（7勝1敗）。リヴァプール15点、チェルシーとボーンマス13点、マンUは10点。",
            "pinClub": "クラブを選択。シティとアーセナルが21点。リヴァプール15点、ボーンマス13点。ボーンマスは敵地で3-0快勝。",
            "plFootnote": "日曜：ボーンマス3-0マンチェスター・U、リヴァプール2-0ブライトン。土曜：スパーズ2-0チェルシー、ヴィラ2-1シティ。",
            "majorsDone": "バミューダ決勝：オースティン・スモーザーマンがプレーオフ3ホール目でシェーマス・パワーを下し優勝。",
            "wnbaFirstRound": "WNBAファイナル第5戦今夜：バルキリーズがチェイス・センターでドリームを迎撃。2-2から頂点を決定。",
            "bracketFootnote": "第1戦：バルキリーズ68-64。第2戦：ドリーム79-65。第3戦：ドリーム97-71。第4戦：バルキリーズ67-62。第5戦今夜。"
        }
    },
    "ko": {
        "f1": {
            "tagline": "안토넬리 F1 월드 챔피언 등극: 이탈리아 10대 신성 미국 GP 폴투윈 달성하며 2026 타이틀 확정.",
            "liveNow": "오스틴 GP 결승: 안토넬리 르클레르와 베르스타펜 제치고 우승. 러셀 8위로 안토넬리가 123점 차로 월드 챔피언 확정.",
            "pulse": "월드 챔피언 탄생: 안토넬리 COTA에서 2026 드라이버 챔피언 등극",
            "keywords": "F1, 미국 그랑프리, 오스틴, COTA, 안토넬리, 월드 챔피언, 베르스타펜, 르클레르"
        },
        "basketball": {
            "tagline": "WNBA 파이널 최종 5차전 오늘 밤 격돌: 발키리스와 드림 체이스 센터에서 마지막 우승 결전.",
            "liveNow": "오늘 밤 샌프란시스코 운명의 승부: 시리즈 2-2 팽팽. 4차전 67-62 원정 승리를 거둔 발키리스 창단 첫 우승 도전.",
            "pulse": "WNBA 파이널 최종전: 운명의 5차전 오늘 밤 샌프란시스코에서 개막",
            "keywords": "WNBA 파이널, 5차전, 발키리스, 드림, 윌리엄스, 리스, 체이스 센터, 최종전"
        },
        "football": {
            "tagline": "NFL 7주 차 슈퍼 선데이 대이변: 시호크스 치프스 20-3 격파, 팰컨스 49ers 제압, 바이킹스 6승 무패 유일한 무패 질주.",
            "liveNow": "일요일 최종: 시호크스 20-3 치프스, 팰컨스 29-20 49ers, 바이킹스 16-10 콜츠. 오늘 밤: 카우보이스 대 이글스 MNF.",
            "pulse": "대이변 선데이: 치프스 49ers 나란히 첫 패배, 바이킹스 6연승 독주",
            "keywords": "NFL 7주 차, 치프스, 49ers, 바이킹스, 시호크스, 팰컨스, 카우보이스, 이글스, MNF"
        },
        "soccer": {
            "tagline": "프리미어리그 8라운드 마감: 본머스 올드 트래퍼드에서 맨유 3-0 완파, 리버풀 브라이턴 2-0 꺾고 3위 도약.",
            "liveNow": "8라운드 일요일: 본머스 3-0 맨유, 리버풀 2-0 브라이턴, 뉴캐슬 2-0 팰리스. 맨시티 아스널 승점 21점 공동 선두.",
            "pulse": "프리미어리그 대이변: 본머스 맨유 안방에서 3-0 완승",
            "keywords": "프리미어리그, 본머스, 맨체스터 유나이티드, 리버풀, 아스널, 맨체스터 시티, 8라운드"
        },
        "golf": {
            "tagline": "버뮤다 챔피언십 연장전 혈투: 오스틴 스모더먼 3번째 연장 홀에서 파워 제치고 한 달 만에 투어 2승 달성.",
            "liveNow": "버뮤다 파이널: 54홀 16언더파 동타 후 16번 홀 파 세이브로 스모더먼 우승. 파워 준우승, 코너스 T3(-14).",
            "pulse": "포트 로열 서든데스: 스모더먼 버뮤다 챔피언십 트로피 쟁취",
            "keywords": "PGA 투어, 버뮤다, 포트 로열, 스모더먼, 파워, 연장전, 우승"
        },
        "tennis": {
            "tagline": "ATP 500 실내 하드코트 시즌 빈과 바젤 개막: 알카라스 하차노프와 격돌, 알마티 챔피언 메드베데프 출격.",
            "liveNow": "월요일 1회전: 오스트리아 에르스테 뱅크 오픈과 스위스 인도어스 개막. 알카라스, 즈베레프, 메드베데프 출전.",
            "pulse": "실내 시즌 개막: 빈과 바젤에서 ATP 500 주간 팡파르",
            "keywords": "ATP, 빈, 바젤, 알카라스, 하차노프, 메드베데프, 즈베레프, 에르스테 뱅크 오픈"
        },
        "home": {
            "tonight": "월요일 데스크",
            "tonightBlurb": "안토넬리 COTA에서 F1 월드 챔피언 대관식. WNBA 파이널 운명의 5차전. NFL 무패 팀들 일요일 연쇄 붕괴.",
            "plTitle": "프리미어리그: 본머스 올드 트래퍼드에서 맨유에 3-0 완승",
            "plBlurb": "본머스의 역사적 압승. 리버풀은 브라이턴을 2-0으로 누르고 승점 21점의 맨시티와 아스널에 이어 3위로 올라섰습니다.",
            "f1Title": "F1 미국 그랑프리: 안토넬리 월드 챔피언 확정",
            "f1Blurb": "키미 안토넬리 오스틴 폴투윈 달성. 팀 동료 러셀이 8위에 그치며 20세 이탈리아 루키가 2026 세계 챔피언을 조기 확정했습니다."
        },
        "pg": {
            "pinFinal": "오스틴 결승: 안토넬리 르클레르와 베르스타펜 제치고 우승. 러셀 8위로 안토넬리 월드 챔피언 등극.",
            "week1Closed": "NFL SNF 결승: 시호크스 루멘 필드에서 치프스 20-3 완파",
            "week1Sub": "시애틀 수비진 머홈스 무터치다운 제어. 팰컨스 29-20 49ers. 바이킹스 6-0 단독 질주. 오늘: 카우보이스 대 이글스.",
            "countdownTnf": "MNF 오늘 밤: 카우보이스(2-4) 대 이글스(2-4). 치프스와 49ers 일요일 첫 패. 바이킹스는 6-0 무패.",
            "barsPoints": "선두와의 격차: 안토넬리 365점, 러셀(242점)에 123점 앞서며 2026 F1 월드 챔피언 확정.",
            "tableAfterMonday": "프리미어리그 순위: 맨시티와 아스널 승점 21점 동률(7-0-1). 리버풀 15점, 첼시 본머스 13점, 맨유 10점.",
            "pinClub": "클럽 선택. 맨시티와 아스널 21점. 리버풀 15점, 본머스 13점. 본머스 올드 트래퍼드 3-0 대승.",
            "plFootnote": "일요일: 본머스 3-0 맨유, 리버풀 2-0 브라이턴. 토요일: 토트넘 2-0 첼시, 빌라 2-1 맨시티.",
            "majorsDone": "버뮤다 파이널: 오스틴 스모더먼이 연장 3번째 홀에서 셰이머스 파워를 꺾고 정상에 올랐습니다.",
            "wnbaFirstRound": "WNBA 파이널 5차전 오늘 밤: 발키리스와 드림이 체이스 센터에서 2-2로 맞서 대망의 챔피언을 결정합니다.",
            "bracketFootnote": "1차전: 발키리스 68-64. 2차전: 드림 79-65. 3차전: 드림 97-71. 4차전: 발키리스 67-62. 5차전 오늘 밤."
        }
    },
    "ar": {
        "f1": {
            "tagline": "انطونيلي بطلا للعالم: النجم الايطالي الصاعد يفوز بسباق امريكا من الصدارة ويحسم لقب 2026 رسميا.",
            "liveNow": "نهائي اوستن: انطونيلي ينتصر امام لوكلير وفيرستابن. وراسل ثامنا ليحسم انطونيلي اللقب بفارق 123 نقطة.",
            "pulse": "بطل العالم: انطونيلي يتوج بلقب موسم 2026 في كوتا",
            "keywords": "فورمولا 1, جائزة امريكا الكبرى, اوستن, كوتا, انطونيلي, بطل العالم, فيرستابن, لوكلير"
        },
        "basketball": {
            "tagline": "المباراة الخامسة الفاصلة لنهائيات WNBA الليلة: فالكيريز ودريم يتصادمان في تشيس سنتر لحسم اللقب.",
            "liveNow": "الليلة في سان فرانسيسكو: مواجهة المجد واللقب. التعادل 2-2 بعد فوز فالكيريز الملحمي 67-62 في اتلانتا بالمباراة الرابعة.",
            "pulse": "حسم نهائيات WNBA: المباراة الخامسة الليلة في سان فرانسيسكو",
            "keywords": "نهائيات WNBA, المباراة 5, فالكيريز, دريم, ويليامز, ريس, تشيس سنتر, الحسم"
        },
        "football": {
            "tagline": "احد المفاجآت في NFL: سيهوكس يسقط تشييفس 20-3، وفالكونز يقهر 49ers، وفايكنغز ينفرد بالصدارة بـ6 انتصارات متتالية.",
            "liveNow": "نتائج الاحد: سيهوكس 20-3 تشييفس، فالكونز 29-20 على 49ers، فايكنغز 16-10 كولتس. الليلة: كاوبويز في فيلادلفيا بالـMNF.",
            "pulse": "احد الصدمات: الفايكنغز الفريق الوحيد دون هزيمة بعد سقوط تشييفس و49ers",
            "keywords": "NFL الاسبوع 7, تشييفس, 49ers, فايكنغز, سيهوكس, فالكونز, كاوبويز, ايغلز, MNF"
        },
        "soccer": {
            "tagline": "ختام الجولة 8 من البريميرليغ: بورنموث يذل مانشستر يونايتد 3-0 في اولد ترافورد، وليفربول يهزم برايتون 2-0.",
            "liveNow": "مباريات الاحد: بورنموث 3-0 مان يونايتد، ليفربول 2-0 برايتون، نيوكاسل 2-0 بالاس. مان سيتي وارسنال في الصدارة بـ21 نقطة.",
            "pulse": "البريميرليغ: بورنموث يكتسح مانشستر يونايتد بثلاثية في معقله",
            "keywords": "الدوري الانجليزي, بورنموث, مانشستر يونايتد, ليفربول, ارسنال, مانشستر سيتي, الجولة 8"
        },
        "golf": {
            "tagline": "اثارة التمايز في برمودا: اوستن سموثيرمان يهزم شيموس باور في الحفرة الاضافية الثالثة ليحرز لقبه الثاني في شهر.",
            "liveNow": "نهائي برمودا: سموثيرمان يسجل البار في الحفرة 16 بعد التعادل بـ16 تحت المعدل مع باور. كونرز في المركز الثالث (-14).",
            "pulse": "فاصلة بورت رويال: سموثيرمان يتوج بطلا في برمودا",
            "keywords": "جولة PGA, برمودا, بورت رويال, سموثيرمان, باور, تمايز, بطل"
        },
        "tennis": {
            "tagline": "انطلاق بطولات ATP 500 داخل الصالات في فيينا وبازل: الكاراز يواجه خاتشانوف وميدفيديف بطل الماتي جاهز.",
            "liveNow": "الاثنين الدور الاول: انطلاق بطولتي فيينا وبازل بمشاركة الكاراز وزفيريف وميدفيديف في صراع النقاط الحاسمة.",
            "pulse": "موسم الصالات: فيينا وبازل تفتتحان اسبوع بطولات ATP 500",
            "keywords": "تنس, فيينا, بازل, الكاراز, خاتشانوف, ميدفيديف, زفيريف, Erste Bank Open"
        },
        "home": {
            "tonight": "مكتب الاثنين",
            "tonightBlurb": "انطونيلي يتوج بطلا للعالم في كوتا. المباراة 5 الفاصلة لنهائيات WNBA في سان فرانسيسكو. سقوط الكبار في NFL.",
            "plTitle": "الدوري الانجليزي: بورنموث يصعق مانشستر يونايتد بثلاثية نظيفة في اولد ترافورد",
            "plBlurb": "انتصار تاريخي لبورنموث خارج ملعبه. ليفربول يتفوق على برايتون 2-0 ويقفز للمركز الثالث خلف مانشستر سيتي وارسنال.",
            "f1Title": "جائزة امريكا الكبرى: انطونيلي بطلا للعالم",
            "f1Blurb": "كيمي انطونيلي ينتصر من الصدارة في اوستن. ومع حلول راسل ثامنا، يحسم السائق الايطالي لقب بطولة العالم 2026."
        },
        "pg": {
            "pinFinal": "نهائي اوستن: انطونيلي يفوز امام لوكلير وفيرستابن. راسل ثامنا ليحسم انطونيلي لقب بطولة العالم.",
            "week1Closed": "سهرة الاحد في NFL: سيهوكس يكتسح تشييفس 20-3 في لومن فيلد",
            "week1Sub": "دفاع سياتل يحرم ماهومز من تسجيل اي هدف. فالكونز يهزم 49ers بنتيجة 29-20. والفايكنغز 6-0. الليلة: كاوبويز في فيلادلفيا.",
            "countdownTnf": "MNF الليلة: كاوبويز (2-4) امام ايغلز (2-4). تشييفس و49ers تلقيا اول خسارة. الفايكنغز 6-0.",
            "barsPoints": "فارق النقاط في الصدارة: انطونيلي يملك 365 نقطة بفارق 123 عن راسل (242). انطونيلي بطل العالم.",
            "tableAfterMonday": "ترتيب البريميرليغ: مان سيتي وارسنال بـ21 نقطة (7-0-1). ليفربول 15، تشيلسي وبورنموث 13. يونايتد 10 نقاط.",
            "pinClub": "اختر ناديا. مان سيتي وارسنال في الصدارة بـ21. ليفربول 15، بورنموث 13 بعد فوزه 3-0 في اولد ترافورد.",
            "plFootnote": "الاحد: بورنموث 3-0 مان يونايتد، ليفربول 2-0 برايتون. السبت: توتنهام 2-0 تشيلسي، فيلا 2-1 سيتي.",
            "majorsDone": "نهائي برمودا: اوستن سموثيرمان يهزم شيموس باور في ثالث حفرة فاصلة ليرفع الكأس.",
            "wnbaFirstRound": "نهائيات WNBA المباراة 5 الليلة: فالكيريز يستضيف دريم في تشيس سنتر لحسم اللقب بعد التعادل 2-2.",
            "bracketFootnote": "المباراة 1: فالكيريز 68-64. المباراة 2: دريم 79-65. المباراة 3: دريم 97-71. المباراة 4: فالكيريز 67-62. المباراة 5 الليلة."
        }
    }
}

# Strict validation: verify NO em-dash or double-hyphen in DATA
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

print("All locale updates for 26 Oct 2026 completed successfully!")
