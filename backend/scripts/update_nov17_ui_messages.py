"""Update playground.ts, messages.ts, and messages-*.ts for 2026-11-17."""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
I18N = os.path.join(ROOT, "frontend", "src", "i18n")

# 1. Update playground.ts
playground_path = os.path.join(I18N, "playground.ts")
pg_txt = open(playground_path, "r", encoding="utf-8").read()

pg_updates = {
    "en": {
        "pinFinal": "Turin Mon Lendl: Alcaraz d Tiafoe 6-2, 6-2; Medvedev d Cobolli 7-6, 6-3. Tue McEnroe: Fils vs Jodar (14:00 CET), Zverev vs Shelton (20:30 CET).",
        "plFootnote": "Mon: Germany 5-0 Netherlands (Wirtz 60, 77, Scherhant, Schlotterbeck, Gruda). Sun: Spain 2-3 England. PL: Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "MNF Final: Chargers 23, Ravens 20 at M&T Bank Stadium (Herbert 22-yd TD run, Hampton 105 yds, Still forced fumble).",
        "week1Sub": "Jim Harbaugh beats John in Harbaugh Bowl. LAC 7-3, BAL 7-3. Sun Munich: Lions 35, Patriots 10 (Gibbs 252 scrimmage yds, 2 TDs).",
        "countdownTnf": "MNF FINAL: Chargers 23-20 Ravens. Week 10 complete. Next: Thursday Night Football Week 11.",
        "majorsDone": "RSM Classic practice underway at Sea Island (top-125 cards). Dubai Complete: Hatton -15 (273); McIlroy -10 (278, 8th Race to Dubai title by 125 pts).",
        "gridAfterMadrid": "Two Days to Round 21 · Las Vegas Strip (19-21 Nov)",
    },
    "fr": {
        "pinFinal": "Turin lun Lendl : Alcaraz bat Tiafoe 6-2, 6-2 ; Medvedev bat Cobolli 7-6, 6-3. Mar McEnroe : Fils vs Jodar (14h00), Zverev vs Shelton (20h30).",
        "plFootnote": "Lun : Allemagne 5-0 Pays-Bas (Wirtz 60, 77, Scherhant, Schlotterbeck, Gruda). Dim : Espagne 2-3 Angleterre. PL : Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "MNF Final : Chargers 23, Ravens 20 au M&T Bank Stadium (course TD de 22 yds de Herbert, Hampton 105 yds, fumble provoqué par Still).",
        "week1Sub": "Jim Harbaugh bat John dans le Harbaugh Bowl. LAC 7-3, BAL 7-3. Dim Munich : Lions 35, Patriots 10 (Gibbs 252 yds, 2 TD).",
        "countdownTnf": "MNF TERMINE : Chargers 23-20 Ravens. Semaine 10 terminee. Prochain : Thursday Night Football Semaine 11.",
        "majorsDone": "Entraînements du RSM Classic a Sea Island (cartes top 125). Dubai termine : Hatton -15 (273) ; McIlroy -10 (278, 8e sacre a la Race to Dubai).",
        "gridAfterMadrid": "J-2 avant la manche 21 · Las Vegas Strip (19-21 nov)",
    },
    "es": {
        "pinFinal": "Turín lun Lendl: Alcaraz supera a Tiafoe 6-2, 6-2; Medvedev vence a Cobolli 7-6, 6-3. Mar McEnroe: Fils vs Jódar (14:00), Zverev vs Shelton (20:30).",
        "plFootnote": "Lun: Alemania 5-0 Países Bajos (Wirtz 60, 77, Scherhant, Schlotterbeck, Gruda). Dom: España 2-3 Inglaterra. PL: Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "MNF Final: Chargers 23, Ravens 20 en M&T Bank Stadium (carrera TD de 22 yds de Herbert, Hampton 105 yds, balón suelto forzado por Still).",
        "week1Sub": "Jim Harbaugh supera a John en el Harbaugh Bowl. LAC 7-3, BAL 7-3. Dom Múnich: Lions 35, Patriots 10 (Gibbs 252 yds, 2 TDs).",
        "countdownTnf": "MNF FINAL: Chargers 23-20 Ravens. Semana 10 finalizada. Siguiente: Thursday Night Football Semana 11.",
        "majorsDone": "Prácticas de The RSM Classic en Sea Island (tarjetas top 125). Dubái concluido: Hatton -15 (273); McIlroy -10 (278, 8vo título Race to Dubai).",
        "gridAfterMadrid": "Dos días para la Ronda 21 · Las Vegas Strip (19-21 nov)",
    },
    "de": {
        "pinFinal": "Turin Mo Lendl: Alcaraz schlägt Tiafoe 6:2, 6:2; Medvedev bezwingt Cobolli 7:6, 6:3. Di McEnroe: Fils vs Jódar (14:00), Zverev vs Shelton (20:30).",
        "plFootnote": "Mo: Deutschland 5:0 Niederlande (Wirtz 60., 77., Scherhant, Schlotterbeck, Gruda). So: Spanien 2:3 England. PL: Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "MNF Endstand: Chargers 23, Ravens 20 im M&T Bank Stadium (Herbert 22-Yd TD-Lauf, Hampton 105 Yds, Still erzwang Fumble).",
        "week1Sub": "Jim Harbaugh schlägt John im Harbaugh Bowl. LAC 7-3, BAL 7-3. So München: Lions 35, Patriots 10 (Gibbs 252 Scrimmage-Yards, 2 TDs).",
        "countdownTnf": "MNF ENDSTAND: Chargers 23-20 Ravens. Woche 10 beendet. Als Nächstes: Thursday Night Football Woche 11.",
        "majorsDone": "Training bei der RSM Classic in Sea Island läuft (Top-125 Karten). Dubai beendet: Hatton -15 (273); McIlroy -10 (278, 8. Race to Dubai Titel).",
        "gridAfterMadrid": "Zwei Tage bis Runde 21 · Las Vegas Strip (19.-21. Nov.)",
    },
    "it": {
        "pinFinal": "Torino lun Lendl: Alcaraz batte Tiafoe 6-2, 6-2; Medvedev supera Cobolli 7-6, 6-3. Mar McEnroe: Fils vs Jodar (14:00), Zverev vs Shelton (20:30).",
        "plFootnote": "Lun: Germania 5-0 Olanda (Wirtz 60, 77, Scherhant, Schlotterbeck, Gruda). Dom: Spagna 2-3 Inghilterra. PL: Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "MNF Finale: Chargers 23, Ravens 20 al M&T Bank Stadium (corsa TD di 22 yd di Herbert, Hampton 105 yd, fumble forzato da Still).",
        "week1Sub": "Jim Harbaugh batte John nell'Harbaugh Bowl. LAC 7-3, BAL 7-3. Dom Monaco: Lions 35, Patriots 10 (Gibbs 252 yd, 2 TD).",
        "countdownTnf": "MNF FINALE: Chargers 23-20 Ravens. Settimana 10 conclusa. Prossimo appuntamento: Thursday Night Football Settimana 11.",
        "majorsDone": "Prove del RSM Classic a Sea Island (carte per la top 125). Dubai concluso: Hatton -15 (273); McIlroy -10 (278, 8° titolo Race to Dubai).",
        "gridAfterMadrid": "Due giorni al Round 21 · Las Vegas Strip (19-21 nov)",
    },
    "pl": {
        "pinFinal": "Turyn pon Lendl: Alcaraz pokonuje Tiafoe 6:2, 6:2; Miedwiediew ogrywa Cobollego 7:6, 6:3. Wt McEnroe: Fils vs Jodar (14:00), Zverev vs Shelton (20:30).",
        "plFootnote": "Pon: Niemcy 5:0 Holandia (Wirtz 60, 77, Scherhant, Schlotterbeck, Gruda). Niedz: Hiszpania 2:3 Anglia. PL: Arsenal 27, Brighton 22, City 21.",
        "week1Closed": "MNF Koniec: Chargers 23, Ravens 20 na M&T Bank Stadium (22-jardowy bieg TD Herberta, Hampton 105 jardów, Still wymusił fumble).",
        "week1Sub": "Jim Harbaugh pokonuje Johna w Harbaugh Bowl. LAC 7-3, BAL 7-3. Niedz Monachium: Lions 35, Patriots 10 (Gibbs 252 jardy, 2 TD).",
        "countdownTnf": "MNF KONIEC: Chargers 23-20 Ravens. Tydzień 10 zakończony. Następnie: Thursday Night Football Tydzień 11.",
        "majorsDone": "Treningi przed RSM Classic w Sea Island (karty dla top 125). Dubaj zakończony: Hatton -15 (273); McIlroy -10 (278, 8. tytuł Race to Dubai).",
        "gridAfterMadrid": "Dwa dni do 21. rundy · Las Vegas Strip (19-21 listopada)",
    },
    "zh": {
        "pinFinal": "都灵周一伦德尔组：阿尔卡拉斯6-2、6-2胜蒂亚福；梅德韦杰夫7-6、6-3胜科博利。周二麦肯罗组：菲斯对霍达尔（14:00），兹维列夫对谢尔顿（20:30）。",
        "plFootnote": "周一：德国5-0狂胜荷兰（维尔茨60、77，谢尔汉特，施洛特贝克，格鲁达）。周日：西班牙2-3英格兰。英超：阿森纳27，布莱顿22，曼城21。",
        "week1Closed": "周一夜赛完场：闪电23-20力克乌鸦（赫伯特22码冲球达阵，汉普顿105码，斯蒂尔关键迫使掉球）。",
        "week1Sub": "吉姆-哈博击败兄长约翰赢得兄弟碗。闪电7-3，乌鸦7-3。周日慕尼黑：雄狮35-10爱国者（吉布斯252码，2达阵）。",
        "countdownTnf": "周一夜赛完场：闪电23-20乌鸦。第10周战罢。下场：第11周周四夜赛。",
        "majorsDone": "海岛RSM精英赛开启官方练习轮（前125全卡争夺）。迪拜收官：哈顿-15（273）；麦克罗伊-10（278，以125分优势斩获第8座总冠军）。",
        "gridAfterMadrid": "第21站倒计时两天 · 拉斯维加斯街道赛（11月19-21日）",
    },
    "ja": {
        "pinFinal": "トリノ月曜レンドル組：アルカラスがティアフォーに6-2、6-2で快勝；メドベージェフがコボッリに7-6、6-3。火曜マッケンロー組：フィス対ホダール（14:00）、ズベレフ対シェルトン（20:30）。",
        "plFootnote": "月曜：ドイツ5-0オランダ（ヴィルツ60, 77、シェルハント、シュロッターベック、グルーダ）。日曜：スペイン2-3イングランド。PL：アーセナル27、ブライトン22、シティ21。",
        "week1Closed": "MNF試合終了：チャージャーズ23-20レイブンズ（ハーバート22yd TDラン、ハンプトン105yd、スティール決勝ファンブル奪取）。",
        "week1Sub": "ジム・ハーボーが兄ジョンとの対決を制す。LAC 7-3、BAL 7-3。日曜ミュンヘン：ライオンズ35-10ペイトリオッツ（ギブス252yd、2TD）。",
        "countdownTnf": "MNF終了：チャージャーズ23-20レイブンズ。第10週終了。次回：第11週サーズデーナイト。",
        "majorsDone": "シーアイランドでRSMクラシック公式練習開始（来季シード125枠争い）。ドバイ終了：ハットン-15（273）；マキロイ-10（278、8度目の欧州年間王者）。",
        "gridAfterMadrid": "第21戦ラスベガス開幕まであと2日 · ストリップ（11月19-21日）",
    },
    "ko": {
        "pinFinal": "토리노 월요일 렌들 조: 알카라스, 티아포에 6-2, 6-2 완승; 메드베데프, 코볼리에 7-6, 6-3 승. 화요일 매켄로 조: 필스 vs 호다르 (14:00), 즈베레프 vs 셸턴 (20:30).",
        "plFootnote": "월요일: 독일 5-0 네덜란드 (비르츠 60, 77, 셰르한트, 슐로터베크, 그루다). 일요일: 스페인 2-3 잉글랜드. PL: 아스널 27, 브라이튼 22, 맨시티 21.",
        "week1Closed": "MNF 경기 종료: 차저스 23-20 레이븐스 (허버트 22야드 TD 러싱, 햄튼 105야드, 스틸 결정적 펌블 유도).",
        "week1Sub": "짐 하보 감독이 형 존 하보를 꺾고 하보 볼 승리. LAC 7-3, BAL 7-3. 일요일 뮌헨: 라이온스 35, 패트리어츠 10 (깁스 252야드, 2TD).",
        "countdownTnf": "MNF 최종: 차저스 23-20 레이븐스. 10주차 종료. 다음 경기: 11주차 서스데이 나이트 풋볼.",
        "majorsDone": "시 아일랜드서 RSM 클래식 공식 연습 개막 (125위 잔류전). 두바이 최종: 해튼 -15 (273); 매킬로이 -10 (278, 통산 8번째 시즌 챔피언).",
        "gridAfterMadrid": "21라운드 개막 D-2 · 라스베이거스 스트립 (11월 19-21일)",
    },
    "ar": {
        "pinFinal": "تورينو الاثنين ليندل: ألكاراز يهزم تيافو 6-2، 6-2؛ ميدفيديف يتغلب على كوبولي 7-6، 6-3. الثلاثاء ماكنرو: فيس ضد خودار (14:00)، زفيريف ضد شيلتون (20:30).",
        "plFootnote": "الاثنين: ألمانيا 5-0 هولندا (فيرتز 60، 77، شيرهانت، شلوتربيك، غرودا). الأحد: إسبانيا 2-3 إنجلترا. الدوري الإنجليزي: أرسنال 27، برايتون 22، سيتي 21.",
        "week1Closed": "ختام ليلة الاثنين: تشارجرز 23، ريفنز 20 في بالتيمور (هربرت يركض 22 ياردة نحو الهدف، هامبتون 105 ياردات، ستيل يجبر على فقدان الكرة).",
        "week1Sub": "جيم هاربوه يهزم شقيقه جون في مواجهة الإخوة. تشارجرز 7-3، ريفنز 7-3. الأحد في ميونخ: لايونز 35، باتريوتس 10 (غيبس 252 ياردة وهدفان).",
        "countdownTnf": "ختام ليلة الاثنين: تشارجرز 23-20 ريفنز. انتهاء الجولة 10. القادم: ليلة الخميس للجولة 11.",
        "majorsDone": "انطلاق تدريبات آر إس إم كلاسيك في سي آيلاند (صراع أفضل 125). ختام دبي: هاتون -15 (273)؛ ماكلروي -10 (278، اللقب الثامن للسباق إلى دبي).",
        "gridAfterMadrid": "يومان على انطلاق الجولة 21 · حلبة لاس فيغاس (19-21 نوفمبر)",
    }
}

