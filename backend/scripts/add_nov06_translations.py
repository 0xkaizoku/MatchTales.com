# -*- coding: utf-8 -*-
"""Add 6 November 2026 translations for all 6 stories across 9 languages."""
import json
import os

NOV06_STORIES = {
    "nfl-week9-tnf-jaguars-33-10-ravens-lawrence-2026": {
        "fr": {
            "title": "NFL Semaine 9 TNF : Les Jaguars ecrasent les Ravens 33-10, Lawrence et quatre field goals de Little",
            "subtitle": "Jacksonville provoque trois turnovers sous la pluie a Baltimore. Joe Fagnano connait un premier depart difficile sans Jackson ni Huntley.",
            "excerpt": "Trevor Lawrence a lance pour 242 yards et un touchdown de 50 yards, et les Jaguars ont battu les Ravens 33-10 jeudi soir.",
            "body": [
                "Les Jacksonville Jaguars ont battu les Baltimore Ravens 33-10 jeudi 5 novembre au M&T Bank Stadium sur Prime Video. Jacksonville passe a 6-2, cinquieme succes en six matches. Baltimore tombe a 4-5 apres une quatrieme defaite d'affilee.",
                "Lawrence a complete 16 passes sur 26 pour 242 yards et un TD de 50 yards a Parker Washington. Cam Little a egalise son record en carriere avec quatre field goals. Joe Fagnano, titulaire en l'absence de Lamar Jackson et Tyler Huntley, a termine a 10 sur 18 pour 60 yards et deux interceptions. Justice Hill a inscrit un TD de 65 yards (9 courses, 85 yards). Affluence : 70 007 spectateurs. Les Steelers restent 6-2 en AFC Nord."
            ]
        },
        "es": {
            "title": "NFL Semana 9 TNF: Los Jaguars golean 33-10 a los Ravens con Lawrence y cuatro goles de campo de Little",
            "subtitle": "Jacksonville fuerza tres perdidas bajo la lluvia en Baltimore. Joe Fagnano debuta como titular sin Jackson ni Huntley.",
            "excerpt": "Trevor Lawrence lanzo para 242 yardas y un touchdown de 50 y los Jaguars vencieron 33-10 a los Ravens el jueves por la noche.",
            "body": [
                "Los Jacksonville Jaguars vencieron 33-10 a los Baltimore Ravens el jueves 5 de noviembre en el M&T Bank Stadium por Prime Video. Jacksonville sube a 6-2. Baltimore cae a 4-5 tras su cuarta derrota seguida.",
                "Lawrence completo 16 de 26 pases para 242 yardas y un TD de 50 a Parker Washington. Cam Little igualo su tope de carrera con cuatro goles de campo. Joe Fagnano, titular por lesiones de Lamar Jackson y Tyler Huntley, fue 10 de 18 para 60 yardas y dos intercepciones. Justice Hill anoto de 65 yardas (9 acarreos, 85 yardas). Asistencia: 70.007. Los Steelers siguen 6-2 en la AFC Norte."
            ]
        },
        "de": {
            "title": "NFL Woche 9 TNF: Jaguars demontieren Ravens 33:10 mit Lawrence und vier Field Goals von Little",
            "subtitle": "Jacksonville erzwingt drei Ballverluste im Regen von Baltimore. Joe Fagnano startet ohne Jackson und Huntley.",
            "excerpt": "Trevor Lawrence wirft 242 Yards und einen 50-Yard-Touchdown, die Jaguars schlagen die Ravens am Donnerstag 33:10.",
            "body": [
                "Die Jacksonville Jaguars schlugen die Baltimore Ravens am Donnerstag, den 5. November, im M&T Bank Stadium mit 33:10. Jacksonville steht 6-2. Baltimore faellt nach der vierten Niederlage in Folge auf 4-5.",
                "Lawrence komplettierte 16 von 26 Passen fuer 242 Yards und einen 50-Yard-TD an Parker Washington. Cam Little egalisierte seine Karrierebestmarke mit vier Field Goals. Joe Fagnano, Starter ohne Lamar Jackson und Tyler Huntley, kam auf 10 von 18 fuer 60 Yards und zwei Interceptions. Justice Hill lief 65 Yards zum TD (9 Laeufe, 85 Yards). Zuschauer: 70.007. Die Steelers bleiben 6-2 in der AFC North."
            ]
        },
        "it": {
            "title": "NFL Week 9 TNF: i Jaguars travolgono i Ravens 33-10 con Lawrence e quattro field goal di Little",
            "subtitle": "Jacksonville forza tre palloni persi sotto la pioggia a Baltimore. Primo start per Joe Fagnano senza Jackson e Huntley.",
            "excerpt": "Trevor Lawrence lancia per 242 yard e un touchdown da 50: i Jaguars battono i Ravens 33-10 giovedi sera.",
            "body": [
                "I Jacksonville Jaguars hanno battuto i Baltimore Ravens 33-10 giovedi 5 novembre al M&T Bank Stadium su Prime Video. Jacksonville sale a 6-2. Baltimore scende a 4-5 dopo la quarta sconfitta di fila.",
                "Lawrence ha completato 16 passaggi su 26 per 242 yard e un TD da 50 a Parker Washington. Cam Little ha eguagliato il suo record in carriera con quattro field goal. Joe Fagnano, titolare al posto di Lamar Jackson e Tyler Huntley, ha chiuso 10 su 18 per 60 yard e due intercetti. Justice Hill ha segnato da 65 yard (9 corse, 85 yard). Pubblico: 70.007. Gli Steelers restano 6-2 in AFC North."
            ]
        },
        "pl": {
            "title": "NFL tydzien 9 TNF: Jaguars rozbijaja Ravens 33:10, Lawrence i cztery field goale Little'a",
            "subtitle": "Jacksonville wymusza trzy straty w deszczu w Baltimore. Joe Fagnano debiutuje w skladzie bez Jacksona i Huntleya.",
            "excerpt": "Trevor Lawrence rzucil na 242 jardy i przylozenie z 50 jardow, a Jaguars wygrali z Ravens 33:10 w czwartek.",
            "body": [
                "Jacksonville Jaguars pokonali Baltimore Ravens 33:10 w czwartek 5 listopada na M&T Bank Stadium. Jacksonville ma 6-2. Baltimore spada do 4-5 po czwartej porazce z rzedu.",
                "Lawrence uzupelnil 16 z 26 podan na 242 jardy i TD z 50 jardow do Parkera Washingtona. Cam Little wyrownal rekord kariery czterema field goalami. Joe Fagnano, starter bez Lamara Jacksona i Tylera Huntleya, mial 10 z 18 na 60 jardow i dwa przechwyty. Justice Hill zdobyl TD z 65 jardow (9 niesien, 85 jardow). Frekwencja: 70 007. Steelers nadal 6-2 w AFC North."
            ]
        },
        "zh": {
            "title": "NFL第9周周四夜赛：美洲虎33-10大胜乌鸦，劳伦斯传球与利特尔四记任意球定胜负",
            "subtitle": "杰克逊维尔在巴尔的摩雨战制造三次失误。法尼亚诺在杰克逊与亨特利缺阵下首次首发。",
            "excerpt": "特雷弗·劳伦斯传球242码并送出50码达阵，美洲虎周四夜赛33-10击败乌鸦。",
            "body": [
                "杰克逊维尔美洲虎11月5日周四在M&T银行球场以33-10击败巴尔的摩乌鸦，战绩升至6胜2负。乌鸦连败四场后战绩为4胜5负。",
                "劳伦斯26次传球完成16次，242码，50码达阵给帕克·华盛顿。卡姆·利特尔踢进四记任意球追平生涯最佳。乔·法尼亚诺在拉马尔·杰克逊与泰勒·亨特利受伤缺阵下首次首发，18中10仅60码并被拦截两次。贾斯蒂斯·希尔跑出65码达阵（9次冲球85码）。现场观众70007人。钢人在美联北区仍为6胜2负。"
            ]
        },
        "ja": {
            "title": "NFL第9週TNF：ジャガーズがレイブンズを33-10で圧倒、ローレンスとリトル4本のFG",
            "subtitle": "ジャクソンビルがボルチモアの雨の中で3ターンオーバーを奪う。ファニャーノがジャクソンとハントリー不在で初先発。",
            "excerpt": "トレバー・ローレンスが242ヤードと50ヤードTDを記録し、ジャガーズが木曜夜にレイブンズを33-10で破った。",
            "body": [
                "ジャクソンビル・ジャガーズは11月5日木曜日、M&Tバンク・スタジアムでボルチモア・レイブンズを33-10で破った。ジャガーズは6勝2敗。レイブンズは4連敗で4勝5敗。",
                "ローレンスは26回中16回成功で242ヤード、パーカー・ワシントンへの50ヤードTD。キャム・リトルはキャリア最多タイの4本のFG。ジョー・ファニャーノはラマー・ジャクソンとタイラー・ハントリーの欠場で初先発し、18回中10回成功60ヤード、2インターセプト。ジャスティス・ヒルが65ヤードTD（9回85ヤード）。観客70,007人。スティーラーズはAFC北地区で引き続き6勝2敗。"
            ]
        },
        "ko": {
            "title": "NFL 9주차 TNF: 재규어스, 로런스와 리틀 필드골 4개로 레이븐스 33-10 대파",
            "subtitle": "잭슨빌이 볼티모어 빗속에서 턴오버 3개를 유도. 파냐노가 잭슨·헌틀리 공백 속 첫 선발.",
            "excerpt": "트레버 로런스가 242야드 패스와 50야드 터치다운을 기록하며 재규어스가 목요일 밤 레이븐스를 33-10으로 꺾었습니다.",
            "body": [
                "잭슨빌 재규어스가 11월 5일 목요일 M&T 뱅크 스타디움에서 볼티모어 레이븐스를 33-10으로 꺾고 6승 2패가 됐습니다. 레이븐스는 4연패로 4승 5패입니다.",
                "로런스는 26회 중 16회 성공 242야드, 파커 워싱턴에게 50야드 TD. 캠 리틀은 필드골 4개로 커리어 타이. 조 파냐노는 라마 잭슨과 타일러 헌틀리 부상으로 첫 선발, 18회 중 10회 60야드 인터셉트 2개. 저스티스 힐이 65야드 TD(9회 85야드). 관중 70,007명. 스틸러스는 AFC 북부에서 여전히 6승 2패입니다."
            ]
        },
        "ar": {
            "title": "الدوري الامريكي الاسبوع 9: جاغوارز يسحق ريڤنز 33-10 بلورنس واربعة ركلات ميدانية من ليتل",
            "subtitle": "جاكسونفيل يجبر على ثلاث خسائر للكرة تحت المطر في بالتيمور. فاينيانو يخوض اول مشاركة اساسية دون جاكسون وهانتلي.",
            "excerpt": "تريفر لورنس يمرر 242 ياردة ويسجل هدفا من 50 ياردة ويقود جاغوارز للفوز 33-10 على ريڤنز الخميس.",
            "body": [
                "فاز جاكسونفيل جاغوارز على بالتيمور ريڤنز 33-10 يوم الخميس 5 نوفمبر في ملعب ام اند تي بنك. جاغوارز الى 6-2. ريڤنز الى 4-5 بعد الخسارة الرابعة تواليا.",
                "اكمل لورنس 16 تمريرة من 26 لـ242 ياردة وهدف من 50 لياردة لباركر واشنطن. عادل كام ليتل رقمه الشخصي باربع ركلات ميدانية. جو فاينيانو، الاساسي بدلا من لامار جاكسون وتايلر هانتلي، انهى 10 من 18 لـ60 ياردة وتقطيعين. جاستس هيل سجل من 65 ياردة (9 ركضات، 85 ياردة). الحضور: 70007. ستيلرز ما زال 6-2 في شمال AFC."
            ]
        }
    },
    "nba-wembanyama-52-24-8-spurs-edge-mavs-112-111-2026": {
        "fr": {
            "title": "NBA : Wembanyama compile 52 points, 24 rebonds et 8 contres, les Spurs battent Dallas 112-111",
            "subtitle": "Premier 50-20-5 contres depuis Bob McAdoo en 1974, scelle par un lancer franc a 24,2 secondes de la fin.",
            "excerpt": "Victor Wembanyama a inscrit 52 points et pris 24 rebonds mercredi soir, et San Antonio a battu Dallas 112-111.",
            "body": [
                "Victor Wembanyama a termine a 52 points, 24 rebonds et 8 contres mercredi 4 novembre au Frost Bank Center. NBA.com et l'AP retiennent des records en carriere aux points et aux rebonds (16/28 aux tirs, 19/23 aux lancers, 1/8 a trois points, 34 minutes).",
                "Il avait 29 points, 15 rebonds et 5 contres a la pause. Un lancer franc a 24,2 secondes a fait 112-111. Kyrie Irving (29 points) a manque un fadeaway a 2,5 secondes. Harper 21, Castle 17 et 10 rebonds, Fox 10. Marshall 22, Washington 21, Flagg 19. Les Spurs sont 6-2. Cleveland est 4-4 apres une defaite 124-116 a Oklahoma City."
            ]
        },
        "es": {
            "title": "NBA: Wembanyama anota 52 puntos, 24 rebotes y 8 tapones y los Spurs ganan 112-111 a Dallas",
            "subtitle": "Primer 50-20-5 tapones desde Bob McAdoo en 1974, sellado con un tiro libre a 24,2 segundos del final.",
            "excerpt": "Victor Wembanyama firmo 52 puntos y 24 rebotes el miercoles y San Antonio vencio 112-111 a Dallas.",
            "body": [
                "Victor Wembanyama cerro con 52 puntos, 24 rebotes y 8 tapones el miercoles 4 de noviembre en el Frost Bank Center. NBA.com y AP recogen maximos de carrera en puntos y rebotes (16 de 28, 19 de 23 libres, 1 de 8 en triples, 34 minutos).",
                "Llego al descanso con 29 puntos, 15 rebotes y 5 tapones. Un libre a 24,2 segundos puso el 112-111. Kyrie Irving (29) fallo un giro a 2,5 segundos. Harper 21, Castle 17 y 10 rebotes, Fox 10. Marshall 22, Washington 21, Flagg 19. Spurs 6-2. Cleveland esta 4-4 tras perder 124-116 en Oklahoma City."
            ]
        },
        "de": {
            "title": "NBA: Wembanyama mit 52 Punkten, 24 Rebounds und 8 Blocks, Spurs schlagen Dallas 112:111",
            "subtitle": "Erstes 50-20-5-Blocks-Spiel seit Bob McAdoo 1974, entschieden per Freiwurf 24,2 Sekunden vor Schluss.",
            "excerpt": "Victor Wembanyama erzielt 52 Punkte und 24 Rebounds, San Antonio gewinnt am Mittwoch 112:111 gegen Dallas.",
            "body": [
                "Victor Wembanyama beendete den Abend am 4. November im Frost Bank Center mit 52 Punkten, 24 Rebounds und 8 Blocks. NBA.com und AP notieren Karrierebestwerte bei Punkten und Rebounds (16/28 FG, 19/23 FT, 1/8 Dreier, 34 Minuten).",
                "Zur Pause standen 29 Punkte, 15 Rebounds und 5 Blocks. Ein Freiwurf bei 24,2 Sekunden machte 112:111. Kyrie Irving (29) verfehlte einen Fadeaway bei 2,5 Sekunden. Harper 21, Castle 17 und 10 Rebounds, Fox 10. Marshall 22, Washington 21, Flagg 19. Spurs 6-2. Cleveland steht nach 124:116 in Oklahoma City bei 4-4."
            ]
        },
        "it": {
            "title": "NBA: Wembanyama 52 punti, 24 rimbalzi e 8 stoppate, gli Spurs battono Dallas 112-111",
            "subtitle": "Primo 50-20-5 stoppate da Bob McAdoo nel 1974, chiuso da un libero a 24,2 secondi dalla sirena.",
            "excerpt": "Victor Wembanyama mette a referto 52 punti e 24 rimbalzi mercoledi e San Antonio vince 112-111 su Dallas.",
            "body": [
                "Victor Wembanyama ha chiuso con 52 punti, 24 rimbalzi e 8 stoppate mercoledi 4 novembre al Frost Bank Center. NBA.com e AP riportano i massimi in carriera di punti e rimbalzi (16/28 dal campo, 19/23 liberi, 1/8 da tre, 34 minuti).",
                "All'intervallo aveva 29 punti, 15 rimbalzi e 5 stoppate. Un libero a 24,2 secondi ha fatto 112-111. Kyrie Irving (29) ha sbagliato un fadeaway a 2,5 secondi. Harper 21, Castle 17 e 10 rimbalzi, Fox 10. Marshall 22, Washington 21, Flagg 19. Spurs 6-2. Cleveland e 4-4 dopo il 124-116 a Oklahoma City."
            ]
        },
        "pl": {
            "title": "NBA: Wembanyama 52 punkty, 24 zbiorki i 8 blokow, Spurs wygrywaja z Dallas 112:111",
            "subtitle": "Pierwszy 50-20-5 blokow od Boba McAdoo w 1974, przesadzony rzutem wolnym na 24,2 sekundy przed koncem.",
            "excerpt": "Victor Wembanyama zdobyl 52 punkty i 24 zbiorki w srode, a San Antonio pokonalo Dallas 112:111.",
            "body": [
                "Victor Wembanyama zakonczyl srode 4 listopada w Frost Bank Center z 52 punktami, 24 zbiorkami i 8 blokami. NBA.com i AP notuja rekordy kariery w punktach i zbiorkach (16/28 z gry, 19/23 z linii, 1/8 za 3, 34 minuty).",
                "Do przerwy mial 29 punktow, 15 zbiorek i 5 blokow. Rzut wolny przy 24,2 s dal 112:111. Kyrie Irving (29) spudlowal przy 2,5 s. Harper 21, Castle 17 i 10 zbiorek, Fox 10. Marshall 22, Washington 21, Flagg 19. Spurs 6-2. Cleveland ma 4-4 po porazce 124:116 w Oklahoma City."
            ]
        },
        "zh": {
            "title": "NBA：文班亚马52分24篮板8盖帽，马刺112-111险胜独行侠",
            "subtitle": "1974年麦卡杜之后首次50+20+5盖，24.2秒罚球绝杀。",
            "excerpt": "维克托·文班亚马周三砍下52分24篮板，圣安东尼奥112-111险胜达拉斯。",
            "body": [
                "文班亚马11月4日周三在霜银行中心拿下52分24篮板8盖帽。NBA官网与美联社记录其生涯得分与篮板新高（投篮16中28，罚球19中23，三分1中8，出场34分钟）。",
                "半场已有29分15篮板5盖。24.2秒罚球将比分改写为112-111。凯里·欧文29分，2.5秒后仰不中。哈珀21分，卡斯尔17分10篮板，福克斯10分。马歇尔22分，华盛顿21分，弗拉格19分。马刺6胜2负。骑士在俄克拉荷马城124-116失利后战绩为4胜4负。"
            ]
        },
        "ja": {
            "title": "NBA：ウェンバンヤマが52得点24リバウンド8ブロック、スパーズがダラスを112-111で破る",
            "subtitle": "1974年マクアドー以来の50-20-5ブロック。残り24.2秒のフリースローで決着。",
            "excerpt": "ビクター・ウェンバンヤマが水曜日に52得点24リバウンドを記録し、サンアントニオがダラスを112-111で破った。",
            "body": [
                "ウェンバンヤマは11月4日水曜日、フロストバンク・センターで52得点24リバウンド8ブロック。NBA.comとAPは得点とリバウンドの自己最多を記録（フィールドゴール16/28、フリースロー19/23、3P 1/8、34分）。",
                "前半は29得点15リバウンド5ブロック。残り24.2秒のフリースローで112-111。カイリー・アービング（29得点）は残り2.5秒のフェイドアウェイを外した。ハーパー21、キャッスル17得点10リバウンド、フォックス10。マーシャル22、ワシントン21、フラッグ19。スパーズは6勝2敗。キャバリアーズはオクラホマシティに124-116で敗れ4勝4敗。"
            ]
        },
        "ko": {
            "title": "NBA: 웸반야마 52점 24리바운드 8블록, 스퍼스가 댈러스 112-111 제압",
            "subtitle": "1974년 맥아두 이후 첫 50-20-5 블록. 종료 24.2초 전 자유투로 승부 결정.",
            "excerpt": "빅터 웸반야마가 수요일 52점 24리바운드를 기록했고 샌안토니오가 댈러스를 112-111로 꺾었습니다.",
            "body": [
                "웸반야마는 11월 4일 수요일 프로스트 뱅크 센터에서 52점 24리바운드 8블록을 기록했습니다. NBA.com과 AP는 득점·리바운드 커리어 하이를 적었습니다(야투 16/28, 자유투 19/23, 3점 1/8, 34분).",
                "전반에만 29점 15리바운드 5블록. 24.2초 전 자유투가 112-111. 카이리 어빙(29점)은 2.5초 페이드어웨이를 놓쳤습니다. 하퍼 21, 캐슬 17점 10리바운드, 폭스 10. 마셜 22, 워싱턴 21, 플래그 19. 스퍼스 6승 2패. 캐벌리어스는 오클라호마시티에 124-116으로 져 4승 4패입니다."
            ]
        },
        "ar": {
            "title": "دوري السلة: ويمبانياما 52 نقطة و24 ارتدادا و8 صدات وسبيرز يهزم دالاس 112-111",
            "subtitle": "اول 50-20-5 صدات منذ بوب مكادو عام 1974، حسمتها رمية حرة قبل 24.2 ثانية.",
            "excerpt": "فيكتور ويمبانياما يسجل 52 نقطة و24 ارتدادا الاربعاء وسان انطونيو يفوز 112-111 على دالاس.",
            "body": [
                "انهى ويمبانياما مساء الاربعاء 4 نوفمبر في فروست بانك سنتر بـ52 نقطة و24 ارتدادا و8 صدات. NBA.com وAP يسجلان ارقاما قياسية في النقاط والارتدادات (16 من 28، 19 من 23 من الخط، 1 من 8 من الثلاث، 34 دقيقة).",
                "في الشوط الاول 29 نقطة و15 ارتدادا و5 صدات. رمية حرة قبل 24.2 ثانية جعلت النتيجة 112-111. كايري ايرفينغ (29) اخطأ تسديدة قبل 2.5 ثانية. هاربر 21، كاسل 17 و10 ارتدادات، فوكس 10. مارشال 22، واشنطن 21، فلاغ 19. سبيرز 6-2. كافالييرز 4-4 بعد خسارة 124-116 في اوكلاهوما سيتي."
            ]
        }
    },
    "atp-paris-masters-2026-shelton-beats-paul-first-bercy-semi": {
        "fr": {
            "title": "Rolex Paris Masters QF : Ben Shelton bat Tommy Paul 6-4, 4-6, 6-3 et rejoint sa premiere demi a Bercy",
            "subtitle": "Dix-neuf aces en 1h46. La course de Paul vers Turin s'arrete. Frances Tiafoe est qualifie pour les ATP Finals.",
            "excerpt": "Tete de serie numero 3, Ben Shelton a battu Tommy Paul 6-4, 4-6, 6-3 vendredi a l'Accor Arena.",
            "body": [
                "Ben Shelton a battu Tommy Paul 6-4, 4-6, 6-3 vendredi 6 novembre au Rolex Paris Masters. L'ATP recense 19 aces pour Shelton, 7 pour Paul, deux balles de break converties sur quatre, et 1h46 de jeu. Shelton a gagne 81 points sur 154.",
                "C'est sa premiere demi a Bercy, le premier Americain dans le dernier carre ici depuis Jack Sock et John Isner en 2017. Tiafoe valide sa premiere qualification pour Turin. Zverev, tete de serie numero 1, a perdu au 3e tour contre Musetti 7-6(5), 6-2 et n'est pas dans ce quart."
            ]
        },
        "es": {
            "title": "Rolex Paris Masters CF: Ben Shelton vence a Tommy Paul 6-4, 4-6, 6-3 y alcanza su primera semifinal en Bercy",
            "subtitle": "Diecinueve aces en 1h46. Paul queda fuera de Turin. Frances Tiafoe se clasifica para las ATP Finals.",
            "excerpt": "El tercer cabeza de serie Ben Shelton gano 6-4, 4-6, 6-3 a Tommy Paul el viernes en el Accor Arena.",
            "body": [
                "Ben Shelton vencio a Tommy Paul 6-4, 4-6, 6-3 el viernes 6 de noviembre en el Rolex Paris Masters. La ATP anota 19 aces de Shelton, 7 de Paul, dos breaks de cuatro y 1h46. Shelton gano 81 de 154 puntos.",
                "Es su primera semifinal en Bercy, el primer estadounidense en semifinales aqui desde Jack Sock y John Isner en 2017. Tiafoe confirma su primer billete a Turin. Zverev, numero 1, cayo en octavos ante Musetti 7-6(5), 6-2 y no esta en este cuarto."
            ]
        },
        "de": {
            "title": "Rolex Paris Masters VF: Ben Shelton schlaegt Tommy Paul 6:4, 4:6, 6:3 und steht im ersten Bercy-Halbfinale",
            "subtitle": "Neunzehn Asse in 1:46 Stunden. Pauls Turin-Jagd endet. Frances Tiafoe ist fuer die ATP Finals qualifiziert.",
            "excerpt": "Setzlisten-Drei Ben Shelton gewinnt am Freitag in der Accor Arena 6:4, 4:6, 6:3 gegen Tommy Paul.",
            "body": [
                "Ben Shelton schlug Tommy Paul am Freitag, den 6. November, beim Rolex Paris Masters 6:4, 4:6, 6:3. Die ATP zaehlt 19 Asse fuer Shelton, 7 fuer Paul, zwei Breaks aus vier Chancen und 1:46 Stunden. Shelton gewann 81 von 154 Punkten.",
                "Es ist sein erstes Halbfinale in Bercy, der erste US-Amerikaner im letzten Vierer hier seit Jack Sock und John Isner 2017. Tiafoe loest das erste Ticket nach Turin. Zverev, die Nummer 1, verlor in Runde 32 gegen Musetti 7:6(5), 6:2 und steht nicht in diesem Viertelfinale."
            ]
        },
        "it": {
            "title": "Rolex Paris Masters QF: Ben Shelton batte Tommy Paul 6-4, 4-6, 6-3 e vola in semifinale a Bercy per la prima volta",
            "subtitle": "Diciannove ace in 1h46. La corsa di Paul verso Torino si ferma. Frances Tiafoe e qualificato alle ATP Finals.",
            "excerpt": "La testa di serie n.3 Ben Shelton vince 6-4, 4-6, 6-3 contro Tommy Paul venerdi all'Accor Arena.",
            "body": [
                "Ben Shelton ha battuto Tommy Paul 6-4, 4-6, 6-3 venerdi 6 novembre al Rolex Paris Masters. L'ATP conta 19 ace di Shelton, 7 di Paul, due break su quattro e 1h46. Shelton ha vinto 81 punti su 154.",
                "E la sua prima semifinale a Bercy, il primo americano in semifinale qui da Jack Sock e John Isner nel 2017. Tiafoe conferma il primo pass per Torino. Zverev, n.1, ha perso al terzo turno con Musetti 7-6(5), 6-2 e non e in questo quarto."
            ]
        },
        "pl": {
            "title": "Rolex Paris Masters CF: Ben Shelton pokonuje Tommy'ego Paula 6:4, 4:6, 6:3 i gra pierwszy polfinal w Bercy",
            "subtitle": "Dziewietnascie asow w 1:46. Walka Paula o Turyn sie konczy. Frances Tiafoe jedzie na ATP Finals.",
            "excerpt": "Trzecia rakieta turnieju Ben Shelton wygrywa w piatek na Accor Arena 6:4, 4:6, 6:3 z Tommym Paulem.",
            "body": [
                "Ben Shelton pokonal Tommy'ego Paula 6:4, 4:6, 6:3 w piatek 6 listopada na Rolex Paris Masters. ATP notuje 19 asow Sheltona, 7 Paula, dwa breaki z czterech i 1:46 gry. Shelton wygral 81 z 154 punktow.",
                "To jego pierwszy polfinal w Bercy, pierwszy Amerykanin w ostatniej czworce tutaj od Jacka Socka i Johna Isnera w 2017. Tiafoe ma pierwszy bilet do Turynu. Zverev, lider rozstawienia, odpadl w 1/16 z Musettim 7:6(5), 6:2 i nie gra w tym cwiercfinale."
            ]
        },
        "zh": {
            "title": "巴黎大师赛四分之一决赛：谢尔顿6-4、4-6、6-3击败保罗，首次打进贝尔西四强",
            "subtitle": "1小时46分钟发出19记ACE。保罗都灵希望终结。蒂亚福锁定年终总决赛资格。",
            "excerpt": "3号种子本·谢尔顿周五在阿科尔体育馆以6-4、4-6、6-3击败汤米·保罗。",
            "body": [
                "本·谢尔顿11月6日周五在巴黎大师赛以6-4、4-6、6-3击败汤米·保罗。ATP统计谢尔顿19记ACE，保罗7记，破发4次机会抓住2次，耗时1小时46分钟。谢尔顿赢得154分中的81分。",
                "这是他首次打进贝尔西四强，也是2017年索克与伊斯内尔之后首位进入半决赛的美国人。蒂亚福锁定首次都灵资格。1号种子兹维列夫已在32强负于穆塞蒂7-6(5)、6-2，不在本场四分之一决赛。"
            ]
        },
        "ja": {
            "title": "ロレックス・パリ・マスターズ準々決勝：シェルトンがポールを6-4, 4-6, 6-3で破り初のベルシー4強",
            "subtitle": "1時間46分で19本のエース。ポールのトリノ挑戦は終了。ティアフォーがATPファイナルズ出場を決めた。",
            "excerpt": "第3シードのベン・シェルトンが金曜日、アコーアリーナでトミー・ポールを6-4, 4-6, 6-3で破った。",
            "body": [
                "ベン・シェルトンは11月6日金曜日、ロレックス・パリ・マスターズでトミー・ポールを6-4, 4-6, 6-3で破った。ATP統計ではシェルトン19エース、ポール7、ブレーク4本中2本、試合時間1時間46分。シェルトンは154ポイント中81を奪った。",
                "ベルシーでの初準決勝で、2017年のジャック・ソックとジョン・イスナー以来の米国人4強。ティアフォーは初のトリノ出場。第1シードのズベレフは3回戦でムセッティに7-6(5), 6-2で敗れており、この準々決勝にはいない。"
            ]
        },
        "ko": {
            "title": "롤렉스 파리 마스터스 8강: 셸턴, 폴을 6-4 4-6 6-3으로 꺾고 첫 베르시 4강",
            "subtitle": "1시간 46분 에이스 19개. 폴의 토리노 도전 종료. 프랜시스 티아포 ATP 파이널스 확정.",
            "excerpt": "3번 시드 벤 셸턴이 금요일 아코르 아레나에서 토미 폴을 6-4, 4-6, 6-3으로 꺾었습니다.",
            "body": [
                "벤 셸턴은 11월 6일 금요일 롤렉스 파리 마스터스에서 토미 폴을 6-4, 4-6, 6-3으로 꺾었습니다. ATP 통계는 셸턴 에이스 19개, 폴 7개, 브레이크 찬스 4개 중 2개, 경기 시간 1시간 46분. 셸턴이 154포인트 중 81점을 가져갔습니다.",
                "베르시 첫 준결승이며 2017년 잭 속·존 이스너 이후 첫 미국인 4강입니다. 티아포는 첫 토리노 티켓을 확정했습니다. 1번 시드 즈베레프는 32강에서 무세티에게 7-6(5), 6-2로 져 이번 8강에 없습니다."
            ]
        },
        "ar": {
            "title": "باريس ماسترز ربع النهائي: بن شيلتون يهزم تومي بول 6-4 و4-6 و6-3 ويبلغ نصف نهائي بيرسي لاول مرة",
            "subtitle": "تسعة عشر ايس في ساعة و46 دقيقة. سباق بول الى تورينو ينتهي. فرانسيس تيافو يتاهل الى النهائيات.",
            "excerpt": "المصنف الثالث بن شيلتون يفوز الجمعة على تومي بول 6-4 و4-6 و6-3 في اكور ارينا.",
            "body": [
                "هزم بن شيلتون تومي بول 6-4 و4-6 و6-3 الجمعة 6 نوفمبر في رولكس باريس ماسترز. ATP تسجل 19 ايس لشيلتون و7 لبول وكسرين من اربع فرص وساعة و46 دقيقة. شيلتون فاز بـ81 نقطة من 154.",
                "هذه اول نصف نهائي له في بيرسي، واول امريكي في المربع الذهبي هنا منذ جاك سوك وجون ايسنر عام 2017. تيافو يؤكد بطاقته الاولى الى تورينو. المصنف الاول زفيريف خرج في دور 32 امام موسيتي 7-6(5) و6-2 وليس في هذا الربع."
            ]
        }
    },
    "f1-sao-paulo-gp-2026-norris-leads-fp1-interlagos": {
        "fr": {
            "title": "GP de São Paulo EL1 : Lando Norris devance Kimi Antonelli et Max Verstappen a Interlagos",
            "subtitle": "Les evolutions McLaren placent Norris 0,082s devant le nouveau champion du monde. Pas de Sprint ce week-end.",
            "excerpt": "Lando Norris a tourne en 1:11.717 en essais libres 1, devant Kimi Antonelli et Max Verstappen. Qualifications samedi, course dimanche.",
            "body": [
                "Lando Norris a signe le meilleur temps des essais libres 1 vendredi 6 novembre a l'Autodromo Jose Carlos Pace en 1:11.717. Antonelli a termine a +0,082s, Verstappen a +0,236s, Hamilton a +0,324s, Russell a +0,386s.",
                "Le week-end bresilien n'a pas de Sprint : EL1 et EL2 vendredi, EL3 et qualifications samedi, course dimanche. ESPN apres Mexico : Antonelli champion a 380 pts, Verstappen 261, Hamilton 259. Constructeurs : Mercedes 630, Ferrari 504. Verstappen a gagne au Mexique devant Hamilton et Antonelli. Les temps d'EL2 ne sont pas publies."
            ]
        },
        "es": {
            "title": "GP de São Paulo EL1: Lando Norris lidera a Kimi Antonelli y Max Verstappen en Interlagos",
            "subtitle": "Las mejoras de McLaren dejan a Norris 0,082s por delante del nuevo campeon. No hay Sprint este fin de semana.",
            "excerpt": "Lando Norris giro en 1:11.717 en los libres 1, por delante de Kimi Antonelli y Max Verstappen. Clasificacion el sabado, carrera el domingo.",
            "body": [
                "Lando Norris fue el mas rapido en los libres 1 el viernes 6 de noviembre en el Autodromo Jose Carlos Pace con 1:11.717. Antonelli acabo a +0,082s, Verstappen a +0,236s, Hamilton a +0,324s, Russell a +0,386s.",
                "El fin de semana de São Paulo no tiene Sprint: EL1 y EL2 el viernes, EL3 y clasificacion el sabado, carrera el domingo. ESPN tras Mexico: Antonelli campeon con 380, Verstappen 261, Hamilton 259. Constructores: Mercedes 630, Ferrari 504. Verstappen gano en Mexico ante Hamilton y Antonelli. Los tiempos de EL2 no se publican."
            ]
        },
        "de": {
            "title": "Sao-Paulo-GP FP1: Lando Norris vor Kimi Antonelli und Max Verstappen in Interlagos",
            "subtitle": "McLaren-Updates bringen Norris 0,082s vor dem neuen Weltmeister. Kein Sprint an diesem Wochenende.",
            "excerpt": "Lando Norris faehrt in FP1 1:11.717, vor Kimi Antonelli und Max Verstappen. Qualifying samstags, Rennen sonntags.",
            "body": [
                "Lando Norris war am Freitag, den 6. November, im Autodromo Jose Carlos Pace in FP1 mit 1:11.717 Schnellster. Antonelli +0,082s, Verstappen +0,236s, Hamilton +0,324s, Russell +0,386s.",
                "Sao Paulo hat keinen Sprint: FP1 und FP2 Freitag, FP3 und Qualifying Samstag, Rennen Sonntag. ESPN nach Mexiko: Antonelli Champion mit 380, Verstappen 261, Hamilton 259. Konstrukteure: Mercedes 630, Ferrari 504. Verstappen siegte in Mexiko vor Hamilton und Antonelli. FP2-Zeiten werden nicht veroeffentlicht."
            ]
        },
        "it": {
            "title": "GP di São Paulo PL1: Lando Norris precede Kimi Antonelli e Max Verstappen a Interlagos",
            "subtitle": "Gli aggiornamenti McLaren mettono Norris a 0,082s dal nuovo campione. Niente Sprint in questo weekend.",
            "excerpt": "Lando Norris gira in 1:11.717 in prove libere 1, davanti a Kimi Antonelli e Max Verstappen. Qualifiche sabato, gara domenica.",
            "body": [
                "Lando Norris e stato il piu veloce nelle prove libere 1 venerdi 6 novembre all'Autodromo Jose Carlos Pace in 1:11.717. Antonelli a +0,082s, Verstappen a +0,236s, Hamilton a +0,324s, Russell a +0,386s.",
                "Il weekend di São Paulo non ha Sprint: PL1 e PL2 venerdi, PL3 e qualifiche sabato, gara domenica. ESPN dopo Città del Messico: Antonelli campione a 380, Verstappen 261, Hamilton 259. Costruttori: Mercedes 630, Ferrari 504. Verstappen ha vinto in Messico davanti a Hamilton e Antonelli. I tempi di PL2 non sono pubblicati."
            ]
        },
        "pl": {
            "title": "GP Sao Paulo FP1: Lando Norris przed Kimi Antonellim i Maxem Verstappenem w Interlagos",
            "subtitle": "Pakiet McLarena daje Norrisowi 0,082s przewagi nad nowym mistrzem. W ten weekend bez sprintu.",
            "excerpt": "Lando Norris pokonal Interlagos w 1:11.717 w pierwszym treningu, przed Antonellim i Verstappenem. Kwalifikacje w sobote, wyscig w niedziele.",
            "body": [
                "Lando Norris byl najszybszy w FP1 w piatek 6 listopada na Autodromo Jose Carlos Pace czasem 1:11.717. Antonelli +0,082s, Verstappen +0,236s, Hamilton +0,324s, Russell +0,386s.",
                "Weekend w Sao Paulo nie ma sprintu: FP1 i FP2 w piatek, FP3 i kwalifikacje w sobote, wyscig w niedziele. ESPN po Meksyku: Antonelli mistrz z 380 pkt, Verstappen 261, Hamilton 259. Konstruktorzy: Mercedes 630, Ferrari 504. Verstappen wygral w Meksyku przed Hamiltonem i Antonellim. Czasow FP2 nie publikujemy."
            ]
        },
        "zh": {
            "title": "圣保罗大奖赛第一次练习：诺里斯领跑安东内利与维斯塔潘",
            "subtitle": "迈凯伦升级件让诺里斯快新科世界冠军0.082秒。本周末无冲刺赛。",
            "excerpt": "兰多·诺里斯第一次练习跑出1:11.717，领先安东内利与维斯塔潘。排位赛周六，正赛周日。",
            "body": [
                "兰多·诺里斯11月6日周五在若泽·卡洛斯·帕塞赛道第一次练习以1:11.717最快。安东内利慢0.082秒，维斯塔潘0.236秒，汉密尔顿0.324秒，拉塞尔0.386秒。",
                "圣保罗站没有冲刺赛：周五FP1与FP2，周六FP3与排位赛，周日正赛。ESPN墨西哥站后积分：安东内利380分已夺冠，维斯塔潘261，汉密尔顿259。车队积分：梅赛德斯630，法拉利504。墨西哥正赛为维斯塔潘、汉密尔顿、安东内利。FP2成绩不作为完赛发布。"
            ]
        },
        "ja": {
            "title": "サンパウロGP FP1：ノリスがアントネッリとフェルスタッペンを抑えて首位",
            "subtitle": "マクラーレンのアップグレードでノリスが新王者に0.082秒差。今週末にスプリントはない。",
            "excerpt": "ランド・ノリスがFP1で1:11.717を記録し、アントネッリとフェルスタッペンを上回った。予選は土曜、決勝は日曜。",
            "body": [
                "ランド・ノリスは11月6日金曜日、アウトドローモ・ジョゼ・カルロス・パーチェのFP1で1:11.717が最速。アントネッリは+0.082秒、フェルスタッペン+0.236秒、ハミルトン+0.324秒、ラッセル+0.386秒。",
                "サンパウロ週末にスプリントはない。金曜FP1とFP2、土曜FP3と予選、日曜決勝。メキシコ後のESPN順位はアントネッリ380点でチャンピオン、フェルスタッペン261、ハミルトン259。コンストラクターズはメルセデス630、フェラーリ504。メキシコ決勝はフェルスタッペン、ハミルトン、アントネッリ。FP2のタイムは掲載しない。"
            ]
        },
        "ko": {
            "title": "상파울루 GP FP1: 노리스가 안토넬리와 베르스타펜을 제치고 1위",
            "subtitle": "맥라렌 업그레이드로 노리스가 신인 챔피언보다 0.082초 빠름. 이번 주말 스프린트 없음.",
            "excerpt": "란도 노리스가 FP1에서 1:11.717을 기록해 키미 안토넬리와 맥스 베르스타펜을 앞섰습니다. 예선은 토요일, 결승은 일요일입니다.",
            "body": [
                "란도 노리스는 11월 6일 금요일 아우토드로모 조제 카를루스 파세 FP1에서 1:11.717로 가장 빨랐습니다. 안토넬리 +0.082초, 베르스타펜 +0.236초, 해밀턴 +0.324초, 러셀 +0.386초.",
                "상파울루 주말에는 스프린트가 없습니다. 금요일 FP1·FP2, 토요일 FP3·예선, 일요일 결승. 멕시코 이후 ESPN 순위는 안토넬리 380점으로 챔피언, 베르스타펜 261, 해밀턴 259. 컨스트럭터는 메르세데스 630, 페라리 504. 멕시코 결승은 베르스타펜, 해밀턴, 안토넬리. FP2 기록은 게시하지 않습니다."
            ]
        },
        "ar": {
            "title": "جائزة ساو باولو الحصة الاولى: لاندو نوريس يتقدم على كيمي انطونيلي وماكس فيرستابن في انترلاغوس",
            "subtitle": "تحديثات مكلارين تضع نوريس امام البطل الجديد بفارق 0.082 ثانية. لا سباق قصير هذا الاسبوع.",
            "excerpt": "لاندو نوريس يسجل 1:11.717 في الحصة الاولى امام انطونيلي وفيرستابن. التصفيات السبت والسباق الاحد.",
            "body": [
                "كان لاندو نوريس الاسرع في الحصة الاولى الجمعة 6 نوفمبر في اوتودرومو خوسيه كارلوس باسي بزمن 1:11.717. انطونيلي +0.082ث، فيرستابن +0.236ث، هاميلتون +0.324ث، راسل +0.386ث.",
                "لا سباق قصير في ساو باولو: الحصتان الجمعة، الحصة الثالثة والتصفيات السبت، السباق الاحد. ESPN بعد المكسيك: انطونيلي بطلا بـ380 نقطة، فيرستابن 261، هاميلتون 259. الصانعون: مرسيدس 630، فيراري 504. فيرستابن فاز في المكسيك امام هاميلتون وانطونيلي. ازمنة الحصة الثانية غير منشورة."
            ]
        }
    },
    "pga-tour-wwt-championship-2026-round1-chris-kirk-63": {
        "fr": {
            "title": "WWT Championship 1er tour : Chris Kirk signe un 63 sans bogey et mene d'un coup a El Cardonal",
            "subtitle": "110e de la FedExCup Fall, il touche tous les fairways. Dunlap et Blair a 64. Bourse de 6 millions de dollars.",
            "excerpt": "Chris Kirk a rentre un 63 sans bogey jeudi pour mener le World Wide Technology Championship apres le premier tour a Los Cabos.",
            "body": [
                "Chris Kirk a signe un 63 sans bogey jeudi 5 novembre a El Cardonal at Diamante (par 72, 7452 yards). L'Associated Press indique qu'il a touche tous les fairways et rate un seul green. Nick Dunlap et Zac Blair ont joue 64. Cinq joueurs a 65 : Pavon, Hall, Montgomery, Hirata et Ben James.",
                "La bourse est de 6 millions de dollars. Kirk est autour de la 110e place de la FedExCup Fall avec trois tournois pour rentrer dans le top 100 et garder une carte 2027. Le deuxieme tour vendredi etait en cours et n'est pas publie comme un classement 36 trous termine."
            ]
        },
        "es": {
            "title": "WWT Championship R1: Chris Kirk firma un 63 sin bogeys y lidera de un golpe en El Cardonal",
            "subtitle": "110o en el FedExCup Fall, pega todos los calles. Dunlap y Blair con 64. Bote de 6 millones de dolares.",
            "excerpt": "Chris Kirk firmo un 63 sin bogeys el jueves para liderar el World Wide Technology Championship tras la primera ronda en Los Cabos.",
            "body": [
                "Chris Kirk firmo un 63 sin bogeys el jueves 5 de noviembre en El Cardonal at Diamante (par 72, 7452 yardas). Associated Press dice que acerto todos los calles y fallo un solo green. Nick Dunlap y Zac Blair hicieron 64. Cinco jugadores a 65: Pavon, Hall, Montgomery, Hirata y Ben James.",
                "El bote es de 6 millones de dolares. Kirk ronda el puesto 110 del FedExCup Fall con tres torneos para meterse en el top 100 y conservar tarjeta 2027. La segunda ronda del viernes estaba en juego y no se publica como tabla cerrada de 36 hoyos."
            ]
        },
        "de": {
            "title": "WWT Championship Runde 1: Chris Kirk spielt ein bogeyfreies 63 und fuehrt um einen Schlag in El Cardonal",
            "subtitle": "Rang 110 in der FedExCup Fall, jedes Fairway getroffen. Dunlap und Blair mit 64. Preisgeld 6 Millionen Dollar.",
            "excerpt": "Chris Kirk spielt am Donnerstag ein bogeyfreies 63 und fuehrt die World Wide Technology Championship nach Runde eins in Los Cabos an.",
            "body": [
                "Chris Kirk spielte am Donnerstag, den 5. November, in El Cardonal at Diamante (Par 72, 7452 Yards) ein bogeyfreies 63. Associated Press schreibt, er traf jedes Fairway und verfehlte nur ein Green. Nick Dunlap und Zac Blair kamen auf 64. Fuenf Spieler mit 65: Pavon, Hall, Montgomery, Hirata und Ben James.",
                "Das Preisgeld betraegt 6 Millionen Dollar. Kirk liegt um Platz 110 der FedExCup Fall, drei Turniere bleiben fuer Top 100 und die Karte 2027. Runde zwei am Freitag lief noch und wird nicht als fertiges 36-Loecher-Board veroeffentlicht."
            ]
        },
        "it": {
            "title": "WWT Championship 1o giro: Chris Kirk chiude 63 senza bogey e guida di un colpo a El Cardonal",
            "subtitle": "110o nella FedExCup Fall, centra tutti i fairway. Dunlap e Blair a 64. Montepremi 6 milioni di dollari.",
            "excerpt": "Chris Kirk firma un 63 senza bogey giovedi e guida il World Wide Technology Championship dopo il primo giro a Los Cabos.",
            "body": [
                "Chris Kirk ha chiuso 63 senza bogey giovedi 5 novembre a El Cardonal at Diamante (par 72, 7452 iarde). Associated Press scrive che ha preso tutti i fairway e sbagliato un solo green. Nick Dunlap e Zac Blair hanno fatto 64. Cinque giocatori a 65: Pavon, Hall, Montgomery, Hirata e Ben James.",
                "Il montepremi e di 6 milioni di dollari. Kirk e intorno alla 110a piazza della FedExCup Fall con tre tornei per entrare nella top 100 e tenere la card 2027. Il secondo giro di venerdi era in corso e non e pubblicato come classifica chiusa a 36 buche."
            ]
        },
        "pl": {
            "title": "WWT Championship runda 1: Chris Kirk gra 63 bez bogeya i prowadzi o uderzenie w El Cardonal",
            "subtitle": "110. w FedExCup Fall, trafia wszystkie fairwaye. Dunlap i Blair z 64. Pula 6 milionow dolarow.",
            "excerpt": "Chris Kirk zagral w czwartek 63 bez bogeya i prowadzi po pierwszej rundzie World Wide Technology Championship w Los Cabos.",
            "body": [
                "Chris Kirk zagral 63 bez bogeya w czwartek 5 listopada w El Cardonal at Diamante (par 72, 7452 jardy). Associated Press pisze, ze trafil wszystkie fairwaye i spudlowal tylko jeden green. Nick Dunlap i Zac Blair mieli 64. Pieciu zawodnikow z 65: Pavon, Hall, Montgomery, Hirata i Ben James.",
                "Pula nagród to 6 milionow dolarow. Kirk jest okolo 110. w FedExCup Fall i ma trzy turnieje, by wejsc do top 100 i zatrzymac karte na 2027. Druga runda w piatek trwała i nie jest publikowana jako zamknieta tabela po 36 dołkach."
            ]
        },
        "zh": {
            "title": "WWT锦标赛第一轮：柯克交出无柏忌63杆并领先一杆",
            "subtitle": "秋季系列约第110位，开球全部上球道。邓拉普与布莱尔64杆。奖金600万美元。",
            "excerpt": "克里斯·柯克周四打出无柏忌63杆，在洛斯卡沃斯WWT锦标赛第一轮结束后领先。",
            "body": [
                "克里斯·柯克11月5日周四在钻石卡多纳尔（标准杆72，7452码）打出无柏忌63杆。美联社称他开球全部上球道，仅错过一个果岭。尼克·邓拉普与扎克·布莱尔64杆。65杆并列第四：帕冯、霍尔、蒙哥马利、平田与本·詹姆斯。",
                "奖金为600万美元。柯克在秋季系列约排第110，还剩三场赛事需进入前100以保住2027年完整卡。周五第二轮进行中，不作为36洞完赛榜发布。"
            ]
        },
        "ja": {
            "title": "WWT選手権第1ラウンド：カークがボギーなし63で1打差首位",
            "subtitle": "フェデックスカップ・フォール約110位。全フェアウェイキープ。ダンラップとブレアは64。賞金600万ドル。",
            "excerpt": "クリス・カークが木曜日にボギーなし63を記録し、ロスカボスのWWT選手権第1ラウンドを終えて首位に立った。",
            "body": [
                "クリス・カークは11月5日木曜日、エル・カルドナル・アット・ディアマンテ（パー72、7452ヤード）でボギーなし63。APは全フェアウェイを捉え、グリーンを外したのは1つと報じた。ニック・ダンラップとザック・ブレアは64。65はパボン、ホール、モンゴメリー、平田、ベン・ジェームズの5人。",
                "賞金総額は600万ドル。カークはフェデックスカップ・フォールで約110位、残り3試合でトップ100に入り2027年のフルカードを守る必要がある。金曜の第2ラウンドは進行中で、36ホール終了の確定ボードとしては掲載しない。"
            ]
        },
        "ko": {
            "title": "WWT 챔피언십 1라운드: 커크가 보기 없는 63타로 1타 선두",
            "subtitle": "페덱스컵 폴 약 110위, 페어웨이 전부 적중. 던랩과 블레어 64. 상금 600만 달러.",
            "excerpt": "크리스 커크가 목요일 보기 없는 63타를 쳐 로스카보스 WWT 챔피언십 1라운드 선두에 올랐습니다.",
            "body": [
                "크리스 커크는 11월 5일 목요일 엘 카르도날 앳 디아만테(파 72, 7452야드)에서 보기 없는 63타를 쳤습니다. AP는 페어웨이를 모두 맞히고 그린을 한 번만 놓쳤다고 전했습니다. 닉 던랩과 잭 블레어는 64. 65타는 파봉, 홀, 몽고메리, 히라타, 벤 제임스 다섯 명입니다.",
                "상금은 600만 달러입니다. 커크는 페덱스컵 폴 약 110위로, 남은 세 대회에서 톱100에 들어 2027년 풀 카드를 지켜야 합니다. 금요일 2라운드는 진행 중이며 36홀 확정 리더보드로 올리지 않습니다."
            ]
        },
        "ar": {
            "title": "بطولة WWT الجولة الاولى: كريس كيرك يسجل 63 دون بوجي ويتقدم بضربة في ال كاردونال",
            "subtitle": "المركز 110 تقريبا في فيدكس كاب الخريف، يصيب كل الممرات. دنلاب وبلير 64. الجائزة 6 ملايين دولار.",
            "excerpt": "كريس كيرك يسجل 63 دون بوجي الخميس ويتصدر بطولة وورلد وايد تكنولوجي بعد الجولة الاولى في لوس كابوس.",
            "body": [
                "سجل كريس كيرك 63 دون بوجي الخميس 5 نوفمبر في ال كاردونال ات ديامانتي (بار 72، 7452 ياردة). اسوشيتد برس تقول انه اصاب كل الممرات واخطأ جرينا واحدا. نيك دنلاب وزاك بلير سجلا 64. خمسة لاعبين عند 65: بافون وهول ومونتغمري وهيراتا وبن جيمس.",
                "الجائزة 6 ملايين دولار. كيرك حول المركز 110 في فيدكس كاب الخريف مع ثلاثة بطولات للدخول الى المئة الاولى والاحتفاظ ببطاقة 2027. الجولة الثانية الجمعة كانت جارية ولم تنشر كجدول مغلق بعد 36 حفرة."
            ]
        }
    },
    "ucl-matchday4-haaland-winner-city-edge-leipzig-3-2-2026": {
        "fr": {
            "title": "C1 J4 : Haaland offre le succes a Manchester City 3-2 a Leipzig",
            "subtitle": "Le capitaine conclut un centre d'Anderson a la 78e apres deux egalisations de Leipzig. City 3-1, 7e de la phase de ligue.",
            "excerpt": "Erling Haaland a inscrit le but de la victoire a la 78e minute, et Manchester City a battu le RB Leipzig 3-2 mercredi.",
            "body": [
                "Manchester City a battu le RB Leipzig 3-2 mercredi 4 novembre a la Red Bull Arena. Castello Lukeba a marque contre son camp a la 37e. Ridle Baku a egalise a la 49e. Enzo Fernandez a recouvert de la tete a la 58e sur un centre d'Iliman Ndiaye. Antonio Nusa a egalise a la 61e sur une passe de Christopher Nkunku. Haaland a conclu un centre bas d'Elliot Anderson a la 78e.",
                "City est 3-1 dans la phase de ligue, 7e. La Premier League apres la 9e journee (BBC, NBC, 6 novembre) : Arsenal 24, City 21, Brighton 19. Everton-Coventry vendredi 6 novembre a 20h00 GMT n'est pas publie avec un score."
            ]
        },
        "es": {
            "title": "UCL J4: Haaland da el 3-2 al Manchester City en Leipzig",
            "subtitle": "El capitan remata un centro de Anderson en el 78 tras dos empates de Leipzig. City 3-1, septimo en la fase de liga.",
            "excerpt": "Erling Haaland marco el gol de la victoria en el minuto 78 y el Manchester City gano 3-2 al RB Leipzig el miercoles.",
            "body": [
                "El Manchester City gano 3-2 al RB Leipzig el miercoles 4 de noviembre en la Red Bull Arena. Castello Lukeba se hizo un gol en propia en el 37. Ridle Baku empato en el 49. Enzo Fernandez cabeceó en el 58 un centro de Iliman Ndiaye. Antonio Nusa empato en el 61 tras un pase de Christopher Nkunku. Haaland empujo un centro raso de Elliot Anderson en el 78.",
                "City esta 3-1 en la fase de liga, septimo. Premier League tras la jornada 9 (BBC, NBC, 6 de noviembre): Arsenal 24, City 21, Brighton 19. Everton-Coventry el viernes 6 de noviembre a las 20:00 GMT no se publica con marcador."
            ]
        },
        "de": {
            "title": "CL MD4: Haaland entscheidet 3:2 fuer Manchester City in Leipzig",
            "subtitle": "Der Kapitaen verwertet Andersons Hereingabe in der 78. nach zwei Leipzig-Ausgleichen. City 3-1, Rang 7 in der Liga-Phase.",
            "excerpt": "Erling Haaland trifft in der 78. Minute zum Sieg, Manchester City gewinnt am Mittwoch 3:2 gegen RB Leipzig.",
            "body": [
                "Manchester City schlug RB Leipzig am Mittwoch, den 4. November, in der Red Bull Arena mit 3:2. Castello Lukeba unterlief in der 37. ein Eigentor. Ridle Baku glich in der 49. aus. Enzo Fernandez koepfte in der 58. nach einer Flanke von Iliman Ndiaye. Antonio Nusa glich in der 61. nach einem Pass von Christopher Nkunku aus. Haaland schob Andersons flache Hereingabe in der 78. ein.",
                "City steht 3-1 in der Liga-Phase auf Rang 7. Premier League nach dem 9. Spieltag (BBC, NBC, 6. November): Arsenal 24, City 21, Brighton 19. Everton gegen Coventry am Freitag, 6. November, 20:00 GMT wird ohne Ergebnis veroeffentlicht."
            ]
        },
        "it": {
            "title": "UCL GS4: Haaland decide 3-2 per il Manchester City a Lipsia",
            "subtitle": "Il capitano spinge un cross di Anderson al 78' dopo due pareggi del Lipsia. City 3-1, settimo nella fase campionato.",
            "excerpt": "Erling Haaland segna il gol della vittoria al 78' e il Manchester City batte il RB Lipsia 3-2 mercoledi.",
            "body": [
                "Il Manchester City ha battuto il RB Lipsia 3-2 mercoledi 4 novembre alla Red Bull Arena. Castello Lukeba ha segnato un autogol al 37'. Ridle Baku ha pareggiato al 49'. Enzo Fernandez ha sfondata di testa al 58' su cross di Iliman Ndiaye. Antonio Nusa ha pareggiato al 61' su assist di Christopher Nkunku. Haaland ha ribattuto un cross basso di Elliot Anderson al 78'.",
                "City e 3-1 nella fase campionato, settimo. Premier League dopo la 9a giornata (BBC, NBC, 6 novembre): Arsenal 24, City 21, Brighton 19. Everton-Coventry venerdi 6 novembre alle 20:00 GMT non e pubblicato con un punteggio."
            ]
        },
        "pl": {
            "title": "LM kolejka 4: Haaland daje City wygrana 3:2 w Lipsku",
            "subtitle": "Kapitan domyka dośrodkowanie Andersona w 78. minucie po dwoch remisach Lipska. City 3-1, 7. miejsce w fazie ligowej.",
            "excerpt": "Erling Haaland strzelil gola zwyciestwa w 78. minucie, a Manchester City pokonal RB Lipsk 3:2 w srode.",
            "body": [
                "Manchester City wygral z RB Lipsk 3:2 w srode 4 listopada na Red Bull Arena. Castello Lukeba strzelil samoboja w 37. Ridle Baku wyroownal w 49. Enzo Fernandez glowką w 58. po dośrodkowaniu Ilimana Ndiaye. Antonio Nusa wyroownal w 61. po podaniu Christophera Nkunku. Haaland domknal plaskie dośrodkowanie Elliota Andersona w 78.",
                "City ma 3-1 w fazie ligowej i jest 7. Premier League po 9. kolejce (BBC, NBC, 6 listopada): Arsenal 24, City 21, Brighton 19. Everton-Coventry w piatek 6 listopada o 20:00 GMT nie ma wyniku na tym desku."
            ]
        },
        "zh": {
            "title": "欧冠联赛阶段第4轮：哈兰德绝杀助曼城3-2战胜莱比锡",
            "subtitle": "队长在第78分钟推射安德森传中。莱比锡两度扳平。曼城联赛阶段3胜1负排第7。",
            "excerpt": "埃尔林·哈兰德第78分钟打入制胜球，曼城周三3-2客胜莱比锡红牛。",
            "body": [
                "曼城11月4日周三在红牛竞技场3-2击败莱比锡红牛。卡斯泰洛·卢克巴第37分钟乌龙。里德勒·巴库第49分钟扳平。恩佐·费尔南德斯第58分钟头球打进恩迪亚耶传中。安东尼奥·努萨第61分钟接恩昆库传球再平。哈兰德第78分钟推射埃利奥特·安德森低平传中。",
                "曼城联赛阶段3胜1负排第7。11月6日BBC与NBC英超第9轮积分：阿森纳24分，曼城21分，布莱顿19分。11月6日周五20:00 GMT埃弗顿对考文垂尚未完赛，本台不发布比分。"
            ]
        },
        "ja": {
            "title": "CL第4節：ハーランドが決勝点、マンチェスター・シティがライプツィヒに3-2勝利",
            "subtitle": "主将が78分にアンダーソンのクロスを押し込む。ライプツィヒは2度追いつく。シティはリーグフェーズ3勝1敗で7位。",
            "excerpt": "エルリング・ハーランドが78分に決勝点を決め、マンチェスター・シティが水曜日にRBライプツィヒを3-2で破った。",
            "body": [
                "マンチェスター・シティは11月4日水曜日、レッドブルアリーナでRBライプツィヒを3-2で破った。カステロ・ルケバが37分にオウンゴール。リドレ・バクが49分に同点。エンソ・フェルナンデスが58分にイリマン・エンディアエのクロスをヘッド。アントニオ・ヌサが61分にクリストファー・エンクンクのパスから再同点。ハーランドが78分にエリオット・アンダーソンの低いクロスを押し込んだ。",
                "シティはリーグフェーズ3勝1敗で7位。11月6日のBBCとNBCによるプレミア第9節後の順位はアーセナル24、シティ21、ブライトン19。11月6日金曜20:00 GMTのエバートン対コヴェントリーは未消化のためスコアは掲載しない。"
            ]
        },
        "ko": {
            "title": "UCL 4차전: 홀란드 결승골로 맨시티가 라이프치히에 3-2 승리",
            "subtitle": "주장이 78분 앤더슨 크로스를 밀어 넣었다. 라이프치히는 두 번 따라붙었다. 시티는 리그 페이즈 3승 1패 7위.",
            "excerpt": "엘링 홀란드가 78분 결승골을 넣었고 맨체스터 시티가 수요일 RB 라이프치히를 3-2로 꺾었습니다.",
            "body": [
                "맨체스터 시티는 11월 4일 수요일 레드불 아레나에서 RB 라이프치히를 3-2로 꺾었습니다. 카스텔로 루케바가 37분 자책골. 리들레 바쿠가 49분 동점. 엔소 페르난데스가 58분 일리만 은디아예 크로스를 헤더. 안토니오 누사가 61분 크리스토퍼 은쿤쿠 패스로 다시 동점. 홀란드가 78분 엘리엇 앤더슨의 낮은 크로스를 밀어 넣었습니다.",
                "시티는 리그 페이즈 3승 1패로 7위입니다. 11월 6일 BBC·NBC 프리미어리그 9라운드 후 순위는 아스널 24, 시티 21, 브라이턴 19. 11월 6일 금요일 20:00 GMT 에버턴 대 코번트리는 미개최로 점수를 올리지 않습니다."
            ]
        },
        "ar": {
            "title": "دوري الابطال الجولة 4: هالاند يحسم 3-2 لمانشستر سيتي في لايبزيغ",
            "subtitle": "القائد يدفع عرضية اندرسون في الدقيقة 78 بعد تعادلين للايبزيغ. سيتي 3-1 في المركز السابع.",
            "excerpt": "ارلينغ هالاند يسجل هدف الفوز في الدقيقة 78 ومانشستر سيتي يفوز 3-2 على لايبزيغ الاربعاء.",
            "body": [
                "فاز مانشستر سيتي على ار بي لايبزيغ 3-2 الاربعاء 4 نوفمبر في ريد بول ارينا. سجل كاستيلو لوكبا في مرماه في الدقيقة 37. عادل ريدل باكو في 49. سجل انزو فرنانديز راسية في 58 من عرضية ايليمان ندياي. عادل انطونيو نوسا في 61 من تمريرة كريستوفر نكونكو. دفع هالاند عرضية اليوت اندرسون المنخفضة في 78.",
                "سيتي 3-1 في مرحلة الدوري في المركز السابع. جدول البريميرليغ بعد الجولة 9 (بي بي سي وNBC في 6 نوفمبر): ارسنال 24، سيتي 21، برايتون 19. مباراة ايفرتون ضد كوفنتري الجمعة 6 نوفمبر الساعة 20:00 GMT لم تلعب ولا تنشر بنتيجة."
            ]
        }
    },
}

