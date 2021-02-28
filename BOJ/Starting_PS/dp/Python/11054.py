import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

inc = [1] * n
dec = [1] * n

for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            inc[i] = max(inc[i], inc[j] + 1)
array.reverse()

for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            dec[i] = max(dec[i], dec[j] + 1)
dec.reverse()

bitonic = [1] * n
for i in range(n):
    bitonic[i] = inc[i] + dec[i]
print(max(bitonic) - 1)
