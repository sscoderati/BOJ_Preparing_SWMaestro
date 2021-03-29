import sys
input = sys.stdin.readline

target = int(input())
m = int(input())
if m == 0:
    button = set()
else:
    malbutton = set(input().split())
    button = set(str(x) for x in range(10)).difference(malbutton)

channel = abs(target - 100)
for i in range(1000001):
    flag = True
    for j in str(i):
        if j not in button:
            flag = False
            break
    if flag:
        channel = min(channel, len(str(i)) + abs(target - i))

print(channel)
