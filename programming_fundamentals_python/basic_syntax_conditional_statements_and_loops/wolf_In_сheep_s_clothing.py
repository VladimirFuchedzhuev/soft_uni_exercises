herd = input()
herd_list = herd.split(", ")
position_counter = 0

for i in range(len(herd_list) - 1, -1, -1):
    if herd_list[i] == "wolf":
        if position_counter == 0:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {position_counter}! You are about to be eaten by a wolf!")
    else:
        position_counter += 1