for slug, langs in NOV06_STORIES.items():
    assert len(langs) == 9, f"{slug} missing langs: {list(langs.keys())}"
    for lang in ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        trans = langs[lang]
        for field in ["title", "subtitle", "excerpt", "body"]:
            val = trans[field]
            items = val if isinstance(val, list) else [val]
            for i, item in enumerate(items):
                if "—" in item:
                    raise SystemExit(f"Em-dash in {slug} {lang} {field}: {item}")
                if "--" in item:
                    raise SystemExit(f"Double-hyphen in {slug} {lang} {field}: {item}")

print("All November 6 story translations validated: 0 em-dashes and 0 double-hyphens.")

snippet_parts = []
for slug, langs in NOV06_STORIES.items():
    snippet_parts.append(f"{json.dumps(slug)}: {json.dumps(langs, ensure_ascii=False, indent=2)},")
snippet = "\n".join(snippet_parts) + "\n"

stories_file = os.path.join(os.path.dirname(__file__), "../../frontend/src/i18n/stories.ts")
with open(stories_file, "r", encoding="utf-8") as f:
    content = f.read()

target = "export const STORY_I18N: Record<string, LocMap> = {\n"
assert target in content, "Target line not found in stories.ts"
# Drop leftover fabricated Nov 6 sprint i18n if present
if '"f1-sao-paulo-gp-2026-piastri-edges-norris-sprint-pole-interlagos"' in content:
    print("WARN: fabricated piastri i18n still in stories.ts")

new_content = content.replace(target, target + snippet, 1)
with open(stories_file, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Successfully injected November 6 translations into frontend/src/i18n/stories.ts")
