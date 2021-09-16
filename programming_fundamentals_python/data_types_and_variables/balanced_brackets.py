n = int(input())
opening_brackets = 0
closing_brackets = 0
is_balanced = True

for i in range(n):
    text = input()
    if text == "(":
        opening_brackets += 1
    elif text == ")":
        closing_brackets += 1
    if closing_brackets > opening_brackets:
        is_balanced = False
        break
    if opening_brackets - 1 > closing_brackets:
        is_balanced = False
        break
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
