import math

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = float(input())
gift_price = float(input())

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.5
cactus_price = 8

income = magnolias * magnolias_price + hyacinths * hyacinths_price + roses * roses_price + cactus * cactus_price
income_after_taxes = income * 0.95

if income_after_taxes >= gift_price:
    money_left = math.floor(income_after_taxes - gift_price)
    print(f"She is left with {money_left} leva.")
else:
    money_needed = math.ceil(gift_price - income_after_taxes)
    print(f"She will have to borrow {money_needed} leva.")

