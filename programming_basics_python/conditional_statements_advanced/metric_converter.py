num_to_convert = float(input())
unit = input()
converted_unit = input()
new_unit = 0

if unit == "mm" and converted_unit == "m":
    new_unit = num_to_convert / 1000
elif unit == "mm" and converted_unit == "cm":
    new_unit = num_to_convert / 10
elif unit == "cm" and converted_unit == "m":
    new_unit = num_to_convert / 100
elif unit == "cm" and converted_unit == "mm":
    new_unit = num_to_convert * 10
elif unit == "m" and converted_unit == "mm":
    new_unit = num_to_convert * 1000
elif unit == "m" and converted_unit == "cm":
    new_unit = num_to_convert * 100

print(f"{new_unit:.3f}")