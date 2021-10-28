collection_of_items = input().split("|")
budget = int(input())
new_prices = []
profit = 0
needed_money = 150
updated_budget = 0

for item in collection_of_items:
    items = item.split("->")
    type_of_item = items[0]
    price_of_item = float(items[1])
    if type_of_item == "Clothes" and price_of_item <= 50.00 and budget >= price_of_item:
        budget -= price_of_item
        profit += price_of_item * 0.4
        new_prices.append(price_of_item * 1.4)
        updated_budget += price_of_item * 1.4
    elif type_of_item == "Shoes" and price_of_item <= 35.00 and budget >= price_of_item:
        budget -= price_of_item
        profit += price_of_item * 0.4
        new_prices.append(price_of_item * 1.4)
        updated_budget += price_of_item * 1.4
    elif type_of_item == "Accessories" and price_of_item <= 20.50 and budget >= price_of_item:
        budget -= price_of_item
        profit += price_of_item * 0.4
        new_prices.append(price_of_item * 1.4)
        updated_budget += price_of_item * 1.4

[print(f"{item:.2f}", end=" ") for item in new_prices]
print(f"\nProfit: {profit:.2f}")
if updated_budget + budget >= needed_money:
    print("Hello, France!")
else:
    print("Time to go.")
