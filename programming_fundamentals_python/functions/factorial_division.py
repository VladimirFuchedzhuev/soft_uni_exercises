def factorial(num_1, num_2):
    new_num_1 = 1
    new_num_2 = 1
    for num in range(1, num_1 + 1):
        new_num_1 *= num
    for num in range(1, num_2 + 1):
        new_num_2 *= num
    
    return new_num_1 / new_num_2

num_1 = int(input())
num_2 = int(input())

print(f"{factorial(num_1, num_2):.2f}")