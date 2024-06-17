# Write a python program that returns the minimum and maximum values in a list of numbers.
# a=[23,34,67,12,76,100]
l1=str(input("Enter elements of list with a space:"))
list1=l1.split()
list1= [int(num) for num in list1]
print("List:", list1) 
maxval=max(list1)
minval=min(list1)
print("The the maximum value in the list of numbers is",maxval)
print("The the minimum value in the list of numbers is",minval)