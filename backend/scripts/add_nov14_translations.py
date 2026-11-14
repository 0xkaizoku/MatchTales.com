#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add 14 November 2026 story translations (all 9 non-en locales) and entity translations to names.ts."""
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

NOV14_STORIES = {
    "uwcl-barcelona-arsenal-1-1-nations-league-thursday-2026": {
        "fr": {
            "title": "Arsenal tient Barcelone 1-1 au Camp Nou ; Kane envoie l'Angleterre en quarts 2-1",
            "subtitle": "Maanum et Graham Hansen se partagent l'UWCL pendant que Kane, pour sa 126e selection, prepare le choc Espagne-Angleterre de dimanche a Madrid.",
            "excerpt": "Frida Maanum ouvre a la 22e, Caroline Graham Hansen egalise a la 59e : 1-1. Angleterre 2-1 Croatie, Italie 3-1 France, Espagne 2-0 Tchequie.",
            "body": [
                "Arsenal Women quitte le Spotify Camp Nou avec un 1-1 jeudi 12 novembre et met fin au debut parfait du FC Barcelona Femeni en UWCL. Frida Maanum inscrit le premier but a la 22e minute apres un arret sur Caitlin Foord. Barcelone aligne 24 tirs et pres de 70% de possession avant que Caroline Graham Hansen ne rentre dans l'axe et ne marque a la 59e. Alessia Russo rate une tete face au but vide. Arsenal est 4e avec 8 points ; Barcelone a 10, a egalite avec Lyon.",
                "La Ligue des nations masculine livre trois finales la meme nuit. A Wembley, Morgan Rogers marque a la 24e et Harry Kane transforme un penalty a la 64e pour sa 126e selection record apres l'egalisation de Petar Sucic (59e). L'Angleterre est en quarts avec 12 points. L'Italie revient de 0-1 pour battre la France 3-1 a San Siro (Olise 10e, Pio Esposito 26e et 75e pen, Frattesi 63e). L'Espagne bat la Tchequie a 10 2-0 a Prague (Baena 39e pen, Pubill 90+6).",
                "Dimanche 15 novembre, l'Espagne recoit l'Angleterre au Metropolitano (19h45 GMT) pour la premiere place du groupe A3. Le classement Premier League reste fige pendant la treve internationale : Arsenal 27, Brighton 22, Manchester City 21, Liverpool 18."
            ]
        },
        "es": {
            "title": "El Arsenal empata 1-1 en el Camp Nou; Kane mete a Inglaterra en cuartos 2-1",
            "subtitle": "Maanum y Graham Hansen se reparten el punto UWCL mientras Kane, en su cap 126, deja listo el Espana-Inglaterra del domingo en Madrid.",
            "excerpt": "Frida Maanum abre en el 22 y Caroline Graham Hansen empata en el 59: 1-1. Inglaterra 2-1 Croacia, Italia 3-1 Francia, Espana 2-0 Chequia.",
            "body": [
                "Arsenal Women sale del Spotify Camp Nou con un 1-1 el jueves 12 de noviembre y corta el inicio perfecto del FC Barcelona Femeni en la UWCL. Frida Maanum marca en el minuto 22 tras una parada a Caitlin Foord. Barcelona acumula 24 disparos y cerca del 70% de posesion antes de que Caroline Graham Hansen entre hacia dentro y definiera en el 59. Alessia Russo desvia de cabeza un gol cantado. El Arsenal es cuarto con 8 puntos; Barcelona tiene 10, empatado con Lyon.",
                "La Liga de Naciones masculina cierra tres partidos la misma noche. En Wembley, Morgan Rogers marca en el 24 y Harry Kane transforma un penalti en el 64 en su cap 126 de record tras el empate de Petar Sucic (59). Inglaterra esta en cuartos con 12 puntos. Italia remonta y gana 3-1 a Francia en San Siro (Olise 10, Pio Esposito 26 y 75 pen, Frattesi 63). Espana vence 2-0 a Chequia con diez (Baena 39 pen, Pubill 90+6).",
                "El domingo 15 de noviembre Espana recibe a Inglaterra en el Metropolitano (19:45 GMT) por el liderato del grupo A3. La Premier sigue congelada en el paron: Arsenal 27, Brighton 22, Manchester City 21, Liverpool 18."
            ]
        },
        "de": {
            "title": "Arsenal haelt Barcelona 1:1 im Camp Nou; Kane schiesst England mit 2:1 ins Viertelfinale",
            "subtitle": "Maanum und Graham Hansen teilen die UWCL-Punkte, waehrend Kane bei Cap 126 das Spanien-England-Duell am Sonntag in Madrid vorbereitet.",
            "excerpt": "Frida Maanum trifft in der 22., Caroline Graham Hansen gleicht in der 59. aus: 1:1. England 2:1 Kroatien, Italien 3:1 Frankreich, Spanien 2:0 Tschechien.",
            "body": [
                "Arsenal Women verlaesst das Spotify Camp Nou am Donnerstag, 12. November, mit einem 1:1 und beendet den perfekten UWCL-Start von FC Barcelona Femeni. Frida Maanum trifft in der 22. Minute, nachdem Caitlin Foord geblockt wurde. Barcelona kommt auf 24 Schuesse und fast 70 Prozent Ballbesitz, ehe Caroline Graham Hansen in der 59. nach innen zieht und trifft. Alessia Russo koepft ein offenes Tor daneben. Arsenal steht mit 8 Punkten Vierter; Barcelona hat 10, gleichauf mit Lyon.",
                "Die Nations League der Maenner liefert drei Finalergebnisse in derselben Nacht. In Wembley trifft Morgan Rogers in der 24., Harry Kane verwandelt in der 64. einen Elfmeter bei seinem 126. Laenderspiel-Rekord, nachdem Petar Sucic (59.) ausgeglichen hatte. England ist mit 12 Punkten im Viertelfinale. Italien dreht gegen Frankreich ein 3:1 in San Siro (Olise 10., Pio Esposito 26. und 75. Elfm., Frattesi 63.). Spanien schlaegt Tschechien in Unterzahl 2:0 in Prag (Baena 39. Elfm., Pubill 90+6).",
                "Am Sonntag, 15. November, empfaengt Spanien England im Metropolitano (19:45 GMT) um Platz eins in Gruppe A3. Die Premier-League-Tabelle bleibt in der Länderspielpause stehen: Arsenal 27, Brighton 22, Manchester City 21, Liverpool 18."
            ]
        },
        "it": {
            "title": "L'Arsenal ferma il Barcellona 1-1 al Camp Nou; Kane porta l'Inghilterra ai quarti 2-1",
            "subtitle": "Maanum e Graham Hansen si spartiscono l'UWCL mentre Kane, alla 126a presenza, prepara lo Spagna-Inghilterra di domenica a Madrid.",
            "excerpt": "Frida Maanum apre al 22', Caroline Graham Hansen pareggia al 59': 1-1. Inghilterra 2-1 Croazia, Italia 3-1 Francia, Spagna 2-0 Cechia.",
            "body": [
                "L'Arsenal Women lascia lo Spotify Camp Nou con un 1-1 giovedi 12 novembre e interrompe l'avvio perfetto del FC Barcelona Femeni in UWCL. Frida Maanum segna al 22' dopo una conclusione respinta di Caitlin Foord. Il Barcellona produce 24 tiri e quasi il 70% di possesso prima che Caroline Graham Hansen entri verso il centro e segni al 59'. Alessia Russo colpisce di testa a porta vuota fuori. L'Arsenal e quarto a 8 punti; il Barcellona ha 10, a pari con il Lione.",
                "La Nations League maschile chiude tre gare nella stessa sera. A Wembley Morgan Rogers segna al 24' e Harry Kane realizza un rigore al 64' nella sua 126a presenza record dopo il pari di Petar Sucic (59'). L'Inghilterra e ai quarti con 12 punti. L'Italia rimonta e batte la Francia 3-1 a San Siro (Olise 10', Pio Esposito 26' e 75' rig., Frattesi 63'). La Spagna batte 2-0 la Cechia in inferiorita a Praga (Baena 39' rig., Pubill 90+6').",
                "Domenica 15 novembre la Spagna ospita l'Inghilterra al Metropolitano (19:45 GMT) per il primo posto del gruppo A3. La Premier resta ferma nella sosta: Arsenal 27, Brighton 22, Manchester City 21, Liverpool 18."
            ]
        },
        "pl": {
            "title": "Arsenal trzyma Barcelone 1:1 na Camp Nou; Kane wpuszcza Anglie do cwiercfinalu 2:1",
            "subtitle": "Maanum i Graham Hansen dziela punkty UWCL, a Kane przy 126. wystepie ustawia niedzielny hit Hiszpania-Anglia w Madrycie.",
            "excerpt": "Frida Maanum otwiera w 22., Caroline Graham Hansen wyrównuje w 59.: 1:1. Anglia 2:1 Chorwacja, Wlochy 3:1 Francja, Hiszpania 2:0 Czechy.",
            "body": [
                "Arsenal Women wychodzi ze Spotify Camp Nou z remisem 1:1 w czwartek 12 listopada i przerywa idealny start FC Barcelona Femeni w UWCL. Frida Maanum strzela w 22. minucie po interwencji na Caitlin Foord. Barcelona oddaje 24 strzaly i ma blisko 70 procent posiadania, zanim Caroline Graham Hansen wchodzi do srodka i trafia w 59. Alessia Russo glowkuje obok pustej bramki. Arsenal jest czwarty z 8 punktami; Barcelona ma 10, tyle co Lyon.",
                "Liga Narodow mezczyzn zamyka trzy mecze tej samej nocy. Na Wembley Morgan Rogers trafia w 24., a Harry Kane wykorzystuje karnego w 64. przy rekordowym 126. wystepie po golu Petara Sucicia (59.). Anglia jest w cwiercfinale z 12 punktami. Wlochy odrabiaja i wygrywaja 3:1 z Francja na San Siro (Olise 10., Pio Esposito 26. i 75. karny, Frattesi 63.). Hiszpania bije 10-osobowe Czechy 2:0 w Pradze (Baena 39. karny, Pubill 90+6).",
                "W niedziele 15 listopada Hiszpania podejmie Anglie na Metropolitano (19:45 GMT) o pierwsze miejsce w grupie A3. Tabela Premier League stoi w trakcie przerwy: Arsenal 27, Brighton 22, Manchester City 21, Liverpool 18."
            ]
        },
        "zh": {
            "title": "阿森纳女足诺坎普1-1逼平巴萨；凯恩点球助英格兰2-1晋级",
            "subtitle": "马努姆与格拉汉姆-汉森分享女足欧冠积分，凯恩第126场国家队出场为周日马德里西班牙-英格兰埋下伏笔。",
            "excerpt": "马努姆第22分钟破门，格拉汉姆-汉森第59分钟扳平：1-1。英格兰2-1克罗地亚，意大利3-1法国，西班牙2-0捷克。",
            "body": [
                "阿森纳女足于11月12日周四在诺坎普1-1战平巴萨女足，终结对手女足欧冠联赛阶段的全胜开局。弗丽达·马努姆在第22分钟抢先破门，此前福特的射门被挡。巴萨打出24次射门、近70%控球，格拉汉姆-汉森第59分钟内切破门。鲁索头球空门偏出。阿森纳积8分排第四；巴萨10分与里昂并列。",
                "同晚男足欧国联收官三场。温布利：罗杰斯第24分钟破门，凯恩在第126场国家队出场第64分钟罚入点球，苏契奇第59分钟曾扳平。英格兰积12分晋级八强。意大利在圣西罗3-1逆转法国（奥利斯10，皮奥·埃斯波西托26与75点球，弗拉泰西63）。西班牙在布拉格2-0击败十人捷克（巴埃纳39点球，普比尔90+6）。",
                "11月15日周日，西班牙将在大都会球场（19:45 GMT）主场迎战英格兰，争夺A3组头名。英超国际比赛日期间积分不变：阿森纳27、布莱顿22、曼城21、利物浦18。"
            ]
        },
        "ja": {
            "title": "アーセナルがカンプ・ノウでバルセロナと1-1；ケインのPKでイングランドが2-1勝ち抜け",
            "subtitle": "マーヌムとグラハム・ハンセンがUWCLの勝ち点を分け合い、126キャップ目のケインが日曜マドリードのスペイン対イングランドをセット。",
            "excerpt": "マーヌムが22分に先制、グラハム・ハンセンが59分に同点：1-1。イングランド2-1クロアチア、イタリア3-1フランス、スペイン2-0チェコ。",
            "body": [
                "アーセナル女子は11月12日木曜、スポティファイ・カンプ・ノウで1-1とし、バルセロナ女子のUWCL完全スタートを止めた。フリダ・マーヌムが22分、フォードのシュートが阻まれた後に先制。バルセロナは24本のシュートと約70%のボール支配を記録し、キャロライン・グラハム・ハンセンが59分にカットインから決めた。ルッソは無人のゴールへヘディングを外した。アーセナルは8ポイントで4位、バルセロナはリヨンと並ぶ10ポイント。",
                "男子ネーションズリーグも同夜に3試合が決着。ウェンブリーではロジャースが24分に得点し、ハリー・ケインが記録づくめの126キャップ目、64分のPKを決めた。スチッチが59分に同点としていた。イングランドは12ポイントで準々決勝進出。イタリアはサンシーロでフランスに3-1逆転勝ち（オリス10分、ピオ・エスポジト26分と75分PK、フラッテージ63分）。スペインはプラハで10人のチェコに2-0（バエナ39分PK、プビル90+6）。",
                "11月15日日曜、スペインはメトロポリターノ（19:45 GMT）でイングランドを迎え、グループA3首位を争う。プレミアは代表ウィークで変動なし：アーセナル27、ブライトン22、マンチェスター・シティ21、リバプール18。"
            ]
        },
        "ko": {
            "title": "아스널, 캄프 누에서 바르셀로나와 1-1; 케인의 PK로 잉글랜드 2-1 8강행",
            "subtitle": "마누움과 그레이엄 한센이 UWCL 승점을 나누고, 126번째 캡의 케인이 일요일 마드리드 스페인-잉글랜드를 예고합니다.",
            "excerpt": "마누움 22분 선제, 그레이엄 한센 59분 동점: 1-1. 잉글랜드 2-1 크로아티아, 이탈리아 3-1 프랑스, 스페인 2-0 체코.",
            "body": [
                "아스널 위민이 11월 12일 목요일 스포티파이 캄프 누에서 1-1을 기록하며 FC 바르셀로나 페메니의 UWCL 완전 출발을 끊었습니다. 프리다 마누움이 22분 포드 슈팅이 막힌 뒤 선제골을 넣었습니다. 바르셀로나는 24개의 슈팅과 약 70% 점유율을 가져갔고 캐롤라인 그레이엄 한센이 59분 컷인 뒤 동점골을 넣었습니다. 알레시아 루소는 빈 골대를 향한 헤더를 빗나갔습니다. 아스널은 승점 8로 4위, 바르셀로나는 리옹과 함께 10점입니다.",
                "남자 네이션스리그도 같은 밤 세 경기가 종료됐습니다. 웸블리에서 모건 로저스가 24분 득점하고 해리 케인이 기록적인 126번째 출전 64분 PK를 넣었으며 페타르 수치치가 59분 동점골을 넣었습니다. 잉글랜드는 승점 12로 8강입니다. 이탈리아는 산시로에서 프랑스를 3-1로 뒤집었습니다(올리세 10, 피오 에스포시토 26·75 PK, 프라테시 63). 스페인은 프라하에서 10명 체코를 2-0으로 이겼습니다(바에나 39 PK, 푸빌 90+6).",
                "11월 15일 일요일 스페인이 메트로폴리타노(19:45 GMT)에서 잉글랜드를 맞아 A3조 1위를 가립니다. 프리미어리그는 국가대표 휴식기 동안 변동 없습니다: 아스널 27, 브라이턴 22, 맨시티 21, 리버풀 18."
            ]
        },
        "ar": {
            "title": "أرسنال يتعادل 1-1 مع برشلونة في كامب نو؛ كين يقود إنجلترا إلى ربع النهائي 2-1",
            "subtitle": "مانوم وغراهام هانسن يقتسمان نقطة دوري السيدات بينما يجهز كين في ظهوره 126 لمواجهة إسبانيا وإنجلترا الأحد في مدريد.",
            "excerpt": "فريدا مانوم تتقدم في الدقيقة 22 وتعادل كارولين غراهام هانسن في 59: 1-1. إنجلترا 2-1 كرواتيا، إيطاليا 3-1 فرنسا، إسبانيا 2-0 التشيك.",
            "body": [
                "غادر أرسنال للسيدات ملعب سبوتيفاي كامب نو بتعادل 1-1 يوم الخميس 12 نوفمبر منهيا البداية المثالية لبرشلونة للسيدات في دوري الأبطال. سجلت فريدا مانوم في الدقيقة 22 بعد صد تسديدة كايتلين فورد. أطلق برشلونة 24 تسديدة وسيطر بنحو 70% قبل أن تدخل كارولين غراهام هانسن إلى العمق وتسجل في 59. أبعدت أليسيا روسو رأسية من أمام المرمى الخالي. أرسنال رابع بـ8 نقاط؛ برشلونة لديه 10 متعادلا مع ليون.",
                "دوري الأمم للرجال أغلق ثلاث مباريات في الليلة ذاتها. في ويمبلي سجل مورغان روجرز في 24 وحول هاري كين ركلة جزاء في 64 في ظهوره القياسي 126 بعد تعادل بيتار سوتشيتش (59). إنجلترا في ربع النهائي بـ12 نقطة. إيطاليا عاد من الخلف وفاز 3-1 على فرنسا في سان سيرو (أوليز 10، بيو إسبوزيتو 26 و75 جزاء، فراتيسي 63). إسبانيا فازت 2-0 على التشيك بعشرة لاعبين في براغ (باينا 39 جزاء، بوبل 90+6).",
                "الأحد 15 نوفمبر تستضيف إسبانيا إنجلترا في المتروبوليتانو (19:45 GMT) على صدارة المجموعة A3. جدول البريميرليغ مجمد في التوقف الدولي: أرسنال 27، برايتون 22، مانشستر سيتي 21، ليفربول 18."
            ]
        }
    },
    "nfl-week10-tnf-commanders-24-21-giants-diggs-2026": {
        "fr": {
            "title": "TNF : Diggs inscrit un TD de 32 yards a 0:57 et les Commanders battent les Giants 24-21",
            "subtitle": "Jayden Daniels lance trois touchdowns, Rasul Douglas scelle le succes d'une interception, et samedi il n'y a pas de match NFL avant le coup d'envoi de Munich dimanche.",
            "excerpt": "Commanders 24, Giants 21 au MetLife. Daniels 23 sur 33, 249 yards, 3 TD. Skattebo deux TD au sol. Washington 3-5-1, New York 5-3-1. Suivant : Patriots vs Lions a Munich, 9h30 ET dimanche.",
            "body": [
                "Jayden Daniels trouve Stefon Diggs pour un touchdown de 32 yards a 57 secondes de la fin et les Washington Commanders battent les New York Giants 24-21 jeudi soir au MetLife Stadium (80 450 spectateurs). Daniels termine a 23 sur 33 pour 249 yards et trois TD apres ses deux premieres interceptions de la saison sur des drives consecutifs au quatrieme quart. Rasul Douglas intercepte ensuite une longue balle de J.J. McCarthy destinee a Malik Nabers.",
                "Cam Skattebo marque deux fois au sol (1 yard, 13 yards) et McCarthy trouve Isaiah Likely pour un TD de 66 yards qui porte le score a 21-17 a 8:13 de la fin. McCarthy termine a 23 sur 36 pour 293 yards. Likely capte neuf passes pour 127 yards. Washington est 3-5-1 ; les Giants sont 5-3-1.",
                "Samedi 14 novembre, il n'y a pas de match NFL. La semaine 10 continue dimanche a Munich : New England Patriots (5-4) contre Detroit Lions (6-2) a 9h30 ET sur FOX, puis 12 matchs domestiques. Le lundi soir, Chargers chez Ravens a 20h15 ET. Les scores de dimanche ne sont pas publies."
            ]
        },
        "es": {
            "title": "TNF: Diggs anota de 32 yardas a falta de 0:57 y Commanders vencen 24-21 a Giants",
            "subtitle": "Jayden Daniels lanza tres touchdowns, Rasul Douglas cierra con una intercepcion y el sabado no hay NFL antes del saque de Munich el domingo.",
            "excerpt": "Commanders 24, Giants 21 en MetLife. Daniels 23 de 33, 249 yardas, 3 TD. Skattebo dos TD de carrera. Washington 3-5-1, New York 5-3-1. Siguiente: Patriots vs Lions en Munich, 9:30 ET domingo.",
            "body": [
                "Jayden Daniels encuentra a Stefon Diggs para un touchdown de 32 yardas a 57 segundos del final y los Washington Commanders vencen a los New York Giants 24-21 el jueves noche en MetLife Stadium (80.450). Daniels cierra 23 de 33 para 249 yardas y tres TD despues de sus dos primeras intercepciones de la temporada en drives consecutivos del ultimo cuarto. Rasul Douglas intercepta luego un envio profundo de J.J. McCarthy para Malik Nabers.",
                "Cam Skattebo anota dos veces por tierra (1 yarda, 13 yardas) y McCarthy conecta con Isaiah Likely para un TD de 66 yardas que pone el 21-17 a falta de 8:13. McCarthy va 23 de 36 para 293 yardas. Likely atrapa nueve pases para 127. Washington esta 3-5-1; los Giants, 5-3-1.",
                "El sabado 14 de noviembre no hay partido de NFL. La Semana 10 sigue el domingo en Munich: New England Patriots (5-4) vs Detroit Lions (6-2) a las 9:30 ET en FOX, mas 12 partidos domésticos. El lunes, Chargers en Ravens a las 20:15 ET. No se publican marcadores del domingo."
            ]
        },
        "de": {
            "title": "TNF: Diggs trifft aus 32 Yards bei 0:57, Commanders schlagen Giants 24:21",
            "subtitle": "Jayden Daniels wirft drei Touchdowns, Rasul Douglas macht mit einer Interception den Deckel drauf, und samstags gibt es kein NFL-Spiel vor dem Muenchen-Kickoff am Sonntag.",
            "excerpt": "Commanders 24, Giants 21 im MetLife. Daniels 23 von 33, 249 Yards, 3 TD. Skattebo zwei Lauf-TDs. Washington 3-5-1, New York 5-3-1. Naechstes: Patriots vs. Lions in Muenchen, 9:30 ET Sonntag.",
            "body": [
                "Jayden Daniels findet Stefon Diggs zum 32-Yards-Touchdown 57 Sekunden vor Schluss, und die Washington Commanders schlagen die New York Giants 24:21 am Donnerstagabend im MetLife Stadium (80.450). Daniels kommt auf 23 von 33 fuer 249 Yards und drei TDs, nachdem er seine ersten beiden Interceptions der Saison in aufeinanderfolgenden Drives im letzten Viertel geworfen hatte. Rasul Douglas faengt anschliessend einen tiefen Ball von J.J. McCarthy auf Malik Nabers.",
                "Cam Skattebo trifft zweimal zu Lauf (1 Yard, 13 Yards), McCarthy findet Isaiah Likely zum 66-Yards-TD zum 21:17 bei 8:13 Restzeit. McCarthy steht bei 23 von 36 fuer 293 Yards. Likely faengt neun Baelle fuer 127. Washington ist 3-5-1, die Giants 5-3-1.",
                "Samstag, 14. November, steht kein NFL-Spiel an. Woche 10 geht sonntags in Muenchen weiter: New England Patriots (5-4) gegen Detroit Lions (6-2) um 9:30 ET auf FOX, danach 12 Heimspiele in den USA. Montag: Chargers bei Ravens, 20:15 ET. Sonntagsergebnisse werden nicht veroeffentlicht."
            ]
        },
        "it": {
            "title": "TNF: Diggs segna da 32 yard a 0:57 e i Commanders battono i Giants 24-21",
            "subtitle": "Jayden Daniels lancia tre touchdown, Rasul Douglas chiude con un intercetto e sabato non c'e NFL prima del calcio d'inizio di Monaco di domenica.",
            "excerpt": "Commanders 24, Giants 21 al MetLife. Daniels 23 su 33, 249 yard, 3 TD. Skattebo due TD su corsa. Washington 3-5-1, New York 5-3-1. Prossimo: Patriots vs Lions a Monaco, 9:30 ET domenica.",
            "body": [
                "Jayden Daniels trova Stefon Diggs per un touchdown da 32 yard a 57 secondi dalla fine e i Washington Commanders battono i New York Giants 24-21 giovedi sera al MetLife Stadium (80.450). Daniels chiude 23 su 33 per 249 yard e tre TD dopo i primi due intercetti della stagione in drive consecutivi nel quarto periodo. Rasul Douglas intercetta poi un lancio profondo di J.J. McCarthy per Malik Nabers.",
                "Cam Skattebo segna due volte su corsa (1 yard, 13 yard) e McCarthy trova Isaiah Likely per un TD da 66 yard che porta il punteggio sul 21-17 a 8:13 dalla fine. McCarthy va 23 su 36 per 293 yard. Likely afferra nove passaggi per 127. Washington e 3-5-1; i Giants 5-3-1.",
                "Sabato 14 novembre non c'e gara NFL. La Week 10 continua domenica a Monaco: New England Patriots (5-4) contro Detroit Lions (6-2) alle 9:30 ET su FOX, poi 12 gare interne. Lunedì: Chargers dai Ravens alle 20:15 ET. I punteggi di domenica non sono pubblicati."
            ]
        },
        "pl": {
            "title": "TNF: Diggs z 32 jardow przy 0:57, Commanders wygrywaja z Giants 24:21",
            "subtitle": "Jayden Daniels rzuca trzy przylozenia, Rasul Douglas zamyka mecz przechwytem, a w sobote nie ma NFL przed niedzielnym startem w Monachium.",
            "excerpt": "Commanders 24, Giants 21 na MetLife. Daniels 23 z 33, 249 jardow, 3 TD. Skattebo dwa TD z biegu. Washington 3-5-1, New York 5-3-1. Nastepnie: Patriots vs Lions w Monachium, 9:30 ET w niedziele.",
            "body": [
                "Jayden Daniels znajduje Stefona Diggsa przy przylozeniu z 32 jardow 57 sekund przed koncem i Washington Commanders pokonuja New York Giants 24:21 w czwartek na MetLife Stadium (80 450). Daniels konczy 23 z 33 na 249 jardow i trzy TD po pierwszych dwoch przechwyconych podaniach sezonu w kolejnych drive'ach czwartej kwarty. Rasul Douglas przechwytuje nastepnie dalekie podanie J.J. McCarthy'ego do Malika Nabersa.",
                "Cam Skattebo zdobywa dwa przylozenia z biegu (1 jard, 13 jardow), a McCarthy trafia do Isaiaha Likely'ego przy TD z 66 jardow na 21:17 przy 8:13 do konca. McCarthy ma 23 z 36 na 293 jardy. Likely lapie dziewiec podań na 127. Washington jest 3-5-1, Giants 5-3-1.",
                "W sobote 14 listopada nie ma meczu NFL. 10. tydzien trwa w niedziele w Monachium: New England Patriots (5-4) kontra Detroit Lions (6-2) o 9:30 ET na FOX, potem 12 meczow krajowych. Poniedzialek: Chargers u Ravens o 20:15 ET. Wyniki niedzieli nie sa publikowane."
            ]
        },
        "zh": {
            "title": "TNF：迪格斯剩余0:57时32码达阵，指挥官24-21击败巨人",
            "subtitle": "丹尼尔斯传出三次达阵，道格拉斯抄截锁定胜局，周六无NFL，周日慕尼黑揭幕战尚未开球。",
            "excerpt": "指挥官24，巨人21。丹尼尔斯23/33、249码、3达阵。斯卡特博两次跑达阵。华盛顿3-5-1，纽约5-3-1。下一场：慕尼黑爱国者对雄狮，周日美东9:30。",
            "body": [
                "杰登·丹尼尔斯在剩余57秒找到斯特冯·迪格斯完成32码达阵，华盛顿指挥官周四夜在大都会球场（80450人）24-21击败纽约巨人。丹尼尔斯23/33、249码、3次达阵，此前他在第四节连续两次被抄截，为本赛季首次。随后拉苏尔·道格拉斯抄截了麦卡锡给纳伯斯的深传。",
                "卡姆·斯卡特博两次跑达阵（1码、13码），麦卡锡找到艾赛亚·莱克利完成66码达阵，8:13时将比分改写为21-17。麦卡锡23/36、293码。莱克利9次接球127码。华盛顿3-5-1，巨人5-3-1。",
                "11月14日周六无NFL比赛。第10周周日在慕尼黑继续：新英格兰爱国者（5-4）对底特律雄狮（6-2），美东9:30 FOX转播，随后还有12场国内赛。周一晚闪电客战乌鸦，美东8:15。周日比分不予发布。"
            ]
        },
        "ja": {
            "title": "TNF：残り0:57でディッグスが32ヤードTD、コマンダースがジャイアンツに24-21",
            "subtitle": "ジェイデン・ダニエルズが3TD、ラスール・ダグラスがINTで締め、土曜はNFLなし。日曜ミュンヘンのキックオフは未開催。",
            "excerpt": "コマンダース24、ジャイアンツ21。ダニエルズ23/33、249yds、3TD。スカテボがランTD2本。ワシントン3-5-1、NY 5-3-1。次戦：ミュンヘンでペイトリオッツ対ライオンズ、日曜ET 9:30。",
            "body": [
                "ジェイデン・ダニエルズが残り57秒でステフォン・ディッグスへ32ヤードTDを通し、ワシントン・コマンダースが木曜夜メットライフ・スタジアム（8万450人）でニューヨーク・ジャイアンツを24-21で破った。ダニエルズは23/33、249ヤード、3TD。第4Q連続ドライブで今季初の2INTを喫した直後だった。ラスール・ダグラスが続くマクカーシーのネイバーズ宛てディープボールをINTした。",
                "キャム・スカテボがランで2TD（1ヤード、13ヤード）。マクカーシーはアイザイア・ライクリーへ66ヤードTDを通し、残り8:13で21-17。マクカーシーは23/36、293ヤード。ライクリーは9キャッチ127ヤード。ワシントンは3-5-1、ジャイアンツは5-3-1。",
                "11月14日土曜にNFLの試合はない。第10週は日曜ミュンヘンで継続：ニューイングランド・ペイトリオッツ（5-4）対デトロイト・ライオンズ（6-2）、ET 9:30 FOX、その後国内12試合。月曜はチャージャーズ対レイブンズ、ET 20:15。日曜のスコアは掲載しない。"
            ]
        },
        "ko": {
            "title": "TNF: 디그스가 0:57에 32야드 TD, 커맨더스가 자이언츠를 24-21로 제압",
            "subtitle": "제이든 대니얼스가 3TD, 라술 더글러스가 인터셉트로 승리를 잠그고 토요일 NFL은 없습니다. 일요일 뮌헨 킥오프는 미개최입니다.",
            "excerpt": "커맨더스 24, 자이언츠 21. 대니얼스 23/33, 249야드, 3TD. 스카테보 런 TD 2개. 워싱턴 3-5-1, 뉴욕 5-3-1. 다음: 뮌헨 패트리어츠 vs 라이온스, 일요일 ET 9:30.",
            "body": [
                "제이든 대니얼스가 57초를 남기고 스테폰 디그스에게 32야드 TD를 연결해 워싱턴 커맨더스가 목요일 밤 메트라이프 스타디움(80,450명)에서 뉴욕 자이언츠를 24-21로 꺾었습니다. 대니얼스는 23/33, 249야드, 3TD. 4쿼터 연속 드라이브에서 시즌 첫 인터셉트 2개를 허용한 직후였습니다. 라술 더글러스가 이어진 J.J. 매카시의 말릭 네이버스 향 깊은 패스를 가로챘습니다.",
                "캠 스카테보가 러닝으로 두 번 득점(1야드, 13야드)했고 매카시는 아이제이아 라이클리에게 66야드 TD를 던져 8:13에 21-17로 앞섰습니다. 매카시는 23/36, 293야드. 라이클리는 9캐치 127야드. 워싱턴은 3-5-1, 자이언츠는 5-3-1입니다.",
                "11월 14일 토요일에는 NFL 경기가 없습니다. 10주차는 일요일 뮌헨에서 이어집니다: 뉴잉글랜드 패트리어츠(5-4) vs 디트로이트 라이온스(6-2), ET 9:30 FOX, 이후 국내 12경기. 월요일은 차저스 @ 레이븐스, ET 8:15. 일요일 스코어는 게시하지 않습니다."
            ]
        },
        "ar": {
            "title": "TNF: ديغز يسجل من 32 ياردة عند 0:57 وكوماندرز يغلبون جاينتس 24-21",
            "subtitle": "جايادن دانيالز يرمي ثلاثة تاتشداون ورسول دوغلاس يغلق المباراة باعتراض، ولا توجد مباراة NFL يوم السبت قبل انطلاقة ميونخ الأحد.",
            "excerpt": "كوماندرز 24، جاينتس 21 في ميتلايف. دانيالز 23 من 33، 249 ياردة، 3 TD. سكاتيبو تاتشداونان بالركض. واشنطن 3-5-1، نيويورك 5-3-1. التالي: باتريوتس ضد ليونز في ميونخ، 9:30 ET الأحد.",
            "body": [
                "وجد جايادن دانيالز ستيفون ديغز لتاتشداون من 32 ياردة قبل 57 ثانية من النهاية وفاز واشنطن كوماندرز على نيويورك جاينتس 24-21 مساء الخميس في ملعب ميتلايف (80,450). أنهى دانيالز 23 من 33 لـ249 ياردة وثلاثة تاتشداون بعد أول اعتراضين له هذا الموسم في هجمتين متتاليتين في الربع الرابع. ثم اعترض رسول دوغلاس كرة عميقة من جي. جي. مكارثي إلى مالك نابر.",
                "سجل كام سكاتيبو مرتين بالركض (ياردة واحدة و13 ياردة) ووصل مكارثي إلى إيزايا لايكلي بتاتشداون من 66 ياردة ليصبح 21-17 عند 8:13. أنهى مكارثي 23 من 36 لـ293 ياردة. لايكلي التقط تسعا لـ127. واشنطن 3-5-1 والجاينتس 5-3-1.",
                "السبت 14 نوفمبر بلا مباراة NFL. الأسبوع 10 يتواصل الأحد في ميونخ: نيو إنغلاند باتريوتس (5-4) ضد ديترويت ليونز (6-2) الساعة 9:30 ET على FOX ثم 12 مباراة محلية. الاثنين تشارجرز عند رافينز الساعة 20:15 ET. لا تُنشر نتائج الأحد."
            ]
        }
    },
    "nba-spurs-11th-straight-castle-32-warriors-2026": {
        "fr": {
            "title": "Castle marque 32 points, les Spurs ecrasent les Warriors 123-85 pour une 11e victoire d'affilee",
            "subtitle": "San Antonio est 11-2 sans laisser Golden State s'installer, une nuit apres les 52 points de Cade Cunningham en double prolongation a Washington.",
            "excerpt": "Spurs 123, Warriors 85. Castle 32, Wembanyama 12/12/6. Curry absent au moins deux semaines (oblique). Jeudi : Cunningham 52, Pistons 144-140 2OT. Samedi : cinq matchs NBA a venir.",
            "body": [
                "Stephon Castle inscrit un record de saison de 32 points (12 sur 18, cinq triples) et les San Antonio Spurs ecrasent les Golden State Warriors 123-85 vendredi soir au Frost Bank Center, 11e succes d'affilee et bilan 11-2. Victor Wembanyama ajoute 12 points, 12 rebonds et six passes. Les Spurs menent 38-14 apres un quart-temps. Stephen Curry est absent au moins deux semaines pour une dechirure de l'oblique droit contractee mercredi a Houston. L.J. Cryer mene Golden State avec 20 points.",
                "Autre tableau jeudi : Cade Cunningham marque 52 points, 11 passes et zero perte de balle, Detroit battant Washington 144-140 en double prolongation. Vendredi aussi : Miami 133-121 Cleveland (Giannis 37), Indiana 106-104 New York (Brunson 33), Orlando 107-99 Milwaukee, Chicago 125-117 OT Atlanta, Memphis 142-111 La Nouvelle-Orleans, Houston 125-118 Utah (Sengun 43), Portland 120-107 Sacramento et les Clippers 113-112 sur Oklahoma City.",
                "Samedi 14 novembre, cinq matchs sont a venir (Nuggets a Pelicans 19h00 ET, Mavericks a Cavaliers 19h30, puis Pistons a Heat, Nets a Grizzlies, Bulls a Timberwolves). Aucun n'est publie comme final."
            ]
        },
        "es": {
            "title": "Castle anota 32 y los Spurs golean 123-85 a Warriors para su 11a seguida",
            "subtitle": "San Antonio esta 11-2 sin dar respiro a Golden State, una noche despues de los 52 puntos de Cade Cunningham en doble prorroga en Washington.",
            "excerpt": "Spurs 123, Warriors 85. Castle 32, Wembanyama 12/12/6. Curry fuera al menos dos semanas (oblicuo). Jueves: Cunningham 52, Pistons 144-140 2OT. Sabado: cinco partidos NBA pendientes.",
            "body": [
                "Stephon Castle anota un maximo de temporada de 32 puntos (12 de 18, cinco triples) y los San Antonio Spurs golean a Golden State Warriors 123-85 el viernes en Frost Bank Center, su 11a seguida y un 11-2. Victor Wembanyama suma 12 puntos, 12 rebotes y seis asistencias. Los Spurs ganan 38-14 el primer cuarto. Stephen Curry esta fuera al menos dos semanas por un desgarro del oblicuo derecho sufrido el miercoles en Houston. L.J. Cryer lidera a Golden State con 20.",
                "El otro titular del jueves: Cade Cunningham anota 52 puntos, 11 asistencias y cero perdidas, Detroit gana 144-140 en doble prorroga a Washington. El viernes tambien: Miami 133-121 Cleveland (Giannis 37), Indiana 106-104 New York (Brunson 33), Orlando 107-99 Milwaukee, Chicago 125-117 OT Atlanta, Memphis 142-111 New Orleans, Houston 125-118 Utah (Sengun 43), Portland 120-107 Sacramento y Clippers 113-112 sobre Oklahoma City.",
                "El sabado 14 de noviembre hay cinco partidos pendientes (Nuggets en Pelicans 19:00 ET, Mavericks en Cavaliers 19:30, luego Pistons en Heat, Nets en Grizzlies, Bulls en Timberwolves). Ninguno se publica como final."
            ]
        },
        "de": {
            "title": "Castle erzielt 32 Punkte, Spurs deklassieren Warriors 123:85 zum 11. Sieg in Serie",
            "subtitle": "San Antonio steht 11-2 und laesst Golden State nicht ins Spiel kommen, eine Nacht nach Cade Cunninghams 52 Punkten in der Doppel-Verlaengerung in Washington.",
            "excerpt": "Spurs 123, Warriors 85. Castle 32, Wembanyama 12/12/6. Curry mindestens zwei Wochen out (Schrägmuskel). Donnerstag: Cunningham 52, Pistons 144:140 2OT. Samstag: fünf NBA-Spiele ausstehend.",
            "body": [
                "Stephon Castle erzielt ein Saisonhoch von 32 Punkten (12 von 18, fünf Dreier), und die San Antonio Spurs deklassieren die Golden State Warriors 123:85 am Freitagabend im Frost Bank Center, der 11. Sieg in Serie und 11-2. Victor Wembanyama steuert 12 Punkte, 12 Rebounds und sechs Assists bei. Die Spurs führen 38:14 nach einem Viertel. Stephen Curry fehlt mindestens zwei Wochen wegen eines Risses am rechten schrägen Bauchmuskel, den er mittwochs in Houston erlitt. L.J. Cryer führt Golden State mit 20 an.",
                "Donnerstags anderer Aufmacher: Cade Cunningham erzielt 52 Punkte, 11 Assists und null Turnover, Detroit schlägt Washington 144:140 in der Doppel-OT. Freitag auch: Miami 133:121 Cleveland (Giannis 37), Indiana 106:104 New York (Brunson 33), Orlando 107:99 Milwaukee, Chicago 125:117 OT Atlanta, Memphis 142:111 New Orleans, Houston 125:118 Utah (Sengun 43), Portland 120:107 Sacramento und Clippers 113:112 gegen Oklahoma City.",
                "Samstag, 14. November, stehen fünf Spiele an (Nuggets bei Pelicans 19:00 ET, Mavericks bei Cavaliers 19:30, dann Pistons bei Heat, Nets bei Grizzlies, Bulls bei Timberwolves). Keines wird als Finale veröffentlicht."
            ]
        },
        "it": {
            "title": "Castle mette 32 punti, gli Spurs travolgono i Warriors 123-85 per l'11a di fila",
            "subtitle": "San Antonio e 11-2 e non lascia spazio a Golden State, una notte dopo i 52 punti di Cade Cunningham nel doppio overtime a Washington.",
            "excerpt": "Spurs 123, Warriors 85. Castle 32, Wembanyama 12/12/6. Curry out almeno due settimane (obliquo). Giovedi: Cunningham 52, Pistons 144-140 2OT. Sabato: cinque gare NBA in programma.",
            "body": [
                "Stephon Castle realizza un massimo stagionale di 32 punti (12 su 18, cinque triple) e i San Antonio Spurs travolgono i Golden State Warriors 123-85 venerdi sera al Frost Bank Center, 11a vittoria di fila e 11-2. Victor Wembanyama aggiunge 12 punti, 12 rimbalzi e sei assist. Gli Spurs chiudono il primo quarto 38-14. Stephen Curry e assente almeno due settimane per uno strappo all'obliquo destro accusato mercoledi a Houston. L.J. Cryer guida Golden State con 20.",
                "Altro titolo del giovedi: Cade Cunningham mette 52 punti, 11 assist e zero palle perse, Detroit batte Washington 144-140 nel doppio overtime. Venerdi anche: Miami 133-121 Cleveland (Giannis 37), Indiana 106-104 New York (Brunson 33), Orlando 107-99 Milwaukee, Chicago 125-117 OT Atlanta, Memphis 142-111 New Orleans, Houston 125-118 Utah (Sengun 43), Portland 120-107 Sacramento e Clippers 113-112 su Oklahoma City.",
                "Sabato 14 novembre ci sono cinque gare in programma (Nuggets dai Pelicans 19:00 ET, Mavericks dai Cavaliers 19:30, poi Pistons dai Heat, Nets dai Grizzlies, Bulls dai Timberwolves). Nessuna e pubblicata come finale."
            ]
        },
        "pl": {
            "title": "Castle rzuca 32 punkty, Spurs rozbijaja Warriors 123:85 i wygrywaja 11. z rzedu",
            "subtitle": "San Antonio ma 11-2 i nie daje Golden State zadnego zaczepienia, noca po 52 punktach Cade'a Cunninghama w podwojnej dogrywce w Waszyngtonie.",
            "excerpt": "Spurs 123, Warriors 85. Castle 32, Wembanyama 12/12/6. Curry poza skladem co najmniej dwa tygodnie (skosny). Czwartek: Cunningham 52, Pistons 144:140 2OT. Sobota: piec meczow NBA przed nami.",
            "body": [
                "Stephon Castle notuje sezonowe maksimum 32 punktow (12 z 18, piec trojek), a San Antonio Spurs rozbijaja Golden State Warriors 123:85 w piatek w Frost Bank Center, 11. zwyciestwo z rzedu i bilans 11-2. Victor Wembanyama doklada 12 punktow, 12 zbiórek i szesc asyst. Spurs prowadza 38:14 po pierwszej kwarcie. Stephen Curry pauzuje co najmniej dwa tygodnie z powodu naderwania prawego miesnia skosnego z srody w Houston. L.J. Cryer prowadzi Warriors z 20 punktami.",
                "Inny hit czwartku: Cade Cunningham rzuca 52 punkty, 11 asyst i zero strat, Detroit wygrywa z Washington 144:140 w podwojnej dogrywce. W piatek takze: Miami 133:121 Cleveland (Giannis 37), Indiana 106:104 New York (Brunson 33), Orlando 107:99 Milwaukee, Chicago 125:117 OT Atlanta, Memphis 142:111 New Orleans, Houston 125:118 Utah (Sengun 43), Portland 120:107 Sacramento i Clippers 113:112 z Oklahoma City.",
                "W sobote 14 listopada czeka piec meczow (Nuggets u Pelicans 19:00 ET, Mavericks u Cavaliers 19:30, potem Pistons u Heat, Nets u Grizzlies, Bulls u Timberwolves). Zadnego nie publikujemy jako finalu."
            ]
        },
        "zh": {
            "title": "卡斯尔32分，马刺123-85横扫勇士拿下11连胜",
            "subtitle": "马刺战绩11-2未给勇士喘息，前一晚坎宁安在华盛顿两加时砍下52分。",
            "excerpt": "马刺123，勇士85。卡斯尔32分，文班12/12/6。库里斜肌伤至少缺阵两周。周四：坎宁安52分，活塞144-140两加时。周六五场NBA待赛。",
            "body": [
                "斯蒂芬·卡斯尔砍下赛季新高32分（12投18中、五记三分），圣安东尼奥马刺周五晚在霜冻银行中心123-85击败金州勇士，拿下11连胜、战绩11-2。维克托·文班亚马贡献12分12篮板6助攻。马刺首节38-14领先。斯蒂芬·库里因周三在休斯敦遭遇的右斜肌撕裂至少缺阵两周。L.J. 克莱尔以20分领军勇士。",
                "周四另一焦点：凯德·坎宁安52分11助攻零失误，底特律两加时144-140击败华盛顿。周五还有：迈阿密133-121克利夫兰（扬尼斯37分）、印第安纳106-104纽约（布伦森33分）、奥兰多107-99密尔沃基、芝加哥加时125-117亚特兰大、孟菲斯142-111新奥尔良、休斯敦125-118犹他（申京43分）、波特兰120-107萨克拉门托，快船113-112险胜俄克拉荷马城。",
                "11月14日周六有五场待赛（掘金客战鹈鹕美东7:00、独行侠客战骑士7:30，随后活塞客战热火、篮网客战灰熊、公牛客战森林狼）。均不作为完场发布。"
            ]
        },
        "ja": {
            "title": "キャッスルが32得点、スパーズがウォリアーズを123-85で下し11連勝",
            "subtitle": "サンアントニオは11勝2敗でゴールデンステートに隙を与えず。前夜はカニンガムがワシントンで2OT52得点。",
            "excerpt": "スパーズ123、ウォリアーズ85。キャッスル32、ウェンバンヤマ12/12/6。カリーは斜筋損傷で少なくとも2週間欠場。木曜：カニンガム52、ピストンズ144-140 2OT。土曜はNBA5試合が未開催。",
            "body": [
                "ステフォン・キャッスルが今季最多32得点（18本中12、スリー5本）を記録し、サンアントニオ・スパーズは金曜夜フロスト・バンク・センターでゴールデンステート・ウォリアーズを123-85で下し11連勝、11勝2敗とした。ビクター・ウェンバンヤマは12得点12リバウンド6アシスト。第1Qは38-14。ステフィン・カリーは水曜ヒューストンで負った右腹斜筋断裂で少なくとも2週間欠場。L.J.クライアーが20得点でウォリアーズを牽引。",
                "木曜のもう一つの見出し：ケイド・カニンガムが52得点11アシスト無ターンオーバー、デトロイトがワシントンに2OTで144-140。金曜は他にマイアミ133-121クリーブランド（ヤニス37）、インディアナ106-104ニューヨーク（ブランソン33）、オーランド107-99ミルウォーキー、シカゴOT125-117アトランタ、メンフィス142-111ニューオーリンズ、ヒューストン125-118ユタ（センギュン43）、ポートランド120-107サクラメント、クリッパーズ113-112オーバーオクラホマシティ。",
                "11月14日土曜は5試合が予定（ナゲッツ対ペリカンズ ET19:00、マーベリックス対キャブス19:30、その後ピストンズ対ヒート、ネッツ対グリズリーズ、ブルズ対ティンバーウルブズ）。いずれも最終として掲載しない。"
            ]
        },
        "ko": {
            "title": "캐슬 32점, 스퍼스가 워리어스를 123-85로 완파하며 11연승",
            "subtitle": "샌안토니오는 11승 2패로 골든스테이트에 틈을 주지 않았고, 전날 밤 워싱턴에서는 커닝햄이 더블OT 52점을 기록했습니다.",
            "excerpt": "스퍼스 123, 워리어스 85. 캐슬 32, 웸반야마 12/12/6. 커리는 복사근 부상으로 최소 2주 결장. 목요일: 커닝햄 52점, 피스톤스 144-140 2OT. 토요일 NBA 5경기 예정.",
            "body": [
                "스테폰 캐슬이 시즌 최다 32점(18중 12, 3점 5개)을 넣었고 샌안토니오 스퍼스가 금요일 밤 프로스트 뱅크 센터에서 골든스테이트 워리어스를 123-85로 꺾으며 11연승, 11승 2패를 달렸습니다. 빅터 웸반야마는 12점 12리바운드 6어시스트. 스퍼스는 1쿼터 38-14. 스테픈 커리는 수요일 휴스턴에서 당한 오른쪽 복사근 파열로 최소 2주 결장입니다. L.J. 크라이어가 20점으로 워리어스를 이끌었습니다.",
                "목요일 다른 헤드라인: 케이드 커닝햄이 52점 11어시스트 무실책, 디트로이트가 워싱턴을 더블OT 144-140으로 이겼습니다. 금요일에는 마이애미 133-121 클리블랜드(야니스 37), 인디애나 106-104 뉴욕(브런슨 33), 올랜도 107-99 밀워키, 시카고 OT 125-117 애틀랜타, 멤피스 142-111 뉴올리언스, 휴스턴 125-118 유타(센군 43), 포틀랜드 120-107 새크라멘토, 클리퍼스 113-112 오클라호마시티도 있었습니다.",
                "11월 14일 토요일에는 5경기가 남았습니다(너기츠 @ 펠리컨스 ET 7:00, 매버릭스 @ 캐벌리어스 7:30, 이후 피스톤스 @ 히트, 네츠 @ 그리즐리스, 불스 @ 팀버울브스). 어느 것도 최종으로 게시하지 않습니다."
            ]
        },
        "ar": {
            "title": "كاسل يسجل 32 نقطة وسبرز يسحقون ووريورز 123-85 للفوز الحادي عشر تواليا",
            "subtitle": "سان أنطونيو 11-2 دون أن يمنح غولدن ستيت موطئ قدم، بعد ليلة سجل فيها كيد كانينغهام 52 نقطة في وقتين إضافيين بواشنطن.",
            "excerpt": "سبرز 123، ووريورز 85. كاسل 32، ويمبانياما 12/12/6. كاري غائب أسبوعين على الأقل (عضلة مائلة). الخميس: كانينغهام 52، بيستونز 144-140 وقتان إضافيان. السبت: خمس مباريات NBA قادمة.",
            "body": [
                "سجل ستيفون كاسل أعلى موسمه بـ32 نقطة (12 من 18، خمس ثلاثيات) وسحق سان أنطونيو سبرز غولدن ستيت ووريورز 123-85 الجمعة مساء في فروست بانك سنتر، الفوز الحادي عشر تواليا و11-2. أضاف فيكتور ويمبانياما 12 نقطة و12 ارتدادا و6 تمريرات. تقدم سبرز 38-14 بعد ربع. ستيفن كاري غائب أسبوعين على الأقل بسبب تمزق في العضلة المائلة اليمنى أصيب به الأربعاء في هيوستن. قاد إل. جي. كراير غولدن ستيت بـ20 نقطة.",
                "عنوان الخميس الآخر: كيد كانينغهام سجل 52 نقطة و11 تمريرة وصفر فقدات، وديترويت فازت على واشنطن 144-140 في وقتين إضافيين. الجمعة أيضا: ميامي 133-121 كليفلاند (يانيس 37)، إنديانا 106-104 نيويورك (برونسون 33)، أورلاندو 107-99 ميلواكي، شيكاغو 125-117 وقت إضافي أتلانتا، ممفيس 142-111 نيو أورلينز، هيوستن 125-118 يوتا (سنغون 43)، بورتلاند 120-107 ساكرامنتو وكليبرز 113-112 على أوكلاهوما سيتي.",
                "السبت 14 نوفمبر خمس مباريات قادمة (ناغتس عند بيليكانز 19:00 ET، مافريكس عند كافالييرز 19:30، ثم بيستونز عند هيت، نتس عند غريزليز، بولز عند تمبروولفز). لا تُنشر أي منها كنهاية."
            ]
        }
    },
    "atp-stockholm-fritz-tirante-final-turin-sunday-2026": {
        "fr": {
            "title": "Fritz rejoint la finale de Stockholm apres Musetti ; Tirante joue aujourd'hui sa premiere finale ATP",
            "subtitle": "Un walkover de Rune et un 6-4, 6-2 en demie placent Taylor Fritz face a Thiago Agustin Tirante. Le round robin de Turin commence dimanche avec Zverev vs Jodar.",
            "excerpt": "Finale de Stockholm aujourd'hui : Fritz vs Tirante. Vendredi : Fritz bat Musetti 6-4, 6-2 ; Tirante bat Tabilo 7-5, 7-6 (1). Turin ouvre dimanche. Pas de score de finale ni de Turin.",
            "body": [
                "Taylor Fritz est en finale du Bybit Stockholm Open aujourd'hui, samedi 14 novembre, au Kungliga Tennishallen. La tete de serie numero 1 a avance quand Holger Rune s'est retire du quart de jeudi (walkover), puis a battu Lorenzo Musetti 6-4, 6-2 en 63 minutes vendredi. Thiago Agustin Tirante, 51e mondial, dispute la premiere finale ATP de sa carriere apres sa victoire 7-5, 7-6 (1) sur Alejandro Tabilo. Le match de championnat est a venir. Aucun score de finale n'est publie.",
                "Les Nitto ATP Finals de Turin ouvrent toujours dimanche 15 novembre a l'Inalpi Arena. Les groupes n'ont pas change depuis le tirage de jeudi : McEnroe (Zverev, Shelton, Fils, Jodar) et Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Simple dimanche : Zverev vs Jodar pas avant 14h00 CET, Shelton vs Fils pas avant 20h30. Lundi : Alcaraz vs Tiafoe, Medvedev vs Cobolli. Aucun simple de Turin n'a ete joue."
            ]
        },
        "es": {
            "title": "Fritz llega a la final de Estocolmo tras Musetti; Tirante debuta hoy en una final ATP",
            "subtitle": "El walkover de Rune y un 6-4, 6-2 en semifinales ponen a Taylor Fritz frente a Thiago Agustin Tirante. El round robin de Turin empieza el domingo con Zverev vs Jodar.",
            "excerpt": "Final de Estocolmo hoy: Fritz vs Tirante. Viernes: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). Turin abre el domingo. Sin marcador de final ni de Turin.",
            "body": [
                "Taylor Fritz esta en la final del Bybit Stockholm Open hoy, sabado 14 de noviembre, en Kungliga Tennishallen. El numero 1 del cuadro avanzo cuando Holger Rune se retiro del cuarto del jueves (walkover) y luego gano 6-4, 6-2 a Lorenzo Musetti en 63 minutos el viernes. Thiago Agustin Tirante, 51 del ranking, disputa la primera final ATP de su carrera tras vencer 7-5, 7-6 (1) a Alejandro Tabilo. El partido por el titulo esta pendiente. No se publica marcador de la final.",
                "Las Nitto ATP Finals de Turin siguen abriendo el domingo 15 de noviembre en Inalpi Arena. Los grupos no cambian desde el sorteo del jueves: McEnroe (Zverev, Shelton, Fils, Jodar) y Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Individuales domingo: Zverev vs Jodar no antes de las 14:00 CET, Shelton vs Fils no antes de las 20:30. Lunes: Alcaraz vs Tiafoe, Medvedev vs Cobolli. No se ha jugado ningun individual en Turin."
            ]
        },
        "de": {
            "title": "Fritz steht nach Musetti im Stockholm-Finale; Tirante gibt heute sein ATP-Finaldebüt",
            "subtitle": "Ein Walkover gegen Rune und 6:4, 6:2 im Halbfinale bringen Taylor Fritz gegen Thiago Agustin Tirante. Turin startet sonntags mit Zverev vs. Jodar.",
            "excerpt": "Stockholm-Finale heute: Fritz vs. Tirante. Freitag: Fritz d Musetti 6:4, 6:2; Tirante d Tabilo 7:5, 7:6 (1). Turin oeffnet sonntags. Kein Finalscore, kein Turin-Score.",
            "body": [
                "Taylor Fritz steht heute, Samstag 14. November, im Finale der Bybit Stockholm Open in der Kungliga Tennishallen. Der Topgesetzte kam weiter, als Holger Rune das Viertelfinale am Donnerstag kampflos abgab, und schlug Lorenzo Musetti am Freitag in 63 Minuten 6:4, 6:2. Thiago Agustin Tirante (ATP 51) erreicht das erste ATP-Finale seiner Karriere nach 7:5, 7:6 (1) gegen Alejandro Tabilo. Das Meisterschaftsspiel steht aus. Es wird kein Finalergebnis veroeffentlicht.",
                "Die Nitto ATP Finals in Turin beginnen weiterhin sonntags, 15. November, in der Inalpi Arena. Die Gruppen sind seit der Auslosung am Donnerstag unveraendert: McEnroe (Zverev, Shelton, Fils, Jodar) und Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Einzel sonntags: Zverev vs. Jodar nicht vor 14:00 MEZ, Shelton vs. Fils nicht vor 20:30. Montag: Alcaraz vs. Tiafoe, Medvedev vs. Cobolli. In Turin ist noch kein Einzel gespielt."
            ]
        },
        "it": {
            "title": "Fritz in finale a Stoccolma dopo Musetti; Tirante gioca oggi la prima finale ATP",
            "subtitle": "Il walkover su Rune e un 6-4, 6-2 in semifinale mettono Taylor Fritz di fronte a Thiago Agustin Tirante. Il round robin di Torino parte domenica con Zverev vs Jodar.",
            "excerpt": "Finale di Stoccolma oggi: Fritz vs Tirante. Venerdi: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). Torino apre domenica. Nessun punteggio di finale ne di Torino.",
            "body": [
                "Taylor Fritz e in finale al Bybit Stockholm Open oggi, sabato 14 novembre, al Kungliga Tennishallen. La testa di serie numero 1 e avanzata quando Holger Rune si e ritirato dal quarto di giovedi (walkover) e poi ha battuto Lorenzo Musetti 6-4, 6-2 in 63 minuti venerdi. Thiago Agustin Tirante, 51 ATP, disputa la prima finale ATP della carriera dopo il 7-5, 7-6 (1) su Alejandro Tabilo. La finale e in programma. Nessun punteggio e pubblicato.",
                "Le Nitto ATP Finals di Torino aprono ancora domenica 15 novembre all'Inalpi Arena. I gironi sono invariati dal sorteggio di giovedi: McEnroe (Zverev, Shelton, Fils, Jodar) e Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Singolare domenica: Zverev vs Jodar non prima delle 14:00 CET, Shelton vs Fils non prima delle 20:30. Lunedì: Alcaraz vs Tiafoe, Medvedev vs Cobolli. Nessun singolare di Torino e stato giocato."
            ]
        },
        "pl": {
            "title": "Fritz w finale Sztokholmu po Musettim; Tirante dzis debiutuje w finale ATP",
            "subtitle": "Walkower Rune'a i 6:4, 6:2 w polfinale stawiaja Taylora Fritza naprzeciw Thiago Agustina Tirante. Round robin w Turynie startuje w niedziele: Zverev vs Jodar.",
            "excerpt": "Final w Sztokholmie dzis: Fritz vs Tirante. Piatek: Fritz d Musetti 6:4, 6:2; Tirante d Tabilo 7:5, 7:6 (1). Turyn otwiera niedziela. Bez wyniku finalu i Turynu.",
            "body": [
                "Taylor Fritz jest w finale Bybit Stockholm Open dzis, w sobote 14 listopada, w Kungliga Tennishallen. Numer 1 turnieju awansowal, gdy Holger Rune wycofal sie z cwiercfinalu w czwartek (walkower), a potem w piatek pokonal Lorenzo Musettiego 6:4, 6:2 w 63 minuty. Thiago Agustin Tirante (ATP 51) gra pierwszy final ATP w karierze po 7:5, 7:6 (1) z Alejandro Tabilo. Mecz o tytul jest przed nami. Wyniku finalu nie publikujemy.",
                "Nitto ATP Finals w Turynie nadal otwieraja sie w niedziele 15 listopada na Inalpi Arena. Grupy bez zmian od czwartkowego losowania: McEnroe (Zverev, Shelton, Fils, Jodar) i Lendl (Alcaraz, Medvedev, Cobolli, Tiafoe). Single w niedziele: Zverev vs Jodar nie wczesniej niz 14:00 CET, Shelton vs Fils nie wczesniej niz 20:30. Poniedzialek: Alcaraz vs Tiafoe, Medvedev vs Cobolli. W Turynie nie rozegrano jeszcze zadnego singla."
            ]
        },
        "zh": {
            "title": "弗里茨淘汰穆塞蒂晋级斯德哥尔摩决赛；蒂兰特今日迎来生涯首个ATP决赛",
            "subtitle": "鲁内退赛与半决赛6-4、6-2让泰勒·弗里茨对阵蒂兰特。都灵循环赛周日以兹维列夫对霍达尔揭幕。",
            "excerpt": "斯德哥尔摩决赛今日：弗里茨对蒂兰特。周五：弗里茨6-4、6-2穆塞蒂；蒂兰特7-5、7-6(1)塔比洛。都灵周日开赛。无决赛比分、无都灵比分。",
            "body": [
                "泰勒·弗里茨将于11月14日周六在皇家网球馆出战Bybit斯德哥尔摩公开赛决赛。头号种子周四四分之一决赛因霍尔格·鲁内退赛以轮空晋级，周五仅用63分钟6-4、6-2击败洛伦佐·穆塞蒂。世界排名51的蒂兰特7-5、7-6(1)击败亚历杭德罗·塔比洛，迎来生涯首个ATP巡回赛决赛。冠军战尚未开打，不发布决赛比分。",
                "都灵Nitto ATP年终总决赛仍于11月15日周日在伊纳尔皮体育馆揭幕。分组自周四抽签未变：麦肯罗组（兹维列夫、谢尔顿、菲尔斯、霍达尔）与伦德尔组（阿尔卡拉斯、梅德韦杰夫、科博利、蒂亚福）。周日单打：兹维列夫对霍达尔不早于中欧时间14:00，谢尔顿对菲尔斯不早于20:30。周一：阿尔卡拉斯对蒂亚福，梅德韦杰夫对科博利。都灵尚未进行任何单打。"
            ]
        },
        "ja": {
            "title": "フリッツがムセッティを破りストックホルム決勝へ；ティランテは本日ATP初決勝",
            "subtitle": "ルーンの棄権と6-4, 6-2の準決勝でテイラー・フリッツがティランテと対戦。トリノの総当たりは日曜にズベレフ対ホダールで開幕。",
            "excerpt": "ストックホルム決勝は本日：フリッツ対ティランテ。金曜：フリッツがムセッティに6-4, 6-2；ティランテがタビロに7-5, 7-6(1)。トリノは日曜開幕。決勝スコアもトリノのスコアもなし。",
            "body": [
                "テイラー・フリッツは11月14日土曜、クングリガ・テニスハレンでBybitストックホルム・オープン決勝に臨む。トップシードは木曜準々決勝でホルガ・ルーンが棄権して勝ち上がり、金曜は63分でロレンツォ・ムセッティを6-4, 6-2。ATP51位のティアゴ・アグスティン・ティランテはアレハンドロ・タビロを7-5, 7-6(1)で破りツアー初決勝。決勝は未開催でスコアは掲載しない。",
                "トリノのNitto ATPファイナルズは引き続き11月15日日曜にイナルピ・アリーナで開幕する。グループは木曜抽選から不変：マクエンロー（ズベレフ、シェルトン、フィス、ホダール）とレンドル（アルカラス、メドベージェフ、コボリ、ティアフォー）。日曜シングルス：ズベレフ対ホダールは14:00 CET以降、シェルトン対フィスは20:30以降。月曜：アルカラス対ティアフォー、メドベージェフ対コボリ。トリノのシングルスは未実施。"
            ]
        },
        "ko": {
            "title": "프리츠, 무세티 꺾고 스톡홀름 결승; 티란테는 오늘 ATP 첫 결승",
            "subtitle": "루네 기권승과 6-4, 6-2 준결승으로 테일러 프리츠가 티란테와 만납니다. 토리노 조별리그는 일요일 츠베레프 vs 호다르로 시작합니다.",
            "excerpt": "스톡홀름 결승 오늘: 프리츠 vs 티란테. 금요일: 프리츠 d 무세티 6-4, 6-2; 티란테 d 타빌로 7-5, 7-6(1). 토리노 일요일 개막. 결승 스코어와 토리노 스코어 없음.",
            "body": [
                "테일러 프리츠가 11월 14일 토요일 쿵리가 테니스할렌에서 바이빗 스톡홀름 오픈 결승에 나섭니다. 1시드는 목요일 8강에서 홀거 루네가 기권해 진출했고 금요일 63분 만에 로렌조 무세티를 6-4, 6-2로 꺾었습니다. ATP 51위 티아고 아구스틴 티란테는 알레한드로 타빌로를 7-5, 7-6(1)로 꺾고 커리어 첫 ATP 결승에 올랐습니다. 결승전은 예정이며 스코어는 게시하지 않습니다.",
                "토리노 니토 ATP 파이널스는 11월 15일 일요일 이날피 아레나에서 그대로 개막합니다. 조 편성은 목요일 추첨 이후 변동 없습니다: 맥엔로(츠베레프, 셸턴, 필스, 호다르)와 렌들(알카라스, 메드베데프, 코볼리, 티아포). 일요일 단식: 츠베레프 vs 호다르는 14:00 CET 이후, 셸턴 vs 필스는 20:30 이후. 월요일: 알카라스 vs 티아포, 메드베데프 vs 코볼리. 토리노 단식은 아직 열리지 않았습니다."
            ]
        },
        "ar": {
            "title": "فريتز يبلغ نهائي ستوكهولم بعد موسيتي؛ تيرانت يخوض اليوم أول نهائي ATP",
            "subtitle": "انسحاب رون ونتيجة 6-4 و6-2 في نصف النهائي يضعان تايلور فريتز أمام تياغو أغوستين تيرانت. دوري تورينو يبدأ الأحد بزفيريف ضد خودار.",
            "excerpt": "نهائي ستوكهولم اليوم: فريتز ضد تيرانت. الجمعة: فريتز يتفوق على موسيتي 6-4، 6-2؛ تيرانت على تابيلو 7-5، 7-6 (1). تورينو تفتح الأحد. لا نتيجة للنهائي ولا لتورينو.",
            "body": [
                "تايلور فريتز في نهائي بطولة بايبت ستوكهولم اليوم السبت 14 نوفمبر في كونغليغا تنيسهالن. تقدم المصنف الأول بعد انسحاب هولغر رون من ربع النهائي الخميس ثم فاز على لورنزو موسيتي 6-4، 6-2 في 63 دقيقة الجمعة. تياغو أغوستين تيرانت (المرتبة 51) يخوض أول نهائي ATP في مسيرته بعد 7-5، 7-6 (1) على أليخاندرو تابيلو. المباراة النهائية قادمة ولا تُنشر نتيجتها.",
                "نهائيات نيتو ATP في تورينو ما زالت تفتح الأحد 15 نوفمبر في إنالبي أرينا. المجموعتان لم تتغيرا منذ قرعة الخميس: ماكنرو (زفيريف، شيلتون، فيلس، خودار) وليندل (ألكاراز، ميدفيديف، كوبولي، تيافو). فردي الأحد: زفيريف ضد خودار ليس قبل 14:00 CET، شيلتون ضد فيلس ليس قبل 20:30. الاثنين: ألكاراز ضد تيافو، ميدفيديف ضد كوبولي. لم تُلعب أي فردي في تورينو."
            ]
        }
    },
    "dp-world-tour-dubai-r2-mcilroy-hatton-share-lead-2026": {
        "fr": {
            "title": "Dubai 36 trous : McIlroy et Hatton partagent 139, Luiten recule ; T3 non publiee",
            "subtitle": "Les totaux AP de vendredi placent Rory McIlroy et Tyrrell Hatton a cinq sous le par, un coup devant Joost Luiten. Le troisieme tour samedi n'est pas affiche comme final.",
            "excerpt": "T2 terminee : McIlroy 69-70 et Hatton 70-69 menent a 139. Luiten 67-73=140. Chacarra 72-71=143 (T11). Le T3 samedi est en cours et non publie.",
            "body": [
                "Associated Press a publie les scores complets du deuxieme tour vendredi 13 novembre sur l'Earth Course a Jumeirah Golf Estates. Rory McIlroy signe 69-70 pour 139 (cinq sous le par) et partage la tete du DP World Tour Championship avec Tyrrell Hatton (70-69). Joost Luiten, auteur d'un 67 jeudi, ajoute un 73 pour 140 aux cotes de Kristoffer Reitan (70-70). Mikael Lindberg, Victor Perez et Freddy Schott sont a 141.",
                "Le leader de la Race to Dubai Eugenio Lopez-Chacarra est a 72-71 pour 143, a egalite pour la 11e place avec Francesco Laporta, Adrian Meronk et le dauphin du premier tour Jacob Skov Olesen (68-75). La finale a 10 millions de dollars a encore 36 trous. Le troisieme tour est en cours samedi 14 novembre et n'est pas publie comme final. Dimanche aura lieu le quatrieme tour."
            ]
        },
        "es": {
            "title": "Dubai 36 hoyos: McIlroy y Hatton comparten 139, Luiten cede; R3 no publicada",
            "subtitle": "Los totales de Associated Press del viernes ponen a Rory McIlroy y Tyrrell Hatton a cinco bajo, uno por delante de Joost Luiten. La tercera ronda del sabado no se publica como final.",
            "excerpt": "R2 cerrada: McIlroy 69-70 y Hatton 70-69 lideran con 139. Luiten 67-73=140. Chacarra 72-71=143 (T11). La R3 del sabado esta en juego y no se publica.",
            "body": [
                "Associated Press publico las tarjetas completas de la segunda ronda el viernes 13 de noviembre en Earth Course, Jumeirah Golf Estates. Rory McIlroy firma 69-70 para 139 (cinco bajo par) y comparte el liderato del DP World Tour Championship con Tyrrell Hatton (70-69). Joost Luiten, que abrio con 67, suma un 73 para 140 junto a Kristoffer Reitan (70-70). Mikael Lindberg, Victor Perez y Freddy Schott estan en 141.",
                "El lider de la Race to Dubai Eugenio Lopez-Chacarra va 72-71 para 143, empatado en el 11 con Francesco Laporta, Adrian Meronk y el segundo de la primera ronda Jacob Skov Olesen (68-75). La final de 10 millones de dolares tiene 36 hoyos por delante. La tercera ronda esta en juego el sabado 14 de noviembre y no se publica como final. El domingo es la cuarta ronda."
            ]
        },
        "de": {
            "title": "Dubai 36 Loecher: McIlroy und Hatton teilen 139, Luiten rutscht; R3 unveröffentlicht",
            "subtitle": "Die AP-Totals vom Freitag setzen Rory McIlroy und Tyrrell Hatton auf fünf unter Par, einen vor Joost Luiten. Die dritte Runde am Samstag gilt nicht als Finale.",
            "excerpt": "R2 komplett: McIlroy 69-70 und Hatton 70-69 führen mit 139. Luiten 67-73=140. Chacarra 72-71=143 (T11). R3 samstags laeuft und wird nicht veroeffentlicht.",
            "body": [
                "Associated Press stellte am Freitag, 13. November, vollstaendige Zweitrounden-Scores vom Earth Course in Jumeirah Golf Estates ein. Rory McIlroy spielt 69-70 auf 139 (fünf unter Par) und teilt die Fuehrung der DP World Tour Championship mit Tyrrell Hatton (70-69). Joost Luiten, der mit 67 eroeffnete, legt eine 73 nach und steht bei 140 neben Kristoffer Reitan (70-70). Mikael Lindberg, Victor Perez und Freddy Schott liegen bei 141.",
                "Race-to-Dubai-Fuehrer Eugenio Lopez-Chacarra steht 72-71 fuer 143, gleichauf auf Platz 11 mit Francesco Laporta, Adrian Meronk und dem R1-Zweiten Jacob Skov Olesen (68-75). Das 10-Millionen-Saisonfinale hat noch 36 Loecher. Runde 3 laeuft am Samstag, 14. November, und wird nicht als Finale veroeffentlicht. Sonntag folgt Runde 4."
            ]
        },
        "it": {
            "title": "Dubai 36 buche: McIlroy e Hatton condividono 139, Luiten scivola; R3 non pubblicata",
            "subtitle": "I totali AP di venerdi mettono Rory McIlroy e Tyrrell Hatton a cinque sotto, uno sopra Joost Luiten. Il terzo giro di sabato non e pubblicato come finale.",
            "excerpt": "R2 chiusa: McIlroy 69-70 e Hatton 70-69 in testa a 139. Luiten 67-73=140. Chacarra 72-71=143 (T11). La R3 di sabato e in corso e non pubblicata.",
            "body": [
                "Associated Press ha pubblicato i punteggi completi del secondo giro venerdi 13 novembre sull'Earth Course a Jumeirah Golf Estates. Rory McIlroy firma 69-70 per 139 (cinque sotto par) e condivide il comando del DP World Tour Championship con Tyrrell Hatton (70-69). Joost Luiten, partito con 67, aggiunge un 73 per 140 insieme a Kristoffer Reitan (70-70). Mikael Lindberg, Victor Perez e Freddy Schott sono a 141.",
                "Il leader della Race to Dubai Eugenio Lopez-Chacarra e 72-71 per 143, a pari 11esimo con Francesco Laporta, Adrian Meronk e il secondo del primo giro Jacob Skov Olesen (68-75). La finale da 10 milioni di dollari ha ancora 36 buche. Il terzo giro e in corso sabato 14 novembre e non e pubblicato come finale. Domenica e il quarto giro."
            ]
        },
        "pl": {
            "title": "Dubaj 36 dolek: McIlroy i Hatton dziela 139, Luiten spada; R3 niepublikowana",
            "subtitle": "Piatekowe sumy AP stawiają Rory'ego McIlroya i Tyrrella Hattona na piec pod parem, jeden przed Joostem Luitenem. Sobotnia trzecia runda nie jest publikowana jako final.",
            "excerpt": "R2 zakonczona: McIlroy 69-70 i Hatton 70-69 prowadza z 139. Luiten 67-73=140. Chacarra 72-71=143 (T11). R3 w sobote trwa i nie jest publikowana.",
            "body": [
                "Associated Press opublikowalo pelne wyniki drugiej rundy w piatek 13 listopada na Earth Course w Jumeirah Golf Estates. Rory McIlroy gra 69-70 na 139 (piec pod parem) i dzieli prowadzenie DP World Tour Championship z Tyrrellem Hattonem (70-69). Joost Luiten, ktory otworzyl 67, doklada 73 na 140 obok Kristoffera Reitana (70-70). Mikael Lindberg, Victor Perez i Freddy Schott sa na 141.",
                "Lider Race to Dubai Eugenio Lopez-Chacarra ma 72-71 na 143, ex aequo na 11. miejscu z Francesco Laporta, Adrianem Meronkiem i wiceliderem pierwszej rundy Jacobem Skovem Olesenem (68-75). Final za 10 milionow dolarow ma jeszcze 36 dolek. Trzecia runda trwa w sobote 14 listopada i nie jest publikowana jako final. Niedziela to czwarta runda."
            ]
        },
        "zh": {
            "title": "迪拜36洞：麦克罗伊与哈顿并列139杆，吕腾下滑；第三轮不作为完场",
            "subtitle": "美联社周五总计将麦克罗伊与哈顿排在五杆低于标准杆，领先吕腾一杆。周六第三轮不作为完场发布。",
            "excerpt": "第二轮收杆：麦克罗伊69-70、哈顿70-69并列139。吕腾67-73=140。查卡拉72-71=143（并列11）。周六第三轮进行中未发布。",
            "body": [
                "美联社于11月13日周五公布朱美拉高尔夫庄园地球球场完整第二轮成绩。罗里·麦克罗伊69-70合计139杆（低于标准杆五杆），与泰瑞尔·哈顿（70-69）并列DP世界巡回赛锦标赛领先。周四打出67杆的约斯特·吕腾再打73杆合计140，与克里斯托弗·雷坦（70-70）并列。林德贝里、佩雷斯与肖特位于141杆。",
                "迪拜积分榜领跑者欧亨尼奥·查卡拉72-71合计143杆，与拉波尔塔、梅龙克及首轮第二雅各布·斯科夫·奥勒森（68-75）并列第11。千万美元赛季收官战还剩36洞。第三轮于11月14日周六进行中，不作为完场发布。周日为第四轮。"
            ]
        },
        "ja": {
            "title": "ドバイ36ホール：マキロイとハットンが139で首位タイ、ルイテン後退；3日目は非掲載",
            "subtitle": "金曜のAP集計でローリー・マキロイとティレル・ハットンが5アンダー、ヨスト・ルイテンに1打差。土曜の第3ラウンドは最終として掲載しない。",
            "excerpt": "2日目終了：マキロイ69-70、ハットン70-69が139で首位。ルイテン67-73=140。チャカラ72-71=143（T11）。土曜3日目は進行中で非掲載。",
            "body": [
                "AP通信は11月13日金曜、ジュメイラ・ゴルフ・エステーツのアースコースから完全な2日目スコアを配信した。ローリー・マキロイは69-70で139（5アンダー）とし、ティレル・ハットン（70-69）とDPワールドツアー選手権の首位を分け合う。木曜67のヨスト・ルイテンは73を加えて140、クリストフェル・レイタン（70-70）と並ぶ。リンドベリ、ペレス、ショットは141。",
                "レース・トゥ・ドバイ首位のエウヘニオ・チャカラは72-71で143、ラポルタ、メロンク、初日2位のヤコブ・スコウ・オレセン（68-75）と11位タイ。1000万ドルのシーズン最終戦は残り36ホール。第3ラウンドは11月14日土曜進行中で最終としては掲載しない。日曜が第4ラウンド。"
            ]
        },
        "ko": {
            "title": "두바이 36홀: 매킬로이·해튼 139 공동 선두, 라위텐 하락; 3R 미게시",
            "subtitle": "AP 금요일 합계가 로리 매킬로이와 타렐 해튼을 5언더, 요스트 라위텐보다 1타 앞에 둡니다. 토요일 3라운드는 최종으로 올리지 않습니다.",
            "excerpt": "2R 종료: 매킬로이 69-70, 해튼 70-69이 139로 선두. 라위텐 67-73=140. 차카라 72-71=143(T11). 토요일 3R는 진행 중이며 미게시.",
            "body": [
                "AP가 11월 13일 금요일 주메이라 골프 에스테이트 어스 코스에서 완전한 2라운드 스코어를 발표했습니다. 로리 매킬로이가 69-70으로 139타(5언더)를 쳐 DP 월드 투어 챔피언십 선두를 타렐 해튼(70-69)과 나눕니다. 목요일 67타의 요스트 라위텐은 73타를 더해 140, 크리스토페르 레이탄(70-70)과 함께입니다. 린드베리, 페레스, 쇼트는 141타입니다.",
                "레이스 투 두바이 선두 에우헤니오 차카라는 72-71로 143타, 라포르타, 메롱크, 1라운드 2위 야코브 스코브 올레센(68-75)과 공동 11위입니다. 1000만 달러 시즌 최종전은 36홀이 남았습니다. 3라운드는 11월 14일 토요일 진행 중이며 최종으로 게시하지 않습니다. 일요일이 4라운드입니다."
            ]
        },
        "ar": {
            "title": "دبي 36 حفرة: ماكلروي وهاتون يقتسمان 139 ويتراجع لويتن؛ الجولة 3 غير منشورة",
            "subtitle": "مجاميع أسوشيتد برس يوم الجمعة تضع روري ماكلروي وتيريل هاتون عند خمسة تحت البار، ضربة أمام جوست لويتن. الجولة الثالثة السبت لا تُنشر كنهاية.",
            "excerpt": "الجولة 2 مكتملة: ماكلروي 69-70 وهاتون 70-69 يتصدران بـ139. لويتن 67-73=140. تشاكارا 72-71=143 (ح11). الجولة 3 السبت جارية وغير منشورة.",
            "body": [
                "نشرت أسوشيتد برس نتائج الجولة الثانية الكاملة الجمعة 13 نوفمبر من إيرث كورس في جميرا غولف إستيتس. سجل روري ماكلروي 69-70 لـ139 (خمسة تحت البار) ويشارك صدارة بطولة جولة DP العالمية مع تيريل هاتون (70-69). جوست لويتن، صاحب 67 يوم الخميس، أضاف 73 لـ140 إلى جانب كريستوفر ريتان (70-70). ميكائيل ليندبرغ وفيكتور بيريز وفريدي شوت عند 141.",
                "متصدر سباق دبي أوخينيو لوبيز تشاكارا عند 72-71 لـ143، متعادل في المركز 11 مع فرانشيسكو لابورتا وأدريان ميرونك ووصيف الجولة الأولى يعقوب سكوف أولسن (68-75). النهائي بجائزة 10 ملايين دولار ما زال فيه 36 حفرة. الجولة الثالثة جارية السبت 14 نوفمبر ولا تُنشر كنهاية. الأحد الجولة الرابعة."
            ]
        }
    },
    "f1-five-days-las-vegas-round-21-p2-chase-2026": {
        "fr": {
            "title": "J-5 avant Las Vegas : Verstappen a Norris toujours groupes en 33 points",
            "subtitle": "Aucun Grand Prix du Strip 2026 n'a ete couru. Antonelli (390) et Mercedes (652) restent champions apres Sao Paulo.",
            "excerpt": "La manche 21 a lieu du 19 au 21 novembre sur 6,201 km a Las Vegas. Classement inchange : Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246. Pas de resultat de course.",
            "body": [
                "Il reste cinq jours avant la manche 21 du championnat du monde FIA de Formule 1 2026 sur le circuit urbain de Las Vegas de 6,201 km (19-21 novembre, course de samedi soir le 21). Aucun essai, qualification ni resultat de course de cet evenement n'a ete enregistre.",
                "Le champion des pilotes Kimi Antonelli est a 390 points et Mercedes a 652 points constructeurs apres Interlagos. La lutte pour la deuxieme place est figee : Max Verstappen 279, George Russell 262, Lewis Hamilton 261, Charles Leclerc 249, Lando Norris 246. Ferrari a 510 points constructeurs, Red Bull 415, McLaren 398. Le Qatar est le 29 novembre, Abou Dabi le 6 decembre. Ne pas convertir un resultat de Las Vegas d'une annee anterieure dans cette horloge."
            ]
        },
        "es": {
            "title": "Cinco dias para Las Vegas: Verstappen y Norris siguen juntos en 33 puntos",
            "subtitle": "No se ha disputado ningun Gran Premio del Strip 2026. Antonelli (390) y Mercedes (652) siguen campeones tras Sao Paulo.",
            "excerpt": "La ronda 21 es del 19 al 21 de noviembre en 6,201 km en Las Vegas. Clasificacion igual: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246. Sin resultado de carrera.",
            "body": [
                "Quedan cinco dias para la ronda 21 del Mundial FIA de Formula 1 2026 en el circuito urbano de Las Vegas de 6,201 km (19-21 de noviembre, carrera sabado noche 21). No se ha registrado ningun libre, clasificacion ni resultado de carrera de este evento.",
                "El campeon de pilotos Kimi Antonelli suma 390 puntos y Mercedes 652 de Constructores tras Interlagos. La pelea por el segundo puesto esta congelada: Max Verstappen 279, George Russell 262, Lewis Hamilton 261, Charles Leclerc 249, Lando Norris 246. Ferrari tiene 510 de Constructores, Red Bull 415, McLaren 398. Qatar es el 29 de noviembre, Abu Dabi el 6 de diciembre. No convertir un resultado de Las Vegas de otro ano a este reloj."
            ]
        },
        "de": {
            "title": "Fuenf Tage bis Las Vegas: Verstappen bis Norris weiter in 33 Punkten",
            "subtitle": "Ein Strip-Grand-Prix 2026 hat nicht stattgefunden. Antonelli (390) und Mercedes (652) bleiben nach Sao Paulo Weltmeister.",
            "excerpt": "Runde 21 ist vom 19. bis 21. November auf 6,201 km in Las Vegas. Stand unveraendert: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246. Kein Rennergebnis.",
            "body": [
                "Es bleiben fuenf Tage bis Runde 21 der FIA-Formel-1-Weltmeisterschaft 2026 auf dem 6,201 Kilometer langen Las-Vegas-Strip-Circuit (19.-21. November, Rennen Samstagnacht 21.). Es gibt kein Training, kein Qualifying und kein Rennergebnis dieses Events.",
                "Fahrerweltmeister Kimi Antonelli steht bei 390 Punkten, Mercedes bei 652 Konstrukteurspunkten nach Interlagos. Der Kampf um Platz zwei ist eingefroren: Max Verstappen 279, George Russell 262, Lewis Hamilton 261, Charles Leclerc 249, Lando Norris 246. Ferrari hat 510 Konstrukteurspunkte, Red Bull 415, McLaren 398. Katar ist am 29. November, Abu Dhabi am 6. Dezember. Kein Vorjahres-Las-Vegas-Ergebnis in diese Uhr uebernehmen."
            ]
        },
        "it": {
            "title": "Cinque giorni a Las Vegas: Verstappen e Norris ancora chiusi in 33 punti",
            "subtitle": "Nessun Gran Premio dello Strip 2026 e stato corso. Antonelli (390) e Mercedes (652) restano campioni dopo San Paolo.",
            "excerpt": "La Round 21 e dal 19 al 21 novembre sui 6,201 km di Las Vegas. Classifica invariata: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246. Nessun risultato di gara.",
            "body": [
                "Mancano cinque giorni alla Round 21 del campionato mondiale FIA di Formula 1 2026 sul circuito cittadino di Las Vegas da 6,201 km (19-21 novembre, gara sabato sera 21). Non e stato registrato alcun turno libero, qualifiche o risultato di gara di questo evento.",
                "Il campione piloti Kimi Antonelli e a 390 punti e Mercedes a 652 punti Costruttori dopo Interlagos. La lotta per il secondo posto e ferma: Max Verstappen 279, George Russell 262, Lewis Hamilton 261, Charles Leclerc 249, Lando Norris 246. Ferrari ha 510 punti Costruttori, Red Bull 415, McLaren 398. Il Qatar e il 29 novembre, Abu Dhabi il 6 dicembre. Non convertire un risultato di Las Vegas di un altro anno in questo orologio."
            ]
        },
        "pl": {
            "title": "Piec dni do Las Vegas: Verstappen i Norris nadal w 33 punktach",
            "subtitle": "Zaden Grand Prix Strip 2026 sie nie odbyl. Antonelli (390) i Mercedes (652) pozostaja mistrzami po Sao Paulo.",
            "excerpt": "Runda 21 trwa 19-21 listopada na 6,201 km w Las Vegas. Klasyfikacja bez zmian: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246. Bez wyniku wyscigu.",
            "body": [
                "Zostalo piec dni do rundy 21 mistrzostw swiata FIA Formuly 1 2026 na ulicznym torze Las Vegas o dlugosci 6,201 km (19-21 listopada, wyscig w sobote wieczorem 21). Nie zarejestrowano zadnego treningu, kwalifikacji ani wyniku wyscigu tej imprezy.",
                "Mistrz kierowcow Kimi Antonelli ma 390 punktow, Mercedes 652 punkty konstruktorow po Interlagos. Walka o drugie miejsce stoi: Max Verstappen 279, George Russell 262, Lewis Hamilton 261, Charles Leclerc 249, Lando Norris 246. Ferrari ma 510 punktow konstruktorow, Red Bull 415, McLaren 398. Katar 29 listopada, Abu Zabi 6 grudnia. Nie przenosic wyniku Las Vegas z innego roku na ten zegar."
            ]
        },
        "zh": {
            "title": "拉斯维加斯倒计时五天：维斯塔潘至诺里斯仍困在33分差内",
            "subtitle": "2026年大道大奖赛尚未开跑。安东内利（390分）与梅赛德斯（652分）在圣保罗后仍为双冠王。",
            "excerpt": "第21站于11月19-21日在6.201公里拉斯维加斯赛道举行。积分不变：维斯塔潘279、拉塞尔262、汉密尔顿261、勒克莱尔249、诺里斯246。无比赛成绩。",
            "body": [
                "距2026赛季F1世界锦标赛第21站还剩五天，赛事将在6.201公里拉斯维加斯大道赛道举行（11月19-21日，正赛为21日周六夜）。本次分站尚未记录任何练习、排位或正赛成绩。",
                "车手冠军基米·安东内利积390分，梅赛德斯在英特拉格斯后积652分车队积分。第二名争夺冻结：马克斯·维斯塔潘279、乔治·拉塞尔262、刘易斯·汉密尔顿261、夏尔·勒克莱尔249、兰多·诺里斯246。法拉利车队510分，红牛415，迈凯伦398。卡塔尔站11月29日，阿布扎比12月6日。请勿把往年拉斯维加斯成绩套入此时钟。"
            ]
        },
        "ja": {
            "title": "ラスベガスまで5日：フェルスタッペンからノリスまでなお33点圏",
            "subtitle": "2026年ストリップGPは未開催。アントネッリ（390点）とメルセデス（652点）はサンパウロ後も王者。",
            "excerpt": "第21戦は11月19-21日、ラスベガス6.201km。順位不変：フェルスタッペン279、ラッセル262、ハミルトン261、ルクレール249、ノリス246。レース結果なし。",
            "body": [
                "2026年FIA F1世界選手権第21戦まであと5日。舞台は全長6.201キロのラスベガス・ストリップ・サーキット（11月19-21日、決勝は21日土曜夜）。本イベントのフリー走行、予選、決勝結果は記録されていない。",
                "ドライバー王者キミ・アントネッリは390点、メルセデスはインテルラゴス後にコンストラクターズ652点。2位争いは凍結：マックス・フェルスタッペン279、ジョージ・ラッセル262、ルイス・ハミルトン261、シャルル・ルクレール249、ランド・ノリス246。フェラーリは510、レッドブル415、マクラーレン398。カタールは11月29日、アブダビは12月6日。過去年のラスベガス結果をこの時計に入れない。"
            ]
        },
        "ko": {
            "title": "라스베이거스 D-5: 베르스타펜부터 노리스까지 여전히 33점 차",
            "subtitle": "2026 스트립 그랑프리는 열리지 않았습니다. 안토넬리(390점)와 메르세데스(652점)는 상파울루 이후에도 챔피언입니다.",
            "excerpt": "21라운드는 11월 19-21일 라스베이거스 6.201km. 순위 변동 없음: 베르스타펜 279, 러셀 262, 해밀턴 261, 르클레르 249, 노리스 246. 경기 결과 없음.",
            "body": [
                "2026 FIA 포뮬러 1 월드 챔피언십 21라운드까지 5일 남았습니다. 장소는 6.201km 라스베이거스 스트립 서킷(11월 19-21일, 본선은 21일 토요일 밤)입니다. 이 대회의 연습, 예선, 본선 결과는 기록되지 않았습니다.",
                "드라이버 챔피언 키미 안토넬리는 390점, 메르세데스는 인터라고스 이후 컨스트럭터즈 652점입니다. 2위 싸움은 멈춰 있습니다: 막스 베르스타펜 279, 조지 러셀 262, 루이스 해밀턴 261, 샤를 르클레르 249, 랜도 노리스 246. 페라리 510, 레드불 415, 맥라렌 398. 카타르는 11월 29일, 아부다비는 12월 6일. 다른 해의 라스베이거스 결과를 이 시계에 넣지 마십시오."
            ]
        },
        "ar": {
            "title": "خمسة أيام على لاس فيغاس: فيرستابن ونوريس ما زالا داخل 33 نقطة",
            "subtitle": "لم يُقم أي سباق جائزة ستريب الكبرى 2026. أنطونيلي (390) ومرسيدس (652) يبقيان بطلين بعد ساو باولو.",
            "excerpt": "الجولة 21 من 19 إلى 21 نوفمبر على 6.201 كلم في لاس فيغاس. الترتيب دون تغيير: فيرستابن 279، راسل 262، هاميلتون 261، لوكلير 249، نوريس 246. لا نتيجة سباق.",
            "body": [
                "تبقى خمسة أيام على الجولة 21 من بطولة العالم للفورمولا 1 2026 على حلبة شوارع لاس فيغاس بطول 6.201 كلم (19-21 نوفمبر، السباق ليلة السبت 21). لم يُسجل أي تدريب أو تصفيات أو نتيجة سباق لهذا الحدث.",
                "بطل السائقين كيمي أنطونيلي عند 390 نقطة ومرسيدس عند 652 نقطة للصانعين بعد إنترلاغوس. معركة المركز الثاني مجمدة: ماكس فيرستابن 279، جورج راسل 262، لويس هاميلتون 261، شارل لوكلير 249، لاندو نوريس 246. فيراري لديه 510 للصانعين، ريد بول 415، مكلارين 398. قطر في 29 نوفمبر وأبوظبي في 6 ديسمبر. لا تحول نتيجة لاس فيغاس من عام سابق إلى هذه الساعة."
            ]
        }
    },
}

