t = int(input())
k = 0
arr = [0]

for i in range(1, 2**16):
    arr.extend((i**2-i+1, i**2+1))
def binary_search(left, right):
    while True:
        mid = (left + right) // 2
        if arr[mid] <= k and k < arr[mid + 1]:
            return mid
        elif k < arr[mid]:
            right = mid
        else:
            left = mid
for i in range(t):
    x, y = map(int, input().split())
    k = y - x
    result = binary_search(0, len(arr))
    print(result)

