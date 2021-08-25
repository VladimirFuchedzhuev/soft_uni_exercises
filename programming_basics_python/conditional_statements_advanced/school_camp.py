season = input()
group_type = input()
students = int(input())
nights = int(input())
nights_price = 0
sport = ""


if season == "Winter":
    if group_type == "girls":
        nights_price = 9.6
        sport = "Gymnastics"
    elif group_type == "boys":
        nights_price = 9.6
        sport = "Judo"
    elif group_type == "mixed":
        nights_price = 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "girls":
        nights_price = 7.2
        sport = "Athletics"
    elif group_type == "boys":
        nights_price = 7.2
        sport = "Tennis"
    elif group_type == "mixed":
        nights_price = 9.5
        sport = "Cycling"
elif season == "Summer":
    if group_type == "girls":
        nights_price = 15
        sport = "Volleyball"
    elif group_type == "boys":
        nights_price = 15
        sport = "Football"
    elif group_type == "mixed":
        nights_price = 20
        sport = "Swimming"

total_expenses = nights * nights_price * students

if students >= 50:
    total_expenses *= 0.5
elif 20 <= students < 50:
    total_expenses *= 0.85
elif 10 <= students < 20:
    total_expenses *= 0.95

print(f"{sport} {total_expenses:.2f} lv.")




