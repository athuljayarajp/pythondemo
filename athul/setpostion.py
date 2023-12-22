
list1=[6,7,9,2]
sum=9
sum_list=[]
for i in range(len(list1)):
    #print("this from outer loop ",i)
    for j in range(i+1,len(list1)):
     if list1[i]+list1[j]==sum:
      print(list1[i],list1[j]) 
      print(list1.index(list1[i]),list1.index(list1[j]))