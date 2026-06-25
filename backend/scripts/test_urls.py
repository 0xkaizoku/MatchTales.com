import urllib.request
import urllib.error

urls = [
    "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?crop=entropy&cs=srgb&fm=jpg&q=85",
    "https://images.unsplash.com/photo-1544698310-74ea9d1c8258?crop=entropy&cs=srgb&fm=jpg&q=85",
    "https://images.unsplash.com/photo-1518063319789-7217e6706b04?crop=entropy&cs=srgb&fm=jpg&q=85",
    "https://images.unsplash.com/photo-1522778147-f246514b53fb?crop=entropy&cs=srgb&fm=jpg&q=85",
    "https://images.unsplash.com/photo-1524143980106-21141365837f?crop=entropy&cs=srgb&fm=jpg&q=85",
    "https://images.unsplash.com/photo-1551958219-acbc608c6377?crop=entropy&cs=srgb&fm=jpg&q=85",
    "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?crop=entropy&cs=srgb&fm=jpg&q=85",
    "https://images.unsplash.com/photo-1459865264687-595d652de67e?crop=entropy&cs=srgb&fm=jpg&q=85",
    "https://images.unsplash.com/photo-1517649763962-0c623066013b?crop=entropy&cs=srgb&fm=jpg&q=85",
    "https://images.unsplash.com/photo-1574629810360-7efbbe195018?crop=entropy&cs=srgb&fm=jpg&q=85"
]

for url in urls:
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            print(f"OK ({response.status}): {url}")
    except Exception as e:
        print(f"FAILED: {url} | Error: {e}")
