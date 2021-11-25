data = input()
cities = {}

while not data == "Sail":
    city, population, gold = data.split("||")
    population, gold = int(population), int(gold)

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

    data = input()

new_data = input()

while not new_data == "End":
    new_data = new_data.split("=>")
    if new_data[0] == "Plunder":
        town = new_data[1]
        people = int(new_data[2])
        gold = int(new_data[3])

        cities[town]['population'] -= people
        cities[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    elif new_data[0] == "Prosper":
        town = new_data[1]
        gold = int(new_data[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            new_data = input()
            continue
        cities[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

    new_data = input()

if not cities:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    sorted_result = sorted(cities.items(), key=lambda tkvp: (-tkvp[1]['gold'], tkvp[0]))
    print(f"Ahoy, Captain! There are {len(sorted_result)} wealthy settlements to go to:")
    for town, stats in sorted_result:
        print(f"{town} -> Population: {stats['population']} citizens, Gold: {stats['gold']} kg")
