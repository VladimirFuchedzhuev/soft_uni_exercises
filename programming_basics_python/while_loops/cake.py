width = int(input())
length = int(input())
count_pieces = width * length

command = input()
while command != "STOP":
    count_taken_pieces = int(command)
    count_pieces -= count_taken_pieces
    if count_pieces < 0:
        print(f"No more cake left! You need {abs(count_pieces)} pieces more.")
        break
    command = input()
else:
    print(f"{count_pieces} pieces are left." )
