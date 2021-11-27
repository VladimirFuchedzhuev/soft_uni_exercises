def longest_consec(strarr, k):
    length = []
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    else:
        while len(strarr) > 0:
            length.append(strarr[0] + strarr[1])
            strarr.pop(0)
    max = length[0]
    for i in range(0, len(length)):
        if len(length[i]) > len(max):
            max = length[i]
    return max

print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))