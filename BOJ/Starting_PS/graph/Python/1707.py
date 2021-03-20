from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        idx = q.popleft()
        for i in graph[idx]:
            if not visited[i]:
                visited[i] = ~visited[idx]
                q.append(i)
            else:
                if visited[i] == visited[idx]:
                    return False
    return True

tc = int(input())
for _ in range(tc):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False for _ in range(v + 1)]
    flag = True
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for y in range(1, v + 1):
        if not visited[y]:
            if not bfs(y):
                flag = False
                break
    if flag:
        print("YES")
    else:
        print("NO")