for loc, fields in pg_updates.items():
    # Find the block for `loc`: "loc": { ... }
    # and replace fields inside it
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
    "todayDesk": "Tuesday desk: Germany crush Netherlands 5-0 in Nations League romp. MNF Chargers edge Ravens 23-20 in Harbaugh Bowl. Turin Alcaraz sweeps Tiafoe 6-2, 6-2; Zverev meets Shelton tonight.",
    "todayNfl": "MNF Final: Chargers 23, Ravens 20 at M&T Bank Stadium (Jim tops John). Sunday Munich: Lions 35-10 Patriots (Gibbs 252 yds).",
    "todayTnf": "NFL Week 10: Chargers edge Ravens 23-20 on Monday Night Football. Week 10 complete. Next: Thursday Night Football Week 11.",
    "football_tagline": "MNF Final: Chargers edge Ravens 23-20 in Harbaugh Bowl; Lions rout Patriots 35-10 in Munich.",
    "football_liveNow": "MNF: Chargers 23, Ravens 20 (Herbert 22-yd TD run, Hampton 105 yds, Still forced fumble). Sun Munich: Lions 35-10 Patriots (Gibbs 252 yds, 2 TDs).",
    "football_pulse": "MNF FINAL: CHARGERS SURVIVE RAVENS 23-20 IN HARBAUGH BOWL AS JIM EDGES JOHN",
    "tennis_tagline": "Turin ATP Finals: Alcaraz storms past Tiafoe 6-2, 6-2; Zverev meets Shelton in Tuesday night clash.",
    "tennis_liveNow": "Mon Lendl: Alcaraz d Tiafoe 6-2, 6-2; Medvedev d Cobolli 7-6 (4), 6-3. Tue McEnroe: Fils vs Jodar (14:00 CET), Zverev vs Shelton (20:30 CET).",
    "tennis_pulse": "TURIN ATP FINALS: ALCARAZ SWEEPS TIAFOE 6-2, 6-2; ZVEREV VS SHELTON TONIGHT IN MCENROE GROUP",
    "f1_tagline": "Two days to Round 21 Las Vegas: Strip setup finishes as five-driver battle for P2 heats up.",
    "f1_liveNow": "Drivers P2 shootout: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Vegas Strip: 19-21 Nov.",
    "f1_pulse": "TWO DAYS TO VEGAS: VERSTAPPEN TO NORRIS SPLIT BY 33 POINTS AHEAD OF THURSDAY PRACTICE",
    "soccer_tagline": "Germany crush Netherlands 5-0 in Nations League romp; England hold off Spain 3-2 in Madrid.",
    "soccer_liveNow": "Mon: Germany 5-0 Netherlands (Wirtz 60, 77, Scherhant, Schlotterbeck, Gruda); Greece 1-0 Serbia. Sun: Spain 2-3 England. PL: Arsenal 27, Brighton 22, City 21.",
    "soccer_pulse": "NATIONS LEAGUE: GERMANY CRUSH NETHERLANDS 5-0 TO CLINCH GROUP A2; WIRTZ SCORES BRACE",
    "basketball_tagline": "Magic rally past Celtics 115-105 to snap Boston streak; Heat extend run to five behind Giannis.",
    "basketball_liveNow": "Mon: Magic 115-105 Celtics (Bane 24); Heat 128-110 Rockets (Giannis 20/13/6, 5th straight win); 76ers 135-123 Nets (Embiid 37); Suns 117-105 Nuggets.",
    "basketball_pulse": "NBA MONDAY: MAGIC END CELTICS STREAK 115-105; HEAT EXTEND RUN TO FIVE BEHIND GIANNIS",
    "golf_tagline": "RSM Classic practice underway at Sea Island with top-125 cards on the line; McIlroy savors 8th crown.",
    "golf_liveNow": "PGA Tour: RSM Classic tournament week begins at Sea Island (19-22 Nov). DP World Tour Complete: Hatton -15 (273); McIlroy -10 (278, 8th Race to Dubai).",
    "golf_pulse": "PGA TOUR FALL FINALE: RSM CLASSIC PRACTICE UNDERWAY AT SEA ISLAND AS PLAYERS CHASE TOP-125 CARDS",
    "tonight": "Tuesday desk",
    "tonightBlurb": "Monday Night Football final: Jim Harbaugh tops brother John as Chargers edge Ravens 23-20. Monday: Germany dismantle Netherlands 5-0 to top Group A2; Magic rally past Celtics 115-105; Alcaraz cruises 6-2, 6-2 in Turin; Zverev meets Shelton tonight.",
    "f1Title": "Two days to Round 21 Las Vegas: 33 points split Verstappen (279) to Norris (246)",
    "f1Blurb": "Two days to Round 21 Las Vegas: Strip setup finishes as five-driver battle for P2 heats up behind Champion Antonelli (390) and Mercedes (652)."
}

