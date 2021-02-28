import sys
input = sys.stdin.readline

n, m = map(int, input().split())

D = set()
B = set()
for _ in range(n):
    D.add(input())
for _ in range(m):
    B.add(input())
DB = list(D & B)
DB.sort()
cnt = len(DB)
print(cnt)
for i in range(cnt):
    print(DB[i], end='')
