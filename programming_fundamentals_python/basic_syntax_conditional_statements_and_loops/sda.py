def duplicate_count(text):
    # Your code goes here
    text = list(text.lower())
    counter = 0
    for letter in text:
        if text.count(letter) > 1:
            counter += 1
            for char in text:
                if letter == char:
                    text.remove(char)
    return counter
print(duplicate_count("iKZgDN0UAXvUdZTQFN3k1vlDsffJdC14EEv4xOP8ChEQkVZe2ID6ExUXE7WmvUjelBSeN7mSlB"))