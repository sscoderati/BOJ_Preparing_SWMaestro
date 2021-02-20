import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
lab = []
virus = []
space = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 2:
            virus.append((i, j))
        if tmp[j] == 0:
            space.append((i, j))
    lab.append(tmp)

def dfs(lab, y, x):
    lab[y][x] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < n and 0 <= nx < m and lab[ny][nx] == 0:
            dfs(lab, dy, dx)
result = 0

for c in combinations(space, 3):
    tmp_lab = deepcopy(lab)
    for y, x in c:
        tmp_lab[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_lab[i][j] == 2:
                dfs(tmp_lab, i, j)
    for g in tmp_lab:
        cnt += g.count(0)
    result = max(result, cnt)
print(result)
