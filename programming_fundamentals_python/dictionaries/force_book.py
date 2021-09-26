data = input()

book = {}

while not data == "Lumpawaroo":
    if " | " in data:
        command = data.split(" | ")
        force_side = command[0]
        force_user = command[1]
        if force_side not in book:
            is_in = False
            for side, user in book.items():
                if force_user in user:
                    is_in = True
                    break
            if not is_in:
                book[force_side] = []
                book[force_side].append(force_user)
        elif force_user not in book[force_side]:
            book[force_side].append(force_user)
    else:
        command = data.split(" -> ")
        force_side = command[1]
        force_user = command[0]
        for key, value in book.items():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in book:
            book[force_side] = []
        book[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')
    data = input()

for (side, users) in sorted(book.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    if len(users) > 0:
        print(f'Side: {side}, Members: {len(users)}')

        for user in sorted(users):
            print(f'! {user}')