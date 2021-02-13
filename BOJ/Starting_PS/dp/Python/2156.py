import sys
input = sys.stdin.readline

n = int(input())
wine = [0]
dp = [0] * (n + 1)

for i in range(1, n + 1):
    wine.append(int(input()))

if n == 1:
    dp[1] = wine[1]
else:
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 1])

print(dp[n])
