lst = [int(i) for i in input().split()]
x = int(input())

if not x in lst:
    print('Отсутствует')
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=' ')
        flag = 1
