from collections import deque
import sys
input = sys.stdin.readline

dp = [0] * 501
dp[0] = 1
dp[1] = 1

n = int(input())
cnt = 0
for i in range(2, n + 1):
    dp[i] = i * dp[i - 1]

s = deque(str(dp[n]))
while s.pop() == '0':
    cnt += 1

print(cnt)
