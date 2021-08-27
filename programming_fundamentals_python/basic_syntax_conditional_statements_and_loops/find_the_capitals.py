text = list(input())
new_text = []
for i in range(len(text)):
    if 65 <= ord(text[i]) <= 90:
        new_text.append(i)

print(new_text)