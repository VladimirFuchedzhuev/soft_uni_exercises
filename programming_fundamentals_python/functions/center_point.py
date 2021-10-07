from math import floor


def center_point(a, b):
    result = abs(a) + abs(b)
    return result

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

point_1 = center_point(x_1, y_1)
point_2 = center_point(x_2, y_2)

if point_1 >= point_2:
    print(f"({floor(x_2)}, {floor(y_2)})")
else:
    print(f"({floor(x_1)}, {floor(y_1)})")