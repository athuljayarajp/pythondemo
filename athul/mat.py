
x=[[2,5,3],[4,3,7]]
y=[[2,2,5],[3,3,2]]
output=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range (len(x[0])):
        output[i][j]=x[i][j]+y[i][j]
for k in output:
    print(k)        