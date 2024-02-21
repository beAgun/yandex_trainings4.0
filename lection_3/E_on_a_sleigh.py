import heapq
import sys


def min_time(n, arr, s):
    #print(*arr, sep=',\n')
    visited = [0] * n
    max_time = float('inf')
    time = [max_time] * n
    time[s] = 0
    prev = [-1] * n
    not_visited_cnt = n

    h = [(time[i], i) for i in range(n)]
    heapq.heapify(h)

    while not_visited_cnt:
        while h:
            min_vertex = heapq.heappop(h)
            if not visited[min_vertex[1]]:
                break

        j = min_vertex[1]

        for i in range(n):
            if i != j and arr[i][j] > 0:
                if time[j] + arr[i][j] < time[i]:
                    time[i] = time[j] + arr[i][j]
                    prev[i] = j
                    heapq.heappush(h, (time[i], i))

        visited[j] = 1
        not_visited_cnt -= 1
    #print(prev)
    way = []
    for i in range(n):
        f = i
        way += [[]]
        while f != -1:
            way[i] += [f + 1]
            f = prev[f]

    return max(time), way[time.index(max(time))]


def f(n ,cities, roads, way):

    # def dfs(v):
    #     print('v', v)
    #     for near_city, s in roads[v].items():
    #         #print(near_city)
    #         del roads[near_city][v]
    #         r = dfs(near_city)
    #
    # dfs(0)
    # print('+'*100)

    def tree_traversal(cur_city, way):
        #print('vert', cur_city)
        for near_city, s in roads[cur_city].items():
            del roads[near_city][cur_city]
            if cur_city != 0:
                for city in range(n):
                    if (way[near_city][city] == 0 and city != near_city and
                        min(way[cur_city][city], way[near_city][cur_city])) != 0:
                        way[near_city][city] = way[city][near_city] = \
                            way[cur_city][city] + way[near_city][cur_city]
                        #print(city, near_city)
            way = tree_traversal(near_city, way)
        return way

    way = tree_traversal(0, way)

    way_times = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if way[i][j] != 0:
                way_times[i][j] = round(cities[i][0] + way[i][j] / cities[i][1], 5)
    #print(*way, sep=',\n')
    #print('*'*50)
    return min_time(n,way_times, 0)



def main():
    sys.setrecursionlimit(3000)

    n = int(input())
    cities = []
    for i in range(n):
        t, v = map(int, input().split())  # h, km/h
        cities += [(t, v)]

    roads = [{} for i in range(n)]
    way = [[0] * n for i in range(n)]
    for i in range(n - 1):
        a, b, s = map(int, input().split())  # km

        way[a - 1][b - 1] = way[b - 1][a - 1] = s

        roads[a - 1][b - 1] = s
        roads[b - 1][a - 1] = s


    time, way = f(n ,cities, roads, way)
    print('{:.4f}'.format(round(time, 4)))
    print(*way)


if __name__ == '__main__':
    main()


'''
10
0 10
2 15
3 40
0 12
0 5
5 10
2 10
2 40
10 60
4 15
1 2 10
2 4 5
2 5 3
2 6 1
5 8 1
1 7 5
1 3 10
7 9 5
7 10 3
'''
