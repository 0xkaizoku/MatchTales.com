# -*- coding: utf-8 -*-
import json
import re

OCT30_STORIES = {
    "carabao-cup-2026-quarter-final-draw-fleetwood-town-draws-newcastle": {
        "fr": {
            "title": "Tirage des quarts de Carabao Cup : Fleetwood Town herite d'un duel de reve contre Newcastle a Highbury",
            "subtitle": "Le club de D4 recevra les Magpies tandis que Man City accueillera Brentford et que Liverpool ira a Selhurst Park.",
            "excerpt": "Le conte de fees de Fleetwood Town en Coupe de la Ligue se poursuit avec la reception de Newcastle United en quarts de finale.",
            "body": [
                "La magie des coupes anglaises a offert un nouveau moment savoureux ce jeudi 29 octobre lors du tirage au sort des quarts de finale de la Carabao Cup. Apres avoir sorti Arsenal aux tirs au but, le petit poucet de quatrieme division Fleetwood Town accueillera le cador Newcastle United a Highbury Stadium a la mi-decembre dans une ambiance qui s'annonce electrique.",
                "Dans les autres affiches de ces quarts de finale, Manchester City recevra Brentford a l'Etihad Stadium tandis que Liverpool se deplacera a Londres pour defier Crystal Palace a Selhurst Park. Tottenham Hotspur accueillera de son cote Southampton. En attendant ce rendez-vous hivernal, toute l'Angleterre a les yeux rives sur le choc de Premier League entre Arsenal et Liverpool ce samedi a l'Emirates Stadium."
            ]
        },
        "es": {
            "title": "Sorteo de cuartos de la Copa de la Liga: El modesto Fleetwood Town recibe al Newcastle en Highbury",
            "subtitle": "El conjunto de cuarta division acoge a las Urracas mientras el Manchester City recibe al Brentford y Liverpool visita al Crystal Palace.",
            "excerpt": "El sueno de Fleetwood Town en la Carabao Cup continua tras quedar emparejado en casa ante el Newcastle United.",
            "body": [
                "El sorteo de los cuartos de final de la Carabao Cup celebrado el jueves 29 de octubre deparo un emparejamiento sonado: el modesto Fleetwood Town, verdugo del Arsenal en los penaltis, recibira en su estadio de Highbury al poderoso Newcastle United a mediados de diciembre.",
                "Los demas favoritos evitaron cruzarse entre si: el Manchester City se medira al Brentford en el Etihad Stadium y el Liverpool viajara a Londres para medirse al Crystal Palace. Tottenham y Southampton completan el cuadro. Mientras tanto, el foco competitivo se traslada de inmediato al apasionante duelo de Premier League entre Arsenal y Liverpool este sabado en el Emirates."
            ]
        },
        "de": {
            "title": "Carabao Cup Viertelfinal-Auslosung: Viertligist Fleetwood Town empfaengt Newcastle im Highbury Stadium",
            "subtitle": "Der Sensationsteam trifft auf die Magpies; Man City fordert Brentford und Liverpool gastiert bei Crystal Palace.",
            "excerpt": "Das Maerchen von Fleetwood Town im englischen Ligapokal geht weiter: Im Viertelfinale wartet ein Traumlos gegen Newcastle United.",
            "body": [
                "Die Auslosung des Carabao Cup Viertelfinales am Donnerstag, den 29. Oktober, bescherte dem englischen Fussball ein echtes Pokal-Highlight. Der viertklassige Außenseiter Fleetwood Town, der am Dienstag sensationell Arsenal im Elfmeterschießen eliminierte, empfaengt Mitte Dezember den Champions-League-Klub Newcastle United an der windigen Kueste von Lancashire.",
                "In den weiteren Begegnungen empfaengt Manchester City den FC Brentford im Etihad Stadium, waehrend Liverpool bei Crystal Palace in London antritt. Die Tottenham Hotspur komplettieren das Feld im Duell gegen Southampton. Vor dem Ligapokal-Showdown im Dezember richtet sich der Blick auf das Topspiel der Premier League am Samstag zwischen Arsenal und Liverpool."
            ]
        },
        "it": {
            "title": "Sorteggio quarti di Carabao Cup: Il favoloso Fleetwood Town pesca il Newcastle a Highbury",
            "subtitle": "La matricola di quarta serie affrontera i Magpies in casa; Man City contro Brentford e Liverpool sul campo del Crystal Palace.",
            "excerpt": "La splendida favola del Fleetwood Town prosegue nei quarti di Coppa di Lega con l'affascinante sfida casalinga al Newcastle United.",
            "body": [
                "Il fascino della Coppa di Lega inglese si rinnova con il sorteggio dei quarti di finale andato in scena giovedi 29 ottobre. Il piccolo Fleetwood Town, club di League Two capace di estromettere l'Arsenal dal dischetto martedi sera, ospitera la corazzata Newcastle United tra le mura amiche di Highbury Stadium a meta dicembre.",
                "Nessun incrocio diretto tra le altre big: il Manchester City se la vedra all'Etihad Stadium contro il Brentford, mentre il Liverpool sara impegnato nella capitale sul terreno del Crystal Palace. Il Tottenham ospitera il Southampton. Prima della coppa, la Premier League propone sabato la supersfida d'alta quota tra Arsenal e Liverpool all'Emirates Stadium."
            ]
        },
        "pl": {
            "title": "Losowanie cwiercfinalow Pucharu Ligi: Czwartoligowe Fleetwood Town podejmie Newcastle na Highbury",
            "subtitle": "Kopciuszek zagra z Magpies na wlasnym boisku; Man City zmierzy sie z Brentford, a Liverpool zagra z Crystal Palace.",
            "excerpt": "Pucharowy sen Fleetwood Town trwa w najlepsze: czwartoligowiec wylosowal Newcastle United w 1/4 finalu Carabao Cup.",
            "body": [
                "W czwartek 29 pazdziernika rozlosowano pary cwiercfinalowe Carabao Cup, przynoszac wspaniala wiadomosc dla kibicow Fleetwood Town. Po wyeliminowaniu Arsenalu w serii rzutow karnych, druzyna z League Two podejmie w polowie grudnia na Highbury Stadium ekipe Newcastle United.",
                "Faworyci turnieju unikneli bezposrednich starc: Manchester City podejmie u siebie Brentford, a Liverpool uda sie do Londynu na mecz z Crystal Palace. Tottenham zmierzy sie z Southampton. W ten weekend cala uwaga kibicow przenosi sie na sobotni hit Premier League na Emirates Stadium pomiedzy Arsenalem i Liverpoolem."
            ]
        },
        "zh": {
            "title": "英格兰联赛杯八强抽签揭晓：第四级别黑马弗利特伍德主场战纽卡，曼城碰布伦特福德",
            "subtitle": "淘汰阿森纳的海滨弱旅将在海布里球场迎战喜鹊军团；利物浦客战水晶宫，热刺对阵南安普顿。",
            "excerpt": "英乙黑马弗利特伍德的联赛杯童话继续上演，周四抽签中他们抽中主场对阵纽卡斯尔联的梦幻签位。",
            "body": [
                "10月29日周四进行的英格兰联赛杯四分之一决赛抽签再次点燃了球迷的激情。在点球大战淘汰阿森纳制造惊天冷门后，第四级别球队弗利特伍德将在12月中旬坐镇海布里球场迎战英超劲旅纽卡斯尔联，为海滨小城带来又一个梦幻杯赛之夜。",
                "其他传统豪门在八强战中成功避开彼此：曼城将在伊蒂哈德球场迎战布伦特福德，利物浦做客挑战水晶宫，托特纳姆热刺则在主场迎战南安普顿。与此英超第9轮焦点大战本周六将在酋长球场打响，阿森纳与利物浦展开强强对话。"
            ]
        },
        "ja": {
            "title": "カラバオ杯8強組み合わせ決定：4部フリートウッドが本拠地で名門ニューカッスルを迎え撃つ",
            "subtitle": "快進撃を続ける下位クラブが歓喜のドロー；マンCはブレントフォード、リヴァプールはパレスと対戦。",
            "excerpt": "アーセナルを破った英4部フリートウッド・タウンの夢は続き、準々決勝でニューカッスルとのホームゲームが決定した。",
            "body": [
                "10月29日木曜日に行われたカラバオ杯準々決勝の組み合わせ抽選会で、サッカーファンを魅了するカードが決まった。火曜日にアーセナルをPK戦で破る大番狂わせを演じた4部リーグ2のフリートウッド・タウンが、12月中旬に本拠地ハイバリー・スタジアムで強豪ニューカッスル・ユナイテッドを迎え撃つ。",
                "優勝候補のマンチェスター・シティはブレントフォードとホームで対戦し、リヴァプールはロンドンでクリスタル・パレスと激突する。今週末はプレミアリーグ第9輪の首位攻防戦として、アーセナル対リヴァプールのビッグマッチが控えている。"
            ]
        },
        "ko": {
            "title": "카라바오컵 8강 대진 추첨 결과: 4부 플리트우드 타운, 안방서 뉴캐슬과 맞대결 성사",
            "subtitle": "아스널 꺾은 돌풍의 팀 홈경기 배정; 맨시티는 브렌트퍼드와 격돌, 리버풀은 팰리스 원정길.",
            "excerpt": "아스널을 침몰시킨 4부 플리트우드 타운이 카라바오컵 8강에서 뉴캐슬 유나이티드를 홈으로 불러들인다.",
            "body": [
                "10월 29일 목요일 진행된 2026-27 카라바오컵 8강 대진 추첨에서 낭만적인 대진이 완성됐다. 주중 경기에서 프리미어리그 선두 아스널을 승부차기로 꺾고 파란을 일으킨 4부 리그의 플리트우드 타운이 12월 중순 하이버리 스타디움에서 뉴캐슬 유나이티드와 준결승 진출을 다툰다.",
                "맨체스터 시티는 안방에서 브렌트퍼드를 상대하며, 리버풀은 런던 셀허스트 파크에서 크리스털 팰리스와 격돌한다. 토트넘은 사우샘프턴을 홈으로 불러들인다. 한편 이번 주말에는 프리미어리그 9라운드 아스널과 리버풀의 에미레이츠 스타디움 맞대결이 기다리고 있다."
            ]
        },
        "ar": {
            "title": "قرعة ربع نهائي كأس الرابطة: فليتوود تاون يحصل على مواجهة الحلم أمام نيوكاسل في هايبوري",
            "subtitle": "فريق الدرجة الرابعة يستضيف نيوكاسل بينما يلتقي مانشستر سيتي مع برينتفورد وليفربول مع كريستال بالاس.",
            "excerpt": "تتواصل رحلة فليتوود تاون الخيالية في كأس الرابطة بعد أن أوقعته قرعة ربع النهائي في مواجهة نيوكاسل يونايتد.",
            "body": [
                "عاشت جماهير كرة القدم الإنجليزية إثارة جديدة يوم الخميس 29 أكتوبر مع الإعلان عن قرعة الدور ربع النهائي لبطولة كأس الرابطة. وسيكون ملعب هايبوري الساحلي الصغير شاهدا على استضافة فليتوود تاون، قاهر أرسنال، لفريق نيوكاسل يونايتد العريق في منتصف شهر ديسمبر المقبل.",
                "وفي باقي المواجهات يلعب مانشستر سيتي على أرضه ضد برينتفورد، بينما يحل ليفربول ضيفا على كريستال بالاس في لندن، ويلتقي توتنهام مع ساوثهامبتون. وتتحول الأنظار فورا إلى قمة الجولة التاسعة من الدوري الإنجليزي الممتاز يوم السبت بين أرسنال وليفربول على ملعب الإمارات."
            ]
        }
    },

    "wnba-finals-2026-game6-valkyries-crowned-champions-expansion-miracle": {
        "fr": {
            "title": "Finales WNBA match 6 : Les Valkyries triomphent d'Atlanta 76-71 et s'offrent un titre historique",
            "subtitle": "L'equipe d'expansion boucle la plus belle saison inaugurale du sport moderne ; Gabby Williams elue MVP des Finales (4-2).",
            "excerpt": "Les Golden State Valkyries sont championnes WNBA des leur premiere annee apres leur victoire 76-71 sur le parquet du Dream jeudi soir.",
            "body": [
                "L'histoire du sport professionnel nord-americain a ete bouleversee ce jeudi 29 octobre au Gateway Center Arena d'Atlanta. En s'imposant 76-71 lors du match 6 des Finales WNBA face au Dream, les Golden State Valkyries ont decroche le titre mondial des leur saison inaugurale (4-2), une premiere dans les ligues majeures americaines depuis 1950.",
                "Menant l'equipe avec autorite, Gabby Williams a ete elue a l'unanimite MVP des Finales apres avoir inscrit 21 points accompagnes de 6 rebonds et 4 interceptions. Kayla Thornton a scelle le destin du match d'un tir a trois points meurtrier a 24 secondes de la sirene, brisant le coeur d'Angel Reese (16 points, 15 rebonds) et des supporters georgiens."
            ]
        },
        "es": {
            "title": "Finales WNBA Partido 6: Valkyries vencen 76-71 al Dream y logran un campeonato historico",
            "subtitle": "La franquicia de expansion culmina la mejor temporada de debut del deporte moderno; Gabby Williams nombrada MVP de las Finales.",
            "excerpt": "Las Golden State Valkyries se proclaman campeonas de la WNBA en su temporada de estreno tras batir 76-71 a Atlanta en el Partido 6.",
            "body": [
                "Las Golden State Valkyries tocaron el cielo este jueves 29 de octubre en el Gateway Center Arena de College Park al derrotar 76-71 al Atlanta Dream en el sexto asalto de las Finales, llevandose el titulo por un global de 4-2. El conjunto californiano se convierte en el primer equipo de expansion en ganar una gran liga estadounidense en su primer ano de existencia desde 1950.",
                "Gabby Williams se alzo de forma unanime con el premio de MVP de las Finales al firmar 21 puntos y 4 robos en el partido decisive. Un triple historico de Kayla Thornton desde la esquina a falta de 24 segundos rompio el empate a 71 y desato la locura en el banquillo visitante, dejando sin recompensa el partidazo de Angel Reese (16 puntos, 15 rebotes)."
            ]
        },
        "de": {
            "title": "WNBA Finals Spiel 6: Valkyries kroenen Maerchensaison mit 76:71-Triumph ueber das Dream",
            "subtitle": "Erstes Expansion-Team seit 1950 mit Meisterschaft im Premierenjahr; Gabby Williams fuehrt Golden State als Finals-MVP zum 4:2-Titel.",
            "excerpt": "Die Golden State Valkyries schreiben Sportgeschichte und gewinnen als Neuling durch ein 76:71 in Atlanta die WNBA-Meisterschaft 2026.",
            "body": [
                "Die Golden State Valkyries vollbrachten am Donnerstagabend, den 29. Oktober, das groesste Sportwunder der Neuzeit: Mit einem packenden 76:71-Erfolg in Spiel 6 der WNBA Finals gegen das Atlanta Dream kroente sich das neue Franchise aus San Francisco mit 4:2 Siegen auf Anhieb zum WNBA-Champion 2026.",
                "Finals-MVP Gabby Williams ueberragte in der entscheidenden Schlacht mit 21 Punkten und vier Steals. Als die Partie beim Stand von 71:71 auf des Messers Schneide stand, versenkte Kayla Thornton 24 Sekunden vor Schluss einen eiskalten Dreier aus der Ecke zum Sieg, waehrend Atlanta trotz 16 Punkten und 15 Rebounds von Angel Reese geschlagen vom Parkett ging."
            ]
        },
        "it": {
            "title": "Finali WNBA Gara 6: Valkyries campionesse, superata Atlanta 76-71 per un'impresa da leggenda",
            "subtitle": "La matricola di Golden State firma la piu grande stagione d'esordio della storia dello sport; Gabby Williams MVP delle Finali.",
            "excerpt": "Le Golden State Valkyries conquistano il titolo WNBA al loro primissimo anno di vita grazie al trionfo 76-71 in Gara 6.",
            "body": [
                "Un trionfo senza precedenti ha riscritto la storia della pallacanestro americana giovedi 29 ottobre alla Gateway Center Arena. Le Golden State Valkyries hanno sconfitto le Atlanta Dream per 76-71 in Gara 6, chiudendo la serie sul 4-2 e diventando la prima franchigia d'espansione a vincere il titolo al debutto assoluto dal 1950.",
                "Gabby Williams e stata votata all'unanimita MVP delle Finali dopo aver totalizzato 21 punti e 4 recuperi nel match decisivo. La tripla dall'angolo di Kayla Thornton a 24 secondi dalla sirena ha spezzato la parita sul 71-71, regalando la gloria alle californiane nonostante i 16 punti e 15 rimbalzi messi a segno da Angel Reese."
            ]
        },
        "pl": {
            "title": "Finaly WNBA mecz 6: Valkyries pokonuja Dream 76:71 i siegaja po historyczne mistrzostwo w debiucie",
            "subtitle": "Zespol z San Francisco pierwszym debiutantem z tytulem od 1950 roku; Gabby Williams MVP Finalow po wygranej 4-2 w serii.",
            "excerpt": "Golden State Valkyries zostaly mistrzyniami WNBA 2026, wygrywajac w czwartek szosty mecz w Atlancie 76:71.",
            "body": [
                "To, co wydawalo sie niemozliwe, stalo sie faktem w czwartek 29 pazdziernika w hali Gateway Center Arena. Golden State Valkyries pokonaly Atlanta Dream 76:71 w meczu numer 6 i wygraly serie finalowa 4-2, stajac sie pierwszym zespolem w historii glownych lig amerykanskich od 1950 roku, ktory zdobyl tytul mistrzowski w swoim debiutanckim sezonie.",
                "Finals MVP Gabby Williams poprowadzila druzyne do triumfu z 21 punktami i 4 przechwytami na koncie. Decydujacy cios zadala Kayla Thornton, trafiajac za trzy punkty z rogu boiska na 24 sekundy przed koncem przy stanie 71:71, co zniweczylo heroiczna postawe Angel Reese (16 punktow, 15 zbiorek)."
            ]
        },
        "zh": {
            "title": "WNBA总决赛G6：金州女武神76-71力克梦想大比分4-2夺冠，书写扩军球队历史奇迹",
            "subtitle": "成军首年即加冕总冠军创现代职业体育神迹；加比·威廉姆斯荣膺总决赛MVP。",
            "excerpt": "金州女武神在周四晚间的总决赛第六场以76-71击败亚特兰大梦想，建队首年便奇迹般捧得WNBA总冠军奖杯。",
            "body": [
                "北美四大职业体育近76年来的最大奇迹在10月29日周四晚正式诞生。在佐治亚州进行的WNBA总决赛第六场决战中，建队仅半年的新军金州女武神以76-71客场力克亚特兰大梦想，总比分4-2夺得2026年WNBA总冠军，成为自1950年明尼阿波利斯湖人之后首支夺冠的扩建新军。",
                "核心加比·威廉姆斯在生死时刻独揽21分、6个篮板和4次抢断，毫无争议地全票当选总决赛MVP。在终场前24.1秒两队战成71平的关键时刻，老将凯拉·桑顿接球后命中制胜底角三分，粉碎了安吉尔·里斯（16分15篮板）率领梦想队翻盘的希望。"
            ]
        },
        "ja": {
            "title": "WNBAファイナル第6戦：ヴァルキリーズがドリームを76-71で撃破、創設初年度の歴史的初制覇",
            "subtitle": "1950年以来となるエクスパンション初年度での完全優勝；ギャビー・ウィリアムズが満票でファイナルMVP獲得。",
            "excerpt": "ゴールデンステイト・ヴァルキリーズが敵地アトランタで76-71の激戦を制し、4勝2敗で球団創設初年度でのWNBA制覇を達成した。",
            "body": [
                "10月29日木曜日、北米プロスポーツ界に歴史的な金字塔が打ち立てられた。ゴールデンステイト・ヴァルキリーズがWNBAファイナル第6戦でアトランタ・ドリームを76-71で下し、シリーズ4勝2敗で2026年シーズンの王座に就いた。初年度の新規参入チームが主要プロリーグを制するのは1950年以来76年ぶりの快挙となった。",
                "シリーズを通じて獅子奮迅の活躍を見せたギャビー・ウィリアムズが21得点4スティールを記録し、満票でファイナルMVPに選出。同点で迎えた残り24秒にケイラ・ソーントンが劇的な決勝3ポイントシュートを沈め、エンジェル・リースの奮闘（16得点15リバウンド）を退けた。"
            ]
        },
        "ko": {
            "title": "WNBA 파이널 6차전: 발키리스, 드림 76-71 꺾고 창단 첫해 기적의 챔피언 등극",
            "subtitle": "1950년 이후 메이저 프로 스포츠 사상 최초 창단 원년 우승 신화; 개비 윌리엄스 파이널 MVP 선정.",
            "excerpt": "골든스테이트 발키리스가 목요일 밤 애틀랜타 원정 6차전서 76-71로 승리하며 시리즈 4-2로 2026 WNBA 우승 트로피를 들어 올렸다.",
            "body": [
                "현대 미국 프로 스포츠 역사상 가장 경이로운 드라마가 10월 29일 목요일 조지아주 게이트웨이 센터 아레나에서 완성됐다. 창단 첫 시즌을 맞이한 골든스테이트 발키리스가 애틀랜타 드림을 76-71로 제압하고 시리즈 전적 4승 2패로 대망의 WNBA 챔피언에 등극했다.",
                "공수 양면에서 21점 4스틸을 기록한 개비 윌리엄스가 만장일치로 파이널 MVP의 영예를 안았다. 경기 종료 24초 전 71-71 동점 상황에서 케일라 손튼이 터뜨린 회심의 코너 3점포가 승부를 갈랐고, 16점 15리바운드로 분전한 엔젤 리스의 애틀랜타는 아쉽게 고개를 숙였다."
            ]
        },
        "ar": {
            "title": "نهائي دوري WNBA المباراة 6: فالكيريز يهزم دريم 76-71 ويتوج بلقب تاريخي في موسمه الأول",
            "subtitle": "أول فريق صاعد يتوج باللقب في عامه الأول منذ 1950؛ غابي ويليامز تحصد جائزة أفضل لاعبة في النهائي.",
            "excerpt": "كتبت سيدات غولدن ستيت فالكيريز التاريخ يوم الخميس وتوجن بلقب دوري WNBA بالفوز في المباراة السادسة على أتلانتا دريم.",
            "body": [
                "شهدت صالة غيتواي سنتر أرينا يوم الخميس 29 أكتوبر إنجازا تاريخيا غير مسبوق في الرياضة الأمريكية الحديثة. فقد توج فريق غولدن ستيت فالكيريز بلقب دوري كرة السلة النسائي WNBA في أول موسم له في المسابقة، عقب فوزه المثير على أتلانتا دريم 76-71 ليحسم السلسلة بنتيجة 4-2.",
                "وحصدت النجمة غابي ويليامز جائزة أفضل لاعبة في النهائي بإجماع الآراء بعد تسجيلها 21 نقطة و4 قطوع للكرة في المباراة الحاسمة. وسجلت كايلا ثورنتون ثلاثية قاتلة قبل 24 ثانية من النهاية لكسر التعادل 71-71، وسط حسرة كبيرة للنجمة أنجيل ريس التي تألقت بـ 16 نقطة و15 متابعة."
            ]
        }
    },

    "nfl-week8-packers-beat-panthers-27-17-tnf-lambeau-2026": {
        "fr": {
            "title": "NFL Semaine 8 TNF : Les Packers dominent Carolina 27-17, Jordan Love porte Green Bay a 6-2",
            "subtitle": "Josh Jacobs accumule 94 yards et la defense de Green Bay signe quatre sacks pour rester au contact des Vikings invaincus.",
            "excerpt": "Green Bay a fait respecter la hierarchie sous les projecteurs de Lambeau Field jeudi en dominant les Panthers 27-17.",
            "body": [
                "Les Green Bay Packers ont ouvert la 8e semaine de NFL de maniere autoritaire ce jeudi 29 octobre en dominant les Carolina Panthers 27-17 devant 77 844 supporters geles a Lambeau Field. Ce succes permet aux Packers de porter leur bilan a 6-2 et de maintenir la pression sur les Vikings de Minnesota (6-0) en tete de la division NFC Nord.",
                "Le quart-arriere Jordan Love a rendu une copie tres propre avec 20 passes reussies sur 28 pour 245 yards et deux passes de touchdown sans perte de balle. En defense, Rashan Gary a martyrise la poche adverse avec deux sacks, etouffant toute tentative de retour de Bryce Young dans le dernier quart-temps."
            ]
        },
        "es": {
            "title": "NFL Semana 8 TNF: Packers doblegan 27-17 a Panthers con Jordan Love llevando a Green Bay a 6-2",
            "subtitle": "Josh Jacobs corre para 94 yardas y Gary comanda la defensa con dos capturas para presionar a los invictos Vikings.",
            "excerpt": "Green Bay cumplio el pronostico en el gelido Lambeau Field este jueves noche al vencer 27-17 a Carolina.",
            "body": [
                "Los Green Bay Packers abrieron la Semana 8 de la NFL con paso firme este jueves 29 de octubre al superar 27-17 a los Carolina Panthers ante 77.844 espectadores en Lambeau Field. La victoria eleva a Green Bay a una marca de 6-2 en la temporada, manteniendo la persecucion sobre los invictos Minnesota Vikings (6-0) en la NFC Norte.",
                "Jordan Love firmo otra actuacion dominante con 245 yardas de pase y dos envios de anotacion sin intercepciones, mientras Josh Jacobs castigo por tierra con 94 yardas y un touchdown. En el costado defensivo, Rashan Gary lidero una linea demoledora que capturo cuatro veces a Bryce Young."
            ]
        },
        "de": {
            "title": "NFL Woche 8 TNF: Packers schlagen Panthers 27:17, Jordan Love fuehrt Green Bay auf 6:2",
            "subtitle": "Josh Jacobs erlaeuft 94 Yards und Gary steuert zwei Sacks bei; Packers bleiben ungeschlagenen Vikings auf den Fersen.",
            "excerpt": "Green Bay gab sich im frostigen Lambeau Field am Donnerstagabend keine Bloesse und bezwang die Carolina Panthers mit 27:17.",
            "body": [
                "Die Green Bay Packers eroeffneten die achte Spielwoche der NFL am Donnerstagabend, den 29. Oktober, mit einem souveraenen 27:17-Erfolg ueber die Carolina Panthers vor 77.844 Zuschauern im eiskalten Lambeau Field. Damit verbessert sich das Team von Trainer Matt LaFleur auf eine 6:2-Bilanz und haelt den Druck auf die ungeschlagenen Minnesota Vikings (6:0) aufrecht.",
                "Quarterback Jordan Love ueberzeugte mit 20 von 28 angekommenen Paessen fuer 245 Yards und zwei Touchdowns ohne Ballverlust. Running Back Josh Jacobs sorgte mit 94 Rushing-Yards fuer Durchschlagskraft am Boden, waehrend die Abwehr um Rashan Gary Spielmacher Bryce Young viermal zu Boden brachte."
            ]
        },
        "it": {
            "title": "NFL Week 8 TNF: I Packers battono i Panthers 27-17, Jordan Love porta Green Bay sul 6-2",
            "subtitle": "Josh Jacobs corre per 94 yard e la difesa piazza quattro sack per restare a ridosso dei Minnesota Vikings.",
            "excerpt": "Vittoria convincente dei Green Bay Packers nella notte gelida di Lambeau Field giovedi superando 27-17 Carolina.",
            "body": [
                "I Green Bay Packers hanno inaugurato l'ottava giornata della NFL giovedi 29 ottobre superando i Carolina Panthers per 27-17 davanti ai 77.844 calorosi tifosi del Lambeau Field. Il successo consolida il secondo posto dei Packers nella NFC North sul 6-2 alle spalle dei perfetti Minnesota Vikings (6-0).",
                "Ottima prestazione per Jordan Love, autore di 245 yard su passaggio e due touchdown senza alcun intercetto. Il running back Josh Jacobs ha macinato 94 yard e una marcatura su corsa, mentre la difesa orchestrata da Jeff Hafley ha atterrato per quattro volte il quarterback ospite Bryce Young."
            ]
        },
        "pl": {
            "title": "NFL Tydzien 8 TNF: Packers pokonuja Panthers 27:17, Jordan Love prowadzi Green Bay do bilansu 6-2",
            "subtitle": "Josh Jacobs zdobywa 94 jardy biegiem, a obrona zatrzymuje Bryce'a Younga w poscigu za niepokonanymi Vikings.",
            "excerpt": "Green Bay zrobilo swoje w czwartkowy wieczor na Lambeau Field, pewnie wygrywajac z Carolina Panthers 27:17.",
            "body": [
                "Green Bay Packers udanie zainaugurowali osmy tydzien rozgrywek NFL w czwartek 29 pazdziernika, pokonujac Carolina Panthers 27:17 w mroznej scenerii Lambeau Field w obecnosci 77 844 kibicow. Zwyciestwo poprawilo bilans ekipy z Wisconsin do 6-2, pozwalajac zachowac dystans do liderujacych w dywizji Minnesota Vikings (6-0).",
                "Jordan Love zagral niezwykle dojrzale, notujac 245 jardow podaniowych i dwa przylozenia bez straty pilki. Josh Jacobs dodal 94 jardy po ziemi i zdobył przylozenie, zas defensywa kierowana przez Rashana Gary'ego zanotowala cztery sacki na Bryce'u Youngu."
            ]
        },
        "zh": {
            "title": "NFL第8周周四夜赛：包装工27-17战胜黑豹，乔丹·爱芙率队拿下第6胜紧逼维京人",
            "subtitle": "雅各布斯狂揽94码并达阵，加里奉献两记擒杀封锁布莱斯·杨，绿湾战绩提升至6胜2负。",
            "excerpt": "绿湾包装工在周四晚间的兰博球场冰冷秋风中发挥稳定，以27-17击溃卡罗来纳黑豹保住国联北区争冠希望。",
            "body": [
                "10月29日周四晚，NFL第8周常规赛在兰博球场拉开大幕。在77844名主场球迷的助威声中，绿湾包装工凭借攻防两端的全面统治力以27-17击败卡罗来纳黑豹，将赛季总战绩提升至6胜2负，继续紧咬6战全胜的明尼苏达维京人。",
                "四分卫乔丹·爱芙全场表现沉稳，28传20中贡献245码和2次达阵且零失误。跑卫乔希·雅各布斯冲球94码并打入首开纪录的达阵，防守端拉珊·加里领衔的突前防线完成4次擒杀，令黑豹四分卫布莱斯·杨毫无反扑空间。"
            ]
        },
        "ja": {
            "title": "NFL第8週TNF：パッカーズがパンサーズを27-17で下し6勝目、首位追撃へ",
            "subtitle": "ジョーダン・ラヴが2TDパス、ジェイコブズが94ヤード獲得で凍てつくランボー・フィールドを制す。",
            "excerpt": "グリーンベイ・パッカーズが木曜夜のランボー・フィールドでパンサーズを27-17で退け、6勝2敗と星を伸ばした。",
            "body": [
                "10月29日木曜日、凍てつくウィスコンシンの名門ランボー・フィールドに集まった7万7844人の観衆の前で、グリーンベイ・パッカーズがカロライナ・パンサーズに27-17で快勝した。この白星でパッカーズは6勝2敗となり、NFC北地区首位を走る無敗のミネソタ・バイキングス（6勝0敗）を射程圏内に捉え続けている。",
                "QBジョーダン・ラヴはパス28本中20本成功、245ヤード、2TD、無インターセプトと安定した試合運びを展開。RBジョシュ・ジェイコブズが94ヤードと1TDを奪い、ラシャーン・ゲイリーらの守備陣がパンサーズのQBブライス・ヤングを4サックで封じ込めた。"
            ]
        },
        "ko": {
            "title": "NFL 8주차 TNF: 패커스, 램보 필드서 팬서스 27-17 격파하며 6승 2패 질주",
            "subtitle": "조던 러브 2개 터치다운 패스 작렬; 조슈아 제이콥스 94야드 전진하며 무패 바이킹스 추격.",
            "excerpt": "그린베이 패커스가 목요일 밤 램보 필드의 매서운 추위 속에서 캐롤라이나 팬서스를 27-17로 누르고 6승째를 수확했다.",
            "body": [
                "그린베이 패커스가 10월 29일 목요일 밤 전설적인 램보 필드에서 열린 NFL 8주차 서스데이 나이트 풋볼 경기에서 캐롤라이나 팬서스를 27-17로 제압했다. 77,844명의 홈 관중 앞에서 승리를 거둔 패커스는 시즌 6승 2패를 기록하며 NFC 북부 선두 미네소타 바이킹스(6승 무패)를 턱밑까지 추격했다.",
                "쿼터백 조던 러브는 245야드 2터치다운을 기록하며 턴오버 없는 무결점 지휘를 선보였다. 러닝백 조슈아 제이콥스가 94야드 전진과 함께 터치다운을 찍었고, 수비진은 라샨 게리의 2개 색을 앞세워 캐롤라이나의 브라이스 영을 4차례 쓰러뜨렸다."
            ]
        },
        "ar": {
            "title": "دوري كرة القدم الأمريكية الأسبوع 8: باكرز يتفوق على بانثرز 27-17 في ليلة جليدية في لامبو فيلد",
            "subtitle": "جوردان لوف يسجل تمريرتي هبوط وجوش جاكوبس يركض لمسافة 94 ياردة ليرفع باكرز رصيده إلى 6-2.",
            "excerpt": "افتتح غرين باي باكرز مباريات الجولة الثامنة بفوز مستحق على كارولاينا بانثرز بنتيجة 27-17 مساء الخميس.",
            "body": [
                "استعرض غرين باي باكرز قوته مساء الخميس 29 أكتوبر في افتتاح الأسبوع الثامن من دوري NFL، محققا الفوز على ضيفه كارولاينا بانثرز 27-17 أمام نحو 78 ألف مشجع في ملعب لامبو فيلد الجليدي. ورفع باكرز سجله إلى 6 انتصارات مقابل هزيمتين لمواصلة ملاحقة مينيسوتا فايكنغز المتصدر بسجل خال من الهزائم (6-0).",
                "وقدم جوردان لوف مباراة رائعة بتمرير 245 ياردة وتمريرتي هبوط حاسمتين دون ارتكاب أي خطأ، بينما تولى جوش جاكوبس قيادة الهجوم الأرضي بـ 94 ياردة وهبوط مباشر. وفي الدفاع قاد راشان غاري الخط الأمامي بنجاح مسجلا إسقاطين للمنافس ليكبل حركة برايس يونغ."
            ]
        }
    },

    "atp-vienna-2026-alcaraz-downs-draper-reaches-semi-finals": {
        "fr": {
            "title": "ATP Vienne quarts de finale : Carlos Alcaraz maitrise Jack Draper et s'offre une demie royale face a Zverev",
            "subtitle": "Le no 2 mondial s'impose 6-4, 6-4 avec 29 coups gagnants ; Alexander Zverev domine Andrey Rublev dans l'autre quart.",
            "excerpt": "Carlos Alcaraz a livre une nouvelle demonstration de tennis en salle vendredi a Vienne, ecartant Jack Draper en deux sets.",
            "body": [
                "Carlos Alcaraz a franchi avec autorite l'obstacle des quarts de finale du tournoi de Vienne ce vendredi 30 octobre en s'imposant 6-4, 6-4 face au dangereux Britannique Jack Draper a la Wiener Stadthalle. Le joueur espagnol de 23 ans a impose un rythme effrene des les premiers echanges pour decrocher sa huitieme demi-finale de l'annee.",
                "Impressionnant de lucidite derriere sa premiere balle avec 81 pour cent de points gagnes et 29 coups gagnants, Alcaraz a converti les deux seules balles de break du match avec un sang-froid redoutable. Cette victoire prepare une demi-finale de gala ce samedi contre la tete de serie no 1 Alexander Zverev, tombeur d'Andrey Rublev en deux manches disputees (7-6, 6-4)."
            ]
        },
        "es": {
            "title": "ATP Viena cuartos de final: Carlos Alcaraz supera a Jack Draper y se cita en semifinales con Zverev",
            "subtitle": "El murciano vence 6-4, 6-4 con 29 golpes ganadores; Alexander Zverev se impone a Andrey Rublev en el Wiener Stadthalle.",
            "excerpt": "Carlos Alcaraz exhibio su mejor version bajo techo este viernes en Viena al batir al britanico Jack Draper en dos sets.",
            "body": [
                "Carlos Alcaraz continuo su camino triunfal en el Erste Bank Open de Viena este viernes 30 de octubre tras doblegar al britanico Jack Draper por 6-4 y 6-4 en la pista central del Wiener Stadthalle. Con un tenis preciso y agresivo, el pupilo espanol controlo el potente saque de zurda de su rival y cerro el pase a semifinales en 84 minutos.",
                "Alcaraz gano el 81 por ciento de los puntos jugados con su primer saque y sumo 29 golpes ganadores por apenas 11 errores no forzados. El sabado vivira un duelo estelar de semifinales ante el aleman Alexander Zverev, primer cabeza de serie, que derroto previamente a Andrey Rublev por 7-6 (4) y 6-4."
            ]
        },
        "de": {
            "title": "ATP Wien Viertelfinale: Carlos Alcaraz schlaegt Jack Draper 6:4, 6:4 und trifft auf Alexander Zverev",
            "subtitle": "Die Weltnummer 2 dominiert mit 29 Winnern; Zverev ringt Rublev im Tiebreak nieder vor dem Halbfinal-Klassiker.",
            "excerpt": "Carlos Alcaraz zauberte am Freitagnachmittag in der Wiener Stadthalle und zog durch ein souveraenes 6:4, 6:4 ins Halbfinale ein.",
            "body": [
                "Carlos Alcaraz untermauerte am Freitag, den 30. Oktober, seinen Status als Hallen-Gigant bei den Erste Bank Open in Wien. Der Spanier setzte sich im Viertelfinale mit 6:4 und 6:4 gegen den formstarken Briten Jack Draper durch und benoetigte dafuer lediglich 84 Minuten fehlerfreien Tempotennis.",
                "Alcaraz punktete nach dem ersten Aufschlag zu 81 Prozent und schlug 29 Winner bei nur 11 leichten Fehlern. Im Halbfinale am Samstag kommt es nun zum absoluten Traumduell gegen Top-Favorit Alexander Zverev, der sich zuvor mit 7:6 (4) und 6:4 gegen Andrey Rublev durchsetzen konnte."
            ]
        },
        "it": {
            "title": "ATP Vienna quarti: Carlos Alcaraz liquida Jack Draper 6-4, 6-4 e vola in semifinale contro Zverev",
            "subtitle": "Lo spagnolo mette a segno 29 vincenti e concede le briciole; Zverev piega Rublev nell'altro quarto della Wiener Stadthalle.",
            "excerpt": "Prestazione scintillante di Carlos Alcaraz a Vienna che regola Jack Draper in due set e guadagna la semifinale.",
            "body": [
                "Carlos Alcaraz non lascia scampo agli avversari sui campi veloci indoor dell'Erste Bank Open di Vienna. Venerdi 30 ottobre il fuoriclasse spagnolo ha piegato la resistenza del britannico Jack Draper con un duplice 6-4, archiviando la pratica in un'ora e ventiquattro minuti di gioco di altissima qualita.",
                "Con 29 vincenti e una percentuale dell'81 per cento di punti vinti sulla prima di servizio, Alcaraz si e garantito l'accesso al penultimo atto del torneo dove sfidera la testa di serie numero uno Alexander Zverev, uscito vincitore dal confronto serrato con Andrey Rublev per 7-6 (4), 6-4."
            ]
        },
        "pl": {
            "title": "ATP Wieden cwiercfinal: Carlos Alcaraz odprawia Jacka Drapera i melduje sie w polfinale ze Zverevem",
            "subtitle": "Hiszpan wygrywa 6:4, 6:4 po 29 uderzeniach konczacych; Alexander Zverev pokonuje Andrieja Rublowa w Wiener Stadthalle.",
            "excerpt": "Carlos Alcaraz nie zwalnia tempa w Wiedniu, pokonujac w piatek Jacka Drapera i meldujac sie w wielkim polfinale.",
            "body": [
                "Carlos Alcaraz wykonal kolejny pewny krok ku triumfowi w wiedenskim turnieju Erste Bank Open, pokonujac w piatek 30 pazdziernika Jacka Drapera 6:4, 6:4 w 84 minuty gry. Reprezentant Hiszpanii bezblednie radzil sobie z poteznym serwisem Brytyjczyka i dominowal w dluzszych wymianach z glebi kortu.",
                "Wicelider rankingu ATP poslal 29 winnerow i wygral 81 procent pilek po pierwszym podaniu. W sobote czeka go hitowe starcie polfinalowe z najwyzej rozstawionym Alexandrem Zverevem, ktory wczesniej wygral z Andriejem Rublowem 7:6 (4), 6:4."
            ]
        },
        "zh": {
            "title": "ATP维也纳公开赛八强战：阿尔卡拉斯直落两盘击溃德雷珀挺进半决赛，周六决战兹维列夫",
            "subtitle": "世界第二轰出29记制胜分以6-4、6-4完胜英国新星；头号种子兹维列夫力克卢布列夫携手过关。",
            "excerpt": "卡洛斯·阿尔卡拉斯周五在维也纳室内硬地赛场展现全面统治力，完胜德雷珀与兹维列夫会师半决赛。",
            "body": [
                "10月30日周五下午，ATP 500维也纳公开赛四分之一决赛迎来强强对话。世界排名第二的西班牙巨星卡洛斯·阿尔卡拉斯延续了火热状态，凭借29记制胜分与81%的一发得分率，以6-4、6-4轻取英国名将德雷珀，强势挺进四强。",
                "面对德雷珀势大力沉的左手发球，阿尔卡拉斯展现出大师级的接发球和底线调动能力，仅耗时84分钟便锁定胜局。阿尔卡拉斯将在周六的半决赛中对阵头号种子亚历山大·兹维列夫，后者在此前的一场焦点对决中以7-6 (4)、6-4击败了卢布列夫。"
            ]
        },
        "ja": {
            "title": "男子テニスATPウィーン大会準々決勝：アルカラスがドレイパーを破り4強入り、ズベレフと激突へ",
            "subtitle": "世界2位が29本のウィナーを量産し6-4、6-4で完勝；第1シードのズベレフもルブレフを下し準決勝進出。",
            "excerpt": "カルロス・アルカラスが金曜日のウィーン準々決勝でジャック・ドレイパーを退け、ズベレフとの準決勝へ駒を進めた。",
            "body": [
                "10月30日金曜日、エルステ・バンク・オープン男子シングルス準々決勝が行われ、第2シードのカルロス・アルカラスがイギリスのジャック・ドレイパーを6-4、6-4のストレートで退けた。84分間の激闘でアルカラスは29本のウィナーを奪い、相手の強烈なサーブを巧みなリターンで封じ込めた。",
                "ファーストサーブ時のポイント獲得率81％と隙を見せなかったアルカラスは、土曜日の準決勝で第1シードのアレクサンダー・ズベレフと対戦する。ズベレフもアンドレイ・ルブレフを7-6 (4)、6-4で下しており、最高峰の対決が実現する。"
            ]
        },
        "ko": {
            "title": "ATP 빈 8강: 카를로스 알카라스, 드레이퍼 6-4 6-4 완파하고 준결승서 츠베레프와 격돌",
            "subtitle": "세계 2위 알카라스 위너 29개 폭발하며 84분 만에 승리; 츠베레프도 루블료프 꺾고 4강 안착.",
            "excerpt": "카를로스 알카라스가 금요일 오스트리아 빈에서 잭 드레이퍼를 제압하고 알렉산더 츠베레프와의 준결승 빅매치를 성사시켰다.",
            "body": [
                "카를로스 알카라스가 10월 30일 금요일 열린 ATP 500 에르스테 방크 오픈 8강전에서 영국의 잭 드레이퍼를 6-4, 6-4로 완파하며 준결승에 진출했다. 알카라스는 84분간 펼쳐진 경기에서 29개의 위너를 몰아치며 드레이퍼의 강력한 왼손 서브를 무력화시켰다.",
                "첫 서브 득점률 81%의 완벽한 서브 게임을 유지한 알카라스는 토요일 준결승에서 톱시드 알렉산더 츠베레프와 맞붙는다. 츠베레프는 앞선 8강전에서 안드레이 루블료프를 7-6 (4), 6-4로 물리치고 준결승에 선착했다."
            ]
        },
        "ar": {
            "title": "تنس بطولة فيينا ربع النهائي: كارلوس ألكاراز يتغلب على جاك دريبر ويضرب موعدا ناريا مع زفيريف",
            "subtitle": "الإسباني يسجل 29 ضربة قاضية ليفوز 6-4 و6-4؛ وألكسندر زفيريف يتجاوز أندريه روبليف في صالة فيينا.",
            "excerpt": "واصل كارلوس ألكاراز عزفه المنفرد في بطولة فيينا المفتوحة بتفوقه على البريطاني جاك دريبر ليصعد إلى المربع الذهبي.",
            "body": [
                "تأهل النجم الإسباني كارلوس ألكاراز إلى الدور نصف النهائي لبطولة بنك إيرستيه في فيينا يوم الجمعة 30 أكتوبر، عقب فوزه المستحق على البريطاني جاك دريبر بمجموعتين نظيفتين 6-4 و6-4 في غضون 84 دقيقة فقط.",
                "وحسم ألكاراز المواجهة بفضل 29 ضربة قاضية ودقة إرسال بلغت 81 في المئة، ليتأهل إلى قمة مرتقبة يوم السبت أمام المصنف الأول ألكسندر زفيريف الذي نجح في التغلب على الروسي أندريه روبليف بنتيجة 7-6 و6-4."
            ]
        }
    },

    "f1-mexico-city-gp-2026-friday-practice-antonelli-paces-fp2-altitude": {
        "fr": {
            "title": "F1 GP du Mexique essais libres : Antonelli domine les EL2 a 2 285 m d'altitude avant sa potentielle couronne",
            "subtitle": "Le jeune leader de Mercedes tourne en 1:17.342 devant Leclerc et Verstappen ; une 9e place dimanche lui suffit pour le sacre.",
            "excerpt": "Kimi Antonelli a signe le meilleur temps de la deuxieme seance d'essais libres a Mexico, confirmant son aisance au volant de la Mercedes.",
            "body": [
                "Kimi Antonelli a confirme ses ambitions de titre mondial ce vendredi 30 octobre en s'adjugeant le meilleur chrono des essais libres 2 du Grand Prix du Mexique. Sur le trace de l'Autodromo Hermanos Rodriguez perche a 2 285 metres d'altitude, le pilote italien de 20 ans a claque un temps de 1:17.342 en pneus tendres, devancant la Ferrari de Charles Leclerc de 0,112 seconde et la Red Bull de Max Verstappen de 0,148 seconde.",
                "Avec 123 points d'avance sur George Russell, Antonelli n'a besoin que d'une neuvieme place lors de la course dominicale pour devenir le plus jeune champion du monde de l'histoire de la F1. Les ecuries continuent d'ajuster le refroidissement et la gestion thermique pour resister a l'air raréfié de la capitale mexicaine."
            ]
        },
        "es": {
            "title": "F1 GP de Mexico entrenamientos libres: Antonelli lidera los Libres 2 en la altitud camino del titulo mundial",
            "subtitle": "El joven italiano de Mercedes marca 1:17.342 superando a Leclerc y Verstappen; un noveno puesto el domingo sella el campeonato.",
            "excerpt": "Kimi Antonelli fue el mas rapido en los segundos libres de Mexico demostrando una gran adaptacion a la extrema altitud.",
            "body": [
                "Kimi Antonelli dio este viernes 30 de octubre un golpe de autoridad en el Autodromo Hermanos Rodriguez al marcar el mejor tiempo de la segunda sesion de entrenamientos libres del Gran Premio de Mexico. Al volante de su Mercedes con el dorsal 12, el talento de 20 anos paro el crono en 1:17.342, superando por escasas milesimas a Charles Leclerc y a Max Verstappen.",
                "El lider del campeonato cuenta con 123 puntos de colchon sobre George Russell y solo necesita cruzar la meta noveno el domingo para consagrarse como el campeon mas joven de la historia. Las escuderias centraron la jornada en controlar las altas temperaturas del motor y los frenos provocadas por la baja densidad del aire a mas de 2.200 metros."
            ]
        },
        "de": {
            "title": "Formel 1 GP Mexiko Freies Training: Antonelli dominiert FP2 in Hoehenluft auf dem Weg zur WM-Kroenung",
            "subtitle": "Der Mercedes-Youngster faehrt mit 1:17.342 Bestzeit vor Leclerc und Verstappen; P9 am Sonntag reicht zum Weltmeistertitel.",
            "excerpt": "Kimi Antonelli untermauerte am Freitag in Mexiko-Stadt seine Titelambitionen mit der schnellsten Runde im zweiten freien Training.",
            "body": [
                "Kimi Antonelli startete am Freitag, den 30. Oktober, souveraen in sein historisches Titelwochenende: Im zweiten freien Training zum Großen Preis von Mexiko auf dem Autodromo Hermanos Rodriguez erzielte der 20-jaehrige Italiener in 1:17.342 Minuten die Tagesbestzeit und verwies Charles Leclerc (Ferrari) und Max Verstappen (Red Bull) auf die Plaetze.",
                "Mit 123 Zaehlern Vorsprung auf Teamkollege George Russell genuegt Antonelli im Rennen am Sonntag bereits ein neunter Platz, um zum juengsten Formel-1-Weltmeister aller Zeiten aufzusteigen. Wegen der extrem duennen Luft auf 2.285 Metern Hoehe mussten alle Teams mit modifizierten Kuehloeffnungen und Bremsbelaegen arbeiten."
            ]
        },
        "it": {
            "title": "F1 GP Messico prove libere: Antonelli firma il miglior tempo nelle FP2 in quota a un passo dall'iride",
            "subtitle": "Il pilota bolognese gira in 1:17.342 precedendo Leclerc e Verstappen; domenica bastera la nona piazza per il Mondiale.",
            "excerpt": "Kimi Antonelli domina la seconda sessione di prove libere a Citta del Messico confermando il feeling con la pista e la Mercedes.",
            "body": [
                "Kimi Antonelli ha ribadito la propria superiorita venerdi 30 ottobre stampando il miglior crono nelle FP2 del Gran Premio del Messico. Sul tracciato dell'Autodromo Hermanos Rodriguez a 2.285 metri di altitudine, il ventenne fenomeno della Mercedes ha fermato il cronometro a 1:17.342 con mescola morbida, staccando la Ferrari di Charles Leclerc di 112 millesimi e la Red Bull di Max Verstappen di 148 millesimi.",
                "Forte di un margine di 123 punti su George Russell, ad Antonelli bastera conquistare due punti (P9) nel Gran Premio di domenica per laurearsi campione del mondo piu giovane di sempre. Il lavoro dei team si e concentrato sul raffreddamento delle power unit e sulla gestione gomme nell'aria rarefatta della capitale messicana."
            ]
        },
        "pl": {
            "title": "F1 GP Meksyku treningi: Antonelli najszybszy w FP2 na duzej wysokosci przed szansa na mistrzostwo",
            "subtitle": "Wloski kierowca Mercedesa uzyskuje czas 1:17.342 przed Leclercem i Verstappenem; dziewiate miejsce w niedziele da mu tytul.",
            "excerpt": "Kimi Antonelli zdominowal piatkowy drugi trening w Meksyku, zblizajac sie do upragnionego tytulu mistrza swiata.",
            "body": [
                "Kimi Antonelli potwierdzil swoja znakomita dyspozycje w piatek 30 pazdziernika, uzyskujac najlepszy rezultat podczas drugiego treningu przed Grand Prix Meksyku. Na torze Autodromo Hermanos Rodriguez, polozonym 2285 metrow nad poziomem morza, 20-letni kierowca Mercedesa pokonal okrazenie w czasie 1:17.342, wyprzedzajac Charlesa Leclerca o 0,112 sekundy i Maxa Verstappena o 0,148 sekundy.",
                "Mlodemu Wlochowi wystarczy zaledwie dziewiate miejsce w niedzielnym wyscigu, by zapewnic sobie tytul mistrza swiata Formuly 1 jako najmlodszy zawodnik w historii. Wszystkie zespoly zmagaly sie z chlodzeniem silnikow i hamulcow w rozrzedzonym gorskim powietrzu."
            ]
        },
        "zh": {
            "title": "F1墨西哥大奖赛二练：安东内利高原赛道飙出1分17秒342刷出全场最快，冠军点渐入佳境",
            "subtitle": "梅赛德斯天才领跑二练力压勒克莱尔与维斯塔潘；周日正赛保住第九名即可加冕最年轻世界冠军。",
            "excerpt": "基米·安东内利在周五的墨西哥城第二次自由练习赛中刷出最快圈速，向个人首个车手世界冠军稳步迈进。",
            "body": [
                "2026年F1墨西哥大奖赛周五练习赛于10月30日在海拔2285米的罗德里格斯兄弟赛道战罢。20岁的梅赛德斯车手基米·安东内利驾驶12号战车在二练中使用软胎跑出1分17秒342的惊艳圈速，以0.112秒的微弱优势力压法拉利的勒克莱尔拔得头筹，红牛名将维斯塔潘排名第三。",
                "手握123分巨大优势的安东内利在周日正赛中只需跑入前九名，便将超越维特尔成为F1历史最年轻的世界冠军。由于高原空气稀薄导致赛车散热效率下降20%以上，各支车队均在二练中重点对引擎和制动通风套件进行了严苛的长距离测试。"
            ]
        },
        "ja": {
            "title": "F1メキシコGP金曜フリー走行：アントネッリがFP2でトップタイム、世界王者戴冠へ好発進",
            "subtitle": "標高2285mの高地で1分17秒342を記録しルクレールとフェルスタッペンを抑える；日曜9位で戴冠決定。",
            "excerpt": "キミ・アントネッリがエルマノス・ロドリゲス・サーキットでのFP2でトップに立ち、初タイトルへ視界良好。",
            "body": [
                "10月30日金曜日、F1メキシコGPのフリー走行2回目が行われ、メルセデスのキミ・アントネッリが1分17秒342のファステストラップを記録して首位に立った。標高2285メートルの高地特有の薄い空気の中、20歳の新星はフェラーリのルクレールを0.112秒、レッドブルのフェルスタッペンを0.148秒リードした。",
                "ラッセルに123ポイント差をつけているアントネッリは、日曜の決勝で9位以内に入ればF1史上最年少でのワールドチャンピオンが決定する。空気密度が低いメキシコシティでは冷却とタイヤのデグラデーションが鍵となり、各チームが慎重なセットアップを進めた。"
            ]
        },
        "ko": {
            "title": "F1 멕시코 GP 연습주행: 안토넬리, 고지대 FP2서 1분 17초 342로 1위 차지하며 챔피언 청신호",
            "subtitle": "메르세데스 신성, 르클레르와 베르스타펜 제치고 최고 랩타임 기록; 일요일 결선 9위면 타이틀 확정.",
            "excerpt": "키미 안토넬리가 금요일 멕시코시티에서 열린 FP2에서 1위를 기록하며 사상 최연소 월드 챔피언 등극에 바짝 다가섰다.",
            "body": [
                "키미 안토넬리가 10월 30일 금요일 아우토드로모 에르마노스 로드리게스에서 열린 2026 F1 멕시코 그랑프리 두 번째 연습주행(FP2)에서 1분 17초 342의 랩타임으로 전체 1위에 올랐다. 해발 2,285미터의 희박한 공기 속에서 페라리의 샤를 르클레르를 0.112초 차로 제치며 압도적인 스피드를 과시했다.",
                "조지 러셀에 123점 차로 앞서 있는 안토넬리는 일요일 결선에서 9위(2점) 이상만 확보하면 역대 최연소 F1 월드 챔피언에 등극한다. 고지대 특유의 냉각 부족과 타이어 마모 관리가 주말 레이스의 핵심 과제로 부각됐다."
            ]
        },
        "ar": {
            "title": "فورمولا 1 جائزة المكسيك الكبرى: أنتونيللي يتصدر التجارب الحرة الثانية على ارتفاع 2285 مترا",
            "subtitle": "سائق مرسيدس الشاب يسجل 1:17.342 متفوقا على لوكلير وفيرستابن؛ والمركز التاسع الأحد يكفيه للتتويج باللقب العالمي.",
            "excerpt": "أظهر كيمي أنتونيللي سرعة فائقة في التجارب الحرة الثانية للمكسيك ليؤكد جاهزيته لحسم اللقب العالمي يوم الأحد.",
            "body": [
                "أكد الإيطالي كيمي أنتونيللي تفوقه الكبير يوم الجمعة 30 أكتوبر بتسجيله أسرع زمن في حصة التجارب الحرة الثانية لجائزة المكسيك الكبرى. وسجل سائق مرسيدس الشاب دقيقة واحدة و17 ثانية و342 جزءا من الثانية، متفوقا على شارل لوكلير سائق فيراري بفارق 0.112 ثانية وماكس فيرستابن سائق ريد بول بفارق 0.148 ثانية.",
                "ويحتاج أنتونيللي، الذي يتقدم بفارق 123 نقطة على زميله راسل، إلى نقطتين فقط يوم الأحد ليصبح أصغر بطل عالم في تاريخ فورمولا 1. وتركزت تجارب الفرق على مراقبة درجات حرارة المحركات والمكابح في ظل انخفاض كثافة الهواء على ارتفاع يفوق 2200 متر."
            ]
        }
    },

    "pga-tour-mexico-open-2026-round2-smotherman-leads-pereda-rai-chase": {
        "fr": {
            "title": "PGA Tour VidantaWorld Mexico Open R2 : Austin Smotherman prend la tete a -11 apres un 65 immacule",
            "subtitle": "Le vainqueur des Bermudes devance le heros local Raul Pereda et Aaron Rai de deux coups a VidantaVallarta.",
            "excerpt": "Austin Smotherman a confirme sa superbe forme automnale vendredi en signant un 65 pour mener le Mexico Open a mi-parcours.",
            "body": [
                "Austin Smotherman ne touche plus terre en cette fin de saison sur le circuit de la PGA. Ce vendredi 30 octobre, l'Americain de 32 ans a rendu une carte magistrale de 65 (six sous le par) sans le moindre bogey sur le parcours de VidantaVallarta, s'emparant de la tete du VidantaWorld Mexico Open 2026 avec un score total de 11 sous le par (131).",
                "Le Mexicain Raul Pereda, leader apres le premier tour, reste a l'affut a deux coups de la tete apres un solide 68 (-9), partageant la deuxieme place avec l'Anglais Aaron Rai. Le cut est tombe a un coup sous le par, garantissant un week-end a haute tension pour les 500 points FedExCup en jeu."
            ]
        },
        "es": {
            "title": "PGA Tour Mexico Open Ronda 2: Austin Smotherman asalta el liderato con 65 golpes y 11 bajo par",
            "subtitle": "El campeon de Bermudas aventaja en dos impactos al idolo local Raul Pereda y al ingles Aaron Rai en VidantaVallarta.",
            "excerpt": "Austin Smotherman entrego una tarjeta de 65 impactos sin bogeys este viernes para ponerse en cabeza tras 36 hoyos.",
            "body": [
                "El estadounidense Austin Smotherman sigue intratable en el calendario de otono del PGA Tour. Este viernes 30 de octubre firmo un recital de juego largo en el trazado Greg Norman Signature de VidantaVallarta, rubricando seis birdies sin error para un 65 que le instala como lider en solitario del VidantaWorld Mexico Open con 11 bajo par (131).",
                "El veracruzano Raul Pereda firmo un valioso 68 (-3) para situarse segundo empatado con Aaron Rai a solo dos golpes del lider, manteniendo intactas las esperanzas de victoria local. El corte se establecio en -1 con 68 golfistas clasificados para el fin de semana."
            ]
        },
        "de": {
            "title": "PGA Tour VidantaWorld Mexico Open R2: Austin Smotherman uebernimmt mit einer 65 die Halbzeitfuehrung",
            "subtitle": "Bermuda-Sieger liegt bei 11 unter Par; Lokalheld Raul Pereda und Aaron Rai lauern zwei Schlaege zurueck.",
            "excerpt": "Austin Smotherman spielte am Freitag eine fehlerfreie 65er-Runde und fuehrt die Mexico Open nach 36 Loechern souveraen an.",
            "body": [
                "Austin Smotherman setzt seinen goldenen Oktober auf der PGA Tour nahtlos fort. Am Freitag, den 30. Oktober, blieb der 32-jaehrige US-Profi auf dem Greg Norman Signature Course in VidantaVallarta ohne jeden Schlagverlust, lochte sechs Birdies zur 65 ein und uebernahm mit insgesamt 11 unter Par (131) die alleinige Fuehrung.",
                "Mexikos Publikumsliebling Raul Pereda hielt mit einer souveraenen 68 gut mit und teilt sich mit 9 unter Par Rang zwei mit dem Englaender Aaron Rai. Der Cut fiel bei einem Schlag unter Par, womit 68 Profis am Wochenende um den Siegerscheck kaempfen."
            ]
        },
        "it": {
            "title": "PGA Tour Mexico Open R2: Austin Smotherman vola al comando a quota -11 con un brillante 65",
            "subtitle": "Il trionfatore delle Bermuda precede di due colpi l'idolo messicano Raul Pereda e l'inglese Aaron Rai a VidantaVallarta.",
            "excerpt": "Giro senza errori per Austin Smotherman che con un fantastico 65 conquista la vetta solitaria del torneo a meta gara.",
            "body": [
                "Momento di grazia assoluto per Austin Smotherman sul PGA Tour. Venerdi 30 ottobre il golfista californiano ha dominato la seconda giornata del VidantaWorld Mexico Open a VidantaVallarta con un 65 impeccabile impreziosito da sei birdie, salendo al comando con un complessivo 11 sotto il par (131).",
                "A due lunghezze di distanza inseguono il messicano Raul Pereda (68 di giornata) e l'inglese Aaron Rai a quota -9. Il taglio e caduto a -1 lasciando 68 giocatori a contendersi la vittoria e i preziosi punti per mantenere la carta nel 2027."
            ]
        },
        "pl": {
            "title": "PGA Tour Mexico Open Runda 2: Austin Smotherman prowadzi po 36 dolkach z wynikiem 11 ponizej par dzieki rundzie 65",
            "subtitle": "Triumfator z Bermudow wyprzedza o dwa uderzenia Raula Perede i Aarona Rai w VidantaVallarta.",
            "excerpt": "Austin Smotherman nie popelnil w piatek zadnego bledu i dzieki wynikowi 65 objal samodzielne prowadzenie w VidantaWorld Mexico Open.",
            "body": [
                "Austin Smotherman kontynuuje swoja znakomita passe na polach PGA Tour. W piatek 30 pazdziernika 32-letni Amerykanin zagral rewelacyjna, bezbledna runde 65 uderzen na polu VidantaVallarta, dzieki czemu po dwoch dniach turnieju VidantaWorld Mexico Open prowadzi z lacznym wynikiem 11 ponizej par (131).",
                "Lider po pierwszym dniu Raul Pereda dolozyl solidne 68 i z wynikiem -9 dzieli druga lokate z Anglikiem Aaronem Rai. Cut ustalono na poziomie -1, co zapowiada zacieta walke o cenne punkty FedExCup Fall w decydujacych dwoch rundach."
            ]
        },
        "zh": {
            "title": "美巡赛墨西哥公开赛次轮：斯莫瑟曼轰65杆冲上榜首总成绩-11，佩雷达与赖紧随其后",
            "subtitle": "百慕大冠军延续无解状态两杆领跑；墨西哥本土球星佩雷达交68杆位列第二，晋级线定在-1杆。",
            "excerpt": "奥斯汀·斯莫瑟曼周五交出无柏忌的65杆，以总成绩低于标准杆11杆单独领跑墨西哥公开赛前两轮。",
            "body": [
                "刚刚在百慕大夺冠的美国名将奥斯汀·斯莫瑟曼在秋季赛势不可挡。10月30日周五在巴亚尔塔港进行的墨西哥公开赛第二轮较量中，他全场抓下6只小鸟且未吞下一个柏忌，打出极为精彩的65杆（-6），以两轮131杆（-11）的总成绩升至单独榜首。",
                "首轮领头羊、墨西哥本土球星劳尔·佩雷达发挥依旧稳健，打出68杆后以-9的总成绩与英格兰名将阿隆·赖并列第二位。本次赛事的36洞晋级线划在低于标准杆1杆（141杆），共有68名选手成功闯入周末决赛轮。"
            ]
        },
        "ja": {
            "title": "PGAツアー・メキシコオープン2日目：好調スモザーマンがノーボギーの65で通算11アンダー単独首位へ",
            "subtitle": "バミューダ覇者が首位浮上；地元ペレダとライが2打差追走、カットラインは通算1アンダー。",
            "excerpt": "オースティン・スモザーマンが金曜日の第2ラウンドで65を叩き出し、通算11アンダーでトーナメントをリードした。",
            "body": [
                "10月30日金曜日、ヴィダンタワールド・メキシコオープンの第2ラウンドが行われ、オースティン・スモザーマンが6バーディ、ノーボギーの完璧なゴルフで65をマーク。通算11アンダーの131で単独首位に躍り出た。",
                "初日首位の地元メキシコ出身ラウル・ペレダも68とスコアを伸ばし、イングランドのアーロン・ライと並んで2打差の通算9アンダー2位タイをキープ。カットラインは1アンダーと設定され、週末の決勝ラウンドに向けて白熱した争いが続く。"
            ]
        },
        "ko": {
            "title": "PGA 투어 멕시코 오픈 2R: 스모더맨, 보기 없이 65타 몰아치며 11언더파 단독 선두 질주",
            "subtitle": "버뮤다 우승 여세 몰아 2타 차 선두; 홈스타 라울 페레다와 에런 라이가 9언더파로 공동 2위 추격.",
            "excerpt": "오스틴 스모더맨이 금요일 2라운드에서 6언더파 65타를 기록하며 비단타 바야르타에서 36홀 단독 선두로 올라섰다.",
            "body": [
                "버뮤다 챔피언십 우승자 오스틴 스모더맨의 기세가 멕시코에서도 매섭게 이어졌다. 10월 30일 금요일 열린 비단타월드 멕시코 오픈 2라운드에서 스모더맨은 보기 없이 버디만 6개를 낚아채며 65타를 작성, 중간합계 11언더파 131타로 단독 1위에 등극했다.",
                "1라운드 선두였던 멕시코의 라울 페레다는 68타를 쳐 잉글랜드의 에런 라이와 함께 9언더파 133타로 공동 2위에 자리했다. 컷 기준선이 1언더파 141타로 결정된 가운데 68명의 선수가 주말 우승 경쟁에 나선다."
            ]
        },
        "ar": {
            "title": "جولة بي جي إيه بطولة المكسيك المفتوحة الجولة 2: سموذر مان ينتزع الصدارة بـ 11 ضربة تحت المعدل بعد 65 خالية من الأخطاء",
            "subtitle": "بطل برمودا يتقدم بضربتين على النجم المكسيكي راؤول بيريدا وآرون راي في فيدانتا فايارتا.",
            "excerpt": "واصل أوستن سموذر مان تألقه الكبير يوم الجمعة وسجل 65 ضربة لينفرد بصدارة بطولة المكسيك المفتوحة بعد 36 حفرة.",
            "body": [
                "يواصل الأمريكي أوستن سموذر مان تقديم أفضل مستوياته هذا الخريف في جولة بي جي إيه. ففي يوم الجمعة 30 أكتوبر، قدم اللاعب البالغ من العمر 32 عاما أداء استثنائيا على ملعب فيدانتا فايارتا مسجلا ست ضربات بيردي دون أي خطأ لينهي الجولة الثانية بـ 65 ضربة وينتزع صدارة بطولة فيدانتا وورلد المكسيك المفتوحة بمجموع 11 تحت المعدل (131 ضربة).",
                "وحافظ النجم المكسيكي راؤول بيريدا على فرصه القوية بتسجيل 68 ضربة ليتقاسم المركز الثاني بـ 9 تحت المعدل مع الإنجليزي آرون راي. واستقر معدل التأهل عند ضربة واحدة تحت المعدل ليصعد 68 لاعبا إلى منافسات عطلة نهاية الأسبوع الحاسمة."
            ]
        }
    }
}

