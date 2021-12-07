def fill_the_box(height, width, length, *args):
    box_area = height * width * length
    left_cubes = 0
    enough_room = True
    for el in args:
        if el == 'Finish':
            break
        if el > box_area and enough_room:
            enough_room = False
            left_cubes += el - box_area
            continue
        if not enough_room:
            left_cubes += el
        else:
            box_area -= el

    if not enough_room:
        return f"No more free space! You have {left_cubes} more cubes."
    else:
        return f"There is free space in the box. You could put {box_area} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
