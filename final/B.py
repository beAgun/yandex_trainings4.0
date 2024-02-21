import time
from math import floor


def f(s):

    n = len(s)
    p = 10 ** 9 + 7
    x_ = 263
    h = [0] * (n + 1)
    h_op = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    s = ' ' + s

    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + ord(s[i])) % p
        h_op[i] = (h_op[i - 1] * x_ + ord(s[-i])) % p
        x[i] = (x[i - 1] * x_) % p

    z = [0] * (n + 1)
    z[1] = 1

    for i in range(2, n + 1):
        l, r = i, i + i - 1
        if s[i] != s[1]:
            continue
        while l <= r:
            m = floor((r + l) / 2)
            slen = m - i + 1
            if ((h_op[(n - i + 1) + slen - 1] + h[0] * x[slen]) % p ==
                (h[slen] + h_op[(n - i + 1) - 1] * x[slen]) % p):
                z[i] = slen
                l = m + 1
            else:
                r = m - 1

    z.pop(0)
    return z


def timer(f):
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        res = f(*args, *kwargs)
        t1 = time.perf_counter()
        print(f'time: {t1 - t0}')
        return res

    return wrapper



def test():
    #timer(f)('a' * 10**6)
    #timer(f)('qwertyuiopasdfghjklzxcvbnm' * 10 ** 5)

    with open('84.txt', 'r') as inf:
        s = inf.readline().rstrip()
        timer(f)(s)


def main():
    n = int(input())
    s = input()

    print(*f(s))


if __name__ == '__main__':
    main()
    #test()
