row_activation_key = input()

data = input()

while not data == "Generate":
    data = data.split(">>>")
    if data[0] == "Contains":
        substring = data[1]
        if substring in row_activation_key:
            print(f"{row_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif data[0] == "Flip":
        state = data[1]
        start_index = int(data[2])
        end_index = int(data[3])

        first_part = row_activation_key[:start_index]
        mid_part = row_activation_key[start_index:end_index]
        last_part = row_activation_key[end_index:]
        if state == "Upper":
            mid_part = mid_part.upper()
        elif state == "Lower":
            mid_part = mid_part.lower()
        row_activation_key = first_part + mid_part + last_part
        print(row_activation_key)
    elif data[0] == "Slice":
        start_index = int(data[1])
        end_index = int(data[2])

        first_part = row_activation_key[:start_index]
        last_part = row_activation_key[end_index:]
        row_activation_key = first_part + last_part
        print(row_activation_key)
    data = input()

print(f"Your activation key is: {row_activation_key}")
