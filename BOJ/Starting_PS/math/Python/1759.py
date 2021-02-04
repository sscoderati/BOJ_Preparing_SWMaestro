from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' '))

arr = input().split(' ')
arr.sort()

for password in combinations(arr, l):
    cnt = 0
    for i in password:
        if i in vowels:
            cnt += 1
    if cnt >= 1 and cnt <= l - 2:
        print(''.join(password))
