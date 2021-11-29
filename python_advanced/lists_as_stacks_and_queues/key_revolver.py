from collections import deque

bullet_price = int(input())
size_of_the_gun_barrel = int(input())
bullets = [int(num) for num in input().split()]
locks = deque([int(num) for num in input().split()])
intelligence_value = int(input())
shooting_counter = 0


while locks:
    while bullets:
        if locks:
            bullet = bullets.pop()
            shooting_counter += 1
            intelligence_value -= bullet_price
            if bullet <= locks[0]:
                locks.popleft()
                print('Bang!')
            else:
                print('Ping!')
        else:
            break
        if shooting_counter == size_of_the_gun_barrel and len(bullets) > 0:
            print('Reloading!')
            shooting_counter = 0
    else:
        break
if len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
