#count()-returns the no. of repeated items
grocery=['tea','sugar','bread','milk','sugar']
print(grocery)      
item=input("enter item name for count:")
if(item in grocery):
    print(f"{item} repeats for {grocery.count(item)} time")
else:
    print("item not found")

#remove()-delete the elements of list by the object
whichitem=input("Enter the value of remove item:")

for i in grocery:
    if(i==whichitem):
        grocery.remove(i)
print(grocery)

#4. Delete-delete the element
# pop()-delete the elements of list by index
#by default,pop removes last element
items=['watch','smartphone','iphone','mouse','laptop']
print(items)

whichitem=input("Which item you want delete in items?")

if(whichitem in items):
    index=items.index(whichitem)

    deleted=items.pop(index)
    print(f"{deleted} item deleted successfully .After update:")
    print(items)
else:
    print("Item not found")


#5. append()-add element at the end
print(items)
elem=input("Enter item to append:")

if(elem.isdigit()):
    elem=int(elem)
items.append(elem)

print("After append")
print(items)

#6 insert()-add element at specific index

pos=int(input("Enter position to insert:"))
if(pos<=0 or pos>=len(items)):
    print("invalid position")

else:
    ele=input("Enter element to insert:")
    items.insert(pos-1,ele)
    print("after insertion")
    print(items)

#7 reverse()-reverse the positions of all elements in list
list1=[10,50,5,1,20,30,40]
print(list1)
list1.reverse()
print("After reverse")
print(list1)


#8 sort(reverse=False)-sort list in asscending/descending
#list1.sort() #ascending order
list1.sort(reverse=True)#descending order
print("after sorting ")
print(list1)


#9 extend()-joins two list.
l1=[10,20,30]
l2=[40,50]

l1.extend(l2)#l1=l1+l2
print("List1:",l1)
print("List2:",l2)
