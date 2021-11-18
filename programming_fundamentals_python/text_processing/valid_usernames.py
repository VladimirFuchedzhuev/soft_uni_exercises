usernames, valid_usernames = input().split(", "), []
valid_symbols = ["_", "-"]

for username in usernames:
    if len(username) not in range(3, 17):
        continue

    is_username_valid = True
    for char in username:
        if not char.isdigit() and not char.isalpha() and char not in valid_symbols:
            is_username_valid = False
            break

    if is_username_valid:
        valid_usernames.append(username)

print('\n'.join(valid_usernames))