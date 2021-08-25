import math
change = float(input()) * 100
change = math.floor(change)
count_coins = 0
while change> 0:
    if change >= 200:
        change -= 200
        count_coins += 1
    elif change >= 100:
        change -= 100
        count_coins += 1
    elif change >= 50:
        change -= 50
        count_coins += 1
    elif change >= 20:
        change -= 20
        count_coins += 1
    elif change >= 10:
        change -= 10
        count_coins += 1
    elif change >= 5:
        change -= 5
        count_coins += 1
    elif change >= 2:
        change -= 2
        count_coins += 1
    elif change >= 1:
        change -= 1
        count_coins += 1
else:
    print(count_coins)