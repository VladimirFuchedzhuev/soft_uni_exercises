inherited_money = float(input())
year_to_live = int(input())
age = 18
needed_money = 0

for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        inherited_money -= 12000
    else:
        age += 1
        inherited_money -= 12000 + 50 * age

money_left = abs(inherited_money - needed_money)
if inherited_money >= needed_money:
        print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {money_left:.2f} dollars to survive.")