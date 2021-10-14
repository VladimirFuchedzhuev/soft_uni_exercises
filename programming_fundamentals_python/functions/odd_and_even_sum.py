def odd_even(number):
    odd_sum = 0
    even_sum = 0

    for ch in number:
        digit = int(ch)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    
    return f"Odd sum = {str(odd_sum)}, Even sum = {str(even_sum)}"

number = input()
print(odd_even(number))