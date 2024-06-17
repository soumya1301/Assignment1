# Write a python program that calculates the sum of the digits of a given number.
num = int(input("Enter a number: ")) 
if num < 0:
    print("Please enter a non-negative integer.")
sum= 0
while num > 0:
    digit = num % 10 
    sum+= digit  
    num //= 10  
print("The sum of digits of the number is",sum)
