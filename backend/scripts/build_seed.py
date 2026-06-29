"""
Builds the canonical MatchTales dataset -> /app/frontend/src/data/seed.json
Real 2026 FIFA World Cup-style field: 48 teams, 12 groups (A-L), week-1 results +
upcoming marquee fixtures, rivalries, iconic moments, player legacies.
Run: python3 scripts/build_seed.py
"""
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT.parent / "frontend" / "src" / "data" / "seed.json"


# ---- Team config object (groups the 13 related team attributes) ----
@dataclass
class Team:
    name: str
    code: str
    flag: str
    group: str
    conf: str
    rank: int
    nick: str
    titles: int
    best: str
    color: str  # primary brand hex used for accents on team pages
    players: List[List[str]]
    fact: str
    story: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name, "code": self.code, "flag": self.flag,
            "group": self.group, "conf": self.conf, "rank": self.rank,
            "nick": self.nick, "titles": self.titles, "best": self.best,
            "color": self.color, "slug": self.name.lower().replace(" ", "-"),
            "keyPlayers": self.players, "funFact": self.fact, "story": self.story,
        }


T: List[Dict[str, Any]] = []


def team(*args: Any) -> None:
    """Thin builder: construct a Team config object and append its dict form."""
    T.append(Team(*args).to_dict())


# Group A
team("Mexico","MEX","🇲🇽","A","CONCACAF",15,"El Tri",0,"Quarter-finals (1970, 1986)","#006847",
     [["Santiago Giménez","Striker"],["Edson Álvarez","Midfield"],["Luis Malagón","Goalkeeper"]],
     "Mexico have reached the World Cup knockout stage a record-tying number of times but rarely broken the quarter-final ceiling.",
     "Co-hosts and the heartbeat of Group A — a nation that lives and breathes the tournament it helped invent the modern atmosphere for.")
team("South Korea","KOR","🇰🇷","A","AFC",25,"Taegeuk Warriors",0,"Fourth place (2002)","#CD2E3A",
     [["Son Heung-min","Forward"],["Lee Kang-in","Midfield"],["Kim Min-jae","Defender"]],
     "Son Heung-min is chasing the one trophy that has eluded a glittering Premier League career.",
     "Forever romantics after 2002, Korea travel with Son's farewell-tour energy and a fearless press.")
team("South Africa","RSA","🇿🇦","A","CAF",60,"Bafana Bafana",0,"Group stage (host 2010)","#007A4D",
     [["Lyle Foster","Striker"],["Percy Tau","Forward"],["Ronwen Williams","Goalkeeper"]],
     "Bafana Bafana remain the only host nation to be eliminated in the group stage (2010) — they want to rewrite that story.",
     "An underdog with golden-generation flashes, dreaming of a first knockout appearance.")
team("Czechia","CZE","🇨🇿","A","UEFA",40,"Národní tým",0,"Runners-up as Czechoslovakia (1934, 1962)","#11457E",
     [["Patrik Schick","Striker"],["Tomáš Souček","Midfield"],["Adam Hložek","Forward"]],
     "Patrik Schick once scored from inside his own half at the Euros — Czechia always carry a moment of magic.",
     "Heirs to a proud Central European footballing tradition, hunting their first deep run as Czechia.")

# Group B
team("Canada","CAN","🇨🇦","B","CONCACAF",27,"Les Rouges",0,"Group stage (1986, 2022)","#FF0000",
     [["Alphonso Davies","Wing-back"],["Jonathan David","Striker"],["Stephen Eustáquio","Midfield"]],
     "Canada are co-hosting their first home World Cup and chasing a first-ever World Cup goal celebration on home soil with fans behind them.",
     "Co-hosts with a rocket in Alphonso Davies and a point to prove after a winless 2022.")
team("Switzerland","SUI","🇨🇭","B","UEFA",19,"Nati",0,"Quarter-finals (1934, 1938, 1954)","#FF0000",
     [["Granit Xhaka","Midfield"],["Dan Ndoye","Winger"],["Breel Embolo","Striker"]],
     "Switzerland have qualified for every major tournament for over a decade — masters of the unglamorous knockout grind.",
     "Quietly excellent and forever underestimated, the side that loves a giant-killing.")
team("Qatar","QAT","🇶🇦","B","AFC",56,"Al Annabi",0,"Group stage (host 2022)","#8A1538",
     [["Akram Afif","Forward"],["Almoez Ali","Striker"],["Hassan Al-Haydos","Midfield"]],
     "Qatar are the reigning Asian champions, hungry to prove their 2022 host campaign wasn't the full story.",
     "Asian kings out to silence the doubters away from home.")
team("Bosnia and Herzegovina","BIH","🇧🇦","B","UEFA",64,"Zmajevi",0,"Group stage (2014)","#002F6C",
     [["Edin Džeko","Striker"],["Sead Kolašinac","Defender"],["Ermedin Demirović","Forward"]],
     "Bosnia's golden generation in 2014 was led by Edin Džeko — their legend returned to guide their return.",
     "The dragons return to the world stage, armed with defensive grit and a legendary forward in Džeko.")

# Group C
team("Brazil","BRA","🇧🇷","C","CONMEBOL",5,"Seleção",5,"Champions (x5)","#FFDF00",
     [["Vinícius Júnior","Winger"],["Rodrygo","Forward"],["Endrick","Striker"]],
     "Brazil are the only nation to play in every World Cup ever held — and the only five-time champions.",
     "The most successful nation in history, chasing a sixth star to end a 24-year wait.")
team("Morocco","MAR","🇲🇦","C","CAF",11,"Atlas Lions",0,"Fourth place (2022)","#C1272D",
     [["Achraf Hakimi","Wing-back"],["Brahim Díaz","Playmaker"],["Bilal El Khannouss","Midfield"]],
     "Morocco became the first African and Arab nation to reach a World Cup semi-final in 2022 — and they are no longer a surprise.",
     "The continent's standard-bearers, carrying a billion dreams and a defence that strangles giants.")
