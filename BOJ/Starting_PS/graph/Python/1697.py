from collections import deque
MAX = 100001

def bfs(arr, n, k):
    q = deque()
    q.append(n)

    while q:
        i = q.popleft()

        if i == k:
            return arr[i]

        for j in (i - 1, i + 1, 2 * i):
            if 0 <= j < MAX and arr[j] == 0:
                arr[j] = arr[i] + 1
                q.append(j)

n, k = map(int, input().split())
trace = [0] * MAX
print(bfs(trace, n, k))
"""방정식 풀이 : 오답
n, k = map(int, input().split())
time = 0
if n == 0:
    n += 1
    time += 1
if n < k:
    while 2 * n < k:
        n *= 2
        time += 1
    while n != k:
        if abs(k - ((n - 1) * 2)) < abs(k - ((2 * n) - 1)):
            n -= 1
            time += 1
        else:
            n *= 2
            time += 1
            if n > k:
                time += n - k
                break
    print(time)
elif n > k:
    print(abs(k - n))
else:
    print(time)
"""
