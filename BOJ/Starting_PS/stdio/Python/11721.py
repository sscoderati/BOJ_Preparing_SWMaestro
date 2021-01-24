s = input()
sep = []
tmp = ""
cnt = 0
for i in range(len(s)):
    tmp += s[i]
    cnt += 1
    if cnt == 10 or cnt < 10 and len(s) - i < 10:
        sep.append(tmp)
        tmp = ""
        cnt = 0
    else:
        continue
for i in sep:
    print(i)
