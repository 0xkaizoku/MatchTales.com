"""Update playground.ts, messages.ts, and messages-*.ts for 2026-11-19."""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
I18N = os.path.join(ROOT, "frontend", "src", "i18n")

# 1. Update playground.ts
playground_path = os.path.join(I18N, "playground.ts")
pg_txt = open(playground_path, "r", encoding="utf-8").read()

pg_updates = {
    "en": {
        "pinFinal": "Turin Thu McEnroe: Shelton vs Jodar (14:00 CET), Zverev vs Fils (20:30 CET). Wed Lendl: Alcaraz d Medvedev 6-2, 6-4 to clinch SF; Tiafoe d Cobolli.",
        "plFootnote": "Tue: Norway 3-2 Denmark (Haaland 88). Mon: Germany 5-0 Netherlands. PL returns Sat: Arsenal 27, Brighton 22, City 21, Liverpool 18.",
        "week1Closed": "TNF Tonight: Colts at Texans in Houston (8:15 PM ET). Week 10 complete: Chargers 23, Ravens 20 in Harbaugh Bowl.",
        "week1Sub": "C.J. Stroud and Texans defend AFC South lead against Anthony Richardson. Week 10 MNF: Chargers 23, Ravens 20.",
        "countdownTnf": "TNF TONIGHT: Colts at Texans (8:15 PM ET Prime Video). Week 11 officially begins.",
        "majorsDone": "RSM Classic Round 1 LIVE at Sea Island: Thompson -5, Hughes -4 (top-125 card bubble). Dubai Complete: McIlroy 8th title.",
        "gridAfterMadrid": "Round 21 · Las Vegas GP Free Practice Tonight (19-21 Nov)",
    },
    "fr": {
        "pinFinal": "Turin jeu McEnroe : Shelton vs Jodar (14h00), Zverev vs Fils (20h30). Mer Lendl : Alcaraz bat Medvedev 6-2, 6-4 et file en demies.",
        "plFootnote": "Mar : Norvège 3-2 Danemark (Haaland 88). Lun : Allemagne 5-0 Pays-Bas. Reprise PL samedi : Arsenal 27, Brighton 22, City 21, Liverpool 18.",
        "week1Closed": "TNF ce soir : Colts chez les Texans a Houston (20h15 ET). Semaine 10 terminee : Chargers 23, Ravens 20.",
        "week1Sub": "C.J. Stroud et les Texans defendent la tete de l'AFC Sud face a Anthony Richardson. MNF S10 : Chargers 23, Ravens 20.",
        "countdownTnf": "TNF CE SOIR : Colts chez les Texans (20h15 ET). Coup d'envoi de la semaine 11.",
        "majorsDone": "RSM Classic 1er tour EN DIRECT a Sea Island : Thompson -5, Hughes -4 (cartes top 125). Dubai termine : McIlroy 8e sacre.",
        "gridAfterMadrid": "Manche 21 · Essais libres du GP de Las Vegas ce soir (19-21 nov)",
    },
    "es": {
        "pinFinal": "Turín jue McEnroe: Shelton vs Jódar (14:00), Zverev vs Fils (20:30). Mié Lendl: Alcaraz vence 6-2, 6-4 a Medvedev y sella su pase a semifinales.",
        "plFootnote": "Mar: Noruega 3-2 Dinamarca (Haaland 88). Lun: Alemania 5-0 Países Bajos. Vuelve la PL el sábado: Arsenal 27, Brighton 22, City 21, Liverpool 18.",
        "week1Closed": "TNF esta noche: Colts en Texans en Houston (8:15 PM ET). Semana 10 finalizada: Chargers 23, Ravens 20.",
        "week1Sub": "C.J. Stroud y Texans defienden la cima del AFC Sur ante Anthony Richardson. MNF Sem 10: Chargers 23, Ravens 20.",
        "countdownTnf": "TNF ESTA NOCHE: Colts en Texans (8:15 PM ET). Comienza oficialmente la Semana 11.",
        "majorsDone": "The RSM Classic Ronda 1 EN VIVO en Sea Island: Thompson -5, Hughes -4 (burbuja top 125). Dubái: 8vo título de McIlroy.",
        "gridAfterMadrid": "Ronda 21 · Prácticas libres del GP de Las Vegas esta noche (19-21 nov)",
    },
    "de": {
        "pinFinal": "Turin Do McEnroe: Shelton vs Jódar (14:00), Zverev vs Fils (20:30). Mi Lendl: Alcaraz bezwingt Medvedev 6:2, 6:4 und steht im Halbfinale.",
        "plFootnote": "Di: Norwegen 3:2 Dänemark (Haaland 88.). Mo: Deutschland 5:0 Niederlande. PL-Rückkehr am Sa: Arsenal 27, Brighton 22, City 21, Liverpool 18.",
        "week1Closed": "TNF heute Nacht: Colts bei den Texans in Houston (8:15 PM ET). Woche 10 beendet: Chargers 23, Ravens 20.",
        "week1Sub": "C.J. Stroud und die Texans verteidigen AFC South Führung gegen Anthony Richardson. Woche 10 MNF: Chargers 23, Ravens 20.",
        "countdownTnf": "TNF HEUTE NACHT: Colts bei den Texans (8:15 PM ET). Startschuss für Woche 11.",
        "majorsDone": "RSM Classic Runde 1 LIVE in Sea Island: Thompson -5, Hughes -4 (Top-125 Bubble). Dubai beendet: 8. Titel für McIlroy.",
        "gridAfterMadrid": "Runde 21 · Las Vegas GP Freies Training heute Nacht (19.-21. Nov.)",
    },
    "it": {
        "pinFinal": "Torino gio McEnroe: Shelton vs Jodar (14:00), Zverev vs Fils (20:30). Mer Lendl: Alcaraz batte Medvedev 6-2, 6-4 e vola in semifinale.",
        "plFootnote": "Mar: Norvegia 3-2 Danimarca (Haaland 88). Lun: Germania 5-0 Olanda. Ritorno PL sabato: Arsenal 27, Brighton 22, City 21, Liverpool 18.",
        "week1Closed": "TNF stanotte: Colts contro Texans a Houston (8:15 PM ET). Settimana 10 conclusa: Chargers 23, Ravens 20.",
        "week1Sub": "C.J. Stroud e i Texans difendono il primato nell'AFC South contro Anthony Richardson. Week 10 MNF: Chargers 23, Ravens 20.",
        "countdownTnf": "TNF STANOTTE: Colts contro Texans (8:15 PM ET). Si apre ufficialmente la Week 11.",
        "majorsDone": "RSM Classic 1° giro LIVE a Sea Island: Thompson -5, Hughes -4 (bolla top 125). Dubai concluso: 8° titolo di McIlroy.",
        "gridAfterMadrid": "Round 21 · Prove libere del GP di Las Vegas stanotte (19-21 nov)",
    },
    "pl": {
        "pinFinal": "Turyn czw McEnroe: Shelton vs Jodar (14:00), Zverev vs Fils (20:30). Śr Lendl: Alcaraz pokonuje Miedwiediewa 6:2, 6:4 i melduje się w półfinale.",
        "plFootnote": "Wt: Norwegia 3:2 Dania (Haaland 88). Pon: Niemcy 5:0 Holandia. Powrót PL w sobotę: Arsenal 27, Brighton 22, City 21, Liverpool 18.",
        "week1Closed": "TNF dziś w nocy: Colts u Texans w Houston (8:15 PM ET). Tydzień 10 zakończony: Chargers 23, Ravens 20.",
        "week1Sub": "C.J. Stroud i Texans bronią pozycji lidera AFC South przed Anthonym Richardsonem. Tydzień 10 MNF: Chargers 23, Ravens 20.",
        "countdownTnf": "TNF DZIŚ W NOCY: Colts u Texans (8:15 PM ET). Oficjalne otwarcie 11. tygodnia.",
        "majorsDone": "RSM Classic 1. runda NA ŻYWO w Sea Island: Thompson -5, Hughes -4 (walka o top 125). Dubaj: 8. tytuł McIlroya.",
        "gridAfterMadrid": "21. runda · Czwartkowy trening przed GP Las Vegas (19-21 listopada)",
    },
    "zh": {
        "pinFinal": "都灵周四麦肯罗组生死战：谢尔顿对霍达尔（14:00），兹维列夫对菲斯（20:30）。周三伦德尔组：阿尔卡拉斯6-2、6-4轻取梅德韦杰夫率先晋级四强。",
        "plFootnote": "周二：挪威3-2丹麦（哈兰德88绝杀）。周一：德国5-0荷兰。英超周六重燃战火：阿森纳27，布莱顿22，曼城21，利物浦18。",
        "week1Closed": "今晚周四夜赛：小马客场挑战得州人（美东20:15）。第10周收官：闪电23-20力克乌鸦。",
        "week1Sub": "斯特劳德与得州人主场迎战理查森与小马争夺美南头名。第10周周一夜赛：闪电23-20乌鸦。",
        "countdownTnf": "今晚周四夜赛：小马客战得州人（美东20:15）。第11周正式开打。",
        "majorsDone": "海岛RSM精英赛首轮激战中：汤普森-5，休斯-4（前125保卡生死战）。迪拜收官：麦克罗伊夺得第8冠。",
        "gridAfterMadrid": "第21站 · 拉斯维加斯大奖赛今晚自由练习赛（11月19-21日）",
    },
    "ja": {
        "pinFinal": "トリノ木曜マッケンロー組決戦：シェルトン対ホダール（14:00）、ズベレフ対フィス（20:30）。水曜レンドル組：アルカラスがメドベージェフを6-2、6-4で下し準決勝へ。",
        "plFootnote": "火曜：ノルウェー3-2デンマーク（ハーランド88分V弾）。月曜：ドイツ5-0オランダ。土曜PL再開：アーセナル27、ブライトン22、シティ21。",
        "week1Closed": "今夜のTNF：ヒューストンでコルツ対テキサンズ（20:15 ET）。第10週終了：チャージャーズ23-20レイブンズ。",
        "week1Sub": "ストラウド擁するテキサンズがリチャードソン率いるコルツと地区首位を懸け激突。第10週MNF：チャージャーズ23-20レイブンズ。",
        "countdownTnf": "今夜TNF：コルツ対テキサンズ（20:15 ET）。第11週が公式に開幕。",
        "majorsDone": "シーアイランドでRSMクラシック第1R進行中：トンプソン-5、ヒューズ-4（来季シード125枠争い）。ドバイ：マキロイ8冠達成。",
        "gridAfterMadrid": "第21戦 · 今夜ラスベガスGPフリー走行開幕（11月19-21日）",
    },
    "ko": {
        "pinFinal": "토리노 목요일 매켄로 조 결전: 셸턴 vs 호다르 (14:00), 즈베레프 vs 필스 (20:30). 수요일 렌들 조: 알카라스, 메드베데프 6-2, 6-4 꺾고 준결승 진출.",
        "plFootnote": "화요일: 노르웨이 3-2 덴마크 (홀란 88분 결승골). 월요일: 독일 5-0 네덜란드. 토요일 PL 재개: 아스널 27, 브라이튼 22, 맨시티 21.",
        "week1Closed": "오늘 밤 TNF: 휴스턴에서 콜츠 vs 텍산스 (20:15 ET). 10주차 종료: 차저스 23-20 레이븐스.",
        "week1Sub": "C.J. 스트라우드의 텍산스가 앤서니 리차드슨의 콜츠를 홈으로 불러들여 남부 선두 격돌. 10주차 MNF: 차저스 23-20 레이븐스.",
        "countdownTnf": "오늘 밤 TNF: 콜츠 vs 텍산스 (20:15 ET). 11주차 공식 개막.",
        "majorsDone": "시 아일랜드 RSM 클래식 1R 진행 중: 톰슨 -5, 휴즈 -4 (125위 잔류 혈투). 두바이 최종: 매킬로이 통산 8번째 타이틀.",
        "gridAfterMadrid": "21라운드 · 오늘 밤 라스베이거스 GP 연습 주행 개막 (11월 19-21일)",
    },
    "ar": {
        "pinFinal": "تورينو الخميس ماكنرو: شيلتون ضد خودار (14:00)، زفيريف ضد فيس (20:30). الأربعاء ليندل: ألكاراز يهزم ميدفيديف 6-2، 6-4 ويبلغ نصف النهائي.",
        "plFootnote": "الثلاثاء: النرويج 3-2 الدنمارك (هالاند 88). الاثنين: ألمانيا 5-0 هولندا. عودة الدوري السبت: أرسنال 27، برايتون 22، سيتي 21.",
        "week1Closed": "ليلة الخميس الليلة: كولتس يحل ضيفا على تكسانز في هيوستن (8:15 مساء بتوقيت شرق أمريكا). انتهاء الجولة 10: تشارجرز 23، ريفنز 20.",
        "week1Sub": "سي جيه ستراود وتكسانز يدافعان عن صدارة القسم أمام أنتوني ريتشاردسون وكولتس. ختام الجولة 10: تشارجرز 23، ريفنز 20.",
        "countdownTnf": "ليلة الخميس الليلة: كولتس في ضيافة تكسانز (8:15 مساء). انطلاق الجولة 11 رسميا.",
        "majorsDone": "الجولة الأولى من آر إس إم كلاسيك مباشرة في سي آيلاند: طومسون -5، هيوز -4 (صراع بطاقات 125). دبي: اللقب الثامن لماكلروي.",
        "gridAfterMadrid": "الجولة 21 · انطلاق تجارب جائزة لاس فيغاس الكبرى الليلة (19-21 نوفمبر)",
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
    "todayDesk": "Thursday desk: TNF Colts at Texans opens Week 11. Turin Day 5 McEnroe deciders (Zverev vs Fils, Shelton vs Jodar). Las Vegas GP practice under the lights tonight.",
    "todayNfl": "TNF Tonight: Colts at Texans (8:15 PM ET, NRG Stadium, Houston). Week 10 in books: Chargers 23, Ravens 20 in Harbaugh Bowl; Lions 35, Patriots 10 in Munich.",
    "todayTnf": "NFL Week 11 TNF: Colts visit Texans tonight. Week 10 complete: Chargers 23-20 Ravens.",
    "football_tagline": "TNF Week 11: Colts clash with Texans in Houston; Chargers fresh off 23-20 Harbaugh Bowl victory.",
    "football_liveNow": "Tonight: Colts at Texans (8:15 PM ET, Prime Video, NRG Stadium). Week 10 MNF: Chargers 23, Ravens 20 (Herbert 22-yd TD run, Hampton 105 yds).",
    "football_pulse": "THURSDAY NIGHT FOOTBALL: COLTS AND TEXANS CLASH IN CRUCIAL AFC SOUTH WEEK 11 SHOWDOWN",
    "tennis_tagline": "Turin Day 5: Zverev faces Fils while Shelton meets Jodar for final McEnroe semifinal spot.",
    "tennis_liveNow": "Thu McEnroe: Shelton vs Jodar (14:00 CET), Zverev vs Fils (20:30 CET). Wed Lendl: Alcaraz d Medvedev 6-2, 6-4 to clinch SF; Tiafoe d Cobolli.",
    "tennis_pulse": "TURIN ATP FINALS: DECISIVE MCENROE BATTLES TODAY AS SHELTON AND FILS FIGHT TO JOIN ZVEREV IN SEMIS",
    "f1_tagline": "Las Vegas GP arrives: Engines fire on the Strip tonight for opening practice sessions under neon lights.",
    "f1_liveNow": "Tonight: Practice 1 (21:30 ET) & Practice 2 (01:00 ET). Drivers P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390).",
    "f1_pulse": "LAS VEGAS GP: ENGINES ROAR TONIGHT ON THE STRIP AS THURSDAY PRACTICE GETS UNDERWAY",
    "soccer_tagline": "Nations League phase wraps with Haaland heroics; Premier League title race resumes this Saturday.",
    "soccer_liveNow": "Tue: Norway 3-2 Denmark (Haaland late winner); Wales 2-3 Portugal. Mon: Germany 5-0 Netherlands. PL resumes Sat: Arsenal 27, Brighton 22, City 21.",
    "soccer_pulse": "SOCCER: NATIONS LEAGUE GROUPS CONCLUDE AS HAALAND FIRES NORWAY; PREMIER LEAGUE RETURNS SATURDAY",
    "basketball_tagline": "Heat top Bucks 137-130 behind Giannis revenge game; Nuggets rally from 17 down to stun Celtics.",
    "basketball_liveNow": "Wed: Heat 137-130 Bucks (Giannis 27/14/9, 6th straight win); Nuggets 105-101 Celtics (Jokic 24/9/8); Wizards 103-99 Raptors (Davis 25/14).",
    "basketball_pulse": "NBA WEDNESDAY: GIANNIS POSTS 27/14/9 TO BEAT FORMER TEAM FOR HEAT SIXTH STRAIGHT WIN",
    "golf_tagline": "The RSM Classic Round 1 underway at Sea Island with 2027 PGA Tour cards and top-125 cutoff on the line.",
    "golf_liveNow": "PGA Tour: Round 1 in progress at Sea Island (Seaside & Plantation). Top-125 bubble: Thompson, Hughes, Smotherman, Dahmen chasing status.",
    "golf_pulse": "PGA TOUR FALL FINALE: ROUND 1 UNDERWAY AT SEA ISLAND AS BUBBLE CONTENDERS FIGHT FOR 2027 CARDS",
    "tonight": "Thursday desk",
    "tonightBlurb": "Thursday Night Football: Colts at Texans opens Week 11 at NRG Stadium. Turin Day 5: Zverev faces Fils while Shelton meets Jodar for final semifinal spot. Las Vegas GP: engines roar tonight on the Strip for Thursday practice. Golf: Round 1 live at Sea Island.",
    "f1Title": "Las Vegas Grand Prix: Engines roar tonight on the Strip as Thursday practice begins",
    "f1Blurb": "Thursday night practice brings 1,000-hp hybrids to Las Vegas Boulevard: 33 points separate Verstappen (279) to Norris (246) behind Champion Antonelli (390)."
}

msg_fr = {
    "todayDesk": "Bureau du jeudi : TNF Colts-Texans pour ouvrir la Semaine 11. Turin J5 McEnroe deciders (Zverev vs Fils, Shelton vs Jodar). Essais du GP de Las Vegas sous les lumieres ce soir.",
    "todayNfl": "TNF ce soir : Colts chez les Texans a Houston (NRG Stadium). Bilan Semaine 10 : Chargers 23-20 Ravens dans le Harbaugh Bowl ; Lions 35-10 Patriots a Munich.",
    "todayTnf": "NFL Semaine 11 TNF : Les Texans recoivent les Colts ce soir. Semaine 10 terminee : Chargers 23-20 Ravens.",
    "football_tagline": "TNF Semaine 11 : duel Colts-Texans a Houston ; les Chargers savourent leur triomphe 23-20 dans le Harbaugh Bowl.",
    "football_liveNow": "Ce soir : Colts chez les Texans (20h15 ET, NRG Stadium). Sem 10 MNF : Chargers 23, Ravens 20 (course TD de Herbert 22 yds, Hampton 105 yds).",
    "football_pulse": "THURSDAY NIGHT FOOTBALL : LES COLTS DEFISENT LES TEXANS POUR LE SOMMET DE L'AFC SUD EN SEMAINE 11",
    "tennis_tagline": "Turin Jour 5 : Zverev defie Fils pendant que Shelton affronte Jodar pour la derniere place en demies.",
    "tennis_liveNow": "Jeu McEnroe : Shelton vs Jodar (14h00), Zverev vs Fils (20h30). Mer Lendl : Alcaraz bat Medvedev 6-2, 6-4 et rejoint le dernier carre.",
    "tennis_pulse": "MASTERS DE TURIN : JOURNEE DECISIVE DANS LE GROUPE MCENROE POUR REJOINDRE ZVEREV ET ALCARAZ EN DEMIES",
    "f1_tagline": "Le GP de Las Vegas demarre : Les moteurs vrombissent sur le Strip ce soir pour les premiers essais libres.",
    "f1_liveNow": "Ce soir : Essais 1 (21h30 ET) et Essais 2 (01h00 ET). Duel P2 : Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390).",
    "f1_pulse": "GP DE LAS VEGAS : PREMIERS TOURS DE ROUE CE SOIR SUR LE STRIP POUR LES ESSAIS DU JEUDI",
    "soccer_tagline": "Fin des groupes de Ligue des nations avec l'eclair de Haaland ; retour de la Premier League ce samedi.",
    "soccer_liveNow": "Mar : Norvege 3-2 Danemark (Haaland 88e) ; Pays de Galles 2-3 Portugal. Lun : Allemagne 5-0 Pays-Bas. Reprise PL samedi : Arsenal 27, Brighton 22, City 21.",
    "soccer_pulse": "FOOTBALL : LA PHASE DE GROUPES DE LIGUE DES NATIONS S'ACHEVE ; LA PREMIER LEAGUE REVIENT SAMEDI",
    "basketball_tagline": "Le Heat domine les Bucks 137-130 avec un Giannis monumental ; Denver efface 17 points de retard contre Boston.",
    "basketball_liveNow": "Mer : Heat 137-130 Bucks (Giannis 27/14/9, 6e de suite) ; Nuggets 105-101 Celtics (Jokic 24/9/8) ; Wizards 103-99 Raptors (Davis 25/14).",
    "basketball_pulse": "NBA MERCREDI : GIANNIS S'ILLUSTRE AVEC 27/14/9 CONTRE MILWAUKEE ; 6E SUCCES DE SUITE POUR LE HEAT",
    "golf_tagline": "1er tour du RSM Classic en direct a Sea Island : cartes du PGA Tour 2027 et bulle du top 125 en jeu.",
    "golf_liveNow": "PGA Tour : 1er tour en cours a Sea Island (Seaside & Plantation). Bulle top 125 : Thompson, Hughes, Smotherman, Dahmen au coude a coude.",
    "golf_pulse": "PGA TOUR FALL FINALE : 1ER TOUR EN DIRECT A SEA ISLAND DANS LA COURSE AUX CARTES DU TOP-125",
    "tonight": "Bureau du jeudi",
    "tonightBlurb": "Thursday Night Football : Les Texans recoivent les Colts a Houston pour lancer la semaine 11. Turin J5 : Zverev contre Fils et Shelton face a Jodar pour la qualification. GP de Las Vegas : premiers essais sur le Strip ce soir. Golf : 1er tour en direct a Sea Island.",
    "f1Title": "Grand Prix de Las Vegas : Les moteurs s'eveillent ce soir sur le Strip pour les essais du jeudi",
    "f1Blurb": "Les monoplaces de 1 000 ch debarquent sur le Strip de Las Vegas : 33 points separent Verstappen (279) de Norris (246) derriere le champion Antonelli (390)."
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
print("Updated messages.ts.")

# 3. Update messages-*.ts files
other_locales = {
    "es": {
        "todayDesk": "Mesa del jueves: TNF Colts en Texans abre la Semana 11. Turín Día 5 decide el Grupo McEnroe (Zverev vs Fils, Shelton vs Jódar). Prácticas del GP de Las Vegas esta noche.",
        "todayNfl": "TNF esta noche: Colts en Texans (8:15 PM ET, NRG Stadium, Houston). Semana 10: Chargers 23-20 Ravens en el Harbaugh Bowl; Lions 35-10 Patriots en Múnich.",
        "todayTnf": "NFL Semana 11 TNF: Texans reciben a Colts esta noche. Semana 10 finalizada: Chargers 23-20 Ravens.",
        "football_tagline": "TNF Semana 11: Choque de trenes entre Colts y Texans en Houston; Chargers celebran triunfo 23-20 en Harbaugh Bowl.",
        "football_liveNow": "Esta noche: Colts en Texans (8:15 PM ET, NRG Stadium). Sem 10 MNF: Chargers 23, Ravens 20 (carrera TD 22 yds de Herbert, Hampton 105 yds).",
        "football_pulse": "THURSDAY NIGHT FOOTBALL: COLTS Y TEXANS CHOCAN POR EL LIDERATO DEL AFC SUR EN LA SEMANA 11",
        "tennis_tagline": "Turín Día 5: Zverev se mide a Fils mientras Shelton juega ante Jódar por el último cupo a semifinales.",
        "tennis_liveNow": "Jue McEnroe: Shelton vs Jódar (14:00), Zverev vs Fils (20:30). Mié Lendl: Alcaraz vence 6-2, 6-4 a Medvedev y clasifica a semifinales.",
        "tennis_pulse": "TORNEO DE MAESTROS TURÍN: DUELOS DECISIVOS HOY EN EL GRUPO MCENROE PARA UNIRSE A ZVEREV Y ALCARAZ EN SEMIS",
        "f1_tagline": "Llega el GP de Las Vegas: Rujen los motores en el Strip esta noche para las prácticas libres bajo las luces.",
        "f1_liveNow": "Esta noche: Práctica 1 (21:30 ET) y Práctica 2 (01:00 ET). Lucha P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390).",
        "f1_pulse": "GP DE LAS VEGAS: PRIMERAS PRÁCTICAS ESTA NOCHE EN EL STRIP CON LA LUCHA POR EL SUBCAMPEONATO AL ROJO VIVO",
        "soccer_tagline": "Concluye la fase de grupos de la Liga de Naciones con gol agónico de Haaland; la Premier League regresa este sábado.",
        "soccer_liveNow": "Mar: Noruega 3-2 Dinamarca (Haaland 88); Gales 2-3 Portugal. Lun: Alemania 5-0 Países Bajos. Vuelve PL sábado: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "FÚTBOL: CONCLUYE LA NATIONS LEAGUE CON HEROICA DE HAALAND; LA PREMIER LEAGUE VUELVE EL SÁBADO",
        "basketball_tagline": "Los Heat superan 137-130 a los Bucks con exhibición de Giannis; Nuggets remontan 17 puntos a Celtics.",
        "basketball_liveNow": "Mié: Heat 137-130 Bucks (Giannis 27/14/9, 6ta seguida); Nuggets 105-101 Celtics (Jokic 24/9/8); Wizards 103-99 Raptors (Davis 25/14).",
        "basketball_pulse": "NBA MIÉRCOLES: GIANNIS SUMA 27/14/9 ANTE BUCKS Y LIDERA LA SEXTA VICTORIA CONSECUTIVA DE HEAT",
        "golf_tagline": "En juego la Ronda 1 de The RSM Classic en Sea Island con las tarjetas de 2027 en disputa.",
        "golf_liveNow": "PGA Tour: Ronda 1 en curso en Sea Island (Seaside & Plantation). Burbuja top 125: Thompson, Hughes, Smotherman, Dahmen en acción.",
        "golf_pulse": "PGA TOUR FALL FINALE: RONDA 1 EN VIVO EN SEA ISLAND EN PLENA BATALLA POR LAS TARJETAS DEL TOP-125",
        "tonight": "Mesa del jueves",
        "tonightBlurb": "Thursday Night Football: Texans reciben a Colts en Houston para abrir la Semana 11. Turín Día 5: Zverev ante Fils y Shelton frente a Jódar por el pase a semifinales. GP de Las Vegas: prácticas nocturnas en el Strip. Golf: Ronda 1 en vivo en Sea Island.",
        "f1Title": "Gran Premio de Las Vegas: Los motores rugen esta noche en el Strip para las prácticas del jueves",
        "f1Blurb": "Los bólidos llegan al Strip de Las Vegas: 33 puntos separan a Verstappen (279) de Norris (246) detrás del campeón Antonelli (390)."
    },
    "de": {
        "todayDesk": "Donnerstags-Desk: TNF Colts bei den Texans eröffnet Woche 11. Turin Tag 5 entscheidet McEnroe-Gruppe (Zverev vs Fils, Shelton vs Jódar). Las Vegas GP Training heute Nacht.",
        "todayNfl": "TNF heute Nacht: Colts bei den Texans (8:15 PM ET, NRG Stadium, Houston). Woche 10: Chargers 23-20 Ravens im Harbaugh Bowl; Lions 35-10 Patriots in München.",
        "todayTnf": "NFL Woche 11 TNF: Texans empfangen Colts heute Nacht. Woche 10 beendet: Chargers 23-20 Ravens.",
        "football_tagline": "TNF Woche 11: Colts fordern Texans in Houston heraus; Chargers feiern 23:20-Sieg im Harbaugh Bowl.",
        "football_liveNow": "Heute Nacht: Colts bei den Texans (8:15 PM ET, NRG Stadium). Woche 10 MNF: Chargers 23, Ravens 20 (Herbert 22-Yd TD, Hampton 105 Yds).",
        "football_pulse": "THURSDAY NIGHT FOOTBALL: COLTS UND TEXANS KÄMPFEN IN WOCHE 11 UM DIE SPITZE DER AFC SOUTH",
        "tennis_tagline": "Turin Tag 5: Zverev trifft auf Fils, während Shelton gegen Jódar um den letzten Halbfinalplatz kämpft.",
        "tennis_liveNow": "Do McEnroe: Shelton vs Jódar (14:00), Zverev vs Fils (20:30). Mi Lendl: Alcaraz bezwingt Medvedev 6:2, 6:4 und steht sicher im Halbfinale.",
        "tennis_pulse": "ATP FINALS TURIN: ENTSCHEIDUNGSTAG IN DER MCENROE-GRUPPE UM DAS HALBFINAL-TICKET NEBEN ZVEREV UND ALCARAZ",
        "f1_tagline": "Las Vegas GP ist da: Motoren heulen heute Nacht auf dem Strip für die ersten Trainings auf.",
        "f1_liveNow": "Heute Nacht: Training 1 (21:30 ET) & Training 2 (01:00 ET). Kampf um P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390).",
        "f1_pulse": "LAS VEGAS GP: HEUTE NACHT ERSTE TRAININGS AUF DEM STRIP MIT PACKENDEM KAMPF UM PLATZ ZWEI",
        "soccer_tagline": "Nations League Gruppenphase endet mit Haaland-Gala; Premier League kehrt am Samstag zurück.",
        "soccer_liveNow": "Di: Norwegen 3:2 Dänemark (Haaland 88.); Wales 2:3 Portugal. Mo: Deutschland 5:0 Niederlande. PL-Rückkehr Sa: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "FUSSBALL: NATIONS LEAGUE GRUPPEN BEENDET DANK HAALAND-TREFFER; PREMIER LEAGUE STARTET AM SAMSTAG",
        "basketball_tagline": "Heat bezwingen Bucks 137:130 nach Giannis-Meisterwerk; Nuggets drehen 17-Punkte-Rückstand gegen Celtics.",
        "basketball_liveNow": "Mi: Heat 137:130 Bucks (Giannis 27/14/9, 6. Sieg in Folge); Nuggets 105:101 Celtics (Jokic 24/9/8); Wizards 103:99 Raptors (Davis 25/14).",
        "basketball_pulse": "NBA MITTWOCH: GIANNIS FÜHRT HEAT MIT 27/14/9 ZUM SECHSTEN ERFOLG IN SERIE GEGEN EX-KLUB BUCKS",
        "golf_tagline": "RSM Classic Runde 1 läuft in Sea Island: Top-125-Tourkarten für 2027 auf dem Spiel.",
        "golf_liveNow": "PGA Tour: Runde 1 im Gange in Sea Island (Seaside & Plantation). Bubble Top 125: Thompson, Hughes, Smotherman, Dahmen im Einsatz.",
        "golf_pulse": "PGA TOUR FALL FINALE: RUNDE 1 LIVE IN SEA ISLAND IM NERVENSPIEL UM DIE KARTEN FÜR 2027",
        "tonight": "Donnerstags-Desk",
        "tonightBlurb": "Thursday Night Football: Texans empfangen die Colts in Houston zum Start von Woche 11. Turin Tag 5: Zverev gegen Fils und Shelton gegen Jódar um den Halbfinaleinzug. Las Vegas GP: Nacht-Trainings auf dem Strip. Golf: Runde 1 live in Sea Island.",
        "f1Title": "Großer Preis von Las Vegas: Motoren heulen heute Nacht auf dem Strip für das Training auf",
        "f1Blurb": "Die F1-Boliden erobern den Las Vegas Strip: 33 Punkte trennen Verstappen (279) und Norris (246) hinter Champion Antonelli (390)."
    },
    "it": {
        "todayDesk": "Desk del giovedì: TNF Colts a Houston contro i Texans per la Week 11. Torino Giorno 5: spareggi nel gruppo McEnroe. Prove libere del GP di Las Vegas stanotte.",
        "todayNfl": "TNF stanotte: Colts contro Texans (8:15 PM ET, NRG Stadium, Houston). Week 10: Chargers 23-20 Ravens nell'Harbaugh Bowl; Lions 35-10 Patriots a Monaco.",
        "todayTnf": "NFL Week 11 TNF: Texans ospitano i Colts stanotte. Settimana 10 conclusa: Chargers 23-20 Ravens.",
        "football_tagline": "TNF Week 11: Sfida divisionale tra Colts e Texans a Houston; Chargers reduci dal 23-20 nell'Harbaugh Bowl.",
        "football_liveNow": "Stanotte: Colts contro Texans (8:15 PM ET, NRG Stadium). Week 10 MNF: Chargers 23, Ravens 20 (corsa TD di Herbert 22 yd, Hampton 105 yd).",
        "football_pulse": "THURSDAY NIGHT FOOTBALL: COLTS E TEXANS SI SFIDANO PER IL VERTICE DELL'AFC SOUTH NELLA WEEK 11",
        "tennis_tagline": "Torino Giorno 5: Zverev affronta Fils mentre Shelton sfida Jodar per l'ultimo posto in semifinale.",
        "tennis_liveNow": "Gio McEnroe: Shelton vs Jodar (14:00), Zverev vs Fils (20:30). Mer Lendl: Alcaraz batte Medvedev 6-2, 6-4 e vola in semifinale.",
        "tennis_pulse": "NITTO ATP FINALS TORINO: GIORNATA DECISIVA NEL GRUPPO MCENROE PER RAGGIUNGERE ZVEREV E ALCARAZ IN SEMIFINALE",
        "f1_tagline": "Arriva il GP di Las Vegas: I motori si accendono sulla Strip stanotte per le prove libere sotto i riflettori.",
        "f1_liveNow": "Stanotte: Prove 1 (21:30 ET) e Prove 2 (01:00 ET). Sfida P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390).",
        "f1_pulse": "GP DI LAS VEGAS: PRIMI GIRI STANOTTE SULLA STRIP CON LA VOLATA PER IL SECONDO POSTO MONDIALE",
        "soccer_tagline": "Si chiude la Nations League col sigillo di Haaland; sabato riparte la corsa scudetto in Premier League.",
        "soccer_liveNow": "Mar: Norvegia 3-2 Danimarca (Haaland 88); Galles 2-3 Portogallo. Lun: Germania 5-0 Olanda. Ritorno PL sabato: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "CALCIO: LA NATIONS LEAGUE SALUTA CON IL TRIONFO DI HAALAND; LA PREMIER LEAGUE TORNA SABATO",
        "basketball_tagline": "I Heat piegano i Bucks 137-130 con un Giannis da favola; Denver rimonta 17 punti e batte Boston.",
        "basketball_liveNow": "Mer: Heat 137-130 Bucks (Giannis 27/14/9, 6a di fila); Nuggets 105-101 Celtics (Jokic 24/9/8); Wizards 103-99 Raptors (Davis 25/14).",
        "basketball_pulse": "NBA MERCOLEDÌ: GIANNIS BRILLA CON 27/14/9 CONTRO MILWAUKEE PER IL SESTO SUCCESSO DI FILA DEI HEAT",
        "golf_tagline": "In corso il 1° giro del RSM Classic a Sea Island con le carte per il PGA Tour 2027 in palio.",
        "golf_liveNow": "PGA Tour: 1° giro in corso a Sea Island (Seaside & Plantation). Bolla top 125: Thompson, Hughes, Smotherman, Dahmen in campo.",
        "golf_pulse": "PGA TOUR FALL FINALE: 1° GIRO LIVE A SEA ISLAND NELLA DRAMMATICA CORSA ALLE CARTE DELLA TOP-125",
        "tonight": "Desk del giovedì",
        "tonightBlurb": "Thursday Night Football: Texans ospitano i Colts a Houston per aprire la Week 11. Torino Giorno 5: Zverev contro Fils e Shelton contro Jodar per le semifinali. GP di Las Vegas: prove notturne sulla Strip. Golf: 1° giro in corso a Sea Island.",
        "f1Title": "Gran Premio di Las Vegas: I motori ruggiscono stanotte sulla Strip per le prove libere",
        "f1Blurb": "Le monoposto sfrecciano sulla Strip di Las Vegas: 33 punti dividono Verstappen (279) da Norris (246) alle spalle del campione Antonelli (390)."
    },
    "pl": {
        "todayDesk": "Biurko na czwartek: TNF Colts u Texans otwiera 11. tydzień. Turyn Dzień 5: rozstrzygnięcia w grupie McEnroe (Zverev vs Fils, Shelton vs Jodar). Nocny trening F1 w Vegas.",
        "todayNfl": "TNF dziś w nocy: Colts u Texans (8:15 PM ET, NRG Stadium, Houston). Tydzień 10: Chargers 23-20 Ravens w Harbaugh Bowl; Lions 35-10 Patriots w Monachium.",
        "todayTnf": "NFL Tydzień 11 TNF: Texans podejmują Colts dziś w nocy. Tydzień 10 zakończony: Chargers 23-20 Ravens.",
        "football_tagline": "TNF Tydzień 11: Starcie Colts z Texans w Houston; Chargers po triumfie 23:20 w Harbaugh Bowl.",
        "football_liveNow": "Dziś w nocy: Colts u Texans (8:15 PM ET, NRG Stadium). Tydzień 10 MNF: Chargers 23, Ravens 20 (bieg TD 22 yds Herberta, Hampton 105 yds).",
        "football_pulse": "THURSDAY NIGHT FOOTBALL: COLTS I TEXANS W WALCE O PRZODOWNICTWO W AFC SOUTH W 11. TYGODNIU",
        "tennis_tagline": "Turyn Dzień 5: Zverev gra z Filsem, a Shelton walczy z Jodarem o ostatnie miejsce w półfinale.",
        "tennis_liveNow": "Czw McEnroe: Shelton vs Jodar (14:00), Zverev vs Fils (20:30). Śr Lendl: Alcaraz ogrywa Miedwiediewa 6:2, 6:4 i wchodzi do półfinału.",
        "tennis_pulse": "ATP FINALS TURYN: DECYDUJĄCE MECZE W GRUPIE MCENROE O AWANS DO PÓŁFINAŁU OBOK ZVEREVA I ALCARAZA",
        "f1_tagline": "GP Las Vegas czas zacząć: Ryk silników na Strip dziś w nocy podczas pierwszych treningów.",
        "f1_liveNow": "Dziś w nocy: Trening 1 (21:30 ET) i Trening 2 (01:00 ET). Walka o P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390).",
        "f1_pulse": "GP LAS VEGAS: PIERWSZE TRENINGI NA STRIP DZIŚ W NOCY Z ZACIĘTĄ WALKĄ O WICEMISTRZOSTWO ŚWIATA",
        "soccer_tagline": "Koniec fazy grupowej Ligi Narodów po popisie Haalanda; Premier League wraca w sobotę.",
        "soccer_liveNow": "Wt: Norwegia 3:2 Dania (Haaland 88); Walia 2:3 Portugalia. Pon: Niemcy 5:0 Holandia. Powrót PL w sobotę: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "PIŁKA NOŻNA: FAZA GRUPOWA LIGI NARODÓW ZAKOŃCZONA GOLAMI HAALANDA; PREMIER LEAGUE WRACA W SOBOTĘ",
        "basketball_tagline": "Heat ogrywają Bucks 137:130 po kapitalnym meczu Giannisa; Nuggets odrabiają 17 punktów z Celtics.",
        "basketball_liveNow": "Śr: Heat 137:130 Bucks (Giannis 27/14/9, 6. wygrana z rzędu); Nuggets 105:101 Celtics (Jokic 24/9/8); Wizards 103:99 Raptors (Davis 25/14).",
        "basketball_pulse": "NBA ŚRODA: GIANNIS NOTUJE 27/14/9 PRZECIWKO BUCKS I PROWADZI HEAT DO SZÓSTEGO ZWYCIĘSTWA Z RZĘDU",
        "golf_tagline": "1. runda RSM Classic trwa w Sea Island: walka o karty PGA Tour na sezon 2027.",
        "golf_liveNow": "PGA Tour: 1. runda w toku w Sea Island (Seaside & Plantation). Na granicy top 125: Thompson, Hughes, Smotherman, Dahmen.",
        "golf_pulse": "PGA TOUR FALL FINALE: 1. RUNDA NA ŻYWO W SEA ISLAND W DRAMATYCZNEJ GRZE O UTRZYMANIE W TOP-125",
        "tonight": "Biurko na czwartek",
        "tonightBlurb": "Thursday Night Football: Texans podejmują Colts w Houston na inaugurację 11. tygodnia. Turyn Dzień 5: Zverev z Filsem oraz Shelton z Jodarem o półfinały. GP Las Vegas: nocne treningi na Strip. Golf: 1. runda na żywo w Sea Island.",
        "f1Title": "Grand Prix Las Vegas: Ryk silników rozbrzmiewa dziś w nocy na Strip podczas treningów",
        "f1Blurb": "Bolidy wyjeżdżają na Las Vegas Strip: 33 punkty dzielą Verstappena (279) od Norrisa (246) za mistrzem Antonellim (390)."
    },
    "zh": {
        "todayDesk": "周四工作台：周四夜赛小马客战得州人揭幕第11周。都灵年终总决赛第5比赛日麦肯罗组生死战。拉斯维加斯大奖赛今晚自由练习赛开跑。",
        "todayNfl": "今晚周四夜赛：小马客战得州人（美东20:15，休斯敦NRG体育场）。第10周战报：闪电23-20胜乌鸦哈博兄弟战；雄狮35-10胜爱国者。",
        "todayTnf": "NFL第11周TNF：得州人今晚主场迎战小马。第10周收官：闪电23-20险胜乌鸦。",
        "football_tagline": "周四夜赛第11周：小马客战得州人争夺美南榜首；闪电刚收获23-20哈博德比胜利。",
        "football_liveNow": "今晚：小马客战得州人（美东20:15，休斯敦NRG体育场）。第10周MNF：闪电23-20乌鸦（赫伯特22码TD冲球，汉普顿105码）。",
        "football_pulse": "周四夜赛焦点：小马客场挑战得州人展开美联南区第11周关键对决",
        "tennis_tagline": "都灵总决赛第5日：兹维列夫对决菲斯，谢尔顿战霍达尔争夺麦肯罗组最后出线权。",
        "tennis_liveNow": "周四麦肯罗组：谢尔顿对霍达尔（14:00），兹维列夫对菲斯（20:30）。周三伦德尔组：阿尔卡拉斯6-2、6-4轻取梅德韦杰夫晋级半决赛。",
        "tennis_pulse": "ATP都灵总决赛：麦肯罗组今日生死对决，谢尔顿与菲斯全力拼杀争夺半决赛席位",
        "f1_tagline": "拉斯维加斯大奖赛打响：赛车今晚轰鸣驶上赌城大道展开夜间自由练习赛。",
        "f1_liveNow": "今晚：一练（美东21:30）与二练（美东01:00）。年度次席之争：维斯塔潘279，拉塞尔262，汉密尔顿261，勒克莱尔249，诺里斯246（安东内利390）。",
        "f1_pulse": "拉斯维加斯大奖赛：今晚赛车亮相赌城大道霓虹灯下，年度亚军厮杀进入白热化",
        "soccer_tagline": "欧国联小组赛在哈兰德绝杀中落幕；英超冠军争夺战本周六重燃战火。",
        "soccer_liveNow": "周二：挪威3-2丹麦（哈兰德88绝杀）；威尔士2-3葡萄牙。周一：德国5-0荷兰。英超周六回归：阿森纳27，布莱顿22，曼城21。",
        "soccer_pulse": "足球动态：哈兰德绝杀助挪威斩获胜仗欧国联收官；英超联赛周六全面重燃战火",
        "basketball_tagline": "字母哥战旧主狂砍准三双助热火137-130擒雄鹿；掘金落后17分逆转凯尔特人。",
        "basketball_liveNow": "周三：热火137-130雄鹿（字母哥27/14/9，六连胜）；掘金105-101凯尔特人（约基奇24/9/8）；奇才103-99猛龙（浓眉25/14）。",
        "basketball_pulse": "NBA周三战报：字母哥贡献27/14/9击溃老东家雄鹿，热火喜迎六连胜",
        "golf_tagline": "海岛RSM精英赛首轮开打：2027年美巡赛全卡与前125保卡大决战打响。",
        "golf_liveNow": "美巡赛：海岛首轮激战中（海滨与种植园球场）。前125保卡线：汤普森、休斯、斯莫瑟曼、达门全情出战。",
        "golf_pulse": "美巡赛秋季收官：海岛RSM精英赛首轮现场激战，前125保卡战惊心动魄",
        "tonight": "周四工作台",
        "tonightBlurb": "周四夜赛：得州人在休斯敦NRG体育场迎战小马打响第11周。都灵第5日：兹维列夫对菲斯，谢尔顿战霍达尔争夺四强席位。拉斯维加斯大奖赛：今晚大道练习赛。高尔夫：海岛首轮激战中。",
        "f1Title": "拉斯维加斯大奖赛：引擎今晚在赌城大道轰鸣展开周四自由练习赛",
        "f1Blurb": "千匹马力混动战车登陆拉斯维加斯大道：双冠王安东内利身后，33分差距分化维斯塔潘（279）至诺里斯（246）。"
    },
    "ja": {
        "todayDesk": "木曜デスク：今夜TNFコルツ対テキサンズで第11週開幕。トリノ第5日マッケンロー組決戦（ズベレフ対フィス、シェルトン対ホダール）。今夜ラスベガスGP夜間練習。",
        "todayNfl": "今夜TNF：コルツ対テキサンズ（20:15 ET、ヒューストンNRGスタジアム）。第10週終了：チャージャーズ23-20レイブンズ（ハーボー対決）；ライオンズ35-10ペイトリオッツ。",
        "todayTnf": "NFL第11週TNF：テキサンズが今夜コルツを迎撃。第10週終了：チャージャーズ23-20レイブンズ。",
        "football_tagline": "TNF第11週：ヒューストンでコルツ対テキサンズの地区首位決戦；チャージャーズは23-20でハーボー対決制す。",
        "football_liveNow": "今夜：コルツ対テキサンズ（20:15 ET、NRGスタジアム）。第10週MNF：チャージャーズ23-20レイブンズ（ハーバート22yd TD、ハンプトン105yd）。",
        "football_pulse": "サーズデーナイト決戦：コルツとテキサンズが第11週AFC南部地区首位を懸けて激突",
        "tennis_tagline": "トリノ第5日：ズベレフがフィスと対戦、シェルトンはホダールと最後の準決勝進出枠を争う。",
        "tennis_liveNow": "木曜マッケンロー組：シェルトン対ホダール（14:00）、ズベレフ対フィス（20:30）。水曜レンドル組：アルカラスがメドベージェフを6-2、6-4で破り準決勝へ。",
        "tennis_pulse": "ATPファイナルズ・トリノ：マッケンロー組決戦、シェルトンとフィスがズベレフとアルカラスの待つ4強入りを目指す",
        "f1_tagline": "ラスベガスGP開幕：今夜ネオン煌めくストリップで木曜フリー走行がスタート。",
        "f1_liveNow": "今夜：FP1（21:30 ET）＆FP2（01:00 ET）。ドライバーズ2位争い：フェルスタッペン279、ラッセル262、ハミルトン261、ルクレール249、ノリス246（アントネッリ390）。",
        "f1_pulse": "ラスベガスGP：今夜ストリップでフリー走行開幕、ランキング2位を懸けた熱戦へ",
        "soccer_tagline": "ネーションズリーグGSがハーランド劇的弾で終了；土曜日にプレミアリーグ再開。",
        "soccer_liveNow": "火曜：ノルウェー3-2デンマーク（ハーランド88分）；ウェールズ2-3ポルトガル。月曜：ドイツ5-0オランダ。土曜PL再開：アーセナル27、ブライトン22、シティ21。",
        "soccer_pulse": "サッカー：ハーランドの劇的弾でネーションズリーグGS終了；土曜日にプレミアリーグ再開へ",
        "basketball_tagline": "ヤニスが古巣相手に27得点の大暴れでヒート6連勝；ナゲッツはセルティックスに17点差大逆転勝利。",
        "basketball_liveNow": "水曜：ヒート137-130バックス（ヤニス27/14/9、6連勝）；ナゲッツ105-101セルティックス（ヨキッチ24/9/8）；ウィザーズ103-99ラプターズ（デイビス25/14）。",
        "basketball_pulse": "NBA水曜：ヤニスが古巣バックス相手に27/14/9と大爆発、ヒートが怒涛の6連勝を達成",
        "golf_tagline": "シーアイランドでRSMクラシック第1R開幕：来季シード125枠争い決着へ。",
        "golf_liveNow": "PGAツアー：シーアイランドで第1R進行中（シーサイド＆プランテーション）。当落線上：トンプソン、ヒューズ、スモザーマン、ダーメン。",
        "golf_pulse": "PGAツアー秋季最終戦：シーアイランドで第1R生中継、来季シード権獲得へ真剣勝負",
        "tonight": "木曜デスク",
        "tonightBlurb": "サーズデーナイト：ヒューストンでテキサンズ対コルツで第11週開幕。トリノ第5日：ズベレフ対フィス、シェルトン対ホダールで準決勝進出決定。ラスベガスGP：今夜ストリップで夜間走行開始。ゴルフ：シーアイランド第1R進行中。",
        "f1Title": "ラスベガスGrand Prix：今夜ストリップで木曜フリー走行がスタート",
        "f1Blurb": "1,000馬力のモンスターマシンがストリップへ：王者アントネッリ（390）の背後でフェルスタッペン（279）からノリス（246）まで33点差。"
    },
    "ko": {
        "todayDesk": "목요일 데스크: 오늘 밤 TNF 콜츠 vs 텍산스로 11주차 개막. 토리노 파이널스 5일차 매켄로 조 결전 (즈베레프 vs 필스, 셸턴 vs 호다르). 오늘 밤 라스베이거스 GP 연습 주행.",
        "todayNfl": "오늘 밤 TNF: 휴스턴에서 콜츠 vs 텍산스 (20:15 ET, NRG 스타디움). 10주차 결산: 차저스 23-20 레이븐스 하보 볼; 라이온스 35-10 패트리어츠 뮌헨.",
        "todayTnf": "NFL 11주차 TNF: 텍산스가 오늘 밤 콜츠를 상대합니다. 10주차 종료: 차저스 23-20 레이븐스.",
        "football_tagline": "TNF 11주차: 콜츠-텍산스 휴스턴서 AFC 남부 선두 격돌; 차저스는 하보 볼 23-20 승리 축하.",
        "football_liveNow": "오늘 밤: 콜츠 vs 텍산스 (20:15 ET, NRG 스타디움). 10주차 MNF: 차저스 23-20 레이븐스 (허버트 22야드 TD 러싱, 햄튼 105야드).",
        "football_pulse": "서스데이 나이트 풋볼: 콜츠와 텍산스가 11주차 AFC 남부 선두 자리를 놓고 격돌합니다",
        "tennis_tagline": "토리노 5일차: 즈베레프 vs 필스, 셸턴 vs 호다르 마지막 4강 티켓 쟁탈전.",
        "tennis_liveNow": "목요일 매켄로 조: 셸턴 vs 호다르 (14:00), 즈베레프 vs 필스 (20:30). 수요일 렌들 조: 알카라스, 메드베데프 6-2, 6-4 꺾고 준결승 안착.",
        "tennis_pulse": "토리노 ATP 파이널스: 매켄로 조 운명의 최종전, 셸턴과 필스가 즈베레프와 알카라스의 4강 파트너를 노립니다",
        "f1_tagline": "라스베이거스 GP 개막: 오늘 밤 네온사인 아래 스트립에서 공식 연습 주행 시작.",
        "f1_liveNow": "오늘 밤: FP1 (21:30 ET) & FP2 (01:00 ET). 드라이버 2위 싸움: 베르스타펜 279, 러셀 262, 해밀턴 261, 르클레르 249, 노리스 246 (안토넬리 390).",
        "f1_pulse": "라스베이거스 GP: 오늘 밤 스트립에서 연습 주행 시작, 2위 타이틀 쟁탈전 본격화",
        "soccer_tagline": "홀란의 극장 결승골로 네이션스리그 조별리그 마감; 이번 주 토요일 프리미어리그 재개.",
        "soccer_liveNow": "화요일: 노르웨이 3-2 덴마크 (홀란 88분); 웨일스 2-3 포르투갈. 월요일: 독일 5-0 네덜란드. 토요일 PL 재개: 아스널 27, 브라이튼 22, 맨시티 21.",
        "soccer_pulse": "축구 소식: 홀란의 극적인 결승골로 네이션스리그 조별리그 종료; 토요일 프리미어리그 복귀",
        "basketball_tagline": "야니스 친정팀에 27득점 폭격 히트 6연승 질주; 덴버는 보스턴에 17점 차 역전승.",
        "basketball_liveNow": "수요일: 히트 137-130 벅스 (야니스 27/14/9, 6연승); 너기츠 105-101 셀틱스 (요키치 24/9/8); 위저즈 103-99 랩터스 (데이비스 25/14).",
        "basketball_pulse": "NBA 수요일: 야니스가 친정팀 벅스 상대로 27/14/9 폭발, 히트 6연승 달성",
        "golf_tagline": "시 아일랜드서 RSM 클래식 1R 티오프: 2027 PGA 투어 시드권 걸린 최종 결전.",
        "golf_liveNow": "PGA 투어: 시 아일랜드서 1R 진행 중 (시사이드 & 플랜테이션). 125위 버블: 톰슨, 휴즈, 스모더먼, 다멘 출격.",
        "golf_pulse": "PGA 투어 피날레: 시 아일랜드서 1R 생중계, 125위 잔류를 향한 사투",
        "tonight": "목요일 데스크",
        "tonightBlurb": "서스데이 나이트: 텍산스가 콜츠를 안방 휴스턴으로 불러들여 11주차 개막. 토리노 5일차: 즈베레프-필스, 셸턴-호다르 준결승 진출 결정. 라스베이거스 GP: 오늘 밤 스트립 야간 주행. 골프: 시 아일랜드 1R 진행 중.",
        "f1Title": "라스베이거스 그랑프리: 오늘 밤 스트립에서 목요일 야간 연습 주행 스타트",
        "f1Blurb": "1,000마력 하이브리드 머신이 라스베이거스 스트립을 질주합니다: 챔피언 안토넬리(390) 뒤로 베르스타펜(279)부터 노리스(246)까지 33점 차."
    },
    "ar": {
        "todayDesk": "مكتب الخميس: مواجهة كولتس وتكسانز تفتتح الجولة 11. اليوم الخامس في تورينو يحسم مجموعة ماكنرو. انطلاق تجارب جائزة لاس فيغاس الليلة.",
        "todayNfl": "ليلة الخميس الليلة: كولتس في ضيافة تكسانز (8:15 مساء بتوقيت شرق أمريكا، هيوستن). حصاد الجولة 10: تشارجرز 23-20 ريفنز؛ لايونز 35-10 باتريوتس في ميونخ.",
        "todayTnf": "NFL الجولة 11: تكسانز يستضيف كولتس الليلة. انتهاء الجولة 10: تشارجرز 23-20 ريفنز.",
        "football_tagline": "قمة الجولة 11: صراع كولتس وتكسانز في هيوستن؛ تشارجرز يحتفل بالفوز 23-20 في مواجهة الإخوة.",
        "football_liveNow": "الليلة: كولتس في ضيافة تكسانز (8:15 مساء، هيوستن). الجولة 10 MNF: تشارجرز 23، ريفنز 20 (هربرت 22 ياردة، هامبتون 105 ياردات).",
        "football_pulse": "ليلة الخميس لكرة القدم الأمريكية: صراع الصدارة بين كولتس وتكسانز في افتتاح الجولة 11",
        "tennis_tagline": "نهائيات تورينو اليوم الخامس: زفيريف يواجه فيس بينما يلتقي شيلتون مع خودار لحسم آخر بطاقات المربع الذهبي.",
        "tennis_liveNow": "الخميس ماكنرو: شيلتون ضد خودار (14:00)، زفيريف ضد فيس (20:30). الأربعاء ليندل: ألكاراز يهزم ميدفيديف 6-2، 6-4 ويبلغ نصف النهائي.",
        "tennis_pulse": "نهائيات تورينو للتنس: جولة الحسم في مجموعة ماكنرو للالتحاق بزفيريف وألكاراز في نصف النهائي",
        "f1_tagline": "انطلاق جائزة لاس فيغاس: هدير المحركات يعلو الليلة على حلبة ستريب في التجارب الحرة الليلية.",
        "f1_liveNow": "الليلة: تجارب 1 (21:30 ET) وتجارب 2 (01:00 ET). صراع الوصافة: فيرستابن 279، راسل 262، هاميلتون 261، لوكلير 249، نوريس 246 (أنتونيللي 390).",
        "f1_pulse": "جائزة لاس فيغاس: انطلاق التجارب الحرة الليلة تحت الأضواء الكاشفة في حلبة ستريب",
        "soccer_tagline": "انتهاء دور المجموعات لدوري الأمم بهدف قاتل لهالاند؛ وعودة الدوري الإنجليزي السبت.",
        "soccer_liveNow": "الثلاثاء: النرويج 3-2 الدنمارك (هالاند 88)؛ ويلز 2-3 البرتغال. الاثنين: ألمانيا 5-0 هولندا. عودة الدوري السبت: أرسنال 27، برايتون 22، سيتي 21.",
        "soccer_pulse": "كرة القدم: ختام دوري الأمم بهدف هالاند الحاسم؛ والدوري الإنجليزي يعود يوم السبت",
        "basketball_tagline": "ميامي هيت يهزم باكس 137-130 بتألق يانيس؛ ودنفر يقلب تأخره بـ 17 نقطة أمام سلتيكس.",
        "basketball_liveNow": "الأربعاء: هيت 137-130 باكس (يانيس 27/14/9، 6 انتصارات متتالية)؛ ناغتس 105-101 سلتيكس (يوكيتش 24/9/8)؛ ويزاردز 103-99 رابتورز (ديفيس 25/14).",
        "basketball_pulse": "دوري السلة الأمريكي الأربعاء: يانيس يسجل 27 نقطة و14 متابعة ليقود هيت للفوز السادس تواليا أمام باكس",
        "golf_tagline": "انطلاق الجولة الأولى لبطولة آر إس إم كلاسيك في سي آيلاند لحسم بطاقات جولة 2027.",
        "golf_liveNow": "جولة البي جي إيه: الجولة الأولى جارية في سي آيلاند. صراع الـ 125: طومسون، هيوز، سموثيرمان، داهمن في الميدان.",
        "golf_pulse": "جولة البي جي إيه: انطلاق الجولة الأولى في سي آيلاند وصراع البقاء ضمن أفضل 125 لاعبا",
        "tonight": "مكتب الخميس",
        "tonightBlurb": "ليلة الخميس: تكسانز يستضيف كولتس في هيوستن لافتتاح الجولة 11. تورينو اليوم الخامس: زفيريف أمام فيس وشيلتون أمام خودار لحسم التأهل. جائزة لاس فيغاس: تجارب ليلية على حلبة ستريب. الجولف: الجولة الأولى مباشرة في سي آيلاند.",
        "f1Title": "جائزة لاس فيغاس الكبرى: المحركات تزأر الليلة على حلبة ستريب في التجارب الحرة",
        "f1Blurb": "سيارات الفورمولا 1 تنطلق في شوارع لاس فيغاس: 33 نقطة تفصل فيرستابن (279) عن نوريس (246) خلف البطل أنتونيللي (390)."
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

