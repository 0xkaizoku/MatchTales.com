import urllib.request
import urllib.error

ids = [
    # Stadiums and pitches
    "photo-1550591927-391fccf9934b",
    "photo-1646643508957-088fe0eac722",
    "photo-1556152352-8edad147cc21",
    "photo-1529900748604-07564a03e7a6",
    "photo-1431324155629-1a6deb1dec8d",
    "photo-1510563800743-aed236490d08",
    "photo-1486286701208-1d58e9338013",
    "photo-1562079592-c17c8c92b300",
    "photo-1579952363873-27f3bade9f55",
    "photo-1518063319789-7217e6706b04",
    "photo-1551958219-acbc608c6377",
    "photo-1516245556604-14300bf7aeeb",
    "photo-1536122985607-4fe00b283652",
    "photo-1509048191080-d2984bad6ae5",
    "photo-1526232761682-d7100d17ff2b",
    "photo-1552820728-8b83bb6b773f",
    "photo-1624880351058-2fb07e609bcf",
    "photo-1560272564-c83b66b1ad12",
    "photo-1550565118-3a14e8d0386f",
    "photo-1508847154043-be12a62861c1",
    "photo-1551244072-5d12893278ab",
    "photo-1531415074968-036ba1b575da",
    "photo-1524413840807-0c3cb6fa808d",
    "photo-1595182877141-862d2948bbca",
    "photo-1606925797300-0b35e9d17d0e",
    "photo-1518605333140-55aa797b5f36",
    # Additional candidates
    "photo-1511512578047-dfb367046420",
    "photo-1504307651254-35680f356dfd",
    "photo-1517245386807-bb43f82c33c4",
    "photo-1518843025960-d60217f226f5",
    "photo-1519766304817-4f37bda74a27",
    "photo-1520333789090-1afc82db536a",
    "photo-1521791136368-1a9b82757a57",
    "photo-1522071820081-009f0129c71c",
    "photo-1523240795612-9a054b0db644",
    "photo-1534438327276-14e5300c3a48",
    "photo-1542744094-3a31f103e35f",
    "photo-1542744095-291d1f67b221",
    "photo-1543269865-cbf427effbad",
    "photo-1543807535-eceef0bc6599"
]

print("Testing candidate IDs...")
working_ids = []

for photo_id in ids:
    url = f"https://images.unsplash.com/{photo_id}?crop=entropy&cs=srgb&fm=jpg&q=85"
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                working_ids.append(photo_id)
                print(f"OK: {photo_id}")
    except Exception as e:
        # Ignore failed ones
        pass

print("\n=== WORKING PHOTO IDS ===")
print(json.dumps(working_ids))
print(f"Total working: {len(working_ids)}")
