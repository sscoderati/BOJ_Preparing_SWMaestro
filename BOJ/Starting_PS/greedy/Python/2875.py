import sys

input = sys.stdin.readline

def group_num(n, m):
    group_num = 0
    while n >= 2 and m >= 1:
        n -= 2
        m -= 1
        group_num += 1
    return group_num

n, m, k = map(int, input().strip().split())
group_num = group_num(n, m)
left = n - group_num * 2 + m - group_num

if k <= left:
    print(group_num)
else:
    while k > left:
        if group_num <= 0:
            print(0)
            sys.exit()
        else:
            group_num -= 1
            left += 3
    print(group_num)
