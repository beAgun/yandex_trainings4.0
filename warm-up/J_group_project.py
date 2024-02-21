t = int(input())
for i in range(t):
    n, a, b = map(int, input().split())
    print('YES' if n % a <= (n // a) * (b - a) else 'NO')