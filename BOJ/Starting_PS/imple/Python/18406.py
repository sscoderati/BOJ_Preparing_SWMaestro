import sys
input = sys.stdin.readline

n = input()
mid = int(len(n) / 2)
end = int(len(n))
front = n[0 : mid]
back = n[mid : end]
lucky = 0
straight = 0
for i in range(mid):
    lucky += int(front[i])
for i in range(mid):
    straight += int(back[i])
if lucky == straight:
    print("LUCKY")
else:
    print("READY")
