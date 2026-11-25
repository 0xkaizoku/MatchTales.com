# Update playground.ts, messages.ts, and messages-*.ts for 2026-11-26.
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
I18N = os.path.join(ROOT, "frontend", "src", "i18n")

# 1. Update playground.ts
playground_path = os.path.join(I18N, "playground.ts")
pg_txt = open(playground_path, "r", encoding="utf-8").read()

pg_updates = {
    "en": {
        "pinFinal": "Davis Cup Bologna: Italy vs South Korea (Musetti d Hong 6-0, 7-6); Czechia d Canada 2-0. Turin: Alcaraz d Zverev 6-2, 7-6(7) to win crown.",
        "plFootnote": "UCL MD5: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoli. PL Table: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "week1Closed": "Thanksgiving Football: Bears at Lions (1:00 PM ET), Eagles at Cowboys (4:30 PM ET), Chiefs at Bills (8:00 PM ET).",
        "week1Sub": "8-win Lions and 8-win Bears clash at Ford Field in NFC North holiday classic. Week 11 in books: Texans 26-3, Bills 26-9.",
        "countdownTnf": "THANKSGIVING DAY: Bears at Lions (1:00 PM ET CBS). Eagles at Cowboys (4:30 PM ET FOX). Chiefs at Bills (8:00 PM ET NBC).",
        "majorsDone": "The RSM Classic Final: Marco Penge wins 4-way playoff on 1st extra hole at -16 (266) over Haotong Li and Thorbjornsen.",
        "gridAfterMadrid": "Round 22 · Qatar GP Sprint Weekend at Lusail (27-29 Nov)",
        "barsPoints": "Antonelli (402) & Mercedes (666) Champions; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (MW11): Arsenal lead 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Select a club. Arsenal lead on 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Chelsea 16."
    },
    "fr": {
        "pinFinal": "Coupe Davis Bologne : Italie vs Coree du Sud (Musetti bat Hong 6-0, 7-6) ; Tchequie bat Canada 2-0. Turin : Alcaraz sacre face a Zverev.",
        "plFootnote": "LDC J5 : Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Naples. Classement PL : Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "week1Closed": "Thanksgiving NFL : Bears chez les Lions (13h00 ET), Eagles chez les Cowboys (16h30 ET), Chiefs chez les Bills (20h00 ET).",
        "week1Sub": "Lions et Bears (8-3) s'affrontent a Ford Field pour la tete de la NFC Nord. Bilan S11 : Texans 26-3, Bills 26-9.",
        "countdownTnf": "THANKSGIVING NFL : Bears chez les Lions (13h00 ET CBS). Eagles chez les Cowboys (16h30 ET FOX). Chiefs chez les Bills (20h00 ET NBC).",
        "majorsDone": "The RSM Classic : Marco Penge s'impose en playoff a quatre a -16 (266) devant Haotong Li et Thorbjornsen.",
        "gridAfterMadrid": "Manche 22 · GP du Qatar a Lusail (27-29 nov)",
        "barsPoints": "Antonelli (402) et Mercedes (666) Champions ; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (J11) : Arsenal en tete avec 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Selectionnez un club. Arsenal en tete avec 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18."
    },
    "es": {
        "pinFinal": "Copa Davis Bolonia: Italia vs Corea del Sur (Musetti d Hong 6-0, 7-6); Chequia 2-0 Canada. Turin: Alcaraz campeon ante Zverev.",
        "plFootnote": "UCL J5: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoles. Tabla PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "week1Closed": "Accion de Gracias NFL: Bears en Lions (1:00 PM ET), Eagles en Cowboys (4:30 PM ET), Chiefs en Bills (8:00 PM ET).",
        "week1Sub": "Lions y Bears (8-3) chocan en Ford Field por la NFC Norte. Semana 11 finalizada: Texans 26-3, Bills 26-9.",
        "countdownTnf": "DIA DE ACCION DE GRACIAS: Bears en Lions (1:00 PM ET CBS). Eagles en Cowboys (4:30 PM ET FOX). Chiefs en Bills (8:00 PM ET NBC).",
        "majorsDone": "The RSM Classic: Marco Penge gana en desempate cuadruple en -16 (266) ante Haotong Li y Thorbjornsen.",
        "gridAfterMadrid": "Ronda 22 · GP de Catar en Lusail (27-29 nov)",
        "barsPoints": "Antonelli (402) y Mercedes (666) Campeones; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (J11): Arsenal lider con 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Selecciona un club. Arsenal lider con 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Chelsea 16."
    },
    "de": {
        "pinFinal": "Davis Cup Bologna: Italien vs Suedkorea (Musetti schlaegt Hong 6:0, 7:6); Tschechien 2:0 Kanada. Turin: Alcaraz schlaegt Zverev.",
        "plFootnote": "UCL Spieltag 5: Real Madrid 5:1 PSV, Arsenal 1:1 Dortmund, Man City 2:2 Napoli. PL-Tabelle: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "week1Closed": "Thanksgiving Football: Bears bei den Lions (1:00 PM ET), Eagles bei Cowboys (4:30 PM ET), Chiefs bei Bills (8:00 PM ET).",
        "week1Sub": "Lions und Bears (je 8-3) kaempfen im Ford Field um NFC North Fuehrung. Woche 11 beendet: Texans 26:3, Bills 26:9.",
        "countdownTnf": "THANKSGIVING DAY: Bears bei Lions (1:00 PM ET CBS). Eagles bei Cowboys (4:30 PM ET FOX). Chiefs bei Bills (8:00 PM ET NBC).",
        "majorsDone": "The RSM Classic: Marco Penge siegt im Vierer-Playoff bei -16 (266) gegen Haotong Li und Thorbjornsen.",
        "gridAfterMadrid": "Runde 22 · Katar GP Sprint-Wochenende in Lusail (27.-29. Nov.)",
        "barsPoints": "Antonelli (402) und Mercedes (666) Weltmeister; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (11. Sp.): Arsenal fuehrt mit 28 Pkt., Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Waehlen Sie einen Klub. Arsenal fuehrt mit 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18."
    },
    "it": {
        "pinFinal": "Coppa Davis Bologna: Italia vs Corea del Sud (Musetti batte Hong 6-0, 7-6); Repubblica Ceca 2-0 Canada. Torino: Alcaraz trionfa su Zverev.",
        "plFootnote": "UCL 5ª giornata: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoli. Classifica PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "week1Closed": "Ringraziamento NFL: Bears a Detroit (19:00 italiane), Eagles a Dallas (22:30), Chiefs a Buffalo (02:00 notte).",
        "week1Sub": "Lions e Bears (8-3) si sfidano al Ford Field per il vertice della NFC North. Week 11 conclusa: Texans 26-3, Bills 26-9.",
        "countdownTnf": "THANKSGIVING DAY: Bears a Detroit (19:00). Eagles a Dallas (22:30). Chiefs a Buffalo (02:00).",
        "majorsDone": "The RSM Classic: Marco Penge trionfa allo spareggio a quattro a -16 (266) contro Haotong Li e Thorbjornsen.",
        "gridAfterMadrid": "Round 22 · GP del Qatar a Lusail (27-29 nov)",
        "barsPoints": "Antonelli (402) e Mercedes (666) Campioni; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (11ª g.): Arsenal capolista a 28 pt, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Seleziona un club. Arsenal in vetta a quota 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18."
    },
    "pl": {
        "pinFinal": "Puchar Davisa Bolonia: Wlochy vs Korea Pld (Musetti pokonal Honga 6:0, 7:6); Czechy 2:0 Kanada. Turyn: Alcaraz mistrzem po wygranej ze Zverevem.",
        "plFootnote": "Liga Mistrzow: Real Madryt 5:1 PSV, Arsenal 1:1 Dortmund, Man City 2:2 Napoli. Tabela PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "week1Closed": "Swieto Dziekczynienia w NFL: Bears u Lions (19:00 czasu polskiego), Eagles u Cowboys (22:30), Chiefs u Bills (02:00).",
        "week1Sub": "Lions i Bears (po 8-3) walcza na Ford Field o tron w NFC North. 11. tydzien zakonczony: Texans 26:3, Bills 26:9.",
        "countdownTnf": "THANKSGIVING DAY: Bears u Lions (19:00). Eagles u Cowboys (22:30). Chiefs u Bills (02:00).",
        "majorsDone": "The RSM Classic: Marco Penge wygrywa czteroosobowa dogrywke z wynikiem -16 (266) przed Haotongiem Li i Thorbjornsenem.",
        "gridAfterMadrid": "Runda 22 · Weekend ze sprintem GP Kataru w Lusail (27-29 listopada)",
        "barsPoints": "Antonelli (402) i Mercedes (666) Mistrzowie; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (11. kol.): Arsenal na czele z 28 pkt, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Wybierz klub. Arsenal liderem z 28 pkt, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18."
    },
    "zh": {
        "pinFinal": "戴维斯杯博洛尼亚：意大利对韩国（穆塞蒂6-0、7-6胜洪性成）；捷克2-0加拿大。都灵：阿尔卡拉斯力克兹维列夫全胜封王。",
        "plFootnote": "欧冠第5轮：皇马5-1埃因霍温，阿森纳1-1多特蒙德，曼城2-2那不勒斯。英超积分榜：阿森纳28，布莱顿22，曼城22，利物浦21。",
        "week1Closed": "NFL感恩节大战：熊队客战雄狮（美东13:00），老鹰客战牛仔（16:30），酋长客战比尔（20:00）。",
        "week1Sub": "同积8胜3负的雄狮与熊队在福特球场打响国北榜首大战。第11周战果：德州人26-3，比尔26-9。",
        "countdownTnf": "感恩节大赛：熊队客战雄狮（美东13:00 CBS）。老鹰客战牛仔（16:30 FOX）。酋长客战比尔（20:00 NBC）。",
        "majorsDone": "RSM精英赛决战：马尔科·彭奇在四人加洞赛首洞以-16（266杆）力压李昊桐与索比约恩森夺冠。",
        "gridAfterMadrid": "第22站 · 卡塔尔大奖赛卢赛尔冲刺周末（11月27-29日）",
        "barsPoints": "安东内利（402分）与梅赛德斯（666分）提前夺冠；维斯塔潘304分，汉密尔顿267分，拉塞尔264分，诺里斯264分。",
        "tableAfterMonday": "英超积分榜（第11轮）：阿森纳28分领跑，布莱顿22分，曼城22分，利物浦21分，伯恩茅斯18分。",
        "pinClub": "选择俱乐部。阿森纳28分领跑，布莱顿22分，曼城22分，利物浦21分，伯恩茅斯18分，切尔西16分。"
    },
    "ja": {
        "pinFinal": "デビスカップ・ボローニャ：イタリア対韓国（ムゼッティがホンに6-0、7-6で先勝）；チェコ2-0カナダ。トリノ：アルカラスが全勝優勝。",
        "plFootnote": "欧州CL第5節：Rマドリード5-1 PSV、アーセナル1-1ドルトムント、マンC 2-2ナポリ。PL順位：アーセナル28、ブライトン22、シティ22、リヴァプール21。",
        "week1Closed": "感謝祭NFL：ライオンズ対ベアーズ（米東部13:00）、カウボーイズ対イーグルス（16:30）、ビルズ対チーフス（20:00）。",
        "week1Sub": "8勝3敗で並ぶライオンズとベアーズがフォード・フィールドで激突。第11週結果：テキサンズ26-3、ビルズ26-9。",
        "countdownTnf": "感謝祭フットボール：ベアーズ対ライオンズ（米東部13:00 CBS）。イーグルス対カウボーイズ（16:30 FOX）。チーフス対ビルズ（20:00 NBC）。",
        "majorsDone": "RSMクラシック最終結果：マルコ・ペンジが通算-16（266）の4人プレーオフ1ホール目を制し李昊桐らを下して初優勝。",
        "gridAfterMadrid": "第22戦 · カタールGPスプリント週末 ルサイル（11月27-29日）",
        "barsPoints": "アントネッリ（402点）＆メルセデス（666点）年間王者；フェルスタッペン304点、ハミルトン267点、ラッセル264点、ノリス264点。",
        "tableAfterMonday": "プレミアリーグ（第11節）：アーセナル首位28点、ブライトン22点、マンC 22点、リヴァプール21点、ボーンマス18点。",
        "pinClub": "クラブを選択。アーセナル28点、ブライトン22点、マンC 22点、リヴァプール21点、ボーンマス18点。"
    },
    "ko": {
        "pinFinal": "데이비스 컵 볼로냐: 이탈리아 vs 한국 (무세티 6-0, 7-6 홍성찬 승); 체코 2-0 캐나다. 토리노: 알카라스 전승 우승 달성.",
        "plFootnote": "UCL 5차전: 레알 마드리드 5-1 PSV, 아스널 1-1 도르트문트, 맨시티 2-2 나폴리. PL 순위: 아스널 28, 브라이튼 22, 맨시티 22, 리버풀 21.",
        "week1Closed": "추수감사절 NFL: 베어스 vs 라이온스 (미 동부 13:00), 이글스 vs 카우보이스 (16:30), 치프스 vs 빌스 (20:00).",
        "week1Sub": "8승 3패 동률의 라이온스와 베어스가 포드 필드에서 지구 1위 격돌. 11주차 결과: 텍산스 26-3, 빌스 26-9.",
        "countdownTnf": "추수감사절 데이: 베어스 vs 라이온스 (13:00 CBS). 이글스 vs 카우보이스 (16:30 FOX). 치프스 vs 빌스 (20:00 NBC).",
        "majorsDone": "RSM 클래식 최종: 마르코 펜지가 4자 연장전 첫 홀에서 -16(266)으로 리하오퉁과 소르비욘센을 꺾고 우승.",
        "gridAfterMadrid": "22라운드 · 카타르 GP 루사일 스프린트 주말 (11월 27-29일)",
        "barsPoints": "안토넬리(402점)와 메르세데스(666점) 챔피언; 페르스타펜 304점, 해밀턴 267점, 러셀 264점, 노리스 264점.",
        "tableAfterMonday": "프리미어리그(11R): 아스널 28점 선두, 브라이튼 22점, 맨시티 22점, 리버풀 21점, 본머스 18점.",
        "pinClub": "클럽을 선택하세요. 아스널 28점 선두, 브라이튼 22점, 맨시티 22점, 리버풀 21점, 본머스 18점."
    },
    "ar": {
        "pinFinal": "كأس ديفيز في بولونيا: إيطاليا ضد كوريا الجنوبية (موسيتي هزم هونغ 6-0 و7-6)؛ التشيك 2-0 كندا. تورينو: ألكاراز بطل الماسترز.",
        "plFootnote": "دوري الأبطال الجولة 5: ريال مدريد 5-1 آيندهوفن، أرسنال 1-1 دورتموند، مانشستر سيتي 2-2 نابولي. الدوري الإنجليزي: أرسنال 28، برايتون 22، سيتي 22.",
        "week1Closed": "عيد الشكر في دوري كرة القدم الأمريكية: بيرز ضد لايونز (1:00 ظهرا بتوقيت شرق أمريكا)، إيغلز ضد كاوبويز (4:30)، تشيفز ضد بيلز (8:00).",
        "week1Sub": "لايونز وبيرز (8-3) في قمة فورد فيلد لحسم صدارة القسم الشمالي. ختام الأسبوع 11: تكسانز 26-3، بيلز 26-9.",
        "countdownTnf": "يوم عيد الشكر: بيرز ضد لايونز (1:00 ظهرا CBS). إيغلز ضد كاوبويز (4:30 FOX). تشيفز ضد بيلز (8:00 NBC).",
        "majorsDone": "بطولة آر إس إم كلاسيك: ماركو بينجي يفوز بالتمايز الرباعي عند -16 (266) متفوقا على لي هاوتونغ وثوربيورنسن.",
        "gridAfterMadrid": "الجولة 22 · عطلة نهاية أسبوع سباق السرعة لجائزة قطر الكبرى في لوسيل (27-29 نوفمبر)",
        "barsPoints": "أنتونيللي (402) ومرسيدس (666) أبطال العالم؛ فيرستابن 304، هاميلتون 267، راسل 264، نوريس 264.",
        "tableAfterMonday": "الدوري الإنجليزي (الجولة 11): أرسنال في الصدارة بـ 28 نقطة، برايتون 22، مانشستر سيتي 22، ليفربول 21.",
        "pinClub": "اختر ناديا. أرسنال يتصدر بـ 28 نقطة، برايتون 22، مانشستر سيتي 22، ليفربول 21، بورنموث 18."
    }
}

