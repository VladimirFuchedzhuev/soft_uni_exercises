numbers = input().split(", ")

for integer in numbers:
    if integer == "0":
        numbers.remove(integer)
        numbers.append(integer)
new_order = ", ".join(numbers)

print(f"[{new_order}]")