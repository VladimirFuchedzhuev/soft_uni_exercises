num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sign(n_1, n_2, n_3):
    counter = 0
    if n_1 == 0 or n_2 == 0 or n_3 == 0:
        counter = -1
        return counter
    else:
        if num_1 > 0:
            counter += 1
        if num_2 > 0:
            counter += 1
        if num_3 > 0:
            counter += 1
        return counter


multiplication = sign(num_1, num_2, num_3)
if multiplication == -1:
    print("zero")
elif multiplication % 2 == 0:
    print("negative")
else:
    print('positive')