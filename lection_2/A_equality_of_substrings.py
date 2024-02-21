def main():
    s = input()

    n = len(s)
    p = 10**9 + 13
    x_ = 263
    h = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    s = ' ' + s

    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + ord(s[i])) % p
        x[i] = (x[i - 1] * x_) % p

    def is_equal(l, a, b):

        return (
                (h[a + l - 1] + h[b - 1] * x[l]) % p ==
                (h[b + l - 1] + h[a - 1] * x[l]) % p
        )

    q = int(input())
    for i in range(q):
        l, a, b = map(int, input().split())
        print('yes' if is_equal(l, a + 1, b + 1) else 'no')


def main2():
    s = input()

    n = len(s)
    p = 10**9 + 13
    x_ = 263
    h = [0] * n
    x = [0] * n
    h[0] = ord(s[0])
    x[0] = x_

    for i in range(1, n):
        h[i] = (h[i - 1] * x_ + ord(s[i])) % p
        x[i] = (x[i - 1] * x_) % p

    def is_equal(l, a, b):

        return (
                (h[a + l - 1] + h[b - 1] * x[l]) % p ==
                (h[b + l - 1] + h[a - 1] * x[l]) % p
        )

    q = int(input())
    for i in range(q):
        l, a, b = map(int, input().split())
        print('yes' if is_equal(l, a, b) else 'no')


if __name__ == '__main__':
    main2()