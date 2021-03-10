n, k = map(int, input().split())
tree = [0] * (4 * n)

def init(node, s, e):
    if s == e:
        tree[node] = 1
        return tree[node]
    m = (s + e) // 2
    tree[node] = init(node * 2, s, m) + init(node * 2 + 1, m + 1, e)
    return tree[node]

def update(node, s, e, i):
    tree[node] -= 1
    if s == e:
        return False
    else:
        m = (s + e) // 2
        if i <= m:
            return update(node * 2, s, m, i)
        else:
            return update(node * 2 + 1, m + 1, e, i)

def query(node, s, e, o):
    if s == e:
        return s
    m = (s + e) // 2
    if o <= tree[node * 2]:
        return query(node * 2, s, m, o)
    else:
        return query(node * 2 + 1, m + 1, e, o - tree[node * 2])


init(1, 1, n)
idx = 1
print("<",end='')
for i in range(n):
    size = n - i
    idx += k - 1

    if idx % size == 0:
        idx = size
    elif idx > size:
        idx %= size

    num = query(1, 1, n, idx)
    update(1, 1, n, num)

    if i == n - 1:
        print(num, end='')
    else:
        print(", ", end='')
print(">", end='')
print()
