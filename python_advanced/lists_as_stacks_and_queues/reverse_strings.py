word = list(input())

stack = []

while len(word) > 0:
    stack.append(word.pop())

print(f"{''.join(stack)}")