# https://suri78.tistory.com/151
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rect = [list(map(int, input().strip())) for _ in range(n)]
res = 0

# |||
for i in range(1, m - 1):
    for j in range(i + 1, m):
        r1 = sum([rect[a][b] for a in range(n) for b in range(i)])
        r2 = sum([rect[a][b] for a in range(n) for b in range(i, j)])
        r3 = sum([rect[a][b] for a in range(n) for b in range(j, m)])
        res = max(res, r1 * r2 * r3)

# ||
# --
for i in range(1, m):
    for j in range(1, n):
        r1 = sum([rect[a][b] for a in range(j) for b in range(i)])
        r2 = sum([rect[a][b] for a in range(j) for b in range(i, m)])
        r3 = sum([rect[a][b] for a in range(j, n) for b in range(m)])
        res = max(res, r1 * r2 * r3)

# --
# ||
for i in range(1, n):
    for j in range(1, m):
        r1 = sum([rect[a][b] for a in range(i) for b in range(m)])
        r2 = sum([rect[a][b] for a in range(i, n) for b in range(j)])
        r3 = sum([rect[a][b] for a in range(i, n) for b in range(j, m)])
        res = max(res, r1 * r2 * r3)

# =|
for i in range(1, n):
    for j in range(1, m):
        r1 = sum([rect[a][b] for a in range(i) for b in range(j)])
        r2 = sum([rect[a][b] for a in range(i, n) for b in range(j)])
        r3 = sum([rect[a][b] for a in range(n) for b in range(j, m)])
        res = max(res, r1 * r2 * r3)

# |=
for i in range(1, n):
    for j in range(1, m):
        r1 = sum([rect[a][b] for a in range(i) for b in range(j, m)])
        r2 = sum([rect[a][b] for a in range(i, n) for b in range(j, m)])
        r3 = sum([rect[a][b] for a in range(n) for b in range(j)])
        res = max(res, r1 * r2 * r3)

# ≡
for i in range(1, n - 1):
    for j in range(i + 1, n):
        r1 = sum([rect[a][b] for a in range(i) for b in range(m)])
        r2 = sum([rect[a][b] for a in range(i, j) for b in range(m)])
        r3 = sum([rect[a][b] for a in range(j, n) for b in range(m)])
        res = max(res, r1 * r2 * r3)
print(res)