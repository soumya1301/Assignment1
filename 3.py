#Write a python program that calculates the factorial of a given number
num=int(input("Enter the number whose factorial is to be calculated:"))
if num<0:
    print("Factorial of negative number cannot be calculated.")
else:
    fact=1
    for i in range(1, num + 1):
        fact *= i
    print("The factorial of",num,"is",fact)