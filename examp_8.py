a = int(input())
b = int(input())
c = int(input())
if a >= b:
    if a >= c:
        if b >= c:
            print(a)
            print(c)
            print(b)
        else:
            print(a)
            print(b)
            print(c)
            
    else:
        print(c)
        print(b)
        print(a)
else:#a<b
    if a <= c:
        if b >= c:
            print(b)
            print(a)
            print(c)
        else:
            print(c)
            print(a)
            print(b)
    else:
        print(b)
        print(c)
        print(a)