def merge_sort(arr, l, r):

    if l < r:
        m = int((l + r) / 2)
        return merge(merge_sort(arr, l, m), merge_sort(arr, m + 1, r))

    return arr[l: r + 1]


def merge(arr1, arr2):
    arr = []
    i, j = 0, 0
    n, m = len(arr1), len(arr2)

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

    if n > 0:
        arr = list(map(int, input().split()))

        print(*merge_sort(arr, 0, n - 1))


if __name__ == '__main__':
    main()