msg_fr = {
    "todayDesk": "Bureau du mardi : L'Allemagne écrase les Pays-Bas 5-0. MNF Chargers-Ravens 23-20 dans le Harbaugh Bowl. Turin Alcaraz balaie Tiafoe 6-2, 6-2 ; Zverev retrouve Shelton ce soir.",
    "todayNfl": "MNF Final : Chargers 23, Ravens 20 au M&T Bank Stadium (Jim bat John). Dimanche Munich : Lions 35-10 Patriots (Gibbs 252 yds).",
    "todayTnf": "NFL Semaine 10 : Les Chargers battent les Ravens 23-20 au Monday Night. Semaine 10 terminee. Prochain : Thursday Night Football Semaine 11.",
    "football_tagline": "MNF Final : duel des freres Harbaugh a Baltimore remporté par les Chargers 23-20 ; les Lions surclassent les Patriots 35-10 a Munich.",
    "football_liveNow": "MNF : Chargers 23, Ravens 20 (course TD de Herbert 22 yds, Hampton 105 yds, fumble de Still). Dim Munich : Lions 35-10 Patriots (Gibbs 252 yds, 2 TD).",
    "football_pulse": "MNF FINAL : LES CHARGERS BATTENT LES RAVENS 23-20 DANS LE HARBAUGH BOWL",
    "tennis_tagline": "Masters de Turin : Alcaraz domine Tiafoe 6-2, 6-2 ; Zverev defie Shelton mardi soir.",
    "tennis_liveNow": "Lun Lendl : Alcaraz bat Tiafoe 6-2, 6-2 ; Medvedev bat Cobolli 7-6 (4), 6-3. Mar McEnroe : Fils vs Jodar (14h00), Zverev vs Shelton (20h30).",
    "tennis_pulse": "MASTERS DE TURIN : ALCARAZ DEROULE 6-2, 6-2 ; ZVEREV DEFIE SHELTON CE SOIR DANS LE GROUPE MCENROE",
    "f1_tagline": "J-2 avant Las Vegas : Le paddock termine ses installations ; lutte a 5 pour la deuxieme place mondiale.",
    "f1_liveNow": "Duel P2 : Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390 ; Mercedes 652). Strip de Vegas : 19-21 nov.",
    "f1_pulse": "J-2 AVANT VEGAS : 33 POINTS SEPARENT VERSTAPPEN A NORRIS POUR LE TITRE DE VICE-CHAMPION",
    "soccer_tagline": "L'Allemagne ecrase les Pays-Bas 5-0 en Ligue des nations ; l'Angleterre bat l'Espagne 3-2 a Madrid.",
    "soccer_liveNow": "Lun : Allemagne 5-0 Pays-Bas (Wirtz 60, 77, Scherhant, Schlotterbeck, Gruda) ; Grece 1-0 Serbie. Dim : Espagne 2-3 Angleterre. PL : Arsenal 27, Brighton 22, City 21.",
    "soccer_pulse": "LIGUE DES NATIONS : L'ALLEMAGNE ECRASE LES PAYS-BAS 5-0 ET TERMINE EN TETE DU GROUPE A2",
    "basketball_tagline": "Le Magic renverse les Celtics 115-105 et brise la serie de Boston ; Miami enchaine un 5e succes avec Giannis.",
    "basketball_liveNow": "Lun : Magic 115-105 Celtics (Bane 24) ; Heat 128-110 Rockets (Giannis 20/13/6, 5e de suite) ; 76ers 135-123 Nets (Embiid 37) ; Suns 117-105 Nuggets.",
    "basketball_pulse": "NBA LUNDI : LE MAGIC BRISA LA SERIE DES CELTICS 115-105 ; MIAMI ENCHAINE UN 5E SUCCES",
    "golf_tagline": "Entraînements du RSM Classic a Sea Island (cartes top 125) ; McIlroy savoure son 8e sacre.",
    "golf_liveNow": "PGA Tour : La semaine du RSM Classic commence a Sea Island (19-22 nov). Dubai termine : Hatton -15 (273) ; McIlroy -10 (278, 8e sacre a la Race to Dubai).",
    "golf_pulse": "PGA TOUR : ENTRAINEMENTS DU RSM CLASSIC A SEA ISLAND AVEC LES CARTES DU TOP-125 EN JEU",
    "tonight": "Bureau du mardi",
    "tonightBlurb": "Monday Night Football : Jim Harbaugh bat son frere John avec les Chargers 23-20. Lundi : l'Allemagne ecrase les Pays-Bas 5-0 ; le Magic surprend Boston 115-105 ; Alcaraz deroule a Turin ; Zverev affronte Shelton ce soir.",
    "f1Title": "J-2 avant Las Vegas (manche 21) : 33 points separent Verstappen (279) de Norris (246)",
    "f1Blurb": "J-2 avant Las Vegas : Le paddock est pret sur le Strip pour la bataille a 5 derriere le champion Antonelli (390) et Mercedes (652)."
}

