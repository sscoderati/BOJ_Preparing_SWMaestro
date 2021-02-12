from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

acnt = 0
bcnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            acnt += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            bcnt += 1
print(acnt, bcnt, end = ' ')
