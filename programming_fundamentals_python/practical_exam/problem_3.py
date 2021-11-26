data = input()
liked_meals = {}
unliked_meals = 0

while not data == "Stop":
    data = data.split("-")
    if data[0] == "Like":
        guest = data[1]
        meal = data[2]
        if guest not in liked_meals:
            liked_meals[guest] = []
        if meal not in liked_meals[guest]:
            liked_meals[guest].append(meal)
    elif data[0] == "Unlike":
        guest = data[1]
        meal = data[2]
        if guest not in liked_meals:
            print(f"{guest} is not at the party.")
        elif meal not in liked_meals[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            liked_meals[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
            unliked_meals += 1

    data = input()

sorted_guests = sorted(liked_meals.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

for (guest, meals) in sorted_guests:
    print(f"{guest}: {', '.join(meals)}")

print(f'Unliked meals: {unliked_meals}')