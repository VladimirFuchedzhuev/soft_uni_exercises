import re

pattern_1 = r"[A-Za-z]+"
pattern_2 = r"\d"
names = input()
names = names.split(", ")
text = input()
names_list = {}
total_km = 0

while not text == "end of race":
    name = "".join(re.findall(pattern_1, text))
    km = [int(num) for num in re.findall(pattern_2, text)]
    km = sum(km)
    if name in names:
        if name not in names_list:
            names_list[name] = km
        else:
            names_list[name] += km
    text = input()

names_sorted = sorted(names_list.items(), key=lambda x: -x[1])


print(f"1st place: {names_sorted[0][0]}")
print(f"2nd place: {names_sorted[1][0]}")
print(f"3rd place: {names_sorted[2][0]}")
