dancers = int(input())
points = float(input())
season = (input())
place = (input())

award = points * dancers

if place == "Bulgaria":
    if season == "summer":
        award *= 0.95
    elif season == "winter":
        award *= 0.92
elif place == "Abroad":
    award *= 1.5
    if season == "summer":
        award *= 0.90
    elif season == "winter":
        award *= 0.85

donation = award * 0.75
money_left = award - donation
money_per_person = money_left / dancers

print(f"Charity - {donation:.2f}")
print(f"Money per dancer - {money_per_person:.2f}")
