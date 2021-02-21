import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
balloon = deque(list(map(int, input().split())))
num = deque([i for i in range(1, n + 1)])
result = []
for _ in range(n):
    m = balloon.popleft()
    result.append(num.popleft())
    if m > 0:
        m -= 1
    balloon.rotate(m)
    num.rotate(m)
print(*result)
