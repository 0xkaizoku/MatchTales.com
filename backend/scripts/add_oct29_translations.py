# -*- coding: utf-8 -*-
import json
import re

OCT29_STORIES = {
    "carabao-cup-2026-city-liverpool-advance-quarter-finals-draw": {
        "fr": {
            "title": "Carabao Cup 4e tour : Man City et Liverpool rejoignent Fleetwood Town en quarts",
            "subtitle": "Haaland et Foden guident City contre Brighton (2-1) ; Gakpo et Szoboszlai terrassent Chelsea (2-0) avant le tirage.",
            "excerpt": "Manchester City et Liverpool ont valide leur billet pour les quarts de finale de la Coupe de la Ligue mercredi soir au terme de duels intenses.",
            "body": [
                "Apres l'incroyable exploit de Fleetwood Town contre Arsenal mardi, les cadors de Premier League ont remis les pendules a l'heure ce mercredi 28 octobre en Carabao Cup. A l'Etihad Stadium, Manchester City a dispose de Brighton 2-1 grace a des buts d'Erling Haaland et Phil Foden, avant de resister au retour des Seagulls porte par la reduction du score de Kaoru Mitoma.",
                "A Anfield, Liverpool a fait preuve d'une formidable maitrise collective pour ecarter Chelsea 2-0 devant pres de 60 000 spectateurs. Cody Gakpo a debloque la situation juste avant la pause avant que Dominik Szoboszlai ne scelle le sort du match d'une frappe sublime de 25 metres flashée a 104 km/h. Le tirage au sort des quarts de finale aura lieu jeudi avec le petit poucet Fleetwood Town dans toutes les tetes."
            ]
        },
        "es": {
            "title": "Copa de la Liga ronda 4: Man City y Liverpool avanzan a cuartos a la espera del sorteo",
            "subtitle": "Haaland y Foden guian al City ante Brighton (2-1); Gakpo y Szoboszlai doblegan al Chelsea (2-0) con Fleetwood expectante.",
            "excerpt": "Manchester City y Liverpool sellaron el miercoles sus pases a los cuartos de final de la Carabao Cup junto al sorprendente Fleetwood Town.",
            "body": [
                "Tras el inolvidable campanazo de Fleetwood Town eliminando al Arsenal el martes, los gigantes de la Premier League impusieron su jerarquia el miercoles 28 de octubre. En el Etihad Stadium, el Manchester City vencio 2-1 al Brighton gracias a los tantos de Erling Haaland y Phil Foden, resistiendo con orden el empuje final visitante tras el descuento de Kaoru Mitoma.",
                "En Anfield, el Liverpool brindo una exhibicion de madurez tactica para apear al Chelsea por 2-0. Cody Gakpo abrio el marcador al filo del descanso y Dominik Szoboszlai desato el jubilo con un misil desde fuera del area a 104 km/h en el minuto 71. El sorteo de cuartos de final se celebrara este jueves con los ocho clasificados definidos."
            ]
        },
        "de": {
            "title": "Carabao Cup Achtelfinale: Man City und Liverpool komplettieren Viertelfinal-Feld",
            "subtitle": "Haaland und Foden schlagen Brighton 2:1; Gakpo und Szoboszlai besiegeln Chelseas 0:2-Aus vor der Auslosung.",
            "excerpt": "Manchester City und Liverpool zogen am Mittwochabend souveraen ins Ligapokal-Viertelfinale ein und folgten Sensationsklub Fleetwood Town.",
            "body": [
                "Nach dem sensationellen Triumph von Viertligist Fleetwood Town ueber Arsenal am Dienstag rueckten die Schwergewichte am Mittwoch, den 28. Oktober, die Hierarchie wieder zurecht. Im Etihad Stadium bezwang Manchester City Brighton mit 2:1 durch Treffer von Erling Haaland und Phil Foden, ehe die Citizens den Anschlusstreffer von Kaoru Mitoma in der Schlussphase schadlos ueberstanden.",
                "An der Anfield Road dominierte Liverpool das Spitzenspiel gegen Chelsea und siegte verdient mit 2:0 vor knapp 60.000 Zuschauern. Cody Gakpo traf kurz vor dem Halbzeitpfiff, ehe Dominik Szoboszlai in der 71. Minute mit einem 104 km/h schnellen Distanzkracher alles klar machte. Am Donnerstag blickt England nun gespannt auf die Auslosung des Viertelfinales."
            ]
        },
        "it": {
            "title": "Carabao Cup ottavi: Man City e Liverpool staccano il pass per i quarti di finale",
            "subtitle": "Haaland e Foden piegano il Brighton 2-1; Gakpo e Szoboszlai liquidano il Chelsea 2-0 all'Anfield.",
            "excerpt": "Manchester City e Liverpool raggiungono la favola Fleetwood Town tra le migliori otto della Coppa di Lega inglese dopo le sfide di mercoledi.",
            "body": [
                "Dopo la storica impresa del Fleetwood Town contro l'Arsenal di martedi, le grandi della Premier League hanno ristabilito l'ordine mercoledi 28 ottobre nel quarto turno di Carabao Cup. All'Etihad Stadium il Manchester City ha sconfitto 2-1 il Brighton grazie ai sigilli di Erling Haaland e Phil Foden, difendendo il vantaggio dopo il gol della bandiera di Kaoru Mitoma.",
                "Ad Anfield il Liverpool ha superato il Chelsea per 2-0 sfoderando una prestazione impeccabile. Cody Gakpo ha sbloccato il match al 43' minuto e Dominik Szoboszlai ha chiuso i conti al 71' con una sassata da fuori area a 104 km/h sotto la traversa. Giovedi e atteso il sorteggio dei quarti di finale con il Fleetwood Town nel ruolo di favola."
            ]
        },
        "pl": {
            "title": "Puchar Ligi runda 4: Man City i Liverpool melduja sie w cwiercfinale przed losowaniem",
            "subtitle": "Haaland i Foden pokonuja Brighton 2:1; Gakpo i Szoboszlai eliminuja Chelsea 2:0 na Anfield.",
            "excerpt": "Manchester City i Liverpool przypieczetowali w srode awans do cwiercfinalu Carabao Cup, dolaczajac do rewelacyjnego Fleetwood Town.",
            "body": [
                "Po wtorkowej sensacji i wyeliminowaniu Arsenalu przez czwartoligowe Fleetwood Town, faworyci Premier League nie zawiedli w srode 28 pazdziernika. Na Etihad Stadium Manchester City wygral 2:1 z Brighton po golach Erlinga Haalanda i Phila Fodena, odpierajac napór rywali po bramce Kaoru Mitomy.",
                "Na Anfield Liverpool pewnie pokonal Chelsea 2:0 w hicie kolejki. Wynik otworzyl tuz przed przerwa Cody Gakpo, a w 71. minucie Dominik Szoboszlai zachwycil kibicow potężnym uderzeniem z dystansu z predkoscia 104 km/h. W czwartek odbedzie sie losowanie cwiercfinalow, w ktorym Fleetwood bedzie wyczekiwać wylosowania giganta."
            ]
        },
        "zh": {
            "title": "英格兰联赛杯第4轮综述：曼城利物浦携手晋级八强，四分之一决赛抽签在即",
            "subtitle": "哈兰德福登建功助曼城2-1力克布莱顿；加克波索博斯洛伊破门利物浦2-0完胜切尔西。",
            "excerpt": "继英乙弗利特伍德爆冷淘汰阿森纳后，曼城与利物浦在周三晚间双双取胜，顺利晋级英格兰联赛杯八强。",
            "body": [
                "在弗利特伍德点球淘汰阿森纳制造惊天冷门后，英超两强在10月28日周三晚间稳住了阵脚。在伊蒂哈德球场，曼城凭借哈兰德与福登的进球以2-1力克布莱顿，并在三笘薰扳回一城后守住胜果，成功杀入联赛杯八强。",
                "安菲尔德球场同样见证了强强对决，利物浦在近六万名主场球迷的助威下2-0力克切尔西。加克波在上半场补时阶段补射破门，索博斯洛伊在第71分钟轰出一记时速高达104公里的世界波锁定胜局。周四将进行四分之一决赛抽签，八强战充满悬念。"
            ]
        },
        "ja": {
            "title": "カラバオ杯4回戦総括：マンチェスターCとリヴァプールが8強進出、抽選会へ",
            "subtitle": "ハーランドとフォーデンのゴールでブライトンを2-1撃破；ガクポとソボスライの弾丸シュートでチェルシーを2-0圧倒。",
            "excerpt": "フリートウッド・タウンの歴史的大波乱に続き、マンチェスター・シティとリヴァプールが水曜夜に8強入りを決めた。",
            "body": [
                "火曜日に4部フリートウッドがアーセナルを破る奇跡を起こした翌日、10月28日水曜日のカラバオ杯4回戦では優勝候補の2強が順当に勝ち名乗りを上げた。エティハド・スタジアムではマンチェスター・シティがハーランドとフォーデンの得点でブライトンに2-1で競り勝ち、終盤の三笘薫の追撃を振り切った。",
                "アンフィールドではリヴァプールがチェルシーを2-0で一蹴。前半終了間際にガクポが押し込んで先制すると、後半71分にはソボスライが時速104キロの豪快ミドルを叩き込んで勝負を決めた。木曜日に準々決勝の組み合わせ抽選が行われる。"
            ]
        },
        "ko": {
            "title": "카라바오컵 16강 결산: 맨시티와 리버풀 나란히 8강 안착, 대진 추첨 임박",
            "subtitle": "홀란과 포든 연속골로 브라이턴 2-1 제압; 각포와 소보슬러이 쐐기포로 첼시 2-0 격파.",
            "excerpt": "4부 플리트우드의 기적에 이어 맨체스터 시티와 리버풀이 수요일 밤 완승을 거두며 리그컵 8강에 합류했다.",
            "body": [
                "화요일 밤 플리트우드가 아스널을 승부차기로 침몰시킨 데 이어, 10월 28일 수요일에는 프리미어리그 강호들이 클래스를 증명했다. 에티하드 스타디움에서는 맨시티가 홀란과 포든의 골을 앞세워 미토마가 한 골을 만회한 브라이턴을 2-1로 제치고 8강에 올랐다.",
                "안필드에서는 리버풀이 첼시를 2-0으로 완파했다. 전반 추가시간 코디 각포의 선제골에 이어 후반 26분 도미니크 소보슬러이가 시속 104km의 대포알 중거리포로 골망을 갈랐다. 목요일 8강전 대진 추첨이 진행되며 4부 리그 돌풍의 플리트우드가 누구와 맞붙을지 관심이 집중된다."
            ]
        },
        "ar": {
            "title": "كأس الرابطة دور الـ 16: مانشستر سيتي وليفربول يبلغان ربع النهائي قبل القرعة المرتقبة",
            "subtitle": "هالاند وفودين يقودان السيتي لتجاوز برايتون 2-1؛ خاكبو وسوبوسلاي يحسمان موقعة تشيلسي 2-0 في أنفيلد.",
            "excerpt": "حجز مانشستر سيتي وليفربول مقعديهما في الدور ربع النهائي لكأس الرابطة بعد ليلة حافلة بالإثارة الكروية.",
            "body": [
                "بعد الصدمة المدوية التي فجرها فليتوود تاون بإقصاء أرسنال يوم الثلاثاء، استعاد عمالقة الدوري الإنجليزي توازنهم يوم الأربعاء 28 أكتوبر. فعلى ملعب الاتحاد، تجاوز مانشستر سيتي عقبة برايتون بنتيجة 2-1 بهدفي إيرلينغ هالاند وفيل فودين، رغم هدف كاورو ميتوما المتأخر.",
                "وعلى ملعب أنفيلد الشهير، قدم ليفربول عرضا متكاملا ليتفوق على تشيلسي بهدفين دون رد أمام نحو 60 ألف متفرج. وافتتح كودي خاكبو التسجيل قبل نهاية الشوط الأول، قبل أن يطلق دومينيك سوبوسلاي قذيفة صاروخية بسرعة 104 كم في الساعة ليضمن التأهل. وتتجه الأنظار يوم الخميس إلى قرعة الدور ربع النهائي لمعرفة منافس فليتوود تاون القادم."
            ]
        }
    },

    "wnba-finals-2026-game6-preview-valkyries-title-brink-dream-atlanta": {
        "fr": {
            "title": "Finales WNBA match 6 : Les Valkyries a 40 minutes d'un sacre historique face au Dream",
            "subtitle": "Golden State mene 3-2 avant d'entrer au Gateway Center ; Angel Reese et Atlanta condamnees a l'exploit pour arracher un match 7.",
            "excerpt": "L'equipe d'expansion des Valkyries peut signer le plus grand exploit inaugural de l'histoire du sport moderne ce jeudi en Georgie.",
            "body": [
                "Les Golden State Valkyries abordent ce jeudi 29 octobre le rendez-vous le plus crucial de leur toute jeune existence en disputant le match 6 des Finales WNBA a Atlanta. Menant 3-2 apres leur festival defensif du match 5 (64-55) au Chase Center, les joueuses de Natalie Nakase ne sont plus qu'a 40 minutes de devenir la premiere equipe d'expansion championne des sa saison inaugurale depuis 1950.",
                "Pour l'Atlanta Dream d'Angel Reese et Rhyne Howard, la defaite est interdite sur leur parquet du Gateway Center Arena. Atlanta devra trouver la parade au piege tactique des Valkyries pour emmener cette serie epique jusqu'a un match 7 decisif dimanche a San Francisco."
            ]
        },
        "es": {
            "title": "Previo del Partido 6 de las Finales WNBA: Valkyries rozan el anillo historico ante el Dream",
            "subtitle": "Golden State viaja con ventaja de 3-2 a Atlanta; Angel Reese y las suyas obligadas a ganar para forzar el Partido 7.",
            "excerpt": "La franquicia de expansion Golden State Valkyries puede culminar la gesta mas asombrosa del baloncesto moderno este jueves por la noche.",
            "body": [
                "Las Golden State Valkyries se plantan este jueves 29 de octubre en el Gateway Center Arena de College Park con una ventaja de 3-2 en las Finales de la WNBA. Ningun equipo de expansion en los grandes deportes norteamericanos ha levantado el titulo en su primer ano desde 1950, y las dirigidas por Natalie Nakase estan a solo un triunfo de reescribir todos los libros de historia.",
                "Para el Atlanta Dream, el choque es a todo o nada. Angel Reese, que ha firmado cuatro dobles-dobles consecutivos en estas Finales, necesita el acierto exterior de Rhyne Howard para derribar la feroz muralla defensiva de Golden State y llevar la final al definitivo Partido 7 en la Bahia."
            ]
        },
        "de": {
            "title": "WNBA Finals Spiel 6 Vorschau: Valkyries stehen 40 Minuten vor historischer Kroenung",
            "subtitle": "Golden State fuehrt 3:2 vor dem Gastspiel in Atlanta; Dream kaempfen um ihr Ueberleben und ein Spiel 7.",
            "excerpt": "Das Expansion-Team der Valkyries kann in der Nacht zum Freitag die sensationellste Premierensaison des modernen US-Sports vergolden.",
            "body": [
                "Die Golden State Valkyries greifen am Donnerstagabend, den 29. Oktober, nach den Sternen: Mit einer 3:2-Fuehrung reist das neue Team zu Spiel 6 der WNBA Finals nach Atlanta. Nach der defensiven Meisterleistung bei Spiel 5 (64:55) fehlt der Mannschaft von Trainerin Natalie Nakase nur noch ein Sieg, um als erstes Expansion-Team seit 1950 auf Anhieb Meister zu werden.",
                "Fuer das Atlanta Dream um Star Angel Reese geht es in der Gateway Center Arena um alles. Atlanta muss gegen die aggressive Verteidigung der Gaeste Luecken finden, um die Serie in ein dramatisches Spiel 7 am Sonntag in San Francisco zu retten."
            ]
        },
        "it": {
            "title": "Finali WNBA Gara 6: Valkyries a un passo dalla leggenda sul campo delle Dream",
            "subtitle": "Golden State avanti 3-2 vola in Georgia; Angel Reese e compagne costrette all'impresa per forzare Gara 7.",
            "excerpt": "La franchigia debuttante delle Valkyries puo completare giovedi la piu straordinaria cavalcata della storia dello sport americano.",
            "body": [
                "Le Golden State Valkyries scendono sul parquet della Gateway Center Arena giovedi 29 ottobre con la serie sul 3-2 e il match point per il titolo WNBA in tasca. Nessuna squadra debuttante ha mai trionfato al primo anno nella storia moderna degli sport professionistici statunitensi, e la formazione di Natalie Nakase e a soli 40 minuti dall'immortalita sportiva.",
                "Per le Atlanta Dream si tratta di un duello da dentro o fuori. Angel Reese, autentica dominatrice a rimbalzo, provera a caricarsi la squadra sulle spalle per contenere Gabby Williams e strappare la vittoria che porterebbe la contesa alla decisiva Gara 7 in California."
            ]
        },
        "pl": {
            "title": "Zapowiedz meczu 6 Finalow WNBA: Valkyries o krok od mistrzowskiego cudu w Atlancie",
            "subtitle": "Golden State prowadzi 3-2 przed meczem w Gateway Center; Angel Reese i Dream walcza o doprowadzenie do decydujacego meczu 7.",
            "excerpt": "Nowo powstaly zespol Valkyries moze w czwartek przypieczetowac najbardziej niesamowity debiutancki sezon w historii amerykanskiego sportu.",
            "body": [
                "Golden State Valkyries staja w czwartek 29 pazdziernika przed historyczna szansa w meczu numer 6 Finalow WNBA. Po zwyciestwie 64:55 w piatym starciu ekipa z San Francisco prowadzi w serii do czterech zwyciestw 3-2 i potrzebuje zaledwie jednej wygranej, by stac sie pierwszym zespolem od 1950 roku, ktory siegnal po tytul w debiutanckim sezonie.",
                "Atlanta Dream staje pod sciana we wlasnej hali w College Park. Angel Reese i Rhyne Howard musza przelamac zelazna defensywe rywalek, by wywalczyc zwyciestwo i wymusic siodmy, rozstrzygajacy mecz w niedziele w Chase Center."
            ]
        },
        "zh": {
            "title": "WNBA总决赛G6前瞻：女武神距历史神迹仅差40分钟，梦想队背水一战誓拖入抢七",
            "subtitle": "金州女武神大比分3-2客战亚特兰大；天使里斯率队在主场奋力抗争力求决胜局。",
            "excerpt": "作为新军的金州女武神队将在周四晚间向总冠军发起最后冲击，有望创造现代职业体育最不可思议的新军夺冠奇迹。",
            "body": [
                "2026年WNBA总决赛在10月29日周四迎来了最关键的第六场对决。金州女武神带着3-2的总比分客场挑战亚特兰大梦想。自1950年以来，北美四大职业体育联盟中还从未有任何一支新扩建球队能在成立元年夺得总冠军，女武神主帅中濑带领的铁血之师距离这一历史丰碑仅差最后一场胜利。",
                "对于主场作战的梦想队而言，今晚是不容有失的生死战。明星前锋安吉尔·里斯在总决赛中连续四场拿下两双，她必须联手外线核心霍华德冲破金州女武神的窒息防守，全力将总决赛拖入周日在旧金山进行的抢七大战。"
            ]
        },
        "ja": {
            "title": "WNBAファイナル第6戦展望：ヴァルキリーズが球団創設初年度の戴冠へ王手、ドリームは背水の陣",
            "subtitle": "ゴールデンステイトが3勝2敗でアトランタに乗り込む；エンジェル・リース擁するドリームは逆王手を目指す。",
            "excerpt": "エクスパンションチームのヴァルキリーズが、北米プロスポーツ史上最も奇跡的な初年度優勝まであと40分に迫っている。",
            "body": [
                "10月29日木曜日、WNBAファイナル第6戦がアトランタのゲートウェイ・センター・アリーナで開催される。第5戦を64-55の堅守で制し3勝2敗と王手をかけたゴールデンステイト・ヴァルキリーズは、1950年以来となるプロスポーツ新規参入初年度での完全制覇に挑む。",
                "一方のアトランタ・ドリームにとっては負ければ終わりの一戦となる。4試合連続ダブルダブルを記録しているエンジェル・リースと司令塔ライン・ハワードがチームを鼓舞し、サンフランシスコでの第7戦へ持ち込めるか注目が集まる。"
            ]
        },
        "ko": {
            "title": "WNBA 파이널 6차전 프리뷰: 발키리스, 창단 첫해 우승 신화까지 단 40분 남았다",
            "subtitle": "골든스테이트 3-2 리드 안고 애틀랜타 원정길; 엔젤 리스의 드림은 7차전 강제 총력전 선언.",
            "excerpt": "신생팀 골든스테이트 발키리스가 목요일 밤 애틀랜타에서 현대 스포츠 역사상 가장 위대한 창단 첫해 우승에 도전한다.",
            "body": [
                "2026 WNBA 파이널 6차전이 10월 29일 목요일 애틀랜타 게이트웨이 센터 아레나에서 열린다. 5차전에서 64-55의 숨 막히는 질식 수비로 3승 2패 우위를 점한 골든스테이트 발키리스는 단 1승만 추가하면 1950년 이후 메이저 프로 스포츠 사상 최초로 창단 원년 챔피언에 등극하게 된다.",
                "벼랑 끝에 몰린 애틀랜타 드림은 홈 팬들의 열광적인 응원을 등에 업고 반격에 나선다. 파이널 내내 더블더블을 기록 중인 엔젤 리스와 외곽 슈터 라인 하워드가 발키리스의 철벽 수비를 뚫어내고 일요일 샌프란시스코에서 열릴 최종 7차전으로 승부를 끌고 갈 수 있을지 주목된다."
            ]
        },
        "ar": {
            "title": "نهائي دوري السلة النسائي WNBA المباراة 6: فالكيريز على بعد 40 دقيقة من معجزة تاريخية",
            "subtitle": "غولدن ستيت يتقدم 3-2 في السلسلة أمام أتلانتا دريم الذي يقاتل من أجل فرض مباراة سابعة حاسمة.",
            "excerpt": "يقف فريق فالكيريز الصاعد حديثا على بعد خطوة واحدة من كتابة التاريخ والتتويج باللقب في أول مواسمه الاحترافية.",
            "body": [
                "تتجه أنظار عشاق كرة السلة مساء الخميس 29 أكتوبر إلى صالة غيتواي سنتر أرينا لمتابعة المواجهة السادسة في نهائي WNBA بين غولدن ستيت فالكيريز ومضيفه أتلانتا دريم. بعد انتصاره الدفاعي الصارم 64-55 في المباراة الخامسة، بات فالكيريز متقدما 3-2 في السلسلة وعلى بعد فوز وحيد من أن يصبح أول فريق حديث التأسيس يتوج باللقب في عامه الأول منذ عام 1950.",
                "وفي المقابل، يخوض أتلانتا دريم لقاء الفرصة الأخيرة بقيادة نجمته أنجيل ريس التي حققت أرقاما مزدوجة في أربع مباريات متتالية. وسيسعى دريم لاستغلال عاملي الأرض والجمهور لاختراق دفاعات فالكيريز وفرض مباراة سابعة فاصلة في سان فرانسيسكو يوم الأحد المقبل."
            ]
        }
    },

    "nfl-week8-tnf-preview-packers-host-panthers-lambeau-prime-time": {
        "fr": {
            "title": "NFL Semaine 8 TNF : Les Packers recoivent Carolina sous les projecteurs de Lambeau Field",
            "subtitle": "Jordan Love mene Green Bay (5-2) face a Bryce Young pour mettre la pression sur les Vikings invaincus.",
            "excerpt": "Le coup d'envoi de la 8e semaine de NFL sera donne jeudi soir dans le froid du Wisconsin entre les Packers et les Panthers.",
            "body": [
                "La huitieme semaine de NFL s'ouvre ce jeudi soir 29 octobre sous les lumieres mythiques de Lambeau Field avec le choc entre les Green Bay Packers (5-2) et les Carolina Panthers (3-4). Les Packers de Matt LaFleur, emmenes par un Jordan Love en grande forme (14 passes de touchdown), cherchent a maintenir la cadence infernale imposee par les Vikings de Minnesota, seuls invaincus de la ligue a 6-0.",
                "Pour Bryce Young et Carolina, ce deplacement dans l'enfer vert du Wisconsin constitue un test supreme. Les Panthers devront s'appuyer sur la puissance de course de Chuba Hubbard pour controler le tempo et proteger leur jeune quart-arriere de la redoutable pression exercee par Rashan Gary."
            ]
        },
        "es": {
            "title": "Previo NFL Semana 8 TNF: Packers reciben a Panthers bajo los focos de Lambeau Field",
            "subtitle": "Jordan Love guia a Green Bay (5-2) ante Bryce Young para presionar a los invictos Vikings en la NFC Norte.",
            "excerpt": "El Thursday Night Football abre la Semana 8 en el frio de Green Bay en un vibrante choque interdivisional.",
            "body": [
                "La Semana 8 de la NFL arranca este jueves 29 de octubre en el historico Lambeau Field con el duelo nocturno entre los Green Bay Packers (5-2) y los Carolina Panthers (3-4). Con los Minnesota Vikings liderando la division con marca perfecta de 6-0, Jordan Love y el ataque de Green Bay necesitan la victoria para no perder pisada en la carrera por los playoffs.",
                "En el bando visitante, Bryce Young encara la prueba mas dura de su campana al frente de los Panthers. Carolina necesitara un plan de juego impecable por tierra con Chuba Hubbard para mitigar el ataque exterior de Rashan Gary y silenciar a las 78.000 almas congregadas en Wisconsin."
            ]
        },
        "de": {
            "title": "NFL Woche 8 TNF Vorschau: Packers fordern Panthers im Lambeau Field heraus",
            "subtitle": "Jordan Love fuehrt Green Bay (5:2) gegen Bryce Young ins Flutlichtduell, um Druck auf die Vikings auszuueben.",
            "excerpt": "Das Thursday Night Football eroeffnet die achte NFL-Woche im frostigen Lambeau Field zwischen Green Bay und Carolina.",
            "body": [
                "Die achte Spielwoche der NFL beginnt am Donnerstagabend, den 29. Oktober, mit einem Klassiker im eiskalten Lambeau Field: Die Green Bay Packers (5:2) empfangen die Carolina Panthers (3:4). Jordan Love glaenzt in dieser Saison mit 14 Touchdown-Paessen und will den Rueckstand auf die noch ungeschlagenen Minnesota Vikings (6:0) in der NFC North weiter verkuerzen.",
                "Fuer Carolina und Spielmacher Bryce Young steht eine Mammutaufgabe bevor. Gegen die aggressive Pass-Rush-Linie um Rashan Gary muss Carolina zwingend auf ein starkes Laufspiel durch Chuba Hubbard setzen, um im vierten Viertel eine Siegchance zu wahren."
            ]
        },
        "it": {
            "title": "NFL Week 8 TNF preview: I Packers ospitano i Panthers nella notte di Lambeau Field",
            "subtitle": "Jordan Love guida Green Bay (5-2) contro Bryce Young per inseguire i Vikings primi e imbattuti.",
            "excerpt": "Il Thursday Night Football apre l'ottava giornata NFL nella suggestiva e gelida cornice del Lambeau Field.",
            "body": [
                "L'ottava settimana della NFL si apre giovedi sera 29 ottobre con la classica sfida di prime time al Lambeau Field tra i Green Bay Packers (5-2) e i Carolina Panthers (3-4). La formazione di casa punta sulla precisione di Jordan Love, gia autore di 14 touchdown, per tenere il passo dei Minnesota Vikings, ancora perfetti a quota 6 vittorie.",
                "I Panthers di Bryce Young cercano invece il colpo esterno per riportare il proprio record in parita a 4-4. La chiave della sfida sara la capacita della linea offensiva ospite di contenere l'esuberanza atletica di Rashan Gary e concedere tempo al giovane quarterback."
            ]
        },
        "pl": {
            "title": "Zapowiedz NFL Tydzien 8 TNF: Packers podejmuja Panthers w blasku swiatel Lambeau Field",
            "subtitle": "Jordan Love prowadzi Green Bay (5-2) przeciwko Bryce'owi Youngowi w pogoni za niepokonanymi Vikings.",
            "excerpt": "Czwartkowy mecz Thursday Night Football zainauguruje osmy tydzien rozgrywek NFL w chlodnym klimacie Green Bay.",
            "body": [
                "Tydzien 8 rozgrywek NFL rozpoczyna sie w czwartek 29 pazdziernika od pojedynku na legendarnym Lambeau Field, gdzie Green Bay Packers (5-2) zmierza sie z Carolina Panthers (3-4). Packers pod wodza Jordana Love'a, ktory rzucil juz 14 przylozen w sezonie, chca wywrzec presje na prowadzacych z bilansem 6-0 Minnesota Vikings.",
                "Dla Bryce'a Younga i zespolu Panthers wizyta w Wisconsin bedzie najtrudniejszym sprawdzianem jesieni. Goscie musza oprzec swoj plan na biegach Chuby Hubbarda, by kontrolowac zegar gry i neutralizowac presje wywierana przez formacje obronna gospodarzy."
            ]
        },
        "zh": {
            "title": "NFL第8周周四夜赛前瞻：包装工坐镇兰博球场迎战黑豹，向不败维京人施压",
            "subtitle": "乔丹·爱芙率领5胜2负的绿湾迎击布莱斯·杨，国联北区头名争夺战趋于白热化。",
            "excerpt": "NFL第八周在兰博球场的凛冽秋风中拉开战幕，绿湾包装工主场迎战卡罗来纳黑豹争取四连胜。",
            "body": [
                "NFL第8周常规赛于10月29日周四晚在威斯康星州著名的兰博球场点燃战火。5胜2负的绿湾包装工主场迎战3胜4负的卡罗来纳黑豹。由于明尼苏达维京人以6胜0负高居联盟唯一不败宝座，四分卫乔丹·爱芙必须率领全队全取胜利以维持对分区冠军的争夺。",
                "对于黑豹二年级四分卫布莱斯·杨而言，面对兰博球场近八万名狂热球迷以及拉珊·加里领衔的凶悍突前防线，将是一场巨大的职业考验。黑豹需要依靠哈伯德的地面推进控制控球时间，才有一线爆冷的希望。"
            ]
        },
        "ja": {
            "title": "NFL第8週TNF展望：パッカーズが名門ランボー・フィールドでパンサーズと激突",
            "subtitle": "ジョーダン・ラヴ率いる5勝2敗のグリーンベイがブライス・ヤングを迎え撃ち首位追撃へ。",
            "excerpt": "全米中継サーズデーナイトフットボールが開幕し、パッカーズが凍てつくウィスコンシンでパンサーズを迎え撃つ。",
            "body": [
                "10月29日木曜日の夜、NFL第8週の幕開けを飾るTNFが聖地ランボー・フィールドで開催される。ここまで14タッチダウンパスを記録しているジョーダン・ラヴ擁するグリーンベイ・パッカーズ（5勝2敗）は、6戦全勝の首位ミネソタ・バイキングスを射程圏内に捉え続けるため負けられない。",
                "敵地に乗り込むカロライナ・パンサーズ（3勝4敗）のQBブライス・ヤングにとっては、ラシャーン・ゲイリーらの強烈なパスラッシュをどう切り抜けるかが勝負の分かれ目となる。地上戦で時間をコントロールできるかが鍵を握る。"
            ]
        },
        "ko": {
            "title": "NFL 8주차 TNF 프리뷰: 패커스, 램보 필드 조명 아래 팬서스 상대로 야간 격돌",
            "subtitle": "조던 러브의 그린베이(5승 2패), 무패 바이킹스 추격 위해 브라이스 영의 캐롤라이나와 맞대결.",
            "excerpt": "NFL 8주차가 목요일 밤 위스콘신의 전설적인 램보 필드에서 패커스와 팬서스의 맞대결로 포문을 연다.",
            "body": [
                "NFL 8주차 일정이 10월 29일 목요일 밤 그린베이의 유서 깊은 램보 필드에서 펼쳐진다. 5승 2패를 기록 중인 그린베이 패커스는 14개의 터치다운 패스를 기록 중인 쿼터백 조던 러브의 지휘 아래 6전 전승의 미네소타 바이킹스를 맹추격하고 있다.",
                "원정길에 오른 캐롤라이나 팬서스(3승 4패)와 쿼터백 브라이스 영에게는 가혹한 시험대가 될 전망이다. 라샨 게리가 버티는 그린베이의 강력한 수비 라인을 상대로 추바 허바드의 지상 공격이 얼마나 효과를 거둘지가 승부의 열쇠다."
            ]
        },
        "ar": {
            "title": "دوري كرة القدم الأمريكية الأسبوع 8: باكرز يستضيف بانثرز تحت أضواء ملعب لامبو فيلد التاريخي",
            "subtitle": "جوردان لوف يقود غرين باي (5-2) في مواجهة برايس يونغ لمواصلة الضغط على فايكنغز المتصدر بدون هزيمة.",
            "excerpt": "تنطلق الجولة الثامنة من دوري NFL مساء الخميس في مواجهة قوية على الأراضي الجليدية في ويسكونسن.",
            "body": [
                "تفتتح منافسات الأسبوع الثامن من دوري كرة القدم الأمريكية مساء الخميس 29 أكتوبر على ملعب لامبو فيلد العريق بمباراة مرتقبة بين غرين باي باكرز (5-2) وكارولاينا بانثرز (3-4). ويسعى جوردان لوف، الذي أحرز 14 تمريرة حاسمة هذا الموسم، لقيادة باكرز نحو فوز حاسم لتضييق الخناق على مينيسوتا فايكنغز صاحب السجل الخالي من الهزائم (6-0).",
                "وفي المقابل يدخل برايس يونغ وفريقه بانثرز المباراة بحثا عن فوز يرفع رصيدهم إلى أربعة انتصارات. وسيتعين على الفريق الضيف الاعتماد على الركض الأرضي عبر تشوبا هوبارد لتخفيف الضغط الدفاعي الرهيب بقيادة راشان غاري والسيطرة على مجريات اللقاء."
            ]
        }
    },

    "atp-vienna-2026-alcaraz-sweeps-berrettini-reaches-quarter-finals": {
        "fr": {
            "title": "ATP Vienne 8es de finale : Carlos Alcaraz maitrise Matteo Berrettini et file en quarts",
            "subtitle": "Le no 2 mondial claque 28 coups gagnants et n'affronte aucune balle de break pour s'imposer 6-3, 6-4 a la Wiener Stadthalle.",
            "excerpt": "Carlos Alcaraz a livre une demonstration d'autorite sur le court interieur de Vienne en dominant nettement Berrettini jeudi.",
            "body": [
                "Carlos Alcaraz a envoye un signal fort au circuit en salle ce jeudi 29 octobre en dominant l'Italien Matteo Berrettini 6-3, 6-4 en huitiemes de finale du tournoi de Vienne. Sur le court rapide de la Wiener Stadthalle, le prodige espagnol de 23 ans n'a eu besoin que d'une heure et dix-huit minutes pour sceller sa qualification sans concéder la moindre balle de break.",
                "Imperturbable au service avec 84 pour cent de points gagnes derriere sa premiere balle et 28 coups gagnants, Alcaraz a etouffe la puissance adverse grace a des retours d'une longueur chirurgicale. Il rejoint en quarts de finale la tete de serie no 1 Alexander Zverev, tombeur de Marcos Giron en deux manches."
            ]
        },
        "es": {
            "title": "ATP Viena octavos: Carlos Alcaraz desarma a Matteo Berrettini y pisa los cuartos de final",
            "subtitle": "El murciano firma 28 golpes ganadores y no cede ni un punto de quiebre para vencer 6-3, 6-4 en el Wiener Stadthalle.",
            "excerpt": "Carlos Alcaraz ofrecio este jueves un autentico recital de saque y derecha en pista cubierta para liquidar a Berrettini.",
            "body": [
                "Carlos Alcaraz impuso su ley este jueves 29 de octubre en el Erste Bank Open de Viena tras deshacerse del peligroso italiano Matteo Berrettini por 6-3 y 6-4 en apenas 78 minutos. El numero dos del mundo cuajo un partido impecable, anotando 28 golpes ganadores por solo 9 errores no forzados y sin conceder una sola oportunidad de quiebre con su servicio.",
                "Con este triunfo, el pupilo espanol eleva a 4-1 su balance directo contra Berrettini y se cita en cuartos de final junto al aleman Alexander Zverev, que tambien avanzo tras superar al estadounidense Marcos Giron por 6-2 y 7-5 en la sesion vespertina."
            ]
        },
        "de": {
            "title": "ATP Wien Achtelfinale: Carlos Alcaraz fegt Matteo Berrettini vom Platz und steht im Viertelfinale",
            "subtitle": "Die Weltnummer 2 schlaegt 28 Winner und laesst keinen einzigen Breakball zu beim 6:3, 6:4 in der Wiener Stadthalle.",
            "excerpt": "Carlos Alcaraz demonstrierte am Donnerstag in Wien seine Hallenklasse und liess Aufschlaghuese Berrettini keine Chance.",
            "body": [
                "Carlos Alcaraz untermauerte am Donnerstagnachmittag, den 29. Oktober, seine Titelambitionen bei den Erste Bank Open in Wien. Der Spanier setzte sich im Achtelfinale mit 6:3 und 6:4 gegen den italienischen Hartplatz-Spezialisten Matteo Berrettini durch und benoetigte dafuer lediglich 78 Minuten hoechster Konzentration.",
                "Alcaraz agierte bei eigenem Aufschlag nahezu unantastbar, gewann 84 Prozent der Punkte nach dem ersten Service und wehrte jeden Angriffsversuch fruehzeitig ab. Neben Alcaraz erreichte auch Top-Favorit Alexander Zverev durch ein 6:2, 7:5 gegen Marcos Giron die Runde der letzten Acht."
            ]
        },
        "it": {
            "title": "ATP Vienna ottavi: Carlos Alcaraz supera Matteo Berrettini e vola ai quarti",
            "subtitle": "Il fuoriclasse spagnolo mette a referto 28 vincenti e concede zero palle break nel 6-3, 6-4 della Wiener Stadthalle.",
            "excerpt": "Prestazione autoritaria di Carlos Alcaraz che supera Berrettini in due set senza mai cedere il turno di battuta.",
            "body": [
                "Si ferma agli ottavi di finale la corsa di Matteo Berrettini all'Erste Bank Open di Vienna. Giovedi 29 ottobre l'azzurro si e arreso per 6-3, 6-4 di fronte a un sontuoso Carlos Alcaraz, capace di dominare gli scambi da fondo e di blindare il servizio senza mai concedere palle break nell'arco dell'intero incontro.",
                "Lo spagnolo ha fatto registrare 28 vincenti a fronte di appena 9 errori non forzati, strappando il servizio al romano nel quarto gioco del primo set e all'inizio del secondo. Insieme ad Alcaraz stacca il pass per i quarti anche Alexander Zverev, vittorioso 6-2, 7-5 sullo statunitense Marcos Giron."
            ]
        },
        "pl": {
            "title": "ATP Wieden 1/8 finalu: Carlos Alcaraz pewnie pokonuje Matteo Berrettiniego i melduje sie w cwiercfinale",
            "subtitle": "Wicelider rankingu posyla 28 winnerow i nie broni ani jednego break pointa przy zwyciestwie 6:3, 6:4 w Wiener Stadthalle.",
            "excerpt": "Carlos Alcaraz zaprezentowal w czwartek w Wiedniu tenis najwyzszej proby, nie dajac szans Berrettiniemu w dwoch setach.",
            "body": [
                "Carlos Alcaraz zrobil w czwartek 29 pazdziernika wielki krok w kierunku tytulu w wiedenskim turnieju Erste Bank Open, pokonujac wlasnego rywala Matteo Berrettiniego 6:3, 6:4 w zaledwie godzinie i 18 minutach. Hiszpan byl nie do ruszenia przy wlasnym podaniu, wygrywajac 84 procent pilek po pierwszym serwisie.",
                "Dzieki precyzyjnym returnom Alcaraz przelamal Wlocha w kluczowych momentach obu partii, notujac 28 uderzen konczacych. W cwiercfinale w Wiedniu zameldowal sie takze najwyzej rozstawiony Alexander Zverev, ktory pokonal Amerykanina Marcosa Girona 6:2, 7:5."
            ]
        },
        "zh": {
            "title": "ATP维也纳站16强战：阿尔卡拉斯直落两盘轻取贝雷蒂尼昂首挺进八强",
            "subtitle": "世界第二轰出28记制胜分且未送出任何破发点，耗时78分钟以6-3、6-4在维也纳室内赛过关。",
            "excerpt": "西班牙巨星阿尔卡拉斯在周四展现了统治级的室内硬地水准，完胜意大利名将贝雷蒂尼晋级八强。",
            "body": [
                "在10月29日周四下午进行的维也纳公开赛男单八分之一决赛中，世界排名第二的卡洛斯·阿尔卡拉斯以6-3、6-4横扫意大利名将贝雷蒂尼，强势闯入八强。全场比赛仅耗时1小时18分钟，阿尔卡拉斯在发球局展现出绝对统治力，一发得分率高达84%且全程未被逼出过任何破发点。",
                "面对以重炮发球闻名的贝雷蒂尼，阿尔卡拉斯依靠精准深远的接发球在两盘各完成一次关键破发，并打出了28记制胜分的华丽数据。头号种子兹维列夫也在同日以6-2、7-5击败吉隆晋级八强，维也纳站四分之一决赛群雄逐鹿。"
            ]
        },
        "ja": {
            "title": "男子テニスATPウィーン大会16強：アルカラスがベレッティーニをストレートで破り8強進出",
            "subtitle": "世界2位が28本のウィナーを放ちブレークポイントを一切与えず6-3、6-4で完勝。",
            "excerpt": "カルロス・アルカラスが木曜日の室内ハードコートで圧巻のテニスを披露し、イタリアのベレッティーニを一蹴した。",
            "body": [
                "10月29日木曜日、オーストリアのウィーンで開催されているエルステ・バンク・オープンで、世界ランク2位のカルロス・アルカラスがマッテオ・ベレッティーニを6-3、6-4で破り準々決勝進出を果たした。78分間の試合を通じてアルカラスはファーストサーブ時のポイント獲得率84％をマークし、一度もブレークポイントを与えなかった。",
                "アルカラスは28本のウィナーを量産し、両セットで1度ずつの決定的なブレークを奪って快勝。同日には第1シードのアレクサンダー・ズベレフもマルコス・ギロンを6-2、7-5で下しており、トリノでの最終戦を前に熱戦が続いている。"
            ]
        },
        "ko": {
            "title": "ATP 빈 16강: 카를로스 알카라스, 베레티니 완파하고 8강 안착",
            "subtitle": "세계 2위 알카라스, 브레이크 포인트 단 하나도 허용하지 않고 28개 위너 앞세워 6-3, 6-4 완승.",
            "excerpt": "카를로스 알카라스가 목요일 오스트리아 빈 스타트할레에서 완벽한 실내 코트 경기력을 과시하며 8강에 올랐다.",
            "body": [
                "카를로스 알카라스가 10월 29일 목요일 열린 ATP 500 에르스테 방크 오픈 16강전에서 이탈리아의 강서버 마테오 베레티니를 6-3, 6-4로 가볍게 제압했다. 1시간 18분 만에 경기를 끝낸 알카라스는 첫 서브 성공 시 84%의 높은 득점률을 기록하며 열 번의 서브 게임에서 단 한 번의 브레이크 위기도 맞지 않았다.",
                "정교한 스트로크로 28개의 위너를 꽂아 넣은 알카라스는 상대 전적을 4승 1패로 벌리며 강력한 우승 후보임을 입증했다. 톱시드 알렉산더 츠베레프 역시 마르코스 기론을 6-2, 7-5로 물리치고 알카라스와 함께 8강 대진에 이름을 올렸다."
            ]
        },
        "ar": {
            "title": "تنس بطولة فيينا ثمن النهائي: كارلوس ألكاراز يتفوق على ماتيو بيريتيني ويبلغ ربع النهائي",
            "subtitle": "المصنف الثاني عالميا يسجل 28 ضربة قاضية دون مواجهة أي نقطة كسر ليفوز 6-3 و6-4 في صالة فيينا.",
            "excerpt": "قدم الإسباني كارلوس ألكاراز استعراضا مبهرا في ملاعب فيينا المغلقة ليتجاوز عقبة الإيطالي بيريتيني بسهولة.",
            "body": [
                "وجه النجم الإسباني كارلوس ألكاراز رسالة قوية لمنافسيه في بطولة بنك إيرستيه المفتوحة في فيينا يوم الخميس 29 أكتوبر، بعد فوزه المستحق على الإيطالي ماتيو بيريتيني بمجموعتين دون رد 6-3 و6-4 في غضون 78 دقيقة فقط.",
                "وحافظ ألكاراز على إرساله بكفاءة تامة حيث حصد 84 في المئة من نقاط إرساله الأول ولم يواجه أي فرصة لكسر إرساله، مسجلا 28 ضربة قاضية. ولحق المصنف الأول ألكسندر زفيريف بالنجم الإسباني في ربع النهائي بعد تغلبه على الأمريكي ماركوس غيرون 6-2 و7-5."
            ]
        }
    },

    "f1-mexico-city-gp-2026-media-day-antonelli-confirms-car-12-altitude": {
        "fr": {
            "title": "F1 GP du Mexique : Antonelli confirme le numero 12 pour 2027 a l'aube d'un sacre historique",
            "subtitle": "Le prodige italien s'exprime a 2 285 m d'altitude et n'a besoin que d'une 9e place dimanche pour entrer dans l'histoire.",
            "excerpt": "Kimi Antonelli a annonce jeudi a Mexico qu'il conserverait son numero 12 fetiche en 2027 meme en cas de titre mondial des dimanche.",
            "body": [
                "L'Autodromo Hermanos Rodriguez a ete le theatre d'une conference de presse tres attendue ce jeudi 29 octobre, avec la presence de Kimi Antonelli a la veille du Grand Prix du Mexique. Avec 365 points et 123 longueurs d'avance sur son equipier George Russell, le pilote Mercedes de 20 ans n'a besoin que de marquer deux points (P9) dimanche pour devenir le plus jeune champion du monde de l'histoire de la F1.",
                "Antonelli a ravi les passionnes en annoncant qu'il conserverait son numero de course 12 la saison prochaine a l'image d'Ayrton Senna, refusant d'adopter le numero 1. Les ecuries se preparent desormais au defi unique de l'altitude mexicaine ou l'air raréfié met a rude epreuve les turbocompresseurs et le refroidissement des monoplaces."
            ]
        },
        "es": {
            "title": "F1 GP de Mexico conferencia de prensa: Antonelli confirma el dorsal 12 a las puertas de la gloria",
            "subtitle": "El joven italiano atiende a los medios a 2.285 metros sabiendo que un noveno puesto el domingo le corona campeon mundial.",
            "excerpt": "Kimi Antonelli confirmo este jueves en el Autodromo Hermanos Rodriguez que conservara el numero 12 si sella su primer titulo.",
            "body": [
                "El paddock de la Formula 1 vivio este jueves 29 de octubre una jornada de maxima expectacion en el Autodromo Hermanos Rodriguez con la conferencia de prensa de Kimi Antonelli. El piloto de Mercedes aventaja en 123 puntos a George Russell y necesita simplemente cruzar la meta en novena posicion el domingo para desbancar a Sebastian Vettel como el campeon del mundo mas joven de todos los tiempos.",
                "El talento italiano confirmo ante los medios que seguira luciendo su dorsal 12 en 2027 para honrar sus inicios y a su idolo Ayrton Senna. Mientras tanto, los ingenieros ajustan los paquetes aerodinamicos y los conductos de refrigeracion para afrontar la extrema altitud de la Ciudad de Mexico."
            ]
        },
        "de": {
            "title": "Formel 1 GP Mexiko Medientag: Antonelli bestaetigt Startnummer 12 vor moeglicher WM-Kroenung",
            "subtitle": "Das 20-jaehrige Ausnahmetalent benoetigt am Sonntag auf 2.285 Metern Hoehe nur Platz 9 fuer den historischen WM-Titel.",
            "excerpt": "Kimi Antonelli erklaerte am Donnerstag in Mexiko-Stadt, dass er auch als Weltmeister 2027 bei seiner Startnummer 12 bleiben wird.",
            "body": [
                "Am Autodromo Hermanos Rodriguez stand Kimi Antonelli am Donnerstag, den 29. Oktober, im Mittelpunkt des weltweiten Medieninteresses. Mit einem komfortablen Vorsprung von 123 Punkten auf George Russell reicht dem Mercedes-Piloten am Sonntag ein neunter Rang, um zum juengsten Formel-1-Weltmeister aller Zeiten aufzusteigen.",
                "Antonelli bestaetigte offiziell, dass er 2027 auf die traditionelle Startnummer 1 verzichten und wie einst Ayrton Senna bei seiner persoenlichen Nummer 12 bleiben wird. Unterdessen stehen die Motoren-Ingenieure vor der gewaltigen Herausforderung, Turbolader und Bremsen an die extrem duenne Hoehenluft von Mexiko-Stadt anzupassen."
            ]
        },
        "it": {
            "title": "F1 GP Messico conferenza stampa: Antonelli conferma il numero 12 a un passo dal titolo mondiale",
            "subtitle": "Il talento bolognese parla a 2.285 metri di quota: un nono posto domenica bastera per scrivere la storia della Formula 1.",
            "excerpt": "Kimi Antonelli ha annunciato giovedi a Citta del Messico che manterra il numero 12 sulla sua Mercedes anche nella stagione 2027.",
            "body": [
                "Tutti gli occhi del Circus erano puntati sull'Autodromo Hermanos Rodriguez giovedi 29 ottobre per la conferenza stampa ufficiale di Kimi Antonelli. Il ventenne fenomeno della Mercedes comanda la classifica con 365 punti e 123 lunghezze su George Russell: un piazzamento nei primi nove domenica gli garantirebbe matematicamente la corona mondiale piu giovane della storia.",
                "Davanti ai giornalisti Antonelli ha confermato la decisione di mantenere il suo iconico numero 12 anche nel 2027 sulle orme di Ayrton Senna. Nel frattempo i tecnici Mercedes hanno finalizzato i cofani motore dedicati per garantire il massimo raffreddamento nella rarefatta aria messicana a oltre 2.200 metri sul livello del mare."
            ]
        },
        "pl": {
            "title": "F1 GP Meksyku dzien medialny: Antonelli potwierdza numer 12 przed historyczna szansa na tytul",
            "subtitle": "Wloski talent potrzebuje zaledwie dziewiatego miejsca w niedziele na wysokosci 2285 m, by zostac mistrzem swiata.",
            "excerpt": "Kimi Antonelli oglosil w czwartek w Meksyku, ze w sezonie 2027 zachowa swoj tradycyjny numer startowy 12.",
            "body": [
                "W czwartek 29 pazdziernika na Autodromo Hermanos Rodriguez uwaga calego swiata motorsportu skupila sie na Kimim Antonellim. Majac 123 punkty przewagi nad Georgem Russellem, 20-letni kierowca Mercedesa stoi przed szansa przejscia do historii jako najmlodszy mistrz swiata Formuly 1 w dziejach w przypadku zajecia co najmniej dziewiatej pozycji w niedzielnym wyscigu.",
                "Wloch podkreslil na konferencji, ze w kolejnym sezonie nie zamierza zmieniac numeru 12 na mistrzowska jedynke, nawiazujac do tradycji Ayrtona Senny. Zespoly skupiaja sie obecnie na wyzwaniach zwiazanych z niska gestoscia powietrza na wysokosci ponad 2200 metrow, co stawia skrajne wymagania przed ukladami chlodzenia."
            ]
        },
        "zh": {
            "title": "F1墨西哥大奖赛媒体日：安东内利确认2027年保留12号车号，距加冕世界冠军仅一步之遥",
            "subtitle": "20岁意大利天才亮相海拔2285米高原赛道，周日正赛仅需拿到第9名即可打破最年轻世界冠军历史纪录。",
            "excerpt": "基米·安东内利周四在罗德里格斯兄弟赛道接受全球媒体采访，明确表示加冕后不会更换冠军1号车号。",
            "body": [
                "2026赛季F1墨西哥大奖赛媒体日于10月29日周四在罗德里格斯兄弟赛道举行，梅赛德斯新星基米·安东内利成为全场焦点。手握365分、领先队友拉塞尔123分的安东内利只要在周日正赛中获得前九名（2分），就将打破维特尔保持的纪录，成为F1历史上最年轻的车手世界冠军。",
                "在新闻发布会上，安东内利向全球媒体证实，即使夺得世界冠军，他在2027赛季也不会启用1号车号，而是继续使用象征偶像塞纳的12号。各车队目前正全力应对海拔2285米高原空气稀薄所带来的涡轮增压与刹车散热极端考验。"
            ]
        },
        "ja": {
            "title": "F1メキシコGP木曜会見：アントネッリが戴冠目前でカーナンバー「12」継続を明言",
            "subtitle": "標高2285メートルの高地で世界王座に王手；日曜決勝で9位以内ならF1史上最年少王者が誕生。",
            "excerpt": "キミ・アントネッリは木曜日、日曜日に初タイトルを確定させた場合でも2027年は伝統の12番を維持すると発表した。",
            "body": [
                "10月29日木曜日、アウトドローモ・エルマノス・ロドリゲスでF1メキシコGPの公式記者会見が行われ、キミ・アントネッリが登壇した。ラッセルに123点差をつけて首位を独走する20歳のメルセデス新星は、日曜日の決勝で9位以上に入れば、ベッテルの持つF1史上最年少チャンピオン記録を塗り替えることになる。",
                "アントネッリは会見で、王者ナンバー「1」は使用せず、憧れのアイルトン・セナにちなんだカーナンバー「12」を2027年も使い続けると明言した。チーム各社は空気密度の薄い超高地でのターボ冷却とブレーキ温度管理に万全を期している。"
            ]
        },
        "ko": {
            "title": "F1 멕시코 GP 미디어 데이: 안토넬리, 월드 챔피언 등극 앞두고 등번호 12번 유지 선언",
            "subtitle": "해발 2,285m 고지대에서 펼쳐질 결선서 9위만 차지해도 F1 역사상 최연소 월드 챔피언 등극 확정.",
            "excerpt": "키미 안토넬리가 목요일 멕시코시티에서 챔피언에 등극하더라도 2027년에도 자신의 고유 번호 12번을 달겠다고 밝혔다.",
            "body": [
                "10월 29일 목요일 아우토드로모 에르마노스 로드리게스에서 열린 2026 F1 멕시코 그랑프리 공식 기자회견에서 키미 안토넬리가 전 세계 취재진의 이목을 집중시켰다. 365점을 획득해 팀 동료 조지 러셀을 123점 차로 앞선 안토넬리는 일요일 결선에서 9위(2점) 이상만 기록하면 페텔의 기록을 깨고 역대 최연소 월드 챔피언에 오른다.",
                "안토넬리는 기자회견에서 우승하더라도 1번 대신 아일톤 세나를 오마주한 12번을 2027년에도 유지하겠다고 발표했다. 공기 밀도가 평지보다 현저히 낮은 고지대 특성상 터보차저와 브레이크 냉각 성능이 이번 주말 우승 경쟁의 최대 변수로 떠올랐다."
            ]
        },
        "ar": {
            "title": "فورمولا 1 جائزة المكسيك الكبرى: أنتونيللي يؤكد احتفاظه بالرقم 12 على مشارف التتويج العالمي",
            "subtitle": "النجم الإيطالي يتحدث من ارتفاع 2285 مترا ويكفيه المركز التاسع يوم الأحد ليدخل تاريخ رياضة المحركات.",
            "excerpt": "أكد كيمي أنتونيللي يوم الخميس في حلبة هيرمانوس رودريغيز تمسكه برقمه المفضل 12 في موسم 2027 حال فوزه باللقب.",
            "body": [
                "تركزت أنظار عشاق بطولة العالم لسباقات فورمولا 1 يوم الخميس 29 أكتوبر على حلبة أوتودرومو هيرمانوس رودريغيز خلال المؤتمر الصحفي لكيمي أنتونيللي. ومع تقدم سائق مرسيدس الإيطالي الشاب بفارق 123 نقطة على زميله جورج راسل، يحتاج أنتونيللي إلى نقطتين فقط (المركز التاسع) يوم الأحد ليتوج كأصغر بطل للعالم في تاريخ الفئة الأولى متخطيا رقم سيباستيان فيتيل.",
                "وأكد أنتونيللي لوسائل الإعلام العالمية تمسكه بالرقم 12 في الموسم المقبل تيمنا بأسطورة السباقات آيرتون سينا بدلا من استخدام الرقم 1 التقليدي. في غضون ذلك، تكثف الفرق جهودها للتغلب على تحديات الهواء الخفيف على ارتفاع يتجاوز 2200 متر لضمان كفاءة تبريد المحركات والمكابح."
            ]
        }
    },

    "pga-tour-mexico-open-2026-round1-pereda-leads-smotherman-shoots-66": {
        "fr": {
            "title": "PGA Tour VidantaWorld Mexico Open R1 : Pereda enflamme le public mexicain, Smotherman signe un 66",
            "subtitle": "Le golfeur local s'empare de la tete avec un superbe 65 ; Smotherman surfe sur son triomphe des Bermudes a un coup.",
            "excerpt": "Raul Pereda a fait vibrer les spectateurs a VidantaVallarta avec une carte de 65, talonné de pres par Austin Smotherman.",
            "body": [
                "Le public mexicain a vecu une premiere journee idyllique ce jeudi 29 octobre au VidantaWorld Mexico Open 2026. Sur le parcours dessine par Greg Norman a VidantaVallarta, l'enfant du pays Raul Pereda a pris seul les commandes du tournoi grace a une splendide carte de 65 (six sous le par), enfilant sept birdies sous les acclamations des galeries.",
                "A un petit coup seulement de la tete, l'Americain Austin Smotherman a confirme son insolente reussite apres sa victoire en playoff aux Bermudes dimanche dernier. Auteur d'un 66 sans trembler a egalite avec l'Anglais Aaron Rai, Smotherman s'installe idealement dans la course au trophee et aux 500 points FedExCup."
            ]
        },
        "es": {
            "title": "PGA Tour Mexico Open Ronda 1: Raul Pereda lidera en VidantaVallarta y Smotherman brilla con 66",
            "subtitle": "El veracruzano deleita a su gente con una tarjeta de 65 golpes; Smotherman mantiene su idilio con el juego a un golpe.",
            "excerpt": "Raul Pereda hizo vibrar a la aficion mexicana este jueves con 6 bajo par para liderar en solitario el VidantaWorld Mexico Open.",
            "body": [
                "Jornada de ensueño para el golf mexicano este jueves 29 de octubre en el arranque del VidantaWorld Mexico Open 2026. En el trazado Greg Norman Signature de VidantaVallarta, el veracruzano Raul Pereda firmo una ronda magistral de 65 impactos (6 bajo par), embocando siete birdies para situarse como lider en solitario ante el delirio de los aficionados locales.",
                "En la segunda posicion, a un solo golpe de Pereda, acechan el ingles Aaron Rai y el hombre del momento en el PGA Tour, el estadounidense Austin Smotherman. Llegando con la inercia ganadora de su triunfo en el desempate de Bermudas, Smotherman comenzo con tres birdies tempraneros para rubricar un 66 que promete una batalla apasionante durante el fin de semana."
            ]
        },
        "de": {
            "title": "PGA Tour VidantaWorld Mexico Open Runde 1: Raul Pereda fuehrt mit 65, Smotherman glaenzt mit 66",
            "subtitle": "Mexikanischer Lokalmatador verzueckt Heimfans; Bermuda-Champion Austin Smotherman lauert nur einen Schlag dahinter.",
            "excerpt": "Raul Pereda setzte sich am Donnerstag mit einer 65 an die Spitze in VidantaVallarta, dicht gefolgt von Austin Smotherman.",
            "body": [
                "Grosser Jubel bei den mexikanischen Golf-Fans am Donnerstag, den 29. Oktober: Bei der VidantaWorld Mexico Open 2026 uebernahm Lokalmatador Raul Pereda mit einer fantastischen 65er-Runde (sechs unter Par) die alleinige Fuehrung auf dem Greg Norman Signature Course in VidantaVallarta.",
                "Nur einen Schlag hinter Pereda teilen sich England-Profi Aaron Rai und der formstarke US-Amerikaner Austin Smotherman mit jeweils 66 Schlaegen Rang zwei. Smotherman nahm den Schwung seines packenden Playoff-Erfolgs bei der Bermuda Championship mit und unterstrich mit sechs Birdies seine aktuelle Spitzenform."
            ]
        },
        "it": {
            "title": "PGA Tour VidantaWorld Mexico Open R1: Raul Pereda guida a sorpresa, Smotherman apre con un 66",
            "subtitle": "Il giocatore di casa infiamma il pubblico con un 65; il vincitore delle Bermuda Smotherman e a una sola lunghezza.",
            "excerpt": "Grande prima giornata a VidantaVallarta con il messicano Pereda in testa e uno Smotherman inarrestabile a quota 66.",
            "body": [
                "Il golf messicano ha vissuto un giovedi da incorniciare il 29 ottobre nel primo giro del VidantaWorld Mexico Open 2026. Sul campo firmato da Greg Norman a VidantaVallarta, l'idolo di casa Raul Pereda ha firmato un brillante 65 (sei colpi sotto il par) con sette birdie, conquistando la vetta solitaria della classifica.",
                "Al secondo posto a quota 66 figurano l'inglese Aaron Rai e l'americano Austin Smotherman, reduce dallo spettacolare trionfo al playoff delle Bermuda. Smotherman ha confermato il suo momento magico mostrando una precisione letale sui green in paspalum e candidandosi per un altro successo autunnale."
            ]
        },
        "pl": {
            "title": "PGA Tour VidantaWorld Mexico Open Runda 1: Raul Pereda prowadzi po 65, Smotherman zaczyna z wynikiem 66",
            "subtitle": "Meksykanski faworyt zachwyca kibicow na wlasnym terenie; triumfator z Bermudow Austin Smotherman o uderzenie za liderem.",
            "excerpt": "Raul Pereda objal w czwartek prowadzenie w VidantaVallarta dzieki wynikowi 65, a w scislej czolowce zameldowal sie Smotherman.",
            "body": [
                "Meksykanscy kibice mieli powody do swietowania w czwartek 29 pazdziernika podczas pierwszej rundy turnieju VidantaWorld Mexico Open 2026. Na polu Greg Norman Signature Course w VidantaVallarta reprezentant gospodarzy Raul Pereda uzyskal swietny rezultat 65 uderzen (szesc ponizej par), notujac siedem birdie i prowadzac w stawce.",
                "Jedno uderzenie za liderem plasuja sie Anglik Aaron Rai oraz bedacy w wybitnej dyspozycji Amerykanin Austin Smotherman (obaj po 66). Zwyciezca z Bermudow rozpoczal runde od trzech birdie z rzedu, udowadniajac, ze zamierza walczyc o kolejne zwyciestwo w jesiennej serii FedExCup."
            ]
        },
        "zh": {
            "title": "美巡赛墨西哥公开赛首轮：本土球星佩雷达轰65杆独占榜首，斯莫瑟曼交66杆紧追不舍",
            "subtitle": "墨西哥名将在诺曼球场点燃主场热情；百慕大锦标赛冠军斯莫瑟曼延续火热手感仅落后一杆。",
            "excerpt": "劳尔·佩雷达在周四的墨西哥公开赛首轮交出低于标准杆6杆的65杆领跑，斯莫瑟曼以66杆并列次席。",
            "body": [
                "2026年美巡赛秋季赛墨西哥公开赛于10月29日周四在巴亚尔塔港正式打响。本土名将劳尔·佩雷达在格雷格·诺曼签名球场状态爆棚，抓下7只小鸟仅吞1记柏忌，以65杆（-6）的绝佳战绩单独领跑首轮记分榜，引发主场观众阵阵欢呼。",
                "刚刚在百慕大锦标赛通过三个加洞惊险夺冠的美国名将奥斯汀·斯莫瑟曼继续保持极佳状态，首轮狂抓6鸟打出66杆（-5），与英格兰名将阿隆·赖并列第二位。随着海风渐起，总奖金600万美元的赛事在首轮便呈现出极高水平的激烈对决。"
            ]
        },
        "ja": {
            "title": "PGAツアー・メキシコオープン初日：地元ペレダが65で単独首位発進、好調スモザーマンが66で猛追",
            "subtitle": "メキシコの星が7バーディの猛チャージ；バミューダ覇者スモザーマンも1打差の好位置につける。",
            "excerpt": "ラウル・ペレダが木曜日のヴィダンタ・ヴァジャルタで65をマークして単独首位に立ち、スモザーマンが追走する。",
            "body": [
                "10月29日木曜日、PGAツアーのヴィダンタワールド・メキシコオープンが開幕した。ヴィダンタ・ヴァジャルタのグレッグ・ノーマン設計コースで、地元メキシコのラウル・ペレダが7バーディ、1ボギーの6アンダー65をマークし、大声援の中で単独首位発進を決めた。",
                "前週のバミューダ選手権でプレーオフ3ホール目を制して優勝したばかりのオースティン・スモザーマンは、疲労の色も見せず6バーディを奪って5アンダー66を記録。イングランドのアーロン・ライと並ぶ2位タイにつけ、2週連続優勝へ向けて絶好の滑り出しを見せた。"
            ]
        },
        "ko": {
            "title": "PGA 투어 멕시코 오픈 1라운드: 라울 페레다 65타 단독 선두, 스모더맨 66타로 1타 차 추격",
            "subtitle": "멕시코 홈스타 페레다, 버디 7개 폭발하며 갤러리 열광; 버뮤다 우승자 스모더맨도 맹타 휘두르며 공동 2위.",
            "excerpt": "라울 페레다가 목요일 비단타 바야르타에서 6언더파 65타를 몰아치며 멕시코 오픈 첫날 단독 선두에 올랐다.",
            "body": [
                "2026 PGA 투어 비단타월드 멕시코 오픈 1라운드가 10月 29일 목요일 멕시코 비단타 바야르타의 그렉 노먼 시그니처 코스에서 막을 올렸다. 멕시코의 라울 페레다는 홈 팬들의 뜨거운 응원 속에 버디 7개를 쓸어 담으며 6언더파 65타를 기록, 단독 선두로 기분 좋게 출발했다.",
                "지난주 버뮤다 챔피언십에서 연장 3차전 접전 끝에 우승 트로피를 들어 올린 오스틴 스모더맨은 무서운 상승세를 이어갔다. 보기 1개와 버디 6개를 묶어 5언더파 66타를 친 스모더맨은 잉글랜드의 에런 라이와 함께 공동 2위에 올라 2주 연속 우승 가능성을 밝혔다."
            ]
        },
        "ar": {
            "title": "جولة بي جي إيه بطولة المكسيك المفتوحة الجولة 1: راؤول بيريدا يتصدر بـ 65 ضربة وسموذر مان يطارده بـ 66",
            "subtitle": "النجم المكسيكي يشعل حماس الجماهير بتسجيل 6 ضربات تحت المعدل؛ وبطل برمودا سموذر مان يواصل تألقه على بعد ضربة واحدة.",
            "excerpt": "خطف راؤول بيريدا صدارة الجولة الافتتاحية في بطولة فيدانتا وورلد المكسيك المفتوحة يوم الخميس وسط ملاحقة قوية من سموذر مان.",
            "body": [
                "عاش عشاق الغولف في المكسيك يوما استثنائيا يوم الخميس 29 أكتوبر مع انطلاق بطولة فيدانتا وورلد المكسيك المفتوحة 2026. فعلى ملعب غريغ نورمان في فيدانتا فايارتا، تألق المكسيكي راؤول بيريدا بتسجيل سبع ضربات بيردي لينهي اليوم بـ 65 ضربة (6 تحت المعدل) منفردا بالصدارة.",
                "وعلى بعد ضربة واحدة فقط، حل الأمريكي أوستن سموذر مان في المركز الثاني مناصفة مع الإنجليزي آرون راي بـ 66 ضربة. ودخل سموذر مان المنافسات بثقة هائلة بعد فوزه الملحمي في بطولة برمودا يوم الأحد الماضي، ليؤكد عزمه على مواصلة حصد نقاط كأس فيديكس الخريفية."
            ]
        }
    }
}

