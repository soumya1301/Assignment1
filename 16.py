# Write a program in python that counts the frequency of each character in a string. 
str1=str(input("Enter the string:"))
val=0
for x in str1:
    if x==x:
        val=+1
    else:
        val=val
print(val)

