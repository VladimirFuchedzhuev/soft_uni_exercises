import re

pattern = r"^>>(?P<Furniture>[A-Za-z]+)<<(?P<Price>\d+\.?\d+)!(?P<Quantity>\d+)$"
command = input()

furniture_stats = []
total_price = 0

while not command == "Purchase":
    valid_furniture = re.match(pattern, command)
    if valid_furniture:
        furniture_name = valid_furniture.group("Furniture")
        price = float(valid_furniture.group("Price"))
        quantity = int(valid_furniture.group("Quantity"))

        furniture_stats.append(furniture_name)
        total_price += price * quantity
    command = input()

print("Bought furniture:")
for furniture in furniture_stats:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")
