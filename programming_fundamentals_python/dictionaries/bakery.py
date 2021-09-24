elements = input().split()
product = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = int(elements[index + 1])
    product[key] = value

print(product)
