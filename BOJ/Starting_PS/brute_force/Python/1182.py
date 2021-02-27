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
"""
틀린 풀이 : 부분합 계산해서 풀려고 했는데 왜 틀렸지...?
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]
for i in array:
    sum_value += i
    prefix_sum.append(sum_value)

cnt = 0
for right in range(1, len(prefix_sum)):
    for left in range(1, right):
        partial = prefix_sum[right] - prefix_sum[left - 1]
        length = right - (left - 1)
        if length > 0 and partial == s:
            cnt += 1
print(cnt)
"""
