number = int(input())

heroes = {}
max_health = 100
max_mana = 200
for i in range(number):
    name, health, mana = input().split()
    health = int(health)
    mana = int(mana)
    heroes[name] = {'health': health, 'mana': mana}

while True:
    command = input()
    if command == "End":
        break
    data = command.split(" - ")
    action = data[0]
    hero_name = data[1]
    if action == "CastSpell":
        needed_mana = int(data[2])
        spell = data[3]
        if heroes[hero_name]['mana'] >= needed_mana:
            print(
                f"{hero_name} has successfully cast {spell} and now has {heroes[hero_name]['mana'] - needed_mana} MP!")
            heroes[hero_name]['mana'] -= needed_mana
        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")
    elif action == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        heroes[hero_name]['health'] -= damage
        if heroes[hero_name]['health'] > 0:
            print(
                f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['health']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            heroes.pop(hero_name)
    elif action == "Recharge":
        amount = int(data[2])
        if heroes[hero_name]['mana'] + amount > max_mana:
            print(f"{hero_name} recharged for {max_mana - heroes[hero_name]['mana']} MP!")
            heroes[hero_name]['mana'] += max_mana - heroes[hero_name]['mana']
        else:
            heroes[hero_name]['mana'] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif action == "Heal":
        hp = int(data[2])
        if heroes[hero_name]['health'] + hp > max_health:
            print(f"{hero_name} healed for {max_health - heroes[hero_name]['health']} HP!")
            heroes[hero_name]['health'] += max_health - heroes[hero_name]['health']
        else:
            heroes[hero_name]['health'] += hp
            print(f"{hero_name} healed for {hp} HP!")
sorted_heroes = sorted(heroes.items(), key=lambda tkvp: (-tkvp[1]['health'], tkvp[0]))
for key, value in sorted_heroes:
    print(f"{key}\n  HP: {value['health']}\n  MP: {value['mana']}")