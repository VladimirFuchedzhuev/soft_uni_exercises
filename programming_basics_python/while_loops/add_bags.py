luggage_price_over_twenty = float(input())
luggage_kg = float(input())
days_to_travel = int(input())
count_of_luggage = int(input())
luggage_price = 0
if luggage_kg < 10:
    luggage_price = luggage_price_over_twenty * 0.2
    if days_to_travel > 30:
        luggage_price *= 1.1
    elif days_to_travel >= 7:
        luggage_price *= 1.15
    else:
        luggage_price *= 1.4
elif 10 <= luggage_kg <= 20:
    luggage_price = luggage_price_over_twenty * 0.5
    if days_to_travel > 30:
        luggage_price *= 1.1
    elif days_to_travel >= 7:
        luggage_price *= 1.15
    else:
        luggage_price *= 1.4
elif luggage_kg > 20:
    luggage_price = luggage_price_over_twenty
    if days_to_travel > 30:
        luggage_price *= 1.1
    elif days_to_travel >= 7:
        luggage_price *= 1.15
    else:
        luggage_price *= 1.4
total_luggage_price = luggage_price * count_of_luggage
print(f" The total price of bags is: {total_luggage_price:.2f} lv. ")

