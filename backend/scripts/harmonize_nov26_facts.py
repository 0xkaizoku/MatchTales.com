# Harmonize 2026-11-26 facts cleanly across desk, matches, stories, playground, and all 10 UI locales.
import os
import json
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# 1. Fix Houston Texans 4-7 -> 4-6 in colts-at-texans, desk.json, playground.ts, messages*.ts
replacements_global = [
    ("TEX 4-7", "HOU 4-6"),
    ("(4-7 vs 3-8)", "(4-6 vs 3-8)"),
    ("(4-7对3-8)", "(4-6对3-8)"),
    ("improve to 4-7", "improve to 4-6"),
    ("improves to 4-7", "improves to 4-6"),
]

def patch_file(rel_path, reps):
    p = os.path.join(ROOT, rel_path)
    txt = open(p, "r", encoding="utf-8").read()
    orig = txt
    for old, new in reps:
        txt = txt.replace(old, new)
    if "\u2014" in txt:
        raise ValueError(f"Em-dash in {rel_path}")
    if rel_path.endswith(".json") or rel_path.endswith(".ts"):
        if "--" in txt:
            raise ValueError(f"Double-hyphen in {rel_path}")
    if txt != orig:
        open(p, "w", encoding="utf-8").write(txt)
        print(f"Harmonized {rel_path}")

patch_file("frontend/src/content/matches/colts-at-texans-tnf-week11-2026.json", replacements_global)
patch_file("frontend/src/data/desk.json", replacements_global)
patch_file("frontend/src/i18n/playground.ts", replacements_global)

# 2. Remove unverified Sabah 0-1 HT score from messages*.ts and harmonize Vegas GP & Texans 4-6 & Bellingham 59/60
msg_reps = replacements_global + [
    # English
    ("Sabah 0-1 Barca HT", "Wed UCL slate unpublished"),
    ("Wed HT: Sabah 0-1 Barcelona.", "Wed UCL slate unpublished."),
    ("Sabah 0-1 Barcelona HT as Wednesday night slate opens.", "Arsenal 1-1 Dortmund; Man City 2-2 Napoli."),
    ("Sabah 0-1 Barcelona HT. Davis Cup Bologna Live: Italy 1-0 South Korea.", "Arsenal 1-1 Dortmund. Davis Cup Bologna: Czechia 2-0 Canada; Italy vs Korea open after Musetti win."),
    ("Davis Cup Bologna Live: Italy 1-0 South Korea", "Davis Cup Bologna: Italy vs Korea open after Musetti win"),
    ("2027 MASTERS TICKET", "PGA TOUR EXEMPTION THROUGH 2028"),
    # French
    ("Sabah 0-1 Barcelone MT", "mercredi LDC a suivre"),
    ("Mercredi MT : Sabah 0-1 Barcelone.", "Mercredi LDC non publie."),
    ("Sabah 0-1 Barcelone a la pause.", "Arsenal 1-1 Dortmund et Man City 2-2 Naples."),
    ("Sabah 0-1 Barcelone MT. Coupe Davis en direct : Italie 1-0 Coree du Sud.", "Arsenal 1-1 Dortmund. Coupe Davis : Italie vs Coree en cours apres Musetti."),
    # Spanish
    ("Sabah 0-1 Barcelona descanso", "miercoles UCL por publicar"),
    ("Mierc desc: Sabah 0-1 Barcelona.", "Miercoles UCL sin publicar."),
    ("Sabah 0-1 Barcelona al descanso.", "Arsenal 1-1 Dortmund y Man City 2-2 Napoles."),
    ("Sabah 0-1 Barcelona al descanso. Copa Davis en directo: Italia 1-0 Corea del Sur.", "Arsenal 1-1 Dortmund. Copa Davis: Italia vs Corea abierto tras triunfo de Musetti."),
    # German
    ("Sabah 0:1 Barcelona HZ", "Mittwoch-Spiele offen"),
    ("Mi HZ: Sabah 0:1 Barcelona.", "Mittwoch noch offen."),
    ("Sabah 0:1 Barcelona zur Pause.", "Arsenal 1:1 Dortmund und Man City 2:2 Napoli."),
    ("Sabah 0:1 Barcelona zur Pause. Davis Cup live: Italien 1:0 Suedkorea.", "Arsenal 1:1 Dortmund. Davis Cup: Italien gegen Suedkorea nach Musetti offen."),
    # Italian
    ("Sabah 0-1 Barcellona int.", "mercoledi UCL da completare"),
    ("Mer int: Sabah 0-1 Barcellona.", "Mercoledi non ancora chiuso."),
    ("Sabah 0-1 Barcellona all'intervallo.", "Arsenal 1-1 Dortmund e Man City 2-2 Napoli."),
    ("Sabah 0-1 Barcellona all'intervallo. Coppa Davis live: Italia 1-0 Corea.", "Arsenal 1-1 Dortmund. Coppa Davis: Italia-Corea aperta dopo Musetti."),
    # Polish
    ("Sabah 0:1 Barcelona HT", "sroda w toku"),
    ("Sr HT: Sabah 0:1 Barcelona.", "Srodowe mecze jeszcze nieopublikowane."),
    ("Sabah 0:1 Barcelona do przerwy.", "Arsenal 1:1 Dortmund oraz Man City 2:2 Napoli."),
    ("Sabah 0:1 Barcelona do przerwy. Puchar Davisa: Wlochy 1:0 Korea Pld.", "Arsenal 1:1 Dortmund. Puchar Davisa: Wlochy-Korea otwarte po Musettim."),
    # Chinese
    ("，萨巴赫0-1巴萨半场", "，周三赛果待定"),
    ("周三半场：萨巴赫0-1巴萨。", "周三欧冠赛果未公布。"),
    ("；周三半场萨巴赫0-1巴塞罗那。", "；阿森纳1-1战平多特蒙德。"),
    ("，巴萨半场领先。戴维斯杯意大利1-0领先韩国。", "，阿森纳1-1多特。戴维斯杯意大利在穆塞蒂取胜后仍与韩国激战中。"),
    # Japanese
    ("、サバフ0-1バルサHT", "、水曜未定"),
    ("水曜HT：サバフ0-1バルサ。", "水曜分は未確定。"),
    ("；サバフ0-1バルセロナ前半終了。", "；アーセナル1-1ドルトムント、マンC 2-2ナポリ。"),
    ("、バルサ前半リード。デビス杯：イタリア1-0韓国。", "、アーセナル1-1ドルトムント。デビス杯はムゼッティ先勝後イタリア対韓国続行中。"),
    # Korean
    (", 사바흐 0-1 바르사 전반", ", 수요일 결과 미발표"),
    ("수 전반: 사바흐 0-1 바르사.", "수요일 경기 미발표."),
    ("; 사바흐 0-1 바르셀로나 전반 종료.", "; 아스널 1-1 도르트문트, 맨시티 2-2 나폴리."),
    (", 바르사 전반 리드. 데이비스컵: 이탈리아 1-0 한국.", ", 아스널 1-1 도르트문트. 데이비스컵 무세티 승리 후 이탈리아-한국 진행 중."),
    # Arabic
    ("، برشلونة متقدم", "، ومباريات الاربعاء قيد الانتظار"),
    ("الاربعاء: برشلونة متقدم 1-0.", "مباريات الاربعاء غير منشورة بعد."),
    ("؛ صباح 0-1 برشلونة بين الشوطين.", "؛ ارسنال 1-1 دورتموند وسيتي 2-2 نابولي."),
    ("وبرشلونة متقدم. كاس ديفيز: ايطاليا 1-0 كوريا.", "وارسنال 1-1 دورتموند. كاس ديفيز: مواجهة ايطاليا وكوريا مفتوحة بعد فوز موسيتي."),
]

