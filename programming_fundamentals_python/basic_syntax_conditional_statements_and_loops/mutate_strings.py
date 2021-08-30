word_1 = input()
word_2 = input()
new_word = word_1

for element in range(len(word_1)):
    left_part = word_2[:element + 1]
    right_part = word_1[element +1:]
    current_word = left_part + right_part
    if current_word == new_word:
        continue
    print(current_word)
    new_word = current_word

