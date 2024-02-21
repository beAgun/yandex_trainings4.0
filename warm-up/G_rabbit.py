import sys


def f(n, m, arr):
    max_num = 0

    dp = [[0] * m for i in range(n)]

    for j in range(m):
        dp[0][j] = arr[0][j]
        if dp[0][j] > max_num:
            max_num = dp[0][j]

    for i in range(1, n):
        dp[i][0] = arr[i][0]
        if dp[i][0] > max_num:
            max_num = dp[i][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = (min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1) if arr[i][j] else 0
            if dp[i][j] > max_num:
                max_num = dp[i][j]

    return max_num


def test():

    with open('09.txt') as inf:
        n, m = map(int, inf.readline().split())
        arr = []
        for i in range(n):
            arr += [list(map(int, inf.readline().split()))]

    res = f(n, m, arr)
    print(res)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr += [list(map(int, input().split()))]

    print(f(n, m, arr))

if __name__ == '__main__':
    main()
    #test()