import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start = 1
end = house[-1] - house[0]
distance = 0

while start <= end:
    mid = (start + end) // 2
    value = house[0]
    cnt = 1
    for i in range(1, n):
        if house[i] >= value + mid:
            value = house[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        distance = mid
    else:
        end = mid - 1
print(distance)
