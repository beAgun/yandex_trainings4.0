import heapq


def min_dist(n, arr, s, f):
    print(*arr, sep='\n')
    visited = [0] * n
    max_dist = 100 * n
    dist = [max_dist] * n
    dist[s] = 0
    prev = [-1] * n
    not_visited_cnt = n

    h = [(dist[i], i) for i in range(n)]
    heapq.heapify(h)

    while not_visited_cnt:
        while h:
            min_vertex = heapq.heappop(h)
            if not visited[min_vertex[1]]:
                break

        i = min_vertex[1]

        for j in range(n):
            if i != j and arr[i][j] >= 0:
                if dist[i] + arr[i][j] < dist[j]:
                    dist[j] = dist[i] + arr[i][j]
                    prev[j] = i
                    heapq.heappush(h, (dist[j], j))

        visited[i] = 1
        not_visited_cnt -= 1
    # print(prev)
    # print(dist[7])
    if dist[f] == max_dist:
        return [-1]
    else:
        #return [dist[i]]
        way = []
        while f != -1:
            way += [f + 1]
            f = prev[f]
        return reversed(way)


def test():
    arr = [[0.0, 2.66667, 3.25, 1.25, 2.6, 6.1, 2.5, 2.35, 10.16667, 4.53333],
           [1.0, 2.0, 3.0, 0.41667, 0.6, 5.1, 2.0, 2.1, 10.0, 4.0],
           [1.0, 2.0, 3.0, 0.0, 0.0, 5.0, 2.0, 2.0, 10.0, 4.0],
           [1.5, 2.33333, 3.0, 0.0, 1.6, 5.6, 2.0, 2.225, 10.0, 4.0],
           [1.3, 2.2, 3.0, 0.66667, 0.0, 5.4, 2.0, 2.025, 10.0, 4.0],
           [1.1, 2.06667, 3.0, 0.5, 0.8, 5.0, 2.0, 2.125, 10.0, 4.0],
           [0.5, 2.0, 3.0, 0.0, 0.0, 5.0, 2.0, 2.0, 10.08333, 4.2],
           [1.4, 2.26667, 3.0, 0.75, 0.2, 5.5, 2.0, 2.0, 10.0, 4.0],
           [1.0, 2.0, 3.0, 0.0, 0.0, 5.0, 2.5, 2.0, 10.0, 4.53333],
           [0.8, 2.0, 3.0, 0.0, 0.0, 5.0, 2.3, 2.0, 10.13333, 4.0]]
    print(*min_dist(10, arr, 0, 1))


def main():
    n, s, f = map(int, input().split())
    adj_m = []
    for i in range(n):
        adj_m += [list(map(int, input().split()))]

    print(*min_dist(n, adj_m, s - 1, f - 1))


if __name__ == '__main__':
    #main()
    test()

'''
4 2 4
0 1 1 -1
4 0 1 -1
2 1 0 -1
1 1 1 0
-1

4 2 1
0 1 1 -1
4 0 1 -1
2 1 0 -1
1 1 1 0
3

6 2 0
0 7 -1 -1 -1 -1
7 0 -1 8 -1 -1
-1 -1 0 100 -1 -1
-1 8 100 0 1 -1
-1 -1 -1 1 0 -1
-1 -1 -1 -1 -1 0

6 3 1
0 7 -1 -1 -1 -1
7 0 -1 8 -1 -1
-1 -1 0 100 -1 -1
-1 8 100 0 1 -1
-1 -1 -1 1 0 -1
-1 -1 -1 -1 -1 0
'''
