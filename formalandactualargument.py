'''#Func tions: block of code that can be reusable
#smaller chunks of code to manage the program
#function is created using def(define) keyword

#global variable - used everywhere in the program

def get(rno,name,add,contact,dob,mail,gender):
    #local variable-variable used in function only
    rno=int(input("enter enroll no.:"))
    name=input("enter name.:")
    add=input("enter address.:")
    contact=int(input("enter contact.:"))
    dob=input("enter dob.:")
    mail=input("enter email.:")
    gender=input("enter gender.:")
def display():
         print("enroll no:",rno)
         print("name:",name)
         print("address:",add)
         print("contact:",contact)
         print("dob:",dob)
         print("email:",mail)
         print("gender:",gender)
#call the function
rno=int(input("enter enroll no.:"))
name=input("enter name.:")
add=input("enter address.:")
contact=int(input("enter contact.:"))
dob=input("enter dob.:")
mail=input("enter email.:")
gender=input("enter gender.:")
get(rno,name,add,contact,dob,mail,gender)
display()'''
def add(a,b):
    sum=a+b
    print("addition:",sum)


n1=int(input("ENter any number:"))
n2=int(input("Enter any number:"))
#add=n1+n2
#print("Addition=",add)
add(n1,n2)

f1=float(input("Enter float number:"))
f2=float(input("Enter float number:"))
#addf=f1+f2
#print("Addition of float value:",addf)
add(f1,f2)

s1=input("enter any string:")
s2=input("enter any string:")
#adds=s1+s2
#print("Add strings:",adds)
add(s1,s2)














