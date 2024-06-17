# Write a python program that takes a list of numbers and returns their sum.
l1=str(input("Enter elements of list with a space:"))
list1=l1.split()
list1= [int(num) for num in list1]
print("List:", list1)  
sum=0
for x in range(0,len(list1)):
    sum=sum+list1[x]

print("The sum of elements in the list is:",sum)
