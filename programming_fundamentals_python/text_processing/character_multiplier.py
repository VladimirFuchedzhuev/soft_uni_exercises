word_1, word_2 = input().split()

sum = 0

for char_1 in word_1:
    for char_2 in word_2:
        if char_1 and  char_2:
            sum += ord(char_1) * ord(char_2)

