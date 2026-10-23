# -*- coding: utf-8 -*-
import json
import re

OCT23_STORIES = {
    "nfl-week7-bears-beat-patriots-30-24": {
        "fr": {
            "title": "Les Bears resistent aux Patriots 30-24 : Santos scelle la victoire",
            "subtitle": "Caleb Williams lance pour 308 yards et deux touchdowns au Soldier Field. Chicago passe a 5-2.",
            "excerpt": "Chicago remporte le match du jeudi soir 30-24 face a la Nouvelle-Angleterre. Cairo Santos reussit un coup de pied decisif de 58 yards.",
            "body": [
                "Les Bears de Chicago ont repousse une furieuse remontee des Patriots de la Nouvelle-Angleterre au quatrieme quart pour s'imposer 30-24 lors du Thursday Night Football au Soldier Field. Le quarterback Caleb Williams a signe l'une de ses meilleures prestations de la saison, completant 22 passes sur 33 pour 308 yards, deux touchdowns et aucune perte de balle. Le receveur debutant Luther Burden III a brille en premiere mi-temps avec 130 yards et un touchdown, tandis que D'Andre Swift a ajoute 78 yards au sol et un touchdown.",
                "La Nouvelle-Angleterre a lutte jusqu'au bout grace a Drake Maye, qui a cumule 321 yards a la passe et deux touchdowns. Mais a 1:34 du terme, le botteur veteran Cairo Santos a reussi un coup de pied monumental de 58 yards, egalant le record de la franchise pour assurer le succes. Cette victoire permet a Chicago d'afficher un bilan de 5-2, tandis que les Patriots glissent a 4-3. Les 49ers restent la seule equipe invaincue a 6-0."
            ]
        },
        "es": {
            "title": "Los Bears aguantan y vencen 30-24 a los Patriots: Santos sella el triunfo",
            "subtitle": "Caleb Williams lanza para 308 yardas y dos anotaciones en Soldier Field. Chicago mejora a 5-2.",
            "excerpt": "Chicago se impuso 30-24 a Nueva Inglaterra en el Thursday Night Football. Cairo Santos anoto un gol de campo clave de 58 yardas.",
            "body": [
                "Los Chicago Bears resistieron una gran reaccion de los New England Patriots en el ultimo cuarto para ganar 30-24 en el Thursday Night Football disputado en Soldier Field. Caleb Williams completo 22 de 33 pases para 308 yardas, dos touchdowns y sin entregas de balon, logrando un rating de 116.7. El novato Luther Burden III destaco en la primera mitad con 130 yardas en cuatro recepciones y una anotacion, mientras que D'Andre Swift sumo 78 yardas terrestres y un touchdown.",
                "Drake Maye comando el regreso de los Patriots con 321 yardas por aire y dos pases de touchdown, conectando con Rhamondre Stevenson en una jugada de 48 yardas. Sin embargo, con 1:34 por jugar, el pateador Cairo Santos acerto un gol de campo de 58 yardas que igualo el record de la franquicia y liquido el partido. Los Bears mejoran a 5-2, mientras que los Patriots quedan con marca de 4-3."
            ]
        },
        "de": {
            "title": "Bears bezwingen Patriots mit 30-24: Santos entscheidet TNF mit 58-Yard-FG",
            "subtitle": "Caleb Williams Glaenzt mit 308 Yards und zwei Touchdowns im Soldier Field. Chicago klettert auf 5-2.",
            "excerpt": "Chicago sichert sich im Thursday Night Football einen 30-24-Erfolg ueber New England. Cairo Santos trifft aus 58 Yards zur Entscheidung.",
            "body": [
                "Die Chicago Bears haben am Donnerstagabend im Soldier Field einen packenden 30-24-Sieg gegen die New England Patriots gefeiert. Quarterback Caleb Williams zeigte eine reife Vorstellung, brachte 22 von 33 Paessen fuer 308 Yards und zwei Touchdowns an den Mann und leistete sich keinen Ballverlust. Rookie Luther Burden III dominierte die erste Halbzeit mit 130 Receiving-Yards und einem Score, waehrend D'Andre Swift 78 Rushing-Yards und einen Touchdown beisteuerte.",
                "New England kaempfte sich angefuehrt von Drake Maye (321 Pass-Yards, zwei Touchdowns) im Schlussviertel noch einmal heran. 1:34 Minuten vor dem Ende verwandelte Kicker Cairo Santos jedoch ein Field Goal aus 58 Yards, stellte damit den Franchise-Rekord ein und machte den Sieg perfekt. Die Bears verbessern sich auf 5-2, waehrend New England auf 4-3 zurueckfaellt. Die 49ers bleiben mit 6-0 ungeschlagen."
            ]
        },
        "it": {
            "title": "I Bears resistono e piegano i Patriots 30-24: Santos decisivo da 58 yard",
            "subtitle": "Caleb Williams lancia per 308 yard e due touchdown al Soldier Field. Chicago sale a 5-2.",
            "excerpt": "Chicago supera 30-24 New England nel Thursday Night Football. Cairo Santos chiude i conti con un field goal da 58 yard a 1:34 dalla sirena.",
            "body": [
                "I Chicago Bears hanno resistito alla rimonta nel quarto periodo dei New England Patriots conquistando una vittoria per 30-24 nel Thursday Night Football al Soldier Field. Il quarterback Caleb Williams ha brillato completando 22 passaggi su 33 per 308 yard, due mete e nessun turnover per un rating di 116.7. Il rookie Luther Burden III e esploso nel primo tempo con 130 yard ricevute e una segnatura, mentre D'Andre Swift ha messo a referto 78 yard su corsa e un touchdown.",
                "New England ha lottato guidata da Drake Maye (321 yard su passaggio e due TD), ma a 1:34 dalla fine il kicker Cairo Santos ha centrato i pali con un field goal da 58 yard che ha eguagliato il record di franchigia e chiuso il match. Chicago sale sul 5-2 mentre i Patriots scivolano a 4-3. I 49ers rimangono l'unica squadra a quota 6-0."
            ]
        },
        "pl": {
            "title": "Bears wytrzymali napor Patriots i wygrali 30-24: Santos trafil z 58 jardow",
            "subtitle": "Caleb Williams rzucil 308 jardow i dwa przylozenia na Soldier Field. Chicago poprawia bilans na 5-2.",
            "excerpt": "Chicago pokonalo Nowa Anglie 30-24 w meczu Thursday Night Football. Cairo Santos przesadzil o losach spotkania kopnieciem z 58 jardow.",
            "body": [
                "Chicago Bears odparli wsciekly poscig New England Patriots w czwartej kwarcie i wygrali 30-24 w meczu Thursday Night Football na Soldier Field. Rozgrywajacy Caleb Williams rozegral znakomite spotkanie, notujac 22 celne podania na 33 proby, 308 jardow, dwa przylozenia i zero strat. Debiuant Luther Burden III zachwycil w pierwszej polowie, zbierajac 130 jardow i zdobywajac punkty, a biegacz D'Andre Swift dolozyl 78 jardow i jedno przylozenie.",
                "Patriots walczyli do konca dzieki Drake'owi Maye (321 jardow, dwa przylozenia), zblizajac sie na trzy punkty. Na poltorej minuty przed koncem kopacz Cairo Santos popisal sie jednak trafieniem z 58 jardow, wyrownujac rekord klubu i pieczetujac triumf gospodarzy. Bears maja teraz bilans 5-2, podczas gdy Patriots spadli na 4-3. 49ers z bilansem 6-0 pozostaja jedyna niepokonana ekipa w lidze."
            ]
        },
        "zh": {
            "title": "熊队30-24力克爱国者：桑托斯58码任意球锁定周四夜赛胜利",
            "subtitle": "凯莱布·威廉姆斯在军人球场传球狂砍308码送出2达阵。芝加哥战绩提升至5胜2负。",
            "excerpt": "芝加哥熊队在周四夜赛中30-24险胜新英格兰爱国者。桑托斯在比赛最后阶段命中58码超远任意球一锤定音。",
            "body": [
                "芝加哥熊队在周四晚间的军人球场顶住了新英格兰爱国者在第四节发起的绝地反扑，以30-24击败对手。四分卫凯莱布·威廉姆斯打出了本赛季代表作之一，33投22中轰下308码，送出2次达阵且没有失误，传球评分高达116.7分。新秀外接手路德·伯登三世在上半场便狂揽130码接球并取得达阵，跑卫斯威夫特也贡献了78码冲球与1次达阵。",
                "爱国者由新秀四分卫德雷克·梅耶带领发起反攻，全场传出321码和2次达阵，将分差迫近至3分。但在比赛仅剩1分34秒时，老将踢球手开罗·桑托斯顶住压力命中平队史纪录的58码超远任意球锁定胜局。此役过后熊队战绩来到5胜2负，爱国者战绩跌至4胜3负。49人以6胜0负继续领跑全联盟。"
            ]
        },
        "ja": {
            "title": "ベアーズが30-24でペイトリオッツに競り勝つ：サントスが58ydのFGで勝負を決める",
            "subtitle": "ケイレブ・ウィリアムズがソルジャー・フィールドで308ヤード・2TD。シカゴは5勝2敗に。",
            "excerpt": "シカゴが木曜夜の熱戦を30-24で制す。ウィリアムズの好投とサントスの球団タイとなる58ydフィールドゴールが決勝点に。",
            "body": [
                "シカゴ・ベアーズはソルジャー・フィールドで行われたサーズデーナイトフットボールで、ニューイングランド・ペイトリオッツの第4クォーターの猛追を振り切り、30-24で勝利を収めました。クォーターバックのケイレブ・ウィリアムズは33投22中、308パスヤード、2タッチダウン、無ターンオーバーの快投を披露。ルーキーWRルーサー・バーデン3世が前半だけで130ヤード・1TDを稼ぎ、RBディエンドレ・スウィフトも78ランヤードと1TDで貢献しました。",
                "ペイトリオッツもQBドレイク・メイエが321ヤード、2TDの活躍で3点差まで迫りましたが、残り1分34秒でベアーズのKカイロ・サントスが球団記録タイとなる58ヤードのフィールドゴールを成功。シカゴは5勝2敗となり、敗れたペイトリオッツは4勝3敗に後退しました。49ersが6勝0敗で依然リーグ唯一の無敗を守っています。"
            ]
        },
        "ko": {
            "title": "베어스, 패트리어츠에 30-24 신승: 산토스의 58야드 필드골로 승리 확정",
            "subtitle": "케イレ브 윌리엄스 308야드 2TD 맹활약. 시카고 베어스 5승 2패 기록.",
            "excerpt": "시카고가 솔저 필드에서 열린 TNF에서 뉴잉글랜드를 30-24로 꺾었습니다. 윌리엄스의 호투와 산토스의 58야드 쐐기 필드골이 빛났습니다.",
            "body": [
                "시카고 베어스가 22일 솔저 필드에서 펼쳐진 TNF 경기에서 뉴잉글랜드 패트리어츠의 거센 4쿼터 추격을 뿌리치고 30-24로 값진 승리를 거뒀습니다. 쿼터백 케イレ브 윌리엄스는 33번의 패스 시도 중 22번을 적중시키며 308야드, 2터치다운, 턴오버 0개를 기록해 116.7의 패서 레이팅을 작성했습니다. 루키 와이드리시버 루서 버든 3세가 전반에만 130야드 리시빙과 1TD를 기록했고, 러닝백 디앤드레 스위프트가 78야드 러싱과 1TD를 보탰습니다.",
                "뉴잉글랜드는 쿼터백 드레이크 메이예가 321야드 패스와 2TD로 분전하며 3점 차까지 따라붙었습니다. 하지만 경기 종료 1분 34초를 남기고 베어스의 카이로 산토스가 구단 타이 기록인 58야드 롱 필드골을 갈라 승부에 마침표를 찍었습니다. 베어스는 5승 2패가 되었고 패트리어츠는 4승 3패로 내려앉았습니다. 49ers가 6승 무패로 단독 무패를 질주하고 있습니다."
            ]
        },
        "ar": {
            "title": "البيرز يتفوقون على الباتريوتس 30-24: سانتوس يحسم موقعة TNF بهدف ميداني من 58 ياردة",
            "subtitle": "كالب ويليامز يتالق بـ308 ياردات تمرير وهبوطين في سولجر فيلد. شيكاغو ترفع رصيدها الى 5-2.",
            "excerpt": "حسمت شيكاغو فوزا مثيرا 30-24 على نيو انغلاند في ليلة الخميس الكروية بفضل تالق ويليامز وهدف كايرو سانتوس الصاروخي.",
            "body": [
                "صمد شيكاغو بيرز امام صحوة نيو انغلاند باتريوتس في الربع الرابع ليحقق فوزا مثيرا 30-24 في افتتاح الاسبوع السابع على ارضية ملعب سولجر فيلد. قدم كالب ويليامز مباراة استثنائية اكمل خلالها 22 تمريرة من اصل 33 محققا 308 ياردات وهبوطين دون اي خطأ. ولفت الصاعد لوثر بيردن الثالث الانظار بجمعه 130 ياردة وهبوطا في الشوط الاول، في حين اضاف دي اندريه سويفت 78 ياردة ارضية مع هبوط اخر.",
                "وعاد الباتريوتس الى اجواء اللقاء بقيادة دريك ماي الذي سجل 321 ياردة وتمريرتي هبوط مقلصا الفارق الى ثلاث نقاط. غير ان المسدد كايرو سانتوس اطلق ركلة ميدانية حاسمة من مسافة 58 ياردة قبل دقيقة و34 ثانية من النهاية ليعادل الرقم القياسي للنادي ويضمن الانتصار. ارتفع رصيد البيرز الى 5-2 وتراجع الباتريوتس الى 4-3، فيما يظل الـ49ers الفريق الوحيد بسجل ناصع بـ6 انتصارات."
            ]
        }
    },
    "atp-friday-almaty-tsitsipas-downs-duckworth-reaches-semis-2026": {
        "fr": {
            "title": "Tsitsipas en demi-finales a Almaty : Bublik vient a bout de Khachanov",
            "subtitle": "Stefanos Tsitsipas ecarte James Duckworth 6-3, 6-4. Alexander Bublik s'impose au bout de deux tie-breaks.",
            "excerpt": "Le Grec Tsitsipas s'est qualifie pour les demi-finales a Almaty en battant Duckworth. Il retrouvera Bublik, tombeur de Khachanov en trois sets.",
            "body": [
                "Stefanos Tsitsipas a poursuivi sa route au tournoi d'Almaty ce vendredi 23 octobre en dominant l'Australien James Duckworth 6-3, 6-4 en quarts de finale. Tete de serie numero 7, le Grec a fait preuve d'une solidite irreprochable au service avec huit aces et seulement neuf points perdus sur son premier engagement en une heure et 22 minutes de jeu. Un break dans chaque manche lui a suffi pour composter son billet sans concéder la moindre balle de break.",
                "Le public kazakh a ensuite vecu un combat dantesque lors du succes d'Alexander Bublik contre Karen Khachanov. Mené d'un set, le joueur local a renverve la rencontre 4-6, 7-6(5), 7-6(5) en deux heures et 38 minutes en claquant 19 aces pour rejoindre Tsitsipas dans une demi-finale tres attendue. Dans l'autre partie du tableau, Daniil Medvedev a battu Terence Atmane 6-4, 6-4 tandis que Nikoloz Basilashvili a elimine Adrian Mannarino 6-3, 6-1."
            ]
        },
        "es": {
            "title": "Tsitsipas avanza a semifinales en Almaty: Bublik vence a Khachanov",
            "subtitle": "Stefanos Tsitsipas supero a James Duckworth 6-3, 6-4. Alexander Bublik remonto con dos desempates.",
            "excerpt": "Tsitsipas sello su pase a semifinales en Almaty con una solida victoria sobre Duckworth. Bublik derroto a Khachanov en un partidazo.",
            "body": [
                "Stefanos Tsitsipas continuo su paso firme en el Almaty Open al derrotar este viernes al australiano James Duckworth por 6-3 y 6-4 en cuartos de final. El griego, septimo cabeza de serie, mostro una notable solvencia al servicio con ocho saques directos y cediendo apenas nueve puntos con su primer saque en una hora y 22 minutos. Tsitsipas quebro en momentos clave de cada set sin afrontar puntos de quiebre en contra.",
                "En el duelo mas vibrante de la jornada, el kazajo Alexander Bublik remonto ante Karen Khachanov para imponerse 4-6, 7-6(5) y 7-6(5) tras dos horas y 38 minutos de intensa batalla. Bublik disparo 19 aces para citarse con Tsitsipas en semifinales. Por el otro lado del cuadro, el maximo favorito Daniil Medvedev vencio 6-4, 6-4 a Terence Atmane, mientras que Nikoloz Basilashvili batio 6-3, 6-1 a Adrian Mannarino."
            ]
        },
        "de": {
            "title": "Tsitsipas zieht ins Halbfinale von Almaty ein: Bublik schlaegt Khachanov",
            "subtitle": "Stefanos Tsitsipas bezwingt James Duckworth 6-3, 6-4. Alexander Bublik dreht Partie in zwei Tiebreaks.",
            "excerpt": "Tsitsipas erreicht nach einem 6-3, 6-4 ueber Duckworth die Runde der letzten Vier. Dort trifft er auf Bublik, der Khachanov in drei Saetzen niederrang.",
            "body": [
                "Stefanos Tsitsipas hat am Freitag mit einer konzentrierten Vorstellung das Halbfinale beim ATP-Turnier in Almaty erreicht. Der an Position sieben gesetzte Grieche setzte sich in einer Stunde und 22 Minuten mit 6-3, 6-4 gegen den Australier James Duckworth durch. Tsitsipas schlug acht Asse, verlor bei eigenem ersten Aufschlag lediglich neun Punkte und ließ ueber das gesamte Match keine einzige Breakchance gegen sich zu.",
                "Fuer Begeisterung beim heimischen Publikum sorgte anschließend Alexander Bublik. Der Kasache drehte einen Satzrueckstand gegen Karen Khachanov und siegte nach zwei Stunden und 38 Minuten mit 4-6, 7-6(5), 7-6(5). Bublik servierte 19 Asse und trifft nun im Halbfinale auf Tsitsipas. Zuvor hatten Topfavorit Daniil Medvedev (6-4, 6-4 gegen Terence Atmane) und Nikoloz Basilashvili (6-3, 6-1 gegen Adrian Mannarino) das erste Halbfinale komplettiert."
            ]
        },
        "it": {
            "title": "Tsitsipas vola in semifinale ad Almaty: Bublik piega Khachanov al tie-break",
            "subtitle": "Stefanos Tsitsipas batte James Duckworth 6-3, 6-4. Alexander Bublik vince in rimonta dopo due ore e mezza.",
            "excerpt": "Tsitsipas approda al penultimo atto ad Almaty superando Duckworth in due set. Bublik rimonta Khachanov e lancia la sfida al greco.",
            "body": [
                "Stefanos Tsitsipas non sbaglia un colpo all'Almaty Open e conquista la semifinale superando venerdi l'australiano James Duckworth con il punteggio di 6-3, 6-4. Il greco, testa di serie numero 7, e stato impeccabile nei turni di battuta, mettendo a segno otto ace e concedendo appena nove punti sulla prima palla in un'ora e 22 minuti. Due break chirurgici hanno chiuso i conti senza concedere occasioni all'avversario.",
                "Il beniamino di casa Alexander Bublik ha infiammato l'Almaty Arena superando in rimonta Karen Khachanov per 4-6, 7-6(5), 7-6(5) grazie a 19 ace e grande freddezza nei momenti cruciali. Sara lui a sfidare Tsitsipas sabato. Nell'altra semifinale si affronteranno il numero uno del seeding Daniil Medvedev (6-4, 6-4 a Terence Atmane) e Nikoloz Basilashvili (6-3, 6-1 ad Adrian Mannarino)."
            ]
        },
        "pl": {
            "title": "Tsitsipas w polfinale w Almatach: Bublik po dramatycznym boju pokonal Chaczanowa",
            "subtitle": "Stefanos Tsitsipas wygral z Jamesem Duckworthem 6-3, 6-4. Alexander Bublik odrobil straty w dwoch tie-breakach.",
            "excerpt": "Tsitsipas awansowal do najlepszej czworki w Almatach po pewnym zwyciestwie nad Duckworthem. W polfinale zagra z Bublikiem.",
            "body": [
                "Stefanos Tsitsipas pewnie zameldowal sie w polfinale turnieju ATP 250 w Almatach, pokonujac w piatek Australijczyka Jamesa Duckwortha 6-3, 6-4. Rozstawiony z numerem siodmym Grek znakomicie serwowal, posylajac osiem asow i tracac zaledwie dziewiec punktow po pierwszym podaniu w ciagu godziny i 22 minut. Tsitsipas nie musial bronic ani jednego break pointa.",
                "Miejscowi kibice przezyli niesamowite emocje podczas starcia Alexandra Bublika z Karenem Chaczanowem. Kazach przegral pierwszego seta, ale odwrocil losy meczu, wygrywajac 4-6, 7-6(5), 7-6(5) po dwoch godzinach i 38 minutach walki i posylajac 19 asow serwisowych. W drugim polfinale Daniil Miedwiediew (6-4, 6-4 z Terence'em Atmane) zmierzy sie z Nikolozem Basilaszwilim (6-3, 6-1 z Adrianem Mannarino)."
            ]
        },
        "zh": {
            "title": "西西帕斯昂首挺进阿拉木图半决赛：布勃利克险胜哈恰诺夫",
            "subtitle": "西西帕斯直落两盘6-3、6-4轻取达克沃斯。布勃利克抢七决胜逆转晋级。",
            "excerpt": "西西帕斯在阿拉木图八强战中完胜达克沃斯。布勃利克三盘逆转哈恰诺夫，与希腊名将会师周六半决赛。",
            "body": [
                "赛会7号种子西西帕斯在周五的阿拉木图公开赛八强战中表现沉稳，耗时1小时22分钟以6-3、6-4完胜澳大利亚选手达克沃斯，强势晋级半决赛。希腊名将全场轰出8记发球ACE，一发仅丢掉9分，并在没有送出任何破发点的情况下，于上下半盘各完成一次关键破发锁定胜局。",
                "主场作战的3号种子布勃利克在另一场焦点战中上演惊天逆转，他在先丢一盘的逆境下通过两度抢七，以4-6、7-6(5)、7-6(5)力克5号种子哈恰诺夫，整场比赛狂轰19记ACE球。半决赛他将迎战西西帕斯。下半区中，头号种子梅德韦杰夫以6-4、6-4淘汰阿特马纳，将与6-3、6-1完胜马纳里诺的巴西拉什维利争夺决赛席位。"
            ]
        },
        "ja": {
            "title": "チチパスがアルマティ準決勝進出：ブブリクがハチャノフとの死闘を制す",
            "subtitle": "チチパスがダックワースを6-3, 6-4で退ける。ブブリクはタイブレーク連取で逆転勝ち。",
            "excerpt": "チチパスが安定したプレーでアルマティ4強入り。ブブリクがハチャノフを下し、注目の準決勝カードが決定しました。",
            "body": [
                "ステファノス・チチパスが23日金曜日、アルマティ・オープンの準々決勝でジェームズ・ダックワースを6-3, 6-4で下し、快調にベスト4入りを果たしました。第7シードのチチパスは8本のサービスエースを決め、ファーストサーブ時の失点をわずか9点に抑える完璧な配球を披露。ブレークポイントを与えることなく1時間22分で快勝しました。",
                "地元カザフスタンの第3シード、アレクサンダー・ブブリクは第5シードのカレン・ハチャノフを相手に4-6, 7-6(5), 7-6(5)の大逆転劇を演じました。2時間38分の激闘で19本のエースを放ったブブリクが準決勝でチチパスと対戦します。もう一方の山では第1シードのダニール・メドベージェフ（6-4, 6-4 アトマネ）とニコロズ・バシラシビリ（6-3, 6-1 マナリノ）が勝ち上がりました。"
            ]
        },
        "ko": {
            "title": "치치파스, 완벽한 경기력으로 알마티 4강 안착: 부블리크 대역전승",
            "subtitle": "스테파노스 치치파스, 제임스 더크워스 6-3, 6-4 격파. 부블리크는 하차노프와 혈투 끝 승리.",
            "excerpt": "치치파스가 8강에서 무실세트 승리를 거두며 알마티 4강에 진출했습니다. 부블리크가 3세트 접전 끝에 하차노프를 꺾고 합류했습니다.",
            "body": [
                "스테파노스 치치파스가 23일 금요일 알마티 오픈 8강전에서 호주의 제임스 더크워스를 6-3, 6-4로 제압하고 준결승에 올랐습니다. 7번 시드 치치파스는 1시간 22분 동안 8개의 서브 에이스를 터뜨리며 첫 번째 서브 득점 확률을 압도적으로 유지했습니다. 단 한 차례의 브레이크 위기도 허용하지 않는 완벽한 서브 게임이 돋보였습니다.",
                "카자흐스탄의 알렉산더 부블리크는 카렌 하차노프를 상대로 4-6, 7-6(5), 7-6(5) 대역전승을 거두며 홈 관중을 열광시켰습니다. 19개의 에이스를 꽂아 넣은 부블리크는 토요일 치치파스와 결승 진출을 다툽니다. 다른 대진에서는 톱시드 다닐 메드베데프(6-4, 6-4 아트만)와 니콜로즈 바실라시빌리(6-3, 6-1 마나리노)가 4강에서 맞붙습니다."
            ]
        },
        "ar": {
            "title": "تسيتسيباس يبلغ نصف نهائي الماتي: وبوبليك يطيح بخاتشانوف في مباراة ملحمية",
            "subtitle": "ستيفانوس تسيتسيباس يفوز على جيمس داكوورث 6-3 و6-4. الكازاخي بوبليك يقلب الطاولة بشوطين فاصلين.",
            "excerpt": "حجز تسيتسيباس مقعده في نصف نهائي بطولة الماتي بتفوقه التام على داكوورث ليضرب موعدا ناريا مع بوبليك.",
            "body": [
                "واصل اليوناني ستيفانوس تسيتسيباس عروضه القوية في بطولة الماتي المفتوحة يوم الجمعة 23 اكتوبر بتغلبه على الاسترالي جيمس داكوورث بنتيجة 6-3 و6-4 في الدور ربع النهائي. اظهر تسيتسيباس براعة تامة في ارساله مسجلا ثمانية ارسال ساحق ولم يفقد سوى تسع نقاط على ارساله الاول خلال ساعة و22 دقيقة دون ان يواجه اي نقطة لكسر ارساله.",
                "واشعل الكازاخي الكسندر بوبليك حماس الجماهير بتعويضه خسارة المجموعة الاولى امام الروسي كارين خاتشانوف الى فوز مثير 4-6 و7-6(5) و7-6(5) بعد ساعتين و38 دقيقة اطلق خلالها 19 ارسالا ساحقا. سيلتقي بوبليك مع تسيتسيباس في نصف نهائي مرتقب يوم السبت، في حين يجمع نصف النهائي الاخر بين دانييل ميدفيديف ونيكولوز باسيلاشفيلي."
            ]
        }
    },
    "pga-tour-bermuda-round2-blanchet-leads-after-opening-62-2026": {
        "fr": {
            "title": "Bermudes 2e tour : Blanchet en tete apres son 62 inaugural et deux eagles",
            "subtitle": "Chandler Blanchet a signe un score record de 9 sous le par a Port Royal. Corey Conners et Ben Kohles en embuscade a 63.",
            "excerpt": "Chandler Blanchet a survole le premier tour du Butterfield Bermuda Championship avec une carte de 62. Le deuxieme tour s'annonce dispute.",
            "body": [
                "Chandler Blanchet a realise la meilleure carte de sa carriere jeudi en bouclant le premier tour du Butterfield Bermuda Championship en 62 coups (-9) pour s'emparer seul de la tete a Southampton. Profitant de conditions meteo clementes sur le par 71 de Port Royal, l'Americain de 31 ans a signe deux eagles, dont un putt mémorable de plus de 15 metres au trou numero 17.",
                "Une meute de poursuivants se tient a deux coups seulement du leader alors que le deuxieme tour s'est elance vendredi matin. Le Canadien Corey Conners, 61e joueur mondial, et l'Americain Ben Kohles ont tous deux signe un 63 (-7) sans bogey. Le tenant du titre Adam Schenk a commence par un 68 (-3) solide pour rester dans la course au cut."
            ]
        },
        "es": {
            "title": "Bermuda Ronda 2: Blanchet lidera tras abrir con un 62 de dos eagles",
            "subtitle": "Chandler Blanchet registro un historico 9 bajo par en Port Royal. Corey Conners y Ben Kohles persiguen con 63.",
            "excerpt": "Blanchet comando la jornada inaugural del Butterfield Bermuda Championship con 62 golpes (-9). La segunda ronda ya esta en marcha.",
            "body": [
                "Chandler Blanchet firmo la mejor ronda de su vida deportiva este jueves al entregar una tarjeta de 62 golpes (-9) para colocarse como lider solitario del Butterfield Bermuda Championship. En una jornada con vientos mas suaves de lo habitual en el recorrido de Port Royal, Blanchet consiguio dos eagles, coronados por un increible putt de 15 metros en el hoyo 17.",
                "El canadiense Corey Conners y el estadounidense Ben Kohles encabezan el grupo perseguidor tras registrar sendas vueltas de 63 impactos (-7). La segunda ronda dio comienzo el viernes por la manana con 120 jugadores en busca de pasar el corte y luchar por la bolsa de 6 millones de dolares y 500 puntos de la FedExCup de otono."
            ]
        },
        "de": {
            "title": "Bermuda Runde 2: Blanchet fuehrt nach ueberragender 62 mit zwei Eagles",
            "subtitle": "Chandler Blanchet gelingt Karrierebestwert von 9 unter Par in Port Royal. Corey Conners und Ben Kohles lauern bei 63.",
            "excerpt": "Chandler Blanchet ueberragte zum Auftakt der Butterfield Bermuda Championship mit einer 62 (-9). Runde zwei laeuft an der Atlantikkueste.",
            "body": [
                "Chandler Blanchet erwischte am Donnerstag in Southampton den perfekten Auftakt und sicherte sich mit einer 62er-Runde (9 unter Par) die Fuehrung bei der Butterfield Bermuda Championship. Auf dem anspruchsvollen Par-71-Kurs von Port Royal lochte der US-Amerikaner gleich zwei Eagles, darunter einen sensationellen 15-Meter-Putt auf der 17. Spielbahn.",
                "Die Verfolger sitzen ihm jedoch dicht im Nacken: Der Kanadier Corey Conners und Landsmann Ben Kohles eroeffneten mit fehlerfreien 63er-Runden (-7). Am Freitagmorgen startete die zweite Runde fuer das 120-koepfige Teilnehmerfeld, das um ein Preisgeld von sechs Millionen Dollar kaempft. Titelverteidiger Adam Schenk hielt mit einer 68 (-3) Anschluss."
            ]
        },
        "it": {
            "title": "Bermuda 2° giro: Blanchet al comando dopo il 62 iniziale con due eagle",
            "subtitle": "Chandler Blanchet firma il record personale a 9 sotto il par a Port Royal. Corey Conners e Ben Kohles inseguono a 63.",
            "excerpt": "Giro spettacolare per Chandler Blanchet al Butterfield Bermuda Championship con un 62 (-9). Secondo giro al via lungo le scogliere dell'Atlantico.",
            "body": [
                "Chandler Blanchet ha disputato il miglior giro della sua carriera professionistica giovedi, consegnando uno straordinario 62 (-9) per conquistare la vetta solitaria del Butterfield Bermuda Championship. Sul percorso par 71 di Port Royal, Blanchet ha brillato mettendo a segno due eagle, impreziositi da un putt da oltre 15 metri alla buca 17.",
                "Alle sue spalle si trova un gruppo compatto guidato dal canadese Corey Conners e dallo statunitense Ben Kohles, entrambi autori di un ottimo 63 (-7). Il secondo giro ha preso il via venerdi mattina tra le consuete brezze oceaniche, con il campione in carica Adam Schenk a quota 68 (-3) in cerca di conferme."
            ]
        },
        "pl": {
            "title": "Bermudy 2. runda: Blanchet liderem po fenomenalnym otwarciu 62 z dwoma eagle'ami",
            "subtitle": "Chandler Blanchet uzyskal zyciowy wynik 9 ponizej par w Port Royal. Corey Conners i Ben Kohles gonia z wynikiem 63.",
            "excerpt": "Blanchet olsnil w 1. rundzie Butterfield Bermuda Championship, zapisujac na koncie 62 uderzenia (-9). Druga runda w toku.",
            "body": [
                "Chandler Blanchet rozegral w czwartek runde zycia, uzyskujac 62 uderzenia (9 ponizej par) i obejmujac samodzielne prowadzenie w turnieju Butterfield Bermuda Championship. Na malowniczym, nadmorskim polu Port Royal 31-letni Amerykanin trafil dwa eagle, w tym popisowego putta z ponad 15 metrow na 17. dolku.",
                "Tuz za jego plecami plasuje sie grupa poscigowa z Coreyem Connersem i Benem Kohlesem, ktorzy rozpoczeli zmagania z wynikiem 63 uderzen (-7). W piatek rano wystartowala druga runda z udzialem 120 zawodnikow walczacych o pule nagrod wynoszaca 6 milionow dolarow oraz cenne punkty FedExCup Fall."
            ]
        },
        "zh": {
            "title": "百慕大锦标赛次轮：布兰切特首轮射双鹰交出62杆牢牢领跑",
            "subtitle": "钱德勒·布兰切特在皇家港交出生涯最佳单轮-9杆。康纳斯与科尔斯以63杆紧咬。",
            "excerpt": "布兰切特首轮狂轰62杆（-9）独占百慕大锦标赛鳌头。次轮比赛周五在皇家港全面打响。",
            "body": [
                "钱德勒·布兰切特在周四迎来了职业生涯的高光时刻，在皇家港高尔夫球场交出令人惊叹的62杆（低于标准杆9杆），强势领跑百慕大锦标赛首轮。在这座总长6828码的海滨球场上，这位31岁的美国球手射落两头老鹰，其中包括在第17号洞推入的一记超过50英尺的远距离长推。",
                "排在追赶梯队前列的是加拿大名将科里·康纳斯以及本·科尔斯等人，他们均打出63杆（-7）并列第二。第二轮比赛于周五上午正式开杆，120名球员将继续为了600万美元总奖金和500点秋季积分展开厮杀。卫冕冠军亚当·申克首轮以68杆（-3）完赛，保持在晋级线之内。"
            ]
        },
        "ja": {
            "title": "バミューダ選手権第2R：初日2イーグルのブランシェットが62で単独首位発進",
            "subtitle": "チャンドラー・ブランシェットがポートロイヤルで自己最高の9アンダーをマーク。コナーズらが63で追走。",
            "excerpt": "ブランシェットが初日62（-9）の圧巻スコアで首位に立ちました。金曜日午前より第2ラウンドがスタートしています。",
            "body": [
                "チャンドラー・ブランシェットが22日木曜日、ポートロイヤル・ゴルフコースで自己ベストとなる62（9アンダー）をマークし、バタフィールド・バミューダ選手権の単独首位に立ちました。比較的穏やかな風に恵まれた初日、ブランシェットはパー5で2つのイーグルを奪取。17番ホールでは15メートルを超える超ロングパットを沈めました。",
                "2打差の2位タイには63（-7）をマークした世界ランク61位のコーリー・コナーズやベン・コールズらがつけています。大会2日目は金曜朝から第2ラウンドがスタートし、120名の選手たちが賞金総額600万ドルとフェデックスカップ・フォールポイントを懸けてしのぎを削っています。"
            ]
        },
        "ko": {
            "title": "버뮤다 챔피언십 2R: 챈들러 블랑셰, 이글 2방 62타로 단독 선두",
            "subtitle": "블랑셰, 포트 로열에서 개인 통산 최소타 9언더파 기록. 코너스와 콜스가 63타로 맹추격.",
            "excerpt": "블랑셰가 1라운드 62타(-9)를 몰아치며 버뮤다 챔피언십 단독 선두에 올랐습니다. 금요일 오전 2라운드가 열립니다.",
            "body": [
                "미국의 챈들러 블랑셰가 22일 버뮤다 사우샘프턴의 포트 로열 골프 코스에서 열린 PGA 투어 버터필드 버뮤다 챔피언십 1라운드에서 9언더파 62타를 쳐 단독 선두로 나섰습니다. 62타는 블랑셰의 투어 통산 최저타 기록입니다. 17번 홀 15m가 넘는 장거리 이글 퍼트를 포함해 파5 홀에서만 이글 2개를 잡는 맹타를 휘둘렀습니다.",
                "캐나다의 코리 코너스와 벤 콜스가 나란히 보기 없이 7언더파 63타를 쳐 2타 차 공동 2위 그룹을 형성했습니다. 23일 오전부터 120명의 출전 선수들이 600만 달러의 총상금과 페덱스컵 가을 시리즈 포인트를 향해 2라운드 플레이에 돌입했습니다."
            ]
        },
        "ar": {
            "title": "بطولة برمودا الجولة 2: بلانشيت ينفرد بالصدارة بـ62 ضربة مع نسريْن",
            "subtitle": "تشاندلر بلانشيت يسجل افضل جولة في مسيرته بـ9 تحت المعدل في بورت رويال. كونرز وكولز يلاحقانه بـ63.",
            "excerpt": "حقق بلانشيت بداية نارية في بطولة برمودا للغولف ببطاقة 62 ضربة. الجولة الثانية انطلقت الجمعة بمشاركة 120 لاعبا.",
            "body": [
                "قدم الامريكي تشاندلر بلانشيت الجولة الافضل في مسيرته الاحترافية يوم الخميس مسجلا 62 ضربة (9 تحت المعدل) لينفرد بصدارة بطولة برمودا في ساوثهامبتون. استغل بلانشيت هدوء الرياح في ملعب بورت رويال ليسجل نسريْن، ابرزهما رمية رائعة من مسافة 15 مترا في الحفرة السابعة عشرة.",
                "ويحتل الكندي كوري كونرز والامريكي بن كولز المركز الثاني بـ63 ضربة (7 تحت المعدل). بدات الجولة الثانية صباح الجمعة بمشاركة 120 لاعبا يتنافسون على جوائز مالية تبلغ 6 ملايين دولار ونقاط كأس فيديكس الخريفية، في حين سجل حامل اللقب ادم شينك 68 ضربة ليبقى قريبا من قمة الترتيب."
            ]
        }
    },
    "f1-austin-friday-practice-underway-cota-antonelli-gap-102-2026": {
        "fr": {
            "title": "Essais d'Austin lances : Antonelli mene la meute sur la piste du COTA",
            "subtitle": "Les essais libres debutent au Texas. Kimi Antonelli defend 102 points d'avance sur George Russell.",
            "excerpt": "Les monoplaces de Formule 1 ont pris la piste vendredi a Austin pour les premiers essais. Antonelli a sa premiere chance de titre.",
            "body": [
                "Le week-end du Grand Prix des Etats-Unis est passe a la vitesse superieure ce vendredi 23 octobre avec les premiers tours de piste lors des Essais Libres 1 au Circuit des Ameriques a Austin. Sous un ciel texan lumineux, les equipes ont evalue l'usure des pneumatiques et la stabilite aerodynamique dans les virages rapides du premier secteur et la montee mythique du virage 1.",
                "Le prodige de Mercedes Kimi Antonelli aborde ce rendez-vous avec 340 points au compteur et une avance confortable de 102 longueurs sur son equipier George Russell (238). A six courses de la fin, Antonelli dispose a Austin de sa premiere opportunite mathematique de decrocher la couronne mondiale. Chez les constructeurs, Mercedes domine Ferrari 578 a 444 avant les qualifications de samedi."
            ]
        },
        "es": {
            "title": "Practicas de Austin en marcha: Antonelli lidera al pelotón en COTA",
            "subtitle": "Comienzan los entrenamientos libres en Texas. Kimi Antonelli defiende 102 puntos de ventaja sobre Russell.",
            "excerpt": "Los monoplazas de F1 salieron a pista este viernes en Austin. Antonelli afronta su primera opcion matematica de ser campeon mundial.",
            "body": [
                "El Gran Premio de Estados Unidos encendio sus motores este viernes 23 de octubre en el Circuito de las Americas en Austin. Los veinte pilotos completaron la primera sesion de entrenamientos libres sobre el trazado de 5,513 kilometros, ajustando las alturas de conduccion y estudiando el desgaste de neumaticos en las exigentes enlazadas del primer sector.",
                "El lider del mundial Kimi Antonelli llega a Texas con 340 puntos frente a los 238 de su compañero George Russell, acumulando un colchon de 102 puntos. En Austin, el joven italiano cuenta con su primera posibilidad teorica de proclamarse campeon del mundo. En constructores, Mercedes manda comodamente con 578 puntos ante los 444 de Ferrari."
            ]
        },
        "de": {
            "title": "Auftakt in Austin: Antonelli fuehrt das Feld auf den COTA-Kurs",
            "subtitle": "Freies Training in Texas laeuft. Kimi Antonelli verteidigt 102 Punkte Vorsprung auf George Russell.",
            "excerpt": "Die Formel 1 startet am Freitag in Austin in den Fahrbetrieb. WM-Spitzenreiter Antonelli hat den ersten Matchball im Titelrennen.",
            "body": [
                "Das Grand-Prix-Wochenende der Formel 1 in Austin hat am Freitag mit dem 1. Freien Training auf dem Circuit of the Americas Fahrt aufgenommen. Bei sonnigen Bedingungen und Asphalttemperaturen von rund 35 Grad konzentrierten sich die Teams auf Aero-Tests in den geschwungenen Kurven des ersten Sektors sowie auf Longrun-Simulationen mit den harten und mittleren Reifenmischungen.",
                "Mercedes-Youngster Kimi Antonelli fuehrt die Fahrer-Weltmeisterschaft mit 340 Punkten an und liegt 102 Zaehler vor Teamkollege George Russell (238). Austin bietet Antonelli die erste rechnerische Gelegenheit, sich vorzeitig zum Weltmeister zu kroenen. Bei den Konstrukteuren liegt Mercedes mit 578 Punkten klar vor Ferrari (444)."
            ]
        },
        "it": {
            "title": "Prove di Austin al via: Antonelli guida il gruppo sulla pista del COTA",
            "subtitle": "Iniziano le prove libere in Texas. Kimi Antonelli difende 102 punti di vantaggio su George Russell.",
            "excerpt": "Le monoposto di Formula 1 hanno acceso i motori venerdi ad Austin. Antonelli ha il primo match point iridato del 2026.",
            "body": [
                "Il Gran Premio degli Stati Uniti e entrato nel vivo venerdi 23 ottobre con la prima sessione di prove libere al Circuit of the Americas di Austin. Le venti monoposto sono scese in pista lungo i 5,513 km del tracciato texano, focalizzandosi sul bilanciamento aerodinamico e sulla gestione termica delle gomme in vista delle qualifiche di sabato.",
                "Il leader della classifica Kimi Antonelli si presenta ad Austin con 340 punti contro i 238 del compagno George Russell, forte di 102 lunghezze di vantaggio. Sul tracciato di Austin Antonelli avra la prima opportunita matematica di chiudere i conti mondiali. Nel mondiale costruttori la Mercedes guida saldamente con 578 punti contro i 444 della Ferrari."
            ]
        },
        "pl": {
            "title": "Treningi w Austin rozpoczeta: Antonelli prowadzi stawke na torze COTA",
            "subtitle": "Kierowcy wyjechali na tor w Teksasie. Kimi Antonelli broni 102 punktow przewagi nad George'em Russellem.",
            "excerpt": "Bolidy Formuly 1 zainaugurowaly jazdy w Austin podczas piatkowych treningow. Antonelli ma pierwsza szanse na tytul mistrza swiata.",
            "body": [
                "Weekend Grand Prix Stanow Zjednoczonych ruszyl pelna para w piatek 23 pazdziernika wraz z rozpoczeciem 1. treningu na Circuit of the Americas w Austin. Kierowcy i inzynierowie poswiecili pierwsza godzine zajec na weryfikacje poprawek aerodynamicznych w szybkich zakretach pierwszego sektora oraz analize zuzycia ogumienia na dlugiej prostej.",
                "Kimi Antonelli przyjechal do Teksasu jako zdecydowany lider klasyfikacji generalnej z 340 punktami, majac 102 punkty przewagi nad kolega z Mercedes George'em Russellem (238). W Austin Wloch ma pierwsza matematyczna szanse na przypieczetowanie tytulu mistrzowskiego. W klasyfikacji konstruktorow Mercedes ma 578 punktow i wyprzedza Ferrari o 134 punkty."
            ]
        },
        "zh": {
            "title": "奥斯汀练习赛打响：安东内利领衔众车手驶入美洲赛道",
            "subtitle": "美国站练习赛正式展开。基米·安东内利在车手榜上对拉塞尔保持102分领先优势。",
            "excerpt": "F1赛车周五在得州美洲赛道展开赛道角逐。领头羊安东内利迎来锁定年度世界冠军的首个理论赛点。",
            "body": [
                "2026年F1美国大奖赛于10月23日周五正式拉开战幕，20辆赛车驶入得克萨斯州奥斯汀的美洲赛道展开一练。在秋日晴朗的天气下，赛道温度达到35摄氏度，各支车队抓紧60分钟的时间评估赛车在1号弯上坡发卡弯以及连续高速S弯中的气动表现与轮胎衰减情况。",
                "梅赛德斯新星基米·安东内利以340分稳居积分榜榜首，对队友拉塞尔（238分）手握102分的巨大优势。本赛季仅剩六场分站赛，奥斯汀站是安东内利提前锁定车手总冠军头衔的首个数学可能站。车队积分榜方面，梅赛德斯以578分大幅领先法拉利的444分。"
            ]
        },
        "ja": {
            "title": "オースティンで練習走行開始：アントネッリがCOTAのコースインを牽引",
            "subtitle": "テキサスでフリー走行が幕開け。キミ・アントネッリがジョージ・ラッセルに102点リードを保持。",
            "excerpt": "F1マシンが金曜日にサーキット・オブ・ジ・アメリカズを疾走。アントネッリが初のタイトル確定チャンスを迎えます。",
            "body": [
                "2026年F1アメリカGPの走行が23日金曜、テキサス州オースティンのサーキット・オブ・ジ・アメリカズで幕を開けました。好天に恵まれたCOTAで各チームはフリー走行1回目に臨み、上り坂の1コーナーや高速S字区間での空力チェックとタイヤの摩耗テストに注力しました。",
                "ポイントリーダーのキミ・アントネッリは340点を獲得しており、チームメイトのジョージ・ラッセル（238点）に102点の大差をつけています。残り6戦となった今季、オースティンで自身初の世界王者確定の理論的可能性を迎えています。コンストラクターズ部門でもメルセデスが578点でフェラーリ（444点）を大きく引き離しています。"
            ]
        },
        "ko": {
            "title": "오스틴 주행 시작: 안토넬리, COTA 트랙에서 첫 연습 세션 돌입",
            "subtitle": "텍사스에서 금요 연습 주행 개막. 키미 안토넬리, 조지 러셀에 102점 차 리드 수성.",
            "excerpt": "F1 머신들이 금요일 오스틴 COTA 트랙을 질주하기 시작했습니다. 선두 안토넬리가 첫 챔피언 확정 기회를 맞았습니다.",
            "body": [
                "2026 F1 미국 그랑프리 레이스 주말이 23일 금요일 오스틴의 서킷 오브 디 아메리카스(COTA)에서 연습 주행 1세션과 함께 본격적인 막을 올렸습니다. 맑은 날씨 속에 트랙 온도 35도에 이르는 조건에서 20대의 머신이 1번 헤어핀과 연속 S자 고속 코너 구간에서 에어로 밸런스와 타이어 마모도를 점검했습니다.",
                "메르세데스의 키미 안토넬리는 340점을 획득해 팀 동료 조지 러셀(238점)에 102점 차 여유 있는 선두를 달리고 있습니다. 이번 오스틴은 안토넬리가 첫 드라이버 월드 챔피언십을 조기에 확정할 수 있는 첫 수학적 기회입니다. 컨스트럭터 부문에서도 메르세데스가 578점으로 페라리(444점)를 여유 있게 앞서 있습니다."
            ]
        },
        "ar": {
            "title": "تجارب اوستن تبدا: انتونيللي يقود السائقين على حلبة الامريكتين",
            "subtitle": "انطلاق التجارب الحرة في تكساس. كيمي انتونيللي يدافع عن صدارة بفارق 102 نقطة امام راسل.",
            "excerpt": "انطلقت سيارات الفورمولا 1 على حلبة الامريكتين الجمعة لخوض التجارب الحرة. انتونيللي يملك اول فرصة لحسم اللقب العالمي.",
            "body": [
                "بدات عطلة اسبوع جائزة الولايات المتحدة الكبرى لعام 2026 يوم الجمعة 23 اكتوبر مع انطلاق حصة التجارب الحرة الاولى على حلبة الامريكتين في اوستن. ركزت الفرق خلال الحصة على موازنة الانسيابية الهوائية عبر المنعطفات السريعة ومراقبة تآكل الاطارات على المسار البالغ 5.513 كم.",
                "يدخل سائق مرسيدس الشاب كيمي انتونيللي المنافسات برصيد 340 نقطة متقدما بفارق 102 نقطة عن زميله جورج راسل (238). ومع تبقي ست جولات، يملك انتونيللي في اوستن اولى فرصه الحسابية للتتويج رسميا بلقب بطولة العالم للسائقين، في حين تتصدر مرسيدس بطولة الصانعين بـ578 نقطة امام فيراري (444)."
            ]
        }
    },
    "premier-league-friday-ipswich-forest-kickoff-tonight-derby-eve-2026": {
        "fr": {
            "title": "La 8e journee debute ce soir : Ipswich recoit Forest a Portman Road",
            "subtitle": "Coup d'envoi vendredi avant le derby londonien Chelsea - Spurs de samedi. Manchester City en tete a 21.",
            "excerpt": "La Premier League reprend ses droits ce vendredi avec Ipswich Town face a Nottingham Forest. City possede trois points d'avance sur Arsenal.",
            "body": [
                "La 8e journee de Premier League debute ce vendredi 23 octobre sous les projecteurs de Portman Road ou Ipswich Town accueille Nottingham Forest a 20h00 heure britannique. Les Tractor Boys occupent la 12e place avec 8 points (2-2-3) et comptent sur leur public apres avoir tenu tete au champion Manchester City le week-end dernier. Forest pointe au 19e rang avec 5 points et doit reagir pour sortir de la zone de relegation.",
                "L'affiche phare du week-end se deroulera samedi a Stamford Bridge avec le derby londonien opposant Chelsea a Tottenham. Les Spurs abordent ce choc en confiance apres avoir battu Coventry 3-1 pour grimper a la 16e place a 6 points. Chelsea est quatrieme a 13 points, a bonne distance de Manchester City, leader sans faute avec 21 points en sept matches, suivi d'Arsenal a 18."
            ]
        },
        "es": {
            "title": "La jornada 8 arranca esta noche: Ipswich recibe a Forest en Portman Road",
            "subtitle": "Accion de viernes por la noche antes del derbi Chelsea vs Spurs el sabado. Manchester City lidera con 21.",
            "excerpt": "La Premier League vuelve este viernes con el duelo entre Ipswich y Nottingham Forest. El City mantiene tres puntos de ventaja sobre el Arsenal.",
            "body": [
                "La octava fecha de la Premier League arranca este viernes 23 de octubre bajo los focos de Portman Road con el choque entre Ipswich Town y Nottingham Forest a las 20:00 hora local. Ipswich se ubica en el puesto 12 con 8 puntos tras su gran despliegue ante el Manchester City la semana pasada. Nottingham Forest ocupa la 19ª plaza con 5 puntos, necesitado de sumar para salir de la zona de descenso.",
                "El plato fuerte del fin de semana llegara el sabado con el apasionante derbi londinense entre Chelsea y Tottenham Hotspur en Stamford Bridge. Los Spurs llegan con la moral alta tras batir 3-1 a Coventry y escalar a la 16ª casilla con 6 puntos. El Chelsea se ubica cuarto con 13 puntos, a la caza del lider Manchester City que ostenta un impecable 21 de 21, tres puntos por delante del Arsenal (18)."
            ]
        },
        "de": {
            "title": "8. Spieltag startet heute Abend: Ipswich empfaengt Forest an der Portman Road",
            "subtitle": "Freitagsspiel eroeffnet das Wochenende vor dem Londoner Derby Chelsea gegen Spurs am Samstag. City fuehrt mit 21.",
            "excerpt": "Die Premier League startet am Freitagabend mit Ipswich Town gegen Nottingham Forest in den 8. Spieltag. Manchester City hat drei Punkte Vorsprung auf Arsenal.",
            "body": [
                "Der 8. Spieltag der englischen Premier League beginnt am Freitagabend, 23. Oktober, an der Portman Road, wo Aufsteiger Ipswich Town um 20:00 Uhr Ortszeit auf Nottingham Forest trifft. Die Gastgeber stehen mit acht Punkten auf Rang 12 und wollen ihren Heimvorteil nutzen. Forest liegt mit fuenf Zaehlern auf dem vorletzten 19. Platz und braucht dringend Punkte im Abstiegskampf.",
                "Das Topspiel der Runde steigt am Samstagabend an der Stamford Bridge beim Londoner Stadtderby zwischen Chelsea und Tottenham Hotspur. Die Spurs schöpfen nach dem 3-1-Erfolg ueber Coventry neuen Mut und kletterten auf Rang 16. Chelsea belegt mit 13 Punkten Platz vier. An der Spitze thront Manchester City mit der Maximalausbeute von 21 Punkten aus sieben Spielen, drei Zaehler vor Verfolger Arsenal (18)."
            ]
        },
        "it": {
            "title": "L'8a giornata scatta stasera: l'Ipswich ospita il Forest a Portman Road",
            "subtitle": "Anticipo del venerdi prima del derby Chelsea - Spurs di sabato. Manchester City al comando a quota 21.",
            "excerpt": "La Premier League riparte venerdi sera con Ipswich Town contro Nottingham Forest. City avanti di tre lunghezze sull'Arsenal.",
            "body": [
                "L'ottavo turno di Premier League si apre venerdi 23 ottobre sotto i riflettori di Portman Road con la sfida tra Ipswich Town e Nottingham Forest alle 20:00 inglesi. I padroni di casa si trovano al 12° posto con 8 punti dopo la bella prova contro il Manchester City, mentre il Forest e penultimo a quota 5 e cerca un risultato positivo per allontanarsi dalla zona rossa.",
                "La gara di cartello del fine settimana andra in scena sabato a Stamford Bridge con il derby londinese tra Chelsea e Tottenham Hotspur. Gli Spurs arrivano rinfrancati dal 3-1 inflitto al Coventry che li ha portati al 16° posto con 6 punti. Il Chelsea e quarto con 13 punti, all'inseguimento della capolista Manchester City che guida a punteggio pieno a 21 punti davanti all'Arsenal (18)."
            ]
        },
        "pl": {
            "title": "8. kolejka rusza dzis wieczorem: Ipswich podejmuje Forest na Portman Road",
            "subtitle": "Piatkowy mecz otwiera weekend przed sobotnimi derbami Chelsea ze Spurs. Manchester City liderem z 21 punktami.",
            "excerpt": "Premier League wraca do gry w piatek starciem Ipswich Town z Nottingham Forest. Manchester City ma trzy punkty przewagi nad Arsenalem.",
            "body": [
                "Osioma kolejka Premier League rozpoczyna sie w piatek 23 pazdziernika na Portman Road, gdzie Ipswich Town zmierzy sie z Nottingham Forest o 20:00 czasu brytyjskiego. Gospodarze zajmuja 12. miejsce z dorobkiem 8 punktow po zacieciu rozegranym meczu z Manchesterem City. Forest plasuja sie na 19. pozycji z 5 punktami i desperacko szukaja punktow, by opuscic strefe spadkowa.",
                "Głównym wydarzeniem weekendu beda sobotnie derby Londynu na Stamford Bridge pomiedzy Chelsea a Tottenhamem Hotspur. Spurs przystepuja do spotkania podbudowani zwyciestwem 3-1 nad Coventry, ktore pozwolilo im awansowac na 16. miejsce z 6 punktami. Chelsea jest czwarta z 13 punktami, goniac liderujacy Manchester City (21 punktow, 7 wygranych z rzedu) oraz Arsenal (18)."
            ]
        },
        "zh": {
            "title": "英超第8轮今晚打响：伊普斯维奇坐镇波特曼路迎战森林",
            "subtitle": "周五夜战揭开大幕，周六迎来切尔西对热刺德比焦点战。曼城积21分高居榜首。",
            "excerpt": "英超第8轮周五晚间重燃战火，伊普斯维奇主场对决诺丁汉森林。领头羊曼城领先阿森纳3分。",
            "body": [
                "英格兰足球超级联赛第8轮于10月23日周五晚间打响，伊普斯维奇在英国时间20:00坐镇波特曼路球场迎战诺丁汉森林。拖拉机男孩目前7战积8分暂列第12位，上轮对阵卫冕冠军曼城展现出顽强斗志。诺丁汉森林积5分深陷降级区排在第19位，急需抢分逃离降级泥潭。",
                "本轮焦点大战将于周六在斯坦福桥球场上演，由切尔西主场迎战托特纳姆热刺。热刺在周一3-1逆转考文垂收获赛季首胜，目前积6分升至第16位。切尔西积13分暂列第四，落后7战全胜积21分的领头羊曼城8分，阿森纳以18分排在第二。"
            ]
        },
        "ja": {
            "title": "第8節が今夜キックオフ：イプスウィッチが本拠地でフォレストと対戦",
            "subtitle": "土曜のチェルシー対スパーズのロンドンダービーを前に金曜夜戦が開幕。首位シティは勝点21。",
            "excerpt": "プレミアリーグ第8節が金曜ナイターで開幕。イプスウィッチ対ノッティンガム・フォレストの一戦から週末が始まります。",
            "body": [
                "プレミアリーグ第8節が23日金曜夜、ポートマン・ロードで幕を開けます。英国時間20:00より12位のイプスウィッチ・タウン（勝点8）が19位のノッティンガム・フォレスト（勝点5）をホームに迎えます。前節マンチェスター・シティを相手に善戦したイプスウィッチに対し、降格圏脱出を図るフォレストが勝ち点獲得を狙います。",
                "今節のメインマッチは土曜日にスタンフォード・ブリッジで行われるチェルシー対トッテナム・ホットスパーのロンドンダービーです。月曜日にコベントリーを3-1で下して16位に浮上したスパーズに対し、4位のチェルシー（勝点13）が激突。7戦全勝のマンチェスター・シティ（21点）がアーセナル（18点）を抑えて首位を快走しています。"
            ]
        },
        "ko": {
            "title": "프리미어리그 8라운드 오늘 밤 개막: 입스위치, 홈에서 포레스트와 격돌",
            "subtitle": "토요일 첼시 대 토트넘 런던 더비에 앞서 금요 야간 경기 시작. 맨시티 승점 21점 선두.",
            "excerpt": "프리미어리그 8라운드가 포트먼 로드에서 개막합니다. 입스위치와 노팅엄 포레스트가 맞붙으며 맨시티가 선두를 달리고 있습니다.",
            "body": [
                "잉글랜드 프리미어리그 8라운드가 23일 금요일 영국 현지 시간 20:00 포트먼 로드에서 열리는 입스위치 타운과 노팅엄 포레스트의 맞대결로 출발합니다. 12위 입스위치(승점 8)는 지난 라운드 맨시티와 접전을 펼친 기세를 이어가고자 하며, 19위 포레스트(승점 5)는 강등권 탈출을 위해 승점이 절실합니다.",
                "이번 라운드 최대 하이라이트는 토요일 스탬퍼드 브리지에서 열리는 첼시와 토트넘 홋스퍼의 런던 더비입니다. 토트넘은 코번트리전 3-1 역전승으로 16위로 올라섰고, 첼시는 승점 13점으로 4위에 자리하고 있습니다. 7전 전승으로 승점 21점을 쌓은 맨체스터 시티가 아스널(18점)에 앞서 선두를 질주 중입니다."
            ]
        },
        "ar": {
            "title": "الجولة 8 تنطلق الليلة: ايبسويتش يستضيف نوتنغهام فورست في بورتمان رود",
            "subtitle": "مواجهة الجمعة تفتتح عطلة الاسبوع قبل ديربي لندن بين تشيلسي وتوتنهام السبت. سيتي في الصدارة بـ21.",
            "excerpt": "تعود عجلة الدوري الانجليزي للدوران مساء الجمعة بلقاء ايبسويتش وفورست. مانشستر سيتي يتقدم بثلاث نقاط عن ارسنال.",
            "body": [
                "تنطلق مباريات الجولة الثامنة من الدوري الانجليزي الممتاز مساء الجمعة 23 اكتوبر على ارضية ملعب بورتمان رود حيث يستضيف ايبسويتش تاون نظيره نوتنغهام فورست الساعة 20:00 بتوقيت بريطانيا. يحتل ايبسويتش المركز الثاني عشر برصيد 8 نقاط بعد ادائه القوي امام مانشستر سيتي، بينما يبحث فورست صاحب المركز التاسع عشر برصيد 5 نقاط عن الهروب من منطقة الخطر.",
                "وتتجه الانظار يوم السبت نحو ملعب ستامفورد بريدج لمتابعة ديربي لندن المرتقب بين تشيلسي وتوتنهام هوتسبير. يدخل توتنهام المواجهة بمعنويات مرتفعة بعد فوزه 3-1 على كوفنتري وتقدمه للمركز السادس عشر برصيد 6 نقاط، بينما يحتل تشيلسي المركز الرابع برصيد 13 نقطة، في حين يتصدر مانشستر سيتي الترتيب بالعلامة الكاملة (21 نقطة من 7 مباريات) امام ارسنال (18)."
            ]
        }
    },
    "wnba-finals-2026-game4-eve-dream-chase-title-valkyries-face-brink": {
        "fr": {
            "title": "Finales WNBA match 4 : le Dream a un pas du titre face aux Valkyries",
            "subtitle": "Atlanta mene 2-1 apres son carton 97-71 au match 3. Angel Reese vise une 4e double-double consecutive.",
            "excerpt": "Le Dream d'Atlanta n'est plus qu'a une victoire de son tout premier titre WNBA. Golden State doit s'imposer a l'exterieur pour survivre.",
            "body": [
                "L'Atlanta Dream aborde le match 4 des Finales WNBA ce vendredi 23 octobre a la State Farm Arena avec l'opportunite de decrocher le premier championnat de son histoire. Portee par un succes ecrasant 97-71 lors du match 3 mercredi, la franchise d'Atlanta mene 2-1 dans cette serie au meilleur des cinq rencontres apres avoir domine chaque quart-temps.",
                "Angel Reese continue d'ecrire l'histoire du basketball feminin. Avec 21 points, 12 rebonds et trois interceptions au match 3, elle est devenue la premiere joueuse de l'histoire de la WNBA a realiser un double-double lors de chacune de ses trois premieres sorties en Finales. Pour les Golden State Valkyries, ce match 4 est synonyme de survie pour esperer arracher un match 5 decisif a San Francisco."
            ]
        },
        "es": {
            "title": "Finales WNBA Juego 4: Dream busca coronarse y Valkyries lucha por sobrevivir",
            "subtitle": "Atlanta lidera 2-1 tras apabullar 97-71 en el Juego 3. Angel Reese busca su cuarto doble-doble seguido.",
            "excerpt": "Atlanta esta a un triunfo de su primer anillo de la WNBA. Golden State necesita ganar a domicilio para forzar el Juego 5.",
            "body": [
                "El Atlanta Dream llega al Juego 4 de las Finales WNBA este viernes 23 de octubre en el State Farm Arena con la posibilidad de levantar el primer trofeo de campeon de su historia. Atlanta domino de principio a fin el Juego 3 del miercoles al vencer 97-71 a las Golden State Valkyries ante 17.854 enfervorizados aficionados.",
                "Angel Reese sigue dejando huella con numeros legendarios: 21 puntos, 12 rebotes y 3 robos en el tercer encuentro para convertirse en la primera jugadora en la historia de la liga con un doble-doble en sus tres primeros juegos de Finales. Las Valkyries, por su parte, se juegan el todo por el todo en Atlanta con la obligacion de ganar para forzar un quinto y definitivo duelo en San Francisco."
            ]
        },
        "de": {
            "title": "WNBA-Finals Spiel 4: Dream greifen nach erstem Titel, Valkyries vor dem Aus",
            "subtitle": "Atlanta fuehrt nach 97-71-Gala mit 2-1. Angel Reese jagt viertes Final-Double-Double in Folge.",
            "excerpt": "Atlanta steht nur noch einen Sieg vor der ersten WNBA-Meisterschaft der Vereinsgeschichte. Golden State muss in Spiel 4 auswaerts siegen.",
            "body": [
                "Das Atlanta Dream geht am Freitag, 23. Oktober, mit einer 2-1-Serienfuehrung in Spiel 4 der WNBA-Finals in der heimischen State Farm Arena. Nach dem souveraenen 97-71-Erfolg am Mittwochabend gegen die Golden State Valkyries haben die Gastgeberinnen nun Matchball auf den ersten Meistertitel ihrer Franchise-Historie.",
                "Angel Reese schrieb in Spiel 3 erneut Geschichte: Mit 21 Punkten, 12 Rebounds und drei Steals avancierte sie zur ersten Spielerin der WNBA-Historie, der in ihren ersten drei Finalpartien jeweils ein Double-Double gelang. Fuer das Expansionsteam der Valkyries ist die Partie ein echtes Endspiel: Nur ein Auswaertssieg rettet die Titelchancen und erzwingt ein entscheidendes fuenftes Spiel in San Francisco."
            ]
        },
        "it": {
            "title": "Finals WNBA Gara 4: il Dream a una vittoria dal titolo, Valkyries all'angolo",
            "subtitle": "Atlanta conduce 2-1 dopo il 97-71 in Gara 3. Angel Reese a caccia della quarta doppia doppia di fila.",
            "excerpt": "L'Atlanta Dream ha a disposizione il match point per il primo anello WNBA della sua storia. Golden State deve vincere in trasferta.",
            "body": [
                "L'Atlanta Dream affronta venerdi 23 ottobre Gara 4 delle WNBA Finals alla State Farm Arena con la possibilita concreta di conquistare il primo titolo nella storia della franchigia. Dopo la netta affermazione per 97-71 in Gara 3 mercoledi sera, Atlanta guida la serie per 2-1 contro le Golden State Valkyries davanti al proprio caldissimo pubblico.",
                "Angel Reese continua a incantare: i 21 punti, 12 rimbalzi e tre recuperi di Gara 3 l'hanno resa la prima giocatrice nella storia della lega a collezionare una doppia doppia in ciascuna delle sue prime tre presenze nelle Finals. Le Valkyries sono chiamate all'impresa esterna per prolungare la serie ed evitare l'eliminazione, cercando di riportare la sfida a San Francisco per Gara 5."
            ]
        },
        "pl": {
            "title": "Finaly WNBA mecz 4: Dream o krok od mistrzostwa, Valkyries pod sciana",
            "subtitle": "Atlanta prowadzi 2-1 po pogromie 97-71 w meczu 3. Angel Reese celuje w czwarte double-double z rzedu.",
            "excerpt": "Atlanta Dream potrzebuje jeszcze tylko jednego zwyciestwa do upragnionego mistrzostwa WNBA. Golden State musi wygrac na wyjezdzie.",
            "body": [
                "Atlanta Dream przystepuje w piatek 23 pazdziernika do czwartego meczu finalow WNBA w State Farm Arena, majac szanse na przypieczetowanie pierwszego w historii tytulu mistrzowskiego. Po srodowym nokaucie 97-71 nad Golden State Valkyries zespol z Atlanty prowadzi w serii do trzech zwyciestw 2-1.",
                "Angel Reese kontynuuje swoj historyczny marsz. Z dorobkiem 21 punktow, 12 zbiorek i trzech przechwytow w meczu 3 zostala pierwsza koszykarka w dziejach WNBA z double-double w kazdym ze swoich trzech pierwszych wystepow w finalach. Dla Valkyries piatkowy mecz to starcie o wszystko, w ktorym musza wygrac, by doprowadzic do decydujacego piatego pojedynku w San Francisco."
            ]
        },
        "zh": {
            "title": "WNBA总决赛第4战：梦想距离首冠一步之遥，女武神背水一战",
            "subtitle": "梦想在第3战97-71大胜后总比分2-1领先。安吉尔·里斯冲击连续第四场两双。",
            "excerpt": "亚特兰大梦想距离队史首座WNBA总冠军仅差一场胜利。金州女武神在客场迎来不容有失的生死战。",
            "body": [
                "亚特兰大梦想在10月23日周五迎来WNBA总决赛第4战的赛点较量，球队有望在州立农业球馆斩获建队以来的首座总冠军奖杯。在周三晚间的第3战中，梦想全队状态神勇，以97-71大胜新军金州女武神，在五局三胜制的系列赛中取得2-1的大比分领先。",
                "超级新星安吉尔·里斯在第3战交出21分12篮板3抢断的华丽答卷，成为WNBA历史上第一位在个人前三场总决赛均砍下两双的球员。对金州女武神而言，周五的客场之战没有任何退路，全队必须顶住亚特兰大主场近两万名球迷的声浪全力争胜，才能将悬念带回旧金山的主场决战。"
            ]
        },
        "ja": {
            "title": "WNBAファイナル第4戦：ドリームが初制覇へ王手、ヴァルキリーズは背水の陣",
            "subtitle": "第3戦で97-71と圧倒したアトランタが2勝1敗でリード。エンジェル・リーズは4戦連続ダブルダブルを狙う。",
            "excerpt": "アトランタ・ドリームが悲願のWNBA初優勝まであと1勝に迫りました。ヴァルキリーズは敵地での第4戦に生き残りを懸けます。",
            "body": [
                "アトランタ・ドリームは23日金曜日、本拠地ステートファーム・アリーナでWNBAファイナル第4戦を迎えます。水曜日の第3戦でゴールデンステイト・ヴァルキリーズを97-71で圧倒し、通算2勝1敗としたドリームは、球団創設以来初となるチャンピオンリング獲得に王手をかけています。",
                "ルーキーのエンジェル・リーズは第3戦で21得点、12リバウンド、3スティールを挙げ、WNBA史上初となるファイナル開幕3戦連続ダブルダブルを達成しました。一方、後がなくなったヴァルキリーズは敵地で勝利を挙げ、サンフランシスコでの第5戦へ持ち込む必要があります。"
            ]
        },
        "ko": {
            "title": "WNBA 파이널 4차전: 드림 창단 첫 우승 눈앞, 발키리스 벼랑 끝 승부",
            "subtitle": "아틀란타, 3차전 97-71 압승 힘입어 2-1 리드. 앤젤 리스 4경기 연속 더블더블 정조준.",
            "excerpt": "아틀란타 드림이 구단 사상 첫 WNBA 우승까지 단 1승만을 남겨두고 있습니다. 골든스테이트는 4차전에서 배수의 진을 칩니다.",
            "body": [
                "아틀란타 드림이 23일 금요일 스테이트 팜 아레나에서 골든스테이트 발키리스와 WNBA 파이널 4차전을 치릅니다. 수요일 3차전에서 97-71 대승을 거두며 시리즈 전적 2승 1패를 만든 아틀란타는 안방에서 구단 역사상 첫 파이널 우승 트로피를 들어 올릴 절호의 기회를 잡았습니다.",
                "앤젤 리스는 3차전에서 21득점 12리바운드 3스틸을 올리며 WNBA 역사상 최초로 개인 첫 파이널 3경기 연속 더블더블이라는 대기록을 작성했습니다. 반면 패배 시 시즌이 종료되는 골든스테이트는 반드시 원정 승리를 따내 승부를 샌프란시스코 5차전으로 끌고 가야 하는 상황입니다."
            ]
        },
        "ar": {
            "title": "نهائيات WNBA المباراة 4: دريم على بعد خطوة من اللقب التاريخي وفالكيريز يقاتل للبقاء",
            "subtitle": "اتلانتا يتقدم 2-1 بعد اكتساح المباراة الثالثة 97-71. انجيل ريس تبحث عن رابع ثنائية مزدوجة متتالية.",
            "excerpt": "بات اتلانتا دريم على بعد فوز واحد من التتويج بلقبه الاول في تاريخ WNBA. ويتعين على غولدن ستيت الفوز خارج ارضه لفرض مباراة خامسة.",
            "body": [
                "يدخل اتلانتا دريم المباراة الرابعة من نهائيات WNBA يوم الجمعة 23 اكتوبر على صالة ستيت فارم ارينا وهو يملك فرصة تاريخية لحسم اول لقب في مسيرته. يتقدم دريم في السلسلة 2-1 بعد فوزه العريض 97-71 في المباراة الثالثة مساء الاربعاء امام اكثر من 17 الف مشجع.",
                "وتواصل انجيل ريس كتابة التاريخ بعد تسجيلها 21 نقطة و12 متابعة و3 سرقات للكرة في المباراة الثالثة لتصبح اول لاعبة في تاريخ البطولة تحقق ثنائية مزدوجة في مبارياتها الثلاث الاولى بالنهائيات. في المقابل، تقف لاعبات غولدن ستيت فالكيريز امام مواجهة مصيرية لا تقبل القسمة على اثنين للابقاء على حظوظهن وفرض مباراة خامسة فاصلة في سان فرانسيسكو."
            ]
        }
    }
}

# Strict validation
for slug, langs in OCT23_STORIES.items():
    for lang, trans in langs.items():
        for field, val in trans.items():
            if isinstance(val, str):
                assert "—" not in val, f"Em-dash in {slug} {lang} {field}"
                assert "--" not in val, f"Double-hyphen in {slug} {lang} {field}"
            elif isinstance(val, list):
                for i, item in enumerate(val):
                    assert "—" not in item, f"Em-dash in {slug} {lang} {field}[{i}]"
                    assert "--" not in item, f"Double-hyphen in {slug} {lang} {field}[{i}]"

print("Verification passed! No em-dashes or double-hyphens.")

snippet_parts = []
for slug, langs in OCT23_STORIES.items():
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

print("Successfully injected October 23 translations into frontend/src/i18n/stories.ts")
