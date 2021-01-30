import sys

input = sys.stdin.readline

n = int(input().strip())
DB = [[0] * 2 for _ in range(n)]

for i in range(n):
    age, name = map(str, input().strip().split())
    DB[i] = int(age), name

DB.sort(key = lambda x: x[0])

for i in range(n):
    print(*DB[i])
