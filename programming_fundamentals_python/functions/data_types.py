def data_type(element_type, data_input):
    if element_type == "int":
        return int(data_input) * 2
    elif element_type == "real":
        return f"{float(data_input) * 1.5:.2f}"
    elif element_type == "string":
        return f"${data_input}$"
element_type = input()
element = input()
print(data_type(element_type, element))
