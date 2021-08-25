import sys
num = int(input())
biggest_num = -sys.maxsize
sum = 0
for i in range(1, num + 1):
    new_num = int(input())
    sum += new_num
    if new_num > biggest_num:
        biggest_num = new_num

sum_numbers = sum - biggest_num
if sum_numbers == biggest_num:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    difference = abs(sum_numbers - biggest_num)
    print("No")
    print(f"Diff = {difference}")