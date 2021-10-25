numbers = int(input())
number_list = [1]

for i in range(numbers - 1):
    sum_ot_number_list = sum(number_list[-3:])
    number_list.append(sum_ot_number_list)

nums_to_str = [str(num) for num in number_list]
print(" ".join(nums_to_str))
