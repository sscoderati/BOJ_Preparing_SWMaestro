s = input()
sep = []
tmp = ""

for i in range(len(s)):
    tmp += s[i]
    if len(tmp) == 10:
        sep.append(tmp)
        tmp = ""
    elif i == len(s) - 1:
        sep.append(tmp)

for i in sep:
    print(i)
