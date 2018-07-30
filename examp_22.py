a = int(input())
count = 0
number = 1
for i in range(a):
    print(number, end=' ')
    count += 1
    if count >= number:
        number += 1
        count = 0