team("Haiti","HAI","🇭🇹","C","CONCACAF",83,"Les Grenadiers",0,"Group stage (1974)","#00209F",
     [["Frantzdy Pierrot","Striker"],["Duckens Nazon","Forward"],["Danley Jean Jacques","Midfield"]],
     "Haiti's only previous appearance was in West Germany 1974, where they scored a famous goal against Dino Zoff's Italy.",
     "Returning after 52 years, Haiti represents the Caribbean's pride and ultimate underdog spirit.")
team("Scotland","SCO","🏴󠁧󠁢󠁳󠁣󠁴󠁿","C","UEFA",42,"Tartan Army",0,"Group stage (multiple)","#002B49",
     [["Andrew Robertson","Defender"],["John McGinn","Midfield"],["Scott McTominay","Midfield"]],
     "Scotland have qualified for their first World Cup since France 1998, ending a 28-year wait.",
     "The Tartan Army marches to North America, bringing immense passion, noise, and key Premier League stars.")

# Group D
team("United States","USA","🇺🇸","D","CONCACAF",14,"USMNT",0,"Third place (1930)","#0A3161",
     [["Christian Pulisic","Winger"],["Weston McKennie","Midfield"],["Gio Reyna","Playmaker"]],
     "The USMNT headline their own home World Cup for the first time since 1994 — and the pressure is enormous.",
     "Hosts with a golden generation that finally has to deliver in front of a home crowd.")
team("Paraguay","PAR","🇵🇾","D","CONMEBOL",41,"La Albirroja",0,"Quarter-finals (2010)","#D52B1E",
     [["Julio Enciso","Playmaker"],["Miguel Almirón","Winger"],["Antonio Sanabria","Striker"]],
     "Paraguay's gritty 2010 side reached the quarter-finals without winning a single knockout game in 90 minutes.",
     "Stubborn, streetwise South Americans who make every match a battle.")
team("Australia","AUS","🇦🇺","D","AFC",27,"Socceroos",0,"Round of 16 (2006, 2022)","#FFCD00",
     [["Cristian Volpato","Playmaker"],["Riley McGree","Midfield"],["Mat Ryan","Goalkeeper"]],
     "The Socceroos' 2022 run was powered by a viral, beer-soaked celebration video back home in Federation Square.",
     "Relentless, organised and impossible to dislike — the ultimate tournament grinders.")
team("Turkiye","TUR","🇹🇷","D","UEFA",22,"Ay-Yıldızlılar",0,"Third place (2002)","#E30A17",
     [["Arda Güler","Playmaker"],["Kenan Yıldız","Winger"],["Hakan Çalhanoğlu","Midfield"]],
     "Turkiye's 2002 third-place run included the fastest goal in World Cup history — 10.8 seconds.",
     "A thrilling new generation led by two of Europe's brightest teenagers.")

# Group E
team("Germany","GER","🇩🇪","E","UEFA",9,"Die Mannschaft",4,"Champions (x4)","#000000",
     [["Jamal Musiala","Playmaker"],["Florian Wirtz","Playmaker"],["Kai Havertz","Striker"]],
     "Germany crashed out in the group stage in BOTH 2018 and 2022 — a four-time champion in crisis seeks redemption.",
     "A fallen giant rebuilt around two of the most exciting playmakers on the planet.")
team("Curaçao","CUW","🇨🇼","E","CONCACAF",82,"La Familia",0,"First-ever World Cup","#002B7F",
     [["Juninho Bacuna","Midfield"],["Leandro Bacuna","Midfield"],["Eloy Room","Goalkeeper"]],
     "Curaçao has qualified for the World Cup for the first time in their history under a golden Caribbean generation.",
     "Debutants bringing Caribbean energy, passion, and tactical flair to Group E.")
team("Ivory Coast","CIV","🇨🇮","E","CAF",33,"Les Éléphants",0,"Group stage (golden generation)","#FF8200",
     [["Simon Adingra","Winger"],["Franck Kessié","Midfield"],["Sébastien Haller","Striker"]],
     "Sébastien Haller scored the winner in the 2023 Africa Cup of Nations final months after beating cancer.",
     "African champions riding a wave of one of football's great comeback stories.")
team("Ecuador","ECU","🇪🇨","E","CONMEBOL",23,"La Tri",0,"Round of 16 (2006)","#FFD100",
     [["Moisés Caicedo","Midfield"],["Kendry Páez","Playmaker"],["Pervis Estupiñán","Wing-back"]],
     "Teen prodigy Kendry Páez became one of the youngest scorers in South American qualifying history.",
     "Altitude-bred and youthful, with a midfield that giants envy.")

# Group F
team("Netherlands","NED","🇳🇱","F","UEFA",8,"Oranje",0,"Runners-up (1974, 1978, 2010)","#FF6200",
     [["Cody Gakpo","Winger"],["Xavi Simons","Playmaker"],["Virgil van Dijk","Defender"]],
     "The Netherlands are the greatest team to never win the World Cup — three finals, three defeats.",
     "Total Football's heirs, forever chasing the trophy that history owes them.")
team("Japan","JPN","🇯🇵","F","AFC",18,"Samurai Blue",0,"Round of 16 (multiple)","#BC002D",
     [["Takefusa Kubo","Winger"],["Kaoru Mitoma","Winger"],["Wataru Endō","Midfield"]],
     "Japan beat both Germany AND Spain in the 2022 group stage — then exited on penalties, breaking hearts.",
     "Technical, brave and forever knocking on the quarter-final door.")
