import sys
from collections import deque

input = sys.stdin.readline

s = deque(input().rstrip())
suffix = []
tmp = ''
for _ in range(len(s)):
    tmp += s.pop()
    suffix.append(tmp[::-1])
suffix.sort()
for i in range(len(suffix)):
    print(suffix[i])
