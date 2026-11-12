#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add 12 November 2026 story translations (all 9 non-en locales) and entity/competition translations to names.ts."""
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

NOV12_STORIES = {
    "uwcl-barcelona-arsenal-camp-nou-ol-lyonnes-6-0-juventus-2026": {
        "fr": {
            "title": "Choc au Camp Nou : Barcelone recoit Arsenal ce soir apres le 6-0 d'OL Lyonnes a la Juventus",
            "subtitle": "Arsenal Women joue son premier match officiel au Spotify Camp Nou dans un remake de la finale 2025, en meme temps qu'Angleterre-Croatie.",
            "excerpt": "Reporte de 24 heures par la tempete Charles, Barcelone (9 pts) recoit Arsenal (7 pts) quelques heures apres le succes 6-0 d'OL Lyonnes a Biella.",
            "body": [
                "Le football europeen de clubs et de selections se retrouve ce jeudi soir 12 novembre, avec en affiche FC Barcelona Femeni contre Arsenal Women au Spotify Camp Nou (18h45 CET) dans un remake de la finale 2025 de Lisbonne. Decale de 24 heures en raison des alertes de la tempete Charles, ce rendez-vous marque le premier match officiel d'Arsenal Women au Camp Nou. Barcelone compte trois victoires en trois journes (19 buts inscrits, plus un 7-0 face au Real Madrid en championnat) avec Aitana Bonmati et Alexia Putellas face a Alessia Russo et Arsenal (7 points).",
                "Cette affiche succede au festival offensif d'OL Lyonnes mercredi soir a Biella face a la Juventus Women (6-0), lance par un double de Marie-Antoinette Katoto (31e, 35e) avant des buts de Melchie Dumornay (40e), Lily Yohannes (80e), Korbin Albert (85e) et Wendie Renard (90+1e), alors que OH Leuven et HB Koge se sont separes sur un nul 1-1. En Ligue des nations ce jeudi : Angleterre-Croatie a Wembley (19h45 UK), Italie-France a San Siro, Tchequie-Espagne (20h45 CET) et Turquie-Belgique (18h00 CET)."
            ]
        },
        "es": {
            "title": "Partidazo en el Camp Nou: Barcelona recibe al Arsenal esta noche tras el 6-0 del OL Lyonnes a la Juventus",
            "subtitle": "El Arsenal femenino juega su primer partido oficial en el Spotify Camp Nou en una reedicion de la final de 2025 junto al Inglaterra-Croacia.",
            "excerpt": "Aplazado 24 horas por la borrasca Charles, el lider Barcelona (9 pts) recibe al Arsenal (7 pts) tras la goleada 6-0 del OL Lyonnes en Biella.",
            "body": [
                "El futbol europeo de clubes y selecciones coincide este jueves 12 de noviembre por la noche, con el FC Barcelona Femeni recibiendo al Arsenal Women en el Spotify Camp Nou (18:45 CET) en la reedicion de la final de Lisboa 2025. Aplazado un dia por los avisos de la borrasca Charles, sera el primer duelo oficial del Arsenal femenino en el Camp Nou. El Barcelona suma pleno de nueve puntos (19 goles en tres triunfos, ademas de un 7-0 al Real Madrid en liga) con Aitana Bonmati y Alexia Putellas frente a Alessia Russo y el Arsenal (7 puntos).",
                "El duelo llega despues de que el OL Lyonnes goleara 0-6 a la Juventus en Biella el miercoles con doblete de Marie-Antoinette Katoto (31', 35') y tantos de Melchie Dumornay (40'), Lily Yohannes (80'), Korbin Albert (85') y Wendie Renard (90+1'), mientras OH Leuven y HB Koge empataron 1-1. En la Liga de Naciones hoy: Inglaterra-Croacia en Wembley (19:45 UK), Italia-Francia en San Siro, Chequia-Espana (20:45 CET) y Turquia-Belgica (18:00 CET)."
            ]
        },
        "de": {
            "title": "Camp-Nou-Kracher: Barcelona empfaengt heute Arsenal nach OL Lyonnes' 6:0 bei Juventus",
            "subtitle": "Arsenal Women bestreiten ihr erstes Pflichtspiel im Spotify Camp Nou als Neuauflage des Finals 2025 neben England gegen Kroatien.",
            "excerpt": "Nach Sturm Charles um 24 Stunden verschoben, trifft Tabellenfuehrer Barcelona (9 Pkt.) auf Arsenal (7 Pkt.), kurz nach dem 6:0 von OL Lyonnes in Biella.",
            "body": [
                "Europaeischer Klub- und Laenderspiel-Abend am Donnerstag, 12. November: Der FC Barcelona Femeni empfaengt Arsenal Women um 18:45 Uhr MEZ im Spotify Camp Nou zur Neuauflage des Lissaboner Finals 2025. Wegen Sturm-Charles-Warnungen um einen Tag verlegt, ist es Arsenals erstes Pflichtspiel im Camp Nou. Barcelona steht bei drei Siegen aus drei Spielen (19 Tore sowie ein 7:0 in der Liga gegen Real Madrid) mit Aitana Bonmati und Alexia Putellas gegen Alessia Russo und Arsenal (7 Punkte).",
                "Zuvor feierte OL Lyonnes am Mittwoch ein 6:0 bei Juventus Women in Biella durch einen Doppelpack von Marie-Antoinette Katoto (31., 35.) sowie Tore von Melchie Dumornay (40.), Lily Yohannes (80.), Korbin Albert (85.) und Wendie Renard (90.+1), waehrend OH Leuven und HB Koge 1:1 spielten. In der Nations League heute: England gegen Kroatien in Wembley (19:45 UK), Italien gegen Frankreich in San Siro, Tschechien gegen Spanien (20:45 MEZ) und Tuerkei gegen Belgien (18:00 MEZ)."
            ]
        },
        "it": {
            "title": "Notte al Camp Nou: il Barcellona ospita l'Arsenal stasera dopo il 6-0 dell'OL Lyonnes alla Juventus",
            "subtitle": "L'Arsenal femminile gioca la sua prima gara ufficiale al Spotify Camp Nou nella rivincita della finale 2025 insieme a Inghilterra-Croazia.",
            "excerpt": "Rinviata di 24 ore per la tempesta Charles, la capolista Barcellona (9 punti) sfida l'Arsenal (7) dopo il 6-0 subito dalla Juventus a Biella.",
            "body": [
                "Grande serata europea giovedi 12 novembre, guidata da FC Barcelona Femeni contro Arsenal Women al Spotify Camp Nou (18:45 CET) nella rivincita della finale di Lisbona 2025. Spostata di un giorno per l'allerta tempesta Charles, segna la prima gara ufficiale dell'Arsenal Women al Camp Nou. Il Barcellona guida a punteggio pieno con 9 punti (19 gol segnati in tre gare e 7-0 al Real Madrid in campionato) con Aitana Bonmati e Alexia Putellas contro Alessia Russo e l'Arsenal (7 punti).",
                "Alla vigilia, l'OL Lyonnes aveva travolto 6-0 la Juventus Women a Biella grazie alla doppietta di Marie-Antoinette Katoto (31', 35') e alle reti di Melchie Dumornay (40'), Lily Yohannes (80'), Korbin Albert (85') e Wendie Renard (90+1'), mentre OH Leuven e HB Koge hanno pareggiato 1-1. In Nations League stasera: Italia-Francia a San Siro (20:45 CET), Inghilterra-Croazia a Wembley, Cechia-Spagna e Turchia-Belgio."
            ]
        },
        "pl": {
            "title": "Hit na Camp Nou: Barcelona podejmuje dzis Arsenal po wygranej OL Lyonnes 6:0 z Juventusem",
            "subtitle": "Pilkarki Arsenalu zagraja swoj pierwszy oficjalny mecz na Spotify Camp Nou w rewanzu za final 2025 obok starcia Anglii z Chorwacja.",
            "excerpt": "Przelozony o dobe przez sztorm Charles hit stawia niepokonana Barcelone (9 pkt) naprzeciw Arsenalu (7 pkt) tuz po triumfie OL Lyonnes 6:0 w Bielli.",
            "body": [
                "Czwartkowy wieczor 12 listopada laczy europejska piłke klubowa i reprezentacyjna, a na czele stoi starcie FC Barcelona Femeni z Arsenal Women na Spotify Camp Nou (18:45 CET) bedace rewanzem za final w Lizbonie z 2025 roku. Mecz przelozono o 24 godziny z powodu ostrzezen przed sztormem Charles i bedzie pierwszym oficjalnym wystepem kobiecego Arsenalu na Camp Nou. Liderujaca Barcelona ma komplet 9 punktow przy 19 strzelonych golach (oraz ligowe 7:0 z Realem Madryt) przeciwko Alessii Russo i Arsenalowi (7 pkt).",
                "Dzien wczesniej OL Lyonnes rozbilo Juventus Women 6:0 w Bielli po dwoch golach Marie-Antoinette Katoto (31', 35') oraz trafieniach Melchie Dumornay (40'), Lily Yohannes (80'), Korbin Albert (85') i Wendie Renard (90+1'), a OH Leuven zremisowalo z HB Koge 1:1. W Lidze Narodow dzis: Anglia-Chorwacja na Wembley, Wlochy-Francja na San Siro, Czechy-Hiszpania i Turcja-Belgia."
            ]
        },
        "zh": {
            "title": "诺坎普焦点夜：里昂6-0大胜尤文后，巴萨女足今晚迎战阿森纳重演2025决赛",
            "subtitle": "阿森纳女足首次在诺坎普出战正式比赛，同晚欧国联英格兰在温布利迎战克罗地亚。",
            "excerpt": "因风暴查尔斯推迟24小时后，三战全胜的巴萨（9分）将在诺坎普对阵阿森纳（7分），前一夜里昂6-0轻取尤文。",
            "body": [
                "11月12日周四晚欧洲足坛好戏连台，核心战役为巴塞罗那女足坐镇诺坎普迎战阿森纳女足（中欧时间18:45），重演2025年里斯本决赛对决。受风暴查尔斯预警影响推迟一天后，这也是阿森纳女足队史首次在诺坎普参加正式比赛。巴萨前3轮全胜积9分并轰入19球（联赛还曾7-0大胜皇马），邦马蒂与普特利亚斯将直面鲁索领衔的阿森纳（7分）。",
                "就在昨晚的周三比赛日，里昂女足在比耶拉6-0大胜尤文图斯，卡托托4分钟内连下两城（第31、35分钟），迪莫奈（40'）、约翰内斯（80'）、阿尔贝特（85'）和勒纳尔（90+1'）相继破门；同日鲁汶1-1战平克厄。男足欧国联今晚同时打响：英格兰在温布利迎战克罗地亚（打平即可出线），意大利对法国，捷克对西班牙，土耳其对比利时。"
            ]
        },
        "ja": {
            "title": "カンプ・ノウ決戦：リヨンがユベントスに6-0大勝の翌日、バルセロナ対アーセナルが今夜激突",
            "subtitle": "アーセナル女子はカンプ・ノウ初の公式戦。2025年決勝の再戦に加え、今夜はネーションズリーグでイングランド対クロアチアも開催。",
            "excerpt": "嵐チャールズの影響で24時間順延された一戦で3戦全勝のバルサ（勝ち点9）とアーセナル（同7）が対戦。前夜はOLリヨンが6-0勝利。",
            "body": [
                "11月12日木曜夜の欧州サッカー最大の注目は、スポティファイ・カンプ・ノウで行われるFCバルセロナ対アーセナル（18:45 CET）の女子CL第4節だ。嵐チャールズの警報により1日順延されたこの試合は、アーセナル女子にとってカンプ・ノウでの記念すべき初の公式戦となる。開幕3連勝で19得点を奪うバルサはボンマティとプテージャスを擁し、アレッシア・ルッソら勝ち点7のアーセナルを迎える。",
                "水曜日の試合ではOLリヨンがビエッラでユベントスに6-0と圧勝。カトトの連続ゴール（31分、35分）に続き、デュモルネ（40分）、ヨハネス（80分）、アルバート（85分）、ルナール（90+1分）が得点し、OHルーヴェン対HBキューゲは1-1で引き分けた。男子UEFAネーションズリーグも今夜開催され、イングランド対クロアチア（ウェンブリー）、イタリア対フランス、チェコ対スペインなどが組まれている。"
            ]
        },
        "ko": {
            "title": "캄프 누 빅매치: 리옹의 유벤투스전 6-0 대승 이어 오늘 밤 바르셀로나 vs 아스널 격돌",
            "subtitle": "아스널 위민이 캄프 누에서 치르는 사상 첫 공식전이자 2025 결승 리매치, 같은 날 잉글랜드 vs 크로아티아도 웸블리에서 열립니다.",
            "excerpt": "폭풍 찰스 여파로 하루 연기된 UWCL 4차전에서 3전 전승 바르셀로나(승점 9)가 아스널(승점 7)을 홈으로 불러들입니다.",
            "body": [
                "11월 12일 목요일 밤 유럽 축구의 하이라이트는 스포티파이 캄프 누에서 열리는 FC 바르셀로나 페메니와 아스널 위민의 UEFA 여자 챔피언스리그 4차전(18:45 CET)입니다. 폭풍 찰스 경보로 24시간 연기된 이날 경기는 2025 리스본 결승 리매치이자 아스널 여자팀의 사상 첫 캄프 누 공식전입니다. 3경기 19골 3연승을 달리는 바르셀로나(본마티, 푸테야스)가 알레시아 루소의 아스널(승점 7)을 맞습니다.",
                "전날 수요일 경기에서는 OL 리옹이 비엘라 원정에서 유벤투스를 6-0으로 대파했습니다. 카토토가 4분 만에 멀티골(31', 35')을 넣은 뒤 뒤모르네(40'), 요하네스(80'), 알베르트(85'), 르나르(90+1')가 득점했고, OH 뢰번과 HB 코게는 1-1로 비겼습니다. 남자 네이션스리그에서는 오늘 밤 잉글랜드-크로아티아(웸블리), 이탈리아-프랑스(산 시로), 체코-스페인, 튀르키예-벨기에가 펼쳐집니다."
            ]
        },
        "ar": {
            "title": "قمة كامب نو الليلة: برشلونة يستضيف أرسنال بعد فوز أولمبيك ليون 6-0 على يوفنتوس",
            "subtitle": "أرسنال للسيدات يخوض أول مباراة رسمية في سبوتيفاي كامب نو في إعادة لنهائي 2025 بالتزامن مع إنجلترا ضد كرواتيا.",
            "excerpt": "بعد تأجيلها 24 ساعة بسبب العاصفة تشارلز، يلتقي المتصدر برشلونة (9 نقاط) مع أرسنال (7 نقاط) عقب اكتساح ليون ليوفنتوس بسداسية نظيفة.",
            "body": [
                "تتجه أنظار الكرة الأوروبية مساء الخميس 12 نوفمبر نحو ملعب سبوتيفاي كامب نو حيث يستضيف برشلونة للسيدات فريق أرسنال في الجولة الرابعة من دوري أبطال أوروبا للسيدات (18:45 بتوقيت وسط أوروبا)، في إعادة لنهائي لشبونة 2025 وأول ظهور رسمي لسيدات أرسنال في كامب نو. يدخل برشلونة بالعلامة الكاملة (9 نقاط و19 هدفاً) بقيادة أيتانا بونماتي وأليكسيا بوتياس أمام أليسيا روسو وأرسنال (7 نقاط).",
                "وكانت مباريات الأربعاء قد شهدت انتصاراً عريضاً لأولمبيك ليون على يوفنتوس بنتيجة 6-0 في بييلا بثنائية كاتوتو (31 و35) وأهداف دومورناي ويوهانس وألبرت ورينارد، فيما تعادل لوفين وكوغه 1-1. وفي دوري الأمم الأوروبية الليلة، تلعب إنجلترا مع كرواتيا في ويمبلي وإيطاليا مع فرنسا في سان سيرو والتشيك مع إسبانيا وتركيا مع بلجيكا."
            ]
        }
    },
    "nfl-week10-tnf-tonight-daniels-mccarthy-giants-commanders-2026": {
        "fr": {
            "title": "NFL TNF ce soir : les deux QB aptes, les Giants (5-2-1) recoivent Washington prive de Lucas Patrick",
            "subtitle": "Jayden Daniels n'a plus aucune mention de blessure face a J.J. McCarthy pour le White Out cinq semaines apres le nul 27-27.",
            "excerpt": "Washington retrouve Jayden Daniels pleinement apte ce soir au MetLife Stadium mais perd son centre titulaire Lucas Patrick et Colson Yankoff contre New York.",
            "body": [
                "Les deux jeunes quarterbacks auront le feu vert ce jeudi soir 12 novembre (20h15 ET sur Prime Video) pour l'ouverture de la Semaine 10 au MetLife Stadium. Jayden Daniels (coude gauche) s'est entraine normalement et ne figure plus sur le rapport des blesses de Washington avant ces retrouvailles apres le nul 27-27 en prolongation de la Semaine 5.",
                "Malgre le retour de Daniels, les Commanders (2-5-1) abordent le choc affaiblis devant : le centre titulaire Lucas Patrick (commotion, remplace par Nick Allegretti) et l'ailier rapproche Colson Yankoff (genou) sont forfait, tandis que Treylon Burks (pied) devrait jouer.",
                "En face, les Giants de John Harbaugh (5-2-1, leaders de la NFC Est apres le succes 19-11 a Philadelphie) retrouvent un groupe offensif au complet : J.J. McCarthy (hanche), Cam Skattebo (ischios), Malik Nabers (genou), Andrew Thomas et Theo Johnson sont tous aptes pour le Vintage White Out."
            ]
        },
        "es": {
            "title": "NFL TNF hoy: ambos QB listos para el duelo entre Giants (5-2-1) y Commanders sin Lucas Patrick",
            "subtitle": "Jayden Daniels queda libre de parte medico frente a J.J. McCarthy en el White Out del MetLife Stadium cinco semanas despues del 27-27.",
            "excerpt": "Washington recupera sin restricciones a Jayden Daniels para esta noche en Nueva York, pero pierde por lesion al centro titular Lucas Patrick y a Colson Yankoff.",
            "body": [
                "Los dos mariscales de campo tienen luz verde esta noche de jueves 12 de noviembre (20:15 ET en Prime Video) para abrir la Semana 10 de la NFL en el MetLife Stadium. Jayden Daniels entreno al completo del codo izquierdo y no arrastra designacion de lesion para repetir un clasico que en la Semana 5 termino 27-27 en prorroga.",
                "Aun con Daniels listo, los Commanders (2-5-1) sufren bajas sensibles: el centro titular Lucas Patrick (conmocion, entra Nick Allegretti) y el ala cerrada Colson Yankoff (rodilla) son baja oficial, mientras que Treylon Burks (pie) apunta a jugar.",
                "Por Nueva York, los lideres del Este de la NFC (5-2-1 tras ganar 19-11 en Filadelfia) cuentan con sus principales armas sin designacion medica: J.J. McCarthy (cadera), Cam Skattebo, Malik Nabers, Andrew Thomas y Theo Johnson encaran el Vintage White Out listos para jugar."
            ]
        },
        "de": {
            "title": "NFL TNF heute Nacht: Beide QBs fit, Giants (5-2-1) empfangen Commanders ohne Lucas Patrick",
            "subtitle": "Jayden Daniels geht ohne Verletzungsstatus gegen J.J. McCarthy ins MetLife White Out, fuenf Wochen nach dem 27:27-Remis.",
            "excerpt": "Washington meldet Jayden Daniels rechtzeitig fuer Donnerstagabend einsatzbereit, muss bei den 5-2-1 Giants jedoch auf Center Lucas Patrick verzichten.",
            "body": [
                "Beide jungen Quarterbacks erhalten gruenes Licht fuer den Auftakt von NFL-Woche 10 heute Nacht (20:15 Uhr ET, Prime Video) im MetLife Stadium. Washingtons Jayden Daniels trainierte nach seiner Ellbogenverletzung voll mit und traegt keinen Verletzungsstatus vor der Neuauflage des 27:27 nach Verlaengerung aus Woche 5.",
                "Trotzdem reisen die Commanders (2-5-1) mit Ausfaellen in East Rutherford an: Stamm-Center Lucas Patrick (Gehirnerschuetterung, Nick Allegretti startet) und Tight End Colson Yankoff (Knie) fallen aus; Receiver Treylon Burks (Fuss) soll spielen.",
                "Bei den fuehrenden New York Giants (5-2-1 nach dem 19:11 in Philadelphia) stehen J.J. McCarthy, Cam Skattebo, Malik Nabers, Andrew Thomas und Theo Johnson voll zur Verfuegung."
            ]
        },
        "it": {
            "title": "NFL TNF stasera: entrambi i QB abili, Giants (5-2-1) ospitano i Commanders senza Lucas Patrick",
            "subtitle": "Jayden Daniels e libero da designazioni contro J.J. McCarthy nel White Out del MetLife cinque settimane dopo il 27-27.",
            "excerpt": "Washington ritrova Jayden Daniels senza restrizioni per la sfida di stanotte, ma perde il centro titolare Lucas Patrick e Colson Yankoff contro New York.",
            "body": [
                "Entrambi i quarterback giovani hanno luce verde per il Thursday Night Football di Week 10 stanotte (20:15 ET su Prime Video). Jayden Daniels si e allenato a pieno regime sul gomito sinistro e non ha nessuna designazione di infortunio prima della rivincita del 27-27 ai supplementari di Week 5.",
                "Washington (2-5-1) paga pero assenze pesanti in linea: il centro titolare Lucas Patrick (commozione cerebrale, gioca Nick Allegretti) e il tight end Colson Yankoff (ginocchio) sono ufficialmente OUT, mentre Treylon Burks dovrebbe esserci.",
                "In casa New York Giants (5-2-1 in testa alla NFC East dopo il 19-11 a Philadelphia), J.J. McCarthy, Cam Skattebo, Malik Nabers, Andrew Thomas e Theo Johnson sono tutti completamente abili per il Vintage White Out."
            ]
        },
        "pl": {
            "title": "NFL TNF dzis w nocy: obaj rozgrywajacy zdrowi, Giants (5-2-1) podejmuja Commanders bez Lucasa Patricka",
            "subtitle": "Jayden Daniels bez oznaczenia kontuzji przed starciem z J.J. McCarthym na MetLife piec tygodni po remisie 27:27.",
            "excerpt": "Washington odzyskuje Jaydena Danielsa na czwartkowy hit w East Rutherford, lecz przeciwko Giants zabraknie centra Lucasa Patricka i Colsona Yankoffa.",
            "body": [
                "Obaj mlodzi rozgrywajacy otrzymali zielone swiatlo na otwarcie 10. tygodnia NFL dzisiaj w nocy (20:15 ET, Prime Video) na MetLife Stadium. Jayden Daniels trenowal z pelnym obciazeniem po urazie lewego lokcia i nie widnieje juz z zadnym statusem kontuzji przed rewanzem za remis 27:27 po dogrywce.",
                "Mimo powrotu Danielsa Commanders (2-5-1) traca kluczowych graczy: srodkowy Lucas Patrick (wstrzasnienie mozgu, zastapi go Nick Allegretti) i Colson Yankoff (kolano) sa wykluczeni, a Treylon Burks ma zagrac.",
                "U prowadzacych w dywizji Giants (5-2-1 po wygranej 19:11 w Filadelfii) J.J. McCarthy, Cam Skattebo, Malik Nabers, Andrew Thomas oraz Theo Johnson sa gotowi na mecz Vintage White Out."
            ]
        },
        "zh": {
            "title": "NFL周四夜赛前瞻：两位四分卫双双获准出战，巨人（5-2-1）主场迎战缺少中锋的指挥官",
            "subtitle": "第5周27-27战平五周后，杰登·丹尼尔斯摆脱伤病标签，将在大都会球场直面J.J.麦卡锡。",
            "excerpt": "指挥官四分卫杰登·丹尼尔斯今夜完全恢复出战，但主力中锋卢卡斯·帕特里克和近端锋扬科夫缺席客战5胜2负1平巨人的比赛。",
            "body": [
                "美东时间11月12日周四晚8点15分，NFL第10周周四夜赛在大都会球场打响，两位年轻四分卫双双获准登场。华盛顿指挥官四分卫杰登·丹尼尔斯左手肘全程参加训练且已移除伤病名单，重演第5周加时27-27激战后的二番战。",
                "不过指挥官（2胜5负1平）前线受损，主力中锋卢卡斯·帕特里克因脑震荡确认缺阵（由尼克·阿莱格雷蒂顶替），近端锋科尔森·扬科夫同样休战，外接手伯克斯预计带伤出场。",
                "主场作战的纽约巨人（5胜2负1平，上轮刚在费城19-11取胜）主力进攻组全员健康：J.J.麦卡锡、跑卫斯卡特博、外接手马利克·纳伯斯以及左截锋安德鲁·托马斯均无伤病限制，将身披复古全白战袍迎战。"
            ]
        },
        "ja": {
            "title": "NFL TNF今夜開催：両QBが出場可能に、ジャイアンツ（5-2-1）がセンター欠くコマンダース迎撃",
            "subtitle": "第5週の27-27引き分けから5週間後、ジェイデン・ダニエルズとJ.J.マッカーシーがメッツライフのホワイトアウトで激突。",
            "excerpt": "ワシントンはQBジェイデン・ダニエルズが負傷表記なしで復帰する一方、先発センターのルーカス・パトリックとTEヤンコフが欠場となる。",
            "body": [
                "現地11月12日木曜20時15分開始のNFL第10週サーズデーナイトは、両チームの若き司令塔に青信号が灯った。ワシントンQBジェイデン・ダニエルズは左肘の回復を経てフル練習をこなし負傷ステータスなしとなり、第5週27-27の延長引き分け以来となる再戦に臨む。",
                "それでもコマンダース（2勝5敗1分）は脳震盪の先発Cルーカス・パトリック（ニック・アレグレッティが代役）とTEコルソン・ヤンコフが欠場確定で、WRトレロン・バークスは出場見込み。",
                "対するNFC東地区首位ジャイアンツ（5勝2敗1分）はJ.J.マッカーシー、カム・スカッテボ、マリク・ネイバーズ、アンドリュー・トーマスらが負傷表記なしで揃い、ホワイトアウトのホームに迎える。"
            ]
        },
        "ko": {
            "title": "NFL 목요일 야간경기 프리뷰: 두 QB 모두 출전 청신호… 자이언츠(5-2-1), 주전 센터 빠진 커맨더스 격돌",
            "subtitle": "5주차 27-27 무승부 이후 5주 만에 제이든 대니얼스와 J.J. 맥카시가 메트라이프 화이트 아웃 경기에서 맞붙습니다.",
            "excerpt": "워싱턴은 QB 제이든 대니얼스가 부상 명단에서 빠지며 출전 준비를 마쳤으나 주전 센터 루카스 패트릭과 TE 얀코프가 결장합니다.",
            "body": [
                "현지시간 11월 12일 밤 8시 15분(ET) 킥오프하는 NFL 10주차 TNF에서 양 팀 주전 쿼터백이 모두 출전 허가를 받았습니다. 워싱턴 QB 제이든 대니얼스는 왼쪽 팔꿈치 훈련을 정상 소화하며 5주차 27-27 연장 무승부의 재대결에 부상 표기 없이 나섭니다.",
                "다만 2승 5패 1무의 커맨더스는 주전 센터 루카스 패트릭(뇌진탕, 닉 알레그레티 대체)과 TE 콜슨 얀코프가 결장하며, WR 트레일런 버크스는 출전이 예상됩니다.",
                "지난주 필라델피아 원정 19-11 승리 포함 5승 2패 1무로 지구 선두를 지키는 자이언츠는 J.J. 맥카시, 캠 스카테보, 말릭 네이버스, 앤드루 토머스가 모두 정상 출전 명단에 이름을 올렸습니다."
            ]
        },
        "ar": {
            "title": "الليلة في NFL: جاهزية دانيالز وماكارثي، والعمالقة (5-2-1) يستضيفون واشنطن دون مركزه الأساسي",
            "subtitle": "جايدن دانيالز يتعافى بالكامل قبل مواجهة جي جي ماكارثي في ليلة وايت أوت بعد تعادل الأسبوع الخامس 27-27.",
            "excerpt": "يدخل واشنطن لقاء الليلة بمشاركة كاملة لجايدن دانيالز لكنه يفتقد المركز الأساسي لوكاس باتريك وكولسون يانكوف أمام نيويورك المتصدر.",
            "body": [
                "يستقبل ملعب ميتلايف الليلة في تمام 8:15 مساءً بتوقيت الساحل الشرقي افتتاح الأسبوع العاشر من دوري NFL، بعودة جايدن دانيالز لقيادة هجوم واشنطن دون أي تصنيف للإصابة عقب تعافيه في المرفق الأيسر، في مواجهة مكررة بعد تعادل الفريقين 27-27 في الأسبوع الخامس.",
                "ورغم جاهزية دانيالز، يفتقد فريق كوماندرز (2-5-1) خدمات لاعب الارتكاز الأساسي لوكاس باتريك بداعي الارتجاج والمهاجم كولسون يانكوف، بينما يُتوقع مشاركة تريلون بيركس.",
                "في المقابل يعتمد نيويورك جاينتس متصدر القسم (5-2-1) على جاهزية كاملة لجي جي ماكارثي وكام سكاتيبو وماليك نابرز وأندرو توماس تحت الأضواء البيضاء الكلاسيكية."
            ]
        }
    },
    "nba-harden-32-cavs-knicks-rockets-beat-warriors-curry-injury-2026": {
        "fr": {
            "title": "NBA : Harden plante 32 points au MSG avec Cleveland, Houston domine Golden State apres la sortie de Curry",
            "subtitle": "Sengun, Smith Jr. et Sheppard offrent le succes 115-108 aux Rockets apres la blessure precoce de Curry ; Boston remonte -22 a Toronto (98-93).",
            "excerpt": "Les Cavaliers dominent New York 115-107 grace aux 32 points de James Harden, tandis que Golden State perd Stephen Curry des le premier quart-temps a Houston.",
            "body": [
                "La double affiche ESPN de mercredi 11 novembre a combine un recital offensif a New York et une alerte blessure a Houston. Au Madison Square Garden, James Harden a inscrit 32 points (dont cinq tirs a trois points) avec 23 points de Donovan Mitchell pour offrir aux Cleveland Cavaliers une victoire 115-107 face aux Knicks de Jalen Brunson (27 pts) et Karl-Anthony Towns (21).",
                "Plus tard au Toyota Center, Golden State a perdu Stephen Curry des le premier quart-temps sur blessure apres trois points inscrits, et les Houston Rockets ont su en profiter pour s'imposer 115-108. Alperen Sengun (19 pts), Jabari Smith Jr. (14) et Reed Sheppard (13) ont surmonte les 25 points de Yaxel Lendeborg et les 22 de Brandin Podziemski.",
                "Ailleurs mercredi, Boston a efface un retard de 22 points a Toronto grace aux 24 points de Jayson Tatum (98-93). Ce jeudi propose quatre affiches : Raptors a Philadelphie, Pistons a Washington, Mavericks a Minnesota et Hornets a Phoenix."
            ]
        },
        "es": {
            "title": "NBA: Harden firma 32 puntos en el MSG con Cleveland y Houston vence 115-108 tras la lesion temprana de Curry",
            "subtitle": "Sengun, Smith Jr. y Sheppard lideran a los Rockets tras la salida de Curry en el primer cuarto; Boston remonta 22 puntos en Toronto (98-93).",
            "excerpt": "Los Cavaliers superan 115-107 a los Knicks con 32 puntos de Harden, mientras Stephen Curry deja el parquet en el primer periodo en Houston.",
            "body": [
                "La doble cartelera de ESPN del miercoles 11 de noviembre dejo exhibicion en Nueva York y preocupacion en Houston. En el Madison Square Garden, James Harden anoto 32 puntos con cinco triples junto a los 23 tantos de Donovan Mitchell para impulsar el 115-107 de los Cleveland Cavaliers sobre los Knicks de Jalen Brunson (27) y Karl-Anthony Towns (21).",
                "Despues en el Toyota Center, Golden State perdio a Stephen Curry en el primer cuarto por lesion tras sumar tres puntos y los Houston Rockets se impusieron 115-108 con Alperen Sengun (19), Jabari Smith Jr. (14) y Reed Sheppard (13), superando los 25 puntos de Yaxel Lendeborg y los 22 de Brandin Podziemski.",
                "En Toronto, los Boston Celtics remontaron 22 puntos de desventaja con 24 tantos de Jayson Tatum para ganar 98-93 antes de los cuatro partidos del jueves: Raptors en 76ers, Pistons en Wizards, Mavericks en Timberwolves y Hornets en Suns."
            ]
        },
        "de": {
            "title": "NBA: Harden erzielt 32 im MSG fuer Cavs-Sieg; Houston bezwingt Warriors nach frueher Curry-Verletzung",
            "subtitle": "Sengun, Smith Jr. und Sheppard sichern Rockets ein 115:108 nach Currys Aus im 1. Viertel; Boston holt in Toronto -22 auf (98:93).",
            "excerpt": "Cleveland gewinnt 115:107 bei den Knicks durch 32 Punkte von James Harden, waehrend Stephen Curry bei den Warriors frueh ausfaellt.",
            "body": [
                "Der ESPN-Doppelspieltag vom 11. November bot in New York eine Gala und in Houston Verletzungssorgen. Im Madison Square Garden schenkte James Harden den Knicks 32 Punkte (fuenf Dreier) ein und fuehrte Cleveland gemeinsam mit Donovan Mitchell (23) zum 115:107-Auswaertssieg gegen Jalen Brunson (27) und Karl-Anthony Towns (21).",
                "Spaeter verlor Golden State Superstar Stephen Curry bereits im ersten Viertel verletzt (3 Punkte), was die Houston Rockets zum 115:108-Heimsieg durch Alperen Sengun (19), Jabari Smith Jr. (14) und Reed Sheppard (13) nutzten, trotz starker 25 Punkte von Yaxel Lendeborg und 22 von Brandin Podziemski.",
                "Zudem drehte Boston in Toronto einen 22-Punkte-Rueckstand durch 24 Punkte von Jayson Tatum zum 98:93. Heute stehen vier Partien an: TOR@PHI, DET@WAS, DAL@MIN und CHA@PHX."
            ]
        },
        "it": {
            "title": "NBA: Harden ne fa 32 al MSG nel colpo Cavs; Houston batte Golden State dopo l'infortunio di Curry",
            "subtitle": "Sengun, Smith Jr. e Sheppard firmano il 115-108 Rockets dopo lo stop di Curry nel 1Q; Celtics da -22 a 98-93 contro Toronto.",
            "excerpt": "Cleveland passa 115-107 sui Knicks con 32 punti di Harden, mentre i Warriors perdono Stephen Curry nel primo quarto a Houston.",
            "body": [
                "Il mercoledi NBA su ESPN dell'11 novembre ha regalato scintille al Madison Square Garden e apprensione a Houston. James Harden ha segnato 32 punti con cinque triple e Donovan Mitchell ne ha aggiunti 23 nel successo per 115-107 dei Cleveland Cavaliers sui New York Knicks di Jalen Brunson (27) e Karl-Anthony Towns (21).",
                "Al Toyota Center i Golden State Warriors hanno perso Stephen Curry gia nel primo quarto per infortunio (3 punti) e gli Houston Rockets hanno vinto 115-108 grazie ad Alperen Sengun (19), Jabari Smith Jr. (14) e Reed Sheppard (13), rendendo vani i 25 punti di Yaxel Lendeborg e i 22 di Brandin Podziemski.",
                "A Toronto Boston ha cancellato 22 punti di svantaggio vincendo 98-93 con 24 punti di Jayson Tatum. Stanotte quattro gare in programma: TOR@PHI, DET@WAS, DAL@MIN e CHA@PHX."
            ]
        },
        "pl": {
            "title": "NBA: 32 punkty Hardena w MSG dla Cavs, Rockets pokonuja Warriors po wczesnej kontuzji Curry'ego",
            "subtitle": "Sengun, Smith Jr. i Sheppard prowadza Houston do 115:108 po zejsciu Curry'ego w 1. kwarcie; Boston odrabia 22 punkty w Toronto.",
            "excerpt": "Cleveland wygrywa 115:107 z Knicks po 32 punktach Jamesa Hardena, a Golden State traci Stephena Curry'ego juz na poczatku meczu w Teksasie.",
            "body": [
                "Srodowe mecze ESPN przyniosly 11 listopada wielki wystep w Nowym Jorku i niepokojace wiesci z Houston. W Madison Square Garden James Harden trafil piec trojek i zdobyl 32 punkty, a Donovan Mitchell dolozyl 23 w wygranej Cleveland Cavaliers 115:107 nad Knicks (Jalen Brunson 27, Karl-Anthony Towns 21).",
                "W Toyota Center Golden State stracilo Stephena Curry'ego z powodu kontuzji juz w pierwszej kwarcie (3 pkt), co wykorzystali Houston Rockets zwyciezajac 115:108 za sprawa Alperena Senguna (19), Jabariego Smitha Jr. (14) i Reeda Shepparda (13) mimo 25 oczek Yaxela Lendeborga.",
                "Wczesniej Boston Celtics odrobili w Toronto az 22 punkty straty i wygrali 98:93 po 24 punktach Jaysona Tatuma przed czwartkowymi czterema spotkaniami."
            ]
        },
        "zh": {
            "title": "NBA战报：哈登32分率骑士客胜尼克斯，火箭115-108力克库里首节伤退的勇士",
            "subtitle": "申京、史密斯和谢泼德合砍46分拿下勇士，凯尔特人客场22分大逆转98-93险胜猛龙。",
            "excerpt": "詹姆斯·哈登轰下32分助骑士115-107击退尼克斯，勇士当家球星斯蒂芬·库里首节因伤早退后以115-108负于火箭。",
            "body": [
                "11月11日周三ESPN两场全美直播激战正酣。在麦迪逊广场花园，詹姆斯·哈登命中5记三分砍下全场最高32分，携手多诺万·米切尔的23分率克利夫兰骑士115-107客场拿下纽约尼克斯，布伦森27分、唐斯21分难阻失利。",
                "随后的休斯顿之战令人揪心，斯蒂芬·库里首节仅得3分便因伤提前退场，休斯顿火箭多点开花以115-108赢下比赛，阿尔佩伦·申京19分、小贾巴里·史密斯14分、里德·谢泼德13分，勇士方面伦德博格25分、波杰姆斯基22分。",
                "同日波士顿凯尔特人在多伦多一度落后22分的情况下完成逆转，杰森·塔图姆独得24分带队98-93取胜。周四共有四场NBA对决：猛龙对76人、活塞对奇才、独行侠对森林狼、黄蜂对太阳。"
            ]
        },
        "ja": {
            "title": "NBA：ハーデン32得点でキャブズがMSG勝利、ロケッツはカリー負傷退場のウォリアーズを下す",
            "subtitle": "シェングンらバランスの攻撃でヒューストンが115-108、セルティックスは22点差大逆転でラプターズに98-93勝利。",
            "excerpt": "クリーブランドがハーデンの32得点でニックスに115-107で勝利。ゴールデンステイトはカリーが第1Qに負傷交代し108-115で敗れた。",
            "body": [
                "11月11日水曜のESPN全米中継はニューヨークの得点ショーとヒューストンの負傷アクシデントが対照的だった。マディソン・スクエア・ガーデンでジェームズ・ハーデンが5本の3ポイントを含むゲーム最多32得点、ドノバン・ミッチェルが23得点を挙げ、キャバリアーズがブランソン（27点）とタウンズ（21点）のニックスを115-107で破った。",
                "続くトヨタ・センターではステフィン・カリーが第1Q序盤（3得点）に負傷退場。ヒューストン・ロケッツはアルペレン・シェングン19点、ジャバリ・スミスJr.14点、リード・シェパード13点とバランス良く加点し115-108で勝利した（レンデボーグ25点、ポジェムスキー22点）。",
                "またトロントではセルティックスが22点差をひっくり返しテイタムの24得点で98-93の逆転勝利。木曜は全4試合が予定されている。"
            ]
        },
        "ko": {
            "title": "NBA: 하든 MSG서 32점 폭발하며 닉스 격파, 로케츠는 커리 1쿼터 부상 악재 겹친 워리어스 제압",
            "subtitle": "센군·스미스 주니어·셰퍼드의 고른 활약으로 휴스턴 115-108 승리, 보스턴은 토론토전 22점 차 뒤집기 98-93 승.",
            "excerpt": "클리블랜드가 제임스 하든의 32점에 힘입어 뉴욕을 115-107로 눌렀고, 골든스테이트는 커리 조기 부상 속에 108-115로 졌습니다.",
            "body": [
                "11월 11일 수요일 밤 ESPN 중계는 뉴욕의 화력전과 휴스턴의 부상 변수로 엇갈렸습니다. 매디슨 스퀘어 가든에서 제임스 하든이 3점슛 5개 포함 32득점, 도노반 미첼이 23득점을 올린 클리블랜드 캐벌리어스가 제일런 브런슨(27점)과 칼-앤서니 타운스(21점)의 뉴욕 닉스를 115-107로 제압했습니다.",
                "이어진 도요타 센터 경기에서는 스테판 커리가 1쿼터 도중 3득점만 남긴 채 부상으로 이탈했고, 휴스턴 로케츠가 알페렌 센군(19점), 자바리 스미스 주니어(14점), 리드 셰퍼드(13점)를 앞세워 115-108로 승리했습니다(렌데보그 25점, 포지엠스키 22점).",
                "보스턴 셀틱스는 제이슨 테이텀의 24득점에 힘입어 토론토 원정에서 22점 차 열세를 뒤집고 98-93으로 이겼습니다. 목요일에는 4경기가 열립니다."
            ]
        },
        "ar": {
            "title": "NBA: هاردن يسجل 32 نقطة في نيويورك ويقود كليفلاند، وهيوستن يهزم ووريورز بعد إصابة مبكرة لكوري",
            "subtitle": "سينغون وسميث جونيور وشيبرد يمنحون روكتس الفوز 115-108 بعد خروج ستيفن كوري، وبوسطن يعود من تأخر 22 نقطة أمام تورونتو.",
            "excerpt": "كافالييرز يتغلب على نيكس 115-107 بـ32 نقطة لهاردن، بينما يفقد غولدن ستيت نجمه كوري في الربع الأول ويخسر في هيوستن.",
            "body": [
                "شهدت سهرة الأربعاء 11 نوفمبر تألقاً هجومياً في ماديسون سكوير غاردن وقلقاً على الإصابات في هيوستن. فقد أحرز جيمس هاردن 32 نقطة بينها خمس ثلاثيات وأضاف دونوفان ميتشل 23 نقطة ليقودا كليفلاند كافالييرز للفوز على نيويورك نيكس 115-107 رغم 27 نقطة لبرونسون و21 لتاونز.",
                "وفي مركز تويوتا تعرض ستيفن كوري لإصابة أجبرته على الخروج في الربع الأول بعد ثلاث نقاط، ليحسم هيوستن روكتس الفوز 115-108 بتألق ألبيرين سينغون (19 نقطة) وجاباري سميث جونيور (14) وريد شيبرد (13).",
                "كما قلب بوسطن سيلتيكس تأخره بـ22 نقطة في تورونتو ليهزم رابتورز 98-93 بـ24 نقطة لتيتوم، قبل أربع مباريات تقام ليلة الخميس."
            ]
        }
    },
    "atp-nitto-finals-2026-turin-draw-alcaraz-zverev-fritz-rune-stockholm": {
        "fr": {
            "title": "Tirage des Nitto ATP Finals : Zverev et Alcaraz separes a Turin, Fritz retrouve Rune en quart a Stockholm",
            "subtitle": "Le tirage de jeudi repartit les huit qualifies en deux groupes avant dimanche tandis que Fritz et Rune s'affrontent aujourd'hui en Suede.",
            "excerpt": "Alexander Zverev herite de Shelton, Fils et Jodar dans le groupe McEnroe, tandis que Carlos Alcaraz affrontera Medvedev, Cobolli et Tiafoe.",
            "body": [
                "Les deux poules des Nitto ATP Finals 2026 ont ete officiellement devoilees ce jeudi a Turin avant le coup d'envoi de dimanche (15-22 novembre) a l'Inalpi Arena. Tete de serie n.1, Alexander Zverev menera le groupe John McEnroe aux cotes de Ben Shelton (3), Arthur Fils (6) et Rafael Jodar (8).",
                "Dans le groupe Ivan Lendl, le vainqueur de Paris Carlos Alcaraz (2) fera face a Daniil Medvedev (4), au joueur local Flavio Cobolli (5) et a Frances Tiafoe (7), promettant un choc de styles intense en salle.",
                "Plus au nord a Stockholm ce jeudi, les quarts de finale opposent Taylor Fritz a Holger Rune sur le Court Central apres leurs succes de mercredi : Fritz a domine Cameron Norrie 7-5, 6-3 et Rune a renverse Miomir Kecmanovic 2-6, 6-1, 6-4."
            ]
        },
        "es": {
            "title": "Sorteo Nitto ATP Finals: Zverev lidera el Grupo McEnroe y Alcaraz el Lendl; hoy Fritz-Rune en Estocolmo",
            "subtitle": "Turin divide a los ocho maestros antes del domingo mientras Taylor Fritz y Holger Rune chocan en cuartos en Suecia.",
            "excerpt": "Alexander Zverev se medira a Shelton, Fils y Jodar en Turin, mientras Carlos Alcaraz encabezara su grupo ante Medvedev, Cobolli y Tiafoe.",
            "body": [
                "El cuadro de las Nitto ATP Finals 2026 quedo definido este jueves en Turin antes del inicio el domingo (15-22 de noviembre) en el Inalpi Arena. El primer favorito Alexander Zverev encabeza el Grupo John McEnroe junto a Ben Shelton (3), Arthur Fils (6) y Rafael Jodar (8).",
                "En el Grupo Ivan Lendl, el reciente campeon de Paris Carlos Alcaraz (2) compartira zona con Daniil Medvedev (4), el italiano Flavio Cobolli (5) y Frances Tiafoe (7).",
                "En paralelo en Estocolmo, los cuartos de final miden hoy a Taylor Fritz y Holger Rune tras ganar el miercoles: Fritz supero 7-5, 6-3 a Cameron Norrie y Rune remonto 2-6, 6-1, 6-4 ante Miomir Kecmanovic."
            ]
        },
        "de": {
            "title": "Nitto ATP Finals Auslosung: Zverev fuehrt McEnroe-Gruppe gegen Alcaraz' Lendl-Gruppe an; Fritz vs. Rune in Stockholm",
            "subtitle": "Turin teilt die besten Acht vor dem Sonntag-Auftakt ein, waehrend sich Fritz und Rune heute im Viertelfinale in Schweden duellieren.",
            "excerpt": "Alexander Zverev trifft in Turin auf Shelton, Fils und Jodar; Carlos Alcaraz bekommt es mit Medvedev, Cobolli und Tiafoe zu tun.",
            "body": [
                "Die Gruppen der Nitto ATP Finals 2026 in Turin (15.-22. November) wurden am Donnerstag ausgelost. Topfavorit Alexander Zverev trifft in der John-McEnroe-Gruppe auf Ben Shelton (3), Arthur Fils (6) und Rafael Jodar (8).",
                "In der Ivan-Lendl-Gruppe wartet Paris-Champion Carlos Alcaraz (2) auf Daniil Medvedev (4), Lokalmatador Flavio Cobolli (5) und Frances Tiafoe (7).",
                "In Stockholm steht heute das Viertelfinale zwischen Taylor Fritz und Holger Rune an: Fritz schlug am Mittwoch Cameron Norrie 7:5, 6:3, waehrend Rune Miomir Kecmanovic 2:6, 6:1, 6:4 niederrang."
            ]
        },
        "it": {
            "title": "Sorteggio Nitto ATP Finals: Zverev nel Gruppo McEnroe, Alcaraz guida il Lendl con Cobolli; Fritz-Rune a Stoccolma",
            "subtitle": "Giovedi a Torino definiti i due gironi verso domenica mentre Fritz e Rune si sfidano oggi ai quarti in Svezia.",
            "excerpt": "Zverev trova Shelton, Fils e Jodar a Torino, mentre Carlos Alcaraz sfida Daniil Medvedev, l'azzurro Flavio Cobolli e Frances Tiafoe.",
            "body": [
                "Il sorteggio di giovedi a Torino ha definito i due gironi delle Nitto ATP Finals 2026 (15-22 novembre all'Inalpi Arena). La testa di serie numero 1 Alexander Zverev guida il Gruppo John McEnroe insieme a Ben Shelton (3), Arthur Fils (6) e Rafael Jodar (8).",
                "Nel Gruppo Ivan Lendl, il campione di Parigi Carlos Alcaraz (2) pesca Daniil Medvedev (4), la quinta forza azzurra Flavio Cobolli (5) e Frances Tiafoe (7).",
                "A Stoccolma oggi riflettori sul quarto di finale tra Taylor Fritz e Holger Rune: mercoledi Fritz ha battuto Cameron Norrie 7-5, 6-3 e Rune ha rimontato Miomir Kecmanovic 2-6, 6-1, 6-4."
            ]
        },
        "pl": {
            "title": "Losowanie Nitto ATP Finals: Zverev w grupie McEnroe, Alcaraz w Lendl; dzis Fritz kontra Rune w Sztokholmie",
            "subtitle": "Czwartkowa ceremonia w Turynie podzielila osemke finalistow przed niedziela, a w Szwecji hitowy cwiercfinal.",
            "excerpt": "Alexander Zverev zagra w Turynie z Sheltonem, Filsem i Jodarem, a Carlos Alcaraz trafi na Miedwiediewa, Cobollego oraz Tiafoe.",
            "body": [
                "W czwartek w Turynie rozlosowano grupy Nitto ATP Finals 2026 (15-22 listopada w Inalpi Arena). Najwyzej rozstawiony Alexander Zverev trafil do Grupy Johna McEnroe z Benem Sheltonem (3), Arthurem Filsem (6) i Rafaelem Jodarem (8).",
                "W Grupie Ivana Lendla mistrz z Paryza Carlos Alcaraz (2) zmierzy sie z Daniiłem Miedwiediewem (4), Wlochem Flavio Cobollim (5) oraz Francesem Tiafoe (7).",
                "Dzis w Sztokholmie w cwiercfinale Taylor Fritz zagra z Holgerem Rune po srodowych zwyciestwach odpowiednio 7:5, 6:3 nad Cameronem Norriem i 2:6, 6:1, 6:4 nad Miomirem Kecmanoviciem."
            ]
        },
        "zh": {
            "title": "ATP年终总决赛抽签揭晓：兹维列夫与阿尔卡拉斯分领两组，弗里茨斯德哥尔摩八强战鲁内",
            "subtitle": "都灵八强周四正式分组静待周日开拍，瑞典站男单四分之一决赛今日迎来强强对话。",
            "excerpt": "兹维列夫在麦肯罗组迎战谢尔顿、菲斯和霍达尔；阿尔卡拉斯则与梅德韦杰夫、科博利、蒂亚福同组竞技。",
            "body": [
                "2026年Nitto ATP年终总决赛周四在都灵完成抽签，比赛将于11月15日至22日在伊纳尔皮体育馆打响。头号种子亚历山大·兹维列夫领衔约翰·麦肯罗组，同组对手为3号种子本·谢尔顿、6号种子阿图尔·菲斯与8号种子拉斐尔·霍达尔。",
                "伊万·伦德尔组则云集刚夺得巴黎冠军的2号种子卡洛斯·阿尔卡拉斯、4号种子丹尼尔·梅德韦杰夫、本土5号种子弗拉维奥·科博利以及7号种子弗朗西斯·蒂亚福。",
                "与此同时在斯德哥尔摩公开赛，周四中心球场迎来头号种子泰勒·弗里茨与霍尔格·鲁内的八强对决：弗里茨周三以7-5、6-3击败诺里，鲁内则以2-6、6-1、6-4逆转凯茨曼诺维奇。"
            ]
        },
        "ja": {
            "title": "Nitto ATPファイナルズ組み合わせ決定：ズベレフとアルカラスが別組、ストックホルム準々決勝でフリッツ対ルネ",
            "subtitle": "トリノの8選手が日曜開幕へ2グループに確定。スウェーデンでは本日センターコートで強豪対決が実現。",
            "excerpt": "第1シードのズベレフはシェルトン、フィス、ホダールと同組、アルカラスはメドベージェフ、コボッリ、ティアフォーと同組に入った。",
            "body": [
                "2026年Nitto ATPファイナルズのグループ抽選会が木曜日にトリノで行われ、11月15日〜22日のインアルピ・アリーナ決戦の枠組みが確定した。第1シードのアレクサンダー・ズベレフはジョン・マッケンロー・グループに入り、ベン・シェルトン（3）、アルトゥール・フィス（6）、ラファエル・ホダール（8）と対戦する。",
                "反対のイワン・レンドル・グループではパリ王者カルロス・アルカラス（2）がダニール・メドベージェフ（4）、開催国イタリアのフラビオ・コボッリ（5）、フランシス・ティアフォー（7）を迎え撃つ。",
                "一方ストックホルム・オープンでは本日、テイラー・フリッツとホルガー・ルネが準々決勝で激突。水曜の2回戦でフリッツはノリーを7-5、6-3で、ルネはケツマノビッチを2-6、6-1、6-4で退けている。"
            ]
        },
        "ko": {
            "title": "니토 ATP 파이널스 조 추첨 완료: 즈베레프-알카라스 조 분리, 스톡홀름 8강 프리츠 vs 루네 격돌",
            "subtitle": "토리노 파이널스 8인 조 편성이 목요일 확정된 가운데 스웨덴에서는 오늘 센터코트 8강 빅매치가 열립니다.",
            "excerpt": "즈베레프는 셸턴·피스·호다르와 매켄로 조에, 알카라스는 메드베데프·코볼리·티아포와 렌들 조에 각각 편성됐습니다.",
            "body": [
                "11월 15일부터 22일까지 토리노 이날피 아레나에서 열리는 2026 니토 ATP 파이널스 공식 조 추첨이 목요일 완료됐습니다. 1번 시드 알렉산더 즈베레프는 벤 셸턴(3), 아르튀르 피스(6), 라파엘 호다르(8)와 함께 존 매켄로 조에 편성됐습니다.",
                "파리 마스터스 챔피언 카를로스 알카라스(2)는 다닐 메드베데프(4), 홈 기대주 플라비오 코볼리(5), 프랜시스 티아포(7)와 함께 이반 렌들 조에서 4강 진출을 다툽니다.",
                "스톡홀름 오픈에서는 오늘 테일러 프리츠와 홀게르 루네의 8강전이 펼쳐집니다. 수요일 16강에서 프리츠는 카메론 노리를 7-5, 6-3으로, 루네는 미오미르 케츠마노비치를 2-6, 6-1, 6-4로 제압했습니다."
            ]
        },
        "ar": {
            "title": "قرعة نهائيات ATP في تورينو: زفيريف وألكاراز على رأس مجموعتين، وفريتز يواجه رونه اليوم في ستوكهولم",
            "subtitle": "توزيع الثمانية الكبار في إيطاليا قبل انطلاق الأحد بالتوازي مع مواجهة ربع نهائي قوية في السويد.",
            "excerpt": "ألكسندر زفيريف يواجه شيلتون وفيلس وجودار في مجموعة ماكنرو، وكارلوس ألكاراز يصطدم بميدفيديف وكوبولي وتيافو في مجموعة ليندل.",
            "body": [
                "أُجريت الخميس في تورينو قرعة نهائيات Nitto ATP لعام 2026 قبل انطلاق البطولة من 15 إلى 22 نوفمبر على ملعب إنالبي أرينا. ويترأس المصنف الأول ألكسندر زفيريف مجموعة جون ماكنرو إلى جانب بن شيلتون (3) وآرثر فيلس (6) ورافاييل جودار (8).",
                "في مجموعة إيفان ليندل، يلتقي بطل باريس كارلوس ألكاراز (2) مع دانييل ميدفيديف (4) والإيطالي فلافيو كوبولي (5) وفرانسيس تيافو (7).",
                "وفي ربع نهائي بطولة ستوكهولم اليوم، يلتقي تايلور فريتز مع هولغر رونه بعد فوزهما الأربعاء على كاميرون نوري (7-5، 6-3) وميومير كيتسمانوفيتش (2-6، 6-1، 6-4)."
            ]
        }
    },
    "dp-world-tour-championship-2026-luiten-leads-67-mcilroy-69-chacarra-72": {
        "fr": {
            "title": "Dubai T1 : Joost Luiten prend la tete en 67 (-5), Rory McIlroy signe 69 et reprend trois coups a Chacarra",
            "subtitle": "Le 50e et dernier qualifie signe son meilleur tour sur l'Earth Course depuis 2016 devant Jacob Skov Olesen (68) et cinq joueurs a -3.",
            "excerpt": "Joost Luiten mene d'un coup apres 67 (-5), tandis que Rory McIlroy (69, T3) prend deja trois coups d'avance sur Eugenio Chacarra (72, T28).",
            "body": [
                "Entre au 50e et dernier rang dans le champ du DP World Tour Championship, le Neerlandais Joost Luiten a cree la surprise ce jeudi a Dubai en signant une carte de 67 (-5), avec sept birdies pour deux bogeys, son meilleur tour sur l'Earth Course depuis 2016.",
                "Le Danois Jacob Skov Olesen suit a un coup en 68 (-4), devant un groupe de cinq joueurs a -3 emmene par Rory McIlroy (69) avec Victor Perez, Gregorio De Leo, Freddy Schott et Francesco Laporta.",
                "Dans le duel pour la Race to Dubai, McIlroy (3 709,86 pts) a conclu sur un birdie donne au 18 pour prendre d'entree trois coups au leader du classement Eugenio Chacarra (4 243,79 pts), auteur d'un 72 dans le par (T28)."
            ]
        },
        "es": {
            "title": "Dubai R1: Joost Luiten lidera con 67 (-5) mientras Rory McIlroy abre con 69 y recorta tres golpes a Chacarra",
            "subtitle": "El ultimo clasificado al torneo de 50 jugadores firma su mejor ronda en el Earth Course desde 2016 ante Skov Olesen (68).",
            "excerpt": "Joost Luiten comanda en Dubai con 67 (-5) por delante de Jacob Skov Olesen (68), mientras Rory McIlroy (69, T3) supera en tres golpes a Eugenio Chacarra (72).",
            "body": [
                "Joost Luiten accedio como el jugador numero 50 al DP World Tour Championship y salio lider en solitario tras firmar este jueves 67 golpes (-5) con siete birdies y dos bogeys, su mejor vuelta en el Earth Course de Jumeirah Golf Estates desde 2016.",
                "El danes Jacob Skov Olesen marcha segundo a un impacto con 68 (-4), seguido por cinco empatados al tercer puesto con -3: Rory McIlroy (69), Victor Perez, Gregorio De Leo, Freddy Schott y Francesco Laporta.",
                "En el partido estelar de la Race to Dubai, McIlroy (3.709,86 pts) cerro con birdie facil en el 18 para arrancar tres golpes por delante del lider espanol Eugenio Chacarra (4.243,79 pts), que firmo el par 72 (T28)."
            ]
        },
        "de": {
            "title": "Dubai R1: Joost Luiten fuehrt mit 67 (-5), waehrend Rory McIlroy mit 69 drei Schlaege auf Chacarra gutmacht",
            "subtitle": "Der 50. Starter im Feld gelingt seine beste Earth-Course-Runde seit 2016 vor Jacob Skov Olesen (68) und Freddy Schott (-3).",
            "excerpt": "Joost Luiten liegt nach einer 67 (-5) vor Jacob Skov Olesen (68); Rory McIlroy (69, T3) nimmt Race-Spitzenreiter Eugenio Chacarra (72, T28) drei Schlaege ab.",
            "body": [
                "Als Letztqualifizierter ins 50er-Feld von Dubai gerutscht, uebernahm der Niederlaender Joost Luiten am Donnerstag beim DP World Tour Championship mit sieben Birdies und zwei Bogeys zur 67 (-5) die alleinige Fuehrung.",
                "Einen Schlag dahinter folgt der Daene Jacob Skov Olesen mit 68 (-4). Zu fuenft auf Platz drei (-3) liegen neben Rory McIlroy (69) auch der Deutsche Freddy Schott, Victor Perez, Gregorio De Leo und Francesco Laporta.",
                "Im direkten Top-Flight der Race to Dubai (10 Millionen Dollar Preisgeld) beendete McIlroy seine 69 mit einem Tap-in-Birdie an der 18 und nahm Spitzenreiter Eugenio Chacarra (72, Even Par, T28) gleich drei Schlaege ab."
            ]
        },
        "it": {
            "title": "Dubai R1: Joost Luiten comanda in 67 (-5), McIlroy apre in 69 e guadagna tre colpi su Chacarra",
            "subtitle": "Bene anche gli azzurri Gregorio De Leo e Francesco Laporta nel quintetto terzo a -3 dietro a Luiten e Skov Olesen (68).",
            "excerpt": "L'olandese Joost Luiten chiude a -5 (67) avanti di uno su Skov Olesen, mentre Rory McIlroy (69) stacca subito Eugenio Chacarra (72) di tre colpi.",
            "body": [
                "Entrato come cinquantesimo ed ultimo qualificato al DP World Tour Championship, l'olandese Joost Luiten ha firmato giovedi un eccellente 67 (-5) con sette birdie e due bogey, il suo giro migliore all'Earth Course dal 2016.",
                "A un solo colpo insegue il danese Jacob Skov Olesen con 68 (-4), poi brillano anche gli italiani Gregorio De Leo e Francesco Laporta al terzo posto a -3 insieme a Rory McIlroy (69), Victor Perez e Freddy Schott.",
                "Nel gruppo clou della Race to Dubai, McIlroy ha chiuso con un birdie facile alla 18 prendendo subito tre lunghezze di margine sul leader spagnolo Eugenio Chacarra, fermo al par di giornata (72, T28)."
            ]
        },
        "pl": {
            "title": "Dubaj R1: Joost Luiten prowadzi z wynikiem 67 (-5), McIlroy otwiera 69 i zyskuje trzy uderzenia nad Chacarra",
            "subtitle": "Ostatni zakwalifikowany do 50-osobowej stawki gra najlepsza runde na Earth Course od 2016 przed Skov Olesenem (68).",
            "excerpt": "Joost Luiten prowadzi w Dubaju (-5, 67), a Rory McIlroy (-3, 69, T3) zyskal od razu trzy uderzenia nad liderem cyklu Eugenio Chacarra (72, T28).",
            "body": [
                "Holender Joost Luiten wszedl do DP World Tour Championship jako ostatni z 50 graczy i w czwartek objal samodzielne prowadzenie wynikiem 67 (-5) po siedmiu birdie i dwoch bogeyach.",
                "O jedno uderzenie za nim jest Dunczyk Jacob Skov Olesen (68, -4), a na trzecim miejscu (-3) ex aequo znajduja sie Rory McIlroy (69), Victor Perez, Gregorio De Leo, Freddy Schott i Francesco Laporta.",
                "W parze dnia Race to Dubai McIlroy (3709,86 pkt) trafil krotkiego birdie na 18. dolku i po pierwszej rundzie prowadzi trzema uderzeniami nad Hiszpanem Eugenio Chacarra (4243,79 pkt), ktory zagral na par (72, T28)."
            ]
        },
        "zh": {
            "title": "迪拜总决赛首轮：吕腾67杆领跑，麦克罗伊69杆并列第三抢占抢分先机",
            "subtitle": "压哨入围的荷兰老将交出2016年来个人球场最佳单轮，麦卡伊首日领先榜首查卡拉（72杆）三杆。",
            "excerpt": "约斯特·吕腾首轮抓7鸟吞2柏忌交出67杆（-5）领先丹麦球员奥莱森（68杆）1杆，麦克罗伊（69杆）力压同组查卡拉（72杆）。",
            "body": [
                "作为50人阵容压哨入围的荷兰选手约斯特·吕腾周四在朱美拉高尔夫庄园大地球场大放异彩，全场捉下7只小鸟吞下2个柏忌，打出67杆（-5）独自领跑DP世界巡回锦标赛首轮。",
                "丹麦选手雅各布·斯科夫·奥莱森以68杆（-4）紧随其后，领先榜第三位有五人并列-3，包括罗里·麦克罗伊（69杆）、维克托·佩雷斯、德莱奥、肖特与拉波尔塔。",
                "在备受瞩目的迪拜竞赛同组对话中，麦克罗伊收官洞轻松抓鸟交出69杆，首日便领先积分榜首位的西班牙选手欧亨尼奥·查卡拉（72杆平标准杆，并列第28）多达三杆。"
            ]
        },
        "ja": {
            "title": "ドバイ初日：ルイテンが67（-5）で単独首位、マキロイは69でチャカラに3打差先勝",
            "subtitle": "50人枠最後の出場となったオランダ勢が2016年以来のコース自己ベスト。オレセンが68で1打差追走。",
            "excerpt": "ヨースト・ルイテンが67（-5）で首位発進。ローリー・マキロイは69（-3、3位タイ）でポイント首位エウヘニオ・チャカラ（72）に3打差をつけた。",
            "body": [
                "ドバイでのDPワールドツアー選手権初日、50番目のギリギリで出場権を得たヨースト・ルイテンが7バーディ・2ボギーの67（-5）をマークし、2016年以来となるアースコース自己ベストで単独首位に立った。",
                "1打差の2位にヤコブ・スコフ・オレセン（68、-4）。3アンダーの3位タイにローリー・マキロイ（69）、ビクトル・ペレス、グレゴリオ・デ・レオ、フレディ・ショット、フランチェスコ・ラポルタの5人が並ぶ。",
                "レース・トゥ・ドバイ頂上決戦の注目組では、マキロイが最終18番のバーディで69にまとめ、イーブンパー72（28位タイ）に終わった首位チャカラに対し初日から3打リードを奪った。"
            ]
        },
        "ko": {
            "title": "두바이 1R: 라위텐 67타(-5) 단독 선두, 매킬로이는 69타로 포인트 1위 차카라에 3타 앞서",
            "subtitle": "50명 출전권 막차를 탄 라위텐이 2016년 이후 코스 최저타를 기록했고, 올레센(68타)이 1타 차로 추격합니다.",
            "excerpt": "요스트 라위텐이 5언더파 67타로 선두에 올랐고, 로리 매킬로이(69타, 공동 3위)는 선두 동반자 차카라(72타)를 3타 앞섰습니다.",
            "body": [
                "DP 월드투어 챔피언십 50번째 막차로 합류한 네덜란드의 요스트 라위텐이 목요일 두바이 주메이라 골프 에스테이트 어스 코스에서 버디 7개와 보기 2개로 67타(-5)를 쳐 단독 선두로 나섰습니다.",
                "덴마크의 야코브 스코브 올레센이 68타(-4)로 1타 뒤진 2위에 자리했고, 로리 매킬로이(69타)를 비롯해 빅토르 페레스, 그레고리오 데 레오, 프레디 쇼트, 프란체스코 라포르타 등 5명이 공동 3위(-3) 그룹을 형성했습니다.",
                "상금 300만 달러와 시즌 챔피언이 걸린 레이스 투 두바이 동반 라운드에서는 매킬로이가 18번 홀 버디로 69타를 적어내며 이븐파 72타(공동 28위)에 머문 포인트 선두 에우헤니오 차카라를 3타 차로 앞질렀습니다."
            ]
        },
        "ar": {
            "title": "دبي الجولة الأولى: لويتن يتصدر بـ67 ضربة (-5)، ومكلروي يتقدم على تشاكارا بثلاث ضربات",
            "subtitle": "آخر المتأهلين للبطولة يحقق أفضل جولة له منذ 2016 أمام أوليسن (68) وخمسة لاعبين في المركز الثالث (-3).",
            "excerpt": "الهولندي يوست لويتن ينفرد بالصدارة بـ67 ضربة (-5)، بينما أنهى روري مكلروي الجولة بـ69 متقدماً بثلاث ضربات على يوجينيو تشاكارا (72).",
            "body": [
                "خطف الهولندي يوست لويتن، آخر المنضمين لقائمة الخمسين لاعباً في بطولة جولة دي بي ورلد، صدارة الجولة الأولى الخميس في دبي بتسجيله 67 ضربة (5 تحت المعدل) عبر سبع بيردي وبوغي مرتين.",
                "ويحل الدنماركي جاكوب سكوف أوليسن ثانياً بفارق ضربة واحدة (68)، متقدماً على خماسي المركز الثالث بـ3 تحت المعدل ويضم روري مكلروي (69) وفيكتور بيريز وغريغوريو دي ليو وفريدي شوت وفرانشيسكو لابورتا.",
                "وفي الصراع المباشر على صدارة السباق إلى دبي، أنهى مكلروي جولته ببيردي سهل في الحفرة 18 (69) ليفتتح أفضليته بثلاث ضربات على المتصدر الإسباني يوجينيو تشاكارا الذي اكتفى بـ72 ضربة (المركز 28 مكرر)."
            ]
        }
    },
    "f1-countdown-las-vegas-round-21-five-way-chase-behind-antonelli-2026": {
        "fr": {
            "title": "J-7 avant la manche 21 a Las Vegas : cinq pilotes F1 groupes en 33 points derriere Antonelli",
            "subtitle": "Avec Mercedes (652) et Antonelli (390) deja titrés, Verstappen (279) mene Russell, Hamilton, Leclerc et Norris sur les 6,201 km du Strip.",
            "excerpt": "A une semaine du GP de Las Vegas (manche 21), 33 points separent Verstappen (279) de Norris (246), et Red Bull devance McLaren de 17 points.",
            "body": [
                "A sept jours du coup d'envoi de la 21e manche du championnat du monde F1 2026 sur le circuit urbain du Strip de Las Vegas (6,201 km, 19-21 novembre, course samedi soir), les deux couronnes appartiennent deja a Mercedes et a Kimi Antonelli, mais le classement derriere eux reste electrique.",
                "Revenu de la 21e place sur la grille a la 2e sous la pluie d'Interlagos, Max Verstappen pointe a 279 points au 2e rang des pilotes, un point devant le duel entre George Russell (262) et Lewis Hamilton (261), suivis de Charles Leclerc (249) et du vainqueur de Sao Paulo Lando Norris (246).",
                "Cote Constructeurs derriere Mercedes (652), Ferrari occupe la deuxieme place avec 510 points tandis que Red Bull (415) defend un court matelas de 17 points devant McLaren (398)."
            ]
        },
        "es": {
            "title": "A una semana de la ronda 21 en Las Vegas: cinco pilotos separados por 33 puntos tras Antonelli",
            "subtitle": "Con Mercedes (652) y Antonelli (390) campeones, Verstappen (279) lidera ante Russell, Hamilton, Leclerc y Norris hacia el trazado de 6,201 km.",
            "excerpt": "La penultima cita en el Strip de Las Vegas mantiene en 33 puntos a Verstappen (279) y Norris (246), con Red Bull solo 17 arriba sobre McLaren.",
            "body": [
                "A siete dias de la ronda 21 del Mundial de Formula 1 en los 6,201 kilometros del circuito urbano de Las Vegas (19-21 de noviembre, carrera el sabado por la noche), ambos titulos ya tienen dueno con Mercedes y Kimi Antonelli, pero la pelea del subcampeonato arde.",
                "Tras remontar del puesto 21 al segundo en Sao Paulo, Max Verstappen suma 279 puntos, seguido muy de cerca por George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) y el ganador en Interlagos Lando Norris (246): cinco estrellas comprimidas en apenas 33 puntos.",
                "Detras de Mercedes (652 puntos), Ferrari suma 510 y Red Bull (415) defiende 17 puntos de ventaja sobre McLaren (398) rumbo a Nevada."
            ]
        },
        "de": {
            "title": "Countdown zu Runde 21 in Las Vegas: Fuenf F1-Stars innerhalb von 33 Punkten hinter Champion Antonelli",
            "subtitle": "Mercedes (652) und Antonelli (390) stehen fest, doch Verstappen (279) bis Norris (246) kaempfen auf dem 6,201-km-Strip um Rang zwei.",
            "excerpt": "Eine Woche vor Las Vegas trennen Verstappen (279) und Norris (246) nur 33 Punkte; Red Bull liegt bei den Konstrukteuren 17 vor McLaren.",
            "body": [
                "Sieben Tage vor Runde 21 der Formel-1-WM 2026 auf dem 6,201 Kilometer langen Las Vegas Strip Circuit (19.-21. November) sind beide WM-Kronen an Mercedes (652) und Kimi Antonelli (390) vergeben, doch im Kampf um Platz zwei geht es extrem eng zu.",
                "Nach seiner Aufholjagd von Startplatz 21 auf Rang zwei in Sao Paulo fuehrt Max Verstappen das Verfolgerfeld mit 279 Punkten an, dicht gefolgt von George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) und Interlagos-Sieger Lando Norris (246).",
                "Hinter Mercedes haelt Ferrari 510 Konstrukteurspunkte, waehrend Red Bull (415) nur noch 17 Zaehler Vorsprung auf McLaren (398) besitzt."
            ]
        },
        "it": {
            "title": "Meno 7 al Round 21 di Las Vegas: cinque piloti F1 racchiusi in 33 punti dietro al campione Antonelli",
            "subtitle": "Con Mercedes (652) e Antonelli (390) gia iridati, Verstappen (279) guida su Russell, Hamilton, Leclerc e Norris verso i 6,201 km dello Strip.",
            "excerpt": "Verso la gara notturna di Las Vegas solo 33 punti dividono Verstappen (279) e Norris (246), mentre la Red Bull precede la McLaren di 17.",
            "body": [
                "A sette giorni dal Round 21 del Mondiale F1 2026 sui 6,201 chilometri del Las Vegas Strip Circuit (19-21 novembre), entrambi i titoli appartengono a Kimi Antonelli (390) e alla Mercedes (652), ma la lotta per il secondo posto resta apertissima.",
                "Dopo la rimonta dal 21o al 2o posto sul bagnato di Interlagos, Max Verstappen guida il gruppetto con 279 punti davanti a George Russell (262), Lewis Hamilton (261), Charles Leclerc (249) e al vincitore di San Paolo Lando Norris (246).",
                "Tra i Costruttori la Ferrari e seconda a quota 510 punti, mentre la Red Bull (415) difende un margine di appena 17 punti sulla McLaren (398)."
            ]
        },
        "pl": {
            "title": "Tydzien do 21. rundy w Las Vegas: piec gwiazd F1 w 33 punktach za mistrzem Antonellim",
            "subtitle": "Mercedes (652) i Antonelli (390) maja juz tytuly, ale od Verstappena (279) do Norrisa (246) trwa scisk przed torem Strip (6,201 km).",
            "excerpt": "Przed runda w Las Vegas tylko 33 punkty dziela Verstappena (279) i Norrisa (246), a Red Bull wyprzedza McLarena o zaledwie 17 punktow.",
            "body": [
                "Na siedem dni przed 21. runda mistrzostw swiata F1 na ulicznym torze w Las Vegas o dlugosci 6,201 km (19-21 listopada) oba tytuly sa juz rozdane, lecz bezposrednio za mistrzem Kimim Antonellim (390 pkt) walka nabiera rumiencow.",
                "Po awansie z 21. na 2. miejsce w Sao Paulo Max Verstappen ma 279 punktow i wyprzedza George'a Russella (262), Lewisa Hamiltona (261), Charlesa Leclerca (249) oraz zwyciezce z Interlagos Lando Norrisa (246).",
                "Wsrod konstruktorow za Mercedesem (652) drugie jest Ferrari (510), a trzeci Red Bull (415) broni 17 punktow przewagi nad McLarenem (398)."
            ]
        },
        "zh": {
            "title": "F1拉斯维加斯站（第21站）倒计时一周：安东内利身后的五虎之争仅差33分",
            "subtitle": "梅赛德斯（652分）与安东内利（390分）加冕双冠后，维斯塔潘（279分）至诺里斯（246分）将决战6.201公里拉斯维加斯大道赛道。",
            "excerpt": "第21站夜赛下周开启，维斯塔潘（279分）领先第六名诺里斯（246分）33分；车队方面红牛（415分）仅领先迈凯伦17分。",
            "body": [
                "距离2026赛季F1第21站拉斯维加斯大奖赛（11月19-21日，单圈6.201公里）仅剩七天，车手总冠军基米·安东内利（390分）与梅赛德斯车队（652分）虽已提前封王，但积分榜第二集团依旧悬念重重。",
                "圣保罗雨战从第21位逆袭至亚军的马克斯·维斯塔潘目前以279分暂居第二，紧随其后的是乔治·拉塞尔（262分）、刘易斯·汉密尔顿（261分）、夏尔·勒克莱尔（249分）以及巴西站冠军兰多·诺里斯（246分）。",
                "车队积分榜上法拉利510分排名第二，红牛（415分）则只领先第四名迈凯伦（398分）17分，夜赛容错空间微乎其微。"
            ]
        },
        "ja": {
            "title": "F1ラスベガスGP（第21戦）開幕まで1週間：王者アントネッリの背後で5選手が33点差の混戦",
            "subtitle": "メルセデス（652点）とアントネッリ（390点）戴冠の中、フェルスタッペン（279点）からノリス（246点）までが全長6.201kmのストリップへ。",
            "excerpt": "第21戦ラスベガスを控え、2位フェルスタッペン（279）から6位ノリス（246）まで33点差。コンストラクターズではレッドブルとマクラーレンが17点差。",
            "body": [
                "全長6.201キロのラスベガス・ストリップ・サーキットを舞台とするF1第21戦（11月19日〜21日、決勝は土曜夜）まであと1週間。キム・アントネッリ（390点）とメルセデス（652点）の王座は確定したものの、ランキング2位争いは白熱している。",
                "サンパウロGPで21番グリッドから2位に浮上したマックス・フェルスタッペンが279点で2番手につけ、ジョージ・ラッセル（262点）、ルイス・ハミルトン（261点）、シャルル・ルクレール（249点）、ブラジル勝者ランド・ノリス（246点）までわずか33点圏内にひしめく。",
                "コンストラクターズは2位フェラーリ（510点）の後ろでレッドブル（415点）がマクラーレン（398点）を17点リードしている。"
            ]
        },
        "ko": {
            "title": "F1 라스베이거스(21라운드) D-7: 챔피언 안토넬리 뒤 5명 33점 차 초박빙 순위 싸움",
            "subtitle": "메르세데스(652점)와 안토넬리(390점) 우승 확정 속 베르스타펜(279점)부터 노리스(246점)까지 6.201km 스트립 서킷 정조준.",
            "excerpt": "다음 주 21라운드 라스베이거스 GP를 앞두고 2위 베르스타펜과 6위 노리스의 격차는 33점, 레드불과 맥라렌 차이는 17점입니다.",
            "body": [
                "11월 19일부터 21일까지 총길이 6.201km 라스베이거스 스트립 서킷에서 펼쳐지는 2026 F1 21라운드를 일주일 앞두고 드라이버 챔피언 키미 안토넬리(390점)와 메르세데스(652점)의 우승은 확정됐지만 2위권 다툼은 치열합니다.",
                "상파울루 빗길에서 21번 그리드 출발해 2위에 오른 막스 베르스타펜이 279점으로 2위를 지키는 가운데 조지 러셀(262점), 루이스 해밀턴(261점), 샤를 르클레르(249점), 브라질 우승자 랜도 노리스(246점)까지 단 33점 차로 뭉쳐 있습니다.",
                "컨스트럭터즈 순위에서는 페라리(510점)에 이어 레드불(415점)이 맥라렌(398점)을 17점 차로 앞서고 있습니다."
            ]
        },
        "ar": {
            "title": "أسبوع واحد على جولة لاس فيغاس (الجولة 21): خمسة سائقين في الفورمولا 1 يفصلهم 33 نقطة خلف أنطونيلي",
            "subtitle": "مع تتويج مرسيدس (652) وأنطونيلي (390)، يتقدم فيرستابن (279) على راسل وهاميلتون ولوكلير ونوريس نحو حلبة 6.201 كلم.",
            "excerpt": "قبل سباق الجولة 21 الليلي الأسبوع المقبل، يفصل 33 نقطة بين الثاني فيرستابن والسادس نوريس، ويتفوق ريد بول على مكلارين بـ17 نقطة فقط.",
            "body": [
                "قبل سبعة أيام من انطلاق الجولة الحادية والعشرين من بطولة العالم للفورمولا 1 لعام 2026 على حلبة شوارع لاس فيغاس البالغ طولها 6.201 كيلومتر (19-21 نوفمبر)، حسم مرسيدس (652 نقطة) وكيمي أنطونيلي (390 نقطة) اللقبين العالميين، لكن معركة الوصافة تشتعل.",
                "وبعد صعوده من المركز 21 إلى الثاني تحت أمطار ساو باولو، يتصدر ماكس فيرستابن المطاردة برصيد 279 نقطة أمام جورج راسل (262) ولويس هاميلتون (261) وشارل لوكلير (249) ولاندو نوريس (246).",
                "وعند الصانعين يحتل فيراري المركز الثاني برصيد 510 نقاط، بينما يدافع ريد بول (415) عن فارق ضئيل يبلغ 17 نقطة أمام مكلارين (398)."
            ]
        }
    }
}