for loc, fields in pg_updates.items():
    loc_pattern = rf'("{loc}":\s*\{{)([\s\S]*?)(\n  \}})'
    match = re.search(loc_pattern, pg_txt)
    if not match:
        print(f"Warning: could not find locale block for {loc} in playground.ts")
        continue
    prefix, block_body, suffix = match.groups()
    for field_name, new_val in fields.items():
        escaped_val = new_val.replace('"', '\\"')
        field_pattern = rf'("{field_name}":\s*")[^"]*(")'
        block_body = re.sub(field_pattern, rf'\g<1>{escaped_val}\g<2>', block_body)
    pg_txt = pg_txt[:match.start()] + prefix + block_body + suffix + pg_txt[match.end():]

open(playground_path, "w", encoding="utf-8").write(pg_txt)
print("Updated playground.ts.")

# 2. Update messages.ts (en and fr)
messages_path = os.path.join(I18N, "messages.ts")
msg_txt = open(messages_path, "r", encoding="utf-8").read()

msg_en = {
    "todayDesk": "Thursday desk: Thanksgiving NFL (Bears at Lions, Eagles at Cowboys, Chiefs at Bills). Champions League MD5 (Real Madrid 5-1 PSV). Qatar GP arrives. Davis Cup Finals in Bologna.",
    "todayNfl": "Thanksgiving Day: Bears at Lions (1:00 PM ET CBS), Eagles at Cowboys (4:30 PM ET FOX), Chiefs at Bills (8:00 PM ET NBC).",
    "todayTnf": "NFL Thanksgiving tripleheader today: Lions host Bears at Ford Field in pivotal NFC North showdown.",
    "football_tagline": "Thanksgiving Classic: 8-win Lions host 8-win Bears at Ford Field; holiday tripleheader underway.",
    "football_liveNow": "Thanksgiving: Bears at Lions (1:00 PM ET), Eagles at Cowboys (4:30 PM ET), Chiefs at Bills (8:00 PM ET). Week 11 final: Texans 26, Colts 3.",
    "football_pulse": "NFL THANKSGIVING DAY: BEARS AND LIONS CLASH AT FORD FIELD IN 8-WIN NFC NORTH HOLIDAY BLOCKBUSTER",
    "tennis_tagline": "Davis Cup Finals in Bologna: Italy launch title defense as Czechia advance to semifinals.",
    "tennis_liveNow": "Davis Cup Bologna: Italy vs South Korea (Musetti d. Hong 6-0, 7-6); Czechia d. Canada 2-0. Turin Final: Alcaraz d. Zverev 6-2, 7-6(7) to seal crown.",
    "tennis_pulse": "DAVIS CUP FINALS: DEFENDING CHAMPIONS ITALY LEAD IN BOLOGNA AS ALCARAZ CELEBRATES TURIN MAIDEN TITLE",
    "f1_tagline": "Qatar GP arrives: Verstappen carries Las Vegas victory momentum into Lusail sprint weekend.",
    "f1_liveNow": "Las Vegas GP Final: 1. Verstappen (75th win), 2. Norris, 3. Piastri. Next: Round 22 Qatar GP at Lusail (27-29 Nov). Drivers: Antonelli 402, Verstappen 304, Norris 264.",
    "f1_pulse": "FORMULA 1: VERSTAPPEN REBOUNDS WITH LAS VEGAS VICTORY AS TEAMS HEAD DIRECTLY TO LUSAIL FOR QATAR GP",
    "soccer_tagline": "Champions League MD5: Real Madrid crush PSV 5-1 to remain perfect; Arsenal and Dortmund draw 1-1.",
    "soccer_liveNow": "UCL MD5: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoli. PL Table: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
    "soccer_pulse": "CHAMPIONS LEAGUE MD5: REAL MADRID SURGE TO FIVE STRAIGHT WINS WHILE PREMIER LEAGUE TITANS BATTLE IN EUROPE",
    "basketball_tagline": "NBA Thanksgiving break: Celtics roll past Wizards 131-116 as Emirates NBA Cup intensity builds.",
    "basketball_liveNow": "Thu: League-wide Thanksgiving holiday break. Tue/Wed Cup: Celtics 131-116 Wizards; Pistons 104-86 Magic; Nuggets 121-118 Mavs. Action resumes Friday with 12 games.",
    "basketball_pulse": "NBA CUP: LEAGUE ENJOYS THANKSGIVING HOLIDAY PAUSE AHEAD OF HIGH-STAKES FRIDAY TOURNAMENT BATTLES",
    "golf_tagline": "Marco Penge captures maiden PGA Tour victory in dramatic four-man playoff at The RSM Classic.",
    "golf_liveNow": "The RSM Classic Final: Marco Penge wins on 1st playoff hole at -16 (266) over Haotong Li and Thorbjornsen. Next: Hero World Challenge (Dec 3-6).",
    "golf_pulse": "PGA TOUR: MARCO PENGE BREAKS THROUGH IN FOUR-WAY SEA ISLAND PLAYOFF TO LOCK IN 2027 TOUR CARD",
    "tonight": "Thursday desk",
    "tonightBlurb": "Thanksgiving Day NFL: Bears at Lions opens holiday slate at Ford Field. Champions League: Real Madrid rout PSV 5-1; Arsenal 1-1 Dortmund. Davis Cup Finals: Italy lead in Bologna. F1: Qatar GP preview.",
    "f1Title": "Qatar Grand Prix: Verstappen brings Las Vegas victory momentum to Lusail sprint weekend",
    "f1Blurb": "The high-speed desert sweepers of Lusail await: Verstappen sits on 304 points after his 75th win on the Strip, with Hamilton, Russell, and Norris in a 3-point fight for third."
}

