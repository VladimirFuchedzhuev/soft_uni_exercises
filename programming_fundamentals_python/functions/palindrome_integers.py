def palindrome(list_of_ints):
    is_palindrome = 0
    for num in list_of_ints.split(", "):
        if str(num[::]) == str(num[::-1]):
            is_palindrome = True
            print(is_palindrome)
        else:
            is_palindrome = False
            print(is_palindrome)
        is_palindrome = 0
numbers = input()
palindrome(numbers)
