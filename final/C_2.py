import heapq
from math import floor

def fun(n, arr, s, f):

    visited = [0] * n
    min_weight = 0
    max_dist = float('inf')
    dist = [max_dist] * n
    dist[s] = 0
    weight = [min_weight] * n
    weight[s] = 10**7
    not_visited_cnt = n
    prev = [-1] * n

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
            if w > 3*10**6 and weight[i] != -1:
                w = w - 3*10**6
                new_weight = min(weight[i], w)
                if weight[j] < new_weight:
                    weight[j] = new_weight
                    #prev[j] = i
                if dist[j] < dist[i] + t:
                    dist[j] = dist[i] + t
                    if dist[j] > 1440:
                        weight[j] =-1
                        heapq.heappush(h, (-weight[j], j))

        visited[i] = 1
        not_visited_cnt -= 1

    return weight[f] if weight[f] != min_weight else 0

    # if weight[f] == min_weight:
    #     return [-1]
    # else:
    #     #return [dist[i]]
    #     way = []
    #     while f != -1:
    #         way += [f + 1]
    #         f = prev[f]
    #     return reversed(way)


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

    print(min(floor(fun(n, adj_m, s - 1, f - 1) / 100), 10**5))


if __name__ == '__main__':
    main()