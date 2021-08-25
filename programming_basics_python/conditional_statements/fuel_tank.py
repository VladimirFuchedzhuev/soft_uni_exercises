fuel_type = input()
fuel_in_letters = int(input())

if fuel_in_letters >= 25 and fuel_type == "Diesel":
    print("You have enough diesel.")
elif fuel_in_letters >= 25 and fuel_type == "Gasoline":
    print("You have enough gasoline.")
elif fuel_in_letters >= 25 and fuel_type == "Gas":
    print("You have enough gas.")
elif fuel_in_letters < 25 and fuel_type == "Diesel":
    print("Fill your tank with diesel!")
elif fuel_in_letters < 25 and fuel_type == "Gasoline":
    print("Fill your tank with gasoline!")
elif fuel_in_letters < 25 and fuel_type == "Gas":
    print("Fill your tank with gas!")
else:
    print("Invalid fuel!")
