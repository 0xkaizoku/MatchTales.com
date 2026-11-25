# Update playground.ts, messages.ts (en + fr), and messages-*.ts (es, de, it, pl, zh, ja, ko, ar) for 2026-11-26.
import os
import json
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
I18N = os.path.join(ROOT, "frontend", "src", "i18n")

# ---------------------------------------------------------
# 1. Update PLAYGROUND in frontend/src/i18n/playground.ts
# ---------------------------------------------------------
pg_path = os.path.join(I18N, "playground.ts")
pg_txt = open(pg_path, "r", encoding="utf-8").read()

pg_updates = {
    "en": {
        "pinFinal": "Davis Cup Bologna: Italy 1-0 South Korea (Musetti d. Hong 6-0, 7-6); Czechia d. Canada 2-0. Turin: Alcaraz d. Zverev 6-2, 7-6(7) unbeaten.",
        "week1Closed": "Thanksgiving Football: Bears (8-2) at Lions (8-2) 1:00 PM ET, Eagles at Cowboys 4:30 PM ET, Chiefs at Bills (9-1) 8:20 PM ET.",
        "week1Sub": "8-2 Lions host 8-2 Bears after Wed Netflix Packers-Rams (6-4). Week 11 Final: Texans 26-3 Colts (TEX 4-7, IND 3-8).",
        "countdownTnf": "THANKSGIVING DAY: Bears at Lions (1:00 PM ET CBS). Eagles at Cowboys (4:30 PM ET FOX). Chiefs at Bills (8:20 PM ET NBC).",
        "gridAfterMadrid": "Round 22 · Qatar GP at Lusail (27-29 Nov, standard format)",
        "barsPoints": "Antonelli (402) & Mercedes (666) Champions; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (MW11): Arsenal 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Select a club. Arsenal lead on 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "UCL MD5 Tue: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoli. PL: Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic Final: Marco Penge wins 4-way playoff on 1st extra hole at -16 (266) over Haotong Li and Thorbjornsen.",
    },
    "fr": {
        "pinFinal": "Coupe Davis Bologne : Italie 1-0 Coree du Sud (Musetti bat Hong 6-0, 7-6) ; Tchequie 2-0 Canada. Turin : Alcaraz bat Zverev 6-2, 7-6(7).",
        "week1Closed": "Thanksgiving NFL : Bears (8-2) chez les Lions (8-2) 13h00 ET, Eagles-Cowboys 16h30, Chiefs-Bills (9-1) 20h20 ET.",
        "week1Sub": "Lions et Bears (8-2) a Ford Field apres Packers-Rams mercredi soir sur Netflix. S11 : Texans 26-3 Colts (4-7 vs 3-8).",
        "countdownTnf": "THANKSGIVING NFL : Bears chez les Lions (13h00 ET CBS). Eagles chez les Cowboys (16h30 ET FOX). Chiefs chez les Bills (20h20 ET NBC).",
        "gridAfterMadrid": "Manche 22 · GP du Qatar a Lusail (27-29 nov, format classique)",
        "barsPoints": "Antonelli (402) et Mercedes (666) Champions ; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (J11) : Arsenal 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Selectionnez un club. Arsenal 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "LDC J5 mardi : Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Naples. PL : Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic : Marco Penge s'impose en playoff a quatre a -16 (266) devant Haotong Li et Thorbjornsen.",
    },
    "es": {
        "pinFinal": "Copa Davis Bolonia: Italia 1-0 Corea del Sur (Musetti d Hong 6-0, 7-6); Chequia 2-0 Canada. Turin: Alcaraz 6-2, 7-6(7) Zverev.",
        "week1Closed": "Accion de Gracias NFL: Bears (8-2) en Lions (8-2) 1:00 PM ET, Eagles en Cowboys 4:30 PM, Chiefs en Bills (9-1) 8:20 PM ET.",
        "week1Sub": "Lions y Bears (8-2) chocan en Ford Field tras Packers-Rams en Netflix. Semana 11: Texans 26-3 Colts (4-7 vs 3-8).",
        "countdownTnf": "DIA DE ACCION DE GRACIAS: Bears en Lions (1:00 PM ET CBS). Eagles en Cowboys (4:30 PM FOX). Chiefs en Bills (8:20 PM NBC).",
        "gridAfterMadrid": "Ronda 22 · GP de Catar en Lusail (27-29 nov, formato clasico)",
        "barsPoints": "Antonelli (402) y Mercedes (666) Campeones; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (J11): Arsenal 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Selecciona un club. Arsenal 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "UCL J5 martes: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoles. PL: Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic: Marco Penge gana el playoff cuadruple en -16 (266) ante Haotong Li y Thorbjornsen.",
    },
    "de": {
        "pinFinal": "Davis Cup Bologna: Italien 1:0 Suedkorea (Musetti 6:0, 7:6 Hong); Tschechien 2:0 Kanada. Turin: Alcaraz schlaegt Zverev 6:2, 7:6(7).",
        "week1Closed": "Thanksgiving Football: Bears (8-2) bei Lions (8-2) 1:00 PM ET, Eagles bei Cowboys 4:30 PM, Chiefs bei Bills (9-1) 8:20 PM ET.",
        "week1Sub": "Lions und Bears (beide 8-2) im Ford Field nach Packers-Rams auf Netflix. Woche 11: Texans 26:3 Colts (TEX 4-7, IND 3-8).",
        "countdownTnf": "THANKSGIVING DAY: Bears bei Lions (1:00 PM ET CBS). Eagles bei Cowboys (4:30 PM FOX). Chiefs bei Bills (8:20 PM NBC).",
        "gridAfterMadrid": "Runde 22 · Katar GP in Lusail (27.-29. Nov., Standard-Format)",
        "barsPoints": "Antonelli (402) und Mercedes (666) Weltmeister; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (11. Sp.): Arsenal 28 Pkt., Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Klub waehlen. Arsenal fuehrt mit 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "UCL 5. Sp. Di: Real Madrid 5:1 PSV, Arsenal 1:1 Dortmund, Man City 2:2 Napoli. PL: Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic: Marco Penge siegt im Vierer-Playoff bei -16 (266) gegen Haotong Li und Thorbjornsen.",
    },
    "it": {
        "pinFinal": "Coppa Davis Bologna: Italia 1-0 Corea del Sud (Musetti 6-0, 7-6 Hong); Rep. Ceca 2-0 Canada. Torino: Alcaraz 6-2, 7-6(7) Zverev.",
        "week1Closed": "Thanksgiving NFL: Bears (8-2) a Detroit (8-2) 19:00, Eagles a Dallas 22:30, Chiefs a Buffalo (9-1) 02:20.",
        "week1Sub": "Lions e Bears (8-2) al Ford Field dopo Packers-Rams su Netflix. Week 11: Texans 26-3 Colts (4-7 vs 3-8).",
        "countdownTnf": "THANKSGIVING DAY: Bears a Detroit (19:00). Eagles a Dallas (22:30). Chiefs a Buffalo (02:20).",
        "gridAfterMadrid": "Round 22 · GP del Qatar a Lusail (27-29 nov, formato classico)",
        "barsPoints": "Antonelli (402) e Mercedes (666) Campioni; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (11a g.): Arsenal 28 pt, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Seleziona un club. Arsenal 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "UCL 5a g. mar: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoli. PL: Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic: Marco Penge trionfa allo spareggio a quattro a -16 (266) contro Haotong Li e Thorbjornsen.",
    },
    "pl": {
        "pinFinal": "Puchar Davisa Bolonia: Wlochy 1:0 Korea Pld (Musetti 6:0, 7:6 Hong); Czechy 2:0 Kanada. Turyn: Alcaraz 6:2, 7:6(7) Zverev.",
        "week1Closed": "Thanksgiving NFL: Bears (8-2) u Lions (8-2) 19:00 PL, Eagles u Cowboys 22:30, Chiefs u Bills (9-1) 02:20.",
        "week1Sub": "Lions i Bears (po 8-2) graja po Packers-Rams na Netflixie. 11. tydzien: Texans 26:3 Colts (4-7 vs 3-8).",
        "countdownTnf": "THANKSGIVING DAY: Bears u Lions (19:00). Eagles u Cowboys (22:30). Chiefs u Bills (02:20).",
        "gridAfterMadrid": "Runda 22 · GP Kataru w Lusail (27-29 listopada, format klasyczny)",
        "barsPoints": "Antonelli (402) i Mercedes (666) Mistrzowie; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (11. kol.): Arsenal 28 pkt, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Wybierz klub. Arsenal 28 pkt, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "LM 5. kol. wt: Real Madryt 5:1 PSV, Arsenal 1:1 Dortmund, Man City 2:2 Napoli. PL: Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic: Marco Penge wygrywa czteroosobowa dogrywke na -16 (266) przed Haotongiem Li i Thorbjornsenem.",
    },
    "zh": {
        "pinFinal": "戴维斯杯博洛尼亚：意大利1-0韩国（穆塞蒂6-0、7-6胜洪性成）；捷克2-0加拿大。都灵：阿尔卡拉斯两盘击败兹维列夫夺冠。",
        "week1Closed": "NFL感恩节：熊队（8-2）客战雄狮（8-2）美东13:00，老鹰战牛仔16:30，酋长战比尔（9-1）20:20。",
        "week1Sub": "周三网飞包装工对公羊后，8胜2负雄狮与熊队交锋。第11周：德州人26-3小马（4-6对3-8）。",
        "countdownTnf": "感恩节大赛：熊队战雄狮（13:00 CBS）。老鹰战牛仔（16:30 FOX）。酋长战比尔（20:20 NBC）。",
        "gridAfterMadrid": "第22站 · 卡塔尔大奖赛卢赛尔常规赛制（11月27-29日）",
        "barsPoints": "安东内利（402）与梅赛德斯（666）加冕；维斯塔潘304，汉密尔顿267，拉塞尔264，诺里斯264。",
        "tableAfterMonday": "英超（第11轮）：阿森纳28分，布莱顿22分，曼城22分，利物浦21分，伯恩茅斯18分。",
        "pinClub": "选择俱乐部。阿森纳28分领跑，布莱顿22，曼城22，利物浦21，伯恩茅斯18，布伦特福德17。",
        "plFootnote": "欧冠第5轮周二：皇马5-1埃因霍温，阿森纳1-1多特，曼城2-2那不勒斯。英超：阿森纳28，布莱顿22，曼城22。",
        "majorsDone": "RSM精英赛：马尔科·彭奇四人加洞赛首洞以-16（266杆）力压李昊桐与索比约恩森夺冠。",
    },
    "ja": {
        "pinFinal": "デビスカップ・ボローニャ：イタリア1-0韓国（ムゼッティ6-0、7-6）；チェコ2-0カナダ。トリノ：アルカラス全勝V。",
        "week1Closed": "感謝祭NFL：ベアーズ(8-2)対ライオンズ(8-2)13:00、イーグルス対カウボーイズ16:30、チーフス対ビルズ(9-1)20:20。",
        "week1Sub": "水曜Netflixパッカーズ対ラムズに続き8勝2敗同士が激突。第11週：テキサンズ26-3コルツ。",
        "countdownTnf": "感謝祭：ベアーズ対ライオンズ(13:00 CBS)。イーグルス対カウボーイズ(16:30 FOX)。チーフス対ビルズ(20:20 NBC)。",
        "gridAfterMadrid": "第22戦 · カタールGP ルサイル通常開催（11月27-29日）",
        "barsPoints": "アントネッリ(402)＆メルセデス(666)王者；フェルスタッペン304、ハミルトン267、ラッセル264、ノリス264。",
        "tableAfterMonday": "プレミアリーグ（第11節）：アーセナル28、ブライトン22、マンC 22、リヴァプール21、ボーンマス18。",
        "pinClub": "クラブ選択：アーセナル28、ブライトン22、マンC 22、リヴァプール21、ボーンマス18、ブレントフォード17。",
        "plFootnote": "CL第5節火曜：Rマドリード5-1 PSV、アーセナル1-1ドルトムント、マンC 2-2ナポリ。PL：アーセナル28、シティ22。",
        "majorsDone": "RSMクラシック：マルコ・ペンジが-16（266）4人POを制し李昊桐らを抑えPGAツアー初優勝。",
    },
    "ko": {
        "pinFinal": "데이비스 컵 볼로냐: 이탈리아 1-0 한국 (무세티 6-0, 7-6 승); 체코 2-0 캐나다. 토리노: 알카라스 무패 우승.",
        "week1Closed": "추수감사절 NFL: 베어스(8-2) vs 라이온스(8-2) 13:00, 이글스 vs 카우보이스 16:30, 치프스 vs 빌스(9-1) 20:20.",
        "week1Sub": "수요일 넷플릭스 패커스-램스전에 이어 8승 2패 동률 격돌. 11주차: 텍산스 26-3 콜츠(TEX 4-7, IND 3-8).",
        "countdownTnf": "추수감사절 데이: 베어스 vs 라이온스(13:00 CBS). 이글스 vs 카우보이스(16:30 FOX). 치프스 vs 빌스(20:20 NBC).",
        "gridAfterMadrid": "22라운드 · 카타르 GP 루사일 일반 포맷 (11월 27-29일)",
        "barsPoints": "안토넬리(402) 및 메르세데스(666) 우승; 페르스타펜 304, 해밀턴 267, 러셀 264, 노리스 264.",
        "tableAfterMonday": "프리미어리그(11R): 아스널 28점, 브라이튼 22, 맨시티 22, 리버풀 21, 본머스 18.",
        "pinClub": "클럽 선택: 아스널 28, 브라이튼 22, 맨시티 22, 리버풀 21, 본머스 18, 브렌트퍼드 17.",
        "plFootnote": "UCL 5차전 화: 레알 마드리드 5-1 PSV, 아스널 1-1 도르트문트, 맨시티 2-2 나폴리. PL: 아스널 28, 브라이튼 22, 맨시티 22.",
        "majorsDone": "RSM 클래식: 마르코 펜지가 -16(266) 4인 연장전 첫 홀에서 리하오퉁 등을 제치고 생애 첫 우승.",
    },
    "ar": {
        "pinFinal": "كاس ديفيز بولونيا: ايطاليا 1-0 كوريا الجنوبية (موسيتي 6-0 و7-6 هونغ)؛ التشيك 2-0 كندا. تورينو: الكاراز بطلا.",
        "week1Closed": "عيد الشكر NFL: بيرز (8-2) ضد لايونز (8-2) 1:00 ظهرا، ايغلز ضد كاوبويز 4:30، تشيفز ضد بيلز (9-1) 8:20.",
        "week1Sub": "صدام 8-2 في فورد فيلد بعد مواجهة باكرز ورامز الاربعاء على نتفليكس. الاسبوع 11: تكسانز 26-3 كولتس.",
        "countdownTnf": "يوم عيد الشكر: بيرز ضد لايونز (1:00 CBS). ايغلز ضد كاوبويز (4:30 FOX). تشيفز ضد بيلز (8:20 NBC).",
        "gridAfterMadrid": "الجولة 22 · جائزة قطر الكبرى في لوسيل (27-29 نوفمبر، الصيغة التقليدية)",
        "barsPoints": "انتونيللي (402) ومرسيدس (666) ابطال العالم؛ فيرستابن 304، هاميلتون 267، راسل 264، نوريس 264.",
        "tableAfterMonday": "الدوري الانجليزي (11): ارسنال 28، برايتون 22، مانشستر سيتي 22، ليفربول 21، بورنموث 18.",
        "pinClub": "اختر ناديا. ارسنال 28، برايتون 22، مانشستر سيتي 22، ليفربول 21، بورنموث 18، برينتفورد 17.",
        "plFootnote": "دوري الابطال الثلاثاء: ريال مدريد 5-1 ايندهوفن، ارسنال 1-1 دورتموند، مانشستر سيتي 2-2 نابولي.",
        "majorsDone": "بطولة RSM: ماركو بينجي يحسم التمايز الرباعي عند -16 (266) على حساب لي هاوتونغ وثوربيورنسن.",
    },
}

