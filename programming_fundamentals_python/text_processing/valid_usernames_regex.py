import re

usernames = input().split(", ")

count = 0
pattern = r"[^A-Za-z0-9\-\_]"
for username in usernames:
    if 3 <= len(username) <= 16:
        match = re.findall(pattern, username)
        if match:
            continue
        else:
            print(username)
