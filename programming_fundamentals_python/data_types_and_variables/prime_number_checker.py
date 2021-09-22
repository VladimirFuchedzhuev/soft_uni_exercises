number = int(input())

checker = 0
prime = True

for num in range(1, number + 1):
    if number % num == 0:
        checker += 1
    if checker > 2:
        prime = False
        break

if prime:
    print("True")
else:
    print("False")