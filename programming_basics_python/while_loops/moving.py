width = int(input())
length = int(input())
height = int(input())
total_volume = width * length * height
command = input()
enough_room = True
while command != "Done":
    boxes = int(command)
    total_volume -= boxes
    if total_volume < 0:
        enough_room = False
        break
    command = input()
if not enough_room:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")
else:
    print(f"{total_volume} Cubic meters left.")