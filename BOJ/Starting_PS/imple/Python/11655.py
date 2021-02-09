import sys
input = sys.stdin.readline

s = input().rstrip()
s = list(s)

for i in range(len(s)):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        s[i] = ord(s[i]) + 13
        if s[i] > 90:
            s[i] = chr(s[i] - 26)
        else:
            s[i] = chr(s[i])
    elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
        s[i] = ord(s[i]) + 13
        if s[i] > 122:
            s[i] = chr(s[i] - 26)
        else:
            s[i] = chr(s[i])
    else:
        continue
print(''.join(s))
