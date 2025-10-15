#methods

str1=input("Enter a string:")

print("Your string:",str1)

print("string in capitalize:",str1.capitalize())

print("String in lowercase:",str1.lower())

print("string in uppercase:",str1.upper())
print("String in swapcase:",str1.swapcase())

print(f"Is {str1} lowercase?:{str1.islower()}")

print(f"Is {str1} uppercase?:{str1.isupper()}")


str2="This is Python version 3.13.7"
str3="Python4"
str4="17"
#isalnum() -check if string has alphabet & numbers
print(f"{str2} is a num? {str2.isalnum()}")
print(f"{str3} is a num? {str3.isalnum()}")
print(f"{str4} is a num? {str4.isalnum()}")

#isalpha() - only alphabets
str5="abc"
print(f"{str5} is a alpha? {str5.isalpha()}")


#isdigit() - only digits
str6="abc"
print(f"{str6} is a alpha? {str6.isdigit()}")


#isspace() - only empty space
str7="  "
print(f"{str7} is isspace()? {str7.isspace()}")

#startswith()
start=input("Enter string for startswith check:")
print(f"{str2} is startswith()? {str2.startswith(start)}")


#endswith()
str8="Hello world from SVGU"
end=input("Enter string for endswith check:")
print(f"{str8} is endswith()? {str8.endswith(end)}")

#find()-return index if substring is found ,  if not found returns -1.
str9="Hello world from SVGU"
find=input("Enter string for find():")
print(f"{find} is in {str9} find()? {str9.find(find)}")

#index()

#count
str10="Hello Hello world from SVGU"
word=input("Enter string that repeats:")
print(f"{word} is repeat in {str10} count()? {str10.count(word)}")
