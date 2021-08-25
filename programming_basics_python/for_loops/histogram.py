n = int(input())

first_group = 0
second_group = 0
third_group = 0
forth_group = 0
fifth_group = 0

for number in range(1, n + 1):
    number = int(input())
    if number < 200:
        first_group += 1
    elif 200 <= number <= 399:
        second_group += 1
    elif 400 <= number <= 599:
        third_group += 1
    elif 600 <= number <= 799:
        forth_group += 1
    elif number >= 800:
        fifth_group += 1

p1 = first_group / n * 100
p2 = second_group / n * 100
p3 = third_group / n * 100
p4 = forth_group / n * 100
p5 = fifth_group / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")