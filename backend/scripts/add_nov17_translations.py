"""Add 10-language translations for the 6 new stories on 2026-11-17."""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
STORIES_TS = os.path.join(ROOT, "frontend", "src", "i18n", "stories.ts")

translations_data = {
  "nations-league-germany-crush-netherlands-5-0-wirtz-brace-2026": {
    "fr": {
      "title": "Ligue des nations : L'Allemagne écrase les Pays-Bas 5-0 grâce à un doublé de Florian Wirtz",
      "subtitle": "L'équipe de Julian Nagelsmann inflige aux Oranje leur plus lourde défaite depuis 1959 et s'assure la première place du groupe A2.",
      "excerpt": "Florian Wirtz signe un doublé tandis que Derry Scherhant, Nico Schlotterbeck et Brajan Gruda marquent dans une démonstration éclatante 5-0 à Leipzig.",
      "body": [
        "L'Allemagne a signé une victoire historique et sans appel lundi soir, 16 novembre, en dominant nettement les Pays-Bas 5-0 à la Red Bull Arena de Leipzig pour s'adjuger la première place du groupe A2 de la Ligue des nations de l'UEFA.",
        "Après un début intense où la sélection de Ronald Koeman tentait de trouver la faille, les hommes de Julian Nagelsmann ont pris l'ascendant au milieu de terrain grâce à Florian Wirtz et Angelo Stiller. L'ouverture du score est venue à la 41e minute grâce à Derry Scherhant d'une frappe croisée. En seconde période, Wirtz a doublé la mise à l'heure de jeu d'une frappe splendide dans la lucarne, suivi par Schlotterbeck de la tête (65e), Gruda (72e) et un subtil lob de Wirtz à la 77e minute.",
        "Ce revers 5-0 est le plus lourd subi par les Pays-Bas depuis 1959. Si les deux nations sont qualifiées pour les quarts de finale en mars 2027, l'Allemagne s'assure le statut de tête de série, plongeant les Oranje dans le doute. Dans les autres rencontres, la Grèce a battu la Serbie 1-0 et la Suisse a dominé l'Écosse 4-0."
      ]
    },
    "es": {
      "title": "Liga de Naciones: Alemania aplasta a Países Bajos 5-0 con doblete de Florian Wirtz",
      "subtitle": "El equipo de Julian Nagelsmann propina a la selección neerlandesa su peor derrota desde 1959 y asegura el liderato del Grupo A2.",
      "excerpt": "Florian Wirtz anota por partida doble mientras Derry Scherhant, Nico Schlotterbeck y Brajan Gruda completan una contundente goleada 5-0 en Leipzig.",
      "body": [
        "Alemania ofreció una exhibición memorable de contundencia ofensiva la noche del lunes 16 de noviembre, arrollando a Países Bajos 5-0 en el Red Bull Arena de Leipzig para conquistar el primer puesto del Grupo A2 de la UEFA Nations League.",
        "Tras unos primeros minutos intensos donde el equipo de Ronald Koeman buscó generar peligro, el cuadro de Julian Nagelsmann tomó el control de la medular de la mano de Florian Wirtz y Angelo Stiller. Derry Scherhant abrió la cuenta en el minuto 41 con un disparo cruzado raso. En la reanudación, Wirtz colocó un remate magistral en la escuadra a la hora de juego, Schlotterbeck cabeceó el tercero en el 65, Gruda firmó el cuarto en el 72 y Wirtz redondeó su doblete con una vaselina en el 77.",
        "El 5-0 representa la derrota más abultada de Países Bajos en cualquier partido internacional desde 1959. Aunque ambos combinados tenían sellado su pase a los cuartos de final de marzo de 2027, Alemania accede como cabeza de serie mientras la defensa neerlandesa queda señalada tras un derrumbe colectivo inesperado."
      ]
    },
    "de": {
      "title": "Nations League Gala: Deutschland fegt die Niederlande mit 5:0 vom Platz dank Wirtz-Doppelpack",
      "subtitle": "Das Team von Julian Nagelsmann fügt der Elftal die höchste Niederlage seit 1959 zu und sichert sich souverän den Gruppensieg in A2.",
      "excerpt": "Florian Wirtz glänzt mit einem Doppelpack, während Derry Scherhant, Nico Schlotterbeck und Brajan Gruda den historischen 5:0-Kantersieg in Leipzig komplettieren.",
      "body": [
        "Die deutsche Nationalmannschaft hat am Montagabend, 16. November, ein historisches Ausrufezeichen gesetzt und den Erzrivalen Niederlande in der Leipziger Red Bull Arena mit 5:0 demontiert, um sich den Gruppensieg in der Gruppe A2 der UEFA Nations League zu sichern.",
        "Nach einer temporeichen Anfangsphase übernahm das DFB-Team über Florian Wirtz und Angelo Stiller im Mittelfeld die Spielkontrolle. Der 23-jährige Derry Scherhant brach in der 41. Minute mit einem platzierten Flachschuss den Bann. Im zweiten Durchgang brachen alle Dämme: Wirtz schlenzte den Ball nach einer Stunde traumhaft in den Winkel, Schlotterbeck erhöhte per Kopf (65.), Gruda legte das 4:0 nach (72.) und erneut Wirtz setzte mit einem gefühlvollen Heber in der 77. Minute den Schlusspunkt.",
        "Die 0:5-Pleite ist die schwerste Niederlage der Niederlande seit 1959. Obwohl beide Teams für das Viertelfinale im März 2027 qualifiziert sind, sichert sich Deutschland den gesetzten Status und reist mit Rückenwind ins Frühjahr."
      ]
    },
    "it": {
      "title": "Nations League: La Germania travolge l'Olanda 5-0 con una doppietta di Florian Wirtz",
      "subtitle": "La squadra di Julian Nagelsmann infligge agli Oranje la sconfitta più pesante dal 1959 e vince il Gruppo A2.",
      "excerpt": "Florian Wirtz firma una doppietta mentre Scherhant, Schlotterbeck e Gruda partecipano alla festa nel 5-0 di Lipsia contro l'Olanda.",
      "body": [
        "La Germania ha offerto una straordinaria dimostrazione di forza lunedì sera, 16 novembre, superando nettamente l'Olanda 5-0 alla Red Bull Arena di Lipsia per conquistare il primato nel Gruppo A2 di UEFA Nations League.",
        "Dopo un avvio vivace della formazione di Ronald Koeman, i tedeschi guidati da Nagelsmann hanno preso possesso del centrocampo con Wirtz e Stiller. A sbloccare il risultato ci ha pensato Derry Scherhant al 41' con un tiro preciso. Nella ripresa la Germania ha dilagato: splendido tiro all'incrocio di Wirtz al 60', colpo di testa vincente di Schlotterbeck al 65', poker di Gruda al 72' e cucchiaio delizioso di Wirtz al 77'.",
        "Il passivo di 5-0 costituisce per l'Olanda la peggior sconfitta a livello internazionale dal 1959. Entrambe le nazionali sono approdate ai quarti di finale di marzo 2027, ma la Germania lo fa da testa di serie tra gli applausi dei 42.000 spettatori."
      ]
    },
    "pl": {
      "title": "Liga Narodów: Niemcy rozbijają Holandię 5:0 po dublecie Floriana Wirtza",
      "subtitle": "Zespół Juliana Nagelsmanna zadaje Oranje najwyższą porażkę od 1959 roku i przypieczętowuje triumf w grupie A2.",
      "excerpt": "Florian Wirtz strzela dwa gole, a Scherhant, Schlotterbeck i Gruda dobijają Holendrów w spektakularnym pogromie 5:0 w Lipsku.",
      "body": [
        "Reprezentacja Niemiec zaprezentowała w poniedziałkowy wieczór, 16 listopada, niesamowitą skuteczność ofensywną, gromiąc Holandię 5:0 na Red Bull Arena w Lipsku i gwarantując sobie pierwsze miejsce w grupie A2 Ligi Narodów UEFA.",
        "Choć drużyna Ronalda Koemana próbowała początkowo narzucić własne warunki, Niemcy szybko zdominowali środek pola za sprawą Wirtza i Stillera. W 41. minucie wynik otworzył Derry Scherhant precyzyjnym strzałem po ziemi. Po przerwie podopieczni Nagelsmanna urządzili prawdziwy festiwal strzelecki: Wirtz przymierzył w okienko w 60. minucie, Schlotterbeck trafił głową w 65., Gruda wbił czwartego gola w 72., a Wirtz ustalił wynik technicznym lobem w 77. minucie.",
        "Klęska 0:5 to najwyższa porażka Holandii w meczu międzypaństwowym od 1959 roku. Obie drużyny zagrają w marcowych ćwierćfinałach 2027 roku, jednak to Niemcy przystąpią do losowania z pozycji drużyny rozstawionej."
      ]
    },
    "zh": {
      "title": "欧国联狂胜：维尔茨双响助德国5-0大胜荷兰锁定A2组头名",
      "subtitle": "纳格尔斯曼率队在莱比锡送给荷兰队自1959年以来的最大比分惨败，昂首晋级八强。",
      "excerpt": "维尔茨独中两元，谢尔汉特、施洛特贝克和格鲁达接连建功，德国队在主场以5-0摧枯拉朽之势横扫宿敌荷兰。",
      "body": [
        "在11月16日周一晚间进行的欧洲国家联赛A2组焦点战中，德国队在莱比锡红牛竞技场展现了惊人的进攻威力，以5-0狂胜传统劲敌荷兰队，锁定小组第一名。",
        "比赛伊始科曼执教的荷兰队曾试图发起攻势，但纳格尔斯曼的球队凭借维尔茨与斯蒂勒在中场的精准调度迅速掌控节奏。第41分钟，23岁边锋谢尔汉特内切低射破门打破僵局。下半场德国队全面开花：维尔茨在第60分钟轰入世界波，施洛特贝克第65分钟角球冲顶破门，替补登场的格鲁达第72分钟扩大比分，维尔茨则在第77分钟轻巧挑射完成双响。",
        "这场5-0创造了荷兰国家队自1959年以来的最惨重失利纪录。尽管两队均已提前晋级2027年3月的八强赛，但德国队凭借这场大胜锁定了种子队席位，而荷兰队的防线则遭遇严厉质疑。"
      ]
    },
    "ja": {
      "title": "ネーションズリーグ：ヴィルツ2発のドイツがオランダを5-0粉砕、A2組首位確定",
      "subtitle": "ナーゲルスマン率いるドイツがライバルに1959年以来となる歴史的惨敗を浴びせ、堂々の首位突破を果たす。",
      "excerpt": "ヴィルツが圧巻の2ゴールを挙げ、シェルハント、シュロッターベック、グルーダも得点。ドイツがライプツィヒでオランダを5-0と圧倒。",
      "body": [
        "UEFAネーションズリーグのリーグAグループ2最終節が11月16日月曜日に行われ、ドイツ代表がライプツィヒのレッドブル・アレーナでオランダを5-0で圧倒し、首位通過を決めました。",
        "序盤はクーマン率いるオランダが仕掛ける場面もありましたが、ナーゲルスマン監督のドイツはヴィルツを中心に中盤を支配。41分にデル・シェルハントが先制点を奪うと、後半はドイツの独壇場となりました。60分にヴィルツが見事なミドルシュートを沈め、65分にはシュロッターベックがヘッドで加点。72分にグルーダ、77分にはヴィルツが技ありのループシュートを決めて5-0としました。",
        "この5-0の敗戦は、オランダ代表にとって1959年以来最悪の大敗となりました。両国ともに2027年3月の準々決勝進出を決めていますが、ドイツがシード権を確保した一方、オランダは守備の立て直しが急務となっています。"
      ]
    },
    "ko": {
      "title": "네이션스리그: 비르츠 멀티골 독일, 네덜란드 5-0 대파하고 A2조 1위 확정",
      "subtitle": "율리안 나겔스만 감독의 독일이 네덜란드에 1959년 이후 최악의 참패를 안기며 8강 시드를 확보했습니다.",
      "excerpt": "플로리안 비르츠의 2골과 셰르한트, 슐로터베크, 그루다의 연속골로 독일이 라이프치히에서 네덜란드를 5-0으로 무너뜨렸습니다.",
      "body": [
        "독일 축구 대표팀이 11월 16일 월요일 밤 라이프치히 레드불 아레나에서 열린 UEFA 네이션스리그 리그A 2조 최종전에서 숙적 네덜란드를 5-0으로 완파하며 조 1위를 차지했습니다.",
        "로날트 쿠만 감독의 네덜란드가 초반 탐색전을 펼쳤으나, 독일은 플로리안 비르츠와 안젤로 슈틸러의 중원 장악력을 앞세워 주도권을 잡았습니다. 전반 41분 데리 셰르한트의 선제골을 시작으로 후반에만 4골이 터졌습니다. 비르츠가 후반 15분 환상적인 감아차기로 추가골을 넣었고, 슐로터베크의 헤더와 그루다의 득점에 이어 비르츠가 후반 32분 칩슛으로 5-0 대승을 완성했습니다.",
        "이번 5-0 패배는 네덜란드 대표팀 역사상 1959년 이후 67년 만에 당한 최다 점수 차 패배입니다. 양 팀 모두 2027년 3월 8강 토너먼트에 진출했지만 독일은 시드 배정의 유리함을 안게 되었습니다."
      ]
    },
    "ar": {
      "title": "دوري الأمم الأوروبية: ألمانيا تسحق هولندا بخماسية نظيفة بفضل ثنائية فيرتز",
      "subtitle": "كتيبة يوليان ناغلسمان تلحق بالطواحين أسوأ هزيمة منذ عام 1959 وتنتزع صدارة المجموعة الثانية في المستوى الأول.",
      "excerpt": "فلوريان فيرتز يسجل هدفين بينما أضاف شيرهانت وشلوتربيك وغرودا الأهداف الأخرى في ليلة اكتساح تاريخية بمدينة لايبزيغ.",
      "body": [
        "قدم المنتخب الألماني عرضا هجوميا كاسحا مساء الاثنين 16 نوفمبر بعدما أمطر شباك غريمه الهولندي بخمسة أهداف دون رد على ملعب ريد بول أرينا في لايبزيغ، ليحسم صدارة المجموعة الثانية في المستوى الأول لدوري الأمم الأوروبية.",
        "بعد بداية متكافئة من جانب فريق المدرب رونالد كومان، فرض الألمان سيطرتهم المطلقة في وسط الملعب بفضل تألق فلوريان فيرتز. وافتتح ديري شيرهانت التسجيل في الدقيقة 41 بتسديدة زاحفة. وفي الشوط الثاني انهار الدفاع الهولندي، حيث أضاف فيرتز الهدف الثاني بتسديدة مقوسة في الدقيقة 60، وتبعه شلوتربيك برأسية في الدقيقة 65، ثم البديل غرودا بالرابع في الدقيقة 72، قبل أن يختتم فيرتز الخماسية بكرة ساقطة في الدقيقة 77.",
        "وتعد هذه الخسارة الأثقل لمنتخب هولندا في جميع البطولات منذ عام 1959. ورغم تأهل المنتخبين سلفا لربع النهائي المقرر في مارس 2027، فإن ألمانيا تدخل القرعة بصفتها متصدرة ومصنفة أولى وسط إشادات واسعة."
      ]
    }
  },
  "nfl-mnf-chargers-edge-ravens-in-harbaugh-bowl-herbert-hampton-2026": {
    "fr": {
      "title": "Harbaugh Bowl : Les Chargers dominent les Ravens 23-20 lors du Monday Night Football",
      "subtitle": "Justin Herbert court pour un touchdown et Omarion Hampton gagne 105 yards alors que Jim Harbaugh bat son frère John à Baltimore.",
      "excerpt": "Les Chargers de Los Angeles résistent au retour des Ravens grâce à Herbert et au rookie Hampton, décrochant un succès 23-20 dans le duel fraternel.",
      "body": [
        "Jim Harbaugh a décroché la victoire familiale lundi soir, 16 novembre, alors que ses Chargers de Los Angeles ont tenu bon pour battre les Baltimore Ravens de John Harbaugh 23-20 au M&T Bank Stadium.",
        "Cette confrontation tant attendue entre les deux frères, la première depuis le Super Bowl XLVII en 2013, a tenu toutes ses promesses. Justin Herbert a rapidement ouvert la marque sur une course magistrale de 22 yards. Le running back rookie Omarion Hampton a fait forte impression en amassant 105 yards au sol et un touchdown de 4 yards en puissance.",
        "Lamar Jackson a ramené Baltimore dans le match au quatrième quart-temps avec une passe de touchdown pour Mark Andrews, mais le cornerback Tarheeb Still a provoqué un fumble décisif sur Zay Flowers dans les deux dernières minutes pour sceller le succès des Chargers (7-3)."
      ]
    },
    "es": {
      "title": "Harbaugh Bowl: Los Chargers superan a los Ravens 23-20 en el Monday Night Football",
      "subtitle": "Justin Herbert corre para touchdown y Omarion Hampton suma 105 yardas terrestres en el triunfo de Jim sobre John Harbaugh en Baltimore.",
      "excerpt": "Los Angeles Chargers se llevan un emocionante triunfo 23-20 en Baltimore con destacadas actuaciones de Herbert, Hampton y una pérdida forzada clave.",
      "body": [
        "Jim Harbaugh se quedó con el triunfo en el duelo familiar del lunes 16 de noviembre, cuando sus Angeles Chargers vencieron 23-20 a los Baltimore Ravens de John Harbaugh en el M&T Bank Stadium.",
        "En su primer duelo directo desde el Super Bowl XLVII, Justin Herbert brilló con una escapada de 22 yardas para touchdown en el primer cuarto. El novato Omarion Hampton castigó la defensa terrestre de Baltimore acumulando 105 yardas en 21 acarreos y una anotación de 4 yardas en el tercer cuarto.",
        "Pese a una tardía reacción de Lamar Jackson con pase de touchdown a Mark Andrews, el esquinero Tarheeb Still provocó un balón suelto clave de Zay Flowers en los últimos dos minutos para asegurar la victoria de los Chargers (7-3)."
      ]
    },
    "de": {
      "title": "Harbaugh Bowl Drama: Chargers bezwingen Ravens mit 23:20 im Monday Night Football",
      "subtitle": "Justin Herbert erläuft einen Touchdown und Omarion Hampton glänzt mit 105 Yards, während Jim Harbaugh seinen Bruder John schlägt.",
      "excerpt": "Die Los Angeles Chargers setzen sich in einem packenden Bruderkampf mit 23:20 in Baltimore durch und zwingen die Ravens in die Knie.",
      "body": [
        "Jim Harbaugh sicherte sich am Montagabend, 16. November, das Familienduell, als seine Los Angeles Chargers die Baltimore Ravens von Bruder John mit 23:20 im M&T Bank Stadium niederrangen.",
        "Justin Herbert brachte die Gäste früh mit einem spektakulären 22-Yard-Touchdown-Lauf in Führung. Rookie-Running-Back Omarion Hampton dominierte am Boden mit 105 Rushing Yards bei 21 Versuchen und einem Touchdown im dritten Viertel.",
        "Lamar Jackson brachte die Ravens im vierten Viertel mit einem Touchdown-Pass auf Mark Andrews noch einmal auf 20:23 heran, doch Chargers-Cornerback Tarheeb Still erzwang kurz vor Schluss ein Fumble von Zay Flowers, das den Sieg für Los Angeles (7-3) besiegelte."
      ]
    },
    "it": {
      "title": "Harbaugh Bowl: I Chargers piegano i Ravens 23-20 nel Monday Night Football",
      "subtitle": "Justin Herbert firma una meta su corsa e Omarion Hampton conquista 105 yard nel successo di Jim sul fratello John a Baltimora.",
      "excerpt": "I Los Angeles Chargers vincono 23-20 in casa dei Ravens grazie alla brillante prova di Herbert, Hampton e a un turnover decisivo nel finale.",
      "body": [
        "Jim Harbaugh ha conquistato la vittoria nel derby di famiglia lunedì sera, 16 novembre, guidando i suoi Los Angeles Chargers al successo per 23-20 sui Baltimore Ravens di John Harbaugh al M&T Bank Stadium.",
        "Justin Herbert ha aperto le danze con una spettacolare corsa da 22 yard per il touchdown inaugurale. Il rookie Omarion Hampton è stato devastante sulle corse accumulando 105 yard e un touchdown nel terzo quarto.",
        "Lamar Jackson ha tentato la rimonta nel quarto periodo con un passaggio da touchdown per Mark Andrews, ma Tarheeb Still ha forzato un fumble su Zay Flowers a meno di due minuti dal termine garantendo la vittoria a Los Angeles (7-3)."
      ]
    },
    "pl": {
      "title": "Harbaugh Bowl: Chargers pokonują Ravens 23:20 w meczu Monday Night Football",
      "subtitle": "Justin Herbert zdobywa przyłożenie po biegu, a Omarion Hampton notuje 105 jardów w bratobójczym starciu w Baltimore.",
      "excerpt": "Los Angeles Chargers wygrywają 23:20 w Baltimore w emocjonującym pojedynku trenerskim braci Jima i Johna Harbaughów.",
      "body": [
        "Jim Harbaugh triumfował w rodzinnym pojedynku w poniedziałkowy wieczór, 16 listopada, kiedy Los Angeles Chargers pokonali Baltimore Ravens Johna Harbaugha 23:20 na M&T Bank Stadium.",
        "Justin Herbert zachwycił na początku spotkania ucieczką na 22 jardy do strefy punktowej. Debiutujący biegacz Omarion Hampton zaliczył świetny występ w porze największej oglądalności, zdobywając 105 jardów i przyłożenie z 4 jardów.",
        "Lamar Jackson poderwał Ravens w czwartej kwarcie podaniem na przyłożenie do Marka Andrewsa, jednak obrońca Tarheeb Still wymusił kluczowe fumble na Zayu Flowersie w ostatnich dwóch minutach, pieczętując wygraną Chargers (7-3)."
      ]
    },
    "zh": {
      "title": "哈博兄弟碗决战：闪电客场23-20险胜乌鸦，吉姆笑傲兄弟内战",
      "subtitle": "赫伯特上演22码冲球达阵，新秀汉普顿冲出105码，洛杉矶闪电客场力擒巴尔的摩乌鸦。",
      "excerpt": "在周一夜赛的哈博兄弟对决中，洛杉矶闪电凭借强硬的地面进攻和关键防守擒抱，以23-20力克巴尔的摩乌鸦。",
      "body": [
        "在11月16日周一晚间进行的NFL周一夜赛中，吉姆-哈博率领的洛杉矶闪电在客场以23-20险胜其兄长约翰-哈博执教的巴尔的摩乌鸦，赢得备受瞩目的哈博兄弟碗对决。",
        "四分卫贾斯汀-赫伯特在首节完成了一记精彩绝伦的22码持球冲球达阵，为闪电队奠定领先基调。新秀跑卫奥马里恩-汉普顿全场冲球21次斩获105码并在第三节贡献达阵，统治了地面战局。",
        "第四节拉马尔-杰克逊连线安德鲁斯达阵将比分迫近至20-23，但在最后两分钟乌鸦推进至射门区域前，闪电角卫斯蒂尔关键拍掉弗劳尔斯手中的皮球并完成夺回，锁定胜局。"
      ]
    },
    "ja": {
      "title": "ハーボー・ボウル決戦：チャージャーズが23-20でレイブンズに競り勝つ",
      "subtitle": "ハーバートが22ヤードTDラン、新人ハンプトンが105ヤード激走。ジム・ハーボーが兄ジョンとの対決を制す。",
      "excerpt": "マンデーナイト・フットボールでロサンゼルス・チャージャーズが敵地でボルティモア・レイブンズを23-20で下し、7勝3敗へ前進。",
      "body": [
        "11月16日月曜日のマンデーナイト・フットボールで、ジム・ハーボー率いるロサンゼルス・チャージャーズが敵地M&Tバンク・スタジアムで兄ジョン・ハーボーのボルティモア・レイブンズを23-20で下しました。",
        "序盘にQBジャスティン・ハーバートがプレッシャーを交わして22ヤードのタッチダウンランを決めると、新人RBオマリオン・ハンプトンが21キャリーで105ヤード、1TDと躍動して地上戦を圧倒しました。",
        "レイブンズはラマー・ジャクソンが第4QにアンドリュースへのTDパスで3点差に迫りましたが、試合終了間際にチャージャーズCBターヒーブ・スティルがフラワーズから値千金のファンブルを奪い、勝利を決定づけました。"
      ]
    },
    "ko": {
      "title": "하보 볼 결전: 차저스, 먼데이 나이트서 레이븐스 23-20 제압",
      "subtitle": "저스틴 허버트의 22야드 러싱 터치다운과 루키 햄튼의 105야드 맹활약 속에 짐 하보 감독이 형 존 하보를 꺾었습니다.",
      "excerpt": "LA 차저스가 볼티모어 원정에서 23-20 승리를 거두며 하보 형제 감독 맞대결에서 기분 좋은 승리를 챙겼습니다.",
      "body": [
        "11월 16일 월요일 밤 볼티모어 M&T 뱅크 스타디움에서 열린 NFL 먼데이 나이트 풋볼에서 짐 하보 감독의 LA 차저스가 형 존 하보 감독의 볼티모어 레이븐스를 23-20으로 꺾었습니다.",
        "쿼터백 저스틴 허버트가 1쿼터 22야드 터치다운 질주를 선보이며 기선을 제압했고, 루키 러닝백 오마리온 햄튼이 21회 러싱으로 105야드와 1터치다운을 기록하며 팀 공격을 이끌었습니다.",
        "레이븐스는 라마 잭슨의 터치다운 패스로 4쿼터 막판 20-23까지 턱밑 추격했으나, 경기 종료 2분을 남기고 차저스 코너백 타힙 스틸이 제이 플라워스의 펌블을 유도해 승부에 쐐기를 박았습니다."
      ]
    },
    "ar": {
      "title": "مواجهة الإخوة هاربوه: تشارجرز يهزم ريفنز 23-20 في ختام الجولة العاشرة",
      "subtitle": "جاستن هربرت يسجل هدفا ركضا من 22 ياردة والوافد الجديد هامبتون يتألق بـ 105 ياردات في فوز جيم هاربوه على شقيقه جون.",
      "excerpt": "لوس أنجلوس تشارجرز يحسم قمة ليلة الاثنين المثيرة أمام بالتيمور ريفنز بنتيجة 23-20 بفضل دفاع فولاذي في اللحظات الأخيرة.",
      "body": [
        "خرج المدرب جيم هاربوه منتصرا في مواجهة العائلة الشهيرة مساء الاثنين 16 نوفمبر بعدما قاد فريقه لوس أنجلوس تشارجرز للفوز على بالتيمور ريفنز بقيادة شقيقه جون بنتيجة 23-20 على ملعب إم آند تي بنك ستاديوم.",
        "افتتح جاستن هربرت التسجيل مبكرا بلقطة رائعة حين انطلق بالكرة لمسافة 22 ياردة مسجلا هدفا حاسما. وسيطر العداء الشاب أوماريون هامبتون على الأرض محققا 105 ياردات من 21 محاولة مع تسجيل هدف رائع في الربع الثالث.",
        "حاول بالتيمور العودة بقيادة لامار جاكسون في الربع الأخير، إلا أن الدفاع أوقف الخطورة بعدما نجح تارهيب ستيل في إجبار زاي فلاورز على فقدان الكرة في الدقيقتين الأخيرتين ليرفع تشارجرز رصيده إلى 7 انتصارات مقابل 3 هزائم."
      ]
    }
  },
  "nba-magic-fourth-quarter-rally-snaps-celtics-six-game-streak-2026": {
    "fr": {
      "title": "Le Magic surprend Boston : Un quatrième quart-temps de feu met fin à la série des Celtics 115-105",
      "subtitle": "Desmond Bane inscrit 24 points et Franz Wagner en ajoute 22 alors qu'Orlando domine le dernier quart 34-21.",
      "excerpt": "Le Magic d'Orlando renverse les Celtics au TD Garden 115-105, tandis que le Heat de Miami signe un cinquième succès de rang avec Giannis.",
      "body": [
        "Le Magic d'Orlando a créé la sensation lundi soir, 16 novembre, en renversant les Boston Celtics 115-105 au TD Garden grâce à une démonstration d'intensité dans le dernier quart-temps.",
        "Menés au score après trois quart-temps équilibrés malgré les 28 points de Jayson Tatum, les joueurs d'Orlando ont totalement étouffé l'attaque celte dans les douze dernières minutes en lui infligeant un cinglant 34-21. Desmond Bane a été le grand artisan de ce retour avec 14 de ses 24 points inscrits dans le quatrième acte, bien secondé par Franz Wagner (22 points, 7 passes).",
        "Cette victoire permet à Orlando de grimper à 8-5 dans la conférence Est. Ailleurs en NBA lundi, Miami a poursuivi sa série victorieuse en dominant Houston 128-110 grâce aux 20 points et 13 rebonds de Giannis Antetokounmpo, tandis que Joel Embiid s'est illustré avec 37 points lors de la victoire de Philadelphie sur Brooklyn (135-123)."
      ]
    },
    "es": {
      "title": "Sorpresa en Boston: El Magic frena la racha de los Celtics con un brillante último cuarto 115-105",
      "subtitle": "Desmond Bane anota 24 puntos y Franz Wagner aporta 22 en la remontada 34-21 de Orlando en el cuarto decisivo.",
      "excerpt": "Orlando Magic da el golpe en el TD Garden al superar 115-105 a los Celtics, mientras los Heat suman su quinta victoria consecutiva con Giannis.",
      "body": [
        "Orlando Magic dio la campanada del lunes 16 de noviembre en la NBA al remontar en el último cuarto para imponerse 115-105 a los Boston Celtics en el TD Garden.",
        "Aunque Jayson Tatum lideró a los locales con 28 puntos, Orlando desató una feroz defensa en el último parcial superando a Boston por 34-21. Desmond Bane brilló con luz propia al anotar 14 de sus 24 puntos en el último cuarto, mientras que Franz Wagner aportó 22 puntos y 7 asistencias para sellar el triunfo visitante.",
        "Con este resultado Orlando mejora su marca a 8-5. En otros encuentros de la jornada, Miami Heat encadenó su quinto triunfo consecutivo al vencer 128-110 a Houston con 20 puntos y 13 rebotes de Giannis Antetokounmpo, y Joel Embiid se destapó con 37 puntos en la victoria de los 76ers 135-123 sobre Brooklyn."
      ]
    },
    "de": {
      "title": "Magic schocken Celtics: Furioses Schlussviertel beendet Bostons Serie mit 115:105",
      "subtitle": "Desmond Bane erzielt 24 Punkte und Franz Wagner steuert 22 Zähler bei, während Orlando das vierte Viertel mit 34:21 dominiert.",
      "excerpt": "Die Orlando Magic feiern einen sensationellen 115:105-Auswärtssieg bei den Boston Celtics. Die Miami Heat siegen erneut dank Giannis.",
      "body": [
        "Die Orlando Magic haben am Montagabend, 16. November, für die Überraschung des NBA-Spieltages gesorgt und den Boston Celtics mit einem 115:105-Sieg im TD Garden die erste Niederlage nach sechs Erfolgen in Serie beigebracht.",
        "Bostons Jayson Tatum erzielte 28 Punkte, doch im vierten Viertel übernahm Orlando mit einem furiosen 34:21-Lauf die Kontrolle. Desmond Bane war mit 24 Punkten der Matchwinner, wovon er 14 im Schlussabschnitt markierte. Nationalspieler Franz Wagner glänzte mit 22 Punkten und 7 Assists.",
        "Orlando verbessert sich damit auf eine Bilanz von 8-5. In weiteren Spielen feierten die Miami Heat ihren fünften Sieg in Serie beim 128:110 gegen Houston (Giannis 20 Punkte, 13 Rebounds), während Joel Embiid Philadelphia mit 37 Punkten zum 135:123 gegen Brooklyn führte."
      ]
    },
    "it": {
      "title": "Colpo Magic a Boston: Quarto periodo super per piegare i Celtics 115-105",
      "subtitle": "Desmond Bane realizza 24 punti e Franz Wagner ne aggiunge 22 nel parziale di 34-21 con cui Orlando espugna il TD Garden.",
      "excerpt": "Orlando Magic interrompe la striscia di sei vittorie dei Boston Celtics imponendosi 115-105 in trasferta. Miami prosegue la serie positiva.",
      "body": [
        "Gli Orlando Magic hanno firmato l'impresa della notte NBA di lunedì 16 novembre superando in rimonta i Boston Celtics per 115-105 sul parquet del TD Garden.",
        "Nonostante i 28 punti di Jayson Tatum per i padroni di casa, Orlando ha cambiato marcia nell'ultimo quarto con un parziale travolgente di 34-21. Desmond Bane è stato immarcabile segnando 14 dei suoi 24 punti nel finale, ben coadiuvato da Franz Wagner (22 punti e 7 assist).",
        "Grazie a questo successo Orlando sale a un record di 8-5. Nelle altre sfide di lunedì, Miami ha centrato la quinta vittoria di fila battendo Houston 128-110 grazie a Giannis Antetokounmpo (20 punti e 13 rimbalzi), mentre Joel Embiid ha dominato con 37 punti nel successo dei 76ers su Brooklyn (135-123)."
      ]
    },
    "pl": {
      "title": "Niespodzianka w Bostonie: Świetna czwarta kwarta Magic przerywa serię Celtics 115:105",
      "subtitle": "Desmond Bane rzuca 24 punkty, a Franz Wagner dokłada 22, gdy Orlando wygrywa decydującą kwartę 34:21.",
      "excerpt": "Orlando Magic odnoszą znakomite wyjazdowe zwycięstwo nad Boston Celtics 115:105 w TD Garden, zatrzymując rozpędzonych rywali.",
      "body": [
        "Koszykarze Orlando Magic sprawili ogromną niespodziankę w poniedziałkowy wieczór, 16 listopada, pokonując na wyjeździe Boston Celtics 115:105 w TD Garden i kończąc ich passę sześciu kolejnych zwycięstw.",
        "Jayson Tatum zdobył dla bostończyków 28 punktów, lecz w czwartej kwarcie defensywa gości zneutralizowała faworytów, a atak wygrał tę część gry 34:21. Liderem Magic okazał się Desmond Bane z 24 punktami (14 w czwartej kwarcie), dzielnie wspierany przez Franza Wagnera (22 punkty, 7 asyst).",
        "Orlando legitymuje się bilansem 8-5. W innych poniedziałkowych spotkaniach NBA Miami Heat wygrali piąty mecz z rzędu, pokonując Houston 128:110 z udziałem Giannisa Antetokounmpo (20 punktów, 13 zbiórek), a Joel Embiid zdobył 37 punktów w wygranej Philadelphii z Brooklynem 135:123."
      ]
    },
    "zh": {
      "title": "魔术末节逆袭波士顿：单节34-21终结凯尔特人六连胜 115-105",
      "subtitle": "贝恩砍下24分、小瓦格纳进账22分，奥兰多魔术在北岸花园球馆上演精彩翻盘好戏。",
      "excerpt": "奥兰多魔术末节发威115-105逆转波士顿凯尔特人，终结对手六连胜；热火击败火箭收获五连胜。",
      "body": [
        "11月16日周一晚间，奥兰多魔术队在波士顿TD花园球馆打出令人振奋的代表作，凭借第四节的压倒性表现以115-105逆转战胜凯尔特人队，终结了对手的六连胜势头。",
        "虽然塔图姆为凯尔特人拿下28分，但魔术队在决胜节凭借严密的高位夹击彻底锁死了主队进攻，打出单节34-21的悬殊比分。射手贝恩全场贡献24分，其中14分来自第四节；弗朗茨-瓦格纳贡献22分和7次助攻，带领魔术稳守胜局。",
        "此役过后魔术战绩提升至8胜5负。在周一的其他较量中，迈阿密热火在扬尼斯-阿德托昆博（20分13篮板）的带领下128-110大胜火箭豪取五连胜，而乔尔-恩比德狂轰37分帮助76人135-123击退篮网。"
      ]
    },
    "ja": {
      "title": "マジックが敵地でセルティックス撃破：第4Q怒涛の猛攻で連勝を6で止める 115-105",
      "subtitle": "デズモンド・ベインが24得点、フランツ・ヴァグナーが22得点。オーランドが勝負の第4Qを34-21と圧倒。",
      "excerpt": "オーランド・マジックがTDガーデンで115-105の逆転劇を演じボストンの連勝を阻止。ヒートは5連勝をマーク。",
      "body": [
        "11月16日月曜日、オーランド・マジックは敵地TDガーデンに乗り込み、第4クォーターでの怒涛の猛攻でボストン・セルティックスを115-105で下すアップセットを演じました。",
        "テイタムに28得点を許したものの、マジックは第4Qに強固なトラップディフェンスを展開し、34-21とボストンを圧倒。ベインが24得点（第4Qに14得点）、ヴァグナーが22得点7アシストを記録してチームを牽引しました。",
        "この勝利でマジックは8勝5敗に浮上。月曜日の他カードでは、ヤニス・アデトクンボ（20得点13リバウンド）を擁するマイアミ・ヒートがロケッツを128-110で下して5連勝を飾り、エンビードが37得点を挙げたシクサーズがネッツに勝利しました。"
      ]
    },
    "ko": {
      "title": "매직, 보스턴 원정서 대역전극: 4쿼터 폭발로 셀틱스 6연승 저지 115-105",
      "subtitle": "데스몬드 베인이 24득점, 프란츠 바그너가 22득점을 기록하며 올랜도가 마지막 쿼터를 34-21로 지배했습니다.",
      "excerpt": "올랜도 매직이 TD 가든에서 보스턴 셀틱스를 115-105로 꺾고 연승을 멈춰 세웠습니다. 마이애미 히트는 5연승을 달렸습니다.",
      "body": [
        "올랜도 매직이 11월 16일 월요일 밤 TD 가든에서 열린 NBA 경기에서 4쿼터 놀라운 집중력을 발휘하며 보스턴 셀틱스를 115-105로 격파하고 원정 대어를 낚았습니다.",
        "보스턴은 테이텀이 28득점을 올리며 앞서갔으나, 올랜도가 4쿼터 들어 강력한 수비 압박을 펼치며 34-21로 승부를 뒤집었습니다. 데스몬드 베인이 4쿼터에만 14점을 몰아넣으며 24득점 8리바운드를 기록했고, 프란츠 바그너가 22득점 7어시스트로 힘을 보탰습니다.",
        "이로써 올랜도는 8승 5패를 기록하며 동부 상위권 도약의 발판을 마련했습니다. 한편 마이애미는 야니스 아데토쿤보(20득점 13리바운드)를 앞세워 휴스턴을 128-110으로 꺾고 5연승을 질주했습니다."
      ]
    },
    "ar": {
      "title": "ماجيك يفاجئ سلتيكس: انتفاضة الربع الأخير توقف سلسلة انتصارات بوسطن 115-105",
      "subtitle": "ديزموند بين يسجل 24 نقطة وفرانز فاغنر يضيف 22 نقطة في عودة قوية لأورلاندو بنتيجة 34-21 في الربع الحاسم.",
      "excerpt": "أورلاندو ماجيك يحقق مفاجأة كبرى في بوسطن بالتفوق 115-105 على سلتيكس، بينما واصل ميامي هيت انتصاراته المتتالية بفضل يانيس.",
      "body": [
        "حقق أورلاندو ماجيك أبرز مفاجآت مساء الاثنين 16 نوفمبر في دوري كرة السلة الأمريكي بعدما قلب تأخره ليفوز على بوسطن سلتيكس بنتيجة 115-105 في صالة تي دي جاردن الشهيرة.",
        "ورغم تسجيل جيسون تيتوم 28 نقطة لبوسطن، فرض ماجيك هيمنة دفاعية وهجومية في الربع الرابع ليتفوق بنتيجة 34-21. وتألق النجم ديزموند بين بتسجيله 14 من أصل 24 نقطة له في الربع الأخير، إلى جانب 22 نقطة و7 تمريرات حاسمة من فرانز فاغنر.",
        "بهذا الفوز رفع أورلاندو رصيده إلى 8 انتصارات مقابل 5 هزائم. وفي مباريات أخرى، حقق ميامي هيت فوزه الخامس تواليا بتغلبه على هيوستن 128-110 بفضل تألق يانيس أنتيتوكونمبو (20 نقطة و13 متابعة)، بينما أحرز جويل إمبيد 37 نقطة في فوز فيلادلفيا على بروكلين 135-123."
      ]
    }
  },
  "atp-finals-turin-alcaraz-cruises-zverev-faces-shelton-tuesday-2026": {
    "fr": {
      "title": "Masters de Turin : Alcaraz déroule contre Tiafoe, Zverev défie Shelton mardi",
      "subtitle": "Carlos Alcaraz ne cède que quatre jeux dans le groupe Lendl, lançant idéalement sa semaine avant le duel Zverev-Shelton.",
      "excerpt": "Carlos Alcaraz écarte Frances Tiafoe 6-2, 6-2 en 69 minutes à Turin, Medvedev bat Cobolli et Alexander Zverev retrouve Ben Shelton mardi soir.",
      "body": [
        "Carlos Alcaraz a fait forte impression lundi 16 novembre aux Nitto ATP Finals de Turin en dominant nettement son ami Frances Tiafoe 6-2, 6-2 en seulement 69 minutes à l'Inalpi Arena.",
        "Le numéro 2 mondial espagnol a livré une partition limpide, distillant 24 coups gagnants sans concéder la moindre balle de break. Dans la session de soirée, Daniil Medvedev a fait respecter son expérience en maîtrisant l'Italien Flavio Cobolli 7-6 (4), 6-3 pour prendre la tête du groupe Ivan Lendl aux côtés d'Alcaraz.",
        "Mardi 17 novembre, le groupe John McEnroe est de retour avec en vedette le choc entre le numéro 1 mondial Alexander Zverev et l'Américain Ben Shelton, revanche de la finale de l'US Open 2026. Les deux joueurs ayant remporté leur premier match, le vainqueur fera un pas décisif vers le dernier carré."
      ]
    },
    "es": {
      "title": "Torneo de Maestros: Alcaraz arrolla a Tiafoe y Zverev se mide a Shelton este martes",
      "subtitle": "Carlos Alcaraz solo cede cuatro juegos en su debut en Turín para liderar el Grupo Lendl con autoridad.",
      "excerpt": "Carlos Alcaraz supera a Frances Tiafoe 6-2, 6-2 en 69 minutos en las Nitto ATP Finals de Turín, mientras Zverev y Shelton buscan el liderato en el Grupo McEnroe.",
      "body": [
        "Carlos Alcaraz comenzó su andadura en las Nitto ATP Finals de Turín este lunes 16 de noviembre con una victoria impecable ante Frances Tiafoe por 6-2 y 6-2 en apenas 69 minutos en el Inalpi Arena.",
        "El número 2 del mundo mostró una precisión formidable desde el fondo de pista, sumando 24 golpes ganadores y sin ceder una sola oportunidad de rotura con su servicio. En el turno de noche, Daniil Medvedev superó al local Flavio Cobolli por 7-6 (4) y 6-3 para sumar también su primer triunfo en el Grupo Ivan Lendl.",
        "La atención regresa el martes 17 de noviembre al Grupo John McEnroe con un duelo estelar nocturno entre el número 1 mundial Alexander Zverev y Ben Shelton, reedición de la final del Abierto de Estados Unidos 2026. Ambos marchan con balance de 1-0 y el vencedor dejará casi sellado su pase a semifinales."
      ]
    },
    "de": {
      "title": "ATP Finals Turin: Alcaraz fegt über Tiafoe hinweg, Zverev trifft am Dienstag auf Shelton",
      "subtitle": "Carlos Alcaraz gibt bei seinem Auftaktsieg in der Lendl-Gruppe nur vier Spiele ab und sendet eine deutliche Botschaft.",
      "excerpt": "Carlos Alcaraz schlägt Frances Tiafoe in 69 Minuten mit 6:2, 6:2. Daniil Medvedev siegt ebenfalls und Alexander Zverev bereitet sich auf Shelton vor.",
      "body": [
        "Carlos Alcaraz hat am Montag, 16. November, bei den Nitto ATP Finals in Turin ein deutliches Ausrufezeichen gesetzt und Frances Tiafoe in nur 69 Minuten mit 6:2, 6:2 bezwungen.",
        "Die spanische Nummer zwei der Welt glänzte in der Inalpi Arena mit 24 Gewinnschlägen und ließ während des gesamten Matches keinen einzigen Breakball zu. In der Abendsession bezwang Daniil Medvedev den italienischen Lokalmatador Flavio Cobolli mit 7:6 (4), 6:3.",
        "Am Dienstag, 17. November, richtet sich der Fokus wieder auf die John-McEnroe-Gruppe. Am Abend kommt es zum hochklassigen Duell zwischen Alexander Zverev und Ben Shelton, der Neuauflage des US-Open-Finals von 2026. Beide Spieler stehen bei 1:0 Siegen und kämpfen um die alleinige Tabellenführung."
      ]
    },
    "it": {
      "title": "Nitto ATP Finals Torino: Alcaraz domina Tiafoe, martedì sera sfida Zverev-Shelton",
      "subtitle": "Carlos Alcaraz lascia solo quattro game all'amico Tiafoe nel Gruppo Lendl; Medvedev batte Cobolli e martedì tocca a Zverev contro Shelton.",
      "excerpt": "Carlos Alcaraz apre il suo torneo con un perentorio 6-2, 6-2 su Tiafoe a Torino, mentre Medvedev piega Cobolli e Zverev sfida Shelton nel Gruppo McEnroe.",
      "body": [
        "Carlos Alcaraz ha debuttato con una prestazione impeccabile alle Nitto ATP Finals di Torino lunedì 16 novembre, superando Frances Tiafoe per 6-2, 6-2 in appena 69 minuti sul campo della Inalpi Arena.",
        "Lo spagnolo numero 2 del mondo ha mostrato un tennis di altissimo livello mettendo a segno 24 vincenti e non concedendo alcuna palla break. Nella sessione serale, Daniil Medvedev ha sconfitto Flavio Cobolli 7-6 (4), 6-3 in una sfida molto combattuta nel Gruppo Ivan Lendl.",
        "Martedì 17 novembre si torna in campo per il Gruppo John McEnroe. La sessione serale propone la rivincita della finale degli US Open 2026 tra il numero 1 del mondo Alexander Zverev e lo statunitense Ben Shelton, entrambi a quota una vittoria nella corsa per le semifinali."
      ]
    },
    "pl": {
      "title": "ATP Finals w Turynie: Alcaraz pewnie pokonuje Tiafoe, we wtorek starcie Zverev kontra Shelton",
      "subtitle": "Carlos Alcaraz oddaje zaledwie cztery gemy w meczu otwarcia grupy Lendl, a Medvedev ogrywa Cobollego.",
      "excerpt": "Carlos Alcaraz wygrywa z Francesem Tiafoe 6:2, 6:2 w 69 minut na inaugurację ATP Finals w Turynie, podczas gdy Alexander Zverev zagra we wtorek z Sheltonem.",
      "body": [
        "Carlos Alcaraz w znakomitym stylu rozpoczął rywalizację w turnieju Nitto ATP Finals w Turynie, pokonując w poniedziałek 16 listopada Francesa Tiafoe 6:2, 6:2 w zaledwie 69 minut gry w Inalpi Arena.",
        "Hiszpański wicelider rankingu zagrał niemal bezbłędnie, posyłając 24 uderzenia kończące i ani razu nie musząc bronić break pointa. W meczu wieczornym Daniił Miedwiediew wygrał z faworytem gospodarzy Flavio Cobollim 7:6 (4), 6:3.",
        "We wtorek 17 listopada zmagania wznawia grupa Johna McEnroe. W hicie wieczornej sesji lider rankingu Alexander Zverev zmierzy się z Benem Sheltonem w powtórce finału tegorocznego US Open, a stawką będzie samotne prowadzenie w tabeli."
      ]
    },
    "zh": {
      "title": "都灵年终总决赛：阿尔卡拉斯轻取蒂亚福，周二夜场兹维列夫大战谢尔顿",
      "subtitle": "阿尔卡拉斯在伦德尔组首战仅丢四局强势取胜，梅德韦杰夫击败科博利同取开门红。",
      "excerpt": "阿尔卡拉斯耗时69分钟以6-2、6-2横扫蒂亚福，都灵总决赛周二将迎来兹维列夫与谢尔顿的焦点对决。",
      "body": [
        "11月16日周一，2026年ATP年终总决赛在都灵伊纳尔皮竞技场展开第二比赛日争夺，世界第二阿尔卡拉斯展现统治级状态，仅用时69分钟便以6-2、6-2横扫好友蒂亚福取得开门红。",
        "全场比赛阿尔卡拉斯轰出24记制胜分且未面临任何破发点，反拍与发球表现极为稳健。在随后的晚场较量中，前赛会冠军梅德韦杰夫以7-6 (4)、6-3击败东道主新星科博利，同样收获伦德尔组首胜。",
        "11月17日周二赛事将重回麦肯罗组，晚场将迎来世界第一兹维列夫与美国名将谢尔顿的重量级对决，重演今年美网决赛巅峰对话。目前两人战绩均为1胜0负，胜者将牢牢占据小组出线主动权。"
      ]
    },
    "ja": {
      "title": "ATPファイナルズ・トリノ：アルカラスがティアフォーを圧倒、火曜夜はズベレフ対シェルトン",
      "subtitle": "アルカラスがレンドル組初戦をわずか4ゲーム喪失で快勝。メドベージェフも白星発進。",
      "excerpt": "アルカラスがティアフォーに6-2、6-2で69分勝利。火曜日のマッケンロー組ではズベレフとシェルトンが激突へ。",
      "body": [
        "11月16日月曜日、イタリア・トリノで開催中の日東ATPファイナルズで、世界ランク2位のカルロス・アルカラスが初戦に登場し、フランシス・ティアフォーを6-2、6-2と圧倒して白星発進を飾りました。",
        "アルカラスは24本のウィナーを放ち、相手に1度もブレークポイントを与えない完璧な試合運びを披露。夜の部ではダニール・メドベージェフがフラビオ・コボッリを7-6 (4)、6-3で退けました。",
        "11月17日火曜日はマッケンロー組の第2戦が行われ、ナイトセッションでは世界1位のアレクサンダー・ズベレフとベン・シェルトンが全米オープン決勝の再現となる注目の一戦を迎えます。"
      ]
    },
    "ko": {
      "title": "토리노 ATP 파이널스: 알카라스, 티아포에 완승…화요일 밤 즈베레프-셸턴 격돌",
      "subtitle": "카를로스 알카라스가 렌들 조 첫 경기서 단 4게임만 내주며 69분 만에 첫 승을 신고했습니다.",
      "excerpt": "알카라스가 티아포를 6-2, 6-2로 제압하며 순조롭게 출발한 가운데, 화요일에는 즈베레프와 셸턴의 빅매치가 열립니다.",
      "body": [
        "세계 랭킹 2위 카를로스 알카라스가 11월 16일 월요일 이탈리아 토리노 이날피 아레나에서 열린 2026 니토 ATP 파이널스 이반 렌들 조 첫 경기에서 프랜시스 티아포를 6-2, 6-2로 완파했습니다.",
        "알카라스는 69분 동안 24개의 위너를 터뜨렸고 단 하나의 브레이크 포인트도 허용하지 않는 완벽한 서브 게임을 펼쳤습니다. 야간 경기에서는 다닐 메드베데프가 플라비오 코볼리를 7-6 (4), 6-3으로 꺾었습니다.",
        "11월 17일 화요일에는 존 매켄로 조 경기가 이어지며, 2026 US 오픈 결승 리턴 매치인 세계 1위 알렉산더 즈베레프와 벤 셸턴의 맞대결이 야간 세션에서 펼쳐집니다."
      ]
    },
    "ar": {
      "title": "نهائيات تورينو للتنس: ألكاراز يتألق أمام تيافو وزفيريف في مواجهة شيلتون مساء الثلاثاء",
      "subtitle": "كارلوس ألكاراز يخسر أربعة أشواط فقط في مستهل مشواره بمجموعة ليندل، وميدفيديف يتخطى كوبولي.",
      "excerpt": "كارلوس ألكاراز يتغلب على فرانسيس تيافو 6-2 و6-2 في 69 دقيقة بتورينو، وزفيريف يلتقي شيلتون في قمة مرتقبة الثلاثاء.",
      "body": [
        "استهل النجم الإسباني كارلوس ألكاراز مشاركته في نهائيات الجولة العالمية للرجال في تورينو يوم الاثنين 16 نوفمبر بانتصار ساحق على صديقه الأمريكي فرانسيس تيافو بنتيجة 6-2 و6-2 في غضون 69 دقيقة بصالة إينالبي أرينا.",
        "ولم يواجه المصنف الثاني عالميا أي نقطة لكسر إرساله طوال اللقاء، مسجلا 24 ضربة قاضية. وفي الفترة المسائية، تغلب الروسي دانييل ميدفيديف على الإيطالي فلافيو كوبولي بنتيجة 7-6 و6-3 ضمن مجموعة إيفان ليندل.",
        "وتتجه الأنظار يوم الثلاثاء 17 نوفمبر إلى مجموعة جون ماكنرو، حيث يلتقي المصنف الأول عالميا ألكسندر زفيريف مع الأمريكي بن شيلتون في إعادة لنهائي بطولة أمريكا المفتوحة 2026، حيث يسعى كلاهما لفض الشراكة على الصدارة."
      ]
    }
  },
  "golf-rsm-classic-fedexcup-fall-finale-sea-island-bubble-cards-2026": {
    "fr": {
      "title": "Finale à Sea Island : Le RSM Classic attribue les dernières cartes PGA Tour pour 2027",
      "subtitle": "Les parcours d'entraînement ont débuté en Géorgie pour le dénouement de la FedExCup Fall avec d'immenses enjeux pour les joueurs du cut-off.",
      "excerpt": "La saison du PGA Tour s'achève au Sea Island Golf Club où les cartes d'exemption du top 125 et les places pour les Signature Events se jouent ce week-end.",
      "body": [
        "Le dernier chapitre de la saison 2026 du PGA Tour s'est ouvert mardi 17 novembre avec les premiers entraînements officiels sur les parcours Seaside et Plantation du Sea Island Golf Club, en vue du RSM Classic (19-22 novembre).",
        "Organisé par Davis Love III en Géorgie, ce tournoi représente le juge de paix pour les golfeurs classés autour de la fatidique 125e place de la FedExCup. Seuls les 125 premiers au terme des quatre tours conserveront une exemption complète sur le circuit américain en 2027.",
        "En parallèle, les joueurs situés entre la 51e et la 60e place se disputent les précieux accès aux Signature Events du début de saison 2027. L'enfant du pays Davis Thompson, le double vainqueur Mackenzie Hughes et Austin Smotherman sont particulièrement attendus."
      ]
    },
    "es": {
      "title": "Duelo en Sea Island: The RSM Classic reparte las tarjetas del PGA Tour de 2027",
      "subtitle": "Comienzan las rondas de práctica en Georgia para el cierre del FedExCup Fall con puestos decisivos en juego.",
      "excerpt": "El PGA Tour concluye su temporada regular en Sea Island con la pelea por meterse entre los 125 mejores y asegurarse la tarjeta completa para 2027.",
      "body": [
        "El desenlace de la temporada 2026 del PGA Tour arrancó este martes 17 de noviembre en los campos Seaside y Plantation de Sea Island Golf Club con las rondas de práctica de The RSM Classic (19-22 de noviembre).",
        "Con Davis Love III como anfitrión en St. Simons Island, Georgia, el certamen define qué jugadores finalizarán dentro del top 125 de la FedExCup para retener sus derechos completos de juego en la temporada 2027.",
        "Asimismo, los golfistas entre los puestos 51 y 60 luchan por las invitaciones a los torneos Signature de inicio de curso. El local Davis Thompson, el bicampeón Mackenzie Hughes y Austin Smotherman encabezan la lista de candidatos."
      ]
    },
    "de": {
      "title": "Showdown in Sea Island: Die RSM Classic entscheidet über die PGA Tour Karten für 2027",
      "subtitle": "Die Trainingsrunden in Georgia haben begonnen. Beim FedExCup Fall Finale steht die Zukunft vieler Profis auf dem Spiel.",
      "excerpt": "Die PGA Tour Saison steuert bei der RSM Classic auf ihren Höhepunkt zu, wo die letzten Vollmitgliedschaften für die Top 125 vergeben werden.",
      "body": [
        "Das letzte Kapitel der PGA Tour Saison 2026 hat am Dienstag, 17. November, mit den Trainingsrunden auf dem Seaside und Plantation Course im Sea Island Golf Club für The RSM Classic (19.-22. November) begonnen.",
        "Das von Hall-of-Famer Davis Love III ausgerichtete Event ist das nervenaufreibendste Turnier des Jahres. Nur die besten 125 Spieler der FedExCup-Rangliste besitzen nach dem Finaltag am Sonntag die volle Spielberechtigung für 2027.",
        "Zusätzlich kämpfen die Profis auf den Rängen 51 bis 60 um Startplätze bei den lukrativen Signature Events. Lokalmatador Davis Thompson, der zweimalige Turniersieger Mackenzie Hughes und Austin Smotherman stehen im Fokus."
      ]
    },
    "it": {
      "title": "Sea Island decisiva: Il RSM Classic assegna le carte per il PGA Tour 2027",
      "subtitle": "Iniziati i giri di prova in Georgia per l'atto conclusivo della FedExCup Fall con la caccia alla top 125.",
      "excerpt": "La stagione del PGA Tour si chiude a Sea Island con le ultime esenzioni piene per il 2027 e i posti per i Signature Events in palio.",
      "body": [
        "L'ultimo appuntamento della stagione 2026 del PGA Tour è entrato nel vivo martedì 17 novembre con le giornate di prova al Sea Island Golf Club in vista del The RSM Classic (19-22 novembre).",
        "Ospitato da Davis Love III in Georgia, il torneo rappresenta l'ultima spiaggia per i giocatori a ridosso della 125esima posizione della FedExCup, traguardo indispensabile per garantire la carta piena nel 2027.",
        "In palio ci sono anche i pass per i prestigiosi Signature Events destinati ai classificati tra il 51esimo e il 60esimo posto. Tra i protagonisti più attesi figurano il beniamino di casa Davis Thompson, il due volte vincitore Mackenzie Hughes e Austin Smotherman."
      ]
    },
    "pl": {
      "title": "Finał w Sea Island: Turniej RSM Classic rozstrzyga o kartach PGA Tour na 2027 rok",
      "subtitle": "W Georgii rozpoczęły się rundy treningowe przed finałem FedExCup Fall, gdzie toczy się walka o przyszłość wielu golfistów.",
      "excerpt": "Sezon PGA Tour dobiega końca w Sea Island Golf Club, gdzie zawodnicy walczą o utrzymanie w czołowej 125 i prawo gry w sezonie 2027.",
      "body": [
        "Ostatni rozdział sezonu PGA Tour 2026 rozpoczął się we wtorek 17 listopada rundami treningowymi na polach Seaside i Plantation w Sea Island Golf Club przed turniejem The RSM Classic (19-22 listopada).",
        "Turniej, którego gospodarzem jest Davis Love III, to ostateczny sprawdzian dla graczy z okolic 125. miejsca w rankingu FedExCup. Tylko gracze z czołowej 125 zachowają pełną kartę zawodniczą na kolejny rok.",
        "Równolegle toczy się walka o miejsca 51-60 dające prawo startu w prestiżowych turniejach Signature Events. Wśród faworytów lokalnych kibiców znajdują się Davis Thompson, dwukrotny mistrz Mackenzie Hughes oraz Austin Smotherman."
      ]
    },
    "zh": {
      "title": "海岛决战：RSM精英赛决定2027年美巡赛全卡归属与标志赛事席位",
      "subtitle": "美巡赛秋季赛收官战在佐治亚州展开官方练习轮，保卡边缘球手迎来生涯关键战役。",
      "excerpt": "2026赛季美巡赛在海岛高尔夫俱乐部迎来收官大戏，前125名全卡资格以及前60名标志赛事豁免权将在此尘埃落定。",
      "body": [
        "2026赛季美巡赛的最终篇章于11月17日周二在佐治亚州海岛高尔夫俱乐部拉开帷幕，球员们在海滨球场与种植园球场展开RSM精英赛（11月19-22日）的官方练习轮。",
        "由高球名人堂成员戴维斯-拉夫三世主持的这项赛事是巡回赛最具戏剧性的保卡之战。在周日决赛轮结束后，只有位列联邦快递杯积分榜前125名的球手才能获得2027赛季美巡赛的全豁免参赛资格。",
        "与此同时，排名第51至60位的球手还在争夺明年初圆石滩职业业余配对赛等高奖金标志赛事的参赛名额。本土作战的戴维斯-汤普森、两届赛会冠军麦肯齐-休斯以及斯莫瑟曼均在参赛名单之中。"
      ]
    },
    "ja": {
      "title": "シーアイランド決戦：RSMクラシックで2027年PGAツアー出場権が決着へ",
      "subtitle": "ジョージア州でフェデックスカップ・フォール最終戦の練習ラウンドが開始。当落線上の選手たちが命運を懸ける。",
      "excerpt": "PGAツアーの今季最終戦がシーアイランドGCで開幕。来季シード権獲得となるトップ125と昇格枠を懸けた熾烈な戦い。",
      "body": [
        "2026年のPGAツアーを締めくくるRSMクラシック（11月19-22日）の練習ラウンドが11月17日火曜日、ジョージア州シーアイランドGCで始まりました。",
        "デービス・ラブ3世がホストを務める本大会は、フェデックスカップランキング125位のボーダーライン上にいる選手たちにとって来季のフルシード権を懸けた最後の戦いとなります。",
        "さらに51位から60位の選手には来季序盤のシグネチャー大会への出場資格が懸かっており、地元期待のデービス・トンプソンや2度の優勝経験を持つマッケンジー・ヒューズらに注目が集まります。"
      ]
    },
    "ko": {
      "title": "시 아일랜드 최종전: RSM 클래식서 2027 PGA 투어 출전권 격돌",
      "subtitle": "조지아주에서 페덱스컵 폴 피날레 공식 연습 라운드가 시작되며 125위 잔류를 향한 혈투가 개막했습니다.",
      "excerpt": "2026시즌 PGA 투어의 마지막 정규 대회가 시 아일랜드 골프클럽에서 열리며 내년도 풀시드권 125장의 주인공이 결정됩니다.",
      "body": [
        "2026 PGA 투어 시즌 최종전인 The RSM 클래식(11월 19-22일)의 공식 연습 라운드가 11월 17일 화요일 미국 조지아주 세인트 시먼스 아일랜드의 시 아일랜드 골프클럽에서 시작되었습니다.",
        "데이비스 러브 3세가 주최하는 이 대회는 페덱스컵 랭킹 125위 진입을 노리는 버블권 선수들의 치열한 생존 무대입니다. 일요일 최종 라운드 결과에 따라 2027시즌 전 경기 출전권의 향방이 갈립니다.",
        "또한 51위부터 60위 사이의 선수들은 시즌 초반 특급 대회 출전권 확보를 노립니다. 지역 출신인 데이비스 톰슨과 2회 우승자 매켄지 휴즈, 오스틴 스모더먼 등이 출격합니다."
      ]
    },
    "ar": {
      "title": "حسم سي آيلاند: بطولة آر إس إم كلاسيك تحدد بطاقات جولة البي جي إيه لعام 2027",
      "subtitle": "انطلاق الجولات التدريبية في ولاية جورجيا لختام الموسم مع صراع شرس للاعبي المراكز الأخيرة للحفاظ على بطاقاتهم.",
      "excerpt": "موسم جولة البي جي إيه للجولف يختتم فعالياته في سي آيلاند حيث يتنافس اللاعبون لضمان التواجد ضمن أفضل 125 لاعبا للموسم المقبل.",
      "body": [
        "انطلقت الجولات التدريبية الرسمية لبطولة آر إس إم كلاسيك (19-22 نوفمبر) يوم الثلاثاء 17 نوفمبر على ملاعب نادي سي آيلاند للجولف في ولاية جورجيا الأمريكية لتسدل الستار على موسم 2026.",
        "وتعد البطولة التي يستضيفها ديفيس لوف الثالث الفرصة الأخيرة للاعبين الواقعين على حافة المراكز الـ 125 الأولى في ترتيب فيديكس كب لضمان العضوية الكاملة والمعفاة لجولة عام 2027 وتفادي خوض التصفيات.",
        "كما تشهد البطولة منافسة قوية بين أصحاب المراكز من 51 إلى 60 لخطف بطاقات التأهل للأحداث الكبرى في مطلع الموسم الجديد، يتقدمهم المحلي ديفيس طومسون وبطل النسختين السابقتين ماكنزي هيوز."
      ]
    }
  },
  "f1-two-days-las-vegas-strip-shootout-p2-verstappen-norris-2026": {
    "fr": {
      "title": "Deux jours avant Las Vegas : Le Strip est prêt pour la bataille à cinq pour la place de dauphin",
      "subtitle": "L'installation du paddock s'achève dans le Nevada alors que Verstappen et Norris ne sont séparés que de 33 points avant les trois dernières courses.",
      "excerpt": "La Formule 1 s'installe à Las Vegas pour la 21e manche. Kimi Antonelli et Mercedes titrés, un combat féroce oppose cinq pilotes pour la deuxième place mondiale.",
      "body": [
        "À seulement deux jours des premiers essais sur le Strip illuminé de Las Vegas, le paddock de la Formule 1 a achevé son installation mardi 17 novembre en vue de la 21e manche de la saison (19-21 novembre).",
        "Tandis que le phénomène italien Kimi Antonelli et l'écurie Mercedes ont d'ores et déjà coiffé les couronnes mondiales au Brésil, la lutte pour la place de vice-champion reste totalement indécise. Cinq pilotes se tiennent en 33 points : Max Verstappen (279), George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) et Lando Norris (246).",
        "Le tracé urbain de 6,201 km et ses longues lignes droites dans la fraîcheur du désert mettront les freins et la gestion des pneus à rude épreuve. Chez les constructeurs, Ferrari (510 points) tente de conserver sa deuxième place face à Red Bull (415) et McLaren (398)."
      ]
    },
    "es": {
      "title": "Dos días para Las Vegas: El Strip listo para la batalla a cinco por el subcampeonato",
      "subtitle": "Concluye el montaje del paddock en Nevada con Verstappen y Norris separados por apenas 33 puntos a falta de tres carreras.",
      "excerpt": "La Fórmula 1 llega a Las Vegas para la Ronda 21. Con Kimi Antonelli ya campeón, cinco pilotos se disputan el segundo lugar mundial.",
      "body": [
        "A falta de solo dos días para que rujan los motores por Las Vegas Boulevard, el paddock de la Fórmula 1 completó su montaje este martes 17 de noviembre para el Gran Premio de Las Vegas (19-21 de noviembre).",
        "Con Kimi Antonelli y Mercedes ya consagrados como campeones del mundo en Brasil, la atención se centra en la vibrante pugna por el subcampeonato de pilotos, donde solo 33 puntos separan a cinco aspirantes: Max Verstappen (279), George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) y Lando Norris (246).",
        "El trazado callejero de 6,201 kilómetros exigirá el máximo rendimiento en velocidad punta y calentamiento de neumáticos ante las bajas temperaturas nocturnas del desierto. En constructores, Ferrari (510) defiende el segundo puesto ante Red Bull (415) y McLaren (398)."
      ]
    },
    "de": {
      "title": "Zwei Tage bis Vegas: Der Strip ist bereit für den Fünfkampf um die Vizemeisterschaft",
      "subtitle": "Der Paddock-Aufbau in Nevada ist abgeschlossen. Verstappen und Norris trennen vor den letzten drei Saisonrennen nur 33 Punkte.",
      "excerpt": "Die Formule 1 reist zum 21. Saisonlauf nach Las Vegas. Während Antonelli bereits Weltmeister ist, tobt ein heißer Kampf um Platz zwei.",
      "body": [
        "Nur noch zwei Tage trennen die Fans vom ersten Freien Training auf dem beleuchteten Strip von Las Vegas. Der Formel-1-Tross schloss am Dienstag, 17. November, die Vorbereitungen im Fahrerlager ab.",
        "Obwohl Kimi Antonelli und Mercedes den WM-Titel bereits in Brasilien perfekt machten, verspricht das Saisonfinale Hochspannung. Fünf Fahrer liegen im Kampf um Platz zwei innerhalb von nur 33 Punkten: Max Verstappen (279), George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) und Lando Norris (246).",
        "Der 6,201 Kilometer lange Stadtkurs mit seiner 1,9 Kilometer langen Vollgaspassage verlangt den Autos bei nächtlichen Wüstentemperaturen unter 12 Grad alles ab. Bei den Konstrukteuren verteidigt Ferrari (510 Punkte) Platz zwei gegen Red Bull (415) und McLaren (398)."
      ]
    },
    "it": {
      "title": "Due giorni a Las Vegas: La Strip è pronta per la sfida a cinque per il secondo posto",
      "subtitle": "Conclusi i preparativi nel paddock in Nevada con Verstappen e Norris racchiusi in 33 punti prima degli ultimi tre appuntamenti.",
      "excerpt": "La Formula 1 approda a Las Vegas per il Round 21. Con Antonelli iridato, la battaglia per la piazza d'onore mondiale entra nel vivo.",
      "body": [
        "A sole 48 ore dall'accensione dei motori sulla Strip illuminata di Las Vegas, il paddock della Formula 1 ha completato i preparativi martedì 17 novembre in vista del Gran Premio di Las Vegas (19-21 novembre).",
        "Con il giovane Kimi Antonelli e la Mercedes già campioni del mondo, l'interesse è tutto concentrato sulla corsa al titolo di vicecampione del mondo: cinque piloti sono racchiusi in appena 33 punti, guidati da Max Verstappen (279) davanti a George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) e Lando Norris (246).",
        "Il tracciato cittadino di 6,201 km metterà a dura prova gli impianti frenanti e la temperatura degli pneumatici nel freddo notturno del deserto. Tra i costruttori la Ferrari (510 punti) difende il secondo posto dall'assalto di Red Bull (415) e McLaren (398)."
      ]
    },
    "pl": {
      "title": "Dwa dni do Vegas: Tor na Strip gotowy na pięcioosobową batalię o wicemistrzostwo",
      "subtitle": "Montaż padoku w Nevadzie dobiegł końca. Verstappena i Norrisa dzielą zaledwie 33 punkty przed trzema ostatnimi rundami.",
      "excerpt": "Formuła 1 zawitała do Las Vegas na 21. rundę sezonu. Kimi Antonelli jest już mistrzem, lecz walka o drugie miejsce rozgrzewa stawkę.",
      "body": [
        "Zostały zaledwie dwa dni do rozpoczęcia nocnych treningów na oświetlonym Las Vegas Strip. We wtorek 17 listopada padok Formuły 1 zakończył instalację przed Grand Prix Las Vegas (19-21 listopada).",
        "Choć Kimi Antonelli i Mercedes zapewnili sobie tytuły mistrzowskie w Brazylii, walka o drugie miejsce w klasyfikacji kierowców pozostaje niezwykle zacięta. Pięciu kierowców dzieli zaledwie 33 punkty: Max Verstappen ma 279 punktów, a za nim plasują się George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) i Lando Norris (246).",
        "Uliczny tor o długości 6,201 km z długą prostą na Las Vegas Boulevard będzie ogromnym wyzwaniem dla dogrzewania opon w chłodne pustynne noce. Wśród konstruktorów Ferrari (510 punktów) broni pozycji wicelidera przed Red Bullem (415) i McLarenem (398)."
      ]
    },
    "zh": {
      "title": "决战拉斯维加斯倒计时两天：赌城大道就绪，年度亚军五方混战一触即发",
      "subtitle": "内华达围场搭建周二收官，维斯塔潘与诺里斯在最后三站前仅相差33分。",
      "excerpt": "F1第21站移师拉斯维加斯。在安东内利与梅赛德斯加冕后，车手积分榜第二名的争夺进入白热化阶段。",
      "body": [
        "距离拉斯维加斯大道灯火辉煌的夜间练习赛仅剩两天时间，F1围场于11月17日周二完成了各项准备工作，迎接第21站拉斯维加斯大奖赛（11月19-21日）的到来。",
        "尽管梅赛德斯超新星安东内利已在巴西站锁定世界冠军，但年度亚军争夺战依然悬念重重。在仅剩的三场比赛中，前六名中的五位车手分差仅有33分：维斯塔潘以279分暂列第二，紧随其后的是拉塞尔（262分）、汉密尔顿（261分）、勒克莱尔（249分）和诺里斯（246分）。",
        "全长6.201公里的城市街道赛道拥有长达1.9公里的全油门直道，夜间沙漠低于12度的低温将对轮胎升温带来严峻考验。车队积分榜上，法拉利（510分）正全力捍卫对红牛（415分）与迈凯伦（398分）的领先优势。"
      ]
    },
    "ja": {
      "title": "ラスベガス開幕まであと2日：ストリップ決戦を前にランキング2位争いが白熱",
      "subtitle": "パドック設営が完了。フェルスタッペンからノリスまでわずか33点差の熾烈な副賞争いへ。",
      "excerpt": "F1第21戦ラスベガスGPの木曜走行まで2日。すでに王座を決めたアントネッリの背後で5人のドライバーが激突。",
      "body": [
        "華やかな光に包まれるラスベガス・ストリップでの走行開始まであと2日となり、F1パドックは11月17日火曜日にネバダ州での設営作業を完了しました。",
        "キミ・アントネッリとメルセデスがすでに戴冠を決めたものの、シリーズ2位争いは極めて白熱しています。2位のマックス・フェルスタッペン（279点）からジョージ・ラッセル（262点）、ルイス・ハミルトン（261点）、シャルル・ルクレール（249点）、ランド・ノリス（246点）までわずか33点差にひしめき合っています。",
        "全長6.201kmのコースでは、12度を下回る砂漠の夜間冷え込みによるタイヤ作動温度の確保が鍵を握ります。製造者部門ではフェラーリ（510点）がレッドブル（415点）とマクラーレン（398点）の追撃を振り切れるか注目されます。"
      ]
    },
    "ko": {
      "title": "라스베이거스 스트립 D-2: 드라이버 준우승 5인 혼전 속 서킷 준비 완료",
      "subtitle": "네바다 패덕 설치 완료. 마지막 세 경기를 앞두고 베르스타펜과 노리스의 격차는 33점에 불과합니다.",
      "excerpt": "F1 21라운드 라스베이거스 그랑프리 개막 이틀 전, 키미 안토넬리에 이은 챔피언십 2위 자리를 놓고 5명의 드라이버가 격돌합니다.",
      "body": [
        "화려한 조명이 빛나는 라스베이거스 스트립 서킷 첫 연습 주행까지 이틀을 남겨두고, F1 패덕은 11월 17일 화요일 라스베이거스 그랑프리(11월 19-21일) 준비를 모두 마쳤습니다.",
        "메르세데스의 키미 안토넬리가 브라질에서 월드 챔피언십을 조기 확정지었지만, 드라이버 부문 2위 경쟁은 마지막까지 불꽃을 튀기고 있습니다. 2위 막스 베르스타펜(279점)부터 조지 러셀(262점), 루이스 해밀턴(261점), 샤를 르클레르(249점), 랜도 노里斯(246점)까지 5명의 점수 차는 단 33점에 불과합니다.",
        "길이 6.201km의 도심 서킷에서 펼쳐질 이번 레이스는 12도 이하로 떨어지는 사막의 쌀쌀한 밤 기온 속에서 타이어 온도를 올리는 것이 핵심 과제입니다. 컨스트럭터 부문에서는 페라리(510점)가 레드불(415점)과 맥라렌(398점)의 추격을 방어해야 합니다."
      ]
    },
    "ar": {
      "title": "يومان على جائزة لاس فيغاس: حلبة ستريب جاهزة لمعركة خماسية شرسة على وصافة العالم",
      "subtitle": "انتهاء تجهيزات البادوك في نيفادا وسط فارق لا يتعدى 33 نقطة بين فيرستابن ونوريس قبل ثلاث جولات على الختام.",
      "excerpt": "الفورمولا 1 تستعد لانطلاق الجولة 21 في لاس فيغاس. مع تتويج كيمي أنتونيللي، يشتعل الصراع بين خمسة سائقين على المركز الثاني.",
      "body": [
        "مع تبقي 48 ساعة فقط على دوران المحركات تحت أضواء لاس فيغاس الساحرة، استكملت فرق الفورمولا 1 تجهيزات البادوك يوم الثلاثاء 17 نوفمبر استعدادا لسباق جائزة لاس فيغاس الكبرى (19-21 نوفمبر).",
        "ورغم حسم الإيطالي الشاب كيمي أنتونيللي وفريق مرسيدس لقبي بطولة العالم في البرازيل، فإن المعركة على مركز الوصافة تزداد اشتعالا؛ حيث تفصل 33 نقطة فقط بين خمسة متسابقين يتقدمهم ماكس فيرستابن (279 نقطة) وجورج راسل (262) ولويس هاميلتون (261) وشارل لوكلير (249) ولاندو نوريس (246).",
        "وسيكون المسار البالغ طوله 6.201 كم والمنعطفات السريعة اختبارا شاقا للإطارات في ظل برودة ليل الصحراء التي تنخفض دون 12 درجة مئوية. وفي صراع الصانعين، تدافع فيراري (510 نقاط) عن مركزها الثاني أمام تهديد رد بول (415) ومكلارين (398)."
      ]
    }
  }
}

