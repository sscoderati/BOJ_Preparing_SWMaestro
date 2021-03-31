# 백트래킹 & 완전탐색
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tmp = []
res = []
visited = [False] * n

def dfs(start):
    if start == n:
        res.append(sum(abs(tmp[i + 1] - tmp[i]) for i in range(n - 1)))
        return
    for i in range(n):
        if visited[i]:
            continue
        tmp.append(arr[i])
        visited[i] = True
        dfs(start + 1)
        tmp.pop()
        visited[i] = False

dfs(0)
print(max(res))
""" 순열 & 완전탐색
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = permutations(map(int, input().split()))
ans = 0

for i in arr:
    tmp = 0
    for j in range(n - 1):
        tmp += abs(i[j] - i[j + 1])
    ans = max(ans, tmp)
print(ans)
"""