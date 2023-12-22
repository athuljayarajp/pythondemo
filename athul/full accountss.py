import newacc
# accounts={}
# data=[]
# amount=0
account_no=100000
cond="y"
while(cond):
    print("welcome to bank")
    print("choose a option:","m.manager","a.accountant","c.client")
    option=input("enter your option:")
    if option.lower()=="m":
        print("choose a option:","1. add","2. view","3.debit","4.credit")
        option=input("enter a option:")
        if option.lower()=="1":
          #   name=input('enter your name:')
          #   conatct=int(input('enter your contact number:'))
          #   age=int(input('enter your age:'))
          #   id_proof=input('enter id proof details:')
            
          #   accounts['name']=name
          #   accounts['contact']=conatct
          #   accounts['age']=age
          #   accounts['id_proof']=id_proof
          #    accounts['account_no']=account_no
          #   accounts['amount']=amount
          #   data.append(accounts.copy())
          #   account_no +=1 
          #   print("") 
          newacc.manadd()
        if option.lower()=="2":
             newacc.view()
             
          #     no_of_accounts=1
          #     for i in data:
          #          print("user details of account",no_of_accounts)
          #          print('-'*15)
          #          for j,k in i.items():
          #               print(j,":",k)
          #          no_of_accounts+=1 
          #          print(" ")
          #          print(" ")

        if option.lower()=="3": 
          #    account_no=int(input("enter your account no:")) 
          #    for i in data:
          #         if i ['account_no']==account_no:
          #               amount=int(input("enter the amount to withdraw:"))
                        newacc.debit()
                    #     i['amount']-= amount  
                    #     print(amount,"is been debited")
                    #     break

        if option.lower()=="4":
          #    account_no=int(input("enter your account no:"))  
          #    for i in data:
          #         if i['account_no']==account_no:
          #              amount=int(input("enter the amount to deposit:"))
                       newacc.credit()
                    #    i['amount']+= amount 
                    #    print(amount,"is been deposited")
                    #    break

    if option.lower()=="a": 
         print("choose a option:","1.debit","2.credit","3.view")
         option=input("enter your option:") 
         if option.lower()=="1":
              account_no=int(input("enter your account no:")) 
              for i in data:
                  if i ['account_no']==account_no:
                        amount=int(input("enter the amount to withdraw:"))
                        i['amount']-= amount  
                        print(amount,"is been debited")
                        break
         if option.lower()=="2":
              account_no=int(input("enter your account no:"))  
              for i in data:
                  if i['account_no']==account_no:
                       amount=int(input("enter the amount to deposit:"))
                       i['amount']+= amount 
                       print(amount,"is been deposited")
                       break

         if option.lower()=="3": 
                #no_of_accounts=1
                for i in data:
                  # print("user details of account",no_of_accounts)
                   print('-'*15)
                   for i in data:
                        print(i)
                   #for j,k in i.items():
                       # print(j,":",k)
                  # no_of_accounts+=1 
                  # print(" ")
                  # print(" ") 
                   break

    if option.lower()=="c":
          account_no=int(input("enter your account no:"))
          for i in data:
               if i["account_no"]==account_no:
                    print(i)
               #     print("user details of account",no_of_accounts)
               #     print('-'*15)
               #     for j,k in i.items():
               #          print(j,":",k)
               #     no_of_accounts+=1 
               #     print(" ")
               #     print(" ") 
                   

                                 



