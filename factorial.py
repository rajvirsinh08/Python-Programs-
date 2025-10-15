#factorial

n=int(input("Enter no:"))

fact=1

for n in range(1,n+1):
    fact=fact*n
print(f"Factorial of (n) is :{fact}")


#reverse string
#forward indexing
str1=input("Enter any string to reverse string:")
length=len(str1)

rev=''
for i in range(length-1,-1,-1):
    rev+=str1[i]
print(f"Reverse string using forward indexing is :{rev}")

#backward indexing
#rev2=''
#for j in range(0,length):
 #   rev2+=str1[length-1-j]
#print(f"Reverse string using backward indexing is :{rev2}")

 