# Verify no em-dashes or double-hyphens in the data
for slug, locales in translations_data.items():
    for loc, d in locales.items():
        for field in ["title", "subtitle", "excerpt"]:
            val = d[field]
            if "\u2014" in val:
                raise ValueError(f"Em-dash in {slug} {loc} {field}")
            if "--" in val:
                raise ValueError(f"Double-hyphen in {slug} {loc} {field}")
        for p in d["body"]:
            if "\u2014" in p:
                raise ValueError(f"Em-dash in body {slug} {loc}")
            if "--" in p:
                raise ValueError(f"Double-hyphen in body {slug} {loc}")

print("Pre-check passed: Zero em-dashes or double-hyphens in translation payload.")

# Now read stories.ts
txt = open(STORIES_TS, "r", encoding="utf-8").read()

# Build the TypeScript code for the new entries
import json

new_entries_ts = []
for slug, locales in translations_data.items():
    # If slug is already in txt, check if we need to replace or skip
    if f'"{slug}":' in txt:
        print(f"Slug {slug} already present in stories.ts, skipping insertion.")
        continue
    entry_code = f'  "{slug}": ' + json.dumps(locales, ensure_ascii=False, indent=4) + ",\n"
    new_entries_ts.append(entry_code)

if new_entries_ts:
    # Find the end of export const STORY_I18N: Record<string, LocMap> = { ... };
    # We replace the closing "};\n" with the new entries and then "};\n"
    last_brace_idx = txt.rfind("};\n")
    if last_brace_idx == -1:
        last_brace_idx = txt.rfind("};")
    
    updated_txt = txt[:last_brace_idx] + "".join(new_entries_ts) + "};\n"
    open(STORIES_TS, "w", encoding="utf-8").write(updated_txt)
    print(f"Added {len(new_entries_ts)} story translations to stories.ts.")
else:
    print("No new translations needed.")