team("Tunisia","TUN","🇹🇳","F","CAF",45,"Eagles of Carthage",0,"Group stage (multiple)","#E20E17",
     [["Elyes Skhiri","Midfield"],["Youssef Msakni","Forward"],["Aissa Laïdouni","Midfield"]],
     "Tunisia shocked reigning champions France 1-0 in Qatar 2022, proving their giant-killing ability.",
     "Tactically disciplined and streetwise, the Eagles of Carthage are a tough hurdle for anyone.")
team("Sweden","SWE","🇸🇪","F","UEFA",38,"Blågult",0,"Runners-up (1958)","#006AA7",
     [["Alexander Isak","Striker"],["Dejan Kulusevski","Winger"],["Viktor Gyökeres","Striker"]],
     "Sweden reached the quarter-finals in 2018 and boast a frighteningly potent attack for 2026.",
     "Scandinavian powerhouses carrying a golden generation of dynamic, clinical attackers.")

# Group G
team("Belgium","BEL","🇧🇪","G","UEFA",8,"Red Devils",0,"Third place (2018)","#E30613",
     [["Kevin De Bruyne","Midfield"],["Jérémy Doku","Winger"],["Romelu Lukaku","Striker"]],
     "Belgium's 'golden generation' won bronze in 2018 but never the gold — this is the last dance for several greats.",
     "A team racing against time, blending fading legends with electric new pace.")
team("Egypt","EGY","🇪🇬","G","CAF",29,"The Pharaohs",0,"Group stage (1934, 1990, 2018)","#C8102E",
     [["Mohamed Salah","Forward"],["Omar Marmoush","Striker"],["Mohamed Elneny","Midfield"]],
     "Mohamed Salah carried Egypt to the 2018 World Cup but injury robbed him of his moment — he's back for redemption.",
     "A pharaoh's last quest: Salah dragging Egypt toward a first knockout stage in the modern era.")
team("Iran","IRN","🇮🇷","G","AFC",20,"Team Melli",0,"Group stage (multiple)","#239F40",
     [["Mehdi Taremi","Striker"],["Sardar Azmoun","Forward"],["Alireza Jahanbakhsh","Winger"]],
     "Iran's 1998 win over the USA in Lyon remains one of football's most politically charged matches ever played.",
     "Asia's perennial heavyweight, still chasing a first-ever knockout berth.")
team("New Zealand","NZL","🇳🇿","G","OFC",85,"All Whites",0,"Unbeaten group stage (2010)","#000000",
     [["Chris Wood","Striker"],["Marko Stamenić","Midfield"],["Liberato Cacace","Wing-back"]],
     "New Zealand are the only team to leave the 2010 World Cup unbeaten — three draws, then knocked out.",
     "The ultimate Cinderella, dreaming of a first-ever World Cup win.")

# Group H
team("Spain","ESP","🇪🇸","H","UEFA",1,"La Roja",1,"Champions (2010)","#C60B1E",
     [["Lamine Yamal","Winger"],["Pedri","Midfield"],["Nico Williams","Winger"]],
     "Teenager Lamine Yamal is already being compared to the greatest wingers in history — this is his coming-out tournament.",
     "Tiki-taka reborn with a fearless teenage generation lighting up the wings.")
team("Cape Verde","CPV","🇨🇻","H","CAF",67,"Blue Sharks",0,"First-ever World Cup","#003893",
     [["Ryan Mendes","Winger"],["Logan Costa","Defender"],["Jovane Cabral","Winger"]],
     "The Blue Sharks reached the quarter-finals of the 2023 Africa Cup of Nations, winning hearts globally.",
     "The ultimate giant-killers of the Atlantic, ready to unleash their speed and spirit in Group H.")
team("Saudi Arabia","KSA","🇸🇦","H","AFC",61,"Green Falcons",0,"Round of 16 (1994)","#006C35",
     [["Salem Al-Dawsari","Winger"],["Firas Al-Buraikan","Striker"],["Nawaf Al-Aqidi","Goalkeeper"]],
     "Saudi Arabia stunned eventual champions Argentina 2-1 in 2022 — one of the greatest upsets in World Cup history.",
     "Giant-killers who proved that on the right day, no superpower is safe.")
team("Uruguay","URU","🇺🇾","H","CONMEBOL",16,"La Celeste",2,"Champions (1930, 1950)","#7BAFD4",
     [["Federico Valverde","Midfield"],["Darwin Núñez","Striker"],["Manuel Ugarte","Midfield"]],
     "Uruguay, a nation of 3.4 million, has won as many World Cups as England, France and Spain combined — two stars on the shirt.",
     "History's original champions, still snarling, still punching far above their weight.")

# Group I
team("France","FRA","🇫🇷","I","UEFA",3,"Les Bleus",2,"Champions (1998, 2018)","#0055A4",
     [["Kylian Mbappé","Forward"],["Aurélien Tchouaméni","Midfield"],["Désiré Doué","Winger"]],
     "Kylian Mbappé already has a World Cup final hat-trick (2022) — and he's still in his twenties.",
     "The most feared attack on earth, captained by a generational superstar in his prime.")
team("Senegal","SEN","🇸🇳","I","CAF",15,"Lions of Teranga",0,"Quarter-finals (2002)","#00853F",
     [["Nicolas Jackson","Striker"],["Pape Matar Sarr","Midfield"],["Édouard Mendy","Goalkeeper"]],
     "Senegal's 2002 debut began with a shock win over reigning champions France — they love a grand entrance.",
     "African powerhouses with speed, steel, and the confidence of a team that fears no one.")
team("Norway","NOR","🇳🇴","I","UEFA",31,"Løvene",0,"Round of 16 (1998)","#BA0C2F",
     [["Erling Haaland","Striker"],["Martin Ødegaard","Midfield"],["Antonio Nusa","Winger"]],
     "Norway return to the World Cup after a 28-year absence — and they're bringing Erling Haaland with them.",
     "A goal machine and a captain-artist finally on the biggest stage together.")
