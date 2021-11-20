import re

pattern = r"(\=|\/)(?P<city>[A-Z][A-Za-z]{2,})\1"
travel_points = 0
command = input()
going_to = []
destinations = re.finditer(pattern, command)
for i in destinations:
    going_to.append(i.group('city'))
    travel_points += len(i.group('city'))
print(f"Destinations: {', '.join(going_to)}\nTravel Points: {travel_points}")