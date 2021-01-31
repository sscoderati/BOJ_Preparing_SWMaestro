import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
num = set(arr)
num = list(num)
num.sort()
max_num = []
max_num.append(num[0])
for i in range(1, len(num)):
    for j in range(len(max_num)):
        if arr.count(num[i]) > arr.count(max_num[j]):
            max_num.pop()
            max_num.append(num[i])
        elif arr.count(num[i]) == arr.count(max_num[j]):
            max_num.append(num[i])
        else:
            continue
max_num.sort()
print(max_num[0])
