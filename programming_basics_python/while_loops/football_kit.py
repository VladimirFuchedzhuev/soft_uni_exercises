t_shirt_price = float(input("pricetshirt"))
spent_money_for_ball = float(input("khghoih"))

shorts = t_shirt_price * 0.75
socks = shorts * 0.2
football_shoes = (t_shirt_price + shorts) * 2
total_expenses = t_shirt_price + shorts + socks + football_shoes
expenses_after_discount = total_expenses * 0.85

if expenses_after_discount >= spent_money_for_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {expenses_after_discount:.2f} lv.")
else:
    needed_money = spent_money_for_ball - expenses_after_discount
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_money:.2f} lv. more.")
