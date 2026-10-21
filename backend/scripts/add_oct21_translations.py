import json
import re

OCT21_STORIES = {
    "wnba-finals-2026-game3-preview-tied-at-atlanta": {
        "fr": {
            "title": "Match 3 des Finales WNBA ce soir : serie a 1-1 a Atlanta",
            "subtitle": "Angel Reese a porte Atlanta lors du match 2. Coup d'envoi a 20 h 00 ET a la State Farm Arena.",
            "excerpt": "Les Finales WNBA s'installent a la State Farm Arena ce mercredi soir. Golden State et Atlanta sont a egalite 1-1. Le vainqueur prendra une avance de 2-1.",
            "body": [
                "Le match 3 des Finales WNBA commence ce mercredi 21 octobre a 20 h 00 ET a la State Farm Arena. La diffusion est assuree sur USA Network, Peacock et CNBC. Les Golden State Valkyries rendent visite a l'Atlanta Dream alors que la finale est a egalite 1-1. ESPN place Atlanta favorite de 3,5 points sur son parquet. Aucun score n'est enregistre pour ce match 3.",
                "La serie a bascule lundi au Chase Center. Atlanta s'est impose 79-65 grace a Angel Reese, auteur de 30 points et 16 rebonds a 10 sur 16 aux tirs et 9 sur 11 aux lancers francs. Allisha Gray a compile 18 points et Jordin Canada 13 points et 10 passes. Golden State a ete limite a neuf points au troisieme quart. Les deux franchises convoitent leur tout premier titre WNBA. Le vainqueur prendra l'avantage 2-1 dans cette confrontation au meilleur des cinq rencontres."
            ]
        },
        "es": {
            "title": "Juego 3 de las Finales WNBA esta noche: serie 1-1 en Atlanta",
            "subtitle": "Angel Reese lidero a Atlanta en el Juego 2. Salto inicial a las 8:00 p.m. ET en el State Farm Arena.",
            "excerpt": "Las Finales WNBA se trasladan al State Farm Arena este miercoles. Golden State y Atlanta empatan 1-1. Quien gane toma ventaja 2-1.",
            "body": [
                "El Juego 3 de las Finales WNBA se juega este miercoles 21 de octubre a las 8:00 p.m. ET en el State Farm Arena. Se transmite por USA Network, Peacock y CNBC. Las Golden State Valkyries visitan al Atlanta Dream con la eliminatoria empatada 1-1. ESPN marca a Atlanta como favorita por 3,5 puntos en casa. No hay marcador registrado para el Juego 3.",
                "La eliminatoria cambio de inercia el lunes en el Chase Center. Atlanta se impuso 79-65 con 30 puntos y 16 rebotes de Angel Reese (10 de 16 en tiros y 9 de 11 libres). Allisha Gray sumo 18 puntos y Jordin Canada 13 puntos y 10 asistencias. Golden State quedo en nueve tantos en el tercer cuarto. Ambas franquicias buscan su primer anillo de la historia. Quien venza hoy se colocara 2-1 en la serie al mejor de cinco."
            ]
        },
        "de": {
            "title": "WNBA-Finals Spiel 3 heute: Serie steht 1-1 in Atlanta",
            "subtitle": "Angel Reese trug Atlanta in Spiel 2. Tip-off um 20:00 Uhr ET in der State Farm Arena.",
            "excerpt": "Die WNBA-Finals ziehen am Mittwochabend in die State Farm Arena. Golden State und Atlanta stehen 1-1. Der Sieger fuehrt 2-1.",
            "body": [
                "Spiel 3 der WNBA-Finals beginnt am Mittwoch, 21. Oktober, um 20:00 Uhr ET in der State Farm Arena. Die Begegnung laeuft auf USA Network, Peacock und CNBC. Die Golden State Valkyries gastieren beim Atlanta Dream bei einem Serienstand von 1-1. ESPN fuehrt Atlanta mit 3,5 Punkten als Favorit. Fuer Spiel 3 liegt noch kein Ergebnis vor.",
                "Das Momentum kippte am Montag im Chase Center. Atlanta siegte 79-65 angefuehrt von Angel Reese, die 30 Punkte und 16 Rebounds bei 10 von 16 aus dem Feld holte. Allisha Gray steuerte 18 Zaehler bei, Jordin Canada 13 Punkte und 10 Assists. Golden State erzielte im dritten Viertel nur neun Punkte. Beide Teams kaempfen um ihre allererste WNBA-Meisterschaft. Der Sieger geht in der Best-of-Five-Serie 2-1 in Fuehrung."
            ]
        },
        "it": {
            "title": "Gara 3 delle WNBA Finals stasera: serie sull'1-1 ad Atlanta",
            "subtitle": "Angel Reese ha guidato Atlanta in Gara 2. Palla a due alle 20:00 ET alla State Farm Arena.",
            "excerpt": "Le WNBA Finals approdano alla State Farm Arena mercoledi sera. Golden State e Atlanta sono sull'1-1. Chi vince sale 2-1.",
            "body": [
                "Gara 3 delle WNBA Finals inizia mercoledi 21 ottobre alle 20:00 ET alla State Farm Arena. Diretta tv su USA Network, Peacock e CNBC. Le Golden State Valkyries fanno visita all'Atlanta Dream con la serie sul punteggio di 1-1. Le quote ESPN vedono Atlanta favorita di 3,5 punti sul parquet di casa. Nessun punteggio registrato per Gara 3.",
                "La serie e cambiata lunedi al Chase Center. Atlanta ha vinto 79-65 grazie a una prova maiuscola di Angel Reese da 30 punti e 16 rimbalzi (10 su 16 al tiro e 9 su 11 ai liberi). Allisha Gray ha segnato 18 punti e Jordin Canada 13 punti con 10 assist. Golden State e rimasta ferma a 9 punti nel terzo quarto. Entrambe le squadre cercano il primo titolo WNBA della loro storia. Chi vince oggi sale 2-1 nella serie al meglio delle cinque."
            ]
        },
        "pl": {
            "title": "Mecz 3 finalow WNBA dzis wieczorem: remis 1-1 w Atlancie",
            "subtitle": "Angel Reese poprowadzila Atlante w meczu 2. Poczatek o 20:00 ET w State Farm Arena.",
            "excerpt": "Finaly WNBA przenosza sie w srode do State Farm Arena. Golden State i Atlanta maja stan 1-1. Zwyciezca obejmie prowadzenie 2-1.",
            "body": [
                "Mecz 3 finalow WNBA rozpoczyna sie w srode 21 pazdziernika o 20:00 ET w State Farm Arena. Transmisja w USA Network, Peacock i CNBC. Golden State Valkyries graja na wyjezdzie z Atlanta Dream przy stanie serii 1-1. ESPN stawia Atlante w roli faworyta z przewaga 3,5 punktu. Wynik meczu 3 nie jest jeszcze znany.",
                "W poniedzialek w Chase Center Atlanta wygrala 79-65. Angel Reese zdobyla 30 punktow i 16 zbiorek, trafiajac 10 z 16 rzutow z gry i 9 z 11 wolnych. Allisha Gray dodala 18 punktow, a Jordin Canada 13 punktow i 10 asyst. Golden State zdobyly zaledwie 9 punktow w trzeciej kwarcie. Oba kluby walcza o swoje pierwsze mistrzostwo WNBA w historii. Zwyciezca dzisiejszego meczu obejmie prowadzenie 2-1 w serii do trzech wygranych."
            ]
        },
        "zh": {
            "title": "今晚WNBA总决赛第3战：亚特兰大总比分1-1战平",
            "subtitle": "安吉尔·里斯在第2战统治全场。比赛美东时间晚8点在州立农业球馆跳球。",
            "excerpt": "WNBA总决赛周三晚移师亚特兰大。金州女武神与亚特兰大梦想战成1-1平。胜者将在总决赛取得2-1领先。",
            "body": [
                "WNBA总决赛第3战于10月21日周三美东晚8:00在州立农业球馆打响。全美直播平台为USA Network、Peacock与CNBC。金州女武神客场挑战亚特兰大梦想，目前总比分1-1平。ESPN让分盘口主队梦想让3.5分。第3战尚未开赛，暂无比分。",
                "周一在追逐中心进行的第2战中，亚特兰大以79-65获胜。安吉尔·里斯打出30分16篮板的豪华数据，投篮16中10，罚球11中9。阿丽莎·格雷贡献18分，乔丁·加拿大交出13分10助攻。女武神在第三节全队仅得9分。两支球队都在追逐队史首座WNBA总冠军奖杯，今晚的胜者将在五局三胜制系列赛中取得2-1的赛点先机。"
            ]
        },
        "ja": {
            "title": "今夜WNBAファイナル第3戦：アトランタで1勝1敗の対決",
            "subtitle": "第2戦はエンジェル・リースが牽引。ステートファーム・アリーナで東部午後8時ティップオフ。",
            "excerpt": "水曜夜、WNBAファイナルがアトランタへ移動。ゴールデンステイトとアトランタが1勝1敗で激突し、勝者が2勝1敗で王手をかけます。",
            "body": [
                "WNBAファイナル第3戦は10月21日水曜、東部午後8時にステートファーム・アリーナで行われます。中継はUSA Network、Peacock、CNBC。ゴールデンステイト・ヴァルキリーズとアトランタ・ドリームが1勝1敗のタイで対戦します。ESPNの予想オッズはホームのアトランタが3.5点リード。スコアはまだありません。",
                "月曜のチェイス・センターでの第2戦はアトランタが79-65で勝利。エンジェル・リースがFG16本中10本成功、フリースロー11本中9本で30得点16リバウンドをマークしました。アリシャ・グレイが18得点、ジョーディン・カナダが13得点10アシスト。ヴァルキリーズは第3クォーターわずか9得点に抑えられました。両軍とも悲願の初優勝を目指し、今夜勝利したチームが2勝1敗で一歩リードします。"
            ]
        },
        "ko": {
            "title": "오늘 밤 WNBA 파이널 3차전: 애틀랜타에서 1승 1패 팽팽",
            "subtitle": "2차전에서 엔젤 리스가 맹활약. 스테이트팜 아레나에서 동부 저녁 8시 팁오프.",
            "excerpt": "WNBA 파이널이 수요일 밤 애틀랜타로 향합니다. 골든스테이트와 애틀랜타가 1승 1패로 맞서며, 승리팀이 2승 1패로 앞서갑니다.",
            "body": [
                "WNBA 파이널 3차전이 10월 21일 수요일 동부 오후 8시 스테이트팜 아레나에서 시작됩니다. 방송은 USA Network, Peacock, CNBC로 중계됩니다. 골든스테이트 발키리스와 애틀랜타 드림이 시리즈 1승 1패 상황에서 맞붙습니다. ESPN 배당은 홈팀 애틀랜타 3.5점 우세를 점치고 있습니다. 3차전 스코어는 아직 없습니다.",
                "월요일 체이스 센터에서 열린 2차전은 애틀랜타가 79-65로 승리했습니다. 엔젤 리스가 16개 야투 중 10개를 적중시키며 30득점 16리바운드로 코트를 지배했습니다. 얼리샤 그레이가 18득점, 조딘 캐나다가 13득점 10어시스트를 기록했습니다. 골든스테이트는 3쿼터 9점에 그쳤습니다. 두 팀 모두 창단 첫 WNBA 우승을 노리며, 오늘 승리하는 팀이 2승 1패로 유리한 고지를 점합니다."
            ]
        },
        "ar": {
            "title": "المباراة 3 من نهائيات WNBA الليلة: السلسلة متعادلة 1-1 في اتلانتا",
            "subtitle": "انجيل ريس قادت اتلانتا في المباراة 2. البداية الساعة 8:00 مساء بتوقيت الشرق في ستيت فارم ارينا.",
            "excerpt": "تنتقل نهائيات WNBA الى ملعب ستيت فارم ارينا مساء الاربعاء. غولدن ستيت واتلانتا متعادلان 1-1، والفائز يتقدم 2-1.",
            "body": [
                "تنطلق المباراة 3 من نهائيات WNBA يوم الاربعاء 21 اكتوبر في تمام الساعة 8:00 مساء بتوقيت الشرق في ستيت فارم ارينا. تبث المواجهة عبر USA Network وPeacock وCNBC. يحل غولدن ستيت فالكيريز ضيفا على اتلانتا دريم والسلسلة متعادلة 1-1. تضع شبكة ESPN اتلانتا مفضلة بفارق 3.5 نقطة على ارضها. لا نتيجة مسجلة بعد للمباراة 3.",
                "تغير مسار السلسلة يوم الاثنين في تشيس سنتر بعد فوز اتلانتا 79-65 بقيادة انيل ريس التي سجلت 30 نقطة و16 متابعة مسددة 10 من 16 من الميدان و9 من 11 رمية حرة. اضافت اليشا غراي 18 نقطة وسجلت جوردين كندا 13 نقطة و10 تمريرات حاسمة. اكتفى غولدن ستيت بتسع نقاط في الربع الثالث. يسعى الفريقان لتحقيق اول لقب WNBA في تاريخهما، والفائز الليلة سيتقدم 2-1 في السلسلة."
            ]
        }
    },
    "atp-wednesday-almaty-tsitsipas-khachanov-advance-2026": {
        "fr": {
            "title": "Tsitsipas domine Kovacevic a Almaty, Khachanov en deux sets",
            "subtitle": "Stefanos Tsitsipas a sauve trois balles de set dans un tie-break a 11-9. Karen Khachanov s'impose sans trembler.",
            "excerpt": "Tsitsipas a battu Kovacevic 7-6(9), 3-6, 6-3 en deux heures mercredi. Khachanov a domine Sakamoto 6-2, 6-4. Duckworth ecarte Darderi.",
            "body": [
                "Stefanos Tsitsipas a surmonte un defi intense d'Aleksandar Kovacevic mercredi 21 octobre, l'emportant 7-6(9), 3-6, 6-3 au premier tour de l'Open d'Almaty. Le joueur grec a sauve trois balles de set dans un jeu decisif intense de vingt points au premier set avant de conclure en deux heures de jeu sur le dur interieur du Kazakhstan. Ce succes lui permet de prendre sa revanche sur Kovacevic apres Winston-Salem et de rallier les huitiemes de finale.",
                "Tete de serie numero 5, Karen Khachanov a livre une prestation maitrisee sur le court central en disposant du qualifie japonais Rei Sakamoto 6-2, 6-4 en une heure et cinq minutes. Khachanov n'a pas concede la moindre balle de break de toute la partie. L'Australien James Duckworth a cree la surprise du jour en eliminant Luciano Darderi, tete de serie numero 2, sur le score de 7-5, 7-6(7). A Lyon, le succes de Corentin Moutet face a Ugo Humbert 6-2, 6-7(5), 7-6(4) reste valide, tout comme le sacre de Davidovich Fokina a Shanghai."
            ]
        },
        "es": {
            "title": "Tsitsipas supera a Kovacevic en Almaty, Khachanov avanza firme",
            "subtitle": "Stefanos Tsitsipas salvo tres bolas de set en un desempate de 11-9. Karen Khachanov resolvio en dos mangas.",
            "excerpt": "Tsitsipas derroto a Kovacevic 7-6(9), 3-6, 6-3 en dos horas el miercoles. Khachanov vencio a Sakamoto 6-2, 6-4. Duckworth dio la sorpresa ante Darderi.",
            "body": [
                "Stefanos Tsitsipas resistio una dura batalla ante Aleksandar Kovacevic este miercoles 21 de octubre, ganando 7-6(9), 3-6, 6-3 en la primera ronda del ATP de Almaty. El tenista griego salvo tres puntos de set en un desempate de veinte puntos en la manga inicial antes de cerrar el duelo tras dos horas en la pista dura bajo techo de Kazajistan. Esta victoria le permite vengar su derrota previa en Winston-Salem y avanzar a octavos.",
                "El quinto cabeza de serie, Karen Khachanov, domino su estreno al batir al clasificado japones Rei Sakamoto por 6-2, 6-4 en una hora y cinco minutos, sin conceder ni un solo punto de rotura con su saque. Por su parte, el australiano James Duckworth protagonizo la sorpresa de la jornada al dejar fuera al segundo preclasificado Luciano Darderi por 7-5, 7-6(7). Siguen en pie el triunfo de Moutet sobre Humbert en Lyon y el titulo de Davidovich Fokina en Shangai."
            ]
        },
        "de": {
            "title": "Tsitsipas ringt Kovacevic in Almaty nieder, Khachanov souveraen",
            "subtitle": "Stefanos Tsitsipas wehrte drei Satzbaelle im 11-9 Tiebreak ab. Karen Khachanov siegte glatt in zwei Saetzen.",
            "excerpt": "Tsitsipas schlug Kovacevic am Mittwoch 7-6(9), 3-6, 6-3 in zwei Stunden. Khachanov besiegte Sakamoto 6-2, 6-4. Duckworth ueberraschte gegen Darderi.",
            "body": [
                "Stefanos Tsitsipas setzte sich am Mittwoch, 21. Oktober, in einem packenden Erstrundenmatch beim Turnier in Almaty mit 7-6(9), 3-6, 6-3 gegen Aleksandar Kovacevic durch. Der Grieche wehrte im ersten Satz drei Satzbaelle in einem dramatischen Tiebreak ab und sicherte sich nach zwei Stunden auf dem Hallenhartplatz das Weiterkommen ins Achtelfinale.",
                "Der an Nummer fuenf gesetzte Karen Khachanov zeigte eine dominante Leistung und bezwang den japanischen Qualifikanten Rei Sakamoto in 65 Minuten mit 6-2, 6-4, ohne eine einzige Breakchance zuzulassen. Fuer die groesste Ueberraschung des Tages sorgte James Duckworth mit einem 7-5, 7-6(7) ueber den an zwei gesetzten Luciano Darderi. In Lyon bleibt Moutets Dreisatzsieg ueber Humbert bestehen, ebenso Davidovich Fokinas Titelgewinn in Shanghai."
            ]
        },
        "it": {
            "title": "Tsitsipas piega Kovacevic ad Almaty, Khachanov passa in due set",
            "subtitle": "Stefanos Tsitsipas ha annullato tre set point nel tie-break finito 11-9. Karen Khachanov avanza senza affanni.",
            "excerpt": "Tsitsipas supera Kovacevic 7-6(9), 3-6, 6-3 in due ore mercoledi. Khachanov batte Sakamoto 6-2, 6-4. Duckworth sorprende Darderi.",
            "body": [
                "Stefanos Tsitsipas ha superato una dura battaglia contro Aleksandar Kovacevic mercoledi 21 ottobre, vincendo 7-6(9), 3-6, 6-3 al primo turno dell'ATP di Almaty. Il tennista greco ha annullato tre set point in un combattuto tie-break da venti punti nel primo set, chiudendo l'incontro in due ore sul cemento indoor kazako. Il successo vendica la sconfitta rimediata a Winston-Salem.",
                "La testa di serie numero cinque Karen Khachanov ha dominato il qualificato giapponese Rei Sakamoto per 6-2, 6-4 in un'ora e cinque minuti, senza concedere palle break sul proprio servizio. La sorpresa di giornata porta la firma di James Duckworth, che ha eliminato la testa di serie numero due Luciano Darderi con il punteggio di 7-5, 7-6(7). Restano invariati il successo di Moutet su Humbert a Lione e la vittoria di Davidovich Fokina a Shanghai."
            ]
        },
        "pl": {
            "title": "Tsitsipas pokonuje Kovacevicia w Almatach, pewny Khachanov",
            "subtitle": "Stefanos Tsitsipas obronil trzy pilki setowe w tie-breaku wygranym 11-9. Karen Khachanov wygral w dwoch setach.",
            "excerpt": "Tsitsipas wygral z Kovaceviciem 7-6(9), 3-6, 6-3 w dwie godziny w srode. Khachanov pokonal Sakamoto 6-2, 6-4. Duckworth pokonal Darderiego.",
            "body": [
                "Stefanos Tsitsipas stoczyl ciezkie spotkanie z Aleksandarem Kovaceviciem w srode 21 pazdziernika, wygrywajac 7-6(9), 3-6, 6-3 w pierwszej rundzie turnieju w Almatach. Grek obronil trzy pilki setowe w dramatycznym tie-breaku pierwszego seta i po dwoch godzinach gry w hali zameldowal sie w 1/8 finalu, rewanzujac sie za porazke z Winston-Salem.",
                "Rozstawiony z numerem piatym Karen Khachanov pewnie odprawil japonskiego kwalifikanta Rei Sakamoto 6-2, 6-4 w godzine i piec minut, nie tracac ani jednego break pointa przy wlasnym podaniu. Najwieksza niespodzianke sprawil James Duckworth, eliminujac turniejowa dwojke Luciano Darderiego 7-5, 7-6(7). Z wtorku w mocy pozostaje triumf Mouteta nad Humbertem w Lyonie i tytul Davidovicha Fokiny w Szanghaju."
            ]
        },
        "zh": {
            "title": "西西帕斯阿拉木图苦战过关，哈恰诺夫轻松晋级",
            "subtitle": "西西帕斯在抢七中挽救三个盘点以11-9逆转。哈恰诺夫直落两盘击败坂本怜。",
            "excerpt": "周三西西帕斯耗时两小时以7-6(9)、3-6、6-3击败科瓦切维奇。哈恰诺夫6-2、6-4轻取对手。达克沃斯爆冷击败达尔德里。",
            "body": [
                "10月21日周三在哈萨克斯坦阿拉木图公开赛首轮，希腊名将西西帕斯经历苦战以7-6(9)、3-6、6-3击败美国选手科瓦切维奇。西西帕斯在首盘抢七中挽救了连续三个盘点，激战20分后以11-9险胜，耗时整整两个小时完成复仇并晋级16强。",
                "5号种子哈恰诺夫表现稳健，耗时65分钟以6-2、6-4完胜日本资格赛选手坂本怜，全场未送出任何破发点。澳大利亚老将达克沃斯制造了当天最大冷门，以7-5、7-6(7)淘汰2号种子达尔德里。此前里昂站穆泰激战淘汰卫冕冠军安贝尔，以及上海大师赛达维多维奇·福基纳击败霍达尔夺冠的赛果保持不变。"
            ]
        },
        "ja": {
            "title": "チチパスがアルマティで激闘を制す、ハチャノフは完勝",
            "subtitle": "チチパスは11-9のタイブレークで3つのセットポイントをしのぐ。ハチャノフはストレート勝ち。",
            "excerpt": "水曜のアルマティでチチパスがコバチェビッチを7-6(9), 3-6, 6-3で下しました。ハチャノフは坂本怜を6-2, 6-4で退けました。",
            "body": [
                "10月21日水曜、アルマティ・オープンの1回戦でステファノス・チチパスがアレクサンダー・コバチェビッチを7-6(9), 3-6, 6-3で破り2回戦へ進出しました。チチパスは第1セットのタイブレークで3つのセットポイントを耐え抜き、2時間の熱戦で過去の敗戦を雪辱しました。",
                "第5シードのカレン・ハチャノフは日本の予選勝者である坂本怜にブレークポイントを一切与えず、65分で6-2, 6-4と快勝。オーストラリアのジェームズ・ダックワースは第2シードのルチアーノ・ダルデリを7-5, 7-6(7)で破る金星を挙げました。リヨンでのミュテの勝利、上海でのダビドビッチ・フォキナの優勝スコアもそのまま記録されています。"
            ]
        },
        "ko": {
            "title": "치치파스, 알마티에서 접전 끝 승리... 하차노프는 완승",
            "subtitle": "스테파노스 치치파스가 11-9 타이브레이크에서 세트포인트 3개를 방어. 카렌 하차노프는 무실세트 통과.",
            "excerpt": "치치파스는 수요일 코바체비치를 7-6(9), 3-6, 6-3으로 꺾었습니다. 하차노프는 사카모토를 6-2, 6-4로 제압했습니다.",
            "body": [
                "10월 21일 수요일 알마티 오픈 1회전에서 스테파노스 치치파스가 알렉산다르 코바체비치를 상대로 7-6(9), 3-6, 6-3 접전 끝에 승리했습니다. 치치파스는 1세트 타이브레이크에서 상대의 세트포인트 3개를 지워내며 2시간 혈투 끝에 16강에 올랐습니다.",
                "5번 시드 카렌 하차노프는 일본 예선 통과자 사카모토 레이를 1시간 5분 만에 6-2, 6-4로 완파하며 브레이크 포인트를 단 한 차례도 내주지 않았습니다. 호주의 제임스 덕워스는 2번 시드 루치아노 다르데리를 7-5, 7-6(7)으로 꺾는 이변을 일으켰습니다. 리옹에서 무테의 승리와 상하이에서 다비도비치 포키나의 우승 기록은 그대로 유지됩니다."
            ]
        },
        "ar": {
            "title": "تسيتسيباس يتخطى كوفاسيفيتش في الماتي، وخاتشانوف يتاهل بسهولة",
            "subtitle": "ستيفانوس تسيتسيباس انقذ ثلاث نقاط حاسمة للمجموعة في شوط كسر التعادل 11-9. كارين خاتشانوف فاز بمجموعتين دون رد.",
            "excerpt": "فاز تسيتسيباس على كوفاسيفيتش 7-6(9) و3-6 و6-3 في ساعتين يوم الاربعاء. خاتشانوف تجاوز ساكاموتو 6-2 و6-4. داكوورث اسقط دارديري.",
            "body": [
                "نجا ستيفانوس تسيتسيباس من اختبار صعب امام الكسندر كوفاسيفيتش يوم الاربعاء 21 اكتوبر ليفوز 7-6(9) و3-6 و6-3 في الدور الاول لبطولة الماتي المفتوحة. انقذ اللاعب اليوناني ثلاث نقاط للمجموعة في شوط كسر التعادل بالاولى قبل ان يحسم المواجهة في ساعتين على الملاعب الصلبة المغطاة في كازاخستان معوضا خسارته السابقة في وينستون-سالم.",
                "قدم المصنف الخامس كارين خاتشانوف اداء مسيطرا متغلبا على الياباني ري ساكاموتو 6-2 و6-4 في ساعة وخمس دقائق دون مواجهة اي نقطة لكسر ارساله. وحقق الاسترالي جيمس داكوورث مفاجاة اليوم باقصاء المصنف الثاني لوتشيانو دارديري بنتيجة 7-5 و7-6(7). تبقى نتيجة فوز موتيه على هومبير في ليون وتتويج دافيدوفيتش فوكينا في شنغهاي ثابتة."
            ]
        }
    },
    "nfl-week7-wednesday-patriots-bears-tnf-preview-2026": {
        "fr": {
            "title": "Les Patriots chez les Bears jeudi soir : coup d'envoi de la semaine 7",
            "subtitle": "Soldier Field accueille la rencontre a 20 h 15 ET sur Prime Video. Les 49ers restent a 6-0.",
            "excerpt": "New England et Chicago abordent le Thursday Night Football a 4-2. Chicago est favori de 3 points. San Francisco demeure la seule equipe a 6-0.",
            "body": [
                "La semaine 7 de la NFL s'ouvre jeudi 22 octobre a 20 h 15 ET au Soldier Field. Les New England Patriots rendent visite aux Chicago Bears, avec une diffusion assuree sur Prime Video. ESPN donne Chicago favori de 3 points a domicile. Les deux formations affichent un bilan de 4-2 et visent un pas supplementaire vers les playoffs. Aucun score n'est inscrit mercredi.",
                "Les entrainements de mercredi ont affine les plans de jeu apres la conclusion de la semaine 6. Les 49ers de San Francisco restent la seule franchise invaincue a 6-0 apres avoir battu les Commanders de Washington 23-17 lundi soir (Purdy 264 yards, McCaffrey 2 touchdowns). Kansas City et Minnesota sont a 5-0. Les Bills, Jaguars, Chargers et Commanders sont au repos cette semaine."
            ]
        },
        "es": {
            "title": "Los Patriots visitan a los Bears el jueves: arranca la semana 7",
            "subtitle": "Soldier Field alberga el inicio a las 8:15 p.m. ET por Prime Video. Los 49ers siguen 6-0.",
            "excerpt": "Tanto New England como Chicago llegan al Thursday Night Football con 4-2. Chicago es favorito por 3 puntos. San Francisco sigue invicto con 6-0.",
            "body": [
                "La semana 7 de la NFL abre el jueves 22 de octubre a las 8:15 p.m. ET en Soldier Field. Los New England Patriots visitan a los Chicago Bears por Prime Video. ESPN situa a Chicago como favorito por 3 puntos en casa. Ambos equipos presentan marca de 4-2 en busca de posicionarse en la lucha por postemporada. El miercoles no hay partido ni marcador.",
                "Las practicas del miercoles dejaron listos los esquemas tras el cierre de la semana 6. Los San Francisco 49ers son el unico equipo 6-0 de la NFL tras batir a los Washington Commanders 23-17 el lunes (Purdy 264 yardas, McCaffrey 2 anotaciones terrestres). Chiefs y Vikings continuan invictos con 5-0. Descansan esta semana Bills, Jaguars, Chargers y Commanders."
            ]
        },
        "de": {
            "title": "Patriots gastieren Donnerstag bei den Bears: Woche 7 beginnt",
            "subtitle": "Kickoff im Soldier Field um 20:15 Uhr ET auf Prime Video. Die 49ers stehen 6-0.",
            "excerpt": "Sowohl New England als auch Chicago gehen mit 4-2 ins Thursday Night Football. Chicago ist 3 Punkte favorisiert. San Francisco bleibt als einziges Team bei 6-0.",
            "body": [
                "Die 7. NFL-Woche startet am Donnerstag, 22. Oktober, um 20:15 Uhr ET im Soldier Field. Die New England Patriots reisen zu den Chicago Bears, live auf Prime Video. ESPN fuehrt Chicago mit drei Punkten Vorsprung. Beide Teams stehen bei 4-2 und wollen ihre Playoff-Ambitionen untermauern. Am Mittwoch gibt es kein Spiel und keinen Spielstand.",
                "Im Mittwochstraining wurden die Plaene nach Abschluss von Woche 6 fixiert. Die San Francisco 49ers sind nach dem 23-17 ueber die Commanders am Montagabend das einzige 6-0-Team der Liga (Purdy 264 Yards, McCaffrey 2 Touchdowns). Chiefs und Vikings stehen ungeschlagen bei 5-0. Spielfrei haben diese Woche die Bills, Jaguars, Chargers und Commanders."
            ]
        },
        "it": {
            "title": "I Patriots sfidano i Bears giovedi notte: apre la Week 7",
            "subtitle": "Soldier Field teatro della sfida alle 20:15 ET su Prime Video. I 49ers restano 6-0.",
            "excerpt": "Sia New England che Chicago arrivano al Thursday Night Football sul 4-2. Chicago favorita di 3 punti. San Francisco resta l'unica squadra a 6-0.",
            "body": [
                "La Week 7 della NFL scatta giovedi 22 ottobre alle 20:15 ET al Soldier Field. I New England Patriots affrontano i Chicago Bears in diretta su Prime Video. Le quote ESPN danno Chicago favorita di 3 punti in casa. Entrambe le formazioni vantano un record di 4-2 e cercano punti pesanti per i playoff. Mercoledi non si gioca e non c'e alcun punteggio.",
                "Gli allenamenti del mercoledi hanno definito i piani partita dopo la chiusura del sesto turno. I San Francisco 49ers guidano la NFL come unica franchigia a 6-0 dopo il 23-17 inflitto ai Washington Commanders lunedi notte (Purdy 264 yard, McCaffrey 2 mete). Chiefs e Vikings restano imbattuti a 5-0. Turno di riposo per Bills, Jaguars, Chargers e Commanders."
            ]
        },
        "pl": {
            "title": "Patriots u Bears w czwartkowa noc: inauguracja 7. tygodnia",
            "subtitle": "Kickoff na Soldier Field o 20:15 ET na Prime Video. 49ers legitymuja sie bilansem 6-0.",
            "excerpt": "Zarowno New England, jak i Chicago przystepuja do meczu z bilansem 4-2. Chicago faworytem o 3 punkty. San Francisco pozostaje jedyna ekipa 6-0.",
            "body": [
                "Tydzien 7 w NFL otwiera czwartkowe spotkanie 22 pazdziernika o 20:15 ET na Soldier Field. New England Patriots zagraja z Chicago Bears w transmisji Prime Video. ESPN stawia Chicago jako 3-punktowego faworyta. Obie druzyny maja bilans 4-2 i walcza o umocnienie pozycji w strefie play-off. W srode nie ma zadnego meczu ani wyniku.",
                "Srodowe treningi zamknely przygotowania po zakonczeniu tygodnia 6. San Francisco 49ers sa jedyna druzyna w lidze z bilansem 6-0 po pokonaniu Washington Commanders 23-17 w poniedzialek (Purdy 264 jardy, McCaffrey 2 przylozenia). Chiefs i Vikings pozostaja niepokonani z 5-0. W tym tygodniu pauzuja Bills, Jaguars, Chargers i Commanders."
            ]
        },
        "zh": {
            "title": "周四夜赛爱国者客战熊：NFL第7周揭开战幕",
            "subtitle": "士兵球场美东晚8:15开踢，Prime Video直播。49人保持6胜0负。",
            "excerpt": "新英格兰与芝加哥同以4胜2负战绩进军周四夜赛。芝加哥主场让3分。旧金山依然是全联盟唯一保持不败的6胜0负队伍。",
            "body": [
                "NFL第7周将于10月22日周四美东晚8:15在士兵球场打响。新英格兰爱国者客场挑战芝加哥熊，由Prime Video进行全美直播。ESPN盘口显示熊队主场让3分。两支球队目前战绩同为4胜2负，力求在季后赛门票争夺中占得先机。周三比赛尚未开始，无比分。",
                "周三各队训练结束了第6周的复盘与周四战术演练。旧金山49人在周一夜赛以23-17力克华盛顿指挥官后，以6胜0负成为联盟唯一全胜球队（珀迪传球264码1次达阵，麦卡弗里冲球贡献两次达阵）。酋长与维京人同为5胜0负保持不败。第7周轮空的队伍包括比尔、美洲虎、闪电与指挥官。"
            ]
        },
        "ja": {
            "title": "木曜夜にペイトリオッツがベアーズを訪問：第7週開幕へ",
            "subtitle": "ソルジャー・フィールドで東部午後8時15分キックオフ。49ersは6勝0敗を維持。",
            "excerpt": "ニューイングランドとシカゴはともに4勝2敗でサーズデーナイトへ。シカゴが3点リードの予想。サンフランシスコは唯一の6勝0敗。",
            "body": [
                "NFL第7週は10月22日木曜、東部午後8時15分にソルジャー・フィールドで幕を開けます。ニューイングランド・ペイトリオッツがシカゴ・ベアーズと対戦し、Prime Videoで生中継されます。ESPNのラインはシカゴが3点優勢。両チームともに4勝2敗でプレーオフ争いに向けた大事な一戦を迎えます。水曜に試合はなくスコアもありません。",
                "水曜の練習で第6週を受けた戦術が固まりました。サンフランシスコ・49ersは月曜夜にワシントン・コマンダーズを23-17で退け、リーグ唯一の6勝0敗を守っています（パーディ264ヤード、マカフリーがランで2TD）。チーフスとバイキングスは5勝0敗を維持。今週はビルズ、ジャガーズ、チャージャーズ、コマンダーズがバイウィークに入ります。"
            ]
        },
        "ko": {
            "title": "목요일 밤 패트리어츠 대 베어스: NFL 7주차 개막",
            "subtitle": "솔저 필드에서 동부 저녁 8시 15분 킥오프, Prime Video 중계. 49ers는 6승 0패 유지.",
            "excerpt": "뉴잉글랜드와 시카고 모두 4승 2패로 서스데이 나이트에 돌입합니다. 시카고 3점 우세. 샌프란시스코는 유일한 6승 무패 팀입니다.",
            "body": [
                "NFL 7주차가 10월 22일 목요일 동부 오후 8시 15분 솔저 필드에서 시작됩니다. 뉴잉글랜드 패트리어츠가 시카고 베어스 원정에 나서며 Prime Video로 중계됩니다. ESPN은 홈팀 시카고의 3점 우세를 예측했습니다. 두 팀 모두 4승 2패를 기록 중이며 플레이오프 경쟁에 속도를 내려 합니다. 수요일 경기는 없습니다.",
                "수요일 훈련을 통해 6주차 후속 준비가 마무리되었습니다. 샌프란시스코 49ers는 월요일 밤 워싱턴 커맨더스를 23-17로 꺾고 리그 유일의 6승 0패 팀으로 우뚝 섰습니다 (퍼디 264야드, 매캐프리 런 2TD). 치프스와 바이킹스는 5승 무패를 달리고 있습니다. 이번 주 휴식팀은 빌스, 재규어스, 차저스, 커맨더스입니다."
            ]
        },
        "ar": {
            "title": "باتريوتس في ضيافة بيرز ليلة الخميس: انطلاق الاسبوع 7",
            "subtitle": "ملعب سولجر فيلد يستضيف ضربة البداية الساعة 8:15 مساء بتوقيت الشرق عبر برايم فيديو. 49ers عند 6-0.",
            "excerpt": "يدخل نيو انغلاند وشيكاغو مواجهة الخميس برصيد 4-2 لكل منهما. شيكاغو مرشحة بفارق 3 نقاط. سان فرانسيسكو الفريق الوحيد بسجل 6-0.",
            "body": [
                "يفتتح الاسبوع 7 من دوري NFL يوم الخميس 22 اكتوبر في تمام الساعة 8:15 مساء بتوقيت الشرق في ملعب سولجر فيلد. يحل نيو انغلاند باتريوتس ضيفا على شيكاغو بيرز عبر برايم فيديو. تضع شبكة ESPN شيكاغو كمرشحة بفارق 3 نقاط. يدخل الفريقان اللقاء بسجل 4-2 سعيا لحجز مقعد مبكر في الادوار الاقصائية. لا مباريات يوم الاربعاء.",
                "اختتمت تدريبات الاربعاء الخطط الفنية بعد نهاية الاسبوع السادس. يبقى سان فرانسيسكو 49ers الفريق الوحيد بسجل 6-0 بعد هزيمة واشنطن كوماندرز 23-17 ليلة الاثنين (بوردي 264 ياردة، مكفري لمستان ارضيتان). تشيفس وفايكنغز بسجل 5-0. الفرق في راحة هذا الاسبوع هي بيلز، جاغوارز، تشارجرز، وكوماندرز."
            ]
        }
    },
    "premier-league-wednesday-spurs-rebound-city-lead-mw8-lookahead": {
        "fr": {
            "title": "Les Spurs savourent leur succes : City garde trois points d'avance",
            "subtitle": "Tottenham prepare le deplacement a Chelsea. Manchester City caracole en tete avec 21 points.",
            "excerpt": "Les Spurs sont 16es apres leur succes 3-1 contre Coventry. La 8e journee s'ouvre vendredi, avec Chelsea recevant Tottenham samedi.",
            "body": [
                "Tottenham Hotspur a prepare mercredi son derby londonien contre Chelsea avec un moral retrouve. Les Spurs ont quitte la 20e et derniere place pour remonter au 16e rang lundi soir grace a une victoire 3-1 contre Coventry City au Tottenham Hotspur Stadium. James Maddison a ouvert le score a la 14e minute pour sa premiere titularisation en 536 jours, Omar Marmoush a double la mise a la 58e et Ben Davies a scelle l'issue dans le temps additionnel devant 60 913 spectateurs.",
                "Ce resultat place Tottenham a 6 points (1-3-3, 6 buts marques, 10 encaisses), a egalite avec Coventry City (2-0-5). Fulham, Nottingham Forest et Sunderland ferment la marche. Aucun match n'est dispute mercredi. Manchester City domine le classement avec un sans-faute de 21 points en sept rencontres apres son succes 3-2 contre Ipswich. Arsenal suit a trois longueurs (18 points), devant Brighton (16 points). La 8e journee debute vendredi avec Ipswich contre Forest, avant Chelsea face a Tottenham samedi."
            ]
        },
        "es": {
            "title": "El Spurs asimila su primer triunfo: el City mantiene tres puntos de renta",
            "subtitle": "El Tottenham prepara su visita a Stamford Bridge. El Manchester City lidera con 21 puntos.",
            "excerpt": "Los Spurs marchan 16os tras vencer 3-1 al Coventry. La fecha 8 abre el viernes y el sabado Chelsea recibe a Tottenham.",
            "body": [
                "El Tottenham Hotspur trabajo este miercoles con nuevos animos de cara al derbi londinense del sabado ante el Chelsea. Los Spurs salieron del fondo de la tabla para situarse en la 16a plaza el lunes por la noche al imponerse 3-1 al Coventry City en el Tottenham Hotspur Stadium. James Maddison abrio la cuenta en el minuto 14 en su primera titularidad en 536 dias, Omar Marmoush anoto en el 58 y Ben Davies cerro la cuenta en el tiempo añadido ante 60.913 espectadores.",
                "Tottenham suma 6 puntos (1-3-3), empatado con el Coventry City (2-0-5). Fulham, Nottingham Forest y Sunderland ocupan la zona de descenso. No hay partidos programados para este miercoles. El Manchester City manda en solitario con 21 puntos tras siete victorias consecutivas (3-2 a Ipswich), con tres de margen sobre el Arsenal (18) y cinco sobre el Brighton (16). La jornada 8 arranca el viernes y vivira el sabado el duelo entre Chelsea y Spurs."
            ]
        },
        "de": {
            "title": "Spurs schöpfen Mut: City haelt Drei-Punkte-Polster an der Spitze",
            "subtitle": "Tottenham bereitet sich auf Chelsea an der Stamford Bridge vor. Manchester City fuehrt mit 21 Punkten.",
            "excerpt": "Die Spurs kletterten nach dem 3-1 ueber Coventry auf Rang 16. Spieltag 8 startet am Freitag, Samstag empfaengt Chelsea Tottenham.",
            "body": [
                "Tottenham Hotspur nutzte den Mittwoch zur Vorbereitung auf das Londoner Derby gegen Chelsea. Mit dem 3-1-Heimsieg gegen Coventry City verliessen die Spurs am Montagabend das Tabellenende und kletterten auf Rang 16. James Maddison traf bei seinem ersten Startelfeinsatz nach 536 Tagen in der 14. Minute, Omar Marmoush legte in der 58. nach und Ben Davies traf in der Nachspielzeit vor 60.913 Zuschauern.",
                "Tottenham steht bei 6 Punkten (1-3-3), punktgleich mit Coventry (2-0-5). Fulham, Nottingham Forest und Sunderland belegen die Abstiegsplaetze. Am Mittwoch finden keine Premier-League-Spiele statt. Manchester City bleibt mit der maximalen Ausbeute von 21 Punkten aus sieben Spielen das Mass aller Dinge, gefolgt von Arsenal mit 18 und Brighton mit 16 Punkten. Der 8. Spieltag beginnt am Freitag mit Ipswich gegen Forest, ehe am Samstag Chelsea die Spurs empfaengt."
            ]
        },
        "it": {
            "title": "Gli Spurs respirano: il City conserva tre punti di vantaggio",
            "subtitle": "Il Tottenham prepara il derby a Stamford Bridge contro il Chelsea. Manchester City primo a punteggio pieno con 21 punti.",
            "excerpt": "Gli Spurs salgono al 16o posto dopo il 3-1 al Coventry. L'ottava giornata scatta venerdi, sabato c'e Chelsea contro Tottenham.",
            "body": [
                "Il Tottenham Hotspur ha lavorato mercoledi con rinnovato entusiasmo in vista del derby di sabato contro il Chelsea. Gli Spurs hanno abbandonato l'ultimo posto risalendo al sedicesimo grazie alla vittoria per 3-1 sul Coventry City al Tottenham Hotspur Stadium. James Maddison ha segnato al 14' nella sua prima da titolare dopo 536 giorni, Omar Marmoush ha raddoppiato al 58' e Ben Davies ha chiuso i conti nel recupero davanti a 60.913 spettatori.",
                "Il Tottenham sale a 6 punti (1-3-3), appaiato al Coventry City (2-0-5). Fulham, Nottingham Forest e Sunderland restano sul fondo. Nessuna gara in programma mercoledi. Il Manchester City comanda a quota 21 con sette vittorie su sette dopo il 3-2 all'Ipswich, staccando l'Arsenal a quota 18 e il Brighton a 16. Il prossimo turno si aprira venerdi sera prima del clou tra Chelsea e Spurs a Stamford Bridge."
            ]
        },
        "pl": {
            "title": "Spurs po pierwszym zwyciestwie: City utrzymuja trzy punkty przewagi",
            "subtitle": "Tottenham przygotowuje sie do starcia z Chelsea na Stamford Bridge. Manchester City liderem z 21 punktami.",
            "excerpt": "Spurs awansowali na 16. miejsce po wygranej 3-1 z Coventry. Kolejka 8 rusza w piatek, w sobote Chelsea podejmie Tottenham.",
            "body": [
                "Tottenham Hotspur z nowa energia przygotowywal sie w srode do derbowego starcia z Chelsea. Wygrana 3-1 z Coventry City w poniedzialkowy wieczor na Tottenham Hotspur Stadium pozwolila Spurs opuscic dno tabeli i wskoczyc na 16. pozycje. James Maddison trafil w 14. minucie w pierwszym wystepie w wyjsciowym skladzie od 536 dni, Omar Marmoush podwyzszyl w 58. minucie, a Ben Davies przypieczetowal sukces w doliczonym czasie gry przy 60 913 kibicach.",
                "Tottenham ma na koncie 6 punktow (1-3-3), tyle samo co Coventry (2-0-5). Strefa spadkowa nalezy do Fulham, Nottingham Forest i Sunderlandu. W srode Premier League nie gra. Manchester City prowadzi z kompletem 21 punktow po siedmiu meczach (3-2 z Ipswich), wyprzedzajac Arsenal (18 punktow) i Brighton (16 punktow). Kolejka 8 startuje w piatek meczem Ipswich z Forest, a w sobote Chelsea podejmie Spurs."
            ]
        },
        "zh": {
            "title": "热刺品尝赛季首胜：曼城领跑积分榜保有3分优势",
            "subtitle": "热刺全队备战斯坦福桥德比。曼城7战全胜积21分位列榜首。",
            "excerpt": "热刺3-1击败考文垂后升至积分榜第16位。英超第8轮将于周五开打，周六切尔西主场迎战热刺。",
            "body": [
                "托特纳姆热刺在周三积极备战周六做客斯坦福桥挑战切尔西的伦敦德比。周一晚在托特纳姆热刺球场，热刺3-1击败考文垂，成功摆脱垫底位置并升至第16名。麦迪逊在时隔536天首次首发登场并于第14分钟破门，马尔穆什第58分钟建功，本·戴维斯补时锁定胜局，现场观众达60913人。",
                "热刺目前积6分（1胜3平3负），与考文垂积分相同。富勒姆、诺丁汉森林与桑德兰位列降级区。10月21日周三并无英超赛事。曼城前7轮全胜积21分领跑积分榜，阿森纳落后3分积18分紧随其后，布莱顿积16分排名第三。第8轮将于周五由伊普斯维奇迎战森林拉开序幕，周六迎来切尔西对阵热刺的重头戏。"
            ]
        },
        "ja": {
            "title": "トッテナムが初勝利で一息：マンチェスター・Cは勝ち点3差で首位堅持",
            "subtitle": "スパーズはスタンフォード・ブリッジでのチェルシー戦へ準備。マンチェスター・Cが21点で首位。",
            "excerpt": "スパーズはコベントリーに3-1で勝ち16位へ浮上。第8節は金曜開幕、土曜にチェルシー対トッテナムが行われます。",
            "body": [
                "トッテナム・ホットスパーは水曜、土曜に控えるチェルシーとのロンドン・ダービーに向けて士気を高めました。月曜夜にホームでコベントリーを3-1で下し、最下位から16位へと順位を上げました。536日ぶりに先発したジェームズ・マディソンが14分に先制点を挙げ、オマル・マルムシュが58分に追加点、ベン・デイヴィスが後半アディショナルタイムにダメ押し点を決めました（観客60,913人）。",
                "トッテナムは勝ち点6（1勝3分3敗）でコベントリーと並び、降級圏にはフラム、フォレスト、サンダーランドが沈んでいます。水曜に試合はありません。マンチェスター・シティは7戦全勝の勝ち点21で首位を快走し、アーセナルが勝ち点18、ブライトンが16で追う展開。第8節は金曜に開幕し、土曜にチェルシー対スパーズのダービーを迎えます。"
            ]
        },
        "ko": {
            "title": "첫 승 거둔 토트넘: 맨시티, 승점 3점 차 선두 질주",
            "subtitle": "스탬퍼드 브리지에서 열릴 첼시전 대비. 맨체스터 시티는 21점으로 선두.",
            "excerpt": "토트넘은 코번트리전 3-1 승리로 16위로 도약했습니다. 8라운드는 금요일 개막하며 토요일 첼시와 토트넘이 맞붙습니다.",
            "body": [
                "토트넘 홋스퍼는 수요일, 토요일 첼시와의 런던 더비를 앞두고 활기찬 분위기 속에 훈련을 진행했습니다. 월요일 밤 홈에서 코번트리 시티를 3-1로 제압하며 최하위에서 16위로 올라섰습니다. 536일 만에 선발 출전한 제임스 매디슨이 14분 선제골을 터뜨렸고, 오마르 마르무시가 58분, 벤 데이비스가 추가시간 쐐기골을 기록했습니다 (관중 60,913명).",
                "토트넘은 1승 3무 3패 승점 6점으로 코번트리와 동률을 이뤘으며, 풀럼, 노팅엄 포리스트, 선덜랜드가 강등권에 머물렀습니다. 수요일 경기 일정은 없습니다. 맨체스터 시티는 7전 전승 승점 21점으로 1위를 달리고 있으며 아스널이 18점, 브라이턴이 16점으로 뒤를 잇고 있습니다. 8라운드는 금요일 입스위치 대 포리스트로 시작해 토요일 첼시 대 토트넘 경기로 이어집니다."
            ]
        },
        "ar": {
            "title": "توتنهام يتنفس بعد فوزه الاول: سيتي يحافظ على فارق ثلاث نقاط في الصدارة",
            "subtitle": "توتنهام يستعد لمواجهة تشيلسي في ستامفورد بريدج. مانشستر سيتي يتصدر برصيد 21 نقطة.",
            "excerpt": "صعد توتنهام للمركز 16 اثر فوزه 3-1 على كوفنتري. تنطلق الجولة 8 الجمعة، ويستضيف تشيلسي توتنهام يوم السبت.",
            "body": [
                "استعد توتنهام هوتسبير يوم الاربعاء لديربي لندن يوم السبت امام تشيلسي بمعنويات مرتفعة. غادر الفريق المركز الاخير وصعد الى المركز 16 بعد فوزه مساء الاثنين 3-1 على كوفنتري سيتي في ملعبه. افتتح جيمس ماديسون التسجيل في الدقيقة 14 في اول مشاركة اساسية له منذ 536 يوما، واضاف عمر مرموش الهدف الثاني في الدقيقة 58 وسجل بن ديفيز في الوقت بدل الضائع امام 60913 متفرجا.",
                "يملك توتنهام 6 نقاط (1-3-3) متساويا مع كوفنتري سيتي. تقبع فرق فولهام ونوتنغهام فورست وسندرلاند في مراكز الهبوط. لا توجد مباريات في الدوري الممتاز يوم الاربعاء. يتصدر مانشستر سيتي بالعلامة الكاملة برصيد 21 نقطة من سبع مباريات، يليه ارسنال برصيد 18 نقطة وبرايتون برصيد 16 نقطة. تنطلق الجولة الثامنة الجمعة بلقاء ابسويتش وفورست، قبل قمة السبت بين تشيلسي وتوتنهام."
            ]
        }
    },
    "pga-tour-bermuda-wednesday-pro-am-opens-thursday-2026": {
        "fr": {
            "title": "Fin du Pro-Am aux Bermudes : Port Royal s'elance jeudi",
            "subtitle": "Adam Schenk defend son titre a Southampton. La victoire de Michael Brennan a 16 sous le par reste la reference.",
            "excerpt": "Le Pro-Am officiel s'est termine mercredi aux Bermudes. Le premier tour debute jeudi pour un champ de 120 joueurs en quete de 500 points FedExCup.",
            "body": [
                "Le Butterfield Bermuda Championship a conclu son traditionnel Pro-Am mercredi sur le parcours de Port Royal a Southampton, aux Bermudes. Le tournoi officiel commence jeudi 22 octobre et s'etend jusqu'au dimanche 25 octobre. Le trace par 71 dessine par Robert Trent Jones s'etend sur 6 828 yards le long de l'ocean Atlantique. La dotation globale s'eleve a 6 millions de dollars, dont 1,08 million et 500 points FedExCup pour le vainqueur. Golf Channel diffusera l'epreuve en direct de jeudi a dimanche de 13 h a 16 h ET.",
                "Un plateau de 120 joueurs est attendu au depart, avec un cut fixe aux 65 premiers et ex aequo apres 36 trous. Le tenant du titre Adam Schenk tente de devenir le premier joueur a conserver son trophee ici. Le Canadien Corey Conners est le joueur le mieux classe a la 61e place mondiale. Aucun coup n'a ete joue pour le score officiel mercredi. Le succes de Michael Brennan a 16 sous le par lors du Baycurrent Classic demeure le dernier titre attribue sur le circuit."
            ]
        },
        "es": {
            "title": "Concluye el Pro-Am en Bermudas: Port Royal arranca el jueves",
            "subtitle": "Adam Schenk defiende corona en Southampton. Sigue vigente el triunfo de Michael Brennan con 16 bajo par.",
            "excerpt": "El Pro-Am oficial finalizo el miercoles en Bermudas. La primera ronda abre el jueves con 120 jugadores peleando por 500 puntos FedExCup.",
            "body": [
                "El Butterfield Bermuda Championship cerro su Pro-Am oficial este miercoles en el campo de Port Royal en Southampton, Bermudas. El torneo oficial se disputara del jueves 22 al domingo 25 de octubre. El diseno par 71 de Robert Trent Jones cuenta con 6.828 yardas frente a la costa del Atlantico. La bolsa asciende a 6 millones de dolares, con 1,08 millones y 500 puntos FedExCup para el campeon. Golf Channel emitira en directo de jueves a domingo de 1:00 a 4:00 p.m. ET.",
                "Un cuadro de 120 golfistas tomara la salida, con el corte fijado en los 65 mejores y empatados tras 36 hoyos. El campeon defensor Adam Schenk intentara revalidar el trofeo. El canadiense Corey Conners llega como el mejor clasificado mundial en el puesto 61. El miercoles no hubo golpes computables para la clasificacion. El titulo de Michael Brennan con 16 bajo par en el Baycurrent Classic se mantiene como el resultado oficial mas reciente."
            ]
        },
        "de": {
            "title": "Bermuda Pro-Am beendet: Port Royal startet am Donnerstag",
            "subtitle": "Adam Schenk verteidigt Titel in Southampton. Michael Brennans 16-unter-Par-Sieg bleibt der letzte Massstab.",
            "excerpt": "Das offizielle Pro-Am endete am Mittwoch auf Bermuda. Runde 1 beginnt am Donnerstag fuer 120 Spieler im Kampf um 500 FedExCup-Punkte.",
            "body": [
                "Die Butterfield Bermuda Championship hat am Mittwoch das Pro-Am auf dem Port Royal Golf Course in Southampton abgeschlossen. Das offizielle Turnier laeuft von Donnerstag, 22. Oktober, bis Sonntag, 25. Oktober. Der Par-71-Kurs von Robert Trent Jones misst 6.828 Yards entlang der Kueste. Das Preisgeld betraegt 6 Millionen Dollar, der Sieger erhaelt 1,08 Millionen und 500 FedExCup-Punkte. Golf Channel uebertraegt taeglich von 13:00 bis 16:00 Uhr ET.",
                "120 Profis treten an, der Cut erfolgt nach 36 Loechern fuer die besten 65 und Schlaggleichen. Titelverteidiger Adam Schenk peilt den historischen Durchmarsch an, waehrend der Kanadier Corey Conners als Weltranglisten-61. der topgesetzte Spieler ist. Am Mittwoch wurden keine gewerteten Turnierrunden gespielt. Michael Brennans Sieg bei der Baycurrent Classic mit 16 unter Par bleibt das aktuellste Ergebnis auf der Tour."
            ]
        },
        "it": {
            "title": "Chiuso il Pro-Am alle Bermuda: giovedi il via a Port Royal",
            "subtitle": "Adam Schenk difende il titolo a Southampton. Il successo di Michael Brennan a -16 resta l'ultimo riferimento.",
            "excerpt": "Il Pro-Am ufficiale si e concluso mercoledi alle Bermuda. Il primo giro scattera giovedi con 120 giocatori a caccia di 500 punti FedExCup.",
            "body": [
                "Il Butterfield Bermuda Championship ha completato mercoledi il consueto Pro-Am sul percorso del Port Royal Golf Course a Southampton, Bermuda. La gara vera e propria prendera il via giovedi 22 ottobre per concludersi domenica 25 ottobre. Il percorso par 71 misura 6.828 yard a ridosso dell'Atlantico. Il montepremi e di 6 milioni di dollari, con una prima moneta da 1,08 milioni e 500 punti FedExCup. Diretta su Golf Channel da giovedi a domenica dalle 13:00 alle 16:00 ET.",
                "Al via 120 giocatori con il taglio fissato ai primi 65 e pari merito dopo 36 buche. Il campione in carica Adam Schenk punta al bis, mentre il canadese Corey Conners e il giocatore dal ranking piu alto al numero 61 mondiale. Nessun colpo ufficiale e stato registrato mercoledi. Il successo di Michael Brennan a 16 sotto il par nel Baycurrent Classic resta l'ultimo referto della stagione."
            ]
        },
        "pl": {
            "title": "Koniec Pro-Am na Bermudach: Port Royal startuje w czwartek",
            "subtitle": "Adam Schenk broni tytulu w Southampton. Triumf Michaela Brennana z wynikiem 16 ponizej par pozostaje aktualny.",
            "excerpt": "Oficjalny turniej Pro-Am zakonczyl sie w srode na Bermudach. Runda 1 rozpoczyna sie w czwartek dla 120 graczy walczacych o 500 punktow FedExCup.",
            "body": [
                "Turniej Butterfield Bermuda Championship zakonczyl srodowy Pro-Am na polu Port Royal Golf Course w Southampton na Bermudach. Turniej glowny odbedzie sie w dniach 22-25 pazdziernika. Pole par 71 liczy 6828 jardow wzdluz wybrzeza Atlantyku. Pula nagrod wynosi 6 milionow dolarow, w tym 1,08 miliona dolarow i 500 punktow FedExCup dla triumfatora. Transmisja w Golf Channel od czwartku do niedzieli w godzinach 13:00-16:00 ET.",
                "Na starcie stanie 120 zawodnikow, a cut po 36 dolkach obejmie 65 najlepszych z remisami. Obroncą tytulu jest Adam Schenk, a najwyzej notowanym graczem jest Corey Conners (61. na swiecie). W srode nie rozegrano zadnego dolka rankingowego. Wygrana Michaela Brennana na 16 ponizej par w Baycurrent Classic pozostaje ostatnim rezultatem na desksie."
            ]
        },
        "zh": {
            "title": "百慕大职业业余配对赛落幕：皇家港周四正式开杆",
            "subtitle": "亚当·申克在南安普顿卫冕。迈克尔·布伦南低于标准杆16杆的胜利依然是最新纪录。",
            "excerpt": "百慕大锦标赛职业业余配对赛于周三结束。正赛首轮将于周四开打，120名球员争夺500分联邦快递杯积分。",
            "body": [
                "百慕大锦标赛周三在南安普顿的皇家港高尔夫球场结束了官方职业业余配对赛。正赛将于10月22日周四开杆，持续至10月25日周日。球场标准杆71杆，全长6828码，紧邻大西洋海岸。赛事总奖金为600万美元，冠军可独得108万美元及500个联邦快递杯积分。高尔夫频道将于周四至周日美东时间下午1点至4点进行现场直播。",
                "共有120名球员出战首轮，两轮36洞过后前65位及并列者晋级周末决赛。卫冕冠军亚当·申克力争成为该赛事首位两连冠得主，加拿大选手科里·康纳斯以世界排名第61位成为参赛阵容中排名最高的球员。周三并没有正赛计分，布伦南在Baycurrent精英赛打出低于标准杆16杆的夺冠成绩仍是美巡赛最新官方纪录。"
            ]
        },
        "ja": {
            "title": "バミューダでプロアマ終了：ポートロイヤルが木曜日に開幕",
            "subtitle": "サウサンプトンでアダム・シェンクが連覇に挑む。マイケル・ブレナンの16アンダー優勝が最新。",
            "excerpt": "バミューダで公式プロアマが水曜日に終了。木曜日から120名の選手が500ポイントのフェデックスカップを競います。",
            "body": [
                "バターフィールド・バミューダ選手権は水曜、サウサンプトンのポートロイヤル・ゴルフコースで公式プロアマを終えました。本大会は10月22日木曜から25日日曜まで開催されます。ロバート・トレント・ジョーンズ設計のパー71、6,828ヤードのコースで争われ、賞金総額は600万ドル、優勝賞金108万ドルとフェデックスカップ500ポイントが授与されます。ゴルフチャンネルが木曜から日曜まで午後1時から4時（東部時間）に生中継します。",
                "120名のフィールドで開幕し、36ホール終了時の上位65位タイまでが予選を通過します。前回覇者のアダム・シェンクが大会史上初の連覇を目指し、世界ランク61位のコーリー・コナーズが最上位選手として出場。水曜日に競技スコアは発生していません。ブレナンが16アンダーで制したベイカレント・クラシックの勝利が直近の公式記録となります。"
            ]
        },
        "ko": {
            "title": "버뮤다 프로암 종료: 포트 로열 목요일 1라운드 티오프",
            "subtitle": "애덤 솅크 사우샘프턴에서 타이틀 방어전. 마이클 브레넌의 16언더파 우승이 기준.",
            "excerpt": "버뮤다에서 수요일 공식 프로암이 마무리됐습니다. 120명의 선수가 500점의 페덱스컵 포인트를 두고 목요일 1라운드에 돌입합니다.",
            "body": [
                "버터필드 버뮤다 챔피언십이 사우샘프턴 포트 로열 골프 코스에서 수요일 프로암 대회를 마쳤습니다. 공식 대회는 10월 22일 목요일부터 25일 일요일까지 열립니다. 파71, 6,828야드 규모의 해안 코스에서 펼쳐지며 총상금 600만 달러, 우승 상금 108만 달러와 페덱스컵 포인트 500점이 걸려 있습니다. 골프 채널이 목요일부터 일요일까지 동부 오후 1시부터 4시까지 생중계합니다.",
                "120명의 선수가 출전하며 36홀 후 상위 65위(동타 포함)까지 컷을 통과합니다. 디펜딩 챔피언 애덤 솅크가 2연패를 노리며, 세계랭킹 61위 코리 코너스가 필드 최고 랭커로 나섭니다. 수요일에는 정규 스코어가 기록되지 않았습니다. 브레넌이 베이커런트 클래식에서 16언더파로 거둔 우승이 가장 최근의 공식 기록입니다."
            ]
        },
        "ar": {
            "title": "اختتام منافسات برو-ام في برمودا: بورت رويال يفتتح جولته الاولى الخميس",
            "subtitle": "ادم شينك يدافع عن لقبه في ساوثهامبتون. فوز مايكل برينان بـ16 تحت المعدل يبقى المرجع.",
            "excerpt": "انتهت بطولة برو-ام الرسمية يوم الاربعاء في برمودا. تنطلق الجولة الاولى يوم الخميس بمشاركة 120 لاعبا يتنافسون على 500 نقطة لفيديكس كاب.",
            "body": [
                "اختتمت بطولة باترفيلد برمودا منافسات برو-ام يوم الاربعاء في ملعب بورت رويال في ساوثهامبتون ببرمودا. تنطلق الجولات الرسمية من الخميس 22 اكتوبر حتى الاحد 25 اكتوبر. يبلغ طول الملعب 6828 ياردة بمعدل 71 ضربة على ساحل الاطلسي. تبلغ الجوائز 6 ملايين دولار، ينال الفائز منها 1.08 مليون دولار و500 نقطة لكاس فيديكس. تبث قناة غولف تشانل المنافسات من الخميس الى الاحد بين 1:00 و4:00 مساء بتوقيت الشرق.",
                "يشارك في الجولة الاولى 120 لاعبا، وتتأهل افضل 65 نتيجة بعد 36 حفرة. يسعى حامل اللقب ادم شينك لتكرار انجازه، بينما يعد الكندي كوري كونرز الاعلى تصنيفا في المركز 61 عالميا. لم تسجل اي ضربات في بطاقات النتائج الرسمية يوم الاربعاء، ويبقى فوز مايكل برينان بـ16 تحت المعدل في بايكرنت احدث انجاز مسجل."
            ]
        }
    },
    "f1-austin-wednesday-two-days-to-track-gap-102-2026": {
        "fr": {
            "title": "Le paddock d'Austin s'anime : Antonelli compte 102 points d'avance",
            "subtitle": "Plus que deux jours avant les essais libres a COTA. Course dimanche 25 octobre a 15:00 locale.",
            "excerpt": "Les ecuries de F1 effectuent le reperage de la piste a Austin. Kimi Antonelli mene devant George Russell (340 contre 238). Mercedes compte 134 points d'avance sur Ferrari.",
            "body": [
                "Le Circuit des Ameriques s'est anime avec les points presse et l'installation des garages mercredi 21 octobre, a deux jours des premiers tours de roue du Grand Prix des Etats-Unis. Les Essais Libres 1 sont prevus vendredi 23 octobre, avant les qualifications samedi et la course de 56 tours dimanche 25 octobre a 15:00 heure locale. Le trace de 5,513 km compte 20 virages et une spectaculaire montee de 41 metres vers le virage 1.",
                "Aucun moteur n'a tourne pour une seance chronometree mercredi. Le classement reflete les resultats du Grand Prix de Singapour, remporte par Max Verstappen depuis la pole position. Le jeune Kimi Antonelli domine le championnat du monde des pilotes avec 340 points, soit 102 longueurs d'avance sur son coequipier George Russell (238). Lewis Hamilton pointe a 229, Verstappen a 221, Charles Leclerc a 215 et Lando Norris a 201. Chez les constructeurs, Mercedes totalise 578 points contre 444 pour Ferrari."
            ]
        },
        "es": {
            "title": "Abre el paddock de Austin: Antonelli mantiene 102 puntos de ventaja",
            "subtitle": "Quedan dos dias para las practicas del viernes en COTA. La carrera es el domingo 25 de octubre a las 15:00 local.",
            "excerpt": "Los equipos de Formula 1 completan el recorrido a pie en Austin. Kimi Antonelli lidera sobre George Russell 340 a 238. Mercedes saca 134 puntos a Ferrari.",
            "body": [
                "El Circuito de las Americas bullio con ruedas de prensa y montaje de boxes este miercoles 21 de octubre, a dos dias de que rueden los monoplazas en el Gran Premio de Estados Unidos. Los Libres 1 estan fijados para el viernes 23 de octubre, seguidos de la clasificacion el sabado y la carrera de 56 vueltas el domingo 25 a las 15:00 hora local. El trazado de 5,513 km presenta 20 curvas y una subida de 41 metros hacia la curva 1.",
                "El miercoles no hubo motores encendidos ni tiempos registrados. La tabla del campeonato refleja lo sucedido en Singapur, donde Max Verstappen gano desde la pole. Kimi Antonelli encabeza la clasificacion de pilotos con 340 puntos, 102 por delante de su companero George Russell (238). Lewis Hamilton suma 229, Verstappen 221, Charles Leclerc 215 y Lando Norris 201. En constructores, Mercedes manda con 578 puntos frente a los 444 de Ferrari."
            ]
        },
        "de": {
            "title": "Paddock in Austin eroeffnet: Antonelli haelt 102 Punkte Vorsprung",
            "subtitle": "Noch zwei Tage bis zum Freitagstraining auf dem COTA. Rennen am Sonntag, 25. Oktober um 15:00 Uhr Ortszeit.",
            "excerpt": "Die Formel-1-Teams absolvieren den Track Walk in Austin. Kimi Antonelli fuehrt vor George Russell (340 zu 238). Mercedes liegt 134 Punkte vor Ferrari.",
            "body": [
                "Am Circuit of the Americas herrschte am Mittwoch, 21. Oktober, reges Treiben beim Aufbau der Garagen und den Medienrunden vor dem Grand Prix der USA. Das 1. Freie Training beginnt am Freitag, 23. Oktober, gefolgt vom Qualifying am Samstag und dem 56-Runden-Rennen am Sonntag, 25. Oktober um 15:00 Uhr Ortszeit. Die 5,513 km lange Strecke bietet 20 Kurven und einen 41 Meter hohen Anstieg zu Kurve 1.",
                "Am Mittwoch liefen keine Motoren fuer gezeitete Runden. Die WM-Staende basieren auf dem Singapur-GP, den Max Verstappen von der Pole gewann. Mercedes-Pilot Kimi Antonelli fuehrt mit 340 Punkten und hat 102 Zaehler Vorsprung auf Teamkollege George Russell (238). Lewis Hamilton liegt bei 229, Verstappen bei 221, Charles Leclerc bei 215 und Lando Norris bei 201. Bei den Konstrukteuren fuehrt Mercedes mit 578 vor Ferrari (444)."
            ]
        },
        "it": {
            "title": "Si accende il paddock di Austin: Antonelli conserva 102 punti di margine",
            "subtitle": "Due giorni al via delle libere del venerdi al COTA. Gara domenica 25 ottobre alle 15:00 locali.",
            "excerpt": "I team di Formula 1 completano la ricognizione della pista ad Austin. Kimi Antonelli guida su George Russell per 340 a 238. Mercedes avanti di 134 su Ferrari.",
            "body": [
                "Il Circuit of the Americas ha aperto i battenti con i briefing media e i lavori nei box mercoledi 21 ottobre, a due giorni dall'inizio dell'azione per il Gran Premio degli Stati Uniti. Le Prove Libere 1 scatteranno venerdi 23 ottobre, con qualifiche sabato e gara da 56 giri domenica 25 alle 15:00 locali. Il tracciato di 5,513 km vanta 20 curve e la celebre salita di 41 metri verso curva 1.",
                "Nessun crono registrato nella giornata di mercoledi. La classifica rispecchia l'esito di Singapore, dove Max Verstappen ha vinto partendo dalla pole. Kimi Antonelli guida il mondiale con 340 punti, 102 in piu rispetto a George Russell (238). Lewis Hamilton segue a 229, Verstappen a 221, Charles Leclerc a 215 e Lando Norris a 201. Tra i costruttori la Mercedes guida con 578 punti contro i 444 della Ferrari."
            ]
        },
        "pl": {
            "title": "Padok w Austin otwarty: Antonelli ma 102 punkty przewagi",
            "subtitle": "Dwa dni do piatkowych treningow na COTA. Wyscig w niedziele 25 pazdziernika o 15:00 czasu lokalnego.",
            "excerpt": "Zespoly F1 zakonczyly obchody toru w Austin. Kimi Antonelli prowadzi przed George'em Russellem (340 do 238). Mercedes ma 134 punkty przewagi nad Ferrari.",
            "body": [
                "Na Circuit of the Americas w srode 21 pazdziernika trwaly przygotowania medialne i montaz garazy przed Grand Prix Stanow Zjednoczonych. Pierwszy trening rusza w piatek 23 pazdziernika, kwalifikacje odbeda sie w sobote, a wyscig na dystansie 56 okrazen w niedziele 25 pazdziernika o 15:00 czasu lokalnego. Nitka toru liczy 5,513 km z 20 zakretami i 41-metrowym wzniesieniem do zakretu 1.",
                "W srode nie prowadzono jazd pomiarowych. Klasyfikacja generalna odzwierciedla wyniki z Singapuru, gdzie Max Verstappen triumfowal z pole position. Kimi Antonelli prowadzi w mistrzostwach z dorobkiem 340 punktow, wyprzedzajac George'a Russella (238) o 102 punkty. Lewis Hamilton ma 229, Verstappen 221, Charles Leclerc 215, a Lando Norris 201 punktow. W klasyfikacji konstruktorow Mercedes prowadzi z 578 punktami przed Ferrari (444)."
            ]
        },
        "zh": {
            "title": "奥斯汀围场揭幕：安东内利手握102分领先优势",
            "subtitle": "距美洲赛道周五练习赛仅剩两天。正赛于10月25日周日当地时间15:00打响。",
            "excerpt": "F1车队在奥斯汀进行赛道踏勘。基米·安东内利以340分对238分领跑拉塞尔。梅赛德斯领先法拉利134分。",
            "body": [
                "10月21日周三，美洲赛道开展了媒体通气会与车房搭建工作，距离美国大奖赛揭幕还有整整两天。一练将于10月23日周五打响，周六进行排位赛，周日当地时间15:00展开56圈正赛角逐。全长5.513公里的赛道拥有20个弯角，1号弯具有标志性的41米海拔爬升。",
                "周三并无赛车上场计时。积分榜依然保持新加坡站后的格局，维斯塔潘在滨海湾杆位发车夺冠。梅赛德斯年轻车手安东内利以340分领跑车手榜，领先队友拉塞尔（238分）达102分。汉密尔顿积229分位列第三，维斯塔潘221分，勒克莱尔215分，诺里斯201分。车队积分榜上，梅赛德斯积578分，领先444分的法拉利134分。"
            ]
        },
        "ja": {
            "title": "オースティンのパドックが始動：アントネッリが102点リードを保持",
            "subtitle": "COTAでの金曜フリー走行まであと2日。決勝は10月25日日曜の現地15:00スタート。",
            "excerpt": "F1各チームがオースティンでトラックウォークを実施。キミ・アントネッリがラッセルを340点対238点でリード。メルセデスはフェラーリに134点差。",
            "body": [
                "サーキット・オブ・ジ・アメリカズでは10月21日水曜、アメリカGP開幕に向けてメディア対応やガレージ設営が進められました。金曜23日にフリー走行1回目が始まり、土曜の予選を経て、25日日曜の現地15:00に56周の決勝を迎えます。全長5.513kmのコースは20のコーナーとターン1への41mの高低差が特徴です。",
                "水曜日に走行セッションはなくタイムもありません。ドライバーズ選手権はフェルスタッペンがポール・トゥ・ウィンを飾ったシンガポールGPの結果がそのまま反映されています。メルセデスのキミ・アントネッリが340点で首位を守り、ジョージ・ラッセル（238点）に102点差をつけています。ハミルトン229点、フェルスタッペン221点、ルクレール215点、ノリス201点。コンストラクターズではメルセデスが578点でフェラーリ（444点）を大きくリードしています。"
            ]
        },
        "ko": {
            "title": "오스틴 패덕 오픈: 안토넬리, 102점 차 리드 유지",
            "subtitle": "COTA 금요 연습 주행까지 이틀 남음. 결승은 10월 25일 일요일 현지 15:00.",
            "excerpt": "F1 팀들이 오스틴에서 트랙 워크를 진행했습니다. 키미 안토넬리가 러셀을 340점 대 238점으로 앞서 있습니다. 메르세데스는 페라리에 134점 차 선두.",
            "body": [
                "10월 21일 수요일 서킷 오브 디 아메리카스에서 미국 그랑프리 개막을 앞두고 미디어 브리핑과 피트 세팅이 한창 진행되었습니다. 금요일 23일 연습 주행 1세션을 시작으로 토요일 예선, 일요일 현지 오후 3시 56랩 결승 레이스가 펼쳐집니다. 5.513km 트랙은 20개 코너와 턴 1로 향하는 41미터의 오르막 구간이 특징입니다.",
                "수요일에는 공식 주행 기록이 없습니다. 드라이버 순위는 베르스타펜이 폴투윈을 거둔 싱가포르 GP 결과를 따르고 있습니다. 메르세데스의 키미 안토넬리가 340점으로 팀 동료 조지 러셀(238점)에 102점 차 리드를 지키고 있습니다. 해밀턴이 229점, 베르스타펜 221점, 르클레르 215점, 노리스 201점 순입니다. 컨스트럭터 부문에서는 메르세데스가 578점으로 페라리(444점)를 134점 차로 앞서고 있습니다."
            ]
        },
        "ar": {
            "title": "افتتاح بادوك اوستن: انتونيللي يحتفظ بفارق 102 نقطة في الصدارة",
            "subtitle": "يومان على انطلاق تجارب الجمعة في حلبة الامريكتين. السباق الاحد 25 اكتوبر الساعة 15:00 بالتوقيت المحلي.",
            "excerpt": "تكمل فرق الفورمولا 1 فحص المسار في اوستن. كيمي انتونيللي يتصدر امام جورج راسل (340 مقابل 238). مرسيدس تتفوق بـ134 نقطة على فيراري.",
            "body": [
                "شهدت حلبة الامريكتين يوم الاربعاء 21 اكتوبر اجتماعات اعلامية وتجهيز المرائب قبل يومين من انطلاق جائزة الولايات المتحدة الكبرى. تبدا التجارب الحرة الاولى الجمعة 23 اكتوبر، تليها التجارب التأهيلية السبت والسباق الرئيسي المكون من 56 لفة الاحد في الساعة 15:00 بالتوقيت المحلي. يبلغ طول المسار 5.513 كم مع 20 منعطفا وصعود بارتفاع 41 مترا نحو المنعطف الاول.",
                "لم تدور اي محركات لتسجيل ازمنة يوم الاربعاء. يعكس الترتيب نتائج سنغافورة حيث فاز فيرستابن من مركز الانطلاق الاول. يقود كيمي انتونيللي بطولة السائقين بـ340 نقطة متقدما بفارق 102 نقطة على زميله جورج راسل (238). يملك هاميلتون 229 وفيرستابن 221 ولوكلير 215 ونوريس 201 نقطة. وفي بطولة الصانعين، تتصدر مرسيدس بـ578 نقطة متقدمة بـ134 نقطة على فيراري (444)."
            ]
        }
    }
}

