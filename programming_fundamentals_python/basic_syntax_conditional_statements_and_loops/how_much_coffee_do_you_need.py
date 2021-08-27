command = input()
counter = 0

while not command == "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        counter += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        counter += 2
    command = input()

if counter > 5:
    print("You need extra sleep")
else:
    print(counter)