deg = float(input())
if deg >= 26 and deg <= 35:
    print("Hot")
elif deg >= 20.1 and deg <= 25.9:
    print("Warm")
elif deg >= 15 and deg <= 20:
    print("Mild")
elif deg >= 12 and deg <= 14.9:
    print("Cool")
elif deg >= 5 and deg <= 11.9:
    print("Cold")
else:
    print("unknown")