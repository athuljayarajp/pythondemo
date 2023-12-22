list1=set(input("enter a list1:"))
list2=set(input("enter a list2:"))
list3=[]
for i in list1:
    if i in list2:
        list3.append([i])
print(list3)        
