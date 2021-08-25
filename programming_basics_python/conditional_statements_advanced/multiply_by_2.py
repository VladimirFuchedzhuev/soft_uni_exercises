import sys

num = float(input())
while(num <= sys.maxsize and num >= 0):
    num *= 2
    print(f"Result: {num:.2f}")
    num = float(input())
else:
    print("Negative number!")