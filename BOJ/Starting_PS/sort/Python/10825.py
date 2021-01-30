import sys

input = sys.stdin.readline

n = int(input())
scoreDB = [[0] * 4 for _ in range(n)]

for i in range(n):
    name, G, Y, S = map(str, input().strip().split())
    scoreDB[i] = name, int(G), int(Y), int(S)

scoreDB.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(scoreDB[i][0])
