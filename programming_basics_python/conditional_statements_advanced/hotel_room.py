mount = input()
nights = int(input())
studio = 0
apartment = 0
if mount == "May" or mount == "October":
    studio = 50
    apartment = 65
    if nights > 14:
        studio *= 0.7
        apartment *= 0.9
    elif nights > 7:
        studio *= 0.95
elif mount == "June" or mount == "September":
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio *= 0.8
        apartment *= 0.9
elif mount == "July" or mount == "August":
    studio = 76
    apartment = 77
    if nights > 14:
        apartment *= 0.9
total_cost_apartment = nights * apartment
total_cost_studio = nights * studio
print(f"Apartment: {total_cost_apartment:.2f} lv.")
print(f"Studio: {total_cost_studio:.2f} lv.")


