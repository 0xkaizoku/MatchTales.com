# -*- coding: utf-8 -*-
"""
Add 31 October 2026 translations for all 6 stories across 9 languages.
"""
import json
import re
import os

OCT31_STORIES = {
    "premier-league-mw9-arsenal-liverpool-emirates-thriller-2026": {
        "fr": {
            "title": "Premier League J9 : Arsenal et Liverpool se neutralisent 2-2 dans un choc au sommet a l'Emirates",
            "subtitle": "Saka et Merino frappent pour les Gunners avant l'egalisation de Mohamed Salah a la 81e minute pour les Reds.",
            "excerpt": "Arsenal et Liverpool ont livre un duel intense conclu sur un score de 2-2 a Londres, laissant Manchester City seul leader.",
            "body": [
                "La course au titre en Premier League a offert un spectacle grandiose ce samedi 31 octobre a l'Emirates Stadium. Arsenal et Liverpool se sont quittes sur un match nul palpitant de 2-2 devant plus de 60 000 spectateurs.",
                "Bukayo Saka a ouvert le score des la 9e minute d'une frappe splendide au premier poteau, avant que Virgil van Dijk n'egalise sur corner. Mikel Merino a redonne l'avantage aux Gunners avant la pause de la tete, mais Mohamed Salah a surgi a la 81e minute sur un centre de Nunez pour arracher le point du match nul. Ce resultat laisse Manchester City seul en tete avec 23 points."
            ]
        },
        "es": {
            "title": "Premier League J9: Arsenal y Liverpool firman tablas 2-2 en un partidazo trepidante en el Emirates",
            "subtitle": "Saka y Merino adelantaron a los Gunners antes de que Mohamed Salah empatara en el minuto 81 para los de Arne Slot.",
            "excerpt": "Arsenal y Liverpool empataron 2-2 en el Emirates Stadium este sabado, permitiendo que el Manchester City quede como lider solitario.",
            "body": [
                "El campeonato ingles vivio otra tarde magica este sabado 31 de octubre en Londres. Arsenal y Liverpool empataron 2-2 en un duelo de enorme nivel competitivo y ritmo incesante.",
                "Bukayo Saka desato la locura local en el minuto 9 con un zurdazo imparable, neutralizado por Virgil van Dijk poco despues. Mikel Merino firmo su primer gol con el Arsenal al cabecear una falta servida por Rice antes del descanso, pero Mohamed Salah igualo el choque en el minuto 81 tras una gran asistencia de Darwin Nunez. El Manchester City aprovecha el empate para tomar el liderato en solitario."
            ]
        },
        "de": {
            "title": "Premier League 9. Spieltag: Arsenal und Liverpool trennen sich 2:2 im packenden Spitzenspiel",
            "subtitle": "Saka und Merino treffen fuer die Gunners, ehe Mohamed Salah in der 81. Minute den Punkt fuer die Reds rettet.",
            "excerpt": "Arsenal und Liverpool teilten sich am Samstag beim 2:2 im Emirates Stadium die Punkte, wodurch Man City die alleinige Tabellensfuehrung uebernimmt.",
            "body": [
                "Das Duell der Meisterschaftsaspiranten hielt am Samstag, den 31. Oktober, alles, was es versprach. Im Emirates Stadium trennten sich Arsenal und Liverpool nach 90 packenden Minuten mit einem leistungsgerechten 2:2-Unentschieden.",
                "Bukayo Saka brachte Arsenal frueh in Fuehrung, van Dijk glich per Kopf aus. Mikel Merino stellte vor der Halbzeit auf 2:1, doch Mohamed Salah traf in der 81. Minute zum Endstand. Manchester City steht nach dem 1:0 ueber Southampton nun mit 23 Punkten allein an der Tabellenspitze."
            ]
        },
        "it": {
            "title": "Premier League 9ª giornata: Arsenal e Liverpool spettacolo ed equilibrio, finisce 2-2 all'Emirates",
            "subtitle": "Saka e Merino firmano il doppio vantaggio per i Gunners, ma all'81' Mohamed Salah fissa il pareggio per i Reds.",
            "excerpt": "Arsenal e Liverpool pareggiano 2-2 in una sfida ad altissima intensita a Londra: ne approfitta il Manchester City, ora capolista solitario.",
            "body": [
                "Emozioni a non finire a Londra sabato 31 ottobre. Arsenal e Liverpool hanno pareggiato 2-2 in una battaglia tattica e spettacolare davanti a 60.383 spettatori all'Emirates Stadium.",
                "Saka ha sbloccato la gara al 9', ripreso dalla deviazione aerea di Van Dijk. Merino ha riportato avanti i londinesi di testa al 43', ma nel finale Salah ha firmato il pareggio capitalizzando l'assist di Nunez. Il Manchester City scappa a quota 23 punti, con l'Arsenal a 22 e il Liverpool a 16."
            ]
        },
        "pl": {
            "title": "Premier League 9. kolejka: Arsenal i Liverpool na remis 2:2 w wielkim hicie na Emirates",
            "subtitle": "Gole Saki i Merino dla Kanonierow; Mohamed Salah wyrownuje w 81. minucie dla ekipy Arne Slota.",
            "excerpt": "Arsenal i Liverpool zremisowaly 2:2 w elektryzujacym starciu na szczycie ligi angielskiej, zostawiajac Manchester City na czele tabeli.",
            "body": [
                "Sobotni szlagier Premier League na Emirates Stadium przyniosl kibicom wielkie emocje. Arsenal dwukrotnie prowadzil z Liverpoolem, ale spotkanie zakonczylo sie sprawiedliwym podzialem punktow 2:2.",
                "Bukayo Saka trafil juz w 9. minucie, po czym wyrownal Virgil van Dijk. Przed przerwa Mikel Merino strzelil debiutanckiego gola glowa dla gospodarzy. W koncowce punkt Liverpoolowi uratowal niezawodny Mohamed Salah, wykorzystujac podanie Darwina Nuneza."
            ]
        },
        "zh": {
            "title": "英超第9轮焦点战：阿森纳2-2战平利物浦，萨拉赫终场前破门救主",
            "subtitle": "萨卡、梅里诺先后破门助枪手两度领先，萨拉赫第81分钟扳平比分；曼城登顶积分榜。",
            "excerpt": "阿森纳与利物浦周六在酋长球场上演精彩对决，双方2-2握手言言和，曼城趁机占据英超榜首位置。",
            "body": [
                "10月31日周六傍晚，英超第9轮天王山之战在酋长球场打响，阿森纳与利物浦联袂奉献了一场荡气回肠的2-2平局，6万余名现场观众见证了这场高水平较量。",
                "萨卡第9分钟精彩内切破门首开纪录，范戴克随后头球扳平。半场结束前梅里诺冲顶破门收获枪手生涯首球。下半场阿森纳后防遭遇伤病，萨拉赫在第81分钟接努涅斯横传推射破门扳平。本轮战罢，曼城积23分独占积分榜首，阿森纳22分紧随其后。"
            ]
        },
        "ja": {
            "title": "プレミアリーグ第9節：アーセナルとリヴァプールがエミレーツで激闘2-2のドロー",
            "subtitle": "サカとメリーノの得点で優位に立つも、81分にサラーが同点弾をマーク；マンCが単独首位浮上。",
            "excerpt": "首位攻防のビッグマッチはアーセナルとリヴァプールが2-2で引き分け、マンチェスター・シティが単独首位に立ちました。",
            "body": [
                "10月31日土曜日、エミレーツ・スタジアムで行われたプレミアリーグ第9節の天王山は、アーセナルとリヴァプールが意地をぶつけ合い2-2の引き分けに終わりました。",
                "サカの鮮やかなゴールで先制したアーセナルは、ファン・ダイクに同点とされるも前半終了間際にメリーノのヘディングで勝ち越し。しかし後半負傷者を出した隙を突かれ、81分にサラーの決定力で追いつかれました。この結果、サウサンプトンを下したマンチェスター・シティが単独首位に浮上しました。"
            ]
        },
        "ko": {
            "title": "프리미어리그 9R: 아스널과 리버풀, 에미레이츠서 2-2 명승부 끝 무승부",
            "subtitle": "사카-메리노 연속골로 앞서간 아스널, 살라가 81분 극적 동점골 작렬; 맨시티 단독 선두.",
            "excerpt": "아스널과 리버풀이 런던에서 열린 프리미어리그 9라운드에서 2-2 무승부를 기록하며 승점 1점씩을 나눠가졌습니다.",
            "body": [
                "10월 31일 토요일 에미레이츠 스타디움에서 열린 2026-27 프리미어리그 9라운드 맞대결에서 아스널과 리버풀이 2-2로 비겼습니다.",
                "사카의 원더골과 메리노의 헤더골로 아스널이 리드를 잡았으나, 리버풀은 반다이크의 만회골에 이어 81분 살라의 침착한 마무리로 균형을 맞췄습니다. 이로써 사우샘프턴을 꺾은 맨체스터 시티(승점 23)가 리그 단독 선두로 올라섰습니다."
            ]
        },
        "ar": {
            "title": "الدوري الإنجليزي الجولة 9: أرسنال وليفربول يقتسمان النقاط في قمة نارية انتهت 2-2 بملعب الإمارات",
            "subtitle": "ساكا وميرينو يمنحان التقدم للغانرز ومحمد صلاح يسجل هدف التعادل القاتل في الدقيقة 81 للريدز.",
            "excerpt": "انتهت قمة الجولة التاسعة من الدوري الإنجليزي الممتاز بين أرسنال وليفربول بالتعادل الإيجابي 2-2 في لندن.",
            "body": [
                "قدم أرسنال وليفربول وجبة كروية دسمة مساء السبت 31 أكتوبر على ملعب الإمارات في قمة الجولة التاسعة التي انتهت بالتعادل 2-2 أمام أكثر من 60 ألف مشجع.",
                "سجل بوكايو ساكا وميكيل ميرينو هدفي أرسنال، في حين تكفل فيرجيل فان دايك ومحمد صلاح بهدفي ليفربول، حيث جاء هدف صلاح في الدقيقة 81 ليحرم المدفعجية من الصدارة التي انفرد بها مانشستر سيتي برصيد 23 نقطة."
            ]
        }
    },
    "atp-vienna-2026-alcaraz-defeats-zverev-advances-to-final": {
        "fr": {
            "title": "Tournoi de Vienne demi-finale : Carlos Alcaraz domine Alexander Zverev et file en finale",
            "subtitle": "Le numero un mondial sauve toutes les balles de break et s'impose 6-4, 7-6 dans la capitale autrichienne.",
            "excerpt": "Carlos Alcaraz a livre une demonstration de solidite pour ecarter Alexander Zverev 6-4, 7-6 et rejoindre la finale a Vienne.",
            "body": [
                "Carlos Alcaraz a composte avec autorite son billet pour la finale du tournoi ATP 500 de Vienne ce samedi 31 octobre en venant a bout d'Alexander Zverev sur le score de 6-4, 7-6 (5).",
                "Le prodige espagnol s'est montre intouchable au service, remportant 84 % des points derriere sa premiere balle et ecartant les trois occasions de break du joueur allemand. Dans un tie-break irrespirable au deuxieme set, Alcaraz a fait la difference grace a un passing supersonique et un amorti millimetre pour signer sa 62e victoire de l'annee 2026."
            ]
        },
        "es": {
            "title": "ATP Viena semifinales: Carlos Alcaraz supera a Alexander Zverev y accede a la gran final",
            "subtitle": "El murciano no cede su saque en todo el partido y firma un 6-4, 7-6 de enorme jerarquia para buscar su sexto titulo del ano.",
            "excerpt": "Carlos Alcaraz doblego este sabado a Alexander Zverev por 6-4 y 7-6 (5) en Viena y disputara este domingo su novena final del curso 2026.",
            "body": [
                "Carlos Alcaraz brillo con luz propia este sabado 31 de octubre en el Wiener Stadthalle al derrotar a Alexander Zverev por 6-4 y 7-6 (5) en una exhibicion de madurez y sangre fria.",
                "El tenista espanol firmo 34 golpes ganadores y no concedio ni un solo quiebre de saque en una hora y 48 minutos de juego. En el desempate del segundo parcial, dos golpes magistrales en carrera inclinaron la balanza para meterle en la gran final del domingo sin haber perdido un solo set en toda la semana."
            ]
        },
        "de": {
            "title": "Erste Bank Open Halbfinale: Carlos Alcaraz besiegt Alexander Zverev und zieht ins Finale ein",
            "subtitle": "Weltranglistenerster bleibt beim 6:4, 7:6 ohne Aufschlagverlust und fordert am Sonntag den Titel in Wien.",
            "excerpt": "Carlos Alcaraz hat das mit Spannung erwartete Halbfinale der Erste Bank Open gegen Alexander Zverev in zwei Saetzen fuer sich entschieden.",
            "body": [
                "Der topgesetzte Spanier Carlos Alcaraz bot am Samstag, den 31. Oktober, vor 9.800 Zuschauern in der Wiener Stadthalle Tennis der Spitzenklasse und bezwang Alexander Zverev mit 6:4, 7:6 (5).",
                "Alcaraz servierte herausragend und wehrte alle drei Breakbaelle des Deutschen souveran ab. Im entscheidenden Tiebreak des zweiten Satzes drehte der 23-Jaehrige mit einem spektakulaeren Passierball und einem Stoppball die Partie zu seinen Gunsten und feierte seinen 62. Matchgewinn der Saison 2026."
            ]
        },
        "it": {
            "title": "ATP Vienna semifinale: Carlos Alcaraz supera Alexander Zverev 6-4, 7-6 e vola in finale",
            "subtitle": "Lo spagnolo non concede break e domina i punti chiave al tie-break guadagnando la nona finale del 2026.",
            "excerpt": "Carlos Alcaraz vince una sfida stellare contro Alexander Zverev e conquista la finale dell'Erste Bank Open di Vienna.",
            "body": [
                "Spettacolo puro a Vienna nella semifinale dell'Erste Bank Open. Carlos Alcaraz ha sconfitto Alexander Zverev con il punteggio di 6-4, 7-6 (5) al termine di una sfida serratissima durata un'ora e 48 minuti.",
                "Il numero uno del mondo ha blindato la battuta con l'84% di punti vinti con la prima palla, annullando tutte le palle break concesse. Nel tie-break del secondo set Alcaraz ha tirato fuori dal cilindro due colpi sensazionali per chiudere i conti e prepararsi alla finale di domenica."
            ]
        },
        "pl": {
            "title": "ATP Wieden polfinal: Carlos Alcaraz pokonuje Alexandra Zvereva 6:4, 7:6 i melduje sie w finale",
            "subtitle": "Hiszpan nie stracil wlasnego podania przez cale spotkanie i wygral kluczowe pilki w tie-breaku drugiego seta.",
            "excerpt": "Carlos Alcaraz awansowal do niedzielnego finalu turnieju w Wiedniu po znakomitym zwyciestwie nad Alexandrem Zverevem.",
            "body": [
                "Lider swiatowego rankingu Carlos Alcaraz zaprezentowal w sobote 31 pazdziernika forme najwyzszej proby, pokonujac w polfinale w Wiedniu Alexandra Zvereva 6:4, 7:6 (5).",
                "Hiszpan zaserwowal bezblednie, nie oddajac ani jednego gema przy wlasnym podaniu. W tie-breaku popisal sie genialnym passing-shotem w pelnym biegu, pieczetujac swoj awans do dziewiatego finalu w sezonie 2026."
            ]
        },
        "zh": {
            "title": "ATP维也纳站半决赛：阿尔卡拉斯双抢直落两盘力克兹维列夫，昂首挺进争冠战",
            "subtitle": "世界第一一发得分率高达84%且未丢一个发球局，以6-4、7-6挺进今年第9个巡回赛决赛。",
            "excerpt": "阿尔卡拉斯在周六的维也纳半决赛中以6-4、7-6(5)战胜兹维列夫，保持一盘未失的强劲势头杀入决赛。",
            "body": [
                "10月31日周六，维也纳斯塔德哈勒体育馆见证了一场高水准强强对话。头号种子阿尔卡拉斯凭借无懈可击的发球与全场攻防，耗时1小时48分钟以6-4、7-6(5)击败3号种子兹维列夫闯入决赛。",
                "西班牙人全场打出34记制胜分并化解了全部3个破发点。第二盘抢七决胜中，阿尔卡拉斯在落后情况下凭借两记不可思议的跑动正手制胜分逆转战局，拿下本赛季个人第62场单打胜利。"
            ]
        },
        "ja": {
            "title": "ATPウィーン準決勝：アルカラスがズベレフを6-4、7-6で破り決勝進出",
            "subtitle": "世界王者アルカラスがブレークポイントをすべてセーブし、ストレート勝ちで今季9度目のツアー決勝へ。",
            "excerpt": "アルカラスは土曜日のウィーン準決勝でズベレフとの激闘を制し、セットを失うことなく決勝進出を決めました。",
            "body": [
                "10月31日土曜日、エルステ・バンク・オープン準決勝でカルロス・アルカラスがアレクサンダー・ズベレフを6-4、7-6(5)で退け、日曜日に行われる決勝へ駒を進めました。",
                "アルカラスはファーストサーブ時のポイント獲得率84％をマークし、3度のブレークのピンチをすべてしのぐ鉄壁のプレーを披露。緊迫した第2セットのタイブレークでも勝負強いパッシングショットを決め、今季62勝目をマークしました。"
            ]
        },
        "ko": {
            "title": "ATP 빈 준결승: 알카라스, 즈베레프 6-4 7-6 꺾고 결승 안착",
            "subtitle": "서브 게임을 단 한 번도 내주지 않은 완벽한 플레이로 시즌 9번째 투어 결승행 확정.",
            "excerpt": "카를로스 알카라스가 토요일 빈 오픈 준결승에서 알렉산더 즈베레프를 2-0으로 제압하고 우승 도전에 나섭니다.",
            "body": [
                "10월 31일 토요일 오스트리아 빈에서 열린 ATP 500 준결승에서 세계 1위 카를로스 알카라스가 알렉산더 즈베레프를 6-4, 7-6(5)으로 따돌리고 결승에 진출했습니다.",
                "알카라스는 34개의 위너를 작렬하며 즈베레프의 서브 공세를 견뎌냈고, 위기 때마다 강력한 포핸드로 브레이크 포인트를 모두 방어했습니다. 2세트 타이브레이크 4-4에서 환상적인 드롭샷을 터뜨리며 올 시즌 62번째 승리를 수확했습니다."
            ]
        },
        "ar": {
            "title": "بطولة فيينا للتنس نصف النهائي: كارلوس ألكاراز يهزم ألكسندر زفيريف 6-4 و7-6 ويتأهل للنهائي",
            "subtitle": "المصنف الأول عالميا يحافظ على إرساله كاملا ويسدد 34 ضربة قاضية ليتأهل للنهائي التاسع له في 2026.",
            "excerpt": "تأهل الإسباني كارلوس ألكاراز إلى نهائي بطولة فيينا المفتوحة بعد فوزه المثير بمجموعتين على الألماني ألكسندر زفيريف.",
            "body": [
                "قدم النجم الإسباني كارلوس ألكاراز عرضا مبهرا يوم السبت 31 أكتوبر في نصف نهائي بطولة فيينا الدولية ليتفوق على غريمه ألكسندر زفيريف بنتيجة 6-4 و7-6 (5) في مباراة استغرقت ساعة و48 دقيقة.",
                "وحافظ ألكاراز على سجله نظيفا دون خسارة أي مجموعة في البطولة هذا الأسبوع، حيث أنقذ نقاط الكسر الثلاث التي واجهها ووجه ضربات حاسمة في الشوط الفاصل ليحقق فوزه الثاني والستين في موسم 2026."
            ]
        }
    },
    "f1-mexico-city-gp-2026-qualifying-antonelli-storms-to-pole": {
        "fr": {
            "title": "GP du Mexique qualifications : Kimi Antonelli s'offre la pole et touche le titre mondial du doigt",
            "subtitle": "Le rookie de Mercedes signe un tour d'anthologie en 1:16.892 devant Charles Leclerc et Max Verstappen a Mexico.",
            "excerpt": "Kimi Antonelli partira en pole position dimanche a Mexico, lui qui n'a besoin que d'une neuvieme place pour devenir champion du monde.",
            "body": [
                "Le prodige italien Kimi Antonelli a marque les esprits ce samedi 31 octobre lors des qualifications du Grand Prix de Mexico a l'Autodromo Hermanos Rodriguez. Avec un tour stratospherique boucle en 1:16.892, le pilote Mercedes de 20 ans a decroche la quatrieme pole position de sa jeune carriere.",
                "Sous les vivats du stade Foro Sol, Antonelli a devance Charles Leclerc de 76 milliemes et Max Verstappen de 142 milliemes. Fort de ses 365 points au championnat, une 9e place dimanche suffira a Antonelli pour devenir le plus jeune champion du monde de l'histoire de la F1."
            ]
        },
        "es": {
            "title": "Clasificacion GP de Mexico: Kimi Antonelli vuela hacia la pole y roza la corona mundial de F1",
            "subtitle": "El novato de Mercedes marca 1:16.892 a 2.285 metros de altitud superando por 76 milesimas a Charles Leclerc.",
            "excerpt": "Kimi Antonelli consiguio la pole position en el Autodromo Hermanos Rodriguez y solo necesita ser noveno el domingo para ser campeon.",
            "body": [
                "Kimi Antonelli dio un paso gigante hacia la historia este sabado 31 de octubre en el Gran Premio de la Ciudad de Mexico. Al volante de su Mercedes, el italiano registro un tiempo de 1:16.892 en su ultimo intento de la Q3 para llevarse la pole ante el delirio de la aficion mexicana.",
                "Antonelli aventajo por escasas milesimas al Ferrari de Charles Leclerc y al Red Bull de Max Verstappen. El piloto de Mercedes, que lidera el Mundial con 365 puntos, acaricia el titulo ya que le basta con finalizar entre los nueve primeros en la carrera del domingo para proclamarse campeon del mundo."
            ]
        },
        "de": {
            "title": "Formel 1 Mexiko Qualifying: Kimi Antonelli stuermt zur Pole und greift nach der WM-Krone",
            "subtitle": "Mercedes-Youngster setzt mit 1:16,892 Min. Bestzeit vor Leclerc und Verstappen; P9 am Sonntag reicht zum Titel.",
            "excerpt": "Kimi Antonelli hat sich beim Grand Prix von Mexiko die Pole Position gesichert und steht vor dem Gewinn der Formel-1-Weltmeisterschaft 2026.",
            "body": [
                "Der 20-jaehrige Kimi Antonelli stellte am Samstag, den 31. Oktober, auf dem Autodromo Hermanos Rodriguez seine Klasse unter Beweis. In der Hoehenluft von Mexiko-Stadt sicherte sich der Mercedes-Pilot mit einer Rundenzeit von 1:16,892 Minuten die Pole Position.",
                "Antonelli verwies Charles Leclerc um 0,076 Sekunden und Max Verstappen um 0,142 Sekunden auf die Plaetze zwei und drei. Belegt Antonelli im Grand Prix am Sonntag mindestens Rang neun, kroent er sich zum juengsten Formel-1-Weltmeister aller Zeiten."
            ]
        },
        "it": {
            "title": "Qualifiche GP Messico: Kimi Antonelli da leggenda, pole d'autore a un passo dal titolo mondiale",
            "subtitle": "Il fenomeno della Mercedes ferma il cronometro a 1:16.892 battendo Leclerc di 76 millesimi; domenica basta un 9° posto.",
            "excerpt": "Kimi Antonelli firma la pole position a Citta del Messico e vede il titolo iridato a portata di mano in vista della gara di domenica.",
            "body": [
                "Capolavoro assoluto di Kimi Antonelli sabato 31 ottobre all'Autodromo Hermanos Rodriguez. Il ventenne pilota della Mercedes ha conquistato la pole position del Gran Premio del Messico con un giro fenomenale da 1:16.892 nella Q3.",
                "Antonelli ha preceduto per appena 76 millesimi la Ferrari di Charles Leclerc e la Red Bull di Max Verstappen. Con 123 punti di vantaggio in classifica, al bolognese bastera un nono posto nella gara di domenica per laurearsi campione del mondo di Formula 1 piu giovane della storia."
            ]
        },
        "pl": {
            "title": "Kwalifikacje GP Meksyku: Kimi Antonelli zdobywa pole position i jest o krok od mistrzostwa swiata",
            "subtitle": "Kierowca Mercedesa wykrecil fantastyczny czas 1:16.892, wyprzedzajac Leclerca o zaledwie 0,076 sekundy.",
            "excerpt": "Kimi Antonelli wystartuje z pierwszego pola do niedzielnego GP Meksyku, potrzebujac zaledwie 9. miejsca do zdobycia tytulu.",
            "body": [
                "Kimi Antonelli zrobil w sobote 31 pazdziernika decydujacy krok w strone tytulu mistrza swiata Formuly 1. Wloski debiutant za kierownica Mercedesa wygral kwalifikacje w Meksyku z czasem 1:16.892.",
                "Mlodzieniec wyprzedzil Charlesa Leclerca z Ferrari o 0,076 s oraz Maxa Verstappena o 0,142 s. Dziewiate miejsce w niedzielnym wyscigu zagwarantuje Antonellemu historyczny triumf i tytul najmlodszego mistrza swiata w dziejach F1."
            ]
        },
        "zh": {
            "title": "F1墨西哥大奖赛排位赛：安东内利力压勒克莱尔夺杆位，加冕世界冠军近在咫尺",
            "subtitle": "梅赛德斯超新星跑出1分16秒892全场最快圈速；周日正赛只需前九即可提前锁定年度车手总冠军。",
            "excerpt": "安东内利在墨西哥城罗德里格斯赛道摘得个人生涯第四个杆位，距离2026年F1世界冠军仅一步之遥。",
            "body": [
                "10月31日周六，F1墨西哥大奖赛排位赛在海拔2285米的高原赛道激烈打响。年仅20岁的梅赛德斯新星基米·安东内利在Q3最后时刻飙出1分16秒892的惊艳圈速夺得杆位。",
                "法拉利车手勒克莱尔以0.076秒的微弱劣势屈居次席，维斯塔潘落后0.142秒名列第三。手握巨大积分优势的安东内利只需在周日正赛中取得第9名或更高名次，便将刷新维特尔的纪录成为F1历史上最年轻的世界冠军。"
            ]
        },
        "ja": {
            "title": "F1メキシコGP予選：アントネッリが圧巻のポールポジション獲得、ワールドチャンピオン王手",
            "subtitle": "メルセデスの20歳新星が1分16秒892を記録しルクレールを撃破；日曜決勝で9位以内なら王座決定。",
            "excerpt": "キミ・アントネッリがメキシコGPの予選を制してポールポジションを獲得し、悲願の年間王者獲得に大きく前進しました。",
            "body": [
                "10月31日土曜日、エルマノス・ロドリゲス・サーキットで行われたF1メキシコGP予選で、メルセデスのキミ・アントネッリが1分16秒892の驚異的なタイムをマークしてポールポジションを獲得しました。",
                "フェラーリのルクレールをわずか0.076秒差、レッドブルのフェルスタッペンを0.142秒差で抑え込んだアントネッリ。日曜日の決勝レースで9位以内に入れば、F1史上最年少でのワールドチャンピオン戴冠が決まります。"
            ]
        },
        "ko": {
            "title": "F1 멕시코 GP 예선: 키미 안토넬리 폴포지션 차지, 월드 챔피언 등극 초읽기",
            "subtitle": "메르세데스 20세 괴물 신예, 1분16초892로 르클레르 제치고 1위; 일요일 본선 9위 이상이면 우승 확정.",
            "excerpt": "키미 안토넬리가 멕시코시티에서 드라마틱한 폴포지션을 획득하며 F1 최연소 챔피언 등극에 단 한 걸음만을 남겨뒀습니다.",
            "body": [
                "10월 31일 토요일 멕시코시티 엘마노스 로드리게스 서킷에서 열린 F1 멕시코 GP 예선에서 메르세데스의 키미 안토넬리가 1분16초892로 당당히 폴포지션을 거머쥐었습니다.",
                "안토넬리는 페라리의 샤를 르클레르를 0.076초 차로 제치며 스타디움 관중들의 뜨거운 환호를 받았습니다. 챔피언십 선두를 질주 중인 안토넬리는 일요일 71랩 레이스에서 9위 이내로 완주하기만 하면 자력으로 2026년 세계 챔피언에 오르게 됩니다."
            ]
        },
        "ar": {
            "title": "تجارب جائزة المكسيك الكبرى: كيمي أنتونيللي يخطف مركز الانطلاق الأول ويقترب من لقب بطولة العالم",
            "subtitle": "سائق مرسيدس الإيطالي يسجل 1:16.892 متقدما على لوكلير وفرستابن؛ والمركز التاسع يكفيه للتتويج يوم الأحد.",
            "excerpt": "حسم الإيطالي الشاب كيمي أنتونيللي مركز الانطلاق الأول لسباق جائزة المكسيك الكبرى للفورمولا 1 ليصبح على أعتاب اللقب العالمي.",
            "body": [
                "حقق السائق الإيطالي الصاعد كيمي أنتونيللي إنجازا استثنائيا يوم السبت 31 أكتوبر على حلبة هيرمانوس رودريغيز بتسجيله أسرع لفة في التجارب التأهيلية بزمن 1:16.892 لينتزع قطب الانطلاق الأول لجائزة المكسيك الكبرى.",
                "وتفوق سائق مرسيدس بفارق 76 جزءا من الألف من الثانية على شارل لوكلير وبفارق 142 جزءا على ماكس فرستابن. ويحتاج أنتونيللي إلى إنهاء سباق الأحد في المركز التاسع أو أفضل ليضمن رسميا التتويج بلقب بطولة العالم لعام 2026 كأصغر بطل في تاريخ المسابقة."
            ]
        }
    },
    "pga-tour-mexico-open-2026-round3-smotherman-pereda-final-round-showdown": {
        "fr": {
            "title": "PGA Tour VidantaWorld Mexico Open R3 : Smotherman garde la tete d'un coup devant le heros Raul Pereda",
            "subtitle": "L'Americain signe un 69 pour pointer a -13 (200), tandis que le Mexicain flambe avec un 67 avant la finale.",
            "excerpt": "Austin Smotherman mene a -13 a Puerto Vallarta mais Raul Pereda est a un coup pour un dimanche de folie au Mexique.",
            "body": [
                "Austin Smotherman a conserve les commandes du VidantaWorld Mexico Open ce samedi 31 octobre en rendant une carte de 69 (-2) dans le vent pour afficher un total de 13 sous le par (200 coups) apres 54 trous.",
                "Mais la sensation du jour est venue du favori local Raul Pereda. Le joueur de Veracruz a enflamme la foule avec cinq birdies pour une carte de 67 (-4) et s'installe a la deuxieme place a -12. Les deux hommes partageront la derniere partie dimanche dans une ambiance surchauffee."
            ]
        },
        "es": {
            "title": "PGA Tour VidantaWorld Mexico Open R3: Smotherman resiste como lider y Pereda enciende la ilusion mexicana",
            "subtitle": "El estadounidense manda con 13 bajo par (200) pero el veracruzano Raul Pereda firma un 67 y se coloca a un solo golpe.",
            "excerpt": "Austin Smotherman lidera con -13 tras 54 hoyos en VidantaVallarta, pero Raul Pereda acecha a un impacto para la ronda final.",
            "body": [
                "El VidantaWorld Mexico Open vivira un desenlace sonado este domingo. Austin Smotherman aguanto la presion del viento costero el sabado 31 de octubre y firmo un 69 para mantener el liderato con 13 bajo par (200 golpes).",
                "Sin embargo, el protagonista absoluto de la jornada del movimiento fue el mexicano Raul Pereda. El golfista de 29 anos emboco cinco birdies para una tarjeta de 67 golpes (-4), situandose a un solo golpe de la cabeza con -12 y desatando la ilusion de la aficion local por ver ganar a un compatriota."
            ]
        },
        "de": {
            "title": "PGA Tour Mexico Open Runde 3: Smotherman haelt knappe Fuehrung, Lokalmatador Pereda greift an",
            "subtitle": "Bermuda-Sieger fuehrt mit 13 unter Par; Mexikos Raul Pereda begeistert mit einer 67 und liegt nur einen Schlag zurueck.",
            "excerpt": "Austin Smotherman liegt vor der Finalrunde der Mexico Open bei -13 in Fuehrung, dicht gefolgt vom Mexikaner Raul Pereda.",
            "body": [
                "Austin Smotherman zeigte am Samstag, den 31. Oktober, bei windigen Bedingungen auf dem Kurs von VidantaVallarta Nervenstaerke und behauptete mit einer 69 (-2) und insgesamt 13 unter Par (200) die Spitzenposition.",
                "Fuer Jubelstuerme bei den Zuschauern sorgte allerdings Lokalmatador Raul Pereda. Der Mexikaner brillierte mit fuenf Birdies zu einer 67 (-4) und liegt mit 12 unter Par nur einen Zaehler hinter Smotherman, was ein dramatisches Duell am Finalsonntag verspricht."
            ]
        },
        "it": {
            "title": "PGA Tour Mexico Open R3: Smotherman resiste in vetta a -13, Raul Pereda infiamma il pubblico di casa",
            "subtitle": "Il leader americano gira in 69 e guida con 200 colpi; il messicano Pereda risale con un superbo 67 a un colpo dalla vetta.",
            "excerpt": "Austin Smotherman comanda il Mexico Open a quota -13 dopo tre giri, ma Raul Pereda e a un soffio in vista del giro decisivo.",
            "body": [
                "Finale al cardiopalma in vista a Puerto Vallarta. Sabato 31 ottobre Austin Smotherman ha saputo gestire il forte vento pomeridiano chiudendo il terzo giro in 69 colpi (-2) e salendo a un punteggio complessivo di 13 sotto il par (200).",
                "L'eroe del giorno e stato pero il messicano Raul Pereda, capace di realizzare cinque birdie per un eccellente 67 (-4). Con -12 complessivo, Pereda si e garantito un posto nell'ultimo team di domenica assieme a Smotherman, a caccia di uno storico trionfo casalingo."
            ]
        },
        "pl": {
            "title": "PGA Tour Mexico Open runda 3: Smotherman prowadzi z wynikiem -13, Pereda zachwyca meksykanskich fanow",
            "subtitle": "Amerykanin zagral 69 i utrzymal prowadzenie; reprezentant gospodarzy Raul Pereda traci tylko jedno uderzenie po 67.",
            "excerpt": "Austin Smotherman pozostaje liderem turnieju w Meksyku po 54 dolkach z wynikiem 13 ponizej par, goni go Raul Pereda (-12).",
            "body": [
                "Austin Smotherman zachowal zimna krew w wietrznych warunkach na polu VidantaVallarta w sobote 31 pazdziernika, uzyskujac wynik 69 (-2) i utrzymujac prowadzenie po trzech rundach z wynikiem 13 ponizej par (200 uderzen).",
                "Wielka radosc miejscowym kibicom sprawil Raul Pereda, ktory po rundzie z wynikiem 67 (-4) awansowal na drugie miejsce z wynikiem -12. O tytul powalcza w niedziele takze Aaron Rai (-11) i Emiliano Grillo (-10)."
            ]
        },
        "zh": {
            "title": "美巡赛墨西哥公开赛第三轮：斯莫瑟曼-13杆保住榜首，本土英雄佩雷达67杆紧追一杆",
            "subtitle": "百慕大冠军交出69杆守住54洞领先；墨西哥名将佩雷达总成绩-12杆力拼主场历史首冠。",
            "excerpt": "斯莫瑟曼在周六的大风天气中顶住压力以总成绩-13杆领跑，墨西哥本土球员佩雷达落后一杆紧随其后。",
            "body": [
                "10月31日周六在巴亚尔塔港进行的维丹塔世界墨西哥公开赛移动日中，美国选手奥斯汀·斯莫瑟曼交出69杆（-2），以三轮总成绩200杆（-13）守住了单独领先位置。",
                "全场的焦点被本土名将劳尔·佩雷达点燃。29岁的佩雷达单轮抓下5只小鸟交出67杆（-4），总成绩来到-12杆，与斯莫瑟曼仅差一杆，两人将在周日决赛轮展开冠军终极对决。"
            ]
        },
        "ja": {
            "title": "PGAツアー メキシコ・オープン第3日：スモーザーマンが通算13アンダーで首位死守、地元ペレダが1打差追走",
            "subtitle": "強風の中スモーザーマンが69でまとめ首位キープ；メキシコのペレダが67の猛チャージで2位浮上。",
            "excerpt": "オースティン・スモーザーマンが54ホール終了時点で通算13アンダーで首位を維持し、地元ペレダとの最終日直接対決へ。",
            "body": [
                "10月31日土曜日のヴィダンタ・バジャルタは沿岸の風が吹き荒れるタフなコンディションとなりましたが、首位発進のスモーザーマンが69（2アンダー）で回り通算13アンダー（200）で単独トップを守りました。",
                "地元の期待を背負うメキシコのラウル・ペレダが5バーディを奪う67をマークし、通算12アンダーの単独2位へ浮上。日曜日はいよいよメキシコ勢初優勝を懸けた運命の最終ラウンドを迎えます。"
            ]
        },
        "ko": {
            "title": "PGA 투어 멕시코 오픈 3R: 스모더먼 13언더파 단독 선두 유지, 홈스타 페레다 1타 차 추격",
            "subtitle": "스모더먼 69타로 54홀 선두 고수; 멕시코의 라울 페레다가 67타 맹타로 최종일 챔피언조 격돌.",
            "excerpt": "오스틴 스모더먼이 비단타바야르타에서 13언더파로 선두를 지켰으나, 멕시코의 라울 페레다가 1타 차로 바짝 따라붙었습니다.",
            "body": [
                "10월 31일 토요일 멕시코 바야르타에서 열린 PGA 투어 비단타월드 멕시코 오픈 무빙데이에서 오스틴 스모더먼이 2타를 줄이며 3라운드 합계 13언더파 200타로 선두 자리를 굳게 지켰습니다.",
                "멕시코 팬들의 열광적인 응원을 등에 업은 라울 페레다는 버디 5개를 낚으며 4언더파 67타를 기록, 합계 12언더파 201타로 단독 2위에 올랐습니다. 잉글랜드의 에런 라이가 11언더파 3위로 뒤를 이었습니다."
            ]
        },
        "ar": {
            "title": "جولة بي جي إيه بطولة المكسيك المفتوحة الجولة 3: سموذر مان يحافظ على الصدارة بـ 13 تحت المعدل وبيريدا يطارده بفارق ضربة",
            "subtitle": "اللاعب الأمريكي يسجل 69 ضربة في الرياح والبطل المكسيكي راؤول بيريدا يسجل 67 ليلهب حماس الجماهير.",
            "excerpt": "يتصدر أوستن سموذر مان بطولة المكسيك المفتوحة للجولف بمجموع 13 تحت المعدل، وسط مطاردة شرسة من راؤول بيريدا (-12).",
            "body": [
                "حافظ الأمريكي أوستن سموذر مان على صدارة بطولة فيدانتا وورلد المكسيك المفتوحة يوم السبت 31 أكتوبر بعد أن أنهى الجولة الثالثة بـ 69 ضربة (-2) ليرفع رصيده إلى 13 تحت المعدل (200 ضربة) بعد 54 حفرة.",
                "وأشعل النجم المكسيكي راؤول بيريدا حماس الجماهير المحلية بتسجيله 67 ضربة (-4) ليحتل المركز الثاني منفردا بـ 12 تحت المعدل، ليخوض الجولة النهائية يوم الأحد في المجموعة الأخيرة بجوار سموذر مان بحثا عن إنجاز تاريخي للمكسيك."
            ]
        }
    },
    "nba-spurs-wembanyama-dominates-suns-118-106-statement-2026": {
        "fr": {
            "title": "NBA : Victor Wembanyama eblouissant avec 31 points et 6 contres, les Spurs dominent Phoenix 118-106",
            "subtitle": "Le prodige francais et Chris Paul (12 passes) etouffent les Suns de Kevin Durant pour grimper a 3-1.",
            "excerpt": "Victor Wembanyama a signe un nouveau chef-d'oeuvre samedi soir avec 31 points et 6 contres pour mener San Antonio a la victoire.",
            "body": [
                "Victor Wembanyama a livre une prestation magistrale ce samedi 31 octobre a Phoenix. Le pivot francais des Spurs a compile 31 points a 12 sur 19 aux tirs, 14 rebonds et 6 contres pour porter San Antonio vers un succes convaincant 118-106 sur les Suns.",
                "Parfaitement guide par un Chris Paul impeccable a la baguette (12 passes, aucun ballon perdu), San Antonio a resiste au retour des Suns emmenes par Kevin Durant (28 points). Dans le money time, Wembanyama a bloque Booker avant d'inscrire un tir a trois points decisif pour plier la rencontre."
            ]
        },
        "es": {
            "title": "NBA: Victor Wembanyama deslumbra con 31 puntos y 6 tapones en el triunfo de Spurs ante Suns 118-106",
            "subtitle": "El fenomeno galo y Chris Paul comandan el asalto a Phoenix para colocar a San Antonio con balance de 3-1.",
            "excerpt": "Victor Wembanyama firmo una actuacion historica este sabado con 31 puntos, 14 rebotes y 6 tapones para derrotar a los Suns en su cancha.",
            "body": [
                "Victor Wembanyama dejo otra noche para el recuerdo este sabado 31 de octubre en el Footprint Center. La estrella de San Antonio destapo todo su potencial con 31 puntos, 14 rebotes, 6 tapones y 3 robos en 34 minutos para doblegar a los Phoenix Suns 118-106.",
                "Con Chris Paul repartiendo 12 asistencias sin perdidas, los Spurs dominaron la primera mitad. Aunque Kevin Durant respondio con 28 puntos para meter presion a los texanos, Wembanyama cerro la victoria con dos acciones defensivas clave y un triple letal en los minutos finales."
            ]
        },
        "de": {
            "title": "NBA: Victor Wembanyama dominiert mit 31 Punkten und 6 Blocks beim 118:106 der Spurs ueber Phoenix",
            "subtitle": "Franzoesisches Ausnahmetalent fuehrt San Antonio zusammen mit Spielmacher Chris Paul zum Auswaertssieg.",
            "excerpt": "Victor Wembanyama zeigte am Samstagabend in Phoenix eine ueberragende Leistung und fuehrte die Spurs zu einem 118:106-Erfolg.",
            "body": [
                "Victor Wembanyama war am Samstag, den 31. Oktober, von den Phoenix Suns nicht zu stoppen. Der 22-jaehrige Franzose verbuchte 31 Punkte, 14 Rebounds, 6 Blocks und 3 Steals und fuehrte die San Antonio Spurs zu einem souveraenen 118:106-Auswaertssieg.",
                "Gemeinsam mit Veteran Chris Paul, der 12 Assists ohne Ballverlust verteilte, kontrollierten die Spurs die Partie. Trotz 28 Punkten von Kevin Durant sicherten die Texaner in der Schlussphase dank Wembanyamas defensiver Praesenz den dritten Saisonsieg."
            ]
        },
        "it": {
            "title": "NBA: Victor Wembanyama monumentale con 31 punti e 6 stoppate, gli Spurs espugnano Phoenix 118-106",
            "subtitle": "Il fenomeno francese domina su entrambi i lati del campo ben innescato da Chris Paul; San Antonio sale sul 3-1.",
            "excerpt": "Ennesima prestazione leggendaria per Victor Wembanyama: 31 punti, 14 rimbalzi e 6 stoppate nel successo di San Antonio sui Suns.",
            "body": [
                "Victor Wembanyama ha incantato il Footprint Center sabato sera 31 ottobre. Il fenomeno francese ha dominato la sfida contro i Phoenix Suns mettendo a referto 31 punti (12/19 al tiro), 14 rimbalzi, 6 stoppate e 3 recuperi nel netto 118-106 finale.",
                "Sostenuti da una superba regia di Chris Paul (12 assist e zero palle perse), gli Spurs hanno rintuzzato il tentativo di rimonta guidato da Kevin Durant (28 punti). Wembanyama ha chiuso la contesa con una tripla e due stoppate consecutive nell'ultimo minuto."
            ]
        },
        "pl": {
            "title": "NBA: Victor Wembanyama dominuje z 31 punktami i 6 blokami, Spurs pokonuja Suns 118:106",
            "subtitle": "Francuski geniusz i Chris Paul prowadza ekipe z San Antonio do cennego triumfu wyjazdowego w Phoenix.",
            "excerpt": "Victor Wembanyama rozegral genialne zawody w Phoenix, notujac 31 punktow, 14 zbiorek i 6 blokow w wygranym meczu Spurs.",
            "body": [
                "San Antonio Spurs wygrali w sobote 31 pazdziernika z Phoenix Suns 118:106 na wyjezdzie, glownie dzieki niesamowitej grze Victora Wembanyamy. 22-letni Francuz rzucil 31 punktow, mial 14 zbiorek i zablokowal 6 rzutow rywali.",
                "Weteran Chris Paul rozdal 12 asyst bez ani jednej straty, swietnie kreujac akcje dla zespolu. Choc Kevin Durant zdobyl dla Suns 28 punktow, to rzuty z dystansu i obrona Wembanyamy w ostatnich minutach przesadzily o sukcesie Spurs."
            ]
        },
        "zh": {
            "title": "NBA常规赛：文班亚马狂砍31分14板6盖帽统治攻防，马刺客场118-106力克太阳",
            "subtitle": "法国天才联手保罗（12助攻0失误）击退杜兰特28分反扑，圣城青年军战绩提升至3胜1负。",
            "excerpt": "文班亚马周六在菲尼克斯打出震撼攻防表现，独揽31分14篮板6盖帽带队战胜太阳队。",
            "body": [
                "10月31日周六晚，马刺队在菲尼克斯足迹中心球馆以118-106战胜太阳队。22岁的法国核心维克托·文班亚马展现了划时代的统治力，全场出战34分钟，19投12中高效轰下31分、14个篮板、6次封盖和3次抢断。",
                "老将克里斯·保罗送出12次助攻且失误为零，完美梳理全队进攻。尽管杜兰特砍下28分试图带队反扑，但文班亚马在第四节最后阶段连送大帽并在外线干拔三分命中，干净利落地为马刺锁定胜局。"
            ]
        },
        "ja": {
            "title": "NBA：ウェンバンヤマが31得点14リバウンド6ブロックと大爆発、スパーズがサンズを118-106で撃破",
            "subtitle": "フランスの新星が攻守で圧倒的な存在感；クリス・ポールも12アシスト0ターンオーバーで貢献。",
            "excerpt": "ウェンバンヤマが31得点6ブロックの驚異的なダブルダブルを記録し、スパーズがフェニックスで快勝しました。",
            "body": [
                "10月31日土曜日、フェニックスで行われたNBA公式戦で、サンアントニオ・スパーズが118-106でフェニックス・サンズを下しました。主役となったのは22歳のビクター・ウェンバンヤマで、31得点、14リバウンド、6ブロック、3スティールと圧巻のスタッツを残しました。",
                "ベテラン司令塔のクリス・ポールが12アシスト・無失策でゲームを支配。ケビン・デュラントが28得点で追いすがったサンズでしたが、終盤にウェンバンヤマが決定的なブロックと3ポイントを決めて突き放しました。"
            ]
        },
        "ko": {
            "title": "NBA: 빅터 웸반야마 31점 14리바운드 6블록 맹폭, 스퍼스 피닉스 원정서 118-106 완승",
            "subtitle": "프랑스 괴물 센터의 공수 지배력과 크리스 폴의 12어시스트 무실책 활약으로 3승 1패 질주.",
            "excerpt": "웸반야마가 토요일 밤 피닉스에서 31점 14리바운드 6블록슛을 기록하며 샌안토니오의 118-106 승리를 이끌었습니다.",
            "body": [
                "10월 31일 토요일 피닉스 풋프린트 센터에서 열린 NBA 경기에서 샌안토니오 스퍼스가 피닉스 선즈를 118-106으로 꺾었습니다. 빅터 웸반야마는 34분 동안 31점 14리바운드 6블록 3스틸을 폭발시키며 코트를 완벽히 장악했습니다.",
                "야전사령관 크리스 폴이 실책 없이 12개의 어시스트를 배달하며 완벽한 조력자 역할을 했습니다. 듀란트가 28점으로 분전한 피닉스는 4쿼터 막판 웸반야마의 결정적인 블록슛과 3점포에 무릎을 꿇었습니다."
            ]
        },
        "ar": {
            "title": "دوري السلة الأمريكي: فيكتور ويمبانياما يتألق بـ 31 نقطة و6 تصديات ويقود سبيرز للفوز على صنز 118-106",
            "subtitle": "العملاق الفرنسي يبهر الجماهير في فينيكس ويعزز انطلاقة سان أنطونيو المميزة بنتيجة 3-1.",
            "excerpt": "قدم فيكتور ويمبانياما أداء تاريخيا بتسجيله 31 نقطة و14 متابعة و6 تصديات ليقود سبيرز لإسقاط صنز.",
            "body": [
                "قدم النجم الفرنسي الشاب فيكتور ويمبانياما عرضا خارقا مساء السبت 31 أكتوبر في قاعة فوتبرينت سنتر، مسجلا 31 نقطة و14 متابعة و6 تصديات و3 سرقات للكرة ليقود سان أنطونيو سبيرز للفوز على فينيكس صنز بنتيجة 118-106.",
                "وساهم المخضرم كريس بول بـ 12 تمريرة حاسمة دون أي خطأ في إدارة هجوم سبيرز، ليتصدى الفريق لمحاولات كيفن دورانت (28 نقطة) ويحسم ويمبانياما الدقائق الأخيرة برمية ثلاثية وتصديين حاسمين تحت السلة."
            ]
        }
    },
    "cfb-week10-georgia-downs-florida-34-20-cocktail-party-2026": {
        "fr": {
            "title": "College Football Semaine 10 : Georgia renverse Florida 34-20 dans le grand classique de Jacksonville",
            "subtitle": "Carson Beck lance 3 touchdowns et Trevor Etienne amasse 112 yards au sol pour preserver l'invincibilite des Bulldogs (8-0).",
            "excerpt": "Georgia a signe une deuxieme mi-temps tonitruante samedi pour dominer son grand rival Florida 34-20 a Jacksonville.",
            "body": [
                "Le traditionnel cocktail de Jacksonville a tourne a l'avantage des Bulldogs de Georgia ce samedi 31 octobre. Menes 13-10 a la mi-temps par une vaillante equipe de Florida, les hommes de Kirby Smart ont accelere apres la pause pour s'imposer 34-20 devant 76 824 spectateurs.",
                "Le quarterback Carson Beck a ete magistral avec 285 yards et 3 passes de touchdown, tandis que l'ancien Gator Trevor Etienne a martyrise son ancienne equipe avec 112 yards au sol et un touchdown decisif. Georgia reste invaincu a 8-0 et conforte sa place de leader de la conference SEC."
            ]
        },
        "es": {
            "title": "College Football Semana 10: Georgia remonta y vence 34-20 a Florida en el clasico de Jacksonville",
            "subtitle": "Carson Beck lanza 3 pases de anotacion y Trevor Etienne corre para 112 yardas para mantener a los Bulldogs invictos (8-0).",
            "excerpt": "Georgia derroto este sabado 34-20 a su eterno rival Florida tras una brillante segunda mitad en el Cocktail Party de Jacksonville.",
            "body": [
                "La 92ª edicion del clasico celebrado en Jacksonville dejo otra victoria de prestigio para los Bulldogs de Georgia este sabado 31 de octubre. Pese a ir perdiendo 13-10 al descanso ante Florida, el equipo numero dos del pais respondio con contundencia en el segundo tiempo para ganar 34-20.",
                "El mariscal Carson Beck brillo con 285 yardas y 3 touchdowns por aire, mientras que Trevor Etienne castigo a su antiguo equipo con 112 yardas terrestres y la anotacion que sentencio el choque. Con este triunfo, Georgia se situa con 8-0 y da un paso de gigante hacia los playoffs."
            ]
        },
        "de": {
            "title": "College Football Woche 10: Georgia triumphiert mit 34:20 ueber Florida bei der Cocktail Party",
            "subtitle": "Carson Beck wirft 3 Touchdowns und Trevor Etienne laeuft fuer 112 Yards; Bulldogs bleiben mit 8:0 ungeschlagen.",
            "excerpt": "Georgia drehte am Samstag in Jacksonville einen Halbzeitrueckstand und besiegte Erzrivale Florida souveraen mit 34:20.",
            "body": [
                "Die traditionsreiche World's Largest Outdoor Cocktail Party in Jacksonville endete am Samstag, den 31. Oktober, mit einem 34:20-Erfolg der ungeschlagenen Georgia Bulldogs ueber Florida vor 76.824 Zuschauern.",
                "Nach einem 10:13-Pausenrueckstand drehte Georgias Quarterback Carson Beck auf und fuehrte sein Team mit 285 Passing-Yards und 3 Touchdown-Paessen zum Sieg. Ex-Gator Trevor Etienne trug mit 112 Rushing-Yards und einem Touchdown maßgeblich zum Erfolg bei, womit Georgia auf 8:0 Siege klettert."
            ]
        },
        "it": {
            "title": "College Football Week 10: Georgia batte Florida 34-20 nella grande classica di Jacksonville",
            "subtitle": "Carson Beck lancia 3 touchdown e Trevor Etienne corre per 112 yard contro la sua ex squadra; Bulldogs imbattuti (8-0).",
            "excerpt": "Georgia rimonta nella ripresa e supera Florida 34-20 a Jacksonville rimanendo perfetta in testa alla SEC.",
            "body": [
                "Grande spettacolo ed entusiasmo a Jacksonville sabato 31 ottobre per la storica sfida tra Georgia e Florida. I Bulldogs, sotto 13-10 all'intervallo, hanno dominato la ripresa chiudendo i conti sul 34-20 davanti a oltre 76.000 spettatori.",
                "Il quarterback Carson Beck ha brillato con 285 yard e 3 passaggi vincenti, mentre il running back Trevor Etienne ha punito i suoi vecchi compagni con 112 yard su corsa e una meta decisiva. Georgia sale a 8-0 in classifica e blinda il comando della SEC."
            ]
        },
        "pl": {
            "title": "College Football Tydzien 10: Georgia pokonuje Floride 34:20 w slynnej Cocktail Party w Jacksonville",
            "subtitle": "Carson Beck rzucil 3 przylozenia, a Trevor Etienne zdobyl 112 jardow dolem; Bulldogs pozostaja niepokonani z bilansem 8-0.",
            "excerpt": "Georgia odwrocila losy meczu po przerwie i pokonala odwiecznego rywala Floride 34:20 w prestizowym meczu w Jacksonville.",
            "body": [
                "Druzyne Georgia Bulldogs czeka kolejny krok w strone play-offow po sobotnim zwyciestwie 34:20 nad Florida Gators w Jacksonville. Mimo iz do przerwy Florida prowadzila 13:10, faworyci pokazali klase w drugiej czesci gry.",
                "Rozgrywajacy Carson Beck rzucil 285 jardow i 3 przylozenia, a Trevor Etienne w meczu przeciwko swojemu bylemu uniwersytetowi wybiegal 112 jardow z przylozeniem. Georgia z kompletem osmiu zwyciestw pewnie zmierza po tytul konferencji SEC."
            ]
        },
        "zh": {
            "title": "NCAA橄榄球第10周：佐治亚下半场发力34-20力克佛罗里达，豪取8连胜领跑SEC",
            "subtitle": "卡森·贝克送出3次达阵传球，转校前锋埃蒂安狂砍112码弑杀旧主；杰克逊维尔传统德比完美收官。",
            "excerpt": "全美第二佐治亚斗牛犬队周六在杰克逊维尔反超佛罗里达，以34-20延续赛季不败金身。",
            "body": [
                "10月31日周六在杰克逊维尔艾佛班克体育场上演的经典狂欢派对德比中，佐治亚斗牛犬队在半场10-13落后的逆境下爆发，以34-20击败佛罗里达短吻鳄队，赛季战绩刷新至8胜0负。",
                "四分卫卡森·贝克下半场状态火热，全场29投22中轰下285码和3次达阵。面对旧主的反戈名将特雷弗·埃蒂安冲球18次拿下112码并在末节打进锁定胜局的达阵，帮助佐治亚取得对佛罗里达的四连胜。"
            ]
        },
        "ja": {
            "title": "カレッジフットボール第10週：ジョージア大が後半逆転で宿敵フロリダ大を34-20で撃破、無敗の8連勝",
            "subtitle": "QBカーソン・ベックが3TDパス、エティエンヌが古巣相手に112ヤード走破；SEC首位を堅持。",
            "excerpt": "全米2位のジョージア大がジャクソンビルの伝統の一戦で後半24点を奪い、34-20でフロリダ大を下しました。",
            "body": [
                "10月31日土曜日にジャクソンビルで行われた全米屈指のライバル対決『カクテルパーティー』は、全米2位のジョージア大が後半の猛攻でフロリダ大を34-20で下しました。",
                "前半を10-13とリードを許したジョージアでしたが、QBカーソン・ベックが285ヤード・3タッチダウンのパスを通し逆転に成功。古巣対決となったRBトレバー・エティエンヌが112ヤードを走ってダメ押しのTDを奪い、開幕8連勝を飾りました。"
            ]
        },
        "ko": {
            "title": "대학 미식축구 10주차: 조지아대, 잭슨빌 더비서 플로리다대 34-20 완파하고 8연승 질주",
            "subtitle": "카슨 벡 3TD 패스 폭발과 트레버 에티엔의 112야드 러싱으로 후반 대역전승; SEC 단독 선두.",
            "excerpt": "조지아대가 토요일 잭슨빌에서 열린 숙명의 라이벌전에서 후반 폭발력을 앞세워 플로리다대를 34-20으로 꺾었습니다.",
            "body": [
                "10월 31일 토요일 잭슨빌 에버뱅크 스타디움에서 열린 전통의 라이벌전에서 전미 2위 조지아 불독스가 플로리다 게이터스를 34-20으로 물리쳤습니다.",
                "전반을 10-13으로 뒤졌던 조지아는 후반 쿼터백 카슨 벡의 정교한 3개의 터치다운 패스로 경기를 뒤집었습니다. 친정팀을 상대한 러닝백 트레버 에티엔이 112야드 러싱과 쐐기 터치다운을 터뜨리며 팀의 무패 행진(8승 0패)을 지켜냈습니다."
            ]
        },
        "ar": {
            "title": "كرة القدم الأمريكية الجامعية الأسبوع 10: جورجيا تقلب الطاولة على فلوريدا وتفوز 34-20 في جاكسونفيل",
            "subtitle": "كارسون بيك يسجل 3 تمريرات هبوط وإيتيين يركض لمسافة 112 ياردة ليقودا بولدوغز لانتصارهم الثامن دون هزيمة.",
            "excerpt": "حسم فريق جورجيا ديربي جاكسونفيل التاريخي لصالحه يوم السبت بالفوز 34-20 على فلوريدا ليحافظ على سجله المثالي 8-0.",
            "body": [
                "شهدت قمة جاكسونفيل التقليدية مساء السبت 31 أكتوبر فوزا مثيرا لفريق جورجيا بولدوغز على غريمه فلوريدا بنتيجة 34-20 أمام أكثر من 76 ألف متفرج.",
                "وعلى الرغم من تأخر جورجيا في الشوط الأول 10-13، تألق الموزع كارسون بيك في الشوط الثاني مسجلا 285 ياردة و3 تمريرات هبوط دون أي خطأ، بينما أضاف تريفور إيتيين 112 ياردة ركضا وهبوطا حاسما ضد فريقه السابق ليمنح جورجيا فوزها الثامن تواليا في صدارة مؤتمر SEC."
            ]
        }
    }
}

# Strict validation
for slug, langs in OCT31_STORIES.items():
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

print("All October 31 story translations validated: 0 em-dashes and 0 double-hyphens.")

snippet_parts = []
for slug, langs in OCT31_STORIES.items():
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

print("Successfully injected October 31 translations into frontend/src/i18n/stories.ts")
