n = int(input())
time = list(map(int, input().split()))
time.sort()
min_time = 0
result = 0
for i in range(n):
    min_time += time[i]
    result += min_time
print(result)
