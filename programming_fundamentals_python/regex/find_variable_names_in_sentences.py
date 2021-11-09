import re

pattern = r"\b\_(?P<variable_name>[A-Za-z0-9]+)\b"
text = input()
grouped_matches = []
matches = re.finditer(pattern, text)
for match in matches:
    grouped_matches.append(match.group('variable_name'))
    
print(','.join(grouped_matches))