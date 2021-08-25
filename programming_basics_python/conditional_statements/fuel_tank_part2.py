fuel_type = input()
fuel_quantity = float(input())
club_cart = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93

cart_discount_gasoline = gasoline - 0.18
cart_discount_diesel = diesel - 0.12
cart_discount_gas = gas - 0.08

# ако има карта за отстъпка получава 18 ст за бензин, 12 ст за дизел и 8 ст за газ
# какъв тип гориво зарежда
# каква е цената за горивото
# при < 20литра няма отстъпка
# между 20 и 25 литра отстъпка 8%
# над 25 литра отстъпка 10%

if club_cart == "Yes" and fuel_type == "Gasoline" and fuel_quantity > 25:
    quantity_discount = (fuel_quantity * cart_discount_gasoline) * 0.9
    print(f"{quantity_discount:.2f} lv.")
elif club_cart == "Yes" and fuel_type == "Diesel" and fuel_quantity > 25:
    quantity_discount = (fuel_quantity * cart_discount_diesel) * 0.9
    print(f"{quantity_discount:.2f} lv.")
elif club_cart == "Yes" and fuel_type == "Gas" and fuel_quantity > 25:
    quantity_discount = (fuel_quantity * cart_discount_gas) * 0.9
    print(f"{quantity_discount:.2f} lv.")
elif club_cart == "Yes" and fuel_type == "Gasoline" and fuel_quantity >= 20:
    quantity_discount = (fuel_quantity * cart_discount_gasoline) * 0.92
    print(f"{quantity_discount:.2f} lv.")
elif club_cart == "Yes" and fuel_type == "Diesel" and fuel_quantity >= 20:
    quantity_discount = (fuel_quantity * cart_discount_diesel) * 0.92
    print(f"{quantity_discount:.2f} lv.")
elif club_cart == "Yes" and fuel_type == "Gas" and fuel_quantity >= 20:
    quantity_discount = (fuel_quantity * cart_discount_gas) * 0.92
    print(f"{quantity_discount:.2f} lv.")
elif club_cart == "Yes" and fuel_type == "Gasoline":
    cart_discount = fuel_quantity * cart_discount_gasoline
    print(f"{cart_discount:.2f} lv.")
elif club_cart == "Yes" and fuel_type == "Diesel":
    cart_discount = fuel_quantity * cart_discount_diesel
    print(f"{cart_discount:.2f} lv.")
elif club_cart == "Yes" and fuel_type == "Gas":
    cart_discount = fuel_quantity * cart_discount_gas
    print(f"{cart_discount:.2f} lv.")
#
elif fuel_type == "Gasoline" and fuel_quantity > 25:
    quantity_discount = fuel_quantity * gasoline * 0.9
    print(f"{quantity_discount:.2f} lv.")
elif fuel_type == "Diesel" and fuel_quantity > 25:
    quantity_discount = fuel_quantity * diesel * 0.9
    print(f"{quantity_discount:.2f} lv.")
elif fuel_type == "Gas" and fuel_quantity > 25:
    quantity_discount = fuel_quantity * gas * 0.9
    print(f"{quantity_discount:.2f} lv.")
elif fuel_type == "Gasoline" and fuel_quantity >= 20:
    quantity_discount = fuel_quantity * gasoline * 0.92
    print(f"{quantity_discount:.2f} lv.")
elif fuel_type == "Diesel" and fuel_quantity >= 20:
    quantity_discount = fuel_quantity * diesel * 0.92
    print(f"{quantity_discount:.2f} lv.")
elif fuel_type == "Gas" and fuel_quantity >= 20:
    quantity_discount = fuel_quantity * gas * 0.92
    print(f"{quantity_discount:.2f} lv.")
elif fuel_type == "Gasoline":
    cart_discount = fuel_quantity * gasoline
    print(f"{cart_discount:.2f} lv.")
elif fuel_type == "Diesel":
    cart_discount = fuel_quantity * diesel
    print(f"{cart_discount:.2f} lv.")
elif fuel_type == "Gas":
    cart_discount = fuel_quantity * gas
    print(f"{cart_discount:.2f} lv.")
