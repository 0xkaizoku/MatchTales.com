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
};

