# -*- coding: utf-8 -*-
import json
import re

OCT26_STORIES = {
    "f1-austin-antonelli-crowned-world-champion-cota-verstappen-2026": {
        "fr": {
            "title": "Antonelli sacre champion du monde de Formule 1 au COTA : premier titre a Austin",
            "subtitle": "La revelation de Mercedes s'impose depuis la pole tandis que Russell termine huitieme. Antonelli devient le plus jeune champion de l'histoire.",
            "excerpt": "Kimi Antonelli a converti sa pole position en victoire au Grand Prix des Etats-Unis dimanche, s'assurant mathematiquement le titre mondial 2026.",
            "body": [
                "Kimi Antonelli est entre dans la legende du sport automobile ce dimanche 25 octobre en remportant une victoire magistrale de bout en bout au Grand Prix des Etats-Unis pour sceller le titre de champion du monde des pilotes 2026. Parti en pole position, le jeune Italien a parfaitement resiste a la pression de Max Verstappen au depart avant de derouler une strategie a deux arrets sans la moindre faille sous la chaleur texane. Franchissant la ligne avec 3,8 secondes d'avance sur Charles Leclerc, Antonelli a fait chavirer de joie le stand Mercedes.",
                "L'officialisation mathematique du sacre est intervenue lorsque son dernier rival pour le titre, son coequipier George Russell, n'a pu faire mieux que huitieme. Avec cet ecart, Antonelli porte son total a 365 points et s'assure un avantage inattaquable de 123 points alors qu'il ne reste que 112 points a distribuer. Verstappen complete le podium devant Lewis Hamilton et Lando Norris, ouvrant une nouvelle ere de domination pour les Fleches d'Argent."
            ]
        },
        "es": {
            "title": "Antonelli se corona campeon mundial de Formula 1 en COTA: primer titulo sellado en Austin",
            "subtitle": "El joven prodigio de Mercedes gana desde la pole y Russell termina octavo. Antonelli es el campeon mas joven de la historia moderna.",
            "excerpt": "Kimi Antonelli convirtio su pole position en una victoria dominante en el Gran Premio de Estados Unidos el domingo para consagrarse campeon mundial de 2026.",
            "body": [
                "Kimi Antonelli inscribio su nombre con letras de oro en la historia del automovilismo este domingo 25 de octubre, al conseguir una brillante victoria de punta a punta en el Gran Premio de Estados Unidos para proclamarse campeon mundial de pilotos 2026. Saliendo desde la pole position, el italiano contuvo la presion de Max Verstappen en los primeros metros y gestiono a la perfeccion su estrategia de dos paradas en el abrasivo asfalto de Austin. Al cruzar la meta con 3.8 segundos de ventaja sobre Charles Leclerc, desato la euforia en Mercedes.",
                "La confirmacion matematica llego gracias al octavo puesto de su companero George Russell, unico rival con opciones remotas de campeonato. La renta elevo a Antonelli hasta los 365 puntos, estableciendo una ventaja inalcanzable de 123 puntos con solo 112 unidades en disputa en las ultimas cuatro citas. Verstappen finalizo en el tercer escalon del podio por delante de Lewis Hamilton y Lando Norris."
            ]
        },
        "de": {
            "title": "Antonelli auf dem COTA zum Formel-1-Weltmeister gekroent: Erster WM-Titel in Austin perfekt",
            "subtitle": "Mercedes-Youngster siegt von der Pole waehrend Russell Rang acht belegt. Antonelli kuerzt sich zum juengsten Champion der Formel-1-Historie.",
            "excerpt": "Kimi Antonelli feierte am Sonntag beim Großen Preis der USA einen souveraenen Start-Ziel-Sieg und sicherte sich vorzeitig den Weltmeistertitel 2026.",
            "body": [
                "Kimi Antonelli schrieb am Sonntag, den 25. Oktober, Motorsportgeschichte: Mit einem souveraenen Start-Ziel-Sieg beim Großen Preis der USA kraente sich der junge Italiener vorzeitig zum Formel-1-Weltmeister 2026. Von der Pole Position gestartet, wehrte Antonelli in Kurve 1 den Angriff von Max Verstappen ab und spulte auf dem heißen Kurs in Austin ein makelloses Rennen mit zwei Boxenstopps ab. Nach 56 Runden siegte er mit 3,8 Sekunden Vorsprung vor Ferrari-Pilot Charles Leclerc.",
                "Da sein einziger verbliebener Rivale im Titelkampf, Teamkollege George Russell, nicht ueber Rang acht hinauskam, wuchs Antonellis Punktestand auf 365 Zaehler an. Bei 123 Punkten Vorsprung und nur noch 112 zu vergebenden Punkten ist ihm der WM-Titel rechnerisch nicht mehr zu nehmen. Verstappen kletterte als Dritter auf das Podest, gefolgt von Lewis Hamilton und Lando Norris."
            ]
        },
        "it": {
            "title": "Antonelli incoronato campione del mondo di Formula 1 al COTA: primo alloro iridato ad Austin",
            "subtitle": "Il fenomeno della Mercedes trionfa dalla pole mentre Russell chiude ottavo. Antonelli e il piu giovane campione del mondo della storia moderna.",
            "excerpt": "Kimi Antonelli ha trasformato la pole in una splendida vittoria al Gran Premio degli Stati Uniti domenica, conquistando matematicamente il Mondiale di Formula 1 2026.",
            "body": [
                "Kimi Antonelli entra nella leggenda del motorsport domenica 25 ottobre, conquistando una travolgente vittoria dal semaforo alla bandiera a scacchi nel Gran Premio degli Stati Uniti per laurearsi ufficialmente campione del mondo di Formula 1 2026. Scattato dalla pole, il ventenne bolognese ha respinto l'attacco di Max Verstappen in Curva 1 gestendo con maturita esemplare la strategia a due soste nei 56 caldissimi giri del COTA. Tagliando il traguardo con 3.8 secondi su Charles Leclerc, ha fatto esplodere la festa nel box Mercedes.",
                "La certezza matematica del titolo iridato e arrivata con l'ottavo posto finale del compagno di squadra George Russell. Antonelli sale cosi a quota 365 punti nella classifica piloti, portando il proprio vantaggio a 123 lunghezze a fronte di soli 112 punti ancora a disposizione nelle ultime quattro gare. Verstappen sale sul gradino piu basso del podio precedendo Lewis Hamilton e Lando Norris."
            ]
        },
        "pl": {
            "title": "Antonelli mistrzem swiata Formuly 1 na COTA: Pierwszy tytul przypieczetowany w Austin",
            "subtitle": "Wloski debiutant wygrywa z pole position, a Russell konczy ósmy. Antonelli zostaje najmlodszym mistrzem swiata w historii.",
            "excerpt": "Kimi Antonelli odniosl bezdyskusyjne zwyciestwo w Grand Prix Stanow Zjednoczonych w niedziele, pieczetujac mistrzostwo swiata Formuly 1 na sezon 2026.",
            "body": [
                "Kimi Antonelli na stale wpisal sie do historii motorsportu w niedziele 25 pazdziernika, odnoszac triumf od startu do mety w Grand Prix Stanow Zjednoczonych i oficjalnie zdobywajac tytul mistrza swiata kierowcow F1 2026. Startujac z pole position, wloski talent obronil sie przed atakiem Maxa Verstappena i po bezblednej jezdzie na dwa pit-stopy zameldowal sie na mecie 3,8 sekundy przed Charlesem Leclerkiem z Ferrari.",
                "Matematyczne potwierdzenie tytulu przypieczetowal George Russell, ktory po starcie z szostego pola ukonczyl wyscig na osmym miejscu. Zmiana punktowa dała Antonellemu 365 punktow i niedoscigniona przewage 123 oczek przy zaledwie 112 punktach mozliwych do zdobycia w czterech ostatnich rundach. Verstappen uzupelnil podium na trzeciej lokacie przed Lewisem Hamiltonem i Lando Norrisem."
            ]
        },
        "zh": {
            "title": "安东内利在美洲赛道加冕F1世界冠军：奥斯汀站夺冠提前锁定首冠",
            "subtitle": "梅赛德斯超级新星杆位起跑一路领跑夺冠，拉塞尔名列第八助安东内利成为历史上最年轻的世界总冠军。",
            "excerpt": "基米·安东内利在周日的美国大奖赛正赛中以统治级表现将杆位转化为分站冠军，提前锁定2026赛季F1年度车手总冠军。",
            "body": [
                "基米·安东内利在10月25日周日将自己的名字镌刻在赛车运动的史册之中。他从杆位发车一路领跑赢得2026年F1美国大奖赛正赛胜利，正式提前加冕本赛季年度车手总冠军。在美洲赛道炎热的高温下，这位年轻的意大利车手在发车一号弯稳稳挡住维斯塔潘的进攻，随后完美执行了两停策略，最终以领先勒克莱尔3.8秒的优势冲过终点线，梅赛德斯车房瞬间陷入狂欢。",
                "随着唯一在理论上仍有争冠希望的队友拉塞尔在比赛中仅获得第八名，安东内利的个人积分攀升至365分，在赛季仅剩4站比赛（最多112分）的情况下建立起多达123分的不可逆优势。维斯塔潘为红牛收获季军，汉密尔顿与诺里斯分列第四和第五位。"
            ]
        },
        "ja": {
            "title": "アントネッリがCOTAでF1世界王者に輝く：オースティンで掴んだ初戴冠の栄光",
            "subtitle": "メルセデスの神童がポール発進から完勝、ラッセル8位でアントネッリが史上最年少のワールドチャンピオンへ。",
            "excerpt": "キミ・アントネッリが日曜のアメリカGPでポール・トゥ・ウィンを飾り、2026年F1ドライバーズ選手権タイトルを確定させました。",
            "body": [
                "キミ・アントネッリが10月25日日曜、モータースポーツの歴史にその名を刻みました。サーキット・オブ・ジ・アメリカズで行われたアメリカGPでポールポジションから終始レースを支配し、2026年F1ドライバーズ世界チャンピオンの栄冠を手にしました。ターン1でフェルスタッペンの猛攻を退けたイタリアの若武者は、猛暑下のCOTAで完璧な2ストップ戦略を完遂。ルクレールに3.8秒差をつけてトップチェッカーを受け、メルセデス陣営を歓喜の渦に巻き込みました。",
                "チームメイトで唯一逆転タイトルの可能性を残していたジョージ・ラッセルが8位に終わったことで、アントネッリは通算365ポイントに到達。残り4戦で獲得可能な最大112ポイントに対し123ポイントの大差を築き、王座決定となりました。3位にはフェルスタッペンが入り、ハミルトンとノリスがトップ5を占めました。"
            ]
        },
        "ko": {
            "title": "안토넬리 COTA에서 F1 월드 챔피언 등극: 오스틴 완승으로 생애 첫 타이틀 확정",
            "subtitle": "메르세데스 신성 폴투윈 질주, 러셀 8위 그치며 안토넬리 역대 최연소 F1 월드 챔피언 등극.",
            "excerpt": "키미 안토넬리가 일요일 미국 그랑프리에서 압도적인 폴투윈을 기록하며 2026년 F1 드라이버 월드 챔피언십 우승을 조기 확정 지었습니다.",
            "body": [
                "키미 안토넬리가 10월 25일 일요일 모터스포츠 역사에 새로운 금자탑을 쌓았습니다. 서킷 오브 디 아메리카스에서 열린 2026 F1 미국 그랑프리에서 폴포지션 출발 후 단 한 차례도 선두를 내주지 않고 완벽한 레이스를 펼치며 생애 첫 월드 챔피언 타이틀을 거머쥐었습니다. 1번 코너에서 베르스타펜의 거센 압박을 막아낸 안토넬리는 텍사스의 무더위 속에서도 노련한 투스톱 작전을 완수하며 샤를 르클레르를 3.8초 차로 제치고 가장 먼저 결승선을 통과했습니다.",
                "팀 동료이자 유일한 타이틀 경쟁자였던 조지 러셀이 8위에 머물면서 안토넬리는 365포인트를 확보, 잔여 4개 대회 최대 112포인트보다 많은 123포인트 차이로 챔피언십 우승을 조기에 확정했습니다. 베르스타펜이 3위로 포디엄에 올랐고 루이스 해밀턴과 랜도 노리스가 그 뒤를 이었습니다."
            ]
        },
        "ar": {
            "title": "انطونيلي يتوج بطلا للعالم في الفورمولا 1 بحلبة كوتا: حسم اللقب العالمي الاول في اوستن",
            "subtitle": "نجم مرسيدس الشاب ينتصر من الصدارة مع اكتفاء راسل بالمركز الثامن. انطونيلي يصبح اصغر بطل عالم في التاريخ الحديث.",
            "excerpt": "حول كيمي انطونيلي مركز الانطلاق الاول الى فوز كاسح بسباق جائزة الولايات المتحدة الكبرى يوم الاحد ليحسم رسميا لقب بطولة العالم لموسم 2026.",
            "body": [
                "خلد كيمي انطونيلي اسمه في سجلات رياضة المحركات يوم الاحد 25 اكتوبر، بتحقيقه انتصارا ساحقا من البداية حتى النهاية في جائزة الولايات المتحدة الكبرى ليتوج رسميا بلقب بطولة العالم لسائقي الفورمولا 1 لعام 2026. وانطلق النجم الايطالي الشاب من الصدارة وصمد بثبات امام هجوم ماكس فيرستابن عند المنعطف الاول قبل ان ينفذ استراتيجية توقفين ناجحة تحت شمس تكساس الحارقة، ليعبر خط النهاية متقدما بفارق 3.8 ثوان عن شارل لوكلير سائق فيراري وسط احتفالات هيستيرية في كراج مرسيدس.",
                "وجاء التأكيد الحسابي للقب بعد ان اكتفى منافسه الوحيد على اللقب وزميله في الفريق جورج راسل بالمركز الثامن. ورفع هذا الانتصار رصيد انطونيلي الى 365 نقطة ليوسع الفارق الى 123 نقطة مع تبقي 112 نقطة فقط في الجولات الاربع الاخيرة. واكمل فيرستابن منصة التتويج في المركز الثالث امام لويس هاميلتون ولاندو نوريس."
            ]
        }
    },
    "wnba-finals-2026-game5-preview-valkyries-host-dream-decider": {
        "fr": {
            "title": "Le match 5 des finales WNBA debarque dans la Baie : les Valkyries et le Dream s'affrontent pour le titre",
            "subtitle": "Egalite parfaite 2-2 alors que le Chase Center accueille l'ultime match decisif. Les Valkyries visent un sacre historique pour leur annee inaugurale.",
            "excerpt": "Les finales WNBA 2026 atteignent leur denouement ce lundi soir a San Francisco ou les Golden State Valkyries recoivent l'Atlanta Dream pour le match 5.",
            "body": [
                "Le chapitre le plus captivant de la saison de basketball 2026 s'ecrit ce lundi 26 octobre au Chase Center de San Francisco, theatre du cinquieme match decisif des finales WNBA entre les Golden State Valkyries et l'Atlanta Dream. A egalite 2-2 dans cette serie au meilleur des cinq manches, les Valkyries ne sont plus qu'a 40 minutes de parachever la saison inaugurale la plus spectaculaire de l'histoire du sport professionnel moderne.",
                "Golden State a arrache cette finale decisive grâce a une prestation defensive monumentale samedi soir a Atlanta (67-62). La strategie elaboree par l'entraineure Natalie Nakase a etouffe Angel Reese, reduite a 8 points grace a la vigilance sous les cercles de Kiah Stokes. Gabby Williams a porte l'attaque avec 17 points et 3 interceptions. Desormais de retour devant 18 000 spectateurs en furie, les Valkyries devront contenir le talent offensif de Rhyne Howard pour soulever le trophee de championnes WNBA."
            ]
        },
        "es": {
            "title": "El Juego 5 de las Finales WNBA llega a la Bahia: Valkyries y Dream se miden por el anillo",
            "subtitle": "Serie igualada 2-2 en el Chase Center para el duelo definitivo. La franquicia debutante de Golden State busca una gesta irrepetible.",
            "excerpt": "Las Finales de la WNBA 2026 alcanzan su momento culminante este lunes por la noche en San Francisco con el quinto juego entre Golden State Valkyries y Atlanta Dream.",
            "body": [
                "El capitulo mas vibrante del ano en el baloncesto se disputa este lunes 26 de octubre en el Chase Center de San Francisco, donde Golden State Valkyries y Atlanta Dream deciden el titulo de la WNBA en un Juego 5 a todo o nada. Con la serie empatada 2-2, el equipo de expansion esta a solo una victoria de completar la temporada de debut mas asombrosa en el deporte profesional frente a un Dream hambriento de gloria.",
                "Las Valkyries salvaron su temporada el sabado en Atlanta con una heroica victoria 67-62 basada en una defensa implacable. El plan tactico de Natalie Nakase y la proteccion de aro de Kiah Stokes dejaron a Angel Reese en apenas ocho puntos, frenando su racha de dobles-dobles. Gabby Williams comando el ataque con 17 unidades. Con un Chase Center repleto por 18,000 aficionados, Atlanta fiara sus opciones al acierto exterior de Rhyne Howard en una velada para la historia."
            ]
        },
        "de": {
            "title": "WNBA Finals Spiel 5 in San Francisco: Valkyries und Dream kaempfen um den Titel",
            "subtitle": "Alles ausgeglichen bei 2-2 vor dem Showdown im Chase Center. Expansion-Team Golden State greift nach historischer Meisterschaft.",
            "excerpt": "Die WNBA Finals 2026 erreichen am Montagabend ihren Hoehepunkt: Die Golden State Valkyries empfangen die Atlanta Dream zu Spiel 5 in San Francisco.",
            "body": [
                "Der packendste Moment der Basketballsaison 2026 steigt am Montagabend, den 26. Oktober, im ausverkauften Chase Center von San Francisco. Die Golden State Valkyries und die Atlanta Dream stehen sich im entscheidenden Spiel 5 der WNBA Finals gegenueber. Beim Serienstand von 2-2 trennen das neue Team der Valkyries nur noch 40 Minuten vom groessten Maerchen einer Debuetsaison im modernen Profisport.",
                "Golden State hatte das Aus am Samstagabend durch ein defensives Meisterstueck mit 67-62 in Atlanta abgewendet. Trainerin Natalie Nakase und Center Kiah Stokes nahmen Dream-Star Angel Reese komplett aus dem Spiel und hielten sie bei nur acht Zahelern. Gabby Williams ging mit 17 Punkten und 3 Steals voran. Vor heimischer Kulisse von ueber 18.000 Fans will Golden State nun den finalen Schritt zur Trophaee machen, waehrend Atlanta auf Rhyne Howard setzt."
            ]
        },
        "it": {
            "title": "WNBA Finals Gara 5 nella Bay Area: Valkyries e Dream all'ultimo atto per il titolo",
            "subtitle": "Serie sul 2-2 al Chase Center per la sfida decisiva. Le debuttanti Valkyries a un passo da una leggendaria impresa sportiva.",
            "excerpt": "Le WNBA Finals 2026 arrivano al verdetto finale questo lunedi sera a San Francisco dove le Golden State Valkyries ospitano l'Atlanta Dream per Gara 5.",
            "body": [
                "Il momento piu atteso della stagione cestistica va in scena lunedi 26 ottobre sul parquet del Chase Center di San Francisco. Le Golden State Valkyries e le Atlanta Dream si sfidano in una drammatica Gara 5 che vale il titolo delle WNBA Finals. Con la serie in perfetta parita sul 2-2, la neonata franchigia californiana ha la straordinaria opportunita di completare la stagione d'esordio piu trionfale dello sport moderno davanti al proprio pubblico.",
                "Le Valkyries hanno prolungato la contesa grazie alla monumentale prestazione difensiva di sabato ad Atlanta, imponendosi 67-62 in trasferta. La gabbia predisposta da coach Natalie Nakase e la marcatura di Kiah Stokes hanno annullato Angel Reese fermandola a soli 8 punti. Con Gabby Williams trascinatrice a quota 17 punti, il Chase Center sara una bolgia per sostenere l'attacco al titolo contro una pericolosa Atlanta trascinata da Rhyne Howard."
            ]
        },
        "pl": {
            "title": "Mecz numer 5 Finalow WNBA w San Francisco: Valkyries i Dream graja o zloty puchar",
            "subtitle": "Stan rywalizacji 2-2 przed decydujacym starciem w Chase Center. Debiutujace Valkyries moga przejsc do legendy sportu.",
            "excerpt": "Finaly WNBA 2026 osiagaja apogeum w poniedzialkowy wieczor w San Francisco, gdzie Golden State Valkyries podejma Atlanta Dream w meczu 5.",
            "body": [
                "Najbardziej emocjonujacy mecz koszykarskiego sezonu odbedzie sie w poniedzialek 26 pazdziernika w hali Chase Center w San Francisco. Golden State Valkyries i Atlanta Dream rozstrzygna losy tytulu mistrzowskiego w 5. meczu Finalow WNBA. Przy stanie 2-2 w serii nowo utworzony zespol Valkyries dziela zaledwie 40 minut od zapisania jednej z najbardziej niewiarygodnych kart w historii profesjonalnego sportu.",
                "Valkyries doprowadzily do decydujacego meczu dzieki wybitnemu wystepowi w defensywie w Atlancie, wygrywajac 67-62. Taktyka trenerki Natalie Nakase i pilnowanie strefy podkoszowej przez Kiah Stokes zatrzymaly Angel Reese na zaledwie 8 punktach. Gabby Williams poprowadzila atak zdobywajac 17 punktow. Wypelniona po brzegi hala w San Francisco czeka na pierwszy w historii tytul debiutujacej ekipy w starciu z grozna Rhyne Howard i Dream."
            ]
        },
        "zh": {
            "title": "WNBA总决赛抢五大战决胜旧金山：女武神与梦想直面终极荣耀",
            "subtitle": "总比分2-2重回大通中心打响抢五决战，新军金州女武神力争创造职业体育史无前例的首季夺冠奇迹。",
            "excerpt": "2026年WNBA总决赛在周一晚间迎来最高潮，金州女武神坐镇旧金山大通中心迎战亚特兰大梦想打响抢五生死战。",
            "body": [
                "2026年女子篮球赛场最震撼的篇章于10月26日周一晚间在大通中心翻开。金州女武神与亚特兰大梦想在WNBA总决赛第五场展开最终决战。在这轮五局三胜制的大战中两队战成2-2平，首年建队参赛的女武神距离完成现代职业体育史上最伟大的处子赛季奇迹仅剩40分钟的拼搏，而梦想全队同样渴望夺取队史首座总冠军奖杯。",
                "女武神在周六客场凭借坚如磐石的防守以67-62掀翻梦想将系列赛拖入决胜场。主教练中濑设计的高强度防守体系由斯托克斯坐镇内线，成功将梦想头号内线里斯限制在仅得8分，加比·威廉姆斯贡献全队最高的17分和3次抢断。今晚在超过18000名狂热主场球迷的助威声中，女武神将全力限制霍华德的突破，全力冲击队史首冠。"
            ]
        },
        "ja": {
            "title": "WNBAファイナル第5戦がベイエリアに到来：バルキリーズとドリームが栄冠をかけ激突",
            "subtitle": "2勝2敗で迎えるチェイス・センターの決戦。新興チームのバルキリーズが史上初のデビュー年制覇へ挑む。",
            "excerpt": "2026年のWNBAファイナルは月曜夜、チェイス・センターで最高潮へ。ゴールデンステイト・バルキリーズとアトランタ・ドリームが第5戦で激突します。",
            "body": [
                "2026年のバスケットボール界で最も注目を集める運命の戦いが10月26日月曜夜、満員のチェイス・センターで開幕します。ゴールデンステイト・バルキリーズとアトランタ・ドリームによるWNBAファイナル第5戦。2勝2敗の五分で迎えた決戦で、創設1年目のバルキリーズはプロスポーツ史に残るデビューイヤー初制覇まであと40分に迫りました。",
                "土曜夜の第4戦でバルキリーズは敵地で67-62の守備的勝利を掴み取り、崖っぷちから生還。中瀬ヘッドコーチの緻密な戦術とカイア・ストークスのインサイド奮闘により、ドリームのエンジェル・リースをわずか8点に抑え込みました。ギャビー・ウィリアムズが17得点で攻撃を牽引。1万8000人の大声援を背に、ライン・ハワード擁するアトランタを退けて栄光のトロフィーを掲げられるかが注目されます。"
            ]
        },
        "ko": {
            "title": "WNBA 파이널 최종 5차전 샌프란시스코 상륙: 발키리스와 드림의 끝장 승부",
            "subtitle": "2승 2패 팽팽한 균형 속 체이스 센터 격돌. 신생팀 골든스테이트 발키리스 역사상 첫 창단 첫해 우승 정조준.",
            "excerpt": "2026 WNBA 파이널이 월요일 밤 샌프란시스코 체이스 센터에서 마지막 5차전 단판 승부로 챔피언을 결정합니다.",
            "body": [
                "2026 여자 농구 최고의 하이라이트가 10월 26일 월요일 밤 샌프란시스코 체이스 센터에서 펼쳐집니다. 골든스테이트 발키리스와 애틀랜타 드림이 WNBA 파이널 최종 5차전에서 단 하나의 우승 트로피를 놓고 격돌합니다. 시리즈 전적 2승 2패로 맞선 가운데 창단 첫해를 맞이한 신생팀 발키리스는 홈팬들 앞에서 현대 프로 스포츠 역사상 유례없는 데뷔 시즌 우승 신화에 도전합니다.",
                "발키리스는 지난 토요일 애틀랜타 원정 4차전에서 67-62로 승리하며 기사회생했습니다. 나탈리 나카세 감독의 수비 전술과 카이아 스톡스의 골밑 봉쇄로 애틀랜타의 에이스 에인절 리스를 8득점으로 묶었고 개비 윌리엄스가 17득점 3스틸로 맹활약했습니다. 1만 8천여 홈팬들의 함성 속에 라인 하워드가 이끄는 애틀랜타의 화력을 막아내고 새 역사를 쓸 수 있을지 관심이 쏠립니다."
            ]
        },
        "ar": {
            "title": "المباراة الخامسة لنهائيات WNBA في سان فرانسيسكو: فالكيريز ودريم يتصارعان على الكأس",
            "subtitle": "تعادل السلسلة 2-2 قبل النزال الفاصل في تشيس سنتر. فالكيريز يطارد اول لقب في تاريخه خلال موسمه التدشيني.",
            "excerpt": "تصل نهائيات دوري كرة السلة الامريكي للسيدات WNBA الى لحظة الحسم مساء الاثنين في سان فرانسيسكو بالمباراة الخامسة بين فالكيريز ودريم.",
            "body": [
                "يفتح مسرح تشيس سنتر في سان فرانسيسكو ابوابه مساء الاثنين 26 اكتوبر لاحتضان اهم مواجهات كرة السلة في عام 2026، حيث يلتقي غولدن ستيت فالكيريز مع اتلانتا دريم في المباراة الخامسة والفاصلة لنهائيات WNBA. ومع تعادل الطرفين 2-2 في السلسلة، تقف كتيبة فالكيريز على بعد 40 دقيقة فقط من تحقيق اعظم انجاز لفريق في موسمه الاول بتاريخ الرياضة الحديثة.",
                "وكان فالكيريز قد اعاد السلسلة للحياة بفوز دفاعي شاق 67-62 مساء السبت في اتلانتا بفضل الخطة التكتيكية للمدربة ناتالي ناكاسي وتألق كيا ستوكس في تقييد حركة انجل ريس لتسجل 8 نقاط فقط. وقادت غابي ويليامز الهجوم برصيد 17 نقطة و3 خطفات. وامام 18 الف مشجع في سان فرانسيسكو، ستكون المواجهة على اشدها امام راين هاوارد وكتيبة دريم لحسم هوية البطل."
            ]
        }
    },
    "pga-tour-bermuda-smotherman-defeats-power-playoff-port-royal-2026": {
        "fr": {
            "title": "Smotherman terrasse Power en playoff aux Bermudes : deuxieme succes en un mois",
            "subtitle": "L'Americain s'impose au troisieme trou de barrage pour priver l'ancien champion du trophee. Le vent a dicte sa loi a Port Royal.",
            "excerpt": "Austin Smotherman a battu Seamus Power au troisieme trou de playoff a Port Royal pour remporter le Butterfield Bermuda Championship lundi.",
            "body": [
                "Austin Smotherman a confirme son statut d'homme en forme du circuit PGA ce lundi matin en s'adjugeant le Butterfield Bermuda Championship au terme d'un barrage haletant face a l'Irlandais Seamus Power a Port Royal. Apres des vents tempetueux a plus de 60 km/h ayant fige la marque apres 54 trous sur une egalite parfaite a 16 sous le par (197), les organisateurs ont lance un playoff palpitant.",
                "Les deux golfeurs ont partage les deux premiers trous de barrage avec des pars autoritaires. C'est sur le redoutable par 3 du trou 16 dominant l'Atlantique que la decision s'est faite : Power a manque le green sur la gauche pour conceder un bogey tandis que Smotherman assurait deux putts pour signer le par de la victoire. Il empoche 1,08 million de dollars et son deuxieme titre en trois semaines apres l'Open de l'Utah."
            ]
        },
        "es": {
            "title": "Smotherman supera a Power en el desempate de Bermudas: segundo titulo en un mes",
            "subtitle": "El estadounidense emboca el par en el tercer hoyo extra y niega la corona al ex campeon tras el temporal en Port Royal.",
            "excerpt": "Austin Smotherman vencio a Seamus Power en el tercer hoyo de desempate en Port Royal para proclamarse campeon del Butterfield Bermuda Championship.",
            "body": [
                "Austin Smotherman se consagro como el golfista mas efectivo del otono en el PGA Tour este lunes al conquistar el Butterfield Bermuda Championship en un apasionante desempate ante el irlandes Seamus Power en Port Royal Golf Course. Con vientos superiores a 60 km/h que obligaron a reducir el evento a 54 hoyos con ambos igualados en 16 bajo par (197), la resolucion se vivio en los hoyos costeros.",
                "Tras igualar con pares en los dos primeros hoyos de desempate, la gloria llego en el espectacular par 3 del hoyo 16 sobre el oceano. Power se desvio al rough izquierdo y solo pudo salvar el bogey, permitiendo a Smotherman asegurar dos putts tranquilos para el par decisivo. El californiano se lleva 1.08 millones de dolares y suma su segundo trofeo en tres semanas tras ganar en Utah."
            ]
        },
        "de": {
            "title": "Smotherman bezwingt Power im Bermuda-Stechen: Zweiter PGA-Tour-Titel innerhalb eines Monats",
            "subtitle": "US-Profi sichert sich am dritten Extraloch mit Par den Sieg gegen den Ex-Champion nach windbedingtem 54-Loch-Finish.",
            "excerpt": "Austin Smotherman hat Seamus Power am dritten Playoff-Loch in Port Royal geschlagen und die Butterfield Bermuda Championship am Montag gewonnen.",
            "body": [
                "Austin Smotherman untermauerte am Montagmorgen seinen Ruf als Formspieler des Herbstes auf der PGA Tour: Im dramatischen Stechen auf dem Port Royal Golf Course bezwang er den Iren Seamus Power und sicherte sich den Titel bei der Butterfield Bermuda Championship. Nachdem Windboeen von ueber 60 km/h eine Wertung nach 54 Loechern bei Gleichstand von 16 unter Par (197) erzwungen hatten, fiel die Entscheidung im Playoff.",
                "Beide Spieler lochten an den ersten beiden Extraloechern zum Par. Am legendaeren Par-3 der 16 ueber dem Atlantik fiel die Entscheidung: Power verzog seinen Abschlag ins dichte Rough und kassierte ein Bogey, waehrend Smotherman mit zwei souveraenen Putts zum Par einlochte. Neben 1,08 Millionen Dollar Preisgeld und 500 FedExCup-Punkten feiert Smotherman seinen zweiten Triumph nach dem Sieg in Utah."
            ]
        },
        "it": {
            "title": "Smotherman piega Power al playoff a Bermuda: secondo successo sul PGA Tour in un mese",
            "subtitle": "Lo statunitense chiude con il par alla terza buca supplementare per battere l'ex campione sul percorso di Port Royal.",
            "excerpt": "Austin Smotherman ha sconfitto Seamus Power alla terza buca di playoff a Port Royal aggiudicandosi il Butterfield Bermuda Championship lunedi.",
            "body": [
                "Austin Smotherman e il protagonista assoluto dell'autunno sul PGA Tour: lunedi mattina ha conquistato il Butterfield Bermuda Championship superando l'irlandese Seamus Power in un playoff al cardiopalma a Port Royal. Con raffiche di vento oceanico oltre i 60 km/h che hanno imposto la chiusura dopo 54 buche con entrambi i giocatori appaiati a quota 16 sotto il par (197), il titolo e stato assegnato alle buche supplementari.",
                "Dopo due buche pareggiate con solidi par, lo spareggio si e deciso sulla spettacolare buca 16, un par 3 affacciato sull'Atlantico. Power ha mancato il green a sinistra terminando in bogey, aprendo la strada a Smotherman che con due putt chirurgici ha siglato il par del trionfo. Per il 31enne californiano arrivano 1.08 milioni di dollari e il secondo successo dopo il Bank of Utah Championship."
            ]
        },
        "pl": {
            "title": "Smotherman pokonuje Powera w dogrywce na Bermudach: Drugi puchar PGA Tour w miesiac",
            "subtitle": "Amerykanin wbija decydujacego para na trzecim dodatkowym dolku i odbiera puchar bylemu mistrzowi w Port Royal.",
            "excerpt": "Austin Smotherman pokonal Seamusa Powera na trzecim dolku dogrywki w Port Royal i siegnal po tytul Butterfield Bermuda Championship w poniedzialek.",
            "body": [
                "Austin Smotherman potwierdzil fantastyczna forme na finiszu sezonu PGA Tour, wygrywajac w poniedzialek rano turniej Butterfield Bermuda Championship po zaciętej dogrywce z Irlandczykiem Seamusem Powerem na polu Port Royal. Porywisty wiatr znad Atlantyku przekraczajacy 60 km/h wymusil zakonczenie rywalizacji zasadniczej po 54 dolkach przy remisie obu golfistow na poziomie 16 ponizej par (197).",
                "Po dwoch dolkach remisowych z parami rozstrzygniecie nadeszlo na spektakularnym dolku 16 z widokiem na ocean. Power spudlowal tee shot w lewe gestwiny i uratowal zaledwie bogeya, co dalo Smothermanowi szanse na spokojnego dwu-putta po zwycieskiego para. Triumf przyniosl Amerykaninowi 1,08 miliona dolarow i drugi puchar w odstepie zaledwie trzech tygodni od wygranej w Utah."
            ]
        },
        "zh": {
            "title": "斯莫瑟曼延长赛绝杀鲍尔问鼎百慕大：一个月内豪取美巡赛两连冠",
            "subtitle": "美国球手在第3个加洞保帕成功阻击前赛会冠军，大风天气造就皇家港史诗级决战。",
            "excerpt": "奥斯汀·斯莫瑟曼在皇家港高尔夫球场通过三个加洞的残酷较量击败爱尔兰名将鲍尔，周一成功捧得百慕大锦标赛冠军奖杯。",
            "body": [
                "奥斯汀·斯莫瑟曼在10月26日周一上午展现了火热的竞技状态。他在皇家港高尔夫球场展开的延长赛中击败爱尔兰名将谢默斯·鲍尔，斩获2026年百慕大锦标赛冠军。受大西洋沿岸时速超过40英里的强风影响，比赛在打完54洞且两人同为低于标准杆16杆（197杆）后进入突然死亡加洞赛。",
                "前两个加洞两人均稳稳保帕。决胜时刻在标志性的海滨16号三杆洞上演：鲍尔开球偏左落入深草吞下柏忌，而斯莫瑟曼两推稳稳保帕一锤定音。31岁的斯莫瑟曼斩获108万美元冠军奖金和500个联邦快递杯秋季积分，继三周前在犹他夺魁后一个月内两度捧杯，世界排名挺进前40位。"
            ]
        },
        "ja": {
            "title": "スモーザーマンがプレーオフでパワーを撃破：バミューダ選手権で今月ツアー2勝目",
            "subtitle": "米国の実力者が延長3ホール目の16番でパーをセーブし前年王者を下す。暴風のポートロイヤルで劇的決着。",
            "excerpt": "オースティン・スモーザーマンがポートロイヤルでのプレーオフ3ホール目でシェーマス・パワーを下し、バターフィールド・バミューダ選手権を制覇しました。",
            "body": [
                "オースティン・スモーザーマンが秋のPGAツアーで破竹の勢いを見せています。月曜朝に行われたバターフィールド・バミューダ選手権のプレーオフで、アイルランドのシェーマス・パワーを破り優勝を飾りました。大西洋からの時速60キロを超える暴風により54ホール終了時点で通算16アンダー（197打）の同スコアとなり、サドンデス決戦へともつれ込みました。",
                "最初の2ホールを互いにパーで分けた後、名物の海越え16番パー3で勝負が決しました。パワーがティーショットを左の深いラフに入れてボギーとしたのに対し、スモーザーマンは冷静に2パットでパーを沈めて歓喜の雄叫びを上げました。優勝賞金108万ドルを獲得し、ユタ選手権に続く1カ月で2勝目を達成しました。"
            ]
        },
        "ko": {
            "title": "스모더먼 연장 접전 끝에 파워 꺾고 버뮤다 챔피언십 우승: 한 달 새 투어 2승 쾌거",
            "subtitle": "미국의 스모더먼 3번째 연장 홀에서 침착하게 파 세이브하며 전 챔피언 제압. 강풍 속 포트 로열 명승부 연출.",
            "excerpt": "오스틴 스모더먼이 포트 로열 골프코스 연장 3번째 홀에서 셰이머스 파워를 꺾고 버터필드 버뮤다 챔피언십 우승컵을 들어 올렸습니다.",
            "body": [
                "오스틴 스모더먼이 10월 26일 월요일 오전 PGA 투어 가을 시리즈 최고의 주인공으로 우뚝 섰습니다. 버뮤다 사우샘프턴의 포트 로열 골프코스에서 치러진 버터필드 버뮤다 챔피언십 연장전에서 아일랜드의 강호 셰이머스 파워를 제압하고 트로피를 차지했습니다. 시속 60km가 넘는 대서양 돌풍으로 54홀 16언더파 동타 상태에서 열린 서든데스 승부였습니다.",
                "앞선 두 차례 연장 홀을 파로 비긴 두 선수의 희비는 바다를 넘겨야 하는 16번 홀(파3)에서 엇갈렸습니다. 파워의 티샷이 왼쪽 러프에 빠지며 보기에 그친 반면 스모더먼은 안전하게 투퍼트로 파를 기록하며 우승을 확정했습니다. 스모더먼은 108만 달러의 상금과 함께 3주 전 유타 대회에 이어 한 달 만에 투어 2승을 수확했습니다."
            ]
        },
        "ar": {
            "title": "سموثيرمان يقهر باور في تمايز برمودا المثير: ثاني القابه في جولة PGA خلال شهر",
            "subtitle": "الامريكي يسجل البار في الحفرة الثالثة الاضافية ليحرم البطل السابق من اللقب بعد عاصفة بورت رويال.",
            "excerpt": "تغلب اوستن سموثيرمان على شيموس باور في ثالث حفرة فاصلة بملعب بورت رويال ليتوج بلقب بطولة برمودا للغولف يوم الاثنين.",
            "body": [
                "ثبت اوستن سموثيرمان اقدامه كابرز نجوم الخريف في جولة PGA الامريكية صباح الاثنين، باحرازه لقب بطولة برمودا للغولف بعد مواجهة فاصلة ملحمية ضد الايرلندي شيموس باور في ملعب بورت رويال. وجاء اللجوء للتمايز بعد ان تسببت رياح عاتية تخطت سرعتها 60 كم/ساعة في تقليص المنافسات الى 54 حفرة مع تعادل الثنائي عند 16 ضربة تحت المعدل (197).",
                "وبعد التعادل بالبار في اول حفرتين، حسمت الحفرة 16 الساحلية الشهيرة الموقف حين سقطت ضربة باور في العشب الكثيف مسجلا بوجي، بينما تعامل سموثيرمان بهدوء وسجل ضربتي بوت ليحصد البار واللقب. ونال سموثيرمان جائزة المركز الاول البالغة 1.08 مليون دولار ليضيف بطولته الثانية في ثلاثة اسابيع بعد فوزه ببطولة يوتا."
            ]
        }
    },
    "nfl-week7-sunday-carnage-chiefs-49ers-fall-vikings-alone-unbeaten-2026": {
        "fr": {
            "title": "Dimanche de seisme en NFL : les Seahawks font tomber les Chiefs, les 49ers terrasses par Atlanta",
            "subtitle": "La defense de Seattle etouffe Mahomes 20-3 lors du choc de dimanche soir. Minnesota s'impose pour rester la seule equipe a 6-0.",
            "excerpt": "Un dimanche fou en 7e semaine de NFL a vu Kansas City et San Francisco subir leur premiere defaite, laissant les Vikings seuls invaincus a 6-0.",
            "body": [
                "La hierarchie de la NFL a vacille ce dimanche 25 octobre avec la chute simultanee des deux derniers invaincus de la ligue. La sensation majeure s'est produite lors du Sunday Night Football au Lumen Field, ou les Seattle Seahawks ont etouffe les Kansas City Chiefs 20-3 grace a une prestation defensive d'anthologie. Pour la premiere fois depuis plus de deux ans, Patrick Mahomes a ete prive du moindre touchdown, subissant quatre sacks et deux pertes de balle sous les rugissements du public de Seattle.",
                "Plus tot dans l'apres-midi a Atlanta, les San Francisco 49ers (6-1) ont egalement vu leur invincibilite prendre fin face aux Falcons (29-20). La pression agressive d'Atlanta a fait plier Brock Purdy, intercepte au quatrieme quart-temps. Pendant ce temps, les Minnesota Vikings ont souffert mais se sont imposes 16-10 contre les Colts d'Indianapolis pour porter leur fiche a 6-0 et s'isoler au sommet de la NFL. La semaine se conclut ce lundi avec le duel Cowboys-Eagles."
            ]
        },
        "es": {
            "title": "Domingo de terremoto en la NFL: Seahawks noquean a Chiefs, Falcons sorprenden a 49ers y Vikings mandan solos con 6-0",
            "subtitle": "La defensa de Seattle seca a Mahomes 20-3 en el SNF. Minnesota supera a Colts para ser el unico equipo invicto de la liga.",
            "excerpt": "Una vibrante Semana 7 dejo las primeras derrotas de Kansas City y San Francisco, encumbrando a los Vikings como los unicos invictos de la NFL.",
            "body": [
                "El orden establecido en la NFL salto por los aires este domingo 25 de octubre con la caida de los dos colosos invictos. El golpe mas rotundo llego en el Sunday Night Football en Lumen Field, donde los Seattle Seahawks dictaron una catedra defensiva para desarbolar a los Kansas City Chiefs por 20-3. Patrick Mahomes se quedo sin anotar un solo touchdown por primera vez en mas de dos anos, sufriendo cuatro capturas y dos entregas ante la atronadora aficion local.",
                "Horas antes en Atlanta, los San Francisco 49ers (6-1) tambien perdieron su marcha perfecta al sucumbir 29-20 frente a unos inspirados Falcons, cuya presion defensiva capturo a Brock Purdy en cuatro ocasiones. Entretanto, los Minnesota Vikings batallaron para superar 16-10 a los Indianapolis Colts y alcanzar una foja de 6-0, quedando como el unico conjunto invicto de toda la NFL antes del choque de lunes por la noche entre Cowboys y Eagles."
            ]
        },
        "de": {
            "title": "Erdbeben am NFL-Sonntag: Seahawks zerlegen Chiefs, Falcons stoppen 49ers, Vikings nun allein bei 6-0",
            "subtitle": "Seattles Defense laehmt Mahomes mit 20-3 im Sunday Night Football. Minnesota feiert sechsten Sieg und bleibt als einziges Team ungeschlagen.",
            "excerpt": "Ein historischer 7. Spieltag brachte die ersten Saisonniederlagen fuer Kansas City und San Francisco, waehrend die Vikings bei 6-0 thronen.",
            "body": [
                "Die Machtverhaeltnisse in der NFL wurden am Sonntag, den 25. Oktober, gehoerig durcheinandergewirbelt: Beide verbliebenen ungeschlagenen Schwergewichte stuerzten in der Fremde. Die groesste Sensation ereignete sich zur Prime Time im Lumen Field, wo die Seattle Seahawks die Kansas City Chiefs mit 20-3 demuetigten. Seattles Defensive erstickte die Offensive um Patrick Mahomes vollstaendig, ließ keinen einzigen Touchdown zu und erzwang vier Sacks sowie zwei Ballverluste.",
                "Bereits am Nachmittag hatte es die San Francisco 49ers (6-1) erwischt, die bei den Atlanta Falcons mit 20-29 unterlagen. Atlantas Pass-Rush setzte Brock Purdy unter Dauerdruck und forcierte eine vorentscheidende Interception im Schlussviertel. Die lachenden Gewinner des Wochenendes sind die Minnesota Vikings, die sich mit 16-10 gegen die Colts durchsetzten und nun mit 6-0 das einzige noch unbesiegte Team der Liga stellen, bevor die Cowboys bei den Eagles gastieren."
            ]
        },
        "it": {
            "title": "Domenica di ribaltoni in NFL: i Seahawks travolgono i Chiefs, i Falcons battono i 49ers e i Vikings volano soli a 6-0",
            "subtitle": "La difesa di Seattle annulla Mahomes per 20-3 nel SNF. Minnesota batte i Colts e resta l'unica franchigia a punteggio pieno.",
            "excerpt": "Una clamorosa Week 7 NFL ha visto cadere sia Kansas City che San Francisco, lasciando i Minnesota Vikings come unica squadra imbattuta a quota 6-0.",
            "body": [
                "Gli equilibri della NFL sono stati sconvolti domenica 25 ottobre con la contemporanea caduta delle due corazzate imbattute. La sorpresa piu clamorosa e arrivata nel Sunday Night Football al Lumen Field, dove i Seattle Seahawks hanno dominato i Kansas City Chiefs con un netto 20-3. La difesa di Seattle ha lasciato Patrick Mahomes senza touchdown per la prima volta in oltre due anni, mettendolo a terra quattro volte e forzando due palle perse.",
                "Nel pomeriggio ad Atlanta anche i San Francisco 49ers (6-1) avevano dovuto incassare il primo stop stagionale, sconfitti 29-20 dai Falcons a causa di una pressione asfissiante su Brock Purdy. Ne approfittano i Minnesota Vikings che, superando 16-10 gli Indianapolis Colts, salgono a 6-0 restando l'unica squadra ancora imbattuta dell'intera lega prima del Monday Night Football tra Cowboys ed Eagles."
            ]
        },
        "pl": {
            "title": "Niedziela sensacji w NFL: Seahawks ucieraja nosa Chiefs, Falcons pokonuja 49ers, Vikings jedynymi niepokonanymi z 6-0",
            "subtitle": "Obrona Seattle zatrzymuje Mahomesa na 20-3 w niedzielnym hicie. Minnesota pokonuje Colts i zostaje sama z bilansem 6-0.",
            "excerpt": "Szalona 7. kolejka NFL przyniosla pierwsze porazki Kansas City i San Francisco, pozostawiajac Minnesote Vikings jako jedyna niepokonana druzyne w lidze.",
            "body": [
                "Hierarchia w lidze NFL zatrzesla sie w posadach w niedziele 25 pazdziernika, gdy obaj dotychczasowi liderzy doznali pierwszych porazek w sezonie. Najwiekszy szok przezyli kibice w Lumen Field podczas Sunday Night Football, gdzie Seattle Seahawks rozbili mistrzow Kansas City Chiefs 20-3. Defensywa gospodarzy nie pozwolila Patrickowi Mahomesowi na ani jedno przylozenie, zaliczajac cztery sacki i dwa przechwyty.",
                "Wczesniej w Atlancie San Francisco 49ers (6-1) ulegli Falcons 20-29 pod wplywem nieustannej presji na Brocka Purdy'ego. Z kolei Minnesota Vikings wygrali zaciety mecz z Indianapolis Colts 16-10 i z bilansem 6-0 sa jedynym zespolem w calej lidze bez zadnej porazki na koncie przed poniedzialkowym hitem Cowboys kontra Eagles."
            ]
        },
        "zh": {
            "title": "NFL第7周超级冷门日：海鹰20-3掀翻酋长，猎鹰终结49人全胜，维京人6胜0负独占鳌头",
            "subtitle": "西雅图铜墙铁壁让马霍姆斯吞下尴尬零达阵。明尼苏达击退小马成为全联盟唯一不败球队。",
            "excerpt": "NFL第7周超级周日诞生大变局，酋长与49人双双遭遇赛季首败，6胜0负的维京人成为联盟唯一的全胜独苗。",
            "body": [
                "2026年NFL常规赛的格局在10月25日周日被彻底打破，此前保持全胜的两大超级热门双双在客场折戟。最大的冷门发生在流明球场的周日夜赛焦点战，西雅图海鹰凭借现象级的防守表现以20-3彻底封锁堪萨斯城酋长。西雅图防线全场4次擒杀马霍姆斯并制造两次球权转换，让卫冕冠军两年来首次整场没有达阵入账。",
                "在此之前，旧金山49人（6胜1负）在亚特兰大客场以20-29爆冷不敌猎鹰，普尔迪在第四节遭遇致命抄截。与此同时，明尼苏达维京人在主场有惊无险地以16-10击败印第安纳波利斯小马，开季豪取6连胜，成为全美职业橄榄球大联盟唯一未尝败绩的球队。第7周的收官大戏将在今晚由牛仔客战老鹰上演。"
            ]
        },
        "ja": {
            "title": "NFL第7週波乱のサンデー：シーホークスがチーフスを20-3撃破、49ersも陥落しバイキングスが単独全勝へ",
            "subtitle": "シアトル鉄壁の守備がマホームズを無TDに封じる完勝劇。ミネソタがコルツを下し6勝0敗でリーグ唯一の無敗に君臨。",
            "excerpt": "NFL第7週の日曜日はチーフスと49ersが揃って初黒星を喫し、6勝無敗のバイキングスがリーグ唯一の全勝チームとなりました。",
            "body": [
                "NFLの勢力図が10月25日日曜日、劇的な波乱によって塗り替えられました。開幕全勝を誇っていた2強が揃って敵地で苦杯をなめました。最大の衝撃はルーメン・フィールドでのサンデーナイト・フットボール。シアトル・シーホークスが王者カンザスシティ・チーフスを20-3で圧倒しました。シアトル守備陣はマホームズを4サック2ターンオーバーに追い込み、2年ぶりとなるチーム無タッチダウンに封じ込めました。",
                "日中にはサンフランシスコ・49ers（6勝1敗）もアトランタ・ファルコンズに20-29で敗戦。ブロック・パーディが激しいパスラッシュに苦しみました。その一方でミネソタ・バイキングスはコルツを16-10で退けて開幕6連勝を達成。全米唯一の無敗チームとして単独首位に立ち、今夜のカウボーイズ対イーグルス戦を迎えます。"
            ]
        },
        "ko": {
            "title": "NFL 7주 차 대이변의 일요일: 시호크스 치프스 20-3 완파, 49ers 침몰 속 바이킹스 6연승 독주",
            "subtitle": "시애틀 철벽 수비 머홈스 무터치다운 봉쇄. 미네소타 콜츠 꺾고 리그 유일 6승 무패 팀 등극.",
            "excerpt": "NFL 7주 차 일요일 캔자스시티와 샌프란시스코가 나란히 시즌 첫 패배를 당하며 6승 무패의 미네소타 바이킹스가 유일한 무패 팀으로 남았습니다.",
            "body": [
                "2026 NFL 정규시즌 판도가 10월 25일 일요일 대이변으로 요동쳤습니다. 개막 후 무패를 달리던 최강 2개 구단이 원정에서 나란히 덜미를 잡혔습니다. 최고의 충격은 루멘 필드에서 열린 선데이 나이트 풋볼이었습니다. 시애틀 시호크스가 패트릭 머홈스의 캔자스시티 치프스를 20-3으로 완파했습니다. 시애틀 수비는 머홈스를 상대로 색 4개와 턴오버 2개를 뺏어내며 2년여 만에 상대 무터치다운 굴욕을 안겼습니다.",
                "앞서 열린 경기에서는 샌프란시스코 49ers(6승 1패)도 애틀랜타 팰컨스에 20-29로 패했습니다. 반면 미네소타 바이킹스는 인디애나폴리스 콜츠를 16-10으로 제압하고 개막 6연승을 질주, NFL 32개 구단 중 유일한 무패 팀으로 우뚝 섰습니다. 7주 차 일정은 오늘 밤 필라델피아에서 열리는 카우보이스와 이글스의 맞대결로 마무리됩니다."
            ]
        },
        "ar": {
            "title": "زلزال الاحد في دوري NFL: سيهوكس يسقط تشييفس 20-3 وفالكونز يقهر 49ers والفايكنغز ينفرد بالصدارة",
            "subtitle": "دفاع سياتل يحرم ماهومز من اي تاتش داون في قمة الاحد. مينيسوتا ترفع رصيدها الى 6-0 لتصبح الفريق الوحيد الخالي من الهزائم.",
            "excerpt": "شهد الاسبوع السابع من دوري كرة القدم الامريكية سقوط حامل اللقب كانساس سيتي وسان فرانسيسكو ليبقى مينيسوتا فايكنغز منفردا بـ6 انتصارات متتالية.",
            "body": [
                "انقلبت موازين القوى في دوري NFL يوم الاحد 25 اكتوبر بسقوط الفريقين الوحيدين اللذين لم يتذوقا طعم الهزيمة خارج ملعبهما. وجاءت المفاجأة المدوية في سهرة الاحد على ملعب لومن فيلد، حين قدم سياتل سيهوكس ملحمة دفاعية تاريخية ليكتسح كانساس سيتي تشييفس بنتيجة 20-3. ونجح دفاع سياتل في حرمان باتريك ماهومز من تسجيل اي هدف للمرة الاولى منذ اكثر من عامين مسجلا 4 اسقاطات وتسبب بخطف كرتين.",
                "وفي مباريات الظهيرة، تلقى سان فرانسيسكو 49ers (6-1) خسارته الاولى بسقوطه امام اتلانتا فالكونز 20-29 تحت ضغط هجومي شرس على بروك بيردي. وفي المقابل، نجا مينيسوتا فايكنغز بفوز ثمين 16-10 على انديانابوليس كولتس ليرفع رصيده الى 6-0 وينفرد بصدارة الدوري دون اي تعثر قبل مواجهة كاوبويز وايغلز في ختام الجولة."
            ]
        }
    },
    "premier-league-mw8-bournemouth-stun-man-united-old-trafford-liverpool-2026": {
        "fr": {
            "title": "Bournemouth terrasse Manchester United 3-0 a Old Trafford : Liverpool bat Brighton en cloture de la 8e journee",
            "subtitle": "Les Cherries punissent les Red Devils avec un realisme clinique. Liverpool grimpe sur le podium a deux longueurs du duo de tete.",
            "excerpt": "L'AFC Bournemouth a cree la sensation dimanche en infligeant un 3-0 a Manchester United a Old Trafford tandis que Liverpool s'imposait 2-0 face a Brighton.",
            "body": [
                "L'AFC Bournemouth a livre une veritable demonstration tactique a Old Trafford ce dimanche 25 octobre en surclassant Manchester United 3-0 devant un public meduse. Les hommes d'Andoni Iraola ont profite des failles defensives mancuniennes des la premiere periode grace a une frappe rasee de Rayan a la 37e minute suivie d'une conclusion limpide de Marcus Tavernier a la 42e.",
                "Incapables de reagir apres la pause, les Red Devils ont encaisse un troisieme but en fin de match signe Ryan Christie en contre-attaque. Cette defaite releve Manchester United au dixieme rang (10 points) tandis que Bournemouth s'invite dans le top six avec 13 points. Plus tard a Anfield, Liverpool a maitrise Brighton 2-0 grace a un contre son camp de Gross et un but d'Alexander Isak, permettant aux Reds de se hisser a la troisieme place avec 15 points derriere Manchester City et Arsenal (21 points)."
            ]
        },
        "es": {
            "title": "Bournemouth golea 3-0 al Manchester United en Old Trafford: Liverpool bate a Brighton en el cierre de la jornada 8",
            "subtitle": "Los Cherries castigan a los locales con pegada letal. Liverpool escala al tercer puesto con su victoria 2-0.",
            "excerpt": "El AFC Bournemouth sonrojo al Manchester United con un contundente 3-0 en Old Trafford el domingo, mientras Liverpool supero 2-0 a Brighton para cerrar la jornada.",
            "body": [
                "El AFC Bournemouth firmo una exhibicion historica en Old Trafford este domingo 25 de octubre al imponerse por 3-0 a un desdibujado Manchester United. El cuadro dirigido por Andoni Iraola desarticulo a los locales antes del descanso gracias al tanto inicial de Rayan en el minuto 37 y al gol de Marcus Tavernier en el 42 tras una brillante transicion.",
                "Pese al dominio territorial del United en el complemento, Ryan Christie puso la puntilla en el descuento culminando un contraataque fulgurante. Con esta derrota el United cae al decimo puesto con 10 puntos, mientras Bournemouth asciende al sexto lugar con 13. En Anfield, Liverpool derroto 2-0 a Brighton con gol en propia puerta de Gross y acierto de Alexander Isak, escalando al tercer escalon con 15 puntos a la caza de City y Arsenal (21)."
            ]
        },
        "de": {
            "title": "Bournemouth fegt Manchester United 3-0 im Old Trafford vom Platz: Liverpool schlaegt Brighton zum Abschluss des 8. Spieltags",
            "subtitle": "Cherries bestrafen fehlerhafte Red Devils eiskalt. Liverpool klettert nach 2-0-Erfolg auf Rang drei hinter City und Arsenal.",
            "excerpt": "Der AFC Bournemouth feierte am Sonntag einen sensationellen 3-0-Auswaertssieg bei Manchester United, waehrend Liverpool Brighton mit 2-0 bezwang.",
            "body": [
                "Der AFC Bournemouth sorgte am Sonntag, den 25. Oktober, fuer das dickste Ausrufezeichen des Wochenendes und fertigte Manchester United im altehrwuerdigen Old Trafford mit 3-0 ab. Die taktisch perfekt eingestellte Mannschaft von Andoni Iraola nutzte die Unruhe der Gastgeber vor der Pause eiskalt aus: Rayan traf in der 37. Minute zur Fuehrung, ehe Marcus Tavernier fuenf Minuten spaeter auf 2-0 erhoehte.",
                "In der Nachspielzeit setzte Ryan Christie nach einem Konter den Schlusspunkt zum 3-0-Endstand. United rutscht mit 10 Punkten auf Platz zehn ab, waehrend Bournemouth mit 13 Punkten gleichzieht mit Chelsea. Im spaeteren Sonntagsspiel siegte Liverpool durch ein Eigentor von Gross und einen Treffer von Alexander Isak mit 2-0 gegen Brighton und sprang mit 15 Punkten auf Rang drei hinter das fuehrende Duo City und Arsenal (21 Punkte)."
            ]
        },
        "it": {
            "title": "Il Bournemouth asfalta il Manchester United 3-0 a Old Trafford: il Liverpool batte il Brighton in chiusura di 8a giornata",
            "subtitle": "I Cherries puniscono i Red Devils con un cinismo spietato. Il Liverpool sale al terzo posto grazie al 2-0 sui Seagulls.",
            "excerpt": "L'AFC Bournemouth ha dominato il Manchester United imponendosi 3-0 a Old Trafford domenica mentre il Liverpool ha battuto 2-0 il Brighton.",
            "body": [
                "L'AFC Bournemouth ha firmato un'impresa straordinaria a Old Trafford domenica 25 ottobre travolgendo il Manchester United per 3-0 davanti a uno stadio attonito. La formazione di Andoni Iraola ha colpito due volte prima dell'intervallo con il vantaggio siglato da Rayan al 37° e il raddoppio fulmineo di Marcus Tavernier al 42° su azione di rimessa.",
                "Nella ripresa lo United non ha trovato varchi nella retroguardia ospite e al 92° Ryan Christie ha chiuso definitivamente i conti in contropiede. I Red Devils precipitano al decimo posto con 10 punti, mentre il Bournemouth sale a 13. Ad Anfield il Liverpool ha liquidato il Brighton per 2-0 con autogol di Gross e rete di Alexander Isak, issandosi al terzo posto con 15 punti dietro al duo di testa City e Arsenal (21 punti)."
            ]
        },
        "pl": {
            "title": "Bournemouth rozbija Manchester United 3-0 na Old Trafford: Liverpool pokonuje Brighton na koniec 8. kolejki",
            "subtitle": "Wisnie bezlitosnie karza bledy gospodarzy. Liverpool awansuje na trzecie miejsce po wygranej 2-0.",
            "excerpt": "AFC Bournemouth sensacyjnie rozgromilo Manchester United 3-0 na Old Trafford w niedziele, zas Liverpool odprawil Brighton 2-0.",
            "body": [
                "AFC Bournemouth zaprezentowalo taktyczny kunszt w niedziele 25 pazdziernika, gromiac Manchester United 3-0 na Teatrze Marzen. Podopieczni Andoniego Iraoli wyprowadzili dwa bolesne ciosy przed przerwa: najpierw w 37. minucie precyzyjnym strzalem popisal sie Rayan, a piec minut pozniej prowadzenie podwyzszyl Marcus Tavernier po szybkiej akcji skrzydlem.",
                "Bezradni po przerwie gospodarze stracili trzecia bramke w doliczonym czasie gry, gdy Ryan Christie sfinalizowal kontratak. Porażka spycha Manchester United na 10. miejsce z 10 punktami, a Bournemouth ma juz 13 oczek. Z kolei Liverpool wygral na Anfield 2-0 z Brighton po samoboju Grossa i bramce Alexandra Isaka, awansujac na trzecia lokate w tabeli z 15 punktami za City i Arsenalem (21 pkt)."
            ]
        },
        "zh": {
            "title": "伯恩茅斯客场3-0横扫曼联震撼老特拉福德：利物浦力挫布莱顿紧咬争冠集团",
            "subtitle": "樱桃军团反击效率极致三度洞穿梦剧场球门，红军主场两球完胜布莱顿升至英超第三。",
            "excerpt": "英超第8轮周日再爆大冷门，伯恩茅斯客场3-0完胜曼联，利物浦2-0战胜布莱顿攀升至积分榜探花位置。",
            "body": [
                "伯恩茅斯在10月25日周日的老特拉福德球场上演了俱乐部历史上最辉煌的客场胜利之一，以3-0横扫曼联让梦剧场全场鸦雀无声。伊劳拉调教的球队在上半场展现出极高的反击效率，拉扬在第37分钟低射打破僵局，随后塔弗尼尔在第42分钟禁区前沿抽射将比分扩大为2-0。",
                "下半场曼联全力狂攻却收效甚微，替补登场的克里斯蒂在补时第92分钟单刀破门彻底杀死悬念。此役过后曼联跌至积分榜第十位（10分），而伯恩茅斯积13分强势杀入前六。在安菲尔德随后进行的比赛中，利物浦凭借格罗斯乌龙以及伊萨克的进球2-0完胜布莱顿，积15分升至积分榜第三位，紧跟同积21分的曼城与阿森纳。"
            ]
        },
        "ja": {
            "title": "ボーンマスがオールド・トラッフォードでマンUを3-0粉砕：リヴァプール快勝で第8節閉幕",
            "subtitle": "チェリーズが電光石火のカウンターで夢の劇場を沈黙させる。リヴァプールがブライトンを下し3位へ浮上。",
            "excerpt": "プレミアリーグ第8節の日曜日はボーンマスが敵地でマンチェスター・ユナイテッドを3-0で下す衝撃の大勝。リヴァプールは2-0で勝利しました。",
            "body": [
                "AFCボーンマスが10月25日日曜日、オールド・トラッフォードで圧巻の戦術眼を披露し、マンチェスター・ユナイテッドに3-0で完勝しました。イラオラ監督率いるチームは前半37分にラヤンのゴールで先制すると、42分にはマーカス・タヴァーニアーが豪快に追加点を奪い、ホームの観客を驚愕させました。",
                "後半に攻勢を強めたユナイテッドの攻撃を組織的守備で跳ね返し、アディショナルタイムにライアン・クリスティがトドメの3点目を沈めました。ユナイテッドは勝点10で10位に沈み、ボーンマスは勝点13でチェルシーと並ぶトップ6へ。アンフィールドではリヴァプールがグロスのOGとイサクの得点でブライトンを2-0で退け、勝点15で3位へ浮上しました。"
            ]
        },
        "ko": {
            "title": "본머스 올드 트래퍼드서 맨유 3-0 완파 충격: 리버풀 브라이턴 잡고 3위 도약",
            "subtitle": "체리스 날카로운 역습으로 꿈의 극장 완벽 침묵. 리버풀은 2-0 승리로 선두권 맹추격.",
            "excerpt": "AFC 본머스가 일요일 올드 트래퍼드에서 맨체스터 유나이티드를 3-0으로 완파했고 리버풀은 브라이턴을 2-0으로 제압하며 8라운드를 마쳤습니다.",
            "body": [
                "AFC 본머스가 10월 25일 일요일 올드 트래퍼드에서 맨체스터 유나이티드를 3-0으로 완파하는 기염을 토했습니다. 안도니 이라올라 감독의 본머스는 전반 37분 하얀의 선제골로 기선을 잡은 데 이어 전반 42분 마커스 태버니어의 추가골로 2-0 리드를 잡으며 홈 팬들을 얼어붙게 만들었습니다.",
                "후반 맨유가 총공세에 나섰지만 본머스의 촘촘한 수비벽에 막혔고 후반 추가시간 라이언 크리스티의 역습 쐐기골이 터지며 경기는 3-0으로 끝났습니다. 맨유는 4패째(승점 10점)로 10위까지 밀려난 반면 본머스는 승점 13점으로 6위로 도약했습니다. 안필드에서는 리버풀이 그로스의 자책골과 이사크의 추가골로 브라이턴을 2-0으로 누르고 승점 15점으로 3위에 안착했습니다."
            ]
        },
        "ar": {
            "title": "بورنموث يكتسح مانشستر يونايتد 3-0 في اولد ترافورد: ليفربول يسقط برايتون في ختام الجولة 8",
            "subtitle": "الكرز يعاقبون اخطاء اليونايتد بفاعلية هجومية حاسمة. وليفربول يصعد للمركز الثالث بفوزه 2-0.",
            "excerpt": "صعق نادي بورنموث مضيفه مانشستر يونايتد بثلاثية نظيفة في معقله يوم الاحد، بينما تخطى ليفربول عقبة برايتون بهدفين دون رد.",
            "body": [
                "قدم بورنموث احد افضل عروضه التكتيكية في تاريخه بملعب اولد ترافورد يوم الاحد 25 اكتوبر، بعدما امطر شباك مانشستر يونايتد بثلاثية نظيفة دون مقابل. واستغل لاعبو المدرب اندوني ايراولا الهفوات الدفاعية لاصحاب الارض ليفتتح رايان التسجيل في الدقيقة 37، قبل ان يعزز ماركوس تافيرنييه النتيجة بهدف ثان في الدقيقة 42.",
                "وعجز اليونايتد عن تقليص الفارق طوال الشوط الثاني امام الدفاع المنظم للضيوف، ليعود ريان كريستي ويسجل الهدف الثالث في الوقت بدل الضائع من مرتدة سريعة. وبهذه الهزيمة تراجع يونايتد للمركز العاشر بـ10 نقاط بينما قفز بورنموث الى 13 نقطة. وفي انفيلد فاز ليفربول على برايتون 2-0 بهدف عكسي لغروس وهدف لالكسندر ايزاك ليرتقي للمركز الثالث برصيد 15 نقطة."
            ]
        }
    },
    "atp-vienna-basel-2026-indoor-swing-alcaraz-khachanov-medvedev": {
        "fr": {
            "title": "La tournee indoor ATP 500 demarre a Vienne et Bâle : Alcaraz face au piege Khachanov",
            "subtitle": "Tout juste titre a Almaty, Medvedev debarque en Autriche. Zverev et Alcaraz tetes d'affiche d'un tableau tres releve.",
            "excerpt": "La saison automnale sous toit passe a la vitesse superieure ce lundi avec les tournois ATP 500 de Vienne et Bâle, marques par le duel Alcaraz-Khachanov.",
            "body": [
                "Le sprint automnal du circuit ATP monte d'un cran ce lundi 26 octobre avec le lancement simultane de deux grands tournois ATP 500 : l'Erste Bank Open a Vienne et les Swiss Indoors a Bâle. Avec en ligne de mire les precieux points pour la qualification aux ATP Finals de Turin, les meilleurs joueurs du monde se sont rassembles sur les courts rapides en dur couverts en Autriche et en Suisse.",
                "A Vienne, le numero deux mondial Carlos Alcaraz attire tous les regards des le premier tour avec un choc complique face au puissant Karen Khachanov. En l'absence de Jannik Sinner blesse au genou, Alcaraz et la tete de serie numero un Alexander Zverev menent le tableau. Daniil Medvedev, tout juste victorieux a Almaty pour son 25e sacre en carriere, rejoint egalement la capitale autrichienne. A Bâle, Novak Djokovic fait son retour sur le circuit indoor aux cotes de Taylor Fritz et Ben Shelton."
            ]
        },
        "es": {
            "title": "Arranca la gira bajo techo ATP 500 en Viena y Basilea: Alcaraz ante la exigencia de Khachanov",
            "subtitle": "Tras defender corona en Almaty, Medvedev aterriza en Austria. Zverev y Alcaraz comandan un cuadro estelar.",
            "excerpt": "La temporada de pistas rapidas indoor pisa el acelerador este lunes con los torneos ATP 500 de Viena y Basilea, con el atractivo Alcaraz contra Khachanov.",
            "body": [
                "La recta final de la temporada ATP entra en su fase mas intensa este lunes 26 de octubre con el inicio simultaneo de dos torneos ATP 500 de gran tradicion: el Erste Bank Open de Viena y el Swiss Indoors de Basilea. En juego estan billetes dorados para las Nitto ATP Finals de Turin, concentrando a las mejores raquetas del planeta en las veloces pistas indoor de Austria y Suiza.",
                "En Viena, el espanol Carlos Alcaraz afronta un exigente debut en primera ronda ante el pegador Karen Khachanov. Con Jannik Sinner ausente por problemas de rodilla, Alcaraz y el aleman Alexander Zverev encabezan el cuadro. Daniil Medvedev llega lanzado tras conquistar en Almaty el trofeo numero 25 de su carrera. Paralelamente en Basilea, Novak Djokovic lidera la competicion junto a los estadounidenses Taylor Fritz y Ben Shelton."
            ]
        },
        "de": {
            "title": "ATP-500-Hallensaison startet in Wien und Basel: Alcaraz vor harter Khachanov-Pruefung",
            "subtitle": "Frischgebackener Almaty-Sieger Medvedev reist nach Oesterreich. Zverev und Alcaraz fuehren starkes Feld der Erste Bank Open an.",
            "excerpt": "Die Hallensaison nimmt am Montag mit den hochkaraetigen ATP-500-Events in Wien und Basel Fahrt auf, angefuehrt vom Auftaktkracher Alcaraz gegen Khachanov.",
            "body": [
                "Der Herbst-Sprint der ATP Tour nimmt am Montag, den 26. Oktober, maximale Fahrt auf: Mit den Erste Bank Open in der Wiener Stadthalle und den Swiss Indoors in Basel starten gleich zwei prestigetraechtige ATP-500-Turniere zeitgleich. Auf den schnellen Hallenbelaegen geht es um entscheidende Punkte fuer die Qualifikation zu den ATP Finals in Turin.",
                "In Wien steht die Nummer zwei der Welt, Carlos Alcaraz, sofort vor einer Bewaehrungsprobe gegen den hart schlagenden Karen Khachanov. Da Titelverteidiger Jannik Sinner mit Kniebeschwerden passen musste, fuehren Alcaraz und der topgesetzte Alexander Zverev das Teilnehmerfeld an. Auch Daniil Medvedev stoesst nach seinem 25. Karrieretitel in Almaty zum Wiener Feld. In Basel fuehrt Altmeister Novak Djokovic das Tableau gemeinsam mit Taylor Fritz an."
            ]
        },
        "it": {
            "title": "Al via la stagione indoor ATP 500 a Vienna e Basilea: Alcaraz esordisce contro Khachanov",
            "subtitle": "Fresco di bis ad Almaty, Medvedev sbarca in Austria. Zverev e Alcaraz guidano il prestigioso Erste Bank Open.",
            "excerpt": "Il circuito sul cemento indoor sale di livello questo lunedi con i tornei ATP 500 di Vienna e Basilea, impreziositi dalla sfida Alcaraz-Khachanov.",
            "body": [
                "La volata conclusiva dell'annata tennistica entra nel vivo lunedi 26 ottobre con l'avvio simultaneo di due storici tornei ATP 500: l'Erste Bank Open alla Wiener Stadthalle di Vienna e gli Swiss Indoors di Basilea. In palio ci sono punti pesantissimi per conquistare gli ultimi pass per le ATP Finals di Torino sul veloce indoor mitteleuropeo.",
                "A Vienna il numero due al mondo Carlos Alcaraz e atteso da un debutto subito complicato contro Karen Khachanov. Senza il campione in carica Jannik Sinner, fermato da un risentimento al ginocchio, Alcaraz e Alexander Zverev sono le prime teste di serie. Nel tabellone austriaco figura anche Daniil Medvedev, reduce dal 25° trionfo in carriera ad Almaty. A Basilea spicca il ritorno in campo di Novak Djokovic affiancato da Taylor Fritz e Ben Shelton."
            ]
        },
        "pl": {
            "title": "Sezon halowy ATP 500 startuje w Wiedniu i Bazylei: Alcaraz staje do walki z Chaczanowem",
            "subtitle": "Po obronie tytulu w Almaty Medwiediew melduje sie w Austrii. Zverev i Alcaraz gwiazdami Erste Bank Open.",
            "excerpt": "Europejski sezon halowy wchodzi w decydujaca faze w poniedzialek wraz ze startem turniejow ATP 500 w Wiedniu i Bazylei, na czele z meczem Alcaraz-Chaczanow.",
            "body": [
                "Jesienny finisz cyklu ATP Tour nabiera pelnego rozpedu w poniedzialek 26 pazdziernika wraz z rownoczesnym rozpoczeciem dwoch wielkich turniejow rangi ATP 500: Erste Bank Open w Wiedniu oraz Swiss Indoors w Bazylei. Walka o bezcenne punkty rankingowe do torynskich ATP Finals przyciagnela na szybkie korty twarde w Austrii i Szwajcarii czolowke swiatowego tenisa.",
                "W Wiedniu Carlos Alcaraz przystepuje do gry od trudnego pojedynku pierwszej rundy z silnie serwujacym Karenem Chaczanowem. Pod nieobecnosc lezacego kolano Jannika Sinnera, turniejowa drabinke otwieraja Alexander Zverev i Alcaraz, do ktorych dolacza swiezo upieczony triumfator z Almaty Daniił Medwiediew. W rownoleglym turnieju w Bazylei glowna gwiazda jest Novak Djokovic walczacy u boku Taylora Fritza."
            ]
        },
        "zh": {
            "title": "ATP 500室内硬地赛季维也纳与巴塞尔开拍：阿尔卡拉斯首轮直面哈恰诺夫",
            "subtitle": "梅德韦杰夫携阿拉木图卫冕之勇抵奥地利，兹维列夫与阿尔卡拉斯领衔豪华参赛阵容。",
            "excerpt": "欧洲室内硬地赛季在周一全面提速，维也纳与巴塞尔两站ATP 500赛事同步挥拍，阿尔卡拉斯与哈恰诺夫上演强强对话。",
            "body": [
                "ATP巡回赛秋季室内冲刺阶段在10月26日周一迎来高潮，两项历史悠久的ATP 500顶级赛事：奥地利维也纳的斯特哈勒公开赛与瑞士巴塞尔室内赛同步开打。为了争夺通往都灵年终总决赛的关键积分，世界顶尖男子网球高手悉数集结在欧陆快速室内硬地球场。",
                "在维也纳，世界排名第二的阿尔卡拉斯首轮便抽到底线重炮哈恰诺夫，迎来极具挑战性的室内硬地首秀。在卫冕冠军辛纳因膝伤缺席的情况下，阿尔卡拉斯与头号种子兹维列夫共同坐镇上下半区。刚刚在阿拉木图斩获职业生涯第25座单打冠军的梅德韦杰夫同样现身维也纳。巴塞尔方面则由天王德约科维奇领衔，弗里茨与谢尔顿等名将亦在列。"
            ]
        },
        "ja": {
            "title": "ATP 500インドアシーズンがウィーンとバーゼルで開幕：アルカラスがハチャノフの挑戦を受ける",
            "subtitle": "アルマトイ連覇のメドベージェフがオーストリアへ転戦。ズベレフとアルカラスが強豪集うドローを牽引。",
            "excerpt": "ヨーロッパの室内ハードコートシーズンが月曜に本格始動。ウィーンとバーゼルのATP 500大会が開幕し、アルカラス対ハチャノフの好カードが実現。",
            "body": [
                "ATPツアーの秋の室内サーキットが10月26日月曜、ウィーン（エルステ・バンク・オープン）とバーゼル（スイス・インドア）のATP 500同時開催によって最高潮に突入しました。トリノでのATPファイナルズ出場権をかけたポイント争奪戦が、オーストリアとスイスの高速室内コートで幕を開けます。",
                "ウィーンでは世界ランク2位のカルロス・アルカラスが1回戦から屈指の強打者カレン・ハチャノフと対峙します。膝の故障で欠場となった前年覇者ヤニック・シナーに代わり、第1シードのアレクサンダー・ズベレフとともに大会を牽引。日曜にアルマトイで自身通算25個目のタイトルを手にしたダニール・メドベージェフも参戦します。バーゼルにはノバク・ジョコビッチが登場します。"
            ]
        },
        "ko": {
            "title": "ATP 500 실내 하드코트 시리즈 빈과 바젤 개막: 알카라스 하차노프와 1회전 격돌",
            "subtitle": "알마티 타이틀 방어 마친 메드베데프 오스트리아 합류. 즈베레프와 알카라스 특급 대진표 견인.",
            "excerpt": "유럽 실내 하드코트 시즌이 월요일 빈과 바젤에서 개막하며 본격화된 가운데 카를로스 알카라스가 카렌 하차노프와 32강 맞대결을 펼칩니다.",
            "body": [
                "ATP 투어의 가을 실내 하드코트 레이스가 10월 26일 월요일 오스트리아 빈의 에르스테 뱅크 오픈과 스위스 바젤의 스위스 인도어스가 동시 개막하며 최고조에 달했습니다. 토리노 ATP 파이널스 출전권이 걸린 귀중한 랭킹 포인트를 놓고 세계 정상급 선수들이 유럽의 빠른 실내 코트에 집결했습니다.",
                "빈에서는 세계 랭킹 2위 카를로스 알카라스가 첫 경기부터 만만치 않은 파워 히터 카렌 하차노프를 상대합니다. 무릎 부상으로 불참한 디펜딩 챔피언 야닉 시너의 공백 속에 알카라스와 톱시드 알렉산더 즈베레프가 우승을 다툽니다. 일요일 알마티에서 통산 25번째 트로피를 들어 올린 다닐 메드베데프도 곧바로 합류했으며, 바젤에서는 노박 조코비치와 테일러 프리츠가 경쟁합니다."
            ]
        },
        "ar": {
            "title": "انطلاق بطولات ATP 500 داخل الصالات في فيينا وبازل: الكاراز في مواجهة نارية امام خاتشانوف",
            "subtitle": "ميدفيديف يصل النمسا بعد تتويجه في الماتي. وزفيريف والكاراز يتصدران قرعة بطولة فيينا المفتوحة.",
            "excerpt": "يدخل موسم الصالات الاوروبي مرحلته الحاسمة يوم الاثنين بانطلاق بطولتي فيينا وبازل من فئة 500 نقطة بمباراة قمة بين الكاراز وخاتشانوف.",
            "body": [
                "تصل سرعة منافسات بطولات رابطة المحترفين للتنس الى ذروتها يوم الاثنين 26 اكتوبر، مع الانطلاق المتزامن لبطولتين عريقتين من فئة 500 نقطة: بطولة فيينا المفتوحة في النمسا وبطولة بازل في سويسرا. وتتنافس نخبة لاعبي التنس العالميين على الملاعب الصلبة السريعة داخل الصالات لحصد نقاط التأهل الى البطولة الختامية في تورينو.",
                "وفي فيينا، يخوض المصنف الثاني عالميا كارلوس الكاراز امتحانا حقيقيا في الدور الاول امام الروسي القوي كارين خاتشانوف. ومع انسحاب حامل اللقب يانيك سينر بسبب اصابة في الركبة، يتصدر الكاراز والالماني الكسندر زفيريف قائمة المرشحين، وينضم اليهما دانييل ميدفيديف المنتشي بلقبه الـ25 في مسيرته بالماضي القريب في الماتي. وفي بازل يظهر الصربي نوفاك ديوكوفيتش الى جانب تايلور فريتز وبين شيلتون."
            ]
        }
    }
}

# Strict validation
for slug, langs in OCT26_STORIES.items():
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
for slug, langs in OCT26_STORIES.items():
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

print("Successfully injected October 26 translations into frontend/src/i18n/stories.ts")
