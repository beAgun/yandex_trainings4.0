from math import sqrt, acos, atan2


def f(x1, y1, x2, y2):

    r1 = sqrt(x1 ** 2 + y1 ** 2)
    r2 = sqrt(x2 ** 2 + y2 ** 2)

    if r2 < r1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        r1, r2 = r2, r1

    if x1 * (y2 - y1) == y1 * (x2 - x1):  # 3 points in the same line
        if x1 * x2 >= 0 and y1 * y2 >= 0:
            return r2 - r1
        if x1 * x2 <= 0 and y1 * y2 <= 0:
            return r1 + r2

    #fi = acos((x1 * x2 + y1 * y2) / (r1 * r2))
    fi = abs(atan2(y1, x1) - atan2(y2, x2))

    return min(r1 * fi + r2 - r1, r1 + r2)


def test(fun):
    def f(*args):
        return round(fun(*args), 6)

    assert f(0, 5, 4, 3) == 4.636476
    assert f(0, 5, 4, -3) == 10
    assert f(0, 0, 0, 0) == 0
    assert f(1, 1, 1, 1) == 0
    assert f(-4, -3, 4, 3) == 10
    assert f(0, 0, 3, 4) == 5
    assert f(0, 8, 0, 4) == 4
    assert f(0, 8, 0, -8) == 16
    assert f(-2, 0, 2, 0) == 4
    assert f(4, 0, 8, 0) == 4
    assert f(1000000, -372061, -999999, - 1000000) == 2481184.920375
    assert f(1000000, 1000000, 999999, 999999) == 1.414214
    assert f(1000000, 1000000, 1000000, 999999) == 1.414213


def main():
    x1, y1, x2, y2 = map(int, input().split())
    print(f(x1, y1, x2, y2))


if __name__ == '__main__':
    main()
    #test(f)
