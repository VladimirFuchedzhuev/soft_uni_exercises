text = input()
data = input()

while not data == "Reveal":
    data = data.split(":|:")
    if data[0] == "InsertSpace":
        index = int(data[1])
        first_part = text[:index]
        last_part = text[index:]
        text = f"{first_part} {last_part}"
        print(text)
    elif data[0] == "Reverse":
        substring = data[1]
        if substring in text:
            text = text.replace(substring, "", 1)
            substring = substring[::-1]
            text += substring
            print(text)
        else:
            print("error")
    elif data[0] == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        text = text.replace(substring, replacement)
        print(text)
    data = input()

print(f"You have a new text message: {text}")