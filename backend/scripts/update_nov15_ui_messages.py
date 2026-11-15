"""
update_nov15_ui_messages.py
Updates playground.ts and all 10 messages*.ts for 15 Nov 2026.
"""
import re
import os

def update_playground():
    path = "frontend/src/i18n/playground.ts"
    content = open(path, "r", encoding="utf-8").read()

    majors_done_map = {
        "en": "Dubai Finale Complete: Tyrrell Hatton -15 (273) wins by 5; Rory McIlroy -10 (278) seals 8th Race to Dubai title.",
        "fr": "Finale de Dubai terminee : Tyrrell Hatton -15 (273) gagne de 5 coups ; Rory McIlroy -10 (278) scelle sa 8e Race to Dubai.",
        "es": "Final de Dubai completa: Tyrrell Hatton -15 (273) gana por 5 golpes; Rory McIlroy -10 (278) sella su 8va Race to Dubai.",
        "de": "Dubai Finale komplett: Tyrrell Hatton -15 (273) siegt mit 5 Schlaegen; Rory McIlroy -10 (278) holt 8. Race to Dubai-Titel.",
        "it": "Finale di Dubai completata: Tyrrell Hatton -15 (273) vince con 5 colpi; Rory McIlroy -10 (278) sigilla l'8a Race to Dubai.",
        "pl": "Final w Dubaju zakonczony: Tyrrell Hatton -15 (273) wygrywa z przewaga 5 uderzen; Rory McIlroy -10 (278) z 8. tytulem Race to Dubai.",
        "zh": "迪拜总决赛收官：泰瑞尔·哈顿-15（273杆）五杆大胜；麦克罗伊-10（278杆）锁定第八座迪拜竞赛总冠军。",
        "ja": "ドバイ最終戦終了：ティレル・ハットンが通算-15（273）で5打差圧勝；ローリー・マキロイが-10（278）で8度目の年間王座戴冠。",
        "ko": "두바이 최종전 종료: 타렐 해튼 -15(273타)로 5타 차 완승; 로리 매킬로이 -10(278타)로 통산 8번째 레이스 투 두바이 제패.",
        "ar": "ختام دبي مكتمل: تيريل هاتون -15 (273) يفوز بفارق 5 ضربات؛ وروري مكلروي -10 (278) يحسم لقبه الثامن في السباق إلى دبي.",
    }

    pin_final_map = {
        "en": "Turin Sunday: Zverev d Jodar 6-4, 6-4; Shelton vs Fils tonight. Stockholm Sat Final: Fritz d Tirante 6-2, 4-6, 7-6 (3).",
        "fr": "Turin dimanche : Zverev bat Jodar 6-4, 6-4 ; Shelton vs Fils ce soir. Stockholm samedi : Fritz bat Tirante 6-2, 4-6, 7-6 (3).",
        "es": "Turin domingo: Zverev vence a Jodar 6-4, 6-4; Shelton vs Fils esta noche. Estocolmo sabado: Fritz vence a Tirante 6-2, 4-6, 7-6 (3).",
        "de": "Turin Sonntag: Zverev besiegt Jodar 6:4, 6:4; Shelton vs. Fils heute Abend. Stockholm Samstag: Fritz schlaegt Tirante 6:2, 4:6, 7:6 (3).",
        "it": "Torino domenica: Zverev batte Jodar 6-4, 6-4; stasera Shelton vs Fils. Stoccolma sabato: Fritz batte Tirante 6-2, 4-6, 7-6 (3).",
        "pl": "Turyn niedziela: Zverev pokonuje Jodara 6:4, 6:4; wieczorem Shelton vs Fils. Sztokholm sobota: Fritz bije Tirante 6:2, 4:6, 7:6 (3).",
        "zh": "都灵周日：兹维列夫6-4、6-4轻取霍达尔；今晚谢尔顿对菲斯。斯德哥尔摩周六决赛：弗里茨6-2、4-6、7-6（3）胜蒂兰特。",
        "ja": "トリノ日曜：ズベレフがジョダルに6-4、6-4で完勝；今夜シェルトン対フィス。ストックホルム土曜決勝：フリッツがティランテを6-2、4-6、7-6（3）で破り優勝。",
        "ko": "토리노 일요일: 즈베레프 호다르에 6-4, 6-4 완승; 오늘 밤 셸턴 vs 피스. 스톡홀름 토요 결승: 프리츠 티란테에 6-2, 4-6, 7-6(3) 승리.",
        "ar": "تورينو الأحد: زفيريف يهزم خودار 6-4 و6-4؛ شيلتون ضد فيلس الليلة. ستوكهولم السبت: فريتز يهزم تيرانتي 6-2 و4-6 و7-6 (3).",
    }

    pl_foot_map = {
        "en": "Sunday: Spain vs England 19:45 GMT Metropolitano. Sat: Denmark 4-1 Portugal; Sweden 3-2 Bosnia. PL: Arsenal 27, Brighton 22, City 21.",
        "fr": "Dimanche : Espagne vs Angleterre 19h45 GMT Metropolitano. Samedi : Danemark 4-1 Portugal ; Suede 3-2 Bosnie. PL : Arsenal 27, Brighton 22, City 21.",
        "es": "Domingo: Espana vs Inglaterra 19:45 GMT Metropolitano. Sabado: Dinamarca 4-1 Portugal; Suecia 3-2 Bosnia. PL: Arsenal 27, Brighton 22, City 21.",
        "de": "Sonntag: Spanien vs. England 19:45 GMT Metropolitano. Samstag: Daenemark 4:1 Portugal; Schweden 3:2 Bosnien. PL: Arsenal 27, Brighton 22, City 21.",
        "it": "Domenica: Spagna vs Inghilterra 19:45 GMT Metropolitano. Sabato: Danimarca 4-1 Portogallo; Svezia 3-2 Bosnia. PL: Arsenal 27, Brighton 22, City 21.",
        "pl": "Niedziela: Hiszpania vs Anglia 19:45 GMT Metropolitano. Sobota: Dania 4:1 Portugalia; Szwecja 3:2 Bosnia. PL: Arsenal 27, Brighton 22, City 21.",
        "zh": "周日：西班牙对英格兰19:45大都会球场。周六：丹麦4-1葡萄牙；瑞典3-2波黑。英超：阿森纳27分领跑。",
        "ja": "日曜：スペイン対イングランド19:45 GMTメトロポリターノ。土曜：デンマーク4-1ポルトガル；スウェーデン3-2ボスニア。PL首位アーセナル27点。",
        "ko": "일요일: 스페인 vs 잉글랜드 19:45 GMT 메트로폴리타노. 토요일: 덴마크 4-1 포르투갈; 스웨덴 3-2 보스니아. PL 아스널 27점 선두.",
        "ar": "الأحد: إسبانيا ضد إنجلترا 19:45 غرينتش في ميتروبوليتانو. السبت: الدنمارك 4-1 البرتغال؛ السويد 3-2 البوسنة. أرسنال 27 في الصدارة.",
    }

    for loc, val in majors_done_map.items():
        loc_pattern = rf'("{loc}":\s*\{{[^}}]*?"majorsDone":\s*)"([^"]*)"'
        content = re.sub(loc_pattern, rf'\g<1>"{val}"', content, count=1, flags=re.DOTALL)

    for loc, val in pin_final_map.items():
        loc_pattern = rf'("{loc}":\s*\{{[^}}]*?"pinFinal":\s*)"([^"]*)"'
        content = re.sub(loc_pattern, rf'\g<1>"{val}"', content, count=1, flags=re.DOTALL)

    for loc, val in pl_foot_map.items():
        loc_pattern = rf'("{loc}":\s*\{{[^}}]*?"plFootnote":\s*)"([^"]*)"'
        content = re.sub(loc_pattern, rf'\g<1>"{val}"', content, count=1, flags=re.DOTALL)

    open(path, "w", encoding="utf-8", newline="\n").write(content)
    print("Updated playground.ts.")

