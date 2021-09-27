resource = input()
all_resource = []
resource_dict = {}
while not resource == "stop":
    all_resource.append(resource)
    resource = input()

for index in range(0, len(all_resource), 2):
    key = all_resource[index]
    value = int(all_resource[index + 1])
    if all_resource[index] not in resource_dict:
        resource_dict[key] = value
    else:
        resource_dict[key] += value

for key, value in resource_dict.items():
    print(f"{key} -> {value}")