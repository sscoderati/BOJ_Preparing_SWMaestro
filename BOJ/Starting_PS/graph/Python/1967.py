import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n + 1)]
first_search = [0 for _ in range(n + 1)]
second_search = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dfs(start, graph, search):
    for node, val in graph[start]:
        if search[node] == 0:
            search[node] = search[start] + val
            dfs(node, graph, search)

dfs(1, graph, first_search)
first_search[1] = 0

fval = 0
fnode = 0

for i in range(n + 1):
    if fval < first_search[i]:
        fval = first_search[i]
        fnode = i

dfs(fnode, graph, second_search)
second_search[fnode] = 0
diameter = max(second_search)
print(diameter)
