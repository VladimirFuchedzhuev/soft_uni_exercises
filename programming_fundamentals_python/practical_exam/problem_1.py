text = input()

command = input()

while not command == "Done":
    command = command.split()
    if command[0] == "Change":
        char = command[1]
        replacment = command[2]
        text = text.replace(char, replacment)
        print(text)
    elif command[0] == "Includes":
        other_string = command[1]
        if other_string in text:
            print(True)
        else:
            print(False)
    elif command[0] == "End":
        other_string = command[1]
        check = text[-len(other_string):]
        if other_string == check:
            print(True)
        else:
            print(False)
    elif command[0] == "Uppercase":
        text = text.upper()
        print(text)
    elif command[0] == "FindIndex":
        char = command[1]
        searched_index = text.find(char)
        print(searched_index)
    elif command[0] == "Cut":
        start_index = int(command[1])
        length = int(command[2])
        text = text[start_index: start_index + length]
        print(text)

    command = input()