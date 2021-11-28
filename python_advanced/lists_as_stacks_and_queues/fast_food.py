from collections import deque

quantity_food = int(input())
orders = deque(int(num) for num in input().split())

print(max(orders))

while orders:
    order_check = orders[0]
    if order_check > quantity_food:
        break
    else:
        quantity_food -= order_check
        orders.popleft()

if orders:
    print(f"Orders left: {' '.join(str(num) for num in orders)}")
else:
    print('Orders complete')
