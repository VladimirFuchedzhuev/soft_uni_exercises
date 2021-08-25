v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

pipes_volume = p1 * h + p2 * h
if pipes_volume < v:
    p1_volume = (p1 * h / pipes_volume) * 100
    p2_volume = (p2 * h / pipes_volume) * 100
    total_volume = (pipes_volume / v) * 100
    print(f"The pool is {total_volume:.2f}% full. Pipe 1: {p1_volume:.2f}%. Pipe 2: {p2_volume:.2f}%.")
else:
    overflow = pipes_volume - v
    print(f"For {h:.2f} hours the pool overflows with {overflow:.2f} liters.")
