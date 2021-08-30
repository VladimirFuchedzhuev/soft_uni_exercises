divisor = int(input())
bound = int(input())

for num in range(bound, -1, -1):
    if num % divisor == 0:
        divisor = num
        break
print(divisor)