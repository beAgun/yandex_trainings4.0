import random


def random_select(arr, l, r, k):

    if l >= r:
        return arr[l]

    i = random.randint(l, r)
    #i = i**2
    arr[i], arr[l] = arr[l], arr[i]

    arr, m1, m2 = partition(arr, l, r)

    if l <= k <= m1 - 1:
        return random_select(arr, l, m1 - 1, k)
    elif k == m1: #m1 <= k <= m2:
        return arr[k]
    else:
        return random_select(arr, m2 + 1, r, k - m2)


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


def main():
    k = int(input())
    #n, k = map(int, input().split())
    n = k
    arr = []
    for i in range(n):
        arr += [(i + 1)**2]
    for i in range(n):
        arr += [(i + 1)**3]
    print(random_select(arr, 0, n - 1, k - 1)) # k - 0-based, if 1-based, then k - 1


if __name__ == '__main__':
    main()
    #test()