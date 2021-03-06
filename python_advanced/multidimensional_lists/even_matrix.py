import sys
from io import StringIO

input1 = '''2
1, 2, 3
4, 5, 6
'''

input2 = '''4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67
'''

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


def read_matrix():
    n = int(input())

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix

matrix = read_matrix()

even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]


print(even_matrix)