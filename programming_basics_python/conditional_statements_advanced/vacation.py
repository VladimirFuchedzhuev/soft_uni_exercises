budget = float(input())
season = input()
location = ""
place = ""
location_price = 0

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        location_price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        location_price = budget * 0.45
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        location_price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        location_price = budget * 0.60
elif budget > 500:
    place = "Hotel"
    if season == "Summer":
        location = "Alaska"
        location_price = budget * 0.9
    elif season == "Winter":
        location = "Morocco"
        location_price = budget * 0.9

print(f"{location} - {place} - {location_price:.2f}")