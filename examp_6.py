a = float(input())
b = float(input())
operator = input()
if operator == '+':
    print(a+b)
elif operator =='-':
    print(a-b)
elif operator =='/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a/b)
elif operator =='*':
    print(a*b)
elif operator =='mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a%int(b))
elif operator =='pow':
    print(a**b)
elif operator =='div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a//int(b))