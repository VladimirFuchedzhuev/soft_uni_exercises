cards_received = input().split()
number = int(input())
half_deck = len(cards_received) // 2


for _ in range(number):
    left_side = cards_received[:half_deck]
    right_side = cards_received[half_deck:]

    shuffled_cards = []

    for num in range(len(left_side)):
        shuffled_cards.append(left_side[num])
        shuffled_cards.append(right_side[num])
    cards_received = shuffled_cards

print(shuffled_cards)
