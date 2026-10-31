# -*- coding: utf-8 -*-
"""
Add 1 November 2026 translations for all 6 stories across 9 languages.
"""
import json
import re
import os

NOV01_STORIES = {
    "f1-mexico-city-gp-2026-antonelli-crowned-world-champion-history": {
        "fr": {
            "title": "GP du Mexique : Kimi Antonelli termine 2e derriere Leclerc et devient le plus jeune champion du monde de F1",
            "subtitle": "A 20 ans et 68 jours, le prodige italien de Mercedes efface le record de Sebastian Vettel et decroche le titre mondial 2026.",
            "excerpt": "Kimi Antonelli est entre dans la legende dimanche a Mexico en devenant le plus jeune champion du monde de l'histoire de la F1.",
            "body": [
                "L'Autodromo Hermanos Rodriguez a ete le theatre d'un moment d'histoire ce dimanche 1er novembre. En franchissant la ligne d'arrivee en deuxieme position derriere Charles Leclerc, l'Italien Kimi Antonelli a officiellement coiffe la couronne de champion du monde des pilotes 2026.",
                "Parti en pole position, le rookie de Mercedes a gere sa course avec un sang-froid remarquable pour securiser les 18 points necessaires. Leclerc s'est impose pour Ferrari, mais le heros du jour est bien Antonelli, qui devient le premier Italien titre depuis Alberto Ascari en 1953 et le plus jeune champion de l'histoire a 20 ans et 68 jours."
            ]
        },
        "es": {
            "title": "GP de Mexico: Kimi Antonelli finaliza segundo tras Leclerc y se corona como el campeon del mundo mas joven de la F1",
            "subtitle": "A sus 20 anos y 68 dias, el prodigio de Mercedes bate el historico registro de Sebastian Vettel y gana el Mundial 2026.",
            "excerpt": "Kimi Antonelli escribio su nombre en los libros de oro del deporte al proclamarse campeon del mundo de Formula 1 en Mexico.",
            "body": [
                "El Autodromo Hermanos Rodriguez vivio una jornada para la posteridad este domingo 1 de noviembre. Al terminar segundo tras Charles Leclerc, Kimi Antonelli se proclamo campeon del mundo de Formula 1 2026 a falta de tres grandes premios para el final.",
                "El piloto de Mercedes, que partia desde la pole, controlo el ritmo sin asumir riesgos innecesarios. Charles Leclerc se llevo el triunfo para Ferrari, mientras Antonelli desataba la fiesta en el Foro Sol al convertirse en el primer italiano campeon desde Alberto Ascari en 1953 y el mas joven de todos los tiempos."
            ]
        },
        "de": {
            "title": "Formel 1 Mexiko GP: Kimi Antonelli wird Zweiter hinter Leclerc und kroent sich zum juengsten Weltmeister aller Zeiten",
            "subtitle": "Mit 20 Jahren und 68 Tagen bricht das Mercedes-Talent den Rekord von Sebastian Vettel und sichert sich den WM-Titel 2026.",
            "excerpt": "Kimi Antonelli hat am Sonntag in Mexiko-Stadt Motorsportgeschichte geschrieben und die Formel-1-Weltmeisterschaft gewonnen.",
            "body": [
                "Das Autodromo Hermanos Rodriguez erlebte am Sonntag, den 1. November, einen historischen Moment. Kimi Antonelli beendete den Grossen Preis von Mexiko auf Platz zwei hinter Charles Leclerc und kroente sich zum Weltmeister 2026.",
                "Der von der Pole Position gestartete Mercedes-Youngster fuhr ein fehlerfreies Rennen. Leclerc holte den Sieg fuer Ferrari, doch der Tag gehoerte Antonelli, der mit 20 Jahren und 68 Tagen den 16 Jahre alten Rekord von Sebastian Vettel ausloeschte und erster italienischer Champion seit Alberto Ascari 1953 ist."
            ]
        },
        "it": {
            "title": "GP Messico: Kimi Antonelli e nella leggenda, 2° dietro a Leclerc e campione del mondo di Formula 1 piu giovane della storia",
            "subtitle": "A 20 anni e 68 giorni il fenomeno della Mercedes batte il record di Vettel e riporta il titolo iridato in Italia dopo 73 anni.",
            "excerpt": "Kimi Antonelli conquista il titolo mondiale di Formula 1 2026 sul circuito di Citta del Messico al termine di una gara memorabile.",
            "body": [
                "L'Italia dei motori torna sul tetto del mondo dopo 73 anni di attesa. Domenica 1 novembre all'Autodromo Hermanos Rodriguez, Kimi Antonelli ha chiuso al secondo posto il Gran Premio del Messico laureandosi campione del mondo 2026.",
                "Gara vinta con merito dalla Ferrari di Charles Leclerc, ma il trionfo iridato e tutto del ventenne bolognese della Mercedes. Antonelli supera il primato di Sebastian Vettel diventando il piu giovane campione nella storia della F1 e il primo italiano iridato dai tempi di Alberto Ascari nel 1953."
            ]
        },
        "pl": {
            "title": "GP Meksyku: Kimi Antonelli drugi za Leclerkiem i zostaje najmlodszym mistrzem swiata w historii Formuly 1",
            "subtitle": "Maja 20 lat i 68 dni mlodzieniec Mercedesa pobija rekord Sebastiana Vettela i zdobywa tytul mistrzowski 2026.",
            "excerpt": "Kimi Antonelli przypieczetowal w niedziele mistrzostwo swiata F1, konczac wyscig w Meksyku na drugim stopniu podium.",
            "body": [
                "W niedziele 1 listopada tor Autodromo Hermanos Rodriguez byl swiadkiem wiekopomnego wydarzenia. Kimi Antonelli minal linie mety na drugim miejscu za Charlesem Leclerkiem i zapewnil sobie tytul mistrza swiata kierowcow F1 2026 roku.",
                "Wloch prowadzil po starcie z pole position, po czym bezblednie dowiozl drugie miejsce. Leclerc wygral dla Ferrari, ale bohaterem dnia zostal Antonelli, stajac sie pierwszym wloskim mistrzem od Alberto Ascariego w 1953 roku i najmlodszym czempionem w dziejach motorsportu."
            ]
        },
        "zh": {
            "title": "F1墨西哥大奖赛：安东内利屈居亚军仍提前加冕，刷新维特尔纪录成F1史上最年轻世界冠军",
            "subtitle": "20岁零68天！梅赛德斯意大利超新星紧随勒克莱尔冲线，提前三站锁定2026年度车手总冠军。",
            "excerpt": "基米·安东内利周日在墨西哥城以亚军完赛，正式登顶2026赛季F1世界冠军宝座，书写历史神迹。",
            "body": [
                "11月1日周日下午，墨西哥城罗德里格斯赛道见证了F1全新历史的诞生。年仅20岁零68天的梅赛德斯新秀基米·安东内利在71圈正赛中稳健完赛收获亚军，正式提前锁定2026年F1车手世界总冠军。",
                "法拉利车手勒克莱尔夺得分站冠军，但领奖台上最大的焦点属于安东内利。他以打破维特尔16年前纪录的姿态，成为F1历史上最年轻的年度世界冠军，也是自1953年传奇车手阿斯卡里之后首位加冕F1世界冠军的意大利人。"
            ]
        },
        "ja": {
            "title": "F1メキシコGP：アントネッリが2位フィニッシュで史上最年少ワールドチャンピオンに輝く",
            "subtitle": "20歳68日！メルセデスの至宝がルクレールに次ぐ表彰台でベッテルの記録を塗り替え2026年王座戴冠。",
            "excerpt": "キミ・アントネッリが日曜日のメキシコGPで2位に入り、F1史上最年少での年間ワールドチャンピオン獲得を決めました。",
            "body": [
                "11月1日日曜日、エルマノス・ロドリゲス・サーキットでF1の歴史が塗り替えられました。メルセデスの20歳キミ・アントネッリがルクレールに続く2位でチェッカーを受け、2026年のドライバーズ世界王者に輝きました。",
                "フェラーリのルクレールが今季5勝目を飾る中、アントネッリは冷静沈着なドライビングで必要なポイントを獲得。セバスチャン・ベッテルの史上最年少記録を更新し、1953年のアルベルト・アスカリ以来となるイタリア人世界王者が誕生しました。"
            ]
        },
        "ko": {
            "title": "F1 멕시코 GP: 키미 안토넬리 2위 완주로 역대 최연소 F1 월드 챔피언 등극",
            "subtitle": "20세 68일! 메르세데스 신예, 르클레르에 이어 준우승하며 페텔의 기록 깨고 2026년 세계 챔피언 확정.",
            "excerpt": "키미 안토넬리가 멕시코시티에서 2위로 결승선을 통과하며 F1 역사상 가장 어린 나이에 세계 챔피언에 올랐습니다.",
            "body": [
                "11월 1일 일요일 멕시코시티 엘마노스 로드리게스 서킷에서 새로운 모터스포츠 전설이 탄생했습니다. 메르세데스의 20세 드라이버 키미 안토넬리가 샤를 르클레르에 이어 2위를 차지하며 2026 F1 월드 챔피언 타이틀을 확정지었습니다.",
                "르클레르가 페라리에 우승을 안긴 가운데, 안토넬리는 안정적인 레이스 운영으로 18점을 추가했습니다. 이로써 안토넬리는 2010년 페텔의 최연소 기록을 3년 이상 앞당겼으며, 1953년 알베르토 아스카리 이후 73년 만에 이탈리아 출신 월드 챔피언이 되었습니다."
            ]
        },
        "ar": {
            "title": "جائزة المكسيك الكبرى: كيمي أنتونيللي ينهي السباق ثانيا خلف لوكلير ويصبح أصغر بطل عالم في تاريخ الفورمولا 1",
            "subtitle": "في عمر 20 عاما و68 يوما، سائق مرسيدس الإيطالي يحطم رقم فيتيل ويتوج بلقب بطولة العالم لعام 2026 رسميا.",
            "excerpt": "دخل الإيطالي الشاب كيمي أنتونيللي التاريخ من أوسع أبوابه يوم الأحد بحسمه لقب بطولة العالم للفورمولا 1 في المكسيك.",
            "body": [
                "شهدت حلبة هيرمانوس رودريغيز يوما للتاريخ يوم الأحد 1 نوفمبر بتتويج السائق الإيطالي كيمي أنتونيللي بلقب بطولة العالم لسائقي الفورمولا 1 لعام 2026 بعد إنهائه السباق في المركز الثاني خلف شارل لوكلير.",
                "وقاد سائق مرسيدس الشاب سباقا تكتيكيا هادئا ضمن له اللقب العالمي قبل 3 جولات من النهاية. وبات أنتونيللي أصغر بطل عالم في تاريخ الفورمولا 1 بعمر 20 عاما و68 يوما، ليكسر رقم سيباستيان فيتيل القياسي ويصبح أول إيطالي يتوج باللقب منذ ألبرتو أسكاري عام 1953."
            ]
        }
    },
    "pga-tour-mexico-open-2026-final-pereda-historic-triumph-vidanta": {
        "fr": {
            "title": "PGA Tour VidantaWorld Mexico Open : Raul Pereda vainqueur historique avec une derniere carte de 66",
            "subtitle": "Le heros local s'impose avec deux coups d'avance sur Austin Smotherman a -17 devant un public en transe a Puerto Vallarta.",
            "excerpt": "Raul Pereda a fait chavirer le Mexique dimanche en devenant le premier golfeur mexicain a remporter l'Open du Mexique sur le PGA Tour.",
            "body": [
                "L'emotion a submerge Puerto Vallarta ce dimanche 1er novembre. En signant une somptueuse carte de 66 (-5), le Mexicain Raul Pereda a remporte le VidantaWorld Mexico Open avec un total de 17 sous le par (267 coups).",
                "Pereda a depasse le leader Austin Smotherman grace a un retour tonitruant marque par des birdies aux trous 15 et 17. Le joueur de 29 ans devient le premier Mexicain de l'ere moderne du PGA Tour a soulever le trophee national, declenchant des scenes de liesse populaires a VidantaVallarta."
            ]
        },
        "es": {
            "title": "PGA Tour VidantaWorld Mexico Open: Raul Pereda hace historia con un 66 y se corona campeon en casa",
            "subtitle": "El veracruzano remonta con tres birdies en los ultimos cuatro hoyos para superar por dos golpes a Austin Smotherman (-17).",
            "excerpt": "Raul Pereda desato la locura en VidantaVallarta este domingo al conquistar el Mexico Open y firmar el triunfo mas emotivo de su carrera.",
            "body": [
                "El golf mexicano vivio su dia mas glorioso este domingo 1 de noviembre. El veracruzano Raul Pereda firmo una tarjeta final de 66 golpes (-5) para ganar el VidantaWorld Mexico Open con un acumulado de 17 bajo par (267).",
                "Pereda supero a Austin Smotherman en una ronda final electrizante gracias a sus birdies en el 15 y el 17. Ante mas de 28.000 aficionados entregados al grito de Viva Mexico, Pereda rompio a llorar en el green del 18 al convertirse en el primer jugador azteca en ganar este torneo dentro del circuito PGA Tour."
            ]
        },
        "de": {
            "title": "PGA Tour Mexico Open: Raul Pereda schreibt mit 66er-Finalrunde Geschichte und siegt in der Heimat",
            "subtitle": "Mexikanischer Nationalheld triumphiert mit 17 unter Par und zwei Schlaegen Vorsprung vor Austin Smotherman.",
            "excerpt": "Raul Pereda feierte am Sonntag bei den VidantaWorld Mexico Open den emotionalsten Sieg seiner Karriere vor heimischem Publikum.",
            "body": [
                "Großer Jubel in Puerto Vallarta: Der 29-jaehrige Mexikaner Raul Pereda gewann am Sonntag, den 1. November, mit einer famosen 66er-Schlussrunde (-5) und insgesamt 17 unter Par (267) die VidantaWorld Mexico Open.",
                "Pereda fing den bisherigen Spitzenreiter Austin Smotherman mit drei Birdies auf den letzten vier Loechern ab. Er ist der erste mexikanische Sieger der Mexico Open in der modernen PGA-Tour-Aera und sicherte sich neben dem Preisgeld auch die Startberechtigung fuer die Masters 2027."
            ]
        },
        "it": {
            "title": "PGA Tour Mexico Open: Raul Pereda nella storia, trionfo casalingo a -17 con un giro finale da 66 colpi",
            "subtitle": "Il beniamino di casa piega Austin Smotherman di due colpi mandando in visibilio i 28.000 spettatori di VidantaVallarta.",
            "excerpt": "Raul Pereda fa impazzire il Messico conquistando il VidantaWorld Mexico Open al termine di una domenica memorabile.",
            "body": [
                "Domenica 1 novembre indimenticabile a VidantaVallarta. Raul Pereda ha scritto la storia del golf messicano conquistando il VidantaWorld Mexico Open con uno score finale di 17 sotto il par (267 colpi).",
                "Con un ultimo giro superbo da 66 colpi (-5), Pereda ha superato l'americano Austin Smotherman grazie ai birdie decisivi alle buche 15 e 17. E il primo giocatore messicano a vincere il torneo da quando fa parte del circuito PGA Tour."
            ]
        },
        "pl": {
            "title": "PGA Tour Mexico Open: Raul Pereda pisze historie po rundzie 66 i wygrywa przed wlasna publicznoscia",
            "subtitle": "Meksykanski bohater triumfuje z wynikiem -17, pokonujac Austina Smothermana o dwa uderzenia w Puerto Vallarta.",
            "excerpt": "Raul Pereda zostal pierwszym w historii Meksykaninem, ktory wygral Mexico Open w ramach prestizowego cyklu PGA Tour.",
            "body": [
                "Meksykanscy kibice przezyli w niedziele 1 listopada chwile euforii. 29-letni Raul Pereda po znakomitej rundzie z wynikiem 66 (-5) wygral turniej VidantaWorld Mexico Open z lacznym rezultatem 17 ponizej par (267 uderzen).",
                "Pereda wyprzedzil dotychczasowego lidera Austina Smothermana o dwa uderzenia dzieki rewelacyjnej koncowce i birdie na 15. i 17. dolku. Zwyciestwo daje mu dwuletnia karte w PGA Tour oraz awans do turnieju Masters 2027."
            ]
        },
        "zh": {
            "title": "美巡赛墨西哥公开赛：佩雷达决赛轮狂飙66杆夺冠创造历史，本土首冠引爆全场狂欢",
            "subtitle": "29岁墨西哥本土名将总成绩-17杆（267杆）反超斯莫瑟曼两杆夺冠，锁定2027美国大师赛门票。",
            "excerpt": "劳尔·佩雷达周日在巴亚尔塔港打出完美的66杆，成为美巡赛历史上首位在本土夺冠的墨西哥球手。",
            "body": [
                "11月1日周日，墨西哥高尔夫迎来史上最激动人心的篇章。本土名将劳尔·佩雷达在维丹塔世界墨西哥公开赛决赛轮抓下6只小鸟交出66杆（-5），以四轮总成绩267杆（-17）两杆优势逆转击败斯莫瑟曼夺冠。",
                "佩雷达在后九洞展现大心脏，在第15洞与第17洞命中关键小鸟球锁定胜局。当他在第18洞推进保帕推杆后热泪盈眶，成为美巡赛进驻该赛事以来首位捧得国家公开赛奖杯的墨西哥人。"
            ]
        },
        "ja": {
            "title": "PGAツアー メキシコ・オープン：ペレダが66の猛チャージで劇的逆転優勝、地元メキシコ勢初の快挙",
            "subtitle": "通算17アンダーでスモーザーマンを2打差で下し悲願達成；2万8千人の大観衆が歓喜の涙。",
            "excerpt": "ラウル・ペレダが日曜日の最終ラウンドで66をマークし、PGAツアー史上初となる地元メキシコ勢の大会制覇を成し遂げました。",
            "body": [
                "11月1日日曜日、ヴィダンタ・バジャルタは熱狂の渦に包まれました。地元メキシコのラウル・ペレダが最終日に5アンダー66を叩き出し、通算17アンダー267で大逆転優勝を飾りました。",
                "1打差を追ってスタートしたペレダは15番と17番で圧巻のバーディを沈め、首位のスモーザーマンを逆転。18番でパットを沈めると涙を流し、メキシコ男子ゴルフ史に新たな金字塔を打ち立てました。"
            ]
        },
        "ko": {
            "title": "PGA 투어 멕시코 오픈: 라울 페레다 최종일 66타 대역전승, 멕시코인 최초 홈 우승 금자탑",
            "subtitle": "합계 17언더파로 오스틴 스모더먼 2타 차 제치고 감격의 PGA 투어 첫 승; 2027 마스터스 출전권 획득.",
            "excerpt": "라울 페레다가 일요일 비단타바야르타에서 66타를 몰아치며 멕시코 골프 역사상 최초로 자국 오픈 우승을 달성했습니다.",
            "body": [
                "11월 1일 일요일 멕시코 바야르타에서 멕시코 골프 역사상 가장 위대한 순간이 연출됐습니다. 29세의 라울 페레다가 최종 4라운드에서 5언더파 66타를 휘두르며 최종 합계 17언더파 267타로 우승 트로피를 들어올렸습니다.",
                "선두 스모더먼에 1타 뒤진 채 출발한 페레다는 후반 15번과 17번 홀에서 결정적인 버디를 낚으며 경기를 뒤집었습니다. 18번 홀에서 파를 지키며 우승을 확정한 페레다는 눈물을 흘리며 홈 갤러리의 뜨거운 환호를 받았습니다."
            ]
        },
        "ar": {
            "title": "جولة بي جي إيه بطولة المكسيك المفتوحة: راؤول بيريدا يصنع التاريخ ويتوج باللقب بعد جولة ختامية بـ 66 ضربة",
            "subtitle": "البطل المكسيكي يسجل 17 تحت المعدل ويتفوق بضربتين على سموذر مان وسط احتفالات هستيرية في فيدانتا فايارتا.",
            "excerpt": "حقق المكسيكي راؤول بيريدا إنجازا تاريخيا يوم الأحد بفوزه بلقب بطولة المكسيك المفتوحة للجولف على أرضه ووسط جماهيره.",
            "body": [
                "عاشت جماهير الجولف المكسيكية يوما تاريخيا لا ينسى يوم الأحد 1 نوفمبر بتتويج ابن بلادها راؤول بيريدا بلقب بطولة فيدانتا وورلد المكسيك المفتوحة بعد أن سجل 66 ضربة (-5) في الجولة الأخيرة ليصل إلى مجموع 17 تحت المعدل (267 ضربة).",
                "وتفوق بيريدا على الأمريكي أوستن سموذر مان بفارق ضربتين بفضل ضربات بيردي حاسمة في الحفرتين 15 و17. وأصبح بيريدا أول لاعب مكسيكي يتوج بالبطولة الوطنية في العصر الحديث لجولة بي جي إيه ليضمن مقعده في بطولة الماسترز لعام 2027."
            ]
        }
    },
    "nfl-week8-vikings-beat-colts-24-17-undefeated-7-0-2026": {
        "fr": {
            "title": "NFL Semaine 8 : Les Vikings toujours invaincus (7-0) apres leur victoire 24-17 contre les Colts",
            "subtitle": "Sam Darnold distribue deux touchdowns a Justin Jefferson et la defense de Flores provoque trois pertes de balle.",
            "excerpt": "Minnesota reste la seule equipe invaincue de la NFL cette saison apres son succes 24-17 a domicile face a Indianapolis.",
            "body": [
                "Les Minnesota Vikings poursuivent leur sans-faute en 2026. Ce dimanche 1er novembre au U.S. Bank Stadium, les hommes de Kevin O'Connell ont dispose des Indianapolis Colts sur le score de 24-17 devant 67 157 spectateurs.",
                "Sam Darnold a ete imperial avec 274 yards et 2 touchdowns, tous deux captes par un Justin Jefferson etincelant (128 yards). La defense etouffante de Brian Flores a fait le reste en interceptant Anthony Richardson a deux reprises pour porter le bilan des Vikings a 7 victoires et 0 defaite."
            ]
        },
        "es": {
            "title": "NFL Semana 8: Los Vikings siguen invictos (7-0) tras superar 24-17 a los Colts con show de Darnold y Jefferson",
            "subtitle": "Sam Darnold conecta dos pases de anotacion con Justin Jefferson y la defensiva de Minnesota roba tres balones clave.",
            "excerpt": "Minnesota se mantiene como el unico equipo invicto de la NFL tras vencer este domingo 24-17 a los Indianapolis Colts.",
            "body": [
                "Los Minnesota Vikings confirmaron su condicion de equipo mas solido de la NFL este domingo 1 de noviembre al vencer 24-17 a los Indianapolis Colts en Minneapolis, alcanzando un registro perfecto de 7-0.",
                "El mariscal Sam Darnold firmo otro gran encuentro con 274 yardas y 2 touchdowns hacia su receptor estrella Justin Jefferson (128 yardas en 9 recepciones). La defensa orquestada por Brian Flores provoco tres perdidas de balon para sellar la victoria y liderar la division NFC Norte."
            ]
        },
        "de": {
            "title": "NFL Woche 8: Ungeschlagene Vikings bezwingen Colts mit 24:17 und stehen dank Darnold bei 7:0",
            "subtitle": "Sam Darnold wirft zwei Touchdowns auf Superstar Justin Jefferson; Vikings-Defense forciert drei Ballverluste.",
            "excerpt": "Die Minnesota Vikings bleiben nach dem 24:17-Erfolg ueber Indianapolis das einzige ungeschlagene Team der NFL.",
            "body": [
                "Die Minnesota Vikings sind in der NFL-Saison 2026 weiter das Maß aller Dinge. Am Sonntag, den 1. November, setzte sich das Team von Head Coach Kevin O'Connell mit 24:17 gegen die Indianapolis Colts durch und feierte den siebten Sieg im siebten Spiel.",
                "Quarterback Sam Darnold ueberzeugte mit 274 Yards und zwei Touchdown-Paessen auf Justin Jefferson, der 128 Receiving-Yards verbuchte. Die Verteidigung von Brian Flores fing Anthony Richardson zweimal ab und sicherte in der Schlussminute den perfekten 7:0-Start."
            ]
        },
        "it": {
            "title": "NFL Week 8: I Vikings restano imbattuti sul 7-0, Colts piegati 24-17 con la coppia Darnold-Jefferson",
            "subtitle": "Due touchdown sull'asse Darnold-Jefferson e tre palle recuperate dalla difesa di Flores lanciano Minnesota in vetta.",
            "excerpt": "Minnesota e l'unica squadra della NFL ancora senza sconfitte grazie al successo casalingo per 24-17 su Indianapolis.",
            "body": [
                "Continua la marcia trionfale dei Minnesota Vikings. Domenica 1 novembre al U.S. Bank Stadium, i padroni di casa hanno superato 24-17 gli Indianapolis Colts salendo sul 7-0 in classifica.",
                "Sam Darnold ha brillato con 274 yard e 2 mete per Justin Jefferson, autore di una gara magistrale da 128 yard. La difesa di Brian Flores ha chiuso ogni varco a Richardson nel finale, certificando il primato assoluto dei Vikings."
            ]
        },
        "pl": {
            "title": "NFL Tydzien 8: Niepokonani Vikings wygrywaja z Colts 24:17 i maja bilans 7-0 dzieki akcjom Darnolda i Jeffersona",
            "subtitle": "Dwa przylozenia duetu Darnold-Jefferson i trzy straty wymuszone przez obrone utrzymuja Minnesote na czele ligi.",
            "excerpt": "Minnesota Vikings pozostaja jedyna niepokonana druzyna w NFL po niedzielnym zwyciestwie 24:17 nad Indianapolis Colts.",
            "body": [
                "Minnesota Vikings potwierdzili swoja dominacje w NFL, pokonujac w niedziele 1 listopada Indianapolis Colts 24:17 przed wlasna publicznoscia i poprawiajac swoj bilans do nieskazitelnego 7-0.",
                "Sam Darnold rzucil 274 jardy i 2 przylozenia do Justina Jeffersona, ktory zlapal 9 pilek na 128 jardow. Obrona prowadzona przez Briana Floresa przechwycila dwa podania rywali i powstrzymala decydujaca probe Colts w czwartej kwarcie."
            ]
        },
        "zh": {
            "title": "NFL常规赛第8周：明尼苏达维京人24-17力克小马，7战全胜独步全联盟",
            "subtitle": "达诺德连线杰弗森砍下两记达阵，弗洛雷斯铁血防守制造3次球权转换锁定胜局。",
            "excerpt": "维京人队周日在主场以24-17力克印第安纳波利斯小马队，成为本赛季全联盟唯一保持不败的球队（7胜0负）。",
            "body": [
                "11月1日周日下午，明尼苏达维京人队在合众银行体育场以24-17力克印第安纳波利斯小马队，将赛季战绩刷新至全联盟独一无二的7胜0负。",
                "四分卫萨姆·达诺德发挥出色，全场31投23中轰下274码和2次达阵，两次均由外接手贾斯廷·杰弗森完成连线（9次接球128码）。防守协调员弗洛雷斯的战术彻底压制了小马四分卫理查森，全场送出4次擒杀并完成两次关键拦截。"
            ]
        },
        "ja": {
            "title": "NFL第8週：バイキングスが開幕7連勝、コルツを24-17で下しリーグ唯一の無敗を堅持",
            "subtitle": "QBダーノルドがエースWRジェファーソンへ2TDパス；強力ディフェンスが3ターンオーバーを奪取。",
            "excerpt": "ミネソタ・バイキングスが日曜日、コルツを24-17で下して開幕7勝0敗とし、NFL唯一の無敗チームとして快走しています。",
            "body": [
                "11月1日日曜日、U.S.バンク・スタジアムで行われた一戦で、ミネソタ・バイキングスがインディアナポリス・コルツを24-17で退け、開幕7連勝を飾りました。",
                "QBサム・ダーノルドが274ヤード、2タッチダウンを投げ、ターゲットのジャスティン・ジェファーソンが128ヤードを獲得。ブライアン・フローレス率いる強力守備陣が相手QBリチャードソンから2インターセプトを奪い、僅差のリードを守り抜きました。"
            ]
        },
        "ko": {
            "title": "NFL 8주차: 무패의 바이킹스, 콜츠 24-17로 꺾고 개막 7연승 질주",
            "subtitle": "샘 다놀드-저스틴 제퍼슨 2TD 합작과 플로레스 수비진의 3턴오버 유도로 전승 행진 고수.",
            "excerpt": "미네소타 바이킹스가 일요일 홈에서 인디애나폴리스 콜츠를 24-17로 제압하고 NFL 유일의 무패 팀(7승 0패)으로 남았습니다.",
            "body": [
                "11월 1일 일요일 미네아폴리스 U.S. 뱅크 스타디움에서 열린 경기에서 미네소타 바이킹스가 인디애나폴리스 콜츠를 24-17로 따돌렸습니다.",
                "쿼터백 샘 다놀드는 274야드 패싱과 2개의 터치다운을 기록했고, 와이드리시버 저스틴 제퍼슨이 128야드 2TD를 잡아내며 공격을 주도했습니다. 브라이언 플로레스의 질식 수비진은 상대 실책 3개를 유도하며 7승 무패로 NFC 북부지구 선두를 굳건히 지켰습니다."
            ]
        },
        "ar": {
            "title": "دوري كرة القدم الأمريكية الأسبوع 8: فايكنغز يحافظ على سجله خاليا من الهزائم (7-0) بعد الفوز 24-17 على كولتس",
            "subtitle": "سام دارنولد يسجل تمريرتي هبوط إلى جيفرسون ودفاع مينيسوتا يجبر الخصم على 3 خسائر للكرة.",
            "excerpt": "واصل مينيسوتا فايكنغز انطلاقته المثالية في دوري NFL بفوزه 24-17 على إنديانابوليس كولتس ليبقى الفريق الوحيد دون هزيمة.",
            "body": [
                "أكد مينيسوتا فايكنغز تفوقه التام في موسم 2026 يوم الأحد 1 نوفمبر بالفوز 24-17 على إنديانابوليس كولتس في ملعب يو إس بانك ستاديوم، ليصل إلى 7 انتصارات دون أي هزيمة.",
                "وقدم سام دارنولد أداء رائعا بتسجيله 274 ياردة وتمريرتي هبوط إلى النجم جاستن جيفرسون الذي حصد 128 ياردة، بينما فرض دفاع المدرب براين فلوريس حصارا محكما وتصدى لكرات حاسمة في الربع الأخير ليحسم الفوز."
            ]
        }
    },
    "atp-vienna-2026-alcaraz-sweeps-musetti-claims-austrian-title": {
        "fr": {
            "title": "Tournoi de Vienne finale : Carlos Alcaraz surclasse Lorenzo Musetti 6-3, 6-4 et s'offre le titre",
            "subtitle": "Le numero un mondial boucle une semaine parfaite sans perdre un set pour remporter son 6e trophee de l'annee 2026.",
            "excerpt": "Carlos Alcaraz a remporte le tournoi ATP 500 de Vienne dimanche en dominant Lorenzo Musetti en deux manches maitrisees.",
            "body": [
                "Carlos Alcaraz a couronne une semaine de reve en Autriche ce dimanche 1er novembre. En finale de l'Erste Bank Open, le prodige espagnol a domine l'Italien Lorenzo Musetti 6-3, 6-4 en 1 heure et 24 minutes a la Wiener Stadthalle.",
                "Alcaraz n'a pas cede le moindre set en cinq matchs dans le tournoi viennois, s'appuyant sur un service intouchable (88 % de points gagnes derriere sa premiere balle) et 28 coups gagnants. C'est son sixieme titre de la saison 2026 avant d'aborder le Rolex Paris Masters."
            ]
        },
        "es": {
            "title": "ATP Viena final: Carlos Alcaraz supera 6-3, 6-4 a Lorenzo Musetti y levanta la corona austriaca",
            "subtitle": "El murciano completa una semana immaculada sin perder un solo set para conquistar su sexto titulo del ano 2026.",
            "excerpt": "Carlos Alcaraz derroto con autoridad a Lorenzo Musetti en Viena y levanto el trofeo del Erste Bank Open este domingo.",
            "body": [
                "Carlos Alcaraz se proclamo campeon del torneo ATP 500 de Viena este domingo 1 de noviembre al vencer a Lorenzo Musetti por 6-3 y 6-4 en un partido de enorme precision y velocidad.",
                "El numero uno del mundo domino de principio a fin, firmando 28 golpes ganadores y sin ceder una sola oportunidad de quiebre. Alcaraz cierra el torneo sin ceder un solo set y suma su 18° titulo profesional a los 23 anos, consolidando su ventaja en la cima del ranking mundial."
            ]
        },
        "de": {
            "title": "Erste Bank Open Finale: Carlos Alcaraz besiegt Lorenzo Musetti 6:3, 6:4 und holt den Titel in Wien",
            "subtitle": "Weltranglistenerster bleibt im gesamten Turnier ohne Satzverlust und feiert seinen sechsten Turniersieg 2026.",
            "excerpt": "Carlos Alcaraz kroente sich am Sonntag in der Wiener Stadthalle mit einem 6:3, 6:4 ueber Lorenzo Musetti zum Champion.",
            "body": [
                "Carlos Alcaraz feierte am Sonntag, den 1. November, einen souveraenen Turniersieg bei den Erste Bank Open in Wien. Vor 9.800 Fans in der Wiener Stadthalle setzte sich der topgesetzte Spanier mit 6:3, 6:4 gegen den Italiener Lorenzo Musetti durch.",
                "Alcaraz dominierte das Endspiel mit 28 Winnern und musste keinen einzigen Breakball abwehren. Fuer den 23-Jaehrigen war es der sechste ATP-Titel der laufenden Saison 2026, den er ohne einen einzigen Satzverlust im Turnierverlauf unter Dach und Fach brachte."
            ]
        },
        "it": {
            "title": "ATP Vienna finale: Carlos Alcaraz supera Lorenzo Musetti 6-3, 6-4 e conquista il titolo austriaco",
            "subtitle": "Lo spagnolo chiude una settimana immacolata senza cedere set e festeggia il sesto trofeo del 2026.",
            "excerpt": "Carlos Alcaraz vince l'Erste Bank Open di Vienna superando Lorenzo Musetti in due set nella finale di domenica.",
            "body": [
                "Trionfo di Carlos Alcaraz nella finale dell'Erste Bank Open a Vienna domenica 1 novembre. Lo spagnolo ha battuto Lorenzo Musetti con il punteggio di 6-3, 6-4 in un'ora e 24 minuti di gioco impeccabile.",
                "Alcaraz ha chiuso il torneo senza perdere neppure un set, mettendo a referto 28 vincenti e l'88% di punti con la prima palla. Per Musetti un ottimo torneo, ma il numero uno del mondo ha dimostrato una superiorita schiacciante nei momenti caldi."
            ]
        },
        "pl": {
            "title": "ATP Wieden final: Carlos Alcaraz pokonuje Lorenzo Musettiego 6:3, 6:4 i wznosi puchar",
            "subtitle": "Lider rankingu zakonczyl caly turniej bez straty seta, zdobywajac swoj szosty tytul w sezonie 2026.",
            "excerpt": "Carlos Alcaraz wygral turniej ATP 500 w Wiedniu, pokonujac w niedzielnym finale Lorenzo Musettiego w dwoch setach.",
            "body": [
                "Carlos Alcaraz potwierdzil mistrzowska forme w niedziele 1 listopada, wygrywajac turniej Erste Bank Open w Wiedniu po zwyciestwie 6:3, 6:4 nad Wlochem Lorenzo Musettim.",
                "Hiszpan byl bezbledny przy wlasnym serwisie, nie bronic ani jednego break pointa i posylajac 28 uderzen konczacych. To szosty tytul Alcaraza w 2026 roku, zdobyty bez straty chocby jednego seta w pieciu rozegranych meczach."
            ]
        },
        "zh": {
            "title": "ATP维也纳站决赛：阿尔卡拉斯6-3、6-4完胜穆塞蒂加冕，不失一盘夺今年第6冠",
            "subtitle": "世界第一一发得分率高达88%全场零破发点，耗时84分钟捧得维也纳赛男单冠军奖杯。",
            "excerpt": "阿尔卡拉斯在周日的维也纳决赛中直落两盘击败穆塞蒂，完美包揽整周比赛冠军并不丢一盘。",
            "body": [
                "11月1日周日，维也纳斯塔德哈勒体育馆9800名观众共同见证了阿尔卡拉斯的统治级表现。在维也纳公开赛决赛中，世界第一阿尔卡拉斯耗时84分钟以6-3、6-4击败意大利名将穆塞蒂，捧起冠军奖杯。",
                "阿尔卡拉斯整场轰出28记制胜分且未送出任何破发点，全周5场比赛未失一盘。这是阿尔卡拉斯本赛季斩获的第6座巡回赛单打冠军，也是他职业生涯第18冠，将世界第一的领先优势进一步扩大。"
            ]
        },
        "ja": {
            "title": "ATPウィーン決勝：アルカラスがムゼッティを6-3、6-4で圧倒し全試合ストレート勝ちで戴冠",
            "subtitle": "世界1位のアルカラスがファーストサーブ獲得率88％を記録し、今季ツアー6勝目をマーク。",
            "excerpt": "カルロス・アルカラスが日曜日のウィーン決勝でムゼッティを下し、1セットも落とさずに大会制覇を果たしました。",
            "body": [
                "11月1日日曜日、オーストリアのウィーンで行われたエルステ・バンク・オープン男子シングルス決勝で、カルロス・アルカラスがロレンツォ・ムゼッティを6-3、6-4で下して優勝を飾りました。",
                "アルカラスは28本のウィナーを決め、ブレークポイントを1度も許さない完璧な内容で84分で勝利。今大会5試合すべてストレート勝ちで飾り、今季6勝目、通算18個目のタイトルを獲得しました。"
            ]
        },
        "ko": {
            "title": "ATP 빈 오픈 결승: 카를로스 알카라스, 무세티 6-3 6-4 완파하고 무실세트 우승",
            "subtitle": "세계 1위 알카라스, 단 하나의 세트도 내주지 않고 시즌 6번째 투어 우승 트로피 획득.",
            "excerpt": "알카라스가 일요일 빈 오픈 결승에서 무세티를 꺾고 대회 내내 단 한 세트도 잃지 않는 압도적 우승을 차지했습니다.",
            "body": [
                "11월 1일 일요일 오스트리아 빈에서 열린 ATP 500 대회 결승에서 세계 1위 카를로스 알카라스가 이탈리아의 로렌초 무세티를 6-3, 6-4로 제압하고 정상에 올랐습니다.",
                "알카라스는 88%의 첫 서브 득점률과 28개의 위너를 뿜어내며 단 한 번의 브레이크 위기 없이 84분 만에 경기를 끝냈습니다. 이번 대회 5경기를 모두 무실세트로 마친 알카라스는 올 시즌 6번째이자 통산 18번째 투어 단독 타이틀을 거머쥐었습니다."
            ]
        },
        "ar": {
            "title": "بطولة فيينا للتنس النهائي: كارلوس ألكاراز يهزم لورينزو موسيتي 6-3 و6-4 ويتوج باللقب دون خسارة أي مجموعة",
            "subtitle": "المصنف الأول عالميا يحقق لقبه السادس في عام 2026 بعد عرض مثالي في العاصمة النمساوية.",
            "excerpt": "توج الإسباني كارلوس ألكاراز بلقب بطولة فيينا المفتوحة يوم الأحد بعد فوزه المستحق بمجموعتين دون رد على موسيتي.",
            "body": [
                "أكد الإسباني كارلوس ألكاراز هيمنته التامة على ملاعب التنس بتتويجه بلقب بطولة فيينا الدولية يوم الأحد 1 نوفمبر إثر فوزه في النهائي على الإيطالي لورينزو موسيتي بنتيجة 6-3 و6-4 في 84 دقيقة.",
                "وحقق ألكاراز اللقب دون أن يخسر أي مجموعة في مبارياته الخمس طوال الأسبوع، مسجلا 28 ضربة قاضية دون مواجهة أي نقطة لكسر إرساله، ليرفع رصيده إلى 6 ألقاب في موسم 2026 و18 لقبا في مسيرته الاحترافية."
            ]
        }
    },
    "nba-thunder-edge-clippers-116-109-sga-36-points-2026": {
        "fr": {
            "title": "NBA dimanche : Shai Gilgeous-Alexander marque 36 points et le Thunder bat les Clippers 116-109",
            "subtitle": "Le champion en titre reste parfait a 4-0 grace au sang-froid de son meneur canadien dans le dernier quart a Los Angeles.",
            "excerpt": "Oklahoma City s'est impose 116-109 sur le parquet des Clippers dimanche soir avec un SGA decisif dans le money-time.",
            "body": [
                "Le champion en titre de la NBA a montre toute sa force de caractere ce dimanche 1er novembre a l'Intuit Dome. Emmenes par un Shai Gilgeous-Alexander magistral (36 points, 9 passes, 6 rebonds), les Oklahoma City Thunder ont domine les Los Angeles Clippers 116-109.",
                "A 102-102 a trois minutes de la sirene, SGA a inscrit 14 points dans le quatrieme quart-temps pour forcer la decision face a Kawhi Leonard (27 points). Chet Holmgren a ajoute 18 points et 4 contres pour permettre au Thunder de demarrer sa saison sur un 4-0 parfait."
            ]
        },
        "es": {
            "title": "NBA domingo: Shai Gilgeous-Alexander firma 36 puntos y el campeon Thunder vence 116-109 a Clippers",
            "subtitle": "Oklahoma City se mantiene invicto con 4-0 tras una actuacion colosal de su estrella canadiense en el Intuit Dome.",
            "excerpt": "Shai Gilgeous-Alexander anoto 36 puntos para liderar la victoria de los Thunder por 116-109 ante los Clippers en Los Angeles.",
            "body": [
                "Los vigentes campeones de la NBA volvieron a dar un golpe sobre la mesa este domingo 1 de noviembre en Inglewood. El Oklahoma City Thunder supero 116-109 a Los Angeles Clippers apoyado en una noche sublime de Shai Gilgeous-Alexander.",
                "El base canadiense registro 36 puntos, 9 asistencias y 6 rebotes, anotando 14 puntos vitales en el ultimo periodo para desarticular la resistencia de Kawhi Leonard (27 puntos). Con el apoyo defensivo de Chet Holmgren (4 tapones), OKC se coloca con un inmaculado 4-0."
            ]
        },
        "de": {
            "title": "NBA Sonntag: Shai Gilgeous-Alexander erzielt 36 Punkte beim 116:109 des Meisters Thunder gegen die Clippers",
            "subtitle": "Oklahoma City bleibt mit 4:0 ungeschlagen dank einer herausragenden Schlussphase von SGA im Intuit Dome.",
            "excerpt": "Titelverteidiger Oklahoma City Thunder bezwang die LA Clippers am Sonntag mit 116:109 dank 36 Punkten von Gilgeous-Alexander.",
            "body": [
                "Die Oklahoma City Thunder untermauerten am Sonntag, den 1. November, ihren Status als Meister. Angefuehrt von Shai Gilgeous-Alexander, der 36 Punkte und 9 Assists verbuchte, siegte OKC mit 116:109 bei den Los Angeles Clippers.",
                "SGA erzielte 14 seiner Punkte im Schlussviertel und entschied das packende Duell gegen Kawhi Leonard (27 Punkte). Chet Holmgren ueberzeugte mit 18 Punkten und 4 Blocks, womit die Thunder die Tabelle im Westen mit 4:0 Siegen anfuehren."
            ]
        },
        "it": {
            "title": "NBA domenica: Shai Gilgeous-Alexander ne mette 36 e i campioni Thunder espugnano i Clippers 116-109",
            "subtitle": "Oklahoma City vola sul 4-0 grazie ai canestri decisivi della sua stella nel finale caldo all'Intuit Dome.",
            "excerpt": "Shai Gilgeous-Alexander firma 36 punti e 9 assist nel successo dei campioni NBA Thunder sui Clippers a Los Angeles.",
            "body": [
                "Grande prova di forza dei campioni in carica di Oklahoma City domenica sera 1 novembre. Il Thunder ha espugnato il nuovissimo Intuit Dome superando i Los Angeles Clippers per 116-109.",
                "Shai Gilgeous-Alexander e stato immarcabile con 36 punti (14 nell'ultimo quarto) e 9 assistenze. A nulla sono valsi i 27 punti di Kawhi Leonard per i padroni di casa: con Holmgren autore di 4 stoppate, OKC mantiene la testa della Western Conference sul 4-0."
            ]
        },
        "pl": {
            "title": "NBA niedziela: Shai Gilgeous-Alexander rzuca 36 punktow, a mistrzowie Thunder pokonuja Clippers 116:109",
            "subtitle": "Oklahoma City ma bilans 4-0 po wysmienitym wystepie kanadyjskiego lidera w Intuit Dome w Los Angeles.",
            "excerpt": "Shai Gilgeous-Alexander poprowadzil obroncow tytulu Thunder do wygranej 116:109 nad Clippers, zdobywajac 36 punktow.",
            "body": [
                "Oklahoma City Thunder udowodnili swoja klase mistrzowska w niedziele 1 listopada w Los Angeles. Druzyna z Oklahomy pokonala Clippers 116:109 po porywajacym meczu w nowej hali Intuit Dome.",
                "Shai Gilgeous-Alexander rzucil 36 punktow i mial 9 asyst, brylujac w koncowce z 14 punktami w czwartej kwarcie. Chet Holmgren dolozyl 18 punktow i 4 bloki, a Thunder pozostaja niepokonani na starcie sezonu z bilansem 4-0."
            ]
        },
        "zh": {
            "title": "NBA常规赛周日：亚历山大狂砍36分9助攻制胜，卫冕冠军雷霆116-109力克快船豪取4连胜",
            "subtitle": "SGA末节独揽14分浇灭快船反扑，霍姆格伦送出4次大帽，雷霆全胜领跑西部积分榜。",
            "excerpt": "亚历山大周日晚在洛杉矶打出MVP级表现轰下36分，带领卫冕冠军雷霆以116-109击败快船队。",
            "body": [
                "11月1日周日晚，卫冕冠军俄克拉荷马城雷霆队做客英格尔伍德直觉穹顶球馆，以116-109力克洛杉矶快船队，赛季开局取得四战全胜。",
                "雷霆当家球星谢伊·吉尔杰斯-亚历山大全场21投13中，砍下36分、9次助攻和6个篮板，并在第四节决胜时刻独得14分。霍姆格伦贡献18分并送出4次封盖，助雷霆在客场顶住了莱昂纳德（27分）与哈登的反攻。"
            ]
        },
        "ja": {
            "title": "NBA日曜：SGAが36得点9アシストの無双、王者サンダーがクリッパーズを116-109で破り開幕4連勝",
            "subtitle": "第4クォーターに14得点を集中させたエースの活躍で接戦を制し、西地区単独首位をキープ。",
            "excerpt": "シェイ・ギルジャス・アレクサンダーが36得点をマークし、王者オクラホマシティ・サンダーが敵地で快勝しました。",
            "body": [
                "11月1日日曜日、ロサンゼルスで行われたNBA公式戦で、昨季王者オクラホマシティ・サンダーがロサンゼルス・クリッパーズを116-109で退けました。",
                "大黒柱のシェイ・ギルジャス・アレクサンダーが36得点、9アシストと大車輪の活躍をみせ、勝負の第4クォーターだけで14得点を奪取。チェット・ホルムグレンも4ブロックとゴール下を死守し、サンダーが開幕4連勝を飾りました。"
            ]
        },
        "ko": {
            "title": "NBA 일요일: 샤이 길저스-알렉산더 36점 폭발, 디펜딩 챔피언 썬더 클리퍼스 116-109 격파",
            "subtitle": "4쿼터에만 14점을 몰아친 SGA의 클러치 활약으로 오클라호마시티 개막 4연승 질주.",
            "excerpt": "SGA가 36점 9어시스트를 기록하며 오클라호마시티 썬더를 클리퍼스전 116-109 승리로 이끌었습니다.",
            "body": [
                "11월 1일 일요일 인튜이트 돔에서 열린 NBA 경기에서 오클라호마시티 썬더가 LA 클리퍼스를 116-109로 꺾고 개막 4연승을 달렸습니다.",
                "샤이 길저스-알렉산더는 36점 9어시스트 6리바운드를 기록했고 4쿼터 막판 14점을 쏟아부으며 카와이 레너드(27점)가 분전한 클리퍼스를 제압했습니다. 쳇 홈그렌도 18점 4블록으로 골밑을 장악했습니다."
            ]
        },
        "ar": {
            "title": "دوري السلة الأمريكي الأحد: شاي غيلجيوس-ألكسندر يسجل 36 نقطة ويقود حامل اللقب ثاندر للفوز على كليبرز 116-109",
            "subtitle": "أوكلاهوما سيتي يحافظ على سجله المثالي 4-0 بفضل 14 نقطة حاسمة لنجمه في الربع الأخير بلوس أنجلوس.",
            "excerpt": "تألق النجم شاي غيلجيوس-ألكسندر بتسجيله 36 نقطة ليقود أوكلاهوما سيتي ثاندر لإسقاط لوس أنجلوس كليبرز.",
            "body": [
                "واصل حامل لقب دوري السلة الأمريكي أوكلاهوما سيتي ثاندر عروضه القوية مساء الأحد 1 نوفمبر بالفوز على لوس أنجلوس كليبرز 116-109 في صالة إنتويت دوم.",
                "وسجل النجم الكندي شاي غيلجيوس-ألكسندر 36 نقطة و9 تمريرات حاسمة، منها 14 نقطة في الربع الرابع الحاسم، ليحسم المواجهة أمام كواي ليونارد (27 نقطة) ويقود ثاندر لانتصاره الرابع على التوالي في صدارة القسم الغربي."
            ]
        }
    },
    "premier-league-mw9-chelsea-downs-newcastle-2-1-palmer-winner": {
        "fr": {
            "title": "Premier League J9 : Cole Palmer offre la victoire a Chelsea 2-1 contre Newcastle a Stamford Bridge",
            "subtitle": "Nicolas Jackson et Cole Palmer marquent pour les Blues qui rejoignent Liverpool au pied du podium avec 16 points.",
            "excerpt": "Chelsea a domine Newcastle 2-1 a Londres dimanche grace a un but splendide de Cole Palmer au retour des vestiaires.",
            "body": [
                "Chelsea a renoue avec le succes en Premier League ce dimanche 1er novembre en dominant Newcastle United 2-1 a Stamford Bridge dans une rencontre disputee a un rythme effrene.",
                "Nicolas Jackson a ouvert le score a la 18e minute a la conclusion d'un contre rapide, mais Alexander Isak a egalise pour les Magpies avant la pause. Au retour des vestiaires, l'incontournable Cole Palmer a fait lever la foule d'un tir puissant a l'entree de la surface. Chelsea grimpe a la 5e place avec 16 points."
            ]
        },
        "es": {
            "title": "Premier League J9: Cole Palmer firma un golazo para dar la victoria al Chelsea 2-1 sobre el Newcastle",
            "subtitle": "Nicolas Jackson y Palmer anotan para los Blues, que empatan con el Liverpool en la cuarta plaza con 16 puntos.",
            "excerpt": "El Chelsea vencio 2-1 al Newcastle United este domingo en Stamford Bridge con una brillante actuacion de Cole Palmer.",
            "body": [
                "El Chelsea se llevo tres puntos de oro este domingo 1 de noviembre en Stamford Bridge al superar 2-1 al Newcastle United en un choque vibrante.",
                "Nicolas Jackson abrio la cuenta en el minuto 18, pero Alexander Isak emparejo la contienda poco despues. Recien iniciada la segunda mitad, Cole Palmer mostro toda su clase con una conduccion letal y un disparo seco que batio a Nick Pope. El equipo de Enzo Maresca alcanza los 16 puntos en la tabla."
            ]
        },
        "de": {
            "title": "Premier League 9. Spieltag: Cole Palmer schiesst Chelsea zum 2:1-Sieg ueber Newcastle United",
            "subtitle": "Nicolas Jackson und Palmer treffen fuer die Blues, die mit 16 Punkten zu Liverpool aufschliessen.",
            "excerpt": "Chelsea behauptete sich am Sonntag an der Stamford Bridge mit 2:1 gegen Newcastle dank eines Treffers von Cole Palmer.",
            "body": [
                "Der FC Chelsea feierte am Sonntag, den 1. November, einen wichtigen 2:1-Heimsieg ueber Newcastle United. Vor 39.812 Zuschauern an der Stamford Bridge zeigten die Blues eine reife Leistung.",
                "Jackson brachte die Hausherren frueh in Fuehrung, Isak glich fuer die Gaeste aus. Kurz nach dem Wiederanpfiff erzielte Ausnahmekoenner Cole Palmer in der 47. Minute mit einem sehenswerten Distanzschuss den Siegtreffer. Chelsea klettert mit 16 Punkten auf Platz fuenf."
            ]
        },
        "it": {
            "title": "Premier League 9ª giornata: Cole Palmer decisivo, il Chelsea piega il Newcastle 2-1 a Stamford Bridge",
            "subtitle": "Jackson e Palmer regalano il successo ai Blues che agganciano il Liverpool a quota 16 punti.",
            "excerpt": "Il Chelsea batte 2-1 il Newcastle United grazie alla perla di Cole Palmer all'inizio del secondo tempo.",
            "body": [
                "Preziosa vittoria del Chelsea domenica 1 novembre a Stamford Bridge. I Blues di Enzo Maresca hanno sconfitto il Newcastle United per 2-1 in una sfida ad alta intensita.",
                "Dopo il vantaggio di Jackson e il pari di Isak, a decidere l'incontro e stato ancora una volta Cole Palmer con uno splendido sinistro al 47'. Il Chelsea sale a 16 punti in classifica agganciando il Liverpool al quarto posto."
            ]
        },
        "pl": {
            "title": "Premier League 9. kolejka: Cole Palmer daje Chelsea zwyciestwo 2:1 nad Newcastle na Stamford Bridge",
            "subtitle": "Nicolas Jackson i Cole Palmer strzelaja gole dla The Blues, ktorzy zrownuja sie punktami z Liverpoolem.",
            "excerpt": "Chelsea pokonala Newcastle United 2:1 w niedzielnym meczu ligi angielskiej po pieknym trafieniu Cole'a Palmera.",
            "body": [
                "Chelsea zdobyla wazne trzy punkty w niedziele 1 listopada, wygrywajac u siebie z Newcastle United 2:1. Bohaterem kibicow w Londynie zostal Cole Palmer.",
                "Wynik meczu otworzyl Nicolas Jackson w 18. minucie, lecz przed przerwa wyrownal Alexander Isak. Decydujacy cios zadal Palmer tuz po zmianie stron w 47. minucie, oddajac potezny strzal zza pola karnego. Chelsea ma na koncie 16 punktow."
            ]
        },
        "zh": {
            "title": "英超第9轮：帕尔默下半场开局破门锁定胜局，切尔西主场2-1力克纽卡斯尔联",
            "subtitle": "杰克逊与帕尔默建功，伊萨克破门难救主；蓝军积分升至16分追平利物浦。",
            "excerpt": "切尔西周日在斯坦福桥球场2-1力克纽卡斯尔联队，帕尔默打进制胜进球助球队重返前五。",
            "body": [
                "11月1日周日下午，切尔西坐镇斯坦福桥球场以2-1战胜纽卡斯尔联队。比赛第18分钟，佩德罗·内托助攻杰克逊推射破门首开纪录，伊萨克随后在第32分钟为客队扳平比分。",
                "下半场开场仅两分钟，核心帕尔默带球突施冷箭，左脚劲射近角破门打进个人本赛季联赛第7球。全场战罢，切尔西积16分升至积分榜第五位，在积分上追平了利物浦。"
            ]
        },
        "ja": {
            "title": "プレミアリーグ第9節：コール・パーマーの鮮烈な決勝点でチェルシーがニューカッスルに2-1で勝利",
            "subtitle": "ジャクソンとパーマーの得点で勝ち点3獲得；勝ち点16でリヴァプールと並び上位追走。",
            "excerpt": "チェルシーが日曜日、スタンフォード・ブリッジでニューカッスルを2-1で下し、パーマーが再び輝きを放ちました。",
            "body": [
                "11月1日日曜日、スタンフォード・ブリッジで行われたプレミアリーグ第9節で、チェルシーがニューカッスル・ユナイテッドを2-1で破りました。",
                "前半18分にジャクソンが先制ゴールを決め、イサクの同点弾で追いつかれるも、後半開始直後の47分にコール・パーマーが強烈な左足ミドルを突き刺して勝ち越し。チェルシーは勝ち点を16に伸ばしました。"
            ]
        },
        "ko": {
            "title": "프리미어리그 9R: 콜 파머 결승골 작렬, 첼시 뉴캐슬 2-1 꺾고 승점 16점 도약",
            "subtitle": "니콜라 잭슨 선제골과 파머의 47분 벼락 결승골로 스탬퍼드 브리지서 짜릿한 승리.",
            "excerpt": "첼시가 일요일 뉴캐슬 유나이티드를 2-1로 물리치며 리버풀과 동률인 승점 16점을 기록했습니다.",
            "body": [
                "11월 1일 일요일 스탬퍼드 브리지에서 열린 프리미어리그 9라운드 경기에서 첼시가 뉴캐슬 유나이티드를 2-1로 제압했습니다.",
                "전반 18분 잭슨의 골로 앞서간 첼시는 이삭에게 동점을 내줬으나, 후반 2분 콜 파머가 환상적인 왼발 슈팅으로 골망을 흔들며 결승골을 터뜨렸습니다. 첼시는 승점 16점으로 리버풀과 어깨를 나란히 했습니다."
            ]
        },
        "ar": {
            "title": "الدوري الإنجليزي الجولة 9: كول بالمر يسجل هدفا رائعا ويقود تشيلسي للفوز 2-1 على نيوكاسل في ستامفورد بريدج",
            "subtitle": "نيكولاس جاكسون وبالمر يمنحان البلوز ثلاث نقاط ثمينة ليرفع الفريق رصيده إلى 16 نقطة.",
            "excerpt": "تغلب تشيلسي على نيوكاسل يونايتد 2-1 يوم الأحد في لندن بفضل هدف حاسم من نجمه كول بالمر.",
            "body": [
                "حقق تشيلسي فوزا مستحقا على ضيفه نيوكاسل يونايتد بنتيجة 2-1 يوم الأحد 1 نوفمبر على ملعب ستامفورد بريدج ضمن الجولة التاسعة من الدوري الإنجليزي الممتاز.",
                "وافتتح نيكولاس جاكسون التسجيل للبلوز في الدقيقة 18، قبل أن يعادل ألكسندر إيساك النتيجة لنيوكاسل. وفي الدقيقة 47 من الشوط الثاني، أطلق كول بالمر تسديدة صاروخية سكنت الشباك لتمنح تشيلسي نقاط المباراة كاملة ويرفع رصيده إلى 16 نقطة."
            ]
        }
    }
}

# Strict validation
for slug, langs in NOV01_STORIES.items():
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

print("All November 1 story translations validated: 0 em-dashes and 0 double-hyphens.")

snippet_parts = []
for slug, langs in NOV01_STORIES.items():
    formatted_slug = json.dumps(slug)
    snippet_parts.append(f"{formatted_slug}: {json.dumps(langs, ensure_ascii=False, indent=2)},")

snippet = "\n".join(snippet_parts) + "\n"

stories_file = os.path.join(os.path.dirname(__file__), "../../frontend/src/i18n/stories.ts")
with open(stories_file, "r", encoding="utf-8") as f:
    content = f.read()

target = "export const STORY_I18N: Record<string, LocMap> = {\n"
assert target in content, "Target line not found in stories.ts"

new_content = content.replace(target, target + snippet, 1)

with open(stories_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully injected November 1 translations into frontend/src/i18n/stories.ts")
