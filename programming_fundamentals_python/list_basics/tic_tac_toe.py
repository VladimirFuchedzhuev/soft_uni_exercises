line_one = [int(el) for el in input().split()]
line_two = [int(el) for el in input().split()]
line_three = [int(el) for el in input().split()]
won = 0
for x in range(len(line_one)):
    if line_one[x] == line_two[x] == line_three[x]:
        if line_one[x] == 1:
            won = "First"
        elif line_one[x] == 2:
            won = "Second"

if all(line_one):
    if line_one[0] == 1:
        won = "First"
    elif line_one[0] == 2:
        won = "Second"

if all(line_two):
    if line_two[0] == 1:
        won = "First"
    elif line_two[0] == 2:
        won = "Second"

if all(line_three):
    if line_three[0] == 1:
        won = "First"
    elif line_three[0] == 2:
        won = "Second"

if line_one[0] == line_two[1] == line_three[2]:
    if line_one[0] == 1:
        won = "First"
    elif line_one[0] == 2:
        won = "Second"

if line_one[2] == line_two[1] == line_three[0]:
    if line_one[2] == 1:
        won = "First"
    elif line_one[2] == 2:
        won = "Second"

if won == 0:
    print("Draw!")
else:
    print(f"{won} player won")