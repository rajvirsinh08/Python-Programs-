#arithmatic menu
import arithmaticfunctions
#from arithmaticfunctions import add,sub,mul,div
from arithmaticfunctions import *
while True:
    print("1.addition")
    print("2.substraction")
    print("3.multiply")
    print("4.division")
    print("5.exit")

    choice=int(input("Enter choice:"))
    no1=int(input("Enter any number:"))
    no2=int(input("Enter any number:"))
    
    if(choice==1):
        print(add(no1,no2))
    elif(choice==2):
        print(sub(no1,no2))
    elif(choice==3):
        print(mul(no1,no2))
    elif(choice==4):
        print(div(no1,no2))