msg_fr = {
    "todayDesk": "Bureau du jeudi : Thanksgiving NFL (Bears chez les Lions, Eagles chez les Cowboys, Chiefs chez les Bills). Ligue des champions (Real Madrid 5-1 PSV). GP du Qatar en vue. Coupe Davis a Bologne.",
    "todayNfl": "Thanksgiving NFL : Bears chez les Lions (13h00 ET CBS), Eagles chez les Cowboys (16h30 ET FOX), Chiefs chez les Bills (20h00 ET NBC).",
    "todayTnf": "Triple affiche de Thanksgiving aujourd'hui : Les Lions recoivent les Bears a Ford Field pour la tete de la NFC Nord.",
    "football_tagline": "Thanksgiving Classic : Les Lions et les Bears (8-3) croisent le fer a Ford Field ; debut des festivites.",
    "football_liveNow": "Thanksgiving : Bears chez les Lions (13h00 ET), Eagles chez les Cowboys (16h30 ET), Chiefs chez les Bills (20h00 ET). Semaine 11 : Texans 26-3.",
    "football_pulse": "NFL THANKSGIVING : LES LIONS ET LES BEARS S'AFFRONTENT A FORD FIELD DANS UN CHOC AU SOMMET DE LA NFC NORD",
    "tennis_tagline": "Coupe Davis a Bologne : L'Italie tenante du titre entame son quart de finale pendant que la Tchequie file en demies.",
    "tennis_liveNow": "Coupe Davis Bologne : Italie vs Coree du Sud (Musetti bat Hong 6-0, 7-6) ; Tchequie bat Canada 2-0. Turin : Alcaraz bat Zverev 6-2, 7-6(7).",
    "tennis_pulse": "COUPE DAVIS : L'ITALIE EN TETE A BOLOGNE ALORS QU'ALCARAZ SAVOURE SON PREMIER TITRE AUX MASTERS DE TURIN",
    "f1_tagline": "GP du Qatar en approche : Verstappen emporte l'elan de sa victoire a Las Vegas vers le sprint de Lusail.",
    "f1_liveNow": "Las Vegas GP : 1. Verstappen (75e victoire), 2. Norris, 3. Piastri. Prochaine etape : Round 22 GP du Qatar (27-29 nov). Pilotes : Antonelli 402, Verstappen 304.",
    "f1_pulse": "FORMULE 1 : VERSTAPPEN REBONDIT AVEC SA VICTOIRE A VEGAS AVANT LE SPRINT DU GP DU QATAR A LUSAIL",
    "soccer_tagline": "Ligue des champions J5 : Le Real Madrid domine le PSV 5-1 ; Arsenal et Dortmund se neutralisent 1-1.",
    "soccer_liveNow": "LDC J5 : Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Naples. Classement PL : Arsenal 28, Brighton 22, City 22, Liverpool 21.",
    "soccer_pulse": "LIGUE DES CHAMPIONS : LE REAL MADRID SIGNE UN CINQ SUR CINQ TANDIS QUE LES CADORS ANGLAIS S'ILLUSTRENT",
    "basketball_tagline": "Pause de Thanksgiving en NBA : Les Celtics dominent les Wizards 131-116 dans la ferveur de la Cup.",
    "basketball_liveNow": "Jeudi : Relache pour Thanksgiving. Resultats Cup : Celtics 131-116 Wizards ; Pistons 104-86 Magic ; Nuggets 121-118 Mavs. Reprise vendredi avec 12 matchs.",
    "basketball_pulse": "NBA CUP : LA LIGUE S'ACCORDE UNE PAUSE POUR THANKSGIVING AVANT LE MARATHON DE 12 MATCHS VENDREDI",
    "golf_tagline": "Marco Penge decroche sa premiere victoire sur le PGA Tour en barrage a quatre au RSM Classic.",
    "golf_liveNow": "The RSM Classic : Marco Penge l'emporte au 1er trou de playoff a -16 (266) face a Haotong Li et Thorbjornsen. Prochain rdv : Hero World Challenge (3-6 dec).",
    "golf_pulse": "PGA TOUR : MARCO PENGE S'OFFRE UN PREMIER SACRE EN BARRAGE A SEA ISLAND ET VERROUILLE SA CARTE 2027",
    "tonight": "Bureau du jeudi",
    "tonightBlurb": "Thanksgiving NFL : Lions-Bears lance la fete a Ford Field. Ligue des champions : Real Madrid 5-1 PSV ; Arsenal 1-1 Dortmund. Coupe Davis : l'Italie debute a Bologne. F1 : GP du Qatar en vue.",
    "f1Title": "Grand Prix du Qatar : Verstappen aborde le week-end sprint de Lusail avec le vent en poupe",
    "f1Blurb": "Le trace nocturne de Lusail attend le paddock : Verstappen totalise 304 points apres son triomphe a Las Vegas, avec Hamilton, Russell et Norris au coude a coude pour la 3e place."
}

