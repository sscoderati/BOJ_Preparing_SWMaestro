import sys

input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.idx = 0
        self.list = []

    def push(self, n):
        self.list.append(n)
        self.idx += 1

    def pop(self):
        if self.size() == 0:
            return -1
        index = self.idx - 1
        ret = self.list[index]
        del self.list[index]
        self.idx -= 1
        return ret

    def size(self):
        return self.idx

    def empty(self):
        if self.idx == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.idx != 0:
            return self.list[-1]
        else:
            return -1

n = int(input())
stack = Stack()
for _ in range(n):
    keyword = input().strip().split()
    command = keyword[0]

    if command == 'push':
        stack.push(keyword[1])
    elif command == 'pop':
        print(stack.pop())
    elif command == 'size':
        print(stack.size())
    elif command == 'empty':
        print(stack.empty())
    elif command == 'top':
        print(stack.top())
