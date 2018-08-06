n = int(input())
i = 0
diction = []
ansver = []
while n > i:
    a = input().lower()
    #print(a)
    diction.append(a)
    i += 1
l = int(input())
#print(diction)
i = 0
while l > i:
    st = input().lower()
    i += 1
    for j in st.split():
        if j not in diction:
            if j not in ansver:
                ansver.append(j)
#print(ansver)
for j in ansver:
    print(j)
