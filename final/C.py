import heapq
from math import floor

def fun(n, arr, s, f):

    visited = [0] * n
    min_weight = 0
    weight = [min_weight] * n
    weight[s] = 10**7
    not_visited_cnt = n

    h = [(-weight[i], i) for i in range(n)]
    heapq.heapify(h)
    # h = [(dist[i], i) for i in range(n)]
    # heapq.heapify(h)

    while not_visited_cnt:
        while h:
            min_vertex = heapq.heappop(h)
            if not visited[min_vertex[1]]:
                break

        i = min_vertex[1]
        for j, t, w in arr[i]:
            if w > 3*10**6:
                w = w - 3*10**6
                new_weight = min(weight[i], w)
                if weight[j] < new_weight:
                    weight[j] = new_weight
                heapq.heappush(h, (-weight[j], j))

        visited[i] = 1
        not_visited_cnt -= 1
    #print(weight)
    return fun2(n, arr, s, f, weight)
    return weight[f] if weight[f] != min_weight else 0

def fun2(n, arr, s, f, weight):

    visited = [0] * n
    max_dist = float('inf')
    dist = [max_dist] * n
    dist[s] = 0
    not_visited_cnt = n

    h = [(dist[i], i) for i in range(n)]
    heapq.heapify(h)

    while not_visited_cnt:
        while h:
            min_vertex = heapq.heappop(h)
            if not visited[min_vertex[1]]:
                break

        i = min_vertex[1]
        for j, t, w in arr[i]:
            if dist[j] < dist[i] + t:
                dist[j] = dist[i] + t
                heapq.heappush(h, (dist[j], j))

        visited[i] = 1
        not_visited_cnt -= 1
    #print(weight)
    if dist[f] > 1440:
        return 0
    else:
        return floor(weight[f] / 100)
    #return weight[f] if weight[f] != min_weight else 0


def main():
    n, m = map(int, input().split())
    adj_m = [[] for i in range(n)]

    for i in range(m):
        a, b, t, w = map(int, input().split())
        a -= 1;
        b -= 1
        adj_m[a] += [(b, t, w)]
        adj_m[b] += [(a, t, w)]

    s, f = 1, n

    print(floor(fun(n, adj_m, s - 1, f - 1) / 100))


if __name__ == '__main__':
    main()

'''
9 12
1 2 10 3000500
2 4 80 300060012
2 5 90 3000700
1 3 50 3000400
3 5 70 3000800
3 7 150 3000900
4 6 80 3000100
5 6 90 3000030
7 8 150 3000500
6 8 50 3000200
8 9 10 3000900
6 9 10 3000900
5

3 2
1 2 20 3000500
2 3 1440 3000500
0

3 2
1 2 20 300000552
2 3 1400 300000552
0

'''