words = input().split()
dictionary = {}

for word in words:
    for letter in word:
        if letter not in dictionary:
            dictionary[letter] = 0
        dictionary[letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")