# Strict validation
for slug, langs in OCT29_STORIES.items():
    assert len(langs) == 9, f"{slug} missing some of the 9 languages: {list(langs.keys())}"
    for lang in ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        assert lang in langs, f"{slug} missing language {lang}"
        trans = langs[lang]
        for field in ["title", "subtitle", "excerpt", "body"]:
            assert field in trans, f"{slug} {lang} missing field {field}"
            val = trans[field]
            if isinstance(val, str):
                assert "—" not in val, f"Em-dash in {slug} {lang} {field}: {val}"
                assert "--" not in val, f"Double-hyphen in {slug} {lang} {field}: {val}"
            elif isinstance(val, list):
                for i, item in enumerate(val):
                    assert "—" not in item, f"Em-dash in {slug} {lang} {field}[{i}]: {item}"
                    assert "--" not in item, f"Double-hyphen in {slug} {lang} {field}[{i}]: {item}"

print("Verification passed! No em-dashes or double-hyphens found in any of the 6 stories across all 9 languages.")

snippet_parts = []
for slug, langs in OCT29_STORIES.items():
    formatted_slug = json.dumps(slug)
    snippet_parts.append(f"{formatted_slug}: {json.dumps(langs, ensure_ascii=False, indent=2)},")

snippet = "\n".join(snippet_parts) + "\n"

stories_file = "frontend/src/i18n/stories.ts"
with open(stories_file, "r", encoding="utf-8") as f:
    content = f.read()

target = "export const STORY_I18N: Record<string, LocMap> = {\n"
assert target in content, "Target line not found in stories.ts"

new_content = content.replace(target, target + snippet, 1)

with open(stories_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully injected October 29 translations into frontend/src/i18n/stories.ts")
