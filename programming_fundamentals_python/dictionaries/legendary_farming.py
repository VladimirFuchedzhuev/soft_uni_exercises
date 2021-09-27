data = input()
key_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
is_obtained = False

while not is_obtained:
    materials = data.split()

    for index in range(0, len(materials), 2):
        if is_obtained:
            break

        material = materials[index + 1].lower()
        quantity = int(materials[index])
        if material in items:
            items[material] += quantity
        else:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += quantity
        for material, quantity in items.items():
            if quantity >= 250:
                is_obtained = True
                items[material] -= 250
                print(f"{key_materials[material]} obtained!")
                break

    if is_obtained:
        break
         
    data = input()

sorted_items = sorted(items.items(), key=lambda kvp: (-kvp[1], kvp[0]))

for material, quantity in sorted_items:
    print(f"{material}: {quantity}")

sorted_junk_items = sorted(junk_items.items(), key=lambda kvp: kvp[0])

for material, quantity in sorted_junk_items:
    print(f"{material}: {quantity}")
