import sys
input = sys.stdin.readline

def push(c):
    q.append(c)

def pop():
    if len(q) == 0:
        print(-1)
    else:
        print(q.pop(0))

def size():
    print(len(q))

def empty():
    if len(q) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(q) == 0:
        print(-1)
    else:
        print(q[0])

def back():
    if len(q) == 0:
        print(-1)
    else:
        print(q[-1])

n = int(input())
q = []

for _ in range(n):
    c = list(input().split())

    if c[0] == 'push':
        push(c[1])
    elif c[0] == 'pop':
        pop()
    elif c[0] == 'size':
        size()
    elif c[0] == 'empty':
        empty()
    elif c[0] == 'front':
        front()
    elif c[0] == 'back':
        back()
