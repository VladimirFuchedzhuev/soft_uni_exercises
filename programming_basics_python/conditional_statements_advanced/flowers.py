chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
total_flowers = chrysanthemums + roses + tulips
bouquet = 0

if season == "Spring":
    chrysanthemums_price = 2
    roses_price = 4.1
    tulips_price = 2.5
    bouquet = chrysanthemums * chrysanthemums_price + roses * roses_price + tulips * tulips_price
    if holiday == "Y":
        bouquet *= 1.15
        if tulips > 7:
            bouquet *= 0.95
    else:
        if tulips > 7:
            bouquet *= 0.95
elif season == "Summer":
    chrysanthemums_price = 2
    roses_price = 4.1
    tulips_price = 2.5
    bouquet = chrysanthemums * chrysanthemums_price + roses * roses_price + tulips * tulips_price
    if holiday == "Y":
        bouquet *= 1.15
elif season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15
    bouquet = chrysanthemums * chrysanthemums_price + roses * roses_price + tulips * tulips_price
    if holiday == "Y":
        bouquet *= 1.15
        if roses >= 10:
            bouquet *= 0.90
    else:
        if roses >= 10:
            bouquet *= 0.90
elif season == "Autumn":
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15
    bouquet = chrysanthemums * chrysanthemums_price + roses * roses_price + tulips * tulips_price
    if holiday == "Y":
        bouquet *= 1.15




if total_flowers < 20:
    bouquet += 2
    print(f"{bouquet:.2f}")
else:
    bouquet *= 0.80
    bouquet += 2
    print(f"{bouquet:.2f}")


