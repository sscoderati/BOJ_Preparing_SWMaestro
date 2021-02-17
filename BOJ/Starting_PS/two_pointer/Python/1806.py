import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = 0
interval_sum = 0
length = int(1e9)

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += array[end]
        end += 1
    if interval_sum >= s and end - start < length:
        length = end - start
    interval_sum -= array[start]

if length == int(1e9):
    print(0)
else:
    print(length)
"""
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]
for i in array:
    sum_value += i
    prefix_sum.append(sum_value)

min_length = {0}

for right in range(len(prefix_sum)):
    for left in range(right):
        partial = prefix_sum[right] - prefix_sum[left - 1]
        length = right - (left - 1)
        if partial < s:
            continue
        else:
            if 0 in min_length:
                min_length.remove(0)
                min_length.add(length)
            else:
                min_length.add(length)
print(min(min_length))
시간초과. 투 포인터를 사용하지 않았다."""
