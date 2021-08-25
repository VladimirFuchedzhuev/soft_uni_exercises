n = int(input())
day_or_night = input()

if n >= 100:
    price = n * 0.06
    print(f"{price:.2f}")
elif n >= 20:
    price = n * 0.09
    print(f"{price:.2f}")
elif day_or_night == "day":
    price = 0.70 + n * 0.79
    print(f"{price:.2f}")
else:
    price = 0.70 + n * 0.90
    print(f"{price:.2f}")