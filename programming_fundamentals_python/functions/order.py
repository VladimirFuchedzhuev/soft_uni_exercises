def bill(product, quantity):
    if product == "water":
        return quantity
    elif product == "coke":
        return quantity * 1.4
    elif product == "coffee":
        return quantity * 1.5
    elif product == "snacks":
        return quantity * 2


type_product = input()
product_quantity = int(input())

total = bill(type_product, product_quantity)
print(f"{total:.2f}")
