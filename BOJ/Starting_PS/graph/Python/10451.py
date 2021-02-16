import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

t = int(input())

def dfs(now, visited):
    visited[now] = True
    idx = p[now - 1]
    if visited[idx] == False:
        visited[idx] = True
        dfs(idx, visited)

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    visited = [False] * (n + 1)
    cnt = 0
    for i in range(1, n + 1):
        if visited[i] == False:
            dfs(i, visited)
            cnt += 1
    print(cnt)
