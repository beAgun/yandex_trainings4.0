import heapq


def min_dist(n, arr, s, f):

    visited = [0] * n
    max_dist = 100 * n
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

        for j in range(n):
            if i != j and arr[i][j] >= 0:
                dist[j] = min(dist[j], dist[i] + arr[i][j])
                heapq.heappush(h, (dist[j], j))

        visited[i] = 1
        not_visited_cnt -= 1

    return dist[f] if dist[f] != max_dist else -1


def main():
    n, s, f = map(int, input().split())
    adj_m = []
    for i in range(n):
        adj_m += [list(map(int, input().split()))]

    print(min_dist(n, adj_m, s - 1, f - 1))


if __name__ == '__main__':
    main()