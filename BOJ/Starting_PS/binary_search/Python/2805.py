import sys
input = sys.stdin.readline

n, m = map(int, input().split())
timber = list(map(int, input().rstrip().split()))

start = 1
end = sum(timber)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in timber:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
