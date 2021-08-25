guests = int(input())
price_per_guest = float(input())
budget = float(input())
cake = budget * 0.1

if guests > 20:
    price_per_guest *= 0.75
elif guests > 15:
    price_per_guest *= 0.8
elif guests >= 10:
    price_per_guest *= 0.85
else:
    price_per_guest = price_per_guest
total_expenses = guests * price_per_guest + cake

if total_expenses < budget:
    budget -= total_expenses
    print(f"It is party time! {budget:.2f} leva left.")
else:
    total_expenses -= budget
    print(f"No party! {total_expenses:.2f} leva needed.")
