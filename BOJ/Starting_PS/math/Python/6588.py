import sys
import math
input = sys.stdin.readline
num = 1000000

prime = [True for _ in range(num + 1)]
prime[1] = False

for i in range(2, int(math.sqrt(num)) + 1):
    if prime[i] == True:
        j = 2
        while i * j <= num:
            prime[i * j] = False
            j += 1
while True:
    n = int(input())
    check = False
    if n == 0:
        break
    for i in range(3, len(prime)):
        if prime[i] and prime[n - i]:
            check = True
            print(str(n) + " = " + str(i) + " + " + str(n - i))
            break
    if check == False:
        print("Goldbach's conjecture is wrong.")