team("Iraq","IRQ","🇮🇶","I","AFC",57,"Lions of Mesopotamia",0,"First World Cup since 1986","#007A3D",
     [["Aymen Hussein","Striker"],["Zidane Iqbal","Midfield"],["Jalal Hassan","Goalkeeper"]],
     "Iraq won the 2007 Asian Cup amid extraordinary adversity — one of sport's most moving triumphs.",
     "A nation for whom simply being here is a victory, and they want much more.")

# Group J
team("Argentina","ARG","🇦🇷","J","CONMEBOL",2,"La Albiceleste",3,"Champions (1978, 1986, 2022)","#75AADB",
     [["Lautaro Martínez","Striker"],["Julián Álvarez","Forward"],["Enzo Fernández","Midfield"]],
     "Reigning champions Argentina arrive in a post-Messi-prime world, defending the crown won in the Qatar epic.",
     "World champions chasing back-to-back glory — the team everyone wants to beat.")
team("Algeria","ALG","🇩🇿","J","CAF",28,"Les Fennecs",0,"Round of 16 (2014)","#006233",
     [["Riyad Mahrez","Winger"],["Ismaël Bennacer","Midfield"],["Mohamed Amoura","Striker"]],
     "Algeria pushed eventual champions Germany to extra time in a thrilling 2014 last-16 classic.",
     "Technical, proud and capable of toppling anyone on their day.")
team("Austria","AUT","🇦🇹","J","UEFA",24,"Das Nationalteam",0,"Third place (1954)","#E30613",
     [["Marcel Sabitzer","Midfield"],["Konrad Laimer","Midfield"],["Christoph Baumgartner","Midfield"]],
     "Austria's high-pressing system has made them one of Europe's most feared tactical sides.",
     "Das Nationalteam travels with cohesion, fire, and a modern press to shake up Group J.")
team("Jordan","JOR","🇯🇴","J","AFC",63,"Al-Nashama",0,"First-ever World Cup","#E2001A",
     [["Musa Al-Taamari","Winger"],["Yazan Al-Naimat","Forward"],["Nizar Al-Rashdan","Midfield"]],
     "Jordan has qualified for their first-ever FIFA World Cup after a historic runners-up finish in the 2023 Asian Cup.",
     "The Chivalrous make their World Cup debut, ready to unleash their lethal counter-attacks on the world.")

# Group K
team("Portugal","POR","🇵🇹","K","UEFA",6,"A Seleção",0,"Third place (1966)","#006600",
     [["Cristiano Ronaldo","Forward"],["Bruno Fernandes","Midfield"],["Rafael Leão","Winger"]],
     "Cristiano Ronaldo is the only player to score in five different World Cups — this is the final chapter.",
     "A legend's last World Cup, surrounded by a frighteningly talented supporting cast.")
team("Uzbekistan","UZB","🇺🇿","K","AFC",50,"White Wolves",0,"First-ever World Cup","#1EB53A",
     [["Eldor Shomurodov","Striker"],["Abbosbek Fayzullaev","Playmaker"],["Khojimat Erkinov","Midfield"]],
     "Uzbekistan have qualified for the World Cup for the very first time in their history.",
     "Debutants writing the opening page of a brand-new footballing story.")
team("Colombia","COL","🇨🇴","K","CONMEBOL",13,"Los Cafeteros",0,"Quarter-finals (2014)","#FCD116",
     [["James Rodríguez","Playmaker"],["Luis Díaz","Winger"],["Jhon Durán","Striker"]],
     "James Rodríguez won the 2014 Golden Boot and scored a goal so good it earned a FIFA Puskás Award.",
     "Carnival football with a maestro orchestrating one last great campaign.")
team("DR Congo","COD","🇨🇩","K","CAF",46,"Leopards",0,"Group stage as Zaire (1974)","#007FFF",
     [["Yoane Wissa","Striker"],["Silas Katompa","Winger"],["Chancel Mbemba","Defender"]],
     "As Zaire in 1974, they were the first Black African nation to reach a World Cup — now they return transformed.",
     "A historic name reborn, hungry to honour a pioneering legacy.")

# Group L
team("England","ENG","🏴󠁧󠁢󠁥󠁮󠁧󠁿","L","UEFA",4,"Three Lions",1,"Champions (1966)","#CE1124",
     [["Jude Bellingham","Midfield"],["Harry Kane","Striker"],["Bukayo Saka","Winger"]],
     "England's quest to bring football home takes them to North America, aiming to build on deep tournament runs.",
     "A golden generation desperate to finally go all the way and win their first trophy since 1966.")
team("Croatia","CRO","🇭🇷","L","UEFA",10,"Vatreni",0,"Runners-up (2018), Third (2022)","#FF0000",
     [["Luka Modrić","Midfield"],["Joško Gvardiol","Defender"],["Mateo Kovačić","Midfield"]],
     "Luka Modrić, the 2018 Ballon d'Or winner, is chasing one final tournament miracle at 40 years old.",
     "The ultimate big-game team — small nation, enormous heart, and a maestro's last waltz.")
team("Ghana","GHA","🇬🇭","L","CAF",73,"Black Stars",0,"Quarter-finals (2010)","#006B3F",
     [["Mohammed Kudus","Forward"],["Thomas Partey","Midfield"],["Antoine Semenyo","Winger"]],
     "Ghana were a Luis Suárez handball away from becoming the first African semi-finalists in 2010 — the wound still aches.",
     "A proud giant chasing the redemption that 2010 cruelly denied them.")
team("Panama","PAN","🇵🇦","L","CONCACAF",34,"La Marea Roja",0,"Group stage (2018)","#DA121A",
     [["Adalberto Carrasquilla","Midfield"],["José Fajardo","Striker"],["Orlando Mosquera","Goalkeeper"]],
     "Panama's first-ever World Cup goal in 2018 was treated as a national holiday back home.",
     "Tiny nation, massive belief — the romantics of Group L.")

