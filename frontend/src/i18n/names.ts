import type { Locale } from './locales';

/** Short native name (headlines, tables). English key = seed `name`. */
const TEAMS: Record<string, Partial<Record<Locale, string>>> = {
  Algeria: { fr: 'Algérie', es: 'Argelia', de: 'Algerien', it: 'Algeria', pl: 'Algieria', zh: '阿尔及利亚', ja: 'アルジェリア', ko: '알제리', ar: 'الجزائر' },
  Argentina: { fr: 'Argentine', es: 'Argentina', de: 'Argentinien', it: 'Argentina', pl: 'Argentyna', zh: '阿根廷', ja: 'アルゼンチン', ko: '아르헨티나', ar: 'الأرجنتين' },
  Australia: { fr: 'Australie', es: 'Australia', de: 'Australien', it: 'Australia', pl: 'Australia', zh: '澳大利亚', ja: 'オーストラリア', ko: '호주', ar: 'أستراليا' },
  Austria: { fr: 'Autriche', es: 'Austria', de: 'Österreich', it: 'Austria', pl: 'Austria', zh: '奥地利', ja: 'オーストリア', ko: '오스트리아', ar: 'النمسا' },
  Belgium: { fr: 'Belgique', es: 'Bélgica', de: 'Belgien', it: 'Belgio', pl: 'Belgia', zh: '比利时', ja: 'ベルギー', ko: '벨기에', ar: 'بلجيكا' },
  'Bosnia and Herzegovina': { fr: 'Bosnie-Herzégovine', es: 'Bosnia y Herzegovina', de: 'Bosnien und Herzegowina', it: 'Bosnia ed Erzegovina', pl: 'Bośnia i Hercegowina', zh: '波黑', ja: 'ボスニア・ヘルツェゴビナ', ko: '보스니아 헤르체고비나', ar: 'البوسنة والهرسك' },
  Brazil: { fr: 'Brésil', es: 'Brasil', de: 'Brasilien', it: 'Brasile', pl: 'Brazylia', zh: '巴西', ja: 'ブラジル', ko: '브라질', ar: 'البرازيل' },
  Canada: { fr: 'Canada', es: 'Canadá', de: 'Kanada', it: 'Canada', pl: 'Kanada', zh: '加拿大', ja: 'カナダ', ko: '캐나다', ar: 'كندا' },
  'Cape Verde': { fr: 'Cap-Vert', es: 'Cabo Verde', de: 'Kap Verde', it: 'Capo Verde', pl: 'Republika Zielonego Przylądka', zh: '佛得角', ja: 'カーボベルデ', ko: '카보베르데', ar: 'الرأس الأخضر' },
  Colombia: { fr: 'Colombie', es: 'Colombia', de: 'Kolumbien', it: 'Colombia', pl: 'Kolumbia', zh: '哥伦比亚', ja: 'コロンビア', ko: '콜롬비아', ar: 'كولومبيا' },
  Croatia: { fr: 'Croatie', es: 'Croacia', de: 'Kroatien', it: 'Croazia', pl: 'Chorwacja', zh: '克罗地亚', ja: 'クロアチア', ko: '크로아티아', ar: 'كرواتيا' },
  Curaçao: { fr: 'Curaçao', es: 'Curazao', de: 'Curaçao', it: 'Curaçao', pl: 'Curaçao', zh: '库拉索', ja: 'キュラソー', ko: '퀴라소', ar: 'كوراساو' },
  Czechia: { fr: 'Tchéquie', es: 'Chequia', de: 'Tschechien', it: 'Cechia', pl: 'Czechy', zh: '捷克', ja: 'チェコ', ko: '체코', ar: 'التشيك' },
  'DR Congo': { fr: 'RD Congo', es: 'RD Congo', de: 'DR Kongo', it: 'RD del Congo', pl: 'DR Konga', zh: '刚果民主共和国', ja: 'コンゴ民主共和国', ko: '콩고민주공화국', ar: 'جمهورية الكونغو الديمقراطية' },
  Ecuador: { fr: 'Équateur', es: 'Ecuador', de: 'Ecuador', it: 'Ecuador', pl: 'Ekwador', zh: '厄瓜多尔', ja: 'エクアドル', ko: '에콰도르', ar: 'الإكوادور' },
  Egypt: { fr: 'Égypte', es: 'Egipto', de: 'Ägypten', it: 'Egitto', pl: 'Egipt', zh: '埃及', ja: 'エジプト', ko: '이집트', ar: 'مصر' },
  England: { fr: 'Angleterre', es: 'Inglaterra', de: 'England', it: 'Inghilterra', pl: 'Anglia', zh: '英格兰', ja: 'イングランド', ko: '잉글랜드', ar: 'إنجلترا' },
  France: { fr: 'France', es: 'Francia', de: 'Frankreich', it: 'Francia', pl: 'Francja', zh: '法国', ja: 'フランス', ko: '프랑스', ar: 'فرنسا' },
  Germany: { fr: 'Allemagne', es: 'Alemania', de: 'Deutschland', it: 'Germania', pl: 'Niemcy', zh: '德国', ja: 'ドイツ', ko: '독일', ar: 'ألمانيا' },
  Ghana: { fr: 'Ghana', es: 'Ghana', de: 'Ghana', it: 'Ghana', pl: 'Ghana', zh: '加纳', ja: 'ガーナ', ko: '가나', ar: 'غانا' },
  Haiti: { fr: 'Haïti', es: 'Haití', de: 'Haiti', it: 'Haiti', pl: 'Haiti', zh: '海地', ja: 'ハイチ', ko: '아이티', ar: 'هايتي' },
  Iran: { fr: 'Iran', es: 'Irán', de: 'Iran', it: 'Iran', pl: 'Iran', zh: '伊朗', ja: 'イラン', ko: '이란', ar: 'إيران' },
  Iraq: { fr: 'Irak', es: 'Irak', de: 'Irak', it: 'Iraq', pl: 'Irak', zh: '伊拉克', ja: 'イラク', ko: '이라크', ar: 'العراق' },
  'Ivory Coast': { fr: "Côte d'Ivoire", es: 'Costa de Marfil', de: 'Elfenbeinküste', it: "Costa d'Avorio", pl: 'Wybrzeże Kości Słoniowej', zh: '科特迪瓦', ja: 'コートジボワール', ko: '코트디부아르', ar: 'ساحل العاج' },
  Japan: { fr: 'Japon', es: 'Japón', de: 'Japan', it: 'Giappone', pl: 'Japonia', zh: '日本', ja: '日本', ko: '일본', ar: 'اليابان' },
  Jordan: { fr: 'Jordanie', es: 'Jordania', de: 'Jordanien', it: 'Giordania', pl: 'Jordania', zh: '约旦', ja: 'ヨルダン', ko: '요르단', ar: 'الأردن' },
  Mexico: { fr: 'Mexique', es: 'México', de: 'Mexiko', it: 'Messico', pl: 'Meksyk', zh: '墨西哥', ja: 'メキシコ', ko: '멕시코', ar: 'المكسيك' },
  Morocco: { fr: 'Maroc', es: 'Marruecos', de: 'Marokko', it: 'Marocco', pl: 'Maroko', zh: '摩洛哥', ja: 'モロッコ', ko: '모로코', ar: 'المغرب' },
  Netherlands: { fr: 'Pays-Bas', es: 'Países Bajos', de: 'Niederlande', it: 'Paesi Bassi', pl: 'Holandia', zh: '荷兰', ja: 'オランダ', ko: '네덜란드', ar: 'هولندا' },
  'New Zealand': { fr: 'Nouvelle-Zélande', es: 'Nueva Zelanda', de: 'Neuseeland', it: 'Nuova Zelanda', pl: 'Nowa Zelandia', zh: '新西兰', ja: 'ニュージーランド', ko: '뉴질랜드', ar: 'نيوزيلندا' },
  Norway: { fr: 'Norvège', es: 'Noruega', de: 'Norwegen', it: 'Norvegia', pl: 'Norwegia', zh: '挪威', ja: 'ノルウェー', ko: '노르웨이', ar: 'النرويج' },
  Panama: { fr: 'Panama', es: 'Panamá', de: 'Panama', it: 'Panama', pl: 'Panama', zh: '巴拿马', ja: 'パナマ', ko: '파나마', ar: 'بنما' },
  Paraguay: { fr: 'Paraguay', es: 'Paraguay', de: 'Paraguay', it: 'Paraguay', pl: 'Paragwaj', zh: '巴拉圭', ja: 'パラグアイ', ko: '파라과이', ar: 'باراغواي' },
  Portugal: { fr: 'Portugal', es: 'Portugal', de: 'Portugal', it: 'Portogallo', pl: 'Portugalia', zh: '葡萄牙', ja: 'ポルトガル', ko: '포르투갈', ar: 'البرتغال' },
  Qatar: { fr: 'Qatar', es: 'Catar', de: 'Katar', it: 'Qatar', pl: 'Katar', zh: '卡塔尔', ja: 'カタール', ko: '카타르', ar: 'قطر' },
  'Saudi Arabia': { fr: 'Arabie saoudite', es: 'Arabia Saudí', de: 'Saudi-Arabien', it: 'Arabia Saudita', pl: 'Arabia Saudyjska', zh: '沙特阿拉伯', ja: 'サウジアラビア', ko: '사우디아라비아', ar: 'السعودية' },
  Scotland: { fr: 'Écosse', es: 'Escocia', de: 'Schottland', it: 'Scozia', pl: 'Szkocja', zh: '苏格兰', ja: 'スコットランド', ko: '스코틀랜드', ar: 'اسكتلندا' },
  Senegal: { fr: 'Sénégal', es: 'Senegal', de: 'Senegal', it: 'Senegal', pl: 'Senegal', zh: '塞内加尔', ja: 'セネガル', ko: '세네갈', ar: 'السنغال' },
  'South Africa': { fr: 'Afrique du Sud', es: 'Sudáfrica', de: 'Südafrika', it: 'Sudafrica', pl: 'Południowa Afryka', zh: '南非', ja: '南アフリカ', ko: '남아프리카공화국', ar: 'جنوب أفريقيا' },
  'South Korea': { fr: 'Corée du Sud', es: 'Corea del Sur', de: 'Südkorea', it: 'Corea del Sud', pl: 'Korea Południowa', zh: '韩国', ja: '韓国', ko: '한국', ar: 'كوريا الجنوبية' },
  Spain: { fr: 'Espagne', es: 'España', de: 'Spanien', it: 'Spagna', pl: 'Hiszpania', zh: '西班牙', ja: 'スペイン', ko: '스페인', ar: 'إسبانيا' },
  Sweden: { fr: 'Suède', es: 'Suecia', de: 'Schweden', it: 'Svezia', pl: 'Szwecja', zh: '瑞典', ja: 'スウェーデン', ko: '스웨덴', ar: 'السويد' },
  Switzerland: { fr: 'Suisse', es: 'Suiza', de: 'Schweiz', it: 'Svizzera', pl: 'Szwajcaria', zh: '瑞士', ja: 'スイス', ko: '스위스', ar: 'سويسرا' },
  Tunisia: { fr: 'Tunisie', es: 'Túnez', de: 'Tunesien', it: 'Tunisia', pl: 'Tunezja', zh: '突尼斯', ja: 'チュニジア', ko: '튀니지', ar: 'تونس' },
  Türkiye: { fr: 'Turquie', es: 'Turquía', de: 'Türkei', it: 'Turchia', pl: 'Turcja', zh: '土耳其', ja: 'トルコ', ko: '튀르키예', ar: 'تركيا' },
  Turkey: { fr: 'Turquie', es: 'Turquía', de: 'Türkei', it: 'Turchia', pl: 'Turcja', zh: '土耳其', ja: 'トルコ', ko: '튀르키예', ar: 'تركيا' },
  'United States': { fr: 'États-Unis', es: 'Estados Unidos', de: 'USA', it: 'Stati Uniti', pl: 'Stany Zjednoczone', zh: '美国', ja: 'アメリカ', ko: '미국', ar: 'الولايات المتحدة' },
  Uruguay: { fr: 'Uruguay', es: 'Uruguay', de: 'Uruguay', it: 'Uruguay', pl: 'Urugwaj', zh: '乌拉圭', ja: 'ウルグアイ', ko: '우루과이', ar: 'الأوروغواي' },
  Uzbekistan: { fr: 'Ouzbékistan', es: 'Uzbekistán', de: 'Usbekistan', it: 'Uzbekistan', pl: 'Uzbekistan', zh: '乌兹别克斯坦', ja: 'ウズベキスタン', ko: '우즈베키스탄', ar: 'أوزبكستان' },
};

