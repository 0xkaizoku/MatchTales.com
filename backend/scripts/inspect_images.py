import glob
import re

files = glob.glob('frontend/src/content/stories/*.md')
print(f"Total stories checked: {len(files)}")
broken_or_missing = []

for f in files:
    content = open(f, encoding='utf-8').read()
    match = re.search(r'image:\s*\"?(.*?)\"?\n', content)
    if not match:
        print(f"No image field in: {f}")
        broken_or_missing.append(f)
    else:
        url = match.group(1).strip('"\'')
        if not url.startswith("http"):
            print(f"Invalid URL in {f}: {url}")
            broken_or_missing.append(f)

if not broken_or_missing:
    print("All stories have valid image URLs starting with http!")
else:
    print(f"Found {len(broken_or_missing)} broken stories.")
