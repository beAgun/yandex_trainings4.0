k = int(input())
a = set()
i, j = 1, 1
while len(a) != k:
    a1 = i**2
    a2 = j**3
    if a1 <= a2:
        a |= {a1}
        i += 1
    else:
        a |= {a2}
        j += 1
print(sorted(a)[k - 1])