NEW_TEAMS = {
    "FC Barcelona Femeni": {"fr": "FC Barcelone Femeni", "es": "FC Barcelona Femenino", "de": "FC Barcelona Frauen", "it": "FC Barcellona Femminile", "pl": "FC Barcelona Kobiety", "zh": "巴塞罗那女足", "ja": "FCバルセロナ女子", "ko": "FC 바르셀로나 페메니", "ar": "برشلونة للسيدات"},
    "Arsenal Women": {"fr": "Arsenal Women", "es": "Arsenal Femenino", "de": "Arsenal Frauen", "it": "Arsenal Femminile", "pl": "Arsenal Kobiety", "zh": "阿森纳女足", "ja": "アーセナル女子", "ko": "아스널 위민", "ar": "أرسنال للسيدات"},
    "Juventus Women": {"fr": "Juventus Women", "es": "Juventus Femenino", "de": "Juventus Frauen", "it": "Juventus Women", "pl": "Juventus Kobiety", "zh": "尤文图斯女足", "ja": "ユベントス女子", "ko": "유벤투스 위민", "ar": "يوفنتوس للسيدات"},
    "OL Lyonnes": {"fr": "OL Lyonnes", "es": "OL Lyonnes", "de": "OL Lyonnes", "it": "OL Lyonnes", "pl": "OL Lyonnes", "zh": "里昂女足", "ja": "OLリヨン", "ko": "OL 리옹", "ar": "أولمبيك ليون للسيدات"},
    "Houston Rockets": {"zh": "休斯敦火箭", "ja": "ヒューストン・ロケッツ", "ko": "휴스턴 로케츠", "ar": "هيوستن روكتس"},
    "Golden State Warriors": {"zh": "金州勇士", "ja": "ゴールデンステート・ウォリアーズ", "ko": "골든스테이트 워리어스", "ar": "غولدن ستيت ووريورز"},
    "Cleveland Cavaliers": {"zh": "克利夫兰骑士", "ja": "クリーブランド・キャバリアーズ", "ko": "클리블랜드 캐벌리어스", "ar": "كليفلاند كافالييرز"},
    "New York Knicks": {"zh": "纽约尼克斯", "ja": "ニューヨーク・ニックス", "ko": "뉴욕 닉스", "ar": "نيويورك نيكس"},
    "Washington Commanders": {"zh": "华盛顿指挥官", "ja": "ワシントン・コマンダース", "ko": "워싱턴 커맨더스", "ar": "واشنطن كوماندرز"},
    "New York Giants": {"zh": "纽约巨人", "ja": "ニューヨーク・ジャイアンツ", "ko": "뉴욕 자이언츠", "ar": "نيويورك جاينتس"},
}

