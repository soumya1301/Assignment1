# Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result. 
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operator=str(input("Enter the operator:"))
if operator=="+":
    sum=num1+num2
    print("The sum of the two numbers is", sum)
elif operator=="-":
    diff=num1-num2
    print("The sum of the two numbers is", diff)
elif operator=="*":
    prod=num1*num2
    print("The sum of the two numbers is", prod)
elif operator=="/":
    if num1 or num2 !=0:
        div=num1/num2
        print("The sum of the two numbers is", div)
    else:
        print("Divison not possible")