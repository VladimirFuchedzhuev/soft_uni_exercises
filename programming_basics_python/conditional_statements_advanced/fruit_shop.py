fruit = input()
day = input()
quantity = float(input())
fruit_price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        fruit_price = quantity * 2.50
    elif fruit == "apple":
        fruit_price = quantity * 1.20
    elif fruit == "orange":
        fruit_price = quantity *  0.85
    elif fruit == "grapefruit":
        fruit_price = quantity * 1.45
    elif fruit == "kiwi":
        fruit_price = quantity * 2.70
    elif fruit == "pineapple":
        fruit_price = quantity * 5.50
    elif fruit == "grapes":
        fruit_price = quantity * 3.85
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        fruit_price = quantity * 2.70
    elif fruit == "apple":
        fruit_price = quantity * 1.25
    elif fruit == "orange":
        fruit_price = quantity * 0.90
    elif fruit == "grapefruit":
        fruit_price = quantity * 1.60
    elif fruit == "kiwi":
        fruit_price = quantity * 3.00
    elif fruit == "pineapple":
        fruit_price = quantity * 5.60
    elif fruit == "grapes":
        fruit_price = quantity * 4.20

if fruit_price:
    print(f"{fruit_price:.2f}")
else:
    print("error")