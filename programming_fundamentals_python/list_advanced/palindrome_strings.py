string = input().split()
palindrome = input()
palindrome_list = [word for word in string if word == word[::-1]]

print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(palindrome)} times')

