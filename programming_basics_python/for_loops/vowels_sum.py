text = input()
sum = 0
for letter in text:
    points = 0
    if letter == "a":
        points = 1
        sum += points
    elif letter == "e":
        points = 2
        sum += points
    elif letter == "i":
        points = 3
        sum += points
    elif letter == "o":
        points = 4
        sum += points
    elif letter == "u":
        points = 5
        sum += points
print(sum)