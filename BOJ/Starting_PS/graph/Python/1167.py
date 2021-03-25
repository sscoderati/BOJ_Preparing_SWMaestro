import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
first_search = [0 for _ in range(n + 1)]
second_search = [0 for _ in range(n + 1)]

for i in range(n):
    vertex = list(map(int, input().split()))
    for i in range(1, len(vertex) // 2):
        graph[vertex[0]].append((vertex[2 * i - 1], vertex[2 * i]))

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
