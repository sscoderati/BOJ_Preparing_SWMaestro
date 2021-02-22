n = int(input())
balloon = list(map(int, input().split()))

num = [i for i in range(1, n + 1)]
result = []
idx = 0

m = balloon.pop(idx)
result.append(num.pop(idx))

while len(balloon) > 0:
    if m > 0:
        idx = (idx + (m - 1)) % len(balloon)
    else:
        m = m * -1
        idx = len(balloon) - idx - 1
        idx = len(balloon) - ((idx + m) % len(balloon)) - 1
    m = balloon.pop(idx)
    result.append(num.pop(idx))

print(*result)
