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
n = int(input())
num_list = []
result = []
stack = Stack()
idx = 0

for i in range(n):
    num_list.append(int(input()))

for i in range(n):
    stack.push(i + 1)
    result.append('+')
    while idx < n and stack.top() == num_list[idx]:
        stack.pop()
        result.append('-')
        idx += 1
if not stack.empty():
    print("NO")
else:
    for r in result:
        print(r)
