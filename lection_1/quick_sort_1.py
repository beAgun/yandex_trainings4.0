def partition(n, arr, x):

    less = -1
    for i in range(n):
        if arr[i] < x:
            less += 1
            arr[i], arr[less] = arr[less], arr[i]

    return less + 1, n - less - 1


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())

    print('\n'.join([str(i) for i in partition(n, arr, x)]))


if __name__ == '__main__':
    main()