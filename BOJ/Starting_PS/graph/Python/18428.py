from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(str,input().split())) for _ in range(n)]
teachers = []
spaces = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

def check(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if board[x][y] == 'S':
        return True

find = False

for a, b in teachers:
    if check(a - 1, b) or check(a, b - 1) or check(a + 1, b) or check(a, b + 1):
        break
    else:
        for data in combinations(spaces, 3):
            for x, y in data:
                board[x][y] = 'O'
            if not process():
                find = True
                break
            for x, y in data:
                board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
