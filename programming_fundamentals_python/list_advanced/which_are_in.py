substring = input().split(", ")
main_string = input().split(", ")
new_string = []
for sub in substring:
    for main in main_string:
        if sub in main:
            if sub not in new_string:
                new_string.append(sub)
print(new_string)