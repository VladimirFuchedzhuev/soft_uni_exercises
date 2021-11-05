number_of_rooms = int(input())
enough_chairs = True
available_chairs = 0
for room in range(1, number_of_rooms + 1):
    chairs, n_people = input().split()
    n_people = int(n_people)
    difference = abs(len(chairs) - n_people)
    if len(chairs) < n_people:
        print(f"{difference} more chairs needed in room {room}")
        enough_chairs = False
    else:
        available_chairs += difference

if enough_chairs:
    print(f"Game On, {available_chairs} free chairs left")