en_match = re.search(r'(export const en:\s*Messages\s*=\s*\{)([\s\S]*?)(\n\};\n\nexport const fr)', msg_txt)
if en_match:
    en_body = en_match.group(2)
    for k, v in msg_en.items():
        escaped_v = v.replace('"', '\\"')
        if k in ["todayDesk", "todayNfl", "todayTnf", "tonight", "tonightBlurb", "f1Title", "f1Blurb"]:
            en_body = re.sub(rf'({k}:\s*")[^"]*(")', rf'\g<1>{escaped_v}\g<2>', en_body)
        elif "_" in k:
            sport, prop = k.split("_", 1)
            sport_m = re.search(rf'({sport}:\s*\{{[^}}]*?{prop}:\s*")[^"]*(")', en_body)
            if sport_m:
                en_body = en_body[:sport_m.start(1)] + f'{sport_m.group(1)}{escaped_v}{sport_m.group(2)}' + en_body[sport_m.end():]
    msg_txt = msg_txt[:en_match.start(2)] + en_body + msg_txt[en_match.end(2):]

fr_match = re.search(r'(export const fr:\s*Messages\s*=\s*\{)([\s\S]*?)(\n\};)', msg_txt)
if fr_match:
    fr_body = fr_match.group(2)
    for k, v in msg_fr.items():
        escaped_v = v.replace('"', '\\"')
        if k in ["todayDesk", "todayNfl", "todayTnf", "tonight", "tonightBlurb", "f1Title", "f1Blurb"]:
            fr_body = re.sub(rf'({k}:\s*")[^"]*(")', rf'\g<1>{escaped_v}\g<2>', fr_body)
        elif "_" in k:
            sport, prop = k.split("_", 1)
            sport_m = re.search(rf'({sport}:\s*\{{[^}}]*?{prop}:\s*")[^"]*(")', fr_body)
            if sport_m:
                fr_body = fr_body[:sport_m.start(1)] + f'{sport_m.group(1)}{escaped_v}{sport_m.group(2)}' + fr_body[sport_m.end():]
    msg_txt = msg_txt[:fr_match.start(2)] + fr_body + msg_txt[fr_match.end(2):]

open(messages_path, "w", encoding="utf-8").write(msg_txt)
print("Updated messages.ts (en and fr).")

