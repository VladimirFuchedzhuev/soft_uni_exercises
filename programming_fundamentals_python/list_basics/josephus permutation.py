string = input().split()
k = int(input())
new_string = []
counter = 0
index = 0

while len(string) > 0:
    counter += 1
    if counter % k == 0:
        new_string.append(string.pop(index))
    else:
        index += 1
    if index >= len(string):
        index = 0

print(str(new_string).replace(' ', '').replace("'", ""))