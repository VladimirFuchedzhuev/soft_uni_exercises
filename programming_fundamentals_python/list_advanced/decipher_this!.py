words = input().split()
deciphered_words = []
for word in words:
    digit = ''
    for letter in word:
        if letter.isdigit():
            digit += letter
    first_letter = chr(int(digit))
    current_word = first_letter + word[len(digit):]
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    print(f"{''.join(current_word)} ", end='')