import sys
input = sys.stdin.readline

def push_front(c):
    d.insert(0, c)

def push_back(c):
    d.append(c)

def pop_front():
    if len(d) == 0:
        print(-1)
    else:
        print(d.pop(0))

def pop_back():
    if len(d) == 0:
        print(-1)
    else:
        print(d.pop(-1))

def size():
    print(len(d))

def empty():
    if len(d) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(d) == 0:
        print(-1)
    else:
        print(d[0])

def back():
    if len(d) == 0:
        print(-1)
    else:
        print(d[-1])

n = int(input())
d = []

for _ in range(n):
    c = list(input().split())

    if c[0] == 'push_front':
        push_front(c[1])
    elif c[0] == 'push_back':
        push_back(c[1])
    elif c[0] == 'pop_front':
        pop_front()
    elif c[0] == 'pop_back':
        pop_back()
    elif c[0] == 'size':
        size()
    elif c[0] == 'empty':
        empty()
    elif c[0] == 'front':
        front()
    elif c[0] == 'back':
        back()
