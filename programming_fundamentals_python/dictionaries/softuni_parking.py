n = int(input())
register_book = {}


for registration in range(n):
    command = input().split()

    if command[0] == "register":
        user_name = command[1]
        car_plate = command[2]
        if user_name in register_book:
            print(f"ERROR: already registered with plate number {car_plate}")
        else:
            register_book[user_name] = car_plate
            print(f"{user_name} registered {car_plate} successfully")
    elif command[0] == "unregister":
        user_name = command[1]
        if user_name not in register_book:
            print(f"ERROR: user {user_name} not found")
        else:
            register_book.pop(user_name)
            print(f"{user_name} unregistered successfully")

for user, car_plate in register_book.items():
    print(f"{user} => {car_plate}")
