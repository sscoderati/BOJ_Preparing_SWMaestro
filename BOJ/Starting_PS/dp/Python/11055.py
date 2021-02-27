import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    tmp = 0
    for j in range(i):
        if array[j] < array[i]:
            tmp = max(tmp, dp[j])
    dp[i] = array[i] + tmp
print(max(dp))
""" dp테이블을 array에서 그대로 가져다 쓰는 풀이
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [x for x in array]

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))
"""
