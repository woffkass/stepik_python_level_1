n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
count = 1
direct = 'r'
i = 0
j = 0
while count < n * n:
    if direct == 'r':
        if j < len(a[i]) - 1  and a[i][j+1] == 0:
            a[i][j] = count
            count += 1
            j += 1
        else:
            direct = 'd'
    if direct == 'd':
        if i < len(a[i]) - 1 and a[i+1][j] == 0:
            a[i][j] = count
            count += 1
            i += 1
        else:
            direct = 'l'
    if direct == 'l':
        if j > -1 and a[i][j-1] == 0:
            a[i][j] = count
            count += 1
            j -= 1
        else:
            direct = 'u'
    if direct == 'u':
        if j > -1 and a[i-1][j] == 0:
            a[i][j] = count
            count += 1
            i -= 1
        else:
            direct = 'r'
a[i][j] = count
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()