NEW_PLACES = {
    "Spotify Camp Nou": {"zh": "诺坎普球场", "ja": "カンプ・ノウ", "ko": "스포티파이 캄프 누", "ar": "سبوتيفاي كامب نو"},
    "Barcelona": {"fr": "Barcelone", "es": "Barcelona", "de": "Barcelona", "it": "Barcellona", "pl": "Barcelona", "zh": "巴塞罗那", "ja": "バルセロナ", "ko": "바르셀로나", "ar": "برشلونة"},
    "Wembley Stadium": {"fr": "Stade de Wembley", "es": "Estadio de Wembley", "de": "Wembley-Stadion", "it": "Wembley", "pl": "Stadion Wembley", "zh": "温布利球场", "ja": "ウェンブリー・スタジアム", "ko": "웸블리 스타디움", "ar": "ملعب ويمبلي"},
    "Turin": {"fr": "Turin", "es": "Turín", "de": "Turin", "it": "Torino", "pl": "Turyn", "zh": "都灵", "ja": "トリノ", "ko": "토리노", "ar": "تورينو"},
    "Inalpi Arena": {"zh": "伊纳尔皮体育馆", "ja": "インアルピ・アリーナ", "ko": "이날피 아레나", "ar": "إنالبي أرينا"},
    "Toyota Center": {"zh": "丰田中心", "ja": "トヨタ・センター", "ko": "도요타 센터", "ar": "مركز تويوتا"},
}

