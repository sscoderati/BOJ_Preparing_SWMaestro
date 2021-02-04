import sys

input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.list = []

    def push(self, n):
        self.list.append(n)

    def pop(self):
        if self.size() == 0:
            return -1
        return self.list.pop()

    def size(self):
        return len(self.list)

    def empty(self):
        if len(self.list) == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.size() != 0:
            return self.list[-1]
        else:
            return -1
    def clear(self):
        return self.list.clear()

T = int(input())
stack = Stack()
ex = 0
for _ in range(T):
    s = input().rstrip()
    for i in range(len(s)):
        if s[i] == '(':
            stack.push(s[i])
        elif s[i] == ')':
            if stack.pop() == -1:
                print('NO')
                ex = 1
                break
    if stack.empty() == 1 and ex != 1:
        print('YES')
    elif stack.empty() == 0 and ex != 1:
        print('NO')
    ex = 0
    stack.clear()
