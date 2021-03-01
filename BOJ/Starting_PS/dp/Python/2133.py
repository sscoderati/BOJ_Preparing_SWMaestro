import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 31
dp[0] = 1
dp[2] = 3

if n % 2 != 0:
    print(dp[n])
    sys.exit()
else:
    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + 2
        for j in range(2, i - 2, 2):
            dp[i] += dp[j] * 2
print(dp[n])
