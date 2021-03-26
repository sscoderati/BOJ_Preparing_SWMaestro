from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(s, 0)])
    visited = [0] * (f + 1)
    visited[s] = 1
    while queue:
        q, button = queue.popleft()
        if q == g:
            return button

        button += 1
        if q - d >= 1 and visited[q - d] == 0:
            visited[q - d] = 1
            queue.append((q - d, button))
        if q + u <= f and visited[q + u] == 0:
            visited[q + u] = 1
            queue.append((q + u, button))
    return -1

f, s, g, u, d = map(int, input().split())
res = bfs()
print(res if res >= 0 else "use the stairs")
