import math
a, b = map(int, input().split())
g = math.gcd(a, b)
print(str(1) * g)
