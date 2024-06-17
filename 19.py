# Write a python program that removes all punctuation from a given string. 
str1=str(input("Enter the string:"))
print("The original string is",str1)
punc='''!()-[]{};:'\",<>./?@#$%^&*_~'''
for ele in str1:
    if ele in punc:
        str1 = str1.replace(ele, "")
print("The string after punctuation filter : " + str1)