numbers = [int(x) for x in input().split()]
#positive_numbers = sum([x for x in numbers if x > 0])
positive_numbers = sum(filter(lambda x: x > 0, numbers))
negative_numbers = sum(filter(lambda x: x < 0, numbers))

print(negative_numbers)
print(positive_numbers)

if abs(negative_numbers) > positive_numbers:
    print("The negatives are stronger than the positives")
else: 
    print("The positives are stronger than the negatives")