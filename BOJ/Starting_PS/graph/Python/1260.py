from collections import deque
import sys

input = sys.stdin

n, m, v = map(int, input.readline().strip().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input.readline().strip().split())
    graph[a][b] = graph[b][a] = 1


def dfs(v):
    visited[v] = 1
    print(v, end =' ')
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = []
    queue = deque(queue)
    queue.append(v)
    visited[v] = 0 # dfs() 호출로 인해 변경된 visited 초기화
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, n + 1):
            if visited[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 0
dfs(v)
print()
bfs(v)
