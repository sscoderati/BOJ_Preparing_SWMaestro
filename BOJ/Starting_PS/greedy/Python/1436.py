import sys
input = sys.stdin.readline

n = int(input())
title = 666

if n == 1:
    print(title)
else:
    t = 1
    while t != n:
        title += 1
        if '666' in str(title):
            t += 1
    print(title)
