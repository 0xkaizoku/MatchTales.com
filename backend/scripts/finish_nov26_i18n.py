# Conservative 26 Nov 2026 i18n + leftover match claims. No LIVE, no unpublished FT, no 75th/35, no Sabah HT.
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
I18N = os.path.join(ROOT, "frontend", "src", "i18n")
MATCHES = os.path.join(ROOT, "frontend", "src", "content", "matches")


def no_dashes(blob, label):
    if "\u2014" in blob:
        raise SystemExit(f"emdash in {label}")
    if "--" in blob:
        raise SystemExit(f"double hyphen in {label}")


def loadm(name):
    return json.load(open(os.path.join(MATCHES, name), encoding="utf-8"))


def savem(name, data):
    raw = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    no_dashes(raw, name)
    open(os.path.join(MATCHES, name), "w", encoding="utf-8").write(raw)
    print("match", name)


# leftover match claims
qatar = loadm("qatar-gp-lusail-preview-2026.json")
qatar["keyPlayers"][0]["hook"] = "Carries Las Vegas win (1:27:39.624) into a standard Lusail weekend with no sprint."
savem("qatar-gp-lusail-preview-2026.json", qatar)

bears = loadm("bears-at-lions-thanksgiving-week12-2026.json")
bears["teaser"] = "First place in the NFC North belongs to the winner as unbeaten-at-home Lions host Ben Johnson five-game-winning Bears on CBS (1:00 PM ET)."
bears["story"] = bears["story"].replace("a spotless 6-0 home mark into", "an unbeaten home mark into")
bears["funFacts"][1] = "Detroit enters Thanksgiving on a six-game win streak and unbeaten inside Ford Field in 2026."
savem("bears-at-lions-thanksgiving-week12-2026.json", bears)

# ---------------------------------------------------------
# PLAYGROUND
# ---------------------------------------------------------
pg_path = os.path.join(I18N, "playground.ts")
pg_txt = open(pg_path, "r", encoding="utf-8").read()
pg_updates = {
    "en": {
        "pinFinal": "Davis Cup Bologna: Czechia d Canada 2-0; Italy vs Korea still open after Musetti d Hong 6-0, 7-6(5). Turin: Alcaraz d Zverev 6-2, 7-6(7) unbeaten.",
        "week1Closed": "Thanksgiving Football: Bears (8-2) at Lions (8-2) 1:00 PM ET, Eagles at Cowboys 4:30 PM ET, Chiefs at Bills (9-1) 8:20 PM ET.",
        "week1Sub": "8-2 Lions host 8-2 Bears. Wed Netflix Packers-Rams unpublished. Week 11 Final: Texans 26-3 Colts (HOU 4-6, IND 3-8).",
        "countdownTnf": "THANKSGIVING DAY: Bears at Lions (1:00 PM ET CBS). Eagles at Cowboys (4:30 PM ET FOX). Chiefs at Bills (8:20 PM ET NBC).",
        "gridAfterMadrid": "Round 22 · Qatar GP at Lusail (27-29 Nov, standard format, no sprint)",
        "barsPoints": "Antonelli (402) and Mercedes (666) Champions; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (MW11): Arsenal 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Select a club. Arsenal lead on 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "UCL MD5 Tue: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoli. Wed unpublished. PL: Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic Final: Marco Penge wins 4-way playoff on 1st extra hole at -16 (266) over Haotong Li and Thorbjornsen.",
    },
    "fr": {
        "pinFinal": "Coupe Davis Bologne : Tchequie 2-0 Canada ; Italie-Coree encore ouverte apres Musetti 6-0, 7-6(5) Hong. Turin : Alcaraz bat Zverev 6-2, 7-6(7).",
        "week1Closed": "Thanksgiving NFL : Bears (8-2) chez les Lions (8-2) 13h00 ET, Eagles-Cowboys 16h30, Chiefs-Bills (9-1) 20h20 ET.",
        "week1Sub": "Lions et Bears (8-2) a Ford Field. Packers-Rams mercredi inedit. S11 : Texans 26-3 Colts (4-6 vs 3-8).",
        "countdownTnf": "THANKSGIVING NFL : Bears chez les Lions (13h00 ET CBS). Eagles chez les Cowboys (16h30 ET FOX). Chiefs chez les Bills (20h20 ET NBC).",
        "gridAfterMadrid": "Manche 22 · GP du Qatar a Lusail (27-29 nov, format classique, pas de sprint)",
        "barsPoints": "Antonelli (402) et Mercedes (666) Champions ; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (J11) : Arsenal 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Selectionnez un club. Arsenal 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "LDC J5 mardi : Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Naples. Mercredi inedit. PL : Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic : Marco Penge s'impose en playoff a quatre a -16 (266) devant Haotong Li et Thorbjornsen.",
    },
    "es": {
        "pinFinal": "Copa Davis Bolonia: Chequia 2-0 Canada; Italia-Corea sigue abierta tras Musetti 6-0, 7-6(5) Hong. Turin: Alcaraz 6-2, 7-6(7) Zverev.",
        "week1Closed": "Accion de Gracias NFL: Bears (8-2) en Lions (8-2) 1:00 PM ET, Eagles en Cowboys 4:30 PM, Chiefs en Bills (9-1) 8:20 PM ET.",
        "week1Sub": "Lions y Bears (8-2) en Ford Field. Packers-Rams del miercoles sin publicar. Semana 11: Texans 26-3 Colts (4-6 vs 3-8).",
        "countdownTnf": "DIA DE ACCION DE GRACIAS: Bears en Lions (1:00 PM ET CBS). Eagles en Cowboys (4:30 PM FOX). Chiefs en Bills (8:20 PM NBC).",
        "gridAfterMadrid": "Ronda 22 · GP de Catar en Lusail (27-29 nov, formato clasico, sin sprint)",
        "barsPoints": "Antonelli (402) y Mercedes (666) Campeones; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (J11): Arsenal 28 pts, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Selecciona un club. Arsenal 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "UCL J5 martes: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoles. Miercoles inedito. PL: Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic: Marco Penge gana el playoff cuadruple en -16 (266) ante Haotong Li y Thorbjornsen.",
    },
    "de": {
        "pinFinal": "Davis Cup Bologna: Tschechien 2:0 Kanada; Italien gegen Korea noch offen nach Musetti 6:0, 7:6(5) Hong. Turin: Alcaraz 6:2, 7:6(7) Zverev.",
        "week1Closed": "Thanksgiving Football: Bears (8-2) bei Lions (8-2) 1:00 PM ET, Eagles bei Cowboys 4:30 PM, Chiefs bei Bills (9-1) 8:20 PM ET.",
        "week1Sub": "Lions und Bears (beide 8-2) im Ford Field. Packers-Rams Mittwoch unveröffentlicht. Woche 11: Texans 26:3 Colts (4-6, IND 3-8).",
        "countdownTnf": "THANKSGIVING DAY: Bears bei Lions (1:00 PM ET CBS). Eagles bei Cowboys (4:30 PM FOX). Chiefs bei Bills (8:20 PM NBC).",
        "gridAfterMadrid": "Runde 22 · Katar GP in Lusail (27.-29. Nov., Standard-Format, kein Sprint)",
        "barsPoints": "Antonelli (402) und Mercedes (666) Weltmeister; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (11. Sp.): Arsenal 28 Pkt., Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Klub waehlen. Arsenal fuehrt mit 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "UCL 5. Sp. Di: Real Madrid 5:1 PSV, Arsenal 1:1 Dortmund, Man City 2:2 Napoli. Mi unveröffentlicht. PL: Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic: Marco Penge siegt im Vierer-Playoff bei -16 (266) gegen Haotong Li und Thorbjornsen.",
    },
    "it": {
        "pinFinal": "Coppa Davis Bologna: Rep. Ceca 2-0 Canada; Italia-Corea ancora aperta dopo Musetti 6-0, 7-6(5) Hong. Torino: Alcaraz 6-2, 7-6(7) Zverev.",
        "week1Closed": "Thanksgiving NFL: Bears (8-2) a Detroit (8-2) 19:00, Eagles a Dallas 22:30, Chiefs a Buffalo (9-1) 02:20.",
        "week1Sub": "Lions e Bears (8-2) al Ford Field. Packers-Rams mercoledi inedito. Week 11: Texans 26-3 Colts (4-6 vs 3-8).",
        "countdownTnf": "THANKSGIVING DAY: Bears a Detroit (19:00). Eagles a Dallas (22:30). Chiefs a Buffalo (02:20).",
        "gridAfterMadrid": "Round 22 · GP del Qatar a Lusail (27-29 nov, formato classico, niente sprint)",
        "barsPoints": "Antonelli (402) e Mercedes (666) Campioni; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (11a g.): Arsenal 28 pt, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Seleziona un club. Arsenal 28, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "UCL 5a g. mar: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoli. Mer inedito. PL: Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic: Marco Penge trionfa allo spareggio a quattro a -16 (266) contro Haotong Li e Thorbjornsen.",
    },
    "pl": {
        "pinFinal": "Puchar Davisa Bolonia: Czechy 2:0 Kanada; Wlochy-Korea nadal otwarte po Musettim 6:0, 7:6(5) Hong. Turyn: Alcaraz 6:2, 7:6(7) Zverev.",
        "week1Closed": "Thanksgiving NFL: Bears (8-2) u Lions (8-2) 19:00 PL, Eagles u Cowboys 22:30, Chiefs u Bills (9-1) 02:20.",
        "week1Sub": "Lions i Bears (po 8-2) na Ford Field. Packers-Rams ze srody nieopublikowane. 11. tydzien: Texans 26:3 Colts (4-6 vs 3-8).",
        "countdownTnf": "THANKSGIVING DAY: Bears u Lions (19:00). Eagles u Cowboys (22:30). Chiefs u Bills (02:20).",
        "gridAfterMadrid": "Runda 22 · GP Kataru w Lusail (27-29 listopada, format klasyczny, bez sprintu)",
        "barsPoints": "Antonelli (402) i Mercedes (666) Mistrzowie; Verstappen 304, Hamilton 267, Russell 264, Norris 264, Leclerc 250.",
        "tableAfterMonday": "Premier League (11. kol.): Arsenal 28 pkt, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18.",
        "pinClub": "Wybierz klub. Arsenal 28 pkt, Brighton 22, Man City 22, Liverpool 21, Bournemouth 18, Brentford 17.",
        "plFootnote": "LM 5. kol. wt: Real Madryt 5:1 PSV, Arsenal 1:1 Dortmund, Man City 2:2 Napoli. Sr nieopublikowane. PL: Arsenal 28, Brighton 22, City 22.",
        "majorsDone": "The RSM Classic: Marco Penge wygrywa czteroosobowa dogrywke na -16 (266) przed Haotongiem Li i Thorbjornsenem.",
    },
    "zh": {
        "pinFinal": "戴维斯杯博洛尼亚：捷克2-0加拿大；意大利对韩国仍在进行（穆塞蒂6-0、7-6胜洪性成）。都灵：阿尔卡拉斯两盘击败兹维列夫夺冠。",
        "week1Closed": "NFL感恩节：熊队（8-2）客战雄狮（8-2）美东13:00，老鹰战牛仔16:30，酋长战比尔（9-1）20:20。",
        "week1Sub": "8胜2负雄狮主场迎战熊队。周三网飞包装工对公羊未公布完场。第11周：德州人26-3小马（4-6对3-8）。",
        "countdownTnf": "感恩节大赛：熊队战雄狮（13:00 CBS）。老鹰战牛仔（16:30 FOX）。酋长战比尔（20:20 NBC）。",
        "gridAfterMadrid": "第22站 · 卡塔尔大奖赛卢赛尔常规赛制无冲刺赛（11月27-29日）",
        "barsPoints": "安东内利（402）与梅赛德斯（666）加冕；维斯塔潘304，汉密尔顿267，拉塞尔264，诺里斯264。",
        "tableAfterMonday": "英超（第11轮）：阿森纳28分，布莱顿22分，曼城22分，利物浦21分，伯恩茅斯18分。",
        "pinClub": "选择俱乐部。阿森纳28分领跑，布莱顿22，曼城22，利物浦21，伯恩茅斯18，布伦特福德17。",
        "plFootnote": "欧冠第5轮周二：皇马5-1埃因霍温，阿森纳1-1多特，曼城2-2那不勒斯。周三未公布。英超：阿森纳28，布莱顿22，曼城22。",
        "majorsDone": "RSM精英赛：马尔科·彭奇四人加洞赛首洞以-16（266杆）力压李昊桐与索比约恩森夺冠。",
    },
    "ja": {
        "pinFinal": "デビスカップ・ボローニャ：チェコ2-0カナダ；イタリア対韓国はムゼッティ6-0、7-6後も未決着。トリノ：アルカラス全勝V。",
        "week1Closed": "感謝祭NFL：ベアーズ(8-2)対ライオンズ(8-2)13:00、イーグルス対カウボーイズ16:30、チーフス対ビルズ(9-1)20:20。",
        "week1Sub": "8勝2敗同士がフォード・フィールドで激突。水曜Netflixパッカーズ対ラムズは未公開。第11週：テキサンズ26-3コルツ（4-6対3-8）。",
        "countdownTnf": "感謝祭：ベアーズ対ライオンズ(13:00 CBS)。イーグルス対カウボーイズ(16:30 FOX)。チーフス対ビルズ(20:20 NBC)。",
        "gridAfterMadrid": "第22戦 · カタールGP ルサイル通常開催・スプリントなし（11月27-29日）",
        "barsPoints": "アントネッリ(402)＆メルセデス(666)王者；フェルスタッペン304、ハミルトン267、ラッセル264、ノリス264。",
        "tableAfterMonday": "プレミアリーグ（第11節）：アーセナル28、ブライトン22、マンC 22、リヴァプール21、ボーンマス18。",
        "pinClub": "クラブ選択：アーセナル28、ブライトン22、マンC 22、リヴァプール21、ボーンマス18、ブレントフォード17。",
        "plFootnote": "CL第5節火曜：Rマドリード5-1 PSV、アーセナル1-1ドルトムント、マンC 2-2ナポリ。水曜未公開。PL：アーセナル28、シティ22。",
        "majorsDone": "RSMクラシック：マルコ・ペンジが-16（266）4人POを制し李昊桐らを抑えPGAツアー初優勝。",
    },
    "ko": {
        "pinFinal": "데이비스 컵 볼로냐: 체코 2-0 캐나다; 이탈리아-한국은 무세티 6-0, 7-6 이후 아직 진행. 토리노: 알카라스 무패 우승.",
        "week1Closed": "추수감사절 NFL: 베어스(8-2) vs 라이온스(8-2) 13:00, 이글스 vs 카우보이스 16:30, 치프스 vs 빌스(9-1) 20:20.",
        "week1Sub": "8승 2패 동률 격돌. 수요일 넷플릭스 패커스-램스는 미공개. 11주차: 텍산스 26-3 콜츠(4-6 vs 3-8).",
        "countdownTnf": "추수감사절 데이: 베어스 vs 라이온스(13:00 CBS). 이글스 vs 카우보이스(16:30 FOX). 치프스 vs 빌스(20:20 NBC).",
        "gridAfterMadrid": "22라운드 · 카타르 GP 루사일 일반 포맷 스프린트 없음 (11월 27-29일)",
        "barsPoints": "안토넬리(402) 및 메르세데스(666) 우승; 페르스타펜 304, 해밀턴 267, 러셀 264, 노리스 264.",
        "tableAfterMonday": "프리미어리그(11R): 아스널 28점, 브라이튼 22, 맨시티 22, 리버풀 21, 본머스 18.",
        "pinClub": "클럽 선택: 아스널 28, 브라이튼 22, 맨시티 22, 리버풀 21, 본머스 18, 브렌트퍼드 17.",
        "plFootnote": "UCL 5차전 화: 레알 마드리드 5-1 PSV, 아스널 1-1 도르트문트, 맨시티 2-2 나폴리. 수 미공개. PL: 아스널 28, 브라이튼 22, 맨시티 22.",
        "majorsDone": "RSM 클래식: 마르코 펜지가 -16(266) 4인 연장전 첫 홀에서 리하오퉁 등을 제치고 생애 첫 우승.",
    },
    "ar": {
        "pinFinal": "كاس ديفيز بولونيا: التشيك 2-0 كندا؛ ايطاليا ضد كوريا ما زالت مفتوحة بعد موسيتي 6-0 و7-6(5). تورينو: الكاراز بطلا.",
        "week1Closed": "عيد الشكر NFL: بيرز (8-2) ضد لايونز (8-2) 1:00 ظهرا، ايغلز ضد كاوبويز 4:30، تشيفز ضد بيلز (9-1) 8:20.",
        "week1Sub": "صدام 8-2 في فورد فيلد. باكرز ورامز الاربعاء غير منشور. الاسبوع 11: تكسانز 26-3 كولتس (4-6 مقابل 3-8).",
        "countdownTnf": "يوم عيد الشكر: بيرز ضد لايونز (1:00 CBS). ايغلز ضد كاوبويز (4:30 FOX). تشيفز ضد بيلز (8:20 NBC).",
        "gridAfterMadrid": "الجولة 22 · جائزة قطر الكبرى في لوسيل (27-29 نوفمبر، الصيغة التقليدية بلا سبرنت)",
        "barsPoints": "انتونيللي (402) ومرسيدس (666) ابطال العالم؛ فيرستابن 304، هاميلتون 267، راسل 264، نوريس 264.",
        "tableAfterMonday": "الدوري الانجليزي (11): ارسنال 28، برايتون 22، مانشستر سيتي 22، ليفربول 21، بورنموث 18.",
        "pinClub": "اختر ناديا. ارسنال 28، برايتون 22، مانشستر سيتي 22، ليفربول 21، بورنموث 18، برينتفورد 17.",
        "plFootnote": "دوري الابطال الثلاثاء: ريال مدريد 5-1 ايندهوفن، ارسنال 1-1 دورتموند، مانشستر سيتي 2-2 نابولي. الاربعاء غير منشور.",
        "majorsDone": "بطولة RSM: ماركو بينجي يحسم التمايز الرباعي عند -16 (266) على حساب لي هاوتونغ وثوربيورنسن.",
    },
}

