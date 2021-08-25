n = int(input())

odd_sum = 0
even_sum = 0

for num in range(0, n +1):
    number = int(input())
    if num % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum  == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    difference = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {difference}")

