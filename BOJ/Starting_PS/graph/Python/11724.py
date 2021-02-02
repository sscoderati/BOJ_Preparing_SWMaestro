import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
        #else:
            #continue

for j in range(1, n + 1):
    if not visited[j]:
        dfs(graph, j, visited)
        cnt += 1
print(cnt)
