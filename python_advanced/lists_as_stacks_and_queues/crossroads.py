from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars_waiting = deque()
passed_cars = 0
crash = False

command = input()

while not command == "END":
    if command == 'green':
        if cars_waiting:
            current_car = cars_waiting.popleft()
            time_remaining = green_light_duration - len(current_car)
            while time_remaining > 0:
                passed_cars += 1
                if cars_waiting:
                    current_car = cars_waiting.popleft()
                    time_remaining -= len(current_car)
                else:
                    break
            if time_remaining == 0:
                passed_cars += 1
            if free_window_duration >= abs(time_remaining):
                if time_remaining < 0:
                    passed_cars += 1
            else:
                idx = free_window_duration + time_remaining
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[idx]}.")
                crash = True
                break
    else:
        cars_waiting.append(command)
    command = input()

if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
