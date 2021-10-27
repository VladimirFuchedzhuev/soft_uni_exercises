n = int(input())
word = input()
new_list = []

for _ in range(n):
    new_word = input()
    new_list.append(new_word)
print(new_list)

# for i in new_list:
# if not word in i:
# new_list.remove(i)
# print(new_list)
print([i for i in new_list if word in i])
