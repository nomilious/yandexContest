import heapq


def main():
    inf = 2000
    V_num, s, f = map(int, input().split())
    graph = []
    for i in range(V_num):
        graph.append(list(map(int, input().split())))
    pq = []
    heapq.heappush(pq, (0, s - 1))
    dist = [V_num * inf] * V_num
    while pq:
        temp = heapq.heappop(pq)
        x = temp[1]
        for i in range(V_num):
            if graph[x][i] != -1 and graph[x][i] - temp[0] < dist[i]:
                dist[i] = graph[x][i] - temp[0]
                heapq.heappush(pq, (-dist[i], i))
    if dist[f - 1] == V_num * inf:
        print("-1")
    else:
        print(dist[f - 1])


if __name__ == "__main__":
    main()
