import heapq


def min_dist(n, arr, s, f):

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

        for j, l in arr[i]:
            if dist[i] + l < dist[j]:
                dist[j] = dist[i] + l
                heapq.heappush(h, (dist[j], j))

        visited[i] = 1
        not_visited_cnt -= 1

    return dist[f] if dist[f] != max_dist else -1


def test():
    with open('08.txt', 'r') as f:
        n, k = map(int, f.readline().rstrip().split())
        adj_m = [[] for i in range(n)]

        for i in range(k):
            a, b, l = map(int, f.readline().rstrip().split())
            a -= 1;
            b -= 1
            adj_m[a] += [(b, l)]
            adj_m[b] += [(a, l)]

        s, f = map(int, f.readline().rstrip().split())

    print(min_dist(n, adj_m, s - 1, f - 1))



def main():
    n, k = map(int, input().split())
    adj_m = [[] for i in range(n)]

    for i in range(k):
        a, b, l = map(int, input().split())
        a -= 1; b -= 1
        adj_m[a] += [(b, l)]
        adj_m[b] += [(a, l)]

    s, f = map(int, input().split())

    print(min_dist(n, adj_m, s - 1, f - 1))


if __name__ == '__main__':
    #main()
    test()