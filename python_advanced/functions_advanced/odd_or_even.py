command= input()
numbers = [int(x) for x in input().split()]

parity = 0 if command == "Even" else 1
sum_of_numbers = sum(filter(lambda x: x % 2 == parity, numbers))

print(sum_of_numbers * len(numbers))