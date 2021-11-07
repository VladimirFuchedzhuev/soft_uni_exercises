words_input = input().split()
even_length_words = [el for el in words_input if len(el) % 2 == 0]
print("\n".join(even_length_words))