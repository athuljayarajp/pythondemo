char=input("enter a sentance:")
char=char.split()
final_list=[]
for i in char:
    if i.istitle():
        final_list.append(i)
print(final_list)        