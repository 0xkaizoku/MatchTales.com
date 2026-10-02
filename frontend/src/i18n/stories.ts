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
  'antonelli-wins-baku-gp-2026': {
    fr: {
      title: 'Antonelli triomphe à Bakou depuis la pole : doublé magistral de Mercedes',
      subtitle: 'Le prodige italien signe sa 9e victoire de 2026. Russell 2e, Leclerc 3e. 88 points d’avance au championnat.',
      excerpt: 'Kimi Antonelli s’impose au Grand Prix d’Azerbaïdjan devant son coéquipier George Russell, scellant un éclatant doublé Mercedes dans les rues de Bakou.',
      body: [
        'Le Grand Prix d’Azerbaïdjan s’est achevé samedi 26 septembre avec une démonstration éclatante de Kimi Antonelli sur le tracé de Bakou.',
        'Parti de la pole position, le rookie de 19 ans a maîtrisé la dégradation de ses gommes et résisté à la pression de George Russell sur l’avenue Neftchilar. Une relance parfaite après la voiture de sécurité au 44e tour lui a permis de l’emporter en 1:31:28.412.',
        'Russell prend la deuxième place à 2,184 secondes pour valider le doublé Mercedes, tandis que Charles Leclerc monte sur le podium pour Ferrari. Antonelli totalise désormais 317 points au championnat du monde.',
      ],
    },
    es: {
      title: 'Antonelli gana en Bakú desde la pole: doblete dominante de Mercedes',
      subtitle: 'Novena victoria de 2026 para la joven promesa. Russell 2º, Leclerc 3º. Ventaja de 88 puntos en el Mundial.',
      excerpt: 'Kimi Antonelli triunfa en el Gran Premio de Azerbaiyán por delante de George Russell, logrando un contundente doblete de Mercedes en el trazado urbano de Bakú.',
      body: [
        'El Gran Premio de Azerbaiyán culminó con una actuación magistral de Kimi Antonelli en las desafiantes calles del circuito de Bakú.',
        'Saliendo desde la pole, el piloto italiano de 19 años resistió los envites de George Russell y gestionó con maestría la zona estrecha del castillo. Tras el auto de seguridad tardío, cruzó la meta en 1:31:28.412.',
        'Russell completó el 1-2 de las flechas plateadas a 2,184 segundos, con Charles Leclerc completando el podio para Ferrari. Antonelli amplía su liderato en el campeonato de pilotos a 317 puntos.',
      ],
    },
    de: {
      title: 'Antonelli siegt in Baku von der Pole: Dominanter Mercedes-Doppelsieg',
      subtitle: 'Neunter Saisonsieg für das Ausnahmetalent. Russell P2, Leclerc P3. WM-Vorsprung wächst auf 88 Punkte.',
      excerpt: 'Formel-1-Spitzenreiter Kimi Antonelli gewinnt den Großen Preis von Aserbaidschan vor Teamkollege George Russell auf dem schnellen Stadtkurs in Baku.',
      body: [
        'Der Große Preis von Aserbaidschan bot am Samstag einen triumphalen Renntag für Kimi Antonelli und das Mercedes-Team auf dem Baku City Circuit.',
        'Von der Pole Position gestartet, behauptete der 19-jährige Italiener die Führung auf der 2,2 km langen Neftchilar-Geraden und meisterte die enge Altstadt-Passage fehlerfrei. Er siegte nach 51 Runden in 1:31:28.412.',
        'George Russell folgte 2,184 Sekunden dahinter und sicherte den Doppelsieg ab. Charles Leclerc belegte im Ferrari den dritten Platz. Antonelli baut seine WM-Führung auf 317 Punkte aus.',
      ],
    },
    it: {
      title: 'Antonelli trionfa a Baku dalla pole: doppietta capolavoro per la Mercedes',
      subtitle: 'Nono trionfo stagionale per il giovane fenomeno. Russell 2°, Leclerc 3°. Il vantaggio sale a 88 punti.',
      excerpt: 'Kimi Antonelli domina il Gran Premio d’Azerbaigian precedendo George Russell sul circuito cittadino di Baku per una spettacolare doppietta Mercedes.',
      body: [
        'Il Gran Premio d’Azerbaigian si è chiuso con il trionfo assoluto di Kimi Antonelli sul velocissimo tracciato cittadino di Baku.',
        'Scattato dalla pole position, il talento bolognese ha controllato la gara con grande freddezza, gestendo le insidie della curva 8 e l’usura gomme sul rettilineo del Caspio, chiudendo in 1:31:28.412.',
        'Russell taglia il traguardo secondo a 2,184 secondi completando l’uno-due Mercedes, con Charles Leclerc terzo per la Ferrari. Antonelli vola nel Mondiale a quota 317 punti.',
      ],
    },
    pl: {
      title: 'Antonelli wygrywa w Baku z pole position: dublet Mercedesa na ulicach miasta',
      subtitle: 'Dziewiąte zwycięstwo młodego talentu w 2026 roku. Russell 2., Leclerc 3. Przewaga w klasyfikacji wzrasta do 88 punktów.',
      excerpt: 'Lider mistrzostw świata Kimi Antonelli triumfuje w Grand Prix Azerbejdżanu przed George’em Russellem, dając Mercedesowi pewny dublet w Baku.',
      body: [
        'Sobotnie Grand Prix Azerbejdżanu przyniosło kolejny bezbłędny występ debiutującego Kimiego Antonellego na torze ulicznym w Baku.',
        'Startując z pole position, 19-letni Włoch utrzymał prowadzenie na długiej prostej Neftchilar i precyzyjnie pokonał ciasny odcinek przy zamku, wygrywając z czasem 1:31:28.412.',
        'George Russell finiszował ze stratą 2,184 sekundy, a podium uzupełnił Charles Leclerc z Ferrari. Antonelli pewnie przewodzi klasyfikacji kierowców z dorobkiem 317 punktów.',
      ],
    },
    zh: {
      title: '安东内利杆位起步问鼎巴库大奖赛：梅赛德斯街道赛包揽冠亚军',
      subtitle: '超级新秀斩获赛季第九冠。拉塞尔位居次席，勒克莱尔第三。车手榜领跑优势扩大至88分。',
      excerpt: 'F1车手积分榜榜首安东内利在巴库城市赛道杆位发车夺得阿塞拜疆大奖赛冠军，携手队友拉塞尔助梅赛德斯包揽冠亚军。',
      body: [
        '周六在巴库城市赛道打响的F1阿塞拜疆大奖赛正赛中，安东内利再次展现出无可挑剔的赛道掌控力。',
        '这位19岁超新星从杆位启航，在2.2公里长的里海超长直道上顶住了队友拉塞尔与勒克莱尔的追击，并在狭窄古堡区保持零失误，最终以1小时31分28秒412率先撞线。',
        '拉塞尔落后2.184秒获得亚军，法拉利车手勒克莱尔登上领奖台第三位。本场胜利使安东内利的个人积分升至317分，梅赛德斯车队以546分遥遥领先。',
      ],
    },
    ja: {
      title: 'アントネッリがバクーでPPトゥウィン：メルセデスが市街地戦でワンツー達成',
      subtitle: '新星ルーキーが今季9勝目をマーク。ラッセル2位、ルクレール3位。ポイント差を88点に拡大。',
      excerpt: 'F1ポイントリーダーのアントネッリがアゼルバイジャンGPでポール・トゥ・ウィンを達成、ラッセルとともにメルセデスのワンツーフィニッシュを飾った。',
      body: [
        'バクー市街地コースで開催されたアゼルバイジャンGP決勝は、メルセデスのキミ・アントネッリによる圧巻の走りで幕を閉じた。',
        'ポールから好発進を決めた19歳のアントネッリは、時速350キロに達するカスピ海ストレートと難所ターン8の古城セクションを完璧に攻略し、1時間31分28秒412で優勝。',
        '2.184秒差でラッセルが2位に入りメルセデスが1-2フィニッシュを達成、ルクレールが3位に入った。アントネッリはドライバーズ選手権で317点までリードを広げた。',
      ],
    },
    ko: {
      title: '안토넬리, 바쿠 GP 폴투윈 달성: 메르세데스 도심 서킷 원투 피니시 완성',
      subtitle: '슈퍼 루키 안토넬리 시즌 9승째 수확. 러셀 2위, 르클레르 3위. 챔피언십 88점 차 선두 질주.',
      excerpt: 'F1 챔피언십 선두 안토넬리가 아제르바이잔 그랑프리에서 폴투윈을 기록하며 팀 동료 조지 러셀과 함께 메르세데스 원투 피니시를 이끌었다.',
      body: [
        '바쿠 시티 서킷에서 펼쳐진 아제르바이잔 그랑프리는 키미 안토넬리의 완벽한 독주 속에 메르세데스의 축제로 끝났다.',
        '폴포지션에서 출발한 19세의 안토넬리는 2.2km 직선 주로의 거센 압박과 성벽 코너의 난코스를 무결점으로 방어하며 1시간 31분 28초 412의 기록으로 체커기를 받았다.',
        '러셀이 2.184초 차 2위로 결승선을 통과하며 메르세데스 원투를 완성했고 페라리의 르클레르가 3위에 올랐다. 안토넬리는 이번 승리로 시즌 317점을 쌓았다.',
      ],
    },
    ar: {
      title: 'أنتونيللي يحرز سباق باكو من قطب الانطلاق: مرسيدس تحكم سيطرتها بثنائية في شوارع العاصمة',
      subtitle: 'الفوز التاسع هذا الموسم للموهبة الصاعدة. راسل ثانيًا ولوكلير ثالثًا. الفارق في الصدارة يرتفع إلى 88 نقطة.',
      excerpt: 'كيمي أنتونيللي يتوج بلقب جائزة أذربيجان الكبرى متفوقًا على زميله جورج راسل ليمنحا مرسيدس ثنائية استثنائية على حلبة باكو.',
      body: [
        'اختتمت منافسات جائزة أذربيجان الكبرى لسباقات فورمولا 1 بعرض مذهل من كيمي أنتونيللي الذي ترجم انطلاقه من المركز الأول إلى انتصار ثمين.',
        'نجح السائق الإيطالي الشاب في إدارة تآكل الإطارات ببراعة على مستقيم نفتشيلار والمنعطفات التاريخية حول القلعة القديمة، ليعبر خط النهاية بزمن قدره 1:31:28.412.',
        'حل زميله جورج راسل ثانيًا بفارق 2.184 ثانية ليحققا ثنائية تاريخية لمرسيدس، وجاء شارل لوكلير ثالثًا مع فيراري. ورفع أنتونيللي رصيده في صدارة البطولة إلى 317 نقطة.',
      ],
    },
  },
  'laver-cup-day3-championship-sunday-2026': {
    fr: {
      title: 'Laver Cup Jour 3 Finale : dimanche à trois points à l’O2 avec le trophée en jeu',
      subtitle: 'Chaque victoire rapporte trois points à Londres. Alcaraz et Zverev mènent l’Europe face à Fritz et De Minaur.',
      excerpt: 'La 9e Laver Cup se conclut ce dimanche à l’O2 Arena de Londres. Avec trois points par victoire, l’Europe et le Monde s’affrontent pour le sacre.',
      body: [
        'La 9e Laver Cup atteint son apogée ce dimanche 27 septembre sous la coupole de l’O2 à Londres, où chaque match rapporte désormais trois points précieux.',
        'Les capitaines Yannick Noah et Andre Agassi ont désigné leurs champions pour cette dernière ligne droite. Carlos Alcaraz et Alexander Zverev ouvrent le bal en double face à Taylor Fritz et Alex de Minaur.',
        'Les simples décisifs opposeront ensuite Alcaraz à De Minaur, puis Zverev à Fritz. La première équipe atteignant 13 points soulèvera le prestigieux trophée.',
      ],
    },
    es: {
      title: 'Laver Cup Día 3 Final: domingo de triple puntuación en el O2 con el título en juego',
      subtitle: 'Cada partido vale tres puntos en Londres. Alcaraz y Zverev lideran a Europa frente a Fritz y De Minaur.',
      excerpt: 'La 9ª Laver Cup culmina este domingo en el O2 de Londres. Con tres puntos por triunfo, Europa y el Resto del Mundo disputan la corona.',
      body: [
        'El desenlace de la 9ª Laver Cup se vive este domingo 27 de septiembre en el O2 Arena de Londres, donde las victorias pasan a premiarse con tres puntos.',
        'Los capitanes Yannick Noah y Andre Agassi definieron un programa estelar. Carlos Alcaraz y Alexander Zverev unen fuerzas en el dobles inaugural ante Taylor Fritz y Alex de Minaur.',
        'A continuación se disputarán los duelos individuales entre Alcaraz y De Minaur, y entre Zverev y Fritz. El primer equipo que alcance los 13 puntos se proclamará campeón.',
      ],
    },
    de: {
      title: 'Laver Cup Tag 3 Finale: Dreifache Punkte am Sonntag in London um die Trophäe',
      subtitle: 'Jeder Sieg bringt drei Punkte in der O2 Arena. Alcaraz und Zverev fordern Fritz und De Minaur.',
      excerpt: 'Der 9. Laver Cup gipfelt am Sonntag in der O2 Arena in London. Bei drei Punkten pro Match kämpfen Team Europe und Team World um den Titel.',
      body: [
        'Der 9. Laver Cup steuert am Sonntag, dem 27. September, in der Londoner O2 Arena auf seinen dramatischen Höhepunkt zu, da Siege heute dreifach gewertet werden.',
        'Die Kapitäne Yannick Noah und Andre Agassi schicken ihre stärksten Kräfte ins Rennen. Alcaraz und Zverev eröffnen im Doppel gegen Fritz und De Minaur.',
        'In den anschließenden Einzeln trifft Alcaraz auf De Minaur und Zverev auf Fritz. Wer zuerst 13 Punkte verbucht, gewinnt den Laver Cup 2026.',
      ],
    },
    it: {
      title: 'Laver Cup Giorno 3 Finale: domenica da tre punti all’O2 con il trofeo in palio',
      subtitle: 'Ogni vittoria vale tre punti a Londra. Alcaraz e Zverev guidano l’Europa contro Fritz e De Minaur.',
      excerpt: 'La 9ª Laver Cup si decide domenica all’O2 di Londra. Con tre punti a match, Team Europe e Team World lottano per il titolo.',
      body: [
        'La 9ª Laver Cup vive il suo atto conclusivo domenica 27 settembre all’O2 Arena di Londra, dove ogni successo assegna ben tre punti in classifica.',
        'I capitani Yannick Noah e Andre Agassi hanno annunciato le formazioni. Carlos Alcaraz e Alexander Zverev giocano insieme nel doppio inaugurale contro Fritz e De Minaur.',
        'Seguiranno le sfide singolari tra Alcaraz e De Minaur e tra Zverev e Fritz. La prima squadra a quota 13 punti alzerà il trofeo.',
      ],
    },
    pl: {
      title: 'Laver Cup Dzień 3 Finał: potrójne punkty w O2 i walka o mistrzostwo',
      subtitle: 'Każdy mecz wart trzy punkty w Londynie. Alcaraz i Zverev kontra Fritz i De Minaur.',
      excerpt: '9. edycja Laver Cup kończy się w niedzielę w londyńskiej O2 Arena. Punkty mnożone razy trzy wyłonią tegorocznego triumfatora.',
      body: [
        'Finałowy dzień Pucharu Lavera w niedzielę 27 września w O2 Arena w Londynie dostarczy najwyższych emocji dzięki potrójnej punktacji.',
        'Kapitanowie Yannick Noah i Andre Agassi wystawili swoje największe gwiazdy. W deblu Alcaraz i Zverev zmierzą się z Fritzem i De Minaurem.',
        'W grach pojedynczych Alcaraz zagra z De Minaurem, a Zverev z Fritzem. Zwycięża drużyna, która jako pierwsza zdobędzie 13 punktów.',
      ],
    },
    zh: {
      title: '拉沃尔杯第3日决赛日：O2球场三倍积分激战，冠军悬念拉满',
      subtitle: '周日每胜独揽三分。阿尔卡拉斯与兹维列夫领衔欧洲队死磕弗里茨与德米纳尔。',
      excerpt: '第九届拉沃尔杯于周日在伦敦O2球场迎来决战日。单场胜者斩获三分，欧洲队与世界队展开13分夺冠大决战。',
      body: [
        '9月27日周日，第九届拉沃尔杯在伦敦O2球场迎来冠军决战日。按照赛事特殊赛制，周日所有比赛单场分值跃升为三分。',
        '诺阿与阿加西两位传奇队长公布了压轴对阵。阿尔卡拉斯与兹维列夫搭档双打迎战弗里茨与德米纳尔，为全天赛事拉开战幕。',
        '随后阿尔卡拉斯将在单打对阵德米纳尔，兹维列夫则迎战弗里茨。率先拿到13个积分的队伍将登顶捧起冠军奖杯。',
      ],
    },
    ja: {
      title: 'レーバーカップ第3日決勝日：O2で勝利点3倍、トロフィーを懸けた激闘',
      subtitle: '最終日は1勝につき3ポイント。アルカラスとズベレフが欧州選抜を牽引、世界選抜に挑む。',
      excerpt: '第9回レーバーカップがロンドンのO2アリーナで決着の時を迎える。3ポイントマッチが続く最終日、栄冠を懸けた熱戦が展開。',
      body: [
        '9月27日日曜日、ロンドンのO2アリーナでレーバーカップ最終日の熱狂が幕を開けた。日曜日は1勝の価値が3点に跳ね上がる。',
        'ノアとアガシの両主将はベストメンバーを指名。アルカラスとズベレフがダブルスでフリッツ、デミノー組と激突する。',
        '続くシングルスではアルカラス対デミノー、ズベレフ対フリッツの好カードが予定され、13点先取を目指す激闘が続く。',
      ],
    },
    ko: {
      title: '레이버컵 3일차 결승전: O2 아레나서 3점짜리 승부 펼치며 트로피 쟁탈전',
      subtitle: '런던 최종일 경기당 3점 부여. 알카라스와 츠베레프, 프리츠와 드미노 상대 출격.',
      excerpt: '제9회 레이버컵이 영국 런던 O2 아레나에서 최종일을 맞았다. 승점 3점이 걸린 일요일 매치에서 유럽과 월드 팀이 격돌한다.',
      body: [
        '레이버컵은 9월 27일 일요일 런던 O2 아레나의 검은 코트 위에서 대망의 챔피언십 선데이를 시작했다. 최종일 승리는 3점으로 계산된다.',
        '야닉 노아와 앙드레 아가시 단장은 최고의 라인업을 공개했다. 알카라스와 츠베레프가 복식에서 프리츠와 드미노 조를 상대한다.',
        '단식에서는 알카라스 대 드미노, 츠베레프 대 프리츠의 빅매치가 이어진다. 어느 팀이 먼저 13점에 도달할지 전 세계 테니스 팬들의 이목이 쏠린다.',
      ],
    },
    ar: {
      title: 'كأس لافر اليوم الثالث الختامي: مباريات بـ3 نقاط في O2 وحسم لقب البطولة',
      subtitle: 'كل فوز يساوي ثلاث نقاط في لندن. ألكاراز وزفيريف يقودان أوروبا أمام فريتز ودي مينور.',
      excerpt: 'تختتم النسخة التاسعة من كأس لافر يوم الأحد في صالة O2 في لندن، حيث تمنح كل مواجهة ثلاث نقاط في سباق الوصول إلى 13 نقطة.',
      body: [
        'تبلغ بطولة كأس لافر قمة الإثارة يوم الأحد 27 أيلول/سبتمبر في لندن، حيث يرتفع رصيد الفوز في كل مباراة إلى ثلاث نقاط حاسمة.',
        'أعلن القائدان يانيك نوا وأندريه أغاسي ترتيب المواجهات، حيث يستهل ألكاراز وزفيريف اليوم بمباراة زوجي مثيرة ضد فريتز ودي مينور.',
        'وتتواصل المباريات بمواجهات الفردي بين ألكاراز ودي مينور، ثم زفيريف وفريتز، لتحديد الفريق الذي سيسبق إلى حصد 13 نقطة ورفع الكأس.',
      ],
    },
  },
  'presidents-cup-sunday-singles-medinah-2026': {
    fr: {
      title: 'Presidents Cup Simples du Dimanche : 12 duels au parcours n°3 de Medinah',
      subtitle: 'Jour final à Medinah. Scheffler contre Matsuyama et Cantlay contre Scott mènent le face-à-face de 12 points.',
      excerpt: 'La 16e Presidents Cup se décide ce dimanche au Medinah Country Club en Illinois. Douze duels en individuel couronneront l’équipe victorieuse.',
      body: [
        'La 16e Presidents Cup livre son dénouement ce dimanche 27 septembre sur le parcours n°3 de Medinah avec douze matches de simples décisifs.',
        'Les capitaines Brandt Snedeker et Geoff Ogilvy ont dévoilé l’ordre des départs. Le numéro un mondial Scottie Scheffler ouvre face à Hideki Matsuyama.',
        'Patrick Cantlay défie ensuite le vétéran Adam Scott pour son 12e tournoi, suivi de Schauffele contre Im. La première équipe à 15,5 points triomphera.',
      ],
    },
    es: {
      title: 'Presidents Cup Individuales del Domingo: 12 duelos deciden la copa en Medinah',
      subtitle: 'Día decisivo en Medinah. Scheffler ante Matsuyama y Cantlay frente a Scott encabezan la batalla de 12 puntos.',
      excerpt: 'La 16ª Presidents Cup concluye este domingo en el Medinah Country Club de Illinois con doce partidos individuales que definirán al campeón.',
      body: [
        'El desenlace de la 16ª Presidents Cup llega este domingo 27 de septiembre al Course No. 3 de Medinah con 12 puntos en disputa en partidos individuales.',
        'Los capitanes Brandt Snedeker y Geoff Ogilvy programaron salidas de alto voltaje. Scottie Scheffler se mide a Hideki Matsuyama en el partido estelar de apertura.',
        'Patrick Cantlay jugará contra el veterano Adam Scott en su 12ª participación, seguido por Schauffele ante Im. Quien alcance 15,5 puntos se llevará la copa.',
      ],
    },
    de: {
      title: 'Presidents Cup Einzel am Sonntag: 12 Matches entscheiden den Cup in Medinah',
      subtitle: 'Finaltag auf Kurs Nr. 3. Scheffler gegen Matsuyama und Cantlay gegen Scott im Fokus.',
      excerpt: 'Der 16. Presidents Cup findet am Sonntag im Medinah Country Club seinen Sieger. Zwölf Einzelmatches bringen die Entscheidung.',
      body: [
        'Am Sonntag, dem 27. September, fällt die Entscheidung beim 16. Presidents Cup auf dem anspruchsvollen Medinah Course No. 3 in Illinois.',
        'Brandt Snedeker und Geoff Ogilvy haben ihre Startlisten festgelegt. Die Nummer eins der Welt, Scottie Scheffler, trifft im Eröffnungsmatch auf Hideki Matsuyama.',
        'Patrick Cantlay spielt gegen Adam Scott bei dessen 12. Auftritt, gefolgt von Schauffele gegen Im. Das erste Team mit 15,5 Punkten gewinnt.',
      ],
    },
    it: {
      title: 'Presidents Cup Singolari della Domenica: 12 sfide assegnano il trofeo a Medinah',
      subtitle: 'Ultimo atto a Medinah. Scheffler contro Matsuyama e Cantlay contro Scott guidano la resa dei conti da 12 punti.',
      excerpt: 'La 16ª Presidents Cup si conclude domenica al Medinah Country Club. Dodici match individuali incoroneranno la squadra campione.',
      body: [
        'La 16ª Presidents Cup raggiunge il verdetto finale domenica 27 settembre sul Course No. 3 di Medinah con dodici singolari ad altissima tensione.',
        'I capitani Snedeker e Ogilvy hanno schierato i rispettivi alfieri. Il leader mondiale Scottie Scheffler apre le danze contro Hideki Matsuyama.',
        'Patrick Cantlay affronta il veterano Adam Scott, mentre Xander Schauffele sfida Sungjae Im. La prima formazione a 15,5 punti solleverà la coppa.',
      ],
    },
    pl: {
      title: 'Presidents Cup Niedzielne Single: 12 pojedynków decyduje o pucharze w Medinah',
      subtitle: 'Finałowy dzień na polu nr 3. Scheffler kontra Matsuyama i Cantlay z Scottem na czele walki o 12 punktów.',
      excerpt: '16. Presidents Cup kończy się w niedzielę w Medinah Country Club w Illinois. Dwanaście meczów indywidualnych wyłoni zwycięzców.',
      body: [
        'Ostateczne rozstrzygnięcia 16. Pucharu Prezydentów zapadną w niedzielę 27 września na polu Medinah Course No. 3 w 12 pojedynkach singlowych.',
        'Kapitanowie Brandt Snedeker i Geoff Ogilvy ustalili kolejność startów. Lider rankingu Scottie Scheffler zmierzy się z Hidekim Matsuyamą.',
        'Patrick Cantlay zagra z weteranem Adamem Scottem, a Xander Schauffele powalczy z Sungjae Imem. Tytuł przypada ekipie, która uzyska 15,5 punktu.',
      ],
    },
    zh: {
      title: '总统杯周日个人对抗赛：12场对决决战梅迪纳3号球场',
      subtitle: '梅迪纳收官之日。舍夫勒对阵松山英树，坎特利交锋斯科特领衔12分决战。',
      excerpt: '第16届总统杯周日在伊利诺伊州梅迪纳乡村俱乐部决出总冠军。12场个人单挑将决定金色奖杯花落谁家。',
      body: [
        '9月27日周日，第16届总统杯在梅迪纳乡村俱乐部3号球场迎来最激烈的个人单挑决胜日，全天共设12个积分。',
        '斯内德克与奥格维两位队长提交了出场名单。世界第一舍夫勒在首场比赛对决前大师赛冠军松山英树。',
        '坎特利随后迎战第12次参赛的澳大利亚名将亚当·斯科特，谢奥菲勒则与韩国名将任成宰较量。率先取得15.5分的一方将夺冠。',
      ],
    },
    ja: {
      title: 'プレジデンツカップ日曜シングルス：メディナ3番コースで12戦の決着へ',
      subtitle: 'メディナ決戦の日。シェフラー対松山英樹、カントレー対スコットなど12ポイント争奪戦。',
      excerpt: '第16回プレジデンツカップは日曜日、メディナ・カントリークラブで決着を迎える。12試合のシングルス戦で勝者が決定。',
      body: [
        'プレジデンツカップは9月27日日曜日、イリノイ州メディナ3番コースで運命の最終日シングルス戦を迎えた。',
        'スネデカーとオギルビーの両主将が発表した組み合わせでは、世界ランク1位のシェフラーと日本の松山英樹が第1組で激突。',
        '第2組ではカントレーが12回目出場のスコットと対戦、シャウフェレはイム・ソンジェと対戦する。15.5点到達チームが勝利する。',
      ],
    },
    ko: {
      title: '프레지던츠컵 일요일 싱글 매치: 메디나 3번 코스서 12개 매치로 최종 승부',
      subtitle: '메디나 마지막 날 결전. 셰플러 대 마쓰야마, 캔틀리 대 스콧 등 12점 쟁탈전.',
      excerpt: '제16회 프레지던츠컵이 미국 메디나 컨트리클럽에서 최종일 일정을 시작했다. 12개 싱글 매치를 통해 최종 우승팀을 가린다.',
      body: [
        '프레지던츠컵은 9월 27일 일요일 메디나 3번 코스에서 12점이 걸린 12개 싱글 매치로 대회의 마지막 장을 펼친다.',
        '스네데커와 오길비 단장의 대진표에 따라 세계 1위 스코티 셰플러와 일본의 마쓰야마 히데키가 1번 매치에서 격돌한다.',
        '패트릭 캔틀리는 12번째 출전하는 애덤 스콧과 맞붙고, 잰더 쇼플리는 임성재와 승부를 겨룬다. 먼저 15.5점을 채우는 팀이 컵을 차지한다.',
      ],
    },
    ar: {
      title: 'كأس الرؤساء مباريات الفردي الأحد: 12 مواجهة تحسم اللقب في ملعب مادينا',
      subtitle: 'اليوم الختامي في مادينا. شيفلر ضد ماتسوياما وكانتلاي أمام سكوت في معركة الـ12 نقطة.',
      excerpt: 'تصل النسخة الـ16 من كأس الرؤساء إلى محطتها الأخيرة الأحد في نادي مادينا في إلينوي مع 12 مواجهة فردية لتحديد بطل البطولة.',
      body: [
        'يسدل الستار على منافسات النسخة 16 من كأس الرؤساء يوم الأحد 27 أيلول/سبتمبر على الملعب رقم 3 في مادينا بـ12 مواجهة فردية حاسمة.',
        'اعتمد القائدان سنديكر وأوجيلفي تشكيلات نارية، حيث يقود المصنف الأول سكوتي شيفلر الفريق الأمريكي في مواجهة الياباني هيديكي ماتسوياما.',
        'ويلتقي باتريك كانتلاي مع الأسترالي المخضرم آدم سكوت، فيما يواجه زاندر شوفيلي الكوري سونغجاي إم. يحتاج الفائز إلى بلوغ 15.5 نقطة للتتويج.',
      ],
    },
  },
  'city-beats-newcastle-2-1-mw6': {
    fr: {
      title: 'City 2-1 Newcastle : Haaland frappe encore et préserve le bilan parfait',
      subtitle: 'Haaland marque pour le 6e match consécutif. Bernardo Silva offre les trois points au sommet de la Premier League.',
      excerpt: 'Manchester City domine Newcastle United 2-1 à l’Etihad Stadium lors de la 6e journée. Les champions de Guardiola poursuivent avec six victoires en six matches.',
      body: [
        'La 6e journée de Premier League a vu Manchester City conforter sa domination samedi en s’imposant 2-1 face à Newcastle United.',
        'Erling Haaland a ouvert le score à la 31e minute sur un service de Kevin De Bruyne, portant son total personnel à neuf réalisations cette saison. Isak a égalisé pour les Magpies au retour des vestiaires.',
        'À la 68e minute, Bernardo Silva a déclenché une frappe lumineuse dans la lucarne pour sceller le succès des Cityzens. Avec 18 points, City compte trois longueurs d’avance sur Arsenal.',
      ],
    },
    es: {
      title: 'City 2-1 Newcastle: Haaland vuelve a marcar y mantiene el pleno de triunfos',
      subtitle: 'Haaland marca por sexto partido consecutivo. El golazo de Bernardo Silva asegura 18 puntos en el liderato.',
      excerpt: 'El Manchester City vence 2-1 al Newcastle en el Etihad en la jornada 6. Los pupilos de Guardiola suman seis victorias en seis partidos.',
      body: [
        'La 6ª jornada de la Premier League reafirmó el liderato indiscutible del Manchester City tras imponerse 2-1 al Newcastle United el sábado.',
        'Erling Haaland adelantó a los locales en el minuto 31 tras asistencia de Kevin De Bruyne, anotando por sexto duelo consecutivo. Alexander Isak igualó provisionalmente en el 52.',
        'En el minuto 68, Bernardo Silva clavó el balón en la escuadra para asegurar el triunfo. El City suma 18 puntos de 18 posibles y aventaja en tres al Arsenal.',
      ],
    },
    de: {
      title: 'City 2-1 Newcastle: Haaland trifft erneut und verteidigt weiße Weste',
      subtitle: 'Haaland im sechsten Ligaspiel in Serie erfolgreich. Bernardo Silva schießt City zu 18 Punkten an der Tabellenspitze.',
      excerpt: 'Manchester City bezwingt Newcastle United am 6. Spieltag im Etihad Stadium mit 2-1 und feiert den sechsten Sieg im sechsten Saisonspiel.',
      body: [
        'Der 6. Spieltag der Premier League bestätigte Guardiolas Mannschaft an der Tabellenspitze. Manchester City siegte am Samstagabend mit 2-1 gegen Newcastle United.',
        'Erling Haaland erzielte in der 31. Minute nach Zuspiel von Kevin De Bruyne sein neuntes Saisontor. Alexander Isak glich kurz nach der Pause für die Gäste aus.',
        'In der 68. Minute traf Bernardo Silva mit einem sehenswerten Schlenzer zum 2-1-Endstand. City thront mit 18 Punkten unangefochten auf Rang eins.',
      ],
    },
    it: {
      title: 'City 2-1 Newcastle: Haaland a segno ancora e percorso netto preservato',
      subtitle: 'Gol di Haaland nella sesta partita di fila. La magia di Bernardo Silva porta i campioni a quota 18 punti.',
      excerpt: 'Il Manchester City supera 2-1 il Newcastle all’Etihad Stadium nella 6ª giornata. Gli uomini di Guardiola mantengono il 100% di vittorie.',
      body: [
        'La 6ª giornata di Premier League ha confermato la superiorità del Manchester City, vittorioso per 2-1 contro il Newcastle United.',
        'Erling Haaland ha sbloccato il match al 31’ su invito di De Bruyne, segnando per la sesta gara consecutiva. Isak ha firmato il pareggio per i Magpies al 52’.',
        'Al 68’ Bernardo Silva ha pennellato un sinistro all’incrocio che è valso il successo. I campioni d’Inghilterra salgono a 18 punti in classifica.',
      ],
    },
    pl: {
      title: 'City 2-1 Newcastle: Haaland znowu trafia, mistrzowie z kompletem punktów',
      subtitle: 'Haaland strzela w szóstym kolejnym meczu. Piękny gol Bernardo Silvy daje 18 punktów na czele tabeli.',
      excerpt: 'Manchester City pokonał Newcastle United 2-1 na Etihad Stadium w 6. kolejce. Zespół Pepa Guardioli ma sześć zwycięstw w sześciu meczach.',
      body: [
        '6. kolejka Premier League potwierdziła dominację Manchesteru City, który w sobotni wieczór pokonał u siebie Newcastle United 2-1.',
        'Erling Haaland otworzył wynik w 31. minucie po podaniu Kevina De Bruyne, notując trafienie w każdym meczu sezonu. Isak wyrównał krótko po przerwie.',
        'W 68. minucie Bernardo Silva kapitalnym strzałem w okienko ustalił wynik spotkania. City z 18 punktami wyprzedza Arsenal o trzy oczka.',
      ],
    },
    zh: {
      title: '曼城2-1击败纽卡斯尔：哈兰德连场破门，蓝月亮全胜领跑英超',
      subtitle: '哈兰德连续六场联赛建功。贝尔纳多·席尔瓦世界波制胜，曼城豪取18分领跑积分榜。',
      excerpt: '英超第6轮曼城在伊蒂哈德球场2-1力克纽卡斯尔联。哈兰德首开纪录，B席绝杀，瓜迪奥拉球队斩获开局六连胜。',
      body: [
        '英超第6轮于周六晚间在伊蒂哈德球场上演焦点战，曼城主场2-1力退强敌纽卡斯尔联，成为全联盟唯一六战全胜的队伍。',
        '第31分钟，德布劳内送出手术刀直塞，哈兰德前插低射破门打进个人本赛季联赛第9球。下半场伊萨克一度为喜鹊军团扳平比分。',
        '第68分钟，贝尔纳多·席尔瓦禁区前沿轰出世界波直挂死角。曼城以18分继续以3分优势压倒阿森纳领跑积分榜。',
      ],
    },
    ja: {
      title: 'シティがニューカッスルに2-1勝利：ハーランド開幕6戦連発で首位快走',
      subtitle: 'ハーランドが毎試合ゴールの快挙。ベルナルド・シウバの決勝弾で開幕6連勝の勝ち点18へ。',
      excerpt: 'プレミアリーグ第6節でマンチェスター・シティがニューカッスルに2-1で勝利。開幕6連勝で首位の座を堅守した。',
      body: [
        'プレミアリーグ第6節がエティハド・スタジアムで行われ、マンチェスター・シティがニューカッスルを2-1で退けた。',
        '前半31分、デ・ブライネの絶妙なスルーパスに抜け出したハーランドが先制ゴールを奪い、開幕からの全試合得点記録を更新。後半イサクが同点弾を決める。',
        '迎えた68分、ベルナルド・シウバが鮮やかなミドルシュートを隅に突き刺し勝ち越し。シティは勝ち点18で2位アーセナルに3差をつけている。',
      ],
    },
    ko: {
      title: '맨시티, 뉴캐슬에 2-1 승리: 홀란 6경기 연속골 앞세워 100% 전승 질주',
      subtitle: '홀란 개막 6경기 연속 득점 행진. 베르나르두 실바의 결승골로 승점 18점 단독 선두.',
      excerpt: '맨체스터 시티가 프리미어리그 6라운드에서 뉴캐슬 유나이티드를 2-1로 꺾고 개막 6연승을 질주하며 선두 자리를 굳혔다.',
      body: [
        '프리미어리그 6라운드 에티하드 스타디움 경기에서 맨체스터 시티가 뉴캐슬을 2-1로 물리치며 전승 행진을 이어갔다.',
        '전반 31분 데브라위너의 패스를 받은 엘링 홀란이 리그 9호 골을 성공시켰다. 뉴캐슬은 이삭의 동점골로 맞섰으나 시티의 벽을 넘지 못했다.',
        '후반 68분 베르나르두 실바가 환상적인 감아차기로 결승골을 터뜨렸다. 시티는 승점 18점으로 2위 아스널에 승점 3점 차로 앞서 있다.',
      ],
    },
    ar: {
      title: 'مانشستر سيتي 2-1 نيوكاسل: هالاند يواصل التسجيل والسيتي يحافظ على العلامة الكاملة',
      subtitle: 'هالاند يسجل في سادس مباراة على التوالي. قذيفة برناردو سيلفا تؤمن النقطة 18 في صدارة الدوري.',
      excerpt: 'حقق مانشستر سيتي فوزًا ثمينًا على نيوكاسل يونايتد 2-1 على ملعب الاتحاد ليواصل انطلاقته المثالية بستة انتصارات من ست مباريات.',
      body: [
        'عزز مانشستر سيتي صدارته للدوري الإنجليزي الممتاز بفوزه المثير 2-1 على نيوكاسل يونايتد مساء السبت على ملعب الاتحاد.',
        'افتتح إيرلينغ هالاند التسجيل في الدقيقة 31 بعد تمريرة ساحرة من كيفين دي بروين مسجلًا هدفه التاسع هذا الموسم، قبل أن يتعادل إيزاك للضيوف.',
        'وفي الدقيقة 68، أحرز برناردو سيلفا هدف الفوز بتسديدة مقوسة رائعة في الزاوية العليا، ليرفع السيتي رصيده إلى 18 نقطة كاملة.',
      ],
    },
  },
  'nfl-week3-sunday-slate-bills-chiefs-2026': {
    fr: {
      title: 'NFL 3e semaine dimanche : les Bills accueillent les Dolphins, les Chiefs défient les Chargers',
      subtitle: 'Buffalo et Kansas City défendent leur invincibilité. Allen et Mahomes sous les projecteurs.',
      excerpt: 'Le grand dimanche de NFL arrive avec des chocs de division. Josh Allen mène Buffalo face à Miami, tandis que Mahomes et les Chiefs affrontent Los Angeles.',
      body: [
        'La 3e semaine de NFL bat son plein ce dimanche après la victoire des Packers 24-20 contre les Falcons jeudi à Lambeau.',
        'À Highmark Stadium, Josh Allen et les Bills (2-0) reçoivent les Dolphins de Miami dans un classique de l’AFC Est. Allen compte déjà neuf touchdowns en deux matches.',
        'À Arrowhead Stadium, Patrick Mahomes et les Chiefs (2-0) accueillent Justin Herbert et les Chargers dans un sommet explosif de l’AFC Ouest.',
      ],
    },
    es: {
      title: 'NFL Semana 3 Domingo: Bills reciben a Dolphins y Chiefs chocan con Chargers',
      subtitle: 'Buffalo y Kansas City exponen su invicto. Josh Allen y Patrick Mahomes toman el protagonismo.',
      excerpt: 'Llega la gran jornada dominical de la NFL con duelos divisionales imperdibles. Buffalo recibe a Miami y Kansas City se mide a los Chargers.',
      body: [
        'El domingo de la semana 3 de la NFL se presenta apasionante tras el triunfo de Green Bay 24-20 ante Atlanta el jueves.',
        'En Highmark Stadium, Josh Allen y los invictos Bills (2-0) reciben a los Miami Dolphins en un clásico de máxima rivalidad en la AFC Este.',
        'Más tarde, Patrick Mahomes y los Kansas City Chiefs (2-0) recibirán a Justin Herbert y Los Angeles Chargers por el liderato de la AFC Oeste.',
      ],
    },
    de: {
      title: 'NFL Woche 3 Sonntag: Bills empfangen Dolphins, Chiefs fordern Chargers heraus',
      subtitle: 'Ungeschlagene Bills und Chiefs verteidigen ihre weiße Weste. Allen und Mahomes im Rampenlicht.',
      excerpt: 'Der NFL-Sonntag bringt hochklassige Divisionsduelle. Josh Allen führt Buffalo gegen Miami an, während Mahomes auf die Chargers trifft.',
      body: [
        'Der 3. Spieltag der NFL erreicht am Sonntag seinen Höhepunkt nach dem 24-20-Sieg der Packers über die Falcons am Donnerstag.',
        'Im Highmark Stadium empfangen die mit 2-0 gestarteten Buffalo Bills die Miami Dolphins zum traditionsreichen AFC-East-Duell.',
        'Im Arrowhead Stadium stehen sich Patrick Mahomes und Justin Herbert beim Gipfeltreffen zwischen den Chiefs und den Chargers gegenüber.',
      ],
    },
    it: {
      title: 'NFL Week 3 Domenica: Bills contro Dolphins e Chiefs contro Chargers nei big match',
      subtitle: 'Buffalo e Kansas City difendono l’imbattibilità. Allen e Mahomes protagonisti assoluti.',
      excerpt: 'La domenica di NFL entra nel vivo con grandi sfide divisionali. Josh Allen guida i Bills contro Miami, mentre i Chiefs sfidano i Chargers.',
      body: [
        'La Week 3 della NFL vive la sua domenica più attesa dopo il successo dei Packers sui Falcons per 24-20 giovedì sera.',
        'All’Highmark Stadium i Buffalo Bills imbattuti (2-0) ospitano i Miami Dolphins in un classico scontro ad alta quota dell’AFC East.',
        'All’Arrowhead Stadium Patrick Mahomes e i Kansas City Chiefs affrontano Justin Herbert e i Los Angeles Chargers per il primato nell’AFC West.',
      ],
    },
    pl: {
      title: 'NFL Tydzień 3 Niedziela: Bills podejmują Dolphins, Chiefs walczą z Chargers',
      subtitle: 'Niepokonane Buffalo i Kansas City bronią bilansu. Allen i Mahomes w centrum uwagi.',
      excerpt: 'Niedzielne mecze NFL przynoszą hity dywizyjne. Josh Allen prowadzi Bills przeciwko Dolphins, a Chiefs mierzą się z Chargers.',
      body: [
        'Trzeci tydzień ligi NFL wchodzi w decydującą fazę po czwartkowym zwycięstwie Packers 24-20 nad Falcons.',
        'Na Highmark Stadium niepokonani Buffalo Bills (2-0) podejmują Miami Dolphins w emocjonującym starciu dywizji AFC East.',
        'Na Arrowhead Stadium Patrick Mahomes i Kansas City Chiefs stoczą pasjonujący pojedynek z Justinem Herbertem i Chargers.',
      ],
    },
    zh: {
      title: 'NFL第3周超级周日：比尔主场硬碰海豚，酋长闪电上演美西天王山之战',
      subtitle: '保持不败的水牛城与堪萨斯城迎来大考。阿伦与马霍姆斯万众瞩目。',
      excerpt: 'NFL第3周周日主赛程全面开打。乔什·阿伦率领2胜0负的比尔迎战海豚，马霍姆斯坐镇主场大战闪电。',
      body: [
        '继周四夜赛包装工24-20力克猎鹰后，NFL第3周在周日迎来精彩纷呈的同分区宿敌对决。',
        '在海马克体育场，开季手感火热的阿伦带领两连胜的比尔队迎战迈阿密海豚，双方将展开激烈空中较量。',
        '下午场比赛中，卫冕强权堪萨斯城酋长坐镇箭头球场迎战赫伯特领衔的洛杉矶闪电，争夺美联西区领跑地位。',
      ],
    },
    ja: {
      title: 'NFL第3週サンデー：ビルズ対ドルフィンズ、チーフス対チャージャーズの激突',
      subtitle: '無敗のビルズとチーフスが全勝維持へ。アレンとマホームズが主役を務める。',
      excerpt: 'NFL第3週の日曜決戦が開幕。2勝0敗のビルズがドルフィンズを迎え、マホームズ率いるチーフスがチャージャーズと激突。',
      body: [
        '木曜日にパッカーズがファルコンズを24-20で下したのに続き、NFL第3週は日曜日のメインカードへと突入した。',
        'ハイマーク・スタジアムでは、絶好調のジョシュ・アレン擁するビルズが同地区ライバルのドルフィンズと対戦。',
        'アローヘッド・スタジアムではパトリック・マホームズのチーフスがハーバートのチャージャーズを迎え撃つ。',
      ],
    },
    ko: {
      title: 'NFL 3주차 일요일 격전: 빌스 대 돌핀스, 치프스 대 차저스 메가 매치',
      subtitle: '개막 2연승 빌스와 치프스 안방 수성 도전. 앨런과 마홈스 정면 승부.',
      excerpt: 'NFL 3주차 일요일 일정이 화려하게 개막한다. 조시 앨런의 버펄로가 마이애미를 맞이하고, 마홈스의 치프스가 차저스와 격돌한다.',
      body: [
        '목요일 패커스의 24-20 승리에 이어 NFL 3주차 일요일 경기가 미국 전역에서 킥오프를 알렸다.',
        '하이마크 스타디움에서는 2승 무패를 달리는 버펄로 빌스가 지구 라이벌 마이애미 돌핀스를 홈으로 불러들인다.',
        '애로우헤드 스타디움에서는 패트릭 마홈스의 캔자스시티 치프스가 저스틴 허버트의 로스앤젤레스 차저스와 맞붙는다.',
      ],
    },
    ar: {
      title: 'دوري كرة القدم الأمريكية الأسبوع 3 الأحد: بيلز يستضيف دولفينز وتشييفس يواجه تشارجرز',
      subtitle: 'بافالو وكانساس سيتي يدافعان عن سجلهما النظيف. جوش ألين وباتريك ماهومز في بؤرة الضوء.',
      excerpt: 'تنطلق مباريات الأحد الكبرى في الأسبوع الثالث من دوري كرة القدم الأمريكية بمواجهات نارية تتصدرها قمة بيلز ضد دولفينز.',
      body: [
        'تتواصل إثارة الأسبوع الثالث من دوري كرة القدم الأمريكية بعد فوز باكرز الخميس 24-20 على فالكونز.',
        'في ملعب هاي مارك، يستضيف جوش ألين وفريقه بافالو بيلز (2-0) غريمهم التاريخي ميامي دولفينز في مواجهة ساخنة.',
        'وفي ملعب أروهيد، يلتقي باتريك ماهومز مع فريقه كانساس سيتي تشييفس ضد جاستن هيربرت وفريق لوس أنجلوس تشارجرز.',
      ],
    },
  },
  'wnba-playoffs-round1-game1-tipoff-2026': {
    fr: {
      title: 'Playoffs WNBA Coup d’envoi : quadruplé du 1er tour match 1 pour lancer la quête du titre',
      subtitle: 'Début des séries au meilleur des trois manches : le Lynx reçoit les Mystics, Clark et le Fever à Atlanta, les Valkyries débutent.',
      excerpt: 'Les playoffs WNBA 2026 débutent ce dimanche 27 septembre avec quatre matches inauguraux à fort enjeu dans tous les États-Unis.',
      body: [
        'Les playoffs WNBA 2026 s’ouvrent ce dimanche 27 septembre avec quatre premiers matches disputés sous haute tension.',
        'À Minneapolis, le Minnesota Lynx, tête de série numéro un (32-10), accueille les Washington Mystics en s’appuyant sur sa défense d’élite.',
        'À Atlanta, Caitlin Clark et l’Indiana Fever défient le Dream, avant les rencontres Golden State-New York et Las Vegas-Dallas.',
      ],
    },
    es: {
      title: 'Inicio de los Playoffs WNBA: cuatro partidos del Juego 1 abren la lucha por el título',
      subtitle: 'Series al mejor de tres: Lynx recibe a Mystics, Clark lidera a Fever en Atlanta y debutan las Valkyries.',
      excerpt: 'La postemporada de la WNBA 2026 arranca este domingo 27 de septiembre con cuatro encuentros del Juego 1 en busca del anillo.',
      body: [
        'Las eliminatorias por el título de la WNBA arrancan este domingo 27 de septiembre con una cartelera cuádruple de altos vuelos.',
        'En el Target Center, las Minnesota Lynx (32-10), primeras cabezas de serie, reciben a las Washington Mystics con su férrea defensa como bandera.',
        'En Atlanta, Caitlin Clark y las Indiana Fever visitan al Dream, mientras las Valkyries reciben a Liberty y las Aces se miden a Dallas.',
      ],
    },
    de: {
      title: 'WNBA-Playoffs Auftakt: Vier Spiele zu Spiel 1 eröffnen die Jagd nach dem Titel',
      subtitle: 'Best-of-Three-Serien starten am Sonntag: Lynx empfangen Mystics, Clark führt Fever nach Atlanta, Valkyries debütieren.',
      excerpt: 'Die WNBA-Playoffs 2026 starten am Sonntag, dem 27. September, mit vier Eröffnungsspielen im Kampf um die Meisterschaft.',
      body: [
        'Die WNBA-Playoffs 2026 beginnen am Sonntag, dem 27. September, mit vier richtungsweisenden Auftaktpartien.',
        'Im Target Center empfangen die topgesetzten Minnesota Lynx (32-10) die Washington Mystics mit ihrer ligaweit besten Defensive.',
        'In Atlanta tritt Caitlin Clark mit den Indiana Fever beim Dream an, gefolgt von den Duellen Valkyries gegen Liberty und Aces gegen Wings.',
      ],
    },
    it: {
      title: 'Al via i Playoff WNBA: quattro sfide di Gara 1 accendono la corsa al titolo',
      subtitle: 'Iniziano le serie al meglio delle tre gare: Lynx contro Mystics, Clark a caccia dell’impresa ad Atlanta, debutto Valkyries.',
      excerpt: 'La post-season WNBA 2026 decolla domenica 27 settembre con quattro partite inaugurali di altissimo livello.',
      body: [
        'I playoff WNBA 2026 scattano domenica 27 settembre con quattro sfide decisive di Gara 1 nei palazzetti americani.',
        'Al Target Center le Minnesota Lynx (32-10), prima testa di serie, ospitano le Washington Mystics forti della loro solida difesa.',
        'Ad Atlanta Caitlin Clark e le Indiana Fever sfidano il Dream, mentre le Valkyries affrontano le Liberty e le Aces incrociano Dallas.',
      ],
    },
    pl: {
      title: 'Start Play-off WNBA: cztery mecze meczu 1 otwierają walkę o pierścienie',
      subtitle: 'Serie do dwóch zwycięstw ruszają w niedzielę: Lynx podejmują Mystics, Clark prowadzi Fever w Atlancie, debiut Valkyries.',
      excerpt: 'Faza play-off WNBA 2026 oficjalnie rusza w niedzielę 27 września czterema starciami meczu pierwszego.',
      body: [
        'Play-offy ligi WNBA 2026 rozpoczynają się w niedzielę 27 września czterema spotkaniami pierwszej rundy.',
        'W Target Center najlepsze w sezonie zasadniczym Minnesota Lynx (32-10) mierzą się z Washington Mystics.',
        'W Atlancie Caitlin Clark i Indiana Fever grają z Dream, a na zachodzie Valkyries podejmują Liberty, zaś Aces grają ze skrzydłami z Dallas.',
      ],
    },
    zh: {
      title: 'WNBA季后赛揭幕：首轮第一战四场连台，总冠军追逐战全面打响',
      subtitle: '三局两胜首战周日打响：山猫迎战神秘人，克拉克率狂热客战梦想，女武神季后赛首秀。',
      excerpt: '2026年WNBA季后赛于9月27日周日正式拉开大幕，全美四地球场上演首轮第一场火星撞地球般的大决战。',
      body: [
        '2026赛季WNBA季后赛于9月27日周日全面打响，四场首轮第一战在全美多座球场连番上演。',
        '在标靶中心，全联盟头号种子明尼苏达山猫（32胜10负）坐镇主场迎接华盛顿神秘人的挑战。',
        '在亚特兰大，凯特琳·克拉克率领五号种子印第安纳狂热客场挑战梦想队。随后金州女武神与卫冕冠军拉斯维加斯王牌也将分别登场。',
      ],
    },
    ja: {
      title: 'WNBAプレーオフ開幕：第1戦4カードが激突、女王への道がスタート',
      subtitle: '3戦2勝制の開幕戦：リンクスがミスティクスを迎撃、クラーク率いるフィーバーがアトランタへ、ヴァルキリーズ初登場。',
      excerpt: '2026年WNBAプレーオフが9月27日日曜日に開幕。4会場で第1戦が行われ、チャンピオンリングへの戦いが始まった。',
      body: [
        'WNBAプレーオフ2026が9月27日日曜日に開幕し、4つのファーストラウンド第1戦が一斉にティップオフを迎えた。',
        'ターゲット・センターでは全体1位のミネソタ・リンクス（32勝10敗）がワシントン・ミスティクスを迎撃。',
        'アトランタではケイトリン・クラークのインディアナ・フィーバーがドリームと対戦、さらにヴァルキリーズ対リバティ、エーシズ対ウィングスと続く。',
      ],
    },
    ko: {
      title: 'WNBA 플레이오프 개막: 1라운드 1차전 4경기 시작되며 우승 경쟁 돌입',
      subtitle: '3전 2선승제 개막: 링스 대 미스틱스, 클라크의 피버 애틀랜타 원정, 발키리스 데뷔전.',
      excerpt: '2026 WNBA 플레이오프가 9월 27일 일요일 공식 개막했다. 1차전 4경기가 일제히 펼쳐지며 우승을 향한 여정이 시작된다.',
      body: [
        '2026 WNBA 플레이오프가 9월 27일 일요일 4개 경기장에서 1라운드 1차전 일정으로 화려한 막을 올렸다.',
        '타깃 센터에서는 전체 1번 시드 미네소타 링스(32승 10패)가 워싱턴 미스틱스를 상대로 기선 제압에 나섰다.',
        '애틀랜타에서는 케이틀린 클라크의 인디애나 피버가 드림과 격돌하며, 골든스테이트 발키리스와 라스베이거스 에이시스도 각각 홈경기를 치른다.',
      ],
    },
    ar: {
      title: 'انطلاق أدوار WNBA الإقصائية: أربع مباريات في الجولة الأولى تشعل صراع اللقب',
      subtitle: 'سلسلة الأفضل من ثلاث مباريات تبدأ الأحد: لينكس يستضيف ميستيكس، وكلارك تقود فيفر في أتلانتا.',
      excerpt: 'تنطلق الأدوار الإقصائية لدوري السلة الأمريكي للسيدات WNBA 2026 يوم الأحد 27 أيلول/سبتمبر بأربع مواجهات نارية في الجولة الأولى.',
      body: [
        'انطلقت الأدوار الإقصائية لدوري كرة السلة الأمريكي للسيدات 2026 يوم الأحد 27 أيلول/سبتمبر بإقامة أربع مباريات في الجولة الأولى.',
        'في قاعة تارغت سنتر، يستقبل فريق مينيسوتا لينكس متصدر الترتيب (32-10) نظيره واشنطن ميستيكس.',
        'وفي أتلانتا، تقود كيتلين كلارك فريق إنديانا فيفر في قمة كبرى ضد دريم، تليها مباراتا فالكيريز ضد ليبرتي وإيسيز ضد وينغز.',
      ],
    },
  },
  'laver-cup-europe-champions-2026': {
    fr: {
      title: "Team Europe remporte la Laver Cup 2026 : Alcaraz scelle un triomphe 13-11 à l'O2",
      subtitle: 'Carlos Alcaraz bat Taylor Fritz 6-2, 7-5 lors du match décisif à Londres pour reconquérir le trophée.',
      excerpt: "Carlos Alcaraz offre la Laver Cup 2026 à Team Europe en dominant Taylor Fritz dans l'ultime simple à l'O2 Arena de Londres pour une victoire 13-11.",
      body: [
        "La 9e édition de la Laver Cup s'est achevée dimanche soir à Londres par un dénouement palpitant : un douzième match décisif sur le court noir de l'O2 Arena.",
        'Menée 4-8 au matin du dimanche des champions, Team Europe a remporté trois des quatre matches à trois points pour devancer Team World 13-11.',
        "Après la victoire en double d'Alcaraz et Zverev puis le succès de Zverev sur Nakashima, Carlos Alcaraz a dominé Taylor Fritz 6-2, 7-5 devant 18 000 spectateurs conquis.",
      ],
    },
    es: {
      title: 'El Team Europe conquista la Laver Cup 2026: Alcaraz sella un épico 13-11 en el O2',
      subtitle: 'Carlos Alcaraz supera a Taylor Fritz 6-2, 7-5 en el duelo definitivo en Londres para recuperar el trofeo.',
      excerpt: 'Carlos Alcaraz corona al Team Europe en la Laver Cup 2026 al vencer a Taylor Fritz en el último partido en el O2 Arena para sellar el triunfo 13-11.',
      body: [
        'La 9ª edición de la Laver Cup concluyó el domingo por la noche en Londres con máxima emoción: un duodécimo partido a todo o nada en la pista negra del O2 Arena.',
        'Con desventaja de 4-8 al comenzar el domingo, el Team Europe sumó tres de los cuatro partidos de triple puntuación para superar al Team World 13-11.',
        'Tras el doblete de Alcaraz y Zverev y la victoria de Zverev ante Nakashima, Carlos Alcaraz venció a Taylor Fritz 6-2, 7-5 ante 18.000 aficionados.',
      ],
    },
    de: {
      title: 'Team Europe gewinnt Laver Cup 2026: Alcaraz besiegelt 13:11-Triumph in London',
      subtitle: 'Carlos Alcaraz schlägt Taylor Fritz 6:2, 7:5 im entscheidenden Sonntagsspiel und holt den Pokal zurück.',
      excerpt: 'Carlos Alcaraz sichert Team Europe den Laver Cup 2026 mit einem Zweisatzsieg gegen Taylor Fritz in der ausverkauften O2 Arena.',
      body: [
        'Die 9. Ausgabe des Laver Cup endete am Sonntagabend in London mit einem packenden Finale auf dem schwarzen Court der O2 Arena.',
        'Team Europe lag vor dem Finaltag 4:8 zurück, gewann aber drei der vier Dreipunkte-Matches am Championship Sunday und siegte 13:11 gegen Team World.',
        'Nach dem Doppelsieg von Alcaraz und Zverev sowie Zverevs Einzelsieg gegen Nakashima machte Carlos Alcaraz mit 6:2, 7:5 gegen Taylor Fritz alles klar.',
      ],
    },
    it: {
      title: 'Il Team Europe vince la Laver Cup 2026: Alcaraz sigilla il 13-11 alla O2 Arena',
      subtitle: 'Carlos Alcaraz supera Taylor Fritz 6-2, 7-5 nella sfida decisiva di Londra e riporta la coppa in Europa.',
      excerpt: "Carlos Alcaraz trascina il Team Europe alla conquista della Laver Cup 2026 battendo Taylor Fritz nell'ultimo match per il trionfo 13-11.",
      body: [
        'La nona edizione della Laver Cup si è conclusa domenica sera a Londra con un finale ad altissima tensione sul campo nero della O2 Arena.',
        "Sotto 4-8 all'inizio della domenica decisiva, il Team Europe ha conquistato tre match su quattro con punteggio triplo, superando il Team World 13-11.",
        'Dopo il successo in doppio di Alcaraz e Zverev e la vittoria di Zverev su Nakashima, Alcaraz ha battuto Fritz 6-2, 7-5 davanti a 18.000 spettatori.',
      ],
    },
    pl: {
      title: 'Team Europe wygrywa Laver Cup 2026: Alcaraz pieczętuje triumf 13-11 w Londynie',
      subtitle: 'Carlos Alcaraz pokonuje Taylora Fritza 6-2, 7-5 w decydującym pojedynku i odzyskuje puchar dla Europy.',
      excerpt: 'Carlos Alcaraz zapewnia drużynie Europy triumf w Laver Cup 2026, pokonując Taylora Fritza w dramatycznym meczu w londyńskiej O2 Arena.',
      body: [
        'Dziewiąta edycja Laver Cup zakończyła się w niedzielę wieczorem w Londynie emocjonującym dwunastym pojedynkiem na czarnym korcie O2 Arena.',
        'Przegrywając 4-8 przed niedzielną serią, Team Europe wygrał trzy z czterech potrójnie punktowanych meczów, pokonując Team World 13-11.',
        'Po zwycięstwie deblowym Alcaraza i Zvereva oraz wygranej Zvereva z Nakashimą, Carlos Alcaraz pokonał Fritza 6-2, 7-5.',
      ],
    },
    zh: {
      title: '欧洲队夺得2026拉沃尔杯：阿尔卡拉斯决胜战建功，13比11逆转夺冠',
      subtitle: '阿尔卡拉斯在O2体育馆6比2、7比5击败弗里茨，助欧洲队重夺冠军奖杯。',
      excerpt: '2026年拉沃尔杯在伦敦O2体育馆收官，阿尔卡拉斯在决胜战直落两盘击败弗里茨，助欧洲队13比11险胜世界队。',
      body: [
        '第9届拉沃尔杯周日晚在伦敦O2体育馆黑色硬地球场迎来终极决战，双方战至第12场一决胜负。',
        '进入周日决赛日时欧洲队以4比8落后，但在单场价值3分的高压下，欧洲队赢下4场中的3场，最终以13比11实现大逆转。',
        '在阿尔卡拉斯与兹维列夫拿下双打、兹维列夫单打获胜后，阿尔卡拉斯以6比2、7比5力克弗里茨锁定冠军。',
      ],
    },
    ja: {
      title: 'チーム・ヨーロッパがレーバーカップ2026制覇：アルカラスが13-11劇的勝利決める',
      subtitle: 'アルカラスが最終戦でフリッツを6-2、7-5で撃破。ロンドンO2アリーナでタイトル奪還。',
      excerpt: '2026年レーバーカップ決勝日、アルカラスが第12試合でフリッツを下し、チーム・ヨーロッパが13-11で世界選抜に逆転勝利。',
      body: [
        'ロンドンのO2アリーナで行われた第9回レーバーカップは、日曜夜の第12試合にもつれ込む大熱戦となった。',
        '4-8のビハインドで最終日を迎えた欧州選抜は、1勝3点のチャンピオンシップ・サンデーで4戦中3勝を奪い13-11で逆転勝利。',
        'ダブルス勝利とズベレフの白星に続き、カルロス・アルカラスがテイラー・フリッツを6-2、7-5で下して栄冠を掴んだ。',
      ],
    },
    ko: {
      title: '팀 유럽, 2026 레이버컵 우승: 알카라스 최종전 승리로 13-11 역전 드라마',
      subtitle: '알카라스가 결승전에서 프리츠를 6-2, 7-5로 꺾고 런던 O2 아레나에서 우승 트로피 탈환.',
      excerpt: '2026 레이버컵 최종일, 카를로스 알카라스가 테일러 프리츠를 제압하며 팀 유럽이 팀 월드를 13-11로 꺾고 우승을 차지했다.',
      body: [
        '제9회 레이버컵이 일요일 밤 런던 O2 아레나에서 마지막 12번째 매치까지 이어지는 명승부 끝에 막을 내렸다.',
        '4-8로 뒤진 채 최종일을 맞이한 팀 유럽은 1승당 3점이 걸린 일요일 4경기 중 3경기를 쓸어담으며 13-11 대역전극을 완성했다.',
        '복식 승리와 츠베레프의 단식 승리에 이어, 카를로스 알카라스가 테일러 프리츠를 6-2, 7-5로 꺾고 마침표를 찍었다.',
      ],
    },
    ar: {
      title: 'فريق أوروبا يتوج بكأس لافر 2026: ألكاراز يحسم لقاء القمة بنتيجة 13-11 في لندن',
      subtitle: 'كارلوس ألكاراز يهزم تايلور فريتز 6-2 و7-5 في المباراة الحاسمة ويعيد الكأس إلى القارة الأوروبية.',
      excerpt: 'توج فريق أوروبا بلقب كأس لافر للتنس 2026 بعد فوز كارلوس ألكاراز في المباراة الختامية على تايلور فريتز في صالة O2 بلندن بنتيجة 13-11.',
      body: [
        'اختتمت النسخة التاسعة من بطولة كأس لافر في صالة O2 بلندن بقمة نارية حسمتها المباراة الثانية عشرة والأخيرة.',
        'دخل فريق أوروبا اليوم الحاسم متأخرا 4-8، لكنه حصد تسع نقاط من أصل 12 ممكنة في مباريات الأحد ليقلب الطاولة بنتيجة 13-11.',
        'بعد فوز ألكاراز وزفيريف بالزوجي وتفوق زفيريف على ناكاشيما، قدم كارلوس ألكاراز أداء رائعا ليتغلب على تايلور فريتز 6-2 و7-5.',
      ],
    },
  },
  'united-states-wins-presidents-cup-2026': {
    fr: {
      title: 'Les États-Unis remportent la 16e Presidents Cup : Scheffler et Cantlay brillent à Medinah',
      subtitle: "L'équipe américaine décroche son 10e sacre consécutif grâce à une démonstration en simples (18,5 - 11,5).",
      excerpt: "Les États-Unis dominent l'équipe internationale 18,5-11,5 au Medinah Country Club, remportant leur 10e Presidents Cup consécutive.",
      body: [
        "La 16e Presidents Cup s'est jouée dimanche sur le parcours n°3 rénové de Medinah, et les États-Unis ont répondu avec autorité.",
        "Avec une avance de 11-7 au départ, le capitaine Brandt Snedeker a vu son équipe récolter 7,5 points en simples pour s'imposer 18,5 - 11,5.",
        'Le numéro un mondial Scottie Scheffler a battu Hideki Matsuyama 3&2, Patrick Cantlay a dominé Adam Scott 2&1, et Xander Schauffele a sécurisé le sacre.',
      ],
    },
    es: {
      title: 'Estados Unidos conquista la 16ª Presidents Cup: Scheffler y Cantlay sellan el 18.5-11.5 en Medinah',
      subtitle: 'El equipo estadounidense logra su décima copa consecutiva tras imponerse en los individuales del domingo.',
      excerpt: 'Estados Unidos vence al equipo Internacional por 18.5-11.5 en Medinah Country Club y retiene la Presidents Cup por décima edición consecutiva.',
      body: [
        'La 16ª Presidents Cup se decidió el domingo en los partidos individuales del Campo N° 3 de Medinah con triunfo categórico estadounidense.',
        'Con una renta de 11-7 al comenzar la jornada, el equipo de Brandt Snedeker sumó 7.5 puntos dominicales para cerrar el marcador en 18.5 - 11.5.',
        'Scottie Scheffler abrió el camino venciendo a Hideki Matsuyama 3&2, Patrick Cantlay superó a Adam Scott 2&1 y Schauffele selló la victoria.',
      ],
    },
    de: {
      title: 'USA gewinnen 16. Presidents Cup: Scheffler und Cantlay führen 18,5:11,5-Sieg in Medinah an',
      subtitle: 'US-Team feiert zehnten Triumph in Folge dank starker Einzelvorstellung auf dem Medinah Course No. 3.',
      excerpt: 'Die USA besiegen das internationale Team mit 18,5:11,5 im Medinah Country Club und verteidigen den Presidents Cup souverän.',
      body: [
        'Der 16. Presidents Cup endete am Sonntag auf dem neu gestalteten Course No. 3 in Medinah mit einem klaren US-Erfolg.',
        'Mit einer 11:7-Führung gestartet, holte das Team von Kapitän Brandt Snedeker 7,5 Punkte in den Einzeln zum 18,5:11,5-Gesamtsieg.',
        'Weltranglistenerster Scottie Scheffler schlug Hideki Matsuyama 3&2, Patrick Cantlay bezwang Adam Scott 2&1 und Schauffele holte den entscheidenden Punkt.',
      ],
    },
    it: {
      title: 'Gli Stati Uniti vincono la 16ª Presidents Cup: Scheffler e Cantlay firmano il 18.5-11.5 a Medinah',
      subtitle: 'Decimo successo consecutivo per la squadra americana grazie ai singoli domenicali sul percorso No. 3.',
      excerpt: 'Gli Stati Uniti battono la selezione Internazionale 18.5-11.5 al Medinah Country Club, confermando la propria egemonia nella Presidents Cup.',
      body: [
        'La 16ª Presidents Cup si è decisa domenica nei singoli sul rinnovato Course No. 3 di Medinah con un successo limpido degli Stati Uniti.',
        'Avanti 11-7 alla vigilia dei singoli, la formazione guidata da Brandt Snedeker ha raccolto 7.5 punti per chiudere sul 18.5 - 11.5.',
        'Il numero uno al mondo Scottie Scheffler ha superato Hideki Matsuyama 3&2, mentre Cantlay e Schauffele hanno blindato il trofeo.',
      ],
    },
    pl: {
      title: 'USA wygrywają 16. Presidents Cup: Scheffler i Cantlay prowadzą do triumfu 18.5-11.5 w Medinah',
      subtitle: 'Amerykanie zdobywają puchar po raz dziesiąty z rzędu dzięki dominacji w niedzielnych meczach singlowych.',
      excerpt: 'Stany Zjednoczone pokonały drużynę Międzynarodową 18.5-11.5 w Medinah Country Club, sięgając po dziesiąty kolejny Presidents Cup.',
      body: [
        'Szesnasta edycja Presidents Cup zakończyła się w niedzielę w Medinah pewnym zwycięstwem reprezentacji Stanów Zjednoczonych.',
        'Prowadząc 11-7 przed grami singlowymi, podopieczni Brandta Snedekera zdobyli w niedzielę 7.5 punktu, ustalając wynik na 18.5 - 11.5.',
        'Lider rankingu Scottie Scheffler pokonał Hidekiego Matsuyamę 3&2, Patrick Cantlay wygrał z Adamem Scottem 2&1, a Schauffele przypieczętował sukces.',
      ],
    },
    zh: {
      title: '美国队夺得第16届总统杯：舍夫勒与坎特利带队，18.5比11.5大胜国际队',
      subtitle: '美国队在梅迪纳3号球场单人对决中火力全开，实现总统杯十连冠伟业。',
      excerpt: '美国队在梅迪纳乡村俱乐部以18.5比11.5战胜国际队，连续第10次捧起总统杯，总战绩扩大为14胜1平1负。',
      body: [
        '第16届总统杯周日在梅迪纳乡村俱乐部3号球场落下帷幕，美国队在个人对抗赛中展现强大阵容深度。',
        '带着11比7优势进入周日单人赛的美国队再揽7.5分，队长斯内德克尔带队以18.5比11.5轻松卫冕。',
        '世界第一舍夫勒以赢3洞剩2洞击败松山英树，坎特利战胜亚当-斯科特，谢奥菲勒随后锁定胜局。',
      ],
    },
    ja: {
      title: '米国選抜が第16回プレジデンツカップ優勝：シェフラーとカントレー牽引で18.5-11.5勝利',
      subtitle: 'メディナ第3コースのシングルス戦で圧倒し、米国チームが大会10連覇を達成。',
      excerpt: '米国選抜が国際選抜を18.5-11.5で退け、プレジデンツカップ10連覇を飾った。シェフラーとカントレーが日曜シングルスで躍動。',
      body: [
        '第16回プレジデンツカップは日曜日、改修されたメディナ・カントリークラブ第3コースでシングルス12戦が行われた。',
        '11-7のリードで出たブラント・スネデカー主将の米国選抜は、日曜日も7.5点を上積みして18.5-11.5で快勝した。',
        '世界1位のスコッティ・シェフラーが松山英樹に3&2で勝利、パトリック・カントレーがアダム・スコットを下して連覇を確定させた。',
      ],
    },
    ko: {
      title: '미국팀, 제16회 프레지던츠컵 우승: 셰플러와 캔틀레이 활약으로 18.5-11.5 완승',
      subtitle: '메디나 3번 코스 일요일 싱글 매치에서 맹활약하며 대회 10연패 달성.',
      excerpt: '미국 대표팀이 인터내셔널팀을 18.5-11.5로 꺾고 프레지던츠컵 10연속 우승을 차지했다. 셰플러와 캔틀레이가 싱글 매치를 지배했다.',
      body: [
        '제16회 프레지던츠컵이 일요일 메디나 컨트리클럽 3번 코스에서 미국팀의 압도적 승리로 막을 내렸다.',
        '11-7 리드를 안고 최종일에 나선 미국팀은 싱글 매치에서 7.5점을 추가하며 18.5-11.5로 승부에 쐐기를 박았다.',
        '세계 1위 스코티 셰플러가 마쓰야마 히데키를 3&2로 제압했고, 패트릭 캔틀레이와 잰더 쇼플리가 승리를 굳혔다.',
      ],
    },
    ar: {
      title: 'الولايات المتحدة تتوج بكأس الرؤساء للمرة السادسة عشرة: شي Handles وميداينا يشهدان فوزا 18.5-11.5',
      subtitle: 'الفريق الأمريكي يحصد لقبه العاشر تواليا بفضل تألق شي Handles وكانتلاي في الفردي.',
      excerpt: 'فازت الولايات المتحدة على الفريق الدولي 18.5-11.5 في نادي ميدينا لتحافظ على كأس الرؤساء للغولف للمرة العاشرة على التوالي.',
      body: [
        'اختتمت منافسات كأس الرؤساء السادسة عشرة يوم الأحد في نادي ميدينا بانتصار أمريكي مستحق بنتيجة 18.5 - 11.5.',
        'بدأ الفريق الأمريكي بقيادة براندت سنيديكر اليوم متقدما 11-7، ثم حصد 7.5 نقطة في مواجهات الفردي لحسم اللقاء.',
        'تغلب المصنف الأول سكوتي شيفلر على هيديكي ماتسوياما، بينما فاز باتريك كانتلاي على آدم سكوت ليحتفظ الأمريكيون باللقب.',
      ],
    },
  },
  'cowboys-eagles-mnf-week3-2026': {
    fr: {
      title: 'Cowboys contre Eagles au Monday Night Football : choc au sommet de la NFC Est',
      subtitle: "Hurts et Prescott s'affrontent au Lincoln Financial Field avec un bilan de 2-1 en ligne de mire.",
      excerpt: 'Le Monday Night Football clôture la 3e semaine NFL avec un grand classique de la NFC Est opposant Philadelphie à Dallas.',
      body: [
        "La 3e semaine de la saison NFL 2026 s'achève par l'un des duels les plus intenses du football américain : Eagles contre Cowboys.",
        'Les deux franchises affichent un bilan de 1-1 et visent la deuxième place de leur division derrière Washington.',
        'Jalen Hurts comptera sur Saquon Barkley et A.J. Brown face à la défense menée par Micah Parsons et Dak Prescott.',
      ],
    },
    es: {
      title: 'Cowboys visitan a Eagles en Monday Night Football: duelo por la cima de la NFC Este',
      subtitle: 'Hurts y Prescott reanudan su histórica rivalidad en el Lincoln Financial Field en busca del 2-1.',
      excerpt: 'El Monday Night Football cierra la Semana 3 de la NFL con el choque divisional entre Philadelphia Eagles y Dallas Cowboys.',
      body: [
        'La Semana 3 de la NFL concluye este lunes con una de las rivalidades más apasionantes del deporte: Dallas en Filadelfia.',
        'Ambos equipos llegan con marca de 1-1, buscando dar un golpe sobre la mesa en una división altamente disputada.',
        'Jalen Hurts y Saquon Barkley buscarán imponer su juego terrestre frente a Micah Parsons y la ofensiva de Dak Prescott.',
      ],
    },
    de: {
      title: 'Cowboys bei den Eagles im Monday Night Football: NFC-East-Klassiker zum Wochenabschluss',
      subtitle: 'Hurts und Prescott treffen im Lincoln Financial Field aufeinander. Beide Teams kämpfen um eine 2-1-Bilanz.',
      excerpt: 'Monday Night Football beschließt Woche 3 der NFL mit dem traditionsreichen NFC-East-Duell zwischen Philadelphia und Dallas.',
      body: [
        'Woche 3 der NFL-Saison 2026 endet am Montagabend mit einem der traditionsreichsten Rivalitätsspiele der Liga in Philadelphia.',
        'Beide Teams stehen bei 1-1 und wollen sich mit einem Sieg im Rennen um die NFC-East-Spitze positionieren.',
        'Jalen Hurts führt den Eagles-Angriff mit Saquon Barkley gegen die von Micah Parsons angeführte Cowboys-Defensive an.',
      ],
    },
    it: {
      title: 'Cowboys contro Eagles al Monday Night Football: sfida per il primato nella NFC East',
      subtitle: 'Hurts e Prescott rinnovano la storica rivalità al Lincoln Financial Field per portarsi sul 2-1.',
      excerpt: 'Il Monday Night Football chiude la Week 3 della NFL con la classica sfida divisionale tra Philadelphia Eagles e Dallas Cowboys.',
      body: [
        'La terza giornata della NFL si chiude lunedì sera con il classico scontro divisionale tra Philadelphia e Dallas.',
        "Entrambe le franchigie arrivano all'appuntamento sull'1-1, a caccia di un successo fondamentale per la corsa ai playoff.",
        "Jalen Hurts e Saquon Barkley sfidano la difesa dei Cowboys guidata da Micah Parsons e l'attacco di Dak Prescott.",
      ],
    },
    pl: {
      title: 'Cowboys u Eagles w Monday Night Football: bitwa o prymat w NFC East',
      subtitle: 'Hurts i Prescott wznawiają prestiżową rywalizację na Lincoln Financial Field przy bilansach 1-1.',
      excerpt: 'Monday Night Football zamyka 3. tydzień NFL wielkim klasykiem dywizji NFC East pomiędzy Philadelphia Eagles a Dallas Cowboys.',
      body: [
        'Trzeci tydzień sezonu NFL 2026 kończy się prestiżowym pojedynkiem Monday Night Football w Filadelfii.',
        'Obie ekipy mają bilans 1-1 i walczą o cenne zwycięstwo wewnątrz dywizji NFC East.',
        'Jalen Hurts i Saquon Barkley postarają się sforsować defensywę Dallas dowodzoną przez Micaha Parsonsa.',
      ],
    },
    zh: {
      title: '周一橄榄球之夜国东内战：牛仔做客费城老鹰，争夺2胜1负先机',
      subtitle: '赫茨与普雷斯科特林肯金融球场再次交手，国联东部宿敌决战黄金时段。',
      excerpt: 'NFL第3周周一之夜迎来经典国东德比，费城老鹰主场迎战达拉斯牛仔，胜者将占据分区有利排名。',
      body: [
        '2026年NFL常规赛第3周在林肯金融球场画上句号，老鹰与牛仔打响国联东部黄金档大战。',
        '两队目前战绩均为1胜1负，本场胜者将升至2胜1负并获得分区胜负交手优势。',
        '赫茨携手巴克利和布朗坐镇主场，迎接普雷斯科特、兰姆以及帕森斯领衔的牛仔军团。',
      ],
    },
    ja: {
      title: 'マンデーナイト・フットボール：カウボーイズがイーグルス本拠地へ乗り込むNFC東地区決戦',
      subtitle: 'ハーツとプレスコットが激突。リンカーン・ファイナンシャル・フィールドで2勝1敗を争う大一番。',
      excerpt: 'NFL第3週のマンデーナイトは、伝統のNFC東地区ライバル対決。フィラデルフィア・イーグルスがダラス・カウボーイズをホームで迎え撃つ。',
      body: [
        'NFL2026年シーズン第3週のフィナーレは、全米が注目するマンデーナイトのイーグルス対カウボーイズ戦。',
        'ともに1勝1敗で迎えた両雄が、地区首位争いの重要な足がかりをかけて激突する。',
        'ジェイレン・ハーツとサクオン・バークリーの地上戦に対し、ダック・プレスコットとマイカ・パーソンズがどう対抗するか注目だ。',
      ],
    },
    ko: {
      title: '먼데이 나이트 풋볼 카우보이스 대 이글스: NFC 동부지구 라이벌전 격돌',
      subtitle: '허츠와 프레스콧이 링컨 파이낸셜 필드에서 격돌. 2승 1패 고지를 향한 프라임타임 대결.',
      excerpt: 'NFL 3주차 마지막 경기로 전통의 NFC 동부지구 맞라이벌 필라델피아 이글스와 댈러스 카우보이스가 격돌한다.',
      body: [
        '2026 NFL 정규시즌 3주차가 필라델피아에서 열리는 먼데이 나이트 풋볼 카우보이스 대 이글스 전으로 막을 내린다.',
        '나란히 1승 1패를 기록 중인 양 팀은 지구 2위 및 콘퍼런스 경쟁에서 우위를 점하기 위해 물러설 수 없는 대결을 펼친다.',
        '제일런 허츠와 세이콴 바클리가 이끄는 필라델피아와 마이카 파슨스 및 닥 프레스콧의 댈러스가 한판 승부를 벌인다.',
      ],
    },
    ar: {
      title: 'كاوبويز يواجه إيغلز في كرة القدم ليلة الإثنين: قمة كبرى في دوري NFL',
      subtitle: 'هيرتس وبريسكوت يجددان المنافسة التاريخية في فيلادلفيا من أجل تحقيق الفوز الثاني هذا الموسم.',
      excerpt: 'تختتم الجولة الثالثة من دوري كرة القدم الأمريكية بمواجهة كلاسيكية نارية بين فيلادلفيا إيغلز ودالاس كاوبويز.',
      body: [
        'يسدل الستار على الأسبوع الثالث من دوري NFL بمباراة ليلة الإثنين المرتقبة بين فيلادلفيا ودالاس.',
        'يدخل الفريقان اللقاء بسجل انتصار وهزيمة، والفائز سينفرد بالمركز الثاني خلف واشنطن في مجموعتهما.',
        'يقود جالين هيرتس هجوم إيغلز رفقة باركلي وبراون في مواجهة دفاع دالاس الشرس بقيادة ميكا بارسونز.',
      ],
    },
  },
  'wnba-playoffs-game1-recap-clark-fever-2026': {
    fr: {
      title: 'Playoffs WNBA Match 1 : Caitlin Clark mène Fever à la victoire, Lynx et Aces au rendez-vous',
      subtitle: "Indiana s'impose 86-80 à Atlanta ; Minnesota, New York et Las Vegas tiennent leur rang à domicile.",
      excerpt: 'Caitlin Clark compile 24 points et 11 passes décisives pour offrir le Match 1 à Indiana contre Atlanta, tandis que le Lynx et les Aces assurent.',
      body: [
        "Le premier tour des playoffs WNBA 2026 a débuté dimanche avec une intensité maximale et quatre matches d'ouverture.",
        "À Atlanta, Caitlin Clark a brillé avec 24 points et 11 passes, guidant Indiana vers une victoire 86-80 à l'extérieur.",
        'Dans les autres matches, Minnesota a battu Washington 84-69, New York a dominé Golden State 79-71 et Las Vegas a disposé de Dallas 92-81.',
      ],
    },
    es: {
      title: 'Playoffs WNBA Partido 1: Caitlin Clark guía a Fever ante Dream; Lynx y Aces se imponen',
      subtitle: 'Indiana roba la ventaja de local con triunfo 86-80 en Atlanta; Minnesota, Nueva York y Las Vegas no fallan.',
      excerpt: 'Caitlin Clark firma 24 puntos y 11 asistencias para dar el primer triunfo a Indiana ante Atlanta Dream en el arranque de playoffs.',
      body: [
        'La postemporada de la WNBA 2026 abrió el domingo con cuatro partidos de primera ronda en series al mejor de tres.',
        'En Atlanta, Caitlin Clark lideró al Indiana Fever con 24 puntos y 11 asistencias para ganar 86-80 a domicilio.',
        'Minnesota Lynx superó a Washington 84-69, New York Liberty venció 79-71 a Valkyries y Las Vegas Aces batió 92-81 a Wings.',
      ],
    },
    de: {
      title: 'WNBA-Playoffs Spiel 1: Caitlin Clark führt Fever zum Auswärtssieg; Lynx und Aces souverän',
      subtitle: 'Indiana siegt 86:80 in Atlanta; Minnesota, New York und Las Vegas verteidigen den Heimvorteil.',
      excerpt: 'Caitlin Clark erzielt 24 Punkte und 11 Assists beim 86:80-Sieg von Indiana Fever bei den Atlanta Dream in Spiel 1 der WNBA-Playoffs.',
      body: [
        'Die WNBA-Playoffs 2026 starteten am Sonntag mit vier Auftaktpartien der Best-of-Three-Erstrundenserien.',
        'In Atlanta führte Caitlin Clark die Indiana Fever mit 24 Punkten und 11 Assists zu einem 86:80-Erfolg auf fremdem Parkett.',
        'Minnesota Lynx schlug Washington 84:69, New York Liberty bezwang Golden State 79:71 und Las Vegas Aces besiegte Dallas 92:81.',
      ],
    },
    it: {
      title: 'Playoff WNBA Gara 1: Caitlin Clark trascina Fever alla vittoria; Lynx e Aces dominano',
      subtitle: 'Indiana espugna Atlanta 86-80; Minnesota, New York e Las Vegas difendono il fattore campo.',
      excerpt: 'Caitlin Clark firma 24 punti e 11 assist guidando Indiana al successo 86-80 contro Atlanta Dream in Gara 1 dei playoff WNBA.',
      body: [
        "Il primo turno dei playoff WNBA 2026 è scattato domenica con quattro gare d'apertura al meglio delle tre sfide.",
        "Ad Atlanta, Caitlin Clark ha offerto una prova sontuosa da 24 punti e 11 assist per l'86-80 di Indiana in trasferta.",
        'Nelle altre gare, le Lynx hanno superato Washington 84-69, Liberty hanno battuto Valkyries 79-71 e le Aces hanno vinto 92-81 su Dallas.',
      ],
    },
    pl: {
      title: 'Playoffy WNBA Mecz 1: Caitlin Clark prowadzi Fever do wygranej; Lynx i Aces nie zawodzą',
      subtitle: 'Indiana wygrywa 86-80 w Atlancie; Minnesota, New York i Las Vegas utrzymują przewagę parkietu.',
      excerpt: 'Caitlin Clark zdobywa 24 punkty i 11 asyst, prowadząc Indiana Fever do zwycięstwa 86-80 w pierwszym meczu fazy pucharowej w Atlancie.',
      body: [
        'Faza play-off WNBA 2026 rozpoczęła się w niedzielę czterema meczami pierwszej rundy rozgrywanej w formule do dwóch wygranych.',
        'W Atlancie Caitlin Clark poprowadziła Fever do wyjazdowego sukcesu 86-80, notując 24 punkty i 11 asyst.',
        'Minnesota pokonała Washington 84-69, New York ograł Valkyries 79-71, a obrończynie tytułu Aces pokonały Dallas 92-81.',
      ],
    },
    zh: {
      title: 'WNBA季后赛首战：克拉克率狂热客胜梦想，山猫王牌携手开门红',
      subtitle: '印第安纳狂热客场86比80力克亚特兰大梦想；明尼苏达、纽约与拉斯维加斯主场告捷。',
      excerpt: '凯特琳-克拉克砍下24分11助攻，率领印第安纳狂热在季后赛首轮第1场客场86比80战胜亚特兰大梦想。',
      body: [
        '2026赛季WNBA季后赛周日打响，首轮三局两胜制的四场首战全面点燃战火。',
        '印第安纳狂热在客场顶住反扑，克拉克独得24分11次助攻，以86比80掀翻亚特兰大梦想夺得赛点。',
        '头号种子山猫84比69大胜神秘人，自由人79比71击败女武神，卫冕冠军王牌92比81战胜飞翼。',
      ],
    },
    ja: {
      title: 'WNBAプレーオフ第1戦：クラークがフィーバーを敵地白星に導く、リンクスとエーシズも先勝',
      subtitle: 'インディアナがアトランタで86-80勝利。ミネソタ、ニューヨーク、ラスベガスが初戦を制す。',
      excerpt: 'ケイトリン・クラークが24得点11アシストの活躍で、インディアナ・フィーバーがアトランタ・ドリームとの第1戦を86-80で制した。',
      body: [
        '2026年WNBAプレーオフが開幕し、3戦2勝制のファーストラウンド第1戦4試合が行われた。',
        'フィーバーは敵地でケイトリン・クラークが24得点11アシストを記録し、ドリームに86-80で逆転勝利を収めた。',
        '第1シードのリンクスはミスティクスに84-69で快勝し、リバティとエーシズもそれぞれ白星発進を決めた。',
      ],
    },
    ko: {
      title: 'WNBA 플레이오프 1차전: 케이틀린 클라크 피버 원정 승리 견인, 링스와 에이시스도 완승',
      subtitle: '인디애나, 애틀랜타 원정서 86-80 제압; 미네소타, 뉴욕, 라스베이거스도 1차전 승리.',
      excerpt: '케이틀린 클라크가 24득점 11어시스트를 기록하며 인디애나 피버를 애틀랜타 드림전 86-80 원정 승리로 이끌었다.',
      body: [
        '2026 WNBA 플레이오프 1라운드 3전 2선승제 시리즈가 일요일 4경기 개막전으로 막을 올렸다.',
        '인디애나 피버는 케이틀린 클라크의 24득점 11어시스트 맹활약에 힘입어 애틀랜타를 86-80으로 제압했다.',
        '1번 시드 미네소타 링스는 워싱턴을 84-69로 완파했고, 뉴욕 리버티와 라스베이거스 에이시스도 첫 승을 챙겼다.',
      ],
    },
    ar: {
      title: 'أدوار WNBA الإقصائية الجولة 1: كلارك تقود فيفر للفوز خارج الديار ولينكس وإيسيز يتألقان',
      subtitle: 'إنديانا تخطف فوزا ثمينا 86-80 في أتلانتا؛ ومينيسوتا ونيويورك ولاس فيغاس تحسم مبارياتها.',
      excerpt: 'سجلت كيتلين كلارك 24 نقطة و11 تمريرة حاسمة لتقود إنديانا فيفر للفوز 86-80 على أتلانتا في افتتاح الأدوار الإقصائية.',
      body: [
        'انطلقت منافسات الأدوار الإقصائية لدوري السلة الأمريكي للسيدات يوم الأحد بأربع مباريات قوية في الجولة الأولى.',
        'في أتلانتا، تألقت كيتلين كلارك بتسجيل 24 نقطة و11 تمريرة حاسمة لتمنح إنديانا الفوز بنتيجة 86-80 خارج الديار.',
        'وفي باقي المباريات، تفوقت مينيسوتا على واشنطن 84-69، وتغلب نيويورك على فالكيريز 79-71 وإيسيز على دالاس 92-81.',
      ],
    },
  },
  'premier-league-mw6-standings-city-18pts-2026': {
    fr: {
      title: 'Bilan 6e journée Premier League : Manchester City seul au sommet avec 18 points',
      subtitle: 'Les hommes de Guardiola devancent Arsenal de trois longueurs avant la semaine de Ligue des Champions.',
      excerpt: 'Manchester City boucle la 6e journée de Premier League avec un sans-faute (6-0-0) et 18 points en tête du classement.',
      body: [
        'Après six journées de Premier League, Manchester City continue son cavalier seul en tête du championnat anglais.',
        'Vainqueurs 2-1 de Newcastle samedi grâce à Haaland et Bernardo Silva, les Cityzens comptent 18 points sur 18 possibles.',
        'Arsenal reste dauphin avec 15 points après sa victoire 2-0 sur Everton, tandis que Liverpool grimpe à la 3e place avec 12 points.',
      ],
    },
    es: {
      title: 'Resumen Jornada 6 Premier League: Manchester City líder solitario con 18 puntos perfectos',
      subtitle: 'El equipo de Guardiola aventaja a Arsenal en tres puntos antes del regreso de la Champions League.',
      excerpt: 'Manchester City comanda la Premier League con pleno de victorias (6-0-0) y 18 puntos tras cerrarse la sexta fecha.',
      body: [
        'Cumplidas seis jornadas de la Premier League 2026-27, el Manchester City de Pep Guardiola marcha con paso perfecto.',
        'El triunfo 2-1 ante Newcastle en el Etihad elevó a los celestes a 18 puntos, con Erling Haaland sumando 10 goles en el torneo.',
        'El Arsenal es segundo con 15 puntos tras superar 2-0 al Everton, mientras que Liverpool es tercero con 12 unidades.',
      ],
    },
    de: {
      title: 'Premier League Spieltag 6: Manchester City thront mit perfekten 18 Punkten an der Spitze',
      subtitle: 'Guardiolas Team liegt drei Punkte vor Arsenal; Haaland steht bei 10 Toren vor der Champions-League-Woche.',
      excerpt: 'Manchester City beendet den 6. Spieltag der Premier League mit einer makellosen 6-0-0-Bilanz und führt die Tabelle mit 18 Punkten an.',
      body: [
        'Nach sechs Runden der Premier League 2026-27 zieht Manchester City an der Tabellenspitze einsam seine Kreise.',
        'Mit dem 2:1-Heimsieg gegen Newcastle bauten die Skyblues ihr Punktekonto auf die Maximalausbeute von 18 Zählern aus.',
        'Arsenal folgt mit 15 Punkten nach einem 2:0 gegen Everton auf Rang zwei, gefolgt von Liverpool mit 12 Punkten.',
      ],
    },
    it: {
      title: 'Premier League 6ª giornata: Manchester City solo in vetta a punteggio pieno con 18 punti',
      subtitle: "La squadra di Guardiola vanta tre punti di vantaggio sull'Arsenal prima del turno di Champions League.",
      excerpt: 'Il Manchester City chiude la sesta giornata di Premier League a punteggio pieno (6-0-0) e 18 punti, davanti ad Arsenal e Liverpool.',
      body: [
        'Dopo sei giornate di campionato, il Manchester City continua la sua marcia perfetta in vetta alla Premier League.',
        'Il successo per 2-1 contro il Newcastle ha permesso ai Citizens di salire a quota 18 punti, con Haaland a quota 10 reti.',
        "L'Arsenal insegue a quota 15 dopo il 2-0 sull'Everton, mentre il Liverpool occupa il terzo gradino del podio con 12 punti.",
      ],
    },
    pl: {
      title: 'Podsumowanie 6. kolejki Premier League: Manchester City na szczycie z kompletem 18 punktów',
      subtitle: 'Ekipa Guardioli ma trzy punkty przewagi nad Arsenalem przed tygodniem z Ligą Mistrzów.',
      excerpt: 'Manchester City zamyka 6. kolejkę Premier League z bilansem 6-0-0 i prowadzi w tabeli z dorobkiem 18 punktów.',
      body: [
        'Po sześciu kolejkach Premier League 2026-27 Manchester City może pochwalić się kompletem zwycięstw.',
        'Wygrana 2-1 z Newcastle na Etihad Stadium dała ekipie Pepa Guardioli 18 punktów, a Haaland ma już 10 bramek na koncie.',
        'Drugie miejsce zajmuje Arsenal z 15 punktami po zwycięstwie 2-0 nad Evertonem, a trzeci jest Liverpool z 12 oczkami.',
      ],
    },
    zh: {
      title: '英超第6轮综述：曼城6战全胜积18分领跑，哈兰德6场轰10球',
      subtitle: '瓜迪奥拉球队领先阿森纳3分稳居榜首，欧冠第2比赛日周中打响。',
      excerpt: '英超第6轮战罢，曼城以6战全胜积18分的完美战绩独占榜首，阿森纳积15分紧随其后，利物浦积12分位列第三。',
      body: [
        '2026-27赛季英格兰超级联赛战罢6轮，曼城展现出无可阻挡的统治力，豪取开局六连胜。',
        '在伊蒂哈德球场2比1力克纽卡斯尔联后，曼城积分达到18分，哈兰德前6轮已打入惊人的10粒联赛进球。',
        '阿森纳主场2比0轻取埃弗顿积15分位列次席，利物浦客场3比1战胜桑德兰以12分升至第三位。',
      ],
    },
    ja: {
      title: 'プレミアリーグ第6節総括：マンチェスター・シティが開幕6連勝で勝点18首位独走',
      subtitle: 'ハーランドが6戦10発と大暴れ。2位アーセナルに勝点3差をつけ欧州CLウィークへ。',
      excerpt: 'プレミアリーグ第6節が終了し、マンチェスター・シティが6戦全勝の勝点18で首位を堅持。2位アーセナルが追走する。',
      body: [
        '2026-27プレミアリーグは第6節を終え、グアルディオラ率いるマンチェスター・シティが唯一の全勝をキープしている。',
        'ニューカッスルを2-1で下したシティは勝点18に到達し、ハーランドは早くもリーグ通算10ゴール目をマークした。',
        'エヴァートンに2-0で勝利したアーセナルが勝点15で2位、サンダーランドに勝ったリヴァプールが勝点12で3位につける。',
      ],
    },
    ko: {
      title: '프리미어리그 6라운드 결산: 맨체스터 시티, 6연승 승점 18점으로 단독 선두 질주',
      subtitle: '홀란 6경기 10골 폭발. 아스널에 승점 3점 앞선 채 챔피언스리그 주간 돌입.',
      excerpt: '프리미어리그 6라운드가 마무리된 가운데 맨체스터 시티가 6전 전승 승점 18점으로 선두를 질주하고 있다.',
      body: [
        '2026-27 프리미어리그 6라운드가 끝난 현재, 펩 과르디올라 감독의 맨체스터 시티가 무결점 6연승을 달리고 있다.',
        '뉴캐슬을 2-1로 꺾은 맨시티는 승점 18점을 확보했으며, 엘링 홀란은 6경기 만에 10호 골을 기록했다.',
        '에버턴을 2-0으로 제압한 아스널이 승점 15점으로 2위, 선덜랜드를 3-1로 꺾은 리버풀이 승점 12점으로 3위를 달린다.',
      ],
    },
    ar: {
      title: 'حصاد الجولة 6 من الدوري الإنجليزي: مانشستر سيتي بالعلامة الكاملة برصيد 18 نقطة',
      subtitle: 'كتيبة غوارديولا تبتعد بثلاث نقاط عن آرسنال وهالاند يسجل 10 أهداف قبل أسبوع الأبطال.',
      excerpt: 'يتصدر مانشستر سيتي جدول ترتيب الدوري الإنجليزي الممتاز برصيد 18 نقطة من 6 انتصارات متتالية.',
      body: [
        'مع نهاية الجولة السادسة من الدوري الإنجليزي الممتاز 2026-27، يواصل مانشستر سيتي انطلاقته المثالية في الصدارة.',
        'وصل السيتي إلى النقطة 18 بعد فوزه على نيوكاسل 2-1، ورفع إرلينغ هالاند رصيده التهديفي إلى 10 أهداف في 6 مباريات.',
        'ويحتل آرسنال المركز الثاني برصيد 15 نقطة بعد تجاوزه إيفرتون بهدفين دون رد، يليه ليفربول ثالثا برصيد 12 نقطة.',
      ],
    },
  },
  'singapore-gp-preview-antonelli-title-march-2026': {
    fr: {
      title: "Présentation GP de Singapour : Antonelli arrive avec 45 points d'avance sous les projecteurs de Marina Bay",
      subtitle: "Le rookie de Mercedes aborde l'épreuve la plus éprouvante du calendrier après sa victoire à Bakou.",
      excerpt: 'Kimi Antonelli se prépare au défi nocturne de Marina Bay en leader solide du championnat de Formule 1 avant le GP de Singapour.',
      body: [
        'La Formule 1 quitte Bakou pour rejoindre la chaleur tropicale et les 1 600 projecteurs du circuit urbain de Marina Bay à Singapour.',
        'Fort de sa victoire autoritaire en Azerbaïdjan, Kimi Antonelli mène le championnat du monde des pilotes avec 317 points.',
        'George Russell (229 pts), Lewis Hamilton (201 pts) et Lando Norris (198 pts) tenteront de contester la suprématie de Mercedes.',
      ],
    },
    es: {
      title: 'Previa GP de Singapur: Antonelli defiende 45 puntos de renta bajo los focos de Marina Bay',
      subtitle: 'El joven prodigio de Mercedes afronta el desafío físico más extremo de la F1 tras vencer en Bakú.',
      excerpt: 'Kimi Antonelli llega al Gran Premio de Singapur como líder del Mundial de Fórmula 1 para encarar la exigente carrera nocturna de Marina Bay.',
      body: [
        'La Fórmula 1 aterriza en el caluroso trazado urbano de Marina Bay para disputar la 18ª ronda del Mundial bajo los reflectores.',
        'Tras su triunfo incontestable desde la pole en Bakú, Kimi Antonelli comanda la clasificación de pilotos con 317 puntos.',
        'George Russell (229 pts), Lewis Hamilton (201 pts) y Lando Norris (198 pts) buscarán desafiar el dominio de las flechas plateadas.',
      ],
    },
    de: {
      title: 'Vorschau GP von Singapur: Antonelli reist mit 45 Punkten Vorsprung ins Flutlicht von Marina Bay',
      subtitle: 'Mercedes-Rookie stellt sich nach dem Baku-Sieg der härtesten Hitzeschlacht des Formel-1-Jahres.',
      excerpt: 'Kimi Antonelli führt die Formel-1-Weltmeisterschaft vor dem prestigeträchtigen Nachtrennen auf dem Marina Bay Street Circuit an.',
      body: [
        'Die Formel 1 zieht direkt von Baku nach Singapur, wo das Nachtrennen auf dem Marina Bay Street Circuit ansteht.',
        'Nach seinem Start-Ziel-Sieg in Aserbaidschan führt Shootingstar Kimi Antonelli die Fahrer-WM mit 317 Punkten souverän an.',
        'Teamkollege George Russell (229 Pkt.), Lewis Hamilton (201 Pkt.) und Lando Norris (198 Pkt.) wollen in der Tropenhitze kontern.',
      ],
    },
    it: {
      title: 'Anteprima GP Singapore: Antonelli vola a Marina Bay forte di 45 punti di vantaggio',
      subtitle: "Il fenomeno della Mercedes affronta la sfida più dura dell'anno sotto i riflettori dopo il trionfo di Baku.",
      excerpt: "Kimi Antonelli guida il mondiale di Formula 1 verso l'appuntamento notturno di Singapore sul tracciato di Marina Bay.",
      body: [
        "La Formula 1 si sposta da Baku all'umidità tropicale di Marina Bay per la 18ª tappa del Campionato Mondiale 2026.",
        'Dopo il dominante successo in terra azera, Kimi Antonelli comanda la classifica piloti con 317 punti iridati.',
        'George Russell a quota 229, Lewis Hamilton a 201 e Lando Norris a 198 inseguono la Mercedes sulle strade asiatiche.',
      ],
    },
    pl: {
      title: 'Zapowiedź GP Singapuru: Antonelli z przewagą 45 punktów rusza na ulice Marina Bay',
      subtitle: 'Rookie Mercedesa zmierzy się z najtrudniejszym fizycznie wyścigiem F1 w blasku jupiterów po triumfie w Baku.',
      excerpt: 'Kimi Antonelli prowadzi w klasyfikacji generalnej F1 i szykuje się do wymagającego nocnego wyścigu o Grand Prix Singapuru.',
      body: [
        'Formuła 1 przenosi się z Baku do Singapuru, gdzie na Marina Bay Street Circuit odbędzie się słynny nocny wyścig.',
        'Po znakomitym zwycięstwie w Azerbejdżanie Kimi Antonelli pewnie przewodzi stawce kierowców z dorobkiem 317 punktów.',
        'George Russell (229 pkt), Lewis Hamilton (201 pkt) oraz Lando Norris (198 pkt) spróbują zatrzymać marsz młodego Włocha.',
      ],
    },
    zh: {
      title: '新加坡大奖赛前瞻：安东内利携45分优势征战滨海湾夜战',
      subtitle: '梅赛德斯新星巴库夺冠后直面F1最严酷体能考验，领跑车手积分榜。',
      excerpt: 'F1锦标赛转战新加坡滨海湾街道赛道，领头羊基米-安东内利在1600盏泛光灯下开启第18站卫冕之旅。',
      body: [
        'F1赛季马不停蹄转战东南亚，在新加坡滨海湾街道赛道展开年度最具挑战性的夜间街道赛对决。',
        '在巴库杆位发车强势夺冠后，梅赛德斯超级新人安东内利已手握317个车手积分遥遥领先。',
        '队友拉塞尔（229分）、汉密尔顿（201分）与诺里斯（198分）将全力在高温高湿考验中发起反扑。',
      ],
    },
    ja: {
      title: 'シンガポールGP展望：アントネッリが45点リードでマリーナベイの夜戦へ挑む',
      subtitle: 'バクー完全勝利のメルセデス新鋭が、F1屈指の過酷な熱帯夜市街地コースで王座進撃を期す。',
      excerpt: 'キミ・アントネッリがドライバーズ選手権首位としてシンガポールGPへ。マリーナベイのナイターレースで激突。',
      body: [
        'F1サーカスはバクーからシンガポールのマリーナベイ市街地サーキットへ直行し、第18戦を迎える。',
        'アゼルバイジャンGPでポール・トゥ・ウィンを飾ったキミ・アントネッリは317ポイントで選手権を牽引。',
        'ラッセル（229点）、ハミルトン（201点）、ノリス（198点）が過酷な熱帯夜でメルセデス追撃を図る。',
      ],
    },
    ko: {
      title: '싱가포르 GP 프리뷰: 안토넬리, 45점 차 리드로 마리나 베이 야간 레이스 출격',
      subtitle: '바쿠 완승 거둔 메르세데스 루키, 1,600개 조명 아래 F1 최고 난도 시가지 서킷 격돌.',
      excerpt: '바쿠 우승을 차지한 키미 안토넬리가 317점으로 챔피언십 선두를 굳건히 지키며 싱가포르 GP 야간 레이스에 나선다.',
      body: [
        '포뮬러 1 서커스가 바쿠에서 싱가포르 마리나 베이 시가지 서킷으로 무대를 옮겨 18라운드를 치른다.',
        '바쿠에서 폴투윈을 완성한 메르세데스의 루키 키미 안토넬리는 317점으로 드라이버 챔피언십 선두를 질주하고 있다.',
        '조지 러셀(229점), 루이스 해밀턴(201점), 랜도 노리스(198점)가 고온다습한 싱가포르 밤하늘 아래 반격에 나선다.',
      ],
    },
    ar: {
      title: 'تقديم جائزة سنغافورة الكبرى: أنتونيللي يتصدر البطولة بفارق 45 نقطة تحت أضواء مارينا باي',
      subtitle: 'نجم مرسيدس الصاعد يتأهب للاختبار البدني الأقسى في فورمولا 1 عقب فوزه المستحق في باكو.',
      excerpt: 'يقود كيمي أنتونيللي بطولة العالم لسباقات فورمولا 1 نحو حلبة مارينا باي في سنغافورة لخوض السباق الليلي المرتقب.',
      body: [
        'تنتقل بطولة العالم لسباقات فورمولا 1 مباشرة من باكو إلى حرارة ورطوبة حلبة مارينا باي في سنغافورة لخوض الجولة 18.',
        'بعد فوزه الرائع في باكو من قطب الانطلاق الأول، يتصدر كيمي أنتونيللي ترتيب السائقين برصيد 317 نقطة.',
        'ويسعى زميله جورج راسل (229 نقطة) ولويس هاميلتون ولاندو نوريس لتحدي هيمنة مرسيدس تحت الأضواء الكاشفة.',
      ],
    },
  },
  'eagles-cowboys-mnf-week3-final-2026': {
    fr: {
      title: 'Eagles 24-20 Cowboys : Hurts et Barkley scellent le thriller du Monday Night pour clore la 3e semaine',
      subtitle: 'La défense de Philadelphie stoppe Dallas en quatrième tentative pour valider un bilan de 2-1 et la 2e place en NFC Est.',
      excerpt: 'Le Monday Night Football clôt la 3e semaine avec la victoire des Eagles 24-20 contre Dallas grâce à Jalen Hurts, Saquon Barkley et un arrêt défensif décisif.',
      body: [
        'La 3e semaine de la saison NFL 2026 s’est terminée sur un duel acharné, et Philadelphie a tenu bon pour s’imposer 24-20 face aux Dallas Cowboys dans un Lincoln Financial Field en fusion.',
        'Jalen Hurts a cumulé 240 yards à la passe et un touchdown, tout en signant son 45e touchdown au sol en carrière. Saquon Barkley a porté l’attaque avec 116 yards en 22 courses et un touchdown décisif de 18 yards au quatrième quart-temps.',
        'Dak Prescott (262 yards, 2 TD pour CeeDee Lamb) a ramené Dallas à quatre longueurs, mais Brandon Graham et Jalen Carter ont stoppé les Cowboys sur quatrième tentative à 1:12 de la fin. Philadelphie monte à 2-1 tandis que Dallas glisse à 1-2.',
      ],
    },
    es: {
      title: 'Eagles 24-20 Cowboys: Hurts y Barkley sellan el triunfo en Monday Night para cerrar la semana 3',
      subtitle: 'La defensa de Filadelfia frena a Dallas en cuarta oportunidad para asegurar récord de 2-1 y segundo lugar en la NFC Este.',
      excerpt: 'Monday Night Football concluye la semana 3 con la victoria de Eagles 24-20 sobre Dallas de la mano de Jalen Hurts, Saquon Barkley y una parada defensiva crucial.',
      body: [
        'La semana 3 de la NFL cerró con una de las mayores rivalidades del deporte, y Filadelfia resistió con firmeza para vencer 24-20 a los Dallas Cowboys ante un Lincoln Financial Field encendido.',
        'Jalen Hurts sumó 240 yardas por aire y una anotación, además de su 45º touchdown terrestre de por vida. Saquon Barkley lideró el ataque con 116 yardas en 22 acarreos y un touchdown determinante de 18 yardas en el último periodo.',
        'Dak Prescott (262 yardas, 2 TD con CeeDee Lamb) acercó a Dallas, pero Brandon Graham y Jalen Carter detuvieron a los Cowboys en cuarta oportunidad con 1:12 en el reloj. Filadelfia queda 2-1 y Dallas cae a 1-2.',
      ],
    },
    de: {
      title: 'Eagles 24:20 Cowboys: Hurts und Barkley entscheiden Monday-Night-Krimi zum Abschluss von Woche 3',
      subtitle: 'Philadelphias Defense stoppt Dallas im vierten Versuch und sichert 2:1-Bilanz sowie Rang zwei in der NFC East.',
      excerpt: 'Monday Night Football schließt Woche 3 mit einem 24:20-Sieg der Eagles über Dallas ab, angeführt von Hurts, Barkley und einem späten Stopp.',
      body: [
        'Woche 3 der NFL-Saison 2026 endete mit einem packenden Divisionsduell: Die Philadelphia Eagles besiegten die Dallas Cowboys mit 24:20 im Lincoln Financial Field.',
        'Jalen Hurts warf für 240 Yards und einen Touchdown und erzielte seinen 45. Regular-Season-Lauf-Touchdown. Saquon Barkley dominierte mit 116 Rushing Yards bei 22 Versuchen und einem 18-Yard-Score im Schlussviertel.',
        'Dak Prescott (262 Yards, 2 TD auf CeeDee Lamb) brachte Dallas heran, doch Brandon Graham und Jalen Carter erzwangen 1:12 Minuten vor Ende einen Turnover on Downs. Philadelphia klettert auf 2-1, Dallas fällt auf 1-2.',
      ],
    },
    it: {
      title: 'Eagles 24-20 Cowboys: Hurts e Barkley firmano il Monday Night e chiudono la week 3',
      subtitle: 'La difesa di Philadelphia ferma Dallas al quarto down e conquista il record di 2-1 al secondo posto nella NFC East.',
      excerpt: 'Il Monday Night Football manda in archivio la week 3 con il successo degli Eagles per 24-20 su Dallas firmato da Hurts, Barkley e dalla difesa.',
      body: [
        'La terza settimana NFL si è chiusa con un classico della NFC East: gli Eagles hanno superato i Dallas Cowboys per 24-20 davanti al pubblico del Lincoln Financial Field.',
        'Jalen Hurts ha accumulato 240 yard su passaggio con un touchdown e ha segnato la sua 45ª meta su corsa in carriera. Saquon Barkley ha trascinato l’attacco con 116 yard su 22 portate e la corsa decisiva da 18 yard nell’ultimo quarto.',
        'Dak Prescott (262 yard e 2 TD per CeeDee Lamb) ha tentato la rimonta, ma Brandon Graham e Jalen Carter hanno sigillato la gara fermando i texani su quarto down a 1:12 dalla fine. Philadelphia sale a 2-1, Dallas scende a 1-2.',
      ],
    },
    pl: {
      title: 'Eagles 24-20 Cowboys: Hurts i Barkley pieczętują triumf w Monday Night na koniec 3. tygodnia',
      subtitle: 'Obrona Filadelfii zatrzymuje Dallas w czwartej próbie i zapewnia bilans 2-1 oraz drugie miejsce w NFC East.',
      excerpt: 'Monday Night Football kończy 3. tydzień wygraną Eagles 24-20 nad Dallas dzięki znakomitej postawie Hurtsa, Barkleya i kluczowemu zatrzymaniu w obronie.',
      body: [
        'Trzeci tydzień sezonu NFL 2026 zamknął się wielkim starciem dywizyjnym, w którym Philadelphia Eagles pokonała Dallas Cowboys 24-20 na Lincoln Financial Field.',
        'Jalen Hurts zanotował 240 jardów podaniowych, przyłożenie górą oraz swoje 45. przyłożenie dołem w karierze. Saquon Barkley wywalczył 116 jardów w 22 biegach i decydujące 18-jardowe przyłożenie w czwartej kwarcie.',
        'Dak Prescott (262 jardy, 2 TD do CeeDee Lamba) poderwał Cowboys do ataku, lecz Brandon Graham i Jalen Carter zatrzymali akcję na 1:12 przed końcem. Eagles osiągają bilans 2-1, a Dallas spada na 1-2.',
      ],
    },
    zh: {
      title: '老鹰 24-20 牛仔：赫茨与巴克利决胜周一之夜，第3周战幕落下',
      subtitle: '费城防线终场前四档防守成功锁定胜局，以2胜1负位列国联东区次席。',
      excerpt: '周一橄榄球夜落下第3周帷幕，费城老鹰在主场以24-20击退达拉斯牛仔，赫茨与巴克利合力统治进攻端。',
      body: [
        '2026年NFL常规赛第3周在林肯金融球场的火爆氛围中收官，费城老鹰以24-20力克劲敌达拉斯牛仔。',
        '四分卫赫茨贡献240码传球与1次达阵，并完成个人常规赛生涯第45次冲球达阵。巴克利全场狂奔116码，并在第四节完成18码致胜冲球得分。',
        '普雷斯科特虽送出262码及2次达阵追近比分，但在比赛仅剩1分12秒时，老鹰防线成功阻截牛仔的四档强攻，将战绩提升至2胜1负，牛仔战绩降为1胜2负。',
      ],
    },
    ja: {
      title: 'イーグルス 24-20 カウボーイズ：ハーツとバークリーがMNF激闘を制し第3週終幕',
      subtitle: 'フィラデルフィア守備陣が終盤の4thダウンを阻止し2勝1敗でNFC東地区2位を確保。',
      excerpt: 'マンデーナイトフットボールでイーグルスがカウボーイズを24-20で撃破。ハーツとバークリーの活躍でNFL第3週が完結。',
      body: [
        '2026年NFL第3週は激闘のNFC東地区ライバル対決で幕を閉じ、イーグルスが本拠地リンカーン・フィナンシャル・フィールドで24-20の勝利を収めた。',
        'QBハーツはパス240ヤードと1TD、さらに通算45個目となるランTDを記録。RBバークリーは22回116ヤードの力走と第4Qの18ヤード決定打TDで試合を支配した。',
        'カウボーイズのプレスコットはラムへ2本のTDパスを通すも、残り1分12秒での4thダウンギャンブルをグラハムらの堅守が阻止。フィラデルフィアが2勝1敗とした。',
      ],
    },
    ko: {
      title: '이글스 24-20 카우보이스: 허츠와 바클리, 먼데이 나이트 혈투 끝내며 3주 차 마무리',
      subtitle: '필라델피아 수비진의 경기 막판 4th 다운 저지로 2승 1패 및 NFC 동부 2위 확보.',
      excerpt: '필라델피아 이글스가 먼데이 나이트 풋볼에서 댈러스 카우보이스를 24-20으로 꺾고 NFL 3주 차를 마감했다.',
      body: [
        '2026 NFL 3주 차 마지막 경기에서 필라델피아 이글스가 링컨 파이낸셜 필드에서 댈러스 카우보이스를 24-20으로 제압했다.',
        '제일런 허츠는 패스 240야드 1TD와 통산 45번째 러싱 TD를 기록했고, 사콴 바클리는 22번의 러싱으로 116야드와 4쿼터 결승 18야드 TD를 폭발시켰다.',
        '프레스콧이 램과 2개의 터치다운을 합작하며 추격했으나 경기 종료 1분 12초 전 이글스 수비진이 4th 다운 공격을 막아내며 승리를 확정지었다.',
      ],
    },
    ar: {
      title: 'إيغلز 24-20 كاوبويز: هيرتس وباركلي يحسمان إثارة ليلة الإثنين في ختام الأسبوع الثالث',
      subtitle: 'دفاع فيلادلفيا يوقف محاولة دالاس في المحاولة الرابعة ليضمن سجل 2-1 والمركز الثاني في الشرق.',
      excerpt: 'اختتمت منافسات الأسبوع الثالث من دوري كرة القدم الأمريكية بفوز إيغلز 24-20 على كاوبويز بفضل تألق هيرتس وباركلي وتصدي دفاعي حاسم.',
      body: [
        'اختتم الأسبوع الثالث من موسم NFL 2026 بقمة نارية تفوق فيها فيلادلفيا إيغلز على دالاس كاوبويز بنتيجة 24-20 على ملعب لينكون فاينانشال فيلد.',
        'حقق جايلن هيرتس 240 ياردة تمريرية وسجل هدف الركض رقم 45 في مسيرته، في حين أبدع ساكوان باركلي بحصده 116 ياردة وهبوطا حاسما في الربع الأخير.',
        'ورغم جهود داك بريسكوت وتمريرتيه الحاسمين لسيدي لامب، أوقف دفاع إيغلز هجوم دالاس عند المحاولة الرابعة قبل 1:12 دقيقة من النهاية ليرفع رصيده إلى انتصارين وهزيمة.',
      ],
    },
  },
  'wnba-playoffs-game2-elimination-fever-dream-2026': {
    fr: {
      title: 'Play-offs WNBA Match 2 : Caitlin Clark et le Fever visent le sweep face au Dream dos au mur',
      subtitle: 'Atlanta joue sa survie à domicile tandis qu’Indiana espère boucler la série du premier tour.',
      excerpt: 'Mardi soir s’annoncent les matches 2 couperets en WNBA : Caitlin Clark et le Fever peuvent rallier les demi-finales dès ce soir.',
      body: [
        'Le premier tour des play-offs WNBA 2026 ne laisse aucun répit : ce mardi soir à Atlanta, le Dream dispute déjà un match à élimination directe contre l’Indiana Fever.',
        'Vainqueur 86-80 dimanche grâce à 24 points et 11 passes de Caitlin Clark, Indiana mène 1-0 dans cette série au meilleur des trois manches et peut décrocher son ticket pour les demi-finales.',
        'À Minneapolis, les Minnesota Lynx mènent également 1-0 face aux Washington Mystics après la démonstration de Napheesa Collier, avec la qualification en ligne de mire.',
      ],
    },
    es: {
      title: 'Playoffs WNBA Partido 2: Caitlin Clark y Fever buscan barrer al Dream contra las cuerdas',
      subtitle: 'Atlanta encara la eliminación en casa mientras Indiana pretende liquidar la primera ronda.',
      excerpt: 'El martes llega la tensión del Juego 2 en los playoffs de la WNBA con Indiana y Minnesota buscando asegurar su pase a semifinales.',
      body: [
        'La primera ronda de los playoffs WNBA 2026 avanza sin descanso: este martes en Atlanta, el Dream afronta un duelo de vida o muerte frente a Indiana Fever.',
        'Tras ganar 86-80 el domingo con 24 puntos y 11 asistencias de Caitlin Clark, Indiana lidera 1-0 la serie al mejor de tres y puede sellar su boleto a semifinales.',
        'En Minneapolis, Minnesota Lynx también comanda 1-0 su cruce ante Washington Mystics tras la brillante actuación de Napheesa Collier y busca barrer la serie.',
      ],
    },
    de: {
      title: 'WNBA-Playoffs Spiel 2: Caitlin Clark und die Fever wollen den Sweep gegen die Dream',
      subtitle: 'Atlanta steht zu Hause vor dem Saisonaus, während Indiana den Halbfinaleinzug perfekt machen kann.',
      excerpt: 'Am Dienstagabend droht das Aus im WNBA-Playoff-Auftakt: Caitlin Clark und Indiana können mit einem Sieg in Atlanta die Serie entscheiden.',
      body: [
        'Die WNBA-Playoffs 2026 kennen kein langes Abtasten: Am Dienstagabend steht für die Atlanta Dream im Duell mit den Indiana Fever die Saison auf dem Spiel.',
        'Nach dem 86:80-Auftaktsieg am Sonntag, angeführt von Caitlin Clarks 24 Punkten und 11 Assists, führt Indiana in der Best-of-Three-Serie mit 1:0 und kann den Halbfinaleinzug klarmachen.',
        'In Minneapolis empfangen die topgesetzten Minnesota Lynx die Washington Mystics mit einer 1:0-Führung im Rücken und wollen nach Colliers Gala ebenfalls den Sweep.',
      ],
    },
    it: {
      title: 'Playoff WNBA Gara 2: Caitlin Clark e le Fever puntano allo sweep contro le Dream a rischio eliminazione',
      subtitle: 'Atlanta si gioca la stagione in casa mentre Indiana cerca il pass per le semifinali.',
      excerpt: 'Martedì sera di gara 2 nei playoff WNBA: Caitlin Clark e Indiana possono chiudere la serie e volare al turno successivo.',
      body: [
        'Il primo turno dei playoff WNBA 2026 è subito da dentro o fuori: martedì sera ad Atlanta le Dream affrontano l’eliminazione contro le Indiana Fever.',
        'Dopo l’86-80 di domenica firmato dai 24 punti e 11 assist di Caitlin Clark, Indiana conduce 1-0 nella serie al meglio delle tre gare e ha il match point.',
        'A Minneapolis le Minnesota Lynx ospitano le Washington Mystics forti dell’1-0 firmato Napheesa Collier e puntano a chiudere i conti senza arrivare a gara 3.',
      ],
    },
    pl: {
      title: 'Play-offy WNBA Mecz 2: Caitlin Clark i Fever chcą zamknąć serię z Dream',
      subtitle: 'Atlanta gra o przetrwanie u siebie, a Indiana celuje w błyskawiczny awans do półfinału.',
      excerpt: 'Wtorkowe mecze nr 2 w play-offach WNBA przynoszą walkę o przetrwanie: Fever i Lynx mogą już dziś zapewnić sobie awans.',
      body: [
        'Pierwsza runda play-offów WNBA 2026 nie wybacza błędów: we wtorek w Atlancie miejscowe Dream stają przed widmem odpadnięcia w starciu z Indiana Fever.',
        'Po zwycięstwie 86-80 w niedzielę, w którym Caitlin Clark zdobyła 24 punkty i 11 asyst, Indiana prowadzi 1-0 w serii do dwóch zwycięstw i stoi przed szansą na awans.',
        'W Minneapolis najwyżej rozstawione Minnesota Lynx prowadzą 1-0 z Washington Mystics i po znakomitej grze Napheesy Collier także chcą przypieczętować awans.',
      ],
    },
    zh: {
      title: 'WNBA季后赛第2战：克拉克率狂热冲击横扫，梦想背水一战',
      subtitle: '亚特兰大主场迎来生死决战，印第安纳期盼连胜提前锁定半决赛席位。',
      excerpt: 'WNBA首轮第2场较量于周二打响，克拉克与狂热力争横扫梦想，山猫同样手握赛点迎战神秘人。',
      body: [
        '2026年WNBA季后赛首轮争夺白热化：周二晚间，亚特兰大梦想在主场迎来关乎赛季命运的生死决战。',
        '凭借克拉克首战24分11次助攻的神勇表现，印第安纳狂热在客场以86-80先拔头筹，在三战两胜制系列赛中占据赛点。',
        '在明尼阿波利斯，头号种子明尼苏达山猫同样以1-0领先华盛顿神秘人，科利尔状态正佳，全力争取横扫晋级。',
      ],
    },
    ja: {
      title: 'WNBAプレーオフ第2戦：クラーク擁するフィーバーがスイープ狙う、ドリームは崖っぷち',
      subtitle: 'アトランタがホームで背水の陣、インディアナは開幕節でのセミファイナル進出に王手。' ,
      excerpt: '火曜日にWNBAプレーオフ第2戦が開催。ケイトリン・クラークとフィーバーがドリーム撃破で4強入りを目指す。',
      body: [
        '2026年WNBAプレーオフ第1ラウンドは火曜夜、早くもサドンデスを迎える。アトランタ・ドリームが本拠地で敗退の危機に直面。',
        '初戦で24得点11アシストを叩き出したケイトリン・クラークの活躍により、フィーバーは86-80で先勝し1勝0敗で準決勝進出へあと1勝。',
        'ミネアポリスでも第1シードのリンクスがミスティクスを1勝0敗と追い詰めており、コリアーを中心に連勝突破を期す。',
      ],
    },
    ko: {
      title: 'WNBA 플레이오프 2차전: 케이틀린 클라크의 피버, 드림 상대 스윕 및 4강 조기 확정 정조준',
      subtitle: '애틀랜타 홈에서 벼랑 끝 탈락 위기, 인디애나는 1라운드 조기 통과 노린다.',
      excerpt: '화요일 WNBA 플레이오프 2차전에서 인디애나 피버와 미네소타 링스가 2연승으로 준결승 진출 확정을 노린다.',
      body: [
        '2026 WNBA 플레이오프 1라운드가 화요일 밤 단판 탈락의 긴장감 속에 2차전에 돌입한다. 애틀랜타 드림이 홈에서 배수의 진을 친다.',
        '1차전에서 24점 11어시스트를 폭발시킨 케이틀린 클라크의 활약으로 86-80 승리를 거둔 피버는 3전 2선승제에서 1승만 더하면 4강에 오른다.',
        '미니애폴리스의 1번 시드 미네소타 링스 역시 나피사 콜리어를 앞세워 워싱턴 미스틱스를 상대로 스윕을 노린다.',
      ],
    },
    ar: {
      title: 'تصفيات WNBA المباراة الثانية: كايتلين كلارك وفيفر يتطلعان لحسم التأهل أمام دريم',
      subtitle: 'أتلانتا يواجه خطر الإقصاء على أرضه بينما يسعى إنديانا لبلوغ نصف النهائي مبكرا.',
      excerpt: 'تنطلق مواجهات المباراة الثانية في تصفيات دوري السلة النسائي الأمريكي حيث يقترب فيفر ولينكس من حسم بطاقتي نصف النهائي.',
      body: [
        'تشهد تصفيات WNBA 2026 ليلة حاسمة يوم الثلاثاء في أتلانتا حيث يخوض فريق دريم مواجهة البقاء أمام إنديانا فيفر.',
        'بعد الفوز 86-80 يوم الأحد بفضل 24 نقطة و11 تمريرة حاسمة من كايتلين كلارك، يتقدم فيفر 1-0 ويحتاج إلى انتصار واحد للتأهل.',
        'وفي مينيابوليس، يسعى مينيسوتا لينكس المتصدر إلى تكرار فوزه على واشنطن ميستيكس بعد تألق نافيسا كوليير في المباراة الأولى.',
      ],
    },
  },
  'premier-league-mw7-preview-haaland-city-march-2026': {
    fr: {
      title: 'Présentation Premier League J7 : Haaland et City visent un septième succès de rang',
      subtitle: 'L’équipe de Guardiola défend son sans-faute à Brentford pendant qu’Arsenal et Liverpool restent en embuscade.',
      excerpt: 'Manchester City caracole en tête de Premier League avec 18 points alors qu’Erling Haaland affole les compteurs avant la 7e journée.',
      body: [
        'Après six journées en Premier League 2026-27, Manchester City réalise un sans-faute absolu avec six victoires et 18 points au compteur.',
        'Erling Haaland affiche une forme stratosphérique avec 10 buts en 6 rencontres, guidant l’armada de Pep Guardiola avant le déplacement à Brentford samedi.',
        'Arsenal (15 pts) et Liverpool (12 pts) attendent le moindre faux pas des Skyblues pour combler l’écart au sommet du classement.',
      ],
    },
    es: {
      title: 'Previa Premier League Jornada 7: Haaland y City buscan el pleno de siete victorias',
      subtitle: 'El conjunto de Guardiola defiende su liderato perfecto en Brentford mientras Arsenal y Liverpool acechan.',
      excerpt: 'Manchester City lidera en solitario con 18 puntos gracias a un Erling Haaland imparable de cara a la séptima jornada liguera.',
      body: [
        'Cumplidas seis fechas de la Premier League 2026-27, el Manchester City domina con autoridad gracias a seis triunfos en seis partidos y 18 puntos.',
        'Erling Haaland encabeza la tabla con 10 goles en 6 jornadas y será la gran amenaza de los citizens en su visita al Brentford este sábado.',
        'Arsenal, segundo con 15 puntos, y Liverpool, tercero con 12, no pueden permitirse tropezar si quieren mantener viva la pugna por el título.',
      ],
    },
    de: {
      title: 'Premier-League-Vorschau Spieltag 7: Haaland und City wollen den siebten Streich in Folge',
      subtitle: 'Guardiolas Elf verteidigt die weiße Weste bei Brentford, während Arsenal und Liverpool auf Ausrutscher lauern.',
      excerpt: 'Manchester City steht nach sechs Runden mit 18 Punkten makellos an der Premier-League-Spitze vor dem siebten Spieltag.',
      body: [
        'Nach sechs Spieltagen der Saison 2026-27 marschiert Manchester City mit der perfekten Ausbeute von 18 Punkten einsam vorneweg.',
        'Erling Haaland dominiert die Torjägerliste mit unglaublichen 10 Treffern in 6 Spielen und führt Pep Guardiolas Team am Samstag nach Brentford.',
        'Arsenal (15 Punkte) und Liverpool (12 Punkte) stehen unter Zugzwang und dürfen sich im Verfolgerfeld keine Schwächen leisten.',
      ],
    },
    it: {
      title: 'Anteprima Premier League 7ª giornata: Haaland e City a caccia del settimo sigillo consecutivo',
      subtitle: 'La squadra di Guardiola difende il primato a punteggio pieno a Brentford con Arsenal e Liverpool all’inseguimento.',
      excerpt: 'Il Manchester City comanda la Premier League a quota 18 punti grazie a uno scatenato Erling Haaland prima della 7ª giornata.',
      body: [
        'Dopo sei giornate di Premier League 2026-27, il Manchester City guida la classifica a punteggio pieno con 6 vittorie su 6 e 18 punti.',
        'Erling Haaland viaggia a medie record con 10 gol in 6 partite e punta a trascinare i campioni anche nella trasferta sul campo del Brentford.',
        'L’Arsenal a quota 15 e il Liverpool a 12 punti cercano continuità per non far scappare la corazzata di Pep Guardiola.',
      ],
    },
    pl: {
      title: 'Zapowiedź 7. kolejki Premier League: Haaland i City idą po siódme z rzędu zwycięstwo',
      subtitle: 'Ekipa Guardioli broni kompletu punktów na wyjeździe z Brentford, a Arsenal i Liverpool gonią lidera.',
      excerpt: 'Manchester City przewodzi tabeli Premier League z kompletem 18 punktów przed 7. kolejką, napędzany bramkami Erlinga Haalanda.',
      body: [
        'Po sześciu seriach gier Premier League 2026-27 Manchester City może pochwalić się perfekcyjnym bilansem sześciu zwycięstw i 18 punktów.',
        'Erling Haaland z 10 golami w 6 występach bije kolejne rekordy strzeleckie przed sobotnim wyjazdem The Citizens na mecz z Brentford.',
        'Arsenal (15 punktów) oraz Liverpool (12 punktów) muszą punktować bezbłędnie, by nie stracić kontaktu z bezwzględnymi mistrzami.',
      ],
    },
    zh: {
      title: '英超第7轮前瞻：哈兰德状态火热，曼城力争开季七连胜',
      subtitle: '瓜迪奥拉率队做客布伦特福德捍卫全胜战绩，阿森纳与利物浦紧追不舍。',
      excerpt: '曼城以6战全胜积18分领跑英超积分榜，哈兰德前6轮斩获10球剑指第七轮连胜。',
      body: [
        '2026-27赛季英超六轮战罢，曼城以无可挑剔的六连胜积18分傲视群雄。',
        '当家射手哈兰德状态如日中天，6场轰入10球，本周六他将率领蓝月亮做客布伦特福德球场争夺开季七连胜。',
        '阿森纳以15分紧随其后，利物浦积12分位列第三，两大追赶者严阵以待期盼缩小分差。',
      ],
    },
    ja: {
      title: 'プレミアリーグ第7節展望：ハーランド爆走のマンチェスター・シティが開幕7連勝へ挑む',
      subtitle: 'ブレントフォード戦で全勝防衛へ、追うアーセナルとリヴァプールも追撃態勢。',
      excerpt: 'マンチェスター・シティが6戦全勝18ポイントで首位独走。ハーランドが10得点で第7節へ。',
      body: [
        '2026-27プレミアリーグは6節を消化し、ペップ・グアルディオラ率いるマンチェスター・シティが勝ち点18で首位を堅持している。',
        'ハーランドは6試合10ゴールと驚異的な決定力を誇り、土曜日のブレントフォード遠征でも主役を務める。',
        '2位アーセナル（15点）と3位リヴァプール（12点）も取りこぼしが許されない緊迫の週末を迎える。',
      ],
    },
    ko: {
      title: '프리미어리그 7라운드 프리뷰: 홀란 앞세운 맨시티, 브렌트퍼드 원정서 개막 7연승 도전',
      subtitle: '과르디올라호 무결점 선두 질주 속 아스널과 리버풀의 거센 추격전 전개.',
      excerpt: '맨체스터 시티가 6전 전승 승점 18점으로 단독 선두를 질주하는 가운데 홀란이 7라운드 득점포 가동을 노린다.',
      body: [
        '2026-27 잉글랜드 프리미어리그에서 맨체스터 시티가 6연승 승점 18점으로 완벽한 선두를 유지하고 있다.',
        '6경기에서 10골을 폭격한 엘링 홀란은 이번 주 토요일 브렌트퍼드 원정에서도 골 폭풍을 예고하고 있다.',
        '아스널(승점 15)과 리버풀(승점 12)은 선두와의 격차를 좁히기 위해 승점 3점 사냥에 나선다.',
      ],
    },
    ar: {
      title: 'تقديم الجولة 7 من الدوري الإنجليزي: هالاند وسيتي يستهدفان الفوز السابع تواليا',
      subtitle: 'كتيبة غوارديولا تدافع عن علامتها الكاملة في برينتفورد بينما يواصل آرسنال وليفربول المطاردة.',
      excerpt: 'يتصدر مانشستر سيتي الترتيب برصيد 18 نقطة من 6 انتصارات متتالية وهالاند يطمح لتعزيز أرقامه القياسية في الجولة السابعة.',
      body: [
        'بعد مرور ست جولات من الدوري الإنجليزي الممتاز 2026-27، ينفرد مانشستر سيتي بالصدارة برصيد 18 نقطة كاملة.',
        'يواصل إرلينغ هالاند تحطيم الأرقام القياسية بتسجيله 10 أهداف في 6 مباريات، ويقود رحلة فريقه إلى برينتفورد يوم السبت.',
        'ويحتل آرسنال المركز الثاني برصيد 15 نقطة متقدما على ليفربول (12 نقطة)، منتظرين أي تعثر لحامل اللقب.',
      ],
    },
  },
  'china-open-beijing-atp-wta-preview-2026': {
    fr: {
      title: 'China Open Pékin 2026 : Sinner et Alcaraz débarquent en Asie au lancement du tableau principal',
      subtitle: 'Le n°1 mondial Sinner remet son titre en jeu tandis que Rybakina et Sabalenka mènent un tableau WTA 1000 royal au Diamond Court.',
      excerpt: 'Le circuit mondial pose ses valises à Pékin pour le China Open 2026 au National Tennis Center.',
      body: [
        'Après le sacre de l’Europe en Laver Cup à Londres, l’élite mondiale du tennis se retrouve à Pékin pour le China Open 2026.',
        'Jannik Sinner, n°1 mondial et tenant du titre, mène le tableau ATP 500 aux côtés de Carlos Alcaraz, Daniil Medvedev et Alexander Zverev.',
        'Sur le Diamond Court, le tableau WTA 1000 promet des étincelles avec Elena Rybakina, sacrée à l’US Open, et Aryna Sabalenka.',
      ],
    },
    es: {
      title: 'Abierto de China Pekín 2026: Sinner y Alcaraz aterrizan en Asia al arrancar el cuadro principal',
      subtitle: 'El número 1 Sinner defiende corona mientras Rybakina y Sabalenka encabezan un cartel estelar de WTA 1000 en Diamond Court.',
      excerpt: 'El tenis mundial se traslada a Pekín con el inicio del Abierto de China 2026 en el Centro Nacional de Tenis.',
      body: [
        'Apenas concluida la Laver Cup en Londres, las grandes figuras del tenis mundial ya compiten en Pekín en el Abierto de China 2026.',
        'Jannik Sinner defiende su cetro ATP 500 frente a Carlos Alcaraz, Daniil Medvedev y Alexander Zverev en la capital china.',
        'En el cuadro femenino WTA 1000, Elena Rybakina, campeona del US Open, y Aryna Sabalenka lideran un torneo de máxima categoría.',
      ],
    },
    de: {
      title: 'China Open Peking 2026: Sinner und Alcaraz schlagen in Asien zum Hauptfeldstart auf',
      subtitle: 'Weltranglistenerster Sinner verteidigt seinen Titel, während Rybakina und Sabalenka das WTA-1000-Feld am Diamond Court anführen.',
      excerpt: 'Die Tennis-Weltspitze zieht nach Peking: Im National Tennis Center beginnt das Hauptfeld der China Open 2026.',
      body: [
        'Unmittelbar nach dem Laver-Cup-Sieg von Team Europe in London reist die Tennis-Elite zu den China Open nach Peking.',
        'Jannik Sinner führt das ATP-500-Feld als Titelverteidiger und Weltranglistenerster zusammen mit Carlos Alcaraz und Alexander Zverev an.',
        'Auf dem Diamond Court glänzt das WTA-1000-Turnier mit US-Open-Siegerin Elena Rybakina, Aryna Sabalenka und Lokalmatadorin Zheng Qinwen.',
      ],
    },
    it: {
      title: 'China Open Pechino 2026: Sinner e Alcaraz in Asia per il via al tabellone principale',
      subtitle: 'Il numero 1 Sinner difende il titolo mentre Rybakina e Sabalenka guidano il WTA 1000 sul Diamond Court.',
      excerpt: 'Il grande tennis sbarca a Pechino per il China Open 2026 sui campi del National Tennis Center.',
      body: [
        'A poche ore dalla vittoria europea in Laver Cup, i big della racchetta sono atterrati a Pechino per il China Open 2026.',
        'Jannik Sinner, numero 1 del mondo e campione uscente, guida il seeding ATP 500 tallonato da Carlos Alcaraz e Daniil Medvedev.',
        'Nel torneo WTA 1000 occhi puntati sulla neo campionessa degli US Open Elena Rybakina, su Aryna Sabalenka e sull’eroina di casa Zheng Qinwen.',
      ],
    },
    pl: {
      title: 'China Open Pekin 2026: Sinner i Alcaraz meldują się w Azji na starcie turnieju głównego',
      subtitle: 'Lider rankingu Sinner broni tytułu, a Rybakina i Sabalenka przewodzą stawce WTA 1000 na korcie Diamond Court.',
      excerpt: 'Tenisowa elita przenosi się do stolicy Chin na turniej China Open 2026 w National Tennis Center.',
      body: [
        'Tuż po emocjach Laver Cup w Londynie najlepsi tenisiści świata rozpoczynają rywalizację w turnieju China Open w Pekinie.',
        'Jannik Sinner przystępuje do obrony tytułu ATP 500 w towarzystwie Carlosa Alcaraza, Daniiła Miedwiediewa i Alexandra Zvereva.',
        'W kobiecym turnieju WTA 1000 zagrają m.in. mistrzyni US Open Elena Rybakina, Aryna Sabalenka oraz reprezentantka gospodarzy Zheng Qinwen.',
      ],
    },
    zh: {
      title: '2026中国网球公开赛：辛纳阿尔卡拉斯齐聚北京，正赛全面打响',
      subtitle: '世界第一辛纳开启卫冕征程，莱巴金娜与萨巴伦卡领衔钻石球场WTA 1000阵容。',
      excerpt: '网坛巨星转战国家网球中心，2026中国网球公开赛正赛正式开打，男女单打看点十足。',
      body: [
        '拉沃尔杯伦敦决战刚刚落幕，世界网坛群雄便已飞抵北京国家网球中心，出战2026中网公开赛。',
        '男单世界第一兼卫冕冠军辛纳与阿尔卡拉斯、梅德韦杰夫领衔ATP 500豪华阵容，全力角逐年终积分。',
        '女单WTA 1000赛场同样众星云集，美网新科冠军莱巴金娜、萨巴伦卡以及东道主名将郑钦文将引爆钻石球场。',
      ],
    },
    ja: {
      title: 'チャイナ・オープン北京2026：シナーとアルカラスがアジアへ到着、本戦開幕',
      subtitle: '世界1位シナーが連覇に挑み、リバキナとサバレンカがダイヤモンド・コートのWTA1000を牽引。',
      excerpt: 'テニス界のスターが北京の国家テニスセンターに集結。2026チャイナ・オープンの本戦がスタート。',
      body: [
        'ロンドンでのレーバーカップ熱戦直後、トッププロたちは北京へ移動しチャイナ・オープン2026に臨む。',
        '世界ランキング1位のシナーがタイトル防衛を目指し、アルカラスやメドベージェフとともにATP500を争う。',
        '女子WTA1000では全米女王リバキナ、サバレンカ、そして地元中国の鄭欽文がセンターコートを熱狂させる。',
      ],
    },
    ko: {
      title: '2026 차이나 오픈 베이징: 신네르와 알카라스 아시아 입성, 본선 개막',
      subtitle: '세계 1위 신네르의 타이틀 방어전, 리바키나와 사발렌카가 다이아몬드 코트 WTA 1000 수놓는다.',
      excerpt: '베이징 국가 테니스 센터에서 2026 차이나 오픈 본선이 시작되며 세계 톱스타들이 격돌한다.',
      body: [
        '런던 레이버컵 종료 직후 세계 테니스 거성들이 베이징 국가 테니스 센터로 집결해 차이나 오픈 본선에 나선다.',
        '세계 1위 얀니크 신네르가 디펜딩 챔피언으로 출격하며, 카를로스 알카라스와 메드베데프가 ATP 500 우승을 다툰다.',
        'WTA 1000 무대에서는 US오픈 챔피언 리바키나와 사발렌카, 정친원이 다이아몬드 코트에서 화려한 대결을 펼친다.',
      ],
    },
    ar: {
      title: 'بطولة الصين المفتوحة ببكين 2026: سينر وألكاراز يصلان إلى آسيا مع انطلاق الجدول الرئيسي',
      subtitle: 'المصنف الأول سينر يدافع عن لقبه وريباكينا وسابالينكا تقودان منافسات السيدات على ملعب دايموند كورت.',
      excerpt: 'تتجه أنظار عشاق التنس إلى العاصمة الصينية بكين مع انطلاق مباريات بطولة الصين المفتوحة 2026 في المركز الوطني للتنس.',
      body: [
        'عقب تتويج أوروبا بكأس لافر في لندن، انتقل نجوم التنس العالمي مباشرة إلى بكين للمشاركة في بطولة الصين المفتوحة 2026.',
        'يدخل الإيطالي يانيك سينر، المصنف الأول عالميا وحامل اللقب، المنافسات جنبا إلى جنب مع كارلوس ألكاراز ودانييل ميدفيديف.',
        'وفي منافسات السيدات لفئة 1000 نقطة، تقود بطلة أمريكا المفتوحة إيلينا ريباكينا وأرينا سابالينكا والبطلة الصينية تشنغ تشينوين قائمة النجمات.',
      ],
    },
  },
  'singapore-gp-night-race-physical-crucible-2026': {
    fr: {
      title: 'Présentation GP de Singapour : la fournaise nocturne de Marina Bay attend Antonelli et Russell',
      subtitle: 'Humidité tropicale, 19 virages et 1 600 projecteurs mettent les leaders du championnat Mercedes au défi le plus rude.',
      excerpt: 'La Formule 1 se prépare pour le défi nocturne de Singapour où Kimi Antonelli défend ses 88 points d’avance au championnat.',
      body: [
        'La Formule 1 pose ses quartiers à Marina Bay pour le Grand Prix de Singapour, l’épreuve physique la plus impitoyable de l’année sous les projecteurs.',
        'Fort de son succès autoritaire à Bakou, le rookie de Mercedes Kimi Antonelli mène le championnat du monde avec 317 points, 88 de plus que George Russell (229 pts).',
        'Ferrari avec Hamilton et Leclerc ainsi que McLaren avec Norris préparent des évolutions aéro pour bousculer les Flèches d’Argent dans les rues sinueuses de la cité-État.',
      ],
    },
    es: {
      title: 'Previa GP de Singapur: el infierno nocturno de Marina Bay espera a Antonelli y Russell',
      subtitle: 'Humedad tropical, 19 curvas y 1.600 focos ponen a prueba a Mercedes en la carrera más exigente de la F1.',
      excerpt: 'La Fórmula 1 aterriza en Marina Bay para el GP de Singapur con Kimi Antonelli defendiendo 88 puntos de renta en el Mundial.',
      body: [
        'El Mundial de F1 encara su examen físico más severo en el circuito urbano de Marina Bay para el Gran Premio de Singapur bajo los reflectores.',
        'Tras su exhibición desde la pole en Bakú, el joven prodigio de Mercedes Kimi Antonelli lidera el certamen con 317 puntos, superando por 88 a George Russell (229 pts).',
        'Ferrari, con Hamilton y Leclerc, y McLaren, con Norris, esperan aprovechar el trazado lento y bacheado para recortar distancias con las flechas de plata.',
      ],
    },
    de: {
      title: 'Vorschau GP von Singapur: Der Flutlicht-Hexenkessel von Marina Bay wartet auf Antonelli und Russell',
      subtitle: 'Tropische Hitze, 19 Kurven und 1.600 Flutlichtstrahler fordern Mercedes im härtesten Ausdauerrennen der Formel 1.',
      excerpt: 'Die Formel 1 rüstet sich für das Nachtrennen in Singapur: Kimi Antonelli verteidigt 88 Punkte Vorsprung in der WM.',
      body: [
        'Die Formel 1 zieht weiter zum spektakulären Marina Bay Street Circuit, wo das Nachtrennen von Singapur den Fahrern alles abverlangt.',
        'Nach seinem dominanten Sieg in Baku führt Mercedes-Shootingstar Kimi Antonelli die Weltmeisterschaft mit 317 Punkten und 88 Zählern Vorsprung vor George Russell an.',
        'Ferrari mit Hamilton und Leclerc sowie McLaren mit Norris bringen Downforce-Upgrades mit, um Mercedes auf dem winkeligen Stadtkurs zu attackieren.',
      ],
    },
    it: {
      title: 'Anteprima GP Singapore: la fornace notturna di Marina Bay attende Antonelli e Russell',
      subtitle: 'Umidità tropicale, 19 curve e 1.600 riflettori mettono alla prova i leader Mercedes nella gara più dura del mondiale.',
      excerpt: 'La Formula 1 si prepara alla notte di Marina Bay per il Gran Premio di Singapore, con Antonelli leader a quota 317 punti.',
      body: [
        'La Formula 1 affronta la sfida più probante dell’anno tra le strade di Marina Bay per il Gran Premio di Singapore in notturna.',
        'Kimi Antonelli si presenta al via forte della vittoria di Baku e comanda la classifica iridata con 317 punti, a +88 sul compagno George Russell (229).',
        'Ferrari e McLaren affilano le armi: Hamilton, Leclerc e Norris cercano il riscatto sulle stradine asiatiche dove la safety car è sempre protagonista.',
      ],
    },
    pl: {
      title: 'Zapowiedź GP Singapuru: nocny kocioł Marina Bay czeka na Antonellego i Russella',
      subtitle: 'Tropikalna wilgoć, 19 zakrętów i 1600 jupiterów przetestują liderów Mercedesa w najtrudniejszym wyścigu sezonu.',
      excerpt: 'Formuła 1 zjeżdża do Singapuru na nocny wyścig uliczny, w którym Kimi Antonelli broni 88 punktów przewagi w mistrzostwach.',
      body: [
        'Formuła 1 przenosi się na tor Marina Bay Street Circuit, by rozegrać najbardziej wymagające fizycznie Grand Prix Singapuru pod jupiterami.',
        'Po triumfie w Baku Kimi Antonelli przewodzi klasyfikacji kierowców z dorobkiem 317 punktów, wyprzedzając George’a Russella o 88 oczek.',
        'Ferrari z Hamiltonem i Leclercem oraz McLaren z Norrisem liczą na krętą specyfikę toru, by rzucić wyzwanie dominującym Srebrnym Strzałom.',
      ],
    },
    zh: {
      title: '新加坡大奖赛前瞻：滨海湾夜战熔炉静候安东内利与拉塞尔',
      subtitle: '热带高温潮湿、19个弯角与1600盏泛光灯考验梅赛德斯双雄，迎来F1最严酷体能决战。',
      excerpt: 'F1转战滨海湾街道赛道展开新加坡大奖赛夜战，领跑积分榜的安东内利手握88分巨大优势出征。',
      body: [
        'F1赛程迎来全年体能考验最严酷的一站：在新加坡滨海湾街道赛道的人工照明下展开夜间街道赛决战。',
        '巴库站杆位夺冠的梅赛德斯超级新星安东内利目前以317分领跑车手榜，领先队友拉塞尔多达88分。',
        '法拉利车队的汉密尔顿与勒克莱尔以及迈凯伦的诺里斯均携升级套件登场，力求在低速多弯赛道中阻击银箭王朝。',
      ],
    },
    ja: {
      title: 'シンガポールGP展望：マリーナベイ熱帯夜の試練がアントネッリとラッセルを待ち受ける',
      subtitle: '過酷な湿気、19のコーナー、1,600基の照明がF1最難関の市街地コースでメルセデス首位を試す。',
      excerpt: 'マリーナベイ市街地サーキットでシンガポールGPが迫る。アントネッリが88点リードでナイターレースへ。',
      body: [
        'F1サーカスは年間屈指の過酷なサバイバル戦となるシンガポールGPのマリーナベイ市街地コースへ舞台を移す。',
        'バクーで完勝を飾ったメルセデスの新星キミ・アントネッリは317ポイントを稼ぎ出し、同僚ラッセルに88点差をつけて首位を独走中。',
        'フェラーリのハミルトン、ルクレール、マクラーレンのノリスも高ダウンフォース仕様でメルセデス包囲網を敷く。',
      ],
    },
    ko: {
      title: '싱가포르 GP 프리뷰: 마리나 베이의 열대 야간 서킷, 안토넬리와 러셀 기다린다',
      subtitle: '열대성 습도, 19개 코너, 1,600개 조명 아래 메르세데스 챔피언십 듀오의 한계 시험대.',
      excerpt: '포뮬러 1이 마리나 베이 시가지 서킷으로 이동해 싱가포르 GP 야간 레이스를 펼친다. 안토넬리가 88점 차 선두를 달린다.',
      body: [
        'F1 서커스가 드라이버들에게 가장 가혹한 체력적 시련을 안겨주는 싱가포르 GP 마리나 베이 서킷에 도착했다.',
        '바쿠 폴투윈 승리로 기세를 올린 메르세데스의 루키 키미 안토넬리는 317점으로 조지 러셀(229점)에 88점 앞서 있다.',
        '페라리의 해밀턴, 르클레르와 맥라렌의 노리스는 저속 코너가 즐비한 시가지 트랙에서 역전을 노린다.',
      ],
    },
    ar: {
      title: 'تقديم جائزة سنغافورة الكبرى: أتون مارينا باي الليلي ينتظر أنتونيللي وراسل',
      subtitle: 'حرارة ورطوبة خانقة و19 منعطفا و1600 كشاف إضاءة تختبر متصدري مرسيدس في السباق الأصعب.',
      excerpt: 'تستعد حلبة مارينا باي لاستضافة سباق جائزة سنغافورة الكبرى الليلي حيث يدافع كيمي أنتونيللي عن صدارته بفارق 88 نقطة.',
      body: [
        'تتأهب بطولة فورمولا 1 للاختبار البدني الأقسى على حلبة مارينا باي لشوارع سنغافورة في سباق ليلي بالغ الإثارة.',
        'يدخل الإيطالي الصاعد كيمي أنتونيللي السباق متصدرا للترتيب برصيد 317 نقطة متقدما بفارق 88 نقطة على زميله جورج راسل.',
        'في المقابل يتسلح ثنائي فيراري هاميلتون ولوكلير ونوريس سائق ماكلارين بحزم انسيابية جديدة لتحدي مرسيدس في المنعطفات الضيقة.',
      ],
    },
  },
  'pga-tour-fall-sanderson-farms-preview-2026': {
    fr: {
      title: 'Début du swing d’automne PGA Tour : le Sanderson Farms Championship s’ouvre à Jackson',
      subtitle: 'Après le sacre américain en Presidents Cup, les joueurs luttent pour leur carte 2027 et de précieux points FedExCup dans le Mississippi.',
      excerpt: 'Le PGA Tour pose ses sacs à Jackson pour le Sanderson Farms Championship, première étape décisive du FedExCup Fall.',
      body: [
        'La fête américaine de la Presidents Cup tout juste achevée à Medinah, le golf professionnel retrouve la dure réalité du FedExCup Fall à Jackson.',
        'Le Sanderson Farms Championship au Country Club of Jackson offre 500 points et deux ans d’exemption sur le PGA Tour pour le vainqueur.',
        'Pour les joueurs classés au-delà de la 50e place, chaque coup compte afin d’intégrer le top 125 qualificatif pour la saison 2027.',
      ],
    },
    es: {
      title: 'Comienza el tramo de otoño del PGA Tour: el Sanderson Farms Championship lleva máxima tensión a Jackson',
      subtitle: 'Tras la conquista estadounidense en la Presidents Cup, los golfistas pelean en Misisipi por la tarjeta de 2027 y puntos de la FedExCup.',
      excerpt: 'El PGA Tour llega a Jackson para el Sanderson Farms Championship con la permanencia en el circuito y exenciones en juego.',
      body: [
        'Apenas apagados los festejos de Estados Unidos en Medinah por la Presidents Cup, el golf profesional se traslada a Jackson para el inicio del FedExCup Fall.',
        'El Country Club de Jackson acoge una cita clave dotada con 500 puntos de la FedExCup y dos años de exención en el PGA Tour para el ganador.',
        'Para los profesionales situados en la frontera del puesto 125, cada birdie en Misisipi puede definir su futuro deportivo para 2027.',
      ],
    },
    de: {
      title: 'PGA Tour Fall Swing startet: Sanderson Farms Championship verspricht Hochspannung in Jackson',
      subtitle: 'Nach dem US-Triumph beim Presidents Cup kämpfen die Profis in Mississippi um Tourkarten für 2027 und FedExCup-Punkte.',
      excerpt: 'Die PGA Tour schlägt in Jackson auf: Bei der Sanderson Farms Championship geht es um die Tourkarte für 2027.',
      body: [
        'Kaum sind die Jubelgesänge nach dem 18,5:11,5-Sieg der USA beim Presidents Cup verklungen, beginnt der knallharte FedExCup Fall in Mississippi.',
        'Die Sanderson Farms Championship im Country Club of Jackson bietet 500 Punkte und eine zweijährige Tour-Exemption für den Sieger.',
        'Für Profis um Rang 125 steht die sportliche Existenz auf dem Spiel, um sich das Spielrecht für die PGA-Tour-Saison 2027 zu sichern.',
      ],
    },
    it: {
      title: 'Al via il PGA Tour Fall: il Sanderson Farms Championship porta alta tensione a Jackson',
      subtitle: 'Dopo il trionfo USA in Presidents Cup, i pro lottano in Mississippi per la carta 2027 e i punti della FedExCup.',
      excerpt: 'Il PGA Tour fa tappa a Jackson per il Sanderson Farms Championship, snodo cruciale per la sopravvivenza sul circuito.',
      body: [
        'Chiusa la trionfale Presidents Cup di Medinah vinta dagli Stati Uniti, il golf professionistico si concentra sulla serrata lotta del FedExCup Fall.',
        'Il Sanderson Farms Championship al Country Club di Jackson mette in palio 500 punti e un’esenzione biennale sul PGA Tour per il vincitore.',
        'Per i giocatori attorno alla 125ª posizione della classifica ogni colpo in Mississippi può valere il futuro nella stagione 2027.',
      ],
    },
    pl: {
      title: 'Jesienny cykl PGA Tour wystartował: Sanderson Farms Championship przynosi wielkie emocje w Jackson',
      subtitle: 'Po triumfie USA w Presidents Cup golfiści walczą w Mississippi o punkty FedExCup i karty na sezon 2027.',
      excerpt: 'PGA Tour przenosi się do Jackson na Sanderson Farms Championship, gdzie toczy się bezwzględna walka o utrzymanie w elicie.',
      body: [
        'Po emocjach Presidents Cup w Medinah i zwycięstwie USA zawodowy golf przechodzi do jesiennej fazy FedExCup Fall w Mississippi.',
        'Turniej Sanderson Farms Championship w Country Club of Jackson oferuje zwycięzcy 500 punktów i dwuletnie zwolnienie w cyklu PGA Tour.',
        'Dla graczy z okolic 125. miejsca rankingu każdy dołek w Jackson ma kolosalne znaczenie dla zachowania pełnych praw gry w 2027 roku.',
      ],
    },
    zh: {
      title: '美巡赛秋季赛启幕：桑德森农场锦标赛在杰克逊上演保卡生死战',
      subtitle: '美国队捧得总统杯后巡回赛转战密西西比，众球手为2027赛季全卡与联邦快递杯积分搏杀。',
      excerpt: '美巡赛转战密西西比州杰克逊乡村俱乐部，桑德森农场锦标赛拉开秋季保卡争夺战序幕。',
      body: [
        '总统杯美国队在麦迪纳夺冠的硝烟散去，美巡赛随即进入残酷的秋季积分赛阶段。',
        '在杰克逊乡村俱乐部举行的桑德森农场锦标赛不仅提供500个联邦快递杯积分，冠军还将直接获得两年美巡赛豁免资格。',
        '对于徘徊在第125位前后的边缘选手而言，密西西比的每一杆都直接决定着2027赛季能否保住全卡席位。',
      ],
    },
    ja: {
      title: 'PGAツアー秋季シリーズ開幕：サンダーソン・ファームズ選手権がジャクソンで緊迫の決戦へ',
      subtitle: 'プレジデンツカップ米国優勝の余韻冷めやらぬ中、ミシシッピで2027年シード権とポイントを懸けた戦いが始まる。',
      excerpt: 'カントリー・クラブ・オブ・ジャクソンでサンダーソン・ファームズ選手権が開幕。シード権争奪戦が激化。',
      body: [
        'メディナでのプレジデンツカップ米国勝利の熱気冷めやらぬ中、PGAツアーはフェデックスカップ・フォールへと舞台を移す。',
        'カントリー・クラブ・オブ・ジャクソンで開催されるサンダーソン・ファームズ選手権は、優勝者に500ポイントと2年シードが授与される。',
        '125位前後のボーダーラインに立つ選手たちにとって、ミシシッピでの4日間は2027年の出場権を懸けた死活問題となる。',
      ],
    },
    ko: {
      title: 'PGA 투어 가을 시리즈 개막: 샌더슨 팜스 챔피언십, 잭슨에서 시드권 혈투 예고',
      subtitle: '미국팀 프레지던츠컵 승리 후 미시시피에서 2027 시즌 투어 카드와 페덱스컵 포인트를 향한 생존경쟁 돌입.',
      excerpt: 'PGA 투어가 잭슨 컨트리 클럽으로 이동해 샌더슨 팜스 챔피언십을 개최하며 가을 시드권 경쟁의 막을 올린다.',
      body: [
        '메디나에서 끝난 프레지던츠컵 미국팀 우승의 여운이 가시기도 전에 PGA 투어는 미시시피 잭슨에서 페덱스컵 가을 시리즈에 돌입한다.',
        '잭슨 컨트리 클럽에서 열리는 샌더슨 팜스 챔피언십 우승자에게는 페덱스컵 500점과 2년간의 PGA 투어 풀시드가 주어진다.',
        '125위권 안팎의 위태로운 선수들에게 이번 대회는 2027 시즌 생존을 결정짓는 절대적인 무대가 될 전망이다.',
      ],
    },
    ar: {
      title: 'انطلاق الجولة الخريفية لجولة بي جيه إيه: بطولة ساندرسون فارمز تفتتح الإثارة في جاكسون',
      subtitle: 'عقب تتويج أمريكا بكأس الرؤساء يتنافس نجوم الغولف في مسيسيبي لضمان بطاقة 2027 ونقاط فيديكس كاب.',
      excerpt: 'تنتقل جولة بي جيه إيه إلى ولاية مسيسيبي لخوض منافسات بطولة ساندرسون فارمز لحسم بطاقات التأهل لعام 2027.',
      body: [
        'بعد أيام قليلة من فوز الفريق الأمريكي بكأس الرؤساء في ميدينا، يتجه التركيز إلى منافسات خريف فيديكس كاب الحاسمة في جاكسون.',
        'تمنح بطولة ساندرسون فارمز في كانتري كلوب أوف جاكسون 500 نقطة وبطاقة مشاركة لمدة عامين للبطل المتوج.',
        'وتعد البطولة فرصة مصيرية للاعبين القابعين حول المركز 125 لضمان بطاقات المشاركة الكاملة لموسم 2027.',
      ],
    },
  },
  'wnba-playoffs-fever-lynx-sweep-semifinals-2026': {
    fr: {
      title: 'Playoffs WNBA : Caitlin Clark qualifie le Fever face au Dream, les Lynx éliminent les Mystics',
      subtitle: 'Indiana et Minnesota sont les premières équipes qualifiées pour les demi-finales 2026 grâce à des victoires décisives au match 2.',
      excerpt: 'Caitlin Clark compile 24 points et 11 passes pour le sweep d’Indiana 2-0 à Atlanta, tandis que Napheesa Collier guide Minnesota vers les demi-finales.',
      body: [
        'Le premier tour des playoffs WNBA 2026 a livré son verdict mardi soir, les deux favoris refusant de disputer un troisième match décisif. À Atlanta comme à Minneapolis, le sang-froid des leaders a fait la différence.',
        'Au Gateway Center Arena, Caitlin Clark a signé un nouveau récital avec 24 points, 11 passes décisives et 7 rebonds pour permettre au Fever d’écarter le Dream 87-81. Kelsey Mitchell a ajouté 22 points, dont deux tirs primés cruciaux en fin de rencontre, propulsant Indiana dans le dernier carré pour la première fois depuis 2015.',
        'Dans le même temps, les Minnesota Lynx n’ont laissé aucun espoir aux Washington Mystics. Napheesa Collier a régné dans la raquette avec 26 points et 9 rebonds pour une victoire nette 85-73. Indiana et Minnesota s’imposent 2-0 et s’offrent un précieux repos avant les demi-finales.',
      ],
    },
    es: {
      title: 'Playoffs WNBA: Caitlin Clark lidera la barrida del Fever ante Dream; Lynx eliminan a Mystics',
      subtitle: 'Indiana y Minnesota se convierten en los primeros semifinalistas de 2026 tras ganar el Juego 2 como visitantes.',
      excerpt: 'Caitlin Clark suma 24 puntos y 11 asistencias en el 2-0 de Indiana sobre Atlanta, mientras Napheesa Collier guía a Minnesota a semifinales.',
      body: [
        'La noche del martes definió la primera ronda de los playoffs de la WNBA 2026, con los dos favoritos cerrando sus series sin necesidad de un tercer partido de desempate.',
        'En Atlanta, Caitlin Clark deslumbró con 24 puntos, 11 asistencias y 7 rebotes para liderar al Indiana Fever a un triunfo 87-81 sobre el Dream. Kelsey Mitchell aportó 22 puntos con triples decisivos en el tramo final, clasificando a Indiana a semifinales por primera vez desde 2015.',
        'En Minneapolis, Minnesota Lynx superó con claridad a Washington Mystics por 85-73 gracias a los 26 puntos y 9 rebotes de Napheesa Collier. Tanto Fever como Lynx sentencian sus eliminatorias por 2-0 y esperan rivales para el campeonato.',
      ],
    },
    de: {
      title: 'WNBA-Playoffs: Caitlin Clark führt Fever zum Sweep gegen Dream; Lynx werfen Mystics raus',
      subtitle: 'Indiana und Minnesota ziehen mit überzeugenden Auswärtssiegen in Spiel 2 als erste Teams ins Halbfinale 2026 ein.',
      excerpt: 'Caitlin Clark glänzt mit 24 Punkten und 11 Assists beim 2:0-Sweep über Atlanta, während Collier Minnesota ins Halbfinale führt.',
      body: [
        'Der Dienstagabend brachte die ersten Vorentscheidungen in den WNBA-Playoffs 2026. Beide Favoriten machten kurzen Prozess und vermieden ein entscheidendes drittes Spiel.',
        'In Atlanta dominierte Caitlin Clark mit 24 Punkten, 11 Assists und 7 Rebounds beim 87:81-Erfolg der Indiana Fever über die Dream. Kelsey Mitchell steuerte 22 Zähler bei und sicherte Indiana die erste Halbfinal-Teilnahme seit 2015.',
        'Im Target Center ließen die Minnesota Lynx den Washington Mystics beim 85:73 keine Chance. Napheesa Collier führte ihr Team mit 26 Punkten und 9 Rebounds an. Sowohl Fever als auch Lynx stehen mit 2:0-Sweeps souverän in der Vorschlussrunde.',
      ],
    },
    it: {
      title: 'Playoff WNBA: Caitlin Clark trascina le Fever al passaggio del turno; Lynx battono le Mystics',
      subtitle: 'Indiana e Minnesota conquistano la qualificazione alle semifinali 2026 chiudendo la serie sul 2-0 in Gara 2.',
      excerpt: 'Caitlin Clark firma 24 punti e 11 assist nel successo delle Fever ad Atlanta, mentre Napheesa Collier spedisce Minnesota in semifinale.',
      body: [
        'La notte di martedì ha regalato i primi verdetti dei playoff WNBA 2026, con le due teste di serie che hanno chiuso i conti senza ricorrere alla bella.',
        'Alla Gateway Center Arena Caitlin Clark ha dato spettacolo con 24 punti, 11 assist e 7 rimbalzi guidando le Indiana Fever alla vittoria per 87-81 sulle Dream. I 22 punti di Kelsey Mitchell hanno sigillato il ritorno di Indiana in semifinale dopo undici anni.',
        'A Minneapolis le Minnesota Lynx hanno dominato le Washington Mystics per 85-73 trascinate dai 26 punti di Napheesa Collier. Entrambe le formazioni archiviano la pratica sul 2-0 e attendono le prossime sfide.',
      ],
    },
    pl: {
      title: 'Play-off WNBA: Caitlin Clark prowadzi Fever do awansu; Lynx eliminują Mystics',
      subtitle: 'Indiana i Minnesota jako pierwsze meldują się w półfinałach 2026 po pewnych triumfach w meczach numer dwa.',
      excerpt: 'Caitlin Clark notuje 24 punkty i 11 asyst w wygranej Indiany z Atlantą 2-0, a Napheesa Collier pieczętuje awans Minnesoty.',
      body: [
        'Wtorkowa noc przyniosła decydujące rozstrzygnięcia w pierwszej rundzie play-off WNBA 2026, a faworyci nie pozwolili rywalkom na doprowadzenie do decydującego meczu.',
        'W Atlancie Caitlin Clark popisała się 24 punktami, 11 asystami i 7 zbiórkami, prowadząc Indiana Fever do zwycięstwa 87-81 nad Dream. 22 punkty Kelsey Mitchell dały Indianie pierwszy awans do półfinału od 2015 roku.',
        'W Minneapolis Minnesota Lynx pewnie pokonała Washington Mystics 85-73. Napheesa Collier rzuciła 26 punktów i zebrała 9 piłek, zapewniając swojej drużynie czyste zwycięstwo w serii 2-0.',
      ],
    },
    zh: {
      title: 'WNBA季后赛：克拉克狂轰24分11助攻横扫梦想，山猫力克神秘人挺进半决赛',
      subtitle: '狂热与山猫在第2场客场决战中展现统治力，成为首批晋级2026年WNBA半决赛的球队。',
      excerpt: '凯特琳·克拉克砍下24分11次助攻率狂热2-0横扫亚特兰大，科利尔砍下26分率山猫淘汰神秘人。',
      body: [
        '周二晚间的WNBA季后赛首轮迎来定局时刻，两支强队均拒绝将系列赛拖入生死第3场，以两连胜强势闯关。',
        '在亚特兰大网关中心球馆，超级新星凯特琳·克拉克再度奉献大师级表演，全场贡献24分、11次助攻和7个篮板，率领印第安纳狂热以87-81力克梦想。米切尔飙中22分并在最后两分钟连中两记关键三分，帮助狂热自2015年以来首度重返半决赛。',
        '在明尼阿波利斯标靶中心，常规赛头名山猫以85-73完胜华盛顿神秘人。内皮莎·科利尔砍下26分9个篮板统治内线。狂热与山猫均以2-0横扫晋级，赢得宝贵的半决赛休整期。',
      ],
    },
    ja: {
      title: 'WNBAプレーオフ：クラークが24得点11アシストでドリームをスイープ、リンクスも準決勝進出',
      subtitle: 'インディアナとミネソタが敵地での第2戦を制し、2026年WNBAベスト4一番乗りを決める。',
      excerpt: 'ケイトリン・クラークが24得点11アシストでフィーバーを2-0スイープへ導き、コリアー率いるリンクスもミスティクスを撃破。',
      body: [
        '火曜日のWNBAプレーオフ1回戦第2戦は、アウェーの強豪2チームが勝負強さを発揮し、第3戦を待たずにシリーズ突破を決めました。',
        'アトランタではケイトリン・クラークが24得点、11アシスト、7リバウンドを記録し、インディアナ・フィーバーが87-81でドリームを撃破。ケルシー・ミッチェルも勝負所で22得点を挙げ、フィーバーは2015年以来となるセミファイナル進出を果たしました。',
        'ミネアポリスでは第1シードのリンクスがナフィーサ・コリアーの26得点9リバウンドの活躍でミスティクスを85-73で退けました。インディアナとミネソタの両チームが2連勝で4強入りを決定づけました。',
      ],
    },
    ko: {
      title: 'WNBA 플레이오프: 케이틀린 클라크 24득점 11어시스트 스윕, 링스도 미스틱스 꺾고 4강 진출',
      subtitle: '인디애나 피버와 미네소타 링스가 2차전 원정 승리로 2026 시즌 4강 티켓을 가장 먼저 확보했다.',
      excerpt: '클라크가 24득점 11어시스트로 드림을 2-0 완파하며 인디애나를 2015년 이후 첫 준결승으로 이끌었다.',
      body: [
        '화요일 밤 열린 WNBA 플레이오프 1라운드 2차전에서 강호들이 흔들림 없는 집중력으로 3차전 없이 시리즈를 조기 매듭지었다.',
        '애틀랜타에서 케이틀린 클라크는 24득점 11어시스트 7리바운드를 기록하며 인디애나 피버의 87-81 승리를 이끌었다. 켈시 미첼이 4쿼터 결정적인 3점포 포함 22점을 보태며 피버는 11년 만에 4강 무대를 밟았다.',
        '미네소타 링스 역시 나피사 콜리어가 26득점 9리바운드로 골밑을 장악하며 워싱턴 미스틱스를 85-73으로 제압했다. 두 팀 모두 2-0 깔끔한 스윕으로 다음 라운드에 안착했다.',
      ],
    },
    ar: {
      title: 'أدوار الحسم في دوري السلة النسائي: كلارك تقود فيفر لسحق دريم ولينكس تطيح بميستيكس',
      subtitle: 'إنديانا ومينيسوتا أول المتأهلين إلى نصف نهائي 2026 بعد حسم المواجهة الثانية خارج الديار.',
      excerpt: 'سجلت كيتلين كلارك 24 نقطة و11 تمريرة حاسمة لتقود إنديانا لفوز ساحق 2-0 على أتلانتا والعبور لنصف النهائي.',
      body: [
        'شهدت مباريات الثلاثاء حسم الجولة الأولى من أدوار خروج المغلوب في دوري السلة الأمريكي للسيدات دون الحاجة لمباراة فاصلة.',
        'في أتلانتا، واصلت النجمة كيتلين كلارك تألقها اللافت مسجلة 24 نقطة و11 تمريرة حاسمة لتقود إنديانا فيفر للفوز 87-81 على أتلانتا دريم وبلوغ نصف النهائي للمرة الأولى منذ 2015.',
        'وفي مينيابوليس، قادت نافيسا كوليير مينيسوتا لينكس للفوز 85-73 على واشنطن بتسجيلها 26 نقطة، ليحسم الفريقان بطاقتي التأهل بنتيجة 2-0.',
      ],
    },
  },
  'nfl-week4-tnf-preview-49ers-rams-2026': {
    fr: {
      title: 'Aperçu NFL Semaine 4 : les 49ers et les Rams relancent leur rivalité lors du Thursday Night Football',
      subtitle: 'Ce choc de la division NFC Ouest au Levi’s Stadium met à l’épreuve la récupération après la fin de la Semaine 3.',
      excerpt: 'Brock Purdy et les 49ers accueillent Matthew Stafford et les Rams pour ouvrir la Semaine 4 de la NFL en prime time.',
      body: [
        'Après la victoire 24-20 de Philadelphie contre Dallas lundi soir, la NFL enchaîne sans attendre avec l’ouverture de la Semaine 4 au Levi’s Stadium.',
        'Il s’agit du second duel entre San Francisco et Los Angeles cette saison après le match historique de Melbourne remporté 27-7 par les 49ers grâce à trois passes de touchdown de Brock Purdy.',
        'Sur une semaine courte de préparation, Kyle Shanahan et Sean McVay savent qu’une victoire divisionnaire en octobre pèse lourd dans la course aux playoffs de la conférence NFC.',
      ],
    },
    es: {
      title: 'Previa Semana 4 de la NFL: 49ers y Rams reeditan su rivalidad en el Thursday Night Football',
      subtitle: 'Duelo clave de la NFC Oeste en el Levi’s Stadium tras cerrarse la Semana 3 con el triunfo de Filadelfia.',
      excerpt: 'Brock Purdy y los 49ers reciben a Matthew Stafford y los Rams para dar inicio a la Semana 4 en horario estelar.',
      body: [
        'Con el triunfo de Filadelfia 24-20 sobre Dallas en el retrovisor, la NFL abre de inmediato la Semana 4 con uno de los choques más intensos del fútbol americano.',
        'Los 49ers y los Rams se ven las caras por segunda vez esta temporada tras el duelo inaugural en Melbourne donde San Francisco se impuso 27-7 con tres pases de anotación de Brock Purdy.',
        'En una semana corta con solo tres días de descanso, Kyle Shanahan y Sean McVay buscarán un golpe de autoridad divisional en Santa Clara.',
      ],
    },
    de: {
      title: 'NFL Woche 4 Vorschau: 49ers und Rams eröffnen die Runde im Thursday Night Football',
      subtitle: 'NFC-West-Schlager im Levi’s Stadium fordert beide Teams nach kurzer Erholungszeit heraus.',
      excerpt: 'Brock Purdy empfängt Matthew Stafford zum Auftakt von Spielwoche 4 im kalifornischen Divisions-Klassiker.',
      body: [
        'Kaum hat Philadelphia die dritte Woche mit einem 24:20-Sieg über Dallas beendet, startet die NFL bereits in die vierte Runde.',
        'Im Levi’s Stadium treffen die San Francisco 49ers und die Los Angeles Rams nach ihrem Auftaktspiel in Melbourne erneut aufeinander.',
        'Brock Purdy und Matthew Stafford stehen im Mittelpunkt eines Duells, das für die frühe Hierarchie in der engen NFC West richtungsweisend sein wird.',
      ],
    },
    it: {
      title: 'Preview NFL Week 4: 49ers e Rams riaccendono la rivalità nel Thursday Night Football',
      subtitle: 'Scontro divisionale di NFC West al Levi’s Stadium con poco riposo dopo la chiusura della terza settimana.',
      excerpt: 'Brock Purdy e i 49ers ospitano Matthew Stafford e i Rams per aprire la Week 4 della NFL in prima serata.',
      body: [
        'Conclusa la Week 3 con il successo di Philadelphia per 24-20 su Dallas, la NFL riparte subito con la sfida tra 49ers e Rams.',
        'Le due franchigie tornano ad affrontarsi dopo il debutto a Melbourne vinto 27-7 da San Francisco con tre passaggi da touchdown di Brock Purdy.',
        'La preparazione ridotta metterà alla prova gli schemi tattici di Kyle Shanahan e Sean McVay in un match fondamentale per la NFC West.',
      ],
    },
    pl: {
      title: 'Zapowiedź 4. tygodnia NFL: 49ers i Rams wznawiają rywalizację w Thursday Night Football',
      subtitle: 'Starcie w dywizji NFC West na Levi’s Stadium po poniedziałkowym finiszu 3. kolejki.',
      excerpt: 'Brock Purdy i San Francisco 49ers podejmują Matthew Stafforda i Rams w meczu otwierającym 4. tydzień NFL.',
      body: [
        'Po poniedziałkowym zwycięstwie Philadelphii nad Dallas 24-20 liga NFL natychmiast przechodzi do inauguracji 4. tygodnia rywalizacji.',
        'San Francisco 49ers i Los Angeles Rams spotykają się po raz drugi w tym sezonie po meczu w Melbourne wygranym przez 49ers 27-7.',
        'Mecz na Levi’s Stadium po zaledwie trzech dniach odpoczynku będzie wielkim testem formy dla obu czołowych ekip NFC West.',
      ],
    },
    zh: {
      title: 'NFL第4周前瞻：49人与公羊周四夜赛再度碰撞，国联西区宿敌之战争霸',
      subtitle: '老鹰周一胜出收官第3周后，李维斯体育场迎来短休息备战的国联西区强强对决。',
      excerpt: '布罗克·珀迪率领旧金山49人主场迎战马修·斯塔福德与洛杉矶公羊，拉开NFL第4周大战序幕。',
      body: [
        '随着费城老鹰周一夜赛24-20击败牛仔，NFL赛程紧接着开启第4周争夺，国联西区最火爆的宿敌交锋在周四夜赛打响。',
        '这是旧金山49人与洛杉矶公羊本赛季的第二次交手。此前在墨尔本进行的海外揭幕战中，珀迪送出3记达阵传球率队27-7大胜公羊。',
        '两队仅有三天休整时间便转战圣克拉拉。沙纳汉与麦克维的战术博弈将直接左右国联西区初期的领跑态势。',
      ],
    },
    ja: {
      title: 'NFL第4週プレビュー：49ersとラムズがサーズデーナイトで伝統の激突',
      subtitle: 'フィラデルフィアの勝利で第3週が幕を閉じた直後、リーバイス・スタジアムでNFC西地区頂上決戦。',
      excerpt: 'ブロック・パーディ率いる49ersがマシュー・スタッフォードとラムズを迎え撃つ全米注目の第4週開幕戦。',
      body: [
        'マンデーナイトでイーグルスがカウボーイズを24-20で下した熱気冷めやらぬ中、NFLは早くも第4週の口火を切ります。',
        'サンフランシスコ49ersとロサンゼルス・ラムズの対戦は、豪州メルボルンでの開幕戦（49ersが27-7で勝利）以来今季2度目となります。',
        '中3日の過密日程の中、リーバイス・スタジアムで行われる伝統の地区対決は序盤戦の順位争いを左右する大一番となります。',
      ],
    },
    ko: {
      title: 'NFL 4주차 프리뷰: 49ers와 램스, 서스데이 나이트 풋볼서 서부 지구 격돌',
      subtitle: '이글스의 3주차 승리 후 곧바로 리바이스 스타디움에서 펼쳐지는 NFC 서부 라이벌전.',
      excerpt: '브록 퍼디의 샌프란시스코와 매튜 스태포드의 LA 램스가 프라임타임 4주차 개막전에서 격돌한다.',
      body: [
        '필라델피아가 카우보이스를 24-20으로 꺾으며 3주차를 마감한 지 얼마 되지 않아 NFL 4주차가 리바이스 스타디움에서 열린다.',
        '멜버른 해외 경기(49ers 27-7 승리)에 이어 이번 시즌 두 번째로 맞붙는 49ers와 램스는 짧은 휴식 후 다시 만난다.',
        '퍼디와 스태포드의 쿼터백 대결은 지구 선두권 경쟁의 향방을 가르는 치열한 승부가 될 전망이다.',
      ],
    },
    ar: {
      title: 'معاينة الأسبوع الرابع من دوري كرة القدم الأمريكية: مواجهة ساخنة بين 49ers ورامز',
      subtitle: 'صراع غرب المؤتمر الوطني في ملعب ليفايز يضع الجاهزية البدنية على المحك بعد ختام الأسبوع الثالث.',
      excerpt: 'يستضيف بروك بيردي وفريق 49ers ماثيو ستافورد وفريق رامز في افتتاح مواجهات الأسبوع الرابع تحت الأضواء الكاشفة.',
      body: [
        'بعد فوز فيلادلفيا المثير على دالاس بنتيجة 24-20، ينطلق الأسبوع الرابع مباشرة بمواجهة عريقة بين سان فرانسيسكو ورامز.',
        'يلتقي الفريقان للمرة الثانية هذا الموسم بعد مواجهتهما في ملبورن التي حسمها سان فرانسيسكو 27-7 بفضل ثلاث تمريرات حاسمة لبيردي.',
        'ويعد اللقاء في سانتا كلارا اختبارا تكتيكيا هاما لكايل شاناهان وشون ماكفاي في صراع صدارة المجموعة.',
      ],
    },
  },
  'arsenal-vs-psg-ucl-matchday2-emirates-2026': {
    fr: {
      title: 'Ligue des champions 2e journée : Arsenal reçoit le PSG dans un choc royal à l’Emirates',
      subtitle: 'Mikel Arteta et Luis Enrique s’affrontent à Londres pour des points capitaux dans la nouvelle phase de ligue.',
      excerpt: 'Arsenal affronte le Paris Saint-Germain à l’Emirates Stadium mercredi soir dans l’affiche phare de la 2e journée européenne.',
      body: [
        'Le football européen vit sa plus belle soirée de la semaine mercredi avec le duel au sommet entre Arsenal et le Paris Saint-Germain à l’Emirates Stadium.',
        'Deuxièmes de Premier League avec 15 points, les Gunners de Mikel Arteta s’appuient sur un Bukayo Saka étincelant et une charnière Saliba-Gabriel quasi infranchissable pour frapper un grand coup face au champion de France.',
        'Le PSG de Luis Enrique se présente avec une formation rajeunie et incisive emmenée par Bradley Barcola et Ousmane Dembélé, désireuse de consolider sa place dans le top 8 qualificatif pour les huitièmes de finale.',
      ],
    },
    es: {
      title: 'Champions League Jornada 2: Arsenal y PSG chocan en un duelo de gigantes en el Emirates',
      subtitle: 'Mikel Arteta y Luis Enrique se miden en Londres con puntos vitales y prestigio continental en juego.',
      excerpt: 'El Arsenal recibe al París Saint-Germain en el Emirates Stadium este miércoles en el partido más esperado de la jornada.',
      body: [
        'La Liga de Campeones ofrece su gran espectáculo de la semana este miércoles cuando el Arsenal y el París Saint-Germain salten al césped del Emirates Stadium.',
        'El equipo de Mikel Arteta llega en gran momento tras sumar 15 puntos en la Premier League, respaldado por la creatividad de Bukayo Saka y una defensa impenetrable liderada por William Saliba.',
        'El PSG de Luis Enrique apuesta por la velocidad de Bradley Barcola y Ousmane Dembélé para sumar tres puntos cruciales en la fase de liga y aspirar a los puestos de clasificación directa.',
      ],
    },
    de: {
      title: 'Champions League Spieltag 2: Arsenal empfängt PSG zum europäischen Topspiel im Emirates',
      subtitle: 'Mikel Arteta und Luis Enrique kämpfen in London um wichtige Punkte in der Ligaphase.',
      excerpt: 'Arsenal trifft am Mittwochabend im Emirates Stadium auf Paris Saint-Germain im Kracher des 2. Spieltags.',
      body: [
        'Europäischer Spitzenfußball garantiert am Mittwochabend Hochspannung, wenn der FC Arsenal im Emirates Stadium auf Paris Saint-Germain trifft.',
        'Mit 15 Punkten auf Rang zwei der Premier League präsentiert sich die Mannschaft von Mikel Arteta in bestechender Form, angetrieben von Bukayo Saka und einer stabilen Abwehr.',
        'PSG reist mit einem jungen, hochpressenden Team um Shootingstar Bradley Barcola an, um sich eine Spitzenposition unter den besten acht Mannschaften der Ligaphase zu sichern.',
      ],
    },
    it: {
      title: 'Champions League 2ª giornata: Arsenal contro PSG, scontro tra titani all’Emirates',
      subtitle: 'Mikel Arteta e Luis Enrique si affrontano a Londra con in palio punti pesanti per la classifica della fase a girone unico.',
      excerpt: 'L’Arsenal ospita il Paris Saint-Germain all’Emirates Stadium nel match clou del mercoledì di Champions League.',
      body: [
        'Serata di grande fascino a Londra dove l’Emirates Stadium ospita la sfida di cartello della seconda giornata di Champions League tra Arsenal e Paris Saint-Germain.',
        'I Gunners di Arteta arrivano all’appuntamento con 15 punti in Premier League e puntano sulla fantasia di Bukayo Saka e sulla solidità difensiva di Saliba per superare i campioni di Francia.',
        'Il PSG di Luis Enrique si affida al talento offensivo di Bradley Barcola e Ousmane Dembélé per strappare punti preziosi nella corsa alla qualificazione diretta agli ottavi.',
      ],
    },
    pl: {
      title: 'Liga Mistrzów 2. kolejka: Arsenal kontra PSG w hicie na Emirates Stadium',
      subtitle: 'Mikel Arteta i Luis Enrique walczą w Londynie o cenne punkty w fazie ligowej europejskich pucharów.',
      excerpt: 'Arsenal podejmuje Paris Saint-Germain w najciekawszym starciu środowej serii spotkań Ligi Mistrzów.',
      body: [
        'Europejski futbol osiąga najwyższy poziom emocji w środę na Emirates Stadium podczas wielkiego starcia Arsenalu z Paris Saint-Germain.',
        'Arsenal zajmuje drugie miejsce w Premier League z 15 punktami, imponując dyscypliną taktyczną i formą Bukayo Saki oraz Williama Saliby.',
        'Paryżanie prowadzeni przez Luisa Enrique stawiają na dynamikę Bradleya Barcoli i chcą wywieźć z Londynu punkty przybliżające ich do czołowej ósemki tabeli ligowej.',
      ],
    },
    zh: {
      title: '欧冠第2轮焦点战：阿森纳主场决战巴黎圣日耳曼，酋长球场迎来豪门对决',
      subtitle: '阿尔特塔与恩里克伦敦斗法，联赛阶段关键积分与欧洲豪门威望在聚光灯下揭晓。' ,
      excerpt: '周三晚间阿森纳在酋长球场迎战法甲霸主巴黎圣日耳曼，上演欧冠第2轮最受瞩目的巅峰战役。',
      body: [
        '周三晚间的酋长球场成为欧洲足坛的绝对中心，阿森纳与巴黎圣日耳曼的巅峰较量为欧冠第2轮定下最强基调。',
        '在阿尔特塔率领下，阿森纳以15分紧随曼城位列英超积分榜次席。萨卡的前场组织与萨利巴统领的稳固防线，让枪手具备了向欧冠奖杯发起冲击的底气。',
        '恩里克率领的年轻化大巴黎同样来势汹汹，巴尔科拉与登贝莱在边路的穿透力极强。在全新36队大联赛制下，每1分都直接决定着能否直通欧冠16强。',
      ],
    },
    ja: {
      title: 'UEFAチャンピオンズリーグ第2節：アーセナル対PSG、エミレーツで欧州最高峰の激突',
      subtitle: 'アルテタとルイス・エンリケがロンドンで激突。決勝トーナメント直行へ重要な勝ち点争い。',
      excerpt: 'アーセナルが本拠地エミレーツ・スタジアムにパリ・サンジェルマンを迎える欧州CL第2節の注目カード。',
      body: [
        '欧州サッカー最高峰の舞台で水曜夜屈指のビッグマッチが実現。エミレーツ・スタジアムでアーセナルとパリ・サンジェルマンが激突します。',
        'プレミアリーグで15ポイントを獲得し好調を維持するアルテタ監督率いるアーセナルは、サカのチャンスメイクと強固な守備陣を武器に勝利を狙います。',
        '対するPSGも新星バルコラやデンベレを擁するスピード感溢れる攻撃陣でロンドン遠征に臨み、上位8チーム入りを目指します。',
      ],
    },
    ko: {
      title: 'UEFA 챔피언스리그 2차전: 아스널 vs PSG, 에미레이츠 스타디움서 펼쳐지는 빅매치',
      subtitle: '아르테타와 루이스 엔리케의 전술 대결. 리그 페이즈 상위권 선점을 향한 격돌.',
      excerpt: '아스널이 수요일 밤 홈에서 파리 생제르맹을 상대로 챔피언스리그 2차전 최대 빅매치를 치른다.',
      body: [
        '유럽 최고의 축구 제전이 수요일 밤 런던 에미레이츠 스타디움에서 아스널과 파리 생제르맹의 맞대결로 최고조에 달한다.',
        '프리미어리그 15점으로 2위를 달리는 아스널은 부카요 사카의 창의성과 윌리엄 살리바의 수비벽을 앞세워 프랑스 챔피언을 맞이한다.',
        '엔리케 감독의 PSG는 바르콜라와 뎀벨레의 기동력을 바탕으로 16강 직행 티켓이 걸린 8위권 진입을 노린다.',
      ],
    },
    ar: {
      title: 'دوري أبطال أوروبا الجولة الثانية: أرسنال يواجه باريس سان جيرمان في قمة ملعب الإمارات',
      subtitle: 'صراع ناري بين ميكيل أرتيتا ولويس إنريكي على نقاط ثمينة في مرحلة الدوري الأوروبية.',
      excerpt: 'يستضيف أرسنال بطل فرنسا باريس سان جيرمان مساء الأربعاء في أبرز مواجهات الجولة الثانية من دوري الأبطال.',
      body: [
        'تتجه أنظار عشاق الكرة الأوروبية مساء الأربعاء إلى ملعب الإمارات بلندن لمتابعة القمة المرتقبة بين أرسنال وباريس سان جيرمان.',
        'يدخل أرسنال اللقاء وهو في وصافة الدوري الإنجليزي برصيد 15 نقطة معتمدا على إبداع بوكايو ساكا وصلابة دفاعه بقيادة ساليبا.',
        'في المقابل، يسعى باريس سان جيرمان بقيادة لويس إنريكي وتألق باركولا وديمبيلي لخطف فوز ثمين يعزز موقعه بين الثمانية الكبار.',
      ],
    },
  },
  'china-open-2026-round1-sinner-sabalenka-beijing': {
    fr: {
      title: 'China Open 1er tour : Sinner lance la défense de son titre, Sabalenka et Zheng régalent à Pékin',
      subtitle: 'Le numéro 1 mondial écarte Safiullin en deux manches pendant que le public chinois acclame sa championne olympique.',
      excerpt: 'Jannik Sinner s’impose 6-3, 6-4 à Pékin, tandis qu’Aryna Sabalenka et Zheng Qinwen filent au deuxième tour.',
      body: [
        'La tournée asiatique a débuté sur les chapeaux de roue mercredi au Centre National de Tennis de Pékin avec une démonstration du tenant du titre Jannik Sinner.',
        'Le numéro 1 mondial italien a disposé de Roman Safiullin 6-3, 6-4 en 82 minutes, ne concédant pas la moindre balle de break et s’appuyant sur 84 % de réussite derrière sa première balle.',
        'Sur le Diamond Court, Aryna Sabalenka a dominé Kalinina 6-2, 6-3, tandis que l’héroïne locale Zheng Qinwen a fait chavirer les 15 000 spectateurs en écrasant Rakhimova 6-1, 6-1.',
      ],
    },
    es: {
      title: 'Abierto de China Ronda 1: Sinner inicia su defensa con autoridad; Sabalenka y Zheng brillan en Pekín',
      subtitle: 'El número 1 del mundo supera a Safiullin en sets corridos mientras el público local vitorea a la campeona olímpica.',
      excerpt: 'Jannik Sinner vence 6-3 y 6-4 en su debut en Pekín, mientras Sabalenka y Zheng Qinwen avanzan con paso firme.',
      body: [
        'La gira asiática de pista dura arrancó este miércoles en el Centro Nacional de Tenis de Pekín con una actuación impecable del vigente campeón Jannik Sinner.',
        'El número 1 mundial italiano doblegó a Roman Safiullin por 6-3 y 6-4 en 82 minutos, sin conceder puntos de rotura y ganando el 84% de los puntos con su primer servicio.',
        'En la pista central Diamond Court, Aryna Sabalenka se impuso 6-2 y 6-3 a Kalinina, mientras la campeona olímpica local Zheng Qinwen arrolló a Rakhimova 6-1 y 6-1 ante el delirio de la afición.',
      ],
    },
    de: {
      title: 'China Open Runde 1: Sinner startet Titelverteidigung souverän; Sabalenka und Zheng glänzen in Peking',
      subtitle: 'Die Nummer 1 der Welt schlägt Safiullin glatt in zwei Sätzen, während Olympiasiegerin Zheng das Heimpublikum begeistert.',
      excerpt: 'Jannik Sinner gewinnt 6:3, 6:4 in Peking; Aryna Sabalenka und Zheng Qinwen ziehen mühelos in Runde 2 ein.',
      body: [
        'Der asiatische Hartplatz-Herbst begann am Mittwoch im Nationalen Tenniszentrum in Peking standesgemäß mit einem dominanten Auftritt von Jannik Sinner.',
        'Der italienische Weltranglistenerste bezwang Roman Safiullin mit 6:3 und 6:4 in 82 Minuten, ohne eine einzige Breakchance zuzulassen.',
        'Auf dem Diamond Court siegte Aryna Sabalenka souverän mit 6:2 und 6:3 über Kalinina, während Chinas Olympiasiegerin Zheng Qinwen beim 6:1, 6:1 über Rakhimova für Begeisterungsstürme sorgte.',
      ],
    },
    it: {
      title: 'China Open 1° turno: Sinner inizia la difesa del titolo vincendo; Sabalenka e Zheng show a Pechino',
      subtitle: 'Il numero 1 del mondo batte Safiullin in due set al National Tennis Center, mentre il pubblico di casa acclama Zheng.',
      excerpt: 'Jannik Sinner supera Safiullin 6-3, 6-4 all’esordio a Pechino, mentre Sabalenka e Zheng volano al secondo turno.',
      body: [
        'La trasferta asiatica sul cemento è partita nel migliore dei modi mercoledì a Pechino grazie alla prova di forza del campione in carica Jannik Sinner.',
        'L’altoatesino numero 1 del mondo ha sconfitto Roman Safiullin per 6-3, 6-4 in 82 minuti, servendo con l’84% di resa sulla prima e senza concedere break.',
        'Sul Diamond Court Aryna Sabalenka ha regolato la Kalinina 6-2, 6-3, mentre l’idolo di casa Zheng Qinwen ha travolto la Rakhimova 6-1, 6-1 tra gli applausi del pubblico cinese.',
      ],
    },
    pl: {
      title: 'China Open 1. runda: Sinner rozpoczyna obronę tytułu od zwycięstwa; Sabalenka i Zheng błyszczą w Pekinie',
      subtitle: 'Lider rankingu pokonuje Safiullina w dwóch setach, a Zheng porywa chińską publiczność.',
      excerpt: 'Jannik Sinner wygrywa 6-3, 6-4 na inaugurację w Pekinie; Aryna Sabalenka i Zheng Qinwen meldują się w 2. rundzie.',
      body: [
        'Azjatycka część sezonu na kortach twardych wystartowała w środę w Pekinie od mocnego uderzenia obrońcy tytułu Jannika Sinnera.',
        'Włoski numer 1 na świecie pokonał Romana Safiullina 6-3, 6-4 w 82 minuty, nie broniąc ani jednego break pointa w całym spotkaniu.',
        'Na korcie Diamond Aryna Sabalenka ograła Kalininę 6-2, 6-3, natomiast mistrzyni olimpijska Zheng Qinwen rozbiła Rakhimovą 6-1, 6-1 ku radości miejscowych kibiców.',
      ],
    },
    zh: {
      title: '中网首轮战报：辛纳完胜萨菲乌林开启卫冕，萨巴伦卡郑钦文携手晋级',
      subtitle: '世界第一在国家网球中心两盘直落过关，本土奥运冠军郑钦文引爆钻石球场狂欢。',
      excerpt: '辛纳以6-3、6-4轻取萨菲乌林开启中网之旅，萨巴伦卡与郑钦文强势晋级女单次轮。',
      body: [
        '周三的北京国家网球中心正式打响亚洲硬地赛季巅峰战役，卫冕冠军、世界第一辛纳展现王者霸气。',
        '辛纳在整场82分钟的对决中未送出任何破发点，一发得分率高达84%，以6-3、6-4干脆利落地击败萨菲乌林，顺利闯过首轮关。',
        '在钻石球场，美网亚军萨巴伦卡以6-2、6-3力克加里宁娜；巴黎奥运会金牌得主郑钦文更是手感火热，仅用时58分钟便以6-1、6-1横扫拉希莫娃，引发全场上万名观众的热烈欢呼。',
      ],
    },
    ja: {
      title: 'チャイナ・オープン1回戦：シナーがストレート勝ちで連覇へ好発進、サバレンカと鄭欽文も圧勝',
      subtitle: '世界ランク1位が北京でサフィウリンを一蹴。地元の大声援を受けた五輪覇者・鄭も2回戦へ。',
      excerpt: 'ヤニック・シナーが6-3、6-4で北京初戦を快勝。サバレンカと鄭欽文も盤石の強さで勝ち上がり。',
      body: [
        '水曜日の北京・国家テニスセンターでアジアのハードコートシーズンが開幕し、ディフェンディング王者のシナーが圧巻のプレーを見せました。',
        'イタリアの世界王者シナーはファーストサーブ時のポイント獲得率84％を記録し、1つのブレークポイントも与えず6-3、6-4でサフィウリンを退けました。',
        'ダイヤモンド・コートではサバレンカが6-2、6-3で快勝し、パリ五輪金メダリストの鄭欽文も6-1、6-1で相手を圧倒して大観衆を沸かせました。',
      ],
    },
    ko: {
      title: '차이나 오픈 1라운드: 시너 무실점 세트 완승으로 타이틀 방어 시동, 사발렌카 정친원 순항',
      subtitle: '세계 1위 시너가 베이징 개막전서 사피울린을 제압했고 정친원이 홈 팬들의 환호를 이끌었다.',
      excerpt: '야닉 시너가 6-3, 6-4 완승으로 2라운드에 올랐고, 아리나 사발렌카와 정친원도 완벽한 승리를 거뒀다.',
      body: [
        '아시아 하드코트 스윙이 수요일 베이징 국가테니스센터에서 본격 개막하며 디펜딩 챔피언 야닉 시너가 압도적인 기량을 선보였다.',
        '세계 1위 시너는 단 하나의 브레이크 포인트도 내주지 않는 완벽한 서브 게임을 앞세워 로만 사피울린을 6-3, 6-4로 완파했다.',
        '다이아몬드 코트에서는 사발렌카가 6-2, 6-3으로 승리했고, 올림픽 금메달리스트 정친원은 라키모바를 6-1, 6-1로 꺾고 홈 관중을 열광시켰다.',
      ],
    },
    ar: {
      title: 'بطولة الصين المفتوحة الدور الأول: سينر يفتتح رحلة الدفاع عن لقبه وسابالينكا وتشنغ تتألقان في بكين',
      subtitle: 'المصنف الأول عالميا يتخطى سافيولين بمجموعتين دون رد وسط هتافات الجماهير الصينية لنجمتهم تشنغ.',
      excerpt: 'حقق يانيك سينر فوزا مقنعا 6-3 و6-4 في بكين، بينما عبرت أرينا سابالينكا وتشنغ تشينوين بسهولة للدور الثاني.',
      body: [
        'انطلقت منافسات الملاعب الصلبة الآسيوية يوم الأربعاء في المركز الوطني للتنس ببكين وسط تألق حامل اللقب يانيك سينر.',
        'وفرض النجم الإيطالي المصنف الأول عالميا أسلوبه ليفوز 6-3 و6-4 على رومان سافيولين دون أن يمنح منافسه أي فرصة لكسر الإرسال.',
        'وفي منافسات السيدات على ملعب دايموند، فازت سابالينكا 6-2 و6-3، بينما سحقت البطلة الأولمبية الصينية تشنغ منافستها راخيموفا 6-1 و6-1.',
      ],
    },
  },
  'pga-tour-sanderson-farms-pro-am-tee-times-2026': {
    fr: {
      title: 'Sanderson Farms Championship : fin du Pro-Am et départs fixés pour le 1er tour à Jackson',
      subtitle: 'Kevin Yu et Mackenzie Hughes mènent la vague matinale au Country Club of Jackson avec 500 points en jeu.',
      excerpt: 'Le Pro-Am officiel s’achève à Jackson, lançant le sprint du FedExCup Fall sur le PGA Tour dès jeudi.',
      body: [
        'Après la ferveur de la Presidents Cup à Medinah, le golf professionnel se tourne vers la bataille pour le maintien sur le circuit.',
        'Le Pro-Am officiel du Sanderson Farms Championship s’est achevé mercredi sous le soleil de Jackson, scellant les horaires du premier tour.',
        'Le tenant du titre Kevin Yu partira jeudi à 7h45 aux côtés de Mackenzie Hughes et Emiliano Grillo, tandis que Rickie Fowler et Sam Burns s’élanceront l’après-midi.',
      ],
    },
    es: {
      title: 'Sanderson Farms Championship: concluye el Pro-Am y quedan listos los horarios en Jackson',
      subtitle: 'Kevin Yu y Mackenzie Hughes encabezan el grupo matinal con 500 puntos de la FedExCup en juego.',
      excerpt: 'El Country Club de Jackson finaliza la jornada de preparación antes de la Ronda 1 del FedExCup Fall.',
      body: [
        'Tras la emoción de la Presidents Cup en Medinah, el golf profesional afronta la dura lucha por asegurar los derechos de juego en el PGA Tour.',
        'El Pro-Am oficial del Sanderson Farms Championship concluyó este miércoles en el Country Club de Jackson con el sorteo de salidas para el jueves.',
        'El campeón defensor Kevin Yu saldrá a las 7:45 hora local junto a Mackenzie Hughes y Emiliano Grillo, con Rickie Fowler compitiendo en el turno vespertino.',
      ],
    },
    de: {
      title: 'Sanderson Farms Championship: Pro-Am beendet und Startzeiten für Runde 1 in Jackson stehen fest',
      subtitle: 'Kevin Yu und Mackenzie Hughes starten am Donnerstagmorgen im Country Club of Jackson ins Turnier.',
      excerpt: 'Die Vorbereitung in Mississippi ist abgeschlossen; der FedExCup Fall beginnt am Donnerstag mit Runde 1.',
      body: [
        'Nach dem Jubel über den Presidents Cup in Medinah kehrt der PGA-Tour-Alltag mit dem Kampf um Tourkarten für 2027 zurück.',
        'Am Mittwoch ging das offizielle Pro-Am im Country Club of Jackson zu Ende und die Startzeiten für den Auftakt wurden bestätigt.',
        'Titelverteidiger Kevin Yu startet um 7:45 Uhr Ortszeit gemeinsam mit Mackenzie Hughes und Emiliano Grillo in Runde 1.',
      ],
    },
    it: {
      title: 'Sanderson Farms Championship: concluso il Pro-Am, definiti gli orari del 1° giro a Jackson',
      subtitle: 'Kevin Yu e Mackenzie Hughes aprono il programma mattutino al Country Club of Jackson.',
      excerpt: 'Terminata la giornata di vigilia in Mississippi per l’avvio del FedExCup Fall del PGA Tour.',
      body: [
        'Chiusa la parentesi della Presidents Cup a Medinah, il PGA Tour riparte con il serrato confronto per la permanenza nel circuito.',
        'Al Country Club di Jackson si è svolto il Pro-Am ufficiale che ha stabilito i tee time della prima giornata di giovedì.',
        'Il campione uscente Kevin Yu scenderà in campo alle 7:45 con Mackenzie Hughes ed Emiliano Grillo alla caccia di punti pesanti.',
      ],
    },
    pl: {
      title: 'Sanderson Farms Championship: Pro-Am zakończony, godziny startu 1. rundy w Jackson ustalone',
      subtitle: 'Kevin Yu i Mackenzie Hughes na czele porannej grupy w walce o 500 punktów FedExCup.',
      excerpt: 'Zakończył się oficjalny Pro-Am w Mississippi przed czwartkowym otwarciem cyklu FedExCup Fall.',
      body: [
        'Po emocjach Presidents Cup w Medinah uwaga zawodowego golfa skupia się na rywalizacji o pełne prawa gry w 2027 roku.',
        'W środę na polu Country Club of Jackson dobiegł końca oficjalny Pro-Am, który ustalił pary na czwartkową 1. rundę turnieju.',
        'Obrońca tytułu Kevin Yu wystartuje o 7:45 rano czasu lokalnego w grupie z Mackenziem Hughesem oraz Emiliano Grillo.',
      ],
    },
    zh: {
      title: '桑德森农场锦标赛：职业业余配对赛落幕，杰克逊首轮出发时间出炉',
      subtitle: '卫冕冠军俞俊安携手休斯领衔周四早场，500个联邦快递杯积分与全卡豁免展开争夺。',
      excerpt: '杰克逊乡村俱乐部结束官方配对赛，美巡赛秋季积分赛首站即将在密西西比正式开杆。',
      body: [
        '麦迪纳总统杯的喧嚣落幕后，职业高尔夫球坛迅速转向残酷的保卡争夺战。',
        '周三桑德森农场锦标赛职业业余配对赛在杰克逊乡村俱乐部顺利结束，周四首轮焦点组出发时间正式公布。',
        '卫冕冠军俞俊安将于早晨7点45分从1号洞开球，同组名将包括休斯与格里略；福勒与伯恩斯则将在下午场亮相。',
      ],
    },
    ja: {
      title: 'サンダーソン・ファームズ選手権：プロアマ戦終了、ジャクソンで初日組み合わせ決定',
      subtitle: 'ディフェンディング王者のケビン・ユーらが木曜朝の第1組でティオフへ。',
      excerpt: 'カントリー・クラブ・オブ・ジャクソンで大会前日のプロアマが終了し、フェデックスカップ秋季初戦の準備が完了。',
      body: [
        'プレジデンツカップの余韻を残しつつ、PGAツアーは2027年のシード権を巡るフォールシリーズ初戦を迎えます。',
        'ミシシッピ州のカントリー・クラブ・オブ・ジャクソンでは水曜日にプロアマ戦が終了し、初日のティオフ時間が決定しました。',
        '連覇を狙うケビン・ユーは午前7時45分にヒューズ、グリ略と同組でスタートし、午後はリッキー・ファウラーらが登場します。',
      ],
    },
    ko: {
      title: '샌더슨 팜스 챔피언십: 프로암 종료, 잭슨 1라운드 티타임 확정',
      subtitle: '디펜딩 챔피언 케빈 유와 매켄지 휴즈가 목요일 오전 티오프를 준비한다.',
      excerpt: '잭슨 컨트리 클럽에서 공식 프로암이 마무리되며 페덱스컵 가을 시리즈 첫 대회의 막이 오른다.',
      body: [
        '프레지던츠컵의 열기 뒤로 PGA 투어 선수들은 2027 시즌 시드권을 지키기 위한 가을 혈투에 돌입한다.',
        '수요일 미시시피 잭슨 컨트리 클럽에서 공식 프로암 행사가 끝나고 1라운드 조 편성이 완료되었다.',
        '디펜딩 챔피언 케빈 유는 현지 시각 오전 7시 45분 1번 홀에서 매켄지 휴즈, 에밀리아노 그리요와 함께 출격한다.',
      ],
    },
    ar: {
      title: 'بطولة ساندرسون فارمز: اختتام جولة المحترفين وتحديد مواعيد انطلاق الدور الأول في جاكسون',
      subtitle: 'كيفن يو وماكنزي هيوز يقودان الانطلاقة الصباحية في كانتري كلوب أوف جاكسون لحصد نقاط فيديكس كاب.',
      excerpt: 'اختتمت الجولة الاستعدادية في مسيسيبي قبل انطلاق الجولة الأولى الحاشدة في بطولة ساندرسون فارمز.',
      body: [
        'عقب إسدال الستار على كأس الرؤساء في ميدينا، يتجدد الصراع على البقاء في جولة بي جيه إيه لضمان بطاقات المشاركة.',
        'اختتمت الأربعاء الفعاليات التمهيدية لبطولة ساندرسون فارمز وتحددت مواعيد انطلاق منافسات الدور الأول يوم الخميس.',
        'وينطلق حامل اللقب كيفن يو عند الساعة 7:45 صباحا برفقة ماكنزي هيوز وإيميليانو غريلو بحثا عن التتويج مجددا.',
      ],
    },
  },
  'f1-singapore-gp-paddock-day-antonelli-title-focus-2026': {
    fr: {
      title: 'Grand Prix de Singapour : le paddock de Marina Bay s’anime, Antonelli serein sous les projecteurs',
      subtitle: 'Le leader du championnat aborde la chaleur tropicale avec 88 points d’avance face aux évolutions de Ferrari et McLaren.',
      excerpt: 'La F1 s’installe à Singapour pour la course nocturne, Kimi Antonelli menant la danse avec 88 points d’avance.',
      body: [
        'Le paddock de Formule 1 a ouvert ses portes mercredi après-midi au bord de l’eau à Marina Bay sous une chaleur humide étouffante de 31 degrés.',
        'Fort de sa victoire autoritaire à Bakou, le prodige de Mercedes Kimi Antonelli aborde la manche nocturne en tête du mondial avec 317 points, soit 88 longueurs d’avance sur George Russell.',
        'Dans les garages voisins, Ferrari et McLaren ont déballé des ailerons à fort appui pour contrer les Flèches d’Argent sur ce tracé sinueux de 19 virages.',
      ],
    },
    es: {
      title: 'Gran Premio de Singapur: el paddock de Marina Bay cobra vida y Antonelli asume el foco del título',
      subtitle: 'El líder del campeonato afronta el calor tropical con 88 puntos de ventaja mientras Ferrari y McLaren traen mejoras.',
      excerpt: 'La Fórmula 1 aterriza en Marina Bay para la carrera nocturna con Kimi Antonelli al frente con 88 puntos de renta.',
      body: [
        'El paddock de la Fórmula 1 comenzó su actividad este miércoles junto a la bahía de Singapur bajo un calor sofocante de 31 grados y alta humedad.',
        'Tras su contundente triunfo de semáforo a bandera en Bakú, el joven piloto de Mercedes Kimi Antonelli lidera el Mundial con 317 puntos, 88 más que George Russell.',
        'Ferrari y McLaren confían en sus paquetes de alta carga aerodinámica para plantar batalla a las Flechas de Plata en las 19 curvas de Marina Bay.',
      ],
    },
    de: {
      title: 'Großer Preis von Singapur: Marina-Bay-Paddock erwacht zum Leben, Antonelli im Titel-Fokus',
      subtitle: 'Der WM-Führende trotzt der Tropenhitze mit 88 Punkten Vorsprung, während Ferrari und McLaren Upgrades bringen.',
      excerpt: 'Die Formel 1 rüstet sich in Singapur für das Nachtrennen, Kimi Antonelli reist mit 88 Zählern Vorsprung an.',
      body: [
        'Im Fahrerlager von Marina Bay herrschte am Mittwochnachmittag bei schweißtreibenden 31 Grad tropischer Hitze reges Treiben.',
        'Nach seinem dominanten Sieg in Baku führt Mercedes-Shootingstar Kimi Antonelli die Weltmeisterschaft mit 317 Punkten und 88 Zählern Vorsprung souverän an.',
        'Ferrari und McLaren haben spezielle High-Downforce-Pakete für die 19 Kurven im Gepäck, um Mercedes beim anspruchsvollen Nachtrennen herauszufordern.',
      ],
    },
    it: {
      title: 'Gran Premio di Singapore: il paddock di Marina Bay si accende, Antonelli concentrato sul titolo',
      subtitle: 'Il leader iridato gestisce 88 punti di vantaggio nel caldo tropicale mentre Ferrari e McLaren preparano novità aerodinamiche.',
      excerpt: 'La Formula 1 si prepara alla notte di Marina Bay con Kimi Antonelli saldamente al comando con 88 punti su Russell.',
      body: [
        'Il paddock di Marina Bay si è animato mercoledì pomeriggio sul lungomare di Singapore con 31 gradi di temperatura e un’afa asfissiante.',
        'Forte del successo dominatore a Baku, il rookie della Mercedes Kimi Antonelli guida il mondiale con 317 punti, a +88 sul compagno Russell.',
        'Ferrari e McLaren sono pronte a dare battaglia con ali ad alto carico per sfruttare la proverbiale agilità sui 19 tornanti del tracciato cittadino.',
      ],
    },
    pl: {
      title: 'Grand Prix Singapuru: padok na Marina Bay tętni życiem, Antonelli w centrum uwagi',
      subtitle: 'Lider mistrzostw przybywa do tropikalnego Singapuru z przewagą 88 punktów, a Ferrari i McLaren szykują poprawki.',
      excerpt: 'Formuła 1 instaluje się w Singapurze przed nocnym wyścigiem, z Kimim Antonellim na czele klasyfikacji.',
      body: [
        'Padok Formuły 1 w środowe popołudnie ożył w tropikalnym upale Singapuru, przygotowując się do 18. rundy sezonu.',
        'Po pewnym triumfie w Baku Kimi Antonelli z Mercedesa ma na koncie 317 punktów i 88 oczek przewagi nad George’em Russellem.',
        'Inżynierowie Ferrari i McLarena liczą, że pakiety aerodynamiczne o wysokim docisku pozwolą im powalczyć o zwycięstwo pod jupiterami.',
      ],
    },
    zh: {
      title: '新加坡大奖赛：滨海湾围场全面启动，安东内利领跑争冠焦点',
      subtitle: '积分领跑者在热带高温下手握88分巨大优势，法拉利与迈凯伦携高下压力套件出击。',
      excerpt: 'F1夜赛大军进驻滨海湾赛道，19岁梅赛德斯超新星安东内利以317分强势领跑车手积分榜。',
      body: [
        '周三下午的新加坡滨海湾围场全面进入备战状态，全员在31摄氏度的高温高湿环境下完成了车房与赛车的最后调试。',
        '刚在巴库杆位领跑夺冠的梅赛德斯超级新星安东内利以317分高居榜首，领先队友拉塞尔达88分之多，面对媒体采访展现出成熟的争冠定力。',
        '法拉利的汉密尔顿、勒克莱尔以及迈凯伦的诺里斯均带来了针对慢速弯角的高下压力套件，力争在19个弯角的夜赛街道战中逆袭银箭。',
      ],
    },
    ja: {
      title: 'シンガポールGP：マリーナベイのパドックが始動、アントネッリが王座へ視界良好',
      subtitle: '選手権首位が88点リードで熱帯夜の決戦へ。フェラーリとマクラーレンは空力改善で対抗。',
      excerpt: 'F1サーカスがマリーナベイに到着。キミ・アントネッリが317ポイントでシンガポール夜戦に挑む。',
      body: [
        '水曜午後のマリーナベイ市街地サーキットは気温31度、湿度85％の熱帯気候の中、週末のナイトレースに向けてパドックが始動しました。',
        'バクーでポール・トゥ・ウィンを飾ったメルセデスのキミ・アントネッリは317点を獲得し、同僚ラッセルに88点差をつけて首位を独走しています。',
        '一方のフェラーリとマクラーレンは高ダウンフォース仕様のウイングを投入し、19のコーナーが待ち受ける市街地コースでメルセデス追撃を誓います。',
      ],
    },
    ko: {
      title: '싱가포르 GP: 마리나 베이 패덕 개장, 안토넬리 88점 차 챔피언십 독주 체제',
      subtitle: '열대야의 시가지 서킷에서 메르세데스 루키가 317점으로 선두를 달리는 가운데 페라리와 맥라렌이 업그레이드로 맞선다.',
      excerpt: 'F1 서커스가 마리나 베이에 입성해 야간 레이스 준비를 마쳤다. 안토넬리가 여유 있는 리드를 지키고 있다.',
      body: [
        '수요일 오후 싱가포르 마리나 베이 패덕은 31도의 무더위와 높은 습도 속에서 주말 야간 레이스를 위한 장비 점검을 마쳤다.',
        '바쿠에서 폴투윈을 거둔 메르세데스의 19세 루키 키미 안토넬리는 317점으로 조지 러셀에 88점 앞서며 차분하게 미디어를 맞이했다.',
        '페라리와 맥라렌은 마리나 베이의 19개 코너에 맞춘 고다운포스 에어로 패키지를 장착하고 메르세데스 독주 저지에 나선다.',
      ],
    },
    ar: {
      title: 'جائزة سنغافورة الكبرى: حلبة مارينا باي تستقبل أبطال فورمولا 1 وأنتونيللي يتصدر المشهد',
      subtitle: 'متصدر بطولة العالم يدخل السباق الليلي بأفضلية 88 نقطة وسط ترقب لتحديثات فيراري وماكلارين.',
      excerpt: 'تستعد حلبة مارينا باي لسباق سنغافورة الليلي المثير تحت الأضواء الكاشفة وكيمي أنتونيللي في الصدارة.',
      body: [
        'دبت الحياة في مرآب حلبة مارينا باي بعد ظهر الأربعاء تحت أجواء سنغافورة الحارة والرطبة استعدادا للجولة الثامنة عشرة.',
        'يدخل الإيطالي كيمي أنتونيللي السباق الليلي برصيد 317 نقطة وبفارق 88 نقطة عن زميله جورج راسل إثر فوزه المستحق في باكو.',
        'وفي المقابل، تسعى فيراري وماكلارين للاستفادة من المنعطفات التسعة عشر الضيقة لحلبة الشوارع لتقليص الفارق مع مرسيدس.',
      ],
    },
  },
  'arsenal-2-0-psg-ucl-statement-victory-2026': {
    fr: {
      title: 'Ligue des Champions : Arsenal surclasse le PSG 2-0 dans un choc magistral à l’Emirates',
      subtitle: 'Mikel Arteta et les Gunners signent une démonstration tactique et défensive face aux champions de France.',
      excerpt: 'Kai Havertz et Bukayo Saka marquent en première période pour offrir à Arsenal une victoire 2-0 nette face au Paris Saint-Germain.',
      body: [
        'Les grandes soirées européennes à l’Emirates exigent du caractère, et Arsenal a répondu présent mercredi soir face au Paris Saint-Germain.',
        'Kai Havertz a ouvert le score dès la 20e minute d’une tête rageuse sur un centre millimétré de Leandro Trossard. Bukayo Saka a ensuite doublé la mise à la 35e minute sur un coup franc brossé qui a surpris toute la défense parisienne.',
        'Avec une charnière Saliba-Gabriel intraitable et trois parades décisives de David Raya, Arsenal s’empare de quatre points précieux en phase de ligue sans encaisser le moindre but.',
      ],
    },
    es: {
      title: 'Champions League: Arsenal derrota 2-0 al PSG con autoridad en el Emirates Stadium',
      subtitle: 'El equipo de Mikel Arteta exhibe solidez táctica y defensiva para superar a los campeones de Francia.',
      excerpt: 'Goles de Kai Havertz y Bukayo Saka en la primera mitad sellan el 2-0 del Arsenal sobre el Paris Saint-Germain.',
      body: [
        'Las noches europeas en el Emirates exigen jerarquía, y el Arsenal dio un golpe sobre la mesa este miércoles ante el Paris Saint-Germain.',
        'Kai Havertz abrió el marcador en el minuto 20 al anticiparse de cabeza tras un preciso centro de Leandro Trossard. Quince minutos después, Bukayo Saka amplió la cuenta con un tiro libre envenenado que despistó a toda la zaga parisina.',
        'Sostenido por una defensa infranqueable liderada por Saliba y Gabriel, el Arsenal suma cuatro puntos en la fase de liga manteniendo su arco en cero.',
      ],
    },
    de: {
      title: 'Champions League: Arsenal bezwingt PSG mit 2:0 nach taktischer Meisterleistung',
      subtitle: 'Mikel Artetas Gunners setzen mit Toren von Havertz und Saka ein dickes Ausrufezeichen gegen Paris Saint-Germain.',
      excerpt: 'Kai Havertz und Bukayo Saka treffen vor der Pause zum verdienten 2:0-Heimsieg von Arsenal gegen PSG.',
      body: [
        'Europäische Nächte im Emirates Stadium verlangen höchste Konzentration, und Arsenal lieferte am Mittwochabend gegen Paris Saint-Germain voll ab.',
        'Kai Havertz köpfte die Gunners in der 20. Minute nach herrlicher Trossard-Flanke in Führung. In der 35. Minute legte Bukayo Saka per direktem Freistoß nach, der an Freund und Feind vorbei ins Netz segelte.',
        'Mit einer kompromisslosen Defensivleistung um Saliba und Gabriel sowie einem glänzenden David Raya feierte Arsenal den zweiten Zu-Null-Auftritt in der Ligaphase.',
      ],
    },
    it: {
      title: 'Champions League: l’Arsenal piega il PSG 2-0 con Havertz e Saka all’Emirates',
      subtitle: 'I Gunners di Mikel Arteta dominano tatticamente i campioni di Francia e salgono a quattro punti.',
      excerpt: 'Le reti di Kai Havertz e Bukayo Saka nel primo tempo decidono la sfida dell’Emirates Stadium per l’Arsenal contro il PSG.',
      body: [
        'Le grandi serate europee all’Emirates richiedono autorevolezza, e l’Arsenal non ha tradito le attese superando 2-0 il Paris Saint-Germain.',
        'Kai Havertz ha sbloccato la gara al 20’ con un perfetto stacco di testa su cross di Leandro Trossard. Al 35’ Bukayo Saka ha raddoppiato su punizione velenosa battendo Gianluigi Donnarumma.',
        'Guidata da una coppia centrale Saliba-Gabriel insuperabile e dalle parate di David Raya, la retroguardia londinese ha blindato un successo continentale di prestigio.',
      ],
    },
    pl: {
      title: 'Liga Mistrzów: Arsenal pokonuje PSG 2:0 po taktycznym popisie na Emirates',
      subtitle: 'Zespół Mikela Artety zagrał po mistrzowsku w defensywie i nie dał szans mistrzom Francji.',
      excerpt: 'Kai Havertz i Bukayo Saka strzelają gole w pierwszej połowie, dając Arsenalowi triumf 2:0 nad Paris Saint-Germain.',
      body: [
        'Europejskie wieczory na Emirates Stadium wymagają żelaznej dyscypliny, a Arsenal zaprezentował ją w pełnej krasie przeciwko PSG.',
        'Kai Havertz otworzył wynik w 20. minucie precyzyjnym strzałem głową po dośrodkowaniu Leandro Trossarda. W 35. minucie Bukayo Saka podwyższył bezpośrednio z rzutu wolnego.',
        'Znakomita postawa duetu Saliba-Gabriel i kluczowe interwencje Davida Rayi zapewniły Kanonierom kolejne czyste konto i cenne punkty w fazie ligowej.',
      ],
    },
    zh: {
      title: '欧冠联赛：阿森纳2-0完胜巴黎圣日耳曼，哈弗茨与萨卡闪耀酋长球场',
      subtitle: '阿尔特塔的球队在主场展现出色的战术纪律与防守硬度，击败法甲冠军巴黎。',
      excerpt: '哈弗茨头球破门，萨卡任意球建功，阿森纳在欧冠第二轮主场2-0力克巴黎圣日耳曼。',
      body: [
        '酋长球场的欧冠之夜见证了一场高水平对决，阿森纳凭借严密的防守与高效的进攻2-0战胜巴黎圣日耳曼。',
        '比赛第20分钟，特罗萨德左路送出精准传中，哈弗茨抢前点头槌破网首开纪录；第35分钟，萨卡开出极具威胁的右侧任意球直接窜入远角。',
        '萨利巴与加布里埃尔领衔的后防线固若金汤，拉亚多次做出关键扑救，枪手在欧冠联赛阶段前两轮收获4分且未失一球。',
      ],
    },
    ja: {
      title: 'UEFAチャンピオンズリーグ：アーセナルがPSGを2-0で撃破、ハヴァーツとサカが導く快勝',
      subtitle: 'アルテタ率いるガナーズが本拠地エミレーツで堅守と決定力を発揮しフランス王者を完封。',
      excerpt: 'ハヴァーツのヘディングとサカの直接FKでアーセナルがPSGに2-0で勝利し、欧冠で勝点4に到達。',
      body: [
        'エミレーツ・スタジアムの欧冠ナイトマッチで、アーセナルが組織力と戦術的完成度を示しPSGを2-0で退けました。',
        '前半20分にトロサールのクロスからハヴァーツが頭で合わせて先制すると、35分にはサカの鋭いフリーキックがそのままゴールに吸い込まれました。',
        'サリバとガブリエウを中心とする守備陣は隙を見せず、GKラヤの好セーブも光り、プレミアリーグ第7節に向けて弾みをつけました。',
      ],
    },
    ko: {
      title: 'UEFA 챔피언스리그: 아스널, 하베르츠와 사카 연속골로 PSG 2-0 완파',
      subtitle: '미켈 아르테타 감독의 맞춤 전술과 무실점 수비가 빛난 에미레이츠 스타디움의 밤.',
      excerpt: '카이 하베르츠의 헤더 선제골과 부카요 사카의 프리킥 추가골로 아스널이 파리 생제르맹을 2-0으로 제압했다.',
      body: [
        '수요일 밤 런던 에미레이츠 스타디움에서 열린 챔피언스리그 2차전에서 아스널이 파리 생제르맹을 상대로 2-0 완승을 거뒀습니다.',
        '전반 20분 트로사르의 날카로운 크로스를 하베르츠가 헤더로 연결해 골망을 흔들었고, 35분 사카의 프리킥이 그대로 득점으로 이어졌습니다.',
        '살리바와 마갈량이스의 탄탄한 수비벽과 라야 골키퍼의 선방 속에 아스널은 리그 페이즈 2경기 연속 무실점을 기록했습니다.',
      ],
    },
    ar: {
      title: 'دوري أبطال أوروبا: أرسنال يتفوق على باريس سان جيرمان 2-0 بثنائية هافيرتز وساكا',
      subtitle: 'كتيبة ميكل أرتيتا تقدم درسا تكتيكيا ودفاعيا في ملعب الإمارات وتهزم بطل فرنسا بجدارة.',
      excerpt: 'أرسنال يحسم قمة الجولة الثانية من دوري الأبطال بالفوز 2-0 على باريس سان جيرمان بهدفي هافيرتز وساكا.',
      body: [
        'أثبت أرسنال جاهزيته للمنافسة القارية بعدما حقق فوزا مستحقا على باريس سان جيرمان بهدفين نظيفين في ملعب الإمارات.',
        'افتتح كاي هافيرتز التسجيل في الدقيقة 20 بضربة رأسية متقنة إثر عرضية تروسار، قبل أن يضيف بوكايو ساكا الهدف الثاني من ركلة حرة مباشرة خادعت الدفاع.',
        'وتألق الثنائي ويليام ساليبا وغابرييل في إغلاق المنافذ أمام هجوم باريس، بينما تصدى ديفيد رايا ببراعة لمحاولات الفريق الفرنسي ليحافظ الغانرز على نظافة شباكهم.',
      ],
    },
  },
  'nfl-week4-tnf-49ers-rams-kickoff-tonight-2026': {
    fr: {
      title: 'NFL Semaine 4 : les 49ers accueillent les Rams au Levi’s Stadium pour le choc du jeudi soir',
      subtitle: 'Rivalité intense en NFC West sur semaine courte : Brock Purdy et Matthew Stafford se disputent la suprématie.',
      excerpt: 'San Francisco et Los Angeles ouvrent la semaine 4 ce soir au Levi’s Stadium lors du Thursday Night Football.',
      body: [
        'Après un match du lundi soir disputé, la NFL enchaîne sans répit avec le coup d’envoi de la quatrième semaine.',
        'Ce soir à Santa Clara, les San Francisco 49ers retrouvent les Los Angeles Rams pour un duel de division primordial. Vainqueurs 27-7 lors du match d’ouverture en Australie, les 49ers veulent confirmer leur ascendant.',
        'Matthew Stafford et Kyren Williams entendent bien riposter pour ramener les Rams à 2-2 dans une rencontre où la gestion de la fatigue sera décisive.',
      ],
    },
    es: {
      title: 'NFL Semana 4: 49ers y Rams abren el telón esta noche en el Thursday Night Football',
      subtitle: 'Duelo divisional del Oeste de la NFC con descanso corto: Brock Purdy y Matthew Stafford frente a frente en Santa Clara.',
      excerpt: 'Los 49ers reciben a los Rams en el Levi’s Stadium para inaugurar la Semana 4 de la temporada regular de la NFL.',
      body: [
        'Sin tregua tras la emocionante jornada anterior, la NFL da inicio a su cuarta semana con un choque divisional de alto voltaje.',
        'En el Levi’s Stadium de Santa Clara, los 49ers buscan afianzar su liderazgo en el Oeste de la NFC ante unos Rams necesitados de victoria.',
        'Brock Purdy comandará el ataque local apoyado en Christian McCaffrey, mientras Matthew Stafford intentará dar la sorpresa en terreno rival.',
      ],
    },
    de: {
      title: 'NFL Woche 4: 49ers empfangen die Rams zum Auftakt im Thursday Night Football',
      subtitle: 'NFC-West-Rivalität auf kurzer Rast: Brock Purdy und Matthew Stafford kämpfen um die Divisionsspitze.',
      excerpt: 'San Francisco und Los Angeles eröffnen heute Nacht im Levi’s Stadium die vierte Woche der NFL-Saison.',
      body: [
        'Ohne Pause geht es in der NFL weiter: Woche 4 startet heute Nacht mit dem traditionsreichen Duell in der NFC West.',
        'Die 49ers wollen vor heimischer Kulisse im Levi’s Stadium nach dem 27:7-Auftaktsieg in Melbourne erneut gegen die Rams triumphieren.',
        'Für Quarterback Matthew Stafford und Head Coach Sean McVay steht viel auf dem Spiel, um den Anschluss in der Division nicht zu verlieren.',
      ],
    },
    it: {
      title: 'NFL Week 4: i 49ers ospitano i Rams al Levi’s Stadium nel Thursday Night Football',
      subtitle: 'Rivalità storica nella NFC West con pochi giorni di riposo: Brock Purdy sfida Matthew Stafford a Santa Clara.',
      excerpt: 'San Francisco e i Los Angeles Rams aprono la quarta settimana NFL questa sera in prima serata al Levi’s Stadium.',
      body: [
        'Il calendario NFL non conosce soste: la Week 4 prende il via questa notte con una classica della NFC West.',
        'I San Francisco 49ers cercano la conferma dopo il successo della prima giornata contro i Rams, puntando sulla precisione di Brock Purdy.',
        'Stafford e Williams guidano l’attacco di Los Angeles alla ricerca del riscatto in una trasferta storicamente insidiosa.',
      ],
    },
    pl: {
      title: 'NFL Tydzień 4: 49ers podejmują Rams na Levi’s Stadium w meczu czwartkowym',
      subtitle: 'Zacięta walka w dywizji NFC West po krótkim odpoczynku: Brock Purdy kontra Matthew Stafford.',
      excerpt: 'San Francisco 49ers i Los Angeles Rams otwierają 4. kolejkę NFL podczas Thursday Night Football.',
      body: [
        'Czwarty tydzień rozgrywek NFL startuje od prestiżowego starcia w Santa Clara pomiędzy odwiecznymi rywalami z NFC West.',
        'Gospodarze z San Francisco chcą wykorzystać atut własnego boiska, opierając grę na Purdym oraz McCaffreyu.',
        'Rams pod wodzą Matthew Stafforda zamierzają wyrównać bilans bezpośrednich spotkań po porażce na otwarcie sezonu w Melbourne.',
      ],
    },
    zh: {
      title: 'NFL第4周揭幕战：49人主场迎战公羊，周四夜赛引爆国联西区内战',
      subtitle: '短周休整迎来关键对决，普尔迪携手麦卡弗里与老将斯塔福德争夺分区榜首。',
      excerpt: '旧金山49人今晚在李维斯体育场迎战洛杉矶公羊，正式拉开NFL常规赛第4周序幕。',
      body: [
        '在经历了激烈的前三周比赛后，NFL第4周今晚将在加州圣克拉拉的李维斯体育场火热开打。',
        '旧金山49人此前在墨尔本揭幕战曾以27-7轻取公羊，今晚主场作战渴望实现对同区死敌的双杀。',
        '斯塔福德与威廉姆斯领衔的公羊进攻组势必全力反扑，体能与战术调整将成为本场周四夜赛的决胜关键。',
      ],
    },
    ja: {
      title: 'NFL第4週：49ersが本拠地にラムズを迎えるサーズデーナイトフットボール',
      subtitle: '中3日の過密日程で激突するNFC西地区の宿敵対決。パーディとスタッフォードが激突。',
      excerpt: 'リーバイス・スタジアムでサンフランシスコ・49ersとロサンゼルス・ラムズが第4週開幕戦を戦う。',
      body: [
        'NFLは休む間もなく第4週へと突入し、今夜リーバイス・スタジアムで伝統のNFC西地区対決が行われます。',
        '開幕戦メルボルンで27-7と快勝した49ersは、クォーターバックのブロック・パーディを中心に地区首位固めを狙います。',
        '対するラムズのベテラン司令塔マシュー・スタッフォードは、ショートウィークの難局を乗り越え敵地でのリベンジを誓います。',
      ],
    },
    ko: {
      title: 'NFL 4주차 킥오프: 49ers, 리바이스 스타디움서 램스와 목요 풋볼 격돌',
      subtitle: '짧은 휴식 뒤 맞붙는 NFC 서부지구 라이벌전. 브록 퍼디와 매슈 스태퍼드의 정면승부.',
      excerpt: '샌프란시스코 49ers와 LA 램스가 오늘 밤 캘리포니아 산타클라라에서 NFL 4주차 개막전을 치른다.',
      body: [
        '치열했던 3주차가 끝나자마자 NFL 4주차가 목요일 밤 리바이스 스타디움에서 화려하게 개막합니다.',
        '호주 멜버른 1주차에서 27-7 완승을 거뒀던 49ers는 브록 퍼디의 지휘 아래 지구 라이벌전 2연승을 노립니다.',
        '스태퍼드가 이끄는 램스는 2승 2패 균형을 맞추기 위해 빠른 템포의 공격으로 샌프란시스코 수비진을 흔들 계획입니다.',
      ],
    },
    ar: {
      title: 'الدوري الأمريكي لكرة القدم الأسبوع الرابع: 49ers يستضيف رامز في قمة ليلة الخميس',
      subtitle: 'صراع مثير في القسم الغربي لفرق NFC بين بروك بيردي وماثيو ستافورد في سانتا كلارا.',
      excerpt: 'يفتتح سان فرانسيسكو ولوس أنجلوس رامز منافسات الأسبوع الرابع من NFL على ملعب ليفايز الليلة.',
      body: [
        'تتواصل الإثارة في دوري كرة القدم الأمريكية بانطلاق مباريات الأسبوع الرابع في مواجهة نارية تجمع الغريمين التقليديين.',
        'يسعى سان فرانسيسكو لتكرار فوزه على رامز بعد تفوقه في الجولة الأولى، متسلحا بجاهزية بروك بيردي وكريستيان ماكافري.',
        'في المقابل، يدخل رامز بقيادة الخبير ماثيو ستافورد اللقاء بطموح تعديل المسار والعودة بانتصار ثمين خارج الديار.',
      ],
    },
  },
  'wnba-playoffs-semifinals-locked-aces-liberty-2026': {
    fr: {
      title: 'Play-offs WNBA : les Aces et le Liberty qualifiés, le dernier carré est scellé',
      subtitle: 'Quatre balayages 2-0 historiques dans le premier tour ouvrent la voie à des demi-finales explosives.',
      excerpt: 'A’ja Wilson et Breanna Stewart guident Las Vegas et New York vers des sweeps 2-0 pour rejoindre le Minnesota et l’Indiana.',
      body: [
        'Le premier tour des play-offs WNBA 2026 s’est achevé mercredi soir avec une domination absolue des favorites en déplacement.',
        'À Arlington, A’ja Wilson a signé 28 points et 13 rebonds pour permettre aux Aces de dominer Dallas 88-74 et d’assurer leur billet.',
        'Dans le même temps à San Francisco, le New York Liberty a contenu les Valkyries 80-76 grâce à un panier primé décisif de Sabrina Ionescu. Les demi-finales opposeront le Lynx au Fever et les Aces au Liberty.',
      ],
    },
    es: {
      title: 'Playoffs WNBA: Aces y Liberty firman barridas y sellan unas semifinales estelares',
      subtitle: 'Por primera vez en la historia, las cuatro series de primera ronda se deciden por 2-0.',
      excerpt: 'A’ja Wilson brilla con 28 puntos y Breanna Stewart lidera a New York para unirse a Lynx y Fever en la ronda semifinal.',
      body: [
        'La primera ronda de la postemporada WNBA concluyó este miércoles con autoridad total de los equipos visitantes.',
        'En Texas, A’ja Wilson impartió una lección con 28 puntos y 13 rebotes para guiar a Las Vegas Aces al triunfo 88-74 sobre Dallas.',
        'En el Chase Center, New York Liberty superó 80-76 a Golden State con un triple providencial de Sabrina Ionescu, cerrando unas semifinales soñadas entre Lynx-Fever y Aces-Liberty.',
      ],
    },
    de: {
      title: 'WNBA-Playoffs: Aces und Liberty machen Halbfinal-Feld mit Sweeps komplett',
      subtitle: 'Vier historische 2:0-Seriensiege in Runde 1 ebnen den Weg für echte Halbfinal-Kracher.',
      excerpt: 'A’ja Wilson dominiert für Las Vegas und Breanna Stewart führt New York zum 2:0-Sweep ins Halbfinale.',
      body: [
        'Die erste Runde der WNBA-Playoffs 2026 endete am Mittwochabend mit einem historischen Meilenstein.',
        'A’ja Wilson führte die Las Vegas Aces mit 28 Punkten und 13 Rebounds zu einem souveränen 88:74-Erfolg über die Dallas Wings.',
        'Gleichzeitig behauptete sich der New York Liberty mit 80:76 bei den Golden State Valkyries, sodass alle vier Serien mit 2:0 endeten. Im Halbfinale treffen Lynx auf Fever sowie Aces auf Liberty.',
      ],
    },
    it: {
      title: 'Playoff WNBA: Aces e Liberty completano il quadro delle semifinali con un secco 2-0',
      subtitle: 'Quattro sweep su quattro al primo turno: il tabellone propone Lynx-Fever e Aces-Liberty.',
      excerpt: 'A’ja Wilson e Breanna Stewart trascinano Las Vegas e New York al secondo turno dei playoff WNBA.',
      body: [
        'Il primo turno della post-season WNBA 2026 è andato in archivio mercoledì sera con un verdetto unanime: tutte le serie chiuse sul 2-0.',
        'A Dallas, una monumentale A’ja Wilson da 28 punti e 13 rimbalzi ha spinto le Aces all’88-74 finale.',
        'Al Chase Center di San Francisco, il New York Liberty ha piegato 80-76 le Valkyries con una tripla chiave di Sabrina Ionescu, regalando al pubblico due semifinali imperdibili.',
      ],
    },
    pl: {
      title: 'Play-off WNBA: Aces i Liberty przypieczętowują awans, skład półfinałów skompletowany',
      subtitle: 'Wszystkie cztery serie pierwszej rundy zakończyły się wynikami 2:0 na korzyść faworytek.',
      excerpt: 'A’ja Wilson i Breanna Stewart poprowadziły Las Vegas oraz New York do pewnych zwycięstw i awansu do najlepszej czwórki.',
      body: [
        'Środowe mecze wyłoniły komplet półfinalistek tegorocznych play-offów ligi WNBA w bezprecedensowym stylu.',
        'A’ja Wilson rzuciła 28 punktów i zebrała 13 piłek, prowadząc Las Vegas Aces do wygranej 88:74 nad Dallas Wings.',
        'Z kolei New York Liberty wygrały 80:76 z Golden State Valkyries, pieczętując awans do starcia z Aces, podczas gdy Lynx zagrają z Fever.',
      ],
    },
    zh: {
      title: 'WNBA季后赛半决赛对阵出炉：王牌与自由人横扫晋级，四强席位全部锁定',
      subtitle: '首轮四组对决全部以2-0横扫收尾创历史纪录，半决赛山猫对阵狂热、王牌再战自由人。',
      excerpt: '阿贾·威尔逊砍下28分13篮板助王牌晋级，斯图尔特率自由人险胜女武神锁定四强。',
      body: [
        '周三晚WNBA季后赛首轮全部战罢，两支客场作战的豪强展现冠军底蕴，双双以2-0横扫对手。',
        '在得克萨斯，常规赛MVP阿贾·威尔逊轰下28分13个篮板和4次封盖，率领拉斯维加斯王牌88-74大胜达拉斯飞翼。',
        '在旧金山大通中心，纽约自由人凭借约内斯库最后时刻的关键三分以80-76力克金州女武神，半决赛将上演山猫对狂热、王牌对自由人的超级对决。',
      ],
    },
    ja: {
      title: 'WNBAプレーオフ準決勝進出チーム決定：エイシズとリバティがスイープで4強進出',
      subtitle: '1回戦4カード全てが2勝0敗のストレート決着。リンクス対フィーバー、エイシズ対リバティの豪華カードが実現。',
      excerpt: 'エイジャ・ウィルソンが28得点13リバウンド、スチュワートが21得点でそれぞれチームをスイープ勝利へ牽引。',
      body: [
        '水曜日に行われた第2戦で、アウェーの有力チームが地力を発揮しWNBAプレーオフ1回戦は歴史的な幕切れを迎えました。',
        'ラスベガス・エイシズのエース、エイジャ・ウィルソンは28得点13リバウンドの圧倒的スタッツでダラス・ウィングスを88-74で撃破。',
        'ニューヨーク・リバティもチェイス・センターでゴールデンステート・ヴァルキリーズを80-76で振り切り、4強出揃いとなりました。',
      ],
    },
    ko: {
      title: 'WNBA 플레이오프 4강 확정: 에이시스와 리버티 2-0 스윕으로 준결승 합류',
      subtitle: '1라운드 4개 매치업 모두 2연승 스윕 기록. 링스-피버, 에이시스-리버티 4강 빅매치 성사.',
      excerpt: '에이자 윌슨이 28득점 13리바운드로 댈러스를 격파했고 브리아나 스튜어트의 리버티도 골든스테이트를 꺾고 준결승에 올랐다.',
      body: [
        '수요일 밤 WNBA 플레이오프 1라운드가 모두 종료되며 리그 역사상 처음으로 4개 시리즈가 전부 2-0 스윕으로 마무리되었습니다.',
        '라스베이거스 에이시스는 에이자 윌슨의 28득점 맹활약에 힘입어 댈러스 윙스를 88-74로 완파했습니다.',
        '뉴욕 리버티 역시 샌프란시스코 원정에서 골든스테이트를 80-76으로 제압해, 준결승에서는 링스 대 피버, 에이시스 대 리버티의 명승부가 펼쳐집니다.',
      ],
    },
    ar: {
      title: 'نهائيات دوري السلة الأمريكي للسيدات: إيسيس وليبرتي يكملان المربع الذهبي بعد اكتساح تاريخي',
      subtitle: 'انتهاء جميع مواجهات الدور الأول بنتيجة 2-0 يمهد لنصف نهائي ناري بين لينكس وفيفر وإيسيس ضد ليبرتي.',
      excerpt: 'تألقت إيجا ويلسون وبريانا ستيوارت لتقودا لاس فيغاس ونيويورك إلى الدور نصف النهائي بعد فوزين متتاليين.',
      body: [
        'اختتمت منافسات الدور الأول من بلاي أوف WNBA مساء الأربعاء بتحقيق الفرق المرشحة للانتصار في جميع المواجهات.',
        'وسجلت العملاقة إيجا ويلسون 28 نقطة و13 متابعة لتقود لاس فيغاس إيسيس لتخطي دالاس وينغز بنتيجة 88-74.',
        'وفي سان فرانسيسكو، نجح نيويورك ليبرتي في تجاوز غولدن ستيت بنتيجة 80-76، ليكتمل المربع الذهبي للبطولة.',
      ],
    },
  },
  'china-open-2026-alcaraz-medvedev-gauff-beijing': {
    fr: {
      title: 'Open de Chine : Carlos Alcaraz dompte le service de Mpetshi Perricard, Medvedev et Gauff s’imposent',
      subtitle: 'Le n°2 mondial passe l’obstacle français en deux sets aux côtés de Daniil Medvedev et Coco Gauff à Pékin.',
      excerpt: 'Alcaraz l’emporte 6-4, 6-4 à Pékin pendant que Medvedev et Gauff rejoignent également les huitièmes de finale.',
      body: [
        'L’Open de Chine est monté d’un cran jeudi au Centre national de tennis de Pékin avec l’entrée en lice des têtes de série.',
        'Face aux services flashés à plus de 230 km/h de Giovanni Mpetshi Perricard, Carlos Alcaraz a livré une partition impeccable en retour pour s’imposer 6-4, 6-4 sans concéder la moindre balle de break.',
        'Dans le tableau féminin, Coco Gauff n’a fait qu’une bouchée de Clara Burel (6-1, 6-2 en 64 minutes), tandis que Daniil Medvedev a écarté Gaël Monfils 6-3, 6-4.',
      ],
    },
    es: {
      title: 'Abierto de China: Carlos Alcaraz desactiva el servicio de Mpetshi Perricard; Medvedev y Gauff avanzan',
      subtitle: 'El número dos del mundo solventa su estreno en Pekín por 6-4 y 6-4 con gran solidez al resto.',
      excerpt: 'Carlos Alcaraz supera a Giovanni Mpetshi Perricard mientras Daniil Medvedev y Coco Gauff sellan victorias en el Diamond Court.',
      body: [
        'La jornada del jueves en Pekín brindó tenis de alto nivel en el Centro Nacional con victorias rotundas de las principales figuras.',
        'Carlos Alcaraz neutralizó los cañonazos a más de 230 km/h del francés Giovanni Mpetshi Perricard para sellar un doble 6-4 en una hora y 21 minutos.',
        'Por su parte, Daniil Medvedev venció a Gaël Monfils por 6-3 y 6-4, y en el cuadro WTA Coco Gauff arrolló a Clara Burel 6-1, 6-2.',
      ],
    },
    de: {
      title: 'China Open: Carlos Alcaraz entschärft Mpetshi Perricard, auch Medvedev und Gauff im Achtelfinale',
      subtitle: 'Die Nummer 2 der Welt meistert den Auftakt in Peking souverän mit 6:4, 6:4.',
      excerpt: 'Alcaraz bezwingt Mpetshi Perricard in zwei Sätzen, während Medvedev und Gauff ebenfalls glatt gewinnen.',
      body: [
        'Am Donnerstag zog das Tempo bei den China Open in Peking spürbar an, als Carlos Alcaraz sein Auftaktmatch bestritt.',
        'Gegen die Aufschlaggranaten von Giovanni Mpetshi Perricard fand Alcaraz stets die richtige Antwort und siegte souverän mit 6:4, 6:4.',
        'Daniil Medvedev setzte sich zeitgleich mit 6:3, 6:4 gegen Gaël Monfils durch, während Coco Gauff Clara Burel in 64 Minuten mit 6:1, 6:2 deklassierte.',
      ],
    },
    it: {
      title: 'China Open: Carlos Alcaraz doma il servizio di Mpetshi Perricard; avanti Medvedev e Gauff a Pechino',
      subtitle: 'Il numero due al mondo vince 6-4, 6-4 e raggiunge gli ottavi con prestazioni solide dei top player.',
      excerpt: 'Alcaraz supera l’ostacolo francese mentre Daniil Medvedev batte Monfils e Coco Gauff concede solo tre game a Burel.',
      body: [
        'Giovedì di grande spettacolo al National Tennis Center di Pechino con i big del circuito protagonisti in campo.',
        'Carlos Alcaraz ha disinnescato le bordate oltre i 230 km/h di Giovanni Mpetshi Perricard imponendosi con un doppio 6-4 senza concedere palle break.',
        'Vittoria convincente anche per Daniil Medvedev su Gaël Monfils (6-3, 6-4) e passeggiata per Coco Gauff, a segno 6-1, 6-2 su Clara Burel.',
      ],
    },
    pl: {
      title: 'China Open: Carlos Alcaraz neutralizuje serwis Mpetshi Perricarda, awans Miedwiediewa i Gauff',
      subtitle: 'Wicelider rankingu ATP pewnie wygrywa 6:4, 6:4 i melduje się w kolejnej rundzie w Pekinie.',
      excerpt: 'Alcaraz pokonuje Mpetshi Perricarda, a Daniił Miedwiediew i Coco Gauff bez problemu przechodzą dalej.',
      body: [
        'Czwartkowe mecze China Open w Pekinie przyniosły triumfy faworytów przed entuzjastycznie nastawioną publicznością.',
        'Carlos Alcaraz poradził sobie z potężnymi serwisami Giovanniego Mpetshi Perricarda, zwyciężając 6:4, 6:4 w 81 minut.',
        'Dalej grają również Daniił Miedwiediew po pokonaniu Gaëla Monfilsa 6:3, 6:4 oraz Coco Gauff, która rozbiła Clarę Burel 6:1, 6:2.',
      ],
    },
    zh: {
      title: '中国网球公开赛：阿尔卡拉斯化解发球大炮过关，梅德韦杰夫与高芙齐进次轮',
      subtitle: '世界第二以两个6-4击败佩里卡尔，钻石球场巨星悉数过关闪耀北京金秋。',
      excerpt: '阿尔卡拉斯直落两盘击败佩里卡尔，梅德韦杰夫击败孟菲尔斯，高芙横扫布雷尔挺进16强。',
      body: [
        '周四的北京国家网球中心热闹非凡，男单2号种子阿尔卡拉斯迎来了极具杀伤力的法国重炮手佩里卡尔。',
        '面对对手时速超230公里的强力发球，阿尔卡拉斯展现顶尖接发水平，两盘各破发一次，以两个6-4顺利取胜。',
        '随后登场的梅德韦杰夫以6-3、6-4战胜老将孟菲尔斯；女子方面，高芙仅用时64分钟便以6-1、6-2横扫布雷尔轻松晋级。',
      ],
    },
    ja: {
      title: 'チャイナ・オープン：アルカラスがペリカーの豪速球サーブを攻略、メドベージェフとガウフも快勝',
      subtitle: '世界2位のアルカラスが6-4、6-4のストレート勝ちで北京のファンを魅了。',
      excerpt: 'カルロス・アルカラスが初戦を完勝で突破。ダニール・メドベージェフとココ・ガウフも順当に勝ち進んだ。',
      body: [
        '北京のナショナル・テニス・センターで行われた木曜日の試合で、トップシード勢が貫禄のテニスを披露しました。',
        '時速230キロを超えるサーブを連発するペリカーに対し、アルカラスは的確なリターンで各セット1ブレークを奪い6-4、6-4で勝利。',
        'メドベージェフもモンフィスを6-3、6-4で退け、女子ではガウフがビュレルを6-1、6-2で圧倒して3回戦進出を決めました。',
      ],
    },
    ko: {
      title: '차이나 오픈: 알카라스 시속 230km 강서브 잠재우고 16강행, 메드베데프 고프 순항',
      subtitle: '세계 2위 알카라스가 6-4, 6-4 완승으로 베이징 개막전을 장식했다.',
      excerpt: '카를로스 알카라스가 엠페치 페리카르를 제압했고 다닐 메드베데프와 코코 고프도 깔끔한 승리를 거뒀다.',
      body: [
        '목요일 베이징 국가테니스센터에서 펼쳐진 차이나 오픈 32강전에서 알카라스가 특유의 수비력과 리턴 능력을 입증했습니다.',
        '프랑스의 신성 엠페치 페리카르의 시속 230km 대포알 서브를 침착하게 받아낸 알카라스는 브레이크 기회를 놓치지 않고 6-4, 6-4로 승리했습니다.',
        '메드베데프도 몽피스를 6-3, 6-4로 꺾었으며, 여자부에서는 코코 고프가 뷔렐을 6-1, 6-2로 완파하며 가볍게 다음 라운드에 올랐습니다.',
      ],
    },
    ar: {
      title: 'بطولة الصين المفتوحة: ألكاراز يروض إرسالات بيريكار الصاروخية وميدفيديف وغوف يعبران في بكين',
      subtitle: 'المصنف الثاني عالميا يفوز 6-4 و6-4 ليحجز مقعده في الدور الثاني إلى جانب نخبة النجوم.',
      excerpt: 'حقق كارلوس ألكاراز فوزا مستحقا على بيريكار، بينما تألق دانييل ميدفيديف وكوكو غوف في بكين.',
      body: [
        'شهد المركز الوطني للتنس في بكين يوم الخميس مستويات رفيعة مع دخول كبار المصنفين في منافسات البطولة.',
        'ونجح الإسباني كارلوس ألكاراز في كسر إرسال الفرنسي بيريكار الذي تجاوزت سرعته 230 كم/ساعة، لينهي اللقاء 6-4 و6-4 دون خسارة أي شوط إرسال.',
        'وفاز دانييل ميدفيديف على غايل مونفيس 6-3 و6-4، في حين اكتسحت الأمريكية كوكو غوف منافستها كلارا بوريل 6-1 و6-2 في 64 دقيقة.',
      ],
    },
  },
  'pga-tour-sanderson-farms-round1-jackson-live-2026': {
    fr: {
      title: 'Sanderson Farms Championship : Chesson Hadley et Beau Hossler prennent les commandes du 1er tour',
      subtitle: 'Le tenant du titre Kevin Yu signe un solide 68 (-4) pour lancer la course aux points du FedExCup Fall à Jackson.',
      excerpt: 'Hadley et Hossler signent des cartes de 66 (-6) pour s’emparer de la tête du Sanderson Farms Championship dans le Mississippi.',
      body: [
        'Le suspense du FedExCup Fall a débuté jeudi matin au Country Club of Jackson dans des conditions de jeu idéales.',
        'Chesson Hadley et Beau Hossler ont profité des greens réceptifs pour rendre de magnifiques cartes de 66 (-6), comptant chacun sept birdies.',
        'Le vainqueur sortant Kevin Yu a entamé la défense de son titre avec un 68 sans accroc (-4), tandis que Mackenzie Hughes et Emiliano Grillo restent en embuscade à 69.',
      ],
    },
    es: {
      title: 'Sanderson Farms Championship: Chesson Hadley y Beau Hossler marcan el ritmo en la Ronda 1',
      subtitle: 'El campeón defensor Kevin Yu debuta con 68 golpes (-4) al inicio de la lucha por la tarjeta del PGA Tour.',
      excerpt: 'Hadley y Hossler colideran en Jackson con sendas rondas de 66 golpes (-6) en el arranque del FedExCup Fall.',
      body: [
        'La batalla por la permanencia en el PGA Tour arrancó este jueves en el Country Club de Jackson con juego agresivo y grandes registros.',
        'Chesson Hadley y Beau Hossler fijaron la referencia en la casa club con 6 bajo par (66 golpes) gracias a una gran efectividad con el putt.',
        'El vigente campeón Kevin Yu firmó una sólida vuelta de 68 impactos (-4), metiéndose de lleno en el grupo de cabeza junto a Mackenzie Hughes.',
      ],
    },
    de: {
      title: 'Sanderson Farms Championship: Chesson Hadley und Beau Hossler führen nach Runde 1',
      subtitle: 'Titelverteidiger Kevin Yu startet mit einer 68 (-4) ins Turnier im Country Club of Jackson.',
      excerpt: 'Hadley und Hossler teilen sich nach Auftaktrunden von 66 Schlägen (-6) die Führung in Mississippi.',
      body: [
        'Der FedExCup Fall der PGA Tour hat am Donnerstag im Country Club of Jackson mit starkem Golf begonnen.',
        'Chesson Hadley und Beau Hossler nutzten die perfekten Morgenbedingungen für fehlerfreie 66er-Runden (-6) und setzten sich an die Spitze.',
        'Titelverteidiger Kevin Yu blieb mit einer 68 (-4) schlagdistanznah, während Mackenzie Hughes mit 69 Schlägen (-3) ebenfalls gut im Rennen liegt.',
      ],
    },
    it: {
      title: 'Sanderson Farms Championship: Chesson Hadley e Beau Hossler in vetta al termine del 1° giro',
      subtitle: 'Il campione in carica Kevin Yu apre con un solido 68 (-4) nella prima tappa del FedExCup Fall a Jackson.',
      excerpt: 'Hadley e Hossler firmano un 66 (-6) e guidano la classifica del Sanderson Farms Championship in Mississippi.',
      body: [
        'Le emozioni del FedExCup Fall sono scattate giovedì mattina al Country Club of Jackson con punteggi molto bassi.',
        'Chesson Hadley e Beau Hossler hanno dettato il passo con due ottimi giri in 66 colpi (-6), realizzando sette birdie ciascuno.',
        'Partenza positiva per il campione uscente Kevin Yu, autore di un 68 (-4) senza sbavature per rimanere a contatto con i primi.',
      ],
    },
    pl: {
      title: 'Sanderson Farms Championship: Chesson Hadley i Beau Hossler liderami po 1. rundzie',
      subtitle: 'Obrońca tytułu Kevin Yu zaczyna od 68 uderzeń (-4) w walce o punkty FedExCup w Jackson.',
      excerpt: 'Hadley i Hossler uzyskali po 66 uderzeń (-6), obejmując prowadzenie na otwarcie turnieju w Mississippi.',
      body: [
        'Jesienna seria PGA Tour wystartowała w czwartek na polu Country Club of Jackson przy znakomitych warunkach pogodowych.',
        'Chesson Hadley i Beau Hossler wykorzystali miękkie greeny, notując po 66 uderzeń (-6) i dzieląc pozycję lidera w domku klubowym.',
        'Obrońca trofeum Kevin Yu rozpoczął występ od pewnego wyniku 68 (-4), co daje mu doskonałą pozycję wyjściową przed piątkiem.',
      ],
    },
    zh: {
      title: '桑德森农场锦标赛：哈德利与霍斯勒首轮并列领跑，俞俊安68杆稳步出发',
      subtitle: '杰克逊乡村俱乐部迎来低杆风暴，卫冕冠军抓下四鸟打出低于标准杆4杆开门红。',
      excerpt: '哈德利与霍斯勒打出66杆（-6）领跑首轮，俞俊安68杆开启美巡秋季赛卫冕征程。',
      body: [
        '美巡赛联邦快递杯秋季系列赛周四在密西西比杰克逊乡村俱乐部正式打响，首轮赛况异常胶着。',
        '切森·哈德利与博·霍斯勒在早场比赛中双双斩获66杆（低于标准杆6杆），凭借精准的铁杆发挥并列会所领先榜首位。',
        '卫冕冠军俞俊安发挥稳健，全天抓下4只小鸟且未吞柏忌，以68杆（-4）位列前茅，同组的休斯与格里略均交出69杆。',
      ],
    },
    ja: {
      title: 'サンダーソン・ファームズ選手権：ハドリーとホスラーが首位発進、ケビン・ユーは68で好発進',
      subtitle: 'ミシシッピでフェデックスカップ秋季シリーズが開幕。ディフェンディング王者が4アンダーで追走。',
      excerpt: 'チェッソン・ハドリーとボー・ホスラーが6アンダー66で初日首位タイに立った。',
      body: [
        'PGAツアーのシード権争いが本格化する中、ジャクソンでサンダーソン・ファームズ選手権の第1ラウンドがスタートしました。',
        'ハドリーとホスラーの2名がバーディラッシュを見せ、6アンダーの66をマークしてクラブハウスリーダーとなりました。',
        '連覇を目指す台湾のケビン・ユーはノーボギーの68（4アンダー）でホールアウトし、首位と2打差の好位置につけています。',
      ],
    },
    ko: {
      title: '샌더슨 팜스 챔피언십: 해들리와 호슬러 1라운드 공동 선두, 케빈 유 68타 순항',
      subtitle: '미시시피 잭슨 컨트리 클럽서 페덱스컵 가을 시리즈 개막. 디펜딩 챔피언 4언더파 출발.',
      excerpt: '체슨 해들리와 보 호슬러가 6언더파 66타로 공동 선두에 올랐고, 케빈 유가 4언더파로 추격 중이다.',
      body: [
        '목요일 아침 미시시피주 잭슨 컨트리 클럽에서 PGA 투어 가을 시리즈 첫 대회의 1라운드가 순조롭게 시작되었습니다.',
        '해들리와 호슬러는 버디 7개씩을 낚으며 나란히 6언더파 66타를 적어내 공동 선두로 클럽하우스에 복귀했습니다.',
        '지난 대회 우승자 케빈 유는 보기 없이 버디만 4개를 잡는 깔끔한 플레이로 68타(-4)를 기록하며 타이틀 방어를 향한 첫 단추를 잘 꿰었습니다.',
      ],
    },
    ar: {
      title: 'بطولة ساندرسون فارمز: هادلي وهوسلر يتشاركان صدارة الجولة الأولى وكيفن يو يبدأ بقوة',
      subtitle: 'انطلاق موسم الخريف لجولة بي جيه إيه في مسيسيبي وحامل اللقب يسجل 68 ضربة (-4).',
      excerpt: 'شيسون هادلي وبو هوسلر يسجلان 66 ضربة (-6) ليتصدرا بطولة ساندرسون فارمز في جاكسون.',
      body: [
        'بدأت منافسات بطولة ساندرسون فارمز صباح الخميس في كانتري كلوب أوف جاكسون وسط أجواء خريفية مشجعة لتسجيل نتائج مميزة.',
        'وسجل الثنائي شيسون هادلي وبو هوسلر 66 ضربة بواقع 6 ضربات تحت المعدل ليتقاسما صدارة اليوم الأول.',
        'وقدم حامل اللقب كيفن يو أداء ثابتا بتسجيله 68 ضربة (-4) دون ارتكاب أي خطأ، ليبقى على مقربة من المتصدرين.',
      ],
    },
  },
  'f1-singapore-gp-thursday-track-walk-2026': {
    fr: {
      title: 'Grand Prix de Singapour : les projecteurs s’allument à Marina Bay pour la visite de piste du jeudi',
      subtitle: 'Les pilotes inspectent les 19 virages du tracé urbain avant les essais libres de vendredi sous une forte chaleur.',
      excerpt: 'Kimi Antonelli mène Mercedes lors des reconnaissances de piste à Singapour alors que Ferrari et McLaren affûtent leurs armes.',
      body: [
        'La nuit singapourienne s’est illuminée jeudi soir alors que 1 600 projecteurs baignaient le circuit de Marina Bay d’une lumière éclatante.',
        'Solide leader du championnat avec 88 points d’avance sur George Russell, le jeune Kimi Antonelli a arpenté le tracé de 4,94 km pour analyser les zones de freinage rénovées.',
        'Ferrari et McLaren ont dévoilé des évolutions aérodynamiques à fort appui pour tenter de bousculer les Flèches d’Argent dès les premiers essais libres de vendredi.',
      ],
    },
    es: {
      title: 'Gran Premio de Singapur: Marina Bay enciende sus focos para la inspección de pista del jueves',
      subtitle: 'Los pilotos reconocen los 19 giros del circuito urbano antes de los entrenamientos libres del viernes.',
      excerpt: 'Kimi Antonelli lidera a Mercedes en Marina Bay mientras Ferrari y McLaren presentan mejoras aerodinámicas.',
      body: [
        'La icónica carrera nocturna de Singapur comenzó a tomar color este jueves con el encendido de los 1.600 proyectores en Marina Bay.',
        'Kimi Antonelli, líder del Mundial con 317 puntos y 88 de ventaja sobre Russell, completó la caminata técnica examinando el nuevo asfalto.',
        'Ferrari y McLaren confían en sus paquetes de alta carga aerodinámica para desafiar el dominio de Mercedes a partir de las prácticas libres del viernes.',
      ],
    },
    de: {
      title: 'Großer Preis von Singapur: Flutlicht erhellt Marina Bay beim Track Walk am Donnerstag',
      subtitle: 'Fahrer und Ingenieure nehmen die 19 Kurven des Stadtkurses vor den Freien Trainings am Freitag unter die Lupe.',
      excerpt: 'Kimi Antonelli führt Mercedes beim Track Walk in Singapur an, während Ferrari und McLaren Upgrades präsentieren.',
      body: [
        'Am Donnerstagabend erstrahlte der Marina Bay Street Circuit in Singapur im Glanz von 1.600 Flutlichtmasten für das bevorstehende Nachtrennen.',
        'WM-Spitzenreiter Kimi Antonelli ging den 4,94 Kilometer langen Kurs aufmerksam ab, um die Bodenwellen und neuen Asphaltabschnitte zu studieren.',
        'Mit speziellen High-Downforce-Konfigurationen wollen Ferrari und McLaren den Silberpfeilen ab Freitag die Stirn bieten.',
      ],
    },
    it: {
      title: 'Gran Premio di Singapore: i riflettori si accendono a Marina Bay per il track walk del giovedì',
      subtitle: 'I piloti analizzano le 19 curve del circuito cittadino prima delle prove libere del venerdì.',
      excerpt: 'Kimi Antonelli guida la Mercedes nell’ispezione della pista a Singapore mentre Ferrari e McLaren preparano novità.',
      body: [
        'I 1.600 fari di Marina Bay hanno illuminato giovedì sera il lungomare di Singapore in vista della spettacolare gara notturna.',
        'Il leader del mondiale Kimi Antonelli ha completato il tradizionale giro a piedi della pista insieme agli ingegneri per verificare il nuovo asfalto.',
        'Ferrari e McLaren puntano sui pacchetti ad alto carico per insidiare la Mercedes nelle curve lente del tracciato asiatico.',
      ],
    },
    pl: {
      title: 'Grand Prix Singapuru: Reflektory oświetlają Marina Bay przed piątkowymi treningami',
      subtitle: 'Kierowcy sprawdzają 19 zakrętów ulicznego toru podczas czwartkowego obchodu trasy.',
      excerpt: 'Kimi Antonelli z Mercedesa bada nawierzchnię w Singapurze, a rywale szykują pakiety aerodynamiczne.',
      body: [
        'W czwartkowy wieczór Marina Bay rozbłysła światłem 1600 projektorów, inaugurując przygotowania do słynnego nocnego wyścigu F1.',
        'Lider klasyfikacji Kimi Antonelli z przewagą 88 punktów nad Russellem dokładnie przeanalizował z inżynierami strefy dohamowań.',
        'Ferrari i McLaren zaprezentowały zmodyfikowane pakiety o wysokim docisku, licząc na zniwelowanie przewagi Mercedesa na wąskich ulicach Singapuru.',
      ],
    },
    zh: {
      title: 'F1新加坡大奖赛：滨海湾灯火通明，安东内利领衔周四赛道漫步',
      subtitle: '车手实地勘测19个弯角与全新路面，法拉利与迈凯伦高下压力套件周五见真章。',
      excerpt: '1600盏泛光灯点亮新加坡滨海湾，领跑积分榜的安东内利与车队完成周四赛道视察。',
      body: [
        '周四傍晚，1600盏泛光投光灯将4.94公里的滨海湾街区赛道照亮如白昼，拉开新加坡大奖赛的序幕。',
        '手握88分领跑优势的梅赛德斯年轻领军人安东内利与工程师一同走过赛道，重点考察了7号与14号弯的重新铺设路段。',
        '法拉利与迈凯伦本站均带来了升级版的高下压力底板与翼片，力求在周五自由练习赛中向银箭发起强力冲击。',
      ],
    },
    ja: {
      title: 'F1シンガポールGP：マリーナ・ベイの照明が点灯、アントネッリらが木曜トラックウォークを実施',
      subtitle: '過酷な19のコーナーを入念にチェック。金曜フリー走行に向けてフェラーリとマクラーレンが改良型を投入。',
      excerpt: '1600基の投光器に照らされたマリーナ・ベイで、ポイント首位のアントネッリがトラックウォークを完了。',
      body: [
        '木曜夜、シンガポールのウォーターフロントに設置された1600基の照明が一斉に点灯し、マリーナ・ベイ市街地コースが夜空に浮かび上がりました。',
        '選手権首位に立つ19歳のアントネッリはエンジニア陣とともにコースを歩き、再舗装された路面グリップの状態を入念に確認しました。',
        '低中速コーナーが連続するこのサーキットで、フェラーリとマクラーレンは高ダウンフォース仕様を投入しメルセデス撃破を目指します。',
      ],
    },
    ko: {
      title: 'F1 싱가포르 GP: 마리나 베이 조명 점등, 안토넬리 목요일 트랙 워크 완료',
      subtitle: '19개 코너 시가지 서킷 점검 완료. 금요일 연습 주행 앞두고 페라리와 맥라렌 다운포스 강화.',
      excerpt: '1,600개의 조명이 켜진 싱가포르에서 키미 안토넬리가 트랙을 점검하며 주말 야간 레이스 준비에 돌입했다.',
      body: [
        '목요일 저녁 싱가포르 마리나 베이 서킷에 1,600개의 투광 조명이 켜지며 아시아 최고 야간 레이스의 서막이 올랐습니다.',
        '챔피언십 88점 차 선두를 달리는 메르세데스의 키미 안토넬리는 레이스 엔지니어와 함께 4.94km 코스를 걸으며 노면 상태를 점검했습니다.',
        '페라리와 맥라렌은 19개 코너에 최적화된 고다운포스 에어로 패키지를 준비하고 금요일 자유 연습 세션부터 메르세데스 공략에 나섭니다.',
      ],
    },
    ar: {
      title: 'جائزة سنغافورة الكبرى: أضواء مارينا باي تسطع مع جولة المشي التمهيدية ليوم الخميس',
      subtitle: 'السائقون يفحصون المنعطفات التسعة عشر وسط حرارة استوائية قبل التجارب الحرة يوم الجمعة.',
      excerpt: 'كيمي أنتونيللي يقود مرسيدس في جولة تفقد الحلبة تحت 1600 كشاف إضاءة في سنغافورة.',
      body: [
        'أضاءت حلبة مارينا باي في سنغافورة مساء الخميس مع تشغيل 1600 كشاف إضاءة استعدادا للسباق الليلي المرتقب.',
        'تفقد متصدر البطولة كيمي أنتونيللي المسار البالغ طوله 4.94 كم برفقة مهندسيه للوقوف على التعديلات في الإسفلت ونقاط الكبح.',
        'وكشفت فرق فيراري وماكلارين عن حزم ديناميكية هوائية ذات ارتكازية عالية لمنافسة مرسيدس بدءا من تجارب الجمعة الحرة.',
      ],
    },
  },
  'aston-villa-1-0-bayern-duran-historic-ucl-2026': {
    fr: {
      title: "Aston Villa 1-0 Bayern Munich : le lob sensationnel de Duran fait revivre la gloire de 1982",
      subtitle: "Le joker colombien trompe Manuel Neuer d'un lob de 30 mètres à la 79e minute et enflamme Villa Park.",
      excerpt: "Quarante-deux ans après Rotterdam, Aston Villa a terrassé le Bayern Munich 1-0 en Ligue des champions grâce à un coup de génie de Jhon Duran.",
      body: [
        "Quarante-deux ans après le sacre historique de Rotterdam, Villa Park a vibré au rythme d'une soirée européenne légendaire. Aston Villa a fait tomber le Bayern Munich 1-0, mettant un terme à une série de 41 matches sans défaite des Bavarois en phase de groupes.",
        "Unai Emery a dressé un piège tactique remarquable face à la formation de Vincent Kompany. Malgré la pression offensive de Kane et Musiala, Emiliano Martinez s'est montré infranchissable dans ses cages avec sept parades décisives.",
        "Le coup de foudre est survenu à la 79e minute : lancé par Pau Torres, Jhon Duran a vu Manuel Neuer trop avancé et a déclenché un lob splendide de 30 mètres sans contrôle pour faire chavirer Birmingham.",
      ],
    },
    es: {
      title: "Aston Villa 1-0 Bayern Múnich: la vaselina de Durán revive la gloria de 1982 en una noche mágica",
      subtitle: "El delantero colombiano sorprende a Manuel Neuer desde 30 metros en el minuto 79 para desatar la euforia en Villa Park.",
      excerpt: "Cuarenta y dos años después de Róterdam, el Aston Villa sorprendió al Bayern Múnich 1-0 con una genialidad inolvidable de Jhon Durán.",
      body: [
        "Cuarenta y dos años después del histórico gol de Peter Withe en Róterdam, Villa Park presenció otra gesta inolvidable. El Aston Villa derrotó 1-0 al Bayern Múnich en la segunda jornada de la Champions League, cortando una racha bávara de 41 partidos invictos en fase de grupos.",
        "El planteamiento de Unai Emery contuvo el poderío ofensivo de Kane y Musiala. El guardameta Emiliano Martínez brilló con siete intervenciones salvadoras bajo los tres palos.",
        "En el minuto 79 llegó el instante definitivo: tras un pase largo de Pau Torres, Jhon Durán vio a Neuer adelantado y sacó una vaselina perfecta con la zurda desde 30 metros para firmar una noche dorada.",
      ],
    },
    de: {
      title: "Aston Villa 1:0 Bayern München: Durán-Traumtor wiederholt den Triumph von 1982",
      subtitle: "Kolumbianischer Joker überlupft Manuel Neuer aus 27 Metern in der 79. Minute und bringt den Villa Park zum Kochen.",
      excerpt: "42 Jahre nach dem Europapokal-Triumph von Rotterdam schlägt Aston Villa den FC Bayern mit 1:0 durch einen Geniestreich von Jhon Durán.",
      body: [
        "42 Jahre nach dem historischen Finalsieg von Rotterdam feierte der Villa Park einen magischen Europapokal-Abend. Aston Villa bezwang den FC Bayern München mit 1:0 und beendete die Serie der Bayern von 41 ungeschlagenen Gruppenspielen.",
        "Unai Emery stellte seine Mannschaft taktisch perfekt ein. Emiliano Martínez hielt mit sieben herausragenden Paraden die Null gegen die Offensivkraft um Harry Kane und Jamal Musiala.",
        "In der 79. Minute folgte der Paukenschlag: Jhon Durán sah Manuel Neuer weit vor seinem Kasten und hob den Ball aus knapp 30 Metern über den Nationaltorwart ins Netz zum umjubelten Sieg.",
      ],
    },
    it: {
      title: "Aston Villa 1-0 Bayern Monaco: il pallonetto di Durán fa rivivere il trionfo del 1982 a Villa Park",
      subtitle: "Il subentrato colombiano beffa Neuer da 30 metri al minuto 79 e regala ai Villans una notte memorabile.",
      excerpt: "Quarantadue anni dopo Rotterdam, l'Aston Villa batte il Bayern Monaco 1-0 grazie a una prodezza di Jhon Durán in Champions League.",
      body: [
        "Quarantadue anni dopo la finale di Rotterdam del 1982, Villa Park ha vissuto un'altra notte di pura leggenda europea. L'Aston Villa ha superato 1-0 il Bayern Monaco, interrompendo una striscia bavarese di 41 partite senza sconfitte nei gironi.",
        "Unai Emery ha allestito un piano tattico impeccabile. Emiliano Martínez è stato determinante con sette parate prodigiose a difesa del risultato contro Kane e compagni.",
        "Al 79' l'apoteosi: imbeccato da Pau Torres, Jhon Durán ha visto Neuer fuori dai pali e ha calciato un pallonetto morbido di prima intenzione che ha fatto esplodere di gioia il popolo di Birmingham.",
      ],
    },
    pl: {
      title: "Aston Villa 1-0 Bayern Monachium: cudowny lob Durana powtarza chwałę z 1982 roku",
      subtitle: "Kolumbijski rezerwowy przelobował Manuela Neuera z 30 metrów w 79. minucie na wypełnionym Villa Park.",
      excerpt: "Czterdzieści dwa lata po finale w Rotterdamie Aston Villa sensacyjnie pokonała Bayern Monachium 1-0 po kapitalnym uderzeniu Jhona Durana.",
      body: [
        "Czterdzieści dwa lata po triumfie w Rotterdamie kibice na Villa Park przeżyli kolejną historyczną noc. Aston Villa pokonała Bayern Monachium 1-0, przerywając passę 41 meczów Bawarczyków bez porażki w fazie grupowej Ligi Mistrzów.",
        "Zespół Unaia Emery'ego zagrał z niezwykłą dojrzałością taktyczną. Emiliano Martinez był niezrównany w bramce, broniąc siedem groźnych strzałów rywali.",
        "W 79. minucie Jhon Duran zauważył wysuniętego Neuera i uderzeniem z pierwszej piłki z 30 metrów posłał piłkę ponad niemieckim bramkarzem prosto do siatki.",
      ],
    },
    zh: {
      title: "阿斯顿维拉 1-0 拜仁慕尼黑：杜兰天外飞仙吊射重现1982欧冠决战荣耀",
      subtitle: "哥伦比亚超级替补第79分钟30米外吊射击溃诺伊尔，维拉公园球场陷入狂欢",
      excerpt: "时隔42年重演鹿特丹决赛经典，阿斯顿维拉凭借杜兰的世界波1-0力克拜仁慕尼黑，打破德甲巨人欧冠小组赛41场不败纪录。",
      body: [
        "时隔42年，维拉公园球场再现了1982年欧洲冠军杯决赛的荣耀时刻。阿斯顿维拉在欧冠第2轮主场1-0力克拜仁慕尼黑，终结了对手在欧冠小组赛阶段保持的41场不败神话。",
        "埃梅里布置了极具针对性的防守反击战术。门将达米安·马丁内斯高接抵挡完成7次扑救，力保球门不失。",
        "比赛第79分钟，替补登场的哥伦比亚前锋杜兰接保·托雷斯后场长传，果断在30米开外起左脚凌空吊射，皮球划出绝美弧线越过诺伊尔头顶坠入球网，引爆全场欢腾。",
      ],
    },
    ja: {
      title: "アストン・ヴィラ 1-0 バイエルン：デュランの芸術的ループ弾が1982年の栄光を再現",
      subtitle: "途中出場のコロンビア代表FWが79分にノイアーの頭上を抜く30mロングシュートを沈めてヴィラ・パーク熱狂",
      excerpt: "42年前のロッテルダム決勝のスコアがヴィラ・パークで再現。アストン・ヴィラがデュランの劇的弾でバイエルンを1-0で破る。",
      body: [
        "1982年のチャンピオンズカップ決勝から42年、ヴィラ・パークが欧州の熱狂に包まれました。アストン・ヴィラはバイエルン・ミュンヘンを1-0で下し、相手のグループステージ41戦無敗記録をストップさせました。",
        "エメリ監督の統率された守備陣とGKエミリアーノ・マルティネスが奮闘し、ケインやムシアラを擁するバイエルンの猛攻を7本の好セーブで完封しました。",
        "勝負を決めたのは79分でした。交代出場のジョン・デュランが前に出ていたノイアーの位置を見逃さず、約30mの距離からダイレクトでループシュートを放ち、見事にゴール右隅へ流し込みました。",
      ],
    },
    ko: {
      title: "아스톤 빌라 1-0 바이에른 뮌헨: 두란의 환상적인 로빙 결승골, 1982년 신화 재현",
      subtitle: "콜롬비아 특급 조커 후반 79분 노이어 키 넘기는 30m 원더골 작렬, 빌라 파크 열광",
      excerpt: "42년 전 로테르담의 기적을 완벽 재현했다. 아스톤 빌라가 존 두란의 환상골로 바이에른 뮌헨의 41경기 챔피언스리그 무패 행진을 저지했다.",
      body: [
        "1982년 유러피언컵 결승전의 감동이 42년 만에 빌라 파크에서 그대로 재현되었습니다. 아스톤 빌라는 바이에른 뮌헨을 1-0으로 꺾고 뮌헨의 챔피언스리그 조별리그 41경기 무패 기록을 멈춰 세웠습니다.",
        "에메리 감독의 완벽한 수비 전술과 골키퍼 에밀리아노 마르티네스의 7차례 신들린 선방 쇼가 해리 케인과 무시알라의 파상 공세를 완벽히 막아냈습니다.",
        "후반 79분 교체 투입된 존 두란이 토레스의 롱패스를 받아 앞으로 나온 마누엘 노이어의 위치를 포착하고 30m 거리에서 지체 없이 왼발 감아차기 로빙슛을 성공시키며 승부를 결정지었습니다.",
      ],
    },
    ar: {
      title: "أستون فيلا 1-0 بايرن ميونخ: تسديدة دوران الساحرة تكرر أمجاد 1982 في ليلة تاريخية",
      subtitle: "المهاجم الكولومبي البديل يباغت مانويل نوير بكرة ساقطة من 30 مترا في الدقيقة 79 ويشعل مدرجات فيلا بارك.",
      excerpt: "بعد مرور 42 عاما على نهائي روتردام، أستون فيلا يصعق بايرن ميونخ 1-0 في دوري أبطال أوروبا بفضل هدف عبقري من جون دوران.",
      body: [
        "بعد 42 عاما من معجزة روتردام التاريخية، شهد ملعب فيلا بارك ملحمة كروية لا تنسى. حقق أستون فيلا فوزا ثمينا على بايرن ميونخ بنتيجة 1-0، لينهي سلسلة من 41 مباراة دون هزيمة للعملاق البافاري في دور المجموعات.",
        "أدار أوناي إيمري المباراة بحنكة تكتيكية عالية، وتألق الحارس إيميليانو مارتينيز بصورة استثنائية ليتصدى لسبع كرات خطيرة حرمت كين ورفاقه من التسجيل.",
        "وفي الدقيقة 79 جاءت اللحظة الساحرة: استغل البديل جون دوران تمريرة طولية ورأى الحارس مانويل نوير متقدما عن مرماه، ليرسل كرة ساقطة مذهلة من 30 مترا استقرت في الشباك وسط احتفالات هيستيرية في برمنغهام.",
      ],
    },
  },
  'nfl-week4-tnf-49ers-edge-rams-24-20-2026': {
    fr: {
      title: "49ers 24-20 Rams : un arrêt héroïque sur la ligne scelle le choc du jeudi soir",
      subtitle: "Brock Purdy lance deux passes de touchdown et la défense repousse Matthew Stafford à quelques secondes du terme.",
      excerpt: "San Francisco s'installe seul en tête de la NFC Ouest après avoir résisté à la dernière offensive des Rams pour l'emporter 24-20.",
      body: [
        "Le Thursday Night Football a tenu toutes ses promesses au Levi's Stadium où les 49ers de San Francisco ont battu les Rams de Los Angeles 24-20 au terme d'une fin de match étouffante.",
        "Brock Purdy a maîtrisé les débats avec 254 yards et deux touchdowns pour Deebo Samuel et George Kittle. Au début du quatrième quart-temps, Christian McCaffrey a franchi la ligne d'en-but pour donner un avantage précieux aux Niners.",
        "Menés de quatre points, les Rams de Matthew Stafford ont atteint la ligne des 7 yards adverses à 42 secondes du terme. Mais la défense californienne a tenu bon sur quatrième tentative, repoussant l'ultime passe pour sceller la victoire.",
      ],
    },
    es: {
      title: "49ers 24-20 Rams: una frenada en la yarda de gol sella un vibrante Thursday Night Football",
      subtitle: "Brock Purdy lanza dos pases de anotación y la defensa detiene a Matthew Stafford en los instantes finales.",
      excerpt: "San Francisco se apodera del liderato en solitario del Oeste de la NFC tras imponerse 24-20 a los Rams en Santa Clara.",
      body: [
        "El Thursday Night Football de la Semana 4 regaló una batalla memorable en el Levi's Stadium. Los San Francisco 49ers vencieron 24-20 a Los Angeles Rams para quedarse en la cima divisional.",
        "Brock Purdy completó 19 de 26 pases para 254 yardas y dos touchdowns hacia Deebo Samuel y George Kittle. En el último cuarto, Christian McCaffrey anotó con una carrera de cuatro yardas.",
        "Matthew Stafford orquestó una serie ofensiva final que llegó hasta la yarda 7 de San Francisco con 42 segundos en el reloj, pero la secundaria de los 49ers desvió el pase en cuarto intento para sellar el triunfo.",
      ],
    },
    de: {
      title: "49ers 24:20 Rams: Goal-Line-Stop sichert dramatischen Thursday-Night-Krimi in Santa Clara",
      subtitle: "Brock Purdy wirft zwei Touchdowns und die Defense stoppt Matthew Stafford kurz vor Schluss an der 7-Yard-Linie.",
      excerpt: "San Francisco übernimmt die alleinige Führung in der NFC West nach einem 24:20-Erfolg über die Los Angeles Rams.",
      body: [
        "Thursday Night Football bot im Levi's Stadium ein mitreißendes Divisionsduell, in dem die San Francisco 49ers die Los Angeles Rams mit 24:20 niederringen konnten.",
        "Quarterback Brock Purdy glänzte mit 254 Yards und zwei Touchdowns auf Deebo Samuel und George Kittle. Im Schlussviertel erzielte Christian McCaffrey den entscheidenden Touchdown-Lauf zur Führung.",
        "Stafford führte die Rams in den Schlusssekunden bis an die 7-Yard-Linie, doch die 49ers-Verteidigung wehrte den vierten Versuch ab und sicherte den 3-1-Saisonstart.",
      ],
    },
    it: {
      title: "49ers 24-20 Rams: la difesa salva sulla linea di meta nel finale al cardiopalma del giovedì",
      subtitle: "Brock Purdy lancia due touchdown e la retroguardia respinge Stafford a 42 secondi dal termine a Santa Clara.",
      excerpt: "San Francisco vola in vetta solitaria alla NFC West superando 24-20 i Los Angeles Rams al Levi's Stadium.",
      body: [
        "Il Thursday Night Football ha regalato un grande spettacolo a Santa Clara con il successo dei San Francisco 49ers per 24-20 sui Los Angeles Rams.",
        "Brock Purdy ha orchestrato l'attacco con precisione, totalizzando 254 yard e due passaggi da touchdown per Deebo Samuel e George Kittle, prima del sigillo di McCaffrey su corsa.",
        "Nel finale i Rams sono arrivati a un passo dal colpaccio sulla linea delle 7 yard, ma il quarto down difensivo dei 49ers ha sbarrato la porta alla rimonta di Stafford.",
      ],
    },
    pl: {
      title: "49ers 24-20 Rams: obrona na linii punktowej pieczętuje triumf w Thursday Night Football",
      subtitle: "Brock Purdy rzuca dwa przyłożenia, a defensywa zatrzymuje Matthew Stafforda na 42 sekundy przed końcem.",
      excerpt: "San Francisco 49ers obejmują samodzielne prowadzenie w dywizji NFC West po wygranej 24-20 nad Los Angeles Rams.",
      body: [
        "Czwartkowy mecz otwarcia 4. kolejki NFL na Levi's Stadium przyniósł wielkie emocje. San Francisco 49ers pokonali Los Angeles Rams 24-20 w zaciętym starciu dywizyjnym.",
        "Brock Purdy rozegrał znakomite zawody, notując 254 jardy i dwa podania na przyłożenia do Samuela i Kittle'a, a Christian McCaffrey zdobył decydujące punkty po ziemi w czwartej kwarcie.",
        "W dramatycznej końcówce Rams dotarli pod samą linię punktową 49ers, jednak obrona gospodarzy zablokowała podanie Stafforda przy czwartej próbie i przypieczętowała zwycięstwo.",
      ],
    },
    zh: {
      title: "49人 24-20 公羊：门线终极防守锁定周四夜赛胜利，旧金山领跑国联西区",
      subtitle: "普尔迪送出两次达阵传球，49人防守组在最后42秒挡住斯塔福德第4档传球",
      excerpt: "在旧金山主场进行的周四夜赛中，49人以24-20力克洛杉矶公羊，战绩升至3胜1负独占国联西区头名。",
      body: [
        "第4周NFL周四夜赛在李维斯体育场上演惊心动魄的同区德比，旧金山49人以24-20击败洛杉矶公羊，占据国联西区领跑地位。",
        "四分卫布洛克·普尔迪表现稳健，26传19中贡献254码，先后助攻萨缪尔和基特尔完成达阵。第四节初，麦卡弗里4码冲球达阵奠定胜局。",
        "公羊队在斯塔福德带领下展开绝地反击，在比赛仅剩42秒时推进至49人7码线。关键的第4档传球被49人角卫防守破坏，成功捍卫了主场胜利。",
      ],
    },
    ja: {
      title: "49ers 24-20 ラムズ：ゴール前劇的ストップでサースデーナイト白星、地区単独首位へ",
      subtitle: "パーディーが2TDパスを決め、マカフリーの決勝TDの後に守備陣がスタッフォードの猛追を阻止",
      excerpt: "サンフランシスコ・49ersが残り42秒のゴール前第4ダウンを守り抜き、ロサンゼルス・ラムズを24-20で下してNFC西地区首位に浮上。",
      body: [
        "リーバイス・スタジアムで行われたNFL第4週のサースデーナイト・フットボールで、49ersが宿敵ラムズを24-20で退けました。",
        "ブロック・パーディーが254ヤードと2本のタッチダウンパスを記録し、第4クォーターにはマカフリーが4ヤードの勝ち越しランTDを奪いました。",
        "終盤にラムズのスタッフォードが敵陣7ヤードまで迫りましたが、49ers守備陣が第4ダウンパスを叩き落として逃げ切り、今季3勝1敗としました。",
      ],
    },
    ko: {
      title: "49ers 24-20 램스: 종료 직전 골라인 스톱으로 서스데이 나이트 짜릿한 승리",
      subtitle: "브록 퍼디 터치다운 패스 2개, 매카프리 결승 러싱 TD로 NFC 서부 단독 선두 등극",
      excerpt: "샌프란시스코 49ers가 종료 42초를 남기고 4th 다운 수비에 성공하며 LA 램스를 24-20으로 제압했다.",
      body: [
        "리바이스 스타디움에서 열린 NFL 4주차 목요일 밤 경기에서 샌프란시스코 49ers가 LA 램스를 24-20으로 꺾고 NFC 서부지구 단독 1위에 올랐습니다.",
        "쿼터백 브록 퍼디는 254패싱야드와 터치다운 2개를 기록하며 공격을 이끌었고, 4쿼터에는 크리스천 매카프리가 4야드 러싱 터치다운을 터뜨렸습니다.",
        "경기 종료 42초 전 램스가 7야드까지 전진하며 역전을 노렸으나, 49ers 수비진이 스태퍼드의 4th 다운 패스를 완벽히 쳐내며 3승 1패를 확정지었습니다.",
      ],
    },
    ar: {
      title: "فورتي ناينرز 24-20 رامز: صمود دفاعي أخير على خط الهدف يحسم قمة الخميس الكروية",
      subtitle: "بروك بيردي يمرر كرتي هبوط وكريستيان ماكافري يسجل الحسم قبل إيقاف هجمة ستافورد الأخيرة.",
      excerpt: "سان فرانسيسكو ينفرد بصدارة مجموعة الغرب في NFL بعد تغلبه المثير على لوس أنجلوس رامز 24-20 في سانتا كلارا.",
      body: [
        "شهد ملعب ليفايس إثارة بالغة في افتتاح الجولة الرابعة من دوري كرة القدم الأمريكية NFL، حيث تغلب سان فرانسيسكو 49ers على لوس أنجلوس رامز 24-20.",
        "قاد بروك بيردي الهجوم ببراعة محققا 254 ياردة وتمريرتي هبوط إلى صامويل وكيتل، قبل أن يسجل كريستيان ماكافري هدف التقدم الحاسم في الربع الأخير.",
        "وفي اللحظات الأخيرة، كاد ماثيو ستافورد أن يقلب النتيجة بوصوله إلى خط 7 ياردات، لكن الدفاع تصدى للكرة في المحاولة الرابعة قبل 42 ثانية من النهاية.",
      ],
    },
  },
  'wnba-semifinals-preview-fever-lynx-aces-liberty-2026': {
    fr: {
      title: "Demi-finales WNBA : Lynx-Fever et Aces-Liberty pour un dernier carré d'anthologie",
      subtitle: "Des balayages historiques au premier tour ouvrent la voie à Caitlin Clark et A'ja Wilson dès dimanche.",
      excerpt: "Après quatre séries bouclées en deux matches, les demi-finales WNBA opposent Minnesota à Indiana et New York à Las Vegas.",
      body: [
        "Pour la première fois de l'histoire de la WNBA, le premier tour s'est achevé par quatre balayages 2-0. Le dernier carré réunit les plus grandes vedettes de la ligue dès dimanche.",
        "Au Target Center, les Minnesota Lynx accueilleront les Indiana Fever de Caitlin Clark. Cheryl Reeve tentera de museler la meneuse vedette tout en s'appuyant sur Napheesa Collier.",
        "À Brooklyn, le Barclays Center vibrera pour la revanche des Finales 2023 entre le New York Liberty et les Las Vegas Aces d'A'ja Wilson dans une série au meilleur des cinq manches.",
      ],
    },
    es: {
      title: "Semifinales de la WNBA: Lynx-Fever y Aces-Liberty prometen un espectáculo colosal",
      subtitle: "Barridas históricas en la primera ronda dan paso a los duelos de Caitlin Clark y A'ja Wilson desde el domingo.",
      excerpt: "Las semifinales de la WNBA al mejor de cinco partidos enfrentarán a Minnesota contra Indiana y a Nueva York contra Las Vegas.",
      body: [
        "Por primera vez en la historia de la WNBA, las cuatro series de primera ronda se definieron por barridas de 2-0, configurando un cuadro de semifinales de ensueño.",
        "En Mineápolis, las Minnesota Lynx de Napheesa Collier se medirán al fenómeno de Caitlin Clark y las Indiana Fever, que llegan con un ritmo ofensivo arrollador.",
        "En Nueva York, el Liberty y las Aces de Las Vegas reeditarán su histórica rivalidad con Breanna Stewart y A'ja Wilson frente a frente en una eliminatoria apasionante.",
      ],
    },
    de: {
      title: "WNBA-Halbfinale steht: Lynx-Fever und Aces-Liberty versprechen Playoff-Feuerwerk am Sonntag",
      subtitle: "Historische Sweeps in Runde 1 ebnen den Weg für Caitlin Clark und A'ja Wilson im Final Four.",
      excerpt: "Nach vier klaren 2:0-Seriensiegen starten die WNBA-Halbfinalserien am Sonntag mit Minnesota gegen Indiana und New York gegen Las Vegas.",
      body: [
        "Erstmals in der WNBA-Geschichte endeten alle Erstrundenserien mit 2:0-Sweeps. Damit steht ein spektakuläres Halbfeld fest, das am Sonntag in die Best-of-Five-Serien startet.",
        "Die topgesetzten Minnesota Lynx um Defensiv-Star Napheesa Collier empfangen Caitlin Clark und die aufstrebenden Indiana Fever im Target Center.",
        "Im Barclays Center kommt es zur Neuauflage der Finals von 2023 zwischen den New York Liberty und den Las Vegas Aces um Dreifach-MVP A'ja Wilson.",
      ],
    },
    it: {
      title: "Semifinali WNBA: Lynx-Fever e Aces-Liberty accendono una domenica di grandi sfide",
      subtitle: "Quattro cappotti al primo turno spianano la strada allo scontro tra Caitlin Clark e A'ja Wilson.",
      excerpt: "Al via domenica le semifinali WNBA al meglio delle cinque gare: Minnesota affronta Indiana e New York ritrova Las Vegas.",
      body: [
        "Per la prima volta nella storia della WNBA, tutte le serie del primo turno si sono concluse con un secco 2-0, proiettando le quattro migliori squadre in semifinale.",
        "Al Target Center, le Minnesota Lynx sfideranno le Indiana Fever guidate dal talento travolgente di Caitlin Clark e Aliyah Boston.",
        "A Brooklyn, le campionesse in carica di Las Vegas guidate da A'ja Wilson affronteranno il New York Liberty di Breanna Stewart e Sabrina Ionescu.",
      ],
    },
    pl: {
      title: "Półfinały WNBA: Lynx kontra Fever oraz Aces z Liberty w starciu gigantów od niedzieli",
      subtitle: "Historyczne czyste serie otwierają drogę do wielkich pojedynków Caitlin Clark i A'ja Wilson.",
      excerpt: "W półfinałach WNBA do trzech zwycięstw Minnesota zagra z Indianą, a Nowy Jork spotka się z Las Vegas.",
      body: [
        "Pierwsza runda play-off WNBA przeszła do historii dzięki czterem zwycięstwom 2-0. Od niedzieli ruszają serie półfinałowe w formacie do trzech wygranych.",
        "W Minneapolis Minnesota Lynx zmierzy się z rewelacją sezonu Indiana Fever prowadzoną przez Caitlin Clark.",
        "W Nowym Jorku dojdzie do rewanżu za finał z 2023 roku pomiędzy New York Liberty a Las Vegas Aces z potężną A'ja Wilson.",
      ],
    },
    zh: {
      title: "WNBA半决赛对阵揭晓：山猫对阵狂热、王牌再战自由人，周日打响天王山",
      subtitle: "首轮四场全横扫创历史，克拉克挑战榜首明尼苏达，阿贾·威尔逊迎战斯图尔特",
      excerpt: "2026年WNBA半决赛五场三胜制系列赛将于周日开打，山猫迎战狂热，自由人再战王牌。",
      body: [
        "WNBA历史上首次出现首轮四轮系列赛全部以2-0横扫告终的盛况，联赛四强以最强姿态会师半决赛。",
        "在标靶中心，常规赛头名明尼苏达山猫队将迎战凯特琳·克拉克领衔的印第安纳狂热队，克拉克将遭遇联盟最强防守考验。",
        "纽约巴克莱中心则将上演2023年总决赛的经典重演，阿贾·威尔逊的卫冕冠军拉斯维加斯王牌客场挑战布里安娜·斯图尔特的纽约自由人。",
      ],
    },
    ja: {
      title: "WNBA準決勝カード確定：リンクス対フィーバー、エranges対リバティが日曜開幕",
      subtitle: "史上初の1回戦全カードスイープ終了、クラークとエイジャ・ウィルソンが頂点目指す",
      excerpt: "5回戦制のWNBA準決勝が日曜日に開幕。首位リンクスとフィーバー、リバティとエrangesが激突。",
      body: [
        "WNBA史上初めて1回戦の全4カードが2-0のスイープで決着し、役者が揃ったベスト4が日曜日から激突します。",
        "ミネソタ・リンクスはターゲット・センターでケイトリン・クラーク率いるインディアナ・フィーバーを迎え撃ちます。",
        "バークレイズ・センターでは2023年ファイナルの再戦となるニューヨーク・リバティ対ラスベガス・エrangesの宿敵対決が火花を散らします。",
      ],
    },
    ko: {
      title: "WNBA 준결승 대진 확정: 링스-피버, 에이스-리버티 일요일 1차전 격돌",
      subtitle: "1라운드 전 시리즈 2-0 스윕 완료, 케이틀린 클라크와 에이자 윌슨의 파이널 도전",
      excerpt: "WNBA 5전 3선승제 준결승이 일요일 개막한다. 미네소타와 인디애나, 뉴욕과 라스베이거스가 격돌한다.",
      body: [
        "WNBA 역사상 최초로 1라운드 4개 시리즈가 모두 2-0 스윕으로 종료되며 최고의 4강 대진이 완성되었습니다.",
        "정규리그 1위 미네소타 링스는 타깃 센터에서 케이틀린 클라크가 이끄는 인디애나 피버와 1차전을 펼칩니다.",
        "뉴욕 바클레이스 센터에서는 2023년 파이널 리매치인 뉴욕 리버티와 에이자 윌슨의 라스베이거스 에이스가 맞붙습니다.",
      ],
    },
    ar: {
      title: "نصف نهائي WNBA: لينكس ضد فيفر وأيسز ضد ليبرتي في معارك نارية تبدأ الأحد",
      subtitle: "اكتساح تاريخي في الدور الأول يمهد الطريق لمواجهات كيتلين كلارك وإيجا ويلسون في المربع الذهبي.",
      excerpt: "تنطلق سلسلة نصف نهائي دوري السلة الأمريكي للسيدات الأحد بمواجهتي مينيسوتا وإنديانا، ونيويورك ولاس فيغاس.",
      body: [
        "للمرة الأولى في تاريخ دوري السلة الأمريكي للسيدات، انتهت جميع سلاسل الدور الأول بانتصارات نظيفة 2-0، لتلتقي أفضل أربعة فرق في نصف النهائي.",
        "يستضيف مينيسوتا لينكس على أرضه فريق إنديانا فيفر بقيادة النجمة الشابة كيتلين كلارك في مواجهة من العيار الثقيل.",
        "وفي بروكلين، يتجدد الصراع التاريخي بين نيويورك ليبرتي ولاس فيغاس أيسز بقيادة إيجا ويلسون في سلسلة من خمس مباريات.",
      ],
    },
  },
  'china-open-2026-alcaraz-sinner-quarterfinal-triumph': {
    fr: {
      title: "China Open 2026 : Alcaraz domine Khachanov et Sinner s'impose face à Lehecka à Pékin",
      subtitle: "Les deux premiers mondiaux s'imposent en deux sets et se rapprochent d'un duel au sommet en finale.",
      excerpt: "Carlos Alcaraz écarte Karen Khachanov 7-5, 6-2 et Jannik Sinner domine Jiri Lehecka 6-2, 7-6 pour rallier le dernier carré à Pékin.",
      body: [
        "La journée de quarts de finale à Pékin a tenu toutes ses promesses avec les victoires autoritaires des deux patrons du circuit mondial.",
        "Carlos Alcaraz a fait étalage de sa puissance face à Karen Khachanov, s'imposant 7-5, 6-2 avec 26 coups gagnants sur le Diamond Court.",
        "De son côté, le numéro un mondial Jannik Sinner a sauvé une balle de set au tie-break pour écarter Jiri Lehecka 6-2, 7-6(6) et enchaîner une 15e victoire consécutive.",
      ],
    },
    es: {
      title: "China Open 2026: Alcaraz arrolla a Khachanov y Sinner resiste ante Lehecka en Pekín",
      subtitle: "Los dos mejores tenistas del mundo avanzan en sets corridos y se acercan a una final soñada.",
      excerpt: "Carlos Alcaraz superó 7-5, 6-2 a Karen Khachanov y Jannik Sinner venció 6-2, 7-6 a Jiri Lehecka para alcanzar las semifinales en Pekín.",
      body: [
        "Los cuartos de final del China Open confirmaron el momento intratable de los dos principales favoritos al título en la capital china.",
        "Carlos Alcaraz desarmó a Karen Khachanov con un tenis agresivo y brillante, sellando un 7-5, 6-2 con 26 tiros ganadores en la pista central.",
        "Jannik Sinner superó momentos de máxima tensión en el segundo set para batir a Jiri Lehecka por 6-2, 7-6(6), firmando su decimoquinta victoria consecutiva en el circuito.",
      ],
    },
    de: {
      title: "China Open 2026: Alcaraz bezwingt Khachanov und Sinner behauptet sich gegen Lehecka in Peking",
      subtitle: "Die beiden Topstars marschieren ohne Satzverlust ins Halbfinale des ATP-500-Turniers.",
      excerpt: "Carlos Alcaraz schlägt Karen Khachanov 7:5, 6:2 und Jannik Sinner ringt Jiri Lehecka 6:2, 7:6 nieder.",
      body: [
        "Am Viertelfinaltag der China Open demonstrierten die beiden weltbesten Spieler einmal mehr ihre Ausnahmestellung auf Hartplatz.",
        "Carlos Alcaraz überzeugte beim 7:5, 6:2 gegen Karen Khachanov mit 26 Gewinnschlägen und dominierte die langen Ballwechsel nach Belieben.",
        "Jannik Sinner wehrte im Tiebreak des zweiten Satzes einen Satzball ab und siegte 6:2, 7:6(6) gegen Jiri Lehecka für seinen 15. Sieg in Serie.",
      ],
    },
    it: {
      title: "China Open 2026: Alcaraz supera Khachanov e Sinner piega Lehecka a Pechino",
      subtitle: "I primi due del ranking mondiale avanzano in due set verso l'attesissima finale al National Tennis Center.",
      excerpt: "Carlos Alcaraz batte 7-5, 6-2 Karen Khachanov e Jannik Sinner supera Jiri Lehecka 6-2, 7-6(6) approdando in semifinale a Pechino.",
      body: [
        "I quarti di finale dell'ATP 500 di Pechino hanno confermato lo straordinario stato di forma dei due dominatori del tennis contemporaneo.",
        "Carlos Alcaraz ha liquidato Karen Khachanov 7-5, 6-2 con una prestazione impeccabile scandita da 26 colpi vincenti.",
        "Jannik Sinner ha dovuto faticare nel secondo set ma ha chiuso 6-2, 7-6(6) contro Jiri Lehecka annullando un set point nel tie-break.",
      ],
    },
    pl: {
      title: "China Open 2026: Alcaraz pokonuje Chaczanowa, a Sinner wygrywa z Lehecką w Pekinie",
      subtitle: "Dwaj najlepsi tenisiści świata awansują w dwóch setach do półfinałów turnieju w stolicy Chin.",
      excerpt: "Carlos Alcaraz wygrał 7-5, 6-2 z Karenem Chaczanowem, a Jannik Sinner pokonał Jiriego Leheckę 6-2, 7-6(6) w Pekinie.",
      body: [
        "Piątkowe ćwierćfinały China Open przyniosły pokaz mistrzowskiej formy liderów światowego rankingu ATP.",
        "Carlos Alcaraz pewnie pokonał Karena Chaczanowa 7-5, 6-2, popisując się 26 uderzeniami kończącymi na korcie Diamond.",
        "Lider rankingu Jannik Sinner obronił piłkę setową w tie-breaku i pokonał Jiriego Leheckę 6-2, 7-6(6), notując 15. wygraną z rzędu.",
      ],
    },
    zh: {
      title: "2026年中网公开赛：阿尔卡拉斯轻取卡恰诺夫，辛纳力克莱赫茨卡跻身四强",
      subtitle: "世界排名前两位巨星直落两盘过关，国家网球中心周末将迎天王山巅峰决战",
      excerpt: "阿尔卡拉斯7-5、6-2横扫卡恰诺夫，辛纳6-2、7-6(6)力克莱赫茨卡，双双强势杀入中国网球公开赛半决赛。",
      body: [
        "中网男单四分之一决赛周五在钻石球场打响，当今男子网坛最顶尖的两大巨星展现出无可匹敌的统治力。",
        "阿尔卡拉斯全场轰出26记制胜分，以7-5、6-2完胜卡恰诺夫，将两人交手战绩改写为4胜0负。",
        "卫冕冠军辛纳同样发挥稳健，在第二盘抢七挽救盘点后以6-2、7-6(6)力克捷克名将莱赫茨卡，豪取个人单打15连胜。",
      ],
    },
    ja: {
      title: "チャイナ・オープン2026：アルカラスがハチャノフ撃破、シナーも4強進出",
      subtitle: "世界トップ2がストレート勝ちで週末の準決勝へ、北京で頂上決戦の期待高まる",
      excerpt: "アルカラスが7-5、6-2でハチャノフを下し、シナーが6-2、7-6でレヘチカに競り勝って準決勝進出を決めた。",
      body: [
        "北京のナショナル・テニスセンターで行われた準々決勝で、男子テニス界の頂点に立つ2人が力強いテニスを披露しました。",
        "カルロス・アルカラスはダイヤモンド・コートで26本のウィナーを放ち、カレン・ハチャノフを7-5、6-2で圧倒しました。",
        "世界1位のヤニック・シナーは第2セットのタイブレークでセットポイントをしのぎ、6-2、7-6(6)でレヘチカを退け15連勝としました。",
      ],
    },
    ko: {
      title: "2026 차이나 오픈: 알카라스, 카차노프 제압 및 신네르 4강 안착",
      subtitle: "세계 1·2위 나란히 무실세트 승리 거두며 베이징 주말 결승 맞대결 기대 고조",
      excerpt: "알카라스가 7-5, 6-2로 카차노프를 꺾고 신네르가 6-2, 7-6으로 레헤츠카를 물리치며 베이징 준결승에 올랐다.",
      body: [
        "차이나 오픈 8강전에서 세계 테니스를 양분하는 두 스타가 나란히 압도적인 기량을 과시했습니다.",
        "카를로스 알카라스는 다이아몬드 코트에서 26개의 위너를 꽂아 넣으며 카렌 카차노프를 7-5, 6-2로 가볍게 완파했습니다.",
        "디펜딩 챔피언 야닉 신네르는 2세트 타이브레이크 위기를 침착하게 넘기며 이르지 레헤츠카를 6-2, 7-6(6)으로 꺾고 15연승을 질주했습니다.",
      ],
    },
    ar: {
      title: "بطولة الصين المفتوحة 2026: ألكاراز يتفوق على خاشانوف وسينر يعبر عقبة ليتشيكا في بكين",
      subtitle: "المصنفان الأول والثاني عالميا يبلغان نصف النهائي بمجموعات نظيفة تمهيدا لنهائي الحلم.",
      excerpt: "كارلوس ألكاراز يفوز 7-5 و6-2 على خاشانوف ويانيك سينر يتغلب على ليتشيكا 6-2 و7-6(6) في بكين.",
      body: [
        "شهدت مباريات ربع نهائي بطولة الصين المفتوحة في بكين عروضا مذهلة من قطبي التنس العالمي الحاليين.",
        "تألق الإسباني كارلوس ألكاراز وضرب 26 كرة قاضية ليتغلب بسهولة على كارين خاشانوف بنتيجة 7-5 و6-2 على الملعب الرئيسي.",
        "بدوره حافظ المصنف الأول يانيك سينر على هدوئه وأنقذ نقطة مجموعة في الشوط الفاصل ليتفوق على ييري ليتشيكا بنتيجة 6-2 و7-6(6).",
      ],
    },
  },
  'pga-tour-sanderson-farms-round2-hossler-leads-2026': {
    fr: {
      title: "Sanderson Farms : Beau Hossler signe un 64 et prend les commandes à -15 à Jackson",
      subtitle: "Huit birdies vendredi permettent à l'Américain de devancer Daniel Berger d'un coup avant le week-end.",
      excerpt: "Beau Hossler vire en tête à 15 sous le par au Country Club of Jackson, un coup devant Daniel Berger dans la course à la FedExCup Fall.",
      body: [
        "Le Country Club of Jackson a une nouvelle fois été le théâtre de scores spectaculaires vendredi, avec la prise de pouvoir de Beau Hossler grâce à un superbe 64 (-8).",
        "L'Américain de 29 ans a totalisé 129 coups sur 36 trous (-15), s'appuyant sur un putting chirurgical pour devancer Daniel Berger d'un coup.",
        "Le champion sortant Kevin Yu reste en embuscade à -10 après un 66 solide, alors que le cut est tombé à 4 sous le par.",
      ],
    },
    es: {
      title: "Sanderson Farms: Beau Hossler firma un 64 y toma el liderato con -15 en Jackson",
      subtitle: "El estadounidense anota ocho birdies el viernes para aventajar por un golpe a Daniel Berger en la FedExCup Fall.",
      excerpt: "Beau Hossler se sitúa en cabeza con 15 bajo par en Jackson tras 36 hoyos, un golpe por delante de Daniel Berger.",
      body: [
        "El Country Club of Jackson brindó otra jornada de ensueño para los golfistas en la segunda ronda del Sanderson Farms Championship.",
        "Beau Hossler firmó una brillante tarjeta de 64 golpes (-8) sin bogeys para acumular 15 bajo par y liderar en solitario hacia el fin de semana.",
        "Daniel Berger lo sigue de cerca con -14 tras su segundo 65 consecutivo, mientras que el campeón defensor Kevin Yu acecha con -10.",
      ],
    },
    de: {
      title: "Sanderson Farms: Beau Hossler spielt eine 64 und führt mit 15 unter Par in Jackson",
      subtitle: "US-Profi locht am Freitag acht Birdies und liegt einen Schlag vor Daniel Berger.",
      excerpt: "Beau Hossler übernimmt die alleinige Führung bei 15 unter Par im Country Club of Jackson vor Daniel Berger.",
      body: [
        "Der Country Club of Jackson bot auch am Freitag perfekte Bedingungen für herausragende Scores auf der PGA Tour.",
        "Beau Hossler setzte sich mit einer fehlerfreien 64 (-8) und einem Gesamtergebnis von 15 unter Par an die Spitze des Klassements.",
        "Daniel Berger lauert mit 14 unter Par auf Rang zwei, während Titelverteidiger Kevin Yu bei 10 unter Par ebenfalls Kontakt zur Spitze hält.",
      ],
    },
    it: {
      title: "Sanderson Farms: Beau Hossler gira in 64 e vola in testa a -15 a Jackson",
      subtitle: "Otto birdie per l'americano che precede di un colpo Daniel Berger nel venerdì della FedExCup Fall.",
      excerpt: "Beau Hossler guida a 15 sotto il par al Country Club of Jackson, tallonato a un colpo da Daniel Berger.",
      body: [
        "Condizioni ideali e punteggi bassissimi hanno caratterizzato il secondo giro del Sanderson Farms Championship in Mississippi.",
        "Beau Hossler ha piazzato un giro spettacolare in 64 colpi (-8) senza bogey, salendo a 15 sotto il par dopo 36 buche.",
        "Daniel Berger insegue a un solo colpo di distanza (-14), mentre il campione in carica Kevin Yu resta competitivo a -10.",
      ],
    },
    pl: {
      title: "Sanderson Farms: Beau Hossler z wynikiem 64 obejmuje prowadzenie z -15 w Jackson",
      subtitle: "Osiem birdie Amerykanina w piątek daje mu jedno uderzenie przewagi nad Danielem Bergerem.",
      excerpt: "Beau Hossler prowadzi po 36 dołkach z wynikiem 15 poniżej par w Country Club of Jackson.",
      body: [
        "Druga runda turnieju Sanderson Farms Championship w Mississippi przyniosła znakomite wyniki na czele stawki.",
        "Beau Hossler zagrał rewelacyjne 64 uderzenia (-8), obejmując samodzielne prowadzenie z łącznym wynikiem 15 poniżej par.",
        "Tuż za nim plasuje się Daniel Berger z wynikiem -14, a obrońca tytułu Kevin Yu traci pięć uderzeń z wynikiem -10.",
      ],
    },
    zh: {
      title: "桑德森农场锦标赛：霍斯勒次轮狂抓8鸟轰出64杆，总成绩-15杆单独领跑",
      subtitle: "霍斯勒一杆优势领先伯格，卫冕冠军俞俊安-10杆紧随其后进入周末决赛圈",
      excerpt: "博·霍斯勒在密西西比杰克逊乡村俱乐部两轮交出-15杆（129杆），以1杆优势力压丹尼尔·伯格领跑美巡秋季赛。",
      body: [
        "美巡赛秋季积分赛桑德森农场锦标赛第二轮在杰克逊乡村俱乐部战罢，球场再次见证了低杆风暴。",
        "29岁的美国选手博·霍斯勒周五发挥神勇，抓下8只小鸟打出零柏忌的64杆（-8），以两轮129杆（-15）的总成绩占据单独榜首。",
        "伤愈复出的丹尼尔·伯格连续两天交出65杆，以一杆之差紧随其后；卫冕冠军中国台北球员俞俊安次轮交出66杆，总成绩-10杆保留争冠希望。",
      ],
    },
    ja: {
      title: "サンダーソン・ファームズ：ホスラーが64を叩き出し通算15アンダーで単独首位浮上",
      subtitle: "ボギーなしの8バーディでバーガーに1打差リード、連覇狙うケビン・ユーも10アンダー追走",
      excerpt: "ボー・ホスラーが36ホール通算15アンダー（129）をマークし、サンダーソン・ファームズ選手権で単独トップに立った。",
      body: [
        "ミシシッピ州ジャクソン・カントリークラブで開催中のPGAツアー秋季シリーズで、バーディ合戦が過熱しています。",
        "ボー・ホスラーが金曜日に8バーディ・ノーボギーの64をマークし、通算15アンダー129で単独首位に立ちました。",
        "1打差の2位には連続65をマークしたダニエル・バーガーがつけ、前年覇者のケビン・ユーも10アンダーで決勝ラウンドへ駒を進めました。",
      ],
    },
    ko: {
      title: "샌더슨 팜스: 보 호슬러 2라운드 64타 폭발, 15언더파 단독 선두 질주",
      subtitle: "보기 없이 버디 8개 몰아치며 버거에 1타 차 선두, 디펜딩 챔피언 케빈 유 10언더파 추격",
      excerpt: "보 호슬러가 36홀 합계 15언더파 129타를 기록하며 미시시피 잭슨에서 1타 차 단독 선두로 나섰다.",
      body: [
        "미시시피주 컨트리클럽 오브 잭슨에서 열린 PGA 투어 샌더슨 팜스 챔피언십 2라운드에서 보 호슬러가 맹타를 휘둘렀습니다.",
        "호슬러는 보기 없이 버디만 8개를 잡아내며 8언더파 64타를 기록, 중간합계 15언더파 129타로 단독 1위에 올랐습니다.",
        "대니얼 버거가 1타 차 2위(14언더파)로 추격 중이며, 타이틀 방어에 나선 케빈 유도 10언더파를 기록하며 주말 우승 경쟁을 예고했습니다.",
      ],
    },
    ar: {
      title: "بطولة ساندرسون فارمز: بو هوسلر يسجل 64 ضربة وينفرد بصدارة الـ 15 تحت المعدل",
      subtitle: "ثماني ضربات بيردي تمنح الأمريكي الصدارة بفارق ضربة واحدة أمام دانييل بيرغر في جولة الجمعة.",
      excerpt: "بو هوسلر ينهي أول 36 حفرة بـ15 ضربة تحت المعدل في نادي جاكسون ليتصدر الترتيب العام.",
      body: [
        "تواصلت العروض التهديفية القوية في بطولة ساندرسون فارمز للجولف في ولاية ميسيسيبي يوم الجمعة.",
        "تألق الأمريكي بو هوسلر مسجلا 64 ضربة (8 تحت المعدل) دون أي خطأ ليرفع رصيده إلى 15 تحت المعدل وينفرد بالصدارة.",
        "ويلاحقه دانييل بيرغر بفارق ضربة واحدة (14 تحت المعدل)، بينما حافظ حامل اللقب كيفن يو على آماله برصيد 10 تحت المعدل.",
      ],
    },
  },
  'f1-singapore-gp-friday-practice-norris-leclerc-2026': {
    fr: {
      title: "GP de Singapour : Lando Norris devance Charles Leclerc de 0,058s sous les projecteurs de Marina Bay",
      subtitle: "McLaren et Ferrari se livrent un duel millimétré lors des essais libres du vendredi soir.",
      excerpt: "Sous l'éclairage de 1 600 projecteurs, Lando Norris a signé le meilleur temps des EL2 en 1:30.727, devançant Charles Leclerc de 58 millièmes.",
      body: [
        "La nuit de Marina Bay a confirmé que le Grand Prix de Singapour 2026 se jouera à d'infimes détails entre McLaren et Ferrari.",
        "Lando Norris a dominé la deuxième séance d'essais libres au volant de sa McLaren avec un chrono référence de 1:30.727 dans des conditions étouffantes.",
        "Charles Leclerc, leader des EL1, a échoué à seulement 0,058 seconde, devançant Carlos Sainz et le leader du championnat Andrea Kimi Antonelli.",
      ],
    },
    es: {
      title: "GP de Singapur: Lando Norris supera a Charles Leclerc por 0.058s bajo los focos de Marina Bay",
      subtitle: "McLaren y Ferrari libran un duelo electrizante en los entrenamientos libres del viernes.",
      excerpt: "Bajo 1.600 focos nocturnos, Lando Norris marcó 1:30.727 en la FP2 para aventajar a Leclerc por apenas 58 milésimas en Singapur.",
      body: [
        "Los entrenamientos nocturnos en el circuito urbano de Marina Bay anticipan una batalla táctica al límite entre McLaren y Ferrari.",
        "Lando Norris completó una vuelta sensacional de 1:30.727 en la FP2 para liderar la tabla de tiempos del viernes en Singapur.",
        "Charles Leclerc quedó a solo 0.058 segundos con su Ferrari, mientras que el líder del certamen Kimi Antonelli finalizó cuarto con Mercedes.",
      ],
    },
    de: {
      title: "Singapur GP: Lando Norris schlägt Charles Leclerc um 0,058s unter den Flutlichtern",
      subtitle: "McLaren und Ferrari liefern sich im Freitagstraining von Marina Bay ein packendes Kopf-an-Kopf-Rennen.",
      excerpt: "Unter 1.600 Scheinwerfern markierte Lando Norris mit 1:30,727 die FP2-Bestzeit, hauchdünn vor Charles Leclerc.",
      body: [
        "Das Flutlicht-Spektakel in Singapur verspricht ein extrem enges Wochenende zwischen McLaren und Ferrari.",
        "Lando Norris stellte seinen McLaren im zweiten freien Training mit 1:30,727 Minuten an die Spitze des Klassements.",
        "Charles Leclerc verpasste die Bestzeit um lediglich 0,058 Sekunden, während WM-Leader Andrea Kimi Antonelli Vierter wurde.",
      ],
    },
    it: {
      title: "GP Singapore: Lando Norris beffa Charles Leclerc per 0,058s sotto i riflettori di Marina Bay",
      subtitle: "McLaren e Ferrari si contendono il primato nelle prove libere del venerdì notte a Singapore.",
      excerpt: "Nelle FP2 a Marina Bay, Lando Norris ha fermato il cronometro a 1:30.727 precedendo Charles Leclerc di soli 58 millesimi.",
      body: [
        "Il venerdì sera a Marina Bay ha offerto un antipasto del duello ravvicinatissimo tra McLaren e Ferrari per la vittoria a Singapore.",
        "Lando Norris ha strappato il miglior tempo delle FP2 in 1:30.727, sfidando l'asfalto sconnesso e l'altissima umidità tropicale.",
        "Charles Leclerc, dopo aver primeggiato nelle FP1, si è piazzato secondo a 58 millesimi, davanti a Carlos Sainz e al leader del mondiale Antonelli.",
      ],
    },
    pl: {
      title: "GP Singapuru: Lando Norris wyprzedza Charlesa Leclerca o 0,058s pod światłami Marina Bay",
      subtitle: "McLaren i Ferrari toczą zaciętą walkę o ułamki sekund w piątkowych treningach nocnych.",
      excerpt: "Lando Norris uzyskał czas 1:30.727 w FP2, wyprzedzając Leclerca o zaledwie 0,058 sekundy w Singapurze.",
      body: [
        "Piątkowe sesje treningowe na Marina Bay pokazały, że walka o pole position w Singapurze rozegra się między McLarenem a Ferrari.",
        "Lando Norris ustanowił najlepszy wynik dnia na poziomie 1:30.727 podczas symulacji kwalifikacyjnych w drugim treningu.",
        "Charles Leclerc stracił do Brytyjczyka zaledwie 0,058 sekundy, a lider mistrzostw Andrea Kimi Antonelli zajął czwartą lokatę.",
      ],
    },
    zh: {
      title: "F1新加坡大奖赛：诺里斯仅领先勒克莱尔0.058秒，闪耀滨海湾周五夜间练习赛",
      subtitle: "迈凯伦与法拉利在1600盏泛光灯下展开微秒级争夺，排位赛前瞻火花四射",
      excerpt: "诺里斯在二练中跑出1分30秒727的最快圈速，以0.058秒的微弱优势力压勒克莱尔领跑周五成绩榜。",
      body: [
        "在1600盏泛光灯的照耀与30度的高温高湿环境下，2026年F1新加坡大奖赛周五练习赛拉开序幕。",
        "迈凯伦车手兰多·诺里斯在二练排位赛模拟中发挥出色，以1分30秒727刷新全场最快圈速。",
        "一练领跑的法拉利车手勒克莱尔仅以0.058秒之差屈居次席，积分榜领头羊安东内利位列第四，周六排位争夺战悬念拉满。",
      ],
    },
    ja: {
      title: "F1シンガポールGP：ノリスが0.058秒差でルクレールを抑えFP2トップに浮上",
      subtitle: "マリーナ・ベイの夜間照明下でマクラーレンとフェラーリがミリ秒単位の攻防を展開",
      excerpt: "1600基の照明の下で行われたFP2で、ノリスが1分30秒727を記録しルクレールを僅差で抑えた。",
      body: [
        "マリーナ・ベイ市街地コースのナイトセッションで、マクラーレンとフェラーリが驚異的なタイム合戦を繰り広げました。",
        "ランド・ノリスがFP2の予選シミュレーションで1分30秒727をマークし、金曜日の最速ドライバーとなりました。",
        "FP1首位だったシャルル・ルクレールがわずか0.058秒差の2位に続き、選手権リーダーのアントネッリが4位につけました。",
      ],
    },
    ko: {
      title: "F1 싱가포르 GP: 랜도 노리스, 0.058초 차로 르클레르 제치고 금요일 야간 주행 1위",
      subtitle: "마리나 베이 1,600개 조명 아래 맥라렌과 페라리의 치열한 초박빙 연습 세션",
      excerpt: "랜도 노리스가 FP2에서 1분 30초 727을 기록하며 르클레르를 0.058초 차로 제치고 금요일 세션을 지배했다.",
      body: [
        "마리나 베이 시가지 서킷에서 펼쳐진 금요일 야간 주행에서 맥라렌과 페라리가 치열한 속도전을 펼쳤습니다.",
        "랜도 노리스는 FP2 예선 시뮬레이션에서 1분 30초 727의 랩타임을 작성하며 금요일 종합 1위에 올랐습니다.",
        "FP1 1위였던 샤를 르클레르는 불과 0.058초 뒤진 2위를 기록했고, 드라이버 챔피언십 선두 안토넬리가 4위를 마크했습니다.",
      ],
    },
    ar: {
      title: "جائزة سنغافورة الكبرى: لاندو نوريس يتقدم على شارل لوكلير بفارق 0.058 ثانية في تجارب الجمعة",
      subtitle: "مكلارين وفيراري يتبادلان الصدارة تحت أضواء مارينا باي الكاشفة في ليلة استوائية حارقة.",
      excerpt: "لاندو نوريس يسجل أسرع لفة في التجارب الحرة الثانية بزمن 1:30.727 متقدما بفارق ضئيل على لوكلير في سنغافورة.",
      body: [
        "أكدت التجارب الحرة لسباق جائزة سنغافورة الكبرى 2026 أن المعركة ستكون شرسة للغاية بين مكلارين وفيراري.",
        "سجل البريطاني لاندو نوريس الزمن الأسرع في حصة التجارب الثانية بزمن قدره 1:30.727 في أجواء شديدة الرطوبة.",
        "وحل شارل لوكلير ثانيا بفارق 0.058 ثانية فقط، بينما احتل متصدر البطولة كيمي أنتونيللي المركز الرابع مع مرسيدس.",
      ],
    },
  },
  'premier-league-mw7-city-seven-straight-wins-2026': {
    fr: {
      title: "Premier League 7e j. : Haaland et Foden renversent Brentford pour un septième succès de rang",
      subtitle: "Manchester City conserve son bilan parfait avec 21 points tandis que Liverpool bat Crystal Palace 1-0.",
      excerpt: "Mené d'entrée, Manchester City s'impose 2-1 à Brentford grâce aux buts d'Erling Haaland et Phil Foden.",
      body: [
        "Sept matches, sept victoires. Manchester City a poursuivi son sans-faute en Premier League samedi sur le terrain de Brentford.",
        "Surpris par Bryan Mbeumo à la 19e minute, les Citizens ont réagi grâce au 11e but de la saison d'Erling Haaland de la tête, avant que Phil Foden n'inscrive le but de la victoire d'une frappe rasante à la 68e minute.",
        "City conserve trois longueurs d'avance sur Arsenal, tombeur de Southampton 3-1, et Liverpool, vainqueur 1-0 à Crystal Palace grâce à Diogo Jota.",
      ],
    },
    es: {
      title: "Premier League Jornada 7: Haaland y Foden remontan ante Brentford para sellar siete triunfos seguidos",
      subtitle: "El Manchester City de Guardiola sigue perfecto con 21 puntos mientras el Liverpool vence 1-0 al Palace.",
      excerpt: "Manchester City remontó en el Gtech Community Stadium para vencer 2-1 al Brentford y sostener su paso ideal.",
      body: [
        "Siete partidos y siete victorias. El Manchester City mantuvo su implacable marcha liguera este sábado tras remontar un partido exigente en Londres.",
        "Bryan Mbeumo adelantó a las Abejas a los 19 minutos, pero Erling Haaland igualó de cabeza con su 11.º gol del curso y Phil Foden sentenció en el minuto 68.",
        "Con este 2-1, el City llega a 21 puntos para mantener su ventaja sobre Arsenal (3-1 a Southampton) y Liverpool (1-0 a Crystal Palace).",
      ],
    },
    de: {
      title: "Premier League 7. Spieltag: Haaland und Foden drehen Spiel bei Brentford zum siebten Sieg in Serie",
      subtitle: "Manchester City bleibt mit 21 Punkten makellos an der Spitze, während Liverpool 1:0 bei Palace gewinnt.",
      excerpt: "Manchester City dreht einen 0:1-Rückstand bei Brentford und siegt dank Haaland und Foden mit 2:1.",
      body: [
        "Sieben Spiele, sieben Siege. Manchester City setzt seinen perfekten Saisonstart in der Premier League mit einem 2:1-Erfolg bei Brentford fort.",
        "Nach dem frühen Rückstand durch Bryan Mbeumo (19.) glich Erling Haaland per Kopf mit seinem 11. Saisontor aus, ehe Phil Foden in der 68. Minute den Siegtreffer erzielte.",
        "City führt die Tabelle mit 21 Punkten weiter vor Arsenal (3:1 gegen Southampton) und Liverpool (1:0 bei Crystal Palace) an.",
      ],
    },
    it: {
      title: "Premier League 7ª giornata: Haaland e Foden firmano la rimonta sul Brentford, settima vittoria City",
      subtitle: "I campioni di Guardiola guidano a punteggio pieno con 21 punti; il Liverpool batte il Palace 1-0.",
      excerpt: "Il Manchester City rimonta lo svantaggio iniziale al Gtech Stadium vincendo 2-1 contro il Brentford.",
      body: [
        "Sette gare e sette vittorie per il Manchester City, che supera un ostico Brentford in trasferta per confermarsi in vetta.",
        "Al gol di Bryan Mbeumo al 19' risponde Erling Haaland di testa (11° centro stagionale), prima del rasoterra decisivo di Phil Foden al 68'.",
        "I Citizens toccano quota 21 punti, mantenendo tre punti di margine su Arsenal (3-1 al Southampton) e Liverpool (1-0 al Crystal Palace).",
      ],
    },
    pl: {
      title: "Premier League 7. kolejka: Haaland i Foden odwracają losy meczu z Brentford, siódme zwycięstwo City",
      subtitle: "Manchester City z kompletem 21 punktów prowadzi w tabeli, podczas gdy Liverpool wygrywa 1-0 z Palace.",
      excerpt: "Manchester City pokonał na wyjeździe Brentford 2-1 dzięki bramkom Erlinga Haalanda i Phila Fodena.",
      body: [
        "Siedem meczów i siedem zwycięstw. Manchester City utrzymał stuprocentowy bilans po zaciętym spotkaniu w zachodnim Londynie.",
        "Gospodarze prowadzili po golu Bryana Mbeumo, lecz Haaland wyrównał strzałem głową, a w 68. minucie zwycięstwo gościom zapewnił Phil Foden.",
        "City ma 21 punktów i wyprzedza Arsenal (3-1 z Southampton) oraz Liverpool (1-0 z Crystal Palace po golu Joty).",
      ],
    },
    zh: {
      title: "英超第7轮：哈兰德扳平福登绝杀，曼城客场2-1逆转布伦特福德豪取七连胜",
      subtitle: "瓜迪奥拉球队21分领跑积分榜，利物浦1-0小胜水晶宫紧随其后",
      excerpt: "曼城在客场先失一球的情况下连入两球，凭借哈兰德第11球与福登的低射2-1力克布伦特福德。",
      body: [
        "七战全胜！曼城在周六下午的西伦敦展现了卫冕冠军的顽强底蕴，客场2-1逆转布伦特福德。",
        "姆贝乌莫第19分钟反击首开纪录，哈兰德第34分钟头球打入个人赛季第11球，福登在第68分钟推射反超比分锁定胜局。",
        "曼城以21分强势领跑，阿森纳3-1逆转南安普顿，利物浦凭借若塔进球1-0击败水晶宫。",
      ],
    },
    ja: {
      title: "プレミアリーグ第7節：ハーランド同点弾とフォーデンの決勝点でマンCがブレントフォードに2-1逆転勝利",
      subtitle: "グアルディオラ率いる首位マンチェスター・シティが開幕7連勝で勝ち点21に到達",
      excerpt: "マンチェスター・シティは敵地で先制を許すも、ハーランドの今季11点目とフォーデンのゴールで2-1の逆転勝利を収めた。",
      body: [
        "開幕7戦全勝。マンチェスター・シティは敵地Gtechコミュニティ・スタジアムでブレントフォードに2-1で逆転勝利を飾りました。",
        "19分にエムベウモに先制点を許したものの、34分にハーランドがヘディングで同点弾を叩き込み、68分にフォーデンが技ありの決勝ゴールを奪いました。",
        "シティは勝ち点21で首位を堅持。アーセナルはサウサンプトンに3-1で勝利し、リヴァプールはパレスを1-0で下しました。",
      ],
    },
    ko: {
      title: "프리미어리그 7라운드: 홀란 동점골과 포든 결승골, 맨시티 브렌트퍼드 2-1 꺾고 개막 7연승 질주",
      subtitle: "과르디올라 감독의 맨시티 승점 21점 완벽한 질주, 리버풀도 팰리스 1-0 제압",
      excerpt: "맨체스터 시티가 브렌트퍼드 원정에서 먼저 실점하고도 홀란과 포든의 연속골로 2-1 역전승을 거두었다.",
      body: [
        "7전 7승 전승 행진. 맨체스터 시티가 토요일 런던 원정에서 브렌트퍼드를 2-1로 꺾고 리그 선두를 지켰습니다.",
        "음뵈모에게 전반 19분 선제골을 내줬지만, 전반 34분 홀란이 시즌 11호 헤더골로 균형을 맞췄고 후반 23분 포든이 결승골을 터뜨렸습니다.",
        "맨시티는 승점 21점으로 아스널(3-1 승)과 리버풀(1-0 승)의 추격을 뿌리치고 3점 차 선두를 유지했습니다.",
      ],
    },
    ar: {
      title: "الدوري الإنجليزي الجولة 7: هالاند وفودين يقودان مانشستر سيتي لقلب الطاولة على برينتفورد وتحقيق الفوز السابع",
      subtitle: "كتيبة غوارديولا تحافظ على العلامة الكاملة برصيد 21 نقطة وليفربول يتخطى بالاس بهدف نظيف.",
      excerpt: "مانشستر سيتي يعوض تأخره بهدف ليفوز 2-1 على برينتفورد بفضل ثنائية إيرلينغ هالاند وفيل فودين.",
      body: [
        "سبع مباريات وسبعة انتصارات متتالية. واصل مانشستر سيتي انطلاقته التاريخية في الدوري الإنجليزي الممتاز بعد فوز صعب في لندن.",
        "تقدم برينتفورد عبر مبيومو في الدقيقة 19، قبل أن يعادل هالاند برأسية رائعة مسجلا هدفه الـ11 هذا الموسم، وسجل فودين هدف الفوز في الدقيقة 68.",
        "رفع سيتي رصيده إلى 21 نقطة في الصدارة، في حين انتصر أرسنال على ساوثهامبتون 3-1 وتغلب ليفربول على كريستال بالاس 1-0.",
      ],
    },
  },
  'nfl-week4-snf-preview-bills-ravens-2026': {
    fr: {
      title: "NFL 4e semaine SNF : les Bills invaincus défient Lamar Jackson et les Ravens à Baltimore",
      subtitle: "Josh Allen vise le 4-0 à la tête de la meilleure attaque de la ligue face au défi physique de Derrick Henry.",
      excerpt: "L'affiche de dimanche soir oppose les Buffalo Bills (3-0) de Josh Allen aux Baltimore Ravens de Lamar Jackson au M&T Bank Stadium.",
      body: [
        "Le choc de la quatrième semaine de NFL promet des étincelles dimanche soir avec le déplacement des Bills invaincus à Baltimore.",
        "Josh Allen brille avec 11 touchdowns et aucune interception en trois matches, menant l'attaque la plus prolifique de la NFL avec 34,3 points de moyenne.",
        "Lamar Jackson et Derrick Henry comptent sur leur jeu au sol dévastateur pour infliger aux Bills leur première défaite de l'automne.",
      ],
    },
    es: {
      title: "NFL Semana 4 SNF: Los invictos Bills se miden a Lamar Jackson y los Ravens en Baltimore",
      subtitle: "Josh Allen busca poner a Buffalo 4-0 ante la poderosa ofensiva terrestre liderada por Derrick Henry.",
      excerpt: "El gran partido del domingo por la noche enfrenta a los Bills de Josh Allen contra los Ravens de Lamar Jackson en el M&T Bank Stadium.",
      body: [
        "El Sunday Night Football de la Semana 4 reúne a dos de los mariscales de campo más determinantes de la Conferencia Americana.",
        "Josh Allen suma 11 anotaciones sin pérdidas de balón comandando un ataque que promedia más de 34 puntos por encuentro.",
        "Baltimore busca equilibrar su récord a 2-2 imponiendo el poder de Derrick Henry ante la defensiva frontal de Buffalo.",
      ],
    },
    de: {
      title: "NFL Woche 4 SNF: Ungeschlagene Bills fordern Lamar Jackson und die Ravens in Baltimore",
      subtitle: "Josh Allen will Buffalo auf 4-0 führen, während Derrick Henry und Baltimore auf Rebound drängen.",
      excerpt: "Im Topspiel am Sonntagabend treffen die fehlerfreien Buffalo Bills auf die körperbetonte Offensive der Baltimore Ravens.",
      body: [
        "Das Highlight von NFL-Woche 4 steigt am Sonntagabend im M&T Bank Stadium zwischen den Buffalo Bills und den Baltimore Ravens.",
        "Josh Allen glänzt mit 11 Gesamt-Touchdowns ohne Ballverlust und führt die beste Punkte-Offensive der Liga (34,3 Punkte pro Spiel) an.",
        "Lamar Jackson und Derrick Henry wollen das Laufspiel dominieren, um Buffalo die erste Saisonniederlage beizubringen.",
      ],
    },
    it: {
      title: "NFL Week 4 SNF: I Bills imbattuti affrontano Lamar Jackson e i Ravens a Baltimora",
      subtitle: "Josh Allen punta al 4-0 per Buffalo contro il temibile attacco su corsa guidato da Derrick Henry.",
      excerpt: "Il Sunday Night Football propone la sfida tra i Buffalo Bills (3-0) e i Baltimore Ravens al M&T Bank Stadium.",
      body: [
        "La quarta giornata NFL culmina con una sfida d'alta quota tra due pesi massimi della AFC a Baltimora.",
        "Josh Allen guida la lega con 11 touchdown totali e zero turnover, orchestrando un attacco da oltre 34 punti di media.",
        "Lamar Jackson e Derrick Henry proveranno a controllare il cronometro con il loro devastante gioco su corsa.",
      ],
    },
    pl: {
      title: "NFL 4. tydzień SNF: Niepokonani Bills mierzą się z Lamarem Jacksonem i Ravens w Baltimore",
      subtitle: "Josh Allen celuje w bilans 4-0, podczas gdy Derrick Henry i gospodarze walczą o powrót do równowagi.",
      excerpt: "Niedzielny hit NFL stawia naprzeciw siebie bezbłędnych Buffalo Bills oraz groźnych Baltimore Ravens.",
      body: [
        "Niedzielne spotkanie na M&T Bank Stadium to pojedynek dwóch czołowych rozgrywających ligi w 4. tygodniu NFL.",
        "Josh Allen ma na koncie 11 przyłożeń bez straty, prowadząc najskuteczniejszy atak ligi ze średnią 34,3 punktu na mecz.",
        "Ravens liczą na siłę biegową Derricka Henry'ego i dynamikę Jacksona, by zatrzymać rozpędzone Buffalo.",
      ],
    },
    zh: {
      title: "NFL第四周周日夜赛前瞻：全胜布法罗比尔客场挑战拉马尔·杰克逊与乌鸦军团",
      subtitle: "乔什·阿伦剑指四连胜开局，德里克·亨利坐镇巴尔的摩主场严阵以待",
      excerpt: "美联重头戏周日晚打响，场均34.3分火力全开的布法罗比尔做客M&T银行体育场挑战巴尔的摩乌鸦。",
      body: [
        "NFL第四周焦点之战将在巴尔的摩打响，保持全胜的比尔队客场挑战拉马尔·杰克逊率领的乌鸦队。",
        "阿伦本赛季已贡献11次达阵且零失误，乔·布拉迪调教的进攻组场均轰下联盟最高的34.3分。",
        "乌鸦队拥有杰克逊与亨利的强力冲球组合，他们将全力掌控控球时间，阻击比尔队的连胜步伐。",
      ],
    },
    ja: {
      title: "NFL第4週SNFプレビュー：無敗のビルズがラマー・ジャクソン率いるレイブンズとボルティモアで激突",
      subtitle: "アレンが4連勝を狙い、デリック・ヘンリー擁するレイブンズが本拠地で迎え撃つ",
      excerpt: "日曜夜の全米中継で、開幕3連勝のバッファロー・ビルズと強力ラン攻撃を誇るボルティモア・レイブンズが対戦する。",
      body: [
        "NFL第4週のサンデーナイト・フットボールは、M&Tバンク・スタジアムでのAFC屈指の強豪対決となります。",
        "ジョシュ・アレンはターンオーバーなしで11タッチダウンを量産し、チームはリーグ最高の平均34.3得点を記録しています。",
        "レイブンズはラマー・ジャクソンとデリック・ヘンリーの破壊的な地上戦でビルズのディフェンスを崩しにかかります。",
      ],
    },
    ko: {
      title: "NFL 4주차 SNF 프리뷰: 무패의 버펄로 빌스, 볼티모어에서 라마 잭슨과 레이븐스 격돌",
      subtitle: "조시 앨런의 4승 도전, 데릭 헨리와 레이븐스의 강력한 러싱 공격에 맞서다",
      excerpt: "선데이 나이트 풋볼에서 3승 무패의 빌스와 전통의 강호 레이븐스가 M&T 뱅크 스타디움에서 맞붙는다.",
      body: [
        "NFL 4주차 최고의 빅매치가 일요일 밤 볼티모어 M&T 뱅크 스타디움에서 화려하게 펼쳐집니다.",
        "조시 앨런은 턴오버 없이 11개의 터치다운을 만들어내며 리그 1위 득점력(평균 34.3점)을 이끌고 있습니다.",
        "레이븐스는 2회 MVP 라마 잭슨과 데릭 헨리의 위력적인 러싱 조합으로 빌스의 무패 행진을 저지하려 합니다.",
      ],
    },
    ar: {
      title: "دوري كرة القدم الأمريكية الأسبوع 4: بافلو بيلز الذي لا يقهر يصطدم بلامار جاكسون والغراب في بالتيمور",
      subtitle: "جوش ألين يطمح لتحقيق الفوز الرابع تواليا في مواجهة آلة بالتيمور الأرضية بقيادة ديريك هنري.",
      excerpt: "قمة ليلة الأحد تجمع بافلو بيلز (3-0) ضد بالتيمور ريفنز على ملعب إم آند تي بنك في الأسبوع الرابع.",
      body: [
        "تتجه أنظار عشاق كرة القدم الأمريكية إلى بالتيمور لمتابعة قمة نارية تجمع بين جوش ألين ولامار جاكسون.",
        "يقدم ألين مستويات استثنائية بتسجيله 11 هبوطا دون أي خطأ، ليقود هجوم بيلز لتسجيل 34.3 نقطة كأعلى معدل في الدوري.",
        "ويعول بالتيمور على القوة الضاربة للعداء ديريك هنري للسيطرة على مجريات اللقاء وتحقيق فوز معنوي حاسم.",
      ],
    },
  },
  'wnba-semifinals-eve-tactical-breakdown-2026': {
    fr: {
      title: "Veille des demi-finales WNBA : décryptage tactique avant le coup d'envoi de Lynx-Fever et Aces-Liberty",
      subtitle: "Cheryl Reeve prépare un piège pour Caitlin Clark tandis que Becky Hammon retrouve New York.",
      excerpt: "Les quatre survivants des séries éliminatoires WNBA 2026 peaufinent leurs plans avant le coup d'envoi des matches 1 dimanche.",
      body: [
        "Samedi a offert un calme trompeur en WNBA, les quatre prétendants au titre terminant leurs séances vidéo avant les demi-finales de dimanche.",
        "À Minneapolis, la numéro 1 Minnesota prépare un défi défensif de taille pour la sensation Caitlin Clark et le Fever d'Indiana.",
        "À New York, les Aces de Las Vegas d'A'ja Wilson retrouvent le Liberty de Breanna Stewart et Sabrina Ionescu dans un remake des finales 2023.",
      ],
    },
    es: {
      title: "Víspera de semifinales WNBA: Análisis táctico antes del inicio de Lynx-Fever y Aces-Liberty",
      subtitle: "Cheryl Reeve prepara trampas defensivas para Caitlin Clark y las Aces reeditan su rivalidad con New York.",
      excerpt: "Los cuatro semifinalistas de la WNBA afinan detalles antes del arranque al mejor de cinco este domingo.",
      body: [
        "La calma previa a la tormenta reinó este sábado en la WNBA con los cuatro mejores equipos afinando su libreta táctica.",
        "En Mineápolis, las Lynx buscan frenar el ritmo vertiginoso de Caitlin Clark con la Jugadora Defensiva del Año Napheesa Collier.",
        "En Nueva York, el Liberty de Breanna Stewart recibe a las bicampeonas Las Vegas Aces lideradas por la tres veces MVP A'ja Wilson.",
      ],
    },
    de: {
      title: "WNBA-Halbfinal-Vorschau: Taktische Analyse vor Spiel 1 von Lynx-Fever und Aces-Liberty",
      subtitle: "Cheryl Reeve plant Fallen gegen Caitlin Clark, während Becky Hammon und New York die Rivalität neu entfachen.",
      excerpt: "Die vier verbliebenen WNBA-Titelanwärter schließen am Samstag ihre Vorbereitung auf Spiel 1 der Halbfinalserien ab.",
      body: [
        "Am Samstag herrschte fokussierte Konzentration vor dem mit Spannung erwarteten Halbfinal-Auftakt am Sonntag.",
        "Die topgesetzten Minnesota Lynx setzen auf ihre Defensivspezialistin Napheesa Collier, um Caitlin Clark und Indiana zu stoppen.",
        "In New York kommt es zum Klassiker zwischen den Las Vegas Aces um MVP A'ja Wilson und dem New York Liberty um Breanna Stewart.",
      ],
    },
    it: {
      title: "Vigilia semifinali WNBA: Analisi tattica prima di Gara 1 tra Lynx-Fever e Aces-Liberty",
      subtitle: "Cheryl Reeve prepara trappole per Caitlin Clark, mentre le Aces ritrovano le rivali di New York.",
      excerpt: "Le magnifiche quattro della WNBA completano i preparativi prima del doppio appuntamento domenicale.",
      body: [
        "Un sabato di studio e concentrazione chiude la vigilia delle semifinali WNBA che scatteranno domenica.",
        "A Minneapolis, le Minnesota Lynx affrontano Caitlin Clark e l'Indiana Fever in una classica sfida tra miglior difesa e attacco esplosivo.",
        "Al Barclays Center va in scena il duello infinito tra A'ja Wilson e le campionesse in carica del New York Liberty guidate da Breanna Stewart.",
      ],
    },
    pl: {
      title: "Wigilia półfinałów WNBA: Analiza taktyczna przed meczami nr 1 Lynx-Fever i Aces-Liberty",
      subtitle: "Cheryl Reeve szykuje pułapki na Caitlin Clark, a Aces i Liberty wznawiają mistrzowską rywalizację.",
      excerpt: "Cztery czołowe zespoły WNBA kończą przygotowania do niedzielnych starć otwierających serie półfinałowe.",
      body: [
        "Sobotnie treningi zamknęły okres przygotowań do decydującej fazy play-off WNBA 2026.",
        "W Minneapolis Minnesota Lynx i Napheesa Collier spróbują powstrzymać rewelacyjną Caitlin Clark i Indiana Fever.",
        "W Nowym Jorku dojdzie do rewanżu za finały 2023 między Las Vegas Aces z A'ja Wilson a New York Liberty z Breanną Stewart.",
      ],
    },
    zh: {
      title: "WNBA半决赛前瞻：山猫对阵狂热、王牌再战自由人，四大豪门战术全面解析",
      subtitle: "里夫为克拉克布设防守陷阱，威尔逊与斯图尔特重演总决赛巅峰对决",
      excerpt: "周六备战全部就绪，2026年WNBA半决赛五局三胜制较量将于周日正式打响两场G1大战。",
      body: [
        "周六的平静难掩大战将至的硝烟，四支晋级四强的豪强完成了周日G1揭幕战前的最后演练。",
        "明尼苏达山猫坐镇主场，年度最佳防守球员科利尔领衔的铁血防线将全力围剿凯特琳·克拉克与狂热队的外线跑轰。",
        "纽约自由人主场迎战卫冕霸主拉斯维加斯王牌，威尔逊与斯图尔特、约内斯库的宿敌对抗再度成为全美焦点。",
      ],
    },
    ja: {
      title: "WNBA準決勝プレビュー：リンクス対フィーバー、エACES対リバティの初戦戦術分析",
      subtitle: "リーブHCがクラーク対策を構築、ウィルソンとスチュワートが再び火花を散らす",
      excerpt: "WNBAファイナル進出を懸けた5戦3勝方式の準決勝第1戦が日曜日にティップオフを迎える。",
      body: [
        "土曜日の非公開練習を終え、WNBAのトップ4チームが日曜日のダブルヘッダー初戦へ万全の準備を整えました。",
        "ミネアポリスでは第1シードのリンクスが、ケイトリン・クラーク擁するインディアナ・フィーバーの高速オフェンスを迎え撃ちます。",
        "ニューヨークではエイジャ・ウィルソン率いるエACESとブレアナ・スチュワートのリバティによる因縁の対決が幕を開けます。",
      ],
    },
    ko: {
      title: "WNBA 4강 준결승 전야: 링스-피버, 에이시스-리버티 1차전 맞대결 전술 분석",
      subtitle: "클라크를 막아설 셰릴 리브의 수비 전술과 윌슨-스튜어트의 라이벌 리턴매치",
      excerpt: "WNBA 플레이오프 4강전 5전 3선승제 1차전이 일요일 드디어 화려하게 막을 올린다.",
      body: [
        "토요일 최종 훈련을 마친 WNBA 4강 팀들이 일요일 1차전 결전을 앞두고 전의를 불태우고 있습니다.",
        "미네소타 링스는 올해의 수비수 나피사 콜리어를 앞세워 케이틀린 클라크의 폭발적인 득점력을 차단하는 데 집중하고 있습니다.",
        "뉴욕 바클레이스 센터에서는 3회 MVP 에이자 윌슨의 에이시스와 브리아나 스튜어트의 리버티가 2023년 파이널 리매치를 벌입니다.",
      ],
    },
    ar: {
      title: "عشية نصف نهائي دوري السلة الأمريكي للسيدات: تفكيك تكتيكي قبل انطلاق قمتي لينكس-فيفر وإيسز-ليبرتي",
      subtitle: "شيريل ريف تجهز فخاخا لإيقاف كايتلين كلارك وآجا ويلسون تجدد صراعها مع بريانا ستيوارت.",
      excerpt: "أكملت الفرق الأربعة المتأهلة لنصف نهائي WNBA استعداداتها التكتيكية قبل انطلاق سلسلة المباريات يوم الأحد.",
      body: [
        "ساد الهدوء الحذر أروقة دوري السلة الأمريكي للسيدات يوم السبت قبل انطلاق قمتي المربع الذهبي.",
        "في مينيسوتا، يواجه فريق لينكس صاحب أفضل دفاع اختبارا حاسما أمام الهجوم الناري لكايتلين كلارك وفريق إنديانا فيفر.",
        "وفي نيويورك، يتجدد الصراع الملحمي بين حاملتي اللقب لاس فيغاس إيسز ونيويورك ليبرتي في مواجهة نارية بين ويلسون وستيوارت.",
      ],
    },
  },
  'china-open-2026-alcaraz-sinner-set-beijing-final': {
    fr: {
      title: "China Open 2026 : Alcaraz écarte Medvedev et Sinner domine Bu pour une finale de rêve à Pékin",
      subtitle: "Le numéro 1 et le numéro 2 mondiaux s'affronteront dimanche sur le court Diamond pour le titre ATP 500.",
      excerpt: "Carlos Alcaraz a dominé Daniil Medvedev 7-5, 6-3 tandis que Jannik Sinner a écarté Bu Yunchaokete pour sceller leur 10e face-à-face.",
      body: [
        "Le scénario rêvé est devenu réalité samedi à Pékin : Carlos Alcaraz et Jannik Sinner se retrouveront en finale du tournoi ATP 500.",
        "Alcaraz s'est montré intraitable face à Daniil Medvedev, s'imposant 7-5, 6-3 grâce à 82 % de points remportés derrière sa première balle.",
        "Jannik Sinner a ensuite maîtrisé le chouchou du public Bu Yunchaokete 6-3, 7-6(3) pour rejoindre l'Espagnol dans un choc au sommet.",
      ],
    },
    es: {
      title: "China Open 2026: Alcaraz supera a Medvedev y Sinner vence a Bu para citarse en la final soñada",
      subtitle: "El número 1 y el número 2 del mundo chocarán este domingo en la pista Diamond por el título de Pekín.",
      excerpt: "Carlos Alcaraz derrotó 7-5, 6-3 a Daniil Medvedev y Jannik Sinner venció a Bu para fijar su décimo duelo directo.",
      body: [
        "El torneo de Pekín disfrutará este domingo del desenlace más esperado con el choque directo entre Carlos Alcaraz y Jannik Sinner.",
        "El español de 21 años neutralizó a Daniil Medvedev con un juego brillante y agresivo para imponerse 7-5 y 6-3 en una hora y 28 minutos.",
        "Por su parte, el vigente campeón Sinner templó los nervios ante el héroe local Bu Yunchaokete para vencer 6-3, 7-6(3) y alcanzar la final.",
      ],
    },
    de: {
      title: "China Open 2026: Alcaraz schlägt Medwedew und Sinner siegt gegen Bu zum Traumfinale in Peking",
      subtitle: "Die Nummer 1 und Nummer 2 der Welt duellieren sich am Sonntag auf dem Diamond Court um den Titel.",
      excerpt: "Carlos Alcaraz setzte sich mit 7:5, 6:3 gegen Daniil Medwedew durch, ehe Titelverteidiger Jannik Sinner nachzog.",
      body: [
        "Peking bekommt sein absolutes Traumfinale: Carlos Alcaraz und Jannik Sinner haben am Samstag souverän das Endspiel erreicht.",
        "Alcaraz dominierte Daniil Medwedew mit 7:5, 6:3 und überzeugte mit variablem Angriffsspiel und hoher Aufschlagquote.",
        "Jannik Sinner behielt gegen Lokalmatador Bu Yunchaokete mit 6:3, 7:6(3) die Nerven und trifft am Sonntag zum 10. Mal auf Alcaraz.",
      ],
    },
    it: {
      title: "China Open 2026: Alcaraz liquida Medvedev e Sinner batte Bu, a Pechino sarà finale da sogno",
      subtitle: "Il numero 1 e il numero 2 del mondo si sfideranno domenica sul Diamond Court per la corona ATP 500.",
      excerpt: "Carlos Alcaraz ha battuto Daniil Medvedev 7-5, 6-3 e Jannik Sinner ha superato Bu Yunchaokete conquistando la finale.",
      body: [
        "Gli appassionati di tennis avranno la finale più attesa: Alcaraz e Sinner si contenderanno il titolo dell'ATP 500 di Pechino.",
        "Lo spagnolo ha superato Daniil Medvedev per 7-5, 6-3 con una prestazione eccezionale al servizio e nei colpi a rimbalzo.",
        "Sinner ha risposto in serata superando il cinese Bu Yunchaokete per 6-3, 7-6(3), fissando il decimo capitolo della loro rivalità.",
      ],
    },
    pl: {
      title: "China Open 2026: Alcaraz pokonuje Miedwiediewa, Sinner ogrywa Bu, wymarzony finał w Pekinie",
      subtitle: "Lider i wicelider rankingu ATP zmierzą się w niedzielę na Diamond Court o prestiżowy tytuł.",
      excerpt: "Carlos Alcaraz wygrał 7-5, 6-3 z Daniiłem Miedwiediewem, a Jannik Sinner odprawił Bu Yunchaokete, meldując się w finale.",
      body: [
        "Wymarzony finał w Pekinie stał się faktem po znakomitych sobotnich półfinałach z udziałem Alcaraza i Sinnera.",
        "Hiszpan nie dał szans Daniiłowi Miedwiediewowi, triumfując 7-5, 6-3 dzięki fantastycznej grze przy własnym podaniu.",
        "Broniący tytułu Jannik Sinner pokonał faworyta gospodarzy Bu Yunchaokete 6-3, 7-6(3), doprowadzając do 10. starcia z Alcarazem.",
      ],
    },
    zh: {
      title: "2026年中网公开赛：阿尔卡拉斯完胜梅德韦杰夫、辛纳击败布云朝克特，梦幻决赛会师钻石球场",
      subtitle: "世界第一与世界第二周日争夺ATP 500冠军头衔，第十次双骄对话如期而至",
      excerpt: "阿尔卡拉斯7-5、6-3击败梅德韦杰夫，卫冕冠军辛纳克服主场观众助威淘汰布云朝克特，携手晋级决赛。",
      body: [
        "北京中网迎来了最具票房号召力的梦幻决赛对决：阿尔卡拉斯与辛纳周六双双闯关成功会师周日争冠战。",
        "阿尔卡拉斯在钻石球场打出攻防转换大师级表现，以7-5、6-3力克前美网冠军梅德韦杰夫，一发得分率高达82%。",
        "辛纳随后顶住了中国新星布云朝克特的强力冲击，以6-3、7-6(3)胜出，将迎来他与阿尔卡拉斯的第十次巡回赛巅峰对话。",
      ],
    },
    ja: {
      title: "チャイナ・オープン2026：アルカラスがメドベージェフ下し、シナーも勝利して北京で夢の決勝が実現",
      subtitle: "世界ランク1位と2位が日曜日、ダイヤモンド・コートでATP500のタイトルを懸けて激突",
      excerpt: "アルカラスが7-5、6-3でメドベージェフを退け、ディフェンディング王者のシナーも決勝進出を決めた。",
      body: [
        "北京のテニスファンが待ち望んだ夢の決勝カードが土曜日の準決勝を経てついに確定しました。",
        "カルロス・アルカラスはダニール・メドベージェフを7-5、6-3で圧倒し、終始試合のペースを握り続けました。",
        "ヤニック・シナーも開催国のブ・ユンチャオケテを6-3、7-6(3)で退け、通算10回目の頂上決戦へと駒を進めました。",
      ],
    },
    ko: {
      title: "2026 차이나 오픈: 알카라스 메드베데프 완파, 시너도 결승 안착하며 베이징 꿈의 결승 성사",
      subtitle: "세계 1위 야닉 시너와 2위 카를로스 알카라스, 일요일 다이아몬드 코트에서 격돌",
      excerpt: "알카라스가 7-5, 6-3으로 메드베데프를 꺾고 시너가 부윈차오커터를 제압하며 열 번째 맞대결을 확정했다.",
      body: [
        "베이징 차이나 오픈이 전 세계 테니스 팬들이 염원하던 최고의 결승 대진을 완성했습니다.",
        "카를로스 알카라스는 다닐 메드베데프를 상대로 82%의 첫 서브 득점률을 앞세워 7-5, 6-3 깔끔한 승리를 거뒀습니다.",
        "디펜딩 챔피언 야닉 시너 역시 홈스타 부윈차오커터를 6-3, 7-6(3)으로 따돌리고 알카라스와의 결승 맞대결에 합류했습니다.",
      ],
    },
    ar: {
      title: "بطولة الصين المفتوحة 2026: ألكاراز يهزم ميدفيديف وسينر يتخطى بو ليضربا موعدا في النهائي الحلم",
      subtitle: "المصنف الأول والثاني عالميا يلتقيان الأحد على الملعب الماسي للمنافسة على لقب بكين.",
      excerpt: "كارلوس ألكاراز يتفوق على دانييل ميدفيديف 7-5 و6-3 ويانيك سينر يفوز على بو ليبلغا النهائي المنتظر.",
      body: [
        "حقق منظمو بطولة الصين المفتوحة النهائي المثالي بعد فوز كارلوس ألكاراز ويانيك سينر في نصف نهائي البطولة السبت.",
        "قدم ألكاراز أداء رائعا تفوق به على ميدفيديف بنتيجة 7-5 و6-3 مستفيدا من دقة إرساله الأول وكراته الساقطة المحكمة.",
        "وتجاوز الإيطالي يانيك سينر حماس الجماهير الصينية بفوزه على بو 6-3 و7-6(3) ليضرب موعدا مع ألكاراز في الفصل العاشر من تنافسهما.",
      ],
    },
  },
  'pga-tour-sanderson-farms-round3-mitchell-leads-2026': {
    fr: {
      title: "Sanderson Farms Championship : Keith Mitchell signe un 64 et prend la tête à -20 après 54 trous",
      subtitle: "Beau Hossler reste en embuscade à un coup à Jackson tandis que le tenant du titre Kevin Yu pointe à -15.",
      excerpt: "Auteur de huit birdies samedi au Country Club of Jackson, Keith Mitchell s'empare des commandes avant le tour final.",
      body: [
        "Le Moving Day a tenu toutes ses promesses à Jackson avec un récital de Keith Mitchell au Country Club.",
        "L'Américain de 32 ans a rendu une carte magistrale de 64 (-8), lui permettant d'afficher un score cumulé de 20 sous le par.",
        "Beau Hossler a signé un 68 sans faute pour rester à un petit coup (-19), promettant une finale explosive dimanche.",
      ],
    },
    es: {
      title: "Sanderson Farms Championship: Keith Mitchell firma un 64 para liderar con -20 tras 54 hoyos",
      subtitle: "Beau Hossler le pisa los talones a un golpe en Jackson y el defensor del título Kevin Yu sigue a tiro.",
      excerpt: "Keith Mitchell embocó ocho birdies este sábado en Misisipi para asumir el liderato en solitario antes del domingo.",
      body: [
        "La jornada de movimiento del Sanderson Farms Championship fue un auténtico espectáculo gracias a Keith Mitchell.",
        "El golfista de Georgia firmó un impecable 64 (-8) con cinco birdies en los primeros siete hoyos para situarse con 20 bajo par.",
        "El líder de las dos primeras rondas, Beau Hossler, se mantuvo firme con un 68 para quedar a un golpe (-19) de cara al domingo.",
      ],
    },
    de: {
      title: "Sanderson Farms Championship: Keith Mitchell spielt 64 und führt nach 54 Löchern mit 20 unter Par",
      subtitle: "Beau Hossler lauert mit einem Schlag Rückstand in Jackson, während Titelverteidiger Kevin Yu bei -15 liegt.",
      excerpt: "Keith Mitchell begeisterte am Samstag im Country Club of Jackson mit acht Birdies und eroberte die alleinige Führung.",
      body: [
        "Der Moving Day im Country Club of Jackson brachte einen Führungswechsel dank einer fehlerfreien 64 von Keith Mitchell.",
        "Der 32-jährige US-Profi schob sich mit 20 unter Par an die Spitze und greift nach seinem zweiten PGA-Tour-Sieg.",
        "Beau Hossler blieb mit einer 68 auf Tuchfühlung bei 19 unter Par, während Titelverteidiger Kevin Yu bei -15 geteilter Dritter ist.",
      ],
    },
    it: {
      title: "Sanderson Farms Championship: Keith Mitchell gira in 64 e vola in testa a -20 dopo 54 buche",
      subtitle: "Beau Hossler insegue a un colpo a Jackson, con il campione in carica Kevin Yu a quota -15.",
      excerpt: "Keith Mitchell ha realizzato otto birdie sabato al Country Club of Jackson portandosi in vetta solitaria.",
      body: [
        "Il Moving Day del Sanderson Farms Championship ha incoronato Keith Mitchell grazie a un giro superlativo da 64 colpi.",
        "Il giocatore della Georgia è salito a -20 totale, mettendo in mostra una straordinaria precisione con i ferri dal tee al green.",
        "Beau Hossler ha risposto con un solido 68 senza bogey per restare a un solo colpo di distanza (-19) in vista del round finale.",
      ],
    },
    pl: {
      title: "Sanderson Farms Championship: Keith Mitchell z wynikiem 64 obejmuje prowadzenie z -20 po 54 dołkach",
      subtitle: "Beau Hossler traci zaledwie jedno uderzenie w Jackson, a broniący tytułu Kevin Yu ma -15.",
      excerpt: "Keith Mitchell popisał się ośmioma birdie w sobotę w Country Club of Jackson, wysuwając się na prowadzenie.",
      body: [
        "Dzień Ruchu na Sanderson Farms Championship przyniósł kapitalny występ Keitha Mitchella w Mississippi.",
        "32-letni Amerykanin zagrał rundę na 64 uderzenia (-8), co dało mu łączny wynik 20 poniżej par po trzech dniach zmagań.",
        "Dotychczasowy lider Beau Hossler uzyskał 68 uderzeń i traci tylko jeden punkt (-19) przed niedzielnym finałem.",
      ],
    },
    zh: {
      title: "桑德森农场锦标赛：米切尔移动日狂飙64杆，总成绩-20杆单挑54洞榜首",
      subtitle: "霍斯勒一杆之差紧随其后，卫冕冠军俞俊安总成绩-15杆保持冲冠希望",
      excerpt: "基斯·米切尔周六在杰克逊乡村俱乐部狂抓八只小鸟，以200杆的总成绩强势反超领跑冲冠组。",
      body: [
        "美巡秋季赛桑德森农场锦标赛迎来火爆移动日，基斯·米切尔凭借精准攻果岭表现打出单轮64杆（-8）。",
        "米切尔在前七洞便抓下五只小鸟，总成绩达到低于标准杆20杆（199杆），单独领跑冲冠积分榜。",
        "前两轮领头羊霍斯勒打出无柏忌的68杆（-19）紧随其后，卫冕冠军中国台北选手俞俊安以-15杆并列第三。",
      ],
    },
    ja: {
      title: "サンダーソン・ファームズ選手権：ミッチェルが64をマークし通算20アンダーで単独首位浮上",
      subtitle: "ホスラーが1打差の19アンダーで追走、前年覇者のケビン・ユーは通算15アンダー",
      excerpt: "キース・ミッチェルが土曜日に8バーディを奪う猛チャージを見せ、通算20アンダーで最終日へ向かう。",
      body: [
        "ジャクソン・カントリークラブでのムービングデーは、キース・ミッチェルの見事なバーディラッシュとなりました。",
        "ミッチェルは8アンダーの64を叩き出し、通算20アンダー（199）でトーナメントリーダーに躍り出ました。",
        "36ホール首位だったボー・ホスラーも68で回り通算19アンダーで追走。日曜日の最終組は激戦が必至です。",
      ],
    },
    ko: {
      title: "샌더슨 팜스 챔피언십: 키스 미첼 64타 맹타, 54홀 통산 20언더파 단독 선두 질주",
      subtitle: "보 호슬러 1타 차 19언더파 추격, 디펜딩 챔피언 케빈 유는 15언더파 3위",
      excerpt: "키스 미첼이 토요일 버디 8개를 몰아치며 20언더파 199타로 잭슨에서 단독 선두로 올라섰다.",
      body: [
        "PGA 투어 가을 시리즈 샌더슨 팜스 챔피언십 무빙데이에서 키스 미첼이 환상적인 샷감을 뽐냈습니다.",
        "미첼은 보기 없이 8언더파 64타를 기록하며 중간 합계 20언더파 199타로 단독 1위에 이름을 올렸습니다.",
        "보 호슬러는 68타를 치며 19언더파로 1타 차 2위를 유지했고, 디펜딩 챔피언 케빈 유는 15언더파 공동 3위에 올랐습니다.",
      ],
    },
    ar: {
      title: "بطولة ساندرسون فارمز: كيث ميتشل يسجل 64 ضربة ويتصدر بـ20 ضربة تحت المعدل بعد 54 حفرة",
      subtitle: "بو هوسلر يلاحقه بفارق ضربة واحدة في جاكسون وحامل اللقب كيفن يو يتربص عند -15.",
      excerpt: "أحرز كيث ميتشل ثماني ضربات بيردي يوم السبت في نادي جاكسون الريفي لينفرد بصدارة الترتيب العام.",
      body: [
        "شهد يوم الحركة في بطولة ساندرسون فارمز تألقا لافتا للأمريكي كيث ميتشل بعد أداء هجومي استثنائي.",
        "أنهى ميتشل الجولة الثالثة مسجلا 64 ضربة (8 تحت المعدل) ليرفع رصيده الإجمالي إلى 20 ضربة تحت المعدل (199).",
        "واكتفى متصدر أول يومين بو هوسلر بتسجيل 68 ضربة ليظل ثانيا بفارق ضربة وحيدة قبل الجولة الختامية الأحد.",
      ],
    },
  },
  'f1-singapore-gp-qualifying-norris-pole-2026': {
    fr: {
      title: "GP de Singapour : Lando Norris décroche une pole magistrale devant Verstappen et Hamilton",
      subtitle: "Le pilote McLaren signe un tour record en 1:29.525 sous les projecteurs tandis que Carlos Sainz sort de piste.",
      excerpt: "Lando Norris a dominé les qualifications à Marina Bay, devançant Max Verstappen de deux dixièmes pour s'offrir la pole.",
      body: [
        "Les qualifications nocturnes à Singapour ont couronné Lando Norris, auteur d'un tour d'anthologie sur le tracé urbain de Marina Bay.",
        "Au volant de sa McLaren, le Britannique a claqué un 1:29.525 en Q3, reléguant Max Verstappen à deux dixièmes et Lewis Hamilton au 3e rang.",
        "La séance a été marquée par le violent crash de Carlos Sainz au virage 19, reléguant Ferrari aux 9e et 10e places sur la grille.",
      ],
    },
    es: {
      title: "GP de Singapur: Lando Norris logra una pole sensacional por delante de Verstappen y Hamilton",
      subtitle: "La estrella de McLaren vuela en 1:29.525 bajo las luces de Marina Bay mientras el accidente de Sainz frena la Q3.",
      excerpt: "Lando Norris superó a Max Verstappen por dos décimas para adjudicarse la pole position en las calles de Singapur.",
      body: [
        "La sesión de clasificación en Marina Bay coronó a Lando Norris tras una vuelta perfecta bajo los reflectores de Singapur.",
        "Norris detuvo el reloj en 1:29.525 con su McLaren para superar por 0.203s a Max Verstappen y dejar a Lewis Hamilton en tercer puesto.",
        "Un fuerte accidente de Carlos Sainz en la curva 19 provocó bandera roja en la Q3, dejando a Ferrari en la novena y décima posición.",
      ],
    },
    de: {
      title: "GP von Singapur: Lando Norris stürmt zur Traum-Pole vor Verstappen und Hamilton",
      subtitle: "McLaren-Star fährt 1:29,525 unter Flutlicht in Marina Bay, während Sainz-Crash Q3 überschattet.",
      excerpt: "Lando Norris sicherte sich mit zwei Zehnteln Vorsprung auf Max Verstappen die Pole-Position beim Nachtrennen in Singapur.",
      body: [
        "Das Qualifying von Singapur unter dem Nachthimmel von Marina Bay endete mit einer Meisterleistung von Lando Norris.",
        "Mit einer Fabelzeit von 1:29,525 sicherte sich der McLaren-Pilot den ersten Startplatz vor Titelrivale Max Verstappen (+0,203s).",
        "Lewis Hamilton stellte seinen Ferrari auf Startplatz drei, während ein Unfall von Carlos Sainz in Kurve 19 die Q3 unterbrach.",
      ],
    },
    it: {
      title: "GP Singapore: Lando Norris conquista una pole stellare davanti a Verstappen e Hamilton",
      subtitle: "Il pilota McLaren brilla in 1:29.525 tra le luci di Marina Bay, mentre l'incidente di Sainz gela la Q3.",
      excerpt: "Lando Norris ha battuto Max Verstappen di due decimi conquistando la pole position per la gara notturna di Singapore.",
      body: [
        "Le qualifiche bagnate dai riflettori di Marina Bay hanno visto trionfare Lando Norris con una McLaren velocissima.",
        "Il crono di 1:29.525 ha consentito al pilota inglese di precedere Max Verstappen di due decimi e Lewis Hamilton di tre decimi.",
        "La sessione è stata interrotta dal pesante impatto a muro di Carlos Sainz in curva 19, che ha costretto le Ferrari al nono e decimo posto.",
      ],
    },
    pl: {
      title: "GP Singapuru: Lando Norris zdobywa rewelacyjne pole position przed Verstappenem i Hamiltonem",
      subtitle: "Gwiazda McLarena uzyskała czas 1:29.525 pod światłami Marina Bay, podczas gdy wypadek Sainza przerwał Q3.",
      excerpt: "Lando Norris okazał się szybszy o dwie dziesiąte od Maxa Verstappena i wystartuje z pole position w Singapurze.",
      body: [
        "Kwalifikacje pod światłami Marina Bay przyniosły popis jazdy Lando Norrisa na trudnym torze ulicznym w Singapurze.",
        "Brytyjczyk wykręcił rewelacyjne 1:29.525, wyprzedzając Maxa Verstappena o 0,203 sekundy i Lewisa Hamiltona o 0,316 sekundy.",
        "Sesję Q3 na kilka minut przerwał groźny wypadek Carlosa Sainza w 19. zakręcie, co zepchnęło Ferrari na odległe pozycje startowe.",
      ],
    },
    zh: {
      title: "F1新加坡大奖赛：诺里斯力压维斯塔潘与汉密尔顿夺得杆位，塞恩斯撞墙引发红旗",
      subtitle: "迈凯伦车手在滨海湾灯光下飙出1分29秒525创纪录飞驰圈锁定首发位置",
      excerpt: "兰多·诺里斯在新加坡排位赛Q3跑出超凡表现，领先维斯塔潘0.203秒夺得个人本赛季第五个杆位。",
      body: [
        "新加坡滨海湾街道赛道周六夜间排位赛高潮迭起，迈凯伦车手诺里斯凭借极致精准的操控夺下杆位。",
        "诺里斯在Q3跑出1分29秒525的惊人成绩，力压红牛车手维斯塔潘与法拉利车手汉密尔顿，锁定周日正赛头排起跑席位。",
        "法拉利车手塞恩斯在19号弯尾部失控撞墙引发红旗中断，勒克莱尔飞驰圈因超限被取消，法拉利正赛只能从第九和第十位起跑。",
      ],
    },
    ja: {
      title: "F1シンガポールGP：ノリスがフェルスタッペンとハミルトンを抑え圧巻のポールポジション獲得",
      subtitle: "マリーナ・ベイのナイトセッションで1分29秒525を記録、サインツのクラッシュでQ3赤旗中断も",
      excerpt: "ランド・ノリスがシンガポール市街地で0.2秒差の完璧なアタックを決め、今季5回目のポールポジションを奪取した。",
      body: [
        "酷暑とコンクリートウォールに囲まれたマリーナ・ベイで、ランド・ノリスが見事なポールポジションを獲得しました。",
        "ノリスはQ3ラストアタックで1分29秒525をマークし、マックス・フェルスタッペンを0.203秒抑えて最前列を確保しました。",
        "ルイス・ハミルトンが3番手に食い込んだ一方、カルロス・サインツのクラッシュで赤旗が出されフェラーリは明暗が分かれました。",
      ],
    },
    ko: {
      title: "F1 싱가포르 GP: 랜도 노리스, 베르스타펜과 해밀턴 꺾고 환상적인 폴포지션 차지",
      subtitle: "마리나 베이 조명 아래 1분 29초 525 랩타임 기록, 사인츠 충돌로 Q3 레드플래그 발생",
      excerpt: "맥라렌의 랜도 노리스가 막스 베르스타펜을 0.2초 차로 제치고 싱가포르 야간 레이스 폴포지션을 획득했다.",
      body: [
        "마리나 베이 시가지 서킷의 야간 예선에서 랜도 노里斯가 압도적인 주행으로 폴포지션을 거머쥐었습니다.",
        "노리스는 Q3 최종 주행에서 1분 29초 525를 기록하며 라이벌 막스 베르스타펜과 루이스 해밀턴을 제치고 맨 앞자리를 차지했습니다.",
        "카를로스 사인츠가 19번 코너에서 방호벽과 충돌하며 레드플래그가 발령되는 등 치열한 드라마가 펼쳐졌습니다.",
      ],
    },
    ar: {
      title: "جائزة سنغافورة الكبرى: لاندو نوريس يقتنص قطب الانطلاق الأول متفوقا على فيرستابن وهاميلتون",
      subtitle: "نجم مكلارين يسجل 1:29.525 تحت أضواء مارينا باي وسط حادث اصطدام قوي لكارلوس ساينز.",
      excerpt: "لاندو نوريس يحرز قطب الانطلاق الأول في سباق سنغافورة الليلي متقدما بفارق عُشرين من الثانية على ماكس فيرستابن.",
      body: [
        "شهدت الحصة التأهيلية لسباق جائزة سنغافورة الكبرى إثارة بالغة تحت أضواء مارينا باي مع تألق لاندو نوريس.",
        "سجل البريطاني زمنا مبهرا قدره 1:29.525 ليضمن الانطلاق من المركز الأول أمام ماكس فيرستابن ولويس هاميلتون.",
        "وتوقفت الحصة الثالثة مؤقتا بالعلم الأحمر إثر حادث اصطدام عنيف للإسباني كارلوس ساينز بالمنعطف رقم 19.",
      ],
    },
  },
  'china-open-2026-final-alcaraz-epic-win-over-sinner': {
    fr: {
      title: "Open de Chine 2026 : Carlos Alcaraz dompte Jannik Sinner dans une finale épique de 3h21",
      subtitle: "L'Espagnol remonte un handicap de 0-3 dans le tie-break décisif pour remporter son 16e titre en carrière.",
      excerpt: "Carlos Alcaraz bat Jannik Sinner 6-7(6), 6-4, 7-6(3) sur le court Diamond à Pékin au terme d'un combat d'anthologie mettant fin à la série de 15 victoires consécutives de l'Italien.",
      body: [
        "La finale de l'Open de Chine a offert un chef-d'œuvre absolu entre Carlos Alcaraz et Jannik Sinner sur le court Diamond.",
        "Alcaraz a signé l'exploit en remontant de 0-3 à 7-3 dans le jeu décisif du troisième set, remportant sept points consécutifs face au numéro un mondial après 3h21 de jeu.",
        "L'Espagnol devient le premier joueur de l'histoire de l'ATP à remporter des tournois ATP 500 sur dur, terre battue et gazon la même année.",
      ],
    },
    es: {
      title: "Abierto de China 2026: Carlos Alcaraz se impone a Jannik Sinner en una épica final de 3h21",
      subtitle: "El español remonta un 0-3 en el tie-break decisivo para alzar su decimosexto título profesional.",
      excerpt: "Carlos Alcaraz superó a Jannik Sinner por 6-7(6), 6-4, 7-6(3) en la pista Diamond de Pekín, cortando la racha de 15 victorias del italiano.",
      body: [
        "La pista Diamond de Pekín presenció uno de los mayores clásicos del tenis moderno entre Carlos Alcaraz y Jannik Sinner.",
        "Alcaraz protagonizó una reacción legendaria en el tie-break final al levantar un 0-3 con siete puntos consecutivos para sellar el triunfo en 3 horas y 21 minutos.",
        "Con este trofeo, el murciano es el primer tenista en ganar torneos ATP 500 en pista dura, tierra batida y hierba en la misma temporada.",
      ],
    },
    de: {
      title: "China Open 2026: Carlos Alcaraz bezwingt Jannik Sinner in dramatischem 3:21-Stunden-Finale",
      subtitle: "Spanier dreht 0:3-Rückstand im entscheidenden Tiebreak und holt seinen 16. Karrieretitel.",
      excerpt: "Carlos Alcaraz schlägt Jannik Sinner mit 6:7(6), 6:4, 7:6(3) auf dem Diamond Court in Peking und beendet Sinners Serie von 15 Siegen.",
      body: [
        "Das Finale der China Open bot das beste Match des Jahres zwischen den beiden Spitzenreitern der Weltrangliste.",
        "Alcaraz triumphierte nach 3 Stunden und 21 Minuten, indem er im Tiebreak des dritten Satzes nach 0:3-Rückstand sieben Punkte in Serie gewann.",
        "Der 21-jährige Spanier ist der erste Spieler der ATP-Geschichte, der in einem Kalenderjahr ATP-500-Titel auf Hartplatz, Sand und Rasen feierte.",
      ],
    },
    it: {
      title: "China Open 2026: Carlos Alcaraz supera Jannik Sinner in un'epica finale di 3 ore e 21 minuti",
      subtitle: "Lo spagnolo rimonta da 0-3 nel tie-break del terzo set e conquista il suo 16° titolo ATP.",
      excerpt: "Carlos Alcaraz sconfigge Jannik Sinner 6-7(6), 6-4, 7-6(3) sul Diamond Court di Pechino, interrompendo la striscia di 15 vittorie dell'azzurro.",
      body: [
        "Sul Diamond Court di Pechino, Carlos Alcaraz e Jannik Sinner hanno disputato una delle finali più spettacolari dell'era recente.",
        "Sinner ha vinto il primo set, ma Alcaraz ha ribaltato il match vincendo sette punti consecutivi nel tie-break finale dopo essere stato sotto 0-3.",
        "Con questo successo Alcaraz si porta sul 6-4 negli scontri diretti con il numero 1 al mondo, chiudendo il 2026 con tre vittorie su tre.",
      ],
    },
    pl: {
      title: "China Open 2026: Carlos Alcaraz pokonał Jannika Sinnera w 3,5-godzinnym dreszczowcu",
      subtitle: "Hiszpan odrobił stratę 0-3 w decydującym tie-breaku i zdobył szesnasty tytuł w karierze.",
      excerpt: "Carlos Alcaraz pokonał Jannika Sinnera 6-7(6), 6-4, 7-6(3) w Pekinie, przerywając serię 15 zwycięstw Włocha po 3 godzinach i 21 minutach walki.",
      body: [
        "Finał China Open na korcie Diamond przyniósł kapitalne widowisko i najwyższy poziom tenisa między dwoma najlepszymi graczami świata.",
        "Alcaraz dokonał niezwykłego wyczynu w tie-breaku trzeciego seta: przegrywając 0-3, wygrał siedem kolejnych punktów i przypieczętował triumf.",
        "Hiszpan został pierwszym tenisistą w historii ATP, który w jednym roku wygrał turnieje rangi ATP 500 na twardej, ziemnej i trawiastej nawierzchni.",
      ],
    },
    zh: {
      title: "2026年中网男单决赛：阿尔卡拉斯历经3小时21分史诗大战逆转辛纳夺冠",
      subtitle: "西班牙天王在决胜盘抢七0-3落后下连赢七分，斩获职业生涯第16座巡回赛冠军",
      excerpt: "阿尔卡拉斯在国家网球中心以6-7(6)、6-4、7-6(3)险胜世界第一辛纳，终结对手15连胜并勇夺中国网球公开赛桂冠。",
      body: [
        "北京中网钻石球场上演了近年来最具统治力的男单决赛对决，阿尔卡拉斯与辛纳激战3小时21分钟。",
        "决胜盘抢七中辛纳一度3-0领先，但阿尔卡拉斯展现大心脏，凭借连续正手攻势连下7分上演不可思议的大逆转。",
        "阿尔卡拉斯由此成为ATP历史上首位在同一赛季于硬地、红土和草地均斩获ATP 500级别冠军的球员。",
      ],
    },
    ja: {
      title: "チャイナ・オープン2026決勝：アルカラスが3時間21分の死闘の末にシナーを破り北京初制覇",
      subtitle: "ファイナルセットのタイブレーク0-3から怒涛の7連続ポイントで通算16個目のタイトル獲得",
      excerpt: "カルロス・アルカラスがヤニック・シナーを6-7(6), 6-4, 7-6(3)で破り、ダイヤモンド・コートでシナーの15連勝を止めて優勝を飾った。",
      body: [
        "北京のダイヤモンド・コートで行われた決勝は、世界ナンバーワンのシナーとアルカラスによる歴史的な名勝負となりました。",
        "最終第3セットのタイブレークで0-3とリードされたアルカラスは、驚異的な反撃で7連続得点を奪い劇的な勝利を収めました。",
        "アルカラスは同一年にハード、クレー、芝の全3サーフェスでATP500を制覇した史上初の選手となりました。",
      ],
    },
    ko: {
      title: "2026 차이나 오픈 결승: 카를로스 알카라스, 3시간 21분 혈투 끝에 야닉 시너 꺾고 베이징 우승",
      subtitle: "마지막 세트 타이브레이크 0-3 열세를 뒤집고 7연속 득점으로 통산 16번째 투어 우승 달성",
      excerpt: "알카라스가 다이아몬드 코트에서 시너를 6-7(6), 6-4, 7-6(3)으로 제압하고 시너의 15연승을 저지하며 베이징 트로피를 들어올렸다.",
      body: [
        "베이징 국가테니스센터 다이아몬드 코트에서 펼쳐진 결승전은 올 시즌 최고의 명승부로 기록되었습니다.",
        "3세트 타이브레이크에서 0-3으로 뒤지던 알카라스는 기적 같은 7연속 득점으로 승부를 결정지었습니다.",
        "이로써 알카라스는 단일 시즌 하드, 클레이, 잔디 모든 코트에서 ATP 500 트로피를 들어올린 최초의 선수가 되었습니다.",
      ],
    },
    ar: {
      title: "بطولة الصين المفتوحة 2026: كارلوس ألكاراز يهزم يانيك سينر في ملحمة استمرت 3 ساعات و21 دقيقة",
      subtitle: "النجم الإسباني يقلب تأخره 0-3 في شوط كسر التعادل الفاصل ليتوج بلقبه السادس عشر في مسيرته.",
      excerpt: "كارلوس ألكاراز يتفوق على يانيك سينر بنتيجة 6-7(6) و6-4 و7-6(3) على الملعب الماسي في بكين منهيا سلسلة انتصارات الإيطالي.",
      body: [
        "شهد الملعب الماسي في بكين قمة كروية وتنسية لا تنسى امتدت لأكثر من ثلاث ساعات بين ألكاراز وسينر.",
        "وفجر ألكاراز مفاجأة كبرى في الشوط الفاصل الحاسم حين حصد سبع نقاط متتالية بعد تأخره 0-3 ليحسم اللقب العالمي.",
        "وأصبح الإسباني الشاب أول لاعب في تاريخ بطولات رابطة المحترفين يتوج بألقاب فئة 500 نقطة على الأراضي الصلبة والترابية والعشبية في عام واحد.",
      ],
    },
  },
  'f1-singapore-gp-race-norris-crushing-victory-2026': {
    fr: {
      title: "GP de Singapour : Lando Norris écrase la course et s'impose avec 20 secondes d'avance sur Verstappen",
      subtitle: "Le Britannique mène les 62 tours sous les projecteurs de Marina Bay et signe son troisième succès en 2026.",
      excerpt: "Lando Norris a transformé sa pole en triomphe magistral à Singapour, devançant Max Verstappen de 20.945 secondes pour consolider l'avance de McLaren.",
      body: [
        "Dans l'étuve de Marina Bay, Lando Norris a livré une démonstration totale en dominant le Grand Prix de Singapour de bout en bout.",
        "Au volant d'une McLaren intouchable, le pilote anglais a repoussé Max Verstappen à plus de vingt secondes sur la ligne d'arrivée.",
        "Avec la 3e place d'Oscar Piastri, McLaren empoche 40 points au championnat des constructeurs et conforte son leadership.",
      ],
    },
    es: {
      title: "GP de Singapur: Lando Norris arrasa en Marina Bay y vence con 20 segundos de ventaja sobre Verstappen",
      subtitle: "El piloto de McLaren lidera las 62 vueltas nocturnas para sumar su tercer triunfo de la temporada.",
      excerpt: "Lando Norris dominó el Gran Premio de Singapur de principio a fin, superando a Max Verstappen por 20.945 segundos en una exhibición de McLaren.",
      body: [
        "Bajo los focos de Marina Bay, Lando Norris firmó la carrera más dominante de su trayectoria en la Fórmula 1.",
        "Norris controló la salida y rodó a un ritmo inalcanzable, cruzando la meta con casi 21 segundos de renta sobre Verstappen.",
        "El podio completado por Oscar Piastri en tercera posición otorgó 40 valiosos puntos a McLaren en el Mundial de Constructores.",
      ],
    },
    de: {
      title: "GP von Singapur: Lando Norris deklassiert Konkurrenz mit 20 Sekunden Vorsprung auf Verstappen",
      subtitle: "McLaren-Star führt alle 62 Runden unter Flutlicht in Marina Bay und feiert dritten Saisonsieg.",
      excerpt: "Lando Norris dominierte den Großen Preis von Singapur souverän von der Pole Position und schlug Max Verstappen um 20,945 Sekunden.",
      body: [
        "Auf dem herausfordernden Stadtkurs von Marina Bay zeigte Lando Norris eine fahrerische Glanzleistung.",
        "Norris kontrollierte das Rennen von der ersten bis zur letzten Runde und verwies Max Verstappen um fast 21 Sekunden auf Platz zwei.",
        "Oscar Piastri komplettierte als Dritter das hervorragende McLaren-Ergebnis mit insgesamt 40 Punkten an einem Wochenende.",
      ],
    },
    it: {
      title: "GP Singapore: Lando Norris trionfa a Marina Bay con oltre 20 secondi di vantaggio su Verstappen",
      subtitle: "L'inglese della McLaren comanda tutti i 62 giri nella notte asiatica e centra il terzo successo stagionale.",
      excerpt: "Lando Norris ha dominato il Gran Premio di Singapore dalla pole position, battendo Max Verstappen di 20.945 secondi.",
      body: [
        "Sul circuito cittadino di Singapore, Lando Norris ha disputato una corsa perfetta, infliggendo distacchi pesanti a tutti i rivali.",
        "Il pilota britannico ha tenuto un passo irresistibile per 62 tornate, precedendo Verstappen di oltre venti secondi e Piastri di quaranta.",
        "La McLaren consolida così la vetta nel Campionato Costruttori con un bottino pieno di 40 punti nel weekend.",
      ],
    },
    pl: {
      title: "GP Singapuru: Lando Norris nokautuje rywali i wygrywa z przewagą 20 sekund nad Verstappenem",
      subtitle: "Kierowca McLarena prowadził przez wszystkie 62 okrążenia pod światłami Marina Bay, zdobywając trzecie zwycięstwo w sezonie.",
      excerpt: "Lando Norris zamienił pole position w bezdyskusyjne zwycięstwo w Singapurze, finiszując 20,945 sekundy przed Maxem Verstappenem.",
      body: [
        "Nocny wyścig na ulicach Singapuru przyniósł całkowitą dominację Lando Norrisa i bolidu McLarena.",
        "Brytyjczyk nie oddał prowadzenia ani na moment, narzucając tempo nieosiągalne dla urzędującego mistrza świata Maxa Verstappena.",
        "Trzecie miejsce Oscara Piastriego przypieczętowało dublet na podium dla ekipy z Woking i powiększyło ich przewagę w klasyfikacji zespołowej.",
      ],
    },
    zh: {
      title: "F1新加坡大奖赛正赛：诺里斯狂揽20秒优势拔得头筹，力压维斯塔潘夺赛季第三冠",
      subtitle: "迈凯伦车手在滨海湾夜战中领跑全程62圈，皮亚斯特里夺得季军迈凯伦双双登台",
      excerpt: "诺里斯以绝对优势将杆位转化为新加坡大奖赛正赛胜利，领先维斯塔潘20.945秒冲线，迈凯伦车队积分榜领先优势进一步扩大。",
      body: [
        "在滨海湾潮湿闷热的街道赛道上，诺里斯用极具统治力的速度统治了整场62圈的比赛。",
        "诺里斯发车守住领跑位置后一路绝尘，最终以近21秒的巨大优势力压红牛车手维斯塔潘夺魁。",
        "队友皮亚斯特里从第五位追至第三，迈凯伦单站揽下40分，在车队总冠军争夺中占据绝对主动。",
      ],
    },
    ja: {
      title: "F1シンガポールGP決勝：ノリスが圧巻の独走劇でフェルスタッペンに20秒差をつけ今季3勝目",
      subtitle: "マリーナ・ベイのナイトレース全62周を支配、ピアストリも3位に入りマクラーレン大勝",
      excerpt: "ランド・ノリスがポール・トゥ・ウィンを飾り、マックス・フェルスタッペンに20.945秒の大差をつけてシンガポールGPを制覇した。",
      body: [
        "酷暑と夜間照明が交錯するマリーナ・ベイで、ランド・ノリスが異次元のスピードを見せつけ完勝しました。",
        "ノリスは全62周をリードし、フェルスタッペンに対して20秒以上のセーフティマージンを築いてチェッカーを受けました。",
        "オスカー・ピアストリが3位表彰台に登り、マクラーレンは1レースで40ポイントを荒稼ぎして選手権首位を固めました。",
      ],
    },
    ko: {
      title: "F1 싱가포르 GP 결승: 랜도 노리스, 베르스타펜에 20초 차 압승 거두며 시즌 3승 수확",
      subtitle: "마리나 베이 62랩 전 구간을 완벽 지배, 피아스트리 3위로 맥라렌 더블 포디엄 완성",
      excerpt: "랜도 노리스가 폴투윈을 달성하며 막스 베르스타펜을 20.945초 차로 따돌리고 싱가포르 그랑프리 우승 트로피를 차지했다.",
      body: [
        "야간 도심 서킷인 마리나 베이에서 랜도 노리스는 그야말로 무결점 독주 레이스를 선보였습니다.",
        "출발부터 선두를 유지한 노리스는 타이어 관리와 압도적인 페이스로 베르스타펜을 20초 이상 밀어냈습니다.",
        "팀 동료 오스카 피아스트리가 3위를 기록하며 맥라렌은 이번 주말에만 40점을 추가해 컨스트럭터 선두를 굳혔습니다.",
      ],
    },
    ar: {
      title: "سباق جائزة سنغافورة الكبرى: لاندو نوريس يسحق المنافسين ويفوز بفارق 20 ثانية عن فيرستابن",
      subtitle: "نجم مكلارين يتصدر جميع لفات السباق الـ62 تحت أضواء مارينا باي ويحصد فوزه الثالث هذا الموسم.",
      excerpt: "لاندو نوريس يترجم انطلاقه من المركز الأول إلى انتصار ساحق في سنغافورة متفوقا بـ20.945 ثانية على ماكس فيرستابن.",
      body: [
        "قدم لاندو نوريس أداء استثنائيا على حلبة مارينا باي الصعبة مسيطرا على مجريات السباق الليلي من البداية حتى النهاية.",
        "تفوق السائق البريطاني على بطل العالم ماكس فيرستابن بفارق تجاوز عشرين ثانية بفضل وتيرة مكلارين الفائقة.",
        "واحتل زميله أوسكار بياستري المركز الثالث ليعزز فريق مكلارين صدارته في بطولة الصانعين بعد حصد 40 نقطة ثمينة.",
      ],
    },
  },
  'pga-tour-sanderson-farms-final-kevin-yu-playoff-victory-2026': {
    fr: {
      title: "Sanderson Farms : Kevin Yu s'offre son premier titre PGA Tour en playoff face à Beau Hossler",
      subtitle: "Deux birdies consécutifs au 18 permettent au joueur de 26 ans de s'imposer en mort subite à Jackson.",
      excerpt: "Kevin Yu a rendu une carte de 67 pour égaler Beau Hossler à -23 avant de rentrer un putt décisif au premier trou de playoff.",
      body: [
        "Le Country Club de Jackson a sacré un nouveau vainqueur sur le PGA Tour avec le triomphe au bout du suspense de Kevin Yu.",
        "Auteur d'un birdie au 72e trou pour arracher le playoff contre Beau Hossler, Yu a récidivé au premier trou supplémentaire avec un putt de cinq pieds.",
        "Cette première victoire en carrière lui ouvre les portes du Masters et lui assure deux années d'exemption sur le circuit américain.",
      ],
    },
    es: {
      title: "Sanderson Farms: Kevin Yu logra su primer título del PGA Tour en el playoff ante Beau Hossler",
      subtitle: "Dos birdies consecutivos en el hoyo 18 coronan al taiwanés de 26 años en el Country Club de Jackson.",
      excerpt: "Kevin Yu firmó 67 golpes para empatar con Beau Hossler en 23 bajo par y embocó un putt de metro y medio en el desempate para ganar.",
      body: [
        "El desenlace del Sanderson Farms Championship deparó un duelo electrizante entre Kevin Yu y Beau Hossler en Misisipi.",
        "Yu embocó sendos birdies en el hoyo 18, primero para forzar el desempate en -23 y minutos después para sentenciar su primer título en el circuito.",
        "El triunfo le otorga dos años de exención en el PGA Tour e invitaciones para el Masters de Augusta y el PGA Championship.",
      ],
    },
    de: {
      title: "Sanderson Farms: Kevin Yu holt ersten PGA-Tour-Titel im Playoff gegen Beau Hossler",
      subtitle: "Zwei Birdies an Loch 18 in Folge bringen dem 26-Jährigen den Durchbruch in Jackson.",
      excerpt: "Kevin Yu spielte eine 67, glich bei 23 unter Par zu Beau Hossler auf und siegte am ersten Extraloch mit einem Birdie-Putt.",
      body: [
        "Das Finale im Country Club of Jackson endete mit einem dramatischen Stechen zwischen Kevin Yu und Beau Hossler.",
        "Yu lochte am 72. Loch zum Birdie ein, um mit 23 unter Par gleichzuziehen, und wiederholte das Kunststück am ersten Playoff-Loch.",
        "Damit sicherte sich der Taiwaner seine volle Tourkarte bis 2028 und die Startberechtigung für das Masters 2027.",
      ],
    },
    it: {
      title: "Sanderson Farms: Kevin Yu vince il primo titolo sul PGA Tour al playoff contro Beau Hossler",
      subtitle: "Due birdie consecutivi alla buca 18 regalano il trionfo al 26enne taiwanese a Jackson.",
      excerpt: "Kevin Yu ha chiuso a -23 dopo un giro in 67, superando Beau Hossler alla prima buca di spareggio con un birdie da un metro e mezzo.",
      body: [
        "Il Country Club di Jackson ha incoronato Kevin Yu, autore di un finale magistrale nel torneo autunnale del PGA Tour.",
        "Dopo aver pareggiato il punteggio di Hossler a -23 grazie a un birdie alla 18, Yu ha ripetuto il colpo decisivo nel playoff per conquistare il trofeo.",
        "La vittoria garantisce a Yu l'esenzione fino al 2028 e la partecipazione al prossimo Masters di Augusta.",
      ],
    },
    pl: {
      title: "Sanderson Farms: Kevin Yu wygrywa pierwszy tytuł PGA Tour w dogrywce z Beau Hosslerem",
      subtitle: "Dwa kolejne birdie na 18. dołku dały 26-latkowi upragnione zwycięstwo w Jackson.",
      excerpt: "Kevin Yu uzyskał wynik -23 po rundzie 67 uderzeń i pokonał Beau Hosslera na pierwszym dołku dogrywki na Country Club of Jackson.",
      body: [
        "Turniej Sanderson Farms przyniósł niezwykłe emocje na finiszu, gdy Kevin Yu i Beau Hossler zakończyli 72 dołki z wynikiem 23 poniżej par.",
        "Yu popisał się fantastycznym finiszem, trafiając birdie na 18. dołku regulaminowej gry, a następnie powtarzając ten wyczyn w dogrywce z odległości 1,5 metra.",
        "Zwycięstwo zapewnia reprezentantowi Tajwanu dwuletnie zwolnienie z kwalifikacji do PGA Tour oraz zaproszenie na turniej Masters.",
      ],
    },
    zh: {
      title: "美巡桑德森农场锦标赛：俞俊安加洞赛力克霍斯勒，摘得个人美巡赛首冠",
      subtitle: "26岁中国台北名将在杰克逊第18号洞两度抓鸟，问鼎总成绩低于标准杆23杆",
      excerpt: "俞俊安在决赛轮打出67杆与霍斯勒进入加洞赛，随后在加洞首洞推进5英尺抓鸟绝杀，捧起职业生涯首座美巡赛奖杯。",
      body: [
        "杰克逊乡村俱乐部周日上演精彩对决，中国台北选手俞俊安凭借关键时刻的大心脏发挥夺得美巡赛首冠。",
        "俞俊安在第72洞精准攻果岭抓鸟追至-23平，随后在18号洞的第一个加洞赛中再次推进5英尺小鸟推完成绝杀。",
        "这场胜利为他锁定了直到2028赛季的美巡赛参赛资格以及2027年美国大师赛的参赛邀请。",
      ],
    },
    ja: {
      title: "サンダーソン・ファームズ選手権：ケビン・ユーがプレーオフでホスラーを下しPGAツアー初優勝",
      subtitle: "18番ホールで連続バーディを奪い、通算23アンダーで劇的なツアー初勝利を掴む",
      excerpt: "ケビン・ユーが最終日67をマークしてボー・ホスラーと並び、プレーオフ1ホール目でバーディパットを沈めて優勝を果たした。",
      body: [
        "ジャクソン・カントリークラブで行われたサンダーソン・ファームズ選手権は、ケビン・ユーの劇的な初優勝で幕を閉じました。",
        "正規の72ホール目で起死回生のバーディを奪ったユーは、プレーオフ1ホール目でも約1.5メートルのバーディを沈めました。",
        "台湾出身選手としてツアー史上3人目の勝者となり、マスターズ出場権と2年間のシード権を獲得しました。",
      ],
    },
    ko: {
      title: "샌더슨 팜스 챔피언십: 케빈 유, 보 호슬러 꺾고 연장전 끝에 PGA 투어 생애 첫 우승",
      subtitle: "18번 홀에서 잇단 버디를 낚아채며 통산 23언더파로 잭슨에서 감격의 첫 트로피 번쩍",
      excerpt: "케빈 유가 최종 라운드 67타를 기록해 보 호슬러와 동타를 이룬 뒤, 연장 첫 번째 홀에서 버디 퍼트를 성공시키며 우승했다.",
      body: [
        "미시시피주 잭슨 컨트리클럽에서 열린 결승전에서 26세의 케빈 유가 생애 첫 PGA 투어 정상에 올랐습니다.",
        "유는 18번 홀에서 연속 버디를 낚으며 연장전에 돌입했고, 연장 첫 홀에서 침착하게 5피트 버디를 떨구며 승리를 확정했습니다.",
        "이 승리로 유는 2028년까지 투어 출전권을 확보함과 동시에 2027년 마스터스 출전 티켓을 거머쥐었습니다.",
      ],
    },
    ar: {
      title: "بطولة ساندرسون فارمز: كيفن يو يتوج بأول ألقابه في جولة بي جي إيه بعد حسم التمايز أمام هوفلر",
      subtitle: "اللاعب البالغ 26 عاما يسجل ضربتي بيردي حاسمتين في الحفرة 18 ليتوج بطلا في جاكسون بمجموع 23 ضربة تحت المعدل.",
      excerpt: "كيفن يو يسجل 67 ضربة في الجولة الأخيرة ليتعادل مع بو هوسلر قبل أن يحسم الجولة الإضافية بضربة بيردي متقنة.",
      body: [
        "شهد نادي جاكسون في ميسيسيبي نهاية درامية بتتويج التايواني كيفن يو بأول ألقابه في جولة رابطة لاعبي الجولف المحترفين.",
        "وسجل يو ضربة بيردي عند الحفرة 72 ليعادل رصيد منافسه هوسلر، قبل أن يحسم اللقاء في الحفرة الفاصلة الأولى بضربة حاسمة.",
        "ويمنح هذا اللقب يو إعفاء لمدة عامين في الجولة العالمية مع بطاقة دعوة مباشرة لبطولة الماسترز لعام 2027.",
      ],
    },
  },
  'nfl-week4-snf-ravens-blowout-bills-35-10-henry-2026': {
    fr: {
      title: "NFL 4e semaine SNF : Derrick Henry marche sur les Bills et offre un festival 35-10 aux Ravens",
      subtitle: "Le running back vedette cumule 199 yards au sol et deux touchdowns, dont une course record de 87 yards.",
      excerpt: "Derrick Henry a fait exploser la défense de Buffalo avec 199 yards au sol tandis que Lamar Jackson totalisait trois touchdowns pour infliger aux Bills leur première défaite de l'année.",
      body: [
        "Le choc de dimanche soir a tourné à la démonstration pour les Baltimore Ravens, vainqueurs 35-10 des Buffalo Bills jusqu'alors invaincus.",
        "Derrick Henry a donné le ton dès le premier jeu offensif avec un touchdown éclair de 87 yards avant de terminer la soirée avec 199 yards au sol.",
        "La défense de Baltimore a complètement neutralisé Josh Allen, sacké trois fois et limité à zéro touchdown marqué.",
      ],
    },
    es: {
      title: "NFL Semana 4 SNF: Derrick Henry desata su poder y los Ravens arrollan 35-10 a los invictos Bills",
      subtitle: "El corredor estelar firma 199 yardas terrestres y dos touchdowns, incluida una escapada de 87 yardas en la primera jugada.",
      excerpt: "Baltimore Ravens arrolló 35-10 a Buffalo Bills con una noche descomunal de Derrick Henry y tres anotaciones de Lamar Jackson.",
      body: [
        "El M&T Bank Stadium presenció una exhibición de poderío físico de los Ravens, que aplastaron a unos Bills que llegaban con 3-0.",
        "Derrick Henry protagonizó una carrera histórica de 87 yardas en la primera acción ofensiva de Baltimore y terminó sumando 199 yardas terrestres.",
        "Josh Allen fue maniatado por la defensa de Baltimore, sufriendo tres capturas y quedándose sin pases de anotación.",
      ],
    },
    de: {
      title: "NFL Woche 4 SNF: Derrick Henry überrollt die Bills beim 35:10-Kantersieg der Ravens",
      subtitle: "Star-Runningback erläuft 199 Yards und zwei Touchdowns, darunter ein 87-Yard-Lauf im ersten Play.",
      excerpt: "Derrick Henry führte die Baltimore Ravens mit 199 Rushing-Yards zu einem überzeugenden 35:10-Sieg über die bis dahin ungeschlagenen Buffalo Bills.",
      body: [
        "Das Sunday Night Football-Spiel entwickelte sich zu einer Demonstration der Ravens-Laufstärke gegen Buffalo.",
        "Gleich im ersten Offensivzug durchbrach Derrick Henry die Abwehrreihe für einen 87-Yard-Touchdown und beendete die Partie mit 199 Rushing-Yards.",
        "Lamar Jackson steuerte drei Touchdowns bei, während die Ravens-Defense Josh Allen keinen einzigen Touchdown erlaubte.",
      ],
    },
    it: {
      title: "NFL Week 4 SNF: Derrick Henry domina e i Ravens travolgono i Bills imbattuti per 35-10",
      subtitle: "Il running back mette a segno 199 yard su corsa e due mete, compresa una fuga da 87 yard.",
      excerpt: "I Baltimore Ravens hanno inflitto la prima sconfitta stagionale ai Buffalo Bills con un netto 35-10 guidato da Derrick Henry e Lamar Jackson.",
      body: [
        "All'M&T Bank Stadium è andata in scena una lezione di football dei Baltimore Ravens, capaci di imporsi 35-10 sui quotati Bills.",
        "Derrick Henry ha firmato una corsa da 87 yard al primo possesso offensivo, terminando la gara con 199 yard e due mete complessive.",
        "Lamar Jackson ha registrato tre mete totali, mentre Josh Allen è stato limitato senza alcuna meta personale.",
      ],
    },
    pl: {
      title: "NFL Tydzień 4 SNF: Derrick Henry niszczy Bills, Ravens wygrywają 35-10 z niepokonanym rywalem",
      subtitle: "Doświadczony running back zdobył 199 jardów biegowych i dwa przyłożenia, w tym 87-jardowy bieg w pierwszej akcji.",
      excerpt: "Baltimore Ravens rozbili dotąd niepokonanych Buffalo Bills 35-10 dzięki popisowi Derricka Henry'ego i trzem przyłożeniom Lamara Jacksona.",
      body: [
        "Mecz Sunday Night Football okazał się popisem siłowego futbolu w wykonaniu gospodarzy z Baltimore.",
        "Derrick Henry otworzył spotkanie najdłuższym biegiem na przyłożenie w historii Ravens na 87 jardów i zakończył mecz ze 199 jardami na koncie.",
        "Lamar Jackson kontrolował przebieg meczu podaniami, podczas gdy defensywa Ravens kompletnie zneutralizowała Josha Allena.",
      ],
    },
    zh: {
      title: "NFL第四周周日夜赛：亨利狂砍199码两达阵，乌鸦35-10大胜送比尔赛季首败",
      subtitle: "亨利开场首档进攻即狂奔87码达阵创队史纪录，杰克逊独造三达阵打崩比尔防线",
      excerpt: "巴尔的摩乌鸦在周日夜赛展现统治力，亨利爆砍199码领衔地面风暴，以35-10送此前三连胜的水牛城比尔首场惨败。",
      body: [
        "在M&T银行体育场，巴尔的摩乌鸦打出了一场教科书级别的路面进攻碾压局，35-10痛击水牛城比尔。",
        "德里克·亨利在开场第一档进攻中便完成87码惊天长途奔袭达阵，全场狂揽199码冲球及两记达阵。",
        "四分卫拉马尔·杰克逊传冲结合贡献三达阵，而乌鸦防守组完成三次擒杀并让阿伦全场零达阵入账。",
      ],
    },
    ja: {
      title: "NFL第4週SNF：デリック・ヘンリーが199ヤード激走、レイブンズが開幕3連勝のビルズを35-10で粉砕",
      subtitle: "開始早々に87ヤードの独走TDランを披露、ラマー・ジャクソンも3TDで攻守に圧倒",
      excerpt: "デリック・ヘンリーが199ラン獲得ヤードと2TDを記録し、ボルティモア・レイブンズが無敗のバッファロー・ビルズを35-10で撃破した。",
      body: [
        "全米注目のサンデーナイトフットボールは、ボルティモア・レイブンズの圧倒的なランオフェンス劇となりました。",
        "ヘンリーは試合最初のプレーで球団記録となる87ヤードTDランを決め、計199ヤードを荒稼ぎしました。",
        "ラマー・ジャクソンが3つのタッチダウンに関与する一方、レイブンズ守備陣はジョシュ・アレンを完全に封じ込めました。",
      ],
    },
    ko: {
      title: "NFL 4주차 SNF: 데릭 헨리 199야드 폭주, 레이븐스가 무패 빌스를 35-10으로 완파",
      subtitle: "첫 공격에서 87야드 터치다운 질주 성공, 라마 잭슨 3TD 합작하며 완승 견인",
      excerpt: "볼티모어 레이븐스가 데릭 헨리의 199 러싱 야드 2TD 맹활약에 힘입어 무패 행진을 달리던 버팔로 빌스를 35-10으로 제압했다.",
      body: [
        "M&T 뱅크 스타디움에서 열린 일요 야간 경기에서 볼티모어 레이븐스가 버팔로를 완벽하게 제압했습니다.",
        "데릭 헨리는 팀의 첫 공격 플레이에서 구단 역사상 최장인 87야드 터치다운 러시를 터뜨리는 등 199 러싱 야드를 쓸어담았습니다.",
        "잭슨의 효율적인 패스와 강력한 수비진의 압박에 조시 앨런은 단 하나의 터치다운도 기록하지 못하고 완패했습니다.",
      ],
    },
    ar: {
      title: "دوري كرة القدم الأمريكية الأسبوع 4: ديريك هنري يتألق وري Raven يسحق بيلز 35-10",
      subtitle: "النجم المخضرم يسجل 199 ياردة اندفاعية وهبوطين أحدهما من ركضة تاريخية لمسافة 87 ياردة.",
      excerpt: "فاز بالتيمور ريفنز بنتيجة عريضة 35-10 على بافلو بيلز الذي تلقى خسارته الأولى بفضل أداء خارق من ديريك هنري ولمار جاكسون.",
      body: [
        "لقن فريق بالتيمور ريفنز منافسه بافلو بيلز درسا كرويا قاسيا بالفوز عليه 35-10 في ختام الأسبوع الرابع.",
        "وانطلق ديريك هنري في أول لعبة هجومية ليركض 87 ياردة نحو منطقة الهبوط محققا رقما قياسيا في تاريخ النادي ومسجلا 199 ياردة في اللقاء.",
        "وأحكم دفاع ريفنز الخناق على جوش ألين وحرمه من تسجيل أي هبوط طوال فترات المواجهة.",
      ],
    },
  },
  'wnba-semifinals-game1-liberty-lynx-take-leads-2026': {
    fr: {
      title: "Demi-finales WNBA Match 1 : Breanna Stewart porte le Liberty, Napheesa Collier et les Lynx résistent au Fever",
      subtitle: "New York domine Las Vegas 87-77 avec 34 points de Stewart tandis que Minnesota bat Indiana 88-82.",
      excerpt: "Breanna Stewart a marqué 34 points pour guider New York vers la victoire contre les Aces, tandis que Napheesa Collier a scellé le succès des Lynx face à Caitlin Clark.",
      body: [
        "L'ouverture des demi-finales WNBA a tenu toutes ses promesses dimanche à Brooklyn et Minneapolis.",
        "Au Barclays Center, Breanna Stewart a été impériale avec 34 points pour infliger une défaite 87-77 aux doubles championnes en titre de Las Vegas.",
        "Au Target Center, Minnesota s'est imposé 88-82 face à Indiana malgré les 22 points et 9 passes de Caitlin Clark, grâce à un grand match de Collier (28 points).",
      ],
    },
    es: {
      title: "Semifinales WNBA Partido 1: Breanna Stewart lidera al Liberty, Collier y las Lynx frenan al Fever",
      subtitle: "New York supera 87-77 a Las Vegas con 34 puntos de Stewart, mientras Minnesota vence 88-82 a Indiana.",
      excerpt: "Breanna Stewart brilló con 34 puntos en el triunfo de New York sobre las Aces, mientras Napheesa Collier guio a Minnesota ante Caitlin Clark.",
      body: [
        "El inicio de las semifinales de la WNBA brindó una jornada apasionante en Nueva York y Mineápolis.",
        "Stewart comandó a las Liberty con 34 puntos y 8 rebotes para superar a A'ja Wilson y a las Aces por 87-77.",
        "En el Target Center, las Lynx aguantaron el empuje final de Caitlin Clark y sellaron el 88-82 con 28 puntos de Collier.",
      ],
    },
    de: {
      title: "WNBA-Halbfinale Spiel 1: Breanna Stewart führt Liberty an, Collier und Lynx stoppen das Fever",
      subtitle: "New York schlägt Las Vegas mit 87:77 dank 34 Stewart-Punkten, Minnesota siegt 88:82 gegen Indiana.",
      excerpt: "Breanna Stewart überragte mit 34 Punkten beim Liberty-Sieg über die Aces, während Napheesa Collier die Lynx zum 88:82-Auftaktsieg führte.",
      body: [
        "Der Auftakt der WNBA-Halbfinals bot hochklassigen Basketball in Brooklyn und Minneapolis.",
        "Stewart war beim 87:77-Erfolg der Liberty über die Aces mit 34 Punkten die dominierende Spielerin auf dem Parkett.",
        "Minnesota wehrte einen späten Sturmlauf von Caitlin Clark (22 Punkte, 9 Assists) ab und gewann dank Napheesa Colliers 28 Punkten mit 88:82.",
      ],
    },
    it: {
      title: "Semifinali WNBA Gara 1: Breanna Stewart trascina le Liberty, Collier e le Lynx domano le Fever",
      subtitle: "New York supera Las Vegas 87-77 con 34 punti di Stewart, Minnesota batte Indiana 88-82.",
      excerpt: "Breanna Stewart ha incantato con 34 punti nella vittoria delle Liberty sulle Aces, mentre Napheesa Collier ha guidato le Lynx contro Caitlin Clark.",
      body: [
        "Gara 1 delle semifinali WNBA ha regalato emozioni fortissime sia a New York che a Minneapolis.",
        "Le New York Liberty hanno battuto le bi-campionesse Las Vegas Aces per 87-77 grazie a una straordinaria Stewart da 34 punti.",
        "Le Lynx hanno resistito al ritorno di Caitlin Clark nel finale vincendo 88-82 con 28 punti di Napheesa Collier.",
      ],
    },
    pl: {
      title: "Półfinały WNBA Mecz 1: Breanna Stewart prowadzi Liberty, Collier i Lynx powstrzymują Fever",
      subtitle: "New York pokonuje Las Vegas 87-77 dzięki 34 punktom Stewart, Minnesota wygrywa z Indianą 88-82.",
      excerpt: "Breanna Stewart rzuciła 34 punkty w wygranym meczu z Aces, a Napheesa Collier poprowadziła Lynx do triumfu nad Caitlin Clark i Fever.",
      body: [
        "Początek półfinałów WNBA przyniósł kapitalne mecze na parkietach w Nowym Jorku i Minneapolis.",
        "W Barclays Center Breanna Stewart rozegrała znakomity mecz z 34 punktami, prowadząc Liberty do triumfu 87-77 nad Las Vegas Aces.",
        "W Target Center Minnesota Lynx utrzymała przewagę i wygrała 88-82 mimo 22 punktów i 9 asyst debiutującej w fazie play-off Caitlin Clark.",
      ],
    },
    zh: {
      title: "WNBA半决赛G1：斯图尔特狂轰34分自由人拔头筹，科利尔28分山猫力克狂热",
      subtitle: "纽约自由人87-77击退王牌，明尼苏达山猫88-82险胜克拉克领衔的狂热占得先机",
      excerpt: "斯图尔特砍下34分带领自由人主场击败卫冕冠军王牌，科利尔拿下28分助山猫末节阻击克拉克的狂轰滥炸。",
      body: [
        "2026年WNBA半决赛周日打响，纽约自由人与明尼苏达山猫双双守卫主场取得系列赛1-0领先。",
        "斯图尔特在巴克莱中心独得34分8篮板，帮助自由人87-77力克两连冠的拉斯维加斯王牌。",
        "在标靶中心，尽管克拉克贡献22分9助攻并在末节扳平比分，科利尔用关键防守和28分锁定胜局，山猫88-82惊险过关。",
      ],
    },
    ja: {
      title: "WNBA準決勝第1戦：スチュワートが34得点でリバティを牽引、コリアーとリンクスがフィーバーを撃破",
      subtitle: "ニューヨークが87-77でエースズに先勝、ミネソタはクラークの猛追を振り切り88-82で勝利",
      excerpt: "ブレアナ・スチュワートが34得点を奪いリバティがエースズを下し、ナフィーサ・コリアーが28得点でリンクスを白星発進に導いた。",
      body: [
        "WNBAセミファイナル第1戦は、ブルックリンとミネアポリスで熱狂的な名勝負となりました。",
        "リバティのスチュワートは34得点・8リバウンドの大活躍で連覇中のラスベガス・エースズを87-77で圧倒しました。",
        "リンクスはケイトリン・クラークの22得点9アシストに苦しみながらも、コリアーの攻守にわたる活躍で88-82で逃げ切りました。",
      ],
    },
    ko: {
      title: "WNBA 4강 1차전: 브리아나 스튜어트 34점 폭발 리버티 선승, 콜리어의 링스 피버 제압",
      subtitle: "뉴욕이 87-77로 에이시스를 완파하고, 미네소타는 클라크의 맹추격을 따돌리며 88-82 승리",
      excerpt: "스튜어트가 34점을 퍼부으며 리버티를 승리로 이끌었고, 나피사 콜리어가 28점을 올리며 인디애나 피버를 꺾었다.",
      body: [
        "WNBA 플레이오프 준결승 1차전 더블헤더에서 홈팀 뉴욕 리버티와 미네소타 링스가 나란히 1승을 챙겼습니다.",
        "바클레이스 센터에서 스튜어트는 34점을 기록하며 지난 시즌 챔피언 라스베이거스를 87-77로 잠재웠습니다.",
        "타깃 센터에서는 케이틀린 클라크가 22점 9어시스트로 분전했으나 콜리어의 클러치 활약에 힘입은 링스가 88-82로 승리했습니다.",
      ],
    },
    ar: {
      title: "نصف نهائي دوري السيدات لكرة السلة المباراة 1: ستيوارت تقود ليبرتي للفوز وكولير تمنح لينكس التقدم",
      subtitle: "نيويورك تهزم لاس فيغاس 87-77 بفضل 34 نقطة لستيوارت ومينيسوتا تتفوق على إنديانا 88-82.",
      excerpt: "تألقت بريانا ستيوارت بـ34 نقطة لتقود ليبرتي للفوز على إيسيز، بينما حسمت نافيسا كولير مواجهة لينكس ضد كايتلين كلارك وفريق فيفر.",
      body: [
        "انطلقت منافسات نصف نهائي دوري السلة الأمريكي للسيدات بإثارة كبرى في نيويورك ومينيابوليس.",
        "سجلت بريانا ستيوارت 34 نقطة لتمنح نيويورك الفوز 87-77 على بطلات العامين الماضيين لاس فيغاس إيسيز.",
        "وفي مينيابوليس، صمدت لينكس أمام محاولات كايتلين كلارك لتفوز بنتيجة 88-82 بعد تسجيل كولير 28 نقطة حاسمة.",
      ],
    },
  },
  'premier-league-mw7-brighton-stun-tottenham-3-2-comeback-2026': {
    fr: {
      title: "Premier League 7e j. : Brighton renverse Tottenham 3-2 après avoir été mené de deux buts",
      subtitle: "Les Seagulls signent une remontée héroïque en seconde période grâce à Minteh, Rutter et un coup de tête de Danny Welbeck.",
      excerpt: "Mené 2-0 à la pause, Brighton a renversé Tottenham 3-2 à l'Amex Stadium grâce à trois buts en 18 minutes pour s'installer à la quatrième place.",
      body: [
        "L'Amex Stadium a vécu une après-midi mémorable lors de la 7e journée de Premier League avec l'incroyable retour de Brighton face à Tottenham.",
        "Devant 2-0 à la mi-temps grâce à Johnson et Maddison, les Spurs se sont effondrés face au pressing étouffant des hommes de Fabian Hürzeler.",
        "Minteh, Rutter et Welbeck ont marqué en l'espace de 18 minutes, permettant aux Seagulls de grimper au 4e rang du championnat avec 14 points.",
      ],
    },
    es: {
      title: "Premier League Jornada 7: Brighton remonta un 0-2 y tumba 3-2 al Tottenham en un segundo tiempo colosal",
      subtitle: "Los Seagulls voltean el partido con dianas de Minteh, Rutter y un cabezazo letal de Danny Welbeck.",
      excerpt: "Brighton & Hove Albion firmó una remontada histórica en el Amex Stadium, marcando tres goles en 18 minutos para derrotar 3-2 al Tottenham.",
      body: [
        "El conjunto de Fabian Hürzeler protagonizó una reacción para el recuerdo tras marcharse al descanso con dos goles de desventaja.",
        "Minteh recortó distancias al 48, Rutter empató en una gran acción individual al 58 y Welbeck culminó la gesta de cabeza en el 66.",
        "El triunfo catapulta al Brighton a la cuarta posición con 14 puntos, mientras los Spurs de Postecoglou caen a la zona baja.",
      ],
    },
    de: {
      title: "Premier League 7. Spieltag: Brighton schockt Tottenham mit 3:2-Comeback nach 0:2-Rückstand",
      subtitle: "Seagulls drehen das Spiel binnen 18 Minuten durch Minteh, Rutter und Welbecks Kopfballtreffer.",
      excerpt: "Nach 0:2-Pausenrückstand drehte Brighton die Partie gegen Tottenham Hotspur im Amex Stadium und siegte spektakulär mit 3:2.",
      body: [
        "Das Team von Fabian Hürzeler zeigte im heimischen Amex Stadium eine der bemerkenswertesten Aufholjagden der jüngeren Premier-League-Geschichte.",
        "Tottenham führte zur Pause verdient 2:0, brach aber nach der Halbzeit unter dem Dauerpressing der Seagulls völlig ein.",
        "Yankuba Minteh, Georginio Rutter und Danny Welbeck schossen Brighton mit drei Toren in 18 Minuten auf Tabellenplatz vier.",
      ],
    },
    it: {
      title: "Premier League 7ª giornata: Il Brighton rimonta due gol e batte il Tottenham 3-2 in 18 minuti",
      subtitle: "I Seagulls ribaltano il doppio svantaggio con le reti di Minteh, Rutter e il colpo di testa di Welbeck.",
      excerpt: "Sotto 2-0 all'intervallo, il Brighton ha travolto il Tottenham all'Amex Stadium con tre reti nella ripresa volando al quarto posto.",
      body: [
        "L'Amex Stadium è esploso di gioia per la clamorosa rimonta del Brighton contro il Tottenham di Postecoglou.",
        "Sotto di due reti dopo i gol di Johnson e Maddison, i padroni di casa hanno pareggiato con Minteh e Rutter prima del gol vittoria di Danny Welbeck al 66'.",
        "Con questo 3-2 la formazione guidata da Hürzeler sale al quarto posto a quota 14 punti, lasciando gli Spurs nei bassifondi.",
      ],
    },
    pl: {
      title: "Premier League 7. kolejka: Brighton odrabia dwa gole i sensacyjnie pokonuje Tottenham 3-2",
      subtitle: "Mewy odwróciły losy meczu w 18 minut drugiej połowy po trafieniach Minteha, Ruttera i Welbecka.",
      excerpt: "Przegrywając 0-2 do przerwy, Brighton strzeliło trzy gole w drugiej części gry i wygrało z Tottenhamem 3-2 na Amex Stadium.",
      body: [
        "Niedzielne spotkanie na Amex Stadium przyniosło jeden z najbardziej spektakularnych powrotów w tym sezonie Premier League.",
        "Tottenham kontrolował grę w pierwszej połowie, jednak po przerwie piłkarze Fabiana Hürzelera ruszyli do wściekłego ataku.",
        "Gole Minteha, Ruttera oraz zwycięska główka Welbecka w 66. minucie zapewniły Brighton awans na czwarte miejsce w tabeli.",
      ],
    },
    zh: {
      title: "英超第7轮：布莱顿下半场18分钟连入三球3-2史诗逆转热刺，升至积分榜第四",
      subtitle: "海鸥军团半场两球落后上演绝地反击，明特、鲁特尔破门，维尔贝克头槌打入制胜球",
      excerpt: "布莱顿在主场Amex球场上演惊天逆转，下半场由明特、鲁特尔和维尔贝克连入三球，3-2逆转战胜托特纳姆热刺。",
      body: [
        "布莱顿在主场奉献了一场英超经典逆转战，在半场0-2落后的绝境中连扳三球击溃热刺。",
        "下半场开场仅18分钟内，明特扳回一城，鲁特尔强行突入禁区扳平，随后维尔贝克力压防守队员头球破门反超比分。",
        "这场胜利让许尔策勒的球队以14分高居联赛第四位，而波斯特科格鲁的热刺则继续深陷危机。",
      ],
    },
    ja: {
      title: "プレミアリーグ第7節：ブライトンが後半18分間で3発の大逆転、トッテナムを3-2で撃破し4位浮上",
      subtitle: "0-2の劣勢からミンテー、ルッター、ウェルベックの電光石火の3ゴールでAmexスタジアム熱狂",
      excerpt: "前半に2点を先行されたブライトンが後半に怒涛の反撃を見せ、トッテナムに3-2で逆転勝利を収めた。",
      body: [
        "Amexスタジアムで行われた一戦で、ブライトンがクラブ史に残る劇的な逆転劇を演じました。",
        "前半を0-2で終えたブライトンでしたが、後半開始直後にミンテーが1点を返すと、ルッターとウェルベックが立て続けにゴールを奪いました。",
        "この3-2の勝利により、ヒュルツェラー率いるブライトンは勝ち点を14に伸ばし単独4位に浮上しました。",
      ],
    },
    ko: {
      title: "프리미어리그 7라운드: 브라이턴, 0-2 열세 딛고 후반 18분 만에 3골 폭풍 몰아치며 토트넘 3-2 격파",
      subtitle: "민테, 뤼터, 웰벡의 연속골로 아멕스 스타디움에서 역대급 대역전승 완성하며 4위 도약",
      excerpt: "전반을 0-2로 뒤지던 브라이턴이 후반 대반격에 나서며 토트넘을 3-2로 꺾고 승점 14점으로 4위에 올랐다.",
      body: [
        "아멕스 스타디움에서 열린 경기에서 브라이턴이 토트넘을 상대로 짜릿한 후반 대역전 드라마를 완성했습니다.",
        "토트넘의 존슨과 매디슨에게 연속골을 내줬던 브라이턴은 후반 시작과 함께 민테, 뤼터, 웰벡이 18분 만에 3골을 합작했습니다.",
        "이 승리로 휠첼러 감독의 브라이턴은 4승 2무 1패(승점 14)를 기록하며 4위로 올라섰습니다.",
      ],
    },
    ar: {
      title: "الدوري الإنجليزي الجولة 7: برايتون يقلب تأخره بهدفين ويهزم توتنهام 3-2 في شوط ثان إعجازي",
      subtitle: "طيور النورس تقلب الطاولة بثلاثية في 18 دقيقة عبر مينته وروتر ورأسية حاسمة لداني ويلبيك.",
      excerpt: "نجح برايتون في تحقيق عودة تاريخية على ملعب أميكس بتحويل تأخره 0-2 أمام توتنهام إلى فوز مثير 3-2 ليصعد للمركز الرابع.",
      body: [
        "عاش ملعب أميكس أجواء جنونية بعدما حول برايتون تأخره بهدفين نظيفين في الشوط الأول إلى فوز تاريخي بنتيجة 3-2.",
        "وسجل أصحاب الأرض ثلاثة أهداف متتالية خلال 18 دقيقة فقط عن طريق مينته وروتر ورأسية رائعة من المهاجم داني ويلبيك.",
        "ورفع برايتون رصيده إلى 14 نقطة ليصعد إلى المركز الرابع في جدول ترتيب الدوري الإنجليزي الممتاز.",
      ],
    },
  },
  'nfl-week4-mnf-lions-seahawks-42-29-goff-perfect-2026': {
    fr: {
      title: "NFL MNF : Jared Goff signe un 18/18 parfait historique, les Lions dominent Seattle 42-29",
      subtitle: "Le quarterback de Detroit bat le record absolu de la NFL de passes réussies sans le moindre échec.",
      excerpt: "Jared Goff a livré le match le plus précis de l'histoire de la NFL avec 18 sur 18 pour 292 yards et deux touchdowns, plus un touchdown réceptionné.",
      body: [
        "Ford Field a été le théâtre d'une performance historique lundi soir avec la démonstration de perfection absolue de Jared Goff.",
        "Goff a complété l'intégralité de ses 18 tentatives de passe pour 292 yards et deux touchdowns, effaçant le record NFL de Kurt Warner.",
        "Avec un touchdown réceptionné sur une feinte d'Amon-Ra St. Brown et deux touchdowns de Jahmyr Gibbs, Detroit s'impose 42-29 et brise une disette de 12 ans contre Seattle.",
      ],
    },
    es: {
      title: "NFL MNF: Jared Goff logra un histórico 18 de 18 perfecto y los Lions vencen 42-29 a los Seahawks",
      subtitle: "El mariscal de Detroit rompe el récord de todos los tiempos de la NFL de pases sin fallo, sumando dos touchdowns aéreos y uno recibido.",
      excerpt: "Jared Goff firmó la actuación de pase más precisa en la historia de la NFL con 18 de 18 para 292 yardas en el triunfo de Detroit sobre Seattle.",
      body: [
        "El Ford Field vivió una noche legendaria con la actuación sin precedentes de Jared Goff al completar el 100% de sus pases.",
        "Goff completó sus 18 envíos para 292 yardas y dos touchdowns, superando la plusmarca histórica de la NFL de pases sin interrupción ni fallo.",
        "Jahmyr Gibbs sumó dos anotaciones terrestres y Kerby Joseph selló el triunfo 42-29 con una intercepción en los minutos finales.",
      ],
    },
    de: {
      title: "NFL MNF: Jared Goff mit historischem 18 von 18 perfekten Passspiel beim 42:29-Sieg der Lions gegen Seahawks",
      subtitle: "Detroits Quarterback bricht den ewigen NFL-Rekord für die meisten Pässe ohne Fehlwurf und fängt selbst einen Touchdown.",
      excerpt: "Jared Goff zeigte die präziseste Passleistung der NFL-Geschichte: 18 von 18 für 292 Yards und zwei Touchdowns beim Sieg über Seattle.",
      body: [
        "Jared Goff schrieb am Montagabend NFL-Geschichte, als er jeden einzelnen seiner 18 Pässe für 292 Yards an den Mann brachte.",
        "Zusätzlich fing Goff einen 7-Yard-Touchdown-Pass von Amon-Ra St. Brown bei einem spektakulären Trickspielzug im dritten Viertel.",
        "Die Detroit Lions gewannen das Offensivspektakel mit 42:29 gegen Seattle und verbesserten ihre Bilanz auf 3-1.",
      ],
    },
    it: {
      title: "NFL MNF: Jared Goff firma un perfetto 18 su 18 storico e i Lions superano i Seahawks 42-29",
      subtitle: "Il quarterback di Detroit stabilisce il record assoluto NFL di completi senza errori, con due touchdown lanciati e uno ricevuto.",
      excerpt: "Jared Goff ha firmato la partita al lancio più precisa della storia NFL con 18 su 18 per 292 yard nel successo dei Lions a Ford Field.",
      body: [
        "Una notte da leggenda al Ford Field dove Jared Goff ha riscritto i record della NFL con una precisione chirurgica del 100%.",
        "Goff ha completato 18 passaggi su 18 per 292 yard e due mete, ricevendo anche un touchdown su ricezione da St. Brown.",
        "I Lions salgono a 3-1 nella NFC North infliggendo ai Seahawks la prima sconfitta stagionale al termine di un pirotecnico 42-29.",
      ],
    },
    pl: {
      title: "NFL MNF: Jared Goff z perfekcyjnym 18 na 18 przechodzi do historii, Lions pokonują Seahawks 42-29",
      subtitle: "Rozgrywający Detroit pobił rekord wszech czasów NFL pod względem celności bez niecelnego podania.",
      excerpt: "Jared Goff rozegrał najbardziej precyzyjny mecz w historii ligi NFL, trafiając 18 z 18 podań na 292 jardy i dwa przyłożenia.",
      body: [
        "Ford Field stało się świadkiem absolutnego rekordu NFL, gdy Jared Goff nie pomylił się ani razu w 18 próbach podaniowych.",
        "Goff dorzucił do tego przyłożenie po chwycie po zagrywce trickowej od Amon-Ra St. Browna w trzeciej kwarcie.",
        "Detroit Lions wygrali 42-29, przerywając passę sześciu kolejnych porażek z Seattle i awansując na bilans 3-1.",
      ],
    },
    zh: {
      title: "NFL周一夜赛：高夫18投18中创历史纪录，雄狮42-29力克海鹰破12年魔咒",
      subtitle: "底特律四分卫打破NFL单场全中传球纪录，送出两次传球达阵并上演接球达阵",
      excerpt: "贾里德-高夫在福特球场打出了NFL历史上最精准的传球表现，18传全中推进292码，率领雄狮42-29击败西雅图海鹰。",
      body: [
        "底特律福特球场周一见证了NFL百年历史级的一战，贾里德-高夫全场18次传球全部命中，创下历史单场100%命中率最高出手纪录。",
        "除了传出292码和两次达阵，高夫还在第三节接圣布朗传球完成一次精彩的7码接球达阵。",
        "雄狮最终以42-29击溃西雅图海鹰，终结了对对手长达12年的六连败，战绩升至3胜1负。",
      ],
    },
    ja: {
      title: "NFLマンデーナイト：ゴフが18打数18安打の完璧投球で歴代記録樹立、ライオンズが42-29で快勝",
      subtitle: "デトロイトのQBがパス成功率100%の歴代新記録を更新、2TDパスに加えTDレシーブも達成",
      excerpt: "ジャレッド・ゴフが18本すべてのパスを通し292ヤードを記録、デトロイト・ライオンズがシーホークスに42-29で快勝。",
      body: [
        "フォード・フィールドでジャレッド・ゴフが1本のミスパスもなく18回すべてのパスを成功させ、NFL記録を塗り替えました。",
        "第3クォーターにはアモン＝ラ・セントブラウンからのトリックプレーで自身も7ヤードのTDキャッチを記録しました。",
        "ライオンズは42-29でシーホークスを下し、シーホークス戦の連敗をストップして3勝1敗としました。",
      ],
    },
    ko: {
      title: "NFL 먼데이 나이트: 재러드 고프 18패스 100% 성공 대기록, 라이언스 42-29 시애틀 제압",
      subtitle: "디트로이트 쿼터백, 단 한 번의 실패도 없는 최다 패스 성공 NFL 역대 신기록 수립",
      excerpt: "재러드 고프가 18번의 패스를 모두 적중시키며 292야드와 2개의 터치다운을 기록, 라이언스가 시애틀에 42-29 승리를 거뒀다.",
      body: [
        "포드 필드에서 열린 경기에서 재러드 고프가 18번의 패스 시도를 모두 성공시키는 경이로운 플레이로 NFL 역사를 새로 썼습니다.",
        "고프는 292야드와 2개의 패스 터치다운 외에도 세인트 브라운의 패스를 받아 직접 터치다운을 성공시켰습니다.",
        "디트로이트 라이언스는 42-29로 시애틀을 꺾고 시애틀전 6연패 사슬을 끊어내며 3승 1패를 기록했습니다.",
      ],
    },
    ar: {
      title: "دوري كرة القدم الأمريكية MNF: جاريد غوف يسجل رقماً قياسياً بنسبة 100% ويقود لايونز للفوز 42-29",
      subtitle: "لاعب ديترويت يكسر الرقم القياسي في تاريخ الدوري بإكمال 18 تمريرة من أصل 18 دون أي خطأ.",
      excerpt: "قدم جاريد غوف الأداء الأكثر دقة في تاريخ NFL بإكماله 18 تمريرة من أصل 18 لمسافة 292 ياردة وتمريرتين حاسمتين ليفوز ديترويت على سياتل.",
      body: [
        "شهد ملعب فورد فيلد ليلة استثنائية دخل فيها جاريد غوف تاريخ دوري كرة القدم الأمريكية من أوسع أبوابه.",
        "أكمل غوف 18 تمريرة من أصل 18 بنسبة نجاح 100% لمسافة 292 ياردة، بالإضافة إلى استقباله تمريرة هبوط مخادعة من سانت براون.",
        "وحسم ديترويت لايونز المواجهة المثيرة بنتيجة 42-29 ليرفع رصيده إلى 3 انتصارات وهزيمة واحدة في صدارة المنافسة.",
      ],
    },
  },
  'shanghai-masters-2026-r1-preview-alcaraz-sinner-djokovic': {
    fr: {
      title: "Rolex Shanghai Masters : coup d'envoi du tableau principal avec Alcaraz, Sinner et Djokovic",
      subtitle: "Le joyau de la tournée asiatique s'ouvre à la Qizhong Arena avec 1 000 points et le trône mondial en jeu.",
      excerpt: "Le Masters 1000 de Shanghai lance son tableau principal avec Jannik Sinner, Carlos Alcaraz et Novak Djokovic en têtes d'affiche.",
      body: [
        "Vingt-quatre heures après la finale légendaire de Pékin, les projecteurs du tennis mondial se braquent sur la Qizhong Arena pour le Masters de Shanghai.",
        "Sinner cherche une revanche immédiate tandis qu'Alcaraz arrive porté par une série de neuf victoires consécutives après ses titres en Laver Cup et à Pékin.",
        "Novak Djokovic fait son grand retour en Chine pour briguer un cinquième sacre à Shanghai et son 100e titre en simple sur le circuit ATP.",
      ],
    },
    es: {
      title: "Rolex Shanghai Masters: arranca el cuadro principal con Alcaraz, Sinner y Djokovic en liza",
      subtitle: "El torneo cumbre de la gira asiática comienza en Qizhong con 1.000 puntos y el número uno de fin de año en juego.",
      excerpt: "El Masters 1000 de Shanghái da inicio a su cuadro principal en el Qizhong Arena con Sinner, Alcaraz y Novak Djokovic.",
      body: [
        "Apenas un día después de la final de 3h21 en Pekín, el circuito ATP aterriza en el imponente Qizhong Forest Arena para el Masters de Shanghái.",
        "Jannik Sinner encabeza la parte alta del cuadro mientras Carlos Alcaraz busca extender su racha ganadora tras coronarse en Pekín.",
        "El cuatro veces campeón Novak Djokovic regresa a territorio chino buscando conquistar su título número 100 como profesional.",
      ],
    },
    de: {
      title: "Rolex Shanghai Masters: Hauptfeld startet mit Alcaraz, Sinner und Djokovic im Fokus",
      subtitle: "Asiens prestigeträchtigstes ATP-1000-Turnier beginnt in der Qizhong Arena mit 1.000 Punkten und dem Kampf um Platz 1.",
      excerpt: "Das Rolex Shanghai Masters eröffnet sein 96er-Hauptfeld mit Jannik Sinner, Carlos Alcaraz und Novak Djokovic.",
      body: [
        "Nur 24 Stunden nach dem Marathon-Finale von Peking schlägt die Weltelite beim Rolex Shanghai Masters in der Qizhong Arena auf.",
        "Der Weltranglistenerste Sinner strebt Wiedergutmachung an, während Alcaraz mit neun Siegen in Serie voller Selbstvertrauen antritt.",
        "Auch Novak Djokovic greift nach fünf Jahren Abwesenheit wieder ins Geschehen ein und jagt seinen 100. Karrieretitel.",
      ],
    },
    it: {
      title: "Rolex Shanghai Masters: via al tabellone principale con Alcaraz, Sinner e Djokovic",
      subtitle: "Il fiore all'occhiello dello swing asiatico parte alla Qizhong Arena con 1.000 punti e la vetta mondiale in palio.",
      excerpt: "Il Masters 1000 di Shanghai apre i battenti con Jannik Sinner, Carlos Alcaraz e il ritorno di Novak Djokovic.",
      body: [
        "Dopo l'epica battaglia di Pechino, il circuito maschile si sposta alla spettacolare Qizhong Arena per il Rolex Shanghai Masters.",
        "Jannik Sinner guida il seeding a caccia del riscatto immediato, mentre Carlos Alcaraz punta a chiudere il gap in classifica.",
        "Il ritorno di Novak Djokovic, a caccia del suo quinto trionfo a Shanghai e del centesimo titolo ATP in carriera, nobilita il tabellone.",
      ],
    },
    pl: {
      title: "Rolex Shanghai Masters: rusza drabinka główna z Alcarazem, Sinnerem i Djokoviciem",
      subtitle: "Największy turniej w Azji rozpoczyna zmagania w Qizhong Arena z 1000 punktami i walką o fotel lidera na szali.",
      excerpt: "Rolex Shanghai Masters otwiera zmagania w turnieju głównym z Jannikiem Sinnerem, Carlosem Alcarazem i Novakiem Djokoviciem.",
      body: [
        "Dzień po niesamowitym finale w Pekinie uwaga fanów tenisa przenosi się do Szanghaju na przedostatni turniej Masters 1000 w tym sezonie.",
        "Jannik Sinner i Carlos Alcaraz mogą spotkać się dopiero w wielkim finale, a w połówce Hiszpana czyha powracający Novak Djoković.",
        "Stawka 1000 punktów rankingowych ma kluczowe znaczenie w wyścigu do turyńskiego ATP Finals.",
      ],
    },
    zh: {
      title: "上海劳力士大师赛正赛打响：阿尔卡拉斯、辛纳与德约科维奇领衔出征旗忠网球中心",
      subtitle: "亚洲唯一ATP 1000大师赛开打，千分积分与年终世界第一争夺战拉开序幕",
      excerpt: "2026年上海大师赛正赛周一正式揭幕，刚在中网夺冠的阿尔卡拉斯与世界第一辛纳、四届赛会冠军德约科维奇齐聚旗忠。",
      body: [
        "在北京经历3小时21分钟的史诗对决仅24小时后，世界男子网坛的目光迅速聚焦于上海旗忠森林体育城网球中心。",
        "头号种子辛纳志在迅速反弹，而手握九连胜的阿尔卡拉斯则希望延续中网夺冠的火热手感，缩小与世界第一的积分差距。",
        "四届赛会冠军德约科维奇时隔五年重返上海参赛，冲击个人职业生涯第100座单打冠军奖杯。",
      ],
    },
    ja: {
      title: "上海ロレックス・マスターズ：アルカラス、シナー、ジョコビッチが集結し本戦開幕",
      subtitle: "アジア唯一のATPマスターズ1000が旗忠アリーナで開幕、世界ランク1位争いが激化",
      excerpt: "上海マスターズの本戦が開幕。北京で優勝したアルカラス、世界1位のシナー、4度優勝のジョコビッチが頂点を狙う。",
      body: [
        "北京での歴史的決勝戦から一夜明け、アジア最高峰のトーナメントである上海マスターズが開幕しました。",
        "リベンジを期す世界1位シナーと9連勝中のアルカラスが両ボトム・トップシードとして牽引します。",
        "上海で4度の優勝を誇るノバク・ジョコビッチも参戦し、通算100個目のツアータイトル獲得を目指します。",
      ],
    },
    ko: {
      title: "상하이 롤렉스 마스터스 본선 개막: 알카라스, 시너, 조코비치 아시아 하드코트 정상 격돌",
      subtitle: "치중 테니스 센터에서 펼쳐지는 아시아 유일의 ATP 1000 대회, 랭킹 1위 쟁탈전 개막",
      excerpt: "상하이 마스터스 96강 본선 일정이 개막하며 야닉 시너, 카를로스 알카라스, 노박 조코비치가 우승 트로피를 향해 출격했다.",
      body: [
        "베이징에서의 혈투 직후 아시아 하드코트 시리즈의 클라이맥스인 상하이 롤렉스 마스터스가 치중 아레나에서 개막했습니다.",
        "세계 1위 야닉 시너와 베이징 챔피언 카를로스 알카라스가 각각 1, 2번 시드로 우승을 노립니다.",
        "상하이 통산 4회 우승자 노박 조코비치 역시 통산 100번째 투어 타이틀 획득을 위해 출전표를 던졌습니다.",
      ],
    },
    ar: {
      title: "بطولة شنغهاي للأساتذة: انطلاق القرعة الرئيسية بمشاركة ألكاراز وسينر وجوكوفيتش",
      subtitle: "أكبر بطولات آسيا فئة 1000 نقطة تفتح أبوابها في صالة كيتشونغ للمنافسة على صدارة التصنيف العالمي.",
      excerpt: "انطلقت مباريات الدور الأول لبطولة شنغهاي للأساتذة بمشاركة كبار نجوم التنس العالمي يتقدمهم سينر وألكاراز وجوكوفيتش.",
      body: [
        "بعد ساعات قليلة من نهائي بكين التاريخي، تتجه أنظار عشاق التنس نحو شنغهاي لانطلاق بطولة الأساتذة الكبرى.",
        "يسعى يانيك سينر للتعويض السريع في حين يدخل كارلوس ألكاراز البطولة متسلحاً بتسع انتصارات متتالية.",
        "ويعود الصربي نوفاك جوكوفيتش للمنافسة على الملاعب الصينية طامحاً لحصد لقبه رقم 100 في مسيرته الاحترافية.",
      ],
    },
  },
  'f1-singapore-gp-aftermath-norris-title-chase-lawson-2026': {
    fr: {
      title: "F1 compte à rebours Amériques : la démonstration de Norris relance le titre, Lawson titularisé chez RB",
      subtitle: "McLaren prend 41 points d'avance chez les constructeurs tandis que Red Bull confie le volant de Ricciardo à Lawson pour Austin.",
      excerpt: "La victoire de 20 secondes de Lando Norris à Singapour bouleverse le championnat avant la tournée américaine et l'arrivée de Liam Lawson chez RB.",
      body: [
        "La démonstration de Lando Norris à Singapour avec près de 21 secondes d'avance sur Max Verstappen a redistribué toutes les cartes.",
        "McLaren s'envole en tête du classement des constructeurs avec 41 points d'avance sur Red Bull à six courses de la fin.",
        "Dans le même temps, Red Bull a officialisé la titularisation du jeune Liam Lawson à la place de Daniel Ricciardo dès le Grand Prix des États-Unis.",
      ],
    },
    es: {
      title: "F1 cuenta atrás América: la exhibición de Norris reabre el mundial y Lawson debuta con RB",
      subtitle: "McLaren estira a 41 puntos su ventaja de constructores mientras Red Bull sienta a Lawson en Austin en lugar de Ricciardo.",
      excerpt: "El aplastante triunfo de Lando Norris en Marina Bay sacude la Fórmula 1 a las puertas del triplete americano y con Liam Lawson en RB.",
      body: [
        "Lando Norris dominó de principio a fin el GP de Singapur logrando una ventaja demoledora de casi 21 segundos sobre Verstappen.",
        "McLaren aventaja ya en 41 puntos a Red Bull en el campeonato de constructores gracias al tercer escalón del podio de Piastri.",
        "Red Bull confirmó además que el neozelandés Liam Lawson ocupará el asiento de Daniel Ricciardo en RB para las seis carreras restantes.",
      ],
    },
    de: {
      title: "F1 Amerika-Countdown: Norris-Gala heizt WM-Kampf an, Lawson übernimmt RB-Cockpit",
      subtitle: "McLaren baut Konstrukteurs-Führung auf 41 Punkte aus, während Red Bull Liam Lawson für die letzten sechs Rennen bestätigt.",
      excerpt: "Der 20-Sekunden-Vorsprung von Lando Norris in Singapur mischt die Formel-1-Weltmeisterschaft vor den Amerika-Rennen völlig neu auf.",
      body: [
        "Mit einem souveränen Start-Ziel-Sieg und 20,9 Sekunden Vorsprung vor Verstappen hat Lando Norris in Singapur ein deutliches Statement gesetzt.",
        "McLaren führt nun mit 41 Punkten Vorsprung vor Red Bull in der Konstrukteurswertung.",
        "Zudem verkündete Red Bull am Montag den Wechsel von Daniel Ricciardo zu Nachwuchsfahrer Liam Lawson ab dem Rennen in Austin.",
      ],
    },
    it: {
      title: "F1 conto alla rovescia Americhe: il dominio di Norris riapre il titolo, Lawson approda in RB",
      subtitle: "McLaren porta a 41 i punti di vantaggio tra i costruttori mentre Red Bull promuove Lawson al posto di Ricciardo per Austin.",
      excerpt: "Il trionfo con 20 secondi di margine di Norris a Marina Bay riaccende la lotta mondiale prima del trittico americano.",
      body: [
        "Il weekend di Marina Bay ha consacrato la supremazia McLaren con la perentoria vittoria di Lando Norris su Max Verstappen.",
        "Il team di Woking guida ora il mondiale costruttori con 41 lunghezze di vantaggio sulla Red Bull in piena crisi d'assetto.",
        "Nel paddock la notizia del giorno è l'ufficialità di Liam Lawson al posto di Daniel Ricciardo sulla Racing Bulls a partire da Austin.",
      ],
    },
    pl: {
      title: "F1 odliczanie do Ameryk: triumf Norrisa zaostrza walkę o tytuł, Lawson w bolidzie RB",
      subtitle: "McLaren ma 41 punktów przewagi wśród konstruktorów, a Red Bull potwierdza Liama Lawsona na finałowe sześć wyścigów.",
      excerpt: "Dominacja Lando Norrisa w Singapurze i 20 sekund przewagi nad Verstappenem otwierają walkę o mistrzostwo F1 przed wyścigami w Ameryce.",
      body: [
        "Lando Norris zdeklasował rywali w Singapurze, finiszując niemal 21 sekund przed Maxem Verstappenem.",
        "McLaren powiększył przewagę w klasyfikacji konstruktorów do 41 punktów nad Red Bullem.",
        "Red Bull ogłosił jednocześnie, że 22-letni Liam Lawson zastąpi Daniela Ricciardo w zespole RB do końca sezonu 2026.",
      ],
    },
    zh: {
      title: "F1美洲三连赛前瞻：诺里斯新加坡碾压夺冠缩小分差，劳森入主RB出征奥斯汀",
      subtitle: "迈凯伦车队积分领先优势扩大至41分，红牛确认新西兰小将劳森顶替里卡多完成赛季",
      excerpt: "诺里斯在滨海湾以20.9秒的巨大优势力克维斯塔潘，在F1进入美洲三连赛之际让总冠军争夺彻底白热化，同时劳森正式加盟RB。",
      body: [
        "诺里斯在新加坡大奖赛上以领跑全场且领先维斯塔潘近21秒的统治级表现夺冠，彻底改写了本赛季争冠格局。",
        "迈凯伦在车队积分榜上以358分对317分领先红牛41分，皮亚斯特里同登领奖台巩固了车队优势。",
        "红牛周一正式确认，22岁的新西兰车手利亚姆-劳森将在奥斯汀站起顶替里卡多出战本赛季最后六场大奖赛。",
      ],
    },
    ja: {
      title: "F1アメリカ連戦プレビュー：ノリスの圧勝でタイトル争い激化、ローソンがRBシートに昇格",
      subtitle: "マクラーレンがコンストラクターズで41点差リード、レッドブルはリカルドに代わりローソンを起用",
      excerpt: "シンガポールGPでノリスがフェルスタッペンに20秒差をつけ優勝。タイトル争いが混沌とする中、ローソンがRBから参戦決定。",
      body: [
        "マリーナベイのナイトレースでランド・ノリスが20.9秒差をつけて圧勝し、ドライバーズ選手権の差を52ポイントに縮めました。",
        "マクラーレンはレッドブルに対して41ポイントのリードを築き、オースティンからのアメリカ連戦に臨みます。",
        "またレッドブルは、ダニエル・リカルドに代わりリアム・ローソンが残り6戦でRBのマシンをドライブすると正式発表しました。",
      ],
    },
    ko: {
      title: "F1 아메리카 3연전 카운트다운: 노리스 싱가포르 압승으로 52점 차 추격, 로슨 RB 합류",
      subtitle: "맥라렌 컨스트럭터 41점 차 선두 질주, 레드불은 리카도 대신 리암 로슨 잔여 6경기 기용 확정",
      excerpt: "란도 노리스의 싱가포르 GP 20초 차 대승으로 F1 챔피언십 경쟁이 요동치는 가운데 리암 로슨이 RB 시트에 전격 합류했다.",
      body: [
        "란도 노리스가 싱가포르 마리나 베이에서 페르스타펜을 20.9초 차로 따돌리고 완승을 거두며 타이틀 희망을 살렸습니다.",
        "맥라렌은 피아스트리의 3위 입상까지 더해 레드불과의 컨스트럭터 격차를 41점 차로 벌렸습니다.",
        "레드불은 잔여 6개 레이스에서 대니얼 리카도 대신 22세 신예 리암 로슨을 RB 드라이버로 투입한다고 공식 발표했습니다.",
      ],
    },
    ar: {
      title: "فورمولا 1 العد التنازلي للأمريكتين: سيطرة نوريس تشعل الصراع ولوسون يقود لـ RB",
      subtitle: "ماكلارين توسع الفارق في بطولة الصانعين إلى 41 نقطة وريد بُل تؤكد ليام لوسون بديلاً لريكاردو.",
      excerpt: "أشعل فوز لاندو نوريس بفارق 20 ثانية في سنغافورة بطولة العالم للفورمولا 1 مع الإعلان الرسمي عن مشاركة ليام لوسون في الجولات القادمة.",
      body: [
        "أحدث فوز لاندو نوريس الساحق في سنغافورة بفارق 20.9 ثانية عن فيرستابن زلزالاً فنياً في بطولة العالم.",
        "عزز فريق ماكلارين صدارته لبطولة الصانعين بفارق 41 نقطة أمام ريد بُل قبل الانتقال إلى حلبة أوستن.",
        "وأعلن فريق ريد بُل رسمياً تعيين السائق النيوزيلندي ليام لوسون ليحل محل دانييل ريكاردو في المقاعد الستة المتبقية.",
      ],
    },
  },
  'pga-tour-black-desert-championship-preview-kevin-yu-2026': {
    fr: {
      title: "PGA Tour : Kevin Yu grimpe dans le top 65 après son sacre, cap sur l'Utah pour le Black Desert Championship",
      subtitle: "Le golfeur taïwanais s'offre son premier trophée en playoff à Sanderson Farms avant les falaises d'Ivins.",
      excerpt: "Kevin Yu a remporté sa première victoire PGA Tour en playoff au Sanderson Farms, bondissant dans le top 65 mondial avant le tournoi d'Utah.",
      body: [
        "Kevin Yu a décroché son premier titre PGA Tour au bout du suspense à Jackson en dominant Beau Hossler en prolongation.",
        "Cette victoire historique propulse le joueur de 26 ans à la 63e place mondiale et lui assure deux ans d'exemption sur le circuit.",
        "Le circuit PGA prend la direction de l'Utah pour l'inaugural Black Desert Championship au milieu des coulées de lave noire.",
      ],
    },
    es: {
      title: "PGA Tour: Kevin Yu sube al top 65 tras su primer título y la gira viaja a Utah para el Black Desert Championship",
      subtitle: "El taiwanés se corona en un vibrante playoff en Sanderson Farms y el circuito estrena sede en los cañones de roca roja.",
      excerpt: "Kevin Yu logró su primera victoria en el PGA Tour en el desempate de Sanderson Farms, saltando al puesto 63 mundial antes de viajar a Utah.",
      body: [
        "Con dos birdies magistrales en el hoyo 72 y en el desempate, Kevin Yu conquistó su primer trofeo profesional del PGA Tour en Jackson.",
        "El triunfo mete a Yu entre los mejores 65 del mundo y le garantiza su presencia en los Majors de 2027.",
        "El PGA Tour aterriza ahora en Ivins, Utah, para el torneo inaugural de Black Desert Championship entre campos de lava y cañones.",
      ],
    },
    de: {
      title: "PGA Tour: Kevin Yu stürmt nach Playoff-Sieg in die Top 65, Tour zieht weiter nach Utah",
      subtitle: "Taiwans Star feiert Premierensieg bei der Sanderson Farms Championship vor der Premiere des Black Desert Championship.",
      excerpt: "Kevin Yu holte sich im dramatischen Stechen in Jackson seinen ersten PGA-Tour-Titel und reist voller Schwung zur Premiere nach Utah.",
      body: [
        "Kevin Yu erzwang am 72. Loch mit einem Birdie das Stechen gegen Beau Hossler und verwandelte dort sicher zum ersten Toursieg.",
        "Durch den Erfolg kletterte der 26-Jährige auf Rang 63 der Weltrangliste und sicherte sich seine Tour-Karte bis Ende 2028.",
        "Die PGA Tour gastiert nun erstmals seit 1963 wieder in Utah auf dem spektakulären Black Desert Resort.",
      ],
    },
    it: {
      title: "PGA Tour: Kevin Yu vola nella top 65 dopo il primo trionfo, la stagione sbarca in Utah per il Black Desert",
      subtitle: "Il golfista taiwanese vince al playoff la Sanderson Farms Championship prima della novità nello Utah tra i canyon rossi.",
      excerpt: "Kevin Yu conquista la sua prima vittoria sul PGA Tour superando Hossler allo spareggio e salendo al 63° posto del ranking mondiale.",
      body: [
        "Un birdie alla 72ª buca e uno allo spareggio hanno regalato a Kevin Yu il suo primo indimenticabile titolo PGA Tour a Jackson.",
        "La vittoria proietta Yu al 60° posto della FedExCup Fall e garantisce l'accesso al Masters e al PGA Championship 2027.",
        "Il PGA Tour debutta questa settimana in Utah con l'inaugurale Black Desert Championship tra rocce rosse e campi di lava.",
      ],
    },
    pl: {
      title: "PGA Tour: Kevin Yu wkracza do czołowej 65 po triumfie w dogrywce, tour przenosi się do Utah",
      subtitle: "Reprezentant Tajwanu zdobył pierwszy tytuł PGA Tour w Sanderson Farms, a stawka szykuje się do Black Desert Championship.",
      excerpt: "Kevin Yu wygrał po dogrywce w Sanderson Farms swój pierwszy turniej PGA Tour, awansując na 63. miejsce na świecie przed turniejem w Utah.",
      body: [
        "Kevin Yu pokonał Beau Hosslera na pierwszym dołku dogrywki, pieczętując swój życiowy sukces na Country Club of Jackson.",
        "Wygrana dała mu skok o 31 pozycji w rankingu OWGR oraz dwuletnie pełne zwolnienie w PGA Tour.",
        "Karawana PGA Tour zawitała do Ivins w stanie Utah na dziewiczy turniej Black Desert Championship pośród czarnych pól lawowych.",
      ],
    },
    zh: {
      title: "美巡赛：俞俊安加洞夺冠首捧美巡奖杯挺进世界前65，美巡移师犹他黑沙漠锦标赛",
      subtitle: "中国台北选手桑德森农场锦标赛加洞抓鸟加冕，美巡时隔61年重返犹他州展开黑沙漠首战",
      excerpt: "俞俊安在密西西比通过加洞赛击败霍斯勒斩获职业美巡首冠，世界排名升至第63位，领衔众将出战犹他黑沙漠锦标赛。",
      body: [
        "26岁的俞俊安在杰克逊乡村俱乐部第72洞和加洞赛连续抓下关键小鸟球，以总成绩-23杆夺得个人首座美巡赛冠军奖杯。",
        "这场突破性胜利让俞俊安的世界排名跃升31位至第63位，联邦快递秋季积分升至第60位，锁定未来两年全卡资格。",
        "美巡赛本周移师犹他州艾文斯，时隔61年再度在犹他州举办正式赛事，球场坐落于壮丽的黑色熔岩与红色砂岩峡谷之间。",
      ],
    },
    ja: {
      title: "PGAツアー：俞俊安がPO制し初優勝で世界ランク65位圏内に急浮上、次戦はユタ州ブラックデザートへ",
      subtitle: "サンダーソンファームズで悲願のツアー初勝利を飾った台湾の新星、ユタ州での新設大会へ",
      excerpt: "ケビン・ユー（俞俊安）がプレーオフで初優勝を飾り世界63位に急浮上。PGAツアーはユタ州の新設大会へ向かう。",
      body: [
        "最終18番で劇的なバーディーを奪いプレーオフに持ち込んだ俞俊安が、1ホール目で決着をつけてPGAツアー初制覇を果たしました。",
        "この勝利により世界ランキングは63位までジャンプアップし、2027年のマスターズ出場権などを獲得しました。",
        "PGAツアーは今週、ユタ州で60年以上ぶりとなる公式戦ブラックデザート・チャンピオンシップを開催します。",
      ],
    },
    ko: {
      title: "PGA 투어: 케빈 위 연장전 끝 생애 첫 우승으로 세계 65위 진입, 유타 블랙 데저트로 이동",
      subtitle: "샌더슨 팜스 챔피언십 우승으로 투어 카드 2년 확보, 유타 붉은 암벽 코스에서 열리는 신설 대회 출격",
      excerpt: "대만의 케빈 위(위쥔안)가 연장 첫 홀 버디로 PGA 투어 첫 승을 거두고 세계 63위로 도약한 가운데 투어가 유타로 향한다.",
      body: [
        "케빈 위는 72번째 홀과 연장 첫 홀에서 연달아 버디를 낚으며 보 호슬러를 제치고 PGA 투어 첫 승의 감격을 누렸습니다.",
        "이번 우승으로 페덱스컵 가을 시리즈 60위로 도약하며 2년간 투어 시드와 주요 메이저 대회 출전권을 확보했습니다.",
        "PGA 투어는 1963년 이후 60여 년 만에 유타주로 이동해 신설 대회인 블랙 데저트 챔피언십을 치릅니다.",
      ],
    },
    ar: {
      title: "جولة PGA: كيفن يو يقفز إلى قائمة أفضل 65 عالمياً بعد لقبه الأول والأنظار تتجه لبطولة بلاك ديزرت في يوتا",
      subtitle: "اللاعب التايواني يحسم لقب ساندرسون فارمز في الحفرة الفاصلة قبل انطلاق البطولة الجديدة بين صخور يوتا.",
      excerpt: "حقق كيفن يو باكورة ألقابه في جولة PGA بعد جولة فاصلة مثيرة في ميسيسيبي، ليصعد للمركز 63 عالمياً قبل بطولة يوتا.",
      body: [
        "حقق اللاعب الشاب كيفن يو إنجازاً تاريخياً بإحراز لقبه الأول في الجولة الأمريكية بعد تفوقه على بو هوسلر في الحفرة الإضافية.",
        "منحه هذا الفوز قفزة كبيرة إلى المركز 63 في التصنيف العالمي وضمان بطاقة المشاركة للعامين المقبلين.",
        "وتتجه أنظار الجولة هذا الأسبوع نحو ولاية يوتا لإقامة بطولة بلاك ديزرت الافتتاحية وسط التكوينات الصخرية البركانية الخلابة.",
      ],
    },
  },
  'wnba-semifinals-game2-preview-aces-fever-adjustments-2026': {
    fr: {
      title: "Demi-finales WNBA veille du Match 2 : les Aces et le Fever préparent leur riposte tactique après leurs revers",
      subtitle: "Becky Hammon règle le problème des pertes de balle tandis que Christie Sides cherche la clé face à Collier.",
      excerpt: "Menées 1-0 par le Liberty et les Lynx, les équipes de Las Vegas et d'Indiana ont passé leur lundi en salle vidéo avant le Match 2.",
      body: [
        "Avec un déficit de 0-1 dans une série au meilleur des cinq matches, la pression est maximale pour Las Vegas et Indiana.",
        "Becky Hammon a axé les entraînements des Aces sur la sécurité du ballon après les 18 pertes de balle concédées face à Stewart à New York.",
        "À Minneapolis, le Fever de Caitlin Clark peaufine son plan défensif pour contenir Napheesa Collier avant le choc de mardi.",
      ],
    },
    es: {
      title: "Semifinales WNBA Víspera del Partido 2: Aces y Fever ajustan piezas en busca de la revancha",
      subtitle: "Becky Hammon corrige las pérdidas de balón y Christie Sides diseña trampas defensivas ante las líderes Lynx.",
      excerpt: "Tras caer en el primer asalto ante Liberty y Lynx, Las Vegas Aces e Indiana Fever dedican el lunes a corregir errores tácticos.",
      body: [
        "Las Vegas Aces e Indiana Fever afrontan un Partido 2 decisivo el martes sabiendo que un 0-2 en contra resultaría casi letal.",
        "Becky Hammon exigió mayor dinamismo para evitar que la defensa de Breanna Stewart neutralice a A'ja Wilson.",
        "Por su parte, Caitlin Clark y las Fever confían en mantener el ritmo anotador del último cuarto para asaltar la cancha de Minnesota.",
      ],
    },
    de: {
      title: "WNBA-Halbfinale vor Spiel 2: Aces und Fever planen taktische Revanche nach Auftaktniederlagen",
      subtitle: "Becky Hammon adressiert Ballverluste in Las Vegas, während Christie Sides Antworten auf Colliers Dominanz sucht.",
      excerpt: "Nach den Siegen von Liberty und Lynx stehen die Aces und das Fever vor Spiel 2 unter enormem Druck und feilen an ihren Systemen.",
      body: [
        "Am Tag vor Spiel 2 stand in Brooklyn und Minneapolis intensive Videoanalyse auf dem Programm der beiden WNBA-Halbfinalserien.",
        "Die Las Vegas Aces müssen gegen Breanna Stewart und die Liberty ihre 18 Ballverluste aus Spiel 1 dringend minimieren.",
        "Indiana sucht derweil nach Wegen, um Napheesa Collier einzudämmen und Caitlin Clark mehr freie Dreierwürfe zu verschaffen.",
      ],
    },
    it: {
      title: "Semifinali WNBA vigilia di Gara 2: Aces e Fever preparano la riscossa dopo i passi falsi iniziali",
      subtitle: "Becky Hammon studia i contromisure per le palle perse, Christie Sides cerca una gabbia difensiva per Collier.",
      excerpt: "Sotto 1-0 nelle serie contro Liberty e Lynx, Las Vegas Aces e Indiana Fever lavorano duramente in palestra prima di Gara 2.",
      body: [
        "Gara 2 rappresenta già un bivio cruciale per le bi-campionesse in carica di Las Vegas e per le rampanti Indiana Fever.",
        "Le Aces hanno subito la clamorosa prova di Breanna Stewart e cercano maggiore fluidità offensiva per innescare A'ja Wilson.",
        "A Minneapolis, la franchigia di Caitlin Clark vuole confermare la bella rimonta del quarto periodo per impattare la serie.",
      ],
    },
    pl: {
      title: "Półfinały WNBA przed meczem nr 2: Aces i Fever szukają taktycznych odpowiedzi po porażkach",
      subtitle: "Becky Hammon poprawia straty Las Vegas, a Christie Sides przygotowuje defensywę na znakomitą Collier.",
      excerpt: "Przegrywając 0-1 z Liberty i Lynx, koszykarki Aces oraz Fever spędziły poniedziałek na analizie wideo przed meczem nr 2.",
      body: [
        "Poniedziałek był dniem intensywnych korekt taktycznych w obozach Las Vegas Aces oraz Indiana Fever.",
        "Trenerka Becky Hammon zażądała większej dyscypliny po 18 stratach w starciu ze świetnie dysponowaną Breanną Stewart.",
        "Indiana Fever liczą, że Caitlin Clark zdoła sforsować defensywę Lynx i doprowadzić do remisu w serii.",
      ],
    },
    zh: {
      title: "WNBA半决赛G2前瞻：王牌与狂热紧急战术纠错，自由人与山猫力争扩大胜势",
      subtitle: "贝基-哈蒙严抓王牌18次失误漏洞，克里斯蒂-塞兹演练防守包夹阻击山猫核心科利尔",
      excerpt: "大比分0-1落后的卫冕冠军拉斯维加斯王牌与印第安纳狂热在周一全天进行录像复盘，力争在周二第二战扳平总比分。",
      body: [
        "在五场三胜制的半决赛中，总比分0-2落后在WNBA历史上逆转概率仅为4%，周二的第二场比赛成为王牌和狂热的生死战。",
        "王牌主帅哈蒙在录像课上重点指出了G1送出18次失误的致命伤，要求加强球的轮转以帮助威尔逊摆脱斯图尔特的包夹。",
        "狂热则寄希望于凯特琳-克拉克在第四节的追分势头，计划通过提速和无球掩护打破山猫严密的阵地防线。",
      ],
    },
    ja: {
      title: "WNBA準決勝第2戦前夜：初戦黒星のエーシズとフィーバーが巻き返しへ戦術修正に着手",
      subtitle: "ハモンHCがターンオーバー対策を徹底、フィーバーはミネソタのエース・コリアー封じに注力",
      excerpt: "リバティとリンクスに先勝を許したラスベガスとインディアナが、火曜の第2戦に向けて徹底したビデオ分析を実施。",
      body: [
        "第1戦を落としたラスベガス・エーシズとインディアナ・フィーバーにとって、火曜日の第2戦は絶対に落とせない正念場です。",
        "スチュワートに34点を許したエーシズは、ウィルソンへのダブルチームを打開すべくパス回しの改善を図ります。",
        "フィーバーは第4Qに猛追を見せたクラークのトランジションを軸に、リンクス相手の敵地勝利を目指します。",
      ],
    },
    ko: {
      title: "WNBA 준결승 2차전 전야: 1차전 패한 에이시스와 피버, 사활 건 전술 수정 돌입",
      subtitle: "베키 해먼 감독 턴오버 방지 집중 훈련, 피버는 미네소타 콜리어 봉쇄책 마련 분주",
      excerpt: "리버티와 링스에 1차전을 내준 에이시스와 피버가 화요일 2차전을 앞두고 월요일 집중적인 비디오 미팅으로 반격을 다짐했다.",
      body: [
        "5전 3선승제 플레이오프에서 0-2로 몰릴 경우 탈락 확률이 96%에 달하는 만큼 2차전은 물러설 수 없는 승부처입니다.",
        "에이시스의 베키 해먼 감독은 브리애나 스튜어트에게 당한 수모를 갚기 위해 1차전 18개의 실책을 줄이는 데 집중했습니다.",
        "인디애나 피버는 케이틀린 클라크의 4쿼터 폭발력을 재현해 링스의 짠물 수비를 뚫고 1승 1패 균형을 맞추겠다는 각오입니다.",
      ],
    },
    ar: {
      title: "نصف نهائي WNBA عشية المباراة 2: إيسز وفيفر يستعدان للرد التكتيكي بعد هزائم الجولة الأولى",
      subtitle: "بيكي هامون تعالج أخطاء فقدان الكرة وكريستي سايدز تبحث عن حلول لإيقاف تألق كوليير.",
      excerpt: "أمضى فريقا لاس فيغاس إيسز وإنديانا فيفر يوم الاثنين في مراجعة الأشرطة المسجلة لتصحيح الأخطاء قبل خوض المباراة الثانية الحاسمة.",
      body: [
        "تكتسب المباراة الثانية أهمية قصوى لحامل اللقب لاس فيغاس إيسز وإنديانا فيفر لتفادي التأخر بنتيجة 0-2 في السلسلة.",
        "ركزت المدربة بيكي هامون على معالجة 18 خسارة للكرة ارتكبها فريقها أمام نيويورك ليبرتي في المباراة الأولى.",
        "في مينيابوليس، يسعى فيفر بقيادة كيتلين كلارك لكسر دفاعات مينيسوتا لينكس وتحقيق انتصار ثمين خارج الديار.",
      ],
    },
  },
  'premier-league-mw7-fallout-tottenham-collapse-brighton-2026': {
    fr: {
      title: "Premier League 7e j. bilan : Tottenham sonné après l'effondrement à Brighton, City seul en tête avec 21 points",
      subtitle: "Les Spurs concèdent un 10e point depuis une position de tête tandis que les hommes de Guardiola réalisent le carton plein.",
      excerpt: "L'incroyable retour 3-2 de Brighton contre Tottenham plonge les Spurs dans la tourmente alors que Manchester City survole la Premier League.",
      body: [
        "La 7e journée de Premier League s'est achevée sur une déflagration tactique à l'Amex Stadium où Tottenham a sombré en 18 minutes.",
        "Menant 2-0 à la pause, les Spurs ont concédé trois buts en seconde période face aux Seagulls déchaînés de Fabian Hürzeler.",
        "Tottenham s'enfonce dans la crise avec 10 points perdus après avoir mené, pendant que Manchester City caracole en tête avec un 7/7 impeccable.",
      ],
    },
    es: {
      title: "Premier League Jornada 7 balance: Tottenham se tambalea tras el colapso ante Brighton, City líder absoluto con 21 puntos",
      subtitle: "Los Spurs dejan escapar su décimo punto tras ir ganando, mientras el equipo de Guardiola firma un arranque impecable.",
      excerpt: "La remontada 3-2 del Brighton ante el Tottenham sacude la Premier antes del parón internacional con el Manchester City intratable en la cima.",
      body: [
        "El descanso de selecciones llega con un ambiente de máxima tensión en el Tottenham tras dilapidar una renta de dos goles en el Amex.",
        "En apenas 18 minutos mágicos, Minteh, Rutter y Welbeck destrozaron el esquema de Ange Postecoglou para colocar al Brighton cuarto.",
        "El Manchester City domina la liga con 21 puntos de 21 posibles, distanciando a un Arsenal que no puede permitirse ningún traspié.",
      ],
    },
    de: {
      title: "Premier League Spieltag 7 Fazit: Tottenham taumelt nach Kollaps in Brighton, City souverän mit 21 Punkten vorn",
      subtitle: "Spurs verspielen bereits ihren 10. Punkt nach Führung, während Guardiolas Meister mit weißer Weste in die Länderspielpause geht.",
      excerpt: "Brightons furiose 3:2-Aufholjagd stürzt die Spurs in eine handfeste Krise, während Manchester City an der Tabellenspitze einsam seine Kreise zieht.",
      body: [
        "Das 3:2 von Brighton nach 0:2-Halbzeitrückstand sorgte am 7. Spieltag für das spektakulärste Comeback der bisherigen Saison.",
        "Tottenham hat in dieser Spielzeit bereits 10 Punkte nach Führungspositionen verschenkt und rutscht immer tiefer in den Tabellenkeller.",
        "Manchester City thront mit der perfekten Ausbeute von 21 Punkten aus sieben Spielen souverän über der Konkurrenz.",
      ],
    },
    it: {
      title: "Premier League 7ª giornata bilancio: Tottenham sotto shock dopo il tracollo di Brighton, City a punteggio pieno a quota 21",
      subtitle: "Spurs rimontati per la decima volta in stagione da situazione di vantaggio, mentre la corazzata di Guardiola non sbaglia un colpo.",
      excerpt: "L'incredibile rimonta per 3-2 del Brighton ai danni del Tottenham lascia Postecoglou nei guai prima della sosta per le nazionali.",
      body: [
        "La pausa per le nazionali inizia con una crisi nera per il Tottenham, crollato all'Amex Stadium sotto i colpi di Minteh, Rutter e Welbeck.",
        "Gli Spurs hanno già sperperato 10 punti da situazioni di vantaggio in questo avvio di Premier League.",
        "In vetta il Manchester City prosegue la sua marcia trionfale a punteggio pieno con 21 punti in sette giornate.",
      ],
    },
    pl: {
      title: "Premier League 7. kolejka podsumowanie: Tottenham w kryzysie po zapaści w Brighton, City z kompletem 21 punktów",
      subtitle: "Spurs stracili już 10 punktów z pozycji prowadzenia, podczas gdy mistrzowie Pepa Guardioli idą jak burza przed przerwą.",
      excerpt: "Sensacyjny powrót Brighton z 0-2 na 3-2 obnażył bezradność Tottenhamu, a Manchester City pewnie przewodzi stawce z kompletem zwycięstw.",
      body: [
        "Porażka na Amex Stadium wywołała ogromne poruszenie w Londynie, gdzie Ange Postecoglou musi zmierzyć się z falą krytyki.",
        "Brighton pod wodzą Fabiana Hürzelera wspięło się na czwarte miejsce po zabójczych 18 minutach drugiej połowy.",
        "Manchester City prowadzi z 21 punktami na koncie po siedmiu meczach, nie dając rywalom cienia nadziei.",
      ],
    },
    zh: {
      title: "英超第7轮战报与综述：热刺惨遭布莱顿逆转深陷危机，曼城七连胜狂轰21分领跑积分榜",
      subtitle: "热刺领先局痛失本季第10个积分后防崩盘，瓜迪奥拉之师全胜完美战绩进入国际比赛日",
      excerpt: "布莱顿主场3-2惊天逆转托特纳姆热刺成为第7轮最大焦点，热刺危机四伏，而曼城则以全胜21分雄霸英超榜首。",
      body: [
        "英超第7轮在一场跌宕起伏的逆转大戏中落下帷幕，波斯特科格鲁的热刺在两球领先的好局下被布莱顿18分钟三球逆转。",
        "热刺本赛季在领先情况下已累计丢掉10分，深陷降级区泥潭，主帅战术引发外界强烈质疑。",
        "而卫冕冠军曼城则以7战全胜积21分的无敌姿态领跑，领先身后的阿森纳3分、利物浦6分进入国际比赛日间歇期。",
      ],
    },
    ja: {
      title: "プレミアリーグ第7節総括：トッテナムが逆転負けで泥沼危機、マンCが開幕7連勝の勝点21で首位独走",
      subtitle: "スパーズはリードから今季10失点目を喫し危機的状況、グアルディオラ率いる王者マンチェスター・Cは全勝街道",
      excerpt: "ブライトンがトッテナムを3-2で下した歴史的大逆転劇により、トッテナムの守備崩壊が浮き彫りとなる一方、マンCが首位を堅持。",
      body: [
        "インターナショナルブレイク前最後のリーグ戦で、ブライトンが後半わずか18分で3ゴールを奪いトッテナムに逆転勝利しました。",
        "トッテナムは今季リードした状況から早くも10ポイントを失っており、ポステコグルー監督への批判が高まっています。",
        "首位マンチェスター・シティは7戦全勝の勝ち点21と圧倒的な強さを見せ、完璧な状態で代表ウィークを迎えます。",
      ],
    },
    ko: {
      title: "프리미어리그 7라운드 결산: 토트넘, 브라이턴전 역전패로 충격 위기… 맨시티 7연승 승점 21 단독 선두",
      subtitle: "토트넘 리드 상황에서 이번 시즌에만 승점 10점 헌납, 과르디올라의 맨시티는 전승으로 A매치 휴식기 돌입",
      excerpt: "브라이턴의 3-2 대역전극으로 토트넘이 최악의 부진에 빠진 가운데, 맨체스터 시티는 7전 전승으로 리그 1위를 굳건히 지켰다.",
      body: [
        "아멕스 스타디움에서 열린 7라운드 마지막 경기에서 토트넘이 전반 2-0 리드를 지키지 못하고 18분 만에 3골을 내주며 무너졌습니다.",
        "토트넘은 올 시즌 리드하던 경기에서만 승점 10점을 날리며 20위로 추락해 포스테코글루 감독의 입지가 위태로워졌습니다.",
        "반면 맨체스터 시티는 7경기 전승(승점 21)을 기록하며 아스널을 승점 3점 차로 따돌리고 완벽한 1위를 질주하고 있습니다.",
      ],
    },
    ar: {
      title: "الدوري الإنجليزي الجولة 7 حصاد: توتنهام يترنح بعد ريمونتادا برايتون ومانشستر سيتي بالعلامة الكاملة بـ 21 نقطة",
      subtitle: "السبيرز يفقدون النقطة العاشرة من وضعية التقدم هذا الموسم بينما تواصل كتيبة غوارديولا التحليق في الصدارة.",
      excerpt: "أشعلت عودة برايتون التاريخية بنتيجة 3-2 أمام توتنهام نيران الأزمة في شمال لندن بينما يحلق مانشستر سيتي وحيداً برصيد 21 نقطة.",
      body: [
        "أسدلت الجولة السابعة من الدوري الإنجليزي الستار على واحدة من أكثر المباريات إثارة بعد ريمونتادا برايتون الخارقة في الشوط الثاني.",
        "تسببت الهزيمة في بقاء توتنهام في قاع الترتيب برصيد نقطتين فقط بعدما خسر 10 نقاط كاملة من مباريات كان متقدماً فيها.",
        "في المقابل، يغادر مانشستر سيتي إلى فترة التوقف الدولي برصيد 21 نقطة من سبعة انتصارات متتالية وبفارق مريح عن ملاحقيه.",
      ],
    },
  },
  'wnba-semifinals-game2-liberty-aces-lynx-fever-2026': {
    fr: {
      title: "Demi-finales WNBA Match 2 : les Aces et le Fever sous pression maximale face au Liberty et aux Lynx",
      subtitle: "Becky Hammon exige de la discipline après 18 pertes de balle tandis que Caitlin Clark et Indiana préparent la riposte.",
      excerpt: "Menées 1-0 dans leurs séries, les formations de Las Vegas et d'Indiana affrontent un Match 2 couperet pour préserver leurs rêves de titre.",
      body: [
        "Dans l'histoire des playoffs WNBA au meilleur des cinq manches, une seule équipe a réussi à combler un retard de 0-2.",
        "Le Liberty a étouffé les Aces au Match 1 grâce à 34 points de Breanna Stewart, poussant Becky Hammon à revoir totalement son jeu de passes pour libérer A'ja Wilson.",
        "À Minneapolis, Caitlin Clark et le Fever veulent s'appuyer sur leur formidable quatrième quart-temps pour égaliser face aux Lynx de Napheesa Collier.",
      ],
    },
    es: {
      title: "Semifinales WNBA Partido 2: Aces y Fever ante una prueba de fuego frente a Liberty y Lynx",
      subtitle: "Becky Hammon exige disciplina defensiva tras 18 pérdidas mientras Caitlin Clark e Indiana buscan dar la sorpresa.",
      excerpt: "Con desventaja de 1-0, Las Vegas Aces e Indiana Fever afrontan un segundo asalto a vida o muerte para no caer en un peligroso 0-2.",
      body: [
        "La historia de la WNBA es demoledora: un 0-2 en contra en semifinales sólo se ha remontado en una ocasión en 25 precedentes.",
        "Las Aces necesitan cuidar el balón y generar mejores espacios para A'ja Wilson ante un Liberty liderado por una incontenible Breanna Stewart.",
        "En el Target Center, Caitlin Clark intentará mantener el acierto del último cuarto para robar el factor cancha a las Lynx de Napheesa Collier.",
      ],
    },
    de: {
      title: "WNBA-Halbfinale Spiel 2: Aces und Fever stehen gegen Liberty und Lynx mit dem Rücken zur Wand",
      subtitle: "Becky Hammon fordert Disziplin nach 18 Ballverlusten, während Caitlin Clark und Indiana den Konter planen.",
      excerpt: "Nach den Auftaktniederlagen stehen die Las Vegas Aces und das Indiana Fever in Spiel 2 vor entscheidenden Auswärtsprüfungen.",
      body: [
        "In der Geschichte der WNBA-Playoffs hat sich ein 0:2-Rückstand in Best-of-Five-Serien zu 96 Prozent als Endstation erwiesen.",
        "Die New York Liberty dominierten Spiel 1 dank 34 Punkten von Breanna Stewart, weshalb die Aces A'ja Wilson besser in Szene setzen müssen.",
        "In Minneapolis hofft Indiana auf die Fortsetzung von Caitlin Clarks furioser Schlussoffensive, um gegen die Lynx auszugleichen.",
      ],
    },
    it: {
      title: "Semifinali WNBA Gara 2: Aces e Fever alla prova del nove contro Liberty e Lynx",
      subtitle: "Becky Hammon invoca disciplina dopo 18 palle perse mentre Caitlin Clark e Indiana cercano il colpo esterno.",
      excerpt: "Sotto 1-0 nelle serie, Las Vegas Aces e Indiana Fever scendono in campo martedì sera in due sfide decisive per non scivolare sullo 0-2.",
      body: [
        "Nella storia della postseason WNBA, rimontare uno 0-2 in una serie al meglio delle cinque gare è riuscito solo nel 4% dei casi.",
        "Le bi-campionesse di Las Vegas devono limitare le palle perse per contenere il contropiede di New York orchestrato da Breanna Stewart.",
        "Al Target Center, le Fever di Caitlin Clark puntano sulla velocità per scardinare l'ermetica difesa delle Minnesota Lynx di Collier.",
      ],
    },
    pl: {
      title: "Półfinały WNBA Mecz nr 2: Aces i Fever przed arcytrudnym zadaniem przeciwko Liberty i Lynx",
      subtitle: "Becky Hammon żąda dyscypliny po 18 stratach, a Caitlin Clark i Indiana szykują rewanż w Target Center.",
      excerpt: "Przegrywając 0-1 w serii, Las Vegas Aces oraz Indiana Fever stają przed meczami o życie, by uniknąć stanu 0-2.",
      body: [
        "W historii play-offów WNBA tylko jednej drużynie udało się podnieść ze stanu 0-2 w serii do trzech zwycięstw.",
        "New York Liberty zdominowały mecz otwarcia za sprawą 34 punktów Breanny Stewart, zmuszając obrończynie tytułu do natychmiastowych korekt.",
        "W Minneapolis Caitlin Clark i Indiana Fever zrobią wszystko, by przełamać znakomitą defensywę Minnesota Lynx i wyrównać stan rywalizacji.",
      ],
    },
    zh: {
      title: "WNBA半决赛G2决战：王牌与狂热客场生死战，自由人与山猫剑指2-0赛点",
      subtitle: "贝基-哈蒙严抓失误命门力争破局，克拉克率印第安纳狂热客战标靶中心渴望复仇",
      excerpt: "大比分0-1落后的卫冕冠军拉斯维加斯王牌与印第安纳狂热在周二客场迎来生死攸关的第二战，力求避免陷入0-2绝境。",
      body: [
        "在WNBA五战三胜制的半决赛历史上，0-2落后的球队最终被淘汰的概率高达96%，G2成为真正的生死天王山。",
        "自由人首战凭借斯图尔特的34分和防守统治力拿下王牌，哈蒙教练要求全队减少18次失误，为威尔逊创造更好的低位出手机会。",
        "在明尼阿波利斯，凯特琳-克拉克希望延续G1第四节独得14分的反扑气势，带领狂热冲垮常规赛冠军山猫的阵地防守。",
      ],
    },
    ja: {
      title: "WNBA準決勝第2戦：初戦を落としたエーシズとフィーバー、王手を防ぐ運命のアウェー戦へ",
      subtitle: "ハモンHCは18ターンオーバーの修正を厳命、クラーク率いるフィーバーはミネソタ攻略に挑む",
      excerpt: "リバティとリンクスに先勝を許したエーシズとフィーバーが、0-2の崖っぷちを回避すべく火曜夜の第2戦へ挑む。",
      body: [
        "WNBAプレーオフの5戦3勝制において、0勝2敗から逆転勝利を収めた例は歴代でわずか4%しか存在しません。",
        "スチュワートに34点を許したエーシズは、ウィルソンへのパス供給ラインを再構築しリバティの速攻を阻止する必要があります。",
        "ターゲット・センターでは、フィーバーのエース・クラークがリンクスの強力な包囲網を破り1勝1敗のタイに持ち込めるかが注目されます。",
      ],
    },
    ko: {
      title: "WNBA 준결승 2차전: 벼랑 끝 에이시스와 피버, 리버티와 링스 상대로 원정 반격 출격",
      subtitle: "베키 해먼 감독 18실책 설욕 다짐, 케이틀린 클라크는 타깃 센터에서 원정 1승 정조준",
      excerpt: "1차전을 내준 라스베이거스 에이시스와 인디애나 피버가 0-2 위기를 피하기 위해 화요일 2차전 총력전에 나선다.",
      body: [
        "WNBA 5전 3선승제 역사상 0-2로 뒤진 팀의 챔프전 진출 확률은 4%에 불과해 2차전은 사실상의 결승전입니다.",
        "뉴욕 리버티는 스튜어트의 34점 원맨쇼로 1차전을 챙겼으며, 에이시스는 에이자 윌슨의 공간 창출을 위한 전술 수정에 나섰습니다.",
        "미네소타에서는 나피사 콜리어의 링스를 상대로 케이틀린 클라크가 4쿼터 폭발력을 재현해 원정 승리를 노립니다.",
      ],
    },
    ar: {
      title: "نصف نهائي WNBA المباراة 2: إيسز وفيفر في مواجهة مصيرية أمام ليبرتي ولينكس لتفادي التأخر 0-2",
      subtitle: "بيكي هامون تطالب بانضباط تكتيكي صارم وكيتلين كلارك تقود إنديانا لمحاولة كسر تفوق مينيسوتا.",
      excerpt: "يدخل لاس فيغاس إيسز وإنديانا فيفر مواجهتي الثلاثاء بشعار الفوز ولا بديل عنه لتفادي التأخر بنتيجة 0-2 في نصف نهائي WNBA.",
      body: [
        "تاريخياً في دوري WNBA، نجح فريق واحد فقط من أصل 25 في العودة من التأخر بنتيجة 0-2 في سلسلة من خمس مباريات.",
        "يسعى إيسز بقيادة إيجا ويلسون لتقليص الأخطاء الهجومية أمام دفاع نيويورك ليبرتي القوي ونجمته بريانا ستيوارت.",
        "وفي مينيابوليس، تأمل كيتلين كلارك في استثمار صحوتها الهجومية المتأخرة لقيادة فيفر لتحقيق انتصار ثمين أمام لينكس.",
      ],
    },
  },
  'shanghai-masters-2026-r1-wawrinka-nishikori-alcaraz-preview': {
    fr: {
      title: "Rolex Shanghai Masters : Wawrinka entre dans l'histoire à 39 ans, Nishikori enchaîne avant l'entrée des favoris",
      subtitle: "Le Suisse devient le 3e vainqueur le plus âgé en Masters 1000 pendant qu'Alcaraz, Sinner et Djokovic préparent leur entrée.",
      excerpt: "Stan Wawrinka a signé un exploit historique en dominant Safiullin tandis que Kei Nishikori a renversé Navone lors du premier tour à Shanghai.",
      body: [
        "À 39 ans et six mois, Stan Wawrinka a ébloui la Qizhong Arena avec 38 coups gagnants pour dominer Roman Safiullin 7-5, 7-6.",
        "Le Suisse devient le troisième joueur le plus âgé de l'histoire à remporter un match en Masters 1000 après Connors et Karlovic.",
        "Kei Nishikori s'est également qualifié en trois sets alors que Carlos Alcaraz, Jannik Sinner et Novak Djokovic peaufinent leurs débuts au deuxième tour.",
      ],
    },
    es: {
      title: "Rolex Shanghai Masters: Wawrinka hace historia a los 39 años y Nishikori avanza antes del debut de los favoritos",
      subtitle: "El suizo se convierte en el tercer ganador más veterano en Masters 1000 mientras Alcaraz, Sinner y Djokovic afinan detalles.",
      excerpt: "Stan Wawrinka firmó una gesta inolvidable ante Safiullin y Kei Nishikori remontó ante Navone en una vibrante jornada en Shanghái.",
      body: [
        "Con un revés a una mano magistral, Stan Wawrinka superó 7-5, 7-6 a Roman Safiullin en el Qizhong Arena a sus 39 años y medio.",
        "Wawrinka se une a Jimmy Connors e Ivo Karlovic como los únicos jugadores de mayor edad en ganar un partido de Masters 1000.",
        "Kei Nishikori también avanzó tras remontar ante Navone, mientras Carlos Alcaraz, Jannik Sinner y Novak Djokovic preparan sus estrenos.",
      ],
    },
    de: {
      title: "Rolex Shanghai Masters: Wawrinka schreibt mit 39 Jahren Geschichte, Nishikori siegt vor Auftritt der Topstars",
      subtitle: "Der Schweizer wird zum drittältesten Matchgewinner der Masters-1000-Geschichte, während Alcaraz, Sinner und Djokovic warten.",
      excerpt: "Stan Wawrinka triumphierte mit 38 Winnern über Safiullin und Kei Nishikori kämpfte sich in drei Sätzen in Runde zwei von Shanghai.",
      body: [
        "Stan Wawrinka begeisterte das Publikum in der Qizhong Arena und bezwang Roman Safiullin im Alter von 39 Jahren mit 7:5, 7:6.",
        "Damit ist Wawrinka nach Jimmy Connors und Ivo Karlovic der drittälteste Spieler mit einem Matcherfolg auf Masters-1000-Ebene.",
        "Auch Kei Nishikori meldete sich mit einem Dreisatzsieg zurück, während Carlos Alcaraz und Jannik Sinner vor ihren Auftaktpartien stehen.",
      ],
    },
    it: {
      title: "Rolex Shanghai Masters: Wawrinka nella storia a 39 anni, Nishikori avanza prima dei big",
      subtitle: "Lo svizzero diventa il terzo vincitore più anziano nei Masters 1000 mentre Alcaraz, Sinner e Djokovic preparano l'esordio.",
      excerpt: "Stan Wawrinka batte Safiullin con 38 vincenti e Kei Nishikori rimonta Navone in un martedì memorabile a Shanghai.",
      body: [
        "A 39 anni e sei mesi, Stan Wawrinka ha incantato la Qizhong Arena piegando Roman Safiullin 7-5, 7-6 con il suo proverbiale rovescio.",
        "Il campione elvetico è ora il terzo tennista più anziano a vincere una partita nei Masters 1000 dopo Connors e Karlovic.",
        "Avanza anche Kei Nishikori al terzo set, mentre Carlos Alcaraz, Jannik Sinner e Novak Djokovic sono pronti al debutto nel secondo turno.",
      ],
    },
    pl: {
      title: "Rolex Shanghai Masters: 39-letni Wawrinka pisze historię, Nishikori gra dalej przed wejściem faworytów",
      subtitle: "Szwajcar trzecim najstarszym zwycięzcą meczu w historii Masters 1000, podczas gdy Alcaraz, Sinner i Djoković czekają na start.",
      excerpt: "Stan Wawrinka pokonał Safiullina po popisie 38 zagrań kończących, a Kei Nishikori awansował po trzysetowym boju w Szanghaju.",
      body: [
        "Stan Wawrinka w wieku 39 lat zachwycił fanów w Qizhong Arena, wygrywając z Romanem Safiullinem 7-5, 7-6.",
        "Szwajcarski mistrz ustępuje pod względem wieku wygranej w Masters 1000 jedynie Jimmy'emu Connorsowi i Ivo Karloviciowi.",
        "Kei Nishikori również zameldował się w 2. rundzie, a do gry szykują się Carlos Alcaraz, Jannik Sinner oraz Novak Djoković.",
      ],
    },
    zh: {
      title: "上海劳力士大师赛：39岁瓦林卡创历史成为大师赛第三年长胜者，锦织圭逆转晋级",
      subtitle: "瑞士老将旗忠网球中心轰出38记制胜分，阿尔卡拉斯、辛纳与德约科维奇严阵以待次轮首秀",
      excerpt: "39岁老将瓦林卡两盘力克萨菲乌林跻身历史前三，锦织圭三盘逆转纳沃内，上海大师赛首轮全面战罢顶尖种子即将登场。",
      body: [
        "在上海旗忠森林网球中心，39岁零6个月的瓦林卡用招牌单反狂轰38记制胜分，以7-5、7-6(3)击败萨菲乌林闯入第二轮。",
        "瓦林卡借此成为ATP大师赛历史上第三年长的单打获胜者，仅次于康纳斯与卡洛维奇。",
        "日本名将锦织圭同样激战三盘逆转纳沃内，而阿尔卡拉斯、辛纳和四届赛会冠军德约科维奇已完成备战蓄势待发。",
      ],
    },
    ja: {
      title: "上海ロレックス・マスターズ：39歳ワウリンカが歴代3位の年長勝利記録を樹立、錦織圭も逆転で初戦突破",
      subtitle: "スイスの巨星が38本のウィナーでサフィウリンを撃破、アルカラスやシナーら上位シードが2回戦へ",
      excerpt: "39歳のスタン・ワウリンカがマスターズ1000歴代3位の年長勝利を挙げ、錦織圭もフルセットで勝利し上海の舞台で輝きを放った。",
      body: [
        "旗忠アリーナでスタン・ワウリンカが代名詞の片手バックハンドを武器にサフィウリンを7-5、7-6で退けました。",
        "39歳6カ月での勝利は、ジミー・コナーズとイボ・カルロビッチに次ぐマスターズ1000史上3番目の年長記録です。",
        "錦織圭もナヴォーネに逆転勝ちを収め、水曜日からはアルカラス、シナー、ジョコビッチらシード勢が登場します。",
      ],
    },
    ko: {
      title: "상하이 롤렉스 마스터스: 39세 바브린카 역대 3위 최고령 승리 신기록, 니시코리도 1회전 통과",
      subtitle: "스위스 베테랑 38개 위너로 사피울린 제압, 알카라스·시너·조코비치는 2회전 출격 대기",
      excerpt: "39세의 스탄 바브린카가 마스터스 1000 역대 3위 최고령 승리를 거뒀고, 니시코리 케이도 역전승을 거두며 상하이 본선 2회전에 올랐다.",
      body: [
        "치중 아레나에서 열린 경기에서 39세 6개월의 스탄 바브린카가 사피울린을 7-5, 7-6(3)으로 꺾고 노익장을 과시했습니다.",
        "바브린카는 코너스와 카를로비치에 이어 ATP 마스터스 1000 역사상 세 번째로 많은 나이에 승리를 따낸 선수가 됐습니다.",
        "니시코리도 풀세트 접전 끝에 나보네를 꺾었으며, 알카라스와 시너, 조코비치가 수요일부터 본격적인 우승 사냥에 나섭니다.",
      ],
    },
    ar: {
      title: "بطولة شنغهاي للأساتذة: فافرينكا يدخل التاريخ بعمر 39 عاماً ونيشيكوري يتأهل بانتظار الكبار",
      subtitle: "النجم السويسري يصبح ثالث أكبر لاعب يحقق فوزاً في بطولات الماسترز بينما يستعد ألكاراز وسينر للظهور الأول.",
      excerpt: "حقق ستان فافرينكا إنجازاً تاريخياً بتغلبه على سافيولين بينما قلب نيشيكوري تأخره ليعبر للدور الثاني في شنغهاي.",
      body: [
        "أمتع النجم السويسري ستان فافرينكا جماهير صالة كيتشونغ بضرباته الخلفية الساحرة وتفوق على رومان سافيولين 7-5 و7-6.",
        "وأصبح فافرينكا بعمر 39 عاماً وستة أشهر ثالث أكبر لاعب يفوز بمباراة في بطولات الماسترز 1000 عبر التاريخ.",
        "وعبر الياباني كي نيشيكوري بثلاث مجموعات، في حين يترقب الجميع انطلاقة ألكاراز وسينر وجوكوفيتش في الدور الثاني.",
      ],
    },
  },
  'nfl-week5-power-rankings-chiefs-vikings-lions-surge-2026': {
    fr: {
      title: "NFL 5e semaine : les Vikings et les Chiefs seuls invaincus, les Lions grimpent sur le podium après le récital de Goff",
      subtitle: "Le classement bousculé au quart de la saison tandis qu'Atlanta et Tampa Bay lancent le Thursday Night Football.",
      excerpt: "Avec Minnesota et Kansas City à 4-0 et l'attaque historique des Lions de Detroit, la hiérarchie de la NFL est totalement redistribuée.",
      body: [
        "Après quatre semaines, seules deux équipes affichent un bilan parfait de 4-0 : les Chiefs de Mahomes et les surprenants Vikings de Darnold.",
        "Les Lions de Detroit grimpent au troisième rang des power rankings après le match historique à 18/18 de Jared Goff face à Seattle.",
        "La 5e semaine s'ouvre jeudi soir avec un duel brûlant de NFC South entre les Falcons de Cousins et les Buccaneers de Mayfield.",
      ],
    },
    es: {
      title: "NFL Semana 5: Vikings y Chiefs son los únicos invictos y los Lions suben al podio tras la perfección de Goff",
      subtitle: "El orden de la liga cambia al completarse el primer cuarto de temporada con Atlanta y Tampa Bay abriendo el jueves.",
      excerpt: "Minnesota y Kansas City comandan la NFL con 4-0 mientras Detroit desata la ofensiva más temible tras la exhibición de Goff.",
      body: [
        "Un mes de competición ha dejado únicamente a dos franquicias invictas: los vigentes campeones Chiefs y los asombrosos Vikings de Sam Darnold.",
        "Los Lions se sitúan entre los tres mejores equipos tras el partido de 18 de 18 pases de Jared Goff y el dominio de Gibbs y Montgomery.",
        "La semana 5 arranca este jueves en Atlanta con un choque crucial de la NFC South entre los Falcons y los Buccaneers.",
      ],
    },
    de: {
      title: "NFL Woche 5: Vikings und Chiefs als letzte Ungeschlagene, Lions stürmen nach Goff-Gala in die Top 3",
      subtitle: "Machtgefüge der Liga nach vier Wochen neu geordnet; Atlanta und Tampa Bay eröffnen Thursday Night Football.",
      excerpt: "Minnesota und Kansas City thronen mit 4:0 an der Spitze der NFL, während die Lions nach Goffs historischem 18-von-18-Auftritt glänzen.",
      body: [
        "Nach dem ersten Saisonviertel haben nur noch die Kansas City Chiefs und die Minnesota Vikings eine weiße Weste von 4:0.",
        "Die Detroit Lions schoben sich nach Jared Goffs Rekordspiel gegen Seattle auf Platz drei der ligaweiten Power Rankings vor.",
        "Woche 5 beginnt bereits am Donnerstagabend mit dem prestigeträchtigen NFC-South-Duell zwischen Falcons und Buccaneers.",
      ],
    },
    it: {
      title: "NFL Week 5: Vikings e Chiefs uniche imbattute, Lions sul podio dopo la perfezione di Goff",
      subtitle: "I power ranking rivoluzionano la lega al primo quarto di stagione; Falcons e Buccaneers aprono il giovedì.",
      excerpt: "Minnesota e Kansas City guidano la NFL sul 4-0 mentre Detroit vola tra le prime tre grazie al 18 su 18 storico di Goff.",
      body: [
        "Soltanto Kansas City e Minnesota restano a punteggio pieno (4-0) dopo quattro turni di una stagione NFL imprevedibile.",
        "I Detroit Lions si issano al terzo posto assoluto nei ranking grazie all'attacco stellare guidato dal perfetto Jared Goff.",
        "La quinta settimana si apre giovedì notte ad Atlanta con lo scontro al vertice della NFC South tra Falcons e Buccaneers.",
      ],
    },
    pl: {
      title: "NFL Tydzień 5: Vikings i Chiefs jedynymi niepokonanymi, Lions w czołowej trójce po perfekcyjnym występie Goffa",
      subtitle: "Układ sił w lidze wywrócony po pierwszej ćwiartce sezonu; Falcons i Buccaneers otwierają Thursday Night Football.",
      excerpt: "Minnesota i Kansas City prowadzą z bilansem 4-0, a Detroit Lions awansowali do czołówki po historycznym meczu Jareda Goffa.",
      body: [
        "Po czterech tygodniach rywalizacji tylko Minnesota Vikings i Kansas City Chiefs mogą pochwalić się bilansem 4-0.",
        "Detroit Lions wskoczyli na trzecie miejsce w rankingach siły po popisie Goffa, który nie pomylił się ani razu w 18 rzutach.",
        "Tydzień 5 rozpocznie się już w czwartek w Atlancie od starcia dywizyjnego Falcons z Tampa Bay Buccaneers.",
      ],
    },
    zh: {
      title: "NFL第5周实力榜：维京人与酋长成仅存不败之师，高夫完美一战助雄狮挺进前三",
      subtitle: "赛季首个四分之一节点格局大洗牌，猎鹰与海盗周四夜赛拉开第5周战幕",
      excerpt: "明尼苏达维京人与堪萨斯城酋长以4胜0负傲视全联盟，底特律雄狮凭借高夫的历史级表现飙升至实力榜第三位。",
      body: [
        "2026赛季常规赛战罢四周，仅剩酋长与维京人两支4胜0负的全胜球队屹立不倒。",
        "雄狮队四分卫高夫在周一夜赛打出18投18中的神迹，带领底特律冲上联盟实力榜前三，展现出摧枯拉朽的进攻火力。",
        "第5周首战将于周四夜赛打响，亚特兰大猎鹰主场迎战坦帕湾海盗，展开国联南区焦点对话。",
      ],
    },
    ja: {
      title: "NFL第5週：バイキングスとチーフスが無敗を維持、ゴフの完璧劇でライオンズがトップ3に浮上",
      subtitle: "第1クォーター終了時点でパワーランキングが激変、ファルコンズ対バッカニアーズでTNF開幕へ",
      excerpt: "開幕4連勝のバイキングスとチーフスが首位を走り、ゴフが歴史を作ったライオンズがリーグ3位へと躍進した。",
      body: [
        "第4週を終えて全勝をキープしているのは、王者チーフスとダーノルド躍進のバイキングスの2チームのみとなりました。",
        "マンデーナイトでパス成功率100%を記録したジャレッド・ゴフ率いるライオンズがパワーランキング3位へ浮上しました。",
        "第5週は木曜夜のサーズデーナイトで幕を開け、ファルコンズとバッカニアーズがNFC南地区首位を争います。",
      ],
    },
    ko: {
      title: "NFL 5주차: 바이킹스와 치프스 유이한 4연승 무패 행진, 고프의 완벽투로 라이언스 톱3 진입",
      subtitle: "시즌 4분의 1 통과하며 파워랭킹 대격변, 팰컨스와 버커니어스의 TNF로 5주차 개막",
      excerpt: "미네소타와 캔자스시티가 4승 무패로 양대 콘퍼런스를 이끄는 가운데, 디트로이트 라이언스가 강력한 화력으로 리그 3위에 올랐다.",
      body: [
        "NFL 4주차가 끝난 현재 32개 구단 중 전승 팀은 캔자스시티 치프스와 미네소타 바이킹스 단 두 팀뿐입니다.",
        "디트로이트 라이언스는 18패스 100% 성공 신화를 쓴 재러드 고프의 활약에 힘입어 파워랭킹 3위로 수직 상승했습니다.",
        "5주차는 목요일 밤 애틀랜타 팰컨스와 탬파베이 버커니어스의 NFC 남부지구 맞대결로 화려하게 시작됩니다.",
      ],
    },
    ar: {
      title: "دوري NFL الأسبوع 5: فايكنغز وتشيفس الوحيدان دون هزيمة ولايونز يقتحم الثلاثي الأفضل بعد تألق غوف",
      subtitle: "انقلاب في موازين القوى بعد انقضاء ربع الموسم وفالكونز وبوكانيرز يفتتحان جولة الخميس.",
      excerpt: "ينفرد مينيسوتا فايكنغز وكانساس سيتي تشيفس بسجل 4-0 في حين يقفز ديترويت لايونز للمركز الثالث في تصنيف القوة.",
      body: [
        "بعد مرور أربعة أسابيع من الإثارة، بقي كانساس سيتي ومينيسوتا فايكنغز فقط بسجل ناصع البياض دون أي خسارة.",
        "وقفز ديترويت لايونز للمركز الثالث عالمياً بفضل ليلة جاريد غوف التاريخية بإكمال 18 تمريرة من أصل 18 أمام سياتل.",
        "وتنطلق الجولة الخامسة مساء الخميس بمواجهة قوية تجمع أتلانتا فالكونز ضد تامبا باي بوكانيرز في صراع الصدارة.",
      ],
    },
  },
  'international-break-nations-league-md3-preview-spurs-inquest-2026': {
    fr: {
      title: "Trêve internationale : la Ligue des Nations propose un choc Italie - Belgique pendant la pause des clubs",
      subtitle: "Les Azzurri visent un sans-faute en Ligue A tandis que Tottenham médite son effondrement face à Brighton.",
      excerpt: "Avec Manchester City solide leader à 21 points, les championnats s'arrêtent pour laisser place aux affiches internationales.",
      body: [
        "Après sept journées folles en Europe, les stars rejoignent leurs sélections nationales pour la Ligue des Nations et les éliminatoires du Mondial 2026.",
        "Le Stadio Olimpico de Rome accueille jeudi une affiche royale entre l'Italie de Spalletti et une Belgique rajeunie privée de De Bruyne et Lukaku.",
        "Pendant ce temps à Londres, Tottenham et Ange Postecoglou disposent de deux semaines d'introspection après avoir concédé 10 points en menant au score.",
      ],
    },
    es: {
      title: "Parón de selecciones: la Nations League trae un Italia - Bélgica de campanillas con las ligas en pausa",
      subtitle: "La Azzurra busca mantener su pleno en la Liga A mientras el Tottenham analiza su derrumbe ante el Brighton.",
      excerpt: "Con el Manchester City intratable con 21 puntos, los clubes dan paso a las selecciones en una apasionante jornada continental.",
      body: [
        "El fútbol europeo de clubes se detiene con el Manchester City en lo más alto para dar paso a la ventana internacional de octubre.",
        "El choque estelar medirá en Roma a la renacida Italia de Luciano Spalletti contra una Bélgica en transición sin De Bruyne ni Lukaku.",
        "En Inglaterra, el Tottenham encara dos semanas de terapia interna tras haber dilapidado diez puntos en ventajas desperdiciadas.",
      ],
    },
    de: {
      title: "Länderspielpause: Nations League lockt mit Italien gegen Belgien, während die Klubligen pausieren",
      subtitle: "Azzurri wollen Erfolgsserie ausbauen, während Tottenham den Brighton-Schock verarbeiten muss.",
      excerpt: "Während Manchester City mit 21 Punkten souverän führt, ruht der Klubfußball für Länderspiel-Kracher in Rom und London.",
      body: [
        "Die europäischen Top-Ligen gehen in die Länderspielpause, angeführt von Guardiolas makellosem Manchester City.",
        "Das Highlight der Nations League steigt im Stadio Olimpico, wo Italien auf ein neu formiertes belgisches Team trifft.",
        "Bei Tottenham Hotspur herrscht derweil Krisenstimmung nach 10 verspielten Punkten aus Führungspositionen.",
      ],
    },
    it: {
      title: "Sosta nazionali: la Nations League regala Italia - Belgio all'Olimpico mentre i club tirano il fiato",
      subtitle: "Gli Azzurri di Spalletti cercano il tris nel girone mentre il Tottenham medita sulla rimonta subita a Brighton.",
      excerpt: "Con il Manchester City a punteggio pieno a quota 21, i campionati si fermano per lasciare spazio alla Nations League.",
      body: [
        "La Serie A e la Premier League si fermano per due settimane per far spazio agli impegni delle selezioni nazionali.",
        "Giovedì sera l'Italia ospita il Belgio all'Olimpico di Roma per consolidare il primato nel Gruppo 2 della League A.",
        "Nel frattempo a Londra il Tottenham apre un processo interno dopo aver dilapidato dieci punti da situazione di vantaggio.",
      ],
    },
    pl: {
      title: "Przerwa reprezentacyjna: Liga Narodów przynosi hit Włochy - Belgia, kluby analizują początek sezonu",
      subtitle: "Azzurri chcą utrzymać komplet punktów, a Tottenham leczy rany po katastrofalnym meczu z Brighton.",
      excerpt: "Gdy Manchester City przewodzi stawce z kompletem 21 punktów, uwaga kibiców przenosi się na mecze Ligi Narodów UEFA.",
      body: [
        "Krajowe rozgrywki ligowe ustępują miejsca reprezentacjom narodowym walczącym w Lidze Narodów UEFA i eliminacjach MŚ.",
        "Hitem 3. kolejki będzie starcie w Rzymie pomiędzy odradzającymi się Włochami Luciano Spallettiego a Belgią.",
        "Tottenham ma przed sobą dwa tygodnie trudnych rozliczeń po stracie dziesiątego punktu z pozycji prowadzenia w Premier League.",
      ],
    },
    zh: {
      title: "国际比赛日打响：欧国联迎来意大利对阵比利时焦点战，英超诸强进入休整期",
      subtitle: "蓝衣军团力争A级三连胜，热刺两周间歇期闭门复盘被布莱顿逆转的惨痛失利",
      excerpt: "曼城豪取21分领跑英超进入间歇期，欧洲国家联赛第三轮即将打响，意大利坐镇罗马奥林匹克球场迎战比利时。",
      body: [
        "在欧洲俱乐部经历七周激战后，各国球星奔赴国家队备战10月国际比赛日及欧国联赛事。",
        "罗马奥林匹克球场周四将见证重头戏，斯帕莱蒂率领的意大利队迎战缺少德布劳内和卢卡库的比利时队。",
        "而在北伦敦，热刺主帅波斯特科格鲁将利用两周时间反思球队领先后狂丢10分的防守痼疾。",
      ],
    },
    ja: {
      title: "代表ウィーク開幕：欧州ネーションズリーグでイタリア対ベルギーのビッグマッチ、クラブ戦は中断",
      subtitle: "アズーリがリーグAで3連勝を狙う一方、逆転負けのスパーズは2週間の反省期間へ",
      excerpt: "マンチェスター・Cが開幕7連勝の21点で首位を独走する中、舞台はネーションズリーグ第3節の代表戦へ移行する。",
      body: [
        "欧州各国の国内リーグが中断し、選手たちはネーションズリーグやW杯予選に向けて代表合宿に合流しました。",
        "注目はローマのスタディオ・オリンピコで行われるイタリア対ベルギーの強豪対決です。",
        "一方、ブライトン戦で手痛い逆転負けを喫したトッテナムは、守備崩壊の原因究明に追われています。",
      ],
    },
    ko: {
      title: "A매치 휴식기 돌입: 네이션스리그 이탈리아 vs 벨기에 빅매치 개막, 클럽 축구 일시 중단",
      subtitle: "스팔레티호 아주리 군단 리그 A 3연승 도전, 토트넘은 브라이턴전 참사 복기 돌입",
      excerpt: "맨시티가 7전 전승 승점 21점으로 프리미어리그 선두를 굳힌 가운데, 대표팀 경기가 유럽 전역에서 펼쳐진다.",
      body: [
        "유럽 리그가 10월 A매치 휴식기에 돌입하며 UEFA 네이션스리그 3라운드 일정에 돌입했습니다.",
        "로마 올림피코 스타디움에서는 2연승을 달리는 이탈리아와 세대교체 중인 벨기에의 빅매치가 열립니다.",
        "올 시즌 리드 상황에서만 승점 10점을 날린 토트넘은 2주간의 뼈아픈 자체 쇄신 시간을 갖게 됩니다.",
      ],
    },
    ar: {
      title: "فترة التوقف الدولي: دوري الأمم الأوروبية يشهد قمة إيطاليا ضد بلجيكا وتوقف المنافسات المحلية",
      subtitle: "الآزوري يستهدف العلامة الكاملة في المستوى الأول وتوتنهام يعيد ترتيب أوراقه بعد صدمة برايتون.",
      excerpt: "مع تحليق مانشستر سيتي في صدارة البريميرليغ برصيد 21 نقطة، تتجه الأنظار نحو قمة إيطاليا وبلجيكا في روما.",
      body: [
        "تتوقف الدوريات الأوروبية لمدة أسبوعين لافساح المجال أمام مباريات دوري الأمم الأوروبية وتصفيات كأس العالم.",
        "ويحتضن الملعب الأولمبي في روما مواجهة من العيار الثقيل تجمع إيطاليا ضد بلجيكا في الجولة الثالثة.",
        "وفي لندن، يقضي توتنهام فترة التوقف في مراجعة شاملة بعد خسارته 10 نقاط كاملة من مباريات كان متقدماً فيها.",
      ],
    },
  },
  'f1-americas-preview-lawson-red-bull-audition-norris-chase-2026': {
    fr: {
      title: "F1 tournée américaine : Liam Lawson entame son grand test chez RB, Red Bull prépare sa riposte à Austin",
      subtitle: "L'écurie autrichienne prépare un nouveau fond plat à Milton Keynes pendant que Lawson joue son avenir sur six courses.",
      excerpt: "Avec McLaren en tête des constructeurs avec 41 points d'avance, Red Bull prépare des évolutions majeures pour Austin tandis que Lawson remplace Ricciardo.",
      body: [
        "La pause automnale de la Formule 1 est le théâtre d'une course acharnée au développement entre McLaren et Red Bull.",
        "Red Bull finalise pour Austin un fond plat entièrement redessiné afin d'enrayer la remontée spectaculaire de Lando Norris.",
        "Titularisé chez RB, le Néo-Zélandais Liam Lawson sait que ses six courses serviront de test direct pour le baquet de Sergio Perez en 2027.",
      ],
    },
    es: {
      title: "F1 previa de América: Liam Lawson inicia su examen en RB y Red Bull prepara su réplica técnica para Austin",
      subtitle: "Red Bull diseña un nuevo fondo en Milton Keynes mientras Lawson se juega un asiento en el equipo grande para 2027.",
      excerpt: "McLaren defiende 41 puntos de ventaja en constructores mientras Red Bull ultima un paquete clave para COTA y debuta Lawson.",
      body: [
        "El parón otoñal de la F1 se vive con máxima intensidad en las fábricas ante el inminente triplete americano.",
        "Red Bull llevará a Austin un suelo revisado para corregir los problemas de equilibrio del RB20 frente al dominio de McLaren.",
        "El joven Liam Lawson tendrá seis carreras con RB para demostrar que merece el asiento de Sergio Pérez la próxima temporada.",
      ],
    },
    de: {
      title: "F1 Amerika-Vorschau: Liam Lawson startet RB-Bewerbung, Red Bull rüstet für Austin auf",
      subtitle: "Red Bull entwickelt neuen Unterboden in Milton Keynes, während Lawson um seine Zukunft für 2027 kämpft.",
      excerpt: "McLaren führt mit 41 Punkten Vorsprung, doch Red Bull plant für Austin ein großes Aerodynamik-Paket und testet Neuzugang Lawson.",
      body: [
        "Die Formel-1-Pause ist geprägt von hektischer Entwicklungsarbeit vor den drei Rennen auf dem amerikanischen Kontinent.",
        "Red Bull bringt für den Circuit of the Americas einen neuen Unterboden, um Norris und Piastri wieder Paroli bieten zu können.",
        "Liam Lawson übernimmt das RB-Cockpit von Ricciardo und steht vor einem intensiven Sechs-Rennen-Vorsprechen für Red Bull.",
      ],
    },
    it: {
      title: "F1 verso le Americhe: Lawson al test decisivo sulla RB, Red Bull prepara gli aggiornamenti per Austin",
      subtitle: "Il team di Milton Keynes sviluppa un nuovo fondo mentre il giovane neozelandese si gioca il futuro per il 2027.",
      excerpt: "McLaren vanta 41 punti di margine tra i costruttori ma Red Bull prepara la riscossa a COTA con sviluppi tecnici e l'esordio di Lawson.",
      body: [
        "La pausa autunnale della Formula 1 serve alle scuderie per affilare le armi prima del trittico americano.",
        "La Red Bull introdurrà ad Austin un fondo evoluto per risolvere i cronici problemi di sottosterzo emersi a Singapore.",
        "Tutti gli occhi saranno puntati anche su Liam Lawson, al volante della Racing Bulls per una sfida diretta con Tsunoda.",
      ],
    },
    pl: {
      title: "F1 przed wyścigami w Amerykach: Liam Lawson zaczyna test w RB, Red Bull szykuje pakiet poprawek na Austin",
      subtitle: "Red Bull projektuje nową podłogę w Milton Keynes, a Lawson walczy o stałe miejsce w stawce na 2027 rok.",
      excerpt: "McLaren ma 41 punktów przewagi, a Red Bull przygotowuje kluczowe poprawki na COTA, gdzie w barwach RB zadebiutuje Liam Lawson.",
      body: [
        "Przerwa w F1 to czas wytężonej pracy inżynierów w bazach zespołów przed wyścigami w USA, Meksyku i Brazylii.",
        "Red Bull przywiezie do Austin gruntownie zmodyfikowaną podłogę, by zneutralizować przewagę technologiczną McLarena.",
        "22-letni Liam Lawson staje przed życiową szansą w zespole RB, mając sześć wyścigów na przekonanie do siebie Helmuta Marko.",
      ],
    },
    zh: {
      title: "F1美洲前瞻：劳森入主RB开启六场大考，红牛奥斯汀备战重大底板升级阻击迈凯伦",
      subtitle: "米尔顿凯恩斯工厂紧锣密鼓赶制新套件，新西兰新星直面角田角逐2027红牛正席",
      excerpt: "迈凯伦以41分领跑车队积分榜，红牛将在奥斯汀推出关键空力升级包，利亚姆-劳森顶替里卡多迎来关键大考。",
      body: [
        "F1秋季休整期成为了迈凯伦与红牛两大豪门的研发军备竞赛，双方即将在奥斯汀展开美洲三连赛首战。",
        "红牛技术团队在新加坡失利后火速改进RB20底板和前翼结构，力保维斯塔潘的52分车手领先优势。",
        "22岁的新西兰新星劳森接替里卡多出战最后六场分站赛，这将是他争取2027年红牛主力席位的决定性面试。",
      ],
    },
    ja: {
      title: "F1アメリカ連戦展望：ローソンがRBで運命の6戦へ、レッドブルはオースティンで大改修投入へ",
      subtitle: "ミルトンキーンズで新フロアを緊急製造、リカルドの後任ローソンは2027年昇格へ向け角田と激突",
      excerpt: "マクラーレンが41点差でリードする中、レッドブルはオースティンに改良型フロアを投入し、ローソンがRBで出走する。",
      body: [
        "シンガポールでのノリス圧勝劇を受け、レッドブルはRB20のアンダーフロアを刷新する大型アップデートをオースティンに持ち込みます。",
        "リカルドに代わってRBのステアリングを握る22歳のリアム・ローソンは、角田裕毅との直接対決に挑みます。",
        "マクラーレンも好調を維持しており、サーキット・オブ・ジ・アメリカズでの初日から激しい開発戦争が火花を散らします。",
      ],
    },
    ko: {
      title: "F1 아메리카 프리뷰: 리암 로슨 RB서 운명의 6경기 돌입, 레드불 오스틴 대규모 업그레이드 준비",
      subtitle: "레드불 공장서 새 플로어 긴급 제작, 로슨은 2027시즌 콜업을 목표로 츠노다와 내부 경쟁",
      excerpt: "맥라렌이 컨스트럭터 41점 차 리드를 지키는 가운데, 레드불이 오스틴에서 공력 패키지를 선보이고 로슨이 RB 시트에 오른다.",
      body: [
        "F1 휴식기 동안 레드불은 싱가포르에서 드러난 머신 밸런스 문제를 해결하기 위해 오스틴에 대대적인 플로어 개선안을 투입합니다.",
        "대니얼 리카도를 대신해 RB에 합류한 리암 로슨은 잔여 6개 레이스에서 자신의 가치를 입증해야 합니다.",
        "맥라렌의 노리스가 52점 차로 페르스타펜을 맹추격하는 가운데 텍사스 COTA에서 타이틀 향방이 크게 요동칠 전망입니다.",
      ],
    },
    ar: {
      title: "فورمولا 1 ترقب الأمريكتين: ليام لوسون يبدأ اختباره الحاسم وريد بُل تجهز تحديثات أوستن",
      subtitle: "مصنع ريد بُل يسابق الزمن لتجهيز أرضية جديدة للسيارة بينما يخوض لوسون اختباراً من ستة سباقات لخطف مقعد 2027.",
      excerpt: "تدافع ماكلارين عن صدارتها بفارق 41 نقطة في حين تسعى ريد بُل للرد بقوة في حلبة أوستن مع الظهور الأول للوسون.",
      body: [
        "تشهد فترة التوقف سباق تطوير هندسي محموم بين ماكلارين وريد بُل قبل بدء جولات القارة الأمريكية.",
        "تجهز ريد بُل حزمة هوائية جديدة لتعديل أرضية سيارة فيرستابن لتقليص الفارق مع ماكلارين في حلبة كوتا.",
        "وسيكون النيوزيلندي ليام لوسون تحت مجهر المتابعة مع فريق RB بعد تعويضه لدانييل ريكاردو حتى نهاية الموسم.",
      ],
    },
  },
  'pga-tour-black-desert-utah-course-preview-mitchell-yu-2026': {
    fr: {
      title: "PGA Tour : le Black Desert Championship prépare ses grands débuts en Utah entre roche rouge et lave noire",
      subtitle: "Keith Mitchell et Beau Hossler cherchent une revanche alors que l'Utah accueille le PGA Tour pour la première fois depuis 1963.",
      excerpt: "Le PGA Tour pose ses valises dans le cadre grandiose de l'Utah après 61 ans d'absence pour une étape capitale de la FedExCup Fall.",
      body: [
        "Soixante-et-un ans après le dernier tournoi professionnel en Utah, le circuit PGA fait étape au spectaculaire Black Desert Resort.",
        "Le parcours serpente au milieu de coulées de lave volcanique noire et de falaises de grès rouge, offrant un décor unique au monde.",
        "Keith Mitchell et Beau Hossler comptent parmi les favoris tandis que Kevin Yu dispute son premier tournoi en tant que vainqueur sur le circuit.",
      ],
    },
    es: {
      title: "PGA Tour: el Black Desert Championship debuta en Utah entre cañones de roca roja y coladas de lava",
      subtitle: "Keith Mitchell y Beau Hossler buscan revancha mientras Utah vuelve al calendario del PGA Tour tras 61 años.",
      excerpt: "El circuito estadounidense regresa a Utah por primera vez desde 1963 en un recorrido volcánico deslumbrante con la salvación en juego.",
      body: [
        "El Black Desert Resort de Ivins acoge el esperado regreso del PGA Tour al estado de Utah seis décadas después.",
        "Diseñado por Tom Weiskopf, el campo combina calles de hierba esmeralda con campos de lava basáltica negra y acantilados rojizos.",
        "Jugadores al borde del top 125 como Keith Mitchell y Beau Hossler buscarán sellar su tarjeta para la temporada 2027.",
      ],
    },
    de: {
      title: "PGA Tour: Black Desert Championship feiert Premiere in Utah inmitten roter Felsen und schwarzer Lava",
      subtitle: "Keith Mitchell und Beau Hossler wollen Wiedergutmachung, während Utah erstmals seit 1963 wieder Schauplatz der PGA Tour ist.",
      excerpt: "Die PGA Tour kehrt nach 61 Jahren nach Utah zurück und gastiert auf dem spektakulären Kurs des Black Desert Resort.",
      body: [
        "Sechs Jahrzehnte nach den Utah Open 1963 schlägt die PGA Tour wieder im Bundesstaat Utah auf dem Black Desert Resort ab.",
        "Der von Tom Weiskopf gestaltete Kurs besticht durch den extremen Kontrast aus sattem Grün, schwarzem Vulkangestein und roten Canyons.",
        "Für Spieler im FedExCup-Fall-Rennen um die Top 125 bietet die Woche in Ivins eine überlebenswichtige Bewährungsprobe.",
      ],
    },
    it: {
      title: "PGA Tour: debutto da sogno nello Utah per il Black Desert Championship tra rocce rosse e lava nera",
      subtitle: "Keith Mitchell e Beau Hossler a caccia del riscatto mentre il circuito ritrova lo Utah dopo 61 anni.",
      excerpt: "Il PGA Tour sbarca nello spettacolare scenario dello Utah a oltre sessant'anni di distanza per una tappa cruciale della FedExCup Fall.",
      body: [
        "Il Black Desert Resort di Ivins ospita il PGA Tour segnando lo storico ritorno del grande golf nello Utah dal lontano 1963.",
        "Il tracciato disegnato da Weiskopf e Smith si snoda attraverso antiche colate laviche nere sotto imponenti falesie di arenaria rossa.",
        "Con i punti FedExCup Fall in palio, Keith Mitchell e il secondo classificato di Jackson Beau Hossler partono con i favori del pronostico.",
      ],
    },
    pl: {
      title: "PGA Tour: Black Desert Championship debiutuje w Utah pośród czerwonych skał i czarnej lawy",
      subtitle: "Keith Mitchell i Beau Hossler szukają rewanżu po Jackson, a tour wraca do Utah po raz pierwszy od 1963 roku.",
      excerpt: "PGA Tour wraca do stanu Utah po 61 latach przerwy na niesamowite pole golfowe Black Desert Resort wyciosane w wulkanicznej lawie.",
      body: [
        "Historyczny powrót PGA Tour do Utah po ponad 60 latach stał się faktem na zjawiskowym obiekcie Black Desert Resort w Ivins.",
        "Soczyście zielone fairwaye przecinają czarne pola bazaltowe na tle monumentalnych czerwonych klifów Snow Canyon.",
        "Keith Mitchell i Beau Hossler celują w zwycięstwo, walcząc o cenne punkty decydujące o utrzymaniu karty PGA Tour w czołowej 125.",
      ],
    },
    zh: {
      title: "美巡赛：黑沙漠锦标赛犹他首秀开杆在即，红岩峡谷与黑色火山熔岩见证保卡大战",
      subtitle: "米切尔与霍斯勒力争密西西比失利救赎，美巡赛时隔61年重返蜂窝之州展开秋季激战",
      excerpt: "美巡赛时隔61年重返犹他州，坐落于黑色玄武岩熔岩与红色砂岩悬崖之间的黑沙漠度假村迎来历史性首秀，联邦快递杯秋季保卡争夺升温。",
      body: [
        "继1963年犹他公开赛后，美巡赛时隔61年再度将正式赛事带回犹他州，落地鬼斧神工的黑沙漠度假村高尔夫球场。",
        "由汤姆-韦斯科夫设计的球场将翠绿的本特草球道巧妙融入1500年前火山爆发形成的黑色玄武岩中，与红色砂岩悬崖交相辉映。",
        "在杰克逊遗憾失利的米切尔和霍斯勒将全力冲击冠军，力保在联邦快递杯秋季排名前125位锁定下赛季全卡资格。",
      ],
    },
    ja: {
      title: "PGAツアー：ブラックデザート選手権がユタ州で歴史的開幕、赤色砂岩と黒い溶岩が織りなす絶景決戦",
      subtitle: "キース・ミッチェルとボウ・ホスラーが前戦の雪辱を期す、ユタ州で61年ぶりとなる公式戦へ",
      excerpt: "1963年以来となるユタ州でのPGAツアー公式戦がブラックデザートで開催。フェデックスカップ・フォールの生き残りをかけた戦いが幕を開ける。",
      body: [
        "トム・ワイスコフ設計のブラックデザート・リゾートは、1500年前の黒い玄武岩の溶岩流と赤い砂岩の峡谷に囲まれた息を呑む絶景コースです。",
        "ユタ州で61年ぶりとなるPGAツアー開催に、前週ジャクソンで悔し涙を呑んだミッチェルやホスラーがリベンジを誓います。",
        "来季のフルシード権獲得となるフェデックスカップ秋季ポイント上位125位を巡り、緊迫したサバイバルが繰り広げられます。",
      ],
    },
    ko: {
      title: "PGA 투어: 블랙 데저트 챔피언십 유타 역사적 개막, 붉은 협곡과 검은 용암석이 빚어낸 무대",
      subtitle: "키스 미첼과 보 호슬러 설욕 도전, 1963년 이후 61년 만에 유타주서 PGA 투어 공식전 개최",
      excerpt: "PGA 투어가 61년 만에 유타주로 복귀해 검은 화산암과 붉은 모래 암벽이 어우러진 블랙 데저트 리조트에서 가을 시리즈 경쟁을 이어간다.",
      body: [
        "1963년 유타 오픈 이후 61년 만에 유타주에 입성한 PGA 투어가 신설 대회인 블랙 데저트 챔피언십을 치릅니다.",
        "톰 와이스코프가 설계한 이 코스는 1500년 전 화산 분출로 형성된 검은 현무암 지대와 붉은 암벽이 절묘한 조화를 이룹니다.",
        "지난주 아쉽게 우승을 놓친 키스 미첼과 보 호슬러가 페덱스컵 가을 시리즈 125위 진입을 위해 배수의 진을 치고 출전합니다.",
      ],
    },
    ar: {
      title: "جولة PGA: بطولة بلاك ديزرت تستعد لظهورها التاريخي في يوتا وسط الصخور البركانية الحمراء والسوداء",
      subtitle: "كيث ميتشل وبو هوسلر يسعيان للتعويض مع عودة الجولة إلى ولاية يوتا لأول مرة منذ عام 1963.",
      excerpt: "تعود جولة PGA إلى ولاية يوتا بعد غياب دام 61 عاماً على مسار بلاك ديزرت الاستثنائي وسط اشتداد صراع بطاقات التأهل.",
      body: [
        "يسجل منتجع بلاك ديزرت في يوتا عودة تاريخية للجولة الأمريكية بعد انقطاع دام ستة عقود منذ بطولة يوتا المفتوحة عام 1963.",
        "يمتاز المسار بتصميم فريد يجمع بين مسارات العشب الأخضر وتدفقات الحمم البركانية السوداء وجدران الأخاديد الحمراء.",
        "ويدخل كيث ميتشل وبو هوسلر المنافسات بحثاً عن نقاط ثمينة لتأمين مراكزهم بين أفضل 125 لاعباً لضمان بطاقة الموسم المقبل.",
      ],
    },
  },
};



