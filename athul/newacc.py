accounts={}
data=[]
amount=0
account_no=100000

def manadd () :
     name=input('enter your name:')
     conatct=int(input('enter your contact number:'))
     age=int(input('enter your age:'))
     id_proof=input('enter id proof details:')
     accounts['name']=name
     accounts['contact']=conatct
     accounts['age']=age
     accounts['id_proof']=id_proof
     accounts['account_no']=account_no
     accounts['amount']=amount
     data.append(accounts.copy())
     account_no +=1 
     print("") 
def view():
      no_of_accounts=1
      for i in data:
          print("user details of account",no_of_accounts)
          print('-'*15)
          for j,k in i.items():
             print(j,":",k)
             no_of_accounts+=1 
             print(" ")
             print(" ")
def debit():
    account_no=int(input("enter your account no:")) 
    for i in data:
        if i ['account_no']==account_no:
         amount=int(input("enter the amount to withdraw:"))
         i['amount']-= amount  
        print(amount,"is been debited")
def credit():
     account_no=int(input("enter your account no:"))  
     for i in data:
         if i['account_no']==account_no:
                       amount=int(input("enter the amount to deposit:"))
     i['amount']+= amount 
     print(amount,"is been deposited")
                                          

     