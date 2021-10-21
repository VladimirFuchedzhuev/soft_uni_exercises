initial_list = [x for x in input().split('!')]
command = input()


while not command == "Go Shopping!":
    command = command.split()
    condition = command[0]
    item = command[1]

    if condition == 'Urgent':
        if item not in initial_list:
            initial_list.insert(0, item)
    elif condition == 'Unnecessary':
        if item in initial_list:
            initial_list.remove(item)
    elif condition == 'Correct':
        for element in range(len(initial_list)):
            if initial_list[element] == item:
                initial_list[element] = command[2]
    elif condition == 'Rearrange':
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

    command = input()

print(', '.join(initial_list))