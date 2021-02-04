from collections import Counter
from string import ascii_lowercase
import sys
input = sys.stdin.readline

s = input().rstrip()
a = list(ascii_lowercase)
c = Counter(s)

for i in range(len(a)):
    print(c[a[i]], end = ' ')
