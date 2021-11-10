import re
pattern = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})"
text = input()
result = re.finditer(pattern, text)
valid_numbers = [match.group() for match in result]

print(", ".join(valid_numbers))
