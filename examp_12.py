a = int(input())
b = int(input())
m = a
if b > m:
    m = b

while m <= a * b:
    if (m % a == 0) and (m % b == 0):
        print(m)
        m = a * b + 1
    m += 1
