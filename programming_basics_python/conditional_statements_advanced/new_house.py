type_flower = input()
count_flowers = int(input())
budget = int(input())

final_price = 0

if type_flower == "Roses":
    final_price = count_flowers * 5
    if count_flowers > 80:
        final_price *= 0.9
elif type_flower == "Dahlias":
    final_price = count_flowers * 3.8
    if count_flowers > 90:
        final_price *= 0.85
elif type_flower == "Tulips":
    final_price = count_flowers * 2.8
    if count_flowers > 80:
        final_price *= 0.85
elif type_flower == "Narcissus":
    final_price = count_flowers * 3
    if count_flowers < 120:
        final_price *= 1.15
elif type_flower == "Gladiolus":
    final_price = count_flowers * 2.5
    if count_flowers < 80:
        final_price *= 1.2

if budget >= final_price:
    money_left = budget - final_price
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {money_left:.2f} leva left.")
else:
    money_left = final_price - budget
    print(f"Not enough money, you need {money_left:.2f} leva more.")