# ---- Rivalries
RIV = [
  {"slug":"england-croatia","title":"England vs Croatia — The 2018 Ghost","teams":["England","Croatia"],
   "blurb":"Moscow, 2018. England led a World Cup semi-final and dared to dream — then Croatia broke their hearts in extra time. Eight years on, they meet again.",
   "points":["2018 semi-final: Croatia won 2-1 after extra time","Modrić's last tournament vs Bellingham's first as a star","Group F's defining fixture"],
   "img":"https://images.unsplash.com/photo-1556152352-8edad147cc21?crop=entropy&cs=srgb&fm=jpg&q=85","heat":9.4},
  {"slug":"usa-iran","title":"USA vs Iran — More Than A Game","teams":["Brazil","Haiti"],
   "blurb":"From the politically-charged 1998 clash in Lyon to the tense 2022 decider, no fixture carries more weight off the pitch than this one.",
   "points":["1998: Iran won 2-1 in an emotional Lyon night","2022: USA won 1-0 to advance","A rivalry that transcends sport"],
   "img":"https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?crop=entropy&cs=srgb&fm=jpg&q=85","heat":8.7},
  {"slug":"uruguay-ghana","title":"Uruguay vs Ghana — The Suárez Wound","teams":["Egypt","Ghana"],
   "blurb":"2010: Luis Suárez's handball on the line denied Ghana a place in history. 2022: Ghana's revenge mission backfired. The trilogy continues.",
   "points":["2010 QF: Suárez handball, Gyan misses the penalty","2022: Uruguay won 2-0 but both went home","Africa's greatest near-miss"],
   "img":"https://images.unsplash.com/photo-1574629810360-7efbbe195018?crop=entropy&cs=srgb&fm=jpg&q=85","heat":8.9},
  {"slug":"germany-algeria","title":"Germany vs Algeria — Old Scores","teams":["Argentina","Austria"],
   "blurb":"From the 1982 'Disgrace of Gijón' to the 2014 extra-time epic, these two share one of the World Cup's most loaded histories.",
   "points":["1982: Algeria beat West Germany, then the Gijón scandal","2014: Germany edged a classic 2-1 in extra time","Redemption on both sides"],
   "img":"https://images.unsplash.com/photo-1508098682722-e99c43a406b2?crop=entropy&cs=srgb&fm=jpg&q=85","heat":7.8},
]

# ---- Iconic moments
MOMENTS = [
  {"year":1986,"title":"Maradona's Hand of God & Goal of the Century","team":"United States","text":"Within four minutes, Diego Maradona produced football's most infamous goal and its most beautiful — both against England."},
  {"year":1950,"title":"The Maracanazo","team":"Egypt","text":"Uruguay silenced 200,000 Brazilians at the Maracanã to win the World Cup in the greatest upset the sport has seen."},
  {"year":2022,"title":"Argentina 3-3 France — The Greatest Final","team":"United States","text":"Messi vs Mbappé, a final-hat-trick, and penalties. Many call it the finest World Cup final ever played."},
  {"year":2014,"title":"Germany 7-1 Brazil","team":"Argentina","text":"On home soil, Brazil suffered the most shocking semi-final collapse in tournament history."},
  {"year":2002,"title":"Senegal Shock France","team":"Scotland","text":"World Cup debutants Senegal beat the reigning champions in the opening match — a statement heard across a continent."},
  {"year":2018,"title":"Croatia's Run to the Final","team":"Croatia","text":"A nation of four million played three straight knockout games to extra time and reached the final — pure defiance."},
]

# ---- Stories (long-form hub) metadata; body authored as MDX by generator
STORIES_META = [
  {"slug":"greatest-world-cup-upsets","title":"The Greatest World Cup Upsets of All Time","category":"History",
   "excerpt":"From Saudi Arabia toppling Argentina to North Korea's 1966 miracle — when football's giants fell.","img":"https://images.unsplash.com/photo-1574629810360-7efbbe195018?crop=entropy&cs=srgb&fm=jpg&q=85","read":7},
  {"slug":"the-last-dance-modric-ronaldo-messi","title":"The Last Dance: A Generation Says Goodbye","category":"Legacy",
   "excerpt":"Modrić, Ronaldo and the legends playing their final World Cup. Savour them while you can.","img":"https://images.unsplash.com/photo-1627774250096-25d8c0ece8ba?crop=entropy&cs=srgb&fm=jpg&q=85","read":6},
  {"slug":"why-the-48-team-world-cup-changes-everything","title":"Why the 48-Team World Cup Changes Everything","category":"Explainer",
   "excerpt":"More teams, more groups, more drama — and a brand-new path to the trophy. Here's what to know.","img":"https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?crop=entropy&cs=srgb&fm=jpg&q=85","read":5},
  {"slug":"hosts-united-usa-mexico-canada","title":"Three Nations, One Party: The Hosts' Story","category":"Hosts",
   "excerpt":"For the first time, three countries host the World Cup together. The stakes for USA, Mexico and Canada could not be higher.","img":"https://images.unsplash.com/photo-1459865264687-595d652de67e?crop=entropy&cs=srgb&fm=jpg&q=85","read":6},
  {"slug":"lamine-yamal-new-tiki-taka","title":"The Rise of Lamine Yamal and Spain's New Age","category":"Tactics",
   "excerpt":"How a teenage sensation and a direct style are reinventing La Roja's historical identity on the world stage.","img":"https://images.unsplash.com/photo-1517649763962-0c623066013b?crop=entropy&cs=srgb&fm=jpg&q=85","read":5},
  {"slug":"norways-golden-duo-haaland-odegaard","title":"Norway's Golden Duo: Haaland and Ødegaard's World Cup Dream","category":"Spotlight",
   "excerpt":"After 28 years in the wilderness, Norway return to the biggest stage powered by two of the world's finest talents.","img":"https://images.unsplash.com/photo-1551958219-acbc608c6377?crop=entropy&cs=srgb&fm=jpg&q=85","read":6},
  {"slug":"african-heavyweights-senegal-morocco","title":"African Heavyweights: The Battle for Continental Supremacy","category":"Continent",
   "excerpt":"Morocco's historic semi-final run in 2022 vs Senegal's reigning champions — who will carry Africa furthest in 2026?","img":"https://images.unsplash.com/photo-1560272564-c83b66b1ad12?crop=entropy&cs=srgb&fm=jpg&q=85","read":7},
]


