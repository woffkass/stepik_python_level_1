s = input()
s = s + ' '
count = 1
str2 = ''
i = 0
while i < len(s) - 1:
    if s[i] == s[i+1]:
        count += 1
    else:
        str2 = str2 + s[i] + str(count)
        count = 1
    i += 1
print(str2)