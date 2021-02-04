import math

m, n = map(int, input().split())
arr = [True for i in range(1000001)]
arr[1] = 0

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for i in range(m, n + 1):
    if arr[i]:
        print(i)
