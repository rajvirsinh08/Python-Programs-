#Dictionary-unordered set of key and value pair
#pair of key(index) and value
#syntax:dict={key:value}
#item=pair of key and value
#meaningfull data
#key=immutable
#value=mutable
#key should be unique
#empty dictionary
'''dict2={}

dict1={'rno':101,'name':"jaimin",'marks':33}

student={101:"ali",102:"piyush",103:"jaimin",102:"manjul"}

teacher={'id':None,'name':None,'edu':None}
print(dict1)
print(student)
print(teacher)

#accessing dictionary through keys(index)
print(dict1['name'])
print(student[101])


#operation

#1 .updateion
teacher['edu']='PHD'
print(teacher)

#2. deletion
#del dict1 #whole dictionary
del teacher['id']
#print(dict1) this line give error after delete dictionary
 #give error Traceback (most recent call last):
  File "D:/dictionary.py", line 35, in <module>
    print(dict1)
NameError: name 'dict1' is not defined
print(teacher)


#Function of dictionary
#1. len- total no. of items{keys & values}
print("Length of student dictionary:",len(student))

#Methods of dictionary
#1. keys()-return all the keys of dictionary
#print("All keys of student dictionary:",student.keys())
emp={'HR':None,'Sales':None,'Marketing':None}
for keys in emp.keys():
    emp[keys]=int(input(f"Enter {keys} value:"))
print(emp)
'''
#2.values()
'''
money={'vansh':500,'jay':200,'piyush':1000}
print(money)
for value in money.values():
    
    value+=500
    print(value)
print(money)'''
    
#3.items()
'''
#4.clear()
print("Student dictionary:",student)
student.clear()
print("After clearing ,Student dictionary:",student)

#5.copy()-copy all items from one dictionary to another
dict2=dict1.copy()
print("dictionary1:",dict1)
print("dictionary2:",dict2)
'''

#6. get(key)-get the value of the specified key
'''
money={'vansh':500,'jay':200,'piyush':1000}
print(money)
key=input("enter any key to get the value:")
val=money.get(key)
if(val is None):
    print("key not found")
else:
    print(f"{key}:{val}")'''

#7. pop(key)- delete the item of specified key
'''
money={'vansh':500,'jay':200,'piyush':1000}
print(money)
key=input("enter any key for delete:")
val=money.get(key)
if(val is None):
    print("key not found")
else:
    money.pop(key)
    print(f"Deleted :{key}:{val}")
print(money)'''

#8. popitem()-delete the last item
money={'vansh':500,'jay':200,'piyush':1000}
print(money)
money.popitem()
print("after pop last item:",money)

#9 update()-update the dictionary from another
#similar to copy method
money1={'vansh':500,'jay':200,'piyush':1000}
money2={'jaimin':500,'ali':200,'nayan':1000}
print(money1)
print(money2)

money2.update(money1)
print(money1)
print(money2)
#10.fromkeys(sequence)- convert sequence into dictionary
'''
dict1={}
list1=[101,11,222,33,44]

dict1=dict1.fromkeys(list1)
print(dict1)
'''

