# Write a program that takes a string input from the user and writes it to a text file.
user_input = input("Enter a string to write to the file: ")
filename = 'output.txt'
with open('file2.txt', 'w') as file:
    file.write(user_input)