NEW_TEAMS = {
    "Thiago Agustin Tirante": {"fr": "Thiago Agustin Tirante", "es": "Thiago Agustin Tirante", "de": "Thiago Agustin Tirante", "it": "Thiago Agustin Tirante", "pl": "Thiago Agustin Tirante", "zh": "蒂兰特", "ja": "ティアゴ・アグスティン・ティランテ", "ko": "티아고 아구스틴 티란테", "ar": "تياغو أغوستين تيرانت"},
    "San Antonio Spurs": {"zh": "圣安东尼奥马刺", "ja": "サンアントニオ・スパーズ", "ko": "샌안토니오 스퍼스", "ar": "سان أنطونيو سبرز"},
    "Detroit Pistons": {"zh": "底特律活塞", "ja": "デトロイト・ピストンズ", "ko": "디트로이트 피스톤스", "ar": "ديترويت بيستونز"},
    "Tyrrell Hatton": {"zh": "泰瑞尔·哈顿", "ja": "ティレル・ハットン", "ko": "타렐 해튼", "ar": "تيريل هاتون"},
    "Stephon Castle": {"zh": "斯蒂芬·卡斯尔", "ja": "ステフォン・キャッスル", "ko": "스테폰 캐슬", "ar": "ستيفون كاسل"},
    "New England Patriots": {"zh": "新英格兰爱国者", "ja": "ニューイングランド・ペイトリオッツ", "ko": "뉴잉글랜드 패트리어츠", "ar": "نيو إنغلاند باتريوتس"},
    "Detroit Lions": {"zh": "底特律雄狮", "ja": "デトロイト・ライオンズ", "ko": "디트로이트 라이온스", "ar": "ديترويت ليونز"},
}

