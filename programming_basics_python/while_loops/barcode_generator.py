num1 = int(input())
num2 = int(input())

for num in range(num1, num2 + 1):
    units = num % 10  # единици
    tens = num // 10 % 10  # десетици
    hundreds = num // 100 % 10  # стотици
    thousands = num // 1000  # хилядни

    check1 = units != 0 and units % 2 != 0
    check2 = tens != 0 and tens % 2 != 0
    check3 = hundreds != 0 and hundreds % 2 != 0
    check4 = thousands % 2 != 0

    if check1 and check2 and check3 and check4:
        print(num, end=' ')