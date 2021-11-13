import re
command = input()

pattern = r"\%(?P<Name>[A-Z][a-z]+)\%[^\|\$\%\.]*?\<(?P<Product>\w+)\>[^\|\$\%\.]*?\|(?P<Qty>[0-9]+)\|[\w\-]*?(?P<Price>\d+(\.\d+)?)\$"
total_price = 0
product_price = 0
while not command == "end of shift":
    valid_orders = re.match(pattern, command)
    if valid_orders:
        name = valid_orders.group("Name")
        product = valid_orders.group("Product")
        qty = int(valid_orders.group("Qty"))
        price = float(valid_orders.group("Price"))

        product_price = qty * price
        total_price += product_price
        print(f"{name}: {product} - {product_price:.2f}")

    command = input()
print(f"Total income: {total_price:.2f}")
