import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0 for _ in range(n + 1)]
parents[1] = 1

def dfs(now, tree, parents):
    for node in tree[now]:
        if parents[node] == 0:
            parents[node] = now
            dfs(node, tree, parents)
dfs(1, tree, parents)
for i in range(2, n + 1):
    print(parents[i])
