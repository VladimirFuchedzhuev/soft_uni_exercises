import math

def get_distance(a, b, c, d):
    a = math.pow(a, 2)
    b = math.pow(b, 2)
    c = math.pow(c, 2)
    d = math.pow(d, 2)
    return math.sqrt(a + b + c + d)

def center_point(a, b):
    a = math.pow(a, 2)
    b = math.pow(b, 2)
    return math.sqrt(a + b)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

first_line = get_distance(x1, y1, x2, y2)
second_line = get_distance(x3, y3, x4, y4)

if first_line >= second_line:
    if center_point(x1, y1) <= center_point(x2, y2):
        print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")
else:
    if center_point(x3, y3) <= center_point(x4, y4):
        print(f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})")
    else:
        print(f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})")