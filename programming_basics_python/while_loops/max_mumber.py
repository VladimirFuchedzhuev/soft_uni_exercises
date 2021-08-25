import sys

command = input()
max_number = -sys.maxsize

while command != "Stop":
    new_number = int(command)
    if max_number < new_number:
        max_number = new_number
    command = input()
print(max_number)
