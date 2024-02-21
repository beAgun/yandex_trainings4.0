from sys import stdin
from math import floor


def f(a):

    n = len(a)
    p = 10 ** 9 + 7
    x_ = 263
    h = [0] * (n + 1)
    h_op = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    a = [0] + a

    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + a[i]) % p
        h_op[i] = (h_op[i - 1] * x_ + a[-i]) % p
        x[i] = (x[i - 1] * x_) % p

    res = []

    from1 = 1
    for slen in range(0, floor(n / 2) + 1):
        from2 = n - 2 * slen + 1

        if ((h[from1 + slen - 1] + h_op[from2 - 1] * x[slen]) % p ==
            (h_op[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p):
            res += [n - slen]

    return sorted(res)


def main():
    n, m = map(int, stdin.readline().rstrip().split())
    cubs = list(map(int, stdin.readline().rstrip().split()))

    print(*f(cubs))


if __name__ == '__main__':
    main()
    #test()

'''
6 5
2 3 3 2 1 4

4 6
------------
6 5
1 2 2 1 3 3 1 2 2 1 1 2 2 1 3 3 1 2 2 1

10 15 18 20
'''