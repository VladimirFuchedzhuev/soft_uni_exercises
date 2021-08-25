joinery_count = int(input())
type_joinery = input()
delivery = input()
price = 0

if type_joinery == "90X130":
    price = 110
    if joinery_count > 60:
        price *= .92
    elif joinery_count > 30:
        price *= 0.95
elif type_joinery == "100X150":
    price = 140
    if joinery_count > 80:
        price *= 0.90
    elif joinery_count > 40:
        price *= 0.94
elif type_joinery == "130X180":
    price = 190
    if joinery_count > 50:
        price *= 0.88
    elif joinery_count > 20:
        price *= 0.93
elif type_joinery == "200X300":
    price = 250
    if joinery_count > 50:
        price *= 0.86
    elif joinery_count > 25:
        price *= 0.91

final_net_price = price * joinery_count
if delivery == "With delivery":
    final_net_price += 60
    if joinery_count > 99:
        final_net_price *= 0.96
elif delivery == "Without delivery":
    if joinery_count > 99:
        final_net_price *= 0.96

if joinery_count < 10:
    print("Invalid order")
else:
    print(f"{final_net_price:.2f} BGN")




