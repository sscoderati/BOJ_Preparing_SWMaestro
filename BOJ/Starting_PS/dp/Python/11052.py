import sys
input = sys.stdin.readline

n = int(input())
price = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(n + 1):
    for j in range(i + 1):
        dp[i] = max(dp[i], dp[i - j] + price[j])
print(dp[n])
