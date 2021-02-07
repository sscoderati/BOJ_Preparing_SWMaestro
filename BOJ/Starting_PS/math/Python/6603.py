import sys
from itertools import combinations
input = sys.stdin.readline
inp = [1]
while sum(inp) != 0:
    inp = list(map(int, input().split()))
    del inp[0]
    for x in combinations(inp, 6):
        print(*x)
    print()
