#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add 11 November 2026 story translations for all 6 stories across 9 non-English locales."""
import json
import os
import re

NOV11_STORIES = {
    "nba-celtics-123-76ers-101-paul-george-revenge-return-2026": {
        "fr": {
            "title": "NBA : Paul George inscrit 36 points pour son retour a Philadelphie, les Celtics dominent les 76ers 123-101",
            "subtitle": "A egalite 79-79 en fin de troisieme quart-temps, Boston passe un 26-3 decisif pendant que Jaylen Brown souffre des fautes.",
            "excerpt": "Paul George a reussi six paniers a trois points pour 36 points a Philadelphie et Boston prend la premiere place a l'Est (9-2).",
            "body": [
                "De retour au Xfinity Mobile Arena pour la premiere fois depuis son transfert estival, Paul George a frappe fort mardi 10 novembre. En 30 minutes et 9 secondes, il a marque 36 points (6 sur 11 a trois points, 5 rebonds, 14 points dans le dernier quart-temps) pour mener les Boston Celtics a un large succes 123-101 chez les Philadelphia 76ers.",
                "A egalite 79-79 en fin de troisieme quart-temps, Boston a brise le match sur un 26-3 a cheval sur les deux derniers quart-temps. Jayson Tatum a ajoute 21 points, Payton Pritchard 18 et Sam Hauser 12 pour hisser Boston a 9-2 en tete de l'Est devant Philadelphie (9-3, 24 points de Tyrese Maxey, 13 pour Jaylen Brown freine par les fautes). Mercredi sur ESPN : Cavaliers chez les Knicks (19h ET) et Warriors a Houston (21h30 ET)."
            ]
        },
        "es": {
            "title": "NBA: Paul George anota 36 puntos en su regreso a Filadelfia y los Celtics vencen 123-101 a los 76ers",
            "subtitle": "Empatados 79-79 al cierre del tercer cuarto, Boston firma un parcial de 26-3 mientras Jaylen Brown sufre con las faltas.",
            "excerpt": "Paul George encesto seis triples para alcanzar 36 puntos en su antiguo pabellon y Boston sube al liderato del Este con 9-2.",
            "body": [
                "En su primera visita al Xfinity Mobile Arena desde su traspaso en verano, Paul George ofrecio una noche inolvidable el martes 10 de noviembre. Sumo 36 puntos en 30:09 con 6 de 11 en triples y 14 tantos en el ultimo cuarto para liderar la victoria 123-101 de los Boston Celtics sobre los Philadelphia 76ers.",
                "Con empate 79-79 en el tercer periodo, Boston sentencio con un parcial de 26-3. Jayson Tatum aporto 21 puntos, Payton Pritchard 18 y Sam Hauser 12 para dejar a Boston (9-2) primero del Este por delante de Filadelfia (9-3, Tyrese Maxey 24, Jaylen Brown 13). Este miercoles en ESPN: Cavaliers en Knicks (19:00 ET) y Warriors en Rockets (21:30 ET)."
            ]
        },
        "de": {
            "title": "NBA: Paul George erzielt 36 Punkte bei Rueckkehr nach Philadelphia, Celtics ueberrollen 76ers 123:101",
            "subtitle": "Beim Stand von 79:79 startet Boston einen 26:3-Lauf, waehrend Jaylen Brown gegen Jayson Tatum in Foulprobleme geraet.",
            "excerpt": "Paul George trifft sechs Dreier zu 36 Punkten gegen sein Ex-Team und fuehrt die Celtics (9-2) an die Spitze der Eastern Conference.",
            "body": [
                "Bei seiner ersten Rueckkehr in die Xfinity Mobile Arena seit dem Sommerwechsel lieferte Paul George am Dienstag, 10. November, 36 Punkte in 30:09 Minuten (6 von 11 Dreiern, 14 Punkte im Schlussviertel) beim 123:101-Auswaertssieg der Boston Celtics gegen die Philadelphia 76ers.",
                "Beim 79:79 im dritten Viertel uebernahm Boston mit einem 26:3-Lauf das Kommando. Jayson Tatum erzielte 21 Punkte, Payton Pritchard 18 und Sam Hauser 12. Boston klettert mit 9-2 auf Platz eins im Osten vor Philadelphia (9-3, Tyrese Maxey 24, Jaylen Brown 13). Heute Nacht auf ESPN: Cavaliers bei den Knicks (19:00 ET) und Warriors in Houston (21:30 ET)."
            ]
        },
        "it": {
            "title": "NBA: Paul George segna 36 punti nel ritorno a Philadelphia, Celtics travolgono i 76ers 123-101",
            "subtitle": "Sul 79-79 nel terzo quarto Boston piazza un parziale di 26-3 mentre Jaylen Brown fatica per falli contro Jayson Tatum.",
            "excerpt": "Con sei triple e 36 punti di Paul George nella sua vecchia arena, Boston sale al primo posto ad Est con il record di 9-2.",
            "body": [
                "Nel suo primo ritorno allo Xfinity Mobile Arena dopo la cessione estiva, Paul George ha dominato martedi 10 novembre con 36 punti in 30:09 (6 su 11 da tre, 14 punti nel quarto quarto) guidando i Boston Celtics al netto 123-101 sui Philadelphia 76ers.",
                "Dal 79-79 nel finale del terzo periodo, Boston ha spaccato la gara con un parziale di 26-3. Jayson Tatum ha aggiunto 21 punti, Payton Pritchard 18 e Sam Hauser 12 per portare i Celtics (9-2) al comando a Est davanti a Philadelphia (9-3, Maxey 24, Jaylen Brown 13). Questa notte su ESPN: Cavaliers dai Knicks e Warriors a Houston."
            ]
        },
        "pl": {
            "title": "NBA: Paul George rzuca 36 punktow po powrocie do Filadelfii, Celtics gromia 76ers 123-101",
            "subtitle": "Przy remisie 79-79 w trzeciej kwarcie Boston notuje serie 26-3, a Jaylen Brown szybko lapie faule przeciwko Tatumowi.",
            "excerpt": "Paul George trafil szesc trojek i zdobyl 36 punktow, wyprowadzajac Boston (9-2) na prowadzenie w Konferencji Wschodniej.",
            "body": [
                "W pierwszym powrocie do hali Xfinity Mobile Arena od letniej wymiany Paul George we wtorek 10 listopada zdobyl 36 punktow w 30 minut i 9 sekund (6 na 11 za trzy, 14 pkt w czwartej kwarcie), prowadzac Boston Celtics do wygranej 123-101 nad Philadelphia 76ers.",
                "Od stanu 79-79 pod koniec trzeciej kwarty Celtics zaliczyli serie 26-3. Jayson Tatum rzucil 21 punktow, Payton Pritchard 18, a Sam Hauser 12, dzieki czemu Boston (9-2) wyprzedzil Filadelfie (9-3, Tyrese Maxey 24, Jaylen Brown 13) na szczycie Wschodu. W srode na ESPN zagraja Cavaliers z Knicks oraz Warriors z Rockets."
            ]
        },
        "zh": {
            "title": "NBA：保罗·乔治重返费城狂砍36分，凯尔特人123-101大胜76人登顶东部",
            "subtitle": "第三节末双方战成79平后绿军打出26-3攻势，杰伦·布朗受困犯规仅得13分。",
            "excerpt": "保罗·乔治飙中6记三分轰下36分，率波士顿9胜2负超越费城升至东部第一。",
            "body": [
                "11月10日周二，夏季转会离队后首次重返Xfinity移动球馆的保罗·乔治火力全开，出场30分09秒砍下36分（三分11投6中，末节14分），带领波士顿凯尔特人客场123-101大胜费城76人。",
                "比赛第三节末一度战至79平，凯尔特人随后轰出一波26-3确立胜局。杰森·塔图姆贡献21分，普里查德18分、豪泽12分，绿军9胜2负反超费城（9胜3负，马克西24分，布朗13分）升至东部头名。周三ESPN直播两场焦点战：骑士客战尼克斯，勇士挑战火箭。"
            ]
        },
        "ja": {
            "title": "NBA：ポール・ジョージが古巣フィラデルフィアで36得点、セルティックスが76ersを123-101で撃破し東1位浮上",
            "subtitle": "第3Q終盤の79-79からボストンが26-3の猛攻。ジェイレン・ブラウンはファウルトラブルで13得点に終わる。",
            "excerpt": "夏のトレード後初のフィラデルフィア凱旋でジョージが6本の3点シュートを含む36得点。セルティックスが9勝2敗で首位に立った。",
            "body": [
                "11月10日火曜、夏の移籍後初めてXfinityモバイル・アリーナへ戻ったポール・ジョージが30分09秒の出場で3点シュート6本（11試投）を含む36得点、第4Qだけで14得点を挙げる爆発を見せ、ボストン・セルティックスがフィラデルフィア・76ersに123-101で圧勝した。",
                "第3クォーター終盤の79-79からボストンは26-3のランで一気に突き放した。ジェイソン・テイタムが21得点、プリチャード18得点、ハウザー12得点を加え、セルティックスは9勝2敗で76ers（9勝3敗、マクシー24点、ブラウン13点）をかわして東首位へ。水曜はESPNでキャバリアーズ対ニックスとウォリアーズ対ロケッツが行われる。"
            ]
        },
        "ko": {
            "title": "NBA: 폴 조지, 친정 필라델피아 원정서 36점 폭발… 보스턴 76ers 123-101 완파 동부 1위",
            "subtitle": "3쿼터 막판 79-79 동점에서 보스턴이 26-3 연속 득점으로 승부를 갈랐고, 제일런 브라운은 파울 트러블에 고전했습니다.",
            "excerpt": "3점슛 6방 포함 36점을 몰아친 폴 조지의 활약으로 보스턴이 9승 2패를 기록하며 동부 컨퍼런스 선두에 올랐습니다.",
            "body": [
                "여름 이적 이후 처음으로 Xfinity 모바일 아레나 원정길에 오른 폴 조지가 11월 10일 화요일(현지시간) 30분 9초 동안 3점슛 11개 중 6개를 적중시키며 36득점(4쿼터 14점)을 몰아쳐 보스턴 셀틱스의 필라델피아 세븐티식서스전 123-101 대승을 이끌었습니다.",
                "3쿼터 막판 79-79 동점 상황에서 보스턴은 26-3 런으로 순식간에 격차를 벌렸습니다. 제이슨 테이텀이 21점, 프리차드가 18점을 보탠 보스턴은 9승 2패로 필라델피아(9승 3패, 맥시 24점, 브라운 13점)를 제치고 동부 1위에 올랐습니다. 수요일 밤에는 클리블랜드-뉴욕전과 골든스테이트-휴스턴전이 ESPN에서 중계됩니다."
            ]
        },
        "ar": {
            "title": "NBA: بول جورج يسجل 36 نقطة في عودته الى فيلادلفيا وسلتيكس يكتسح سيكسرز 123-101",
            "subtitle": "بعد التعادل 79-79 في نهاية الربع الثالث، يفرض بوسطن سيطرته بسلسلة 26-3 مع معاناة جايلن براون من الاخطاء.",
            "excerpt": "احرز بول جورج ست ثلاثيات و36 نقطة ليقود بوسطن سلتيكس (9-2) لصدارة المنطقة الشرقية على حساب فيلادلفيا (9-3).",
            "body": [
                "في اول عودة له الى قاعة Xfinity Mobile Arena منذ انتقاله الصيفي، تالق بول جورج يوم الثلاثاء 10 نوفمبر وسجل 36 نقطة خلال 30:09 دقيقة (6 من 11 من الثلاثيات، و14 نقطة في الربع الاخير) ليقود بوسطن سلتيكس للفوز 123-101 على مضيفه فيلادلفيا سفنتي سيكسرز.",
                "عقب التعادل 79-79 اواخر الربع الثالث، انتفض سلتيكس بسلسلة 26-3 حاسمة. واضاف جيسون تيتوم 21 نقطة وبايتون بريتشارد 18 وسام هاوزر 12 ليرفع بوسطن رصيده الى 9-2 في قمة الشرق امام فيلادلفيا (9-3، ماكسي 24، براون 13). والليلة على ESPN يلعب كليفلاند في ضيافة نيكس وواريورز امام روكتس."
            ]
        }
    },
    "nfl-week10-tnf-commanders-at-giants-whiteout-rematch-2026": {
        "fr": {
            "title": "NFL Semaine 10 TNF : les Giants (5-2-1) et J.J. McCarthy recoivent les Commanders en White Out",
            "subtitle": "Leader de la NFC Est, New York retrouve Washington jeudi au MetLife Stadium cinq semaines apres un nul 27-27 en prolongation.",
            "excerpt": "Cinq semaines apres un nul 27-27, les Giants (5-2-1) visent un nouveau succes jeudi soir avec le retour a l'entrainement complet de J.J. McCarthy.",
            "body": [
                "La premiere place de la NFC Est se joue jeudi soir 12 novembre au MetLife Stadium (20h15 ET, Prime Video), ou les New York Giants (5-2-1, 2-0-1 en division) accueillent les Washington Commanders (2-5-1) devant un stade invite a porter du blanc pour ce White Out.",
                "Apres leur succes 19-11 a Philadelphie dimanche, le premier des Giants la-bas depuis 2013, J.J. McCarthy (hanche) s'est entraine normalement et devrait debuter aux cotes de Malik Nabers, Cam Skattebo et Darnell Mooney pour effacer le nul 27-27 de la Semaine 5. De son cote, Buffalo affiche 7-1 apres avoir domine Minnesota (6-2) 23-6 lundi."
            ]
        },
        "es": {
            "title": "NFL Semana 10 TNF: Giants (5-2-1) y J.J. McCarthy reciben a los Commanders tras el empate 27-27",
            "subtitle": "El lider de la NFC Este juega el jueves en MetLife Stadium en noche de White Out frente a unos Commanders con marca 2-5-1.",
            "excerpt": "Cinco semanas despues del 27-27 en prorroga, los Giants reciben el jueves a Washington con J.J. McCarthy entrenando al maximo.",
            "body": [
                "El liderato de la NFC Este abre la Semana 10 este jueves 12 de noviembre en el MetLife Stadium (8:15 p.m. ET, Prime Video) con la revancha entre New York Giants (5-2-1, 2-0-1 en division) y Washington Commanders (2-5-1) cinco semanas despues de su empate 27-27 en prorroga.",
                "Tras ganar 19-11 en Filadelfia por primera vez desde 2013, el quarterback J.J. McCarthy (cadera) entreno completo y apunta a ser titular junto a Malik Nabers y Cam Skattebo en una noche de uniforme Vintage White. En la AFC, Buffalo subio a 7-1 tras derrotar 23-6 a los Vikings (6-2) el lunes."
            ]
        },
        "de": {
            "title": "NFL Woche 10 TNF: Giants (5-2-1) mit J.J. McCarthy empfangen Commanders zum Rueckspiel nach 27:27",
            "subtitle": "NFC-East-Spitzenreiter New York laedt am Donnerstag ins MetLife Stadium zum White Out gegen Washington (2-5-1).",
            "excerpt": "Fuenf Wochen nach dem 27:27 nach Verlaengerung kehrt J.J. McCarthy vor heimischem Publikum in East Rutherford als Starter zurueck.",
            "body": [
                "Am Donnerstagabend, 12. November (20:15 Uhr ET, Prime Video), eroeffnen die New York Giants (5-2-1) und die Washington Commanders (2-5-1) die zehnte NFL-Woche im MetLife Stadium. Vor fuenf Wochen trennten sich beide Divisionsrivalen 27:27 nach Verlaengerung.",
                "Nach dem 19:11-Auswaertssieg in Philadelphia am Sonntag trainierte Quarterback J.J. McCarthy (Huefte) voll mit und steht neben Malik Nabers und Cam Skattebo vor dem White-Out-Heimspiel bereit. Washington setzt offensiv weiter auf Treylon Burks. Am Montag verbesserten sich die Bills mit einem 23:6 bei den Vikings (6-2) auf 7-1."
            ]
        },
        "it": {
            "title": "NFL Week 10 TNF: Giants (5-2-1) con J.J. McCarthy sfidano i Commanders dopo il 27-27 dell'andata",
            "subtitle": "La capolista della NFC East scende in campo giovedi al MetLife Stadium in serata White Out contro Washington.",
            "excerpt": "Cinque settimane dopo il pareggio per 27-27 ai supplementari, i Giants riabbracciano J.J. McCarthy a pieno regime per il TNF.",
            "body": [
                "Giovedi 12 novembre (20:15 ET, Prime Video), i New York Giants (5-2-1, 2-0-1 nella NFC East) ospitano i Washington Commanders (2-5-1) al MetLife Stadium nel primo appuntamento della Week 10, cinque settimane dopo il rocambolesco pareggio 27-27 ai tempi supplementari.",
                "Dopo il successo per 19-11 a Philadelphia, il primo dal 2013 sul campo degli Eagles, il quarterback J.J. McCarthy (anca) si e allenato completamente e guida l'attacco con Malik Nabers e Cam Skattebo in maglia Vintage White. Intanto Buffalo e salita a 7-1 battendo 23-6 i Vikings (6-2) lunedi notte."
            ]
        },
        "pl": {
            "title": "NFL tydzien 10 TNF: Giants (5-2-1) z J.J. McCarthym podejmuja Commanders w meczu rewanzowym po 27-27",
            "subtitle": "Lider dywizji NFC East zagra w czwartek na MetLife Stadium w bialych barwach piec tygodni po remisie po dogrywce.",
            "excerpt": "New York Giants przystepuja do czwartkowego TNF z pelnym treningiem J.J. McCarthy'ego po wygranej 19-11 w Filadelfii.",
            "body": [
                "Walka w NFC East otwiera 10. tydzien NFL w czwartek 12 listopada o 20:15 ET (Prime Video), gdy New York Giants (5-2-1) podejma Washington Commanders (2-5-1) na MetLife Stadium piec tygodni po szalonym remisie 27-27 po dogrywce.",
                "Po niedzielnej wygranej 19-11 w Filadelfii (pierwszej od 2013 roku) rozgrywajacy J.J. McCarthy wrocil do pelnych treningow i ma wyjsc w pierwszym skladzie z Malikiem Nabersem oraz Camem Skattebo. Tymczasem Bills poprawili bilans na 7-1, pokonujac Vikings (6-2) 23-6 w poniedzialek."
            ]
        },
        "zh": {
            "title": "NFL第10周周四夜赛：巨人（5-2-1）与麦卡锡主场“白色主题战”再战指挥官",
            "subtitle": "两队曾在第5周加时战成27-27平，国联东区领头羊纽约周四晚在大都会人寿体育场迎战华盛顿。",
            "excerpt": "四分卫J.J.麦卡锡全额参与合练有望首发，5胜2负1平的巨人周四夜赛在主场再度过招指挥官。",
            "body": [
                "北京时间11月13日周五早（美东周四晚8:15，Prime Video直播），NFL第10周周四夜赛将迎来国联东区二番战，领头羊纽约巨人（5胜2负1平，区内2胜0负1平）坐镇大都会人寿体育场举办白色主题夜赛，迎战华盛顿指挥官（2胜5负1平）。两队第5周曾加时战成27-27平。",
                "周日客场19-11击败老鹰（自2013年以来首次客胜费城）后，巨人四分卫J.J.麦卡锡髋部恢复良好并全程参加训练，预计领衔内伯斯和斯卡特博先发；华盛顿外接手特雷隆·伯克斯预计出战。本周早些时候，比尔周一夜赛23-6轻取维京人（6-2）升至7胜1负。"
            ]
        },
        "ja": {
            "title": "NFL第10週TNF：NFC東首位のジャイアンツ（5-2-1）がホワイトアウトでコマンダーズと再戦",
            "subtitle": "第5週に延長27-27の引き分けを演じた両者が木曜夜メットライフ・スタジアムで激突。QBマッカーシーが先発見込み。",
            "excerpt": "J.J.マッカーシーが全体練習にフル復帰。地区首位に立つニューヨークが第5週の雪辱を期して木曜夜戦に臨む。",
            "body": [
                "NFL第10週は現地木曜11月12日20時15分（Prime Video）のTNFで幕を開け、NFC東地区首位のニューヨーク・ジャイアンツ（5勝2敗1分）がホームのメットライフ・スタジアムにワシントン・コマンダーズ（2勝5敗1分）を迎える。第5週の前戦は延長の末27-27のドローに終わっていた。",
                "日曜にフィラデルフィアで2013年以来となる敵地勝利（19-11）を挙げたジャイアンツは、腰の負傷が癒えたQB J.J.マッカーシーが完全合流しており、マリック・ネイバースやキャム・スカッテボと共に先発する見込み。一方、月曜MNFではビルズがバイキングス（6-2）を23-6で破り7勝1敗としている。"
            ]
        },
        "ko": {
            "title": "NFL 10주차 TNF: 지구 1위 자이언츠(5-2-1), 5주차 27-27 무승부 설욕전… 맥카시 선발 유력",
            "subtitle": "목요일 밤 메트라이프 스타디움 화이트아웃 경기에서 커맨더스(2-5-1)를 상대로 디비전 2차전을 치릅니다.",
            "excerpt": "부상에서 회복한 J.J. 맥카시가 정상 훈련을 소화하며 목요일 밤 워싱턴전 선발 출격을 준비하고 있습니다.",
            "body": [
                "현지시간 11월 12일 목요일 밤 8시 15분(ET, 프라임 비디오) 열리는 NFL 10주차 서스데이 나이트 풋볼에서 NFC 동부지구 선두 뉴욕 자이언츠(5승 2패 1무)가 워싱턴 커맨더스(2승 5패 1무)를 홈 메트라이프 스타디움으로 불러들입니다. 두 팀은 5주차 맞대결에서 연장 끝에 27-27로 비겼습니다.",
                "일요일 필라델피아 원정에서 2013년 이후 첫 승리(19-11)를 따낸 자이언츠는 고관절 부상을 털고 완전 훈련에 복귀한 J.J. 맥카시가 말릭 네이버스, 캠 스카테보와 호흡을 맞출 전망입니다. 한편 버펄로는 월요일 미네소타(6-2)를 23-6으로 꺾고 7승 1패를 기록했습니다."
            ]
        },
        "ar": {
            "title": "NFL الاسبوع 10 الخميس ليلا: جاينتس (5-2-1) وجيه جيه مكارثي يستضيفان كوماندرز في مواجهة الثار",
            "subtitle": "متصدر NFC الشرق يعود الى ملعب ميتلايف بقمصان بيضاء كلاسيكية بعد خمسة اسابيع من تعادلهما 27-27.",
            "excerpt": "يعود لاعب الوسط جيه جيه مكارثي للمشاركة الكاملة في التدريبات قبل مواجهة الخميس امام واشنطن كوماندرز.",
            "body": [
                "تفتتح مواجهات الاسبوع العاشر من NFL ليلة الخميس 12 نوفمبر (8:15 مساء بالتوقيت الشرقي، برايم فيديو) بلقاء داخل قسم NFC الشرق يجمع متصدر الترتيب نيويورك جاينتس (5-2-1) وضيفه واشنطن كوماندرز (2-5-1) في ملعب ميتلايف بعد خمسة اسابيع من تعادلهما 27-27 في الوقت الاضافي.",
                "عقب الفوز في فيلادلفيا 19-11 يوم الاحد، تدرب جيه جيه مكارثي بشكل كامل وبات مرشحا لبدء اللقاء مع مالك نابرز وكام سكاتيبو. وفي نتيجة الاثنين السابق، رفع بافلو بيلز رصيده الى 7-1 بفوزه على مينيسوتا فايكنغز (6-2) بنتيجة 23-6."
            ]
        }
    },
    "uwcl-md4-bayern-beat-psg-real-madrid-cruises-2026": {
        "fr": {
            "title": "UWCL J4 : le Bayern bat le PSG 2-1 a Paris avant Juventus-OL Lyonnes ce soir et Barcelone-Arsenal jeudi",
            "subtitle": "Klara Buhl marque au Parc des Princes, le Real Madrid domine le Paris FC 3-0 et Chelsea bute a Goteborg (0-0).",
            "excerpt": "Le Bayern Munich s'est impose 2-1 sur la pelouse du PSG mardi soir en Ligue des champions feminine avant le choc de Biella ce mercredi.",
            "body": [
                "La quatrieme journee de la Ligue des champions feminine a souri mardi 10 novembre au Bayern Munich, vainqueur 2-1 au Parc des Princes face au Paris Saint-Germain. Apres un but contre son camp de Katarzyna Kiedrzynek (29e) puis un tir precis de Klara Buhl (40e), le penalty de Paulina Dudek (65e) n'a pas suffi a faire douter les Bavaroises.",
                "Dans les autres rencontres de mardi, le Real Madrid a battu le Paris FC 3-0 apres la pause (Caruso, Beerensteyn, Caicedo) tandis que Chelsea a tire 28 fois sans marquer a BK Hacken (0-0). Ce mercredi 11 novembre : OH Leuven-HB Koge (17h45 UTC) puis Juventus-OL Lyonnes (20h00 UTC), avant Barcelone-Arsenal jeudi (18h45 CET) et la reprise de la Ligue des nations."
            ]
        },
        "es": {
            "title": "UWCL J4: el Bayern asalta al PSG (1-2) y el Real Madrid golea antes de Juventus-OL Lyonnes hoy",
            "subtitle": "Klara Buhl decide en el Parque de los Principes, las blancas superan 3-0 al Paris FC y Barcelona-Arsenal pasa al jueves.",
            "excerpt": "El Bayern Munich vencio 2-1 en Paris y el Real Madrid brillo en la segunda mitad, mientras la Juventus recibe hoy al Lyon en Biella.",
            "body": [
                "El Bayern Munich sumo una valiosa victoria por 2-1 a domicilio ante el Paris Saint-Germain el martes 10 de noviembre en el Parque de los Principes en la cuarta jornada de la UWCL. Un autogol de Katarzyna Kiedrzynek (29') y un tanto de Klara Buhl (40') dieron dos goles de ventaja al conjunto aleman antes del penalti de Paulina Dudek en el 65'.",
                "En el resto del martes, el Real Madrid vencio 3-0 al Paris FC con goles en la reanudacion de Caruso, Beerensteyn y Linda Caicedo, mientras el Chelsea empato 0-0 ante el BK Hacken pese a sus 28 disparos. Hoy miercoles 11 juegan OH Leuven-HB Koge (17:45 UTC) y Juventus-OL Lyonnes (20:00 UTC); Barcelona-Arsenal sera el jueves a las 18:45 CET."
            ]
        },
        "de": {
            "title": "UWCL Spieltag 4: Bayern siegt 2:1 in Paris vor Juventus gegen OL Lyonnes heute Abend",
            "subtitle": "Klara Buhl trifft im Prinzenpark, Real Madrid schlaegt Paris FC 3:0 und Chelsea remisiert trotz 28 Schuessen torlos.",
            "excerpt": "Der FC Bayern gewinnt 2:1 bei PSG, ehe die Frauen-Champions-League am Mittwochabend in Biella und am Donnerstag in Barcelona weitergeht.",
            "body": [
                "Der FC Bayern Muenchen hat am Dienstag, 10. November, am 4. Spieltag der UEFA Women's Champions League einen 2:1-Auswaertssieg bei Paris Saint-Germain gefeiert. Nach einem Eigentor von Katarzyna Kiedrzynek (29.) erhoehte Klara Buhl (40.), ehe Paulina Dudek in der 65. Minute per Elfmeter fuer PSG verkuerzte.",
                "Am selben Abend siegte Real Madrid mit 3:0 gegen den Paris FC (Tore durch Caruso, Beerensteyn und Linda Caicedo), waehrend Chelsea beim BK Hacken trotz 28 Abschluessen nicht ueber ein 0:0 hinauskam. Heute (11. November) spielen OH Leuven gegen HB Koge (17:45 UTC) sowie Juventus gegen OL Lyonnes (20:00 UTC); Barcelona gegen Arsenal steigt am Donnerstag."
            ]
        },
        "it": {
            "title": "UWCL 4a giornata: Bayern espugna Parigi 2-1, Real Madrid cala il tris prima di Juventus-OL Lyonnes",
            "subtitle": "Klara Buhl firma il successo bavarese al Parco dei Principi, Chelsea sullo 0-0 ad Hacken e stasera tocca alle bianconere.",
            "excerpt": "Martedi vittorioso per il Bayern sul PSG e per il Real sul Paris FC; stasera Juventus Women ospita l'OL Lyonnes a Biella alle 21:00.",
            "body": [
                "Il Bayern Monaco si e imposto 2-1 sul campo del Paris Saint-Germain martedi 10 novembre al Parco dei Principi nella quarta giornata della UEFA Women's Champions League. L'autorete di Katarzyna Kiedrzynek al 29' e la rete di Klara Buhl al 40' hanno indirizzato la gara prima del rigore di Paulina Dudek al 65'.",
                "Nelle altre sfide del martedi il Real Madrid ha superato 3-0 il Paris FC con reti nella ripresa di Caruso, Beerensteyn e Linda Caicedo, mentre il Chelsea si e fermato sullo 0-0 contro l'Hacken nonostante 28 tiri. Stasera (11 novembre) spazio a OH Leuven-HB Koge (18:45 CET) e Juventus-OL Lyonnes (21:00 CET a Biella), poi giovedi Barcellona-Arsenal."
            ]
        },
        "pl": {
            "title": "UWCL 4. kolejka: Bayern wygrywa z PSG 2-1 w Paryzu przed wieczornym hitem Juventus - OL Lyonnes",
            "subtitle": "Klara Buhl trafia na Parc des Princes, Real Madryt ogrywa Paris FC 3-0, a Chelsea oddaje 28 strzalow w remisie 0-0.",
            "excerpt": "Bayern Monachium zwyciezyl we wtorek 2-1 w Paryzu, a juz w srode o 21:00 CET Juventus zmierzy sie w Bielli z OL Lyonnes.",
            "body": [
                "Bayern Monachium zdobyl cenne wyjazdowe punkty we wtorek 10 listopada, pokonujac Paris Saint-Germain 2-1 na Parc des Princes w 4. kolejce Ligi Mistrzyn UEFA. Po samobojczym trafieniu Katarzyny Kiedrzynek w 29. minucie wynik podwyzszyla Klara Buhl (40.), a dla gospodyn z rzutu karnego trafila Paulina Dudek (65.).",
                "W pozostalych wtorkowych meczach Real Madryt wygral z Paris FC 3-0 po golach Caruso, Beerensteyn i Caicedo w drugiej polowie, zas Chelsea zremisowala 0-0 z BK Hacken mimo 28 strzalow. W srode zagraja OH Leuven z HB Koge (17:45 UTC) oraz Juventus z OL Lyonnes (20:00 UTC), a w czwartek Barcelona z Arsenalem."
            ]
        },
        "zh": {
            "title": "女足欧冠第4轮：拜仁客场2-1击败大巴黎，今晚尤文迎战里昂、周四巴萨对决阿森纳",
            "subtitle": "克拉拉·布尔建功助拜仁在王子公园取胜，皇马3-0完胜巴黎FC，切尔西28脚射门0-0平赫根。",
            "excerpt": "拜仁周二晚2-1客胜巴黎圣日耳曼，今夜聚焦尤文图斯女足对阵里昂，周四诺坎普将上演巴萨迎战阿森纳。",
            "body": [
                "北京时间周三凌晨（当地时间11月10日晚），2026/27赛季女足欧冠联赛阶段第4轮打响焦点战，拜仁慕尼黑客场2-1力克巴黎圣日耳曼。第29分钟基德日内克自摆乌龙，第40分钟克拉拉·布尔破门助拜仁两球领先，巴黎仅由杜德克第65分钟点射追回一城。",
                "同日皇马凭借卡鲁索、贝伦斯泰因与琳达·凯塞多的下半场进球3-0轻取巴黎FC，切尔西狂轰28脚却0-0闷平赫根。本周三（11日）迎来奥德赫维里vs克厄（17:45 UTC）和尤文图斯vs里昂（20:00 UTC），受西班牙大罢工影响推迟一天的巴萨vs阿森纳将于周四（12日）18:45 CET打响。"
            ]
        },
        "ja": {
            "title": "UWCL第4節：バイエルンがパリでPSGを2-1撃破、今夜はユヴェントス対リヨン、木曜バルサ対アーセナル",
            "subtitle": "ビュール弾でバイエルン勝利、レアル・マドリードは3-0快勝、チェルシーはシュート28本もスコアレスドロー。",
            "excerpt": "火曜夜のパルク・デ・プランスでバイエルンが2-1で競り勝ち、水曜夜はユヴェントス対OLリヨンヌ、木曜はカンプ・ノウ決戦へ続く。",
            "body": [
                "11月10日火曜のUEFA女子チャンピオンズリーグ第4節で、バイエルン・ミュンヘンがアウェーのパルク・デ・プランスでパリ・サンジェルマンを2-1で下した。29分のオウンゴールで先制したバイエルンは40分にクララ・ビュールが加点し、65分のドゥデクのPKによる反撃をしのいだ。",
                "同日の他会場ではレアル・マドリードが後半のカルーソ、ベーレンシュタイン、カイセドの得点でパリFCに3-0で勝利。チェルシーはヘッケン戦に28本のシュートを浴びせながら0-0に終わった。水曜（11日）はルーヴェン対キューゲ（17:45 UTC）とユヴェントス対OLリヨンヌ（20:00 UTC）、木曜（12日）はバルセロナ対アーセナルが行われる。"
            ]
        },
        "ko": {
            "title": "UWCL 4차전: 바이에른, 파리 원정 2-1 승… 오늘 밤 유벤투스-리옹전 이어 목요일 바르셀로나-아스널 격돌",
            "subtitle": "클라라 뷜 추가골로 바이에른 승리, 레알 마드리드는 파리 FC 3-0 완파, 첼시는 슈팅 28개 속 0-0 무승부.",
            "excerpt": "화요일 밤 파리에서 바이에른 뮌헨이 2-1 승리를 거뒀고, 수요일 밤에는 비엘라에서 유벤투스와 OL 리옹이 맞붙습니다.",
            "body": [
                "바이에른 뮌헨이 11월 10일 화요일 파르크 데 프랭스에서 열린 UEFA 여자 챔피언스리그(UWCL) 4차전 원정 경기에서 파리 생제르맹(PSG)을 2-1로 꺾었습니다. 전반 29분 자책골과 40분 클라라 뷜의 연속골로 앞선 바이에른은 후반 20분 파울리나 두데크의 페널티킥 만회골을 버텨냈습니다.",
                "같은 날 레알 마드리드는 카루소, 베렌스테인, 카이세도의 후반 릴레이 골로 파리 FC를 3-0으로 완파했고, 첼시는 28개의 슈팅에도 해켄과 0-0으로 비겼습니다. 11일 수요일에는 뢰벤-코게(17:45 UTC)와 유벤투스-OL 리옹(20:00 UTC)이 열리며, 목요일(12일)에는 바르셀로나와 아스널이 캄프 누에서 맞붙습니다."
            ]
        },
        "ar": {
            "title": "دوري ابطال اوروبا للسيدات الجولة 4: بايرن يهزم باريس 2-1 قبل مواجهة يوفنتوس وليون الليلة وبرشلونة وارسنال غدا",
            "subtitle": "كلارا بول تسجل في بارك دي برينس وريال مدريد يهزم باريس اف سي 3-0 وتشيلسي يكتفي بالتعادل السلبي رغم 28 تسديدة.",
            "excerpt": "حقق بايرن ميونخ انتصارا ثمينا خارج ارضه على باريس سان جيرمان 2-1 ليلة الثلاثاء قبل استكمال الجولة اليوم الاربعاء.",
            "body": [
                "نجح بايرن ميونخ في العودة بفوز ثمين 2-1 من ملعب بارك دي برينس امام باريس سان جيرمان مساء الثلاثاء 10 نوفمبر في الجولة الرابعة من دوري ابطال اوروبا للسيدات. وتقدم بايرن بهدف عكسي من كاتارزينا كيدرينيك (29) واضافت كلارا بول الثاني (40) قبل ان تقلص باولينا دوديك من ركلة جزاء (65).",
                "في بقية مباريات الثلاثاء، تغلب ريال مدريد على باريس اف سي 3-0 في الشوط الثاني باهداف كاروسو وبيرنشتاين وكايسيدو، بينما تعادل تشيلسي 0-0 امام هاكن رغم 28 تسديدة. وتستكمل الجولة اليوم الاربعاء بمباراتي لوفين ضد كوغه (17:45 UTC) ويوفنتوس ضد ليون (20:00 UTC)، على ان تقام قمة برشلونة وارسنال غدا الخميس."
            ]
        }
    },
    "atp-stockholm-open-2026-musetti-rune-advance-turin-draw-next": {
        "fr": {
            "title": "ATP Stockholm : Lorenzo Musetti et Holger Rune filent sans trembler avant le tirage de Turin jeudi",
            "subtitle": "L'Italien bat Toby Samuel 6-1, 6-4 et le Danois ecarte Zizou Bergs 6-3, 6-4 a la veille du tirage des Nitto ATP Finals.",
            "excerpt": "Musetti et Rune brillent a Stockholm tandis que les huit qualifies de Turin attendent le tirage au sort officiel jeudi a 12h00 CET.",
            "body": [
                "Lorenzo Musetti, tete de serie numero 3 a Stockholm, n'a laisse que cinq jeux a Toby Samuel (6-1, 6-4) mardi 10 novembre en huitiemes de finale au Kungliga Tennishallen. L'ancien champion Holger Rune s'est egalement impose en deux manches face a Zizou Bergs (6-3, 6-4), tout comme Ugo Humbert devant Adolfo Daniel Vallejo (6-4, 6-3) lundi.",
                "Alex Michelsen (6-3, 6-2), Alejandro Tabilo (7-6, 2-6, 7-5) et Miomir Kecmanovic (7-6(4), 4-6, 6-4) ont egalement valide leur billet avant le tirage au sort officiel des Nitto ATP Finals de Turin ce jeudi 12 novembre a 12h00 CET entre Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe et Rafael Jodar."
            ]
        },
        "es": {
            "title": "ATP Estocolmo: Lorenzo Musetti y Holger Rune avanzan con firmeza antes del sorteo de Turin el jueves",
            "subtitle": "El italiano derrota 6-1 y 6-4 a Toby Samuel y Rune supera a Zizou Bergs 6-3 y 6-4 rumbo a las Nitto ATP Finals.",
            "excerpt": "Musetti y Rune cumplen en pista cubierta en Suecia en la vispera del sorteo de grupos del torneo de maestros este jueves a las 12:00 CET.",
            "body": [
                "El tercer cabeza de serie Lorenzo Musetti apenas cedio cinco juegos el martes 10 de noviembre ante Toby Samuel (6-1, 6-4) en los octavos de final del Abierto de Estocolmo. Holger Rune tambien abrio con solvencia al batir 6-3 y 6-4 a Zizou Bergs, tras el triunfo de Ugo Humbert por 6-4 y 6-3 el lunes sobre Adolfo Daniel Vallejo.",
                "Alex Michelsen (6-3, 6-2), Alejandro Tabilo (7-6, 2-6, 7-5) y Miomir Kecmanovic (7-6(4), 4-6, 6-4) completaron las victorias confirmadas antes de la gran cita de mañana: el sorteo de las Nitto ATP Finals en Turin (jueves 12, 12:00 CET) con Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe y Jodar."
            ]
        },
        "de": {
            "title": "ATP Stockholm: Musetti und Rune siegen souveraen vor der Turin-Auslosung am Donnerstag",
            "subtitle": "Musetti schlaegt Toby Samuel 6:1, 6:4 und Rune bezwingt Zizou Bergs 6:3, 6:4 vor der Nitto ATP Finals Gruppenauslosung.",
            "excerpt": "Klare Zweisatzsiege fuer Lorenzo Musetti und Holger Rune in Schweden einen Tag vor der Auslosung in Turin um 12:00 Uhr MEZ.",
            "body": [
                "Der an Position drei gesetzte Lorenzo Musetti gab am Dienstag, 10. November, in Stockholm nur fuenf Spiele ab und besiegte Toby Samuel im Achtelfinale mit 6:1, 6:4. Auch Holger Rune startete mit einem 6:3, 6:4 gegen den an acht gesetzten Zizou Bergs souveraen, nachdem Ugo Humbert am Montag Adolfo Daniel Vallejo mit 6:4, 6:3 geschlagen hatte.",
                "Zudem feierten Alex Michelsen (6:3, 6:2), Alejandro Tabilo (7:6, 2:6, 7:5) und Miomir Kecmanovic (7:6(4), 4:6, 6:4) sichere Siege, bevor sich am Donnerstag um 12:00 Uhr MEZ alles auf Turin richtet: Bei der Auslosung der Nitto ATP Finals warten Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe und Rafael Jodar auf ihre Gruppen."
            ]
        },
        "it": {
            "title": "ATP Stoccolma: Lorenzo Musetti e Holger Rune volano avanti prima del sorteggio di Torino",
            "subtitle": "L'azzurro regola Toby Samuel 6-1, 6-4 e Rune supera Bergs 6-3, 6-4 alla vigilia della cerimonia per le Nitto ATP Finals.",
            "excerpt": "Musetti concede appena cinque game a Stoccolma mentre giovedi alle 12:00 CET verra sorteggiato il tabellone delle Finals di Torino.",
            "body": [
                "Terza testa di serie al Kungliga Tennishallen, Lorenzo Musetti ha liquidato martedi 10 novembre Toby Samuel per 6-1, 6-4 negli ottavi dell'ATP 250 di Stoccolma. Successi netti in due set anche per Holger Rune contro Zizou Bergs (6-3, 6-4) e per Ugo Humbert su Adolfo Daniel Vallejo (6-4, 6-3).",
                "Vittorie confermate inoltre per Alex Michelsen (6-3, 6-2), Alejandro Tabilo (7-6, 2-6, 7-5) e Miomir Kecmanovic (7-6(4), 4-6, 6-4), mentre cresce l'attesa per giovedi 12 novembre alle 12:00 CET: il sorteggio dei gironi delle Nitto ATP Finals a Torino tra Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe e Rafael Jodar."
            ]
        },
        "pl": {
            "title": "ATP Sztokholm: Lorenzo Musetti i Holger Rune pewnie zwyciezaja przed czwartkowym losowaniem w Turynie",
            "subtitle": "Wloch pokonuje Toby'ego Samuela 6-1, 6-4, a Rune ogrywa Zizou Bergsa 6-3, 6-4 na dzien przed losowaniem Nitto ATP Finals.",
            "excerpt": "Musetti stracil tylko piec gemow w Sztokholmie, a juz w czwartek o 12:00 CET poznamy grupy turnieju mistrzow w Turynie.",
            "body": [
                "Rozstawiony z numerem trzecim Lorenzo Musetti we wtorek 10 listopada pewnie wygral z Tobym Samuelem 6-1, 6-4 w 1/8 finalu halowego turnieju ATP 250 w Sztokholmie. Bez straty seta awansowal tez Holger Rune przeciwko Zizou Bergsowi (6-3, 6-4) oraz Ugo Humbert po wygranej 6-4, 6-3 z Vallejo.",
                "Swoje mecze rozstrzygneli rowniez Alex Michelsen (6-3, 6-2), Alejandro Tabilo (7-6, 2-6, 7-5) i Miomir Kecmanovic (7-6(4), 4-6, 6-4). Uwaga kibicow przenosi sie juz na czwartek 12 listopada o 12:00 CET, kiedy Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe i Rafael Jodar poznaja rywali w Nitto ATP Finals w Turynie."
            ]
        },
        "zh": {
            "title": "ATP斯德哥尔摩：穆塞蒂6-1、6-4携鲁内晋级，周四聚焦都灵年终总决赛抽签",
            "subtitle": "三号种子穆塞蒂横扫萨缪尔，鲁内两盘淘汰贝尔格斯，周四中午12点都灵将揭晓年终分组。",
            "excerpt": "穆塞蒂仅丢五局闯入斯德哥尔摩八强，网坛目光已锁定周四12:00 CET都灵Nitto ATP年终总决赛抽签仪式。",
            "body": [
                "11月10日周二在斯德哥尔摩室内硬地赛场上，3号种子洛伦佐·穆塞蒂以6-1、6-4干脆击败托比·萨缪尔晋级八强。前赛会冠军霍尔格·鲁内以6-3、6-4击败8号种子齐祖·贝尔格斯，周一乌戈·安贝尔也以6-4、6-3取胜。",
                "此外亚历克斯·米歇尔森（6-3、6-2）、塔比洛与凯茨马诺维奇均顺利过关。男子网坛即将迎来本周四11月12日中午12:00 CET的重头戏：都灵2026 Nitto ATP年终总决赛分组抽签，兹韦列夫、阿尔卡拉斯、谢尔顿、梅德韦杰夫、科博利、菲斯、蒂亚福与拉斐尔·霍达尔静候分组结果。"
            ]
        },
        "ja": {
            "title": "ATPストックホルム：ムゼッティとルーネが快勝、木曜はトリノNitto ATPファイナルズの抽選会へ",
            "subtitle": "第3シードのムゼッティが6-1, 6-4で快勝し、ルーネもストレート勝ち。12日12:00 CETにトリノ組合せ抽選が行われる。",
            "excerpt": "ムゼッティがわずか5ゲームしか与えずベスト8へ進出。男子テニス界は木曜昼のトリノ年終大会ドロー発表に注目が集まる。",
            "body": [
                "11月10日火曜のストックホルム・オープン2回戦で、第3シードのロレンツォ・ムゼッティがトビー・サミュエルを6-1, 6-4のストレートで下し準々決勝へ進出した。元覇者ホルガ・ルーネもジズー・ベルグスに6-3, 6-4で快勝し、ウーゴ・アンベールも6-4, 6-3で勝ち上がっている。",
                "さらにミケルセン（6-3, 6-2）やタビロ、ケツマノビッチも勝利を収め、男子ツアーの注目は木曜11月12日12:00 CETに行われるトリノNitto ATPファイナルズ（15〜22日）のドローへ。ズベレフ、アルカラス、シェルトン、メドベージェフ、コボリ、フィス、ティアフォー、ジョダールが組分けを待つ。"
            ]
        },
        "ko": {
            "title": "ATP 스톡홀름: 무세티·루네 완승으로 순항… 목요일 토리노 ATP 파이널스 조 추첨 임박",
            "subtitle": "무세티가 토비 새뮤얼을 6-1, 6-4로 제압하고 루네도 2-0 승리를 거두며 토리노 왕중왕전 추첨 전초전을 장식했습니다.",
            "excerpt": "스톡홀름에서 무세티와 루네가 깔끔한 승리를 챙긴 가운데, 12일 12시 CET 토리노 파이널스 공식 대진 추첨이 진행됩니다.",
            "body": [
                "11월 10일 화요일 스톡홀름 오픈 16강에서 3번 시드 로렌초 무세티가 토비 새뮤얼을 6-1, 6-4로 완파하며 8강에 선착했습니다. 전 챔피언 홀거 루네 역시 지주 베르흐스를 6-3, 6-4로 꺾었고, 위고 엄베르도 6-4, 6-3으로 1회전을 통과했습니다.",
                "알렉스 미켈슨(6-3, 6-2), 타빌로, 케츠마노비치도 승리를 보탠 가운데, 남자 테니스의 시선은 11월 12일 목요일 12:00 CET(동부 오전 6시) 열리는 토리노 니토 ATP 파이널스 공식 조 추첨으로 향합니다. 즈베레프, 알카라스, 셸턴, 메드베데프, 코볼리, 피스, 티아포, 호다르 8인이 대진표를 받아듭니다."
            ]
        },
        "ar": {
            "title": "تنس ستوكهولم: موسيتي وروني يتاهلان بثبات قبيل قرعة نهائيات تورينو يوم الخميس",
            "subtitle": "الايطالي يهزم توبي صامويل 6-1 و6-4 وروني يتخطى بيرغز 6-3 و6-4 عشية قرعة نهائيات نيتو الختامية.",
            "excerpt": "موسيتي وروني يواصلان التقدم في السويد فيما يترقب الثمانية المتاهلون قرعة مجموعات تورينو غدا الخميس عند الساعة 12:00 بتوقيت وسط اوروبا.",
            "body": [
                "حجز الايطالي لورينزو موسيتي المصنف ثالثا مقعده في ربع نهائي بطولة ستوكهولم المفتوحة يوم الثلاثاء 10 نوفمبر بفوزه السهل على توبي صامويل 6-1 و6-4. كما تفوق البطل السابق هولغر روني على زيزو بيرغز 6-3 و6-4 بعد فوز اوغو اومبير على فاييخو 6-4 و6-3.",
                "كما سجل ميكيلسن (6-3 و6-2) وتابيلو وكيتسمانوفيتش انتصارات مؤكدة قبل الموعد المنتظر غدا الخميس 12 نوفمبر الساعة 12:00 ظهرا بتوقيت وسط اوروبا لقرعة نهائيات نيتو ATP في تورينو بمشاركة زفيريف والكاراز وشيلتون ومدفيديف وكوبولي وفيلس وتيافو وجودار."
            ]
        }
    },
    "dp-world-tour-championship-2026-mcilroy-chacarra-dubai-preview": {
        "fr": {
            "title": "DP World Tour Championship : Rory McIlroy associe au leader Eugenio Chacarra des le 1er tour a Dubai",
            "subtitle": "Separes par 533,93 points a la Race to Dubai, les deux hommes partent ensemble jeudi a 12h40 locale pour 3 millions de dollars.",
            "excerpt": "Avec 533,93 points d'avance, Eugenio Chacarra jouera les deux premiers tours face a Rory McIlroy a Jumeirah Golf Estates des jeudi.",
            "body": [
                "La finale de la saison sur le circuit europeen debute jeudi 12 novembre sur l'Earth Course de Jumeirah Golf Estates a Dubai avec une derniere partie royale a 12h40 heure locale (8h40 GMT) : le leader Eugenio Chacarra (4 243,79 pts) face a son dauphin Rory McIlroy (3 709,86 pts).",
                "Avec 2 000 points pour le vainqueur (10 M$ de dotation dont 3 M$ au champion), Chacarra sera assure du titre en cas de victoire a Dubai apres ses trois succes en 2026. Vainqueur du Masters 2026 et troisieme a Abu Dhabi la semaine derniere, McIlroy vise un huitieme trophee Harry Vardon pour egaler le record de Colin Montgomerie. En PGA Tour, Blades Brown reste sur son triomphe historique (-23, 265) a Cabo avant l'Austin Championship."
            ]
        },
        "es": {
            "title": "DP World Tour Championship: Eugenio Chacarra defiende el trono junto a Rory McIlroy en Dubai",
            "subtitle": "Separados por 533,93 puntos en la Race to Dubai, lider y segundo saldran juntos el jueves a las 12:40 hora local.",
            "excerpt": "El espanol Eugenio Chacarra (4.243,79 puntos) y Rory McIlroy (3.709,86) forman el partido estelar del jueves en Jumeirah Golf Estates.",
            "body": [
                "El DP World Tour Championship arranca este jueves 12 de noviembre en el Earth Course de Jumeirah Golf Estates con el duelo directo que esperaba el golf europeo: el lider Eugenio Chacarra (4.243,79 puntos, tres victorias en 2026) compartira el ultimo partido de las 12:40 GST (8:40 GMT) junto a Rory McIlroy (3.709,86).",
                "Con 2.000 puntos y 3 millones de dolares para el ganador, el triunfo en Dubai garantiza el titulo a Chacarra pase lo que pase. El campeon del Masters 2026 McIlroy supero a Patrick Reed la semana pasada en Abu Dabi y persigue su octavo trofeo Harry Vardon para igualar el record de Colin Montgomerie. En el PGA Tour, Blades Brown (-23, 265) dejo marca centenaria en Cabo antes de Austin."
            ]
        },
        "de": {
            "title": "DP World Tour Championship: Rory McIlroy startet in Dubai im Top-Flight mit Eugenio Chacarra",
            "subtitle": "Nur 533,93 Punkte trennen beide im Race to Dubai vor dem ersten Abschlag am Donnerstag um 12:40 Uhr Ortszeit.",
            "excerpt": "Spitzenreiter Eugenio Chacarra (4.243,79 Punkte) und Masters-Sieger Rory McIlroy (3.709,86) gehen in Dubai am Donnerstag gemeinsam auf die Runde.",
            "body": [
                "Beim Saisonfinale in Dubai beginnt am Donnerstag, 12. November, auf dem Earth Course der direkte Kampf um die Jahreswertung: Race-to-Dubai-Spitzenreiter Eugenio Chacarra (4.243,79 Punkte, drei Saisonsiege) spielt im letzten Flight um 12:40 Uhr Ortszeit (8:40 GMT) gemeinsam mit Rory McIlroy (3.709,86 Punkte).",
                "Mit 2.000 Punkten und drei Millionen US-Dollar Preisgeld fuer den Sieger macht ein Triumph in Dubai Chacarra sicher zum Gesamtsieger. McIlroy zog vergangene Woche als Dritter in Abu Dhabi an Patrick Reed vorbei und jagt die achte Harry Vardon Trophy, um mit Colin Montgomerie gleichzuziehen. Auf der PGA Tour folgt nach Blades Browns Playoff-Coup (-23, 265) nun Austin."
            ]
        },
        "it": {
            "title": "DP World Tour Championship: McIlroy e il leader Chacarra subito insieme nel giro d'apertura a Dubai",
            "subtitle": "Separati da 533,93 punti nella Race to Dubai, i primi due del ranking partono giovedi alle 12:40 locali.",
            "excerpt": "Eugenio Chacarra (4.243,79 punti) difende il primato al fianco di Rory McIlroy (3.709,86) al Jumeirah Golf Estates per 3 milioni di dollari.",
            "body": [
                "Il gran finale stagionale di Dubai scatta giovedi 12 novembre sull'Earth Course del Jumeirah Golf Estates con l'ultimo flight affidato ai protagonisti del titolo: il leader Eugenio Chacarra (4.243,79 punti) e Rory McIlroy (3.709,86) prenderanno il via insieme alle 12:40 locali (8:40 GMT).",
                "Con 2.000 punti in palio e 3 milioni di dollari per il vincitore, una vittoria consegnerebbe matematicamente la Race to Dubai a Chacarra. Il campione del Masters 2026 McIlroy ha scavalcato Patrick Reed grazie al terzo posto di Abu Dhabi e insegue l'ottavo Harry Vardon Trophy per eguagliare Colin Montgomerie."
            ]
        },
        "pl": {
            "title": "DP World Tour Championship: Rory McIlroy zagra w grupie lidera Eugenio Chacarry juz od czwartku w Dubaju",
            "subtitle": "Roznica 533,93 pkt w Race to Dubai i wspolny tee time o 12:40 czasu lokalnego otwieraja wielki final o 3 mln dolarow.",
            "excerpt": "Lider cyklu Eugenio Chacarra (4243,79 pkt) i Rory McIlroy (3709,86) wyjda razem na pole Earth Course w czwartkowe poludnie.",
            "body": [
                "Finał sezonu DP World Tour rusza w czwartek 12 listopada na polu Earth Course w Jumeirah Golf Estates w Dubaju od wymarzonej ostatniej grupy o 12:40 czasu lokalnego (8:40 GMT): lider Race to Dubai Eugenio Chacarra (4243,79 pkt) zagra bezposrednio z drugim Rorym McIlroyem (3709,86 pkt).",
                "Zwyciezca turnieju zgarnie 2000 punktow oraz 3 mln dolarow z puli 10 mln. Wygrana w Dubaju zapewni Chacarrze triumf w calym cyklu po trzech tytulach w 2026 roku, podczas gdy mistrz Masters McIlroy po wyprzedzeniu Patricka Reeda walczy o osme trofeum Harry'ego Vardona i wyrownanie rekordu Colina Montgomeriego."
            ]
        },
        "zh": {
            "title": "DP世界巡回锦标赛前瞻：麦克罗伊周四首轮同组领跑者查卡拉决战迪拜",
            "subtitle": "迪拜竞赛榜首仅差533.93分，前两位周四当地时间12:40携手出发，争夺300万美元冠军奖金与年度总冠军。",
            "excerpt": "西班牙人尤金尼奥·查卡拉（4,243.79分）与罗里·麦克罗伊（3,709.86分）周四将在朱美拉高尔夫庄园同组挥杆。",
            "body": [
                "北京时间周四（11月12日）当地时间12:40（格林尼治时间08:40），DP世界巡回锦标赛将在迪拜朱美拉高尔夫庄园土球场迎来激动人心的首轮焦点组对决：迪拜竞赛领头羊尤金尼奥·查卡拉（4,243.79分，2026赛季三冠王）与第二名罗里·麦克罗伊（3,709.86分）同组出发。",
                "本站总奖金1000万美元（冠军独享300万美元及2000个积分）。只要在迪拜夺冠，查卡拉即可直接锁定年度总冠军；上周在阿布扎比获得第三从而反超帕特里克·里德的2026大师赛冠军麦克罗伊则须全力争冠，力争追平科林·蒙哥马利八夺哈里·瓦顿奖杯的历史纪录。"
            ]
        },
        "ja": {
            "title": "DPワールドツアー選手権：マキロイが木曜初日から首位チャカラと同組対決、年間王者を懸けドバイへ",
            "subtitle": "レース・トゥ・ドバイの差は533.93ポイント。現地木曜12:40発の最終組で直接対決し、優勝賞金300万ドルと2,000ptを争う。",
            "excerpt": "年間1位のチャカラ（4,243.79pt）とマスターズ覇者マキロイ（3,709.86pt）が木曜アースコースで直接激突する。",
            "body": [
                "木曜11月12日、ドバイのジュメイラ・ゴルフエステーツ（アースコース）で開幕するDPワールドツアー選手権の第1ラウンド最終組（現地12:40 / 08:40 GMT）で、レース・トゥ・ドバイ首位エウヘニオ・チャカラ（4,243.79pt）と2位ロリー・マキロイ（3,709.86pt）が同組で回る。",
                "優勝者に2,000ptと賞金300万ドル（総額1,000万ドル）が与えられる最終戦。今季3勝のチャカラはドバイ優勝で年間タイトルが確定し、先週アブダビ3位でパトリック・リードを抜いたマスターズ王者マキロイは、コリン・モンゴメリーの歴代最多8度目となるハリー・バードン・トロフィーに並べるか挑む。"
            ]
        },
        "ko": {
            "title": "DP 월드투어 챔피언십: 맥길로이, 선두 차카라와 목요일 1라운드 동반 플레이… 두바이 최종 격돌",
            "subtitle": "레이스 투 두바이 533.93점 차의 두 톱랭커가 목요일 낮 12시 40분(현지) 마지막 조에서 우승 상금 300만 달러를 놓고 맞붙습니다.",
            "excerpt": "연간 랭킹 1위 에우헤니오 차카라(4,243.79점)와 2위 로리 맥길로이(3,709.86점)가 목요일 어스 코스에서 1라운드를 출발합니다.",
            "body": [
                "11월 12일 목요일 두바이 주메이라 골프 에스테이츠 어스 코스에서 개막하는 시즌 최종전 DP 월드투어 챔피언십 1라운드 마지막 조(현지시간 12:40, 08:40 GMT)에서 레이스 투 두바이 1위 에우헤니오 차카라(4,243.79점)와 2위 로리 맥길로이(3,709.86점)가 동반 라운드를 펼칩니다.",
                "우승 포인트 2,000점과 총상금 1,000만 달러(우승 상금 300만 달러)가 걸린 최종전에서 올 시즌 3승을 거둔 차카라는 두바이 우승 시 자력으로 연간 왕좌를 확정합니다. 지난주 아부다비 3위로 패트릭 리드를 제친 마스터스 챔피언 맥길로이는 콜린 몽고메리의 역대 최다 8회 해리 바든 트로피 타이 기록에 도전합니다."
            ]
        },
        "ar": {
            "title": "بطولة جولة دي بي ورلد دبي: ماكلروي يبدأ الجولة الاولى برفقة المتصدر تشاكارا الخميس",
            "subtitle": "بفارق 533.93 نقطة في السباق الى دبي، ينطلق الثنائي معا في المجموعة الاخيرة الساعة 12:40 ظهرا بتوقيت دبي.",
            "excerpt": "يخوض المتصدر الاسباني اوجينيو تشاكارا (4243.79 نقطة) جولة الخميس الافتتاحية جنبا الى جنب مع روري ماكلروي على ارض جميرا غولف.",
            "body": [
                "تنطلق البطولة الختامية لجولة دي بي ورلد يوم الخميس 12 نوفمبر على ملعب Earth في جميرا غولف إستيتس بدبي بمواجهة مباشرة في المجموعة الاخيرة عند الساعة 12:40 بتوقيت الامارات (08:40 غرينتش)، بين متصدر السباق الى دبي اوجينيو تشاكارا (4243.79 نقطة) وملاحقه روري ماكلروي (3709.86 نقطة).",
                "ومع رصد 2000 نقطة وجائزة كبرى بقيمة 3 ملايين دولار للبطل من مجموع جوائز 10 ملايين، سيضمن تشاكارا اللقب السنوي تلقائيا اذا توج في دبي. اما بطل الماسترز 2026 ماكلروي، الذي تخطى باتريك ريد في ابوظبي الاسبوع الماضي، فيبحث عن تتويجه الثامن لمعادلة الرقم القياسي لكولين مونتغمري."
            ]
        }
    },
    "f1-sao-paulo-aftermath-verstappen-charge-las-vegas-preview-2026": {
        "fr": {
            "title": "F1 avant Las Vegas : cinq pilotes en 33 points derriere le champion Kimi Antonelli",
            "subtitle": "Norris s'impose a Sao Paulo et Mercedes scelle le titre constructeurs (652), laissant une lutte intense pour la 2e place.",
            "excerpt": "Apres la pluie d'Interlagos, Max Verstappen (279) et Lando Norris (246) se tiennent en 33 points a l'approche du GP de Las Vegas (19-21 nov).",
            "body": [
                "Si Kimi Antonelli (390 pts) et Mercedes (652 pts) ont deja verrouille les deux couronnes mondiales 2026 a l'issue d'Interlagos, la route vers le Grand Prix de Las Vegas (19-21 novembre) reste sous haute tension juste derriere le leader. Vainqueur sous la pluie en 1:35:23.504, Lando Norris (246 pts) s'est rapproche a 33 longueurs du deuxieme, Max Verstappen (279 pts apres sa remontee de 21e a 2e).",
                "Entre eux deux figurent George Russell (262), Lewis Hamilton (261 pour son 400e depart, P9 au Bresil) et Charles Leclerc (249). Chez les constructeurs, Ferrari pointe deuxieme a 510 points devant Red Bull (415) et McLaren (398), separes de seulement 17 points pour la troisieme place."
            ]
        },
        "es": {
            "title": "F1 rumbo a Las Vegas: cinco pilotos en solo 33 puntos tras el campeon Kimi Antonelli",
            "subtitle": "Norris gana en Interlagos y Mercedes cierra Constructores (652), mientras Ferrari (510), Red Bull (415) y McLaren (398) pujan por el podio.",
            "excerpt": "Solo 33 puntos separan a Max Verstappen (279) de Lando Norris (246) antes de la cita nocturna en el Strip del 19 al 21 de noviembre.",
            "body": [
                "Aunque Kimi Antonelli (390 pts) y Mercedes (652 pts) ya celebran ambos campeonatos mundiales de 2026 tras Interlagos, el Gran Premio de Las Vegas (19-21 de noviembre, 50 vueltas) presenta una vibrante batalla por el subcampeonato. Lando Norris gano en Brasil bajo la lluvia (1:35:23.504) para sumar 246 puntos frente a los 279 de un Max Verstappen que remonto del 21º al 2º (+14.602s).",
                "Apenas un punto separa a George Russell (262) de Lewis Hamilton (261 tras su GP numero 400), con Charles Leclerc en 249. En Constructores, Ferrari marcha segundo con 510 puntos y Red Bull (415) defiende 17 puntos de margen frente a McLaren (398)."
            ]
        },
        "de": {
            "title": "Formel 1 vor Las Vegas: Fuenf Fahrer binnen 33 Punkten hinter Weltmeister Kimi Antonelli",
            "subtitle": "Norris gewinnt in Interlagos und Mercedes sichert die Konstrukteurs-WM (652), dahinter tobt der Kampf um Rang zwei.",
            "excerpt": "Max Verstappen (279) bis Lando Norris (246) liegen vor Las Vegas (19.-21. November) innerhalb von 33 Punkten eng beisammen.",
            "body": [
                "Obwohl Kimi Antonelli (390 Punkte) und Mercedes (652 Punkte) nach dem Regenrennen von Sao Paulo bereits als Weltmeister feststehen, bleibt die Ausgangslage vor dem Grossen Preis von Las Vegas (19.-21. November) hochspannend. Sao-Paulo-Sieger Lando Norris (246 Punkte, Siegerzeit 1:35:23.504) rueckte bis auf 33 Zaehler an den Gesamtzweiten Max Verstappen (279 Punkte nach Aufholjagd von P21 auf P2) heran.",
                "Dazwischen kaempfen George Russell (262), Lewis Hamilton (261 nach seinem 400. Grand-Prix-Start) und Charles Leclerc (249). Bei den Konstrukteuren liegt Ferrari mit 510 Punkten auf Platz zwei, waehrend Red Bull (415) nur 17 Punkte vor McLaren (398) liegt."
            ]
        },
        "it": {
            "title": "F1 verso Las Vegas: cinque piloti in 33 punti dietro al campione del mondo Kimi Antonelli",
            "subtitle": "Norris trionfa a Interlagos e Mercedes conquista i Costruttori a quota 652, con Ferrari (510) e lotta Red Bull-McLaren.",
            "excerpt": "Tra Max Verstappen secondo (279) e Lando Norris sesto (246) ci sono solo 33 punti a due gare dal termine verso Las Vegas.",
            "body": [
                "Con entrambi i titoli mondiali 2026 gia assegnati a Kimi Antonelli (390) e alla Mercedes (652 punti dopo il quarto posto di Russell e il quinto dell'italiano a Interlagos), il circus si prepara al GP di Las Vegas (19-21 novembre) con un duello apertissimo alle spalle del campione.",
                "Dopo il successo sul bagnato di San Paolo in 1:35:23.504, Lando Norris e salito a 246 punti, a 33 lunghezze da Max Verstappen (279, secondo dopo una rimonta da P21 a P2). George Russell (262), Lewis Hamilton (261 al suo 400esimo GP) e Charles Leclerc (249) restano tutti in corsa, mentre nei Costruttori Ferrari e a 510 con Red Bull (415) a +17 su McLaren (398)."
            ]
        },
        "pl": {
            "title": "F1 przed Las Vegas: piec gwiazd w 33 punktach za mistrzem swiata Kimi Antonellim",
            "subtitle": "Norris wygral w Sao Paulo, a Mercedes przypieczetowal tytul konstruktorow (652 pkt), zostawiajac zaciekla walke o drugie miejsce.",
            "excerpt": "Od Maxa Verstappena (279 pkt) do Lando Norrisa (246 pkt) rozstaw wynosi tylko 33 punkty przed nocnym wyscigiem w Las Vegas.",
            "body": [
                "Choc Kimi Antonelli (390 pkt) i Mercedes (652 pkt) zapewnili sobie juz oba tytuly mistrzowskie sezonu 2026 po deszczowym wyscigu na Interlagos, przed przedostatnia runda w Las Vegas (19-21 listopada) walka o wicemistrzostwo nabrala rumiencow.",
                "Zwyciezca GP Sao Paulo Lando Norris (1:35:23.504, 246 pkt) traci 33 punkty do drugiego Maxa Verstappena (279 pkt po awansie z 21. na 2. miejsce). George Russell (262), Lewis Hamilton (261 po 400. starcie w F1) oraz Charles Leclerc (249) mieszcza sie w scisku, a w konstruktorach Red Bull (415) wyprzedza McLarena (398) o zaledwie 17 punktow za drugim Ferrari (510)."
            ]
        },
        "zh": {
            "title": "F1拉斯维加斯前瞻：安东内利加冕后，维斯塔潘至诺里斯5人仅差33分",
            "subtitle": "诺里斯巴西夺冠、梅赛德斯652分提前卫冕车队总冠军，身后法拉利（510）、红牛（415）与迈凯伦（398）激战正酣。",
            "excerpt": "桑巴雨战过后，维斯塔潘（279）到诺里斯（246）五位车手分差仅33分，将于11月19日至21日夜战拉斯维加斯。",
            "body": [
                "尽管Kimi·安东内利（390分）与梅赛德斯（652分）在圣保罗站雨战后已双双锁定2026年F1车手与车队年度总冠军，但下周拉斯维加斯大奖赛（11月19日至21日，正赛50圈）依然看点十足：英特拉格斯冠军诺里斯（夺冠成绩1:35:23.504）积246分，距离第二名维斯塔潘（279分，正赛从第21位追至第2）仅差33分。",
                "这33分区间内还聚集着拉塞尔（262分）、迎来第400场大奖赛的汉密尔顿（261分）以及勒克莱尔（249分）。车队积分榜上法拉利积510分居次席，红牛（415分）仅领先迈凯伦（398分）17分，第三名归属仍悬而未决。"
            ]
        },
        "ja": {
            "title": "F1ラスベガスGP展望：王者アントネッリの背後、フェルスタッペンからノリスまで5人が33点差の大混戦",
            "subtitle": "サンパウロ雨戦を制したノリス、コンストラクターズ王座を決めたメルセデス（652点）に続き2位争いが白熱。",
            "excerpt": "ブラジルGP後のドライバーズ順位は2位フェルスタッペン（279）から6位ノリス（246）までわずか33点差でラスベガスへ向かう。",
            "body": [
                "雨のインテルラゴスを終えてキミ・アントネッリ（390点）とメルセデス（652点）の2026年F1両王座は確定したものの、来週のラスベガスGP（11月19〜21日、決勝50周）は2位争いが過熱している。サンパウロを1:35:23.504で制したランド・ノリス（246点）が、21番手から2位へ猛追したマックス・フェルスタッペン（279点）に33点差と接近した。",
                "両者の間にはジョージ・ラッセル（262点）、F1通算400戦目のルイス・ハミルトン（261点）、シャルル・ルクレール（249点）がひしめく。コンストラクターズでは2位フェラーリ（510点）の後ろでレッドブル（415点）とマクラーレン（398点）が17点差で3位を争っている。"
            ]
        },
        "ko": {
            "title": "F1 라스베이거스 전망: 챔피언 안토넬리 뒤 2위권 대혼전… 베르스타펀~노리스 5명 단 33점 차",
            "subtitle": "인터라고스 우중전 우승자 노리스와 컨스트럭터스 챔프 메르세데스(652점)에 이어 남은 2경기 순위 싸움이 치열합니다.",
            "excerpt": "브라질 그랑프리 이후 드라이버 2위 베르스타펀(279점)부터 6위 노리스(246점)까지 단 33점 차로 라스베이거스를 향합니다.",
            "body": [
                "상파울루 그랑프리(노리스 1시간35분23초504 우승, 베르스타펀 21위에서 2위 대추격)를 끝으로 키미 안토넬리(390점)와 메르세데스(652점)가 2026 F1 양대 타이틀을 모두 확정했지만, 오는 11월 19~21일 열리는 라스베이거스 GP의 2위권 경쟁은 정점으로 치닫고 있습니다.",
                "드라이버 2위 막스 베르스타펀(279점) 뒤로 조지 러셀(262점), 400번째 GP를 치른 루이스 해밀턴(261점), 샤를 르클레르(249점), 랜도 노리스(246점)까지 다섯 명이 33점 안에 몰려 있습니다. 컨스트럭터스에서도 페라리(510점)에 이어 레드불(415점)이 맥라렌(398점)을 단 17점 차로 앞서 있습니다."
            ]
        },
        "ar": {
            "title": "فورمولا 1 قبل لاس فيغاس: خمسة سائقين في 33 نقطة فقط خلف البطل كيمي انتونيلي",
            "subtitle": "نوريس يتوج تحت المطر في ساو باولو ومرسيدس يحسم لقب الصانعين بـ652 نقطة وسط صراع مشتعل على المركز الثاني.",
            "excerpt": "يدخل ماكس فيرستابن (279 نقطة) ولاندو نوريس (246 نقطة) ضمن فارق 33 نقطة لخمسة سائقين قبل جولة لاس فيغاس الليلية.",
            "body": [
                "بعد حسم كيمي انتونيلي (390 نقطة) وفريق مرسيدس (652 نقطة) لقبي السائقين والصانعين لعام 2026 في انترلاغوس، تتجه الانظار الى سباق لاس فيغاس (19-21 نوفمبر، 50 لفة) حيث يحتدم الصراع على وصافة الترتيب عقب فوز لاندو نوريس في البرازيل بزمن 1:35:23.504 وصعود ماكس فيرستابن من المركز 21 الى الثاني.",
                "لا يفصل سوى 33 نقطة بين الثاني فيرستابن (279) والسادس نوريس (246)، مع وجود جورج راسل (262) ولويس هاميلتون (261 في مشاركته الـ400) وشارل لوكلير (249) في قلب الصراع. وعند الصانعين يلاحق فيراري (510) بينما يتقدم ريد بول (415) على مكلارين (398) بفارق 17 نقطة فقط."
            ]
        }
    }
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


if __name__ == "__main__":
    lint_obj(NOV11_STORIES)
    print("All Nov 11 story translations validated: 0 em-dashes and 0 double-hyphens.")

    stories_file = os.path.join(os.path.dirname(__file__), "../../frontend/src/i18n/stories.ts")
    with open(stories_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already injected; avoid duplicates if re-run
    to_inject = []
    for slug, langs in NOV11_STORIES.items():
        if f'"{slug}":' in content or f"'{slug}':" in content:
            print(f"Skipping already-present slug in stories.ts: {slug}")
        else:
            to_inject.append(f"  {json.dumps(slug)}: {json.dumps(langs, ensure_ascii=False, indent=2)},")

    # Fix Nov 10 factual errors inside existing nfl-week9-mnf story translations in stories.ts if present
    replacements = [
        ("Sam Darnold", "Carson Wentz"),
        ("Dalton Kincaid", "Keleki Latu"),
        ("萨姆·达诺德", "卡森·温茨"),
        ("达尔顿·金凯德", "凯莱基·拉图"),
        ("サム・ダーノルド", "カーソン・ウェンツ"),
        ("ダルトン・キンケイド", "ケレキ・ラトゥ"),
        ("샘 다놀드", "카슨 웬츠"),
        ("돌턴 킨케이드", "켈레키 라투"),
        ("سام دارنولد", "كارسون وينتز"),
        ("دالتون كينكيد", "كيليكي لاتو"),
    ]
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)

    if to_inject:
        target = "export const STORY_I18N: Record<string, LocMap> = {\n"
        assert target in content, "Target marker not found in stories.ts"
        snippet = "\n".join(to_inject) + "\n"
        content = content.replace(target, target + snippet, 1)

    with open(stories_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated frontend/src/i18n/stories.ts successfully.")