NEW_PLACES = {
    "Frost Bank Center": {"zh": "霜冻银行中心", "ja": "フロスト・バンク・センター", "ko": "프로스트 뱅크 센터", "ar": "فروست بانك سنتر"},
    "Metropolitano": {"fr": "Metropolitano", "es": "Metropolitano", "de": "Metropolitano", "it": "Metropolitano", "pl": "Metropolitano", "zh": "大都会球场", "ja": "メトロポリターノ", "ko": "메트로폴리타노", "ar": "المتروبوليتانو"},
    "Munich": {"fr": "Munich", "es": "Múnich", "de": "Muenchen", "it": "Monaco di Baviera", "pl": "Monachium", "zh": "慕尼黑", "ja": "ミュンヘン", "ko": "뮌헨", "ar": "ميونخ"},
    "Kungliga Tennishallen": {"zh": "皇家网球馆", "ja": "クングリガ・テニスハレン", "ko": "쿵리가 테니스할렌", "ar": "كونغليغا تنيسهالن"},
}

NEW_COMPETITIONS = {}


def lint_obj(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            lint_obj(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            lint_obj(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        s = re.sub(r"https?://\S+", "", obj)
        if "\u2014" in s or "--" in s:
            raise SystemExit(f"Disallowed dash in {path}: {s[:80]}")


def inject_dict_entries(ts_text, dict_header, closing_regex, new_entries):
    start = ts_text.find(dict_header)
    assert start != -1, f"Missing header {dict_header}"
    m = re.search(closing_regex, ts_text[start:])
    assert m is not None, f"Missing closing {closing_regex} after {dict_header}"
    end = start + m.start()
    block = ts_text[start:end]
    to_add = []
    for k, v in new_entries.items():
        if f"'{k}':" in block or f'"{k}":' in block or f" {k}: {{" in block:
            continue
        to_add.append(f"  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)},")
    if not to_add:
        return ts_text
    newline = "\r\n" if "\r\n" in ts_text[:500] else "\n"
    insertion = newline + newline.join(to_add) + newline
    return ts_text[:end] + insertion + ts_text[end:]


if __name__ == "__main__":
    lint_obj(NOV14_STORIES)
    lint_obj(NEW_TEAMS)
    lint_obj(NEW_PLACES)
    lint_obj(NEW_COMPETITIONS)
    print("All Nov 14 translations validated: 0 em-dashes and 0 double-hyphens.")

    stories_file = os.path.join(ROOT, "frontend/src/i18n/stories.ts")
    with open(stories_file, "r", encoding="utf-8") as f:
        st_content = f.read()

    to_inject = []
    for slug, langs in NOV14_STORIES.items():
        if f'"{slug}":' in st_content or f"'{slug}':" in st_content:
            print(f"Skipping already-present slug in stories.ts: {slug}")
        else:
            to_inject.append(f"  {json.dumps(slug)}: {json.dumps(langs, ensure_ascii=False, indent=2)},")

    if to_inject:
        target = "export const STORY_I18N: Record<string, LocMap> = {\n"
        assert target in st_content, "Target marker not found in stories.ts"
        st_content = st_content.replace(target, target + "\n".join(to_inject) + "\n", 1)

    with open(stories_file, "w", encoding="utf-8") as f:
        f.write(st_content)
    print("Updated frontend/src/i18n/stories.ts successfully.")

    names_file = os.path.join(ROOT, "frontend/src/i18n/names.ts")
    with open(names_file, "r", encoding="utf-8") as f:
        names_content = f.read()

    names_content = inject_dict_entries(names_content, "const TEAMS:", r"\r?\n\};\r?\n\r?\nconst PLACES:", NEW_TEAMS)
    names_content = inject_dict_entries(names_content, "const PLACES:", r"\r?\n\};\r?\n\r?\nconst COMPETITIONS:", NEW_PLACES)
    if NEW_COMPETITIONS:
        names_content = inject_dict_entries(names_content, "const COMPETITIONS:", r"\r?\n\};\r?\n\r?\nexport function entityName", NEW_COMPETITIONS)

    with open(names_file, "w", encoding="utf-8") as f:
        f.write(names_content)
    print("Updated frontend/src/i18n/names.ts successfully.")
