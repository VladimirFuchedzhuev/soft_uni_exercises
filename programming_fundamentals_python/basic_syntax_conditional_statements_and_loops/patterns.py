number = int(input())
counter = "*"
for a in range(number + 1):
    for b in range(a):
        print("*", end="")
    print("")
for a in range(number - 1, -1, -1):
    for b in range(a -1, -1, -1):
        print("*", end="")
    print("")