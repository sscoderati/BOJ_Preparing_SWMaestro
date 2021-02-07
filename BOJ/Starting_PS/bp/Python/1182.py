import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cursum = 0
cnt = 0

def dfs(cur):
    global cnt, cursum
    if cur == n:
        return
    if cursum + arr[cur] == s:
        cnt += 1
    dfs(cur + 1)
    cursum += arr[cur]
    dfs(cur + 1)
    cursum -= arr[cur]

dfs(0)
print(cnt)
