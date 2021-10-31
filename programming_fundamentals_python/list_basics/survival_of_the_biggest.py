list_of_numbers = [int(x) for x in (input().split())]
number = int(input())

[list_of_numbers.remove(min(list_of_numbers)) for x in range(number)]

print(", ".join([str(x) for x in list_of_numbers]))
