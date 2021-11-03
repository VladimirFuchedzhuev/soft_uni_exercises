numbers_input = [int(num) for num in input().split(', ')]

step = 10

while numbers_input:
    group_list = [num for num in numbers_input if num <= step]
    for num in group_list:
        numbers_input.remove(num)
    print(f"Group of {step}'s: {group_list}")

    step += 10

