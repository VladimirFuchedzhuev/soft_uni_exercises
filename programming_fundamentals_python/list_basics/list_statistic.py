n = int(input())

count_positives = []
sum_of_negatives = []

for i in range(n):
    number = int(input())
    if 0 <= number:
        count_positives.append(number)
    else:
        sum_of_negatives.append(number)

print(count_positives)
print(sum_of_negatives)
print(f"Count of positives: {len(count_positives)}. Sum of negatives: {sum(sum_of_negatives)}")