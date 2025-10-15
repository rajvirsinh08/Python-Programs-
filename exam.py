items1=[]
positive=[]
while True:
    print("\n\n\n\n1.add all the items in a list")
    print("2.Retrive only positive numbers from list of numbers.")
    print("3.Ask user to insert a new value in list.")
    print("4.sort the list in descending order")
    print("5.print total number of elements in list")
    print("6.Exit\n")

    choice=int(input("Enter your choice:"))

    if(choice==1):
        n=int(input("How many items add into list"))
        for i in range(1,n+1):
            el=int(input(f"Enter number{i}:"))
            items1.append(el)
        print(items1)
    elif(choice==2):
        print(items1)
        print("Positive numbers:")
        for p in items1:
            if(p>0):
                positive.append(p)
        print(positive)
                
    elif(choice==3):
        ask=input("You want to insert a new value in list(yes/no):")

        if(ask=="yes"):
            print(items1)
            n=int(input("How many items add into list you want"))
            for i in range(1,n+1):
                add=int(input(f"Enter number{i}:"))
                items1.append(add)
            print(items1)
        elif(ask=="no"):
            print("Ok. you can continue...")
 
    elif(choice==4):
        items1.sort(reverse=True)
        print(items1)
    elif(choice==5):
        count=0
        print(items1)
        for c in items1:
            count+=1
        print("Total number of elements in list:",count)
    elif(choice>6):
        print("Invalid choice.Please enter valid choice!")
    elif(choice==6):
        break
