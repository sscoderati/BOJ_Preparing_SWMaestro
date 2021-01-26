import sys
input = sys.stdin

n, k = map(int, input.readline().strip().split())
value = []
cnt = 0

for i in range(n):
    tmp = int(input.readline().strip())
    value.append(tmp)

value.sort(reverse = True)

for i in range(len(value)):
    if k == 0:
        break
    else:
        cnt += k // value[i]
        k %= value[i]

print(cnt)
