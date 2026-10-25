# -*- coding: utf-8 -*-
import json
import re

OCT25_STORIES = {
    "atp-almaty-2026-medvedev-defends-title-over-basilashvili": {
        "fr": {
            "title": "Medvedev renverse Basilashvili a Almaty : premier titre conserve en carriere",
            "subtitle": "La tete de serie numero un cede le premier tiebreak avant de dominer les deux manches suivantes pour soulever son 25e trophee ATP.",
            "excerpt": "Daniil Medvedev a surmonte la resistance du qualifie Nikoloz Basilashvili 6-7(6), 6-1, 6-3 pour conserver sa couronne a l'Open d'Almaty dimanche.",
            "body": [
                "La tete de serie numero un Daniil Medvedev a franchi un cap personnel marquant ce dimanche 25 octobre en signant un retour victorieux face au qualifie georgien Nikoloz Basilashvili 6-7(6), 6-1, 6-3 en finale de l'Open d'Almaty. Ce succes apporte a Medvedev son 25e titre en simple sur le circuit ATP et son quatrieme trophee de la saison 2026. Surtout, cette victoire marque la premiere fois de sa carriere professionnelle que l'ancien numero un mondial parvient a conserver un titre conquis l'annee precedente, mettant un terme a une etonnante serie sur ses 24 premiers sacres. Basilashvili, classe au-dela du 150e rang a l'entame du tournoi avant de terrasser Stefanos Tsitsipas en demi-finale, a joue crânement sa chance. Le Georgien de 34 ans a garde son sang-froid dans un jeu decisif serre, convertissant sa deuxieme balle de set pour empocher la premiere manche 8-6 apres 54 minutes de frappes lourdes.",
                "Medvedev a reagi des l'entame de la deuxieme manche. En se rapprochant de sa ligne de fond et en trouvant des angles incisifs en revers, le Russe a breake des le deuxieme jeu pour derouler et recoller a un set partout. Dans l'ultime manche, Medvedev s'est empare du service adverse au troisieme jeu sans concéder la moindre balle de break sur son propre engagement, concluant la finale en une heure et 53 minutes. Ce sacre consolide sa place de qualification pour le Masters de fin d'annee a Turin. Pour Basilashvili, ce parcours exemplaire permettra un retour bienvenu vers le top 100 mondial au moment ou le circuit en salle rejoint Vienne et Bâle."
            ]
        },
        "es": {
            "title": "Medvedev remonta ante Basilashvili en Almaty: primera defensa de titulo en su carrera",
            "subtitle": "El maximo favorito cede el primer desempate antes de dominar los dos ultimos sets. Medvedev levanta su trofeo ATP numero 25.",
            "excerpt": "Daniil Medvedev supero una dura prueba del clasificado Nikoloz Basilashvili 6-7(6), 6-1, 6-3 para revalidar su corona en el Open de Almaty el domingo.",
            "body": [
                "El primer cabeza de serie Daniil Medvedev alcanzo un hito muy especial este domingo 25 de octubre al firmar una gran remontada ante el clasificado georgiano Nikoloz Basilashvili por 6-7(6), 6-1, 6-3 en la final del Abierto de Almaty. El triunfo otorgo a Medvedev el titulo individual numero 25 de su trayectoria en el circuito ATP y su cuarta corona de la temporada 2026. Mas significativo aun, represento la primera vez en su carrera profesional que el ex numero uno del mundo logra defender con exito un trofeo en el circuito, quebrando una curiosa racha de sus 24 conquistas anteriores. Basilashvili, situado fuera del top 150 antes de derribar a Stefanos Tsitsipas en semifinales, inicio el duelo pegando con enorme potencia. El georgiano de 34 anos mantuvo la calma en el desempate inicial, aprovechando su segundo punto de set para llevarse el parcial por 8-6 tras 54 minutos de intensos intercambios.",
                "Medvedev no tardo en responder en la segunda manga. Adelantando su posicion en la pista y encontrando angulos precisos con su reves, el maximo favorito quebro el saque en el segundo juego y solo cedio un parcial antes de equilibrar el encuentro. En el capitulo decisivo, Medvedev volvio a quebrar en el tercer juego y no enfrento un solo punto de quiebre con su servicio, cerrando la final en una hora y 53 minutos. El titulo afianza su clasificacion a las Finales ATP de Turin. Para Basilashvili, una actuacion memorable desde la clasificacion le abrira de nuevo las puertas del top 100 mundial de cara a la gira bajo techo en Viena y Basilea."
            ]
        },
        "de": {
            "title": "Medvedev kaempft Basilashvili in Almaty nieder: Erste Titelverteidigung der Karriere",
            "subtitle": "Topgesetzter verliert ersten Satz im Tiebreak und dominiert danach die Partie. Medvedev holt seinen 25. ATP-Titel.",
            "excerpt": "Daniil Medvedev bezwang Qualifikant Nikoloz Basilashvili nach hartem Kampf mit 6-7(6), 6-1, 6-3 und verteidigte am Sonntag erfolgreich seinen Titel in Almaty.",
            "body": [
                "Der topgesetzte Daniil Medvedev feierte am Sonntag, den 25. Oktober, einen besonderen persoenlichen Meilenstein, als er nach Satzrueckstand den georgischen Qualifikanten Nikoloz Basilashvili mit 6-7(6), 6-1, 6-3 im Finale der Almaty Open bezwang. Der Erfolg bescherte Medvedev den 25. ATP-Einzeltitel seiner Karriere und die vierte Trophaee der Saison 2026. Noch bedeutender: Zum allerersten Mal in seiner Profikarriere gelang es der ehemaligen Nummer eins der Welt, einen Turniersieg erfolgreich zu verteidigen. Basilashvili, der vor Turnierbeginn ausserhalb der Top 150 notiert war und im Halbfinale Stefanos Tsitsipas ausgeschaltet hatte, startete extrem druckvoll. Der 34-Jaehrige behielt im Tiebreak des ersten Satzes die Nerven und nutzte seinen zweiten Satzball nach 54 Minuten hochklassigem Grundlinienduell zum 8-6.",
                "Medvedev fand zu Beginn des zweiten Durchgangs umgehend die passende Antwort. Er rueckte naeher an die Grundlinie heran, fand mit seiner Rueckhand messerscharfe Winkel und nahm Basilashvili im zweiten Spiel das Service ab. Auf dem Weg zum Satzausgleich gab Medvedev nur ein einziges Aufschlagspiel ab. Im entscheidenden dritten Satz gelang ihm das fruehe Break zum 2-1, waehrend er bei eigenem Aufschlag keinen einzigen Breakball zuliess. Nach einer Stunde und 53 Minuten verwandelte er seinen Matchball. Der Sieg festigt Medvedevs Ticket fuer die ATP Finals in Turin. Fuer Basilashvili bedeutet der starke Lauf die Rueckkehr in Richtung der Top 100 vor den Hallenturnieren in Wien und Basel."
            ]
        },
        "it": {
            "title": "Medvedev rimonta Basilashvili ad Almaty: prima difesa del titolo in carriera",
            "subtitle": "La prima testa di serie cede il tiebreak iniziale ma domina i restanti due set. Medvedev conquista il suo 25° trofeo ATP.",
            "excerpt": "Daniil Medvedev ha piegato la tenace resistenza del qualificato Nikoloz Basilashvili 6-7(6), 6-1, 6-3 confermandosi campione all'Almaty Open domenica.",
            "body": [
                "La prima testa di serie Daniil Medvedev ha tagliato un traguardo storico personale domenica 25 ottobre, completando una brillante rimonta per battere il qualificato georgiano Nikoloz Basilashvili 6-7(6), 6-1, 6-3 nella finale dell'Almaty Open. Il successo consegna a Medvedev il 25° titolo di singolare ATP in carriera e il quarto trofeo del 2026. Soprattutto, e la prima volta in carriera che l'ex numero uno al mondo difende con successo un titolo conquistato in precedenza, interrompendo una singolare serie nei suoi primi 24 successi. Basilashvili, fuori dai primi 150 al via prima di superare Stefanos Tsitsipas in semifinale, ha martellato con grande intensita. Il 34enne georgiano ha mantenuto i nervi saldi nel tiebreak del primo set, chiudendo 8-6 al secondo set point dopo 54 minuti di scambi serrati.",
                "Medvedev ha reagito prontamente nel secondo parziale. Giocando piu vicino alla riga di fondo e aprendo angoli con il rovescio, il russo ha strappato il servizio a Basilashvili nel secondo game, concedendo un solo gioco prima di pareggiare i conti. Nel set decisivo, Medvedev ha ottenuto il break nel terzo game senza concedere palle break sul proprio servizio, chiudendo i giochi in un'ora e 53 minuti. Questa vittoria rafforza la sua posizione nella corsa verso le ATP Finals di Torino. Per Basilashvili, lo straordinario percorso portera un prezioso ritorno verso la top 100 in vista degli appuntamenti indoor di Vienna e Basilea."
            ]
        },
        "pl": {
            "title": "Medwiediew odrabia straty z Basilaszwilim w Almaty: pierwsza obrona tytulu w karierze",
            "subtitle": "Najwyzej rozstawiony przegrywa tie-break, by zdominowac kolejne dwa sety. Medwiediew siega po 25. trofeum ATP.",
            "excerpt": "Daniił Medwiediew pokonal twardo grajacego kwalifikanta Nikołoza Basilaszwilego 6-7(6), 6-1, 6-3 i obronil tytul Almaty Open w niedziele.",
            "body": [
                "Najwyzej rozstawiony Daniił Medwiediew osiagnal wyjatkowy kamien milowy w niedziele 25 pazdziernika, odrabiajac straty i pokonujac gruzinskiego kwalifikanta Nikołoza Basilaszwilego 6-7(6), 6-1, 6-3 w finale turnieju Almaty Open. Wygrana ta zapewnila Medwiediewowi 25. tytul singlowy w cyklu ATP oraz czwarte trofeum w sezonie 2026. Co wazniejsze, to pierwszy raz w profesjonalnej karierze, kiedy byly lider rankingu swiatowego z powodzeniem obronil wywalczony wczesniej puchar, przelamujac nietypowa serie z poprzednich 24 triumfow. Basilaszwili, ktory przed turniejem byl poza czolowa 150 rankingu i sensacyjnie wyeliminowal Stefanosa Tsitsipasa w polfinale, wszedl w mecz bez kompleksow. 34-letni Gruzin zachowal zimna krew w tie-breaku, wygrywajac go 8-6 po 54 minutach ciezkiej walki z glebi kortu.",
                "Medwiediew blyskawicznie odpowiedzial na poczatku drugiej partii. Podchodzac blizej linii koncowej i rozrzucajac rywala ostrym bekhendem, faworyt przelamal serwis przeciwnika w drugim gemie i oddal tylko jednego gema w drodze do remisu w meczu. W decydujacym secie Medwiediew zanotowal decydujace przelamanie w trzecim gemie i nie dopuscil do zadnego break pointa przy wlasnym serwisie, konczac final po godzinie i 53 minutach. Triumf w Kazachstanie przybliza Medwiediewa do wystepu w torynskich ATP Finals. Z kolei dla Basilaszwilego ten spektakularny turniej oznacza powrot w okolice czolowej setki przed zmaganiami w Wiedniu i Bazylei."
            ]
        },
        "zh": {
            "title": "梅德韦杰夫逆转巴斯拉什维利问鼎阿拉木图：职业生涯首次成功卫冕",
            "subtitle": "头号种子抢七惜败后连扳两盘展现绝对统治力，梅德韦杰夫斩获职业生涯第25座ATP冠军奖杯。",
            "excerpt": "丹尼尔·梅德韦杰夫顶住资格赛黑马巴斯拉什维利的顽强阻击，以6-7(6)、6-1、6-3逆转夺冠，周日成功卫冕阿拉木图公开赛。",
            "body": [
                "头号种子丹尼尔·梅德韦杰夫在10月25日周日迎来了职业生涯的重要里程碑。他在阿拉木图公开赛男单决赛中上演精彩逆转，以6-7(6)、6-1、6-3击败格鲁吉亚资格赛黑马巴斯拉什维利。这场胜利让梅德韦杰夫捧起了个人第25座巡回赛单打冠军奖杯，这也是他2026赛季夺得的第四冠。更为关键的是，这是前世界第一职业生涯中首次成功实现卫冕，打破了此前24个冠军从未实现连霸的特殊纪录。现年34岁的巴斯拉什维利在半决赛爆冷淘汰齐齐帕斯，决赛开局同样火力全开。他在首盘抢七中顶住压力，在激战54分钟后以8-6先拔头筹。",
                "进入第二盘后，梅德韦杰夫迅速做出战术调整。他提升了接发球站位，用角度刁钻的反手压制对手，并在第二局完成破发，随后仅丢一局便将盘分扳平。在决胜盘中，梅德韦杰夫在第三局抓住机会完成关键破发，并在自己的发球局中未送出任何破发点，历时1小时53分钟锁定胜局。此冠进一步巩固了梅德韦杰夫入围都灵年终总决赛的席位。而对于巴斯拉什维利而言，凭借从资格赛一路杀入决赛的出色表现，其世界排名将重返前100位。"
            ]
        },
        "ja": {
            "title": "メドベージェフがアルマトイで逆転劇：バシラシビリを下しキャリア初の大会連覇",
            "subtitle": "第1シードが第1セットのタイブレークを落とすも残り2セットを圧倒。通算25個目のATPトロフィーを掲げる。",
            "excerpt": "ダニール・メドベージェフが予選勝者ニコロズ・バシラシビリに6-7(6)、6-1、6-3で競り勝ち、日曜のアルマトイ・オープンで自身初となる連覇を達成しました。",
            "body": [
                "第1シードのダニール・メドベージェフが10月25日日曜、アルマトイ・オープン決勝でジョージアの予選勝者ニコロズ・バシラシビリに6-7(6)、6-1、6-3で逆転勝利を収め、キャリアの大きな節目を打ち立てました。この栄冠によりメドベージェフはATPツアー通算25勝目をマークし、2026シーズン4つ目のトロフィーを獲得。元世界ランク1位にとって過去24回の優勝で一度も成し遂げていなかった自身初のタイトル防衛に成功しました。準決勝でチチパスを撃破して勢いに乗る34歳のバシラシビリは立ち上がりから強打を連発。白熱したタイブレークを8-6で制し、54分の熱闘の末に第1セットを先取しました。",
                "しかしメドベージェフは第2セットに入ると立ち位置を前へ移し、バックハンドで鋭いクロスを連発。第2ゲームをブレークするとわずか1ゲームしか与えずにセットオールに持ち込みました。迎えた最終セットも第3ゲームで決定的なブレークを奪うと、自身のサービスゲームでは一度もブレークポイントを与えず、1時間53分で勝利を掴み取りました。この勝利でメドベージェフはトリノでのATPファイナルズ出場をより盤石にしました。一方のバシラシビリも予選からの快進撃で世界トップ100復帰を手中に収めています。"
            ]
        },
        "ko": {
            "title": "메드베데프 알마티 오픈 역전 우승: 커리어 첫 대회 2연패 달성",
            "subtitle": "톱시드 메드베데프 첫 세트 타이브레이크 패배 딛고 내리 두 세트 압도. 통산 25번째 ATP 트로피 포효.",
            "excerpt": "다닐 메드베데프가 예선 돌풍의 니콜로즈 바실라슈빌리를 6-7(6), 6-1, 6-3으로 제압하고 일요일 알마티 오픈 정상 수성에 성공했습니다.",
            "body": [
                "톱시드 다닐 메드베데프가 10월 25일 일요일 알마티 오픈 결승에서 조지아의 예선 통과자 니콜로즈 바실라슈빌리를 6-7(6), 6-1, 6-3으로 꺾고 개인 통산 의미 있는 이정표를 세웠습니다. 이번 우승은 메드베데프의 통산 25번째 ATP 투어 단식 타이틀이자 2026시즌 4번째 트로피입니다. 무엇보다 전 세계 랭킹 1위였던 그가 프로 커리어 사상 처음으로 대회 타이틀 방어에 성공했다는 점에서 남다른 의미를 지닙니다. 준결승에서 치치파스를 꺾고 결승에 오른 34세 베테랑 바실라슈빌리는 경기 초반부터 강력한 베이스라인 샷을 앞세워 1세트 타이브레이크를 8-6으로 따내며 기선을 제압했습니다.",
                "하지만 메드베데프의 진가는 2세트부터 드러났습니다. 베이스라인 안쪽으로 바짝 다가선 메드베데프는 예리한 백핸드 각도를 구사하며 2번째 게임을 브레이크했고 단 1게임만 내주며 세트 스코어 균형을 맞췄습니다. 마지막 3세트에서도 3번째 게임을 브레이크한 뒤 단 한 차례의 브레이크 포인트도 허용하지 않고 1시간 53분 만에 우승을 확정 지었습니다. 이로써 메드베데프는 토리노에서 열리는 ATP 파이널스 진출을 사실상 확정 지었으며, 바실라슈빌리 역시 눈부신 결승 진출로 톱 100 복귀를 눈앞에 두게 되었습니다."
            ]
        },
        "ar": {
            "title": "ميدفيديف يقلب الطاولة على باسيلاشفيلي في الماتي: اول دفاع ناجح عن لقب في مسيرته",
            "subtitle": "المصنف الاول يخسر الشوط الفاصل في المجموعة الاولى قبل ان يكتسح المجموعتين التاليتين ويتوج بلقبه الـ25 في بطولات المحترفين.",
            "excerpt": "تغلب دانييل ميدفيديف على مقاومة نيكولوز باسيلاشفيلي بنتيجة 6-7(6) و6-1 و6-3 ليحتفظ بتاج بطولة الماتي المفتوحة يوم الاحد.",
            "body": [
                "حقق المصنف الاول دانييل ميدفيديف انجازا شخصيا استثنائيا يوم الاحد 25 اكتوبر بعد ان عاد بقوة ليهزم المتأهل من التصفيات الجورجي نيكولوز باسيلاشفيلي بنتيجة 6-7(6) و6-1 و6-3 في نهائي بطولة الماتي المفتوحة للتنس. ومنح هذا الانتصار ميدفيديف لقبه الفردي رقم 25 في مسيرته ببطولات رابطة المحترفين ورابع القابه في موسم 2026. والاهم من ذلك، يمثل هذا التتويج المرة الاولى في مسيرته الاحترافية التي ينجح فيها المصنف الاول عالميا سابقا في الدفاع عن لقبه، كاسرا بذلك مفارقة غريبة استمرت طوال القابه الـ24 السابقة. باسيلاشفيلي، الذي اخرج تسيتسيباس من نصف النهائي، دخل اللقاء بضربات قوية وحسم الشوط الفاصل للمجموعة الاولى 8-6 بعد 54 دقيقة من الصراع البدني الشرس.",
                "وجاء رد ميدفيديف سريعا مع انطلاقة المجموعة الثانية، حيث تقدم للامام ووجه ضربات خلفية محكمة ليكسر ارسال باسيلاشفيلي في الشوط الثاني ويحسم المجموعة خاسرا شوطا واحدا فقط. وفي المجموعة الحاسمة، كسر ميدفيديف الارسال في الشوط الثالث ولم يواجه اي نقطة لكسر ارساله طوال المجموعة لينهي المباراة في ساعة و53 دقيقة. هذا اللقب يعزز بطاقة تأهله للبطولة الختامية في تورينو، بينما يعيد هذا الانجاز باسيلاشفيلي الى قائمة افضل 100 لاعب في العالم قبل بطولتي فيينا وبازل."
            ]
        }
    },
    "premier-league-mw8-spurs-stun-chelsea-villa-topple-city-2026": {
        "fr": {
            "title": "Secousse en Premier League : les Spurs domptent Chelsea a Stamford Bridge, Villa renverse City",
            "subtitle": "Tottenham s'impose a Stamford Bridge pour la premiere fois depuis 2018. Aston Villa brise la serie parfaite de Manchester City.",
            "excerpt": "Tottenham a battu Chelsea 2-0 a dix contre onze pendant qu'Aston Villa surprenait City 2-1 lors d'un samedi fou qui voit City et Arsenal a egalite avec 21 points.",
            "body": [
                "La 8e journee de Premier League a reserve d'enormes surprises ce samedi 24 octobre, marquee par le succes historique de Tottenham Hotspur sur la pelouse de Chelsea (2-0), leur premiere victoire en championnat a Stamford Bridge depuis avril 2018. Le derby londonien est reste indecis jusqu'a la 77e minute, moment ou un corner vicieux a pousse le portier de Chelsea Mike Penders a devier le ballon dans ses propres filets sous la pression adverse.",
                "Le sort des Blues a vire au cauchemar trois minutes plus tard avec l'expulsion de Cole Palmer pour un deuxieme avertissement lie a une contestation. En inferiorite numerique, Chelsea s'est decouvert et a ete puni a la 87e minute par une splendide chevauchee solitaire de Mathys Tel qui a scelle le triomphe des Spurs. Plus tot dans l'apres-midi, Aston Villa a fait sensation a Villa Park en infligeant a Manchester City sa premiere defaite de la saison (2-1) grâce a un double de Nicolas Jackson. Arsenal en a profite pour battre Everton 2-0 (Konsa 7', Gabriel 68') et rejoindre City en tete du classement avec 21 points."
            ]
        },
        "es": {
            "title": "Terremoto en la Premier League: Spurs sorprenden a Chelsea y Villa tumba al Manchester City",
            "subtitle": "Tottenham conquista Stamford Bridge por primera vez desde 2018. Aston Villa frena la marcha perfecta de los de Guardiola.",
            "excerpt": "Tottenham vencio 2-0 a un Chelsea con diez jugadores y Aston Villa batio 2-1 al City en un sabado magico que deja a City y Arsenal empatados con 21 puntos.",
            "body": [
                "La jornada 8 de la Premier League dejo resultados electrizantes este sabado 24 de octubre, con el Tottenham Hotspur logrando su primer triunfo de liga en Stamford Bridge desde abril de 2018 tras imponerse 2-0 al Chelsea. El derbi de Londres se mantuvo empatado hasta el minuto 77, cuando un centro envenenado de tiro de esquina provoco que el arquero local Mike Penders enviara el balon a su propia meta ante el acoso visitante.",
                "El panorama empeoro para los Blues tres minutos despues al ver Cole Palmer la segunda tarjeta amarilla por protestar. Con diez hombres, Chelsea se volco al ataque y Tottenham lo liquido a la contra en el minuto 87 con una notable carrera individual de Mathys Tel. La sorpresa habia comenzado mas temprano en Villa Park, donde Aston Villa derroto 2-1 al Manchester City con doblete de Nicolas Jackson (6' y 60'), cortando la racha invicta de siete triunfos celestes. Arsenal capitalizo el traspie al superar 2-0 a Everton (Konsa 7', Gabriel 68') para compartir la cima con el City con 21 puntos."
            ]
        },
        "de": {
            "title": "Beben in der Premier League: Spurs schocken Chelsea, Villa stoppt Manchester City",
            "subtitle": "Tottenham siegt erstmals seit 2018 an der Stamford Bridge. Aston Villa beendet die Siegesserie von Manchester City.",
            "excerpt": "Tottenham besiegte dezimierte Blues mit 2-0 waehrend Aston Villa Man City mit 2-1 bezwang: City und Arsenal stehen punktgleich mit 21 Punkten ganz oben.",
            "body": [
                "Der 8. Spieltag der Premier League brachte am Samstag, 24. Oktober, dramatische Wendungen im Titelrennen. Allen voran feierte Tottenham Hotspur durch ein 2-0 beim FC Chelsea seinen ersten Ligasieg an der Stamford Bridge seit April 2018. Das hitzige Londoner Derby blieb bis zur 77. Minute torlos, ehe Chelsea-Torwart Mike Penders nach einer scharfen Ecke den Ball unter Bedraengnis ins eigene Tor lenkte.",
                "Drei Minuten spaeter flog Cole Palmer mit Gelb-Rot wegen Reklamierens vom Platz. In Unterzahl warfen die Blues alles nach vorne und wurden in der 87. Minute eiskalt ausgekontert, als Mathys Tel nach einem Solo zum 2-0 vollstreckte. Bereits am Nachmittag hatte Aston Villa fuer eine Sensation gesorgt und Tabellenfuehrer Manchester City durch einen Doppelpack von Nicolas Jackson mit 2-1 die erste Saisonniederlage zugefuegt. Arsenal nutzte die Gunst der Stunde, schlug Everton mit 2-0 (Konsa 7., Gabriel 68.) und zog mit 21 Punkten mit City an der Tabellenspitze gleich."
            ]
        },
        "it": {
            "title": "Scossone in Premier League: gli Spurs gelano il Chelsea, il Villa abbatte il Manchester City",
            "subtitle": "Il Tottenham espugna Stamford Bridge per la prima volta dal 2018. L'Aston Villa interrompe la marcia perfetta del City.",
            "excerpt": "Il Tottenham vince 2-0 contro un Chelsea in dieci mentre l'Aston Villa supera 2-1 il City: City e Arsenal si ritrovano appaiati in vetta con 21 punti.",
            "body": [
                "L'8a giornata di Premier League ha regalato verdetti clamorosi sabato 24 ottobre, guidati dal trionfo del Tottenham Hotspur per 2-0 sul campo del Chelsea: il primo successo in campionato a Stamford Bridge dall'aprile 2018. Il derby di Londra si e sbloccato al 77° minuto quando, su un velenoso calcio d'angolo, il portiere del Chelsea Mike Penders ha deviato sfortunatamente il pallone nella propria porta.",
                "I padroni di casa sono poi rimasti in dieci tre minuti piu tardi per l'espulsione di Cole Palmer per proteste. Con il Chelsea sbilanciato, Mathys Tel ha chiuso la contesa all'87° con una travolgente ripartenza personale. Nel pomeriggio a Villa Park l'Aston Villa aveva firmato la grande impresa piegando 2-1 il Manchester City con una doppietta di Nicolas Jackson (6' e 60'), fermando a sette la striscia di vittorie di Guardiola. L'Arsenal ha sfruttato l'occasione battendo 2-0 l'Everton (Konsa 7', Gabriel 68') per agganciare il City in vetta a 21 punti."
            ]
        },
        "pl": {
            "title": "Trzesienie ziemi w Premier League: Spurs uciszaja Stamford Bridge, Villa bije Manchester City",
            "subtitle": "Tottenham wygrywa na terenie Chelsea pierwszy raz od 2018 roku. Aston Villa przerywa perfekcyjna serie City.",
            "excerpt": "Tottenham pokonal oslabiona Chelsea 2-0, a Aston Villa ograla Manchester City 2-1 w sobote pelna emocji, po ktorej City i Arsenal maja po 21 punktow.",
            "body": [
                "8. kolejka Premier League przyniosla w sobote 24 pazdziernika sensacyjne rozstrzygniecia. Najwiekszym echem odbila sie wygrana Tottenhamu Hotspur 2-0 nad Chelsea na Stamford Bridge, oznaczajaca pierwszy ligowy triumf Spurs na tym stadionie od kwietnia 2018 roku. Losy derbow rozstrzygnely sie w koncowce: w 77. minucie pod naciskiem rywali bramkarz Chelsea Mike Penders skierowal pilke do wlasnej bramki po dosrodkowaniu z rzutu roznego.",
                "Trzy minuty pozniej sytuacje gospodarzy pogorszyla czerwona kartka dla Cole'a Palmera za dyskusje z arbitrem. Grajaca w dziesiatke Chelsea rzucila sie do odrabiania strat, lecz w 87. minucie Mathys Tel po solowym rajdzie z kontry przypieczetowal zwyciestwo Spurs. Wczesniej na Villa Park Aston Villa sprawila ogromna niespodzianke, pokonujac lidera Manchester City 2-1 dzieki dwom bramkom Nicolasa Jacksona. Szanse wykorzystal Arsenal, ktory wygral 2-0 z Evertonem (Konsa 7', Gabriel 68') i zrownal sie z City na szczycie tabeli z 21 punktami."
            ]
        },
        "zh": {
            "title": "英超超级冷门夜：热刺客斩切尔西破魔咒，维拉力克曼城送首败",
            "subtitle": "托特纳姆热刺自2018年以来首次攻陷斯坦福桥。阿斯顿维拉终结曼城开季全胜金身。",
            "excerpt": "热刺2-0力克十人切尔西，阿斯顿维拉2-1爆冷击败曼城，阿森纳完胜埃弗顿追平积分，英超争冠双雄同积21分并驾齐驱。",
            "body": [
                "英超第8轮在10月24日周六上演惊天波澜。托特纳姆热刺在客场以2-0击败切尔西，自2018年4月以来首次在斯坦福桥球场带走联赛胜利。这场激烈的伦敦德比战至第77分钟风云突变，热刺角球开入禁区制造混乱，切尔西门将彭德斯在重压之下不慎将球碰入自家大门打破僵局。",
                "仅仅3分钟后，切尔西核心帕尔默因对裁判判罚过度抗议领到第二张黄牌被罚下场。少一人作战的蓝军全线压上反扑，热刺在第87分钟通过犀利反击由特尔长途奔袭推射破门锁定胜局。在此前进行的比赛中，阿斯顿维拉在主场2-1力克领头羊曼城，杰克逊梅开二度终结了曼城的7连胜。阿森纳则抓住机会主场2-0轻取埃弗顿（孔萨7分钟、加布里埃尔68分钟），与曼城同积21分并列积分榜首位。"
            ]
        },
        "ja": {
            "title": "プレミアリーグ激震の土曜日：スパーズがブリッジを攻略、アストン・ヴィラがマンCを撃破",
            "subtitle": "トッテナムが2018年以来となるスタンフォード・ブリッジ白星。ヴィラがマンチェスター・シティの開幕連勝を止める。",
            "excerpt": "トッテナムが10人のチェルシーを2-0で下し、アストン・ヴィラがシティを2-1で撃破。アーセナルが追いつき勝点21で首位タイに並びました。",
            "body": [
                "10月24日土曜日のプレミアリーグ第8節は衝撃の結末を迎えました。トッテナム・ホットスパーがスタンフォード・ブリッジでチェルシーに2-0で完勝し、2018年4月以来となる敵地でのリーグ戦白星を飾りました。膠着状態が続いたダービーは77分、熱のこもったコーナーキックからチェルシーGKペンダースがプレッシャーを受けてオウンゴールを献上して動きます。",
                "その3分後には抗議によりコール・パーマーが2枚目の警告を受けて退場。10人となったチェルシーが前がかりになった隙を突き、87分にマティス・テルが圧巻の単独カウンターから追加点を奪いました。また午後にはアストン・ヴィラがニコラス・ジャクソンの2発（6分、60分）で首位マンチェスター・シティを2-1で下し開幕連勝をストップ。アーセナルがエバートンに2-0（コンサ7分、ガブリエウ68分）で快勝したことで、シティとアーセナルが勝点21で首位に並びました。"
            ]
        },
        "ko": {
            "title": "프리미어리그 충격의 토요일: 토트넘 첼시 원정 격파, 빌라 맨시티 연승 저지",
            "subtitle": "토트넘 2018년 이후 첫 스탬퍼드 브리지 승리. 아스톤 빌라 맨체스터 시티 개막 전승 행진에 제동.",
            "excerpt": "토트넘이 10명이 싸운 첼시를 2-0으로 제압하고 빌라가 맨시티를 2-1로 잡으며 아스널과 맨시티가 나란히 승점 21점으로 공동 선두에 올랐습니다.",
            "body": [
                "프리미어리그 8라운드가 10월 24일 토요일 대이변의 드라마를 연출했습니다. 토트넘 홋스퍼가 스탬퍼드 브리지 원정에서 첼시를 2-0으로 제압하며 2018년 4월 이후 무려 8년 만에 첼시 안방에서 리그 승리를 챙겼습니다. 팽팽하던 런던 더비는 후반 77분 코너킥 상황에서 첼시 골키퍼 마이크 펜더스가 볼을 자기 골문으로 쳐내는 자책골을 범하며 균형이 깨졌습니다.",
                "설상가상으로 3분 뒤 첼시의 콜 파머가 판정 항의로 두 번째 경고를 받아 퇴장당했습니다. 수적 열세에 놓인 첼시가 공세를 펴자 토트넘은 후반 87분 마티스 텔의 환상적인 단독 역습 쐐기골로 승부를 갈랐습니다. 앞서 열린 경기에서는 아스톤 빌라가 니콜라스 잭슨의 멀티골(6분, 60분)에 힘입어 맨체스터 시티를 2-1로 꺾고 시티의 7연승을 저지했습니다. 아스널은 에버턴을 2-0(콘사 7분, 마갈량이스 68분)으로 완파하며 맨시티와 나란히 승점 21점으로 공동 1위에 올랐습니다."
            ]
        },
        "ar": {
            "title": "زلزال في البريميرليغ: توتنهام يصدم تشيلسي في الستامفورد وفيلّا يسقط مانشستر سيتي",
            "subtitle": "توتنهام ينتصر في معقل تشيلسي لاول مرة منذ 2018. واستون فيلا يوقف قطار انتصارات مانشستر سيتي المتتالية.",
            "excerpt": "هزم توتنهام مضيفه تشيلسي 2-0 بينما صعق استون فيلا مانشستر سيتي 2-1 في سبت مثير شهد تساوي السيتي وارسنال في الصدارة بـ21 نقطة.",
            "body": [
                "شهدت الجولة الثامنة من الدوري الانجليزي الممتاز مفاجآت مدوية يوم السبت 24 اكتوبر، تصدرها فوز تاريخي لتوتنهام هوتسبير على تشيلسي 2-0 في ستامفورد بريدج، وهو اول انتصار للسبيرز في معقل البلوز بالدوري منذ ابريل 2018. وظل الديربي اللندني معلقا حتى الدقيقة 77 حين حول حارس تشيلسي الشاب مايك بيندرز كرة من ركنية بالخطأ الى مرماه تحت الضغط.",
                "وتعقدت الامور على تشيلسي بعد ثلاث دقائق بطرد نجمه كول بالمر بالانذار الثاني للاعتراض. وبينما اندفع البلوز للتعويض، انطلق ماتيس تيل في هجمة مرتدة فردية خاطفة بالدقيقة 87 ليطلق رصاصة الرحمة. وكانت المفاجآت قد انطلقت مبكرا في فيلا بارك حين اسقط استون فيلا المتصدر مانشستر سيتي بنتيجة 2-1 بهدفي نيكولاس جاكسون (6 و60) لينهي سلسلة انتصارات السيتي السبعة. واستغل ارسنال التعثر ليفوز على ايفرتون 2-0 (كونسا 7 وغابرييل 68) ليتشارك الصدارة مع مانشستر سيتي برصيد 21 نقطة."
            ]
        }
    },
    "wnba-finals-2026-game4-valkyries-stun-dream-force-game5": {
        "fr": {
            "title": "Les Valkyries ecartent l'elimination a Atlanta : les finales WNBA filent vers un match 5",
            "subtitle": "Golden State etouffe le Dream 67-62 pour egaliser a 2-2. L'ultime combat pour le titre aura lieu a San Francisco.",
            "excerpt": "Les Golden State Valkyries ont arrache une victoire vitale 67-62 dans le match 4, ramenant les finales au Chase Center pour un match 5 decisif.",
            "body": [
                "Les Golden State Valkyries ont refuse d'abdiquer ce samedi soir, signant une lecon defensive a l'exterieur pour surprendre l'Atlanta Dream 67-62 lors du match 4 des finales WNBA. Dos au mur devant un public hostile a la State Farm Arena, la franchise d'expansion a bati une avance de 16 points a la mi-temps avant de resister au retour fulgurant d'Atlanta dans le dernier quart pour recoller a 2-2 dans la serie.",
                "Gabby Williams a donne le ton pour Golden State en terminant meilleure marqueuse de son equipe avec 17 points, 5 rebonds et 3 interceptions. Hayes et Burton ont ajoute 13 points chacune, assurant la continuite offensive. Mais c'est dans la raquette que la difference s'est faite : Kiah Stokes a cadenasse la vedette d'Atlanta Angel Reese, limitee a 8 points a 2 sur 12 au tir, mettant fin a sa serie record de trois double-doubles en finales. La serie retourne desormais a San Francisco pour un match 5 couperet au Chase Center."
            ]
        },
        "es": {
            "title": "Valkyries evitan la eliminacion en Atlanta: las Finales WNBA van a un definitivo Juego 5",
            "subtitle": "Golden State frena a Dream 67-62 para empatar la serie 2-2. La gloria se decidira en San Francisco.",
            "excerpt": "Las Golden State Valkyries sobrevivieron a domicilio con triunfo 67-62 en el Juego 4 y fuerzan el quinto partido en el Chase Center.",
            "body": [
                "Las Golden State Valkyries se negaron a despedirse este sabado por la noche y dieron una autentica catedra defensiva para sorprender al Atlanta Dream 67-62 en el Juego 4 de las Finales de la WNBA. Con la espalda contra la pared ante una multitud abarrotada en el State Farm Arena, la franquicia de expansion saco 16 puntos de ventaja al descanso y resistio la embestida local en el ultimo cuarto para empatar 2-2 la serie final.",
                "Gabby Williams lidero a Golden State con 17 puntos, 5 rebotes y 3 robos. Hayes y Burton sumaron 13 puntos cada una aportando serenidad ante la presion a toda cancha de Atlanta. La defensa interior liderada por Kiah Stokes seco por completo a Angel Reese, reducida a solo 8 puntos con 2 de 12 en tiros de campo, rompiendo su racha de tres dobles-dobles consecutivos en las finales. Ahora la serie viaja a San Francisco para un apasionante Juego 5 en el Chase Center."
            ]
        },
        "de": {
            "title": "Valkyries wenden Aus in Atlanta ab: WNBA Finals gehen ins entscheidende Spiel 5",
            "subtitle": "Golden State besiegt die Dream mit 67-62 zum 2-2-Serienausgleich. Showdown um den Titel steigt in San Francisco.",
            "excerpt": "Die Golden State Valkyries holten einen hart umkaempften 67-62-Auswaertssieg in Spiel 4 und bringen die WNBA Finals zurueck ins Chase Center.",
            "body": [
                "Die Golden State Valkyries stemmten sich am Samstagabend mit aller Macht gegen das Saisonende und boten eine defensive Meisterleistung, um die Atlanta Dream in Spiel 4 der WNBA Finals mit 67-62 zu schlagen. Vor ausverkaufter Kulisse in der State Farm Arena erarbeitete sich das Expansionsteam eine 16-Punkte-Pausenfuehrung und brachte den Vorsprung ueber die Zeit, um die Best-of-Five-Serie auf 2-2 zu stellen.",
                "Gabby Williams fuehrte die Gaeste mit 17 Punkten, 5 Rebounds und 3 Steals an, waehrend Hayes und Burton jeweils 13 Zaehler beisteuerten. Den Schluessel zum Erfolg bildete die Zone-Verteidigung um Center Kiah Stokes, die Atlanta-Star Angel Reese bei lediglich 8 Punkten und 2 von 12 Treffern aus dem Feld hielt. Damit riss Reeses Serie von drei Final-Double-Doubles in Folge. Die Entscheidung faellt nun im Chase Center von San Francisco in einem alles entscheidenden Spiel 5."
            ]
        },
        "it": {
            "title": "Le Valkyries evitano l'eliminazione ad Atlanta: le WNBA Finals vanno a Gara 5",
            "subtitle": "Golden State doma le Dream 67-62 pareggiando la serie sul 2-2. La sfida decisiva si giochera a San Francisco.",
            "excerpt": "Le Golden State Valkyries vincono 67-62 in trasferta in Gara 4 e riportano le WNBA Finals al Chase Center per una decisiva Gara 5.",
            "body": [
                "Le Golden State Valkyries non hanno alcuna intenzione di arrendersi: sabato sera hanno sfoderato una prestazione difensiva impeccabile superando le Atlanta Dream 67-62 in Gara 4 delle WNBA Finals. Con le spalle al muro davanti a una State Farm Arena gremita, la franchigia d'espansione ha accumulato un vantaggio di 16 punti all'intervallo e ha contenuto il furioso rientro avversario nel finale pareggiando la serie sul 2-2.",
                "Gabby Williams e stata la protagonista assoluta con 17 punti, 5 rimbalzi e 3 recuperi, supportata dai 13 punti ciascuna di Hayes e Burton. Sotto canestro Kiah Stokes ha guidato una guardia asfissiante che ha limitato la stella di Atlanta Angel Reese a soli 8 punti con 2 su 12 dal campo, interrompendo la sua striscia di tre doppie doppie consecutive nelle Finals. Ora il titolo verra assegnato al Chase Center di San Francisco in una storica Gara 5."
            ]
        },
        "pl": {
            "title": "Valkyries uciekaja spod topora w Atlancie: Finaly WNBA rozstrzygna sie w meczu numer 5",
            "subtitle": "Golden State pokonuje Dream 67-62 i doprowadza do remisu 2-2 w serii. O mistrzostwie zadecyduje starcie w San Francisco.",
            "excerpt": "Golden State Valkyries wygraly na wyjezdzie 67-62 w meczu numer 4, przenoszac decydujaca rywalizacje o tytul WNBA do Chase Center.",
            "body": [
                "Koszykarki Golden State Valkyries nie pozwolily zakonczyc sezonu w sobote wieczorem, prezentujac wybitna dostawe w defensywie i pokonujac Atlanta Dream 67-62 w 4. meczu Finalow WNBA. Stojac pod sciana przed zywiolowa publicznoscia w State Farm Arena, debiutujacy w lidze zespol wypracowal 16-punktowa przewage do przerwy i obronil prowadzenie w nerwowej koncowce, wyrownujac stan rywalizacji na 2-2.",
                "Gabby Williams poprowadzila Valkyries, zdobywajac 17 punktow, 5 zbiorek i 3 przechwyty, a Hayes i Burton dolozyly po 13 punktow. Kluczowa okazala sie jednak defensywa podkoszowa pod wodza Kiah Stokes, ktora zatrzymala gwiazde Atlanty Angel Reese na zaledwie 8 punktach przy skutecznosci 2/12 z gry, przerywajac jej serie meczow z double-double. O mistrzostwie WNBA zdecyduje piate starcie w San Francisco."
            ]
        },
        "zh": {
            "title": "女武神客场死里逃生绝地反击：WNBA总决赛进入抢五决战",
            "subtitle": "金州女武神67-62力克亚特兰大梦想将总比分扳成2-2平，总冠军奖杯将在旧金山大通中心决出。",
            "excerpt": "面临赛点淘汰的金州女武神客场以67-62击溃梦想，将WNBA总决赛拖入最终的第五场生死战。",
            "body": [
                "背水一战的金州女武神在周六晚间展现了顽强的冠军底蕴，凭借铜墙铁壁般的防守在客场以67-62战胜亚特兰大梦想，将WNBA总决赛大比分扳为2-2平。在州立农业球馆全场爆满的助威声浪中，这支新军半场建立起16分的巨大优势，并在第四节顶住了主队的疯狂反扑。",
                "加比·威廉姆斯全场贡献17分、5个篮板和3次抢断成为制胜功臣，海耶斯和伯顿各自拿下13分稳住阵脚。女武神内线防守在斯托克斯的领衔下发挥极致，将梦想当家球星安吉尔·里斯限制到仅得8分（12投2中），终结了她连续三场总决赛两双的纪录。悬念留到了旧金山，两队将在大通中心迎来一战定乾坤的抢五决战。"
            ]
        },
        "ja": {
            "title": "バルキリーズがアトランタで踏みとどまる：WNBAファイナルは運命の第5戦へ",
            "subtitle": "ゴールデンステイトがドリームを67-62で封じ2勝2敗のタイに。決着はサンフランシスコへ持ち越し。",
            "excerpt": "敗退の危機に瀕したゴールデンステイト・バルキリーズが敵地で67-62の勝利をもぎ取り、WNBAファイナルはチェイス・センターでの第5戦へ突入。",
            "body": [
                "ゴールデンステイト・バルキリーズが土曜夜、アトランタのステートファーム・アリーナで意地を見せました。王手をかけられていたエクスパンション・チームは圧巻のディフェンスを披露し、アトランタ・ドリームを67-62で撃破。前半で16点差のリードを奪い、最終クォーターの猛反撃をしのぎ切って対戦成績を2勝2敗の五分に戻しました。",
                "ギャビー・ウィリアムズがチーム最多の17得点、5リバウンド、3スティールと獅子奮迅の活躍を見せ、ヘイズとバートンも13得点ずつで貢献。カイア・ストークスを中心とするインサイド守備はドリームのエースであるエンジェル・リースをわずか8得点（FG 2/12）に抑え込み、ファイナル連続ダブルダブルをストップさせました。歴史的栄冠の行方は本拠地チェイス・センターでの最終第5戦に委ねられます。"
            ]
        },
        "ko": {
            "title": "발키리스 벼랑 끝 탈출: WNBA 파이널 최종 5차전으로 간다",
            "subtitle": "골든스테이트 드림에 67-62 짜릿한 승리 거두고 시리즈 2-2 균형. 대망의 트로피는 샌프란시스코에서 결정.",
            "excerpt": "탈락 위기에 몰렸던 골든스테이트 발키리스가 4차전 원정에서 67-62로 승리하며 WNBA 파이널을 체이스 센터 5차전으로 이끌었습니다.",
            "body": [
                "골든스테이트 발키리스가 10월 24일 토요일 밤 원정에서 믿기 힘든 수비전을 펼치며 애틀랜타 드림을 67-62로 누르고 WNBA 파이널 4차전을 승리로 장식했습니다. 스테이트 팜 아레나 원정 팬들의 일방적 응원 속에 치러진 경기에서 신생팀 발키리스는 전반에만 16점 차 리드를 잡은 뒤 4쿼터 애틀랜타의 맹추격을 침착하게 따돌리며 시리즈 전적 2-2 동률을 만들었습니다.",
                "개비 윌리엄스가 17득점 5리바운드 3스틸로 팀 공격을 주도했고 헤이즈와 버튼이 나란히 13점을 보탰습니다. 특히 카이아 스톡스가 이끄는 골밑 수비는 애틀랜타 에이스 에인절 리스를 8득점(야투 2/12)으로 꽁꽁 묶으며 파이널 연속 더블더블 행진을 멈춰 세웠습니다. 이제 두 팀은 샌프란시스코 체이스 센터로 이동해 운명의 5차전 단판 승부를 펼칩니다."
            ]
        },
        "ar": {
            "title": "فالكيريز يتفادى الاقصاء في اتلانتا: نهائيات WNBA تتجه لمباراة خامسة حاسمة",
            "subtitle": "غولدن ستيت يخنق دريم بنتيجة 67-62 ويعادل السلسلة 2-2. الحسم ينتقل الى سان فرانسيسكو.",
            "excerpt": "نجا غولدن ستيت فالكيريز في معقل مضيفه بالفوز 67-62 في المباراة الرابعة ليعيد نهائيات WNBA الى تشيس سنتر في مواجهة خامسة فاصلة.",
            "body": [
                "رفض فريق غولدن ستيت فالكيريز الاستسلام مساء السبت، مقدما درسا دفاعيا مبهرا خارج ملعبه ليفاجئ اتلانتا دريم بنتيجة 67-62 في المباراة الرابعة من نهائيات WNBA. وتحت ضغط خطر الاقصاء امام جماهير صاخبة في ستيت فارم ارينا، بنى الفريق الواعد تقدما مريحا بفارق 16 نقطة في الشوط الاول وصمد امام عودة اصحاب الارض ليعادل السلسلة 2-2.",
                "وتألقت غابي ويليامز بتسجيل 17 نقطة مع 5 متابعات و3 خطفات، واضافت كل من هايز وبيرتون 13 نقطة. وكان مفتاح الانتصار هو الدفاع الحديدي بقيادة كيا ستوكس التي شلت خطورة نجمة اتلانتا انجل ريس وحدت من خطورتها لتسجل 8 نقاط فقط بنسبة 2 من 12، لتتوقف سلسلتها التاريخية بثلاث مباريات متتالية برقمين مزدوجين. وتتجه السلسلة الان الى سان فرانسيسكو لخوض المباراة الخامسة والفاصلة للتتويج باللقب."
            ]
        }
    },
    "f1-austin-sunday-race-day-antonelli-pole-verstappen-cota-2026": {
        "fr": {
            "title": "Jour de course a Austin : Antonelli s'elance en pole devant Verstappen a COTA",
            "subtitle": "Le rookie de Mercedes bat Verstappen de 0,179 seconde en qualifications. Antonelli en quete du sacre mondial.",
            "excerpt": "Kimi Antonelli prend le depart en pole position au Grand Prix des Etats-Unis ce dimanche avec Max Verstappen a ses cotes et le titre mondial en ligne de mire.",
            "body": [
                "Kimi Antonelli a signe une seance de qualifications eblouissante samedi apres-midi sur le Circuit des Ameriques, s'adjugeant la pole position du Grand Prix des Etats-Unis 2026 avec un chrono de 1:34.035. Le prodige italien a domine le premier secteur sinueux pour devancer la Red Bull de Max Verstappen de 0,179 seconde, offrant a Mercedes un avantage strategique majeur avant les 56 tours de course a Austin.",
                "Cette pole position offre a Antonelli l'opportunite d'etendre encore son avance au championnat du monde. Avec 102 points d'avance sur son equipier George Russell (340 contre 238), Antonelli peut mathematiquement decrocher sa premiere couronne mondiale des ce dimanche s'il l'emporte et que Russell termine au-dela de la cinquieme place. Verstappen s'elancera en premiere ligne a la recherche d'une quatrieme victoire a COTA, tandis que Ferrari verra Charles Leclerc et Lewis Hamilton en embuscade."
            ]
        },
        "es": {
            "title": "Dia de carrera en Austin: Antonelli parte desde la pole con Verstappen como escolta en COTA",
            "subtitle": "El novato de Mercedes supera a Verstappen por 0.179 segundos en la clasificacion. Antonelli busca sellar el titulo mundial.",
            "excerpt": "Kimi Antonelli arranca en pole position en el Gran Premio de Estados Unidos este domingo con Max Verstappen en primera fila y el campeonato en juego.",
            "body": [
                "Kimi Antonelli consiguio una vuelta de clasificacion fantastica el sabado por la tarde en el Circuito de las Americas, asegurando la pole position para el Gran Premio de Estados Unidos 2026 con un tiempo de 1:34.035. El joven italiano domino las rapidas curvas del primer sector para aventajar al Red Bull de Max Verstappen por 0.179 segundos y desatar la alegria en el garaje de Mercedes de cara a las 56 vueltas del domingo.",
                "La pole coloca a Antonelli en una posicion inmejorable para ampliar su ventaja en la clasificacion de pilotos. Con 102 puntos de ventaja sobre George Russell (340 a 238 puntos), Antonelli puede consagrarse campeon mundial de Formula 1 este domingo si se lleva la victoria y Russell finaliza fuera de los cinco primeros puestos. Verstappen largara a su lado en primera fila buscando su cuarto triunfo en Texas, en una prueba donde la gestion termica de los neumaticos sera clave."
            ]
        },
        "de": {
            "title": "Renntag in Austin: Antonelli startet von der Pole vor Verstappen auf dem COTA",
            "subtitle": "Mercedes-Rookie schlaegt Verstappen im Qualifying um 0,179 Sekunden. Antonelli greift nach dem WM-Titel.",
            "excerpt": "Kimi Antonelli steht beim Großen Preis der USA auf der Pole Position, waehrend Max Verstappen aus der ersten Reihe startet und um die WM gekaempft wird.",
            "body": [
                "Kimi Antonelli zauberte am Samstagnachmittag auf dem Circuit of the Americas eine sensationelle Qualifikationsrunde auf den Asphalt und sicherte sich mit 1:34.035 die Pole Position fuer den Großen Preis der USA 2026. Der italienische Youngster dominierte die schnellen Kurven von Sektor 1 und verwies Red-Bull-Star Max Verstappen um 0,179 Sekunden auf Rang zwei, was Mercedes vor dem 56-Runden-Krimi beste Aussichten verschafft.",
                "Mit dieser Pole kann Antonelli seinen ueberlegenen Vorsprung in der Fahrerwertung weiter ausbauen. Bei 102 Punkten Vorsprung auf Teamkollege George Russell (340 zu 238 Punkte) kann Antonelli am Sonntag rechnerisch seinen ersten WM-Titel perfekt machen, sollte er gewinnen und Russell die Top Fünf verpassen. Verstappen startet aus der ersten Startreihe und peilt seinen vierten Austin-Sieg an, waehrend erwartet hohe Asphalttemperaturen eine anspruchsvolle Zweistopp-Strategie verlangen."
            ]
        },
        "it": {
            "title": "Giorno di gara ad Austin: Antonelli scatta in pole con Verstappen al fianco al COTA",
            "subtitle": "Il rookie Mercedes precede Verstappen di 0.179 secondi nelle qualifiche. Antonelli a caccia dell'alloro iridato.",
            "excerpt": "Kimi Antonelli parte dalla pole position al Gran Premio degli Stati Uniti questa domenica con Max Verstappen in prima fila e la corona mondiale in palio.",
            "body": [
                "Kimi Antonelli ha firmato un giro di qualifica da applausi sabato pomeriggio al Circuit of the Americas, conquistando la pole position del Gran Premio degli Stati Uniti 2026 con il crono di 1:34.035. Il talento italiano della Mercedes e stato impeccabile nel primo settore, beffando la Red Bull di Max Verstappen per 0.179 secondi e regalando al team di Brackley la miglior posizione di partenza per i 56 giri di Austin.",
                "Questa pole position consente ad Antonelli di consolidare il proprio vantaggio nella classifica piloti. Con 102 punti di margine sul compagno George Russell (340 contro 238), Antonelli puo chiudere matematicamente la partita per il titolo mondiale domenica in caso di vittoria con Russell fuori dai primi cinque. Verstappen partira al suo fianco cercando il quarto sigillo in Texas, mentre Leclerc e Hamilton partiranno dalla seconda fila."
            ]
        },
        "pl": {
            "title": "Niedziela wyscigowa w Austin: Antonelli startuje z pole position przed Verstappenem",
            "subtitle": "Debiutant Mercedesa pokonuje Verstappena o 0,179 sekundy w kwalifikacjach. Antonelli poluje na tytul mistrza swiata.",
            "excerpt": "Kimi Antonelli rusza z pole position do Grand Prix Stanow Zjednoczonych, majac obok siebie Maxa Verstappena i tytul mistrzowski na wyciagniecie reki.",
            "body": [
                "Kimi Antonelli zaliczyl rewelacyjny wystep w sobotnich kwalifikacjach na Circuit of the Americas, siegajac po pole position do Grand Prix Stanow Zjednoczonych 2026 z czasem 1:34.035. Wloski nastolatek okazal sie bezkonkurencyjny w szybkich zakretach pierwszego sektora, wyprzedzajac Maxa Verstappena z Red Bulla o 0,179 sekundy i dajac Mercedesowi idealna pozycje przed 56 okrazeniami w Teksasie.",
                "Wywalczone pierwsze pole stawia Antonellego w znakomitym polozeniu w walce o mistrzostwo swiata. Majac 102 punkty przewagi nad zespołowym partnerem George'em Russellem (340 do 238 punktow), Antonelli moze matematycznie przypieczetowac tytul juz w niedziele, jesli wygra wyscig, a Russell skonczy poza pierwsza piatka. Verstappen ruszy z pierwszej linii w poszukiwaniu czwartego triumfu na COTA, a wysokie temperatury zapowiadaja kluczowa bitwe na strategie dwoch zjazdow."
            ]
        },
        "zh": {
            "title": "奥斯汀正赛日大幕拉开：安东内利斩获杆位，维斯塔潘头排同台起步",
            "subtitle": "梅赛德斯新星排位赛以0.179秒优势险胜维斯塔潘，安东内利全力冲击年度车手总冠军点。",
            "excerpt": "基米·安东内利在美国大奖赛以杆位起跑，与红牛车手维斯塔潘并排占据头排，美洲赛道总冠军争夺一触即发。",
            "body": [
                "基米·安东内利在美洲赛道周六下午的排位赛中表现惊艳，以1分34秒035的单圈成绩勇夺2026年F1美国大奖赛杆位。这位意大利超级新星在第一赛段高速连续弯道展现出无可匹敌的下压力掌控力，以0.179秒的微弱优势力压红牛车队的维斯塔潘，为梅赛德斯车队在周日56圈的正赛中抢占先机。",
                "这个宝贵的杆位让安东内利在车手积分榜上的优势进一步巩固。目前他领先队友拉塞尔多达102分（340分对238分）。如果安东内利在周日夺冠且拉塞尔未能进入前五名，他将提前加冕个人首个F1世界冠军头衔。维斯塔潘将同排起步力争在奥斯汀四度封王，而勒克莱尔与汉密尔顿则在第二排虎视眈眈，轮胎退化与两停策略将成为决定胜负的关键。"
            ]
        },
        "ja": {
            "title": "オースティン決勝日：アントネッリがポール発進、フェルスタッペンが2番手から追撃",
            "subtitle": "メルセデスの新星が予選でフェルスタッペンを0.179秒差で退ける。アントネッリが世界タイトル獲得へ王手。",
            "excerpt": "キミ・アントネッリがアメリカGPでポールポジションからスタート。フロントローのフェルスタッペンとともに王座をかけた戦いに挑みます。",
            "body": [
                "キミ・アントネッリがサーキット・オブ・ジ・アメリカズで行われた土曜午後の予選で圧巻のアタックを披露し、1分34秒035の好タイムで2026年F1アメリカGPのポールポジションを射止めました。イタリアの逸材はセクター1の連続高速コーナーで圧倒的な速さを見せ、レッドブルのマックス・フェルスタッペンを0.179秒差で抑えてメルセデスに歓喜をもたらしました。",
                "このポール獲得により、アントネッリはドライバーズ選手権での優位を決定的なものにする好機を迎えました。チームメイトのジョージ・ラッセルに102点差（340点対238点）をつけており、アントネッリが優勝しラッセルが6位以下に沈めば自身初の世界王者が確定します。隣にはCOTA4勝目を狙うフェルスタッペンが並び、猛暑下のタイヤマネジメントと2ストップ戦略が勝敗を握ります。"
            ]
        },
        "ko": {
            "title": "오스틴 레이스 데이: 안토넬리 COTA 폴포지션, 베르스타펜 2위 출발",
            "subtitle": "메르세데스 루키 예선에서 베르스타펜을 0.179초 차로 제치고 1위 차지. 안토넬리 월드 챔피언십 조기 확정 조준.",
            "excerpt": "키미 안토넬리가 일요일 미국 그랑프리 폴포지션에서 출발합니다. 막스 베르스타펜이 프런트 로우에서 추격하며 챔피언 타이틀이 걸린 승부가 펼쳐집니다.",
            "body": [
                "키미 안토넬리가 토요일 오후 서킷 오브 디 아메리카스에서 환상적인 예선 랩을 선보이며 1분 34초 035의 기록으로 2026 미국 그랑프리 폴포지션을 차지했습니다. 이탈리아 출신 10대 루키 안토넬리는 섹터 1의 고속 코너 구간을 완벽하게 주파해 레드불의 막스 베르스타펜을 0.179초 차로 제치고 메르세데스 차고에 축포를 안겼습니다.",
                "이번 폴포지션으로 안토넬리는 드라이버 챔피언십 우승에 한 걸음 더 다가섰습니다. 팀 동료 조지 러셀에 102점 차(340점 대 238점)로 앞서 있는 안토넬리는 일요일 레이스에서 우승하고 러셀이 5위 밖으로 밀려날 경우 생애 첫 F1 월드 챔피언 타이틀을 조기 확정 짓게 됩니다. 베르스타펜이 첫 줄에서 COTA 4번째 우승을 노리는 가운데 고온의 트랙에서 타이어 마모 관리가 승부처가 될 전망입니다."
            ]
        },
        "ar": {
            "title": "يوم السباق في اوستن: انطونيلي ينطلق من الصدارة وفيرستابن يطارده في كوتا",
            "subtitle": "نجم مرسيدس الشاب يتفوق على فيرستابن بفارق 0.179 ثانية في التجارب التأهيلية. انطونيلي يقترب من حسم اللقب العالمي.",
            "excerpt": "ينطلق كيمي انطونيلي من المركز الاول في سباق جائزة الولايات المتحدة الكبرى اليوم بجوار ماكس فيرستابن مع اقتراب حسم لقب بطولة العالم.",
            "body": [
                "قدم كيمي انطونيلي لفة تأهيلية خيالية بعد ظهر السبت في حلبة الاميركتين، ليحرز مركز الانطلاق الاول لسباق جائزة الولايات المتحدة الكبرى 2026 بزمن قدره 1:34.035. وبرهن السائق الايطالي الشاب على براعته الفائقة في المنعطفات السريعة بالقطاع الاول ليتفوق على بطل ريد بول ماكس فيرستابن بفارق 0.179 ثانية، ليمنح مرسيدس صدارة شبكة الانطلاق لسباق الاحد المكون من 56 لفة.",
                "ويضع هذا المركز الاول انطونيلي في موقع مثالي لتعزيز صدارته لبطولة العالم للسائقين. وبفارق 102 نقطة عن زميله جورج راسل (340 مقابل 238 نقطة)، يستطيع انطونيلي حسم لقبه العالمي الاول حسابيا يوم الاحد اذا حقق الفوز وانهاه راسل خارج المراكز الخمسة الاولى. وينطلق فيرستابن من الصف الاول باحثا عن فوزه الرابع في اوستن، بينما ينتظر ان تلعب استراتيجية التوقفين وادارة الاطارات دورا حاسما."
            ]
        }
    },
    "pga-tour-bermuda-sunday-final-round-power-smotherman-co-lead-2026": {
        "fr": {
            "title": "Denouement aux Bermudes : Power et Smotherman co-leaders apres 54 trous",
            "subtitle": "Seamus Power et Austin Smotherman a 14 sous le par. Blanchet et Hirata en embuscade dans le vent dominical.",
            "excerpt": "Seamus Power et Austin Smotherman partagent la tete avant le tour final du Butterfield Bermuda Championship avec un tableau serre a leur poursuite.",
            "body": [
                "Tous les ingredients sont reunis pour une fin de tournoi palpitante au Butterfield Bermuda Championship, l'Irlandais Seamus Power et l'Americain Austin Smotherman partageant les commandes a 14 sous le par a Port Royal. Les deux hommes ont su dompter des rafales a plus de 30 km/h venues de l'Atlantique samedi lors du troisieme tour, reussissant des sauvetages de pars capitaux sur la dangereuse sequence cotiere des trous 15 a 17.",
                "Power, deja couronne sur ce parcours par le passe, a rendu une carte solide de 68 (-3) tandis que Smotherman signait cinq birdies sur son retour pour un 67 (-4). Les deux coleaders comptent un coup d'avance sur le heros du premier tour Chandler Blanchet et le Japonais Kensei Hirata (-13). Le Canadien Corey Conners suit a deux longueurs (-12), promettant un duel explosif sur le celebre par 3 du 16 dominant l'ocean."
            ]
        },
        "es": {
            "title": "Definicion en Bermudas: Power y Smotherman comparten el liderato tras 54 hoyos",
            "subtitle": "Seamus Power y Austin Smotherman mandan con 14 bajo par. Blanchet e Hirata al acecho en el viento dominical.",
            "excerpt": "Seamus Power y Austin Smotherman lideran de cara a la ronda final del Butterfield Bermuda Championship con una tabla muy apretada.",
            "body": [
                "El desenlace del Butterfield Bermuda Championship promete maxima tension este domingo con el irlandes Seamus Power y el estadounidense Austin Smotherman empatados en la cima con 14 bajo par en Port Royal Golf Course. Ambos golfistas supieron navegar vientos atlanticos de 30 km/h durante el sabado, firmando salvadas clave de par en la exigente seccion costera de los hoyos 15 al 17.",
                "Power, quien ya gano en este trazado, firmo un sereno 68 (-3) el sabado, mientras Smotherman registro cinco birdies en los segundos nueve hoyos para entregar un 67 (-4). Ambos afrontan los ultimos 18 hoyos con un golpe de renta sobre Chandler Blanchet y el japones Kensei Hirata (-13). Corey Conners acecha a dos golpes (-12), con el mitico hoyo 16 sobre el oceano listo para dictar sentencia."
            ]
        },
        "de": {
            "title": "Showdown auf Bermuda: Power und Smotherman fuehren nach 54 Loechern gemeinsam",
            "subtitle": "Seamus Power und Austin Smotherman liegen bei 14 unter Par. Blanchet und Hirata lauern im Atlantikwind.",
            "excerpt": "Seamus Power und Austin Smotherman teilen sich vor der Finalrunde der Butterfield Bermuda Championship die Fuehrung vor einem dichten Verfolgerfeld.",
            "body": [
                "Auf dem Port Royal Golf Course bahnt sich ein hochdramatischer Schlusstag an: Der Ire Seamus Power und der US-Amerikaner Austin Smotherman teilen sich nach drei Runden mit 14 unter Par die Fuehrung bei der Butterfield Bermuda Championship. Beide Profis trotzten am Samstag boeigen Winden von 30 km/h vom Atlantik und glaenzten mit starken Par-Rettungen an den anspruchsvollen Kuestenloechern 15 bis 17.",
                "Power, der auf diesem Platz bereits einen PGA-Tour-Titel geholt hat, spielte eine kontrollierte 68 (-3), waehrend Smotherman mit fuehnf Birdies auf den zweiten Neun eine 67 (-4) verbuchte. Das Duo geht mit einem Schlag Vorsprung auf Chandler Blanchet und den Japaner Kensei Hirata (-13) auf die letzte Runde. Auch der topgesetzte Kanadier Corey Conners liegt bei 12 unter Par in Schlagdistanz fuer das packende Finale am beruehmten 16. Loch ueber dem tuerkisblauen Meer."
            ]
        },
        "it": {
            "title": "Resa dei conti a Bermuda: Power e Smotherman guidano dopo 54 buche",
            "subtitle": "Seamus Power e Austin Smotherman guidano a 14 sotto il par. Blanchet e Hirata all'inseguimento nel vento oceanico.",
            "excerpt": "Seamus Power e Austin Smotherman si dividono il comando in vista dell'ultimo giro del Butterfield Bermuda Championship con una classifica cortissima.",
            "body": [
                "Tutto e pronto per un finale al cardiopalma al Butterfield Bermuda Championship: l'irlandese Seamus Power e lo statunitense Austin Smotherman condividono il comando a 14 sotto il par a Port Royal. Entrambi hanno domato venti oceanici a oltre 30 km/h nella giornata di sabato, salvando par preziosi nel delicato tratto costiero tra le buche 15 e 17.",
                "Power, che su questo campo ha gia vinto sul PGA Tour, ha chiuso sabato in 68 (-3), mentre Smotherman ha piazzato cinque birdie sulle seconde nove per un giro in 67 (-4). La coppia vanta un solo colpo di margine su Chandler Blanchet e sul giapponese Kensei Hirata (-13). Il canadese Corey Conners insegue a quota -12 in vista delle decisive 18 buche finali con la spettacolare buca 16 a picco sull'oceano."
            ]
        },
        "pl": {
            "title": "Finalowa walka na Bermudach: Power i Smotherman liderami po 54 dolkach",
            "subtitle": "Seamus Power i Austin Smotherman prowadza z wynikiem 14 ponizej par. Blanchet i Hirata naciskaja w niedzielnym wietrze.",
            "excerpt": "Seamus Power i Austin Smotherman dziela prowadzenie przed niedzielna runda finalowa Butterfield Bermuda Championship z grupa poscigowa za plecami.",
            "body": [
                "Niedzielny final Butterfield Bermuda Championship na polu Port Royal zapowiada sie pasjonujaco: Irlandczyk Seamus Power i Amerykanin Austin Smotherman dziela prowadzenie po trzech rundach z wynikiem 14 ponizej par. Obaj zawodnicy znakomicie poradzili sobie z porywistym wiatrem znad Atlantyku dochodzacym do 30 km/h, ratujac wazne pary na trudnym nadmorskim fragmencie od dolka 15 do 17.",
                "Power, ktory juz wczesniej triumfowal na tym polu, zanotowal w sobote solidne 68 (-3), zas Smotherman popisal sie piecioma birdie na drugiej dziewiatce, uzyskujac 67 (-4). Wspolliderzy maja jeden uderzeniowy przewagi nad Chandlerem Blanchetem i Japonczykiem Kenseiem Hirata (-13). Corey Conners traci tylko dwa uderzenia (-12), co gwarantuje emocje do ostatniego putta na slynnej 16. wyspie."
            ]
        },
        "zh": {
            "title": "百慕大锦标赛决赛轮前瞻：鲍尔与斯莫瑟曼54洞后并列领跑",
            "subtitle": "谢默斯·鲍尔与奥斯汀·斯莫瑟曼总成绩低于标准杆14杆，布兰切特与平田宪圣大风中紧追不舍。",
            "excerpt": "百慕大锦标赛进入周日决胜轮，爱尔兰名将鲍尔与美国球手斯莫瑟曼以-14杆并列榜首，争冠集团咬合极为紧密。",
            "body": [
                "2026年百慕大锦标赛在皇家港高尔夫球场迎来了决战时刻。爱尔兰名将谢默斯·鲍尔与美国球手奥斯汀·斯莫瑟曼在打完前54洞后同以低于标准杆14杆的成绩并列领先。周六第三轮两人顶住了大西洋超过每小时20英里的强风考验，在海滨沿岸关键的15至17号洞展现出极佳的救帕韧性。",
                "曾在本项赛事登顶的鲍尔周六交出稳定的68杆（-3），而斯莫瑟曼后九洞抓下5只小鸟交出67杆（-4）。两人目前仅领先首轮纪录创造者布兰切特和日本新星平田宪圣（-13杆）1杆。加拿大好手科纳斯也以-12杆虎视眈眈，周日标志性的海边16号洞将再度成为决出冠军归属的试金石。"
            ]
        },
        "ja": {
            "title": "バミューダ選手権最終ラウンド展望：パワーとスモーザーマンが54ホール首位タイ",
            "subtitle": "シェーマス・パワーとオースティン・スモーザーマンが通算14アンダー。ブランシェットと平田憲聖が日曜の強風の中で追撃。",
            "excerpt": "バターフィールド・バミューダ選手権は日曜の最終日を迎え、パワーとスモーザーマンが通算14アンダーで首位タイに並び大混戦となっています。",
            "body": [
                "ポートロイヤル・ゴルフコースで開催中のバターフィールド・バミューダ選手権は緊迫の最終日を迎えました。アイルランドのシェーマス・パワーと米国のオースティン・スモーザーマンが3日目を終えて通算14アンダーで首位を分け合っています。両選手は土曜、大西洋からの時速30キロを超える突風を巧みにいなし、海岸沿いの難関15番から17番で貴重なパーセーブを連発しました。",
                "当コースでの優勝経験を持つパワーは手堅く68（-3）をマークし、スモーザーマンもバックナインで5バーディを奪い67（-4）をマーク。初日記録保持者のブランシェットと日本の平田憲聖（-13）が1打差の3位タイで追う展開となっています。カナダの実力者コーリー・コナーズも2打差（-12）につけており、エメラルドグリーンの海越えとなる名物16番ホールが栄冠の行方を左右します。"
            ]
        },
        "ko": {
            "title": "버뮤다 챔피언십 최종 라운드 격돌: 파워와 스모더먼 54홀 공동 선두",
            "subtitle": "셰이머스 파워와 오스틴 스모더먼 14언더파 선두 질주. 블랑셰와 히라타 1타 차 추격.",
            "excerpt": "버터필드 버뮤다 챔피언십 최종 라운드를 앞두고 아일랜드의 파워와 미국의 스모더먼이 14언더파로 공동 선두에 올랐습니다.",
            "body": [
                "포트 로열 골프코스에서 펼쳐지는 버터필드 버뮤다 챔피언십이 마지막 18홀을 앞두고 치열한 우승 경쟁에 돌입했습니다. 아일랜드의 셰이머스 파워와 미국의 오스틴 스모더먼이 3라운드 합계 14언더파를 기록하며 나란히 공동 선두로 올라섰습니다. 두 선수는 토요일 시속 30km가 넘는 대서양 바닷바람 속에서도 까다로운 15번부터 17번 홀을 완벽하게 파 세이브하며 선두권을 지켰습니다.",
                "이 대회 우승 경험이 있는 파워는 3라운드에서 68타(-3)를 적어냈고, 스모더먼은 후반 9홀에서 버디 5개를 쓸어 담으며 67타(-4)를 기록했습니다. 1라운드 코스 레코드를 세운 블랑셰와 일본의 히라타 겐세이가 1타 차 공동 3위(-13)로 바짝 뒤쫓고 있으며, 캐나다의 코리 코너스도 12언더파로 역전을 노리고 있습니다. 청록색 바다를 넘겨야 하는 시그니처 16번 홀이 최종 챔피언을 가릴 전망입니다."
            ]
        },
        "ar": {
            "title": "نهائي برمودا المثير: باور وسموثيرمان يتقاسمان الصدارة بعد 54 حفرة",
            "subtitle": "شيموس باور واوستن سموثيرمان في الصدارة بـ14 ضربة تحت المعدل. وبلانشيه وهيراتا يطاردان وسط رياح المحيط.",
            "excerpt": "يتقاسم شيموس باور واوستن سموثيرمان الصدارة قبل الجولة الختامية من بطولة برمودا للغولف وسط مطاردة شرسة من المنافسين.",
            "body": [
                "باتت كل الانظار شاخصة نحو الجولة الختامية لبطولة برمودا للغولف في ملعب بورت رويال، حيث يتقاسم الايرلندي شيموس باور والامريكي اوستن سموثيرمان صدارة الترتيب بعد 54 حفرة برصيد 14 ضربة تحت المعدل. ونجح اللاعبان في مواجهة رياح اطلسية عاتية تجاوزت سرعتها 30 كم/ساعة يوم السبت مسجلين ضربات بار حاسمة على امتداد الحفر الساحلية الصعبة من 15 الى 17.",
                "وسجل باور، الفائز سابقا بهذا اللقب، 68 ضربة (-3) يوم السبت، بينما احرز سموثيرمان خمس ضربات بيردي في النصف الثاني لينهي اليوم بـ67 ضربة (-4). ويتقدم المتصدران بفارق ضربة واحدة على تشاندلر بلانشيه والياباني كينسي هيراتا (-13)، بينما يلاحقهما الكندي كوري كونرز (-12). وستكون الحفرة 16 الشهيرة المطلة على المحيط هي الفيصل في تحديد هوية حامل الكأس."
            ]
        }
    },
    "nfl-week7-sunday-slate-unbeaten-trio-chiefs-49ers-vikings-2026": {
        "fr": {
            "title": "NFL semaine 7 dimanche : les 49ers, Chiefs et Vikings invaincus mettent leur invincibilite en jeu",
            "subtitle": "San Francisco a Atlanta, les Vikings recoivent les Colts et Kansas City defie Seattle lors du Sunday Night Football.",
            "excerpt": "Trois equipes invaincues passent un test majeur ce dimanche lors de la 7e semaine NFL, avec le deplacement de Patrick Mahomes a Seattle.",
            "body": [
                "La 7e semaine de la saison reguliere NFL atteint son apogee ce dimanche 25 octobre avec trois franchises invaincues qui risquent leur parcours immacule au cours d'un programme palpitant de 12 rencontres. Le choc au sommet se deroulera en prime time lors du Sunday Night Football, ou Patrick Mahomes et les champions en titre des Kansas City Chiefs (5-0) plongeront dans le vacarme du Lumen Field pour defier les Seattle Seahawks.",
                "Plus tot dans l'apres-midi, la franchise la plus victorieuse de la ligue, les San Francisco 49ers (6-0), se rend au Mercedes-Benz Stadium d'Atlanta. Brock Purdy et Christian McCaffrey dirigent une attaque californienne a plus de 29 points par match. Pendant ce temps a Minneapolis, les surprenants Minnesota Vikings (5-0) recoivent les Indianapolis Colts. Jeudi soir a Soldier Field, Chicago s'etait impose 30-24 face a New England grâce a 308 yards de Caleb Williams et un coup de pied de 58 yards de Cairo Santos."
            ]
        },
        "es": {
            "title": "NFL Semana 7 domingo: records invictos en juego para 49ers, Chiefs y Vikings",
            "subtitle": "San Francisco visita Atlanta, Vikings reciben a Colts y Kansas City viaja a Seattle en el Sunday Night Football.",
            "excerpt": "Tres equipos invictos exponen su paso perfecto este domingo en la Semana 7 de la NFL con Patrick Mahomes y los Chiefs visitando Seattle.",
            "body": [
                "La Semana 7 de la temporada regular 2026 de la NFL llega a su punto culminante este domingo 25 de octubre con tres franquicias invictas arriesgando su marca perfecta a lo largo de 12 electrizantes partidos. El duelo estelar llegara en horario estelar en el Sunday Night Football, cuando Patrick Mahomes y los campeones Kansas City Chiefs (5-0) se metan al ruidoso Lumen Field para chocar con los Seattle Seahawks.",
                "En la tanda vespertina, el equipo con mejor foja, los San Francisco 49ers (6-0), viajara a Atlanta para medirse a los Falcons con Brock Purdy y Christian McCaffrey comandando una ofensiva de mas de 29 puntos por partido. En Minneapolis, los sorprendentes Minnesota Vikings (5-0) seran anfitriones de los Indianapolis Colts. El jueves, Chicago Bears abrio la jornada ganando 30-24 a New England Patriots con 308 yardas de Caleb Williams y un gol de campo de 58 yardas de Cairo Santos."
            ]
        },
        "de": {
            "title": "NFL Woche 7 Sonntag: Weisse Weste der 49ers, Chiefs und Vikings steht auf dem Spiel",
            "subtitle": "San Francisco gastiert in Atlanta, Vikings empfangen die Colts und Kansas City reist im Sunday Night Football nach Seattle.",
            "excerpt": "Drei ungeschlagene Teams werden am Sonntag in Woche 7 der NFL auf die Probe gestellt, angefuehrt von Patrick Mahomes bei den Seahawks.",
            "body": [
                "Woche 7 der NFL-Saison 2026 erreicht am Sonntag, 25. Oktober, ihren Hoehepunkt: Drei noch unbesiegte Mannschaften setzen ihre perfekte Bilanz in zwoelf packenden Partien aufs Spiel. Das Highlight steigt zur besten Sendezeit im Sunday Night Football, wenn Patrick Mahomes und die Titelverteidiger Kansas City Chiefs (5-0) im stimmgewaltigen Lumen Field auf die Seattle Seahawks treffen.",
                "Zuvor reisen die San Francisco 49ers (6-0) zu den Atlanta Falcons ins Mercedes-Benz Stadium. Brock Purdy und Christian McCaffrey fuehren eine Offensive an, die durchschnittlich ueber 29 Punkte erzielt. Parallel wollen die Minnesota Vikings (5-0) im U.S. Bank Stadium gegen die Indianapolis Colts ungeschlagen bleiben. Am Donnerstag hatten die Chicago Bears die New England Patriots im Soldier Field dank 308 Yards von Caleb Williams mit 30-24 niedergerungen."
            ]
        },
        "it": {
            "title": "NFL Week 7 domenica: record di imbattibilita alla prova per 49ers, Chiefs e Vikings",
            "subtitle": "San Francisco visita Atlanta, i Vikings ospitano i Colts e Kansas City affronta Seattle nel Sunday Night Football.",
            "excerpt": "Tre squadre imbattute mettono alla prova il loro percorso perfetto nella domenica di Week 7 NFL, con Patrick Mahomes a Seattle.",
            "body": [
                "La Week 7 della stagione NFL 2026 tocca il culmine domenica 25 ottobre con tre franchigie imbattute chiamate a difendere il record perfetto in un programma ricchissimo di 12 sfide. Il match clou andra in scena in prima serata nel Sunday Night Football, con Patrick Mahomes e i campioni in carica dei Kansas City Chiefs (5-0) impegnati nell'inferno di Lumen Field contro i Seattle Seahawks.",
                "Nel pomeriggio i San Francisco 49ers (6-0) fanno visita agli Atlanta Falcons al Mercedes-Benz Stadium, guidati dall'attacco da oltre 29 punti a partita di Brock Purdy e Christian McCaffrey. A Minneapolis i sorprendenti Minnesota Vikings (5-0) attendono gli Indianapolis Colts. Giovedi a Soldier Field i Chicago Bears si erano imposti 30-24 sui New England Patriots grazie a 308 yard di Caleb Williams e a un field goal da 58 yard di Cairo Santos."
            ]
        },
        "pl": {
            "title": "Niedziela 7. tygodnia NFL: Niepokonani 49ers, Chiefs i Vikings graja o utrzymanie perfekcji",
            "subtitle": "San Francisco w Atlancie, Vikings podejmuja Colts, a Kansas City leca do Seattle na Sunday Night Football.",
            "excerpt": "Trzy niepokonane druzyny wystawiaja swoj bilans na ciezka probe w 7. tygodniu NFL, z hitem Mahomes kontra Seahawks na czele.",
            "body": [
                "7. tydzien sezonu regularnego NFL osiaga punkt kulminacyjny w niedziele 25 pazdziernika, kiedy trzy niepokonane ekipy powalcza o przedluzenie zwycieskich serii w zestawie 12 pasjonujacych spotkan. Mecz wieczoru w Sunday Night Football to starcie Patricka Mahomesa i mistrzow Kansas City Chiefs (5-0) z glosnym Lumen Field przeciwko Seattle Seahawks.",
                "Wczesniej najlepsi dotad w lidze San Francisco 49ers (6-0) zmierza sie na wyjezdzie z Atlanta Falcons, gdzie Brock Purdy i Christian McCaffrey napedzaja atak zdobywajacy srednio ponad 29 punktow na mecz. Rownolegle w Minneapolis niepokonani Minnesota Vikings (5-0) podejma Indianapolis Colts. W czwartek Chicago Bears pokonali New England Patriots 30-24 po 308 jardach Caleba Williamsa i rekordowym 58-jardowym kopnieciu Cairo Santosa."
            ]
        },
        "zh": {
            "title": "NFL第7周周日开战：49人、酋长与维京人三大不败豪强迎客场大考",
            "subtitle": "旧金山出征亚特兰大，维京人主场迎战小马，堪萨斯城做客西雅图打响周日夜赛决战。",
            "excerpt": "NFL第7周周日战火全开，三支保持全胜的超级强队面临硬仗考验，马霍姆斯领衔酋长客战海鹰打响周日夜赛焦点战。",
            "body": [
                "2026年NFL常规赛第7周在10月25日周日迎来高潮，三支开季保持全胜的球队将在涵盖12场激烈交锋的超级周日接受严峻考验。本轮最具看点的对决当属周日夜赛，帕特里克·马霍姆斯率领卫冕冠军堪萨斯城酋长（5胜0负）奔赴声浪震天的流明球场客场挑战西雅图海鹰。",
                "在此之前，战绩领跑全联盟的旧金山49人（6胜0负）做客梅赛德斯奔驰球场迎战亚特兰大猎鹰，普尔迪与麦卡弗里领衔的49人进攻组场均轰下超过29分。与此同时在明尼阿波利斯，黑马明尼苏达维京人（5胜0负）坐镇主场迎战印第安纳波利斯小马。周四夜赛中芝加哥熊队凭借威廉姆斯传出的308码和桑托斯58码任意球以30-24险胜爱国者，为第7周奠定了火热基调。"
            ]
        },
        "ja": {
            "title": "NFL第7週サンデー：無敗の49ers、チーフス、バイキングスが無傷の記録をかけて激突",
            "subtitle": "サンフランシスコはアトランタ遠征、バイキングスはコルツを迎撃、カンザスシティはSNFでシアトルへ乗り込む。",
            "excerpt": "NFL第7週の日曜日は全勝を維持する3チームが試練の戦いへ。パトリック・マホームズ率いるチーフスがシアトルでSNFに臨みます。",
            "body": [
                "2026年NFLレギュラーシーズン第7週は10月25日日曜日、12試合の豪華ラインナップでクライマックスを迎えます。開幕無敗をキープする3チームが揃って登場。最大の注目はサンデーナイト・フットボールで、パトリック・マホームズ率いる王者カンザスシティ・チーフス（5勝0敗）が敵地ルーメン・フィールドの爆音の中でシアトル・シーホークスと激突します。",
                "日中にはリーグ最多勝のサンフランシスコ・49ers（6勝0敗）がアトランタ・ファルコンズの本拠地に乗り込み、ブロック・パーディとクリスチャン・マキャフリーが牽引する平均29得点超の強力オフェンスが試されます。ミネアポリスでは無敗のバイキングス（5勝0敗）がコルツを迎撃。木曜夜にはケイレブ・ウィリアムズの308ヤードとサントスの58ヤードFGでベアーズがペイトリオッツを30-24で下し、熱戦が続いています。"
            ]
        },
        "ko": {
            "title": "NFL 7주 차 슈퍼 선데이: 49ers, 치프스, 바이킹스 무패 행진 시험대",
            "subtitle": "샌프란시스코 애틀랜타 원정, 바이킹스 콜츠 격돌, 캔자스시티 시애틀서 선데이 나이트 풋볼 격돌.",
            "excerpt": "NFL 7주 차 일요일 3개 무패 팀이 시험대에 오릅니다. 패트릭 머홈스의 치프스가 시애틀 원정에서 선데이 나이트 풋볼을 치릅니다.",
            "body": [
                "2026 NFL 정규시즌 7주 차가 10월 25일 일요일 절정에 달합니다. 개막 후 무패를 달리고 있는 3개 구단이 12경기의 치열한 일전 속에서 퍼펙트 시즌 수성에 나섭니다. 최고의 하이라이트는 선데이 나이트 풋볼로, 패트릭 머홈스가 이끄는 캔자스시티 치프스(5승 0패)가 악명 높은 루멘 필드 원정에서 시애틀 시호크스를 상대합니다.",
                "이에 앞서 리그 최다승의 샌프란시스코 49ers(6승 0패)는 애틀랜타 팰컨스 원정을 떠납니다. 브록 퍼디와 크리스천 맥캐프리가 이끄는 49ers 공격진은 경기당 평균 29점 이상을 몰아치고 있습니다. 미니애폴리스에서는 돌풍의 미네소타 바이킹스(5승 0패)가 인디애나폴리스 콜츠를 홈으로 불러들입니다. 목요일 밤 경기에서는 케일럽 윌리엄스의 308패싱야드와 산토스의 58야드 필드골을 앞세운 베어스가 패트리어츠를 30-24로 제압했습니다."
            ]
        },
        "ar": {
            "title": "احد الاسبوع السابع في NFL: السجلات الخالية من الهزائم في خطر للـ49ers وتشييفس وفايكنغز",
            "subtitle": "سان فرانسيسكو يحل ضيفا على اتلانتا، والفايكنغز يستقبلون كولتس، وكانساس سيتي في مواجهة سياتل بسهرة الاحد.",
            "excerpt": "تخوض ثلاثة فرق لم تتذوق طعم الهزيمة اختبارات قوية يوم الاحد في الاسبوع السابع للـNFL، تتصدرها رحلة باتريك ماهومز الى سياتل.",
            "body": [
                "يصل الاسبوع السابع من دوري كرة القدم الامريكية NFL الى ذروته يوم الاحد 25 اكتوبر مع وضع ثلاثة فرق سجلاتها الخالية من الهزائم على المحك عبر 12 مواجهة نارية. وستكون قمة الجولة في سهرة الاحد، حين يقود باتريك ماهومز حامل اللقب كانساس سيتي تشييفس (5-0) في اجواء صاخبة بملعب لومن فيلد ضد سياتل سيهوكس.",
                "وفي مباريات الظهيرة، يسافر الفريق الاكثر انتصارا سان فرانسيسكو 49ers (6-0) الى اتلانتا لمواجهة الفالكونز، حيث يقود بروك بيردي وكريستيان مكافري هجوما يسجل اكثر من 29 نقطة في اللقاء. وفي مينيابوليس، يستضيف مينيسوتا فايكنغز (5-0) نظيره انديانابوليس كولتس. وكانت الجولة قد انطلقت فجر الجمعة بفوز شيكاغو بيرز على نيو انغلاند باتريوتس 30-24 بفضل 308 ياردات لكاليب ويليامز وهدف ميداني حاسم من 58 ياردة لكايرو سانتوس."
            ]
        }
    }
}

# 1. Strict validation
for slug, langs in OCT25_STORIES.items():
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

# 2. Format snippet for injection
snippet_parts = []
for slug, langs in OCT25_STORIES.items():
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

print("Successfully injected October 25 translations into frontend/src/i18n/stories.ts")
