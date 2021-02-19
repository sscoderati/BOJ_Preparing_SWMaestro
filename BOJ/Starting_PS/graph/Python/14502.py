import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx, ny)

def safe_zone():
    safe = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                safe += 1
    return safe

def dfs(count):
    global result
    if count == 3:
        tmp = copy.deepcopy(lab)
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)
        result = max(result, safe_zone())
        return True
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                dfs(count + 1)
                lab[i][j] = 0
dfs(0)
print(result)
