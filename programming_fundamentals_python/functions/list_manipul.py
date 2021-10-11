def exchange(numbers, index):
    return numbers[index + 1:] + numbers[:index + 1]


def max_even(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    if len(even_numbers) > 0:
        max_even_num = max(even_numbers)
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] == max_even_num:
                return i
    else:
        return "No matches"


def max_odd(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    if len(odd_numbers) > 0:
        max_odd_num = max(odd_numbers)
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] == max_odd_num:
                return i
    else:
        return "No matches"


def min_even(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    if len(even_numbers) > 0:
        min_even_num = min(even_numbers)
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] == min_even_num:
                return i
    else:
        return "No matches"


def min_odd(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    if len(odd_numbers) > 0:
        min_odd_num = min(odd_numbers)
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] == min_odd_num:
                return i
    else:
        return "No matches"


def first_even(numbers, get_numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers[:get_numbers]


def first_odd(numbers, get_numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers[:get_numbers]


def last_even(numbers, get_numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers[-get_numbers:]


def last_odd(numbers, get_numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers[-get_numbers:]


numbers = [int(num) for num in input().split()]
command = input()

while command != "end":
    get_function = command.split()
    if get_function[0] == "exchange":
        index = int(get_function[1])
        if index not in range(len(numbers)):
            print("Invalid index")
        else:
            numbers = exchange(numbers, index)
    elif get_function[0] == "max":
        type = get_function[1]
        if type == "even":
            print(max_even(numbers))
        elif type == "odd":
            print(max_odd(numbers))
    elif get_function[0] == "min":
        type = get_function[1]
        if type == "even":
            print(min_even(numbers))
        elif type == "odd":
            print(min_odd(numbers))
    elif get_function[0] == "first":
        get_numbers = int(get_function[1])
        if get_numbers > len(numbers):
            print("Invalid count")
        else:
            type = get_function[2]
            if type == "even":
                print(first_even(numbers, get_numbers))
            elif type == "odd":
                print(first_odd(numbers, get_numbers))
    elif get_function[0] == "last":
        get_numbers = int(get_function[1])
        if get_numbers > len(numbers):
            print("Invalid count")
        else:
            type = get_function[2]
            if type == "even":
                print(last_even(numbers, get_numbers))
            elif type == "odd":
                print(last_odd(numbers, get_numbers))
    command = input()

print(numbers)