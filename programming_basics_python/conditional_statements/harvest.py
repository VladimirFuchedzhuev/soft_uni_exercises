import math


yard = int(input())
grape = float(input())
z = int(input())
workers = int(input())


total_grape = yard * grape
total_wine = ((total_grape * 0.4) / 2.5)

if total_wine > z:
    wine_left = math.ceil(total_wine - z)
    litters_per_person = math.ceil(wine_left / workers)
    print(f"Good harvest this year! Total wine: {math.floor(total_wine)} liters.")
    print(f"{wine_left} liters left -> {litters_per_person} liters per person.")
else:
    wine_needed = math.floor(z - total_wine)
    print(f"It will be a tough winter! More {wine_needed} liters wine needed.")
