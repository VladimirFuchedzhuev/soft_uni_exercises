numbers_received = input().split(", ")
beggars = int(input())
sum_per_beggar = []
start_index = 0

for beggar in range(beggars):
    current_sum = 0
    for income in range(start_index, len(numbers_received), beggars):
        current_sum += int(numbers_received[income])
    sum_per_beggar.append(current_sum)
    start_index += 1

print(sum_per_beggar)