# ---- Fixtures
# status: FINISHED / LIVE / UPCOMING. Matchday 1 finished, MD2 marquee upcoming/live.
@dataclass
class Fixture:
    home: str
    away: str
    group: str
    md: int
    date: str
    time: str
    venue: str
    city: str
    status: str
    hs: Optional[Any] = None
    as_: Optional[Any] = None
    marquee: bool = False
    live_minute: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        slug = f"{self.home.lower().replace(' ', '-')}-vs-{self.away.lower().replace(' ', '-')}-md{self.md}"
        return {
            "slug": slug, "home": self.home, "away": self.away, "group": self.group,
            "matchday": self.md, "date": self.date, "time": self.time,
            "venue": self.venue, "city": self.city, "status": self.status,
            "homeScore": self.hs, "awayScore": self.as_,
            "marquee": self.marquee, "liveMinute": self.live_minute,
        }


def fx(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    """Thin builder: construct a Fixture config object and return its dict form."""
    return Fixture(*args, **kwargs).to_dict()


F = []
# Matchday 1 (finished) — one signature result per group + extras
F.append(fx("Mexico","South Africa","A",1,"2026-06-11","19:00","Estadio Azteca","Mexico City","FINISHED",2,0,True))
F.append(fx("South Korea","Czechia","A",1,"2026-06-12","16:00","Estadio Akron","Guadalajara","FINISHED",2,1))
F.append(fx("Switzerland","Bosnia and Herzegovina","B",1,"2026-06-12","13:00","BC Place","Vancouver","FINISHED",1,1))
F.append(fx("Canada","Qatar","B",1,"2026-06-12","19:00","BMO Field","Toronto","FINISHED",0,2))
F.append(fx("Brazil","Morocco","C",1,"2026-06-11","20:00","SoFi Stadium","Los Angeles","FINISHED",2,1,True))
F.append(fx("Haiti","Scotland","C",1,"2026-06-13","16:00","Lumen Field","Seattle","FINISHED",0,1))
F.append(fx("United States","Paraguay","D",1,"2026-06-13","21:00","Mercedes-Benz Stadium","Atlanta","FINISHED",3,0,True))
F.append(fx("Australia","Turkiye","D",1,"2026-06-14","16:00","Gillette Stadium","Boston","FINISHED",1,2))
F.append(fx("Germany","Ivory Coast","E",1,"2026-06-14","19:00","Hard Rock Stadium","Miami","FINISHED",4,0))
F.append(fx("Curaçao","Ecuador","E",1,"2026-06-14","13:00","Levi's Stadium","San Francisco","FINISHED",1,1,True))
F.append(fx("England","Ghana","L",1,"2026-06-13","13:00","MetLife Stadium","New Jersey","FINISHED",2,1,True))
F.append(fx("Croatia","Panama","L",1,"2026-06-13","19:00","Lincoln Financial Field","Philadelphia","FINISHED",3,1))
F.append(fx("Belgium","New Zealand","G",1,"2026-06-15","21:00","NRG Stadium","Houston","FINISHED",2,0,True))
F.append(fx("Egypt","Iran","G",1,"2026-06-15","16:00","AT&T Stadium","Dallas","FINISHED",1,0))
F.append(fx("Spain","Saudi Arabia","H",1,"2026-06-15","13:00","Arrowhead Stadium","Kansas City","FINISHED",2,0,True))
F.append(fx("Cape Verde","Uruguay","H",1,"2026-06-16","16:00","Lumen Field","Seattle","FINISHED",1,1))
F.append(fx("France","Senegal","I",1,"2026-06-16","19:00","SoFi Stadium","Los Angeles","FINISHED",2,2,True))
F.append(fx("Norway","Iraq","I",1,"2026-06-16","13:00","BC Place","Vancouver","FINISHED",1,0))
F.append(fx("Argentina","Algeria","J",1,"2026-06-16","21:00","MetLife Stadium","New Jersey","FINISHED",2,0,True))
F.append(fx("Austria","Jordan","J",1,"2026-06-17","13:00","Gillette Stadium","Boston","FINISHED",1,0))
F.append(fx("Portugal","Uzbekistan","K",1,"2026-06-17","16:00","Mercedes-Benz Stadium","Atlanta","FINISHED",2,1))
F.append(fx("Colombia","DR Congo","K",1,"2026-06-17","13:00","Hard Rock Stadium","Miami","FINISHED",2,0))
F.append(fx("Netherlands","Tunisia","F",1,"2026-06-15","19:00","Levi's Stadium","San Francisco","FINISHED",1,0,True))
F.append(fx("Japan","Sweden","F",1,"2026-06-16","16:00","NRG Stadium","Houston","FINISHED",2,1))

# Matchday 2 (finished)
F.append(fx("Brazil","Haiti","C",2,"2026-06-17","20:00","Rose Bowl","Los Angeles","FINISHED",1,1,True))
F.append(fx("England","Croatia","L",2,"2026-06-18","16:00","MetLife Stadium","New Jersey","FINISHED",4,2,True))
F.append(fx("DR Congo","Uzbekistan","K",2,"2026-06-18","16:00","Hard Rock Stadium","Miami","FINISHED",1,3))
F.append(fx("Ghana","Panama","L",2,"2026-06-18","19:00","Lincoln Financial Field","Philadelphia","FINISHED",1,0))
F.append(fx("Czechia","South Africa","A",2,"2026-06-18","21:30","Estadio Akron","Guadalajara","FINISHED",1,1))
F.append(fx("United States","Australia","D",2,"2026-06-19","21:00","Mercedes-Benz Stadium","Atlanta","FINISHED",2,1,True))
F.append(fx("Belgium","Egypt","G",2,"2026-06-20","19:00","AT&T Stadium","Dallas","FINISHED",1,1,True))
F.append(fx("Spain","Cape Verde","H",2,"2026-06-20","16:00","Arrowhead Stadium","Kansas City","FINISHED",2,0,True))
F.append(fx("Germany","Curaçao","E",2,"2026-06-20","13:00","Hard Rock Stadium","Miami","FINISHED",2,1,True))
F.append(fx("Argentina","Austria","J",2,"2026-06-21","16:00","MetLife Stadium","New Jersey","FINISHED",2,1,True))
F.append(fx("France","Norway","I",2,"2026-06-21","19:00","SoFi Stadium","Los Angeles","FINISHED",1,1,True))
F.append(fx("Mexico","South Korea","A",2,"2026-06-18","20:00","Estadio Azteca","Mexico City","FINISHED",1,0,True))
F.append(fx("Portugal","Colombia","K",2,"2026-06-21","13:00","Mercedes-Benz Stadium","Atlanta","FINISHED",2,2,False))
F.append(fx("Netherlands","Japan","F",2,"2026-06-21","21:00","Levi's Stadium","San Francisco","FINISHED",1,0,True))

# Matchday 2 (Remaining matches completed)
F.append(fx("Switzerland","Canada","B",2,"2026-06-18","13:00","BC Place","Vancouver","FINISHED",2,1))
F.append(fx("Qatar","Bosnia and Herzegovina","B",2,"2026-06-19","19:00","BMO Field","Toronto","FINISHED",2,0))
F.append(fx("Scotland","Morocco","C",2,"2026-06-18","16:00","Lumen Field","Seattle","FINISHED",1,1))
F.append(fx("Turkiye","Paraguay","D",2,"2026-06-19","16:00","Gillette Stadium","Boston","FINISHED",2,2))
F.append(fx("Ecuador","Ivory Coast","E",2,"2026-06-20","19:00","Levi's Stadium","San Francisco","FINISHED",3,1))
F.append(fx("Sweden","Tunisia","F",2,"2026-06-20","16:00","NRG Stadium","Houston","FINISHED",1,1))
F.append(fx("Iran","New Zealand","G",2,"2026-06-21","16:00","AT&T Stadium","Dallas","FINISHED",1,2))
F.append(fx("Uruguay","Saudi Arabia","H",2,"2026-06-21","16:00","Lumen Field","Seattle","FINISHED",2,1))
F.append(fx("Iraq","Senegal","I",2,"2026-06-21","13:00","BC Place","Vancouver","FINISHED",0,2))
F.append(fx("Jordan","Algeria","J",2,"2026-06-21","13:00","Gillette Stadium","Boston","FINISHED",1,1))

# Matchday 3
F.append(fx("Mexico","Czechia","A",3,"2026-06-22","20:00","Estadio Azteca","Mexico City","FINISHED",1,1,True))
F.append(fx("South Korea","South Africa","A",3,"2026-06-22","20:00","Estadio Akron","Guadalajara","FINISHED",2,1,False))
F.append(fx("Canada","Bosnia and Herzegovina","B",3,"2026-06-22","16:00","BMO Field","Toronto","FINISHED",2,1,False))
F.append(fx("Switzerland","Qatar","B",3,"2026-06-22","19:00","BC Place","Vancouver","FINISHED",1,2,True))
F.append(fx("Brazil","Scotland","C",3,"2026-06-23","20:00","SoFi Stadium","Los Angeles","FINISHED",1,1,True))
F.append(fx("Haiti","Morocco","C",3,"2026-06-23","16:00","Lumen Field","Seattle","FINISHED",0,1,False))
F.append(fx("United States","Turkiye","D",3,"2026-06-23","21:00","Mercedes-Benz Stadium","Atlanta","FINISHED",2,1,True))
F.append(fx("Australia","Paraguay","D",3,"2026-06-23","16:00","Gillette Stadium","Boston","FINISHED",1,2,False))
F.append(fx("Germany","Ecuador","E",3,"2026-06-24","19:00","Hard Rock Stadium","Miami","FINISHED",3,1,True))
F.append(fx("Curaçao","Ivory Coast","E",3,"2026-06-24","13:00","Levi's Stadium","San Francisco","FINISHED",2,0,False))
F.append(fx("Netherlands","Sweden","F",3,"2026-06-24","19:00","Levi's Stadium","San Francisco","FINISHED",2,0,True))
F.append(fx("Japan","Tunisia","F",3,"2026-06-24","16:00","NRG Stadium","Houston","FINISHED",1,1,False))
F.append(fx("Belgium","Iran","G",3,"2026-06-24","21:00","NRG Stadium","Houston","FINISHED",3,0,True))
F.append(fx("Egypt","New Zealand","G",3,"2026-06-24","16:00","AT&T Stadium","Dallas","FINISHED",2,0,False))
F.append(fx("Spain","Uruguay","H",3,"2026-06-25","13:00","Arrowhead Stadium","Kansas City","FINISHED",2,1,True))
F.append(fx("Cape Verde","Saudi Arabia","H",3,"2026-06-25","16:00","Lumen Field","Seattle","FINISHED",1,1,False))
F.append(fx("France","Iraq","I",3,"2026-06-25","19:00","SoFi Stadium","Los Angeles","FINISHED",3,0,True))
F.append(fx("Norway","Senegal","I",3,"2026-06-25","13:00","BC Place","Vancouver","FINISHED",2,1,False))
F.append(fx("Argentina","Jordan","J",3,"2026-06-25","21:00","MetLife Stadium","New Jersey","FINISHED",2,0,True))
F.append(fx("Austria","Algeria","J",3,"2026-06-25","13:00","Gillette Stadium","Boston","FINISHED",1,0,False))
F.append(fx("Portugal","DR Congo","K",3,"2026-06-22","13:00","Mercedes-Benz Stadium","Atlanta","FINISHED",3,1,False))
F.append(fx("Uzbekistan","Colombia","K",3,"2026-06-22","16:00","Hard Rock Stadium","Miami","FINISHED",1,2,True))
F.append(fx("England","Panama","L",3,"2026-06-22","16:00","MetLife Stadium","New Jersey","FINISHED",3,0,True))
F.append(fx("Croatia","Ghana","L",3,"2026-06-22","19:00","Lincoln Financial Field","Philadelphia","FINISHED",1,1,False))

# ---- Build groups standings from finished fixtures
groups = {}
for tm in T:
    groups.setdefault(tm["group"], [])
    groups[tm["group"]].append({"name":tm["name"],"code":tm["code"],"flag":tm["flag"],
        "P":0,"W":0,"D":0,"L":0,"GF":0,"GA":0,"GD":0,"Pts":0})

def find_row(g: str, name: str) -> Optional[Dict[str, Any]]:
    for r in groups[g]:
        if r["name"] == name:
            return r
    return None

for m in F:
    if m["status"] != "FINISHED":
        continue
    hs, as_ = m["homeScore"], m["awayScore"]
    # Only completed matches with numeric scores contribute to the standings.
    if not isinstance(hs, int) or not isinstance(as_, int):
        continue
    hr, ar = find_row(m["group"], m["home"]), find_row(m["group"], m["away"])
    if not hr or not ar: continue
    for r in (hr,ar): r["P"]+=1
    hr["GF"]+=hs; hr["GA"]+=as_; ar["GF"]+=as_; ar["GA"]+=hs
    if hs>as_: hr["W"]+=1; ar["L"]+=1; hr["Pts"]+=3
    elif hs<as_: ar["W"]+=1; hr["L"]+=1; ar["Pts"]+=3
    else: hr["D"]+=1; ar["D"]+=1; hr["Pts"]+=1; ar["Pts"]+=1

for g in groups:
    for r in groups[g]: r["GD"]=r["GF"]-r["GA"]
    groups[g].sort(key=lambda r:(r["Pts"], r["GD"], r["GF"]), reverse=True)

VENUES = sorted({(m["venue"], m["city"]) for m in F})

import hashlib
for fixture in F:
    story_slug = f"{fixture['slug']}-story"
    unsplash_images = [
        "https://images.unsplash.com/photo-1550591927-391fccf9934b?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1646643508957-088fe0eac722?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1556152352-8edad147cc21?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1529900748604-07564a03e7a6?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1510563800743-aed236490d08?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1486286701208-1d58e9338013?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1518063319789-7217e6706b04?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1551958219-acbc608c6377?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1536122985607-4fe00b283652?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1509048191080-d2984bad6ae5?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1550565118-3a14e8d0386f?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1551244072-5d12893278ab?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1531415074968-036ba1b575da?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1524413840807-0c3cb6fa808d?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1511512578047-dfb367046420?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1504307651254-35680f356dfd?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1518843025960-d60217f226f5?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1520333789090-1afc82db536a?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1522071820081-009f0129c71c?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1523240795612-9a054b0db644?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1542744095-291d1f67b221?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1543269865-cbf427effbad?crop=entropy&cs=srgb&fm=jpg&q=85",
        "https://images.unsplash.com/photo-1543807535-eceef0bc6599?crop=entropy&cs=srgb&fm=jpg&q=85"
    ]
    img_idx = int(hashlib.md5(fixture['slug'].encode('utf-8')).hexdigest(), 16) % len(unsplash_images)
    img_url = unsplash_images[img_idx]
    
    home, away = fixture["home"], fixture["away"]
    hs, as_ = fixture["homeScore"], fixture["awayScore"]
    played = fixture["status"] == "FINISHED"
    score_str = f" {hs}-{as_}" if (played and hs is not None and as_ is not None) else ""
    title = f"{home} vs {away}{score_str} Match Report"
    
    if not any(s["slug"] == story_slug for s in STORIES_META):
        STORIES_META.append({
            "slug": story_slug,
            "title": title,
            "category": "Match Report",
            "excerpt": f"Full editorial coverage and details of the World Cup match between {home} and {away}.",
            "img": img_url,
            "read": 4
        })

data = {
  "meta": {
    "name":"MatchTales",
    "tournament":"FIFA World Cup 2026",
    "hosts":["United States","Mexico","Canada"],
    "startDate":"2026-06-11",
    "today":"2026-06-26",
    "tagline":"Why this match matters.",
    "groupsCount":12, "teamsCount":48,
  },
  "teams": T,
  "groups": groups,
  "fixtures": F,
  "rivalries": RIV,
  "moments": MOMENTS,
  "storiesMeta": STORIES_META,
  "venues": [{"venue":v,"city":c} for v,c in VENUES],
}

def clean_style(val: Any) -> Any:
    if isinstance(val, str):
        # Replace em-dash with a clean space-hyphen-space
        val = val.replace("—", " - ")
        # Replace double-hyphen with a single hyphen
        val = val.replace("--", "-")
        return val
    elif isinstance(val, list):
        return [clean_style(v) for v in val]
    elif isinstance(val, dict):
        return {k: clean_style(v) for k, v in val.items()}
    return val

data = clean_style(data)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {OUT} | teams={len(T)} fixtures={len(F)} groups={len(groups)} rivalries={len(RIV)}")

