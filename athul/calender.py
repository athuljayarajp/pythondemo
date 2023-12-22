d={31:['jan','march','may','july','aug','oct','dec'],
   30:['april','june','sep','nov'],
   28:'feb',
   29:'feb'}
n=input("enter the month name:")
if n in d [31]:
    print("31days")
elif n in d[30]:
    print("30days") 
elif n in d[29]:
    print("29 days")
elif n in d [28]:
    print("28days") 
else:
    print("invalid month")  
days=int(input("enter day:"))
if days==31:
    print(d[31])
elif days==30:
    print(d[30])
elif days==28:
    print(d[28])
elif days==29:
    print(d[29]) 
else:
    print("invalid" )                    


