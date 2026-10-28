# -*- coding: utf-8 -*-
import json
import re

OCT28_STORIES = {
    "carabao-cup-2026-fleetwood-town-stun-arsenal-shootout-miracle": {
        "fr": {
            "title": "Exploit en Carabao Cup : Fleetwood Town (D4) elimine Arsenal au bout d'une seance de tirs au but epique",
            "subtitle": "Le club de League Two tient les Gunners en echec 1-1 avant qu'Harrington ne repousse le tir de Saka pour une victoire 5-3.",
            "excerpt": "Fleetwood Town a signe mardi l'une des plus grandes surprises de l'histoire de la Coupe de la Ligue en sortant Arsenal aux tirs au but.",
            "body": [
                "Le football anglais a vecu une soiree magique ce mardi 27 octobre avec l'elimination d'Arsenal, co-leader de Premier League, par Fleetwood Town, pensionnaire de quatrieme division. Dans un Highbury Stadium balaye par le vent de la cote du Lancashire, les 5 124 supporters locaux ont porte leur equipe tout au long d'un match heroique conclu par une seance de tirs au but historique (5-3) apres un score de 1-1. Aaron Loupalo-Bi a fait exploser les tribunes juste avant la mi-temps en reprenant de la tete un corner au second poteau.",
                "Mikel Arteta a du faire appel a son banc en seconde periode, et Viktor Gyokeres a egalise a la 76e minute d'une frappe rasee. Mais l'expulsion directe du jeune Max Dowman a la 84e minute a redonne foi aux locaux. Lors de la seance de penalties, le gardien David Harrington a detourne la frappe de Bukayo Saka avant que Ryan Broom ne scelle la qualification pour les quarts de finale, une premiere en 118 ans d'existence pour Fleetwood."
            ]
        },
        "es": {
            "title": "Milagro en la Copa de la Liga: Fleetwood Town de cuarta division elimina a Arsenal en los penaltis",
            "subtitle": "El humilde equipo de League Two empata 1-1 y Harrington detiene el tiro de Saka en un memorable 5-3 en Highbury.",
            "excerpt": "Fleetwood Town protagonizo el martes una de las mayores sorpresas del futbol moderno al apear al Arsenal en los penaltis.",
            "body": [
                "La magia de la copa inglesa brillo en todo su esplendor este martes 27 de octubre, cuando el Fleetwood Town, modesto equipo de la cuarta division, echo de la Carabao Cup al colider de la Premier League, el Arsenal. En un Highbury Stadium desatado por 5.124 espectadores, el equipo costero resistio con bravura para sellar el 1-1 y llevarse la gloria en los penaltis por 5-3. Aaron Loupalo-Bi desato el delirio al filo del descanso con un soberbio cabezazo a la salida de un corner.",
                "Pese a que Viktor Gyokeres igualo el choque en el minuto 76 tras entrar desde el banquillo, la expulsion por roja directa del juvenil Max Dowman en el minuto 84 devolvio la energia al conjunto local. En la tanda fatidica, el portero David Harrington se convirtio en leyenda al desviar el tiro de Bukayo Saka, dejando en bandeja a Ryan Broom el penal definitivo que clasifico a Fleetwood a cuartos de final por primera vez en 118 anos de historia."
            ]
        },
        "de": {
            "title": "Pokal-Wunder an der Kueste: Viertligist Fleetwood Town wirft Arsenal im Elfmeterschießen raus",
            "subtitle": "Der League-Two-Klub trotzt den Gunners ein 1:1 ab; Harrington pariert gegen Saka beim dramatischen 5:3-Triumph.",
            "excerpt": "Fleetwood Town sorgte am Dienstag fuer eine der groessten Pokal-Sensationen der Moderne und warf Arsenal im Elfmeterschießen aus dem Wettbewerb.",
            "body": [
                "Der englische Pokalfussball erlebte am Dienstag, den 27. Oktober, eine Sternstunde: Der viertklassige Klub Fleetwood Town warf den Premier-League-Spitzenreiter Arsenal mit 5:3 im Elfmeterschießen aus dem Carabao Cup. Im windigen Highbury Stadium peitschten 5.124 Fans ihr Team zu einer heroischen Abwehrschlacht. Aaron Loupalo-Bi brachte die Gastgeber kurz vor der Pause per Kopfball nach einer Ecke in Fuehrung.",
                "Arsenal glich in der 76. Minute durch den eingewechselten Viktor Gyokeres aus, verlor jedoch kurz vor Schluss Nachwuchshoffnung Max Dowman nach einer Notbremse per Roter Karte. Im Elfmeterschießen avancierte Torhueter David Harrington zum Helden, indem er den Schuss von Bukayo Saka parierte, ehe Ryan Broom den entscheidenden Elfmeter verwandelte und Fleetwood zum ersten Mal in der 118-jaehrigen Vereinsgeschichte ins Viertelfinale schoss."
            ]
        },
        "it": {
            "title": "Miracolo in Carabao Cup: il Fleetwood Town (D4) elimina l'Arsenal ai calci di rigore",
            "subtitle": "La formazione di quarta serie ferma i Gunners sull'1-1 prima della parata decisiva di Harrington su Saka nel 5-3 finale.",
            "excerpt": "Il Fleetwood Town ha firmato martedi una delle imprese piu clamorose della storia della Coppa di Lega, estromettendo l'Arsenal dal dischetto.",
            "body": [
                "La magia del calcio inglese si e manifestata martedi 27 ottobre con l'incredibile successo del Fleetwood Town, club di League Two, che ha eliminato l'Arsenal dalla Carabao Cup. Davanti ai 5.124 tifosi di Highbury Stadium, la squadra di quarta serie ha disputato una gara commovente chiusa sull'1-1 prima di trionfare 5-3 ai rigori. Aaron Loupalo-Bi ha sbloccato la sfida al 41' minuto con un imperioso colpo di testa da corner.",
                "Mikel Arteta ha inserito i suoi titolari e Viktor Gyokeres ha trovato il pareggio al 76', ma il cartellino rosso sventolato a Max Dowman all'84' ha restituito coraggio ai padroni di casa. Nella serie di rigori il portiere David Harrington ha neutralizzato il tiro di Bukayo Saka, consentendo a Ryan Broom di realizzare il rigore decisivo e regalare al Fleetwood i primi quarti di finale nei suoi 118 anni di vita."
            ]
        },
        "pl": {
            "title": "Cud w Pucharze Ligi: Czwartoligowe Fleetwood Town wyrzuca Arsenal po rzutach karnych",
            "subtitle": "Druzyna z League Two remisuje 1:1, a Harrington broni karny Saki przy historycznym triumfie 5:3 w serii jedenastek.",
            "excerpt": "Fleetwood Town sprawilo we wtorek jedna z najwiekszych sensacji w dziejach Carabao Cup, eliminujac Arsenal w rzutach karnych.",
            "body": [
                "Angielski futbol pucharowy napisal we wtorek 27 pazdziernika niesamowity rozdzial: czwartoligowe Fleetwood Town wyeliminowalo wspolnego lidera Premier League, Arsenal. Na stadionie Highbury 5 124 kibicow ogladalo heroiczna walke zakonczona remisem 1:1 i zwycieska seria karnych 5:3. Gospodarze objeli prowadzenie w 41. minucie po strzale glowa Aarona Loupalo-Bi z rzutu roznego.",
                "W drugiej polowie rezerwowy Viktor Gyokeres wyrownal stan meczu w 76. minucie, lecz czerwona kartka dla nastoletniego Maxa Dowmana w 84. minucie przywrocila wiare gospodarzom. W konkursie jedenastek bramkarz David Harrington obronil strzal Bukayo Saki, a decydujacy strzal Ryana Brooma wprowadzil Fleetwood do cwiercfinalu po raz pierwszy w 118-letniej historii klubu."
            ]
        },
        "zh": {
            "title": "联赛杯奇迹之夜：英乙弗利特伍德点球大战淘汰阿森纳爆出惊天大冷",
            "subtitle": "第四级别弱旅常规时间1-1逼平枪手，门将哈灵顿扑出萨卡点球助球队5-3创造建队118年历史。",
            "excerpt": "弗利特伍德在周二创造了现代英格兰联赛杯历史上最不可思议的奇迹之一，点球大战击溃阿森纳挺进八强。",
            "body": [
                "英格兰足球在10月27日周二见证了最具浪漫色彩的杯赛爆冷：英乙联赛排名靠后的弗利特伍德坐镇海布里球场，在5124名主场球迷的呐喊声中，鏖战120分钟战成1-1平，最终通过点球大战5-3将英超领头羊阿森纳淘汰出局。上半场第41分钟，阿隆·卢帕洛-比接角球头球破门，引爆了整座海滨球场。",
                "下半场阿尔特塔换上主力救场，约克雷斯在第76分钟低射扳平比分。然而第84分钟阿森纳新星道曼因飞铲被直接红牌罚下，比赛天平再次倾斜。进入点球大战后，弗利特伍德门将哈灵顿飞身扑出萨卡的射门，随后布鲁姆罚入制胜点球，弗利特伍德建队118年来首次杀入联赛杯四分之一决赛。"
            ]
        },
        "ja": {
            "title": "リーグ杯の大波乱：英4部フリートウッドがPK戦で名門アーセナルを撃破する歴史的勝利",
            "subtitle": "4部クラブが1-1と耐え抜き、守護神ハリントンがサカのPKを阻止して5-3のジャイアントキリングを完遂。",
            "excerpt": "フリートウッド・タウンは火曜日、アーセナルをPK戦の末に破り、現代カラバオ杯史上最大級の大番狂わせを成し遂げた。",
            "body": [
                "イングランドのカップ戦の醍醐味が10月27日火曜日に凝縮された。英4部リーグ2に属するフリートウッド・タウンが、プレミアリーグ首位タイのアーセナルをPK戦5-3で破り大会から敗退させた。風吹きすさぶハイバリー・スタジアムの5124人の観衆の前で、前半41分にアーロン・ルパロ・ビがCKからヘディングシュートを突き刺し先制した。",
                "後半にアルテタ監督が投入したヴィクトル・ギョケレシュが76分に同点弾を決めたものの、84分に若手マックス・ドウマンが一発退場となり流れが急変。もつれ込んだPK戦では守護神デイヴィッド・ハリントンがブカヨ・サカのシュートを見事にストップ。ライアン・ブルームが最後のPKをネットに突き刺し、クラブ創設118年目で初のベスト8進出を決めた。"
            ]
        },
        "ko": {
            "title": "카라바오컵 대이변: 4부 플리트우드 타운, 승부차기 끝에 아스널 제압하고 8강 진출",
            "subtitle": "4부 언더독 1-1 맞선 뒤 해링턴 골키퍼가 사카 킥 막아내며 하이버리 스타디움서 5-3 승부차기 승리.",
            "excerpt": "플리트우드 타운이 화요일 승부차기 접전 끝에 아스널을 탈락시키며 현대 리그컵 역사상 가장 위대한 이변을 연출했다.",
            "body": [
                "잉글랜드 컵대회의 마법이 10월 27일 화요일 밤 하이버리 스타디움에서 폭발했다. 4부 리그 소속 플리트우드 타운이 프리미어리그 공동 1위 아스널을 상대로 1-1 무승부 후 승부차기 5-3 승리를 거두는 초대형 이변을 일으켰다. 전반 41분 아론 루팔로-비의 헤더 선제골로 기선을 제압하며 5,124명의 홈 팬들을 열광의 도가니에 빠뜨렸다.",
                "아스널은 후반 31분 교체 투입된 빅토르 요케레스의 동점골로 균형을 맞췄으나, 후반 39분 맥스 도먼이 다이렉트 퇴장을 당하며 수세에 몰렸다. 이어진 승부차기에서 플리트우드의 수문장 데이비드 해링턴이 부카요 사카의 킥을 환상적으로 막아냈고, 라이언 브룸이 마지막 키커로 골망을 흔들며 창단 118년 만에 최초로 8강 무대를 밟았다."
            ]
        },
        "ar": {
            "title": "معجزة كأس الرابطة: فليتوود تاون من الدرجة الرابعة يقصي أرسنال بركلات الترجيح",
            "subtitle": "فريق الدرجة الرابعة يجبر الغانرز على التعادل 1-1 قبل أن يتصدى هارينغتون لركلة ساكا في فوز تاريخي 5-3.",
            "excerpt": "حقق فليتوود تاون يوم الثلاثاء واحدة من أعظم المفاجآت في تاريخ كأس الرابطة بإقصاء متصدر الدوري الإنجليزي أرسنال.",
            "body": [
                "عاشت كرة القدم الإنجليزية ليلة استثنائية يوم الثلاثاء 27 أكتوبر عندما نجح فليتوود تاون، القابع في دوري الدرجة الرابعة، في إقصاء أرسنال متصدر الدوري الممتاز من كأس الرابطة. أمام 5124 مشجعا في ملعب هايبوري، تقدم أصحاب الأرض برأسية متقنة من آرون لوبالو-بي في الدقيقة 41 من ركلة ركنية ليشعل حماس الجماهير.",
                "وعلى الرغم من تعادل أرسنال عبر فيكتور غيوكيريس في الدقيقة 76، إلا أن طرد البديل الشاب ماكس دومان بالبطاقة الحمراء المباشرة في الدقيقة 84 أعاد التوازن لفليتوود. وفي ركلات الترجيح تألق الحارس ديفيد هارينغتون وتصدى لتسديدة بوكايو ساكا، قبل أن يسجل رايان بروم الركلة الحاسمة ليتأهل فليتوود لربع النهائي لأول مرة في تاريخه الممتد لـ 118 عاما."
            ]
        }
    },

    "wnba-finals-2026-game5-valkyries-edge-dream-nba-opening-night-wembanyama": {
        "fr": {
            "title": "Les Valkyries prennent l'avantage 3-2 en Finales tandis que la NBA s'enflamme avec Wembanyama",
            "subtitle": "Golden State etouffe Atlanta 64-55 lors du match 5 ; Wembanyama cumule 29 points et 9 dunks a San Antonio.",
            "excerpt": "L'equipe d'expansion des Valkyries n'est plus qu'a une victoire du titre WNBA apres son succes 64-55, pendant que Wembanyama illuminait la reprise NBA.",
            "body": [
                "Les Golden State Valkyries ont pris une option majeure sur le titre WNBA lundi 26 octobre en s'imposant 64-55 face a l'Atlanta Dream dans un match 5 ultra-defensif au Chase Center. Portee par 18 064 supporters en fusion a San Francisco, l'equipe californienne a limite Atlanta a seulement neuf petits points dans le dernier quart-temps. Gabby Williams a ete magistrale avec 16 points, 8 rebonds et 4 interceptions, tandis que Kayla Thornton a rentre deux tirs primes consecutifs pour faire basculer la rencontre.",
                "Le lendemain, la saison reguliere NBA 2026-27 s'est ouverte sur une demonstration magistrale de Victor Wembanyama. L'interieur francais des Spurs a compile 29 points, 10 rebonds et 4 contres en seulement 31 minutes dans une victoire ecrasante 130-103 contre Sacramento, egalant son record en carriere avec neuf dunks spectaculaires. Dans le meme temps, Jayson Tatum a inscrit 40 points pour Boston face a Brooklyn."
            ]
        },
        "es": {
            "title": "Valkyries acarician el titulo de la WNBA con ventaja 3-2 y Wembanyama asombra en el debut NBA",
            "subtitle": "Golden State frena a Atlanta 64-55 en el Partido 5; Wembanyama brilla con 29 puntos y nueve mates con los Spurs.",
            "excerpt": "Las debutantes Valkyries se colocan a un paso del anillo tras ganar 64-55, mientras Victor Wembanyama inaugura la NBA con una actuacion estelar.",
            "body": [
                "Las Golden State Valkyries dieron un paso de gigante hacia el campeonato de la WNBA este lunes 26 de octubre, al derrotar 64-55 a las Atlanta Dream en el quinto partido disputado en el Chase Center. Con una defensa ferrea que solo permitio nueve puntos en el ultimo cuarto a las visitantes, Gabby Williams lidero la ofensiva con 16 puntos y cuatro robos. Kayla Thornton rompio la igualdad con dos triples decisivos desde la esquina para poner la serie 3-2 a favor de la franquicia debutante.",
                "La noche del martes marco el arranque de la temporada NBA 2026-27 con una exhibicion portentosa de Victor Wembanyama. El prodigio galo lidero a los San Antonio Spurs en el triunfo 130-103 sobre Sacramento Kings, firmando 29 puntos, 10 rebotes, cuatro tapones e igualando su mejor marca con nueve mates demoledores. En el Este, Jayson Tatum sumo 40 puntos en la ajustada victoria de Boston ante Brooklyn."
            ]
        },
        "de": {
            "title": "Valkyries fuehren 3:2 in den WNBA-Finals waehrend Wembanyama die NBA-Saison eroeffnet",
            "subtitle": "Golden State bezwingt Atlanta mit 64:55 in Spiel 5; Wembanyama verbucht 29 Punkte und neun Dunks in San Antonio.",
            "excerpt": "Das Expansion-Team der Valkyries steht nach einem defensiven 64:55-Sieg kurz vor der Krone, waehrend Victor Wembanyama die NBA verzaubert.",
            "body": [
                "Die Golden State Valkyries rueckten am Montag, den 26. Oktober, dem WNBA-Titel ganz nah: Vor 18.064 Fans im Chase Center bezwangen sie die Atlanta Dream mit 64:55 in Spiel 5. Eine eisenharte Defensivleistung hielt Atlanta im vierten Viertel bei nur neun Zaehlern. Gabby Williams ueberragte mit 16 Punkten und vier Steals, waehrend Kayla Thornton mit zwei Dreiern in der Schlussphase die 3:2-Serienfuehrung besiegelte.",
                "Am Dienstagabend startete die NBA-Saison 2026-27 mit einem Ausrufezeichen von Victor Wembanyama. Der franzoesische Ausnahmespieler dominierte beim 130:103-Auftaktsieg der San Antonio Spurs gegen Sacramento mit 29 Punkten, zehn Rebounds und vier Blocks. Mit neun Dunks egalisierte er seinen persoenlichen Karrierebestwert. Parallel steuerte Jayson Tatum 40 Punkte zum 125:124-Sieg der Celtics gegen Brooklyn bei."
            ]
        },
        "it": {
            "title": "Le Valkyries volano sul 3-2 nelle Finals WNBA e l'NBA riparte con la magia di Wembanyama",
            "subtitle": "Golden State piega Atlanta 64-55 in Gara 5; Wembanyama domina con 29 punti e nove schiacciate a San Antonio.",
            "excerpt": "Le debuttanti Valkyries sono a una vittoria dal titolo WNBA dopo il successo per 64-55, mentre Wembanyama incanta all'esordio stagionale NBA.",
            "body": [
                "Le Golden State Valkyries si sono portate sul 3-2 nelle Finals WNBA lunedi 26 ottobre, superando le Atlanta Dream per 64-55 in una tiratissima Gara 5 al Chase Center di San Francisco. La difesa guidata da Natalie Nakase ha concesso appena nove punti alle rivali nella quarta frazione. Gabby Williams e stata il faro con 16 punti e quattro recuperi, mentre Kayla Thornton ha spaccato l'equilibrio con due triple pesantissime dall'angolo.",
                "Martedi sera l'opening night NBA ha regalato subito spettacolo grazie a Victor Wembanyama. Il fenomeno francese ha trascinato i San Antonio Spurs al travolgente 130-103 sui Sacramento Kings con 29 punti, 10 rimbalzi e 4 stoppate in appena 31 minuti, pareggiando il suo primato in carriera con nove schiacciate. A Est, Jayson Tatum ne ha messi 40 nel successo al fotofinish di Boston su Brooklyn."
            ]
        },
        "pl": {
            "title": "Valkyries obejmuja prowadzenie 3-2 w Finalach WNBA, a Wembanyama otwiera sezon NBA z przytupem",
            "subtitle": "Golden State pokonuje Atlante 64:55 w meczu numer 5; Wembanyama notuje 29 punktow i dziewiec wsadow dla Spurs.",
            "excerpt": "Debiutujace Valkyries dzieli jedno zwyciestwo od tytulu mistrzowskiego po triumfie 64:55, podczas gdy Victor Wembanyama zachwycil na inauguracje NBA.",
            "body": [
                "Koszykarki Golden State Valkyries sa o krok od historycznego mistrzostwa WNBA po wygranej 64:55 z Atlanta Dream w poniedzialkowym meczu numer 5 w Chase Center. Przed kompletem 18 064 widzow defensywa gospodyn pozwolila rywalkom na zdobycie zaledwie dziewieciu punktow w czwartej kwarcie. Gabby Williams poprowadzila zespol z 16 punktami i czterema przechwytami, a seria rzutow za trzy Kayli Thornton dala prowadzenie 3-2 w finale.",
                "Zaledwie dobe pozniej we wtorek wystartowal sezon NBA 2026-27, a show skradl Victor Wembanyama. Gwiazdor San Antonio Spurs zdobyl 29 punktow, zebral 10 pilek i zablokowal cztery rzuty w wygranym 130:103 meczu z Sacramento Kings, wyrownujac swoj rekord kariery dzieki dziewieciu efektownym wsadom. W Bostonie Jayson Tatum rzucil 40 punktow w wygranym 125:124 dreszczowcu z Brooklynem."
            ]
        },
        "zh": {
            "title": "金州女武神总决赛3-2夺得赛点，文班亚马29分9记暴扣引爆NBA揭幕战",
            "subtitle": "女武神末节仅让老鹰得9分以64-55取胜；文班亚马统治攻防助马刺大胜国王，塔图姆空砍40分助绿军险胜。",
            "excerpt": "新军女武神在总决赛天王山之战中以64-55击败老鹰手握赛点，文班亚马则在NBA揭幕战中打出统治级表现。",
            "body": [
                "金州女武神在10月26日周一的大通中心迈出了创造历史的关键一步。在这场总决赛G5防守大战中，女武神末节上演窒息防守仅让亚特兰大梦想得到9分，最终以64-55锁定胜局，在七场四胜制系列赛中以3-2抢下赛点。威廉姆斯砍下全队最高的16分并送出4次抢断，桑顿在第四节胶着时刻连中两记底角三分彻底杀死比赛悬念。",
                "周二晚间2026-27赛季NBA常规赛正式揭幕，文班亚马用无可阻挡的统治力点燃全场。在马刺130-103大胜国王的比赛中，这位法国超级巨星出场31分钟便轰下29分、10个篮板和4次封盖，全场奉献9次势大力沉的暴扣追平个人生涯最高纪录。同日凯尔特人双加时125-124险胜篮网，塔图姆独得40分。"
            ]
        },
        "ja": {
            "title": "ヴァルキリーズがWNBAファイナルで3-2と王手、NBA開幕戦ではウェンバンヤマが29得点9ダンクの大暴れ",
            "subtitle": "GSVが第4Qをわずか9点に抑え64-55で勝利；スパーズのウェンバンヤマが攻守で圧倒しキングスを粉砕。",
            "excerpt": "新規参入のヴァルキリーズが64-55の守備戦を制して初優勝に王手をかけ、NBAではウェンバンヤマが衝撃の開幕戦を飾った。",
            "body": [
                "ゴールデンステート・ヴァルキリーズが10月26日月曜日、チェイス・センターの大観衆の前でアトランタ・ドリームを64-55で退け、WNBAファイナル制覇まであと1勝に迫った。第4クォーターに相手をわずか9点に抑え込む鉄壁のディフェンスを披露。ギャビー・ウィリアムズが16得点4スティールを記録し、ケイラ・ソーントンが勝負どころで2本の3ポイントを沈めて3勝2敗とした。",
                "翌27日火曜日にはNBAの2026-27シーズンが開幕し、ビクター・ウェンバンヤマが衝撃的なパフォーマンスを見せた。キングス戦でわずか31分の出場ながら29得点、10リバウンド、4ブロックを記録し130-103の圧勝を牽引。キャリアハイに並ぶ9本の豪快ダンクを叩き込んだ。ボストンではジェイソン・テイタムが40得点を挙げ、ネッツを125-124で下している。"
            ]
        },
        "ko": {
            "title": "발키리스 파이널 3-2로 우승 눈앞, NBA 개막전서는 웸반야마 29득점 9덩크 대폭발",
            "subtitle": "골든스테이트, 4쿼터 실점 9점으로 묶고 64-55 승리; 웸반야마 공수 장악하며 스퍼스 130-103 대승 견인.",
            "excerpt": "창단 첫해 발키리스가 64-55로 파이널 5차전을 잡으며 우승에 단 1승만 남겼고, NBA 무대선 웸반야마가 개막전 영웅으로 떴다.",
            "body": [
                "골든스테이트 발키리스가 10월 26일 월요일 체이스 센터에서 열린 2026 WNBA 파이널 5차전에서 애틀랜타 드림을 64-55로 제압했다. 4쿼터 상대 득점을 9점으로 묶는 완벽한 질식 수비를 앞세워 시리즈 전적 3-2를 만들었다. 개비 윌리엄스가 16득점 8리바운드 4스틸로 맹활약했고, 케일라 손턴이 4쿼터 연속 코너 3점포를 터뜨리며 승부에 쐐기를 박았다.",
                "화요일 밤에는 2026-27 NBA 정규리그가 개막하며 빅터 웸반야마의 독무대가 펼쳐졌다. 웸반야마는 새크라멘토 킹스와의 개막전에서 31분간 29득점 10리바운드 4블록을 기록하고 개인 최다 타이인 9개의 덩크슛을 꽂아 넣으며 130-103 압승을 이끌었다. 보스턴의 제이슨 테이텀도 40득점을 쏟아부으며 브루클린을 125-124로 꺾었다."
            ]
        },
        "ar": {
            "title": "فالكيريز يتقدمون 3-2 في نهائي السيدات، وضربة بداية نارية لموسم السلة الأمريكي بقيادة ويمبانياما",
            "subtitle": "غولدن ستيت يقيد أتلانتا بـ 9 نقاط في الربع الرابع ليفوز 64-55؛ وويمبانياما يسجل 29 نقطة و9 دنك في سان أنطونيو.",
            "excerpt": "أصبح فريق فالكيريز الوافد الجديد على بعد فوز واحد من التتويج بلقب WNBA بعد الفوز 64-55، بينما أشعل ويمبانياما انطلاقة NBA.",
            "body": [
                "اقترب فريق غولدن ستيت فالكيريز من كتابة التاريخ في نهائي دوري السيدات الأمريكي لكرة السلة يوم الاثنين 26 أكتوبر، بعد فوزه الدفاعي المثير 64-55 على أتلانتا دريم في المباراة الخامسة على ملعب تشيس سنتر. ونجحت دفاعات فالكيريز في حرمان أتلانتا من التسجيل، مكتفية بـ 9 نقاط فقط في الربع الأخير، بفضل تألق غابي ويليامز بـ 16 نقطة و4 قطوعات للكرة.",
                "وفي مساء الثلاثاء، انطلق موسم دوري الرجال 2026-27 بعرض استثنائي من العملاق الفرنسي فيكتور ويمبانياما. قاد ويمبي فريقه سان أنطونيو سبيرز لسحق سكرامنتو كينغز 130-103، مسجلا 29 نقطة و10 متابعات و4 تصديات، مع معادلة رقمه القياسي بـ 9 ضربات ساحقة دنك في 31 دقيقة فقط. كما سجل جايسون تاتوم 40 نقطة ليقود بوسطن للفوز على بروكلين 125-124."
            ]
        }
    },

    "nfl-week7-wrap-cowboys-blow-out-eagles-packers-panthers-tnf-2026": {
        "fr": {
            "title": "Les Cowboys corrigent les Eagles 38-21 au MNF : Prescott lance trois TD avant Packers-Panthers jeudi",
            "subtitle": "Dallas s'impose avec autorite a Philadelphie et remonte a 3-4 ; Minnesota (6-0) reste la seule franchise invaincue.",
            "excerpt": "Dak Prescott a mystifie la defense des Eagles avec 288 yards et trois passes de touchdown, relancant Dallas dans la course aux playoffs.",
            "body": [
                "Les Dallas Cowboys ont fait taire les critiques lundi soir 26 octobre en allant s'imposer 38-21 sur la pelouse de leurs rivaux historiques, les Philadelphia Eagles. En l'absence de Jalen Hurts blesse a la cheville, Philadelphie s'en remettait a Tanner McKee. Mais le quarterback remplacant n'a rien pu faire face a la masterclass de Dak Prescott, auteur d'une prestation magistrale avec 21 passes reussies sur 27 pour 288 yards et trois touchdowns.",
                "CeeDee Lamb a martyrise la defense aerienne des Eagles avec 116 yards et un touchdown de 44 yards en solitaire. Cette victoire replace Dallas a 3-4 tandis que Philadelphie s'enfonce a 2-5. Apres les revers des Chiefs et des 49ers dimanche, les Vikings du Minnesota (6-0) demeurent la seule equipe invaincue de la ligue avant le coup d'envoi de la semaine 8 entre Packers et Panthers a Lambeau Field jeudi soir."
            ]
        },
        "es": {
            "title": "Cowboys arrollan a Eagles 38-21 en el MNF: Prescott lanza tres TD antes del Packers-Panthers",
            "subtitle": "Dallas conquista el Lincoln Financial Field para situarse 3-4; Vikings (6-0) queda como unico invicto antes del TNF.",
            "excerpt": "Dak Prescott lidero la exhibicion de Dallas con 288 yardas de pase y tres touchdowns en Filadelfia para reavivar la temporada de los Cowboys.",
            "body": [
                "Los Dallas Cowboys respondieron con contundencia este lunes 26 de octubre, imponiendose 38-21 a los Philadelphia Eagles a domicilio en el cierre de la semana 7. Con Jalen Hurts ausente por una lesion de tobillo, los Eagles confiaron en el suplente Tanner McKee, pero no pudieron frenar a un inspiradisimo Dak Prescott, que completo 21 de 27 pases para 288 yardas y tres touchdowns sin perdidas de balon.",
                "CeeDee Lamb fue una pesadilla constante para la secundaria local, sumando 116 yardas y una anotacion de 44 yardas en el ultimo cuarto. El triunfo eleva a Dallas a 3-4 y deja a los Eagles tocados con 2-5. Con las derrotas de Chiefs y 49ers el domingo, los Minnesota Vikings (6-0) lideran la NFL como unico equipo invicto antes del choque entre Packers y Panthers en Lambeau Field el jueves por la noche."
            ]
        },
        "de": {
            "title": "Cowboys fegen Eagles mit 38:21 im MNF vom Feld: Prescott wirft 3 TDs vor Packers gegen Panthers",
            "subtitle": "Dallas dominiert in Philadelphia und verbessert sich auf 3-4; Vikings (6-0) bleiben einziges ungeschlagenes Team der NFL.",
            "excerpt": "Dak Prescott zerlegte die Eagles-Defense mit 288 Passing-Yards und drei Touchdowns und fuehrte die Cowboys zu einem wichtigen Auswaertssieg.",
            "body": [
                "Die Dallas Cowboys setzten am Montagabend, den 26. Oktober, ein dickes Ausrufezeichen im Lincoln Financial Field und schlugen die Philadelphia Eagles deutlich mit 38:21. Bei den Eagles fehlte Starting-Quarterback Jalen Hurts verletzungsbedingt, und Ersatzmann Tanner McKee war gegen einen souveraen aufspielenden Dak Prescott chancenlos. Prescott brachte 21 von 27 Paessen fuer 288 Yards und drei Touchdowns an den Mann.",
                "Receiver-Star CeeDee Lamb brillierte mit 116 Yards und einem spektakulaeren 44-Yard-Touchdown im Schlussviertel. Waehrend Dallas auf 3-4 klettert, rutschen die Eagles auf 2-5 ab. Nach den Niederlagen der Chiefs und 49ers am Sonntag sind die Minnesota Vikings (6-0) das einzige ungeschlagene Team der Liga, ehe am Donnerstag die Green Bay Packers auf die Carolina Panthers treffen."
            ]
        },
        "it": {
            "title": "I Cowboys travolgono gli Eagles 38-21 al MNF: 3 TD per Prescott in vista di Packers-Panthers",
            "subtitle": "Dallas espugna Philadelphia e sale a 3-4; i Minnesota Vikings (6-0) restano l'unica squadra imbattuta della NFL.",
            "excerpt": "Dak Prescott ha incantato con 288 yard e tre passaggi da touchdown nel Monday Night Football, rilanciando le ambizioni di Dallas.",
            "body": [
                "I Dallas Cowboys hanno risposto sul campo alle critiche lunedi sera 26 ottobre, espugnando il Lincoln Financial Field con un roboante 38-21 sui Philadelphia Eagles. Privi del titolare Jalen Hurts per una distorsione alla caviglia, gli Eagles si sono affidati a Tanner McKee, ma non hanno retto l'urto contro un Dak Prescott chirurgico: 21 completi su 27 per 288 yard e tre touchdown senza turnover.",
                "CeeDee Lamb ha fatto ammattire i defensive back avversari con 116 yard ricevute e un touchdown da 44 yard nel quarto periodo. Con questo successo Dallas sale a 3-4 e condanna Philadelphia al 2-5. Con i Chiefs e i 49ers battuti domenica, i Vikings (6-0) rimangono gli unici imbattuti della NFL in attesa del Thursday Night tra Packers e Panthers a Green Bay."
            ]
        },
        "pl": {
            "title": "Cowboys rozbijaja Eagles 38:21 w MNF: Prescott z trzema TD przed meczem Packers z Panthers",
            "subtitle": "Dallas dominuje na wyjezdzie i awansuje na bilans 3-4; Vikings (6-0) jedynym zespolem bez porazki w NFL.",
            "excerpt": "Dak Prescott rozmontowal obrone Eagles, zdobywajac 288 jardow i trzy touchdowny w poniedzialkowym klasyku w Filadelfii.",
            "body": [
                "Dallas Cowboys zamkneli 7. tydzien NFL efektownym zwyciestwem w poniedzialek 26 pazdziernika, gromiac Philadelphia Eagles 38:21 na ich wlasnym terenie. Pod nieobecnosc kontuzjowanego Jalena Hurtsa gospodarzy prowadzil Tanner McKee, jednak to Dak Prescott zagral perfekcyjne zawody: zaliczyl 21 celnych podan na 27 prob, 288 jardow i trzy przylozenia bez straty pilki.",
                "Gwiazda ataku CeeDee Lamb uzbieral 116 jardow i przypieczetowal sukces 44-jardowym touchdownem w czwartej kwarcie. Wygrana poprawia bilans Dallas do 3-4, podczas gdy Eagles spadaja na 2-5. Po niedzielnych porazkach Chiefs i 49ers, Minnesota Vikings (6-0) pozostaje jedyna niezwyciezona ekipa ligi przed czwartkowym starciem Packers z Panthers na Lambeau Field."
            ]
        },
        "zh": {
            "title": "牛仔周一夜赛38-21大胜老鹰：普雷斯科特3记达阵带队反弹，包装工周四迎战黑豹",
            "subtitle": "达拉斯攻陷费城主场战绩来到3胜4负，明尼苏达维京人（6胜0负）成为全联盟唯一不败金身。",
            "excerpt": "普雷斯科特传出288码和3次达阵，带领牛仔客场38-21击溃缺少赫茨的费城老鹰。",
            "body": [
                "达拉斯牛仔在10月26日周一夜赛中展现了强大的进攻火力，客场38-21大胜宿敌费城老鹰。由于老鹰当家四分卫赫茨脚踝扭伤缺阵，替补麦基临危受命，但在发挥极其稳定的普雷斯科特面前相形见绌。普雷斯科特全场27投21中，狂揽288码和3次达阵，且未出现任何失误。",
                "当家外接手兰姆完成7次接球斩获116码，并在第四节完成一记精彩绝伦的44码长传达阵锁定胜局。牛仔此役过后战绩提升至3胜4负重燃季后赛希望，而老鹰战绩下滑至2胜5负。随着酋长和49人在周日双双落败，6胜0负的维京人成为联盟唯一不败球队，目光已转向周四包装工主场迎战黑豹的第八周首战。"
            ]
        },
        "ja": {
            "title": "カウボーイズがMNFでイーグルスを38-21で粉砕：プレスコットが3TDパス、木曜TNFはパッカーズ対パンサーズ",
            "subtitle": "ダラスが敵地フィラデルフィアで大勝し3勝4敗に浮上；バイキングス（6勝0敗）がNFL唯一の無敗を維持。",
            "excerpt": "ダック・プレスコットが288ヤード、3TDパスを記録し、カウボーイズが敵地でイーグルスに38-21で圧勝した。",
            "body": [
                "ダラス・カウボーイズは10月26日月曜日のMNFで、宿敵フィラデルフィア・イーグルスを敵地で38-21と圧倒した。足首の負傷で欠場した先発QBジェイレン・ハーツに代わりタナー・マッキーが出場したが、ダック・プレスコットの正確無比なパスワークの前に屈した。プレスコットはパス27回中21回成功、288ヤード、3TD、ターンオーバーなしの完璧な数字を残した。",
                "ワイドレシーバーのシーディー・ラムは116ヤードを獲得し、第4クォーターに44ヤードのダメ押しTDパスをキャッチ。カウボーイズは3勝4敗へと持ち直し、イーグルスは2勝5敗へ後退した。日曜にチーフスと49ersが敗れたため、6勝0敗のミネソタ・バイキングスがNFL唯一の全勝チームとして第8週のサーズデーナイト（パッカーズ対パンサーズ）を迎える。"
            ]
        },
        "ko": {
            "title": "카우보이스 MNF서 이글스 38-21 격파: 프레스콧 3TD 대폭발, 목요일엔 패커스-팬서스 격돌",
            "subtitle": "댈러스, 필라델피아 원정 완승으로 3승 4패 반등; 바이킹스(6승 무패) 유일한 전승 팀으로 8주차 돌입.",
            "excerpt": "닥 프레스콧이 288야드 3터치다운 패스를 기록하며 카우보이스를 이끌고 필라델피아 원정에서 38-21 대승을 거뒀다.",
            "body": [
                "댈러스 카우보이스가 10월 26일 월요일 밤 라이벌 필라델피아 이글스를 38-21로 완파했다. 이글스는 주전 쿼터백 제일런 허츠가 발목 부상으로 빠진 가운데 태너 맥키가 분전했으나, 무결점 플레이를 펼친 닥 프레스콧의 벽을 넘지 못했다. 프레스콧은 27차례 패스 시도 중 21개를 적중시키며 288패싱야드 3터치다운을 기록했다.",
                "리시버 시디 램은 116야드를 기록하고 4쿼터에 쐐기 44야드 터치다운을 터뜨리며 승리를 굳혔다. 댈러스는 3승 4패로 반등에 성공했고, 이글스는 2승 5패로 추락했다. 일요일 치프스와 49ers가 모두 무너지며 6승 무패의 미네소타 바이킹스가 유일한 무패 팀으로 남은 가운데, 시선은 목요일 패커스와 팬서스의 8주차 오프닝전으로 쏠린다."
            ]
        },
        "ar": {
            "title": "كاوبويز يسحقون إيغلز 38-21 في ليلة الاثنين: بريسكوت يمرر 3 لمسات هبوط وباكرز يستعدون لبانثرز",
            "subtitle": "دالاس يفرض سيطرته في فيلادلفيا ويرتقي إلى 3-4؛ وفايكنغز (6-0) ينفرد بصدارة الفرق الخالية من الهزيمة.",
            "excerpt": "تألق داك بريسكوت بـ 288 ياردة و3 تمريرات حاسمة ليقود دالاس كاوبويز لفوز عريض على فيلادلفيا إيغلز في ليلة الاثنين.",
            "body": [
                "رد دالاس كاوبويز بقوة على منتقديه مساء الاثنين 26 أكتوبر بعدما تفوق على غريمه فيلادلفيا إيغلز بنتيجة 38-21 على أرض الأخير. في ظل غياب النجم جالين هيرتس بسبب إصابة في الكاحل، اعتمد إيغلز على الحارس البديل تانر ماكي، لكن داك بريسكوت كان في قمة مستواه بتمريره 21 كرة ناجحة من أصل 27 محاولة محققا 288 ياردة و3 لمسات هبوط دون أي خطأ.",
                "ولمع النجم سيدي لامب بالتقاطه 116 ياردة وتسجيله لمسة هبوط رائعة من مسافة 44 ياردة في الربع الأخير. الفوز رفع رصيد دالاس إلى 3 انتصارات مقابل 4 هزائم، بينما تراجع إيغلز إلى 2-5. ومع سقوط تشيفز وفورتي ناينرز يوم الأحد، ينفرد مينيسوتا فايكنغز (6-0) بسجل ناصع في انتظار انطلاق الأسبوع الثامن ليلة الخميس بلقاء باكرز وبانثرز."
            ]
        }
    },

    "atp-vienna-2026-alcaraz-subdues-khachanov-zverev-survives-epic-tiebreak": {
        "fr": {
            "title": "Frissons a Vienne : Alcaraz ecarte Khachanov en deux manches, Zverev survit a un tiebreak de folie 13-11",
            "subtitle": "Carlos Alcaraz rejoint les huitiemes de finale ; le numero 3 mondial Zverev ecarte des balles de match face a Landaluce.",
            "excerpt": "Carlos Alcaraz et Alexander Zverev ont surmonte des tests d'une rare intensite au premier tour de l'Erste Bank Open de Vienne mardi.",
            "body": [
                "Carlos Alcaraz a lance sa campagne indoor europeenne avec brio mardi 27 octobre en dominant Karen Khachanov 6-4, 7-6(5) lors du premier tour de l'Erste Bank Open a Vienne. Face a la puissance de frappe du Russe, l'Espagnol de 23 ans a remonte un break d'entree dans le premier set avant de faire parler sa vista. Au terme d'un tiebreak ultra-tendu dans la deuxieme manche, Alcaraz a fait la difference a 5-5 grace a un amorti de revers millimetre pour s'imposer en 1h48.",
                "De son cote, la tete de serie numero un Alexander Zverev est passee a un cheveu de l'elimination face au jeune espoir espagnol Martin Landaluce. Dans un combat de pres de trois heures, l'Allemand a du sauver deux balles de match dans un tiebreak d'anthologie avant de triompher 7-5, 3-6, 7-6(11). Avec la presence de Daniil Medvedev egalement en lice, le tournoi viennois s'impose deja comme le grand spectacle de cette fin de saison ATP."
            ]
        },
        "es": {
            "title": "Batalla en Viena: Alcaraz frena a Khachanov en dos sets y Zverev sobrevive a un tiebreak titanico de 13-11",
            "subtitle": "Carlos Alcaraz accede a octavos de final; el aleman Zverev levanta bolas de partido ante el joven Landaluce tras tres horas.",
            "excerpt": "Carlos Alcaraz y Alexander Zverev superaron durisimas pruebas en sus respectivos estrenos en el Erste Bank Open de Viena el martes.",
            "body": [
                "Carlos Alcaraz inicio con paso firme su gira europea bajo techo este martes 27 de octubre al batir a Karen Khachanov por 6-4 y 7-6(5) en el Erste Bank Open de Viena. Pese a ceder un quiebre en los primeros compases, el murciano reacciono con su habitual despliegue defensivo y golpes ganadores. En un tenso desempate en la segunda manga, Alcaraz rompio el 5-5 con una magistral dejada de reves antes de cerrar el partido tras una hora y 48 minutos de juego.",
                "Por su parte, el maximo favorito Alexander Zverev rozo la catastrofe frente al prometedor espanol Martin Landaluce. En un combate memorable de casi tres horas, el germano tuvo que salvar dos puntos de partido con su primer servicio antes de imponerse por 7-5, 3-6 y 7-6(11) en un desempate de 24 puntos. Con Daniil Medvedev tambien en el cuadro, Viena concentra todas las miradas del circuito en la pugna por las ATP Finals de Turin."
            ]
        },
        "de": {
            "title": "Wiener Hallenkrimi: Alcaraz besiegt Khachanov in zwei Saetzen, Zverev zittert sich durch 13:11-Tiebreak",
            "subtitle": "Carlos Alcaraz zieht ins Achtelfinale ein; Top-Seed Zverev wehrt Matchbaelle gegen Teenager Landaluce ab.",
            "excerpt": "Carlos Alcaraz und Alexander Zverev haben am Dienstag bei den Erste Bank Open in Wien packende Erstrunden-Krimis fuer sich entschieden.",
            "body": [
                "Carlos Alcaraz startete am Dienstag, den 27. Oktober, souveraen in die europaeische Hallensaison und bezwang Karen Khachanov mit 6:4 und 7:6(5) in der Wiener Stadthalle. Nach einem fruehen Break-Rueckstand kaempfte sich der 23-jaehrige Spanier mit druckvollen Vorhaenden zurueck. Im hochklassigen Tiebreak des zweiten Satzes gelang Alcaraz beim Stand von 5:5 mit einem brillanten Rueckhand-Stopp der vorentscheidende Punkt zum Matchgewinn nach 108 Minuten.",
                "Wesentlich mehr Muehe hatte Turnierfavorit Alexander Zverev, der gegen den spanischen Qualifikanten Martin Landaluce ueber fast drei Stunden an den Rand einer Niederlage gedraengt wurde. In einem dramatischen 24-Punkte-Tiebreak des dritten Satzes wehrte der Weltranglistendritte zwei Matchbaelle ab und setzte sich schließlich mit 7:5, 3:6 und 7:6(11) durch. Zusammen mit Daniil Medvedev verspricht das Wiener Feld absolute Weltklasse im Kampf um die ATP Finals in Turin."
            ]
        },
        "it": {
            "title": "Brividi a Vienna: Alcaraz piega Khachanov in due set, Zverev si salva in un tiebreak infinito per 13-11",
            "subtitle": "Carlos Alcaraz approda agli ottavi; il numero 3 del mondo Zverev cancella match point contro il giovane Landaluce.",
            "excerpt": "Carlos Alcaraz e Alexander Zverev hanno superato esordi ad altissima tensione all'Erste Bank Open di Vienna martedi.",
            "body": [
                "Carlos Alcaraz ha aperto la sua stagione indoor con una prestazione di grande spessore martedi 27 ottobre, sconfiggendo Karen Khachanov con il punteggio di 6-4, 7-6(5) a Vienna. Il fuoriclasse iberico ha rimontato un break iniziale nel primo set, imponendo il proprio ritmo negli scambi prolungati. Sul 5-5 del tiebreak della seconda frazione, Alcaraz ha inventato una sontuosa palla corta di rovescio che gli ha regalato il match point decisivo dopo un'ora e 48 minuti.",
                "Giornata di sofferenza estrema invece per la prima testa di serie Alexander Zverev, trascinato al terzo set dal ventenne spagnolo Martin Landaluce. In una maratona di quasi tre ore culminata in un tiebreak da 24 punti, il tedesco ha dovuto annullare due match point prima di spuntarla per 7-5, 3-6, 7-6(11). Con Daniil Medvedev pronto a scendere in campo, il torneo austriaco accende la corsa ai punti per le Finals di Torino."
            ]
        },
        "pl": {
            "title": "Tenisowe grzmoty w Wiedniu: Alcaraz pokonuje Chaczanowa, Zverev wygrywa tiebreak 13:11 po obronie pilek meczowych",
            "subtitle": "Carlos Alcaraz melduje sie w 1/8 finalu; turniejowa jedynka Alexander Zverev unika kleski z Landaluce po trzygodzinnej batalii.",
            "excerpt": "Carlos Alcaraz i Alexander Zverev przeszli przez niezwykle wymagajace sprawdziany w pierwszej rundzie Erste Bank Open w Wiedniu.",
            "body": [
                "Carlos Alcaraz znakomicie zainaugurowal europejska czesc sezonu halowego we wtorek 27 pazdziernika, pokonujac Karena Chaczanowa 6:4, 7:6(5) w wiedenskiej Stadthalle. Drugi tenisista swiata musial odrabiac strate przelamania w pierwszej partii, po czym zaprezentowal swoj najlepszy tenis w defensywie. Przy stanie 5:5 w tiebreaku Hiszpan popisal sie genialnym skrotem z bekhendu i zamknal spotkanie po godzinie i 48 minutach.",
                "Jeszcze wiekszych emocji dostarczyl wystep Alexandra Zvereva, ktory musial stoczyc blisko trzygodzinna walke z 20-letnim Martinem Landaluce. Niemiec obronil dwie pilki meczowe w morderczym tiebreaku decydujacego seta, zwyciezajac ostatecznie 7:5, 3:6, 7:6(11). Wobec startu Daniila Miedwiediewa turniej w Wiedniu gromadzi najwieksze gwiazdy walczace o awans do turyńskich finałów ATP."
            ]
        },
        "zh": {
            "title": "维也纳惊险开局：阿尔卡拉斯直落两盘力克哈恰诺夫，兹维列夫抢七13-11挽救赛点史诗晋级",
            "subtitle": "世界第二阿尔卡拉斯晋级十六强；头号种子兹维列夫鏖战近三小时经历24分抢七惊险击败兰达鲁塞。",
            "excerpt": "阿尔卡拉斯与兹维列夫在周二的维也纳公开赛首轮均经受住了严峻考验，双双闯入第二轮。",
            "body": [
                "卡洛斯·阿尔卡拉斯在10月27日周二开启了他的欧洲室内赛季征程，在维也纳公开赛首轮以6-4、7-6(5)击败俄罗斯名将哈恰诺夫。虽然开局遭遇破发，但西班牙名将迅速找回节奏依靠强大的底线穿透力完成逆转。在关键的第二盘抢七打到5-5平分时，阿尔卡拉斯用一记精妙绝伦的反手放短球拿到赛点，并在1小时48分钟内锁定胜利顺利杀入十六强。",
                "相比之下头号种子兹维列夫则经历了真正的生死时刻。面对年仅20岁的西班牙资格赛黑马兰达鲁塞，德国名将苦战近三个小时，在决胜盘挽救了两个赛点，最终在一场打满24分的惊心动魄抢七中以7-5、3-6、7-6(11)艰难突围。随着梅德韦杰夫即将登场，维也纳站正成为通往都灵年终总决赛最关键的战场。"
            ]
        },
        "ja": {
            "title": "ウィーン熱戦：アルカラスがハチャノフにストレート勝ち、ズベレフは13-11の死闘タイブレークを制す",
            "subtitle": "カルロス・アルカラスが16強へ進出；第1シードのズベレフはマッチポイントをしのぎ3時間の激闘を制覇。",
            "excerpt": "火曜日のエルステ・バンク・オープンでアルカラスとズベレフが揃って白熱の1回戦を突破した。",
            "body": [
                "カルロス・アルカラスが10月27日火曜日、ウィーンで行われたエルステ・バンク・オープンの1回戦でカレン・ハチャノフを6-4、7-6(5)で下し、ヨーロッパ室内シーズンを白星で滑り出した。序盤で先にブレークを許したものの持ち前の驚異的なフットワークとフォアハンドで挽回。第2セットのタイブレーク5-5からは見事なバックハンドのドロップショットを決めて1時間48分で試合を締めくくった。",
                "一方、第1シードのアレクサンダー・ズベレフは20歳のスペイン新鋭マルティン・ランダルーチェを相手に大苦戦。3時間近くに及んだ死闘の最終セットタイブレークでは相手に2本のマッチポイントを握られながらも強力なサーブで凌ぎ、7-5、3-6、7-6(11)で薄氷の勝利を収めた。メドベージェフも参戦するウィーンは、トリノ最終戦に向けた熱いポイント争いの中心地となっている。"
            ]
        },
        "ko": {
            "title": "빈 오픈 격돌: 알카라스 하차노프 제압, 츠베레프는 13-11 혈투 끝 매치포인트 극복 승리",
            "subtitle": "알카라스 16강 안착; 톱시드 츠베레프, 20세 신예 린다루세와 3시간 접전 끝 대역전승.",
            "excerpt": "카를로스 알카라스와 알렉산더 츠베레프가 화요일 에르스테 방크 오픈 1회전에서 극적인 승리를 거두고 나란히 16강에 올랐다.",
            "body": [
                "카를로스 알카라스가 10월 27일 화요일 에르스테 방크 오픈 1회전에서 카렌 하차노프를 6-4, 7-6(5)으로 꺾고 유럽 실내 하드코트 시즌을 산뜻하게 출발했다. 1세트 초반 브레이크를 허용했으나 특유의 폭발적인 기동력으로 경기를 뒤집었다. 2세트 타이브레이크 5-5 승부처에서 환상적인 백핸드 드롭샷으로 매치포인트를 잡은 뒤 1시간 48분 만에 승리를 확정지었다.",
                "반면 톱시드 알렉산더 츠베레프는 스페인의 20세 신예 마르틴 린다루세를 상대로 벼랑 끝까지 몰렸다. 장장 2시간 54분간 이어진 접전 끝에 3세트 24포인트 타이브레이크에서 두 차례 매치포인트를 막아내며 7-5, 3-6, 7-6(11)으로 간신히 승리했다. 메드베데프까지 합류한 빈 오픈은 토리노 파이널스를 향한 랭킹 포인트 전쟁의 중심지가 되고 있다."
            ]
        },
        "ar": {
            "title": "إثارة بالغة في فيينا: ألكاراز يجتاز خاتشانوف وزفيريف ينجو في شوط كسر تعادل ماراثوني 13-11",
            "subtitle": "كارلوس ألكاراز يبلغ ثمن النهائي؛ والمصنف الأول زفيريف ينقذ كرات المباراة بعد ملحمة استمرت 3 ساعات أمام لاندالوس.",
            "excerpt": "تجاوز كارلوس ألكاراز وألكسندر زفيريف اختبارين في غاية الصعوبة في افتتاح بطولة فيينا للتنس يوم الثلاثاء.",
            "body": [
                "افتتح كارلوس ألكاراز جولته الأوروبية في الملاعب المغلقة بنجاح يوم الثلاثاء 27 أكتوبر بفوزه الصعب على كارين خاتشانوف بنتيجة 6-4 و7-6(5) في بطولة فيينا. ورغم تأخره بكسر إرسال مبكر في المجموعة الأولى، استعاد النجم الإسباني إيقاعه بفضل تغطيته الرائعة للملعب، وحسم شوط كسر التعادل في المجموعة الثانية بكرة ساقطة ساحرة عند التعادل 5-5 منهيا اللقاء في ساعة و48 دقيقة.",
                "في المقابل، واجه المصنف الأول ألكسندر زفيريف خطرا حقيقيا أمام الشاب الإسباني الصاعد مارتن لاندالوس في مواجهة دامت قرابة ثلاث ساعات. ونجح النجم الألماني في إنقاذ كرتين حاسمتين للمباراة في شوط كسر التعادل المثير للمجموعة الثالثة (24 نقطة) ليفوز في النهاية 7-5 و3-6 و7-6(11). ومع انضمام دانييل ميدفيديف للمنافسات، تصبح فيينا بؤرة الصراع على التأهل لنهائيات تورينو."
            ]
        }
    },

    "f1-mexico-city-gp-2026-preview-antonelli-threshold-youngest-title": {
        "fr": {
            "title": "Presentation du GP du Mexique : Kimi Antonelli aux portes d'un titre mondial historique",
            "subtitle": "Le prodige de Mercedes n'a besoin que d'une 9e place a Mexico pour etre sacre ; Antonelli confirme qu'il gardera le numero 12.",
            "excerpt": "Fort de 123 points d'avance apres son triomphe a Austin, Antonelli arrive a Mexico ou deux points lui suffisent pour entrer dans la legende.",
            "body": [
                "Le paddock de la Formule 1 prend ses quartiers a Mexico cette semaine pour la 19e manche du championnat 2026, ou Andrea Kimi Antonelli se tient au seuil de l'immortalite sportive. Apres sa victoire eclatante depuis la pole au Texas, le prodige italien de 20 ans totalise 365 points et possede 123 points d'avance sur son equipier George Russell alors qu'il n'en reste que 125 en jeu.",
                "L'equation du titre est simple : une 9e place dimanche sur l'Autodromo Hermanos Rodriguez fera d'Antonelli le plus jeune champion du monde de l'histoire de la F1, surpassant Sebastian Vettel. Dans le paddock mexicain mercredi, Antonelli a egalement confirme qu'il conserverait son numero fetiche 12 la saison prochaine pour rendre hommage a son idole Ayrton Senna, refusant d'adopter le numero 1 reserve au champion."
            ]
        },
        "es": {
            "title": "Previa del GP de Mexico: Kimi Antonelli a las puertas del campeonato mundial de F1 mas joven de la historia",
            "subtitle": "La joya de Mercedes necesita acabar noveno en el Hermanos Rodriguez para coronarse; Antonelli confirma que mantendra el numero 12.",
            "excerpt": "Con 123 puntos de ventaja tras su recital en Austin, Kimi Antonelli aterriza en Mexico a un paso de sellar la gloria eterna en la Formula 1.",
            "body": [
                "El gran circo de la Formula 1 aterriza en la Ciudad de Mexico para la disputa de la 19ª cita del Mundial 2026, con Andrea Kimi Antonelli acariciando el trofeo de campeon. Tras su incontestable victoria de principio a fin en Austin, el piloto italiano de Mercedes lidera la clasificacion con 365 puntos, 123 por delante de su companero George Russell con solo 125 puntos en liza.",
                "Las cuentas son claras para el domingo en el Autodromo Hermanos Rodriguez: si Antonelli termina en novena posicion o mejor, se convertira en el campeon del mundo mas joven de todos los tiempos, batiendo el registro de Sebastian Vettel. Ademas, el joven piloto confirmo en el paddock que en 2027 seguira luciendo el numero 12 en honor a su gran referente de la infancia, Ayrton Senna."
            ]
        },
        "de": {
            "title": "Vorschau GP von Mexiko: Kimi Antonelli vor historischer Kroenung zum juengsten Formel-1-Weltmeister",
            "subtitle": "Dem Mercedes-Youngster genuegt Rang neun im Autodromo Hermanos Rodriguez zum WM-Titel; Antonelli behaelt die Startnummer 12.",
            "excerpt": "Mit 123 Punkten Vorsprung nach dem Triumph in Austin benoetigt Kimi Antonelli in Mexiko nur noch zwei Punkte, um Formel-1-Geschichte zu schreiben.",
            "body": [
                "Die Formel 1 gastiert an diesem Wochenende in Mexiko-Stadt zum 19. Saisonlauf 2026, und Kimi Antonelli steht unmittelbar vor dem groessten Meilenstein seiner jungen Karriere. Nach seinem Start-Ziel-Sieg beim Großen Preis der USA auf dem COTA fuehrt der 20-jaehrige Italiener die Fahrerwertung mit 365 Punkten an und liegt uneinholbare 123 Zaehler vor Teamkollege George Russell.",
                "Die Titelrechnung fuer das Rennen im Autodromo Hermanos Rodriguez ist denkbar einfach: Erreicht Antonelli Platz neun oder besser, ist er der juengste Formel-1-Weltmeister aller Zeiten und loest Sebastian Vettel ab. Zudem verriet Antonelli am Mittwoch im Fahrerlager, dass er auch als Weltmeister 2027 auf die traditionelle Startnummer 1 verzichten und zu Ehren seines Idols Ayrton Senna weiterhin mit der Nummer 12 antreten wird."
            ]
        },
        "it": {
            "title": "Presentazione GP del Messico: Kimi Antonelli a un passo dal titolo mondiale di Formula 1 piu precoce di sempre",
            "subtitle": "Al bolognese della Mercedes basta un nono posto all'Hermanos Rodriguez per laurearsi campione; confermata la vettura numero 12 per il 2027.",
            "excerpt": "Con 123 punti di margine dopo il dominio di Austin, Kimi Antonelli arriva all'alta quota di Citta del Messico per chiudere i conti iridati.",
            "body": [
                "Il paddock della Formula 1 approda a Citta del Messico per il 19° appuntamento del campionato 2026, dove Andrea Kimi Antonelli attende solo la consacrazione definitiva. Reduce dal trionfo senza sbavature al COTA in Texas, il ventenne talento della Mercedes guida la classifica con 365 punti, forte di un vantaggio di 123 lunghezze su George Russell con appena 125 punti ancora in palio.",
                "I calcoli per domenica sono elementari: con un nono posto o migliore sul circuito Hermanos Rodriguez, Antonelli diventera matematicamente il piu giovane campione del mondo nella storia della Formula 1, battendo il primato di Sebastian Vettel. Nel paddock messicano il pilota italiano ha confermato che nel 2027 non utilizzera il numero 1, mantenendo con orgoglio il numero 12 in omaggio al suo idolo di sempre, Ayrton Senna."
            ]
        },
        "pl": {
            "title": "Zapowiedz GP Meksyku: Kimi Antonelli o krok od przejscia do historii Formuly 1",
            "subtitle": "Wloski talent Mercedes potrzebuje 9. miejsca w Meksyku do tytulu mistrza swiata; Antonelli potwierdza numer 12 na bolidzie w 2027 roku.",
            "excerpt": "Mając 123 punkty przewagi po triumfie w Austin, Kimi Antonelli staje przed szansa zostania najmlodszym mistrzem swiata w dziejach F1.",
            "body": [
                "Formuła 1 zawitala do Meksyku na 19. runde sezonu 2026, w ktorej Andrea Kimi Antonelli moze ostatecznie przypieczetowac tytul mistrza swiata kierowcow. Po dominujacym zwyciestwie z pole position na torze COTA w Austin 20-letni Wloch zgromadzil 365 punktow i wyprzedza zespolowego partnera George'a Russella o 123 punkty przy zaledwie 125 mozliwych do zdobycia.",
                "Rachunek przed niedzielnym wyscigiem na Autodromo Hermanos Rodriguez jest prosty: dziewiate miejsce lub wyzsze zapewni Antonellemu tytul najmlodszego czempiona w 76-letniej historii dyscypliny, odbierajac rekord Sebastianowi Vettelowi. W srode w padoku Antonelli oswiadczyl rowniez, ze w sezonie 2027 nie wezmie numeru 1, zachowujac swoj ulubiony numer 12 dla uczczenia pamieci Ayrtona Senny."
            ]
        },
        "zh": {
            "title": "F1墨西哥大奖赛前瞻：安东内利即将加冕史上最年轻F1世界冠军",
            "subtitle": "梅赛德斯超级新星罗德里格斯赛道获第九即可锁定年度车手总冠军，确认2027赛季保留12号车号致敬塞纳。",
            "excerpt": "手握123分巨大优势，安东内利进军墨西哥高原赛道，距离打破维特尔保持的历史最年轻总冠军纪录仅差2个积分。",
            "body": [
                "2026赛季F1锦标赛第19站本周移师墨西哥城罗德里格斯赛道，年仅20岁的安东内利即将迎来职业生涯的最高光时刻。在上一站美洲赛道斩获杆位并以统治级表现夺冠后，这位意大利新星的个人积分达到365分，在赛季仅剩125分可拿的情况下领先队友拉塞尔达123分之多。",
                "周日正赛的争冠数学计算极为明朗：只要安东内利在71圈的正赛中取得第九名或更好的成绩，就将正式加冕F1历史上最年轻的年度车手总冠军，打破维特尔在2010年创下的纪录。周三在墨西哥赛道围场接受采访时，安东内利还确认即便夺冠下赛季也将继续使用12号车号，以此向儿时偶像塞纳致敬。"
            ]
        },
        "ja": {
            "title": "F1メキシコGP展望：キミ・アントネッリが史上最年少ワールドチャンピオン戴冠へ王手",
            "subtitle": "メルセデスの至宝はエルマノス・ロドリゲスで9位以上なら王座確定；2027年もセナを称えるカーナンバー12を継続使用へ。",
            "excerpt": "オースティンでの圧勝により123点差を築いたアントネッリは、高地のメキシコで史上最年少F1王者誕生の瞬間を迎える。",
            "body": [
                "2026年F1第19戦メキシコGPが今週末に開幕し、20歳のアンドレア・キミ・アントネッリが歴史的戴冠を目前にしている。前戦アメリカGPでポール・トゥ・ウィンを飾り、ドライバーズポイントを365点まで伸ばしたアントネッリは、チームメイトのジョージ・ラッセルに123点の大差をつけている（残り最大125点）。",
                "日曜日に行われる決勝でのタイトル獲得条件はシンプルそのものだ。アントネッリが9位以上でフィニッシュすれば、セバスチャン・ベッテルが持つ史上最年少ワールドチャンピオン記録を塗り替える。また水曜日のパドックでアントネッリは、タイトルを獲得した場合でも2027年にカーナンバー1を付けず、憧れのアイルトン・セナに捧げるナンバー12を維持すると明言した。"
            ]
        },
        "ko": {
            "title": "F1 멕시코시티 GP 프리뷰: 키미 안토넬리, 역대 최연소 월드 챔피언 등극 초읽기",
            "subtitle": "메르세데스 신성, 에르마노스 로드리게스서 9위만 해도 조기 우승 확정; 2027년에도 세나 기리는 12번 유지 선언.",
            "excerpt": "오스틴 완승으로 123점 리드를 확보한 안토넬리가 멕시코시티에서 F1 역대 최연소 챔피언 타이틀에 단 2점만을 남겨두고 있다.",
            "body": [
                "2026 포뮬러 원 19라운드가 멕시코시티에서 펼쳐지는 가운데, 만 20세의 키미 안토넬리가 모터스포츠 역사상 가장 눈부신 대기록을 눈앞에 두고 있다. COTA에서 폴투윈 압승을 거두며 365점을 쌓은 안토넬리는 팀 동료 조지 러셀을 123점 차로 따돌렸으며, 시즌 종료까지 남은 점수는 최대 125점에 불과하다.",
                "일요일 에르마노스 로드리게스 결선에서 안토넬리가 9위 이상으로 결승선을 통과하면 제바스티안 페텔을 넘어 F1 76년 역사상 최연소 월드 챔피언에 등극한다. 또한 안토넬리는 수요일 패덕 인터뷰에서 내년 시즌에도 1번 대신 우상 아일톤 세나를 기리는 12번을 그대로 달고 달릴 것이라고 공식 발표했다."
            ]
        },
        "ar": {
            "title": "نظرة على جائزة المكسيك: كيمي أنتونيللي على عتبة التتويج التاريخي بلقب بطولة العالم للفورمولا 1",
            "subtitle": "نجم مرسيدس الشاب بحاجة فقط للمركز التاسع في حلبة هيرمانوس رودريغيز؛ ويؤكد احتفاظه بالرقم 12 تكريما لسينا.",
            "excerpt": "بفارق 123 نقطة عقب تتويجه في أوستن، يصل كيمي أنتونيللي إلى مكسيكو سيتي لحسم أصغر لقب بطولة عالم في تاريخ الفئة الأولى.",
            "body": [
                "تحط بطولة العالم للفورمولا 1 رحالها هذا الأسبوع في العاصمة المكسيكية لخوض الجولة التاسعة عشرة من موسم 2026، حيث يقف الإيطالي كيمي أنتونيللي (20 عاما) على حافة المجد الرياضي. فبعد فوزه الساحق من نقطة الانطلاق في أوستن، وصل رصيده إلى 365 نقطة متقدما بفارق 123 نقطة على زميله جورج راسل مع بقاء 125 نقطة فقط في الحسبان.",
                "معادلة التتويج بسيطة للغاية: إنهاء سباق الأحد في المركز التاسع أو أفضل يمنح أنتونيللي رسميا لقب أصغر بطل عالم في تاريخ فورمولا 1 محطما رقم سيباستيان فيتيل. وفي حديثه في حلبة هيرمانوس رودريغيز يوم الأربعاء، أكد السائق الإيطالي أنه سيحتفظ برقمه المفضل 12 في موسم 2027 تكريما لقدوته البرازيلي الراحل آيرتون سينا بدلا من حمل الرقم 1."
            ]
        }
    },

    "pga-tour-mexico-open-2026-preview-smotherman-momentum-vidantavallarta": {
        "fr": {
            "title": "Presentation du VidantaWorld Mexico Open : Smotherman surfe sur son exploit des Bermudes a Vallarta",
            "subtitle": "Le PGA Tour pose ses valises sur le parcours signe Greg Norman alors que les joueurs se battent pour leur carte 2027.",
            "excerpt": "Apres son sacre au 3e trou de playoff aux Bermudes, Austin Smotherman emmene le peloton du VidantaWorld Mexico Open dote de 6M$.",
            "body": [
                "La serie d'automne de la FedExCup quitte les falaises des Bermudes pour la cote Pacifique du Mexique cette semaine a l'occasion du VidantaWorld Mexico Open 2026. Dispute sur le splendide parcours concu par Greg Norman a VidantaVallarta, ce tournoi dote de six millions de dollars represente un champ de bataille decisif pour les golfeurs en quete d'une exemption pleine pour la saison 2027.",
                "Austin Smotherman arrive avec le plein de confiance apres avoir remporte son deuxieme titre PGA Tour du mois dimanche a Port Royal, en venant a bout de Seamus Power au troisieme trou de playoff a -16. Tandis que Smotherman joue desormais l'esprit libere, la lutte fait rage pour les joueurs situes entre la 100e et la 125e place du classement, seuls garants de conserver leurs droits de jeu complets."
            ]
        },
        "es": {
            "title": "Previa del VidantaWorld Mexico Open: Smotherman traslada a Vallarta la inercia de su triunfo en Bermudas",
            "subtitle": "El PGA Tour se traslada al diseno de Greg Norman mientras los golfistas pelean por las cruciales tarjetas del circuito 2027.",
            "excerpt": "Tras su emocionante triunfo en el desempate en Bermudas, Austin Smotherman encabeza el plantel en el torneo de 6 millones en Vallarta.",
            "body": [
                "El calendario de otono de la FedExCup viaja de las islas atlanticas a las costas del Pacifico mexicano esta semana con la celebracion del VidantaWorld Mexico Open 2026. Con sede en el magnifico trazado Signature de Greg Norman en VidantaVallarta, el torneo de seis millones de dolares ofrece una oportunidad de oro para aquellos golfistas que pelean por asegurar sus derechos de juego para 2027.",
                "Nadie aterriza en Jalisco en mejor momento de forma que Austin Smotherman, quien sumo el domingo su segundo titulo del PGA Tour del mes de octubre tras derrotar al irlandes Seamus Power en el tercer hoyo de desempate en Port Royal. Mientras Smotherman compite con la tranquilidad de estar exento durante dos anos, la atencion se centra en la batalla de la burbuja entre los puestos 100 y 125 de la clasificacion."
            ]
        },
        "de": {
            "title": "Vorschau VidantaWorld Mexico Open: Smotherman bringt Bermuda-Schwung zum 6-Mio-Dollar-Turnier nach Vallarta",
            "subtitle": "PGA Tour schlaegt auf dem Greg-Norman-Kurs ab, waehrend Profis um ihre Spielberechtigungen fuer 2027 kaempfen.",
            "excerpt": "Nach seinem dramatischen Playoff-Triumph auf Bermuda fuehrt Austin Smotherman das Starterfeld bei der VidantaWorld Mexico Open an.",
            "body": [
                "Die FedExCup Fall Series zieht in dieser Woche von den Klippen Bermudas an die sonnige Pazifikkueste Mexikos zur VidantaWorld Mexico Open 2026. Auf dem spektakulaeren Greg Norman Signature Course in VidantaVallarta kaempft die Golf-Elite bei einem Preisgeld von 6.000.000 US-Dollar um entscheidende Punkte fuer die Tour-Karten der Saison 2027.",
                "Topfavorit Austin Smotherman reist mit breiter Brust an, nachdem er am Sonntag bei der Butterfield Bermuda Championship Seamus Power am dritten Playoff-Loch niederrang und seinen zweiten PGA-Tour-Titel innerhalb eines Monats feierte. Waehrend Smotherman seine Tour-Zukunft gesichert hat, kaempfen die Profis auf den Plaetzen 100 bis 125 um ihr sportliches Ueberleben fuer das kommende Jahr."
            ]
        },
        "it": {
            "title": "Presentazione VidantaWorld Mexico Open: Smotherman cerca il bis a Vallarta dopo il capolavoro a Bermuda",
            "subtitle": "Il PGA Tour sbarca sul tracciato disegnato da Greg Norman con in palio le carte per la stagione 2027.",
            "excerpt": "Reduce dal trionfo al playoff a Port Royal, Austin Smotherman guida il field del torneo da 6 milioni di dollari in Messico.",
            "body": [
                "La FedExCup Fall lascia le scogliere di Bermuda e sbarca sulle coste del Pacifico per il VidantaWorld Mexico Open 2026. Ospitato sul suggestivo percorso firmato Greg Norman a VidantaVallarta, l'evento mette in palio un montepremi di sei milioni di dollari e punti vitali per i golfisti a caccia dell'esenzione completa per la stagione 2027.",
                "Il giocatore piu atteso e senza dubbio Austin Smotherman, reduce dalla vittoria al terzo buco di playoff contro Seamus Power domenica scorsa. Con due titoli vinti nel solo mese di ottobre e la carta blindata per due anni, l'americano gioca senza pressioni, mentre per molti altri atleti posizionati a ridosso della 125ª posizione mondiale ogni colpo sul percorso messicano sara decisivo per il proprio futuro professionale."
            ]
        },
        "pl": {
            "title": "Zapowiedz VidantaWorld Mexico Open: Smotherman przywozi do Vallarty forme po dogrywce na Bermudach",
            "subtitle": "PGA Tour przenosi sie na pole projektu Grega Normana, gdzie trwa walka o pelne karty turniejowe na sezon 2027.",
            "excerpt": "Po emocjonujacym triumfie w dogrywce na Bermudach Austin Smotherman jest glowna postacia turnieju z pula 6 mln dolarow w Meksyku.",
            "body": [
                "Jesienna seria FedExCup Fall opuszcza atlantyckie Bermudy i zawita na pacyficzne wybrzeze Meksyku na turniej VidantaWorld Mexico Open 2026. Rozgrywane na malowniczym polu Greg Norman Signature w VidantaVallarta zawody z pula nagrod wynoszaca szesc milionow dolarow stanowia kluczowy etap walki o prawo gry w PGA Tour w 2027 roku.",
                "Nikt nie przyjezdza do Meksyku w lepszym nastroju niz Austin Smotherman. 32-letni Amerykanin wygral w niedziele swoj drugi tytul w pazdzierniku, pokonujac Seamusa Powera na trzecim dolku dogrywki w Bermuda Championship. Podczas gdy Smotherman ma juz zapewnione zwolnienie na dwa lata, gracze z miejsc 100-125 na liscie rankingowej toczyc beda dramatyczna walke o utrzymanie w elicie."
            ]
        },
        "zh": {
            "title": "维丹塔世界墨西哥公开赛前瞻：斯莫瑟曼携百慕大加洞赛夺冠之势转战瓦亚塔",
            "subtitle": "美巡赛秋季赛移师诺曼设计的锦标赛级球场，众球员为2027赛季全卡资格展开殊死搏斗。",
            "excerpt": "在百慕大第三个加洞赛艰难夺冠后，斯莫瑟曼领衔出战总奖金达600万美元的墨西哥公开赛。",
            "body": [
                "美巡赛联邦快递杯秋季赛本周从百慕大群岛转战墨西哥太平洋沿岸，2026年维丹塔世界墨西哥公开赛正式打响。在维丹塔瓦亚塔风景如画的诺曼签名球场上，总奖金高达600万美元的赛事将成为众多职业球员争夺2027赛季全卡豁免权的最关键舞台。",
                "美国名将斯莫瑟曼无疑是目前手感最火热的球员。周日他在百慕大锦标赛第三个加洞赛中击败爱尔兰名将鲍尔，一个月内斩获两座美巡赛冠军奖杯。在斯莫瑟曼提前锁定未来两年参赛资格的同时，积分榜排名第100位至125位之间的球员则面临巨大的保卡压力，每个推杆都事关职业生涯走向。"
            ]
        },
        "ja": {
            "title": "ヴィダンタ・ワールド・メキシコ・オープン展望：バミューダを制したスモザーマンが賞金600万ドル大会へ挑む",
            "subtitle": "PGAツアーはグレッグ・ノーマン設計コースへ移動；選手たちは2027年ツアーカード獲得へ死闘を展開。",
            "excerpt": "バミューダでの劇的なプレーオフ勝利を飾ったオースティン・スモザーマンがメキシコ・オープンで連勝を狙う。",
            "body": [
                "PGAツアーのフェデックスカップ・フォールは今週、大西洋のバミューダから太平洋に面したメキシコのリゾート地へ舞台を移し、2026年ヴィダンタ・ワールド・メキシコ・オープンが開幕する。ヴィダンタ・バジャルタのグレッグ・ノーマン設計コースを舞台に、賞金総額600万ドルを懸けて2027年シーズンのシード権を巡る激戦が繰り広げられる。",
                "今大会の主役はオースティン・スモザーマンだ。日曜日に行われたバミューダ選手権でシェイマス・パワーとのプレーオフ3ホール目を制し、10月だけで2勝目を挙げた。2年間のシード権を獲得し余裕を持って臨むスモザーマンに対し、ランキング100位から125位のボーダーライン上にいる選手たちはフルシード維持を懸けて一打も無駄にできない戦いに挑む。"
            ]
        },
        "ko": {
            "title": "비단타월드 멕시코 오픈 프리뷰: 버뮤다 연장 우승 스머더먼, 600만 달러 가을 무대 출격",
            "subtitle": "PGA 투어, 그렉 노먼 설계 코스서 개막; 2027시즌 투어 카드 확보 위한 살얼음판 경쟁 시작.",
            "excerpt": "버뮤다에서 3차 연장 끝에 우승을 차지한 오스틴 스머더먼이 멕시코 바야르타에서 열리는 600만 달러 대회에 출전한다.",
            "body": [
                "PGA 투어 페덱스컵 폴 시리즈가 대서양 버뮤다를 떠나 멕시코 태평양 연안으로 무대를 옮겨 2026 비단타월드 멕시코 오픈을 개최한다. 비단타바야르타의 아름다운 그렉 노먼 시그니처 코스에서 펼쳐지는 이번 대회는 총상금 600만 달러가 걸려 있으며, 2027시즌 풀시드 확보를 위한 치열한 격전지가 될 전망이다.",
                "가장 주목받는 선수는 단연 오스틴 스머더먼이다. 지난 일요일 버뮤다 챔피언십 3차 연장전에서 셰이머스 파워를 꺾고 10월에만 2승을 거두는 절정의 샷감을 자랑하고 있다. 2년 시드를 확보한 스머더먼과 달리, 페덱스컵 랭킹 100위에서 125위 사이에 위치한 선수들은 투어 카드를 지키기 위해 사활을 걸고 티샷을 날린다."
            ]
        },
        "ar": {
            "title": "نظرة على بطولة المكسيك المفتوحة: سموذر مان يدخل المنافسات بزخم تتويجه في برمودا بجوائز 6 ملايين دولار",
            "subtitle": "جولة بي جي إيه تحط رحالها في ملعب غريغ نورمان مع احتدام الصراع على بطاقات التأهل الكاملة لموسم 2027.",
            "excerpt": "بعد فوزه الدرامي في الحفرة الإضافية الثالثة في برمودا، يتصدر أوستن سموذر مان قائمة النجوم في بطولة المكسيك المفتوحة.",
            "body": [
                "تنتقل سلسلة الخريف لجولة بي جي إيه هذا الأسبوع من شواطئ برمودا إلى ساحل المكسيك على المحيط الهادئ لإقامة بطولة فيدانتا وورلد المكسيك المفتوحة 2026. وتستضيف حلبة فيدانتا فايارتا بتصميمها الرائع من غريغ نورمان منافسات البطولة البالغ مجموع جوائزها ستة ملايين دولار، والتي تشكل مرحلة حاسمة للاعبين الساعين لتأمين بطاقات المشاركة الكاملة لموسم 2027.",
                "ويدخل الأمريكي أوستن سموذر مان المنافسات بمعنويات مرتفعة للغاية بعد فوزه بلقبه الثاني في شهر أكتوبر يوم الأحد الماضي، متفوقا على الإيرلندي شيموس باور في الحفرة الفاصلة الثالثة. وفي حين يخوض سموذر مان المنافسات بأريحية بعد ضمانه بطاقة العامين، يحتدم الصراع بين اللاعبين المصنفين بين المراكز 100 و125 لضمان مقاعدهم في دوري النخبة."
            ]
        }
    }
}

# Strict validation
for slug, langs in OCT28_STORIES.items():
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
for slug, langs in OCT28_STORIES.items():
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

print("Successfully injected October 28 translations into frontend/src/i18n/stories.ts")
