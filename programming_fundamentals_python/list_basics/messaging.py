numbers = input().split(" ")
text = [x for x in input()]
message = []
for num in numbers:
    index = sum(int(el) for el in num)
    if len(text) < index + 1:
        index = index - len(text)
    message.append(text[index])
    text.pop(index)
print("".join(message))