import heapq


def min_time(n, arr, s, f):

    visited = [0] * n
    max_time = float('inf')
    time = [max_time] * n
    time[s] = 0
    not_visited_cnt = n

    h = [(time[i], i) for i in range(n)]
    heapq.heapify(h)

    while not_visited_cnt:
        while h:
            min_vertex = heapq.heappop(h)
            if not visited[min_vertex[1]]:
                break

        a = min_vertex[1]

        for t0, b, t1 in arr[a]:
            if t0 >= time[a] and t1 < time[b]:
                time[b] = t1
                heapq.heappush(h, (time[b], b))

        visited[a] = 1
        not_visited_cnt -= 1

    return time[f] if time[f] != max_time else -1


def main():
    n = int(input())
    s, f = map(int, input().split())
    r = int(input())
    adj_l = [[] for i in range(n)]
    for i in range(r):
        a, t0, b, t1 = map(int, input().split())
        a -= 1; b -= 1
        adj_l[a] += [(t0, b, t1)]

    print(min_time(n, adj_l, s - 1, f - 1))


if __name__ == '__main__':
    main()