# Parse existing PLAYGROUND keys cleanly per locale block
header_part, body_part = pg_txt.split("export const PLAYGROUND: Record<Locale, PlaygroundCopy> = {", 1)
obj_part, footer_part = body_part.rsplit("};", 1)
obj_text = "{" + obj_part + "}"
pg_data = json.loads(obj_text)
for loc, upd in pg_updates.items():
    for k, v in upd.items():
        pg_data[loc][k] = v

pg_out = header_part + "export const PLAYGROUND: Record<Locale, PlaygroundCopy> = " + json.dumps(pg_data, ensure_ascii=False, indent=2) + ";" + footer_part
if "\u2014" in pg_out or "--" in pg_out:
    raise ValueError("Em-dash or double-hyphen in playground.ts!")
open(pg_path, "w", encoding="utf-8").write(pg_out)
print("Cleanly updated playground.ts across all 10 locales.")

# ---------------------------------------------------------
# 2. Desk / Sports / Home message updates across all 10 locales
# ---------------------------------------------------------
messages_updates = {
    "en": {
        "common_todayDesk": "Thursday desk: NFL Thanksgiving (8-2 Bears at 8-2 Lions, Chiefs 8-2 at Bills 9-1) after Wed Packers-Rams. UCL MD5 (Real Madrid 5-1 PSV, Sabah 0-1 Barca HT). Davis Cup Bologna. Qatar GP Friday.",
        "common_todayNfl": "Thanksgiving Day: Bears (8-2) at Lions (8-2) 1:00 PM ET CBS, Eagles (3-7) at Cowboys (5-6) 4:30 PM ET FOX, Chiefs (8-2) at Bills (9-1) 8:20 PM ET NBC.",
        "common_todayTnf": "Thanksgiving Eve Wed 8:15 PM ET (Netflix): Packers (6-4) at Rams (6-4). Thu opener: Bears at Lions in Ford Field showdown.",
        "football_tagline": "Thanksgiving Football: 8-2 Bears at 8-2 Lions open Thursday tripleheader after Wed Packers-Rams on Netflix.",
        "football_liveNow": "Thanksgiving Eve Wed Netflix: Packers (6-4) at Rams (6-4). Thu: Bears (8-2) at Lions (8-2) 1 PM ET, Eagles at Cowboys 4:30 PM, Chiefs (8-2) at Bills (9-1) 8:20 PM ET.",
        "football_pulse": "NFL WEEK 12 THANKSGIVING: IDENTICAL 8-2 LIONS AND BEARS CLASH FOR NFC NORTH LEAD; CHIEFS VISIT BILLS NIGHTCAP",
        "tennis_tagline": "Davis Cup Final 8 in Bologna: Defending champions Italy lead South Korea 1-0; Alcaraz crowned Turin champion.",
        "tennis_liveNow": "Davis Cup Bologna: Czechia d. Canada 2-0; Italy 1-0 South Korea (Musetti d. Hong 6-0, 7-6(5), Cobolli vs Kwon). Thu: GB vs Germany. Turin: Alcaraz d. Zverev 6-2, 7-6(7).",
        "tennis_pulse": "DAVIS CUP FINALS: ITALY LEAD SOUTH KOREA IN BOLOGNA QUARTERFINALS; ALCARAZ COMPLETES 5-0 TURIN TITLE RUN",
        "f1_tagline": "Qatar GP next (27-29 Nov): Verstappen carries chaotic Las Vegas victory into Lusail standard weekend.",
        "f1_liveNow": "Vegas GP Final: 1. Verstappen (75th win), 2. Norris (+0.639s), 3. Piastri (from P17); Russell crashed Lap 48. Standings: Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264.",
        "f1_pulse": "FORMULA 1: VERSTAPPEN TAKES LAS VEGAS THROUGH 35 LEAD CHANGES AS MCLAREN SLASH RED BULL GAP TO 9 POINTS",
        "soccer_tagline": "Champions League MD5: Real Madrid storm past PSV 5-1; Sabah 0-1 Barcelona HT as Wednesday night slate opens.",
        "soccer_liveNow": "UCL Tue: Real Madrid 5-1 PSV (Mbappe 2), Arsenal 1-1 Dortmund, Man City 2-2 Napoli. Wed HT: Sabah 0-1 Barcelona. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "soccer_pulse": "CHAMPIONS LEAGUE MD5: REAL MADRID HIT 15 POINTS AT SUMMIT; LIVERPOOL ROUT MAN UTD 4-0 IN POCHETTINO BOW",
        "basketball_tagline": "Emirates NBA Cup heats up before Thanksgiving break: Mavericks stun Nuggets 120-101; Celtics drop 131 on Wizards.",
        "basketball_liveNow": "Tue Cup Finals: Mavericks 120-101 Nuggets (Flagg 24/6/12); Celtics 131-116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104-86 Magic (Joe 21). Wed 9 games; Thu off.",
        "basketball_pulse": "EMIRATES NBA CUP: MAVS CRUISE BEHIND COOPER FLAGG AND TATUM EXPLODES FOR 41 AS LEAGUE NEARS THANKSGIVING PAUSE",
        "golf_tagline": "Marco Penge captures maiden PGA Tour victory in dramatic four-man Sea Island playoff at The RSM Classic.",
        "golf_liveNow": "RSM Classic Final (23 Nov): Marco Penge (-16, 266) wins 1st playoff hole over Haotong Li, Michael Thorbjornsen, and Max Greyserman. Next: Hero World Challenge (3-6 Dec).",
        "golf_pulse": "PGA TOUR: MARCO PENGE CAPS FOUR-WAY PLAYOFF AT SEA ISLAND FOR MAIDEN WIN AND 2027 MASTERS TICKET",
        "home_tonight": "Thursday desk",
        "home_tonightBlurb": "Thanksgiving NFL: 8-2 Bears at 8-2 Lions open Thursday (1:00 PM ET CBS) and Chiefs at 9-1 Bills cap the night after Wed Packers-Rams on Netflix. UCL MD5: Real Madrid 5-1 PSV, Sabah 0-1 Barcelona HT. Davis Cup Bologna Live: Italy 1-0 South Korea. Qatar GP Friday.",
        "home_plTitle": "Arsenal lead Premier League on 28; Real Madrid hit 15 points atop Champions League",
        "home_plBlurb": "PL after MW11: Arsenal 28, Brighton 22, Man City 22, Liverpool 21 (Liverpool 4-0 Man Utd in Pochettino debut, Man City 1-1 Fulham, Newcastle 2-2 Arsenal). UCL Tuesday: Real Madrid 5-1 PSV (Mbappe 2, Bellingham), Arsenal 1-1 Dortmund.",
        "home_f1Title": "Qatar Grand Prix next: Verstappen brings 75th victory to Lusail with P3 split by three points",
        "home_f1Blurb": "Antonelli (402) and Mercedes (666) hold both 2026 titles, while Verstappen sits 2nd on 304 after conquering Las Vegas. Just 3 points divide Hamilton (267) from Russell and Norris (264), and McLaren (431) sit 9 behind Red Bull (440).",
    },
    "fr": {
        "common_todayDesk": "Bureau du jeudi : Thanksgiving NFL (Bears 8-2 chez Lions 8-2, Chiefs 8-2 chez Bills 9-1) apres Packers-Rams mercredi. LDC J5 (Real Madrid 5-1 PSV, Sabah 0-1 Barcelone MT). Coupe Davis a Bologne.",
        "common_todayNfl": "Thanksgiving NFL : Bears (8-2) chez Lions (8-2) 13h00 ET CBS, Eagles (3-7) chez Cowboys (5-6) 16h30 ET FOX, Chiefs (8-2) chez Bills (9-1) 20h20 ET NBC.",
        "common_todayTnf": "Mercredi soir sur Netflix : Packers (6-4) chez Rams (6-4) avant le choc Bears-Lions a Ford Field.",
        "football_tagline": "Thanksgiving NFL : Lions et Bears (8-2) ouvrent jeudi apres Packers-Rams mercredi sur Netflix.",
        "football_liveNow": "Mercredi Netflix : Packers (6-4) chez Rams (6-4). Jeudi : Bears (8-2) chez Lions (8-2) 13h00 ET, Eagles-Cowboys 16h30, Chiefs-Bills (9-1) 20h20 ET.",
        "football_pulse": "NFL THANKSGIVING : LIONS ET BEARS A 8-2 POUR LA TETE DE LA NFC NORD ; CHIEFS CHEZ BILLS EN SOIREE",
        "tennis_tagline": "Coupe Davis a Bologne : L'Italie tenante mene 1-0 face a la Coree du Sud ; Alcaraz sacre a Turin.",
        "tennis_liveNow": "Coupe Davis Bologne : Tchequie 2-0 Canada ; Italie 1-0 Coree du Sud (Musetti 6-0, 7-6 Hong, Cobolli-Kwon). Jeudi : GB-Allemagne. Turin : Alcaraz bat Zverev 6-2, 7-6(7).",
        "tennis_pulse": "COUPE DAVIS : L'ITALIE MENE A BOLOGNE ALORS QU'ALCARAZ SAVOURE SON SACRE INVAINCU A TURIN",
        "f1_tagline": "GP du Qatar (27-29 nov) : Verstappen emporte son succes de Las Vegas vers le format classique de Lusail.",
        "f1_liveNow": "Las Vegas GP : 1. Verstappen (75e victoire), 2. Norris (+0,639s), 3. Piastri (de P17). Pilotes : Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264.",
        "f1_pulse": "FORMULE 1 : VERSTAPPEN REMPORTE VEGAS APRES 35 RELAIS EN TETE ET MCLAREN REVIENT A 9 PTS DE RED BULL",
        "soccer_tagline": "Ligue des champions J5 : Le Real Madrid ecrase le PSV 5-1 ; Sabah 0-1 Barcelone a la pause.",
        "soccer_liveNow": "LDC mardi : Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Naples. Mercredi MT : Sabah 0-1 Barcelone. PL : Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "soccer_pulse": "LIGUE DES CHAMPIONS : REAL MADRID SEUL A 15 POINTS ; LIVERPOOL BALAIE MAN UTD 4-0 POUR LES DEBUTS DE POCHETTINO",
        "basketball_tagline": "Avant la pause de Thanksgiving NBA : Dallas surprend Denver 120-101 et Boston bat Washington 131-116.",
        "basketball_liveNow": "NBA Cup mardi : Mavericks 120-101 Nuggets (Flagg 24/6/12) ; Celtics 131-116 Wizards (Tatum 41, George 28 ; Davis 33/13) ; Pistons 104-86 Magic (Joe 21). Jeudi pause.",
        "basketball_pulse": "EMIRATES NBA CUP : COOPER FLAGG ET TATUM (41 PTS) BRILLENT AVANT LA RELACHE DE THANKSGIVING",
        "golf_tagline": "Marco Penge decroche sa premiere victoire sur le PGA Tour en barrage a quatre au RSM Classic.",
        "golf_liveNow": "RSM Classic (23 nov) : Marco Penge (-16, 266) gagne au 1er trou de playoff devant Haotong Li, Michael Thorbjornsen et Max Greyserman. Suite : Hero World Challenge (3-6 dec).",
        "golf_pulse": "PGA TOUR : MARCO PENGE S'IMPOSE EN BARRAGE A SEA ISLAND POUR UN PREMIER SACRE SUR LE CIRCUIT",
        "home_tonight": "Bureau du jeudi",
        "home_tonightBlurb": "Thanksgiving NFL : Bears (8-2) chez Lions (8-2) puis Chiefs chez Bills (9-1) apres Packers-Rams mercredi. LDC J5 : Real Madrid 5-1 PSV, Sabah 0-1 Barcelone MT. Coupe Davis en direct : Italie 1-0 Coree du Sud.",
        "home_plTitle": "Arsenal mene la Premier League avec 28 points ; le Real Madrid seul en tete de la C1",
        "home_plBlurb": "PL J11 : Arsenal 28, Brighton 22, Man City 22, Liverpool 21 (Liverpool 4-0 Man Utd, Man City 1-1 Fulham, Newcastle 2-2 Arsenal). LDC : Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund.",
        "home_f1Title": "Cap sur Lusail : Verstappen emmene sa 75e victoire au Qatar, trois points pour le podium mondial",
        "home_f1Blurb": "Antonelli (402) et Mercedes (666) sont deja sacres, Verstappen pointe a 304 pts apres Las Vegas. Hamilton (267) ne devance Russell et Norris (264) que de trois points.",
    },
    "es": {
        "common_todayDesk": "Mesa del jueves: Thanksgiving NFL (Bears 8-2 en Lions 8-2, Chiefs 8-2 en Bills 9-1) tras Packers-Rams en Netflix. UCL J5 (Real Madrid 5-1 PSV, Sabah 0-1 Barcelona descanso). Copa Davis en Bolonia.",
        "common_todayNfl": "Dia de Accion de Gracias: Bears (8-2) en Lions (8-2) 1:00 PM ET CBS, Eagles (3-7) en Cowboys (5-6) 4:30 PM ET FOX, Chiefs (8-2) en Bills (9-1) 8:20 PM ET NBC.",
        "common_todayTnf": "Miercoles en Netflix: Packers (6-4) en Rams (6-4) antes del Lions-Bears de Ford Field.",
        "football_tagline": "Accion de Gracias NFL: Lions y Bears (8-2) abren el jueves tras Packers-Rams en Netflix.",
        "football_liveNow": "Miercoles Netflix: Packers (6-4) en Rams (6-4). Jueves: Bears (8-2) en Lions (8-2) 1 PM ET, Eagles-Cowboys 4:30 PM, Chiefs (8-2) en Bills (9-1) 8:20 PM ET.",
        "football_pulse": "NFL THANKSGIVING: LIONS Y BEARS (8-2) SE JUEGAN LA NFC NORTE; CHIEFS VISITA A BILLS EN ESTELAR",
        "tennis_tagline": "Copa Davis Bolonia: Italia lidera 1-0 a Corea del Sur; Carlos Alcaraz campeon invicto en Turin.",
        "tennis_liveNow": "Copa Davis Bolonia: Chequia 2-0 Canada; Italia 1-0 Corea (Musetti 6-0, 7-6 Hong, Cobolli-Kwon). Jueves: GB-Alemania. Turin: Alcaraz d. Zverev 6-2, 7-6(7).",
        "tennis_pulse": "COPA DAVIS: ITALIA MANDA EN BOLONIA TRAS LA CORONA INVICTA DE ALCARAZ EN TURIN",
        "f1_tagline": "Proxima parada GP de Catar (27-29 nov): Verstappen lleva su triunfo 75 a Lusail en formato clasico.",
        "f1_liveNow": "Las Vegas GP: 1. Verstappen (75.a victoria), 2. Norris (+0,639s), 3. Piastri (desde P17). Pilotos: Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264.",
        "f1_pulse": "FORMULA 1: VERSTAPPEN VENCE EN LAS VEGAS CON 35 CAMBIOS DE LIDER Y MCLAREN SE ACERCA A RED BULL",
        "soccer_tagline": "Champions League J5: Real Madrid golea 5-1 al PSV; Sabah 0-1 Barcelona al descanso.",
        "soccer_liveNow": "UCL martes: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoles. Mierc desc: Sabah 0-1 Barcelona. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "soccer_pulse": "CHAMPIONS LEAGUE: REAL MADRID PLENO DE 15 PUNTOS; LIVERPOOL GOLEA 4-0 AL MAN UTD DE POCHETTINO",
        "basketball_tagline": "Antes del paron de Accion de Gracias: Dallas vence 120-101 a Denver y Boston 131-116 a Washington.",
        "basketball_liveNow": "NBA Cup martes: Mavericks 120-101 Nuggets (Flagg 24/6/12); Celtics 131-116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104-86 Magic (Joe 21). Jueves descanso.",
        "basketball_pulse": "EMIRATES NBA CUP: COOPER FLAGG Y JAYSON TATUM (41 PTS) BRILLAN ANTES DE LA PAUSA DEL JUEVES",
        "golf_tagline": "Marco Penge gana su primer titulo PGA Tour en desempate cuadruple en The RSM Classic.",
        "golf_liveNow": "RSM Classic (23 nov): Marco Penge (-16, 266) vence en el primer hoyo extra a Haotong Li, Michael Thorbjornsen y Max Greyserman. Siguiente: Hero World Challenge (3-6 dic).",
        "golf_pulse": "PGA TOUR: MARCO PENGE CONQUISTA SEA ISLAND EN DESEMPATE PARA LOGRAR SU PRIMER TROFEO",
        "home_tonight": "Mesa del jueves",
        "home_tonightBlurb": "Thanksgiving NFL: Bears (8-2) en Lions (8-2) y Chiefs en Bills (9-1) tras Packers-Rams en Netflix. UCL J5: Real Madrid 5-1 PSV, Sabah 0-1 Barcelona al descanso. Copa Davis en directo: Italia 1-0 Corea del Sur.",
        "home_plTitle": "Arsenal domina la Premier con 28 puntos; Real Madrid lider solitario de la Champions",
        "home_plBlurb": "PL tras J11: Arsenal 28, Brighton 22, Man City 22, Liverpool 21 (Liverpool 4-0 Man Utd, Man City 1-1 Fulham, Newcastle 2-2 Arsenal). UCL: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund.",
        "home_f1Title": "Llega el GP de Catar: Verstappen tras su 75.a victoria y tres puntos por el podio en Lusail",
        "home_f1Blurb": "Con Antonelli (402) y Mercedes (666) campeones, Verstappen suma 304 tras Las Vegas. Tres puntos separan a Hamilton (267) de Russell y Norris (264), con McLaren a nueve de Red Bull.",
    },
    "de": {
        "common_todayDesk": "Donnerstag-Desk: Thanksgiving NFL (Bears 8-2 bei Lions 8-2, Chiefs 8-2 bei Bills 9-1) nach Packers-Rams. UCL 5. Sp. (Real 5:1 PSV, Sabah 0:1 Barcelona HZ). Davis Cup Bologna. Katar GP am Freitag.",
        "common_todayNfl": "Thanksgiving Day: Bears (8-2) bei Lions (8-2) 1:00 PM ET CBS, Eagles (3-7) bei Cowboys (5-6) 4:30 PM FOX, Chiefs (8-2) bei Bills (9-1) 8:20 PM NBC.",
        "common_todayTnf": "Mittwoch auf Netflix: Packers (6-4) bei Rams (6-4) vor dem Duell Lions gegen Bears im Ford Field.",
        "football_tagline": "Thanksgiving Football: 8-2 Lions gegen 8-2 Bears eroeffnen Donnerstag nach Packers-Rams.",
        "football_liveNow": "Mittwoch Netflix: Packers (6-4) bei Rams (6-4). Donnerstag: Bears bei Lions (1 PM ET), Eagles bei Cowboys (4:30 PM), Chiefs bei Bills (9-1, 8:20 PM ET).",
        "football_pulse": "NFL THANKSGIVING: LIONS UND BEARS (8-2) UM NFC NORTH; CHIEFS BEI BILLS IM TOPSPIEL",
        "tennis_tagline": "Davis Cup Final 8 Bologna: Titelverteidiger Italien fuehrt 1:0; Alcaraz Turin-Champion.",
        "tennis_liveNow": "Davis Cup Bologna: Tschechien 2:0 Kanada; Italien 1:0 Suedkorea (Musetti 6:0, 7:6 Hong, Cobolli-Kwon). Do: GB-Deutschland. Turin: Alcaraz 6:2, 7:6(7) Zverev.",
        "tennis_pulse": "DAVIS CUP: ITALIEN FUEHRT IN BOLOGNA NACH ALCARAZ' UNGESCHLAGENEM TURIN-TRIUMPH",
        "f1_tagline": "Katar GP (27.-29. Nov.): Verstappen bringt Las-Vegas-Sieg nach Lusail im Standard-Format.",
        "f1_liveNow": "Vegas GP: 1. Verstappen (75. Sieg), 2. Norris (+0,639s), 3. Piastri (von P17). WM-Stand: Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264.",
        "f1_pulse": "FORMEL 1: VERSTAPPEN GEWINNT LAS VEGAS NACH 35 FUEHRUNGSWECHSELN; MCLAREN NUR 9 PKT HINTER RED BULL",
        "soccer_tagline": "Champions League 5. Sp.: Real Madrid schlaegt PSV 5:1; Sabah 0:1 Barcelona zur Pause.",
        "soccer_liveNow": "UCL Di: Real Madrid 5:1 PSV, Arsenal 1:1 Dortmund, Man City 2:2 Napoli. Mi HZ: Sabah 0:1 Barcelona. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "soccer_pulse": "CHAMPIONS LEAGUE: REAL MADRID MIT 15 PUNKTEN GANZ OBEN; LIVERPOOL 4:0 GEGEN POCHETTINOS MAN UTD",
        "basketball_tagline": "NBA vor Thanksgiving-Pause: Dallas bezwingt Denver 120:101; Boston schlaegt Wizards 131:116.",
        "basketball_liveNow": "NBA Cup Di: Mavericks 120:101 Nuggets (Flagg 24/6/12); Celtics 131:116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104:86 Magic (Joe 21). Do spielfrei.",
        "basketball_pulse": "EMIRATES NBA CUP: COOPER FLAGG UND TATUM (41 PKT) GLANZEN VOR DER THANKSGIVING-PAUSE",
        "golf_tagline": "Marco Penge gewinnt Vierer-Playoff auf Sea Island fuer ersten PGA-Tour-Titel beim RSM Classic.",
        "golf_liveNow": "RSM Classic Finale (23. Nov.): Marco Penge (-16, 266) siegt am 1. Extraloch vor Haotong Li, Michael Thorbjornsen und Max Greyserman. Weiter: Hero World Challenge (3.-6. Dez.).",
        "golf_pulse": "PGA TOUR: MARCO PENGE HOLT ERSTEN TITEL IM PLAYOFF AUF SEA ISLAND UND SICHERTSICH TOURKARTE",
        "home_tonight": "Donnerstag-Desk",
        "home_tonightBlurb": "Thanksgiving NFL: Bears (8-2) bei Lions (8-2) und Chiefs bei Bills (9-1) nach Packers-Rams. UCL 5. Sp.: Real Madrid 5:1 PSV, Sabah 0:1 Barcelona zur Pause. Davis Cup live: Italien 1:0 Suedkorea.",
        "home_plTitle": "Arsenal fuehrt die Premier League mit 28 Punkten an; Real Madrid makellos Erster in Europa",
        "home_plBlurb": "PL nach 11. Sp.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21 (Liverpool 4:0 Man Utd bei Pochettinos Debuet, City 1:1 Fulham, Newcastle 2:2 Arsenal). UCL: Real 5:1 PSV, Arsenal 1:1 Dortmund.",
        "home_f1Title": "Vorschau Katar GP: Verstappen reist mit 75. Sieg nach Lusail im engen Kampf um Platz drei",
        "home_f1Blurb": "Weltmeister Antonelli (402) und Mercedes (666) stehen fest, waehrend Verstappen nach Vegas 304 Punkte haelt. Nur 3 Punkte trennen Hamilton (267) von Russell und Norris (264).",
    },
    "it": {
        "common_todayDesk": "Desk del giovedi: Thanksgiving NFL (Bears 8-2 a Detroit 8-2, Chiefs 8-2 a Buffalo 9-1) dopo Packers-Rams. UCL 5a g. (Real Madrid 5-1 PSV, Sabah 0-1 Barcellona int.). Coppa Davis Bologna.",
        "common_todayNfl": "Ringraziamento: Bears (8-2) a Detroit (8-2) 19:00, Eagles a Dallas 22:30, Chiefs (8-2) a Buffalo (9-1) 02:20.",
        "common_todayTnf": "Mercoledi su Netflix: Packers (6-4) contro Rams (6-4) prima della sfida Bears-Lions al Ford Field.",
        "football_tagline": "Thanksgiving NFL: Lions e Bears (8-2) inaugurano il giovedi dopo Packers-Rams su Netflix.",
        "football_liveNow": "Mercoledi Netflix: Packers (6-4) a Los Angeles (6-4). Giovedi: Bears-Lions 19:00, Eagles-Cowboys 22:30, Chiefs-Bills (9-1) 02:20.",
        "football_pulse": "NFL THANKSGIVING: LIONS E BEARS (8-2) PER LA NFC NORTH; CHIEFS A BUFFALO IN NOTTURNA",
        "tennis_tagline": "Coppa Davis Bologna: Italia avanti 1-0 sulla Corea del Sud; Alcaraz campione imbattuto a Torino.",
        "tennis_liveNow": "Coppa Davis Bologna: Rep. Ceca 2-0 Canada; Italia 1-0 Corea (Musetti 6-0, 7-6 Hong, Cobolli-Kwon). Gio: GB-Germania. Torino: Alcaraz 6-2, 7-6(7) Zverev.",
        "tennis_pulse": "COPPA DAVIS: ITALIA IN VANTAGGIO A BOLOGNA DOPO IL TRIONFO IMBATTUTO DI ALCARAZ A TORINO",
        "f1_tagline": "GP del Qatar (27-29 nov): Verstappen porta il 75esimo trionfo a Lusail in formato classico.",
        "f1_liveNow": "Las Vegas GP: 1. Verstappen (75a vittoria), 2. Norris (+0,639s), 3. Piastri (da P17). Piloti: Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264.",
        "f1_pulse": "FORMULA 1: VERSTAPPEN VINCE A VEGAS TRA 35 SORPASSI IN TESTA E MCLAREN A 9 PT DALLA RED BULL",
        "soccer_tagline": "Champions League 5a g.: Real Madrid 5-1 al PSV; Sabah 0-1 Barcellona all'intervallo.",
        "soccer_liveNow": "UCL mar: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoli. Mer int: Sabah 0-1 Barcellona. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "soccer_pulse": "CHAMPIONS LEAGUE: REAL MADRID SOLO A QUOTA 15; LIVERPOOL 4-0 ALLO UNITED DI POCHETTINO",
        "basketball_tagline": "Prima della sosta del Ringraziamento NBA: Dallas espugna Denver 120-101; Boston 131-116 a Washington.",
        "basketball_liveNow": "NBA Cup mar: Mavericks 120-101 Nuggets (Flagg 24/6/12); Celtics 131-116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104-86 Magic (Joe 21). Gio riposo.",
        "basketball_pulse": "EMIRATES NBA CUP: COOPER FLAGG E JAYSON TATUM (41 PT) BRILLANO PRIMA DELLA SOSTA DI GIOVEDI",
        "golf_tagline": "Marco Penge vince lo spareggio a quattro a Sea Island per il primo titolo PGA Tour al RSM Classic.",
        "golf_liveNow": "RSM Classic (23 nov): Marco Penge (-16, 266) supera alla 1a buca extra Haotong Li, Michael Thorbjornsen e Max Greyserman. Prossima: Hero World Challenge (3-6 dic).",
        "golf_pulse": "PGA TOUR: MARCO PENGE TRIONFA AL PLAYOFF A SEA ISLAND E CONQUISTA IL PRIMO TROFEO",
        "home_tonight": "Desk del giovedi",
        "home_tonightBlurb": "Thanksgiving NFL: Bears (8-2) a Detroit e Chiefs a Buffalo (9-1) dopo Packers-Rams. UCL 5a g.: Real Madrid 5-1 PSV, Sabah 0-1 Barcellona all'intervallo. Coppa Davis live: Italia 1-0 Corea.",
        "home_plTitle": "Arsenal guida la Premier a quota 28; Real Madrid capolista solitario in Champions",
        "home_plBlurb": "PL 11a g.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21 (Liverpool 4-0 Man Utd all'esordio di Pochettino, City 1-1 Fulham, Newcastle 2-2 Arsenal). UCL: Real 5-1 PSV, Arsenal 1-1 Dortmund.",
        "home_f1Title": "Verso il Qatar: Verstappen sbarca a Lusail dopo il 75esimo sigillo con 3 punti per il podio",
        "home_f1Blurb": "Antonelli (402) e Mercedes (666) gia campioni, Verstappen sale a 304 dopo Las Vegas. Appena 3 punti separano Hamilton (267) da Russell e Norris (264).",
    },
    "pl": {
        "common_todayDesk": "Czwartkowy desk: Thanksgiving NFL (Bears 8-2 u Lions 8-2, Chiefs 8-2 u Bills 9-1) po Packers-Rams. LM 5. kol. (Real 5:1 PSV, Sabah 0:1 Barcelona HT). Puchar Davisa w Bolonii.",
        "common_todayNfl": "Thanksgiving Day: Bears (8-2) u Lions (8-2) 19:00, Eagles u Cowboys 22:30, Chiefs (8-2) u Bills (9-1) 02:20.",
        "common_todayTnf": "Sroda na Netflixie: Packers (6-4) u Rams (6-4) przed hitem Lions-Bears na Ford Field.",
        "football_tagline": "Thanksgiving NFL: Lions i Bears (8-2) otwieraja czwartek po Packers-Rams na Netflixie.",
        "football_liveNow": "Sroda Netflix: Packers (6-4) u Rams (6-4). Czwartek: Bears-Lions 19:00, Eagles-Cowboys 22:30, Chiefs-Bills (9-1) 02:20.",
        "football_pulse": "NFL THANKSGIVING: LIONS I BEARS (8-2) O PRYM W NFC NORTH; CHIEFS U BILLS W NOCNYM HICIE",
        "tennis_tagline": "Puchar Davisa w Bolonii: Wlochy prowadza 1:0 z Korea Pld; Alcaraz mistrzem w Turynie.",
        "tennis_liveNow": "Bolonia: Czechy 2:0 Kanada; Wlochy 1:0 Korea Pld (Musetti 6:0, 7:6 Hong, Cobolli-Kwon). Czw: GB-Niemcy. Turyn: Alcaraz 6:2, 7:6(7) Zverev.",
        "tennis_pulse": "PUCHAR DAVISA: WLOSI PROWADZA W BOLONII PO TRIUMFIE BEZ PORAZKI ALCARAZA W TURYNIE",
        "f1_tagline": "Przed GP Kataru (27-29 list.): Verstappen przenosi triumf z Vegas do Lusail w klasycznym formacie.",
        "f1_liveNow": "Las Vegas GP: 1. Verstappen (75. wygrana), 2. Norris (+0,639s), 3. Piastri (z P17). Kierowcy: Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264.",
        "f1_pulse": "FORMULA 1: VERSTAPPEN WYGRYWA W VEGAS PO 35 ZMIANACH LIDERA; MCLAREN 9 PKT ZA RED BULLEM",
        "soccer_tagline": "Liga Mistrzow 5. kol.: Real Madryt rozbil PSV 5:1; Sabah 0:1 Barcelona do przerwy.",
        "soccer_liveNow": "LM wt: Real Madryt 5:1 PSV, Arsenal 1:1 Dortmund, Man City 2:2 Napoli. Sr HT: Sabah 0:1 Barcelona. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
        "soccer_pulse": "LIGA MISTRZOW: REAL MADRYT Z KOMPLETEM 15 PKT; LIVERPOOL ROZBIL MAN UTD POCHETTINO 4:0",
        "basketball_tagline": "Przed czwartkowa pauza w NBA: Dallas ogralo Denver 120:101, a Boston rzucil 131 punktow Wizards.",
        "basketball_liveNow": "NBA Cup wt: Mavericks 120:101 Nuggets (Flagg 24/6/12); Celtics 131:116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104:86 Magic (Joe 21). Czw wolne.",
        "basketball_pulse": "EMIRATES NBA CUP: COOPER FLAGG I JAYSON TATUM (41 PKT) BLYSZCZA PRZED SWIATECZNA PAUZA",
        "golf_tagline": "Marco Penge wygrywa czteroosobowa dogrywke na Sea Island i zdobywa pierwszy tytul PGA Tour.",
        "golf_liveNow": "The RSM Classic (23 list.): Marco Penge (-16, 266) lepszy na 1. dodatkowym dolku od Haotonga Li, Thorbjornsena i Greysermana. Dalej: Hero World Challenge (3-6 grud.).",
        "golf_pulse": "PGA TOUR: MARCO PENGE ZWYCIEZA W DOGRYWCE NA SEA ISLAND I ZDOBYWA PREMIEROWY PUCHAR",
        "home_tonight": "Czwartkowy desk",
        "home_tonightBlurb": "Thanksgiving NFL: Bears (8-2) u Lions (8-2) oraz Chiefs u Bills (9-1) po meczu Packers-Rams. LM 5. kol.: Real Madryt 5:1 PSV, Sabah 0:1 Barcelona do przerwy. Puchar Davisa: Wlochy 1:0 Korea Pld.",
        "home_plTitle": "Arsenal liderem Premier League z 28 pkt; Real Madryt samotnie na czele Ligi Mistrzow",
        "home_plBlurb": "PL po 11. kol.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21 (Liverpool 4:0 Man Utd w debiucie Pochettino, Man City 1:1 Fulham, Newcastle 2:2 Arsenal). LM: Real 5:1 PSV, Arsenal 1:1 Dortmund.",
        "home_f1Title": "Zapowiedz GP Kataru: Verstappen z 75. wygrana w drodze do Lusail, trzy punkty na podium",
        "home_f1Blurb": "Mistrzowie Antonelli (402) i Mercedes (666) sa juz pewni, Verstappen ma 304 pkt po Las Vegas. Zaledwie 3 punkty dziela Hamiltona (267) od Russella i Norrisa (264).",
    },
    "zh": {
        "common_todayDesk": "周四体育台：NFL感恩节大战（熊8-2战雄狮8-2，酋长8-2战比尔9-1）紧接周三网飞包装工对公羊。欧冠第5轮皇马5-1大胜，萨巴赫0-1巴萨半场。戴维斯杯博洛尼亚。",
        "common_todayNfl": "感恩节赛程：熊（8-2）战雄狮（8-2）13:00 CBS，老鹰战牛仔16:30 FOX，酋长（8-2）战比尔（9-1）20:20 NBC。",
        "common_todayTnf": "周三网飞先战：包装工（6-4）客战公羊（6-4），周四熊狮福特球场定国北榜首。",
        "football_tagline": "NFL感恩节：周三网飞大战后，同积8胜2负的雄狮与熊队周四揭幕。",
        "football_liveNow": "周三网飞：包装工（6-4）战公羊（6-4）。周四：熊战雄狮13:00，老鹰战牛仔16:30，酋长（8-2）战比尔（9-1）20:20。",
        "football_pulse": "NFL感恩节：8胜2负雄狮与熊队直面国北榜首之争；酋长压轴客战9胜1负比尔",
        "tennis_tagline": "戴维斯杯博洛尼亚总决赛：卫冕冠军意大利1-0领先韩国；阿尔卡拉斯都灵封王。",
        "tennis_liveNow": "博洛尼亚：捷克2-0加拿大；意大利1-0韩国（穆塞蒂6-0、7-6胜洪性成，科博利战权纯雨）。周四英德大战。都灵：阿尔卡拉斯胜兹维列夫。",
        "tennis_pulse": "戴维斯杯：意大利在博洛尼亚占得先机，阿尔卡拉斯刚全胜夺得都灵年终首冠",
        "f1_tagline": "卡塔尔大奖赛（11月27-29日）：维斯塔潘挟拉斯维加斯第75胜抵达卢赛尔常规周末。",
        "f1_liveNow": "拉斯维加斯站：1.维斯塔潘（75胜），2.诺里斯（+0.639秒），3.皮亚斯特里（第17起步）。积分：安东内利402，维斯塔潘304，汉密尔顿267，拉塞尔264，诺里斯264。",
        "f1_pulse": "F1：维斯塔潘鏖战35次领跑交替称霸维加斯，迈凯伦距红牛仅剩9分",
        "soccer_tagline": "欧冠第5轮：皇马5-1横扫埃因霍温；周三半场萨巴赫0-1巴塞罗那。",
        "soccer_liveNow": "欧冠周二：皇马5-1埃因霍温，阿森纳1-1多特，曼城2-2那不勒斯。周三半场：萨巴赫0-1巴萨。英超：阿森纳28，布莱顿22，曼城22，利物浦21。",
        "soccer_pulse": "欧冠第5轮：皇马15分独居榜首；利物浦4-0大胜波切蒂诺曼联首秀",
        "basketball_tagline": "NBA感恩节休战前夕：独行侠120-101胜掘金，凯尔特人131-116力克奇才。",
        "basketball_liveNow": "周二NBA杯：独行侠120-101掘金（弗拉格24/6/12）；绿军131-116奇才（塔图姆41，乔治28；戴维斯33/13）；活塞104-86魔术（乔21）。周四休战。",
        "basketball_pulse": "NBA杯：库珀·弗拉格24+12与塔图姆狂轰41分点燃感恩节前夜",
        "golf_tagline": "马尔科·彭奇在海岛四人加洞赛夺得RSM精英赛冠军，收获美巡首冠。",
        "golf_liveNow": "RSM精英赛（11月23日）：彭奇（-16，266杆）加洞首洞胜李昊桐、索比约恩森与格雷泽曼。下站：英雄世界挑战赛（12月3-6日）。",
        "golf_pulse": "美巡赛：马尔科·彭奇海岛加洞封王锁定生涯首冠与完整美巡会员资格",
        "home_tonight": "周四体育台",
        "home_tonightBlurb": "NFL感恩节：周三包装工对公羊后，周四熊（8-2）战雄狮（8-2）及酋长战比尔（9-1）连场好戏。欧冠皇马5-1埃因霍温，巴萨半场领先。戴维斯杯意大利1-0领先韩国。",
        "home_plTitle": "阿森纳28分领跑英超；皇家马德里五战全胜15分独居欧冠榜首",
        "home_plBlurb": "英超第11轮后：阿森纳28，布莱顿22，曼城22，利物浦21（利物浦4-0曼联，曼城1-1富勒姆，纽卡2-2阿森纳）。欧冠皇马5-1埃因霍温，阿森纳1-1多特。",
        "home_f1Title": "卡塔尔站前瞻：维斯塔潘75胜挺进卢赛尔，车手季军之争仅差3分",
        "home_f1Blurb": "安东内利（402分）与梅赛德斯（666分）已锁双冠，维斯塔潘维加斯夺冠升至304分；汉密尔顿（267分）仅领先拉塞尔与诺里斯（264分）3分。",
    },
    "ja": {
        "common_todayDesk": "木曜デスク：感謝祭NFL（ベアーズ8-2対ライオンズ8-2、チーフス8-2対ビルズ9-1）。欧州CL第5節（Rマドリード5-1 PSV、サバフ0-1バルサHT）。デビス杯ボローニャ。",
        "common_todayNfl": "感謝祭：ベアーズ(8-2)対ライオンズ(8-2) 13:00 CBS、イーグルス対カウボーイズ 16:30 FOX、チーフス(8-2)対ビルズ(9-1) 20:20 NBC。",
        "common_todayTnf": "水曜Netflix：パッカーズ(6-4)対ラムズ(6-4)に続き木曜はフォード・フィールド決戦。",
        "football_tagline": "感謝祭NFL：水曜パッカーズ対ラムズの後、8勝2敗のライオンズとベアーズが木曜開幕。",
        "football_liveNow": "水曜Netflix：パッカーズ(6-4)対ラムズ(6-4)。木曜：ベアーズ対ライオンズ13:00、イーグルス対カウボーイズ16:30、チーフス対ビルズ(9-1)20:20。",
        "football_pulse": "NFL感謝祭：8勝2敗ライオンズとベアーズがNFC北首位懸け激突；チーフス対ビルズ",
        "tennis_tagline": "デビス杯ボローニャ：イタリアが韓国に1-0リード；アルカラスがトリノ無敗V。",
        "tennis_liveNow": "デビス杯：チェコ2-0カナダ；イタリア1-0韓国（ムゼッティ6-0, 7-6ホン、コボッリ戦）。木曜：英国対ドイツ。トリノ：アルカラス6-2, 7-6(7)ズベレフ。",
        "tennis_pulse": "デビス杯：ボローニャでイタリア先行、アルカラスはトリノ5戦全勝で戴冠",
        "f1_tagline": "次戦カタールGP（11/27-29）：ベガス制覇のフェルスタッペンがルサイル通常開催へ。",
        "f1_liveNow": "ラスベガスGP結果：1.フェルスタッペン（通算75勝）、2.ノリス(+0.639s)、3.ピアストリ(17番手から)。ランキング：アントネッリ402、フェルスタッペン304、ハミルトン267、ラッセル/ノリス264。",
        "f1_pulse": "F1：35度の首位交代を制したフェルスタッペンがベガス優勝、マクラーレンはレッドブルに9点差",
        "soccer_tagline": "欧州CL第5節：レアル・マドリード5-1 PSV；サバフ0-1バルセロナ前半終了。",
        "soccer_liveNow": "CL火曜：Rマドリード5-1 PSV、アーセナル1-1ドルトムント、マンC 2-2ナポリ。水曜HT：サバフ0-1バルサ。PL：アーセナル28、ブライトン22、シティ22、リヴァプール21。",
        "soccer_pulse": "欧州CL：レアル・マドリードが勝ち点15単独首位；リヴァプールはポチェッティーノ初陣のマンUを4-0粉砕",
        "basketball_tagline": "NBA感謝祭前：マーベリックスがナゲッツを120-101撃破；セルティックス131得点。",
        "basketball_liveNow": "火曜NBA杯：マブス120-101ナゲッツ（フラッグ24/6/12）；セルティックス131-116ウィザーズ（テイタム41、ジョージ28；デイビス33/13）；ピストンズ104-86マジック（ジョー21）。木曜全休。",
        "basketball_pulse": "NBAカップ：フラッグ24点12アシストとテイタム41点爆発後に感謝祭ブレイク突入",
        "golf_tagline": "マルコ・ペンジがシーアイランドの4人POを制しRSMクラシックでPGAツアー初優勝。",
        "golf_liveNow": "RSMクラシック（11/23）：ペンジ(-16, 266)が1ホール目で李昊桐、ソービョルンセンらを下す。次戦：ヒーローワールドチャレンジ（12/3-6）。",
        "golf_pulse": "PGAツアー：マルコ・ペンジがシーアイランド4人POを制し初の栄冠獲得",
        "home_tonight": "木曜デスク",
        "home_tonightBlurb": "感謝祭NFL：パッカーズ対ラムズに続きベアーズ(8-2)対ライオンズ(8-2)とチーフス対ビルズ(9-1)が開幕。CL：Rマドリード5-1 PSV、バルサ前半リード。デビス杯：イタリア1-0韓国。",
        "home_plTitle": "アーセナルが勝ち点28でプレミア首位、レアル・マドリードが勝ち点15でCL単独首位",
        "home_plBlurb": "プレミア第11節：アーセナル28、ブライトン22、マンC 22、リヴァプール21（リヴァプール4-0マンU、シティ1-1フラム、ニューカッスル2-2アーセナル）。CL：レアル5-1 PSV、アーセナル1-1ドルトムント。",
        "home_f1Title": "カタールGP展望：通算75勝のフェルスタッペンがルサイルへ、3位争いは僅か3点差",
        "home_f1Blurb": "王者アントネッリ（402点）とメルセデス（666点）が決する中、フェルスタッペンは304点へ上昇。ハミルトン（267点）をラッセルとノリス（264点）が3点差で追う。",
    },
    "ko": {
        "common_todayDesk": "목요 데스크: NFL 추수감사절(베어스 8-2 vs 라이온스 8-2, 치프스 8-2 vs 빌스 9-1). UCL 5차전(레알 5-1 PSV, 사바흐 0-1 바르사 전반). 데이비스컵 볼로냐.",
        "common_todayNfl": "추수감사절: 베어스(8-2) vs 라이온스(8-2) 13:00 CBS, 이글스 vs 카우보이스 16:30 FOX, 치프스(8-2) vs 빌스(9-1) 20:20 NBC.",
        "common_todayTnf": "수요일 넷플릭스: 패커스(6-4) vs 램스(6-4) 이후 목요일 포드 필드 빅매치 개막.",
        "football_tagline": "추수감사절 NFL: 수요일 패커스-램스 뒤를 이어 8승 2패 동률 라이온스-베어스 목요일 첫 경기.",
        "football_liveNow": "수 Netflix: 패커스(6-4) vs 램스(6-4). 목: 베어스 vs 라이온스 13:00, 이글스-카우보이스 16:30, 치프스(8-2) vs 빌스(9-1) 20:20.",
        "football_pulse": "NFL 추수감사절: 8승 2패 라이온스-베어스 NFC 북부 1위 혈투; 치프스 vs 빌스 야간 빅매치",
        "tennis_tagline": "데이비스컵 볼로냐: 디펜딩 챔피언 이탈리아 한국에 1-0 리드; 알카라스 토리노 무패 우승.",
        "tennis_liveNow": "볼로냐: 체코 2-0 캐나다; 이탈리아 1-0 한국(무세티 6-0, 7-6 홍성찬, 코볼리-권순우). 목: 영국-독일. 토리노: 알카라스 6-2, 7-6(7) 즈베레프.",
        "tennis_pulse": "데이비스컵: 볼로냐 8강 이탈리아 기선제압, 알카라스 토리노 5전 전승 첫 정상",
        "f1_tagline": "카타르 GP(11/27-29): 베가스 통산 75승 거둔 페르스타펜, 루사일 전통 주말 일정 돌입.",
        "f1_liveNow": "베가스 결과: 1.페르스타펜(75승), 2.노리스(+0.639초), 3.피아스트리(17번 출발). 순위: 안토넬리 402, 페르스타펜 304, 해밀턴 267, 러셀/노리스 264.",
        "f1_pulse": "포뮬러 1: 35차례 선두 교체 혈투 끝 페르스타펜 우승; 맥라렌 레드불 9점 차 맹추격",
        "soccer_tagline": "UCL 5차전: 레알 마드리드 5-1 PSV 완파; 사바흐 0-1 바르셀로나 전반 종료.",
        "soccer_liveNow": "UCL 화: 레알 5-1 PSV, 아스널 1-1 도르트문트, 맨시티 2-2 나폴리. 수 전반: 사바흐 0-1 바르사. PL: 아스널 28, 브라이튼 22, 시티 22, 리버풀 21.",
        "soccer_pulse": "챔피언스리그: 레알 마드리드 승점 15점 단독 선두; 리버풀, 포체티노 맨유 데뷔전 4-0 대파",
        "basketball_tagline": "NBA 추수감사절 휴식 전: 댈러스, 덴버 120-101 완파; 보스턴 131-116 위저즈 제압.",
        "basketball_liveNow": "화 컵대회: 매버릭스 120-101 너기츠(플래그 24/6/12); 셀틱스 131-116 위저즈(테이텀 41, 조지 28; 데이비스 33/13); 피스톤스 104-86 매직(조 21). 목 휴식.",
        "basketball_pulse": "에미레이츠 NBA 컵: 쿠퍼 플래그 24+12, 제이슨 테이텀 41점 맹활약 후 목요일 전체 휴식",
        "golf_tagline": "마르코 펜지, RSM 클래식 4인 연장 승부 끝 생애 첫 PGA 투어 우승 트로피 차지.",
        "golf_liveNow": "RSM 클래식(11/23): 펜지(-16, 266)가 1차 연장서 리하오퉁, 소르비욘센, 그레이저먼 제압. 다음 대회: 히어로 월드 챌린지(12/3-6).",
        "golf_pulse": "PGA 투어: 마르코 펜지, 시아일랜드 연장 첫 홀 버디로 생애 첫 투어 우승 달성",
        "home_tonight": "목요 데스크",
        "home_tonightBlurb": "추수감사절 NFL: 패커스-램스 뒤 베어스(8-2) vs 라이온스(8-2)와 치프스-빌스(9-1) 출격. UCL: 레알 5-1 PSV, 바르사 전반 리드. 데이비스컵: 이탈리아 1-0 한국.",
        "home_plTitle": "아스널 승점 28점 프리미어리그 선두; 레알 마드리드 15점으로 UCL 단독 1위",
        "home_plBlurb": "PL 11R: 아스널 28, 브라이튼 22, 맨시티 22, 리버풀 21 (리버풀 4-0 맨유 포체티노 데뷔전, 맨시티 1-1 풀럼, 뉴캐슬 2-2 아스널). UCL: 레알 5-1 PSV, 아스널 1-1 도르트문트.",
        "home_f1Title": "카타르 GP 프리뷰: 통산 75승 페르스타펜 루사일 입성, 3위 경쟁은 단 3점 차",
        "home_f1Blurb": "안토넬리(402)와 메르세데스(666)가 양대 챔피언을 확정한 가운데 페르스타펜은 베가스 우승으로 304점에 도달했고 해밀턴(267)과 러셀, 노리스(264)는 3점 차다.",
    },
    "ar": {
        "common_todayDesk": "مكتب الخميس: عيد الشكر NFL (بيرز 8-2 ضد لايونز 8-2، تشيفز 8-2 ضد بيلز 9-1) بعد باكرز ورامز. دوري الابطال (ريال مدريد 5-1، برشلونة متقدم). كاس ديفيز بولونيا.",
        "common_todayNfl": "عيد الشكر: بيرز (8-2) ضد لايونز (8-2) 1:00 ظهرا CBS، ايغلز ضد كاوبويز 4:30 FOX، تشيفز (8-2) ضد بيلز (9-1) 8:20 NBC.",
        "common_todayTnf": "ليلة الاربعاء على نتفليكس: باكرز (6-4) ضد رامز (6-4) قبل قمة فورد فيلد.",
        "football_tagline": "عيد الشكر NFL: لايونز وبيرز (8-2) يفتتحان الخميس بعد مواجهة باكرز ورامز على نتفليكس.",
        "football_liveNow": "الاربعاء نتفليكس: باكرز (6-4) ضد رامز (6-4). الخميس: بيرز-لايونز 1:00، ايغلز-كاوبويز 4:30، تشيفز-بيلز (9-1) 8:20.",
        "football_pulse": "عيد الشكر NFL: صراع 8-2 بين لايونز وبيرز على القمة وتشيفز يحل ضيفا على بيلز",
        "tennis_tagline": "كاس ديفيز بولونيا: ايطاليا حاملة اللقب تتقدم 1-0 على كوريا الجنوبية؛ الكاراز بطل تورينو.",
        "tennis_liveNow": "بولونيا: التشيك 2-0 كندا؛ ايطاليا 1-0 كوريا (موسيتي 6-0 و7-6 هونغ، كوبولي-كوون). الخميس: بريطانيا-المانيا. تورينو: الكاراز 6-2، 7-6(7) زفيريف.",
        "tennis_pulse": "كاس ديفيز: ايطاليا تتقدم في بولونيا بعد تتويج الكاراز التاريخي دون هزيمة في تورينو",
        "f1_tagline": "جائزة قطر الكبرى (27-29 نوفمبر): فيرستابن يحمل انتصاره الـ75 نحو لوسيل بالصيغة التقليدية.",
        "f1_liveNow": "لاس فيغاس: 1.فيرستابن (فوزه 75)، 2.نوريس (+0.639ث)، 3.بياستري (من المركز 17). السائقون: انتونيللي 402، فيرستابن 304، هاميلتون 267، راسل ونوريس 264.",
        "f1_pulse": "فورمولا 1: فيرستابن يحسم فيغاس بعد 35 تبديلا للصدارة ومكلارين يلاحق ريد بول بفارق 9 نقاط",
        "soccer_tagline": "دوري الابطال الجولة 5: ريال مدريد يسحق ايندهوفن 5-1؛ صباح 0-1 برشلونة بين الشوطين.",
        "soccer_liveNow": "الثلاثاء: ريال مدريد 5-1 ايندهوفن، ارسنال 1-1 دورتموند، مانشستر سيتي 2-2 نابولي. الاربعاء: برشلونة متقدم 1-0. الانجليزي: ارسنال 28، برايتون 22، سيتي 22، ليفربول 21.",
        "soccer_pulse": "دوري الابطال: ريال مدريد ينفرد بـ15 نقطة وليفربول يكتسح يونايتد بوتشيتينو برباعية",
        "basketball_tagline": "قبل عطلة عيد الشكر في NBA: دالاس يهزم دنفر 120-101 وبوسطن يتفوق على واشنطن 131-116.",
        "basketball_liveNow": "كاس الدوري الثلاثاء: مافريكس 120-101 ناغتس (فلاغ 24/6/12)؛ سلتيكس 131-116 ويزاردز (تايتوم 41، جورج 28؛ ديفيس 33/13)؛ بيستونز 104-86 ماجيك (جو 21). الخميس راحة.",
        "basketball_pulse": "كاس الامارات NBA: كوبر فلاغ وتايتوم (41 نقطة) يتالقان قبل استراحة الخميس",
        "golf_tagline": "ماركو بينجي يتوج بلقبه الاول في جولة PGA بعد تمايز رباعي في بطولة RSM كلاسيك.",
        "golf_liveNow": "بطولة RSM (23 نوفمبر): ماركو بينجي (-16، 266) يتفوق من الحفرة الاضافية الاولى على لي هاوتونغ وثوربيورنسن وغريزرمان. القادم: تحدي هيرو العالمي (3-6 ديسمبر).",
        "golf_pulse": "جولة PGA: بينجي يحسم التمايز الرباعي في سي آيلاند ويحقق اول لقب له في الجولة",
        "home_tonight": "مكتب الخميس",
        "home_tonightBlurb": "عيد الشكر NFL: بيرز (8-2) ضد لايونز (8-2) وتشيفز ضد بيلز (9-1) بعد باكرز ورامز. دوري الابطال: ريال مدريد 5-1 ايندهوفن وبرشلونة متقدم. كاس ديفيز: ايطاليا 1-0 كوريا.",
        "home_plTitle": "ارسنال يتصدر الدوري الانجليزي بـ28 نقطة؛ ريال مدريد منفرد بقمة دوري الابطال",
        "home_plBlurb": "الجولة 11: ارسنال 28، برايتون 22، مانشستر سيتي 22، ليفربول 21 (ليفربول 4-0 مان يونايتد في ظهور بوتشيتينو، سيتي 1-1 فولهام، نيوكاسل 2-2 ارسنال). دوري الابطال: ريال 5-1 ايندهوفن.",
        "home_f1Title": "تقديم جائزة قطر: فيرستابن يصل لوسيل بفوزه الـ75 وسط صراع ثلاثي النقاط على الثالث",
        "home_f1Blurb": "انتونيللي (402) ومرسيدس (666) ضمنا اللقبين، فيما رفع فيرستابن رصيده الى 304 نقاط بعد لاس فيغاس ويفصل 3 نقاط فقط هاميلتون (267) عن راسل ونوريس (264).",
    }
}

