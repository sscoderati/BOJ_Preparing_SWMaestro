import sys
input = sys.stdin.readline

dp = [0] * 13
dp[0] = 1
dp[1] = 1

n = int(input())
for i in range(2, n + 1):
    dp[i] = i * dp[i - 1]

print(dp[n])
