#Func tions: block of code that can be reusable
#smaller chunks of code to manage the program
#function is created using def(define) keyword

#global variable - used everywhere in the program
rno=contact=0
name=add=dob=mail=gender=""
def get():
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
get()
display()