# 3. Update messages-*.ts for other locales
other_locales = {
    "es": {
        "todayDesk": "Mesa del jueves: Accion de Gracias NFL (Bears en Lions, Eagles en Cowboys, Chiefs en Bills). Champions League (Real Madrid 5-1 PSV). Previa del GP de Catar. Copa Davis en Bolonia.",
        "todayNfl": "Dia de Accion de Gracias: Bears en Lions (1:00 PM ET CBS), Eagles en Cowboys (4:30 PM ET FOX), Chiefs en Bills (8:00 PM ET NBC).",
        "todayTnf": "Triple cartelera de Accion de Gracias: Los Lions reciben a los Bears en Ford Field en un duelo directo por la NFC Norte.",
        "football_tagline": "Clasico de Accion de Gracias: Lions y Bears (8-3) miden fuerzas en Ford Field; arranca la triple jornada.",
        "football_liveNow": "Accion de Gracias: Bears en Lions (1:00 PM ET), Eagles en Cowboys (4:30 PM ET), Chiefs en Bills (8:00 PM ET). Semana 11: Texans 26-3.",
        "football_pulse": "NFL ACCION DE GRACIAS: LIONS Y BEARS CHOCAN EN FORD FIELD POR EL DOMINIO DE LA NFC NORTE",
        "tennis_tagline": "Copa Davis en Bolonia: La campeona Italia arranca con ventaja ante Corea del Sur; Chequia en semifinales.",
        "tennis_liveNow": "Copa Davis Bolonia: Italia vs Corea del Sur (Musetti b. Hong 6-0, 7-6); Chequia b. Canada 2-0. Turin: Alcaraz campeon ante Zverev 6-2, 7-6(7).",
        "tennis_pulse": "COPA DAVIS: ITALIA TOMA LA DELANTERA EN BOLONIA MIENTRAS ALCARAZ FESTEJA SU PRIMER TITRO DE MAESTRO",
        "f1_tagline": "Llega el GP de Catar: Verstappen traslada el impulso de Las Vegas al fin de semana sprint de Lusail.",
        "f1_liveNow": "GP de Las Vegas: 1. Verstappen (75ª victoria), 2. Norris, 3. Piastri. Proximo: Ronda 22 GP de Catar (27-29 nov). Pilotos: Antonelli 402, Verstappen 304.",
        "f1_pulse": "FORMULA 1: VERSTAPPEN REINA EN VEGAS Y APUNTA AL PENULTIMO DESAFIO EN EL SPRINT DEL GP DE CATAR",
        "soccer_tagline": "Champions League J5: El Real Madrid aplasta 5-1 al PSV; empate 1-1 entre Arsenal y Dortmund.",
        "soccer_liveNow": "UCL J5: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoles. Tabla Premier: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "soccer_pulse": "CHAMPIONS LEAGUE: EL REAL MADRID LIDERA CON PLENO DE VICTORIAS MIENTRAS CONTINUA LA PUJA INGLESA",
        "basketball_tagline": "Pausa de Accion de Gracias en la NBA: Los Celtics arrollan a los Wizards 131-116 antes del descanso festivo.",
        "basketball_liveNow": "Jueves: Descanso general por Accion de Gracias. Resultados Cup: Celtics 131-116 Wizards; Pistons 104-86 Magic; Nuggets 121-118 Mavs. Vuelve el viernes.",
        "basketball_pulse": "NBA CUP: LA LIGA TOMA UN RESPIRO POR ACCION DE GRACIAS ANTES DE LA JORNADA DECISIVA DEL VIERNES",
        "golf_tagline": "Marco Penge logra su primera victoria en el PGA Tour en desempate cuadruple en The RSM Classic.",
        "golf_liveNow": "The RSM Classic: Marco Penge vence en el 1er hoyo extra en -16 (266) a Haotong Li y Thorbjornsen. Proximo: Hero World Challenge (3-6 dic).",
        "golf_pulse": "PGA TOUR: MARCO PENGE TRIUNFA EN DRAMATICO DESEMPATE EN SEA ISLAND Y SE ASEGURA LA TARJETA 2027",
        "tonight": "Mesa del jueves",
        "tonightBlurb": "Accion de Gracias NFL: Lions y Bears abren la fiesta en Ford Field. Champions: Real Madrid 5-1 PSV; Arsenal 1-1 Dortmund. Copa Davis en Bolonia. F1: Previa de Catar.",
        "f1Title": "Gran Premio de Catar: Verstappen aterriza en Lusail con el impulso de su triunfo en Las Vegas",
        "f1Blurb": "Las rapidas curvas de Lusail esperan al pelotón: Verstappen suma 304 puntos tras su victoria 75, con Hamilton, Russell y Norris a 3 puntos por el tercer cajon."
    },
    "de": {
        "todayDesk": "Donnerstags-Desk: Thanksgiving NFL (Bears bei Lions, Eagles bei Cowboys, Chiefs bei Bills). Champions League (Real Madrid 5:1 PSV). Katar-GP Vorschau. Davis Cup in Bologna.",
        "todayNfl": "Thanksgiving Day: Bears bei Lions (1:00 PM ET CBS), Eagles bei Cowboys (4:30 PM ET FOX), Chiefs bei Bills (8:00 PM ET NBC).",
        "todayTnf": "NFL Thanksgiving-Dreierpack: Lions empfangen die Bears im Ford Field zum Divisionskrimi der NFC North.",
        "football_tagline": "Thanksgiving Classic: Lions und Bears (je 8-3) kaempfen im Ford Field; Feiertags-Tripleheader beginnt.",
        "football_liveNow": "Thanksgiving: Bears bei Lions (1:00 PM ET), Eagles bei Cowboys (4:30 PM ET), Chiefs bei Bills (8:00 PM ET). Woche 11: Texans 26:3.",
        "football_pulse": "NFL THANKSGIVING: LIONS UND BEARS DUELLIEREN SICH IM FORD FIELD UM DIE NFC NORTH SPITZE",
        "tennis_tagline": "Davis Cup in Bologna: Titelverteidiger Italien startet souveraen; Tschechien erreicht das Halbfinale.",
        "tennis_liveNow": "Davis Cup Bologna: Italien vs Suedkorea (Musetti schlaegt Hong 6:0, 7:6); Tschechien schlaegt Kanada 2:0. Turin: Alcaraz schlaegt Zverev 6:2, 7:6(7).",
        "tennis_pulse": "DAVIS CUP: ITALIEN FUEHRT IN BOLOGNA WAEHREND ALCARAZ SEINEN ERSTEN MASTERS-TITEL IN TURIN FEIERT",
        "f1_tagline": "Katar-GP naht: Verstappen nimmt Las-Vegas-Schwung mit ins Sprint-Wochenende von Lusail.",
        "f1_liveNow": "Las Vegas GP: 1. Verstappen (75. Sieg), 2. Norris, 3. Piastri. Naechster Halt: Runde 22 Katar-GP (27.-29. Nov.). Fahrer: Antonelli 402, Verstappen 304.",
        "f1_pulse": "FORMEL 1: VERSTAPPEN SIEGT IN LAS VEGAS UND BEREITET SICH AUF DEN SPRINT IN KATAR VOR",
        "soccer_tagline": "Champions League Spieltag 5: Real Madrid schlaegt PSV 5:1; Arsenal und Dortmund trennen sich 1:1.",
        "soccer_liveNow": "UCL 5. Sp.: Real Madrid 5:1 PSV, Arsenal 1:1 Dortmund, Man City 2:2 Napoli. PL-Tabelle: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "soccer_pulse": "CHAMPIONS LEAGUE: REAL MADRID BLEIBT MAKellos WAEHREND ENGLANDS TOPKLUBS IN EUROPA GEFORDERT SIND",
        "basketball_tagline": "Thanksgiving-Pause in der NBA: Celtics schlagen Wizards 131:116 vor dem Feiertags-Break.",
        "basketball_liveNow": "Donnerstag: Spielfrei an Thanksgiving. Cup-Spiele: Celtics 131:116 Wizards; Pistons 104:86 Magic; Nuggets 121:118 Mavs. Weiter am Freitag mit 12 Spielen.",
        "basketball_pulse": "NBA CUP: DIE LIGA PAUSIERT AN THANKSGIVING VOR DER GROSSEN FREITAGS-RUNDE MIT 12 SPIELEN",
        "golf_tagline": "Marco Penge sichert sich ersten PGA-Tour-Titel im Vierer-Stechen beim RSM Classic.",
        "golf_liveNow": "The RSM Classic: Marco Penge gewinnt am 1. Extra-Loch bei -16 (266) gegen Haotong Li und Thorbjornsen. Naechstes Event: Hero World Challenge (3.-6. Dez.).",
        "golf_pulse": "PGA TOUR: MARCO PENGE TRIUMPHIERT IM PLAYOFF IN SEA ISLAND UND SICHERT DIE TOURKARTE 2027",
        "tonight": "Donnerstags-Desk",
        "tonightBlurb": "Thanksgiving NFL: Lions gegen Bears eroeffnet den Feiertag. Champions League: Real Madrid 5:1 PSV; Arsenal 1:1 Dortmund. Davis Cup in Bologna. F1: Katar-Vorschau.",
        "f1Title": "Grosser Preis von Katar: Verstappen reist nach Las-Vegas-Erfolg mit Rueckenwind nach Lusail",
        "f1Blurb": "Der Wuestenkurs von Lusail wartet: Verstappen steht nach seinem 75. Sieg bei 304 Punkten, waehrend Hamilton, Russell und Norris um Rang drei ringen."
    },
    "it": {
        "todayDesk": "Desk del giovedi: Ringraziamento NFL (Bears a Detroit, Eagles a Dallas, Chiefs a Buffalo). Champions League (Real Madrid 5-1 PSV). GP del Qatar. Coppa Davis a Bologna.",
        "todayNfl": "Giorno del Ringraziamento: Bears a Detroit (19:00 italiane), Eagles a Dallas (22:30), Chiefs a Buffalo (02:00).",
        "todayTnf": "Tripletta del Ringraziamento NFL: I Lions ospitano i Bears al Ford Field nel duello al vertice della NFC North.",
        "football_tagline": "Thanksgiving Classic: Lions e Bears (8-3) si sfidano al Ford Field; al via il grande giovedi festivo.",
        "football_liveNow": "Ringraziamento: Bears a Detroit (19:00), Eagles a Dallas (22:30), Chiefs a Buffalo (02:00). Week 11: Texans 26-3.",
        "football_pulse": "NFL RINGRAZIAMENTO: LIONS E BEARS SI SFIDANO AL FORD FIELD PER IL PRIMATO NELLA NFC NORTH",
        "tennis_tagline": "Coppa Davis a Bologna: L'Italia campione in carica avanti con Musetti; Repubblica Ceca in semifinale.",
        "tennis_liveNow": "Coppa Davis Bologna: Italia vs Corea del Sud (Musetti b. Hong 6-0, 7-6); Repubblica Ceca b. Canada 2-0. Torino: Alcaraz batte Zverev 6-2, 7-6(7).",
        "tennis_pulse": "COPPA DAVIS: L'ITALIA COMINCIA AL MEGLIO A BOLOGNA MENTRE ALCARAZ FESTEGGIA IL TITOLO DI TORINO",
        "f1_tagline": "In arrivo il GP del Qatar: Verstappen porta la carica di Las Vegas al weekend sprint di Lusail.",
        "f1_liveNow": "GP Las Vegas: 1. Verstappen (75ª vittoria), 2. Norris, 3. Piastri. Prossima tappa: Round 22 GP del Qatar (27-29 nov). Piloti: Antonelli 402, Verstappen 304.",
        "f1_pulse": "FORMULA 1: VERSTAPPEN TRIONFA SULLA STRIP E GUIDA IL GRUPPO VERSO IL CIRCUITO DI LUSAIL",
        "soccer_tagline": "Champions League 5ª giornata: Il Real Madrid travolge il PSV 5-1; Arsenal e Dortmund pareggiano 1-1.",
        "soccer_liveNow": "UCL 5ª g.: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoli. Classifica PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "soccer_pulse": "CHAMPIONS LEAGUE: IL REAL MADRID RESTA A PUNTEGGIO PIENO MENTRE LE INGLESI COMBATTONO IN EUROPA",
        "basketball_tagline": "Pausa del Ringraziamento in NBA: I Celtics battono i Wizards 131-116 prima della sosta per le feste.",
        "basketball_liveNow": "Giovedi: Riposo generale per il Ringraziamento. Risultati Cup: Celtics 131-116 Wizards; Pistons 104-86 Magic; Nuggets 121-118 Mavs. Si riparte venerdi.",
        "basketball_pulse": "NBA CUP: LA LEGA SI FERMA PER IL RINGRAZIAMENTO IN ATTESA DELLE 12 GARE DI VENERDI",
        "golf_tagline": "Marco Penge conquista il primo titolo PGA Tour allo spareggio a quattro all'RSM Classic.",
        "golf_liveNow": "The RSM Classic: Marco Penge vince alla 1ª buca extra a -16 (266) su Haotong Li e Thorbjornsen. Prossimo torneo: Hero World Challenge (3-6 dic).",
        "golf_pulse": "PGA TOUR: MARCO PENGE TRIONFA AL PLAYOFF A SEA ISLAND E GUADAGNA L'ESENZIONE FINO AL 2028",
        "tonight": "Desk del giovedi",
        "tonightBlurb": "Ringraziamento NFL: Lions-Bears apre la festa al Ford Field. Champions: Real Madrid 5-1 PSV; Arsenal 1-1 Dortmund. Coppa Davis a Bologna. F1: Verso il Qatar.",
        "f1Title": "Gran Premio del Qatar: Verstappen approda a Lusail con l'entusiasmo della vittoria di Las Vegas",
        "f1Blurb": "Le curve veloci di Lusail attendono la Formula 1: Verstappen a quota 304 punti dopo la sua 75ª vittoria, con Hamilton, Russell e Norris appaiati per il podio mondiale."
    },
    "pl": {
        "todayDesk": "Czwartkowy przeglad: Swieto Dziekczynienia w NFL (Bears u Lions, Eagles u Cowboys, Chiefs u Bills). Liga Mistrzow (Real Madryt 5:1 PSV). Przed GP Kataru. Puchar Davisa w Bolonii.",
        "todayNfl": "Thanksgiving Day: Bears u Lions (19:00 czasu polskiego), Eagles u Cowboys (22:30), Chiefs u Bills (02:00 w nocy).",
        "todayTnf": "Swiateczny maraton NFL: Lions podejmuja Bears na Ford Field w wielkim starciu o pierwsze miejsce w NFC North.",
        "football_tagline": "Thanksgiving Classic: Lions i Bears (po 8-3) starcia sie na Ford Field; start swiatecznego potrojnego meczu.",
        "football_liveNow": "Thanksgiving: Bears u Lions (19:00), Eagles u Cowboys (22:30), Chiefs u Bills (02:00). 11. tydzien: Texans 26:3.",
        "football_pulse": "NFL THANKSGIVING: LIONS I BEARS WALCZA NA FORD FIELD O PRZODOWNICTWO W NFC NORTH",
        "tennis_tagline": "Puchar Davisa w Bolonii: Broniace tytulu Wlochy prowadza z Korea; Czechy w polfinale.",
        "tennis_liveNow": "Puchar Davisa Bolonia: Wlochy vs Korea Pld (Musetti pokonal Honga 6:0, 7:6); Czechy pokonaly Kanade 2:0. Turyn: Alcaraz mistrzem.",
        "tennis_pulse": "PUCHAR DAVISA: WLOSI NA PROWADZENIU W BOLONII PO TYTULE ALCARAZA W TURYNIE",
        "f1_tagline": "Zbliza sie GP Kataru: Verstappen przenosi impet po triumfie w Las Vegas na sprint w Lusail.",
        "f1_liveNow": "GP Las Vegas: 1. Verstappen (75. wygrana), 2. Norris, 3. Piastri. Nastepny wyscig: 22. runda GP Kataru (27-29 listopada). Kierowcy: Antonelli 402, Verstappen 304.",
        "f1_pulse": "FORMULA 1: VERSTAPPEN ZWYCIEZA W LAS VEGAS I RUSZA DO LUSAIL NA SPRINT O GP KATARU",
        "soccer_tagline": "Liga Mistrzow 5. kolejka: Real Madryt gromi PSV 5:1; remis 1:1 Arsenalu z Borussia Dortmund.",
        "soccer_liveNow": "LM 5. kol.: Real Madryt 5:1 PSV, Arsenal 1:1 Dortmund, Man City 2:2 Napoli. Tabela Premier League: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "soccer_pulse": "LIGA MISTRZOW: REAL MADRYT Z KOMPLETEM PIECIU WYGRANYCH NA CZELE 36 KLUBOW",
        "basketball_tagline": "Swiateczna pauza w NBA: Celtics rozbili Wizards 131:116 przed Dniem Dziekczynienia.",
        "basketball_liveNow": "Czwartek: Dzien wolny od gry w NBA. Puchar NBA: Celtics 131:116 Wizards; Pistons 104:86 Magic; Nuggets 121:118 Mavs. Powrot w piatek (12 meczow).",
        "basketball_pulse": "NBA CUP: LIGA PAUZUJE W SWIETO DZIEKCZYNIENIA PRZED PIATKOWA SERIA 12 MECZOW",
        "golf_tagline": "Marco Penge zdobywa pierwszy tytul PGA Tour po czteroosobowej dogrywce w The RSM Classic.",
        "golf_liveNow": "The RSM Classic: Marco Penge wygrywa na 1. dolku dogrywki przy -16 (266) przed Haotongiem Li i Thorbjornsenem. Kolejny turniej: Hero World Challenge (3-6 grudnia).",
        "golf_pulse": "PGA TOUR: MARCO PENGE ZWYCIEZA PO DOGRYWCE W SEA ISLAND I ZAPEWNIA SOBIE KARTE DO 2028 ROKU",
        "tonight": "Czwartkowy przeglad",
        "tonightBlurb": "Thanksgiving NFL: Mecz Lions z Bears otwiera swiateczny maraton na Ford Field. Liga Mistrzow: Real Madryt 5:1 PSV; Arsenal 1:1 Dortmund. Puchar Davisa w Bolonii. F1: Przed Katarem.",
        "f1Title": "Grand Prix Kataru: Verstappen zjezdzaja do Lusail po 75. triumfie odniesionym w Las Vegas",
        "f1Blurb": "Szybki tor w Lusail czeka na stawke: Verstappen z 304 punktami na koncie po wygranej na Stripie, a Hamilton, Russell i Norris w 3-punktowym scisku o 3. miejsce."
    },
    "zh": {
        "todayDesk": "周四要闻：NFL感恩节大战（熊队客战雄狮、老鹰客战牛仔、酋长客战比尔）。欧冠第5轮（皇马5-1大胜埃因霍温）。卡塔尔大奖赛在即。戴维斯杯博洛尼亚开打。",
        "todayNfl": "感恩节大赛：熊队客战雄狮（美东13:00 CBS），老鹰客战牛仔（16:30 FOX），酋长客战比尔（20:00 NBC）。",
        "todayTnf": "NFL感恩节三连赛今日打响：雄狮坐镇福特球场迎战熊队争夺国北榜首。",
        "football_tagline": "感恩节经典战役：同为8胜3负的雄狮与熊队在福特球场相遇；节日大战开打。",
        "football_liveNow": "感恩节：熊队客战雄狮（美东13:00），老鹰客战牛仔（16:30），酋长客战比尔（20:00）。第11周：德州人26-3小马。",
        "football_pulse": "NFL感恩节大战：雄狮与熊队在福特球场打响8胜国北榜首争夺战",
        "tennis_tagline": "戴维斯杯总决赛博洛尼亚打响：卫冕冠军意大利先拔头筹，捷克率先挺进四强。",
        "tennis_liveNow": "戴维斯杯博洛尼亚：意大利对韩国（穆塞蒂6-0、7-6胜洪性成）；捷克2-0加拿大。都灵决赛：阿尔卡拉斯6-2、7-6击败兹维列夫全胜夺冠。",
        "tennis_pulse": "戴维斯杯：卫冕冠军意大利博洛尼亚领跑，阿尔卡拉斯都灵年终全胜捧杯",
        "f1_tagline": "卡塔尔大奖赛来临：维斯塔潘携拉斯维加斯胜利势头进军卢赛尔冲刺周末。",
        "f1_liveNow": "拉斯维加斯GP决赛：1. 维斯塔潘（生涯第75胜），2. 诺里斯，3. 皮亚斯特里。下站：第22站卡塔尔GP（11月27-29日）。车手榜：安东内利402分，维斯塔潘304分。",
        "f1_pulse": "一级方程式：维斯塔潘拉斯维加斯夺魁重振声威，全队奔赴卢赛尔备战卡塔尔GP",
        "soccer_tagline": "欧冠联赛第5轮：皇家马德里5-1横扫埃因霍温斩获全胜；阿森纳客场1-1战平多特蒙德。",
        "soccer_liveNow": "欧冠第5轮：皇马5-1埃因霍温，阿森纳1-1多特蒙德，曼城2-2那不勒斯。英超积分榜：阿森纳28分，布莱顿22分，曼城22分，利物浦21分。",
        "soccer_pulse": "欧洲冠军联赛：皇家马德里豪取五连胜领跑36强，英超双雄在欧洲战场各有平局",
        "basketball_tagline": "NBA感恩节休整日：凯尔特人131-116击溃奇才，NBA杯战况愈演愈烈。",
        "basketball_liveNow": "周四：全联盟感恩节休赛。杯赛赛况：凯尔特人131-116奇才；活塞104-86魔术；掘金121-118独行侠。周五重燃战火（12场激战）。",
        "basketball_pulse": "NBA杯：全联盟欢度感恩节休赛一天，周五将迎12场杯赛出线生死决战",
        "golf_tagline": "马尔科·彭奇在RSM精英赛四人加洞赛中斩获美巡赛首冠。",
        "golf_liveNow": "RSM精英赛决赛：马尔科·彭奇在首个加洞以-16（266杆）战胜李昊桐与索比约恩森夺冠。下站：英雄世界挑战赛（12月3-6日）。",
        "golf_pulse": "美巡赛：彭奇海岛球场加洞赛绝杀夺得美巡首冠，直接锁定至2028赛季参赛卡",
        "tonight": "周四要闻",
        "tonightBlurb": "NFL感恩节大战：雄狮与熊队在福特球场揭幕节日盛宴。欧冠：皇马5-1埃因霍温；阿森纳1-1多特蒙德。戴维斯杯博洛尼亚激战。F1：卡塔尔站前瞻。",
        "f1Title": "卡塔尔大奖赛：维斯塔潘带拉斯维加斯夺冠余威奔赴卢赛尔冲刺赛",
        "f1Blurb": "卢赛尔高速沙漠赛道即将迎来决战：维斯塔潘在内华达拿下第75胜后积分达到304分，汉密尔顿、拉塞尔和诺里斯仅差3分争夺年度第三。"
    },
    "ja": {
        "todayDesk": "木曜デスク：感謝祭NFL（ベアーズ対ライオンズ、イーグルス対カウボーイズ、チーフス対ビルズ）。欧州CL第5節（Rマドリード5-1 PSV）。カタールGP展望。デビスカップ・ボローニャ大会。",
        "todayNfl": "感謝祭NFL日程：ライオンズ対ベアーズ（米東部13:00 CBS）、カウボーイズ対イーグルス（16:30 FOX）、ビルズ対チーフス（20:00 NBC）。",
        "todayTnf": "感謝祭NFLトリプルヘッダー開幕：ライオンズがフォード・フィールドでベアーズを迎え撃つNFC北地区首位攻防戦。",
        "football_tagline": "感謝祭クラシック：8勝3敗で並ぶライオンズとベアーズがフォード・フィールドで激突；ホリデー開幕。",
        "football_liveNow": "感謝祭：ライオンズ対ベアーズ（米東部13:00）、カウボーイズ対イーグルス（16:30）、ビルズ対チーフス（20:00）。第11週：テキサンズ26-3。",
        "football_pulse": "NFL感謝祭：ライオンズ対ベアーズがフォード・フィールドで地区首位を懸けて激突",
        "tennis_tagline": "デビスカップ・ボローニャ大会：王者イタリアが好発進、チェコが準決勝へ進出。",
        "tennis_liveNow": "デビスカップ・ボローニャ：イタリア対韓国（ムゼッティがホンに6-0、7-6で先勝）；チェコ2-0カナダ。トリノ：アルカラスがズベレフを下し初制覇。",
        "tennis_pulse": "デビスカップ：イタリアがボローニャで白星スタート、アルカラスはトリノで悲願の初制覇",
        "f1_tagline": "カタールGP開幕直前：フェルスタッペンがラスベガス勝利の勢いそのままにルサイルのスプリントへ。",
        "f1_liveNow": "ラスベガスGP決勝：1. フェルスタッペン（通算75勝）、2. ノリス、3. ピアストリ。次回：第22戦カタールGP（11月27-29日）。ドライバーズ：アントネッリ402点、フェルスタッペン304点。",
        "f1_pulse": "F1：フェルスタッペンがラスベガスを制し、砂漠のルサイルでの第22戦カタールGPへ",
        "soccer_tagline": "チャンピオンズリーグ第5節：レアル・マドリードがPSVに5-1で快勝；アーセナルはドルトムントと1-1。",
        "soccer_liveNow": "欧州CL第5節：Rマドリード5-1 PSV、アーセナル1-1ドルトムント、マンC 2-2ナポリ。プレミア順位：アーセナル28点、ブライトン22点、マンC 22点、リヴァプール21点。",
        "soccer_pulse": "チャンピオンズリーグ：レアル・マドリードが開幕5連勝、欧州の舞台で熱戦続く",
        "basketball_tagline": "NBA感謝祭ブレイク：セルティックスがウィザーズを131-116で圧倒、NBAカップ熱戦へ。",
        "basketball_liveNow": "木曜：感謝祭のため全試合休止。カップ戦結果：セルティックス131-116ウィザーズ；ピストンズ104-86マジック；ナゲッツ121-118マブス。金曜に12試合再開。",
        "basketball_pulse": "NBAカップ：感謝祭の休止日を経て、金曜日には12試合のトーナメント決戦へ",
        "golf_tagline": "マルコ・ペンジがRSMクラシックの4人プレーオフを制し、PGAツアー初優勝。",
        "golf_liveNow": "RSMクラシック：マルコ・ペンジがプレーオフ1ホール目で通算-16（266）をマークし李昊桐らを退ける。次戦：ヒーロー・ワールド・チャレンジ（12月3-6日）。",
        "golf_pulse": "PGAツアー：ペンジがシーアイランドのプレーオフを制し初勝利、2028年までの出場権を確保",
        "tonight": "木曜デスク",
        "tonightBlurb": "感謝祭NFL：ライオンズ対ベアーズがフォード・フィールドで開幕。欧州CL：Rマドリード5-1 PSV；アーセナル1-1ドルトムント。デビスカップ：ボローニャで開幕。F1：カタール展望。",
        "f1Title": "カタールGP：ラスベガスで勝利を挙げたフェルスタッペンがルサイルへ乗り込む",
        "f1Blurb": "ルサイルの高速コーナーが待つ：ラスベガスで75勝目を挙げ304点としたフェルスタッペンに対し、ハミルトン、ラッセル、ノリスが3点差で3位を争う。"
    },
    "ko": {
        "todayDesk": "목요일 데스크: 추수감사절 NFL (베어스 vs 라이온스, 이글스 vs 카우보이스, 치프스 vs 빌스). 챔피언스리그 (레알 마드리드 5-1 PSV). 카타르 GP 개막 임박. 데이비스 컵 볼로냐.",
        "todayNfl": "추수감사절 경기 일정: 베어스 vs 라이온스 (미 동부 13:00 CBS), 이글스 vs 카우보이스 (16:30 FOX), 치프스 vs 빌스 (20:00 NBC).",
        "todayTnf": "NFL 추수감사절 트리플헤더 개막: 라이온스가 포드 필드에서 베어스를 상대로 NFC 북부 선두 격돌.",
        "football_tagline": "추수감사절 클래식: 8승 3패 동률의 라이온스와 베어스가 포드 필드에서 격돌; 홀리데이 개막.",
        "football_liveNow": "추수감사절: 베어스 vs 라이온스 (13:00), 이글스 vs 카우보이스 (16:30), 치프스 vs 빌스 (20:00). 11주차: 텍산스 26-3.",
        "football_pulse": "NFL 추수감사절: 라이온스와 베어스가 포드 필드에서 NFC 북부 1위를 놓고 격돌",
        "tennis_tagline": "데이비스 컵 볼로냐: 디펜딩 챔피언 이탈리아 선두 출발; 체코 4강 진출.",
        "tennis_liveNow": "데이비스 컵 볼로냐: 이탈리아 vs 한국 (무세티 6-0, 7-6 승); 체코 2-0 캐나다. 토리노 결승: 알카라스, 츠베레프 6-2, 7-6(7) 꺾고 전승 우승.",
        "tennis_pulse": "데이비스 컵: 이탈리아 볼로냐에서 순항, 알카라스 토리노 파이널 첫 제패",
        "f1_tagline": "카타르 GP 임박: 페르스타펜, 라스베이거스 우승 기세를 몰아 루사일 스프린트로 진격.",
        "f1_liveNow": "라스베이거스 GP 결선: 1위 페르스타펜(통산 75승), 2위 노리스, 3위 피아스트리. 다음 라운드: 22R 카타르 GP (11월 27-29일). 드라이버: 안토넬리 402점, 페르스타펜 304점.",
        "f1_pulse": "F1: 페르스타펜 라스베이거스 우승으로 2위 굳히기, 루사일 서킷 카타르 GP 출격",
        "soccer_tagline": "챔피언스리그 5차전: 레알 마드리드 PSV 5-1 완파 전승 행진; 아스널 도르트문트와 1-1 무승부.",
        "soccer_liveNow": "UCL 5차전: 레알 마드리드 5-1 PSV, 아스널 1-1 도르트문트, 맨시티 2-2 나폴리. PL 순위: 아스널 28점, 브라이튼 22점, 맨시티 22점, 리버풀 21점.",
        "soccer_pulse": "챔피언스리그: 레알 마드리드 5전 전승 단독 선두, 유럽 무대 혈전 지속",
        "basketball_tagline": "NBA 추수감사절 휴식: 셀틱스, 위저즈 131-116 대파 후 컵 토너먼트 열기 고조.",
        "basketball_liveNow": "목요일: 추수감사절 리그 전체 휴식. 컵 결과: 셀틱스 131-116 위저즈; 피스톤스 104-86 매직; 너기츠 121-118 매브스. 금요일 12경기 재개.",
        "basketball_pulse": "NBA 컵: 추수감사절 하루 휴식 후 금요일 12경기 본선 진출전 재개",
        "golf_tagline": "마르코 펜지, RSM 클래식 4인 연장전 끝에 PGA 투어 첫 우승 트로피.",
        "golf_liveNow": "RSM 클래식: 마르코 펜지 1차 연장서 -16(266)으로 리하오퉁과 소르비욘센 꺾고 우승. 다음 대회: 히어로 월드 챌린지 (12월 3-6일).",
        "golf_pulse": "PGA 투어: 펜지, 시아일랜드 4자 연장전서 극적 우승 거두며 2028년까지 투어 카드 확보",
        "tonight": "목요일 데스크",
        "tonightBlurb": "추수감사절 NFL: 라이온스 vs 베어스가 포드 필드에서 개막. 챔피언스리그: 레알 5-1 PSV; 아스널 1-1 도르트문트. 데이비스 컵 볼로냐. F1 카타르 프리뷰.",
        "f1Title": "카타르 그랑프리: 라스베이거스에서 75승 달성한 페르스타펜, 루사일 스프린트 출격",
        "f1Blurb": "루사일 고속 서킷이 기다립니다: 라스베이거스 우승으로 304점을 쌓은 페르스타펜에 맞서 해밀턴, 러셀, 노리스가 3점 차로 3위 경쟁을 벌입니다."
    },
    "ar": {
        "todayDesk": "مكتب الخميس: عيد الشكر في دوري كرة القدم الأمريكية (بيرز ضد لايونز، إيغلز ضد كاوبويز، تشيفز ضد بيلز). دوري أبطال أوروبا (ريال مدريد 5-1 آيندهوفن). اقتراب جائزة قطر الكبرى. كأس ديفيز في بولونيا.",
        "todayNfl": "مباريات عيد الشكر: بيرز ضد لايونز (1:00 ظهرا بتوقيت شرق أمريكا CBS)، إيغلز ضد كاوبويز (4:30 FOX)، تشيفز ضد بيلز (8:00 NBC).",
        "todayTnf": "ثلاثية عيد الشكر تنطلق اليوم: لايونز يستقبل بيرز في فورد فيلد لحسم صدارة القسم الشمالي.",
        "football_tagline": "كلاسيكو عيد الشكر: لايونز وبيرز (8-3) يتواجهان في فورد فيلد في افتتاح الثلاثية الاحتفالية.",
        "football_liveNow": "عيد الشكر: بيرز ضد لايونز (1:00 ظهرا)، إيغلز ضد كاوبويز (4:30)، تشيفز ضد بيلز (8:00). الأسبوع 11: تكسانز 26-3.",
        "football_pulse": "كرة القدم الأمريكية: لايونز وبيرز يتصادمان في فورد فيلد لحسم قمة القسم الشمالي",
        "tennis_tagline": "كأس ديفيز في بولونيا: إيطاليا حاملة اللقب تتقدم والتشيك تبلغ الدور نصف النهائي.",
        "tennis_liveNow": "كأس ديفيز بولونيا: إيطاليا ضد كوريا الجنوبية (موسيتي فاز على هونغ 6-0 و7-6)؛ التشيك 2-0 كندا. تورينو: ألكاراز هزم زفيريف 6-2 و7-6(7).",
        "tennis_pulse": "كأس ديفيز: إيطاليا في الصدارة ببولونيا وتتويج ألكاراز التاريخي في تورينو",
        "f1_tagline": "جائزة قطر الكبرى تقترب: فيرستابن يدخل حلبة لوسيل بروح انتصار لاس فيغاس.",
        "f1_liveNow": "جائزة لاس فيغاس: 1. فيرستابن (فوزه الـ 75)، 2. نوريس، 3. بياستري. الجولة القادمة: جائزة قطر الكبرى (27-29 نوفمبر). السائقون: أنتونيللي 402، فيرستابن 304.",
        "f1_pulse": "فورمولا 1: فيرستابن يعود بقوة بعد فوزه في فيغاس والأنظار تتجه نحو سباق السرعة في قطر",
        "soccer_tagline": "دوري أبطال أوروبا الجولة 5: ريال مدريد يكتسح آيندهوفن 5-1؛ وتعادل أرسنال ودورتموند 1-1.",
        "soccer_liveNow": "دوري الأبطال: ريال مدريد 5-1 آيندهوفن، أرسنال 1-1 دورتموند، مانشستر سيتي 2-2 نابولي. الدوري الإنجليزي: أرسنال 28، برايتون 22، سيتي 22.",
        "soccer_pulse": "دوري أبطال أوروبا: ريال مدريد يواصل العلامة الكاملة بينما تواصل الأندية الإنجليزية الصراع",
        "basketball_tagline": "استراحة عيد الشكر في دوري السلة: سلتكس يتجاوز ويزاردز 131-116 مع اشتعال كأس الدوري.",
        "basketball_liveNow": "الخميس: راحة لجميع الفرق بمناسبة عيد الشكر. نتائج الكأس: سلتكس 131-116 ويزاردز؛ بيستونز 104-86 ماجيك؛ ناغتس 121-118 مافريكس. الاستئناف الجمعة بـ 12 مباراة.",
        "basketball_pulse": "دوري السلة الأمريكي: استراحة عيد الشكر قبل العودة ليوم الجمعة الحاسم بـ 12 مواجهة في الكأس",
        "golf_tagline": "ماركو بينجي يتوج بلقبه الأول في جولة بي جي إيه بعد تمايز رباعي درامي في آر إس إم كلاسيك.",
        "golf_liveNow": "آر إس إم كلاسيك: ماركو بينجي يفوز في الحفرة الإضافية الأولى بـ -16 (266) على لي هاوتونغ وثوربيورنسن. القادم: هيرو وورلد تشالنج (3-6 ديسمبر).",
        "golf_pulse": "جولة بي جي إيه: بينجي يحسم التمايز الرباعي في سي آيلاند ويضمن بطاقة المشاركة حتى 2028",
        "tonight": "مكتب الخميس",
        "tonightBlurb": "عيد الشكر NFL: مواجهة لايونز وبيرز تفتتح العطلة في فورد فيلد. دوري الأبطال: ريال مدريد 5-1 آيندهوفن؛ أرسنال 1-1 دورتموند. كأس ديفيز في بولونيا. الفورمولا 1 في قطر.",
        "f1Title": "جائزة قطر الكبرى: فيرستابن يصل لوسيل مدعوما بفوزه المثير في لاس فيغاس",
        "f1Blurb": "منعطفات لوسيل السريعة تترقب السائقين: فيرستابن يملك 304 نقاط بعد انتصاره الـ 75 في فيغاس، وهاميلتون وراسل ونوريس في صراع شرس بفارق 3 نقاط على المركز الثالث."
    }
}

for loc, updates in other_locales.items():
    loc_file = os.path.join(I18N, f"messages-{loc}.ts")
    if not os.path.exists(loc_file):
        print(f"File not found: {loc_file}")
        continue
    txt = open(loc_file, "r", encoding="utf-8").read()
    for k, v in updates.items():
        escaped_v = v.replace('"', '\\"')
        if k in ["todayDesk", "todayNfl", "todayTnf", "tonight", "tonightBlurb", "f1Title", "f1Blurb"]:
            txt = re.sub(rf'({k}:\s*")[^"]*(")', rf'\g<1>{escaped_v}\g<2>', txt)
        elif "_" in k:
            sport, prop = k.split("_", 1)
            sport_m = re.search(rf'({sport}:\s*\{{[^}}]*?{prop}:\s*")[^"]*(")', txt)
            if sport_m:
                txt = txt[:sport_m.start(1)] + f'{sport_m.group(1)}{escaped_v}{sport_m.group(2)}' + txt[sport_m.end():]
    open(loc_file, "w", encoding="utf-8").write(txt)
    print(f"Updated messages-{loc}.ts.")

print("All UI messages updated successfully.")
