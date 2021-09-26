dragon_count = int(input())
dragon_collection = {}

for _ in range(dragon_count):
    dragon_type, name, damage, health, armor = input().split()

    if damage == "null":
        damage = 45
    else:
        damage = int(damage)
    if health == "null":
        health = 250
    else:
        health = int(health)
    if armor == "null":
        armor = 10
    else:
        armor = int(armor)
    if dragon_type not in dragon_collection:
        dragon_collection[dragon_type] = {name: {'damage': damage, 'health': health, 'armor': armor}}
    else:
        dragon_collection[dragon_type][name] = {'damage': damage, 'health': health, 'armor': armor}

for key, dragon in dragon_collection.items():
    total_group_damage, total_group_health, total_group_armor, divider = 0, 0, 0, len(dragon)
    for digit in dragon.values():
        total_group_damage += digit['damage']
        total_group_health += digit['health']
        total_group_armor += digit['armor']

    total_group_damage = total_group_damage / divider
    total_group_health = total_group_health / divider
    total_group_armor = total_group_armor / divider
    print(f"{key}::({total_group_damage:.2f}/{total_group_health:.2f}/{total_group_armor:.2f})")

    for key, value in sorted(dragon.items()):
        damage, health, armor = value.values()
        print(f"-{key} -> damage: {damage}, health: {health}, armor: {armor}")