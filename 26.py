# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix. 
str1=str(input("Enter the string:"))
prefix=str(input("Enter the prefix:"))
suffix=str(input("Enter the suffix:"))

x=str1.startswith(prefix)
y=str1.endswith(suffix)
if x==True:
    print("The string does start with the prefix")
else:
    print("The string does not start with the prefix")
if y==True:
    print("The string does end with the suffix")
else:
    print("The string does not end with the suffix")