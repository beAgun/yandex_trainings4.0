import heapq


def min_dist(n, arr, s, f):

    visited = [0] * n
    min_weight = 0
    weight = [min_weight] * n
    weight[s] = float('inf')
    not_visited_cnt = n
    prev = [-1] * n

    h = [(-weight[i], i) for i in range(n)]
    heapq.heapify(h)

    while not_visited_cnt:
        while h:
            min_vertex = heapq.heappop(h)
            if not visited[min_vertex[1]]:
                break

        i = min_vertex[1]

        for j in range(n):
            if i != j and arr[i][j] >= 0: # if there is  a way between different vertexes
                new_weight = min(weight[i], arr[i][j])
                if weight[j] < new_weight:
                    weight[j] = new_weight
                    prev[j] = i
                heapq.heappush(h, (weight[j], j))

        visited[i] = 1
        not_visited_cnt -= 1

    return weight[f] if weight[f] != min_weight else -1

    if weight[f] == min_weight:
        return [-1]
    else:
        #return [dist[i]]
        way = []
        while f != -1:
            way += [f + 1]
            f = prev[f]
        return reversed(way)


def main():
    n, s, f = map(int, input().split())
    adj_m = []
    for i in range(n):
        adj_m += [list(map(int, input().split()))]

    print(min_dist(n, adj_m, s - 1, f - 1))


if __name__ == '__main__':
    main()