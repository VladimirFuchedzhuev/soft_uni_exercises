num1 = int(input())
num2 = int(input())
operator = input()
result = 0
odd_or_even = ""

if operator == "+":
    result = num1 + num2
    if result % 2 == 0:
        odd_or_even = "even"
        print(f"{num1} {operator} {num2} = {result} - {odd_or_even}")
    else:
        odd_or_even = "odd"
        print(f"{num1} {operator} {num2} = {result} - {odd_or_even}")
elif operator == "-":
    result = num1 - num2
    if result % 2 == 0:
        odd_or_even = "even"
        print(f"{num1} {operator} {num2} = {result} - {odd_or_even}")
    else:
        odd_or_even = "odd"
        print(f"{num1} {operator} {num2} = {result} - {odd_or_even}")
elif operator == "*":
    result = num1 * num2
    if result % 2 == 0:
        odd_or_even = "even"
        print(f"{num1} {operator} {num2} = {result} - {odd_or_even}")
    else:
        odd_or_even = "odd"
        print(f"{num1} {operator} {num2} = {result} - {odd_or_even}")
elif operator == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
elif operator == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")

