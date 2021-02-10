import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    cnt = 0

    def dfs(x, y):
        visited[x][y] = True
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx <= -1 or nx >= m or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == False:
                dfs(i, j)
                cnt += 1
    print(cnt)
