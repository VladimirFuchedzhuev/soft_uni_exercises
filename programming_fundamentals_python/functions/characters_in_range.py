def in_betwen(char_1, char_2):
    single_line = ""
    for i in range(ord(char_1) + 1, ord(char_2)):
        single_line += f" {chr(i)}"
    return single_line

char_1 = input()
char_2 = input()
print(in_betwen(char_1, char_2))