a1 = 0
a2 = 0
a3 = 0
n = 0
with open('dataset_3363_4.txt') as inf:
    for line in inf:
        a = line.split(';')
        b1 = int(a[1])
        b2 = int(a[2])
        b3 = int(a[3])
        #print(b1, b2, b3)
        print((b1+b2+b3)/3)
        a1 += b1
        a2 += b2
        a3 += b3
        n += 1
print(a1/n, a2/n, a3/n)