import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

cnt = 0

def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        cnt += 1
        return True
    return False

unit = 0
count = []

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            count.append(cnt)
            unit += 1
            cnt = 0
count.sort()
print(unit)
for i in range(len(count)):
    print(count[i])
