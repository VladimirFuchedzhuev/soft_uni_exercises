import string

lower_letter = string.ascii_lowercase
upper_letter = string.ascii_uppercase

total_sum = 0
str_num = ""
sum_word = 0
text = [t.strip() for t in input().split()]

for word in text:
    for i in word:
        if i.isdigit():
            str_num += i
    for i in range(len(word)):

        if i == 0:
            if word[i].isupper():
                position = upper_letter.find(word[i]) + 1
                sum_word += int(str_num) / position
            elif word[i].islower():
                position = lower_letter.find(word[i]) + 1
                sum_word += int(str_num) * position
        else:
            if word[i].isupper():
                position = upper_letter.find(word[i]) + 1
                sum_word -= position
            elif word[i].islower():
                position = lower_letter.find(word[i]) + 1
                sum_word += position

    total_sum += sum_word
    sum_word = 0
    str_num = ""
print(f"{total_sum:.2f}")