const PLACES: Record<string, Partial<Record<Locale, string>>> = {
  'New Jersey': { fr: 'New Jersey', es: 'Nueva Jersey', de: 'New Jersey', it: 'New Jersey', pl: 'New Jersey', zh: '新泽西', ja: 'ニュージャージー', ko: '뉴저지', ar: 'نيوجيرسي' },
  Miami: { zh: '迈阿密', ja: 'マイアミ', ko: '마이애미', ar: 'ميامي' },
  'Mexico City': { fr: 'Mexico', es: 'Ciudad de México', de: 'Mexiko-Stadt', it: 'Città del Messico', pl: 'Meksyk', zh: '墨西哥城', ja: 'メキシコシティ', ko: '멕시코시티', ar: 'مدينة مكسيكو' },
  'New York': { fr: 'New York', es: 'Nueva York', de: 'New York', it: 'New York', pl: 'Nowy Jork', zh: '纽约', ja: 'ニューヨーク', ko: '뉴욕', ar: 'نيويورك' },
  London: { fr: 'Londres', es: 'Londres', de: 'London', it: 'Londra', pl: 'Londyn', zh: '伦敦', ja: 'ロンドン', ko: '런던', ar: 'لندن' },
  Madrid: { fr: 'Madrid', es: 'Madrid', de: 'Madrid', it: 'Madrid', pl: 'Madryt', zh: '马德里', ja: 'マドリード', ko: '마드리드', ar: 'مدريد' },
  Melbourne: { fr: 'Melbourne', es: 'Melbourne', de: 'Melbourne', it: 'Melbourne', pl: 'Melbourne', zh: '墨尔本', ja: 'メルボルン', ko: '멜버른', ar: 'ملبورن' },
  Toronto: { zh: '多伦多', ja: 'トロント', ko: '토론토', ar: 'تورونتو' },
  Dallas: { zh: '达拉斯', ja: 'ダラス', ko: '댈러스', ar: 'دالاس' },
  Houston: { zh: '休斯敦', ja: 'ヒューストン', ko: '휴스턴', ar: 'هيوستن' },
  Atlanta: { zh: '亚特兰大', ja: 'アトランタ', ko: '애틀랜타', ar: 'أتلانتا' },
  Boston: { zh: '波士顿', ja: 'ボストン', ko: '보스턴', ar: 'بوسطن' },
  Seattle: { zh: '西雅图', ja: 'シアトル', ko: '시애틀', ar: 'سياتل' },
  'Kansas City': { zh: '堪萨斯城', ja: 'カンザスシティ', ko: '캔자스시티', ar: 'كانساس سيتي' },
  Buffalo: { zh: '布法罗', ja: 'バッファロー', ko: '버펄로', ar: 'بوفالو' },
  Wentworth: { zh: '温特沃斯', ja: 'ウェントワース', ko: '웬트워스', ar: 'وينتوورث' },
  Medinah: { zh: '麦迪纳', ja: 'メディナ', ko: '메디나', ar: 'مدينا' },
  'East Lake': { zh: '东湖', ja: 'イーストレイク', ko: '이스트레이크', ar: 'إيست ليك' },
  'Royal Birkdale': { zh: '皇家伯克戴尔', ja: 'ロイヤル・バークデール', ko: '로열 버크데일', ar: 'رويال بيركديل' },
  Baku: { fr: 'Bakou', es: 'Bakú', de: 'Baku', it: 'Baku', pl: 'Baku', zh: '巴库', ja: 'バクー', ko: '바쿠', ar: 'باكو' },
  Monza: { zh: '蒙扎', ja: 'モンツァ', ko: '몬차', ar: 'مونزا' },
  'Silverstone': { zh: '银石', ja: 'シルバーストーン', ko: '실버스톤', ar: 'سيلفرستون' },
  'Spa-Francorchamps': { zh: '斯帕', ja: 'スパ', ko: '스파', ar: 'سبا' },
  Zandvoort: { zh: '赞德福特', ja: 'ザントフールト', ko: '잔트보르트', ar: 'زاندفورت' },
  Flushing: { zh: '法拉盛', ja: 'フラッシング', ko: '플러싱', ar: 'فلشينغ' },
  Wimbledon: { fr: 'Wimbledon', es: 'Wimbledon', de: 'Wimbledon', it: 'Wimbledon', pl: 'Wimbledon', zh: '温布尔登', ja: 'ウィンブルドン', ko: '윔블던', ar: 'ويمبلدون' },
};

