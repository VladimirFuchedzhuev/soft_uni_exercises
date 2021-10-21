received_cards = input().split(':')
command = input().split()
new_deck = []


while not command[0] == 'Ready':
    if command[0] == 'Add':
        if command[1] not in received_cards:
            print('Card not found.')
        else:
            new_deck.append(command[1])
    elif command[0] == 'Insert':
        if command[1] not in received_cards or int(command[2]) > len(received_cards):
            print('Error!')
        else:
            new_deck.insert(int(command[2]), command[1])
    elif command[0] == 'Remove':
        if command[1] not in new_deck:
            print('Card not found.')
        else:
            new_deck.remove(command[1])
    elif command[0] == 'Swap':
        x = new_deck.index(command[1])
        y = new_deck.index(command[2])
        new_deck[x], new_deck[y] = new_deck[y], new_deck[x]
    elif ' '.join(command) == 'Shuffle deck':
        new_deck.reverse()

    command = input().split()

print(' '.join(new_deck))
