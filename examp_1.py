
x = int(input())
hs = int(input())
ms = int(input())
x = x + hs*60 + ms
h = x // 60
m = x % 60
print(h)
print(m)
