print(oct(int(input(), 2))[2::])
"""import sys
input = sys.stdin.readline

n = input().rstrip()
n = n[::-1]
total = 0
for i in range(len(n)):
    if n[i] == '1':
        total += 2 ** i
    else:
        continue
print(format(total,'o'))
시간초과"""
