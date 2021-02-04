import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0
data = list(range(1, n + 1))

for x in itertools.combinations(data, m):
    cnt += 1
print(cnt)