for fn in ["messages.ts"] + [f"messages-{loc}.ts" for loc in ["es", "de", "it", "pl", "zh", "ja", "ko", "ar"]]:
    patch_file(f"frontend/src/i18n/{fn}", msg_reps)

# 3. Also patch F1 Qatar story & Las Vegas mentions in f1-qatar-gp MD and stories.ts to match official Vegas timing (Antonelli P4, Russell P9)
f1_story_path = os.path.join(ROOT, "frontend/src/content/stories/f1-qatar-gp-lusail-preview-verstappen-vegas-triumph-norris-battle-2026.md")
f1_txt = open(f1_story_path, "r", encoding="utf-8").read()
f1_old = "late chaos eliminated both factory Mercedes challengers: George Russell hit the barrier on Lap 48 (finishing 9th) and champion Kimi Antonelli suffered a sudden power loss while fighting up front."
f1_new = "champion Kimi Antonelli took 4th (+2.574s) while George Russell brushed the wall late and recovered to finish 9th (+13.192s)."
if f1_old in f1_txt:
    f1_txt = f1_txt.replace(f1_old, f1_new)
    open(f1_story_path, "w", encoding="utf-8").write(f1_txt)
    print("Harmonized F1 Qatar story.md with official Vegas timing")

# 4. Make sure Davis Cup story + json have exact consistency on Italy vs Korea open tie
dc_json_path = os.path.join(ROOT, "frontend/src/content/matches/davis-cup-finals-2026-bologna-knockout.json")
dc_data = json.load(open(dc_json_path, "r", encoding="utf-8"))
if dc_data.get("status") == "UPCOMING":
    dc_data["status"] = "LIVE"
    dc_data["homeScore"] = "1"
    dc_data["awayScore"] = "0"
    dc_data["liveMinute"] = "Rubber 2"
    open(dc_json_path, "w", encoding="utf-8").write(json.dumps(dc_data, ensure_ascii=False, indent=2) + "\n")
    print("Ensured Davis Cup match JSON status=LIVE")

print("Harmonization complete.")

