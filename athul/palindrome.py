num=int(input("enter a number:"))
temp=num
reversenum=0
while temp !=0:
    digit=temp%10
    reversenum=(reversenum*10)+digit
    temp//=10
if num ==reversenum:
    print("it is palindrome") 
else:
    print("it is not a palindrome")       


    
    

