# Add 10-language translations for the 6 new stories on 2026-11-21.
import os
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
STORIES_TS = os.path.join(ROOT, "frontend", "src", "i18n", "stories.ts")

translations_data = {
  "atp-finals-turin-semifinals-saturday-alcaraz-shelton-zverev-medvedev-2026": {
    "fr": {
      "title": "Demies a Turin : Alcaraz defie Shelton, Zverev affronte Medvedev lors d'un samedi de gala",
      "subtitle": "Invaincus en poules, Carlos Alcaraz et Alexander Zverev visent la grande finale des Nitto ATP Finals a Turin.",
      "excerpt": "Le Super Samedi des Nitto ATP Finals 2026 propose Alcaraz contre Shelton a 14h00, puis le choc Zverev contre Medvedev a 20h30 a l'Inalpi Arena.",
      "body": [
        "Le dernier carre des Nitto ATP Finals 2026 promet une journee grandiose ce samedi 21 novembre a l'Inalpi Arena de Turin, avec deux affiches d'exception pour decider des finalistes de dimanche.",
        "A 14h00 CET, Carlos Alcaraz se mesure a la puissance de Ben Shelton. Vainqueur du groupe Ivan Lendl sans perdre le moindre set (3-0), l'Espagnol a impressionne face a Daniil Medvedev (6-2, 6-4) et Frances Tiafoe. De son cote, Shelton s'est hisse en demi-finale grace a sa deuxieme place dans le groupe John McEnroe (2-1), validee par un net succes 6-3, 6-4 contre Rafael Jodar jeudi.",
        "A 20h30 CET, Alexander Zverev retrouve son vieux rival Daniil Medvedev. Le numero un mondial allemand a survole le groupe McEnroe (3-0), s'imposant 6-4, 7-6 (5) face a Arthur Fils jeudi soir. Medvedev s'est assure la deuxieme place du groupe Lendl. Avec 1 500 points au classement et le prestigieux trophee de fin de saison en jeu, le spectacle sera total a Turin."
      ]
    },
    "es": {
      "title": "Semifinales en Turin: Alcaraz se mide a Shelton y Zverev choca con Medvedev en un super sabado",
      "subtitle": "Los invictos de grupo Carlos Alcaraz y Alexander Zverev buscan sellar su pase a la final de las Nitto ATP Finals en Turin.",
      "excerpt": "El Super Sabado de las Nitto ATP Finals 2026 presenta a Alcaraz contra Shelton a las 14:00 CET, seguido del clasico Zverev ante Medvedev a las 20:30 CET.",
      "body": [
        "El cuadro de las Nitto ATP Finals 2026 llega a su punto culminante este sabado 21 de noviembre en el Inalpi Arena de Turin, donde los cuatro mejores del mundo buscan el billete para la final dominical.",
        "A las 14:00 CET, Carlos Alcaraz abre la jornada ante el estadounidense Ben Shelton. El murciano domino de forma impecable el Grupo Ivan Lendl con tres victorias sin ceder un solo set (3-0), superando a Daniil Medvedev (6-2, 6-4) y Frances Tiafoe. Shelton aseguro la segunda plaza del Grupo John McEnroe con record de 2-1 tras vencer 6-3, 6-4 a Rafael Jodar el jueves.",
        "A las 20:30 CET, Alexander Zverev y Daniil Medvedev reeditan una de las rivalidades mas intensas del circuito. El numero 1 mundial cerro invicto el Grupo McEnroe (3-0) tras batir 6-4, 7-6 (5) a Arthur Fils. Medvedev llega con confianza tras sus triunfos sobre Tiafoe y Cobolli. Con 1.500 puntos en juego, Turin vivira una velada inolvidable."
      ]
    },
    "de": {
      "title": "Halbfinale in Turin: Alcaraz trifft auf Shelton, Zverev duelliert sich mit Medwedew am Super-Samstag",
      "subtitle": "Die ungeschlagenen Gruppensieger Carlos Alcaraz und Alexander Zverev peilen das Endspiel der Nitto ATP Finals in Turin an.",
      "excerpt": "Am Super-Samstag der Nitto ATP Finals 2026 trifft Alcaraz um 14:00 Uhr auf Shelton, ehe Zverev und Medwedew um 20:30 Uhr in der Inalpi Arena aufeinandertreffen.",
      "body": [
        "Die Runde der letzten Vier bei den Nitto ATP Finals 2026 verspricht am Samstag, 21. November, hochklassiges Tennis in der Inalpi Arena von Turin.",
        "Um 14:00 Uhr MEZ trifft der spanische Ausnahmekoenner Carlos Alcaraz auf Aufschlaghuene Ben Shelton. Alcaraz stuermte ohne Satzverlust mit 3-0 durch die Ivan-Lendl-Gruppe und bezwang unter anderem Medwedew (6-2, 6-4). Shelton loeste das Halbfinalticket als Zweiter der John-McEnroe-Gruppe (2-1) durch einen 6-3, 6-4-Erfolg gegen Rafael Jodar am Donnerstag.",
        "Um 20:30 Uhr MEZ kommt es zum Klassiker zwischen Alexander Zverev und Daniil Medwedew. Die deutsche Nummer eins blieb in der McEnroe-Gruppe mit 3-0 makellos und rang Arthur Fils am Donnerstag mit 6-4, 7-6 (5) nieder. Medwedew sicherte sich Rang zwei in der Lendl-Gruppe. Bei 1.500 Weltranglistenpunkten steht am Samstagabend in Turin alles auf dem Spiel."
      ]
    },
    "it": {
      "title": "Semifinali a Torino: Alcaraz sfida Shelton, Zverev contro Medvedev nel Super Sabato dell'Inalpi Arena",
      "subtitle": "I vincitori imbattuti dei gironi Carlos Alcaraz e Alexander Zverev cercano il pass per la finalissima delle Nitto ATP Finals a Torino.",
      "excerpt": "Super Sabato alle Nitto ATP Finals 2026 con Alcaraz opposto a Shelton alle 14:00, seguito dal big match Zverev contro Medvedev alle 20:30 a Torino.",
      "body": [
        "L'Inalpi Arena di Torino e pronta per un indimenticabile Super Sabato il 21 novembre, quando i quattro protagonisti rimasti si contenderanno l'accesso alla finale delle Nitto ATP Finals 2026.",
        "Nella prima semifinale alle 14:00 CET, Carlos Alcaraz affronta il potente mancino americano Ben Shelton. Lo spagnolo ha dominato il gruppo Ivan Lendl con un perfetto 3-0 senza cedere set, superando Medvedev (6-2, 6-4) e Tiafoe. Shelton ha conquistato il secondo posto nel girone John McEnroe con un record di 2-1 battendo Rafael Jodar 6-3, 6-4 giovedi.",
        "Alle 20:30 CET andra in scena il capitolo decisivo della rivalita tra Alexander Zverev e Daniil Medvedev. Il numero 1 del mondo tedesco ha vinto tutte e tre le sfide del girone McEnroe, compreso il 6-4, 7-6 (5) su Arthur Fils. Medvedev ha chiuso secondo nel girone Lendl. Con 1.500 punti e il titolo di maestro di fine anno in palio, Torino si prepara a una serata spettacolare."
      ]
    },
    "pl": {
      "title": "Polfinaly w Turynie: Alcaraz gra z Sheltonem, a Zverev walczy z Miedwiediewem w wielka sobote",
      "subtitle": "Niepokonani triumfatorzy grup Carlos Alcaraz i Alexander Zverev walcza o awans do finalu Nitto ATP Finals w Turynie.",
      "excerpt": "Super Sobota w Nitto ATP Finals 2026: Carlos Alcaraz mierzy sie z Benem Sheltonem o 14:00 CET, a Alexander Zverev gra z Daniilem Miedwiediewem o 20:30 CET.",
      "body": [
        "Walka o tytul mistrza konczacego sezon turnieju Nitto ATP Finals wkracza w decydujaca faze w sobote, 21 listopada, w torynskiej Inalpi Arena.",
        "O godzinie 14:00 CET Carlos Alcaraz zmierzy sie z amerykanskim bombardierem Benem Sheltonem. Hiszpan pewnie wygral grupe Ivana Lendla z kompletem zwyciestw bez straty seta (3-0), pokonujac miedzy innymi Miedwiediewa 6-2, 6-4. Shelton zajal drugie miejsce w grupie Johna McEnroe z bilansem 2-1 po czwartkowym zwyciestwie 6-3, 6-4 nad Rafaelem Jodarem.",
        "O 20:30 CET kibice zobacza kolejne starcie Aleksandra Zvereva z Daniilem Miedwiediewem. Lider rankingu Zverev zakonczyl grupe McEnroe z wynikiem 3-0 po wygranej 6-4, 7-6 (5) z Arthurem Filsem. Miedwiediew awansowal z drugiego miejsca grupy Lendla. Stawka 1500 punktow i prestizowy puchar gwarantuja ogromne emocje."
      ]
    },
    "zh": {
      "title": "都灵半决赛：阿尔卡拉斯迎战谢尔顿，兹维列夫大战梅德韦杰夫争夺决赛席位",
      "subtitle": "小组全胜出线的阿尔卡拉斯与兹维列夫力争在都灵年终总决赛超级星期六会师决战。",
      "excerpt": "2026年ATP年终总决赛迎来半决赛对决：阿尔卡拉斯于14:00对阵谢尔顿，兹维列夫于20:30再战梅德韦杰夫。",
      "body": [
        "11月21日周六，都灵伊纳尔皮体育馆迎来2026年ATP年终总决赛的半决赛争夺，四位顶级名将全力冲击周日冠军决战的入场券。",
        "下午14:00首场半决赛，伦德尔组头名卡洛斯·阿尔卡拉斯将对阵美国新星本·谢尔顿。阿尔卡拉斯在小组赛中展现出统治级状态，连克梅德韦杰夫（6-2、6-4）、蒂亚福与科博利，以一盘未失的3胜0负完美晋级。谢尔顿则在麦肯罗组以2胜1负紧随其后，在周四直落两盘击败霍达尔锁定四强。",
        "晚上20:30第二场半决赛，现世界第一亚历山大·兹维列夫将再次对决老对手梅德韦杰夫。德国名将在麦肯罗组以3战全胜领跑，周四晚顶住压力以6-4、7-6击败菲斯。梅德韦杰夫以伦德尔组第二名晋级。伴随着1500点积分与年终荣耀，都灵之夜注定高潮迭起。"
      ]
    },
    "ja": {
      "title": "トリノ準決勝：アルカラス対シェルトン、ズベレフ対メドベージェフの激突",
      "subtitle": "無敗でグループを首位通過したアルカラスとズベレフが、日曜日決勝進出を懸けて激突する。",
      "excerpt": "2026年Nitto ATPファイナルズのスーパーサタデー：14:00からアルカラス対シェルトン、20:30からズベレフ対メドベージェフが開催。",
      "body": [
        "11月21日土曜日、トリノのイナルピ・アリーナで2026年Nitto ATPファイナルズの準決勝が行われ、世界屈指の4選手が決勝進出を争います。",
        "午後2時開始の第1試合では、イワン・レンドル組を1セットも落とさず3勝0敗で首位通過したカルロス・アルカラスが、ジョン・マッケンロー組2位（2勝1负）のベン・シェルトンと対戦します。アルカラスはメドベージェフを6-2、6-4で破るなど絶好調を維持しています。",
        "午後8時30分開始の第2試合は、世界ランキング1位のアレクサンダー・ズベレフとダニール・メドベージェフによる屈指のライバル対決です。ズベレフは木曜夜にフィスを6-4、7-6で退け3連勝。メドベージェフも安定した戦いで4強入りを果たしました。1500ポイントと年間王者の栄冠を懸けた熱戦に注目です。"
      ]
    },
    "ko": {
      "title": "토리노 준결승: 알카라스 vs 셸턴, 츠베레프 vs 메드베데프 토요일 격돌",
      "subtitle": "조별리그 무패 1위 카를로스 알카라스와 알렉산더 츠베레프가 일요일 결승 진출을 놓고 맞붙습니다.",
      "excerpt": "2026 니토 ATP 파이널스 슈퍼 토요일: 14시 알카라스 vs 셸턴, 20시 30분 츠베레프 vs 메드베데프 준결승전 개막.",
      "body": [
        "11월 21일 토요일 이탈리아 토리노 이날피 아레나에서 2026 니토 ATP 파이널스 준결승전이 펼쳐지며 4강 진출자들이 일요일 결승행 티켓을 다툽니다.",
        "오후 2시(CET) 첫 번째 준결승에서는 이반 렌들 조를 무실세트 3전 전승으로 통과한 카를로스 알카라스가 미국의 강서버 벤 셸턴과 대결합니다. 알카라스는 메드베데프(6-2, 6-4) 등을 압도하며 완벽한 경기력을 뽐냈고, 셸턴은 2승 1패로 4강에 올랐습니다.",
        "오후 8시 30분에는 세계 1위 알렉산더 츠베레프와 다닐 메드베데프의 통산 라이벌전이 열립니다. 츠베레프는 맥켄로 조에서 아르튀르 피스를 꺾고 3전 전승을 기록했습니다. 랭킹 포인트 1500점과 시즌 최종 트로피가 걸린 토요일 밤의 열기가 절정에 달하고 있습니다."
      ]
    },
    "ar": {
      "title": "نصف نهائي تورينو: ألكاراز يواجه شيلتون وزفيريف يصطدم بميدفيديف في سبت الحسم",
      "subtitle": "متصدرا المجموعتين دون هزيمة كارلوس ألكاراز وألكسندر زفيريف يسعيان لحجز بطاقتي النهائي في البطولة الختامية بتورينو.",
      "excerpt": "السبت الكبير في ختام بطولات التنس 2026: ألكاراز يلاقي شيلتون في الثانية ظهرا، وزفيريف يصطدم بميدفيديف في الثامنة والنصف مساء بتوقيت تورينو.",
      "body": [
        "وصلت الإثارة ذروتها في صالة إينالبي أرينا بمدينة تورينو الإيطالية يوم السبت 21 نوفمبر، حيث يتنافس أربعة من عمالقة التنس لحجز مكان في المباراة النهائية يوم الأحد.",
        "في نصف النهائي الأول عند الساعة 14:00 بتوقيت وسط أوروبا، يلتقي الإسباني كارلوس ألكاراز مع الأمريكي القوي بن شيلتون. ألكاراز قدم أداء مبهرا في مجموعة إيفان ليندل محققا 3 انتصارات نظيفة دون خسارة أي مجموعة، بينما ضمن شيلتون المركز الثاني في مجموعة ماكنرو برصيد انتصارين وهزيمة.",
        "وفي قمة المساء عند الساعة 20:30، تتجدد المواجهة الكلاسيكية بين المصنف الأول عالميا ألكسندر زفيريف ودانييل ميدفيديف. زفيريف تصدر مجموعته بالعلامة الكاملة بعد فوزه على فيس 6-4 و7-6، بينما حسم ميدفيديف وصافة مجموعته بثبات. مع 1500 نقطة على المحك، تورينو موعودة بليلة تاريخية."
      ]
    }
  },
  "f1-las-vegas-gp-race-night-verstappen-pole-russell-strip-showdown-2026": {
    "fr": {
      "title": "Soir de course a Las Vegas : Verstappen herite de la pole aux cotes de Russell sur le Strip",
      "subtitle": "Kimi Antonelli etant sacre champion mais penalise sur la grille, Max Verstappen s'elancera en pole pour le grand prix nocturne au Nevada.",
      "excerpt": "Sous les neons scintillants du Strip de Las Vegas, Max Verstappen s'aligne en pole position devant George Russell pour la 21e manche de la saison.",
      "body": [
        "La tension monte au milieu du desert de Mojave alors que le Grand Prix de Formule 1 de Las Vegas 2026 s'apprete a rugir ce samedi 21 novembre a 22h00 locales (01h00 ET dimanche).",
        "Le trace ultra-rapide de 6,201 km a livre des qualifications spectaculaires. Si le jeune prodige Kimi Antonelli a signe le meilleur chrono absolu pour Mercedes, sa penalite de cinq places sur la grille le repousse au sixieme rang. Cette sanction propulse Max Verstappen en pole position au volant de sa Red Bull, avec George Russell a ses cotes en premiere ligne.",
        "Derriere eux, Charles Leclerc place sa Ferrari au troisieme rang aupres de Lando Norris. Avec Mercedes deja assuree du titre des constructeurs avec 652 points, la féroce bataille pour la place de dauphin retient toute l'attention : Verstappen (279) mene d'une courte tete sur Russell (262), Hamilton (261), Leclerc (249) et Norris (246)."
      ]
    },
    "es": {
      "title": "Noche de carrera en Las Vegas: Verstappen hereda la pole junto a Russell en el Strip",
      "subtitle": "Con Kimi Antonelli ya coronado campeon pero penalizado, Max Verstappen arranca en pole para el gran duelo nocturno a 50 vueltas en Nevada.",
      "excerpt": "Bajo las luces de neon del Strip de Las Vegas, Max Verstappen saldra desde la pole position por delante de George Russell en la ronda 21.",
      "body": [
        "La magia nocturna llega al desierto de Nevada con el Gran Premio de Las Vegas 2026, que arranca este sabado 21 de noviembre a las 22:00 hora local (01:00 ET del domingo).",
        "El veloz circuito urbano de 6,201 km deparo una calificacion emocionante. Aunque el flamante campeon Kimi Antonelli logro el mejor tiempo para Mercedes, una penalizacion de cinco puestos en parrilla desplaza al italiano al sexto cajon. Esto deja a Max Verstappen con la pole al frente de su Red Bull, compartiendo primera fila con George Russell.",
        "En la segunda fila arrancan Charles Leclerc con Ferrari y Lando Norris con McLaren. Con Mercedes ya proclamada campeona de constructores con 652 puntos, el gran atractivo radica en el subcampeonato de pilotos: Verstappen (279 puntos) aventaja por poco a Russell (262), Hamilton (261), Leclerc (249) y Norris (246)."
      ]
    },
    "de": {
      "title": "Renntag in Las Vegas: Verstappen erbt die Pole Position neben Russell auf dem Strip",
      "subtitle": "Kimi Antonelli ist bereits Weltmeister, muss aber wegen einer Strafe zurueck: Max Verstappen startet vom besten Platz in den 50-Runden-Nacht-GP.",
      "excerpt": "Im Flutlicht des Las Vegas Strip steht Max Verstappen auf der Pole Position vor George Russell fuer die 21. Runde der Formel-1-Saison.",
      "body": [
        "Mitternachtsspannung in der Mojave-Wueste: Der Grosse Preis von Las Vegas 2026 startet heute, Samstag, 21. November, um 22:00 Uhr Ortszeit (07:00 Uhr MEZ am Sonntagmorgen).",
        "Der 6,201 km lange Strip-Kurs sorgte fuer rasantes Qualifying-Tempo. Zwar erzielte der frisch gekroente Champion Kimi Antonelli fuer Mercedes die Bestzeit, doch eine Strafversetzung um fuenf Startplaetze wirft das Ausnahmetalent auf Rang sechs zurueck. Dadurch erbt Red-Bull-Star Max Verstappen die Pole Position neben George Russell in Startreihe eins.",
        "Dahinter lauern Charles Leclerc im Ferrari und Lando Norris im McLaren. Waehrend Mercedes mit 652 Punkten laengst als Konstrukteurs-Weltmeister feststeht, brennt der Kampf um Rang zwei: Verstappen (279) liegt knapp vor Russell (262), Hamilton (261), Leclerc (249) und Norris (246)."
      ]
    },
    "it": {
      "title": "Notte di gara a Las Vegas: Verstappen eredita la pole accanto a Russell sulla Strip",
      "subtitle": "Con Kimi Antonelli iridato ma penalizzato in griglia, Max Verstappen scatta dalla pole per la sfida notturna di 50 giri in Nevada.",
      "excerpt": "Sotto le mille luci della Strip di Las Vegas, Max Verstappen parte in pole davanti a George Russell per il Round 21, con il secondo posto mondiale in palio.",
      "body": [
        "Grande spettacolo nel deserto del Nevada con il Gran Premio di Las Vegas 2026, al via sabato 21 novembre alle 22:00 locali (07:00 italiane di domenica).",
        "Il tracciato cittadino di 6,201 km ha regalato qualifiche ad altissima velocita. Nonostante il neocampione Kimi Antonelli abbia firmato il giro piu veloce su Mercedes, una penalita di cinque posizioni lo fa arretrare al sesto posto in griglia. La pole position va quindi a Max Verstappen su Red Bull, affiancato da George Russell in prima fila.",
        "In seconda fila scatteranno Charles Leclerc su Ferrari e Lando Norris su McLaren. Con il titolo costruttori gia assegnato a Mercedes a quota 652 punti, tutti gli occhi sono puntati sul duello per il secondo posto piloti: Verstappen (279) precede di poco Russell (262), Hamilton (261), Leclerc (249) e Norris (246)."
      ]
    },
    "pl": {
      "title": "Noc wyscigu w Las Vegas: Verstappen przejmuje pole position obok Russella na Stripie",
      "subtitle": "Kimi Antonelli ma juz tytul, lecz po karze na starcie to Max Verstappen rusza z pole position do 50-okrazeniowego nocnego wyscigu.",
      "excerpt": "W blasku neonow Las Vegas Strip Max Verstappen wystartuje z pole position przed George'em Russellem do 21. rundy sezonu Formuly 1.",
      "body": [
        "Wielkie emocje na pustyni Mojave: Grand Prix Las Vegas 2026 wystartuje w sobote, 21 listopada, o godzinie 22:00 czasu lokalnego (07:00 w niedziele czasu polskiego).",
        "Tor uliczny o dlugosci 6,201 km byl swiadkiem kapitalnych kwalifikacji. Najszybszy czas wykrecil nowy mistrz swiata Kimi Antonelli w barwach Mercedesa, jednak kara cofniecia o piec pozycji oznacza dla niego start z szostego pola. Dzieki temu z pole position ruszy Max Verstappen z Red Bulla, majac obok siebie George'a Russella.",
        "W drugim rzedzie ustawia sie Charles Leclerc w Ferrari i Lando Norris w McLarenie. Mercedes z 652 punktami zapewnil juz sobie mistrzostwo konstruktorow, dlatego najciekawiej zapowiada sie walka o wicemistrzostwo kierowcow: Verstappen (279) broni przewagi nad Russellem (262), Hamiltonem (261), Leclercem (249) i Norrisem (246)."
      ]
    },
    "zh": {
      "title": "拉斯维加斯大奖赛正赛之夜：维斯塔潘继承杆位，与拉塞尔头排并排发车",
      "subtitle": "虽然新科世界冠军安东内利遭遇罚退，维斯塔潘将在今晚拉斯维加斯大道50圈夜战中从杆位起步。",
      "excerpt": "在内华达拉斯维加斯大道的璀璨霓虹下，维斯塔潘力压拉塞尔夺得第21站发车首位，年度亚军争夺战一触即发。",
      "body": [
        "11月21日周六当地时间22:00（北京时间周日下午14:00），2026赛季F1拉斯维加斯大奖赛将在莫哈韦沙漠的霓虹夜空下打响50圈正赛对决。",
        "全长6.201公里的拉斯维加斯街道赛道在排位赛中刷新了速度极限。尽管新科世界冠军基米·安东内利代表梅赛德斯做出了全场最快圈速，但由于此前未执行的5位发车罚退，这位超新星正赛只能从第6位起步。红牛车手维斯塔潘顺理成章接过杆位，并与梅赛德斯车手拉塞尔共享头排。",
        "第二排发车的是法拉利车手勒克莱尔与迈凯伦车手诺里斯。梅赛德斯车队已凭借652分提前卫冕车队总冠军，车手年度亚军之争成为下半赛季最大悬念：维斯塔潘（279分）面对拉塞尔（262分）、汉密尔顿（261分）、勒克莱尔（249分）以及诺里斯（246分）的强力追击。"
      ]
    },
    "ja": {
      "title": "ラスベガスGP決勝の夜：ペナルティでフェルスタッペンがポール獲得、ラッセルとフロントロー",
      "subtitle": "王者アントネッリのグリッド降格により、フェルスタッペンが今夜50周のラスベガス夜間決勝で先頭からスタートする。",
      "excerpt": "ラスベガス・ストリップの華やかな照明の下、フェルスタッペンがポールポジションを獲得し、ドライバーズ2位争いが白熱する。",
      "body": [
        "11月21日土曜日現地時間午後10時、2026年F1第21戦ラスベガスGPの決勝がストリップのきらめく夜景の中でスタートします。",
        "全長6.201kmの超高速ストリートコースで行われた予選では、メルセデスの王者キミ・アントネッリがトップタイムを記録したものの、5グリッド降格ペナルティにより6番手スタートに後退。これによりレッドブルのマックス・フェルスタッペンがポールポジションに繰り上がり、ジョージ・ラッセルとフロントローに並びます。",
        "セカンドローにはルクレールとノリスが並びます。メルセデスが652ポイントでコンストラクターズ選手権を制圧した今、焦点はドライバーズランキング2位争いへ。フェルスタッペン（279点）を追うラッセル（262点）、ハミルトン（261点）、ルクレール（249点）、ノリス（246点）の激突が見逃せません。"
      ]
    },
    "ko": {
      "title": "라스베이거스 GP 결선: 페르스타펜 폴 포지션 승계, 러셀과 스트립 프런트로 출발",
      "subtitle": "챔피언 안토넬리의 그리드 페널티로 막스 페르스타펜이 오늘 밤 50랩 네온 레이스에서 폴 포지션으로 나섭니다.",
      "excerpt": "라스베이거스 스트립의 화려한 불빛 아래, 페르스타펜이 21라운드 결선에서 조지 러셀을 제치고 맨 앞자리에서 출발합니다.",
      "body": [
        "11월 21일 토요일 현지 시간 밤 10시, 모하비 사막을 배경으로 2026 F1 라스베이거스 그랑프리 본선 레이스가 화려하게 펼쳐집니다.",
        "길이 6.201km의 초고속 서킷 예선에서 메르세데스의 키미 안토넬리가 가장 빠른 랩타임을 기록했으나, 5그리드 강등 페널티로 인해 6위로 밀려났습니다. 이에 따라 레드불의 막스 페르스타펜이 폴 포지션을 차지하며 메르세데스의 조지 러셀과 함께 프런트로를 장악했습니다.",
        "그 뒤를 이어 르클레르와 노리스가 2열에서 출발합니다. 메르세데스가 652점으로 컨스트럭터 챔피언을 확정한 가운데, 드라이버 부문 2위 경쟁이 치열합니다. 페르스타펜(279점)과 러셀(262점), 해밀턴(261점), 르클레르(249점), 노리스(246점) 간의 5파전이 전개됩니다."
      ]
    },
    "ar": {
      "title": "ليلة سباق جائزة لاس فيغاس الكبرى: فيرستابن يرث قطب الانطلاق إلى جانب راسل في قطاع ذا ستريب",
      "subtitle": "بعد تتويج أنتونيللي باللقب ومعاقبته بالتراجع على شبكة الانطلاق، ماكس فيرستابن ينطلق أولا في سباق الـ 50 لفة تحت أضواء النيون.",
      "excerpt": "تحت أضواء قطاع ذا ستريب الساحرة في لاس فيغاس، يقف ماكس فيرستابن في قطب الانطلاق أمام جورج راسل في الجولة 21.",
      "body": [
        "تتجه أنظار عشاق السرعة نحو صحراء نيفادا حيث ينطلق سباق جائزة لاس فيغاس الكبرى 2026 مساء السبت 21 نوفمبر في تمام العاشرة ليلا بالتوقيت المحلي.",
        "شهدت حلبة الشوارع البالغ طولها 6.201 كم تصفيات بالغة الإثارة. ورغم أن البطل المتوج كيمي أنتونيللي سجل أسرع لفة لمرسيدس، إلا أن عقوبة التراجع خمسة مراكز أسقطته للمركز السادس. منح ذلك سائق ريد بول ماكس فيرستابن قطب الانطلاق الأول ليجاور جورج راسل في الصف الأمامي.",
        "وينطلق شارل لوكلير ولاندو نوريس من الصف الثاني. ومع حسم مرسيدس للقب الصانعين برصيد 652 نقطة، يتركز الصراع على وصافة السائقين: فيرستابن (279 نقطة) يتقدم بفارق ضئيل أمام راسل (262)، هاميلتون (261)، لوكلير (249) ونوريس (246)."
      ]
    }
  },
  "premier-league-fulham-lead-man-city-etihad-muniz-newcastle-arsenal-2026": {
    "fr": {
      "title": "Retour de la Premier League : Fulham surprend Manchester City d'entree a l'Etihad avant Newcastle-Arsenal",
      "subtitle": "Rodrigo Muniz donne l'avantage a Fulham a l'Etihad Stadium alors que la 11e journee de Premier League demarre sur les chapeaux de roue.",
      "excerpt": "Rodrigo Muniz marque de la tete a la 16e minute et permet a Fulham de mener 1-0 face a Manchester City, tandis qu'Arsenal se prepare a defier Newcastle.",
      "body": [
        "La Premier League a repris ses droits ce samedi 21 novembre apres la treve internationale, et le spectacle a commence aussitot a l'Etihad Stadium lors du coup d'envoi matinal.",
        "Fulham a fait sensation en ouvrant le score des la 16e minute sur la pelouse du champion Manchester City. Sur un centre precis d'Antonee Robinson, Rodrigo Muniz a trompe Ederson d'une superbe tete piquee. Malgre une domination de Pep Guardiola dans la possession, les Londoniens menacent en contre-attaque.",
        "Cette 11e journee s'annonce capitale au sommet du classement. Le leader Arsenal (27 points) se deplace a St. James' Park pour y defier Newcastle a 17h30 GMT. Alors que Brighton occupe une surprenante 2e place avec 22 points et que City reste bloque a 21 points, tout faux pas mancunien offrirait une voie royale aux Gunners."
      ]
    },
    "es": {
      "title": "Vuelve la Premier League: Fulham sorprende de inicio al Manchester City en el Etihad antes del Newcastle-Arsenal",
      "subtitle": "Rodrigo Muniz adelanta al Fulham en el Etihad Stadium en el arranque de la jornada 11 tras el paron internacional.",
      "excerpt": "Rodrigo Muniz marca de cabeza en el minuto 16 para poner al Fulham 1-0 sobre el Manchester City, mientras el lider Arsenal visita Newcastle.",
      "body": [
        "La Premier League regreso a la accion este sabado 21 de noviembre tras la ventana de selecciones, con sorpresa inmediata en el Etihad Stadium.",
        "El Fulham conmociono a los aficionados locales al tomar ventaja 1-0 en el minuto 16 gracias a un cabezazo letal de Rodrigo Muniz tras un envio de Antonee Robinson. Los de Pep Guardiola monopolizan el balon, pero el orden tactico de Marco Silva mantiene a raya al City en este duelo clave.",
        "Los focos se trasladaran despues a St. James' Park a las 17:30 GMT, donde el lider Arsenal (27 puntos) expone su ventaja ante el Newcastle. Con el Brighton segundo con 22 puntos y el Manchester City con 21, cualquier tropiezo de los locales podria consolidar el mando de los Gunners."
      ]
    },
    "de": {
      "title": "Premier League Comeback: Fulham ueberrascht Manchester City frueh im Etihad vor Newcastle gegen Arsenal",
      "subtitle": "Rodrigo Muniz koepft Fulham im Etihad Stadium frueh in Fuehrung, waehrend Matchweek 11 nach der Laenderspielpause startet.",
      "excerpt": "Rodrigo Muniz trifft in der 16. Minute zur 1:0-Fuehrung fuer Fulham gegen Manchester City, waehrend Tabellenfuehrer Arsenal nach Newcastle reist.",
      "body": [
        "Die Premier League ist zurueck: Nach der Laenderspielpause begann der 11. Spieltag am Samstag, 21. November, mit einem Paukenschlag im Etihad Stadium.",
        "Fulham schockte Meister Manchester City mit der fruehen Fuehrung in der 16. Minute, als Rodrigo Muniz eine Flanke von Antonee Robinson per Kopf im Tor von Ederson unterbrachte. Pep Guardiolas Elf erhoeht den Druck, doch die Londoner verteidigen leidenschaftlich.",
        "Um 17:30 Uhr GMT wartet das naechste Highlight: Tabellenfuehrer Arsenal (27 Punkte) gastiert bei Newcastle United im St. James' Park. Da Brighton mit 22 Punkten Zweiter ist und City bei 21 Punkten steht, waere ein Ausrutscher der Citizens ein herber Daempfer im Titelrennen."
      ]
    },
    "it": {
      "title": "Ritorno della Premier League: Fulham a sorpresa in vantaggio all'Etihad sul City prima di Newcastle-Arsenal",
      "subtitle": "Rodrigo Muniz porta avanti il Fulham all'Etihad Stadium nella prima sfida dell'11ª giornata dopo la pausa nazionali.",
      "excerpt": "Rodrigo Muniz sblocca il match al 16' e porta il Fulham sull'1-0 contro il Manchester City, mentre la capolista Arsenal fa visita al Newcastle.",
      "body": [
        "Ritorno col botto per la Premier League sabato 21 novembre dopo la sosta per le nazionali: subito brividi all'Etihad Stadium nel lunch match.",
        "Il Fulham gela il Manchester City al 16' con un colpo di testa perentorio di Rodrigo Muniz su traversone di Antonee Robinson. La formazione di Pep Guardiola ha preso d'assalto l'area avversaria, ma la squadra di Marco Silva resiste con ordine.",
        "Nel pomeriggio occhi puntati su St. James' Park alle 17:30 GMT per la sfida tra Newcastle e la capolista Arsenal (27 punti). Con il Brighton secondo a quota 22 e il Manchester City a 21, la lotta per la vetta inglese e incandescente."
      ]
    },
    "pl": {
      "title": "Powrot Premier League: Fulham zaskakuje Manchester City na Etihad przed hitem Newcastle - Arsenal",
      "subtitle": "Rodrigo Muniz daje Fulham prowadzenie na Etihad Stadium na inauguracje 11. kolejki Premier League po przerwie reprezentacyjnej.",
      "excerpt": "Rodrigo Muniz trafia glowa w 16. minucie i Fulham prowadzi 1:0 z Manchesterem City, podczas gdy liderujacy Arsenal zagra z Newcastle.",
      "body": [
        "Premier League powrocila w sobote, 21 listopada, a mecz otwarcia 11. kolejki na Etihad Stadium przyniosl blyskawiczna sensacje.",
        "Fulham objelo prowadzenie 1:0 w 16. minucie po znakomitym uderzeniu glowa Rodrigo Muniza, ktory wykorzystal dosrodkowanie Antonee Robinsona. Podopieczni Pepa Guardioli przewazaja w posiadaniu pilki, lecz goscie groznie kontratakuja.",
        "O 17:30 GMT oczy kibicow zwroca sie na St. James' Park, gdzie liderujacy Arsenal (27 pkt) zmierzy sie z Newcastle United. Przy drugim miejscu Brighton (22 pkt) i 21 punktach City, kazde potkniecie faworytow moze zadecydowac o losach jesieni."
      ]
    },
    "zh": {
      "title": "英超重燃战火：富勒姆伊蒂哈德客场闪击曼城，领头羊阿森纳客战纽卡斯尔",
      "subtitle": "国际比赛日后英超第11轮揭幕战，罗德里戈·穆尼斯头槌破门助富勒姆客场反客为主领先曼城。",
      "excerpt": "穆尼斯在第16分钟打破僵局助富勒姆客场1-0领先曼城，榜首阿森纳稍后将迎来客战纽卡斯尔的硬仗。",
      "body": [
        "11月21日周六，随着国际比赛日落幕，英超联赛战火重燃，伊蒂哈德球场的早场对决便爆出冷门气息。",
        "客场作战的富勒姆在第16分钟先声夺人，巴西前锋罗德里戈·穆尼斯接安东尼·罗宾逊传中头球破门，攻破埃德森把守的大门。尽管瓜迪奥拉的曼城占据了场上绝对控球优势，但马尔科·席尔瓦调教的客队防线固若金汤。",
        "本轮争冠格局极为胶着。目前领跑积分榜的阿森纳（27分）将于格林威治时间17:30客场挑战纽卡斯尔联队。在布莱顿以22分位居次席、曼城积21分紧追的情况下，伊蒂哈德球场的战果将直接影响争冠走势。"
      ]
    },
    "ja": {
      "title": "プレミアリーグ再開：フラムがエティハドでマンCから先制点、首位アーセナルはニューカッスル戦へ",
      "subtitle": "代表ウィーク明けの第11節、ムニスのヘディングでフラムがマンチェスター・シティ相手にアウェイで先制。",
      "excerpt": "フラムのムニスが16分に先制弾を奪いマンCに1-0とリード。首位アーセナルはセント・ジェームズ・パークでの難敵戦を控える。",
      "body": [
        "代表戦中断期間が明け、11月21日土曜日にプレミアリーグ第11節が再開。エティハド・スタジアムのランチタイムキックオフで早くも波乱の幕開けとなりました。",
        "前半16分、フラムのFWロドリゴ・ムニスがロビンソンのクロスから完璧なヘディングシュートを叩き込み、王者マンチェスター・シティから先制点を奪取。グアルディオラ率いるホームチームは反撃を試みるものの、フラムの堅守に苦しんでいます。",
        "今節は首位攻防戦も注目です。27ポイントで首位を快走するアーセナルは、日本時間深夜2時30分から難所セント・ジェームズ・パークでニューカッスルと激突。22点のブライトン、21点のマンチェスター・Cの追撃を受ける中、首位固めを狙います。"
      ]
    },
    "ko": {
      "title": "프리미어리그 재개: 풀럼, 에티하드 원정서 맨시티에 기습 선제골... 아스널은 뉴캐슬 원정",
      "subtitle": "A매치 휴식기 직후 열린 11라운드, 호드리구 무니스의 16분 헤더 골로 풀럼이 맨시티 원정서 1-0 리드.",
      "excerpt": "풀럼이 전반 16분 무니스의 헤더 골로 맨체스터 시티에 1-0으로 앞서가는 가운데, 1위 아스널은 뉴캐슬 원정을 치릅니다.",
      "body": [
        "11월 21일 토요일 A매치 휴식기를 마친 잉글랜드 프리미어리그 11라운드가 재개되자마자 에티하드 스타디움에서 이변의 조짐이 나타났습니다.",
        "원정팀 풀럼은 전반 16분 안토니 로빈슨의 크로스를 받은 호드리구 무니스가 완벽한 헤더로 골망을 흔들며 맨체스터 시티에 1-0 선제골을 뽑아냈습니다. 펩 과르디올라 감독의 맨시티가 볼 점유율을 끌어올리며 맹공을 퍼붓고 있습니다.",
        "한편 리그 선두 아스널(승점 27)은 17시 30분(GMT) 세인트 제임스 파크에서 난적 뉴캐슬 유나이티드와 맞붙습니다. 2위 브라이튼(승점 22)과 3위 맨시티(승점 21)의 추격이 이어지는 가운데 이번 라운드 결과에 관심이 집중됩니다."
      ]
    },
    "ar": {
      "title": "عودة الدوري الإنجليزي: فولهام يفاجئ مانشستر سيتي بهدف مبكر في الاتحاد قبل قمة نيوكاسل وأرسنال",
      "subtitle": "رودريغو مونيز يمنح فولهام التقدم في ملعب الاتحاد مع استئناف مباريات الجولة 11 بعد انتهاء التوقف الدولي.",
      "excerpt": "مونيز يسجل برأسية في الدقيقة 16 ليمنح فولهام التقدم 1-0 على مانشستر سيتي، بينما يتأهب المتصدر أرسنال لزيارة صعبة إلى نيوكاسل.",
      "body": [
        "عادت عجلة الدوري الإنجليزي الممتاز للدوران يوم السبت 21 نوفمبر عقب نهاية التوقف الدولي، واشتعلت الإثارة مبكرا على أرضية ملعب الاتحاد.",
        "فاجأ فولهام مضيفه مانشستر سيتي بتسجيل هدف مباغت في الدقيقة 16 برأسية متقنة من البرازيلي رودريغو مونيز إثر عرضية من أنتوني روبنسون. ورغم سيطرة كتيبة بيب غوارديولا على الكرة، إلا أن خطة ماركو سيلفا الدفاعية تصنع الفارق حتى الآن.",
        "وتتجه الأنظار لاحقا إلى ملعب سانت جيمس بارك في تمام 17:30 بتوقيت غرينتش لمتابعة المتصدر أرسنال (27 نقطة) في ضيافة نيوكاسل. وفي ظل احتلال برايتون للمركز الثاني (22 نقطة) وسيتي الثالث (21 نقطة)، فإن أي تعثر قد يوسع الفارق لصالح المدفعجية."
      ]
    }
  },
  "golf-rsm-classic-moving-day-live-sea-island-co-leaders-9-under-cut-2026": {
    "fr": {
      "title": "RSM Classic en direct : Trio de tete a -9 a Sea Island, le cut tombe a -2",
      "subtitle": "Michael Thorbjornsen, Marco Penge et Rasmus Neergaard-Petersen menent la danse tandis que la lutte pour les cartes du PGA Tour fait rage.",
      "excerpt": "Le Moving Day du 3e tour est lance a Sea Island avec trois colegitimes leaders a -9 (131) et un cut fige a -2.",
      "body": [
        "Le Moving Day du samedi bat son plein au Sea Island Golf Club en Georgie, ou le 3e tour du RSM Classic decide a la fois du trophee et des cartes du PGA Tour 2027.",
        "Apres deux premiers tours exigeants, trois golfeurs partagent la tete a 9 sous le par (131) : l'Americain Michael Thorbjornsen, l'Anglais Marco Penge et le Danois Rasmus Neergaard-Petersen. Tous trois ont enchaine des cartes sous les 70 malgre le vent cotier.",
        "Le cut a ete fixe a 2 sous le par (138), qualifiant 65 joueurs pour le week-end sur le parcours Seaside. Les pretendents a la bulle du top 125 FedExCup Fall restent en vie, notamment Austin Smotherman (-4), Mackenzie Hughes (-4) et Joel Dahmen (-3)."
      ]
    },
    "es": {
      "title": "RSM Classic en directo: Tres colideres en -9 en Sea Island y el corte cae en -2",
      "subtitle": "Michael Thorbjornsen, Marco Penge y Rasmus Neergaard-Petersen comandan la clasificacion en Georgia en plena batalla por las tarjetas del PGA Tour.",
      "excerpt": "El Moving Day de la ronda 3 esta en marcha en Sea Island con tres colideres en 9 bajo par (131) y el corte establecido en 2 bajo par.",
      "body": [
        "El Moving Day sabatino ya esta en juego en Sea Island Golf Club en Georgia, donde la tercera ronda del RSM Classic perfila a los aspirantes al titulo y a los salvados del top 125 de la FedExCup Fall.",
        "Tres jugadores comparten la punta con 9 bajo par (131): el estadounidense Michael Thorbjornsen, el ingles Marco Penge y el danes Rasmus Neergaard-Petersen. El trio domino el viento costero con vueltas consistentes en los sesenta.",
        "El corte a 36 hoyos se cerro en 2 bajo par (138), permitiendo el paso a 65 profesionales al recorrido Seaside. Jugadores al limite de la tarjeta como Austin Smotherman (-4), Mackenzie Hughes (-4) y Joel Dahmen (-3) siguen en la pelea."
      ]
    },
    "de": {
      "title": "RSM Classic Moving Day live: Dreierfuehrung bei -9 in Sea Island, Cut faellt bei -2",
      "subtitle": "Michael Thorbjornsen, Marco Penge und Rasmus Neergaard-Petersen geben das Tempo vor, waehrend um die Top-125-Tourkarten gekaempft wird.",
      "excerpt": "Runde 3 am Moving Day laeuft auf dem Seaside Course von Sea Island: Drei Führende bei 9 unter Par (131) und Cut bei -2.",
      "body": [
        "Der Moving Day am Samstag ist im Sea Island Golf Club in Georgia in vollem Gange. Bei der RSM Classic geht es um den Titel und um die PGA-Tour-Karten fuer die Saison 2027.",
        "Nach 36 Loechern teilen sich drei Profis mit 9 unter Par (131) die Spitze: der US-Amerikaner Michael Thorbjornsen, der Englaender Marco Penge und der Daene Rasmus Neergaard-Petersen. Alle drei trotzten den windigen Bedingungen an der Atlantikkueste.",
        "Die Cut-Linie fiel bei 2 unter Par (138), womit 65 Spieler den Sprung ins Wochenende schafften. Wichtig fuer das Saisonfinale: Hoffnungstraeger wie Austin Smotherman (-4), Mackenzie Hughes (-4) und Joel Dahmen (-3) bleiben im Rennen um die Tourkarte."
      ]
    },
    "it": {
      "title": "RSM Classic Moving Day live: Tre leader a -9 a Sea Island, il taglio si fissa a -2",
      "subtitle": "Michael Thorbjornsen, Marco Penge e Rasmus Neergaard-Petersen guidano la classifica mentre infuria la lotta per le carte del PGA Tour.",
      "excerpt": "Il Moving Day del 3° giro e in corso a Sea Island: tre atleti al comando a 9 sotto il par (131) e taglio fissato a -2.",
      "body": [
        "Il Moving Day di sabato e entrato nel vivo al Sea Island Golf Club in Georgia, dove il terzo round dell'RSM Classic decide il trofeo e le ultime carte del PGA Tour per il 2027.",
        "Tre giocatori guidano a braccetto con 9 colpi sotto il par (131): lo statunitense Michael Thorbjornsen, l'inglese Marco Penge e il danese Rasmus Neergaard-Petersen. Tutti e tre hanno saputo gestire il vento costiero del percorso Seaside.",
        "Il taglio a meta gara e caduto a 2 sotto il par (138), ammettendo 65 giocatori al fine settimana. Restano in corsa per confermare la carta tra i primi 125 anche Austin Smotherman (-4), Mackenzie Hughes (-4) e Joel Dahmen (-3)."
      ]
    },
    "pl": {
      "title": "RSM Classic Moving Day na zywo: Trzej liderzy z wynikiem -9 w Sea Island, cut na poziomie -2",
      "subtitle": "Michael Thorbjornsen, Marco Penge i Rasmus Neergaard-Petersen prowadza w Georgii, podczas gdy gracze walcza o karty PGA Tour.",
      "excerpt": "Trzecia runda Moving Day trwa w Sea Island: trzech liderow na poziomie -9 (131), a linia cuta ustalona na -2.",
      "body": [
        "Sobotni Moving Day trwa na polach Sea Island Golf Club w Georgii, gdzie 3. runda The RSM Classic decyduje o losach tytulu i kart PGA Tour na rok 2027.",
        "Po dwoch rundach prowadzenie dziela trzej zawodnicy z wynikiem 9 ponizej par (131): Amerykanin Michael Thorbjornsen, Anglik Marco Penge oraz Dunczyk Rasmus Neergaard-Petersen. Wszyscy znakomicie poradzili sobie z wietrznymi warunkami.",
        "Cut po 36 dolkach wyniosl 2 ponizej par (138), dajac awans 65 graczom. W grze o utrzymanie w czolowej 125 FedExCup Fall pozostaja m.in. Austin Smotherman (-4), Mackenzie Hughes (-4) oraz Joel Dahmen (-3)."
      ]
    },
    "zh": {
      "title": "RSM精英赛移动日战况：三位选手9杆领跑海岛球场，晋级线定在低于标准杆2杆",
      "subtitle": "索比约恩森、彭奇与尼尔高-彼得森并列领先，争夺美巡赛前125位参赛卡生死战进入周末决战。",
      "excerpt": "海岛球场第三轮移动日正在展开，三位领头羊同以低于标准杆9杆（131杆）并驾齐驱，晋级线为低于标准杆2杆。",
      "body": [
        "11月21日周六，美巡秋季赛收官之战RSM精英赛在佐治亚州海岛高尔夫俱乐部迎来关键的第三轮移动日。",
        "经过前两轮海滨与种植园球场的较量，三位选手以总成绩低于标准杆9杆（131杆）共享领先榜首位：美国小将迈克尔·索比约恩森、英格兰选手马尔科·彭奇以及丹麦新秀拉斯穆斯·尼尔高-彼得森。三人在强风中均交出了稳定的6字头杆数。",
        "两轮过后的晋级线定在低于标准杆2杆（138杆），共有65名选手顺利挺进周末的海滨球场决赛轮。奥斯汀·斯莫瑟曼（-4）、麦肯齐·休斯（-4）和乔尔·达门（-3）等处于前125名保卡边缘的选手成功晋级，继续为保留美巡全卡拼搏。"
      ]
    },
    "ja": {
      "title": "RSMクラシック・ムービングデー生中継：シーアイランドで3人が9アンダー首位、カットラインは2アンダー",
      "subtitle": "ソービョルンセン、ペンジ、ニアガード＝ペテルセンが首位を並走。来季シード権を巡る激戦が続く。",
      "excerpt": "シーアイランドのシーサイドコースで第3ラウンド進行中。3名が9アンダー（131）で首位タイ、カットは2アンダー。",
      "body": [
        "ジョージア州シーアイランド・ゴルフクラブで、フェデックスカップ・フォール最終戦「RSMクラシック」のムービングデー（第3ラウンド）が開催されています。",
        "36ホールを終えて通算9アンダー（131）の首位に並んだのは、マイケル・ソービョルンセン（米）、マルコ・ペンジ（英）、ラスムス・ニアガード＝ペテルセン（デンマーク）の3選手。強風下でも着実にアンダーパーを重ねました。",
        "通算2アンダー（138）で予選カットが行われ、65名が決勝ラウンドへ進出。来季のフルシード権（トップ125位）を争うジョエル・ダーメン（-3）やマッケンジー・ヒューズ（-4）も無事に予选を通過しました。"
      ]
    },
    "ko": {
      "title": "RSM 클래식 무빙데이 라이브: 시아일랜드 9언더파 공동 선두 3명, 컷 기준은 2언더파",
      "subtitle": "마이클 소르비욘센, 마르코 펜지, 라스무스 네어가르-페테르센이 선두를 달리는 가운데 투어 카드 확보 전쟁이 치열합니다.",
      "excerpt": "조지아주 시아일랜드에서 3라운드 무빙데이가 진행 중이며 9언더파(131) 공동 선두 3명과 2언더파 컷 통과자가 격돌합니다.",
      "body": [
        "11월 21일 토요일 미국 조지아주 시아일랜드 골프클럽에서 2026 PGA 투어 페덱스컵 폴 최종전인 The RSM 클래식 3라운드 무빙데이가 개막했습니다.",
        "36홀 합계 9언더파 131타를 기록한 미국의 마이클 소르비욘센, 잉글랜드의 마르코 펜지, 덴마크의 라스무스 네어가르-페테르센이 공동 선두로 나섰습니다. 세 선수 모두 해안가 돌풍 속에서도 견고한 플레이를 펼쳤습니다.",
        "컷 탈락 기준선은 2언더파 138타로 확정되어 총 65명이 주말 본선에 진출했습니다. 내년 투어 카드(상위 125위)를 지키기 위해 사투를 벌이는 조엘 다멘(-3)과 매켄지 휴스(-4) 등도 생존에 성공했습니다."
      ]
    },
    "ar": {
      "title": "بطولة آر إس إم كلاسيك مباشرة: صدارة ثلاثية بـ 9 ضربات تحت المعدل والقص يستقر عند -2",
      "subtitle": "مايكل ثوربيورنسن وماركو بينجي وراسموس نيرغارد يتصدرون في سي آيلاند وسط معركة شرسة لحسم بطاقات الجولة الأمريكية.",
      "excerpt": "يوم الحسم في الجولة الثالثة ينطلق في سي آيلاند بتصدر ثلاثي بـ 9 تحت المعدل (131) واجتياز 65 لاعبا لخط القص عند -2.",
      "body": [
        "انطلقت الجولة الثالثة الحاسمة في نادي سي آيلاند للغولف بولاية جورجيا، حيث تختتم بطولة آر إس إم كلاسيك موسم جولة بي جي إيه 2026 وتحدد البطاقات للموسم القادم.",
        "يشترك ثلاثة لاعبين في صدارة الترتيب بعد 36 حفرة بمجموع 9 ضربات تحت المعدل (131): الأمريكي مايكل ثوربيورنسن، والإنجليزي ماركو بينجي، والدنماركي راسموس نيرغارد. ونجح الثلاثي في مواجهة الرياح الساحلية بثبات.",
        "واستقر خط القص عند ضربتين تحت المعدل (138) ليتأهل 65 لاعبا إلى عطلة نهاية الأسبوع. ونجح لاعبون يقاتلون من أجل البقاء ضمن أفضل 125 لاعبا في العبور، من بينهم جويل داهمن (-3) وماكنزي هيوز (-4)."
      ]
    }
  },
  "nfl-tnf-texans-rout-colts-26-3-stroud-afc-south-control-week11-2026": {
    "fr": {
      "title": "Les Texans surclassent les Colts 26-3 au Thursday Night Football : Stroud et la defense regnent sur l'AFC Sud",
      "subtitle": "Houston provoque trois pertes de balle et limite Anthony Richardson a 112 yards a la passe pour s'imposer avec autorite au NRG Stadium.",
      "excerpt": "C.J. Stroud lance deux passes de touchdown et la defense des Texans etouffe les Colts 26-3 pour porter Houston a 7-4 au sommet de sa division.",
      "body": [
        "Les Houston Texans ont marque les esprits jeudi soir en dominant leurs rivaux de division, les Indianapolis Colts, sur le score sans appel de 26-3 au NRG Stadium devant plus de 71 000 spectateurs.",
        "Le quarterback C.J. Stroud a livre une prestation d'une grande precision avec 22 passes completees sur 31 pour 248 yards et deux touchdowns, trouvant Nico Collins puis le rookie Cade Stover. La defense agressive de DeMeco Ryans a completement neutralise Anthony Richardson, auteur de seulement 112 yards et coupable de deux interceptions.",
        "Avec ce succes probant, Houston porte son bilan a 7-4 et prend les commandes de l'AFC Sud. L'attention de la semaine 11 de la NFL se tourne desormais vers les affiches dominicales, avec notamment le deplacement des Chiefs chez les Panthers et le choc entre les 49ers et les Packers a Lambeau Field."
      ]
    },
    "es": {
      "title": "Los Texans aplastan 26-3 a los Colts en el Thursday Night Football: Stroud y la defensa mandan en la AFC Sur",
      "subtitle": "Houston fuerza tres perdidas de balon y frena a Anthony Richardson en 112 yardas para firmar un triunfo estelar en el NRG Stadium.",
      "excerpt": "C.J. Stroud lanza dos pases de touchdown y la defensiva de DeMeco Ryans seca a los Colts 26-3 para dejar a Houston con marca de 7-4.",
      "body": [
        "Los Houston Texans dieron un golpe de autoridad en la AFC Sur este jueves por la noche al vencer de forma contundente 26-3 a los Indianapolis Colts ante 71.842 aficionados en el NRG Stadium.",
        "C.J. Stroud estuvo impecable completando 22 de 31 envios para 248 yardas y dos touchdowns con Nico Collins y Cade Stover. Mientras tanto, la defensa tejana capturo en cuatro ocasiones a Anthony Richardson, limitandolo a 112 yardas aereas y robando tres balones.",
        "Con este triunfo, los Texans mejoran a 7-4 y se consolidan en la cima divisional. La atencion de la semana 11 de la NFL se centra ahora en el domingo, con partidos destacados como la visita de los Chiefs a Carolina y el 49ers frente a Packers en Lambeau Field."
      ]
    },
    "de": {
      "title": "Texans demontieren Colts mit 26:3 im Thursday Night Football: Stroud und Defensive dominieren die AFC South",
      "subtitle": "Houston erzwingt drei Ballverluste und haelt Anthony Richardson bei 112 Passing Yards fuer einen souveraenen Heimsieg im NRG Stadium.",
      "excerpt": "C.J. Stroud wirft zwei Touchdown-Paesse und Houstons Defensive erstickt die Colts mit 26:3, um die Bilanz auf 7-4 auszubauen.",
      "body": [
        "Die Houston Texans haben am Donnerstagabend ein deutliches Ausrufezeichen in der AFC South gesetzt und Divisionsrivale Indianapolis Colts vor 71.842 Fans im NRG Stadium mit 26:3 abgefertigt.",
        "Quarterback C.J. Stroud glanzte mit 22 von 31 angekommenen Paessen fuer 248 Yards und zwei Touchdowns auf Nico Collins und Cade Stover. Die Texans-Abwehr unter Head Coach DeMeco Ryans lieferte ein Meisterstueck ab, sackte Anthony Richardson viermal und fing zwei Interceptions.",
        "Mit einer Bilanz von 7-4 uebernimmt Houston die alleinige Fuehrung in der Division. Der Fokus von NFL-Woche 11 richtet sich nun auf die Sonntagsspiele, darunter der Auftritt der Chiefs bei den Panthers und das Traditionsduell 49ers bei den Packers."
      ]
    },
    "it": {
      "title": "I Texans travolgono i Colts 26-3 nel Thursday Night Football: Stroud e la difesa conquistano la AFC South",
      "subtitle": "Houston forza tre turnover e concede appena 112 yard su passaggio ad Anthony Richardson in un trionfo senza appello all'NRG Stadium.",
      "excerpt": "C.J. Stroud lancia due touchdown e la difesa asfissia Indianapolis per il 26-3 finale che proietta Houston sul record di 7-4 in vetta alla divisione.",
      "body": [
        "Grande prova di forza degli Houston Texans giovedi notte: davanti ai 71.842 spettatori dell'NRG Stadium, i padroni di casa hanno spazzato via gli Indianapolis Colts con un perentorio 26-3.",
        "Il quarterback C.J. Stroud ha diretto l'attacco con precisione chirurgica (22 su 31 per 248 yard e 2 TD), mentre la retroguardia di DeMeco Ryans ha concesso le briciole ad Anthony Richardson, costretto a soli 112 yard di lancio e a 2 intercetti subiti.",
        "Grazie a questo successo, Houston sale a un record di 7-4 e si prende il comando dell'AFC South. Lo sguardo della Week 11 della NFL si sposta ora sulla domenica, con i Chiefs impegnati a Carolina e l'attesissimo scontro tra 49ers e Packers a Lambeau Field."
      ]
    },
    "pl": {
      "title": "Texans rozbijaja Colts 26:3 w Thursday Night Football: Stroud i defensywa przejmuja AFC South",
      "subtitle": "Houston wymusza trzy straty i zatrzymuje Anthony'ego Richardsona na 112 jardach podaniowych w pewnym triumfie na NRG Stadium.",
      "excerpt": "C.J. Stroud rzuca dwa podania na przylozenie, a zelazna obrona Texans rozbija Colts 26:3, dajac Houston bilans 7-4 na czele dywizji.",
      "body": [
        "Houston Texans dali popis formy w czwartkowym meczu otwarcia 11. tygodnia NFL, rozbijajac rywali z dywizji Indianapolis Colts 26:3 przed 71 tysiacami widzow na NRG Stadium.",
        "Rozgrywajacy C.J. Stroud zaprezentowal profesure, kompletujac 22 z 31 podan na 248 jardow i dwa przylozenia (do Nico Collinsa i Cade'a Stovera). Defensywa gospodarzy calkowicie wylaczyla Anthony'ego Richardsona, notujac cztery sacki i dwie przechwycone pilki.",
        "Po tej wygranej Texans z bilansem 7-4 objeli samodzielne prowadzenie w AFC South. Uwaga kibicow przenosi sie na niedzielne starcia, m.in. wyjazd Chiefs do Karoliny oraz klasyk 49ers kontra Packers na Lambeau Field."
      ]
    },
    "zh": {
      "title": "德州人周四夜赛26-3大胜小马：斯特劳德两达阵与铁血防守掌控美南赛区",
      "subtitle": "休斯敦全场迫使对手3次失误，将理查德森传球限制在112码，在NRG体育场奉献统治级胜利。",
      "excerpt": "斯特劳德传出两记达阵，德梅科·莱昂斯调教的防守组全面压制小马，休斯敦德州人26-3取胜战绩升至7胜4负。",
      "body": [
        "休斯敦德州人在周四夜赛中向全联盟展现了统治力，在NRG体育场71,842名球迷的欢呼声中以26-3横扫同区死敌印第安纳波利斯小马。",
        "四分卫C.J.斯特劳德发挥极其稳健，31传22中拿下248码并收获两记达阵，分别连线外接手尼科·柯林斯与新秀近端锋凯德·斯托弗。与此同时，休斯敦坚固的防守组全场完成4次擒杀并送出2记抄截，让小马四分卫安东尼·理查德森全场传球仅得112码。",
        "此役获胜后，德州人战绩提升至7胜4负，独占美联南区榜首。NFL第11周的焦点随即转向周日对局，包括堪萨斯城酋长客战黑豹，以及旧金山49人做客兰博球场挑战绿湾包装工。"
      ]
    },
    "ja": {
      "title": "サーズデーナイトでテキサンズがコルツを26-3で圧倒：ストラウドと堅守で地区首位固め",
      "subtitle": "ヒューストン守備陣が3つのターンオーバーを奪い、リチャードソンのパスを112ヤードに封じ込めてNRGスタジアムで完勝。",
      "excerpt": "C.J.ストラウドの2本のTDパスと鉄壁のディフェンスでコルツを26-3で下し、テキサンズが7勝4敗で地区単独首位へ浮上。",
      "body": [
        "木曜夜のNFL第11週開幕戦、ヒューストン・テキサンズは本拠地NRGスタジアムで同地区のライバルであるインディアナポリス・コルツを26-3で圧倒しました。",
        "QBのC.J.ストラウドは31本中22本のパスを通し、248ヤード、2TDパスをマーク。デミコ・ライアンズHC率いる守備陣がコルツの若き司令塔アンソニー・リチャードソンを4サック、2インターセプトに追い込み、わずか112ヤードのパスに封殺しました。",
        "この勝利でテキサンズは7勝4敗となり、AFC南部地区の首位をガッチリとキープ。第11週の注目は日曜日のゲームに移り、チーフス対パンサーズやランボー・フィールドでの49ers対パッカーズ戦が控えています。"
      ]
    },
    "ko": {
      "title": "텍산스, 목요일 밤 풋볼서 콜츠 26-3 완파: 스트라우드와 철벽 수비로 AFC 남부 독주",
      "subtitle": "휴스턴 수비진이 턴오버 3개를 유도하고 앤서니 리처드슨의 패스를 112야드로 묶으며 NRG 스타디움 완승 달성.",
      "excerpt": "C.J. 스트라우드의 2개 터치다운 패스와 질식 수비를 앞세운 휴스턴 텍산스가 콜츠를 26-3으로 꺾고 7승 4패로 조 선두를 질주했습니다.",
      "body": [
        "휴스턴 텍산스가 11월 19일 목요일 밤 NRG 스타디움에서 열린 NFL 11주차 경기에서 디비전 라이벌 인디애나폴리스 콜츠를 26-3으로 대파했습니다.",
        "쿼터백 C.J. 스트라우드는 31번의 패스 시도 중 22번을 적중시켜 248야드와 터치다운 2개를 기록했습니다. 디메코 라이언스 감독의 강력한 수비진은 앤서니 리처드슨을 상대로 4개의 색과 2개의 인터셉트를 기록하며 콜츠 공격을 완전히 잠재웠습니다.",
        "이로써 텍산스는 7승 4패를 기록하며 AFC 남부지구 단독 1위 자리를 굳혔습니다. NFL 11주차 일정은 일요일 캔자스시티 치프스의 캐롤라이나 원정과 샌프란시스코 49ers 대 그린베이 패커스의 격돌로 이어집니다."
      ]
    },
    "ar": {
      "title": "تكسانز يكتسحون كولتس 26-3 في كرة القدم ليلة الخميس: سترود والدفاع يفرضون السيطرة على الجنوب الأمريكي",
      "subtitle": "دفاع هيوستن يجبر الخصم على 3 أخطاء ويقيد ريتشاردسون عند 112 ياردة فقط في فوز كاسح بملعب إن آر جي.",
      "excerpt": "سي جي سترود يرمي تمريرتي هبوط ودفاع تكسانز يخنق كولتس بنتيجة 26-3 ليرفع الفريق رصيده إلى 7-4 في صدارة مجموعته.",
      "body": [
        "وجه هيوستن تكسانز رسالة تحذيرية شديدة اللهجة لمنافسيه في دوري كرة القدم الأمريكية ليلة الخميس، باكتساحه غريمه إنديانابوليس كولتس 26-3 أمام أكثر من 71 ألف متفرج في ملعب إن آر جي.",
        "تألق صانع الألعاب سي جي سترود بدقة عالية محققا 22 تمريرة ناجحة من أصل 31 لمسافة 248 ياردة وتمريرتي هبوط. في المقابل، قدم دفاع المدرب ديميكو رايانز أداء حديديا، حيث أسقط أنتوني ريتشاردسون 4 مرات وقطع تمريرتين، ليعطل هجوم كولتس تماما.",
        "بهذا الفوز يرفع تكسانز رصيدهم إلى 7-4 في صدارة القسم الجنوبي للاتحاد الأمريكي. وتتحول الأنظار إلى مباريات الأحد الممتازة في الأسبوع 11، وأبرزها مواجهة كانساس سيتي تشيفز ضد كارولاينا ومباراة فورتي ناينرز ضد باكرز في لامبو فيلد."
      ]
    }
  },
  "nba-lakers-edge-kings-sacramento-thriller-jokic-triple-double-2026": {
    "fr": {
      "title": "Vendredi NBA : Les Lakers dominent les Kings 106-104 a Sacramento, Jokic s'offre un triple-double",
      "subtitle": "Austin Reaves rentre les lancers francs decisifs dans les ultimes secondes et Los Angeles resiste aux 29 points de De'Aaron Fox au Golden 1 Center.",
      "excerpt": "Les Lakers s'imposent au finish 106-104 face a Sacramento tandis que Nikola Jokic signe un triple-double a 32 points pour Denver face a Houston.",
      "body": [
        "La soiree de vendredi 20 novembre en NBA a offert un spectacle haletant a travers la Conference Ouest, marquee par le duel intense entre les Lakers et les Kings au Golden 1 Center de Sacramento.",
        "Les Los Angeles Lakers ont survecu a l'ultime assaut des Kings pour l'emporter 106-104. Austin Reaves n'a pas tremble sur la ligne des lancers francs a 4,1 secondes du terme avant que le tir au buzzer de De'Aaron Fox (29 points) ne rebondisse sur le cercle. Anthony Davis (24 points, 14 rebonds) et LeBron James (18 points, 9 passes) ont assure le gain du match.",
        "A Denver, le triple MVP Nikola Jokic a livre un nouveau chef-d'oeuvre avec 32 points, 12 rebonds et 10 passes pour guider les Nuggets vers un succes 133-124 sur les Rockets. Avec la victoire des Cavaliers a Indiana (128-119), la lutte pour les places en playoffs s'annonce plus serree que jamais."
      ]
    },
    "es": {
      "title": "Viernes de la NBA: Los Lakers vencen 106-104 a los Kings en Sacramento, Jokic firma un triple-doble",
      "subtitle": "Austin Reaves anota tiros libres decisivos en los ultimos segundos y Los Angeles resiste los 29 puntos de De'Aaron Fox en el Golden 1 Center.",
      "excerpt": "Los Lakers aguantan el empuje de Sacramento para ganar 106-104, mientras Nikola Jokic firma un triple-doble de 32 puntos con Denver.",
      "body": [
        "La jornada del viernes 20 de noviembre en la NBA regalo un desenlace apasionante en la Conferencia Oeste con el triunfo de los Lakers 106-104 en Sacramento.",
        "Los Angeles Lakers supieron templar los nervios en el Golden 1 Center. Austin Reaves encesto dos tiros libres clave a 4,1 segundos del final para amarrar la victoria tras el triple fallado sobre la bocina por De'Aaron Fox (29 puntos). Anthony Davis (24 puntos, 14 rebotes) y LeBron James (18 puntos, 9 asistencias) fueron pilares decisivos.",
        "En Denver, Nikola Jokic brillo con un triple-doble de 32 puntos, 12 rebotes y 10 asistencias en la victoria de los Nuggets 133-124 sobre Houston Rockets. Junto al triunfo de Cleveland 128-119 en Indiana, el Oeste y el Este confirman una tremenda paridad competitiva."
      ]
    },
    "de": {
      "title": "NBA-Freitag: Lakers bezwingen Kings mit 106:104 im Sacramento-Krimi, Jokic glaenzt mit Triple-Double",
      "subtitle": "Austin Reaves versenkt entscheidende Freiwuerfe in den Schlusssekunden, damit Los Angeles die 29 Punkte von De'Aaron Fox uebersteht.",
      "excerpt": "Die Lakers retten einen 106:104-Sieg in Sacramento ueber die Zeit, waehrend Nikola Jokic mit einem 32-Punkte-Triple-Double Denver zum Sieg fuehrt.",
      "body": [
        "Die NBA-Spiele am Freitagabend, 20. November, boten packende Dramatik in der Western Conference, angefuehrt vom Krimi im Golden 1 Center zwischen den Kings und den Lakers.",
        "Die Los Angeles Lakers behielten beim 106:104 ueber die Sacramento Kings hauchduenn die Oberhand. Austin Reaves traf 4,1 Sekunden vor Schluss zwei eiskalte Freiwuerfe, ehe der letzte Dreierversuch von De'Aaron Fox (29 Punkte) das Ziel verfehlte. Anthony Davis (24 Punkte, 14 Rebounds) und LeBron James (18 Punkte, 9 Assists) gaben den Ausschlag.",
        "In Denver brillierte Nikola Jokic mit 32 Punkten, 12 Rebounds und 10 Assists beim 133:124-Erfolg der Nuggets gegen Houston. Zudem gewannen die Cleveland Cavaliers 128:119 in Indiana."
      ]
    },
    "it": {
      "title": "Venerdi NBA: I Lakers superano i Kings 106-104 a Sacramento, Jokic trascina i Nuggets con una tripla doppia",
      "subtitle": "Austin Reaves segna i liberi decisivi nel finale e Los Angeles resiste ai 29 punti di De'Aaron Fox al Golden 1 Center.",
      "excerpt": "I Lakers vincono 106-104 sul filo di lana a Sacramento, mentre Nikola Jokic mette a referto una tripla doppia da 32 punti contro Houston.",
      "body": [
        "Venerdi 20 novembre ad altissima tensione sui parquet NBA, con una sfida spettacolare della Pacific Division al Golden 1 Center di Sacramento.",
        "I Los Angeles Lakers hanno piegato i Sacramento Kings 106-104 resistendo all'ultimo assalto guidato da De'Aaron Fox (29 punti). Due tiri liberi glaciali di Austin Reaves a 4 secondi dalla sirena hanno blindato il successo, supportati dalla solida prova di Anthony Davis (24 punti, 14 rimbalzi) e LeBron James (18 punti).",
        "A Denver, straordinaria prova per Nikola Jokic con 32 punti, 12 rimbalzi e 10 assist nel successo dei Nuggets per 133-124 sugli Houston Rockets. Da segnalare anche il colpo esterno dei Cleveland Cavaliers a Indianapolis (128-119)."
      ]
    },
    "pl": {
      "title": "Piatek w NBA: Lakers pokonuja Kings 106:104 w Sacramento, Jokic notuje triple-double",
      "subtitle": "Austin Reaves trafia kluczowe rzuty wolne w ostatnich sekundach, a Los Angeles odpiera 29-punktowy zryw De'Aarona Foxa.",
      "excerpt": "Lakers wygrywaja 106:104 z Kings w Sacramento, a Nikola Jokic prowadzi Nuggets do triumfu nad Rockets zdobywajac triple-double z 32 punktami.",
      "body": [
        "Piatkowa noc na parkietach NBA przyniosla ogromne emocje, a glownym wydarzeniem bylo zaciety derbowy pojedynek Kings z Lakers w Sacramento.",
        "Los Angeles Lakers wygrali 106:104 po nerwowej koncowce. Austin Reaves zachowal zimna krew na linii rzutow wolnych na 4 sekundy przed koncem, a rzut za trzy De'Aarona Foxa (29 punktow) odbil sie od obreczy. Anthony Davis zanotowal 24 punkty i 14 zbiorek, a LeBron James dolozyl 18 punktow i 9 asyst.",
        "W Denver Nikola Jokic zaliczyl kolejne imponujace triple-double (32 punkty, 12 zbiorek, 10 asyst), prowadzac Nuggets do wygranej 133:124 nad Houston Rockets. W Indianapolis gora byli Cleveland Cavaliers (128:119)."
      ]
    },
    "zh": {
      "title": "NBA周五战报：湖人客场106-104险胜国王，约基奇32分三双率掘金击退火箭",
      "subtitle": "里夫斯最后时刻两罚全中锁定胜局，洛杉矶湖人在黄金一号中心顶住福克斯29分的猛烈反扑。",
      "excerpt": "湖人末节惊险以106-104击败国王拿下加州内战，约基奇砍下32分12板10助率掘金主场力克火箭。",
      "body": [
        "11月20日周五晚间的NBA常规赛精彩纷呈，西部各路豪强展开激烈角逐，黄金一号中心的太平洋区焦点大战战至最后一秒。",
        "洛杉矶湖人顶住萨克拉门托国王在第四节的顽强反击，最终以106-104险胜。奥斯汀·里夫斯在比赛仅剩4.1秒时稳稳命中两次罚球，随后福克斯（全场29分）的绝杀压哨三分磕框而出。安东尼·戴维斯贡献24分14个篮板，勒布朗·詹姆斯入账18分9次助攻，联手守护胜局。",
        "在丹佛高原，三届MVP得主尼古拉·约基奇再度贡献统治级全能表现，全场拿下32分、12个篮板和10次助攻的三双数据，带领掘金主场133-124击败年轻的休斯敦火箭。克利夫兰骑士则在客场128-119力克步行者。"
      ]
    },
    "ja": {
      "title": "金曜NBA：レイカーズがサクラメントの熱戦を106-104で逃げ切る、ヨキッチがトリプルダブル",
      "subtitle": "オースティン・リーブスが終了直前に値千金のフリースローを沈め、フォックスの29得点の猛反撃を退ける。",
      "excerpt": "レイカーズが接戦の末にキングスを106-104で下す。デンバーではヨキッチが32得点トリプルダブルをマーク。",
      "body": [
        "11月20日金曜日のNBAは西地区の好カードが目白押しとなり、ゴールデン1センターでのキングス対レイカーズ戦は劇的な幕切れを迎えました。",
        "ロサンゼルス・レイカーズが第4クォーターのサクラメント・キングスの猛追をしのぎ、106-104で逃げ切りました。残り4.1秒でオースティン・リーブスが2本のフリースローを沈め、フォックス（29得点）のブザービーター3Pが外れて決着。アンソニー・デイビスが24得点14リバウンド、レブロン・ジェームズが18得点をマークしました。",
        "デンバーではニコラ・ヨキッチが32得点、12リバウンド、10アシストのトリプルダブルを達成し、ナゲッツがロケッツを133-124で下しました。"
      ]
    },
    "ko": {
      "title": "NBA 금요일: 레이커스, 새크라멘토에 106-104 신승... 요키치 32점 트리플더블로 너기츠 승리 견인",
      "subtitle": "오스틴 리브스가 종료 직전 위닝 자유투를 침착하게 성공시키며 디애런 팍스의 29점 맹공을 막아냈습니다.",
      "excerpt": "레이커스가 4쿼터 접전 끝에 새크라멘토를 106-104로 제압했고, 니콜라 요키치는 32점 트리플더블로 휴스턴전 승리를 이끌었습니다.",
      "body": [
        "11월 20일 금요일 밤 서부 컨퍼런스 라이벌전이 열린 새크라멘토 골든 1 센터에서 레이커스와 킹스의 숨 막히는 명승부가 펼쳐졌습니다.",
        "LA 레이커스는 4쿼터 막판 새크라멘토의 거센 추격을 뿌리치고 106-104로 승리를 거머쥐었습니다. 오스틴 리브스가 경기 종료 4.1초를 남기고 침착하게 자유투 2개를 모두 넣었고, 디애런 팍스(29점)의 버저비터 3점슛이 림을 빗나갔습니다. 앤서니 데이비스가 24점 14리바운드, 르브론 제임스가 18점을 보탰습니다.",
        "덴버에서는 니콜라 요키치가 32점 12리바운드 10어시스트로 개인 통산 또 하나의 트리플더블을 작성하며 너기츠를 133-124 승리로 이끌었습니다. 클리블랜드도 인디애나 원정에서 128-119로 승리했습니다."
      ]
    },
    "ar": {
      "title": "دوري السلة الأمريكي الجمعة: ليكرز يخطف فوزا مثيرا 106-104 أمام كينغز، ويوكيتش يسجل ثلاثية مزدوجة",
      "subtitle": "أوستن ريفز يحسم الفوز برميات حرة في الثواني الأخيرة ولوس أنجلوس يصمد أمام 29 نقطة من دي آرون فوكس.",
      "excerpt": "ليكرز يتفوق 106-104 على سكرامنتو في لقاء حبس الأنفاس، ونيكولا يوكيتش يقود دنفر للفوز على هيوستن بتسجيل 32 نقطة وتريبل دبل.",
      "body": [
        "شهدت صالة غولدن 1 سنتر إثارة لا توصف مساء الجمعة 20 نوفمبر ضمن دوري كرة السلة الأمريكي، في مواجهة مثيرة بين ليكرز ومضيفه كينغز.",
        "صمد لوس أنجلوس ليكرز أمام العودة القوية لسكرامنتو ليفوز بنتيجة 106-104. وسجل أوستن ريفز رميتين حرتين حاسمتين قبل 4.1 ثانية من النهاية، قبل أن تفشل رمية دي آرون فوكس (29 نقطة) الثلاثية مع صافرة النهاية. وتألق أنتوني ديفيس بـ 24 نقطة و14 متابعة مع 18 نقطة من ليبرون جيمس.",
        "وفي دنفر، قدم النجم نيكولا يوكيتش لوحة فنية بتسجيله 32 نقطة و12 متابعة و10 تمريرات حاسمة، ليقود ناغتس لتجاوز هيوستن روكتس 133-124. كما تغلب كليفلاند على إنديانا 128-119."
      ]
    }
  }
}

