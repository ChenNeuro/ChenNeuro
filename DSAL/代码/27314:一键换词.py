import re
raw = input().lower()
old, new = input().lower().split()
text = re.sub(r'(?<=\b)' + old + r'(?=\b)', new, raw)
print(". ".join(s.capitalize() for s in text.split(". ")))
