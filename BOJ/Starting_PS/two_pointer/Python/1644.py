import sys
import math
input = sys.stdin.readline

n = int(input())
prime = [True for _ in range(n + 1)]
prime[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i] == True:
        j = 2
        while i * j <= n:
            prime[i * j] = False
            j += 1

data = []

for i in range(2, n + 1):
    if prime[i]:
        data.append(i)
m = len(data)

cnt = 0
interval_sum = 0
end = 0

for start in range(m):
    while interval_sum < n and end < m:
        interval_sum += data[end]
        end += 1
    if interval_sum == n:
        cnt += 1
    interval_sum -= data[start]
print(cnt)
"""
import sys
import math
input = sys.stdin.readline

n = int(input())
prime = [True for _ in range(n + 1)]
prime[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i] == True:
        j = 2
        while i * j <= n:
            prime[i * j] = False
            j += 1

data = []

for i in range(2, n + 1):
    if prime[i]:
        data.append(i)

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

way = 0
for right in range(len(prefix_sum)):
    for left in range(right + 1):
        partial = prefix_sum[right] - prefix_sum[left - 1]
        if partial == n:
            way += 1
print(way)
투 포인터 미사용 : 시간초과"""
