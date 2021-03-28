import sys
input = sys.stdin.readline

target = int(input())
m = int(input())
if m == 0:
    button = set()
else:
    malbutton = set(map(int, input().split()))
    button = set(x for x in range(10)).difference(malbutton)

channel = abs(target - 100)
for i in range(1000001):
    a = set(list(str(i)))
    if not button & a:
        channel = min(channel, len(str(i)) + abs(target - i))
print(channel)
