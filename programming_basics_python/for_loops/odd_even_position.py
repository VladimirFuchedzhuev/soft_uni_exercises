import sys
numbers = int(input())
OddSum = 0
EvenSum = 0
EvenMin = sys.maxsize
EvenMax = -sys.maxsize
OddMin = sys.maxsize
OddMax = -sys.maxsize
for num in range(1, numbers + 1):
    new_num = float(input())
    if num % 2 == 0:
        EvenSum += new_num
        if new_num > EvenMax:
            EvenMax = new_num
        if new_num < EvenMin:
            EvenMin = new_num
    else:
        OddSum += new_num
        if new_num > OddMax:
            OddMax = new_num
        if OddMin > new_num:
            OddMin = new_num
print(f"OddSum={OddSum:.2f},")
if OddMin == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={OddMin:.2f},")
if OddMax == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={OddMax:.2f},")
print(f"EvenSum={EvenSum:.2f},")
if EvenMin == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={EvenMin:.2f},")
if EvenMax == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={EvenMax:.2f}")










