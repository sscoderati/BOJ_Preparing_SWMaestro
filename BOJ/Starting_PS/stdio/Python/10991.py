n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i), sep ='', end='')
    for j in range(1, i):
        print('* ', sep='', end='')
    print('*')
