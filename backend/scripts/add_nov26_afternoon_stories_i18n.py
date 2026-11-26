# Insert/replace STORY_I18N for afternoon 26 Nov stories.
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PATH = os.path.join(ROOT, "frontend", "src", "i18n", "stories.ts")


def no_dashes(blob, label):
    if "\u2014" in blob:
        raise SystemExit(f"emdash in {label}")
    if "--" in blob.replace("---", ""):
        raise SystemExit(f"double hyphen in {label}")


def loc(title, subtitle, excerpt, p1, p2, p3):
    return {
        "title": title,
        "subtitle": subtitle,
        "excerpt": excerpt,
        "body": [p1, p2, p3],
    }


NEW = {
    "rams-packers-thanksgiving-eve-week12-2026": {
        "fr": loc(
            "Thanksgiving Eve : Corum (184 yards) offre le 26-13 aux Rams contre Green Bay",
            "Los Angeles gagne une cinquieme fois de suite et passe a 7-4, Green Bay tombe a 6-5 apres une deuxieme periode blanche.",
            "Blake Corum a porte 32 fois pour 184 yards et un TD, et les Rams ont battu les Packers 26-13 pour le premier Thanksgiving Eve de la NFL.",
            "La NFL a ouvert la semaine de Thanksgiving mercredi 25 novembre avec un premier match du mercredi soir sur Netflix, et les Los Angeles Rams ont battu les Green Bay Packers 26-13 au SoFi Stadium.",
            "Blake Corum, le jour de ses 26 ans, a porte 32 fois pour 184 yards et un TD d un yard, dont 161 yards apres la pause. Kyren Williams a ajoute une course de 7 yards. Brandon McManus a inscrit quatre field goals de 43, 41, 40 et 30 yards. Les Rams ont couru 241 yards et garde le ballon 40:40 contre 19:20.",
            "Stafford : 16/23, 140 yards, 1 INT. Love : 17/29, 198 yards, 1 TD, 2 INT. Christian Watson (4-65-1) est sorti sur commotion apres un plaquage casque en avant de Kam Kinchens, expulse. Los Angeles est 7-4, Green Bay 6-5. Le triple-header du jeudi reste inedit.",
        ),
        "es": loc(
            "Vispera de Accion de Gracias: Corum (184 yardas) da el 26-13 a los Rams ante Packers",
            "Los Angeles encadena un quinto triunfo y pasa a 7-4; Green Bay cae a 6-5 tras un segundo tiempo en blanco.",
            "Blake Corum corrio 32 veces para 184 yardas y un TD, y los Rams ganaron 26-13 en el primer Thanksgiving Eve de la NFL.",
            "La NFL abrio la semana de Accion de Gracias el miercoles 25 de noviembre con su primer partido de vispera en Netflix, y los Rams vencieron 26-13 a los Packers en SoFi Stadium.",
            "Corum, en su 26 cumpleanos, acumulo 32 acarreos, 184 yardas y un TD de 1 yarda, 161 de ellas en la segunda mitad. Kyren Williams anoto de 7. McManus pateo cuatro goles de campo (43, 41, 40 y 30). Los Rams corrieron 241 yardas y tuvieron el balon 40:40 a 19:20.",
            "Stafford 16/23, 140 y 1 INT. Love 17/29, 198, 1 TD y 2 INT. Watson (4-65-1) salio por concussion tras un golpe de Kinchens, expulsado. Los Angeles 7-4, Green Bay 6-5. El tripleheader del jueves sigue inedito.",
        ),
        "de": loc(
            "Thanksgiving Eve: Corum mit 184 Yards, Rams schlagen Packers 26:13",
            "Los Angeles gewinnt zum fuenften Mal in Folge und steht 7-4, Green Bay faellt auf 6-5 nach einer torlosen zweiten Haelfte.",
            "Blake Corum lief 32 Mal fuer 184 Yards und einen TD, die Rams siegten 26:13 im ersten Thanksgiving-Eve-Spiel der NFL.",
            "Die NFL eroeffnete die Thanksgiving-Woche am Mittwoch, 25. November, mit dem ersten Eve-Spiel auf Netflix. Die Los Angeles Rams bezwangen die Green Bay Packers 26:13 im SoFi Stadium.",
            "Corum trug 32 Mal fuer 184 Yards und einen 1-Yard-TD, davon 161 Yards nach der Pause. Kyren Williams erlief 7 Yards zum TD. McManus traf vier Field Goals (43, 41, 40, 30). Die Rams kamen auf 241 Laufyards und 40:40 Ballbesitz gegen 19:20.",
            "Stafford 16/23, 140, 1 INT. Love 17/29, 198, 1 TD, 2 INT. Watson (4-65-1) ging mit Gehirnerschuetterung vom Feld, Kinchens flog. Los Angeles 7-4, Green Bay 6-5. Das Donnerstags-Tripleheader bleibt unveröffentlicht.",
        ),
        "it": loc(
            "Thanksgiving Eve: Corum (184 yard) trascina i Rams sul 26-13 ai Packers",
            "Los Angeles vince la quinta di fila e sale a 7-4, Green Bay scende a 6-5 dopo un secondo tempo a zero.",
            "Blake Corum ha portato 32 volte per 184 yard e un TD: i Rams hanno battuto i Packers 26-13 nel primo Thanksgiving Eve NFL.",
            "La NFL ha aperto la settimana del Ringraziamento mercoledi 25 novembre con il primo Eve game su Netflix, e i Rams hanno battuto i Packers 26-13 al SoFi Stadium.",
            "Corum, nel giorno del 26esimo compleanno, 32 portate, 184 yard e un TD da 1 yarda, di cui 161 dopo l intervallo. Williams ha corso 7 yard in meta. McManus quattro field goal da 43, 41, 40 e 30. I Rams 241 yard su corsa e possesso 40:40 a 19:20.",
            "Stafford 16/23, 140, 1 INT. Love 17/29, 198, 1 TD, 2 INT. Watson (4-65-1) esce per concussione dopo il placcaggio di Kinchens, espulso. Los Angeles 7-4, Green Bay 6-5. Il tripleheader di giovedi resta inedito.",
        ),
        "pl": loc(
            "Thanksgiving Eve: Corum (184 jardy) daje Rams 26:13 z Packers",
            "Los Angeles wygrywa piata z rzedu i ma 7-4, Green Bay spada do 6-5 po bezbramkowej drugiej polowie.",
            "Blake Corum mial 32 niesienia, 184 jardy i przylozenie. Rams pokonali Packers 26:13 w pierwszym Thanksgiving Eve NFL.",
            "NFL otworzyla tydzien Swieta Dziekczynienia w srode 25 listopada pierwszym meczem Wednesday Eve na Netflixie. Rams wygrali 26:13 z Packers na SoFi Stadium.",
            "Corum w 26. urodziny: 32 niesienia, 184 jardy i TD z 1 jarda, w tym 161 po przerwie. Williams TD z 7 jardow. McManus cztery FG (43, 41, 40, 30). Rams 241 jardow biegiem i posiadanie 40:40 do 19:20.",
            "Stafford 16/23, 140, 1 INT. Love 17/29, 198, 1 TD, 2 INT. Watson (4-65-1) z wstrzasnieniem po uderzeniu Kinchensa (czerwona). Los Angeles 7-4, Green Bay 6-5. Czwartkowy tripleheader pozostaje nieopublikowany.",
        ),
        "zh": loc(
            "感恩节前夜：科勒姆184码冲球，公羊26-13击败包装工",
            "洛杉矶豪取五连胜升至7胜4负，绿湾下半场颗粒无收跌至6胜5负。",
            "布莱克·科勒姆32次持球184码并达阵，公羊在NFL首次感恩节前夜大战中26-13取胜。",
            "NFL于11月25日周三在网飞推出首次感恩节前夜赛，洛杉矶公羊在SoFi球场26-13击败绿湾包装工。",
            "科勒姆26岁生日当天32次持球184码、1码达阵，下半场独揽161码。凯伦·威廉姆斯7码达阵。麦克马纳斯踢进43、41、40、30码四个任意球。公羊冲球241码，控球40分40秒对19分20秒。",
            "斯塔福德16/23、140码、1抄截。洛夫17/29、198码、1达阵2抄截。沃森（4接65码达阵）因金琴斯头盔撞击脑震荡离场，金琴斯被罚下。公羊7-4，包装工6-5。周四三连战仍未公布完场。",
        ),
        "ja": loc(
            "感謝祭前夜：コーラム184ヤード、ラムズがパッカーズに26-13",
            "ロサンゼルスは5連勝で7勝4敗、グリーンベイは後半無得点で6勝5敗。",
            "ブレイク・コーラムが32回184ヤード1TD。NFL初の感謝祭前夜戦でラムズが26-13勝利。",
            "NFLは11月25日水曜、Netflixで初のThanksgiving Eveを開催し、ラムズがSoFiスタジアムでパッカーズに26-13で勝った。",
            "26歳の誕生日を迎えたコーラムは32回184ヤード、1ヤードTD（後半161ヤード）。カイレン・ウィリアムズが7ヤードTD。マクマナスは43、41、40、30ヤードの4FG。ラン241ヤード、ボール保持40:40対19:20。",
            "スタッフォード16/23、140ヤード、1INT。ラブ17/29、198、1TD、2INT。ワトソン（4-65-1）はキンチェンズのヘルメットヒットで脳震盪、キンチェンズ退場。LAR 7-4、GB 6-5。木曜三重戦は未公開。",
        ),
        "ko": loc(
            "추수감사절 전야: 코럼 184야드, 램스가 패커스를 26-13으로 제압",
            "로스앤젤레스 5연승으로 7-4, 그린베이는 후반 무득점으로 6-5.",
            "블레이크 코럼이 32회 184야드 1TD. NFL 첫 추수감사절 전야전에서 램스가 26-13 승리.",
            "NFL은 11월 25일 수요일 넷플릭스에서 첫 Thanksgiving Eve를 열었고, 램스가 소파이 스타디움에서 패커스를 26-13으로 꺾었다.",
            "26번째 생일을 맞은 코럼은 32회 184야드, 1야드 TD(후반 161야드). 카이렌 윌리엄스 7야드 TD. 맥매너스는 43, 41, 40, 30야드 필드골 4개. 런 241야드, 점유 40:40 대 19:20.",
            "스태퍼드 16/23, 140야드, 1INT. 러브 17/29, 198, 1TD 2INT. 왓슨(4-65-1)은 킨첸스의 헬멧 히트로 뇌진탕, 킨첸스 퇴장. LAR 7-4, GB 6-5. 목요일 3연전은 미공개.",
        ),
        "ar": loc(
            "عشية عيد الشكر: كوروم 184 ياردة يقود رامز للفوز 26-13 على باكرز",
            "لوس انجلوس يحقق خامس فوز متتال ويصبح 7-4، غرين باي يسقط الى 6-5 بعد شوط ثان بلا نقاط.",
            "بليك كوروم ركض 32 مرة لـ184 ياردة وتاتش داون، ورامز فاز 26-13 في اول عشية عيد شكر في NFL.",
            "افتتح NFL اسبوع عيد الشكر الاربعاء 25 نوفمبر باول مباراة عشية على نتفليكس، وفاز رامز 26-13 على باكرز في استاد سوفاي.",
            "كوروم في عيد ميلاده الـ26: 32 حملة و184 ياردة وتاتش داون من ياردة، منها 161 بعد الاستراحة. كايرن ويليامز سجل من 7 ياردات. مكمانوس اربع ركلات (43 و41 و40 و30). رامز ركض 241 ياردة واستحوذ 40:40 مقابل 19:20.",
            "ستافورد 16/23 و140 ياردة وتقاطع. لوف 17/29 و198 وتاتش داون وتقاطعان. واتسون (4-65-1) خرج بارتجاج بعد تدخل كينشنز الذي طرد. رامز 7-4 وباكرز 6-5. ثلاثية الخميس غير منشورة.",
        ),
    },
    "champions-league-md5-wednesday-barcelona-liverpool-2026": {
        "fr": loc(
            "Ligue des champions mercredi : Barcelone 4-1 a Sabah, Liverpool 3-0 a Bruges",
            "Gordon double a Bakou et Isak guide Liverpool a 12 points, le Real Madrid reste premier a 15 apres le 5-1 contre le PSV.",
            "Anthony Gordon a marque aux 31e et 51e, Barcelone a battu Sabah 4-1. Liverpool a gagne 3-0 a Bruges par Isak et Wirtz.",
            "La 5e journee de Ligue des champions s est achevee mercredi 25 novembre avec des victoires de Barcelone et de Liverpool dans la course au top 8 automatique.",
            "A Bakou, Gordon a marque aux 31e et 51e, Adeyemi a 55e, Jesus a 60e, Mickels a 63e. Flick, sans Yamal, signe une 4e victoire en 5 et 12 points. Gordon homme du match.",
            "Liverpool a gagne 3-0 a Bruges : Isak a 13e puis un dribble tardif, Wirtz a 79e. Apres 5 journees le Real reste 1er a 15 (5-1 mardi, Bellingham 59). PSG 13, Barca et Liverpool 12. PL : Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        ),
        "es": loc(
            "Champions el miercoles: Barcelona 4-1 en Sabah, Liverpool 3-0 en Brujas",
            "Gordon marca dos en Baku e Isak lleva a Liverpool a 12 puntos; el Madrid sigue primero con 15 tras el 5-1 al PSV.",
            "Anthony Gordon anoto en el 31 y el 51, Barcelona gano 4-1. Liverpool vencio 3-0 en Brujas con Isak y Wirtz.",
            "La jornada 5 de Champions cerro el miercoles 25 de noviembre con victorias de Barcelona y Liverpool en la pelea por el top 8.",
            "En Baku, Gordon 31 y 51, Adeyemi 55, Jesus 60, Mickels 63. Flick, sin Yamal, suma un cuarto triunfo en cinco y 12 puntos. Gordon, mejor del partido.",
            "Liverpool 3-0 en Brujas: Isak al 13 y un globo tardio, Wirtz al 79. Tras cinco jornadas el Madrid sigue 1o con 15 (5-1 el martes, Bellingham 59). PSG 13, Barca y Liverpool 12. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        ),
        "de": loc(
            "Champions League Mittwoch: Barcelona 4:1 in Sabah, Liverpool 3:0 in Bruegge",
            "Gordon trifft doppelt in Baku, Isak fuehrt Liverpool auf 12 Punkte, Real bleibt mit 15 Erster nach dem 5:1 gegen PSV.",
            "Anthony Gordon traf in der 31. und 51., Barcelona siegte 4:1. Liverpool gewann 3:0 in Bruegge durch Isak und Wirtz.",
            "Der 5. Spieltag der Champions League endete am Mittwoch, 25. November, mit Siegen von Barcelona und Liverpool im Kampf um die Top 8.",
            "In Baku: Gordon 31 und 51, Adeyemi 55, Jesus 60, Mickels 63. Flick ohne Yamal holt den vierten Sieg aus fuenf und 12 Punkte. Gordon Spieler des Spiels.",
            "Liverpool 3:0 in Bruegge: Isak 13 und spaeter ein Chip, Wirtz 79. Nach fuenf Spielen bleibt Real mit 15 Erster (5:1 Dienstag, Bellingham 59). PSG 13, Barca und Liverpool 12. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        ),
        "it": loc(
            "Champions mercoledi: Barcellona 4-1 a Sabah, Liverpool 3-0 a Bruges",
            "Gordon doppietta a Baku e Isak porta il Liverpool a 12 punti; il Real resta primo a 15 dopo il 5-1 al PSV.",
            "Anthony Gordon ha segnato al 31 e al 51, il Barcellona ha vinto 4-1. Il Liverpool ha battuto il Club Brugge 3-0 con Isak e Wirtz.",
            "La 5a giornata di Champions si e chiusa mercoledi 25 novembre con i successi di Barcellona e Liverpool nella corsa al top 8.",
            "A Baku Gordon 31 e 51, Adeyemi 55, Jesus 60, Mickels 63. Flick senza Yamal firma la quarta vittoria su cinque e 12 punti. Gordon uomo partita.",
            "Liverpool 3-0 a Bruges: Isak al 13 e un pallonetto a fine gara, Wirtz al 79. Dopo cinque turni il Real resta 1o a 15 (5-1 martedi, Bellingham 59). PSG 13, Barca e Liverpool 12. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        ),
        "pl": loc(
            "Liga Mistrzow w srode: Barcelona 4:1 w Sabah, Liverpool 3:0 w Brugii",
            "Gordon dwa gole w Baku, Isak daje Liverpoolowi 12 pkt, Real zostaje pierwszy z 15 po 5:1 z PSV.",
            "Anthony Gordon strzelil w 31. i 51., Barcelona wygrala 4:1. Liverpool pokonal Club Brugge 3:0 po golach Isaka i Wirtza.",
            "5. kolejka Ligi Mistrzow zamknela sie w srode 25 listopada zwyciestwami Barcelony i Liverpoolu w walce o czołowa osmke.",
            "W Baku Gordon 31 i 51, Adeyemi 55, Jesus 60, Mickels 63. Flick bez Yamala ma czwarte zwyciestwo z pieciu i 12 pkt. Gordon zawodnikiem meczu.",
            "Liverpool 3:0 w Brugii: Isak 13 i pozny chip, Wirtz 79. Po pieciu kolejkach Real pierwszy z 15 (5:1 we wtorek, Bellingham 59). PSG 13, Barca i Liverpool 12. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        ),
        "zh": loc(
            "欧冠周三：巴萨客场4-1萨巴赫，利物浦3-0布鲁日",
            "戈登巴库梅开二度，伊萨克带利物浦升至12分，皇马5-1埃因霍温后仍以15分领跑。",
            "安东尼·戈登31、51分钟破门，巴萨4-1取胜。利物浦凭伊萨克与维尔茨3-0布鲁日。",
            "欧冠联赛阶段第5轮于11月25日周三收官，巴萨与利物浦双双取胜，继续争夺自动晋级前八。",
            "巴库：戈登31、51，阿德耶米55，热苏斯60，米克尔斯63。弗利克轮换无亚马尔，五战四胜积12分。戈登当选最佳。",
            "利物浦客场3-0布鲁日：伊萨克13分钟及补时前吊射，维尔茨79分钟。五轮后皇马仍以15分领跑（周二5-1，贝林厄姆59）。巴黎13，巴萨与利物浦12。英超：阿森纳28，布莱顿22，曼城22，利物浦21。",
        ),
        "ja": loc(
            "欧州CL水曜：バルセロナがサバフに4-1、リヴァプールがブルージュに3-0",
            "ゴードンがバクーで2得点、イサクがリヴァプールを12に乗せる。レアルはPSV戦5-1の後も15で首位。",
            "アンソニー・ゴードンが31分と51分に得点しバルサが4-1。リヴァプールはイサクとヴィルツで3-0。",
            "CLリーグフェーズ第5節は11月25日水曜に閉幕。バルセロナとリヴァプールが勝ち、自動進出トップ8争いを維持した。",
            "バクーではゴードン31・51、アデイェミ55、ジェズス60、ミッケルズ63。ヤマル不在のフリック指揮で5戦4勝12ポイント。ゴードンがMOM。",
            "リヴァプールはブルージュに3-0。イサク13分と終盤チップ、ヴィルツ79分。5節後レアルは15で首位（火曜5-1、ベリンガム59）。PSG 13、バルサとリヴァプール12。PLはアーセナル28、ブライトン22、シティ22、リヴァプール21。",
        ),
        "ko": loc(
            "UCL 수요일: 바르사 사바흐 원정 4-1, 리버풀 브뤼헤 3-0",
            "고든이 바쿠에서 두 골, 이삭이 리버풀을 12점으로. 레알은 PSV 5-1 이후에도 15점 선두.",
            "앤서니 고든이 31분과 51분 골로 바르사가 4-1. 리버풀은 이삭과 비르츠로 3-0.",
            "챔피언스리그 리그 페이즈 5차전은 11월 25일 수요일 종료. 바르셀로나와 리버풀이 상위 8강 자동 진출 싸움을 이어갔다.",
            "바쿠: 고든 31·51, 아데예미 55, 제수스 60, 미켈스 63. 야말 없는 플릭 체제에서 5전 4승 12점. 고든 MOM.",
            "리버풀은 브뤼헤를 3-0. 이삭 13분과 후반 칩샷, 비르츠 79분. 5라운드 후 레알 15점 선두(화 5-1, 벨링엄 59). PSG 13, 바르사·리버풀 12. PL 아스널 28, 브라이튼 22, 시티 22, 리버풀 21.",
        ),
        "ar": loc(
            "دوري الابطال الاربعاء: برشلونة 4-1 في باكو وليفربول 3-0 في بروج",
            "غوردون يسجل هدفين وايساك يقود ليفربول الى 12 نقطة، وريال مدريد يبقى الاول بـ15 بعد الخماسية في ايندهوفن.",
            "انطوني غوردون سجل في 31 و51، برشلونة فاز 4-1. ليفربول فاز 3-0 في بروج بايساك وفيرتز.",
            "اغلقت الجولة الخامسة من دوري الابطال الاربعاء 25 نوفمبر بفوز برشلونة وليفربول في سباق المراكز الثمانية.",
            "في باكو غوردون 31 و51، ادييمي 55، جيسوس 60، ميكلز 63. فليك بدون يامال يحقق رابع فوز من خمسة و12 نقطة. غوردون رجل المباراة.",
            "ليفربول 3-0 في بروج: ايساك 13 ثم رفعه متاخرة، فيرتز 79. بعد خمس جولات ريال مدريد اول بـ15 (5-1 الثلاثاء، بيلينغهام 59). باريس 13، برشا وليفربول 12. الدوري الانجليزي: ارسنال 28، برايتون 22، سيتي 22، ليفربول 21.",
        ),
    },
    "davis-cup-finals-bologna-italy-musetti-alcaraz-turin-glory-2026": {
        "fr": loc(
            "Coupe Davis Bologne : Italie 2-1 Coree et Grande-Bretagne 2-1 Allemagne en demi",
            "Berrettini et Vavassori ferment le tie italien ; Patten et Skupski offrent a la GB une premiere demi depuis 2019.",
            "Italie 2-1 mercredi, GB 2-1 jeudi a Bologne. Autriche-Espagne a 17h00 CET inedit.",
            "La Final 8 de Coupe Davis a Bologne a trois quarts de finale boucles et un encore a jouer.",
            "Mercredi, l Italie a battu la Coree du Sud 2-1. Musetti d Hong 6-0, 7-6(5). Kwon d Cobolli 3-6, 7-6(3), 7-6(5). Berrettini et Vavassori 7-6(2), 7-6(11). La Tchequie avait balaye le Canada 2-0. Italie-Tchequie vendredi 16h00.",
            "Jeudi, la Grande-Bretagne a battu l Allemagne 2-1, premiere demi depuis 2019. Norrie d Struff 6-3, 3-6, 6-2. Zverev d Fery 6-3, 6-2. Patten et Skupski 6-2, 7-6(6). Autriche-Espagne 17h00 inedit. Turin : Alcaraz 6-2, 7-6(7) imbattu 5-0.",
        ),
        "es": loc(
            "Copa Davis Bolonia: Italia 2-1 Corea y Gran Bretana 2-1 Alemania a semifinales",
            "Berrettini y Vavassori cierran el empate italiano; Patten y Skupski meten a GB en semis por primera vez desde 2019.",
            "Italia 2-1 el miercoles y GB 2-1 el jueves en Bolonia. Austria-Espana 17:00 CET inedito.",
            "La Final 8 de Copa Davis en Bolonia tiene tres cuartos cerrados y uno por jugar.",
            "El miercoles Italia gano 2-1 a Corea del Sur. Musetti d Hong 6-0, 7-6(5). Kwon d Cobolli 3-6, 7-6(3), 7-6(5). Berrettini y Vavassori 7-6(2), 7-6(11). Chequia ya habia barrido a Canada 2-0. Italia-Chequia el viernes 16:00.",
            "El jueves Gran Bretana gano 2-1 a Alemania, primera semifinal desde 2019. Norrie d Struff 6-3, 3-6, 6-2. Zverev d Fery 6-3, 6-2. Patten y Skupski 6-2, 7-6(6). Austria-Espana 17:00 inedito. Turin: Alcaraz 6-2, 7-6(7) invicto 5-0.",
        ),
        "de": loc(
            "Davis Cup Bologna: Italien 2:1 Korea und Grossbritannien 2:1 Deutschland im Halbfinale",
            "Berrettini und Vavassori retten Italien; Patten und Skupski schicken GB erstmals seit 2019 ins Halbfinale.",
            "Italien 2:1 am Mittwoch, GB 2:1 am Donnerstag in Bologna. Oesterreich-Spanien 17:00 CET unveröffentlicht.",
            "Die Davis-Cup-Final-8 in Bologna hat drei Viertelfinals abgeschlossen und eines noch offen.",
            "Mittwoch gewann Italien 2:1 gegen Suedkorea. Musetti d Hong 6:0, 7:6(5). Kwon d Cobolli 3:6, 7:6(3), 7:6(5). Berrettini/Vavassori 7:6(2), 7:6(11). Tschechien hatte Kanada 2:0 gefegt. Italien-Tschechien Freitag 16:00.",
            "Donnerstag schlug Grossbritannien Deutschland 2:1, erstes Halbfinale seit 2019. Norrie d Struff 6:3, 3:6, 6:2. Zverev d Fery 6:3, 6:2. Patten/Skupski 6:2, 7:6(6). Oesterreich-Spanien 17:00 unveröffentlicht. Turin: Alcaraz 6:2, 7:6(7) ungeschlagen 5-0.",
        ),
        "it": loc(
            "Coppa Davis Bologna: Italia 2-1 Corea e Gran Bretagna 2-1 Germania in semifinale",
            "Berrettini e Vavassori chiudono il tie azzurro; Patten e Skupski riportano la GB in semifinale dal 2019.",
            "Italia 2-1 mercoledi e GB 2-1 giovedi a Bologna. Austria-Spagna 17:00 CET inedito.",
            "La Final 8 di Coppa Davis a Bologna ha tre quarti chiusi e uno ancora da giocare.",
            "Mercoledi l Italia ha battuto la Corea del Sud 2-1. Musetti d Hong 6-0, 7-6(5). Kwon d Cobolli 3-6, 7-6(3), 7-6(5). Berrettini e Vavassori 7-6(2), 7-6(11). La Ceca aveva spazzato il Canada 2-0. Italia-Ceca venerdi 16:00.",
            "Giovedi la Gran Bretagna ha battuto la Germania 2-1, prima semifinale dal 2019. Norrie d Struff 6-3, 3-6, 6-2. Zverev d Fery 6-3, 6-2. Patten e Skupski 6-2, 7-6(6). Austria-Spagna 17:00 inedito. Torino: Alcaraz 6-2, 7-6(7) imbattuto 5-0.",
        ),
        "pl": loc(
            "Puchar Davisa Bolonia: Wlochy 2:1 Korea i Wielka Brytania 2:1 Niemcy w polfinale",
            "Berrettini i Vavassori domykaja tie Wloch; Patten i Skupski daja GB pierwszy polfinal od 2019.",
            "Wlochy 2:1 w srode, GB 2:1 w czwartek w Bolonii. Austria-Hiszpania 17:00 CET nieopublikowane.",
            "Final 8 Pucharu Davisa w Bolonii ma trzy cwiercfinaly zamkniete i jeden do zagrania.",
            "W srode Wlochy wygraly 2:1 z Korea Pld. Musetti d Hong 6:0, 7:6(5). Kwon d Cobolli 3:6, 7:6(3), 7:6(5). Berrettini/Vavassori 7:6(2), 7:6(11). Czechy wczesniej zmietly Kanade 2:0. Wlochy-Czechy w piatek 16:00.",
            "W czwartek Wielka Brytania pokonala Niemcy 2:1, pierwszy polfinal od 2019. Norrie d Struff 6:3, 3:6, 6:2. Zverev d Fery 6:3, 6:2. Patten/Skupski 6:2, 7:6(6). Austria-Hiszpania 17:00 nieopublikowane. Turyn: Alcaraz 6:2, 7:6(7) bez porazki 5-0.",
        ),
        "zh": loc(
            "戴维斯杯博洛尼亚：意大利2-1韩国、英国2-1德国晋级四强",
            "贝雷蒂尼与瓦瓦索里锁定意大利；帕滕与斯库普斯基送英国2019年以来首次四强。",
            "周三意大利2-1，周四英国2-1。奥地利对西班牙中欧17:00未公布。",
            "戴维斯杯总决赛八强在博洛尼亚已有三场四分之一决赛完场，一场待赛。",
            "周三意大利2-1韩国。穆塞蒂6-0、7-6(5)洪性成。权纯宇3-6、7-6(3)、7-6(5)科博利。贝雷蒂尼/瓦瓦索里7-6(2)、7-6(11)。捷克周二2-0加拿大。周五意大利对捷克16:00。",
            "周四英国2-1德国，2019年来首次四强。诺里6-3、3-6、6-2施特鲁夫。兹维列夫6-3、6-2费里。帕滕/斯库普斯基6-2、7-6(6)。奥西17:00未公布。都灵：阿尔卡拉斯6-2、7-6(7)五战全胜。",
        ),
        "ja": loc(
            "デビス杯ボローニャ：イタリア2-1韓国、英国2-1ドイツが準決勝へ",
            "ベレッティーニ＆ババッソリがイタリアを救い、パッテン＆スクプスキが2019年以来の準決勝へ導く。",
            "水曜イタリア2-1、木曜英国2-1。オーストリア対スペイン17:00 CETは未公開。",
            "ボローニャのデビス杯ファイナル8は準々決勝3試合が終了、1試合が残る。",
            "水曜、イタリアが韓国に2-1。ムゼッティがホンに6-0, 7-6(5)。クォンがコボッリに3-6, 7-6(3), 7-6(5)。ベレッティーニ／ババッソリが7-6(2), 7-6(11)。チェコは火曜カナダに2-0。金曜イタリア対チェコ16:00。",
            "木曜、英国がドイツに2-1、2019年以来の準決勝。ノリーがシュトルフに6-3, 3-6, 6-2。ズベレフがフェリーに6-3, 6-2。パッテン／スクプスキが6-2, 7-6(6)。オーストリア対スペイン17:00未公開。トリノ：アルカラス6-2, 7-6(7)で5戦全勝。",
        ),
        "ko": loc(
            "데이비스컵 볼로냐: 이탈리아 2-1 한국, 영국 2-1 독일이 4강",
            "베레티니-바바소리가 이탈리아를 살리고, 패튼-스쿱스키가 2019년 이후 첫 준결승으로 이끈다.",
            "수요일 이탈리아 2-1, 목요일 영국 2-1. 오스트리아-스페인 17:00 CET는 미공개.",
            "볼로냐 데이비스컵 파이널8은 8강 3경기가 끝났고 1경기가 남았다.",
            "수요일 이탈리아가 한국에 2-1. 무세티가 홍성찬에 6-0, 7-6(5). 권순우가 코볼리에 3-6, 7-6(3), 7-6(5). 베레티니/바바소리 7-6(2), 7-6(11). 체코는 화요일 캐나다를 2-0. 금요일 이탈리아-체코 16:00.",
            "목요일 영국이 독일에 2-1, 2019년 이후 첫 준결승. 노리가 슈트루프에 6-3, 3-6, 6-2. 즈베레프가 페리에 6-3, 6-2. 패튼/스쿱스키 6-2, 7-6(6). 오스트리아-스페인 17:00 미공개. 토리노: 알카라스 6-2, 7-6(7) 5전 전승.",
        ),
        "ar": loc(
            "كاس ديفيز بولونيا: ايطاليا 2-1 كوريا وبريطانيا 2-1 المانيا الى نصف النهائي",
            "بيريتيني وفافاسوري يحسمان التعادل الايطالي؛ باتن وسكوبسكي يعيدان بريطانيا الى نصف النهائي منذ 2019.",
            "ايطاليا 2-1 الاربعاء وبريطانيا 2-1 الخميس. النمسا-اسبانيا 17:00 غير منشور.",
            "نهائيات كاس ديفيز الثمانية في بولونيا اغلقت ثلاثة ارباع نهائي وبقي لقاء.",
            "الاربعاء فازت ايطاليا 2-1 على كوريا. موسيتي 6-0 و7-6(5) هونغ. كوون 3-6 و7-6(3) و7-6(5) كوبولي. بيريتيني وفافاسوري 7-6(2) و7-6(11). التشيك كنس كندا 2-0. ايطاليا-التشيك الجمعة 16:00.",
            "الخميس فازت بريطانيا 2-1 على المانيا، اول نصف نهائي منذ 2019. نوري 6-3 و3-6 و6-2 شتروف. زفيريف 6-3 و6-2 فيري. باتن وسكوبسكي 6-2 و7-6(6). النمسا-اسبانيا 17:00 غير منشور. تورينو: الكاراز 6-2 و7-6(7) دون هزيمة 5-0.",
        ),
    },
    "nba-sixers-heat-lebron-triple-double-2026": {
        "fr": loc(
            "NBA Cup mercredi : premier triple-double de LeBron chez les Sixers, 111-104 contre le Heat",
            "James compile 25 points, 10 rebonds et 12 passes, Philadelphie stoppe la serie de sept victoires de Miami avant la pause.",
            "LeBron signe son premier triple-double en Sixer, Maxey 30 points. Portland bat San Antonio 116-111, Wembanyama 44 et 16.",
            "La NBA Cup s est arretee mercredi 25 novembre avant un jeudi de Thanksgiving sans match.",
            "Les 76ers ont battu le Heat 111-104. LeBron James : 25 points, 10 rebonds, 12 passes, premier triple-double sous le maillot de Philadelphie. Maxey 30. Giannis 32 points et 14 rebonds. Philadelphie passe a 15-4 et coupe la serie de sept succes de Miami.",
            "Portland a battu San Antonio 116-111. Avdija 33, 12 rebonds, 7 passes. Lillard 29 points, 10/10 aux lancers. Wembanyama 44 points et 16 rebonds. Mardi tient : Dallas 120-101 Denver, Boston 131-116 Washington, Detroit 104-86 Orlando.",
        ),
        "es": loc(
            "NBA Cup miercoles: primer triple-doble de LeBron con los Sixers, 111-104 al Heat",
            "James firma 25 puntos, 10 rebotes y 12 asistencias; Filadelfia corta la racha de siete del Heat antes del descanso.",
            "LeBron logra su primer triple-doble como Sixer y Maxey anota 30. Portland gana 116-111 a San Antonio, Wembanyama 44 y 16.",
            "La NBA Cup cerro el miercoles 25 de noviembre antes de un jueves de Accion de Gracias sin partidos.",
            "Los 76ers ganaron 111-104 al Heat. LeBron: 25, 10 y 12, primer triple-doble con Filadelfia. Maxey 30. Giannis 32 y 14. Filadelfia 15-4 y corta la racha de siete de Miami.",
            "Portland 116-111 San Antonio. Avdija 33/12/7. Lillard 29, 10/10 en tiros libres. Wembanyama 44 y 16. El martes sigue: Dallas 120-101 Denver, Boston 131-116 Washington, Detroit 104-86 Orlando.",
        ),
        "de": loc(
            "NBA Cup Mittwoch: erstes Sixers-Triple-Double von LeBron, 111:104 gegen Heat",
            "James mit 25 Punkten, 10 Rebounds und 12 Assists; Philadelphia beendet Miamis Serie von sieben Siegen vor der Pause.",
            "LeBron holt sein erstes Triple-Double als Sixer, Maxey 30. Portland schlaegt San Antonio 116:111, Wembanyama 44 und 16.",
            "Der NBA Cup endete am Mittwoch, 25. November, vor einem spielfreien Thanksgiving-Donnerstag.",
            "Die 76ers gewannen 111:104 gegen die Heat. LeBron 25/10/12, erstes Triple-Double im Sixers-Trikot. Maxey 30. Giannis 32 und 14. Philadelphia 15-4, Miami-Serie von sieben Siegen gerissen.",
            "Portland 116:111 San Antonio. Avdija 33/12/7. Lillard 29, 10/10 Freiwuerfe. Wembanyama 44 und 16. Dienstag bleibt: Dallas 120:101 Denver, Boston 131:116 Washington, Detroit 104:86 Orlando.",
        ),
        "it": loc(
            "NBA Cup mercoledi: primo triple-double di LeBron con i Sixers, 111-104 sul Heat",
            "James 25 punti, 10 rimbalzi e 12 assist; Philadelphia spezza la striscia di sette del Heat prima della sosta.",
            "LeBron firma il primo triple-double da Sixer, Maxey 30. Portland batte San Antonio 116-111, Wembanyama 44 e 16.",
            "La NBA Cup si e fermata mercoledi 25 novembre prima del giovedi del Ringraziamento senza gare.",
            "I 76ers hanno battuto il Heat 111-104. LeBron 25/10/12, primo triple-double con Philadelphia. Maxey 30. Giannis 32 e 14. Philadelphia 15-4, striscia di sette del Heat interrotta.",
            "Portland 116-111 San Antonio. Avdija 33/12/7. Lillard 29, 10/10 liberi. Wembanyama 44 e 16. Martedi resta: Dallas 120-101 Denver, Boston 131-116 Washington, Detroit 104-86 Orlando.",
        ),
        "pl": loc(
            "NBA Cup w srode: pierwsze triple-double LeBrona w Sixers, 111:104 z Heat",
            "James 25 pkt, 10 zbiórek i 12 asyst; Filadelfia przerywa serie siedmiu wygranych Miami przed pauza.",
            "LeBron pierwsze triple-double jako Sixer, Maxey 30. Portland 116:111 San Antonio, Wembanyama 44 i 16.",
            "NBA Cup zakonczyla sie w srode 25 listopada przed czwartkiem Swieta Dziekczynienia bez meczow.",
            "76ers wygrali 111:104 z Heat. LeBron 25/10/12, pierwsze triple-double w barwach Filadelfii. Maxey 30. Giannis 32 i 14. Filadelfia 15-4, seria siedmiu Miami przerwana.",
            "Portland 116:111 San Antonio. Avdija 33/12/7. Lillard 29, 10/10 z linii. Wembanyama 44 i 16. Wtorek bez zmian: Dallas 120:101 Denver, Boston 131:116 Washington, Detroit 104:86 Orlando.",
        ),
        "zh": loc(
            "NBA杯周三：詹姆斯76人首记三双，111-104击败热火",
            "詹姆斯25分10篮板12助攻，费城终结迈阿密七连胜后迎感恩节休战。",
            "詹姆斯完成76人首个三双，马克西30分。开拓者116-111马刺，文班亚马44分16板。",
            "NBA杯于11月25日周三收官，周四感恩节全联盟休战。",
            "76人以111-104击败热火。詹姆斯25分10篮板12助攻，穿76人球衣首个三双。马克西30分。字母哥32分14板。费城升至15胜4负，热火七连胜作罢。",
            "开拓者116-111马刺。阿夫迪亚33分12板7助。利拉德29分罚球10中10。文班亚马44分16板。周二战绩仍在：独行侠120-101掘金，凯尔特人131-116奇才，活塞104-86魔术。",
        ),
        "ja": loc(
            "NBA杯水曜：レブロンがシクサーズ初トリプルダブル、111-104でヒート撃破",
            "ジェームズ25点10リバウンド12アシスト。フィラデルフィアがマイアミの7連勝を止めて感謝祭休養へ。",
            "レブロンがシクサーズ初のトリプルダブル、マクシー30点。ポートランドがサンアントニオに116-111、ウェンバンヤマ44点16リバウンド。",
            "NBAカップは11月25日水曜で終了し、木曜は感謝祭で全休。",
            "76ersがヒートに111-104。レブロン25/10/12でシクサーズ初トリプルダブル。マクシー30。ヤニス32点14リバウンド。フィラデルフィアは15勝4敗、マイアミの7連勝を止めた。",
            "ポートランド116-111サンアントニオ。アヴディヤ33/12/7。リラード29点、フリースロー10/10。ウェンバンヤマ44点16リバウンド。火曜は変わらずダラス120-101、ボストン131-116、デトロイト104-86。",
        ),
        "ko": loc(
            "NBA컵 수요일: 르브론 식서스 첫 트리플더블, 히트에 111-104",
            "제임스 25점 10리바운드 12어시스트. 필라델피아가 마이애미 7연승을 끊고 추수감사절 휴식으로.",
            "르브론이 식서스 첫 트리플더블, 맥시 30점. 포틀랜드가 샌안토니오에 116-111, 웸반야마 44점 16리바운드.",
            "NBA컵은 11월 25일 수요일 종료, 목요일은 추수감사절 전 리그 휴식.",
            "76ers가 히트를 111-104로 꺾었다. 르브론 25/10/12, 식서스 유니폼 첫 트리플더블. 맥시 30. 야니스 32점 14리바운드. 필라델피아 15승 4패, 마이애미 7연승 종료.",
            "포틀랜드 116-111 샌안토니오. 아브디야 33/12/7. 릴라드 29점 자유투 10/10. 웸반야마 44점 16리바운드. 화요일은 그대로 댈러스 120-101, 보스턴 131-116, 디트로이트 104-86.",
        ),
        "ar": loc(
            "كأس NBA الاربعاء: اول تريبل دبل لليبرون مع سيكسرز، 111-104 امام هيت",
            "جيمس 25 نقطة و10 متابعات و12 تمريرة حاسمة، فيلادلفيا توقف سلسلة ميامي من سبع انتصارات قبل الراحة.",
            "ليبرون يسجل اول تريبل دبل بقميص سيكسرز وماكسي 30. بورتلاند 116-111 سان انطونيو، ويمبانياما 44 و16.",
            "اغلقت كأس الدوري الاربعاء 25 نوفمبر قبل خميس عيد الشكر بلا مباريات.",
            "فاز سيكسرز 111-104 على هيت. ليبرون 25/10/12 اول تريبل دبل مع فيلادلفيا. ماكسي 30. يانيس 32 و14. فيلادلفيا 15-4 وتوقف سلسلة ميامي من سبع.",
            "بورتلاند 116-111 سان انطونيو. افديا 33/12/7. ليلارد 29 مع 10/10 رميات حرة. ويمبانياما 44 و16. الثلاثاء كما هو: دالاس 120-101 دنفر، بوسطن 131-116 واشنطن، ديترويت 104-86 اورلاندو.",
        ),
    },
}


def replace_slug(text, slug, obj):
    needle = f'  "{slug}": '
    start = text.find(needle)
    dumped = json.dumps(obj, ensure_ascii=False, indent=2)
    dumped = "  " + dumped.replace("\n", "\n  ")
    block = f'  "{slug}": ' + dumped[2:]  # dumped starts with {
    if start == -1:
        return None, block
    i = text.find("{", start)
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                end = j + 1
                break
    else:
        raise SystemExit(f"unclosed {slug}")
    return text[:start] + block + text[end:], None


text = open(PATH, encoding="utf-8").read()
to_insert = []
for slug, obj in NEW.items():
    updated, block = replace_slug(text, slug, obj)
    if updated is None:
        to_insert.append((slug, obj))
    else:
        text = updated
        print("replaced", slug)

if to_insert:
    inner = ",\n".join(
        f'  "{slug}": ' + json.dumps(obj, ensure_ascii=False, indent=2).replace("\n", "\n  ")
        for slug, obj in to_insert
    )
    idx = text.rstrip().rfind("};")
    text = text.rstrip()[:idx] + inner + "\n};\n"
    for slug, _ in to_insert:
        print("inserted", slug)

no_dashes(text, "stories.ts")
open(PATH, "w", encoding="utf-8").write(text)
print("stories.ts ok")
