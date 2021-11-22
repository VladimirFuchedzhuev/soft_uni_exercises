num = int(input())
plants = {}
for i in range(num):
    text = input().split("<->")
    plant = text[0]
    rarity = int(text[1])
    if plant not in plants.keys():
        plants[plant] = []
        plants[plant].append(rarity)
    else:
        plants[plant] = []
        plants[plant].append(rarity)

while True:
    text = input()
    if text == "Exhibition":
        break
    command = text.split(": ")[0]
    second_part = text.split(": ")[1]
    if "Rate" in text:
        plant_to_be_rated = second_part.split(" - ")[0]
        rating_plant = int(second_part.split(" - ")[1])
        if plant_to_be_rated not in plants.keys():
            print("error")
        else:
            plants[plant_to_be_rated].append(rating_plant)
    elif "Update" in text:
        update_plant = second_part.split(" - ")[0]
        if update_plant not in plants.keys():
            print("error")
        else:
            new_rarity = int(second_part.split(" - ")[1])
            plants[update_plant].pop(0)
            plants[update_plant].insert(0, new_rarity)
    elif "Reset" in text:
        plant_to_be_reset = text.split(": ")[1]
        if plant_to_be_reset not in plants.keys():
            print("error")
        else:
            rarity_to_add_back = plants[plant_to_be_reset][0]
            plants[plant_to_be_reset].clear()
            plants[plant_to_be_reset].append(rarity_to_add_back)

for key, value in plants.items():
    item_to_amend = value[1:]
    remaining_part = value[0]
    if len(item_to_amend) > 1:
        sum_all_ratings = sum(item_to_amend)
        average_rating = sum_all_ratings / len(item_to_amend)
        value.clear()
        value.append(remaining_part)
        value.append(average_rating)
    if len(value) == 1:
        value.append(0)

print(f"Plants for the exhibition:")
plants = dict(sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][1])))
for key, value in plants.items():
    print(f"- {key}; Rarity: {int(value[0])}; Rating: {value[1]:.2f}")