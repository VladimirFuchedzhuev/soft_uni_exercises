import re

n_lines = int(input())

pattern = r"^(\$|\%)(?P<Tag>[A-Z][a-z]{3,})(\1)\:\s(?P<FirstNum>\[\d+\])\|(?P<SecondNum>\[\d+\])\|(?P<ThirdNum>\[\d+\])\|$"

for line in range(n_lines):
    text = input()
    message = re.match(pattern, text)
    if message:
        tag = message.group('Tag')
        first_num = message.group('FirstNum')
        num_1 = [el for el in first_num if el.isdigit()]
        second_num = message.group('SecondNum')
        num_2 = [el for el in second_num if el.isdigit()]
        third_num = message.group('ThirdNum')
        num_3 = [el for el in third_num if el.isdigit()]
        decrypted_message = chr(int(''.join(num_1))) + chr(int(''.join(num_2))) + chr(int(''.join(num_3)))
        print(f"{tag}: {decrypted_message}")
    else:
        print("Valid message not found!")