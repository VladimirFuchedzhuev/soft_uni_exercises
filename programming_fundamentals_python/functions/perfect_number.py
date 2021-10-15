def perfect_number(number):
    proper_divisors = []
    for num in range(1, number):
        if number % num == 0:
            proper_divisors.append(num)
    if sum(proper_divisors) == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number_check = perfect_number(int(input()))
print(number_check)