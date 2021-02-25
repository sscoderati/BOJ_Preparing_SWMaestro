n = int(input())

for i in range(1, n + 1):
    if i in (1, n):
        print(' ' * (n - i),'*' * (2 * i - 1), sep='')
    else:
        print(' ' * (n - i), '*', ' ' * (2 * (i - 1) - 1), '*', sep='')
