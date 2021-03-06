import sys
input = sys.stdin.readline

code = input().strip()
array = [int(i) for i in list(code)]
length = len(code)

if code[0] != '0':
    dp = [0] * (length + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, length + 1):
        one = array[i - 1]
        two = 10 * array[i - 2] + array[i - 1]
        if one > 0:
            dp[i] += dp[i - 1]
        if 10 <= two <=26:
            dp[i] += dp[i - 2]
        dp[i] %= 1000000
    print(dp[length])
else:
    print(0)
