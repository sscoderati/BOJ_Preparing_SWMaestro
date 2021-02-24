from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tube = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
virus = []

dx = [1, -1 ,0, 0]
dy = [0, 0, -1 ,1]

for i in range(n):
    for j in range(n):
        if tube[i][j] != 0:
            virus.append((tube[i][j], i, j, 0))

virus.sort(key = lambda x:x[0])
q = deque(virus)

while q:
    v, cx, cy, time = q.popleft()
    if s == time: break

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < n and 0 <= ny < n and tube[nx][ny] == 0:
            tube[nx][ny] = v
            q.append((tube[nx][ny], nx, ny, time + 1))

print(tube[x - 1][y - 1])
