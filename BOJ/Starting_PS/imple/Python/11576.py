a, b = map(int, input().split())
n = int(input())
num = list(map(int, input().split()))

res = []
m = 0

for i in range(len(num)):
    m = m + (num.pop() * (a ** i))

while m:
    res.append(m % b)
    m //= b

while res:
    print(res.pop(), end=' ')
