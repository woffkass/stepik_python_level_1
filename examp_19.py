s = [int(i) for i in input().split()]
r = []
if len(s) > 1:
    for i in range(len(s)):
        if i == 0:
            r.append(s[1] + s[-1])
        elif i == len(s)-1:
            r.append(s[len(s)-2] + s[0])
        else:
            r.append(s[i-1] + s[i+1])

else:
    print(s[0])
for i in r:
    print(i, end=' ')
