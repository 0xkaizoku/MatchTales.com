# Afternoon 26 Nov i18n, desk.json, playground, STORY_I18N.
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
I18N = os.path.join(ROOT, "frontend", "src", "i18n")
DESK = os.path.join(ROOT, "frontend", "src", "data", "desk.json")


def no_dashes(blob, label):
    if "\u2014" in blob:
        raise SystemExit(f"emdash in {label}")
    stripped = blob.replace("---", "")
    if "--" in stripped:
        raise SystemExit(f"double hyphen in {label}")


def replace_pairs(path, pairs):
    txt = open(path, encoding="utf-8").read()
    for old, new in pairs:
        if old not in txt:
            raise SystemExit(f"MISSING in {os.path.basename(path)}: {old[:80]}")
        txt = txt.replace(old, new, 1)
    no_dashes(txt, path)
    open(path, "w", encoding="utf-8").write(txt)
    print("updated", os.path.basename(path))


# desk.json
desk = json.load(open(DESK, encoding="utf-8"))
for g in desk["nflWeek1"]:
    if g.get("date") == "2026-11-25" and "Rams" in g.get("home", ""):
        g["note"] = "FINAL: Rams 26, Packers 13. Corum 32-184-1 TD, McManus 4 FGs. LAR 7-4 fifth straight, GB 6-5."
for t in desk["usOpenQF"]:
    if t.get("p1") == "Italy" and t.get("p2") == "South Korea":
        t["status"] = "Italy won 2-1 on 25 Nov (Musetti d Hong 6-0, 7-6(5); Kwon d Cobolli 3-6, 7-6(3), 7-6(5); Berrettini/Vavassori d Chung/Kwon 7-6(2), 7-6(11))"
    if t.get("p1") == "Great Britain" and t.get("p2") == "Germany":
        t["status"] = "Great Britain won 2-1 on 26 Nov (Norrie d Struff 6-3, 3-6, 6-2; Zverev d Fery 6-3, 6-2; Patten/Skupski d Krawietz/Puetz 6-2, 7-6(6)). Austria vs Spain 17:00 CET unpublished."
raw = json.dumps(desk, ensure_ascii=False, indent=2) + "\n"
no_dashes(raw, "desk.json")
open(DESK, "w", encoding="utf-8").write(raw)
print("desk.json")