# Verify no em-dash or double-hyphen
for slug, langs in OCT21_STORIES.items():
    for lang, trans in langs.items():
        for field, val in trans.items():
            if isinstance(val, str):
                assert "—" not in val, f"Em-dash in {slug} {lang} {field}"
                assert "--" not in val, f"Double-hyphen in {slug} {lang} {field}"
            elif isinstance(val, list):
                for i, item in enumerate(val):
                    assert "—" not in item, f"Em-dash in {slug} {lang} {field}[{i}]"
                    assert "--" not in item, f"Double-hyphen in {slug} {lang} {field}[{i}]"

print("Verification passed! No em-dashes or double-hyphens.")

# Generate code snippet to insert into stories.ts
snippet_parts = []
for slug, langs in OCT21_STORIES.items():
    formatted_slug = json.dumps(slug)
    snippet_parts.append(f"{formatted_slug}: {json.dumps(langs, ensure_ascii=False, indent=2)},")

snippet = "\n".join(snippet_parts) + "\n"

# Read frontend/src/i18n/stories.ts
stories_file = "frontend/src/i18n/stories.ts"
with open(stories_file, "r", encoding="utf-8") as f:
    content = f.read()

target = "export const STORY_I18N: Record<string, LocMap> = {\n"
assert target in content, "Target line not found in stories.ts"

new_content = content.replace(target, target + snippet, 1)

with open(stories_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully injected translations into frontend/src/i18n/stories.ts")
