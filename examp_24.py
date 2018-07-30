mat =[]
while True:
    string = input()
    if string == 'end':
        break
    s = [int(i) for i in string.split()]
    mat.append(s)    
for i in range(len(mat)):    
    for j in range(len(mat[i])):
        result = mat[i-1][j] + mat[i+1-len(mat)][j] + mat[i][j-1] + mat[i][j+1-len(mat[i])]
        print(result, end = ' ')
    print()