header_part, body_part = pg_txt.split("export const PLAYGROUND: Record<Locale, PlaygroundCopy> =", 1)
m_end = re.search(r"\};\s*export function", body_part)
if not m_end:
    raise SystemExit("playground object end not found")
brace = m_end.start()
obj_text = body_part[: brace + 1].strip()
pg_data = json.loads(obj_text)
tail = body_part[brace + 1 :]
for loc, upd in pg_updates.items():
    for k, v in upd.items():
        pg_data[loc][k] = v
pg_out = (
    header_part
    + "export const PLAYGROUND: Record<Locale, PlaygroundCopy> = "
    + json.dumps(pg_data, ensure_ascii=False, indent=2)
    + tail
)
if not tail.lstrip().startswith(";"):
    pg_out = (
        header_part
        + "export const PLAYGROUND: Record<Locale, PlaygroundCopy> = "
        + json.dumps(pg_data, ensure_ascii=False, indent=2)
        + ";\n"
        + tail.lstrip()
    )
no_dashes(pg_out, "playground.ts")
open(pg_path, "w", encoding="utf-8").write(pg_out)
print("playground.ts")

# ---------------------------------------------------------
# messages
# ---------------------------------------------------------
messages_updates = {
    "en": {
        "common_todayDesk": "Thursday desk: NFL Thanksgiving (8-2 Bears at 8-2 Lions, Chiefs 8-2 at Bills 9-1). UCL MD5 Tuesday: Real Madrid 5-1 PSV. Davis Cup Bologna. Qatar GP Friday.",
        "common_todayNfl": "Thanksgiving Day: Bears (8-2) at Lions (8-2) 1:00 PM ET CBS, Eagles (3-7) at Cowboys (5-6) 4:30 PM ET FOX, Chiefs (8-2) at Bills (9-1) 8:20 PM ET NBC.",
        "common_todayTnf": "Thanksgiving Eve Wed 8:00 PM ET (Netflix): Packers (6-4) at Rams (6-4) unpublished as final. Thu opener: Bears at Lions at Ford Field.",
        "football_tagline": "Thanksgiving Football: 8-2 Bears at 8-2 Lions open Thursday tripleheader after Wed Packers-Rams on Netflix.",
        "football_liveNow": "Thu Nov 26: Bears (8-2) at Lions (8-2) 1 PM ET CBS, Eagles (3-7) at Cowboys (5-6) 4:30 PM FOX, Chiefs (8-2) at Bills (9-1) 8:20 PM NBC. Wed Netflix Packers-Rams unpublished. Week 11: Texans 26-3 Colts (HOU 4-6).",
        "football_pulse": "NFL WEEK 12 THANKSGIVING: IDENTICAL 8-2 LIONS AND BEARS CLASH FOR NFC NORTH LEAD; CHIEFS VISIT 9-1 BILLS",
        "tennis_tagline": "Davis Cup Final 8 in Bologna: Czechia through 2-0; Italy vs Korea still open; Alcaraz crowned in Turin.",
        "tennis_liveNow": "Davis Cup Bologna: Czechia d Canada 2-0; Italy vs Korea open after Musetti d Hong 6-0, 7-6(5). Thu QFs: GB vs Germany 10:00 CET, Austria vs Spain 17:00 CET. Turin Final: Alcaraz d Zverev 6-2, 7-6(7).",
        "tennis_pulse": "DAVIS CUP FINALS: CZECHIA INTO THE LAST FOUR; GREAT BRITAIN VS GERMANY OPENS THURSDAY IN BOLOGNA",
        "f1_tagline": "Qatar GP next (27-29 Nov): Verstappen carries Las Vegas victory into a standard Lusail weekend with no sprint.",
        "f1_liveNow": "Vegas GP Final: 1. Verstappen 1:27:39.624, 2. Norris +0.639s, 3. Piastri from P17; Russell P9 +13.192s. Standings: Antonelli 402 (Champ), Verstappen 304, Hamilton 267, Russell 264, Norris 264. Qatar Fri FP1.",
        "f1_pulse": "FORMULA 1: VERSTAPPEN WINS LAS VEGAS AS MCLAREN CUT RED BULL CONSTRUCTORS GAP TO 9 POINTS",
        "soccer_tagline": "Champions League MD5: Real Madrid storm past PSV 5-1 to sit alone on 15 points; Wednesday slate unpublished.",
        "soccer_liveNow": "UCL Tue: Real Madrid 5-1 PSV (Mbappe 64, 84), Arsenal 1-1 Dortmund (Gyokeres 10; Beier 55), Man City 2-2 Napoli. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1-1 Fulham (Anderson 57; Muniz 16).",
        "soccer_pulse": "CHAMPIONS LEAGUE MD5: REAL MADRID HIT 15 POINTS AT SUMMIT AFTER 5-1 PSV; ARSENAL LEAD PL ON 28",
        "basketball_tagline": "Emirates NBA Cup before Thanksgiving rest: Mavericks beat Nuggets 120-101; Celtics drop 131 on Wizards.",
        "basketball_liveNow": "Tue Cup: Mavericks 120-101 Nuggets (Flagg 24/6/12); Celtics 131-116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104-86 Magic (Joe 21). Wed unpublished. Thu rest.",
        "basketball_pulse": "EMIRATES NBA CUP: MAVS CRUISE BEHIND COOPER FLAGG AND TATUM SCORES 41 AS THE LEAGUE TAKES THANKSGIVING OFF",
        "golf_tagline": "Marco Penge captures maiden PGA Tour victory in a four-man Sea Island playoff at The RSM Classic.",
        "golf_liveNow": "RSM Classic Final (23 Nov): Marco Penge (-16, 266) wins 1st playoff hole over Haotong Li, Michael Thorbjornsen, and Max Greyserman. Next: Hero World Challenge (3-6 Dec).",
        "golf_pulse": "PGA TOUR: MARCO PENGE CAPS FOUR-WAY PLAYOFF AT SEA ISLAND FOR MAIDEN WIN AND 2027 MASTERS TICKET",
        "home_tonight": "Thursday desk",
        "home_tonightBlurb": "Thanksgiving NFL: 8-2 Bears at 8-2 Lions open Thursday (1:00 PM ET CBS) and Chiefs at 9-1 Bills cap the night. Wed Packers-Rams unpublished. UCL MD5: Real Madrid 5-1 PSV. Davis Cup Bologna: Czechia through, Italy vs Korea still open. Qatar GP Friday.",
        "home_plTitle": "Arsenal lead Premier League on 28; Real Madrid hit 15 points atop Champions League",
        "home_plBlurb": "PL after MW11: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1-1 Fulham (Anderson 57, Muniz 16). UCL Tuesday: Real Madrid 5-1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1-1 Dortmund.",
        "home_f1Title": "Qatar Grand Prix next: Verstappen carries Las Vegas win to Lusail with P3 split by three points",
        "home_f1Blurb": "Antonelli (402) and Mercedes (666) hold both 2026 titles, while Verstappen sits 2nd on 304 after Las Vegas. Just 3 points divide Hamilton (267) from Russell and Norris (264), and McLaren (431) sit 9 behind Red Bull (440).",
    },
    "fr": {
        "common_todayDesk": "Bureau du jeudi : Thanksgiving NFL (Bears 8-2 chez Lions 8-2, Chiefs 8-2 chez Bills 9-1). LDC J5 mardi : Real Madrid 5-1 PSV. Coupe Davis a Bologne. GP du Qatar vendredi.",
        "common_todayNfl": "Thanksgiving NFL : Bears (8-2) chez Lions (8-2) 13h00 ET CBS, Eagles (3-7) chez Cowboys (5-6) 16h30 ET FOX, Chiefs (8-2) chez Bills (9-1) 20h20 ET NBC.",
        "common_todayTnf": "Mercredi soir sur Netflix : Packers (6-4) chez Rams (6-4), resultat inedit. Jeudi : Bears chez Lions a Ford Field.",
        "football_tagline": "Thanksgiving NFL : Lions et Bears (8-2) ouvrent jeudi apres Packers-Rams mercredi sur Netflix.",
        "football_liveNow": "Jeudi 26 nov : Bears (8-2) chez Lions (8-2) 13h00 ET CBS, Eagles-Cowboys 16h30 FOX, Chiefs-Bills (9-1) 20h20 NBC. Packers-Rams mercredi inedit. S11 : Texans 26-3 Colts (HOU 4-6).",
        "football_pulse": "NFL THANKSGIVING : LIONS ET BEARS A 8-2 POUR LA TETE DE LA NFC NORD ; CHIEFS CHEZ BILLS 9-1 EN SOIREE",
        "tennis_tagline": "Coupe Davis a Bologne : la Tchequie qualifiee 2-0 ; Italie-Coree encore ouverte ; Alcaraz sacre a Turin.",
        "tennis_liveNow": "Coupe Davis Bologne : Tchequie 2-0 Canada ; Italie-Coree ouverte apres Musetti 6-0, 7-6(5) Hong. Jeudi : GB-Allemagne 10h00, Autriche-Espagne 17h00. Turin : Alcaraz bat Zverev 6-2, 7-6(7).",
        "tennis_pulse": "COUPE DAVIS : LA TCHEQUIE EN DEMI ; GRANDE-BRETAGNE - ALLEMAGNE OUVRE LE JEUDI A BOLOGNE",
        "f1_tagline": "GP du Qatar (27-29 nov) : Verstappen emporte son succes de Las Vegas vers le format classique de Lusail, sans sprint.",
        "f1_liveNow": "Las Vegas GP : 1. Verstappen 1:27:39.624, 2. Norris +0,639s, 3. Piastri (de P17) ; Russell 9e +13,192s. Pilotes : Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264. Qatar vendredi.",
        "f1_pulse": "FORMULE 1 : VERSTAPPEN REMPORTE VEGAS ET MCLAREN REVIENT A 9 PTS DE RED BULL",
        "soccer_tagline": "Ligue des champions J5 : le Real Madrid ecrase le PSV 5-1 et reste seul a 15 points ; mercredi inedit.",
        "soccer_liveNow": "LDC mardi : Real Madrid 5-1 PSV (Mbappe 64, 84), Arsenal 1-1 Dortmund (Gyokeres 10 ; Beier 55), Man City 2-2 Naples. PL : Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1-1 Fulham (Anderson 57 ; Muniz 16).",
        "soccer_pulse": "LIGUE DES CHAMPIONS : REAL MADRID SEUL A 15 POINTS APRES LE 5-1 CONTRE LE PSV ; ARSENAL MENE LA PL A 28",
        "basketball_tagline": "Avant la pause de Thanksgiving NBA : Dallas bat Denver 120-101 et Boston bat Washington 131-116.",
        "basketball_liveNow": "NBA Cup mardi : Mavericks 120-101 Nuggets (Flagg 24/6/12) ; Celtics 131-116 Wizards (Tatum 41, George 28 ; Davis 33/13) ; Pistons 104-86 Magic (Joe 21). Mercredi inedit. Jeudi pause.",
        "basketball_pulse": "EMIRATES NBA CUP : COOPER FLAGG ET TATUM (41 PTS) BRILLENT AVANT LA RELACHE DE THANKSGIVING",
        "golf_tagline": "Marco Penge decroche sa premiere victoire sur le PGA Tour en barrage a quatre au RSM Classic.",
        "golf_liveNow": "RSM Classic (23 nov) : Marco Penge (-16, 266) gagne au 1er trou de playoff devant Haotong Li, Michael Thorbjornsen et Max Greyserman. Suite : Hero World Challenge (3-6 dec).",
        "golf_pulse": "PGA TOUR : MARCO PENGE S'IMPOSE EN BARRAGE A SEA ISLAND POUR UN PREMIER SACRE SUR LE CIRCUIT",
        "home_tonight": "Bureau du jeudi",
        "home_tonightBlurb": "Thanksgiving NFL : Bears (8-2) chez Lions (8-2) puis Chiefs chez Bills (9-1). Packers-Rams mercredi inedit. LDC : Real Madrid 5-1 PSV. Coupe Davis : Tchequie qualifiee, Italie-Coree encore ouverte. GP du Qatar vendredi.",
        "home_plTitle": "Arsenal mene la Premier League avec 28 points ; le Real Madrid seul en tete de la C1",
        "home_plBlurb": "PL J11 : Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1-1 Fulham (Anderson 57, Muniz 16). LDC : Real Madrid 5-1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1-1 Dortmund.",
        "home_f1Title": "Cap sur Lusail : Verstappen emmene sa victoire de Las Vegas au Qatar, trois points pour le podium mondial",
        "home_f1Blurb": "Antonelli (402) et Mercedes (666) sont deja sacres, Verstappen pointe a 304 pts apres Las Vegas. Hamilton (267) ne devance Russell et Norris (264) que de trois points. McLaren (431) est a 9 de Red Bull (440).",
    },
    "es": {
        "common_todayDesk": "Mesa del jueves: Thanksgiving NFL (Bears 8-2 en Lions 8-2, Chiefs 8-2 en Bills 9-1). UCL J5 martes: Real Madrid 5-1 PSV. Copa Davis en Bolonia. GP de Catar el viernes.",
        "common_todayNfl": "Dia de Accion de Gracias: Bears (8-2) en Lions (8-2) 1:00 PM ET CBS, Eagles (3-7) en Cowboys (5-6) 4:30 PM ET FOX, Chiefs (8-2) en Bills (9-1) 8:20 PM ET NBC.",
        "common_todayTnf": "Miercoles en Netflix: Packers (6-4) en Rams (6-4) sin publicar. Jueves: Bears en Lions en Ford Field.",
        "football_tagline": "Accion de Gracias NFL: Lions y Bears (8-2) abren el jueves tras Packers-Rams en Netflix.",
        "football_liveNow": "Jueves 26 nov: Bears (8-2) en Lions (8-2) 1 PM ET CBS, Eagles-Cowboys 4:30 PM FOX, Chiefs (8-2) en Bills (9-1) 8:20 PM NBC. Packers-Rams miercoles inedito. Semana 11: Texans 26-3 Colts (HOU 4-6).",
        "football_pulse": "NFL THANKSGIVING: LIONS Y BEARS (8-2) SE JUEGAN LA NFC NORTE; CHIEFS VISITA A BILLS 9-1 EN ESTELAR",
        "tennis_tagline": "Copa Davis Bolonia: Chequia pasa 2-0; Italia-Corea sigue abierta; Carlos Alcaraz campeon invicto en Turin.",
        "tennis_liveNow": "Copa Davis Bolonia: Chequia 2-0 Canada; Italia-Corea abierta tras Musetti 6-0, 7-6(5) Hong. Jueves: GB-Alemania 10:00, Austria-Espana 17:00. Turin: Alcaraz d. Zverev 6-2, 7-6(7).",
        "tennis_pulse": "COPA DAVIS: CHEQUIA A SEMIS; GRAN BRETANA CONTRA ALEMANIA ABRE EL JUEVES EN BOLONIA",
        "f1_tagline": "Proxima parada GP de Catar (27-29 nov): Verstappen lleva su triunfo de Las Vegas a Lusail en formato clasico, sin sprint.",
        "f1_liveNow": "Las Vegas GP: 1. Verstappen 1:27:39.624, 2. Norris +0,639s, 3. Piastri (desde P17); Russell 9o +13,192s. Pilotos: Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264. Catar viernes.",
        "f1_pulse": "FORMULA 1: VERSTAPPEN VENCE EN LAS VEGAS Y MCLAREN SE ACERCA A 9 PUNTOS DE RED BULL",
        "soccer_tagline": "Champions League J5: Real Madrid golea 5-1 al PSV y se queda solo con 15 puntos; miercoles inedito.",
        "soccer_liveNow": "UCL martes: Real Madrid 5-1 PSV (Mbappe 64, 84), Arsenal 1-1 Dortmund (Gyokeres 10; Beier 55), Man City 2-2 Napoles. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1-1 Fulham (Anderson 57; Muniz 16).",
        "soccer_pulse": "CHAMPIONS LEAGUE: REAL MADRID PLENO DE 15 PUNTOS TRAS EL 5-1 AL PSV; ARSENAL LIDER DE LA PL CON 28",
        "basketball_tagline": "Antes del paron de Accion de Gracias: Dallas vence 120-101 a Denver y Boston 131-116 a Washington.",
        "basketball_liveNow": "NBA Cup martes: Mavericks 120-101 Nuggets (Flagg 24/6/12); Celtics 131-116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104-86 Magic (Joe 21). Miercoles inedito. Jueves descanso.",
        "basketball_pulse": "EMIRATES NBA CUP: COOPER FLAGG Y JAYSON TATUM (41 PTS) BRILLAN ANTES DE LA PAUSA DEL JUEVES",
        "golf_tagline": "Marco Penge gana su primer titulo PGA Tour en desempate cuadruple en The RSM Classic.",
        "golf_liveNow": "RSM Classic (23 nov): Marco Penge (-16, 266) vence en el primer hoyo extra a Haotong Li, Michael Thorbjornsen y Max Greyserman. Siguiente: Hero World Challenge (3-6 dic).",
        "golf_pulse": "PGA TOUR: MARCO PENGE CONQUISTA SEA ISLAND EN DESEMPATE PARA LOGRAR SU PRIMER TROFEO",
        "home_tonight": "Mesa del jueves",
        "home_tonightBlurb": "Thanksgiving NFL: Bears (8-2) en Lions (8-2) y Chiefs en Bills (9-1). Packers-Rams del miercoles inedito. UCL: Real Madrid 5-1 PSV. Copa Davis: Chequia clasificada, Italia-Corea abierta. GP de Catar el viernes.",
        "home_plTitle": "Arsenal domina la Premier con 28 puntos; Real Madrid lider solitario de la Champions",
        "home_plBlurb": "PL tras J11: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1-1 Fulham (Anderson 57, Muniz 16). UCL: Real Madrid 5-1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1-1 Dortmund.",
        "home_f1Title": "Llega el GP de Catar: Verstappen lleva el triunfo de Las Vegas a Lusail y tres puntos por el podio",
        "home_f1Blurb": "Con Antonelli (402) y Mercedes (666) campeones, Verstappen suma 304 tras Las Vegas. Tres puntos separan a Hamilton (267) de Russell y Norris (264), con McLaren a nueve de Red Bull.",
    },
    "de": {
        "common_todayDesk": "Donnerstag-Desk: Thanksgiving NFL (Bears 8-2 bei Lions 8-2, Chiefs 8-2 bei Bills 9-1). UCL 5. Sp. Dienstag: Real 5:1 PSV. Davis Cup Bologna. Katar GP am Freitag.",
        "common_todayNfl": "Thanksgiving Day: Bears (8-2) bei Lions (8-2) 1:00 PM ET CBS, Eagles (3-7) bei Cowboys (5-6) 4:30 PM FOX, Chiefs (8-2) bei Bills (9-1) 8:20 PM NBC.",
        "common_todayTnf": "Mittwoch auf Netflix: Packers (6-4) bei Rams (6-4) unveröffentlicht. Donnerstag: Bears bei Lions im Ford Field.",
        "football_tagline": "Thanksgiving Football: 8-2 Lions gegen 8-2 Bears eroeffnen Donnerstag nach Packers-Rams.",
        "football_liveNow": "Do 26. Nov.: Bears (8-2) bei Lions (8-2) 1 PM ET CBS, Eagles bei Cowboys 4:30 PM FOX, Chiefs bei Bills (9-1) 8:20 PM NBC. Packers-Rams Mi unveröffentlicht. Woche 11: Texans 26:3 Colts (HOU 4-6).",
        "football_pulse": "NFL THANKSGIVING: LIONS UND BEARS (8-2) UM NFC NORTH; CHIEFS BEI BILLS 9-1 IM TOPSPIEL",
        "tennis_tagline": "Davis Cup Final 8 Bologna: Tschechien weiter 2:0; Italien gegen Korea noch offen; Alcaraz Turin-Champion.",
        "tennis_liveNow": "Davis Cup Bologna: Tschechien 2:0 Kanada; Italien-Korea offen nach Musetti 6:0, 7:6(5) Hong. Do: GB-Deutschland 10:00, Oesterreich-Spanien 17:00. Turin: Alcaraz 6:2, 7:6(7) Zverev.",
        "tennis_pulse": "DAVIS CUP: TSCHECHIEN IM HALBFINALE; GROSSBRITANNIEN GEGEN DEUTSCHLAND EROEFFNET DONNERSTAG IN BOLOGNA",
        "f1_tagline": "Katar GP (27.-29. Nov.): Verstappen bringt Las-Vegas-Sieg nach Lusail im Standard-Format ohne Sprint.",
        "f1_liveNow": "Vegas GP: 1. Verstappen 1:27:39.624, 2. Norris +0,639s, 3. Piastri (von P17); Russell P9 +13,192s. WM-Stand: Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264. Katar Fr FP1.",
        "f1_pulse": "FORMEL 1: VERSTAPPEN GEWINNT LAS VEGAS; MCLAREN NUR 9 PKT HINTER RED BULL",
        "soccer_tagline": "Champions League 5. Sp.: Real Madrid schlaegt PSV 5:1 und bleibt allein mit 15 Punkten; Mittwoch unveröffentlicht.",
        "soccer_liveNow": "UCL Di: Real Madrid 5:1 PSV (Mbappe 64, 84), Arsenal 1:1 Dortmund (Gyokeres 10; Beier 55), Man City 2:2 Napoli. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1:1 Fulham (Anderson 57; Muniz 16).",
        "soccer_pulse": "CHAMPIONS LEAGUE: REAL MADRID MIT 15 PUNKTEN GANZ OBEN NACH 5:1 GEGEN PSV; ARSENAL FUEHRT DIE PL MIT 28",
        "basketball_tagline": "NBA vor Thanksgiving-Pause: Dallas bezwingt Denver 120:101; Boston schlaegt Wizards 131:116.",
        "basketball_liveNow": "NBA Cup Di: Mavericks 120:101 Nuggets (Flagg 24/6/12); Celtics 131:116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104:86 Magic (Joe 21). Mi unveröffentlicht. Do spielfrei.",
        "basketball_pulse": "EMIRATES NBA CUP: COOPER FLAGG UND TATUM (41 PKT) GLANZEN VOR DER THANKSGIVING-PAUSE",
        "golf_tagline": "Marco Penge gewinnt Vierer-Playoff auf Sea Island fuer ersten PGA-Tour-Titel beim RSM Classic.",
        "golf_liveNow": "RSM Classic Finale (23. Nov.): Marco Penge (-16, 266) siegt am 1. Extraloch vor Haotong Li, Michael Thorbjornsen und Max Greyserman. Weiter: Hero World Challenge (3.-6. Dez.).",
        "golf_pulse": "PGA TOUR: MARCO PENGE HOLT ERSTEN TITEL IM PLAYOFF AUF SEA ISLAND",
        "home_tonight": "Donnerstag-Desk",
        "home_tonightBlurb": "Thanksgiving NFL: Bears (8-2) bei Lions (8-2) und Chiefs bei Bills (9-1). Packers-Rams Mittwoch unveröffentlicht. UCL: Real Madrid 5:1 PSV. Davis Cup: Tschechien weiter, Italien-Korea offen. Katar GP Freitag.",
        "home_plTitle": "Arsenal fuehrt die Premier League mit 28 Punkten an; Real Madrid makellos Erster in Europa",
        "home_plBlurb": "PL nach 11. Sp.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1:1 Fulham (Anderson 57, Muniz 16). UCL: Real 5:1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1:1 Dortmund.",
        "home_f1Title": "Vorschau Katar GP: Verstappen reist mit Las-Vegas-Sieg nach Lusail im engen Kampf um Platz drei",
        "home_f1Blurb": "Weltmeister Antonelli (402) und Mercedes (666) stehen fest, waehrend Verstappen nach Vegas 304 Punkte haelt. Nur 3 Punkte trennen Hamilton (267) von Russell und Norris (264).",
    },
    "it": {
        "common_todayDesk": "Desk del giovedi: Thanksgiving NFL (Bears 8-2 a Detroit 8-2, Chiefs 8-2 a Buffalo 9-1). UCL 5a g. martedi: Real Madrid 5-1 PSV. Coppa Davis Bologna. GP Qatar venerdi.",
        "common_todayNfl": "Ringraziamento: Bears (8-2) a Detroit (8-2) 19:00, Eagles a Dallas 22:30, Chiefs (8-2) a Buffalo (9-1) 02:20.",
        "common_todayTnf": "Mercoledi su Netflix: Packers (6-4) contro Rams (6-4) inedito. Giovedi: Bears-Lions al Ford Field.",
        "football_tagline": "Thanksgiving NFL: Lions e Bears (8-2) inaugurano il giovedi dopo Packers-Rams su Netflix.",
        "football_liveNow": "Giovedi 26 nov: Bears (8-2) a Detroit (8-2) 19:00, Eagles-Cowboys 22:30, Chiefs-Bills (9-1) 02:20. Packers-Rams mercoledi inedito. Week 11: Texans 26-3 Colts (HOU 4-6).",
        "football_pulse": "NFL THANKSGIVING: LIONS E BEARS (8-2) PER LA NFC NORTH; CHIEFS A BUFFALO 9-1 IN NOTTURNA",
        "tennis_tagline": "Coppa Davis Bologna: Rep. Ceca avanti 2-0; Italia-Corea ancora aperta; Alcaraz campione imbattuto a Torino.",
        "tennis_liveNow": "Coppa Davis Bologna: Rep. Ceca 2-0 Canada; Italia-Corea aperta dopo Musetti 6-0, 7-6(5) Hong. Gio: GB-Germania 10:00, Austria-Spagna 17:00. Torino: Alcaraz 6-2, 7-6(7) Zverev.",
        "tennis_pulse": "COPPA DAVIS: REPUBBLICA CECA IN SEMIFINALE; GRAN BRETAGNA-GERMANIA APRE IL GIOVEDI A BOLOGNA",
        "f1_tagline": "GP del Qatar (27-29 nov): Verstappen porta il trionfo di Las Vegas a Lusail in formato classico, senza sprint.",
        "f1_liveNow": "Las Vegas GP: 1. Verstappen 1:27:39.624, 2. Norris +0,639s, 3. Piastri (da P17); Russell 9o +13,192s. Piloti: Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264. Qatar ven FP1.",
        "f1_pulse": "FORMULA 1: VERSTAPPEN VINCE A VEGAS E MCLAREN A 9 PT DALLA RED BULL",
        "soccer_tagline": "Champions League 5a g.: Real Madrid 5-1 al PSV e resta solo a quota 15; mercoledi inedito.",
        "soccer_liveNow": "UCL mar: Real Madrid 5-1 PSV (Mbappe 64, 84), Arsenal 1-1 Dortmund (Gyokeres 10; Beier 55), Man City 2-2 Napoli. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1-1 Fulham (Anderson 57; Muniz 16).",
        "soccer_pulse": "CHAMPIONS LEAGUE: REAL MADRID SOLO A QUOTA 15 DOPO IL 5-1 AL PSV; ARSENAL GUIDA LA PL A 28",
        "basketball_tagline": "Prima della sosta del Ringraziamento NBA: Dallas espugna Denver 120-101; Boston 131-116 a Washington.",
        "basketball_liveNow": "NBA Cup mar: Mavericks 120-101 Nuggets (Flagg 24/6/12); Celtics 131-116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104-86 Magic (Joe 21). Mer inedito. Gio riposo.",
        "basketball_pulse": "EMIRATES NBA CUP: COOPER FLAGG E JAYSON TATUM (41 PT) BRILLANO PRIMA DELLA SOSTA DI GIOVEDI",
        "golf_tagline": "Marco Penge vince lo spareggio a quattro a Sea Island per il primo titolo PGA Tour al RSM Classic.",
        "golf_liveNow": "RSM Classic (23 nov): Marco Penge (-16, 266) supera alla 1a buca extra Haotong Li, Michael Thorbjornsen e Max Greyserman. Prossima: Hero World Challenge (3-6 dic).",
        "golf_pulse": "PGA TOUR: MARCO PENGE TRIONFA AL PLAYOFF A SEA ISLAND E CONQUISTA IL PRIMO TROFEO",
        "home_tonight": "Desk del giovedi",
        "home_tonightBlurb": "Thanksgiving NFL: Bears (8-2) a Detroit e Chiefs a Buffalo (9-1). Packers-Rams mercoledi inedito. UCL: Real Madrid 5-1 PSV. Coppa Davis: Ceca avanti, Italia-Corea aperta. GP Qatar venerdi.",
        "home_plTitle": "Arsenal guida la Premier a quota 28; Real Madrid capolista solitario in Champions",
        "home_plBlurb": "PL 11a g.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1-1 Fulham (Anderson 57, Muniz 16). UCL: Real 5-1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1-1 Dortmund.",
        "home_f1Title": "Verso il Qatar: Verstappen sbarca a Lusail dopo Las Vegas con 3 punti per il podio",
        "home_f1Blurb": "Antonelli (402) e Mercedes (666) gia campioni, Verstappen sale a 304 dopo Las Vegas. Appena 3 punti separano Hamilton (267) da Russell e Norris (264).",
    },
    "pl": {
        "common_todayDesk": "Czwartkowy desk: Thanksgiving NFL (Bears 8-2 u Lions 8-2, Chiefs 8-2 u Bills 9-1). LM 5. kol. wtorek: Real 5:1 PSV. Puchar Davisa w Bolonii. GP Kataru w piatek.",
        "common_todayNfl": "Thanksgiving Day: Bears (8-2) u Lions (8-2) 19:00, Eagles u Cowboys 22:30, Chiefs (8-2) u Bills (9-1) 02:20.",
        "common_todayTnf": "Sroda na Netflixie: Packers (6-4) u Rams (6-4) nieopublikowane. Czwartek: Bears u Lions na Ford Field.",
        "football_tagline": "Thanksgiving NFL: Lions i Bears (8-2) otwieraja czwartek po Packers-Rams na Netflixie.",
        "football_liveNow": "Czw 26 list.: Bears (8-2) u Lions (8-2) 19:00, Eagles-Cowboys 22:30, Chiefs-Bills (9-1) 02:20. Packers-Rams sroda nieopublikowane. Tydzien 11: Texans 26:3 Colts (HOU 4-6).",
        "football_pulse": "NFL THANKSGIVING: LIONS I BEARS (8-2) O PRYM W NFC NORTH; CHIEFS U BILLS 9-1 W NOCNYM HICIE",
        "tennis_tagline": "Puchar Davisa w Bolonii: Czechy dalej 2:0; Wlochy-Korea nadal otwarte; Alcaraz mistrzem w Turynie.",
        "tennis_liveNow": "Bolonia: Czechy 2:0 Kanada; Wlochy-Korea otwarte po Musettim 6:0, 7:6(5) Hong. Czw: GB-Niemcy 10:00, Austria-Hiszpania 17:00. Turyn: Alcaraz 6:2, 7:6(7) Zverev.",
        "tennis_pulse": "PUCHAR DAVISA: CZECHY W POLFINALE; WIELKA BRYTANIA KONTRA NIEMCY OTWIERA CZWARTEK W BOLONII",
        "f1_tagline": "Przed GP Kataru (27-29 list.): Verstappen przenosi triumf z Vegas do Lusail w klasycznym formacie bez sprintu.",
        "f1_liveNow": "Las Vegas GP: 1. Verstappen 1:27:39.624, 2. Norris +0,639s, 3. Piastri (z P17); Russell P9 +13,192s. Kierowcy: Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264. Katar pt FP1.",
        "f1_pulse": "FORMULA 1: VERSTAPPEN WYGRYWA W VEGAS; MCLAREN 9 PKT ZA RED BULLEM",
        "soccer_tagline": "Liga Mistrzow 5. kol.: Real Madryt rozbil PSV 5:1 i zostaje sam na 15 pkt; sroda nieopublikowana.",
        "soccer_liveNow": "LM wt: Real Madryt 5:1 PSV (Mbappe 64, 84), Arsenal 1:1 Dortmund (Gyokeres 10; Beier 55), Man City 2:2 Napoli. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1:1 Fulham (Anderson 57; Muniz 16).",
        "soccer_pulse": "LIGA MISTRZOW: REAL MADRYT Z KOMPLETEM 15 PKT PO 5:1 Z PSV; ARSENAL LIDERE PL Z 28",
        "basketball_tagline": "Przed czwartkowa pauza w NBA: Dallas ogralo Denver 120:101, a Boston rzucil 131 punktow Wizards.",
        "basketball_liveNow": "NBA Cup wt: Mavericks 120:101 Nuggets (Flagg 24/6/12); Celtics 131:116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104:86 Magic (Joe 21). Sr nieopublikowane. Czw wolne.",
        "basketball_pulse": "EMIRATES NBA CUP: COOPER FLAGG I JAYSON TATUM (41 PKT) BLYSZCZA PRZED SWIATECZNA PAUZA",
        "golf_tagline": "Marco Penge wygrywa czteroosobowa dogrywke na Sea Island i zdobywa pierwszy tytul PGA Tour.",
        "golf_liveNow": "The RSM Classic (23 list.): Marco Penge (-16, 266) lepszy na 1. dodatkowym dolku od Haotonga Li, Thorbjornsena i Greysermana. Dalej: Hero World Challenge (3-6 grud.).",
        "golf_pulse": "PGA TOUR: MARCO PENGE ZWYCIEZA W DOGRYWCE NA SEA ISLAND I ZDOBYWA PREMIEROWY PUCHAR",
        "home_tonight": "Czwartkowy desk",
        "home_tonightBlurb": "Thanksgiving NFL: Bears (8-2) u Lions (8-2) oraz Chiefs u Bills (9-1). Packers-Rams sroda nieopublikowane. LM: Real Madryt 5:1 PSV. Puchar Davisa: Czechy dalej, Wlochy-Korea otwarte. GP Kataru w piatek.",
        "home_plTitle": "Arsenal liderem Premier League z 28 pkt; Real Madryt samotnie na czele Ligi Mistrzow",
        "home_plBlurb": "PL po 11. kol.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1:1 Fulham (Anderson 57, Muniz 16). LM: Real 5:1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1:1 Dortmund.",
        "home_f1Title": "Zapowiedz GP Kataru: Verstappen z wygrana w Vegas w drodze do Lusail, trzy punkty na podium",
        "home_f1Blurb": "Mistrzowie Antonelli (402) i Mercedes (666) sa juz pewni, Verstappen ma 304 pkt po Las Vegas. Zaledwie 3 punkty dziela Hamiltona (267) od Russella i Norrisa (264).",
    },
    "zh": {
        "common_todayDesk": "周四体育台：NFL感恩节大战（熊8-2战雄狮8-2，酋长8-2战比尔9-1）。欧冠第5轮周二皇马5-1大胜。戴维斯杯博洛尼亚。周五卡塔尔大奖赛。",
        "common_todayNfl": "感恩节赛程：熊（8-2）战雄狮（8-2）13:00 CBS，老鹰战牛仔16:30 FOX，酋长（8-2）战比尔（9-1）20:20 NBC。",
        "common_todayTnf": "周三网飞先战：包装工（6-4）客战公羊（6-4）尚未公布完场。周四熊狮福特球场揭幕。",
        "football_tagline": "NFL感恩节：周三网飞大战后，同积8胜2负的雄狮与熊队周四揭幕。",
        "football_liveNow": "周四11月26日：熊（8-2）战雄狮（8-2）13:00 CBS，老鹰战牛仔16:30 FOX，酋长（8-2）战比尔（9-1）20:20 NBC。周三包装工对公羊未公布。第11周：德州人26-3小马（休斯敦4-6）。",
        "football_pulse": "NFL感恩节：8胜2负雄狮与熊队直面国北榜首之争；酋长压轴客战9胜1负比尔",
        "tennis_tagline": "戴维斯杯博洛尼亚总决赛：捷克2-0晋级；意大利对韩国仍在进行；阿尔卡拉斯都灵封王。",
        "tennis_liveNow": "博洛尼亚：捷克2-0加拿大；意大利对韩国在穆塞蒂6-0、7-6胜洪性成后仍未完结。周四英德10:00、奥西17:00。都灵：阿尔卡拉斯胜兹维列夫。",
        "tennis_pulse": "戴维斯杯：捷克杀入四强；周四博洛尼亚英国对德国揭幕",
        "f1_tagline": "卡塔尔大奖赛（11月27-29日）：维斯塔潘挟拉斯维加斯胜利抵达卢赛尔常规周末，不设冲刺赛。",
        "f1_liveNow": "拉斯维加斯站：1.维斯塔潘1:27:39.624，2.诺里斯+0.639秒，3.皮亚斯特里（第17起步）；拉塞尔第9+13.192秒。积分：安东内利402，维斯塔潘304，汉密尔顿267，拉塞尔264，诺里斯264。周五卡塔尔练习赛。",
        "f1_pulse": "F1：维斯塔潘称霸维加斯，迈凯伦距红牛仅剩9分",
        "soccer_tagline": "欧冠第5轮：皇马5-1横扫埃因霍温独居15分；周三赛程未公布。",
        "soccer_liveNow": "欧冠周二：皇马5-1埃因霍温（姆巴佩64、84），阿森纳1-1多特（哲凯雷什10；拜尔55），曼城2-2那不勒斯。英超：阿森纳28，布莱顿22，曼城22，利物浦21。曼城1-1富勒姆（安德森57；穆尼斯16）。",
        "soccer_pulse": "欧冠第5轮：皇马15分独居榜首；阿森纳以28分领跑英超",
        "basketball_tagline": "NBA感恩节休战前夕：独行侠120-101胜掘金，凯尔特人131-116力克奇才。",
        "basketball_liveNow": "周二NBA杯：独行侠120-101掘金（弗拉格24/6/12）；绿军131-116奇才（塔图姆41，乔治28；戴维斯33/13）；活塞104-86魔术（乔21）。周三未公布。周四休战。",
        "basketball_pulse": "NBA杯：库珀·弗拉格24+12与塔图姆狂轰41分点燃感恩节前夜",
        "golf_tagline": "马尔科·彭奇在海岛四人加洞赛夺得RSM精英赛冠军，收获美巡首冠。",
        "golf_liveNow": "RSM精英赛（11月23日）：彭奇（-16，266杆）加洞首洞胜李昊桐、索比约恩森与格雷泽曼。下站：英雄世界挑战赛（12月3-6日）。",
        "golf_pulse": "美巡赛：马尔科·彭奇海岛加洞封王锁定生涯首冠",
        "home_tonight": "周四体育台",
        "home_tonightBlurb": "NFL感恩节：周四熊（8-2）战雄狮（8-2）及酋长战比尔（9-1）。周三包装工对公羊未公布。欧冠皇马5-1埃因霍温。戴维斯杯捷克晋级，意大利对韩国仍在进行。周五卡塔尔站。",
        "home_plTitle": "阿森纳28分领跑英超；皇家马德里五战全胜15分独居欧冠榜首",
        "home_plBlurb": "英超第11轮后：阿森纳28，布莱顿22，曼城22，利物浦21。曼城1-1富勒姆（安德森57，穆尼斯16）。欧冠皇马5-1埃因霍温（姆巴佩64、84，贝林厄姆59），阿森纳1-1多特。",
        "home_f1Title": "卡塔尔站前瞻：维斯塔潘携拉斯维加斯胜利挺进卢赛尔，车手季军之争仅差3分",
        "home_f1Blurb": "安东内利（402分）与梅赛德斯（666分）已锁双冠，维斯塔潘维加斯夺冠升至304分；汉密尔顿（267分）仅领先拉塞尔与诺里斯（264分）3分。",
    },
    "ja": {
        "common_todayDesk": "木曜デスク：感謝祭NFL（ベアーズ8-2対ライオンズ8-2、チーフス8-2対ビルズ9-1）。欧州CL第5節火曜はRマドリード5-1。デビス杯ボローニャ。金曜カタールGP。",
        "common_todayNfl": "感謝祭：ベアーズ(8-2)対ライオンズ(8-2) 13:00 CBS、イーグルス対カウボーイズ 16:30 FOX、チーフス(8-2)対ビルズ(9-1) 20:20 NBC。",
        "common_todayTnf": "水曜Netflix：パッカーズ(6-4)対ラムズ(6-4)は未公開。木曜はフォード・フィールド決戦。",
        "football_tagline": "感謝祭NFL：水曜パッカーズ対ラムズの後、8勝2敗のライオンズとベアーズが木曜開幕。",
        "football_liveNow": "11/26木：ベアーズ(8-2)対ライオンズ(8-2)13:00 CBS、イーグルス対カウボーイズ16:30 FOX、チーフス対ビルズ(9-1)20:20 NBC。水曜パッカーズ対ラムズは未公開。第11週：テキサンズ26-3コルツ（HOU 4-6）。",
        "football_pulse": "NFL感謝祭：8勝2敗ライオンズとベアーズがNFC北首位懸け激突；チーフス対ビルズ9-1",
        "tennis_tagline": "デビス杯ボローニャ：チェコ2-0で通過；イタリア対韓国は未決着；アルカラスがトリノ無敗V。",
        "tennis_liveNow": "デビス杯：チェコ2-0カナダ；イタリア対韓国はムゼッティ6-0, 7-6後も進行中。木曜：英国対ドイツ10:00、オーストリア対スペイン17:00。トリノ：アルカラス6-2, 7-6(7)ズベレフ。",
        "tennis_pulse": "デビス杯：チェコが準決勝へ；木曜ボローニャは英国対ドイツで開幕",
        "f1_tagline": "次戦カタールGP（11/27-29）：ベガス制覇のフェルスタッペンがルサイル通常開催へ。スプリントなし。",
        "f1_liveNow": "ラスベガスGP結果：1.フェルスタッペン1:27:39.624、2.ノリス(+0.639s)、3.ピアストリ(17番手から)；ラッセル9位+13.192s。ランキング：アントネッリ402、フェルスタッペン304、ハミルトン267、ラッセル/ノリス264。金曜カタールFP1。",
        "f1_pulse": "F1：フェルスタッペンがベガス優勝、マクラーレンはレッドブルに9点差",
        "soccer_tagline": "欧州CL第5節：レアル・マドリード5-1 PSVで勝ち点15単独首位；水曜カードは未公開。",
        "soccer_liveNow": "CL火曜：Rマドリード5-1 PSV（エムバペ64、84）、アーセナル1-1ドルトムント（ジョケレス10；バイヤー55）、マンC 2-2ナポリ。PL：アーセナル28、ブライトン22、シティ22、リヴァプール21。シティ1-1フラム（アンダーソン57；ムニス16）。",
        "soccer_pulse": "欧州CL：レアル・マドリードが勝ち点15単独首位；アーセナルはプレミア28で首位",
        "basketball_tagline": "NBA感謝祭前：マーベリックスがナゲッツを120-101撃破；セルティックス131得点。",
        "basketball_liveNow": "火曜NBA杯：マブス120-101ナゲッツ（フラッグ24/6/12）；セルティックス131-116ウィザーズ（テイタム41、ジョージ28；デイビス33/13）；ピストンズ104-86マジック（ジョー21）。水曜未公開。木曜全休。",
        "basketball_pulse": "NBAカップ：フラッグ24点12アシストとテイタム41点爆発後に感謝祭ブレイク突入",
        "golf_tagline": "マルコ・ペンジがシーアイランドの4人POを制しRSMクラシックでPGAツアー初優勝。",
        "golf_liveNow": "RSMクラシック（11/23）：ペンジ(-16, 266)が1ホール目で李昊桐、ソービョルンセンらを下す。次戦：ヒーローワールドチャレンジ（12/3-6）。",
        "golf_pulse": "PGAツアー：マルコ・ペンジがシーアイランド4人POを制し初の栄冠獲得",
        "home_tonight": "木曜デスク",
        "home_tonightBlurb": "感謝祭NFL：ベアーズ(8-2)対ライオンズ(8-2)とチーフス対ビルズ(9-1)。水曜パッカーズ対ラムズは未公開。CL：Rマドリード5-1 PSV。デビス杯：チェコ通過、イタリア対韓国は進行中。金曜カタールGP。",
        "home_plTitle": "アーセナルが勝ち点28でプレミア首位、レアル・マドリードが勝ち点15でCL単独首位",
        "home_plBlurb": "プレミア第11節：アーセナル28、ブライトン22、マンC 22、リヴァプール21。シティ1-1フラム（アンダーソン57、ムニス16）。CL：レアル5-1 PSV（エムバペ64、84、ベリンガム59）、アーセナル1-1ドルトムント。",
        "home_f1Title": "カタールGP展望：ラスベガス勝者フェルスタッペンがルサイルへ、3位争いは僅か3点差",
        "home_f1Blurb": "王者アントネッリ（402点）とメルセデス（666点）が決する中、フェルスタッペンは304点へ上昇。ハミルトン（267点）をラッセルとノリス（264点）が3点差で追う。",
    },
    "ko": {
        "common_todayDesk": "목요 데스크: NFL 추수감사절(베어스 8-2 vs 라이온스 8-2, 치프스 8-2 vs 빌스 9-1). UCL 5차전 화요일 레알 5-1 PSV. 데이비스컵 볼로냐. 금요일 카타르 GP.",
        "common_todayNfl": "추수감사절: 베어스(8-2) vs 라이온스(8-2) 13:00 CBS, 이글스 vs 카우보이스 16:30 FOX, 치프스(8-2) vs 빌스(9-1) 20:20 NBC.",
        "common_todayTnf": "수요일 넷플릭스: 패커스(6-4) vs 램스(6-4) 결과는 미공개. 목요일 포드 필드 개막.",
        "football_tagline": "추수감사절 NFL: 수요일 패커스-램스 뒤를 이어 8승 2패 동률 라이온스-베어스 목요일 첫 경기.",
        "football_liveNow": "11/26 목: 베어스(8-2) vs 라이온스(8-2) 13:00 CBS, 이글스-카우보이스 16:30 FOX, 치프스(8-2) vs 빌스(9-1) 20:20 NBC. 수 패커스-램스 미공개. 11주차: 텍산스 26-3 콜츠(HOU 4-6).",
        "football_pulse": "NFL 추수감사절: 8승 2패 라이온스-베어스 NFC 북부 1위 혈투; 치프스 vs 빌스 9-1 야간 빅매치",
        "tennis_tagline": "데이비스컵 볼로냐: 체코 2-0 통과; 이탈리아-한국은 아직 진행; 알카라스 토리노 무패 우승.",
        "tennis_liveNow": "볼로냐: 체코 2-0 캐나다; 이탈리아-한국은 무세티 6-0, 7-6 이후 진행 중. 목: 영국-독일 10:00, 오스트리아-스페인 17:00. 토리노: 알카라스 6-2, 7-6(7) 즈베레프.",
        "tennis_pulse": "데이비스컵: 체코 4강 진출; 목요일 볼로냐는 영국 대 독일로 개막",
        "f1_tagline": "카타르 GP(11/27-29): 베가스 우승 페르스타펜, 루사일 전통 주말 일정 돌입. 스프린트 없음.",
        "f1_liveNow": "베가스 결과: 1.페르스타펜 1:27:39.624, 2.노리스(+0.639초), 3.피아스트리(17번 출발); 러셀 9위 +13.192초. 순위: 안토넬리 402, 페르스타펜 304, 해밀턴 267, 러셀/노리스 264. 금 카타르 FP1.",
        "f1_pulse": "포뮬러 1: 페르스타펜 베가스 우승; 맥라렌 레드불 9점 차 맹추격",
        "soccer_tagline": "UCL 5차전: 레알 마드리드 5-1 PSV 완파로 승점 15 단독 선두; 수요일 일정은 미공개.",
        "soccer_liveNow": "UCL 화: 레알 5-1 PSV(음바페 64, 84), 아스널 1-1 도르트문트(죄케레시 10; 바이어 55), 맨시티 2-2 나폴리. PL: 아스널 28, 브라이튼 22, 시티 22, 리버풀 21. 시티 1-1 풀럼(앤더슨 57; 무니스 16).",
        "soccer_pulse": "챔피언스리그: 레알 마드리드 승점 15점 단독 선두; 아스널 PL 28점 선두",
        "basketball_tagline": "NBA 추수감사절 휴식 전: 댈러스, 덴버 120-101 완파; 보스턴 131-116 위저즈 제압.",
        "basketball_liveNow": "화 컵대회: 매버릭스 120-101 너기츠(플래그 24/6/12); 셀틱스 131-116 위저즈(테이텀 41, 조지 28; 데이비스 33/13); 피스톤스 104-86 매직(조 21). 수 미공개. 목 휴식.",
        "basketball_pulse": "에미레이츠 NBA 컵: 쿠퍼 플래그 24+12, 제이슨 테이텀 41점 맹활약 후 목요일 전체 휴식",
        "golf_tagline": "마르코 펜지, RSM 클래식 4인 연장 승부 끝 생애 첫 PGA 투어 우승 트로피 차지.",
        "golf_liveNow": "RSM 클래식(11/23): 펜지(-16, 266)가 1차 연장서 리하오퉁, 소르비욘센, 그레이저먼 제압. 다음 대회: 히어로 월드 챌린지(12/3-6).",
        "golf_pulse": "PGA 투어: 마르코 펜지, 시아일랜드 연장 첫 홀 버디로 생애 첫 투어 우승 달성",
        "home_tonight": "목요 데스크",
        "home_tonightBlurb": "추수감사절 NFL: 베어스(8-2) vs 라이온스(8-2)와 치프스-빌스(9-1). 패커스-램스 미공개. UCL: 레알 5-1 PSV. 데이비스컵: 체코 통과, 이탈리아-한국 진행 중. 금요일 카타르 GP.",
        "home_plTitle": "아스널 승점 28점 프리미어리그 선두; 레알 마드리드 15점으로 UCL 단독 1위",
        "home_plBlurb": "PL 11R: 아스널 28, 브라이튼 22, 맨시티 22, 리버풀 21. 맨시티 1-1 풀럼(앤더슨 57, 무니스 16). UCL: 레알 5-1 PSV(음바페 64, 84, 벨링엄 59), 아스널 1-1 도르트문트.",
        "home_f1Title": "카타르 GP 프리뷰: 라스베이거스 우승 페르스타펜 루사일 입성, 3위 경쟁은 단 3점 차",
        "home_f1Blurb": "안토넬리(402)와 메르세데스(666)가 양대 챔피언을 확정한 가운데 페르스타펜은 베가스 우승으로 304점에 도달했고 해밀턴(267)과 러셀, 노리스(264)는 3점 차다.",
    },
    "ar": {
        "common_todayDesk": "مكتب الخميس: عيد الشكر NFL (بيرز 8-2 ضد لايونز 8-2، تشيفز 8-2 ضد بيلز 9-1). دوري الابطال الثلاثاء: ريال مدريد 5-1. كاس ديفيز بولونيا. جائزة قطر الجمعة.",
        "common_todayNfl": "عيد الشكر: بيرز (8-2) ضد لايونز (8-2) 1:00 ظهرا CBS، ايغلز ضد كاوبويز 4:30 FOX، تشيفز (8-2) ضد بيلز (9-1) 8:20 NBC.",
        "common_todayTnf": "ليلة الاربعاء على نتفليكس: باكرز (6-4) ضد رامز (6-4) غير منشور. الخميس: بيرز ضد لايونز في فورد فيلد.",
        "football_tagline": "عيد الشكر NFL: لايونز وبيرز (8-2) يفتتحان الخميس بعد مواجهة باكرز ورامز على نتفليكس.",
        "football_liveNow": "الخميس 26 نوفمبر: بيرز (8-2) ضد لايونز (8-2) 1:00 CBS، ايغلز-كاوبويز 4:30 FOX، تشيفز-بيلز (9-1) 8:20 NBC. باكرز ورامز الاربعاء غير منشور. الاسبوع 11: تكسانز 26-3 كولتس (هيوستن 4-6).",
        "football_pulse": "عيد الشكر NFL: صراع 8-2 بين لايونز وبيرز على القمة وتشيفز يحل ضيفا على بيلز 9-1",
        "tennis_tagline": "كاس ديفيز بولونيا: التشيك يعبر 2-0؛ ايطاليا ضد كوريا ما زالت مفتوحة؛ الكاراز بطل تورينو.",
        "tennis_liveNow": "بولونيا: التشيك 2-0 كندا؛ ايطاليا-كوريا مفتوحة بعد موسيتي 6-0 و7-6(5) هونغ. الخميس: بريطانيا-المانيا 10:00 والنمسا-اسبانيا 17:00. تورينو: الكاراز 6-2، 7-6(7) زفيريف.",
        "tennis_pulse": "كاس ديفيز: التشيك الى نصف النهائي؛ بريطانيا ضد المانيا تفتح الخميس في بولونيا",
        "f1_tagline": "جائزة قطر الكبرى (27-29 نوفمبر): فيرستابن يحمل انتصار لاس فيغاس نحو لوسيل بالصيغة التقليدية بلا سبرنت.",
        "f1_liveNow": "لاس فيغاس: 1.فيرستابن 1:27:39.624، 2.نوريس +0.639ث، 3.بياستري من المركز 17؛ راسل تاسعا +13.192ث. السائقون: انتونيللي 402، فيرستابن 304، هاميلتون 267، راسل ونوريس 264. قطر الجمعة.",
        "f1_pulse": "فورمولا 1: فيرستابن يحسم فيغاس ومكلارين يلاحق ريد بول بفارق 9 نقاط",
        "soccer_tagline": "دوري الابطال الجولة 5: ريال مدريد يسحق ايندهوفن 5-1 وينفرد بـ15 نقطة؛ الاربعاء غير منشور.",
        "soccer_liveNow": "الثلاثاء: ريال مدريد 5-1 ايندهوفن (مبابي 64 و84)، ارسنال 1-1 دورتموند (جوكيريس 10؛ باير 55)، مانشستر سيتي 2-2 نابولي. الانجليزي: ارسنال 28، برايتون 22، سيتي 22، ليفربول 21. سيتي 1-1 فولهام (انديرسون 57؛ مونيز 16).",
        "soccer_pulse": "دوري الابطال: ريال مدريد ينفرد بـ15 نقطة بعد الخماسية وارسنال يتصدر الانجليزي بـ28",
        "basketball_tagline": "قبل عطلة عيد الشكر في NBA: دالاس يهزم دنفر 120-101 وبوسطن يتفوق على واشنطن 131-116.",
        "basketball_liveNow": "كاس الدوري الثلاثاء: مافريكس 120-101 ناغتس (فلاغ 24/6/12)؛ سلتيكس 131-116 ويزاردز (تايتوم 41، جورج 28؛ ديفيس 33/13)؛ بيستونز 104-86 ماجيك (جو 21). الاربعاء غير منشور. الخميس راحة.",
        "basketball_pulse": "كاس الامارات NBA: كوبر فلاغ وتايتوم (41 نقطة) يتالقان قبل استراحة الخميس",
        "golf_tagline": "ماركو بينجي يتوج بلقبه الاول في جولة PGA بعد تمايز رباعي في بطولة RSM كلاسيك.",
        "golf_liveNow": "بطولة RSM (23 نوفمبر): ماركو بينجي (-16، 266) يتفوق من الحفرة الاضافية الاولى على لي هاوتونغ وثوربيورنسن وغريزرمان. القادم: تحدي هيرو العالمي (3-6 ديسمبر).",
        "golf_pulse": "جولة PGA: بينجي يحسم التمايز الرباعي في سي آيلاند ويحقق اول لقب له في الجولة",
        "home_tonight": "مكتب الخميس",
        "home_tonightBlurb": "عيد الشكر NFL: بيرز (8-2) ضد لايونز (8-2) وتشيفز ضد بيلز (9-1). باكرز ورامز غير منشور. دوري الابطال: ريال مدريد 5-1 ايندهوفن. كاس ديفيز: التشيك يعبر وايطاليا-كوريا مفتوحة. جائزة قطر الجمعة.",
        "home_plTitle": "ارسنال يتصدر الدوري الانجليزي بـ28 نقطة؛ ريال مدريد منفرد بقمة دوري الابطال",
        "home_plBlurb": "الجولة 11: ارسنال 28، برايتون 22، مانشستر سيتي 22، ليفربول 21. سيتي 1-1 فولهام (انديرسون 57، مونيز 16). دوري الابطال: ريال 5-1 ايندهوفن (مبابي 64 و84، بيلينغهام 59).",
        "home_f1Title": "تقديم جائزة قطر: فيرستابن يصل لوسيل بفوز لاس فيغاس وسط صراع ثلاثي النقاط على الثالث",
        "home_f1Blurb": "انتونيللي (402) ومرسيدس (666) ضمنا اللقبين، فيما رفع فيرستابن رصيده الى 304 نقاط بعد لاس فيغاس ويفصل 3 نقاط فقط هاميلتون (267) عن راسل ونوريس (264).",
    },
}


