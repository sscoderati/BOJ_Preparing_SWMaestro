import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
rotation = []
for _ in range(k):
    a, b = map(str, input().split())
    rotation.append((int(a), b))
wheel = deque([0 for _ in range(n)])

for i in range(k):
    r, alpha = rotation[i]
    wheel.rotate(r)
    if wheel[0] == 0:
        wheel[0] = alpha
    elif wheel[0] == alpha:
        continue
    else:
        print("!")
        sys.exit()

while 0 in wheel:
    wheel[wheel.index(0)] = "?"

print("".join(wheel))