def replace_in_block(block_text, updates_dict):
    def esc(val):
        return val.replace('\\', '\\\\').replace('"', '\\"')
    
    # Replace common/home fields cleanly
    flat_map = {
        "common_todayDesk": "todayDesk",
        "common_todayNfl": "todayNfl",
        "common_todayTnf": "todayTnf",
        "home_tonight": "tonight",
        "home_tonightBlurb": "tonightBlurb",
        "home_plTitle": "plTitle",
        "home_plBlurb": "plBlurb",
        "home_f1Title": "f1Title",
        "home_f1Blurb": "f1Blurb",
    }
    for flat_k, ts_k in flat_map.items():
        val = esc(updates_dict[flat_k])
        # Matches both single-quoted multi-line/single-line and double-quoted!
        pattern = rf'({ts_k}:\s*)(?:"[^"\n]*"|\'[^\'\n]*\'|\n\s*(?:"[^"\n]*"|\'[^\'\n]*\'))'
        m = re.search(pattern, block_text)
        if not m:
            raise RuntimeError(f"Failed to match key {ts_k} in locale block")
        block_text = block_text[:m.start()] + f'{m.group(1)}"{val}"' + block_text[m.end():]
        
    for sport in ["football", "tennis", "f1", "soccer", "basketball", "golf"]:
        for prop in ["tagline", "liveNow", "pulse"]:
            val = esc(updates_dict[f"{sport}_{prop}"])
            sp_pat = rf'({sport}:\s*\{{.*?{prop}:\s*)(?:"[^"\n]*"|\'[^\'\n]*\')'
            m = re.search(sp_pat, block_text, flags=re.DOTALL)
            if not m:
                raise RuntimeError(f"Failed to match {sport}.{prop} in locale block")
            block_text = block_text[:m.start()] + f'{m.group(1)}"{val}"' + block_text[m.end():]
    return block_text

