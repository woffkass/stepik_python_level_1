a = int(input())
b = int(input())
s = 0
n = 0
av = 0
for i in range(a,b+1):
    if i % 3 == 0:
        s += i
        n += 1
av = s / n
print(av)