# Verification before injection
for slug, locs in translations_data.items():
    for loc, data in locs.items():
        if '\u2014' in data['title'] or '\u2014' in data['subtitle'] or '\u2014' in data['excerpt']:
            raise ValueError(f"Em-dash in {slug} {loc}")
        if '--' in data['title'] or '--' in data['subtitle'] or '--' in data['excerpt']:
            raise ValueError(f"Double-hyphen in {slug} {loc}")
        for p in data['body']:
            if '\u2014' in p:
                raise ValueError(f"Em-dash in body {slug} {loc}")
            if '--' in p:
                raise ValueError(f"Double-hyphen in body {slug} {loc}")

print("Pre-check passed: Zero em-dashes or double-hyphens in translation payload.")

# Read stories.ts
txt = open(STORIES_TS, "r", encoding="utf-8").read()

new_entries_ts = []
for slug, locales in translations_data.items():
    if f'"{slug}":' in txt:
        print(f"Slug {slug} already present in stories.ts, skipping insertion.")
        continue
    entry_code = f'  "{slug}": ' + json.dumps(locales, ensure_ascii=False, indent=4) + ",\n"
    new_entries_ts.append(entry_code)

if new_entries_ts:
    last_brace_idx = txt.rfind("};\n")
    if last_brace_idx == -1:
        last_brace_idx = txt.rfind("};")
    
    updated_txt = txt[:last_brace_idx] + "".join(new_entries_ts) + "};\n"
    open(STORIES_TS, "w", encoding="utf-8").write(updated_txt)
    print(f"Added {len(new_entries_ts)} story translations to stories.ts.")
else:
    print("No new translations needed.")

