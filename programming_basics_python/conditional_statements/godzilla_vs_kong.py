budget = float(input())
actors = int(input())
clothes_per_actor = float(input())

decors = budget * 0.1
clothes = actors * clothes_per_actor
if actors >= 150:
    clothes *= 0.9
expenses = clothes + decors


if budget < expenses:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget - expenses):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget - expenses):.2f} leva left.")
