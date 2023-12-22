n=int(input("Enter the number of steps: "))
lists=[[1],[2]]
for i in range(n):
    new_list=[]
    for j in lists:
        sum=0
        list_str=" "
        for k in range(len(j)):
            sum += j[k]
            if k>0:
                list_str += " + "
            list_str += str(j[k])+" stairs "
            if sum==n:
                print(list_str)
                break
            elif sum<n:
                new_list.append(j+[1])
                new_list.append(j+[2])
            lists=new_list
