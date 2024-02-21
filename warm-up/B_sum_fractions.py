prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                 79, 83, 89, 97, 101, 103, 107, 109, 113,
                 127, 131, 137, 139, 149, 151, 157, 163,
                 167, 173, 179, 181, 191, 193, 197, 199]


def sum_fractions(a, b, c, d):

    m, n = (d * a + b * c), (b * d)

    if (m / n) % 1 == 0:
        return int(m / n), 1

    while True:
        for pr in prime_numbers:
            if pr < max(m, n) and m % pr == n % pr == 0:
                m /= pr; n /= pr
                break
        else:
            return int(m), int(n)


def main():
    a, b, c, d = map(int, input().split())

    print(*sum_fractions(a, b, c, d))


if __name__ == '__main__':
    main()
