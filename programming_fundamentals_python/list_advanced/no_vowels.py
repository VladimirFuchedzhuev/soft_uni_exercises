vowels = ['a', 'o', 'u', 'e', 'i']
text = input()
print("".join([el for el in text if el.lower() not in vowels]))
