lili_age = int(input())
laundry_machine = float(input())
toys_price = int(input())


even_birthday = 0
odd_birthday = 0
birthday_income = 0

for birthday in range(1, lili_age + 1):
    if birthday % 2 == 0:
        even_birthday += 10
        birthday_income += even_birthday
        birthday_income -= 1
    else:
        odd_birthday += 1
toys_income = toys_price * odd_birthday
total_income = toys_income + birthday_income
change = abs(total_income - laundry_machine)
if total_income >= laundry_machine:
    print(f"Yes! {change:.2f}")
else:
    print(f"No! {change:.2f}")
