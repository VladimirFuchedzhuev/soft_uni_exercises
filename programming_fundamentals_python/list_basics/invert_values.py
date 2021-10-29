current_string = input()

opposite_value_list = current_string.split(" ")
opposite_value_list = [-int(el) for el in opposite_value_list]

print(opposite_value_list)