figur = input()
if figur == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print(s)
elif figur == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = a * b
    print(s)
elif figur == 'круг':
    pi = 3.14
    a = int(input())
    s = pi * a ** 2
    print(s)