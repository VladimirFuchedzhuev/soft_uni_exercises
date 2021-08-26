budget = float(input())
flour_price = float(input())

eggs_pack = flour_price * 0.75
liter_milk = flour_price * 1.25

cozonac = eggs_pack + flour_price + liter_milk * 0.25
number_of_cozonacs = 0
colored_eggs = 0

while budget - cozonac >= 0:
    budget -= cozonac
    number_of_cozonacs += 1
    colored_eggs += 3
    if number_of_cozonacs % 3 == 0:
        colored_eggs -= number_of_cozonacs - 2

print(f"You made {number_of_cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")