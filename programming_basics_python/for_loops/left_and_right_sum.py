n = int(input())

sum_left = 0
sum_right = 0

for num in range(0, n):
    number = int(input())
    sum_left += number
for num in range(0, n):
    number = int(input())
    sum_right += number

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    difference = abs(sum_left - sum_right)
    print(f"No, diff = {difference}")