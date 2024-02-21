from math import factorial
import sys


def permutations(n, perm=list(), res=list()):

    if len(perm) == n:
        res += [perm.copy()]
        print(*perm, sep='')
    else:
        for i in range(n):
            if i + 1 not in perm:
                perm += [i + 1]
                perm, res = permutations(n, perm, res)

    if perm != []:
        perm.pop()
        return perm, res
    else:
        return res


def permutations2(n, perm=list()):
    if len(perm) == n:
        print(*perm, sep='')
    else:
        for i in range(n):
            if i + 1 not in perm:
                perm += [i + 1]
                perm = permutations2(n, perm)

    if perm:
        perm.pop()
    return perm


def gen(p, cur):
    if cur == n:
        ans.append(''.join(p))
    else:
        for i in range(cur, n):
            p[i], p[cur] = p[cur], p[i]
            gen(p, cur + 1)
            p[i], p[cur] = p[cur], p[i]


p = list(map(str, range(1, n + 1)))
gen(p, 0)


def main():
    n = int(input())

    # res = permutations(n)
    # for i in res:
    #     print(*i, sep='')
    permutations2(n)


if __name__ == '__main__':
    sys.setrecursionlimit(3000)
    main()