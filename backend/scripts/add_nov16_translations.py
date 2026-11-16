"""Inject all 9-locale translations for the 6 stories on 2026-11-16 into stories.ts."""
import os
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
STORIES_TS = os.path.join(ROOT, "frontend", "src", "i18n", "stories.ts")

nov16_translations = {
  "nations-league-england-stun-spain-in-madrid-kane-konsa-2026": {
    "fr": {
      "title": "L'Angleterre cree la sensation contre l'Espagne (3-2) a Madrid et remporte le Groupe A3",
      "subtitle": "Harry Kane, Ezri Konsa et Ben White donnent trois buts d'avance avant que les Three Lions reduits a dix ne resistent au retour espagnol pour stopper une serie de 43 matchs sans defaite.",
      "excerpt": "L'Angleterre s'impose 3-2 face a l'Espagne au Metropolitano malgre le carton rouge d'Elliot Anderson et s'empare de la premiere place du Groupe A3.",
      "body": [
        "L'Angleterre a signe un exploit retentissant dimanche 15 novembre en dominant l'Espagne 3-2 devant 63 788 spectateurs au Riyadh Air Metropolitano de Madrid. Ce succes magistral met un terme a l'incroyable serie de 43 matchs d'invincibilite de la Roja en competition officielle et hisse les hommes de Thomas Tuchel en tete du Groupe A3 de la Ligue des Nations.",
        "Le capitaine Harry Kane a debloque la partie juste avant la pause en transformant sereinement un penalty a la 45e minute pour sa 73e realisation internationale. Au retour des vestiaires, Ezri Konsa a double la mise d'une tete sur corner (53e), avant que Ben White ne conclue une contre-attaque eclair a la 58e pour porter le score a 3-0.",
        "Les champions d'Europe espagnols ont replique avec un penalty de Mikel Oyarzabal (65e) et une superbe finition de Nico Williams (75e). Malgre l'expulsion d'Elliot Anderson a la 84e minute, Jordan Pickford a realise deux parades decisives dans le temps additionnel pour valider la victoire et le statut de tete de serie en quarts de finale."
      ]
    },
    "es": {
      "title": "Inglaterra sorprende a Espana 3-2 en Madrid y conquista la cima del Grupo A3",
      "subtitle": "Harry Kane, Ezri Konsa y Ben White ponen el 3-0 y los Tres Leones resisten con diez jugadores la reaccion de la Roja para romper su racha de 43 partidos invicta.",
      "excerpt": "Inglaterra logra una historica victoria 3-2 sobre Espana en el Metropolitano, sobreponiendose a la roja de Elliot Anderson para asegurar el primer puesto del Grupo A3.",
      "body": [
        "Inglaterra firmo una actuacion historica este domingo 15 de noviembre al vencer 3-2 a la campeona de Europa Espana ante 63.788 aficionados en el Riyadh Air Metropolitano de Madrid. El triunfo puso fin a una impresionante racha espanola de 43 partidos invicta en competiciones oficiales que se remontaba a marzo de 2023.",
        "El capitan Harry Kane abrio la cuenta al borde del descanso transformando con serenidad un penalti en el minuto 45 para su gol internacional numero 73. Ezri Konsa cabeceo un saque de esquina en el 53 y Ben White finalizo un contragolpe fulgurante en el 58 para poner una ventaja de 3-0 que parecia definitiva.",
        "Espana reacciono con garra gracias a un penalti de Mikel Oyarzabal en el minuto 65 y un gran gol de Nico Williams en el 75. Pese a la expulsion de Elliot Anderson en el 84, Inglaterra resistio con diez hombres gracias a dos paradas providenciales de Jordan Pickford en el alargue, asegurando la condicion de cabeza de serie en cuartos de final."
      ]
    },
    "de": {
      "title": "England schockt Spanien mit 3:2-Triumph in Madrid und holt Gruppensieg in der Nations League",
      "subtitle": "Kane, Konsa und White schiessen die Three Lions mit 3:0 in Fuehrung, ehe England in Unterzahl dem spanischen Sturmlauf trotzt und Spaniens Serie nach 43 Spielen beendet.",
      "excerpt": "England bezwingt Europameister Spanien mit 3:2 im Metropolitano und sichert sich trotz Roter Karte fuer Elliot Anderson Platz eins in der Gruppe A3.",
      "body": [
        "England feierte am Sonntag, 15. November, einen historischen 3:2-Erfolg ueber Europameister Spanien vor 63.788 Zuschauern im Riyadh Air Metropolitano in Madrid. Damit endete Spaniens bemerkenswerte Serie von 43 ungeschlagenen Pflichtspielen in Serie, waehrend die Elf von Thomas Tuchel Platz eins in der Nations-League-Gruppe A3 eroberte.",
        "Kapitaen Harry Kane eroeffnete kurz vor der Pause per Foulelfmeter (45.) mit seinem 73. Laenderspieltor den Torreigen. Ezri Konsa erhoehte per Kopf nach einer Ecke (53.), ehe Ben White nach einem Konter in der 58. Minute das sensationelle 3:0 erzielte.",
        "Spanien kaempfte sich durch einen Elfmeter von Mikel Oyarzabal (65.) und ein Tor von Nico Williams (75.) heran. Obwohl Elliot Anderson in der 84. Minute die Rote Karte sah, hielten die Gaeste mit zehn Mann und zwei Glanzparaden von Jordan Pickford in der Nachspielzeit den wertvollen Auswaertssieg fest."
      ]
    },
    "it": {
      "title": "L'Inghilterra batte la Spagna 3-2 a Madrid e conquista il primato nel Gruppo A3",
      "subtitle": "Harry Kane, Ezri Konsa e Ben White firmano il tris inglese, poi gli uomini di Tuchel resistono in dieci alla rimonta delle Furie Rosse interrompendo una serie di 43 gare di imbattibilita.",
      "excerpt": "Grande impresa dei Tre Leoni che superano la Spagna 3-2 al Metropolitano resistendo in dieci dopo il rosso ad Anderson e chiudono al primo posto il girone.",
      "body": [
        "L'Inghilterra ha compiuto una memorabile impresa domenica 15 novembre, superando i campioni d'Europa della Spagna per 3-2 davanti a 63.788 tifosi al Riyadh Air Metropolitano di Madrid. Il risultato ha interrotto la striscia di 43 partite ufficiali senza sconfitte della Roja e garantito all'Inghilterra la testa di serie nei quarti di Nations League.",
        "Harry Kane ha sbloccato il risultato allo scadere del primo tempo realizzando un calcio di rigore al 45' per il suo 73esimo gol in nazionale. Nella ripresa Ezri Konsa ha raddoppiato di testa al 53' e Ben White ha finalizzato un contropiede perfetto al 58' per il clamoroso 3-0.",
        "La Spagna ha accorciato con il rigore di Mikel Oyarzabal al 65' e la rete di Nico Williams al 75'. Nonostante l'espulsione diretta di Elliot Anderson all'84', l'Inghilterra ha difeso il vantaggio con dieci uomini grazie a due interventi decisivi di Jordan Pickford nei minuti di recupero."
      ]
    },
    "pl": {
      "title": "Anglia szokuje Hiszpanie wygrana 3:2 w Madrycie i wygrywa grupe A3 Ligi Narodow",
      "subtitle": "Kane, Konsa i White dali prowadzenie 3:0, po czym grajaca w dziesiatke ekipa Tuchela obronila przewage, przerywajac serie 43 meczow Hiszpanii bez porazki.",
      "excerpt": "Anglia odnosi spektakularne zwyciestwo 3:2 nad mistrzami Europy w Madrycie i pomimo czerwonej kartki dla Andersona pieczetuje pierwsze miejsce w grupie A3.",
      "body": [
        "Anglia odniosla historyczne zwyciestwo w niedziele 15 listopada, pokonujac mistrzow Europy Hiszpanie 3:2 przed 63 788 widzami na Riyadh Air Metropolitano w Madrycie. Wygrana zakonczyla niesamowita serie 43 meczow o punkty z rzedu bez porazki La Roja i dala druzynie Thomasa Tuchela pierwsze miejsce w grupie A3.",
        "Kapitan Harry Kane otworzyl wynik w 45. minucie pewnym strzalem z rzutu karnego, zdobywajac swoja 73. bramke w kadrze. Po przerwie Ezri Konsa podwyzszyl strzalem glowa (53.), a Ben White wykonczyl kontratak w 58. minucie na 3:0.",
        "Gospodarze odpowiedzieli rzutem karnym Mikela Oyarzabala w 65. minucie i trafieniem Nico Williamsa w 75. minucie. Mimo czerwonej kartki dla Elliota Andersona w 84. minucie, Anglia przetrwala napór rywali dzieki dwom swietnym obronom Jordana Pickforda w doliczonym czasie gry."
      ]
    },
    "zh": {
      "title": "英格兰在马德里3比2力克西班牙，终结对手43场不败并锁定欧国联小组头名",
      "subtitle": "哈里·凯恩、孔萨与本·怀特建功确立三球领先，十人三狮军团顶住斗牛士军团最后反扑锁定胜局。",
      "excerpt": "英格兰在客场3比2力克欧洲冠军西班牙，顶住埃利奥特·安德森染红压力，夺得欧国联A3组第一名种子席位。",
      "body": [
        "英格兰队于11月15日周日晚在马德里大都会球场创造历史，在63788名观众见证下以3比2客场力克欧洲冠军西班牙。此役不仅终结了西班牙队长达43场各项正式比赛不败的辉煌纪录，还让图赫尔执教的英格兰反超对手斩获欧国联A3组头名。",
        "队长哈里·凯恩在第45分钟点球破门打破僵局，斩获个人第73粒国家队进球。下半场孔萨在第53分钟利用角球头槌破网，本·怀特在第58分钟反击推射得手，英格兰不可思议地取得3比0领先。",
        "西班牙队绝地反击，奥亚萨瓦尔第65分钟罚入点球，尼科·威廉姆斯第75分钟低射扳回一城。英格兰中场安德森在第84分钟领到红牌被罚出场，但门将皮克福德在补时阶段奉献两次神勇扑救，守住这场荡气回肠的3比2客胜。"
      ]
    },
    "ja": {
      "title": "イングランドがマドリードでスペインを3-2で撃破、公式戦43戦不敗を止めA3組首位通過",
      "subtitle": "ハリー・ケイン、コンサ、ホワイトのゴールで3点リードを奪い、アンダーソン退場後も猛攻をしのぎきり歴史的勝利。",
      "excerpt": "イングランドが大都会メトロポリターノで欧州王者スペインに3-2で勝利。数的不利を耐えてネーションズリーグA3組首位を奪取した。",
      "body": [
        "イングランド代表は11月15日日曜日、マドリードのリアド・エア・メトロポリターノで欧州王者スペインを3-2で下す大金星を挙げました。これにより2023年3月以来続いていたスペインの公式戦43試合無敗記録がストップし、トーマス・トゥヘル率いるイングランドがネーションズリーグA3組の首位シードを確定させました。",
        "前半終了間際の45分、主将ハリー・ケインがPKを冷静に沈めて代表通算73点目をマーク。後半立ち上がりの53分にエズリ・コンサがCKからヘディングを決め、58分にはベン・ホワイトが電光石火のカウンターを完結させて3-0とリードを広げました。",
        "スペインも65分にオヤルサバルのPK、75分にニコ・ウィリアムズのゴールで1点差に迫り、84分にはイングランドのエリオット・アンダーソンが一発退場。10人となったアウェイチームでしたが、GKピックフォードがアディショナルタイムにスーパーセーブを連発して逃げ切りました。"
      ]
    },
    "ko": {
      "title": "잉글랜드, 마드리드서 스페인 3-2 격파하고 43경기 무패 행진 저지 및 조 1위 확보",
      "subtitle": "해리 케인, 콘사, 벤 화이트의 연속골로 3-0 리드 후 퇴장 악재 속에서도 스페인의 맹추격을 뿌리치고 승리.",
      "excerpt": "잉글랜드가 메트로폴리타노에서 스페인을 3-2로 제압하며 43경기 연속 무패를 마감시키고 네이션스리그 A3조 1위를 확정 지었다.",
      "body": [
        "잉글랜드가 11월 15일 일요일 마드리드의 리야드 에어 메트로폴리타노에서 63,788명의 관중이 지켜보는 가운데 유럽 챔피언 스페인을 3-2로 꺾는 대이변을 연출했습니다. 스페인의 공식전 43경기 연속 무패 행진이 멈췄으며 토마스 투헬 감독의 잉글랜드는 네이션스리그 A3조 1위로 8강 시드를 따냈습니다.",
        "전반 45분 주장 해리 케인이 페널티킥을 침착하게 성공시키며 A매치 73호 골을 기록했습니다. 후반 53분 수비수 에즈리 콘사가 코너킥 헤더로 격차를 벌렸고, 58분 벤 화이트가 번개 같은 역습을 마무리해 3-0을 만들었습니다.",
        "스페인은 오야르사발(65분 PK)과 니코 윌리엄스(75분)의 골로 턱밑까지 추격했고 84분 엘리엇 앤더슨이 다이렉트 퇴장을 당해 수적 우위까지 점했습니다. 하지만 조던 픽포드 골키퍼가 추가시간 결정적인 선방 두 개를 기록하며 3-2 귀중한 승리를 지켜냈습니다."
      ]
    },
    "ar": {
      "title": "إنجلترا تصعق إسبانيا بنتيجة 3-2 في مدريد وتنتزع صدارة المجموعة الثالثة بدوري الأمم",
      "subtitle": "هاري كين وإزري كونسا وبن وايت يتقدمون بثلاثية قبل أن يصمد الإنجليز بعشرة لاعبين أمام انتفاضة لا روخا وينهون سلسلة 43 مباراة بلا هزيمة.",
      "excerpt": "إنجلترا تحقق فوزاً تاريخياً 3-2 على بطلة أوروبا إسبانيا في ملعب ميتروبوليتانو وتتأهل كمتصدرة للمجموعة الثالثة بدوري الأمم الأوروبية.",
      "body": [
        "حققت إنجلترا انتصاراً تاريخياً مساء الأحد 15 نوفمبر بعدما أسقطت بطلة أوروبا إسبانيا بنتيجة 3-2 أمام 63,788 متفرجاً على ملعب رياض إير ميتروبوليتانو في مدريد. ووضعت النتيجة حداً لسلسلة لا روخا القياسية في 43 مباراة رسمية متتالية بلا هزيمة، لتنتزع كتيبة توماس توخيل صدارة المجموعة الثالثة بالمستوى الأول لدوري الأمم الأوروبية.",
        "افتتح القائد هاري كين التسجيل في الدقيقة 45 من ركلة جزاء محكماً هدفه الدولي رقم 73 في مباراته رقم 126. ومع بداية الشوط الثاني ضاعف إزري كونسا النتيجة بضربة رأسية في الدقيقة 53، قبل أن يضيف بن وايت الهدف الثالث من هجمة مرتدة خاطفة بالدقيقة 58.",
        "عادت إسبانيا بهدفين عبر ركلة جزاء لميكيل أويارزابال بالدقيقة 65 وهدف رائع لنيكو ويليامز بالدقيقة 75. وتعرض إليوت أندرسون للطرد المباشر في الدقيقة 84، لتلعب إنجلترا بعشرة لاعبين، إلا أن تألق الحارس جوردان بيكفورد في الوقت بدل الضائع حافظ على الانتصار الثمين."
      ]
    }
  },
  "nfl-mnf-harbaugh-bowl-chargers-ravens-lions-rout-in-munich-2026": {
    "fr": {
      "title": "Le Harbaugh Bowl en vedette du Monday Night alors que Detroit fete son succes 35-10 a Munich",
      "subtitle": "Jim et John Harbaugh s'affrontent a Baltimore, au lendemain du festival des Lions a l'Allianz Arena porte par les 252 yards de Jahmyr Gibbs.",
      "excerpt": "Le Monday Night Football met aux prises les Chargers et les Ravens dans le duel familial Harbaugh, tandis que Detroit passe a 7-2 apres sa victoire nette a Munich.",
      "body": [
        "L'affiche du Monday Night Football s'installe a Baltimore ce lundi 16 novembre avec les retrouvailles des freres Jim et John Harbaugh, opposant les Chargers de Los Angeles (6-3) aux Ravens de Baltimore (7-2) au M&T Bank Stadium. Il s'agit de leur premier face-a-face depuis le Super Bowl XLVII, avec un enjeu capital pour le classement AFC.",
        "La defense hermetique des Chargers menee par Joey Bosa et Derwin James (14,8 points encaisses par match) defie le double MVP Lamar Jackson et le puissant running back Derrick Henry. Justin Herbert compte sur l'attaque au sol de Jim Harbaugh pour creer la surprise a l'exterieur.",
        "Cette affiche fait suite au triomphe de Detroit dimanche a Munich, ou 70 225 supporters ont vu les Lions ecraser les Patriots 35-10. Jahmyr Gibbs a totalise 252 yards et deux touchdowns, pendant que Jared Goff lancait trois passes de touchdown dont deux pour Amon-Ra St. Brown. Sorti sur blessure a la cheville au premier quart-temps, Drake Maye laisse New England a 5-5."
      ]
    },
    "es": {
      "title": "El Harbaugh Bowl ilumina el Monday Night tras la aplastante victoria de Lions 35-10 en Munich",
      "subtitle": "Jim y John Harbaugh se miden en Baltimore en plena carrera de playoffs de la AFC, mientras Detroit celebra un festival de 252 yardas de Jahmyr Gibbs en Alemania.",
      "excerpt": "El Monday Night Football presenta a Chargers y Ravens en el Harbaugh Bowl tras la exhibicion de los Lions de Detroit 35-10 sobre Patriots en el Allianz Arena.",
      "body": [
        "El espectaculo de la NFL aterriza en Baltimore este lunes 16 de noviembre con el esperado duelo entre los hermanos Jim y John Harbaugh en Monday Night Football, donde Los Angeles Chargers (6-3) visitan a los Baltimore Ravens (7-2) en el M&T Bank Stadium.",
        "Los Chargers de Jim Harbaugh poseen la tercera mejor defensa de la liga con solo 14,8 puntos permitidos por encuentro, liderada por Joey Bosa y Derwin James. Frente a ellos estaran Lamar Jackson y Derrick Henry en una ofensiva que promedia 29,4 puntos y busca imponer su ley como local.",
        "La accion del lunes sigue al espectacular partido internacional del domingo en Munich, donde 70.225 aficionados presenciaron la victoria de Detroit Lions 35-10 sobre New England Patriots. Jahmyr Gibbs firmo 252 yardas de ataque y dos touchdowns, Jared Goff lanzo para tres anotaciones y Drake Maye sufrio una lesion de tobillo en la primera mitad."
      ]
    },
    "de": {
      "title": "Harbaugh Bowl im Fokus am Monday Night nach Detroits 35:10-Gala in Muenchen",
      "subtitle": "Jim und John Harbaugh kaempfen in Baltimore um die AFC-Playoff-Positionen, nachdem Jahmyr Gibbs mit 252 Yards die Lions in der Allianz Arena zum Sieg fuehrte.",
      "excerpt": "Monday Night Football praesentiert das Bruder-Duell Chargers gegen Ravens, waehrend Detroit nach dem 35:10 ueber die Patriots in Muenchen bei 7-2 steht.",
      "body": [
        "Am Montagabend, 16. November, blickt die NFL nach Baltimore zum prestigetraechtigen Monday Night Football, wenn Jim Harbaughs Los Angeles Chargers (6-3) bei John Harbaughs Baltimore Ravens (7-2) im M&T Bank Stadium gastieren.",
        "Die Chargers reisen mit der drittbesten Defensive der Liga (14,8 zugelassene Punkte pro Spiel) an, um gegen den zweifachen MVP Lamar Jackson und Runningback Derrick Henry zu bestehen. Es ist das erste Aufeinandertreffen der Harbaugh-Brueder seit dem Super Bowl XLVII.",
        "Zuvor begeisterten die Detroit Lions am Sonntag 70.225 Zuschauer in der Muenchner Allianz Arena mit einem dominanten 35:10-Sieg ueber die New England Patriots. Jahmyr Gibbs glaenzte mit 252 Scrimmage-Yards und zwei Touchdowns, Jared Goff warf drei Touchdowns (zwei auf Amon-Ra St. Brown), waehrend Patriots-Quarterback Drake Maye mit einer Knoechelverletzung frueh ausschied."
      ]
    },
    "it": {
      "title": "Harbaugh Bowl protagonista del Monday Night dopo il netto 35-10 dei Lions a Monaco",
      "subtitle": "Jim e John Harbaugh si sfidano a Baltimora per la corsa playoff AFC, all'indomani dello show di Jahmyr Gibbs da 252 yard all'Allianz Arena.",
      "excerpt": "Il Monday Night Football propone il duello Chargers-Ravens tra i fratelli Harbaugh, mentre Detroit sale a 7-2 dopo il successo per 35-10 su New England a Monaco.",
      "body": [
        "La scena NFL si sposta a Baltimora questo lunedi 16 novembre per un imperdibile Monday Night Football tra i Los Angeles Chargers (6-3) e i Baltimore Ravens (7-2) all'M&T Bank Stadium, prima sfida tra i fratelli Jim e John Harbaugh dal Super Bowl XLVII.",
        "La solida difesa dei Chargers (appena 14,8 punti concessi a partita) affronta Lamar Jackson e Derrick Henry in una sfida ad altissima intensita fisica con enormi ripercussioni sulla griglia playoff dell'AFC.",
        "La partita chiude il decimo turno dopo la splendida domenica all'Allianz Arena di Monaco, dove 70.225 spettatori hanno applaudito il trionfo dei Detroit Lions per 35-10 sui New England Patriots. Jahmyr Gibbs ha incantato con 252 yard totali e due mete, Jared Goff ha lanciato tre passaggi da touchdown e il rookie dei Patriots Drake Maye si e infortunato alla caviglia nel primo quarto."
      ]
    },
    "pl": {
      "title": "Harbaugh Bowl w centrum uwagi Monday Night po triumfie Lions 35:10 w Monachium",
      "subtitle": "Jim i John Harbaugh staja naprzeciw siebie w Baltimore, podczas gdy Detroit swietuje efektowne zwyciestwo nad Patriots dzieki 252 jardom Jahmyra Gibbsa.",
      "excerpt": "Monday Night Football przynosi starcie Chargers z Ravens w Harbaugh Bowl, a Detroit poprawia bilans na 7-2 po rozbiciu Patriots 35:10 na Allianz Arena.",
      "body": [
        "W poniedzialkowy wieczor 16 listopada oczy kibicow NFL zwrocone sa na Baltimore, gdzie w ramach Monday Night Football zmierza sie Los Angeles Chargers (6-3) i Baltimore Ravens (7-2) w pojedynku braci Jima i Johna Harbaugh.",
        "Swietna defensywa Chargers (trzecia w lidze ze srednia 14,8 punktu) prowadzona przez Joeya Bose stanie przed wyzwaniem zatrzymania dwukrotnego MVP Lamara Jacksona i poteznego Derricka Henry'ego.",
        "Mecz ten zwienczy kolejke po niedzielnym widowisku w Monachium, gdzie 70 225 kibicow na Allianz Arena ogladalo zwyciestwo Detroit Lions nad New England Patriots 35:10. Jahmyr Gibbs zdobyl 252 jardy i dwa przylozenia, Jared Goff rzucil trzy podania na punkty, a rozgrywajacy Patriots Drake Maye musial opuscic boisko z kontuzja kostki."
      ]
    },
    "zh": {
      "title": "哈博兄弟对决领衔周一夜赛，底特律雄狮在慕尼黑35比10大胜爱国者",
      "subtitle": "吉姆与约翰·哈博在巴尔的摩争夺美联季后赛身位，此前吉布斯轰下252码助雄狮在安联球场狂胜。",
      "excerpt": "周一夜赛上演充电器对决乌鸦的哈博兄弟德比；此前雄狮在慕尼黑安联球场35比10痛击爱国者，战绩升至7胜2负。",
      "body": [
        "NFL第10周焦点移师巴尔的摩，吉姆·哈博率领的洛杉矶充电器（6胜3负）与约翰·哈博执教的巴尔的摩乌鸦（7胜2负）在M&T银行球场上演备受瞩目的哈博德比，这是兄弟俩自第47届超级碗以来的首次交锋。",
        "充电器队携全联盟场均仅失14.8分的铁血防守出征，迎战由两届MVP拉马尔·杰克逊与跑卫德里克·亨利坐镇、场均轰下29.4分的乌鸦进攻组，比赛极具季后赛关键卡位意义。",
        "在周日的慕尼黑国际赛上，底特律雄狮在安联球场70225名观众面前以35比10横扫新英格兰爱国者。跑卫吉布斯狂砍252码并收获两记达阵，高夫传出3次达阵，爱国者四分卫梅耶则在首节因脚踝受伤遗憾退场。"
      ]
    },
    "ja": {
      "title": "ハーボー兄弟対決がマンデーナイトを席巻、ライオンズはミュンヘンで35-10の大勝",
      "subtitle": "ジムとジョンのハーボー兄弟がボルティモアで激突。ミュンヘンではジャミール・ギブスが252ヤードを稼ぎライオンズが圧勝。",
      "excerpt": "マンデーナイトでチャージャーズ対レイブンズのハーボー対決が開幕。ミュンヘンではライオンズがペイトリオッツを35-10で粉砕した。",
      "body": [
        "11月16日月曜夜のNFLは、ボルティモアのM&Tバンク・スタジアムでジム・ハーボー率いるロサンゼルス・チャージャーズ（6勝3敗）とジョン・ハーボー率いるボルティモア・レイブンズ（7勝2敗）が激突する注目のマンデーナイトです。",
        "チャージャーズのリーグ屈指の堅守（平均失点14.8）が、2度のMVPラマー・ジャクソンと剛腕デリック・ヘンリー擁するレイブンズの爆発的攻撃陣に挑みます。",
        "一方、日曜日にドイツのアリアンツ・アレーナで行われた公式戦では、デトロイト・ライオンズが70,225人の大観衆の前でペイトリオッツを35-10で一蹴。ジャミール・ギブスがランとパスで計252ヤード、2TDの大活躍を見せ、ペイトリオッツのドレイク・メイは足首負傷で途中退場しました。"
      ]
    },
    "ko": {
      "title": "하버 형제 매치 먼데이 나이트 장식, 라이언스는 뮌헨에서 35-10 대승 축제",
      "subtitle": "볼티모어에서 짐과 존 하버 감독이 맞붙는 가운데, 디트로이트는 깁스의 252야드 맹활약으로 페이트리어츠 완파.",
      "excerpt": "먼데이 나이트 풋볼에서 차저스와 레이븐스가 격돌하며, 디트로이트 라이언스는 뮌헨 알리안츠 아레나에서 뉴잉글랜드를 35-10으로 제압했다.",
      "body": [
        "11월 16일 월요일 밤 NFL은 볼티모어 M&T 뱅크 스타디움에서 짐 하버의 LA 차저스(6승 3패)와 존 하버의 볼티모어 레이븐스(7승 2패)가 맞붙는 하버 볼로 뜨겁게 달아오릅니다. 제47회 슈퍼볼 이후 처음 성사된 형제 감독 맞대결입니다.",
        "경기당 14.8실점에 불과한 차저스의 짠물 수비가 라마 잭슨과 데릭 헨리가 이끄는 볼티모어의 막강한 화력을 시험하게 됩니다.",
        "앞서 일요일 뮌헨 알리안츠 아레나에서 열린 정규시즌 경기에서는 디트로이트 라이언스가 뉴잉글랜드 페이트리어츠를 35-10으로 대파했습니다. 러닝백 자미어 깁스가 252야드 2터치다운을 기록했고, 페이트리어츠 쿼터백 드레이크 메이는 1쿼터 발목 부상으로 이탈했습니다."
      ]
    },
    "ar": {
      "title": "نزال الإخوة هاربوه يسرق أضواء مانداي نايت بعد سحق ديترويت لنيو إنجلاند 35-10 في ميونخ",
      "subtitle": "جيم وجون هاربوه يتواجهان في بالتيمور لتحديد مسار البلاي أوف، بينما احتفلت جماهير أليانز أرينا بتألق جيبس بـ252 ياردة.",
      "excerpt": "مانداي نايت فوتبول يشهد صدام تشارجرز وريفنز في نزال عائلة هاربوه، وديترويت يعزز سجله إلى 7-2 بعد اكتساح باتريوتس في ميونخ.",
      "body": [
        "تتجه أنظار دوري كرة القدم الأمريكية NFL مساء الاثنين 16 نوفمبر إلى بالتيمور، حيث يلتقي لوس أنجلوس تشارجرز بقيادة جيم هاربوه مع بالتيمور ريفنز بقيادة شقيقه جون هاربوه في قمة مانداي نايت فوتبول على ملعب M&T بنك.",
        "وتدخل دفاعات تشارجرز القوية التي تستقبل 14.8 نقطة فقط في المباراة اختباراً حاسماً أمام أفضل لاعب مرتين لامار جاكسون والعملاق ديريك هنري في صراع محموم على صدارة التصنيف في القسم الأمريكي AFC.",
        "ويأتي اللقاء بعد الأحد المثير في ميونخ الألمانية، حيث دك ديترويت لايونز شباك نيو إنجلاند باتريوتس بنتيجة 35-10 أمام 70,225 متفرجاً في أليانز أرينا، بفضل تألق جاهيمير جيبس بـ252 ياردة وهبوطين، بينما غادر دريك ماي مصاباً في الكاحل."
      ]
    }
  },
  "nba-spurs-extend-streak-to-12-wembanyama-harper-top-jazz-2026": {
    "fr": {
      "title": "Les Spurs portent leur serie a 12 victoires : Wembanyama et Harper dominent le Jazz 110-102",
      "subtitle": "Victor Wembanyama cumule 26 points, 11 rebonds et 5 contres tandis que Dylan Harper enfile 31 points pour maintenir San Antonio au sommet.",
      "excerpt": "San Antonio poursuit son debut de saison historique en s'imposant 110-102 dans l'Utah avec 18 points de Dylan Harper dans le dernier quart-temps.",
      "body": [
        "Les San Antonio Spurs ont prolonge dimanche 15 novembre leur depart sensationnel en signant une 12e victoire d'affilee, s'imposant 110-102 sur le parquet du Utah Jazz au Delta Center. Avec un bilan de 12 victoires pour une seule defaite, San Antonio s'affirme comme l'equipe phare de ce debut de saison NBA.",
        "Victor Wembanyama a livre une partition complete avec 26 points, 11 rebonds, 6 passes decisives et 5 contres en 34 minutes. Le prodige francais a verrouille la raquette tout en sanctionnant a trois points avec trois tirs primes reussis.",
        "Dans le money-time, c'est le rookie de 20 ans Dylan Harper qui a fait basculer la rencontre en inscrivant 31 points, dont 18 dans un quatrieme quart-temps incandescent. Mo Bamba a inscrit 26 points pour Utah, mais le Jazz a cede face au sang-froid des Spurs dans les trois dernieres minutes."
      ]
    },
    "es": {
      "title": "Los Spurs elevan su racha a 12 victorias: Wembanyama y Harper vencen a Jazz 110-102",
      "subtitle": "Victor Wembanyama aporta 26 puntos, 11 rebotes y 5 tapones mientras Dylan Harper suma 31 para mantener a San Antonio en lo mas alto de la NBA.",
      "excerpt": "San Antonio alarga a 12 su racha de triunfos consecutivos tras derrotar 110-102 a Utah con 18 puntos decisivos de Harper en el ultimo cuarto.",
      "body": [
        "Los San Antonio Spurs extendieron su impresionante inicio de campana el domingo 15 de noviembre al lograr su duodecima victoria consecutiva, imponiendose 110-102 en la pista de Utah Jazz en el Delta Center para colocar su registro en un imponente 12-1.",
        "Victor Wembanyama firmo una actuacion monumental con 26 puntos, 11 rebotes, 6 asistencias y 5 tapones en 34 minutos. La estrella francesa dicto el ritmo defensivo y sumo tres triples para abrir la defensa mormona.",
        "El golpe de gracia lo dio el novato Dylan Harper, quien alcanzo el tope de su carrera con 31 puntos, 18 de ellos en un ultimo cuarto sensacional con 7 de 9 en tiros. Pese a los 26 puntos de Mo Bamba para Utah, San Antonio liquido el encuentro con un parcial demoledor."
      ]
    },
    "de": {
      "title": "Spurs bauen Siegesserie auf 12 Spiele aus: Wembanyama und Harper bezwingen Jazz 110:102",
      "subtitle": "Victor Wembanyama glaenzt mit 26 Punkten, 11 Rebounds und 5 Blocks, waehrend Rookie Dylan Harper 31 Punkte zum Auswaertssieg beisteuert.",
      "excerpt": "San Antonio behauptet mit dem 110:102 in Utah die NBA-Spitze; Harper ueberragt mit 18 Punkten im Schlussviertel neben Wembanyamas Defensivleistung.",
      "body": [
        "Die San Antonio Spurs setzten ihren famosen Saisonstart am Sonntagabend, 15. November, mit dem zwoelften Sieg in Folge fort und schlugen die Utah Jazz im Delta Center mit 110:102. Mit einer Bilanz von 12-1 fuehren die Texaner die NBA souveraen an.",
        "Victor Wembanyama zeigte eine weltklasse Allround-Leistung und verbuchte 26 Punkte, 11 Rebounds, 6 Assists und 5 Blocks. Der 2,24 Meter grosse Franzose kontrollierte beide Enden des Parketts nach Belieben.",
        "In der Schlussphase drehte Rookie Dylan Harper auf und erzielte 18 seiner insgesamt 31 Punkte im vierten Viertel. Utah, angefuehrt von Mo Bambas 26 Punkten, konnte der Abgeklaertheit der Spurs in den entscheidenden Minuten nichts mehr entgegensetzen."
      ]
    },
    "it": {
      "title": "Spurs a quota 12 vittorie consecutive: Wembanyama e Harper piegano i Jazz 110-102",
      "subtitle": "Victor Wembanyama firma 26 punti, 11 rimbalzi e 5 stoppate mentre la matricola Dylan Harper ne segna 31 per tenere San Antonio in vetta alla NBA.",
      "excerpt": "San Antonio vince la dodicesima partita di fila superando Utah 110-102 grazie a un fantastico quarto periodo da 18 punti di Dylan Harper.",
      "body": [
        "I San Antonio Spurs non si fermano piu: domenica 15 novembre hanno conquistato la dodicesima vittoria consecutiva espugnando il Delta Center di Salt Lake City per 110-102 contro gli Utah Jazz, portandosi sul 12-1 in testa alla lega.",
        "Victor Wembanyama ha dominato con 26 punti, 11 rimbalzi, 6 assist e 5 stoppate in 34 minuti, guidando la difesa e segnando tre triple decisive.",
        "Il protagonista del finale e stato il rookie Dylan Harper, autore di 31 punti complessivi di cui ben 18 nel solo quarto periodo con 7 su 9 al tiro. A nulla sono serviti i 26 punti di Mo Bamba per Utah di fronte alla precisione nei possessi decisivi degli Spurs."
      ]
    },
    "pl": {
      "title": "Spurs przedluzaja serie do 12 zwyciestw: Wembanyama i Harper pokonuja Jazz 110:102",
      "subtitle": "Victor Wembanyama zalicza 26 punktow, 11 zbiorek i 5 blokow, a rewelacyjny debiutant Dylan Harper doklada 31 punktow w Salt Lake City.",
      "excerpt": "San Antonio wygrywa dwunasty mecz z rzedu, pokonujac Jazz 110:102 dzieki 18 punktom Harpera w czwartej kwarcie i dominacji Wembanyamy.",
      "body": [
        "San Antonio Spurs kontynuuja kapitalna serie w sezonie NBA, odnoszac w niedziele 15 listopada dwunaste zwyciestwo z rzedu po wygranej 110:102 z Utah Jazz w Delta Center. Podopieczni z Teksasu legitymuja sie najlepszym bilansem w lidze (12-1).",
        "Victor Wembanyama zaprezentowal pelnie mozliwosci, notujac 26 punktow, 11 zbiorek, 6 asyst i 5 blokow. Francuski center zdominowal strefe podkoszowa, dokladajac takze trzy celne rzuty z dystansu.",
        "W decydujacych fragmentach blyszczal debiutant Dylan Harper, ktory rzucil rekordowe w karierze 31 punktow, w tym 18 w samej czwartej kwarcie. Utah walczylo dzieki 26 punktom Mo Bamby, lecz doswiadczenie i zimna krew Spurs przesadzily o triumfie gosci."
      ]
    },
    "zh": {
      "title": "马刺豪取12连胜：文班亚马攻防统治，哈珀砍31分力克爵士110比102",
      "subtitle": "文班亚马轰下26分11篮板5盖帽全能数据，新秀迪伦·哈珀末节爆砍18分率队稳居全联盟榜首。",
      "excerpt": "圣安东尼奥马刺客场110比102力克犹他爵士取得12连胜，哈珀末节爆发联手文班亚马捍卫联盟第一战绩。",
      "body": [
        "圣安东尼奥马刺在11月15日周日晚继续连胜脚步，客场以110比102力克犹他爵士，将开季连胜纪录扩大至12场，以12胜1负继续领跑全联盟。",
        "维克托·文班亚马在盐湖城攻防两端展现绝对统治力，出战34分钟砍下26分、11个篮板、6次助攻和5记盖帽，同时在外线命中三记三分球，完全封锁了爵士的禁区冲击。",
        "20岁新秀后卫迪伦·哈珀在第四节迎来爆发，单节9投7中狂砍18分，全场斩获生涯新高的31分。在爵士将分差追至2分时，哈珀凭借连续突破和关键三分球打出一波14比4的高潮彻底杀死悬念。"
      ]
    },
    "ja": {
      "title": "スパーズが12連勝に到達：ウェンバンヤマとハーパーが躍動しジャズを110-102で撃破",
      "subtitle": "ビクター・ウェンバンヤマが26得点11リバウンド5ブロック、新人ディラン・ハーパーが31得点を記録しNBA首位を快走。",
      "excerpt": "サンアントニオ・スパーズがユタ・ジャズに110-102で競り勝ち12連勝を達成。ハーパーが第4Qに18得点の大爆発を見せた。",
      "body": [
        "サンアントニオ・スパーズは11月15日日曜日、デルタ・センターで行われたユタ・ジャズ戦に110-102で競り勝ち、今季リーグ最長となる12連勝をマークして12勝1敗の首位を守りました。",
        "ビクター・ウェンバンヤマは34分間の出場で26得点、11リバウンド、6アシスト、5ブロックをマーク。リムプロテクトだけでなく外角からも3本の3ポイントを沈めて圧倒的な存在感を放ちました。",
        "勝負を決めたのは20歳のルーキーガード、ディラン・ハーパーでした。ハーパーは第4クォーターだけで18得点を奪うなどキャリアハイの31得点を叩き出し、接戦を一気に引き寄せました。"
      ]
    },
    "ko": {
      "title": "스퍼스 12연승 질주: 웸반야마 5블록·하퍼 31점으로 재즈 110-102 제압",
      "subtitle": "빅터 웸반야마가 26득점 11리바운드 5블록을 올리고, 신인 딜런 하퍼가 4쿼터 18점 폭발로 샌안토니오 선두 수성.",
      "excerpt": "샌안토니오 스퍼스가 유타 원정에서 110-102로 승리하며 12연승을 달성, 리그 최고 승률(12승 1패)을 이어갔다.",
      "body": [
        "샌안토니오 스퍼스가 11월 15일 일요일 유타 재즈와의 원정 경기에서 110-102 승리를 거두며 파죽의 12연승을 질주했습니다. 시즌 전적 12승 1패로 리그 단독 선두 자리를 굳게 지켰습니다.",
        "빅터 웸반야마는 34분 동안 26득점 11리바운드 6어시스트 5블록슛을 기록하며 공수 양면에서 유타를 압도했습니다. 외곽에서도 3점슛 3개를 터뜨리며 다채로운 득점력을 과시했습니다.",
        "승부처의 주인공은 신인 가드 딜런 하퍼였습니다. 하퍼는 4쿼터에만 야투 7개를 성공시키며 18점을 몰아넣는 등 개인 최다인 31점을 폭발시켜 유타의 맹추격을 잠재웠습니다."
      ]
    },
    "ar": {
      "title": "سبيرز يمددون سلسلة انتصاراتهم إلى 12 مباراة: ويمبانياما وهاربر يقودان الفوز على جاز 110-102",
      "subtitle": "فيكتور ويمبانياما يسجل 26 نقطة و11 متابعة و5 تصديات والوافد الجديد ديلان هاربر يحرز 31 نقطة للحفاظ على صدارة الدوري الأمريكي.",
      "excerpt": "سان أنطونيو سبيرز يحقق فوزه الثاني عشر توالياً بعد إسقاط يوتا جاز 110-102 في سولت ليك سيتي بفضل تألق هاربر بالربع الأخير.",
      "body": [
        "واصل سان أنطونيو سبيرز انطلاقته الخرافية لموسم دوري كرة السلة الأمريكي NBA محققاً فوزه الثاني عشر توالياً بنتيجة 110-102 على حساب يوتا جاز في دلتا سنتر، رافعاً سجله الأفضل في الدوري إلى 12 انتصاراً وهزيمة واحدة.",
        "وقدم النجم الفرنسي فيكتور ويمبانياما أداءً متكاملاً مسجلاً 26 نقطة و11 متابعة و6 تمريرات حاسمة و5 تصديات للكرات في 34 دقيقة، فارضاً سيطرته الدفاعية المطلقة.",
        "وفي الربع الأخير، خطف الصاعد الشاب ديلان هاربر الأضواء بتسجيل 18 نقطة من أصل 31 نقطة حققها في اللقاء، ليحسم فوز فريقه بسلسلة نقاط حاسمة عندما قلص أصحاب الأرض الفارق لنقطتين."
      ]
    }
  },
  "atp-finals-turin-shelton-downs-fils-alcaraz-tiafoe-open-lendl-2026": {
    "fr": {
      "title": "Shelton dompte Fils dans la soiree turinoise ; Alcaraz et Tiafoe lancent le groupe Lendl",
      "subtitle": "Ben Shelton claque 16 aces pour ecarter Arthur Fils 6-2, 3-6, 6-3 a l'Inalpi Arena avant l'entree en lice de Carlos Alcaraz lundi.",
      "excerpt": "La premiere journee des ATP Finals a Turin s'acheve sur le succes en trois sets de Shelton sur Fils, preparant le choc Alcaraz-Tiafoe lundi.",
      "body": [
        "Les Nitto ATP Finals 2026 a Turin ont offert une magnifique empoignade dimanche soir 15 novembre, au cours de laquelle l'Americain Ben Shelton a pris le meilleur sur le Francais Arthur Fils (6-2, 3-6, 6-3) a l'Inalpi Arena. Shelton rejoint Alexander Zverev en tete du groupe John McEnroe.",
        "Shelton a impose sa puissance au service avec sept aces dans le premier set avant que Fils ne replique avec autorite dans la deuxieme manche. Dans le troisieme acte, Shelton a sauve deux balles de break a 2-2 avant de breaker pour s'imposer en 2 heures et 8 minutes avec 16 aces au compteur.",
        "L'attention se tourne lundi 16 novembre vers le groupe Ivan Lendl. Le numero deux mondial Carlos Alcaraz effectue ses debuts face a Frances Tiafoe a partir de 14h00 CET, suivi par le duel entre Daniil Medvedev et l'Italien Flavio Cobolli."
      ]
    },
    "es": {
      "title": "Shelton supera a Fils en tres sets en Turin; Alcaraz y Tiafoe abren el grupo Lendl el lunes",
      "subtitle": "Ben Shelton conecta 16 saques directos para vencer a Arthur Fils 6-2, 3-6, 6-3 antes del esperado debut de Carlos Alcaraz ante Tiafoe.",
      "excerpt": "La primera jornada de las Finales ATP concluye con el triunfo de Shelton en tres mangas, preparando el escenario para el debut de Alcaraz el lunes.",
      "body": [
        "Las Nitto ATP Finals de Turin regalaron un gran espectaculo el domingo por la noche, 15 de noviembre, con la victoria del estadounidense Ben Shelton sobre el frances Arthur Fils por 6-2, 3-6 y 6-3 en el Inalpi Arena.",
        "Shelton domino con su servicio sumando 16 saques directos para neutralizar la reaccion de Fils en el segundo set y sellar el triunfo en dos horas y ocho minutos, igualando a Alexander Zverev con balance de 1-0 en el Grupo McEnroe.",
        "Este lunes 16 de noviembre llega el turno del Grupo Ivan Lendl con el debut del espanol Carlos Alcaraz ante su amigo Frances Tiafoe no antes de las 14:00 CET, seguido por el choque entre Daniil Medvedev y el local Flavio Cobolli."
      ]
    },
    "de": {
      "title": "Shelton ringt Fils in Turin nieder; Alcaraz und Tiafoe eroeffnen Lendl-Gruppe am Montag",
      "subtitle": "Ben Shelton serviert 16 Asse beim 6:2, 3:6, 6:3 ueber Arthur Fils, waehrend Carlos Alcaraz am Montag gegen Frances Tiafoe startet.",
      "excerpt": "Tag 1 der ATP Finals in Turin endet mit Sheltons Dreisatzerfolg ueber Fils, ehe Alcaraz am Montagnachmittag ins Geschehen eingreift.",
      "body": [
        "Die Nitto ATP Finals in Turin boten am Sonntagabend, 15. November, packendes Tennis, als Ben Shelton den Franzosen Arthur Fils mit 6:2, 3:6 und 6:3 in der Inalpi Arena niederrang.",
        "Der US-Amerikaner dominierte mit 16 Assen und wehrte im Entscheidungssatz zwei Breakbaelle ab, um sich nach 2 Stunden und 8 Minuten gemeinsam mit Alexander Zverev an die Spitze der McEnroe-Gruppe zu setzen.",
        "Am Montag, 16. November, startet die Ivan-Lendl-Gruppe: Die Nummer zwei der Welt, Carlos Alcaraz, trifft ab 14:00 Uhr MEZ auf Frances Tiafoe, gefolgt vom Duell zwischen Daniil Medvedev und Lokalmatador Flavio Cobolli."
      ]
    },
    "it": {
      "title": "Shelton piega Fils in tre set a Torino; Alcaraz sfida Tiafoe all'esordio del gruppo Lendl",
      "subtitle": "Ben Shelton batte Arthur Fils 6-2, 3-6, 6-3 con 16 ace all'Inalpi Arena prima dell'attesissimo debutto di Carlos Alcaraz lunedi.",
      "excerpt": "La prima giornata delle ATP Finals si chiude con la vittoria di Shelton su Fils in tre set; lunedi tocca ad Alcaraz contro Tiafoe.",
      "body": [
        "Le Nitto ATP Finals di Torino hanno chiuso la domenica di apertura del 15 novembre con la combattuta vittoria di Ben Shelton su Arthur Fils per 6-2, 3-6, 6-3 all'Inalpi Arena.",
        "Shelton ha fatto valere il proprio servizio con 16 ace complessivi e grande freddezza nel terzo set, agganciando Alexander Zverev in testa al girone John McEnroe con un record di 1-0.",
        "Lunedi 16 novembre scattera il girone Ivan Lendl: Carlos Alcaraz affronta Frances Tiafoe non prima delle 14:00, prima della sfida serale tra Daniil Medvedev e l'azzurro Flavio Cobolli."
      ]
    },
    "pl": {
      "title": "Shelton pokonuje Filsa w Turynie; Alcaraz i Tiafoe otwieraja grupe Lendl w poniedzialek",
      "subtitle": "Ben Shelton serwuje 16 asow i wygrywa z Arthurem Filsem 6:2, 3:6, 6:3, szykujac grunt pod poniedzialkowy wystep Carlosa Alcaraza.",
      "excerpt": "Pierwszy dzien ATP Finals w Turynie zwienczylo trzysetowe zwyciestwo Sheltona nad Filsem; w poniedzialek Alcaraz zmierzy sie z Tiafoe.",
      "body": [
        "Turniej Nitto ATP Finals 2026 w Turynie dostarczyl wielkich emocji w niedzielny wieczor 15 listopada, gdy Ben Shelton pokonal Francuza Arthura Filsa 6:2, 3:6, 6:3 w Inalpi Arena.",
        "Amerykanin popisal sie 16 asami serwisowymi i obronil dwa break pointy w trzecim secie, dolaczajac do Alexandra Zvereva na czele grupy Johna McEnroe z bilansem 1-0.",
        "W poniedzialek 16 listopada do gry wkracza grupa Ivana Lendla: wicelider rankingu Carlos Alcaraz zmierzy sie z Francesem Tiafoe po godz. 14:00 CET, a wieczorem Daniil Medvedev zagra z Flavio Cobollim."
      ]
    },
    "zh": {
      "title": "谢尔顿三盘力克菲斯迎都灵开门红，阿尔卡拉斯周一亮相伦德尔组对阵蒂亚福",
      "subtitle": "本·谢尔顿轰出16记ACE球以6比2、3比6、6比3击败阿蒂尔·菲斯，卡洛斯·阿尔卡拉斯周一下午登场。",
      "excerpt": "ATP年终总决赛首日收官，谢尔顿三盘击败菲斯携手兹维列夫领跑麦肯罗组，周一阿尔卡拉斯将战蒂亚福。",
      "body": [
        "2026年ATP都灵年终总决赛在11月15日周日晚迎来激战，美国名将本·谢尔顿在伊纳尔皮竞技场以6比2、3比6、6比3力克法国新星阿蒂尔·菲斯，与兹维列夫同以1胜0负领跑约翰·麦肯罗组。",
        "谢尔顿全场轰出16记ACE球，并在决胜盘2平的关键时刻挽救两个破发点，随后在第六局实现致命破发，历时2小时08分钟锁定胜局。",
        "赛事焦点在11月16日周一转向伊万·伦德尔组。世界排名第二的卡洛斯·阿尔卡拉斯将于欧洲中部时间14:00后对阵弗朗西斯·蒂亚福，晚场则由前冠军梅德韦杰夫迎战本土新秀科博利。"
      ]
    },
    "ja": {
      "title": "シェルトンがフィルスとの死闘を制す、月曜はアルカラスがティアフォーと激突",
      "subtitle": "ベン・シェルトンが16本のエースを放ち6-2、3-6、6-3で勝利。月曜日はカルロス・アルカラスがトリノ初戦へ。",
      "excerpt": "ATPファイナルズ初日はシェルトンの3セット勝利で幕。月曜日のレンドル組ではアルカラス対ティアフォーが開幕する。",
      "body": [
        "トリノで開催中の2026年Nitto ATPファイナルズは11月15日日曜夜、第3シードのベン・シェルトンがフランスのアルトゥール・フィルスを6-2、3-6、6-3で下し、イナルピ・アリーナで白星発進を飾りました。",
        "シェルトンは持ち前の強烈なサーブで16本のエースを叩き出し、ファイナルセットのピンチを切り抜けて2時間8分の激闘を制し、ズベレフと並びマッケンロー組1勝0敗としました。",
        "11月16日月曜日からはイワン・レンドル組が開幕。世界ランク2位のカルロス・アルカラスがフランシス・ティアフォーと対戦し、夜にはダニール・メドベージェフが地元イタリアのフラビオ・コボッリと対戦します。"
      ]
    },
    "ko": {
      "title": "셸턴, 3세트 접전 끝에 피스 제압; 알카라스는 월요일 티아포와 렌들 조 첫판",
      "subtitle": "벤 셸턴이 서브 에이스 16개를 폭발하며 아르튀르 피스를 6-2, 3-6, 6-3으로 꺾고 토리노 첫 승 기록.",
      "excerpt": "ATP 파이널스 개막전 밤 경기에서 셸턴이 피스를 잡고 1승을 챙겼으며, 월요일에는 카를로스 알카라스가 출격한다.",
      "body": [
        "2026 니토 ATP 파이널스 개막일인 11월 15일 일요일 밤, 미국의 벤 셸턴이 프랑스의 아르튀르 피스와의 혈투 끝에 6-2, 3-6, 6-3으로 승리하며 산뜻하게 출발했습니다.",
        "셸턴은 16개의 서브 에이스를 앞세워 피스의 거센 반격을 잠재우고 2시간 8분 만에 승리를 따내며 즈베레프와 함께 매켄로 조 공동 선두(1승)에 올랐습니다.",
        "11월 16일 월요일에는 이반 렌들 조의 열전이 시작됩니다. 세계 2위 카를로스 알카라스가 절친 프랜시스 티아포를 상대로 첫 경기를 치르며, 야간 경기에서는 다닐 메드베데프와 플라비오 코볼리가 격돌합니다."
      ]
    },
    "ar": {
      "title": "شيلتون يتجاوز فيس في سهرة تورينو المثيرة؛ ألكاراز وتيافو يفتتحان مجموعة ليندل الاثنين",
      "subtitle": "بن شيلتون يطلق 16 إرسالاً ساحقاً ليهزم أرتور فيس 6-2 و3-6 و6-3 قبل الظهور المنتظر لكارلوس ألكاراز أمام تيافو.",
      "excerpt": "اليوم الأول من نهائيات الجولة الختامية بتورينو ينتهي بفوز شيلتون في ثلاث مجموعات تمهيداً لظهور ألكاراز يوم الاثنين.",
      "body": [
        "اختتم اليوم الافتتاحي للبطولة الختامية لمحترفي التنس في تورينو مساء الأحد 15 نوفمبر بمواجهة نارية تفوق فيها الأمريكي بن شيلتون على الفرنسي أرتور فيس بنتيجة 6-2 و3-6 و6-3 في صالة إينالبي أرينا.",
        "وفرض شيلتون هيمنته بـ16 إرسالاً ساحقاً وتماسك ذهني لافت في المجموعة الفاصلة، ليلتحق بالألماني ألكسندر زفيريف في صدارة مجموعة جون ماكنرو بسجل فوز دون هزيمة.",
        "وتتجه الأنظار يوم الاثنين 16 نوفمبر إلى منافسات مجموعة إيفان ليندل، حيث يستهل المصنف الثاني عالمياً كارلوس ألكاراز مشواره بمواجهة صديقه فرانسيس تيافو، يعقبها لقاء الروسي دانييل ميدفيديف مع الإيطالي فلافيو كوبولي."
      ]
    }
  },
  "golf-mcilroy-celebrates-record-tying-8th-race-to-dubai-rsm-classic-next-2026": {
    "fr": {
      "title": "McIlroy savoure son 8e titre a la Race to Dubai ; le PGA Tour prend la direction du RSM Classic",
      "subtitle": "Rory McIlroy egale le record absolu de Colin Montgomerie apres le sacre de Tyrrell Hatton a Dubai, alors que la lutte pour le maintien s'ouvre a Sea Island.",
      "excerpt": "Rory McIlroy savoure sa huitieme couronne europeenne apres avoir devance Eugenio Chacarra de 125 points a Dubai, le regard tourne vers le RSM Classic.",
      "body": [
        "Rory McIlroy s'est reveille lundi 16 novembre dans l'histoire vivante du golf europeen apres avoir scelle sa huitieme couronne a la Race to Dubai sur les greens du Jumeirah Golf Estates. Sa derniere carte de 67 (-5) sans bogey lui a permis d'arracher la deuxieme place en solitaire a -10 (278), devancant l'Espagnol Eugenio Chacarra de seulement 125 points pour brandir son cinquieme Harry Vardon Trophy consecutif.",
        "Ce sacre permet au Nord-Irlandais d'egaler le record mythique de l'Ecossais Colin Montgomerie, couronne a huit reprises entre 1993 et 2005. Tandis que l'Anglais Tyrrell Hatton savourait sa victoire eclatante avec cinq longueurs d'avance a -15 (273), McIlroy a dedie sa couronne a son pere Gerry, en convalescence apres une double greffe pulmonaire a Cleveland.",
        "La saison du DP World Tour etant bouclee, l'attention se deplace en Georgie ou debute la semaine du RSM Classic au Sea Island Golf Club (19-22 novembre). Ce tournoi constitue l'ultime epreuve des FedExCup Fall, ou les joueurs se battent pour integrer le top 125 et preserver leurs droits de jeu complets pour 2027."
      ]
    },
    "es": {
      "title": "McIlroy celebra su historica octava Race to Dubai mientras el PGA Tour viaja al RSM Classic",
      "subtitle": "Rory McIlroy iguala el record europeo de Colin Montgomerie tras la victoria de Tyrrell Hatton en Dubai, dando paso a la definicion del top 125 en Sea Island.",
      "excerpt": "Rory McIlroy saborea su octava Orden de Merito europea tras superar a Eugenio Chacarra por 125 puntos en Dubai antes de la definicion del RSM Classic.",
      "body": [
        "Rory McIlroy amanecio este lunes 16 de noviembre en la cuspide del golf mundial tras asegurar su octavo titulo de la Race to Dubai en Jumeirah Golf Estates. Una ronda final de 67 (-5) sin bogeys le valio el segundo puesto en solitario con 278 golpes (-10), aventajando por apenas 125 puntos a Eugenio Chacarra para ganar su quinto Harry Vardon Trophy consecutivo.",
        "La hazana permitio a McIlroy empatar el record historico de Colin Montgomerie, ocho veces campeon de la Orden de Merito entre 1993 y 2005. Mientras Tyrrell Hatton celebraba su victoria por cinco golpes con 15 bajo par (273), McIlroy dedico entre lagrimas el trofeo a su padre Gerry, recuperado tras un trasplante de pulmon doble.",
        "Concluido el periplo europeo, el foco se traslada a Sea Island, Georgia, para el RSM Classic del PGA Tour (19-22 de noviembre), el decisivo cierre del FedExCup Fall donde los golfistas luchan por meterse entre los 125 mejores y asegurar su tarjeta para 2027."
      ]
    },
    "de": {
      "title": "McIlroy feiert achten Race-to-Dubai-Titel; PGA Tour blickt auf die RSM Classic",
      "subtitle": "Rory McIlroy stellt Montgomeries Rekord nach Tyrrell Hattons Dubai-Triumph ein; in Sea Island beginnt der Kampf um die Tourkarten fuer 2027.",
      "excerpt": "Rory McIlroy geniesst seinen achten Gesamtsieg auf der European Tour mit 125 Punkten Vorsprung auf Chacarra, waehrend der Fokus auf die RSM Classic wandert.",
      "body": [
        "Rory McIlroy zog am Montag, 16. November, endgueltig mit den Legenden des europaeischen Golfsports gleich, nachdem er sich auf dem Earth Course in Dubai seinen achten Race-to-Dubai-Titel gesichert hatte. Eine fehlerfreie 67er-Runde reichte zu Rang zwei (-10, 278) und brachte ihm 125 Punkte Vorsprung auf Eugenio Chacarra.",
        "Damit egalisierte der Nordire den Rekord von Colin Montgomerie, der die Jahreswertung zwischen 1993 und 2005 achtmal gewann. Waehrend Tyrrell Hatton mit fuenf Schlaegen Vorsprung bei -15 (273) souveraen siegte, widmete McIlroy den Titel seinem genesenden Vater Gerry.",
        "Nach dem DP-World-Tour-Finale richtet sich der Blick nach Georgia: Auf Sea Island beginnt die Turnierwoche der RSM Classic (19.-22. November), dem letzten Event der FedExCup Fall, bei dem es um die begehrten Top-125-Plaetze fuer die Saison 2027 geht."
      ]
    },
    "it": {
      "title": "McIlroy festeggia l'ottava Race to Dubai; il PGA Tour si prepara al RSM Classic",
      "subtitle": "Rory McIlroy eguaglia il record storico di Colin Montgomerie dopo il trionfo di Tyrrell Hatton a Dubai, mentre a Sea Island si decide il destino del top 125.",
      "excerpt": "Rory McIlroy celebra l'ottavo titolo europeo conquistato con 125 punti di margine su Chacarra, in attesa dell'atto finale del FedExCup Fall.",
      "body": [
        "Rory McIlroy si e svegliato lunedi 16 novembre nella storia leggendaria del golf europeo dopo aver conquistato il suo ottavo titolo nella Race to Dubai a Jumeirah Golf Estates. Un solido 67 finale senza bogey gli e valso il secondo posto a -10 (278), battendo Eugenio Chacarra per soli 125 punti.",
        "Il nordirlandese ha cosi eguagliato lo scozzese Colin Montgomerie, vincitore di otto ordini di merito europei tra il 1993 e il 2005. Mentre Tyrrell Hatton trionfava con 15 colpi sotto il par (273), McIlroy ha dedicato il trofeo a suo padre Gerry.",
        "Chiusa la stagione europea, i riflettori si spostano a Sea Island, in Georgia, per il prestigioso RSM Classic del PGA Tour (19-22 novembre), ultimo appuntamento del FedExCup Fall in cui i golfisti lottano per entrare nei primi 125 posti della classifica."
      ]
    },
    "pl": {
      "title": "McIlroy swietuje 8. tytul Race to Dubai; PGA Tour przenosi sie na RSM Classic",
      "subtitle": "Rory McIlroy wyrownuje rekord Colina Montgomerie po wygranej Tyrrella Hattona w Dubaju; w Sea Island rusza walka o karty na sezon 2027.",
      "excerpt": "Rory McIlroy raduje sie z osmego triumfu w klasyfikacji generalnej European Tour wyprzedzajac Chacarre o 125 punktow przed finalem FedExCup Fall.",
      "body": [
        "Rory McIlroy przypieczetowal w niedziele swoje osemkowe zwyciestwo w klasyfikacji Race to Dubai na Earth Course w Dubaju. Bogey-free runda 67 (-5) dala mu drugie miejsce z wynikiem -10 (278), co wystarczylo, by wyprzedzic Eugenio Chacarre o zaledwie 125 punktow.",
        "Tym samym reprezentant Irlandii Polnocnej zrownal sie z legendarnym Colinem Montgomerie, ktory dominowal w Europie w latach 1993-2005. Tyrrell Hatton siegnal po tytul z wynikiem -15 (273), a wzruszony McIlroy zadedykowal swoj piaty z rzedu Harry Vardon Trophy ojcu Gerry'emu.",
        "Po zakonczeniu sezonu DP World Tour uwaga przenosi sie do Georgii, gdzie na polach Sea Island Golf Club odbedzie sie RSM Classic (19-22 listopada) - finalowy turniej FedExCup Fall decydujacy o miejscach w czolowej 125."
      ]
    },
    "zh": {
      "title": "麦克罗伊庆祝第八次问鼎迪拜竞赛总冠军，美巡赛移师RSM精英赛",
      "subtitle": "哈顿在迪拜大胜夺冠，麦克罗伊追平蒙哥马利八冠历史纪录，美巡秋季赛在海岛迎来保卡终局之战。",
      "excerpt": "麦克罗伊以125分微弱优势力压查卡拉第八次登顶欧巡年度总冠军，美巡赛将在佐治亚州海岛迎来RSM精英赛。",
      "body": [
        "罗里·麦克罗伊在11月16日周一迎来了职业生涯的又一丰碑，他在朱美拉高尔夫庄园以第八次加冕迪拜竞赛总冠军的战绩比肩传奇。决赛轮打出无柏忌的67杆（-5）助他以总成绩278杆（-10）独占亚军，以125分险胜西班牙新星查卡拉，连续第五年捧起哈里·瓦登奖杯。",
        "这一成就让麦克罗伊追平了苏格兰名宿科林·蒙哥马利在1993年至2005年间创下的八次加冕欧巡奖金榜纪录。英格兰名将哈顿以低于标准杆15杆（273杆）豪取5杆大胜，赛后麦克罗伊动情地将荣誉献给刚做完肺部移植手术的父亲。",
        "随着欧巡赛季圆满落幕，高坛目光转向美国佐治亚州圣西蒙斯岛。美巡秋季赛收官战RSM精英赛将于11月19日至22日在海岛高尔夫俱乐部展开，球手们将为前125名全卡席位展开白热化搏杀。"
      ]
    },
    "ja": {
      "title": "マキロイが歴代最多タイ8度目の年間王者を祝う、PGAツアーはRSMクラシックへ",
      "subtitle": "ハットンのドバイ制覇の陰でマキロイがコリン・モンゴメリーの偉業に到達。シード権を懸けたシーアイランド決戦が開幕。",
      "excerpt": "マキロイがチャカラをわずか125pt差で抑えて欧州年間王者に輝き、PGAツアーは秋季最終戦RSMクラシックを迎える。",
      "body": [
        "ローリー・マキロイは11月16日月曜日、ジュメイラ・ゴルフ・エステーツでのドラマチックな戦いを経て、通算8度目となるレース・トゥ・ドバイ年間王者の栄誉に浸りました。最終ラウンドでノーボギーの67をマークして単独2位（278打、-10）に入り、チャカラをわずか125ポイント上回って栄冠を手にしました。",
        "この戴冠により、マキロイは1993年から2005年にかけて8度の欧州賞金王に輝いたコリン・モンゴメリーの不滅の金字塔に並びました。大会はティレル・ハットンが通算15アンダー（273打）で5打差の圧勝を飾りました。",
        "欧州ツアーが幕を閉じたことで、ゴルフ界の視線はジョージア州セントサイモンズ島へ移ります。シーアイランドGCで開催されるPGAツアー「RSMクラシック」（11月19-22日）は、来季フルシードとなるトップ125を争う秋季シリーズの最終戦となります。"
      ]
    },
    "ko": {
      "title": "매킬로이 8번째 유럽 투어 올해의 선수 금자탑; PGA 투어는 RSM 클래식 격돌",
      "subtitle": "해튼의 두바이 우승 속 매킬로이가 몽고메리의 역대 최다 기록과 동률을 이뤘으며, 시 아일랜드에서 시드권 최종전이 열린다.",
      "excerpt": "로리 매킬로이가 차카라를 125점 차로 제치고 8번째 레이스 투 두바이 정상에 올랐으며, PGA 투어는 RSM 클래식에 돌입한다.",
      "body": [
        "로리 매킬로이가 11월 16일 월요일 통산 8번째 레이스 투 두바이 챔피언에 등극하며 유럽 골프 역사의 전설들과 어깨를 나란히 했습니다. 최종 라운드에서 보기 없는 67타를 기록해 단독 2위(278타, -10)를 차지하며 에우헤니오 차카라를 125포인트 차로 따돌렸습니다.",
        "매킬로이는 1993년부터 2005년까지 8차례 유럽 투어 상금왕에 오른 스코틀랜드의 전설 콜린 몽고메리의 역대 최다 기록과 동률을 이뤘습니다. 티럴 해튼이 15언더파 273타로 5타 차 우승을 차지했습니다.",
        "유럽 투어가 성황리에 막을 내리면서 골프 팬들의 시선은 미국 조지아주 세인트 사이먼스 아일랜드로 향합니다. 시 아일랜드 골프클럽에서 개막하는 PGA 투어 RSM 클래식(11월 19-22일)은 내년도 풀시드가 걸린 페덱스컵 가을 시리즈 최종전입니다."
      ]
    },
    "ar": {
      "title": "ماكلروي يحتفل بلقبه الثامن القياسي في السباق إلى دبي؛ وبطولة RSM كلاسيك المحطة القادمة",
      "subtitle": "روري ماكلروي يعادل الرقم القياسي لكولين مونتغومري بعد تتويج هاتون في دبي، والأنظار تتجه لحسم بطاقات الجولة الأمريكية في سي آيلاند.",
      "excerpt": "روري ماكلروي يتوج بلقبه الأوروبي الثامن بفارق 125 نقطة عن شاكارا، وجولة PGA تترقب نهائي الخريف في بطولة RSM كلاسيك.",
      "body": [
        "استيقظ روري ماكلروي يوم الاثنين 16 نوفمبر وهو في قمة المجد بعد حسمه اللقب الثامن في مسيرته بالسباق إلى دبي في عقارات جميرا للجولف. وأحرز المركز الثاني منفرداً بـ10 ضربات تحت المعدل (278) إثر جولة ختامية بـ67 ضربة، متفوقاً على الإسباني أوخينيو شاكارا بـ125 نقطة فقط.",
        "وعادل الإيرلندي الشمالي الرقم القياسي للأسطورة كولين مونتغومري صاحب ثمانية ألقاب بين 1993 و2005. وفيما احتفل تيريل هاتون بلقبه بفارق خمس ضربات مسجلاً 15 تحت المعدل (273)، أهدى ماكلروي لقبه لوالده جيري الذي يتعافى من زراعة رئة.",
        "ومع ختام الجولة الأوروبية، تنتقل الإثارة إلى جورجيا الأمريكية حيث تبدأ منافسات بطولة RSM كلاسيك في نادي سي آيلاند للجولف (19-22 نوفمبر)، وهي المحطة الختامية لموسم الخريف التي تحدد أفضل 125 لاعباً لضمان بطاقات المشاركة الكاملة لعام 2027."
      ]
    }
  },
  "f1-three-days-las-vegas-strip-p2-five-driver-shootout-2026": {
    "fr": {
      "title": "A trois jours du Strip de Las Vegas : 33 points separent cinq pilotes pour la place de vice-champion",
      "subtitle": "Kimi Antonelli et Mercedes etant deja couronnes, Max Verstappen, George Russell, Lewis Hamilton, Charles Leclerc et Lando Norris se disputent la 2e place.",
      "excerpt": "La Formule 1 installe ses quartiers au Nevada a trois jours des premiers essais sur le Strip de 6,201 km dans une lutte a cinq pour le titre de dauphin.",
      "body": [
        "Le paddock de la Formule 1 s'installe a Las Vegas ce lundi 16 novembre, a seulement trois jours des premiers essais libres sur le Strip Circuit de 6,201 km (19-21 novembre). Alors que le prodige Kimi Antonelli (390 points) et Mercedes (652 points) ont deja conquis les deux couronnes mondiales au Bresil, la bataille pour la deuxieme place du championnat des pilotes s'annonce electrique.",
        "Seulement 33 points separent le deuxieme Max Verstappen (279 points) du sixieme Lando Norris (246 points) a trois manches de la fin. Entre eux s'intercalent George Russell (262), Lewis Hamilton (261) et Charles Leclerc (249). La longue ligne droite du Strip exigera une vitesse de pointe maximale sous des temperatures nocturnes desertiques particulierement fraiches.",
        "Chez les constructeurs, Ferrari (510 points) defend sa deuxieme place face aux assauts de Red Bull Racing (415) et McLaren (398). Aucun tour de piste n'a encore ete dispute a Vegas, mais la tension est deja palpable sur le boulevard de la capitale du jeu."
      ]
    },
    "es": {
      "title": "A tres dias del Strip de Las Vegas: 33 puntos separan a cinco pilotos en la pugna por el subcampeonato",
      "subtitle": "Con Kimi Antonelli y Mercedes ya campeones, Verstappen, Russell, Hamilton, Leclerc y Norris inician una batalla crucial en la ronda 21.",
      "excerpt": "La Formula 1 llega a Nevada a tres dias de los primeros libres en el circuito del Strip con una intensa batalla a cinco bandas por el segundo puesto.",
      "body": [
        "El paddock de la Formula 1 comienza los preparativos en Nevada este lunes 16 de noviembre, a tres dias del inicio de la accion en pista del Gran Premio de Las Vegas (19-21 de noviembre). Aunque Kimi Antonelli (390 puntos) y Mercedes (652 puntos) ya sellaron los dos titulos mundiales, la lucha por el subcampeonato ofrece un duelo apasionante.",
        "Apenas 33 puntos distancian a Max Verstappen (279) en la segunda posicion de Lando Norris (246) en la sexta, con George Russell (262), Lewis Hamilton (261) y Charles Leclerc (249) en medio. El trazado urbano de 6,201 km y su larguisima recta pondran a prueba la velocidad punta y el calentamiento de neumaticos bajo el frio nocturno del desierto.",
        "En el mundial de constructores, Ferrari (510 puntos) defiende el segundo puesto ante el asedio de Red Bull (415) y McLaren (398). Todavia no se ha disputado ninguna sesion en pista, pero la expectacion en Las Vegas es maxima."
      ]
    },
    "de": {
      "title": "Drei Tage bis zum Las Vegas Strip: Fuenfkampf um die Vize-Weltmeisterschaft spitzt sich zu",
      "subtitle": "Kimi Antonelli und Mercedes sind Weltmeister; zwischen Verstappen, Russell, Hamilton, Leclerc und Norris liegen vor Runde 21 nur 33 Zaehler.",
      "excerpt": "Die Formule 1 reist nach Nevada: Drei Tage vor dem Trainingsauftakt auf dem 6,201 km langen Strip Circuit kaempfen fuenf Piloten um Platz zwei.",
      "body": [
        "Der Formel-1-Tross schlaegt am Montag, 16. November, seine Zelte in Nevada auf. In drei Tagen beginnt auf dem 6,201 km langen Las Vegas Strip Circuit das Rennwochenende (19.-21. November). Kimi Antonelli (390 Punkte) und Mercedes (652 Punkte) stehen zwar bereits als Weltmeister fest, doch der Kampf um Platz zwei verspricht Hochspannung.",
        "Lediglich 33 Punkte trennen den Gesamtzweiten Max Verstappen (279 Punkte) vom Sechsten Lando Norris (246 Punkte). Dazwischen lauern George Russell (262), Lewis Hamilton (261) und Charles Leclerc (249). Die Highspeed-Passagen auf dem Strip fordern bei naechtlicher Kaelte alles von Bremsen und Reifen.",
        "Bei den Konstrukteuren kaempft Ferrari (510 Punkte) gegen Red Bull (415) und McLaren (398) um Rang zwei. Noch hat kein Bolide die Strecke befahren, doch der Wettstreit im Spielerparadies ist eroeffnet."
      ]
    },
    "it": {
      "title": "Tre giorni al Las Vegas Strip: 33 punti dividono cinque piloti per il titolo di vicecampione",
      "subtitle": "Mentre Antonelli e la Mercedes festeggiano i titoli mondiali, Verstappen, Russell, Hamilton, Leclerc e Norris si sfidano nel terzultimo round.",
      "excerpt": "La Formula 1 sbarca in Nevada: tre giorni all'avvio delle prove libere sul circuito della Strip con cinque piloti in lizza per il secondo posto.",
      "body": [
        "Il paddock della Formula 1 prende forma a Las Vegas questo lunedi 16 novembre, a soli tre giorni dal via delle prove libere del Gran Premio di Las Vegas (19-21 novembre). Con Kimi Antonelli (390 punti) e la Mercedes (652 punti) campioni del mondo, l'interesse e puntato sulla corsa per il secondo posto iridato.",
        "Sono soltanto 33 i punti che separano Max Verstappen (279 punti) da Lando Norris (246), con in mezzo George Russell (262), Lewis Hamilton (261) e Charles Leclerc (249). Il rettilineo della Strip lungo 1,9 km mettera a dura prova l'efficienza aerodinamica e la gestione delle gomme con il freddo del deserto.",
        "Tra i costruttori la Ferrari (510 punti) deve guardarsi le spalle da Red Bull (415) e McLaren (398). Non si e ancora disputata alcuna sessione in pista, ma la sfida sotto le luci del Nevada e gia caldissima."
      ]
    },
    "pl": {
      "title": "Trzy dni do Las Vegas Strip: 33 punkty dziela pieciu kierowcow w walce o wicemistrzostwo",
      "subtitle": "Kimi Antonelli i Mercedes zapewnili sobie tytuly; Verstappen, Russell, Hamilton, Leclerc i Norris staja do walki o 2. miejsce.",
      "excerpt": "Formule 1 wkracza do Nevady: trzy dni przed treningami na torze Strip Circuit piatka kierowcow toczy walke o wicemistrzostwo swiata.",
      "body": [
        "Padok Formuly 1 melduje sie w poniedzialek 16 listopada w Nevadzie, na trzy dni przed pierwszymi treningami przed Grand Prix Las Vegas (19-21 listopada). Podczas gdy Kimi Antonelli (390 pkt) i Mercedes (652 pkt) swietuja podwojna korone, walka o tytul wicemistrza swiata zapowiada sie pasjonujaco.",
        "Zaledwie 33 punkty dziela drugiego w tabeli Maxa Verstappena (279) od szostego Lando Norrisa (246). Pomiedzy nimi znajduja sie George Russell (262), Lewis Hamilton (261) i Charles Leclerc (249). Dluga prosta na Stripie o dlugosci 1,9 km bedzie testem predkosci i dogrzewania opon w chlodna noc.",
        "W klasyfikacji konstruktorow Ferrari (510 pkt) broni drugiego miejsca przed Red Bullem (415) i McLarenem (398). Sesje treningowe rusza dopiero w czwartek, ale napiecie w Las Vegas siega zenitu."
      ]
    },
    "zh": {
      "title": "距离拉斯维加斯街道战仅剩三天：五位车手相差33分争夺年度亚军",
      "subtitle": "安东内利与梅赛德斯加冕世界冠军后，维斯塔潘、拉塞尔、汉密尔顿、勒克莱尔和诺里斯展开年度次席大混战。",
      "excerpt": "F1围场进驻内华达，距离拉斯维加斯大奖赛练习赛仅剩三天，五大车手为年度亚军荣誉展开白热化争夺。",
      "body": [
        "F1围场于11月16日周一全面进驻内华达州，距离拉斯维加斯大奖赛（11月19日至21日）首节练习赛仅剩最后三天。在基米·安东内利（390分）与梅赛德斯（652分）已提前锁定双料世界冠军的背景下，年度车手亚军之争演变为近年最激烈的乱局。",
        "在赛季仅剩最后三站之际，从排名第二的维斯塔潘（279分）到第六的诺里斯（246分）之间仅相差33分，拉塞尔（262分）、汉密尔顿（261分）和勒克莱尔（249分）紧随其后。长达6.201公里的赌城大道赛道以极速直道著称，寒冷的沙漠夜间气温对轮胎升温提出了巨大考验。",
        "车队积分榜上，法拉利（510分）同样面临红牛（415分）和迈凯伦（398分）对车队亚军席位的猛烈冲击。目前尚未进行任何赛道练习，但赌城霓虹下的火药味已然十足。"
      ]
    },
    "ja": {
      "title": "ラスベガス決戦まであと3日：5名のドライバーが33点差でランキング2位を争う",
      "subtitle": "アントネッリとメルセデスの戴冠後、フェルスタッペン、ラッセル、ハミルトン、ルクレール、ノリスによる副賞争いが激化。",
      "excerpt": "F1がネバダ州に集結。全長6.201kmのストリップ・サーキットでの走行開始まで3日となり、熾烈なシリーズ2位争いが展開される。",
      "body": [
        "F1パドックは11月16日月曜日、ネバダ州ラスベガスで設営を開始しました。第21戦ラスベガスGP（11月19-21日）の木曜フリー走行まであと3日です。キミ・アントネッリ（390点）とメルセデス（652点）がタイトルを確定させたものの、ランキング2位争いは白熱しています。",
        "残り3戦で、2位のマックス・フェルスタッペン（279点）から6位のランド・ノリス（246点）までの差はわずか33点。その間にジョージ・ラッセル（262点）、ルイス・ハミルトン（261点）、シャルル・ルクレール（249点）がひしめき合っています。",
        "コンストラクターズ部門でも、2位のフェラーリ（510点）にレッドブル（415点）とマクラーレン（398点）が肉薄。砂漠の冷え込む夜間に行われるストリップでのハイスピードバトルに注目が集まります。"
      ]
    },
    "ko": {
      "title": "라스베이거스 스트립 결전 D-3: 드라이버 5명 33점 차 준우승 대접전",
      "subtitle": "안토넬리와 메르세데스의 월드 챔피언 확정 속 베르스타펜, 러셀, 해밀턴, 르클레르, 노리스가 21라운드 격돌을 준비합니다.",
      "excerpt": "F1 서커스가 네바다에 상륙했습니다. 6.201km 스트립 서킷 첫 연습 주행까지 3일 남은 가운데 치열한 준우승 쟁탈전이 펼쳐집니다.",
      "body": [
        "F1 패덕이 11月 16일 월요일 네바다주 라스베이거스에 입성했습니다. 제21라운드 라스베이거스 그랑프리(11월 19-21일) 첫 연습 주행까지 단 3일만을 남겨두고 있습니다. 키미 안토넬리(390점)와 메르세데스(652점)가 챔피언십을 조기 확정지었지만, 드라이버 2위 싸움은 절정으로 치닫고 있습니다.",
        "남은 세 경기에서 2위 막스 베르스타펜(279점)부터 6위 랜도 노리스(246점)까지의 격차는 불과 33점에 불과합니다. 조지 러셀(262점), 루이스 해밀턴(261점), 샤를 르클레르(249점)가 촘촘히 포진해 있으며, 추운 밤 사막 기온 속 타이어 관리가 승부를 가를 변수로 꼽힙니다.",
        "컨스트럭터 부문에서도 2위 페라리(510점)가 레드불(415점)과 맥라렌(398점)의 거센 추격을 받고 있습니다. 아직 트랙 세션은 시작되지 않았지만 라스베이거스 스트립의 긴장감은 최고조에 달했습니다."
      ]
    },
    "ar": {
      "title": "ثلاثة أيام على جائزة لاس فيغاس: 33 نقطة تفصل خمسة سائقين في صراع وصافة بطولة العالم",
      "subtitle": "مع تتويج كيمي أنتونيللي ومرسيدس باللقبين، يشتعل الصراع على المركز الثاني بين فيرستابن وراسل وهاميلتون ولوكلير ونوريس.",
      "excerpt": "الفورمولا 1 تحط رحالها في نيفادا قبل ثلاثة أيام من التجارب الحرة على حلبة ستريب البالغ طولها 6.201 كم وسط صراع محموم على الوصافة.",
      "body": [
        "بدأت فرق بطولة العالم لسباقات الفورمولا 1 التجمع في نيفادا يوم الاثنين 16 نوفمبر مع تبقي ثلاثة أيام فقط على انطلاق التجارب الحرة للجولة 21 على حلبة لاس فيغاس الشهيرة (19-21 نوفمبر). وفيما حسم الإيطالي كيمي أنتونيللي (390 نقطة) ومرسيدس (652 نقطة) لقبي العالم، فإن المنافسة على المركز الثاني تشتعل بشكل غير مسبوق.",
        "تفصل 33 نقطة فقط بين الثاني ماكس فيرستابن (279) والسادس لاندو نوريس (246)، وبينهما جورج راسل (262) ولويس هاميلتون (261) وشارل لوكلير (249) قبل ثلاث جولات على الختام. وستكون السرعة القصوى على خط ستريب المستقيم وإحماء الإطارات في البرودة الصحراوية مفتاح التفوق.",
        "وعلى صعيد الصانعين، تدافع فيراري (510 نقاط) عن وصافتها أمام ملاحقة رد بول (415) ومكلارين (398)، في عطلة أسبوع مشتعلة تحت أضواء نيفادا الصاخبة."
      ]
    }
  }
}

# Read stories.ts
stories_content = open(STORIES_TS, "r", encoding="utf-8").read()

# Insert before the closing `};` of STORY_I18N
# We can format each slug cleanly
entries_to_insert = []
for slug, translations in nov16_translations.items():
    if f'"{slug}":' in stories_content:
        print(f"Slug {slug} already in stories.ts, skipping.")
        continue
    slug_str = f'  "{slug}": ' + json.dumps(translations, indent=4, ensure_ascii=False) + ",\n"
    entries_to_insert.append(slug_str)

if entries_to_insert:
    # Find the last `};\n` or `};` in stories_content
    last_brace = stories_content.rfind("};")
    if last_brace != -1:
        new_content = stories_content[:last_brace] + "".join(entries_to_insert) + stories_content[last_brace:]
        open(STORIES_TS, "w", encoding="utf-8").write(new_content)
        print(f"Injected {len(entries_to_insert)} nov16 translations into stories.ts.")
    else:
        print("Error: Could not find closing `};` in stories.ts")
else:
    print("No new translations to insert.")

