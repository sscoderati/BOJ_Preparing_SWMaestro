import sys

input = sys.stdin.readline

n = int(input())
num_list = [0] * 10001

for i in range(n):
    num_list[int(input())] += 1
for i in range(10001):
    sys.stdout.write('%s\n' % i * num_list[i])
