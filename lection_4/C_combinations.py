from itertools import combinations
from math import floor
import sys
input = sys.stdin.readline


def f1(n, adj_m):
    arr = set(i + 1 for i in range(n))
    # cache = {}
    cache = set()
    best_sum = 0
    best_comb = tuple()
    res = [1] * n

    for k in range(1, floor(n / 2) + 1):
        combs = list(combinations(arr, k))
        sum = 0
        for comb in combs:
            comp_comb = tuple(arr.difference(comb))
            if comb not in cache:
                sum = 0
                for i in comb:
                    for j in comp_comb:
                        sum += adj_m[i - 1][j - 1]
                # cache[comb] = cache[comp_comb] = sum
                cache |= {comb, comp_comb}
                if sum > best_sum:
                    best_sum = sum
                    best_comb = comb
        cache.clear()

    for i in best_comb:
        res[i - 1] = 2
    print(best_sum)
    print(*res)


def f2(n, adj_m, best_sum, best_comb):
    arr = [i + 1 for i in range(n)]
    res = [1] * n

    for k in range(2, floor(n / 2) + 1):
        combs = list(combinations(arr, k))
        summa = 0
        m = floor(len(combs) / 2) if n % k == 0 else len(combs)
        for i in range(m):
            summa = sum([adj_m[j - 1][-1] for j in combs[i]])
            if summa < best_sum:
                continue
            for f, s in list(combinations(combs[i], 2)):
                summa -= 2*adj_m[f - 1][s - 1]
            if summa > best_sum:
                best_sum = summa
                best_comb = combs[i]

    for i in best_comb:
        res[i - 1] = 2
    print(best_sum)
    print(*res)



def rec(n, adj_m, v=0, res=None, summa=0, best_sum=0, best_res=None):
    if res is None:
        res = [-1] * n
    if best_res is None:
        best_res = [-1] * n

    if v == n:
        return (summa, res) if summa > best_sum else None

    for group in [1, 2]:
        new_sum, new_res = summa, res.copy()
        new_res[v] = group
        for i in range(n):
            if i == v:
                break
            elif new_res[i] != new_res[v]:
                new_sum += adj_m[v][i]
        ans = rec(n, adj_m, v + 1, new_res, new_sum, best_sum, best_res)
        if ans:
            (best_sum, best_res) = ans

    return best_sum, best_res


def main():
    n = int(input())
    adj_m = []
    best_sum = 0
    best_comb = []
    for i in range(n):
        s = list(map(int, input().split()))
        if sum(s) > best_sum:
            best_sum = sum(s)
            best_comb = [i + 1]
        s += [sum(s)]
        adj_m += [s]

    #f2(n, adj_m, best_sum, best_comb)
    best_sum, best_res = rec(n, adj_m)
    print(best_sum)
    print(*best_res)


main()