const COMPETITIONS: Record<string, Partial<Record<Locale, string>>> = {
  'world-cup-2026': {
    fr: 'Coupe du monde 2026',
    es: 'Mundial 2026',
    de: 'WM 2026',
    it: 'Mondiali 2026',
    pl: 'Mistrzostwa Świata 2026',
    zh: '2026世界杯',
    ja: '2026ワールドカップ',
    ko: '2026 월드컵',
    ar: 'كأس العالم 2026',
  },
  'premier-league': {
    fr: 'Premier League',
    es: 'Premier League',
    de: 'Premier League',
    it: 'Premier League',
    pl: 'Premier League',
    zh: '英超',
    ja: 'プレミアリーグ',
    ko: '프리미어리그',
    ar: 'الدوري الإنجليزي',
  },
};

export function entityName(name: string | null | undefined, locale: Locale): string {
  if (!name) return '';
  if (locale === 'en') return name;
  const hit = TEAMS[name] || PLACES[name] || COMPETITIONS[name];
  return hit?.[locale] || name;
}

export function competitionName(competition: string | null | undefined, locale: Locale): string {
  if (!competition) return '';
  if (locale === 'en') {
    if (competition === 'world-cup-2026') return 'World Cup 2026';
    if (competition.startsWith('premier-league')) return 'Premier League';
    return competition;
  }
  const key = competition.startsWith('premier-league') ? 'premier-league' : competition;
  return COMPETITIONS[key]?.[locale] || entityName(competition, locale);
}