# Update messages.ts (contains BOTH export const en = ... AND export const fr: Messages = ...)
msg_ts_path = os.path.join(I18N, "messages.ts")
msg_ts = open(msg_ts_path, "r", encoding="utf-8").read()
split_marker = "export const fr: Messages = {"
en_part, fr_part = msg_ts.split(split_marker, 1)

en_part = replace_in_block(en_part, messages_updates["en"])
fr_part = replace_in_block(fr_part, messages_updates["fr"])
new_msg_ts = en_part + split_marker + fr_part
if "\u2014" in new_msg_ts or "--" in new_msg_ts:
    raise ValueError("Em-dash or double-hyphen in messages.ts!")
open(msg_ts_path, "w", encoding="utf-8").write(new_msg_ts)
print("Cleanly updated messages.ts (both en and fr).")

# Update messages-*.ts for es, de, it, pl, zh, ja, ko, ar
for loc in ["es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
    p = os.path.join(I18N, f"messages-{loc}.ts")
    txt = open(p, "r", encoding="utf-8").read()
    new_txt = replace_in_block(txt, messages_updates[loc])
    if "\u2014" in new_txt or "--" in new_txt:
        raise ValueError(f"Em-dash or double-hyphen in messages-{loc}.ts!")
    open(p, "w", encoding="utf-8").write(new_txt)
    print(f"Cleanly updated messages-{loc}.ts.")
