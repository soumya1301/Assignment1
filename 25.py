# Write a program that copies the contents of one text file to another. 
with open('file1.txt','r') as a, open('file2.txt','a') as b:
    for line in a:
        b.write(line)