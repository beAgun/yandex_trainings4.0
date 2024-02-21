import time
from sys import stdin


def f(s):

    n = len(s)
    p = 10 ** 9 + 7
    x_ = 263
    h = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    s = ' ' + s

    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + ord(s[i])) % p
        x[i] = (x[i - 1] * x_) % p

    from1 = 1
    for slen in range(n - 1, 0, -1):
        k = n - slen
        from2 = from1 + k

        if ((h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % p ==
            (h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p):
            res = k
            break
    else:
        res = n

    return res


def main():
    s = stdin.readline().rstrip()

    print(f(s))


if __name__ == '__main__':
    main()
    #test()
