text, current_string, result, num = input(), "", "", ""

for index in range(len(text)):
    if not text[index].isdigit():
        current_string += text[index]
        continue

    if index != (len(text) - 1) and text[index + 1].isdigit():
        num += text[index]
        continue

    num += text[index]
    result += current_string.upper() * int(num)
    current_string = ""
    num = ""

unique_characters = set(result)
print(f"Unique symbols used: {len(unique_characters)}")
print(result)