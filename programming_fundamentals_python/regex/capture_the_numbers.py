import re

command = input()
pattern = r"\d+"
digits = []
while command:
    for num in re.finditer(pattern, command):
        digits.append(num.group())
    command = input()
print(*digits)