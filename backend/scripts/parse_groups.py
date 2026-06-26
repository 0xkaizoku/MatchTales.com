import re

filepath = r"C:\Users\THIS PC\.gemini\antigravity-ide\brain\6c997e21-6c01-4d26-98ad-a2ad4840e449\.system_generated\steps\711\content.md"
content = open(filepath, encoding="utf-8").read()

groups = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
for g in groups:
    print(f"=== Group {g} ===")
    matches = list(re.finditer(rf"Group {g}\b", content))
    if matches:
        for idx in range(min(5, len(matches))):
            start = matches[idx].start()
            snippet = content[max(0, start-50):start+300]
            print(f"Match {idx}: {snippet.replace(chr(10), ' ')}")

