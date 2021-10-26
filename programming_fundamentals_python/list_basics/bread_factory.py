working_day = input().split("|")

initial_energy = 100
initial_coins = 100
is_bankrupted = False

for event in working_day:
    working_event = event.split("-")
    action = working_event[0]
    value = int(working_event[1])

    if action == "rest":
        gained_energy = value
        if initial_energy + value > 100:
            gained_energy = 100 - initial_energy
        initial_energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif action == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += value
            print(f"You earned {value} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins - value > 0:
            initial_coins -= value
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            is_bankrupted = True
            break
if not is_bankrupted:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")


