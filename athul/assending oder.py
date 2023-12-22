n=[17,14,2,1,5]
temp=0
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if (n[i]>n[j]):
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
        print(n)

