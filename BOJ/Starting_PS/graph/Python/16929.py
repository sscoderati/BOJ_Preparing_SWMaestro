import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = False
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def findCycle(x, y, cnt):
    global cx, cy, answer
    if answer:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] != graph[x][y]:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = True
            findCycle(nx, ny, cnt + 1)
            visited[nx][ny] = False
        else:
            if cnt >= 4 and cx == nx and cy == ny:
                answer = True
                return

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cx, cy = i, j
            visited[i][j] = True
            findCycle(i, j, 1)
        if answer:
            print('Yes')
            sys.exit()

print('No')
