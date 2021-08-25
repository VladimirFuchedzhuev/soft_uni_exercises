start = int(input())
end = int(input())
magic_num = int(input())
combinations = 0
is_found = False
for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
        combinations += 1
        if num1 + num2 == magic_num:
            print(f"Combination N:{combinations} ({num1} + {num2} = {magic_num})")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f"{combinations} combinations - neither equals {magic_num}")