# -*- coding: utf-8 -*-
import json
import re

OCT24_STORIES = {
    "premier-league-mw8-chelsea-vs-tottenham-derby-day-2026": {
        "fr": {
            "title": "Jour de derby a Stamford Bridge : Chelsea recoit les Spurs dans le choc londonien",
            "subtitle": "Tottenham vise un deuxieme succes consecitif apres sa remontee contre Coventry. Chelsea veut defendre sa place dans le top 4.",
            "excerpt": "La 8e journee de Premier League monte d'un cran ce samedi avec l'affiche entre Chelsea et Tottenham a Stamford Bridge. Vendredi, Ipswich et Forest se sont neutralises 1-1.",
            "body": [
                "L'affiche majeure de la 8e journee de Premier League se tient ce samedi 24 octobre, Chelsea accueillant son rival historique Tottenham Hotspur a Stamford Bridge a 17h30 UK. Les Blues abordent le week-end au quatrieme rang du classement avec 13 points (4-1-2), soucieux de rebondir apres de recents points perdus et de maintenir la pression sur le deuxieme Arsenal (18 points) et le leader Manchester City (21 points). L'entraineur Enzo Maresca a insiste sur l'intensite defensive face a une equipe des Spurs redoutable en transition rapide.",
                "Tottenham traverse la capitale avec un regain d'optimisme. La victoire spectaculaire 3-1 acquise lundi soir contre Coventry City a mis fin a une passe delicate et a hisse l'equipe d'Ange Postecoglou au 16e rang avec 6 points. Le retour au tableau d'affichage de James Maddison aux cotes d'Omar Marmoush a apporte l'etincelle attendue. Un succes samedi permettrait aux Spurs de se replacer en milieu de tableau et de signer leur premier succes a Stamford Bridge depuis 2018. Vendredi soir a Portman Road, Ipswich Town et Nottingham Forest se sont quittes sur un match nul 1-1 (buts de Williams a la 13e minute et d'Enciso a la 41e)."
            ]
        },
        "es": {
            "title": "Dia de derbi en el Bridge: Chelsea recibe a Spurs en el duelo de Londres",
            "subtitle": "Tottenham busca su segunda victoria seguida tras remontar ante Coventry. Chelsea quiere proteger su puesto en el top cuatro.",
            "excerpt": "La jornada 8 de la Premier League sube de temperatura el sabado con Chelsea frente a Tottenham en Stamford Bridge. El viernes, Ipswich y Forest empataron 1-1.",
            "body": [
                "El partido estelar de la jornada 8 de la Premier League llega este sabado 24 de octubre, cuando el Chelsea reciba a su clasico rival Tottenham Hotspur en Stamford Bridge a las 17:30 UK. Los Blues inician el fin de semana en el cuarto puesto de la tabla con 13 puntos (4-1-2), buscando recuperarse de puntos cedidos recientemente y mantener la presion sobre el sublider Arsenal (18 puntos) y el puntero Manchester City (21 puntos). El tecnico Enzo Maresca ha exigido rigor defensivo ante unos Spurs peligrosos al contraataque.",
                "El Tottenham viaja por Londres con optimismo renovado. La electrizante remontada 3-1 del lunes sobre Coventry City freno una racha negativa y coloco al conjunto de Ange Postecoglou en el puesto 16 con 6 puntos. James Maddison y Omar Marmoush brillaron en ataque aportando la chispa necesaria. Un triunfo el sabado impulsaria a los Spurs a la zona media y significaria su primera victoria en Stamford Bridge desde 2018. El viernes por la noche en Portman Road, Ipswich Town y Nottingham Forest igualaron 1-1 con tantos de Williams (13') y Enciso (41')."
            ]
        },
        "de": {
            "title": "Derby-Tag an der Bridge: Chelsea empfaengt Spurs zum London-Showdown",
            "subtitle": "Tottenham will zweiten Sieg in Serie nach Coventry-Aufholjagd. Chelsea verteidigt Platz unter den Top Vier.",
            "excerpt": "Der 8. Spieltag der Premier League gewinnt an Fahrt: Chelsea trifft an der Stamford Bridge auf Tottenham. Am Freitag trennten sich Ipswich und Forest 1-1.",
            "body": [
                "Das Topspiel des 8. Spieltags der Premier League steigt am Samstag, 24. Oktober: Der FC Chelsea empfaengt seinen Erzrivalen Tottenham Hotspur um 17:30 Uhr UK an der Stamford Bridge. Die Blues gehen als Tabellenvierter mit 13 Punkten (4-1-2) in die Partie und wollen nach juengsten Punktverlusten den Anschluss an Verfolger Arsenal (18 Punkte) und Spitzenreiter Manchester City (21 Punkte) halten. Cheftrainer Enzo Maresca forderte hoechste defensive Konzentration gegen konterstarke Spurs.",
                "Tottenham reist mit neuem Selbstvertrauen durch die Hauptstadt. Der emotionale 3-1-Comeback-Sieg am Montagabend gegen Coventry City beendete eine Durststrecke und brachte die Mannschaft von Ange Postecoglou mit 6 Punkten auf Rang 16. James Maddison und Omar Marmoush sorgten mit ihren Treffern fuer die noetige Durchschlagskraft. Ein Sieg an der Stamford Bridge waere fuer die Spurs der erste Auswaertserfolg dort seit 2018. Am Freitagabend trennten sich Ipswich Town und Nottingham Forest an der Portman Road mit 1-1 (Tore durch Williams 13. und Enciso 41.)."
            ]
        },
        "it": {
            "title": "Giorno di derby al Bridge: il Chelsea ospita gli Spurs nel duello di Londra",
            "subtitle": "Il Tottenham cerca il secondo successo di fila dopo la rimonta sul Coventry. Il Chelsea vuole blindare il quarto posto.",
            "excerpt": "L'8a giornata di Premier League si accende sabato con Chelsea contro Tottenham a Stamford Bridge. Venerdi Ipswich e Forest hanno pareggiato 1-1.",
            "body": [
                "La sfida di cartello dell'8a giornata di Premier League va in scena sabato 24 ottobre, con il Chelsea che ospita l'acerrimo rivale Tottenham Hotspur a Stamford Bridge alle 17:30 UK. I Blues affrontano il weekend al quarto posto con 13 punti (4-1-2), decisi a riscattare i recenti passi falsi e a tenere il passo del secondo Arsenal (18 punti) e del capolista Manchester City (21 punti). Il tecnico Enzo Maresca ha preteso massima intensita difensiva contro le rapide ripartenze degli Spurs.",
                "Il Tottenham attraversa Londra con ritrovata fiducia. L'emozionante successo in rimonta per 3-1 di lunedi sul Coventry City ha spezzato un momento difficile portando la squadra di Ange Postecoglou al 16° posto con 6 punti. James Maddison e Omar Marmoush hanno fatto la differenza sul tabellino dei marcatori. Una vittoria sabato spingerebbe gli Spurs verso meta classifica e regalerebbe il primo successo a Stamford Bridge dal 2018. Venerdi sera a Portman Road Ipswich Town e Nottingham Forest hanno impattato sull'1-1 con reti di Williams (13') ed Enciso (41')."
            ]
        },
        "pl": {
            "title": "Dzien derbow na the Bridge: Chelsea podejmuje Spurs w hicie Londynu",
            "subtitle": "Tottenham szuka drugiej wygranej z rzedu po powrocie z Coventry. Chelsea broni miejsca w czolowej czworce.",
            "excerpt": "8. kolejka Premier League nabiera rumiencow: Chelsea mierzy sie z Tottenhamem na Stamford Bridge. W piatek Ipswich zremisowalo z Forest 1-1.",
            "body": [
                "Glowne wydarzenie 8. kolejki Premier League przypada na sobote 24 pazdziernika, gdy Chelsea podejmie odwiecznego rywala Tottenham Hotspur na Stamford Bridge o 17:30 UK. The Blues przystepuja do spotkania na czwartej pozycji z 13 punktami (4-1-2), chcac zrehabilitowac sie po ostatnich potknieciach i wywrzec presje na wicelidera Arsenal (18 punktow) oraz lidera Manchester City (21 punktow). Menedzer Enzo Maresca wymagal pelnej dyscypliny defensywnej wobec groznych kontratakow Spurs.",
                "Tottenham przyjezdza na zachod Londynu z nowym entuzjazmem. Efektowne zwyciestwo 3-1 odniesione w poniedzialek nad Coventry City przerwalo zla passe i przesunelo zespol Ange Postecoglou na 16. miejsce z 6 punktami. James Maddison oraz Omar Marmoush dali impuls, ktorego druzyna pilnie potrzebowala. Zwyciestwo w sobote daloby Spurs awans do srodka tabeli i pierwsza wygrana na Stamford Bridge od 2018 roku. W piatkowym meczu otwarcia na Portman Road Ipswich Town zremisowalo 1-1 z Nottingham Forest po golach Williamsa (13') i Enciso (41')."
            ]
        },
        "zh": {
            "title": "斯坦福桥德比日：切尔西坐镇主场与热刺上演伦敦巅峰对决",
            "subtitle": "热刺逆转考文垂后力争连胜，切尔西全力捍卫积分榜前四位置。",
            "excerpt": "英超第8轮周六迎来重头戏，切尔西与热刺在斯坦福桥球场狭路相逢。周五揭幕战伊普斯维奇与森林1-1握手言和。",
            "body": [
                "英超第8轮焦点大战于10月24日周六上演，切尔西在英国时间17:30坐镇斯坦福桥球场迎战宿敌托特纳姆热刺。蓝军目前以13分（4胜1平2负）位居积分榜第四位，急需在近期丢分后重整旗鼓，紧追积18分的阿森纳和积21分的领头羊曼城。主帅马雷斯卡要求全队提高防守强度，严防热刺犀利的快速反击。",
                "热刺带着重燃的信心跨城出征。周一晚间3-1逆转战胜考文垂城，终结了近期的低迷表现，波斯特科格鲁的球队也以6分升至积分榜第16位。麦迪逊与马尔穆什双双建功，为球队进攻端注入活力。若能在周六全取三分，热刺不仅将重返积分榜中游，还将斩获自2018年以来在斯坦福桥的首场胜利。在周五率先进行的比赛中，伊普斯维奇在波特曼路与诺丁汉森林1-1战平，威廉姆斯第13分钟建功，恩西索第41分钟扳平。"
            ]
        },
        "ja": {
            "title": "スタンフォード・ブリッジの激突：チェルシーがロンドン決戦でトッテナムを迎撃",
            "subtitle": "トッテナムはコベントリー戦の逆転勝ちに続く連勝を狙う。チェルシーはトップ4死守へ。",
            "excerpt": "プレミアリーグ第8節は土曜に注目のロンドンダービーを開催。チェルシーがトッテナムと激突。金曜はイプスウィッチ対フォレストが1-1の引き分け。",
            "body": [
                "プレミアリーグ第8節の最注目カードが10月24日土曜にキックオフ。チェルシーが英国時間17:30からスタンフォード・ブリッジでトッテナム・ホットスパーを迎え撃ちます。ブルーズは勝点13（4勝1分2敗）の4位につけ、直近の取りこぼしを払拭し2位アーセナル（18点）と首位マンチェスター・シティ（21点）を追走したいところ。エンツォ・マレスカ監督はカウンターの鋭いトッテナム相手に守備の集中を厳命しています。",
                "一方のスパーズは自信を取り戻して敵地に乗り込みます。月曜夜にコベントリー・シティに3-1で逆転勝利を収め、ポステコグルー監督率いるチームは勝点6で16位へ浮上。ジェームズ・マディソンとオマル・マルムシュの得点が攻撃陣に活気をもたらしました。土曜に勝利すれば中位進出とともに2018年以来となるスタンフォード・ブリッジでの歓喜となります。なお金曜の開幕戦はポートマン・ロードでイプスウィッチとノッティンガム・フォレストが1-1で引き分けました（ウィリアムズ13分、エンシソ41分）。"
            ]
        },
        "ko": {
            "title": "스탬퍼드 브리지 더비 데이: 첼시와 토트넘의 런던 정면 승부",
            "subtitle": "토트넘 코번트리전 역전승에 이어 연승 정조준. 첼시는 리그 4위 수성 노린다.",
            "excerpt": "프리미어리그 8라운드 토요일 최고의 빅매치 첼시 대 토트넘 격돌. 금요일 개막전에서는 입스위치와 포레스트가 1-1로 비겼습니다.",
            "body": [
                "프리미어리그 8라운드 최고의 관심사인 런던 더비가 10월 24일 토요일 펼쳐집니다. 첼시는 영국 시간 17:30 스탬퍼드 브리지에서 오랜 라이벌 토트넘 홋스퍼를 상대합니다. 승점 13점(4승 1무 2패)으로 리그 4위에 랭크된 첼시는 최근 승점 실점을 만회하고 2위 아스널(18점)과 선두 맨체스터 시티(21점) 추격에 속도를 내야 합니다. 엔조 마레스카 감독은 토트넘의 빠른 역습에 대비해 강력한 수비 압박을 주문했습니다.",
                "토트넘 역시 분위기 반전에 성공했습니다. 지난 월요일 코번트리 시티를 상대로 3-1 짜릿한 역전승을 거두며 포스테코글루 감독의 팀은 승점 6점으로 16위까지 올라섰습니다. 제임스 매디슨과 오마르 마르무시의 득점포가 살아난 점이 고무적입니다. 토트넘이 토요일 승리를 챙길 경우 중위권 도약과 함께 2018년 이후 첫 스탬퍼드 브리지 원정 승리를 거두게 됩니다. 한편 금요일 밤 개막전에서는 입스위치 타운과 노팅엄 포레스트가 1-1 무승부를 기록했습니다."
            ]
        },
        "ar": {
            "title": "يوم الديربي في الستامفورد: تشيلسي يستضيف توتنهام في قمة لندن",
            "subtitle": "توتنهام يبحث عن فوزه الثاني تواليا بعد ريمونتادا كوفنتري. وتشيلسي يسعى لحماية موقعه بين الاربعة الاوائل.",
            "excerpt": "تشتعل الجولة الثامنة من الدوري الانجليزي الممتاز يوم السبت بقمة تشيلسي وتوتنهام في ستامفورد بريدج. ويوم الجمعة تعادل ايبسويتش مع فورست 1-1.",
            "body": [
                "تتجه انظار جماهير الكرة الانجليزية يوم السبت 24 اكتوبر الى ملعب ستامفورد بريدج، حيث يستضيف تشيلسي غريمه اللندني توتنهام هوتسبير في تمام الساعة 17:30 بتوقيت بريطانيا ضمن الجولة الثامنة من البريميرليغ. ويدخل البلوز اللقاء في المركز الرابع برصيد 13 نقطة (4-1-2)، متطلعين لاستعادة نغمة الانتصارات ومواصلة الضغط على ارسنال صاحب المركز الثاني (18 نقطة) والمتصدر مانشستر سيتي (21 نقطة). وشدد المدرب انزو ماريسكا على ضرورة الانضباط الدفاعي امام هجمات توتنهام المرتدة.",
                "في المقابل، يدخل توتنهام اللقاء بمعنويات مرتفعة بعد فوزه المثير 3-1 على كوفنتري سيتي مساء الاثنين الماضي، وهو ما رفع رصيد كتيبة انجي بوستيكوغلو الى 6 نقاط في المركز السادس عشر. وقدم جيمس ماديسون وعمر مرموش الاضافة الهجومية المطلوبة. وسيمنح الفوز يوم السبت توتنهام دفعة هائلة نحو منتصف الترتيب واول فوز في ستامفورد بريدج منذ عام 2018. وكانت الجولة قد افتتحت مساء الجمعة بتعادل ايبسويتش تاون ونوتينغهام فورست 1-1 في بورتمان رود (سجل ويليامز في الدقيقة 13 ورد انسيسو في الدقيقة 41)."
            ]
        }
    },
    "atp-saturday-almaty-basilashvili-stuns-tsitsipas-medvedev-final-2026": {
        "fr": {
            "title": "Basilashvili terrasse Tsitsipas a Almaty : Medvedev file en finale",
            "subtitle": "Nikoloz Basilashvili cree la surprise en trois manches. Daniil Medvedev rejoint la finale apres l'abandon de Bublik.",
            "excerpt": "Le qualifie Basilashvili cree la sensation contre Tsitsipas 6-4, 6-7, 6-3 pour atteindre la finale d'Almaty. La tete de serie numero un Medvedev passe sur abandon.",
            "body": [
                "Nikoloz Basilashvili a signe l'un des plus grands exploits de la saison automnale en salle ce samedi 24 octobre, dominant la tete de serie numero sept Stefanos Tsitsipas 6-4, 6-7(5), 6-3 en demi-finale de l'Open d'Almaty. Le qualifie georgien a fait parler la puissance de ses frappes du fond de court, claquant 32 coups gagnants au terme d'un combat intense de deux heures et 18 minutes. Malgre la perte du jeu decisif dans le deuxieme set, Basilashvili a repris sa marche en avant en breakant Tsitsipas a deux reprises dans l'ultime manche.",
                "Cette victoire consacre le retour au premier plan de Basilashvili, qui a franchi deux tours de qualifications avant d'ecarter Adrian Mannarino puis Tsitsipas pour disputer sa premiere finale sur le circuit ATP depuis 2022. Dans la seconde demi-finale, Daniil Medvedev s'est qualifie pour la finale apres l'abandon du heros local Alexander Bublik en raison d'une blessure au genou droit. Medvedev avait empoche la premiere manche 6-3 avant le retrait de son adversaire. La finale de dimanche opposera Medvedev a Basilashvili au Kazakhstan."
            ]
        },
        "es": {
            "title": "Basilashvili sorprende a Tsitsipas en Almaty: Medvedev avanza a la final",
            "subtitle": "Nikoloz Basilashvili da la campanada en tres sets. Daniil Medvedev avanza tras el retiro de Bublik.",
            "excerpt": "El clasificado Basilashvili supero 6-4, 6-7, 6-3 a Stefanos Tsitsipas para meterse en la final de Almaty. Medvedev avanzo por el abandono de Bublik.",
            "body": [
                "Nikoloz Basilashvili firmo una de las mayores sorpresas de la temporada bajo techo este sabado 24 de octubre al eliminar al septimo sembrado Stefanos Tsitsipas por 6-4, 6-7(5), 6-3 para avanzar a la final del Almaty Open. El jugador georgiano desplego una pegada demoledora desde el fondo, conectando 32 tiros ganadores en dos horas y 18 minutos de juego de alto voltaje. Pese a ceder el desempate del segundo parcial, Basilashvili quebro dos veces el saque de Tsitsipas en el tercer set para sellar el triunfo.",
                "La victoria confirma el renacer de Basilashvili, quien supero la clasificacion previa antes de apear a Adrian Mannarino y ahora a Tsitsipas, alcanzando su primera final ATP desde 2022. En la otra semifinal, el maximo favorito Daniil Medvedev sello su pase al duelo por el titulo tras la retirada del idolo local Alexander Bublik por una molestia en la rodilla derecha. Medvedev gano el primer set 6-3 antes del abandono. La final dominical enfrentara a Medvedev contra Basilashvili en Kazajistan."
            ]
        },
        "de": {
            "title": "Basilashvili schockt Tsitsipas in Almaty: Medvedev zieht ins Finale ein",
            "subtitle": "Nikoloz Basilashvili gelingt Dreisatz-Ueberraschung. Daniil Medvedev profitiert von Bubliks verletzungsbedingter Aufgabe.",
            "excerpt": "Qualifikant Basilashvili schlaegt Stefanos Tsitsipas 6-4, 6-7, 6-3 und steht im Almaty-Finale. Topfavorit Medvedev profitiert von Bubliks Aufgabe.",
            "body": [
                "Nikoloz Basilashvili hat am Samstag, 24. Oktober, fuer eine der groessten Ueberraschungen der Hallensaison gesorgt und den an Nummer sieben gesetzten Stefanos Tsitsipas im Halbfinale von Almaty mit 6-4, 6-7(5), 6-3 bezwungen. Der georgische Qualifikant ueberzeugte mit kompromisslosen Grundschlaegen und verbuchte 32 Winner in 2 Stunden und 18 Minuten. Nachdem er im Tiebreak des zweiten Durchgangs eine Fuehrung vergab, holte er sich im Entscheidungssatz zwei entscheidende Breaks.",
                "Fuer Basilashvili bedeutet der Erfolg den Einzug in sein erstes ATP-Finale seit 2022, nachdem er zuvor bereits die Qualifikation und Altmeister Adrian Mannarino gemeistert hatte. Im zweiten Halbfinale zog der topgesetzte Daniil Medvedev ins Endspiel ein, nachdem Lokalmatador Alexander Bublik wegen einer Knieverletzung aufgeben musste. Medvedev gewann Satz eins mit 6-3, ehe Bublik das Match vorzeitig beendete. Am Sonntag kaempfen Medvedev und Basilashvili um die Trophaee."
            ]
        },
        "it": {
            "title": "Basilashvili ribalta Tsitsipas ad Almaty: Medvedev approda in finale",
            "subtitle": "Nikoloz Basilashvili compie l'impresa in tre set. Daniil Medvedev vola all'atto conclusivo dopo il ritiro di Bublik.",
            "excerpt": "Il qualificato Basilashvili batte a sorpresa Tsitsipas 6-4, 6-7, 6-3 e vola in finale ad Almaty. Medvedev avanza per il forfait di Bublik.",
            "body": [
                "Nikoloz Basilashvili ha firmato una delle sorprese piu clamorose della stagione autunnale indoor sabato 24 ottobre, sconfiggendo la testa di serie numero sette Stefanos Tsitsipas con il punteggio di 6-4, 6-7(5), 6-3 nella semifinale dell'Almaty Open. Il qualificato georgiano ha fatto la voce grossa da fondo campo mettendo a segno 32 vincenti in due ore e 18 minuti di battaglia serrata. Dopo aver sprecato un vantaggio nel tie-break del secondo set, Basilashvili ha strappato due volte il servizio al greco nel terzo parziale.",
                "Il successo corona una settimana magica per Basilashvili, che arrivando dalle qualificazioni e battendo Mannarino e Tsitsipas ha conquistato la sua prima finale ATP dal 2022. Nella seconda semifinale, la testa di serie numero uno Daniil Medvedev ha staccato il pass per la finalissima approfittando del ritiro del kazako Alexander Bublik per un problema al ginocchio destro, dopo aver incamerato il primo set per 6-3. Domenica la finale vedra Medvedev opposto a Basilashvili."
            ]
        },
        "pl": {
            "title": "Basilashvili szokuje Tsitsipasa w Almatach: Medvedev melduje sie w finale",
            "subtitle": "Nikoloz Basilashvili sprawia sensacje w trzech setach. Daniil Medvedev awansuje po kreczu Bublika.",
            "excerpt": "Kwalifikant Basilashvili ogral Stefanosa Tsitsipasa 6-4, 6-7, 6-3 i awansowal do finalu w Almatach. Medvedev gra dalej po kreczu Bublika.",
            "body": [
                "Nikoloz Basilashvili sprawil w sobote 24 pazdziernika jedna z najwiekszych sensacji jesiennych turniejow halowych, eliminujac rozstawionego z numerem siodmym Stefanosa Tsitsipasa 6-4, 6-7(5), 6-3 w polfinale Almaty Open. Gruzinski kwalifikant imponowal potega uderzen z glebi kortu, posylajac 32 uderzenia konczace w trwajacym 2 godziny i 18 minut pojedynku. Choc w tie-breaku drugiego seta wypuscil prowadzenie, w decydujacej partii dwukrotnie przelamal serwis greckiego rywala.",
                "Triumf oznacza dla Basilashvilego powrot do finalu turnieju ATP po raz pierwszy od 2022 roku, po wczesniejszym przejsciu kwalifikacji i odprawieniu Adriana Mannarino. W drugim polfinale najwyzej rozstawiony Daniil Medvedev awansowal do meczu o tytul po tym, jak ulubieniec miejscowej publicznosci Alexander Bublik poddal mecz z powodu kontuzji kolana. Medvedev wygral pierwszego seta 6-3. Niedzielny final w Kazachstanie to starcie Medvedeva z Basilashvilim."
            ]
        },
        "zh": {
            "title": "巴西拉什维利爆冷掀翻西西帕斯：梅德韦杰夫挺进阿拉木图决赛",
            "subtitle": "资格赛黑马巴西拉什维利三盘力克7号种子。布勃利克因伤退赛保送梅德韦杰夫晋级。",
            "excerpt": "格鲁吉亚资格赛黑马巴西拉什维利以6-4、6-7、6-3爆冷击败西西帕斯，与头号种子梅德韦杰夫会师阿拉木图决赛。",
            "body": [
                "10月24日周六，格鲁吉亚选手尼科洛兹·巴西拉什维利在阿拉木图公开赛半决赛中爆出大冷，苦战2小时18分钟以6-4、6-7(5)、6-3力克7号种子斯特凡诺斯·西西帕斯杀入决赛。这位资格赛黑马底线重炮火力全开，全场狂轰32记制胜分。尽管在第二盘抢七惜败，但他顶住压力在决胜盘两度完成破发锁定胜局。",
                "这场胜利让巴西拉什维利自2022年以来首度重返ATP巡回赛单打决赛。在稍后进行的另一场半决赛中，头号种子丹尼尔·梅德韦杰夫轻松晋级，本土名将亚历山大·布勃利克在首盘3-6告负后因右膝伤势退赛。周日的争冠之战将在梅德韦杰夫与巴西拉什维利之间展开。"
            ]
        },
        "ja": {
            "title": "バシラシビリがチチパスを撃破：メドベージェフがアルマティ決勝へ進出",
            "subtitle": "予選勝者のバシラシビリが3セットの激闘を制す。メドベージェフはブブリクの途中棄権で決勝へ。",
            "excerpt": "予選上がりのバシラシビリがチチパスを6-4, 6-7, 6-3で破りアルマティ決勝へ進出。第1シードのメドベージェフも棄権勝ちで進出。",
            "body": [
                "10月24日土曜、アルマティ・オープンの準決勝で予選勝者のニコロズ・バシラシビリが第7シードのステファノス・チチパスを6-4, 6-7(5), 6-3で破る大波乱を起こしました。ジョージア出身のバシラシビリは強烈なストロークを武器に2時間18分の熱戦で32本のウィナーをマーク。第2セットのタイブレークを落としたものの、ファイナルセットで2度のブレークを奪い切り見事な勝利を飾りました。",
                "バシラシビリにとっては2022年以来となるATPツアー決勝進出。一方の準決勝では、第1シードのダニール・メドベージェフが地元カザフスタンのアレクサンダー・ブブリクと対戦。メドベージェフが第1セットを6-3で先取した後、ブブリクが右膝の負傷により無念の棄権を選択しました。日曜の決勝はメドベージェフ対バシラシビリの顔合わせとなります。"
            ]
        },
        "ko": {
            "title": "바실라시빌리 치치파스 꺾고 대이변: 메드베데프 알마티 결승 안착",
            "subtitle": "예선 통과자 바실라시빌리 3세트 접전 승리. 메드베데프는 부블리크 기권으로 결승행.",
            "excerpt": "예선 통과자 바실라시빌리가 스테파노스 치치파스를 6-4, 6-7, 6-3으로 꺾고 결승에 올랐습니다. 톱시드 메드베데프도 결승에 진출했습니다.",
            "body": [
                "10월 24일 토요일 카자흐스탄 알마티 오픈 준결승에서 대이변이 일어났습니다. 예선을 거쳐 올라온 니콜로즈 바실라시빌리가 7번 시드 스테파노스 치치파스를 2시간 18분 접전 끝에 6-4, 6-7(5), 6-3으로 꺾고 결승에 진출했습니다. 바실라시빌리는 양손 백핸드와 포핸드에서 32개의 위너를 몰아치며 치치파스를 강하게 밀어붙였고, 3세트에서 두 차례 브레이크를 따내 승기를 잡았습니다.",
                "이로써 바실라시빌리는 2022년 이후 처음으로 ATP 투어 결승 무대를 밟게 되었습니다. 이어진 다른 준결승에서는 톱시드 다닐 메드베데프가 카자흐스탄의 알렉산더 부블리크를 상대로 1세트를 6-3으로 따낸 뒤, 부블리크가 오른쪽 무릎 부상으로 기권하면서 손쉽게 결승행 티켓을 거머쥐었습니다. 일요일 결승에서는 메드베데프와 바실라시빌리가 우승 트로피를 놓고 격돌합니다."
            ]
        },
        "ar": {
            "title": "باسيلاشفيلي يصدم تسيتسيباس في الماتي: وميدفيديف يتاهل الى النهائي",
            "subtitle": "نيكولوز باسيلاشفيلي يفجر مفاجأة مدوية في ثلاث مجموعات. ودانييل ميدفيديف يتاهل بانسحاب بوبليك.",
            "excerpt": "صدم المتأهل من التصفيات باسيلاشفيلي منافسه ستيفانوس تسيتسيباس 6-4 و6-7 و6-3 ليبلغ نهائي الماتي. وميدفيديف يتاهل بعد انسحاب بوبليك.",
            "body": [
                "حقق الجورجي نيكولوز باسيلاشفيلي كبرى مفاجآت موسم البطولات داخل القاعات يوم السبت 24 اكتوبر، بعدما اطاح بالمصنف السابع اليوناني ستيفانوس تسيتسيباس بنتيجة 6-4 و6-7(5) و6-3 ليبلغ المباراة النهائية لبطولة الماتي المفتوحة. واعتمد اللاعب المتأهل من التصفيات على ضربات ارضية ساحقة وسجل 32 نقطة مباشرة في مواجهة ماراثونية استمرت ساعتين و18 دقيقة. ورغم خسارته الشوط الفاصل في المجموعة الثانية، استعاد باسيلاشفيلي زمام المبادرة وكسر ارسال تسيتسيباس مرتين في المجموعة الفاصلة.",
                "ويعد هذا الفوز عودة قوية لباسيلاشفيلي الذي يبلغ اول نهائي له في جولات ATP منذ عام 2022. وفي نصف النهائي الثاني، بلغ المصنف الاول دانييل ميدفيديف النهائي بعد انسحاب النجم المحلي الكازاخي الكسندر بوبليك بسبب اصابة في الركبة اليمنى. وكان ميدفيديف قد حسم المجموعة الاولى 6-3 قبل انسحاب بوبليك. ويلتقي ميدفيديف مع باسيلاشفيلي يوم الاحد في نهائي البطولة."
            ]
        }
    },
    "pga-tour-bermuda-round3-blanchet-hirata-tied-for-lead-2026": {
        "fr": {
            "title": "Bermudes 3e tour : Blanchet et Hirata co-leaders apres 36 trous a Port Royal",
            "subtitle": "Chandler Blanchet et Kensei Hirata pointent a 13 sous le par. Le moving day commence face aux vents atlantiques.",
            "excerpt": "Blanchet et Hirata partagent les commandes a 129 (-13) avant le 3e tour ce samedi. Corey Conners reste en embuscade a Port Royal.",
            "body": [
                "Le moving day du Butterfield Bermuda Championship s'est elance ce samedi 24 octobre, avec l'Americain Chandler Blanchet et le Japonais Kensei Hirata en tete d'affiche, a egalite parfaite a 13 sous le par (129). Blanchet a confirme son sensationnel 62 inaugural en signant un solide 67 (-4) vendredi, avec cinq birdies et un seul bogey dans le vent marin. De son cote, Hirata a realise un sans-faute vendredi avec une carte vierge de tout bogey de 64 (-7).",
                "Le duo mene les debats sur le sublime trace de Port Royal a Southampton, ou le cut a 36 trous a reduit le peloton aux 65 meilleurs joueurs et ex aequo. Les pretendants se disputent 500 points au classement FedExCup Fall et un cheque de 1.08 million de dollars destine au vainqueur. Le Canadien Corey Conners, joueur le mieux classe du tournoi au 61e rang mondial, demeure en embuscade apres des cartes de 63 et 68."
            ]
        },
        "es": {
            "title": "Bermudas Ronda 3: Blanchet y Hirata comparten el liderato en Port Royal",
            "subtitle": "Chandler Blanchet y Kensei Hirata lideran con 13 bajo par. Inicia el moving day con intensas rachas de viento.",
            "excerpt": "Blanchet e Hirata comparten la cima con 129 (-13) de cara a la tercera ronda del sabado. Corey Conners sigue en la pelea en Port Royal.",
            "body": [
                "La tercera jornada del Butterfield Bermuda Championship comenzo este sabado 24 de octubre con Chandler Blanchet y el japones Kensei Hirata igualados en lo mas alto de la clasificacion con 13 bajo par (129). Blanchet respaldo su historico 62 de apertura con una vuelta de 67 (-4) el viernes, registrando cinco birdies y un unico bogey. Hirata escalo posiciones gracias a una ronda impecable sin bogeys de 64 golpes (-7).",
                "Ambos golfistas comandan el torneo en el espectacular campo de Port Royal Golf Course, donde el corte de 36 hoyos dejo en competicion a los mejores 65 y empates. Todos luchan por 500 puntos de la FedExCup de otono y un premio de 1.08 millones de dolares para el campeon. El canadiense Corey Conners se mantiene muy cerca tras rondas de 63 y 68, listo para aprovechar las complicadas rafagas de viento atlantico."
            ]
        },
        "de": {
            "title": "Bermuda Runde 3: Blanchet und Hirata teilen 36-Loch-Fuehrung in Port Royal",
            "subtitle": "Chandler Blanchet und Kensei Hirata liegen bei 13 unter Par. Moving Day an den windigen Klippen des Atlantiks.",
            "excerpt": "Blanchet und Hirata fuehren das Feld mit 129 Schlaegen (-13) in Runde drei an. Corey Conners lauert in Port Royal.",
            "body": [
                "Der Moving Day der Butterfield Bermuda Championship begann am Samstag, 24. Oktober, mit Chandler Blanchet und dem Japaner Kensei Hirata schlaggleich an der Spitze bei 13 unter Par (129 Schlaege). Blanchet bestaetigte seine 62er-Traumrunde vom Donnerstag mit einer souveraenen 67 (-4) am Freitag. Hirata ueberzeugte seinerseits mit einer fehlerfreien, bogeyfreien 64 (-7) und zog mit dem Amerikaner gleich.",
                "Das Fuehrungsduo liegt knapp vor einem dicht gestaffelten Verfolgerfeld auf dem Par-71-Kurs von Port Royal. Nach dem Cut am Freitagabend spielen noch die besten 65 Profis und Schlaggleichen um 500 FedExCup-Punkte und 1.08 Millionen Dollar Siegerpreisgeld. Der kanadische Topstar Corey Conners bleibt nach Runden von 63 und 68 in Schlagdistanz und lauert auf seine Chance am windigen Moving Day."
            ]
        },
        "it": {
            "title": "Bermuda 3° giro: Blanchet e Hirata guidano a -13 a Port Royal",
            "subtitle": "Chandler Blanchet e Kensei Hirata appaiati in vetta con 13 colpi sotto il par. Al via il moving day sull'Atlantico.",
            "excerpt": "Blanchet e Hirata condividono la testa della classifica con 129 (-13) verso il terzo giro di sabato. Corey Conners in agguato a Port Royal.",
            "body": [
                "Il moving day del Butterfield Bermuda Championship e iniziato sabato 24 ottobre, con Chandler Blanchet e il giapponese Kensei Hirata appaiati al comando con uno score complessivo di 13 colpi sotto il par (129). Blanchet ha dato continuita al suo splendido 62 d'apertura girando in 67 (-4) venerdi con cinque birdie. Hirata si e arrampicato in testa grazie a una splendida carta da 64 (-7) senza alcun bogey.",
                "I due guidano il torneo sul suggestivo percorso di Port Royal Golf Course, dove il taglio a 36 buche ha promosso i primi 65 atleti e pari merito. In palio ci sono 500 punti FedExCup Fall e una prima moneta da 1.08 milioni di dollari dal montepremi di 6 milioni. Il canadese Corey Conners si trova a ridosso dei leader dopo due giri da 63 e 68 colpi, pronto ad approfittare delle raffiche di vento oceanico."
            ]
        },
        "pl": {
            "title": "Bermudy 3. runda: Blanchet i Hirata prowadza po 36 dolkach w Port Royal",
            "subtitle": "Chandler Blanchet i Kensei Hirata na czele z wynikiem 13 ponizej par. Poczatek moving day nad Atlantykiem.",
            "excerpt": "Blanchet i Hirata dziela prowadzenie z wynikiem 129 (-13) przed sobota. Corey Conners pozostaje w grze o tytul w Port Royal.",
            "body": [
                "Sobota 24 pazdziernika przynosi moving day podczas Butterfield Bermuda Championship, gdzie Chandler Blanchet oraz Japonczyk Kensei Hirata dziela pozycje lidera z wynikiem 13 ponizej par (129). Blanchet po czwartkowym rekordowym 62 dolozyl w piatek spokojna runde 67 (-4). Z kolei Hirata zanotowal bezbledna runde 64 (-7) bez ani jednego bogeya.",
                "Obaj zawodnicy maja niewielka przewage nad grupa poscigowa na polu Port Royal Golf Course w Southampton. Po piatkowym cutcie w rywalizacji pozostalo 65 najlepszych golfistow walczacych o 500 punktow FedExCup i nagrode glowna w wysokosci 1.08 miliona dolarow. Kanadyjczyk Corey Conners zachowuje realne szanse na zwyciestwo po rundach 63 i 68."
            ]
        },
        "zh": {
            "title": "百慕大锦标赛第三轮：布兰切特与平田宪圣前36洞并列领跑皇家港",
            "subtitle": "布兰切特与平田宪圣同以低于标准杆13杆并列榜首。“移动日”在大西洋海风中打响。",
            "excerpt": "布兰切特与平田宪圣前两轮交出129杆（-13）并列领先进入周六第三轮。科纳斯在皇家港保持争冠希望。",
            "body": [
                "百慕大锦标赛“移动日”于10月24日周六拉开帷幕，钱德勒·布兰切特与日本选手平田宪圣前36洞同以低于标准杆13杆的129杆并列领跑。布兰切特在首轮交出惊艳的62杆后，周五稳扎稳打抓下5只小鸟交出67杆（-4）。而平田宪圣则在周五轰出无博忌的64杆（-7），强势追平榜首。",
                "这对领头羊组合目前在皇家港高尔夫球场保持微弱领先。经过周五晚间的晋级线筛选，排名前65位及并列的球员进入后两轮争夺，角逐500个联邦快递杯秋季积分以及600万美元总奖金中高达108万美元的冠军奖金。加拿大名将科纳斯在前两轮打出63杆与68杆，紧追第一集团。"
            ]
        },
        "ja": {
            "title": "バミューダ第3R：ブランシェットと平田憲聖が通算13アンダーで首位タイ",
            "subtitle": "ブランシェットと平田憲聖が129ストロークで並ぶ。大西洋の強風のなかムービングデー開幕。",
            "excerpt": "通算129（-13）でブランシェットと平田憲聖が首位に並び土曜の第3ラウンドへ突入。ポートロイヤルでコナーズも上位を追走。",
            "body": [
                "バミューダ選手権のムービングデーが10月24日土曜にスタート。チャンドラー・ブランシェットと日本の平田憲聖が36ホール終了時点で通算13アンダーの129で首位タイに並びました。初日に圧巻の62を叩き出したブランシェットは金曜も67（-4）と手堅くまとめ首位をキープ。一方の平田はボギーなしの7バーディー・64（-7）と猛チャージを見せトップに立ちました。",
                "美しい大西洋沿いに広がる名門ポートロイヤル・ゴルフコースでは、36ホール終了時の予選カットを通過した上位陣が500フェデックスカップポイントと優勝賞金108万ドルを巡って争います。世界ランク61位で今大会最高位のコーリー・コナーズも63、68と好位置を維持しており、週末の優勝争いに絡む構えです。"
            ]
        },
        "ko": {
            "title": "버뮤다 챔피언십 3R: 블랑셰와 히라타 켄세이 13언더파 공동 선두",
            "subtitle": "챈들러 블랑셰와 히라타 켄세이 36홀 합계 129타 기록. 대서양 바람 속 무빙데이 개막.",
            "excerpt": "블랑셰와 히라타가 13언더파 129타로 공동 선두를 형성하며 토요일 3라운드에 돌입했습니다. 코너스도 포트 로열에서 선두 추격전.",
            "body": [
                "버터필드 버뮤다 챔피언십 무빙데이가 10월 24일 토요일 포트 로열 골프코스에서 열렸습니다. 미국의 챈들러 블랑셰와 일본의 히라타 켄세이가 나란히 13언더파 129타를 기록하며 공동 선두로 나섰습니다. 1라운드 62타를 쳤던 블랑셰는 2라운드에서 버디 5개와 보기 1개로 67타(-4)를 적어냈고, 히라타는 노보기 64타(-7)의 무결점 플레이로 공동 선두에 합류했습니다.",
                "사우샘프턴의 파71 해안 링크스 코스에서 펼쳐지는 이번 대회는 상위 65명이 본선에 진출했습니다. 우승자에게는 페덱스컵 가을 시리즈 500포인트와 108만 달러의 상금이 주어집니다. 캐나다의 코리 코너스는 1, 2라운드에서 각각 63타, 68타를 치며 선두 그룹을 바짝 뒤쫓고 있습니다."
            ]
        },
        "ar": {
            "title": "بطولة برمودا الجولة 3: بلانشيت وهيراتا يتقاسمان الصدارة في بورت رويال",
            "subtitle": "تشاندلر بلانشيت وكينسي هيراتا في الصدارة بـ13 ضربة تحت المعدل. انطلاق يوم الحسم وسط رياح الاطلسي.",
            "excerpt": "بلانشيت وهيراتا يتشاركان الصدارة بـ129 ضربة (-13) قبل الجولة الثالثة السبت. وكوري كونرز يواصل المطاردة في بورت رويال.",
            "body": [
                "انطلقت منافسات الجولة الثالثة من بطولة برمودا للجولف يوم السبت 24 اكتوبر، حيث يتقاسم الامريكي تشاندلر بلانشيت والياباني كينسي هيراتا الصدارة بمجموع 13 ضربة تحت المعدل (129 ضربة). وعزز بلانشيت رقمه القياسي بالجولة الاولى ببطاقة 67 ضربة (-4) يوم الجمعة، في حين تقدم هيراتا بقوة مسجلا 64 ضربة خالية من الاخطاء (-7).",
                "ويتقدم الثنائي بفارق ضئيل امام كوكبة من الملاحقين على ملعب بورت رويال في ساوثهامبتون، بعد ان اجتاز 65 لاعبا حاجز التصفية. ويتنافس اللاعبون على 500 نقطة في كأس فيديكس الخريفي وجائزة مالية للمركز الاول قدرها 1.08 مليون دولار من اجمالي 6 ملايين دولار. ويحتفظ الكندي كوري كونرز بفرص قوية في المنافسة بعد تسجيله 63 و68 ضربة."
            ]
        }
    },
    "f1-austin-saturday-qualifying-cota-antonelli-title-chase-2026": {
        "fr": {
            "title": "Qualifications au sommet a Austin : Leclerc dicte le tempo, Antonelli vise la pole",
            "subtitle": "Ferrari a domine les essais au COTA avec Antonelli a 0.042 seconde. Les qualifications de samedi etablissent la grille.",
            "excerpt": "Les qualifications de samedi sur le Circuit des Ameriques se profilent avec Antonelli en tete avec 102 points d'avance. Leclerc a ete le plus rapide pour Ferrari.",
            "body": [
                "Le Circuit des Ameriques a Austin s'apprete a vibrer ce samedi 24 octobre pour les qualifications du Grand Prix des Etats-Unis 2026. Apres deux seances d'essais libres dominees vendredi par Charles Leclerc au volant de sa Ferrari, la grille se prepare pour les EL3 et la lutte acharnee pour la pole position a 16:00 locale. En EL2, Leclerc n'a devance le leader du championnat Kimi Antonelli que de 42 millièmes de seconde en pneus tendres.",
                "Mercedes aborde ce samedi en position ideale : Antonelli domine le classement des pilotes avec 340 points, 102 longueurs devant son coequipier George Russell (238). Une pole et un succes dimanche rapprocheraient encore le prodige italien d'un sacre mondial. Derriere, Max Verstappen et Red Bull restent en embuscade a un dixieme, promettant une bataille de haut vol sous des temperatures avoisinant les 38 degres sur l'asphalte texan."
            ]
        },
        "es": {
            "title": "Duelo de clasificacion en Austin: Leclerc manda en libres y Antonelli busca la pole",
            "subtitle": "Ferrari domino el viernes en COTA con Antonelli a 0.042 segundos. La clasificacion del sabado define la parrilla.",
            "excerpt": "Llega la clasificacion de sabado en el Circuito de las Americas con Antonelli defendiendo 102 puntos de ventaja. Leclerc domino para Ferrari.",
            "body": [
                "El Circuito de las Americas en Austin acoge este sabado 24 de octubre una batalla crucial en la clasificacion del Gran Premio de Estados Unidos 2026. Luego de que Charles Leclerc colocara a su Ferrari en la cima en los entrenamientos del viernes, los pilotos ultiman detalles para la sesion definitoria de las 16:00 local. Leclerc supero a Kimi Antonelli por escasas 42 milesimas en simulacion de clasificacion.",
                "Mercedes llega al sabado con gran solvencia: Antonelli comanda el campeonato con 340 puntos, 102 por delante de George Russell (238). Una pole y posterior victoria dominical dejarian al novato italiano a las puertas del campeonato mundial. Por su parte, Max Verstappen se ubico tercero con Red Bull a poco mas de una decima, anticipando una sesion ardiente con temperaturas en pista superiores a los 38 grados Celsius."
            ]
        },
        "de": {
            "title": "Qualifying-Showdown in Austin: Leclerc dominiert Training, Antonelli jagt Pole",
            "subtitle": "Ferrari am Freitag am COTA vorn, Antonelli nur 0.042 Sekunden zurueck. Samstags-Qualifying entscheidet ueber die Startaufstellung.",
            "excerpt": "Das Qualifying am Samstag auf dem Circuit of the Americas steht an. Antonelli verteidigt 102 Punkte Vorsprung, waehrend Leclerc fuer Ferrari das Tempo vorgab.",
            "body": [
                "Auf dem Circuit of the Americas in Austin steht am Samstag, 24. Oktober, der packende Kampf um die Pole Position beim Grossen Preis der USA auf dem Programm. Nachdem Charles Leclerc seinen Ferrari in beiden Freitagstrainings an die Spitze setzte, bereiten sich die Teams auf das entscheidende Qualifying um 16:00 Uhr Ortszeit vor. Im zweiten freien Training trennten Leclerc und WM-Spitzenreiter Kimi Antonelli lediglich 0.042 Sekunden.",
                "Mercedes geht aus einer Position der Staerke in den Samstag. Antonelli fuehrt die Fahrerwertung mit 340 Punkten souveraen an, 102 Punkte vor Stallgefaehrte George Russell (238). Eine Pole Position und ein Sieg am Sonntag wuerden den Italiener dem WM-Titel ganz nahe bringen. Doch auch Red-Bull-Pilot Max Verstappen lauerte am Freitag nur gut ein Zehntel zurueck auf Rang drei."
            ]
        },
        "it": {
            "title": "Sfida per la pole ad Austin: Leclerc detta il passo, Antonelli all'attacco",
            "subtitle": "Ferrari al comando nelle libere al COTA con Antonelli a soli 0.042 secondi. Le qualifiche di sabato decidono la griglia.",
            "excerpt": "Le qualifiche di sabato al Circuit of the Americas vedono Antonelli forte di 102 punti di vantaggio. Leclerc il piu veloce nelle libere con la Ferrari.",
            "body": [
                "Tutto pronto al Circuit of the Americas di Austin per le qualifiche del Gran Premio degli Stati Uniti 2026, in programma sabato 24 ottobre. Dopo che Charles Leclerc ha spinto la sua Ferrari in cima ai monitor dei tempi nelle due sessioni del venerdi, la griglia si prepara al verdetto delle qualifiche delle 16:00 locali. Leclerc ha preceduto il leader del mondiale Kimi Antonelli di appena 42 millesimi di secondo nella simulazione sul giro secco.",
                "La Mercedes arriva al sabato forte del proprio dominio tecnico. Antonelli guida la classifica piloti con 340 punti, 102 lunghezze di vantaggio sul compagno George Russell (238). Una pole position e una vittoria domenica avvicinerebbero ulteriormente il giovane talento italiano al titolo iridato. Terzo tempo per Max Verstappen su Red Bull a poco piu di un decimo, pronto a dare battaglia su un asfalto texano vicino ai 38 gradi."
            ]
        },
        "pl": {
            "title": "Walka o pole position w Austin: Leclerc dyktuje tempo, Antonelli goni za pole",
            "subtitle": "Ferrari najszybsze w piatkowych treningach na COTA, Antonelli tylko 0.042 sekundy za nim. Sobotnie kwalifikacje ukladaja stawke.",
            "excerpt": "Sobotnie kwalifikacje na Circuit of the Americas nadchodza w momencie, gdy Antonelli ma 102 punkty przewagi. Leclerc byl najszybszy dla Ferrari.",
            "body": [
                "Circuit of the Americas w Austin jest gotowy na zaciete kwalifikacje przed Grand Prix Stanow Zjednoczonych w sobote 24 pazdziernika. Po piatkowych treningach, w ktorych Charles Leclerc z Ferrari uzyskal najlepszy czas, kierowcy stana do walki o pole position o godzinie 16:00 czasu lokalnego. Leclerc w drugim treningu wyprzedzil lidera klasyfikacji generalnej Kimiego Antonellego o zaledwie 0.042 sekundy.",
                "Mercedes znajduje sie w doskonalej sytuacji punktowej. Antonelli prowadzi w mistrzostwach z 340 punktami, wyprzedzajac kolege z zespolu George'a Russella (238 punktow) o 102 punkty. Zwyciestwo w kwalifikacjach i wyscigu przyblizy wloskiego debiutanta do mistrzostwa swiata. Trzeci czas piatku nalezal do Maxa Verstappena z Red Bulla, co zapowiada zacieta rywalizacje na nagrzanym do 38 stopni teksanskim torze."
            ]
        },
        "zh": {
            "title": "奥斯汀排位巅峰战：勒克莱尔练习赛领跑，安东内利冲击杆位",
            "subtitle": "法拉利在美洲赛道领跑周五练习赛，安东内利仅落后0.042秒。周六排位赛决定正赛发车位。",
            "excerpt": "美洲赛道周六排位赛大战一触即发，安东内利手握102分榜首优势。勒克莱尔为法拉利拔得头筹。",
            "body": [
                "2026年F1美国大奖赛排位赛将于10月24日周六在奥斯汀美洲赛道激情上演。法拉利车手勒克莱尔在周五两次自由练习赛中均刷新全场最快圈速，正赛发车位争夺战将于当地时间16:00打响。在二练的软胎飞驰圈模拟中，勒克莱尔仅以0.042秒的微弱优势险胜积分榜领头羊基米·安东内利。",
                "梅赛德斯车队目前在积分榜上占据绝对优势。安东内利积340分高居榜首，领先队友拉塞尔（238分）多达102分。如果能在周日夺得杆位并斩获冠军，这位意大利超级新星将极具希望提前锁定年度车手总冠军。红牛车队的维斯塔潘在二练中落后头名0.1秒位列第三，在赛道温度高达38摄氏度的高温考验下，轮胎管理将成为决定杆位归属的关键因素。"
            ]
        },
        "ja": {
            "title": "オースティン予選決戦：ルクレールが金曜トップ、アントネッリがポール狙う",
            "subtitle": "フェラーリがCOTAのフリー走行を制覇、アントネッリはわずか0.042秒差。土曜予選で決勝グリッド決定へ。",
            "excerpt": "サーキット・オブ・ジ・アメリカズで土曜公式予選が開幕。アントネッリが102点リードを守り、ルクレールがフェラーリで速さを見せる。",
            "body": [
                "10月24日土曜、テキサス州オースティンのサーキット・オブ・ジ・アメリカズ（COTA）で2026年F1アメリカGPの公式予選が行われます。金曜のフリー走行2回でシャルル・ルクレールがフェラーリを駆りトップタイムを記録。現地時間16:00からの予選に注目が集まります。FP2のアタックラップではルクレールが選手権リーダーのキミ・アントネッリをわずか0.042秒差で上回りました。",
                "メルセデスは盤石の態勢で土曜を迎えます。アントネッリは340点で首位、チームメイトのジョージ・ラッセル（238点）に102点の大差をつけています。土曜のポールと日曜の優勝が決まれば、イタリアの俊英にとって初タイトル獲得へ王手がかかります。3番手にはシンガポール勝者のマックス・フェルスタッペンが0.1秒差でつけており、路面温度38度を超える暑さの中で激しいポール争いが展開されます。"
            ]
        },
        "ko": {
            "title": "오스틴 예선 정면 승부: 르클레르 연습 주행 1위, 안토넬리 폴포지션 정조준",
            "subtitle": "페라리 COTA 금요일 주행 장악, 안토넬리 불과 0.042초 차. 토요일 예선으로 그리드 확정.",
            "excerpt": "서킷 오브 디 아메리카스에서 토요일 예선 개막. 안토넬리가 102점 차 리드를 지키는 가운데 르클레르가 페라리를 이끌고 있습니다.",
            "body": [
                "10월 24일 토요일 미국 텍사스주 오스틴의 서킷 오브 디 아메리카스(COTA)에서 2026 F1 미국 그랑프리 예선전이 펼쳐집니다. 금요일 연습 주행에서 샤를 르클레르가 페라리를 이끌고 가장 빠른 랩타임을 기록한 가운데, 현지 시간 16:00 공식 예선에서 치열한 폴포지션 다툼이 예상됩니다. 르클레르는 FP2 소프트 타이어 시뮬레이션에서 챔피언십 선두 키미 안토넬리를 0.042초 차로 제쳤습니다.",
                "메르세데스는 여전히 강력한 우승 후보입니다. 안토넬리는 드라이버 챔피언십 340점으로 팀 동료 조지 러셀(238점)에 102점 앞서 있습니다. 토요일 예선 1위와 일요일 결승 우승을 거머쥘 경우 월드 챔피언 등극에 결정적 교두보를 마련하게 됩니다. 한편 싱가포르 우승자 막스 페르스타펀도 0.1초 차 3위로 뒤를 바짝 쫓고 있습니다."
            ]
        },
        "ar": {
            "title": "صراع التجارب التاهيلية في اوستن: لوكلير يقود التجارب وانتونيلي يسعى للقطب",
            "subtitle": "فيراري تتصدر تجارب الجمعة في حلبة الامريكيتين وانتونيلي على بعد 0.042 ثانية فقط. التاهيل يحسم شبكة الانطلاق.",
            "excerpt": "تنطلق التجارب التاهيلية السبت في حلبة الامريكيتين وانتونيلي يتقدم بفارق 102 نقطة. لوكلير حقق الصدارة لفيراري.",
            "body": [
                "تتجه انظار عشاق السرعة يوم السبت 24 اكتوبر الى حلبة الامريكيتين في اوستن لمتابعة التجارب التاهيلية لسباق جائزة الولايات المتحدة الكبرى 2026. وتصدر شارل لوكلير سائق فيراري جولتي التجارب الحرة يوم الجمعة، ليضع فريقه في موقع متميز قبل حصة الحسم الساعة 16:00 محليا. وتفوق لوكلير على متصدر الترتيب كيمي انتونيلي بفارق ضئيل بلغ 0.042 ثانية فقط.",
                "ويدخل فريق مرسيدس المنافسات باريحية كبيرة، حيث يتصدر انتونيلي ترتيب بطولة السائقين برصيد 340 نقطة، متقدما بفارق 102 نقطة على زميله جورج راسل (238 نقطة). وسيقرب الانطلاق من المركز الاول والفوز يوم الاحد السائق الايطالي الواعد من حسم اللقب العالمي. وفي المقابل، يتربص ماكس فيرستابن سائق ريد بول في المركز الثالث بفارق اعشار قليلة من الثانية."
            ]
        }
    },
    "wnba-finals-2026-game4-dream-host-valkyries-title-brink": {
        "fr": {
            "title": "Finales WNBA match 4 : le Dream a une victoire d'un sacre historique a Atlanta",
            "subtitle": "Atlanta mene 2-1 dans la serie avec balle de match a la State Farm Arena. Golden State lutte pour arracher un match 5.",
            "excerpt": "L'Atlanta Dream peut remporter son tout premier titre WNBA aujourd'hui lors du match 4. Angel Reese poursuit sa serie historique de double-doubles.",
            "body": [
                "L'Atlanta Dream touche du doigt la gloire ce samedi 24 octobre en accueillant les Golden State Valkyries pour le match 4 des Finales WNBA a la State Farm Arena. Menant 2-1 dans cette serie au meilleur des cinq matches, la franchise georgienne a l'occasion de decrocher le premier championnat de son histoire devant son public. L'effervescence a gagne le centre-ville d'Atlanta apres la demonstration de force du Dream, vainqueur 97-71 lors du match 3 mercredi.",
                "Tous les projecteurs sont braques sur Angel Reese, dont la premiere campagne en Finales est deja historique. Reese est devenue la premiere joueuse de l'histoire de la WNBA a reussir un double-double lors de ses trois premieres rencontres de Finales en carriere, inscrivant 21 points et captant 12 rebonds au match 3. Pour Golden State, la defaite est interdite sous peine d'elimination, les Valkyries devant imperativement s'imposer pour ramener la serie au Chase Center pour un match 5 decisif."
            ]
        },
        "es": {
            "title": "Finales WNBA Juego 4: Dream busca sellar un titulo historico en Atlanta",
            "subtitle": "Atlanta lidera 2-1 la serie con punto de campeonato en State Farm Arena. Golden State lucha por forzar el Juego 5.",
            "excerpt": "El Atlanta Dream puede coronarse campeon de la WNBA hoy en el Juego 4. Angel Reese llega con una historica racha de doble-dobles.",
            "body": [
                "El Atlanta Dream se encuentra a las puertas de la gloria deportiva este sabado 24 de octubre, al recibir a las Golden State Valkyries en el Juego 4 de las Finales de la WNBA en el State Farm Arena. Con ventaja de 2-1 en la serie al mejor de cinco, Atlanta puede levantar el primer trofeo de campeonato en la historia de la franquicia ante su aficion tras la contundente victoria 97-71 del Juego 3.",
                "El foco estelar apunta a Angel Reese, cuya campana de debut en Finales ha destrozado marcas historicas. Reese se convirtio en la primera jugadora en la historia de la WNBA en firmar un doble-doble en sus tres primeros partidos de Finales, aportando 21 puntos y 12 rebotes el miercoles. Las Valkyries de Golden State se juegan la vida en un duelo a todo o nada, obligadas a ganar para forzar un quinto y decisivo encuentro en el Chase Center de San Francisco."
            ]
        },
        "de": {
            "title": "WNBA-Finals Spiel 4: Dream greifen in Atlanta nach historischer Krone",
            "subtitle": "Atlanta fuehrt 2-1 in der Serie mit Meisterschaftsball in der State Farm Arena. Golden State kaempft um Spiel 5.",
            "excerpt": "Die Atlanta Dream koennen heute in Spiel 4 ihren ersten WNBA-Titel holen. Angel Reese setzt historische Double-Double-Serie fort.",
            "body": [
                "Die Atlanta Dream stehen am Samstag, 24. Oktober, vor dem groessten Triumph ihrer Vereinsgeschichte: In Spiel 4 der WNBA-Finals empfangen sie die Golden State Valkyries in der State Farm Arena. Mit einer 2-1-Fuehrung in der Best-of-Five-Serie kann Atlanta mit einem Heimsieg die erste WNBA-Meisterschaft perfekt machen, befluegelt vom souveraenen 97-71-Erfolg in Spiel 3.",
                "Im Rampenlicht steht Rookie-Star Angel Reese, die mit 21 Punkten und 12 Rebounds als erste Spielerin der WNBA-Geschichte in ihren ersten drei Finalspielen jeweils ein Double-Double auflegte. Fuer das Expansion-Team Golden State Valkyries geht es um das nackte Ueberleben. Nur ein Auswaertssieg in Atlanta haelt die Titelhoffnungen am Leben und erzwingt ein entscheidendes Spiel 5 im Chase Center von San Francisco."
            ]
        },
        "it": {
            "title": "Finals WNBA Gara 4: il Dream vuole chiudere i conti e fare la storia ad Atlanta",
            "subtitle": "Atlanta avanti 2-1 nella serie con il match point alla State Farm Arena. Golden State combatte per portare la sfida a Gara 5.",
            "excerpt": "L'Atlanta Dream puo conquistare oggi il primo anello WNBA della sua storia in Gara 4. Angel Reese arriva con una striscia record di doppie doppie.",
            "body": [
                "L'Atlanta Dream e a un passo dalla leggenda sabato 24 ottobre, quando ospitera le Golden State Valkyries in Gara 4 delle WNBA Finals alla State Farm Arena. In vantaggio 2-1 nella serie al meglio delle cinque partite, Atlanta ha l'occasione di centrare il primo titolo nella storia della franchigia davanti ai propri tifosi, sull'onda dell'entusiasmo per il perentorio 97-71 ottenuto in Gara 3.",
                "Tutti gli occhi sono puntati su Angel Reese, protagonista di un debutto da record nelle Finals: e la prima giocatrice nella storia della WNBA a mettere a referto una doppia doppia in ciascuna delle sue prime tre partite di finale, grazie ai 21 punti e 12 rimbalzi di mercoledi. Per Golden State si tratta di una sfida da dentro o fuori, con l'obbligo di vincere in trasferta per rimandare il verdetto alla decisiva Gara 5 al Chase Center."
            ]
        },
        "pl": {
            "title": "Finaly WNBA mecz 4: Dream chca przypieczetowac historyczny tytul w Atlancie",
            "subtitle": "Atlanta prowadzi w serii 2-1 i ma pilke meczowa w State Farm Arena. Golden State walczy o doprowadzenie do meczu 5.",
            "excerpt": "Atlanta Dream moze dzis zdobyc pierwsze mistrzostwo WNBA w historii w meczu 4. Angel Reese notuje historyczna serie double-double.",
            "body": [
                "Atlanta Dream staje w sobote 24 pazdziernika przed historyczna szansa na zdobycie tytulu mistrzowskiego WNBA, podejmujac Golden State Valkyries w meczu numer 4 w State Farm Arena. Prowadzac 2-1 w serii do trzech zwyciestw, ekipa z Atlanty moze swietowac pierwsze mistrzostwo w historii klubu przed wlasna publicznoscia po zdemolowaniu rywalek 97-71 w srode.",
                "Cala uwaga skupia sie na Angel Reese, ktora pisze historie kobiecej koszykowki: jako pierwsza zawodniczka w dziejach WNBA zaliczyla double-double w trzech swoich pierwszych meczach finalowych, notujac 21 punktow i 12 zbiorek. Dla beniaminka Golden State Valkyries to mecz o przetrwanie, w ktorym musza wygrac na wyjezdzie, aby przeniesc serie na decydujace piate starcie do Chase Center w San Francisco."
            ]
        },
        "zh": {
            "title": "WNBA总决赛第4战：梦想全力在亚特兰大冲击队史首冠",
            "subtitle": "亚特兰大梦想大比分2-1手握冠军点。金州女武神背水一战争取拖入第5战决胜。",
            "excerpt": "亚特兰大梦想队今日有望在第4战斩获队史首座WNBA总冠军奖杯。安吉尔·里斯携历史级两双纪录领衔出战。",
            "body": [
                "10月24日周六，亚特兰大梦想队迎来创造俱乐部历史的决战时刻，她们将在州立农业球馆主场迎战金州女武神，展开WNBA总决赛第4战的较量。在五场三胜制的大比分中以2-1领先后，梦想队只要在主场再取一胜，便可捧起建队以来的首座总冠军奖杯。周三晚间以97-71狂胜对手的惊艳表现让全场士气高涨。",
                "全场目光再度汇聚在超级新星安吉尔·里斯身上。她在第3战砍下21分、12个篮板和3次抢断，成为WNBA历史上第一位在个人职业生涯前三场总决赛均斩获两双的球员。对于作为新军的金州女武神而言，此役是不折不扣的生死战，唯有客场取胜才能将悬念带回旧金山大通中心进行抢五决战。"
            ]
        },
        "ja": {
            "title": "WNBAファイナル第4戦：ドリームがアトランタで歴史的初制覇に挑む",
            "subtitle": "アトランタが2勝1敗で優勝に王手。ゴールデンステイトは第5戦へ逆王手を狙う。",
            "excerpt": "アトランタ・ドリームが本日第4戦で球団史上初のWNBA王座を狙う。エンジェル・リーズが前人未到のダブルダブル連発。",
            "body": [
                "10月24日土曜、アトランタ・ドリームはステートファーム・アリーナにゴールデンステイト・ヴァルキリーズを迎えてWNBAファイナル第4戦を戦います。5戦3勝制で2勝1敗とリードしたドリームは、本拠地で勝利すれば球団創設以来初となる優勝トロフィーを掲げることになります。水曜の第3戦では97-71と相手を圧倒しチームの勢いは最高潮に達しています。",
                "注目は新星エンジェル・リーズ。第3戦で21得点12リバウンドを記録し、WNBA史上初となるファイナルデビューから3戦連続ダブルダブルの金字塔を打ち立てました。後がない新規参入のゴールデンステイト・ヴァルキリーズにとっては負ければ終わりの一戦。敵地で意地を見せサンフランシスコのチェイス・センターでの最終第5戦へ持ち込めるか注目です。"
            ]
        },
        "ko": {
            "title": "WNBA 파이널 4차전: 드림 안방 애틀랜타에서 사상 첫 우승 축포 노린다",
            "subtitle": "애틀랜타 2승 1패로 챔피언십 포인트 획득. 골든스테이트는 5차전 강제 돌입 총력전.",
            "excerpt": "애틀랜타 드림이 오늘 4차전에서 창단 첫 WNBA 우승 트로피를 노립니다. 엔젤 리스가 역사적인 더블더블 행진을 이어갑니다.",
            "body": [
                "애틀랜타 드림이 10월 24일 토요일 스테이트 팜 아레나에서 골든스테이트 발키리스와 WNBA 파이널 4차전을 펼치며 구단 역사상 가장 중요한 순간을 맞이합니다. 5전 3선승제 시리즈에서 2승 1패로 앞선 애틀랜타는 안방 팬들 앞에서 창단 첫 우승을 확정 지을 수 있는 절호의 기회를 잡았습니다. 수요일 3차전 97-71 완승의 기세가 팀 전체에 넘쳐납니다.",
                "스포트라이트는 신인 엔젤 리스에게 집중되고 있습니다. 리스는 3차전에서 21점 12리바운드 3스틸을 기록하며 WNBA 역사상 최초로 개인 첫 파이널 3경기 연속 더블더블이라는 대기록을 작성했습니다. 벼랑 끝에 몰린 골든스테이트는 반드시 승리해 샌프란시스코 체이스 센터에서 열릴 최종 5차전으로 승부를 끌고 가야 합니다."
            ]
        },
        "ar": {
            "title": "نهائيات WNBA المباراة 4: دريم يسعى لحسم اللقب التاريخي في اتلانتا",
            "subtitle": "اتلانتا يتقدم 2-1 مع نقطة حسم البطولة في ستيت فارم ارينا. وغولدن ستيت يقاتل لفرض مباراة خامسة.",
            "excerpt": "يستطيع اتلانتا دريم التتويج بلقبه الاول في تاريخ WNBA اليوم في المباراة الرابعة. وتدخل انجيل ريس اللقاء برقم قياسي من الثنائيات المزدوجة.",
            "body": [
                "يقف اتلانتا دريم على مشارف المجد التاريخي يوم السبت 24 اكتوبر حين يستضيف غولدن ستيت فالكيريز في المباراة الرابعة من نهائيات WNBA في صالة ستيت فارم ارينا. وبعد تقدمه 2-1 في السلسلة، يحتاج اتلانتا الى فوز واحد على ارضه وامام جماهيره ليرفع درع البطولة للمرة الاولى في تاريخ النادي، بعد فوزه الكاسح 97-71 في المباراة الثالثة.",
                "وتتجه الانظار مجددا نحو النجمة انجيل ريس التي حطمت الارقام القياسية بعد تسجيلها 21 نقطة و12 متابعة في المباراة الثالثة لتصبح اول لاعبة في تاريخ البطولة تحقق ثنائية مزدوجة في مبارياتها الثلاث الاولى بالنهائيات. وفي المقابل، يخوض غولدن ستيت مواجهة البقاء ولا بديل امامه سوى الفوز لاعادة السلسلة الى سان فرانسيسكو لخوض مباراة خامسة حاسمة."
            ]
        }
    },
    "nfl-week7-sunday-eve-chiefs-seahawks-49ers-unbeaten-slate-2026": {
        "fr": {
            "title": "NFL semaine 7 veille de dimanche : le trio d'invaincus pret, les Bears savourent",
            "subtitle": "Chicago passe a 5-2 apres son succes face a New England. 49ers, Chiefs et Vikings visent le sans-faute dimanche.",
            "excerpt": "La semaine 7 de la NFL se poursuit dimanche avec de superbes affiches. Kansas City rend visite a Seattle lors du Sunday Night Football.",
            "body": [
                "La NFL s'apprete a vivre un dimanche grandiose lors de la semaine 7, avec trois franchises invaincues qui mettront leur bilan parfait a l'epreuve le 25 octobre. L'affiche du Sunday Night Football verra Patrick Mahomes et les Kansas City Chiefs (5-0) defier les Seattle Seahawks dans la bruyante enceinte de Lumen Field. Dans la NFC, les San Francisco 49ers (6-0) se deplacent chez les Atlanta Falcons, tandis que les surprenants Minnesota Vikings (5-0) recoivent les Indianapolis Colts.",
                "Cette semaine 7 a debute en fanfare jeudi soir a Soldier Field, ou les Chicago Bears ont domine les New England Patriots 30-24. Caleb Williams a signe un match plein avec 308 yards a la passe et deux touchdowns, tandis que Cairo Santos a scelle la victoire d'un coup de pied de 58 yards a 1:34 de la fin. Chicago passe a 5-2 pendant que New England recule a 4-3."
            ]
        },
        "es": {
            "title": "NFL Semana 7 vispera dominical: trio de invictos listo mientras Bears celebran triunfo",
            "subtitle": "Chicago sube a 5-2 tras vencer a Nueva Inglaterra. 49ers, Chiefs y Vikings buscan mantener la perfeccion el domingo.",
            "excerpt": "La Semana 7 de la NFL continua el domingo con atractivos duelos. Kansas City visita a Seattle en el Sunday Night Football.",
            "body": [
                "La NFL se prepara para un domingo repleto de accion en la Semana 7, con tres equipos invictos poniendo a prueba sus marcas perfectas el 25 de octubre. El duelo estelar del Sunday Night Football enfrentara a Patrick Mahomes y los Kansas City Chiefs (5-0) ante los Seattle Seahawks en el hostil Lumen Field. En la NFC, los lideres San Francisco 49ers (6-0) visitan a los Atlanta Falcons, mientras que los invictos Minnesota Vikings (5-0) reciben a los Indianapolis Colts.",
                "La jornada inicio con gran emocion el jueves por la noche en Soldier Field, donde los Chicago Bears resistieron ante los New England Patriots 30-24. Caleb Williams brillo con 308 yardas por pase y dos anotaciones, y Cairo Santos aseguro la victoria con un gol de campo de 58 yardas a 1:34 del final. Con esto, Chicago se coloco con 5-2 y los Patriots cayeron a 4-3."
            ]
        },
        "de": {
            "title": "NFL Woche 7 vor dem Sonntag: Ungeschlagenes Trio bereit, Bears feiern TNF-Sieg",
            "subtitle": "Chicago verbessert sich auf 5-2 nach Sieg ueber New England. 49ers, Chiefs und Vikings wollen am Sonntag makellos bleiben.",
            "excerpt": "NFL Woche 7 geht am Sonntag mit packenden Duellen weiter. Kansas City gastiert im Sunday Night Football in Seattle.",
            "body": [
                "Die NFL steht vor einem mitreissenden Sonntag in Woche 7, wenn drei noch ungeschlagene Teams am 25. Oktober ihre weisse Weste verteidigen. Das Highlight im Sunday Night Football steigt in Seattle, wo Patrick Mahomes und die Kansas City Chiefs (5-0) im lautstarken Lumen Field antreten. In der NFC reisen die San Francisco 49ers (6-0) zu den Atlanta Falcons, waehrend die Minnesota Vikings (5-0) die Indianapolis Colts empfangen.",
                "Eroeffnet wurde der Spieltag am Donnerstag mit einem packenden 30-24-Heimsieg der Chicago Bears ueber die New England Patriots im Soldier Field. Caleb Williams glaenzte mit 308 Pass-Yards und zwei Touchdowns, waehrend Cairo Santos mit einem 58-Yard-Field-Goal kurz vor Schluss alles klar machte. Die Bears verbesserten sich damit auf 5-2, waehrend die Patriots auf 4-3 zurueckfielen."
            ]
        },
        "it": {
            "title": "NFL Week 7 vigilia di domenica: il trio di imbattuti pronto, i Bears festeggiano",
            "subtitle": "Chicago sale a 5-2 dopo il successo su New England. 49ers, Chiefs e Vikings cercano la perfezione domenica.",
            "excerpt": "La Week 7 NFL prosegue domenica con grandi sfide. Kansas City fa visita a Seattle nel Sunday Night Football.",
            "body": [
                "La NFL si prepara a una domenica ricca di spettacolo nella Week 7, con tre franchigie imbattute che metteranno alla prova la loro imbattibilita il 25 ottobre. Il big match del Sunday Night Football vedra Patrick Mahomes e i Kansas City Chiefs (5-0) far visita ai Seattle Seahawks nel caldissimo Lumen Field. Nella NFC, i capolisti San Francisco 49ers (6-0) volano ad Atlanta, mentre i sorprendenti Minnesota Vikings (5-0) attendono gli Indianapolis Colts.",
                "Il turno si era aperto giovedi notte al Soldier Field con la vittoria dei Chicago Bears sui New England Patriots per 30-24. Caleb Williams ha guidato l'attacco con 308 yard e due touchdown, prima del field goal da 58 yard di Cairo Santos che ha chiuso i giochi a 1:34 dalla sirena. Chicago e salita sul 5-2 mentre New England e scivolata sul 4-3."
            ]
        },
        "pl": {
            "title": "NFL Tydzien 7 przed niedziela: Niepokonane trio gotowe, Bears swietuja wygrana w TNF",
            "subtitle": "Chicago poprawia bilans na 5-2 po pokonaniu Nowej Anglii. 49ers, Chiefs i Vikings chca utrzymac perfekcje w niedziele.",
            "excerpt": "Tydzien 7 w NFL trwa w najlepsze: Kansas City zmierzy sie z Seattle w niedzielnym meczu wieczoru.",
            "body": [
                "Liga NFL szykuje sie na pelna emocji niedziele w 7. tygodniu rozgrywek, kiedy trzy niepokonane ekipy sprawdza swoja forme 25 pazdziernika. W hicie Sunday Night Football Patrick Mahomes i Kansas City Chiefs (5-0) zagraja w Seattle przeciwko Seahawks na goracym terenie Lumen Field. W konferencji NFC liderzy San Francisco 49ers (6-0) zagraja w Atlancie z Falcons, a rewelacyjni Minnesota Vikings (5-0) podejma Indianapolis Colts.",
                "Tydzien rozpoczal sie w czwartek na Soldier Field, gdzie Chicago Bears pokonali New England Patriots 30-24. Caleb Williams rozegral swietny mecz, rzucajac 308 jardow i dwa przylozenia, a Cairo Santos przypieczetowal sukces trafieniem z 58 jardow na 1:34 przed koncem. Dzieki temu Bears poprawili swoj bilans na 5-2, spychajac Patriots na 4-3."
            ]
        },
        "zh": {
            "title": "NFL第7周超级周日前瞻：三支不败之师整装待发，熊队欢庆周四夜赛胜利",
            "subtitle": "芝加哥击败新英格兰战绩升至5胜2负。49人、酋长与维京人周日力争延续全胜势头。",
            "excerpt": "NFL第7周超级周日即将开战。堪萨斯城酋长在周日夜赛客场挑战西雅图海鹰。",
            "body": [
                "NFL第7周即将迎来精彩纷呈的周日大战，三支开季至今保持不败的劲旅将在10月25日迎接严峻考验。周日夜赛焦点战中，帕特里克·马霍姆斯率领的堪萨斯城酋长（5胜0负）将做客流明球场挑战西雅图海鹰。国联方面，全联盟领头羊旧金山49人（6胜0负）客场挑战亚特兰大猎鹰，而保持全胜的明尼苏达维京人（5胜0负）将在主场迎战印第安纳波利斯小马。",
                "本周战火在周四晚间的军人球场点燃，芝加哥熊队以30-24力克新英格兰爱国者。四分卫凯莱布·威廉姆斯发挥稳健轰出308码和2次达阵，开罗·桑托斯在比赛最后阶段命中平队史纪录的58码任意球锁定胜局。此役过后熊队将战绩改写为5胜2负，爱国者战绩跌至4胜3负。"
            ]
        },
        "ja": {
            "title": "NFL第7週日曜決戦前夜：全勝3チームが出撃へ、ベアーズはTNF勝利に沸く",
            "subtitle": "ペイトリオッツを下したシカゴが5勝2敗に。49ers、チーフス、バイキングスが日曜に全勝キープを狙う。",
            "excerpt": "NFL第7週は日曜も注目カードが目白押し。サンデーナイト・フットボールでチーフスが敵地シアトルに乗り込む。",
            "body": [
                "NFL第7週は10月25日日曜に大注目のゲームが並び、ここまで無敗を維持する3チームが真価を問われます。サンデーナイト・フットボールではパトリック・マホームズ率いるカンザスシティ・チーフス（5勝0敗）が敵地ルーメン・フィールドでシアトル・シーホークスと激突。NFCでは首位のサンフランシスコ・49ers（6勝0敗）がアトランタへ遠征し、無敗のミネソタ・バイキングス（5勝0敗）はインディアナポリス・コルツを本拠地に迎えます。",
                "今週は木曜夜にソルジャー・フィールドで開幕し、シカゴ・ベアーズがニューイングランド・ペイトリオッツを30-24で下しました。ケイレブ・ウィリアムズが308パスヤードと2TDを記録し、カイロ・サントスが試合終了間際に58ヤードのFGを沈めて勝利を確定。ベアーズは5勝2敗とし、ペイトリオッツは4勝3敗に後退しました。"
            ]
        },
        "ko": {
            "title": "NFL 7주차 슈퍼 선데이 전야: 무패 3총사 출격 대기, 베어스 TNF 승리 환호",
            "subtitle": "뉴잉글랜드를 제압한 시카고 5승 2패. 49ers, 치프스, 바이킹스 일요일 전승 행진 도전.",
            "excerpt": "NFL 7주차 일요일 대진이 펼쳐집니다. 선데이 나이트 풋볼에서는 캔자스시티가 시애틀 원정을 떠납니다.",
            "body": [
                "NFL 7주차 슈퍼 선데이가 10월 25일 막을 올립니다. 개막 후 무패를 달리고 있는 세 팀이 완벽한 성적표를 걸고 시험대에 오릅니다. 최고의 빅매치인 선데이 나이트 풋볼에서는 패트릭 마홈스의 캔자스시티 치프스(5승 0패)가 시애틀 시호크스의 홈구장 루멘 필드로 원정을 떠납니다. NFC에서는 리그 선두 샌프란시스코 49ers(6승 0패)가 애틀랜타 팰컨스와 맞붙고, 무패 돌풍의 미네소타 바이킹스(5승 0패)는 인디애나폴리스 콜츠를 상대합니다.",
                "이번 주차는 목요일 밤 솔저 필드에서 화려하게 개막했습니다. 시카고 베어스는 뉴잉글랜드 패트리어츠를 30-24로 제압했습니다. 쿼터백 케イレ브 윌리엄스가 308패싱야드 2TD로 맹활약했고, 카이로 산토스가 경기 종료 1분 34초 전 58야드 필드골을 작렬시켜 승리를 매듭지었습니다. 시카고는 5승 2패로 올라섰고 패트리어츠는 4승 3패가 되었습니다."
            ]
        },
        "ar": {
            "title": "NFL الاسبوع 7 عشية الاحد: ثلاثي الصدارة بلا هزيمة يتاهب وبيرز يحتفل بفوز TNF",
            "subtitle": "شيكاغو يصعد الى 5-2 بعد اسقاط نيو انغلاند. و49رز وتشيفس وفايكنغز يطمحون لمواصلة السجل المثالي يوم الاحد.",
            "excerpt": "تتواصل منافسات الاسبوع السابع من NFL يوم الاحد بمواجهات كبرى. كانساس سيتي يحل ضيفا على سياتل في سهرة الاحد.",
            "body": [
                "تستعد رابطة كرة القدم الامريكية NFL ليوم احد حافل بالاثارة في الاسبوع السابع، حيث تضع ثلاثة فرق لم تتذوق طعم الخسارة سجلها المثالي على المحك في 25 اكتوبر. وتبرز مواجهة الاحد ليلا حين يحل باتريك ماهومز وكانساس سيتي تشيفس (5-0) ضيوفا على سياتل سيهوكس في ملعب لومن فيلد. وفي مؤتمر NFC، يحل المتصدر سان فرانسيسکو 49رز (6-0) ضيفا على اتلانتا فالكونز، بينما يستضيف مينيسوتا فايكنغز (5-0) فريق انديانابوليس كولتس.",
                "وكان الاسبوع السابع قد انطلق باثارة بالغة مساء الخميس على ملعب سولجر فيلد، حين تفوق شيكاغو بيرز على نيو انغلاند باتريوتس 30-24. وقدم كاليب ويليامز اداء رائعا مسجلا 308 ياردات تمرير وهدفين، قبل ان يسجل كايرو سانتوس هدفا ميدانيا من 58 ياردة ليحسم اللقاء مع تبقي 1:34 دقيقة. ورفع شيكاغو رصيده الى 5-2 بينما تراجع باتريوتس الى 4-3."
            ]
        }
    }
}

# Strict validation
for slug, langs in OCT24_STORIES.items():
    assert len(langs) == 9, f"{slug} missing some of the 9 languages: {list(langs.keys())}"
    for lang in ["fr", "es", "de", "it", "pl", "zh", "ja", "ko", "ar"]:
        assert lang in langs, f"{slug} missing language {lang}"
        trans = langs[lang]
        for field in ["title", "subtitle", "excerpt", "body"]:
            assert field in trans, f"{slug} {lang} missing field {field}"
            val = trans[field]
            if isinstance(val, str):
                assert "—" not in val, f"Em-dash in {slug} {lang} {field}"
                assert "--" not in val, f"Double-hyphen in {slug} {lang} {field}"
            elif isinstance(val, list):
                for i, item in enumerate(val):
                    assert "—" not in item, f"Em-dash in {slug} {lang} {field}[{i}]"
                    assert "--" not in item, f"Double-hyphen in {slug} {lang} {field}[{i}]"

print("Verification passed! No em-dashes or double-hyphens found in any of the 6 stories across all 9 languages.")

snippet_parts = []
for slug, langs in OCT24_STORIES.items():
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

print("Successfully injected October 24 translations into frontend/src/i18n/stories.ts")
