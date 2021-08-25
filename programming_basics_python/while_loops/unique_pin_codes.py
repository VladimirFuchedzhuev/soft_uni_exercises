first_num_limit = int(input())
second_num_limit = int(input())
third_num_limit = int(input())



for num1 in range(2, first_num_limit + 1, 2):
    for num2 in range(2, second_num_limit + 1):
        is_prime = False
        counter = 0
        for num in range(0, num2 + 1):
            if num != 0:
                if num2 % num == 0:
                    counter += 1
        if counter == 2:
            is_prime = True
        for num3 in range(2, third_num_limit + 1, 2):
            if is_prime:
                print(num1, num2, num3)


