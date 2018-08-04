dic = {}
i = 0
n = int(input())
while n > i:
    st = input()
    data = st.split(';')
    if data[0] not in dic:
        dic[data[0]] = [0,0,0,0,0]
    if data[2] not in dic:
        dic[data[2]] = [0,0,0,0,0]
    if data[1] > data[3]:
        dic[data[0]][0] += 1
        dic[data[0]][1] += 1
        dic[data[0]][4] += 3
        dic[data[2]][0] += 1
        dic[data[2]][3] += 1
    elif data[1] < data[3]:
        dic[data[2]][0] += 1
        dic[data[2]][1] += 1
        dic[data[2]][4] += 3
        dic[data[0]][0] += 1
        dic[data[0]][3] += 1
    else:
        dic[data[0]][0] += 1
        dic[data[0]][2] += 1
        dic[data[0]][4] += 1
        dic[data[2]][0] += 1
        dic[data[2]][2] += 1
        dic[data[2]][4] += 1
    i += 1
for key, value in dic.items():
    print(key,":", value[0],' ',value[1],' ',value[2],' ',value[3],' ',value[4], sep='')