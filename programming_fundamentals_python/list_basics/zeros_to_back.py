numbers = [int(x) for x in input().split(", ")]
zero_count = numbers.count(0)
numbers = [int(x) for x in numbers if x != 0]
for i in range(zero_count):
    numbers.append(0)
print(numbers)