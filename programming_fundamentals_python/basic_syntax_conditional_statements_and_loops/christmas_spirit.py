quantity = int(input())
days = int(input())

ornament_set= 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
expenses = 0
christmas_spirit = 0
days_counter = 0

for day in range(1, days + 1):
    days_counter += 1
    if days_counter % 11 == 0:
        quantity += 2
    if days_counter % 2 == 0:
        expenses += ornament_set * quantity
        christmas_spirit += 5
    if days_counter % 3 == 0:
        expenses += (tree_skirt + tree_garlands) * quantity
        christmas_spirit += 13
    if days_counter % 5 == 0:
        expenses += tree_lights * quantity
        christmas_spirit += 17
        if days_counter % 3 == 0:
            christmas_spirit += 30
    if days_counter % 10 == 0:
        christmas_spirit -= 20
        expenses += tree_skirt + tree_garlands + tree_lights

if days % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {expenses}")
print(f"Total spirit: {christmas_spirit}")
