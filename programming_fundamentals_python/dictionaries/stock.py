products = input().split()
searched_products = input().split()

stock = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index + 1])
    stock[key] = value

for el in searched_products:
    if el in stock:
        print(f'We have {stock[el]} of {el} left')
    else:
        print(f"Sorry, we don't have {el}")