import math
s = list(map(int, input()))
cnt = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        cnt += 1
if cnt % 2 == 0:
    cnt /= 2
else:
    cnt = math.ceil(cnt / 2)
cnt = int(cnt)
print(cnt)

