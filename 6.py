# Write a program that reads the content of a text file and prints it to the console.
with open('file1.txt', 'r') as file:
        for line in file:
            print(line)