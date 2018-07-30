s = 0
p = 0
while True:
    a = int(input())
    p += a * a
    s += a
    if s == 0:
        print(p)
        break
    