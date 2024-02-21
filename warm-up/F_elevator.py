from math import ceil


def min_time(k, n, a):
    rest, time= 0, 0

    for i in reversed(range(n)):
        if a[i] == 0:
            continue

        if rest != 0:
            if a[i] >= (k - rest):
                a[i] -= (k - rest)
                time += (i + 1) * 2 * ceil(a[i]/ k)
                rest = a[i] % k
            else:
                rest += a[i]
        else:
            time += (i + 1) * 2 * ceil((a[i] + rest) / k)
            rest = a[i] % k


    return time


def test(f):
    assert f(2, 3, [3, 0, 1]) == 8
    assert f(10, 1, [5]) == 2
    assert f(2, 1, [5]) == 6
    assert f(5, 1, [5]) == 2
    assert f(5, 5, [5, 5, 5, 5, 5]) == 2 + 4 + 6 + 8 + 10
    assert f(5, 5, [5, 5, 5, 5, 2]) == 30
    assert f(5, 5, [5, 5, 5, 5, 6]) == 40
    assert f(5, 1, [0]) == 0
    assert f(10, 5, [2, 2, 2, 2, 2]) == 10
    assert f(10, 11, [2, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0]) == 18
    assert f(10, 5, [0, 0, 0, 0, 0]) == 0
    #assert f(0, 3, [4, 0, 5]) == 0
    assert f(1, 3, [4, 0, 5]) == 8 + 30
    assert f(1, 6, [4, 0, 5, 0, 0, 0]) == 8 + 30
    assert f(1, 1, [1]) == 2
    assert f(1, 2, [1, 0]) == 2
    assert f(10, 5, [0, 0, 0, 0, 10]) == 10
    assert f(2, 3, [1, 1, 1]) == 8
    assert f(3, 3, [0, 3, 0]) == 4
    assert f(3, 3, [0, 1, 0]) == 4
    assert f(3, 3, [0, 4, 0]) == 8


def main():
    k = int(input())
    n = int(input())
    arr = []
    for i in range(n):
        arr += [int(input())]

    print(min_time(k, n, arr))


if __name__ == '__main__':
    main()
    #test(min_time)