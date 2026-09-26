import type { Locale } from './locales';

export type StoryI18n = {
  title: string;
  subtitle: string;
  excerpt: string;
  body: string[];
};

type LocMap = Partial<Record<Exclude<Locale, 'en'>, StoryI18n>>;

export const STORY_I18N: Record<string, LocMap> = {
  'brighton-arsenal-mw5': {
    fr: {
      title: 'Brighton 3-0 Arsenal : les champions chutent, dimanche reste ouvert',
      subtitle: 'Groß, Kostoulas, Chema Andrés. City reste 4-0-0 avec un match en retard. La 5e journée n’est pas close.',
      excerpt: 'Brighton bat Arsenal 3-0 à l’Amex le 19 septembre. Sky, The Athletic et Brighton.com impriment le même score. Xinhua : City 12 en quatre, Arsenal 12 en cinq, Brighton 10.',
      body: [
        'Arsenal arrivait à 4-0-0. Brighton mène le classement des buteurs. Samedi à l’Amex s’est fini 3-0. Les champions ont une première défaite de championnat. Manchester City a toujours 12 points en quatre matches. Dimanche n’a pas commencé.',
        'Brighton.com : Pascal Groß 31e, Charalampos Kostoulas 45e, Chema Andrés 57e. Sky, The Athletic, The Guardian et ESPN impriment le même 3-0. Groß et Kostoulas de loin. Andrés a repris le corner de Gross. Opta : 16 buts de Brighton, meilleur total du championnat.',
        'Xinhua après samedi : City 12 en quatre, Arsenal 12 en cinq, Brighton 10. Dimanche est listé, pas fini : Leeds-Palace, City-Sunderland, Bournemouth-Liverpool, Fulham-United. Le tableau ESPN du 20 septembre imprime encore vs. N’inventez pas un score de dimanche.',
      ],
    },
    es: {
      title: 'Brighton 3-0 Arsenal: caen los campeones y el domingo sigue abierto',
      subtitle: 'Groß, Kostoulas, Chema Andrés. City sigue 4-0-0 con un partido menos. La jornada 5 no está cerrada.',
      excerpt: 'Brighton gana 3-0 a Arsenal en el Amex el 19 de septiembre. Sky, The Athletic y Brighton.com imprimen el mismo marcador. Xinhua: City 12 en cuatro, Arsenal 12 en cinco, Brighton 10.',
      body: [
        'Arsenal llegó 4-0-0. Brighton lidera la tabla de goleadores. El sábado en el Amex acabó 3-0. Los campeones tienen su primera derrota liguera. Manchester City sigue con 12 puntos en cuatro partidos. El domingo no ha arrancado.',
        'Brighton.com: Pascal Groß 31, Charalampos Kostoulas 45, Chema Andrés 57. Sky, The Athletic, The Guardian y ESPN imprimen el mismo 3-0. Groß y Kostoulas de lejos. Andrés cabeceó el córner de Gross. Opta: 16 goles de Brighton, máximo de la liga.',
        'Xinhua tras el sábado: City 12 en cuatro, Arsenal 12 en cinco, Brighton 10. El domingo está listado, no cerrado. El marcador ESPN del 20 de septiembre sigue en vs. No inventes un resultado del domingo.',
      ],
    },
    de: {
      title: 'Brighton 3:0 Arsenal: die Meister verlieren, Sonntag bleibt offen',
      subtitle: 'Groß, Kostoulas, Chema Andrés. City bleibt 4-0-0 mit einem Spiel weniger. Spieltag 5 ist nicht zu Ende.',
      excerpt: 'Brighton schlägt Arsenal 3:0 am 19. September. Sky, The Athletic und Brighton.com drucken denselben Stand. Xinhua: City 12 aus vier, Arsenal 12 aus fünf, Brighton 10.',
      body: [
        'Arsenal kam 4-0-0. Brighton führt die Torschützenliste. Samstag an der Amex endete 3:0. Die Meister haben eine erste Liga-Niederlage. Manchester City hat weiter 12 Punkte aus vier Spielen. Sonntag hat nicht angepfiffen.',
        'Brighton.com: Pascal Groß 31., Charalampos Kostoulas 45., Chema Andrés 57. Sky, The Athletic, The Guardian und ESPN drucken dasselbe 3:0. Groß und Kostoulas aus der Distanz. Andrés köpfte Gross’ Ecke. Opta: 16 Brighton-Tore, Liga-Bestwert.',
        'Xinhua nach Samstag: City 12 aus vier, Arsenal 12 aus fünf, Brighton 10. Sonntag ist gelistet, nicht fertig. ESPN am 20. September druckt noch vs. Keinen Sonntagsscore erfinden.',
      ],
    },
    it: {
      title: 'Brighton 3-0 Arsenal: i campioni cadono, la domenica resta aperta',
      subtitle: 'Groß, Kostoulas, Chema Andrés. City resta 4-0-0 con una partita da recuperare. La 5ª giornata non è chiusa.',
      excerpt: 'Brighton batte l’Arsenal 3-0 all’Amex il 19 settembre. Sky, The Athletic e Brighton.com stampano lo stesso punteggio. Xinhua: City 12 in quattro, Arsenal 12 in cinque, Brighton 10.',
      body: [
        'L’Arsenal è arrivato 4-0-0. Brighton guida i cannonieri. Sabato all’Amex è finito 3-0. I campioni hanno una prima sconfitta in campionato. Il Manchester City ha ancora 12 punti in quattro partite. La domenica non è partita.',
        'Brighton.com: Pascal Groß 31’, Charalampos Kostoulas 45’, Chema Andrés 57’. Sky, The Athletic, The Guardian ed ESPN stampano lo stesso 3-0. Groß e Kostoulas da lontano. Andrés ha colpito il corner di Gross. Opta: 16 gol del Brighton, massimo del campionato.',
        'Xinhua dopo sabato: City 12 in quattro, Arsenal 12 in cinque, Brighton 10. La domenica è in elenco, non chiusa. ESPN il 20 settembre stampa ancora vs. Non inventare un risultato di domenica.',
      ],
    },
    pl: {
      title: 'Brighton 3-0 Arsenal: mistrzowie przegrywają, niedziela zostaje otwarta',
      subtitle: 'Groß, Kostoulas, Chema Andrés. City nadal 4-0-0 z meczem w ręku. 5. kolejka nie jest zamknięta.',
      excerpt: 'Brighton wygrywa 3-0 z Arsenalem 19 września. Sky, The Athletic i Brighton.com drukują ten sam wynik. Xinhua: City 12 z czterech, Arsenal 12 z pięciu, Brighton 10.',
      body: [
        'Arsenal przyszedł 4-0-0. Brighton prowadzi w strzelcach. Sobota na Amex skończyła się 3-0. Mistrzowie mają pierwszą ligową porażkę. Manchester City ma nadal 12 punktów z czterech meczów. Niedziela nie wystartowała.',
        'Brighton.com: Pascal Groß 31, Charalampos Kostoulas 45, Chema Andrés 57. Sky, The Athletic, The Guardian i ESPN drukują to samo 3-0. Groß i Kostoulas z dystansu. Andrés główkował rożny Grossa. Opta: 16 goli Brighton, najlepszy wynik ligi.',
        'Xinhua po sobocie: City 12 z czterech, Arsenal 12 z pięciu, Brighton 10. Niedziela jest w terminarzu, nie skończona. ESPN 20 września nadal drukuje vs. Nie wymyślaj niedzielnego wyniku.',
      ],
    },
    zh: {
      title: '布莱顿 3-0 阿森纳：卫冕冠军落败，周日仍开放',
      subtitle: '格罗斯、科斯图拉斯、切马·安德烈斯。曼城仍是 4 胜，少赛一轮。第 5 轮尚未结束。',
      excerpt: '9 月 19 日布莱顿在 Amex 3-0 击败阿森纳。天空、The Athletic 与布莱顿官网印同一比分。新华社：曼城 4 轮 12 分，阿森纳 5 轮 12 分，布莱顿 10 分。',
      body: [
        '阿森纳以 4 胜 0 平 0 负到来。布莱顿是联赛进球最多的球队。周六 Amex 结束于 3-0。卫冕冠军有了第一场联赛失利。曼城仍是 4 轮 12 分。周日尚未开球。',
        '布莱顿官网：帕斯卡尔·格罗斯 31 分钟，哈拉兰波斯·科斯图拉斯 45 分钟，切马·安德烈斯 57 分钟。天空、The Athletic、卫报与 ESPN 印同一 3-0。格罗斯与科斯图拉斯远射。安德烈斯头球攻入格罗斯角球。Opta：布莱顿 16 球，联赛最多。',
        '新华社周六后：曼城 4 轮 12 分，阿森纳 5 轮 12 分，布莱顿 10 分。周日已排期，未结束。ESPN 9 月 20 日比分板仍是 vs。不要编造周日比分。',
      ],
    },
    ja: {
      title: 'ブライトン 3-0 アーセナル：王者が負け、日曜はまだ開いている',
      subtitle: 'グロス、コストウラス、チェマ・アンドレス。シティはなお4勝で試合消化が少ない。第5節は終わっていない。',
      excerpt: '9月19日、ブライトンがAmexでアーセナルに3-0。Sky、The Athletic、ブライトン公式が同じスコア。新華社：シティ4試合12、アーセナル5試合12、ブライトン10。',
      body: [
        'アーセナルは4勝0分0敗で来た。ブライトンは得点首位。土曜のAmexは3-0で終わった。王者に今季初のリーグ黒星。マンチェスター・シティはなお4試合12点。日曜は未キックオフ。',
        'ブライトン公式：パスカル・グロス31分、ハラランボス・コストウラス45分、チェマ・アンドレス57分。Sky、The Athletic、ガーディアン、ESPNは同じ3-0。グロスとコストウラスは距離から。アンドレスはグロスのコーナーをヘッド。Opta：ブライトン16得点、リーグ最多。',
        '新華社の土曜後：シティ4試合12、アーセナル5試合12、ブライトン10。日曜は日程にあり、終了していない。ESPNの9月20日ボードはまだvs。日曜のスコアを作らない。',
      ],
    },
    ko: {
      title: '브라이턴 3-0 아스널: 챔피언이 지고, 일요일은 열려 있다',
      subtitle: '그로스, 코스툴라스, 체마 안드레스. 시티는 여전히 4승에 한 경기를 덜 했다. 5라운드는 끝나지 않았다.',
      excerpt: '9월 19일 브라이턴이 Amex에서 아스널을 3-0으로 이겼다. 스카이, The Athletic, 브라이턴 공식 사이트가 같은 스코어. 신화사: 시티 4경기 12점, 아스널 5경기 12점, 브라이턴 10점.',
      body: [
        '아스널은 4승 0무 0패로 왔다. 브라이턴은 득점 선두. 토요일 Amex는 3-0으로 끝났다. 챔피언의 첫 리그 패배. 맨체스터 시티는 여전히 4경기 12점. 일요일은 킥오프 전.',
        '브라이턴 공식: 파스칼 그로스 31분, 하랄람보스 코스툴라스 45분, 체마 안드레스 57분. 스카이, The Athletic, 가디언, ESPN이 같은 3-0. 그로스와 코스툴라스는 거리에서. 안드레스는 그로스 코너를 헤더. Opta: 브라이턴 16골, 리그 최다.',
        '신화사 토요일 후: 시티 4경기 12점, 아스널 5경기 12점, 브라이턴 10점. 일요일은 일정에 있고 끝나지 않았다. ESPN 9월 20일 보드는 아직 vs. 일요일 점수를 만들지 마라.',
      ],
    },
    ar: {
      title: 'برايتون 3-0 أرسنال: الأبطال يسقطون والأحد ما زال مفتوحًا',
      subtitle: 'غروس وكوستولاس وشيما أندريس. سيتي ما زال 4-0-0 بمباراة أقل. الجولة 5 لم تغلق.',
      excerpt: 'برايتون يهزم أرسنال 3-0 في الأميكس في 19 أيلول/سبتمبر. سكاي وThe Athletic وموقع برايتون يطبعون النتيجة نفسها. شينخوا: سيتي 12 من أربع، أرسنال 12 من خمس، برايتون 10.',
      body: [
        'وصل أرسنال 4-0-0. برايتون يتصدر الهدافين. انتهى السبت في الأميكس 3-0. للأبطال أول خسارة دوري. مانشستر سيتي ما زال 12 نقطة من أربع مباريات. الأحد لم ينطلق.',
        'موقع برايتون: باسكال غروس 31، هارالامبوس كوستولاس 45، شيما أندريس 57. سكاي وThe Athletic والغارديان وESPN يطبعون 3-0 نفسه. غروس وكوستولاس من بعيد. أندريس رأس ركنية غروس. أوبتا: 16 هدفًا لبرايتون، الأكثر في الدوري.',
        'شينخوا بعد السبت: سيتي 12 من أربع، أرسنال 12 من خمس، برايتون 10. الأحد مدرج غير مكتمل. لوحة ESPN في 20 أيلول/سبتمبر ما زالت vs. لا تخترع نتيجة الأحد.',
      ],
    },
  },
  'bmw-pga-celli-54-holes': {
    fr: {
      title: 'Celli et Elvira à 13 sous après 54 trous. Dimanche n’a pas de champion.',
      subtitle: 'AP : tous deux 203. Gerard a cardé 75. McIlroy a eaglé le 18. Le 4e tour est aujourd’hui. N’inventez pas un vainqueur.',
      excerpt: 'Filippo Celli et Manuel Elvira partagent la tête du BMW PGA à 13 sous après trois tours. AP imprime 203. Gerard, leader à 36 trous, est à 207. Le 4e tour est le 20 septembre.',
      body: [
        'Le BMW PGA est le phare du DP World Tour. Après 54 trous à Wentworth, deux noms sont à 13 sous et il n’y a pas de vainqueur. C’est la ligne honnête du 20 septembre.',
        'AP : Filippo Celli 68-66-69, 203. Manuel Elvira 69-66-68, 203. Del Rey, Spaun et Veerman 204. McIlroy 205. Gerard, leader à 36 trous, 67-65-75, 207. CBS : eagle de McIlroy au 18. FOX et Today’s Golfer impriment Celli et Elvira co-leaders.',
        'N’imprimez pas un champion. Le 4e tour est le 20 septembre. La Presidents Cup reste les 24-27 septembre à Medinah.',
      ],
    },
    es: {
      title: 'Celli y Elvira a 13 bajo tras 54 hoyos. El domingo no tiene campeón.',
      subtitle: 'AP: ambos 203. Gerard firmó 75. McIlroy hizo eagle en el 18. La 4ª ronda es hoy. No inventes un ganador.',
      excerpt: 'Filippo Celli y Manuel Elvira comparten el liderato del BMW PGA a 13 bajo tras tres vueltas. AP imprime 203. Gerard, líder a 36 hoyos, está en 207. La 4ª ronda es el 20 de septiembre.',
      body: [
        'El BMW PGA es el buque insignia del DP World Tour. Tras 54 hoyos en Wentworth hay dos nombres a 13 bajo y no hay ganador. Esa es la línea honesta del 20 de septiembre.',
        'AP: Filippo Celli 68-66-69, 203. Manuel Elvira 69-66-68, 203. Del Rey, Spaun y Veerman 204. McIlroy 205. Gerard, líder a 36, 67-65-75, 207. CBS: eagle de McIlroy en el 18. FOX y Today’s Golfer imprimen a Celli y Elvira como colíderes.',
        'No imprimas un campeón. La 4ª ronda es el 20 de septiembre. La Presidents Cup sigue el 24-27 de septiembre en Medinah.',
      ],
    },
    de: {
      title: 'Celli und Elvira 13 unter nach 54 Löchern. Sonntag hat keinen Champion.',
      subtitle: 'AP: beide 203. Gerard spielte 75. McIlroy eaglete 18. Runde 4 ist heute. Keinen Sieger erfinden.',
      excerpt: 'Filippo Celli und Manuel Elvira teilen die BMW-PGA-Führung bei 13 unter nach drei Runden. AP druckt 203. Gerard, 36-Loch-Leader, steht bei 207. Runde 4 ist der 20. September.',
      body: [
        'Die BMW PGA ist das Flaggschiff der DP World Tour. Nach 54 Löchern in Wentworth stehen zwei Namen bei 13 unter, und es gibt keinen Sieger. Das ist die ehrliche Zeile am 20. September.',
        'AP: Filippo Celli 68-66-69, 203. Manuel Elvira 69-66-68, 203. Del Rey, Spaun und Veerman 204. McIlroy 205. Gerard, 36-Loch-Leader, 67-65-75, 207. CBS: McIlroy-Eagle auf 18. FOX und Today’s Golfer drucken Celli und Elvira als Co-Leader.',
        'Keinen Champion drucken. Runde 4 ist der 20. September. Der Presidents Cup bleibt 24.-27. September in Medinah.',
      ],
    },
    it: {
      title: 'Celli ed Elvira a 13 sotto dopo 54 buche. La domenica non ha un campione.',
      subtitle: 'AP: entrambi 203. Gerard ha chiuso 75. McIlroy ha eagled il 18. Il 4º giro è oggi. Non inventare un vincitore.',
      excerpt: 'Filippo Celli e Manuel Elvira condividono il comando del BMW PGA a 13 sotto dopo tre giri. AP stampa 203. Gerard, leader a 36 buche, è a 207. Il 4º giro è il 20 settembre.',
      body: [
        'Il BMW PGA è la bandiera del DP World Tour. Dopo 54 buche a Wentworth ci sono due nomi a 13 sotto e non c’è un vincitore. Questa è la riga onesta del 20 settembre.',
        'AP: Filippo Celli 68-66-69, 203. Manuel Elvira 69-66-68, 203. Del Rey, Spaun e Veerman 204. McIlroy 205. Gerard, leader a 36, 67-65-75, 207. CBS: eagle di McIlroy al 18. FOX e Today’s Golfer stampano Celli ed Elvira co-leader.',
        'Non stampare un campione. Il 4º giro è il 20 settembre. La Presidents Cup resta il 24-27 settembre a Medinah.',
      ],
    },
    pl: {
      title: 'Celli i Elvira 13 poniżej po 54 dołkach. Niedziela nie ma mistrza.',
      subtitle: 'AP: obaj 203. Gerard zagrał 75. McIlroy eagle na 18. 4. runda jest dzisiaj. Nie wymyślaj zwycięzcy.',
      excerpt: 'Filippo Celli i Manuel Elvira dzielą prowadzenie BMW PGA przy 13 poniżej po trzech rundach. AP drukuje 203. Gerard, lider po 36, ma 207. 4. runda 20 września.',
      body: [
        'BMW PGA to flagowiec DP World Tour. Po 54 dołkach w Wentworth są dwa nazwiska na 13 poniżej i nie ma zwycięzcy. To uczciwa linia na 20 września.',
        'AP: Filippo Celli 68-66-69, 203. Manuel Elvira 69-66-68, 203. Del Rey, Spaun i Veerman 204. McIlroy 205. Gerard, lider po 36, 67-65-75, 207. CBS: eagle McIlroya na 18. FOX i Today’s Golfer drukują Celliego i Elvirę jako współliderów.',
        'Nie drukuj mistrza. 4. runda jest 20 września. Presidents Cup nadal 24-27 września w Medinah.',
      ],
    },
    zh: {
      title: '切利与埃尔维拉 54 洞后低于标准杆 13 杆。周日没有冠军。',
      subtitle: '美联社：两人同为 203。杰拉德打出 75。麦克罗伊在 18 号鹰击。第 4 轮就是今天。不要编造冠军。',
      excerpt: '菲利波·切利与曼努埃尔·埃尔维拉在三轮后并列宝马 PGA 领先，低于标准杆 13 杆。美联社印 203。36 洞领先者杰拉德为 207。第 4 轮是 9 月 20 日。',
      body: [
        '宝马 PGA 是 DP 世界巡回赛旗舰。温特沃斯 54 洞后有两个名字在 13 杆下，没有冠军。这是 9 月 20 日的诚实写法。',
        '美联社：切利 68-66-69，203。埃尔维拉 69-66-68，203。德尔雷伊、斯庞、维尔曼 204。麦克罗伊 205。杰拉德 67-65-75，207。CBS：麦克罗伊 18 号鹰击。FOX 与 Today’s Golfer 印切利与埃尔维拉并列领先。',
        '不要印冠军。第 4 轮是 9 月 20 日。总统杯仍是 9 月 24-27 日在麦迪纳。',
      ],
    },
    ja: {
      title: 'チェッリとエルビラが54ホール後13アンダー。日曜に優勝者はいない。',
      subtitle: 'AP：ともに203。ジェラルドは75。マキロイは18番でイーグル。第4ラウンドは今日。優勝者を作らない。',
      excerpt: 'フィリッポ・チェッリとマヌエル・エルビラが3ラウンド後BMW PGAを13アンダーで分け合う。APは203。36ホール首位のジェラルドは207。第4ラウンドは9月20日。',
      body: [
        'BMW PGAはDPワールドツアーの旗艦。ウェントワース54ホール後、13アンダーに二つの名前があり、優勝者はいない。それが9月20日の正直な一文。',
        'AP：チェッリ 68-66-69、203。エルビラ 69-66-68、203。デル・レイ、スポーン、ヴィアマン 204。マキロイ 205。ジェラルド 67-65-75、207。CBS：マキロイ18番イーグル。FOXとToday’s Golferはチェッリとエルビラを共同首位と印刷。',
        '優勝者を印刷しない。第4ラウンドは9月20日。プレジデンツカップはなお9月24-27日、メディナ。',
      ],
    },
    ko: {
      title: '첼리와 엘비라, 54홀 후 13언더. 일요일에는 챔피언이 없다.',
      subtitle: 'AP: 둘 다 203. 제라드는 75. 맥길로이는 18번 이글. 4라운드는 오늘. 우승자를 만들지 마라.',
      excerpt: '필리포 첼리와 마누엘 엘비라가 3라운드 후 BMW PGA를 13언더로 나눠 갖는다. AP는 203. 36홀 선두 제라드는 207. 4라운드는 9월 20일.',
      body: [
        'BMW PGA는 DP 월드 투어 플래그십이다. 웬트워스 54홀 후 13언더에 두 이름이 있고 우승자는 없다. 그것이 9월 20일의 정직한 한 줄이다.',
        'AP: 첼리 68-66-69, 203. 엘비라 69-66-68, 203. 델 레이, 스폰, 비어먼 204. 맥길로이 205. 제라드 67-65-75, 207. CBS: 맥길로이 18번 이글. FOX와 Today’s Golfer는 첼리와 엘비라를 공동 선두로 인쇄한다.',
        '챔피언을 인쇄하지 마라. 4라운드는 9월 20일. 프레지던츠컵은 여전히 9월 24-27일 메디나.',
      ],
    },
    ar: {
      title: 'تشيللي وإلفيرا تحت البار بـ13 بعد 54 حفرة. الأحد بلا بطل.',
      subtitle: 'AP: كلاهما 203. جيرارد سجّل 75. ماكلروي نسر 18. الجولة 4 اليوم. لا تخترع فائزًا.',
      excerpt: 'فيليبو تشيللي ومانويل إلفيرا يتقاسمان صدارة BMW PGA عند 13 تحت بعد ثلاثة أشواط. AP تطبع 203. جيرارد، متصدر الـ36، عند 207. الجولة 4 في 20 أيلول/سبتمبر.',
      body: [
        'بطولة BMW PGA هي علم جولة DP العالمية. بعد 54 حفرة في وينتوورث اسمان عند 13 تحت ولا فائز. هذا السطر الصادق في 20 أيلول/سبتمبر.',
        'AP: تشيللي 68-66-69، 203. إلفيرا 69-66-68، 203. ديل ري وسبون وفيرمان 204. ماكلروي 205. جيرارد 67-65-75، 207. CBS: نسر ماكلروي على 18. FOX وToday’s Golfer يطبعان تشيللي وإلفيرا متصدرين معًا.',
        'لا تطبع بطلًا. الجولة 4 في 20 أيلول/سبتمبر. كأس الرؤساء ما زال 24-27 أيلول/سبتمبر في مدينا.',
      ],
    },
  },
  'week2-sunday-slate-2026': {
    fr: {
      title: 'Le dimanche de la semaine 2 est listé. Bills 41-31 reste le seul final.',
      subtitle: 'CBS et FOX impriment 14 coups d’envoi dimanche plus Monday Night. Aucun de ces matches n’a été joué. N’inventez pas un score.',
      excerpt: 'Buffalo a battu Detroit 41-31 jeudi. CBS : Colts chez Chiefs le dimanche soir, 20 h 20 ET, NBC. Chaque autre match de la semaine 2 après jeudi est encore une heure, pas un résultat.',
      body: [
        'Jeudi a ouvert la semaine 2 dans un nouveau Highmark Stadium. Buffalo 41, Detroit 31. ESPN : Josh Allen, cinq touchdowns au total. C’est le seul final imprimé de la semaine 2. Le dimanche 20 septembre est une feuille, pas une box.',
        'CBS et FOX : huit matches à 13 h ET, dont Steelers chez Patriots et Bengals chez Texans. Sunday Night : Colts chez Chiefs, 20 h 20 ET, NBC, Arrowhead. Monday Night : Giants chez Rams, 21 septembre, ABC.',
        'N’imprimez pas un vainqueur du dimanche. Bills 41-31 est le résultat verrouillé. Le reste de la semaine 2 n’a pas été joué.',
      ],
    },
    es: {
      title: 'El domingo de la semana 2 está listado. Bills 41-31 sigue siendo el único final.',
      subtitle: 'CBS y FOX imprimen 14 saques del domingo más el Monday Night. Ninguno de esos partidos se ha jugado. No inventes un marcador.',
      excerpt: 'Buffalo ganó 41-31 a Detroit el jueves. CBS: Colts en casa de Chiefs el domingo noche, 20:20 ET, NBC. Cualquier otro partido de la semana 2 después del jueves sigue siendo una hora, no un resultado.',
      body: [
        'El jueves abrió la semana 2 en el nuevo Highmark Stadium. Buffalo 41, Detroit 31. ESPN: Josh Allen, cinco touchdowns en total. Ese es el único final impreso de la semana 2. El domingo 20 de septiembre es una hoja, no un box score.',
        'CBS y FOX: ocho partidos a la 13:00 ET. Sunday Night: Colts en Kansas City, 20:20 ET, NBC, Arrowhead. Monday Night: Giants en Rams, 21 de septiembre, ABC.',
        'No imprimas un ganador del domingo. Bills 41-31 es el resultado cerrado. El resto de la semana 2 no se ha jugado.',
      ],
    },
    de: {
      title: 'Der Sonntag von Woche 2 ist gelistet. Bills 41:31 bleibt der einzige Endstand.',
      subtitle: 'CBS und FOX drucken 14 Sonntags-Anstoßzeiten plus Monday Night. Keines dieser Spiele ist gespielt. Keinen Score erfinden.',
      excerpt: 'Buffalo schlug Detroit 41:31 am Donnerstag. CBS: Colts bei Chiefs am Sunday Night, 20:20 ET, NBC. Jedes andere Woche-2-Spiel nach Donnerstag ist noch eine Uhrzeit, kein Ergebnis.',
      body: [
        'Donnerstag öffnete Woche 2 in einem neuen Highmark Stadium. Buffalo 41, Detroit 31. ESPN: Josh Allen fünf Touchdowns insgesamt. Das ist der einzige gedruckte Woche-2-Endstand. Sonntag, 20. September, ist ein Blatt, kein Boxscore.',
        'CBS und FOX: acht Spiele um 13:00 ET. Sunday Night: Colts bei Chiefs, 20:20 ET, NBC, Arrowhead. Monday Night: Giants bei Rams, 21. September, ABC.',
        'Keinen Sonntagssieger drucken. Bills 41:31 ist das verriegelte Ergebnis. Der Rest von Woche 2 ist nicht gespielt.',
      ],
    },
    it: {
      title: 'La domenica della Week 2 è in elenco. Bills 41-31 resta l’unico finale.',
      subtitle: 'CBS e FOX stampano 14 kickoff domenicali più il Monday Night. Nessuna di quelle partite è stata giocata. Non inventare un punteggio.',
      excerpt: 'Buffalo ha battuto Detroit 41-31 giovedì. CBS: Colts dai Chiefs la domenica sera, 20:20 ET, NBC. Ogni altra partita della Week 2 dopo giovedì è ancora un orario, non un risultato.',
      body: [
        'Giovedì ha aperto la Week 2 nel nuovo Highmark Stadium. Buffalo 41, Detroit 31. ESPN: Josh Allen cinque touchdown totali. È l’unico finale stampato della Week 2. Domenica 20 settembre è un tabellone, non un box.',
        'CBS e FOX: otto partite alle 13:00 ET. Sunday Night: Colts dai Chiefs, 20:20 ET, NBC, Arrowhead. Monday Night: Giants dai Rams, 21 settembre, ABC.',
        'Non stampare un vincitore della domenica. Bills 41-31 è il risultato bloccato. Il resto della Week 2 non è stato giocato.',
      ],
    },
    pl: {
      title: 'Niedziela tygodnia 2 jest w terminarzu. Bills 41-31 nadal jedynym finałem.',
      subtitle: 'CBS i FOX drukują 14 niedzielnych kickoffów plus Monday Night. Żaden z tych meczów nie został rozegrany. Nie wymyślaj wyniku.',
      excerpt: 'Buffalo pokonało Detroit 41-31 w czwartek. CBS: Colts u Chiefs w niedzielę wieczorem, 20:20 ET, NBC. Każdy inny mecz tygodnia 2 po czwartku to wciąż godzina, nie wynik.',
      body: [
        'Czwartek otworzył tydzień 2 na nowym Highmark Stadium. Buffalo 41, Detroit 31. ESPN: Josh Allen pięć przyłożeń łącznie. To jedyny wydrukowany finał tygodnia 2. Niedziela 20 września to karta, nie box.',
        'CBS i FOX: osiem meczów o 13:00 ET. Sunday Night: Colts u Chiefs, 20:20 ET, NBC, Arrowhead. Monday Night: Giants u Rams, 21 września, ABC.',
        'Nie drukuj niedzielnego zwycięzcy. Bills 41-31 to zablokowany wynik. Reszta tygodnia 2 nie została rozegrana.',
      ],
    },
    zh: {
      title: '第二周周日已排期。比尔 41-31 仍是唯一完场。',
      subtitle: 'CBS 与 FOX 印出 14 场周日开球加周一晚。这些比赛都还没打。不要编造比分。',
      excerpt: '布法罗周四 41-31 击败底特律。CBS：小马客场挑战酋长，周日夜 美东 20:20，NBC。周四之后的第二周其余场次仍是时间，不是结果。',
      body: [
        '周四在新高通球场打开第二周。布法罗 41，底特律 31。ESPN：乔什·艾伦合计 5 次达阵。这是第二周唯一印出的完场。9 月 20 日周日是赛程，不是技术统计。',
        'CBS 与 FOX：美东 13:00 八场。周日夜：小马挑战酋长，美东 20:20，NBC，箭头球场。周一晚：巨人挑战公羊，9 月 21 日，ABC。',
        '不要印周日赢家。比尔 41-31 是锁定结果。第二周其余尚未进行。',
      ],
    },
    ja: {
      title: '第2週の日曜は日程にある。ビルズ 41-31 が唯一の決勝スコア。',
      subtitle: 'CBSとFOXは日曜14試合とマンデーナイトを印刷。どれも未実施。スコアを作らない。',
      excerpt: 'バッファローが木曜にデトロイトを41-31。CBS：コルツがチーフスへ、サンデーナイト東部20:20、NBC。木曜以降の第2週はまだ時刻であり、結果ではない。',
      body: [
        '木曜が新ハイマークで第2週を開いた。バッファロー41、デトロイト31。ESPN：ジョシュ・アレン合計5TD。それが第2週で印刷された唯一の決勝。9月20日日曜はカードであり、ボックスではない。',
        'CBSとFOX：東部13:00に8試合。サンデーナイト：コルツ対チーフス、東部20:20、NBC、アローヘッド。マンデーナイト：ジャイアンツ対ラムズ、9月21日、ABC。',
        '日曜の勝者を印刷しない。ビルズ 41-31 が固定結果。第2週の残りは未実施。',
      ],
    },
    ko: {
      title: '2주차 일요일이 일정에 있다. 빌스 41-31이 유일한 최종 스코어다.',
      subtitle: 'CBS와 FOX가 일요일 14경기와 먼데이 나이트를 인쇄한다. 그 경기들은 아직 없다. 점수를 만들지 마라.',
      excerpt: '버펄로가 목요일 디트로이트를 41-31로 이겼다. CBS: 콜츠가 치프스 원정, 선데이 나이트 동부 20:20, NBC. 목요일 이후 2주차는 아직 시간이지 결과가 아니다.',
      body: [
        '목요일이 새 하이마크에서 2주차를 열었다. 버펄로 41, 디트로이트 31. ESPN: 조시 앨런 합계 5TD. 그것이 인쇄된 유일한 2주차 최종. 9월 20일 일요일은 카드이지 박스가 아니다.',
        'CBS와 FOX: 동부 13:00 여덟 경기. 선데이 나이트: 콜츠 대 치프스, 동부 20:20, NBC, 애로헤드. 먼데이 나이트: 자이언츠 대 램스, 9월 21일, ABC.',
        '일요일 승자를 인쇄하지 마라. 빌스 41-31이 잠긴 결과다. 2주차 나머지는 아직 없다.',
      ],
    },
    ar: {
      title: 'أحد الأسبوع 2 مدرج. بيلز 41-31 ما زال النهائي الوحيد.',
      subtitle: 'CBS وFOX يطبعان 14 انطلاقة أحد بالإضافة إلى ليلة الاثنين. لم تُلعب أي منها. لا تخترع نتيجة.',
      excerpt: 'بوفالو فاز على ديترويت 41-31 الخميس. CBS: كولتس عند تشيفز الأحد ليلًا، 20:20 شرقًا، NBC. كل مباراة أخرى في الأسبوع 2 بعد الخميس ما زالت وقتًا لا نتيجة.',
      body: [
        'الخميس فتح الأسبوع 2 في ملعب هايمارك الجديد. بوفالو 41، ديترويت 31. ESPN: جوش ألين خمسة لمسات أرضية إجمالاً. هذا النهائي المطبوع الوحيد للأسبوع 2. الأحد 20 أيلول/سبتمبر ورقة لا صندوق إحصاء.',
        'CBS وFOX: ثماني مباريات في 13:00 شرقًا. ليلة الأحد: كولتس عند تشيفز، 20:20 شرقًا، NBC، أروهيد. ليلة الاثنين: جاينتس عند رامز، 21 أيلول/سبتمبر، ABC.',
        'لا تطبع فائز الأحد. بيلز 41-31 هي النتيجة المقفلة. بقية الأسبوع 2 لم تُلعب.',
      ],
    },
  },
  'laver-cup-london-2026': {
    fr: {
      title: 'La Laver Cup est les 25-27 septembre à The O2. L’US Open a déjà ses noms.',
      subtitle: 'Zverev et Rybakina ont fermé Flushing. Sky liste l’Europe contre le Monde à Londres. Aucun match de Laver Cup n’a été joué.',
      excerpt: 'Team Europe contre Team World, The O2, 25-27 septembre. Wikipedia : Nakashima a remplacé Shelton. Premier à 13 points. N’inventez pas un vainqueur.',
      body: [
        'L’US Open est close. Zverev a battu Shelton. Rybakina a battu Sabalenka. La prochaine date de tennis par équipes imprimée est la Laver Cup à The O2.',
        'Sky Sports : vendredi 25 au dimanche 27 septembre, The O2. Wikipedia : Team Europe Zverev, Alcaraz, Cobolli, Jódar, Menšík, Ruud. Team World Nakashima, de Minaur, Fritz, Tien, Bublik, Cerúndolo. Shelton forfait le 17 septembre.',
        'N’imprimez pas un champion 2026 de Laver Cup. Les matches n’ont pas été joués. Revenez après le 25 septembre.',
      ],
    },
    es: {
      title: 'La Laver Cup es el 25-27 de septiembre en The O2. El US Open ya tiene nombres.',
      subtitle: 'Zverev y Rybakina cerraron Flushing. Sky lista a Europa contra el Mundo en Londres. No se ha jugado ningún partido de Laver Cup.',
      excerpt: 'Team Europe vs Team World, The O2, 25-27 de septiembre. Wikipedia: Nakashima sustituyó a Shelton. Primero a 13 puntos. No inventes un ganador.',
      body: [
        'El US Open está cerrado. Zverev ganó a Shelton. Rybakina ganó a Sabalenka. La siguiente fecha impresa de tenis por equipos es la Laver Cup en The O2.',
        'Sky Sports: viernes 25 a domingo 27 de septiembre, The O2. Wikipedia: Team Europe Zverev, Alcaraz, Cobolli, Jódar, Menšík, Ruud. Team World Nakashima, de Minaur, Fritz, Tien, Bublik, Cerúndolo. Shelton se retiró el 17 de septiembre.',
        'No imprimas un campeón 2026 de Laver Cup. Los partidos no se han jugado. Vuelve después del 25 de septiembre.',
      ],
    },
    de: {
      title: 'Der Laver Cup ist 25.-27. September in der O2. Die US Open haben schon Namen.',
      subtitle: 'Zverev und Rybakina haben Flushing geschlossen. Sky listet Europa gegen die Welt in London. Kein Laver-Cup-Match ist gespielt.',
      excerpt: 'Team Europe gegen Team World, The O2, 25.-27. September. Wikipedia: Nakashima ersetzte Shelton. Erster zu 13 Punkten. Keinen Sieger erfinden.',
      body: [
        'Die US Open sind zu. Zverev schlug Shelton. Rybakina schlug Sabalenka. Das nächste gedruckte Team-Tennis-Datum ist der Laver Cup in der O2.',
        'Sky Sports: Freitag 25. bis Sonntag 27. September, The O2. Wikipedia: Team Europe Zverev, Alcaraz, Cobolli, Jódar, Menšík, Ruud. Team World Nakashima, de Minaur, Fritz, Tien, Bublik, Cerúndolo. Shelton zog am 17. September zurück.',
        'Keinen Laver-Cup-Champion 2026 drucken. Die Matches sind nicht gespielt. Komm nach dem 25. September zurück.',
      ],
    },
    it: {
      title: 'La Laver Cup è il 25-27 settembre all’O2. Gli US Open hanno già i nomi.',
      subtitle: 'Zverev e Rybakina hanno chiuso Flushing. Sky elenca l’Europa contro il Mondo a Londra. Nessun match di Laver Cup è stato giocato.',
      excerpt: 'Team Europe vs Team World, The O2, 25-27 settembre. Wikipedia: Nakashima ha sostituito Shelton. Primo a 13 punti. Non inventare un vincitore.',
      body: [
        'Gli US Open sono chiusi. Zverev ha battuto Shelton. Rybakina ha battuto Sabalenka. La prossima data stampata di tennis a squadre è la Laver Cup all’O2.',
        'Sky Sports: venerdì 25-domenica 27 settembre, The O2. Wikipedia: Team Europe Zverev, Alcaraz, Cobolli, Jódar, Menšík, Ruud. Team World Nakashima, de Minaur, Fritz, Tien, Bublik, Cerúndolo. Shelton si è ritirato il 17 settembre.',
        'Non stampare un campione 2026 della Laver Cup. I match non sono stati giocati. Torna dopo il 25 settembre.',
      ],
    },
    pl: {
      title: 'Laver Cup 25-27 września na O2. US Open już ma nazwiska.',
      subtitle: 'Zverev i Rybakina zamknęli Flushing. Sky wymienia Europę przeciw Światu w Londynie. Żaden mecz Laver Cup nie został rozegrany.',
      excerpt: 'Team Europe vs Team World, The O2, 25-27 września. Wikipedia: Nakashima zastąpił Sheltona. Pierwszy do 13 punktów. Nie wymyślaj zwycięzcy.',
      body: [
        'US Open jest zamknięty. Zverev pokonał Sheltona. Rybakina pokonała Sabalenkę. Następna drukowana data tenisa drużynowego to Laver Cup na O2.',
        'Sky Sports: piątek 25 do niedzieli 27 września, The O2. Wikipedia: Team Europe Zverev, Alcaraz, Cobolli, Jódar, Menšík, Ruud. Team World Nakashima, de Minaur, Fritz, Tien, Bublik, Cerúndolo. Shelton wycofał się 17 września.',
        'Nie drukuj mistrza Laver Cup 2026. Mecze nie zostały rozegrane. Wróć po 25 września.',
      ],
    },
    zh: {
      title: '拉沃尔杯 9 月 25-27 日在 O2。美网已经有名字。',
      subtitle: '兹维列夫和莱巴金娜关闭了法拉盛。天空列出欧洲对世界在伦敦。拉沃尔杯尚未开打。',
      excerpt: '欧洲队对世界队，O2，9 月 25-27 日。维基百科：中岛接替谢尔顿。先到 13 分。不要编造冠军。',
      body: [
        '美网已结束。兹维列夫击败谢尔顿。莱巴金娜击败萨巴伦卡。下一份印出的团体网球日期是 O2 的拉沃尔杯。',
        '天空体育：9 月 25 日周五至 27 日周日，O2。维基百科：欧洲队兹维列夫、阿尔卡拉斯、科博利、霍达尔、门希克、鲁德。世界队中岛、德米纳尔、弗里茨、田、布布利克、塞伦多洛。谢尔顿 9 月 17 日退出。',
        '不要印 2026 拉沃尔杯冠军。比赛尚未进行。9 月 25 日后再来。',
      ],
    },
    ja: {
      title: 'レーバーカップは9月25-27日、O2。全米オープンにはすでに名前がある。',
      subtitle: 'ズベレフとリバキナがフラッシングを閉じた。Skyはロンドンで欧州対世界を掲載。レーバーカップの試合は未実施。',
      excerpt: 'チーム欧州対チーム世界、O2、9月25-27日。ウィキペディア：ナカシマがシェルトンの代わり。先に13ポイント。優勝者を作らない。',
      body: [
        '全米オープンは終了。ズベレフがシェルトンを破った。リバキナがサバレンカを破った。次に印刷された団体テニスの日付はO2のレーバーカップ。',
        'Sky Sports：9月25日金曜から27日日曜、O2。ウィキペディア：欧州はズベレフ、アルカラス、コボリ、ホダル、メンシク、ルード。世界はナカシマ、デミノー、フリッツ、ティエン、ブブリク、セルンドロ。シェルトンは9月17日に欠場。',
        '2026レーバーカップ優勝者を印刷しない。試合は未実施。9月25日以降に戻る。',
      ],
    },
    ko: {
      title: '레이버컵은 9월 25-27일 O2. US오픈에는 이미 이름이 있다.',
      subtitle: '즈베레프와 리바키나가 플러싱을 닫았다. 스카이가 런던에서 유럽 대 월드를 올린다. 레이버컵 경기는 아직 없다.',
      excerpt: '팀 유럽 대 팀 월드, O2, 9월 25-27일. 위키피디아: 나카시마가 셸턴을 대체. 13점 선착. 우승자를 만들지 마라.',
      body: [
        'US오픈은 끝났다. 즈베레프가 셸턴을 이겼다. 리바키나가 사발렌카를 이겼다. 다음 인쇄된 단체 테니스 일정은 O2 레이버컵이다.',
        'Sky Sports: 9월 25일 금요일부터 27일 일요일, O2. 위키피디아: 유럽은 즈베레프, 알카라스, 코볼리, 호다르, 멘시크, 루드. 월드는 나카시마, 드미나우르, 프리츠, 티엔, 부블릭, 세룬돌로. 셸턴은 9월 17일 기권.',
        '2026 레이버컵 챔피언을 인쇄하지 마라. 경기는 아직 없다. 9월 25일 이후에 돌아오라.',
      ],
    },
    ar: {
      title: 'كأس لافر 25-27 أيلول/سبتمبر في O2. أمريكا المفتوحة لها أسماء أصلًا.',
      subtitle: 'زفيريف وريباكينا أغلقا فلاشينغ. سكاي تدرج أوروبا ضد العالم في لندن. لم تُلعب أي مباراة لكأس لافر.',
      excerpt: 'فريق أوروبا ضد فريق العالم، O2، 25-27 أيلول/سبتمبر. ويكيبيديا: ناكاشيما بدل شيلتون. أول من يصل 13 نقطة. لا تخترع فائزًا.',
      body: [
        'أمريكا المفتوحة أغلقت. زفيريف فاز على شيلتون. ريباكينا فازت على سابالينكا. التاريخ المطبوع التالي لتنس الفرق هو كأس لافر في O2.',
        'سكاي سبورتس: الجمعة 25 إلى الأحد 27 أيلول/سبتمبر، O2. ويكيبيديا: أوروبا زفيريف وألكاراز وكوبولي وخودار ومنشيك وروود. العالم ناكاشيما ودي مينور وفريتز وتيان وبوبليك وسيروندولو. شيلتون انسحب في 17 أيلول/سبتمبر.',
        'لا تطبع بطل كأس لافر 2026. المباريات لم تُلعب. عد بعد 25 أيلول/سبتمبر.',
      ],
    },
  },
  'baku-gp-preview-2026': {
    fr: {
      title: 'Bakou, 24-26 septembre. Course samedi. Antonelli 292. Pas de résultat.',
      subtitle: 'Formula1.com liste les EL1 jeudi. Sky : qualifications vendredi, Grand Prix samedi midi UK. Madrid est classé. L’Azerbaïdjan ne l’est pas.',
      excerpt: 'Le Grand Prix d’Azerbaïdjan est un week-end jeudi-samedi au Baku City Circuit. Pilotes après Madrid : Antonelli 292, Russell 211, Hamilton 191. N’inventez pas un vainqueur.',
      body: [
        'Kimi Antonelli a gagné le premier Grand Prix de Madrid. Le championnat est 292-211-191. La course suivante n’est pas un dimanche en Europe. C’est un samedi à Bakou.',
        'Formula1.com : EL1 jeudi 24 septembre, qualifications vendredi 25, Grand Prix samedi 26. 51 tours de 6,003 km. Sky Sports : qualifications 13 h UK, course 12 h UK. Les essais n’ont pas commencé.',
        'N’imprimez pas une pole de Bakou ni un vainqueur du samedi. Revenez après le 26 septembre.',
      ],
    },
    es: {
      title: 'Bakú, 24-26 de septiembre. Carrera el sábado. Antonelli 292. Sin resultado.',
      subtitle: 'Formula1.com lista los FP1 el jueves. Sky: clasificación el viernes, Gran Premio el sábado al mediodía UK. Madrid está cerrado. Azerbaiyán no.',
      excerpt: 'El Gran Premio de Azerbaiyán es un fin de semana jueves-sábado en el Baku City Circuit. Pilotos tras Madrid: Antonelli 292, Russell 211, Hamilton 191. No inventes un ganador.',
      body: [
        'Kimi Antonelli ganó el primer Gran Premio de Madrid. El campeonato es 292-211-191. La siguiente carrera no es un domingo en Europa. Es un sábado en Bakú.',
        'Formula1.com: FP1 jueves 24 de septiembre, clasificación viernes 25, Gran Premio sábado 26. 51 vueltas de 6,003 km. Sky Sports: clasificación 13:00 UK, carrera 12:00 UK. Los entrenamientos no han empezado.',
        'No imprimas una pole de Bakú ni un ganador del sábado. Vuelve después del 26 de septiembre.',
      ],
    },
    de: {
      title: 'Baku, 24.-26. September. Rennen am Samstag. Antonelli 292. Kein Ergebnis.',
      subtitle: 'Formula1.com listet FP1 am Donnerstag. Sky: Qualifying Freitag, Grand Prix Samstag mittags UK. Madrid ist verbucht. Aserbaidschan nicht.',
      excerpt: 'Der Große Preis von Aserbaidschan ist ein Donnerstag-Samstag-Wochenende am Baku City Circuit. Fahrer nach Madrid: Antonelli 292, Russell 211, Hamilton 191. Keinen Sieger erfinden.',
      body: [
        'Kimi Antonelli gewann den ersten Großen Preis von Madrid. Die WM steht 292-211-191. Das nächste Rennen ist kein Sonntag in Europa. Es ist ein Samstag in Baku.',
        'Formula1.com: FP1 Donnerstag 24. September, Qualifying Freitag 25., Grand Prix Samstag 26. 51 Runden à 6,003 km. Sky Sports: Qualifying 13 Uhr UK, Rennen 12 Uhr UK. Das Training hat nicht begonnen.',
        'Keine Baku-Pole und keinen Samstagssieger drucken. Komm nach dem 26. September zurück.',
      ],
    },
    it: {
      title: 'Baku, 24-26 settembre. Gara il sabato. Antonelli 292. Nessun risultato.',
      subtitle: 'Formula1.com elenca le FP1 giovedì. Sky: qualifiche venerdì, Gran Premio sabato a mezzogiorno UK. Madrid è in archivio. L’Azerbaigian no.',
      excerpt: 'Il Gran Premio d’Azerbaigian è un weekend giovedì-sabato al Baku City Circuit. Piloti dopo Madrid: Antonelli 292, Russell 211, Hamilton 191. Non inventare un vincitore.',
      body: [
        'Kimi Antonelli ha vinto il primo Gran Premio di Madrid. Il campionato è 292-211-191. La prossima gara non è una domenica in Europa. È un sabato a Baku.',
        'Formula1.com: FP1 giovedì 24 settembre, qualifiche venerdì 25, Gran Premio sabato 26. 51 giri di 6,003 km. Sky Sports: qualifiche 13:00 UK, gara 12:00 UK. Le prove non sono iniziate.',
        'Non stampare una pole di Baku né un vincitore del sabato. Torna dopo il 26 settembre.',
      ],
    },
    pl: {
      title: 'Baku, 24-26 września. Wyścig w sobotę. Antonelli 292. Bez wyniku.',
      subtitle: 'Formula1.com wymienia FP1 w czwartek. Sky: kwalifikacje w piątek, Grand Prix w sobotę w południe UK. Madryt jest w książce. Azerbejdżan nie.',
      excerpt: 'Grand Prix Azerbejdżanu to weekend czwartek-sobota na Baku City Circuit. Kierowcy po Madrycie: Antonelli 292, Russell 211, Hamilton 191. Nie wymyślaj zwycięzcy.',
      body: [
        'Kimi Antonelli wygrał pierwsze Grand Prix Madrytu. Mistrzostwa to 292-211-191. Następny wyścig to nie niedziela w Europie. To sobota w Baku.',
        'Formula1.com: FP1 czwartek 24 września, kwalifikacje piątek 25, Grand Prix sobota 26. 51 okrążeń po 6,003 km. Sky Sports: kwalifikacje 13:00 UK, wyścig 12:00 UK. Treningi nie wystartowały.',
        'Nie drukuj pola Baku ani sobotniego zwycięzcy. Wróć po 26 września.',
      ],
    },
    zh: {
      title: '巴库，9 月 24-26 日。周六正赛。安东内利 292。没有结果。',
      subtitle: 'Formula1.com 列出周四 FP1。天空：周五排位，周六正午英国时间正赛。马德里已入账。阿塞拜疆没有。',
      excerpt: '阿塞拜疆大奖赛是巴库城市赛道的周四至周六周末。马德里后车手：安东内利 292，拉塞尔 211，汉密尔顿 191。不要编造冠军。',
      body: [
        '基米·安东内利赢了首届马德里大奖赛。积分是 292-211-191。下一站不是欧洲周日。是巴库的周六。',
        'Formula1.com：FP1 9 月 24 日周四，排位 25 日周五，正赛 26 日周六。51 圈 6.003 公里。天空体育：排位英国 13:00，正赛英国 12:00。练习尚未开始。',
        '不要印巴库杆位或周六冠军。9 月 26 日后再来。',
      ],
    },
    ja: {
      title: 'バクー、9月24-26日。土曜レース。アントネッリ292。結果なし。',
      subtitle: 'Formula1.comは木曜FP1を掲載。Sky：金曜予選、土曜正午UKで決勝。マドリードは帳簿入り。アゼルバイジャンは違う。',
      excerpt: 'アゼルバイジャンGPはバクー・シティ・サーキットの木曜から土曜。マドリード後：アントネッリ292、ラッセル211、ハミルトン191。優勝者を作らない。',
      body: [
        'キミ・アントネッリが初のマドリードGPを勝った。選手権は292-211-191。次戦は欧州の日曜ではない。バクーの土曜だ。',
        'Formula1.com：FP1は9月24日木曜、予選25日金曜、決勝26日土曜。6.003kmを51周。Sky Sports：予選UK13時、決勝UK12時。練習は始まっていない。',
        'バクーのポールも土曜の勝者も印刷しない。9月26日以降に戻る。',
      ],
    },
    ko: {
      title: '바쿠, 9월 24-26일. 토요일 레이스. 안토넬리 292. 결과 없음.',
      subtitle: 'Formula1.com이 목요일 FP1을 올린다. 스카이: 금요일 예선, 토요일 정오 영국 시간 본선. 마드리드는 장부에 있다. 아제르바이잔은 아니다.',
      excerpt: '아제르바이잔 그랑프리는 바쿠 시티 서킷의 목-토 주말이다. 마드리드 후 드라이버: 안토넬리 292, 러셀 211, 해밀턴 191. 우승자를 만들지 마라.',
      body: [
        '키미 안토넬리가 첫 마드리드 그랑프리를 이겼다. 챔피언십은 292-211-191. 다음 레이스는 유럽 일요일이 아니다. 바쿠의 토요일이다.',
        'Formula1.com: FP1 9월 24일 목요일, 예선 25일 금요일, 본선 26일 토요일. 6.003km 51랩. Sky Sports: 예선 영국 13:00, 본선 영국 12:00. 연습은 시작되지 않았다.',
        '바쿠 폴이나 토요일 우승자를 인쇄하지 마라. 9월 26일 이후에 돌아오라.',
      ],
    },
    ar: {
      title: 'باكو، 24-26 أيلول/سبتمبر. السباق السبت. أنطونيلي 292. لا نتيجة.',
      subtitle: 'Formula1.com يدرج التجارب الأولى الخميس. سكاي: التصفيات الجمعة، الجائزة الكبرى السبت ظهرًا بتوقيت بريطانيا. مدريد في الدفتر. أذربيجان ليست كذلك.',
      excerpt: 'جائزة أذربيجان الكبرى عطلة خميس-سبت على حلبة مدينة باكو. السائقون بعد مدريد: أنطونيلي 292، راسل 211، هاميلتون 191. لا تخترع فائزًا.',
      body: [
        'كيمي أنطونيلي فاز بأول جائزة مدريد الكبرى. البطولة 292-211-191. السباق التالي ليس أحدًا في أوروبا. إنه سبت في باكو.',
        'Formula1.com: التجارب الأولى الخميس 24 أيلول/سبتمبر، التصفيات الجمعة 25، الجائزة الكبرى السبت 26. 51 لفة بطول 6.003 كم. سكاي سبورتس: التصفيات 13:00 بريطانيا، السباق 12:00 بريطانيا. التدريبات لم تبدأ.',
        'لا تطبع قطب باكو ولا فائز السبت. عد بعد 26 أيلول/سبتمبر.',
      ],
    },
  },
  'liberty-lynx-93-81': {
    fr: {
      title: 'Liberty 93-81 Lynx : Stewart 24 et 10, le Minnesota reste n°1',
      subtitle: 'AP : New York a marqué 23-12 après 8:18 du quatrième. Les play-offs commencent le 27 septembre. Les matches de dimanche n’ont pas tippé.',
      excerpt: 'Les New York Liberty battent les Minnesota Lynx 93-81 le 18 septembre. AP : Breanna Stewart 24 points et 10 rebonds. Lynx 31-10. Play-offs le 27 septembre.',
      body: [
        'Si vous voulez du basket avec un tableau en septembre 2026, c’est la WNBA. Le Minnesota avait la tête de série n°1. New York est entré au Target Center le 18 septembre et a imprimé 93-81. Les play-offs commencent toujours le 27 septembre.',
        'AP : Breanna Stewart 24 points, 10 rebonds. Jonquel Jones 18 et 10. Sabrina Ionescu 17. Olivia Miles 20 pour le Minnesota. Miles un 3+1 pour 69-67 à 8:18. Stewart un 3 ensuite. New York 23-12 jusqu’à la fin. Lynx 31-10, toujours n°1.',
        'Tableau Wikipedia du 20 septembre : Lynx 31-10, Valkyries 31-11, Aces 28-13, Dream 28-14, Fever 27-14, Wings 26-16, Liberty 25-16, Mystics 25-16. ESPN : premier tour le 27 septembre. WNBA.com liste encore des matches de saison dimanche. N’inventez pas un champion 2026.',
      ],
    },
    es: {
      title: 'Liberty 93-81 Lynx: Stewart 24 y 10, Minnesota sigue n.º 1',
      subtitle: 'AP: Nueva York anotó 23-12 tras el 8:18 del cuarto. Los playoffs empiezan el 27 de septiembre. Los partidos del domingo no han tipado.',
      excerpt: 'Las New York Liberty ganan 93-81 a las Minnesota Lynx el 18 de septiembre. AP: Breanna Stewart 24 puntos y 10 rebotes. Lynx 31-10. Playoffs el 27 de septiembre.',
      body: [
        'Si quieres baloncesto con marcador en septiembre de 2026, es la WNBA. Minnesota tenía el n.º 1. Nueva York entró en el Target Center el 18 de septiembre e imprimió 93-81. Los playoffs siguen el 27 de septiembre.',
        'AP: Breanna Stewart 24 puntos, 10 rebotes. Jonquel Jones 18 y 10. Sabrina Ionescu 17. Olivia Miles 20 para Minnesota. Miles un 3+1 para 69-67 a falta de 8:18. Stewart un triple después. Nueva York 23-12 hasta el final. Lynx 31-10, siguen n.º 1.',
        'Tabla Wikipedia del 20 de septiembre: Lynx 31-10, Valkyries 31-11, Aces 28-13, Dream 28-14, Fever 27-14, Wings 26-16, Liberty 25-16, Mystics 25-16. ESPN: primera ronda el 27 de septiembre. WNBA.com aún lista partidos de temporada el domingo. No inventes un campeón 2026.',
      ],
    },
    de: {
      title: 'Liberty 93-81 Lynx: Stewart 24 und 10, Minnesota bleibt Nummer 1',
      subtitle: 'AP: New York erzielte 23-12 nach 8:18 im Viertel. Playoffs ab 27. September. Sonntagsspiele haben nicht getippt.',
      excerpt: 'Die New York Liberty schlagen die Minnesota Lynx 93-81 am 18. September. AP: Breanna Stewart 24 Punkte und 10 Rebounds. Lynx 31-10. Playoffs am 27. September.',
      body: [
        'Wer Basketball mit Anzeigetafel im September 2026 will, will die WNBA. Minnesota hatte die Nummer 1. New York ging am 18. September ins Target Center und druckte 93-81. Die Playoffs beginnen weiter am 27. September.',
        'AP: Breanna Stewart 24 Punkte, 10 Rebounds. Jonquel Jones 18 und 10. Sabrina Ionescu 17. Olivia Miles 20 für Minnesota. Miles ein And-One zum 69-67 bei 8:18. Stewart danach ein Dreier. New York 23-12 den Rest. Lynx 31-10, weiter Nummer 1.',
        'Wikipedia-Tableau 20. September: Lynx 31-10, Valkyries 31-11, Aces 28-13, Dream 28-14, Fever 27-14, Wings 26-16, Liberty 25-16, Mystics 25-16. ESPN: erste Runde 27. September. WNBA.com listet noch Saisonspiele am Sonntag. Keinen Champion 2026 erfinden.',
      ],
    },
    it: {
      title: 'Liberty 93-81 Lynx: Stewart 24 e 10, il Minnesota resta n. 1',
      subtitle: 'AP: New York ha segnato 23-12 dopo 8:18 del quarto. I playoff iniziano il 27 settembre. Le partite di domenica non sono partite.',
      excerpt: 'Le New York Liberty battono le Minnesota Lynx 93-81 il 18 settembre. AP: Breanna Stewart 24 punti e 10 rimbalzi. Lynx 31-10. Playoff il 27 settembre.',
      body: [
        'Se vuoi basket con un tabellone a settembre 2026, è la WNBA. Il Minnesota aveva la testa di serie n. 1. New York è entrata al Target Center il 18 settembre e ha stampato 93-81. I playoff iniziano ancora il 27 settembre.',
        'AP: Breanna Stewart 24 punti, 10 rimbalzi. Jonquel Jones 18 e 10. Sabrina Ionescu 17. Olivia Miles 20 per il Minnesota. Miles un 3+1 per 69-67 a 8:18. Stewart un triple dopo. New York 23-12 fino alla fine. Lynx 31-10, ancora n. 1.',
        'Tabella Wikipedia del 20 settembre: Lynx 31-10, Valkyries 31-11, Aces 28-13, Dream 28-14, Fever 27-14, Wings 26-16, Liberty 25-16, Mystics 25-16. ESPN: primo turno il 27 settembre. WNBA.com elenca ancora partite di regular season domenica. Non inventare un campione 2026.',
      ],
    },
    pl: {
      title: 'Liberty 93-81 Lynx: Stewart 24 i 10, Minnesota nadal numer 1',
      subtitle: 'AP: Nowy Jork zdobył 23-12 po 8:18 czwartej. Play-offy 27 września. Niedzielne mecze nie wystartowały.',
      excerpt: 'New York Liberty wygrywają 93-81 z Minnesota Lynx 18 września. AP: Breanna Stewart 24 punkty i 10 zbiórek. Lynx 31-10. Play-offy 27 września.',
      body: [
        'Jeśli chcesz koszykówkę z tablicą we wrześniu 2026, chcesz WNBA. Minnesota miała numer 1. Nowy Jork wszedł do Target Center 18 września i wydrukował 93-81. Play-offy nadal 27 września.',
        'AP: Breanna Stewart 24 punkty, 10 zbiórek. Jonquel Jones 18 i 10. Sabrina Ionescu 17. Olivia Miles 20 dla Minnesoty. Miles 3+1 na 69-67 przy 8:18. Stewart trójka potem. Nowy Jork 23-12 do końca. Lynx 31-10, nadal numer 1.',
        'Tabela Wikipedia 20 września: Lynx 31-10, Valkyries 31-11, Aces 28-13, Dream 28-14, Fever 27-14, Wings 26-16, Liberty 25-16, Mystics 25-16. ESPN: pierwsza runda 27 września. WNBA.com nadal wymienia mecze sezonu w niedzielę. Nie wymyślaj mistrza 2026.',
      ],
    },
    zh: {
      title: '自由人 93-81 山猫：斯图尔特 24+10，明尼苏达仍是一号种子',
      subtitle: '美联社：纽约在第四节 8:18 后打出 23-12。季后赛 9 月 27 日开始。周日比赛尚未开始。',
      excerpt: '纽约自由人 9 月 18 日 93-81 击败明尼苏达山猫。美联社：布丽安娜·斯图尔特 24 分 10 篮板。山猫 31-10。季后赛 9 月 27 日。',
      body: [
        '若你要 2026 年 9 月仍有记分板的篮球，那是 WNBA。明尼苏达握有一号种子。纽约 9 月 18 日走进标靶中心，印出 93-81。季后赛仍是 9 月 27 日开始。',
        '美联社：斯图尔特 24 分 10 篮板。琼奎尔·琼斯 18+10。萨布丽娜·伊奥内斯库 17。奥利维亚·迈尔斯为明尼苏达得 20。迈尔斯在 8:18 打成 69-67 的 2+1。斯图尔特随即三分。纽约此后 23-12。山猫 31-10，仍是一号种子。',
        '维基百科 9 月 20 日资格表：山猫 31-10，女武神 31-11，王牌 28-13，梦想 28-14，狂热 27-14，飞翼 26-16，自由人 25-16，神秘人 25-16。ESPN：首轮 9 月 27 日。WNBA.com 仍列出周日常规赛。不要编造 2026 冠军。',
      ],
    },
    ja: {
      title: 'リバティ 93-81 リンクス：スチュワート24と10、ミネソタはなお1シード',
      subtitle: 'AP：ニューヨークは第4Q 8:18以降に23-12。プレーオフは9月27日開始。日曜試合は未チップオフ。',
      excerpt: 'ニューヨーク・リバティが9月18日にミネソタ・リンクスを93-81。AP：ブリアナ・スチュワート24点10リバウンド。リンクス 31-10。プレーオフは9月27日。',
      body: [
        '2026年9月にスコアボードのあるバスケが欲しければWNBAだ。ミネソタは1シードだった。ニューヨークは9月18日にターゲット・センターへ入り、93-81を印刷した。プレーオフはなお9月27日開始。',
        'AP：スチュワート24点10リバウンド。ジョンケル・ジョーンズ18と10。サブリナ・イオネスク17。オリビア・マイルズがミネソタで20。マイルズが8:18に69-67の3点プレー。スチュワートが直後に3。ニューヨークはその後23-12。リンクス 31-10、なお1シード。',
        'ウィキペディア9月20日の出場表：リンクス31-10、ヴァルキリーズ31-11、エーシズ28-13、ドリーム28-14、フィーバー27-14、ウィングズ26-16、リバティ25-16、ミスティクス25-16。ESPN：1回戦は9月27日。WNBA.comは日曜のレギュラーシーズンをまだ掲載。2026年の王者を作らない。',
      ],
    },
    ko: {
      title: '리버티 93-81 링스: 스튜어트 24와 10, 미네소타는 여전히 1시드',
      subtitle: 'AP: 뉴욕이 4쿼터 8:18 이후 23-12. 플레이오프는 9월 27일 시작. 일요일 경기는 아직 팁오프 전.',
      excerpt: '뉴욕 리버티가 9월 18일 미네소타 링스를 93-81로 이겼다. AP: 브리애나 스튜어트 24점 10리바운드. 링스 31-10. 플레이오프 9월 27일.',
      body: [
        '2026년 9월에 스코어보드가 있는 농구를 원하면 WNBA다. 미네소타가 1시드였다. 뉴욕은 9월 18일 타깃 센터로 들어가 93-81을 인쇄했다. 플레이오프는 여전히 9월 27일 시작.',
        'AP: 스튜어트 24점 10리바운드. 존켈 존스 18과 10. 사브리나 이오네스쿠 17. 올리비아 마일이 미네소타에서 20. 마일이 8:18에 69-67 3점 플레이. 스튜어트가 바로 3점. 뉴욕은 이후 23-12. 링스 31-10, 여전히 1시드.',
        '위키피디아 9월 20일 출전표: 링스 31-10, 발키리스 31-11, 에이시스 28-13, 드림 28-14, 피버 27-14, 윙스 26-16, 리버티 25-16, 미스틱스 25-16. ESPN: 1라운드 9월 27일. WNBA.com은 일요일 정규시즌을 아직 올린다. 2026 챔피언을 만들지 마라.',
      ],
    },
    ar: {
      title: 'ليبرتي 93-81 لينكس: ستيوارت 24 و10، مينيسوتا ما زالت الأولى',
      subtitle: 'AP: نيويورك سجلت 23-12 بعد 8:18 من الرابعة. التصفيات تبدأ 27 أيلول/سبتمبر. مباريات الأحد لم تبدأ.',
      excerpt: 'نيويورك ليبرتي تهزم مينيسوتا لينكس 93-81 في 18 أيلول/سبتمبر. AP: بريانا ستيوارت 24 نقطة و10 متابعات. لينكس 31-10. التصفيات 27 أيلول/سبتمبر.',
      body: [
        'إن أردت كرة سلة بلوحة في أيلول/سبتمبر 2026 فأنت تريد WNBA. كانت مينيسوتا الأولى. دخلت نيويورك تارغت سنتر في 18 أيلول/سبتمبر وطبعت 93-81. التصفيات ما زالت 27 أيلول/سبتمبر.',
        'AP: بريانا ستيوارت 24 نقطة و10 متابعات. جونكيل جونز 18 و10. سابرينا إيونيسكو 17. أوليفيا مايلز 20 لمينيسوتا. مايلز لعبة ثلاثية لـ69-67 عند 8:18. ستيوارت ثلاثية بعدها. نيويورك 23-12 حتى النهاية. لينكس 31-10، ما زالوا الأول.',
        'جدول ويكيبيديا في 20 أيلول/سبتمبر: لينكس 31-10، فالكيريز 31-11، إيسيس 28-13، دريم 28-14، فيفر 27-14، وينغز 26-16، ليبرتي 25-16، ميستيكس 25-16. ESPN: الدور الأول 27 أيلول/سبتمبر. WNBA.com ما زال يدرج مباريات موسم الأحد. لا تخترع بطل 2026.',
      ],
    },
  },
  'city-sunderland-5-3': {
    fr: {
      title: 'City 5-3 Sunderland : cinq sur cinq, triplette de Brobbey dans une défaite',
      subtitle: 'Fernandez, Cherki, Semenyo deux fois, Haaland. ESPN : City 15 points. La 5e journée est close.',
      excerpt: 'Manchester City bat Sunderland 5-3 à l’Etihad le 20 septembre. ESPN, AFP et IOL impriment le même score. City 5-0-0, 15 points. Arsenal 12. Brighton 10.',
      body: [
        'Arsenal a perdu 3-0 à Brighton samedi. City avait encore un match en retard. Dimanche à l’Etihad s’est fini 5-3. City est cinq sur cinq. La 5e journée est close.',
        'ESPN UK et AFP : Enzo Fernandez 9e, Rayan Cherki 29e, Antoine Semenyo 43e et 57e, Erling Haaland 81e. Brian Brobbey 12e, 33e, 59e, triplette dans une défaite. IOL : le but de Haaland signalé hors-jeu puis validé par la VAR.',
        'Reste du dimanche, ESPN UK et AFP : Bournemouth 0-1 Liverpool (Isak 57e). Leeds 0-0 Palace. Fulham 1-1 United (CSC Martinez 63e, Cunha 89e). Tableau ESPN UK : City 15, Arsenal 12, Brighton 10, Liverpool 9, sixième.',
      ],
    },
    es: {
      title: 'City 5-3 Sunderland: cinco de cinco, tripleta de Brobbey en derrota',
      subtitle: 'Fernandez, Cherki, Semenyo dos veces, Haaland. ESPN: City 15 puntos. La jornada 5 está cerrada.',
      excerpt: 'Manchester City gana 5-3 a Sunderland en el Etihad el 20 de septiembre. ESPN, AFP e IOL imprimen el mismo marcador. City 5-0-0, 15 puntos. Arsenal 12. Brighton 10.',
      body: [
        'Arsenal perdió 3-0 en Brighton el sábado. City aún tenía un partido menos. El domingo en el Etihad acabó 5-3. City es cinco de cinco. La jornada 5 está cerrada.',
        'ESPN UK y AFP: Enzo Fernandez 9, Rayan Cherki 29, Antoine Semenyo 43 y 57, Erling Haaland 81. Brian Brobbey 12, 33, 59, tripleta en derrota. IOL: el gol de Haaland anulado por fuera de juego y dado por el VAR.',
        'Resto del domingo, ESPN UK y AFP: Bournemouth 0-1 Liverpool (Isak 57). Leeds 0-0 Palace. Fulham 1-1 United (p.p. Martinez 63, Cunha 89). Tabla ESPN UK: City 15, Arsenal 12, Brighton 10, Liverpool 9, sexto.',
      ],
    },
    de: {
      title: 'City 5:3 Sunderland: fünf aus fünf, Brobbey-Hattrick in einer Niederlage',
      subtitle: 'Fernandez, Cherki, Semenyo zweimal, Haaland. ESPN: City 15 Punkte. Spieltag 5 ist zu Ende.',
      excerpt: 'Manchester City schlägt Sunderland 5:3 an der Etihad am 20. September. ESPN, AFP und IOL drucken denselben Stand. City 5-0-0, 15 Punkte. Arsenal 12. Brighton 10.',
      body: [
        'Arsenal verlor samstags 3:0 in Brighton. City hatte noch ein Nachholspiel. Sonntag an der Etihad endete 5:3. City ist fünf aus fünf. Spieltag 5 ist zu Ende.',
        'ESPN UK und AFP: Enzo Fernandez 9., Rayan Cherki 29., Antoine Semenyo 43. und 57., Erling Haaland 81. Brian Brobbey 12., 33., 59., Hattrick in einer Niederlage. IOL: Haalands Tor wegen Abseits angezeigt, dann vom VAR gegeben.',
        'Restlicher Sonntag, ESPN UK und AFP: Bournemouth 0:1 Liverpool (Isak 57.). Leeds 0:0 Palace. Fulham 1:1 United (Eigentor Martinez 63., Cunha 89.). ESPN-UK-Tabelle: City 15, Arsenal 12, Brighton 10, Liverpool 9, Sechster.',
      ],
    },
    it: {
      title: 'City 5-3 Sunderland: cinque su cinque, tripletta di Brobbey in una sconfitta',
      subtitle: 'Fernandez, Cherki, Semenyo due volte, Haaland. ESPN: City 15 punti. La 5ª giornata è chiusa.',
      excerpt: 'Il Manchester City batte il Sunderland 5-3 all’Etihad il 20 settembre. ESPN, AFP e IOL stampano lo stesso punteggio. City 5-0-0, 15 punti. Arsenal 12. Brighton 10.',
      body: [
        'L’Arsenal ha perso 3-0 a Brighton sabato. City aveva ancora una partita da recuperare. Domenica all’Etihad è finita 5-3. City è cinque su cinque. La 5ª giornata è chiusa.',
        'ESPN UK e AFP: Enzo Fernandez 9’, Rayan Cherki 29’, Antoine Semenyo 43’ e 57’, Erling Haaland 81’. Brian Brobbey 12’, 33’, 59’, tripletta in una sconfitta. IOL: gol di Haaland segnalato in fuorigioco poi convalidato dal VAR.',
        'Resto della domenica, ESPN UK e AFP: Bournemouth 0-1 Liverpool (Isak 57’). Leeds 0-0 Palace. Fulham 1-1 United (autogol Martinez 63’, Cunha 89’). Classifica ESPN UK: City 15, Arsenal 12, Brighton 10, Liverpool 9, sesto.',
      ],
    },
    pl: {
      title: 'City 5-3 Sunderland: pięć z pięciu, hat-trick Brobbeya w porażce',
      subtitle: 'Fernandez, Cherki, Semenyo dwa razy, Haaland. ESPN: City 15 punktów. 5. kolejka zamknięta.',
      excerpt: 'Manchester City wygrywa 5-3 z Sunderlandem na Etihad 20 września. ESPN, AFP i IOL drukują ten sam wynik. City 5-0-0, 15 punktów. Arsenal 12. Brighton 10.',
      body: [
        'Arsenal przegrał 3-0 w Brighton w sobotę. City miało jeszcze mecz w ręku. Niedziela na Etihad skończyła się 5-3. City jest pięć z pięciu. 5. kolejka jest zamknięta.',
        'ESPN UK i AFP: Enzo Fernandez 9, Rayan Cherki 29, Antoine Semenyo 43 i 57, Erling Haaland 81. Brian Brobbey 12, 33, 59, hat-trick w porażce. IOL: gol Haalanda na spalonym, potem dany przez VAR.',
        'Reszta niedzieli, ESPN UK i AFP: Bournemouth 0-1 Liverpool (Isak 57). Leeds 0-0 Palace. Fulham 1-1 United (samobój Martinez 63, Cunha 89). Tabela ESPN UK: City 15, Arsenal 12, Brighton 10, Liverpool 9, szósty.',
      ],
    },
    zh: {
      title: '曼城 5-3 桑德兰：五战全胜，布罗贝帽子戏法仍输',
      subtitle: '费尔南德斯、切尔基、塞门约两球、哈兰德。ESPN：曼城 15 分。第 5 轮结束。',
      excerpt: '9 月 20 日曼城在伊蒂哈德 5-3 击败桑德兰。ESPN、法新社与 IOL 印同一比分。曼城 5 胜，15 分。阿森纳 12。布莱顿 10。',
      body: [
        '阿森纳周六在布莱顿 0-3 落败。曼城仍有一轮少赛。周日伊蒂哈德结束于 5-3。曼城五战全胜。第 5 轮结束。',
        'ESPN UK 与法新社：恩佐·费尔南德斯 9 分钟，拉扬·切尔基 29 分钟，安托万·塞门约 43 与 57 分钟，埃尔林·哈兰德 81 分钟。布赖恩·布罗贝 12、33、59 分钟，帽子戏法仍输。IOL：哈兰德进球先判越位，VAR 改判有效。',
        '周日其余，ESPN UK 与法新社：伯恩茅斯 0-1 利物浦（伊萨克 57）。利兹 0-0 水晶宫。富勒姆 1-1 曼联（马丁内斯乌龙 63，库尼亚 89）。ESPN UK 积分榜：曼城 15，阿森纳 12，布莱顿 10，利物浦 9 分第六。',
      ],
    },
    ja: {
      title: 'シティ 5-3 サンダーランド：5戦全勝、ブロベイのハットトリックも敗戦',
      subtitle: 'フェルナンデス、チェルキ、セメニョ2、ハーランド。ESPN：シティ15点。第5節は終了。',
      excerpt: '9月20日、マンチェスター・シティがエティハドでサンダーランドに5-3。ESPN、AFP、IOLが同じスコア。シティ5勝15点。アーセナル12。ブライトン10。',
      body: [
        'アーセナルは土曜にブライトンで3-0負け。シティはまだ試合消化が少なかった。日曜のエティハドは5-3で終わった。シティは5戦全勝。第5節は終了。',
        'ESPN UKとAFP：エンソ・フェルナンデス9分、ラヤン・チェルキ29分、アントワーヌ・セメニョ43分と57分、アーリング・ハーランド81分。ブライアン・ブロベイ12、33、59分、ハットトリックも敗戦。IOL：ハーランドのゴールはオフサイド判定後にVARで認められた。',
        '日曜の残り、ESPN UKとAFP：ボーンマス 0-1 リヴァプール（イサク57分）。リーズ 0-0 パレス。フラム 1-1 ユナイテッド（マルティネスOG63分、クーニャ89分）。ESPN UK順位表：シティ15、アーセナル12、ブライトン10、リヴァプール9で6位。',
      ],
    },
    ko: {
      title: '시티 5-3 선덜랜드: 5전 전승, 브로베이 해트트릭에도 패배',
      subtitle: '페르난데스, 셰르키, 세메뇨 두 골, 홀란. ESPN: 시티 15점. 5라운드 종료.',
      excerpt: '9월 20일 맨체스터 시티가 에티하드에서 선덜랜드를 5-3으로 이겼다. ESPN, AFP, IOL이 같은 점수. 시티 5승 15점. 아스널 12. 브라이턴 10.',
      body: [
        '아스널은 토요일 브라이턴에서 3-0으로 졌다. 시티는 아직 한 경기를 덜 했다. 일요일 에티하드는 5-3으로 끝났다. 시티는 5전 전승. 5라운드는 종료.',
        'ESPN UK와 AFP: 엔소 페르난데스 9분, 라얀 셰르키 29분, 앙투안 세메뇨 43분과 57분, 엘링 홀란 81분. 브라이언 브로베이 12, 33, 59분, 해트트릭에도 패배. IOL: 홀란 골이 오프사이드 선언 뒤 VAR로 인정.',
        '일요일 나머지, ESPN UK와 AFP: 본머스 0-1 리버풀(이삭 57). 리즈 0-0 팰리스. 풀럼 1-1 유나이티드(마르티네스 자책 63, 쿠냐 89). ESPN UK 순위: 시티 15, 아스널 12, 브라이턴 10, 리버풀 9점 6위.',
      ],
    },
    ar: {
      title: 'سيتي 5-3 سندرلاند: خمس من خمس، هاتريك بروبي في خسارة',
      subtitle: 'فرنانديز، تشيركي، سيمينيو مرتين، هالاند. ESPN: سيتي 15 نقطة. الجولة 5 أغلقت.',
      excerpt: 'مانشستر سيتي يهزم سندرلاند 5-3 في الإتيهاد في 20 أيلول/سبتمبر. ESPN وAFP وIOL تطبع نفس النتيجة. سيتي 5-0-0، 15 نقطة. أرسنال 12. برايتون 10.',
      body: [
        'خسر أرسنال 3-0 في برايتون السبت. كان لسيتي مباراة أقل. الأحد في الإتيهاد انتهى 5-3. سيتي خمس من خمس. الجولة 5 أغلقت.',
        'ESPN UK وAFP: إنزو فرنانديز 9، رايان تشيركي 29، أنطوان سيمينيو 43 و57، إرلينغ هالاند 81. برايان بروبي 12 و33 و59، هاتريك في خسارة. IOL: هدف هالاند احتُسب تسللاً ثم أثبته VAR.',
        'بقية الأحد، ESPN UK وAFP: بورنموث 0-1 ليفربول (إيساك 57). ليدز 0-0 بالاس. فولهام 1-1 يونايتد (هدف عكسي مارتينيز 63، كونيا 89). جدول ESPN UK: سيتي 15، أرسنال 12، برايتون 10، ليفربول 9، السادس.',
      ],
    },
  },
  'spaun-bmw-pga-2026': {
    fr: {
      title: 'JJ Spaun gagne le BMW PGA. 17 sous. Elvira double-bogey au 18.',
      subtitle: 'AP : 70-66-68-67, 271. Elvira, McIlroy, Rai et Scott partagent 273. Le tournoi phare a un vainqueur.',
      excerpt: 'JJ Spaun a gagné le BMW PGA Championship à Wentworth le 20 septembre. AP et le DP World Tour impriment 271, 17 sous. Heart : Elvira a fait un double-bogey au 18.',
      body: [
        'Le BMW PGA est le phare du DP World Tour. Après 54 trous il avait deux noms à 13 sous et pas de vainqueur. Dimanche a imprimé un vainqueur. AP : JJ Spaun, 17 sous.',
        'AP via WTOP : Spaun 70-66-68-67, 271. Elvira, McIlroy, Rai et Scott 273. Celli 274. Gerard, leader à 36 trous, 278. Heart : Spaun un 67 final, six birdies. Elvira avait besoin d’un birdie au 18, double-bogey.',
        'Pas de play-off. Pas de 62. La Presidents Cup reste les 24-27 septembre à Medinah. Heart : la suite DP World Tour est l’Open de France FedEx au Golf National.',
      ],
    },
    es: {
      title: 'JJ Spaun gana el BMW PGA. 17 bajo. Elvira hace doble bogey en el 18.',
      subtitle: 'AP: 70-66-68-67, 271. Elvira, McIlroy, Rai y Scott comparten 273. El torneo insignia tiene ganador.',
      excerpt: 'JJ Spaun ganó el BMW PGA Championship en Wentworth el 20 de septiembre. AP y el DP World Tour imprimen 271, 17 bajo. Heart: Elvira hizo doble bogey en el 18.',
      body: [
        'El BMW PGA es la prueba insignia del DP World Tour. Tras 54 hoyos había dos nombres a 13 bajo y ningún ganador. El domingo imprimió un ganador. AP: JJ Spaun, 17 bajo.',
        'AP vía WTOP: Spaun 70-66-68-67, 271. Elvira, McIlroy, Rai y Scott 273. Celli 274. Gerard, líder a 36, 278. Heart: Spaun un 67 final, seis birdies. Elvira necesitaba birdie en el 18 y hizo doble bogey.',
        'No hay playoff. No hay 62. La Presidents Cup sigue el 24-27 de septiembre en Medinah. Heart: el siguiente DP World Tour es el Open de Francia FedEx en Le Golf National.',
      ],
    },
    de: {
      title: 'JJ Spaun gewinnt die BMW PGA. 17 unter. Elvira Doppelbogey auf 18.',
      subtitle: 'AP: 70-66-68-67, 271. Elvira, McIlroy, Rai und Scott teilen 273. Das Flaggschiff hat einen Sieger.',
      excerpt: 'JJ Spaun gewann die BMW PGA Championship in Wentworth am 20. September. AP und die DP World Tour drucken 271, 17 unter. Heart: Elvira machte ein Doppelbogey auf 18.',
      body: [
        'Die BMW PGA ist das Flaggschiff der DP World Tour. Nach 54 Löchern gab es zwei Namen bei 13 unter und keinen Sieger. Sonntag druckte einen Sieger. AP: JJ Spaun, 17 unter.',
        'AP via WTOP: Spaun 70-66-68-67, 271. Elvira, McIlroy, Rai und Scott 273. Celli 274. Gerard, 36-Loch-Leader, 278. Heart: Spaun eine 67 am Finaltag, sechs Birdies. Elvira brauchte ein Birdie auf 18, Doppelbogey.',
        'Kein Playoff. Keine 62. Der Presidents Cup bleibt 24.-27. September in Medinah. Heart: nächstes DP-World-Tour-Event ist die FedEx Open de France in Le Golf National.',
      ],
    },
    it: {
      title: 'JJ Spaun vince il BMW PGA. 17 sotto. Elvira doppio bogey al 18.',
      subtitle: 'AP: 70-66-68-67, 271. Elvira, McIlroy, Rai e Scott condividono 273. Il torneo di punta ha un vincitore.',
      excerpt: 'JJ Spaun ha vinto il BMW PGA Championship a Wentworth il 20 settembre. AP e il DP World Tour stampano 271, 17 sotto. Heart: Elvira ha fatto doppio bogey al 18.',
      body: [
        'Il BMW PGA è il torneo di punta del DP World Tour. Dopo 54 buche c’erano due nomi a 13 sotto e nessun vincitore. La domenica ha stampato un vincitore. AP: JJ Spaun, 17 sotto.',
        'AP via WTOP: Spaun 70-66-68-67, 271. Elvira, McIlroy, Rai e Scott 273. Celli 274. Gerard, leader a 36, 278. Heart: Spaun un 67 finale, sei birdie. Elvira serviva un birdie al 18, doppio bogey.',
        'Niente playoff. Niente 62. La Presidents Cup resta il 24-27 settembre a Medinah. Heart: il prossimo DP World Tour è l’Open de France FedEx al Golf National.',
      ],
    },
    pl: {
      title: 'JJ Spaun wygrywa BMW PGA. 17 poniżej. Elvira podwójny bogey na 18.',
      subtitle: 'AP: 70-66-68-67, 271. Elvira, McIlroy, Rai i Scott dzielą 273. Flagowy turniej ma zwycięzcę.',
      excerpt: 'JJ Spaun wygrał BMW PGA Championship w Wentworth 20 września. AP i DP World Tour drukują 271, 17 poniżej. Heart: Elvira zrobił podwójnego bogeya na 18.',
      body: [
        'BMW PGA to flagowy turniej DP World Tour. Po 54 dołkach były dwa nazwiska przy 13 poniżej i brak zwycięzcy. Niedziela wydrukowała zwycięzcę. AP: JJ Spaun, 17 poniżej.',
        'AP via WTOP: Spaun 70-66-68-67, 271. Elvira, McIlroy, Rai i Scott 273. Celli 274. Gerard, lider po 36, 278. Heart: Spaun 67 w finale, sześć birdie. Elvira potrzebował birdie na 18, podwójny bogey.',
        'Bez play-offu. Bez 62. Presidents Cup nadal 24-27 września w Medinah. Heart: następny DP World Tour to FedEx Open de France w Le Golf National.',
      ],
    },
    zh: {
      title: '斯庞赢下宝马 PGA。低于标准杆 17 杆。埃尔维拉 18 号洞双柏忌。',
      subtitle: '美联社：70-66-68-67，271。埃尔维拉、麦克罗伊、拉伊、斯科特并列 273。旗舰赛有了冠军。',
      excerpt: '9 月 20 日 JJ·斯庞在温特沃斯赢下宝马 PGA。美联社与欧巡印 271，低于标准杆 17 杆。Heart：埃尔维拉在 18 号洞打出双柏忌。',
      body: [
        '宝马 PGA 是欧巡旗舰赛。54 洞后两人低于标准杆 13 杆、没有冠军。周日印出了冠军。美联社：JJ·斯庞，低于标准杆 17 杆。',
        '美联社经 WTOP：斯庞 70-66-68-67，271。埃尔维拉、麦克罗伊、拉伊、斯科特 273。切利 274。36 洞领先的杰拉德 278。Heart：斯庞决赛轮 67，六个小鸟。埃尔维拉 18 号洞需要小鸟，打出双柏忌。',
        '没有附加赛。没有 62。总统杯仍是 9 月 24-27 日在梅迪纳。Heart：下一站欧巡是法国高尔夫国家球场的 FedEx 法国公开赛。',
      ],
    },
    ja: {
      title: 'JJ・スパンがBMW PGAを勝つ。17アンダー。エルビラは18番でダブルボギー。',
      subtitle: 'AP：70-66-68-67、271。エルビラ、マキロイ、ライ、スコットが273を分け合う。旗艦戦に優勝者がついた。',
      excerpt: '9月20日、JJ・スパンがウェントワースでBMW PGAを勝った。APとDPワールドツアーは271、17アンダー。Heart：エルビラは18番でダブルボギー。',
      body: [
        'BMW PGAはDPワールドツアーの旗艦。54ホール後は13アンダーが二人で優勝者なし。日曜が優勝者を印刷した。AP：JJ・スパン、17アンダー。',
        'AP（WTOP経由）：スパン 70-66-68-67、271。エルビラ、マキロイ、ライ、スコット273。チェッリ274。36ホール首位のジェラルド278。Heart：スパン最終67、バーディー6。エルビラは18番でバーディーが必要でダブルボギー。',
        'プレーオフなし。62なし。プレジデンツカップはなお9月24-27日、メディナ。Heart：次のDPワールドツアーはル・ゴルフ・ナショナルのフェデックス・オープン・ド・フランス。',
      ],
    },
    ko: {
      title: 'JJ 스폰이 BMW PGA를 이기다. 17언더. 엘비라는 18번 더블 보기.',
      subtitle: 'AP: 70-66-68-67, 271. 엘비라, 맥일로이, 라이, 스콧이 273을 나눈다. 플래그십에 우승자가 있다.',
      excerpt: '9월 20일 JJ 스폰이 웬트워스에서 BMW PGA를 이겼다. AP와 DP 월드 투어는 271, 17언더. Heart: 엘비라가 18번에서 더블 보기.',
      body: [
        'BMW PGA는 DP 월드 투어 플래그십이다. 54홀 후 13언더가 두 명이고 우승자가 없었다. 일요일이 우승자를 인쇄했다. AP: JJ 스폰, 17언더.',
        'AP(WTOP): 스폰 70-66-68-67, 271. 엘비라, 맥일로이, 라이, 스콧 273. 첼리 274. 36홀 선두 제라드 278. Heart: 스폰 최종 67, 버디 6. 엘비라는 18번 버디가 필요했고 더블 보기.',
        '플레이오프 없음. 62 없음. 프레지던츠컵은 여전히 9월 24-27일 메디나. Heart: 다음 DP 월드 투어는 르 골프 나시오날의 FedEx 프랑스 오픈.',
      ],
    },
    ar: {
      title: 'جي جي سبون يفوز بـ BMW PGA. 17 تحت البار. إلفيرا دبل بوجي في 18.',
      subtitle: 'AP: 70-66-68-67، 271. إلفيرا وماكيلروي وراي وسكوت يقتسمون 273. البطولة الأبرز لها فائز.',
      excerpt: 'جي جي سبون فاز ببطولة BMW PGA في وينتوورث في 20 أيلول/سبتمبر. AP وDP World Tour تطبعان 271، 17 تحت. Heart: إلفيرا سجّل دبل بوجي في 18.',
      body: [
        'BMW PGA علم DP World Tour. بعد 54 حفرة كان هناك اسمان عند 13 تحت ولا فائز. الأحد طبع فائزاً. AP: جي جي سبون، 17 تحت.',
        'AP عبر WTOP: سبون 70-66-68-67، 271. إلفيرا وماكيلروي وراي وسكوت 273. تشيللي 274. جيرارد قائد 36 حفرة 278. Heart: سبون 67 ختامي وستة بيردي. إلفيرا احتاج بيردي في 18 فصنع دبل بوجي.',
        'لا ملحق. لا 62. كأس الرؤساء ما زال 24-27 أيلول/سبتمبر في ميدينا. Heart: التالي في DP World Tour هو أوبن فرنسا FedEx في لو غولف ناسيونال.',
      ],
    },
  },
  'davis-cup-final-8-2026': {
    fr: {
      title: 'Allemagne 3-1 Croatie. Grande-Bretagne 4-0 Équateur. Le Final 8 de Coupe Davis est fixé.',
      subtitle: 'AP : Zverev 6-2, 6-4 en 77 minutes. Bologne, 24-29 novembre. La Laver Cup reste la semaine prochaine.',
      excerpt: 'Alexander Zverev a envoyé l’Allemagne en Final 8 de Coupe Davis le 20 septembre. AP : 6-2, 6-4 contre Dino Prizmic. TNT Sports : Grande-Bretagne 4-0 Équateur. Wikipédia nomme les huit.',
      body: [
        'L’US Open a déjà des noms. La Laver Cup reste les 25-27 septembre à The O2. Dimanche a nommé les derniers billets du Final 8 pour Bologne en novembre.',
        'AP : Zverev bat Prizmic 6-2, 6-4 en 77 minutes à Halle. Krawietz et Puetz avaient battu Mektic et Pavic 7-5, 6-2. Allemagne 3-1. AP : Patten et Skupski 6-3, 6-4. TNT Sports et Wikipédia : Grande-Bretagne 4-0 Équateur. Wikipédia : Espagne 3-0 Chili.',
        'Wikipédia Final 8, Bologne, 24-29 novembre : Italie, Canada, Tchéquie, Autriche, Corée du Sud, Allemagne, Grande-Bretagne, Espagne. N’imprimez pas un champion 2026. N’imprimez pas un vainqueur de Laver Cup. Ces matches n’ont pas été joués.',
      ],
    },
    es: {
      title: 'Alemania 3-1 Croacia. Gran Bretaña 4-0 Ecuador. El Final 8 de Copa Davis está fijado.',
      subtitle: 'AP: Zverev 6-2, 6-4 en 77 minutos. Bolonia, 24-29 de noviembre. La Laver Cup sigue la semana que viene.',
      excerpt: 'Alexander Zverev metió a Alemania en el Final 8 de Copa Davis el 20 de septiembre. AP: 6-2, 6-4 a Dino Prizmic. TNT Sports: Gran Bretaña 4-0 Ecuador. Wikipedia nombra a los ocho.',
      body: [
        'El US Open ya tiene nombres. La Laver Cup sigue el 25-27 de septiembre en The O2. El domingo nombró los últimos boletos del Final 8 para Bolonia en noviembre.',
        'AP: Zverev gana a Prizmic 6-2, 6-4 en 77 minutos en Halle. Krawietz y Puetz habían ganado a Mektic y Pavic 7-5, 6-2. Alemania 3-1. AP: Patten y Skupski 6-3, 6-4. TNT Sports y Wikipedia: Gran Bretaña 4-0 Ecuador. Wikipedia: España 3-0 Chile.',
        'Wikipedia Final 8, Bolonia, 24-29 de noviembre: Italia, Canadá, Chequia, Austria, Corea del Sur, Alemania, Gran Bretaña, España. No imprimas un campeón 2026. No imprimas un ganador de Laver Cup. Esos partidos no se han jugado.',
      ],
    },
    de: {
      title: 'Deutschland 3:1 Kroatien. Großbritannien 4:0 Ecuador. Das Davis-Cup-Final 8 steht.',
      subtitle: 'AP: Zverev 6:2, 6:4 in 77 Minuten. Bologna, 24.-29. November. Der Laver Cup bleibt nächste Woche.',
      excerpt: 'Alexander Zverev schickte Deutschland am 20. September ins Davis-Cup-Final 8. AP: 6:2, 6:4 gegen Dino Prizmic. TNT Sports: Großbritannien 4:0 Ecuador. Wikipedia nennt die Acht.',
      body: [
        'Die US Open haben schon Namen. Der Laver Cup bleibt 25.-27. September in der O2. Sonntag nannte die letzten Final-8-Tickets für Bologna im November.',
        'AP: Zverev schlägt Prizmic 6:2, 6:4 in 77 Minuten in Halle. Krawietz und Puetz hatten Mektic und Pavic 7:5, 6:2 geschlagen. Deutschland 3:1. AP: Patten und Skupski 6:3, 6:4. TNT Sports und Wikipedia: Großbritannien 4:0 Ecuador. Wikipedia: Spanien 3:0 Chile.',
        'Wikipedia Final 8, Bologna, 24.-29. November: Italien, Kanada, Tschechien, Österreich, Südkorea, Deutschland, Großbritannien, Spanien. Keinen Champion 2026 drucken. Keinen Laver-Cup-Sieger drucken. Diese Matches sind nicht gespielt.',
      ],
    },
    it: {
      title: 'Germania 3-1 Croazia. Gran Bretagna 4-0 Ecuador. Il Final 8 di Coppa Davis è fissato.',
      subtitle: 'AP: Zverev 6-2, 6-4 in 77 minuti. Bologna, 24-29 novembre. La Laver Cup resta la settimana prossima.',
      excerpt: 'Alexander Zverev ha mandato la Germania al Final 8 di Coppa Davis il 20 settembre. AP: 6-2, 6-4 su Dino Prizmic. TNT Sports: Gran Bretagna 4-0 Ecuador. Wikipedia nomina gli otto.',
      body: [
        'Gli US Open hanno già i nomi. La Laver Cup resta il 25-27 settembre all’O2. La domenica ha nominato gli ultimi biglietti del Final 8 per Bologna a novembre.',
        'AP: Zverev batte Prizmic 6-2, 6-4 in 77 minuti a Halle. Krawietz e Puetz avevano battuto Mektic e Pavic 7-5, 6-2. Germania 3-1. AP: Patten e Skupski 6-3, 6-4. TNT Sports e Wikipedia: Gran Bretagna 4-0 Ecuador. Wikipedia: Spagna 3-0 Cile.',
        'Wikipedia Final 8, Bologna, 24-29 novembre: Italia, Canada, Cechia, Austria, Corea del Sud, Germania, Gran Bretagna, Spagna. Non stampare un campione 2026. Non stampare un vincitore di Laver Cup. Quelle partite non sono state giocate.',
      ],
    },
    pl: {
      title: 'Niemcy 3-1 Chorwacja. Wielka Brytania 4-0 Ekwador. Final 8 Pucharu Davisa ustalony.',
      subtitle: 'AP: Zverev 6-2, 6-4 w 77 minut. Bolonia, 24-29 listopada. Laver Cup zostaje na przyszły tydzień.',
      excerpt: 'Alexander Zverev wprowadził Niemcy do Final 8 Pucharu Davisa 20 września. AP: 6-2, 6-4 z Dino Prizmiciem. TNT Sports: Wielka Brytania 4-0 Ekwador. Wikipedia wymienia ósemkę.',
      body: [
        'US Open ma już nazwiska. Laver Cup zostaje 25-27 września na O2. Niedziela nazwała ostatnie bilety Final 8 do Bolonii w listopadzie.',
        'AP: Zverev bije Prizmicia 6-2, 6-4 w 77 minut w Halle. Krawietz i Puetz pokonali wcześniej Mekticia i Pavicia 7-5, 6-2. Niemcy 3-1. AP: Patten i Skupski 6-3, 6-4. TNT Sports i Wikipedia: Wielka Brytania 4-0 Ekwador. Wikipedia: Hiszpania 3-0 Chile.',
        'Wikipedia Final 8, Bolonia, 24-29 listopada: Włochy, Kanada, Czechy, Austria, Korea Południowa, Niemcy, Wielka Brytania, Hiszpania. Nie drukuj mistrza 2026. Nie drukuj zwycięzcy Laver Cup. Te mecze nie zostały rozegrane.',
      ],
    },
    zh: {
      title: '德国 3-1 克罗地亚。英国 4-0 厄瓜多尔。戴维斯杯总决赛八强已定。',
      subtitle: '美联社：兹维列夫 6-2、6-4，用时 77 分钟。博洛尼亚，11 月 24-29 日。拉沃尔杯仍在下周。',
      excerpt: '9 月 20 日亚历山大·兹维列夫送德国进入戴维斯杯总决赛八强。美联社：6-2、6-4 击败普里兹米奇。TNT Sports：英国 4-0 厄瓜多尔。维基百科点出八强。',
      body: [
        '美网已有名字。拉沃尔杯仍是 9 月 25-27 日在 O2。周日点出了 11 月博洛尼亚总决赛八强的最后门票。',
        '美联社：兹维列夫在哈勒 6-2、6-4 用时 77 分钟击败普里兹米奇。克拉维茨/皮茨此前 7-5、6-2 击败梅克蒂奇/帕维奇。德国 3-1。美联社：帕滕/斯库普斯基 6-3、6-4。TNT 与维基百科：英国 4-0 厄瓜多尔。维基百科：西班牙 3-0 智利。',
        '维基百科总决赛八强，博洛尼亚，11 月 24-29 日：意大利、加拿大、捷克、奥地利、韩国、德国、英国、西班牙。不要打印 2026 冠军。不要打印拉沃尔杯冠军。那些比赛尚未进行。',
      ],
    },
    ja: {
      title: 'ドイツ 3-1 クロアチア。イギリス 4-0 エクアドル。デビスカップファイナル8が確定。',
      subtitle: 'AP：ズベレフ 6-2、6-4、77分。ボローニャ、11月24-29日。レーバーカップは来週のまま。',
      excerpt: '9月20日、アレクサンダー・ズベレフがドイツをデビスカップファイナル8へ送った。AP：プリズミッチに6-2、6-4。TNTスポーツ：イギリス 4-0 エクアドル。ウィキペディアが8か国を名指し。',
      body: [
        '全米オープンにはすでに名前がある。レーバーカップはなお9月25-27日、O2。日曜が11月ボローニャのファイナル8最後の切符を名付けた。',
        'AP：ズベレフがハレでプリズミッチに6-2、6-4、77分。クラヴィーツ/ピュッツが先にメクティッチ/パビッチに7-5、6-2。ドイツ 3-1。AP：パッテン/スクプスキ 6-3、6-4。TNTとウィキペディア：イギリス 4-0 エクアドル。ウィキペディア：スペイン 3-0 チリ。',
        'ウィキペディアのファイナル8、ボローニャ、11月24-29日：イタリア、カナダ、チェコ、オーストリア、韓国、ドイツ、イギリス、スペイン。2026年の王者を印刷しない。レーバーカップの勝者を印刷しない。それらの試合はまだ行われていない。',
      ],
    },
    ko: {
      title: '독일 3-1 크로아티아. 영국 4-0 에콰도르. 데이비스컵 파이널 8 확정.',
      subtitle: 'AP: 즈베레프 6-2, 6-4, 77분. 볼로냐, 11월 24-29일. 레이버컵은 다음 주.',
      excerpt: '9월 20일 알렉산더 즈베레프가 독일을 데이비스컵 파이널 8로 보냈다. AP: 프리즈미치에 6-2, 6-4. TNT 스포츠: 영국 4-0 에콰도르. 위키피디아가 8개국을 적었다.',
      body: [
        'US오픈에는 이미 이름이 있다. 레이버컵은 여전히 9월 25-27일 O2. 일요일이 11월 볼로냐 파이널 8의 마지막 티켓을 이름 붙였다.',
        'AP: 즈베레프가 할레에서 프리즈미치에 6-2, 6-4, 77분. 크라비츠/퓌츠가 먼저 멕티치/파비치에 7-5, 6-2. 독일 3-1. AP: 패튼/스쿱스키 6-3, 6-4. TNT와 위키피디아: 영국 4-0 에콰도르. 위키피디아: 스페인 3-0 칠레.',
        '위키피디아 파이널 8, 볼로냐, 11월 24-29일: 이탈리아, 캐나다, 체코, 오스트리아, 한국, 독일, 영국, 스페인. 2026 챔피언을 인쇄하지 마라. 레이버컵 우승자를 인쇄하지 마라. 그 경기는 아직 없다.',
      ],
    },
    ar: {
      title: 'ألمانيا 3-1 كرواتيا. بريطانيا 4-0 الإكوادور. نهائي 8 كأس ديفيس تحدّد.',
      subtitle: 'AP: زفيريف 6-2، 6-4 في 77 دقيقة. بولونيا، 24-29 تشرين الثاني/نوفمبر. كأس لافر ما زال الأسبوع المقبل.',
      excerpt: 'ألكسندر زفيريف أهّل ألمانيا إلى نهائي 8 كأس ديفيس في 20 أيلول/سبتمبر. AP: 6-2، 6-4 على دينو بريزميتش. TNT Sports: بريطانيا 4-0 الإكوادور. ويكيبيديا تسمّي الثمانية.',
      body: [
        'أمريكا المفتوحة لها أسماء. كأس لافر ما زال 25-27 أيلول/سبتمبر في O2. الأحد سمّى آخر تذاكر نهائي 8 لبولونيا في تشرين الثاني/نوفمبر.',
        'AP: زفيريف يهزم بريزميتش 6-2، 6-4 في 77 دقيقة في هاله. كرافيتس وبوتيز سبقا بفوز 7-5، 6-2 على ميكتتش وبافيتش. ألمانيا 3-1. AP: باتن وسكوبسكي 6-3، 6-4. TNT وويكيبيديا: بريطانيا 4-0 الإكوادور. ويكيبيديا: إسبانيا 3-0 تشيلي.',
        'ويكيبيديا نهائي 8، بولونيا، 24-29 تشرين الثاني/نوفمبر: إيطاليا، كندا، التشيك، النمسا، كوريا الجنوبية، ألمانيا، بريطانيا، إسبانيا. لا تطبع بطل 2026. لا تطبع فائز كأس لافر. تلك المباريات لم تُلعب.',
      ],
    },
  },
  'chiefs-colts-snf-33-30': {
    fr: {
      title: 'Chiefs 33-30 Colts : Butker scelle la victoire à 40 yards en prolongation',
      subtitle: 'CBS et Sky : 30-30 dans le temps réglementaire, Harrison Butker à 40 yards en prolongation. Kansas City à 2-0.',
      excerpt: 'Kansas City a battu Indianapolis 33-30 en prolongation lors du Sunday Night Football. Harrison Butker a réussi le coup de pied gagnant après un nul 30-30. Sky Sports et CBS confirment le score final.',
      body: [
        'Jeudi a offert un duel de 41-31 à Buffalo. Le Sunday Night Football à Arrowhead a répondu par un drame en prolongation : 30-30 après quatre quart-temps, puis la mort subite sous les projecteurs.',
        'Sky Sports, CBS et Chiefs.com détaillent un match intense entre deux attaques explosives. Patrick Mahomes a mené l’égalisation en fin de quatrième quart-temps, tandis qu’Indianapolis a forcé un 30-30 au terme du temps réglementaire.',
        'En prolongation, la défense de Kansas City a stoppé Indianapolis. Mahomes a placé l’attaque à portée, et Harrison Butker a envoyé son coup de pied de 40 yards entre les poteaux. Kansas City passe à 2-0.',
      ],
    },
    es: {
      title: 'Chiefs 33-30 Colts: Butker anota de 40 yardas en la prórroga',
      subtitle: 'CBS y Sky: 30-30 en tiempo regular, Harrison Butker de 40 yardas en tiempo extra. Kansas City 2-0.',
      excerpt: 'Kansas City venció 33-30 a Indianapolis en la prórroga de Sunday Night Football. Harrison Butker anotó el gol de campo ganador tras el 30-30 regular. Sky Sports y CBS confirman el resultado.',
      body: [
        'El jueves dejó un 41-31 en Buffalo. Sunday Night Football en Arrowhead respondió con drama de prórroga: 30-30 tras cuatro cuartos, seguido de muerte súbita bajo las luces.',
        'Sky Sports, CBS y Chiefs.com detallan un choque vibrante. Patrick Mahomes armó ofensivas tardías en el cuarto periodo para empatar, mientras Indianapolis forzó el 30-30 al cierre del tiempo regular.',
        'En tiempo extra, la defensa de Kansas City frenó a los Colts. Mahomes llevó la ofensiva a zona de gol de campo y Harrison Butker acertó desde 40 yardas. Kansas City se coloca 2-0.',
      ],
    },
    de: {
      title: 'Chiefs 33:30 Colts: Butker trifft aus 40 Yards in der Verlängerung',
      subtitle: 'CBS und Sky: 30:30 nach vier Vierteln, Harrison Butker aus 40 Yards in der Overtime. Kansas City 2-0.',
      excerpt: 'Kansas City schlägt Indianapolis 33:30 nach Verlängerung im Sunday Night Football. Harrison Butker traf das siegbringende Field Goal aus 40 Yards nach 30:30 in der regulären Spielzeit.',
      body: [
        'Donnerstag brachte ein 41:31 in Buffalo. Sunday Night Football im Arrowhead antwortete mit Verlängerungs-Drama: 30:30 nach vier Vierteln und Entscheidung in der Overtime.',
        'Sky Sports, CBS und Chiefs.com berichten von einem packenden Duell. Patrick Mahomes führte späte Angriffsserien an, während Indianapolis den 30:30-Ausgleich zur Verlängerung erzwang.',
        'In der Overtime stoppte Kansas Citys Defensive die Colts. Mahomes brachte den Ball in Position, und Harrison Butker verwandelte sicher aus 40 Yards zum 33:30. Kansas City steht 2-0.',
      ],
    },
    it: {
      title: 'Chiefs 33-30 Colts: Butker firma il trionfo da 40 yard ai supplementari',
      subtitle: 'CBS e Sky: 30-30 nei regolamentari, Harrison Butker da 40 yard all’overtime. Kansas City a 2-0.',
      excerpt: 'Kansas City supera Indianapolis 33-30 all’overtime nel Sunday Night Football. Harrison Butker calcia il field goal decisivo dopo il 30-30 dei regolamentari. Sky Sports e CBS confermano il finale.',
      body: [
        'Giovedì aveva regalato un 41-31 a Buffalo. Il Sunday Night Football ad Arrowhead ha risposto con una sfida spettacolare: 30-30 al termine dei quattro quarti e supplementari decisivi.',
        'Sky Sports, CBS e Chiefs.com descrivono una gara ad altissima intensità. Patrick Mahomes ha guidato la rimonta nel quarto quarto prima che Indianapolis pareggiasse sul 30-30 finale.',
        'Ai supplementari la difesa di Kansas City ha fermato l’attacco avversario. Mahomes ha condotto il drive decisivo e Harrison Butker ha centrato i pali da 40 yard. Kansas City sale a 2-0.',
      ],
    },
    pl: {
      title: 'Chiefs 33-30 Colts: Butker trafia z 40 jardów w dogrywce',
      subtitle: 'CBS i Sky: 30-30 w regulaminowym czasie, Harrison Butker z 40 jardów w dogrywce. Kansas City 2-0.',
      excerpt: 'Kansas City pokonało Indianapolis 33-30 po dogrywce w Sunday Night Football. Harrison Butker zdobył zwycięskie punkty po remisie 30-30. Sky Sports i CBS potwierdzają wynik.',
      body: [
        'Czwartek przyniósł 41-31 w Buffalo. Sunday Night Football na Arrowhead odpowiedział dramatem w dogrywce: 30-30 po czterech kwartach i decydujący cios w doliczonym czasie.',
        'Sky Sports, CBS i Chiefs.com opisują zacięte starcie. Patrick Mahomes poprowadził kluczowe akcje w czwartej kwarcie, a Indianapolis doprowadziło do dogrywki przy stanie 30-30.',
        'W dogrywce defensywa Kansas City zatrzymała rywali. Mahomes ustawił pozycję do kopnięcia, a Harrison Butker pewnie trafił z 40 jardów. Kansas City ma bilans 2-0.',
      ],
    },
    zh: {
      title: '酋长 33-30 小马：巴特克加时赛 40 码射门绝杀',
      subtitle: 'CBS 与天空体育：常规时间 30-30 战平，哈里森·巴特克加时 40 码绝杀。堪萨斯城开季 2 胜 0 负。',
      excerpt: '堪萨斯城酋长在周日夜赛加时以 33-30 险胜印第安纳波利斯小马。在常规时间战成 30-30 后，巴特克命中 40 码任意球制胜。天空体育与 CBS 确认终场比分。',
      body: [
        '周四夜赛在布法罗打出 41-31 的对攻大战。箭头体育场的周日夜赛则上演加时苦战：四节战罢 30-30，随后进入骤死加时。',
        '天空体育、CBS 与酋长官网报道了这场惊心动魄的较量。帕特里克·马霍姆斯在第四节后段主导进攻，而小马队展现顽强韧性将比赛拖入加时。',
        '加时赛中，酋长防守组率先完成关键防守。马霍姆斯推进至射门距离，哈里森·巴特克稳稳命中 40 码任意球，助酋长 33-30 取胜取得开季两连胜。',
      ],
    },
    ja: {
      title: 'チーフス 33-30 コルツ：バトカーが延長40ヤード決勝FG',
      subtitle: 'CBSとSky：レギュラータイム30-30、ハリソン・バトカーがOTで40ヤードV弾。カンザスシティ開幕2勝。',
      excerpt: 'カンザスシティ・チーフスがサンデーナイトの延長戦でインディアナポリス・コルツを33-30で破った。4クォーター30-30の後、バトカーが40ヤードFGを沈めた。',
      body: [
        '木曜はバッファローで41-31の激闘。アローヘッドのサンデーナイトは延長戦のドラマで応えた。4クォーター終えて30-30、ナイターの死闘へ。',
        'Sky Sports、CBS、チーフス公式が激しい攻防を詳報。パトリック・マホームズが第4Q終盤にドライブを決めるも、コルツも粘り30-30で延長に突入した。',
        '延長ではチーフス守備陣が相手をストップ。マホームズが射程圏へ運び、ハリソン・バトカーが40ヤードFGを決めて33-30。チーフスが開幕2連勝を飾った。',
      ],
    },
    ko: {
      title: '치프스 33-30 콜츠: 벗커, 연장 40야드 끝내기 필드골',
      subtitle: 'CBS와 스카이: 정규시간 30-30, 해리슨 벗커 연장 40야드 결승골. 캔자스시티 2승 무패.',
      excerpt: '캔자스시티가 선데이 나이트 풋볼 연장전에서 인디애나폴리스를 33-30으로 꺾었다. 정규시간 30-30 동점 후 벗커가 40야드 끝내기 골을 성공했다.',
      body: [
        '목요일 버펄로에서 41-31 난타전이 펼쳐졌고, 애로헤드의 선데이 나이트는 연장 승부로 응답했다. 4쿼터 30-30 동점 후 연장 서든데스로 향했다.',
        '스카이 스포츠와 CBS는 팽팽한 공격전을 전했다. 패트릭 마홈스가 4쿼터 막판 득점을 이끌었으나 인디애나폴리스도 물러서지 않고 동점을 만들었다.',
        '연장전에서 캔자스시티 수비가 첫 공격을 막아냈고, 마홈스가 사정거리로 진입시킨 뒤 해리슨 벗커가 40야드 킥을 성공시켜 33-30 승리를 확정지었다.',
      ],
    },
    ar: {
      title: 'تشيفز 33-30 كولتس: باتكر يسجل هدف الفوز من 40 ياردة في الوقت الإضافي',
      subtitle: 'CBS وسكاي: التعادل 30-30 في الوقت الأصلي، وهاريسون باتكر يحسمها في الشوط الإضافي. كانساس سيتي 2-0.',
      excerpt: 'حقق كانساس سيتي فوزا مثيرا 33-30 على إنديانابوليس في الوقت الإضافي لمباراة ليلة الأحد. هاريسون باتكر سدد ركلة الحسم بعد تعادل 30-30. سكاي وCBS تؤكدان النتيجة.',
      body: [
        'شهد يوم الخميس مواجهة هجومية انتهت 41-31 في بوفالو. ورد ملعب أروهيد في ليلة الأحد بمباراة مثيرة انتهت بالتعادل 30-30 قبل التمديد للشوط الإضافي.',
        'نقلت سكاي وCBS وتفاصيل موقع تشيفز تبادلا مستمرا للهجمات. قاد باتريك ماهومز محاولات هجومية حاسمة بينما فرض إنديانابوليس التعادل 30-30 مع نهاية الوقت الأصلي.',
        'في الشوط الإضافي تصدى دفاع كانساس سيتي للمحاولة الأولى، ثم تقدم ماهومز بالكرة ليسدد هاريسون باتكر كرة الفوز من 40 ياردة محققا فوز تشيفز 33-30 ليرفع رصيده إلى 2-0.',
      ],
    },
  },
  'rams-giants-mnf-28-6': {
    fr: {
      title: 'Rams 28-6 Giants : Los Angeles maîtrise la nuit de lundi, Dart se blesse',
      subtitle: 'Deux touchdowns pour Stafford, la défense des Rams intraitable. Blessure de Jaxson Dart. La 2e journée est close.',
      excerpt: 'Los Angeles a dominé les New York Giants 28-6 lors du Monday Night Football au SoFi Stadium. Matthew Stafford a lancé deux passes de touchdown et Jaxson Dart est sorti sur blessure au genou.',
      body: [
        'La 2e journée s’est achevée en Californie. Après l’ouverture à Buffalo et la prolongation à Kansas City, le Monday Night Football au SoFi Stadium a vu les Rams signer leur première victoire 28-6.',
        'Sky Sports et NFL.com soulignent la maîtrise de Matthew Stafford en première mi-temps avec deux touchdowns. New York a perdu son quarterback Jaxson Dart sur blessure au genou avant la pause.',
        'La défense de Los Angeles n’a accordé que deux field goals en soixante minutes. Les deux clubs affichent un bilan de 1-1, fermant définitivement le chapitre de la 2e journée.',
      ],
    },
    es: {
      title: 'Rams 28-6 Giants: Los Angeles manda el lunes por la noche y Dart sale lesionado',
      subtitle: 'Dos touchdowns de Stafford y defensa dominante de Rams. Lesión de Jaxson Dart. Semana 2 cerrada.',
      excerpt: 'Los Angeles venció 28-6 a New York Giants en Monday Night Football en SoFi Stadium. Matthew Stafford sumó dos pases de anotación y Jaxson Dart se marchó con una lesión de rodilla.',
      body: [
        'La semana 2 culminó en California. Tras la apertura en Buffalo y el tiempo extra en Kansas City, Monday Night Football en SoFi Stadium entregó el primer triunfo de Rams por 28-6.',
        'Sky Sports y NFL.com destacan el dominio de Matthew Stafford en la primera mitad con dos pases de touchdown. Los Giants sufrieron la salida de su mariscal Jaxson Dart por lesión de rodilla.',
        'La defensa angelina solo permitió dos goles de campo en todo el partido. Con este 28-6 ambos equipos quedan 1-1 y la semana 2 de la NFL concluye por completo.',
      ],
    },
    de: {
      title: 'Rams 28:6 Giants: Los Angeles dominiert Monday Night, Dart verletzt raus',
      subtitle: 'Stafford wirft zwei Touchdowns, Rams-Defensive bärenstark. Knieverletzung bei Jaxson Dart. Woche 2 beendet.',
      excerpt: 'Los Angeles schlägt die New York Giants 28:6 im Monday Night Football im SoFi Stadium. Matthew Stafford warf zwei Touchdowns, während Jaxson Dart mit Knieproblemen ausschied.',
      body: [
        'Woche 2 endete am Montagabend in Kalifornien. Nach dem Auftakt in Buffalo und dem Krimi in Kansas City feierten die Rams im SoFi Stadium ihren ersten Saisonsieg mit 28:6.',
        'Sky Sports und NFL.com berichten von Staffords starker erster Hälfte mit zwei Touchdown-Pässen. Die Giants wurden durch den frühen Ausfall von Quarterback Jaxson Dart schwer getroffen.',
        'Die Defensive der Rams ließ in 60 Minuten lediglich zwei Field Goals zu. Beide Teams stehen nun bei 1-1, und Woche 2 der NFL ist offiziell komplett abgeschlossen.',
      ],
    },
    it: {
      title: 'Rams 28-6 Giants: Los Angeles vince il Monday Night, Dart esce per infortunio',
      subtitle: 'Due touchdown di Stafford, difesa dei Rams insuperabile. Stop per Jaxson Dart. Week 2 conclusa.',
      excerpt: 'Los Angeles travolge i New York Giants 28-6 nel Monday Night Football al SoFi Stadium. Due touchdown lanciati da Matthew Stafford e infortunio al ginocchio per Jaxson Dart.',
      body: [
        'La Week 2 si è chiusa in California. Dopo le emozioni di Buffalo e l’overtime di Kansas City, il Monday Night Football al SoFi Stadium ha consegnato il primo successo ai Rams per 28-6.',
        'Sky Sports e NFL.com evidenziano la prestazione di Matthew Stafford, autore di due lanci da touchdown. New York ha perso il quarterback titolare Jaxson Dart per un infortunio al ginocchio.',
        'La difesa dei padroni di casa ha concesso appena due field goal in tutta la serata. Entrambe le formazioni salgono a quota 1-1 e la seconda giornata va definitivamente in archivio.',
      ],
    },
    pl: {
      title: 'Rams 28-6 Giants: Los Angeles pewnie wygrywa w poniedziałek, Dart z kontuzją',
      subtitle: 'Dwa przyłożenia Stafforda, świetna defensywa Rams. Kontuzja kolana Jaxsona Darta. 2. tydzień zamknięty.',
      excerpt: 'Los Angeles pokonało New York Giants 28-6 w Monday Night Football na SoFi Stadium. Matthew Stafford rzucił dwa przyłożenia, a Jaxson Dart przedwcześnie opuścił boisko z urazem kolana.',
      body: [
        'Tydzień 2 zakończył się w Kalifornii. Po meczu w Buffalo i dogrywce w Kansas City poniedziałkowe starcie na SoFi Stadium dało Rams pierwsze zwycięstwo w sezonie, 28-6.',
        'Sky Sports i NFL.com podkreślają znakomitą pierwszą połowę Matthew Stafforda z dwoma podaniami na przyłożenie. Giants ponieśli dotkliwą stratę po kontuzji kolana Jaxsona Darta.',
        'Obrona Rams pozwoliła rywalom zaledwie na dwa kopnięcia z gry w całym meczu. Wynik 28-6 oznacza bilans 1-1 dla obu ekip i ostateczne zamknięcie 2. tygodnia NFL.',
      ],
    },
    zh: {
      title: '公羊 28-6 巨人：洛杉矶周一夜赛轻取对手，达特伤退',
      subtitle: '斯塔福德传出两次达阵，公羊防守组坚不可摧。贾克森·达特膝伤退场。NFL 第 2 周完结。',
      excerpt: '洛杉矶公羊在 SoFi 体育场的周一夜赛中以 28-6 战胜纽约巨人。马修·斯塔福德送出两次达阵，巨人四分卫达特因膝伤提前离场。天空体育与 NFL 确认比分。',
      body: [
        'NFL 第 2 周在加州落下帷幕。继布法罗的高比分大战和堪萨斯城的加时绝杀后，SoFi 体育场的周一夜赛见证了公羊以 28-6 斩获赛季首胜。',
        '天空体育与 NFL 官网报道，斯塔福德上半场发挥稳健，先后连线队友完成两次达阵。巨人队则遭遇重大打击，首发四分卫达特因膝伤提前退赛。',
        '公羊防守组全场仅让巨人命中两记任意球，彻底掌控了比赛走势。这场 28-6 让双方战绩均变为 1 胜 1 负，第 2 周 16 场比赛至此全部结束。',
      ],
    },
    ja: {
      title: 'ラムズ 28-6 ジャイアンツ：LAがマンデーナイト完勝、ダートは負傷交代',
      subtitle: 'スタッフォードが2TDパス、ラムズ守備がFGのみに封じる。ダート膝負傷。第2週全試合終了。',
      excerpt: 'ロサンゼルス・ラムズがSoFiスタジアムのマンデーナイトでニューヨーク・ジャイアンツを28-6で撃破。スタッフォードが2TDを挙げ、ダートが負傷退場した。',
      body: [
        '第2週の最後はカリフォルニアで締めくくられた。バッファローの乱打戦、カンザスシティの延長劇に続き、SoFiスタジアムでラムズが28-6の今季初白星を掴んだ。',
        'Sky SportsとNFL公式によれば、マシュー・スタッフォードが前半に2つのTDパスを通し主導権を握った。ジャイアンツはQBジャクソン・ダートが膝の負傷で途中退場。',
        'ラムズ守備陣は相手を2本のFGに抑え込み、試合を通じて隙を見せなかった。28-6の決着で両軍ともに1勝1敗となり、NFL第2週が全日程を終えた。',
      ],
    },
    ko: {
      title: '램스 28-6 자이언츠: LA, 먼데이 나이트 완승 속 다트 부상 강판',
      subtitle: '스태퍼드 2개 터치다운, 램스 수비 필드골만 허용. 잭슨 다트 무릎 부상. 2주차 완료.',
      excerpt: 'LA 램스가 SoFi 스타디움에서 열린 먼데이 나이트 풋볼에서 뉴욕 자이언츠를 28-6으로 완파했다. 매슈 스태퍼드가 2개의 터치다운을 기록했고 다트는 부상으로 퇴장했다.',
      body: [
        'NFL 2주차가 캘리포니아에서 마무리되었다. 버펄로의 화력전과 캔자스시티의 연장전에 이어 SoFi 스타디움에서 램스가 28-6으로 시즌 첫 승을 거뒀다.',
        '스카이 스포츠와 NFL닷컴은 스태퍼드가 전반에만 2개의 터치다운 패스를 성공시키며 경기를 주도했다고 전했다. 자이언츠는 쿼터백 잭슨 다트가 무릎 부상으로 조기 이탈했다.',
        '램스 수비진은 60분 동안 단 2개의 필드골만 허용하며 완승을 이끌었다. 28-6으로 두 팀 모두 1승 1패가 되었으며, 2주차 일정이 모두 종료되었다.',
      ],
    },
    ar: {
      title: 'رامز 28-6 جاينتس: لوس أنجلوس يتفوق في ليلة الاثنين ودارت يخرج مصابا',
      subtitle: 'تمريرتا هبوط من ستافورد ودفاع رامز يمنع المحاولات. إصابة ركبة لجاكسون دارت. اكتمال الأسبوع 2.',
      excerpt: 'تغلب لوس أنجلوس رامز على نيويورك جاينتس 28-6 في مباراة ليلة الاثنين على ملعب سوفاي. أرسل ماثيو ستافورد تمريرتي هبوط بينما خرج جاكسون دارت مصابا في الركبة.',
      body: [
        'اختتمت منافسات الأسبوع الثاني في كاليفورنيا. بعد الإثارة في بوفالو وكانساس سيتي، حقق رامز فوزه الأول هذا الموسم بنتيجة 28-6 على ملعب سوفاي في ليلة الاثنين.',
        'ذكرت سكاي وموقع NFL أن ماثيو ستافورد أحكم السيطرة مبكرا بتمريرتي هبوط. وتلقى جاينتس ضربة قوية بخروج لاعب الوسط جاكسون دارت مصابا في ركبته.',
        'وفرض دفاع رامز سيطرته الكاملة مكتفيا بالسماح بركلتي جزاء طوال اللقاء. رفعت النتيجة رصيد الفريقين إلى فوز وهزيمة لكل منهما، معلنة ختام الأسبوع الثاني رسميا.',
      ],
    },
  },
  'presidents-cup-medinah-2026': {
    fr: {
      title: 'Presidents Cup à Medinah : USA, Internationaux et le parcours n°3',
      subtitle: 'Brandt Snedeker mène les USA, Geoff Ogilvy les Internationaux. 12e participation pour Adam Scott. Entraînements lancés.',
      excerpt: 'La 16e Presidents Cup se déroule au Medinah Country Club dans l’Illinois du 22 au 27 septembre. Les entraînements officiels ont débuté avant le coup d’envoi de la compétition jeudi.',
      body: [
        'Après la victoire de JJ Spaun au BMW PGA Championship à Wentworth à 17 sous le par, le golf mondial bascule vers le jeu par équipes. Le Medinah Country Club accueille la 16e Presidents Cup sur son parcours n°3 entièrement rénové.',
        'Le PGA Tour et PresidentsCup.com détaillent les équipes réunies en Illinois dès le 22 septembre. Brandt Snedeker dirige l’équipe américaine avec Scottie Scheffler, Cameron Young, Wyndham Clark, Sam Burns, Collin Morikawa et Patrick Cantlay.',
        'Geoff Ogilvy mène l’équipe internationale avec Adam Scott qui dispute sa 12e coupe, Hideki Matsuyama, Min Woo Lee et Ryan Fox. La compétition officielle commence jeudi 24 septembre.',
      ],
    },
    es: {
      title: 'Presidents Cup en Medinah: Estados Unidos, Internacionales y el campo n°3',
      subtitle: 'Brandt Snedeker capitanea a USA, Geoff Ogilvy al equipo Internacional. Adam Scott en su 12ª copa. Prácticas en marcha.',
      excerpt: 'La 16ª Presidents Cup llega al Medinah Country Club en Illinois del 22 al 27 de septiembre. Las rondas de práctica están en marcha antes del inicio del torneo el jueves.',
      body: [
        'Tras el triunfo de JJ Spaun en el BMW PGA Championship en Wentworth con 17 bajo par, el golf centra su atención en el duelo por equipos. Medinah Country Club recibe la 16ª Presidents Cup en su Course No. 3.',
        'PGA Tour y PresidentsCup.com destacan la llegada de los equipos el 22 de septiembre. Brandt Snedeker lidera a los estadounidenses con Scottie Scheffler, Cameron Young, Wyndham Clark, Sam Burns, Collin Morikawa y Patrick Cantlay.',
        'Geoff Ogilvy comanda a los Internacionales con el veterano Adam Scott en su 12ª edición, Hideki Matsuyama, Min Woo Lee y Ryan Fox. La competición oficial arranca el jueves 24 de septiembre.',
      ],
    },
    de: {
      title: 'Presidents Cup in Medinah: USA, Internationales Team und Course No. 3',
      subtitle: 'Brandt Snedeker führt USA an, Geoff Ogilvy das internationale Team. Adam Scotts 12. Auftritt. Training läuft.',
      excerpt: 'Der 16. Presidents Cup gastiert vom 22. bis 27. September im Medinah Country Club in Illinois. Die offiziellen Trainingsrunden laufen, bevor am Donnerstag die Matches beginnen.',
      body: [
        'Nach JJ Spauns Sieg bei der BMW PGA Championship in Wentworth mit 17 unter Par schaut die Golfwelt auf den Teamwettbewerb. Der Medinah Country Club richtet den 16. Presidents Cup auf Course No. 3 aus.',
        'PGA Tour und PresidentsCup.com melden die Ankunft der Teams am 22. September. Brandt Snedeker leitet die USA mit Scottie Scheffler, Cameron Young, Wyndham Clark, Sam Burns, Collin Morikawa und Patrick Cantlay.',
        'Geoff Ogilvy führt das internationale Team mit Rekordspieler Adam Scott in dessen 12. Auflage, Hideki Matsuyama, Min Woo Lee und Ryan Fox an. Der offizielle Wettkampf startet am Donnerstag, 24. September.',
      ],
    },
    it: {
      title: 'Presidents Cup a Medinah: USA, Internazionali e il Course No. 3',
      subtitle: 'Brandt Snedeker guida gli USA, Geoff Ogilvy gli Internazionali. 12ª presenza per Adam Scott. Prove in corso.',
      excerpt: 'La 16ª Presidents Cup va in scena al Medinah Country Club in Illinois dal 22 al 27 settembre. Prove ufficiali sul Course No. 3 prima delle gare di giovedì.',
      body: [
        'Dopo il successo di JJ Spaun al BMW PGA Championship a Wentworth a 17 sotto il par, il golf vira sulle sfide a squadre. Il Medinah Country Club ospita la 16ª Presidents Cup sul Course No. 3.',
        'PGA Tour e PresidentsCup.com confermano l’arrivo dei team in Illinois il 22 settembre. Brandt Snedeker è il capitano USA con Scottie Scheffler, Cameron Young, Wyndham Clark, Sam Burns, Collin Morikawa e Patrick Cantlay.',
        'Geoff Ogilvy guida gli Internazionali con Adam Scott alla sua 12ª presenza record, Hideki Matsuyama, Min Woo Lee e Ryan Fox. La competizione ufficiale si accenderà giovedì 24 settembre.',
      ],
    },
    pl: {
      title: 'Presidents Cup w Medinah: USA, Międzynarodowi i Course No. 3',
      subtitle: 'Brandt Snedeker prowadzi USA, Geoff Ogilvy drużynę międzynarodową. 12. występ Adama Scotta. Treningi trwają.',
      excerpt: '16. Presidents Cup zawita do Medinah Country Club w Illinois w dniach 22-27 września. Oficjalne rundy treningowe już trwają przed czwartkową rywalizacją.',
      body: [
        'Po wygranej JJ Spauna w BMW PGA Championship w Wentworth z wynikiem 17 poniżej par uwaga golfowego świata skupia się na rywalizacji drużynowej. Medinah Country Club gości 16. Presidents Cup na polu Course No. 3.',
        'PGA Tour i PresidentsCup.com opisują przygotowania zespołów w Illinois od 22 września. Brandt Snedeker kapitanuje drużynie USA z Scottiem Schefflerem, Cameronem Youngiem, Wyndhamem Clarkiem, Samem Burnsem i Collinem Morikawą.',
        'Geoff Ogilvy stoi na czele drużyny międzynarodowej z Adamem Scottem rozgrywającym 12. turniej, Hidekim Matsuyamą, Min Woo Lee i Ryanem Foxem. Oficjalne zmagania rozpoczną się w czwartek 24 września.',
      ],
    },
    zh: {
      title: '麦迪纳总统杯：美国队、国际队与3号球场',
      subtitle: '斯内德克尔领衔美国队，奥格维统帅国际队。亚当·斯科特第12次参赛。官方试场已开启。',
      excerpt: '第16届总统杯于9月22-27日在伊利诺伊州麦迪纳乡村俱乐部举行。正赛于周四打响前，各队正在3号球场进行官方试场备战。',
      body: [
        '在斯庞以低于标准杆17杆加冕温特沃斯宝马PGA锦标赛后，高尔夫焦点迅速转向团队对抗。麦迪纳乡村俱乐部在焕然一新的3号球场承办第16届总统杯。',
        '美巡赛与总统杯官网报道，两队于9月22日集结备战。布兰特·斯内德克尔执掌美国队，阵容包含世界第一舍夫勒、扬、克拉克、伯恩斯、森川与坎特利。',
        '杰夫·奥格维率领国际队，老将亚当·斯科特追平纪录迎来第12次参赛，携手松山英树、李旻宇与福克斯出征。正赛将于9月24日周四正式开杆。',
      ],
    },
    ja: {
      title: 'メディナのプレジデンツカップ：米国選抜、世界選抜、第3コース',
      subtitle: 'スネデカーが米国を率い、オギルビーが世界選抜を指揮。アダム・スコット12度目出場。公式練習開始。',
      excerpt: '第16回プレジデンツカップが9月22-27日にイリノイ州メディナCCで開催。木曜の競技開始を前に、第3コースでの公式練習ラウンドが進行している。',
      body: [
        'JJスパーンがウェントワースのBMW PGA選手権を通算17アンダーで制した後、ゴルフ界は団体対抗戦へと移った。メディナCCの改修された第3コースで第16回プレジデンツカップが開幕する。',
        'PGAツアーと大会公式によれば、選手団は9月22日に現地入りした。ブラント・スネデカー率いる米国選抜は世界1位シェフラー、ヤング、クラーク、バーンズ、モリカワらが並ぶ。',
        'ジェフ・オギルビー率いる世界選抜は最多タイ12回出場のスコットをはじめ、松山英樹、ミンウー・リー、フォックスらで挑む。公式競技は9月24日木曜日に火ぶたを切る。',
      ],
    },
    ko: {
      title: '메디나 프레지던츠컵: 미국팀, 인터내셔널팀, 3번 코스',
      subtitle: '스네데커 미국 단장, 오길비 인터내셔널 단장. 애덤 스콧 12번째 출전. 공식 연습 돌입.',
      excerpt: '제16회 프레지던츠컵이 9월 22-27일 일리노이주 메디나 컨트리클럽에서 열린다. 목요일 개막에 앞서 3번 코스에서 공식 연습라운드가 진행 중이다.',
      body: [
        'JJ 스폰이 웬트워스 BMW PGA 챔피언십에서 17언더파로 정상에 오른 직후 골프계는 대항전으로 향했다. 메디나 CC가 재설계된 3번 코스에서 제16회 프레지던츠컵을 개최한다.',
        'PGA 투어와 대회 공식에 따르면 각 팀은 9월 22일 현지에 모여 연습에 돌입했다. 브랜트 스네데커 단장의 미국팀에는 세계 1위 셰플러, 영, 클라크, 번스, 모리카와 등이 포진했다.',
        '제프 오길비 단장의 인터내셔널팀은 최다 출전 타이인 12번째 대회에 나서는 애덤 스콧과 마쓰야마 히데키, 이민우, 라이언 폭스 등으로 맞선다. 정규 경기는 9월 24일 목요일 시작된다.',
      ],
    },
    ar: {
      title: 'كأس الرؤساء في مدينا: الولايات المتحدة والفريق الدولي والملعب رقم 3',
      subtitle: 'براندت سنيديكر يقود أمريكا وجيف أوجيلفي يقود الفريق الدولي. المشاركة 12 لآدم سكوت. انطلاق التدريبات.',
      excerpt: 'تقام النسخة 16 من كأس الرؤساء في نادي مدينا بولاية إلينوي من 22 إلى 27 أيلول/سبتمبر. تجري الجولات التدريبية الرسمية على الملعب رقم 3 قبل انطلاق المنافسات يوم الخميس.',
      body: [
        'بعد تتويج جيه جيه سباون ببطولة BMW PGA في وينتوورث بنتيجة 17 تحت المعدل، يتحول اهتمام الغولف إلى مواجهة الفرق. يستضيف نادي مدينا الريفي كأس الرؤساء 16 على ملعبه رقم 3 المجدد.',
        'أفادت رابطة لاعبي الغولف المحترفين بوصول الفرق إلى إلينوي في 22 أيلول/سبتمبر. يقود براندت سنيديكر الفريق الأمريكي الذي يضم المصنف الأول شيفلر ويونغ وكلارك وبيرنز وموريكاوا.',
        'يقود جيف أوجيلفي الفريق الدولي بمشاركة تاريخية هي 12 لآدم سكوت إلى جانب هيديكي ماتسوياما ومين وو لي ورايان فوكس. تبدأ المنافسات الرسمية يوم الخميس 24 أيلول/سبتمبر.',
      ],
    },
  },

  'falcons-packers-tnf-week3-2026': {
    fr: {
      title: 'Falcons chez les Packers : Penix de retour sous les projecteurs de Lambeau pour la 3e journée',
      subtitle: 'Michael Penix Jr. revient d’une rupture du ligament croisé. Jordan Love et Green Bay célèbrent le week-end des anciens. Prime Video jeudi.',
      excerpt: 'La 3e journée s’ouvre jeudi soir à Lambeau Field avec Green Bay face à Atlanta. Michael Penix Jr. reprend sa place de titulaire après sa convalescence.',
      body: [
        'La 2e journée s’est achevée lundi soir à Los Angeles sans laisser de répit. Le calendrier de la NFL enchaîne directement avec la 3e journée jeudi soir dans le stade mythique de Lambeau Field.',
        'NFL.com et Sports Illustrated confirment qu’Atlanta confiera à nouveau les commandes à Michael Penix Jr. jeudi soir. Le jeune quarterback revient plus tôt que prévu après sa rééducation, remplaçant Cooper Rush alors que les Falcons cherchent une première victoire après un départ à 0-2.',
        'En face, Jordan Love mène les Packers avec un bilan de 1-1 après un succès 20-17 en prolongation face aux Jets. La franchise célèbre son week-end des anciens en présence de plus de cinquante légendes pour les anniversaires du Super Bowl I et du Super Bowl XXXI.',
      ],
    },
    es: {
      title: 'Falcons en casa de Packers: Penix regresa bajo los focos de Lambeau para abrir la semana 3',
      subtitle: 'Michael Penix Jr. vuelve tras romperse el ligamento cruzado. Jordan Love y Green Bay celebran el fin de semana de exalumnos. Prime Video jueves.',
      excerpt: 'La semana 3 arranca el jueves por la noche en Lambeau Field con Green Bay recibiendo a Atlanta. Michael Penix Jr. vuelve a la titularidad tras su recuperación.',
      body: [
        'La semana 2 concluyó el lunes por la noche en Los Ángeles sin dar tregua. El calendario de la NFL avanza de inmediato hacia la semana 3 el jueves por la noche en el legendario Lambeau Field.',
        'NFL.com y Sports Illustrated informan de que Atlanta devolverá la titularidad a Michael Penix Jr. el jueves. El pasador regresa antes de lo previsto tras rehabilitarse de su lesión de rodilla, relevando a Cooper Rush mientras los Falcons buscan su primer triunfo tras empezar 0-2.',
        'En el otro bando, Jordan Love guía a los Packers con marca de 1-1 tras ganar 20-17 en tiempo extra a los Jets. Green Bay celebra su fin de semana de leyendas con más de cincuenta exjugadores conmemorando los aniversarios del Super Bowl I y Super Bowl XXXI.',
      ],
    },
    de: {
      title: 'Falcons bei den Packers: Penix kehrt unter Flutlicht im Lambeau Field zur Woche 3 zurück',
      subtitle: 'Michael Penix Jr. nach Kreuzbandriss zurück. Jordan Love und Green Bay feiern Alumni-Wochenende. Prime Video Donnerstag.',
      excerpt: 'Woche 3 beginnt am Donnerstagabend im Lambeau Field, wenn Green Bay die Atlanta Falcons empfängt. Michael Penix Jr. kehrt nach seiner Genesung in die Startelf zurück.',
      body: [
        'Woche 2 endete erst am Montagabend in Los Angeles. Der NFL-Spielplan rollt am Donnerstagabend im legendären Lambeau Field nahtlos in Woche 3.',
        'NFL.com und Sports Illustrated melden, dass Atlanta am Donnerstag wieder auf Michael Penix Jr. setzt. Der Spielmacher kehrt nach erfolgreicher Reha früher als erwartet zurück und ersetzt Cooper Rush, während die Falcons nach zwei Niederlagen ihren ersten Saisonsieg anpeilen.',
        'Auf der Gegenseite führt Jordan Love die Packers mit einer 1-1-Bilanz nach dem 20:17-Overtime-Erfolg gegen die Jets an. Green Bay ehrt beim Alumni-Wochenende mit über fünfzig Legenden die Meilensteine von Super Bowl I und Super Bowl XXXI.',
      ],
    },
    it: {
      title: 'Falcons a Green Bay: Penix torna sotto i riflettori di Lambeau per aprire la Week 3',
      subtitle: 'Michael Penix Jr. rientra dopo la rottura del crociato. Jordan Love e i Packers celebrano l’Alumni Weekend. Giovedì su Prime Video.',
      excerpt: 'La Week 3 si apre giovedì notte a Lambeau Field con i Green Bay Packers che ospitano gli Atlanta Falcons. Michael Penix Jr. torna titolare dopo l’infortunio.',
      body: [
        'La Week 2 si è chiusa lunedì notte a Los Angeles senza sosta. Il calendario NFL prosegue giovedì notte con la Week 3 nel tempio di Lambeau Field.',
        'NFL.com e Sports Illustrated riportano che Atlanta affiderà la regia a Michael Penix Jr. giovedì notte. Il giovane quarterback torna in anticipo dopo la riabilitazione al crociato, rilevando Cooper Rush mentre i Falcons cercano il primo riscatto dopo lo 0-2 iniziale.',
        'Dall’altra parte Jordan Love guida i Packers sull’1-1 dopo la vittoria per 20-17 all’overtime contro i Jets. Green Bay celebra l’Alumni Weekend con oltre cinquanta leggende per gli anniversari di Super Bowl I e Super Bowl XXXI.',
      ],
    },
    pl: {
      title: 'Falcons u Packers: Penix wraca pod światła Lambeau na inaugurację 3. tygodnia',
      subtitle: 'Michael Penix Jr. wraca po zerwaniu więzadła. Jordan Love i Packers świętują Weekend Absolwentów. Prime Video w czwartek.',
      excerpt: '3. tydzień NFL rusza w czwartek w Lambeau Field, gdzie Green Bay Packers podejmują Atlanta Falcons. Michael Penix Jr. wraca do składu po rehabilitacji.',
      body: [
        '2. tydzień zakończył się w poniedziałek wieczorem w Los Angeles. Kalendarz NFL przechodzi prosto w 3. tydzień w czwartek na legendarnym Lambeau Field.',
        'NFL.com i Sports Illustrated podają, że Atlanta postawi w czwartek na powracającego Michaela Penixa Jr. Rozgrywający wraca wcześniej po zerwaniu więzadła, zastępując Coopera Rusha, podczas gdy Falcons walczą o pierwsze zwycięstwo po starcie 0-2.',
        'Naprzeciwko Jordan Love prowadzi Packers z bilansem 1-1 po zwycięstwie 20-17 po dogrywce z Jets. Klub celebruje Weekend Legend z udziałem ponad pięćdziesięciu dawnych gwiazd na rocznice Super Bowl I i Super Bowl XXXI.',
      ],
    },
    zh: {
      title: '猎鹰客战包装工：小佩尼克斯兰博球场复出点燃第3周揭幕战',
      subtitle: '小迈克尔·佩尼克斯十字韧带伤愈归队。乔丹·洛夫率队迎战校友周末。周四Prime Video独播。',
      excerpt: 'NFL第3周于周四晚在兰博球场打响，绿湾包装工主场迎战亚特兰大猎鹰。小迈克尔·佩尼克斯伤愈复出重返首发。',
      body: [
        '第2周周一夜赛在洛杉矶刚落下帷幕，NFL赛程紧接着在周四晚转战传奇球场兰博球场，开启第3周对决。',
        'NFL官网与《体育画报》报道，亚特兰大猎鹰周四晚迎回小迈克尔·佩尼克斯首发。这位年轻四分卫从膝盖十字韧带撕裂伤势中提前康复替换库珀·拉什，力争带领0胜2负的猎鹰斩获赛季首胜。',
        '主队方面，乔丹·洛夫在第2周加时20-17险胜喷气机后率包装工取得1胜1负。绿湾此役还将举办年度校友周末活动，邀请五十多位传奇名宿共同纪念第一届与第三十一届超级碗夺冠周年。',
      ],
    },
    ja: {
      title: 'ファルコンズ対パッカーズ：ペニックスがランボーのナイターで復帰、第3週開幕',
      subtitle: 'マイケル・ペニックスJr.が膝前十字靭帯断裂から復帰。ジョーダン・ラヴ率いるグリーンベイはOBウィークエンド。木曜Prime Video中継。',
      excerpt: 'NFL第3週が木曜夜にランボー・フィールドで開幕し、グリーンベイ・パッカーズがアトランタ・ファルコンズを迎え撃つ。ペニックスJr.が先発復帰。',
      body: [
        '第2週のマンデーナイトがロサンゼルスで終了した直後、NFLの舞台は木曜夜の名門ランボー・フィールドでの第3週開幕戦へと移る。',
        'NFL公式とスポーツ・イラストレイテッドによれば、ファルコンズは前十字靭帯断裂から復帰したペニックスJr.をクーパー・ラッシュに代えて先発起用する。開幕2連敗のアトランタは初勝利を期す。',
        '迎え撃つパッカーズは第2週にジェッツを延長20-17で下し1勝1敗。今節はスーパーボウル第1回および第31回の記念として50名以上のOBが集結する特別試合となる。',
      ],
    },
    ko: {
      title: '팰컨스 대 패커스: 페닉스, 램보 필드 조명 아래 3주차 개막전 복귀',
      subtitle: '마이클 페닉스 주니어 십자인대 부상 털고 복귀. 조던 러브와 패커스 동문 주간 개최. 목요일 프라임 비디오 생중계.',
      excerpt: 'NFL 3주차가 목요일 밤 램보 필드에서 개막하며 그린베이 패커스가 애틀랜타 팰컨스를 상대한다. 마이클 페닉스 주니어가 선발로 돌아온다.',
      body: [
        '로스앤젤레스에서 2주차 먼데이 나이트가 끝난 지 얼마 지나지 않아, NFL 일정은 목요일 밤 전설적인 램보 필드로 직행한다.',
        'NFL 공식과 스포츠 일러스트레이티드에 따르면 애틀랜타는 십자인대 부상에서 조기 복귀한 마이클 페닉스 주니어를 선발 쿼터백으로 내세운다. 2연패에 빠진 팰컨스는 첫 승 사냥에 나선다.',
        '그린베이는 2주차에 제츠를 연장전 20-17로 꺾고 1승 1패를 기록 중이다. 조던 러브가 이끄는 패커스는 슈퍼볼 1회 및 31회 우승 기념 동문 주간을 맞아 홈 팬들 앞에서 연승을 노린다.',
      ],
    },
    ar: {
      title: 'فالكونز في ضيافة باكرز: عودة بينيكس تحت أضواء لامبو لافتتاح الأسبوع الثالث',
      subtitle: 'مايكل بينيكس جونيور يعود بعد تعافيه من الرباط الصليبي. جوردان لوف وباكرز يحتفلون بأسبوع الأساطير. بث حصري على برايم فيديو الخميس.',
      excerpt: 'ينطلق الأسبوع الثالث مساء الخميس في لامبو فيلد حيث يستضيف غرين باي باكرز فريق أتلانتا فالكونز مع عودة بينيكس جونيور للتشكيلة الأساسية.',
      body: [
        'اختتم الأسبوع الثاني مساء الاثنين في لوس أنجلوس، ليتجه جدول دوري كرة القدم الأمريكية مباشرة نحو الأسبوع الثالث مساء الخميس على ملعب لامبو فيلد التاريخي.',
        'أكد موقع الدوري وسبورتس إليستريتد أن أتلانتا سيعيد قيادة الهجوم لمايكل بينيكس جونيور بعد تعافيه السريع من إصابة الرباط الصليبي ليحل محل كوبر راش سعيا وراء الفوز الأول بعد هزيمتين.',
        'في المقابل يقود جوردان لوف فريق باكرز بسجل فوز وهزيمة عقب الانتصار المثير 20-17 بالشوط الإضافي على جيتس، مع احتفال النادي بذكرى بطولتي السوبر بول بحضور أكثر من 50 أسطورة.',
      ],
    },
  },
  'fever-lynx-clark-96-77': {
    fr: {
      title: 'Fever 96-77 Lynx : Caitlin Clark guide Indiana vers un exploit face au leader',
      subtitle: 'Clark 27 points, 9 passes, 7 rebonds. Kelsey Mitchell 20. Indiana frappe un grand coup avant les playoffs.',
      excerpt: 'Indiana s’impose avec autorité 96-77 sur le parquet de Minnesota le 22 septembre. Caitlin Clark compile 27 points, neuf passes et sept rebonds dans une prestation de haut vol.',
      body: [
        'À quarante-huit heures de la fin de la saison régulière en WNBA, Indiana s’est mesuré à la référence de la ligue au Target Center. Le score final de 96-77 a fait retentir un sérieux avertissement pour les playoffs.',
        'WNBA.com et l’Associated Press soulignent la maestria de Caitlin Clark. La meneuse a compilé 27 points, neuf passes et sept rebonds, dictant le rythme face à la redoutable défense des Lynx. Kelsey Mitchell a ajouté 20 points à longue distance pour creuser l’écart après la pause.',
        'Minnesota avait déjà validé la première place du tableau avec 32 victoires et 10 défaites, mais ce revers à domicile montre des failles exploitables. Indiana passe à 27-15 et aborde les séries éliminatoires du 27 septembre en pleine confiance.',
      ],
    },
    es: {
      title: 'Fever 96-77 Lynx: Caitlin Clark comanda una exhibición de Indiana ante el líder',
      subtitle: 'Clark 27 puntos, 9 asistencias, 7 rebotes. Kelsey Mitchell 20. Indiana manda un aviso antes de los playoffs.',
      excerpt: 'Indiana superó 96-77 a las líderes Minnesota Lynx el 22 de septiembre. Caitlin Clark firmó 27 puntos, nueve asistencias y siete rebotes en una notable victoria a domicilio.',
      body: [
        'Con la temporada regular de la WNBA en sus últimas 48 horas, Indiana visitó el Target Center para medirse al mejor equipo de la liga. El 96-77 definitivo resonó con fuerza en toda la competición.',
        'WNBA.com y Associated Press destacan el recital de Caitlin Clark, autora de 27 puntos, nueve asistencias y siete rebotes controlando los tiempos del juego. Su compañera Kelsey Mitchell aportó 20 puntos desde el perímetro para romper el choque en el tercer cuarto.',
        'Minnesota ya tenía asegurado el puesto número uno con récord de 32-10, pero la derrota exhibió grietas ante su público. Indiana sube a 27-15 y se postula como un rival temible para los playoffs que arrancan el 27 de septiembre.',
      ],
    },
    de: {
      title: 'Fever 96:77 Lynx: Caitlin Clark führt Indiana zum Überraschungscoup beim Spitzenreiter',
      subtitle: 'Clark 27 Punkte, 9 Assists, 7 Rebounds. Kelsey Mitchell 20. Indiana setzt Ausrufezeichen vor den Playoffs.',
      excerpt: 'Indiana feiert am 22. September einen klaren 96:77-Auswärtssieg bei den topgesetzten Minnesota Lynx. Caitlin Clark glänzt mit 27 Punkten, neun Vorlagen und sieben Rebounds.',
      body: [
        'Wenige Tage vor Ende der WNBA-Hauptrunde trat Indiana im Target Center an, um sich mit dem Ligaprimus zu messen. Das deutliche 96:77 lieferte eine eindrucksvolle Machtdemonstration.',
        'WNBA.com und Associated Press berichten von einer herausragenden Leistung von Caitlin Clark mit 27 Punkten, neun Assists und sieben Rebounds gegen Minnesotas Elite-Defensive. Kelsey Mitchell steuerte 20 Zähler von außen bei, um den Vorsprung im dritten Viertel auszubauen.',
        'Minnesota stand mit einer 32-10-Bilanz bereits als Nummer eins der Setzliste fest, zeigte jedoch Schwächen vor heimischem Publikum. Indiana verbessert sich auf 27-15 vor dem Playoff-Start am 27. September.',
      ],
    },
    it: {
      title: 'Fever 96-77 Lynx: Caitlin Clark guida il trionfo di Indiana contro la capolista',
      subtitle: 'Clark 27 punti, 9 assist, 7 rimbalzi. Kelsey Mitchell 20. Indiana manda un segnale chiaro in vista dei playoff.',
      excerpt: 'Indiana espugna il campo delle Minnesota Lynx per 96-77 il 22 settembre. Caitlin Clark firma 27 punti, nove assist e sette rimbalzi in una prova superlativa.',
      body: [
        'A quarantotto ore dalla chiusura della stagione regolare WNBA, Indiana ha fatto visita al Target Center per testare le proprie ambizioni contro la prima della classe, firmando un netto 96-77.',
        'WNBA.com e Associated Press esaltano la regia di Caitlin Clark, capace di mettere a referto 27 punti, nove assist e sette rimbalzi. Kelsey Mitchell ha aggiunto 20 punti dal perimetro permettendo alle Fever di scappare via nel terzo quarto.',
        'Minnesota aveva già blindato il primo posto assoluto sul 32-10, ma il pesante ko casalingo lancia un monito prima dei playoff a otto squadre in partenza il 27 settembre, con Indiana salita sul 27-15.',
      ],
    },
    pl: {
      title: 'Fever 96-77 Lynx: Caitlin Clark prowadzi Indianę do zwycięstwa nad liderem',
      subtitle: 'Clark 27 punktów, 9 asyst, 7 zbiórek. Kelsey Mitchell 20. Indiana wysyła ostrzeżenie przed play-offami.',
      excerpt: 'Indiana pokonała 96-77 liderujące Minnesota Lynx 22 września. Caitlin Clark zanotowała 27 punktów, dziewięć asyst i siedem zbiórek w znakomitym występie wyjazdowym.',
      body: [
        'Na dwa dni przed końcem sezonu zasadniczego WNBA Indiana przyjechała do Target Center, by sprawdzić formę na tle najlepszej drużyny ligi, wygrywając bezdyskusyjnie 96-77.',
        'WNBA.com i Associated Press relacjonują koncert gry Caitlin Clark, która zdobyła 27 punktów, rozdała dziewięć asyst i zebrała siedem piłek. Kelsey Mitchell dołożyła 20 punktów z obwodu, budując bezpieczną przewagę w trzeciej kwarcie.',
        'Minnesota miała już zapewnione pierwsze miejsce z bilansem 32-10, lecz porażka na własnym parkiecie ujawniła luki. Indiana poprawiła bilans na 27-15 przed startem play-offów 27 września.',
      ],
    },
    zh: {
      title: '狂热96-77山猫：凯特琳·克拉克砍下27分率队大胜头号种子',
      subtitle: '克拉克27分9助攻7篮板。米切尔20分。印第安纳在季后赛前释放强劲信号。',
      excerpt: '印第安纳狂热于9月22日在客场以96-77大胜排名第一的明尼苏达山猫。凯特琳·克拉克贡献27分9次助攻与7个篮板。',
      body: [
        '在WNBA常规赛收官前夕，印第安纳狂热做客标靶中心检验自身实力，以96-77的悬殊比分展现了强大的统治力。',
        'WNBA官网与美联社报道，凯特琳·克拉克掌控全场节奏，独得27分9助攻7篮板，撕破山猫的顶级防线。后场搭档凯尔西·米切尔命中多记远投贡献20分，助狂热在第三节彻底拉开比分。',
        '尽管明尼苏达此前已凭借32胜10负锁定全联盟头号种子，但主场惨败敲响了警钟。狂热战绩提升至27胜15负，带着极佳势头迈向9月27日打响的季后赛。',
      ],
    },
    ja: {
      title: 'フィーバー96-77山猫：クラークが27得点、インディアナが首位を撃破',
      subtitle: 'クラーク27得点9アシスト7リバウンド。ミッチェル20得点。インディアナがプレーオフへ向け警告弾。',
      excerpt: 'インディアナ・フィーバーが9月22日に敵地で首位ミネソタ・リンクスを96-77で圧倒。ケイトリン・クラークが27得点9アシスト7リバウンドを記録。',
      body: [
        'WNBAレギュラーシーズン最終盤、インディアナは敵地ターゲット・センターに乗り込みリーグ最高勝率の相手に96-77の圧勝を飾った。',
        'WNBA公式とAP通信によれば、ケイトリン・クラークが27得点9アシスト7リバウンドと躍動し強固な相手守備を攻略。ケルシー・ミッチェルも外角から20得点を挙げ、第3クォーターで点差を決定づけた。リンクスは32勝10敗ですでに第1シードを確定させていたものの、ホームでの大敗は課題を残した。27勝15敗となったフィーバーは9月27日開幕のプレーオフへ弾みをつけた。',
      ],
    },
    ko: {
      title: '피버 96-77 링스: 케이틀린 클라크 27득점 지휘, 인디애나 1위 완파',
      subtitle: '클라크 27득점 9어시스트 7리바운드. 켈시 미첼 20득점. 플레이오프 앞두고 강력한 메시지 전달.',
      excerpt: '인디애나 피버가 9월 22일 미네소타 링스를 96-77로 완파했다. 케이틀린 클라크가 27득점 9어시스트 7리바운드로 맹활약했다.',
      body: [
        'WNBA 정규시즌 폐막을 앞두고 인디애나는 타깃 센터 원정에서 리그 최강팀을 96-77로 대파하며 플레이오프를 향한 기세를 올렸다.',
        'WNBA 공식과 AP 통신에 따르면 케이틀린 클라크는 27득점 9어시스트 7리바운드를 기록하며 상대 수비를 완벽하게 무너뜨렸다. 켈시 미첼 또한 외곽포 20득점으로 3쿼터 승기를 잡는 데 기여했다.',
        '미네소타는 32승 10패로 이미 전체 1번 시드를 확정했으나 홈에서 일격을 당했다. 27승 15패를 기록한 인디애나는 9월 27일 시작되는 8강 플레이오프를 앞두고 다크호스로 떠올랐다.',
      ],
    },
    ar: {
      title: 'فيفر 96-77 لينكس: كيتلين كلارك تقود إنديانا لفوز كاسح على المتصدر',
      subtitle: 'كلارك 27 نقطة و9 تمريرات و7 متابعات. كيلسي ميتشل 20 نقطة. إنذار قوي قبل انطلاق الأدوار الإقصائية.',
      excerpt: 'حققت إنديانا فوزا مستحقا 96-77 على أرض مينيسوتا لينكس متصدرة الترتيب في 22 أيلول/سبتمبر بتألق كيتلين كلارك التي سجلت 27 نقطة.',
      body: [
        'مع اقتراب نهاية الموسم المنتظم في دوري كرة السلة الأمريكي للسيدات، دخلت إنديانا صالة تارغت سنتر لاختبار جاهزيتها محققة فوزا لافتا 96-77.',
        'ذكر موقع الدوري وأسوشيتد برس أن كيتلين كلارك أحكمت قبضتها على المباراة مسجلة 27 نقطة مع 9 تمريرات حاسمة و7 متابعات، بينما أضافت كيلسي ميتشل 20 نقطة لفرض تفوق مريح.',
        'ورغم ضمان مينيسوتا المركز الأول في الترتيب بسجل 32 فوزا مقابل 10 هزائم، فإن خسارتها على أرضها تعطي دافعا كبيرا لإنديانا الصاعدة إلى 27 انتصارا قبل بدء البلاي أوف في 27 أيلول/سبتمبر.',
      ],
    },
  },
  'bayern-man-city-uwcl-2-2': {
    fr: {
      title: 'Bayern 2-2 Man City : l’égalisation de Wamser à la 86e illumine la C1 féminine',
      subtitle: 'Gwinn et un contre son camp de Casparij lancent le Bayern. Mead et Wamser arrachent le nul. Partage des points pour la 1re journée.',
      excerpt: 'Manchester City remonte deux buts pour arracher un nul 2-2 à Munich lors de la première journée de la Ligue des champions féminine. Carlotta Wamser égalise à la 86e minute.',
      body: [
        'La phase de ligue de la Ligue des champions féminine s’est ouverte en Bavière par un choc au sommet entre deux prétendants au sacre continental le 22 septembre.',
        'UEFA.com et The Guardian décrivent un match spectaculaire. Le Bayern a pris deux longueurs d’avance grâce à Giulia Gwinn à la 11e minute et un but contre son camp de Kerstin Casparij à la 28e, avant qu’Ena Mahmutovic ne stoppe un penalty de Khadija Shaw.',
        'City n’a pas baissé les bras : Beth Mead a réduit l’écart juste avant la mi-temps, puis Carlotta Wamser a converti l’égalisation à la 86e minute pour offrir un point précieux aux Mancuniennes.',
      ],
    },
    es: {
      title: 'Bayern 2-2 Man City: el gol de Wamser en el 86 culmina la remontada en Champions',
      subtitle: 'Gwinn y un autogol de Casparij adelantan al Bayern. Mead y Wamser sellan el empate. Reparto de puntos en la jornada 1.',
      excerpt: 'Manchester City remontó dos goles de desventaja para firmar un 2-2 en el feudo del Bayern Múnich en la jornada inaugural de la Champions League Femenina.',
      body: [
        'La fase de grupos de la Champions Femenina 2026-27 arrancó en Baviera con un duelo estelar entre dos de los clubes más potentes de Europa el 22 de septiembre.',
        'UEFA.com y The Guardian relatan un choque electrizante donde el Bayern se puso 2-0 arriba con tanto de Giulia Gwinn en el minuto 11 y autogol de Casparij en el 28. Además, Ena Mahmutovic detuvo un penalti a Khadija Shaw.',
        'Sin embargo, el City reaccionó con gol de Beth Mead antes del descanso y encontró la recompensa definitiva en el minuto 86 gracias a Carlotta Wamser para salvar un empate de enorme valor.',
      ],
    },
    de: {
      title: 'Bayern 2:2 Man City: Wamsers Treffer in der 86. Minute krönt UWCL-Spektakel',
      subtitle: 'Gwinn und ein Eigentor von Casparij bringen Bayern 2:0 in Führung. Mead und Wamser gleichen aus. Punkteteilung an Spieltag 1.',
      excerpt: 'Manchester City gleicht in München einen 0:2-Rückstand aus und holt zum Auftakt der UEFA Women’s Champions League ein 2:2 beim FC Bayern. Wamser trifft in der 86. Minute.',
      body: [
        'Die Ligaphase der UEFA Women’s Champions League begann am 22. September auf dem FC Bayern Campus mit einem hochklassigen Duell zweier Titelanwärter.',
        'UEFA.com und The Guardian schildern eine packende Partie: Giulia Gwinn traf in der 11. Minute zur Führung, ehe ein Eigentor von Kerstin Casparij das 2:0 brachte. Bayern-Torhüterin Ena Mahmutovic parierte zudem einen Strafstoß von Khadija Shaw.',
        'City gab sich nicht auf. Beth Mead verkürzte kurz vor der Pause, ehe die eingewechselte Carlotta Wamser in der 86. Minute den verdienten 2:2-Ausgleichstreffer erzielte.',
      ],
    },
    it: {
      title: 'Bayern 2-2 Man City: il pareggio all’86’ di Wamser sigilla la rimonta in Champions',
      subtitle: 'Gwinn e un autogol di Casparij lanciano il Bayern sul 2-0. Mead e Wamser firmano il pari. Punti divisi alla prima giornata.',
      excerpt: 'Il Manchester City recupera due reti e strappa un pareggio per 2-2 sul campo del Bayern Monaco nella prima giornata di Women’s Champions League.',
      body: [
        'La fase a gironi della UEFA Women’s Champions League è ripartita in Baviera il 22 settembre con una sfida stellare tra due corazzate continentali.',
        'UEFA.com e The Guardian descrivono una gara ricca di ribaltamenti. Il Bayern è volato sul 2-0 con Giulia Gwinn all’11’ e l’autorete sfortunata di Kerstin Casparij al 28’, mentre Ena Mahmutovic ha neutralizzato un rigore di Khadija Shaw.',
        'La reazione inglese si è concretizzata prima dell’intervallo con Beth Mead e si è completata all’86’ grazie al gol di Carlotta Wamser per un 2-2 dal sapore di vittoria.',
      ],
    },
    pl: {
      title: 'Bayern 2-2 Man City: gol Wamser w 86. minucie wieńczy remis w Lidze Mistrzyń',
      subtitle: 'Gwinn i samobój Casparij dają Bayernowi prowadzenie 2-0. Mead i Wamser wyrównują stan meczu. Podział punktów w 1. kolejce.',
      excerpt: 'Manchester City odrobił dwubramkową stratę i zremisował 2-2 z Bayernem Monachium w 1. kolejce Ligi Mistrzyń UEFA. Carlotta Wamser trafiła w 86. minucie.',
      body: [
        'Faza ligowa Ligi Mistrzyń UEFA rozpoczęła się w Bawarii 22 września od starcia wagi ciężkiej pomiędzy czołowymi klubami Europy.',
        'UEFA.com i The Guardian opisują emocjonujący pojedynek, w którym Bayern prowadził 2-0 po bramce Giulii Gwinn w 11. minucie i samobóju Casparij w 28. Bramkarka Ena Mahmutovic obroniła rzut karny egzekwowany przez Khadiję Shaw.',
        'City odpowiedziało tuż przed przerwą golem Beth Mead, a w 86. minucie rezerwowa Carlotta Wamser ustaliła wynik na 2-2, zapewniając cenne wyjazdowe punkty.',
      ],
    },
    zh: {
      title: '拜仁2-2曼城：瓦姆泽第86分钟绝平点燃女足欧冠揭幕战',
      subtitle: '格温与卡斯帕里乌龙球助拜仁两球领先。米德与瓦姆泽完成顽强逆转。首轮强强对话握手言和。',
      excerpt: '曼城在女足欧冠第一轮客场克服两球落后劣势，以2-2战平拜仁慕尼黑。替补登场的卡洛塔·瓦姆泽在第86分钟攻入绝平球。',
      body: [
        '2026-27赛季女足欧冠联赛阶段于9月22日在巴伐利亚拉开战幕，两支具备争冠实力的欧洲劲旅狭路相逢。',
        '欧足联官网与《卫报》报道，拜仁开局强势，朱莉娅·格温第11分钟首开纪录，卡斯帕里第28分钟自摆乌龙让主队两球领先。拜仁门将马赫穆托维奇还扑出了肖的点球。',
        '曼城展现出极强韧性，贝丝·米德半场前扳回一城，替补登场的瓦姆泽在第86分钟推射破门，将比分定格在2-2，在客场抢下宝贵的1分。',
      ],
    },
    ja: {
      title: 'バイエルン2-2マンC：86分のヴァムザー同点弾で女子欧州CL初戦ドロー',
      subtitle: 'グウィンとオウンゴールでバイエルンが2点先行。ミードとヴァムザーが反撃し勝ち点分け合う。',
      excerpt: 'マンチェスター・シティが女子チャンピオンズリーグ第1節で敵地バイエルン相手に2点差を追いつき2-2で引き分けた。ヴァムザーが86分に値千金の同点弾。',
      body: [
        'UEFA女子チャンピオンズリーグのリーグフェーズが9月22日にミュンヘンで幕を開け、欧州屈指の強豪同士による激闘が繰り広げられた。',
        'UEFA公式とガーディアン紙によれば、ジュリア・グウィンの11分弾と28分の相手オウンゴールでバイエルンが2点リード。さらにマフムトヴィッチがショーのPKを阻むなどホーム優勢で進んだ。',
        'しかしシティは前半終了直前にベス・ミードが1点を返すと、86分に途中出場のヴァムザーが同点ゴールを押し込み、敵地で価値ある2-2の引き分けに持ち込んだ。',
      ],
    },
    ko: {
      title: '바이에른 2-2 맨시티: 팜저의 86분 극적 동점골로 여자 챔스 1차전 무승부',
      subtitle: '그빈 선제골과 카스파리 자책골로 바이에른 2-0 리드. 미드와 팜저 연속골로 맨시티 원정 무승부.',
      excerpt: '맨체스터 시티가 9월 22일 여자 챔피언스리그 1차전 바이에른 뮌헨 원정에서 0-2 열세를 딛고 2-2 무승부를 거뒀다. 팜저가 86분 동점골을 터뜨렸다.',
      body: [
        '2026-27 UEFA 여자 챔피언스리그 리그 페이즈가 9월 22일 뮌헨에서 유럽 최정상 클럽 간의 격돌로 시작됐다.',
        'UEFA 공식과 가디언에 따르면 바이에른은 11분 율리아 그빈의 선제골과 28분 카스파리의 자책골로 2-0으로 앞서갔고 골키퍼 마흐무토비치가 쇼의 페널티킥까지 막아냈다.',
        '맨시티는 전반 종료 직전 베스 미드의 만회골로 추격한 뒤 86분 카를로타 팜저가 골망을 흔들며 적지에서 귀중한 승점 1점을 챙겼다.',
      ],
    },
    ar: {
      title: 'بايرن 2-2 مان سيتي: هدف فامزر بالدقيقة 86 يتوج إثارة دوري أبطال أوروبا للسيدات',
      subtitle: 'غفين وهدف عكسي لكاسباري يمنحان بايرن التقدم بهدفين. ميد وفامزر تقودان عودة السيتي وتقاسم النقاط بالجولة الأولى.',
      excerpt: 'عاد مانشستر سيتي من التأخر بهدفين ليحقق تعادلا مثيرا 2-2 مع بايرن ميونخ في الجولة الافتتاحية لدوري أبطال أوروبا للسيدات بفضل هدف فامزر بالدقيقة 86.',
      body: [
        'انطلقت مرحلة الدوري في دوري أبطال أوروبا للسيدات في بافاريا في 22 أيلول/سبتمبر بقمة كروية كبرى بين مرشحين للقب الأوروبي.',
        'أوضح موقع يويفا وصحيفة الغارديان تقدم بايرن بهدفين عن طريق جوليا غفين في الدقيقة 11 وهدف بالخطأ من كاسباري في الدقيقة 28، وتصدت الحارسة محمودوفيتش لركلة جزاء من خديجة شو.',
        'واصل سيتي الضغط وقلصت بيث ميد الفارق قبل نهاية الشوط الأول، قبل أن تسجل البديلة كارلوتا فامزر هدف التعادل في الدقيقة 86 ليحصد الفريق نقطة ثمينة من قلب ألمانيا.',
      ],
    },
  },
  'presidents-cup-day1-foursomes-2026': {
    fr: {
      title: 'Presidents Cup Jour 1 : les foursomes débutent sur le parcours n° 3 de Medinah',
      subtitle: 'Brandt Snedeker et Geoff Ogilvy fixent les duels du jour 1. Scottie Scheffler mène la défense américaine. Adam Scott pour sa 12e coupe.',
      excerpt: 'La 16e Presidents Cup s’ouvre jeudi au Medinah Country Club dans l’Illinois. Brandt Snedeker et Geoff Ogilvy mènent leurs équipes dans les foursomes matinaux sur le parcours n° 3 rénové.',
      body: [
        'Après le triomphe de JJ Spaun au BMW PGA Championship à Wentworth, le golf mondial se tourne vers Chicago pour l’un des plus grands rendez-vous par équipes. La 16e Presidents Cup a débuté jeudi matin à Medinah, testant 24 champions sur un parcours n° 3 entièrement repensé.',
        'Le PGA Tour et PresidentsCup.com rapportent que Brandt Snedeker et Geoff Ogilvy ont dévoilé leurs associations pour les foursomes. Le n° 1 mondial Scottie Scheffler fait équipe avec Russell Henley dans le match 1, tandis que Xander Schauffele et Patrick Cantlay affrontent Jason Day et Christiaan Bezuidenhout. Côté international, Adam Scott dispute sa 12e coupe aux côtés d’Hideki Matsuyama.',
        'Les foursomes du jeudi attribuent quatre points cruciaux. Les Internationaux parviendront-ils à briser l’hégémonie américaine invaincue depuis 1998, ou l’équipe américaine prendra-t-elle l’avantage d’entrée à Chicago ?',
      ],
    },
    es: {
      title: 'Presidents Cup Día 1: arrancan los foursomes en el campo n.º 3 de Medinah',
      subtitle: 'Brandt Snedeker y Geoff Ogilvy definen los duelos del día 1. Scottie Scheffler lidera la defensa de EE. UU. Adam Scott en su 12.ª copa.',
      excerpt: 'La 16.ª Presidents Cup arranca este jueves en el Medinah Country Club de Illinois. Brandt Snedeker y Geoff Ogilvy dirigen a sus escuadras en los foursomes matutinos sobre el renovado recorrido n.º 3.',
      body: [
        'Tras el título de JJ Spaun en Wentworth, el calendario internacional mira a Chicago para uno de los mayores espectáculos por equipos. La 16.ª Presidents Cup comenzó este jueves en Medinah Country Club, midiendo a 24 de los mejores golfistas del planeta en un rediseñado campo n.º 3.',
        'PGA Tour y PresidentsCup.com informan que Brandt Snedeker y Geoff Ogilvy anunciaron sus emparejamientos de foursomes. El número uno mundial Scottie Scheffler forma dupla con Russell Henley en el partido 1, mientras Xander Schauffele y Patrick Cantlay se miden a Jason Day y Christiaan Bezuidenhout. Adam Scott hace historia jugando su 12.ª Presidents Cup consecutiva junto a Hideki Matsuyama.',
        'Los foursomes del jueves entregan cuatro puntos vitales en la carrera hacia los 15,5. El equipo Internacional busca quebrar una racha estadounidense que se extiende desde 1998 en Melbourne.',
      ],
    },
    de: {
      title: 'Presidents Cup Tag 1: Medinah Kurs Nr. 3 eröffnet mit hochkarätigen Foursomes',
      subtitle: 'Brandt Snedeker und Geoff Ogilvy stellen Spielpaarungen für Tag 1 auf. Scottie Scheffler führt US-Titelverteidigung an. Adam Scott beim 12. Cup.',
      excerpt: 'Der 16. Presidents Cup beginnt am Donnerstag im Medinah Country Club in Illinois. Brandt Snedeker und Geoff Ogilvy führen ihre Teams in die morgendlichen Foursomes auf dem neugestalteten Kurs Nr. 3.',
      body: [
        'Nach dem Triumph von JJ Spaun bei der BMW PGA Championship in Wentworth schaut die Golfwelt nach Chicago. Der 16. Presidents Cup begann am Donnerstagmorgen im Medinah Country Club und fordert 24 Weltklasse-Golfer auf einem komplett renovierten Kurs Nr. 3.',
        'PGA Tour und PresidentsCup.com berichten, dass Brandt Snedeker und Geoff Ogilvy ihre Foursomes-Paarungen bekanntgaben. Die Nummer 1 der Welt, Scottie Scheffler, tritt im Match 1 mit Russell Henley an, während Xander Schauffele und Patrick Cantlay auf Jason Day und Christiaan Bezuidenhout treffen. Adam Scott bestreitet seinen 12. Presidents Cup an der Seite von Hideki Matsuyama.',
        'Am Donnerstag stehen vier wichtige Punkte auf dem Spiel. Schafft das internationale Team den ersten Sieg seit 1998, oder dominieren die US-Amerikaner von Beginn an?',
      ],
    },
    it: {
      title: 'Presidents Cup Giorno 1: partono i foursomes sul percorso n. 3 di Medinah',
      subtitle: 'Brandt Snedeker e Geoff Ogilvy schierano i match del giorno 1. Scottie Scheffler guida gli USA. Adam Scott alla 12ª presenza.',
      excerpt: 'La 16ª Presidents Cup comincia giovedì al Medinah Country Club in Illinois. Brandt Snedeker e Geoff Ogilvy guidano le rispettive squadre nei foursomes mattutini sul ridisegnato Course No. 3.',
      body: [
        'Dopo la vittoria di JJ Spaun al BMW PGA Championship a Wentworth, il golf mondiale si sposta a Chicago per la 16ª Presidents Cup al Medinah Country Club sul nuovo Course No. 3.',
        'PGA Tour e PresidentsCup.com riportano le scelte dei capitani per la prima sessione. Il numero 1 al mondo Scottie Scheffler fa coppia con Russell Henley nel Match 1, mentre Schauffele e Cantlay affrontano Day e Bezuidenhout. Adam Scott gioca la sua dodicesima Presidents Cup insieme a Hideki Matsuyama.',
        'I foursomes del giovedì mettono in palio quattro punti chiave nella corsa a 15,5 punti. Gli internazionali cercano la prima vittoria dal 1998 contro una solida squadra statunitense.',
      ],
    },
    pl: {
      title: 'Puchar Prezydentów Dzień 1: Medinah Course No. 3 otwiera zmagania czwórkami',
      subtitle: 'Brandt Snedeker i Geoff Ogilvy ogłosili składy na dzień 1. Scottie Scheffler liderem obrońców tytułu. Adam Scott w 12. występie.',
      excerpt: '16. Puchar Prezydentów rozpoczyna się w czwartek w Medinah Country Club w stanie Illinois. Kapitanowie Snedeker i Ogilvy wystawiają swoje pary na przebudowane pole Course No. 3.',
      body: [
        'Po zwycięstwie JJ Spauna w Wentworth uwaga golfowego świata przenosi się do Chicago. 16. edycja Pucharu Prezydentów rozpoczęła się w czwartek rano w Medinah Country Club.',
        'PGA Tour i PresidentsCup.com podały pary na poranne mecze foursomes. Lider rankingu światowego Scottie Scheffler gra z Russellem Henleyem, natomiast Xander Schauffele i Patrick Cantlay mierzą się z Jasonem Dayem i Christiaanem Bezuidenhoutem. Legendarny Adam Scott występuje u boku Hidekiego Matsuyamy.',
        'Czwartkowa runda foursomes to cztery punkty do zdobycia na drodze do wymaganych 15,5 punktu. Drużyna Międzynarodowa poluje na pierwszy triumf od 1998 roku.',
      ],
    },
    zh: {
      title: '2026总统杯首日：梅迪纳3号球场打响高水准四人两球赛',
      subtitle: '斯内德克与奥格维公布首日对阵。世界第一舍夫勒领衔卫冕，斯科特第12次出战创纪录。',
      excerpt: '第16届总统杯于周四在伊利诺伊州梅迪纳乡村俱乐部开打。队长布兰特·斯内德克与杰夫·奥格维带领队员在全新设计的3号球场展开首日上午的四人两球赛角逐。',
      body: [
        '继JJ·斯鲍恩在温特沃斯捧起宝马PGA锦标赛奖杯后，国际高尔夫赛程迅速聚焦芝加哥。第16届总统杯于周四上午在梅迪纳乡村俱乐部开幕，24位世界顶尖选手在全面改造的3号球场展开对决。',
        '美巡赛与总统杯官方消息显示，队长斯内德克与奥格维在周三晚宴后公布了首日四人两球赛对阵。世界第一斯科蒂·舍夫勒搭档罗素·亨利在第1场出击，赞德·谢奥菲勒与帕特里克·坎特利对阵简森·戴伊和贝苏伊登霍特。国际队传奇亚当·斯科特第12次出战，与松山英树联手。',
        '周四四人两球赛将产生关键的4分。国际队全力争取自1998年以来的首场胜利，而美国队力图在芝加哥早早确立领先优势。',
      ],
    },
    ja: {
      title: 'プレジデンツカップ初日：メディナ3番コースでフォーサム戦が開幕',
      subtitle: 'スネデカーとオギルビーが初日のペアを発表。世界ランク1位シェフラーが連覇を牽引、スコットは12回目の出場。',
      excerpt: '第16回プレジデンツカップが24日木曜日、米イリノイ州のメディナCCで開幕。スネデカー主将とオギルビー主将が率いる両軍が改修後の3番コースで午前フォーサム戦に臨む。',
      body: [
        'ウェントワースでのJJ・スポーン優勝に続き、ゴルフ界の視線はシカゴへ。第16回プレジデンツカップが24日木曜午前にメディナCCで幕を開け、全面改修された難関3番コースに24名の精鋭が集結した。',
        'PGAツアーおよび大会公式によると、スネデカー主将とオギルビー主将が初日フォーサムのペアを発表。世界1位のスコッティ・シェフラーはラッセル・ヘンリーと組み第1マッチに登場、ショーフリーとカントレーはデイ＆ベザイデンホウトと激突する。世界選抜のアダム・スコットは松山英樹とタッグを組む。',
        '木曜のフォーサム4マッチで序盤の主導権争いが展開される。世界選抜が1998年以来となる勝利を掴むか、米国選抜が序盤から圧倒するか注目が集まる。',
      ],
    },
    ko: {
      title: '프레지던츠컵 1일차: 메디나 3번 코스서 박진감 넘치는 포섬 매치 개막',
      subtitle: '스네데커와 오길비 1일차 대진 확정. 세계 1위 셰플러 미국 수성 선봉, 애덤 스콧 12회 출전 금자탑.',
      excerpt: '제16회 프레지던츠컵이 9월 24일 목요일 미국 일리노이주 메디나 컨트리클럽에서 개막했다. 브랜트 스네데커와 제프 오길비 단장이 새롭게 단장된 3번 코스 포섬 경기에 나선다.',
      body: [
        'JJ 스폰이 웬트워스에서 BMW PGA 챔피언십 정상에 오른 뒤 골프 팬들의 시선은 시카고로 향했다. 제16회 프레지던츠컵이 24일 오전 메디나 컨트리클럽에서 개막해 24명의 세계적 스타들이 재설계된 3번 코스에서 격돌한다.',
        'PGA 투어와 대회 공식 발표에 따르면 브랜트 스네데커와 제프 오길비 단장은 1일차 포섬 대진을 확정했다. 세계 1위 스코티 셰플러는 러셀 헨리와 1경기에 나서고, 쇼플리와 캔틀리는 제이슨 데이 및 베자위덴하우트와 맞붙는다. 애덤 스콧은 마쓰야마 히데키와 호흡을 맞춘다.',
        '목요일 포섬에 걸린 승점은 4점이다. 인터내셔널 팀이 1998년 이후 28년 만의 승리를 노리는 가운데 미국 팀이 홈그라운드 우위를 굳힐지 주목된다.',
      ],
    },
    ar: {
      title: 'كأس الرؤساء اليوم الأول: انطلاق مواجهات الفورسوم على ملعب مادينا رقم 3',
      subtitle: 'سنديكر وأوجيلفي يحددان مواجهات اليوم الأول. سكوتي شيفلر يقود دفاع أمريكا وآدم سكوت يخوض مشاركته الـ12.',
      excerpt: 'انطلقت النسخة الـ16 من كأس الرؤساء يوم الخميس في نادي مادينا الريفي في إلينوي، حيث يقود براندت سنديكر وجيف أوجيلفي فرقهما في مواجهات الفورسوم الصباحية.',
      body: [
        'بعد تتويج جيه جيه سباون ببطولة بي إم دبليو في وينتورث، تتجه أنظار الجولف العالمي إلى شيكاغو. بدأت النسخة الـ16 من كأس الرؤساء صباح الخميس في مادينا بمشاركة 24 من نخبة لاعبي العالم.',
        'أفادت جولة بي جي إيه والموقع الرسمي للبطولة بإعلان تشكيلات الفورسوم لليوم الأول. يلعب المصنف الأول سكوتي شيفلر مع راسل هينلي في المباراة الأولى، بينما يواجه زاندر شوفيلي وباتريك كانتلي الثنائي جيسون داي وبيزويدنهوت. ويلعب آدم سكوت بجانب هيديكي ماتسوياما.',
        'تمنح مواجهات الفورسوم يوم الخميس 4 نقاط حاسمة في السباق نحو 15.5 نقطة، حيث يسعى الفريق الدولي لكسر هيمنة أمريكا المستمرة منذ عام 1998.',
      ],
    },
  },
  'baku-gp-thursday-practice-2026': {
    fr: {
      title: 'Essais du jeudi à Bakou : Antonelli et Russell emmènent Mercedes sur le circuit urbain',
      subtitle: 'Début exceptionnel le jeudi au circuit urbain de Bakou. Mercedes défend ses 503 points au championnat constructeurs. Qualifications vendredi, course samedi.',
      excerpt: 'La Formule 1 prend la piste à Bakou pour les séances d’essais du jeudi. Kimi Antonelli et George Russell mènent le peloton Mercedes avant les qualifications de vendredi et le Grand Prix de samedi.',
      body: [
        'La Formule 1 avance son calendrier d’une journée pour le Grand Prix d’Azerbaïdjan 2026, courant du jeudi au samedi afin de respecter la journée du souvenir du dimanche 27 septembre. Le tracé de 6,003 km allie une ligne droite de 2,2 km et le passage du château le plus étroit du calendrier.',
        'Formula1.com et Sky Sports confirment que les EL1 et EL2 ont débuté jeudi sous la chaleur des rives de la Caspienne. Mercedes arrive forte de sa domination après la victoire de Kimi Antonelli à Madrid. Le jeune prodige mène le classement pilotes avec 292 points, devant Russell (211 points).',
        'L’action s’accélère dès vendredi avec les EL3 et les qualifications, qui fixeront la grille du Grand Prix de 51 tours programmé samedi à midi heure de Londres.',
      ],
    },
    es: {
      title: 'Entrenamientos del jueves en Bakú: Antonelli y Russell ponen a prueba a Mercedes en el trazado urbano',
      subtitle: 'Raro inicio en jueves en el circuito de Bakú. Mercedes defiende su ventaja de 503 puntos en constructores. Clasificación el viernes, carrera el sábado.',
      excerpt: 'La Fórmula 1 rueda en Bakú en las prácticas libres del jueves. Kimi Antonelli y George Russell comandan a Mercedes antes de la clasificación del viernes y el Gran Premio del sábado.',
      body: [
        'La Fórmula 1 adelanta su fin de semana un día en el Gran Premio de Azerbaiyán 2026, disputándose de jueves a sábado con motivo del Día del Recuerdo del domingo 27 de septiembre. El circuito de 6,003 km combina una recta de 2,2 km con el paso del castillo más estrecho del automovilismo.',
        'Formula1.com y Sky Sports informan del inicio de los entrenamientos libres 1 y 2 a orillas del mar Caspio. Mercedes lidera el certamen de constructores con 503 puntos, mientras Kimi Antonelli encabeza el mundial de pilotos con 292 puntos frente a los 211 de George Russell.',
        'El viernes albergará los Libres 3 y la sesión de clasificación, estableciendo la parrilla para el Gran Premio del sábado a 51 vueltas.',
      ],
    },
    de: {
      title: 'Donnerstagstraining in Baku: Antonelli und Russell testen Mercedes auf dem Straßenkurs',
      subtitle: 'Ungewöhnlicher Donnerstag-Start am Baku City Circuit. Mercedes verteidigt 503 Punkte in der Konstrukteurs-WM. Qualifying am Freitag, Rennen am Samstag.',
      excerpt: 'Die Formel 1 startet am Donnerstag in Baku in die freien Trainings. Antonelli und Russell führen das Mercedes-Feld vor dem Freitag-Qualifying und dem Grand Prix am Samstag an.',
      body: [
        'Die Formel 1 rückt ihren Ablauf um einen Tag vor: Der Große Preis von Aserbaidschan findet wegen des nationalen Gedenktags am Sonntag von Donnerstag bis Samstag statt. Der 6,003 Kilometer lange Kurs verbindet eine 2,2 km lange Vollgasgerade mit der extrem engen Burgpassage.',
        'Formula1.com und Sky Sports bestätigen den Beginn von FP1 und FP2 am Kaspischen Meer. Mercedes tritt als WM-Führender mit 503 Konstrukteurspunkten an. Rookie Kimi Antonelli führt die Fahrerwertung mit 292 Punkten vor George Russell mit 211 Punkten an.',
        'Am Freitag folgen FP3 und das Qualifying, bevor am Samstag der 51 Runden lange Grand Prix um 12:00 Uhr britischer Zeit gestartet wird.',
      ],
    },
    it: {
      title: 'Prove del giovedì a Baku: Antonelli e Russell portano la Mercedes sul tracciato cittadino',
      subtitle: 'Inedita partenza di giovedì al Baku City Circuit. Mercedes difende 503 punti costruttori. Qualifiche venerdì, gara sabato.',
      excerpt: 'La Formula 1 scende in pista a Baku per le prove libere del giovedì. I compagni di squadra Antonelli e Russell aprono i lavori in vista di qualifiche e gara.',
      body: [
        'La Formula 1 anticipa il weekend di un giorno per il Gran Premio d’Azerbaigian 2026, in programma da giovedì a sabato per rispettare la Giornata del Ricordo del 27 settembre. Il tracciato cittadino di 6,003 km presenta un rettilineo di 2,2 km e la sezione del castello più stretta del mondiale.',
        'Formula1.com e Sky Sports confermano l’avvio di FP1 e FP2. La Mercedes si presenta al comando dei costruttori con 503 punti. Kimi Antonelli guida il mondiale piloti a quota 292 punti, seguito da Russell a 211.',
        'Venerdì sarà tempo di FP3 e qualifiche, per definire lo schieramento del Gran Premio di sabato articolato su 51 giri.',
      ],
    },
    pl: {
      title: 'Czwartkowe treningi w Baku: Antonelli i Russell testują Mercedesa na torze ulicznym',
      subtitle: 'Nietypowy czwartkowy start w Baku City Circuit. Mercedes broni 503 punktów wśród konstruktorów. Kwalifikacje w piątek, wyścig w sobotę.',
      excerpt: 'Formuła 1 rozpoczęła czwartkowe sesje treningowe w Baku. Duet Mercedesa Antonelli i Russell sprawdza tempo przed piątkowymi kwalifikacjami i sobotnim wyścigiem.',
      body: [
        'Formuła 1 przesunęła weekend wyścigowy o jeden dzień z racji Dnia Pamięci w Azerbejdżanie przypadającego w niedzielę. Tor Baku City Circuit o długości 6,003 km łączy 2,2-kilometrową prostą z ciasną sekcją wokół zamku.',
        'Formula1.com i Sky Sports donoszą o rozpoczęciu FP1 i FP2. Mercedes dominuje w klasyfikacji konstruktorów z dorobkiem 503 punktów. Debiutant Kimi Antonelli prowadzi wśród kierowców z 292 punktami przed George’em Russellem (211 punktów).',
        'W piątek odbędą się FP3 i kwalifikacje, które ustalą pola startowe do sobotniego Grand Prix na dystansie 51 okrążeń.',
      ],
    },
    zh: {
      title: '巴库周四练习赛：安东内利与拉塞尔携奔驰出战街道赛道',
      subtitle: '巴库城市赛道罕见周四开跑。梅赛德斯捍卫503分车队榜首。周五排位赛，周六正赛。',
      excerpt: 'F1在巴库城市赛道打响周四自由练习赛。梅赛德斯车手安东内利与拉塞尔在周五排位赛与周六正赛前领跑备战。',
      body: [
        '为避开9月27日周日的阿塞拜疆全国纪念日，2026年阿塞拜疆大奖赛提前至周四至周六举行。全长6.003公里的巴库城市赛道包含长达2.2公里的超长全油门直道以及极为狭窄的城堡赛段。',
        'F1官网与天空体育报道，周四一练与二练在里海之滨的温暖天气中展开。梅赛德斯携503分领跑车队积分榜。超级新星基米·安东内利以292分在车手榜领跑，队友拉塞尔积211分位居第二。',
        '赛程节奏紧凑，周五将进行三练与排位赛，为周六全长51圈的正赛确定发车顺位。',
      ],
    },
    ja: {
      title: 'バクー木曜フリー走行：アントネッリとラッセルが市街地コースでメルセデスを駆る',
      subtitle: 'バクー市街地コースで異例の木曜開幕。メルセデスは503点の製造者首位を守る。金曜予選、土曜決勝。',
      excerpt: 'F1アゼルバイジャンGPの木曜フリー走行がバクー市街地コースで始まった。アントネッリとラッセルが金曜の予選、土曜の決勝に向けてマシンの感触を確かめる。',
      body: [
        '9月27日日曜の追悼記念日を考慮し、2026年アゼルバイジャンGPは木曜から土曜の日程で開催。全長6.003キロのコースは2.2キロの超高速ストレートと城壁沿いの極狭区間が交錯する。',
        'F1公式とSky Sportsによると、FP1とFP2が木曜にスタート。マドリードで歴史的勝利を挙げたメルセデスは製造者部門で503点を獲得。新星キミ・アントネッリが292点でドライバーズ首位、ラッセルが211点で追う。',
        '金曜にはFP3と予選が行われ、土曜の51周の決勝に向けたスターティンググリッドが決まる。',
      ],
    },
    ko: {
      title: '바쿠 목요 연습 세션: 안토넬리와 러셀, 시가지 서킷서 메르세데스 테스트',
      subtitle: '바쿠 시티 서킷의 이례적인 목요일 출발. 메르세데스 503점 제조사 선두 방어. 금요일 예선, 토요일 결선.',
      excerpt: 'F1 아제르바이잔 그랑프리가 목요일 바쿠 시티 서킷에서 공식 연습 세션을 시작했다. 메르세데스의 안토넬리와 러셀이 금요일 예선과 토요일 결선을 앞두고 속도를 끌어올린다.',
      body: [
        '일요일 전몰자 추모의 날을 배려해 2026 아제르바이잔 GP는 목요일부터 토요일까지 치러진다. 6.003km의 바쿠 서킷은 2.2km의 고속 직선 구간과 올드타운의 좁은 성벽 코너로 악명 높다.',
        'F1 공식과 스카이 스포츠에 따르면 목요일 FP1과 FP2가 카스피해 연안에서 진행됐다. 메르세데스는 컨스트럭터 503점으로 선두를 질주 중이며, 키미 안토넬리는 292점으로 조지 러셀(211점)을 앞서고 있다.',
        '금요일에는 FP3과 예선이 열려 토요일 51랩 결선 레이스의 그리드가 최종 확정된다.',
      ],
    },
    ar: {
      title: 'تجارب باكو يوم الخميس: أنتونيللي وروسيل يقودان مرسيدس في حلبة الشوارع',
      subtitle: 'انطلاق استثنائي يوم الخميس في حلبة باكو. مرسيدس تدافع عن 503 نقاط في بطولة الصانعين. التصفيات الجمعة والسباق السبت.',
      excerpt: 'انطلقت تجارب سباق جائزة أذربيجان الكبرى لسباقات فورمولا 1 يوم الخميس في حلبة باكو، حيث يختبر ثنائي مرسيدس أنتونيللي وروسيل مسار الحلبة.',
      body: [
        'تم تقديم جدول سباق أذربيجان 2026 يوما واحدا ليقام من الخميس إلى السبت احتراما ليوم الذكرى الوطني الأحد. يبلغ طول حلبة باكو 6.003 كم مع خط مستقيم بطول 2.2 كم ومقطع قلعة شديد الضيق.',
        'أكد موقع فورمولا 1 وسكاي سبورتس انطلاق حصتي التجارب الأولى والثانية يوم الخميس. تتصدر مرسيدس بطولة الصانعين برصيد 503 نقاط، بينما يتصدر كيمي أنتونيللي بطولة السائقين برصيد 292 نقطة متقدما على جورج روسيل برصيد 211 نقطة.',
        'تتواصل الإثارة يوم الجمعة مع حصة التجارب الثالثة والتصفيات الرسمية لتحديد شبكة انطلاق السباق المكون من 51 لفة يوم السبت.',
      ],
    },
  },
  'laver-cup-london-eve-2026': {
    fr: {
      title: 'Veille de Laver Cup à Londres : Noah et Agassi dévoilent les duels du vendredi à l’O2',
      subtitle: 'L’équipe Europe et l’équipe Monde finalisent l’ordre des matches du jour 1. Alcaraz et Zverev mènent l’Europe. Fritz et De Minaur mènent le Monde.',
      excerpt: 'À la veille de la Laver Cup 2026 à l’O2 Arena de Londres, les capitaines Yannick Noah et Andre Agassi ont dévoilé les affiches de la journée d’ouverture du vendredi.',
      body: [
        'Après les sacres d’Alexander Zverev et d’Elena Rybakina à New York, le tennis mondial prend ses quartiers sur le court noir de l’O2 à Londres. La 9e édition de la Laver Cup marque la passation de relais entre les capitaines légendaires : Yannick Noah et Andre Agassi prennent les rênes.',
        'Les organisateurs et Sky Sports ont confirmé les conférences de presse et les sélections d’équipes jeudi. L’Europe compte sur Zverev, Carlos Alcaraz, Casper Ruud, Flavio Cobolli, Jakub Mensik et Rafael Jodar. L’équipe Monde d’Agassi s’appuie sur Taylor Fritz, Alex de Minaur, Brandon Nakashima, Learner Tien, Alexander Bublik et Francisco Cerundolo.',
        'Les matches du vendredi rapportent un point chacun, le samedi deux points et le dimanche trois points. La première formation à 13 points soulève le trophée.',
      ],
    },
    es: {
      title: 'Víspera de la Laver Cup en Londres: Noah y Agassi revelan los duelos del viernes en el O2',
      subtitle: 'El Equipo Europa y el Equipo Resto del Mundo definen el orden de juego del día 1. Alcaraz y Zverev lideran Europa. Fritz y De Minaur comandan el Mundo.',
      excerpt: 'En la víspera de la Laver Cup 2026 en el O2 de Londres, los capitanes Yannick Noah y Andre Agassi anunciaron los cruces de la jornada inaugural del viernes.',
      body: [
        'Tras los títulos de Zverev y Rybakina en Flushing Meadows, el tenis aterriza en la emblemática pista negra del O2 de Londres. La 9.ª Laver Cup presenta una nueva era con Yannick Noah y Andre Agassi tomando el mando como capitanes.',
        'Sky Sports y la web del torneo confirmaron los anuncios oficiales de este jueves. Europa cuenta con Zverev, Carlos Alcaraz, Casper Ruud, Flavio Cobolli, Jakub Mensik y Rafael Jodar. El Equipo Mundo de Agassi alinea a Taylor Fritz, Alex de Minaur, Brandon Nakashima, Learner Tien, Alexander Bublik y Francisco Cerundolo.',
        'El sistema de puntuación otorga un punto por victoria el viernes, dos el sábado y tres el domingo. El primer equipo en llegar a 13 puntos se corona campeón.',
      ],
    },
    de: {
      title: 'Laver-Cup-Auftakt in London: Noah und Agassi geben Eröffnungsmatches für Freitag bekannt',
      subtitle: 'Team Europa und Team Welt finalisieren Spielplan für Tag 1. Alcaraz und Zverev führen Europa an. Fritz und De Minaur führen Team Welt.',
      excerpt: 'Am Vorabend des Laver Cup 2026 in der Londoner O2 Arena enthüllten die Kapitäne Yannick Noah und Andre Agassi die Duelle für den Eröffnungstag am Freitag.',
      body: [
        'Nach den US-Open-Triumphen von Zverev und Rybakina wechselt die Tenniselite auf den schwarzen Hartplatz der O2 Arena in London. Die neunte Auflage des Laver Cup markiert einen historischen Wechsel auf der Trainerbank: Yannick Noah und Andre Agassi übernehmen das Kommando.',
        'Sky Sports und die Laver-Cup-Leitung bestätigten die Aufgebote am Donnerstag. Team Europa setzt auf Zverev, Carlos Alcaraz, Casper Ruud, Flavio Cobolli, Jakub Mensik und Rafael Jodar. Agassis Weltauswahl tritt mit Taylor Fritz, Alex de Minaur, Brandon Nakashima, Learner Tien, Alexander Bublik und Francisco Cerundolo an.',
        'Jeder Sieg am Freitag bringt einen Punkt, am Samstag zwei und am Sonntag drei. Das erste Team mit 13 Punkten gewinnt die Trophäe.',
      ],
    },
    it: {
      title: 'Vigilia di Laver Cup a Londra: Noah e Agassi svelano i match di venerdì all’O2',
      subtitle: 'Team Europe e Team World stabiliscono l’ordine di gioco del day 1. Alcaraz e Zverev guidano l’Europa. Fritz e De Minaur guidano il Resto del Mondo.',
      excerpt: 'Alla vigilia della Laver Cup 2026 all’O2 di Londra, i capitani Yannick Noah e Andre Agassi hanno presentato le partite della giornata inaugurale di venerdì.',
      body: [
        'Dopo i trionfi newyorkesi di Alexander Zverev ed Elena Rybakina, il circuito approda sul campo nero dell’O2 Arena di Londra. La nona edizione della Laver Cup segna il debutto in panchina di Yannick Noah e Andre Agassi.',
        'Sky Sports e l’organizzazione hanno reso note le formazioni nella giornata di giovedì. L’Europa schiera Zverev, Carlos Alcaraz, Casper Ruud, Flavio Cobolli, Jakub Mensik e Rafael Jodar. Il Team World replica con Taylor Fritz, Alex de Minaur, Brandon Nakashima, Learner Tien, Alexander Bublik e Francisco Cerundolo.',
        'Venerdì ogni vittoria vale un punto, sabato due punti e domenica tre punti. La prima squadra a raggiungere quota 13 conquista il trofeo.',
      ],
    },
    pl: {
      title: 'Przedednie Laver Cup w Londynie: Noah i Agassi ogłaszają piątkowe pojedynki w The O2',
      subtitle: 'Drużyna Europy i Drużyna Świata zamykają plan gier na 1. dzień. Alcaraz i Zverev liderami Europy. Fritz i De Minaur na czele Świata.',
      excerpt: 'W przeddzień Laver Cup 2026 w The O2 w Londynie kapitanowie Yannick Noah i Andre Agassi ogłosili zestaw par na piątkowe otwarcie turnieju.',
      body: [
        'Po sukcesach Zvereva i Rybakiny na US Open uwaga przenosi się na charakterystyczny czarny kort w londyńskiej The O2. 9. edycja Pucharu Lavera to nowa era kapitanów: stery objęli Yannick Noah i Andre Agassi.',
        'Sky Sports i organizatorzy potwierdzili składy w czwartek. Drużynę Europy reprezentują Zverev, Carlos Alcaraz, Casper Ruud, Flavio Cobolli, Jakub Mensik oraz Rafael Jodar. W Drużynie Świata grają Taylor Fritz, Alex de Minaur, Brandon Nakashima, Learner Tien, Alexander Bublik i Francisco Cerundolo.',
        'W piątek za każde zwycięstwo przyznawany jest jeden punkt, w sobotę dwa, a w niedzielę trzy. Do zdobycia pucharu potrzeba 13 punktów.',
      ],
    },
    zh: {
      title: '拉沃尔杯伦敦前瞻：诺阿与阿加西揭晓周五O2揭幕对决',
      subtitle: '欧洲队与世界队敲定首日出场名单。阿尔卡拉斯与兹维列夫领衔欧洲，弗里茨与德米纳尔率世界队应战。',
      excerpt: '在2026年拉沃尔杯于伦敦O2体育馆揭幕前夕，两位新任队长雅尼克·诺阿与安德烈·阿加西公布了周五开幕日的比赛对阵。',
      body: [
        '随着兹维列夫与莱巴金娜在美网捧杯，世界网坛迅速移师伦敦O2体育馆的黑色球场。第9届拉沃尔杯迎来了历史性交接：传奇队长博格与麦肯罗功成身退，诺阿与阿加西正式执掌帅印。',
        '天空体育与拉沃尔杯官方周四举行了媒体日发布会。欧洲队阵容包括美网冠军兹维列夫、阿尔卡拉斯、鲁德、科博利、门希克以及新星霍达尔。阿加西的世界队则由弗里茨、德米纳尔、中岛布兰登、田恩、布勃利克和塞伦多洛组成。',
        '比赛积分采取递增制：周五每胜1分，周六每胜2分，周日每胜3分。率先获得13分的队伍将捧起拉沃尔杯。周五揭幕战于英国时间下午1点打响。',
      ],
    },
    ja: {
      title: 'レーバーカップ前夜・ロンドン：ノアとアガシがO2での金曜開幕カードを発表',
      subtitle: 'チーム・ヨーロッパとチーム・ワールドが初日の対戦順を決定。アルカラスとズベレフが欧州牽引、フリッツとデミノーが世界選抜を率いる。',
      excerpt: 'ロンドンのO2アリーナで開催される2026年レーバーカップの開幕を翌日に控え、ノアとアガシ両主将が金曜初日の対戦カードを明らかにした。',
      body: [
        '全米オープンでのズベレフとルバキナの優勝を受け、テニス界はロンドンO2アリーナの黒い特設コートに集結。第9回レーバーカップはボルグとマッケンローからノアとアガシへと主将が引き継がれる新時代を迎えた。',
        'Sky Sportsと大会公式は木曜日に記者会見を開きメンバーを発表。欧州選抜はズベレフ、アルカラス、ルード、コボッリ、メンシク、ホダル。アガシ率いる世界選抜はフリッツ、デミノー、ナカシマ、ティエン、ブブリク、セルンドロが並ぶ。',
        '勝利ポイントは金曜1点、土曜2点、日曜3点と増え、先に13点を獲得したチームが栄冠を手にする。金曜の第1試合は英国時間午後1時に始まる。',
      ],
    },
    ko: {
      title: '런던 레이버컵 전야: 노아와 애거시, O2 아레나 금요 개막 대진 발표',
      subtitle: '팀 유럽과 팀 월드 1일차 경기 순서 확정. 알카라스와 츠베레프 유럽 선봉, 프리츠와 드미노 팀 월드 지휘.',
      excerpt: '런던 O2 아레나에서 열리는 2026 레이버컵 개막을 하루 앞두고 야닉 노아와 안드레 애거시 주장이 금요일 개막전 대진을 발표했다.',
      body: [
        'US 오픈에서 알렉산더 츠베레프와 엘레나 리바키나가 우승을 차지한 뒤 테니스 팬들의 시선은 런던 O2 아레나의 블랙 코트로 향했다. 제9회 레이버컵은 노아와 애거시가 지휘봉을 넘겨받으며 새 시대를 열었다.',
        '스카이 스포츠와 대회 조직위원회는 목요일 기자회견을 열고 공식 스쿼드를 확정했다. 팀 유럽은 츠베레프, 카를로스 알카라스, 카스페르 루드, 플라비오 코볼리, 야쿠프 멘시크, 라파엘 호다르로 구성됐다. 팀 월드는 테일러 프리츠, 알렉스 드미노, 브랜던 나카시마, 러너 티엔, 알렉산더 부블릭, 프란시스코 세룬돌로가 출전한다.',
        '승점은 금요일 1점, 토요일 2점, 일요일 3점으로 늘어나며 13점을 먼저 선점하는 팀이 우승 트로피를 차지한다. 1일차 경기는 영국 시간 금요일 오후 1시에 시작된다.',
      ],
    },
    ar: {
      title: 'عشية كأس لافر في لندن: نواه وأغاسي يعلنان مواجهات الجمعة الافتتاحية في O2',
      subtitle: 'فريق أوروبا وفريق العالم يحددان جدول مباريات اليوم الأول. ألكاراز وزفيريف يقودان أوروبا، وفريتز ودي مينور يقودان العالم.',
      excerpt: 'عشية انطلاق كأس لافر 2026 في قاعة O2 في لندن، كشف القائدان يانيك نواه وأندريه أغاسي عن مواجهات اليوم الافتتاحي الجمعة.',
      body: [
        'بعد تتويج زفيريف وريباكينا في أمريكا المفتوحة، ينتقل التنس العالمي إلى الملعب الأسود الشهير في O2 لندن. تشهد النسخة التاسعة بداية حقبة جديدة بتولي يانيك نواه وأندريه أغاسي قيادة الفريقين.',
        'أكدت شبكة سكاي سبورتس والموقع الرسمي تشكيلات الفرق يوم الخميس. يضم فريق أوروبا زفيريف وألكاراز ورود وكوبولي ومنسيك وجودار. ويضم فريق العالم بقيادة أغاسي فريتز ودي مينور وناكاشيما وتيين وبوبليك وسيروندولو.',
        'تمنح انتصارات الجمعة نقطة واحدة والسبت نقطتين والأحد ثلاث نقاط، ويتوج باللقب أول فريق يصل إلى 13 نقطة. تنطلق مباريات الجمعة في الواحدة ظهرا بتوقيت بريطانيا.',
      ],
    },
  },
  'laver-cup-day1-o2-london-2026': {
    fr: {
      title: 'Laver Cup Jour 1 : Ruud contre Cerúndolo et Menšík contre Nakashima enflamment l’O2',
      subtitle: 'Yannick Noah et Andre Agassi fixent les premiers duels à Londres. Un point par victoire le premier jour. Première équipe à 13 points.',
      excerpt: 'La 9e Laver Cup s’ouvre vendredi à l’O2 Arena de Londres. Casper Ruud affronte Francisco Cerúndolo et Jakub Menšík défie Brandon Nakashima en simple.',
      body: [
        'Après Flushing Meadows, le tennis mondial s’installe sous le dôme de l’O2 à Londres pour la 9e Laver Cup. Ce tournoi marque une grande première avec de nouveaux capitaines : Yannick Noah dirige l’équipe Europe et Andre Agassi mène l’équipe Monde.',
        'Les organisateurs et Sky Sports ont confirmé la feuille de match du vendredi. La session de jour débute à 13h00 sur le court noir. Casper Ruud ouvre le bal pour l’Europe contre l’Argentin Francisco Cerúndolo, suivi du match entre le jeune tchèque Jakub Menšík et l’Américain Brandon Nakashima.',
        'Chaque succès le vendredi rapporte un point. Les matches de samedi vaudront deux points et ceux de dimanche trois points. La première formation à atteindre 13 points soulève le trophée.',
      ],
    },
    es: {
      title: 'Laver Cup Día 1: Ruud ante Cerúndolo y Menšík ante Nakashima encienden el O2',
      subtitle: 'Yannick Noah y Andre Agassi definen los duelos del viernes en Londres. Un punto por victoria en la jornada 1. Primer equipo en llegar a 13 puntos.',
      excerpt: 'La 9.ª Laver Cup se pone en marcha este viernes en el O2 Arena de Londres. Casper Ruud choca con Francisco Cerúndolo y Jakub Menšík se mide a Brandon Nakashima en individuales.',
      body: [
        'Tras el cierre del US Open, el tenis internacional aterriza bajo el techo del O2 de Londres para la 9.ª Laver Cup. El certamen estrena la era de Yannick Noah al frente de Europa y Andre Agassi como capitán del Equipo Mundo.',
        'Sky Sports y la organización confirmaron el orden de juego del viernes. La jornada diurna arranca a las 13:00 hora local en la pista negra con el duelo entre Casper Ruud y Francisco Cerúndolo, seguido por el choque entre Jakub Menšík y Brandon Nakashima.',
        'Cada victoria del viernes otorga un punto. Las del sábado sumarán dos y las del domingo tres. El primer equipo que consiga 13 puntos alzará la copa.',
      ],
    },
    de: {
      title: 'Laver Cup Tag 1: Ruud gegen Cerúndolo und Menšík gegen Nakashima eröffnen The O2',
      subtitle: 'Yannick Noah und Andre Agassi stellen Aufstellung für Freitag auf. Ein Punkt pro Sieg am ersten Tag. Erstes Team bei 13 Punkten gewinnt.',
      excerpt: 'Der 9. Laver Cup beginnt am Freitag in der Londoner O2 Arena. Casper Ruud trifft auf Francisco Cerúndolo und Jakub Menšík spielt gegen Brandon Nakashima.',
      body: [
        'Nach Flushing Meadows versammelt sich die Tenniselite in der Londoner O2 Arena zum 9. Laver Cup. Die Kapitäne Yannick Noah (Team Europa) und Andre Agassi (Team Welt) leiten erstmals ihre Teams an.',
        'Sky Sports und die Laver-Cup-Leitung bestätigten das Programm für Freitag. Ab 13:00 Uhr Ortszeit eröffnet Casper Ruud gegen Francisco Cerúndolo auf dem schwarzen Hartplatz, gefolgt vom Duell Jakub Menšík gegen Brandon Nakashima.',
        'Jeder Sieg am Freitag bringt einen Punkt, am Samstag zwei und am Sonntag drei. Das Team, das zuerst 13 Punkte erzielt, gewinnt den Pokal.',
      ],
    },
    it: {
      title: 'Laver Cup Giorno 1: Ruud contro Cerúndolo e Menšík contro Nakashima accendono l’O2',
      subtitle: 'Yannick Noah e Andre Agassi ufficializzano le sfide del venerdì a Londra. Un punto a vittoria nella prima giornata. Vince chi arriva a 13 punti.',
      excerpt: 'La nona edizione della Laver Cup prende il via venerdì all’O2 Arena di Londra. Casper Ruud sfida Francisco Cerúndolo e Jakub Menšík affronta Brandon Nakashima in singolare.',
      body: [
        'Dopo gli US Open, il grande tennis si ritrova all’O2 di Londra per la 9ª Laver Cup. Debutto assoluto per i nuovi capitani: Yannick Noah guida Team Europe e Andre Agassi guida Team World.',
        'Sky Sports e gli organizzatori hanno confermato il programma del venerdì. La sessione diurna inizia alle 13:00 locali con Ruud contro Cerúndolo, seguito dal match tra Menšík e Nakashima sul campo nero indoor.',
        'Ogni successo del venerdì vale un punto, due al sabato e tre alla domenica. La prima squadra a toccare quota 13 punti conquista il titolo.',
      ],
    },
    pl: {
      title: 'Laver Cup Dzień 1: Ruud kontra Cerúndolo i Menšík kontra Nakashima otwierają The O2',
      subtitle: 'Yannick Noah i Andre Agassi ustalili piątkowe składy w Londynie. Jeden punkt za zwycięstwo w pierwszym dniu. Do triumfu potrzeba 13 punktów.',
      excerpt: '9. edycja Laver Cup rozpoczyna się w piątek w londyńskiej hali The O2. Casper Ruud gra z Francisco Cerúndolo, a Jakub Menšík mierzy się z Brandonem Nakashimą.',
      body: [
        'Po zakończeniu zmagań w Nowym Jorku tenis przenosi się do hali The O2 w Londynie na 9. Puchar Lavera. Po raz pierwszy w roli kapitanów debiutują Yannick Noah dla Europy i Andre Agassi dla Świata.',
        'Organizatorzy i Sky Sports podali plan gier na piątek. Sesja dzienna startuje o 13:00 na czarnym korcie od pojedynku Caspera Ruuda z Francisco Cerúndolo, po którym na kort wyjdą Jakub Menšík i Brandon Nakashima.',
        'Za każdy piątkowy triumf przyznawany jest jeden punkt, w sobotę dwa, a w niedzielę trzy. Zwycięża drużyna, która jako pierwsza zgromadzi 13 punktów.',
      ],
    },
    zh: {
      title: '拉沃尔杯首日：鲁德迎战塞伦多洛，门希克对决中岛布兰登点燃O2',
      subtitle: '诺阿与阿加西排定伦敦周五开幕战对阵。首日获胜积1分，先得13分捧杯。',
      excerpt: '第9届拉沃尔杯周五在伦敦O2体育馆打响。卡斯珀·鲁德对阵弗朗西斯科·塞伦多洛，捷克新星雅库布·门希克迎战中岛布兰登。',
      body: [
        '美网落幕后，国际网坛焦点转战伦敦O2体育馆的黑色特制球场。第9届拉沃尔杯迎来了新队长时代：诺阿率领欧洲队，阿加西执掌世界队。',
        '天空体育与拉沃尔杯官方公布了周五对阵。日场于当地时间下午1点开打，鲁德率先出战对阵阿根廷名将塞伦多洛，随后门希克对阵美网表现抢眼的中岛布兰登。晚场还将进行单打与双打较量。',
        '比赛采取积分递增制：周五每胜得1分，周六得2分，周日得3分。率先获得13分的队伍将夺得拉沃尔杯冠军。',
      ],
    },
    ja: {
      title: 'レーバーカップ初日：ルード対セルンドロ、メンシク対ナカシマでO2熱戦開幕',
      subtitle: 'ノアとアガシ両主将が金曜日の初戦ラインナップを決定。初日は各勝点1、先に13点到達で勝利。',
      excerpt: '第9回レーバーカップが金曜日にロンドンのO2アリーナで開幕。シングルスでキャスパー・ルードがセルンドロと、メンシクがナカシマと激突する。',
      body: [
        '全米オープンが閉幕し、テニス界はロンドンO2アリーナの特設黒コートへ。第9回大会はヤニック・ノア欧州選抜主将とアンドレ・アガシ世界選抜主将の初陣となる。',
        '大会公式とSky Sportsによると、昼セッションは現地13時開始。第1試合でルードがセルンドロと、第2試合でメンシクがナカシマと対戦。夜セッションにはシングルスとダブルスが控える。',
        '勝利ポイントは金曜1点、土曜2点、日曜3点。先に13点を獲得したチームが優勝トロフィーを手にする。',
      ],
    },
    ko: {
      title: '레이버컵 1일차: 루드 vs 세룬돌로, 멘시크 vs 나카시마로 O2 아레나 개막',
      subtitle: '야닉 노아와 안드레 애거시 금요 개막전 라인업 확정. 1일차 승점 1점, 13점 선점 시 우승.',
      excerpt: '제9회 레이버컵이 금요일 런던 O2 아레나에서 개막했다. 카스페르 루드가 프란시스코 세룬돌로와 맞붙고 야쿠프 멘시크가 브랜던 나카시마와 격돌한다.',
      body: [
        'US 오픈을 마친 세계 테니스가 런던 O2 아레나의 블랙 코트로 모였다. 이번 제9회 대회는 야닉 노아(유럽)와 안드레 애거시(월드) 단장 체제의 첫 맞대결이다.',
        '스카이 스포츠와 대회 본부에 따르면 주간 세션은 현지 오후 1시에 시작된다. 1경기에서 루드가 세룬돌로를 상대하고 2경기에서 멘시크가 나카시마와 맞선다. 야간 세션에는 단식과 복식이 이어진다.',
        '승점은 금요일 경기당 1점, 토요일 2점, 일요일 3점으로 늘어나며 13점을 먼저 획득하는 팀이 챔피언에 오른다.',
      ],
    },
    ar: {
      title: 'كأس لافر اليوم الأول: رود ضد سيروندولو ومنسيك ضد ناكاشيما يشعلان أجواء O2',
      subtitle: 'يانيك نواه وأندريه أغاسي يحددان مواجهات الجمعة في لندن. نقطة واحدة لكل فوز في اليوم الأول. أول فريق يبلغ 13 نقطة يفوز باللقب.',
      excerpt: 'انطلقت النسخة التاسعة من كأس لافر يوم الجمعة في قاعة O2 في لندن بمواجهتي كاسبر رود ضد فرانشيسكو سيروندولو وياكوب منسيك ضد براندون ناكاشيما.',
      body: [
        'بعد ختام بطولة أمريكا المفتوحة، ينتقل التنس إلى الملعب الأسود في قاعة O2 في لندن للنسخة التاسعة من كأس لافر، بقيادة القائدين الجديدين يانيك نواه لفريق أوروبا وأندريه أغاسي لفريق العالم.',
        'أكدت شبكة سكاي سبورتس جدول مباريات الجمعة. تبدأ الجلسة النهارية في الواحدة ظهرا بمباراة رود أمام سيروندولو، تليها مباراة الصاعد منسيك أمام ناكاشيما، قبل مواجهتي المساء في الفردي والزوجي.',
        'يمنح كل فوز يوم الجمعة نقطة واحدة، وترتفع إلى نقطتين السبت وثلاث نقاط الأحد، ويتوج باللقب أول فريق يحصد 13 نقطة.',
      ],
    },
  },
  'baku-gp-qualifying-day-2026': {
    fr: {
      title: 'Qualifications à Bakou : Antonelli et Russell en quête de la pole sur le circuit urbain',
      subtitle: 'Séance de qualifications le vendredi pour verrouiller la grille des 51 tours du samedi. Mercedes domine les constructeurs avec 503 points.',
      excerpt: 'La Formule 1 dispute ses qualifications vendredi sur le circuit urbain de Bakou. Kimi Antonelli et George Russell mènent l’assaut Mercedes face à Ferrari et McLaren.',
      body: [
        'La Formule 1 aborde la phase décisive de son calendrier inhabituel du jeudi au samedi à Bakou, la journée de dimanche étant consacrée au souvenir national en Azerbaïdjan. La grille de départ du Grand Prix de 51 tours sera établie ce vendredi après-midi.',
        'Après les essais du jeudi le long de la Caspienne, Formula1.com et Sky Sports précisent le déroulement des EL3 puis de la séance qualificative à 13h00 heure de Londres (16h00 locales). Mercedes arrive en favorite avec Antonelli (292 pts) et Russell (211 pts).',
        'La position sur la grille à Bakou est primordiale. Les pilotes n’auront que 24 heures pour peaufiner leurs réglages avant la course de 51 tours programmée samedi.',
      ],
    },
    es: {
      title: 'Día de clasificación en Bakú: Antonelli y Russell van por la pole en el circuito urbano',
      subtitle: 'Rara sesión de clasificación en viernes para armar la parrilla de las 51 vueltas del sábado. Mercedes lidera constructores con 503 puntos.',
      excerpt: 'La Fórmula 1 disputa este viernes la clasificación en Bakú. Kimi Antonelli y George Russell comandan a Mercedes en la batalla por la pole position.',
      body: [
        'La Fórmula 1 encara la jornada crucial de su cronograma especial en el Gran Premio de Azerbaiyán 2026. Con el domingo dedicado al Día del Recuerdo, la parrilla completa de 51 vueltas se definirá este viernes por la tarde en el trazado de 6,003 km.',
        'Tras los entrenamientos del jueves, Formula1.com y Sky Sports marcan la pauta con los Libres 3 y la sesión clasificatoria a las 13:00 hora del Reino Unido (16:00 locales). Mercedes lidera el certamen con Antonelli (292 pts) y Russell (211 pts).',
        'La posición de salida en Bakú resulta determinante. Los equipos solo dispondrán de 24 horas para afinar estrategias antes de la carrera del sábado.',
      ],
    },
    de: {
      title: 'Qualifying-Tag in Baku: Antonelli und Russell kämpfen um die Pole Position',
      subtitle: 'Freitags-Qualifying entscheidet über Startaufstellung für 51-Runden-Grand-Prix am Samstag. Mercedes führt Konstrukteure mit 503 Punkten an.',
      excerpt: 'Die Formel 1 trägt am Freitag das Qualifying auf dem Baku City Circuit aus. WM-Leader Kimi Antonelli und George Russell kämpfen um die Pole gegen Ferrari und McLaren.',
      body: [
        'Die Formel 1 erreicht den Höhepunkt ihres ungewöhnlichen Zeitplans in Aserbaidschan. Da der Sonntag dem nationalen Gedenktag vorbehalten ist, wird die komplette Startaufstellung für den 51-Runden-Grand-Prix bereits am Freitagnachmittag ermittelt.',
        'Formula1.com und Sky Sports berichten über den Übergang von FP3 zum Qualifying um 13:00 Uhr britischer Zeit (16:00 Uhr Ortszeit). Mercedes reist als Favorit an: Rookie Kimi Antonelli führt mit 292 Punkten, Russell folgt mit 211.',
        'Die Startposition ist auf dem Hochgeschwindigkeits-Stadtkurs entscheidend. Den Fahrern bleiben nach dem Qualifying nur 24 Stunden bis zum Rennstart am Samstag.',
      ],
    },
    it: {
      title: 'Qualifiche a Baku: Antonelli e Russell cacciano la pole al Baku City Circuit',
      subtitle: 'Inedita qualifica al venerdì per comporre lo schieramento dei 51 giri del sabato. Mercedes al comando costruttori con 503 punti.',
      excerpt: 'La Formula 1 entra nel vivo venerdì a Baku con le qualifiche ufficiali. Il leader Kimi Antonelli e George Russell puntano alla prima fila contro Ferrari e McLaren.',
      body: [
        'La Formula 1 entra nel momento clou del suo weekend anticipato in Azerbaigian. Con la domenica riservata alla Giornata del Ricordo, la griglia per il Gran Premio di 51 giri si forma questo venerdì pomeriggio sul tracciato cittadino di 6,003 km.',
        'Formula1.com e Sky Sports evidenziano il programma con le FP3 seguite dalla qualifica alle 13:00 ora britannica (16:00 locali). La Mercedes comanda la classifica con Antonelli a 292 punti e Russell a 211.',
        'A Baku la qualifica è fondamentale per evitare i pericoli dei muretti. I piloti avranno solo 24 ore prima dello spegnimento dei semafori sabato.',
      ],
    },
    pl: {
      title: 'Dzień kwalifikacji w Baku: Antonelli i Russell walczą o pole position',
      subtitle: 'Piątkowe kwalifikacje ustalają pola startowe do 51-okrążeniowego wyścigu w sobotę. Mercedes liderem konstruktorów z 503 punktami.',
      excerpt: 'Formuła 1 przeprowadza w piątek kwalifikacje na Baku City Circuit. Lider klasyfikacji Kimi Antonelli i George Russell rywalizują o pole position z Ferrari i McLarenem.',
      body: [
        'Formuła 1 wkracza w decydującą fazę skróconego weekendu w Baku. Ze względu na niedzielny Dzień Pamięci w Azerbejdżanie, ustawienie na starcie do 51-okrążeniowego wyścigu zostanie ustalone w piątek po południu.',
        'Formula1.com i Sky Sports zapowiadają sesję kwalifikacyjną o 13:00 czasu brytyjskiego (16:00 czasu lokalnego). Mercedes pozostaje zespołem numer jeden dzięki Antonellemu (292 pkt) i Russellowi (211 pkt).',
        'Pozycja startowa w Baku jest kluczowa. Kierowcy będą mieli zaledwie 24 godziny na przygotowanie strategii do sobotniego wyścigu.',
      ],
    },
    zh: {
      title: '巴库排位日：安东内利与拉塞尔冲击街道赛杆位',
      subtitle: '罕见周五排位赛敲定周六51圈正赛发车位。梅赛德斯积503分领跑车队榜。',
      excerpt: 'F1周五在巴库城市赛道打响排位赛。积分榜领头羊安东内利与队友拉塞尔代表梅赛德斯迎战法拉利与迈凯伦的挑战。',
      body: [
        '2026年阿塞拜疆大奖赛的周四至周六赛程在周五进入关键阶段。为尊重周日的全国纪念日，全长51圈的正赛发车位将于周五下午在6.003公里的巴库城市赛道决出。',
        'F1官网与天空体育报道，车手在三练后直接进入英国时间下午1点（当地时间下午4点）展开的排位赛较量。梅赛德斯以503分强势领跑车队榜，新星安东内利以292分在车手榜居首。',
        '在兼具2.2公里大直道和极窄城堡弯的巴库赛道，杆位至关重要。排位赛结束后车手仅有24小时为周六的正赛做最后调整。',
      ],
    },
    ja: {
      title: 'バクー予選日：アントネッリとラッセルが市街地コースでポールポジションを争う',
      subtitle: '異例の金曜予選で土曜51周の決勝グリッドが確定。メルセデスが503点で製造者首位を独走。',
      excerpt: 'F1アゼルバイジャンGPの公式予選が金曜日にバクー市街地コースで実施される。ポイント首位のアントネッリとラッセルが最前列を狙う。',
      body: [
        '日曜の戦没者追悼記念日に伴い、2026年アゼルバイジャンGPは金曜日に予選を迎えた。全長6.003kmのバクー市街地コースで土曜決勝51周のグリッドが決定する。',
        'F1公式とSky Sportsによると、FP3に続き英国時間午後1時（現地時間16時）からノックアウト予選がスタート。メルセデスはアントネッリ（292点）とラッセル（211点）が好調を維持している。',
        '最高速340km/hのストレートと狭隘な城塞区間を持つバクーではグリッド位置が勝敗を左右する。各車は土曜決勝へ向け24時間の準備期間に入る。',
      ],
    },
    ko: {
      title: '바쿠 예선일: 안토넬리와 러셀, 바쿠 시티 서킷서 폴포지션 격돌',
      subtitle: '금요 예선으로 토요일 51랩 결선 그리드 확정. 메르세데스 503점으로 컨스트럭터 선두 질주.',
      excerpt: 'F1 아제르바이잔 그랑프리 예선이 금요일 바쿠 시티 서킷에서 펼쳐진다. 챔피언십 1위 키미 안토넬리와 조지 러셀이 폴포지션 사냥에 나선다.',
      body: [
        '일요일 전몰자 추모의 날을 맞아 특별 일정으로 치러지는 2026 아제르바이잔 GP가 금요일 예선에 돌입한다. 6.003km 서킷에서 토요일 51랩 결선 출발 순서가 정해진다.',
        'F1 공식과 스카이 스포츠에 따르면 영국 시간 오후 1시(현지시간 오후 4시)부터 공식 예선이 열린다. 메르세데스는 안토넬리(292점)와 러셀(211점)을 앞세워 1열 독점을 겨냥한다.',
        '2.2km의 초고속 직선로와 올드타운 병목 코너가 공존하는 바쿠에서는 예선 순위가 결정적이다. 결선 레이스는 토요일 정오(영국 시간)에 시작된다.',
      ],
    },
    ar: {
      title: 'يوم تصفيات باكو: أنتونيللي وروسيل يطاردان مركز الانطلاق الأول في حلبة الشوارع',
      subtitle: 'تصفيات الجمعة تحدد شبكة انطلاق سباق السبت المكون من 51 لفة. مرسيدس تقود بطولة الصانعين برصيد 503 نقاط.',
      excerpt: 'تخوض فرق فورمولا 1 حصة التصفيات الرسمية يوم الجمعة في حلبة باكو. يسعى متصدر البطولة كيمي أنتونيللي وزميله جورج روسيل لحسم الصدارة.',
      body: [
        'تصل جائزة أذربيجان الكبرى لعام 2026 إلى ذروتها يوم الجمعة مع إجراء التصفيات الرسمية على مسار باكو البالغ طوله 6.003 كم لتحديد شبكة انطلاق سباق السبت المكون من 51 لفة.',
        'أفادت تقارير فورمولا 1 وسكاي سبورتس بانطلاق التصفيات في الواحدة ظهرا بتوقيت بريطانيا (الرابعة عصرا بتوقيت باكو). تتصدر مرسيدس الترتيب بفضل أنتونيللي (292 نقطة) وروسيل (211 نقطة).',
        'يعد مركز الانطلاق حاسما في حلبة باكو نظرا لصعوبة التجاوز عند مقطع القلعة الضيق، ويفصل السائقين 24 ساعة فقط عن انطلاق السباق الرئيسي يوم السبت.',
      ],
    },
  },
  'presidents-cup-day2-medinah-2026': {
    fr: {
      title: 'Presidents Cup Jour 2 : Medinah n° 3 intensifie les débats du vendredi',
      subtitle: 'Brandt Snedeker et Geoff Ogilvy abordent le jour 2 sur des greens rénovés. Scottie Scheffler et Adam Scott mènent leurs camps.',
      excerpt: 'La 16e Presidents Cup poursuit son rythme au Medinah Country Club dans l’Illinois. L’équipe américaine et les Internationaux se disputent des points capitaux vendredi.',
      body: [
        'Après une première journée disputée à Medinah, la 16e Presidents Cup s’accélère vendredi. Avec 30 points au total sur quatre journées, les matches du vendredi constituent un tournant avant le samedi et les simples du dimanche.',
        'Le PGA Tour et PresidentsCup.com indiquent que Brandt Snedeker et Geoff Ogilvy ont ajusté leurs duos sur le parcours n° 3 redessiné par OCM Golf. Les zones de dégagement et les greens fermes obligent les joueurs à un jeu d’approche millimétré.',
        'Le n° 1 mondial Scottie Scheffler continue de porter l’équipe américaine, tandis qu’Adam Scott, dans sa 12e participation, apporte son calme aux côtés d’Hideki Matsuyama et Tom Kim pour tenter de renverser les champions en titre.',
      ],
    },
    es: {
      title: 'Presidents Cup Día 2: Medinah n.º 3 eleva la exigencia en los duelos del viernes',
      subtitle: 'Brandt Snedeker y Geoff Ogilvy afrontan la segunda jornada en greens renovados. Scottie Scheffler y Adam Scott lideran los equipos.',
      excerpt: 'La 16.ª Presidents Cup continúa este viernes en Medinah Country Club de Illinois. EE. UU. y el equipo Internacional disputan puntos clave en el campo n.º 3.',
      body: [
        'Tras un inicio vibrante en Medinah Country Club, la 16.ª Presidents Cup sube de nivel este viernes. Con 30 puntos en juego durante cuatro días, la jornada de hoy marca un punto de inflexión crucial.',
        'PGA Tour y PresidentsCup.com señalan que Brandt Snedeker y Geoff Ogilvy movieron sus fichas en el recorrido n.º 3 rediseñado por OCM Golf. El diseño castiga los errores con amplias trampas de arena y caídas pronunciadas alrededor de los greens.',
        'El número uno Scottie Scheffler sostiene la ofensiva estadounidense, mientras que el veterano Adam Scott y Hideki Matsuyama buscan liderar la remontada del equipo Internacional.',
      ],
    },
    de: {
      title: 'Presidents Cup Tag 2: Medinah Kurs Nr. 3 fordert die Teams am Freitag',
      subtitle: 'Brandt Snedeker und Geoff Ogilvy stellen Teams auf renovierten Grüns ein. Scottie Scheffler und Adam Scott als Ankerpunkte.',
      excerpt: 'Der 16. Presidents Cup geht am Freitag im Medinah Country Club in Illinois in die zweite Runde. Die USA und das internationale Team kämpfen um entscheidende Matchplay-Punkte.',
      body: [
        'Nach einem packenden Auftakt im Medinah Country Club nimmt der 16. Presidents Cup am Freitag Fahrt auf. Bei insgesamt 30 zu vergebenden Punkten sind die heutigen Duelle von zentraler Bedeutung für den weiteren Turnierverlauf.',
        'PGA Tour und PresidentsCup.com berichten über die taktischen Aufstellungen von Snedeker und Ogilvy auf dem neu gestalteten Kurs Nr. 3. Schnelle Grüns und offene Bunkerlandschaften verlangen äußerste Präzision.',
        'Die Nummer 1 Scottie Scheffler führt die US-Amerikaner an, während Adam Scott bei seinem 12. Auftritt gemeinsam mit Hideki Matsuyama und Tom Kim das internationale Team inspiriert.',
      ],
    },
    it: {
      title: 'Presidents Cup Giorno 2: il percorso n. 3 di Medinah alza la posta per le sfide del venerdì',
      subtitle: 'Brandt Snedeker e Geoff Ogilvy gestiscono il day 2 sui rinnovati green. Scottie Scheffler e Adam Scott pilastri dei due schieramenti.',
      excerpt: 'La 16ª Presidents Cup entra nella seconda giornata al Medinah Country Club in Illinois. USA e Team Internazionale si contendono punti pesanti.',
      body: [
        'Dopo l’intenso avvio a Medinah, la 16ª Presidents Cup entra nel vivo questo venerdì. Con 30 punti totali in palio nel weekend, le sfide odierne rappresentano uno snodo cruciale.',
        'PGA Tour e PresidentsCup.com segnalano le nuove formazioni scelte dai capitani sul ridisegnato Course No. 3. I green fermi e le ampie aree sabbiose mettono a dura prova i migliori interpreti mondiali.',
        'Scottie Scheffler fa da traino per gli statunitensi, mentre Adam Scott e Hideki Matsuyama guidano la riscossa della selezione internazionale contro lo strapotere a stelle e strisce.',
      ],
    },
    pl: {
      title: 'Puchar Prezydentów Dzień 2: Medinah Course No. 3 podgrzewa atmosferę w piątek',
      subtitle: 'Brandt Snedeker i Geoff Ogilvy prowadzą zespoły na przebudowanym polu. Scottie Scheffler i Adam Scott liderami formacji.',
      excerpt: '16. Puchar Prezydentów wkracza w drugi dzień zmagań w Medinah Country Club w Illinois. Zespoły USA i Świata walczą o kluczowe punkty meczowe.',
      body: [
        'Po zaciętym początku w Medinah Country Club rywalizacja w 16. Pucharze Prezydentów nabiera tempa w piątek. Spośród 30 punktów do zdobycia w całym turnieju, dzisiejsze mecze mają kluczowe znaczenie strategiczne.',
        'PGA Tour i PresidentsCup.com donoszą o nowych parach wystawionych przez kapitanów Snedekera i Ogilvy’ego na polu Course No. 3. Trudne kontury greenów i rozległe przeszkody piaskowe wymagają bezbłędnej gry żelazami.',
        'Lider rankingu Scottie Scheffler przewodzi Amerykanom, podczas gdy Adam Scott i Hideki Matsuyama starają się zapewnić cenne punkty Drużynie Międzynarodowej.',
      ],
    },
    zh: {
      title: '2026总统杯次日：梅迪纳3号球场战况升级',
      subtitle: '斯内德克与奥格维在翻新果岭排兵布阵。舍夫勒与斯科特各自领衔核心对决。',
      excerpt: '第16届总统杯在伊利诺伊州梅迪纳乡村俱乐部迎来第二日角逐。美国队与国际队在改建后的3号球场全力争夺关键积分。',
      body: [
        '在首日胶着的对抗后，第16届总统杯在周五全面提速。在全部30分的分值中，周五的对决将直接决定周末决战前的走势。',
        '美巡赛与总统杯官网报道，斯内德克与奥格维派出了针对性极强的出场阵容。梅迪纳3号球场坚硬起伏的果岭给推杆带来了极大考验。',
        '世界第一斯科蒂·舍夫勒继续担当美国队定海神针，而第12次参赛的亚当·斯科特联手松山英树与金柱亨，力争在周五缩小与美国队的差距。',
      ],
    },
    ja: {
      title: 'プレジデンツカップ2日目：メディナ3番コースで白熱の金曜決戦',
      subtitle: 'スネデカーとオギルビーが改修グリーンで激突。シェフラーとスコットがチームの要。',
      excerpt: '第16回プレジデンツカップは米イリノイ州メディナCCで2日目を迎えた。米国選抜と世界選抜が改修された3番コースで貴重な勝ち点を争う。',
      body: [
        '初日の激闘を経て、第16回プレジデンツカップは金曜日に一段と熱を帯びる。通算30ポイントのうち、週末を前にした2日目のマッチは勝敗を占う重要な局面となる。',
        'PGAツアーおよび大会公式によると、スネデカー主将とオギルビー主将が新たなペアリングを投入。OCMゴルフが改修した硬く起伏のあるグリーンが選手たちの技量を試す。',
        '世界1位シェフラーが米国を牽引する一方、12度目の出場となるアダム・スコットと松山英樹が世界選抜の逆襲を狙う。'
      ],
    },
    ko: {
      title: '프레지던츠컵 2일차: 메디나 3번 코스서 달아오르는 금요 격돌',
      subtitle: '스네데커와 오길비, 새 단장된 그린서 승부수. 셰플러와 애덤 스콧 각 팀 기둥 역할.',
      excerpt: '제16회 프레지던츠컵이 미국 일리노이주 메디나 컨트리클럽에서 2일차 일정에 돌입했다. 미국과 인터내셔널 팀이 중요한 매치플레이 승점을 다툰다.',
      body: [
        '1일차 접전을 치른 제16회 프레지던츠컵이 금요일 더 뜨거운 열기로 이어진다. 총 30점의 승점 중 2일차 경기는 주말 결전을 앞둔 핵심 승부처다.',
        'PGA 투어와 대회 공식 사이트에 따르면 스네데커와 오길비 단장은 새로운 조합으로 필드에 나섰다. OCM 골프가 재설계한 단단하고 경사진 그린이 쇼트게임의 정교함을 요구한다.',
        '세계 1위 스코티 셰플러가 미국 팀을 이끌고, 12회 출전의 애덤 스콧과 마쓰야마 히데키가 인터내셔널 팀의 반격을 주도한다.',
      ],
    },
    ar: {
      title: 'كأس الرؤساء اليوم الثاني: اشتعال المنافسة على ملعب مادينا رقم 3',
      subtitle: 'سنديكر وأوجيلفي يقودان مواجهات الجمعة فوق مساحات خضراء متجددة. شيفلر وسكوت يقودان الفريقين.',
      excerpt: 'تتواصل النسخة الـ16 من كأس الرؤساء في نادي مادينا في إلينوي في يومها الثاني، مع تنافس أمريكا والفريق الدولي على نقاط حاسمة.',
      body: [
        'بعد انطلاقة قوية في نادي مادينا، تتسارع وتيرة النسخة الـ16 من كأس الرؤساء يوم الجمعة. تمثل مباريات اليوم نقطة تحول كبرى ضمن 30 نقطة مطروحة في البطولة.',
        'أفادت تقارير جولة بي جي إيه والموقع الرسمي للبطولة باعتماد القائدين تشكيلات تكتيكية جديدة على الملعب رقم 3. وتفرض الحفر والرمال المتسعة تحديا كبيرا على دقة الضربات.',
        'يواصل المصنف الأول سكوتي شيفلر قيادة الفريق الأمريكي، بينما يعتمد الفريق الدولي على خبرة آدم سكوت وهيديكي ماتسوياما لإشعال المنافسة قبل عطلة نهاية الأسبوع.',
      ],
    },
  },
  'baku-gp-race-day-2026': {
    fr: {
      title: 'Jour de course à Bakou : Antonelli mène le doublé Mercedes en première ligne',
      subtitle: 'Le prodige décroche la pole aux côtés de Russell. 51 tours à haute vitesse le long de la forteresse et de la ligne droite de la Caspienne.',
      excerpt: 'La Formule 1 s’élance ce samedi sur le circuit urbain de Bakou. Le leader du championnat Kimi Antonelli part en pole position devant son coéquipier George Russell.',
      body: [
        'La Formule 1 aborde sa journée de course ce samedi 26 septembre sur le tracé de 6,003 kilomètres du circuit urbain de Bakou. En raison de la journée du souvenir observée le dimanche en Azerbaïdjan, l’épreuve reine a été avancée de 24 heures.',
        'Formula1.com et Sky Sports confirment que Kimi Antonelli a signé la pole position vendredi avec un chrono de 1:40.445, devançant son coéquipier George Russell pour verrouiller la première ligne Mercedes. Antonelli compte 81 points d’avance au championnat avec 292 points.',
        'Charles Leclerc s’élance troisième sur Ferrari aux côtés de Lando Norris sur McLaren en deuxième ligne, tandis que Lewis Hamilton part cinquième. Avec des pointes à 350 km/h sur l’avenue Neftchilar et le passage étroit du virage 8, la course promet de grands rebondissements.',
      ],
    },
    es: {
      title: 'Día de carrera en Bakú: Antonelli encabeza el doblete de Mercedes en primera línea',
      subtitle: 'El joven talento logra la pole junto a Russell. 51 vueltas a fondo junto a la fortaleza y la recta del Caspio.',
      excerpt: 'La Fórmula 1 compite este sábado en el circuito urbano de Bakú. El líder del Mundial Kimi Antonelli arranca desde la pole con su compañero George Russell en segundo lugar.',
      body: [
        'La Fórmula 1 disputa el Gran Premio de Azerbaiyán este sábado 26 de septiembre en el circuito de 6,003 kilómetros de Bakú. Con el domingo reservado al día de conmemoración nacional, la carrera principal se adelanta 24 horas.',
        'Formula1.com y Sky Sports confirman que Kimi Antonelli se adjudicó la pole el viernes con un tiempo de 1:40.445, superando a su compañero George Russell para asegurar una primera fila exclusiva de Mercedes. Antonelli lidera el campeonato con 292 puntos.',
        'Charles Leclerc sale tercero para Ferrari con Lando Norris en McLaren en la segunda fila, mientras Lewis Hamilton parte quinto. Las velocidades de 350 km/h en la recta de Neftchilar y la estrechez del castillo exigirán la máxima concentración a los pilotos.',
      ],
    },
    de: {
      title: 'Renntag in Baku: Antonelli führt Mercedes-Doppelführung in erste Startreihe',
      subtitle: 'Rookie-Sensation sichert sich Pole neben Russell. 51 rasante Runden vorbei an Festungsmauern und Kaspischem Meer.',
      excerpt: 'Die Formel 1 startet am Samstag auf dem Baku City Circuit ins Rennen. WM-Spitzenreiter Kimi Antonelli steht auf der Pole Position, George Russell auf Platz zwei.',
      body: [
        'Die Formel 1 startet am Samstag, dem 26. September, auf dem 6,003 Kilometer langen Baku City Circuit in den Renntag. Da der Sonntag in Aserbaidschan als nationaler Gedenktag begangen wird, findet der Grand Prix 24 Stunden früher statt.',
        'Formula1.com und Sky Sports bestätigen, dass Kimi Antonelli im Freitags-Qualifying mit einer Runde von 1:40.445 die Pole Position vor Teamkollege George Russell holte. Antonelli führt die Fahrerwertung mit 292 Punkten an.',
        'Charles Leclerc im Ferrari startet als Dritter neben Lando Norris im McLaren aus Reihe zwei, während Lewis Hamilton Fünfter ist. Geschwindigkeiten von 350 km/h auf der Neftchilar-Geraden und die enge Kurve 8 an der Altstadt fordern höchste fahrerische Präzision.',
      ],
    },
    it: {
      title: 'Giorno di gara a Baku: Antonelli guida la prima fila tutta Mercedes per 51 giri mozzafiato',
      subtitle: 'Il giovane talento conquista la pole accanto a Russell. 51 giri ad alta velocità tra le mura della fortezza e il rettilineo sul Caspio.',
      excerpt: 'La Formula 1 scende in pista sabato sul Baku City Circuit. Il leader della classifica Kimi Antonelli scatta dalla pole position affiancato dal compagno George Russell.',
      body: [
        'La Formula 1 entra nel giorno del Gran Premio sabato 26 settembre sul tracciato cittadino di 6,003 chilometri a Baku. Con la domenica dedicata alla giornata del ricordo in Azerbaijan, la gara principale è stata anticipata di 24 ore.',
        'Formula1.com e Sky Sports confermano che il debuttante Kimi Antonelli ha conquistato la pole position venerdì fermando il cronometro a 1:40.445, precedendo George Russell per una prima fila interamente Mercedes. Antonelli guida il mondiale a quota 292 punti.',
        'Charles Leclerc scatterà terzo con la Ferrari al fianco di Lando Norris su McLaren in seconda fila, con Lewis Hamilton in quinta casella. Con velocità di 350 km/h sul viale Neftchilar e il passaggio stretto della curva 8, la sfida per la vittoria sarà totale.',
      ],
    },
    pl: {
      title: 'Dzień wyścigu w Baku: Antonelli prowadzi pierwszy rząd Mercedesa w 51-okrążeniowej walce',
      subtitle: 'Rewelacyjny debiutant zdobywa pole position obok Russella. 51 szybkich okrążeń wokół murów twierdzy i prostej nad Morzem Kaspijskim.',
      excerpt: 'Formuła 1 ściga się w sobotę na torze Baku City Circuit. Lider mistrzostw Kimi Antonelli rusza z pole position, a tuż obok stanie George Russell.',
      body: [
        'Formuła 1 wkracza w dzień wyścigu w sobotę 26 września na ulicznym torze w Baku o długości 6,003 kilometra. Ponieważ niedziela jest w Azerbejdżanie dniem pamięci narodowej, rywalizację przeniesiono na sobotę.',
        'Formula1.com i Sky Sports potwierdzają, że Kimi Antonelli wywalczył pole position z czasem 1:40.445, wyprzedzając George’a Russella i blokując cały pierwszy rząd dla Mercedesa. Włoch prowadzi w klasyfikacji generalnej z 292 punktami.',
        'Charles Leclerc w Ferrari ruszy z trzeciego pola obok Lando Norrisa z McLarena, a Lewis Hamilton zajmie piątą pozycję. Prędkości rzędu 350 km/h na prostej Neftchilar oraz wąski fragment przy baszcie o szerokości zaledwie 7,6 metra będą kluczem do sukcesu.',
      ],
    },
    zh: {
      title: '巴库正赛日：安东内利携手拉塞尔包揽梅赛德斯头排发车位',
      subtitle: '超级新秀力夺杆位，与队友并肩作战。51圈街道激战穿越老城古堡与里海超长直道。',
      excerpt: 'F1阿塞拜疆大奖赛正赛于周六在巴库城市赛道打响。车手积分榜领跑者基米·安东内利从杆位起步，梅赛德斯队友拉塞尔位列次席。',
      body: [
        '9月26日周六，F1阿塞拜疆大奖赛在全长6.003公里的巴库城市赛道迎来正赛决战。为尊重阿塞拜疆周日的国家烈士纪念日，本站大奖赛提前24小时于周六举行。',
        '据Formula1.com与天空体育报道，梅赛德斯新秀安东内利在周五排位赛跑出1分40秒445斩获杆位，与队友拉塞尔携手锁定头排发车区。安东内利以292分在车手积分榜领先81分。',
        '法拉利车手勒克莱尔与迈凯伦车手诺里斯分列第三、第四位占据第二排，汉密尔顿第五。赛车将在2.2公里的涅夫捷扬尼科夫大道直道飙至350公里时速，并在古堡狭窄的第8弯接受极致考验。',
      ],
    },
    ja: {
      title: 'バクー決勝日：アントネッリがラッセルとメルセデス最前列独占で51周の激闘へ',
      subtitle: '新星ルーキーがポールポジション獲得。旧市街の古城とカスピ海ストレートを駆け抜ける51周。',
      excerpt: 'F1アゼルバイジャンGP決勝が土曜日にバクー市街地コースで開催される。ポイントリーダーのアントネッリがPPから発進、ラッセルが2番手に並ぶ。',
      body: [
        '9月26日土曜日、F1第17戦アゼルバイジャンGPが6.003キロのバクー市街地コースで決勝日を迎えた。日曜日に追悼記念日を迎えるため、決勝レースは土曜日に前倒しされて争われる。',
        'Formula1.comとSky Sportsによると、メルセデスのキミ・アントネッリが予選で1分40秒445を記録しポールポジションを獲得、ラッセルとともにフロントローを独占した。アントネッリは292ポイントでランキング首位に立つ。',
        'フェラーリのルクレールが3番手、マクラーレンのノリスが4番手で2列目に並び、ハミルトンが5番手から追う。最高時速350キロに達する長いストレートと幅7.6メートルの城壁セクションが勝負を左右する。',
      ],
    },
    ko: {
      title: '바쿠 레이스 데이: 안토넬리, 러셀과 함께 메르세데스 1열 독점 후 51랩 결전',
      subtitle: '슈퍼 루키 안토넬리 폴포지션 획득. 고대 성벽과 카스피해 직선 주로를 질주하는 51랩 결승전.',
      excerpt: '포뮬러 1 아제르바이잔 그랑프리 결승 레이스가 토요일 바쿠 시티 서킷에서 펼쳐진다. 챔피언십 선두 안토넬리가 폴에서 출발하며 팀 동료 러셀이 2위를 차지했다.',
      body: [
        '포뮬러 1은 9월 26일 토요일 바쿠 시티 서킷의 6.003km 코스에서 대망의 결승전을 치른다. 아제르바이잔의 일요일 국가 추모일을 고려해 결승 레이스가 24시간 앞당겨 열린다.',
        'Formula1.com과 스카이 스포츠에 따르면 메르세데스의 키미 안토넬리가 예선에서 1분 40초 445로 폴포지션을 획득했으며 조지 러셀이 2위로 첫 줄을 완성했다. 안토넬리는 292점으로 챔피언십 선두를 굳건히 지키고 있다.',
        '페라리의 샤를 르클레르와 맥라렌의 랜도 노里斯가 두 번째 줄에서 출발하며 루이스 해밀턴이 5위에 자리했다. 시속 350km에 달하는 2.2km 직선 주로와 7.6m에 불과한 8번 성벽 코너에서 치열한 승부가 기대된다.',
      ],
    },
    ar: {
      title: 'يوم سباق باكو: أنتونيللي يقود ثنائية مرسيدس في الصف الأول لمعركة من 51 لفة',
      subtitle: 'الموهبة الصاعدة يحصد قطب الانطلاق إلى جانب راسل. 51 لفة عالية السرعة حول القلعة القديمة ومستقيم قزوين.',
      excerpt: 'تنطلق فورمولا 1 في شوارع باكو اليوم السبت على حلبة باكو سيتي. ينطلق متصدر البطولة كيمي أنتونيللي من المركز الأول وزميله جورج راسل ثانيًا.',
      body: [
        'تبلغ فورمولا 1 ذروة الإثارة في يوم السباق يوم السبت 26 أيلول/سبتمبر على حلبة باكو سيتي البالغ طولها 6.003 كيلومترات. ونظرًا لإحياء يوم الذكرى الوطني في أذربيجان يوم الأحد، تم تقديم موعد السباق 24 ساعة.',
        'أفادت تقارير Formula1.com وسكاي سبورتس بأن كيمي أنتونيللي انتزع قطب الانطلاق الأول يوم الجمعة بزمن قدره 1:40.445 متقدمًا على زميله جورج راسل ليضمنا الصف الأول لمرسيدس. يتصدر أنتونيللي البطولة برصيد 292 نقطة.',
        'ينطلق شارل لوكلير سائق فيراري ثالثًا إلى جانب لاندو نوريس سائق مكلارين من الصف الثاني، بينما يبدأ لويس هاميلتون خامسًا. وستحدد السرعات القصوى على مستقيم نفتشيلار والمنعطفات الضيقة حول القلعة هوية الفائز.',
      ],
    },
  },
  'laver-cup-day2-london-2026': {
    fr: {
      title: 'Laver Cup Jour 2 : Alcaraz, Zverev et Fritz en vedette pour le samedi à deux points à l’O2',
      subtitle: 'Les victoires valent double à Londres. Noah et Agassi peaufinent leurs duels avec l’objectif des 13 points.',
      excerpt: 'La 9e Laver Cup prend une nouvelle dimension ce samedi à l’O2 Arena de Londres. Avec deux points par victoire, Alcaraz, Zverev et Fritz s’affrontent sur le court noir.',
      body: [
        'La 9e Laver Cup entre dans sa phase décisive ce samedi 26 septembre sous les projecteurs de l’O2 à Londres. Le barème double aujourd’hui, chaque match remporté rapportant deux points au compteur.',
        'LaverCup.com et Sky Sports ont publié l’ordre des rencontres établi par Yannick Noah et Andre Agassi. Après un premier jour équilibré, la tension monte d’un cran dans la capitale britannique.',
        'Carlos Alcaraz ouvre la session de jour pour l’Europe face au finaliste de l’US Open Taylor Fritz. Alexander Zverev défie ensuite l’Australien Alex de Minaur dans un duel d’une grande intensité en fond de court.',
      ],
    },
    es: {
      title: 'Laver Cup Día 2: Alcaraz, Zverev y Fritz protagonizan el sábado de doble puntuación en el O2',
      subtitle: 'Los puntos valen doble en Londres. Noah y Agassi perfilan los duelos sabatinos rumbo a los 13 puntos.',
      excerpt: 'La 9ª Laver Cup acelera en su segunda jornada en el O2 Arena de Londres. Con dos puntos por victoria, Carlos Alcaraz, Alexander Zverev y Taylor Fritz asumen el protagonismo.',
      body: [
        'La 9ª Laver Cup llega a su punto culminante este sábado 26 de septiembre en la pista negra del O2 de Londres. Las reglas estipulan que los triunfos de hoy otorgan dos puntos, frente al punto concedido el viernes.',
        'LaverCup.com y Sky Sports publicaron el orden de juego confeccionado por los capitanes Yannick Noah y Andre Agassi. El equilibrio de la jornada inaugural da paso a choques de máxima exigencia.',
        'Carlos Alcaraz abre la sesión diurna por Europa frente a Taylor Fritz, referente del Equipo Mundo. En el segundo turno, el campeón del US Open Alexander Zverev medirá fuerzas con el australiano Alex de Minaur.',
      ],
    },
    de: {
      title: 'Laver Cup Tag 2: Alcaraz, Zverev und Fritz im Fokus am Samstag mit doppelten Punkten',
      subtitle: 'Siege bringen zwei Zähler in London. Noah und Agassi stellen Top-Duelle vor dem Erreichen der 13 Punkte auf.',
      excerpt: 'Der 9. Laver Cup geht am Samstag in The O2 in London in Tag 2. Mit zwei Punkten pro Sieg stehen Alcaraz, Zverev und Fritz auf dem schwarzen Hallenboden im Mittelpunkt.',
      body: [
        'Der 9. Laver Cup erreicht am Samstag, dem 26. September, in London seinen heißesten Abschnitt. Die Spielregeln verdoppeln heute den Wert jedes Sieges von einem auf zwei Zähler pro Match.',
        'LaverCup.com und Sky Sports veröffentlichten die Aufstellungen der Kapitäne Yannick Noah und Andre Agassi. Nach einem packenden Auftakt am Freitag geht es heute um insgesamt acht Zähler.',
        'Carlos Alcaraz bestreitet das Eröffnungseinzel für Europa gegen Taylor Fritz. Anschließend trifft US-Open-Sieger Alexander Zverev auf Alex de Minaur in einem mitreißenden Grundlinienduell.',
      ],
    },
    it: {
      title: 'Laver Cup Giorno 2: Alcaraz, Zverev e Fritz protagonisti del sabato da due punti all’O2',
      subtitle: 'Punti doppi a Londra. Noah e Agassi schierano i big verso il traguardo dei 13 punti.',
      excerpt: 'La 9ª Laver Cup entra nel vivo questo sabato all’O2 Arena di Londra. Con due punti per vittoria, Carlos Alcaraz, Alexander Zverev e Taylor Fritz illuminano il campo nero.',
      body: [
        'La 9ª Laver Cup affronta il suo snodo cruciale sabato 26 settembre sul campo nero dell’O2 di Londra. Il regolamento assegna oggi due punti per ciascuna vittoria rispetto al punto singolo del venerdì.',
        'LaverCup.com e Sky Sports hanno annunciato il programma stabilito dai capitani Yannick Noah e Andre Agassi. La parità della giornata inaugurale cede il passo a sfide di altissimo livello agonistico.',
        'Carlos Alcaraz apre la sessione diurna per il Team Europe contro Taylor Fritz. A seguire, il trionfatore degli US Open Alexander Zverev sfida l’australiano Alex de Minaur in una maratona da fondo campo.',
      ],
    },
    pl: {
      title: 'Puchar Lavera Dzień 2: Alcaraz, Zverev i Fritz na czele podwójnie punktowanej soboty w O2',
      subtitle: 'Punkty liczą się podwójnie w Londynie. Noah i Agassi ustalają sobotnie hity w drodze do 13 punktów.',
      excerpt: '9. Puchar Lavera nabiera tempa w drugim dniu w londyńskiej O2 Arena. Za zwycięstwo przyznawane są dwa punkty, a na korcie pojawią się Alcaraz, Zverev i Fritz.',
      body: [
        '9. edycja Pucharu Lavera wkracza w decydującą fazę w sobotę 26 września pod dachem hali The O2 w Londynie. Zgodnie z formatem turnieju punkty za wygrane mecze ulegają podwojeniu.',
        'LaverCup.com i Sky Sports opublikowały plan gier na sobotę ustalony przez kapitanów Yannicka Noah i Andre Agassiego. Dzisiejsze cztery starcia wyłonią faworyta przed niedzielnym finałem.',
        'Carlos Alcaraz otwiera sesję dzienną dla Europy meczem z finalistą US Open Taylorem Fritzem. Następnie mistrz US Open Alexander Zverev zmierzy się z nieustępliwym Alexem de Minaurem.',
      ],
    },
    zh: {
      title: '拉沃尔杯次日：阿尔卡拉斯、兹维列夫与弗里茨领衔周六双倍积分大战',
      subtitle: '伦敦现场积分翻倍。诺阿与阿加西布阵周六焦点对决，向13分夺冠目标冲刺。',
      excerpt: '第9届拉沃尔杯周六在伦敦O2体育馆进入第二日角逐。随着每场胜利提升至2分，阿尔卡拉斯、兹维列夫和弗里茨在黑色球场全力出击。',
      body: [
        '9月26日周六，第9届拉沃尔杯在伦敦O2体育馆迎来积分倍增的关键次日比赛。根据赛事规则，周六每场比赛胜利将计入2分，今日四场比赛总计产生8分。',
        '拉沃尔杯官网与天空体育公布了由诺阿和阿加西敲定的周六出场名单。首日的胶着让周六的交锋更具火药味。',
        '世界第二阿尔卡拉斯率先代表欧洲队登场，迎战世界队头号球星弗里茨。随后，美网新科冠军兹维列夫与澳大利亚名将德米纳尔展开底线攻防决战。',
      ],
    },
    ja: {
      title: 'レーバーカップ2日目：アルカラス、ズベレフ、フリッツがO2で2点マッチの土曜決戦へ',
      subtitle: '土曜日は勝利ごとに2ポイント。ノアとアガシが13点到達を見据えて主力を投入。',
      excerpt: '第9回レーバーカップは土曜日、ロンドンのThe O2で第2日を迎えた。勝利ごとに2点が付与される重要な日程でアルカラスとズベレフが登場する。',
      body: [
        '第9回レーバーカップは9月26日土曜日、ロンドンのThe O2で重要な第2日目に突入した。大会規定により土曜日の勝利は1勝につき2ポイントが与えられる。',
        '大会公式とSky Sportsによると、主将のヤニック・ノアとアンドレ・アガシが土曜のオーダーを発表。初日の競り合いを経て、一気に点差を広げたい両陣営の思惑が激突する。',
        'デイセッション第1試合では欧州代表のアルカラスが全米準優勝のフリッツと対戦。続く第2試合では全米王者ズベレフが俊足のデミノーと熱戦を繰り広げる。',
      ],
    },
    ko: {
      title: '레이버컵 2일차: 알카라스, 츠베레프, 프리츠가 나서는 O2의 더블 포인트 토요일',
      subtitle: '런던 결전서 승점 2점씩 걸린다. 노아와 애거시, 13점 고지를 향해 주전 총출동.',
      excerpt: '제9회 레이버컵이 토요일 영국 런던 O2 아레나에서 2일차 일정에 돌입했다. 경기당 승점 2점이 걸린 가운데 알카라스와 츠베레프가 블랙 코트에 오른다.',
      body: [
        '제9회 레이버컵은 9월 26일 토요일 런던 The O2에서 승부의 분수령을 맞는다. 대회 규정에 따라 토요일 승리는 금요일의 1점에서 2점으로 두 배 가치를 지닌다.',
        'LaverCup.com과 스카이 스포츠에 따르면 야닉 노아와 안드레 애거시 주장은 핵심 카드를 꺼내 들었다. 1일차 팽팽한 흐름을 깨기 위해 양 팀 모두 총력을 기울인다.',
        '낮 세션 첫 경기에서 유럽의 카를로스 알카라스가 팀 월드의 테일러 프리츠와 맞붙는다. 이어 US 오픈 챔피언 알렉산더 츠베레프가 알렉스 드 미노와 혈투를 벌인다.',
      ],
    },
    ar: {
      title: 'كأس ليفر اليوم الثاني: ألكاراز وزفيريف وفريتز يتصدرون سبت النقاط المضاعفة في The O2',
      subtitle: 'الفوز يمنح نقطتين في لندن. نوح وأغاسي يعلنان مواجهات السبت سعيًا لبلوغ 13 نقطة.',
      excerpt: 'تتسارع أحداث النسخة التاسعة من كأس ليفر يوم السبت في صالة The O2 في لندن. مع احتساب نقطتين لكل انتصار، يشعل ألكاراز وزفيريف وفريتز الحماس على الملعب الأسود.',
      body: [
        'تبلغ بطولة كأس ليفر التاسعة ذروة الإثارة يوم السبت 26 أيلول/سبتمبر تحت أضواء The O2 في لندن. وبموجب لوائح البطولة تتضاعف قيمة الفوز اليوم إلى نقطتين.',
        'أعلن الموقع الرسمي للبطولة وشبكة سكاي سبورتس جدول مباريات السبت الذي وضعه القائدان يانيك نوح وأندريه أغاسي. وتمنح مباريات اليوم دفعة هائلة نحو الـ13 نقطة الحاسمة.',
        'يفتتح كارلوس ألكاراز منافسات النهار ممثلًا لأوروبا أمام تايلور فريتز نجم فريق العالم، يليه بطل أمريكا المفتوحة ألكسندر زفيريف في مواجهة صعبة ضد الأسترالي أليكس دي مينور.',
      ],
    },
  },
  'presidents-cup-day3-moving-day-2026': {
    fr: {
      title: 'Presidents Cup Jour 3 : Medinah n° 3 teste l’endurance pour un moving day à 8 points',
      subtitle: 'Double session ce samedi : four-balls le matin et foursomes l’après-midi. Scheffler et Scott en fers de lance.',
      excerpt: 'La 16e Presidents Cup aborde le moving day au Medinah Country Club en Illinois. Une double session éreintante met en jeu huit points cruciaux avant les simples de dimanche.',
      body: [
        'Le samedi de la Presidents Cup est reconnu comme la journée la plus exigeante du calendrier golfique. Sur 36 trous au Medinah Country Club, huit matches sont disputés pour attribuer plus d’un quart des 30 points du tournoi.',
        'PGA Tour et PresidentsCup.com indiquent que Brandt Snedeker et Geoff Ogilvy ont dévoilé leurs duos matinaux. Les États-Unis s’appuient sur Scottie Scheffler et Collin Morikawa pour défier Adam Scott et Min Woo Lee.',
        'Patrick Cantlay et Xander Schauffele affrontent ensuite Hideki Matsuyama et Sungjae Im. Sur les greens fermes de Medinah, la précision et la gestion de la fatigue feront la différence.',
      ],
    },
    es: {
      title: 'Presidents Cup Día 3: Medinah nº 3 pone a prueba la resistencia en un moving day de 8 puntos',
      subtitle: 'Doble sesión el sábado: four-balls por la mañana y foursomes por la tarde. Scheffler y Scott lideran a sus equipos.',
      excerpt: 'La 16ª Presidents Cup afronta la jornada clave en Medinah Country Club en Illinois. Una intensa doble sesión pone en juego ocho puntos vitales antes de los individuales del domingo.',
      body: [
        'El sábado en la Presidents Cup es la jornada más exigente del golf por equipos. A lo largo de 36 hoyos en el recorrido nº 3 de Medinah, se disputan ocho partidos entre four-balls y foursomes.',
        'PGA Tour y PresidentsCup.com informan de las alineaciones matinales elegidas por Brandt Snedeker y Geoff Ogilvy. El número 1 mundial Scottie Scheffler y Collin Morikawa abren ante Adam Scott y Min Woo Lee.',
        'Patrick Cantlay y Xander Schauffele se miden a Hideki Matsuyama y Sungjae Im en el segundo turno. El diseño exigente de Medinah castigará cualquier error con los hierros.',
      ],
    },
    de: {
      title: 'Presidents Cup Tag 3: Medinah Kurs Nr. 3 fordert Ausdauer am 8-Punkte-Moving-Day',
      subtitle: 'Doppelsession am Samstag: Four-Balls am Vormittag und Foursomes am Nachmittag. Scheffler und Scott als Säulen.',
      excerpt: 'Der 16. Presidents Cup erreicht den entscheidenden Moving Day im Medinah Country Club in Illinois. Acht wichtige Punkte stehen vor den Sonntags-Einzeln auf dem Spiel.',
      body: [
        'Der Samstag beim Presidents Cup gilt als die anstrengendste Phase im Teamgolf. Über 36 Löcher auf Medinahs Kurs Nr. 3 stehen acht Duelle an, die mehr als ein Viertel aller 30 Punkte vergeben.',
        'PGA Tour und PresidentsCup.com berichten über die Aufstellungen der Kapitäne Brandt Snedeker und Geoff Ogilvy. Die Nummer 1 Scottie Scheffler spielt mit Collin Morikawa gegen Adam Scott und Min Woo Lee.',
        'Patrick Cantlay und Xander Schauffele duellieren sich mit Hideki Matsuyama und Sungjae Im. Auf den schnellen Grüns von Medinah entscheiden Präzision und Nervenstärke.',
      ],
    },
    it: {
      title: 'Presidents Cup Giorno 3: il percorso n. 3 di Medinah testa la tenuta in un moving day da 8 punti',
      subtitle: 'Doppia sessione di sabato: four-ball al mattino e foursome al pomeriggio. Scheffler e Scott pilastri delle squadre.',
      excerpt: 'La 16ª Presidents Cup affronta il cruciale moving day al Medinah Country Club in Illinois. Una doppia sessione mette in palio otto punti prima dei singoli di domenica.',
      body: [
        'Il sabato della Presidents Cup è universalmente considerato la giornata più dura del golf internazionale. Su 36 buche a Medinah vengono disputati otto incontri che assegnano oltre un quarto dei punti complessivi.',
        'PGA Tour e PresidentsCup.com segnalano le coppie mattutine scelte da Brandt Snedeker e Geoff Ogilvy. Il numero 1 Scottie Scheffler e Collin Morikawa aprono contro Adam Scott e Min Woo Lee.',
        'Patrick Cantlay e Xander Schauffele sfidano Hideki Matsuyama e Sungjae Im nel secondo incontro. I green ridisegnati da OCM Golf premieranno solo i colpi più precisi.',
      ],
    },
    pl: {
      title: 'Puchar Prezydentów Dzień 3: Medinah Course No. 3 sprawdza siły w 8-punktowym moving day',
      subtitle: 'Podwójna sesja w sobotę: four-ball rano i foursome po południu. Scheffler i Scott liderami ekip.',
      excerpt: '16. Puchar Prezydentów wkracza w decydującą fazę w Medinah Country Club w Illinois. Wyczerpująca sobota przynosi osiem kluczowych punktów przed niedzielnymi singlami.',
      body: [
        'Sobota w Pucharze Prezydentów to tradycyjnie najbardziej wymagający dzień w kalendarzu golfowym. Na dystansie 36 dołków pola Course No. 3 w Medinah zostanie rozegranych osiem meczów.',
        'PGA Tour i PresidentsCup.com donoszą o zestawieniach wybranych przez kapitanów Snedekera i Ogilvy’ego. Scottie Scheffler w parze z Collinem Morikawą grają przeciwko Adamowi Scottowi i Min Woo Lee.',
        'W drugim meczu Patrick Cantlay i Xander Schauffele rywalizują z Hidekim Matsuyamą i Sungjae Imem. Trudne ukształtowanie greenów wymaga bezbłędnej strategii.',
      ],
    },
    zh: {
      title: '2026总统杯第3日：梅迪纳3号球场迎来8分大决战移动日',
      subtitle: '周六双重赛程：上午四球赛加下午四人两球赛。舍夫勒与斯科特分别坐镇。',
      excerpt: '第16届总统杯在伊利诺伊州梅迪纳乡村俱乐部迎来决定走势的移动日。全天36洞马拉松双重赛程将在周日单人对决前决出8个关键积分。',
      body: [
        '总统杯周六向来被公认为高尔夫赛场上最具考验的一天。在梅迪纳3号球场进行的36洞较量中，全天八场四球与四人两球赛将瓜分赛事30个总积分中超过四分之一的分值。',
        '据美巡赛与总统杯官方消息，斯内德克与奥格维派出了顶尖组合。世界第一舍夫勒与森川搭档在上午四球赛迎战国际队老将斯科特与李旻宇。',
        '坎特利与肖夫勒将对阵松山英树与任成宰。在梅迪纳起伏剧烈的坚硬果岭上，推杆稳定度与体能分配将直接决定谁能在周日前占据主动。',
      ],
    },
    ja: {
      title: 'プレジデンツカップ3日目：メディナ3番コースで8ポイントを懸けた移動日決戦',
      subtitle: '土曜は午前フォアボールと午後フォアサムのダブルセッション。シェフラーとスコットが牽引。',
      excerpt: '第16回プレジデンツカップは米メディナCCで重要なムービングデーを迎えた。日曜のシングルスを前に、36ホールの激闘で8つの勝ち点を争う。',
      body: [
        'プレジデンツカップの土曜日は、ゴルフ界で最もタフな移動日として知られる。メディナ3番コースを舞台に計36ホール・8マッチが行われ、総得点30のうち8点が動く。',
        'PGAツアーおよび大会公式によると、スネデカー主将とオギルビー主将が朝のペアを発表。世界ランク1位のシェフラーがモリカワと組み、アダム・スコットとミンウー・リーのペアと対戦する。',
        'カントレーとシャウフレの米ペアは松山英樹とイム・ソンジェのアジア最強タッグと激突。改修された難関グリーンを攻略したチームが勝利を引き寄せる。',
      ],
    },
    ko: {
      title: '프레지던츠컵 3일차: 메디나 3번 코스서 8점이 걸린 무빙 데이 마라톤',
      subtitle: '토요일 더블 세션: 오전 포볼 및 오후 포섬 경기. 셰플러와 애덤 스콧 각 팀 견인.',
      excerpt: '제16회 프레지던츠컵이 미국 메디나 컨트리클럽에서 승부의 분수령인 무빙 데이에 돌입했다. 일요일 싱글 매치를 앞두고 8점의 승점이 걸린 36홀 승부가 펼쳐진다.',
      body: [
        '프레지던츠컵 토요일은 팀 골프에서 가장 체력 소모가 큰 일정이다. 메디나 3번 코스에서 포볼과 포섬에 걸쳐 36홀 동안 8개 매치가 치러지며 전체 30점 중 8점이 걸려 있다.',
        'PGA 투어와 대회 공식 사이트에 따르면 스네데커와 오길비 단장은 오전 조합을 확정했다. 세계 1위 스코티 셰플러와 콜린 모리카와가 애덤 스콧, 이민우 조와 격돌한다.',
        '패트릭 캔틀리와 잰더 쇼플리는 마쓰야마 히데키와 임성재 조를 상대한다. 메디나의 빠르고 굴곡진 그린에서 정교한 샷 메이킹이 승패를 가를 전망이다.',
      ],
    },
    ar: {
      title: 'كأس الرؤساء اليوم الثالث: ملعب مادينا رقم 3 يختبر اللياقة في يوم حاسم بـ8 نقاط',
      subtitle: 'جلسة مزدوجة السبت: أربع كرات صباحًا وضربات متناوبة بعد الظهر. شيفلر وسكوت يقودان الدفاع.',
      excerpt: 'تدخل النسخة الـ16 من كأس الرؤساء يومها الفاصل في نادي مادينا في إلينوي. 8 نقاط كاملة على المحك قبل مواجهات الفردي المقررة الأحد.',
      body: [
        'يعد يوم السبت في كأس الرؤساء الأكثر صعوبة وإرهاقًا للاعبي الجولف. تقام 8 مواجهات على مدار 36 حفرة في ملعب مادينا رقم 3 تمثل أكثر من ربع نقاط البطولة الثلاثين.',
        'أفادت تقارير جولة بي جي إيه والموقع الرسمي للبطولة باختيار القائدين سنديكر وأوجيلفي تشكيلات قوية. يشارك المصنف الأول سكوتي شيفلر مع كولين موريكاوا ضد آدم سكوت ومين وو لي.',
        'يواجه باتريك كانتلاي وزاندر شوفيلي الثنائي الآسيوي هيديكي ماتسوياما وسونغجاي إم. وتتطلب المساحات الرملية والمنحدرات دقة متناهية للحفاظ على التقدم.',
      ],
    },
  },
  'premier-league-matchweek-6-saturday': {
    fr: {
      title: 'Premier League 6e journée : City reçoit Newcastle alors que la course au titre se resserre',
      subtitle: 'Les leaders invaincus de Guardiola défient les Magpies à l’Etihad. Arsenal et Brighton à l’affût.',
      excerpt: 'La 6e journée de Premier League débute ce samedi avec Manchester City qui défend son bilan parfait face à Newcastle. Arsenal et Liverpool cherchent à mettre la pression.',
      body: [
        'La Premier League dispute sa 6e journée ce samedi 26 septembre avec Manchester City seul au sommet grâce à cinq victoires en cinq matches. Avec Arsenal et Brighton en embuscade, la journée s’annonce capitale.',
        'PremierLeague.com et Sky Sports détaillent le programme en Angleterre. À l’Etihad Stadium, City reçoit Newcastle en fin d’après-midi. Les hommes de Guardiola comptent 15 points après leur victoire 5-3 contre Sunderland, portés par Erling Haaland.',
        'Dans les autres rencontres, Arsenal accueille Everton à l’Emirates pour réagir après son revers à Brighton. Chelsea affronte Brighton à Stamford Bridge, tandis que Liverpool vise la victoire à Anfield face à Sunderland.',
      ],
    },
    es: {
      title: 'Premier League jornada 6: City recibe a Newcastle con la pugna por el título al rojo vivo',
      subtitle: 'El líder impecable de Guardiola se mide a las Urracas en el Etihad. Arsenal y Brighton buscan presionar.',
      excerpt: 'La 6ª jornada de la Premier League arranca este sábado con el Manchester City defendiendo su pleno de victorias frente al Newcastle United.',
      body: [
        'La Premier League alcanza su 6ª jornada este sábado 26 de septiembre con el Manchester City como único equipo con cinco triunfos en cinco partidos. Arsenal y Brighton siguen de cerca sus pasos.',
        'PremierLeague.com y Sky Sports destacan el duelo de la tarde en el Etihad Stadium entre el City y el Newcastle. El conjunto de Guardiola suma 15 puntos tras vencer 5-3 al Sunderland con tantos de Haaland y Semenyo.',
        'En el resto de la jornada sabatina, el Arsenal recibe al Everton en el Emirates tras caer en Brighton, mientras que el Chelsea se mide a un sorprendente Brighton en Stamford Bridge y Liverpool recibe a Sunderland.',
      ],
    },
    de: {
      title: 'Premier League Spieltag 6: City empfängt Newcastle im heißen Titelrennen',
      subtitle: 'Guardiolas makelloser Tabellenführer trifft im Etihad auf die Magpies. Arsenal und Brighton lauern.',
      excerpt: 'Der 6. Spieltag der Premier League beginnt am Samstag: Manchester City verteidigt seine weiße Weste gegen Newcastle United.',
      body: [
        'Die Premier League startet am Samstag, dem 26. September, in ihren 6. Spieltag. Manchester City steht mit fünf Siegen aus fünf Partien unangefochten an der Spitze, verfolgt von Arsenal und Brighton.',
        'PremierLeague.com und Sky Sports blicken auf das Spitzenspiel im Etihad Stadium zwischen City und Newcastle. City hält bei 15 Punkten nach dem spektakulären 5:3 gegen Sunderland, angeführt von Erling Haaland.',
        'Arsenal empfängt Everton im Emirates Stadium nach der 0:3-Niederlage in Brighton, während Chelsea an der Stamford Bridge auf Brighton trifft und Liverpool gegen Sunderland um drei Punkte kämpft.',
      ],
    },
    it: {
      title: 'Premier League 6ª giornata: il City ospita il Newcastle mentre la corsa al vertice si infiamma',
      subtitle: 'I capolisti a punteggio pieno di Guardiola affrontano i Magpies all’Etihad. Arsenal e Brighton all’inseguimento.',
      excerpt: 'La 6ª giornata di Premier League scatta sabato con il Manchester City che difende il percorso netto contro il Newcastle United.',
      body: [
        'La Premier League celebra la 6ª giornata sabato 26 settembre con il Manchester City unica formazione a punteggio pieno dopo cinque turni. Arsenal e Brighton restano a stretto contatto.',
        'PremierLeague.com e Sky Sports presentano la sfida dell’Etihad tra City e Newcastle. La squadra di Guardiola viaggia a quota 15 punti dopo il pirotecnico 5-3 sul Sunderland trascinata da Erling Haaland.',
        'Nelle altre partite di sabato, l’Arsenal attende l’Everton all’Emirates per riscattare il ko di Brighton, il Chelsea ospita il Brighton a Stamford Bridge e il Liverpool cerca conferme contro il Sunderland ad Anfield.',
      ],
    },
    pl: {
      title: 'Premier League 6. kolejka: City podejmuje Newcastle w zaciętej walce o fotel lidera',
      subtitle: 'Niepokonani liderzy Guardioli mierzą się ze Srokami na Etihad. Arsenal i Brighton polują na potknięcie.',
      excerpt: '6. kolejka Premier League rusza w sobotę: Manchester City broni kompletu punktów w starciu z Newcastle United.',
      body: [
        'Premier League wkracza w 6. kolejkę w sobotę 26 września, a Manchester City pozostaje jedynym klubem z kompletem pięciu zwycięstw. Za jego plecami czają się Arsenal i rewelacyjne Brighton.',
        'PremierLeague.com i Sky Sports zapowiadają popołudniowe starcie na Etihad Stadium. City ma 15 punktów po wygranej 5-3 z Sunderlandem, w czym kluczową rolę odegrał niezawodny Erling Haaland.',
        'W innych meczach soboty Arsenal podejmuje Everton na Emirates po porażce w Brighton, Chelsea mierzy się z Brighton na Stamford Bridge, a Liverpool gra u siebie z Sunderlandem.',
      ],
    },
    zh: {
      title: '英超第6轮：曼城坐镇伊蒂哈德迎战纽卡斯尔，争冠悬念升级',
      subtitle: '瓜迪奥拉的全胜领头羊迎战喜鹊。阿森纳与布莱顿周六全速追赶。',
      excerpt: '英超第6轮于周六打响，豪取五连胜的曼城主场迎战纽卡斯尔联。阿森纳与利物浦在各条战线展开追击。',
      body: [
        '9月26日周六，英超联赛迎来第6轮较量。曼城以五战全胜积15分独自领跑积分榜，阿森纳、布莱顿及追赶梯队紧随其后。',
        '英超官网与天空体育报道，瓜迪奥拉的球队将在伊蒂哈德球场迎战纽卡斯尔联。上一轮曼城5-3力克桑德兰，哈兰德持续进球状态，给亚伊斯勒的后防线带来严峻考验。',
        '在周六的其他对决中，阿森纳坐镇酋长球场迎战埃弗顿力求重返胜利轨道；切尔西在斯坦福桥硬碰状态火热的布莱顿，利物浦则在安菲尔德迎战桑德兰。',
      ],
    },
    ja: {
      title: 'プレミアリーグ第6節：シティがエティハドでニューカッスルを迎撃、首位争い激化',
      subtitle: '開幕5連勝のグアルディオラ率いる首位チームがマグパイズと対戦。アーセナルとブライトンが追撃。',
      excerpt: 'プレミアリーグ第6節が土曜日に開幕。全勝を守るマンチェスター・シティがホームでニューカッスル・ユナイテッドを迎え撃つ。',
      body: [
        'プレミアリーグは9月26日土曜日に第6節を迎えた。開幕から5戦全勝のマンチェスター・シティが単独首位を快走し、アーセナルとブライトンが追う展開となっている。',
        'プレミアリーグ公式とSky Sportsによると、首位シティはエティハドでニューカッスルと激突。前節サンダーランドを5-3で下したシティは、毎試合得点を記録しているハーランドを中心に攻撃陣が絶好調。',
        '土曜の他会場では、ブライトン戦の敗戦から立ち直りを図るアーセナルがエバートンと対戦。チェルシーは好調ブライトンをスタンフォード・ブリッジに迎え、リバプールはサンダーランドと対戦する。',
      ],
    },
    ko: {
      title: '프리미어리그 6라운드: 맨시티, 뉴캐슬 상대 안방 수성 나서며 선두 경쟁 가열',
      subtitle: '과르디올라의 5전 전승 선두 팀, 에티하드서 매그파이스와 격돌. 아스널과 브라이턴 맹추격.',
      excerpt: '프리미어리그 6라운드가 토요일 개막한다. 100% 승률을 달리는 맨체스터 시티가 홈에서 뉴캐슬 유나이티드를 맞이한다.',
      body: [
        '프리미어리그는 9월 26일 토요일 6라운드 일정에 돌입했다. 맨체스터 시티가 5전 전승 승점 15점으로 단독 선두를 질주하는 가운데 아스널과 브라이턴이 바짝 뒤를 쫓고 있다.',
        '프리미어리그 공식과 스카이 스포츠에 따르면 시티는 에티하드 스타디움에서 뉴캐슬과 맞대결을 펼친다. 선덜랜드를 5-3으로 제압한 시티는 매 경기 골을 터뜨리는 홀란을 앞세워 6연승을 노린다.',
        '토요일 다른 경기에서는 브라이턴전 패배를 만회하려는 아스널이 에버턴을 홈으로 불러들이고, 첼시는 스탬퍼드 브리지에서 돌풍의 브라이턴을 상대하며 리버풀은 선덜랜드와 맞붙는다.',
      ],
    },
    ar: {
      title: 'الدوري الإنجليزي الجولة 6: مانشستر سيتي يستضيف نيوكاسل مع اشتعال سباق الصدارة',
      subtitle: 'كتيبة غوارديولا بالعلامة الكاملة تواجه نيوكاسل في الاتحاد. أرسنال وبرايتون يتربصان.',
      excerpt: 'تنطلق الجولة السادسة من الدوري الإنجليزي الممتاز يوم السبت حيث يدافع مانشستر سيتي عن سجله الخالي من الهزائم أمام نيوكاسل يونايتد.',
      body: [
        'تصل منافسات الدوري الإنجليزي الممتاز إلى الجولة السادسة يوم السبت 26 أيلول/سبتمبر، حيث ينفرد مانشستر سيتي بالصدارة بخمسة انتصارات من خمس مباريات.',
        'أفادت تقارير الموقع الرسمي للبطولة وسكاي سبورتس بمواجهة مرتقبة على ملعب الاتحاد بين السيتي ونيوكاسل. يملك السيتي 15 نقطة بعد فوزه المثير 5-3 على سندرلاند بفضل تألق إيرلينغ هالاند المستمر.',
        'وفي مواجهات السبت الأخرى، يستضيف أرسنال فريق إيفرتون في ملعب الإمارات للتعافي من خسارة برايتون، بينما يلتقي تشيلسي مع برايتون في ستامفورد بريدج، ويستقبل ليفربول فريق سندرلاند في أنفيلد.',
      ],
    },
  },
  'packers-falcons-week3-final-2026': {
    fr: {
      title: 'Les Packers résistent aux Falcons 24-20 : Love brille pour l’Alumni Weekend avant le dimanche de NFL',
      subtitle: 'Jordan Love inscrit trois touchdowns à Lambeau. Penix lance pour 268 yards pour son retour. Bills-Dolphins et Chiefs-Chargers en approche.',
      excerpt: 'Le Thursday Night Football de la 3e semaine voit Green Bay battre Atlanta 24-20 à Lambeau Field. Jordan Love signe trois touchdowns tandis que la NFL se tourne vers dimanche.',
      body: [
        'La 3e semaine de NFL a débuté sous les projecteurs de Lambeau Field avec la victoire 24-20 des Packers de Green Bay face aux Falcons d’Atlanta. Green Bay passe à 2-1 en tête de la NFC Nord avant une grande journée dominicale.',
        'NFL.com et Packers.com rapportent que Jordan Love a brillé devant cinquante légendes du club pour l’Alumni Weekend. Love a lancé deux passes de touchdown pour Christian Watson et Romeo Doubs, avant d’ajouter un touchdown au sol de 4 yards au troisième quart-temps.',
        'Michael Penix Jr. a réalisé une prestation remarquable pour son retour de blessure avec 268 yards à la passe et un touchdown vers Drake London. Une interception tardive de Xavier McKinney a scellé le sort d’Atlanta. Dimanche, Allen et les Bills défient les Dolphins à Highmark, tandis que Mahomes et les Chiefs accueillent les Chargers.',
      ],
    },
    es: {
      title: 'Los Packers frenan a los Falcons 24-20: Love brilla en el Alumni Weekend rumbo al domingo de NFL',
      subtitle: 'Jordan Love anota tres touchdowns en Lambeau. Penix suma 268 yardas en su regreso. Bills-Dolphins y Chiefs-Chargers en el horizonte.',
      excerpt: 'El Thursday Night Football de la semana 3 finaliza con victoria de Green Bay 24-20 sobre Atlanta en Lambeau Field. Jordan Love suma tres touchdowns mientras la NFL mira al domingo.',
      body: [
        'La semana 3 de la NFL arrancó en horario de máxima audiencia en Lambeau Field con el triunfo de los Green Bay Packers por 24-20 ante los Atlanta Falcons. Green Bay se sitúa 2-1 al frente de la NFC Norte.',
        'NFL.com y Packers.com informan de la gran actuación de Jordan Love ante medio centenar de leyendas históricas en el Alumni Weekend. Love lanzó dos pases de anotación para Watson y Doubs y anotó otra marca terrestre de 4 yardas en el tercer cuarto.',
        'Michael Penix Jr. completó 268 yardas y un touchdown hacia Drake London en su regreso, pero una intercepción decisiva de Xavier McKinney aseguró el festejo local. Todas las miradas apuntan ahora a los duelos dominicales Bills-Dolphins y Chiefs-Chargers.',
      ],
    },
    de: {
      title: 'Packers bezwingen Falcons 24-20: Love glänzt am Alumni-Wochenende vor heißem NFL-Sonntag',
      subtitle: 'Jordan Love erzielt drei Touchdowns im Lambeau Field. Penix wirft für 268 Yards bei Rückkehr. Bills-Dolphins und Chiefs-Chargers im Fokus.',
      excerpt: 'Das Thursday Night Football der 3. Woche endet mit einem 24-20-Erfolg der Green Bay Packers über die Atlanta Falcons. Jordan Love verbucht drei Touchdowns.',
      body: [
        'Die 3. NFL-Woche begann am Donnerstagabend im Lambeau Field mit einem hart erkämpften 24-20-Sieg der Green Bay Packers gegen die Atlanta Falcons. Green Bay rückt mit 2-1 an die Spitze der NFC North vor.',
        'NFL.com und Packers.com berichten von einer starken Vorstellung von Jordan Love vor 50 Vereinslegenden am Alumni-Wochenende. Love warf zwei Touchdowns auf Watson und Doubs und lief im dritten Viertel selbst über vier Yards in die Endzone.',
        'Falcons-Quarterback Michael Penix Jr. überzeugte bei seinem Comeback mit 268 Passing Yards und einem Touchdown auf Drake London, ehe eine späte Interception von Xavier McKinney die Niederlage besiegelte. Am Sonntag folgen die Topspiele Bills gegen Dolphins und Chiefs gegen Chargers.',
      ],
    },
    it: {
      title: 'I Packers superano i Falcons 24-20: Love protagonista all’Alumni Weekend verso la domenica NFL',
      subtitle: 'Jordan Love firma tre touchdown a Lambeau. Penix lancia per 268 yard al rientro. All’orizzonte Bills-Dolphins e Chiefs-Chargers.',
      excerpt: 'Il Thursday Night Football della Week 3 si chiude con il successo di Green Bay per 24-20 su Atlanta al Lambeau Field. Jordan Love trascina i suoi con tre touchdown.',
      body: [
        'La Week 3 della NFL si è aperta nel prime time del Lambeau Field con la vittoria dei Green Bay Packers per 24-20 sugli Atlanta Falcons. Green Bay sale a 2-1 in vetta alla NFC North.',
        'NFL.com e Packers.com celebrano la prova maiuscola di Jordan Love davanti a 50 leggende del club per l’Alumni Weekend. Love ha lanciato due mete per Watson e Doubs e segnato un touchdown su corsa da 4 yard nel terzo quarto.',
        'Michael Penix Jr. ha risposto al rientro con 268 yard e un touchdown per Drake London, ma un intercetto nel finale di Xavier McKinney ha blindato il successo dei padroni di casa. La NFL si prepara ora alle sfide domenicali tra Bills e Dolphins e tra Chiefs e Chargers.',
      ],
    },
    pl: {
      title: 'Packers pokonują Falcons 24-20: Love bohaterem Alumni Weekend przed niedzielnymi meczami NFL',
      subtitle: 'Jordan Love notuje trzy przyłożenia na Lambeau Field. Penix rzuca 268 jardów po powrocie. W niedzielę hity Bills-Dolphins i Chiefs-Chargers.',
      excerpt: 'Mecz Thursday Night Football 3. tygodnia kończy się wygraną Green Bay Packers 24-20 nad Atlanta Falcons. Jordan Love zapisuje trzy przyłożenia na swoje konto.',
      body: [
        'Tydzień 3 ligi NFL rozpoczął się na Lambeau Field, gdzie Green Bay Packers odnieśli cenne zwycięstwo 24-20 nad Atlanta Falcons. Wygrana daje Packers bilans 2-1 i prowadzenie w dywizji NFC North.',
        'Według relacji NFL.com i Packers.com Jordan Love rozegrał znakomity mecz w obecności kilkudziesięciu legend klubu. Rozgrywający rzucił dwa przyłożenia do Watsona i Doubsa oraz dołożył 4-jardowy bieg na pole punktowe w trzeciej kwarcie.',
        'Michael Penix Jr. zaliczył udany powrót po kontuzji, zdobywając 268 jardów podaniowych i przyłożenie z Drake’em Londonem. Przechwyt Xaviera McKinneya w końcówce przypieczętował jednak sukces gospodarzy przed niedzielnymi hitami Bills z Dolphins oraz Chiefs z Chargers.',
      ],
    },
    zh: {
      title: '包装工24-20险胜猎鹰：勒夫校友周末轰出三达阵，NFL周日大战触手可及',
      subtitle: '乔丹·勒夫兰博球场贡献三达阵。佩尼克斯伤愈复出传出268码。比尔对海豚与酋长战闪电引人瞩目。',
      excerpt: 'NFL第3周周四夜赛在兰博球场收官，绿湾包装工24-20击退亚特兰大猎鹰。乔丹·勒夫独造三达阵，联盟目光全面转向周日决战。',
      body: [
        'NFL第3周在兰博球场的聚光灯下打响，绿湾包装工以24-20力克亚特兰大猎鹰。凭借这场硬仗的胜利，包装工以2胜1负升至国联北区头名，拉开了精彩周末的序幕。',
        '据NFL官网与包装工官方报道，勒夫在五十余位队史名宿见证的校友周末打出统治级表现。他先后传球助攻沃森和道布斯达阵，并在第三节完成4码冲球达阵得分。',
        '猎鹰四分卫佩尼克斯伤愈复出表现抢眼，34传22中砍下268码并连线伦敦达阵。但麦金尼在关键时刻的抄截终结了逆转悬念。周日联盟将迎来比尔对阵海豚以及酋长迎战闪电的重头戏。',
      ],
    },
    ja: {
      title: 'パッカーズがファルコンズを24-20で撃破：ラブが3TDの活躍、注目の日曜決戦へ',
      subtitle: 'ジョーダン・ラブがランボー・フィールドで3TDを記録。復帰のペニックスも268ヤードを投球。ビルズ対ドルフィンズなど好カード控える。',
      excerpt: 'NFL第3週のサーズデーナイトフットボールはグリーンベイ・パッカーズが24-20でアトランタ・ファルコンズに競り勝った。ラブが3つのタッチダウンをマーク。',
      body: [
        'NFL第3週は伝統のランボー・フィールドで幕を開け、グリーンベイ・パッカーズが24-20でアトランタ・ファルコンズを退けた。パッカーズは今季成績を2勝1敗としてNFC北地区首位に立った。',
        'NFL.comによると、同校OBら多くのレジェンドが集うアルムナイ・ウィークエンドでQBジョーダン・ラブが大活躍。パスで2つのTDを演出し、第3クォーターには自らの4ヤードランでTDを決めた。',
        '膝の手術から復帰したファルコンズのペニックスも268ヤード1TDと奮闘したが、マッキニーのインターセプトが勝敗を決した。視線は早くも日曜日のビルズ対ドルフィンズやチーフス対チャージャーズへと向かう。',
      ],
    },
    ko: {
      title: '패커스, 팰컨스에 24-20 진땀승: 러브의 3TD 맹활약 속 NFL 일요일 격전 카운트다운',
      subtitle: '조던 러브 램보 필드서 터치다운 3개 작렬. 복귀전 페닉스 268패싱야드 기록. 빌스-돌핀스 및 치프스-차저스 격돌 임박.',
      excerpt: 'NFL 3주차 서스데이 나이트 풋볼에서 그린베이 패커스가 애틀랜타 팰컨스를 24-20으로 꺾었다. 조던 러브가 터치다운 3개를 책임지며 일요일 경기 기대감을 높였다.',
      body: [
        'NFL 3주차 경기는 램보 필드의 화려한 조명 아래 펼쳐졌으며, 그린베이 패커스가 애틀랜타 팰컨스를 24-20으로 제압했다. 패커스는 2승 1패로 NFC 북부지구 선두로 올라섰다.',
        'NFL 공식 홈페이지에 따르면 조던 러브는 50여 명의 구단 레전드들이 모인 동문 주간 경기에서 맹활약했다. 러브는 패스 터치다운 2개를 성공시킨 데 이어 3쿼터 4야드 러싱 터치다운까지 성공시켰다.',
        '부상에서 돌아온 팰컨스의 마이클 페닉스 주니어도 268패싱야드로 분전했으나 매키니의 결정적인 가로채기로 패배를 안았다. 이제 관심은 일요일 열리는 빌스 대 돌핀스, 치프스 대 차저스의 대결로 쏠린다.',
      ],
    },
    ar: {
      title: 'باكرز يتفوق على فالكونز 24-20: لوف يتألق في عطلة الأساطير قبل جولة الأحد المرتقبة',
      subtitle: 'جوردان لوف يسجل ثلاثة تاتش داون في لامبو فيلد. بينيكس يحقق 268 ياردة عند عودته. مواجهات نارية تنتظر بيلز وتشييفس.',
      excerpt: 'انتهت مواجهة الخميس في الأسبوع الثالث من دوري كرة القدم الأمريكية بفوز غرين باي باكرز على أتلانتا فالكونز 24-20. سجل لوف ثلاثة تاتش داون مع التطلع لمباريات الأحد.',
      body: [
        'انطلق الأسبوع الثالث من دوري كرة القدم الأمريكية ليلة الخميس على ملعب لامبو فيلد العريق، حيث حقق غرين باي باكرز انتصارًا قويًا على أتلانتا فالكونز بنتيجة 24-20 ليعزز صدارته لمجموعته برصيد 2-1.',
        'أفادت تقارير NFL.com بأن جوردان لوف قدم عرضًا استثنائيًا أمام أكثر من خمسين أسطورة من قدامى لاعبي النادي، حيث مرر كرتين حاسمتين وسجل بنفسه من ركضة لمسافة 4 ياردات في الربع الثالث.',
        'من جانبه، تألق مايكل بينيكس العائد من الإصابة محققًا 268 ياردة وتمريرة تاتش داون لدريك لندن، قبل أن يحسم اعتراض زافير ماكيني الفوز لباكرز. وتتجه الأنظار الآن نحو قمم الأحد بين بيلز ودولفينز وتشييفس ضد تشارجرز.',
      ],
    },
  },
  'wnba-playoffs-2026-countdown-round1': {
    fr: {
      title: 'Playoffs WNBA 2026 : compte à rebours de 24 heures avant le coup d’envoi de dimanche',
      subtitle: 'Le premier tour débute dimanche 27 septembre. Minnesota tête de série à 32-10, les Valkyries impressionnent, le Fever défie le Dream.',
      excerpt: 'Il ne reste que 24 heures avant le lancement des playoffs WNBA 2026 ce dimanche 27 septembre. Le tableau à huit équipes réunit les plus grandes stars du basket féminin.',
      body: [
        'La saison régulière WNBA 2026 est terminée et le tableau des playoffs est en place. Ce dimanche 27 septembre, huit équipes débutent leur quête du titre suprême dans un premier tour au meilleur des trois manches.',
        'WNBA.com et ESPN ont officialisé les têtes de série après une fin de saison palpitante. Les Minnesota Lynx s’avancent avec le statut de numéro un grâce à leur bilan de 32-10 et la meilleure défense de la ligue. Les Golden State Valkyries décrochent la deuxième place à 31-11 pour leur deuxième année d’existence.',
        'Les Las Vegas Aces d’A’ja Wilson occupent la 3e place à 29-13. Le choc du premier tour opposera l’Atlanta Dream, 4e à 28-14, à l’Indiana Fever de Caitlin Clark, 5e à 27-15. Les séries débutent ce dimanche sur les parquets américains.',
      ],
    },
    es: {
      title: 'Playoffs WNBA 2026: cuenta atrás de 24 horas para el inicio del domingo con Lynx y Valkyries al frente',
      subtitle: 'La primera ronda arranca el domingo 27 de septiembre. Minnesota lidera con 32-10, las Valkyries brillan y Fever visita a Dream.',
      excerpt: 'Apenas restan 24 horas para que arranquen las eliminatorias por el título de la WNBA este domingo 27 de septiembre con los ocho mejores equipos en liza.',
      body: [
        'La temporada regular de la WNBA ha concluido y el cuadro de postemporada está listo. El domingo 27 de septiembre, ocho franquicias inician la primera ronda al mejor de tres partidos en busca del trofeo de campeonas.',
        'WNBA.com y ESPN confirmaron el cuadro final. Las Minnesota Lynx parten como primeras cabezas de serie con un balance de 32-10 y una defensa imponente. Las Golden State Valkyries firman la segunda plaza con 31-11 en apenas su segundo año en la competición.',
        'Las vigentes campeonas Las Vegas Aces ocupan la tercera plaza con 29-13, mientras que el Dream de Atlanta (28-14) recibirá en una serie apasionante al Indiana Fever de Caitlin Clark (27-15). La carrera por el anillo de 2026 arranca este domingo.',
      ],
    },
    de: {
      title: 'WNBA-Playoffs 2026: 24-Stunden-Countdown vor dem Sonntags-Auftakt mit Lynx und Valkyries',
      subtitle: 'Erste Runde startet am Sonntag, 27. September. Minnesota topgesetzt mit 32-10, Valkyries überzeugen, Fever gastiert bei Dream.',
      excerpt: 'Nur noch 24 Stunden bis zum Start der WNBA-Playoffs 2026 am Sonntag, dem 27. September. Acht Teams kämpfen im K.o.-Modus um die Meisterschaft.',
      body: [
        'Die reguläre Saison der WNBA 2026 ist abgeschlossen und die Playoff-Bühne bereitet. Am Sonntag, dem 27. September, eröffnen acht Teams die erste Runde im Best-of-Three-Modus im Rennen um die Krone.',
        'WNBA.com und ESPN bestätigten die Setzliste nach einem packenden Saisonfinale. Die Minnesota Lynx gehen mit einer Bilanz von 32-10 als Nummer eins ins Rennen. Die Golden State Valkyries sicherten sich in ihrem zweiten Jahr sensationell Rang zwei mit 31-11.',
        'Titelverteidiger Las Vegas Aces folgt auf Platz drei mit 29-13. Ein echtes Highlight verspricht das Duell zwischen Atlanta Dream (28-14) und den Indiana Fever um Caitlin Clark (27-15). Vier mitreißende Serien beginnen am Sonntag.',
      ],
    },
    it: {
      title: 'Playoff WNBA 2026: conto alla rovescia di 24 ore verso la palla a due di domenica',
      subtitle: 'Il primo turno scatta domenica 27 settembre. Minnesota prima testa di serie a 32-10, le Valkyries stupiscono, Fever contro Dream.',
      excerpt: 'Mancano solo 24 ore all’inizio dei playoff WNBA 2026 di domenica 27 settembre. Il tabellone a otto squadre mette in palio il titolo supremo.',
      body: [
        'La regular season della WNBA 2026 è agli archivi e la post-season è pronta a decollare. Domenica 27 settembre otto formazioni scendono sul parquet per il primo turno al meglio delle tre gare.',
        'WNBA.com ed ESPN hanno ufficializzato le posizioni della griglia playoff. Le Minnesota Lynx si presentano come prima testa di serie assoluta con un record di 32-10. Al secondo posto brillano le Golden State Valkyries a 31-11 al loro secondo anno di vita.',
        'Le campionesse in carica delle Las Vegas Aces sono terze a 29-13, mentre l’Atlanta Dream (28-14) sfiderà l’Indiana Fever di Caitlin Clark (27-15) nella serie più attesa. La corsa al titolo parte domenica.',
      ],
    },
    pl: {
      title: 'Play-off WNBA 2026: 24 godziny do niedzielnego startu, Lynx i Valkyries na czele stawki',
      subtitle: 'Pierwsza runda rusza w niedzielę 27 września. Minnesota numerem jeden z bilansem 32-10, Valkyries zachwycają, Fever gra z Dream.',
      excerpt: 'Już tylko 24 godziny dzielą nas od startu fazy play-off ligi WNBA w niedzielę 27 września. Osiem najlepszych zespołów rozpoczyna walkę o mistrzostwo.',
      body: [
        'Sezon zasadniczy WNBA 2026 dobiegł końca i znamy pełną drabinkę play-off. W niedzielę 27 września osiem klubów zainauguruje rywalizację w pierwszej rundzie rozgrywanej w formule do dwóch zwycięstw.',
        'WNBA.com i ESPN potwierdziły rozstawienie po emocjonującej końcówce sezonu. Minnesota Lynx przystępują do gry z pierwszego miejsca z imponującym bilansem 32-10. Rewelacyjne Golden State Valkyries zajęły drugie miejsce z wynikiem 31-11.',
        'Obrończynie tytułu Las Vegas Aces są rozstawione z numerem trzecim (29-13), a w hicie pierwszej rundy Atlanta Dream (28-14) podejmie Indiana Fever z Caitlin Clark (27-15). Wielka gra o mistrzostwo startuje w niedzielę.',
      ],
    },
    zh: {
      title: '2026年WNBA季后赛：周日揭幕战进入24小时倒计时，山猫与女武神领衔争冠阵营',
      subtitle: '首轮将于9月27日周日打响。明尼苏达32胜10负锁定头号种子，金州女武神队史第二年跃居次席，狂热挑战梦想。',
      excerpt: '距离2026年WNBA季后赛9月27日周日打响仅剩24小时。八强对阵落定，山猫、女武神、王牌与狂热等队伍展开首轮三局两胜角逐。',
      body: [
        '2026年WNBA常规赛正式圆满收官，季后赛大幕即将拉开。9月26日进入最后24小时倒计时，八支季后赛劲旅将在9月27日周日开启三局两胜制的首轮争夺。',
        '据WNBA官网与ESPN报道，明尼苏达山猫以32胜10负傲视群雄夺得全联盟头号种子席位。建队仅第二年的金州女武神表现抢眼，以31胜11负高居第二号种子。',
        '卫冕冠军拉斯维加斯王牌以29胜13负排在第三位。首轮最受瞩目的对决当属四号种子亚特兰大梦想（28胜14负）迎战凯特琳·克拉克领衔的五号种子印第安纳狂热（27胜15负）。周日四场大戏连台，总冠军追逐战全面打响。',
      ],
    },
    ja: {
      title: 'WNBAプレーオフ2026：開幕まで24時間カウントダウン、リンクスとヴァルキリーズが牽引',
      subtitle: '1回戦は9月27日日曜日に開幕。ミネソタが32勝10敗で第1シード、ヴァルキリーズ躍進、フィーバーがドリームに挑む。',
      excerpt: '9月27日日曜日に開幕する2026年WNBAプレーオフまであと24時間。8チームによる3戦2勝制の第1ラウンドが始まります。',
      body: [
        '2026年WNBAレギュラーシーズンが終了し、プレーオフの組み合わせが決定した。9月27日日曜日、選ばれし8チームが3戦2勝制のファーストラウンドで王座を目指す戦いを始める。',
        'WNBA公式とESPNの発表によると、強固な守備を誇るミネソタ・リンクスが32勝10敗で全体第1シードを獲得。参入2年目のゴールデンステート・ヴァルキリーズが31勝11敗で第2シードに躍進した。',
        '連覇を狙うラスベガス・エーシズが29勝13敗で第3シード。最大の注目カードは第4シードのアトランタ・ドリームとケイトリン・クラーク擁するインディアナ・フィーバーの一戦。日曜日のティップオフが迫る。',
      ],
    },
    ko: {
      title: '2026 WNBA 플레이오프: 일요일 개막 앞두고 24시간 카운트다운, 링스와 발키리스 선두 질주',
      subtitle: '1라운드 9월 27일 일요일 개막. 미네소타 32승 10패로 1번 시드, 발키리스 2년차 돌풍, 피버 대 드림 격돌.',
      excerpt: '9월 27일 일요일 시작되는 2026 WNBA 플레이오프까지 24시간 남았다. 미네소타, 골든스테이트, 라스베이거스, 인디애나 등 8개 팀이 우승컵을 향해 격돌한다.',
      body: [
        '2026 WNBA 정규리그가 모두 마무리되고 플레이오프 대진표가 완성되었다. 9월 27일 일요일, 8개 구단이 3전 2선승제의 1라운드에 돌입해 치열한 승부를 펼친다.',
        'WNBA 공식 발표에 따르면 미네소타 링스가 32승 10패로 전체 1번 시드를 거머쥐었다. 창단 2년차를 맞은 골든스테이트 발키리스는 31승 11패로 2번 시드에 오르는 기염을 토했다.',
        '디펜딩 챔피언 라스베이거스 에이시스가 29승 13패로 3번 시드를 차지한 가운데, 4번 시드 애틀랜타 드림과 케이틀린 클라크가 이끄는 5번 시드 인디애나 피버의 맞대결이 가장 큰 관심을 모은다. 우승을 향한 여정이 일요일 시작된다.',
      ],
    },
    ar: {
      title: 'أدوار WNBA الإقصائية 2026: العد التنازلي لـ24 ساعة قبل ضربة بداية الأحد بقيادة لينكس وفالكيريز',
      subtitle: 'تنطلق الجولة الأولى الأحد 27 أيلول/سبتمبر. مينيسوتا تتصدر بـ32-10، وفالكيريز تبهر الجميع، وفيفر يحل ضيفًا على دريم.',
      excerpt: 'لم يتبق سوى 24 ساعة على انطلاق الأدوار الإقصائية لدوري السلة الأمريكي للسيدات WNBA يوم الأحد 27 أيلول/سبتمبر بمشاركة ثمانية فرق تتنافس على اللقب.',
      body: [
        'اختتم الموسم المنتظم لدوري السلة الأمريكي للسيدات 2026 واكتملت خريطة الأدوار الإقصائية. تنطلق المنافسات يوم الأحد 27 أيلول/سبتمبر بمواجهات الجولة الأولى الأفضل من بين ثلاث مباريات.',
        'أكدت تقارير WNBA.com وإي إس بي إن تصدر مينيسوتا لينكس الترتيب برصيد 32-10 بالمركز الأول بفضل أقوى دفاع في البطولة. واحتل فريق غولدن ستيت فالكيريز المركز الثاني برصيد 31-11 في موسمه الثاني فقط.',
        'وجاء حامل اللقب لاس فيغاس إيسيز ثالثًا بـ29-13، بينما تترقب الجماهير قمة أتلانتا دريم صاحب المركز الرابع ضد إنديانا فيفر بقيادة كيتلين كلارك. ساعات قليلة تفصلنا عن صافرة البداية يوم الأحد.',
      ],
    },
  },
};



