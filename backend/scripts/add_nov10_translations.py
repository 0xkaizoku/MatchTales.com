# -*- coding: utf-8 -*-
"""Add 10 November 2026 translations for all 6 stories across 9 languages."""
import json
import os
import re

NOV10_STORIES = {
    "nfl-week9-mnf-bills-23-6-vikings-cook-allen-defense-2026": {
        "fr": {
            "title": "NFL Semaine 9 MNF : les Bills etouffent les Vikings 23-6 dans une demonstration a l'exterieur",
            "subtitle": "James Cook cumule 107 yards au sol et un touchdown. Buffalo inflige a Minnesota sa premiere defaite de la saison.",
            "excerpt": "James Cook a gagne 107 yards au sol et Buffalo a reussi cinq sacks sur Sam Darnold pour battre Minnesota 23-6 lundi.",
            "body": [
                "Les Buffalo Bills ont livre une lecon defensive lundi 9 novembre en s'imposant 23-6 face aux Minnesota Vikings au U.S. Bank Stadium de Minneapolis. James Cook a porte l'attaque au sol avec 19 courses pour 107 yards et un touchdown de 12 yards au deuxieme quart-temps. Josh Allen a ajoute 235 yards a la passe et trouve Dalton Kincaid pour un touchdown de 24 yards, portant Buffalo a 7-2.",
                "Le quarterback des Vikings Sam Darnold a subi cinq sacks et deux pertes de balle au quatrieme quart-temps. Invaincu a 7-0 au coup d'envoi, Minnesota n'a inscrit que deux field goals de Will Reichard, terminant sans touchdown pour la premiere fois de la saison. Dimanche a Madrid, les Bengals ont battu les Falcons 34-17 grace a 4 touchdowns de Joe Burrow."
            ]
        },
        "es": {
            "title": "NFL Semana 9 MNF: los Bills frenan a los Vikings 23-6 con gran actuacion de Cook y su defensa",
            "subtitle": "James Cook suma 107 yardas terrestres y un touchdown. Buffalo propina a Minnesota su primera derrota del curso.",
            "excerpt": "James Cook logro 107 yardas por tierra y Buffalo consiguio cinco capturas sobre Sam Darnold para vencer 23-6 a Minnesota.",
            "body": [
                "Los Buffalo Bills firmaron una actuacion defensiva sobresaliente el lunes 9 de noviembre al derrotar 23-6 a los invictos Minnesota Vikings en el U.S. Bank Stadium de Minneapolis. James Cook comando el ataque terrestre con 19 acarreos para 107 yardas y un touchdown de 12 yardas en el segundo cuarto. Josh Allen sumo 235 yardas de pase y conecto con Dalton Kincaid para un touchdown de 24 yardas, dejando a Buffalo con balance de 7-2.",
                "El mariscal de los Vikings Sam Darnold sufrio cinco capturas y dos perdidas de balon en el ultimo periodo. Minnesota llegaba 7-0 pero solo consiguio dos goles de campo de Will Reichard, quedandose sin touchdown por primera vez en la temporada. El domingo en Madrid, los Bengals derrotaron 34-17 a los Falcons con 4 touchdowns de Joe Burrow."
            ]
        },
        "de": {
            "title": "NFL Woche 9 MNF: Bills bremsen Vikings mit 23:6 durch James Cook und starke Defense aus",
            "subtitle": "James Cook erlaeuft 107 Yards und einen Touchdown. Buffalo fuegt Minnesota die erste Saisonniederlage zu.",
            "excerpt": "James Cook verbuchte 107 Rushing Yards und Buffalos Defense erzielte fuenf Sacks gegen Sam Darnold beim 23:6-Erfolg.",
            "body": [
                "Die Buffalo Bills zeigten am Montag, 9. November, eine dominante Defensivleistung und besiegten die zuvor ungeschlagenen Minnesota Vikings mit 23:6 im U.S. Bank Stadium in Minneapolis. James Cook fuehrte das Laufspiel mit 19 Laeufen fuer 107 Yards und einem 12-Yard-Touchdown an. Josh Allen warf fuer 235 Yards und bediente Dalton Kincaid fuer einen 24-Yard-Score zum 7-2-Rekord der Bills.",
                "Vikings-Quarterback Sam Darnold musste fuenf Sacks und zwei Turnover im vierten Viertel hinnehmen. Minnesota stand zuvor bei 7-0, kam aber nur zu zwei Field Goals durch Will Reichard und blieb erstmals ohne Touchdown. Am Sonntag in Madrid schlugen die Bengals die Falcons mit 34:17 dank vier Touchdowns von Joe Burrow."
            ]
        },
        "it": {
            "title": "NFL Week 9 MNF: i Bills soffocano i Vikings 23-6 guidati da James Cook e da una grande difesa",
            "subtitle": "James Cook corre per 107 yard e un touchdown. Buffalo infligge a Minnesota la prima sconfitta stagionale.",
            "excerpt": "James Cook corre per 107 yard e la difesa di Buffalo mette a segno cinque sack su Sam Darnold nel successo per 23-6.",
            "body": [
                "I Buffalo Bills hanno offerto una prova difensiva magistrale lunedi 9 novembre, superando per 23-6 gli imbattuti Minnesota Vikings al U.S. Bank Stadium di Minneapolis. James Cook ha guidato l'attacco su corsa con 19 portate per 107 yard e un touchdown da 12 yard. Josh Allen ha completato lanci per 235 yard e trovato Dalton Kincaid per un touchdown da 24 yard, portando Buffalo sul 7-2.",
                "Il quarterback dei Vikings Sam Darnold ha subito cinque sack e perso due palloni nel quarto periodo. Minnesota arrivava da un percorso netto di 7-0, ma ha segnato solo con due field goal di Will Reichard, restando senza mete per la prima volta nell'anno. Domenica a Madrid, i Bengals avevano battuto i Falcons 34-17 con 4 touchdown totali di Joe Burrow."
            ]
        },
        "pl": {
            "title": "NFL tydzien 9 MNF: Bills dławia Vikings 23-6 dzieki Jamesowi Cookowi i swietnej obronie",
            "subtitle": "James Cook zdobywa 107 jardow biegiem i przylozenie. Buffalo zadaje Minnesocie pierwsza porazke w sezonie.",
            "excerpt": "James Cook wybiegal 107 jardow, a obrona Buffalo zanotowala piec sackow na Samie Darnoldzie w wygranej 23-6.",
            "body": [
                "Buffalo Bills zaprezentowali znakomity popis defensywny w poniedzialek 9 listopada, pokonujac niepokonanych dotad Minnesota Vikings 23-6 na U.S. Bank Stadium w Minneapolis. James Cook poprowadzil gre biegowa z 19 probami na 107 jardow i 12-jardowym przylozeniem w drugiej kwarcie. Josh Allen dodal 235 jardow podaniami i podal na 24-jardowe przylozenie do Daltona Kincaida, prowadzac Bills do bilansu 7-2.",
                "Quarterback Vikings Sam Darnold zostal powalony pieciokrotnie i popelnil dwie straty w czwartej kwarcie. Minnesota miala bilans 7-0, ale zdobyla punkty tylko z dwoch kopniec Willa Reicharda i po raz pierwszy w sezonie nie zdobyla przylozenia. W niedziele w Madrycie Bengals pokonali Falcons 34-17 po 4 przylozeniach Joe Burrowa."
            ]
        },
        "zh": {
            "title": "NFL第9周周一夜赛：布法罗比尔23-6力克明尼苏达维京人送对手赛季首败",
            "subtitle": "詹姆斯·库克冲球107码并斩获达阵。比尔防守组完成五次擒杀，打破维京人7战全胜不败金身。",
            "excerpt": "詹姆斯·库克冲球107码加达阵，比尔防守组全场完成5次擒杀，布法罗客场23-6击败明尼苏达。",
            "body": [
                "布法罗比尔在11月9日周一的周一夜赛中展现了极具统治力的防守表现，客场23-6战胜此前保持不败的明尼苏达维京人。詹姆斯·库克全场19次冲球推进107码并在第二节斩获12码冲球达阵。四分卫乔希·阿伦传出235码并连线达尔顿·金凯德完成24码达阵，带领比尔将战绩提升至7胜2负。",
                "维京人四分卫萨姆·达诺德全场遭遇五次擒杀并在第四节出现两次失误。此前7胜0负的维京人仅靠踢球手威尔·赖查德命中两个任意球得分，遭遇本赛季首次无达阵尴尬。周日马德里赛中，辛辛那提猛虎34-17击败亚特兰大猎鹰，伯罗独揽4次达阵。"
            ]
        },
        "ja": {
            "title": "NFL第9週MNF：ビルズがクックの107ヤード走と堅守でバイキングスを23-6で圧倒",
            "subtitle": "ジェームズ・クックが107ヤード走とTDを記録。バッファローが無敗のミネソタに今季初黒星をつける。",
            "excerpt": "ジェームズ・クックが107ヤードを走り、ビルズ守備陣が5サックを奪ってバイキングスを23-6で撃破した。",
            "body": [
                "バッファロー・ビルズは11月9日月曜のマンデーナイトで鉄壁のディフェンスを披露し、開幕7連勝中だったミネソタ・バイキングスを23-6で下した。ジェームズ・クックが19回のキャリーで107ヤード、第2クォーターに12ヤードのTDランを決めた。ジョシュ・アレンは235パスヤードを記録し、ダルトン・キンケイドへ24ヤードのTDパスを通した。",
                "バイキングスのQBサム・ダーノルドは5つのサックを浴び、第4クォーターに2つのターンオーバーを喫した。ミネソタはKウィル・ライヒャードのFG2本のみに終わり、今季初のTDゼロ。日曜のマドリード戦では、ベンガルズがバロウの4TDでファルコンズを34-17で下している。"
            ]
        },
        "ko": {
            "title": "NFL 9주차 MNF: 버펄로 빌스, 쿡의 107야드 질주와 질식 수비로 바이킹스 23-6 완파",
            "subtitle": "제임스 쿡이 107야드 러싱과 1TD를 기록하며 버펄로가 무패 미네소타에 시즌 첫 패배를 안겼습니다.",
            "excerpt": "제임스 쿡이 107야드를 달리고 빌스 수비가 5개의 색을 성공시키며 미네소타를 23-6으로 제압했습니다.",
            "body": [
                "버펄로 빌스는 11월 9일 월요일 미니애폴리스 U.S. 뱅크 스타디움에서 열린 먼데이 나이트 풋볼에서 무패 행진을 달리던 미네소타 바이킹스를 23-6으로 꺾었습니다. 제임스 쿡이 19회 러싱 107야드와 12야드 터치다운을 기록했고, 조시 앨런은 235패싱야드와 돌턴 킨케이드에게 24야드 터치다운 패스를 연결했습니다.",
                "바이킹스 쿼터백 샘 다놀드는 5개의 색을 당하고 4쿼터에 2개의 턴오버를 헌납했습니다. 7연승을 달리던 미네소타는 윌 라이커드의 필드골 2개에 그치며 이번 시즌 처음으로 무터치다운 경기를 치렀습니다. 일요일 마드리드 경기에서는 신시내티가 조 버로의 4개 터치다운 활약으로 애틀랜타를 34-17로 눌렀습니다."
            ]
        },
        "ar": {
            "title": "الدوري الامريكي الاسبوع 9 MNF: بيلز يخنق فايكنغز 23-6 بقيادة جيمس كوك والدفاع القوي",
            "subtitle": "جيمس كوك يركض لمسافة 107 ياردات مع لمسة هبوط. بافلو يلحق بمينيسوتا اول خسارة في الموسم.",
            "excerpt": "جيمس كوك يحقق 107 ياردات بالركض ودفاع بافلو يسجل 5 اسقاطات على سام دارنولد للفوز 23-6.",
            "body": [
                "قدم بافلو بيلز عرضا دفاعيا استثنائيا يوم الاثنين 9 نوفمبر وتغلب على مينيسوتا فايكنغز الذي لم يهزم سابقا 23-6 في ملعب يو اس بنك بمنيابوليس. قاد جيمس كوك الهجوم الارضي بـ19 انطلاقة لمسافة 107 ياردات ولمسة هبوط من 12 ياردة. واضاف جوش الن 235 ياردة تمرير ولمسة 24 ياردة الى دالتون كينكيد ليصعد بافلو الى 7-2.",
                "تعرض قاذف فايكنغز سام دارنولد لخمسة اسقاطات وفقد كرتين في الربع الرابع. مينيسوتا التي دخلت اللقاء بسجل 7-0 اكتفت بهدفين ميدانيين من ويل رايتشارد وبقيت بلا لمسة هبوط لاول مرة. ويوم الاحد في مدريد تغلب بنغالز على فالكونز 34-17 بفضل 4 لمسات من جو بارو."
            ]
        }
    },
    "f1-sao-paulo-gp-2026-norris-wins-mercedes-clinch-constructors": {
        "fr": {
            "title": "GP de Sao Paulo : Lando Norris triomphe sous la pluie a Interlagos, Mercedes sacre chez les constructeurs",
            "subtitle": "Norris domine depuis la pole sous une meteo changeante. Verstappen remonte de la 21e a la 2e place. Mercedes valide le titre avec 652 points.",
            "excerpt": "Lando Norris a maitrise les pieges de la pluie pour remporter le GP du Bresil devant Max Verstappen, tandis que Mercedes s'assure le titre constructeurs 2026.",
            "body": [
                "Lando Norris a converti sa pole position en une victoire magistrale avec 14,618 secondes d'avance dimanche 8 novembre lors d'un Grand Prix de Sao Paulo tres arrose a Interlagos. Au volant de sa McLaren, le Britannique a surmonte les neutralisations et l'adherence precaire pour signer son 4e succes de la saison.",
                "La remontee du jour revient a Max Verstappen, parti 21e apres des penalites de moteur et remonte jusqu'au deuxieme rang grace a des depassements incisifs sous la pluie. George Russell 4e et Kimi Antonelli 5e ont apporte a Mercedes les points necessaires pour porter leur total a 652 points, scellant mathematiquement le titre mondial des constructeurs 2026."
            ]
        },
        "es": {
            "title": "GP de Sao Paulo: Lando Norris reina bajo la lluvia de Interlagos y Mercedes corona el Mundial de Constructores",
            "subtitle": "Norris manda desde la pole bajo condiciones cambiantes. Max Verstappen remonta de 21 a segundo. Mercedes asegura el titulo con 652 puntos.",
            "excerpt": "Lando Norris gano con autoridad en Brasil superando por 14.6s a Verstappen, mientras Mercedes festejo su primer cetro de equipos desde 2021.",
            "body": [
                "Lando Norris consiguio un triunfo memorable el domingo 8 de noviembre en un Gran Premio de Sao Paulo marcado por la lluvia en Interlagos. Saliendo desde la pole, el piloto de McLaren controlo los autos de seguridad y las condiciones de la pista para aventajar en 14.618 segundos a sus rivales y sellar su cuarta victoria del ano.",
                "Max Verstappen completo una remontada historica desde la 21ª posicion en parrilla hasta el segundo puesto con maniobras magistrales en agua. George Russell termino cuarto y Kimi Antonelli quinto, sumando los puntos que aseguraron el campeonato de constructores de Mercedes con 652 unidades, inalcanzable para Ferrari."
            ]
        },
        "de": {
            "title": "Sao Paulo GP: Lando Norris siegt im Regenchaos von Interlagos, Mercedes sichert Konstrukteurstitel",
            "subtitle": "Norris verwandelt Pole in Rennsieg bei wechselhaften Bedingungen. Verstappen rast von P21 auf Platz zwei. Mercedes mit 652 Punkten Weltmeister.",
            "excerpt": "Lando Norris gewann den dramatischen GP von Sao Paulo mit 14,6 Sekunden Vorsprung, waehrend Mercedes die Konstrukteurs-WM 2026 perfekt machte.",
            "body": [
                "Lando Norris feierte am Sonntag, 8. November, einen meisterhaften Regen-Triumph beim Grande Premio de Sao Paulo im Autodromo Jose Carlos Pace. Von der Pole Position aus behielt der McLaren-Pilot trotz mehrerer Safety-Car-Phasen die Nerven und fuhr mit 14,618 Sekunden Vorsprung zu seinem vierten Saisonsieg.",
                "Fuer das Highlight sorgte Max Verstappen, der nach einer Motorenstrafe von Platz 21 startete und sich bei nasser Fahrbahn sensationell auf Rang zwei nach vorne kaempfte. George Russell als Vierter und Kimi Antonelli als Fuenfter holten die entscheidenden Punkte, mit denen Mercedes (652 Punkte) den Konstrukteurstitel vorzeitig besiegelte."
            ]
        },
        "it": {
            "title": "GP San Paolo: Lando Norris domina sotto la pioggia a Interlagos, Mercedes vince il titolo Costruttori",
            "subtitle": "Norris vince dalla pole in condizioni bagnate. Verstappen compie una rimonta epica dal 21° al 2° posto. Mercedes campione con 652 punti.",
            "excerpt": "Lando Norris ha trionfato a Interlagos davanti a Verstappen, mentre la Mercedes ha conquistato matematicamente il Mondiale Costruttori 2026.",
            "body": [
                "Lando Norris ha conquistato una splendida vittoria domenica 8 novembre nel bagnatissimo Gran Premio di San Paolo a Interlagos. Partito dalla pole position, l'inglese della McLaren ha gestito magistralmente safety car e asfalto viscido, vincendo con 14,618 secondi di margine per centrare il quarto successo stagionale.",
                "L'eroe della domenica e stato Max Verstappen, risalito dal 21° posto in griglia fino al secondo gradino del podio con una serie incredibile di sorpassi sul bagnato. Con George Russell quarto e il campione del mondo Kimi Antonelli quinto, la Mercedes ha raggiunto quota 652 punti, vincendo matematicamente il campionato costruttori."
            ]
        },
        "pl": {
            "title": "GP Sao Paulo: Lando Norris wygrywa w deszczu na Interlagos, Mercedes mistrzem konstruktorow",
            "subtitle": "Norris triumfuje z pole position w zmiennych warunkach. Verstappen awansuje z 21. na 2. miejsce. Mercedes pieczetuje tytul z 652 punktami.",
            "excerpt": "Lando Norris wygral deszczowy wyscig o GP Sao Paulo przed Maxem Verstappenem, a Mercedes przypieczetowal tytul mistrza konstruktorow.",
            "body": [
                "Lando Norris odniosl znakomite zwyciestwo w niedziele 8 listopada w deszczowym Grand Prix Sao Paulo na torze Interlagos. Startujac z pole position, kierowca McLarena pewnie kontrolowal sytuacje na torze i wygral z przewaga 14,618 sekundy, siegajac po czwarty triumf w sezonie.",
                "Bohaterem wyscigu byl Max Verstappen, ktory po karze silnikowej ruszyl z 21. pola i po fenomenalnej jezdzie w deszczu przebil sie na drugie miejsce. George Russell na 4. pozycji oraz Kimi Antonelli na 5. dali Mercedesowi punkty, ktore zapewnily niemieckiej ekipie mistrzostwo swiata konstruktorow z dorobkiem 652 punktow."
            ]
        },
        "zh": {
            "title": "F1圣保罗大奖赛：诺里斯英特拉格斯雨战折桂 梅赛德斯锁定年度车队总冠军",
            "subtitle": "诺里斯杆位起步雨中独领风骚。维斯塔潘从第21位惊天超车杀至亚军。梅赛德斯以652分提前锁定车队总冠军。",
            "excerpt": "诺里斯在多变的雨地条件下力克群雄夺冠，维斯塔潘上演第21位追至亚军的史诗级逆转，梅赛德斯加冕2026车队总冠军。",
            "body": [
                "11月8日周日，迈凯伦车手兰多·诺里斯在英特拉格斯赛道的大雨中展现大师级控车技术，将杆位转化为14.618秒的巨大优势夺得圣保罗大奖赛胜利。这是诺里斯本赛季斩获的第四场分站冠军。",
                "全场最佳表现属于红牛车手马克斯·维斯塔潘，他因更换引擎受罚从第21位发车，在湿滑赛道上一路狂飙超车斩获亚军。拉塞尔获得第四，世界冠军安东内利位列第五，梅赛德斯车队积分达到652分，领先法拉利140分提前两站加冕2026赛季F1车队总冠军。"
            ]
        },
        "ja": {
            "title": "F1サンパウロGP：雨のインテルラゴスでノリスが優勝、メルセデスがコンストラクターズ王座獲得",
            "subtitle": "ノリスがポールからウェットレースを制覇。フェルスタッペンが21番手から2位へ驚異の猛追。メルセデスが652点で王者決定。",
            "excerpt": "ランド・ノリスが雨のサンパウロGPを14.6秒差で制し、メルセデスが2026年のコンストラクターズタイトルを確定させた。",
            "body": [
                "マクラーレンのランド・ノリスは11月8日日曜、雨に濡れたインテルラゴス・サーキットでポール・トゥ・ウィンを飾り、今季4勝目を挙げた。刻々と変わる雨脚とセーフティカー出動のなか、14.618秒差をつけてトップでチェッカーを受けた。",
                "圧巻だったのはペナルティで21番グリッドから発進したマックス・フェルスタッペン。雨中で脅威の追い上げを見せて2位でフィニッシュした。ジョージ・ラッセルが4位、キミ・アントネッリが5位に入り、メルセデスは652ポイントに到達して2026年コンストラクターズ王座を自力で確定させた。"
            ]
        },
        "ko": {
            "title": "F1 상파울루 GP: 빗속의 인터라고스에서 랜도 노리스 우승, 메르세데스 컨스트럭터 챔피언 확정",
            "subtitle": "노리스가 폴포지션에서 우중 레이스를 완벽 통제했습니다. 베르스타펜은 21위에서 2위로 대역전 질주. 메르세데스 652점으로 우승.",
            "excerpt": "랜도 노리스가 비 내리는 브라질 GP에서 우승을 차지했고, 메르세데스는 2026 시즌 F1 팀 챔피언 타이틀을 확정지었습니다.",
            "body": [
                "맥라렌의 랜도 노리스가 11월 8일 일요일 인터라고스 서킷에서 펼쳐진 상파울루 그랑프리에서 14.618초 차이로 압도적인 우승을 차지했습니다. 빗길 속에서 침착하게 레이스를 이끌며 시즌 4번째 그랑프리 우승 트로피를 들어올렸습니다.",
                "막스 베르스타펜은 엔진 페널티로 21번째 그리드에서 출발했으나, 빗길 속에서 믿기지 않는 추월쇼를 펼치며 2위로 완주했습니다. 조지 러셀 4위, 키미 안토넬리 5위로 메르세데스는 652점을 확보하며 페라리를 따돌리고 2026 시즌 컨스트럭터 챔피언십 우승을 조기 확정했습니다."
            ]
        },
        "ar": {
            "title": "جائزة ساو باولو الكبرى: لاندو نوريس يفوز بسباق انترلاغوس الممطر ومرسيدس تحسم بطولة الصانعين",
            "subtitle": "نوريس يحول الانطلاق الاول الى فوز بـ14.6 ثانية. فيرستابن يصعد من المركز 21 الى الوصافة. مرسيدس بطلة بـ652 نقطة.",
            "excerpt": "لاندو نوريس يحكم السيطرة في امطار انترلاغوس ليحقق الفوز، بينما ضمنت مرسيدس لقب الصانعين لعام 2026 رسميا.",
            "body": [
                "حقق لاندو نوريس فوزا بارعا يوم الاحد 8 نوفمبر في سباق جائزة ساو باولو الكبرى الممطر على حلبة انترلاغوس. انطلق سائق مكلارين من المركز الاول وحافظ على هدوئه خلال فترات سيارة الامان وتقلبات الطقس ليفوز بفارق 14.618 ثانية محققا فوزه الرابع هذا العام.",
                "وقدم ماكس فيرستابن سباقا اسطوريا بعدما انطلق من المركز 21 بسبب عقوبة المحرك وتجاوز سيارات الحلبة في مياه الامطار لينهي ثانيا. ومع حلول جورج راسل رابعا وكيمي انتونيلي خامسا، رفعت مرسيدس رصيدها الى 652 نقطة وحسمت لقب بطولة الصانعين لموسم 2026 رسميا."
            ]
        }
    },
    "atp-paris-masters-2026-alcaraz-downs-shelton-ninth-masters": {
        "fr": {
            "title": "Rolex Paris Masters Finale : Carlos Alcaraz dompte Ben Shelton 7-6(5), 7-5 pour son premier titre a Bercy",
            "subtitle": "L'Espagnol prend sa revanche de l'US Open, resiste aux 14 aces de Shelton et souleve son 9e trophee en Masters 1000.",
            "excerpt": "Carlos Alcaraz a battu Ben Shelton 7-6(5), 7-5 dimanche en finale a Paris pour s'offrir son tout premier titre au Rolex Paris Masters.",
            "body": [
                "Carlos Alcaraz a remporte son premier titre au Rolex Paris Masters dimanche 8 novembre en venant a bout de l'Americain Ben Shelton 7-6(5), 7-5 a l'Accor Arena. Cette victoire offre au joueur de 23 ans sa neuvieme couronne en carriere dans un tournoi ATP Masters 1000 et conforte sa place de numero un mondial de fin d'annee.",
                "Shelton a servi le feu avec 14 aces et menait 5-4 dans le tie-break de la premiere manche, mais Alcaraz a remporte trois echanges cruciaux du fond de court. Au deuxieme set, l'Espagnol a sauve deux balles de break a 4-4 puis breake a 5-5 sur un passing de coup droit laser avant de conclure blanc son jeu de service. En demi-finale samedi, Alcaraz avait domine Casper Ruud 6-4, 6-2."
            ]
        },
        "es": {
            "title": "Final Rolex Paris Masters: Carlos Alcaraz supera a Ben Shelton 7-6(5), 7-5 y conquista su primera corona en Bercy",
            "subtitle": "El espanol venga su tropiezo en el US Open, frena 14 saques directos de Shelton y alza su noveno titulo ATP Masters 1000.",
            "excerpt": "Carlos Alcaraz derroto a Ben Shelton 7-6(5), 7-5 en una intensa final bajo techo para inaugurar su palmares en el Masters de Paris.",
            "body": [
                "Carlos Alcaraz estreno su vitrina en el Rolex Paris Masters el domingo 8 de noviembre tras derrotar a Ben Shelton por 7-6(5) y 7-5 en el Accor Arena de Paris. Es el noveno titulo ATP Masters 1000 en el palmares del espanol de 23 anos, asegurando el numero uno mundial al cierre del curso.",
                "Shelton disparo 14 aces y mando 5-4 en el desempate de la manga inicial, pero Alcaraz encadeno tres puntos sublimes para embolsarse el parcial. En el segundo set, Alcaraz levanto dos bolas de rotura con 4-4 y rompio con 5-5 gracias a un passing cruzado perfecto antes de sellar en blanco su servicio. El sabado en semifinales Alcaraz habia vencido a Casper Ruud por 6-4 y 6-2."
            ]
        },
        "de": {
            "title": "Rolex Paris Masters Finale: Carlos Alcaraz bezwingt Ben Shelton 7:6(5), 7:5 fuer ersten Bercy-Titel",
            "subtitle": "Der Spanier raecht US-Open-Niederlage, trotzt 14 Shelton-Assen und feiert seine 9. Masters-1000-Kroenung.",
            "excerpt": "Carlos Alcaraz schlug Ben Shelton am Sonntag mit 7:6, 7:5 im Pariser Finale und holte seine neunte Masters-1000-Trophaee.",
            "body": [
                "Carlos Alcaraz hat am Sonntag, 8. November, seinen ersten Titel beim Rolex Paris Masters gewonnen. Im Endspiel der Accor Arena rang er Ben Shelton mit 7:6(5), 7:5 nieder. Fuer den 23-jaehrigen Spanier war es der neunte ATP-Masters-1000-Triumph seiner Karriere, der ihm die Nummer-eins-Position zum Jahresende sichert.",
                "Shelton schlug 14 Asse und fuehrte im Tiebreak des ersten Durchgangs mit 5:4, doch Alcaraz gewann drei Ballwechsel in Serie. Im zweiten Satz wehrte der Spanier bei 4:4 zwei Breakbaelle ab und schlug bei 5:5 mit einem Vorhand-Passierball zu, ehe er zu Null ausservierte. Im Halbfinale hatte Alcaraz am Samstag Casper Ruud 6:4, 6:2 geschlagen."
            ]
        },
        "it": {
            "title": "Rolex Paris Masters Finale: Carlos Alcaraz piega Ben Shelton 7-6(5), 7-5 e conquista il primo titolo a Bercy",
            "subtitle": "Lo spagnolo vendica la sconfitta agli US Open, resiste a 14 ace dell'americano e alza il 9° trofeo Masters 1000.",
            "excerpt": "Carlos Alcaraz ha battuto Ben Shelton 7-6(5), 7-5 nella finale di Parigi-Bercy conquistando il nono titolo Masters 1000 in carriera.",
            "body": [
                "Carlos Alcaraz ha trionfato per la prima volta al Rolex Paris Masters domenica 8 novembre, sconfiggendo l'americano Ben Shelton 7-6(5), 7-5 all'Accor Arena di Parigi. Per il 23enne spagnolo e il nono successo in carriera in un torneo ATP Masters 1000 e la certezza del primato mondiale a fine stagione.",
                "Shelton ha martellato con 14 ace e si e portato sul 5-4 nel tie-break del primo set, ma Alcaraz ha infilato tre punti capolavoro da fondo. Nel secondo set, lo spagnolo ha annullato due palle break sul 4-4 e ha trovato il break decisivo sul 5-5 con un passante di dritto prima di chiudere a zero il game conclusivo. Sabato Alcaraz aveva battuto Ruud 6-4, 6-2."
            ]
        },
        "pl": {
            "title": "Final Rolex Paris Masters: Carlos Alcaraz pokonuje Bena Sheltona 7-6(5), 7-5 i zdobywa pierwszy tytul w Bercy",
            "subtitle": "Hiszpan rewanżuje sie za US Open, odpiera 14 asow Sheltona i siega po dziewiaty tytul Masters 1000 w karierze.",
            "excerpt": "Carlos Alcaraz wygral z Benem Sheltonem 7-6(5), 7-5 w paryskim finale i po raz pierwszy zatriumfowal w turnieju w hali Bercy.",
            "body": [
                "Carlos Alcaraz wywalczyl w niedziele 8 listopada swoj dziewiaty tytul ATP Masters 1000 w karierze, pokonujac Bena Sheltona 7-6(5), 7-5 w finale Rolex Paris Masters w Accor Arena. Dzieki temu sukcesowi Hiszpan zapewnil sobie miano lidera rankingu na koniec sezonu.",
                "Shelton zaserwowal 14 asow i prowadzil 5-4 w tie-breaku pierwszego seta, lecz Alcaraz wygral trzy kluczowe akcje z rzedu. W drugiej partii Hiszpan obronil dwa break pointy przy stanie 4-4, po czym przelamal rywala przy 5-5 swietnym passing shotem i zakonczyl mecz gemem wygranym do zera. W sobote Alcaraz pokonal w polfinale Caspera Ruuda 6-4, 6-2."
            ]
        },
        "zh": {
            "title": "巴黎大师赛决赛：阿尔卡拉斯7-6(5)、7-5力克谢尔顿 斩获贝西首冠兼大师赛第9冠",
            "subtitle": "西班牙名将复仇美网失利，顶住谢尔顿14记ACE球狂轰，锁定年终世界第一荣耀。",
            "excerpt": "阿尔卡拉斯在巴黎大师赛决赛中直落两盘击败谢尔顿，斩获个人职业生涯首座巴黎冠军和第9座大师赛奖杯。",
            "body": [
                "11月8日周日，卡洛斯·阿尔卡拉斯在贝尔西体育馆的男单决赛中以7-6(5)、7-5击败美国年轻悍将本·谢尔顿，首度捧起劳力士巴黎大师赛冠军奖杯。这是23岁的西班牙天王斩获的个人第9座ATP大师赛冠军，也提前锁定了年终世界第一宝座。",
                "谢尔顿全场轰出14记ACE球，首盘抢七一度5-4领先，但阿尔卡拉斯在关键分展现坚韧防守连得3分逆转拿下一盘。第二盘阿尔卡拉斯在4-4平挽救破发点，并在5-5平轰出正手穿越破发，最终直落四分保发夺冠。周六半决赛中，阿尔卡拉斯以6-4、6-2横扫鲁德晋级。"
            ]
        },
        "ja": {
            "title": "ロレックス・パリ・マスターズ決勝：アルカラスがシェルトンを7-6(5)、7-5で破りベルシー初優勝",
            "subtitle": "スペインの怪童が全米オープンの雪辱を果たし、シェルトンの14本のエースを封じて通算9度目のマスターズ1000制覇。",
            "excerpt": "カルロス・アルカラスが接戦の末にベン・シェルトンをストレートで退け、パリ・マスターズ初制覇を達成した。",
            "body": [
                "カルロス・アルカラスは11月8日日曜、アコー・アリーナで行われたロレックス・パリ・マスターズ決勝でベン・シェルトンを7-6(5)、7-5で破り、念願の同大会初タイトルを獲得した。23歳のアルカラスにとっては通算9度目のATPマスターズ1000優勝となり、年間最終世界ランキング1位を確実にした。",
                "シェルトンは14本のエースを放ち、第1セットのタイブレークでも5-4とリードしたが、アルカラスがベースラインから3連続ポイントを奪って先取。第2セットも4-4の危機を脱し、5-5で鮮やかなフォアハンドパッシングでブレークを奪って勝利を収めた。土曜の準決勝ではルードを6-4、6-2で下していた。"
            ]
        },
        "ko": {
            "title": "롤렉스 파리 마스터스 결승: 카를로스 알카라스, 벤 셸턴 7-6(5), 7-5 꺾고 베르시 첫 우승",
            "subtitle": "US오픈 패배 설욕, 셸턴의 14개 서브에이스를 무력화하며 통산 9번째 마스터스 1000 트로피를 차지했습니다.",
            "excerpt": "카를로스 알카라스가 벤 셸턴과의 접전 끝에 7-6, 7-5로 승리하며 파리 마스터스 첫 정상에 올랐습니다.",
            "body": [
                "카를로스 알카라스가 11월 8일 일요일 파리 아코르 아레나에서 열린 결승전에서 미국의 벤 셸턴을 7-6(5), 7-5로 물리치고 생애 첫 롤렉스 파리 마스터스 타이틀을 차지했습니다. 23세의 알카라스는 통산 9번째 ATP 마스터스 1000 우승을 기록하며 연말 세계 1위를 굳혔습니다.",
                "셸턴은 14개의 에이스를 앞세워 1세트 타이브레이크 5-4까지 앞섰으나, 알카라스가 3연속 득점을 뽑아내며 세트를 챙겼습니다. 2세트 4-4에서 브레이크 위기를 넘긴 알카라스는 5-5에서 날카로운 포핸드 패싱샷으로 브레이크에 성공한 뒤 서브게임을 러브로 마무리했습니다. 토요일 준결승에서 알카라스는 루드를 6-4, 6-2로 제압했습니다."
            ]
        },
        "ar": {
            "title": "نهائي باريس بيرسي: كارلوس الكاراز يتفوق على بين شيلتون 7-6(5) و7-5 ليحرز لقبه الاول في البطولة",
            "subtitle": "الاسباني يثأر لخسارة امريكا المفتوحة، يقهر 14 ارسالا ساحقا لشيلتون، ويتوج بلقبه التاسع في بطولات الماسترز.",
            "excerpt": "كارلوس الكاراز يهزم بين شيلتون بمجموعتين دون رد 7-6 و7-5 في نهائي باريس للماسترز ليحقق تاسع القابه الكبرى.",
            "body": [
                "توج كارلوس الكاراز بلقبه الاول في دورة رولكس باريس للماسترز يوم الاحد 8 نوفمبر بعد فوزه على الامريكي بين شيلتون 7-6(5) و7-5 في صالة اكور ارينا. هذا اللقب هو التاسع في مسيرة النجم الاسباني البالغ 23 عاما في بطولات الاساتذة ذات الـ1000 نقطة، ليؤكد صدارته للتصنيف العالمي في نهاية الموسم.",
                "ضرب شيلتون 14 ارسالا ساحقا وتقدم 5-4 في الشوط الفاصل للمجموعة الاولى، لكن الكاراز انتزع ثلاث نقاط متتالية ليفوز بالمجموعة. وفي المجموعة الثانية انقذ الاسباني نقطتي كسر عند 4-4 ثم كسر ارسال شيلتون عند 5-5 بتسديدة امامية حاسمة قبل ان يحسم ارساله نظيفا. وكان الكاراز قد هزم كاسبر رود 6-4 و6-2 في نصف النهائي السبت."
            ]
        }
    },
    "pga-tour-wwt-championship-2026-final-blades-brown-playoff-win": {
        "fr": {
            "title": "WWT Championship : Blades Brown, 19 ans, bat Ben James en playoff et signe un exploit historique",
            "subtitle": "Brown rend une derniere carte de 64 et reussit un birdie au deuxieme trou de playoff a El Cardonal, devenant le plus jeune vainqueur depuis 95 ans.",
            "excerpt": "Blades Brown s'impose au deuxieme trou de barrage contre Ben James pour remporter son premier titre PGA Tour a Los Cabos a seulement 19 ans.",
            "body": [
                "Blades Brown est entre dans l'histoire du circuit PGA dimanche 8 novembre en remportant le World Wide Technology Championship en playoff face a Ben James a El Cardonal at Diamante. Auteur d'un magnifique 64 (-8) lors du dernier tour, Brown est revenu a hauteur de James (69) a 24 sous le par (264).",
                "Apres un birdie chacun sur le premier trou de barrage au 18, Brown a touche le green en deux coups lors du passage suivant pour assurer un nouveau birdie. Ben James ayant manque son putt de deux metres et demi, Brown est devenu a 19 ans le plus jeune vainqueur sur le PGA Tour en 95 ans. Peter Malnati termine troisieme a -21."
            ]
        },
        "es": {
            "title": "WWT Championship: Blades Brown, de 19 anos, vence a Ben James en el desempate en un triunfo historico",
            "subtitle": "Brown firma un 64 final y emboca birdie en el segundo hoyo extra en El Cardonal para ser el campeon mas joven en 95 anos en el PGA Tour.",
            "excerpt": "Blades Brown derroto a Ben James en el playoff de desempate en Diamante para alzar su primer trofeo del PGA Tour con 19 anos.",
            "body": [
                "Blades Brown hizo historia en el golf mundial el domingo 8 de noviembre al adjudicarse el World Wide Technology Championship tras superar a Ben James en el segundo hoyo de playoff en El Cardonal at Diamante, Los Cabos. Una tarjeta final de 64 golpes (-8) le permitio empatar a James (69) con un acumulado de 24 bajo par (264).",
                "Tras empatar con birdie el hoyo 18 en el primer desempate, Brown alcanzo el green en dos en la siguiente salida y firmo otro birdie. Cuando James fallo su intento de birdie desde dos metros y medio, Brown se consagro como el ganador mas joven del PGA Tour en 95 anos. Peter Malnati ocupo la tercera plaza en solitario con -21."
            ]
        },
        "de": {
            "title": "WWT Championship: 19-jaehriger Blades Brown schlaegt Ben James im Playoff zu historischem Premierensieg",
            "subtitle": "Brown spielt Schlussrunde von 64 und sichert sich mit Birdie am zweiten Extraloch als juengster PGA-Tour-Sieger seit 95 Jahren den Titel.",
            "excerpt": "Blades Brown siegte am zweiten Playoff-Loch gegen Ben James und kroente sich in Los Cabos mit 19 Jahren zum PGA-Tour-Champion.",
            "body": [
                "Der 19-jaehrige Blades Brown hat am Sonntag, 8. November, Geschichte auf der PGA Tour geschrieben. Bei der World Wide Technology Championship im El Cardonal at Diamante bezwang er Ben James am zweiten Playoff-Loch, nachdem er mit einer spektakulaeren 64er-Schlussrunde (-8) James (69) bei 24 unter Par (264) eingeholt hatte.",
                "Nachdem beide Spieler am ersten Extraloch auf der 18 zum Birdie lochten, traf Brown das Gruen im zweiten Durchgang mit zwei Schlaegen und sicherte sich per Zwei-Putt das Birdie. Da James aus rund zweieinhalb Metern vergab, wurde Brown der juengste Turniersieger auf der Tour seit 95 Jahren. Peter Malnati belegte mit -21 Rang drei."
            ]
        },
        "it": {
            "title": "WWT Championship: il 19enne Blades Brown supera Ben James al playoff in uno storico trionfo",
            "subtitle": "Brown gira in 64 nell'ultimo round e firma il birdie alla seconda buca di spareggio a El Cardonal, diventando il piu giovane vincitore in 95 anni.",
            "excerpt": "Blades Brown ha sconfitto Ben James alla seconda buca di playoff a Los Cabos, conquistando a 19 anni il primo titolo sul PGA Tour.",
            "body": [
                "Il diciannovenne Blades Brown ha scritto una pagina indimenticabile di golf domenica 8 novembre, vincendo il World Wide Technology Championship al playoff contro Ben James a El Cardonal at Diamante. Con un brillante 64 (-8) nell'ultimo giro, Brown ha raggiunto James (69) a quota 24 sotto il par (264 colpi).",
                "Dopo che entrambi avevano segnato un birdie alla prima buca supplementare sulla 18, Brown ha raggiunto il green in due colpi al passaggio successivo imbucando per un altro birdie. Quando James ha mancato il putt da due metri e mezzo, Brown e diventato il piu giovane vincitore sul PGA Tour negli ultimi 95 anni. Peter Malnati ha chiuso terzo a -21."
            ]
        },
        "pl": {
            "title": "WWT Championship: 19-letni Blades Brown pokonuje Bena Jamesa w dogrywce i przechodzi do historii",
            "subtitle": "Brown zagral 64 w finale i zrobil birdie na drugim dolku dogrywki w El Cardonal, zostajac najmlodszym mistrzem PGA Tour od 95 lat.",
            "excerpt": "Blades Brown wygral z Benem Jamesem na drugim dolku dogrywki w Los Cabos, zdobywajac swoj pierwszy puchar PGA Tour w wieku 19 lat.",
            "body": [
                "19-letni Blades Brown zapisal sie w historii zawodowego golfa w niedziele 8 listopada, wygrywajac World Wide Technology Championship po dogrywce z Benem Jamesem na polu El Cardonal at Diamante. Runda finałowa na poziomie 64 uderzen (-8) pozwolila mu zrownac sie z Jamesem (69) na wynik 24 ponizej par (264).",
                "Po birdie obu graczy na pierwszym dolku dogrywki na 18. dolku, Brown wszedl na green w dwoch uderzeniach i z latwoscia wbil birdie. Gdy James spudlowal swoj put z dwoch i pol metra, Brown zostal najmlodszym zwyciezca turnieju PGA Tour od 95 lat. Peter Malnati zajal trzecie miejsce z wynikiem -21."
            ]
        },
        "zh": {
            "title": "全球科技锦标赛：19岁小将布雷兹·布朗加洞赛绝杀本·詹姆斯 创95年最年轻美巡冠军纪录",
            "subtitle": "布朗决赛轮狂飙64杆，在卡多纳尔球场第二加洞抓鸟夺冠，成为美巡赛近95年来最年轻冠军。",
            "excerpt": "布雷兹·布朗在墨西哥洛斯卡波斯的加洞赛第二洞击败本·詹姆斯，以19岁之龄夺得职业生涯美巡首冠。",
            "body": [
                "11月8日周日，19岁的美国新星布雷兹·布朗在墨西哥卡多纳尔球场创造了美巡赛历史。他在世界科技锦标赛决赛轮交出不可思议的64杆（-8），与54洞领先者本·詹姆斯（69杆）同以低于标准杆24杆的264杆进入加洞决胜。",
                "在第18洞的第一个加洞两人双双抓鸟。再次回到18洞，布朗两杆将球送上果岭，稳稳两推抓下小鸟。随着詹姆斯错失8英尺鸟推，布朗加冕桂冠，成为美巡赛95年以来最年轻的分站冠军。彼得·马尔纳蒂以-21杆收获单独第三名。"
            ]
        },
        "ja": {
            "title": "WWT選手権：19歳のブレイズ・ブラウンがPOでベン・ジェームズを下し95年ぶりの最年少PGAツアー優勝",
            "subtitle": "ブラウンが最終日64をマークし、エル・カルドナルでのプレーオフ2ホール目でバーディ奪取。歴史的初優勝を飾る。",
            "excerpt": "19歳のブレイズ・ブラウンがプレーオフ2ホール目でベン・ジェームズを振り切り、米ツアー95年ぶりの最年少王者に輝いた。",
            "body": [
                "19歳のブレイズ・ブラウンは11月8日日曜、メキシコのエル・カルドナル・アット・ディアマンテで開催されたワールドワイド・テクノロジー選手権でベン・ジェームズをプレーオフで破り、PGAツアー史上95年ぶりとなる最年少優勝を成し遂げた。最終日に8アンダー64を叩き出し、通算24アンダー（264打）でジェームズ（69）に追いついた。",
                "18番パー5で行われたプレーオフ1ホール目は両者バーディ。2ホール目でブラウンは2オンに成功して確実にバーディを奪い、ジェームズの約2.5メートルのパットが外れて劇的な決着となった。ピーター・マルナティが通算21アンダーで単独3位に入った。"
            ]
        },
        "ko": {
            "title": "WWT 챔피언십: 19세 블레이즈 브라운, 연장 접전 끝 벤 제임스 꺾고 95년 만의 PGA 투어 최연소 우승",
            "subtitle": "브라운이 최종일 64타를 몰아치며 카르도날 2번째 연장 홀에서 버디를 잡아내 역사적인 첫 승을 거뒀습니다.",
            "excerpt": "블레이즈 브라운이 로스카보스에서 벤 제임스를 연장 끝에 꺾고 19세의 나이로 PGA 투어 최연소 챔피언에 올랐습니다.",
            "body": [
                "19세의 신예 블레이즈 브라운이 11월 8일 일요일 멕시코 엘 카르도날 앳 디아만테에서 열린 월드 와이드 테크놀로지 챔피언십에서 54홀 선두 벤 제임스를 연장 승부 끝에 제압하고 PGA 투어 역사를 썼습니다. 브라운은 최종 라운드에서 8언더파 64타를 몰아쳐 제임스(69타)와 함께 24언더파 264타 동타를 만들었습니다.",
                "18번 홀에서 열린 첫 번째 연장에서 나란히 버디를 잡은 뒤, 두 번째 연장에서 브라운은 투온에 성공하며 손쉽게 버디를 낚았습니다. 제임스의 2.5m 버디 퍼트가 빗나가면서 브라운은 95년 만에 PGA 투어 최연소 우승자가 되었습니다. 피터 말나티가 21언더파로 단독 3위를 기록했습니다."
            ]
        },
        "ar": {
            "title": "بطولة تكنولوجيا العالم للغولف: الشاب بليدز براون (19 عاما) يهزم بن جيمس في التمايز ليحقق فوزا تاريخيا",
            "subtitle": "براون يسجل 64 في الجولة الاخيرة ويحقق ضربة طائر في الحفرة الاضافية الثانية ليصبح اصغر بطل منذ 95 عاما في PGA.",
            "excerpt": "بليدز براون يفوز باللقب بعد جولة تمايز مثيرة في لوس كابوس ليصبح اصغر بطل في جولة PGA الامريكية منذ 95 عاما.",
            "body": [
                "حقق الشاب بليدز براون البالغ 19 عاما انجازا تاريخيا يوم الاحد 8 نوفمبر بفوزه ببطولة تكنولوجيا العالم للغولف على ملعب ال كاردونال في لوس كابوس. احرز براون 64 ضربة (-8) في اليوم الاخير ليعادل بن جيمس (69) عند 24 ضربة تحت المعدل (264 ضربة).",
                "وبعدما سجل اللاعبان ضربة طائر في الحفرة الاضافية الاولى على الحفرة 18، وصل براون الى المنطقة الخضراء بضربتين في الحفرة التالية محققا طائرا سهلا. وعندما اهدر جيمس محاولته، اصبح براون اصغر فائز ببطولة في جولة PGA منذ 95 عاما. وحل بيتر مالناتي ثالثا بمجموع -21."
            ]
        }
    },
    "pl-mw10-arsenal-1-0-hull-odegaard-six-clear-2026": {
        "fr": {
            "title": "Premier League J10 : Martin Odegaard crucifie Hull et permet a Arsenal de prendre six points d'avance",
            "subtitle": "Les Gunners s'imposent 1-0 a l'Emirates tandis que Manchester City chute 3-1 a Nottingham Forest et Chelsea tombe a Sunderland.",
            "excerpt": "Une frappe enroulee de Martin Odegaard a la 72e minute a donne la victoire 1-0 a Arsenal face a Hull City, portant leur avance a 6 points.",
            "body": [
                "Arsenal a conforte sa premiere place en Premier League samedi 7 novembre en s'imposant 1-0 face a Hull City a l'Emirates Stadium. L'equipe de Mikel Arteta a patiemment contourne le bloc adverse jusqu'a la 72e minute, quand Bukayo Saka a servi son capitaine Martin Odegaard dont la frappe enroulee du pied gauche a trouve la lucarne.",
                "Cette victoire porte Arsenal a 27 points en 10 journees (9 victoires, 1 defaite). Les Gunners profitent pleinement du faux pas de Manchester City, battu 3-1 a Nottingham Forest avec un double de Liam Delap. Chelsea a egalement trebuche a Sunderland (1-0), Liverpool a gagne 3-1 a Crystal Palace, Leeds a battu Tottenham 1-0 et Everton a domine Coventry 3-1. Classement : Arsenal 27, City 21, Brighton 19, Liverpool 18, Chelsea 16, Everton 16."
            ]
        },
        "es": {
            "title": "Premier League J10: Martin Odegaard tumba al Hull y dispara al Arsenal con seis puntos de ventaja",
            "subtitle": "Los Gunners ganan 1-0 en el Emirates mientras el Manchester City cae 3-1 ante el Forest y el Chelsea tropieza en Sunderland.",
            "excerpt": "Un golazo de Martin Odegaard en el minuto 72 dio la victoria 1-0 al Arsenal sobre el Hull City para afianzar el liderato con 27 puntos.",
            "body": [
                "El Arsenal amplio a seis puntos su ventaja al frente de la Premier League el sabado 7 de noviembre tras superar por 1-0 al Hull City en el Emirates Stadium. El conjunto de Mikel Arteta domino la posesion pero tuvo que esperar al minuto 72 para derribar el muro rival, cuando Martin Odegaard recibio de Bukayo Saka y clavo el balon en la escuadra con la zurda.",
                "El triunfo coloca a los Gunners con 27 puntos en 10 jornadas. El liderato se ensancho tras la sorprendente derrota 3-1 del Manchester City en casa del Nottingham Forest con doblete de Liam Delap. Ademas, el Chelsea cayo 1-0 en Sunderland, el Liverpool gano 3-1 al Crystal Palace, el Leeds vencio 1-0 al Tottenham y el Everton 3-1 al Coventry. Clasificacion: Arsenal 27, City 21, Brighton 19, Liverpool 18, Chelsea 16, Everton 16."
            ]
        },
        "de": {
            "title": "Premier League 10. Spieltag: Martin Odegaard schiesst Arsenal gegen Hull zu sechs Punkten Vorsprung",
            "subtitle": "Gunners siegen 1:0 im Emirates, waehrend Manchester City 1:3 bei Nottingham Forest patzt und Chelsea in Sunderland verliert.",
            "excerpt": "Ein Kunstschuss von Martin Odegaard in der 72. Minute sicherte Arsenal einen 1:0-Heimsieg ueber Hull City und baute die Tabellenfuehrung aus.",
            "body": [
                "Der FC Arsenal hat am Samstag, 7. November, seine Spitzenposition in der Premier League gefestigt. Gegen ein defensiv eingestelltes Hull City siegten die Gunners im Emirates Stadium mit 1:0. Den erloesenden Treffer erzielte Kapitaen Martin Odegaard in der 72. Minute mit einem sehenswerten Schlenzer in den Winkel nach Vorarbeit von Bukayo Saka.",
                "Arsenal steht nach 10 Spielen bei 27 Punkten (9 Siege, 1 Niederlage). Die Verfolger ließen Federn: Manchester City unterlag sensationell 1:3 bei Nottingham Forest (Doppelpack Liam Delap), waehrend Chelsea 0:1 in Sunderland verlor. Liverpool siegte 3:1 bei Crystal Palace, Leeds 1:0 gegen Tottenham und Everton 3:1 gegen Coventry. Tabelle: Arsenal 27, City 21, Brighton 19, Liverpool 18, Chelsea 16, Everton 16."
            ]
        },
        "it": {
            "title": "Premier League 10ª giornata: Martin Odegaard piega l'Hull e lancia l'Arsenal a +6 in vetta",
            "subtitle": "I Gunners superano 1-0 l'Hull all'Emirates, mentre il City crolla 3-1 a Nottingham e il Chelsea cade a Sunderland.",
            "excerpt": "Un gioiello a giro di Martin Odegaard al 72' ha regalato all'Arsenal l'1-0 sull'Hull City, portando i Gunners a sei lunghezze di vantaggio.",
            "body": [
                "L'Arsenal ha allungato a sei punti il proprio vantaggio in vetta alla Premier League sabato 7 novembre superando 1-0 l'Hull City all'Emirates Stadium. La squadra di Mikel Arteta ha scardinato la difesa ospite al 72', quando Bukayo Saka ha servito Martin Odegaard per uno splendido mancino a giro sotto l'incrocio dei pali.",
                "L'Arsenal vola a 27 punti in 10 giornate. Nel frattempo il Manchester City e caduto rovinosamente per 3-1 sul campo del Nottingham Forest sotto i colpi di Liam Delap (doppietta). Il Chelsea ha perso 1-0 a Sunderland, il Liverpool ha vinto 3-1 in casa del Crystal Palace, il Leeds 1-0 sul Tottenham e l'Everton 3-1 sul Coventry. Classifica: Arsenal 27, City 21, Brighton 19, Liverpool 18, Chelsea 16, Everton 16."
            ]
        },
        "pl": {
            "title": "Premier League 10. kolejka: Martin Odegaard daje wygrana z Hull, Arsenal ucieka na szesc punktow",
            "subtitle": "Kanonierzy wygrywaja 1-0 na Emirates, podczas gdy Manchester City przegrywa 1-3 w Nottingham, a Chelsea ulega Sunderlandowi.",
            "excerpt": "Piekne uderzenie Martina Odegaarda w 72. minucie dalo Arsenalowi wygrana 1-0 z Hull City i 6 punktow przewagi na czele tabeli.",
            "body": [
                "Arsenal umocnil sie na prowadzeniu w Premier League w sobote 7 listopada, pokonujac Hull City 1-0 na Emirates Stadium. Druzyna Mikela Artety przewazala caly mecz, a decydujacy cios zadala w 72. minucie, gdy Martin Odegaard po podaniu Bukayo Saki poslal precyzyjny rogal w samo okienko bramki rywali.",
                "To dziewiate zwyciestwo Arsenalu w 10 meczach, dajace 27 punktow. Z potkniec rywali skorzystal pelna garscia: Manchester City przegral 1-3 z Nottingham Forest po dwoch golach Liama Delapa, a Chelsea polegla 0-1 w Sunderlandzie. Liverpool wygral 3-1 z Crystal Palace, Leeds 1-0 ze Spurs, a Everton 3-1 z Coventry. Tabela: Arsenal 27, City 21, Brighton 19, Liverpool 18, Chelsea 16, Everton 16."
            ]
        },
        "zh": {
            "title": "英超第10轮：厄德高世界波制胜阿森纳1-0赫尔城 曼城爆冷落败枪手6分领跑",
            "subtitle": "阿森纳主场苦战告捷豪取27分，曼城客场1-3不敌诺丁汉森林，切尔西0-1负于桑德兰。",
            "excerpt": "厄德高第72分钟兜射死角破门，阿森纳主场1-0力克赫尔城，在积分榜上建立起6分的领先优势。",
            "body": [
                "11月7日周六，阿森纳在酋长球场凭借队长马丁·厄德高在第72分钟的精彩兜射破门，1-0力克赫尔城，将英超领跑优势扩大到6分。萨卡助攻厄德高在大禁区边缘轰出世界波直挂死角，打破了赫尔城的铁桶防守。",
                "此役过后，阿森纳10战9胜1负积27分稳居榜首。争冠主要对手曼城在客场1-3爆冷不敌诺丁汉森林，德拉普梅开二度。切尔西客场0-1输给桑德兰，利物浦客场3-1战胜水晶宫，利兹联1-0热刺，埃弗顿3-1考文垂。最新积分榜：阿森纳27分，曼城21分，布莱顿19分，利物浦18分，切尔西与埃弗顿同积16分。"
            ]
        },
        "ja": {
            "title": "プレミアリーグ第10節：ウーデゴール決勝弾でアーセナルがハルに1-0勝利、首位リードを6差に拡大",
            "subtitle": "エミレーツでガナーズが粘り勝ち。マンチェスター・シティがフォレストに1-3で敗戦、チェルシーもサンダーランドに屈す。",
            "excerpt": "72分のマルティン・ウーデゴールの見事なミドルシュートでアーセナルがハル・シティを1-0で破り、首位独走体制へ。",
            "body": [
                "アーセナルは11月7日土曜、エミレーツ・スタジアムで行われたハル・シティ戦に1-0で勝利し、プレミアリーグ首位でのリードを6ポイントに広げた。堅固な守備を崩しあぐねたが、72分にブカヨ・サカの折り返しを受けた主将ウーデゴールが鮮やかな左足シュートをゴール隅に沈めた。",
                "この勝利でアーセナルは10試合で9勝1敗の勝ち点27に到達。2位マンチェスター・シティがノッティンガム・フォレストに1-3で敗れる波乱が起き、チェルシーもサンダーランドに0-1で敗れた。リヴァプールはパレスに3-1で快勝。順位表：アーセナル27点、マン・C21点、ブライトン19点、リヴァプール18点、チェルシー16点、エヴァートン16点。"
            ]
        },
        "ko": {
            "title": "프리미어리그 10R: 외데고르 환상 결승골 아스널, 헐시티 1-0 꺾고 6점 차 선두 질주",
            "subtitle": "에미레이츠에서 1-0 신승. 맨체스터 시티가 포레스트에 1-3 일격을 당하고 첼시도 선덜랜드에 덜미를 잡혔습니다.",
            "excerpt": "마르틴 외데고르의 후반 72분 감아차기 결승골에 힘입어 아스널이 헐시티를 1-0으로 꺾고 선두를 굳건히 지켰습니다.",
            "body": [
                "아스널이 11월 7일 토요일 에미레이츠 스타디움에서 열린 헐시티와의 홈경기에서 1-0으로 승리하며 프리미어리그 선두 자리를 6점 차로 벌렸습니다. 답답한 흐름이 이어지던 후반 72분, 부카요 사카의 패스를 받은 주장 외데고르가 그림 같은 왼발 감아차기로 골망을 흔들었습니다.",
                "아스널은 10경기 9승 1패 승점 27점으로 단독 선두를 질주했습니다. 반면 2위 맨체스터 시티는 노팅엄 포레스트 원정에서 델랍에게 멀티골을 내주며 1-3 충격패를 당했습니다. 첼시도 선덜랜드에 0-1로 졌고, 리버풀은 팰리스를 3-1로 제압했습니다. 순위: 아스널 27, 맨시티 21, 브라이턴 19, 리버풀 18, 첼시 16, 에버턴 16."
            ]
        },
        "ar": {
            "title": "الدوري الانجليزي الجولة 10: اوديغارد يسجل هدفا رائعا ويقود ارسنال للفوز 1-0 على هال وتوسيع الفارق الى 6 نقاط",
            "subtitle": "الغانرز يتجاوزون هال بهدف نظيف بينما سقط مانشستر سيتي 1-3 امام فورست وخسر تشيلسي في سندرلاند.",
            "excerpt": "تسديدة متقنة من مارتن اوديغارد في الدقيقة 72 قادت ارسنال للفوز 1-0 على هال سيتي والابتعاد بصدارة الدوري الممتاز.",
            "body": [
                "عزز ارسنال صدارته للدوري الانجليزي الممتاز يوم السبت 7 نوفمبر بعد فوزه الصعب 1-0 على هال سيتي في ملعب الامارات. فك القائد مارتن اوديغارد شفرة الدفاع المتكتل في الدقيقة 72 عندما استلم تمريرة بوكايو ساكا وسدد كرة مقوسة بيسراه سكنت اعلى الزاوية.",
                "رفع ارسنال رصيده الى 27 نقطة من 10 مباريات (9 انتصارات وخسارة). واتسع الفارق بعد خسارة مانشستر سيتي المفاجئة 1-3 امام نوتنغهام فورست بهدفي ليام ديلاب، وهزيمة تشيلسي 0-1 امام سندرلاند. وفاز ليفربول 3-1 على كريستال بالاس، وليدز 1-0 على توتنهام، وايفرتون 3-1 على كوفنتري. الترتيب: ارسنال 27، سيتي 21، برايتون 19، ليفربول 18، تشيلسي 16، ايفرتون 16."
            ]
        }
    },
    "nba-warriors-crush-pelicans-138-87-curry-milestone-2026": {
        "fr": {
            "title": "NBA : Stephen Curry depasse DeRozan au 16e rang historique, les Warriors ecrasent les Pelicans 138-87",
            "subtitle": "Golden State aligne une huitieme victoire consecutive portee par 25 points de Curry, 25 de Podziemski et 23 de Lendeborg.",
            "excerpt": "Stephen Curry a inscrit 25 points en 21 minutes pour grimper au 16e rang des meilleurs marqueurs de l'histoire lors du carton des Warriors 138-87.",
            "body": [
                "Stephen Curry a offert un festival d'adresse lundi 9 novembre en marquant 25 points en seulement 21 minutes lors de la correction infligee par les Golden State Warriors aux New Orleans Pelicans (138-87) au Chase Center. Avec quatre tirs a trois points, Curry a porte son total en carriere a 26 803 points, depassant DeMar DeRozan (26 800) pour s'installer au 16e rang historique de la NBA.",
                "Les Warriors ont pris le large des le premier quart-temps (38-19) et compte jusqu'a 53 points d'avance. Brandin Podziemski a inscrit 25 points et le rookie Yaxel Lendeborg a brille en sortie de banc avec 23 points, 7 rebonds et 4 passes. Golden State enchaine un huitieme succes d'affilee et affiche un bilan de 8-3."
            ]
        },
        "es": {
            "title": "NBA: Stephen Curry supera a DeRozan en la lista historica y los Warriors arrollan 138-87 a los Pelicans",
            "subtitle": "Octavo triunfo consecutivo de Golden State con 25 puntos de Curry, 25 de Podziemski y 23 del novato Lendeborg.",
            "excerpt": "Stephen Curry sumo 25 puntos en 21 minutos y subio al 16º puesto historico de anotadores de la NBA en la paliza de los Warriors 138-87.",
            "body": [
                "Stephen Curry protagonizo otra exhibicion de tiro el lunes 9 de noviembre al anotar 25 puntos en apenas 21 minutos en la paliza de los Golden State Warriors por 138-87 sobre los New Orleans Pelicans en el Chase Center. Con cuatro triples, Curry alcanzo los 26.803 puntos de por vida en temporada regular, superando a DeMar DeRozan (26.800) para situarse 16º en la historia de la liga.",
                "Golden State sentencio el choque con un primer cuarto demoledor (38-19) y llego a mandar por 53 tantos. Brandin Podziemski igualo a Curry con 25 puntos y el novato Yaxel Lendeborg aporto 23 puntos, 7 rebotes y 4 asistencias desde el banquillo. Es la octava victoria seguida de los Warriors, que se colocan con marca de 8-3."
            ]
        },
        "de": {
            "title": "NBA: Stephen Curry ueberholt DeRozan auf Rang 16 aller Zeiten, Warriors deklassieren Pelicans 138:87",
            "subtitle": "Achter Sieg in Folge fuer Golden State dank 25 Punkten von Curry, 25 von Podziemski und 23 von Rookie Lendeborg.",
            "excerpt": "Stephen Curry erzielte 25 Punkte in 21 Minuten, zog an DeMar DeRozan vorbei und fuehrte Golden State zu einem 138:87-Kantersieg.",
            "body": [
                "Stephen Curry zeigte am Montag, 9. November, eine Demonstration seiner Wurfkraft und fuehrte die Golden State Warriors im Chase Center zu einem 138:87-Triumph ueber die New Orleans Pelicans. In nur 21 Minuten Spielzeit markierte Curry 25 Punkte und vier Dreier, womit er seine Karriereausbeute auf 26.803 Punkte steigerte und DeMar DeRozan (26.800) auf Platz 16 der ewigen NBA-Scoring-Liste abloeste.",
                "Die Warriors ueberrollten New Orleans bereits im ersten Viertel (38:19) und fuehrten zwischenzeitlich mit 53 Zaehlern. Brandin Podziemski steuerte ebenfalls 25 Punkte bei, Rookie Yaxel Lendeborg ueberzeugte von der Bank mit 23 Punkten und 7 Rebounds. Fuer Golden State war es der achte Sieg hintereinander zum 8-3-Saisonstart."
            ]
        },
        "it": {
            "title": "NBA: Stephen Curry supera DeRozan al 16° posto ogni epoca, i Warriors travolgono i Pelicans 138-87",
            "subtitle": "Ottava vittoria di fila per Golden State con 25 punti di Curry, 25 di Podziemski e 23 del rookie Lendeborg.",
            "excerpt": "Stephen Curry realizza 25 punti in 21 minuti e scavalca DeRozan nella classifica marcatori all-time nel roboante 138-87 dei Warriors.",
            "body": [
                "Stephen Curry ha regalato una delle sue serate di tiro straordinarie lunedi 9 novembre, segnando 25 punti in soli 21 minuti nel travolgente 138-87 dei Golden State Warriors contro i New Orleans Pelicans al Chase Center. Mandando a bersaglio quattro triple, Curry ha toccato quota 26.803 punti in carriera, superando DeMar DeRozan (26.800) al 16° posto assoluto nella storia della NBA.",
                "I Warriors hanno spaccato la gara gia nel primo quarto (38-19) toccando un vantaggio massimo di 53 punti. Brandin Podziemski ha segnato 25 punti e la matricola Yaxel Lendeborg ha incantato dalla panchina con 23 punti, 7 rimbalzi e 4 assist. Si tratta dell'ottavo successo consecutivo per Golden State, salita sul record di 8-3."
            ]
        },
        "pl": {
            "title": "NBA: Stephen Curry wyprzedza DeRozana na 16. miejscu w historii, Warriors rozbijaja Pelicans 138-87",
            "subtitle": "Osme zwyciestwo z rzedu Golden State dzieki 25 punktom Curry'ego, 25 Podziemskiego i 23 rezerwowego Lendeborga.",
            "excerpt": "Stephen Curry rzucil 25 punktow w 21 minut i awansowal na 16. miejsce na liscie strzelcow wszech czasow NBA w pogromie 138-87.",
            "body": [
                "Stephen Curry dal kolejny popis skutecznosci w poniedzialek 9 listopada, zdobywajac 25 punktow w zaledwie 21 minut gry w efektownym zwyciestwie Golden State Warriors nad New Orleans Pelicans 138-87 w Chase Center. Trafiajac cztery trojki, Curry osiagnal 26 803 punkty w sezonie zasadniczym, wyprzedzajac DeMara DeRozana (26 800) na 16. miejscu w klasyfikacji wszech czasow NBA.",
                "Warriors zdominowali rywali juz w pierwszej kwarcie (38-19) i prowadzili nawet roznica 53 punktow. Brandin Podziemski rowniez rzucil 25 punktow, a debiutant Yaxel Lendeborg zanotowal 23 punkty, 7 zbiorek i 4 asysty z lawki. To osma wygrana Warriors z rzedu, poprawiajaca ich bilans do 8-3."
            ]
        },
        "zh": {
            "title": "NBA常规赛：库里总得分超越德罗赞升至历史第16 勇士138-87狂胜鹈鹕豪取8连胜",
            "subtitle": "金州勇士掀起进攻狂潮，库里21分钟砍下25分，波杰姆斯基25分，新秀伦德博格替补贡献23分7板。",
            "excerpt": "库里出场21分钟命中4记三分砍下25分，总得分升至NBA历史第16位，勇士51分大胜鹈鹕豪取八连胜。",
            "body": [
                "11月9日周一，金州勇士在大通中心以138-87狂胜新奥尔良鹈鹕。斯蒂芬·库里仅出战21分钟便高效轰下25分并命中4记三分球。凭借这25分，库里职业生涯常规赛总得分达到26803分，正式超越德马尔·德罗赞（26800分），独占NBA历史得分榜第16位。",
                "勇士在首节便打出38-19确立胜势，下半场最大领先优势达到53分。布兰丁·波杰姆斯基同样砍下25分，新秀亚克塞尔·伦德博格替补登场24分钟贡献23分、7个篮板和4次助攻。这场51分的大胜让勇士豪取8连胜，战绩提升至8胜3负。"
            ]
        },
        "ja": {
            "title": "NBA：カリーが歴代得点16位に浮上、ウォリアーズがペリカンズを138-87で圧倒し8連勝",
            "subtitle": "カリーが21分で25点、ポジェムスキー25点、新人レンデボーグが23得点。ゴールデンステイトが破竹の8連勝。",
            "excerpt": "ステフィン・カリーがデローザンを抜いて通算得点歴代16位に浮上。ウォリアーズが51点差の大勝で8連勝を飾った。",
            "body": [
                "ゴールデンステイト・ウォリアーズは11月9日月曜、チェイス・センターでニューオーリンズ・ペリカンズを138-87で粉砕した。ステフィン・カリーはわずか21分間の出場で4本のスリーポイントを含む25得点を挙げ、通算26,803得点に到達。デマー・デローザン（26,800得点）を抜いてNBA歴代得点ランキング16位に浮上した。",
                "ウォリアーズは第1クォーターで38-19と圧倒し、最大53点差をつける猛攻を見せた。ブランディン・ポジェムスキーも25得点をマークし、ルーキーのヤクセル・レンデボーグがベンチから23得点、7リバウンド、4アシストと躍動。ウォリアーズは怒涛の8連勝で8勝3敗とした。"
            ]
        },
        "ko": {
            "title": "NBA: 스테픈 커리, 드로잔 제치고 역대 득점 16위 등극, 워리어스 펠리컨스 138-87 대파 8연승",
            "subtitle": "커리 21분 25점 폭발, 포지엠스키 25점, 루키 렌데보그 23점. 골든스테이트 8연승으로 8승 3패 질주.",
            "excerpt": "스테픈 커리가 25점을 올리며 NBA 역대 통산 득점 16위로 올라섰고, 골든스테이트는 뉴올리언스를 51점 차로 대파했습니다.",
            "body": [
                "골든스테이트 워리어스는 11월 9일 월요일 체이스 센터에서 열린 경기에서 뉴올리언스 펠리컨스를 138-87로 대파했습니다. 스테픈 커리는 21분만 뛰고도 3점슛 4개를 묶어 25점을 기록, 정규시즌 통산 26,803점에 도달하며 더마 드로잔(26,800점)을 제치고 NBA 통산 득점 16위로 올라섰습니다.",
                "워리어스는 1쿼터부터 38-19로 크게 앞서며 후반 한때 53점 차까지 격차를 벌렸습니다. 브랜딘 포지엠스키가 25점을 넣었고 루키 포워드 약셀 렌데보그가 벤치에서 23점 7리바운드 4어시스트를 보탰습니다. 51점 차 대승으로 워리어스는 8연승을 질주하며 8승 3패를 기록했습니다."
            ]
        },
        "ar": {
            "title": "الدوري الامريكي للمحترفين: ستيفن كاري يصعد للمركز 16 تاريخيا وواريورز يكتسح بيلوكانز 138-87",
            "subtitle": "غولدن ستيت يحقق فوزه الثامن تواليا بفضل 25 نقطة لكاري و25 لبودزيمسكي و23 للمبتدئ لينديبورغ.",
            "excerpt": "ستيفن كاري يسجل 25 نقطة في 21 دقيقة ويتجاوز ديروزان في قائمة هدافي NBA التاريخية في انتصار واريورز الساحق.",
            "body": [
                "قدم ستيفن كاري عرضا هجوميا رائعا يوم الاثنين 9 نوفمبر وسجل 25 نقطة في 21 دقيقة فقط ليقود غولدن ستيت واريورز لسحق نيو اورليانز بيلوكانز 138-87 في تشيس سنتر. وبأربع ثلاثيات رفع كاري رصيده الى 26803 نقاط في مسيرته متخطيا ديمار ديروزان (26800) ليحتل المركز 16 في تاريخ هدافي NBA.",
                "سيطر واريورز من البداية متقدما 38-19 في الربع الاول ووصل الفارق الى 53 نقطة. واضاف براندين بودزيمسكي 25 نقطة وسجل المبتدئ ياكسيل لينديبورغ 23 نقطة و7 متابعات من دكة البدلاء. وهذا هو الفوز الثامن تواليا لغولدن ستيت ليرفع رصيده الى 8-3."
            ]
        }
    }
}


def lint_obj(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            lint_obj(v, path + "/" + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            lint_obj(v, path + "[%s]" % i)
    elif isinstance(obj, str):
        s = re.sub(r"https?://\S+", "", obj)
        if "—" in s or "--" in s:
            raise SystemExit("dash in %s: %s" % (path, s[:80]))


if __name__ == "__main__":
    lint_obj(NOV10_STORIES)
    print("All November 10 story translations validated: 0 em-dashes and 0 double-hyphens.")

    snippet_parts = []
    for slug, langs in NOV10_STORIES.items():
        snippet_parts.append(f"{json.dumps(slug)}: {json.dumps(langs, ensure_ascii=False, indent=2)},")
    snippet = "\n".join(snippet_parts) + "\n"

    stories_file = os.path.join(os.path.dirname(__file__), "../../frontend/src/i18n/stories.ts")
    with open(stories_file, "r", encoding="utf-8") as f:
        content = f.read()

    target = "export const STORY_I18N: Record<string, LocMap> = {\n"
    assert target in content, "Target line not found in stories.ts"

    new_content = content.replace(target, target + snippet, 1)
    with open(stories_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully injected November 10 translations into frontend/src/i18n/stories.ts")

