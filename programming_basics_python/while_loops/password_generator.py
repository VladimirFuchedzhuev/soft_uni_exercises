n = int(input())
l = int(input())
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
for first in range(1, n + 1):
    for second in range(1, n +1):
        for index1 in ascii_lowercase[0: l]:
            for index2 in ascii_lowercase[0: l]:
                for fifth in range(1, n + 1):
                    if fifth > second and fifth > first:
                        print(f"{first}{second}{index1}{index2}{fifth}", end=" ")


