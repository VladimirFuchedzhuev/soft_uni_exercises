party_size = int(input())
days = int(input())

total_coins = 0

for days in range(1, days + 1):
    if days % 10 == 0:
        party_size -= 2
    if days % 15 == 0:
        party_size += 5
    total_coins += 50 - (party_size * 2)
    if days % 3 == 0:
        total_coins -= party_size * 3
    if days % 5 == 0:
        total_coins += party_size * 20
        if days % 3 == 0:
            total_coins -= party_size * 2

coins_per_companion = int(total_coins / party_size)
print(f"{party_size} companions received {coins_per_companion} coins each.")