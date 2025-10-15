#Types of Actual Arguments(Function call)
#1.Positional - arguments are passed as per sequence/position
#2.Keyword-arguments are passed by keywords
#3.Default-arguments's values are assigned by default
#last arguments can be as default.
'''
def display(rno,name,gender="",age=0):
    print("Roll no:",rno)
    print("Name:",name)
    print("Gender:",gender)
    print("Age:",age)

display(rno=101,age=22,name="Rajvir",gender="Male")
display(102,"Jaimin","Male")
display(103,"Devprint("Roll no:",rno)")
'''
#4.Variable Length
def add(*num):
    sum=0
    for i in num:
        if(type(i)==int or type(i)==float):
            sum+=i
    print("Sum is :",sum);

add(1,2,3,4,22,33,44,"ABC",True)

#passing group of elements(list,tuple)
'''def show(val):
    print("Your entered Value:",val);
list1=[11,22,33,34,44,55,"ABC","Jay",True]
show(list1)'''


'''def add(val):
    sum=0
    for i in val:
        if(type(i)==int or type(i)==float):
            sum+=i
    print("Sum is :",sum);
list1=[11,22,33,34,44,55,"ABC","Jay",True]
add(list1)
'''
'''
def add(val):
    sum=0
    for i in val:
        if(type(i)==int or type(i)==float):
            sum+=i
    print("Sum is :",sum);
list1=input("Enter int element separeted by space:").split();
integer=[]
print(list1)
for elem in list1:
    if(elem.isdigit()):
        elem=int(elem)
        integer.append(elem)
print(integer)
add(integer)

'''
