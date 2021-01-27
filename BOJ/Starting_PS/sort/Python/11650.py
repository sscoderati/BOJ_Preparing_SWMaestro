import sys

input = sys.stdin.readline

n = int(input().strip())
coordinate = [[0] * 2 for _ in range(n)]

for i in range(n):
    x, y = map(int, input().strip().split())
    coordinate[i] = x, y

coordinate.sort(key = lambda x:x[0])
coordinate.sort(key = lambda x:x[1])

for i in range(n):
    print(*coordinate[i])
