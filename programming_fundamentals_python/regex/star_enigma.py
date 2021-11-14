import re

number_of_lines = int(input())
pattern = r"[starSTAR]"
# pattern_2 = r".*@(?P<planet_name>[a-zA-Z]+).*\:(?P<population>\d+).*!(?P<attack_type>[AD])!.*\-\>(?P<soldier_count>\d+).*"
pattern_2 = r"[^\@\-\!\:\>]*@(?P<planet_name>[a-zA-Z]+)[^\@\-\!\:\>]*\:(?P<population>\d+)[^\@\-\!\:\>]*!(?P<attack_type>[AD])![^\@\-\!\:\>]*\-\>(?P<soldier_count>\d+)[^\@\-\!\:\>]*"
attacked_planets = []
destroyed_planets = []

for line in range(number_of_lines):
    text = input()
    decrypted_message = ""
    key = len(re.findall(pattern, text))
    for char in text:
        decrypted_message += chr(ord(char) - key)
    derived_info_iter = re.finditer(pattern_2, decrypted_message)
    for info in derived_info_iter:
        planet_name = info.group("planet_name")
        attack_type = info.group("attack_type")
        if attack_type == "A":
            if planet_name not in attacked_planets:
                attacked_planets.append(planet_name)
        else:
            if planet_name not in destroyed_planets:
                destroyed_planets.append(planet_name)

print(f"Attacked planets: {len(attacked_planets)}")
for attacked_planet in sorted(attacked_planets):
    print(f"-> {attacked_planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for destroyed_planet in sorted(destroyed_planets):
    print(f"-> {destroyed_planet}")
