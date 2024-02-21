import sys


def f(n):

    queens = []
    j, i = 0, 0
    cnt = 0
    #res = []

    while j < n:
        while i < n:
            for q_j, q_i in enumerate(queens):
                if q_i == i or (q_i + q_j == i + j) or (q_i - q_j == i - j):
                    break
            else:
                queens.append(i)
                i = 0
                break
            i += 1
        else:
            j -= 1
            if queens:
                i = queens.pop() + 1
                continue
            else:
                break

        if len(queens) == n:
            cnt += 1
            #res += [queens.copy()]
            i = queens.pop() + 1
        else:
            j += 1


    return cnt


def main():
    n = int(sys.stdin.readline())

    res = f(n)
    print(res)
    '''
    for i in res:
        print(i)
    for cond in res:
        board = [[0] * n for i in range(n)]
        for j, i in enumerate(cond):
            board[i][j] = 1
        for i in range(n):
            for j in range(n):
                print(board[i][j], end='  ')
            print()
        print('*'*70)
    '''



main()