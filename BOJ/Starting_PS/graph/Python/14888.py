import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
operands = list(map(int, input().split()))

mini = int(1e9)
maxi = int(-1e9)

def dfs(cur, num):
    global operands, mini, maxi
    if cur == n:
        mini = min(mini, num)
        maxi = max(maxi, num)
    else:
        if operands[0] > 0: # +
            operands[0] -= 1
            dfs(cur + 1, num + array[cur])
            operands[0] += 1
        if operands[1] > 0: # -
            operands[1] -= 1
            dfs(cur + 1, num - array[cur])
            operands[1] += 1
        if operands[2] > 0: # *
            operands[2] -= 1
            dfs(cur + 1, num * array[cur])
            operands[2] += 1
        if operands[3] > 0: # /
            operands[3] -= 1
            dfs(cur + 1, int(num / array[cur]))
            operands[3] += 1

dfs(1, array[0])
print(maxi)
print(mini)
