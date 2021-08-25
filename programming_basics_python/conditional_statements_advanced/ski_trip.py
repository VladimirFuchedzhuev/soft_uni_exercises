days = int(input())
room_type = input()
feedback = input()
nights = days - 1
discount = 0

room_for_one_price = 18.00
apartment_price = 25.00
president_apartment_price = 35.00

if days > 15:
    if room_type == "room for one person":
        discount = room_for_one_price
    elif room_type == "apartment":
        discount = apartment_price * 0.5
    elif room_type == "president apartment":
        discount = president_apartment_price * 0.8
elif days >= 10:
    if room_type == "room for one person":
        discount = room_for_one_price
    elif room_type == "apartment":
        discount = apartment_price * 0.65
    elif room_type == "president apartment":
        discount = president_apartment_price * 0.85
elif days > 0:
    if room_type == "room for one person":
        discount = room_for_one_price
    elif room_type == "apartment":
        discount = apartment_price * 0.7
    elif room_type == "president apartment":
        discount = president_apartment_price * 0.9

if feedback == "positive":
    discount *= 1.25
else:
    discount *= 0.9

final_price = nights * discount
print(f"{final_price:.2f}")
