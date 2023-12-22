
accounts={}
data=[]

account_no=100000
cond="y"
while(cond):
    print("welcome to bank")
    print("choose a option:","add","view","debit","credit")
    option=input("enter a option:")
    if option.lower()=="add":

     name=input('enter your name:')
     conatct=input('enter your contact number:')
     age=input('enter your age:')
     id_proof=input('enter id proof details:')
    
     accounts['name']=name
     accounts['contact']=conatct
     accounts['age']=age
     accounts['id_proof']=id_proof
     accounts['account_no']=account_no
     
     data.append(accounts.copy())
     account_no +=1 

     print("") 
     print(data)
    if option.lower()=="view":
       #bal=input("enter your account number:")
       for i in data:
          #account_no==data
            print(i)
         #  print("user details",accounts)
         #  for j,k in i.items():
         #      print(j,":",k)
          #print("")
    #if option.lower()=="debit":
      #  debit=input("enter your account no:")
   #     for x in data:
   #        print(x)
   #     withdraw=input("enter the ammount to debit")

   #     balance={}
   #     accounts["account_no"]=account_no  
   #  if option.lower()=="credit":
   #     credit=input("enter account no:") 
   #     balance={}  
   #     accounts["account_no"]=account_no
    c=input("do you want to continue 'y' or 'n' :")
    if c!=cond:
       breakpoint         