# playground
pg_path = os.path.join(I18N, "playground.ts")
pg_txt = open(pg_path, encoding="utf-8").read()
pg_updates = {
    "en": {
        "pinFinal": "Davis Cup Bologna: Italy 2-1 Korea; GB 2-1 Germany; Czechia 2-0 Canada. Austria vs Spain 17:00 CET unpublished. Turin: Alcaraz d Zverev 6-2, 7-6(7).",
        "week1Closed": "Thanksgiving Football: Rams 26-13 Packers (LAR 7-4, GB 6-5). Bears (8-2) at Lions (8-2) 1:00 PM ET still to kick.",
        "week1Sub": "Rams fifth straight at SoFi. Thu unpublished: Bears-Lions 1:00 CBS, Eagles-Cowboys 4:30 FOX, Chiefs-Bills 8:20 NBC. Week 11: Texans 26-3 Colts (HOU 4-6).",
        "countdownTnf": "THANKSGIVING DAY UNPUBLISHED: Bears at Lions (1:00 PM ET CBS). Eagles at Cowboys (4:30 PM FOX). Chiefs at Bills (8:20 PM NBC).",
        "plFootnote": "UCL MD5: Real Madrid 5-1 PSV, Sabah 1-4 Barcelona, Club Brugge 0-3 Liverpool. Table: Madrid 15, PSG 13, Barca 12, Liverpool 12. PL: Arsenal 28, Brighton 22, City 22.",
    },
    "fr": {
        "pinFinal": "Coupe Davis Bologne : Italie 2-1 Coree ; GB 2-1 Allemagne ; Tchequie 2-0 Canada. Autriche-Espagne 17h00 inedit. Turin : Alcaraz bat Zverev 6-2, 7-6(7).",
        "week1Closed": "Thanksgiving NFL : Rams 26-13 Packers (7-4 vs 6-5). Bears (8-2) chez Lions (8-2) 13h00 ET encore a jouer.",
        "week1Sub": "Cinquieme succes d affilee des Rams. Jeudi inedit : Bears-Lions 13h00 CBS, Eagles-Cowboys 16h30 FOX, Chiefs-Bills 20h20 NBC. S11 : Texans 26-3 Colts (4-6).",
        "countdownTnf": "THANKSGIVING INEDIT : Bears chez Lions (13h00 ET CBS). Eagles chez Cowboys (16h30 FOX). Chiefs chez Bills (20h20 NBC).",
        "plFootnote": "LDC J5 : Real Madrid 5-1 PSV, Sabah 1-4 Barcelone, Club Brugge 0-3 Liverpool. Classement : Madrid 15, PSG 13, Barca 12, Liverpool 12. PL : Arsenal 28, Brighton 22, City 22.",
    },
    "es": {
        "pinFinal": "Copa Davis Bolonia: Italia 2-1 Corea; GB 2-1 Alemania; Chequia 2-0 Canada. Austria-Espana 17:00 inedito. Turin: Alcaraz 6-2, 7-6(7) Zverev.",
        "week1Closed": "Accion de Gracias NFL: Rams 26-13 Packers (7-4 vs 6-5). Bears (8-2) en Lions (8-2) 1:00 PM ET aun por jugar.",
        "week1Sub": "Quinta seguida de los Rams. Jueves inedito: Bears-Lions 1:00 CBS, Eagles-Cowboys 4:30 FOX, Chiefs-Bills 8:20 NBC. Semana 11: Texans 26-3 Colts (4-6).",
        "countdownTnf": "ACCION DE GRACIAS INEDITO: Bears en Lions (1:00 PM ET CBS). Eagles en Cowboys (4:30 FOX). Chiefs en Bills (8:20 NBC).",
        "plFootnote": "UCL J5: Real Madrid 5-1 PSV, Sabah 1-4 Barcelona, Club Brugge 0-3 Liverpool. Tabla: Madrid 15, PSG 13, Barca 12, Liverpool 12. PL: Arsenal 28, Brighton 22, City 22.",
    },
    "de": {
        "pinFinal": "Davis Cup Bologna: Italien 2:1 Korea; GB 2:1 Deutschland; Tschechien 2:0 Kanada. Oesterreich-Spanien 17:00 unveröffentlicht. Turin: Alcaraz 6:2, 7:6(7) Zverev.",
        "week1Closed": "Thanksgiving Football: Rams 26:13 Packers (7-4 vs 6-5). Bears (8-2) bei Lions (8-2) 1:00 PM ET noch offen.",
        "week1Sub": "Fuenfter Rams-Sieg in Folge. Do unveröffentlicht: Bears-Lions 1:00 CBS, Eagles-Cowboys 4:30 FOX, Chiefs-Bills 8:20 NBC. Woche 11: Texans 26:3 Colts (4-6).",
        "countdownTnf": "THANKSGIVING UNVEROEFFENTLICHT: Bears bei Lions (1:00 PM ET CBS). Eagles bei Cowboys (4:30 FOX). Chiefs bei Bills (8:20 NBC).",
        "plFootnote": "UCL 5. Sp.: Real Madrid 5:1 PSV, Sabah 1:4 Barcelona, Club Brugge 0:3 Liverpool. Tabelle: Madrid 15, PSG 13, Barca 12, Liverpool 12. PL: Arsenal 28, Brighton 22, City 22.",
    },
    "it": {
        "pinFinal": "Coppa Davis Bologna: Italia 2-1 Corea; GB 2-1 Germania; Ceca 2-0 Canada. Austria-Spagna 17:00 inedito. Torino: Alcaraz 6-2, 7-6(7) Zverev.",
        "week1Closed": "Thanksgiving NFL: Rams 26-13 Packers (7-4 vs 6-5). Bears (8-2) a Detroit (8-2) 19:00 ancora da giocare.",
        "week1Sub": "Quinta di fila dei Rams. Giovedi inedito: Bears-Lions, Eagles-Cowboys, Chiefs-Bills. Week 11: Texans 26-3 Colts (4-6).",
        "countdownTnf": "THANKSGIVING INEDITO: Bears a Detroit. Eagles a Dallas. Chiefs a Buffalo.",
        "plFootnote": "UCL 5a g.: Real Madrid 5-1 PSV, Sabah 1-4 Barcellona, Club Brugge 0-3 Liverpool. Classifica: Madrid 15, PSG 13, Barca 12, Liverpool 12. PL: Arsenal 28, Brighton 22, City 22.",
    },
    "pl": {
        "pinFinal": "Puchar Davisa Bolonia: Wlochy 2:1 Korea; GB 2:1 Niemcy; Czechy 2:0 Kanada. Austria-Hiszpania 17:00 nieopublikowane. Turyn: Alcaraz 6:2, 7:6(7) Zverev.",
        "week1Closed": "Thanksgiving NFL: Rams 26:13 Packers (7-4 vs 6-5). Bears (8-2) u Lions (8-2) 19:00 jeszcze nie rozegrane.",
        "week1Sub": "Piata z rzedu wygrana Rams. Czwartek nieopublikowany: Bears-Lions, Eagles-Cowboys, Chiefs-Bills. 11. tydzien: Texans 26:3 Colts (4-6).",
        "countdownTnf": "THANKSGIVING NIEOPUBLIKOWANE: Bears u Lions. Eagles u Cowboys. Chiefs u Bills.",
        "plFootnote": "LM 5. kol.: Real Madryt 5:1 PSV, Sabah 1:4 Barcelona, Club Brugge 0:3 Liverpool. Tabela: Madryt 15, PSG 13, Barca 12, Liverpool 12. PL: Arsenal 28, Brighton 22, City 22.",
    },
    "zh": {
        "pinFinal": "戴维斯杯博洛尼亚：意大利2-1韩国；英国2-1德国；捷克2-0加拿大。奥地利对西班牙17:00未公布。都灵：阿尔卡拉斯两盘击败兹维列夫。",
        "week1Closed": "NFL感恩节：公羊26-13包装工（7-4对6-5）。熊队（8-2）客战雄狮（8-2）美东13:00尚未开球。",
        "week1Sub": "公羊五连胜。周四未公布：熊-雄狮、老鹰-牛仔、酋长-比尔。第11周：德州人26-3小马（4-6）。",
        "countdownTnf": "感恩节未开赛：熊队战雄狮（13:00 CBS）。老鹰战牛仔（16:30 FOX）。酋长战比尔（20:20 NBC）。",
        "plFootnote": "欧冠第5轮：皇马5-1埃因霍温，萨巴赫1-4巴萨，布鲁日0-3利物浦。积分：皇马15，巴黎13，巴萨12，利物浦12。英超：阿森纳28，布莱顿22，曼城22。",
    },
    "ja": {
        "pinFinal": "デビスカップ・ボローニャ：イタリア2-1韓国、英国2-1ドイツ、チェコ2-0カナダ。オーストリア対スペイン17:00は未公開。トリノ：アルカラス全勝V。",
        "week1Closed": "感謝祭NFL：ラムズ26-13パッカーズ（7-4対6-5）。ベアーズ(8-2)対ライオンズ(8-2)13:00は未キックオフ。",
        "week1Sub": "ラムズ5連勝。木曜未公開：ベアーズ対ライオンズ、イーグルス対カウボーイズ、チーフス対ビルズ。第11週：テキサンズ26-3コルツ（4-6）。",
        "countdownTnf": "感謝祭は未公開：ベアーズ対ライオンズ(13:00 CBS)。イーグルス対カウボーイズ(16:30 FOX)。チーフス対ビルズ(20:20 NBC)。",
        "plFootnote": "CL第5節：Rマドリード5-1 PSV、サバフ1-4バルセロナ、ブルージュ0-3リヴァプール。順位：Madrid 15、PSG 13、Barca 12、Liverpool 12。PL：アーセナル28、ブライトン22、マンC 22。",
    },
    "ko": {
        "pinFinal": "데이비스 컵 볼로냐: 이탈리아 2-1 한국, 영국 2-1 독일, 체코 2-0 캐나다. 오스트리아-스페인 17:00 미공개. 토리노: 알카라스 무패 우승.",
        "week1Closed": "추수감사절 NFL: 램스 26-13 패커스(7-4 vs 6-5). 베어스(8-2) vs 라이온스(8-2) 13:00 아직 미킥오프.",
        "week1Sub": "램스 5연승. 목요일 미공개: 베어스-라이온스, 이글스-카우보이스, 치프스-빌스. 11주차: 텍산스 26-3 콜츠(4-6).",
        "countdownTnf": "추수감사절 미공개: 베어스 vs 라이온스(13:00 CBS). 이글스 vs 카우보이스(16:30 FOX). 치프스 vs 빌스(20:20 NBC).",
        "plFootnote": "UCL 5차전: 레알 5-1 PSV, 사바흐 1-4 바르사, 브뤼헤 0-3 리버풀. 순위: 마드리드 15, PSG 13, 바르사 12, 리버풀 12. PL: 아스널 28, 브라이튼 22, 맨시티 22.",
    },
    "ar": {
        "pinFinal": "كاس ديفيز بولونيا: ايطاليا 2-1 كوريا؛ بريطانيا 2-1 المانيا؛ التشيك 2-0 كندا. النمسا ضد اسبانيا 17:00 غير منشور. تورينو: الكاراز بطلا.",
        "week1Closed": "عيد الشكر NFL: رامز 26-13 باكرز (7-4 مقابل 6-5). بيرز (8-2) ضد لايونز (8-2) 1:00 ظهرا لم يبدا بعد.",
        "week1Sub": "خامس فوز متتال للرامز. الخميس غير منشور: بيرز-لايونز، ايغلز-كاوبويز، تشيفز-بيلز. الاسبوع 11: تكسانز 26-3 كولتس (4-6).",
        "countdownTnf": "عيد الشكر غير منشور: بيرز ضد لايونز (1:00 CBS). ايغلز ضد كاوبويز (4:30 FOX). تشيفز ضد بيلز (8:20 NBC).",
        "plFootnote": "دوري الابطال ج5: ريال مدريد 5-1 ايندهوفن، ساباه 1-4 برشلونة، كلوب بروج 0-3 ليفربول. الترتيب: مدريد 15، باريس 13، برشا 12، ليفربول 12. الدوري الانجليزي: ارسنال 28.",
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

# messages EN (first sports block in messages.ts)
replace_pairs(os.path.join(I18N, "messages.ts"), [
    ('tagline: "Thanksgiving Football: 8-2 Bears at 8-2 Lions open Thursday tripleheader after Wed Packers-Rams on Netflix.",',
     'tagline: "Thanksgiving Football: Rams 26-13 Packers on Netflix; 8-2 Bears at 8-2 Lions still to kick at 1 PM ET.",'),
    ('liveNow: "Thu Nov 26: Bears (8-2) at Lions (8-2) 1 PM ET CBS, Eagles (3-7) at Cowboys (5-6) 4:30 PM FOX, Chiefs (8-2) at Bills (9-1) 8:20 PM NBC. Wed Netflix Packers-Rams unpublished. Week 11: Texans 26-3 Colts (HOU 4-6).",',
     'liveNow: "FINAL Wed: Rams 26, Packers 13 (Corum 32-184-1; LAR 7-4, GB 6-5). Thu unpublished: Bears (8-2) at Lions (8-2) 1 PM ET CBS, Eagles (3-7) at Cowboys (5-6) 4:30 FOX, Chiefs (8-2) at Bills (9-1) 8:20 NBC.",'),
    ('pulse: "NFL WEEK 12 THANKSGIVING: IDENTICAL 8-2 LIONS AND BEARS CLASH FOR NFC NORTH LEAD; CHIEFS VISIT 9-1 BILLS",',
     'pulse: "NFL WEEK 12: RAMS 26-13 PACKERS; 8-2 BEARS AT 8-2 LIONS OPEN THANKSGIVING TRIPLEHEADER",'),
    ('tagline: "Davis Cup Final 8 in Bologna: Czechia through 2-0; Italy vs Korea still open; Alcaraz crowned in Turin.",',
     'tagline: "Davis Cup Bologna: Italy 2-1 Korea and Great Britain 2-1 Germany; Austria vs Spain 17:00 CET unpublished.",'),
    ('liveNow: "Davis Cup Bologna: Czechia d Canada 2-0; Italy vs Korea open after Musetti d Hong 6-0, 7-6(5). Thu QFs: GB vs Germany 10:00 CET, Austria vs Spain 17:00 CET. Turin Final: Alcaraz d Zverev 6-2, 7-6(7).",',
     'liveNow: "QF complete: Czechia 2-0 Canada; Italy 2-1 Korea; GB 2-1 Germany. Austria vs Spain 17:00 CET unpublished. Fri: Italy vs Czechia 16:00 CET. Turin: Alcaraz d Zverev 6-2, 7-6(7).",'),
    ('pulse: "DAVIS CUP FINALS: CZECHIA INTO THE LAST FOUR; GREAT BRITAIN VS GERMANY OPENS THURSDAY IN BOLOGNA",',
     'pulse: "DAVIS CUP: GREAT BRITAIN AND ITALY JOIN CZECHIA IN THE LAST FOUR; AUSTRIA-SPAIN STILL TO PLAY",'),
    ('tagline: "Champions League MD5: Real Madrid storm past PSV 5-1 to sit alone on 15 points; Wednesday slate unpublished.",',
     'tagline: "Champions League MD5: Barcelona 4-1 at Sabah and Liverpool 3-0 at Brugge; Real Madrid still first on 15.",'),
    ('liveNow: "UCL Tue: Real Madrid 5-1 PSV (Mbappe 64, 84), Arsenal 1-1 Dortmund (Gyokeres 10; Beier 55), Man City 2-2 Napoli. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1-1 Fulham (Anderson 57; Muniz 16).",',
     'liveNow: "UCL Wed: Sabah 1-4 Barcelona (Gordon 31, 51); Club Brugge 0-3 Liverpool (Isak 13, Wirtz 79). Tue: Real Madrid 5-1 PSV (Bellingham 59). Table: Madrid 15, PSG 13, Barca 12, Liverpool 12. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",'),
    ('pulse: "CHAMPIONS LEAGUE MD5: REAL MADRID HIT 15 POINTS AT SUMMIT AFTER 5-1 PSV; ARSENAL LEAD PL ON 28",',
     'pulse: "CHAMPIONS LEAGUE MD5: BARCELONA 4-1 SABAH AND LIVERPOOL 3-0 BRUGGE; MADRID STILL FIRST ON 15",'),
    ('tagline: "Emirates NBA Cup before Thanksgiving rest: Mavericks beat Nuggets 120-101; Celtics drop 131 on Wizards.",',
     'tagline: "NBA Cup: Sixers 111-104 Heat as LeBron posts 25/10/12; league rests on Thanksgiving.",'),
    ('liveNow: "Tue Cup: Mavericks 120-101 Nuggets (Flagg 24/6/12); Celtics 131-116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104-86 Magic (Joe 21). Wed unpublished. Thu rest.",',
     'liveNow: "Wed Cup: 76ers 111-104 Heat (LeBron 25/10/12, Maxey 30; Giannis 32/14); Blazers 116-111 Spurs (Wemby 44/16). Tue: Mavs 120-101, Celtics 131-116, Pistons 104-86. Thu rest.",'),
    ('pulse: "EMIRATES NBA CUP: MAVS CRUISE BEHIND COOPER FLAGG AND TATUM SCORES 41 AS THE LEAGUE TAKES THANKSGIVING OFF",',
     'pulse: "NBA CUP: LEBRON FIRST SIXERS TRIPLE-DOUBLE BEATS HEAT 111-104 BEFORE THANKSGIVING REST",'),
    ('tonightBlurb: "Thanksgiving NFL: 8-2 Bears at 8-2 Lions open Thursday (1:00 PM ET CBS) and Chiefs at 9-1 Bills cap the night. Wed Packers-Rams unpublished. UCL MD5: Real Madrid 5-1 PSV. Davis Cup Bologna: Czechia through, Italy vs Korea still open. Qatar GP Friday.",',
     'tonightBlurb: "Thanksgiving NFL: Rams 26-13 Packers (LAR 7-4). Bears (8-2) at Lions (8-2) 1:00 PM ET CBS still to kick. UCL: Barca 4-1 Sabah, Liverpool 3-0 Brugge, Madrid 15 pts. Davis Cup: Italy 2-1 Korea, GB 2-1 Germany. Qatar GP Friday.",'),
    ('plTitle: "Arsenal lead Premier League on 28; Real Madrid hit 15 points atop Champions League",',
     'plTitle: "Arsenal lead Premier League on 28; Real Madrid 15, Barcelona 12 after UCL MD5",'),
    ('plBlurb: "PL after MW11: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1-1 Fulham (Anderson 57, Muniz 16). UCL Tuesday: Real Madrid 5-1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1-1 Dortmund.",',
     'plBlurb: "PL after MW11: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. UCL Wednesday: Sabah 1-4 Barcelona, Club Brugge 0-3 Liverpool. Tuesday: Real Madrid 5-1 PSV (Bellingham 59).",'),
    # FR
    ('tagline: "Thanksgiving NFL : Lions et Bears (8-2) ouvrent jeudi apres Packers-Rams mercredi sur Netflix.",',
     'tagline: "Thanksgiving NFL : Rams 26-13 Packers ; Lions et Bears (8-2) encore a jouer a 13h00 ET.",'),
    ('liveNow: "Jeudi 26 nov : Bears (8-2) chez Lions (8-2) 13h00 ET CBS, Eagles-Cowboys 16h30 FOX, Chiefs-Bills (9-1) 20h20 NBC. Packers-Rams mercredi inedit. S11 : Texans 26-3 Colts (HOU 4-6).",',
     'liveNow: "FINAL mercredi : Rams 26-13 Packers (LAR 7-4, GB 6-5). Jeudi inedit : Bears (8-2) chez Lions (8-2) 13h00 CBS, Eagles-Cowboys 16h30 FOX, Chiefs-Bills (9-1) 20h20 NBC.",'),
    ('pulse: "NFL THANKSGIVING : LIONS ET BEARS A 8-2 POUR LA TETE DE LA NFC NORD ; CHIEFS CHEZ BILLS 9-1 EN SOIREE",',
     'pulse: "NFL : RAMS 26-13 PACKERS ; BEARS ET LIONS A 8-2 OUVRENT LE TRIPLE-HEADER DE THANKSGIVING",'),
    ('tagline: "Coupe Davis a Bologne : la Tchequie qualifiee 2-0 ; Italie-Coree encore ouverte ; Alcaraz sacre a Turin.",',
     'tagline: "Coupe Davis Bologne : Italie 2-1 Coree et GB 2-1 Allemagne ; Autriche-Espagne 17h00 inedit.",'),
    ('liveNow: "Coupe Davis Bologne : Tchequie 2-0 Canada ; Italie-Coree ouverte apres Musetti 6-0, 7-6(5) Hong. Jeudi : GB-Allemagne 10h00, Autriche-Espagne 17h00. Turin : Alcaraz bat Zverev 6-2, 7-6(7).",',
     'liveNow: "QF : Tchequie 2-0 Canada ; Italie 2-1 Coree ; GB 2-1 Allemagne. Autriche-Espagne 17h00 inedit. Vendredi : Italie-Tchequie 16h00. Turin : Alcaraz 6-2, 7-6(7).",'),
    ('pulse: "COUPE DAVIS : LA TCHEQUIE EN DEMI ; GRANDE-BRETAGNE - ALLEMAGNE OUVRE LE JEUDI A BOLOGNE",',
     'pulse: "COUPE DAVIS : GB ET ITALIE REJOIGNENT LA TCHEQUIE EN DEMI ; AUTRICHE-ESPAGNE A JOUER",'),
    ('tagline: "Ligue des champions J5 : le Real Madrid ecrase le PSV 5-1 et reste seul a 15 points ; mercredi inedit.",',
     'tagline: "Ligue des champions J5 : Barcelone 4-1 a Sabah et Liverpool 3-0 a Bruges ; le Real toujours premier a 15.",'),
    ('liveNow: "LDC mardi : Real Madrid 5-1 PSV (Mbappe 64, 84), Arsenal 1-1 Dortmund (Gyokeres 10 ; Beier 55), Man City 2-2 Naples. PL : Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1-1 Fulham (Anderson 57 ; Muniz 16).",',
     'liveNow: "LDC mercredi : Sabah 1-4 Barcelone (Gordon 31, 51) ; Club Brugge 0-3 Liverpool (Isak 13, Wirtz 79). Mardi : Real 5-1 PSV (Bellingham 59). Tableau : Madrid 15, PSG 13, Barca 12, Liverpool 12. PL : Arsenal 28.",'),
    ('pulse: "LIGUE DES CHAMPIONS : REAL MADRID SEUL A 15 POINTS APRES LE 5-1 CONTRE LE PSV ; ARSENAL MENE LA PL A 28",',
     'pulse: "LIGUE DES CHAMPIONS : BARCELONE 4-1 SABAH ET LIVERPOOL 3-0 BRUGES ; MADRID TOUJOURS PREMIER A 15",'),
    ('tagline: "Avant la pause de Thanksgiving NBA : Dallas bat Denver 120-101 et Boston bat Washington 131-116.",',
     'tagline: "NBA Cup : Sixers 111-104 Heat, triple-double de LeBron 25/10/12 ; pause Thanksgiving jeudi.",'),
    ('liveNow: "NBA Cup mardi : Mavericks 120-101 Nuggets (Flagg 24/6/12) ; Celtics 131-116 Wizards (Tatum 41, George 28 ; Davis 33/13) ; Pistons 104-86 Magic (Joe 21). Mercredi inedit. Jeudi pause.",',
     'liveNow: "NBA Cup mercredi : 76ers 111-104 Heat (LeBron 25/10/12, Maxey 30) ; Blazers 116-111 Spurs (Wemby 44/16). Mardi : Mavs 120-101, Celtics 131-116, Pistons 104-86. Jeudi pause.",'),
    ('pulse: "EMIRATES NBA CUP : COOPER FLAGG ET TATUM (41 PTS) BRILLENT AVANT LA RELACHE DE THANKSGIVING",',
     'pulse: "NBA CUP : PREMIER TRIPLE-DOUBLE DE LEBRON CHEZ LES SIXERS, 111-104 CONTRE LE HEAT",'),
    ('tonightBlurb: "Thanksgiving NFL : Bears (8-2) chez Lions (8-2) puis Chiefs chez Bills (9-1). Packers-Rams mercredi inedit. LDC : Real Madrid 5-1 PSV. Coupe Davis : Tchequie qualifiee, Italie-Coree encore ouverte. GP du Qatar vendredi.",',
     'tonightBlurb: "Thanksgiving NFL : Rams 26-13 Packers. Bears (8-2) chez Lions (8-2) 13h00 encore a jouer. LDC : Barca 4-1 Sabah, Liverpool 3-0 Bruges. Coupe Davis : Italie 2-1 Coree, GB 2-1 Allemagne. GP Qatar vendredi.",'),
    ('plTitle: "Arsenal mene la Premier League avec 28 points ; le Real Madrid seul en tete de la C1",',
     'plTitle: "Arsenal mene la Premier League a 28 ; Real Madrid 15, Barcelone 12 apres la J5 de C1",'),
    ('plBlurb: "PL J11 : Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1-1 Fulham (Anderson 57, Muniz 16). LDC : Real Madrid 5-1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1-1 Dortmund.",',
     'plBlurb: "PL J11 : Arsenal 28, Brighton 22, Man City 22, Liverpool 21. LDC mercredi : Sabah 1-4 Barcelone, Club Brugge 0-3 Liverpool. Mardi : Real 5-1 PSV (Bellingham 59).",'),
])

replace_pairs(os.path.join(I18N, "messages-es.ts"), [
    ('tagline: "Accion de Gracias NFL: Lions y Bears (8-2) abren el jueves tras Packers-Rams en Netflix.",',
     'tagline: "Accion de Gracias NFL: Rams 26-13 Packers; Lions y Bears (8-2) aun por patear a la 1 PM ET.",'),
    ('liveNow: "Jueves 26 nov: Bears (8-2) en Lions (8-2) 1 PM ET CBS, Eagles-Cowboys 4:30 PM FOX, Chiefs (8-2) en Bills (9-1) 8:20 PM NBC. Packers-Rams miercoles inedito. Semana 11: Texans 26-3 Colts (HOU 4-6).",',
     'liveNow: "FINAL mie: Rams 26-13 Packers (LAR 7-4, GB 6-5). Jueves inedito: Bears (8-2) en Lions (8-2) 1 PM CBS, Eagles-Cowboys 4:30 FOX, Chiefs-Bills (9-1) 8:20 NBC.",'),
    ('pulse: "NFL THANKSGIVING: LIONS Y BEARS (8-2) SE JUEGAN LA NFC NORTE; CHIEFS VISITA A BILLS 9-1 EN ESTELAR",',
     'pulse: "NFL: RAMS 26-13 PACKERS; BEARS Y LIONS (8-2) ABREN EL TRIPLEHEADER DE THANKSGIVING",'),
    ('tagline: "Copa Davis Bolonia: Chequia pasa 2-0; Italia-Corea sigue abierta; Carlos Alcaraz campeon invicto en Turin.",',
     'tagline: "Copa Davis Bolonia: Italia 2-1 Corea y GB 2-1 Alemania; Austria-Espana 17:00 inedito.",'),
    ('liveNow: "Copa Davis Bolonia: Chequia 2-0 Canada; Italia-Corea abierta tras Musetti 6-0, 7-6(5) Hong. Jueves: GB-Alemania 10:00, Austria-Espana 17:00. Turin: Alcaraz d. Zverev 6-2, 7-6(7).",',
     'liveNow: "QF: Chequia 2-0 Canada; Italia 2-1 Corea; GB 2-1 Alemania. Austria-Espana 17:00 inedito. Viernes: Italia-Chequia 16:00. Turin: Alcaraz 6-2, 7-6(7).",'),
    ('pulse: "COPA DAVIS: CHEQUIA A SEMIS; GRAN BRETANA CONTRA ALEMANIA ABRE EL JUEVES EN BOLONIA",',
     'pulse: "COPA DAVIS: GB E ITALIA SE UNEN A CHEQUIA EN SEMIS; AUSTRIA-ESPANA AUN POR JUGAR",'),
    ('tagline: "Champions League J5: Real Madrid golea 5-1 al PSV y se queda solo con 15 puntos; miercoles inedito.",',
     'tagline: "Champions League J5: Barcelona 4-1 en Sabah y Liverpool 3-0 en Brujas; el Madrid sigue primero con 15.",'),
    ('liveNow: "UCL martes: Real Madrid 5-1 PSV (Mbappe 64, 84), Arsenal 1-1 Dortmund (Gyokeres 10; Beier 55), Man City 2-2 Napoles. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1-1 Fulham (Anderson 57; Muniz 16).",',
     'liveNow: "UCL mie: Sabah 1-4 Barcelona (Gordon 31, 51); Club Brugge 0-3 Liverpool (Isak 13, Wirtz 79). Mar: Real 5-1 PSV (Bellingham 59). Tabla: Madrid 15, PSG 13, Barca 12, Liverpool 12. PL: Arsenal 28.",'),
    ('pulse: "CHAMPIONS LEAGUE: REAL MADRID PLENO DE 15 PUNTOS TRAS EL 5-1 AL PSV; ARSENAL LIDER DE LA PL CON 28",',
     'pulse: "CHAMPIONS LEAGUE: BARCELONA 4-1 SABAH Y LIVERPOOL 3-0 BRUJAS; MADRID SIGUE PRIMERO CON 15",'),
    ('tagline: "Antes del paron de Accion de Gracias: Dallas vence 120-101 a Denver y Boston 131-116 a Washington.",',
     'tagline: "NBA Cup: Sixers 111-104 Heat con triple-doble de LeBron 25/10/12; descanso el jueves.",'),
    ('liveNow: "NBA Cup martes: Mavericks 120-101 Nuggets (Flagg 24/6/12); Celtics 131-116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104-86 Magic (Joe 21). Miercoles inedito. Jueves descanso.",',
     'liveNow: "NBA Cup mie: 76ers 111-104 Heat (LeBron 25/10/12, Maxey 30); Blazers 116-111 Spurs (Wemby 44/16). Mar: Mavs 120-101, Celtics 131-116, Pistons 104-86. Jueves descanso.",'),
    ('pulse: "EMIRATES NBA CUP: COOPER FLAGG Y JAYSON TATUM (41 PTS) BRILLAN ANTES DE LA PAUSA DEL JUEVES",',
     'pulse: "NBA CUP: PRIMER TRIPLE-DOBLE DE LEBRON CON LOS SIXERS, 111-104 ANTE EL HEAT",'),
    ('tonightBlurb: "Thanksgiving NFL: Bears (8-2) en Lions (8-2) y Chiefs en Bills (9-1). Packers-Rams del miercoles inedito. UCL: Real Madrid 5-1 PSV. Copa Davis: Chequia clasificada, Italia-Corea abierta. GP de Catar el viernes.",',
     'tonightBlurb: "Thanksgiving NFL: Rams 26-13 Packers. Bears (8-2) en Lions (8-2) 1:00 PM aun por jugar. UCL: Barca 4-1 Sabah, Liverpool 3-0 Brujas. Copa Davis: Italia 2-1 Corea, GB 2-1 Alemania. GP de Catar el viernes.",'),
    ('plBlurb: "PL tras J11: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1-1 Fulham (Anderson 57, Muniz 16). UCL: Real Madrid 5-1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1-1 Dortmund.",',
     'plBlurb: "PL tras J11: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. UCL miercoles: Sabah 1-4 Barcelona, Club Brugge 0-3 Liverpool. Martes: Real 5-1 PSV (Bellingham 59).",'),
])

replace_pairs(os.path.join(I18N, "messages-de.ts"), [
    ('tagline: "Thanksgiving Football: 8-2 Lions gegen 8-2 Bears eroeffnen Donnerstag nach Packers-Rams.",',
     'tagline: "Thanksgiving Football: Rams 26:13 Packers; Lions und Bears (8-2) stossen um 13:00 ET noch an.",'),
    ('liveNow: "Do 26. Nov.: Bears (8-2) bei Lions (8-2) 1 PM ET CBS, Eagles bei Cowboys 4:30 PM FOX, Chiefs bei Bills (9-1) 8:20 PM NBC. Packers-Rams Mi unveröffentlicht. Woche 11: Texans 26:3 Colts (HOU 4-6).",',
     'liveNow: "FINAL Mi: Rams 26:13 Packers (LAR 7-4, GB 6-5). Do unveröffentlicht: Bears (8-2) bei Lions (8-2) 1 PM CBS, Eagles-Cowboys 4:30 FOX, Chiefs-Bills (9-1) 8:20 NBC.",'),
    ('pulse: "NFL THANKSGIVING: LIONS UND BEARS (8-2) UM NFC NORTH; CHIEFS BEI BILLS 9-1 IM TOPSPIEL",',
     'pulse: "NFL: RAMS 26:13 PACKERS; BEARS UND LIONS (8-2) EROEFFNEN DAS THANKSGIVING-TRIPLEHEADER",'),
    ('tagline: "Davis Cup Final 8 Bologna: Tschechien weiter 2:0; Italien gegen Korea noch offen; Alcaraz Turin-Champion.",',
     'tagline: "Davis Cup Bologna: Italien 2:1 Korea und GB 2:1 Deutschland; Oesterreich-Spanien 17:00 unveröffentlicht.",'),
    ('liveNow: "Davis Cup Bologna: Tschechien 2:0 Kanada; Italien-Korea offen nach Musetti 6:0, 7:6(5) Hong. Do: GB-Deutschland 10:00, Oesterreich-Spanien 17:00. Turin: Alcaraz 6:2, 7:6(7) Zverev.",',
     'liveNow: "VF: Tschechien 2:0 Kanada; Italien 2:1 Korea; GB 2:1 Deutschland. Oesterreich-Spanien 17:00 unveröffentlicht. Fr: Italien-Tschechien 16:00. Turin: Alcaraz 6:2, 7:6(7).",'),
    ('pulse: "DAVIS CUP: TSCHECHIEN IM HALBFINALE; GROSSBRITANNIEN GEGEN DEUTSCHLAND EROEFFNET DONNERSTAG IN BOLOGNA",',
     'pulse: "DAVIS CUP: GB UND ITALIEN STOSSEN ZU TSCHECHIEN INS HALBFINALE; OESTERREICH-SPANIEN OFFEN",'),
    ('tagline: "Champions League 5. Sp.: Real Madrid schlaegt PSV 5:1 und bleibt allein mit 15 Punkten; Mittwoch unveröffentlicht.",',
     'tagline: "Champions League 5. Sp.: Barcelona 4:1 in Sabah und Liverpool 3:0 in Bruegge; Real weiter Erster mit 15.",'),
    ('liveNow: "UCL Di: Real Madrid 5:1 PSV (Mbappe 64, 84), Arsenal 1:1 Dortmund (Gyokeres 10; Beier 55), Man City 2:2 Napoli. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1:1 Fulham (Anderson 57; Muniz 16).",',
     'liveNow: "UCL Mi: Sabah 1:4 Barcelona (Gordon 31, 51); Club Brugge 0:3 Liverpool (Isak 13, Wirtz 79). Di: Real 5:1 PSV (Bellingham 59). Tabelle: Madrid 15, PSG 13, Barca 12, Liverpool 12. PL: Arsenal 28.",'),
    ('pulse: "CHAMPIONS LEAGUE: REAL MADRID MIT 15 PUNKTEN GANZ OBEN NACH 5:1 GEGEN PSV; ARSENAL FUEHRT DIE PL MIT 28",',
     'pulse: "CHAMPIONS LEAGUE: BARCELONA 4:1 SABAH UND LIVERPOOL 3:0 BRUEGGE; REAL WEITER ERSTER MIT 15",'),
    ('tagline: "NBA vor Thanksgiving-Pause: Dallas bezwingt Denver 120:101; Boston schlaegt Wizards 131:116.",',
     'tagline: "NBA Cup: Sixers 111:104 Heat, LeBron mit 25/10/12; Thanksgiving-Pause am Donnerstag.",'),
    ('liveNow: "NBA Cup Di: Mavericks 120:101 Nuggets (Flagg 24/6/12); Celtics 131:116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104:86 Magic (Joe 21). Mi unveröffentlicht. Do spielfrei.",',
     'liveNow: "NBA Cup Mi: 76ers 111:104 Heat (LeBron 25/10/12, Maxey 30); Blazers 116:111 Spurs (Wemby 44/16). Di: Mavs 120:101, Celtics 131:116, Pistons 104:86. Do spielfrei.",'),
    ('pulse: "EMIRATES NBA CUP: COOPER FLAGG UND TATUM (41 PKT) GLANZEN VOR DER THANKSGIVING-PAUSE",',
     'pulse: "NBA CUP: ERSTES SIXERS-TRIPLE-DOUBLE VON LEBRON, 111:104 GEGEN DIE HEAT",'),
    ('tonightBlurb: "Thanksgiving NFL: Bears (8-2) bei Lions (8-2) und Chiefs bei Bills (9-1). Packers-Rams Mittwoch unveröffentlicht. UCL: Real Madrid 5:1 PSV. Davis Cup: Tschechien weiter, Italien-Korea offen. Katar GP Freitag.",',
     'tonightBlurb: "Thanksgiving NFL: Rams 26:13 Packers. Bears (8-2) bei Lions (8-2) 13:00 noch offen. UCL: Barca 4:1 Sabah, Liverpool 3:0 Bruegge. Davis Cup: Italien 2:1 Korea, GB 2:1 Deutschland. Katar GP Freitag.",'),
    ('plBlurb: "PL nach 11. Sp.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1:1 Fulham (Anderson 57, Muniz 16). UCL: Real 5:1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1:1 Dortmund.",',
     'plBlurb: "PL nach 11. Sp.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. UCL Mi: Sabah 1:4 Barcelona, Club Brugge 0:3 Liverpool. Di: Real 5:1 PSV (Bellingham 59).",'),
])

replace_pairs(os.path.join(I18N, "messages-it.ts"), [
    ('tagline: "Thanksgiving NFL: Lions e Bears (8-2) inaugurano il giovedi dopo Packers-Rams su Netflix.",',
     'tagline: "Thanksgiving NFL: Rams 26-13 Packers; Lions e Bears (8-2) ancora da giocare alle 19:00.",'),
    ('liveNow: "Giovedi 26 nov: Bears (8-2) a Detroit (8-2) 19:00, Eagles-Cowboys 22:30, Chiefs-Bills (9-1) 02:20. Packers-Rams mercoledi inedito. Week 11: Texans 26-3 Colts (HOU 4-6).",',
     'liveNow: "FINAL mer: Rams 26-13 Packers (LAR 7-4, GB 6-5). Gio inedito: Bears (8-2) a Detroit (8-2), Eagles-Cowboys, Chiefs-Bills (9-1).",'),
    ('pulse: "NFL THANKSGIVING: LIONS E BEARS (8-2) PER LA NFC NORTH; CHIEFS A BUFFALO 9-1 IN NOTTURNA",',
     'pulse: "NFL: RAMS 26-13 PACKERS; BEARS E LIONS (8-2) APRONO IL TRIPLEHEADER DEL RINGRAZIAMENTO",'),
    ('tagline: "Coppa Davis Bologna: Rep. Ceca avanti 2-0; Italia-Corea ancora aperta; Alcaraz campione imbattuto a Torino.",',
     'tagline: "Coppa Davis Bologna: Italia 2-1 Corea e GB 2-1 Germania; Austria-Spagna 17:00 inedito.",'),
    ('liveNow: "Coppa Davis Bologna: Rep. Ceca 2-0 Canada; Italia-Corea aperta dopo Musetti 6-0, 7-6(5) Hong. Gio: GB-Germania 10:00, Austria-Spagna 17:00. Torino: Alcaraz 6-2, 7-6(7) Zverev.",',
     'liveNow: "QF: Ceca 2-0 Canada; Italia 2-1 Corea; GB 2-1 Germania. Austria-Spagna 17:00 inedito. Ven: Italia-Ceca 16:00. Torino: Alcaraz 6-2, 7-6(7).",'),
    ('pulse: "COPPA DAVIS: REPUBBLICA CECA IN SEMIFINALE; GRAN BRETAGNA-GERMANIA APRE IL GIOVEDI A BOLOGNA",',
     'pulse: "COPPA DAVIS: GB E ITALIA CON LA CECA IN SEMIFINALE; AUSTRIA-SPAGNA ANCORA DA GIOCARE",'),
    ('tagline: "Champions League 5a g.: Real Madrid 5-1 al PSV e resta solo a quota 15; mercoledi inedito.",',
     'tagline: "Champions League 5a g.: Barcellona 4-1 a Sabah e Liverpool 3-0 a Bruges; il Real resta primo a 15.",'),
    ('liveNow: "UCL mar: Real Madrid 5-1 PSV (Mbappe 64, 84), Arsenal 1-1 Dortmund (Gyokeres 10; Beier 55), Man City 2-2 Napoli. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1-1 Fulham (Anderson 57; Muniz 16).",',
     'liveNow: "UCL mer: Sabah 1-4 Barcellona (Gordon 31, 51); Club Brugge 0-3 Liverpool (Isak 13, Wirtz 79). Mar: Real 5-1 PSV (Bellingham 59). Classifica: Madrid 15, PSG 13, Barca 12, Liverpool 12. PL: Arsenal 28.",'),
    ('pulse: "CHAMPIONS LEAGUE: REAL MADRID SOLO A QUOTA 15 DOPO IL 5-1 AL PSV; ARSENAL GUIDA LA PL A 28",',
     'pulse: "CHAMPIONS LEAGUE: BARCELLONA 4-1 SABAH E LIVERPOOL 3-0 BRUGES; REAL ANCORA PRIMO A 15",'),
    ('tagline: "Prima della sosta del Ringraziamento NBA: Dallas espugna Denver 120-101; Boston 131-116 a Washington.",',
     'tagline: "NBA Cup: Sixers 111-104 Heat, triple-double di LeBron 25/10/12; sosta del giovedi.",'),
    ('liveNow: "NBA Cup mar: Mavericks 120-101 Nuggets (Flagg 24/6/12); Celtics 131-116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104-86 Magic (Joe 21). Mer inedito. Gio riposo.",',
     'liveNow: "NBA Cup mer: 76ers 111-104 Heat (LeBron 25/10/12, Maxey 30); Blazers 116-111 Spurs (Wemby 44/16). Mar: Mavs 120-101, Celtics 131-116, Pistons 104-86. Gio riposo.",'),
    ('pulse: "EMIRATES NBA CUP: COOPER FLAGG E JAYSON TATUM (41 PT) BRILLANO PRIMA DELLA SOSTA DI GIOVEDI",',
     'pulse: "NBA CUP: PRIMO TRIPLE-DOUBLE DI LEBRON CON I SIXERS, 111-104 SUL HEAT",'),
    ('tonightBlurb: "Thanksgiving NFL: Bears (8-2) a Detroit e Chiefs a Buffalo (9-1). Packers-Rams mercoledi inedito. UCL: Real Madrid 5-1 PSV. Coppa Davis: Ceca avanti, Italia-Corea aperta. GP Qatar venerdi.",',
     'tonightBlurb: "Thanksgiving NFL: Rams 26-13 Packers. Bears (8-2) a Detroit ancora da giocare. UCL: Barca 4-1 Sabah, Liverpool 3-0 Bruges. Coppa Davis: Italia 2-1 Corea, GB 2-1 Germania. GP Qatar venerdi.",'),
    ('plBlurb: "PL 11a g.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1-1 Fulham (Anderson 57, Muniz 16). UCL: Real 5-1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1-1 Dortmund.",',
     'plBlurb: "PL 11a g.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. UCL mer: Sabah 1-4 Barcellona, Club Brugge 0-3 Liverpool. Mar: Real 5-1 PSV (Bellingham 59).",'),
])

replace_pairs(os.path.join(I18N, "messages-pl.ts"), [
    ('tagline: "Thanksgiving NFL: Lions i Bears (8-2) otwieraja czwartek po Packers-Rams na Netflixie.",',
     'tagline: "Thanksgiving NFL: Rams 26:13 Packers; Lions i Bears (8-2) jeszcze przed pierwszym snapem.",'),
    ('liveNow: "Czw 26 list.: Bears (8-2) u Lions (8-2) 19:00, Eagles-Cowboys 22:30, Chiefs-Bills (9-1) 02:20. Packers-Rams sroda nieopublikowane. Tydzien 11: Texans 26:3 Colts (HOU 4-6).",',
     'liveNow: "FINAL sr: Rams 26:13 Packers (LAR 7-4, GB 6-5). Czw nieopublikowane: Bears (8-2) u Lions (8-2), Eagles-Cowboys, Chiefs-Bills (9-1).",'),
    ('pulse: "NFL THANKSGIVING: LIONS I BEARS (8-2) O PRYM W NFC NORTH; CHIEFS U BILLS 9-1 W NOCNYM HICIE",',
     'pulse: "NFL: RAMS 26:13 PACKERS; BEARS I LIONS (8-2) OTWIERAJA THANKSGIVING TRIPLEHEADER",'),
    ('tagline: "Puchar Davisa w Bolonii: Czechy dalej 2:0; Wlochy-Korea nadal otwarte; Alcaraz mistrzem w Turynie.",',
     'tagline: "Puchar Davisa Bolonia: Wlochy 2:1 Korea i GB 2:1 Niemcy; Austria-Hiszpania 17:00 nieopublikowane.",'),
    ('liveNow: "Bolonia: Czechy 2:0 Kanada; Wlochy-Korea otwarte po Musettim 6:0, 7:6(5) Hong. Czw: GB-Niemcy 10:00, Austria-Hiszpania 17:00. Turyn: Alcaraz 6:2, 7:6(7) Zverev.",',
     'liveNow: "CF: Czechy 2:0 Kanada; Wlochy 2:1 Korea; GB 2:1 Niemcy. Austria-Hiszpania 17:00 nieopublikowane. Pt: Wlochy-Czechy 16:00. Turyn: Alcaraz 6:2, 7:6(7).",'),
    ('pulse: "PUCHAR DAVISA: CZECHY W POLFINALE; WIELKA BRYTANIA KONTRA NIEMCY OTWIERA CZWARTEK W BOLONII",',
     'pulse: "PUCHAR DAVISA: GB I WLOCHY Z CZECHAMI W POLFINALE; AUSTRIA-HISZPANIA CZEKA",'),
    ('tagline: "Liga Mistrzow 5. kol.: Real Madryt rozbil PSV 5:1 i zostaje sam na 15 pkt; sroda nieopublikowana.",',
     'tagline: "Liga Mistrzow 5. kol.: Barcelona 4:1 w Sabah i Liverpool 3:0 w Brugii; Real nadal pierwszy z 15.",'),
    ('liveNow: "LM wt: Real Madryt 5:1 PSV (Mbappe 64, 84), Arsenal 1:1 Dortmund (Gyokeres 10; Beier 55), Man City 2:2 Napoli. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1:1 Fulham (Anderson 57; Muniz 16).",',
     'liveNow: "LM sr: Sabah 1:4 Barcelona (Gordon 31, 51); Club Brugge 0:3 Liverpool (Isak 13, Wirtz 79). Wt: Real 5:1 PSV (Bellingham 59). Tabela: Madryt 15, PSG 13, Barca 12, Liverpool 12. PL: Arsenal 28.",'),
    ('pulse: "LIGA MISTRZOW: REAL MADRYT Z KOMPLETEM 15 PKT PO 5:1 Z PSV; ARSENAL LIDERE PL Z 28",',
     'pulse: "LIGA MISTRZOW: BARCELONA 4:1 SABAH I LIVERPOOL 3:0 BRUGIA; REAL NADAL PIERWSZY Z 15",'),
    ('tagline: "Przed czwartkowa pauza w NBA: Dallas ogralo Denver 120:101, a Boston rzucil 131 punktow Wizards.",',
     'tagline: "NBA Cup: Sixers 111:104 Heat, triple-double LeBrona 25/10/12; czwartkowa pauza.",'),
    ('liveNow: "NBA Cup wt: Mavericks 120:101 Nuggets (Flagg 24/6/12); Celtics 131:116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104:86 Magic (Joe 21). Sr nieopublikowane. Czw wolne.",',
     'liveNow: "NBA Cup sr: 76ers 111:104 Heat (LeBron 25/10/12, Maxey 30); Blazers 116:111 Spurs (Wemby 44/16). Wt: Mavs 120:101, Celtics 131:116, Pistons 104:86. Czw wolne.",'),
    ('pulse: "EMIRATES NBA CUP: COOPER FLAGG I JAYSON TATUM (41 PKT) BLYSZCZA PRZED SWIATECZNA PAUZA",',
     'pulse: "NBA CUP: PIERWSZE TRIPLE-DOUBLE LEBRONA W SIXERS, 111:104 Z HEAT",'),
    ('tonightBlurb: "Thanksgiving NFL: Bears (8-2) u Lions (8-2) oraz Chiefs u Bills (9-1). Packers-Rams sroda nieopublikowane. LM: Real Madryt 5:1 PSV. Puchar Davisa: Czechy dalej, Wlochy-Korea otwarte. GP Kataru w piatek.",',
     'tonightBlurb: "Thanksgiving NFL: Rams 26:13 Packers. Bears (8-2) u Lions (8-2) jeszcze przed meczem. LM: Barca 4:1 Sabah, Liverpool 3:0 Brugia. Puchar Davisa: Wlochy 2:1 Korea, GB 2:1 Niemcy. GP Kataru w piatek.",'),
    ('plBlurb: "PL po 11. kol.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. City 1:1 Fulham (Anderson 57, Muniz 16). LM: Real 5:1 PSV (Mbappe 64, 84, Bellingham 59), Arsenal 1:1 Dortmund.",',
     'plBlurb: "PL po 11. kol.: Arsenal 28, Brighton 22, Man City 22, Liverpool 21. LM sr: Sabah 1:4 Barcelona, Club Brugge 0:3 Liverpool. Wt: Real 5:1 PSV (Bellingham 59).",'),
])

replace_pairs(os.path.join(I18N, "messages-zh.ts"), [
    ('tagline: "NFL感恩节：周三网飞大战后，同积8胜2负的雄狮与熊队周四揭幕。",',
     'tagline: "NFL感恩节：公羊26-13击败包装工；8胜2负熊队与雄狮13:00尚未开球。",'),
    ('liveNow: "周四11月26日：熊（8-2）战雄狮（8-2）13:00 CBS，老鹰战牛仔16:30 FOX，酋长（8-2）战比尔（9-1）20:20 NBC。周三包装工对公羊未公布。第11周：德州人26-3小马（休斯敦4-6）。",',
     'liveNow: "周三完场：公羊26-13包装工（7-4对6-5）。周四未开赛：熊（8-2）战雄狮（8-2）13:00 CBS，老鹰-牛仔16:30 FOX，酋长-比尔（9-1）20:20 NBC。",'),
    ('pulse: "NFL感恩节：8胜2负雄狮与熊队直面国北榜首之争；酋长压轴客战9胜1负比尔",',
     'pulse: "NFL：公羊26-13包装工；8胜2负熊队与雄狮揭幕感恩节三连战",'),
    ('tagline: "戴维斯杯博洛尼亚总决赛：捷克2-0晋级；意大利对韩国仍在进行；阿尔卡拉斯都灵封王。",',
     'tagline: "戴维斯杯博洛尼亚：意大利2-1韩国、英国2-1德国；奥地利对西班牙17:00未公布。",'),
    ('liveNow: "博洛尼亚：捷克2-0加拿大；意大利对韩国在穆塞蒂6-0、7-6胜洪性成后仍未完结。周四英德10:00、奥西17:00。都灵：阿尔卡拉斯胜兹维列夫。",',
     'liveNow: "四分之一决赛：捷克2-0加拿大；意大利2-1韩国；英国2-1德国。奥西17:00未公布。周五意大利对捷克16:00。都灵：阿尔卡拉斯6-2、7-6(7)。",'),
    ('pulse: "戴维斯杯：捷克杀入四强；周四博洛尼亚英国对德国揭幕",',
     'pulse: "戴维斯杯：英国与意大利携捷克晋级四强；奥西尚未开打",'),
    ('tagline: "欧冠第5轮：皇马5-1横扫埃因霍温独居15分；周三赛程未公布。",',
     'tagline: "欧冠第5轮：巴萨客场4-1萨巴赫、利物浦3-0布鲁日；皇马仍以15分领跑。",'),
    ('liveNow: "欧冠周二：皇马5-1埃因霍温（姆巴佩64、84），阿森纳1-1多特（哲凯雷什10；拜尔55），曼城2-2那不勒斯。英超：阿森纳28，布莱顿22，曼城22，利物浦21。曼城1-1富勒姆（安德森57；穆尼斯16）。",',
     'liveNow: "欧冠周三：萨巴赫1-4巴萨（戈登31、51）；布鲁日0-3利物浦（伊萨克13，维尔茨79）。周二皇马5-1埃因霍温（贝林厄姆59）。积分：皇马15，巴黎13，巴萨12，利物浦12。英超阿森纳28。",'),
    ('pulse: "欧冠第5轮：皇马15分独居榜首；阿森纳以28分领跑英超",',
     'pulse: "欧冠第5轮：巴萨4-1萨巴赫、利物浦3-0布鲁日；皇马仍以15分领跑",'),
    ('tagline: "NBA感恩节休战前夕：独行侠120-101胜掘金，凯尔特人131-116力克奇才。",',
     'tagline: "NBA杯：76人111-104热火，詹姆斯25+10+12三双；周四全联盟休战。",'),
    ('liveNow: "周二NBA杯：独行侠120-101掘金（弗拉格24/6/12）；绿军131-116奇才（塔图姆41，乔治28；戴维斯33/13）；活塞104-86魔术（乔21）。周三未公布。周四休战。",',
     'liveNow: "周三NBA杯：76人111-104热火（詹姆斯25/10/12，马克西30）；开拓者116-111马刺（文班44/16）。周二独行侠、绿军、活塞取胜。周四休战。",'),
    ('pulse: "NBA杯：库珀·弗拉格24+12与塔图姆狂轰41分点燃感恩节前夜",',
     'pulse: "NBA杯：詹姆斯76人首记三双，111-104击败热火后迎感恩节休战",'),
    ('tonightBlurb: "NFL感恩节：周四熊（8-2）战雄狮（8-2）及酋长战比尔（9-1）。周三包装工对公羊未公布。欧冠皇马5-1埃因霍温。戴维斯杯捷克晋级，意大利对韩国仍在进行。周五卡塔尔站。",',
     'tonightBlurb: "NFL感恩节：公羊26-13包装工。熊（8-2）战雄狮（8-2）13:00尚未开球。欧冠巴萨4-1萨巴赫、利物浦3-0布鲁日。戴维斯杯意大利2-1韩国、英国2-1德国。周五卡塔尔站。",'),
    ('plBlurb: "英超第11轮后：阿森纳28，布莱顿22，曼城22，利物浦21。曼城1-1富勒姆（安德森57，穆尼斯16）。欧冠皇马5-1埃因霍温（姆巴佩64、84，贝林厄姆59），阿森纳1-1多特。",',
     'plBlurb: "英超第11轮后：阿森纳28，布莱顿22，曼城22，利物浦21。欧冠周三萨巴赫1-4巴萨、布鲁日0-3利物浦。周二皇马5-1埃因霍温（贝林厄姆59）。",'),
])

replace_pairs(os.path.join(I18N, "messages-ja.ts"), [
    ('tagline: "感謝祭NFL：水曜パッカーズ対ラムズの後、8勝2敗のライオンズとベアーズが木曜開幕。",',
     'tagline: "感謝祭NFL：ラムズ26-13パッカーズ；8勝2敗ベアーズ対ライオンズは13:00未キックオフ。",'),
    ('liveNow: "11/26木：ベアーズ(8-2)対ライオンズ(8-2)13:00 CBS、イーグルス対カウボーイズ16:30 FOX、チーフス対ビルズ(9-1)20:20 NBC。水曜パッカーズ対ラムズは未公開。第11週：テキサンズ26-3コルツ（HOU 4-6）。",',
     'liveNow: "水曜終了：ラムズ26-13パッカーズ（7-4対6-5）。木曜未公開：ベアーズ(8-2)対ライオンズ(8-2)13:00 CBS、イーグルス対カウボーイズ16:30、チーフス対ビルズ(9-1)20:20。",'),
    ('pulse: "NFL感謝祭：8勝2敗ライオンズとベアーズがNFC北首位懸け激突；チーフス対ビルズ9-1",',
     'pulse: "NFL：ラムズ26-13パッカーズ；8勝2敗ベアーズ対ライオンズが感謝祭三重戦の幕開け",'),
    ('tagline: "デビス杯ボローニャ：チェコ2-0で通過；イタリア対韓国は未決着；アルカラスがトリノ無敗V。",',
     'tagline: "デビス杯ボローニャ：イタリア2-1韓国、英国2-1ドイツ；オーストリア対スペイン17:00は未公開。",'),
    ('liveNow: "デビス杯：チェコ2-0カナダ；イタリア対韓国はムゼッティ6-0, 7-6後も進行中。木曜：英国対ドイツ10:00、オーストリア対スペイン17:00。トリノ：アルカラス6-2, 7-6(7)ズベレフ。",',
     'liveNow: "QF：チェコ2-0カナダ、イタリア2-1韓国、英国2-1ドイツ。オーストリア対スペイン17:00未公開。金曜イタリア対チェコ16:00。トリノ：アルカラス6-2, 7-6(7)。",'),
    ('pulse: "デビス杯：チェコが準決勝へ；木曜ボローニャは英国対ドイツで開幕",',
     'pulse: "デビス杯：英国とイタリアがチェコと並び準決勝；オーストリア対スペインはこれから",'),
    ('tagline: "欧州CL第5節：レアル・マドリード5-1 PSVで勝ち点15単独首位；水曜カードは未公開。",',
     'tagline: "欧州CL第5節：バルセロナがサバフに4-1、リヴァプールがブルージュに3-0；レアルは15で首位。",'),
    ('liveNow: "CL火曜：Rマドリード5-1 PSV（エムバペ64、84）、アーセナル1-1ドルトムント（ジョケレス10；バイヤー55）、マンC 2-2ナポリ。PL：アーセナル28、ブライトン22、シティ22、リヴァプール21。シティ1-1フラム（アンダーソン57；ムニス16）。",',
     'liveNow: "CL水曜：サバフ1-4バルセロナ（ゴードン31、51）；ブルージュ0-3リヴァプール（イサク13、ヴィルツ79）。火曜レアル5-1 PSV（ベリンガム59）。順位：Madrid 15、PSG 13、Barca 12、Liverpool 12。PLアーセナル28。",'),
    ('pulse: "欧州CL：レアル・マドリードが勝ち点15単独首位；アーセナルはプレミア28で首位",',
     'pulse: "欧州CL：バルセロナ4-1サバフ、リヴァプール3-0ブルージュ；レアルは15で首位堅持",'),
    ('tagline: "NBA感謝祭前：マーベリックスがナゲッツを120-101撃破；セルティックス131得点。",',
     'tagline: "NBA杯：シクサーズ111-104ヒート、レブロン25/10/12；木曜は感謝祭休養。",'),
    ('liveNow: "火曜NBA杯：マブス120-101ナゲッツ（フラッグ24/6/12）；セルティックス131-116ウィザーズ（テイタム41、ジョージ28；デイビス33/13）；ピストンズ104-86マジック（ジョー21）。水曜未公開。木曜全休。",',
     'liveNow: "水曜NBA杯：76ers 111-104ヒート（レブロン25/10/12、マクシー30）；ブレイザーズ116-111スパーズ（ウェンバン44/16）。火曜マブス、セルティックス、ピストンズ勝利。木曜全休。",'),
    ('pulse: "NBAカップ：フラッグ24点12アシストとテイタム41点爆発後に感謝祭ブレイク突入",',
     'pulse: "NBAカップ：レブロンがシクサーズ初トリプルダブル、111-104でヒート撃破",'),
    ('tonightBlurb: "感謝祭NFL：ベアーズ(8-2)対ライオンズ(8-2)とチーフス対ビルズ(9-1)。水曜パッカーズ対ラムズは未公開。CL：Rマドリード5-1 PSV。デビス杯：チェコ通過、イタリア対韓国は進行中。金曜カタールGP。",',
     'tonightBlurb: "感謝祭NFL：ラムズ26-13パッカーズ。ベアーズ(8-2)対ライオンズ(8-2)は未キックオフ。CL：バルサ4-1サバフ、リヴァプール3-0ブルージュ。デビス杯：イタリア2-1韓国、英国2-1ドイツ。金曜カタールGP。",'),
    ('plBlurb: "プレミア第11節：アーセナル28、ブライトン22、マンC 22、リヴァプール21。シティ1-1フラム（アンダーソン57、ムニス16）。CL：レアル5-1 PSV（エムバペ64、84、ベリンガム59）、アーセナル1-1ドルトムント。",',
     'plBlurb: "プレミア第11節：アーセナル28、ブライトン22、マンC 22、リヴァプール21。CL水曜：サバフ1-4バルセロナ、ブルージュ0-3リヴァプール。火曜：レアル5-1 PSV（ベリンガム59）。",'),
])

replace_pairs(os.path.join(I18N, "messages-ko.ts"), [
    ('tagline: "추수감사절 NFL: 수요일 패커스-램스 뒤를 이어 8승 2패 동률 라이온스-베어스 목요일 첫 경기.",',
     'tagline: "추수감사절 NFL: 램스 26-13 패커스; 8승 2패 베어스-라이온스는 13:00 미킥오프.",'),
    ('liveNow: "11/26 목: 베어스(8-2) vs 라이온스(8-2) 13:00 CBS, 이글스-카우보이스 16:30 FOX, 치프스(8-2) vs 빌스(9-1) 20:20 NBC. 수 패커스-램스 미공개. 11주차: 텍산스 26-3 콜츠(HOU 4-6).",',
     'liveNow: "수 종료: 램스 26-13 패커스(7-4 vs 6-5). 목 미공개: 베어스(8-2) vs 라이온스(8-2) 13:00 CBS, 이글스-카우보이스 16:30, 치프스-빌스(9-1) 20:20.",'),
    ('pulse: "NFL 추수감사절: 8승 2패 라이온스-베어스 NFC 북부 1위 혈투; 치프스 vs 빌스 9-1 야간 빅매치",',
     'pulse: "NFL: 램스 26-13 패커스; 8승 2패 베어스-라이온스가 추수감사절 3연전 개막",'),
    ('tagline: "데이비스컵 볼로냐: 체코 2-0 통과; 이탈리아-한국은 아직 진행; 알카라스 토리노 무패 우승.",',
     'tagline: "데이비스컵 볼로냐: 이탈리아 2-1 한국, 영국 2-1 독일; 오스트리아-스페인 17:00 미공개.",'),
    ('liveNow: "볼로냐: 체코 2-0 캐나다; 이탈리아-한국은 무세티 6-0, 7-6 이후 진행 중. 목: 영국-독일 10:00, 오스트리아-스페인 17:00. 토리노: 알카라스 6-2, 7-6(7) 즈베레프.",',
     'liveNow: "8강: 체코 2-0 캐나다, 이탈리아 2-1 한국, 영국 2-1 독일. 오스트리아-스페인 17:00 미공개. 금: 이탈리아-체코 16:00. 토리노: 알카라스 6-2, 7-6(7).",'),
    ('pulse: "데이비스컵: 체코 4강 진출; 목요일 볼로냐는 영국 대 독일로 개막",',
     'pulse: "데이비스컵: 영국과 이탈리아가 체코와 함께 4강; 오스트리아-스페인은 대기",'),
    ('tagline: "UCL 5차전: 레알 마드리드 5-1 PSV 완파로 승점 15 단독 선두; 수요일 일정은 미공개.",',
     'tagline: "UCL 5차전: 바르사 사바흐 원정 4-1, 리버풀 브뤼헤 3-0; 레알은 15점으로 선두.",'),
    ('liveNow: "UCL 화: 레알 5-1 PSV(음바페 64, 84), 아스널 1-1 도르트문트(죄케레시 10; 바이어 55), 맨시티 2-2 나폴리. PL: 아스널 28, 브라이튼 22, 시티 22, 리버풀 21. 시티 1-1 풀럼(앤더슨 57; 무니스 16).",',
     'liveNow: "UCL 수: 사바흐 1-4 바르사(고든 31, 51); 브뤼헤 0-3 리버풀(이삭 13, 비르츠 79). 화: 레알 5-1 PSV(벨링엄 59). 순위: 마드리드 15, PSG 13, 바르사 12, 리버풀 12. PL 아스널 28.",'),
    ('pulse: "챔피언스리그: 레알 마드리드 승점 15점 단독 선두; 아스널 PL 28점 선두",',
     'pulse: "챔피언스리그: 바르사 4-1 사바흐, 리버풀 3-0 브뤼헤; 레알 15점 선두 유지",'),
    ('tagline: "NBA 추수감사절 휴식 전: 댈러스, 덴버 120-101 완파; 보스턴 131-116 위저즈 제압.",',
     'tagline: "NBA컵: 식서스 111-104 히트, 르브론 25/10/12; 목요일 전체 휴식.",'),
    ('liveNow: "화 컵대회: 매버릭스 120-101 너기츠(플래그 24/6/12); 셀틱스 131-116 위저즈(테이텀 41, 조지 28; 데이비스 33/13); 피스톤스 104-86 매직(조 21). 수 미공개. 목 휴식.",',
     'liveNow: "수 컵대회: 76ers 111-104 히트(르브론 25/10/12, 맥시 30); 블레이저스 116-111 스퍼스(웸비 44/16). 화: 매브, 셀틱스, 피스톤스 승리. 목 휴식.",'),
    ('pulse: "에미레이츠 NBA 컵: 쿠퍼 플래그 24+12, 제이슨 테이텀 41점 맹활약 후 목요일 전체 휴식",',
     'pulse: "NBA컵: 르브론 식서스 첫 트리플더블, 111-104로 히트 제압 후 추수감사절 휴식",'),
    ('tonightBlurb: "추수감사절 NFL: 베어스(8-2) vs 라이온스(8-2)와 치프스-빌스(9-1). 패커스-램스 미공개. UCL: 레알 5-1 PSV. 데이비스컵: 체코 통과, 이탈리아-한국 진행 중. 금요일 카타르 GP.",',
     'tonightBlurb: "추수감사절 NFL: 램스 26-13 패커스. 베어스(8-2) vs 라이온스(8-2)는 미킥오프. UCL: 바르사 4-1 사바흐, 리버풀 3-0 브뤼헤. 데이비스컵: 이탈리아 2-1 한국, 영국 2-1 독일. 금요일 카타르 GP.",'),
    ('plBlurb: "PL 11R: 아스널 28, 브라이튼 22, 맨시티 22, 리버풀 21. 맨시티 1-1 풀럼(앤더슨 57, 무니스 16). UCL: 레알 5-1 PSV(음바페 64, 84, 벨링엄 59), 아스널 1-1 도르트문트.",',
     'plBlurb: "PL 11R: 아스널 28, 브라이튼 22, 맨시티 22, 리버풀 21. UCL 수: 사바흐 1-4 바르사, 브뤼헤 0-3 리버풀. 화: 레알 5-1 PSV(벨링엄 59).",'),
])

replace_pairs(os.path.join(I18N, "messages-ar.ts"), [
    ('tagline: "عيد الشكر NFL: لايونز وبيرز (8-2) يفتتحان الخميس بعد مواجهة باكرز ورامز على نتفليكس.",',
     'tagline: "عيد الشكر NFL: رامز 26-13 باكرز؛ بيرز ولايونز (8-2) لم يبدا بعد عند 1:00 ظهرا.",'),
    ('liveNow: "الخميس 26 نوفمبر: بيرز (8-2) ضد لايونز (8-2) 1:00 CBS، ايغلز-كاوبويز 4:30 FOX، تشيفز-بيلز (9-1) 8:20 NBC. باكرز ورامز الاربعاء غير منشور. الاسبوع 11: تكسانز 26-3 كولتس (هيوستن 4-6).",',
     'liveNow: "نهائي الاربعاء: رامز 26-13 باكرز (7-4 مقابل 6-5). الخميس غير منشور: بيرز (8-2) ضد لايونز (8-2) 1:00 CBS، ايغلز-كاوبويز 4:30، تشيفز-بيلز (9-1) 8:20.",'),
    ('pulse: "عيد الشكر NFL: صراع 8-2 بين لايونز وبيرز على القمة وتشيفز يحل ضيفا على بيلز 9-1",',
     'pulse: "NFL: رامز 26-13 باكرز؛ بيرز ولايونز (8-2) يفتتحان ثلاثية عيد الشكر",'),
    ('tagline: "كاس ديفيز بولونيا: التشيك يعبر 2-0؛ ايطاليا ضد كوريا ما زالت مفتوحة؛ الكاراز بطل تورينو.",',
     'tagline: "كاس ديفيز بولونيا: ايطاليا 2-1 كوريا وبريطانيا 2-1 المانيا؛ النمسا-اسبانيا 17:00 غير منشور.",'),
    ('liveNow: "بولونيا: التشيك 2-0 كندا؛ ايطاليا-كوريا مفتوحة بعد موسيتي 6-0 و7-6(5) هونغ. الخميس: بريطانيا-المانيا 10:00 والنمسا-اسبانيا 17:00. تورينو: الكاراز 6-2، 7-6(7) زفيريف.",',
     'liveNow: "ربع النهائي: التشيك 2-0 كندا؛ ايطاليا 2-1 كوريا؛ بريطانيا 2-1 المانيا. النمسا-اسبانيا 17:00 غير منشور. الجمعة: ايطاليا-التشيك 16:00. تورينو: الكاراز 6-2، 7-6(7).",'),
    ('pulse: "كاس ديفيز: التشيك الى نصف النهائي؛ بريطانيا ضد المانيا تفتح الخميس في بولونيا",',
     'pulse: "كاس ديفيز: بريطانيا وايطاليا مع التشيك في نصف النهائي؛ النمسا-اسبانيا بانتظار اللعب",'),
    ('tagline: "دوري الابطال الجولة 5: ريال مدريد يسحق ايندهوفن 5-1 وينفرد بـ15 نقطة؛ الاربعاء غير منشور.",',
     'tagline: "دوري الابطال ج5: برشلونة 4-1 في باكو وليفربول 3-0 في بروج؛ ريال مدريد ما زال الاول بـ15.",'),
    ('liveNow: "الثلاثاء: ريال مدريد 5-1 ايندهوفن (مبابي 64 و84)، ارسنال 1-1 دورتموند (جوكيريس 10؛ باير 55)، مانشستر سيتي 2-2 نابولي. الانجليزي: ارسنال 28، برايتون 22، سيتي 22، ليفربول 21. سيتي 1-1 فولهام (انديرسون 57؛ مونيز 16).",',
     'liveNow: "الاربعاء: ساباه 1-4 برشلونة (غوردون 31 و51)؛ كلوب بروج 0-3 ليفربول (ايساك 13، فيرتز 79). الثلاثاء: ريال 5-1 ايندهوفن (بيلينغهام 59). الترتيب: مدريد 15، باريس 13، برشا 12، ليفربول 12. ارسنال 28.",'),
    ('pulse: "دوري الابطال: ريال مدريد ينفرد بـ15 نقطة بعد الخماسية وارسنال يتصدر الانجليزي بـ28",',
     'pulse: "دوري الابطال: برشلونة 4-1 ساباه وليفربول 3-0 بروج؛ ريال مدريد ما زال الاول بـ15",'),
    ('tagline: "قبل عطلة عيد الشكر في NBA: دالاس يهزم دنفر 120-101 وبوسطن يتفوق على واشنطن 131-116.",',
     'tagline: "كأس NBA: سيكسرز 111-104 هيت، ليبرون 25/10/12؛ راحة الخميس.",'),
    ('liveNow: "كاس الدوري الثلاثاء: مافريكس 120-101 ناغتس (فلاغ 24/6/12)؛ سلتيكس 131-116 ويزاردز (تايتوم 41، جورج 28؛ ديفيس 33/13)؛ بيستونز 104-86 ماجيك (جو 21). الاربعاء غير منشور. الخميس راحة.",',
     'liveNow: "كأس الدوري الاربعاء: 76ers 111-104 هيت (ليبرون 25/10/12، ماكسي 30)؛ بلايزرز 116-111 سبرز (ويمبانياما 44/16). الثلاثاء: مافز وسلتيكس وبيستونز. الخميس راحة.",'),
    ('pulse: "كاس الامارات NBA: كوبر فلاغ وتايتوم (41 نقطة) يتالقان قبل استراحة الخميس",',
     'pulse: "كأس NBA: اول تريبل دبل لليبرون مع سيكسرز، 111-104 امام هيت",'),
    ('tonightBlurb: "عيد الشكر NFL: بيرز (8-2) ضد لايونز (8-2) وتشيفز ضد بيلز (9-1). باكرز ورامز غير منشور. دوري الابطال: ريال مدريد 5-1 ايندهوفن. كاس ديفيز: التشيك يعبر وايطاليا-كوريا مفتوحة. جائزة قطر الجمعة.",',
     'tonightBlurb: "عيد الشكر NFL: رامز 26-13 باكرز. بيرز (8-2) ضد لايونز (8-2) لم يبدا. دوري الابطال: برشا 4-1 ساباه وليفربول 3-0 بروج. كاس ديفيز: ايطاليا 2-1 كوريا وبريطانيا 2-1 المانيا. جائزة قطر الجمعة.",'),
    ('plBlurb: "الجولة 11: ارسنال 28، برايتون 22، مانشستر سيتي 22، ليفربول 21. سيتي 1-1 فولهام (انديرسون 57، مونيز 16). دوري الابطال: ريال 5-1 ايندهوفن (مبابي 64 و84، بيلينغهام 59).",',
     'plBlurb: "الجولة 11: ارسنال 28، برايتون 22، مانشستر سيتي 22، ليفربول 21. الاربعاء: ساباه 1-4 برشلونة وكلوب بروج 0-3 ليفربول. الثلاثاء: ريال 5-1 ايندهوفن (بيلينغهام 59).",'),
])

print("all message locales done")



