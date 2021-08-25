budget = float(input())
season = input()
destination = ""
stay_in = ""
expenses = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        expenses = budget * 0.3
        stay_in = "Camp"
    elif season == "winter":
        expenses = budget * 0.7
        stay_in = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        expenses = budget * 0.4
        stay_in = "Camp"
    elif season == "winter":
        expenses = budget * 0.8
        stay_in = "Hotel"
elif budget > 1000:
    destination = "Europe"
    expenses = budget * 0.9
    stay_in = "Hotel"

print(f"Somewhere in {destination}")
print(f"{stay_in} - {expenses:.2f}")
