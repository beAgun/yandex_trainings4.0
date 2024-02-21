# Input: Chessboard size `n` (1-7)
# Initial location of a knight: (0, 0)
# Output: an ordered list of coordinates of the knight moves if it can visit all places
# or `None` instead

def f(n, i, j):
    '''Returns `None` if there is no solution or an ordered list of coordinates
       of moves `coords`.  '''
    def rec(cnt, coords):
        if cnt == 0:
            return coords

        i, j = coords[-1]
        moves = ((i - 1, j - 2), (i - 2, j - 1), (i - 2, j + 1),
                 (i - 1, j + 2), (i + 1, j + 2), (i + 2, j + 1),
                 (i + 2, j - 1), (i + 1, j - 2))
        for k, m in moves:
            if 0 <= k < n and 0 <= m < n and (k, m) not in coords:
                res = rec(cnt - 1, coords + [(k, m)])
                if res is not None:
                    return res

    return rec(n**2 - 1, [(0, 0)])


def main():
    board_size = int(input())
    i, j = 0, 0
    print(f(board_size, i, j))


if __name__ == '__main__':
    main()
    #test(f)