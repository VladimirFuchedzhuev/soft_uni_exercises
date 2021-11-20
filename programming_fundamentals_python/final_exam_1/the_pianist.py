number = int(input())

pieces = {}

for i in range(number):
    play, composer, key = input().split("|")
    if composer not in pieces:
        pieces[play] = {'composer': [composer], 'key': [key]}
    else:
        pieces[play]["key"].append(key)

while True:
    command = input()
    if command == 'Stop':
        break
    data = command.split("|")
    play = data[1]
    action = data[0]
    if action == "Add":
        composer = data[2]
        key = data[3]
        if play not in pieces:
            pieces[play] = {'composer': [composer], 'key': [key]}
            print(f"{play} by {composer} in {key} added to the collection!")
        else:
            print(f"{play} is already in the collection!")
    elif action == "Remove":
        if play in pieces:
            pieces.pop(play)
            print(f"Successfully removed {play}!")
        else:
            print(f"Invalid operation! {play} does not exist in the collection.")
    elif action == "ChangeKey":
        if play in pieces:
            new_key = data[2]
            pieces[play]['key'] = new_key
            print(f"Changed the key of {play} to {new_key}!")
        else:
            print(f"Invalid operation! {play} does not exist in the collection.")
sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1]['composer']))

for key, value in sorted_pieces:
    print(f"{key} -> Composer: {''.join(value['composer'])}, Key: {''.join(value['key'])}")