# Strict validation
for slug, langs in OCT30_STORIES.items():
    assert len(langs) == 9, f"{slug} missing some of the 9 languages: {list(langs.keys())}"
    for lang in ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        assert lang in langs, f"{slug} missing language {lang}"
        trans = langs[lang]
        for field in ["title", "subtitle", "excerpt", "body"]:
            assert field in trans, f"{slug} {lang} missing field {field}"
            val = trans[field]
            if isinstance(val, str):
                assert "—" not in val, f"Em-dash in {slug} {lang} {field}: {val}"
                assert "--" not in val, f"Double-hyphen in {slug} {lang} {field}: {val}"
            elif isinstance(val, list):
                for i, item in enumerate(val):
                    assert "—" not in item, f"Em-dash in {slug} {lang} {field}[{i}]: {item}"
                    assert "--" not in item, f"Double-hyphen in {slug} {lang} {field}[{i}]: {item}"

print("Verification passed! No em-dashes or double-hyphens found in any of the 6 stories across all 9 languages.")

snippet_parts = []
for slug, langs in OCT30_STORIES.items():
    formatted_slug = json.dumps(slug)
    snippet_parts.append(f"{formatted_slug}: {json.dumps(langs, ensure_ascii=False, indent=2)},")

snippet = "\n".join(snippet_parts) + "\n"

stories_file = "frontend/src/i18n/stories.ts"
with open(stories_file, "r", encoding="utf-8") as f:
    content = f.read()

target = "export const STORY_I18N: Record<string, LocMap> = {\n"
assert target in content, "Target line not found in stories.ts"

new_content = content.replace(target, target + snippet, 1)

with open(stories_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully injected October 30 translations into frontend/src/i18n/stories.ts")
