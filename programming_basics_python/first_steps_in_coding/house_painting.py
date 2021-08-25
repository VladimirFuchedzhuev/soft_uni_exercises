x = float(input())
y = float(input())
h = float(input())
#стени
side_wall = x * y
window = 1.5 ** 2
side_walls = side_wall * 2 - window * 2
back_wall = x ** 2
door = 1.2 * 2
front_back_walls = back_wall * 2 - door
total_area = front_back_walls + side_walls
green_paint = total_area / 3.4
#покрив
side_roof = (x * y) * 2
front_back_roof = ((h * x) / 2) * 2
red_paint = (side_roof + front_back_roof) / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")