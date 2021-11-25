import re

digit_pattern = r"\d"
pattern = r"(?P<surr>\:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})(?P=surr)"

text = input()

all_numbers = re.findall(digit_pattern, text)
all_numbers_int = [int(num) for num in all_numbers]
result = 1
for num in all_numbers_int:
    result *= num


data = re.finditer(pattern, text)
emoji_count = 0
emoji_list = []
for match in data:
    emoji_count += 1
    emoji = match.groupdict()
    valid_emoji = emoji["emoji"]
    emoji_coolness = sum(ord(letter) for letter in valid_emoji)
    if emoji_coolness >= result:
        emoji_list.append(emoji["surr"]+valid_emoji+emoji["surr"])

print(f"Cool threshold: {result}")
print(f"{emoji_count} emojis found in the text. The cool ones are:")
for emoji in emoji_list:
    print(emoji)