import json
import re

OCT22_STORIES = {
    "wnba-finals-2026-game3-dream-crush-valkyries-97-71": {
        "fr": {
            "title": "Le Dream ecrase les Valkyries 97-71 et mene 2-1",
            "subtitle": "Angel Reese entre dans l'histoire avec 21 points et 12 rebonds. Match 4 vendredi a Atlanta.",
            "excerpt": "Atlanta s'impose de 26 points lors du match 3 mercredi soir. Le Dream mene 2-1 et peut remporter le titre des vendredi.",
            "body": [
                "L'Atlanta Dream a pris les commandes des Finales WNBA mercredi soir en surclassant les Golden State Valkyries 97-71 lors du match 3 a la State Farm Arena. Ce large succes de 26 points permet a Atlanta de mener 2-1 dans cette serie au meilleur des cinq matches. Le Dream a domine les quatre quart-temps (25-18, 24-17, 26-16, 22-20) devant 17 854 spectateurs enthousiastes.",
                "Angel Reese a encore ecrit l'histoire avec 21 points, 12 rebonds et trois interceptions a 8 sur 14 aux tirs. Elle devient la premiere joueuse de l'histoire de la WNBA a reussir un double-double lors de chacun de ses trois premiers matches en Finales. Rhyne Howard a ajoute 16 points et Naz Hillmon 15. Golden State a ete limite a 35 pour cent de reussite. Le match 4 aura lieu vendredi a Atlanta avec la balle de titre pour le Dream."
            ]
        },
        "es": {
            "title": "El Dream arrolla 97-71 a las Valkyries y se adelanta 2-1",
            "subtitle": "Angel Reese hace historia con 21 puntos y 12 rebotes. El Juego 4 es el viernes en Atlanta.",
            "excerpt": "Atlanta vencio por 26 puntos en el Juego 3 el miercoles por la noche. El Dream manda 2-1 y puede coronarse campeon este viernes.",
            "body": [
                "El Atlanta Dream tomo el control de las Finales WNBA este miercoles al arrollar 97-71 a las Golden State Valkyries en el State Farm Arena. El triunfo por 26 puntos coloca a Atlanta 2-1 arriba en la serie por el campeonato. El Dream domino cada uno de los cuatro periodos (25-18, 24-17, 26-16, 22-20) ante 17.854 espectadores que llenaron las gradas.",
                "Angel Reese firmo otra actuacion historica con 21 puntos, 12 rebotes y tres robos con 8 de 14 en tiros de campo. Se convierte en la primera jugadora en la historia de la liga en registrar un doble-doble en sus tres primeros partidos de Finales. Rhyne Howard aporto 16 puntos y Naz Hillmon 15. Golden State se quedo en un 35 por ciento en tiros. El Juego 4 sera el viernes en Atlanta."
            ]
        },
        "de": {
            "title": "Dream fegen Valkyries mit 97-71 vom Feld und fuehren 2-1",
            "subtitle": "Angel Reese schreibt WNBA-Geschichte mit 21 Punkten und 12 Rebounds. Spiel 4 am Freitag in Atlanta.",
            "excerpt": "Atlanta feiert am Mittwochabend einen 26-Punkte-Kantersieg in Spiel 3. Das Dream fuehrt 2-1 und kann am Freitag den Titel holen.",
            "body": [
                "Das Atlanta Dream hat am Mittwochabend mit einem souveraenen 97-71-Erfolg ueber die Golden State Valkyries in Spiel 3 der WNBA-Finals die Serienfuehrung uebernommen. Durch den 26-Punkte-Sieg liegt Atlanta in der Best-of-Five-Serie mit 2-1 vorn. Das Dream entschied jedes einzelne Viertel fuer sich (25-18, 24-17, 26-16, 22-20) vor 17.854 Zuschauern in der ausverkauften State Farm Arena.",
                "Angel Reese Glaenzte erneut mit 21 Punkten, 12 Rebounds und drei Steals bei einer Trefferquote von 8 aus 14. Sie ist die erste Spielerin der WNBA-Geschichte mit einem Double-Double in jedem ihrer ersten drei Finalspiele. Rhyne Howard steuerte 16 Punkte bei, Naz Hillmon erzielte 15. Golden State traf lediglich 35 Prozent aus dem Feld. Spiel 4 folgt am Freitagabend in Atlanta."
            ]
        },
        "it": {
            "title": "Il Dream travolge le Valkyries 97-71 e sale 2-1 nelle Finals",
            "subtitle": "Angel Reese nella storia con 21 punti e 12 rimbalzi. Gara 4 venerdi ad Atlanta.",
            "excerpt": "Atlanta domina con 26 punti di scarto in Gara 3 mercoledi sera. Il Dream conduce 2-1 e venerdi avra il match point per il titolo.",
            "body": [
                "L'Atlanta Dream ha preso il comando delle WNBA Finals mercoledi sera superando nettamente le Golden State Valkyries per 97-71 in Gara 3 alla State Farm Arena. Il successo da 26 punti porta Atlanta avanti 2-1 nella serie per il titolo. Il Dream ha vinto ogni singolo quarto (25-18, 24-17, 26-16, 22-20) davanti al pubblico delle grandi occasioni di 17.854 spettatori.",
                "Angel Reese e entrata nella storia con 21 punti, 12 rimbalzi e tre recuperi tirando 8 su 14 dal campo. E la prima giocatrice nella storia della WNBA a centrare una doppia doppia in ciascuna delle sue prime tre gare di Finale. Rhyne Howard ha messo a referto 16 punti e Naz Hillmon 15. Golden State ha tirato con il 35 per cento dal campo. Gara 4 andra in scena venerdi ad Atlanta."
            ]
        },
        "pl": {
            "title": "Dream rozbily Valkyries 97-71 i prowadza 2-1 w finalach",
            "subtitle": "Angel Reese tworzy historie z 21 punktami i 12 zbiorkami. Mecz 4 w piatek w Atlancie.",
            "excerpt": "Atlanta wygrala mecz 3 roznica 26 punktow w srode wieczorem. Dream prowadza 2-1 i w piatek moga siegnac po mistrzostwo.",
            "body": [
                "Atlanta Dream objely prowadzenie w finalach WNBA po przekonujacym zwyciestwie 97-71 nad Golden State Valkyries w meczu 3 w State Farm Arena w srode wieczorem. Wygrana 26 punktami daje Atlancie prowadzenie 2-1 w serii do trzech zwyciestw. Gospodynie wygraly kazda z czterech kwart (25-18, 24-17, 26-16, 22-20) przy komplecie 17 854 widzow.",
                "Angel Reese znow zachwycila, notujac 21 punktow, 12 zbiorek i trzy przechwyty przy skutecznosci 8 na 14 z gry. Zostala pierwsza koszykarka w historii WNBA z double-double w kazdym ze swoich trzech pierwszych meczow finalowych. Rhyne Howard dolozyla 16 punktow, a Naz Hillmon 15. Valkyries trafily zaledwie 35 procent rzutow z gry. Czwarty mecz odbedzie sie w piatek w Atlancie."
            ]
        },
        "zh": {
            "title": "梦想97-71大胜女武神，总决赛取得2-1领先",
            "subtitle": "安吉尔·里斯砍下21分12篮板创纪录。第4战将于周五在亚特兰大打响。",
            "excerpt": "亚特兰大在周三晚第3战净胜26分。梦想总比分2-1领先，周五若再胜即可夺得队史首座总冠军。",
            "body": [
                "亚特兰大梦想在周三晚的WNBA总决赛第3战中牢牢掌控局势，在州立农业球馆以97-71大胜金州女武神。这场26分的大胜让梦想在五局三胜制系列赛中以2-1抢下赛点。现场17854名爆满观众见证了主队在四节比赛中全部占据优势（25-18、24-17、26-16、22-20）。",
                "安吉尔·里斯交出21分12篮板3抢断的全面数据，全场14投8中。她成为WNBA历史上第一位在个人职业生涯前三场总决赛均斩获两双的球员。莱恩·霍华德贡献16分，替补出场的纳兹·希尔蒙拿下15分。女武神全队投篮命中率仅为35%。总决赛第4战将于周五在亚特兰大进行。"
            ]
        },
        "ja": {
            "title": "ドリームがヴァルキリーズを97-71で圧倒、2勝1敗で王手へ",
            "subtitle": "エンジェル・リースが21得点12リバウンドで歴史的快挙。第4戦は金曜日にアトランタで開催。",
            "excerpt": "アトランタが水曜夜の第3戦を26点差で大勝。ドリームが2勝1敗とし、金曜日の第4戦で初優勝を狙います。",
            "body": [
                "アトランタ・ドリームは水曜夜、ステートファーム・アリーナで行われたWNBAファイナル第3戦でゴールデンステイト・ヴァルキリーズを97-71で圧倒しました。26点差の完勝でシリーズを2勝1敗とし、初優勝へ王手をかけました。17,854人の超満員の観衆の前で、ドリームは4つのクォーター全てでリードを奪いました（25-18, 24-17, 26-16, 22-20）。",
                "エンジェル・リースはFG14本中8本成功の21得点12リバウンド3スティールを記録。ファイナル最初の3試合すべてでダブルダブルを達成したWNBA史上初の選手となりました。ライン・ハワードが16得点、ナズ・ヒルモンが15得点をマーク。ヴァルキリーズはFG成功率35パーセントに抑え込まれました。運命の第4戦は金曜日にアトランタで行われます。"
            ]
        },
        "ko": {
            "title": "드림, 발키리스 97-71 대파... 파이널 2승 1패 리드",
            "subtitle": "엔젤 리스 21득점 12리바운드로 WNBA 역사 작성. 4차전은 금요일 애틀랜타.",
            "excerpt": "애틀랜타가 수요일 밤 3차전에서 26점 차 완승을 거뒀습니다. 드림이 2승 1패로 앞서며 금요일 첫 우승에 도전합니다.",
            "body": [
                "애틀랜타 드림이 수요일 밤 스테이트팜 아레나에서 열린 WNBA 파이널 3차전에서 골든스테이트 발키리스를 97-71로 완파했습니다. 26점 차 압승으로 시리즈 2승 1패를 만든 애틀랜타는 창단 첫 우승까지 1승만을 남겨뒀습니다. 17,854명 만원 관중 앞에서 드림은 매 쿼터 상대를 압도했습니다 (25-18, 24-17, 26-16, 22-20).",
                "엔젤 리스는 야투 14개 중 8개를 성공시키며 21득점 12리바운드 3스틸을 기록했습니다. 파이널 첫 3경기에서 모두 더블더블을 달성한 선수는 WNBA 역사상 리스가 처음입니다. 라인 하워드가 16점, 나즈 힐먼이 15점을 보탰습니다. 발키리스의 야투율은 35퍼센트에 묶였습니다. 4차전은 금요일 애틀랜타에서 치러집니다."
            ]
        },
        "ar": {
            "title": "دريم يسحق فالكيريز 97-71 ويتقدم 2-1 في النهائيات",
            "subtitle": "انجيل ريس تصنع التاريخ بـ21 نقطة و12 متابعة. المباراة 4 تقام الجمعة في اتلانتا.",
            "excerpt": "فازت اتلانتا بفارق 26 نقطة في المباراة 3 مساء الاربعاء. دريم يتقدم 2-1 ويقترب من اللقب يوم الجمعة.",
            "body": [
                "فرض اتلانتا دريم سيطرته على نهائيات WNBA مساء الاربعاء بعد فوزه العريض 97-71 على غولدن ستيت فالكيريز في المباراة 3 على ملعب ستيت فارم ارينا. هذا الفوز بفارق 26 نقطة يمنح اتلانتا التقدم 2-1 في السلسلة. وتفوق دريم في جميع الاشواط الاربعة (25-18 و24-17 و26-16 و22-20) امام 17854 متفرجا.",
                "حققت انجيل ريس انجازا تاريخيا بتسجيل 21 نقطة و12 متابعة و3 سرقات للكرة مسددة 8 من 14 من الميدان. واصبحت اول لاعبة في تاريخ المسابقة تسجل ثنائية مزدوجة في مبارياتها الثلاث الاولى بالنهائيات. اضافت راين هوارد 16 نقطة وناز هيلمون 15 نقطة. اكتفى فالكيريز بنسبة تسديد بلغت 35 بالمئة. تقام المباراة 4 الجمعة في اتلانتا."
            ]
        }
    },
    "atp-thursday-almaty-tsitsipas-mannarino-rublev-upset-2026": {
        "fr": {
            "title": "Tsitsipas conclut la carriere de Kukushkin, Mannarino bat Rublev",
            "subtitle": "Mikhail Kukushkin a dispute son match d'adieu a Almaty. Adrian Mannarino a terrasse la tete de serie 4 en trois sets.",
            "excerpt": "Tsitsipas rallie les quarts a Almaty en battant le veteran Kukushkin 6-1, 6-2. Mannarino surprend Rublev 6-4, 3-6, 6-3.",
            "body": [
                "La journee de jeudi 22 octobre a offert un moment charge d'emotion a l'Open d'Almaty. Stefanos Tsitsipas s'est qualifie pour les quarts de finale en battant le joueur kazakh Mikhail Kukushkin 6-1, 6-2. Ce match marquait le dernier duel professionnel en simple de la carriere de Kukushkin, apres vingt annees sur le circuit ATP. Le public de l'Almaty Arena lui a reserve une ovation debout inoubliable.",
                "Les huitiemes de finale ont egalement vu Adrian Mannarino creer une enorme sensation en dominant Andrey Rublev, tete de serie numero 4, sur le score de 6-4, 3-6, 6-3. Mannarino a brise le jeu du joueur du top dix mondial grace a une remarquable precision tactique. James Duckworth a egalement rejoint les quarts de finale en disposant de Luciano Darderi 7-5, 7-6(9), tout comme Mattia Bellucci vainqueur d'Etcheverry."
            ]
        },
        "es": {
            "title": "Tsitsipas despide a Kukushkin, Mannarino sorprende a Rublev",
            "subtitle": "Mikhail Kukushkin jugo su ultimo partido en Almaty. Adrian Mannarino elimino al cuarto favorito en tres mangas.",
            "excerpt": "Tsitsipas avanzo a cuartos en Almaty al superar a Kukushkin 6-1, 6-2. Mannarino dio la campanada ante Rublev 6-4, 3-6, 6-3.",
            "body": [
                "El jueves 22 de octubre dejo una jornada historica y emotiva en el ATP de Almaty. Stefanos Tsitsipas sello su pase a cuartos de final al vencer por 6-1, 6-2 al veterano kazajo Mikhail Kukushkin. El partido supuso la despedida oficial de Kukushkin tras dos decadas en el tenis profesional, recibiendo una emocionante ovacion del publico local.",
                "La gran sorpresa de los octavos la firmo el frances Adrian Mannarino al eliminar al cuarto cabeza de serie Andrey Rublev por 6-4, 3-6, 6-3 en un despliegue de maestria sobre pista rapida cubierta. El australiano James Duckworth tambien se instalo en cuartos tras derrotar al segundo sembrado Luciano Darderi por 7-5, 7-6(9), mientras Mattia Bellucci doblego a Tomas Martin Etcheverry."
            ]
        },
        "de": {
            "title": "Tsitsipas beendet Kukushkins Karriere, Mannarino schockt Rublev",
            "subtitle": "Mikhail Kukushkin spielte sein Abschiedsmatch in Almaty. Adrian Mannarino bezwang die Nummer 4 in drei Saetzen.",
            "excerpt": "Tsitsipas zog mit 6-1, 6-2 ueber Routinier Kukushkin ins Almaty-Viertelfinale ein. Mannarino ueberraschte Rublev 6-4, 3-6, 6-3.",
            "body": [
                "Am Donnerstag, 22. Oktober, erlebten die Tennisfans in Almaty einen zutiefst emotionalen Nachmittag. Stefanos Tsitsipas erreichte das Viertelfinale durch ein 6-1, 6-2 ueber den 38-Jaehrigen Lokalmatador Mikhail Kukushkin. Fuer Kukushkin war es das letzte Einzelmatch seiner fast 20-Jaehrigen Profikarriere, gewuerdigt mit stehenden Ovationen der Almaty Arena.",
                "Fuer die groesste sportliche Ueberraschung sorgte Adrian Mannarino, der den an Nummer vier gesetzten Andrey Rublev mit 6-4, 3-6, 6-3 aus dem Turnier warf. Der franzoesische Routinier kontrollierte das Tempo mit praezisem Konterspiel. Auch James Duckworth steht nach einem 7-5, 7-6(9) ueber den an zwei gesetzten Luciano Darderi im Viertelfinale, waehrend Mattia Bellucci Tomas Martin Etcheverry bezwang."
            ]
        },
        "it": {
            "title": "Tsitsipas chiude la carriera di Kukushkin, Mannarino batte Rublev",
            "subtitle": "Mikhail Kukushkin ha disputato il suo match d'addio ad Almaty. Adrian Mannarino elimina il numero 4 in tre set.",
            "excerpt": "Tsitsipas vola ai quarti ad Almaty superando Kukushkin 6-1, 6-2. Mannarino firma l'impresa battendo Rublev 6-4, 3-6, 6-3.",
            "body": [
                "Giovedi 22 ottobre ha regalato grandi emozioni all'ATP di Almaty. Stefanos Tsitsipas si e qualificato per i quarti di finale battendo 6-1, 6-2 il trentottenne kazako Mikhail Kukushkin. E stata l'ultima partita da professionista per Kukushkin, salutato da una calorosa standing ovation del pubblico di casa dopo vent'anni di carriera nel circuito.",
                "Nel tabellone spicca il colpo di Adrian Mannarino, capace di eliminare la quarta testa di serie Andrey Rublev con lo score di 6-4, 3-6, 6-3 dopo quasi due ore di battaglia tattica sul veloce indoor. Avanza ai quarti anche James Duckworth, che ha eliminato il numero due del seeding Luciano Darderi 7-5, 7-6(9), mentre Mattia Bellucci ha estromesso Etcheverry."
            ]
        },
        "pl": {
            "title": "Tsitsipas konczy kariere Kukushkina, Mannarino pokonuje Rublowa",
            "subtitle": "Mikhail Kukushkin rozegral pozegnalny mecz w Almatach. Adrian Mannarino wyeliminowal turniejowa czworke.",
            "excerpt": "Tsitsipas zameldowal sie w cwiercfinale w Almatach, wygrywajac z Kukushkinem 6-1, 6-2. Mannarino pokonal Rublowa 6-4, 3-6, 6-3.",
            "body": [
                "Czwartek 22 pazdziernika przyniosl wzruszajace chwile podczas turnieju w Almatach. Stefanos Tsitsipas pewnie awansowal do cwiercfinalu, pokonujac 6-1, 6-2 38-letniego reprezentanta gospodarzy Mikhaila Kukushkina. Dla Kazacha byl to ostatni zawodowy mecz w singlu, zamykajacy blisko dwudziestoletnia przygode na kortach ATP.",
                "Wielka niespodzianke sprawil Francuz Adrian Mannarino, ktory wyeliminowal rozstawionego z numerem czwartym Andreya Rublowa 6-4, 3-6, 6-3. Mannarino zaimponowal precyzja i taktycznym spokojem. Do najlepszej osemki dotarl takze James Duckworth po zwyciestwie nad Luciano Darderim 7-5, 7-6(9), a Mattia Bellucci pokonal Tomasa Martina Etcheverry'ego."
            ]
        },
        "zh": {
            "title": "西西帕斯送别库库什金，马纳里诺爆冷击败卢布列夫",
            "subtitle": "库库什金在阿拉木图上演生涯告别战。马纳里诺三盘力克4号种子卢布列夫。",
            "excerpt": "西西帕斯以6-1、6-2击败老将库库什金晋级八强。马纳里诺以6-4、3-6、6-3爆冷击败卢布列夫。",
            "body": [
                "10月22日周四阿拉木图公开赛见证了充满温情与敬意的一幕。7号种子西西帕斯以6-1、6-2击败38岁的哈萨克斯坦外卡老将库库什金，挺进男单八强。本场比赛是库库什金长达近二十年职业网球单打生涯的谢幕之战，全场观众起立为他送上持久的掌声。",
                "在另一场焦点对决中，法国老将马纳里诺上演精彩逆转，以6-4、3-6、6-3爆冷战胜4号种子卢布列夫，凭借精湛的变线与防反让世界前十高手无计可施。澳大利亚好手达克沃斯以7-5、7-6(9)挑落2号种子达尔德里晋级八强，贝鲁奇也三盘淘汰埃切韦里。"
            ]
        },
        "ja": {
            "title": "チチパスがククシュキンの引退戦を制す、マナリノがルブレフ撃破",
            "subtitle": "ミハイル・ククシュキンがアルマティで現役ラストマッチ。マナリノが第4シードを撃破。",
            "excerpt": "チチパスがククシュキンを6-1, 6-2で下し準々決勝へ。マナリノはルブレフに6-4, 3-6, 6-3で大金星を挙げました。",
            "body": [
                "10月22日木曜、アルマティ・オープンで感動的な一戦が行われました。第7シードのステファノス・チチパスが、地元カザフスタンの38歳ミハイル・ククシュキンを6-1, 6-2で退けベスト8進出を果たしました。約20年に及ぶプロキャリアに終止符を打つククシュキンに対し、満員の観客から惜しみないスタンディングオベーションが送られました。",
                "波乱となったのはアドリアン・マナリノの試合で、第4シードのアンドレイ・ルブレフを6-4, 3-6, 6-3で撃破。巧みな配球とカウンターで大物食いを演じました。ジェームズ・ダックワースも第2シードのダルデリを7-5, 7-6(9)で退けて準々決勝へ駒を進めました。"
            ]
        },
        "ko": {
            "title": "치치파스, 쿠쿠슈킨 은퇴 경기 승리... 마나리노는 루블료프 제압",
            "subtitle": "미하일 쿠쿠슈킨 알마티에서 고별전. 아드리안 마나리노가 4번 시드를 3세트 끝에 제압.",
            "excerpt": "치치파스가 베테랑 쿠쿠슈킨을 6-1, 6-2로 꺾고 8강에 올랐습니다. 마나리노는 루블료프를 6-4, 3-6, 6-3으로 꺾는 이변을 연출했습니다.",
            "body": [
                "10월 22일 목요일 알마티 오픈에서는 뭉클한 순간이 펼쳐졌습니다. 7번 시드 스테파노스 치치파스가 카자흐스탄의 38세 베테랑 미하일 쿠쿠슈킨을 6-1, 6-2로 꺾고 8강에 올랐습니다. 이 경기는 약 20년간 이어진 쿠쿠슈킨의 프로 단식 마지막 은퇴 경기였으며 관중들은 기립 박수로 그를 배웅했습니다.",
                "16강전에서는 프랑스의 아드리안 마나리노가 4번 시드 안드레이 루블료프를 6-4, 3-6, 6-3으로 격파하는 대이변을 낳았습니다. 마나리노는 정교한 코스 공략으로 톱10 선수를 무너뜨렸습니다. 제임스 덕워스도 2번 시드 루치아노 다르데리를 7-5, 7-6(9)으로 누르고 8강에 합류했습니다."
            ]
        },
        "ar": {
            "title": "تسيتسيباس ينهي مسيرة كوكوشكين، ومانارينو يفجر مفاجاة امام روبليف",
            "subtitle": "ميخائيل كوكوشكين خاض مباراته الوداعية في الماتي. ادريان مانارينو اسقط المصنف الرابع في ثلاث مجموعات.",
            "excerpt": "تاهل تسيتسيباس لربع النهائي في الماتي بفوزه على كوكوشكين 6-1 و6-2. مانارينو فاجأ روبليف 6-4 و3-6 و6-3.",
            "body": [
                "شهد يوم الخميس 22 اكتوبر لحظات مؤثرة في بطولة الماتي المفتوحة. حجز ستيفانوس تسيتسيباس مقعده في الدور ربع النهائي بعد فوزه 6-1 و6-2 على الكازاخستاني ميخائيل كوكوشكين البالغ 38 عاما. كانت هذه اخر مباراة فردية احترافية في مسيرة كوكوشكين التي امتدت لعشرين عاما، حيث ودعه الجمهور بتحية وقوف مؤثرة.",
                "كما شهدت المنافسات مفاجاة مدوية بفوز الفرنسي ادريان مانارينو على المصنف الرابع اندريه روبليف بنتيجة 6-4 و3-6 و6-3 بفضل براعته التكتيكية على الملاعب الصلبة. وصعد الاسترالي جيمس داكوورث الى ربع النهائي ايضا بعد تغلبه على المصنف الثاني لوتشيانو دارديري بنتيجة 7-5 و7-6(9)."
            ]
        }
    },
    "nfl-week7-thursday-patriots-bears-kickoff-tonight-2026": {
        "fr": {
            "title": "Les Patriots chez les Bears ce soir : la semaine 7 demarre a Chicago",
            "subtitle": "Soldier Field accueille le Thursday Night Football a 20 h 15 ET sur Prime Video. Les deux clubs sont a 4-2.",
            "excerpt": "La semaine 7 de la NFL debute ce soir avec Patriots chez les Bears. Chicago est favori de 3 points. Les 49ers restent a 6-0.",
            "body": [
                "La semaine 7 de la NFL s'ouvre jeudi 22 octobre a 20 h 15 ET au Soldier Field de Chicago. Les New England Patriots se deplacent chez les Chicago Bears dans un duel interconference tres attendu diffuse sur Prime Video. ESPN donne Chicago favori de 3 points a domicile.",
                "Les deux equipes arrivent avec un bilan identique de 4-2 et ambitionnent de consolider leur place dans la course aux playoffs. La semaine 6 s'etait terminee lundi soir sur la victoire des 49ers de San Francisco 23-17 face aux Commanders de Washington, maintenant les Californiens seuls invaincus a 6-0. Les Chiefs et les Vikings restent invaincus a 5-0."
            ]
        },
        "es": {
            "title": "Los Patriots visitan a los Bears hoy: arranca la semana 7 en Chicago",
            "subtitle": "Soldier Field alberga el Thursday Night Football a las 8:15 p.m. ET por Prime Video. Ambos estan 4-2.",
            "excerpt": "La semana 7 de la NFL empieza esta noche con Patriots en Bears. Chicago es favorito por 3 puntos. Los 49ers siguen 6-0.",
            "body": [
                "La semana 7 de la NFL comienza este jueves 22 de octubre a las 8:15 p.m. ET en Soldier Field. Los New England Patriots visitan a los Chicago Bears en un duelo transmitido a todo el pais por Prime Video. Las lineas de ESPN situan a Chicago favorito por 3 puntos.",
                "Ambos clubes llegan con registro de 4-2 en busca de un triunfo clave para sus aspiraciones de playoffs. En el cierre de la semana 6, los San Francisco 49ers vencieron 23-17 a Washington el lunes por la noche para ser el unico equipo invicto con 6-0. Kansas City y Minnesota continuan sin perder con marca de 5-0."
            ]
        },
        "de": {
            "title": "Patriots heute bei den Bears: Woche 7 startet in Chicago",
            "subtitle": "Soldier Field ist Schauplatz des Thursday Night Football um 20:15 Uhr ET auf Prime Video. Beide Teams stehen 4-2.",
            "excerpt": "NFL Woche 7 beginnt heute mit Patriots bei den Bears. Chicago ist 3 Punkte favorisiert. Die 49ers stehen bei 6-0.",
            "body": [
                "Die 7. NFL-Woche startet am Donnerstag, 22. Oktober, um 20:15 Uhr ET im Soldier Field in Chicago. Die New England Patriots gastieren bei den Chicago Bears live auf Prime Video. Laut ESPN-Buchmachern geht Chicago als 3-Punkte-Favorit in die Partie.",
                "Beide Franchisen halten bei einer Bilanz von 4-2 und wollen im Playoff-Rennen vorlegen. Die 49ers aus San Francisco bleiben nach dem 23-17-Sieg ueber Washington am Montagabend das einzige ungeschlagene Team mit 6-0. Die Chiefs und Vikings stehen jeweils bei 5-0."
            ]
        },
        "it": {
            "title": "I Patriots sfidano i Bears stasera: parte la Week 7 a Chicago",
            "subtitle": "Soldier Field ospita il Thursday Night Football alle 20:15 ET su Prime Video. Entrambe sul 4-2.",
            "excerpt": "La Week 7 della NFL scatta stasera con Patriots dai Bears. Chicago favorita di 3 punti. I 49ers restano imbattuti sul 6-0.",
            "body": [
                "La settima settimana della stagione NFL si apre giovedi 22 ottobre alle 20:15 ET al Soldier Field di Chicago. I New England Patriots fanno visita ai Chicago Bears in diretta nazionale su Prime Video. ESPN fissa Chicago favorita di 3 punti in casa.",
                "Entrambe le formazioni vantano un record di 4-2 e cercano punti pesanti per la corsa postseason. La settimana 6 si e chiusa lunedi notte con il successo dei San Francisco 49ers per 23-17 sui Washington Commanders, confermandosi unica capolista a quota 6-0. Chiefs e Vikings restano intonsi sul 5-0."
            ]
        },
        "pl": {
            "title": "Patriots u Bears dzis wieczorem: start 7. tygodnia w Chicago",
            "subtitle": "Soldier Field gosci Thursday Night Football o 20:15 ET na Prime Video. Obie ekipy maja 4-2.",
            "excerpt": "Tydzien 7 w NFL startuje dzis meczem Patriots u Bears. Chicago faworytem o 3 punkty. 49ers legitymuja sie bilansem 6-0.",
            "body": [
                "Tydzien 7 ligi NFL rozpoczyna sie w czwartek 22 pazdziernika o 20:15 ET na Soldier Field w Chicago. New England Patriots zagraja z Chicago Bears w meczu transmitowanym przez Prime Video. ESPN stawia Chicago w roli 3-punktowego faworyta.",
                "Oba kluby maja identyczny bilans 4-2 i celuja w umocnienie pozycji w strefie play-off. Poprzedni tydzien zakonczyl sie w poniedzialek wygrana San Francisco 49ers 23-17 nad Washington Commanders, dzieki czemu 49ers sa jedyna druzyna 6-0 w lidze. Chiefs i Vikings maja bilans 5-0."
            ]
        },
        "zh": {
            "title": "今晚爱国者客战熊：NFL第7周在芝加哥打响",
            "subtitle": "士兵球场美东晚8:15迎来周四夜赛，Prime Video直播。两队战绩同为4胜2负。",
            "excerpt": "NFL第7周今晚开战，爱国者客场挑战熊。芝加哥主场让3分。旧金山49人维持6胜0负领跑。",
            "body": [
                "NFL第7周比赛于10月22日周四美东晚8:15在芝加哥士兵球场开踢。新英格兰爱国者做客挑战芝加哥熊，由Prime Video进行全美直播。ESPN盘口显示主场作战的熊队让3分。",
                "两支球队目前的战绩同为4胜2负，力求拿下这场关键的跨区对决。在此前结束的第6周周一夜赛中，旧金山49人以23-17力克华盛顿指挥官，成为全联盟唯一保持6胜0负不败的球队。酋长与维京人同以5胜0负紧随其后。"
            ]
        },
        "ja": {
            "title": "今夜ペイトリオッツがベアーズ戦へ：第7週がシカゴで開幕",
            "subtitle": "ソルジャー・フィールドで東部午後8時15分にTNFキックオフ。両軍ともに4勝2敗。",
            "excerpt": "NFL第7週が今夜開幕。ペイトリオッツがベアーズを訪問し、シカゴが3点優勢の予想。49ersは6勝0敗を維持。",
            "body": [
                "NFL第7週は10月22日木曜、東部午後8時15分にシカゴのソルジャー・フィールドで幕を開けます。ニューイングランド・ペイトリオッツがシカゴ・ベアーズと対戦し、Prime Videoで生中継されます。ESPNのラインはシカゴの3点リード。",
                "両チームともに4勝2敗の好成績で今夜の一戦を迎えます。第6週の月曜夜にはサンフランシスコ・49ersがワシントンを23-17で退け、リーグ唯一の6勝0敗を堅持しました。チーフスとバイキングスは5勝0敗を守っています。"
            ]
        },
        "ko": {
            "title": "오늘 밤 패트리어츠 대 베어스: NFL 7주차 시카고 개막",
            "subtitle": "솔저 필드에서 동부 저녁 8시 15분 TNF 킥오프, Prime Video 중계. 양 팀 모두 4승 2패.",
            "excerpt": "NFL 7주차가 오늘 밤 패트리어츠 대 베어스 전으로 시작됩니다. 시카고 3점 우세. 49ers는 6승 0패 유지.",
            "body": [
                "NFL 7주차가 10월 22일 목요일 동부 저녁 8시 15분 시카고 솔저 필드에서 시작됩니다. 뉴잉글랜드 패트리어츠가 시카고 베어스 원정에 나서며 Prime Video로 중계됩니다. ESPN은 시카고의 3점 우세를 예상했습니다.",
                "두 팀 모두 4승 2패를 기록 중이며 플레이오프 경쟁에 중요한 승리를 노립니다. 지난 6주차 월요일 경기에서는 샌프란시스코 49ers가 워싱턴을 23-17로 꺾고 유일한 6승 0패 무패 팀으로 남았습니다. 치프스와 바이킹스는 5승 0패를 달리고 있습니다."
            ]
        },
        "ar": {
            "title": "باتريوتس يحل ضيفا على بيرز الليلة: انطلاق الاسبوع 7 في شيكاغو",
            "subtitle": "سولجر فيلد يستضيف مواجهة الخميس الساعة 8:15 مساء بتوقيت الشرق عبر برايم فيديو. كلاهما 4-2.",
            "excerpt": "يبدا الاسبوع 7 من دوري NFL الليلة بمواجهة باتريوتس عند بيرز. شيكاغو مرشحة بفارق 3 نقاط. 49ers يبقى عند 6-0.",
            "body": [
                "يفتتح الاسبوع 7 من دوري NFL يوم الخميس 22 اكتوبر في تمام الساعة 8:15 مساء بتوقيت الشرق في ملعب سولجر فيلد بشيكاغو. يحل نيو انغلاند باتريوتس ضيفا على شيكاغو بيرز عبر برايم فيديو، حيث تضع شبكة ESPN شيكاغو كمرشحة بفارق 3 نقاط.",
                "يدخل الفريقان اللقاء بسجل 4-2 سعيا لتحقيق فوز ثمين في سباق الادوار الاقصائية. وكان الاسبوع السادس قد اختتم بفوز سان فرانسيسكو 49ers بنتيجة 23-17 على كوماندرز ليبقى الفريق الوحيد بسجل 6-0، فيما يواصل تشيفس وفايكنغز سجلهما بـ5-0."
            ]
        }
    },
    "premier-league-thursday-mw8-opens-friday-chelsea-spurs-derby-2026": {
        "fr": {
            "title": "Week-end de derbys : la 8e journee debute vendredi a Portman Road",
            "subtitle": "Ipswich recoit Forest vendredi avant Chelsea face a Tottenham samedi. Manchester City en tete avec 21 points.",
            "excerpt": "La Premier League reprend vendredi avec Ipswich contre Nottingham Forest. Manchester City compte trois points d'avance sur Arsenal.",
            "body": [
                "Les clubs de Premier League ont peaufine leurs preparations jeudi avant la 8e journee. Le bal s'ouvrira vendredi soir 23 octobre a Portman Road avec Ipswich Town accueillant Nottingham Forest a 20:00 UK. Ipswich est 12e avec 8 points apres avoir bouscule Manchester City (3-2) le week-end passe, tandis que Forest pointe au 19e rang avec 5 points.",
                "Le choc du week-end opposera samedi Chelsea a Tottenham a Stamford Bridge. Les Spurs restent sur leur premiere victoire de la saison contre Coventry (3-1) qui les a hisses au 16e rang avec 6 points. Manchester City trone au sommet avec un sans-faute de 21 points en sept matches, trois longueurs devant Arsenal (18) et cinq devant Brighton (16)."
            ]
        },
        "es": {
            "title": "Fin de semana de derbis: la fecha 8 arranca el viernes en Portman Road",
            "subtitle": "Ipswich recibe a Forest el viernes antes del Chelsea contra Tottenham el sabado. El City lidera con 21.",
            "excerpt": "La Premier League regresa el viernes con Ipswich frente a Nottingham Forest. El Manchester City saca tres puntos de ventaja al Arsenal.",
            "body": [
                "Los equipos de la Premier League cerraron sus sesiones tacticas este jueves de cara a la jornada 8. El telon se abre el viernes 23 de octubre en Portman Road, donde el Ipswich Town se mide al Nottingham Forest a las 20:00 UK. El Ipswich ocupa el puesto 12 con 8 puntos, mientras Forest esta en zona de descenso con 5.",
                "El plato fuerte del fin de semana llegara el sabado con el derbi londinense entre Chelsea y Tottenham en Stamford Bridge. Los Spurs llegan con la moral alta tras batir 3-1 al Coventry y situarse 16os con 6 unidades. El Manchester City lidera con 21 puntos perfectos tras siete fechas, escoltado por el Arsenal con 18 y el Brighton con 16."
            ]
        },
        "de": {
            "title": "Derby-Wochenende voraus: Spieltag 8 startet am Freitag an der Portman Road",
            "subtitle": "Ipswich empfaengt Forest am Freitag vor dem Duell Chelsea gegen Spurs am Samstag. Manchester City fuehrt mit 21 Punkten.",
            "excerpt": "Die Premier League startet am Freitag mit Ipswich gegen Nottingham Forest. Manchester City liegt drei Punkte vor Arsenal.",
            "body": [
                "Die Premier-League-Klubs schlossen am Donnerstag ihre Taktikschulungen vor dem 8. Spieltag ab. Das Auftaktspiel steigt am Freitagabend, 23. Oktober, an der Portman Road zwischen Ipswich Town und Nottingham Forest um 20:00 Uhr UK. Ipswich belegt mit 8 Punkten Rang 12, waehrend Forest mit 5 Zaehlern auf Platz 19 im Keller steht.",
                "Der Hoehepunkt folgt am Samstag an der Stamford Bridge beim Londoner Derby zwischen Chelsea und Tottenham Hotspur. Die Spurs schöpften beim 3-1 gegen Coventry neuen Mut und kletterten auf Rang 16 mit 6 Punkten. Manchester City fuehrt das Klassement mit makellosen 21 Punkten aus sieben Siegen an, gefolgt von Arsenal (18) und Brighton (16)."
            ]
        },
        "it": {
            "title": "Weekend di derby: l'ottava giornata scatta venerdi a Portman Road",
            "subtitle": "Ipswich contro Forest venerdi prima del derby Chelsea-Tottenham di sabato. Manchester City primo a 21 punti.",
            "excerpt": "La Premier League riparte venerdi con Ipswich contro Nottingham Forest. Il Manchester City ha tre punti di vantaggio sull'Arsenal.",
            "body": [
                "Le squadre di Premier League hanno completato la preparazione giovedi in vista dell'ottava giornata. Si comincia venerdi 23 ottobre a Portman Road dove l'Ipswich Town ospita il Nottingham Forest alle 20:00 UK. L'Ipswich e dodicesimo a 8 punti, mentre il Forest si trova al diciannovesimo posto a quota 5.",
                "La sfida di cartello andra in scena sabato a Stamford Bridge tra Chelsea e Tottenham Hotspur. Gli Spurs arrivano carichi dopo il 3-1 al Coventry che li ha portati al sedicesimo posto con 6 punti. Il Manchester City guida la classifica a punteggio pieno con 21 punti su 21, inseguito dall'Arsenal a quota 18 e dal Brighton a 16."
            ]
        },
        "pl": {
            "title": "Derbowy weekend: kolejka 8 rusza w piatek na Portman Road",
            "subtitle": "Ipswich podejmie Forest w piatek przed derbami Chelsea ze Spurs w sobote. Manchester City liderem z 21 punktami.",
            "excerpt": "Premier League wznawia rozgrywki w piatek meczem Ipswich z Nottingham Forest. Manchester City ma trzy punkty przewagi nad Arsenalem.",
            "body": [
                "Kluby Premier League zamknely w czwartek przygotowania taktyczne do 8. kolejki. Pierwszy gwizdek rozbrzmi w piatek 23 pazdziernika o 20:00 UK na Portman Road w starciu Ipswich Town z Nottingham Forest. Gospodarze zajmuja 12. miejsce z 8 punktami, a Forest sa na 19. pozycji z 5 punktami.",
                "Hitem kolejki beda sobotnie derby Londynu Chelsea z Tottenhamem na Stamford Bridge. Spurs maja w pamieci wygrana 3-1 z Coventry, ktora dala im 16. miejsce z 6 punktami. Manchester City przewodzi stawce z kompletem 21 punktow po siedmiu meczach, wyprzedzajac Arsenal (18) i Brighton (16)."
            ]
        },
        "zh": {
            "title": "德比周末来袭：英超第8轮周五相约波特曼路",
            "subtitle": "伊普斯维奇周五迎战森林，切尔西对热刺周六打响。曼城7战全胜积21分领跑。",
            "excerpt": "英超第8轮周五由伊普斯维奇对阵诺丁汉森林揭幕。曼城以3分优势领先阿森纳高居榜首。",
            "body": [
                "英超各队周四结束了第8轮的赛前战术演练。本轮将于10月23日周五晚在波特曼路球场开战，由伊普斯维奇主场迎战诺丁汉森林。伊普斯维奇目前积8分排名第12位，森林积5分处于降级区第19位。",
                "周末焦点大战将在周六于斯坦福桥打响，由切尔西迎战热刺。热刺此前3-1击败考文垂积6分升至第16位。瓜迪奥拉率领的曼城以7战全胜积21分的完美战绩领跑积分榜，阿森纳积18分紧随其后，布莱顿积16分位列第三。"
            ]
        },
        "ja": {
            "title": "ダービーの週末へ：第8節は金曜日にポートマン・ロードで開幕",
            "subtitle": "金曜にイプスウィッチ対フォレスト、土曜にチェルシー対スパーズ。マンチェスター・Cが勝ち点21で首位。",
            "excerpt": "プレミアリーグ第8節が金曜日に開幕。首位マンチェスター・シティはアーセナルに勝ち点3差をつけています。",
            "body": [
                "プレミアリーグ各クラブは木曜日に第8節へ向けた戦術確認を終えました。開幕戦は10月23日金曜のポートマン・ロードで行われるイプスウィッチ対ノッティンガム・フォレスト。イプスウィッチは勝ち点8で12位、フォレストは降格圏の19位（勝ち点5）です。",
                "最大の注目カードは土曜日にスタンフォード・ブリッジで行われるチェルシー対トッテナムのロンドン・ダービー。スパーズはコベントリー戦の3-1勝利で勝ち点6の16位へと浮上しました。ペップ率いるマンチェスター・シティは7戦全勝の勝ち点21で首位を守り、アーセナルが18点、ブライトンが16点で追っています。"
            ]
        },
        "ko": {
            "title": "더비 주말 개막: 프리미어리그 8라운드 금요일 포트먼 로드 출발",
            "subtitle": "금요일 입스위치 대 포리스트에 이어 토요일 첼시 대 토트넘 격돌. 맨시티 승점 21점 선두.",
            "excerpt": "프리미어리그 8라운드가 금요일 포트먼 로드에서 열립니다. 맨체스터 시티는 아스널에 승점 3점 차로 앞서 있습니다.",
            "body": [
                "프리미어리그 팀들이 목요일 8라운드를 위한 훈련을 마쳤습니다. 첫 경기는 10월 23일 금요일 포트먼 로드에서 열리는 입스위치 타운 대 노팅엄 포리스트 전입니다. 입스위치는 승점 8점으로 12위, 포리스트는 승점 5점으로 강등권인 19위에 위치해 있습니다.",
                "이번 라운드 최고 빅매치는 토요일 스탬퍼드 브리지에서 열리는 첼시 대 토트넘의 런던 더비입니다. 토트넘은 코번트리전 3-1 승리로 승점 6점을 기록하며 16위로 올라섰습니다. 맨체스터 시티는 7전 전승 승점 21점으로 선두를 달리고 있으며 아스널이 18점, 브라이턴이 16점으로 추격 중입니다."
            ]
        },
        "ar": {
            "title": "عطلة نهاية اسبوع الديربيات: الجولة 8 تفتح الجمعة في بورتمان رود",
            "subtitle": "ابسويتش يستضيف فورست الجمعة قبل قمة تشيلسي وتوتنهام السبت. مانشستر سيتي يتصدر بـ21 نقطة.",
            "excerpt": "تعود منافسات الدوري الممتاز الجمعة بلقاء ابسويتش وفورست. مانشستر سيتي يتفوق بثلاث نقاط على ارسنال.",
            "body": [
                "انهت اندية البريميرليج تحضيراتها يوم الخميس للجولة الثامنة. تفتتح الجولة مساء الجمعة 23 اكتوبر في بورتمان رود حين يستضيف ابسويتش تاون نظيره نوتنغهام فورست. يحتل ابسويتش المركز 12 برصيد 8 نقاط بينما يقبع فورست في المركز 19 برصيد 5 نقاط.",
                "وتتجه الانظار يوم السبت الى ستامفورد بريدج حيث يستضيف تشيلسي غريمه توتنهام هوتسبير. يدخل توتنهام المواجهة بعد فوزه 3-1 على كوفنتري الذي رفعه للمركز 16 برصيد 6 نقاط. ويتصدر مانشستر سيتي بالعلامة الكاملة برصيد 21 نقطة امام ارسنال (18) وبرايتون (16)."
            ]
        }
    },
    "pga-tour-bermuda-round1-opens-at-port-royal-2026": {
        "fr": {
            "title": "Ouverture aux Bermudes : le 1er tour debute a Port Royal",
            "subtitle": "120 joueurs convoitent 500 points FedExCup a Southampton. Adam Schenk defend son titre.",
            "excerpt": "Le Butterfield Bermuda Championship a commence jeudi matin sur la cote atlantique. Le tenant du titre Adam Schenk mene le champ de 120 joueurs.",
            "body": [
                "Le Butterfield Bermuda Championship 2026 a debute jeudi matin 22 octobre sur le parcours de Port Royal a Southampton, aux Bermudes. Les premiers departs ont ete donnes des 7 h 35 locale depuis les tees 1 et 10. Le par 71 dessine par Robert Trent Jones developpe 6 828 yards face aux vents de l'Atlantique.",
                "L'epreuve est dotee de 6 millions de dollars, dont 1,08 million et 500 points FedExCup promis au vainqueur. Golf Channel diffuse les tours chaque jour de 13 h a 16 h ET. Le tenant du titre Adam Schenk tente un double historique, alors que le Canadien Corey Conners (61e mondial) et les amateurs Miles Russell et Mason Howell figurent parmi les engagés."
            ]
        },
        "es": {
            "title": "Arranca en Bermudas: la ronda 1 inicia en Port Royal",
            "subtitle": "120 jugadores buscan 500 puntos FedExCup en Southampton. Adam Schenk defiende la corona.",
            "excerpt": "El Butterfield Bermuda Championship comenzo este jueves junto al Atlantico. El campeon Adam Schenk lidera el field de 120 golfistas.",
            "body": [
                "El Butterfield Bermuda Championship 2026 abrio su primera ronda este jueves 22 de octubre en Port Royal Golf Course en Southampton, Bermudas. Las salidas empezaron a las 7:35 a.m. local por los tees del 1 y del 10. El diseno par 71 de Robert Trent Jones cuenta con 6.828 yardas frente a los vientos marinos.",
                "La bolsa reparte 6 millones de dolares, con 1,08 millones y 500 puntos FedExCup para el campeon. Golf Channel transmite en directo de 1:00 a 4:00 p.m. ET. El defensor del titulo Adam Schenk aspira a repetir triunfo, frente a rivales de la talla de Corey Conners (61 del mundo) y jovenes promesas como Miles Russell."
            ]
        },
        "de": {
            "title": "Auftakt auf Bermuda: Runde 1 startet in Port Royal",
            "subtitle": "120 Profis jagen 500 FedExCup-Punkte in Southampton. Adam Schenk verteidigt seinen Titel.",
            "excerpt": "Die Butterfield Bermuda Championship begann am Donnerstagmorgen an der Kueste. Titelverteidiger Adam Schenk fuehrt das 120-koepfige Feld an.",
            "body": [
                "Die Butterfield Bermuda Championship 2026 startete am Donnerstagmorgen, 22. Oktober, auf dem Port Royal Golf Course in Southampton auf Bermuda. Die ersten Abschlaege erfolgten um 7:35 Uhr Ortszeit von Tee 1 und 10. Der Par-71-Kurs von Robert Trent Jones misst 6.828 Yards entlang der windigen Kueste.",
                "Es geht um ein Preisgeld von 6 Millionen Dollar und 500 FedExCup-Punkte fuer den Sieger. Golf Channel berichtet taeglich von 13:00 bis 16:00 Uhr ET. Titelverteidiger Adam Schenk strebt die erfolgreiche Titelverteidigung an, waehrend der Kanadier Corey Conners als Weltranglisten-61. der Topfavorit ist."
            ]
        },
        "it": {
            "title": "Al via alle Bermuda: scatta il primo giro a Port Royal",
            "subtitle": "120 giocatori a caccia di 500 punti FedExCup a Southampton. Adam Schenk difende il titolo.",
            "excerpt": "Il Butterfield Bermuda Championship e iniziato giovedi mattina sull'Atlantico. Il campione in carica Adam Schenk guida i 120 iscritti.",
            "body": [
                "Il Butterfield Bermuda Championship 2026 ha aperto i battenti giovedi mattina 22 ottobre al Port Royal Golf Course di Southampton, Bermuda. Prime partenze alle 7:35 locali dai tee delle buche 1 e 10. Il percorso par 71 misura 6.828 yard battute dal vento dell'oceano.",
                "In palio un montepremi di 6 milioni di dollari con 1,08 milioni e 500 punti FedExCup per il vincitore. Diretta quotidiana su Golf Channel dalle 13:00 alle 16:00 ET. Il campione in carica Adam Schenk cerca il bis storico contro rivali come il canadese Corey Conners (numero 61 del ranking mondiale)."
            ]
        },
        "pl": {
            "title": "Start na Bermudach: runda 1 rusza w Port Royal",
            "subtitle": "120 graczy walczy o 500 punktow FedExCup w Southampton. Adam Schenk broni tytulu.",
            "excerpt": "Turniej Butterfield Bermuda Championship rozpoczal sie w czwartek rano. Obroncą tytulu jest Adam Schenk w stawce 120 golfistow.",
            "body": [
                "Turniej Butterfield Bermuda Championship 2026 wystartowal w czwartek 22 pazdziernika na polu Port Royal Golf Course w Southampton na Bermudach. Pierwsze grupy wyruszyly o 7:35 czasu lokalnego z dolkow 1 i 10. Pole par 71 liczy 6828 jardow wzdluz wybrzeza Atlantyku.",
                "Pula nagrod wynosi 6 milionow dolarow, w tym 1,08 miliona dolarow oraz 500 punktow rankingowych dla triumfatora. Transmisje na zywo prowadzi Golf Channel w godzinach 13:00-16:00 ET. Tytulu broni Adam Schenk, a najwyzej notowanym uczestnikiem jest Corey Conners (61. na swiecie)."
            ]
        },
        "zh": {
            "title": "百慕大锦标赛启幕：首轮在皇家港正式开杆",
            "subtitle": "120名球员在南安普顿争夺500分联邦快递杯积分。卫冕冠军亚当·申克领衔出战。",
            "excerpt": "百慕大锦标赛周四上午在大西洋海滨球场打响首轮争夺。卫冕冠军亚当·申克率领120人阵容亮相。",
            "body": [
                "2026年百慕大锦标赛于10月22日周四上午在南安普顿的皇家港高尔夫球场正式开杆。球员们自当地时间早晨7:35分别从1号洞和10号洞出发。由罗伯特·特伦特·琼斯设计的标准杆71杆球场全长6828码，受到大西洋海风的严峻考验。",
                "赛事总奖金达600万美元，冠军将独得108万美元与500个联邦快递杯积分。高尔夫频道每天美东时间下午1点至4点进行现场直播。卫冕冠军亚当·申克力争实现该赛事首个连冠，世界排名第61位的加拿大名将科里·康纳斯以及业余新星迈尔斯·拉塞尔也同场竞技。"
            ]
        },
        "ja": {
            "title": "バミューダで開幕：ポートロイヤルで第1ラウンドがスタート",
            "subtitle": "120名の選手が500ポイントのフェデックスカップを狙う。アダム・シェンクが連覇に挑む。",
            "excerpt": "バターフィールド・バミューダ選手権が木曜朝、大西洋岸のコースで開幕。前回覇者アダム・シェンクら120名が出場。",
            "body": [
                "2026年バターフィールド・バミューダ選手権が10月22日木曜の朝、サウサンプトンのポートロイヤル・ゴルフコースで開幕しました。現地時間午前7時35分に1番・10番ティからスタート。ロバート・トレント・ジョーンズ設計のパー71、6,828ヤードのコースは大西洋からの強風が特徴です。",
                "賞金総額600万ドル、優勝賞金108万ドルとフェデックスカップ500ポイントを懸けて争われます。ゴルフチャンネルが東部午後1時から4時に生中継。連覇を目指すアダム・シェンクや世界ランク61位のコーリー・コナーズらが出場しています。"
            ]
        },
        "ko": {
            "title": "버뮤다 개막: 포트 로열에서 1라운드 티오프",
            "subtitle": "120명의 골퍼가 500점의 페덱스컵 포인트를 노립니다. 애덤 솅크 타이틀 방어전.",
            "excerpt": "버터필드 버뮤다 챔피언십이 목요일 아침 대서양 코스에서 시작되었습니다. 디펜딩 챔피언 애덤 솅크가 출격합니다.",
            "body": [
                "2026 버터필드 버뮤다 챔피언십이 10월 22일 목요일 아침 사우샘프턴 포트 로열 골프 코스에서 개막했습니다. 현지 시간 오전 7시 35분 1번과 10번 홀에서 티오프가 시작되었습니다. 파71, 6,828야드 규모의 링크스 스타일 코스는 강한 바닷바람이 승부처입니다.",
                "총상금 600만 달러, 우승 상금 108만 달러와 페덱스컵 포인트 500점이 걸려 있습니다. 골프 채널이 매일 동부 오후 1시부터 4시까지 생중계합니다. 2연패를 노리는 애덤 솅크와 세계랭킹 61위 코리 코너스가 우승 경쟁을 펼칩니다."
            ]
        },
        "ar": {
            "title": "افتتاح بطولة برمودا: انطلاق الجولة الاولى في بورت رويال",
            "subtitle": "120 لاعبا يتنافسون على 500 نقطة لفيديكس كاب في ساوثهامبتون. ادم شينك يدافع عن لقبه.",
            "excerpt": "انطلقت بطولة باترفيلد برمودا صباح الخميس على ساحل الاطلسي بمشاركة 120 لاعبا يتقدمهم حامل اللقب ادم شينك.",
            "body": [
                "افتتحت بطولة باترفيلد برمودا 2026 صباح الخميس 22 اكتوبر في ملعب بورت رويال في ساوثهامبتون ببرمودا. بدأت الضربات الاولى في الساعة 7:35 صباحا بالتوقيت المحلي من الحفرتين 1 و10. يبلغ طول الملعب 6828 ياردة بمعدل 71 ضربة مع رياح بحرية شديدة.",
                "تبلغ الجوائز 6 ملايين دولار، منها 1.08 مليون دولار و500 نقطة كاس فيديكس للبطل. تبث قناة غولف تشانل المنافسات يوميا من 1:00 الى 4:00 مساء بتوقيت الشرق. ويسعى حامل اللقب ادم شينك للفوز مجددا امام كوري كونرز صاحب المركز 61 عالميا."
            ]
        }
    },
    "f1-austin-thursday-media-day-one-day-to-practice-2026": {
        "fr": {
            "title": "Journee medias a Austin : plus qu'un jour avant les essais",
            "subtitle": "Les pilotes s'expriment au COTA. Kimi Antonelli devance George Russell de 102 points.",
            "excerpt": "Les ecuries de Formule 1 ont tenu leurs conferences de presse jeudi a Austin. Les essais libres debutent vendredi avant le Grand Prix dimanche.",
            "body": [
                "Le paddock de Formule 1 a ouvert ses portes jeudi 22 octobre sur le Circuit des Ameriques a Austin, au Texas. Les pilotes ont repondu aux questions des medias sous un ciel ensoleille sur ce trace exigeant de 5,513 km. L'action en piste demarre vendredi avec les Essais Libres 1 et les qualifications Sprint, avant la course dimanche a 15:00 heure locale.",
                "Aucun chrono n'a ete enregistre jeudi. Kimi Antonelli aborde le week-end en solide leader du championnat avec 340 points, fort d'une avance de 102 points sur son coequipier George Russell (238). Chez les constructeurs, Mercedes totalise 578 points contre 444 pour Ferrari. Antonelli dispose au Texas de sa premiere opportunite mathematique de decrocher le titre mondial."
            ]
        },
        "es": {
            "title": "Dia de medios en Austin: queda un dia para los entrenamientos libres",
            "subtitle": "Los pilotos atienden a la prensa en COTA. Kimi Antonelli lidera sobre George Russell por 102 puntos.",
            "excerpt": "Los equipos de Formula 1 celebraron las ruedas de prensa este jueves en Austin. El viernes arrancan las practicas antes del GP del domingo.",
            "body": [
                "El paddock de la Formula 1 cobro vida este jueves 22 de octubre en el Circuito de las Americas en Austin, Texas. Los pilotos cumplieron con los compromisos ante los medios en el trazado de 5,513 km. La actividad en pista comenzara el viernes con los Libres 1 y la clasificacion Sprint, con miras a la carrera del domingo a las 15:00 hora local.",
                "El jueves no se registraron tiempos competitivos. Kimi Antonelli domina el mundial con 340 puntos, 102 por delante de su companero George Russell (238). En constructores, Mercedes lidera con 578 frente a 444 de Ferrari. En Austin, Antonelli dispone de su primera oportunidad matematica de coronarse campeon del mundo si los resultados le favorecen."
            ]
        },
        "de": {
            "title": "Medientag in Austin: Noch ein Tag bis zum ersten Training",
            "subtitle": "Fahrer stellen sich der Presse am COTA. Kimi Antonelli fuehrt mit 102 Punkten vor George Russell.",
            "excerpt": "Die Formel-1-Teams absolvierten am Donnerstag in Austin die Medienrunden. Am Freitag beginnt das Training vor dem GP am Sonntag.",
            "body": [
                "Im Fahrerlager des Circuit of the Americas in Austin erwachte am Donnerstag, 22. Oktober, das Renngeschehen. Die Piloten stellten sich den offiziellen Pressefragen auf dem 5,513 km langen Kurs. Der Fahrbetrieb startet am Freitag mit dem 1. Freien Training und dem Sprint-Qualifying vor dem Grand Prix am Sonntag um 15:00 Uhr Ortszeit.",
                "Am Donnerstag wurden keine gezeiteten Runden absolviert. Mercedes-Junior Kimi Antonelli fuehrt die Weltmeisterschaft mit 340 Punkten an und liegt 102 Zaehler vor Teamkollege George Russell (238). Bei den Konstrukteuren liegt Mercedes mit 578 zu 444 Punkten vor Ferrari. In Austin hat Antonelli die erste rechnerische Chance auf den WM-Titel."
            ]
        },
        "it": {
            "title": "Media day ad Austin: manca un giorno al via delle prove libere",
            "subtitle": "I piloti incontrano la stampa al COTA. Kimi Antonelli guida su George Russell con 102 punti di vantaggio.",
            "excerpt": "I team di Formula 1 hanno aperto il weekend con i briefing giovedi ad Austin. Venerdi scattano le prove prima del Gran Premio domenicale.",
            "body": [
                "Il paddock della Formula 1 si e animato giovedi 22 ottobre al Circuit of the Americas di Austin, in Texas. I piloti hanno risposto alle domande dei media lungo il circuito da 5,513 km. L'azione in pista iniziera venerdi con le Prove Libere 1 e la Sprint Qualifying in vista della gara di domenica alle 15:00 locali.",
                "Nessun tempo cronometrato e stato registrato giovedi. Kimi Antonelli comanda il mondiale con 340 punti, 102 in piu rispetto al compagno di squadra George Russell (238). Nella classifica costruttori la Mercedes domina con 578 punti contro i 444 della Ferrari. In Texas Antonelli ha la prima occasione matematica per chiudere i conti mondiali."
            ]
        },
        "pl": {
            "title": "Dzien mediow w Austin: tylko doba do pierwszych treningow",
            "subtitle": "Kierowcy spotykaja sie z dziennikarzami na COTA. Kimi Antonelli ma 102 punkty przewagi nad George'em Russellem.",
            "excerpt": "Zespoly Formuly 1 zorganizowaly w czwartek konferencje w Austin. W piatek ruszaja treningi przed niedzielnym Grand Prix.",
            "body": [
                "Padok Formuly 1 ozyl w czwartek 22 pazdziernika na Circuit of the Americas w Austin w Teksasie. Kierowcy wypelniali obowiazki medialne przed inauguracja weekendu na torze o dlugosci 5,513 km. Jazdy rozpoczna sie w piatek od 1. treningu i kwalifikacji do sprintu przed niedzielnym wyscigiem o 15:00 czasu lokalnego.",
                "W czwartek bolidy nie wyjezdzaly na tor. Kimi Antonelli jest liderem mistrzostw z dorobkiem 340 punktow, wyprzedzajac kolege z zespolu George'a Russella (238) o 102 punkty. W klasyfikacji konstruktorow Mercedes prowadzi z 578 punktami przed Ferrari (444). W Austin Antonelli ma pierwsza matematyczna szanse na tytul."
            ]
        },
        "zh": {
            "title": "奥斯汀媒体日：距离周五一练仅剩一天",
            "subtitle": "车手在美洲赛道出席新闻发布会。基米·安东内利领先拉塞尔102分。",
            "excerpt": "F1各车队周四在奥斯汀完成媒体通气会。周五正式展开练习赛，周日迎来美国大奖赛正赛。",
            "body": [
                "F1围场于10月22日周四在得克萨斯州奥斯汀的美洲赛道全面运转。车手们在全长5.513公里的赛道旁履行官方媒体采访义务。赛道竞技将于周五由一练和冲刺排位赛拉开序幕，正赛将于周日当地时间15:00开跑。",
                "周四并没有赛车计时圈速。梅赛德斯车手安东内利积340分高居车手榜首，领先队友拉塞尔（238分）达102分。车队积分榜上梅赛德斯以578分领先法拉利的444分。奥斯汀大奖赛是安东内利本赛季首个具备锁定世界冠军理论可能的分站赛。"
            ]
        },
        "ja": {
            "title": "オースティンでメディアデー：金曜フリー走行まであと1日",
            "subtitle": "COTAでドライバーが会見に出席。キミ・アントネッリがラッセルに102点リード。",
            "excerpt": "F1各チームが木曜日にオースティンで公式会見を実施。金曜から走行が始まり日曜の決勝へ向かいます。",
            "body": [
                "10月22日木曜、テキサス州オースティンのサーキット・オブ・ジ・アメリカズでメディアデーが行われました。5.513kmのサーキットで各ドライバーが会見に出席。金曜日にフリー走行1回目とスプリント予選が行われ、日曜現地15:00に56周の決勝レースを迎えます。",
                "木曜日にタイム計測はありません。メルセデスのキミ・アントネッリが340点で首位を守り、ジョージ・ラッセル（238点）に102点差をつけています。コンストラクターズではメルセデスが578点でフェラーリ（444点）をリード。アントネッリには今週末、タイトル確定の理論的な可能性が開かれます。"
            ]
        },
        "ko": {
            "title": "오스틴 미디어 데이: 금요 연습 주행까지 단 하루 남음",
            "subtitle": "COTA에서 드라이버 공식 기자회견 진행. 키미 안토넬리, 조지 러셀에 102점 차 선두.",
            "excerpt": "F1 팀들이 목요일 오스틴에서 미디어 일정을 소화했습니다. 금요일 공식 연습 주행을 시작으로 일요일 결승이 열립니다.",
            "body": [
                "10월 22일 목요일 미국 텍사스주 오스틴의 서킷 오브 디 아메리카스에서 미디어 데이가 열렸습니다. 5.513km 트랙에서 드라이버들은 공식 인터뷰를 진행했습니다. 금요일 연습 주행 1세션과 스프린트 예선으로 본격적인 레이스 주말이 시작되며, 결승은 일요일 현지 15:00에 펼쳐집니다.",
                "목요일에는 공식 랩 타임이 없습니다. 메르세데스의 키미 안토넬리가 340점으로 팀 동료 조지 러셀(238점)에 102점 차 리드를 지키고 있습니다. 컨스트럭터 부문은 메르세데스가 578점으로 페라리(444점)를 앞서고 있습니다. 안토넬리는 이번 오스틴에서 첫 월드 챔피언 확정 가능성을 맞이합니다."
            ]
        },
        "ar": {
            "title": "اليوم الاعلامي في اوستن: يوم واحد يفصلنا عن تجارب الجمعة",
            "subtitle": "السائقون يواجهون وسائل الاعلام في حلبة الامريكتين. كيمي انتونيللي يتقدم بـ102 نقطة على جورج راسل.",
            "excerpt": "عقدت فرق الفورمولا 1 مؤتمراتها الاعلامية الخميس في اوستن. تبدا التجارب الجمعة قبل سباق الاحد الكبير.",
            "body": [
                "عادت اجواء الاثارة يوم الخميس 22 اكتوبر في حلبة الامريكتين باوستن في تكساس مع انطلاق اليوم الاعلامي الرسمي للسائقين على المسار البالغ 5.513 كم. تبدا المنافسات على ارض الحلبة يوم الجمعة بالتجارب الحرة الاولى وتصفيات السبرينت قبل السباق الرئيسي الاحد الساعة 15:00 بالتوقيت المحلي.",
                "لم تسجل اي ازمنة رسمية يوم الخميس. يتصدر كيمي انتونيللي بطولة العالم للسائقين برصيد 340 نقطة بفارق 102 نقطة عن زميله جورج راسل (238). وتتصدر مرسيدس بطولة الصانعين بـ578 نقطة امام فيراري (444). يملك انتونيللي في اوستن اولى فرصه الحسابية لحسم اللقب العالمي."
            ]
        }
    }
}

# Verify no em-dash or double-hyphen
for slug, langs in OCT22_STORIES.items():
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

snippet_parts = []
for slug, langs in OCT22_STORIES.items():
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

print("Successfully injected October 22 translations into frontend/src/i18n/stories.ts")
