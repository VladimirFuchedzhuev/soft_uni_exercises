def calculate(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return int(num1 / num2)
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2


operator_1 = input()
number_1 = int(input())
number_2 = int(input())

print(calculate(operator_1, number_1, number_2))
