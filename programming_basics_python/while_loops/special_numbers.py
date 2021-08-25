n = int(input())

for number in range(1111, 10000):
    units = number % 10
    tens = number // 10 % 10
    hundreds = number // 100 % 10
    thousands = number // 1000

    check1 = units != 0 and n % units == 0
    check2 = tens != 0 and n % tens == 0
    check3 = hundreds != 0 and n % hundreds == 0
    check4 = n % thousands == 0

    if check1 and check2 and check3 and check4:
        print(number, end=' ')