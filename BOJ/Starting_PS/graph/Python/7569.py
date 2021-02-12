import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, k = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(k)]
q = deque()

for d in range(k):
    for i in range(n):
        for j in range(m):
            if graph[d][i][j] == 1:
                q.append((d, i, j))

def bfs():
    cnt = 0
    while q:
        cnt += 1
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m or nz <= -1 or nz >= k:
                continue
            if graph[nz][nx][ny] == -1:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nz, nx, ny))
bfs()
check = True
days = -1
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                check = False
            days = max(days, k)

if check == False:
    print(-1)
else:
    if days == 1:
        print(0)
    else:
        print(days - 1)
