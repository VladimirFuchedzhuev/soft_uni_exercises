from collections import deque

cups = deque(int(num) for num in input().split())
bottles = [int(num) for num in input().split()]
waisted_litters = 0


while bottles:
    if cups:
        current_bottle = bottles[-1]
        current_cup = cups[0]
        if current_bottle >= current_cup:
            waisted_litters += current_bottle - current_cup
            bottles.pop()
            cups.popleft()
        else:
            cups[0] -= bottles[-1]
            bottles.pop()
    else:
        break



if bottles:
    print(f"Bottles: {' '.join(str(num) for num in bottles)}")
elif cups:
    print(f"Cups: {' '.join(str(num) for num in cups)}")
print(f"Wasted litters of water: {waisted_litters}")