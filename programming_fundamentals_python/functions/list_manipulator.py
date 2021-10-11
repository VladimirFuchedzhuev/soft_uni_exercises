def exchange(numbers_list, index):
    return numbers_list[index + 1:] + numbers_list[:index + 1]


def max_even(numbers_list):
    if len(even_numbers) > 0:
        max_even_num = max(even_numbers)
        for i in range(len(numbers_list) - 1, -1, -1):
            if numbers_list[i] == max_even_num:
                return i
    else:
        return "No matches"


def max_odd(numbers_list):
    if len(odd_numbers) > 0:
        max_odd_number = max(odd_numbers)
        for i in range(len(numbers_list) - 1, -1, -1):
            if numbers_list[i] == max_odd_number:
                return i
    else:
        return "No matches"


def min_even(numbers_list):
    if len(even_numbers) > 0:
        min_even_num = min(even_numbers)
        for i in range(len(numbers_list) - 1, -1, -1):
            if numbers_list[i] == min_even_num:
                return i
    else:
        return "No matches"


def min_odd(numbers_list):
    if len(odd_numbers) > 0:
        min_odd_num = min(odd_numbers)
        for i in range(len(numbers_list) - 1, -1, -1):
            if numbers_list[i] == min_odd_num:
                return i
    else:
        return "No matches"


def first_even(count):
    return even_numbers[:count]


def first_odd(count):
    return odd_numbers[:count]


def last_even(count):
    return even_numbers[-count:]


def last_odd(count):
    return odd_numbers[-count:]


numbers = [int(num) for num in input().split()]
command = input()
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 == 1]

while not command == "end":
    get_function = command.split()
    if get_function[0] == 'exchange':
        index = int(get_function[1])
        if index not in range(len(numbers)):
            print("Invalid index")
        else:
            numbers = exchange(numbers, index)
    elif get_function[0] == 'max':
        if get_function[1] == 'even':
            print(max_even(numbers))
        elif get_function[1] == 'odd':
            print(max_odd(numbers))
    elif get_function[0] == 'min':
        if get_function[1] == 'even':
            print(min_even(numbers))
        elif get_function[1] == 'odd':
            print(min_odd(numbers))
    elif get_function[0] == 'first':
        get_number = int(get_function[1])
        if get_number > len(numbers):
            print('Invalid count')
        elif get_function[2] == 'even':
            print(first_even(get_number))
        elif get_function[2] == 'odd':
            print(first_odd(get_number))
    elif get_function[0] == 'last':
        get_number = int(get_function[1])
        if get_number > len(numbers):
            print('Invalid count')
        elif get_function[2] == 'even':
            print(last_even(get_number))
        elif get_function[2] == 'odd':
            print(last_odd(get_number))
    even_numbers = [x for x in numbers if x % 2 == 0]
    odd_numbers = [x for x in numbers if x % 2 == 1]
    command = input()

print(numbers)
