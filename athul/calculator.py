number1=int(input("enter number1:"))
number2=int(input("enter number2:"))
operation=input("enter operation:")
if operation=='+':
    sum=number1+number2
    print("the sum is:",sum)
elif operation=='-':
    sub=number1-number2
    print("the substraction value is:",sub)
elif operation=='*':
    mul=number1*number2
    print("the multipliaction value is:",mul)
elif operation=='/':
    div=number1/number2
    print("the division value is:",div) 
elif operation=='//':
    floor=number1//number2
    print("the floor division is:",floor) 
elif operation=='**':
    expo=number1**number2
    print("the exponent value is ",expo)
else:print("invalid")    


