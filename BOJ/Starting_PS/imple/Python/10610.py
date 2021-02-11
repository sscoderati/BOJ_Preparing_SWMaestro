import sys
input = sys.stdin.readline

n = list(input().rstrip())
n.sort(reverse = True)

tmp = ''
for i in range(len(n)):
    tmp += n.pop(0)

if int(tmp) % 30 == 0:
    print(tmp)
else:
    print(-1)
