"""
update_nov16_ui_messages.py
Updates playground.ts and all 10 messages*.ts for 16 Nov 2026.
"""
import re
import os

def update_playground():
    path = "frontend/src/i18n/playground.ts"
    content = open(path, "r", encoding="utf-8").read()

    majors_done_map = {
        "en": "Dubai Complete: Tyrrell Hatton -15 (273) wins by 5; Rory McIlroy -10 (278) seals 8th Race to Dubai title. Next: RSM Classic at Sea Island.",
        "fr": "Dubai termine : Tyrrell Hatton -15 (273) gagne de 5 coups ; Rory McIlroy -10 (278) scelle sa 8e Race to Dubai. Prochain : RSM Classic a Sea Island.",
        "es": "Dubai completo: Tyrrell Hatton -15 (273) gana por 5 golpes; Rory McIlroy -10 (278) sella su 8va Race to Dubai. Proximo: RSM Classic en Sea Island.",
        "de": "Dubai Finale komplett: Tyrrell Hatton -15 (273) siegt mit 5 Schlaegen; Rory McIlroy -10 (278) holt 8. Race to Dubai. Weiter geht es mit der RSM Classic.",
        "it": "Dubai completata: Tyrrell Hatton -15 (273) vince con 5 colpi; Rory McIlroy -10 (278) sigilla l'8a Race to Dubai. Prossimo: RSM Classic a Sea Island.",
        "pl": "Dubaj zakonczony: Tyrrell Hatton -15 (273) wygrywa z 5 uderzeniami przewagi; Rory McIlroy -10 (278) z 8. tytulem. Nastepnie: RSM Classic.",
        "zh": "迪拜总决赛收官：哈顿-15（273杆）五杆大胜；麦克罗伊-10（278杆）加冕第八座总冠军。下一站：海岛RSM精英赛。",
        "ja": "ドバイ最終戦終了：ティレル・ハットンが-15（273）で5打差圧勝；ローリー・マキロイが-10（278）で8度目の年間王座。次はRSMクラシック。",
        "ko": "두바이 최종전 종료: 해튼 -15(273타) 5타 차 우승; 매킬로이 -10(278타)로 8번째 레이스 투 두바이 제패. 다음: RSM 클래식.",
        "ar": "ختام دبي مكتمل: تيريل هاتون -15 (273) يفوز بفارق 5 ضربات؛ وروري ماكلروي -10 (278) يحسم لقبه الثامن. التالي: RSM كلاسيك.",
    }

    pin_final_map = {
        "en": "Turin Sun: Shelton d Fils 6-2, 3-6, 6-3; Zverev d Jodar 6-4, 6-4. Mon Lendl: Alcaraz vs Tiafoe (14:00 CET), Medvedev vs Cobolli (20:30 CET).",
        "fr": "Turin dim : Shelton bat Fils 6-2, 3-6, 6-3 ; Zverev bat Jodar 6-4, 6-4. Lun Lendl : Alcaraz vs Tiafoe (14h00), Medvedev vs Cobolli (20h30).",
        "es": "Turin dom: Shelton vence a Fils 6-2, 3-6, 6-3; Zverev vence a Jodar 6-4, 6-4. Lun Lendl: Alcaraz vs Tiafoe (14:00 CET), Medvedev vs Cobolli (20:30 CET).",
        "de": "Turin So: Shelton besiegt Fils 6:2, 3:6, 6:3; Zverev schlaegt Jodar 6:4, 6:4. Mo Lendl: Alcaraz vs. Tiafoe (14:00 MEZ), Medvedev vs. Cobolli (20:30 MEZ).",
        "it": "Torino dom: Shelton batte Fils 6-2, 3-6, 6-3; Zverev batte Jodar 6-4, 6-4. Lun Lendl: Alcaraz vs Tiafoe (14:00), Medvedev vs Cobolli (20:30).",
        "pl": "Turyn niedz: Shelton bije Filsa 6:2, 3:6, 6:3; Zverev bije Jodara 6:4, 6:4. Pon Lendl: Alcaraz vs Tiafoe (14:00), Medvedev vs Cobolli (20:30).",
        "zh": "都灵周日：谢尔顿6-2、3-6、6-3击败菲斯；兹维列夫6-4、6-4轻取霍达尔。周一伦德尔组：阿尔卡拉斯对蒂亚福，梅德韦杰夫对科博利。",
        "ja": "トリノ日曜：シェルトンがフィスを6-2、3-6、6-3で撃破；ズベレフがジョダルに6-4、6-4完勝。月曜：アルカラス対ティアフォー、メドベージェフ対コボッリ。",
        "ko": "토리노 일요: 셸턴 피스에 6-2, 3-6, 6-3 승리; 즈베레프 호다르에 6-4, 6-4 승리. 월요 렌들 조: 알카라스 vs 티아포, 메드베데프 vs 코볼리.",
        "ar": "تورينو الأحد: شيلتون يهزم فيس 6-2 و3-6 و6-3؛ وزفيريف يهزم خودار 6-4 و6-4. الاثنين: ألكاراز ضد تيافو، وميدفيديف ضد كوبولي.",
    }

    pl_foot_map = {
        "en": "Sun: Spain 2-3 England (Kane 45 pen, Konsa 53, White 58; Oyarzabal 65 pen, Williams 75). PL: Arsenal 27, Brighton 22, City 21.",
        "fr": "Dim : Espagne 2-3 Angleterre (Kane 45 sp, Konsa 53, White 58 ; Oyarzabal 65 sp, Williams 75). PL : Arsenal 27, Brighton 22, City 21.",
        "es": "Dom: Espana 2-3 Inglaterra (Kane 45 p, Konsa 53, White 58; Oyarzabal 65 p, Williams 75). PL: Arsenal 27, Brighton 22, City 21.",
        "de": "So: Spanien 2:3 England (Kane 45. FE, Konsa 53., White 58.; Oyarzabal 65. FE, Williams 75.). PL: Arsenal 27, Brighton 22, City 21.",
        "it": "Dom: Spagna 2-3 Inghilterra (Kane 45 r, Konsa 53, White 58; Oyarzabal 65 r, Williams 75). PL: Arsenal 27, Brighton 22, City 21.",
        "pl": "Niedz: Hiszpania 2:3 Anglia (Kane 45 k, Konsa 53, White 58; Oyarzabal 65 k, Williams 75). PL: Arsenal 27, Brighton 22, City 21.",
        "zh": "周日：西班牙2-3英格兰（凯恩45点，孔萨53，怀特58；奥亚萨瓦尔65点，威廉姆斯75）。英超：阿森纳27分领跑。",
        "ja": "日曜：スペイン2-3イングランド（ケイン45PK、コンサ53、ホワイト58；オヤルサバル65PK、ウィリアムズ75）。PL首位アーセナル27点。",
        "ko": "일요: 스페인 2-3 잉글랜드 (케인 45 PK, 콘사 53, 화이트 58; 오야르사발 65 PK, 윌리엄스 75). PL 아스널 27점 선두.",
        "ar": "الأحد: إسبانيا 2-3 إنجلترا (كين 45 ج، كونسا 53، وايت 58؛ أويارزابال 65 ج، ويليامز 75). أرسنال 27 نقطة في الصدارة.",
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

    en_today = "Monday desk: MNF Chargers at Ravens in Harbaugh Bowl. England shock Spain 3-2 in Madrid. Spurs win 12th in a row; Alcaraz opens Turin Monday."
    en_tonight = "Monday Night Football features Jim vs John Harbaugh in Baltimore (8:15 PM ET). Sunday: England stun Spain 3-2 to win Group A3; Lions rout Patriots 35-10 in Munich (Gibbs 252 yds); Spurs claim 12th straight win 110-102 over Jazz; Shelton beats Fils in Turin thriller; McIlroy celebrates 8th Race to Dubai title."
    en_nfl = "MNF Tonight: Chargers at Ravens (8:15 PM ET, M&T Bank Stadium). Sunday Munich: Lions 35-10 Patriots (Gibbs 252 scrimmage yds, 2 TDs; Maye hurt ankle)."
    en_tnf = "NFL Week 10: Chargers at Ravens on Monday Night Football. Sunday Munich: Lions 35, Patriots 10. Thursday: Commanders 24-21 Giants."

    # EN
    en_block = re.sub(r'todayDesk:\s*"[^"]*"', f'todayDesk: "{en_today}"', en_block, count=1)
    en_block = re.sub(r'todayNfl:\s*"[^"]*"', f'todayNfl: "{en_nfl}"', en_block, count=1)
    en_block = re.sub(r'todayTnf:\s*"[^"]*"', f'todayTnf: "{en_tnf}"', en_block, count=1)
    en_block = re.sub(r'tonightBlurb:\s*"[^"]*"', f'tonightBlurb: "{en_tonight}"', en_block, count=1)

    en_block = re.sub(r'(football:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"MNF Tonight: Chargers at Ravens in Harbaugh Bowl; Lions rout Patriots 35-10 in Munich."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(football:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Tonight: Chargers at Ravens (8:15 PM ET, M&T Bank Stadium, Harbaugh Bowl). Sun Munich: Lions 35-10 Patriots (Gibbs 252 yds, 2 TDs)."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(football:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"MNF TONIGHT: CHARGERS AT RAVENS IN HARBAUGH BOWL; LIONS ROUT PATRIOTS 35-10 IN MUNICH"', en_block, count=1, flags=re.DOTALL)

    en_block = re.sub(r'(soccer:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"England shock Spain 3-2 in Madrid thriller to claim Group A3 top spot; Denmark crush Portugal 4-1."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(soccer:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Sun: Spain 2-3 England (Kane 45 pen, Konsa 53, White 58; Oyarzabal 65 pen, Williams 75). PL: Arsenal 27, Brighton 22, City 21."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(soccer:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"NATIONS LEAGUE: ENGLAND STUN SPAIN 3-2 IN MADRID; THREE LIONS CLAIM GROUP A3 TOP SEED"', en_block, count=1, flags=re.DOTALL)

    en_block = re.sub(r'(basketball:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Spurs extend streak to 12 behind Wembanyama and Harper; Lakers outlast Suns 131-123."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(basketball:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Sun: Spurs 110-102 Jazz (Wembanyama 26/11/6/5, Harper 31, 12 in a row); Lakers 131-123 Suns; Celtics 131-94 Mavs; Knicks 112-108 Raptors (OT)."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(basketball:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"NBA SUNDAY: SPURS WIN 12TH STRAIGHT, DOWN JAZZ 110-102; LAKERS BEAT SUNS 131-123"', en_block, count=1, flags=re.DOTALL)

    en_block = re.sub(r'(golf:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"McIlroy celebrates record-equalling 8th Race to Dubai title; RSM Classic tournament week begins."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(golf:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Dubai Complete: 1. Hatton -15 (273); 2. McIlroy -10 (278, seals 8th season crown by 125 pts). Next: RSM Classic at Sea Island (19-22 Nov)."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(golf:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"MCILROY SEALS RECORD-EQUALING 8TH RACE TO DUBAI; PGA TOUR HEADS TO SEA ISLAND FOR RSM CLASSIC"', en_block, count=1, flags=re.DOTALL)

    en_block = re.sub(r'(tennis:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Turin ATP Finals: Shelton edges Fils in three; Alcaraz meets Tiafoe as Lendl Group opens Monday."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(tennis:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Turin Sun: Shelton d Fils 6-2, 3-6, 6-3; Zverev d Jodar 6-4, 6-4. Mon Lendl Group: Alcaraz vs Tiafoe (14:00 CET), Medvedev vs Cobolli (20:30 CET)."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(tennis:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"TURIN ATP FINALS: SHELTON EDGES FILS 6-2, 3-6, 6-3; ALCARAZ MEETS TIAFOE ON MONDAY"', en_block, count=1, flags=re.DOTALL)

    en_block = re.sub(r'(f1:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Three days to Round 21 Las Vegas: 33 points cover five drivers in furious shootout for P2."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(f1:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Drivers P2 battle: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Vegas Strip: 19-21 Nov."', en_block, count=1, flags=re.DOTALL)
    en_block = re.sub(r'(f1:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"THREE DAYS TO VEGAS: 33 POINTS SPLIT VERSTAPPEN TO NORRIS FOR RUNNER-UP HONORS"', en_block, count=1, flags=re.DOTALL)

    # FR
    fr_today = "Bureau du lundi : MNF Chargers-Ravens dans le Harbaugh Bowl. L'Angleterre surprend l'Espagne 3-2 a Madrid. Les Spurs a 12 victoires ; Alcaraz ouvre a Turin."
    fr_tonight = "Monday Night Football met aux prises Jim et John Harbaugh a Baltimore. Dimanche : l'Angleterre bat l'Espagne 3-2 ; Detroit domine New England 35-10 a Munich (Gibbs 252 yds) ; San Antonio enchaine une 12e victoire ; Shelton domine Fils a Turin ; McIlroy fete son 8e sacre."
    fr_nfl = "MNF ce soir : Chargers vs Ravens a Baltimore (M&T Bank Stadium). Dimanche Munich : Lions 35-10 Patriots (Gibbs 252 yds, 2 TD ; Maye blesse a la cheville)."
    fr_tnf = "NFL Semaine 10 : Chargers vs Ravens au Monday Night. Dimanche Munich : Lions 35, Patriots 10. Jeudi : Commanders 24-21 Giants."

    fr_block = re.sub(r'todayDesk:\s*"[^"]*"', f'todayDesk: "{fr_today}"', fr_block, count=1)
    fr_block = re.sub(r'todayNfl:\s*"[^"]*"', f'todayNfl: "{fr_nfl}"', fr_block, count=1)
    fr_block = re.sub(r'todayTnf:\s*"[^"]*"', f'todayTnf: "{fr_tnf}"', fr_block, count=1)
    fr_block = re.sub(r'tonightBlurb:\s*"[^"]*"', f'tonightBlurb: "{fr_tonight}"', fr_block, count=1)

    fr_block = re.sub(r'(football:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"MNF ce soir : duel des freres Harbaugh a Baltimore ; les Lions surclassent les Patriots 35-10 a Munich."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(football:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Ce soir : Chargers chez les Ravens (Harbaugh Bowl). Dim Munich : Lions 35-10 Patriots (Gibbs 252 yds, 2 TD)."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(football:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"MNF CE SOIR : CHARGERS CHEZ LES RAVENS ; LES LIONS ECRASTENT LES PATRIOTS 35-10 A MUNICH"', fr_block, count=1, flags=re.DOTALL)

    fr_block = re.sub(r'(soccer:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"L\'Angleterre surprend l\'Espagne 3-2 a Madrid pour la tete du Groupe A3 ; le Danemark bat le Portugal 4-1."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(soccer:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Dim : Espagne 2-3 Angleterre (Kane 45 sp, Konsa 53, White 58 ; Oyarzabal 65 sp, Williams 75). PL : Arsenal 27, Brighton 22, City 21."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(soccer:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"LIGUE DES NATIONS : L\'ANGLETERRE BAT L\'ESPAGNE 3-2 A MADRID ET FINIT EN TETE DU GROUPE A3"', fr_block, count=1, flags=re.DOTALL)

    fr_block = re.sub(r'(basketball:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Les Spurs montent a 12 victoires de suite avec Wembanyama et Harper ; les Lakers dominent les Suns 131-123."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(basketball:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Dim : Spurs 110-102 Jazz (Wembanyama 26/11/6/5, Harper 31, 12 de suite) ; Lakers 131-123 Suns ; Celtics 131-94 Mavs."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(basketball:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"NBA DIMANCHE : 12E SUCCES DE SUITE POUR LES SPURS (110-102 CONTRE LE JAZZ) ; LES LAKERS GAGNENT"', fr_block, count=1, flags=re.DOTALL)

    fr_block = re.sub(r'(golf:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"McIlroy fete son 8e sacre a la Race to Dubai ; la semaine du RSM Classic s\'ouvre sur le PGA Tour."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(golf:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Dubai termine : 1. Hatton -15 (273) ; 2. McIlroy -10 (278, 8e titre par 125 pts). Prochain : RSM Classic a Sea Island."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(golf:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"MCILROY EGALISE LE RECORD DE 8 TITRES EUROPEENS ; LE PGA TOUR EN ROUTE POUR SEA ISLAND"', fr_block, count=1, flags=re.DOTALL)

    fr_block = re.sub(r'(tennis:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"Masters de Turin : Shelton dompte Fils en 3 sets ; Alcaraz defie Tiafoe dans le groupe Lendl lundi."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(tennis:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Turin dim : Shelton bat Fils 6-2, 3-6, 6-3 ; Zverev bat Jodar 6-4, 6-4. Lun Lendl : Alcaraz vs Tiafoe (14h00), Medvedev vs Cobolli (20h30)."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(tennis:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"MASTERS DE TURIN : SHELTON S\'IMPOSE EN TROIS SETS FACE A FILS ; ALCARAZ ENTRE EN PISTE LUNDI"', fr_block, count=1, flags=re.DOTALL)

    fr_block = re.sub(r'(f1:\s*\{[^}]*?tagline:\s*)"[^"]*"', r'\g<1>"J-3 avant Las Vegas : 33 points separent 5 pilotes pour la place de vice-champion."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(f1:\s*\{[^}]*?liveNow:\s*)"[^"]*"', r'\g<1>"Duel P2 : Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390). Strip de Vegas : 19-21 nov."', fr_block, count=1, flags=re.DOTALL)
    fr_block = re.sub(r'(f1:\s*\{[^}]*?pulse:\s*)"[^"]*"', r'\g<1>"J-3 AVANT VEGAS : 33 POINTS SEPARENT VERSTAPPEN A NORRIS POUR LE TITRE DE VICE-CHAMPION"', fr_block, count=1, flags=re.DOTALL)

    open(path_main, "w", encoding="utf-8", newline="\n").write(en_block + fr_block)
    print("Updated messages.ts.")

    # Other locales
    locales_data = {
        "es": {
            "todayDesk": "Mesa del lunes: MNF Chargers en Ravens en el Harbaugh Bowl. Inglaterra supera 3-2 a Espana en Madrid. Spurs suman 12 seguidas; Alcaraz debuta en Turin.",
            "tonightBlurb": "Monday Night Football presenta el duelo de los hermanos Harbaugh en Baltimore. Domingo: Inglaterra vence 3-2 a Espana; Lions arrollan a Patriots 35-10 en Munich; Spurs ganan su 12do partido al hilo; Shelton bate a Fils en Turin; McIlroy celebra su octava Race to Dubai.",
            "todayNfl": "MNF esta noche: Chargers en Ravens (M&T Bank Stadium). Domingo Munich: Lions 35-10 Patriots (Gibbs 252 yardas, 2 TD; Maye lesionado).",
            "todayTnf": "NFL Semana 10: Chargers contra Ravens en Monday Night. Domingo Munich: Lions 35, Patriots 10. Jueves: Commanders 24-21 Giants.",
            "fb_tag": "MNF esta noche: Chargers en Ravens en el Harbaugh Bowl; Lions aplastan 35-10 a Patriots en Munich.",
            "fb_live": "Esta noche: Chargers en Ravens (Harbaugh Bowl). Dom Munich: Lions 35-10 Patriots (Gibbs 252 yds, 2 TD).",
            "fb_pulse": "MNF ESTA NOCHE: CHARGERS EN RAVENS EN EL HARBAUGH BOWL; LIONS ARROLLAN A PATRIOTS 35-10 EN MUNICH",
            "soc_tag": "Inglaterra vence 3-2 a Espana en Madrid para liderar el Grupo A3; Dinamarca golea 4-1 a Portugal.",
            "soc_live": "Dom: Espana 2-3 Inglaterra (Kane 45 p, Konsa 53, White 58; Oyarzabal 65 p, Williams 75). PL: Arsenal 27, Brighton 22, City 21.",
            "soc_pulse": "LIGA DE NACIONES: INGLATERRA VENCE 3-2 A ESPANA EN MADRID Y GANA EL GRUPO A3",
            "bb_tag": "Los Spurs alargan racha a 12 con Wembanyama y Harper; Lakers superan a Suns 131-123.",
            "bb_live": "Dom: Spurs 110-102 Jazz (Wembanyama 26/11/6/5, Harper 31, 12 seguidas); Lakers 131-123 Suns; Celtics 131-94 Mavs.",
            "bb_pulse": "NBA DOMINGO: SPURS SUMAN 12 VICTORIAS SEGUIDAS ANTE JAZZ 110-102; LAKERS GANAN",
            "gf_tag": "McIlroy festeja su octavo titulo de la Race to Dubai; arranca la semana del RSM Classic en el PGA Tour.",
            "gf_live": "Dubai finalizado: 1. Hatton -15 (273); 2. McIlroy -10 (278, campeon por 125 pts). Proximo: RSM Classic en Sea Island.",
            "gf_pulse": "MCILROY SELLA OCTAVO TITULO DE LA RACE TO DUBAI; EL PGA TOUR VIAJA A SEA ISLAND",
            "tn_tag": "Finales ATP de Turin: Shelton bate a Fils en tres sets; Alcaraz debuta ante Tiafoe este lunes.",
            "tn_live": "Turin dom: Shelton vence a Fils 6-2, 3-6, 6-3; Zverev vence a Jodar 6-4, 6-4. Lun Lendl: Alcaraz vs Tiafoe (14:00 CET), Medvedev vs Cobolli (20:30 CET).",
            "tn_pulse": "FINALES ATP DE TURIN: SHELTON BATE A FILS EN TRES SETS; ALCARAZ DEBUTA EL LUNES",
            "f1_tag": "A tres dias de Las Vegas: 33 puntos separan a cinco pilotos en la puja por el subcampeonato.",
            "f1_live": "Lucha por P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390). Strip: 19-21 nov.",
            "f1_pulse": "A TRES DIAS DE LAS VEGAS: 33 PUNTOS SEPARAN A VERSTAPPEN DE NORRIS POR EL SEGUNDO PUESTO"
        },
        "de": {
            "todayDesk": "Montagspult: MNF Chargers bei Ravens im Harbaugh Bowl. England schockt Spanien 3:2 in Madrid. Spurs holen 12. Sieg; Alcaraz startet in Turin.",
            "tonightBlurb": "Monday Night Football praesentiert das Bruder-Duell Jim gegen John Harbaugh in Baltimore. Sonntag: England besiegt Spanien 3:2; Lions dominieren Patriots 35:10 in Muenchen; Spurs siegen 110:102 in Utah; Shelton siegt in Turin; McIlroy feiert 8. Race to Dubai.",
            "todayNfl": "MNF heute Nacht: Chargers bei Ravens (M&T Bank Stadium). Sonntag Muenchen: Lions 35:10 Patriots (Gibbs 252 Yds, 2 TD; Maye verletzt).",
            "todayTnf": "NFL Woche 10: Chargers bei Ravens am Monday Night. Sonntag Muenchen: Lions 35, Patriots 10. Donnerstag: Commanders 24:21 Giants.",
            "fb_tag": "MNF heute Nacht: Chargers bei Ravens im Harbaugh Bowl; Lions zerlegen Patriots 35:10 in Muenchen.",
            "fb_live": "Heute Nacht: Chargers bei Ravens (Harbaugh Bowl). So Muenchen: Lions 35:10 Patriots (Gibbs 252 Yds, 2 TD).",
            "fb_pulse": "MNF HEUTE NACHT: CHARGERS BEI RAVENS IM HARBAUGH BOWL; LIONS DOMINIEREN PATRIOTS 35:10 IN MUENCHEN",
            "soc_tag": "England bezwingt Spanien 3:2 in Madrid und sichert sich Platz eins in Gruppe A3; Daenemark schlaegt Portugal 4:1.",
            "soc_live": "So: Spanien 2:3 England (Kane 45. FE, Konsa 53., White 58.; Oyarzabal 65. FE, Williams 75.). PL: Arsenal 27, Brighton 22, City 21.",
            "soc_pulse": "NATIONS LEAGUE: ENGLAND SCHOCKT SPANIEN 3:2 IN MADRID UND HOLT DEN GRUPPENSIEG",
            "bb_tag": "Spurs bauen Serie dank Wembanyama und Harper auf 12 Siege aus; Lakers schlagen Suns 131:123.",
            "bb_live": "So: Spurs 110:102 Jazz (Wembanyama 26/11/6/5, Harper 31, 12 in Folge); Lakers 131:123 Suns; Celtics 131:94 Mavs.",
            "bb_pulse": "NBA SONNTAG: SPURS FEIERN 12. SIEG IN SERIE MIT 110:102 GEGEN JAZZ; LAKERS SIEGEN",
            "gf_tag": "McIlroy feiert 8. Race-to-Dubai-Titel; PGA Tour blickt auf die RSM Classic auf Sea Island.",
            "gf_live": "Dubai komplett: 1. Hatton -15 (273); 2. McIlroy -10 (278, Saisontitel um 125 Pkt). Naechster Halt: RSM Classic auf Sea Island.",
            "gf_pulse": "MCILROY STELLT MIT 8. TITEL REKORD EIN; PGA TOUR REIST ZUR RSM CLASSIC",
            "tn_tag": "ATP Finals Turin: Shelton bezwingt Fils in drei Saetzen; Alcaraz startet am Montag gegen Tiafoe.",
            "tn_live": "Turin So: Shelton besiegt Fils 6:2, 3:6, 6:3; Zverev schlaegt Jodar 6:4, 6:4. Mo Lendl: Alcaraz vs. Tiafoe (14:00 MEZ), Medvedev vs. Cobolli (20:30 MEZ).",
            "tn_pulse": "ATP FINALS TURIN: SHELTON SIEGT IN DREI SAETZEN GEGEN FILS; ALCARAZ GREIFT MONTAG EIN",
            "f1_tag": "Drei Tage bis Las Vegas: 33 Punkte trennen fuenf Fahrer im Kampf um die Vize-Weltmeisterschaft.",
            "f1_live": "P2-Kampf: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390). Strip: 19.-21. Nov.",
            "f1_pulse": "DREI TAGE BIS VEGAS: 33 PUNKTE ABSTAND ZWISCHEN VERSTAPPEN UND NORRIS UM PLATZ ZWEI"
        },
        "it": {
            "todayDesk": "Desk del lunedi: MNF Chargers a Baltimora nell'Harbaugh Bowl. L'Inghilterra batte la Spagna 3-2 a Madrid. Spurs a quota 12; Alcaraz debutta a Torino.",
            "tonightBlurb": "Monday Night Football con la sfida tra i fratelli Harbaugh a Baltimora. Domenica: l'Inghilterra batte la Spagna 3-2; Detroit travolge i Patriots 35-10 a Monaco (Gibbs 252 yard); 12ma vittoria Spurs; Shelton supera Fils; McIlroy festeggia l'8a Race to Dubai.",
            "todayNfl": "MNF stasera: Chargers a Baltimora (M&T Bank Stadium). Domenica Monaco: Lions 35-10 Patriots (Gibbs 252 yds, 2 TD; Maye infortunato).",
            "todayTnf": "NFL Settimana 10: Chargers contro Ravens al Monday Night. Domenica Monaco: Lions 35, Patriots 10. Giovedi: Commanders 24-21 Giants.",
            "fb_tag": "MNF stasera: Chargers a Baltimora nell'Harbaugh Bowl; Lions dominano i Patriots 35-10 a Monaco.",
            "fb_live": "Stasera: Chargers contro Ravens (Harbaugh Bowl). Dom Monaco: Lions 35-10 Patriots (Gibbs 252 yds, 2 TD).",
            "fb_pulse": "MNF STASERA: CHARGERS CONTRO RAVENS NELL'HARBAUGH BOWL; LIONS TRAVOLGONO I PATRIOTS A MONACO",
            "soc_tag": "L'Inghilterra batte la Spagna 3-2 a Madrid e vince il Gruppo A3; la Danimarca supera il Portogallo 4-1.",
            "soc_live": "Dom: Spagna 2-3 Inghilterra (Kane 45 r, Konsa 53, White 58; Oyarzabal 65 r, Williams 75). PL: Arsenal 27, Brighton 22, City 21.",
            "soc_pulse": "NATIONS LEAGUE: L'INGHILTERRA BATTE LA SPAGNA 3-2 A MADRID E CONQUISTA IL PRIMATO NEL GIRONE",
            "bb_tag": "Gli Spurs volano a 12 vittorie con Wembanyama e Harper; i Lakers superano i Suns 131-123.",
            "bb_live": "Dom: Spurs 110-102 Jazz (Wembanyama 26/11/6/5, Harper 31, 12 di fila); Lakers 131-123 Suns; Celtics 131-94 Mavs.",
            "bb_pulse": "NBA DOMENICA: SPURS A QUOTA 12 SUCCESSI DI FILA CON IL 110-102 SUI JAZZ; VINCONO I LAKERS",
            "gf_tag": "McIlroy festeggia l'ottava Race to Dubai; il PGA Tour si prepara al RSM Classic a Sea Island.",
            "gf_live": "Dubai conclusa: 1. Hatton -15 (273); 2. McIlroy -10 (278, campione per 125 pt). Prossimo: RSM Classic a Sea Island.",
            "gf_pulse": "MCILROY VINCE L'OTTAVO TITOLO DELLA RACE TO DUBAI; IL PGA TOUR VERSO SEA ISLAND",
            "tn_tag": "ATP Finals Torino: Shelton batte Fils in tre set; Alcaraz debutta con Tiafoe questo lunedi.",
            "tn_live": "Torino dom: Shelton batte Fils 6-2, 3-6, 6-3; Zverev batte Jodar 6-4, 6-4. Lun Lendl: Alcaraz vs Tiafoe (14:00), Medvedev vs Cobolli (20:30).",
            "tn_pulse": "ATP FINALS TORINO: SHELTON PIEGA FILS IN TRE SET; ALCARAZ IN CAMPO LUNEDI",
            "f1_tag": "Tre giorni a Las Vegas: 33 punti dividono cinque piloti per il titolo di vicecampione.",
            "f1_live": "Corsa P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390). Strip: 19-21 nov.",
            "f1_pulse": "TRE GIORNI A LAS VEGAS: 33 PUNTI TRA VERSTAPPEN E NORRIS NELLA CORSA AL SECONDO POSTO"
        },
        "pl": {
            "todayDesk": "Poniedzialkowy pulpit: MNF Chargers u Ravens w Harbaugh Bowl. Anglia szokuje Hiszpanie 3:2 w Madrycie. Spurs maja 12 z rzedu; Alcaraz w Turynie.",
            "tonightBlurb": "Monday Night Football przynosi pojedynek braci Harbaugh w Baltimore. Niedziela: Anglia bije Hiszpanie 3:2; Lions gromia Patriots 35:10 w Monachium; 12. wygrana Spurs z rzedu; Shelton pokonuje Filsa; McIlroy swietuje 8. Race to Dubai.",
            "todayNfl": "MNF dzis w nocy: Chargers u Ravens (M&T Bank Stadium). Niedziela Monachium: Lions 35:10 Patriots (Gibbs 252 jardy, 2 TD; Maye kontuzjowany).",
            "todayTnf": "NFL Tydzien 10: Chargers z Ravens w Monday Night. Niedziela Monachium: Lions 35, Patriots 10. Czwartek: Commanders 24-21 Giants.",
            "fb_tag": "MNF dzis w nocy: Chargers u Ravens w Harbaugh Bowl; Lions rozbijaja Patriots 35:10 w Monachium.",
            "fb_live": "Dzis w nocy: Chargers u Ravens (Harbaugh Bowl). Niedz Monachium: Lions 35:10 Patriots (Gibbs 252 jardy, 2 TD).",
            "fb_pulse": "MNF DZIS W NOCY: CHARGERS U RAVENS W HARBAUGH BOWL; LIONS GROMIA PATRIOTS 35:10 W MONACHIUM",
            "soc_tag": "Anglia pokonuje Hiszpanie 3:2 w Madrycie i wygrywa grupe A3; Dania rozbija Portugalie 4:1.",
            "soc_live": "Niedz: Hiszpania 2:3 Anglia (Kane 45 k, Konsa 53, White 58; Oyarzabal 65 k, Williams 75). PL: Arsenal 27, Brighton 22, City 21.",
            "soc_pulse": "LIGA NARODOW: ANGLIA SZOKUJE HISZPANIE WYGRANA 3:2 W MADRYCIE I WYGRYWA GRUPE A3",
            "bb_tag": "Spurs przedluzaja serie do 12 wygranych dzieki Wembanyamie i Harperowi; Lakers pokonuja Suns 131:123.",
            "bb_live": "Niedz: Spurs 110:102 Jazz (Wembanyama 26/11/6/5, Harper 31, 12 z rzedu); Lakers 131:123 Suns; Celtics 131:94 Mavs.",
            "bb_pulse": "NBA NIEDZIELA: SPURS Z 12. WYGRANA Z RZEDU PO 110:102 Z JAZZ; LAKERS LEPSI OD SUNS",
            "gf_tag": "McIlroy cieszy sie z 8. tytulu Race to Dubai; PGA Tour przygotowuje sie do RSM Classic w Sea Island.",
            "gf_live": "Dubaj zakonczony: 1. Hatton -15 (273); 2. McIlroy -10 (278, mistrz o 125 pkt). Nastepnie: RSM Classic w Sea Island.",
            "gf_pulse": "MCILROY PIECZETUJE 8. TYTUL RACE TO DUBAI; PGA TOUR RUSZA DO SEA ISLAND",
            "tn_tag": "ATP Finals Turyn: Shelton pokonuje Filsa w trzech setach; Alcaraz gra z Tiafoe w poniedzialek.",
            "tn_live": "Turyn niedz: Shelton bije Filsa 6:2, 3:6, 6:3; Zverev bije Jodara 6:4, 6:4. Pon Lendl: Alcaraz vs Tiafoe (14:00), Medvedev vs Cobolli (20:30).",
            "tn_pulse": "ATP FINALS TURYN: SHELTON WYGRYWA W TRZECH SETACH Z FILSEM; ALCARAZ NA KORCIE W PONIEDZIALEK",
            "f1_tag": "Trzy dni do Las Vegas: 33 punkty dziela pieciu kierowcow w walce o wicemistrzostwo swiata.",
            "f1_live": "Batalia o P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390). Strip: 19-21 listopada.",
            "f1_pulse": "TRZY DNI DO LAS VEGAS: 33 PUNKTY ROZNICY POMIEDZY VERSTAPPENEM A NORRISEM W WALCE O P2"
        },
        "zh": {
            "todayDesk": "周一工作台：周一夜赛哈博兄弟德比充电器战乌鸦。英格兰3-2客胜西班牙夺小组头名。马刺豪取12连胜；阿尔卡拉斯都灵亮相。",
            "tonightBlurb": "周一夜赛聚焦巴尔的摩哈博兄弟对决。周日：英格兰3-2力克西班牙终结对手43场不败；雄狮慕尼黑35-10狂胜爱国者（吉布斯252码）；马刺击败爵士迎12连胜；谢尔顿三盘胜菲斯；麦克罗伊庆祝第八次总冠军。",
            "todayNfl": "今晚MNF：充电器做客巴尔的摩战乌鸦。周日慕尼黑赛：雄狮35-10爱国者（吉布斯252码2达阵，梅耶脚踝受伤）。",
            "todayTnf": "NFL第10周：周一夜赛充电器对决乌鸦。慕尼黑国际赛：雄狮35-10爱国者。周四夜赛：指挥官24-21巨人。",
            "fb_tag": "今晚MNF：哈博兄弟德比充电器战乌鸦；底特律雄狮在慕尼黑35-10横扫爱国者。",
            "fb_live": "今晚：充电器做客对阵乌鸦（哈博德比）。周日慕尼黑：雄狮35-10爱国者（吉布斯252码2达阵）。",
            "fb_pulse": "今晚MNF：充电器战乌鸦上演哈博德比；雄狮慕尼黑35-10大胜爱国者",
            "soc_tag": "英格兰在马德里3-2险胜西班牙夺欧国联A3组头名；丹麦4-1大胜葡萄牙。",
            "soc_live": "周日：西班牙2-3英格兰（凯恩45点，孔萨53，怀特58；奥亚萨瓦尔65点，威廉姆斯75）。英超阿森纳27分领跑。",
            "soc_pulse": "欧国联焦点：英格兰3-2客胜西班牙破对手43场不败锁定A3组头名",
            "bb_tag": "文班亚马与哈珀联手助马刺豪取12连胜；湖人131-123击退太阳。",
            "bb_live": "周日：马刺110-102爵士（文班26/11/6/5，哈珀31分，12连胜）；湖人131-123太阳；凯尔特人131-94独行侠。",
            "bb_pulse": "NBA周日战报：马刺110-102轻取爵士豪取12连胜；湖人战胜太阳",
            "gf_tag": "麦克罗伊庆祝追平纪录的第八座迪拜总冠军；美巡赛海岛RSM精英赛打响。",
            "gf_live": "迪拜收官：1. 哈顿-15（273）；2. 麦克罗伊-10（278，125分险胜加冕第8冠）。下一站：海岛RSM精英赛。",
            "gf_pulse": "麦克罗伊斩获第八座欧巡年度总冠军追平纪录；美巡赛移师海岛",
            "tn_tag": "ATP都灵总决赛：谢尔顿三盘力克菲斯；阿尔卡拉斯周一迎战蒂亚福。",
            "tn_live": "都灵周日：谢尔顿6-2、3-6、6-3胜菲斯；兹维列夫6-4、6-4胜霍达尔。周一：阿尔卡拉斯对蒂亚福，梅德韦杰夫对科博利。",
            "tn_pulse": "ATP都灵总决赛：谢尔顿三盘苦战胜菲斯；阿尔卡拉斯周一出战",
            "f1_tag": "拉斯维加斯站倒计时3天：五位车手相差33分展开年度亚军激烈角逐。",
            "f1_live": "年度次席之争：维斯塔潘279，拉塞尔262，汉密尔顿261，勒克莱尔249，诺里斯246（安东内利390）。赌城大道：19-21日。",
            "f1_pulse": "拉斯维加斯倒计时3天：五大车手相差33分争夺年度亚军荣耀"
        },
        "ja": {
            "todayDesk": "月曜デスク：MNFハーボー兄弟対決チャージャーズ対レイブンズ。イングランドがマドリードでスペインを3-2撃破。スパーズ12連勝、アルカラス初戦。",
            "tonightBlurb": "マンデーナイトでハーボー兄弟対決。日曜日：イングランドがスペインを3-2で下し43戦不敗をストップ；ライオンズがミュンヘンでペイトリオッツを35-10粉砕（ギブス252yd）；スパーズ12連勝；シェルトンがフィスを撃破；マキロイが8度目の年間王座を祝う。",
            "todayNfl": "今夜のMNF：チャージャーズ対レイブンズ（ボルティモア）。日曜ミュンヘン：ライオンズ35-10ペイトリオッツ（ギブス252yd 2TD、メイ足首負傷）。",
            "todayTnf": "NFL第10週：マンデーナイトでチャージャーズ対レイブンズ。ミュンヘン：ライオンズ35-10ペイトリオッツ。木曜：コマンダーズ24-21ジャイアンツ。",
            "fb_tag": "今夜のMNF：ハーボー兄弟対決チャージャーズ対レイブンズ；ライオンズがミュンヘンで35-10の快勝。",
            "fb_live": "今夜：チャージャーズ対レイブンズ（ハーボー対決）。日曜ミュンヘン：ライオンズ35-10ペイトリオッツ（ギブス252yd 2TD）。",
            "fb_pulse": "今夜のMNF：ハーボー兄弟対決チャージャーズ対レイブンズ；ライオンズがミュンヘンで圧勝",
            "soc_tag": "イングランドがマドリードでスペインを3-2で下しA3組首位通過；デンマークがポルトガルに4-1大勝。",
            "soc_live": "日曜：スペイン2-3イングランド（ケイン45PK、コンサ53、ホワイト58；オヤルサバル65PK、ウィリアムズ75）。PL首位アーセナル27点。",
            "soc_pulse": "ネーションズリーグ：イングランドがスペインを3-2で撃破しA3組首位シード獲得",
            "bb_tag": "ウェンバンヤマとハーパーの活躍でスパーズが12連勝；レイカーズがサンズを131-123で破る。",
            "bb_live": "日曜：スパーズ110-102ジャズ（ウェンバンヤマ26/11/6/5、ハーパー31、12連勝）；レイカーズ131-123サンズ；セルティックス131-94マーベリックス。",
            "bb_pulse": "NBA日曜：スパーズがジャズを110-102で退け12連勝；レイカーズ勝利",
            "gf_tag": "マキロイが歴代最多タイ8度目の年間王座を戴冠；PGAツアーはRSMクラシックへ突入。",
            "gf_live": "ドバイ終了：1. ハットン -15（273）；2. マキロイ -10（278、125pt差で年間制覇）。次戦：シーアイランドRSMクラシック。",
            "gf_pulse": "マキロイが通算8度目の年間王者を確定；PGAツアーはシーアイランドへ",
            "tn_tag": "ATPファイナルズ：シェルトンがフィスとの接戦を制す；月曜はアルカラスがティアフォーと激突。",
            "tn_live": "トリノ日曜：シェルトンがフィスを6-2、3-6、6-3で撃破；ズベレフがジョダルに6-4、6-4完勝。月曜：アルカラス対ティアフォー、メドベージェフ対コボッリ。",
            "tn_pulse": "ATPファイナルズ：シェルトンが3セットの熱戦を制す；月曜アルカラス登場",
            "f1_tag": "ラスベガス決戦まで3日：5名のドライバーが33点差でランキング2位を激しく争う。",
            "f1_live": "P2争い：フェルスタッペン279、ラッセル262、ハミルトン261、ルクレール249、ノリス246（アントネッリ390）。ストリップ：19-21日。",
            "f1_pulse": "ラスベガスまであと3日：フェルスタッペンからノリスまで33点差の2位争い"
        },
        "ko": {
            "todayDesk": "월요일 데스크: MNF 하버 형제 매치 차저스 대 레이븐스. 잉글랜드 마드리드서 스페인 3-2 제압. 스퍼스 12연승 질주; 알카라스 토리노 출격.",
            "tonightBlurb": "먼데이 나이트 풋볼서 볼티모어 하버 형제 매치 성사. 일요일: 잉글랜드 스페인 3-2 꺾고 43경기 무패 저지; 라이언스 뮌헨서 페이트리어츠 35-10 대파 (깁스 252야드); 스퍼스 12연승 질주; 셸턴 피스 격파; 매킬로이 8번째 타이틀 축하.",
            "todayNfl": "오늘 밤 MNF: 볼티모어 차저스 vs 레이븐스. 일요 뮌헨: 라이언스 35-10 페이트리어츠 (깁스 252야드 2TD; 메이 발목 부상).",
            "todayTnf": "NFL 10주차: 먼데이 나이트 차저스 vs 레이븐스. 뮌헨 인터내셔널: 라이언스 35-10 페이트리어츠. 목요일: 커맨더스 24-21 자이언츠.",
            "fb_tag": "오늘 밤 MNF: 하버 형제 매치 차저스 대 레이븐스; 라이언스 뮌헨서 페이트리어츠 35-10 대파.",
            "fb_live": "오늘 밤: 차저스 vs 레이븐스 (하버 볼). 일요 뮌헨: 라이언스 35-10 페이트리어츠 (깁스 252야드 2TD).",
            "fb_pulse": "오늘 밤 MNF: 하버 형제 더비 차저스 vs 레이븐스; 라이언스 뮌헨서 35-10 완승",
            "soc_tag": "잉글랜드 마드리드서 스페인 3-2 꺾고 A3조 1위 확보; 덴마크 포르투갈 4-1 대파.",
            "soc_live": "일요: 스페인 2-3 잉글랜드 (케인 45 PK, 콘사 53, 화이트 58; 오야르사발 65 PK, 윌리엄스 75). PL 아스널 27점 선두.",
            "soc_pulse": "네이션스리그: 잉글랜드 스페인 3-2 격파하고 43경기 무패 행진 저지 및 조 1위",
            "bb_tag": "웸반야마와 하퍼 앞세운 스퍼스 12연승 질주; 레이커스 선즈 131-123 제압.",
            "bb_live": "일요: 스퍼스 110-102 재즈 (웸반야마 26/11/6/5, 하퍼 31, 12연승); 레이커스 131-123 선즈; 셀틱스 131-94 매버릭스.",
            "bb_pulse": "NBA 일요일: 스퍼스 유타 110-102 꺾고 12연승 달성; 레이커스 승리",
            "gf_tag": "매킬로이 역대 최다 타이 8번째 레이스 투 두바이 제패; PGA 투어 RSM 클래식 개막.",
            "gf_live": "두바이 종료: 1. 해튼 -15 (273); 2. 매킬로이 -10 (278, 125점 차 8번째 제패). 다음: 시 아일랜드 RSM 클래식.",
            "gf_pulse": "매킬로이 8번째 유럽 투어 올해의 선수 금자탑; PGA 투어 시 아일랜드 격돌",
            "tn_tag": "ATP 파이널스 토리노: 셸턴 3세트 접전 끝 피스 제압; 알카라스 월요일 티아포와 격돌.",
            "tn_live": "토리노 일요: 셸턴 피스에 6-2, 3-6, 6-3 승리; 즈베레프 호다르에 6-4, 6-4 승리. 월요 렌들 조: 알카라스 vs 티아포, 메드베데프 vs 코볼리.",
            "tn_pulse": "ATP 파이널스: 셸턴 피스 꺾고 개막전 승리; 알카라스 월요일 출격",
            "f1_tag": "라스베이거스 스트립 결전 D-3: 드라이버 5명 33점 차 준우승 대접전.",
            "f1_live": "P2 경쟁: 베르스타펜 279, 러셀 262, 해밀턴 261, 르클레르 249, 노리스 246 (안토넬리 390). 스트립 서킷: 19-21일.",
            "f1_pulse": "라스베이거스 결전 D-3: 베르스타펜부터 노리스까지 33점 차 2위 쟁탈전"
        },
        "ar": {
            "todayDesk": "مكتب الاثنين: قمة مانداي نايت بين الإخوة هاربوه تشارجرز وريفنز. إنجلترا تصعق إسبانيا 3-2 في مدريد. سبيرز يحقق فوزه الـ12؛ وألكاراز يبدأ في تورينو.",
            "tonightBlurb": "مانداي نايت فوتبول يشهد نزال الإخوة هاربوه في بالتيمور. الأحد: إنجلترا تسقط إسبانيا 3-2 وتنهي سلسلة 43 مباراة بلا هزيمة؛ ديترويت يكتسح باتريوتس 35-10 في ميونخ؛ الفوز الـ12 توالياً لسبيرز؛ شيلتون يهزم فيس؛ ماكلروي يحتفل بلقبه الثامن.",
            "todayNfl": "الليلة MNF: تشارجرز ضد ريفنز في بالتيمور. الأحد ميونخ: لايونز 35-10 باتريوتس (جيبس 252 ياردة، وهبوطان؛ إصابة ماي).",
            "todayTnf": "NFL الأسبوع 10: تشارجرز ضد ريفنز في مانداي نايت. ميونخ: لايونز 35-10 باتريوتس. الخميس: كوماندرز 24-21 جاينتس.",
            "fb_tag": "الليلة MNF: صدام الإخوة هاربوه بين تشارجرز وريفنز؛ ولايونز يسحقون باتريوتس 35-10 في ميونخ.",
            "fb_live": "الليلة: تشارجرز ضد ريفنز (نزال هاربوه). الأحد ميونخ: لايونز 35-10 باتريوتس (جيبس 252 ياردة وهبوطان).",
            "fb_pulse": "الليلة MNF: صدام الإخوة هاربوه تشارجرز وريفنز؛ ولايونز يكتسحون باتريوتس 35-10 في ميونخ",
            "soc_tag": "إنجلترا تصعق إسبانيا بنتيجة 3-2 في مدريد وتنتزع صدارة المجموعة الثالثة؛ والدنمارك تسحق البرتغال 4-1.",
            "soc_live": "الأحد: إسبانيا 2-3 إنجلترا (كين 45 ج، كونسا 53، وايت 58؛ أويارزابال 65 ج، ويليامز 75). أرسنال 27 نقطة في الصدارة.",
            "soc_pulse": "دوري الأمم: إنجلترا تصعق إسبانيا 3-2 في مدريد وتنتزع صدارة المجموعة الثالثة",
            "bb_tag": "سبيرز يمددون سلسلة انتصاراتهم إلى 12 مباراة مع ويمبانياما وهاربر؛ وليكرز يهزمون صنز 131-123.",
            "bb_live": "الأحد: سبيرز 110-102 جاز (ويمبانياما 26/11/6/5، وهاربر 31، 12 توالياً)؛ ليكرز 131-123 صنز؛ سلتكس 131-94 مافريكس.",
            "bb_pulse": "NBA الأحد: سبيرز يحقق الفوز الـ12 توالياً بإسقاط جاز 110-102؛ وليكرز يفوزون",
            "gf_tag": "ماكلروي يحتفل بلقبه الثامن القياسي في السباق إلى دبي؛ وبطولة RSM كلاسيك تنطلق على الجولة الأمريكية.",
            "gf_live": "ختام دبي: 1. هاتون -15 (273)؛ 2. ماكلروي -10 (278، بطل بفارق 125 نقطة). التالي: RSM كلاسيك في سي آيلاند.",
            "gf_pulse": "ماكلروي يعادل الرقم القياسي بلقبه الأوروبي الثامن؛ وجولة PGA تتجه إلى سي آيلاند",
            "tn_tag": "نهائيات تورينو: شيلتون يتجاوز فيس في ثلاث مجموعات؛ وألكاراز يستهل مشواره أمام تيافو يوم الاثنين.",
            "tn_live": "تورينو الأحد: شيلتون يهزم فيس 6-2 و3-6 و6-3؛ وزفيريف يهزم خودار 6-4 و6-4. الاثنين: ألكاراز ضد تيافو، وميدفيديف ضد كوبولي.",
            "tn_pulse": "نهائيات تورينو: شيلتون يحسم مواجهة فيس في ثلاث مجموعات؛ وألكاراز يبدأ الاثنين",
            "f1_tag": "ثلاثة أيام على جائزة لاس فيغاس: 33 نقطة تفصل خمسة سائقين في صراع وصافة بطولة العالم.",
            "f1_live": "صراع الوصافة: فيرستابن 279، راسل 262، هاميلتون 261، لوكلير 249، نوريس 246 (أنتونيللي 390). حلبة ستريب: 19-21 نوفمبر.",
            "f1_pulse": "ثلاثة أيام على لاس فيغاس: 33 نقطة تفصل فيرستابن عن نوريس في صراع الوصافة"
        }
    }

    for loc, data in locales_data.items():
        loc_file = f"frontend/src/i18n/messages-{loc}.ts"
        c = open(loc_file, "r", encoding="utf-8").read()
        c = re.sub(r'todayDesk:\s*"[^"]*"', f'todayDesk: "{data["todayDesk"]}"', c, count=1)
        c = re.sub(r'todayNfl:\s*"[^"]*"', f'todayNfl: "{data["todayNfl"]}"', c, count=1)
        c = re.sub(r'todayTnf:\s*"[^"]*"', f'todayTnf: "{data["todayTnf"]}"', c, count=1)
        c = re.sub(r'tonightBlurb:\s*"[^"]*"', f'tonightBlurb: "{data["tonightBlurb"]}"', c, count=1)

        c = re.sub(r'(football:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{data["fb_tag"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(football:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{data["fb_live"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(football:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{data["fb_pulse"]}"', c, count=1, flags=re.DOTALL)

        c = re.sub(r'(soccer:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{data["soc_tag"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(soccer:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{data["soc_live"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(soccer:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{data["soc_pulse"]}"', c, count=1, flags=re.DOTALL)

        c = re.sub(r'(basketball:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{data["bb_tag"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(basketball:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{data["bb_live"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(basketball:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{data["bb_pulse"]}"', c, count=1, flags=re.DOTALL)

        c = re.sub(r'(golf:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{data["gf_tag"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(golf:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{data["gf_live"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(golf:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{data["gf_pulse"]}"', c, count=1, flags=re.DOTALL)

        c = re.sub(r'(tennis:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{data["tn_tag"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(tennis:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{data["tn_live"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(tennis:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{data["tn_pulse"]}"', c, count=1, flags=re.DOTALL)

        c = re.sub(r'(f1:\s*\{[^}]*?tagline:\s*)"[^"]*"', rf'\g<1>"{data["f1_tag"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(f1:\s*\{[^}]*?liveNow:\s*)"[^"]*"', rf'\g<1>"{data["f1_live"]}"', c, count=1, flags=re.DOTALL)
        c = re.sub(r'(f1:\s*\{[^}]*?pulse:\s*)"[^"]*"', rf'\g<1>"{data["f1_pulse"]}"', c, count=1, flags=re.DOTALL)

        open(loc_file, "w", encoding="utf-8", newline="\n").write(c)
        print(f"Updated {loc_file}.")

if __name__ == "__main__":
    update_playground()
    update_messages()

