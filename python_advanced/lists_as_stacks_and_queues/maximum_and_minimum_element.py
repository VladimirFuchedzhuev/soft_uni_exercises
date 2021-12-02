n = int(input())

stack = []
for _ in range(n):
    line = input().split()
    if line[0] == '1':
        stack.append(line[1])
    elif line[0] == '2':
        if stack:
            stack.pop()
    elif line[0] == '3':
        if stack:
            print(max(stack))
    elif line[0] == '4':
        if stack:
            print(min(stack))
result = []
while stack:
    result.append(stack.pop())

print(', '.join(result))