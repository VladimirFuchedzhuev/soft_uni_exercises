from collections import deque

litters = int(input())
name = input()

queue = deque()

while not name == "Start":
    queue.append(name)
    name = input()

command = input()

while not command == "End":
    if command.startswith("refill"):
        litters += int(command.split()[-1])
    else:
        name = queue.popleft()
        if litters >= int(command):
            litters -= int(command)
            print(f"{name} got water")
        else:
            print(f"{name} must wait")

    command = input()

print(f"{litters} liters left")
