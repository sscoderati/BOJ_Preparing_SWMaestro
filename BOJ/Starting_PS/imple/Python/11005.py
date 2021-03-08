import sys
input = sys.stdin.readline

num1, base = map(int, input().split())
num2 = ""

while num1:
    x = num1 % base
    convert = str(x) if x < 10 else chr(x + 55)
    num2 += convert
    num1 //= base

print("".join(num2[::-1]))