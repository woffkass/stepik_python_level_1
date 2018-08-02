with open('dataset_3363_2 (1).txt') as inf:
    s1 = inf.readline().strip()
#print(s1)
s2 = ''
char = ''
i = 0
num = ''
while i < len(s1):
    char = s1[i]
    #print(char)
    i += 1
    #print(i)
    while '0' <= s1[i] and s1[i] <= '9':
        num += s1[i]
        i += 1
        if i >= len(s1):
            break
    s2 += char * int(num)
    #print(i)
    num = ''
with open('result.txt', 'w') as ouf:
    ouf.write(s2)