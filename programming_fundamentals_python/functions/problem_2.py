numbers = [int(num) for num in input().split()]
command = input().split()

while not command[0] == 'Finish':
    if command[0] == 'Add':
        numbers.append(int(command[1]))
    elif command[0] == 'Remove':
        if int(command[1]) in numbers:
            numbers.remove(int(command[1]))
    elif command[0] == 'Replace':
        x = numbers.index(int(command[1]))
        numbers.remove(int(command[1]))
        numbers.insert(x, int(command[2]))
    elif command[0] == 'Collapse':
        for num in numbers:
            if num < int(command[1]):
                numbers.remove(num)
    command = input().split()

print(' '.join([str(x) for x in numbers]))
