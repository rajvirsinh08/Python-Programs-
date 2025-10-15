#syntax- lambda argument:expression
'''
ans=lambda n1,n2:n1+n2
print("addition is :",ans(10,20))

square=lambda n1:n1*n1
print("square:",square(9))

cube=lambda n1:n1*n1*n1
print("cube:",cube(9))

product=lambda n1,n2:n1*n2
print("product:",product(9,10))

swap = lambda n1, n2: (n2, n1)
n1= 9
n2=19
print("Before Swapped:", n1, n2)

n1, n2 = swap(n1, n2)
print("After Swapped:", n1, n2)
'''
#syntax:filter(lambda,sequence)
'''
list1=[]
no=int(input("Till how many numbers:"))
for n in range(1,no+1):
    list1.append(n)
print(list1)
even=filter(lambda no:no%2==0,list1)
print("Even numbers:",list(even))

even=tuple(filter(lambda no:no%2==0,list1))
print("Even numbers:",even)

odd=filter(lambda no:no%2!=0,list1)
print("Odd numbers:",list(odd))

odd=tuple(filter(lambda no:no%2!=0,list1))
print("Odd numbers:",odd)'''

#list using range function

#tuple - odd no
#list - only vowels
'''
text1="Rajvir"
vowels=list(filter(lambda char:char in "aeiouAEIOU",text1))

print(f"Vowels in {text1} are {vowels}")'''

#map=process each element and stores in new list
#syntax:map(lambda,sequence)
'''list1=[1,2,3,4,5]

square=map(lambda elem:elem*elem,list1)
print(list1)
print("Square:",list(square))
square=tuple(map(lambda elem:elem*elem,list1))
print("Square:",square)
'''

#salary-10% increment
'''
salary=[1000,2000,2500,2200]

incre=map(lambda sal:sal+sal*0.10,salary)
print("Original salary:",salary)
print("Incremented salary:",list(incre))
'''


#reduce - reduce the list/tuple into single value
#syntax: reduce(lambda,seq)
from functools import reduce
list1=list(range(1,11))
'''print(list1)
list1=[1,2,3]
ans=reduce(lambda no1,no2:no1+no2,list1)
print(ans)
''' 

#product of all elements of list
product=reduce(lambda no1,no2:no1*no2,list1)
print(product)
