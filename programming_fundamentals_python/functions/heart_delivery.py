neighborhood = [int(num) for num in input().split('@')]
house_position = 0

command = input().split()

while not command[0] == 'Love!':
    house_position += int(command[1])
    if house_position >= len(neighborhood):
        house_position = 0

    if neighborhood[house_position] == 0:
        print(f"Place {house_position} already had Valentine's day.")
    else:
        neighborhood[house_position] -= 2

        if neighborhood[house_position] == 0:
            print(f"Place {house_position} has Valentine's day.")

    command = input().split()

missed_houses = len(neighborhood) - neighborhood.count(0)
print(f"Cupid's last position was {house_position}.")
if missed_houses == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {missed_houses} places.")
