data = input()

stack = []

for index in range(len(data)):
    if data[index] == "(":
        stack.append(index)
    elif data[index] == ")":
        start_index = stack.pop()
        print(data[start_index: index + 1])
