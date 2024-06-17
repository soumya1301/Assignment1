# Write a python program that counts the occurrences of a specific element in a list.
l1=str(input("Enter elements of list with a space:"))
y=int(input("Enter the specific element:"))
list1=l1.split()
list1= [int(num) for num in list1]
print("List:", list1)  
count=0
for x in list1:
    if y==x:
        count=count+1
print("The element",y,"occurs",count,"times")
