def merge(n, arr1, m, arr2):
    arr = []
    i, j = 0, 0

    while n and m:
        if arr1[-n] <= arr2[-m]:
            arr += [arr1[-n]]
            n -= 1
        else:
            arr += [arr2[-m]]
            m -= 1

    while n:
        arr += [arr1[-n]]
        n -= 1
    while m:
        arr += [arr2[-m]]
        m -= 1

    return arr


def main():
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    print(*merge(n, arr1, m, arr2))


if __name__ == '__main__':
    main()