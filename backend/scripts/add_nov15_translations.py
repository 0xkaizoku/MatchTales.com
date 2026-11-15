"""
add_nov15_translations.py
Injects 9-locale translations for the 6 stories of 15 Nov 2026 into STORY_I18N in stories.ts.
"""
import re
import json

nov15_i18n = {
  "dp-world-tour-dubai-hatton-wins-mcilroy-seals-race-to-dubai-2026": {
    "fr": {
      "title": "Hatton s'envole vers le trophee a Dubai avec un 66 ; McIlroy scelle sa 8e Race to Dubai",
      "subtitle": "Tyrrell Hatton termine a 15 sous le par pour l'emporter avec cinq coups d'avance, tandis que Rory McIlroy (67) devance Eugenio Chacarra de 125 points pour egaler Colin Montgomerie.",
      "excerpt": "Hatton rend une derniere carte de 66 pour atteindre -15 (273) et remporter le DP World Tour Championship. McIlroy termine 2e seul a -10 (278) et empoche sa 8e couronne.",
      "body": [
        "Tyrrell Hatton a remporte dimanche 15 novembre son neuvieme titre sur le DP World Tour et son sixieme trophee Rolex Series en signant un magistral 66 (-6) sans bogey sur l'Earth Course a Jumeirah Golf Estates, s'imposant avec cinq longueurs d'avance a -15 (273). Parti avec un coup d'avance, l'Anglais a boucle quatre birdies sur ses huit premiers trous pour ne plus jamais etre rejoint.",
        "La Race to Dubai a offert un denouement a suspense jusqu'au green du 72e trou. L'Espagnol Eugenio Chacarra, en tete du classement virtuel pendant le retour, a signe un solide 68 pour finir 3e ex aequo a 9 sous le par (279) aux cotes d'Oliver Lindell. Mais Rory McIlroy a fait parler son sang-froid en rendant un 67 (-5) illumine par un birdie determinant au trou 16 pour prendre seul la 2e place a -10 (278).",
        "Cette deuxieme place permet a McIlroy de decrocher sa huitieme couronne de l'Ordre du Merite europeen et son cinquieme Harry Vardon Trophy consecutif avec seulement 125 points d'avance, egalant le record historique de Colin Montgomerie. Emoustille au micro, McIlroy a dedie sa victoire a son pere Gerry, qui a passe plusieurs semaines en soins intensifs a Cleveland apres une double greffe pulmonaire cet automne."
      ]
    },
    "es": {
      "title": "Hatton vuela al titulo en Dubai con 66; McIlroy emboca en el 16 y sella su octava Race to Dubai",
      "subtitle": "Tyrrell Hatton finaliza con 15 bajo par para imponerse por cinco golpes, mientras el 67 sin bogeys de Rory McIlroy supera a Eugenio Chacarra por 125 puntos igualando a Colin Montgomerie.",
      "excerpt": "Hatton firma 66 en la ronda final para ganar con -15 (273) el DP World Tour Championship. McIlroy es segundo en solitario (-10, 278) y se queda con el trofeo de la temporada.",
      "body": [
        "Tyrrell Hatton conquisto su noveno titulo del DP World Tour y sexto Rolex Series este domingo 15 de noviembre, firmando un impecable 66 (-6) sin bogeys en el Earth Course de Jumeirah Golf Estates para terminar con 15 bajo par (273) y ganar por cinco golpes el DP World Tour Championship. Con cuatro birdies en sus primeros ocho hoyos, el ingles aseguro una victoria inapelable en Dubai.",
        "La Race to Dubai mantuvo la emocion al maximo hasta el hoyo 72. El espanol Eugenio Chacarra, que lidero la clasificacion virtual durante la segunda vuelta, entrego un 68 para empatar el tercer puesto con 9 bajo par (279) junto a Oliver Lindell. Sin embargo, Rory McIlroy respondio con serenidad de campeon, sellando una tarjeta de 67 (-5) con un birdie decisivo en el par 4 del hoyo 16 para terminar segundo en solitario con 278 (-10).",
        "El subcampeonato aseguro a McIlroy su octava Orden de Merito de Europa y su quinto Harry Vardon Trophy seguido por una ventaja de solo 125 puntos, igualando la marca de Colin Montgomerie. Conmovido, el norirlandes dedico la corona a su padre Gerry, quien se recupera de un trasplante bipulmonar realizado en Cleveland a comienzos de otono."
      ]
    },
    "de": {
      "title": "Hatton triumphiert in Dubai mit 66er-Runde; McIlroy sichert sich achten Race-to-Dubai-Titel",
      "subtitle": "Tyrrell Hatton siegt mit fuenf Schlaegen Vorsprung bei 15 unter Par, waehrend Rory McIlroys bogeyfreie 67 Eugenio Chacarra um 125 Punkte distanziert und Montgomeries Rekord einstellt.",
      "excerpt": "Hatton spielt eine 66 fuer 15 unter Par (273) und gewinnt das Finale. McIlroy wird Zweiter (-10, 278) und verteidigt den Saisontitel um 125 Punkte gegen Chacarra.",
      "body": [
        "Tyrrell Hatton sicherte sich am Sonntag, 15. November, seinen neunten DP World Tour-Titel und sechsten Rolex Series-Erfolg mit einer ueberragenden 66 (-6) ohne Schlagverlust auf dem Earth Course von Jumeirah Golf Estates. Mit 15 unter Par (273) dominierte der Englaender das DP World Tour Championship und gewann mit fuenf Schlaegen Vorsprung.",
        "Das Duell um die Race to Dubai bot Dramatik bis zum 72. Gruen. Der Spanier Eugenio Chacarra, der auf den zweiten neun Loechern virtuell fuehrte, unterschrieb eine 68 und teilte Rang drei bei 9 unter Par (279) mit Oliver Lindell. Doch Rory McIlroy bewies Nervenstaerke: Seine fehlerfreie 67 (-5) mit einem Schluessel-Birdie auf der 16 brachte ihm Rang zwei (-10, 278) ein.",
        "Dieses Ergebnis genuegte McIlroy, um mit 125 Punkten Vorsprung seine achte europaeische Geldranglistenkrone zu gewinnen und Colin Montgomeries ewigen Rekord einzustellen. Unter Traenen widmete er den Triumph seinem Vater Gerry, der sich von einer doppelten Lungentransplantation in Cleveland erholt."
      ]
    },
    "it": {
      "title": "Hatton domina a Dubai con un 66; McIlroy birdie alla 16 e sigilla l'ottava Race to Dubai",
      "subtitle": "Tyrrell Hatton vince con cinque colpi di margine a 15 sotto il par, mentre il 67 senza bogey di Rory McIlroy beffa Eugenio Chacarra per 125 punti eguagliando Colin Montgomerie.",
      "excerpt": "Hatton chiude in 66 a -15 (273) per conquistare il DP World Tour Championship. McIlroy e secondo a -10 (278) e conquista il suo ottavo Harry Vardon Trophy.",
      "body": [
        "Tyrrell Hatton ha conquistato domenica 15 novembre il suo nono titolo sul DP World Tour e sesto trofeo Rolex Series, firmando un magnifico 66 (-6) bogey-free sull'Earth Course a Jumeirah Golf Estates per chiudere a 15 sotto il par (273) e trionfare con cinque colpi di vantaggio nel DP World Tour Championship.",
        "La battaglia per la Race to Dubai e stata vibrante fino alla 72a buca. Lo spagnolo Eugenio Chacarra, leader virtuale sulle seconde nove buche, ha chiuso con un 68 per il terzo posto a -9 (279) assieme a Oliver Lindell. Ma Rory McIlroy ha mantenuto la calma, girando in 67 (-5) grazie a un birdie determinante alla buca 16 che gli e valso il secondo posto solitario a quota 278 (-10).",
        "Il piazzamento ha consegnato a McIlroy il suo ottavo trionfo nell'Ordine di Merito europeo per appena 125 punti, eguagliando il primato di Colin Montgomerie. Commosso, il campione ha dedicato la vittoria al padre Gerry, reduce da un trapianto di polmoni a Cleveland."
      ]
    },
    "pl": {
      "title": "Hatton triumfuje w Dubaju runda 66; McIlroy birdie na 16. dolku pieczetuje osmy tytul Race to Dubai",
      "subtitle": "Tyrrell Hatton konczy 15 ponizej par z przewaga pieciu uderzen, a bezbledne 67 Rory'ego McIlroya wyprzedza Eugenio Chakarre o 125 punktow i wyrownuje rekord Montgomeriego.",
      "excerpt": "Hatton z 66 w finale osiaga -15 (273) i wygrywa DP World Tour Championship. McIlroy zajmuje drugie miejsce (-10, 278) i zdobywa osmy tytul sezonu.",
      "body": [
        "Tyrrell Hatton wygral w niedziele 15 listopada swoj dziewiaty turniej DP World Tour i szosty Rolex Series, notujac perfekcyjna runde 66 (-6) bez bogeyow na Earth Course w Jumeirah Golf Estates, triumfujac z przewaga pieciu uderzen z wynikiem 15 ponizej par (273).",
        "Rywalizacja o puchar Race to Dubai trzymala w napieciu do ostatniego dolka. Hiszpan Eugenio Chacarra, ktory prowadzil w wirtualnej tabeli w drugiej polowie rundy, zagral 68 i podzielil trzecie miejsce z wynikiem 279 (-9) z Oliverem Lindellem. Rory McIlroy zachowal jednak spokoj mistrza, notujac bezbledne 67 (-5) z kluczowym birdie na 16. dolku, co dalo mu samodzielne drugie miejsce (278, -10).",
        "Ten wynik zapewnil McIlroyowi osmy tytul Order of Merit i piaty z rzedu Harry Vardon Trophy o zaledwie 125 punktow, czym wyrownal historyczny rekord Colina Montgomeriego. Wzruszony zadedykowal sukces swojemu ojcu Gerry'emu, dochodzacemu do siebie po przeszczepie pluc w Cleveland."
      ]
    },
    "zh": {
      "title": "哈顿末轮轰出66杆加冕迪拜总冠军；麦克罗伊第16洞抓鸟八度登顶迪拜竞赛",
      "subtitle": "哈顿以低于标准杆15杆（273杆）的绝对优势五杆大胜，麦克罗伊零柏忌67杆以125分微弱优势险胜查卡拉，追平蒙哥马利八冠纪录。",
      "excerpt": "哈顿末轮交出66杆总成绩-15（273杆）夺得DP世界巡回锦标赛冠军。麦克罗伊以-10（278杆）单独位居次席，力压查卡拉第八次捧起哈里·瓦登奖杯。",
      "body": [
        "11月15日周日，英格兰名将泰瑞尔·哈顿在朱美拉高尔夫庄园大地球场展现统领级表现，末轮打出无可挑剔的零柏忌66杆（-6），以54洞与末轮合计273杆（-15）赢得DP世界巡回锦标赛冠军，并揽下个人第九座欧巡赛奖杯及第六座劳力士系列赛冠军。",
        "赛季收官的迪拜竞赛总冠军争夺战则直到第72洞果岭才见分晓。西班牙黑马欧亨尼奥·查卡拉后九洞一度在即时积分榜领先，交出68杆后以279杆（-9）与奥利弗·林德尔并列第三位。然而罗里·麦克罗伊展现王者定力，抓下四只小鸟并于第16洞推入制胜鸟推，交出零柏忌67杆，以278杆（-10）独享第二名。",
        "凭借这一亚军，麦克罗伊最终以仅125分的微弱优势绝杀查卡拉，职业生涯第八次加冕欧巡赛奖金王并连续五年捧得哈里·瓦登奖杯，追平了名宿科林·蒙哥马利的历史纪录。赛后麦克罗伊热泪盈眶，将胜利献给了今秋在克利夫兰接受双肺移植手术后康复中的父亲杰里。"
      ]
    },
    "ja": {
      "title": "ハットンが66で5打差圧勝；マキロイが16番バーディで8度目の年間王者戴冠",
      "subtitle": "ティレル・ハットンが通算15アンダー（273）でジュメイラを制覇。マキロイがノーボギー67でチャカラをわずか125点差でかわし、モンゴメリーの歴代最多記録に並ぶ。",
      "excerpt": "ハットンが最終日66で通算-15（273）としDPワールドツアー選手権を制覇。マキロイは通算-10（278）の単独2位に入り、チャカラを抑えて8度目の年間王者に輝いた。",
      "body": [
        "11月15日日曜日、イングランドのティレル・ハットンがジュメイラ・ゴルフ・エステーツのアースコースで圧巻のノーボギー66（-6）をマークし、通算15アンダー（273）で5打差の独走勝利を飾り、DPワールドツアー通算9勝目、ロレックスシリーズ6勝目を飾った。",
        "シーズン総合王者を争うレース・トゥ・ドバイは最終72ホール目まで劇的な展開となった。後半に一時ポイント首位に立ったスペインのエウヘニオ・チャカラは68で回り通算9アンダー（279）で3位タイ。しかしローリー・マキロイが勝負強さを発揮し、16番パー4での値千金のバーディを含むノーボギー67で通算10アンダー（278）の単独2位を死守した。",
        "この結果、マキロイはわずか125ポイント差でチャカラを抑えて8度目の欧州年間王者となり、コリン・モンゴメリーの歴代最多記録に並んだ。グリーンサイドでのインタビューで、マキロイはこの栄冠をクリーブランドで肺移植手術から回復中の父ジェリーに捧げた。"
      ]
    },
    "ko": {
      "title": "해튼 66타로 두바이 5타 차 완승; 매킬로이 16번 홀 버디로 통산 8번째 레이스 투 두바이 제패",
      "subtitle": "타렐 해튼이 15언더파(273타)로 압도적 우승을 차지했고, 로리 매킬로이는 보기 없는 67타로 차카라를 125점 차로 제치며 몽고메리의 역대 최다 기록과 동률을 이뤘습니다.",
      "excerpt": "해튼이 최종 라운드 66타로 15언더파(273타) 우승을 달성. 매킬로이는 10언더파(278타) 단독 2위로 차카라를 125점 차로 제치고 8번째 해리 바든 트로피를 차지했습니다.",
      "body": [
        "11월 15일 일요일 주메이라 골프 에스테이트 어스 코스에서 열린 DP 월드투어 챔피언십 최종 라운드에서 잉글랜드의 타렐 해튼이 보기 없이 버디만 6개를 낚아채며 66타(-6)를 기록, 54홀에 이어 최종 합계 15언더파(273타)로 5타 차 완승을 거두었습니다.",
        "시즌 전체 챔피언을 가리는 레이스 투 두바이 경쟁은 마지막 72번째 홀까지 치열하게 전개되었습니다. 후반 한때 가상 선두에 올랐던 에우헤니오 차카라가 68타로 합계 9언더파(279타) 공동 3위를 기록했으나, 로리 매킬로이가 승부처인 16번 홀 버디를 포함해 67타(-5)로 합계 10언더파(278타) 단독 2위를 확보했습니다.",
        "이로써 매킬로이는 차카라를 단 125포인트 차로 제치고 통산 8번째 오더 오브 메리트 및 5년 연속 해리 바든 트로피를 들어 올리며 콜린 몽고메리의 전설적 기록과 타이를 이뤘습니다. 경기 후 매킬로이는 클리블랜드에서 폐 이식 수술을 받고 회복 중인 아버지 게리에게 이 트로피를 바쳤습니다."
      ]
    },
    "ar": {
      "title": "هاتون يحلق بلقب دبي بـ66 ضربة؛ ومكلروي يسجل بيردي في الحفرة 16 ليحسم لقبه الثامن في السباق إلى دبي",
      "subtitle": "تيريل هاتون ينهي البطولة عند 15 تحت المعدل ليفوز بفارق خمس ضربات، بينما 67 ضربة نظيفة من روري مكلروي تمنحه التفوق على تشاكارا بفارق 125 نقطة ليعادل رقم مونتغمري.",
      "excerpt": "هاتون يوقع 66 ضربة ليصل إلى 15 تحت المعدل (273) متوجاً ببطولة دي بي ورلد. مكلروي يحل وصيفاً منفرداً بـ-10 (278) ويحسم لقبه الثامن ببطولة الموسم.",
      "body": [
        "توج الإنجليزي تيريل هاتون يوم الأحد 15 نوفمبر بلقبه التاسع في جولة دي بي ورلد وسادس ألقاب سلسلة رولكس، مسجلاً 66 ضربة (-6) دون أي بوغي في ملعب إيرث بجميرا غولف إستيتس ليحسم بطولة جولة دي بي ورلد بمجموع 273 ضربة (-15) وبفارق خمس ضربات.",
        "وشهد الصراع على لقب الموسم في السباق إلى دبي إثارة بالغة حتى الحفرة 72. الإسباني يوجينيو تشاكارا، الذي تصدر الترتيب المباشر في النصف الثاني، سجل 68 ضربة ليتقاسم المركز الثالث عند 9 تحت المعدل (279) مع أوليفر لينديل. لكن روري مكلروي أظهر ثبات الأبطال محققاً 67 ضربة (-5) وبيردي حاسم في الحفرة 16 ليحسم وصافة البطولة منفرداً بـ278 ضربة (-10).",
        "وضمن هذا المركز لمكلروي الفوز بلقب قائمة الاستحقاق الأوروبية للمرة الثامنة وخامس كأس هاري فاردون توالياً بفارق 125 نقطة فقط، ليعادل الرقم القياسي التاريخي لكولين مونتغمري. وفي لقاء مؤثر عقب التتويج، أهدى مكلروي الفوز لوالده جيري الذي يتعافى من زراعة رئة مزدوجة في كليفلاند."
      ]
    }
  },

  "atp-finals-turin-zverev-downs-jodar-fritz-takes-stockholm-2026": {
    "fr": {
      "title": "Zverev lance Turin en deux sets contre Jodar ; Fritz s'offre Stockholm au finish",
      "subtitle": "Le numero un mondial Alexander Zverev domine Rafael Jodar 6-4, 6-4 dans le groupe John McEnroe, tandis que Taylor Fritz s'impose 6-2, 4-6, 7-6 (3) en Suede.",
      "excerpt": "Ouverture a Turin dimanche : Zverev bat Jodar 6-4, 6-4 en 87 minutes ; Shelton affronte Fils ce soir. A Stockholm, Fritz decroche le titre au jeu decisif face a Tirante.",
      "body": [
        "Les Nitto ATP Finals 2026 ont demarre dimanche 15 novembre a l'Inalpi Arena de Turin avec la victoire autoritaire du numero un mondial Alexander Zverev sur l'espoir espagnol Rafael Jodar (6-4, 6-4) dans le groupe John McEnroe. L'Allemand a livre une prestation impériale au service pendant 87 minutes, ne concédant que sept points sur sa premiere balle pour reussir son entree.",
        "La session du soir a Turin propose un duel passionnant entre l'Americain Ben Shelton et le Francais Arthur Fils, signant le retour d'un tricolore au Masters pour la premiere fois en dix ans. Le groupe Ivan Lendl ouvrira ses portes lundi avec Carlos Alcaraz oppose a Frances Tiafoe et Daniil Medvedev face a Flavio Cobolli.",
        "Samedi a Stockholm, la tete de serie numero un Taylor Fritz a glane son deuxieme trophee dans la capitale suedoise en venant a bout du surprenant finaliste argentin Thiago Agustin Tirante (6-2, 4-6, 7-6 (3)). Fritz a du batailler jusqu'au jeu decisif du troisieme set pour l'emporter avant de s'envoler pour l'Italie."
      ]
    },
    "es": {
      "title": "Zverev arranca Turin en dos sets ante Jodar; Fritz supera a Tirante en Estocolmo",
      "subtitle": "El numero uno mundial Alexander Zverev vence a Rafael Jodar 6-4, 6-4 en el grupo McEnroe, mientras Taylor Fritz triunfa 6-2, 4-6, 7-6 (3) en Suecia.",
      "excerpt": "Turin abre el domingo: Zverev vence a Jodar 6-4, 6-4 en 87 minutos; Shelton vs Fils esta noche. En Estocolmo, Fritz gana el titulo en el tiebreak ante Tirante.",
      "body": [
        "Las Nitto ATP Finals 2026 comenzaron este domingo 15 de noviembre en el Inalpi Arena de Turin con la victoria del numero uno Alexander Zverev ante el joven espanol Rafael Jodar por 6-4 y 6-4 en el grupo John McEnroe. Zverev sirvio a gran nivel durante 87 minutos, cediendo apenas siete puntos con su primer saque y logrando un quiebre en cada set.",
        "La jornada nocturna en Turin presenta el choque entre Ben Shelton y el frances Arthur Fils en el segundo encuentro del grupo McEnroe. La accion del grupo Ivan Lendl iniciara el lunes con Carlos Alcaraz frente a Frances Tiafoe y Daniil Medvedev ante Flavio Cobolli.",
        "El sabado en Estocolmo, el estadounidense Taylor Fritz se proclamo campeon al derrotar al argentino Thiago Agustin Tirante por 6-2, 4-6 y 7-6 (3). Tirante ofrecio una gran resistencia, pero Fritz mostro mayor temple en el desempate decisivo para levantar el trofeo sueco."
      ]
    },
    "de": {
      "title": "Zverev startet in Turin mit Zweisatzsieg gegen Jodar; Fritz triumphiert in Stockholm",
      "subtitle": "Weltranglistenerster Alexander Zverev schlaegt Rafael Jodar 6:4, 6:4 in der McEnroe-Gruppe, waehrend Taylor Fritz in Schweden 6:2, 4:6, 7:6 (3) gewinnt.",
      "excerpt": "Turin eroeffnet am Sonntag: Zverev bezwingt Jodar 6:4, 6:4 in 87 Minuten; Shelton vs. Fils heute Abend. In Stockholm gewinnt Fritz den Titel im Tiebreak gegen Tirante.",
      "body": [
        "Die Nitto ATP Finals 2026 begannen am Sonntag, 15. November, in der Inalpi Arena in Turin mit einem soliden Auftaktsieg der Nummer eins der Welt: Alexander Zverev bezwang den spanischen Debuetanten Rafael Jodar mit 6:4, 6:4 in der John McEnroe-Gruppe. Zverev servierte ueber 87 Minuten souveraen und gab bei eigenem ersten Aufschlag nur sieben Punkte ab.",
        "In der Abendsession von Turin trifft Ben Shelton auf Arthur Fils, den ersten franzoesischen Starter bei den ATP Finals seit zehn Jahren. Die Ivan Lendl-Gruppe greift am Montag mit Carlos Alcaraz gegen Frances Tiafoe und Daniil Medvedev gegen Flavio Cobolli ins Geschehen ein.",
        "Am Samstag hatte Taylor Fritz das Stockholm Open-Finale gewonnen: Gegen den Kaempfer Thiago Agustin Tirante setzte sich der topgesetzte US-Amerikaner nach hartem Kampf mit 6:2, 4:6, 7:6 (3) im entscheidenden Tiebreak durch."
      ]
    },
    "it": {
      "title": "Zverev apre Torino battendo Jodar in due set; Fritz piega Tirante a Stoccolma",
      "subtitle": "Il numero uno Alexander Zverev regola Rafael Jodar 6-4, 6-4 nel gruppo McEnroe, mentre Taylor Fritz vince 6-2, 4-6, 7-6 (3) la finale svedese.",
      "excerpt": "Torino apre domenica: Zverev batte Jodar 6-4, 6-4 in 87 minuti; stasera Shelton contro Fils. A Stoccolma, Fritz vince il titolo al tiebreak su Tirante.",
      "body": [
        "Le Nitto ATP Finals 2026 sono scattate domenica 15 novembre all'Inalpi Arena di Torino con il successo del numero uno mondiale Alexander Zverev sullo spagnolo Rafael Jodar per 6-4, 6-4 nel gruppo John McEnroe. Il tedesco ha dominato al servizio per 87 minuti, concedendo appena sette punti sulla prima palla.",
        "La sessione serale torinese propone la sfida tra Ben Shelton e il francese Arthur Fils. Lunedi scattera il gruppo Ivan Lendl con l'esordio di Carlos Alcaraz contro Frances Tiafoe e Daniil Medvedev opposto all'azzurro Flavio Cobolli.",
        "Sabato a Stoccolma il titolo e andato a Taylor Fritz, che ha superato l'argentino Thiago Agustin Tirante per 6-2, 4-6, 7-6 (3) al termine di una splendida battaglia risolta al tiebreak decisivo."
      ]
    },
    "pl": {
      "title": "Zverev otwiera Turyn wygrana z Jodarem; Fritz zdobywa tytul w Sztokholmie",
      "subtitle": "Lider rankingu Alexander Zverev pokonuje Rafaela Jodara 6:4, 6:4 w grupie McEnroe, a Taylor Fritz wygrywa 6:2, 4:6, 7:6 (3) w Szwecji.",
      "excerpt": "Turyn startuje w niedziele: Zverev pokonuje Jodara 6:4, 6:4 w 87 minut; wieczorem Shelton kontra Fils. W Sztokholmie Fritz wygrywa tytul po tiebreaku z Tirante.",
      "body": [
        "Turniej Nitto ATP Finals 2026 rozpoczal sie w niedziele 15 listopada w Inalpi Arena w Turynie od pewnego zwyciestwa lidera rankingu Alexandra Zvereva nad Rafaelem Jodarem 6:4, 6:4 w grupie Johna McEnroe. Niemiec serwowal znakomicie przez 87 minut, tracac tylko siedem punktow po pierwszym podaniu.",
        "W sesji wieczornej Ben Shelton zmierzy sie z Arthurem Filsem. Grupa Ivana Lendla rozpocznie zmagania w poniedzialek grami Carlosa Alcaraza z Francesem Tiafoe oraz Daniila Miedwiediewa z Flavio Cobollim.",
        "W sobote w Sztokholmie Taylor Fritz siegnal po tytul, pokonujac w finale Thiago Agustina Tirante 6:2, 4:6, 7:6 (3). Amerykanin rozstrzygnal zaciety pojedynek na swoja korzysc w decydujacym tiebreaku."
      ]
    },
    "zh": {
      "title": "兹维列夫都灵直落两盘击退霍达尔；弗里茨险胜蒂兰特斯德哥尔摩加冕",
      "subtitle": "世界第一兹维列夫在麦肯罗组6-4、6-4完胜新星霍达尔，弗里茨在瑞典决胜盘抢七6-2、4-6、7-6（3）力克阿根廷黑马。",
      "excerpt": "ATP年终总决赛周日都灵揭幕：兹维列夫87分钟6-4、6-4轻取霍达尔；今晚谢尔顿迎战菲斯。斯德哥尔摩决赛弗里茨险胜蒂兰特夺冠。",
      "body": [
        "2026年Nitto ATP年终总决赛于11月15日周日在意大利都灵伊纳尔皮竞技场挥拍。世界第一亚历山大·兹维列夫在约翰·麦肯罗组首轮较量中，耗时87分钟以6-4、6-4直落两盘击败西班牙年轻小将拉斐尔·霍达尔。德国名将全场一发仅丢7分，两盘各完成一次破发顺利取得开门红。",
        "都灵晚场将上演美国好手本·谢尔顿与法国新星阿瑟·菲斯的对决。伊万·伦德尔组将于周一开打，二号种子卡洛斯·阿尔卡拉斯将对阵弗朗西斯·蒂亚福，丹尼尔·梅德韦杰夫则遭遇弗拉维奥·科博利。",
        "周六在瑞典斯德哥尔摩公开赛男单决赛中，头号种子泰勒·弗里茨与阿根廷黑马蒂亚戈·阿古斯汀·蒂兰特激战三盘，最终弗里茨在决胜盘抢七发挥沉稳，以6-2、4-6、7-6（3）险胜夺魁。"
      ]
    },
    "ja": {
      "title": "ズベレフがジョダルをストレートで下しトリノ白星発進；フリッツがストックホルム制覇",
      "subtitle": "世界1位ズベレフがマッケンロー組でジョダルに6-4、6-4で完勝。スウェーデンではフリッツが6-2、4-6、7-6（3）でティランテを下し優勝。",
      "excerpt": "日曜日トリノ開幕：ズベレフがジョダルを87分で6-4、6-4で退ける；今夜シェルトン対フィス。ストックホルム決勝はフリッツが激闘を制す。",
      "body": [
        "2026年Nitto ATPファイナルズが11月15日日曜日、トリノのイナルピ・アリーナで開幕。世界ランク1位のアレクサンダー・ズベレフがジョン・マッケンロー組の初戦でスペインの若手ラファエル・ジョダルを6-4、6-4のストレートで下した。ズベレフは87分間でファーストサーブ時の失点をわずか7点に抑える完璧な立ち上がりを見せた。",
        "今夜のトリノ夜のセッションではベン・シェルトンとフランスのアントワーヌ・フィスが激突する。イワン・レンドル組は月曜日にカルロス・アルカラス対フランシス・ティアフォー、ダニール・メドベージェフ対フラビオ・コボッリの顔合わせで幕を開ける。",
        "土曜日のストックホルム・オープン決勝では第1シードのテイラー・フリッツがアルゼンチンのチアゴ・アグスティン・ティランテを6-2、4-6、7-6（3）で破り、最終セットタイブレークの末にタイトルを獲得した。"
      ]
    },
    "ko": {
      "title": "즈베레프 호다르 꺾고 토리노 산뜻한 출발; 프리츠 스톡홀름 결승 극적 우승",
      "subtitle": "세계 1위 알렉산더 즈베레프가 매켄로 그룹에서 6-4, 6-4 완승을 거두었고, 테일러 프리츠는 6-2, 4-6, 7-6(3) 타이브레이크 끝에 스웨덴 정상을 밟았습니다.",
      "excerpt": "일요일 토리노 개막: 즈베레프 호다르에 87분 만에 6-4, 6-4 승리; 오늘 밤 셸턴 vs 피스. 스톡홀름에서는 프리츠가 티란테를 꺾고 우승.",
      "body": [
        "2026 니토 ATP 파이널스가 11월 15일 일요일 이탈리아 토리노 이날피 아레나에서 막을 올렸습니다. 세계 1위 알렉산더 즈베레프는 존 매켄로 그룹 1차전에서 스페인의 신예 라파엘 호다르를 87분 만에 6-4, 6-4로 제압했습니다. 즈베레프는 첫 서브 시 단 7점만을 내주는 완벽한 서브 게임을 선보였습니다.",
        "토리노 야간 세션에서는 벤 셸턴과 프랑스의 아르튀르 피스가 맞대결을 펼칩니다. 이반 렌들 그룹은 월요일 카를로스 알카라스 vs 프랜시스 티아포, 다닐 메드베데프 vs 플라비오 코볼리의 대진으로 시작됩니다.",
        "앞서 토요일 스톡홀름 오픈 결승에서는 톱시드 테일러 프리츠가 아르헨티나의 돌풍 티아고 아구스틴 티란테와 3세트 접전 끝에 6-2, 4-6, 7-6(3) 타이브레이크 승리를 거두고 우승 트로피를 차지했습니다."
      ]
    },
    "ar": {
      "title": "زفيريف يفتتح تورينو بالفوز على خودار بمجموعتين؛ وفريتز يحسم لقب ستوكهولم بشق الأنفس",
      "subtitle": "المصنف الأول عالمياً ألكسندر زفيريف يتغلب على رافاييل خودار 6-4 و6-4 في مجموعة ماكنرو، بينما تايلور فريتز يتوج بلقب السويد 6-2 و4-6 و7-6 (3).",
      "excerpt": "تورينو تفتتح الأحد: زفيريف يهزم خودار 6-4 و6-4 في 87 دقيقة؛ شيلتون ضد فيلس الليلة. وفي ستوكهولم فريتز يخطف اللقب بكسر التعادل أمام تيرانتي.",
      "body": [
        "انطلقت نهائيات نيتو ATP لعام 2026 يوم الأحد 15 نوفمبر في إينالبي أرينا بتورينو بفوز المصنف الأول ألكسندر زفيريف على الشاب الإسباني رافاييل خودار 6-4 و6-4 في افتتاح مجموعة جون ماكنرو. وقدم الألماني عرضاً إرسالياً قوياً عبر 87 دقيقة خسر خلالها سبع نقاط فقط على إرساله الأول.",
        "وتشهد الفترة المسائية في تورينو مواجهة قوية بين الأمريكي بن شيلتون والفرنسي آرثر فيلس. بينما تبدأ منافسات مجموعة إيفان ليندل يوم الاثنين بلقاء كارلوس ألكاراز مع فرانسيس تيافو ودانييل ميدفيديف مع فلافيو كوبولي.",
        "ويوم السبت في السويد، حسم تايلور فريتز لقب بطولة ستوكهولم المفتوحة بفوزه المثير على الأرجنتيني تياغو أغوستين تيرانتي بنتيجة 6-2 و4-6 و7-6 (3) بعد شوط كسر تعادل حاسم."
      ]
    }
  },

  "nations-league-spain-england-metropolitano-denmark-stun-portugal-2026": {
    "fr": {
      "title": "L'Espagne recoit l'Angleterre au Metropolitano ; le Danemark ecrase le Portugal 4-1",
      "subtitle": "La Roja n'a besoin que d'un point a Madrid pour remporter le groupe A3, alors que l'Angleterre de Thomas Tuchel vise l'exploit apres la defaite portugaise a Lisbonne.",
      "excerpt": "Ligue des nations dimanche : Espagne-Angleterre debute a 19h45 GMT au Metropolitano. Samedi : le Danemark gifle le Portugal 4-1 ; la Suede bat la Bosnie 3-2.",
      "body": [
        "Le choc au sommet du football europeen se deroule dimanche soir 15 novembre au Riyadh Air Metropolitano de Madrid (19h45 GMT) entre l'Espagne et l'Angleterre pour la premiere place du groupe A3 de la Ligue des nations. En tete avec 13 points, la Roja de Luis de la Fuente n'a besoin que d'un match nul a domicile pour s'assurer le statut de tete de serie en quarts de finale.",
        "L'Angleterre de Thomas Tuchel aborde ce deplacement perilleux avec la volonte de frapper un grand coup, portee par sa victoire 2-1 contre la Croatie a Wembley jeudi grace au penalty de Harry Kane pour sa 126e selection. Les 68 000 spectateurs madrilenes attendent un duel d'une intensite rare.",
        "Samedi soir, le Danemark a cree la surprise en dominant outrageusement le Portugal 4-1 a Lisbonne dans la Ligue A, tandis que la Suede dominait la Bosnie 3-2. En club, Arsenal conserve cinq longueurs d'avance en tete de Premier League."
      ]
    },
    "es": {
      "title": "Espana recibe a Inglaterra en el Metropolitano; Dinamarca sorprende a Portugal 4-1",
      "subtitle": "La Roja solo necesita un empate en Madrid para liderar el grupo A3, mientras la Inglaterra de Thomas Tuchel busca el asalto tras la debacle lusa en Lisboa.",
      "excerpt": "Nations League domingo: Espana vs Inglaterra arranca a las 19:45 GMT en el Metropolitano. Sabado: Dinamarca golea 4-1 a Portugal; Suecia supera 3-2 a Bosnia.",
      "body": [
        "El gran duelo del futbol europeo se juega este domingo 15 de noviembre en el Riyadh Air Metropolitano de Madrid (19:45 GMT) entre Espana e Inglaterra por el liderato definitivo del grupo A3 de la UEFA Nations League. El equipo de Luis de la Fuente lidera con 13 puntos y le basta un empate en casa para garantizar la primera plaza y ser cabeza de serie.",
        "La Inglaterra de Thomas Tuchel llega con 12 puntos tras ganar 2-1 a Croacia el jueves en Wembley, con Harry Kane transformando un penal crucial en su internacionalidad 126. Ambos conjuntos reeditaran la final de la Eurocopa 2024 ante mas de 68.000 aficionados.",
        "En la jornada del sabado, Dinamarca dio la gran campanada al vencer 4-1 a Portugal en Lisboa en el Grupo 4 de la Liga A, mientras Suecia se impuso 3-2 a Bosnia. En la Premier League, el Arsenal se mantiene cinco puntos arriba durante el paron."
      ]
    },
    "de": {
      "title": "Spanien empfaengt England im Metropolitano; Daenemark ueberrascht Portugal mit 4:1",
      "subtitle": "La Roja reicht in Madrid ein Zaehler fuer Platz eins in Gruppe A3, waehrend Thomas Tuchels Three Lions nach Portugals Pleite auf den Sieg hoffen.",
      "excerpt": "Nations League am Sonntag: Spanien vs. England ab 19:45 GMT im Metropolitano. Samstag: Daenemark demuetigt Portugal 4:1; Schweden siegt 3:2 gegen Bosnien.",
      "body": [
        "Europas Top-Laenderspiel steigt am Sonntagabend, 15. November, im Riyadh Air Metropolitano in Madrid (19:45 GMT): Spanien kaempft gegen England um den Gruppensieg in der Nations League A3. Den Iberern unter Luis de la Fuente reicht dank 13 Punkten bereits ein Unentschieden fuer Platz eins und das Viertelfinal-Heimrecht.",
        "England und Trainer Thomas Tuchel reisen nach dem 2:1-Erfolg ueber Kroatien am Donnerstag nach Madrid, bei dem Harry Kane bei seinem 126. Laenderspiel einen Foulelfmeter verwandelte. Vor 68.000 Zuschauern wollen die Gaeste die Revanche fuer das EM-Finale von 2024 suchen.",
        "Am Samstag hatte Daenemark fuer das Resultat des Wochenendes gesorgt und Portugal in Lissabon mit 4:1 deklassiert. Schweden bezwang Bosnien mit 3:2, waehrend der FC Arsenal in der Premier League mit fuenf Punkten Vorsprung an der Spitze ueberwintert."
      ]
    },
    "it": {
      "title": "Spagna contro Inghilterra al Metropolitano; Danimarca travolge il Portogallo 4-1",
      "subtitle": "Alle Furie Rosse basta un punto a Madrid per vincere il girone A3, mentre l'Inghilterra di Thomas Tuchel cerca il colpo esterno dopo il crollo lusitano.",
      "excerpt": "Nations League domenica: Spagna-Inghilterra alle 19:45 GMT al Metropolitano. Sabato: Danimarca show 4-1 sul Portogallo; Svezia batte Bosnia 3-2.",
      "body": [
        "La grande classica del calcio europeo va in scena domenica sera 15 novembre al Riyadh Air Metropolitano di Madrid (19:45 GMT): Spagna e Inghilterra si contendono il primato nel gruppo A3 della Nations League. La squadra di Luis de la Fuente, prima a 13 punti, sara testa di serie nei quarti di primavera anche con un semplice pareggio.",
        "L'Inghilterra guidata da Thomas Tuchel e seconda a quota 12 dopo il 2-1 rifilato alla Croazia a Wembley grazie al rigore di Harry Kane alla 126a presenza. Davanti a 68.000 spettatori gli inglesi cercano il blitz per ribaltare l'esito della finale di Euro 2024.",
        "Sabato la Danimarca ha firmato la sorpresa della giornata travolgendo 4-1 il Portogallo a Lisbona nella Lega A, mentre la Svezia ha superato 3-2 la Bosnia. In Premier League l'Arsenal guida sempre con cinque lunghezze di vantaggio."
      ]
    },
    "pl": {
      "title": "Hiszpania podejmuje Anglie na Metropolitano; Dania szokuje Portugalia 4:1",
      "subtitle": "La Roja potrzebuje remisu w Madrycie by wygrac grupe A3, podczas gdy ekipa Thomasa Tuchela walczy o triumf po pogromie Portugalii w Lizbonie.",
      "excerpt": "Liga Narodow w niedziele: Hiszpania vs Anglia o 19:45 GMT na Metropolitano. W sobote Dania gromi Portugalie 4:1; Szwecja pokonuje Bosnie 3:2.",
      "body": [
        "Wielki hit reprezentacyjnej jesieni odbedzie sie w niedziele wieczorem 15 listopada na Riyadh Air Metropolitano w Madrycie (19:45 GMT). Hiszpania i Anglia zagraja o pierwsze miejsce w grupie A3 Ligi Narodow. Gospodarzom z 13 punktami na koncie wystarcza remis do rozstawienia w cwiercfinalach.",
        "Prowadzona przez Thomasa Tuchela Anglia ma 12 punktow po czwartkowym 2:1 z Chorwacja na Wembley, gdzie Harry Kane trafil z rzutu karnego w swoim 126. wystepie w kadrze. Rewanz za final Euro 2024 zapowiada wielkie emocje przed 68 tysiacami kibicow.",
        "W sobote Dania sprawila ogromna niespodzianke, rozbijajac Portugalie 4:1 w Lizbonie, a Szwecja wygrala 3:2 z Bosnia i Hercegowina. W Premier League Arsenal wciaz ma piec punktow przewagi."
      ]
    },
    "zh": {
      "title": "西班牙大都会球场决战英格兰；丹麦客场4-1重创葡萄牙",
      "subtitle": "斗牛士军团在马德里仅需一场平局即可锁定A3组头名，图赫尔率领的三狮军团力图在丹麦客场大胜葡萄牙后上演客场逆转。",
      "excerpt": "欧国联周日焦点战：西班牙对英格兰晚间19:45在马德里大都会球场打响。周六赛况：丹麦4-1客场大胜葡萄牙；瑞典3-2险胜波黑。",
      "body": [
        "欧洲足坛焦点大战于11月15日周日晚在马德里利雅得航空大都会球场打响（格林尼治时间19:45），西班牙与英格兰直接对话争夺欧国联A3组榜首。路易斯·德拉富恩特率领的欧洲冠军目前积13分领跑，坐镇主场只要取得平局即可锁定明年春季八强战的种子席位。",
        "托马斯·图赫尔执掌的三狮军团积12分紧随其后。周四英格兰在温布利2-1力克斯罗地亚，凯恩在个人第126场里程碑之役罚入制胜点球。此番面对2024年欧洲杯决赛对手，客队将在6.8万名马德里球迷面前全力争胜。",
        "周六欧国联爆出最大冷门，丹麦在里斯本反客为主以4-1痛击葡萄牙，瑞典则在B级联赛3-2击退波黑。英超俱乐部赛事暂歇，阿森纳以5分优势继续领跑积分榜。"
      ]
    },
    "ja": {
      "title": "スペインが本拠メトロポリターノでイングランドと決戦；デンマークがポルトガルを4-1撃破",
      "subtitle": "無敵艦隊は引き分け以上でA3組首位確定、トゥヘル監督率いるイングランドはリスボンでのポルトガル大敗の翌日に敵地勝利を狙う。",
      "excerpt": "UEFAネーションズリーグ日曜決戦：スペイン対イングランドはメトロポリターノで19:45 GMTキックオフ。土曜はデンマークがポルトガルに4-1圧勝。",
      "body": [
        "欧州最強国同士の頂上対決が11月15日日曜夜、マドリードのリヤド・エア・メトロポリターノ（19:45 GMT）で開催。UEFAネーションズリーグ・リーグA3組の首位突破を懸けてスペインとイングランドが激突する。勝ち点13のスペインは本拠地で引き分け以上なら準々決勝シードを獲得する。",
        "勝ち点12のイングランドは敵地での勝利のみが逆転首位への条件。木曜にウェンブリーでクロアチアを2-1で下し、ケインが代表126試合目で決勝PKを決めた。EURO2024決勝の再戦はマドリードの6万8000人の大観衆を熱狂させる。",
        "土曜のネーションズリーグではデンマークがリスボンでポルトガルを4-1で粉砕する大波乱を演出。スウェーデンはボスニアに3-2で辛勝した。プレミアリーグはアーセナルが首位を堅持している。"
      ]
    },
    "ko": {
      "title": "스페인 메트로폴리타노서 잉글랜드와 A3조 최종 결전; 덴마크 포르투갈 4-1 완파",
      "subtitle": "스페인은 마드리드에서 무승부만 거둬도 조 1위를 확정하며, 토마스 투헬 감독의 잉글랜드는 리스본 대이변 속에 역전 1위를 정조준합니다.",
      "excerpt": "네이션스리그 일요일: 스페인 vs 잉글랜드 메트로폴리타노서 19:45 GMT 킥오프. 토요일 덴마크 포르투갈 4-1 완파, 스웨덴 보스니아 3-2 제압.",
      "body": [
        "유럽 축구의 최정상 격돌이 11월 15일 일요일 밤 마드리드 리야드 에어 메트로폴리타노(19:45 GMT)에서 펼쳐집니다. UEFA 네이션스리그 리그A 3조 1위를 놓고 스페인과 잉글랜드가 맞붙습니다. 승점 13점의 스페인은 안방에서 무승부만 기록해도 8강 시드를 확보합니다.",
        "승점 12점의 잉글랜드는 반드시 승리해야 1위를 탈환할 수 있습니다. 목요일 웸블리에서 해리 케인의 126번째 A매치 기념 결승 페널티킥으로 크로아티아를 2-1로 꺾은 잉글랜드는 유로 2024 결승전의 리턴매치에서 총력전을 다짐하고 있습니다.",
        "전날 토요일에는 덴마크가 리스본 원정에서 포르투갈을 4-1로 대파하는 이변을 연출했으며, 스웨덴은 보스니아를 3-2로 꺾었습니다. 프리미어리그는 아스널이 승점 5점 차 선두를 달리는 가운데 휴식기를 이어가고 있습니다."
      ]
    },
    "ar": {
      "title": "إسبانيا تستضيف إنجلترا في حسم ميتروبوليتانو؛ والدنمارك تصدم البرتغال 4-1",
      "subtitle": "لا روخا بحاجة لنقطة واحدة في مدريد لضمان صدارة المجموعة A3، بينما يسعى منتخب إنجلترا بقيادة توخيل للانتصار بعد سقوط البرتغال في لشبونة.",
      "excerpt": "دوري الأمم الأحد: إسبانيا ضد إنجلترا تنطلق في 19:45 بتوقيت غرينتش في ميتروبوليتانو. السبت: الدنمارك تسحق البرتغال 4-1 والسويد تهزم البوسنة 3-2.",
      "body": [
        "تتجه أنظار كرة القدم العالمية مساء الأحد 15 نوفمبر نحو ملعب الرياض إير ميتروبوليتانو في مدريد (19:45 غرينتش)، حيث تستضيف إسبانيا نظيرتها إنجلترا لتحديد متصدر المجموعة A3 لدوري الأمم الأوروبية. وتدخل إسبانيا اللقاء في الصدارة بـ13 نقطة ويكفيها التعادل لضمان التصنيف الأول في ربع النهائي.",
        "في المقابل، تدخل إنجلترا بقيادة مدربها الجديد توماس توخيل وفي جعبتها 12 نقطة بعد الفوز الصعب على كرواتيا 2-1 في ويمبلي بفضل ركلة جزاء هاري كين في مباراته الدولية رقم 126. وتتكرر مواجهة نهائي يورو 2024 أمام أكثر من 68 ألف متفرج.",
        "ويوم السبت، فجرت الدنمارك مفاجأة مدوية باكتساح البرتغال 4-1 في لشبونة، بينما تجاوزت السويد البوسنة 3-2. وفي إنجلترا يواصل أرسنال تصدر الدوري بفارق خمس نقاط خلال فترة التوقف الدولي."
      ]
    }
  },

  "nfl-munich-lions-lead-patriots-maye-hurt-allianz-arena-2026": {
    "fr": {
      "title": "Les Lions menent 21-3 a Munich contre les Patriots ; Drake Maye touche a la cheville",
      "subtitle": "L'attaque de Detroit marque trois touchdowns en premiere mi-temps a l'Allianz Arena, alors que le rookie de New England quitte le terrain apres un sack de Hutchinson.",
      "excerpt": "Match NFL a Munich en direct : Detroit mene 21-3 face a New England. Touchdowns de St. Brown, TeSlaa et Gibbs ; Maye blesse a la cheville. Match en cours.",
      "body": [
        "La serie internationale de la NFL a pose ses valises en Allemagne dimanche 15 novembre a l'Allianz Arena de Munich, ou les Detroit Lions ont pris les devants face aux New England Patriots avec un avantage de 21-3 a la pause devant plus de 70 000 spectateurs.",
        "Coup dur pour New England des le premier quart-temps : le quarterback rookie Drake Maye a ete victime d'une blessure a la cheville gauche sur un sack d'Aidan Hutchinson et a ete contraint de declarer forfait, laissant la place a Tommy DeVito. Les Patriots n'ont inscrit qu'un field goal de 33 yards par Andy Borregales.",
        "Detroit a capitalise avec une passe de touchdown de 56 yards de Jared Goff pour Amon-Ra St. Brown, une passe de 12 yards pour Isaac TeSlaa et une course de 5 yards de Jahmyr Gibbs. La seconde periode est actuellement en cours a Munich avant la suite de la 10e semaine ce soir."
      ]
    },
    "es": {
      "title": "Lions toman ventaja 21-3 en Munich ante Patriots; Drake Maye lesionado del tobillo",
      "subtitle": "El ataque de Detroit anota tres touchdowns en la primera mitad en el Allianz Arena, mientras el mariscal novato de Nueva Inglaterra sale lesionado tras un sack de Hutchinson.",
      "excerpt": "NFL en Munich en vivo: Lions superan 21-3 a Patriots en la segunda mitad. Touchdowns de St. Brown, TeSlaa y Gibbs; Maye baja por tobillo. Partido en juego.",
      "body": [
        "El partido internacional de la Semana 10 de la NFL aterrizo este domingo 15 de noviembre en el Allianz Arena de Munich, donde los Detroit Lions dominaron la primera parte para irse al descanso arriba 21-3 frente a los New England Patriots ante un lleno absoluto.",
        "Nueva Inglaterra sufrio un golpe critico en el primer cuarto cuando su quarterback titular Drake Maye sufrio una lesion en el tobillo izquierdo al ser capturado por Aidan Hutchinson, quedando fuera del encuentro y cediendo los controles a Tommy DeVito. Los Pats solo sumaron un gol de campo de 33 yardas de Andy Borregales.",
        "Detroit capitalizo con un pase de anotacion de 56 yardas de Jared Goff a Amon-Ra St. Brown, un envio de 12 yardas a Isaac TeSlaa y un acarreo de 5 yardas de Jahmyr Gibbs. El segundo tiempo se disputa actualmente en Alemania."
      ]
    },
    "de": {
      "title": "Lions fuehren in Muenchen mit 21:3 gegen Patriots; Drake Maye verletzt am Knoechel",
      "subtitle": "Detroits Offensive glaenzt mit drei Touchdowns in der ersten Halbzeit in der Allianz Arena, waehrend New Englands Rookie-Quarterback nach Hutchinson-Sack raus muss.",
      "excerpt": "NFL Munich Game live: Detroit Lions fuehren 21:3 gegen New England Patriots. Touchdowns durch St. Brown, TeSlaa und Gibbs; Maye verletzt. Zweite Halbzeit laeuft.",
      "body": [
        "Die NFL Week 10 International Series machte am Sonntag, 15. November, in Deutschland Station: In der ausverkauften Muenchner Allianz Arena dominierten die Detroit Lions die New England Patriots und fuehren zur Halbzeit souveraen mit 21:3.",
        "Bitterer Rueckschlag fuer die Patriots im ersten Viertel: Rookie-Quarterback Drake Maye verletzte sich bei einem Sack von Aidan Hutchinson am linken Knoechel und musste das Spiel vorzeitig beenden. Backup Tommy DeVito uebernahm. New England erzielte lediglich ein 33-Yard-Field-Goal durch Andy Borregales.",
        "Die Lions schlugen eiskalt zu: Jared Goff bediente Amon-Ra St. Brown per 56-Yard-Touchdown-Pass und Isaac TeSlaa ueber 12 Yards, ehe Jahmyr Gibbs aus fuenf Yards in die Endzone stuermte. Die zweite Halbzeit laeuft derzeit in Muenchen."
      ]
    },
    "it": {
      "title": "Lions avanti 21-3 a Monaco sui Patriots; Drake Maye ko alla caviglia",
      "subtitle": "L'attacco di Detroit vola con tre touchdown all'Allianz Arena, mentre il quarterback rookie dei Patriots e costretto a uscire dopo un sack di Hutchinson.",
      "excerpt": "NFL Munich Game live: Detroit Lions conducono 21-3 sui New England Patriots nel secondo tempo. Touchdown di St. Brown, TeSlaa e Gibbs; Maye infortunato.",
      "body": [
        "La serie internazionale NFL della Week 10 e sbarcata in Germania domenica 15 novembre all'Allianz Arena di Monaco, con i Detroit Lions padroni del campo capaci di chiudere il primo tempo avanti 21-3 sui New England Patriots davanti a oltre 70.000 spettatori.",
        "I Patriots hanno perso nel primo quarto il quarterback titolare Drake Maye, infortunatosi alla caviglia sinistra su un sack di Aidan Hutchinson e costretto ad abbandonare la gara, lasciando spazio a Tommy DeVito. Per New England solo un field goal da 33 yard di Andy Borregales.",
        "Detroit ha risposto con la bomba da 56 yard di Jared Goff per Amon-Ra St. Brown, una ricezione vincente di 12 yard di Isaac TeSlaa e la corsa da 5 yard di Jahmyr Gibbs. La ripresa e attualmente in corso in Germania."
      ]
    },
    "pl": {
      "title": "Lions prowadza w Monachium 21:3 z Patriots; Drake Maye z kontuzja kostki",
      "subtitle": "Ofensywa Detroit zdobywa trzy przylozenia w pierwszej polowie na Allianz Arena, a debiutujacy rozgrywajacy New England schodzi z boiska po sacku Hutchinsona.",
      "excerpt": "Mecz NFL w Monachium na zywo: Detroit Lions prowadza 21:3 z New England Patriots. Przylozenia St. Browna, TeSlaa i Gibbsa; Maye kontuzjowany.",
      "body": [
        "Miedzynarodowy mecz 10. tygodnia NFL odbyl sie w niedziele 15 listopada na Allianz Arena w Monachium. Detroit Lions zdominowali pierwsza polowe, prowadzac 21:3 z New England Patriots przy dopingu ponad 70 tysiecy kibicow.",
        "Patriots spotkalo nieszczescie juz w pierwszej kwarcie, gdy rozgrywajacy Drake Maye doznal urazu lewej kostki po sacku Aidana Hutchinsona i opuscil boisko. Zastepuje go Tommy DeVito, a jedyne punkty dla ekipy z Foxborough zdobyl kopacz Andy Borregales z 33 jardow.",
        "Detroit odpowiedzialo 56-jardowym podaniem Jareda Goffa do Amon-Ra St. Browna, 12-jardowym chwytem Isaaca TeSlaa oraz 5-jardowym biegiem Jahmyra Gibbsa. Mecz trwa w najlepsze w Monachium."
      ]
    },
    "zh": {
      "title": "底特律雄狮慕尼黑赛半场21-3领先爱国者；梅耶脚踝受伤退场",
      "subtitle": "雄狮进攻组在安联球场上半场完成三次达阵，新英格兰爱国者新秀四分卫遭哈钦森擒杀后因伤离场退赛。",
      "excerpt": "NFL慕尼黑赛直播进行中：雄狮半场21-3领先爱国者。圣布朗、特斯拉与吉布斯相继达阵；梅耶伤退，第二半场激战中。",
      "body": [
        "NFL第10周国际系列赛于11月15日周日登陆德国慕尼黑安联球场。底特律雄狮上半场展现强劲火力，在逾7万名狂热球迷面前以21-3确立对新英格兰爱国者的明显优势。",
        "爱国者在首节遭遇重创：主力新秀四分卫德雷克·梅耶在第三档进攻中遭遇艾丹·哈钦森擒杀，导致左脚踝受伤被搀扶回更衣室并确认退赛，替补四分卫汤米·德维托披挂上阵。爱国者上半场仅靠博雷加莱斯的33码任意球拿下3分。",
        "雄狮抓住机会多点开花：四分卫高夫先后完成连线圣布朗的56码超远达阵传球和特斯拉的12码接球达阵，跑卫吉布斯随后完成5码冲球达阵。目前下半场比赛正在慕尼黑进行中。"
      ]
    },
    "ja": {
      "title": "ライオンズがミュンヘンでペイトリオッツに21-3リード；メイが足首負傷退場",
      "subtitle": "デトロイトがアリアンツ・アレーナの前半で3TDを奪取、ニューイングランドの新人QBメイはハッチンソンのサックで無念の負傷交代。",
      "excerpt": "NFLミュンヘンゲーム生中継：ライオンズが21-3でペイトリオッツをリード。セントブラウン、テスラー、ギブスがTD；後半進行中。",
      "body": [
        "NFL第10週のインターナショナルゲームが11月15日日曜日、ドイツのアリアンツ・アレーナで開催され、デトロイト・ライオンズがニューイングランド・ペイトリオッツを相手に前半21-3の大量リードを奪った。",
        "ペイトリオッツは第1クォーターにエース新人QBドレイク・メイがエイダン・ハッチンソンのサックを受けて左足首を負傷、ロッカーへ下がり退場となった。急遽トミー・デビートが登板したが、前半はボレガレスの33ヤードFGによる3点にとどまった。",
        "ライオンズはゴフがセントブラウンへ56ヤードのロングTDパス、テスラーへ12ヤードTDを成功させ、ギブスが5ヤードを走り切って3TD。現在ミュンヘンで後半の熱戦が続いている。"
      ]
    },
    "ko": {
      "title": "라이언스 뮌헨 경기서 패트리어츠에 전반 21-3 리드; 메이 발목 부상 이탈",
      "subtitle": "디트로이트가 알리안츠 아레나에서 전반에만 3개의 터치다운을 터뜨렸고, 뉴잉글랜드 신인 쿼터백 메이는 허친슨의 색 이후 경기에서 빠졌습니다.",
      "excerpt": "NFL 뮌헨 경기 생중계: 라이언스가 패트리어츠에 21-3 리드. 세인트브라운, 테슬라, 깁스 TD; 메이 부상 교체, 후반 진행 중.",
      "body": [
        "NFL 10주차 인터내셔널 경기가 11월 15일 일요일 독일 뮌헨 알리안츠 아레나에서 열린 가운데, 디트로이트 라이언스가 전반전을 21-3으로 앞선 채 마쳤습니다.",
        "뉴잉글랜드는 1쿼터에 주전 쿼터백 드레이크 메이가 에이든 허친슨에게 색을 당하며 왼쪽 발목을 다쳐 경기장을 떠나는 악재를 맞았습니다. 토미 드비토가 긴급 투입되었으나 안드레스 보레갈레스의 33야드 필드골 3점에 그쳤습니다.",
        "반면 디트로이트는 제러드 고프가 아몬-라 세인트브라운에게 56야드 터치다운 패스를 연결하고 아이작 테슬라에게 12야드 패스, 자미어 깁스의 5야드 러싱 TD를 더해 격차를 벌렸습니다. 현재 뮌헨에서 후반전이 진행 중입니다."
      ]
    },
    "ar": {
      "title": "لايونز يتقدمون 21-3 في ميونخ على باتريوتس؛ وإصابة دريك ماي في الكاحل",
      "subtitle": "هجوم ديترويت يسجل ثلاثة أهداف في الشوط الأول بأليانز أرينا، بينما يغادر لاعب نيو إنجلاند بعد إسقاط قوي من هتشينسون.",
      "excerpt": "مباراة NFL في ميونخ مباشرة: لايونز يتقدمون 21-3 على باتريوتس. أهداف لسانت براون وتيسلا وغيبس؛ وخروج ماي مصاباً. اللقاء مستمر.",
      "body": [
        "حطت سلسلة مباريات NFL الدولية للأسبوع العاشر رحالها في ألمانيا الأحد 15 نوفمبر على ملعب أليانز أرينا في ميونخ، حيث بسط ديترويت لايونز سيطرته لينهي الشوط الأول متقدماً 21-3 على نيو إنجلاند باتريوتس أمام مدرجات ممتلئة بأكثر من 70 ألف مشجع.",
        "وتلقت آمال نيو إنجلاند ضربة موجعة في الربع الأول بعد إصابة الظهير الربعي الشاب دريك ماي في كاحله الأيسر إثر تدخل قوي من إيدان هتشينسون ليخرج رسمياً من اللقاء ويدخل بديله تومي ديفيتو، بينما اكتفى الفريق بثلاث نقاط من ركلة أندي بوريغالس.",
        "واستغل ديترويت الموقف بتمريرة 56 ياردة من جاريد غوف إلى آمون-را سانت براون، وتمريرة 12 ياردة لآيزاك تيسلا، وركضة خمس ياردات من جامعير غيبس. وتتواصل مجريات الشوط الثاني حالياً في ميونخ."
      ]
    }
  },

  "nba-heat-drop-pistons-cavaliers-proctor-triple-double-2026": {
    "fr": {
      "title": "Giannis marque 34 points et le Heat domine Detroit 137-117 ; Proctor signe un triple-double historique pour les Cavs",
      "subtitle": "Miami s'envole derriere Antetokounmpo et le retour a 26 points de Klay Thompson, tandis qu'une equipe bis de Cleveland surprend Dallas derriere le 24-11-10 de son rookie.",
      "excerpt": "Scores NBA de samedi : Miami ecrase Detroit 137-117 malgre 33 points de Cunningham. Les Cavaliers diminués battent Dallas 127-117 grace au triple-double de Proctor.",
      "body": [
        "Le Miami Heat a deroule un basket offensif de haute volee samedi soir 14 novembre pour surclasser les Detroit Pistons 137-117 au Kaseya Center. Giannis Antetokounmpo a guide les siens avec 34 points, 14 rebonds et 8 passes, bien epaule par Klay Thompson (26 points, sept tirs a trois points) pour son retour. Cade Cunningham a tente de repliquer avec 33 points et 8 passes pour Detroit.",
        "A Cleveland, les Cavaliers ont realise un exploit retentissant en battant les Dallas Mavericks 127-117 a la Rocket Arena malgre le repos accorde a Donovan Mitchell, James Harden et Evan Mobley. Le rookie Tyrese Proctor a creve l'ecran avec le premier triple-double de sa carriere (24 points, 11 rebonds, 10 passes), eclipsant les 34 points de Kyrie Irving.",
        "A l'Ouest, les Denver Nuggets ont domine les New Orleans Pelicans 116-108. Les San Antonio Spurs etaient eux au repos apres leur 11e victoire d'affilee signee vendredi face aux Warriors."
      ]
    },
    "es": {
      "title": "Giannis anota 34 y Heat supera 137-117 a Pistons; Proctor firma triple-doble historico con Cavs",
      "subtitle": "Miami se despega de la mano de Antetokounmpo y 26 de Klay Thompson, mientras un quinteto mermado de Cleveland sorprende a Dallas con el 24-11-10 de su novato.",
      "excerpt": "Resultados NBA del sabado: Heat arrolla 137-117 a Pistons pese a 33 de Cunningham. Cavaliers superan 127-117 a Mavericks con triple-doble de Proctor.",
      "body": [
        "Los Miami Heat brindaron una funcion anotadora el sabado 14 de noviembre al vencer 137-117 a los Detroit Pistons en el Kaseya Center. Giannis Antetokounmpo comando el triunfo con 34 puntos, 14 rebotes y 8 asistencias, mientras Klay Thompson aporto 26 tantos con 7 triples en su regreso. Por Detroit, Cade Cunningham termino con 33 unidades.",
        "En Cleveland, unos disminuidos Cavaliers dieron la sorpresa de la noche al imponerse 127-117 a los Dallas Mavericks sin Donovan Mitchell ni James Harden. El base novato Tyrese Proctor brillo con el primer triple-doble de su carrera al acumular 24 puntos, 11 rebotes y 10 asistencias, frenando los 34 tantos de Kyrie Irving.",
        "En otros partidos, los Denver Nuggets vencieron 116-108 a los New Orleans Pelicans. Los San Antonio Spurs disfrutaron de descanso tras sumar su undécima victoria consecutiva el viernes."
      ]
    },
    "de": {
      "title": "Giannis glaenzt mit 34 Punkten beim 137:117 des Heat gegen Detroit; Proctor mit historischem Triple-Double",
      "subtitle": "Miami zieht dank Antetokounmpo und Klay Thompsons 26 Punkten davon, waehrend Ersatz-Cavaliers Dallas dank Proctors 24-11-10 duespieren.",
      "excerpt": "NBA-Ergebnisse vom Samstag: Heat schlaegt Pistons 137:117 trotz 33 Cunningham-Punkten. Rumpf-Cavaliers siegen 127:117 gegen Mavericks dank Proctors Gala.",
      "body": [
        "Die Miami Heat brannten am Samstagabend, 14. November, im Kaseya Center ein Offensivfeuerwerk ab und besiegten die Detroit Pistons klar mit 137:117. Giannis Antetokounmpo fuehrte das Team mit 34 Punkten, 14 Rebounds und 8 Assists an, unterstuetzt von Klay Thompsons 26 Punkten bei sieben verwandelten Dreiern. Cade Cunningham steuerte 33 Punkte fuer Detroit bei.",
        "In Cleveland gelang den Cavaliers ein Husarenstueck: Ohne Donovan Mitchell und James Harden schlugen sie die Dallas Mavericks 127:117. Rookie Tyrese Proctor stahl allen die Show und verbuchte mit 24 Punkten, 11 Rebounds und 10 Assists sein erstes Karriere-Triple-Double gegen Kyrie Irvings 34 Punkte.",
        "Im Westen setzten sich die Denver Nuggets mit 116:108 bei den New Orleans Pelicans durch. Die San Antonio Spurs pausierten nach ihrem elften Sieg in Serie am Freitag."
      ]
    },
    "it": {
      "title": "Giannis ne mette 34 e Miami batte Detroit 137-117; Proctor da tripla doppia per i Cavs",
      "subtitle": "Gli Heat allungano con Antetokounmpo e 26 punti di Klay Thompson, mentre una Cleveland rimaneggiata stende Dallas grazie al 24-11-10 del suo rookie.",
      "excerpt": "NBA sabato: Heat a valanga sui Pistons 137-117 nonostante 33 di Cunningham. Cavaliers battono Mavericks 127-117 con tripla doppia di Proctor.",
      "body": [
        "I Miami Heat hanno offerto una grande prova offensiva sabato sera 14 novembre superando i Detroit Pistons 137-117 al Kaseya Center. Giannis Antetokounmpo ha firmato 34 punti, 14 rimbalzi e 8 assist, con Klay Thompson rientrato con 26 punti e 7 triple. A Detroit non sono bastati i 33 punti di Cade Cunningham.",
        "A Cleveland i Cavaliers hanno sorpreso i Dallas Mavericks 127-117 pur senza Mitchell e Harden. Il rookie Tyrese Proctor e stato l'eroe con la sua prima tripla doppia in carriera da 24 punti, 11 rimbalzi e 10 assist, vanificando i 34 punti di Kyrie Irving.",
        "Denver ha battuto New Orleans 116-108, mentre gli Spurs hanno riposato dopo l'undicesimo successo consecutivo centrato venerdi."
      ]
    },
    "pl": {
      "title": "Giannis rzuca 34 punkty i Heat groma Pistons 137:117; Proctor z historycznym triple-double dla Cavs",
      "subtitle": "Miami odskakuje dzieki Antetokounmpo i powrotowi Klaya Thompsona (26 pkt), a rezerwowy sklad Cleveland ogrywa Dallas po linijce 24-11-10 debiutanta.",
      "excerpt": "Sobotnie mecze NBA: Heat rozbijaja Pistons 137:117 mimo 33 punktow Cunninghama. Oslabieni Cavaliers pokonuja Mavericks 127:117 dzieki popisowi Proctora.",
      "body": [
        "Miami Heat dali popis w ofensywie w sobote 14 listopada, pokonujac Detroit Pistons 137:117 w Kaseya Center. Giannis Antetokounmpo zanotowal 34 punkty, 14 zbiorek i 8 asyst, a powracajacy Klay Thompson trafil 7 trojek zdobywajac 26 punktow. Cade Cunningham rzucil 33 punkty dla Pistons.",
        "W Cleveland rezerwowy sklad Cavaliers pokonal Dallas Mavericks 127:117 pod nieobecnosc Donovana Mitchella i Jamesa Hardena. Debiutant Tyrese Proctor zaliczyl pierwsze w karierze triple-double (24 punkty, 11 zbiorek, 10 asyst), powstrzymujac 34 punkty Kyriego Irvinga.",
        "Denver Nuggets pokonali New Orleans Pelicans 116:108, a San Antonio Spurs odpoczywali po piatkowym 11. z rzedu zwyciestwie."
      ]
    },
    "zh": {
      "title": "字母哥空砍34分热火137-117大胜活塞；普罗克特三双率残阵骑士掀翻独行侠",
      "subtitle": "阿德托昆博率热火下半场发力，克莱复出飙中7记三分轰下26分；米切尔休战骑士新秀普罗克特交出24+11+10力压欧文34分。",
      "excerpt": "NBA周六战报：热火137-117轻取活塞，康宁汉姆空砍33分；残阵骑士127-117爆冷击退独行侠，新秀普罗克特斩获生涯首个三双。",
      "body": [
        "迈阿密热火在11月14日周六晚展现恐怖进攻火力，下半场拉开比分以137-117大胜底特律活塞。字母哥扬尼斯·阿德托昆博统治内线拿下34分、14个篮板和8次助攻，伤愈复出的克莱·汤普森在外线发炮命中7记三分砍下26分。活塞核心康宁汉姆空砍33分和8次助攻未能救主。",
        "在克利夫兰，阵容严重残缺的骑士队在米切尔、哈登和莫布利休战的情况下上演惊天冷门，以127-117击败达拉斯独行侠。新秀后卫泰里斯·普罗克特打出代表作，交出24分、11个篮板和10次助攻的生涯首度三双，顶住了欧文单场34分的反扑。",
        "在西部赛场，丹佛掘金116-108力克新奥尔良鹈鹕。而携11连胜之威的圣安东尼奥马刺队在周五狂胜勇士后获得休整。"
      ]
    },
    "ja": {
      "title": "ヤニス34点でヒートがピストンズに137-117快勝；プロクターがトリプルダブルでキャブズを牽引",
      "subtitle": "アデトクンボと復帰したクレイ・トンプソンの26点でマイアミが快勝、主力欠場のキャブズは新人プロクターが24得点11リバウンド10アシストでマブス撃破。",
      "excerpt": "NBA土曜結果：ヒートがカニンガム33点のピストンズを137-117で圧倒。キャバリアーズはプロクターの初トリプルダブルでマブスを127-117で下す。",
      "body": [
        "マイアミ・ヒートは11月14日土曜夜、カセヤ・センターでデトロイト・ピストンズを137-117で破った。ヤニス・アデトクンボが34得点14リバウンド8アシストを記録し、復帰したクレイ・トンプソンが7本の3ポイントを含む26得点で援護。ピストンズはケイド・カニンガムが33得点を挙げたものの及ばなかった。",
        "クリーブランドでは、ミッチェルやハーデンら主力を休養させたキャバリアーズがダラス・マーベリックスを127-117で撃破する大波乱。新人のタイリース・プロクターが24点11リバウンド10アシストの自身初トリプルダブルをマークし、カイリー・アービングの34点を退けた。",
        "デンバー・ナゲッツはペリカンズに116-108で競り勝った。金曜日にウォリアーズを破り11連勝を飾ったスパーズはこの日は試合がなかった。"
      ]
    },
    "ko": {
      "title": "야니스 34점 히트, 피스톤스 137-117 격파; 프록터 트리플더블로 캐브스 승리 견인",
      "subtitle": "아데토쿤보와 복귀전 26점의 클레이 톰슨이 마이애미 공격을 이끌었고, 주전이 빠진 클리블랜드는 신인 프록터의 24-11-10 활약으로 댈러스를 꺾었습니다.",
      "excerpt": "NBA 토요일 경기: 히트가 커닝햄의 33점 분전에도 피스톤스를 137-117로 제압. 클리블랜드는 프록터의 생애 첫 트리플더블로 매버릭스에 127-117 승리.",
      "body": [
        "마이애미 히트가 11월 14일 토요일 밤 카세야 센터에서 디트로이트 피스톤스를 137-117로 완파했습니다. 야니스 아데토쿤보가 34점 14리바운드 8어시스트로 맹활약했고 부상에서 복귀한 클레이 톰슨이 3점슛 7개를 터뜨리며 26점을 보탰습니다. 디트로이트는 케이드 커닝햄이 33점을 올리며 분전했습니다.",
        "클리블랜드에서는 도너번 미첼과 제임스 하든이 결장한 가운데 캐벌리어스가 댈러스 매버릭스를 127-117로 꺾는 이변을 일으켰습니다. 신인 가드 타이리스 프록터가 24점 11리바운드 10어시스트로 생애 첫 트리플더블을 작성하며 34점을 넣은 카이리 어빙을 잠재웠습니다.",
        "덴버 너기츠는 뉴올리언스 펠리컨스를 116-108로 꺾었으며, 금요일 워리어스를 꺾고 11연승을 달린 샌안토니오 스퍼스는 휴식을 취했습니다."
      ]
    },
    "ar": {
      "title": "يانيس يسجل 34 نقطة ويقود هيت لاكتساح بيستونز 137-117؛ وبروكتور يسجل ثلاثية تاريخية لكافالييرز",
      "subtitle": "ميامي يبتعد بالنتيجة بفضل أنتيتوكونمبو و26 نقطة من كلاي طومسون، بينما تشكيلة كليفلاند الاحتياطية تفاجئ دالاس بفضل تألق لاعبها الصاعد.",
      "excerpt": "نتائج NBA السبت: هيت يسحق بيستونز 137-117 رغم 33 نقطة من كانينغهام. كافالييرز يهزم مافريكس 127-117 بفضل ثلاثية مزدوجة لبروكتور.",
      "body": [
        "قدم ميامي هيت عرضاً هجومياً ممتعاً مساء السبت 14 نوفمبر ليتغلب على ديترويت بيستونز بنتيجة 137-117 في كاسيا سنتر. وقاد يانيس أنتيتوكونمبو فريقه بتسجيله 34 نقطة و14 متابعة و8 تمريرات حاسمة، بينما عاد كلاي طومسون ليسجل 26 نقطة منها سبع ثلاثيات، في حين أحرز كيد كانينغهام 33 نقطة لديترويت.",
        "وفي كليفلاند حقق كافالييرز مفاجأة مدوية بالفوز على دالاس مافريكس 127-117 رغم إراحة دونوفان ميتشل وجيمس هاردن. وتألق الصاعد تيريس بروكتور مسجلاً أول ثلاثية مزدوجة في مسيرته (24 نقطة و11 متابعة و10 تمريرات حاسمة) ليتفوق على نقاط كايري إيرفينغ الـ34.",
        "وفي الغرب تغلب دنفر ناغتس على نيو أورليانز بيليكانز 116-108، بينما نال سان أنطونيو سبيرز راحة بعد انتصاره الحادي عشر توالياً يوم الجمعة."
      ]
    }
  },

  "f1-four-days-las-vegas-strip-p2-battle-antonelli-mercedes-2026": {
    "fr": {
      "title": "J-4 avant Las Vegas : 33 points separent cinq pilotes pour la place de vice-champion",
      "subtitle": "Kimi Antonelli et Mercedes etant deja sacres champions du monde, la bataille fait rage sur le Strip de 6,201 km entre Verstappen, Russell, Hamilton, Leclerc et Norris.",
      "excerpt": "La manche 21 a Las Vegas debute dans quatre jours (19-21 novembre). Max Verstappen (279) mene d'un souffle le peloton des poursuivants. Pas de course encore disputee.",
      "body": [
        "Le paddock de la Formule 1 n'est plus qu'a quatre jours des premiers essais libres sous les lumieres de Las Vegas pour la manche 21 (19-21 novembre). Les monoplaces defileront sur le Strip de 6,201 km dans la nuit du jeudi avant la course phare de samedi soir le 21 novembre. Aucune session de course n'a encore eu lieu.",
        "Si le jeune prodige Kimi Antonelli (390 points) et Mercedes-AMG (652 points) ont scelle les deux couronnes mondiales a Sao Paulo, la lutte pour le titre de vice-champion n'a jamais ete aussi disputee. Seulement 33 points separent Max Verstappen (279), George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) et Lando Norris (246).",
        "A trois epreuves de la fin de la saison, Ferrari (510 points) defend sa deuxieme place constructeurs face a Red Bull (415) et McLaren (398). Les temperatures nocturnes fraiches du desert du Nevada mettront a rude epreuve la gestion thermique des pneumatiques."
      ]
    },
    "es": {
      "title": "Cuatro dias para Las Vegas: 33 puntos separan a cinco pilotos en la lucha por el subcampeonato",
      "subtitle": "Con Kimi Antonelli y Mercedes proclamados campeones del mundo, la atencion se centra en el Strip de 6,201 km donde luchan Verstappen, Russell, Hamilton, Leclerc y Norris.",
      "excerpt": "La Ronda 21 de Las Vegas empieza en cuatro dias (19-21 de noviembre). Max Verstappen (279) aventaja en solo 33 puntos a Norris (246). No se ha disputado la carrera.",
      "body": [
        "El circo de la Formula 1 esta a solo cuatro dias de salir a pista bajo las luces de neon de Nevada para la Ronda 21, el Gran Premio de Las Vegas (19-21 de noviembre). Los coches rodaran por los 6,201 km del Strip el jueves por la noche antes de la carrera del sabado 21. No se ha celebrado ninguna sesion oficial todavia.",
        "Aunque Kimi Antonelli (390 puntos) y Mercedes (652 puntos) ya amarraron ambos campeonatos en Brasil, el subcampeonato promete chispas. Apenas 33 puntos separan a Max Verstappen (279), George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) y Lando Norris (246).",
        "A falta de tres citas para el cierre, Ferrari (510 puntos) defiende el segundo escalon de constructores ante Red Bull (415) y McLaren (398). Las bajas temperaturas nocturnas del desierto pondran a prueba el calentamiento de neumaticos."
      ]
    },
    "de": {
      "title": "Vier Tage bis Las Vegas: 33 Punkte trennen fuenf Fahrer im Kampf um die Vizemeisterschaft",
      "subtitle": "Kimi Antonelli und Mercedes stehen bereits als Weltmeister fest, doch auf dem 6,201 km langen Strip-Kurs duellieren sich Verstappen, Russell, Hamilton, Leclerc und Norris.",
      "excerpt": "Runde 21 in Las Vegas startet in vier Tagen (19. bis 21. November). Max Verstappen (279) fuehrt die Verfolgergruppe an. Noch kein Rennergebnis veroeffentlicht.",
      "body": [
        "Das Formel-1-Feld ist nur noch vier Tage vom Streckenauftakt unter den Neonlichtern Nevadas fuer Runde 21 beim Las Vegas Grand Prix (19.-21. November) entfernt. Auf dem 6,201 km langen Strip-Kurs beginnen am Donnerstagabend die Trainings, ehe am Samstagabend das Hauptrennen steigt.",
        "Waehrend Kimi Antonelli (390 Punkte) und Mercedes-AMG (652 Punkte) beide WM-Titel bereits in Brasilien perfekt machten, ist der Kampf um Platz zwei extrem eng. Nur 33 Punkte trennen Max Verstappen (279), George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) und Lando Norris (246).",
        "Bei noch drei ausstehenden Rennen verteidigt Ferrari (510 Punkte) Platz zwei bei den Konstrukteuren gegen Red Bull (415) und McLaren (398). Die kuehlen Wuestennacht-Temperaturen werden das Reifenmanagement auf eine harte Probe stellen."
      ]
    },
    "it": {
      "title": "Quattro giorni a Las Vegas: 33 punti dividono cinque piloti per il secondo posto mondiale",
      "subtitle": "Con Kimi Antonelli e la Mercedes gia campioni del mondo, i riflettori sono puntati sul circuito di 6,201 km dove duellano Verstappen, Russell, Hamilton, Leclerc e Norris.",
      "excerpt": "Il Round 21 di Las Vegas scatta tra quattro giorni (19-21 novembre). Max Verstappen (279) guida la volata per il secondo posto. Nessuna gara ancora disputata.",
      "body": [
        "Il paddock della Formula 1 e a soli quattro giorni dal via delle prove libere sotto i riflettori di Las Vegas per il Round 21 (19-21 novembre). I bolidi sfrecceranno sul tracciato cittadino di 6,201 km giovedi sera in vista della gara notturna di sabato 21 novembre.",
        "Nonostante Kimi Antonelli (390 punti) e la Mercedes (652 punti) abbiano gia conquistato entrambi i titoli iridati a San Paolo, la sfida per il posto d'onore e incandescente: solo 33 punti separano Max Verstappen (279), George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) e Lando Norris (246).",
        "A tre gare dal termine Ferrari (510 punti) difende il secondo posto costruttori dall'assalto di Red Bull (415) e McLaren (398). Il freddo notturno del deserto sara una sfida cruciale per portare in temperatura le gomme."
      ]
    },
    "pl": {
      "title": "Cztery dni do Las Vegas: 33 punkty dziela pieciu kierowcow w walce o wicemistrzostwo",
      "subtitle": "Kimi Antonelli i Mercedes zapewnili sobie tytuly mistrzowskie, a na torze Strip o dlugosci 6,201 km o drugie miejsce walcza Verstappen, Russell, Hamilton, Leclerc i Norris.",
      "excerpt": "21. runda w Las Vegas rusza za cztery dni (19-21 listopada). Max Verstappen (279) prowadzi w zaciatej walce o wicemistrzostwo. Wyscig jeszcze sie nie odbyl.",
      "body": [
        "Padok Formuly 1 jest o cztery dni od wyjazdu na tor wsrod neonow Nevady podczas Grand Prix Las Vegas (19-21 listopada). Bolidy wyjada na 6,201-kilometrowy tor uliczny Strip w czwartek wieczorem przed sobotnim glownym wyscigiem nocnym 21 listopada.",
        "Choc Kimi Antonelli (390 punktow) oraz Mercedes (652 punkty) zapewnili sobie oba tytuly mistrzowskie w Brazylii, walka o drugie miejsce jest nieslychanie zacieta. Zaledwie 33 punkty dziela Maxa Verstappena (279), George'a Russella (262), Lewisa Hamiltona (261), Charlesa Leclerca (249) oraz Lando Norrisa (246).",
        "Na trzy rundy przed koncem Ferrari (510 punktow) broni drugiego miejsca wsrod konstruktorow przed Red Bullem (415) i McLarenem (398). Chlodne pustynne noce beda powaznym sprawdzianem dogrzewania opon."
      ]
    },
    "zh": {
      "title": "距拉斯维加斯站还有四天：五位车手相差33分展开年度亚军争夺战",
      "subtitle": "在安东内利与梅赛德斯提前加冕双料世界冠军后，聚光灯转向全长6.201公里的赌城大道赛道，维斯塔潘、拉塞尔、汉密尔顿、勒克莱尔与诺里斯决战。",
      "excerpt": "第21站拉斯维加斯大奖赛将于四天后（11月19至21日）揭幕。维斯塔潘（279分）与诺里斯（246分）之间仅相差33分。尚未进行任何比赛。",
      "body": [
        "F1围场距离在内华达州璀璨霓虹下打响的第21站拉斯维加斯大奖赛（11月19-21日）仅剩四天。赛车将于周四晚间驶上全长6.201公里的拉斯维加斯大道赛道进行练习赛，并于11月21日周六夜间展开正赛决战。该赛事目前尚未进行任何正式比赛。",
        "尽管20岁的新星基米·安东内利（390分）与梅赛德斯车队（652分）已在巴西双双加冕世界冠军，但年度车手亚军的争夺空前白热化。第二名维斯塔潘（279分）与第五名诺里斯（246分）之间仅差33分，拉塞尔（262分）、汉密尔顿（261分）和勒克莱尔（249分）紧随其后。",
        "在赛季仅剩拉斯维加斯、卡塔尔和阿布扎比三站之际，法拉利（510分）正力保车队次席，抵挡红牛（415分）与迈凯伦（398分）的追击。沙漠深夜的低温环境将极大考验各队的轮胎升温策略。"
      ]
    },
    "ja": {
      "title": "ラスベガスGPまであと4日：ランキング2位を巡り5人のドライバーが33点差の大混戦",
      "subtitle": "アントネッリとメルセデスが世界王者に輝いた後、全長6.201kmのストリップコースでフェルスタッペン、ラッセル、ハミルトン、ルクレール、ノリスが激突。",
      "excerpt": "第21戦ラスベガスは4日後開幕（11月19-21日）。フェルスタッペン（279）からノリス（246）まで33ポイント差の争い。決勝レースは未開催。",
      "body": [
        "F1サーカスはネバダのネオン輝く第21戦ラスベガスGP（11月19-21日）開幕まであと4日に迫った。木曜夜に全長6.201kmのストリップ市街地コースでプラクティスが始まり、21日土曜夜に決勝レースを迎える。現時点で競技セッションは行われていない。",
        "キミ・アントネッリ（390点）とメルセデス（652点）がブラジルでドライバーズおよびコンストラクターズのダブルタイトルを決めたものの、ランキング2位争いは史上稀に見る激戦となっている。2位のフェルスタッペン（279点）から5位のノリス（246点）までわずか33点差で、ラッセル（262）、ハミルトン（261）、ルクレール（249）がひしめく。",
        "残り3戦でフェラーリ（510点）はレッドブル（415点）とマクラーレン（398点）を抑えてコンストラクターズ2位を守りたい。砂漠の冷え込む夜の気温と低グリップ路面がタイヤ熱入れの鍵となる。"
      ]
    },
    "ko": {
      "title": "라스베이거스 GP D-4: 준우승 향한 5명 드라이버 33점 차 대접전",
      "subtitle": "키미 안토넬리와 메르세데스가 월드 챔피언에 오른 가운데, 6.201km 스트립 서킷에서 베르스타펜, 러셀, 해밀턴, 르클레르, 노리스가 격돌합니다.",
      "excerpt": "21라운드 라스베이거스는 4일 후 개막(11월 19-21일). 막스 베르스타펜(279점)부터 랜도 노리스(246점)까지 33점 차. 레이스는 아직 미개최.",
      "body": [
        "F1 패덕이 네바다의 네온사인 아래서 펼쳐지는 21라운드 라스베이거스 그랑프리(11월 19-21일) 트랙 액션까지 단 4일을 남겨두고 있습니다. 목요일 밤 6.201km 스트립 서킷에서 연습 주행이 시작되며 21일 토요일 밤 본선 레이스가 열립니다. 현재까지 어떠한 주행 세션도 진행되지 않았습니다.",
        "키미 안토넬리(390점)와 메르세데스(652점)가 브라질에서 드라이버 및 컨스트럭터 월드 챔피언십을 조기 확정지었지만, 시즌 준우승 다툼은 극도로 치열합니다. 2위 막스 베르스타펜(279점)과 5위 랜도 노리스(246점)의 격차는 33점에 불과하며 조지 러셀(262), 루이스 해밀턴(261), 샤를 르클레르(249)가 촘촘히 포진해 있습니다.",
        "남은 세 경기 동안 페라리(510점)는 레드불 레이싱(415점)과 맥라렌(398점)을 상대로 컨스트럭터 2위 수성에 나섭니다. 차가운 사막의 야간 기온은 타이어 예열 전략에 중대한 시험대가 될 전망입니다."
      ]
    },
    "ar": {
      "title": "أربعة أيام على جائزة لاس فيغاس: 33 نقطة تفصل خمسة سائقين في صراع وصافة البطولة",
      "subtitle": "مع حسم كيمي أنتونيللي ومرسيدس لقبي بطولة العالم، يتحول الصراع إلى حلبة ستريب بطول 6.201 كم بين فيرستابن، راسل، هاميلتون، لوكلير ونوريس.",
      "excerpt": "الجولة 21 في لاس فيغاس تنطلق بعد أربعة أيام (19-21 نوفمبر). ماكس فيرستابن (279) يقود صراع الوصافة بفارق ضئيل. لم يجر السباق بعد.",
      "body": [
        "تقف بطولة العالم لسباقات الفورمولا 1 على بعد أربعة أيام فقط من انطلاق الجولة 21 على حلبة لاس فيغاس الشهيرة وسط أضواء نيفادا (19-21 نوفمبر). وتنطلق التجارب الحرة مساء الخميس على مسار ستريب بطول 6.201 كم، وصولاً للسباق الرئيسي ليل السبت 21 نوفمبر. ولم يُجرَ أي سباق حتى الآن.",
        "وبينما حسم الشاب كيمي أنتونيللي (390 نقطة) ومرسيدس (652 نقطة) لقبي السائقين والصانعين في البرازيل، فإن الصراع على المركز الثاني مشتعل للغاية، إذ تفصل 33 نقطة فقط بين الثاني ماكس فيرستابن (279) والخامس لاندو نوريس (246)، وبينهما جورج راسل (262) ولويس هاميلتون (261) وشارل لوكلير (249).",
        "ومع بقاء ثلاث جولات في فيغاس وقطر وأبوظبي، تدافع فيراري (510 نقاط) عن وصافة الصانعين أمام رد بول (415) ومكلارين (398)، وسط توقعات بأن تكون درجات الحرارة المنخفضة ليلاً في الصحراء اختباراً حاسماً للإطارات."
      ]
    }
  }
}

def inject():
    path = "frontend/src/i18n/stories.ts"
    content = open(path, "r", encoding="utf-8").read()

    # Find the closing `};` of STORY_I18N
    # It ends with `};` at the end of the file
    last_brace = content.rfind("};")
    if last_brace == -1:
        print("ERROR: Could not find closing }; in stories.ts")
        return

    # Build the new entries string
    entries_str = ""
    for slug, loc_map in nov15_i18n.items():
        entries_str += f'  "{slug}": '
        # Format json with 2 spaces indent
        slug_json = json.dumps(loc_map, ensure_ascii=False, indent=2)
        # Indent each line by 2 spaces except the first
        lines = slug_json.split("\n")
        indented = [lines[0]] + [("  " + l if l else "") for l in lines[1:]]
        entries_str += "\n".join(indented) + ",\n"

    # Insert before last_brace
    new_content = content[:last_brace] + entries_str + content[last_brace:]

    open(path, "w", encoding="utf-8", newline="\n").write(new_content)
    print("Injected nov15 translations into stories.ts.")

if __name__ == "__main__":
    inject()

