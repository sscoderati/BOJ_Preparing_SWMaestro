import sys
input = sys.stdin.readline

a, b, c, d = input().strip().split()
n = a + b
m = c + d
print(int(n) + int(m))
