factor = int(input())
count = int(input())

new_list = [el for el in range(1, count * factor + 1) if el % factor == 0]

print(new_list)