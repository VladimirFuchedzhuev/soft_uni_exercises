import re

pattern = r"(?P<Url>(?P<sub_domain>www)\.(?P<domain>[A-Za-z0-9]+(\-?[A-Za-z0-9]+)*)(?P<Extension>(\.[a-z]+)+))"

command = input()

while command:
    domain = re.finditer(pattern, command)
    for el in domain:
        print(el.group("Url"))


    command = input()
