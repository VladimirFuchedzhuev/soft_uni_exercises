import math
object_input = input()
square = "square"
rectangle = "rectangle"
circle = "circle"
if object_input == square:
    a_square = float(input())
    area = a_square ** 2
elif object_input == rectangle:
    a_rectangle = float(input())
    b_rectangle = float(input())
    area = a_rectangle * b_rectangle
elif object_input == circle:
    r = float(input())
    area = math.pi * (r ** 2)
else:
    base = float(input())
    hight = float(input())
    area = (base * hight) / 2

print(f"{area:.3f}")
