"""count()를 이용한 풀이: 시간초과
import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

count = []
for i in range(m):
    count.append(card.count(target[i]))
print(*count)"""
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def count_by_range(array, left, right):
    idx_l = bisect_left(array, left)
    idx_r = bisect_right(array, right)
    return idx_r - idx_l

n = int(input())
card = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

card.sort()
count = []

for i in range(m):
    count.append(count_by_range(card, target[i], target[i]))
print(*count)
