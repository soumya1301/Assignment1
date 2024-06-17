# Write a python program that checks if two strings are anagrams of each other.
str1=str(input("Enter the first string:"))
str2=str(input("Enter the second string:"))
if(sorted(str1)== sorted(str2)):
    print("The strings are anagrams.") 
else:
    print("The strings aren't anagrams.")