import sys
input = sys.stdin.readline

n, k = map(int, input().split())

seg = [0] * (4 * n)
r = []

def update(pos, val, node, x, y):
    if pos < x or y < pos:
        return seg[node]
    if x == y:
        return seg[node]
    m = (x + y) // 2
    seg[node] = update(pos, val, node * 2, x, m) + update(pos, val, node * 2 + 1, m + 1, y)
    return seg[node]

def query(val, node, x, y):
    if x == y:
        return x
    m = (x + y) // 2
    if seg[node * 2] >= val:
        return query(val, node * 2, x, m)
    else:
        return query(val - seg[node * 2], node * 2 + 1, m + 1, y)

def squery(lo, hi, node, x, y):
    if y < lo or hi < x:
        return False
    if lo <= x and y <= hi:
        return seg[node]
    m = (x + y) // 2
    return squery(lo, hi, node * 2, x, m) + squery(lo, hi, node * 2 + 1, m + 1, y)

for i in range(1, n + 1):
    update(i, 1, 1, 1, n)
mod = n - 1
r.append(k)
update(k, 0, 1, 1, n)
for i in range(2, n + 1):
    x = (squery(1, r[-1], 1, 1, n) + k) % mod
    if not x:
        x = mod
    r.append(query(x, 1, 1, n))
    update(r[-1], 0, 1, 1, n)
    mod -= 1
print('<', ', '.join(map(str, r)), '>', sep='')
