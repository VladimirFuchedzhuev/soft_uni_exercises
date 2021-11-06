command = input()
notes = [0] * 10

while not command == 'End':
    importance, note = command.split('-')
    importance = int(importance) -1
    notes.pop(importance)
    notes.insert(importance, note)

    command = input()

print([el for el in notes if not el == 0])