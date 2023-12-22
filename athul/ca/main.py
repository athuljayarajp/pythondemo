import platform
import datetime
#a=int (input("enter your number:"))
#b=int (input("enter your number:"))
#r1.add(a,b)
x=datetime.datetime.now()
print("system name:" ,platform.node())
print("os name:",platform.system())
print("processor name:",platform.processor())
print("architecture:",platform.architecture())
print("date:",x.strftime("%d/%m/%Y"))
print("time:",x.strftime("%I:%M:%S "))
