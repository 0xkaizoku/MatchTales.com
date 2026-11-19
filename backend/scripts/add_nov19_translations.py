"""Add 10-language translations for the 6 new stories on 2026-11-19."""
import os
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
STORIES_TS = os.path.join(ROOT, "frontend", "src", "i18n", "stories.ts")

translations_data = {
  "atp-finals-turin-shelton-fils-zverev-mcenroe-deciders-2026": {
    "fr": {
      "title": "Tension à Turin : Shelton et Fils luttent pour le dernier billet en demi-finale",
      "subtitle": "Alexander Zverev étant déjà qualifié à 2-0, Ben Shelton et Arthur Fils se disputent la deuxième place du groupe McEnroe ce jeudi.",
      "excerpt": "Alors qu'Alcaraz a rejoint le dernier carré dans le groupe Lendl, la phase de poules s'achève à Turin avec d'immenses enjeux de qualification.",
      "body": [
        "La lutte pour le dernier carré des Nitto ATP Finals 2026 atteint son paroxysme ce jeudi 19 novembre, alors que le groupe John McEnroe dispute ses rencontres décisives à l'Inalpi Arena de Turin.",
        "Le numéro 1 mondial Alexander Zverev est déjà assuré de disputer les demi-finales de samedi grâce à deux succès sans concéder le moindre set, dont une victoire 6-2, 7-6 (4) contre Ben Shelton mardi. Derrière lui, la course à la deuxième place reste totalement indécise.",
        "Arthur Fils a relancé ses espoirs mardi en renversant le jeune Rafael Jodar 4-6, 6-2, 6-2 pour équilibrer son bilan à 1-1. Le Français défie Zverev en soirée à 20h30, tandis que Shelton affronte Jodar à 14h00, sachant qu'un succès en deux sets lui conférerait un avantage déterminant au jeu des pourcentages."
      ]
    },
    "es": {
      "title": "Tensión en Turín: Shelton y Fils pelean por el pase a semifinales en el Grupo McEnroe",
      "subtitle": "Con Alexander Zverev clasificado con marca de 2-0, Ben Shelton y Arthur Fils buscan este jueves el último billete a semifinales.",
      "excerpt": "Con Carlos Alcaraz ya en semifinales por el Grupo Lendl, la fase de grupos concluye en Turín con máxima emoción y plazas en juego.",
      "body": [
        "La batalla por las semifinales de las Nitto ATP Finals 2026 alcanza su punto álgido este jueves 19 de noviembre, con el desenlace del Grupo John McEnroe en el Inalpi Arena de Turín.",
        "El número 1 del mundo, Alexander Zverev, ya tiene asegurado el liderato y su plaza en el fin de semana tras vencer 6-2, 7-6 (4) a Ben Shelton el martes. Por detrás, la lucha por el segundo puesto está al rojo vivo entre Shelton y el francés Arthur Fils.",
        "Fils sumó su primer triunfo al remontar ante Rafael Jódar por 4-6, 6-2 y 6-2, y se mide a Zverev a las 20:30. Antes, a las 14:00, Shelton se enfrenta a Jódar sabiendo que una victoria en dos parciales puede resultar decisiva para el desempate por sets."
      ]
    },
    "de": {
      "title": "Hochspannung in Turin: Shelton und Fils kämpfen um das Halbfinalticket",
      "subtitle": "Alexander Zverev steht mit 2:0 Siegen bereits im Halbfinale, während Ben Shelton und Arthur Fils am Donnerstag um Platz zwei duellieren.",
      "excerpt": "Nachdem Carlos Alcaraz in der Lendl-Gruppe das Weiterkommen fixierte, fällt am Donnerstag in Turin die Entscheidung in der McEnroe-Gruppe.",
      "body": [
        "Der Kampf um das Halbfinale der Nitto ATP Finals 2026 spitzt sich am Donnerstag, 19. November, in der Turiner Inalpi Arena dramatisch zu.",
        "Branchenprimus Alexander Zverev hat seinen Halbfinalplatz nach zwei glatten Zweisatzsiegen, darunter das 6:2, 7:6 (4) gegen Ben Shelton, bereits sicher. Hinter dem Hamburger kämpfen Shelton und Arthur Fils im Fernduell um das verbleibende Halbfinalticket.",
        "Fils wahrte seine Chancen mit einem Dreisatzsieg über Rafael Jódar und fordert Zverev um 20:30 Uhr heraus. Zuvor trifft Shelton um 14:00 Uhr auf den noch sieglosen Jódar, wo jeder verlorene Satz das Aus bedeuten könnte."
      ]
    },
    "it": {
      "title": "Tensione a Torino: Shelton e Fils si contendono l'ultimo posto in semifinale",
      "subtitle": "Con Alexander Zverev già qualificato sul 2-0, Ben Shelton e Arthur Fils si giocano il passaggio del turno giovedì al Pala Inalpi.",
      "excerpt": "Dopo la qualificazione di Alcaraz nel gruppo Lendl, il round robin di Torino si chiude con sfide decisive nel gruppo McEnroe.",
      "body": [
        "La caccia alle semifinali delle Nitto ATP Finals 2026 vive giovedì 19 novembre la sua giornata decisiva per il Gruppo John McEnroe all'Inalpi Arena di Torino.",
        "Il numero 1 del mondo Alexander Zverev ha già staccato il pass per le semifinali grazie al successo per 6-2, 7-6 (4) su Shelton. Alle sue spalle, Arthur Fils e Ben Shelton si contendono a distanza la seconda piazza con un record di 1-1 ciascuno.",
        "Fils è chiamato all'impresa serale contro Zverev alle 20:30, mentre Shelton affronta alle 14:00 lo spagnolo Rafael Jodar con l'obiettivo di vincere in due set per massimizzare il quoziente set."
      ]
    },
    "pl": {
      "title": "Emocje w Turynie: Shelton i Fils walczą o awans do półfinału w grupie McEnroe",
      "subtitle": "Alexander Zverev jest już pewny gry w półfinale, a Ben Shelton i Arthur Fils toczą we czwartek korespondencyjny bój o drugie miejsce.",
      "excerpt": "Po awansie Carlosa Alcaraza w grupie Lendl, rywalizacja grupowa w Turynie dobiega końca w pełnym napięcia czwartkowym finiszu.",
      "body": [
        "Walka o czołową czwórkę turnieju Nitto ATP Finals 2026 osiąga kulminacyjny punkt w czwartek 19 listopada w turyńskiej Inalpi Arena.",
        "Lider rankingu Alexander Zverev z bilansem 2-0 ma już zapewniony awans po wtorkowym zwycięstwie 6:2, 7:6 (4) nad Benem Sheltonem. Za jego plecami Shelton i Arthur Fils mają bilans 1-1 i walczą o drugie premiowane awansem miejsce.",
        "Fils zagra wieczorem o 20:30 z niepokonanym Zverevem, natomiast Shelton o 14:00 zmierzy się z Rafaelem Jodarem, polując na szybkie zwycięstwo bez straty seta."
      ]
    },
    "zh": {
      "title": "都灵决战日：谢尔顿与菲斯周四争夺麦肯罗组最后一张半决赛门票",
      "subtitle": "世界第一兹维列夫已携两连胜锁定出线，谢尔顿与菲斯将在最后一轮小组赛展开隔空生死对决。",
      "excerpt": "继阿尔卡拉斯从伦德尔组强势突围后，ATP都灵年终总决赛麦肯罗组迎来生死战，四强最后席位今日出炉。",
      "body": [
        "2026年ATP年终总决赛的半决赛争夺在11月19日周四进入白热化阶段，都灵伊纳尔皮竞技场迎来麦肯罗组的最终决战轮次。",
        "头号种子兹维列夫在周二直落两盘以6-2、7-6 (4)力克谢尔顿后，已携2胜0负的不败战绩提前锁定四强席位。但在他身后，战绩同为1胜1负的谢尔顿与法国新星菲斯将为第二张门票全力拼杀。",
        "菲斯在周二击败霍达尔重燃希望，今晚20:30他将直面强大的兹维列夫；而谢尔顿将在14:00对阵两连败的霍达尔，若能直落两盘横扫将占据得失局率的绝对优势。"
      ]
    },
    "ja": {
      "title": "トリノ激闘：シェルトンとフィスがマッケンロー組準決勝進出を懸けて激突",
      "subtitle": "2勝のアレクサンダー・ズベレフが突破を決める中、シェルトンとフィスが木曜日に最後の4強枠を争う。",
      "excerpt": "アルカラスがレンドル組を突破したのに続き、ATPファイナルズは木曜日にマッケンロー組の最終節を迎え緊迫感が高まる。",
      "body": [
        "2026年日東ATPファイナルズの4強入りを懸けた戦いが、11月19日木曜日にイタリア・トリノのイナルピ・アレーナで決着を迎えます。",
        "世界1位のズベレフは火曜日にシェルトンを6-2、7-6 (4)で退け、2勝0敗で準決勝進出を確定させました。その背後で、1勝1敗で並ぶベン・シェルトンとアルトゥール・フィスが残る1枠を争っています。",
        "火曜日に初勝利を挙げたフィスは夜20:30にズベレフに挑み、シェルトンは14:00から未勝利のホダールと対戦。セット失失率が命運を分ける緊迫の一日となります。"
      ]
    },
    "ko": {
      "title": "토리노 대접전: 셸턴과 필스, 매켄로 조 마지막 4강 티켓 놓고 격돌",
      "subtitle": "알렉산더 즈베레프가 2승으로 4강을 확정한 가운데, 셸턴과 필스가 목요일 결전에서 마지막 자리를 다툽니다.",
      "excerpt": "알카라스가 렌들 조 1위로 준결승에 선착한 데 이어, 토리노 파이널스는 목요일 매켄로 조 최종전을 통해 4강 대진을 완성합니다.",
      "body": [
        "2026 니토 ATP 파이널스 준결승을 향한 마지막 관문이 11월 19일 목요일 이탈리아 토리노 이날피 아레나에서 열립니다.",
        "세계 랭킹 1위 즈베레프는 화요일 셸턴을 6-2, 7-6 (4)으로 제압하며 조 1위로 4강 진출을 조기 확정지었습니다. 그러나 1승 1패로 팽팽히 맞선 벤 셸턴과 아르튀르 필스는 2위 자리를 놓고 벼랑 끝 승부를 벌입니다.",
        "필스는 밤 8시 30분 최강 즈베레프를 넘어야 하며, 셸턴은 오후 2시 라파엘 호다르를 상대로 세트 득실 우위를 노리는 완승을 정조준합니다."
      ]
    },
    "ar": {
      "title": "إثارة في تورينو: شيلتون وفيس يتصارعان على بطاقة نصف النهائي الأخيرة",
      "subtitle": "بعد ضمان زفيريف التأهل بسجل مثالي، يخوض بن شيلتون وآرثر فيس مواجهات حاسمة لحجز المقعد المتبقي.",
      "excerpt": "بعد حسم ألكاراز تأهله من مجموعة ليندل، تختتم منافسات مجموعة ماكنرو في تورينو مع صراع شرس على بلوغ المربع الذهبي.",
      "body": [
        "تبلغ الإثارة ذروتها في نهائيات الجولة العالمية للرجال في تورينو يوم الخميس 19 نوفمبر، حيث تسدل الستار على مواجهات مجموعة جون ماكنرو في إينالبي أرينا.",
        "وضمن المصنف الأول عالميا ألكسندر زفيريف تأهله للمربع الذهبي بعد فوزه على شيلتون 6-2 و7-6 (4). وتشتعل المنافسة خلفه بين الأمريكي شيلتون والفرنسي الشاب آرثر فيس ولكل منهما انتصار وهزيمة.",
        "يواجه فيس مهمة شاقة أمام زفيريف في الفترة المسائية، بينما يلتقي شيلتون مع الإسباني خودار في مواجهة يسعى خلالها للفوز بمجموعتين نظيفتين لحسم بطاقة العبور."
      ]
    }
  },
  "nfl-tnf-colts-visit-texans-stroud-richardson-week11-2026": {
    "fr": {
      "title": "Thursday Night Football : Choc au sommet en AFC Sud entre Colts et Texans",
      "subtitle": "C.J. Stroud et Houston accueillent Anthony Richardson et Indianapolis dans un duel crucial pour les playoffs.",
      "excerpt": "La suprématie de l'AFC Sud se joue ce jeudi soir au NRG Stadium où les Texans de Houston défient les Colts d'Indianapolis pour lancer la semaine 11.",
      "body": [
        "La semaine 11 de la NFL débute en prime time jeudi soir, 19 novembre, avec une affiche brûlante de division entre les Houston Texans et les Indianapolis Colts au NRG Stadium.",
        "Houston aborde ce duel en leader grâce à la précision de son quarterback C.J. Stroud et une ligne défensive emmenée par Will Anderson Jr, qui domine l'AFC avec 10 sacks. En face, les Colts comptent sur la puissance au sol d'Anthony Richardson et le talent de Jonathan Taylor pour imposer leur rythme.",
        "Dans une conférence AFC extrêmement dense, ce face-à-face direct aura une valeur inestimable pour les critères de départage en vue de la qualification pour les séries éliminatoires."
      ]
    },
    "es": {
      "title": "Thursday Night Football: Colts y Texans protagonizan un duelo clave del AFC Sur",
      "subtitle": "C.J. Stroud lidera a Houston frente al ataque terrestre de Anthony Richardson e Indianapolis en la Semana 11.",
      "excerpt": "El liderato divisional del AFC Sur está en juego en el NRG Stadium cuando los Texans reciban a los Colts en un electrizante choque nocturno.",
      "body": [
        "La Semana 11 de la NFL arranca este jueves 19 de noviembre en horario estelar con el esperado enfrentamiento divisional entre los Houston Texans y los Indianapolis Colts en el NRG Stadium.",
        "Los Texans de C.J. Stroud buscan consolidar el primer puesto de la división apoyados en una feroz presión liderada por Will Anderson Jr. Por su parte, Indianápolis presenta una peligrosa ofensiva terrestre liderada por Jonathan Taylor y la potencia de Anthony Richardson.",
        "Con ambos equipos en plena pugna por boletos de comodín en la AFC, el vencedor dará un paso de gigante al asegurarse el criterio de desempate directo."
      ]
    },
    "de": {
      "title": "Thursday Night Football: Colts fordern Texans im brisanten AFC South Duell heraus",
      "subtitle": "C.J. Stroud empfängt Anthony Richardson und die Colts in einem richtungsweisenden Matchup der Woche 11.",
      "excerpt": "Im NRG Stadium von Houston steht am Donnerstagabend die Vormachtstellung in der AFC South auf dem Spiel, wenn die Texans auf die Colts treffen.",
      "body": [
        "Woche 11 der NFL-Saison startet am Donnerstagabend, 19. November, mit einem hochkarätigen Divisionsduell zwischen den Houston Texans und den Indianapolis Colts im NRG Stadium.",
        "Houston setzt auf die Passpräzision von Quarterback C.J. Stroud und eine dominante Defensive um Pass-Rusher Will Anderson Jr., der die AFC mit 10 Sacks anführt. Die Colts halten mit der Athletik von Anthony Richardson und Star-Running-Back Jonathan Taylor dagegen.",
        "Im engen Playoff-Rennen der AFC geht es für beide Franchises nicht nur um den Sieg, sondern auch um entscheidende direkte Tiebreaker für die Postseason."
      ]
    },
    "it": {
      "title": "Thursday Night Football: Colts contro Texans per il primato nell'AFC South",
      "subtitle": "C.J. Stroud sfida Anthony Richardson all'NRG Stadium in un match della Week 11 fondamentale per i playoff.",
      "excerpt": "La corsa per la corona dell'AFC South si infiamma nel Thursday Night Football tra gli Houston Texans e gli Indianapolis Colts.",
      "body": [
        "La Week 11 della NFL si apre nella notte di giovedì 19 novembre con l'intrigante derby divisionale tra Houston Texans e Indianapolis Colts all'NRG Stadium.",
        "I padroni di casa guidati da C.J. Stroud vogliono consolidare la vetta della division con l'apporto difensivo di Will Anderson Jr, mentre Indianapolis punta sulle corse esplosive di Richardson e Jonathan Taylor.",
        "Con la griglia playoff dell'AFC ancora apertissima, il risultato di questa notte peserà enormemente nei criteri di spareggio per la postseason."
      ]
    },
    "pl": {
      "title": "Thursday Night Football: Colts i Texans w bitwie o dominację w AFC South",
      "subtitle": "C.J. Stroud podejmuje Anthony'ego Richardsona w kluczowym meczu 11. tygodnia z myślą o play-offach.",
      "excerpt": "W Houston na NRG Stadium stawką czwartkowego hitu NFL jest fotel lidera AFC South oraz bezcenny tie-breaker przed końcówką sezonu.",
      "body": [
        "Jedenasty tydzień sezonu NFL rozpoczyna się w czwartek 19 listopada arcyważnym starciem w Houston, gdzie Texans podejmują Indianapolis Colts.",
        "Prowadzona przez C.J. Strouda ofensywa gospodarzy zmierzy się z nieprzewidywalną formacją Colts opartą na biegach Anthony'ego Richardsona i Jonathana Taylora. W obronie Houston postrachem rywali pozostaje Will Anderson Jr.",
        "Wygrana w tym meczu nie tylko przybliża triumfatora do korony dywizji, ale zapewnia także kluczowy bezpośredni bilans w konferencji AFC."
      ]
    },
    "zh": {
      "title": "周四夜赛激战：小马客战得州人，斯特劳德对决理查森争夺美南头名",
      "subtitle": "斯特劳德率领休斯敦得州人在NRG体育场迎战印第安纳波利斯小马，季后赛外卡排位战一触即发。",
      "excerpt": "NFL第11周周四夜赛在休斯敦打响，得州人与小马展开美联南区榜首关键战，双方年轻四分卫正面对决。",
      "body": [
        "11月19日周四晚间，NFL第11周赛事在休斯敦NRG体育场揭幕，得州人主场迎战美联南区死敌印第安纳波利斯小马队。",
        "得州人四分卫斯特劳德本赛季发挥稳健，与防守端砍下10次擒杀的安德森组成强力攻防核心。小马队则凭借安东尼-理查森的超强身体素质和泰勒的强硬地面冲击给予强力回应。",
        "在竞争白热化的美联季后赛格局中，这场周四夜赛的直接交锋胜负将对两队的相互战绩胜负关系产生决定性影响。"
      ]
    },
    "ja": {
      "title": "サーズデーナイト決戦：コルツ対テキサンズ、AFC南部首位を懸けた激突",
      "subtitle": "C.J.ストラウド擁するテキサンズがリチャードソン率いるコルツをホームNRGスタジアムで迎え撃つ。",
      "excerpt": "NFL第11週の幕開けはテキサンズとコルツの同地区対決。プレイオフ進出に向けてタイブレークが懸かる重要戦。",
      "body": [
        "NFL第11週が11月19日木曜日の夜、ヒューストンのNRGスタジアムで行われるコルツ対テキサンズのAFC南部地区首位決戦で開幕します。",
        "テキサンズはQBストラウドの正確なパスと、AFCトップの10サックを誇るDEアンダーソンJr.を中心とした強固な守備で地区連覇を狙います。対するコルツはQBアンソニー・リチャードソンとRBテイラーの強力ラン攻撃で敵地攻略を目指します。",
        "混戦が続くAFCのプレイオフ争いにおいて、この直接対決の結果はポストシーズン進出の命運を左右する極めて重要な一戦となります。"
      ]
    },
    "ko": {
      "title": "서스데이 나이트 풋볼: 콜츠-텍산스, AFC 남부 선두 격돌",
      "subtitle": "C.J. 스트라우드의 텍산스와 앤서니 리차드슨의 콜츠가 11주차 개막전에서 플레이오프 유리한 고지를 놓고 격돌합니다.",
      "excerpt": "휴스턴 NRG 스타디움에서 펼쳐지는 AFC 남부 라이벌전. 11주차 목요일 밤 포스트시즌 타이틀 향방이 갈립니다.",
      "body": [
        "NFL 11주차 일정이 11월 19일 목요일 밤 휴스턴 NRG 스타디움에서 열리는 인디애나폴리스 콜츠와 휴스턴 텍산스의 AFC 남부 맞대결로 시작됩니다.",
        "텍산스는 쿼터백 C.J. 스트라우드의 안정적인 패싱과 10개의 색을 기록 중인 윌 앤더슨 주니어의 수비를 앞세워 홈 승리를 노립니다. 콜츠는 앤서니 리차드슨의 러싱 위력과 조나단 테일러의 지상전을 무기로 맞불을 놓습니다.",
        "치열한 와일드카드 레이스 속에서 맞대결 승자가 쥐게 될 상대 전적 우위는 포스트시즌 진출의 결정적 열쇠가 될 전망입니다."
      ]
    },
    "ar": {
      "title": "ليلة الخميس في دوري كرة القدم الأمريكية: مواجهة مشتعلة بين كولتس وتكسانز",
      "subtitle": "سي جيه ستراود يقود تكسانز أمام ريتشاردسون وكولتس في صراع الصدارة للتأهل إلى الأدوار الإقصائية.",
      "excerpt": "قمة مرتقبة تجمع هيوستن تكسانز وإنديانابوليس كولتس على ملعب إن آر جي ستاديوم في افتتاح الجولة 11.",
      "body": [
        "تنطلق منافسات الجولة 11 من دوري كرة القدم الأمريكية مساء الخميس 19 نوفمبر بمواجهة نارية تجمع هيوستن تكسانز بغريمه إنديانابوليس كولتس على ملعب إن آر جي ستاديوم.",
        "يسعى هيوستن بقيادة نجمه الصاعد سي جيه ستراود ودفاعه القوي إلى فرض سيطرته، بينما يعتمد كولتس على القدرات البدنية العالية لرباع الهجوم أنتوني ريتشاردسون والعداء جوناثان تايلور.",
        "وتحمل هذه المواجهة أهمية قصوى لحسم أفضلية المواجهات المباشرة في سباق بطاقات التأهل للأدوار الإقصائية في القسم الأمريكي."
      ]
    }
  },
  "f1-las-vegas-gp-thursday-practice-opens-strip-showdown-2026": {
    "fr": {
      "title": "Le Strip s'embrase : La Formule 1 ouvre le GP de Las Vegas sous les néons",
      "subtitle": "Les moteurs vrombissent sur le boulevard de Las Vegas pour les essais libres du jeudi avec une lutte féroce pour le titre de vice-champion.",
      "excerpt": "Le Strip de Las Vegas s'illumine pour la manche 21. Kimi Antonelli déjà titré, cinq pilotes séparés par 33 points chassent la place de dauphin.",
      "body": [
        "Le tracé urbain le plus spectaculaire du calendrier s'éveille jeudi soir, 19 novembre, alors que la Formule 1 lance ses premiers essais libres sur le Strip de Las Vegas pour la 21e manche de la saison.",
        "Alors que le prodige italien Kimi Antonelli et Mercedes sont déjà couronnés champions du monde, la bataille pour la deuxième place au classement des pilotes bat son plein. Max Verstappen (279 points) ne compte que 33 longueurs d'avance sur Lando Norris (246), tandis que Russell (262), Hamilton (261) et Leclerc (249) restent en embuscade.",
        "Sur cette piste de 6,201 km où les monoplaces flirtent avec les 350 km/h, le froid nocturne du désert sous les 12 degrés posera un immense casse-tête pour la mise en température des pneumatiques dès cette première séance."
      ]
    },
    "es": {
      "title": "Ruge el Strip: La Fórmula 1 abre el GP de Las Vegas con las prácticas nocturnas",
      "subtitle": "Los monoplazas salen a pista bajo los neones de Las Vegas con cinco pilotos en 33 puntos peleando por el subcampeonato.",
      "excerpt": "Las Vegas Boulevard acoge las prácticas libres de la Ronda 21. Con Antonelli campeón, Verstappen y Norris encabezan la lucha por el segundo puesto.",
      "body": [
        "El circuito urbano más deslumbrante del automovilismo se llena de acción este jueves 19 de noviembre con la disputa de los primeros entrenamientos libres del Gran Premio de Las Vegas.",
        "Con Kimi Antonelli y Mercedes ya consagrados como monarcas de 2026, el aliciente se centra en el subcampeonato de pilotos, donde solo 33 puntos distancian a Verstappen (279) de Norris (246), pasando por Russell, Hamilton y Leclerc.",
        "Los 6,201 kilómetros del trazado exigirán máxima velocidad punta en la larga recta del Strip, mientras las bajas temperaturas nocturnas pondrán a prueba el agarre y la degradación de los neumáticos."
      ]
    },
    "de": {
      "title": "Der Strip erwacht zum Leben: Formel 1 startet Las Vegas GP mit Donnerstagstraining",
      "subtitle": "Die Motoren heulen auf dem Las Vegas Boulevard auf, während fünf Piloten um den prestigeträchtigen Vizeweltmeistertitel kämpfen.",
      "excerpt": "Flutlicht und Glamour: In Las Vegas beginnt der 21. WM-Lauf mit den ersten Trainingssessions, in denen 33 Punkte fünf Fahrer trennen.",
      "body": [
        "Die berühmteste Vergnügungsmeile der Welt verwandelt sich am Donnerstagabend, 19. November, in eine Hochgeschwindigkeitsarena für die ersten Trainings des Las Vegas Grand Prix.",
        "Zwar hat Mercedes-Youngster Kimi Antonelli den Fahrertitel bereits sicher, doch der Kampf um Platz zwei ist heißer denn je. Max Verstappen (279 Punkte), George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) und Lando Norris (246) liegen innerhalb von nur 33 Zählern.",
        "Bei kühlen Wüstentemperaturen unter 12 Grad Celsius wird das Aufwärmen der Reifen auf den langen Geraden die größte Herausforderung des Wochenendes darstellen."
      ]
    },
    "it": {
      "title": "La Strip si accende: La Formula 1 apre il weekend di Las Vegas con le prove libere",
      "subtitle": "I motori ruggiscono nella notte del Nevada: cinque piloti racchiusi in 33 punti per la piazza d'onore mondiale.",
      "excerpt": "Le luci di Las Vegas illuminano il Round 21. Antonelli e Mercedes già campioni, ma la sfida per il secondo posto promette scintille.",
      "body": [
        "Il circuito cittadino più sfarzoso del mondiale prende vita giovedì sera, 19 novembre, con le prime due sessioni di prove libere del Gran Premio di Las Vegas.",
        "Mentre il fenomeno Kimi Antonelli si gode il titolo iridato, la lotta per il secondo posto vede cinque piloti in lizza separati da 33 punti: Verstappen guida l'inseguimento davanti a Russell, Hamilton, Leclerc e Norris.",
        "I 6,201 km del tracciato, con il lunghissimo rettilineo da oltre 350 km/h, metteranno a dura prova la gestione termica delle gomme nel freddo pungente del deserto."
      ]
    },
    "pl": {
      "title": "Ryk silników na Strip: Formuła 1 rozpoczyna weekend w Las Vegas czwartkowym treningiem",
      "subtitle": "Bolidy wyjeżdżają na Las Vegas Boulevard, a pięciu kierowców w granicach 33 punktów toczy bój o wicemistrzostwo.",
      "excerpt": "Światła kasyn rozbłyskają dla 21. rundy F1. Kimi Antonelli jest już mistrzem, lecz walka o drugie miejsce na świecie nabiera tempa.",
      "body": [
        "Najbardziej spektakularny tor uliczny w kalendarzu ożywa w czwartek wieczorem 19 listopada podczas pierwszych treningów przed Grand Prix Las Vegas.",
        "Chociaż Kimi Antonelli i Mercedes świętują już mistrzowskie tytuły, rywalizacja o wicemistrzostwo świata wciąż elektryzuje kibiców. Maxa Verstappena (279 pkt) i Lando Norrisa (246 pkt) dzieli zaledwie 33 punkty, a w grze są też Russell, Hamilton i Leclerc.",
        "Szybka prosta o długości 1,9 km na Las Vegas Boulevard w połączeniu z temperaturami spadającymi poniżej 12 stopni Celsjusza będzie arcytrudnym testem dla dogrzewania opon."
      ]
    },
    "zh": {
      "title": "赌城大道轰鸣启幕：F1拉斯维加斯大奖赛周四夜间练习赛开跑",
      "subtitle": "赛车呼啸驰骋于拉斯维加斯大道霓虹灯下，五位车手分差仅33分展开年度亚军终极较量。",
      "excerpt": "拉斯维加斯大奖赛周四正式打响，双冠王安东内利与梅赛德斯身后，维斯塔潘携手诺里斯展开激烈排位争夺。",
      "body": [
        "11月19日周四晚间，全球最具观赏性的城市街道赛道迎来引擎轰鸣，F1第21站拉斯维加斯大奖赛一练与二练正式在赌城大道拉开战幕。",
        "虽然梅赛德斯新星安东内利已提前加冕车手世界冠军，但年度亚军争夺依然悬念丛生。第二名维斯塔潘（279分）与第六名诺里斯（246分）之间仅相差33分，拉塞尔、汉密尔顿与勒克莱尔同样具备极强竞争力。",
        "全长6.201公里的赛道拥有长达1.9公里的全油门直道，夜间低于12度的低温将对车队轮胎升温和下压力设定带来严峻挑战。"
      ]
    },
    "ja": {
      "title": "ストリップに轟音響く：F1ラスベガスGPが木曜夜間フリー走行で開幕",
      "subtitle": "ネオン輝くラスベガス大通りでマシンが疾走。ランキング2位を懸けて5人のドライバーが激突。",
      "excerpt": "ラスベガス第21戦の走行が木曜夜にスタート。王者アントネッリの背後で33点差にひしめく白熱のシリーズ2位争い。",
      "body": [
        "モータースポーツ屈指の華麗なストリートサーキットが11月19日木曜日の夜、F1第21戦ラスベガスGPのフリー走行1回目で幕を開けました。",
        "メルセデスのアントネッリがすでにタイトルを確定させたものの、2位フェルスタッペン（279点）からノリス（246点）までわずか33点差の熾烈な準優勝争いが展開されています。",
        "全長6.201kmのコースでは、最高速350km/hに達するストリップのストレートと12度を下回る砂漠の夜間冷え込みによるタイヤ管理が勝負を左右します。"
      ]
    },
    "ko": {
      "title": "라스베이거스 스트립 질주 시작: F1 21라운드 목요일 야간 연습 주행 개막",
      "subtitle": "화려한 네온사인 아래 굉음이 울려 퍼집니다. 33점 차 5명의 드라이버가 준우승 타이틀을 놓고 격돌합니다.",
      "excerpt": "라스베이거스 그랑프리 개막. 챔피언 키미 안토넬리의 뒤를 이어 베르스타펜, 러셀, 해밀턴, 르클레르, 노리스가 2위 쟁탈전을 펼칩니다.",
      "body": [
        "세계에서 가장 화려한 도심 서킷인 라스베이거스 스트립이 11월 19일 목요일 밤 F1 21라운드 공식 연습 주행과 함께 깨어났습니다.",
        "메르세데스의 키미 안토넬리가 월드 챔피언에 올랐지만, 2위 막스 베르스타펜(279점)부터 6위 랜도 노리스(246점)까지 33점 차에 불과한 드라이버 준우승 경쟁이 절정에 달하고 있습니다.",
        "시속 350km를 넘나드는 1.9km 직선 구간과 12도 이하로 떨어지는 서늘한 사막 밤 기온 속 타이어 관리가 이번 주말 최대 변수로 떠올랐습니다."
      ]
    },
    "ar": {
      "title": "أضواء حلبة ستريب تشتعل: انطلاق التجارب الحرة لجائزة لاس فيغاس الكبرى",
      "subtitle": "هدير المحركات يعلو في لاس فيغاس مساء الخميس وسط منافسة محتدمة بين خمسة سائقين على وصافة العالم.",
      "excerpt": "افتتاح منافسات الجولة 21 في لاس فيغاس مع انطلاق التجارب الحرة الليلية، وصراع شرس على المركز الثاني بوجود فارق 33 نقطة فقط.",
      "body": [
        "تحت أضواء نيفادا الساحرة، انطلقت مساء الخميس 19 نوفمبر التجارب الحرة الأولى والثانية لسباق جائزة لاس فيغاس الكبرى للفورمولا 1.",
        "ومع حسم كيمي أنتونيللي لقب العالم، يتركز الاهتمام على وصافة البطولة؛ حيث لا تفصل سوى 33 نقطة بين ماكس فيرستابن (279) ولاندو نوريس (246) وبينهما راسل وهاميلتون ولوكلير.",
        "ويشكل المسار البالغ 6.201 كم والبرودة الصحراوية التي تنخفض دون 12 درجة مئوية تحديا معقدا للمهندسين في إحماء الإطارات وضبط السرعات القصوى."
      ]
    }
  },
  "golf-rsm-classic-round1-live-sea-island-thompson-bubble-cards-2026": {
    "fr": {
      "title": "Tension à Sea Island : Le 1er tour du RSM Classic lance la course aux cartes PGA Tour 2027",
      "subtitle": "Davis Thompson s'illustre à -5 tandis que les joueurs de la bulle du top 125 affrontent le vent côtier en Géorgie.",
      "excerpt": "Le premier tour du RSM Classic est officiellement lancé au Sea Island Golf Club, où la survie sportive pour la saison 2027 se joue à chaque coup.",
      "body": [
        "Le dernier tournoi officiel de la saison 2026 du PGA Tour a démarré jeudi matin, 19 novembre, avec le premier tour du RSM Classic sur les parcours Seaside et Plantation du Sea Island Golf Club.",
        "Pour les compétiteurs situés autour de la fatidique 125e place de la FedExCup, chaque coup sur les links de Géorgie peut faire basculer une carrière. Rester dans le top 125 garantit l'exemption complète en 2027, tandis qu'une sortie de route condamne aux tournois qualificatifs.",
        "L'enfant du pays Davis Thompson a enflammé le public avec un excellent départ à 5 sous le par, imité par le double vainqueur Mackenzie Hughes à -4, alors que des joueurs sous pression comme Joel Dahmen jouent leur avenir sur chaque putt."
      ]
    },
    "es": {
      "title": "Comienza la batalla en Sea Island: La Ronda 1 de The RSM Classic reparte las tarjetas de 2027",
      "subtitle": "Davis Thompson marca el paso con 5 bajo par en el dramático cierre del FedExCup Fall en Georgia.",
      "excerpt": "Arrancó la primera ronda de The RSM Classic en Sea Island, donde los jugadores al borde del corte del top 125 pelean por sus derechos para el PGA Tour.",
      "body": [
        "El epílogo de la temporada 2026 del PGA Tour se puso en marcha este jueves 19 de noviembre en los campos de Sea Island Golf Club con la primera ronda de The RSM Classic.",
        "La tensión es absoluta para quienes se ubican en la burbuja del puesto 125 de la FedExCup, el límite estricto para asegurar la membresía completa para 2027. Davis Thompson asumió el liderato provisional con 5 bajo par gracias a seis birdies en sus primeros 14 hoyos.",
        "El bicampeón Mackenzie Hughes y el reciente ganador Austin Smotherman también arrancaron con solidez a cuatro bajo par, mientras favoritos del público como Joel Dahmen sufren cada impacto con el futuro en juego."
      ]
    },
    "de": {
      "title": "Nervenkrimi in Sea Island: Runde 1 der RSM Classic entscheidet über PGA Tour Karten für 2027",
      "subtitle": "Davis Thompson setzt mit 5 unter Par das frühe Ausrufezeichen im Kampf um die Top-125-Exemptionen.",
      "excerpt": "Runde 1 der RSM Classic läuft in Georgia: Für viele Profis geht es auf den Links von Sea Island um die sportliche Existenz auf der PGA Tour.",
      "body": [
        "Die offizielle PGA Tour Saison 2026 steuert seit Donnerstagmorgen, 19. November, auf ihren nervenaufreibenden Höhepunkt zu: Die erste Runde der RSM Classic im Sea Island Golf Club ist in vollem Gange.",
        "Für die Spieler rund um Platz 125 im FedExCup-Ranking zählt jeder einzelne Schlag. Ein Verbleib unter den besten 125 sichert die volle Tourkarte für 2027, während ein Abrutschen den Gang in die Qualifying School bedeutet.",
        "Lokalmatador Davis Thompson übernahm mit einer starken 5-unter-Par-Runde früh die Führung, dicht gefolgt vom zweifachen Champion Mackenzie Hughes (-4), während Bubble-Spieler wie Joel Dahmen um jeden Zentimeter kämpfen."
      ]
    },
    "it": {
      "title": "Dramma a Sea Island: Al via il 1° giro del RSM Classic per le carte PGA Tour 2027",
      "subtitle": "Davis Thompson guida a -5 mentre i giocatori sulla bolla della top 125 sfidano il vento in Georgia.",
      "excerpt": "Il primo giro del RSM Classic è in corso a Sea Island: in palio le preziose esenzioni per la stagione 2027 del circuito americano.",
      "body": [
        "L'ultimo torneo ufficiale del PGA Tour 2026 è scattato giovedì mattina, 19 novembre, con il primo giro del The RSM Classic sui campi di Sea Island Golf Club in Georgia.",
        "Per i golfisti a ridosso della 125esima posizione della FedExCup la posta in palio è altissima: mantenere la carta piena per il 2027 ed evitare i tornei di qualificazione. Il beniamino di casa Davis Thompson ha aperto con un solido 5 sotto il par.",
        "Tra i protagonisti di giornata anche il due volte campione Mackenzie Hughes (-4), mentre golfisti come Joel Dahmen giocano ogni colpo sotto un'enorme pressione emotiva."
      ]
    },
    "pl": {
      "title": "Dramat w Sea Island: 1. runda RSM Classic decyduje o kartach PGA Tour na 2027 rok",
      "subtitle": "Davis Thompson prowadzi z wynikiem 5 poniżej par, gdy zawodnicy z okolic 125. miejsca walczą o przyszłość.",
      "excerpt": "Pierwsza runda turnieju RSM Classic w Sea Island Golf Club trwa na żywo. Gra toczy się o pełne karty członkowskie na sezon 2027.",
      "body": [
        "Finałowy turniej sezonu PGA Tour 2026 wystartował w czwartek 19 listopada w Sea Island Golf Club w stanie Georgia.",
        "Dla graczy z okolic 125. pozycji w rankingu FedExCup każdy uderzony dołek decyduje o utrzymaniu w elicie na rok 2027. Davis Thompson zachwycił kibiców świetnym początkiem na poziomie 5 poniżej par.",
        "W czołówce z wynikiem -4 plasuje się dwukrotny zwycięzca Mackenzie Hughes, podczas gdy walczący o przetrwanie Joel Dahmen mierzy się z olbrzymią presją każdego uderzenia."
      ]
    },
    "zh": {
      "title": "海岛保卡决战打响：RSM精英赛首轮开杆，前125席位争夺进入白热化",
      "subtitle": "本土好手戴维斯-汤普森以-5杆暂居前列，保卡边缘球员在佐治亚海岸展开生涯关键战役。",
      "excerpt": "2026赛季美巡赛收官战RSM精英赛首轮在海岛高尔夫俱乐部正式打响，2027赛季全卡资格在此一举。",
      "body": [
        "美巡赛2026赛季最后一站官方赛事于11月19日周四上午在佐治亚州海岛高尔夫俱乐部全面开杆，RSM精英赛首轮正式打响。",
        "对于排在联邦快递杯积分榜125位边缘的球员而言，海滨球场的每一个推杆都决定着下赛季的饭碗。本土名将汤普森开局斩获6只小鸟交出-5杆领跑，两届冠军休斯以-4杆紧随其后。",
        "与此同时，达门等保卡边缘热门球手在巨大心理压力下奋力保帕，第51至60位的标志赛事名额争夺同样扣人心弦。"
      ]
    },
    "ja": {
      "title": "シーアイランド激闘開始：RSMクラシック第1Rで来季PGAシード権争奪戦が開幕",
      "subtitle": "地元デービス・トンプソンが5アンダーで好発進。125位の当落線上の選手たちが命運を懸ける。",
      "excerpt": "PGAツアー今季最終戦RSMクラシックがシーアイランドで開幕。来季フルシード権トップ125を懸けた真剣勝負。",
      "body": [
        "2026年PGAツアーの掉尾を飾るRSMクラシック第1ラウンドが、11月19日木曜日の朝にジョージア州シーアイランドGCで開幕しました。",
        "フェデックスカップランキング125位前後の選手にとって、この4日間のスコアが来季の出場資格を直結します。地元出身のデービス・トンプソンが5アンダーと好発進を切り、2度優勝のヒューズも4アンダーと順調な滑り出しを見せました。",
        "シード権確保が危ぶまれるジョエル・ダーメンらボーダーラインの選手たちは、1打のミスも許されない極限のプレッシャーの中でプレーを続けています。"
      ]
    },
    "ko": {
      "title": "시 아일랜드 결전 개막: RSM 클래식 1라운드서 2027 PGA 투어 시드권 혈투",
      "subtitle": "데이비스 톰슨이 5언더파로 선두권을 달리는 가운데, 125위 버블 선수들이 조지아 해안에서 생존 경쟁을 펼칩니다.",
      "excerpt": "2026 PGA 투어 최종전 The RSM 클래식 1라운드가 시작되었습니다. 2027시즌 전 경기 출전권이 걸린 마지막 무대입니다.",
      "body": [
        "2026 PGA 투어 정규시즌 최종전인 The RSM 클래식 1라운드가 11월 19일 목요일 오전 조지아주 시 아일랜드 골프클럽에서 공식 티오프했습니다.",
        "페덱스컵 랭킹 125위 진입을 노리는 선수들에게는 매 홀이 절체절명의 승부처입니다. 지역 출신 데이비스 톰슨이 5언더파를 치며 선두로 치고 나갔고, 매켄지 휴즈도 4언더파로 상위권에 자리했습니다.",
        "시드 유지가 절실한 조엘 다멘을 비롯한 버블권 선수들의 살얼음판 승부가 펼쳐지며 갤러리들의 손에 땀을 쥐게 하고 있습니다."
      ]
    },
    "ar": {
      "title": "انطلاق معركة سي آيلاند: الجولة الأولى لبطولة آر إس إم كلاسيك تحسم بطاقات 2027",
      "subtitle": "ديفيس طومسون يتألق بـ 5 ضربات تحت المعدل بينما يقاتل لاعبو حافة الـ 125 لإنقاذ موسمهم في جورجيا.",
      "excerpt": "بدأت منافسات الجولة الأولى لبطولة آر إس إم كلاسيك في نادي سي آيلاند للجولف حيث يتحدد مصير بطاقات جولة البي جي إيه للعام المقبل.",
      "body": [
        "انطلقت الجولة الأولى من بطولة آر إس إم كلاسيك صباح الخميس 19 نوفمبر على ملاعب سي آيلاند للجولف في ولاية جورجيا، مسدلة الستار على موسم 2026 للجولة الأمريكية.",
        "وتحمل البطولة أهمية مصيرية للاعبين الواقعين حول المركز 125 في ترتيب فيديكس كب لضمان البقاء في الجولة الممتازة وتجنب الهبوط. واستهل المحلي ديفيس طومسون المنافسات بتسجيل 5 ضربات تحت المعدل.",
        "ويلاحقه البطل السابق ماكنزي هيوز بـ 4 ضربات تحت المعدل، وسط صراع درامي للاعبين المهددين بفقدان بطاقاتهم مثل جويل داهمن."
      ]
    }
  },
  "nba-giannis-masterclass-downs-bucks-heat-sixth-straight-2026": {
    "fr": {
      "title": "Récital de Giannis : 27 points face aux Bucks pour porter le Heat à 6 victoires de rang (137-130)",
      "subtitle": "Giannis Antetokounmpo frôle le triple-double contre son ancienne franchise pour offrir à Miami un succès de prestige.",
      "excerpt": "Miami s'impose 137-130 face à Milwaukee grâce à un Giannis magistral, tandis que Denver renverse Boston après avoir été mené de 17 points.",
      "body": [
        "Pour ses grandes retrouvailles avec les Milwaukee Bucks mercredi soir, 18 novembre, Giannis Antetokounmpo a livré une prestation de patron en guidant le Miami Heat vers une victoire étincelante 137-130 au Kaseya Center.",
        "Le double MVP a compilé 27 points, 14 rebonds et 9 passes décisives, idéalement épaulé par Bam Adebayo (26 points, 10 rebonds) et Tyler Herro (23 points) pour permettre à Miami d'enchaîner une sixième victoire d'affilée et d'afficher un bilan de 9-3.",
        "À l'Ouest, les Denver Nuggets ont effacé un débours de 17 points pour dominer les Boston Celtics 105-101 grâce à un Nikola Jokic omniprésent (24 points, 9 passes, 8 rebonds), infligeant aux Celtics un deuxième revers de rang."
      ]
    },
    "es": {
      "title": "Recital de Giannis: 27 puntos ante los Bucks para guiar a los Heat a su sexto triunfo seguido (137-130)",
      "subtitle": "Antetokounmpo firma 27 puntos, 14 rebotes y 9 asistencias en su reencuentro con Milwaukee y Miami no afloja.",
      "excerpt": "Miami Heat derrota 137-130 a los Bucks con una brillante actuación de Giannis, mientras Denver remonta 17 puntos a Boston.",
      "body": [
        "Giannis Antetokounmpo vivió una noche inolvidable este miércoles 18 de noviembre al liderar a Miami Heat en el triunfo 137-130 sobre su exequipo, los Milwaukee Bucks, en el Kaseya Center.",
        "El astro griego rozó el triple-doble con 27 puntos, 14 rebotes y 9 asistencias, secundado por los 26 puntos de Bam Adebayo. Miami suma ya seis victorias seguidas y escala a la segunda posición del Este con marca de 9-3.",
        "En otro choque destacado, los Denver Nuggets vinieron de atrás tras perder por 17 puntos para vencer 105-101 a los Boston Celtics gracias a 24 puntos de Nikola Jokic, sumiendo a los de verde en su segunda caída consecutiva."
      ]
    },
    "de": {
      "title": "Giannis Gala: 27 Punkte gegen Ex-Klub Bucks führen Heat zum sechsten Sieg in Folge (137:130)",
      "subtitle": "Giannis Antetokounmpo glänzt mit 27 Punkten, 14 Rebounds und 9 Assists beim emotionalen Wiedersehen in Miami.",
      "excerpt": "Die Miami Heat bezwingen die Milwaukee Bucks in einem Offensivspektakel mit 137:130. Denver schockt die Boston Celtics nach 17-Punkte-Rückstand.",
      "body": [
        "Giannis Antetokounmpo hat am Mittwochabend, 18. November, ein emotionales Ausrufezeichen gesetzt und die Miami Heat zu einem spektakulären 137:130-Heimsieg über seinen Ex-Klub Milwaukee Bucks geführt.",
        "Der Superstar verpasste mit 27 Punkten, 14 Rebounds und 9 Assists nur knapp ein Triple-Double. Zusammen mit Bam Adebayo (26 Punkte) sicherte er Miami den sechsten Erfolg in Serie (Bilanz 9-3).",
        "Unterdessen drehten die Denver Nuggets angeführt von Nikola Jokic (24 Punkte, 9 Assists, 8 Rebounds) einen 17-Punkte-Rückstand und fügten den Boston Celtics mit 105:101 die zweite Niederlage hintereinander zu."
      ]
    },
    "it": {
      "title": "Capolavoro di Giannis: 27 punti contro i Bucks per la sesta vittoria di fila dei Heat (137-130)",
      "subtitle": "Antetokounmpo sfiora la tripla doppia nel primo incrocio con Milwaukee e trascina Miami sul 9-3.",
      "excerpt": "Spettacolo a Miami dove i Heat battono i Bucks 137-130 con uno scatenato Giannis. Denver rimonta 17 punti e batte Boston.",
      "body": [
        "Prima sfida da ex indimenticabile per Giannis Antetokounmpo, che mercoledì 18 novembre ha condotto i Miami Heat al successo per 137-130 sui Milwaukee Bucks al Kaseya Center.",
        "Il fuoriclasse ha messo a referto 27 punti, 14 rimbalzi e 9 assist, ben coadiuvato dai 26 punti di Bam Adebayo. Per Miami si tratta del sesto successo consecutivo, confermandosi forza trainante a Est.",
        "A Denver, i Nuggets hanno firmato una clamorosa rimonta da -17 superando i Boston Celtics 105-101 con 24 punti e 9 assist di Nikola Jokic, costringendo i campioni al secondo ko di fila."
      ]
    },
    "pl": {
      "title": "Popis Giannisa: 27 punktów przeciwko Bucks i szóste z rzędu zwycięstwo Heat (137:130)",
      "subtitle": "Giannis Antetokounmpo notuje 27 punktów, 14 zbiórek i 9 asyst w pierwszym meczu przeciwko swojemu byłemu klubowi.",
      "excerpt": "Miami Heat ogrywają Milwaukee Bucks 137:130 po znakomitym występie Giannisa, a Denver Nuggets odrabiają 17 punktów straty z Celtics.",
      "body": [
        "Giannis Antetokounmpo w wielkim stylu powitał swój były zespół w Kaseya Center, prowadząc w środę 18 listopada Miami Heat do zwycięstwa 137:130 nad Milwaukee Bucks.",
        "Grecki skrzydłowy otarł się o triple-double, notując 27 punktów, 14 zbiórek oraz 9 asyst. Bam Adebayo dołożył 26 punktów, co pozwoliło ekipie z Florydy przedłużyć serię zwycięstw do sześciu meczów (bilans 9-3).",
        "W Denver gospodarze dokonali niezwykłego wyczynu, odrabiając 17 punktów straty i pokonując Boston Celtics 105:101. Liderem Nuggets był Nikola Jokic z 24 punktami, 9 asystami i 8 zbiórkami."
      ]
    },
    "zh": {
      "title": "字母哥战旧主狂砍准三双：热火137-130力克雄鹿豪取六连胜",
      "subtitle": "阿德托昆博交出27分14篮板9助攻豪华数据击溃老东家，迈阿密热火战绩升至9胜3负。",
      "excerpt": "热火与雄鹿上演对攻大战，字母哥统治内线率队137-130告捷；掘金落后17分上演惊天翻盘逆转凯尔特人。",
      "body": [
        "11月18日周三晚间，迈阿密卡塞亚中心迎来充满情怀的大战，字母哥首次面对旧主雄鹿毫不手软，砍下27分14篮板9助攻准三双，带领热火137-130力克对手。",
        "阿德巴约同砍26分10篮板，希罗贡献23分，热火全场命中率高达54.3%，在第四节顶住了利拉德与库兹马的反扑，收获六连胜的同时稳居东部前两名。",
        "在丹佛高原，约基奇贡献24分9助攻8篮板，率领掘金在落后17分的绝境下以105-101逆转波士顿凯尔特人，送给东部劲旅两连败。"
      ]
    },
    "ja": {
      "title": "ヤニスが古巣相手に27得点の大暴れ：ヒートがバックスを137-130で下し6連勝",
      "subtitle": "アデトクンボが27得点14リバウンド9アシストの準トリプルダブルで古巣を圧倒。ヒートは9勝3敗に。",
      "excerpt": "マイアミがハイスコアゲームを制し137-130でバックスを撃破。ナゲッツはセルティックスに17点差からの大逆転勝利。",
      "body": [
        "11月18日水曜日の夜、マイアミのカセヤ・センターでヤニス・アデトクンボが古巣ミルウォーキー・バックスと初対戦し、27得点14リバウンド9アシストと大車輪の活躍で137-130の勝利に導きました。",
        "アデバヨが26得点、ヒーローが23得点をマークしたヒートはチームFG成功率54.3%を記録し、今季最長の6連勝を飾りました。",
        "デンバーでは、ヨキッチが24得点9アシスト8リバウンドを挙げ、17点ビハインドを跳ね返したナゲッツがボストン・セルティックスを105-101で下しました。"
      ]
    },
    "ko": {
      "title": "야니스 친정팀에 비수: 27득점 트리플더블급 맹활약으로 히트 6연승 견인 (137-130)",
      "subtitle": "아데토쿤보가 밀워키와의 첫 맞대결에서 27득점 14리바운드 9어시스트를 기록하며 마이애미의 상승세를 이끌었습니다.",
      "excerpt": "마이애미 히트가 벅스를 137-130으로 난타전 끝에 꺾었습니다. 덴버 너기츠는 보스턴을 상대로 17점 차 역전승을 거뒀습니다.",
      "body": [
        "11월 18일 수요일 밤 마이애미 카세야 센터에서 열린 친정팀과의 맞대결에서 야니스 아데토쿤보가 27득점 14리바운드 9어시스트를 기록하며 마이애미 히트의 137-130 승리를 이끌었습니다.",
        "뱀 아데바요가 26득점 10리바운드로 골밑을 장악한 히트는 6연승을 질주하며 9승 3패를 기록, 동부 2위를 공고히 했습니다.",
        "한편 덴버 너기츠는 니콜라 요키치(24득점 9어시스트 8리바운드)를 앞세워 17점 차 열세를 뒤집고 보스턴 셀틱스를 105-101로 꺾었습니다."
      ]
    },
    "ar": {
      "title": "عرض استثنائي ليانيس: 27 نقطة أمام فريقه السابق تقود هيت للفوز السادس تواليا (137-130)",
      "subtitle": "أنتيتوكونمبو يسجل 27 نقطة و14 متابعة و9 تمريرات حاسمة في ليلة عاطفية بملعب كاسيا سنتر.",
      "excerpt": "ميامي هيت يتفوق على ميلووكي باكس 137-130 بفضل تألق يانيس، بينما قلب دنفر ناغتس تأخره بفارق 17 نقطة ليفوز على سلتيكس.",
      "body": [
        "قدم النجم يانيس أنتيتوكونمبو أداء لا ينسى مساء الأربعاء 18 نوفمبر حين واجه فريقه السابق ميلووكي باكس لأول مرة، ليقود ميامي هيت لفوز مثير بنتيجة 137-130 في كاسيا سنتر.",
        "واقترب النجم اليوناني من تحقيق ثلاثة أرقام مزدوجة بتسجيله 27 نقطة و14 متابعة و9 تمريرات، وأضاف بام أديبايو 26 نقطة ليحقق ميامي فوزه السادس على التوالي ويرفع رصيده إلى 9 انتصارات.",
        "وفي دنفر، نجح ناغتس بقيادة نيكولا يوكيتش (24 نقطة و9 تمريرات) في قلب تأخره بفارق 17 نقطة ليتفوق على بوسطن سلتيكس 105-101."
      ]
    }
  },
  "nations-league-haaland-fires-norway-past-denmark-3-2-parken-2026": {
    "fr": {
      "title": "Haaland crucifie le Danemark : La Norvège s'impose 3-2 à Copenhague en Ligue des nations",
      "subtitle": "Erling Haaland inscrit le but de la victoire à la 88e minute d'un derby scandinave d'anthologie pour clore la phase de poules.",
      "excerpt": "Fin de match irrespirable au Parken Stadium où la Norvège bat le Danemark 3-2 grâce à Haaland, avant le retour des championnats ce week-end.",
      "body": [
        "La phase de groupes de la Ligue des nations de l'UEFA s'est achevée de manière spectaculaire mardi soir, 17 novembre, avec le triomphe de la Norvège 3-2 sur le Danemark au Parken Stadium de Copenhague.",
        "Dans ce choc nordique haletant, les Danois ont ouvert la marque par Hojlund, avant que Sorloth n'égalise de la tête. Antonio Nusa a donné l'avantage aux Norvégiens d'une superbe frappe enveloppée à la 61e, mais Christian Eriksen a remis les compteurs à zéro sur un sublime coup franc direct à la 74e minute.",
        "C'est finalement Erling Haaland qui a fait la décision à la 88e minute en profitant d'un service parfait de Martin Odegaard pour battre le portier danois d'un tir rasant. La trêve internationale terminée, les regards se tournent vers la Premier League dès samedi."
      ]
    },
    "es": {
      "title": "Haaland decide en el 88: Noruega supera 3-2 a Dinamarca en un electrizante derbi nórdico",
      "subtitle": "Erling Haaland sella un agónico triunfo en el Parken de Copenhague en el cierre de la fase de grupos de la Liga de Naciones.",
      "excerpt": "Un gol de Haaland en los minutos finales le da a Noruega la victoria 3-2 en Dinamarca, dando paso al regreso de las ligas europeas este fin de semana.",
      "body": [
        "La fase de grupos de la UEFA Nations League bajó el telón con un auténtico partidazo el martes 17 de noviembre, en el que Noruega derrotó 3-2 a Dinamarca en el Parken Stadium de Copenhague.",
        "Tras los tantos de Hojlund para Dinamarca y de Sorloth y Nusa para Noruega, Christian Eriksen levantó a la grada con un soberbio gol de falta en el minuto 74. Sin embargo, en el 88, una conexión entre Martin Odegaard y Erling Haaland terminó con el ariete definiendo con la zurda para sentenciar el choque.",
        "Con el parón de selecciones finalizado, la atención regresa este sábado a la Premier League, donde el Arsenal defenderá su liderato con 27 puntos ante el acecho de Brighton y City."
      ]
    },
    "de": {
      "title": "Haaland schlägt spät zu: Norwegen siegt nach Spektakel mit 3:2 in Dänemark",
      "subtitle": "Erling Haaland erzielt in der 88. Minute den Siegtreffer im packenden Skandinavien-Derby zum Abschluss der Nations League.",
      "excerpt": "Dramatisches Finale im Parken von Kopenhagen: Norwegen schlägt Dänemark mit 3:2 durch Haalands späten Treffer vor der Rückkehr des Ligafußballs.",
      "body": [
        "Die Gruppenphase der UEFA Nations League fand am Dienstagabend, 17. November, einen spektakulären Schlusspunkt, als Norwegen den Erzrivalen Dänemark im Kopenhagener Parken-Stadion mit 3:2 niederrang.",
        "Nach Toren von Hojlund für Dänemark sowie Sorloth und Nusa für Norwegen glich Christian Eriksen in der 74. Minute per Traumfreistoß aus. In der 88. Minute bediente Martin Ödegaard seinen Sturmstar Erling Haaland, der eiskalt zum 3:2-Endstand vollstreckte.",
        "Damit ist die Länderspielpause beendet. Ab Samstag richtet sich der Blick wieder auf die Premier League, in der Arsenal (27 Punkte) die Tabelle vor Brighton (22) und Manchester City (21) anführt."
      ]
    },
    "it": {
      "title": "Haaland decide all'88': La Norvegia espugna la Danimarca 3-2 nel derby scandinavo",
      "subtitle": "Erling Haaland firma il gol vittoria a Copenaghen chiudendo la fase a gironi di Nations League.",
      "excerpt": "Partita memorabile al Parken Stadium dove la Norvegia supera la Danimarca 3-2 grazie al timbro nel finale del suo bomber.",
      "body": [
        "La fase a gironi di UEFA Nations League si è chiusa con fuochi d'artificio martedì sera, 17 novembre, con la vittoria per 3-2 della Norvegia sulla Danimarca al Parken Stadium di Copenaghen.",
        "In un match ricchissimo di emozioni, ai gol di Hojlund, Sorloth e Nusa ha risposto la perla su punizione di Christian Eriksen al 74'. A due minuti dal novantesimo, un assist al bacio di Martin Odegaard ha liberato Erling Haaland per il diagonale del definitivo 3-2.",
        "Conclusa la finestra delle nazionali, l'attenzione torna sui campionati nazionali, a partire dalla Premier League che riparte sabato con l'Arsenal al comando a quota 27 punti."
      ]
    },
    "pl": {
      "title": "Haaland uderza w 88. minucie: Norwegia wygrywa z Danią 3:2 w hicie Ligi Narodów",
      "subtitle": "Erling Haaland strzela decydującego gola w Kopenhadze, pieczętując triumf w skandynawskim klasyku na koniec fazy grupowej.",
      "excerpt": "Niezwykłe emocje na Parken Stadium: Norwegia ogrywa Danię 3:2 po bramce Haalanda tuż przed wznowieniem rozgrywek ligowych.",
      "body": [
        "Faza grupowa Ligi Narodów UEFA zakończyła się we wtorek 17 listopada fantastycznym widowiskiem w Kopenhadze, gdzie Norwegia pokonała Danię 3:2.",
        "Gospodarze prowadzili po trafieniu Hojlunda, lecz Sorloth i Nusa dali prowadzenie Norwegom. W 74. minucie Christian Eriksen popisał się kapitalnym golem z rzutu wolnego, jednak ostatnie słowo należało do Haalanda, który po podaniu Odegaarda ustalił wynik w 88. minucie.",
        "Koniec przerwy reprezentacyjnej oznacza powrót ligowych emocji: już w sobotę w Premier League liderujący Arsenal (27 pkt) broni przewagi nad Brightonem i Manchesterem City."
      ]
    },
    "zh": {
      "title": "哈兰德第88分钟绝杀：挪威客场3-2力克丹麦收官欧国联小组赛",
      "subtitle": "哈兰德在哥本哈根帕肯球场上演终场绝杀，五球北欧德比大战为欧洲国家联赛秋季战事画上句号。",
      "excerpt": "欧国联小组赛在火爆的北欧德比中收官，哈兰德接厄德高妙传打入绝杀进球，挪威客场3-2险胜丹麦，周末俱乐部赛事重燃战火。",
      "body": [
        "11月17日周二晚间，欧洲国家联赛小组赛以极具戏剧性的一幕落下帷幕，挪威队凭借哈兰德在第88分钟的绝杀，在哥本哈根帕肯球场以3-2险胜老对手丹麦队。",
        "霍伊伦为丹麦首开纪录，随后索尔洛特头球扳平，努萨世界波助挪威反超。埃里克森在第74分钟用标志性直接任意球将比分扳为2-2。比赛尾声阶段，队长厄德高送出穿透性直塞，哈兰德凭借强悍身体护球推射远角破门锁定胜局。",
        "随着欧国联小组赛全面结束，欧洲五大联赛将于本周末回归。英超联赛将在周六打响第11轮，榜首阿森纳（27分）将全力捍卫对布莱顿（22分）与曼城（21分）的领先优势。"
      ]
    },
    "ja": {
      "title": "ハーランドが88分に劇的決勝弾：ノルウェーがデンマークを3-2で下し大会終幕",
      "subtitle": "ハーランドがコペンハーゲンのパルケン・スタジアムで北欧ダービーを決着づける一撃。ネーションズリーグGSが終了。",
      "excerpt": "ネーションズリーグGS最終節でノルウェーがデンマークに3-2で競り勝つ。代表ウィークが明け週末から国内リーグ再開へ。",
      "body": [
        "UEFAネーションズリーグのグループステージが11月17日火曜日に全日程を終了し、パルケン・スタジアムで行われた北欧ダービーでノルウェーがデンマークを3-2で下しました。",
        "ホイルンドの先制弾に対し、スルロットとヌサのゴールでノルウェーが逆転。エリクセンが74分に芸術的なFKを沈めて追いつきましたが、88分にウーデゴールの絶妙なスルーパスを受けたハーランドが左足で勝ち越しゴールを決めました。",
        "代表戦期間が終わり、今週末の21日土曜日からはプレミアリーグが再開。首位アーセナル（27点）がブライトン（22点）とマンチェスター・シティ（21点）を従えて過密日程に挑みます。"
      ]
    },
    "ko": {
      "title": "홀란 88분 극장 결승골: 노르웨이, 덴마크에 3-2 역전승 거두고 조별리그 피날레",
      "subtitle": "엘링 홀란이 코펜하겐 파르켄 스타디움에서 터뜨린 결승골로 북유럽 라이벌전을 승리로 장식했습니다.",
      "excerpt": "네이션스리그 조별리그가 노르웨이의 극적인 3-2 승리로 마무리되었습니다. 이번 주말 프리미어리그 등 클럽 축구가 재개됩니다.",
      "body": [
        "11월 17일 화요일 밤 코펜하겐 파르켄 스타디움에서 열린 UEFA 네이션스리그 조별리그 최종전에서 노르웨이가 엘링 홀란의 88분 극장골에 힘입어 덴마크를 3-2로 제압했습니다.",
        "회일룬의 선제골 후 쇠를로스와 누사의 연속골로 노르웨이가 전세를 뒤집었으나, 에릭센이 74분 프리킥으로 동점을 만들었습니다. 그러나 경기 종료 직전 외데고르의 패스를 받은 홀란이 침착한 마무리로 원정 승리를 확정지었습니다.",
        "A매치 휴식기가 끝나면서 이번 주말인 21일 토요일부터 아스널(27점), 브라이튼(22점), 맨시티(21점)가 각축을 벌이는 프리미어리그 일정이 재개됩니다."
      ]
    },
    "ar": {
      "title": "هالاند يلدغ في الدقيقة 88: النرويج تسقط الدنمارك 3-2 في ديربي إسكندنافي مثير",
      "subtitle": "إيرلينغ هالاند يحسم قمة ملعب باركن بهدف متأخر في ختام دور المجموعات لدوري الأمم الأوروبية.",
      "excerpt": "النرويج تحقق فوزا دراميا 3-2 على الدنمارك بفضل هدف هالاند القاتل، والأنظار تتحول إلى عودة الدوريات الأوروبية نهاية الأسبوع.",
      "body": [
        "أسدل الستار على دور المجموعات لدوري الأمم الأوروبية مساء الثلاثاء 17 نوفمبر بمواجهة ملحمية تفوقت فيها النرويج على غريمتها الدنمارك بنتيجة 3-2 على ملعب باركن في كابنهاغن.",
        "افتتح هويلوند التسجيل لأصحاب الأرض، ليرد سورلوث ونوسا لصالح النرويج، قبل أن يدرك كريستيان إريكسن التعادل بركلة حرة ساحرة في الدقيقة 74. ولكن في الدقيقة 88، أرسل مارتن أوديغارد تمريرة حاسمة لهالاند الذي حسم الانتصار بتسديدة زاحفة.",
        "ومع انتهاء فترة التوقف الدولي، تتجه الأنظار إلى عودة الدوري الإنجليزي الممتاز يوم السبت 21 نوفمبر، حيث يتصدر أرسنال برصيد 27 نقطة أمام برايتون ومانشستر سيتي."
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

