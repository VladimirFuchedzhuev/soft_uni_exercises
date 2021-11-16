path = input().split("\\")

list_text = []
for text in path:
    for ch in text:
        if ch == ".":
            fine_name_extract = text
            list_text = fine_name_extract.split(".")
print(f"File name: {list_text[0]}")
print(f"File extension: {list_text[1]}")