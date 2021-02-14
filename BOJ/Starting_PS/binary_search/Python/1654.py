import sys
input = sys.stdin.readline

k, n = map(int, input().split())
cable = [int(input()) for _ in range(k)]
start = 1
end = sum(cable)
result = 0
while start <= end:
    amount = 0
    mid = (start + end) // 2
    amount = sum([x // mid for x in cable])
    if amount < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
