n=int(input("enter a  number:"))
lastdigit =n%10
if(lastdigit%3==0):
    print("last digit of given number is",lastdigit and "divisible by 3")
else:
    print("las digit is not divisible by 3")    
