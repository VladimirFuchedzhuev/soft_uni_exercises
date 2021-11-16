text = input()
power = 0

i = 0
while i < len(text):
    ch = text[i]

    if ch == ">":
        power += int(text[i + 1])
    elif power > 0:
        first_part = text[:i]
        second_part = text[i + 1:]
        text = first_part + second_part
        i -= 1
        power -= 1
    i += 1

print(text)