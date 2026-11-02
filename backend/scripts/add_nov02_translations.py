# -*- coding: utf-8 -*-
"""
Add 2 November 2026 translations for all 6 stories across 9 languages.
"""
import json
import re
import os

NOV02_STORIES = {
    "nfl-week8-mnf-steelers-beat-giants-26-18-watt-austin-2026": {
        "fr": {
            "title": "NFL Semaine 8 MNF : Les Steelers domptent les Giants 26-18 grace a Calvin Austin et une defense de fer",
            "subtitle": "Calvin Austin III signe deux touchdowns au troisieme quart-temps et T.J. Watt etouffe New York pour placer Pittsburgh en tete de l'AFC Nord a 6-2.",
            "excerpt": "Les Steelers de Pittsburgh ont pris les commandes de l'AFC Nord lundi soir en dominant les Giants 26-18 au Acrisure Stadium.",
            "body": [
                "Les Steelers de Pittsburgh ont confirme leur statut d'equipe redoutable en prime time lundi 2 novembre, s'imposant 26-18 face aux Giants de New York devant 67 430 spectateurs au Acrisure Stadium. L'equipe de Mike Tomlin passe a 6-2 et prend seule la tete de l'AFC Nord.",
                "Le receveur Calvin Austin III a fait basculer la rencontre au troisieme quart avec un spectaculaire retour de coup de pied de 73 yards pour un touchdown, suivi d'une reception de 29 yards signee Russell Wilson (278 yards, 0 interception). En defense, T.J. Watt a totalise 2 sacks et provoque un fumble decisif pour repousser l'assaut final new-yorkais."
            ]
        },
        "es": {
            "title": "NFL Semana 8 MNF: Los Steelers doblegan 26-18 a los Giants impulsados por Calvin Austin y una defensa feroz",
            "subtitle": "Calvin Austin III anota en un retorno de 73 yardas y en una recepcion de 29 yardas mientras T.J. Watt lidera a Pittsburgh a colocarse 6-2.",
            "excerpt": "Los Pittsburgh Steelers se consolidaron como lideres en solitario de la AFC Norte al batir 26-18 a los New York Giants en Monday Night Football.",
            "body": [
                "Los Pittsburgh Steelers dieron un golpe sobre la mesa este lunes 2 de noviembre al vencer 26-18 a los New York Giants ante 67.430 hinchas en el Acrisure Stadium. La victoria coloca al equipo de Mike Tomlin con marca de 6-2 como puntero solitario de la division AFC Norte.",
                "Calvin Austin III dinamito el choque en el tercer cuarto con una espectacular escapada de 73 yardas tras patada de despeje y una recepcion anotadora de 29 yardas enviada por Russell Wilson. La defensa acerera completo la faena con dos capturas de T.J. Watt y una intercepcion del novato Beanie Bishop Jr. en el tramo final."
            ]
        },
        "de": {
            "title": "NFL Woche 8 MNF: Steelers dominieren Giants mit 26:18 dank Doppelpack von Calvin Austin und starker Defense",
            "subtitle": "Calvin Austin III Glaenzt mit 73-Yard-Punt-Return und 29-Yard-Touchdown; T.J. Watt fuehrt Pittsburgh zu Platz eins in der AFC North.",
            "excerpt": "Die Pittsburgh Steelers sicherten sich am Montagabend mit einem 26:18-Sieg ueber die New York Giants die alleinige Tabellenfuehrung der AFC North.",
            "body": [
                "Die Pittsburgh Steelers setzten am Montagabend, den 2. November, vor 67.430 Zuschauern im Acrisure Stadium ein Ausrufezeichen und schlugen die New York Giants mit 26:18. Das Team von Head Coach Mike Tomlin verbesserte seine Bilanz auf 6-2.",
                "Matchwinner war Calvin Austin III, der im dritten Viertel erst einen Punt ueber 73 Yards in die Endzone trug und wenig spaeter einen 29-Yard-Touchdown-Pass von Quarterback Russell Wilson fing. In der Abwehr glaenzte Superstar T.J. Watt mit zwei Sacks und einem eroberten Fumble."
            ]
        },
        "it": {
            "title": "NFL Week 8 MNF: Gli Steelers piegano i Giants 26-18 trascinati da Calvin Austin e da una difesa soffocante",
            "subtitle": "Due touchdown da urlo per Calvin Austin III e due sack di T.J. Watt lanciano Pittsburgh in vetta all'AFC North con un record di 6-2.",
            "excerpt": "I Pittsburgh Steelers conquistano il primato solitario nell'AFC North superando i New York Giants 26-18 nel Monday Night Football.",
            "body": [
                "Serata di grande football all'Acrisure Stadium lunedi 2 novembre, dove 67.430 spettatori hanno spinto i Pittsburgh Steelers al successo per 26-18 sui New York Giants. La formazione di Mike Tomlin sale a 6-2 conquistando il comando solitario della divisione.",
                "Il protagonista assoluto e stato il ricevitore Calvin Austin III, autore nel terzo quarto di un travolgente ritorno di punt da 73 yard e di un touchdown da 29 yard su lancio perfetto di Russell Wilson. In difesa T.J. Watt ha fatto la differenza con 2 sack e un fumble forzato nei momenti chiave."
            ]
        },
        "pl": {
            "title": "NFL Tydzien 8 MNF: Steelers pokonuja Giants 26:18 dzieki popisom Calvina Austina i zelaznej defensywie",
            "subtitle": "Calvin Austin III zdobywa dwa przylozenia w trzeciej kwarcie, a T.J. Watt prowadzi Pittsburgh na fotel lidera AFC North z bilansem 6-2.",
            "excerpt": "Pittsburgh Steelers objeli samodzielne prowadzenie w dywizji AFC North, wygrywajac w poniedzialek z New York Giants 26:18.",
            "body": [
                "Pittsburgh Steelers potwierdzili wysoka forme w prime-time, pokonujac w poniedzialek 2 listopada New York Giants 26:18 na oczach 67 430 fanow na Acrisure Stadium. Druzyna Mike'a Tomlina awansowala na bilans 6-2.",
                "Bohaterem nocy zostal Calvin Austin III, ktory popisal sie 73-jardowym returnem na przylozenie z puntu oraz 29-jardowa zlapana pilka w endzone od Russella Wilsona. W defensywie rzadzil T.J. Watt, notujac 2 sacki i wymuszone fumble."
            ]
        },
        "zh": {
            "title": "NFL第8周周一夜赛：奥斯汀连下两城防线发威，钢人26-18击溃巨人领跑美北",
            "subtitle": "卡尔文·奥斯汀上演73码弃踢回攻达阵加29码接球达阵，瓦特两记擒杀力助匹兹堡战绩升至6胜2负。",
            "excerpt": "匹兹堡钢人队周一在主场阿克里苏尔球场26-18力克纽约巨人队，战绩提升至6胜2负独占美联北区榜首。",
            "body": [
                "11月2日周一晚间，匹兹堡钢人队在67430名现场球迷见证下，坐镇阿克里苏尔球场以26-18战胜纽约巨人队，凭借这场关键胜利以6胜2负的战绩独占美联北区第一位。",
                "外接手卡尔文·奥斯汀在第三节爆发神威，先是完成一记震撼全场的73码弃踢回攻达阵，随后又接四分卫拉塞尔·威尔逊29码精准传球完成本场第二记达阵。防守端超级巨星T.J.瓦特贡献2次擒杀与1次制造掉球，彻底击碎了巨人的反扑希望。"
            ]
        },
        "ja": {
            "title": "NFL第8週MNF：スティーラーズがオースティンの2TDと強固な守備でジャイアンツを26-18で破り地区首位浮上",
            "subtitle": "カルビン・オースティンが73ヤードのリターンTDと29ヤードのレシーブTDを記録し、T.J.ワットが守備陣を牽引。",
            "excerpt": "ピッツバーグ・スティーラーズがマンデーナイトでニューヨーク・ジャイアンツを26-18で退け、6勝2敗でAFC北地区単独首位に立ちました。",
            "body": [
                "11月2日月曜日、アクリシュア・スタジアムで行われたマンデーナイトフットボールで、ピッツバーグ・スティーラーズがニューヨーク・ジャイアンツを26-18で下しました。マイク・トムリン率いるスティーラーズは通算6勝2敗としています。",
                "第3クォーターにカルビン・オースティン3世が圧巻の73ヤードパントリターンタッチダウンを決めると、直後にもラッセル・ウィルソンからの29ヤードパスをキャッチして追加点を奪取。守備ではT.J.ワットが2サックをマークし、相手の反撃を封じ込めました。"
            ]
        },
        "ko": {
            "title": "NFL 8주차 MNF: 스틸러스, 캘빈 오스틴의 2TD 대폭발 앞세워 자이언츠 26-18 격파하고 AFC 북부 선두",
            "subtitle": "캘빈 오스틴 73야드 펀트 리턴 및 29야드 패스 리시빙 터치다운 작렬; T.J. 와트 2색 맹활약으로 6승 2패 도약.",
            "excerpt": "피츠버그 스틸러스가 먼데이 나이트 풋볼에서 뉴욕 자이언츠를 26-18로 꺾고 6승 2패로 AFC 북부지구 단독 1위에 올랐습니다.",
            "body": [
                "11월 2일 월요일 아크리슈어 스타디움에서 열린 먼데이 나이트 풋볼 경기에서 피츠버그 스틸러스가 뉴욕 자이언츠를 26-18로 완파했습니다. 이 승리로 스틸러스는 6승 2패를 기록하며 지구 단독 선두로 올라섰습니다.",
                "와이드 리시버 캘빈 오스틴 3세가 3쿼터에 73야드 펀트 리턴 터치다운에 이어 러셀 윌슨의 29야드 패스를 받아 연속 터치다운을 기록하며 경기 흐름을 장악했습니다. 수비진에서는 에이스 T.J. 와트가 2개의 색을 기록하며 자이언츠의 막판 추격을 원천 봉쇄했습니다."
            ]
        },
        "ar": {
            "title": "دوري NFL الأسبوع 8: ستيلرز يتفوق على جاينتس 26-18 بفضل تألق كالفين أوستن ودفاع صلب",
            "subtitle": "كالفين أوستن يسجل هدفين رائعين وتي جيه وات يقود بيتسبرغ لتصدر مجموعته بسجل 6 انتصارات وهزيمتين.",
            "excerpt": "انفرد بيتسبرغ ستيلرز بصدارة مجموعته في دوري كرة القدم الأمريكية بعد فوزه المثير 26-18 على نيويورك جاينتس مساء الإثنين.",
            "body": [
                "حقق بيتسبرغ ستيلرز فوزا ثمينا بنتيجة 26-18 على ضيفه نيويورك جاينتس مساء الإثنين 2 نوفمبر على ملعب أكرسور ستاديوم أمام أكثر من 67 ألف متفرج، ليرفع رصيده إلى 6 انتصارات وهزيمتين في صدارة المجموعة.",
                "وتألق المستقبل كالفين أوستن بتسجيل هبوطين تاريخيين في الربع الثالث بعد ركضة مذهلة لمسافة 73 ياردة واستقبال كرة لمسافة 29 ياردة من راسل ويلسون. وفي الدفاع، فرض تي جيه وات سيطرته بإسقاطين حاسمين ليقود فريقه نحو حسم اللقاء."
            ]
        }
    },
    "nba-cavaliers-edge-bucks-114-113-mitchell-buzzer-beater-2026": {
        "fr": {
            "title": "NBA thriller : Donovan Mitchell crucifie les Bucks a 0,3 seconde de la fin, Cleveland toujours invaincu a 7-0",
            "subtitle": "Mitchell marque 30 points et rentre le tir de la gagne pour repondre aux 41 points de Damian Lillard dans un match d'anthologie (114-113).",
            "excerpt": "Donovan Mitchell a inscrit un shoot miraculeux sur le gong pour offrir la victoire aux Cavaliers 114-113 a Milwaukee et preserver leur invincibilite.",
            "body": [
                "Le Fiserv Forum a ete le theatre d'un match de legende lundi 2 novembre. Donovan Mitchell a reussi un panier desespere en arriere le long de la ligne de fond a 0,3 seconde du buzzer final, offrant aux Cavaliers de Cleveland une victoire magistrale 114-113 face aux Bucks de Milwaukee.",
                "Ce duel au sommet a vu Damian Lillard flamber avec 41 points dont 10 paniers a trois points, epaule par Giannis Antetokounmpo (34 points, 16 rebonds). Mais Mitchell, auteur de 30 points, a eu le dernier mot pour permettre a Cleveland de porter son bilan parfait a 7-0."
            ]
        },
        "es": {
            "title": "NBA Thriller: Donovan Mitchell encesta a 0.3 segundos del final y los invictos Cavaliers baten 114-113 a los Bucks",
            "subtitle": "Mitchell firma 30 puntos y la canasta de la victoria para frenar los 41 puntos de Damian Lillard y mantener a Cleveland con 7-0.",
            "excerpt": "Donovan Mitchell clavo una suspension agonica sobre la bocina para sellar el triunfo de los Cavaliers 114-113 ante los Bucks en Milwaukee.",
            "body": [
                "Un final para el recuerdo se vivio este lunes 2 de noviembre en el Fiserv Forum. Con 0.3 segundos por jugar, Donovan Mitchell se elevo sobre Gary Trent Jr. desde la linea de fondo para clavar una suspension magistral que dio a Cleveland la victoria 114-113 sobre Milwaukee.",
                "Damian Lillard tuvo una noche antologica con 41 puntos y 10 triples, mientras Giannis Antetokounmpo domino la pintura con 34 puntos y 16 rebotes. Sin embargo, los 30 puntos de Mitchell mantuvieron a los Cavaliers como el unico equipo invicto del Este con un arranque perfecto de 7-0."
            ]
        },
        "de": {
            "title": "NBA Thriller: Donovan Mitchell trifft 0,3 Sekunden vor Schluss, Cavaliers schlagen Bucks 114:113 und bleiben bei 7:0",
            "subtitle": "Mitchell erzielt 30 Punkte und den Game-Winner gegen Damian Lillards 41-Punkte-Gala in einem packenden Schlagabtausch.",
            "excerpt": "Mit einem sensationellen Buzzer-Beater fuehrte Donovan Mitchell die ungeschlagenen Cleveland Cavaliers zu einem dramatischen 114:113-Erfolg in Milwaukee.",
            "body": [
                "Das Fiserv Forum erlebte am Montag, den 2. November, ein Spektakel der Extraklasse. Donovan Mitchell versenkte 0,3 Sekunden vor der Schlusssirene einen schweren Wurf aus der Rueckwaertsbewegung zum 114:113-Endstand fuer die Cleveland Cavaliers gegen die Milwaukee Bucks.",
                "Damian Lillard ragte mit 41 Punkten und 10 verwandelten Dreiern fuer die Bucks heraus, unterstuetzt von Giannis Antetokounmpo mit 34 Punkten und 16 Rebounds. Mitchell konterte mit 30 Punkten und sicherte Cleveland damit den siebten Sieg im siebten Saisonspiel."
            ]
        },
        "it": {
            "title": "NBA Thriller: Donovan Mitchell gela i Bucks a 0.3 secondi dalla sirena, Cleveland resta imbattuta sul 7-0 (114-113)",
            "subtitle": "Mitchell realizza 30 punti e il canestro decisivo rispondendo ai 41 punti con 10 triple di Damian Lillard in un finale da batticuore.",
            "excerpt": "Canestro prodigioso di Donovan Mitchell a tre decimi dalla sirena: i Cavaliers espugnano Milwaukee 114-113 e conservano l'imbattibilita.",
            "body": [
                "Finale al cardiopalma al Fiserv Forum lunedi 2 novembre. Donovan Mitchell ha realizzato un canestro in fadeaway a 0.3 secondi dalla fine regalando ai Cleveland Cavaliers un pazzesco successo per 114-113 sui Milwaukee Bucks.",
                "I padroni di casa si erano affidati a un monumentale Damian Lillard da 41 punti (10 triple) e ai 34 punti con 16 rimbalzi di Giannis Antetokounmpo. Ma Mitchell, autore di 30 punti, ha piazzato il colpo del k.o. permettendo a Cleveland di confermarsi in vetta a Est con un impeccabile 7-0."
            ]
        },
        "pl": {
            "title": "NBA dreszczowiec: Donovan Mitchell trafia na 0,3 sekundy przed koncem, Cavaliers pokonuja Bucks 114:113",
            "subtitle": "Mitchell zdobywa 30 punktow i rzut meczowy, neutralizujac 41 punktow Damiana Lillarda i zapewniajac bilans 7-0.",
            "excerpt": "Niesamowity rzut Donovana Mitchella w koncowce zapewnil Cleveland Cavaliers triumf 114:113 nad Bucks i przedluzyl passe zwyciestw.",
            "body": [
                "Prawdziwy spektakl koszykowki w Fiserv Forum w poniedzialek 2 listopada. Donovan Mitchell trafil z polodleglosci na 0,3 sekundy przed syrena koncowa, dajac Cleveland Cavaliers wygrana 114:113 nad Milwaukee Bucks.",
                "Gospodarze mieli w swoich szeregach genialnego Damiana Lillarda, ktory trafil 10 trojek i rzucil 41 punktow, a Giannis Antetokounmpo dolozyl 34 punkty i 16 zbiorek. Jednak to 30 punktow Mitchella i jego zimna krew w koncowce pozwolily Cleveland zachowac status niepokonanych z bilansem 7-0."
            ]
        },
        "zh": {
            "title": "NBA焦点战：米切尔终场前0.3秒中投绝杀，骑士114-113险胜雄鹿豪取开季7连胜",
            "subtitle": "利拉德狂飙10记三分轰下41分，米切尔空砍30分后奉献致命绝杀，克利夫兰保持全胜领跑东部。",
            "excerpt": "多诺万·米切尔在终场前0.3秒命中后仰跳投绝杀，帮助骑士队客场114-113险胜雄鹿，豪取开季7连胜保持不败。",
            "body": [
                "11月2日周一晚间，密尔沃基费瑟夫球馆见证了一场载入赛季史册的绝杀对决。在全场还剩0.3秒时，克利夫兰骑士队当家球星米切尔在底线面对严防后仰跳投空心入网，帮助球队以114-113反超绝杀雄鹿队。",
                "雄鹿队双星此役火力全开，利拉德三分球15投10中狂砍41分，字母哥揽下34分16篮板的大号两双。但得到30分的米切尔在最后时刻接管了比赛，率领骑士以7胜0负的不败金身创下队史近50年来的最佳开局纪录。"
            ]
        },
        "ja": {
            "title": "NBA激闘：ミッチェルが残り0.3秒で決勝ブザービーター、無敗キャバリアーズがバックスを114-113で破る",
            "subtitle": "リラードの10本3P含む41得点に対し、ミッチェルが30得点と劇的ショットで応戦し開幕7連勝達成。",
            "excerpt": "ドノバン・ミッチェルが残り0.3秒に奇跡の決勝シュートを沈め、キャブズがバックスに114-113で競り勝ちました。",
            "body": [
                "11月2日月曜日、ファイサーブ・フォーラムで行われたNBA屈指の好カードは劇的な結末を迎えました。残り0.3秒、ドノバン・ミッチェルが高難度のフェイダウェイジャンパーを沈め、クリーブランド・キャバリアーズが114-113でミルウォーキー・バックスを下しました。",
                "バックスはデイミアン・リラードがスリーポイント10本を含む41得点、ヤニス・アデトクンボが34得点16リバウンドと躍動。しかし30得点を挙げたミッチェルが最後の最後で試合を決め、キャブズは開幕無傷の7連勝を飾りました。"
            ]
        },
        "ko": {
            "title": "NBA 명승부: 도노반 미첼 0.3초 남기고 위닝샷 작렬, 무패 캐벌리어스 벅스 114-113 제압",
            "subtitle": "데미안 릴라드의 3점 10방 41점 폭발에도 미첼이 30점과 결승 버저비터로 응수하며 클리블랜드 7연승 질주.",
            "excerpt": "도노반 미첼이 경기 종료 0.3초 전 환상적인 위닝 점퍼를 꽂아 넣으며 클리블랜드가 밀워키를 114-113으로 꺾었습니다.",
            "body": [
                "11월 2일 월요일 밀워키 파이서브 포럼에서 이번 시즌 최고의 명승부가 펼쳐졌습니다. 경기 종료 0.3초 전, 도노반 미첼이 베이스라인 페이드어웨이 슛을 깨끗하게 적중시키며 클리블랜드 캐벌리어스가 밀워키 벅스를 114-113으로 제압했습니다.",
                "밀워키는 릴라드가 3점슛 10개를 꽂으며 41점, 쿤보가 34점 16리바운드로 맹폭했으나 마지막 순간 미첼(30점)의 클러치 샷 한 방에 무릎을 꿇었습니다. 클리블랜드는 개막 7연승을 달리며 동부 1위를 굳건히 지켰습니다."
            ]
        },
        "ar": {
            "title": "دوري السلة الأمريكي: دونوفان ميتشل يسجل سلة الفوز القاتلة قبل 0.3 ثانية وكافالييرز يهزم باكس 114-113",
            "subtitle": "ميتشل يسجل 30 نقطة ويبطل مفعول 41 نقطة من داميان ليلارد ليحافظ كليفلاند على سجله المثالي بـ 7 انتصارات دون هزيمة.",
            "excerpt": "خطف دونوفان ميتشل فوزا تاريخيا لكليفلاند كافالييرز برمية قاتلة قبل ثلاثة أعشار من الثانية أمام ميلووكي باكس (114-113).",
            "body": [
                "شهدت صالة فايسرف فورم في ميلووكي ليلة الإثنين 2 نوفمبر واحدة من أكثر مباريات الدوري إثارة هذا الموسم، عندما خطف دونوفان ميتشل رمية النصر لكليفلاند كافالييرز قبل 0.3 ثانية من النهاية ليفوز فريقه بنتيجة 114-113.",
                "وتألق داميان ليلارد بتسجيله 41 نقطة منها 10 ثلاثيات إلى جانب 34 نقطة و16 متابعة من يانيس أنتيتوكونمبو، غير أن ميتشل (30 نقطة) حسم اللقاء ببراعة مذهلة ليقود كافالييرز لتحقيق فوزه السابع تواليا دون أي هزيمة."
            ]
        }
    },
    "premier-league-mw9-fulham-stun-brentford-2-1-wilson-stoppage-time-brace-2026": {
        "fr": {
            "title": "Premier League J9 : Harry Wilson signe un double historique dans le temps additionnel, Fulham renverse Brentford 2-1",
            "subtitle": "Entre en jeu a la 82e, l'international gallois marque a la 92e et a la 97e pour faire basculer le derby de l'ouest londonien a Craven Cottage.",
            "excerpt": "Craven Cottage a chavire dans la folie lundi soir : Harry Wilson a inscrit deux buts miraculeux dans les arrets de jeu pour battre Brentford 2-1.",
            "body": [
                "Le derby de l'ouest de Londres a bascule dans l'irrationnel lundi soir 2 novembre sur les bords de la Tamise. Menes 1-0 par Brentford suite a un boulet de canon de Vitaly Janelt, les joueurs de Fulham ont arrache un succes inespere 2-1 grace au joker Harry Wilson.",
                "Entre a la 82e minute, le Gallois a d'abord realise une reprise acrobatique d'une aile de pigeon subtile a la 92e minute, avant de sceller la victoire a la 97e minute d'une tete lobee magnifique sur un centre d'Antonee Robinson. Fulham remonte au classement avec 8 points."
            ]
        },
        "es": {
            "title": "Premier League J9: Harry Wilson anota un doblete milagroso en el anadido y el Fulham tumba 2-1 al Brentford",
            "subtitle": "El suplente de lujo remonta el derbi del oeste de Londres marcando en el 92 y en el 97 para desatar la locura en Craven Cottage.",
            "excerpt": "El Fulham logro una remontada epica en Craven Cottage con dos goles en el descuento de Harry Wilson para vencer 2-1 al Brentford.",
            "body": [
                "Craven Cottage vivio un final legendario este lunes 2 de noviembre en el derbi del oeste londinense. El Brentford se habia adelantado con un zapatazo lejano de Vitaly Janelt, pero la entrada al campo de Harry Wilson en el minuto 82 cambio por completo el destino del encuentro.",
                "En el minuto 92, Wilson firmo una genialidad rematando con el exterior del pie en el aire para superar al portero Mark Flekken. Y en el 97, conecto un cabezazo bombeado tras centro de Antonee Robinson que dio al Fulham una victoria inolvidable por 2-1 para sumar 8 puntos."
            ]
        },
        "de": {
            "title": "Premier League 9. Spieltag: Harry Wilson schockt Brentford mit Nachspielzeit-Doppelpack zum 2:1-Derbysieg fuer Fulham",
            "subtitle": "Der Joker trifft in der 92. und 97. Minute per artistischem Fersentrick und Kopfball und sorgt fuer Ekstase im Craven Cottage.",
            "excerpt": "Wahnsinn an der Themse: Harry Wilson drehte das West-London-Derby mit zwei Toren in der Nachspielzeit zum 2:1-Triumph ueber Brentford.",
            "body": [
                "Das Craven Cottage stand am Montagabend, den 2. November, Kopf. Der FC Brentford lag nach einem Gewaltschuss von Vitaly Janelt lange vorne, ehe Fulhams Einwechselspieler Harry Wilson zur historischen Derby-Aufholjagd ansetzte.",
                "In der 92. Minute traf der Waliser spektakulaer mit der Hacke im Flug zum Ausgleich. In der 97. Minute kroente Wilson die Aufholjagd mit einem feinen Kopfballbogen nach Flanke von Robinson zum 2:1-Endstand. Fulham klettert auf 8 Punkte."
            ]
        },
        "it": {
            "title": "Premier League 9ª giornata: Favola Harry Wilson, doppietta nei minuti di recupero e il Fulham ribalta il Brentford 2-1",
            "subtitle": "Il gallese entra all'82' e segna al 92' al volo e al 97' di testa, regalando un derby memorabile al pubblico di Craven Cottage.",
            "excerpt": "Apoteosi Fulham a Craven Cottage: due reti incredibili di Harry Wilson nel recupero piegano il Brentford 2-1 nel derby londinese.",
            "body": [
                "Finale surreale nel derby del West London lunedi 2 novembre a Craven Cottage. Sotto 1-0 contro il Brentford per via della gran botta di Janelt, il Fulham ha rovesciato l'esito della sfida grazie a un clamoroso Harry Wilson.",
                "Subentrato all'82', l'esterno gallese ha pareggiato al 92' con un tocco aereo al volo da cineteca, per poi completare il sorpasso al 97' con un colpo di testa a pallonetto su cross di Robinson. I Cottagers festeggiano salendo a 8 punti in classifica."
            ]
        },
        "pl": {
            "title": "Premier League 9. kolejka: Magiczny dublet Harry'ego Wilsona w doliczonym czasie gry, Fulham ogrywa Brentford 2:1",
            "subtitle": "Wprowadzony z lawki skrzydlowy trafia w 92. i 97. minucie, wywolujac szalenstwo radosci na Craven Cottage.",
            "excerpt": "Niewiarygodna koncowka derbow zachodniego Londynu: Harry Wilson strzelil dwa gole w doliczonym czasie, dajac Fulham wygrana 2:1 nad Brentfordem.",
            "body": [
                "Craven Cottage eksplodowalo z radosci w poniedzialkowy wieczor 2 listopada. Brentford prowadzil po znakomitym uderzeniu Vitaly'ego Janelta z 30 metrow, lecz koncowka nalezala do rezerwowego Harry'ego Wilsona.",
                "Walijczyk najpierw w 92. minucie zlozyl sie do ekwilibrystycznego uderzenia pieta w powietrzu, pokonujac Flekkena, a w 97. minucie precyzyjna glowka przelobowal bramkarza gosci. Fulham triumfowalo 2:1 i ma na koncie 8 punktow."
            ]
        },
        "zh": {
            "title": "英超第9轮：威尔逊补时连进两球演神奇逆转，富勒姆2-1绝杀布伦特福德德比告捷",
            "subtitle": "第82分钟替补登场的威尔逊在第92和97分钟奉献神级蝎子摆尾与吊射头球，克拉文农场陷入疯狂。",
            "excerpt": "克拉文农场见证了英超西伦敦德比的永恒名局，哈里·威尔逊在补时阶段连入两球助富勒姆2-1绝杀布伦特福德。",
            "body": [
                "11月2日周一晚间，泰晤士河畔的克拉文农场球场上演了不可思议的绝地逆转。布伦特福德凭借雅内尔特上半场的重炮轰门取得领先，并将优势保持到了全场常规时间最后阶段。",
                "第82分钟替补上阵的哈里·威尔逊在补时阶段封神。第92分钟，他接特劳雷传中凌空用外脚背垫出绝妙吊射破门；第97分钟，他又接罗宾逊传中轻巧头球挑过门将弗莱肯，帮助富勒姆2-1逆转绝杀，积分升至8分。"
            ]
        },
        "ja": {
            "title": "プレミアリーグ第9節：ハリー・ウィルソンが劇的AT2発！フラムがブレントフォードに2-1逆転勝利",
            "subtitle": "82分投入のスーパーサブが92分のアクロバティック弾と97分のループヘッドで西ロンドンダービーを制す。",
            "excerpt": "クレイヴン・コテージが熱狂！アディショナルタイムにウィルソンが2得点を奪い、フラムが2-1でブレントフォードを下しました。",
            "body": [
                "11月2日月曜日、クレイヴン・コテージで行われた西ロンドンダービーは伝説的な幕切れとなりました。ヤネルトの鮮烈なロングシュートで先制されたフラムでしたが、途中出場のハリー・ウィルソンが奇跡を起こしました。",
                "92分にトラオレのクロスをアクロバティックなボレーで流し込んで同点とすると、97分にはロビンソンのクロスをふわりとしたヘディングで沈めて劇的決勝ゴール。フラムが2-1で逆転勝利を収め勝ち点8に到達しました。"
            ]
        },
        "ko": {
            "title": "프리미어리그 9R: 해리 윌슨 추가시간 멀티골 기적, 풀럼 브렌트퍼드 2-1 대역전승",
            "subtitle": "82분 교체 투입된 윌슨이 92분 힐킥 동점골과 97분 헤더 결승골 작렬하며 서런던 더비 장악.",
            "excerpt": "크레이븐 코티지에서 기적이 일어났습니다. 해리 윌슨이 후반 추가시간에만 2골을 몰아치며 풀럼의 2-1 역전승을 이끌었습니다.",
            "body": [
                "11월 2일 월요일 런던 크레이븐 코티지에서 열린 프리미어리그 서런던 더비는 축구사에 남을 대역전극으로 마무리되었습니다. 야넬트에게 선제골을 내주고 끌려가던 풀럼은 마르코 실바 감독의 용병술로 경기를 뒤집었습니다.",
                "82분에 교체로 들어간 해리 윌슨은 92분에 트라오레의 크로스를 감각적인 공중 뒤꿈치 슈팅으로 마무리해 동점을 만들었고, 97분에는 로빈슨의 크로스를 절묘한 로빙 헤더로 연결해 2-1 승리를 완성했습니다. 풀럼은 승점 8점으로 도약했습니다."
            ]
        },
        "ar": {
            "title": "الدوري الإنجليزي الجولة 9: هاري ويلسون يقلب الطاولة بثنائية إعجازية في الوقت القاتل وفولهام يهزم برينتفورد 2-1",
            "subtitle": "البديل الويلزي يسجل في الدقيقتين 92 و97 بلمستين فنيتين ساحرتين ليمنح فريقه دربي غرب لندن في كرافن كوتيج.",
            "excerpt": "عاش ملعب كرافن كوتيج ليلة تاريخية الإثنين بعدما سجل هاري ويلسون هدفين في الوقت بدل الضائع ليقود فولهام للفوز 2-1 على برينتفورد.",
            "body": [
                "شهد دربي غرب لندن يوم الإثنين 2 نوفمبر إثارة لا مثيل لها على ملعب كرافن كوتيج. وتقدم برينتفورد أولا بتسديدة صاروخية من يانيلت، وظل متقدما حتى الدقيقة 90 وسط صمود دفاعي كبير.",
                "لكن البديل هاري ويلسون، الذي شارك في الدقيقة 82، صنع المعجزة بتسجيل هدف التعادل في الدقيقة 92 بلمسة أكروباتية رائعة في الشباك، قبل أن يسجل هدف الفوز القاتل في الدقيقة 97 برأسية ساقطة من فوق الحارس لتنتهي المباراة 2-1 ويرتفع رصيد فولهام إلى 8 نقاط."
            ]
        }
    },
    "atp-paris-masters-2026-tsitsipas-battles-past-carballes-baena-bercy-opener": {
        "fr": {
            "title": "Rolex Paris Masters : Stefanos Tsitsipas renverse Roberto Carballes Baena (4-6, 6-3, 6-3) pour son entree a Bercy",
            "subtitle": "Auteur de 37 coups gagnants et 11 aces, le Grec comble un set de retard et preserve ses chances de qualification pour les ATP Finals.",
            "excerpt": "Stefanos Tsitsipas s'est extirpe d'un piege lundi a Bercy en venant a bout de l'Espagnol Carballes Baena en trois manches.",
            "body": [
                "Le Rolex Paris Masters a demarre sous haute tension lundi 2 novembre a l'Accor Arena. Tete de serie numero 10, Stefanos Tsitsipas s'est employe pendant plus de deux heures pour ecarter le coriace Roberto Carballes Baena 4-6, 6-3, 6-3.",
                "Apres une premiere manche dominee par l'Espagnol, le joueur hellene a hausse son niveau en frappant 37 winners et en verrouillant sa mise en jeu avec 81% de points gagnes sur premiere balle. Tsitsipas engrange 50 points capitaux dans la course pour le Masters de Turin."
            ]
        },
        "es": {
            "title": "Rolex Paris Masters: Stefanos Tsitsipas remonta a Roberto Carballes Baena (4-6, 6-3, 6-3) en su estreno en Bercy",
            "subtitle": "El griego firma 37 golpes ganadores y 11 saques directos para alcanzar la segunda ronda y seguir en la carrera por Turín.",
            "excerpt": "Stefanos Tsitsipas debuto con victoria trabajada en el Masters 1000 de Paris al batir en tres sets al espanol Carballes Baena.",
            "body": [
                "Jornada inaugural intensa en el Accor Arena este lunes 2 de noviembre. Stefanos Tsitsipas tuvo que emplearse a fondo durante 2 horas y 7 minutos para doblegar al espanol Roberto Carballes Baena por 4-6, 6-3 y 6-3 en la pista central.",
                "Carballes se anoto el primer parcial gracias a su solidez de fondo, pero el decimo cabeza de serie reacciono atacando la red y conectando 37 golpes ganadores y 11 aces. Tsitsipas suma 50 valiosos puntos ATP para mantener vivas sus opciones de estar en las ATP Finals de Turin."
            ]
        },
        "de": {
            "title": "Rolex Paris Masters: Stefanos Tsitsipas kaempft Roberto Carballes Baena mit 4:6, 6:3, 6:3 nieder",
            "subtitle": "Der an Position zehn gesetzte Grieche schlaegt 37 Winner und wahrt mit dem Dreisatzerfolg seine Chance auf die ATP Finals.",
            "excerpt": "Stefanos Tsitsipas drehte am Montag in Paris einen Satzrueckstand gegen Roberto Carballes Baena und zog in die zweite Runde ein.",
            "body": [
                "Das Rolex Paris Masters in der Accor Arena startete am Montag, den 2. November, mit harter Arbeit fuer Stefanos Tsitsipas. Der Grieche bezwang den spanischen Sandplatzspezialisten Roberto Carballes Baena nach Satzrueckstand mit 4:6, 6:3, 6:3.",
                "Tsitsipas benoetigte zwei Stunden und sieben Minuten und stellte im zweiten Durchgang seine Taktik um. Mit 37 direkten Gewinnschlaegen und 11 Assen sicherte sich der Athener den Sieg und wichtige Punkte fuer das Saisonfinale in Turin."
            ]
        },
        "it": {
            "title": "Rolex Paris Masters: Stefanos Tsitsipas rimonta Roberto Carballes Baena 4-6, 6-3, 6-3 all'esordio a Bercy",
            "subtitle": "Il greco piazza 37 vincenti e 11 ace per accedere ai sedicesimi e alimentare il sogno delle Nitto ATP Finals di Torino.",
            "excerpt": "Esordio vincente ma sofferto per Stefanos Tsitsipas all'Accor Arena di Parigi: vittoria in tre set su Carballes Baena.",
            "body": [
                "Inizia con una battaglia il cammino di Stefanos Tsitsipas al Rolex Paris Masters lunedi 2 novembre. Il tennista greco, testa di serie numero 10, ha superato lo spagnolo Roberto Carballes Baena con lo score di 4-6, 6-3, 6-3.",
                "Perso il primo parziale sotto la spinta del dritto arrotato dell'iberico, Tsitsipas ha preso in mano lo scambio mettendo a segno 37 colpi vincenti. Il successo vale l'accesso al secondo turno e 50 punti preziosi nella Race to Turin."
            ]
        },
        "pl": {
            "title": "Rolex Paris Masters: Stefanos Tsitsipas odrabia straty i pokonuje Roberto Carballesa Baene 4:6, 6:3, 6:3",
            "subtitle": "Grek poslal 37 uderzen konczacych i 11 asow, meldujac sie w drugiej rundzie i przedluzajac szanse na Turyn.",
            "excerpt": "Stefanos Tsitsipas po ciezkim trzysetowym boju pokonal Hiszpana Carballesa Baene na otwarcie turnieju Masters 1000 w Paryzu.",
            "body": [
                "W poniedzialek 2 listopada w paryskiej hali Accor Arena rozpoczal sie turniej Rolex Paris Masters. Rozstawiony z numerem 10 Stefanos Tsitsipas musial mocno sie napracowac, by pokonac Roberto Carballesa Baene 4:6, 6:3, 6:3.",
                "Grek przegral partig otwarcia, lecz w dwoch kolejnych setach dominowal dzieki swietnemu serwisowi i odwaznym atakom. Tsitsipas zapisal na swoim koncie 37 winnerow oraz 11 asow i zachowal realne szanse na awans do turnieju ATP Finals."
            ]
        },
        "zh": {
            "title": "劳力士巴黎大师赛：西西帕斯4-6、6-3、6-3逆转卡巴列斯，首战告捷保留总决赛希望",
            "subtitle": "10号种子全场轰出37记制胜分与11记发球得分，苦战三盘挺进贝尔西次轮。",
            "excerpt": "在巴黎大师赛首轮较量中，希腊名将西西帕斯上演三盘逆转，以4-6、6-3、6-3击败西班牙好手卡巴列斯晋级32强。",
            "body": [
                "11月2日周一，年度最后一站ATP1000大师赛在巴黎贝尔西体育馆拉开战幕。10号种子西西帕斯经历2小时零7分钟的激战，以4-6、6-3、6-3逆转击败西班牙红土好手卡巴列斯·巴埃纳。",
                "在首盘受阻的不利局面下，西西帕斯调整战术加强正手进攻，全场轰出37记制胜分并赢下81%的一发得分。凭借这场胜利，希腊名将收获50个积分，继续保留着入围都灵ATP年终总决赛的微弱希望。"
            ]
        },
        "ja": {
            "title": "ロレックス・パリ・マスターズ：チチパスがカルバレス・バエナに4-6, 6-3, 6-3で逆転勝利し初戦突破",
            "subtitle": "第10シードが37本のウィナーと11本のエースを浴びせ、トリノ最終戦への望みをつなぐ2回戦進出。",
            "excerpt": "パリのアコー・アリーナでチチパスがセットを失いながらもカルバレス・バエナに競り勝ち、幸先の良いスタートを切りました。",
            "body": [
                "11月2日月曜日、パリのアコー・アリーナで今季最後のマスターズ1000が開幕しました。第10シードのステファノス・チチパスがスペインのロベルト・カルバレス・バエナに4-6、6-3、6-3で逆転勝ちを収めました。",
                "初めのセットを落としたチチパスでしたが、アグレッシブな攻めに切り替えてウィナー37本、サービスエース11本を記録。2時間7分の激闘を制し、ATPファイナルズ出場権獲得へ向けて貴重な勝ち点50を積み上げました。"
            ]
        },
        "ko": {
            "title": "롤렉스 파리 마스터스: 치치파스, 카르바예스 바에나에 4-6, 6-3, 6-3 역전승 거두고 베르시 2회전 진출",
            "subtitle": "위너 37개와 에이스 11개 폭발시킨 10번 시드, 세트스코어 뒤집으며 투린 파이널스 진출 희망 이어가.",
            "excerpt": "스테파노스 치치파스가 파리 마스터스 1회전에서 카르바예스 바에나를 상대로 3세트 접전 끝에 역전승을 거뒀습니다.",
            "body": [
                "11월 2일 월요일 파리 아코르 아레나에서 열린 롤렉스 파리 마스터스 개막전에서 10번 시드 스테파노스 치치파스가 스페인의 로베르토 카르바예스 바에나를 4-6, 6-3, 6-3으로 꺾었습니다.",
                "첫 세트를 내준 치치파스는 공격적인 네트 대시와 포핸드 강타로 37개의 위너를 기록하며 분위기를 반전시켰습니다. 2시간 7분의 혈투 끝에 승리한 치치파스는 랭킹 포인트 50점을 획득하며 투린 ATP 파이널스 출전 경쟁을 이어갔습니다."
            ]
        },
        "ar": {
            "title": "بطولة باريس للماسترز: ستيفانوس تسيتسيباس يقلب تأخره ويهزم كارباييس باينا 4-6 و6-3 و6-3 في الدور الأول",
            "subtitle": "اللاعب اليوناني يسدد 37 ضربة قاضية و11 إرسالا ساحقا ليبلغ دور الـ32 ويحافظ على آماله في التأهل للبطولة الختامية في تورينو.",
            "excerpt": "افتتح تسيتسيباس مشواره في بطولة باريس للماسترز بفوز شاق على الإسباني كارباييس باينا بعد ثلاث مجموعات في قاعة بيرسي.",
            "body": [
                "انطلقت منافسات بطولة رولكس باريس للماسترز يوم الإثنين 2 نوفمبر في صالة أكور أرينا بلقاء حماسي نجح خلاله اليوناني ستيفانوس تسيتسيباس المصنف العاشر في تعويض خسارته للمجموعة الأولى ليفوز على الإسباني روبرتو كارباييس باينا بنتيجة 4-6 و6-3 و6-3.",
                "واحتاج تسيتسيباس إلى ساعتين و7 دقائق لكسر مقاومة منافسه، معتمدا على قوة إرساله وتسديد 37 ضربة ناجحة و11 إرسالا ساحقا، ليحصد 50 نقطة هامة تعزز حظوظه في التأهل إلى نهائيات رابطة المحترفين في تورينو."
            ]
        }
    },
    "f1-sao-paulo-gp-2026-preview-antonelli-coronation-interlagos-constructors-fight": {
        "fr": {
            "title": "F1 GP de São Paulo présentation : Apres le sacre d'Antonelli, cap sur Interlagos pour la bataille des constructeurs",
            "subtitle": "Mercedes devance Ferrari de 133 points alors que le format Sprint promet un spectacle electrique au Bresil.",
            "excerpt": "Au lendemain du titre historique de Kimi Antonelli a Mexico, la Formule 1 s'installe a Interlagos pour le duel Mercedes-Ferrari chez les constructeurs.",
            "body": [
                "Le paddock de la Formule 1 a pose ses valises au Bresil ce lundi 2 novembre, encore emu par le sacre historique de Kimi Antonelli dimanche a Mexico. A seulement 20 ans et 68 jours, le pilote Mercedes est devenu le plus jeune champion du monde des pilotes de l'histoire.",
                "Avec le titre pilotes scelle, tous les regards se tournent vers le championnat du monde des constructeurs. Mercedes mene avec 133 points d'avance sur Ferrari (607 contre 474). A Interlagos, circuit mythique avec la course Sprint de samedi, Leclerc et Hamilton comptent tout donner pour faire briller la Scuderia."
            ]
        },
        "es": {
            "title": "F1 Previa GP de São Paulo: Tras la coronacion de Antonelli, Interlagos acoge la batalla final de constructores",
            "subtitle": "Mercedes aventaja a Ferrari en 133 puntos con el penultimo fin de semana con formato Sprint de la temporada 2026.",
            "excerpt": "Tras el historico titulo de Kimi Antonelli en Mexico, la Formula 1 llega a Brasil con el duelo Mercedes vs Ferrari por el campeonato de escuderias.",
            "body": [
                "La Formula 1 llego este lunes 2 de noviembre a Brasil con el eco del historico triunfo de Kimi Antonelli, quien el domingo se convirtio en el campeon del mundo mas joven de todos los tiempos en la Ciudad de Mexico.",
                "Ahora la atencion se traslada al legendario Autodromo Jose Carlos Pace de Interlagos, donde Mercedes defiende una renta de 133 puntos frente a Ferrari en la lucha por el mundial de constructores (607 contra 474). El formato Sprint del sabado anadira maxima emocion a un fin de semana decisivo."
            ]
        },
        "de": {
            "title": "Formel 1 Sao Paulo GP Vorschau: Nach Antonellis Kroenung tobt in Interlagos der Kampf um die Konstrukteurs-WM",
            "subtitle": "Mercedes fuehrt mit 133 Punkten Vorsprung auf Ferrari vor dem vorletzten Sprint-Wochenende der Saison 2026.",
            "excerpt": "Nur einen Tag nach Kimi Antonellis historischem Titelgewinn zieht der Formel-1-Zirkus weiter nach Brasilien zum Showdown in Interlagos.",
            "body": [
                "Der Formel-1-Tross erreichte am Montag, den 2. November, Brasilien. Nach dem Sensationserfolg von Kimi Antonelli, der in Mexiko mit 20 Jahren zum juengsten Fahrer-Weltmeister der Geschichte avancierte, rueckt die Team-Weltmeisterschaft in den Fokus.",
                "Mercedes geht mit 133 Punkten Vorsprung auf Ferrari (607 zu 474) in das traditionsreiche Rennwochenende auf dem Autodromo Jose Carlos Pace. Mit dem Sprintrennen am Samstag stehen bis zu 59 Punkte auf dem Spiel, waehrend Leclerc und Hamilton den Angriff auf die Silberpfeile planen."
            ]
        },
        "it": {
            "title": "F1 Presentazione GP San Paolo: Dopo il trionfo iridato di Antonelli, a Interlagos e sfida aperta tra Mercedes e Ferrari",
            "subtitle": "Mercedes in vantaggio di 133 punti sulla Rossa mentre la penultima gara Sprint del 2026 accende l'Autodromo Jose Carlos Pace.",
            "excerpt": "All'indomani del mondiale vinto da Kimi Antonelli in Messico, la Formula 1 approda in Brasile per il duello costruttori.",
            "body": [
                "Il paddock della Formula 1 e sbarcato a San Paolo lunedi 2 novembre con l'entusiasmo ancora alle stelle per il titolo mondiale conquistato da Kimi Antonelli, il piu giovane iridato nella storia della F1.",
                "Archiviato il titolo piloti, a Interlagos andra in scena il verdetto del mondiale costruttori: la Mercedes comanda con 607 punti davanti alla Ferrari a quota 474. Charles Leclerc e Lewis Hamilton cercheranno il colpaccio sulla pista paulista sfruttando la gara Sprint di sabato."
            ]
        },
        "pl": {
            "title": "F1 Zapowiedz GP Sao Paulo: Po koronacji Antonellego na torze Interlagos zaplonie walka o mistrzostwo konstruktorow",
            "subtitle": "Mercedes wyprzedza Ferrari o 133 punkty przed przedostatnim weekendem ze sprintem w sezonie 2026.",
            "excerpt": "Dzien po tym, jak Kimi Antonelli zostal najmlodszym mistrzem swiata F1, karawana wyscigowa zawitala do Brazylii na starcie na torze Interlagos.",
            "body": [
                "Padok Formuly 1 dotarl w poniedzialek 2 listopada do Brazylii. Po niedzielnym triumfie 20-letniego Kimiego Antonellego w Meksyku, uwaga calego swiata motorsportu przenosi sie na rywalizacje konstruktorow.",
                "Na kultowym torze Interlagos Mercedes broni 133 punktow przewagi nad Ferrari (607 do 474). Sobotni wyscig sprinterski i niedzielne Grand Prix zwiastuja wielkie emocje, w ktorych Leclerc i Hamilton beda polowac na dublet dla stajni z Maranello."
            ]
        },
        "zh": {
            "title": "F1圣保罗大奖赛前瞻：安东内利加冕后F1移师英特拉格斯，梅赛德斯与法拉利打响车队冠军决战",
            "subtitle": "梅赛德斯手握133分领先优势，年度倒数第二场冲刺赛即将引爆巴西传奇赛道狂潮。",
            "excerpt": "在安东内利创纪录加冕车手世界冠军的次日，F1全员抵达巴西，英特拉格斯将迎来梅赛德斯与法拉利的车队争霸战。",
            "body": [
                "11月2日周一，F1围场正式进驻巴西圣保罗英特拉格斯赛道。就在周日，20岁的梅赛德斯超新星安东内利在墨西哥城登顶，成为F1史上最年轻的车手世界冠军。",
                "随着车手总冠军悬念揭晓，车队世界冠军之争进入白热化阶段。目前梅赛德斯以607分领先法拉利（474分）达133分。巴西站包含冲刺赛赛制，最多可产生59个车队积分，勒克莱尔与汉密尔顿将全力向银箭发起最后反扑。"
            ]
        },
        "ja": {
            "title": "F1サンパウロGPプレビュー：アントネッリ戴冠の興奮冷めやらぬ中、名門インテルラゴスで熱きコンストラクターズ決戦",
            "subtitle": "メルセデスがフェラーリに133点差リード；今季5度目のスプリントフォーマットが波乱を呼ぶ。",
            "excerpt": "アントネッリが最年少王者に輝いた翌日、F1はブラジルへ移動。インテルラゴスを舞台にチームタイトルを懸けた激突が始まります。",
            "body": [
                "11月2日月曜日、F1サーカスはブラジルのインテルラゴス・サーキットに到着しました。日曜日のメキシコGPでキミ・アントネッリが史上最年少でのワールドチャンピオン獲得を決めた興奮がまだ残っています。",
                "個人タイトルの次はチームの栄冠を懸けた戦いです。コンストラクターズ選手権首位のメルセデス（607点）と追うフェラーリ（474点）の差は133ポイント。土曜日のスプリントを含むブラジルGPでルクレールとハミルトンが逆転を目指します。"
            ]
        },
        "ko": {
            "title": "F1 상파울루 GP 프리뷰: 안토넬리 대관식 뒤이어 인테를라고스서 메르세데스 대 페라리 컨스트럭터 혈전",
            "subtitle": "메르세데스가 페라리에 133점 앞선 가운데 2026시즌 5번째 스프린트 레이스가 펼쳐지는 브라질 결전.",
            "excerpt": "키미 안토넬리의 최연소 월드 챔피언 등극 다음 날, F1 그리드가 브라질 상파울루로 이동해 팀 챔피언십 쟁탈전에 돌입합니다.",
            "body": [
                "11월 2일 월요일 F1 패덕이 브라질 인테를라고스 서킷에 도착했습니다. 멕시코시티에서 20세 안토넬리가 페텔의 기록을 깨고 역대 최연소 챔피언에 오른 지 불과 하루 만입니다.",
                "드라이버 타이틀이 확정된 가운데 이제 시선은 컨스트럭터 챔피언십으로 향합니다. 메르세데스가 페라리에 133점 차(607점 대 474점)로 앞서 있지만, 토요일 스프린트가 포함된 인테를라고스에서는 르클레르와 해밀턴의 거센 반격이 예상됩니다."
            ]
        },
        "ar": {
            "title": "فورمولا 1 تقديم جائزة ساو باولو: بعد تتويج أنتونيللي التاريخي، حلبة إنترلاغوس تشهد صراع الصانعين بين مرسيدس وفيراري",
            "subtitle": "مرسيدس تتصدر بفارق 133 نقطة أمام فيراري مع انطلاق عطلة سباق السرعة القبل أخير لموسم 2026.",
            "excerpt": "بعد يوم واحد من تتويج الإيطالي أنتونيللي بلقب العالم، تنتقل فورمولا 1 إلى البرازيل لحسم معركة بطولة الصانعين في إنترلاغوس.",
            "body": [
                "وصلت فرق الفورمولا 1 إلى البرازيل يوم الإثنين 2 نوفمبر وسط أجواء احتفالية بتتويج كيمي أنتونيللي كأصغر بطل عالم في تاريخ الرياضة بعد إنهائه سباق المكسيك في المركز الثاني خلف شارل لوكلير.",
                "ومع حسم لقب السائقين، يتحول التركيز بالكامل إلى بطولة العالم للصانعين، حيث تتقدم مرسيدس برصيد 607 نقاط مقابل 474 لفيراري. وتوفر حلبة إنترلاغوس الشهيرة، مع سباق السرعة يوم السبت، فرصة كبيرة للوكلير وهاميلتون لتقليص الفارق وإشعال المنافسة."
            ]
        }
    },
    "pga-tour-wwt-championship-2026-preview-cabo-pereda-momentum-diamante": {
        "fr": {
            "title": "PGA Tour WWT Championship présentation : Dans l'elan du sacre de Pereda, le circuit debarque a Cabo pour la course aux cartes",
            "subtitle": "Le parcours El Cardonal concu par Tiger Woods accueille l'epreuve alors que la lutte pour le top 125 de la FedExCup Fall bat son plein.",
            "excerpt": "Apres l'emotion de la victoire historique de Raul Pereda au Mexico Open, le PGA Tour se rend a Los Cabos pour le WWT Championship a Diamante.",
            "body": [
                "Le golf mexicain est sur un nuage ce lundi 2 novembre alors que le PGA Tour pose son sac a Los Cabos pour le World Wide Technology Championship 2026. Dimanche a VidantaVallarta, Raul Pereda est entre dans l'histoire en remportant l'Open national grace a un dernier tour en 66.",
                "Ce succes retentissant offre a Pereda une exemption de deux ans et le propulse dans le top 50 mondial. Desormais, sur le splendide trace d'El Cardonal at Diamante dessine par Tiger Woods, Austin Smotherman et le reste du plateau bataillent pour assurer leur avenir parmi les 125 premiers de la FedExCup Fall."
            ]
        },
        "es": {
            "title": "PGA Tour Previa WWT Championship: Tras la hazaña historica de Pereda, el tour llega a Cabo con las tarjetas en juego",
            "subtitle": "El campo El Cardonal diseñado por Tiger Woods recibe a los golfistas en plena pugna por entrar al top 125 de la FedExCup Fall.",
            "excerpt": "Tras la apoteosica victoria de Raul Pereda en Puerto Vallarta, el PGA Tour viaja a Los Cabos para disputar el torneo en Diamante.",
            "body": [
                "El golf mexicano vive dias de ensueño este lunes 2 de noviembre con la llegada del PGA Tour a Los Cabos para disputar el World Wide Technology Championship 2026. La historica victoria de Raul Pereda en VidantaWorld lo catapulto al top 50 mundial con pase al Masters y al PGA Championship.",
                "Ahora, los focos se dirigen a El Cardonal en Diamante, el primer trazado diseñado por Tiger Woods en acoger un torneo oficial del circuito. Con solo tres citas para concluir el calendario otoñal, jugadores como Austin Smotherman y Aaron Rai buscan puntos vitales para salvar sus tarjetas dentro del top 125."
            ]
        },
        "de": {
            "title": "PGA Tour WWT Championship Vorschau: Nach Peredas historischem Coup schlaegt die Tour in Los Cabos ab",
            "subtitle": "Tiger Woods' Meisterschaftsplatz El Cardonal at Diamante fordert die Profis im dramatischen Kampf um die Top-125-Karten.",
            "excerpt": "Befluegelt von Raul Peredas Heimsieg reist die PGA Tour weiter nach Cabo San Lucas zur World Wide Technology Championship.",
            "body": [
                "Mexikos Golfwelt feiert am Montag, den 2. November, noch immer den historischen Sieg von Raul Pereda bei den VidantaWorld Mexico Open. Mit einer finalen 66er-Runde hatte sich der Lokalmatador den Titel gesichert und sich bis unter die Top 50 der Weltrangliste vorgeschoben.",
                "In dieser Woche gastiert die Tour auf dem von Tiger Woods entworfenen Kurs El Cardonal at Diamante in Los Cabos. Waehrend Pereda gefeiert wird, geht es fuer Austin Smotherman und viele weitere Akteure um das Ueberleben auf der PGA Tour im Kampf um die 125 besten Plaetze des FedExCup Fall."
            ]
        },
        "it": {
            "title": "PGA Tour Presentazione WWT Championship: Sulle ali del trionfo di Pereda, il circuito sbarca a Cabo San Lucas",
            "subtitle": "Il percorso El Cardonal disegnato da Tiger Woods ospita la sfida decisiva per le carte del tour tra i migliori 125 della FedExCup Fall.",
            "excerpt": "Dopo l'emozionante successo di Raul Pereda a Puerto Vallarta, il PGA Tour resta in Messico per il torneo di Diamante a Los Cabos.",
            "body": [
                "Clima di festa per il golf messicano lunedi 2 novembre con l'arrivo della carovana del PGA Tour a Los Cabos per il World Wide Technology Championship 2026. L'indimenticabile vittoria casalinga di Raul Pereda ha regalato al ventinovenne l'ingresso nei primi 50 al mondo e l'invito al Masters.",
                "La nuova tappa si gioca sul celebre tracciato di El Cardonal a Diamante, firmato da Tiger Woods. In palio ci sono 500 punti FedExCup fondamentali per chi cerca di chiudere la stagione tra i primi 125 e garantire la propria carta per il 2027."
            ]
        },
        "pl": {
            "title": "PGA Tour Zapowiedz WWT Championship: Na fali historycznego triumfu Peredy golfisci graja w Cabo o karty na 2027",
            "subtitle": "Pole El Cardonal projektu Tigera Woodsa gosci zawodnikow walczacych o utrzymanie w czołowej 125 rankingu FedExCup Fall.",
            "excerpt": "Po wielkim sukcesie Raula Peredy w Mexico Open cykl PGA Tour przenosi sie do Los Cabos na prestizowe zawody w Diamante.",
            "body": [
                "Meksykanski golf przezyl chwile chwaly, a w poniedzialek 2 listopada PGA Tour zawitalo do Los Cabos na World Wide Technology Championship 2026. Triumf Raula Peredy z wynikiem 17 ponizej par zapewnil mu skok do czolowej 50 rankingu i przepustke do turniejow wielkoszlemowych.",
                "Rywalizacja przenosi sie na pole El Cardonal w osrodku Diamante, zaprojektowane przez Tigera Woodsa. Austin Smotherman oraz Aaron Rai powalcza o cenne punkty FedExCup Fall, ktore zadecyduja o kartach PGA Tour na przyszly sezon."
            ]
        },
        "zh": {
            "title": "美巡赛WWT锦标赛前瞻：佩雷达历史性夺冠余威尚存，美巡转战卡博打响保卡生死战",
            "subtitle": "老虎伍兹操刀设计的迪亚曼特卡多纳尔球场迎战群雄，秋季赛前125名全卡争夺进入白热化阶段。",
            "excerpt": "在劳尔·佩雷达捧得墨西哥公开赛冠军后，美巡赛移师下加利福尼亚，迪亚曼特球场即将上演保卡大戏。",
            "body": [
                "11月2日周一，墨西哥高尔夫界沉浸在空前的自豪与喜悦之中。劳尔·佩雷达周日在巴亚尔塔港以两杆优势夺冠，成为美巡赛时代首位在本土夺冠的墨西哥球手，不仅世界排名跻身前50，更锁定了大师赛与PGA锦标赛参赛席位。",
                "本周美巡赛继续留在墨西哥，转战由老虎·伍兹亲自设计的洛斯卡波斯卡多纳尔球场。除了携荣耀登场的佩雷达外，斯莫瑟曼、阿龙·莱等一众名将也将全力出击，在仅剩3站的秋季赛中为确保前125名参赛全卡奋力搏杀。"
            ]
        },
        "ja": {
            "title": "PGAツアー WWT選手権プレビュー：ペレダの歴史的快挙に沸くメキシコ、カボでシード権争奪戦が開幕",
            "subtitle": "タイガー・ウッズ設計のエル・カルドナルが舞台；フェデックスカップ・フォール上位125名を巡る激戦。",
            "excerpt": "ラウル・ペレダの感動的なメキシコオープン制覇の熱気そのままに、PGAツアーはロスカボスのディアマンテへと舞台を移します。",
            "body": [
                "11月2日月曜日、メキシコ・ゴルフ界が熱狂に包まれる中、PGAツアーはロスカボスでのワールドワイド・テクノロジー選手権へと移動しました。日曜日、ラウル・ペレダが母国初優勝を飾り世界ランキングトップ50入りとマスターズ出場権を獲得しました。",
                "今週の舞台はタイガー・ウッズが設計した名コース、エル・カルドナル・アット・ディアマンテ。ペレダの凱旋とともに、来季の出場権確保となるフォールシリーズ上位125位以内を目指す選手たちの熱い戦いが幕を開けます。"
            ]
        },
        "ko": {
            "title": "PGA 투어 WWT 챔피언십 프리뷰: 페레다의 역사적 우승 열기 속 카보서 펼쳐지는 시드권 쟁탈전",
            "subtitle": "타이거 우즈가 설계한 엘 카르도날 코스서 격돌; 페덱스컵 가을 시리즈 톱125 보장 카드 전쟁.",
            "excerpt": "라울 페레다의 감격적인 멕시코 오픈 제패에 이어, PGA 투어는 로스카보스의 디아만테로 무대를 옮깁니다.",
            "body": [
                "11월 2일 월요일 멕시코 골프계가 페레다의 우승 열기로 가득 찬 가운데, PGA 투어가 로스카보스에서 2026 월드와이드 테크놀로지 챔피언십을 개최합니다. 전날 페레다는 17언더파로 자국 대회 정상에 오르며 세계랭킹 50위권 진입과 마스터스 출전권을 따냈습니다.",
                "이번 대회는 타이거 우즈가 설계한 명문 코스인 엘 카르도날 앳 디아만테에서 열립니다. 준우승자 오스틴 스모더먼을 비롯한 선수들은 2027년 풀 시드가 주어지는 페덱스컵 가을 시리즈 상위 125위 진입을 위해 치열한 샷 대결을 벌입니다."
            ]
        },
        "ar": {
            "title": "جولة بي جي إيه تقديم بطولة دابليو دابليو تي: بعد إنجاز بيريدا التاريخي، الجولة تنتقل إلى كابو لحسم بطاقات الموسم",
            "subtitle": "ملعب إل كاردونال من تصميم تايغر وودز يستضيف البطولة مع اشتعال المنافسة لحجز مقعد ضمن أفضل 125 لاعبا.",
            "excerpt": "بعد التتويج التاريخي للبطل المكسيكي راؤول بيريدا، تحط جولة الجولف الأمريكية رحالها في لوس كابوس لخوض منافسات بطولة ديامانتي.",
            "body": [
                "تعيش رياضة الجولف المكسيكية أياما من الفخر يوم الإثنين 2 نوفمبر مع وصول نجوم جولة بي جي إيه إلى لوس كابوس لخوض بطولة التكنولوجيا العالمية لعام 2026. وتوج راؤول بيريدا يوم الأحد بلقب بطولة المكسيك ليقفز إلى قائمة أفضل 50 لاعبا عالميا ويضمن المشاركة في الماسترز وبطولة بي جي إيه الكبرى.",
                "وتقام منافسات هذا الأسبوع على ملعب إل كاردونال في ديامانتي، وهو أول ملعب من تصميم الأسطورة تايغر وودز يستضيف حدثا رسميا للجولة. ويسعى أوستن سموذر مان وآرون راي لجمع نقاط ثمينة تضمن بقاءهما ضمن أفضل 125 لاعبا في تصنيف الخريف لضمان بطاقة المشاركة للموسم المقبل."
            ]
        }
    }
}

# Strict validation
for slug, langs in NOV02_STORIES.items():
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

print("All November 2 story translations validated: 0 em-dashes and 0 double-hyphens.")

snippet_parts = []
for slug, langs in NOV02_STORIES.items():
    formatted_slug = json.dumps(slug)
    snippet_parts.append(f"{formatted_slug}: {json.dumps(langs, ensure_ascii=False, indent=2)},")

snippet = "\n".join(snippet_parts) + "\n"

stories_file = os.path.join(os.path.dirname(__file__), "../../frontend/src/i18n/stories.ts")
with open(stories_file, "r", encoding="utf-8") as f:
    content = f.read()

target = "export const STORY_I18N: Record<string, LocMap> = {\n"
assert target in content, "Target line not found in stories.ts"

new_content = content.replace(target, target + snippet, 1)

with open(stories_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully injected November 2 translations into frontend/src/i18n/stories.ts")
