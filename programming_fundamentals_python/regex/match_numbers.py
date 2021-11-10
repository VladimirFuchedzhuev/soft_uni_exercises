import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()

valid_nums = [nums.group() for nums in re.finditer(pattern, text)]
print(*valid_nums)