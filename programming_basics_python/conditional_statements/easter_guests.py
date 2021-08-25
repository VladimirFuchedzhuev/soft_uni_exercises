from math import ceil


guests = int(input())
budget = int(input())

easter_bread_price = 4
egg_price = 0.45
easter_bread = ceil(guests / 3)
easter_eggs = ceil(guests * 2)

total_breads = easter_bread * easter_bread_price
total_eggs = easter_eggs * egg_price
total_expenses = total_eggs + total_breads

if total_expenses <= budget:
    money_left = budget - total_expenses
    print(f"Lyubo bought {easter_bread} Easter bread and {easter_eggs} eggs.")
    print(f"He has {money_left:.2f} lv. left.")
else:
    money_needed = total_expenses - budget
    print("Lyubo doesn't have enough money.")
    print(f"He needs {money_needed:.2f} lv. more.")


