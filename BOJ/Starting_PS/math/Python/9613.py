from itertools import combinations
import math
import sys
input = sys.stdin.readline

t= int(input())

for _ in range(t):
    array = list(map(int, input().split()))
    array = array[1:]
    combi = list(combinations(array, 2))
    result = 0
    for i in range(len(combi)):
        x, y = combi[i]
        result += math.gcd(x, y)
    print(result)
