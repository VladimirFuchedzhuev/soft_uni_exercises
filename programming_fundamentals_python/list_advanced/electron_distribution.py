number_of_electrons = int(input())
shell_number = 1
electrons = []

while number_of_electrons > 0:
    max_electrons = 2 * shell_number ** 2
    if max_electrons > number_of_electrons:
        electrons.append(number_of_electrons)
    else:
        electrons.append(max_electrons)
    number_of_electrons -= max_electrons
    shell_number += 1

print(electrons)