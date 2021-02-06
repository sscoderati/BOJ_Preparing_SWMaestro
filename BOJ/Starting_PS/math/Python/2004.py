import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

def two_Counter(n):
    cnt = 0
    while n != 0:
        n = math.floor(n / 2)
        cnt += n
    return cnt

def five_Counter(n):
    cnt = 0
    while n != 0:
        n = math.floor(n / 5)
        cnt += n
    return cnt

tcnt = two_Counter(n) - two_Counter(m) - two_Counter(n - m)
fcnt = five_Counter(n) - five_Counter(m) - five_Counter(n - m)
tzero = min(tcnt, fcnt)

print(tzero)
