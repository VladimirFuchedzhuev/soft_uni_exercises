vacation = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
truck_toys = int(input())

sum1 = puzzles * 2.6 + dolls * 3 + teddy_bears * 4.1 + minions * 8.2 + truck_toys * 2
toys = puzzles + dolls + teddy_bears + minions + truck_toys
if toys >= 50:
    sum1 *= 0.75
sum1 *= 0.9
income = abs(sum1 - vacation)
if sum1 >= vacation:
    print(f"Yes! {income:.2f} lv left.")
else:
    print(f"Not enough money! {income:.2f} lv needed.")
