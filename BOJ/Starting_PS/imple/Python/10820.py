import sys
input = sys.stdin.readline

while True:
    n = input().rstrip('\n')
    if not n:
        break
    lower = 0
    upper = 0
    num = 0
    blank = 0
    for i in range(len(n)):
        if ord(n[i]) == 32:
            blank += 1
        elif ord(n[i]) >= 48 and ord(n[i]) <= 57:
            num += 1
        elif ord(n[i]) >= 65 and ord(n[i]) <= 90:
            upper += 1
        elif ord(n[i]) >= 97 and ord(n[i]) <= 122:
            lower += 1
        else:
            continue
    print(lower, upper, num, blank)
