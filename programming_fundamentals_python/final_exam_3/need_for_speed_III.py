cars_number = int(input())
cars = {}

for i in range(cars_number):
    cars_data = input().split("|")
    car, mileage, fuel = cars_data[0], cars_data[1], cars_data[2]
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

command = input()
while command != "Stop":
    command_data = command.split(" : ")
    current_car = command_data[1]
    if command_data[0] == "Drive":
        distance_to_drive = int(command_data[2])
        need_fuel = int(command_data[3])
        if cars[current_car]["fuel"] < need_fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[current_car]['mileage'] += distance_to_drive
            cars[current_car]['fuel'] -= need_fuel
            print(f"{current_car} driven for {distance_to_drive} kilometers. {need_fuel} liters of fuel consumed.")
            if cars[current_car]['mileage'] >= 100_000:
                print(f"Time to sell the {current_car}!")
                del cars[current_car]
    elif command_data[0] == "Refuel":
        given_fuel = int(command_data[2])
        if cars[current_car]['fuel'] + given_fuel > 75:
            print(f"{current_car} refueled with {75 - cars[current_car]['fuel']} liters")
            cars[current_car]['fuel'] = 75
        else:
            print(f"{current_car} refueled with {given_fuel} liters")
            cars[current_car]['fuel'] += given_fuel
    elif command_data[0] == "Revert":
        kilometers = int(command_data[2])
        if cars[current_car]['mileage'] - kilometers < 10_000:
            cars[current_car]['mileage'] = 10_000
        else:
            print(f"{current_car} mileage decreased by {kilometers} kilometers")
            cars[current_car]['mileage'] -= kilometers

    command = input()

sorted_result = sorted(cars.items(), key=lambda kvp: (-kvp[1]['mileage'], kvp[0]))
for k, v in sorted_result:
    print(f"{k} -> Mileage: {v['mileage']} kms, Fuel in the tank: {v['fuel']} lt.")