import math

lenght = float(input())
width = float(input())

width_working_space = math.floor((width * 100 - 100) / 70)
length_working_space = math.floor((lenght * 100) / 120)
total_working_spaces = (width_working_space * length_working_space) - 3
print(int(total_working_spaces))