def replace_in_block(block_text, updates_dict):
    def esc(val):
        return val.replace("\\", "\\\\").replace('"', '\\"')

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
        pattern = rf'({ts_k}:\s*)(?:"[^"\n]*"|\'[^\'\n]*\'|\n\s*(?:"[^"\n]*"|\'[^\'\n]*\'))'
        m = re.search(pattern, block_text)
        if not m:
            raise RuntimeError(f"Failed to match key {ts_k} in locale block")
        block_text = block_text[: m.start()] + f'{m.group(1)}"{val}"' + block_text[m.end() :]

    for sport in ["football", "tennis", "f1", "soccer", "basketball", "golf"]:
        for prop in ["tagline", "liveNow", "pulse"]:
            val = esc(updates_dict[f"{sport}_{prop}"])
            sp_pat = rf'({sport}:\s*\{{.*?{prop}:\s*)(?:"[^"\n]*"|\'[^\'\n]*\')'
            m = re.search(sp_pat, block_text, flags=re.DOTALL)
            if not m:
                raise RuntimeError(f"Failed to match {sport}.{prop} in locale block")
            block_text = block_text[: m.start()] + f'{m.group(1)}"{val}"' + block_text[m.end() :]
    return block_text


# German playground used unveröffentlicht which is fine; messages too. Check -- after write.

