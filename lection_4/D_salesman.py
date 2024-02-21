import sys
input = sys.stdin.readline


def f(n, adj_m):
    if n == 1:
        return adj_m[0][0]

    def rec(v=0, not_visited=None, sum=0, min_sum=float('+inf')):
        if not_visited is None:
            not_visited = set(i for i in range(1, n))

        if len(not_visited) == 0:
            if adj_m[v][0] != 0 and sum + adj_m[v][0] < min_sum:
                min_sum = sum + adj_m[v][0]

        for i in not_visited:
            if adj_m[v][i] == 0:
                continue
            ans = rec(i, not_visited.difference({i}), sum + adj_m[v][i], min_sum)
            if ans is not None:
                min_sum = ans

        return min_sum

    return rec()


def main():
    n = int(input())
    adj_m = []
    for i in range(n):
        s = list(map(int, input().split()))
        adj_m += [s]

    res = f(n, adj_m)
    print(-1 if res == float('+inf') else res)


if __name__ == '__main__':
    main()