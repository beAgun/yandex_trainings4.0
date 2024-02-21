def not_min(n, arr, l, r):

    for i in range(l + 1, r + 1):
        if arr[i] != arr[l]:
            ans = max(arr[i], arr[l])
            break
    else:
        ans = 'NOT FOUND'

    return ans


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(m):
        l, r = map(int, input().split())
        print(not_min(n, arr, l, r))


if __name__ == '__main__':
    main()