def update_messages():
    # 1. messages.ts (en and fr)
    path_main = "frontend/src/i18n/messages.ts"
    content_main = open(path_main, "r", encoding="utf-8").read()

    m_split = re.search(r'(export const fr(?::\s*Messages)?\s*=\s*\{)', content_main)
    en_block = content_main[:m_split.start()]
    fr_block = content_main[m_split.start():]

    en_today = "Sunday desk: Munich Lions lead Patriots 21-3 at half. Spain vs England 19:45 GMT Madrid. Dubai Final: Hatton -15 (273), McIlroy 8th title."
    en_tonight = "Lions lead Patriots 21-3 in Munich with Maye injured. Spain host England tonight in Madrid for Group A3 decider. Turin ATP Finals: Zverev sweeps Jodar 6-4, 6-4; Shelton vs Fils tonight. Dubai Final: Hatton fires 66 to win on -15 (273); McIlroy pips Chacarra for eighth Race to Dubai crown."
    en_nfl = "NFL Munich Live: Lions 21, Patriots 3 at half. Drake Maye out with ankle injury; St. Brown 56-yd TD, Gibbs TD. Sunday early slate 1:00 p.m. ET."
    en_tnf = "NFL Week 10: Lions lead Patriots 21-3 in Munich. Thursday Final: Commanders 24-21 Giants. Sunday slate underway."

    # EN football
    en_block = re.sub(r'todayDesk:\s*"[^"]*"', f'todayDesk: "{en_today}"', en_block, count=1)
    en_block = re.sub(r'todayNfl:\s*"[^"]*"', f'todayNfl: "{en_nfl}"', en_block, count=1)
    en_block = re.sub(r'todayTnf:\s*"[^"]*"', f'todayTnf: "{en_tnf}"', en_block, count=1)
    en_block = re.sub(r'tonightBlurb:\s*"[^"]*"', f'tonightBlurb: "{en_tonight}"', en_block, count=1)

    en_block = re.sub(r'(football:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"NFL Munich Live: Lions lead Patriots 21-3 at half; Drake Maye exits with ankle injury."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(football:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"LIVE Munich: Lions 21, Patriots 3 (St. Brown 56-yd TD, Gibbs TD, Borregales 33-yd FG). Maye hurt ankle. 2nd half in progress."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(football:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"NFL MUNICH LIVE: LIONS LEAD PATRIOTS 21-3 AT HALF; DRAKE MAYE RULED OUT WITH ANKLE INJURY"', en_block, count=1, flags=re.DOTALL)

    en_block = re.sub(r'(soccer:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Spain host England tonight in Madrid (19:45 GMT) for Group A3; Denmark stun Portugal 4-1."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(soccer:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Tonight: Spain vs England, 19:45 GMT Metropolitano. Sat: Denmark 4-1 Portugal; Sweden 3-2 Bosnia. PL: Arsenal 27, Brighton 22, City 21."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(soccer:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"SPAIN VS ENGLAND TONIGHT IN MADRID; DENMARK STUN PORTUGAL 4-1 IN NATIONS LEAGUE"', en_block, count=1, flags=re.DOTALL)

    en_block = re.sub(r'(basketball:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Giannis 34 leads Heat 137-117 over Pistons; Proctor triple-double powers short-handed Cavs 127-117."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(basketball:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Sat: Heat 137-117 Pistons (Giannis 34, Klay 26, Cade 33); Cavs 127-117 Mavs (Proctor 24/11/10). Fri: Spurs 123-85 Warriors (11 straight)."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(basketball:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"NBA SATURDAY: HEAT 137-117 PISTONS, GIANNIS 34; PROCTOR TRIPLE-DOUBLE LEADS CAVS OVER MAVS"', en_block, count=1, flags=re.DOTALL)

    en_block = re.sub(r'(golf:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Dubai Finale Complete: Tyrrell Hatton fires 66 to win by 5 at -15; Rory McIlroy seals 8th Race to Dubai title."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(golf:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Dubai Final: 1. Tyrrell Hatton -15 (273, 66); 2. Rory McIlroy -10 (278, 67, Race to Dubai champion); T3. Chacarra -9 (279), Lindell -9. Final."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(golf:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"DUBAI FINALE: HATTON WINS ON 273 (-15); MCILROY (278, -10) SEALS EIGHTH RACE TO DUBAI CROWN"', en_block, count=1, flags=re.DOTALL)

    en_block = re.sub(r'(tennis:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Turin ATP Finals: Zverev sweeps Jodar 6-4, 6-4; Fritz outlasts Tirante in Stockholm final."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(tennis:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Turin Sun: Zverev d Jodar 6-4, 6-4; Shelton vs Fils tonight (20:30 CET). Stockholm Sat Final: Fritz d Tirante 6-2, 4-6, 7-6 (3)."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(tennis:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"TURIN ATP FINALS OPEN: ZVEREV SWEEPS JODAR 6-4, 6-4; FRITZ WINS STOCKHOLM IN DECIDING TIEBREAK"', en_block, count=1, flags=re.DOTALL)

    en_block = re.sub(r'(f1:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Four days to Round 21 Las Vegas: 33 points still split Verstappen to Norris. No Strip race yet."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(f1:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Drivers P2 race unchanged: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Round 21: 19-21 Nov."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(f1:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"FOUR DAYS TO VEGAS: VERSTAPPEN TO NORRIS STILL 33 PTS BEHIND CHAMPION ANTONELLI"', en_block, count=1, flags=re.DOTALL)

    # FR updates
    fr_today = "Bureau du dimanche : les Lions menent 21-3 a Munich. Espagne-Angleterre a 19h45 GMT a Madrid. Finale de Dubai : Hatton -15 (273), 8e titre pour McIlroy."
    fr_tonight = "Les Lions menent 21-3 a Munich contre New England. L'Espagne recoit l'Angleterre ce soir a Madrid pour la premiere place du groupe A3. Turin : Zverev bat Jodar 6-4, 6-4 ; Shelton vs Fils ce soir. Finale de Dubai : Hatton gagne a -15 (273) ; McIlroy scelle sa 8e couronne."
    fr_nfl = "NFL a Munich en direct : Lions 21, Patriots 3 a la pause. Maye forfait (cheville) ; TD de St. Brown et Gibbs. Multiplex ce soir a 19h00 CET."
    fr_tnf = "NFL Semaine 10 : Lions 21-3 Patriots a Munich. Jeudi : Commanders 24-21 Giants. Dimanche lance."

    fr_block = re.sub(r'todayDesk:\s*"[^"]*"', f'todayDesk: "{fr_today}"', fr_block, count=1)
    fr_block = re.sub(r'todayNfl:\s*"[^"]*"', f'todayNfl: "{fr_nfl}"', fr_block, count=1)
    fr_block = re.sub(r'todayTnf:\s*"[^"]*"', f'todayTnf: "{fr_tnf}"', fr_block, count=1)
    fr_block = re.sub(r'tonightBlurb:\s*"[^"]*"', f'tonightBlurb: "{fr_tonight}"', fr_block, count=1)

    fr_block = re.sub(r'(football:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"NFL a Munich en direct : les Lions menent 21-3 ; Drake Maye blesse a la cheville."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(football:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"EN DIRECT Munich : Lions 21, Patriots 3 (St. Brown 56 yds TD, Gibbs TD). Maye blesse. 2e mi-temps."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(football:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"NFL A MUNICH EN DIRECT : LES LIONS MENENT 21-3 ; DRAKE MAYE FORFAIT SUR BLESSURE"', fr_block, count=1, flags=re.DOTALL)

    fr_block = re.sub(r'(soccer:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"L\'Espagne recoit l\'Angleterre ce soir a Madrid (19h45 GMT) ; le Danemark surclasse le Portugal 4-1."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(soccer:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Ce soir : Espagne vs Angleterre 19h45 GMT Metropolitano. Samedi : Danemark 4-1 Portugal ; Suede 3-2 Bosnie."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(soccer:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"ESPAGNE VS ANGLETERRE CE SOIR A MADRID ; LE DANEMARK SURCLASSE LE PORTUGAL 4-1"', fr_block, count=1, flags=re.DOTALL)

    fr_block = re.sub(r'(basketball:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Giannis (34) porte le Heat 137-117 contre les Pistons ; Proctor triple-double avec les Cavs."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(basketball:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Samedi : Heat 137-117 Pistons (Giannis 34, Klay 26, Cade 33) ; Cavs 127-117 Mavs (Proctor 24/11/10)."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(basketball:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"NBA SAMEDI : HEAT 137-117 PISTONS, GIANNIS 34 ; PROCTOR SIGNE UN TRIPLE-DOUBLE AVEC LES CAVS"', fr_block, count=1, flags=re.DOTALL)

    fr_block = re.sub(r'(golf:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Finale de Dubai terminee : Tyrrell Hatton gagne de 5 coups a -15 ; Rory McIlroy scelle sa 8e Race to Dubai."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(golf:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Dubai Final : 1. Tyrrell Hatton -15 (273, 66) ; 2. Rory McIlroy -10 (278, 67, champion) ; T3. Chacarra -9. Termine."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(golf:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"FINALE DE DUBAI : HATTON GAGNE A -15 (273) ; MCILROY S\'OFFRE SA 8E COURONNE EUROPEENNE"', fr_block, count=1, flags=re.DOTALL)

    fr_block = re.sub(r'(tennis:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Masters de Turin : Zverev domine Jodar 6-4, 6-4 ; Fritz titraire a Stockholm."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(tennis:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Turin dim : Zverev bat Jodar 6-4, 6-4 ; Shelton vs Fils ce soir (20h30). Stockholm sam : Fritz bat Tirante 6-2, 4-6, 7-6 (3)."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(tennis:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"MASTERS DE TURIN : ZVEREV BAT JODAR 6-4, 6-4 ; FRITZ SACRE A STOCKHOLM AU TIEBREAK"', fr_block, count=1, flags=re.DOTALL)

    fr_block = re.sub(r'(f1:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"J-4 avant Las Vegas : 33 points separent Verstappen a Norris. Pas de course Strip pour l\'instant."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(f1:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Classement P2 inchange : Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390). Manche 21 : 19-21 nov."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(f1:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"J-4 AVANT VEGAS : VERSTAPPEN A NORRIS TOUJOURS EN 33 POINTS DERRIERE LE CHAMPION ANTONELLI"', fr_block, count=1, flags=re.DOTALL)

    open(path_main, "w", encoding="utf-8", newline="\n").write(en_block + fr_block)
    print("Updated messages.ts.")

    # Other locales
    locales_data = {
        "es": {
            "path": "frontend/src/i18n/messages-es.ts",
            "today": "Domingo: Lions dominan 21-3 a Patriots en Munich. Espana vs Inglaterra a las 19:45 GMT en Madrid. Final Dubai: Hatton -15 (273), 8vo titulo para McIlroy.",
            "tonight": "Lions ganan 21-3 en Munich ante Patriots con Maye lesionado. Espana recibe a Inglaterra esta noche por el grupo A3. Turin: Zverev supera 6-4, 6-4 a Jodar; Shelton vs Fils esta noche. Dubai: Hatton gana con 66 a -15 (273); McIlroy amarra su octava corona.",
            "nfl": "NFL Munich en vivo: Lions 21, Patriots 3 al descanso. Maye fuera por tobillo; TD de St. Brown y Gibbs. Domingo NFL en marcha.",
            "tnf": "NFL Semana 10: Lions 21-3 Patriots en Munich. Jueves: Commanders 24-21 Giants. Jornada dominical iniciada.",
            "football_tag": "NFL Munich en vivo: Lions dominan 21-3 al descanso; Drake Maye lesionado del tobillo.",
            "football_live": "EN VIVO Munich: Lions 21, Patriots 3 (St. Brown 56 yds TD, Gibbs TD). Maye lesionado. 2do tiempo en juego.",
            "football_pulse": "NFL MUNICH EN VIVO: LIONS SUPERAN 21-3 A PATRIOTS AL DESCANSO; MAYE FUERA POR TOBILLO",
            "soccer_tag": "Espana recibe a Inglaterra esta noche en Madrid (19:45 GMT) por el grupo A3; Dinamarca golea 4-1 a Portugal.",
            "soccer_live": "Esta noche: Espana vs Inglaterra 19:45 GMT Metropolitano. Sab: Dinamarca 4-1 Portugal; Suecia 3-2 Bosnia. Premier: Arsenal 27.",
            "soccer_pulse": "ESPANA VS INGLATERRA ESTA NOCHE EN MADRID; DINAMARCA GOLEA 4-1 A PORTUGAL EN NATIONS LEAGUE",
            "basketball_tag": "Giannis (34) guia a Heat 137-117 sobre Pistons; Proctor triple-doble lidera victoria de Cavs 127-117.",
            "basketball_live": "Sab: Heat 137-117 Pistons (Giannis 34, Klay 26, Cade 33); Cavs 127-117 Mavs (Proctor 24/11/10). Vie: Spurs 123-85 Warriors.",
            "basketball_pulse": "NBA SABADO: HEAT 137-117 PISTONS, GIANNIS 34; TRIPLE-DOBLE DE PROCTOR GUIA A CAVS SOBRE MAVS",
            "golf_tag": "Final de Dubai completa: Tyrrell Hatton firma 66 para ganar por 5 con -15; Rory McIlroy sella su 8va Race to Dubai.",
            "golf_live": "Final Dubai: 1. Tyrrell Hatton -15 (273, 66); 2. Rory McIlroy -10 (278, 67, campeon); T3. Chacarra -9. Final.",
            "golf_pulse": "FINAL DE DUBAI: HATTON GANA CON 273 (-15); MCILROY (278, -10) SELLA SU OCTAVA CORONA DE LA TEMPORADA",
            "tennis_tag": "Finales ATP Turin: Zverev vence 6-4, 6-4 a Jodar; Fritz supera a Tirante en final de Estocolmo.",
            "tennis_live": "Turin dom: Zverev vence a Jodar 6-4, 6-4; Shelton vs Fils esta noche (20:30 CET). Estocolmo sab: Fritz gana a Tirante 6-2, 4-6, 7-6 (3).",
            "tennis_pulse": "FINALES ATP TURIN: ZVEREV VENCE 6-4, 6-4 A JODAR; FRITZ CAMPEON EN ESTOCOLMO EN EL TIEBREAK",
            "f1_tag": "Cuatro dias para Ronda 21 Las Vegas: 33 puntos separan a Verstappen de Norris. Sin carrera todavia.",
            "f1_live": "Lucha P2 inalterada: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). R21: 19-21 nov.",
            "f1_pulse": "CUATRO DIAS PARA VEGAS: VERSTAPPEN A NORRIS EN 33 PUNTOS DETRAS DEL CAMPEON ANTONELLI",
        },
        "de": {
            "path": "frontend/src/i18n/messages-de.ts",
            "today": "Sonntag: Lions fuehren 21:3 in Muenchen gegen Patriots. Spanien vs. England 19:45 GMT in Madrid. Dubai-Finale: Hatton -15 (273), McIlroy holt 8. Titel.",
            "tonight": "Lions fuehren in Muenchen mit 21:3 gegen Patriots (Maye verletzt). Spanien empfaengt England heute Abend in Madrid um Gruppe A3. Turin ATP Finals: Zverev siegt 6:4, 6:4 gegen Jodar; Shelton vs. Fils heute. Dubai: Hatton siegt mit 66 bei -15 (273); McIlroy feiert 8. Saisonsieg.",
            "nfl": "NFL Munich Game live: Lions 21, Patriots 3 zur Pause. Drake Maye knoechelverletzt raus; TDs durch St. Brown und Gibbs.",
            "tnf": "NFL Woche 10: Lions 21:3 Patriots in Muenchen. Donnerstag: Commanders 24:21 Giants. Sonntagsspiele laufen.",
            "football_tag": "NFL Munich live: Lions fuehren 21:3 zur Pause; Drake Maye verletzt am Knoechel raus.",
            "football_live": "LIVE Muenchen: Lions 21, Patriots 3 (St. Brown 56-yd TD, Gibbs TD). Maye verletzt. 2. Halbzeit laeuft.",
            "football_pulse": "NFL MUNICH LIVE: LIONS FUEHREN 21:3 GEGEN PATRIOTS ZUR HALBZEIT; MAYE VERLETZT RAUS",
            "soccer_tag": "Spanien empfaengt England heute Abend in Madrid (19:45 GMT); Daenemark demuetigt Portugal 4:1.",
            "soccer_live": "Heute: Spanien vs. England 19:45 GMT Metropolitano. Sa: Daenemark 4:1 Portugal; Schweden 3:2 Bosnien. PL: Arsenal 27.",
            "soccer_pulse": "SPANIEN VS ENGLAND HEUTE IN MADRID; DAENEMARK UEBERRASCHT PORTUGAL 4:1 IN NATIONS LEAGUE",
            "basketball_tag": "Giannis (34) fuehrt Heat zum 137:117 ueber Pistons; Proctor mit Triple-Double fuer dezimierte Cavs.",
            "basketball_live": "Sa: Heat 137:117 Pistons (Giannis 34, Klay 26, Cade 33); Cavs 127:117 Mavs (Proctor 24/11/10). Fr: Spurs 123:85 Warriors.",
            "basketball_pulse": "NBA SAMSTAG: HEAT 137:117 PISTONS, GIANNIS 34; PROCTOR TRIPLE-DOUBLE BEFLUEGELT CAVS GEGEN MAVS",
            "golf_tag": "Dubai-Finale komplett: Tyrrell Hatton spielt 66 und siegt mit 5 vor; Rory McIlroy holt 8. Race to Dubai-Titel.",
            "golf_live": "Dubai Finale: 1. Tyrrell Hatton -15 (273, 66); 2. Rory McIlroy -10 (278, 67, Champion); T3. Chacarra -9. Beendet.",
            "golf_pulse": "DUBAI-FINALE: HATTON SIEGT MIT 273 (-15); MCILROY (278, -10) SICHERT SICH ACHTEN SAISONTITEL",
            "tennis_tag": "Turin ATP Finals: Zverev besiegt Jodar 6:4, 6:4; Fritz bezwingt Tirante im Stockholm-Finale.",
            "tennis_live": "Turin So: Zverev d Jodar 6:4, 6:4; Shelton vs. Fils heute Abend (20:30 CET). Stockholm Sa: Fritz schlaegt Tirante 6:2, 4:6, 7:6 (3).",
            "tennis_pulse": "TURIN ATP FINALS ERÖFFNET: ZVEREV SIEGT 6:4, 6:4 GEGEN JODAR; FRITZ SIEGT IM TIEBREAK IN STOCKHOLM",
            "f1_tag": "Vier Tage bis Runde 21 Las Vegas: 33 Punkte trennen Verstappen von Norris. Noch kein Rennen.",
            "f1_live": "P2-Kampf unveraendert: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). R21: 19.-21. Nov.",
            "f1_pulse": "VIER TAGE BIS VEGAS: VERSTAPPEN BIS NORRIS NOCH 33 PKT HINTER CHAMPION ANTONELLI",
        },
        "it": {
            "path": "frontend/src/i18n/messages-it.ts",
            "today": "Domenica: Lions avanti 21-3 a Monaco sui Patriots. Spagna-Inghilterra alle 19:45 GMT a Madrid. Finale Dubai: Hatton -15 (273), McIlroy ottavo titolo.",
            "tonight": "I Lions conducono 21-3 sui Patriots a Monaco con Maye infortunato. La Spagna ospita l'Inghilterra stasera a Madrid per il girone A3. Finals Torino: Zverev supera 6-4, 6-4 Jodar; stasera Shelton vs Fils. Dubai: Hatton vince con 66 a -15 (273); McIlroy conquista l'ottava Race to Dubai.",
            "nfl": "NFL Munich live: Lions 21, Patriots 3 all'intervallo. Maye infortunato alla caviglia; TD per St. Brown e Gibbs. Programma domenicale iniziato.",
            "tnf": "NFL Week 10: Lions 21-3 sui Patriots a Monaco. Giovedi: Commanders 24-21 Giants. Domenica in corso.",
            "football_tag": "NFL Monaco live: Lions avanti 21-3 all'intervallo; Drake Maye fuori per infortunio alla caviglia.",
            "football_live": "DIRETTA Monaco: Lions 21, Patriots 3 (St. Brown 56 yds TD, Gibbs TD). Maye ko. Secondo tempo in corso.",
            "football_pulse": "NFL MONACO LIVE: LIONS AVANTI 21-3 SUI PATRIOTS A META GARA; MAYE OUT PER CAVIGLIA",
            "soccer_tag": "Spagna contro Inghilterra stasera a Madrid (19:45 GMT) per il gruppo A3; Danimarca travolge Portogallo 4-1.",
            "soccer_live": "Stasera: Spagna vs Inghilterra 19:45 GMT Metropolitano. Sab: Danimarca 4-1 Portogallo; Svezia 3-2 Bosnia. PL: Arsenal 27.",
            "soccer_pulse": "SPAGNA VS INGHILTERRA STASERA A MADRID; DANIMARCA SUPERA IL PORTOGALLO 4-1 IN NATIONS LEAGUE",
            "basketball_tag": "Giannis (34) guida Miami 137-117 sui Pistons; Proctor tripla doppia da urlo per i rimaneggiati Cavs.",
            "basketball_live": "Sab: Heat 137-117 Pistons (Giannis 34, Klay 26, Cade 33); Cavs 127-117 Mavs (Proctor 24/11/10). Ven: Spurs 123-85 Warriors.",
            "basketball_pulse": "NBA SABATO: HEAT 137-117 PISTONS, GIANNIS 34; TRIPLA DOPPIA DI PROCTOR TRASCINA I CAVS",
            "golf_tag": "Finale di Dubai completata: Tyrrell Hatton vince con 66 a -15; Rory McIlroy sigilla l'ottava Race to Dubai.",
            "golf_live": "Finale Dubai: 1. Tyrrell Hatton -15 (273, 66); 2. Rory McIlroy -10 (278, 67, campione); T3. Chacarra -9. Finale.",
            "golf_pulse": "FINALE DUBAI: HATTON VINCE A 273 (-15); MCILROY (278, -10) SIGILLA L'OTTAVA CORONA STAGIONALE",
            "tennis_tag": "Torino ATP Finals: Zverev batte Jodar 6-4, 6-4; Fritz supera Tirante nella finale di Stoccolma.",
            "tennis_live": "Torino dom: Zverev batte Jodar 6-4, 6-4; Shelton vs Fils stasera (20:30 CET). Stoccolma sab: Fritz piega Tirante 6-2, 4-6, 7-6 (3).",
            "tennis_pulse": "ATP FINALS TORINO: ZVEREV PIEGA JODAR 6-4, 6-4; FRITZ TRIONFA A STOCCOLMA AL TIEBREAK",
            "f1_tag": "Quattro giorni a Round 21 Las Vegas: 33 punti dividono Verstappen e Norris. Gara non ancora corsa.",
            "f1_live": "Lotta P2 invariata: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). R21: 19-21 nov.",
            "f1_pulse": "QUATTRO GIORNI A VEGAS: DA VERSTAPPEN A NORRIS ANCORA 33 PUNTI DIETRO AL CAMPIONE ANTONELLI",
        },
        "pl": {
            "path": "frontend/src/i18n/messages-pl.ts",
            "today": "Niedziela: Lions prowadza 21:3 w Monachium z Patriots. Hiszpania vs Anglia o 19:45 GMT w Madrycie. Final w Dubaju: Hatton -15 (273), McIlroy z 8. tytulem.",
            "tonight": "Lions prowadza 21:3 z Patriots w Monachium (Maye kontuzjowany). Hiszpania podejmuje Anglie dzis w Madrycie o wygrana w grupie A3. Turyn ATP Finals: Zverev wygrywa 6:4, 6:4 z Jodarem; wieczorem Shelton vs Fils. Dubaj: Hatton wygrywa runda 66 na -15 (273); McIlroy zdobywa osmy puchar.",
            "nfl": "NFL mecz w Monachium na zywo: Lions 21, Patriots 3 do przerwy. Drake Maye zszedl z kontuzja kostki; TD St. Browna i Gibbsa.",
            "tnf": "NFL 10. tydzien: Lions 21:3 Patriots w Monachium. Czwartek: Commanders 24:21 Giants. Niedzielne mecze trwaja.",
            "football_tag": "NFL Monachium na zywo: Lions prowadza 21:3 do przerwy; Drake Maye opuscil mecz z kontuzja kostki.",
            "football_live": "NA ZYWO Monachium: Lions 21, Patriots 3 (St. Brown 56 yd TD, Gibbs TD). Maye z kontuzja. Trwa 2. polowa.",
            "football_pulse": "NFL MECZ W MONACHIUM: LIONS PROWADZA 21:3 Z PATRIOTS DO PRZERWY; DRAKE MAYE KONTUZJOWANY",
            "soccer_tag": "Hiszpania podejmuje Anglie dzis w Madrycie (19:45 GMT) o grupe A3; Dania gromi Portugalie 4:1.",
            "soccer_live": "Dzis: Hiszpania vs Anglia 19:45 GMT Metropolitano. Sob: Dania 4:1 Portugalia; Szwecja 3:2 Bosnia. PL: Arsenal 27.",
            "soccer_pulse": "HISZPANIA VS ANGLIA DZIS W MADRYCIE; DANIA SZOKUJE PORTUGALIE 4:1 W LIDZE NARODOW",
            "basketball_tag": "Giannis (34) prowadzi Heat do 137:117 nad Pistons; Proctor z triple-double dla rezerwowych Cavs.",
            "basketball_live": "Sob: Heat 137:117 Pistons (Giannis 34, Klay 26, Cade 33); Cavs 127:117 Mavs (Proctor 24/11/10). Pt: Spurs 123:85 Warriors.",
            "basketball_pulse": "NBA SOBOTA: HEAT 137:117 PISTONS, GIANNIS 34; TRIPLE-DOUBLE PROCTORA PROWADZI CAVS",
            "golf_tag": "Final w Dubaju zakonczony: Tyrrell Hatton wygrywa runda 66 na -15; Rory McIlroy pieczetuje 8. Race to Dubai.",
            "golf_live": "Dubaj Final: 1. Tyrrell Hatton -15 (273, 66); 2. Rory McIlroy -10 (278, 67, mistrz); T3. Chacarra -9. Zakonczony.",
            "golf_pulse": "FINAL W DUBAJU: HATTON WYGRYWA Z 273 (-15); MCILROY (278, -10) PIECZETUJE OSMY TYTUL SEZONU",
            "tennis_tag": "Turyn ATP Finals: Zverev pokonuje Jodara 6:4, 6:4; Fritz pokonuje Tirante w finale w Sztokholmie.",
            "tennis_live": "Turyn nd: Zverev bije Jodara 6:4, 6:4; Shelton vs Fils dzis (20:30 CET). Sztokholm sob: Fritz bije Tirante 6:2, 4:6, 7:6 (3).",
            "tennis_pulse": "TURYN ATP FINALS: ZVEREV POKONUJE JODARA 6:4, 6:4; FRITZ WYGRYWA W SZTOKHOLMIE PO TIEBREAKU",
            "f1_tag": "Cztery dni do 21. rundy Las Vegas: 33 punkty dziela Verstappena od Norrisa. Wyscig sie nie odbyl.",
            "f1_live": "Walka o P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). R21: 19-21 lis.",
            "f1_pulse": "CZTERY DNI DO VEGAS: OD VERSTAPPENA DO NORRISA CIAGLE 33 PKT ZA MISTRZEM ANTONELLIM",
        },
        "zh": {
            "path": "frontend/src/i18n/messages-zh.ts",
            "today": "周日要闻：慕尼黑赛雄狮半场21-3领先爱国者。马德里西班牙对英格兰19:45打响。迪拜总决赛：哈顿-15夺冠，麦克罗伊八度加冕。",
            "tonight": "雄狮在慕尼黑半场21-3领先爱国者（梅耶伤退）。西班牙今晚坐镇马德里迎战英格兰决战A3组头名。都灵总决赛：兹维列夫6-4、6-4轻取霍达尔；今晚谢尔顿对菲斯。迪拜总决赛：哈顿66杆总成绩-15（273）夺冠；麦克罗伊险胜查卡拉第八度加冕总冠军。",
            "nfl": "NFL慕尼黑赛直播：雄狮半场21-3领先爱国者。梅耶脚踝受伤退赛；圣布朗56码达阵，吉布斯冲球达阵。下半场进行中。",
            "tnf": "NFL第10周：雄狮21-3领先爱国者。周四夜赛：指挥官24-21胜巨人。周日早场赛事陆续展开。",
            "football_tag": "NFL慕尼黑赛直播：雄狮半场21-3领先爱国者；德雷克·梅耶脚踝受伤退场。",
            "football_live": "直播 慕尼黑：雄狮21，爱国者3（圣布朗56码TD，吉布斯TD）。梅耶伤退。下半场进行中。",
            "football_pulse": "NFL慕尼黑赛直播：雄狮半场21-3领先爱国者；新秀四分卫梅耶伤退",
            "soccer_tag": "西班牙今晚坐镇马德里（19:45）决战英格兰；丹麦客场4-1重创葡萄牙。",
            "soccer_live": "今晚：西班牙对英格兰 19:45 GMT 大都会球场。周六：丹麦4-1葡萄牙；瑞典3-2波黑。英超：阿森纳27分。",
            "soccer_pulse": "西班牙对英格兰今晚在马德里决战；丹麦欧国联客场4-1痛击葡萄牙",
            "basketball_tag": "字母哥34分率热火137-117大胜活塞；新秀普罗克特三双率残阵骑士掀翻独行侠。",
            "basketball_live": "周六：热火137-117活塞（字母哥34分，克莱26分，康宁汉姆33分）；骑士127-117独行侠（普罗克特24/11/10）。周五：马刺123-85勇士。",
            "basketball_pulse": "NBA周六战报：热火137-117轻取活塞，字母哥34分；普罗克特首度三双率残阵骑士击退独行侠",
            "golf_tag": "迪拜总决赛收官：哈顿末轮轰出66杆以-15夺冠；麦克罗伊锁定第八座迪拜竞赛总冠军。",
            "golf_live": "迪拜决赛：1. 哈顿 -15（273，66）；2. 麦克罗伊 -10（278，67，赛季总冠军）；并列第3. 查卡拉 -9。完场。",
            "golf_pulse": "迪拜总决赛：哈顿273杆（-15）夺冠；麦克罗伊（278，-10）锁定第八座赛季总冠军奖杯",
            "tennis_tag": "都灵年终总决赛：兹维列夫6-4、6-4轻取霍达尔；弗里茨险胜蒂兰特斯德哥尔摩称雄。",
            "tennis_live": "都灵周日：兹维列夫6-4、6-4胜霍达尔；今晚谢尔顿对菲斯（20:30 CET）。斯德哥尔摩周六决赛：弗里茨6-2、4-6、7-6（3）胜蒂兰特。",
            "tennis_pulse": "ATP年终总决赛都灵揭幕：兹维列夫两盘轻取霍达尔；弗里茨决胜盘抢七斩获斯德哥尔摩冠军",
            "f1_tag": "距第21站拉斯维加斯站还有四天：维斯塔潘与诺里斯等五将相差33分。正赛尚未开始。",
            "f1_live": "车手榜榜眼之争依旧：维斯塔潘279，拉塞尔262，汉密尔顿261，勒克莱尔249，诺里斯246（安东内利390；梅赛德斯652）。第21站：11月19-21日。",
            "f1_pulse": "距赌城大奖赛还有四天：五位车手相差33分争夺年度亚军，安东内利与梅奔已提前夺冠",
        },
        "ja": {
            "path": "frontend/src/i18n/messages-ja.ts",
            "today": "日曜デスク：ミュンヘンでライオンズがペイトリオッツに21-3リード。マドリードでスペイン対イングランド19:45。ドバイ最終戦：ハットン-15優勝、マキロイ8度目王者。",
            "tonight": "ライオンズがミュンヘンでペイトリオッツに21-3リード（メイ負傷）。スペインが今夜マドリードでイングランドと首位決戦。トリノ：ズベレフがジョダルに6-4、6-4完勝；今夜シェルトン対フィス。ドバイ：ハットンが66で通算-15（273）優勝；マキロイが8度目の年間王座獲得。",
            "nfl": "NFLミュンヘン速報：ライオンズ前半21-3リード。ドレイク・メイが足首負傷退場；セントブラウン56ヤードTD、ギブスTD。後半進行中。",
            "tnf": "NFL第10週：ライオンズがミュンヘンで21-3リード。木曜：コマンダース24-21ジャイアンツ。日曜ゲーム開幕。",
            "football_tag": "NFLミュンヘン生中継：ライオンズが21-3リード；ドレイク・メイが足首負傷退場。",
            "football_live": "速報 ミュンヘン：ライオンズ21、ペイトリオッツ3（セントブラウン56yd TD、ギブスTD）。メイ負傷。後半進行中。",
            "football_pulse": "NFLミュンヘン速報：ライオンズがペイトリオッツに前半21-3リード；メイ負傷退場",
            "soccer_tag": "スペインが今夜マドリード（19:45 GMT）でイングランドと決戦；デンマークがポルトガルを4-1粉砕。",
            "soccer_live": "今夜：スペイン対イングランド 19:45 GMT メトロポリターノ。土曜：デンマーク4-1ポルトガル；スウェーデン3-2ボスニア。プレミア首位アーセナル27点。",
            "soccer_pulse": "スペイン対イングランド今夜マドリードで激突；デンマークがポルトガルを4-1撃破",
            "basketball_tag": "ヤニス34点でヒートがピストンズに137-117快勝；プロクターの初トリプルダブルでキャブズ勝利。",
            "basketball_live": "土曜：ヒート137-117ピストンズ（ヤニス34、クレイ26、カニンガム33）；キャブズ127-117マブス（プロクター24/11/10）。金曜：スパーズ123-85ウォリアーズ。",
            "basketball_pulse": "NBA土曜：ヒート137-117ピストンズ、ヤニス34点；プロクターがトリプルダブルでキャブズを牽引",
            "golf_tag": "ドバイ最終戦終了：ティレル・ハットンが66で通算-15とし5打差圧勝；ローリー・マキロイが8度目の年間王者戴冠。",
            "golf_live": "ドバイ決勝：1. ハットン -15（273、66）；2. マキロイ -10（278、67、年間王者）；3位タイ チャカラ -9。終了。",
            "golf_pulse": "ドバイ最終戦：ハットンが273（-15）で優勝；マキロイ（278、-10）が8度目の年間タイトル獲得",
            "tennis_tag": "トリノATPファイナルズ：ズベレフがジョダルを6-4、6-4で退ける；フリッツがストックホルム制覇。",
            "tennis_live": "トリノ日曜：ズベレフがジョダルを6-4、6-4で破る；今夜シェルトン対フィス（20:30 CET）。ストックホルム土曜決勝：フリッツがティランテを6-2、4-6、7-6（3）で下す。",
            "tennis_pulse": "ATPファイナルズ開幕：ズベレフがジョダルにストレート勝ち；フリッツが激闘制しストックホルム制覇",
            "f1_tag": "ラスベガスGPまであと4日：フェルスタッペンからノリスまで33点差の争い。決勝レースは未開催。",
            "f1_live": "2位争い激化：フェルスタッペン279、ラッセル262、ハミルトン261、ルクレール249、ノリス246（アントネッリ390；メルセデス652）。第21戦：11月19-21日。",
            "f1_pulse": "ラスベガスまであと4日：フェルスタッペンからノリスまで33点差で王者アントネッリを追う",
        },
        "ko": {
            "path": "frontend/src/i18n/messages-ko.ts",
            "today": "일요일 데스크: 뮌헨서 라이언스 패트리어츠에 21-3 리드. 마드리드 스페인 vs 잉글랜드 19:45. 두바이 최종전: 해튼 -15 우승, 매킬로이 8번째 왕좌.",
            "tonight": "라이언스가 뮌헨에서 패트리어츠에 21-3 리드(메이 부상). 스페인이 오늘 밤 마드리드에서 잉글랜드와 A3조 1위 결정전. 토리노: 즈베레프 호다르에 6-4, 6-4 완승; 오늘 밤 셸턴 vs 피스. 두바이: 해튼 66타로 -15(273) 우승; 매킬로이 8번째 시즌 제패.",
            "nfl": "NFL 뮌헨 경기 생중계: 라이언스 전반 21-3 리드. 드레이크 메이 발목 부상 이탈; 세인트브라운 56야드 TD, 깁스 TD. 후반 진행 중.",
            "tnf": "NFL 10주차: 라이언스 뮌헨서 21-3 리드. 목요일: 커맨더스 24-21 자이언츠. 일요일 정규 경기 개막.",
            "football_tag": "NFL 뮌헨 경기 생중계: 라이언스 전반 21-3 리드; 드레이크 메이 발목 부상 교체.",
            "football_live": "생중계 뮌헨: 라이언스 21, 패트리어츠 3(세인트브라운 56yd TD, 깁스 TD). 메이 부상. 후반 진행 중.",
            "football_pulse": "NFL 뮌헨 생중계: 라이언스 패트리어츠에 전반 21-3 리드; 쿼터백 메이 부상 이탈",
            "soccer_tag": "스페인 오늘 밤 마드리드(19:45 GMT)서 잉글랜드와 맞대결; 덴마크 포르투갈 4-1 완파.",
            "soccer_live": "오늘 밤: 스페인 vs 잉글랜드 19:45 GMT 메트로폴리타노. 토: 덴마크 4-1 포르투갈; 스웨덴 3-2 보스니아. PL 아스널 27점.",
            "soccer_pulse": "스페인 vs 잉글랜드 오늘 밤 마드리드 격돌; 덴마크 네이션스리그서 포르투갈 4-1 대파",
            "basketball_tag": "야니스 34점 히트 137-117 피스톤스 완파; 프록터 트리플더블로 주전 빠진 캐브스 승리.",
            "basketball_live": "토: 히트 137-117 피스톤스(야니스 34, 톰슨 26, 커닝햄 33); 캐브스 127-117 매브스(프록터 24/11/10). 금: 스퍼스 123-85 워리어스.",
            "basketball_pulse": "NBA 토요 경기: 히트 137-117 피스톤스, 야니스 34점; 프록터 생애 첫 트리플더블로 캐브스 승리 견인",
            "golf_tag": "두바이 최종전 종료: 타렐 해튼 66타로 -15(273) 5타 차 우승; 로리 매킬로이 8번째 레이스 투 두바이 달성.",
            "golf_live": "두바이 최종전: 1. 해튼 -15(273, 66); 2. 매킬로이 -10(278, 67, 시즌 챔피언); 공동 3위 차카라 -9. 종료.",
            "golf_pulse": "두바이 최종전: 해튼 273타(-15) 우승; 매킬로이(278, -10) 통산 8번째 시즌 챔피언 트로피 획득",
            "tennis_tag": "토리노 ATP 파이널스: 즈베레프 호다르에 6-4, 6-4 완승; 프리츠 스톡홀름 결승 제패.",
            "tennis_live": "토리노 일: 즈베레프 호다르에 6-4, 6-4 승; 오늘 밤 셸턴 vs 피스(20:30 CET). 스톡홀름 토: 프리츠 티란테에 6-2, 4-6, 7-6(3) 승.",
            "tennis_pulse": "ATP 파이널스 개막: 즈베레프 호다르에 완승; 프리츠 타이브레이크 끝에 스톡홀름 정복",
            "f1_tag": "라스베이거스 GP D-4: 베르스타펜부터 노리스까지 33점 차 2위 쟁탈전. 레이스 아직 미개최.",
            "f1_live": "준우승 경쟁: 베르스타펜 279, 러셀 262, 해밀턴 261, 르클레르 249, 노리스 246(안토넬리 390; 메르세데스 652). 21R: 11월 19-21일.",
            "f1_pulse": "라스베이거스 D-4: 베르스타펜부터 노리스까지 33점 차 대접전, 안토넬리 조기 챔피언",
        },
        "ar": {
            "path": "frontend/src/i18n/messages-ar.ts",
            "today": "نشرة الأحد: لايونز يتقدمون 21-3 في ميونخ على باتريوتس. إسبانيا ضد إنجلترا 19:45 غرينتش في مدريد. ختام دبي: هاتون -15 (273)، ومكلروي لقبه الثامن.",
            "tonight": "لايونز يتقدمون 21-3 في ميونخ على باتريوتس مع إصابة ماي. إسبانيا تستضيف إنجلترا الليلة في مدريد لتحديد متصدر المجموعة A3. نهائيات تورينو: زفيريف يتجاوز خودار 6-4 و6-4؛ شيلتون ضد فيلس الليلة. دبي: هاتون يفوز بـ66 (-15، 273)؛ ومكلروي يحسم لقبه الثامن بالسباق إلى دبي.",
            "nfl": "مباراة ميونخ مباشرة: لايونز 21، باتريوتس 3 في الشوط الأول. خروج ماي لإصابة الكاحل؛ هدف لسانت براون وغيبس. الشوط الثاني جارٍ.",
            "tnf": "NFL الأسبوع 10: لايونز 21-3 باتريوتس في ميونخ. الخميس: كوماندرز 24-21 جاينتس. مباريات الأحد انطلقت.",
            "football_tag": "مباراة ميونخ مباشرة: لايونز يتقدمون 21-3 في الشوط الأول؛ خروج دريك ماي مصاباً في الكاحل.",
            "football_live": "مباشر ميونخ: لايونز 21، باتريوتس 3 (سانت براون 56 ياردة، غيبس TD). إصابة ماي. الشوط الثاني مستمر.",
            "football_pulse": "NFL ميونخ مباشر: لايونز يتقدمون 21-3 على باتريوتس؛ وخروج الظهير دريك ماي مصاباً",
            "soccer_tag": "إسبانيا تستضيف إنجلترا الليلة في مدريد (19:45 غرينتش) لحسم المجموعة A3؛ والدنمارك تكتسح البرتغال 4-1.",
            "soccer_live": "الليلة: إسبانيا ضد إنجلترا 19:45 غرينتش ميتروبوليتانو. السبت: الدنمارك 4-1 البرتغال؛ السويد 3-2 البوسنة. أرسنال 27.",
            "soccer_pulse": "إسبانيا ضد إنجلترا الليلة في مدريد؛ والدنمارك تسحق البرتغال 4-1 في دوري الأمم",
            "basketball_tag": "يانيس (34) يقود هيت للفوز 137-117 على بيستونز؛ وبروكتور يحقق ثلاثية مزدوجة مع كافالييرز.",
            "basketball_live": "السبت: هيت 137-117 بيستونز (يانيس 34، طومسون 26، كانينغهام 33)؛ كافالييرز 127-117 مافريكس (بروكتور 24/11/10). الجمعة: سبرز 123-85 ووريورز.",
            "basketball_pulse": "NBA السبت: هيت 137-117 بيستونز، يانيس 34؛ ثلاثية بروكتور تقود كافالييرز البديل للفوز على مافريكس",
            "golf_tag": "ختام دبي مكتمل: تيريل هاتون يسجل 66 ليفوز بفارق 5 عند -15؛ روري مكلروي يحسم لقبه الثامن في السباق إلى دبي.",
            "golf_live": "نهائي دبي: 1. تيريل هاتون -15 (273، 66)؛ 2. روري مكلروي -10 (278، 67، بطل الموسم)؛ الثالث مكرر تشاكارا -9. انتهت.",
            "golf_pulse": "ختام دبي: هاتون يفوز بـ273 (-15)؛ ومكلروي (278، -10) يحسم تاجه الأوروبي الثامن في الموسم",
            "tennis_tag": "نهائيات تورينو ATP: زفيريف يتغلب 6-4 و6-4 على خودار؛ وفريتز يحسم لقب ستوكهولم أمام تيرانتي.",
            "tennis_live": "تورينو الأحد: زفيريف يهزم خودار 6-4 و6-4؛ شيلتون ضد فيلس الليلة (20:30 CET). ستوكهولم السبت: فريتز يهزم تيرانتي 6-2 و4-6 و7-6 (3).",
            "tennis_pulse": "افتتاح نهائيات تورينو ATP: زفيريف يهزم خودار بمجموعتين؛ وفريتز يظفر بلقب ستوكهولم بكسر التعادل",
            "f1_tag": "أربعة أيام على جولة لاس فيغاس 21: 33 نقطة تفصل فيرستابن عن نوريس. لم يجر السباق بعد.",
            "f1_live": "صراع الوصافة: فيرستابن 279، راسل 262، هاميلتون 261، لوكلير 249، نوريس 246 (أنتونيللي 390؛ مرسيدس 652). الجولة 21: 19-21 نوفمبر.",
            "f1_pulse": "أربعة أيام على فيغاس: فيرستابن ونوريس في صراع 33 نقطة خلف البطل أنتونيللي",
        },
    }

    for loc, d in locales_data.items():
        p = d["path"]
        txt = open(p, "r", encoding="utf-8").read()

        txt = re.sub(r'todayDesk:\s*"[^"]*"', f'todayDesk: "{d["today"]}"', txt, count=1)
        txt = re.sub(r'todayNfl:\s*"[^"]*"', f'todayNfl: "{d["nfl"]}"', txt, count=1)
        txt = re.sub(r'todayTnf:\s*"[^"]*"', f'todayTnf: "{d["tnf"]}"', txt, count=1)
        txt = re.sub(r'tonightBlurb:\s*"[^"]*"', f'tonightBlurb: "{d["tonight"]}"', txt, count=1)

        txt = re.sub(r'(football:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{d["football_tag"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(football:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{d["football_live"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(football:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{d["football_pulse"]}"', txt, count=1, flags=re.DOTALL)

        txt = re.sub(r'(soccer:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{d["soccer_tag"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(soccer:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{d["soccer_live"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(soccer:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{d["soccer_pulse"]}"', txt, count=1, flags=re.DOTALL)

        txt = re.sub(r'(basketball:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{d["basketball_tag"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(basketball:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{d["basketball_live"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(basketball:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{d["basketball_pulse"]}"', txt, count=1, flags=re.DOTALL)

        txt = re.sub(r'(golf:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{d["golf_tag"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(golf:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{d["golf_live"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(golf:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{d["golf_pulse"]}"', txt, count=1, flags=re.DOTALL)

        txt = re.sub(r'(tennis:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{d["tennis_tag"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(tennis:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{d["tennis_live"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(tennis:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{d["tennis_pulse"]}"', txt, count=1, flags=re.DOTALL)

        txt = re.sub(r'(f1:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{d["f1_tag"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(f1:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{d["f1_live"]}"', txt, count=1, flags=re.DOTALL)
        txt = re.sub(r'(f1:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{d["f1_pulse"]}"', txt, count=1, flags=re.DOTALL)

        open(p, "w", encoding="utf-8", newline="\n").write(txt)
        print(f"Updated {p}.")

if __name__ == "__main__":
    update_playground()
    update_messages()

