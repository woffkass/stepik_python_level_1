st_alf = input()
st_key = input()
st1 = input()
st2 = input()
st3 = ''
st4 = ''
for i in range(len(st1)):
    st3 += st_key[st_alf.find(st1[i])]
for i in range(len(st2)):
    st4 += st_alf[st_key.find(st2[i])]
print(st3)
print(st4)