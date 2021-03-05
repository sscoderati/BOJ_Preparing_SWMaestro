import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
dist = [[0] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    graph[a][a] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                dist[a][b] = k

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end = " ")
        else:
            print(graph[a][b], end = " ")
    print()

def path(i, j):
    if dist[i][j] == 0:
        return []
    k = dist[i][j]
    return path(i, k) + [k] + path(k, j)

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] in [INF, 0]:
            print(0)
            continue
        min_path = [a] + path(a, b) + [b]
        print(len(min_path), end=' ')
        print(*min_path)
