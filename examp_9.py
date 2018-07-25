a = int(input())
if 10 < a%100 < 20:
    print(a, 'программистов')
elif a%10 == 1:
    print(a, 'программист')
elif 1 < a%10 < 5:
    print(a, 'программиста')
else:
    print(a, 'программистов')
