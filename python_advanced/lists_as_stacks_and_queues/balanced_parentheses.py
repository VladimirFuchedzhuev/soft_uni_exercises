parentheses = input()
is_balanced = True
parentheses_check = {
    '{': '}',
    '[': ']',
    '(': ')'
}
opening = []

for el in parentheses:
    if el in "{[(":
        opening.append(el)
    elif el in "}])":
        if not opening:
            is_balanced = False
            break
        last_el = opening.pop()
        if not parentheses_check[last_el] == el:
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")