# Update playground.ts, messages.ts, and messages-*.ts for 2026-11-21.
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
I18N = os.path.join(ROOT, "frontend", "src", "i18n")

# 1. Update playground.ts
playground_path = os.path.join(I18N, "playground.ts")
pg_txt = open(playground_path, "r", encoding="utf-8").read()

pg_updates = {
    "en": {
        "pinFinal": "Turin Sat Semifinals: Alcaraz vs Shelton (14:00 CET), Zverev vs Medvedev (20:30 CET). Finalists decided today at Inalpi Arena.",
        "plFootnote": "Live: Man City 0-1 Fulham (Muniz 16). Today: Newcastle vs Arsenal (17:30 GMT). Table: Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "TNF Final: Texans 26, Colts 3 at NRG Stadium (Stroud 2 TDs, defense forces 3 turnovers). Next: Sunday Week 11 slate.",
        "week1Sub": "Houston takes full command of AFC South with 26-3 rout. Sunday: Chiefs at Panthers, 49ers at Packers, Eagles at Rams.",
        "countdownTnf": "TNF FINAL: Texans 26-3 Colts. Week 11 TNF complete. Sunday kickoff: 1:00 PM ET FOX/CBS.",
        "majorsDone": "The RSM Classic Moving Day LIVE at Sea Island: Thorbjornsen, Penge, Neergaard-Petersen -9. Cut made at -2.",
        "gridAfterMadrid": "Round 21 · Las Vegas GP 50-Lap Main Race Tonight (22:00 PST / 01:00 ET Sun)",
    },
    "fr": {
        "pinFinal": "Turin sam demies : Alcaraz vs Shelton (14h00), Zverev vs Medvedev (20h30). Les finalistes decident aujourd'hui a l'Inalpi Arena.",
        "plFootnote": "En direct : Man City 0-1 Fulham (Muniz 16e). Ce samedi : Newcastle vs Arsenal (17h30 GMT). Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "TNF Termine : Texans 26, Colts 3 au NRG Stadium (Stroud 2 TD, la defense provoque 3 pertes de balle). Suite : dimanche Semaine 11.",
        "week1Sub": "Houston prend les commandes de l'AFC Sud avec ce 26-3. Dimanche : Chiefs chez les Panthers, 49ers chez les Packers.",
        "countdownTnf": "TNF TERMINE : Texans 26-3 Colts. Rendez-vous dimanche des 13h00 ET.",
        "majorsDone": "RSM Classic Moving Day EN DIRECT a Sea Island : Thorbjornsen, Penge, Neergaard-Petersen -9. Cut passe a -2.",
        "gridAfterMadrid": "Manche 21 · Course principale de 50 tours du GP de Las Vegas ce soir (22h00 PST / 07h00 Paris)",
    },
    "es": {
        "pinFinal": "Turin sab semifinales: Alcaraz vs Shelton (14:00), Zverev vs Medvedev (20:30). Los finalistas se deciden hoy en el Inalpi Arena.",
        "plFootnote": "En vivo: Man City 0-1 Fulham (Muniz 16). Hoy: Newcastle vs Arsenal (17:30 GMT). Tabla: Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "TNF Final: Texans 26, Colts 3 en NRG Stadium (Stroud 2 TD, defensa fuerza 3 entregas). Proximo: domingo Semana 11.",
        "week1Sub": "Houston toma el mando total de la AFC Sur con paliza 26-3. Domingo: Chiefs en Panthers, 49ers en Packers.",
        "countdownTnf": "TNF FINAL: Texans 26-3 Colts. Fin del TNF. Domingo de NFL desde las 13:00 ET.",
        "majorsDone": "The RSM Classic Moving Day EN VIVO en Sea Island: Thorbjornsen, Penge, Neergaard-Petersen -9. Corte en -2.",
        "gridAfterMadrid": "Ronda 21 · Carrera nocturna de 50 vueltas del GP de Las Vegas esta noche (22:00 PST)",
    },
    "de": {
        "pinFinal": "Turin Sa Halbfinale: Alcaraz vs Shelton (14:00), Zverev vs Medwedew (20:30). Finalisten werden heute in der Inalpi Arena ermittelt.",
        "plFootnote": "Live: Man City 0-1 Fulham (Muniz 16.). Heute: Newcastle vs Arsenal (17:30 GMT). Tabelle: Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "TNF Endstand: Texans 26, Colts 3 im NRG Stadium (Stroud 2 TDs, Defensive erzwingt 3 Ballverluste). Weiter: Sonntag Woche 11.",
        "week1Sub": "Houston uebernimmt AFC South Fuehrung nach 26:3. Sonntag: Chiefs bei den Panthers, 49ers bei den Packers.",
        "countdownTnf": "TNF ENDSTAND: Texans 26-3 Colts. Woche 11 TNF beendet. Sonntag Kickoff: 1:00 PM ET.",
        "majorsDone": "RSM Classic Moving Day LIVE in Sea Island: Thorbjornsen, Penge, Neergaard-Petersen -9. Cut bei -2.",
        "gridAfterMadrid": "Runde 21 · Las Vegas GP 50-Runden-Hauptrennen heute Nacht (22:00 PST / 07:00 MEZ)",
    },
    "it": {
        "pinFinal": "Torino sab semifinali: Alcaraz vs Shelton (14:00), Zverev vs Medvedev (20:30). Oggi si decidono i finalisti all'Inalpi Arena.",
        "plFootnote": "Live: Man City 0-1 Fulham (Muniz 16'). Oggi: Newcastle vs Arsenal (17:30 GMT). Classifica: Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "TNF Finale: Texans 26, Colts 3 all'NRG Stadium (Stroud 2 TD, difesa forza 3 palle perse). Prossimo: domenica Week 11.",
        "week1Sub": "Houston prende il comando dell'AFC South con il 26-3. Domenica: Chiefs a Carolina, 49ers a Green Bay.",
        "countdownTnf": "TNF FINALE: Texans 26-3 Colts. Week 11 TNF completato. Kickoff domenica: 19:00 italiane.",
        "majorsDone": "RSM Classic Moving Day LIVE a Sea Island: Thorbjornsen, Penge, Neergaard-Petersen -9. Taglio a -2.",
        "gridAfterMadrid": "Round 21 · Gara notturna di 50 giri del GP di Las Vegas stanotte (22:00 PST / 07:00 CET)",
    },
    "pl": {
        "pinFinal": "Turyn sob polfinaly: Alcaraz vs Shelton (14:00), Zverev vs Miedwiediew (20:30). Wylonienie finalistow w Inalpi Arena.",
        "plFootnote": "Na zywo: Man City 0-1 Fulham (Muniz 16). Dzis: Newcastle vs Arsenal (17:30 GMT). Tabela: Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "TNF Koniec: Texans 26, Colts 3 na NRG Stadium (Stroud 2 TD, obrona wymusza 3 straty). Dalej: niedziela 11. tygodnia.",
        "week1Sub": "Houston przejmuje kontrole nad AFC South po pogromie 26:3. Niedziela: Chiefs u Panthers, 49ers u Packers.",
        "countdownTnf": "TNF KONIEC: Texans 26-3 Colts. TNF 11. tygodnia zakonczony. Niedzielny start: 19:00 czasu polskiego.",
        "majorsDone": "RSM Classic Moving Day NA ZYWO w Sea Island: Thorbjornsen, Penge, Neergaard-Petersen -9. Cut na -2.",
        "gridAfterMadrid": "Runda 21 · Wyscig glowny 50 okrazen GP Las Vegas dzis w nocy (22:00 PST)",
    },
    "zh": {
        "pinFinal": "都灵周六半决赛：阿尔卡拉斯对谢尔顿（14:00），兹维列夫对梅德韦杰夫（20:30）。决赛名额今日揭晓。",
        "plFootnote": "进行中：曼城0-1富勒姆（穆尼斯16分）。今日：纽卡斯尔对阿森纳（17:30 GMT）。榜首阿森纳27，布莱顿22，曼城21。",
        "week1Closed": "TNF战报：德州人26-3大胜小马（斯特劳德2达阵，防守迫使3次失误）。周日第11周大战待续。",
        "week1Sub": "休斯敦26-3狂胜掌控美联南区。周日焦点：酋长客战黑豹，49人客战包装工。",
        "countdownTnf": "TNF完赛：德州人26-3小马。周四夜赛落幕，周日比赛美东时间下午1点开打。",
        "majorsDone": "RSM精英赛移动日海岛球场进行中：索比约恩森、彭奇、尼尔高-彼得森-9并列领跑，晋级线-2。",
        "gridAfterMadrid": "第21站 · 拉斯维加斯大奖赛今晚打响50圈正赛夜战（当地时间22:00）",
    },
    "ja": {
        "pinFinal": "トリノ土曜準決勝：アルカラス対シェルトン（14:00）、ズベレフ対メドベージェフ（20:30）。決勝進出者が決定。",
        "plFootnote": "生中継：マンC 0-1 フラム（ムニス16分）。本日：ニューカッスル対アーセナル（17:30 GMT）。首位アーセナル27、ブライトン22、シティ21。",
        "week1Closed": "TNF終了：テキサンズ26-3コルツ（ストラウド2TD、守備陣が3ターンオーバーを誘発）。日曜の第11週本番へ。",
        "week1Sub": "ヒューストンが26-3の完勝でAFC南部地区首位を堅持。日曜日：チーフス対パンサーズ、49ers対パッカーズ。",
        "countdownTnf": "TNF終了：テキサンズ 26-3 コルツ。第11週TNF終了。日曜キックオフ：米東部13:00。",
        "majorsDone": "RSMクラシック・ムービングデー生中継：ソービョルンセン、ペンジ、ニアガード＝ペテルセンが-9首位。カットは-2。",
        "gridAfterMadrid": "第21戦 · 今夜ラスベガスGP 50周の決勝ナイトレース（現地22:00）",
    },
    "ko": {
        "pinFinal": "토리노 토요일 준결승: 알카라스 vs 셸턴 (14:00), 츠베레프 vs 메드베데프 (20:30). 결승 진출자 오늘 확정.",
        "plFootnote": "라이브: 맨시티 0-1 풀럼 (무니스 16분). 오늘: 뉴캐슬 vs 아스널 (17:30 GMT). 아스널 27, 브라이튼 22, 맨시티 21.",
        "week1Closed": "TNF 최종: 텍산스 26, 콜츠 3 (스트라우드 2 TD, 수비진 턴오버 3개 유도). 다음은 11주차 일요일 경기.",
        "week1Sub": "휴스턴 26-3 대승으로 AFC 남부 독주. 일요일: 치프스 vs 팬서스, 49ers vs 패커스.",
        "countdownTnf": "TNF 최종: 텍산스 26-3 콜츠. 11주차 TNF 종료. 일요일 킥오프: 미 동부 오후 1시.",
        "majorsDone": "RSM 클래식 무빙데이 라이브: 소르비욘센, 펜지, 네어가르-페테르센 -9 공동 선두. 컷 -2 통과.",
        "gridAfterMadrid": "21라운드 · 오늘 밤 라스베이거스 GP 50랩 결선 나이트 레이스 (현지 22:00)",
    },
    "ar": {
        "pinFinal": "تورينو السبت نصف النهائي: ألكاراز ضد شيلتون (14:00)، زفيريف ضد ميدفيديف (20:30). تحديد طرفي النهائي اليوم.",
        "plFootnote": "مباشر: مانشستر سيتي 0-1 فولهام (مونيز 16). اليوم: نيوكاسل ضد أرسنال (17:30 بتوقيت غرينتش). أرسنال 27، برايتون 22، سيتي 21.",
        "week1Closed": "ختام ليلة الخميس: تكسانز 26، كولتس 3 (سترود 2 هبوط، الدفاع يجبر الخصم على 3 أخطاء). التالي: مواجهات الأحد.",
        "week1Sub": "هيوستن يحكم قبضته على الجنوب الأمريكي بفوز كاسح 26-3. الأحد: تشيفز ضد بانثرز، 49ers ضد باكرز.",
        "countdownTnf": "نهاية ليلة الخميس: تكسانز 26-3 كولتس. انطلاق مباريات الأحد 1:00 ظهرا بتوقيت شرق أمريكا.",
        "majorsDone": "يوم الحسم لبطولة آر إس إم كلاسيك مباشرة: ثوربيورنسن، بينجي، نيرغارد في الصدارة بـ -9. اجتياز القص عند -2.",
        "gridAfterMadrid": "الجولة 21 · سباق جائزة لاس فيغاس الكبرى الليلي من 50 لفة الليلة (22:00 بالتوقيت المحلي)",
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
    "todayDesk": "Saturday desk: Turin Semifinals (Alcaraz vs Shelton 14:00, Zverev vs Medvedev 20:30). Las Vegas GP 50-lap night race tonight. PL restarts (Man City 0-1 Fulham live; Newcastle vs Arsenal). RSM Classic Moving Day live.",
    "todayNfl": "TNF Final: Texans 26, Colts 3 (Stroud 2 TDs, defense forces 3 turnovers). Sunday Week 11 up next: Chiefs at Panthers, 49ers at Packers.",
    "todayTnf": "NFL Week 11 TNF Final: Texans 26-3 Colts at NRG Stadium. Texans (7-4) take command of AFC South.",
    "football_tagline": "TNF Final: Texans throttle Colts 26-3 behind Stroud and stifling defense; Sunday Week 11 slate looms.",
    "football_liveNow": "TNF Final: Texans 26, Colts 3 (Stroud 22/31, 248 yds, 2 TDs; Richardson held to 112 yds, 2 INTs). Sunday: Chiefs at Panthers, 49ers at Packers.",
    "football_pulse": "NFL WEEK 11: TEXANS ROUT COLTS 26-3 TO SEIZE AFC SOUTH COMMAND; SUNDAY SLATE ON DECK",
    "tennis_tagline": "Turin Super Saturday: Alcaraz faces Shelton at 14:00 CET before Zverev clashes with Medvedev at 20:30 CET.",
    "tennis_liveNow": "Turin Semifinals: Alcaraz vs Shelton (14:00 CET), Zverev vs Medvedev (20:30 CET). Friday McEnroe: Zverev d Fils 6-4, 7-6(5); Shelton d Jodar 6-3, 6-4.",
    "tennis_pulse": "NITTO ATP FINALS: SUPER SATURDAY IN TURIN AS ALCARAZ, SHELTON, ZVEREV AND MEDVEDEV BATTLE FOR FINALS",
    "f1_tagline": "Las Vegas GP Main Race Tonight: Verstappen lines up on pole alongside Russell under the neon lights.",
    "f1_liveNow": "Tonight: 50-Lap Race (22:00 local / 01:00 ET Sun). Grid: Verstappen P1, Russell P2, Leclerc P3, Norris P4. Antonelli 5-place penalty (starts P6). Drivers P2 battle: Verstappen 279, Russell 262, Norris 246.",
    "f1_pulse": "LAS VEGAS GP: VERSTAPPEN INHERITS POLE ALONGSIDE RUSSELL AS 50-LAP STRIP NIGHT RACE ROARS TONIGHT",
    "soccer_tagline": "Premier League restarts: Fulham stun Man City early at Etihad; leaders Arsenal visit Newcastle later today.",
    "soccer_liveNow": "Live: Man City 0-1 Fulham (Muniz 16). Later: Newcastle vs Arsenal (17:30 GMT), Chelsea vs Leeds (15:00 GMT). Table: Arsenal 27, Brighton 22, Man City 21.",
    "soccer_pulse": "SOCCER: PREMIER LEAGUE RETURNS AS FULHAM LEAD AT ETIHAD AND LEAGUE LEADERS ARSENAL TRAVEL TO NEWCASTLE",
    "basketball_tagline": "Lakers survive late scare to edge Kings 106-104; Jokic posts 32-point triple-double in Nuggets victory.",
    "basketball_liveNow": "Friday: Lakers 106-104 Kings (Reaves clutch FTs, Fox 29); Nuggets 133-124 Rockets (Jokic 32/12/10); Cavaliers 128-119 Pacers. Thursday: Spurs beat Warriors 118-106.",
    "basketball_pulse": "NBA FRIDAY: LAKERS EDGE KINGS 106-104 IN SACRAMENTO THRILLER AS JOKIC POWERS NUGGETS PAST ROCKETS",
    "golf_tagline": "The RSM Classic Moving Day live at Sea Island: Three share 9-under lead as cut falls at 2-under.",
    "golf_liveNow": "PGA Tour: Round 3 Moving Day live at Sea Island (Seaside). Co-leaders at -9: Thorbjornsen, Penge, Neergaard-Petersen. Cut made at -2 (65 players). Top 125 card race active.",
    "golf_pulse": "PGA TOUR FALL FINALE: ROUND 3 MOVING DAY UNDERWAY AT SEA ISLAND IN FIGHT FOR 2027 CARDS",
    "tonight": "Saturday desk",
    "tonightBlurb": "Turin Semifinals: Alcaraz vs Shelton at 14:00 CET and Zverev vs Medvedev at 20:30 CET. Las Vegas GP: 50-lap night race tonight with Verstappen on pole. Premier League: Fulham lead Man City 1-0 early at Etihad; Arsenal visit Newcastle at 17:30 GMT. Golf: Round 3 Moving Day live at Sea Island.",
    "f1Title": "Las Vegas Grand Prix: Verstappen lines up on pole for tonight 50-lap night race on the Strip",
    "f1Blurb": "The neon shootout on Las Vegas Boulevard begins tonight at 22:00 local time: Verstappen starts on pole ahead of Russell, with 33 points covering Verstappen (279) to Norris (246) in the fight for P2."
}

msg_fr = {
    "todayDesk": "Bureau du samedi : Demies a Turin (Alcaraz vs Shelton 14h00, Zverev vs Medvedev 20h30). Course de nuit du GP de Las Vegas ce soir. Reprise de la Premier League (Man City 0-1 Fulham en direct). Moving Day du RSM Classic.",
    "todayNfl": "TNF Termine : Texans 26, Colts 3 (Stroud 2 TD, la defense provoque 3 pertes de balle). Suite de la Semaine 11 dimanche : Chiefs chez les Panthers, 49ers chez les Packers.",
    "todayTnf": "NFL Semaine 11 TNF Termine : Texans 26-3 Colts au NRG Stadium. Houston (7-4) prend les commandes de l'AFC Sud.",
    "football_tagline": "TNF Termine : Les Texans etouffent les Colts 26-3 avec Stroud et une defense imperiale ; la suite dimanche.",
    "football_liveNow": "TNF Termine : Texans 26, Colts 3 (Stroud 22/31, 248 yds, 2 TD ; Richardson limite a 112 yds, 2 INT). Dimanche : Chiefs chez les Panthers, 49ers chez les Packers.",
    "football_pulse": "NFL SEMAINE 11 : LES TEXANS SURCLASSENT LES COLTS 26-3 ET PRENNENT LA MAIN SUR L'AFC SUD",
    "tennis_tagline": "Super Samedi a Turin : Alcaraz defie Shelton a 14h00 avant le grand choc Zverev contre Medvedev a 20h30.",
    "tennis_liveNow": "Demies a Turin : Alcaraz vs Shelton (14h00), Zverev vs Medvedev (20h30). Vendredi McEnroe : Zverev bat Fils 6-4, 7-6(5) ; Shelton bat Jodar 6-3, 6-4.",
    "tennis_pulse": "NITTO ATP FINALS : SUPER SAMEDI A TURIN OU ALCARAZ, SHELTON, ZVEREV ET MEDVEDEV VISENT LA FINALE",
    "f1_tagline": "Course nocturne du GP de Las Vegas ce soir : Verstappen en pole position aux cotes de Russell sous les neons.",
    "f1_liveNow": "Ce soir : Course de 50 tours (22h00 PST / 07h00 Paris). Grille : Verstappen P1, Russell P2, Leclerc P3, Norris P4. Penalite pour Antonelli (P6). Bataille P2 : Verstappen 279, Russell 262, Norris 246.",
    "f1_pulse": "GP DE LAS VEGAS : VERSTAPPEN HERITE DE LA POLE DEVANT RUSSELL POUR LE DEPART DE LA COURSE CE SOIR",
    "soccer_tagline": "Reprise de la Premier League : Fulham surprend City d'entree a l'Etihad ; le leader Arsenal a Newcastle tout a l'heure.",
    "soccer_liveNow": "En direct : Man City 0-1 Fulham (Muniz 16e). Ce samedi : Newcastle vs Arsenal (17h30 GMT), Chelsea vs Leeds (15h00 GMT). Arsenal 27, Brighton 22, City 21.",
    "soccer_pulse": "FOOTBALL : LA PREMIER LEAGUE REPREND SES DROITS AVEC FULHAM EN TETE A L'ETIHAD ET ARSENAL A NEWCASTLE",
    "basketball_tagline": "Les Lakers resistent et battent les Kings 106-104 ; Jokic empile un triple-double a 32 points avec Denver.",
    "basketball_liveNow": "Vendredi : Lakers 106-104 Kings (lancers de Reaves, Fox 29) ; Nuggets 133-124 Rockets (Jokic 32/12/10) ; Cavaliers 128-119 Pacers.",
    "basketball_pulse": "NBA VENDREDI : LES LAKERS DOMINENT LES KINGS 106-104 A SACRAMENTO PENDANT QUE JOKIC GUIDE DENVER",
    "golf_tagline": "RSM Classic Moving Day en direct a Sea Island : Trois leaders a -9, le cut passe a -2.",
    "golf_liveNow": "PGA Tour : 3e tour Moving Day en direct a Sea Island (Seaside). Leaders a -9 : Thorbjornsen, Penge, Neergaard-Petersen. Cut a -2 (65 joueurs qualifies).",
    "golf_pulse": "PGA TOUR FALL FINALE : 3E TOUR MOVING DAY EN DIRECT A SEA ISLAND DANS LA BATAILLE POUR LES CARTES 2027",
    "tonight": "Bureau du samedi",
    "tonightBlurb": "Demies a Turin : Alcaraz affronte Shelton a 14h00 et Zverev defie Medvedev a 20h30. GP de Las Vegas : 50 tours de nuit avec Verstappen en pole. Premier League : Fulham mene 1-0 a l'Etihad ; Arsenal a Newcastle a 17h30 GMT. Golf : 3e tour en direct a Sea Island.",
    "f1Title": "Grand Prix de Las Vegas : Verstappen en pole position pour les 50 tours nocturnes sur le Strip",
    "f1Blurb": "Le duel nocturne de Las Vegas Boulevard demarre ce soir a 22h00 locales : Verstappen en pole devant Russell, avec 33 points d'ecart entre Verstappen (279) et Norris (246) pour la place de dauphin."
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
        "todayDesk": "Mesa del sabado: Semifinales en Turin (Alcaraz vs Shelton 14:00, Zverev vs Medvedev 20:30). Carrera nocturna del GP de Las Vegas esta noche. Vuelve la Premier League (Man City 0-1 Fulham en vivo). Moving Day del RSM Classic.",
        "todayNfl": "TNF Final: Texans 26, Colts 3 (Stroud 2 TD, defensa fuerza 3 entregas). Domingo Semana 11: Chiefs en Panthers, 49ers en Packers.",
        "todayTnf": "NFL Semana 11 TNF Final: Texans 26-3 Colts en NRG Stadium. Houston (7-4) toma el mando de la AFC Sur.",
        "football_tagline": "TNF Final: Texans aplastan 26-3 a Colts con Stroud y gran defensa; todo listo para el domingo.",
        "football_liveNow": "TNF Final: Texans 26, Colts 3 (Stroud 22/31, 248 yds, 2 TD; Richardson frenado en 112 yds, 2 INT). Domingo: Chiefs en Panthers, 49ers en Packers.",
        "football_pulse": "NFL SEMANA 11: TEXANS GOLEAN 26-3 A COLTS Y ASUMEN EL LIDERATO DE LA AFC SUR",
        "tennis_tagline": "Super Sabado en Turin: Alcaraz enfrenta a Shelton a las 14:00 CET antes del clasico Zverev ante Medvedev a las 20:30 CET.",
        "tennis_liveNow": "Semifinales de Turin: Alcaraz vs Shelton (14:00 CET), Zverev vs Medvedev (20:30 CET). Viernes: Zverev d Fils 6-4, 7-6(5); Shelton d Jodar 6-3, 6-4.",
        "tennis_pulse": "NITTO ATP FINALS: SUPER SABADO EN TURIN CON ALCARAZ, SHELTON, ZVEREV Y MEDVEDEV EN BUSCA DE LA FINAL",
        "f1_tagline": "Carrera del GP de Las Vegas esta noche: Verstappen larga en pole junto a Russell bajo las luces de neon.",
        "f1_liveNow": "Esta noche: Carrera a 50 vueltas (22:00 PST). Parrilla: Verstappen P1, Russell P2, Leclerc P3, Norris P4. Sancion a Antonelli (P6). Lucha P2: Verstappen 279, Russell 262, Norris 246.",
        "f1_pulse": "GP DE LAS VEGAS: VERSTAPPEN HEREDA LA POLE JUNTO A RUSSELL PARA LA NOCHE DE CARRERA EN EL STRIP",
        "soccer_tagline": "Vuelve la Premier League: Fulham sorprende al City en el Etihad; el lider Arsenal visita al Newcastle esta tarde.",
        "soccer_liveNow": "En vivo: Man City 0-1 Fulham (Muniz 16). Hoy: Newcastle vs Arsenal (17:30 GMT), Chelsea vs Leeds (15:00 GMT). Tabla: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "FUTBOL: VUELVE LA PREMIER LEAGUE CON EL FULHAM ADELANTE EN EL ETIHAD Y ARSENAL RUMBO A NEWCASTLE",
        "basketball_tagline": "Lakers resisten y vencen 106-104 a Kings en Sacramento; Jokic firma triple-doble de 32 puntos con Denver.",
        "basketball_liveNow": "Viernes: Lakers 106-104 Kings (tiros libres de Reaves, Fox 29); Nuggets 133-124 Rockets (Jokic 32/12/10); Cavaliers 128-119 Pacers.",
        "basketball_pulse": "NBA VIERNES: LAKERS SUPERAN 106-104 A KINGS EN FINAL DE INFARTO MIENTRAS JOKIC GUIA A DENVER",
        "golf_tagline": "The RSM Classic Moving Day en vivo en Sea Island: Tres lideres en -9, corte superado en -2.",
        "golf_liveNow": "PGA Tour: Ronda 3 Moving Day en vivo en Sea Island (Seaside). Colideres en -9: Thorbjornsen, Penge, Neergaard-Petersen. Corte en -2 (65 jugadores).",
        "golf_pulse": "PGA TOUR FALL FINALE: TERCERA RONDA MOVING DAY EN MARCHA EN SEA ISLAND POR LAS TARJETAS 2027",
        "tonight": "Mesa del sabado",
        "tonightBlurb": "Semifinales de Turin: Alcaraz vs Shelton a las 14:00 CET y Zverev vs Medvedev a las 20:30 CET. GP de Las Vegas: 50 vueltas esta noche con Verstappen en pole. Premier League: Fulham vence 1-0 al City de inicio; Arsenal en Newcastle a las 17:30 GMT. Golf: Ronda 3 en Sea Island.",
        "f1Title": "Gran Premio de Las Vegas: Verstappen en pole para la carrera nocturna a 50 vueltas en el Strip",
        "f1Blurb": "El espectaculo nocturno en Las Vegas Boulevard arranca a las 22:00 hora local: Verstappen parte en pole por delante de Russell, con 33 puntos entre Verstappen (279) y Norris (246) por el subcampeonato."
    },
    "de": {
        "todayDesk": "Samstags-Desk: Halbfinale in Turin (Alcaraz vs Shelton 14:00, Zverev vs Medwedew 20:30). Las Vegas GP 50-Runden-Nachtrennen heute Nacht. Premier League Rueckkehr (Man City 0:1 Fulham live). RSM Classic Moving Day live.",
        "todayNfl": "TNF Endstand: Texans 26, Colts 3 (Stroud 2 TDs, Defensive erzwingt 3 Ballverluste). Sonntag Woche 11 folgt: Chiefs bei den Panthers, 49ers bei den Packers.",
        "todayTnf": "NFL Woche 11 TNF Endstand: Texans 26-3 Colts im NRG Stadium. Texans (7-4) uebernehmen AFC South Fuehrung.",
        "football_tagline": "TNF Endstand: Texans fertigen Colts mit 26:3 ab dank Stroud und dominanter Defensive; Sonntag naht.",
        "football_liveNow": "TNF Endstand: Texans 26, Colts 3 (Stroud 22/31, 248 Yds, 2 TDs; Richardson bei 112 Yds, 2 INTs gehalten). Sonntag: Chiefs bei Panthers, 49ers bei Packers.",
        "football_pulse": "NFL WOCHE 11: TEXANS DEMONTIEREN COLTS MIT 26:3 UND EROBERN DIE AFC SOUTH SPITZE",
        "tennis_tagline": "Super-Samstag in Turin: Alcaraz trifft um 14:00 Uhr auf Shelton vor dem Klassiker Zverev gegen Medwedew um 20:30 Uhr.",
        "tennis_liveNow": "Turin Halbfinale: Alcaraz vs Shelton (14:00 MEZ), Zverev vs Medwedew (20:30 MEZ). Freitag: Zverev d Fils 6-4, 7-6(5); Shelton d Jodar 6-3, 6-4.",
        "tennis_pulse": "NITTO ATP FINALS: SUPER-SAMSTAG IN TURIN WO ALCARAZ, SHELTON, ZVEREV UND MEDWEDEW UMS ENDSPIEL KAEMPFEN",
        "f1_tagline": "Las Vegas GP Hauptrennen heute Nacht: Verstappen startet im Flutlicht von der Pole Position neben Russell.",
        "f1_liveNow": "Heute Nacht: 50-Runden-Rennen (22:00 PST / 07:00 MEZ). Startaufstellung: Verstappen P1, Russell P2, Leclerc P3, Norris P4. Antonelli Strafe (Start P6). P2 Duell: Verstappen 279, Russell 262, Norris 246.",
        "f1_pulse": "LAS VEGAS GP: VERSTAPPEN ERBT DIE POLE POSITION NEBEN RUSSELL FUER DAS NACHTRENNEN AUF DEM STRIP",
        "soccer_tagline": "Premier League Comeback: Fulham schockt City frueh im Etihad; Tabellenfuehrer Arsenal gastiert spaeter in Newcastle.",
        "soccer_liveNow": "Live: Man City 0:1 Fulham (Muniz 16.). Heute: Newcastle vs Arsenal (17:30 GMT), Chelsea vs Leeds (15:00 GMT). Tabelle: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "FUSSBALL: PREMIER LEAGUE ZURUECK MIT FULHAM-FUEHRUNG IM ETIHAD UND ARSENAL-GASPTSPIEL IN NEWCASTLE",
        "basketball_tagline": "Lakers retten 106:104-Krimi in Sacramento; Jokic glaenzt mit 32-Punkte-Triple-Double fuer Denver.",
        "basketball_liveNow": "Freitag: Lakers 106-104 Kings (Reaves Freiwuerfe, Fox 29); Nuggets 133-124 Rockets (Jokic 32/12/10); Cavaliers 128-119 Pacers.",
        "basketball_pulse": "NBA FREITAG: LAKERS SCHLAGEN KINGS 106:104 IN SACRAMENTO WAEHREND JOKIC NUGGETS ZUM SIEG FUEHRT",
        "golf_tagline": "The RSM Classic Moving Day live in Sea Island: Drei fuehren bei -9, Cut faellt bei -2.",
        "golf_liveNow": "PGA Tour: Runde 3 Moving Day live in Sea Island (Seaside). Führende bei -9: Thorbjornsen, Penge, Neergaard-Petersen. Cut bei -2 (65 Profis). Kampf um Tourkarten 2027.",
        "golf_pulse": "PGA TOUR FALL FINALE: 3. RUNDE MOVING DAY IN SEA ISLAND IM KAMPF UM DIE TOURKARTEN 2027",
        "tonight": "Samstags-Desk",
        "tonightBlurb": "Halbfinale in Turin: Alcaraz gegen Shelton um 14:00 Uhr MEZ und Zverev gegen Medwedew um 20:30 Uhr MEZ. Las Vegas GP: 50-Runden-Nachtrennen mit Verstappen auf Pole. Premier League: Fulham fuehrt 1:0 im Etihad; Arsenal in Newcastle um 17:30 GMT. Golf: Moving Day in Sea Island.",
        "f1Title": "Grosser Preis von Las Vegas: Verstappen auf Pole Position fuer das 50-Runden-Nachtrennen auf dem Strip",
        "f1Blurb": "Das Nachtrennen auf dem Las Vegas Boulevard beginnt um 22:00 Uhr Ortszeit: Verstappen startet vor Russell, waehrend 33 Punkte Verstappen (279) und Norris (246) im Kampf um Rang zwei trennen."
    },
    "it": {
        "todayDesk": "Desk del sabato: Semifinali a Torino (Alcaraz vs Shelton 14:00, Zverev vs Medvedev 20:30). Gara notturna del GP di Las Vegas stanotte. Riparte la Premier League (Man City 0-1 Fulham live). Moving Day del RSM Classic.",
        "todayNfl": "TNF Finale: Texans 26, Colts 3 (Stroud 2 TD, difesa forza 3 turnover). Domenica Week 11 in arrivo: Chiefs a Carolina, 49ers a Green Bay.",
        "todayTnf": "NFL Week 11 TNF Finale: Texans 26-3 Colts all'NRG Stadium. Houston (7-4) prende il comando dell'AFC South.",
        "football_tagline": "TNF Finale: I Texans travolgono i Colts 26-3 con Stroud e una difesa insuperabile; attesa per la domenica.",
        "football_liveNow": "TNF Finale: Texans 26, Colts 3 (Stroud 22/31, 248 yds, 2 TD; Richardson fermato a 112 yds, 2 INT). Domenica: Chiefs a Carolina, 49ers a Green Bay.",
        "football_pulse": "NFL WEEK 11: I TEXANS DOMINANO I COLTS 26-3 E CONQUISTANO LA VETTA DELL'AFC SOUTH",
        "tennis_tagline": "Super Sabato a Torino: Alcaraz affronta Shelton alle 14:00 prima della grande sfida Zverev-Medvedev alle 20:30.",
        "tennis_liveNow": "Semifinali Torino: Alcaraz vs Shelton (14:00 CET), Zverev vs Medvedev (20:30 CET). Venerdi: Zverev b. Fils 6-4, 7-6(5); Shelton b. Jodar 6-3, 6-4.",
        "tennis_pulse": "NITTO ATP FINALS: SUPER SABATO A TORINO CON ALCARAZ, SHELTON, ZVEREV E MEDVEDEV A CACCIA DELLA FINALE",
        "f1_tagline": "Gara del GP di Las Vegas stanotte: Verstappen in pole accanto a Russell sotto le luci scintillanti della Strip.",
        "f1_liveNow": "Stanotte: Gara di 50 giri (22:00 PST / 07:00 italiane). Griglia: Verstappen P1, Russell P2, Leclerc P3, Norris P4. Penalita Antonelli (P6). Duello P2: Verstappen 279, Russell 262, Norris 246.",
        "f1_pulse": "GP DI LAS VEGAS: VERSTAPPEN EREDITA LA POLE ACCANTO A RUSSELL PER LA SFIDA NOTTURNA SULLA STRIP",
        "soccer_tagline": "Ritorno della Premier League: Fulham avanti a sorpresa all'Etihad sul City; la capolista Arsenal a Newcastle alle 17:30 GMT.",
        "soccer_liveNow": "Live: Man City 0-1 Fulham (Muniz 16'). Oggi: Newcastle vs Arsenal (17:30 GMT), Chelsea vs Leeds (15:00 GMT). Classifica: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "CALCIO: RIPARTE LA PREMIER LEAGUE CON IL FULHAM AVANTI ALL'ETIHAD E L'ARSENAL DI SCENA A NEWCASTLE",
        "basketball_tagline": "I Lakers superano i Kings 106-104 nel finale a Sacramento; Jokic firma una tripla doppia da 32 punti per Denver.",
        "basketball_liveNow": "Venerdi: Lakers 106-104 Kings (liberi di Reaves, Fox 29); Nuggets 133-124 Rockets (Jokic 32/12/10); Cavaliers 128-119 Pacers.",
        "basketball_pulse": "NBA VENERDI: LAKERS DI MISURA SUI KINGS 106-104 MENTRE JOKIC TRASCINA I NUGGETS CONTRO HOUSTON",
        "golf_tagline": "The RSM Classic Moving Day live a Sea Island: Tre in testa a -9, taglio fissato a -2.",
        "golf_liveNow": "PGA Tour: 3° giro Moving Day live a Sea Island (Seaside). Leader a -9: Thorbjornsen, Penge, Neergaard-Petersen. Taglio a -2 (65 giocatori). Carte 2027 in palio.",
        "golf_pulse": "PGA TOUR FALL FINALE: 3° GIRO MOVING DAY A SEA ISLAND NELLA CORSA ALLE CARTE DEL CIRCUITO 2027",
        "tonight": "Desk del sabato",
        "tonightBlurb": "Semifinali Torino: Alcaraz contro Shelton alle 14:00 CET e Zverev contro Medvedev alle 20:30 CET. GP Las Vegas: 50 giri notturni con Verstappen in pole. Premier League: Fulham avanti 1-0 all'Etihad; Arsenal a Newcastle alle 17:30 GMT. Golf: Moving Day a Sea Island.",
        "f1Title": "Gran Premio di Las Vegas: Verstappen in pole position per i 50 giri notturni sulla Strip",
        "f1Blurb": "La sfida sotto i riflettori di Las Vegas Boulevard parte alle 22:00 locali: Verstappen scatta in pole davanti a Russell, con 33 punti tra Verstappen (279) e Norris (246) per il secondo posto iridato."
    },
    "pl": {
        "todayDesk": "Sobotni przeglad: Polfinaly w Turynie (Alcaraz vs Shelton 14:00, Zverev vs Miedwiediew 20:30). Wyscig glowny GP Las Vegas dzis w nocy. Powrot Premier League (Man City 0:1 Fulham na zywo). Moving Day w RSM Classic.",
        "todayNfl": "TNF Koniec: Texans 26, Colts 3 (Stroud 2 TD, defensywa wymusza 3 straty). Niedziela 11. tygodnia: Chiefs u Panthers, 49ers u Packers.",
        "todayTnf": "NFL 11. tydzien TNF Koniec: Texans 26-3 Colts na NRG Stadium. Texans (7-4) przejmuja prowadzenie w AFC South.",
        "football_tagline": "TNF Koniec: Texans rozbijaja Colts 26:3 ze Stroudem i zelazna obrona; niedziela przed nami.",
        "football_liveNow": "TNF Koniec: Texans 26, Colts 3 (Stroud 22/31, 248 yds, 2 TD; Richardson zatrzymany na 112 yds, 2 INT). Niedziela: Chiefs u Panthers, 49ers u Packers.",
        "football_pulse": "NFL 11. TYDZIEN: TEXANS ROZBIJAJA COLTS 26:3 I PRZEJMUJA PRZODOWNICTWO W AFC SOUTH",
        "tennis_tagline": "Super Sobota w Turynie: Alcaraz gra z Sheltonem o 14:00 CET, a Zverev walczy z Miedwiediewem o 20:30 CET.",
        "tennis_liveNow": "Polfinaly w Turynie: Alcaraz vs Shelton (14:00 CET), Zverev vs Miedwiediew (20:30 CET). Piatek: Zverev pokonal Filsa 6-4, 7-6(5); Shelton wygral z Jodarem 6-3, 6-4.",
        "tennis_pulse": "NITTO ATP FINALS: SUPER SOBOTA W T难题RYNIE GDZIE ALCARAZ, SHELTON, ZVEREV I MIEDWIEDIEW GRAJA O FINAL",
        "f1_tagline": "Wyscig glowny GP Las Vegas dzis w nocy: Verstappen na pole position obok Russella w blasku neonow.",
        "f1_liveNow": "Dzis w nocy: Wyscig 50 okrazen (22:00 PST / 07:00 w Polsce). Start: Verstappen P1, Russell P2, Leclerc P3, Norris P4. Kara dla Antonellego (P6). Walka o P2: Verstappen 279, Russell 262, Norris 246.",
        "f1_pulse": "GP LAS VEGAS: VERSTAPPEN RUSZA Z POLE POSITION OBOK RUSSELLA DO 50-OKRAZENIOWEGO NOCNEGO WYSGCIGU",
        "soccer_tagline": "Powrot Premier League: Fulham szokuje City na Etihad; lider Arsenal gra pozniej z Newcastle.",
        "soccer_liveNow": "Na zywo: Man City 0:1 Fulham (Muniz 16). Dzis: Newcastle vs Arsenal (17:30 GMT), Chelsea vs Leeds (15:00 GMT). Tabela: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "PILKA NOZNA: PREMIER LEAGUE WRACA Z PROWADZENIEM FULHAM NA ETIHAD I WYJAZDEM ARSENALU DO NEWCASTLE",
        "basketball_tagline": "Lakers uciekaja przed zrywem Kings 106:104 w Sacramento; Jokic notuje 32-punktowe triple-double dla Denver.",
        "basketball_liveNow": "Piatek: Lakers 106-104 Kings (wolne Reavesa, Fox 29); Nuggets 133-124 Rockets (Jokic 32/12/10); Cavaliers 128-119 Pacers.",
        "basketball_pulse": "NBA PIATEK: LAKERS WYGRYWAJA Z KINGS 106:104 W NERWOWEJ KONCOWCE GDY JOKIC CIAGNIE NUGGETS",
        "golf_tagline": "The RSM Classic Moving Day na zywo w Sea Island: Trzech graczy na czele z -9, cut ustalony na -2.",
        "golf_liveNow": "PGA Tour: 3. runda Moving Day na zywo w Sea Island (Seaside). Liderzy na -9: Thorbjornsen, Penge, Neergaard-Petersen. Cut na -2 (65 graczy). Walka o karty 2027.",
        "golf_pulse": "PGA TOUR FALL FINALE: TRZECIA RUNDA MOVING DAY W SEA ISLAND W ZACIEKLEJ WALCE O KARTY PGA TOUR",
        "tonight": "Sobotni przeglad",
        "tonightBlurb": "Polfinaly w Turynie: Alcaraz vs Shelton o 14:00 CET i Zverev vs Miedwiediew o 20:30 CET. GP Las Vegas: 50 okrazen noca z Verstappenem na pole position. Premier League: Fulham prowadzi 1:0 z City; Arsenal w Newcastle o 17:30 GMT. Golf: Moving Day w Sea Island.",
        "f1Title": "Grand Prix Las Vegas: Verstappen na pole position do 50-okrazeniowego nocnego wyscigu na Stripie",
        "f1Blurb": "Nocne starcie na bulwarze w Las Vegas rusza o 22:00 czasu lokalnego: Verstappen rusza przed Russellem, a 33 punkty dziela Verstappena (279) i Norrisa (246) w walce o wicemistrzostwo."
    },
    "zh": {
        "todayDesk": "周六要闻：都灵半决赛（阿尔卡拉斯对谢尔顿 14:00，兹维列夫对梅德韦杰夫 20:30）。拉斯维加斯大奖赛今晚50圈夜战。英超回归（曼城0-1富勒姆直播中；纽卡斯尔对阿森纳）。RSM精英赛移动日。",
        "todayNfl": "TNF战报：德州人26-3小马（斯特劳德2达阵，防守迫使3次失误）。周日第11周大战待续：酋长客战黑豹，49人客战包装工。",
        "todayTnf": "NFL第11周TNF完赛：德州人26-3小马。休斯敦（7-4）掌控美联南区榜首。",
        "football_tagline": "TNF完赛：德州人26-3横扫小马，斯特劳德与铁血防守显威；周日大战蓄势待发。",
        "football_liveNow": "TNF完赛：德州人26-3小马（斯特劳德31传22中248码2达阵；理查德森仅112码2抄截）。周日：酋长客战黑豹，49人客战包装工。",
        "football_pulse": "NFL第11周：德州人26-3横扫小马独占美南榜首，周日战火即将打响",
        "tennis_tagline": "都灵超级星期六：阿尔卡拉斯14:00对阵谢尔顿，兹维列夫20:30再战梅德韦杰夫。",
        "tennis_liveNow": "都灵半决赛：阿尔卡拉斯对谢尔顿（14:00 CET），兹维列夫对梅德韦杰夫（20:30 CET）。周五：兹维列夫6-4、7-6击败菲斯；谢尔顿6-3、6-4胜霍达尔。",
        "tennis_pulse": "ATP年终总决赛：都灵超级星期六打响，阿尔卡拉斯、谢尔顿、兹维列夫与梅德韦杰夫决战四强",
        "f1_tagline": "拉斯维加斯大奖赛今晚正赛：维斯塔潘携手拉塞尔在霓虹夜空下头排起步。",
        "f1_liveNow": "今晚：50圈夜赛正赛（当地时间22:00）。发车位：维斯塔潘P1，拉塞尔P2，勒克莱尔P3，诺里斯P4。安东内利罚退至P6。亚军争夺战：维斯塔潘279分，拉塞尔262分，诺里斯246分。",
        "f1_pulse": "拉斯维加斯大奖赛：维斯塔潘接过杆位携手拉塞尔，50圈夜间正赛今晚震撼开打",
        "soccer_tagline": "英超重燃战火：富勒姆伊蒂哈德客场闪击曼城；领头羊阿森纳稍后客战纽卡斯尔。",
        "soccer_liveNow": "进行中：曼城0-1富勒姆（穆尼斯16分）。今日：纽卡斯尔对阿森纳（17:30 GMT），切尔西对利兹联（15:00 GMT）。积分榜：阿森纳27，布莱顿22，曼城21。",
        "soccer_pulse": "足球：英超重开富勒姆客场领先曼城，榜首阿森纳出征圣詹姆斯公园",
        "basketball_tagline": "湖人末节惊险106-104击退国王；约基奇砍下32分三双率掘金击退火箭。",
        "basketball_liveNow": "周五：湖人106-104国王（里夫斯关键罚球，福克斯29分）；掘金133-124火箭（约基奇32/12/10）；骑士128-119步行者。",
        "basketball_pulse": "NBA周五：湖人客场106-104险胜国王，约基奇32分三双带领掘金奏凯",
        "golf_tagline": "RSM精英赛移动日海岛球场进行中：三人同以低于标准杆9杆并列领跑，晋级线定在-2杆。",
        "golf_liveNow": "美巡赛：海岛球场第3轮移动日进行中。低于标准杆9杆并列领先：索比约恩森、彭奇、尼尔高-彼得森。晋级线-2杆（65人进决赛）。2027年参赛卡争夺激烈。",
        "golf_pulse": "美巡秋季赛收官战：海岛球场第三轮移动日打响，球员全力争夺2027美巡全卡",
        "tonight": "周六要闻",
        "tonightBlurb": "都灵半决赛：阿尔卡拉斯对谢尔顿（14:00 CET）与兹维列夫对梅德韦杰夫（20:30 CET）。拉斯维加斯大奖赛：今晚50圈夜战维斯塔潘杆位起步。英超：富勒姆客场1-0领先曼城；阿森纳客战纽卡斯尔（17:30 GMT）。高尔夫：海岛球场移动日进行中。",
        "f1Title": "拉斯维加斯大奖赛：维斯塔潘夺得杆位，领衔今晚拉斯维加斯大道50圈夜赛",
        "f1Blurb": "拉斯维加斯大道霓虹对决于当地时间今晚22:00打响：维斯塔潘力压拉塞尔从杆位出发，年度亚军33分大混战一触即发。"
    },
    "ja": {
        "todayDesk": "土曜デスク：トリノ準決勝（アルカラス対シェルトン 14:00、ズベレフ対メドベージェフ 20:30）。今夜ラスベガスGP 50周決勝。プレミアリーグ再開（マンC 0-1 フラム生中継；ニューカッスル対アーセナル）。RSMムービングデー。",
        "todayNfl": "TNF結果：テキサンズ 26-3 コルツ（ストラウド2TD、守備陣が3ターンオーバーを誘発）。日曜の第11週本番へ：チーフス対パンサーズ、49ers対パッカーズ。",
        "todayTnf": "NFL第11週TNF終了：テキサンズ 26-3 コルツ（NRGスタジアム）。ヒューストン（7勝4敗）がAFC南部首位を快走。",
        "football_tagline": "TNF終了：テキサンズがコルツを26-3で圧倒、ストラウドと堅守で勝利；日曜のゲームへ。",
        "football_liveNow": "TNF終了：テキサンズ 26-3 コルツ（ストラウド22/31、248ヤード、2TD；リチャードソンを112ヤードに封殺）。日曜：チーフス対パンサーズ、49ers対パッカーズ。",
        "football_pulse": "NFL第11週：テキサンズがコルツを26-3で下し地区首位を堅持、日曜の本戦へ",
        "tennis_tagline": "トリノのスーパーサタデー：14:00からアルカラス対シェルトン、20:30からズベレフ対メドベージェフの激突。",
        "tennis_liveNow": "トリノ準決勝：アルカラス対シェルトン（14:00 CET）、ズベレフ対メドベージェフ（20:30 CET）。金曜：ズベレフがフィスを6-4、7-6で下す；シェルトンがホダールに6-3、6-4で勝利。",
        "tennis_pulse": "ATPファイナルズ：トリノでスーパーサタデー開幕、アルカラス、シェルトン、ズベレフ、メドベージェフが決勝争い",
        "f1_tagline": "今夜ラスベガスGP決勝レース：ネオン輝くストリップでフェルスタッペンがラッセルとフロントローからスタート。",
        "f1_liveNow": "今夜：50周の決勝レース（現地22:00 / 日本時間日曜15:00）。グリッド：フェルスタッペンP1、ラッセルP2、ルクレールP3、ノリスP4。アントネッリは降格でP6。2位争い：フェルスタッペン279点、ラッセル262点、ノリス246点。",
        "f1_pulse": "ラスベガスGP：フェルスタッペンがポールを継承、今夜50周のストリップ夜間決戦へ出走",
        "soccer_tagline": "プレミアリーグ再開：フラムがエティハドでマンCから電撃先制；首位アーセナルは後ほどニューカッスル戦。",
        "soccer_liveNow": "生中継：マンC 0-1 フラム（ムニス16分）。本日：ニューカッスル対アーセナル（17:30 GMT）、チェルシー対リーズ（15:00 GMT）。順位：アーセナル27、ブライトン22、シティ21。",
        "soccer_pulse": "サッカー：プレミアリーグ再開、フラムが敵地で先制＆首位アーセナルはニューカッスルへ遠征",
        "basketball_tagline": "レイカーズが接戦を逃げ切りキングスに106-104で勝利；ヨキッチが32得点トリプルダブルでナゲッツ牽引。",
        "basketball_liveNow": "金曜：レイカーズ 106-104 キングス（リーブスの勝負強いFT、フォックス29得点）；ナゲッツ 133-124 ロケッツ（ヨキッチ32/12/10）；キャバリアーズ 128-119 ペイサーズ。",
        "basketball_pulse": "NBA金曜：レイカーズがサクラメントの熱戦を106-104で制す、ヨキッチがトリプルダブル達成",
        "golf_tagline": "RSMクラシック・ムービングデー生中継：シーアイランドで3選手が9アンダー首位、カットラインは-2。",
        "golf_liveNow": "PGAツアー：シーアイランド（シーサイド）で第3Rムービングデー進行中。9アンダー首位タイ：ソービョルンセン、ペンジ、ニアガード＝ペテルセン。カット-2（65名予選通過）。来季シード争い激化。",
        "golf_pulse": "PGAツアー最終戦：シーアイランドで第3ラウンド進行中、2027年シード権獲得への熱い戦い",
        "tonight": "土曜デスク",
        "tonightBlurb": "トリノ準決勝：アルカラス対シェルトン（14:00 CET）とズベレフ対メドベージェフ（20:30 CET）。ラスベガスGP：今夜50周の夜間決勝でフェルスタッペンがポール発進。プレミアリーグ：フラムがエティハドで1-0リード；アーセナル対ニューカッスル（17:30 GMT）。ゴルフ：シーアイランドでムービングデー中継。",
        "f1Title": "ラスベガスGP：今夜ストリップで開催される50周の夜間決勝でフェルスタッペンがポール発進",
        "f1Blurb": "ラスベガス・ブルバードの夜間決戦が現地22:00にスタート：フェルスタッペンが先頭から発進、2位を争うフェルスタッペン（279）とノリス（246）の差は33ポイント。"
    },
    "ko": {
        "todayDesk": "토요일 데스크: 토리노 준결승 (알카라스 vs 셸턴 14:00, 츠베레프 vs 메드베데프 20:30). 라스베이거스 GP 50랩 결선 오늘 밤. 프리미어리그 재개 (맨시티 0-1 풀럼 라이브; 뉴캐슬 vs 아스널). RSM 클래식 무빙데이.",
        "todayNfl": "TNF 최종: 텍산스 26, 콜츠 3 (스트라우드 2 TD, 수비 턴오버 3개 유도). 일요일 11주차 경기: 치프스 vs 팬서스, 49ers vs 패커스.",
        "todayTnf": "NFL 11주차 TNF 최종: 텍산스 26-3 콜츠 (NRG 스타디움). 휴스턴(7승 4패) AFC 남부 선두 독주.",
        "football_tagline": "TNF 최종: 텍산스, 스트라우드와 질식 수비 앞세워 콜츠 26-3 완파; 일요일 경기 대기.",
        "football_liveNow": "TNF 최종: 텍산스 26, 콜츠 3 (스트라우드 22/31, 248야드, 2 TD; 리처드슨 112야드 2 INT 억제). 일요일: 치프스 vs 팬서스, 49ers vs 패커스.",
        "football_pulse": "NFL 11주차: 텍산스, 콜츠 26-3으로 대파하고 AFC 남부 단독 선두 질주",
        "tennis_tagline": "토리노 슈퍼 토요일: 14:00 알카라스 vs 셸턴, 20:30 츠베레프 vs 메드베데프 결승행 격돌.",
        "tennis_liveNow": "토리노 준결승: 알카라스 vs 셸턴 (14:00 CET), 츠베레프 vs 메드베데프 (20:30 CET). 금요일: 츠베레프, 필스에 6-4, 7-6 승리; 셸턴, 호다르에 6-3, 6-4 승리.",
        "tennis_pulse": "니토 ATP 파이널스: 토리노 슈퍼 토요일 개막, 알카라스·셸턴·츠베레프·메드베데프 결승 티켓 혈투",
        "f1_tagline": "라스베이거스 GP 결선 오늘 밤: 페르스타펜이 네온 불빛 아래 러셀과 함께 프런트로 출발.",
        "f1_liveNow": "오늘 밤: 50랩 결선 (현지 22:00 / 한국 일요일 15:00). 그리드: 페르스타펜 P1, 러셀 P2, 르클레르 P3, 노리스 P4. 안토넬리 강등(P6 출발). 드라이버 2위 싸움: 페르스타펜 279점, 러셀 262점, 노리스 246점.",
        "f1_pulse": "라스베이거스 GP: 페르스타펜 폴 포지션 승계, 오늘 밤 50랩 스트립 나이트 레이스 출격",
        "soccer_tagline": "프리미어리그 재개: 풀럼, 에티하드 원정서 맨시티에 기습 선제골; 1위 아스널은 잠시 후 뉴캐슬 원정.",
        "soccer_liveNow": "라이브: 맨시티 0-1 풀럼 (무니스 16분). 오늘: 뉴캐슬 vs 아스널 (17:30 GMT), 첼시 vs 리즈 (15:00 GMT). 순위: 아스널 27, 브라이튼 22, 맨시티 21.",
        "soccer_pulse": "축구: 프리미어리그 복귀전서 풀럼 깜짝 선제골, 선두 아스널은 뉴캐슬 원정 출격",
        "basketball_tagline": "레이커스, 새크라멘토에 106-104 신승; 요키치 32득점 트리플더블로 너기츠 승리 견인.",
        "basketball_liveNow": "금요일: 레이커스 106-104 킹스 (리브스 클러치 자유투, 팍스 29점); 너기츠 133-124 로케츠 (요키치 32/12/10); 캐벌리어스 128-119 페이서스.",
        "basketball_pulse": "NBA 금요일: 레이커스, 접전 끝에 킹스 106-104 제압... 요키치는 트리플더블 폭발",
        "golf_tagline": "RSM 클래식 무빙데이 시아일랜드 라이브: 3명 9언더파 공동 선두, 컷 통과선은 -2.",
        "golf_liveNow": "PGA 투어: 시아일랜드(씨사이드) 3R 무빙데이 라이브. 9언더파 공동 선두: 소르비욘센, 펜지, 네어가르-페테르센. 컷 -2 (65명 진출). 2027 투어 카드 생존 경쟁.",
        "golf_pulse": "PGA 투어 가을 최종전: 시아일랜드에서 3라운드 무빙데이 진행, 2027 시드권 확보 전쟁",
        "tonight": "토요일 데스크",
        "tonightBlurb": "토리노 준결승: 알카라스 vs 셸턴 (14:00 CET) 및 츠베레프 vs 메드베데프 (20:30 CET). 라스베이거스 GP: 페르스타펜 폴 포지션의 50랩 나이트 레이스. 프리미어리그: 풀럼 1-0 맨시티 리드; 아스널 vs 뉴캐슬 (17:30 GMT). 골프: 시아일랜드 무빙데이 생중계.",
        "f1Title": "라스베이거스 그랑프리: 페르스타펜, 오늘 밤 스트립 50랩 나이트 레이스 폴 포지션 출발",
        "f1Blurb": "라스베이거스 스트립 야간 레이스가 현지 22:00에 시작됩니다: 페르스타펜이 러셀에 앞서 출발하며 2위 페르스타펜(279점)과 노리스(246점) 간의 33점 차 승부가 펼쳐집니다."
    },
    "ar": {
        "todayDesk": "مكتب السبت: نصف نهائي تورينو (ألكاراز ضد شيلتون 14:00، زفيريف ضد ميدفيديف 20:30). سباق جائزة لاس فيغاس الكبرى الليلة. عودة الدوري الإنجليزي (مانشستر سيتي 0-1 فولهام مباشر). يوم الحسم في بطولة آر إس إم كلاسيك.",
        "todayNfl": "ختام ليلة الخميس: تكسانز 26، كولتس 3 (سترود 2 هبوط، الدفاع يجبر الخصم على 3 أخطاء). مواجهات الأحد للأسبوع 11: تشيفز ضد بانثرز، 49ers ضد باكرز.",
        "todayTnf": "NFL الأسبوع 11 ختام ليلة الخميس: تكسانز 26-3 كولتس في ملعب إن آر جي. هيوستن (7-4) ينفرد بصدارة القسم الجنوبي.",
        "football_tagline": "ختام ليلة الخميس: تكسانز يكتسحون كولتس 26-3 بفضل سترود ودفاع لا يرحم؛ انتظار مباريات الأحد.",
        "football_liveNow": "ختام ليلة الخميس: تكسانز 26، كولتس 3 (سترود 22/31، 248 ياردة، 2 هبوط؛ ريتشاردسون 112 ياردة، 2 اعتراض). الأحد: تشيفز ضد بانثرز، 49ers ضد باكرز.",
        "football_pulse": "NFL الأسبوع 11: تكسانز يكتسحون كولتس 26-3 ويحكمون قبضتهم على صدارة القسم الجنوبي",
        "tennis_tagline": "السبت الكبير في تورينو: ألكاراز يلاقي شيلتون في الثانية ظهرا قبل صدام زفيريف وميدفيديف في الثامنة والنصف مساء.",
        "tennis_liveNow": "نصف نهائي تورينو: ألكاراز ضد شيلتون (14:00 بتوقيت وسط أوروبا)، زفيريف ضد ميدفيديف (20:30). الجمعة: زفيريف هزم فيس 6-4 و7-6؛ شيلتون هزم خودار 6-3 و6-4.",
        "tennis_pulse": "نهائيات التنس: السبت الكبير في تورينو وصراع ألكاراز، شيلتون، زفيريف وميدفيديف نحو النهائي",
        "f1_tagline": "سباق جائزة لاس فيغاس الليلة: فيرستابن في قطب الانطلاق إلى جانب راسل تحت أضواء النيون.",
        "f1_liveNow": "الليلة: سباق الـ 50 لفة (22:00 بالتوقيت المحلي). شبكة الانطلاق: فيرستابن أولا، راسل ثانيا، لوكلير ثالثا، نوريس رابعا. عقوبة أنتونيللي (المركز السادس). صراع الوصافة: فيرستابن 279، راسل 262، نوريس 246.",
        "f1_pulse": "جائزة لاس فيغاس: فيرستابن يرث قطب الانطلاق أمام راسل في سباق الـ 50 لفة الليلي على قطاع ذا ستريب",
        "soccer_tagline": "عودة الدوري الإنجليزي: فولهام يصدم سيتي بهدف مبكر في الاتحاد؛ والمتصدر أرسنال يحل ضيفا على نيوكاسل لاحقا.",
        "soccer_liveNow": "مباشر: مانشستر سيتي 0-1 فولهام (مونيز 16). اليوم: نيوكاسل ضد أرسنال (17:30 بتوقيت غرينتش)، تشيلسي ضد ليدز (15:00). الترتيب: أرسنال 27، برايتون 22، سيتي 21.",
        "soccer_pulse": "كرة القدم: عودة الدوري الإنجليزي بتقدم فولهام في ملعب الاتحاد وأرسنال يتأهب لقمة نيوكاسل",
        "basketball_tagline": "ليكرز يصمد ويهزم كينغز 106-104 في سكرامنتو؛ يوكيتش يسجل ثلاثية مزدوجة بـ 32 نقطة مع دنفر.",
        "basketball_liveNow": "الجمعة: ليكرز 106-104 كينغز (رميات ريفز الحاسمة، فوكس 29 نقطة)؛ ناغتس 133-124 روكتس (يوكيتش 32/12/10)؛ كافالييرز 128-119 بيسرز.",
        "basketball_pulse": "NBA الجمعة: ليكرز يحسم قمة سكرامنتو 106-104 في الثواني الأخيرة ويوكيتش يتألق مع دنفر",
        "golf_tagline": "بطولة آر إس إم كلاسيك مباشرة في سي آيلاند: ثلاثة متصدرين بـ -9 واجتياز القص عند -2.",
        "golf_liveNow": "جولة بي جي إيه: الجولة الثالثة مباشرة في سي آيلاند (المسار الساحلي). الصدارة بـ -9: ثوربيورنسن، بينجي، نيرغارد. خط القص عند -2 (65 لاعبا). معركة بطاقات 2027.",
        "golf_pulse": "ختام موسم بي جي إيه: انطلاق الجولة الثالثة في سي آيلاند في صراع شرس لحسم بطاقات موسم 2027",
        "tonight": "مكتب السبت",
        "tonightBlurb": "نصف نهائي تورينو: ألكاراز ضد شيلتون (14:00 بتوقيت وسط أوروبا) وزفيريف ضد ميدفيديف (20:30). جائزة لاس فيغاس: سباق ليلي من 50 لفة مع فيرستابن في المقدمة. الدوري الإنجليزي: فولهام يتقدم 1-0 على سيتي؛ أرسنال في نيوكاسل (17:30). الغولف: يوم الحسم في سي آيلاند.",
        "f1Title": "جائزة لاس فيغاس الكبرى: فيرستابن ينطلق أولا في السباق الليلي المكون من 50 لفة على قطاع ذا ستريب",
        "f1Blurb": "المواجهة تحت أضواء نيون لاس فيغاس تبدأ الليلة عند العاشرة مساء: فيرستابن ينطلق أولا أمام راسل، و33 نقطة تفصل فيرستابن (279) عن نوريس (246) في صراع الوصافة."
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

