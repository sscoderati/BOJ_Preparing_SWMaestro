import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
res = []

while q:
    q.rotate(-k + 1)
    res.append(str(q.popleft()))

print("<" + ", ".join(res) + ">")

"""
from collections import deque

n, k = map(int, input().split())
queue = []
for i in range(1, n + 1):
    queue.append(i)
queue = deque(queue)
print('<', end = '')
for i in range(n):
    for j in range(k - 1):
        queue.append(queue.popleft())
    print(queue.popleft(), end = '')
    if i == n - 1:
        pass
    else:
        print(',', end=' ')
print('>', end ='')
"""
