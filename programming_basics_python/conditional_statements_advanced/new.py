budget = float(input())
category = input()
number_of_people = int(input())
tickets_price = 0
transport = 0

if 1 >= number_of_people <= 4:
    transport = budget * 0.75
elif 5 >= number_of_people <= 9:
    transport = budget * 0.6
elif 10 >= number_of_people <= 24:
    transport = budget * 0.5
elif 25 >= number_of_people <= 49:
    transport = budget * 0.4
elif number_of_people >= 50:
    transport = budget * 0.25

if category == "VIP":
    tickets_price = number_of_people * 499.99
elif category == "Normal":
    tickets_price = number_of_people * 249.99

total_expenses = transport + tickets_price
money_left = budget - total_expenses

if budget >= total_expenses:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva.")
