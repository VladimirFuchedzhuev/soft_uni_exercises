from collections import deque
pumps = int(input())

petrol_stations = deque()
for _ in range(pumps):
    pump = [int(pump) for pump in input().split()]
    petrol_stations.append(pump)


for index in range(pumps):
    car_fuel = 0
    complete = True
    for petrol, distance in petrol_stations:
        car_fuel += petrol
        if distance > car_fuel:
            complete = False
            break
        car_fuel -= distance
    if complete:
        print(index)
        break
    else:
        petrol_stations.rotate(-1)
