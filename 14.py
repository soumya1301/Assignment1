# Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines. 
while True:
    lines=input("Enter the lines:")
    if lines==" ":
        print("An empty line is entered.")
        break