import sys
input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        dp[i][j] = dp[i][j] + max(up_left, up)
print(max(dp[n - 1]))
