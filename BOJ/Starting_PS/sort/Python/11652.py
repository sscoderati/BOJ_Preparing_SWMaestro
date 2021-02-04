import sys
input = sys.stdin.readline

n = int(input())
arr = {}
for i in range(n):
    a = int(input())
    if a in arr:
        arr[a] += 1
    else:
        arr[a] = 1

arr = sorted(arr.items(), key = lambda x : (-x[1], x[0]))
print(arr[0][0])


"""n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
amount = []
for i in range(len(arr) - 1):
    if arr[i] != arr[i + 1] or i == len(arr) - 2:
        amount.append((arr[i],arr.count(arr[i])))
amount.sort(key = lambda x : x[1], reverse = True)
print(amount[0][0])시간초과"""

#리스트랑 count함수가 문제인 것 같다 너무느림..

"""n = int(input())
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
시간 초과 판정"""
