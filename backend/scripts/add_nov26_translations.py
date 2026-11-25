# Inject 10-language translations for the 6 Nov 26, 2026 stories into frontend/src/i18n/stories.ts
import os
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
STORIES_TS = os.path.join(ROOT, "frontend", "src", "i18n", "stories.ts")

translations = {
  "nfl-thanksgiving-lions-bears-thanksgiving-clash-week12-2026": {
    "fr": {
      "title": "Thanksgiving NFL : Lions et Bears a 8-2 s'affrontent a Ford Field pour la tete de la NFC Nord",
      "subtitle": "Ben Johnson revient a Detroit aux commandes des Bears de Caleb Williams face aux Lions de Dan Campbell sur CBS.",
      "excerpt": "Pour la quatrieme fois seulement en 193 duels, Chicago et Detroit se retrouvent a Thanksgiving avec un bilan identique de 8-2 et la premiere place en jeu.",
      "body": [
        "La grande fete americaine du football debute jeudi 26 novembre par un choc monumental au Ford Field entre les Detroit Lions et les Chicago Bears (13h00 ET, CBS), avec deux rivaux historiques presents a egalite parfaite de 8 victoires pour 2 defaites.",
        "Les Lions de Dan Campbell arrivent sur six succes consecutifs et un bilan parfait de 6-0 a domicile apres leur victoire 31-21 contre Tampa Bay, portes par Jared Goff, Jameson Williams et Jahmyr Gibbs.",
        "Sur la ligne de touche opposee, l'ancien coordinateur Ben Johnson retrouve Detroit avec des Bears invaincus depuis cinq matchs. Depuis son retour de blessure, Caleb Williams n'a jamais concede l'avantage au score lors des cinq dernieres rencontres, avant le grand choc nocturne entre Chiefs (8-2) et Bills (9-1)."
      ]
    },
    "es": {
      "title": "Accion de Gracias NFL: Lions y Bears con marca de 8-2 chocan en Ford Field por la cima",
      "subtitle": "Ben Johnson regresa a Detroit al frente de los Bears de Caleb Williams ante unos Lions con seis triunfos seguidos.",
      "excerpt": "Por cuarta vez en 193 duelos historicos, Chicago y Detroit se miden en Thanksgiving con identico registro de 8-2 y el liderato de la NFC Norte en juego.",
      "body": [
        "La tradicional jornada de Accion de Gracias abre el jueves 26 de noviembre con un duelo enorme en Ford Field (13:00 ET, CBS), donde los Detroit Lions y los Chicago Bears llegan igualados a 8-2.",
        "Detroit defiende un invicto de 6-0 en casa y seis victorias consecutivas tras superar 31-21 a Tampa Bay, guiado por Jared Goff, Jameson Williams y dos touchdowns de Jahmyr Gibbs.",
        "En la banda visitante, el excoordinador Ben Johnson lidera unos Bears con cinco triunfos al hilo sin haber ido por detras en el marcador en ninguno de ellos desde el regreso de Caleb Williams, antes del estelar Chiefs (8-2) ante Bills (9-1)."
      ]
    },
    "de": {
      "title": "Thanksgiving Football: Lions und Bears mit 8-2-Bilanz kaempfen im Ford Field um Platz eins",
      "subtitle": "Ben Johnson kehrt mit den Bears und Caleb Williams nach Detroit gegen Dan Campbells Lions zurueck.",
      "excerpt": "Zum vierten Mal in 193 Duellen treffen Chicago und Detroit am Thanksgiving Day mit identischer 8-2-Bilanz um die Fuehrung in der NFC North aufeinander.",
      "body": [
        "Der amerikanische Football-Feiertag beginnt am Donnerstag, 26. November, mit einem Spitzenspiel im Ford Field (13:00 Uhr ET, CBS), wenn die Detroit Lions die Chicago Bears bei jeweils 8-2 empfangen.",
        "Dan Campbells Lions gehen mit sechs Siegen in Serie und makelloser 6-0-Heimbilanz nach dem 31:21 gegen Tampa Bay ins Rennen, angefuehrt von Jared Goff und Jahmyr Gibbs.",
        "Auf der Gegenseite kehrt Ex-Koordinator Ben Johnson als Bears-Headcoach mit fuenf Siegen am Stueck zurueck. Caleb Williams lag dabei in keinem einzigen Spiel sekundenlang hinten, bevor am Abend die Chiefs (8-2) bei den Bills (9-1) antreten."
      ]
    },
    "it": {
      "title": "Thanksgiving NFL: Lions e Bears a 8-2 si sfidano al Ford Field per il primato nella NFC North",
      "subtitle": "Ben Johnson torna a Detroit alla guida dei Bears di Caleb Williams contro i Lions reduci da sei vittorie consecutive.",
      "excerpt": "Per la quarta volta in 193 sfide storiche, Chicago e Detroit si incontrano nel giorno del Ringraziamento con record identico di 8-2.",
      "body": [
        "La grande tradizione del Ringraziamento americano scatta giovedi 26 novembre al Ford Field (13:00 ET, CBS) con un confronto ad altissima tensione tra Detroit Lions e Chicago Bears, appaiati a quota 8-2.",
        "I Lions di Dan Campbell vantano una striscia di sei successi e un percorso netto di 6-0 in casa dopo il 31-21 su Tampa Bay, spinti da Jared Goff, Jameson Williams e Jahmyr Gibbs.",
        "Sulla panchina ospite siede l'ex Ben Johnson alla guida di Chicago, capace di cinque vittorie di fila con Caleb Williams senza mai inseguire nel punteggio, prima della sfida serale tra Chiefs (8-2) e Bills (9-1)."
      ]
    },
    "pl": {
      "title": "Swieto Dziekczynienia w NFL: Lions i Bears z bilansem 8-2 graja o fotel lidera NFC North",
      "subtitle": "Ben Johnson wraca do Detroit z Chicago Bears Caleba Williamsa na starcie z rozpędzonymi Lions na Ford Field.",
      "excerpt": "Czwarty raz w historii 193 spotkan Chicago i Detroit staja naprzeciw siebie w Thanksgiving z identycznym bilansem 8-2 i pierwszym miejscem w dywizji w stawce.",
      "body": [
        "Tradycyjny maraton futbolowy w czwartek 26 listopada otworzy starcie na szczycie na Ford Field (13:00 ET, CBS), gdzie Detroit Lions podejma Chicago Bears przy rownym bilansie 8-2 obu druzyn.",
        "Zespol Dana Campbella moze pochwalic sie sześcioma wygranymi z rzedu i bilansem 6-0 u siebie po zwyciestwie 31:21 nad Tampa Bay, napedzany przez Jareda Goffa i Jahmyr Gibbsa.",
        "Po drugiej stronie boiska byly koordynator z Detroit Ben Johnson prowadzi Bears po pieciu wygranych z rzedu bez ani jednej sekundy straty punktowej od powrotu Caleba Williamsa, a wieczorem Chiefs (8-2) zagraja z Bills (9-1)."
      ]
    },
    "zh": {
      "title": "NFL感恩节盛宴：同为8胜2负的雄狮与熊队福特球场角逐国北榜首",
      "subtitle": "本·约翰逊重返底特律率领凯勒布·威廉姆斯的熊队，挑战豪取六连胜的丹·坎贝尔雄狮。",
      "excerpt": "芝加哥熊队与底特律雄狮队史193次交锋仅第4次在感恩节以同为8胜2负的战绩正面碰撞。",
      "body": [
        "美国传统橄榄球节日大战将于11月26日周四拉开帷幕，底特律雄狮坐镇福特球场迎战芝加哥熊（美东13:00，CBS直播），两支宿敌同以8胜2负并列国联北区榜首。",
        "丹·坎贝尔执教的雄狮目前主场6胜0负且豪取六连胜，上一轮31比21击败坦帕湾海盗的比赛中，四分卫贾里德·戈夫与跑卫贾迈尔·吉布斯表现极其稳健。",
        "熊队主帅本·约翰逊此番重返旧地福特球场。自四分卫凯勒布·威廉姆斯伤愈复出以来，芝加哥已豪取五连胜且连续五场一秒未落后，而在夜场酋长（8胜2负）还将客战比尔（9胜1负）。"
      ]
    },
    "ja": {
      "title": "NFL感謝祭決戦：ともに8勝2敗のライオンズとベアーズがNFC北首位を懸け激突",
      "subtitle": "ベン・ジョンソンがベアーズを率いてデトロイトへ凱旋、6連勝のライオンズとフォード・フィールドで対決。",
      "excerpt": "通算193回の対戦で史上4度目となる同率8勝2敗でのサンクスギビング決戦、勝利チームが単独首位に立つ。",
      "body": [
        "11月26日木曜日、NFL伝統の感謝祭トリプルヘッダーはフォード・フィールドでの大一番（米東部13:00、CBS）で開幕する。デトロイト・ライオンズとシカゴ・ベアーズがともに8勝2敗で相まみえる。",
        "ダン・キャンベル率いるライオンズは今季ホーム6戦全勝で6連勝中。タンパベイ戦を31-21で制したジェレッド・ゴフとジャミア・ギブスの攻撃陣が火を吹く。",
        "敵将ベンチには元ライオンズ攻撃陣の知将ベン・ジョンソンが座る。ケイレブ・ウィリアムズの復帰後、ベアーズは5連勝中すべてで一度もリードを許さずに進撃しており、夜にはチーフス（8勝2敗）対ビルズ（9勝1敗）も控える。"
      ]
    },
    "ko": {
      "title": "NFL 추수감사절 빅매치: 8승 2패 동률 라이온스와 베어스, NFC 북부 1위 격돌",
      "subtitle": "벤 존슨 감독이 케일럽 윌리엄스의 베어스를 이끌고 포드 필드로 돌아와 6연승의 라이온스와 맞붙는다.",
      "excerpt": "역대 193차례 맞대결 중 단 네 번째로 양 팀이 8승 2패 동률 상태에서 추수감사절에 충돌한다.",
      "body": [
        "11월 26일 목요일, 미국의 추수감사절 풋볼 축제가 포드 필드에서 열리는 디트로이트 라이온스와 시카고 베어스의 빅매치(미 동부 13:00 CBS)로 막을 올린다.",
        "댄 캠벨 감독의 라이온스는 탬파베이전 31-21 승리를 포함해 6연승과 홈 6전 전승을 달리고 있으며, 재러드 고프와 자미르 깁스가 막강한 공격을 이끌고 있다.",
        "원정팀 벤치에는 친정팀 디트로이트로 돌아온 벤 존슨 감독이 자리한다. 케일럽 윌리엄스 복귀 이후 5연승 동안 단 한 순간도 리드를 내주지 않은 베어스는 야간 칩스(8-2)-빌스(9-1)전에 앞서 단독 선두를 노린다."
      ]
    },
    "ar": {
      "title": "مواجهات عيد الشكر في NFL: لايونز وبيرز بسجل 8-2 يتصادمان على قمة القسم الشمالي",
      "subtitle": "بن جونسون يعود الى ديترويت مدربا لبيرز بقيادة كالب ويليامز لمواجهة لايونز المنتشي بستة انتصارات متتالية.",
      "excerpt": "للمرة الرابعة فقط في 193 مواجهة تاريخية، يلتقي شيكاغو وديترويت في عيد الشكر بسجل متطابق 8-2 والصدارة على المحك.",
      "body": [
        "تنطلق احتفالات كرة القدم الامريكية يوم الخميس 26 نوفمبر بقمة من العيار الثقيل في فورد فيلد (1:00 ظهرا بتوقيت شرق امريكا على CBS)، حيث يستضيف ديترويت لايونز غريمه شيكاغو بيرز بسجل متطابق 8-2 لكل فريق.",
        "يدخل فريق لايونز بقيادة دان كامبل المواجهة بسلسلة ستة انتصارات متتالية وسجل مثالي على ارضه (6-0) بعد الفوز 31-21 على تامبا باي بتالق جارد غوف وجامير جيبس.",
        "على الخط المقابل يقود المدرب بن جونسون فريق بيرز العائد بسلسلة خمسة انتصارات متتالية دون ان يتاخر في النتيجة ولو لثانية واحدة منذ عودة كالب ويليامز، قبل القمة الليلية بين كانساس سيتي تشيفز (8-2) وبافالو بيلز (9-1)."
      ]
    }
  },
  "champions-league-real-madrid-rout-psv-5-1-mbappe-bellingham-2026": {
    "fr": {
      "title": "Ligue des champions : Le Real Madrid passe cinq buts en seconde periode au PSV (5-1) et reste seul leader",
      "subtitle": "Valverde, Bellingham, Mbappe par deux fois et Vinicius frappent en 37 minutes pour porter Madrid a 15 points.",
      "excerpt": "Apres un penalty d'Ivan Perisic avant la pause, le Real Madrid se dechaine au retour des vestiaires pour ecraser le PSV 5-1 au Bernabeu.",
      "body": [
        "Le Real Madrid a frappe un grand coup mardi soir 24 novembre en retournant une situation delicate pour surclasser le PSV Eindhoven 5-1 au Santiago Bernabeu et rester l'unique equipe avec 15 points apres cinq journees.",
        "Ivan Perisic avait donne l'avantage aux Neerlandais sur penalty a la 32e minute. Mais cinq minutes apres la reprise, Federico Valverde a egalise avant qu'un bijou de Jude Bellingham a la 60e ne fasse basculer le match.",
        "Kylian Mbappe a ensuite inscrit un double (64e, 84e) avant que Vinicius Junior ne scelle le score a la 87e. Ailleurs, Arsenal a partage 1-1 avec Dortmund (Gyokeres 10e, Beier 55e) et Man City a fait 2-2 contre Naples, tandis qu'Arsenal mene la Premier League avec 28 points."
      ]
    },
    "es": {
      "title": "Autoridad Champions: El Real Madrid golea 5-1 al PSV en el Bernabeu y sigue lider con 15 puntos",
      "subtitle": "Valverde, Bellingham, Mbappe por partida doble y Vinicius rematan en 37 minutos una remontada implacable tras el descanso.",
      "excerpt": "Ivan Perisic adelanto de penalti al PSV, pero cinco goles blancos en la segunda mitad dejan al Real Madrid con pleno de cinco victorias.",
      "body": [
        "El Real Madrid confirmo su dominio europeo la noche del martes 24 de noviembre al desatar un vendaval ofensivo tras el descanso para arrollar 5-1 al PSV Eindhoven en el Santiago Bernabeu y quedar como lider solitario con 15 puntos.",
        "Ivan Perisic habia sorprendido transformando un penalti en el minuto 32 para el PSV. En el 50 igualo Federico Valverde y diez minutos despues Jude Bellingham giro el partido con un golazo desde fuera del area.",
        "Kylian Mbappe sentencio con un doblete en los minutos 64 y 84 y Vinicius Junior redondeo la manita en el 87. En los otros grandes duelos del martes, el Arsenal empato 1-1 con el Dortmund (Gyokeres 10; Beier 55) y el Manchester City firmo un 2-2 ante el Napoles."
      ]
    },
    "de": {
      "title": "Champions League: Real Madrid ueberrollt PSV nach der Pause mit 5:1 und bleibt alleiniger Tabellenfuehrer",
      "subtitle": "Valverde, Bellingham, Mbappe doppelt und Vinicius Jr drehen das Spiel binnen 37 Minuten zu Real Madrids fuenftem Sieg.",
      "excerpt": "Nach Ivan Perisics Elfmeter zur PSV-Pausenfuerung erzielt Real Madrid fuenf Tore in der zweiten Halbzeit zum 5:1-Triumph mit maximalen 15 Punkten.",
      "body": [
        "Real Madrid setzte am Dienstagabend, 24. November, ein klares Zeichen an der Tabellenspitze und fertigte PSV Eindhoven nach Rueckstand noch mit 5:1 im Santiago Bernabeu ab - als einziges Team mit makellosen 15 Punkten.",
        "Ivan Perisic hatte PSV in der 32. Minute per Strafstoss in Fuehrung gebracht. Doch Federico Valverde glich in der 50. Minute aus, ehe Jude Bellingham in der 60. mit einem Traumtor die Partie drehte.",
        "Kylian Mbappe traf in der 64. und 84. Minute doppelt, und Vinicius Junior markierte den 5:1-Endstand (87.). Zuvor trennten sich Arsenal und Borussia Dortmund 1:1 (Gyokeres 10., Beier 55.) sowie Man City und Neapel 2:2."
      ]
    },
    "it": {
      "title": "Champions League: Il Real Madrid travolge 5-1 il PSV nella ripresa e resta solo in testa con 15 punti",
      "subtitle": "Valverde, Bellingham, doppietta di Mbappe e Vinicius scatenano 37 minuti furiosi al Bernabeu.",
      "excerpt": "Dopo il rigore di Ivan Perisic per gli olandesi, cinque reti nella ripresa regalano al Real Madrid la quinta vittoria in cinque partite.",
      "body": [
        "Il Real Madrid ha confermato la sua leadership europea martedi sera 24 novembre ribaltando con autorita il PSV Eindhoven fino al 5-1 finale al Santiago Bernabeu, restando l'unica squadra a punteggio pieno a quota 15.",
        "Ivan Perisic aveva portato avanti il PSV su rigore al 32' minuto. Al rientro dagli spogliatoi sono pero bastati cinque minuti a Federico Valverde (50') per pareggiare, prima della perla di Jude Bellingham al 60'.",
        "Kylian Mbappe ha firmato la doppietta (64' e 84') e Vinicius Junior ha chiuso i conti all'87'. Negli altri big match di martedi, Arsenal-Dortmund e finita 1-1 (Gyokeres 10', Beier 55') e Manchester City-Napoli 2-2."
      ]
    },
    "pl": {
      "title": "Liga Mistrzow: Real Madryt rozbil PSV 5:1 po przerwie i jest jedynym liderem z kompletem 15 punktow",
      "subtitle": "Valverde, Bellingham, dwa gole Mbappe i Vinicius rozstrzelali rywala w 37 minut na Bernabeu.",
      "excerpt": "Po rzucie karnym Ivana Perisicia Real Madryt odpowiedzial piecioma golami w drugiej polowie, utrzymujac bilans pieciu zwyciestw w pieciu meczach.",
      "body": [
        "Real Madryt potwierdzil europejska dominacje we wtorek wieczorem 24 listopada, odrabiajac straty z pierwszej polowy i rozbijajac PSV Eindhoven 5:1 na Santiago Bernabeu jako jedyny klub z 15 punktami w tabeli.",
        "W 32. minucie Ivan Perisic wykorzystal rzut karny dla PSV. Po zmianie stron sygnal do ataku dal Federico Valverde (50.), a po dziesieciu minutach pieknym trafieniem wynik odmienil Jude Bellingham (60.).",
        "Dwa ciosy zadal Kylian Mbappe (64., 84.), a wynik zamknal Vinicius Junior w 87. minucie. W innych hitach wtorku Arsenal zremisowal z Dortmundem 1:1 (Gyokeres 10., Beier 55.), a Manchester City podzielil sie punktami z Napoli (2:2)."
      ]
    },
    "zh": {
      "title": "欧冠权威：皇马下半场轰五球5-1逆转埃因霍温，五战全胜独居榜首",
      "subtitle": "巴尔韦德、贝林厄姆、姆巴佩梅开二度与维尼修斯37分钟内连入五球，伯纳乌绽放狂攻火力。",
      "excerpt": "佩里西奇上半场点射破门后，皇家马德里在下半场连下五城5-1横扫埃因霍温，成为36强唯一15分领跑者。",
      "body": [
        "11月24日周二欧冠第5轮，皇家马德里在伯纳乌球场上演酣畅淋漓的下半场逆转，以5比1大胜埃因霍温，以五战全胜积15分傲视36强积分榜。",
        "上半场第32分钟，老将伊万·佩里西奇主罚点球为客队先声夺人。但下半场第50分钟费德里科·巴尔韦德率先扳平比分，随后第60分钟祖德·贝林厄姆禁区外兜射世界波反超。",
        "基利安·姆巴佩在第64和第84分钟连进两球扩大优势，维尼修斯在第87分钟完成绝杀锦上添花。同日其他焦点战中，阿森纳1比1战平多特蒙德（哲凯赖什第10分钟、拜尔第55分钟），曼城2比2战平那不勒斯。"
      ]
    },
    "ja": {
      "title": "欧州CL：レアル・マドリードが後半5ゴールでPSVに5-1圧勝、無傷の5連勝で単独首位",
      "subtitle": "バルベルデ、ベリンガム、ムバッペ2発、ヴィニシウスが後半の37分間でベルナベウを沸かせる。",
      "excerpt": "ペリシッチのPKで先制を許したマドリードが後半に5得点を奪う猛攻を見せ、36チーム中唯一の勝ち点15に到達。",
      "body": [
        "11月24日火曜日のUEFAチャンピオンズリーグ第5節で、レアル・マドリードはサンティアゴ・ベルナベウでPSVアイントホーフェンを後半のゴールラッシュで5-1と粉砕し、5戦全勝の勝ち点15で首位を独走している。",
        "前半32分、イヴァン・ペリシッチのPKでPSVが先行する波乱の展開となったが、後半50分にフェデリコ・バルベルデが同点弾を叩き込み、60分にはジュード・ベリンガムの美しいミドルシュートで一気に逆転した。",
        "さらにキリアン・ムバッペが64分と84分に連続ゴールを挙げ、87分にヴィニシウス・ジュニオールが締めくくった。同時開催の注目カードでは、アーセナルがドルトムントと1-1（ギェケレシュ10分、バイアー55分）、マンチェスター・シティがナポリと2-2で引き分けた。"
      ]
    },
    "ko": {
      "title": "UCL 제왕의 위엄: 레알 마드리드, 후반에만 5골 폭발하며 PSV에 5-1 대승 및 5연승 단독 선두",
      "subtitle": "발베르데, 벨링엄, 음바페 멀티골, 비니시우스가 37분 만에 5골을 몰아치며 승점 15점 고지를 밟았다.",
      "excerpt": "페리시치에게 페널티킥 선제골을 허용한 레알 마드리드가 후반전 5득점 화력을 앞세워 PSV를 5-1로 대파했다.",
      "body": [
        "11월 24일 화요일 UEFA 챔피언스리그 리그 페이즈 5차전에서 레알 마드리드가 산티아고 베르나베우 홈팬들 앞에서 PSV 에인트호번에 5-1 역전 대승을 거두고 유일한 5전 전승 승점 15점 선두에 올랐다.",
        "전반 32분 이반 페리시치의 페널티킥으로 리드를 내준 레알 마드리드는 후반 50분 페데리코 발베르데의 동점골로 반격을 시작한 뒤 60분 주드 벨링엄의 환상적인 역전골로 흐름을 완벽히 뒤집었다.",
        "이어 킬리안 음바페가 64분과 84분 연속골을 터뜨렸고, 87분 비니시우스 주니오르가 대미를 장식했다. 같은 날 아스널은 도르트문트와 1-1(요케레스 10분, 바이어 55분), 맨시티는 나폴리와 2-2 무승부를 기록했다."
      ]
    },
    "ar": {
      "title": "دوري الابطال: ريال مدريد يضرب ايندهوفن بخماسية في الشوط الثاني (5-1) وينفرد بالصدارة بـ15 نقطة",
      "subtitle": "فالفيردي وبيلينغهام ومبابي مرتين وفينيسيوس يحسمون مهرجان الاهداف خلال 37 دقيقة في البرنابيو.",
      "excerpt": "بعد تقدم ايفان بيريسيتش من علامة الجزاء، انفجر هجوم ريال مدريد بخمسة اهداف بعد الاستراحة ليواصل السجل المثالي بخمسة انتصارات.",
      "body": [
        "اكد ريال مدريد سطوته الاوروبية مساء الثلاثاء 24 نوفمبر بعد قلب تاخره في الشوط الاول الى فوز كاسح 5-1 على بي اس في ايندهوفن في ملعب سانتياغو برنابيو، ليصبح الفريق الوحيد بالعلامة الكاملة 15 نقطة.",
        "فاجا ايفان بيريسيتش الجماهير بهدف التقدم لايندهوفن من ركلة جزاء في الدقيقة 32. لكن فيديريكو فالفيردي ادرك التعادل في الدقيقة 50، قبل ان يطلق جود بيلينغهام تسديدة ساحرة في الدقيقة 60.",
        "واضاف كيليان مبابي ثنائية في الدقيقتين 64 و84 قبل ان يختتم فينيسيوس جونيور الخماسية في الدقيقة 87. وفي بقية قمم الثلاثاء تعادل ارسنال 1-1 مع دورتموند ومانشستر سيتي 2-2 مع نابولي."
      ]
    }
  },
  "f1-qatar-gp-lusail-preview-verstappen-vegas-triumph-norris-battle-2026": {
    "fr": {
      "title": "Avant le GP du Qatar : Verstappen arrive fort de son 75e succes avec un podium mondial ultra serre",
      "subtitle": "Apres 35 changements de leader a Las Vegas, la Formule 1 retrouve son format classique a Lusail.",
      "excerpt": "Max Verstappen aborde la 22e manche a 304 points devant Hamilton (267), Russell (264) et Norris (264) pour le podium final.",
      "body": [
        "La Formule 1 quitte les neons de Las Vegas pour les virages rapides de Lusail lors de la 22e manche, le Grand Prix du Qatar (27-29 novembre). Le week-end revient au format traditionnel avec trois essais libres, qualifications samedi soir et Grand Prix de 57 tours dimanche a 19h00 heure locale.",
        "Max Verstappen arrive fort d'un classique instantane dans le Nevada : au terme de 35 changements en tete, il a signe sa 4e victoire de l'annee et 75e en carriere pour 0,639 seconde devant Lando Norris et Oscar Piastri parti 17e.",
        "Meme si Kimi Antonelli (402 pts) et Mercedes (666 pts) sont deja titres, le classement reste brulant : trois points seulement separent Lewis Hamilton (267) de Russell et Norris (264), tandis que McLaren (431) menace Red Bull (440)."
      ]
    },
    "es": {
      "title": "Previa GP de Catar: Verstappen llega a Lusail tras su victoria 75 con el podio separado por tres puntos",
      "subtitle": "Tras 35 cambios de lider en Las Vegas, la Formula 1 retoma el formato tradicional en Losail del 27 al 29 de noviembre.",
      "excerpt": "Max Verstappen suma 304 puntos antes de Catar, con Hamilton (267) apenas tres por delante de Russell y Norris (264) en lucha cerrada.",
      "body": [
        "La Formula 1 cambia el asfalto nocturno de Nevada por el circuito de Lusail para la Ronda 22, el Gran Premio de Catar (27 al 29 de noviembre), regresando al formato clasico sin carrera Sprint antes de los 57 giros dominicales.",
        "Max Verstappen aterriza impulsado por su 75.a victoria tras ganar por apenas 0,639 segundos a Lando Norris en un caotico Las Vegas con 35 adelantamientos en cabeza y doble podio de McLaren junto a Oscar Piastri desde el 17.o puesto.",
        "Con Kimi Antonelli (402) y Mercedes (666) ya campeones, tres puntos separan a Lewis Hamilton (267) de George Russell y Lando Norris (264), mientras McLaren (431) acecha a solo nueve puntos de Red Bull (440)."
      ]
    },
    "de": {
      "title": "Vorschau Katar GP: Verstappen reist nach 75. Sieg nach Lusail waehrend drei Punkte Platz drei trennen",
      "subtitle": "Nach 35 Fuehrungswechseln auf dem Strip kehrt die Formel 1 in Katar zum gewohnten Drei-Trainings-Format zurueck.",
      "excerpt": "Max Verstappen (304 Pkt.) kommt als Las-Vegas-Sieger nach Lusail, wo Hamilton (267) knapp vor Russell und Norris (je 264) liegt.",
      "body": [
        "Von Las Vegas zieht die Formel 1 direkt weiter auf den Lusail International Circuit zu Runde 22 in Katar (27.-29. November). Anders als zuletzt wird das Wochenende dort im klassischen Format ohne Sprint gefahren, mit dem 57-Runden-Rennen am Sonntagabend.",
        "Max Verstappen feierte in Nevada nach 35 Fuehrungswechseln seinen 75. Grand-Prix-Triumph knapp 0,639 Sekunden vor Lando Norris und Oscar Piastri (von Startplatz 17), waehrend beide Mercedes spaet Pech hatten.",
        "Waehrend Weltmeister Kimi Antonelli (402) und Mercedes (666) bereits feststehen, trennen Lewis Hamilton (267) nur drei Punkte von Russell und Norris (264), und McLaren (431) liegt lediglich neun Zaehler hinter Red Bull (440)."
      ]
    },
    "it": {
      "title": "Anteprima GP del Qatar: Verstappen arriva a Lusail forte del 75esimo successo nella volata per il podio",
      "subtitle": "Dopo i 35 sorpassi in testa a Las Vegas, la Formula 1 torna al weekend tradizionale in Qatar dal 27 al 29 novembre.",
      "excerpt": "Verstappen si presenta a 304 punti, mentre appena tre lunghezze dividono Hamilton (267) da Russell e Norris (264).",
      "body": [
        "La Formula 1 lascia i neon di Las Vegas per i riflettori del Lusail International Circuit in vista del round 22 in Qatar (27-29 novembre). L'evento seguira il formato classico con tre prove libere, qualifiche e gara da 57 giri domenica alle 19:00 locali.",
        "Max Verstappen arriva sulle ali del 75esimo trionfo in carriera conquistato in Nevada al termine di 35 cambi di leader, precedendo Lando Norris per 0,639 secondi e Oscar Piastri risalito dal 17esimo posto.",
        "Nonostante i titoli gia assegnati a Kimi Antonelli (402) e Mercedes (666), tre soli punti separano Lewis Hamilton (267) da George Russell e Lando Norris (264), mentre McLaren (431) insegue la Red Bull (440) a soli nove punti."
      ]
    },
    "pl": {
      "title": "Zapowiedz GP Kataru: Verstappen przybywa do Lusail po 75. triumfie przy pasjonujacej walce o podium",
      "subtitle": "Po szalonym wyscigu z 35 zmianami lidera w Las Vegas F1 wraca do klasycznego formatu bez sprintu.",
      "excerpt": "Max Verstappen ma 304 punkty przed runda nr 22 w Katarze, a Lewisa Hamiltona (267) od Russella i Norrisa (264) dziela trzy oczka.",
      "body": [
        "Formula 1 przenosi sie z Las Vegas na tor Lusail przed przedostatnia runda sezonu w Katarze (27-29 listopada), gdzie obowiazywac bedzie klasyczny format weekendowy zakonczony 57-okrozeniowym wyscigiem w niedziele wieczorem.",
        "Max Verstappen przyjezdza po 75. zwyciestwie w karierze wywalczonym w Nevadzie po 35 zmianach prowadzenia o zaledwie 0,639 sekundy przed Lando Norrisem oraz Oscarem Piastrim startujacym z 17. pola.",
        "Mistrzowie Kimi Antonelli (402 pkt) i Mercedes (666) maja juz pewny tytul, lecz Walka o P3 miedzy Hamiltonem (267), Russellem (264) i Norrisem (264) oraz pojedynek Red Bulla (440) z McLarenem (431) trwaja."
      ]
    },
    "zh": {
      "title": "F1卡塔尔站前瞻：维斯塔潘挟75胜莅临卢赛尔，季军之争仅差3分",
      "subtitle": "历经拉斯维加斯35次领跑交替的史诗对决后，F1卡塔尔周末回归常规赛制并于周五揭幕。",
      "excerpt": "维斯塔潘在拉斯维加斯险胜诺里斯夺冠积304分，车手榜第三名汉密尔顿（267分）仅领先拉塞尔与诺里斯3分。",
      "body": [
        "世界一级方程式锦标赛移师卢赛尔国际赛道，第22站卡塔尔大奖赛将于11月27日至29日打响。本站回归包含三次自由练习赛、周六排位赛与周日57圈正赛的传统比赛周末安排，不设F1冲刺赛。",
        "红牛车手维斯塔潘刚刚在拉斯维加斯历经35次头名交替的激战，以0.639秒惊险击败诺里斯夺得生涯第75胜，迈凯伦车手皮亚斯特里则从第17位发车强势登上领奖台。",
        "尽管安东内利（402分）和梅赛德斯（666分）已提前夺冠，目前汉密尔顿（267分）与并列264分的拉塞尔、诺里斯仅差3分，车队榜迈凯伦（431分）也紧追红牛（440分）仅落后9分。"
      ]
    },
    "ja": {
      "title": "F1カタールGP展望：通算75勝のフェルスタッペンがルサイルへ、3位争いはわずか3点差",
      "subtitle": "35回の首位交代を演じたラスベガスの激闘を経て、第22戦カタールは伝統の通常フォーマットで開催。",
      "excerpt": "ラスベガスを制したフェルスタッペンが304点、3位のハミルトン（267点）とラッセル、ノリス（264点）が3点差で迫る。",
      "body": [
        "F1世界選手権第22戦カタールGPは11月27日から29日にかけてルサイル国際サーキットで開催される。今年のカタールはF1スプリントを含まない通常の3セッション構成となり、日曜現地19時に57周の決勝を迎える。",
        "前戦ラスベガスでは35回の首位交代劇の末にマックス・フェルスタッペンがランド・ノリスを0.639秒抑えてキャリア通算75勝目を飾り、17番手スタートのオスカー・ピアストリも3位表彰台へ駆け上がった。",
        "キミ・アントネッリ（402点）とメルセデス（666点）がすでに王座を決めた一方、ルイス・ハミルトン（267点）とラッセル、ノリス（264点）はわずか3点差、マクラーレン（431点）もレッドブル（440点）に9点差へ迫る。"
      ]
    },
    "ko": {
      "title": "F1 카타르 GP 프리뷰: 통산 75승 페르스타펜 루사일 입성, 3위 경쟁은 단 3점 차",
      "subtitle": "라스베이거스 35회 선두 교대 혈투를 뒤로하고 카타르 대회가 스핀트 없는 전통 주말 일정으로 돌아온다.",
      "excerpt": "라스베이거스에서 우승한 페르스타펜(304점)의 뒤로 해밀턴(267점)과 러셀, 노리스(264점)가 3점 차 접전을 벌인다.",
      "body": [
        "포뮬러 1 22라운드 카타르 그랑프리가 11월 27일부터 29일까지 루사일 인터내셔널 서킷에서 열린다. 이번 카타르 주말은 F1 스프린트 레이스 없이 3차례 연습주행과 토요일 예선, 일요일 57랩 결승의 정통 일정으로 치러진다.",
        "막스 페르스타펜은 지난 라스베이거스 야간 레이스에서 무려 35차례 선두가 바뀐 격전 끝에 랜도 노리스를 0.639초 차로 따돌리고 커리어 75승을 거뒀으며, 오스카 피아스트리도 17그리드에서 포디움에 올랐다.",
        "키미 안토넬리(402점)와 메르세데스(666점)가 조기 우승을 확정한 가운데, 루이스 해밀턴(267점)과 러셀, 노리스(이상 264점)가 단 3점 차, 맥라렌(431점) 역시 레드불(440점)을 9점 차로 추격 중이다."
      ]
    },
    "ar": {
      "title": "تقديم جائزة قطر الكبرى: فيرستابن يصل الى لوسيل بفوزه الـ75 وصراع المركز الثالث بفارق 3 نقاط",
      "subtitle": "بعد 35 تغييرا للصدارة في لاس فيغاس، تعود الفورمولا 1 الى الصيغة التقليدية في حلبة لوسيل.",
      "excerpt": "فيرستابن يرفع رصيده الى 304 نقاط بعد ليلة فيغاس بينما يفصل ثلاث نقاط فقط بين هاميلتون (267) وراسل ونوريس (264).",
      "body": [
        "تنتقل الفورمولا 1 من أضواء لاس فيغاس الى حلبة لوسيل الدولية لخوض الجولة 22 في قطر من 27 الى 29 نوفمبر، مع العودة الى نظام عطلة نهاية الأسبوع التقليدي بثلاث حصص تجارب وتأهيلي وسباق من 57 لفة يوم الأحد.",
        "يدخل ماكس فيرستابن السباق منتشيا بانتصاره الـ75 في مسيرته بعدما حسم سباق فيغاس بفارق 0.639 ثانية امام لاندو نوريس رغم 35 تبديلا للصدارة، مع صعود أوسكار بياستري ثالثا من المركز 17.",
        "ومع حسم كيمي أنتونيللي (402 نقطة) ومرسيدس (666) للقبين العالميين، تفصل ثلاث نقاط فقط لويس هاميلتون (267) عن راسل ونوريس (264)، فيما يلاحق مكلارين (431) ريد بول (440) بفارق 9 نقاط."
      ]
    }
  },
  "davis-cup-finals-bologna-italy-musetti-alcaraz-turin-glory-2026": {
    "fr": {
      "title": "Coupe Davis a Bologne : L'Italie mene face a la Coree du Sud apres le triomphe d'Alcaraz a Turin",
      "subtitle": "Lorenzo Musetti ecrase Seongchan Hong pour lancer les tenants du titre tandis que la Tchequie domine le Canada 2-0.",
      "excerpt": "L'Italie s'offre un depart 1-0 en quarts de finale a Bologne apres la semaine parfaite de Carlos Alcaraz a Turin (6-2, 7-6 face a Zverev).",
      "body": [
        "Le tennis mondial reste ancre en Italie du Nord cette semaine pour le Final 8 de la Coupe Davis a Bologne, quelques jours apres le sacre historique de Carlos Alcaraz aux Nitto ATP Finals de Turin.",
        "Dimanche a Turin, l'Espagnol de 23 ans a battu le numero 1 mondial Alexander Zverev 6-2, 7-6(7) en sauvant trois balles de set dans le tie-break, achevant un tournoi invaincu (5-0, 5,171 millions de dollars) pour devenir le quatrieme homme a remporter tous les Grands Chelems et le Masters.",
        "Desormais place aux nations a Bologne : apres la qualification de la Tchequie face au Canada (2-0), Lorenzo Musetti a balaye Seongchan Hong 6-0, 7-6(5) pour placer l'Italie a 1-0 contre la Coree du Sud avant Grande-Bretagne - Allemagne et Autriche - Espagne jeudi."
      ]
    },
    "es": {
      "title": "Copa Davis en Bolonia: Italia toma ventaja sobre Corea del Sur tras la corona invicta de Alcaraz",
      "subtitle": "Lorenzo Musetti vence 6-0, 7-6(5) a Seongchan Hong luego de que Chequia derrotara 2-0 a Canada.",
      "excerpt": "Los campeones defensores arrancan 1-0 en Bolonia dias despues de que Carlos Alcaraz levantara invicto su primer titulo de Maestro en Turin.",
      "body": [
        "El tenis masculino sigue centrado en el norte de Italia con la Final 8 de la Copa Davis en Bolonia, apenas dias despues de la apoteosica coronacion de Carlos Alcaraz en las Nitto ATP Finals de Turin.",
        "El domingo 22 de noviembre, Alcaraz vencio 6-2, 7-6(7) a Alexander Zverev tras levantar tres bolas de set en el desempate para completar un 5-0 perfecto (5,171 millones de dolares) y convertirse en el cuarto hombre con los cuatro Grand Slams y la Copa de Maestros.",
        "En Bolonia, Chequia selló el primer pase semifinal venciendo 2-0 a Canada (Machac sobre Draxl), y el miercoles Lorenzo Musetti arrollo 6-0, 7-6(5) a Seongchan Hong para dar el 1-0 a Italia antes de los cruces del jueves."
      ]
    },
    "de": {
      "title": "Davis Cup Bologna: Italien fuehrt gegen Suedkorea nach Alcaraz' ungeschlagenem Turin-Triumph",
      "subtitle": "Lorenzo Musetti besiegt Seongchan Hong glatt mit 6:0, 7:6(5), nachdem Tschechien Kanada 2:0 schlug.",
      "excerpt": "Titelverteidiger Italien geht im Viertelfinale von Bologna mit 1:0 in Fuehrung, kurz nachdem Carlos Alcaraz in Turin 5:0 den Gesamtsieg feierte.",
      "body": [
        "Das Welt-Tennis bleibt in Norditalien, wo das Final 8 des Davis Cups in Bologna steigt, wenige Tage nach der kroenenden Woche von Carlos Alcaraz bei den Nitto ATP Finals in Turin.",
        "Am Sonntag in Turin besiegte der 23-jaehrige Spanier den Weltranglistenersten Alexander Zverev mit 6:2, 7:6(7), wehrte drei Satzbaelle im Tiebreak ab und kassierte mit einer perfekten 5:0-Bilanz 5,171 Millionen Dollar als erst vierter Spieler mit allen Slams plus Saisonfinale.",
        "Beim Nationenturnier in Bologna zitterte niemand im Auftakteinzel: Nach Tschechiens 2:0 ueber Kanada fertigte Lorenzo Musetti Seongchan Hong 6:0, 7:6(5) fuer Italien ab, ehe am Donnerstag Grossbritannien gegen Deutschland antritt."
      ]
    },
    "it": {
      "title": "Coppa Davis a Bologna: Italia avanti sulla Corea del Sud dopo il trionfo imbattuto di Alcaraz a Torino",
      "subtitle": "Lorenzo Musetti batte Seongchan Hong 6-0, 7-6(5) dopo il successo per 2-0 della Repubblica Ceca sul Canada.",
      "excerpt": "Gli azzurri tre volte campioni in carica scattano sull'1-0 nei quarti alla SuperTennis Arena pochi giorni dopo lo storico sigillo di Alcaraz.",
      "body": [
        "Il grande tennis resta di casa nel Nord Italia per le Final 8 di Coppa Davis a BolognaFiere, all'indomani dell'indimenticabile settimana torinese firmata da Carlos Alcaraz alle Nitto ATP Finals.",
        "Domenica a Torino lo spagnolo ha superato Alexander Zverev 6-2, 7-6(7) annullando tre set point al tie-break (9-7), chiudendo imbattuto 5-0 (5,171 milioni di dollari) da quarto giocatore nella storia capace di vincere tutti gli Slam e le Finals.",
        "A Bologna la Repubblica Ceca ha aperto il tabellone battendo il Canada 2-0, mentre mercoledi Lorenzo Musetti ha piegato Seongchan Hong 6-0, 7-6(5) portando l'Italia sull'1-0 prima di Cobolli-Kwon e delle sfide di giovedi."
      ]
    },
    "pl": {
      "title": "Puchar Davisa w Bolonii: Wlosi prowadza z Korea Pld po triumfie bez porazki Alcaraza w Turynie",
      "subtitle": "Lorenzo Musetti pokonal Seongchana Honga 6:0, 7:6(5), wczesniej Czechy wyeliminowaly Kanade 2:0.",
      "excerpt": "Obroncy trofeum prowadza 1:0 w cwiercfinale w Bolonii kilka dni po tym, jak Carlos Alcaraz zdobyl pierwszy tytul Nitto ATP Finals.",
      "body": [
        "Tenisowa elita przeniosla sie z Turynu do Bolonii na turniej Final 8 Pucharu Davisa, zaledwie kilka dni po historycznym wystepie Carlosa Alcaraza w Nitto ATP Finals.",
        "W niedzielnym finale 22 listopada Alcaraz pokonal lidera rankingu Alexandra Zvereva 6:2, 7:6(7), broniac trzech pilek setowych w tie-breaku i zgarniajac 5,171 miliona dolarow jako czwarty tenisista w dziejach ze wszystkimi Szlemami i tytulem mistrza sezonu.",
        "W Bolonii Czechy ograly Kanade 2:0, a w srode Lorenzo Musetti rozbil Seongchana Honga 6:0, 7:6(5), dajac Wlochom prowadzenie 1:0 przed czwartkowymi meczami Wielka Brytania - Niemcy i Austria - Hiszpania."
      ]
    },
    "zh": {
      "title": "戴维斯杯博洛尼亚总决赛：卫冕冠军意大利领先韩国，阿尔卡拉斯刚在都灵全胜封王",
      "subtitle": "穆塞蒂直落两盘击败洪性成，此前捷克2比0淘汰加拿大率先晋级四强。",
      "excerpt": "博洛尼亚八强淘汰赛激战正酣，穆塞蒂为意大利先拔头筹；几天前阿尔卡拉斯刚直落两盘击败兹维列夫夺得年终首冠。",
      "body": [
        "网坛本周聚焦意大利北部博洛尼亚的戴维斯杯八强决赛，紧随卡洛斯·阿尔卡拉斯在都灵Nitto ATP年终总决赛上的历史性加冕之后登场。",
        "11月22日周日都灵决赛中，23岁的阿尔卡拉斯在第二盘抢七挽救三个盘点，以6比2、7比6(7)力克头号种子兹维列夫，五战全胜独揽517.1万美元最高奖金，成为史上第四位集齐四大满贯与年终总决赛的男子选手。",
        "转战博洛尼亚团体舞台，捷克周二2比0完胜加拿大率先晋级四强，周三洛伦佐·穆塞蒂6比0、7比6(5)力克洪性成助意大利1比0领先韩国，周四英国对德国以及奥地利对西班牙还将接连打响。"
      ]
    },
    "ja": {
      "title": "デビスカップ・ボローニャ：王者イタリアが韓国に先勝、直前のトリノではアルカラスが全勝V",
      "subtitle": "ムゼッティがホン・ソンチャンをストレートで下し先制点、チェコはカナダに2-0で完勝。",
      "excerpt": "ボローニャでのファイナル8準々決勝が開幕しイタリアが1-0と先行、トリノではアルカラスがズベレフを破り初の年間王者へ。",
      "body": [
        "男子テニスの舞台はトリノから同じくイタリア北部のボローニャへ移り、デビスカップ・ファイナル8のノックアウト決戦が展開されている。",
        "22日のNitto ATPファイナルズ決勝では、23歳のカルロス・アルカラスが世界1位アレクサンダー・ズベレフを6-2、7-6(7)で撃破。5戦全勝で最高賞金517万1000ドルを獲得し、4大大会すべてと年間最終戦を制した史上4人目の選手となった。",
        "ボローニャでは火曜日にチェコがカナダを2-0で下して準決勝一番乗りを決め、水曜日にはイタリアのロレンツォ・ムゼッティがホン・ソンチャンに6-0、7-6(5)で勝利して先制、木曜はイギリス対ドイツとオーストリア対スペインが行われる。"
      ]
    },
    "ko": {
      "title": "데이비스 컵 볼로냐 파이널: 이탈리아 한국전 리드, 알카라스는 토리노 무패 우승 위업",
      "subtitle": "로렌초 무세티가 홍성찬을 제압하며 디펜딩 챔피언에 1승 안겨, 체코는 캐나다에 2-0 완승.",
      "excerpt": "볼로냐 파이널 8 토너먼트에서 이탈리아가 먼저 승기를 잡은 가운데, 직전 토리노에서는 카를로스 알카라스가 5전 전승으로 생애 첫 파이널스 정상에 올랐다.",
      "body": [
        "세계 남자 테니스의 열기가 토리노 ATP 파이널스에 이어 이탈리아 북부 볼로냐에서 열리는 2026 데이비스 컵 파이널 8 토너먼트로 그대로 이어지고 있다.",
        "지난 일요일 토리노 결승에서는 카를로스 알카라스가 세계 1위 알렉산더 즈베레프를 상대로 2세트 타이브레이크 3개의 세트포인트를 막아내며 6-2, 7-6(7) 완승을 거뒀다. 무패 우승으로 517만 1천 달러를 수확하며 커리어 슈퍼 슬램에 파이널스까지 석권한 역대 네 번째 선수가 됐다.",
        "이어진 볼로냐 국가대항전에서는 체코가 캐나다를 2-0으로 꺾고 4강에 선착했고, 수요일 이탈리아의 무세티가 한국의 홍성찬을 6-0, 7-6(5)으로 제압하며 1-0 리드를 잡았다."
      ]
    },
    "ar": {
      "title": "كاس ديفيز في بولونيا: ايطاليا تتقدم على كوريا الجنوبية بعد تتويج الكاراز في تورينو",
      "subtitle": "لورينزو موسيتي يكتسح هونغ سونغ تشان 6-0 و7-6 ليمنح حامل اللقب التقدم بعد تاهل التشيك على حساب كندا.",
      "excerpt": "المتنافسون يدخلون ربع النهائي في بولونيا اياما بعد فوز كارلوس الكاراز بلقب نهائيات التنس دون هزيمة على حساب زفيريف.",
      "body": [
        "تواصل التنس العالمي حضوره في شمال ايطاليا هذا الاسبوع مع منافسات ربع نهائي كاس ديفيز في بولونيا، بعد ايام قليلة من التتويج التاريخي للاسباني كارلوس الكاراز في نهائيات تورينو.",
        "ففي نهائي الاحد تغلب الكاراز على المصنف اول الكسندر زفيريف بنتيجة 6-2 و7-6(7) بعدما انقذ ثلاث كرات لحسم المجموعة، محققا 5 انتصارات دون هزيمة وجائزة مالية قياسية قدرها 5.171 مليون دولار.",
        "وفي بولونيا حسمت التشيك بطاقة نصف النهائي بفوزها 2-0 على كندا، بينما تقدم لورينزو موسيتي لايطاليا على كوريا الجنوبية بالفوز 6-0 و7-6(5) قبل لقاءات الخميس بين بريطانيا والمانيا ثم النمسا واسبانيا."
      ]
    }
  },
  "golf-rsm-classic-penge-breakthrough-playoff-victory-sea-island-2026": {
    "fr": {
      "title": "Marco Penge remporte le playoff a quatre a Sea Island pour son premier titre PGA Tour",
      "subtitle": "L'Anglais gagne des le premier trou de mort subite lundi matin apres une egalite a -16 (266).",
      "excerpt": "Marco Penge domine Haotong Li, Michael Thorbjornsen et Max Greyserman en prolongation lundi a The RSM Classic.",
      "body": [
        "La saison FedExCup Fall 2026 s'est achevee dans le suspense lundi matin 23 novembre a Sea Island en Georgie, ou l'Anglais Marco Penge a remporte son tout premier titre PGA Tour au bout d'un playoff a quatre.",
        "Les intemperies du dimanche ont repousse la fin du tournoi au lundi pour la deuxieme semaine consecutive sur le circuit. Auteur d'un superbe 65 final, Penge a termine a -16 (266) a egalite avec le Chinois Haotong Li, l'Americain Michael Thorbjornsen et Max Greyserman.",
        "Revenu sur le 18e trou en mort subite, Penge a scelle la victoire des le premier trou supplementaire avec 1,332 million de dollars a la cle et son plein droit de jeu, avant le rendez-vous du Hero World Challenge de Tiger Woods du 3 au 6 decembre."
      ]
    },
    "es": {
      "title": "Marco Penge conquista el desempate a cuatro en Sea Island y estrena su palmares en el PGA Tour",
      "subtitle": "El ingles vence en el primer hoyo de muerte subita el lunes tras igualar a -16 (266) en el Seaside Course.",
      "excerpt": "Marco Penge supera en el playoff a Haotong Li, Michael Thorbjornsen y Max Greyserman para ganar The RSM Classic.",
      "body": [
        "La campana de otono del PGA Tour cerro con dramatismo la manana del lunes 23 de noviembre en Sea Island, Georgia, donde el ingles Marco Penge sobrevivio a un playoff de cuatro jugadores para ganar por primera vez en el circuito.",
        "La lluvia dominical volvio a llevar el desenlace al lunes. Con una ronda final de 65 golpes, Penge empato en 16 bajo par (266) junto al chino Haotong Li y los estadounidenses Michael Thorbjornsen y Max Greyserman.",
        "En el primer hoyo de desempate, Penge sello el triunfo, el cheque de 1,332 millones de dolares y su tarjeta asegurada antes del Hero World Challenge que organiza Tiger Woods del 3 al 6 de diciembre."
      ]
    },
    "de": {
      "title": "Marco Penge gewinnt Vierer-Playoff auf Sea Island fuer seinen ersten PGA-Tour-Triumph",
      "subtitle": "Der Englaender siegt gleich am ersten Extraloch am Montagmorgen nach Gleichstand bei 16 unter Par (266).",
      "excerpt": "Marco Penge setzt sich im Stechen von The RSM Classic gegen Haotong Li, Michael Thorbjornsen und Max Greyserman durch.",
      "body": [
        "Die FedExCup-Fall-Serie 2026 fand am Montagvormittag, 23. November, auf Sea Island ein dramatisches Ende: Der Englaender Marco Penge entschied das Vierer-Playoff bei The RSM Classic fuer seinen ersten PGA-Tour-Titel fuer sich.",
        "Wetterunterbrechungen hatten das Finale erneut auf Montag verschoben. Dank einer Schlussrunde von 65 Schlaegen schloss Penge bei 16 unter Par (266) punktgleich mit Haotong Li, Michael Thorbjornsen und Max Greyserman ab.",
        "Direkt am ersten Extraloch machte Penge den Sieg sowie 1,332 Millionen Dollar Preisgeld perfekt und sicherte sich damit seine Tour-Mitgliedschaft vor Tiger Woods' Hero World Challenge (3.-6. Dezember)."
      ]
    },
    "it": {
      "title": "Marco Penge trionfa nello spareggio a quattro di Sea Island per il primo titolo sul PGA Tour",
      "subtitle": "L'inglese conquista The RSM Classic gia alla prima buca di playoff lunedi mattina a quota -16 (266).",
      "excerpt": "Marco Penge batte Haotong Li, Michael Thorbjornsen e Max Greyserman nel finale posticipato al lunedi in Georgia.",
      "body": [
        "La stagione FedExCup Fall 2026 si e chiusa lunedi mattina 23 novembre a Sea Island, in Georgia, con il primo trionfo sul PGA Tour dell'inglese Marco Penge al termine di uno spareggio a quattro.",
        "Le condizioni meteo della domenica hanno portato la sfida al lunedi per la seconda settimana consecutiva. Grazie a un giro finale in 65 colpi, Penge ha chiuso le 72 buche a -16 (266) assieme a Haotong Li, Michael Thorbjornsen e Max Greyserman.",
        "Alla prima buca di playoff Penge ha risolto la contesa intascando 1,332 milioni di dollari e la carta PGA Tour, dando appuntamento all'Hero World Challenge di Tiger Woods dal 3 al 6 dicembre alle Bahamas."
      ]
    },
    "pl": {
      "title": "Marco Penge zwycieza w czteroosobowej dogrywce i siega po premierowy tytul PGA Tour na Sea Island",
      "subtitle": "Anglik wygrywa na pierwszym dodatkowym dolku w poniedzialek rano po remisie czolowki na poziomie -16 (266).",
      "excerpt": "Marco Penge wyprzedzil Haotonga Li, Michaela Thorbjornsena i Maxa Greysermana w emocjonujacym finale The RSM Classic.",
      "body": [
        "Jesienna seria PGA Tour zakonczyla sie wielkim dramatem w poniedzialek 23 listopada w Sea Island w Georgii, gdzie Anglik Marco Penge wygral czteroosobowa dogrywke o swoje pierwsze zwyciestwo w cyklu.",
        "Niedzielna pogoda wymusila dogranie turnieju w poniedzialek drugi tydzien z rzedu. Swietna runda finałowa 65 uderzen pozwolila Penge zakonczyc zawody na -16 (266), rowno z Haotongiem Li, Michaelem Thorbjornsenem i Maxem Greysermanem.",
        "Wracajac na dogrywke, Penge rozstrzygnal losy pucharu i czeku na 1,332 miliona dolarow juz na pierwszym dolku przed grudniowym Hero World Challenge Tigera Woodsa."
      ]
    },
    "zh": {
      "title": "RSM精英赛：马尔科·彭奇赢下四人加洞赛斩获个人美巡赛首冠",
      "subtitle": "因周末天气延期至周一完赛，英格兰球手彭奇在海岛球场凭借-16杆进入加洞并在首洞胜出。",
      "excerpt": "彭奇力压李昊桐、索比约恩森与格雷泽曼赢得生涯首座美巡赛冠军并收获133.2万美元奖金。",
      "body": [
        "2026年美巡赛联邦快递杯秋季赛于11月23日周一上午在佐治亚州海岛高尔夫俱乐部戏剧性收官，英格兰选手马尔科·彭奇在紧张的四人延长赛中胜出，夺得职业生涯首座美巡赛冠军。",
        "由于周日天气影响，比赛连续第二周延至周一决胜。彭奇在决赛轮表现强势，以总成绩低于标准杆16杆（266杆）与中国名将李昊桐以及美国选手索比约恩森、格雷泽曼并列进入加洞赛。",
        "在加洞赛第一个洞便抓鸟胜出后，彭奇赢得133.2万美元冠军支票并锁定美巡全卡。接下来高坛将在12月3日至6日迎来泰格·伍兹做东的英雄世界挑战赛。"
      ]
    },
    "ja": {
      "title": "RSMクラシック：マルコ・ペンジが4人プレーオフを制しPGAツアー初優勝を達成",
      "subtitle": "悪天候による月曜フィニッシュのサドンデス1ホール目で決着、通算16アンダー266で頂点へ。",
      "excerpt": "リ・ハオトンやマイケル・ソービョルンセンらとの4人のプレーオフを制したペンジが初タイトルと133万2000ドルを獲得。",
      "body": [
        "2026年PGAツアー秋季シリーズ最終戦は11月23日月曜日の午前、ジョージア州シーアイランドで英国のマルコ・ペンジが4人によるプレーオフを制し、待望のツアー初優勝を飾った。",
        "悪天候のため2週連続で月曜決着となったシーサイド・コースの最終日、ペンジは通算16アンダー（266）までスコアを伸ばし、中国の李昊桐、アメリカのマイケル・ソービョルンセン、マックス・グレイサーマンと並んで並走した。",
        "突入したサドンデス・プレーオフの1ホール目で決着をつけたペンジは、優勝賞金133万2000ドルとともにシード権を確定させ、12月3日から6日のヒーローワールドチャレンジへ弾みをつけた。"
      ]
    },
    "ko": {
      "title": "PGA 투어 RSM 클래식: 마르코 펜지, 4인 연장전 끝에 생애 첫 투어 우승",
      "subtitle": "기상 악화로 월요일로 연기된 최종 라운드 끝에 합계 16언더파 266타 동타 뒤 연장 첫 홀서 승부 갈라.",
      "excerpt": "영국의 마르코 펜지가 리하오퉁, 마이클 소르비욘센, 맥스 그레이저먼을 제치고 133만 2천 달러 우승 상금을 거머쥐었다.",
      "body": [
        "2026 시즌 PGA 투어 페덱스컵 가을 시리즈가 11월 23일 월요일 오전 조지아주 시아일랜드에서 영국의 마르코 펜지가 4인 연장전을 뚫고 생애 첫 투어 우승을 차지하며 화려하게 막을 내렸다.",
        "일요일 기상 악화로 2주 연속 월요일 순연 결승이 치러진 가운데, 펜지는 최종일 65타 맹타를 휘두르며 16언더파 266타로 중국의 리하오퉁, 마이클 소르비욘센, 맥스 그레이저먼과 연장전에 돌입했다.",
        "연장 첫 번째 홀에서 극적인 승리를 따낸 펜지는 133만 2천 달러의 우승 상금과 투어 카드를 손에 넣었으며, 다음 달 3일부터 타이거 우즈가 주최하는 히어로 월드 챌린지가 바하마에서 이어진다."
      ]
    },
    "ar": {
      "title": "جولة PGA: الانجليزي ماركو بينجي يحسم التمايز الرباعي في سي آيلاند ويحصد لقبه الاول",
      "subtitle": "تأجل الختام الى الاثنين بسبب الطقس وحقق بينجي الفوز من الحفرة الفاصلة الاولى عند -16 (266).",
      "excerpt": "ماركو بينجي يتفوق على لي هاوتونغ ومايكل ثوربيورنسن وماكس غريزرمان لينال 1.332 مليون دولار.",
      "body": [
        "اختتمت سلسلة خريف PGA 2026 صباح الاثنين 23 نوفمبر في جزيرة سي آيلاند بولاية جورجيا بتتويج الانجليزي ماركو بينجي بلقبه الاحترافي الاول في الجولة عقب فوز دراماتيكي في تمايز رباعي.",
        "واجبر الطقس البطولة على الامتداد ليوم الاثنين للاسبوع الثاني تواليا، حيث سجل بينجي رصيدا نهائيا 16 ضربة تحت المعدل (266) متعادلا مع الصيني لي هاوتونغ والامريكيين ثوربيورنسن وغريزرمان.",
        "وحسم بينجي اللقب من الحفرة الاضافية الاولى ليظفر بـ 1.332 مليون دولار ويضمن بطاقته الكاملة قبل تحدي تايغر وودز العالمي بين 3 و6 ديسمبر في البهاماس."
      ]
    }
  },
  "nba-thanksgiving-holiday-break-celtics-pistons-cup-showdowns-2026": {
    "fr": {
      "title": "Pause de Thanksgiving NBA : Tatum claque 41 points, Cooper Flagg enchaine pour Dallas",
      "subtitle": "Jayson Tatum et Paul George cumulent 69 points face a Washington pendant que les Mavericks dominent Denver 120-101.",
      "excerpt": "Boston bat Washington 131-116 et Dallas surprend Denver 120-101 avec 24 points et 12 passes de Cooper Flagg avant le repos de jeudi.",
      "body": [
        "La NBA marque sa pause traditionnelle de Thanksgiving jeudi 26 novembre apres une semaine spectaculaire d'Emirates NBA Cup marquee par les offensives de Boston et Dallas mardi soir.",
        "A Washington, Jayson Tatum (41 points, 8 passes) et Paul George (28 points, 6/9 a trois points) ont porte les Celtics a 80 points a la pause vers un succes 131-116 malgre les 33 points et 13 rebonds d'Anthony Davis et les 20 points, 11 rebonds et 7 passes d'AJ Dybantsa.",
        "Dans le meme temps a Denver, Cooper Flagg a compile 24 points, 6 rebonds et 12 passes pour offrir aux Mavericks une victoire nette 120-101 face a Nikola Jokic (18/11), tandis que Detroit sans Cade Cunningham battait Orlando 104-86."
      ]
    },
    "es": {
      "title": "Pausa de Accion de Gracias en la NBA: Tatum anota 41 puntos y Cooper Flagg guia a los Mavericks",
      "subtitle": "Tatum y Paul George suman 69 tantos ante los Wizards mientras Dallas supera 120-101 a Denver en la Copa NBA.",
      "excerpt": "Boston vence 131-116 a Washington y Dallas domina 120-101 a los Nuggets con 24 puntos y 12 asistencias de Cooper Flagg antes del descanso.",
      "body": [
        "La NBA descansa el jueves 26 de noviembre por Accion de Gracias tras una intensa jornada de Emirates NBA Cup que dejo grandes exhibiciones el martes.",
        "En la capital, Boston anoto 80 puntos en la primera mitad rumbo a un 131-116 sobre Washington comandado por Jayson Tatum (41 puntos, 8 asistencias) y Paul George (28 puntos, 6 triples), superando los 33 puntos y 13 rebotes de Anthony Davis.",
        "Ademas en Denver, Cooper Flagg brilló con 24 puntos y 12 asistencias para llevar a Dallas al 120-101 sobre los Nuggets de Nikola Jokic (18 puntos, 11 rebotes), mientras Detroit sin Cade Cunningham vencia 104-86 a Orlando con 21 puntos de Isaiah Joe."
      ]
    },
    "de": {
      "title": "NBA Thanksgiving-Pause: Tatum erzielt 41 Punkte fuer Boston und Cooper Flagg fuehrt Dallas an",
      "subtitle": "Tatum und Paul George schenken Washington 69 Punkte ein, waehrend die Mavericks Denver mit 120:101 abfertigen.",
      "excerpt": "Vor dem spielfreien Donnerstag glaenzen die Celtics beim 131:116 ueber die Wizards und Dallas schlaegt Nikola Jokics Nuggets dank Cooper Flagg.",
      "body": [
        "Am Donnerstag, 26. November, legt die NBA ihre traditionelle Thanksgiving-Spielpause ein, nachdem zuvor im Emirates NBA Cup am Dienstag spektakulare Resultate gefallen waren.",
        "Boston erzielte schon zur Halbzeit 80 Punkte gegen Washington und siegte 131:116 dank Jayson Tatum (41 Punkte, 8 Assists) und Paul George (28 Punkte), obgleich Anthony Davis 33 Punkte und 13 Rebounds fuer die Wizards holte.",
        "In Denver glaenzte Cooper Flagg mit 24 Punkten und 12 Assists beim 120:101-Auswaertssieg der Mavericks gegen Nikola Jokic (18/11), waehrend Detroit auch ohne den verletzten Cade Cunningham durch Isaiah Joes 21 Punkte 104:86 in Orlando gewann."
      ]
    },
    "it": {
      "title": "Pausa del Ringraziamento NBA: Tatum esplode a quota 41 e Cooper Flagg trascina Dallas a Denver",
      "subtitle": "Jayson Tatum e Paul George firmano 69 punti contro Washington mentre i Mavericks travolgono i Nuggets 120-101.",
      "excerpt": "Boston regola i Wizards 131-116 e Dallas espugna Denver 120-101 con 24 punti e 12 assist di Cooper Flagg prima dello stop di giovedi.",
      "body": [
        "La NBA osserva il tradizionale turno di riposo del Ringraziamento giovedi 26 novembre dopo le spettacolari sfide di Emirates NBA Cup disputate in settimana.",
        "Nella capitale Boston ha segnato 80 punti gia all'intervallo imponendosi 131-116 con 41 punti e 8 assist di Jayson Tatum e 28 punti di Paul George, rendendo vani i 33 punti e 13 rimbalzi di Anthony Davis per Washington.",
        "A Denver invece Cooper Flagg ha brillato con 24 punti, 6 rimbalzi e 12 assist guidando i Mavericks al 120-101 sui Nuggets di Nikola Jokic, mentre i Pistons privi di Cade Cunningham hanno battuto Orlando 104-86 con 21 punti di Isaiah Joe."
      ]
    },
    "pl": {
      "title": "Swiateczna przerwa w NBA: 41 punktow Tatuma i wielki wystep Coopera Flagga dla Dallas",
      "subtitle": "Tatum i Paul George zdobyli 69 punktow w Waszyngtonie, a Mavericks rozbili Denver 120:101 przed czwartkowa pauza.",
      "excerpt": "Celtics ograli Wizards 131:116, a Dallas rozgromilo Nuggets 120:101 po 24 punktach i 12 asystach Coopera Flagga.",
      "body": [
        "W czwartek 26 listopada cala liga NBA pauzuje z okazji Swieta Dziekczynienia po ekscytujacych meczach fazy grupowej Emirates NBA Cup we wtorek i srode.",
        "W Waszyngtonie koszykarze Boston Celtics rzucili 80 punktow do przerwy i wygrali 131:116 dzieki 41 punktom i 8 asystom Jaysona Tatuma oraz 28 punktom Paula George'a, mimo ze Anthony Davis zanotowal 33 punkty i 13 zbiorek.",
        "W Denver Cooper Flagg zapisal na koncie 24 punkty, 6 zbiorek i 12 asyst, prowadzac Dallas Mavericks do triumfu 120:101 nad ekipa Nikoli Jokicia, a osłabieni Pistons bez Cade'a Cunninghama wygrali w Orlando 104:86."
      ]
    },
    "zh": {
      "title": "NBA感恩节休战：塔图姆狂轰41分，库珀·弗拉格率独行侠客场大胜掘金",
      "subtitle": "塔图姆与保罗·乔治联手砍下69分击败奇才，独行侠120-101力克约基奇的掘金。",
      "excerpt": "NBA周四进入全联盟感恩节休战日，此前周二凯尔特人131-116击退奇才，弗拉格24分12助攻闪耀丹佛。",
      "body": [
        "周四11月26日感恩节期间NBA全联盟照例休战一天，此前周二与周三多场阿联酋NBA杯小组赛已将对抗气氛推向顶点。",
        "周二夜在华盛顿，凯尔特人上半场爆砍80分以131比116大胜奇才。杰森·塔图姆独得41分6篮板8助攻，保罗·乔治三分9投6中拿下28分9助攻，化解了安东尼·戴维斯空砍33分13篮板及阿杰·迪班萨20分11篮板7助攻的反扑。",
        "同日在丹佛，库珀·弗拉格交出24分6篮板12助攻的全面数据，助独行侠120比101轻取掘金；缺少康宁汉姆的活塞则凭借以赛亚·乔的21分在奥兰多104比86获胜。"
      ]
    },
    "ja": {
      "title": "NBA感謝祭ブレイク：テイタム41得点、クーパー・フラッグ躍動でマーベリックス快勝",
      "subtitle": "テイタムとポール・ジョージの計69得点でボストンがウィザーズを撃破、ダラスはデンバーを120-101で下す。",
      "excerpt": "木曜日の感謝祭全休前、エミレーツNBAカップでセルティックスが131-116、マーベリックスがフラッグの24点12アシストで勝利。",
      "body": [
        "11月26日木曜日の感謝祭を迎えNBAはリーグ全体が休養日に入る。その直前、火曜・水曜のエミレーツNBAカップでは各チームが熾烈な攻防を繰り広げた。",
        "ワシントンではボストン・セルティックスが前半だけで80得点を奪い131-116で快勝。ジェイソン・テイタムが41得点8アシスト、ポール・ジョージが6本の3点シュートを含む28得点9アシストを挙げ、アンソニー・デイビスの33得点13リバウンドを退けた。",
        "一方デンバーでは、クーパー・フラッグが24得点6リバウンド12アシストと躍動しダラスがナゲッツを120-101で撃破。ケイド・カニングハム欠場のピストンズもアイザイア・ジョーの21得点などでマジックに104-86で勝利した。"
      ]
    },
    "ko": {
      "title": "NBA 추수감사절 휴식기: 테이텀 41점 폭발, 쿠퍼 플래그 12어시스트 댈러스 대승",
      "subtitle": "제이슨 테이텀과 폴 조지가 69점을 합작하며 위저즈를 꺾었고, 댈러스는 덴버를 120-101로 제압했다.",
      "excerpt": "목요일 추수감사절 전 구단 휴식을 앞두고 보스턴이 131-116 승리를 거뒀으며 댈러스는 쿠퍼 플래그의 활약으로 덴버 원정을 챙겼다.",
      "body": [
        "11월 26일 목요일 추수감사절을 맞아 NBA가 전통적인 휴식일을 보내는 가운데, 직전 화요일 에미레이츠 NBA 컵에서는 폭발적인 득점전이 이어졌다.",
        "워싱턴 원정에서 보스턴 셀틱스는 전반에만 80점을 몰아친 끝에 131-116 완승을 거뒀다. 제이슨 테이텀이 41점 8어시스트, 폴 조지가 3점슛 6개 포함 28점 9어시스트로 앤서니 데이비스(33점 13리바운드)와 AJ 디반사(20점 11리바운드)의 추격을 따돌렸다.",
        "덴버에서는 쿠퍼 플래그가 24점 6리바운드 12어시스트로 맹활약하며 댈러스의 120-101 대승을 이끌었고, 케이드 커닝햄이 결장한 디트로이트도 올랜도를 104-86으로 제압했다."
      ]
    },
    "ar": {
      "title": "عطلة عيد الشكر في NBA: تايتوم ينفجر بـ41 نقطة وكوبر فلاغ يقود دالاس لفوز كبير",
      "subtitle": "جايسون تايتوم وبول جورج يسجلان 69 نقطة في واشنطن بينما دالاس يسحق دنفر 120-101 في كاس الدوري.",
      "excerpt": "بوسطن يتخطى واشنطن 131-116 ومافريكس يهزم ناغتس بفضل 24 نقطة و12 تمريرة من كوبر فلاغ قبل استراحة الخميس.",
      "body": [
        "تاخذ رابطة NBA استراحتها التقليدية بمناسبة عيد الشكر يوم الخميس 26 نوفمبر بعد مواجهات مثيرة في كاس الامارات للدوري ليلة الثلاثاء والاربعاء.",
        "في واشنطن سجل بوسطن سيلتيكس 80 نقطة في الشوط الاول ليحسم اللقاء 131-116 بقيادة جايسون تايتوم (41 نقطة و8 تمريرات) وبول جورج (28 نقطة)، رغم تالق انطوني ديفيس بـ33 نقطة و13 متابعة.",
        "وفي دنفر تالق كوبر فلاغ مسجلا 24 نقطة و12 تمريرة حاسمة ليقود دالاس مافريكس للفوز 120-101 على نيكولا يوكيتش ورفاقه، فيما تغلب ديترويت بيستونز رغم غياب كيد كانينغهام على اورلاندو 104-86."
      ]
    }
  }
}

with open(STORIES_TS, "r", encoding="utf-8") as f:
    src = f.read()

marker = "export const STORY_I18N: Record<string, LocMap> = {"
if marker not in src:
    raise RuntimeError("Could not find STORY_I18N anchor")

chunks = []
for slug, locmap in translations.items():
    if f'"{slug}":' in src:
        raise RuntimeError(f"Slug {slug} already in stories.ts")
    block = json.dumps(locmap, ensure_ascii=False, indent=2)
    # indent inside object by 2 spaces
    indented = "\n".join("  " + line if i > 0 else line for i, line in enumerate(block.splitlines()))
    chunks.append(f'  "{slug}": {indented},')

injected = "\n".join(chunks)
for chk in [injected]:
    if "\u2014" in chk or "--" in chk:
        raise ValueError("Em-dash or double-hyphen detected in stories translations!")

new_src = src.replace(marker, marker + "\n" + injected, 1)
with open(STORIES_TS, "w", encoding="utf-8") as f:
    f.write(new_src)
print(f"Injected {len(translations)} story translations (x9 locales = {len(translations)*9} blocks) into stories.ts")
