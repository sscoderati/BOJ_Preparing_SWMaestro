import sys
input = sys.stdin.readline

num1, base = map(str, input().split())
base = int(base)
cnt = 0
num2 = 0
for i in num1[::-1]:
    if i.isdigit():
        convert = int(i)
    else:
        convert = ord(i) - 55
    num2 += (convert * (base ** cnt))
    cnt += 1
print(num2)