import re

text = input()
pattern = r"(?P<sep>[#|\|])(?P<food>([A-Z( )*a-z])+)(?P=sep)(?P<expiration>(\d{2}\/\d{2}\/\d{2})*)(?P=sep)(?P<calories>\d+)(?P=sep)"
food = re.finditer(pattern, text)
total_calories = 0
for match in food:
    total_calories += int(match.group("calories"))
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
food = re.finditer(pattern, text)
for match in food:
    print(
        f"Item: {match.group('food')}, Best before: {match.group('expiration')}, Nutrition: {match.group('calories')}")