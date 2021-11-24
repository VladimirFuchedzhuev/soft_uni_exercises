password = input()
line = input()

while line != "Done":
    action = line.split(" ")
    command = action[0]
    if command == "TakeOdd":
        new_pass = ""
        for index in range(len(password)):
            if index % 2 == 1:
                new_pass += password[index]
        password = new_pass
        print(password)

    elif command == "Cut":
        index = int(action[1])
        length = int(action[2])
        substring = password[index:index + length]
        password = password.replace(substring, "", 1)
        print(password)

    elif command == "Substitute":
        substring = action[1]
        substitute = action[2]
        if substring not in password:
            print("Nothing to replace!")
        else:
            password = password.replace(substring, substitute)
            print(password)
    line = input()

print(f"Your password is: {password}")