import sys
input = sys.stdin.readline

n = int(input())
conference = []
for _ in range(n):
    s, e = map(int, input().split())
    conference.append((s, e))
conference.sort(key = lambda x: (x[1], x[0]))
cnt = 1
end = conference[0][1]
for i in range(1, n):
    if conference[i][0] >= end:
        cnt += 1
        end = conference[i][1]
print(cnt)
