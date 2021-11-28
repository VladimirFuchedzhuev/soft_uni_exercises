box = [int(num) for num in input().split()]
capacity = int(input())

counter_racks = 1

current_capacity = capacity
while len(box) > 0:
    current_clothes = box.pop()
    if current_clothes <= current_capacity:
        current_capacity -= current_clothes
    else:
        counter_racks += 1
        current_capacity = capacity
        current_capacity -= current_clothes

print(counter_racks)
