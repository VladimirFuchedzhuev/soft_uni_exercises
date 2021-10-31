n = int(input())
numbers = []
filtered = []

for i in range(n):
    current_number = int(input())
    numbers.append(current_number)
command = input()
for number in numbers:
    if command == "even":
        if number % 2 == 0:
            filtered.append(number)
    if command == "odd":
        if not number % 2 == 0:
            filtered.append(number)
    if command == "positive":
        if number >=0:
            filtered.append(number)
    if command == "negative":
        if number < 0:
            filtered.append(number)

print(filtered)
