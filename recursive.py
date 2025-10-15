#recursive function-function that call itself
#factorial
'''def fact(num):
    if(num<0):
        return "not possible"
    elif(num==0):
        return 1
    else:
        return num*fact(num-1)
val=5
result=fact(val)
print(f"Factorial of {val} is: {result}")
'''

#recursive function-function that call itself
#factorial
def fib(num):
    if(num<0):
        return "not possible"
    elif(num==0):
        return 1
    else:
        a=0
        b=1
        for _ in range(2,num+1):
            a=b
            b=a+b
    
val=55
result=fib(val)
print(f"fibonacci of {val} is: {result}")
