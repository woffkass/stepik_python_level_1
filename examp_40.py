n = int(input())
i = 0
dx = 0
dy = 0
while n > i:
    a = input().split()
    if a[0] == 'север':
        dy += int(a[1])
    elif a[0] == 'юг':
        dy -= int(a[1])
    elif a[0] == 'восток':
        dx += int(a[1])
    elif a[0] == 'запад':
        dx -= int(a[1])
    i += 1
print(dx, dy)
