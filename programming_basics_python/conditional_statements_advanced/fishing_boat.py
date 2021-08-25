budget = int(input())
season = input()
fishers = int(input())

boat_rent = 0
discount = 0

if season == "Spring":
    boat_rent = 3000
    if fishers <= 6:
        boat_rent *= 0.9
    elif 7<= fishers <= 11:
        boat_rent *= 0.85
    elif fishers >= 12:
        boat_rent *= 0.75
elif season == "Summer" or season  == "Autumn":
    boat_rent = 4200
    if fishers <= 6:
        boat_rent *= 0.9
    elif 7<= fishers <= 11:
        boat_rent *= 0.85
    elif fishers >= 12:
        boat_rent *= 0.75
elif season == "Winter":
    boat_rent = 2600
    if fishers <= 6:
        boat_rent *= 0.9
    elif 7<= fishers <= 11:
        boat_rent *= 0.85
    elif fishers >= 12:
        boat_rent *= 0.75
if fishers % 2 == 0:
    if season == "Spring" or season == "Winter" or season == "Summer":
        boat_rent *= 0.95
if budget >= boat_rent:
    final_price = budget - boat_rent
    print(f"Yes! You have {final_price:.2f} leva left.")
else:
    final_price = boat_rent - budget
    print(f"Not enough money! You need {final_price:.2f} leva.")
