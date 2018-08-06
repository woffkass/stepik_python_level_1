average = [[0, 0] for i in range(11)]
with open('dataset_3380_5.txt') as inf:
    for line in inf:
        a = line.split('\t')
        average[int(a[0])-1][0] += int(a[2])
        average[int(a[0])-1][1] += 1
for i in range(11):
    if average[i][0] == 0:
        print(i+1, '-')
    else:
        print(i+1, average[i][0]/average[i][1]) 
