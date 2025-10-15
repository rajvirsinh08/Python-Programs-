#List
#Mutable object - can change the value

list1=[11,22,33,44,55]
list2=[101,"BBA","BCA","MCA1","MCA2",22,33]
list3=[22.5,49.4]

#empty
list4=[]

#indexing
#1.Forward-start with 0 (1st element/member)
print(list1[3])

#backward-starts with -1(last element)
print(list1[-4])
#operations

#1 Addition-adds two list.
#creates a new list and adds elements of all list added
add=list1+list2
print(add)

#2. Replication - repetition of list
print(list3*5)

#slicing
print(list1[2:5])
print(list1[-4:-1])
print(list1[-1:-4:-1])#when use for if 5 to 2 index so use -1 [5:2:-1].if 2 to 5 index so only [2:5]
print(list1[::-1])#reverse list print


#4. update-update the element

items=['watch','smartphone','iphone','mouse','laptop']
print(items)

whichitem=input("Which item you want change in items?")

if(whichitem in items):
    index=items.index(whichitem)

    #index=int(input("Enter index to change:"))
    updateditem=input("Enter item for change in items:")

    items[index]=updateditem#if we use [index] only so start with 0.user cant understand start with 0.so we put index-1]

    print("After update:")
    print(items)
else:
    print("Item not found")




#4. Delete-delete the element

#items=['watch','smartphone','iphone','mouse','laptop']
print(items)

whichitem=input("Which item you want delete in items?")

if(whichitem in items):
    index=items.index(whichitem)

    del items[index]
    print(f"item deleted successfully .After update:")
    print(items)
else:
    print("Item not found")


#Functions of List
#1 min()-return minimum value from the list
#2 max()-return maximum value from the list
#3 len()- return length of list

list1=[22,11,66,33]
print("Maximum:",max(list1))
print("Minimum:",min(list1))
print("Length:",len(list1))

#4list()-typecasting
#convert any object to list
tuple1=(11,22,33)
print(tuple1,type(tuple1))

tuple1=list(tuple1)
print(tuple1,type(tuple1))

#tuple() -typecasting for convert any object into tuple
tuple1=tuple(tuple1)
print(tuple1,type(tuple1))

