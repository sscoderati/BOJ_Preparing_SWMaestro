import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
rotation = []
check = True
for _ in range(k):
    a, b = map(str, input().split())
    rotation.append((int(a), b))
wheel = deque(['?' for _ in range(n)])

for i in range(k):
    r, alpha = rotation[i]
    wheel.rotate(r)
    if wheel[0] != '?':
        if wheel[0] == alpha:
            continue
        check = False
    else:
        wheel[0] = alpha

for i in range(n):
    if wheel[i] == '?':
        continue
    for j in range(i + 1, n):
        if wheel[i] == wheel[j]:
            check = False
            break

if check == False:
    print('!')
else:
    print("".join(wheel))
