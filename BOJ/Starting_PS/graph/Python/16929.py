import sys
input = sys.stdin.readline

color = {}
N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
answer = False
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def findCycle(x, y, prev_x, prev_y):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        elif graph[nx][ny] != graph[x][y]:
            continue
        elif visited[nx][ny] == 0:
            if findCycle(nx, ny, x, y):
                return True
        elif prev_x != nx or prev_y != ny:
            return True
    return False

for i in range(N):
    for j in range(M):
        color.setdefault(graph[i][j], (i, j))

for value in color.values():
    x, y = value
    if findCycle(x, y, -1, -1):
        answer = True
        break

if answer:
    print('Yes')
else:
    print('No')
