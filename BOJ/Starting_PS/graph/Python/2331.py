import sys
input = sys.stdin.readline

def next(a, b):
    s = str(a)
    res = 0
    for i in s:
        res += pow(int(i), b)
    return res

def dfs(a, b, cnt, visited):
    if visited[a] != 0:
        return visited[a] - 1
    visited[a] = cnt
    n = next(a, b)
    cnt += 1
    return dfs(n, b, cnt, visited)

visited = [0] * 250000
a, b = map(int, input().split())
cnt = 1
print(dfs(a, b, cnt, visited))
