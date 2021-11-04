software_version = input().split(".")
software_version_as_int = int("".join(software_version)) + 1
new_version = list(str(software_version_as_int))
print(".".join(new_version))

