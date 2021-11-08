import re

text = input().lower()
word = input().lower()

pattern = rf"\b{word}\b"

matches = [w.group() for w in re.finditer(pattern, text)]
print(len(matches))