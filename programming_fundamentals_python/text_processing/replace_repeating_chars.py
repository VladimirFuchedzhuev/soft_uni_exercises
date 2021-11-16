text = input()
count = 0
while count < len(text) - 1:
    if text[count] == text[count + 1]:
        element_to_replace = f"{text[count]}{text[count + 1]}"
        text = text.replace(element_to_replace, text[count])
        count = 0
    else:
        count += 1
print(text)