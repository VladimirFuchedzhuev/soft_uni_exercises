text = input()
encrypted_version = ""
for symbol in text:
    new_symbol = chr(ord(symbol) + 3)
    encrypted_version += new_symbol
print(encrypted_version)