NEW_COMPETITIONS = {
    "atp-finals-2026": {
        "fr": "Nitto ATP Finals 2026",
        "es": "Nitto ATP Finals 2026",
        "de": "Nitto ATP Finals 2026",
        "it": "Nitto ATP Finals 2026",
        "pl": "Nitto ATP Finals 2026",
        "zh": "2026 ATP年终总决赛",
        "ja": "Nitto ATPファイナルズ 2026",
        "ko": "2026 니토 ATP 파이널스",
        "ar": "نهائيات ATP 2026",
    },
    "nations-league-2026-27": {
        "fr": "Ligue des nations UEFA 2026-27",
        "es": "Liga de Naciones UEFA 2026-27",
        "de": "UEFA Nations League 2026/27",
        "it": "UEFA Nations League 2026-27",
        "pl": "Liga Narodów UEFA 2026/27",
        "zh": "2026-27 欧国联",
        "ja": "UEFAネーションズリーグ 2026-27",
        "ko": "2026-27 UEFA 네이션스리그",
        "ar": "دوري الأمم الأوروبية 2026-27",
    },
}


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
    lint_obj(NOV12_STORIES)
    lint_obj(NEW_TEAMS)
    lint_obj(NEW_PLACES)
    lint_obj(NEW_COMPETITIONS)
    print("All Nov 12 translations validated: 0 em-dashes and 0 double-hyphens.")

    # 1. Inject 6 Nov 12 story translations into stories.ts
    stories_file = os.path.join(ROOT, "frontend/src/i18n/stories.ts")
    with open(stories_file, "r", encoding="utf-8") as f:
        st_content = f.read()

    to_inject = []
    for slug, langs in NOV12_STORIES.items():
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

    # 2. Update frontend/src/i18n/names.ts
    names_file = os.path.join(ROOT, "frontend/src/i18n/names.ts")
    with open(names_file, "r", encoding="utf-8") as f:
        names_content = f.read()

    names_content = inject_dict_entries(names_content, "const TEAMS:", r"\r?\n\};\r?\n\r?\nconst PLACES:", NEW_TEAMS)
    names_content = inject_dict_entries(names_content, "const PLACES:", r"\r?\n\};\r?\n\r?\nconst COMPETITIONS:", NEW_PLACES)
    names_content = inject_dict_entries(names_content, "const COMPETITIONS:", r"\r?\n\};\r?\n\r?\nexport function entityName", NEW_COMPETITIONS)

    # Also ensure competitionName English case handles 'atp-finals-2026'
    if "if (competition === 'atp-finals-2026')" not in names_content:
        anchor = "    if (competition === 'atp-250-stockholm-2026') return 'Stockholm Open';\n"
        anchor_crlf = "    if (competition === 'atp-250-stockholm-2026') return 'Stockholm Open';\r\n"
        if anchor in names_content:
            names_content = names_content.replace(
                anchor,
                anchor + "    if (competition === 'atp-finals-2026') return 'Nitto ATP Finals';\n",
                1,
            )
        elif anchor_crlf in names_content:
            names_content = names_content.replace(
                anchor_crlf,
                anchor_crlf + "    if (competition === 'atp-finals-2026') return 'Nitto ATP Finals';\r\n",
                1,
            )

    with open(names_file, "w", encoding="utf-8") as f:
        f.write(names_content)
    print("Updated frontend/src/i18n/names.ts successfully.")
