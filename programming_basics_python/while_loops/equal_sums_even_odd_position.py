num1 = int(input())
num2 = int(input())

for num in range(num1, num2 + 1):
    num_to_str = str(num)
    even_sum = 0
    odd_sum = 0
    for index in range(0, len(num_to_str)):
        if index % 2 == 0:
            even_sum += int(num_to_str[index])
        else:
            odd_sum += int(num_to_str[index])
    if even_sum == odd_sum:
        print(num, end = " ")