n = int(input())

first_group = 0
second_group = 0
third_group = 0

for i in range(1, n + 1):
    num = int(input())
    if num % 2 == 0:
        first_group += 1
    if num % 3 == 0:
        second_group += 1
    if num % 4 == 0:
        third_group += 1

p1 = first_group / n * 100
p2 = second_group / n * 100
p3 = third_group / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")