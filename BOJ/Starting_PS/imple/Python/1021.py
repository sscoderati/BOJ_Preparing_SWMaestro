import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
index = list(map(int, input().rstrip().split()))
queue = deque([i for i in range(1, n + 1)])
min_count = 0

for i in index:
    if i == queue[0]:
        queue.popleft()
        continue
    left_count = queue.index(i)
    right_count = len(queue) - left_count
    if left_count <= right_count:
        queue.rotate(-left_count)
        queue.popleft()
        min_count += left_count
    else:
        queue.rotate(right_count)
        queue.popleft()
        min_count += right_count
print(min_count)