msg_ts_path = os.path.join(I18N, "messages.ts")
msg_ts = open(msg_ts_path, "r", encoding="utf-8").read()
split_marker = "export const fr: Messages = {"
en_part, fr_part = msg_ts.split(split_marker, 1)
en_part = replace_in_block(en_part, messages_updates["en"])
fr_part = replace_in_block(fr_part, messages_updates["fr"])
new_msg_ts = en_part + split_marker + fr_part
no_dashes(new_msg_ts, "messages.ts")
open(msg_ts_path, "w", encoding="utf-8").write(new_msg_ts)
print("messages.ts")

for loc in ["es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
    p = os.path.join(I18N, f"messages-{loc}.ts")
    txt = open(p, "r", encoding="utf-8").read()
    new_txt = replace_in_block(txt, messages_updates[loc])
    no_dashes(new_txt, f"messages-{loc}.ts")
    open(p, "w", encoding="utf-8").write(new_txt)
    print(f"messages-{loc}.ts")


def patch_story_block(txt, slug, replacements):
    start = txt.find(f'  "{slug}":')
    if start < 0:
        raise SystemExit(f"missing story {slug}")
    nxt = txt.find('\n  "', start + 10)
    if nxt < 0:
        raise SystemExit(f"no next story after {slug}")
    block = txt[start:nxt]
    for a, b in replacements:
        if a not in block:
            print(f"WARN missing in {slug}: {a[:60]}")
        else:
            block = block.replace(a, b)
    return txt[:start] + block + txt[nxt:]


stories_path = os.path.join(I18N, "stories.ts")
st = open(stories_path, "r", encoding="utf-8").read()

st = patch_story_block(
    st,
    "nfl-thanksgiving-lions-bears-thanksgiving-clash-week12-2026",
    [
        ("et un bilan parfait de 6-0 a domicile apres", "et toujours invaincus a Ford Field apres"),
        ("Detroit defiende un invicto de 6-0 en casa y seis victorias consecutivas", "Detroit defiende su invicto en Ford Field y seis victorias consecutivas"),
        ("und makelloser 6-0-Heimbilanz nach dem", "und unbesiegt im Ford Field nach dem"),
        ("und ein Verlauf netto di 6-0 in casa dopo", "und un percorso netto di 6-0 in casa dopo"),
        ("e un percorso netto di 6-0 in casa dopo il", "e restano imbattuti al Ford Field dopo il"),
        ("i bilansem 6-0 u siebie po zwyciestwie", "i bez porazki na Ford Field po zwyciestwie"),
        ("目前主场6胜0负且豪取六连胜", "目前主场保持不败且豪取六连胜"),
        ("今季ホーム6戦全勝で6連勝中", "今季ホーム無敗で6連勝中"),
        ("6연승과 홈 6전 전승을 달리고 있으며", "6연승과 홈 무패를 달리고 있으며"),
        ("وسجل مثالي على ارضه (6-0) بعد الفوز", "وسجل دون هزيمة على ارض فورد فيلد بعد الفوز"),
    ],
)

st = patch_story_block(
    st,
    "champions-league-real-madrid-rout-psv-5-1-mbappe-bellingham-2026",
    [
        ("un bijou de Jude Bellingham a la 60e ne fasse", "un bijou de Jude Bellingham a la 59e ne fasse"),
        ("a la 60e", "a la 59e"),
    ],
)

st = patch_story_block(
    st,
    "f1-qatar-gp-lusail-preview-verstappen-vegas-triumph-norris-battle-2026",
    [
        ("fort de son 75e succes avec un podium mondial ultra serre", "fort de Las Vegas avec un podium mondial ultra serre"),
        ("Apres 35 changements de leader a Las Vegas, la Formule 1 retrouve son format classique a Lusail.", "Apres un Grand Prix serre a Las Vegas, la Formule 1 retrouve son format classique a Lusail, sans sprint."),
        ("au terme de 35 changements en tete, il a signe sa 4e victoire de l'annee et 75e en carriere pour 0,639 seconde devant Lando Norris et Oscar Piastri parti 17e.", "il a signe sa 4e victoire de l'annee en 1:27:39.624, 0,639 seconde devant Lando Norris, Oscar Piastri parti 17e, et George Russell neuvieme apres un contact avec le mur."),
        ("tras su victoria 75 con el podio separado por tres puntos", "tras Las Vegas con el podio separado por tres puntos"),
        ("Tras 35 cambios de lider en Las Vegas, la Formula 1 retoma el formato tradicional en Losail del 27 al 29 de noviembre.", "Tras un Gran Premio apretado en Las Vegas, la Formula 1 retoma el formato tradicional en Lusail del 27 al 29 de noviembre, sin sprint."),
        ("impulsado por su 75.a victoria tras ganar por apenas 0,639 segundos a Lando Norris en un caotico Las Vegas con 35 adelantamientos en cabeza y doble podio de McLaren junto a Oscar Piastri desde el 17.o puesto.", "tras ganar por 0,639 segundos a Lando Norris en Las Vegas, con Oscar Piastri desde el 17.o puesto y George Russell noveno tras rozar el muro."),
        ("nach 75. Sieg nach Lusail waehrend drei Punkte Platz drei trennen", "nach Las Vegas nach Lusail waehrend drei Punkte Platz drei trennen"),
        ("Nach 35 Fuehrungswechseln auf dem Strip kehrt die Formel 1 in Katar zum gewohnten Drei-Trainings-Format zurueck.", "Nach einem engen Rennen auf dem Strip kehrt die Formel 1 in Katar zum gewohnten Drei-Trainings-Format ohne Sprint zurueck."),
        ("Max Verstappen feierte in Nevada nach 35 Fuehrungswechseln seinen 75. Grand-Prix-Triumph knapp 0,639 Sekunden vor Lando Norris und Oscar Piastri (von Startplatz 17), waehrend beide Mercedes spaet Pech hatten.", "Max Verstappen siegte in Nevada in 1:27:39.624, 0,639 Sekunden vor Lando Norris und Oscar Piastri (von Startplatz 17). George Russell wurde nach einer Mauerberuehrung Neunter."),
        ("forte del 75esimo successo nella volata per il podio", "forte del successo di Las Vegas nella volata per il podio"),
        ("Dopo i 35 sorpassi in testa a Las Vegas, la Formula 1 torna al weekend tradizionale in Qatar dal 27 al 29 novembre.", "Dopo un Gran Premio tirato a Las Vegas, la Formula 1 torna al weekend tradizionale in Qatar dal 27 al 29 novembre, senza sprint."),
        ("sulle ali del 75esimo trionfo in carriera conquistato in Nevada al termine di 35 cambi di leader, precedendo Lando Norris per 0,639 secondi e Oscar Piastri risalito dal 17esimo posto.", "sulle ali del trionfo in Nevada in 1:27:39.624, precedendo Lando Norris per 0,639 secondi e Oscar Piastri risalito dal 17esimo posto. George Russell chiude nono dopo un contatto col muro."),
        ("po 75. triumfie przy pasjonujacej walce o podium", "po triumfie w Las Vegas przy pasjonujacej walce o podium"),
        ("Po szalonym wyscigu z 35 zmianami lidera w Las Vegas F1 wraca do klasycznego formatu bez sprintu.", "Po ciasnym wyscigu w Las Vegas F1 wraca do klasycznego formatu bez sprintu."),
        ("Max Verstappen przyjezdza po 75. zwyciestwie w karierze wywalczonym w Nevadzie po 35 zmianach prowadzenia o zaledwie 0,639 sekundy przed Lando Norrisem oraz Oscarem Piastrim startujacym z 17. pola.", "Max Verstappen przyjezdza po zwyciestwie w Nevadzie (1:27:39.624) o 0,639 sekundy przed Lando Norrisem oraz Oscarem Piastrim z 17. pola. George Russell convalesced to ninth."),
        ("维斯塔潘挟75胜莅临卢赛尔", "维斯塔潘挟拉斯维加斯胜利莅临卢赛尔"),
        ("历经拉斯维加斯35次领跑交替的史诗对决后，F1卡塔尔周末回归常规赛制并于周五揭幕。", "拉斯维加斯激战后，F1卡塔尔周末回归常规赛制、不设冲刺赛，并于周五揭幕。"),
        ("红牛车手维斯塔潘刚刚在拉斯维加斯历经35次头名交替的激战，以0.639秒惊险击败诺里斯夺得生涯第75胜，迈凯伦车手皮亚斯特里则从第17位发车强势登上领奖台。", "红牛车手维斯塔潘在拉斯维加斯以1:27:39.624、0.639秒击败诺里斯夺冠，迈凯伦车手皮亚斯特里从第17位发车登上领奖台，拉塞尔擦墙后仍收第9。"),
        ("通算75勝のフェルスタッペンがルサイルへ", "ラスベガス勝者フェルスタッペンがルサイルへ"),
        ("35回の首位交代を演じたラスベガスの激闘を経て、第22戦カタールは伝統の通常フォーマットで開催。", "ラスベガスの接戦を経て、第22戦カタールはスプリントなしの伝統フォーマットで開催。"),
        ("前戦ラスベガスでは35回の首位交代劇の末にマックス・フェルスタッペンがランド・ノリスを0.639秒抑えてキャリア通算75勝目を飾り、17番手スタートのオスカー・ピアストリも3位表彰台へ駆け上がった。", "前戦ラスベガスではマックス・フェルスタッペンが1:27:39.624でランド・ノリスを0.639秒抑え、17番手スタートのオスカー・ピアストリが3位。ジョージ・ラッセルはウォール接触後に9位で完走した。"),
        ("통산 75승 페르스타펜 루사일 입성", "라스베이거스 우승 페르스타펜 루사일 입성"),
        ("라스베이거스 35회 선두 교대 혈투를 뒤로하고 카타르 대회가 스핀트 없는 전통 주말 일정으로 돌아온다.", "라스베이거스 접전을 뒤로하고 카타르 대회가 스프린트 없는 전통 주말 일정으로 돌아온다."),
        ("막스 페르스타펜은 지난 라스베이거스 야간 레이스에서 무려 35차례 선두가 바뀐 격전 끝에 랜도 노리스를 0.639초 차로 따돌리고 커리어 75승을 거뒀으며, 오스카 피아스트리도 17그리드에서 포디움에 올랐다.", "막스 페르스타펜은 라스베이거스를 1:27:39.624, 0.639초 차로 랜도 노리스를 제치고 우승했고 오스카 피아스트리는 17그리드에서 포디움에 올랐으며 조지 러셀은 벽 접촉 후 9위로 들어왔다."),
        ("فيرستابن يصل الى لوسيل بفوزه الـ75 وصراع المركز الثالث بفارق 3 نقاط", "فيرستابن يصل الى لوسيل بفوز لاس فيغاس وصراع المركز الثالث بفارق 3 نقاط"),
        ("بعد 35 تغييرا للصدارة في لاس فيغاس، تعود الفورمولا 1 الى الصيغة التقليدية في حلبة لوسيل.", "بعد سباق متقارب في لاس فيغاس، تعود الفورمولا 1 الى الصيغة التقليدية بلا سبرنت في حلبة لوسيل."),
        ("يدخل ماكس فيرستابن السباق منتشيا بانتصاره الـ75 في مسيرته بعدما حسم سباق فيغاس بفارق 0.639 ثانية امام لاندو نوريس رغم 35 تبديلا للصدارة، مع صعود أوسكار بياستري ثالثا من المركز 17.", "يدخل ماكس فيرستابن السباق منتشيا بفوز فيغاس في 1:27:39.624 بفارق 0.639 ثانية امام لاندو نوريس، مع صعود أوسكار بياستري ثالثا من المركز 17 وجورج راسل تاسعا بعد ملامسة الجدار."),
    ],
)

# fix accidental English leftover in Polish F1 body
st = st.replace(
    "George Russell convalesced to ninth.",
    "George Russell finiszowal dziewiaty po kontakcie ze sciana.",
)

st = patch_story_block(
    st,
    "davis-cup-finals-bologna-italy-musetti-alcaraz-turin-glory-2026",
    [
        ("L'Italie mene face a la Coree du Sud apres le triomphe d'Alcaraz a Turin", "La Tchequie se qualifie, l'Italie et la Coree restent ouvertes apres le triomphe d'Alcaraz a Turin"),
        ("L'Italie s'offre un depart 1-0 en quarts de finale a Bologne apres la semaine parfaite de Carlos Alcaraz a Turin (6-2, 7-6 face a Zverev).", "La Tchequie balaye le Canada 2-0. Lorenzo Musetti bat Seongchan Hong 6-0, 7-6(5) ; la rencontre Italie-Coree reste ouverte. Jeudi : Grande-Bretagne - Allemagne."),
        ("Desormais place aux nations a Bologne : apres la qualification de la Tchequie face au Canada (2-0), Lorenzo Musetti a balaye Seongchan Hong 6-0, 7-6(5) pour placer l'Italie a 1-0 contre la Coree du Sud avant Grande-Bretagne - Allemagne et Autriche - Espagne jeudi.", "A Bologne, apres la qualification de la Tchequie face au Canada (2-0), Lorenzo Musetti a balaye Seongchan Hong 6-0, 7-6(5). La rencontre Italie-Coree reste ouverte. Jeudi : Grande-Bretagne - Allemagne a 10h00 puis Autriche - Espagne."),
        ("Italia toma ventaja sobre Corea del Sur tras la corona invicta de Alcaraz", "Chequia avanza e Italia-Corea sigue abierta tras la corona invicta de Alcaraz"),
        ("Los campeones defensores arrancan 1-0 en Bolonia dias despues de que Carlos Alcaraz levantara invicto su primer titulo de Maestro en Turin.", "Chequia vence 2-0 a Canada. Musetti gana el primer punto de Italia; Davis Cup sigue listando Italia-Corea en juego. Jueves: Gran Bretana vs Alemania."),
        ("y el miercoles Lorenzo Musetti arrollo 6-0, 7-6(5) a Seongchan Hong para dar el 1-0 a Italia antes de los cruces del jueves.", "y el miercoles Lorenzo Musetti arrollo 6-0, 7-6(5) a Seongchan Hong. El choque Italia-Corea sigue abierto antes de Gran Bretana-Alemania y Austria-Espana el jueves."),
        ("Italien fuehrt gegen Suedkorea nach Alcaraz' ungeschlagenem Turin-Triumph", "Tschechien ist durch, Italien gegen Korea noch offen nach Alcaraz' Turin-Triumph"),
        ("Titelverteidiger Italien geht im Viertelfinale von Bologna mit 1:0 in Fuehrung, kurz nachdem Carlos Alcaraz in Turin 5:0 den Gesamtsieg feierte.", "Tschechien schlaegt Kanada 2:0. Musetti gewinnt den ersten Punkt fuer Italien; Italien gegen Korea bleibt offen. Donnerstag: Grossbritannien gegen Deutschland."),
    ],
)

st = patch_story_block(
    st,
    "nba-thanksgiving-holiday-break-celtics-pistons-cup-showdowns-2026",
    [
        ("malgre les 33 points et 13 rebonds d'Anthony Davis et les 20 points, 11 rebonds et 7 passes d'AJ Dybantsa.", "malgre les 33 points et 13 rebonds d'Anthony Davis."),
        ("pour offrir aux Mavericks une victoire nette 120-101 face a Nikola Jokic (18/11), tandis que Detroit sans Cade Cunningham battait Orlando 104-86.", "pour offrir aux Mavericks une victoire nette 120-101, Jamal Murray inscrivant 20 points, tandis que Detroit sans Cade Cunningham battait Orlando 104-86."),
        ("para llevar a Dallas al 120-101 sobre los Nuggets de Nikola Jokic (18 puntos, 11 rebotes), mientras Detroit sin Cade Cunningham vencia 104-86 a Orlando con 21 puntos de Isaiah Joe.", "para llevar a Dallas al 120-101, con 20 puntos de Jamal Murray, mientras Detroit sin Cade Cunningham vencia 104-86 a Orlando con 21 puntos de Isaiah Joe."),
        ("beim 120:101-Auswaertssieg der Mavericks gegen Nikola Jokic (18/11), waehrend Detroit auch ohne den verletzten Cade Cunningham durch Isaiah Joes 21 Punkte 104:86 in Orlando gewann.", "beim 120:101-Auswaertssieg der Mavericks (Jamal Murray 20 Punkte), waehrend Detroit auch ohne den verletzten Cade Cunningham durch Isaiah Joes 21 Punkte 104:86 in Orlando gewann."),
        ("guidando i Mavericks al 120-101 sui Nuggets di Nikola Jokic, mentre i Pistons privi di Cade Cunningham hanno battuto Orlando 104-86 con 21 punti di Isaiah Joe.", "guidando i Mavericks al 120-101 (Jamal Murray 20 punti), mentre i Pistons privi di Cade Cunningham hanno battuto Orlando 104-86 con 21 punti di Isaiah Joe."),
        ("po 24 punktach i 12 asystach Coopera Flagga.", "po 24 punktach, 6 zbiorkach i 12 asystach Coopera Flagga (Murray 20)."),
    ],
)

st = patch_story_block(
    st,
    "nba-thanksgiving-holiday-break-celtics-pistons-cup-showdowns-2026",
    [
        ("prowadzac Dallas Mavericks do triumfu 120:101 nad ekipa Nikoli Jokicia, a osłabieni Pistons bez Cade'a Cunninghama wygrali w Orlando 104:86.", "prowadzac Dallas Mavericks do triumfu 120:101 (Jamal Murray 20 punktow), a oslabieni Pistons bez Cade'a Cunninghama wygrali w Orlando 104:86."),
        ("化解了安东尼·戴维斯空砍33分13篮板及阿杰·迪班萨20分11篮板7助攻的反扑。", "化解了安东尼·戴维斯空砍33分13篮板的反扑。"),
        ("助独行侠120比101轻取掘金；缺少康宁汉姆的活塞则凭借以赛亚·乔的21分在奥兰多104比86获胜。", "助独行侠120比101轻取掘金（穆雷20分）；缺少康宁汉姆的活塞则凭借以赛亚·乔的21分在奥兰多104比86获胜。"),
        ("제이슨 테이텀이 41점 8어시스트, 폴 조지가 3점슛 6개 포함 28점 9어시스트로 앤서니 데이비스(33점 13리바운드)와 AJ 디반사(20점 11리바운드)의 추격을 따돌렸다.", "제이슨 테이텀이 41점 8어시스트, 폴 조지가 28점 9어시스트로 앤서니 데이비스(33점 13리바운드)의 추격을 따돌렸다."),
    ],
)

no_dashes(st, "stories.ts")
open(stories_path, "w", encoding="utf-8").write(st)
print("stories.ts")
print("done")