# Apply en block (first export const en: Messages = { ... })
# and fr block (export const fr: Messages = { ... })
en_match = re.search(r'(export const en:\s*Messages\s*=\s*\{)([\s\S]*?)(\n\};\n\nexport const fr)', msg_txt)
if en_match:
    en_body = en_match.group(2)
    for k, v in msg_en.items():
        escaped_v = v.replace('"', '\\"')
        if k in ["todayDesk", "todayNfl", "todayTnf", "tonight", "tonightBlurb", "f1Title", "f1Blurb"]:
            en_body = re.sub(rf'({k}:\s*")[^"]*(")', rf'\g<1>{escaped_v}\g<2>', en_body)
        elif "_" in k:
            sport, prop = k.split("_", 1)
            # Find sport block: football: { ... prop: "..." }
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
        "todayDesk": "Mesa del martes: Alemania golea 5-0 a Países Bajos. MNF Chargers vencen 23-20 a Ravens en el Harbaugh Bowl. Turín Alcaraz arrolla 6-2, 6-2 a Tiafoe; Zverev ante Shelton esta noche.",
        "todayNfl": "MNF Final: Chargers 23, Ravens 20 en M&T Bank Stadium (Jim vence a John). Domingo Munich: Lions 35-10 Patriots (Gibbs 252 yds).",
        "todayTnf": "NFL Semana 10: Chargers superan 23-20 a Ravens en Monday Night Football. Semana 10 finalizada. Siguiente: Thursday Night Football Semana 11.",
        "football_tagline": "MNF Final: Chargers vencen 23-20 a Ravens en el Harbaugh Bowl; Lions arrollan 35-10 a Patriots en Múnich.",
        "football_liveNow": "MNF: Chargers 23, Ravens 20 (carrera TD 22 yds de Herbert, Hampton 105 yds, fumble forzado por Still). Dom Múnich: Lions 35-10 Patriots.",
        "football_pulse": "MNF FINAL: CHARGERS VENCEN A RAVENS 23-20 EN EL HARBAUGH BOWL CON JIM SUPERANDO A JOHN",
        "tennis_tagline": "Torneo de Maestros Turín: Alcaraz arrolla a Tiafoe 6-2, 6-2; Zverev se mide a Shelton este martes por la noche.",
        "tennis_liveNow": "Lun Lendl: Alcaraz supera a Tiafoe 6-2, 6-2; Medvedev vence a Cobolli 7-6 (4), 6-3. Mar McEnroe: Fils vs Jódar (14:00), Zverev vs Shelton (20:30).",
        "tennis_pulse": "TORNEO DE MAESTROS: ALCARAZ ARROLLA 6-2, 6-2; ZVEREV CONTRA SHELTON ESTA NOCHE EN EL GRUPO MCENROE",
        "f1_tagline": "Dos días para Las Vegas: El Strip listo mientras cinco pilotos luchan por el subcampeonato.",
        "f1_liveNow": "Lucha por P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Las Vegas Strip: 19-21 nov.",
        "f1_pulse": "DOS DÍAS PARA VEGAS: 33 PUNTOS SEPARAN A VERSTAPPEN DE NORRIS ANTES DE LAS PRÁCTICAS DEL JUEVES",
        "soccer_tagline": "Alemania golea 5-0 a Países Bajos en la Liga de Naciones; Inglaterra supera 3-2 a España en Madrid.",
        "soccer_liveNow": "Lun: Alemania 5-0 Países Bajos (Wirtz 60, 77, Scherhant, Schlotterbeck, Gruda); Grecia 1-0 Serbia. Dom: España 2-3 Inglaterra. PL: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "LIGA DE NACIONES: ALEMANIA APLASTA 5-0 A PAÍSES BAJOS Y GANA EL GRUPO A2 CON DOBLETE DE WIRTZ",
        "basketball_tagline": "El Magic sorprende a los Celtics 115-105 y frena la racha de Boston; Heat suman su quinta victoria consecutiva con Giannis.",
        "basketball_liveNow": "Lun: Magic 115-105 Celtics (Bane 24); Heat 128-110 Rockets (Giannis 20/13/6, 5ta victoria seguida); 76ers 135-123 Nets (Embiid 37); Suns 117-105 Nuggets.",
        "basketball_pulse": "NBA LUNES: MAGIC FRENA LA RACHA DE CELTICS 115-105; HEAT SUMAN CINCO SEGUIDAS CON GIANNIS",
        "golf_tagline": "Prácticas de The RSM Classic en Sea Island con tarjetas en juego; McIlroy festeja su 8vo título.",
        "golf_liveNow": "PGA Tour: Comienza la semana del RSM Classic en Sea Island (19-22 nov). Dubái concluido: Hatton -15 (273); McIlroy -10 (278, 8va corona Race to Dubai).",
        "golf_pulse": "PGA TOUR: PRÁCTICAS DEL RSM CLASSIC EN SEA ISLAND CON LAS TARJETAS DEL TOP-125 EN JUEGO",
        "tonight": "Mesa del martes",
        "tonightBlurb": "Monday Night Football: Jim Harbaugh supera a su hermano John en la victoria de Chargers 23-20 sobre Ravens. Lunes: Alemania golea 5-0 a Países Bajos; Magic superan a Celtics 115-105; Alcaraz debuta 6-2, 6-2 en Turín; Zverev se mide a Shelton esta noche.",
        "f1Title": "Dos días para Las Vegas (Ronda 21): 33 puntos separan a Verstappen (279) de Norris (246)",
        "f1Blurb": "Dos días para Las Vegas: El Strip está listo para el duelo entre cinco pilotos detrás del campeón Antonelli (390) y Mercedes (652)."
    },
    "de": {
        "todayDesk": "Dienstags-Desk: Deutschland fegt Niederlande mit 5:0 vom Platz. MNF Chargers schlagen Ravens 23:20 im Harbaugh Bowl. Turin Alcaraz schlägt Tiafoe 6:2, 6:2; Zverev trifft heute auf Shelton.",
        "todayNfl": "MNF Endstand: Chargers 23, Ravens 20 im M&T Bank Stadium (Jim schlägt John). Sonntag München: Lions 35-10 Patriots (Gibbs 252 Yds).",
        "todayTnf": "NFL Woche 10: Chargers bezwingen Ravens mit 23:20 im Monday Night Football. Woche 10 beendet. Als Nächstes: Thursday Night Football Woche 11.",
        "football_tagline": "MNF Endstand: Chargers schlagen Ravens 23:20 im Harbaugh Bowl; Lions demütigen Patriots 35:10 in München.",
        "football_liveNow": "MNF: Chargers 23, Ravens 20 (Herbert 22-Yd TD-Lauf, Hampton 105 Yds, Still erzwang Fumble). So München: Lions 35-10 Patriots (Gibbs 252 Yds, 2 TDs).",
        "football_pulse": "MNF ENDSTAND: CHARGERS SCHLAGEN RAVENS 23:20 IM HARBAUGH BOWL, JIM BEZWINGT JOHN",
        "tennis_tagline": "ATP Finals Turin: Alcaraz fegt über Tiafoe hinweg (6:2, 6:2); Zverev trifft am Dienstagabend auf Shelton.",
        "tennis_liveNow": "Mo Lendl: Alcaraz d Tiafoe 6:2, 6:2; Medvedev d Cobolli 7:6 (4), 6:3. Di McEnroe: Fils vs Jódar (14:00), Zverev vs Shelton (20:30).",
        "tennis_pulse": "ATP FINALS TURIN: ALCARAZ SIEGT 6:2, 6:2; ZVEREV GEGEN SHELTON HEUTE ABEND IN DER MCENROE-GRUPPE",
        "f1_tagline": "Zwei Tage bis Las Vegas: Der Strip ist bereit für den Fünfkampf um die Vizemeisterschaft.",
        "f1_liveNow": "Kampf um P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Las Vegas Strip: 19.-21. Nov.",
        "f1_pulse": "ZWEI TAGE BIS VEGAS: 33 PUNKTE TRENNEN VERSTAPPEN UND NORRIS VOR DEM DONNERSTAGSTRAINING",
        "soccer_tagline": "Deutschland demontiert Niederlande mit 5:0 in der Nations League; England siegt 3:2 in Madrid.",
        "soccer_liveNow": "Mo: Deutschland 5:0 Niederlande (Wirtz 60., 77., Scherhant, Schlotterbeck, Gruda); Griechenland 1:0 Serbien. So: Spanien 2:3 England. PL: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "NATIONS LEAGUE: DEUTSCHLAND FEGT DIE NIEDERLANDE MIT 5:0 VOM PLATZ UND GEWINNT GRUPPE A2",
        "basketball_tagline": "Magic schocken Celtics mit 115:105 und stoppen Bostons Serie; Heat feiern fünften Sieg in Serie mit Giannis.",
        "basketball_liveNow": "Mo: Magic 115:105 Celtics (Bane 24); Heat 128:110 Rockets (Giannis 20/13/6, 5. Sieg in Serie); 76ers 135:123 Nets (Embiid 37); Suns 117:105 Nuggets.",
        "basketball_pulse": "NBA MONTAG: MAGIC STOPPEN CELTICS MIT 115:105; HEAT SIEGEN WEITER MIT GIANNIS",
        "golf_tagline": "RSM Classic Training in Sea Island mit Tourkarten auf dem Spiel; McIlroy feiert 8. Krone.",
        "golf_liveNow": "PGA Tour: RSM Classic Woche beginnt in Sea Island (19.-22. Nov). Dubai beendet: Hatton -15 (273); McIlroy -10 (278, 8. Race to Dubai).",
        "golf_pulse": "PGA TOUR: TRAINING BEI DER RSM CLASSIC IN SEA ISLAND MIT DEN TOP-125 KARTEN AUF DEM SPIEL",
        "tonight": "Dienstags-Desk",
        "tonightBlurb": "Monday Night Football: Jim Harbaugh schlägt seinen Bruder John beim 23:20-Sieg der Chargers über die Ravens. Montag: Deutschland demontiert Niederlande 5:0; Magic bezwingen Celtics 115:105; Alcaraz siegt 6:2, 6:2 in Turin; Zverev trifft heute auf Shelton.",
        "f1Title": "Zwei Tage bis Las Vegas (Runde 21): 33 Punkte trennen Verstappen (279) und Norris (246)",
        "f1Blurb": "Zwei Tage bis Las Vegas: Der Strip ist bereit für das Fünfer-Duell hinter Champion Antonelli (390) und Mercedes (652)."
    },
    "it": {
        "todayDesk": "Desk del martedì: La Germania travolge l'Olanda 5-0. MNF Chargers battono Ravens 23-20 nell'Harbaugh Bowl. Torino Alcaraz liquida Tiafoe 6-2, 6-2; Zverev sfida Shelton stasera.",
        "todayNfl": "MNF Finale: Chargers 23, Ravens 20 al M&T Bank Stadium (Jim batte John). Domenica Monaco: Lions 35-10 Patriots (Gibbs 252 yd).",
        "todayTnf": "NFL Settimana 10: I Chargers piegano i Ravens 23-20 nel Monday Night Football. Settimana 10 conclusa. Prossimo: Thursday Night Football Settimana 11.",
        "football_tagline": "MNF Finale: Chargers battono Ravens 23-20 nell'Harbaugh Bowl; Lions travolgono i Patriots 35-10 a Monaco.",
        "football_liveNow": "MNF: Chargers 23, Ravens 20 (corsa TD di 22 yd di Herbert, Hampton 105 yd, fumble forzato da Still). Dom Monaco: Lions 35-10 Patriots (Gibbs 252 yd, 2 TD).",
        "football_pulse": "MNF FINALE: I CHARGERS PIEGANO I RAVENS 23-20 NELL'HARBAUGH BOWL CON JIM CHE BATTE JOHN",
        "tennis_tagline": "Nitto ATP Finals Torino: Alcaraz domina Tiafoe 6-2, 6-2; Zverev sfida Shelton martedì sera.",
        "tennis_liveNow": "Lun Lendl: Alcaraz batte Tiafoe 6-2, 6-2; Medvedev supera Cobolli 7-6 (4), 6-3. Mar McEnroe: Fils vs Jodar (14:00), Zverev vs Shelton (20:30).",
        "tennis_pulse": "NITTO ATP FINALS: ALCARAZ DOMINA 6-2, 6-2; ZVEREV CONTRO SHELTON STASERA NEL GRUPPO MCENROE",
        "f1_tagline": "Due giorni a Las Vegas: La Strip è pronta per la sfida a cinque per la piazza d'onore mondiale.",
        "f1_liveNow": "Sfida P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Las Vegas Strip: 19-21 nov.",
        "f1_pulse": "DUE GIORNI A VEGAS: 33 PUNTI SEPARANO VERSTAPPEN DA NORRIS PRIMA DELLE PROVE DI GIOVEDÌ",
        "soccer_tagline": "La Germania travolge l'Olanda 5-0 in Nations League; l'Inghilterra batte la Spagna 3-2 a Madrid.",
        "soccer_liveNow": "Lun: Germania 5-0 Olanda (Wirtz 60, 77, Scherhant, Schlotterbeck, Gruda); Grecia 1-0 Serbia. Dom: Spagna 2-3 Inghilterra. PL: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "NATIONS LEAGUE: LA GERMANIA TRAVOLGE L'OLANDA 5-0 E CONQUISTA IL GRUPPO A2",
        "basketball_tagline": "I Magic sorprendono i Celtics 115-105 fermando la striscia di Boston; Miami centra la quinta vittoria con Giannis.",
        "basketball_liveNow": "Lun: Magic 115-105 Celtics (Bane 24); Heat 128-110 Rockets (Giannis 20/13/6, 5a di fila); 76ers 135-123 Nets (Embiid 37); Suns 117-105 Nuggets.",
        "basketball_pulse": "NBA LUNEDÌ: I MAGIC FERMANO I CELTICS 115-105; MIAMI ALLUNGA A CINQUE CON GIANNIS",
        "golf_tagline": "RSM Classic: prove in corso a Sea Island con le carte per il 2027 in palio; McIlroy festeggia l'8° titolo.",
        "golf_liveNow": "PGA Tour: Inizia la settimana del RSM Classic a Sea Island (19-22 nov). Dubai concluso: Hatton -15 (273); McIlroy -10 (278, 8° titolo Race to Dubai).",
        "golf_pulse": "PGA TOUR: PROVE DEL RSM CLASSIC A SEA ISLAND CON LE CARTE DELLA TOP-125 IN PALIO",
        "tonight": "Desk del martedì",
        "tonightBlurb": "Monday Night Football: Jim Harbaugh batte il fratello John con il successo dei Chargers 23-20 sui Ravens. Lunedì: la Germania travolge l'Olanda 5-0; i Magic piegano i Celtics 115-105; Alcaraz vince 6-2, 6-2 a Torino; Zverev sfida Shelton stasera.",
        "f1Title": "Due giorni a Las Vegas (Round 21): 33 punti separano Verstappen (279) da Norris (246)",
        "f1Blurb": "Due giorni a Las Vegas: La Strip è pronta per il duello tra cinque piloti alle spalle del campione Antonelli (390) e della Mercedes (652)."
    },
    "pl": {
        "todayDesk": "Biurko na wtorek: Niemcy rozbijają Holandię 5:0 w Lidze Narodów. MNF Chargers pokonują Ravens 23:20 w Harbaugh Bowl. Turyn Alcaraz pewnie 6:2, 6:2 z Tiafoe; Zverev gra dziś z Sheltonem.",
        "todayNfl": "MNF Koniec: Chargers 23, Ravens 20 na M&T Bank Stadium (Jim wygrywa z Johnem). Niedziela Monachium: Lions 35-10 Patriots (Gibbs 252 jardy).",
        "todayTnf": "NFL Tydzień 10: Chargers wygrywają z Ravens 23:20 w Monday Night Football. Tydzień 10 zakończony. Następnie: Thursday Night Football Tydzień 11.",
        "football_tagline": "MNF Koniec: Chargers wygrywają 23:20 z Ravens w Harbaugh Bowl; Lions gromią Patriots 35:10 w Monachium.",
        "football_liveNow": "MNF: Chargers 23, Ravens 20 (bieg TD 22 yds Herberta, Hampton 105 yds, Still wymusił fumble). Niedz Monachium: Lions 35-10 Patriots (Gibbs 252 yds, 2 TD).",
        "football_pulse": "MNF KONIEC: CHARGERS WYGRYWAJĄ Z RAVENS 23:20 W HARBAUGH BOWL, JIM POKONUJE JOHNA",
        "tennis_tagline": "ATP Finals w Turynie: Alcaraz pewnie pokonuje Tiafoe 6:2, 6:2; Zverev zagra we wtorek wieczorem z Sheltonem.",
        "tennis_liveNow": "Pon Lendl: Alcaraz d Tiafoe 6:2, 6:2; Medvedev d Cobolli 7:6 (4), 6:3. Wt McEnroe: Fils vs Jodar (14:00), Zverev vs Shelton (20:30).",
        "tennis_pulse": "ATP FINALS: ALCARAZ ZWYCIĘŻA 6:2, 6:2; ZVEREV KONTRA SHELTON DZIŚ WIECZOREM W GRUPIE MCENROE",
        "f1_tagline": "Dwa dni do Vegas: Tor na Strip gotowy na pięcioosobową batalię o wicemistrzostwo.",
        "f1_liveNow": "Walka o P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Las Vegas Strip: 19-21 listopada.",
        "f1_pulse": "DWA DNI DO VEGAS: 33 PUNKTY DZIELĄ VERSTAPPENA I NORRISA PRZED CZWARTKOWYMI TRENINGAMI",
        "soccer_tagline": "Niemcy rozbijają Holandię 5:0 w Lidze Narodów; Anglia pokonuje Hiszpanię 3:2 w Madrycie.",
        "soccer_liveNow": "Pon: Niemcy 5:0 Holandia (Wirtz 60, 77, Scherhant, Schlotterbeck, Gruda); Grecja 1:0 Serbia. Niedz: Hiszpania 2:3 Anglia. PL: Arsenal 27, Brighton 22, City 21.",
        "soccer_pulse": "LIGA NARODÓW: NIEMCY ROZBIJAJĄ HOLANDIĘ 5:0 I WYGRYWAJĄ GRUPĘ A2 Z DUBLETEM WIRTZA",
        "basketball_tagline": "Magic sprawiają niespodziankę i ogrywają Celtics 115:105; Heat z piątą z rzędu wygraną z Giannisem.",
        "basketball_liveNow": "Pon: Magic 115:105 Celtics (Bane 24); Heat 128:110 Rockets (Giannis 20/13/6, 5. z rzędu); 76ers 135:123 Nets (Embiid 37); Suns 117:105 Nuggets.",
        "basketball_pulse": "NBA PONIEDZIAŁEK: MAGIC PRZERYWAJĄ SERIĘ CELTICS 115:105; HEAT Z PIĄTĄ WYGRANĄ Z RZĘDU",
        "golf_tagline": "Treningi przed RSM Classic w Sea Island z kartami na 2027 na szali; McIlroy świętuje 8. koronę.",
        "golf_liveNow": "PGA Tour: Tydzień turniejowy RSM Classic rusza w Sea Island (19-22 listopada). Dubaj: Hatton -15 (273); McIlroy -10 (278, 8. tytuł Race to Dubai).",
        "golf_pulse": "PGA TOUR: TRENINGI PRZED RSM CLASSIC W SEA ISLAND Z KARTAMI TOP-125 W GRZE",
        "tonight": "Biurko na wtorek",
        "tonightBlurb": "Monday Night Football: Jim Harbaugh pokonuje brata Johna, gdy Chargers ogrywają Ravens 23:20. Poniedziałek: Niemcy gromią Holandię 5:0; Magic zatrzymują Celtics 115:105; Alcaraz wygrywa 6:2, 6:2 w Turynie; Zverev gra dziś z Sheltonem.",
        "f1Title": "Dwa dni do Las Vegas (Runda 21): 33 punkty dzielą Verstappena (279) od Norrisa (246)",
        "f1Blurb": "Dwa dni do Las Vegas: Tor na Strip czeka na pojedynek pięciu kierowców za mistrzem Antonellim (390) i Mercedesem (652)."
    },
    "zh": {
        "todayDesk": "周二工作台：德国5-0狂胜荷兰登顶A2组。周一夜赛闪电23-20险胜乌鸦哈博兄弟战。都灵总决赛阿尔卡拉斯6-2、6-2横扫蒂亚福；兹维列夫今晚战谢尔顿。",
        "todayNfl": "周一夜赛完场：闪电23-20力克乌鸦（吉姆胜约翰）。周日慕尼黑赛：雄狮35-10爱国者（吉布斯252码）。",
        "todayTnf": "NFL第10周：闪电23-20险胜乌鸦。第10周收官。下场：第11周周四夜赛。",
        "football_tagline": "周一夜赛完场：哈博兄弟德比闪电23-20力克乌鸦；雄狮慕尼黑35-10大胜爱国者。",
        "football_liveNow": "MNF：闪电23-20乌鸦（赫伯特22码TD冲球，汉普顿105码，斯蒂尔关键迫使掉球）。周日慕尼黑：雄狮35-10爱国者（吉布斯252码2TD）。",
        "football_pulse": "周一夜赛完场：闪电23-20险胜乌鸦赢得哈博德比，吉姆击败兄长约翰",
        "tennis_tagline": "都灵总决赛：阿尔卡拉斯6-2、6-2轻取蒂亚福；兹维列夫周二晚大战谢尔顿。",
        "tennis_liveNow": "周一伦德尔组：阿尔卡拉斯6-2、6-2胜蒂亚福；梅德韦杰夫7-6、6-3胜科博利。周二麦肯罗组：菲斯对霍达尔（14:00），兹维列夫对谢尔顿（20:30）。",
        "tennis_pulse": "ATP都灵总决赛：阿尔卡拉斯横扫首胜；兹维列夫今晚迎战谢尔顿重现美网决战",
        "f1_tagline": "拉斯维加斯站倒计时2天：赌城大道就绪，五大车手展开年度亚军激烈厮杀。",
        "f1_liveNow": "年度次席之争：维斯塔潘279，拉塞尔262，汉密尔顿261，勒克莱尔249，诺里斯246（安东内利390；梅赛德斯652）。赌城大道：19-21日。",
        "f1_pulse": "拉斯维加斯倒计时2天：维斯塔潘至诺里斯仅差33分，周四练习赛前白热化",
        "soccer_tagline": "德国队5-0狂胜荷兰斩获欧国联A2组头名；英格兰3-2力克西班牙。",
        "soccer_liveNow": "周一：德国5-0荷兰（维尔茨60、77，谢尔汉特，施洛特贝克，格鲁达）；希腊1-0塞尔维亚。周日：西班牙2-3英格兰。英超：阿森纳27，布莱顿22，曼城21。",
        "soccer_pulse": "欧国联焦点：德国5-0大胜荷兰锁定A2组头名；维尔茨双响闪耀莱比锡",
        "basketball_tagline": "魔术115-105逆转凯尔特人终结对手连胜；热火在字母哥带领下豪取五连胜。",
        "basketball_liveNow": "周一：魔术115-105凯尔特人（贝恩24分）；热火128-110火箭（字母哥20/13/6，五连胜）；76人135-123篮网（恩比德37分）；太阳117-105掘金。",
        "basketball_pulse": "NBA周一：魔术第四节发威115-105力克凯尔特人；热火豪取五连胜",
        "golf_tagline": "海岛RSM精英赛开启官方练习轮，保卡战一触即发；麦克罗伊庆祝第八冠。",
        "golf_liveNow": "美巡赛：RSM精英赛海岛开战（11月19-22日）。迪拜收官：哈顿-15（273）；麦克罗伊-10（278，加冕第8座迪拜总冠军）。",
        "golf_pulse": "美巡赛秋季收官：海岛RSM精英赛打响官方练习轮，前125全卡争夺激烈",
        "tonight": "周二工作台",
        "tonightBlurb": "周一夜赛：吉姆-哈博率闪电23-20险胜兄长约翰执教的乌鸦。周一赛况：德国5-0横扫荷兰夺头名；魔术115-105翻盘凯尔特人；阿尔卡拉斯都灵6-2、6-2轻松过关；兹维列夫今晚麦肯罗组对决谢尔顿。",
        "f1Title": "拉斯维加斯大奖赛倒计时2天：33分差距分化维斯塔潘（279）至诺里斯（246）",
        "f1Blurb": "拉斯维加斯站倒计时2天：双冠王安东内利（390）与梅赛德斯（652）之后，五位车手在赌城大道争夺年度亚军。"
    },
    "ja": {
        "todayDesk": "火曜デスク：ドイツがオランダを5-0粉砕しA2組首位確定。MNFチャージャーズ23-20レイブンズ（ハーボー対決）。トリノでアルカラス快勝、今夜ズベレフ対シェルトン。",
        "todayNfl": "MNF終了：チャージャーズ23-20レイブンズ（ジムが兄ジョンに勝利）。日曜ミュンヘン：ライオンズ35-10ペイトリオッツ（ギブス252yd）。",
        "todayTnf": "NFL第10週：チャージャーズがマンデーナイトでレイブンズを23-20で撃破。第10週終了。次回：第11週サーズデーナイト。",
        "football_tagline": "MNF試合終了：チャージャーズが23-20でレイブンズに競り勝ちハーボー対決制す；ライオンズがミュンヘンで35-10大勝。",
        "football_liveNow": "MNF：チャージャーズ23-20レイブンズ（ハーバート22yd TDラン、ハンプトン105yd、スティール決勝ファンブル）。日曜ミュンヘン：ライオンズ35-10ペイトリオッツ。",
        "football_pulse": "MNF試合終了：チャージャーズが23-20でレイブンズを下しハーボー対決でジムが勝利",
        "tennis_tagline": "ATPファイナルズ・トリノ：アルカラスがティアフォーに6-2、6-2快勝；火曜夜にズベレフ対シェルトン。",
        "tennis_liveNow": "月曜レンドル組：アルカラス6-2、6-2ティアフォー；メドベージェフ7-6 (4)、6-3コボッリ。火曜マッケンロー組：フィス対ホダール（14:00）、ズベレフ対シェルトン（20:30）。",
        "tennis_pulse": "ATPファイナルズ・トリノ：アルカラスが6-2、6-2で圧勝；今夜マッケンロー組でズベレフ対シェルトン",
        "f1_tagline": "ラスベガス開幕まであと2日：ストリップ準備完了、5人によるシリーズ2位争いが激化。",
        "f1_liveNow": "ドライバーズ2位争い：フェルスタッペン279、ラッセル262、ハミルトン261、ルクレール249、ノリス246（アントネッリ390；メルセデス652）。ラスベガス：19-21日。",
        "f1_pulse": "ベガスまであと2日：フェルスタッペンからノリスまでわずか33点差、木曜フリー走行へ",
        "soccer_tagline": "ドイツがネーションズリーグでオランダを5-0粉砕；イングランドはマドリードでスペインを3-2撃破。",
        "soccer_liveNow": "月曜：ドイツ5-0オランダ（ヴィルツ60, 77、シェルハント、シュロッターベック、グルーダ）；ギリシャ1-0セルビア。日曜：スペイン2-3イングランド。PL：アーセナル27、ブライトン22、シティ21。",
        "soccer_pulse": "ネーションズリーグ：ドイツがオランダを5-0粉砕してA2組首位獲得；ヴィルツ2発",
        "basketball_tagline": "マジックがセルティックスを115-105で下し連勝阻止；ヒートはヤニス躍動で5連勝。",
        "basketball_liveNow": "月曜：マジック115-105セルティックス（ベイン24）；ヒート128-110ロケッツ（ヤニス20/13/6、5連勝）；シクサーズ135-123ネッツ（エンビード37）；サンズ117-105ナゲッツ。",
        "basketball_pulse": "NBA月曜：マジックが115-105でセルティックスの連勝ストップ；ヒート5連勝",
        "golf_tagline": "シーアイランドでRSMクラシック公式練習開始（来季シード125枠争い）；マキロイ8度目年間王者。",
        "golf_liveNow": "PGAツアー：シーアイランドでRSMクラシック開幕週（11月19-22日）。ドバイ終了：ハットン-15（273）；マキロイ-10（278、8度目の欧州制覇）。",
        "golf_pulse": "PGAツアー秋季最終戦：シーアイランドでRSMクラシック公式練習開始、シード争奪戦",
        "tonight": "火曜デスク",
        "tonightBlurb": "MNF：ジム・ハーボー率いるチャージャーズが兄ジョンのレイブンズを23-20で撃破。月曜：ドイツがオランダを5-0粉砕；マジックがセルティックスに逆転勝ち；アルカラスがトリノ快勝；今夜ズベレフ対シェルトン。",
        "f1Title": "第21戦ラスベガス開幕まであと2日：フェルスタッペン（279）からノリス（246）まで33点差",
        "f1Blurb": "ラスベガス開幕まであと2日：戴冠済みのアントネッリ（390）とメルセデス（652）の背後で5人のドライバーがストリップで激突。"
    },
    "ko": {
        "todayDesk": "화요일 데스크: 독일 네덜란드 5-0 대파 A2조 1위. MNF 차저스 23-20 레이븐스 하보 볼 승리. 토리노 알카라스 6-2, 6-2 완승; 오늘 밤 즈베레프 vs 셸턴 격돌.",
        "todayNfl": "MNF 경기 종료: 차저스 23-20 레이븐스 (짐이 형 존 꺾음). 일요일 뮌헨: 라이온스 35-10 패트리어츠 (깁스 252야드).",
        "todayTnf": "NFL 10주차: 차저스가 먼데이 나이트서 레이븐스를 23-20으로 꺾었습니다. 10주차 종료. 다음 경기: 11주차 서스데이 나이트.",
        "football_tagline": "MNF 경기 종료: 차저스, 하보 볼에서 레이븐스 23-20 제압; 라이온스 뮌헨서 패트리어츠 35-10 대파.",
        "football_liveNow": "MNF: 차저스 23-20 레이븐스 (허버트 22야드 TD 러싱, 햄튼 105야드, 스틸 결정적 펌블). 일요일 뮌헨: 라이온스 35-10 패트리어츠 (깁스 252야드, 2TD).",
        "football_pulse": "MNF 경기 종료: 차저스가 레이븐스를 23-20으로 꺾고 하보 볼 승리, 짐 하보 형 존 제압",
        "tennis_tagline": "토리노 ATP 파이널스: 알카라스, 티아포에 6-2, 6-2 완승; 화요일 밤 즈베레프-셸턴 빅매치.",
        "tennis_liveNow": "월요일 렌들 조: 알카라스 d 티아포 6-2, 6-2; 메드베데프 d 코볼리 7-6 (4), 6-3. 화요일 매켄로 조: 필스 vs 호다르 (14:00), 즈베레프 vs 셸턴 (20:30).",
        "tennis_pulse": "토리노 ATP 파이널스: 알카라스 6-2, 6-2 완승 출발; 오늘 밤 매켄로 조 즈베레프 vs 셸턴 격돌",
        "f1_tagline": "라스베이거스 스트립 D-2: 드라이버 준우승 5인 혼전 속 서킷 준비 완료.",
        "f1_liveNow": "드라이버 P2 싸움: 베르스타펜 279, 러셀 262, 해밀턴 261, 르클레르 249, 노리스 246 (안토넬리 390; 메르세데스 652). 라스베이거스 스트립: 11월 19-21일.",
        "f1_pulse": "베이거스 개막 D-2: 목요일 연습 주행 앞두고 베르스타펜부터 노리스까지 33점 차 대접전",
        "soccer_tagline": "독일, 네이션스리그서 네덜란드 5-0 대파하고 A2조 1위; 잉글랜드 마드리드서 스페인 3-2 제압.",
        "soccer_liveNow": "월요일: 독일 5-0 네덜란드 (비르츠 60, 77, 셰르한트, 슐로터베크, 그루다); 그리스 1-0 세르비아. 일요일: 스페인 2-3 잉글랜드. PL: 아스널 27, 브라이튼 22, 맨시티 21.",
        "soccer_pulse": "네이션스리그: 독일, 네덜란드 5-0 대파하고 A2조 1위 확정; 비르츠 멀티골 맹활약",
        "basketball_tagline": "매직, 셀틱스 115-105 격파하고 연승 저지; 히트는 아데토쿤보 앞세워 5연승.",
        "basketball_liveNow": "월요일: 매직 115-105 셀틱스 (베인 24); 히트 128-110 로케츠 (야니스 20/13/6, 5연승); 식서스 135-123 네츠 (엠비드 37); 선즈 117-105 너기츠.",
        "basketball_pulse": "NBA 월요일: 매직이 115-105로 셀틱스 연승 저지; 히트 5연승 질주",
        "golf_tagline": "시 아일랜드서 RSM 클래식 공식 연습 개막 (125위 잔류전); 매킬로이 8번째 왕관 환호.",
        "golf_liveNow": "PGA 투어: 시 아일랜드서 RSM 클래식 대회 주간 개막 (11월 19-22일). 두바이 최종: 해튼 -15 (273); 매킬로이 -10 (278, 통산 8번째 시즌 챔피언).",
        "golf_pulse": "PGA 투어 가을 피날레: 시 아일랜드서 RSM 클래식 공식 연습 개막, 125위 잔류 혈투",
        "tonight": "화요일 데스크",
        "tonightBlurb": "먼데이 나이트: 짐 하보의 차저스가 형 존의 레이븐스를 23-20으로 제압. 월요일: 독일이 네덜란드를 5-0 대파; 매직이 셀틱스를 115-105로 역전승; 알카라스 토리노 6-2, 6-2 완승; 오늘 밤 즈베레프 vs 셸턴 격돌.",
        "f1Title": "21라운드 라스베이거스 개막 D-2: 33점 차 베르스타펜 (279)부터 노리스 (246)까지",
        "f1Blurb": "라스베이거스 개막 D-2: 챔피언 안토넬리 (390)와 메르세데스 (652) 뒤를 이어 5명의 드라이버가 스트립에서 2위 쟁탈전을 펼칩니다."
    },
    "ar": {
        "todayDesk": "مكتب الثلاثاء: ألمانيا تسحق هولندا 5-0 في دوري الأمم. تشارجرز يهزم ريفنز 23-20 في مواجهة الأخوين هاربوه. ألكاراز يكتسح تيافو 6-2 و6-2؛ زفيريف يواجه شيلتون الليلة.",
        "todayNfl": "ختام ليلة الاثنين: تشارجرز 23، ريفنز 20 في بالتيمور (جيم يهزم جون). الأحد في ميونخ: لايونز 35-10 باتريوتس (غيبس 252 ياردة).",
        "todayTnf": "NFL الجولة 10: تشارجرز يهزم ريفنز 23-20 في ختام ليلة الاثنين. انتهاء الجولة 10. القادم: ليلة الخميس للجولة 11.",
        "football_tagline": "ختام ليلة الاثنين: تشارجرز يهزم ريفنز 23-20 في مواجهة الإخوة هاربوه؛ لايونز يكتسح باتريوتس 35-10 في ميونخ.",
        "football_liveNow": "ختام ليلة الاثنين: تشارجرز 23، ريفنز 20 (هربرت يركض 22 ياردة، هامبتون 105 ياردات، ستيل يجبر على فقدان الكرة). الأحد ميونخ: لايونز 35-10 باتريوتس.",
        "football_pulse": "ختام ليلة الاثنين: تشارجرز يهزم ريفنز 23-20 في مواجهة الإخوة هاربوه، وجيم يتفوق على جون",
        "tennis_tagline": "نهائيات تورينو: ألكاراز يكتسح تيافو 6-2، 6-2؛ زفيريف يواجه شيلتون مساء الثلاثاء.",
        "tennis_liveNow": "الاثنين ليندل: ألكاراز يهزم تيافو 6-2، 6-2؛ ميدفيديف يهزم كوبولي 7-6 (4)، 6-3. الثلاثاء ماكنرو: فيس ضد خودار (14:00)، زفيريف ضد شيلتون (20:30).",
        "tennis_pulse": "نهائيات تورينو للتنس: ألكاراز يكتسح 6-2 و6-2؛ زفيريف يلتقي شيلتون الليلة في قمة مجموعة ماكنرو",
        "f1_tagline": "يومان على انطلاق جائزة لاس فيغاس: حلبة ستريب جاهزة وصراع الوصافة يشتعل بين خمسة سائقين.",
        "f1_liveNow": "صراع وصافة السائقين: فيرستابن 279، راسل 262، هاميلتون 261، لوكلير 249، نوريس 246 (أنتونيللي 390؛ مرسيدس 652). حلبة لاس فيغاس: 19-21 نوفمبر.",
        "f1_pulse": "يومان على جائزة لاس فيغاس: 33 نقطة تفصل فيرستابن عن نوريس قبل انطلاق تجارب الخميس",
        "soccer_tagline": "ألمانيا تسحق هولندا 5-0 لتتصدر مجموعتها في دوري الأمم؛ إنجلترا تهزم إسبانيا 3-2 في مدريد.",
        "soccer_liveNow": "الاثنين: ألمانيا 5-0 هولندا (فيرتز 60، 77، شيرهانت، شلوتربيك، غرودا)؛ اليونان 1-0 صربيا. الأحد: إسبانيا 2-3 إنجلترا. الدوري الإنجليزي: أرسنال 27، برايتon 22، سيتي 21.",
        "soccer_pulse": "دوري الأمم الأوروبية: ألمانيا تسحق هولندا 5-0 وتتصدر المجموعة الثانية بثنائية فيرتز",
        "basketball_tagline": "ماجيك يفاجئ سلتيكس 115-105 ويوقف سلسلة بوسطن؛ ميامي هيت يواصل انتصاراته المتتالية بفضل يانيس.",
        "basketball_liveNow": "الاثنين: ماجيك 115-105 سلتيكس (بين 24)؛ هيت 128-110 روكتس (يانيس 20/13/6، 5 انتصارات متتالية)؛ 76ers 135-123 نتس (إمبيد 37)؛ صنز 117-105 ناغتس.",
        "basketball_pulse": "دوري السلة الأمريكي الاثنين: ماجيك يوقف سلسلة سلتيكس بالفوز 115-105؛ ميامي يحقق فوزه الخامس تواليا",
        "golf_tagline": "انطلاق تدريبات آر إس إم كلاسيك في سي آيلاند مع صراع البطاقات؛ ماكلروي يحتفل بلقبه الثامن.",
        "golf_liveNow": "جولة البي جي إيه: أسبوع بطولة آر إس إم كلاسيك يبدأ في سي آيلاند (19-22 نوفمبر). ختام دبي: هاتون -15 (273)؛ ماكلروي -10 (278، اللقب الثامن).",
        "golf_pulse": "جولة البي جي إيه: تدريبات آر إس إم كلاسيك تنطلق في سي آيلاند والبطاقات على المحك",
        "tonight": "مكتب الثلاثاء",
        "tonightBlurb": "ليلة الاثنين: جيم هاربوه يهزم شقيقه جون بفوز تشارجرز 23-20 على ريفنز. الاثنين: ألمانيا تكتسح هولندا 5-0؛ ماجيك يفاجئ سلتيكس 115-105؛ ألكاراز يتألق في تورينو 6-2 و6-2؛ زفيريف يلتقي شيلتون الليلة.",
        "f1Title": "يومان على جائزة لاس فيغاس (الجولة 21): 33 نقطة تفصل فيرستابن (279) عن نوريس (246)",
        "f1Blurb": "يومان على جائزة لاس فيغاس: حلبة ستريب جاهزة لمعركة المركز الثاني بين خمسة سائقين خلف البطل أنتونيللي (390) ومرسيدس (652)."
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

