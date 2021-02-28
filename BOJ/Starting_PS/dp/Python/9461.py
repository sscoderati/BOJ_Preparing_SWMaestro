import sys
input = sys.stdin.readline

t = int(input())

dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 3
for i in range(5, 101):
    dp[i] = dp[i - 1] + dp[i - 5]
for _ in range(t):
    n = int(input())
    print(dp[n - 1])
