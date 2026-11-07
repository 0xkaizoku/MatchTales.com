# -*- coding: utf-8 -*-
"""Add 7 November 2026 translations for all 6 stories across 9 languages."""
import json
import os
import re

NOV07_STORIES = {
    "nfl-week9-saturday-madrid-bengals-falcons-preview-2026": {
        "fr": {
            "title": "NFL Semaine 9 Madrid : les Bengals jouent les Falcons au Bernabeu dimanche a 9h30 ET",
            "subtitle": "Pas de match NFL le samedi. Cincinnati 5-2 affronte Atlanta 3-5 en Espagne. Dernier score : Jaguars 33, Ravens 10.",
            "excerpt": "Les Cincinnati Bengals jouent les Atlanta Falcons dimanche au stade Santiago Bernabeu. Coup d'envoi a 9h30 ET sur NFL Network. Pas de score.",
            "body": [
                "Le samedi 7 novembre n'a pas de match NFL. Le prochain rendez-vous est dimanche : Cincinnati contre Atlanta au Santiago Bernabeu a Madrid, 9h30 ET (15h30 locale) sur NFL Network. Atlanta est l'equipe recevante designee. Ce desk ne publie pas de score.",
                "Cincinnati est 5-2 apres une victoire 43-36 en prolongation contre le Tennessee. Atlanta est 3-5. Bengals.com place Joe Burrow en tete de la NFL en pourcentage de passes (73,0), touchdowns a la passe (20) et yards par match (302,1). Bijan Robinson mene avec 780 yards au sol. Dernier score jeudi : Jaguars 33, Ravens 10. Les Steelers restent 6-2, au repos en semaine 9."
            ]
        },
        "es": {
            "title": "NFL Semana 9 Madrid: los Bengals visitan a los Falcons en el Bernabeu el domingo a las 9:30 ET",
            "subtitle": "No hay partido NFL el sabado. Cincinnati 5-2 contra Atlanta 3-5 en Espana. Ultimo final: Jaguars 33, Ravens 10.",
            "excerpt": "Los Cincinnati Bengals juegan contra los Atlanta Falcons el domingo en el Santiago Bernabeu. Saque a las 9:30 ET en NFL Network. Sin marcador.",
            "body": [
                "El sabado 7 de noviembre no hay partido de la NFL. El siguiente tablero es el domingo: Bengals contra Falcons en el Santiago Bernabeu, Madrid, 9:30 a.m. ET (15:30 local) en NFL Network. Atlanta es el local designado. Este desk no publica marcador.",
                "Cincinnati esta 5-2 tras ganar 43-36 en prorroga a Tennessee. Atlanta esta 3-5. Bengals.com sitúa a Joe Burrow lider en porcentaje de pases (73.0), touchdowns de pase (20) y yardas por partido (302.1). Bijan Robinson lidera con 780 yardas de carrera. Ultimo final jueves: Jaguars 33, Ravens 10. Pittsburgh sigue 6-2, bye en la semana 9."
            ]
        },
        "de": {
            "title": "NFL Woche 9 Madrid: Bengals gegen Falcons am Sonntag 9:30 ET im Bernabeu",
            "subtitle": "Samstag kein NFL-Spiel. Cincinnati 5-2 trifft in Spanien auf Atlanta 3-5. Letztes Ergebnis: Jaguars 33, Ravens 10.",
            "excerpt": "Die Cincinnati Bengals spielen am Sonntag im Santiago Bernabeu gegen die Atlanta Falcons. Kickoff 9:30 ET auf NFL Network. Kein Spielstand.",
            "body": [
                "Samstag, der 7. November, hat kein NFL-Spiel. Naechstes Board: Sonntag, Bengals gegen Falcons im Santiago Bernabeu, Madrid, 9:30 ET (15:30 Ortszeit) auf NFL Network. Atlanta ist das designierte Heimteam. Dieser Desk veroeffentlicht keinen Spielstand.",
                "Cincinnati steht 5-2 nach einem 43:36-Sieg in Overtime gegen Tennessee. Atlanta steht 3-5. Bengals.com fuehrt Joe Burrow in Completion Percentage (73,0), Passing-Touchdowns (20) und Yards pro Spiel (302,1). Bijan Robinson fuehrt mit 780 Rushing Yards. Letztes Ergebnis Donnerstag: Jaguars 33, Ravens 10. Pittsburgh bleibt 6-2, Bye in Woche 9."
            ]
        },
        "it": {
            "title": "NFL Week 9 Madrid: i Bengals affrontano i Falcons al Bernabeu domenica alle 9:30 ET",
            "subtitle": "Nessuna partita NFL il sabato. Cincinnati 5-2 contro Atlanta 3-5 in Spagna. Ultimo risultato: Jaguars 33, Ravens 10.",
            "excerpt": "I Cincinnati Bengals giocano domenica contro gli Atlanta Falcons al Santiago Bernabeu. Kickoff alle 9:30 ET su NFL Network. Nessun punteggio.",
            "body": [
                "Sabato 7 novembre non c'e una partita NFL. Il prossimo tabellone e domenica: Bengals contro Falcons al Santiago Bernabeu, Madrid, 9:30 ET (15:30 locali) su NFL Network. Atlanta e la squadra di casa designata. Questo desk non pubblica un punteggio.",
                "Cincinnati e 5-2 dopo un 43-36 ai supplementari sul Tennessee. Atlanta e 3-5. Bengals.com indica Joe Burrow primo in percentuale di completamento (73.0), touchdown su passaggio (20) e yard a partita (302.1). Bijan Robinson guida con 780 yard su corsa. Ultimo risultato giovedi: Jaguars 33, Ravens 10. Pittsburgh resta 6-2, bye nella settimana 9."
            ]
        },
        "pl": {
            "title": "NFL tydzien 9 Madryt: Bengals graja z Falcons na Bernabeu w niedziele o 9:30 ET",
            "subtitle": "W sobote nie ma meczu NFL. Cincinnati 5-2 przeciwko Atlanta 3-5 w Hiszpanii. Ostatni wynik: Jaguars 33, Ravens 10.",
            "excerpt": "Cincinnati Bengals graja w niedziele z Atlanta Falcons na Santiago Bernabeu. Poczatek o 9:30 ET w NFL Network. Bez wyniku.",
            "body": [
                "Sobota 7 listopada nie ma meczu NFL. Nastepna plansza to niedziela: Bengals przeciwko Falcons na Santiago Bernabeu w Madrycie, 9:30 ET (15:30 czasu lokalnego) w NFL Network. Atlanta jest gospodarzem. Ten desk nie publikuje wyniku.",
                "Cincinnati ma 5-2 po wygranej 43-36 po dogrywce z Tennessee. Atlanta ma 3-5. Bengals.com podaje Joe Burrowa jako lidera w skutecznosci (73.0), przylozeniach podaniem (20) i jardach na mecz (302.1). Bijan Robinson prowadzi z 780 jardami biegiem. Ostatni wynik w czwartek: Jaguars 33, Ravens 10. Steelers maja 6-2 i pauza w 9. tygodniu."
            ]
        },
        "zh": {
            "title": "NFL第9周马德里：猛虎周日美东9:30在伯纳乌对阵猎鹰",
            "subtitle": "周六无NFL比赛。辛辛那提5胜2负客战亚特兰大3胜5负。最近完场仍为美洲虎33-10乌鸦。",
            "excerpt": "辛辛那提猛虎周日在圣地亚哥伯纳乌球场对阵亚特兰大猎鹰。开球美东时间9:30，NFL Network转播。暂无比分。",
            "body": [
                "11月7日周六没有NFL比赛。下一场是周日：猛虎对猎鹰，马德里圣地亚哥伯纳乌球场，美东时间9:30（当地15:30），NFL Network。亚特兰大为指定主队。本台不发布比分。",
                "辛辛那提战绩5胜2负，加时43-36击败田纳西后三连胜。亚特兰大为3胜5负。Bengals.com显示乔·伯罗在完成率（73.0%）、传球达阵（20）和场均码数（302.1）领先联盟。比扬·罗宾逊以780冲球码领先。周四最近完场：美洲虎33-10乌鸦。钢人6胜2负，第9周轮空。"
            ]
        },
        "ja": {
            "title": "NFL第9週マドリード：ベンガルズが日曜午前9時30分ETにベルナベウでファルコンズと対戦",
            "subtitle": "土曜にNFLの試合はない。シンシナティ5勝2敗がスペインでアトランタ3勝5敗と対戦。直近の確定はジャガーズ33-10レイブンズ。",
            "excerpt": "シンシナティ・ベンガルズは日曜、サンティアゴ・ベルナベウでアトランタ・ファルコンズと対戦する。キックオフは東部時間午前9時30分、NFLネットワーク。スコアなし。",
            "body": [
                "11月7日土曜にNFLの試合はない。次のボードは日曜：ベンガルズ対ファルコンズ、マドリードのサンティアゴ・ベルナベウ、東部時間午前9時30分（現地午後3時30分）、NFLネットワーク。アトランタが指定ホーム。本デスクはスコアを出さない。",
                "シンシナティはテネシーに延長43-36で勝って5勝2敗。アトランタは3勝5敗。Bengals.comはジョー・バロウが完成率73.0%、パスTD20、試合平均302.1ヤードでリーグ首位と記す。ビジャン・ロビンソンはラッシング780ヤードで首位。木曜の直近確定はジャガーズ33-10レイブンズ。スティーラーズは6勝2敗で第9週バイ。"
            ]
        },
        "ko": {
            "title": "NFL 9주차 마드리드: 벵걸스, 일요일 동부 9시 30분 베르나베우에서 팰컨스와 대결",
            "subtitle": "토요일 NFL 경기 없음. 신시내티 5승 2패가 스페인에서 애틀랜타 3승 5패와 만납니다. 최근 확정은 재규어스 33-10 레이븐스.",
            "excerpt": "신시내티 벵걸스가 일요일 산티아고 베르나베우에서 애틀랜타 팰컨스와 경기합니다. 킥오프는 동부 9시 30분, NFL 네트워크. 점수 없음.",
            "body": [
                "11월 7일 토요일에는 NFL 경기가 없습니다. 다음 보드는 일요일: 벵걸스 대 팰컨스, 마드리드 산티아고 베르나베우, 동부 오전 9시 30분(현지 오후 3시 30분), NFL 네트워크. 애틀랜타가 지정 홈. 이 데스크는 점수를 내지 않습니다.",
                "신시내티는 테네시에 연장 43-36 승리 후 5승 2패입니다. 애틀랜타는 3승 5패. Bengals.com은 조 버로가 패스 성공률 73.0%, 패스 TD 20개, 경기당 302.1야드로 NFL 선두라고 적습니다. 비잔 로빈슨은 러싱 780야드 선두. 목요일 최근 확정은 재규어스 33-10 레이븐스. 스틸러스는 6승 2패로 9주차 바이입니다."
            ]
        },
        "ar": {
            "title": "الدوري الامريكي الاسبوع 9 مدريد: بنغالز يلاقي فالكونز في البرنابيو الاحد الساعة 9:30 بتوقيت شرق امريكا",
            "subtitle": "لا مباراة يوم السبت. سينسيناتي 5-2 ضد اتلانتا 3-5 في اسبانيا. اخر نتيجة: جاغوارز 33، ريڤنز 10.",
            "excerpt": "سينسيناتي بنغالز يلعب الاحد ضد اتلانتا فالكونز في سانتياغو برنابيو. البداية 9:30 صباحا بتوقيت شرق امريكا على NFL Network. بلا نتيجة.",
            "body": [
                "السبت 7 نوفمبر لا توجد مباراة في الدوري الامريكي. اللوحة التالية الاحد: بنغالز ضد فالكونز في سانتياغو برنابيو بمدريد، 9:30 صباحا بتوقيت شرق امريكا (15:30 محليا) على NFL Network. اتلانتا الفريق المضيف المعتمد. هذا المكتب لا ينشر نتيجة.",
                "سينسيناتي 5-2 بعد فوز 43-36 في الوقت الاضافي على تينيسي. اتلانتا 3-5. موقع بنغالز يضع جو بارو في الصدارة بنسبة اكمال 73.0 و20 لمسة تمرير و302.1 ياردة في المباراة. بيجان روبنسون يتصدر بـ780 ياردة ركضا. اخر نتيجة الخميس: جاغوارز 33، ريڤنز 10. ستيلرز 6-2 في راحة الاسبوع 9."
            ]
        }
    },
    "nba-doncic-53-lakers-beat-blazers-124-118-2026": {
        "fr": {
            "title": "NBA : Luka Doncic inscrit 53 points, les Lakers battent les Trail Blazers 124-118",
            "subtitle": "Onzieme match a 50 points en carriere, un lancer de 62 pieds a la pause, un jump shot a 28 secondes. Quatrieme succes d'affilee des Lakers.",
            "excerpt": "Luka Doncic a marque 53 points et les Los Angeles Lakers ont battu les Portland Trail Blazers 124-118 vendredi au Crypto.com Arena.",
            "body": [
                "Luka Doncic a inscrit 53 points vendredi 6 novembre au Crypto.com Arena. Associated Press recense son 11e match a 50 points en carriere, le quatrieme sous le maillot des Lakers. Il a tourne a 17 sur 33, 5 sur 15 a trois points, cinq rebonds et cinq passes. Portland a mene de 16 points. Un heave de 62 pieds a la sirene a ramene Los Angeles a 60-53 a la pause.",
                "Austin Reaves a marque 25 points. Walker Kessler 16 points et 12 rebonds. Deni Avdija 22 points, 9 rebonds, 11 passes. Damian Lillard 22. Autres resultats vendredi : Spurs 124-109 Kings (Wembanyama 30 et 14, San Antonio 7-2) ; Cavaliers 119-95 Sixers (Mitchell 23, Cleveland 5-4, Philadelphie 8-2) ; Celtics 119-80 Hornets (Tatum 34). Les matches NBA du samedi ne sont pas publies."
            ]
        },
        "es": {
            "title": "NBA: Luka Doncic anota 53 y los Lakers ganan 124-118 a los Trail Blazers",
            "subtitle": "Undecimo partido de 50 puntos en su carrera, un tiro de 62 pies al descanso y un jumper a 28 segundos. Cuarta victoria seguida de Los Angeles.",
            "excerpt": "Luka Doncic anoto 53 puntos y los Lakers de Los Angeles ganaron 124-118 a los Trail Blazers de Portland el viernes en el Crypto.com Arena.",
            "body": [
                "Luka Doncic anoto 53 el viernes 6 de noviembre en el Crypto.com Arena. Associated Press registra su 11o partido de 50 puntos, el cuarto con los Lakers. Tiro 17 de 33 y 5 de 15 en triples, con cinco rebotes y cinco asistencias. Portland llego a ir 16 arriba. Un tiro de 62 pies en la sirena dejo el 60-53 al descanso.",
                "Austin Reaves anoto 25. Walker Kessler 16 y 12 rebotes. Deni Avdija 22, 9 y 11. Damian Lillard 22. Otros viernes: Spurs 124-109 Kings (Wembanyama 30 y 14, San Antonio 7-2); Cavaliers 119-95 76ers (Mitchell 23, Cleveland 5-4, Filadelfia 8-2); Celtics 119-80 Hornets (Tatum 34). Los partidos NBA del sabado no se publican."
            ]
        },
        "de": {
            "title": "NBA: Luka Doncic erzielt 53 Punkte, Lakers schlagen Trail Blazers 124:118",
            "subtitle": "Elftes 50-Punkte-Spiel der Karriere, 62-Fuss-Wurf zur Pause, Jumper 28 Sekunden vor Schluss. Vierter Lakers-Sieg in Folge.",
            "excerpt": "Luka Doncic erzielt 53 Punkte, die Los Angeles Lakers schlagen die Portland Trail Blazers am Freitag im Crypto.com Arena 124:118.",
            "body": [
                "Luka Doncic erzielte am Freitag, den 6. November, 53 Punkte in der Crypto.com Arena. Associated Press zaehlt sein 11. 50-Punkte-Spiel, das vierte im Lakers-Trikot. Er traf 17 von 33 und 5 von 15 Dreiern, plus fuenf Rebounds und fuenf Assists. Portland fuehrte mit 16. Ein 62-Fuss-Heave zum Pausenpfiff machte 60:53.",
                "Austin Reaves erzielte 25. Walker Kessler 16 Punkte und 12 Rebounds. Deni Avdija 22, 9 und 11. Damian Lillard 22. Weitere Freitagsspiele: Spurs 124:109 Kings (Wembanyama 30 und 14, San Antonio 7-2); Cavaliers 119:95 76ers (Mitchell 23, Cleveland 5-4, Philadelphia 8-2); Celtics 119:80 Hornets (Tatum 34). Samstagsspiele bleiben unveroeffentlicht."
            ]
        },
        "it": {
            "title": "NBA: Luka Doncic segna 53, i Lakers battono i Trail Blazers 124-118",
            "subtitle": "Undicesima gara da 50 in carriera, un tiro da 62 piedi all'intervallo e un jumper a 28 secondi. Quarta vittoria di fila dei Lakers.",
            "excerpt": "Luka Doncic ha segnato 53 punti e i Los Angeles Lakers hanno battuto i Portland Trail Blazers 124-118 venerdi al Crypto.com Arena.",
            "body": [
                "Luka Doncic ha chiuso con 53 venerdi 6 novembre al Crypto.com Arena. Associated Press conta l'11a gara da 50 punti in carriera, la quarta con i Lakers. Ha tirato 17 su 33 e 5 su 15 da tre, con cinque rimbalzi e cinque assist. Portland e arrivata a +16. Un heave da 62 piedi alla sirena ha portato il 60-53 all'intervallo.",
                "Austin Reaves ha segnato 25. Walker Kessler 16 punti e 12 rimbalzi. Deni Avdija 22, 9 e 11. Damian Lillard 22. Altri venerdi: Spurs 124-109 Kings (Wembanyama 30 e 14, San Antonio 7-2); Cavaliers 119-95 76ers (Mitchell 23, Cleveland 5-4, Philadelphia 8-2); Celtics 119-80 Hornets (Tatum 34). Le gare NBA del sabato non sono pubblicate."
            ]
        },
        "pl": {
            "title": "NBA: Luka Doncic zdobywa 53 punkty, Lakers wygrywaja z Trail Blazers 124:118",
            "subtitle": "11. mecz z 50 punktami w karierze, rzut z 62 stop po pierwszej polowie i jumper na 28 sekund przed koncem. Czwarta wygrana Lakers z rzedu.",
            "excerpt": "Luka Doncic zdobyl 53 punkty, a Los Angeles Lakers pokonali Portland Trail Blazers 124:118 w piatek w Crypto.com Arena.",
            "body": [
                "Luka Doncic zdobyl 53 punkty w piatek 6 listopada w Crypto.com Arena. Associated Press notuje 11. mecz z 50 punktami, czwarty w barwach Lakers. Trafil 17 z 33 i 5 z 15 za trzy, piec zbiórek i piec asyst. Portland prowadzilo 16 punktami. Rzut z 62 stop na syrenie dal 60:53 na przerwe.",
                "Austin Reaves zdobyl 25. Walker Kessler 16 punktow i 12 zbiórek. Deni Avdija 22, 9 i 11. Damian Lillard 22. Inne piatkowe wyniki: Spurs 124:109 Kings (Wembanyama 30 i 14, San Antonio 7-2); Cavaliers 119:95 76ers (Mitchell 23, Cleveland 5-4, Filadelfia 8-2); Celtics 119:80 Hornets (Tatum 34). Sobotnie mecze NBA nie sa publikowane."
            ]
        },
        "zh": {
            "title": "NBA：东契奇砍下53分，湖人124-118逆转开拓者",
            "subtitle": "生涯第11次50+，中场62英尺超远三分，还剩28秒跳投锁定。湖人四连胜。",
            "excerpt": "卢卡·东契奇砍下53分，洛杉矶湖人周五在Crypto.com Arena以124-118击败波特兰开拓者。",
            "body": [
                "卢卡·东契奇11月6日周五在Crypto.com Arena得到53分。美联社记为其生涯第11次50+，湖人时期第4次。投篮33中17，三分15中5，5篮板5助攻。开拓者最多领先16分。中场结束前62英尺超远球将比分追至60-53。",
                "奥斯汀·里夫斯25分。沃克·凯斯勒16分12篮板。德尼·阿夫迪亚22分9篮板11助攻。达米安·利拉德22分。周五其他完场：马刺124-109国王（文班亚马30分14板，圣安东尼奥7胜2负）；骑士119-9576人（米切尔23分，克利夫兰5胜4负，费城8胜2负）；凯尔特人119-80黄蜂（塔图姆34分）。周六NBA比赛暂不发布。"
            ]
        },
        "ja": {
            "title": "NBA：ルカ・ドンチッチが53得点、レイカーズがトレイルブレイザーズに124-118",
            "subtitle": "キャリア11度目の50得点。ハーフの62フィート、残り28秒のジャンパー。レイカーズ4連勝。",
            "excerpt": "ルカ・ドンチッチが53得点を挙げ、ロサンゼルス・レイカーズが金曜にCrypto.comアリーナでポートランド・トレイルブレイザーズを124-118で破った。",
            "body": [
                "ルカ・ドンチッチは11月6日金曜、Crypto.comアリーナで53得点。APはキャリア11度目の50得点試合、レイカーズでは4度目と記録。33本中17本、3ポイント15本中5本、リバウンド5、アシスト5。ポートランドは最大16点リード。ハーフ終了間際の62フィートで60-53。",
                "オースティン・リーブス25得点。ウォーカー・ケスラー16得点12リバウンド。デニ・アヴディヤ22得点9リバウンド11アシスト。ダミアン・リラード22得点。金曜の他試合：スパーズ124-109キングス（ウェンバンヤマ30点14リバウンド、サンアントニオ7勝2敗）；キャブス119-95シクサーズ（ミッチェル23点、クリーブランド5勝4敗、フィラデルフィア8勝2敗）；セルティックス119-80ホーネッツ（タトゥム34点）。土曜のNBAは未掲載。"
            ]
        },
        "ko": {
            "title": "NBA: 루카 돈치치 53점, 레이커스가 트레일 블레이저스 124-118 제압",
            "subtitle": "커리어 11번째 50점 경기, 하프타임 62피트 슛, 28초 전 점퍼. 레이커스 4연승.",
            "excerpt": "루카 돈치치가 53점을 넣으며 로스앤젤레스 레이커스가 금요일 Crypto.com 아레나에서 포틀랜드 트레일 블레이저스를 124-118로 꺾었습니다.",
            "body": [
                "루카 돈치치는 11월 6일 금요일 Crypto.com 아레나에서 53점을 기록했습니다. AP는 커리어 11번째 50점 경기, 레이커스 유니폼으로는 네 번째로 적었습니다. 33개 중 17개, 3점 15개 중 5개, 리바운드 5, 어시스트 5. 포틀랜드는 최대 16점 차. 하프 종료 버저 62피트 슛으로 60-53.",
                "오스틴 리브스 25점. 워커 케슬러 16점 12리바운드. 데니 아브디야 22점 9리바운드 11어시스트. 데미안 릴라드 22점. 금요일 다른 결과: 스퍼스 124-109 킹스(웸반야마 30점 14리바운드, 샌안토니오 7승 2패); 캐벌리어스 119-95 76ers(미첼 23점, 클리블랜드 5승 4패, 필라델피아 8승 2패); 셀틱스 119-80 호네츠(테이텀 34점). 토요일 NBA는 미공개입니다."
            ]
        },
        "ar": {
            "title": "دوري السلة: لوكا دونتشيتش يسجل 53 ويقود ليكرز لفوز 124-118 على تريل بليزرز",
            "subtitle": "المباراة الحادية عشرة بـ50 نقطة في مسيرته، رمية من 62 قدما عند الاستراحة وجامبر قبل 28 ثانية. رابع فوز متتال لليكرز.",
            "excerpt": "لوكا دونتشيتش يسجل 53 نقطة وليكرز لوس انجلوس يفوز 124-118 على بورتلاند تريل بليزرز الجمعة في Crypto.com ارينا.",
            "body": [
                "سجل لوكا دونتشيتش 53 نقطة الجمعة 6 نوفمبر في Crypto.com ارينا. اسوشيتد برس تحصي مباراته الـ11 بـ50 نقطة، الرابعة مع ليكرز. سدد 17 من 33 و5 من 15 من الثلاثية مع خمس متابعات وخمس تمريرات. بورتلاند تقدمت بـ16. رمية من 62 قدما عند الصفارة جعلت النتيجة 60-53 عند الاستراحة.",
                "اوستن ريفز 25 نقطة. ووكر كيسلر 16 نقطة و12 متابعة. ديني افدييا 22 و9 و11. داميان ليلارد 22. نتائج الجمعة الاخرى: سبيرز 124-109 كينغز (ويمبانياما 30 و14، سان انطونيو 7-2)؛ كافالييرز 119-95 سيكسرز (ميتشل 23، كليفلاند 5-4، فيلادلفيا 8-2)؛ سلتيكس 119-80 هورنتس (تاتوم 34). مباريات السبت غير منشورة."
            ]
        }
    },
    "atp-paris-masters-2026-shelton-beats-van-assche-reaches-final": {
        "fr": {
            "title": "Rolex Paris Masters DF : Ben Shelton bat Luca Van Assche 5-7, 6-3, 6-4 et rejoint la finale",
            "subtitle": "Premier Americain en finale a Bercy depuis Jack Sock en 2017. Alcaraz-Ruud n'est pas publie.",
            "excerpt": "Ben Shelton a renverse un break dans le troisieme set pour battre Luca Van Assche 5-7, 6-3, 6-4 et atteindre la finale du Rolex Paris Masters.",
            "body": [
                "Ben Shelton a battu Luca Van Assche 5-7, 6-3, 6-4 samedi 7 novembre a l'Accor Arena. Associated Press indique que la tete de serie n.3 a comble un 1-3 dans la manche decisive. Shelton est le premier Americain en finale a Paris depuis le sacre de Jack Sock en 2017. C'est sa troisieme finale de Masters 1000, la premiere hors du Canada.",
                "Van Assche, 47e mondial, disputait sa premiere demi-finale de Masters et a pris le premier set 7-5. Vendredi : Shelton bat Paul 6-4, 4-6, 6-3 ; Alcaraz bat Fritz 6-7(10), 7-5, 6-3 apres deux balles de match ; Ruud bat Borges 7-6(5), 6-4 ; Van Assche bat Hijikata 6-4, 6-7(4), 7-5. Alcaraz-Ruud n'est pas publie. La finale de dimanche n'est pas publiee."
            ]
        },
        "es": {
            "title": "Rolex Paris Masters SF: Ben Shelton vence a Luca Van Assche 5-7, 6-3, 6-4 y alcanza la final",
            "subtitle": "Primer estadounidense en la final de Bercy desde Jack Sock en 2017. Alcaraz-Ruud no se publica.",
            "excerpt": "Ben Shelton remonto un break en el tercer set para vencer a Luca Van Assche 5-7, 6-3, 6-4 y meterse en la final del Rolex Paris Masters.",
            "body": [
                "Ben Shelton gano 5-7, 6-3, 6-4 a Luca Van Assche el sabado 7 de noviembre en Accor Arena. Associated Press relata que el tercer cabeza de serie recupero un 1-3 en el set decisivo. Shelton es el primer estadounidense en la final de Paris desde el titulo de Jack Sock en 2017. Es su tercera final Masters 1000 y la primera fuera de Canada.",
                "Van Assche, 47 del mundo, jugaba su primera semifinal Masters y gano el primer set 7-5. Viernes: Shelton d. Paul 6-4, 4-6, 6-3; Alcaraz d. Fritz 6-7(10), 7-5, 6-3 tras dos bolas de partido; Ruud d. Borges 7-6(5), 6-4; Van Assche d. Hijikata 6-4, 6-7(4), 7-5. Alcaraz-Ruud no se publica. La final del domingo no se publica."
            ]
        },
        "de": {
            "title": "Rolex Paris Masters HF: Ben Shelton schlaegt Luca Van Assche 5:7, 6:3, 6:4 und steht im Finale",
            "subtitle": "Erster US-Amerikaner im Bercy-Finale seit Jack Sock 2017. Alcaraz gegen Ruud bleibt unveroeffentlicht.",
            "excerpt": "Ben Shelton dreht ein Break im dritten Satz und schlaegt Luca Van Assche 5:7, 6:3, 6:4 im Halbfinale der Rolex Paris Masters.",
            "body": [
                "Ben Shelton schlug Luca Van Assche am Samstag, den 7. November, in der Accor Arena 5:7, 6:3, 6:4. Associated Press schreibt, dass die Nummer 3 ein 1:3 im Entscheidungssatz aufholte. Shelton ist der erste Amerikaner im Pariser Finale seit Jack Socks Titel 2017. Es ist sein drittes Masters-1000-Finale, das erste ausserhalb Kanadas.",
                "Van Assche, Weltranglisten-47, stand in seinem ersten Masters-Halbfinale und nahm den ersten Satz 7:5. Freitag: Shelton gegen Paul 6:4, 4:6, 6:3; Alcaraz gegen Fritz 6:7(10), 7:5, 6:3 nach zwei Matchbaellen; Ruud gegen Borges 7:6(5), 6:4; Van Assche gegen Hijikata 6:4, 6:7(4), 7:5. Alcaraz gegen Ruud bleibt unveroeffentlicht. Das Finale am Sonntag ebenfalls."
            ]
        },
        "it": {
            "title": "Rolex Paris Masters SF: Ben Shelton batte Luca Van Assche 5-7, 6-3, 6-4 e vola in finale",
            "subtitle": "Primo americano in finale a Bercy da Jack Sock nel 2017. Alcaraz-Ruud non e pubblicato.",
            "excerpt": "Ben Shelton rimonta un break nel terzo set e batte Luca Van Assche 5-7, 6-3, 6-4 nella semifinale del Rolex Paris Masters.",
            "body": [
                "Ben Shelton ha battuto Luca Van Assche 5-7, 6-3, 6-4 sabato 7 novembre all'Accor Arena. Associated Press racconta che la testa di serie n.3 ha recuperato dallo 1-3 nel set decisivo. Shelton e il primo americano in finale a Parigi dal titolo di Jack Sock nel 2017. E la sua terza finale Masters 1000, la prima fuori dal Canada.",
                "Van Assche, 47 del ranking, giocava la prima semifinale Masters e ha preso il primo set 7-5. Venerdi: Shelton d. Paul 6-4, 4-6, 6-3; Alcaraz d. Fritz 6-7(10), 7-5, 6-3 dopo due palle match; Ruud d. Borges 7-6(5), 6-4; Van Assche d. Hijikata 6-4, 6-7(4), 7-5. Alcaraz-Ruud non e pubblicato. La finale di domenica non e pubblicata."
            ]
        },
        "pl": {
            "title": "Rolex Paris Masters PF: Ben Shelton pokonuje Luce Van Assche 5:7, 6:3, 6:4 i gra w finale",
            "subtitle": "Pierwszy Amerykanin w finale Bercy od Jacka Socka w 2017. Alcaraz-Ruud nieopublikowany.",
            "excerpt": "Ben Shelton odrobil breaka w trzecim secie i pokonal Luce Van Assche 5:7, 6:3, 6:4 w polfinale Rolex Paris Masters.",
            "body": [
                "Ben Shelton wygral z Luca Van Assche 5:7, 6:3, 6:4 w sobote 7 listopada na Accor Arena. Associated Press pisze, ze trzecia rakieta turnieju odrobil 1:3 w decydujacym secie. Shelton jest pierwszym Amerykaninem w finale Paryza od tytulu Jacka Socka w 2017. To jego trzeci final Masters 1000 i pierwszy poza Kanada.",
                "Van Assche, 47. w rankingu, gral pierwszy polfinal Masters i wzial pierwszego seta 7:5. Piatek: Shelton d. Paul 6:4, 4:6, 6:3; Alcaraz d. Fritz 6:7(10), 7:5, 6:3 po dwoch meczbolach; Ruud d. Borges 7:6(5), 6:4; Van Assche d. Hijikata 6:4, 6:7(4), 7:5. Alcaraz-Ruud nieopublikowany. Niedzielny final tez nie."
            ]
        },
        "zh": {
            "title": "巴黎大师赛半决赛：谢尔顿5-7、6-3、6-4击败范阿舍晋级决赛",
            "subtitle": "自2017年杰克·索克之后首位打进贝尔西决赛的美国人。阿尔卡拉斯对鲁德暂不发布。",
            "excerpt": "本·谢尔顿在第三盘挽回破发，以5-7、6-3、6-4击败卢卡·范阿舍，晋级巴黎大师赛决赛。",
            "body": [
                "本·谢尔顿11月7日周六在阿科尔体育馆以5-7、6-3、6-4击败卢卡·范阿舍。美联社称3号种子在决胜盘1-3落后后连赢四局。谢尔顿成为自2017年杰克·索克夺冠后首位打进巴黎决赛的美国人。这是他第三次大师赛决赛，也是首次在加拿大以外。",
                "世界排名47的范阿舍首次打进大师赛四强，并7-5拿下首盘。周五：谢尔顿6-4、4-6、6-3胜保罗；阿尔卡拉斯挽救两个赛点后6-7(10)、7-5、6-3胜弗里茨；鲁德7-6(5)、6-4胜博尔热斯；范阿舍6-4、6-7(4)、7-5胜土方。阿尔卡拉斯对鲁德暂不发布。周日决赛暂不发布。"
            ]
        },
        "ja": {
            "title": "パリ・マスターズ準決勝：シェルトンがバンアッシェに5-7、6-3、6-4で勝ち決勝へ",
            "subtitle": "2017年のジャック・ソック以来、ベルシー決勝に進んだ初の米国人。アルカラス対ルードは未掲載。",
            "excerpt": "ベン・シェルトンは第3セットでブレイクを取り返し、ルカ・バンアッシェを5-7、6-3、6-4で破ってロレックス・パリ・マスターズ決勝に進んだ。",
            "body": [
                "ベン・シェルトンは11月7日土曜、アコール・アリーナでルカ・バンアッシェに5-7、6-3、6-4で勝った。APは3シードが決勝セット1-3から4ゲーム連取したと伝える。シェルトンは2017年にジャック・ソックが優勝して以来、パリ決勝に進んだ初の米国人。マスターズ1000決勝は3度目でカナダ以外では初。",
                "世界47位のバンアッシェは初のマスターズ準決勝で第1セットを7-5。金曜：シェルトンがポールに6-4、4-6、6-3；アルカラスがマッチポイント2本をしのぎフリッツに6-7(10)、7-5、6-3；ルードがボルジェスに7-6(5)、6-4；バンアッシェがヒジカタに6-4、6-7(4)、7-5。アルカラス対ルードは未掲載。日曜決勝も未掲載。"
            ]
        },
        "ko": {
            "title": "파리 마스터스 준결승: 셸턴, 반 아슈에 5-7 6-3 6-4 승리하고 결승 진출",
            "subtitle": "2017년 잭 속 이후 베르시 결승에 오른 첫 미국인. 알카라스 대 루드는 미공개.",
            "excerpt": "벤 셸턴이 3세트에서 브레이크를 만회하며 루카 반 아슈를 5-7, 6-3, 6-4로 꺾고 롤렉스 파리 마스터스 결승에 올랐습니다.",
            "body": [
                "벤 셸턴은 11월 7일 토요일 아코르 아레나에서 루카 반 아슈를 5-7, 6-3, 6-4로 꺾었습니다. AP는 3번 시드가 결승 세트 1-3에서 네 게임을 연속으로 가져갔다고 전합니다. 셸턴은 2017년 잭 속이 우승한 이후 파리 결승에 오른 첫 미국인입니다. 마스터스 1000 결승은 세 번째, 캐나다 밖에서는 처음입니다.",
                "세계 47위 반 아슈는 첫 마스터스 준결승에서 1세트를 7-5로 가져갔습니다. 금요일: 셸턴 d. 폴 6-4 4-6 6-3; 알카라스가 매치포인트 2개를 살리고 프리츠에 6-7(10) 7-5 6-3; 루드 d. 보르게스 7-6(5) 6-4; 반 아슈 d. 히지카타 6-4 6-7(4) 7-5. 알카라스 대 루드는 미공개. 일요일 결승도 미공개입니다."
            ]
        },
        "ar": {
            "title": "باريس ماسترز نصف النهائي: بن شيلتون يهزم لوكا فان آش 5-7 و6-3 و6-4 ويبلغ النهائي",
            "subtitle": "اول اميركي في نهائي بيرسي منذ جاك سوك عام 2017. الكاراز ضد رود غير منشور.",
            "excerpt": "بن شيلتون يعود من كسر في المجموعة الثالثة ويهزم لوكا فان آش 5-7 و6-3 و6-4 لبلوغ نهائي رولكس باريس ماسترز.",
            "body": [
                "فاز بن شيلتون على لوكا فان آش 5-7 و6-3 و6-4 السبت 7 نوفمبر في اكور ارينا. اسوشيتد برس تقول ان المصنف الثالث عاد من 1-3 في المجموعة الحاسمة. شيلتون اول اميركي يبلغ نهائي باريس منذ لقب جاك سوك عام 2017. هذه نهائيته الثالثة في الماسترز 1000 والاولى خارج كندا.",
                "فان آش المصنف 47 كان في اول نصف نهائي ماسترز واخذ المجموعة الاولى 7-5. الجمعة: شيلتون على بول 6-4 و4-6 و6-3؛ الكاراز على فريتز 6-7(10) و7-5 و6-3 بعد انقاذ نقطتي مباراة؛ رود على بورغيس 7-6(5) و6-4؛ فان آش على هيجيكاتا 6-4 و6-7(4) و7-5. الكاراز ضد رود غير منشور. نهائي الاحد غير منشور."
            ]
        }
    },
    "f1-sao-paulo-gp-2026-fp3-verstappen-leads-antonelli": {
        "fr": {
            "title": "GP de Sao Paulo EL3 : Max Verstappen devance Kimi Antonelli de 0,025 s a Interlagos",
            "subtitle": "Derniere seance terminee. Qualifications non publiees. Pas de Sprint. Mercedes 630, Ferrari 504.",
            "excerpt": "Max Verstappen a tourne en 1:11.622 lors des EL3 samedi a Interlagos, 0,025 s devant le champion du monde Kimi Antonelli. Les qualifications ne sont pas publiees.",
            "body": [
                "Max Verstappen a signe le meilleur temps des essais libres 3 samedi 7 novembre a l'Autodromo Jose Carlos Pace en 1:11.622. La feuille FIA place Kimi Antonelli a +0,025 s, Lando Norris a +0,131 s, George Russell a +0,184 s, Charles Leclerc a +0,274 s et Oscar Piastri a +0,313 s. Lewis Hamilton n'a fait que sept tours, 12e.",
                "Vendredi : EL1 Norris 1:11.717, Antonelli +0,082 s, Verstappen +0,236 s. EL2 Antonelli 1:10.763. Pas de Sprint a Sao Paulo en 2026. Les qualifications du samedi apres-midi ne sont pas publiees. Classement inchange apres Mexico : Antonelli 380, Verstappen 261, Hamilton 259. Constructeurs : Mercedes 630, Ferrari 504."
            ]
        },
        "es": {
            "title": "GP de Sao Paulo EL3: Max Verstappen lidera a Kimi Antonelli por 0.025s en Interlagos",
            "subtitle": "Ultima practica cerrada. Clasificacion no publicada. Sin Sprint. Mercedes 630, Ferrari 504.",
            "excerpt": "Max Verstappen firmo 1:11.622 en la EL3 del sabado en Interlagos, 0.025s por delante del campeon Kimi Antonelli. La clasificacion no se publica.",
            "body": [
                "Max Verstappen fue el mas rapido en los Libres 3 el sabado 7 de noviembre en el Autodromo Jose Carlos Pace con 1:11.622. La clasificacion FIA pone a Kimi Antonelli a +0.025s, Lando Norris a +0.131s, George Russell a +0.184s, Charles Leclerc a +0.274s y Oscar Piastri a +0.313s. Lewis Hamilton solo dio siete vueltas y fue 12o.",
                "Viernes: EL1 Norris 1:11.717, Antonelli +0.082s, Verstappen +0.236s. EL2 Antonelli 1:10.763. No hay Sprint en Sao Paulo 2026. La clasificacion del sabado por la tarde no se publica. Tras Mexico: Antonelli 380, Verstappen 261, Hamilton 259. Constructores: Mercedes 630, Ferrari 504."
            ]
        },
        "de": {
            "title": "Sao-Paulo-GP FP3: Max Verstappen fuehrt Kimi Antonelli um 0,025s an in Interlagos",
            "subtitle": "Letztes Training komplett. Qualifying unveroeffentlicht. Kein Sprint. Mercedes 630, Ferrari 504.",
            "excerpt": "Max Verstappen faehrt 1:11.622 im Samstags-FP3 in Interlagos, 0,025s vor Weltmeister Kimi Antonelli. Das Qualifying bleibt unveroeffentlicht.",
            "body": [
                "Max Verstappen war am Samstag, den 7. November, im dritten Freien Training auf dem Autodromo Jose Carlos Pace mit 1:11.622 Schnellster. Das FIA-Blatt listet Kimi Antonelli +0,025s, Lando Norris +0,131s, George Russell +0,184s, Charles Leclerc +0,274s und Oscar Piastri +0,313s. Lewis Hamilton fuhr nur sieben Runden, Rang 12.",
                "Freitag: FP1 Norris 1:11.717, Antonelli +0,082s, Verstappen +0,236s. FP2 Antonelli 1:10.763. Kein Sprint in Sao Paulo 2026. Das Samstags-Qualifying bleibt unveroeffentlicht. Nach Mexiko: Antonelli 380, Verstappen 261, Hamilton 259. Konstrukteure: Mercedes 630, Ferrari 504."
            ]
        },
        "it": {
            "title": "GP di Sao Paulo PL3: Max Verstappen precede Kimi Antonelli di 0.025s a Interlagos",
            "subtitle": "Ultima prova completa. Qualifiche non pubblicate. Niente Sprint. Mercedes 630, Ferrari 504.",
            "excerpt": "Max Verstappen gira in 1:11.622 nelle PL3 del sabato a Interlagos, 0.025s davanti al campione Kimi Antonelli. Le qualifiche non sono pubblicate.",
            "body": [
                "Max Verstappen e stato il piu veloce nelle Prove Libere 3 sabato 7 novembre all'Autodromo Jose Carlos Pace in 1:11.622. Il foglio FIA mette Kimi Antonelli a +0.025s, Lando Norris a +0.131s, George Russell a +0.184s, Charles Leclerc a +0.274s e Oscar Piastri a +0.313s. Lewis Hamilton ha fatto solo sette giri, 12o.",
                "Venerdi: PL1 Norris 1:11.717, Antonelli +0.082s, Verstappen +0.236s. PL2 Antonelli 1:10.763. Niente Sprint a Sao Paulo nel 2026. Le qualifiche del sabato pomeriggio non sono pubblicate. Dopo il Messico: Antonelli 380, Verstappen 261, Hamilton 259. Costruttori: Mercedes 630, Ferrari 504."
            ]
        },
        "pl": {
            "title": "GP Sao Paulo T3: Max Verstappen wyprzedza Kimiego Antonellego o 0,025 s na Interlagos",
            "subtitle": "Ostatni trening zakonczony. Kwalifikacje nieopublikowane. Bez sprintu. Mercedes 630, Ferrari 504.",
            "excerpt": "Max Verstappen osiagnal 1:11.622 w sobotnim trzecim treningu na Interlagos, 0,025 s przed mistrzem Kimim Antonellim. Kwalifikacje nie sa publikowane.",
            "body": [
                "Max Verstappen byl najszybszy w trzecim treningu w sobote 7 listopada na Autodromo Jose Carlos Pace czasem 1:11.622. Arkusz FIA: Kimi Antonelli +0,025 s, Lando Norris +0,131 s, George Russell +0,184 s, Charles Leclerc +0,274 s, Oscar Piastri +0,313 s. Lewis Hamilton zrobil tylko siedem okrazen, 12. miejsce.",
                "Piatek: T1 Norris 1:11.717, Antonelli +0,082 s, Verstappen +0,236 s. T2 Antonelli 1:10.763. W Sao Paulo 2026 nie ma sprintu. Sobotnie kwalifikacje nie sa publikowane. Po Meksyku: Antonelli 380, Verstappen 261, Hamilton 259. Konstruktorzy: Mercedes 630, Ferrari 504."
            ]
        },
        "zh": {
            "title": "圣保罗大奖赛第三次练习：维斯塔潘1:11.622领先安东内利0.025秒",
            "subtitle": "末次练习结束。排位赛暂不发布。本周末无冲刺赛。梅赛德斯630，法拉利504。",
            "excerpt": "马克斯·维斯塔潘周六在英特拉格斯第三次练习跑出1:11.622，领先世界冠军基米·安东内利0.025秒。排位赛暂不发布。",
            "body": [
                "马克斯·维斯塔潘11月7日周六在何塞·卡洛斯·帕塞赛道第三次自由练习以1:11.622最快。国际汽联成绩单：安东内利+0.025秒，诺里斯+0.131秒，拉塞尔+0.184秒，勒克莱尔+0.274秒，皮亚斯特里+0.313秒。刘易斯·汉密尔顿只跑七圈排第12。",
                "周五：第一次练习诺里斯1:11.717，安东内利+0.082秒，维斯塔潘+0.236秒。第二次练习安东内利1:10.763。2026年圣保罗无冲刺赛。周六下午排位赛暂不发布。墨西哥站后积分不变：安东内利380，维斯塔潘261，汉密尔顿259。车队：梅赛德斯630，法拉利504。"
            ]
        },
        "ja": {
            "title": "サンパウロGP FP3：フェルスタッペンが1:11.622、アントネッリに0.025秒差",
            "subtitle": "最終練習終了。予選は未掲載。スプリントなし。メルセデス630、フェラーリ504。",
            "excerpt": "マックス・フェルスタッペンが土曜のFP3で1:11.622を記録し、世界王者キミ・アントネッリに0.025秒差。予選は未掲載。",
            "body": [
                "マックス・フェルスタッペンは11月7日土曜、アウトドロモ・ジョゼ・カルロス・パーチェのFP3で1:11.622が最速。FIAの表はキミ・アントネッリ+0.025秒、ランド・ノリス+0.131秒、ジョージ・ラッセル+0.184秒、シャルル・ルクレール+0.274秒、オスカー・ピアストリ+0.313秒。ルイス・ハミルトンは7周のみで12位。",
                "金曜：FP1ノリス1:11.717、アントネッリ+0.082秒、フェルスタッペン+0.236秒。FP2アントネッリ1:10.763。2026年サンパウロにスプリントはない。土曜午後の予選は未掲載。メキシコ後の順位は不変：アントネッリ380、フェルスタッペン261、ハミルトン259。コンストラクター：メルセデス630、フェラーリ504。"
            ]
        },
        "ko": {
            "title": "상파울루 GP FP3: 베르스타펜 1:11.622, 안토넬리를 0.025초 차로 선두",
            "subtitle": "최종 연습 종료. 예선은 미공개. 스프린트 없음. 메르세데스 630, 페라리 504.",
            "excerpt": "막스 베르스타펜이 토요일 인테를라고스 FP3에서 1:11.622를 찍어 월드 챔피언 키미 안토넬리를 0.025초 앞섰습니다. 예선은 미공개입니다.",
            "body": [
                "막스 베르스타펜은 11월 7일 토요일 아우토드로모 조제 카를루스 파세 FP3에서 1:11.622로 가장 빨랐습니다. FIA 기록은 키미 안토넬리 +0.025초, 란도 노리스 +0.131초, 조지 러셀 +0.184초, 샤를 르클레르 +0.274초, 오스카 피아스트리 +0.313초. 루이스 해밀턴은 7바퀴만 돌고 12위.",
                "금요일: FP1 노리스 1:11.717, 안토넬리 +0.082초, 베르스타펜 +0.236초. FP2 안토넬리 1:10.763. 2026 상파울루에는 스프린트가 없습니다. 토요일 오후 예선은 미공개. 멕시코 이후 순위 불변: 안토넬리 380, 베르스타펜 261, 해밀턴 259. 컨스트럭터: 메르세데스 630, 페라리 504."
            ]
        },
        "ar": {
            "title": "جائزة ساو باولو الحصة الثالثة: ماكس فيرستابن يتقدم على كيمي انطونيلي بـ0.025 ثانية في انترلاغوس",
            "subtitle": "التدريب الاخير اكتمل. التصفيات غير منشورة. لا سباق قصير. مرسيدس 630 وفيراري 504.",
            "excerpt": "ماكس فيرستابن يسجل 1:11.622 في الحصة الثالثة السبت في انترلاغوس، متقدما 0.025 ثانية على البطل كيمي انطونيلي. التصفيات غير منشورة.",
            "body": [
                "تصدر ماكس فيرستابن الحصة الثالثة السبت 7 نوفمبر في اوتودرومو خوسيه كارلوس باسي بزمن 1:11.622. ورقة الاتحاد الدولي تضع كيمي انطونيلي عند +0.025ث ولاندو نوريس +0.131ث وجورج راسل +0.184ث وشارل لوكلير +0.274ث واوسكار بياستري +0.313ث. لويس هاميلتون اتم سبعة لفات فقط وحل 12.",
                "الجمعة: الحصة الاولى نوريس 1:11.717، انطونيلي +0.082ث، فيرستابن +0.236ث. الحصة الثانية انطونيلي 1:10.763. لا سباق قصير في ساو باولو 2026. تصفيات بعد ظهر السبت غير منشورة. بعد المكسيك: انطونيلي 380، فيرستابن 261، هاميلتون 259. الصانعون: مرسيدس 630 وفيراري 504."
            ]
        }
    },
    "pga-tour-wwt-championship-2026-round2-james-leads-malnati": {
        "fr": {
            "title": "WWT Championship 2e tour : Ben James signe un 64 et mene a 15 sous le par a El Cardonal",
            "subtitle": "James 65-64=129, un coup devant Peter Malnati. Chris Kirk enchaine 63 puis 72. Le 3e tour n'est pas publie.",
            "excerpt": "Ben James a rendu un 64 vendredi pour atteindre 129, 15 sous le par, et mener le World Wide Technology Championship apres 36 trous a Los Cabos.",
            "body": [
                "Ben James a signe un 64 vendredi 6 novembre et mene le World Wide Technology Championship a 15 sous le par (129). Associated Press decrit cinq birdies d'affilee autour du turn a El Cardonal at Diamante (par 72, 7 452 yards). Peter Malnati est a 130 (66-64). Zac Blair 132. Stephan Jaeger et Denny McCarthy 133.",
                "Chris Kirk avait mene apres un 63 sans bogey jeudi, puis un 72, il est a 135. Le cut est tombe a 5 sous le par (139). Bourse : 6 millions de dollars. Le 3e tour samedi n'est pas publie comme tableau ferme a 54 trous."
            ]
        },
        "es": {
            "title": "WWT Championship 2a ronda: Ben James firma 64 y lidera a 15 bajo en El Cardonal",
            "subtitle": "James 65-64=129, un golpe por delante de Peter Malnati. Chris Kirk sigue 63 con 72. La 3a ronda no se publica.",
            "excerpt": "Ben James entrego un 64 el viernes para llegar a 129, 15 bajo par, y liderar el World Wide Technology Championship tras 36 hoyos en Los Cabos.",
            "body": [
                "Ben James firmo un 64 el viernes 6 de noviembre y lidera el World Wide Technology Championship a 15 bajo (129). Associated Press relata cinco birdies seguidos en el turn en El Cardonal at Diamante (par 72, 7.452 yardas). Peter Malnati esta a 130 (66-64). Zac Blair 132. Stephan Jaeger y Denny McCarthy 133.",
                "Chris Kirk lidero tras un 63 sin bogeys el jueves, luego un 72, y esta a 135. El corte cayo en 5 bajo (139). Bolsa: 6 millones de dolares. La tercera ronda del sabado no se publica como tablero cerrado a 54 hoyos."
            ]
        },
        "de": {
            "title": "WWT Championship Runde 2: Ben James spielt 64 und fuehrt mit 15 unter in El Cardonal",
            "subtitle": "James 65-64=129, ein Schlag vor Peter Malnati. Chris Kirk folgt auf 63 mit 72. Runde 3 unveroeffentlicht.",
            "excerpt": "Ben James spielt am Freitag 64 und liegt nach 36 Loechern bei 15 unter 129 in Fuehrung bei der World Wide Technology Championship in Los Cabos.",
            "body": [
                "Ben James spielte am Freitag, den 6. November, eine 64 und fuehrt die World Wide Technology Championship mit 15 unter (129) an. Associated Press beschreibt fuenf Birdies in Folge um den Turn in El Cardonal at Diamante (Par 72, 7.452 Yards). Peter Malnati steht bei 130 (66-64). Zac Blair 132. Stephan Jaeger und Denny McCarthy 133.",
                "Chris Kirk fuehrte nach einer bogeyfreien 63 am Donnerstag, dann 72, jetzt 135. Der Cut lag bei 5 unter (139). Preisgeld: 6 Millionen Dollar. Die dritte Runde am Samstag wird nicht als geschlossenes 54-Loecher-Board veroeffentlicht."
            ]
        },
        "it": {
            "title": "WWT Championship 2o giro: Ben James firma 64 e guida a 15 sotto a El Cardonal",
            "subtitle": "James 65-64=129, un colpo su Peter Malnati. Chris Kirk segue 63 con 72. Il 3o giro non e pubblicato.",
            "excerpt": "Ben James consegna un 64 venerdi e arriva a 129, 15 sotto, in testa al World Wide Technology Championship dopo 36 buche a Los Cabos.",
            "body": [
                "Ben James ha firmato un 64 venerdi 6 novembre e guida il World Wide Technology Championship a 15 sotto (129). Associated Press racconta cinque birdie di fila intorno al turn a El Cardonal at Diamante (par 72, 7.452 iarde). Peter Malnati e a 130 (66-64). Zac Blair 132. Stephan Jaeger e Denny McCarthy 133.",
                "Chris Kirk guidava dopo un 63 senza bogey giovedi, poi un 72, ora e a 135. Il taglio e caduto a 5 sotto (139). Montepremi: 6 milioni di dollari. Il terzo giro di sabato non e pubblicato come tabellone chiuso a 54 buche."
            ]
        },
        "pl": {
            "title": "WWT Championship 2. runda: Ben James gra 64 i prowadzi na 15 pod parem na El Cardonal",
            "subtitle": "James 65-64=129, jeden uderzenie przed Peterem Malnatim. Chris Kirk po 63 gra 72. 3. runda nieopublikowana.",
            "excerpt": "Ben James oddal 64 w piatek i jest na 129, 15 pod parem, na czele World Wide Technology Championship po 36 dołkach w Los Cabos.",
            "body": [
                "Ben James zagral 64 w piatek 6 listopada i prowadzi w World Wide Technology Championship na 15 pod (129). Associated Press opisuje piec birdie z rzedu przy turnie na El Cardonal at Diamante (par 72, 7452 jardy). Peter Malnati ma 130 (66-64). Zac Blair 132. Stephan Jaeger i Denny McCarthy 133.",
                "Chris Kirk prowadzil po 63 bez bogeya w czwartek, potem 72, teraz 135. Cut padl na 5 pod (139). Pula: 6 milionow dolarow. Sobotnia 3. runda nie jest publikowana jako zamknieta tablica po 54 dołkach."
            ]
        },
        "zh": {
            "title": "WWT锦标赛第二轮：本·詹姆斯64杆以15杆优势领先埃尔卡多纳尔",
            "subtitle": "詹姆斯65-64=129，领先彼得·马尔纳蒂一杆。柯克63后打出72。第三轮暂不发布。",
            "excerpt": "本·詹姆斯周五打出64杆，36洞结束后以15杆129杆领跑洛斯卡沃斯世界广域科技锦标赛。",
            "body": [
                "本·詹姆斯11月6日周五打出64杆，以低于标准杆15杆的129杆领跑世界广域科技锦标赛。美联社称他在埃尔卡多纳尔（标准杆72，7452码）转场前后连抓五个小鸟。彼得·马尔纳蒂130杆（66-64）。扎克·布莱尔132。斯蒂芬·耶格尔与丹尼·麦卡锡133。",
                "克里斯·柯克周四无柏忌63杆领先，随后72杆现为135。晋级线为低于标准杆5杆（139）。奖金600万美元。周六第三轮不作为54洞封闭榜发布。"
            ]
        },
        "ja": {
            "title": "WWT選手権第2ラウンド：ベン・ジェームズが64を出し15アンダーで首位",
            "subtitle": "ジェームズ65-64=129、ピーター・マルナティに1打差。カークは63の後72。第3ラウンドは未掲載。",
            "excerpt": "ベン・ジェームズは金曜に64をマークし、36ホール終了時点で15アンダー129、ロスカボスのワールドワイド・テクノロジー選手権を首位で折り返した。",
            "body": [
                "ベン・ジェームズは11月6日金曜に64を出し、ワールドワイド・テクノロジー選手権を15アンダー129で首位。APはエル・カルドナル（パー72、7452ヤード）のターン前後でバーディー5連続と伝える。ピーター・マルナティは130（66-64）。ザック・ブレア132。ステファン・イェーガーとデニー・マッカーシー133。",
                "クリス・カークは木曜ボギーなし63で首位、その後72で135。カットは5アンダー139。賞金600万ドル。土曜の第3ラウンドは54ホール確定ボードとしては掲載しない。"
            ]
        },
        "ko": {
            "title": "WWT 챔피언십 2라운드: 벤 제임스가 64타로 15언더 선두",
            "subtitle": "제임스 65-64=129, 피터 말나티에 1타 차. 커크는 63 뒤 72. 3라운드는 미공개.",
            "excerpt": "벤 제임스가 금요일 64타를 쳐 15언더 129타로 로스카보스 WWT 챔피언십 36홀 선두에 올랐습니다.",
            "body": [
                "벤 제임스는 11월 6일 금요일 64타를 쳐 월드 와이드 테크놀로지 챔피언십을 15언더 129로 이끌고 있습니다. AP는 엘 카르도날(파 72, 7452야드) 턴 전후 버디 5연속을 전합니다. 피터 말나티 130(66-64). 잭 블레어 132. 스테판 예거와 데니 매카시 133.",
                "크리스 커크는 목요일 보기 없는 63으로 선두였다가 72를 쳐 135입니다. 컷은 5언더 139. 상금 600만 달러. 토요일 3라운드는 54홀 확정 리더보드로 올리지 않습니다."
            ]
        },
        "ar": {
            "title": "بطولة WWT الجولة الثانية: بن جيمس يسجل 64 ويتقدم بـ15 تحت في ال كاردونال",
            "subtitle": "جيمس 65-64=129، ضربة امام بيتر مالناتي. كيرك بعد 63 يسجل 72. الجولة الثالثة غير منشورة.",
            "excerpt": "بن جيمس يسجل 64 الجمعة ليصل الى 129، 15 تحت البار، ويتصدر بطولة وورلد وايد تكنولوجي بعد 36 حفرة في لوس كابوس.",
            "body": [
                "سجل بن جيمس 64 الجمعة 6 نوفمبر ويتصدر بطولة وورلد وايد تكنولوجي بـ15 تحت (129). اسوشيتد برس تصف خمسة بيردي متتالية حول المنعطف في ال كاردونال ات ديامانتي (بار 72، 7452 ياردة). بيتر مالناتي عند 130 (66-64). زاك بلير 132. ستيفان ياغر وديني مكارثي 133.",
                "كريس كيرك تصدر بعد 63 دون بوجي الخميس ثم سجل 72 وهو عند 135. خط القطع 5 تحت (139). الجائزة 6 ملايين دولار. الجولة الثالثة السبت لا تنشر كجدول مغلق بعد 54 حفرة."
            ]
        }
    },
    "pl-mw10-leeds-1-0-tottenham-okafor-2026": {
        "fr": {
            "title": "Premier League J10 : Noah Okafor offre le 1-0 a Leeds contre Tottenham",
            "subtitle": "Okafor marque 97 secondes apres son entree. Vendredi : Everton 3-1 Coventry. Arsenal-Hull non publie.",
            "excerpt": "Noah Okafor a marque a la 79e minute et Leeds United a battu Tottenham Hotspur 1-0 a Elland Road samedi.",
            "body": [
                "Leeds United a battu Tottenham Hotspur 1-0 samedi 7 novembre a Elland Road. Noah Okafor a marque a la 79e minute, 97 secondes apres avoir remplace Lukas Nmecha. ESPN et Opta indiquent qu'Harry Wilson a prolonge un long throw-in avant la frappe. Affluence : 36 921. Arbitre : John Brooks. Leeds termine une serie de cinq matches sans victoire. Tottenham voit s'arreter une serie de trois succes.",
                "Vendredi 6 novembre : Everton 3-1 Coventry, Yann Gboho 52, Thierno Barry 56 et 61, Kiernan Dewsbury-Hall 81, affluence 52 395. Tableau conservateur apres ces deux matches termines de la J10 : Arsenal 24 en 9, City 21, Brighton 19, Chelsea 16, Everton 16 en 10, Leeds 14 en 10. Arsenal-Hull et le reste du samedi ne sont pas publies."
            ]
        },
        "es": {
            "title": "Premier League J10: gol de Noah Okafor y Leeds gana 1-0 a Tottenham",
            "subtitle": "Okafor marca 97 segundos despues de entrar. Viernes: Everton 3-1 Coventry. Arsenal-Hull no se publica.",
            "excerpt": "Noah Okafor marco en el minuto 79 y Leeds United gano 1-0 a Tottenham Hotspur en Elland Road el sabado.",
            "body": [
                "Leeds United gano 1-0 a Tottenham Hotspur el sabado 7 de noviembre en Elland Road. Noah Okafor marco en el 79, 97 segundos despues de sustituir a Lukas Nmecha. ESPN y Opta dicen que Harry Wilson prolongo un saque largo antes del disparo. Asistencia: 36.921. Arbitro: John Brooks. Leeds corta cinco partidos sin ganar. Tottenham corta una racha de tres victorias.",
                "Viernes 6 de noviembre: Everton 3-1 Coventry, Yann Gboho 52, Thierno Barry 56 y 61, Kiernan Dewsbury-Hall 81, asistencia 52.395. Tabla conservadora tras esos dos partidos cerrados de la J10: Arsenal 24 en 9, City 21, Brighton 19, Chelsea 16, Everton 16 en 10, Leeds 14 en 10. Arsenal-Hull y el resto del sabado no se publican."
            ]
        },
        "de": {
            "title": "Premier League ST10: Noah Okafor trifft, Leeds schlaegt Tottenham 1:0",
            "subtitle": "Okafor trifft 97 Sekunden nach seiner Einwechslung. Freitag: Everton 3:1 Coventry. Arsenal gegen Hull unveroeffentlicht.",
            "excerpt": "Noah Okafor trifft in der 79. Minute, Leeds United schlaegt Tottenham Hotspur am Samstag in Elland Road 1:0.",
            "body": [
                "Leeds United schlug Tottenham Hotspur am Samstag, den 7. November, in Elland Road 1:0. Noah Okafor traf in der 79., 97 Sekunden nach seiner Einwechslung fuer Lukas Nmecha. ESPN und Opta berichten, dass Harry Wilson einen langen Einwurf verlaengerte. Zuschauer: 36.921. Schiedsrichter: John Brooks. Leeds beendet fuenf Spiele ohne Sieg. Tottenhams Dreier-Siegesserie endet.",
                "Freitag, 6. November: Everton 3:1 Coventry, Yann Gboho 52, Thierno Barry 56 und 61, Kiernan Dewsbury-Hall 81, 52.395 Zuschauer. Konservative Tabelle nach diesen zwei beendeten ST10-Spielen: Arsenal 24 aus 9, City 21, Brighton 19, Chelsea 16, Everton 16 aus 10, Leeds 14 aus 10. Arsenal gegen Hull und der Rest des Samstags bleiben unveroeffentlicht."
            ]
        },
        "it": {
            "title": "Premier League 10a: gol di Noah Okafor, Leeds batte il Tottenham 1-0",
            "subtitle": "Okafor segna 97 secondi dopo l'ingresso. Venerdi: Everton 3-1 Coventry. Arsenal-Hull non pubblicato.",
            "excerpt": "Noah Okafor segna al 79' e il Leeds United batte il Tottenham Hotspur 1-0 a Elland Road sabato.",
            "body": [
                "Il Leeds United ha battuto il Tottenham Hotspur 1-0 sabato 7 novembre a Elland Road. Noah Okafor ha segnato al 79', 97 secondi dopo aver sostituito Lukas Nmecha. ESPN e Opta dicono che Harry Wilson ha prolungato una rimesse lunga. Pubblico: 36.921. Arbitro: John Brooks. Il Leeds interrompe cinque gare senza vittorie. Il Tottenham ferma una striscia di tre successi.",
                "Venerdi 6 novembre: Everton 3-1 Coventry, Yann Gboho 52, Thierno Barry 56 e 61, Kiernan Dewsbury-Hall 81, 52.395 spettatori. Classifica conservativa dopo queste due gare chiuse della 10a: Arsenal 24 in 9, City 21, Brighton 19, Chelsea 16, Everton 16 in 10, Leeds 14 in 10. Arsenal-Hull e il resto del sabato non sono pubblicati."
            ]
        },
        "pl": {
            "title": "Premier League kol. 10: gol Noaha Okafora, Leeds wygrywa z Tottenhamem 1:0",
            "subtitle": "Okafor trafia 97 sekund po wejściu. Piatek: Everton 3:1 Coventry. Arsenal-Hull nieopublikowany.",
            "excerpt": "Noah Okafor strzelil w 79. minucie, a Leeds United pokonal Tottenham Hotspur 1:0 na Elland Road w sobote.",
            "body": [
                "Leeds United wygral z Tottenhamem 1:0 w sobote 7 listopada na Elland Road. Noah Okafor strzelil w 79. minucie, 97 sekund po zmianie Lukasa Nmechy. ESPN i Opta podaja, ze Harry Wilson przedluzyl dlugie wrzut z autu. Frekwencja: 36 921. Sedzia: John Brooks. Leeds konczy piec meczow bez wygranej. Tottenham przerywa serie trzech zwyciestw.",
                "Piatek 6 listopada: Everton 3:1 Coventry, Yann Gboho 52, Thierno Barry 56 i 61, Kiernan Dewsbury-Hall 81, 52 395 widzow. Konserwatywna tabela po tych dwoch zakonczonych meczach 10. kolejki: Arsenal 24 z 9, City 21, Brighton 19, Chelsea 16, Everton 16 z 10, Leeds 14 z 10. Arsenal-Hull i reszta soboty nie sa publikowane."
            ]
        },
        "zh": {
            "title": "英超第10轮：奥卡福尔绝杀，利兹联1-0击败热刺",
            "subtitle": "奥卡福尔上场97秒破门。周五：埃弗顿3-1考文垂。阿森纳对赫尔城暂不发布。",
            "excerpt": "诺亚·奥卡福尔第79分钟破门，利兹联周六在埃兰路1-0击败托特纳姆热刺。",
            "body": [
                "利兹联11月7日周六在埃兰路1-0击败托特纳姆热刺。诺亚·奥卡福尔第79分钟进球，换下卢卡斯·恩梅查后97秒。ESPN与Opta称哈里·威尔逊将界外球摆渡给奥卡福尔。观众36921人。主裁约翰·布鲁克斯。利兹结束五场不胜。热刺三连胜中止。",
                "11月6日周五：埃弗顿3-1考文垂，扬·格博霍52分钟，蒂尔诺·巴里56、61分钟，基尔南·杜斯伯里-霍尔81分钟，观众52395人。仅计入这两场已完赛第10轮的保守积分：阿森纳9场24分，曼城21分，布莱顿19分，切尔西16分，埃弗顿10场16分，利兹10场14分。阿森纳对赫尔城及周六其余比赛暂不发布。"
            ]
        },
        "ja": {
            "title": "プレミアリーグ第10節：オカフォが決勝点、リーズがトッテナムに1-0",
            "subtitle": "オカフォは投入97秒で得点。金曜：エバートン3-1コヴェントリー。アーセナル対ハルは未掲載。",
            "excerpt": "ノア・オカフォが79分に決め、リーズ・ユナイテッドは土曜にエランド・ロードでトッテナム・ホットスパーを1-0で破った。",
            "body": [
                "リーズ・ユナイテッドは11月7日土曜、エランド・ロードでトッテナムを1-0で破った。ノア・オカフォはルーカス・ンメチャに代わって79分、投入97秒で決めた。ESPNとOptaはハリー・ウィルソンがロングスローを繋いだと伝える。観客36921人。主審ジョン・ブルックス。リーズは5試合勝利なしを終えた。トッテナムは3連勝が止まった。",
                "11月6日金曜：エバートン3-1コヴェントリー、ヤン・グボホ52分、ティエルノ・バリー56分と61分、キーナン・デューズベリー＝ホール81分、観客52395人。終了した第10節2試合のみの保守的順位：アーセナル9試合24、シティ21、ブライトン19、チェルシー16、エバートン10試合16、リーズ10試合14。アーセナル対ハルと土曜の残りは未掲載。"
            ]
        },
        "ko": {
            "title": "프리미어리그 10라운드: 오카포르 결승골, 리즈가 토트넘에 1-0 승리",
            "subtitle": "오카포르는 투입 97초 만에 골. 금요일: 에버턴 3-1 코번트리. 아스널 대 헐은 미공개.",
            "excerpt": "노아 오카포르가 79분에 골을 넣어 리즈 유나이티드가 토요일 엘랜드 로드에서 토트넘 홋스퍼를 1-0으로 꺾었습니다.",
            "body": [
                "리즈 유나이티드는 11월 7일 토요일 엘랜드 로드에서 토트넘을 1-0으로 꺾었습니다. 노아 오카포르는 루카스 은메차를 대신해 79분, 투입 97초 만에 넣었습니다. ESPN과 Opta는 해리 윌슨이 롱스로인을 연결했다고 전합니다. 관중 36,921명. 주심 존 브룩스. 리즈는 5경기 무승 행진을 끊었습니다. 토트넘의 3연승도 끝났습니다.",
                "11월 6일 금요일: 에버턴 3-1 코번트리, 얀 그보호 52분, 티에르노 배리 56·61분, 키어넌 듀즈베리홀 81분, 관중 52,395명. 끝난 10라운드 두 경기만 반영한 보수적 순위: 아스널 9경기 24, 시티 21, 브라이턴 19, 첼시 16, 에버턴 10경기 16, 리즈 10경기 14. 아스널 대 헐과 토요일 나머지는 미공개입니다."
            ]
        },
        "ar": {
            "title": "الدوري الانجليزي الجولة 10: هدف نوح اوكافور يمنح ليدز الفوز 1-0 على توتنهام",
            "subtitle": "اوكافور يسجل بعد 97 ثانية من دخوله. الجمعة: ايفرتون 3-1 كوفنتري. ارسنال ضد هال غير منشور.",
            "excerpt": "نوح اوكافور يسجل في الدقيقة 79 وليدز يونايتد يفوز 1-0 على توتنهام هوتسبير في ايلاند رود السبت.",
            "body": [
                "فاز ليدز يونايتد على توتنهام 1-0 السبت 7 نوفمبر في ايلاند رود. سجل نوح اوكافور في الدقيقة 79، بعد 97 ثانية من حلول محل لوكاس نميشا. ESPN وOpta يقولان ان هاري ويلسون ابقى رمية طويلة قبل التسديدة. الحضور 36921. الحكم جون بروكس. ليدز ينهي خمسة مباريات بلا فوز. توتنهام يتوقف عن ثلاث انتصارات متتالية.",
                "الجمعة 6 نوفمبر: ايفرتون 3-1 كوفنتري، يان غبوهو 52، تيرنو باري 56 و61، كيرنان ديوسبري هول 81، الحضور 52395. جدول محافظ بعد هاتين المباراتين المكتملتين من الجولة 10: ارسنال 24 من 9، سيتي 21، برايتون 19، تشيلسي 16، ايفرتون 16 من 10، ليدز 14 من 10. ارسنال ضد هال وبقية السبت غير منشورة."
            ]
        }
    },
}


def lint_obj(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            lint_obj(v, path + "/" + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            lint_obj(v, path + "[%s]" % i)
    elif isinstance(obj, str):
        s = re.sub(r"https?://\S+", "", obj)
        if "—" in s or "--" in s:
            raise SystemExit("dash in %s: %s" % (path, s[:80]))


lint_obj(NOV07_STORIES)
print("All November 7 story translations validated: 0 em-dashes and 0 double-hyphens.")

snippet_parts = []
for slug, langs in NOV07_STORIES.items():
    snippet_parts.append(f"{json.dumps(slug)}: {json.dumps(langs, ensure_ascii=False, indent=2)},")
snippet = "\n".join(snippet_parts) + "\n"

stories_file = os.path.join(os.path.dirname(__file__), "../../frontend/src/i18n/stories.ts")
with open(stories_file, "r", encoding="utf-8") as f:
    content = f.read()

target = "export const STORY_I18N: Record<string, LocMap> = {\n"
assert target in content, "Target line not found in stories.ts"

new_content = content.replace(target, target + snippet, 1)
with open(stories_file, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Successfully injected November 7 translations into frontend/src/i18n/stories.ts")
