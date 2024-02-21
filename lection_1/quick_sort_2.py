def quick_sort(arr, l, r):

    while l <= r:
        import random
        i = random.randint(l, r)
        arr[i], arr[l] = arr[l], arr[i]

        arr, m1, m2 = partition(arr, l, r)

        if (m1 - l) <= (r - m2):
            quick_sort(arr, l, m1 - 1)
            l = m2 + 1
        else:
            quick_sort(arr, m2 + 1, r)
            r = m1 - 1

    return arr

def partition(arr, l, r): # l - the index of the first el,  r - the size of the arr

    x = arr[l]
    k, j = l, l # k - the first el of equal el-s,  j - the last el of equal el-s

    for i in range(l + 1, r + 1):
        if arr[i] <= x:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]  # I swapped arr[i] and arr[j]!!

            if arr[j] != x:
                k += 1
                arr[k], arr[j] = arr[j], arr[k]

    arr[k], arr[l] = arr[l], arr[k]

    return arr, k, j


def test():
    import random

    for i in range(50):
        n = random.randint(0, 10**6)
        arr = [random.randint(-10**9, 10**9) for i in range(n)]
        try:
            assert quick_sort(arr, 0, n - 1) == sorted(arr)
        except AssertionError:
            print(n)
            print(arr)
            print(quick_sort(arr, 0, n - 1))
            print(sorted(arr))
            raise AssertionError

    print('Everything is OK')

def main():
    n = int(input())
    if n > 0:
        arr = list(map(int, input().split()))

        print(*quick_sort(arr, 0, n - 1))


if __name__ == '__main__':
    main()
    #test()