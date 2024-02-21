from math import ceil

# n1 / n2 ~ max(>=1) => n1 ~ max & n2 ~ min
a, b, n = int(input()), int(input()), int(input())
print('Yes' if a > ceil(b / n) else 'No')