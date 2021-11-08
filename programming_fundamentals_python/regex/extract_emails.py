import re

pattern = r"\s(?P<e_mail>[A-Za-z0-9]+[A-Za-z0-9\.\-\_]*\@[A-za-z]+[A-Za-z\-]*(\.[A-Za-z]+)+)\b"
text = input()
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group('e_mail'))