s = [int(i) for i in input().split()]
s = sorted(s)
s.append(' ')
count = 1
i = 0
while i < len(s) - 1:

    if s[i] == s[i+1]:
        count += 1

    else:
        if count > 1:
            print(s[i], end=' ')
        count = 1
    i += 1