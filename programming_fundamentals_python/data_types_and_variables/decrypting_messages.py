key = int(input())
lines = int(input())

for n in range(0, lines):
    sym = ord(input()) + key
    character = chr(sym)
    print(character, end= "")